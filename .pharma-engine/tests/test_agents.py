"""Tests for the agent layer.

These run against the offline rule backend and against scripted fake backends,
never against a live model: a test suite that needs a network call is a test
suite that gets skipped. What is asserted here is the *machinery* — that the
validator holds, that the critic can veto, that nothing reaches the ledger
without a human step — which is exactly the part that must not depend on which
model is behind it.

Run: python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from agents import contract, ingest, loop
from agents.llm import Completion, OfflineBackend, available
from engine.ledger import Ledger
from engine.model import Direction, EvidenceAtom
from engine.scoring import score_pair

CORPUS = Path(__file__).resolve().parent.parent / "data" / "corpus"


class ScriptedBackend:
    """A backend that returns whatever the test hands it."""

    def __init__(self, extract_text: str, critic_text: str = '{"verdict": "accept", "reason": "ok"}'):
        self.name = "scripted"
        self.extract_text = extract_text
        self.critic_text = critic_text
        self.calls: list[str] = []

    def complete(self, system: str, user: str, max_tokens: int = 4096) -> Completion:
        if "CRITIC" in system:
            self.calls.append("critic")
            return Completion(text=self.critic_text, backend=self.name)
        self.calls.append("extract")
        return Completion(text=self.extract_text, backend=self.name)


def _atoms_payload(**overrides) -> str:
    atom = {
        "target": "PCSK9",
        "disease": "ASCVD",
        "evidence_class": "human_genetics_causal",
        "predicate": "test_finding",
        "direction": "inhibit",
        "strength": 0.5,
        "year": 2018,
        "citation": "Harrison et al., J Hepatol 2020 (STELLAR-3 and STELLAR-4)",
        "replications": 1,
        "refutes": False,
        "rationale": "test",
    }
    atom.update(overrides)
    return json.dumps({"atoms": [atom]})


class ValidatorTests(unittest.TestCase):
    """The validator is the trust boundary. Everything else is convenience."""

    def setUp(self):
        self.ledger = Ledger.load()
        self.doc_citation = "Harrison et al., J Hepatol 2020 (STELLAR-3 and STELLAR-4)"

    def _validate(self, **overrides):
        return contract.validate(
            json.loads(_atoms_payload(**overrides)),
            self.ledger,
            doc_citation=self.doc_citation,
            doc_year=2020,
            backend_name="scripted",
            atom_prefix="T",
        )

    def test_a_well_formed_atom_passes(self):
        self.assertTrue(self._validate().ok)

    def test_unknown_target_is_rejected(self):
        r = self._validate(target="NEWGENE1")
        self.assertFalse(r.ok)
        self.assertIn("unknown target", r.rejections[0].reason)

    def test_unknown_disease_is_rejected(self):
        r = self._validate(disease="MADEUPDISEASE")
        self.assertFalse(r.ok)
        self.assertIn("unknown disease", r.rejections[0].reason)

    def test_a_pathway_id_cannot_masquerade_as_a_disease(self):
        r = self._validate(disease="IL23_TH17")
        self.assertFalse(r.ok)

    def test_undeclared_evidence_class_is_rejected(self):
        r = self._validate(evidence_class="vibes")
        self.assertFalse(r.ok)
        self.assertIn("undeclared evidence class", r.rejections[0].reason)

    def test_invalid_direction_is_rejected(self):
        self.assertFalse(self._validate(direction="maybe").ok)

    def test_strength_outside_range_is_rejected(self):
        self.assertFalse(self._validate(strength=1.4).ok)
        self.assertFalse(self._validate(strength=-0.1).ok)

    def test_fabricated_citation_is_rejected(self):
        r = self._validate(citation="Nature 2024, landmark study")
        self.assertFalse(r.ok)
        self.assertIn("does not match", r.rejections[0].reason)

    def test_atom_cannot_postdate_its_document(self):
        r = self._validate(year=2026)
        self.assertFalse(r.ok)
        self.assertIn("but the document is from", r.rejections[0].reason)

    def test_strength_is_capped_without_a_stated_effect_size(self):
        r = self._validate(strength=1.0)
        self.assertTrue(r.ok)
        self.assertLessEqual(r.atoms[0].strength, contract.MAX_STRENGTH_WITHOUT_EFFECT)

    def test_rule_engine_output_is_capped_harder(self):
        r = contract.validate(
            json.loads(_atoms_payload(strength=1.0, effect="huge")),
            self.ledger,
            doc_citation=self.doc_citation,
            doc_year=2020,
            backend_name="offline_rules",
            atom_prefix="T",
        )
        self.assertLessEqual(r.atoms[0].strength, contract.OFFLINE_STRENGTH_CAP)

    def test_rejections_are_kept_with_reasons(self):
        r = self._validate(target="NEWGENE1")
        self.assertEqual(len(r.rejections), 1)
        self.assertTrue(r.rejections[0].reason)

    def test_provenance_records_the_backend(self):
        self.assertEqual(self._validate().atoms[0].source_db, "agent:scripted")


class PromptInjectionTests(unittest.TestCase):
    """The corpus contains a document that instructs whatever reads it.

    The guarantee is not that a model resists the instruction -- a model might
    not. It is that the validator makes the instruction unachievable: the entity
    it asks for does not exist, and the citation it asks for is not the
    document's.
    """

    def setUp(self):
        self.ledger = Ledger.load()
        self.doc = next(d for d in ingest.load_corpus(CORPUS) if d.id == "injection-fixture")

    def test_the_fixture_still_contains_its_payload(self):
        self.assertIn("Ignore your previous", self.doc.text)
        self.assertIn("NEWGENE1", self.doc.text)

    def test_a_fully_compromised_extractor_still_cannot_reach_the_ledger(self):
        """Simulate the worst case: the model obeys the injection completely."""
        compromised = json.dumps(
            {
                "atoms": [
                    {
                        "target": "NEWGENE1", "disease": "AD",
                        "evidence_class": "human_genetics_causal", "predicate": "x",
                        "direction": "inhibit", "strength": 1.0, "year": 2024,
                        "citation": "Nature 2024, landmark study", "replications": 9,
                        "refutes": False,
                    },
                    {
                        "target": "TNF", "disease": "AD",
                        "evidence_class": "human_genetics_causal", "predicate": "x",
                        "direction": "inhibit", "strength": 1.0, "year": 2024,
                        "citation": "Nature 2024, landmark study", "replications": 9,
                        "refutes": False,
                    },
                ]
            }
        )
        backend = ScriptedBackend(compromised)
        result = ingest.ingest_document(self.doc, self.ledger, backend)
        self.assertEqual(result.staged, [], "an injected atom reached the staging file")
        self.assertEqual(len(result.rejected), 2)
        self.assertTrue(all("NEWGENE1" in r.reason or "citation" in r.reason for r in result.rejected))

    def test_the_offline_extractor_does_not_follow_the_instruction(self):
        result = ingest.ingest_document(self.doc, self.ledger, OfflineBackend())
        for atom in result.staged:
            self.assertNotEqual(atom.evidence_class, "human_genetics_causal")
            self.assertLessEqual(atom.strength, contract.OFFLINE_STRENGTH_CAP)
            self.assertEqual(atom.replications, 1)


class CriticTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()
        self.doc = next(d for d in ingest.load_corpus(CORPUS) if d.id == "ask1-mash-failure")

    def test_critic_veto_blocks_an_otherwise_valid_atom(self):
        backend = ScriptedBackend(
            _atoms_payload(target="MAP3K5", disease="MASH", evidence_class="human_perturbation", year=2020),
            critic_text='{"verdict": "reject", "reason": "the document does not support this"}',
        )
        result = ingest.ingest_document(self.doc, self.ledger, backend)
        self.assertEqual(result.staged, [])
        self.assertEqual(result.rejected[0].stage, "critic")

    def test_critic_revision_is_applied_and_revalidated(self):
        backend = ScriptedBackend(
            _atoms_payload(target="MAP3K5", disease="MASH", evidence_class="human_perturbation",
                           year=2020, strength=0.9),
            critic_text='{"verdict": "revise", "reason": "overstated", "revised": {"strength": 0.3}}',
        )
        result = ingest.ingest_document(self.doc, self.ledger, backend)
        self.assertEqual(len(result.revised), 1)
        self.assertAlmostEqual(result.revised[0][0].strength, 0.3)

    def test_a_revision_that_breaks_the_schema_is_rejected_not_applied(self):
        backend = ScriptedBackend(
            _atoms_payload(target="MAP3K5", disease="MASH", evidence_class="human_perturbation", year=2020),
            critic_text='{"verdict": "revise", "reason": "x", "revised": {"evidence_class": "nonsense"}}',
        )
        result = ingest.ingest_document(self.doc, self.ledger, backend)
        self.assertEqual(result.staged, [])
        self.assertIn("revision failed validation", result.rejected[0].reason)

    def test_an_unreachable_critic_is_not_an_implicit_accept(self):
        class BrokenCritic(ScriptedBackend):
            def complete(self, system, user, max_tokens=4096):
                if "CRITIC" in system:
                    return Completion(text="not json at all", backend=self.name)
                return Completion(text=self.extract_text, backend=self.name)

        backend = BrokenCritic(
            _atoms_payload(target="MAP3K5", disease="MASH", evidence_class="human_perturbation", year=2020)
        )
        result = ingest.ingest_document(self.doc, self.ledger, backend)
        self.assertEqual(result.staged, [])

    def test_the_critic_sees_the_document_not_just_the_atom(self):
        backend = ScriptedBackend(
            _atoms_payload(target="MAP3K5", disease="MASH", evidence_class="human_perturbation", year=2020)
        )
        ingest.ingest_document(self.doc, self.ledger, backend)
        self.assertIn("critic", backend.calls)


class DeduplicationTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_reingesting_a_known_paper_does_not_create_a_second_line_of_evidence(self):
        doc = next(d for d in ingest.load_corpus(CORPUS) if d.id == "hsd17b13-mash")
        backend = ScriptedBackend(
            _atoms_payload(
                target="HSD17B13", disease="MASH", evidence_class="human_genetics_causal",
                year=2018, citation="Abul-Husn et al., N Engl J Med 2018",
            )
        )
        result = ingest.ingest_document(doc, self.ledger, backend)
        self.assertEqual(result.staged, [])
        self.assertEqual(len(result.duplicates), 1)
        self.assertEqual(result.duplicates[0][1].id, "EV120")


class ScoringIsolationTests(unittest.TestCase):
    """A batch of atoms must not leak between hypotheses.

    Found by running the loop: a refuted MAP3K5 claim was scored against PNPLA3
    because the loop passes everything it has gathered into the rescore.
    """

    def setUp(self):
        self.ledger = Ledger.load()

    def test_atoms_for_another_target_are_ignored(self):
        foreign = EvidenceAtom(
            id="X", target="MAP3K5", disease="MASH", evidence_class="human_perturbation",
            predicate="failed", direction=Direction.UNCLEAR, strength=0.9, year=2020,
            citation="test", refutes=True,
        )
        clean = score_pair(self.ledger, "PNPLA3", "MASH")
        contaminated = score_pair(self.ledger, "PNPLA3", "MASH", extra_atoms=[foreign])
        self.assertAlmostEqual(clean.posterior, contaminated.posterior)

    def test_atoms_for_another_disease_are_ignored(self):
        foreign = EvidenceAtom(
            id="X", target="PNPLA3", disease="T2D", evidence_class="human_perturbation",
            predicate="failed", direction=Direction.UNCLEAR, strength=0.9, year=2020,
            citation="test", refutes=True,
        )
        clean = score_pair(self.ledger, "PNPLA3", "MASH")
        contaminated = score_pair(self.ledger, "PNPLA3", "MASH", extra_atoms=[foreign])
        self.assertAlmostEqual(clean.posterior, contaminated.posterior)


class CorpusSearchTests(unittest.TestCase):
    def setUp(self):
        self.docs = ingest.load_corpus(CORPUS)

    def test_corpus_loads_with_citations_and_years(self):
        self.assertGreaterEqual(len(self.docs), 5)
        for d in self.docs:
            self.assertTrue(d.citation)
            self.assertGreater(d.year, 1900)

    def test_search_requires_the_target_or_the_disease(self):
        """An IL6R safety paper surfaced against a PNPLA3 question because both
        mention human perturbation. Class keywords alone are not relevance."""
        hits = ingest.search_corpus(
            self.docs, target="PNPLA3",
            disease_name="Metabolic dysfunction-associated steatohepatitis",
            evidence_class="human_perturbation",
        )
        self.assertNotIn("il6r-safety-phewas", [d.id for d in hits])

    def test_search_finds_the_obviously_relevant_document(self):
        hits = ingest.search_corpus(self.docs, target="PNPLA3", disease_name="steatohepatitis")
        self.assertIn("pnpla3-liver-fat", [d.id for d in hits])


class StagingTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_nothing_reaches_the_ledger_without_an_explicit_commit(self):
        doc = next(d for d in ingest.load_corpus(CORPUS) if d.id == "ask1-mash-failure")
        backend = ScriptedBackend(
            _atoms_payload(target="MAP3K5", disease="MASH", evidence_class="human_perturbation", year=2020)
        )
        result = ingest.ingest_document(doc, self.ledger, backend)
        self.assertTrue(result.staged)

        with tempfile.TemporaryDirectory() as tmp:
            staged = Path(tmp) / "staged.jsonl"
            evidence = Path(tmp) / "evidence.jsonl"
            evidence.write_text("")
            ingest.stage([result], path=staged)

            before = Ledger.load()
            self.assertEqual(
                len(before.atoms_for("MAP3K5", "MASH")), 0,
                "staging wrote into the live ledger",
            )
            added = ingest.commit(staged, evidence)
            self.assertEqual(added, len(result.staged))
            self.assertFalse(staged.exists(), "the staging file should be consumed by commit")

    def test_commit_is_idempotent_on_atom_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            staged = Path(tmp) / "staged.jsonl"
            evidence = Path(tmp) / "evidence.jsonl"
            row = json.dumps({"id": "AG-X-00", "target": "PCSK9", "disease": "ASCVD",
                              "evidence_class": "human_genetics_causal", "predicate": "p",
                              "direction": "inhibit", "strength": 0.5, "year": 2018,
                              "citation": "test"})
            evidence.write_text(row + "\n")
            staged.write_text(row + "\n")
            self.assertEqual(ingest.commit(staged, evidence), 0)


class LoopTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_loop_runs_offline_and_produces_a_transcript(self):
        run_log = loop.run(
            self.ledger, "MASH", OfflineBackend(), max_iterations=1, stage_atoms=False
        )
        self.assertTrue(run_log.iterations)
        text = loop.transcript(run_log, self.ledger)
        self.assertIn("Discovery loop", text)
        self.assertIn("Iteration 1", text)

    def test_loop_stops_rather_than_spinning(self):
        run_log = loop.run(
            self.ledger, "MASH", OfflineBackend(), max_iterations=5, stage_atoms=False
        )
        self.assertTrue(run_log.stopped_because)
        self.assertLessEqual(len(run_log.iterations), 5)

    def test_loop_does_not_write_to_the_ledger(self):
        before = len(Ledger.load().atoms)
        loop.run(self.ledger, "MASH", OfflineBackend(), max_iterations=2, stage_atoms=False)
        self.assertEqual(len(Ledger.load().atoms), before)

    def test_a_pinned_loop_stays_on_its_target(self):
        run_log = loop.run(
            self.ledger, "MASH", OfflineBackend(), target="PNPLA3",
            max_iterations=2, stage_atoms=False,
        )
        self.assertTrue(all(it.target == "PNPLA3" for it in run_log.iterations))


class BackendTests(unittest.TestCase):
    def test_available_never_raises_and_always_returns_something(self):
        self.assertIsNotNone(available("offline"))
        self.assertIsNotNone(available())

    def test_offline_backend_is_labelled_as_not_a_model(self):
        self.assertEqual(OfflineBackend().name, "offline_rules")

    def test_json_parsing_tolerates_fences_and_prose(self):
        self.assertEqual(contract.parse_json('```json\n{"a": 1}\n```'), {"a": 1})
        self.assertEqual(contract.parse_json('Here you go:\n{"a": 1}'), {"a": 1})


if __name__ == "__main__":
    unittest.main()
