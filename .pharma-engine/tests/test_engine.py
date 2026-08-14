"""Tests for the target-hypothesis engine.

Most of these are invariant tests rather than golden-output tests: they assert
the properties the design claims, so that changing the numbers in priors.json
is allowed but breaking the reasoning is not.

Run: python3 -m unittest discover -s tests -v
"""

from __future__ import annotations

import math
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from engine import backtest as bt
from engine import experiments as exp
from engine.graph import discover, inferred_evidence, paths_between, transfer_atoms
from engine.ledger import Ledger
from engine.model import Direction, EntityKind, EvidenceAtom
from engine.safety import safety_discount, scan
from engine.scoring import combine_groups, resolve_direction, saturate, score_pair


class SaturationTests(unittest.TestCase):
    def test_empty_is_zero(self):
        self.assertEqual(saturate([]), 0.0)

    def test_single_atom_keeps_its_strength(self):
        # The reason noisy-or is the default: one decisive observation must not
        # be deflated just because it is alone.
        self.assertAlmostEqual(saturate([0.95]), 0.95, places=6)

    def test_more_evidence_never_lowers_the_score(self):
        base = saturate([0.7])
        self.assertGreater(saturate([0.7, 0.6]), base)
        self.assertGreater(saturate([0.7, 0.6, 0.5]), saturate([0.7, 0.6]))

    def test_returns_diminish(self):
        first = saturate([0.6, 0.6]) - saturate([0.6])
        second = saturate([0.6, 0.6, 0.6]) - saturate([0.6, 0.6])
        self.assertGreater(first, second)

    def test_bounded_above_by_one(self):
        self.assertLessEqual(saturate([1.0] * 20), 1.0)

    def test_harmonic_mode_matches_open_targets_shape(self):
        # sum(s_i / i^2) / 1.6449
        self.assertAlmostEqual(saturate([1.0], mode="harmonic"), 1 / 1.6449, places=4)


class CorrelatedEvidenceTests(unittest.TestCase):
    """The central claim: correlated evidence must not compound."""

    def setUp(self):
        self.ledger = Ledger.load()

    def _atom(self, cls, strength, aid, direction=Direction.INHIBIT):
        return EvidenceAtom(
            id=aid, target="TEST", disease="RA", evidence_class=cls,
            predicate="p", direction=direction, strength=strength, year=2000, citation="test",
        )

    def test_same_group_is_damped(self):
        from engine.scoring import score_classes

        both = [self._atom("human_genetics_causal", 0.9, "A"), self._atom("human_genetics_gwas", 0.9, "B")]
        one = [both[0]]
        cs_both = score_classes(both, self.ledger, "RA", Direction.INHIBIT)
        cs_one = score_classes(one, self.ledger, "RA", Direction.INHIBIT)

        lr_both = combine_groups(cs_both, self.ledger)
        lr_one = combine_groups(cs_one, self.ledger)
        naive = sum(c.log_lr for c in cs_both)

        self.assertGreater(lr_both, lr_one)      # more evidence still helps
        self.assertLess(lr_both, naive)          # but not as much as summing would say

    def test_different_groups_add_fully(self):
        from engine.scoring import score_classes

        atoms = [self._atom("human_genetics_causal", 0.9, "A"), self._atom("perturbation_biology", 0.9, "B")]
        cs = score_classes(atoms, self.ledger, "RA", Direction.INHIBIT)
        self.assertAlmostEqual(combine_groups(cs, self.ledger), sum(c.log_lr for c in cs), places=9)


class CalibrationTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_genetics_alone_lands_near_the_published_multiplier(self):
        """A clean human genetic signal and nothing else should move the odds by
        about the 2.6x that Minikel et al. report, not by an arbitrary amount."""
        atom = EvidenceAtom(
            id="G", target="PCSK9", disease="RA", evidence_class="human_genetics_causal",
            predicate="loss_of_function_protective", direction=Direction.INHIBIT,
            strength=1.0, year=2000, citation="test",
        )
        h = score_pair(self.ledger, "PCSK9", "RA", extra_atoms=[atom])
        self.assertAlmostEqual(math.exp(h.log_lr_total), 2.6, places=2)

    def test_no_evidence_returns_the_base_rate(self):
        h = score_pair(self.ledger, "PCSK9", "RA")
        self.assertAlmostEqual(h.posterior, self.ledger.priors["base_rates"]["p_approval_from_phase1"])

    def test_likelihood_ratio_is_capped(self):
        atoms = [
            EvidenceAtom(id=f"X{i}", target="PCSK9", disease="RA", evidence_class=cls,
                         predicate="p", direction=Direction.INHIBIT, strength=1.0, year=2000,
                         citation="test", replications=5)
            for i, cls in enumerate(self.ledger.priors["evidence_classes"])
        ]
        h = score_pair(self.ledger, "PCSK9", "RA", extra_atoms=atoms)
        self.assertLessEqual(math.exp(h.log_lr_total), self.ledger.priors["lr_cap"]["value"] + 1e-6)
        self.assertTrue(any(f.startswith("LR-CAPPED") for f in h.flags))


class RefutationTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_negative_clinical_readout_pushes_below_the_prior(self):
        """CETP is the canonical surrogate-endpoint failure. A ledger that could
        only accumulate would still rank it on its HDL and literature evidence."""
        h = score_pair(self.ledger, "CETP", "ASCVD")
        self.assertLess(h.posterior, h.prior)

    def test_il17a_crohn_is_parked_despite_pathway_membership(self):
        h = score_pair(self.ledger, "IL17A", "CROHN")
        self.assertLess(h.posterior, h.prior)
        self.assertEqual(h.decision(), "park")

    def test_the_same_pathway_still_scores_high_in_the_right_tissue(self):
        skin = score_pair(self.ledger, "IL17A", "PSORIASIS")
        gut = score_pair(self.ledger, "IL17A", "CROHN")
        self.assertGreater(skin.posterior, 0.25)
        self.assertGreater(skin.posterior, gut.posterior * 5)


class DirectionTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_conflict_is_flagged_not_averaged(self):
        """GIPR: agonism is approved for obesity and loss-of-function variants
        also associate with lower BMI. The engine must refuse to pick a side."""
        h = score_pair(self.ledger, "GIPR", "OBESITY")
        self.assertTrue(any(f.startswith("DIRECTION-CONFLICT") for f in h.flags), h.flags)
        self.assertEqual(h.decision(), "resolve-direction-first")

    def test_conflict_puts_a_resolution_experiment_first(self):
        h = score_pair(self.ledger, "GIPR", "OBESITY")
        plan = exp.plan(self.ledger, h)
        self.assertEqual(plan[0].name, "Direction-of-effect resolution")

    def test_agonism_targets_are_marked_harder_to_drug(self):
        agonist = score_pair(self.ledger, "TREM2", "AD")
        self.assertIs(agonist.direction, Direction.ACTIVATE)
        self.assertLess(agonist.tractability, 0.8)

    def test_unclear_direction_when_nothing_carries_one(self):
        d, contest, flags = resolve_direction([], self.ledger)
        self.assertIs(d, Direction.UNCLEAR)
        self.assertTrue(flags)


class GraphTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_diseases_are_never_waypoints(self):
        for target in ("HMGCR", "PCSK9", "CETP"):
            for p in paths_between(self.ledger, target, "AD", max_len=4):
                middles = p.nodes[1:-1]
                kinds = [self.ledger.entities[n].kind for n in middles if n in self.ledger.entities]
                self.assertNotIn(EntityKind.DISEASE, kinds, f"{target}: {p.describe(self.ledger)}")

    def test_sign_propagates_through_an_inhibitory_edge(self):
        """SOST inhibits Wnt, Wnt drives bone formation, bone formation prevents
        osteoporosis: two negatives, so the move is to inhibit sclerostin."""
        paths = paths_between(self.ledger, "SOST", "OSTEOPOROSIS", max_len=3)
        self.assertTrue(paths)
        self.assertEqual(paths[0].sign, 1)

    def test_transfer_flips_direction_when_the_path_flips_sign(self):
        """MERTK must be activated to restore RPE phagocytosis; ROCK constrains
        the same process, so the borrowed direction must invert to inhibit."""
        atoms = transfer_atoms(self.ledger, "ROCK1", "DRY_AMD")
        self.assertTrue(atoms)
        borrowed = next(a for a in atoms if "MERTK" in a.id or "MERTK" in a.citation)
        self.assertIs(borrowed.direction, Direction.INHIBIT)

    def test_inference_never_stacks_on_direct_evidence(self):
        self.assertEqual(inferred_evidence(self.ledger, "PCSK9", "ASCVD"), [])

    def test_generated_hypotheses_stay_below_evidenced_ones(self):
        generated = discover(self.ledger, "AD")
        evidenced = score_pair(self.ledger, "TREM2", "AD")
        self.assertTrue(generated)
        self.assertTrue(all(g.posterior < evidenced.posterior for g in generated))


class SafetyTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_sclerostin_vascular_risk_is_visible_from_the_graph(self):
        h = score_pair(self.ledger, "SOST", "OSTEOPOROSIS")
        signals = scan(self.ledger, h)
        self.assertTrue(any("calcification" in s.trait for s in signals),
                        [s.trait for s in signals])

    def test_safety_never_touches_the_efficacy_posterior(self):
        h = score_pair(self.ledger, "SOST", "OSTEOPOROSIS")
        before = h.posterior
        h.safety = scan(self.ledger, h)
        self.assertEqual(h.posterior, before)
        self.assertLess(safety_discount(h.safety), 1.0)

    def test_discount_is_bounded(self):
        h = score_pair(self.ledger, "SOST", "OSTEOPOROSIS")
        self.assertGreaterEqual(safety_discount(scan(self.ledger, h)), 0.05)


class ExperimentTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()
        self.h = score_pair(self.ledger, "LRRK2", "PD")
        # A pair with neither genetics nor expression answered, so both appear
        # in the plan and can be compared on value.
        self.unevidenced = score_pair(self.ledger, "NLRP3", "MASH")

    def test_information_gain_is_non_negative(self):
        for e in exp.plan(self.ledger, self.h):
            self.assertGreaterEqual(e.expected_info_gain, -1e-9, e.name)

    def test_low_specificity_work_is_poor_value_however_cheap(self):
        """Differential expression is sensitive and unspecific. It should lose
        to human genetics on information per dollar, which is the whole point of
        pricing experiments rather than listing them."""
        plan = {e.evidence_class: e for e in exp.plan(self.ledger, self.unevidenced)}
        self.assertLess(
            plan["expression_correlative"].bits_per_100k,
            plan["human_genetics_causal"].bits_per_100k,
        )

    def test_a_kill_experiment_is_always_named(self):
        plan = exp.plan(self.ledger, self.h)
        self.assertEqual(sum(1 for e in plan if e.is_kill_experiment), 1)

    def test_kill_experiment_lowers_the_posterior_when_negative(self):
        kill = next(e for e in exp.plan(self.ledger, self.h) if e.is_kill_experiment)
        self.assertLess(kill.posterior_if_negative, self.h.posterior)

    def test_budget_is_respected(self):
        plan = exp.plan(self.ledger, self.h, budget_usd=100_000)
        self.assertTrue(all(e.cost_usd <= 100_000 for e in plan))

    def test_saturated_groups_are_not_re_proposed(self):
        """SOST already has a Mendelian human knockout. Offering to buy GWAS
        fine-mapping in the same independence group is offering more of what you
        have, and the information calculation cannot see that on its own."""
        h = score_pair(self.ledger, "SOST", "OSTEOPOROSIS")
        classes = {e.evidence_class for e in exp.plan(self.ledger, h)}
        self.assertNotIn("human_genetics_gwas", classes)
        self.assertNotIn("human_genetics_causal", classes)

    def test_answered_classes_are_not_re_proposed(self):
        classes = {e.evidence_class for e in exp.plan(self.ledger, self.h)}
        strong = {c.evidence_class for c in self.h.class_scores if c.saturated_strength >= 0.45}
        self.assertFalse(classes & strong)


class TemporalTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_as_of_hides_later_evidence(self):
        past = self.ledger.as_of(2010)
        self.assertTrue(all(a.year < 2010 for a in past.atoms))
        self.assertLess(len(past.atoms), len(self.ledger.atoms))

    def test_hindsight_does_not_leak_into_the_backtest(self):
        """PCSK9's outcome trial is 2017; scored at its 2012 entry the engine
        must not have it."""
        past = self.ledger.as_of(2012)
        h = score_pair(past, "PCSK9", "ASCVD")
        self.assertFalse(any(a.year >= 2012 for a in h.atoms))
        self.assertLess(h.posterior, score_pair(self.ledger, "PCSK9", "ASCVD").posterior)


class BacktestTests(unittest.TestCase):
    def setUp(self):
        self.ledger = Ledger.load()

    def test_approved_programmes_outrank_failures_on_average(self):
        rep = bt.run(self.ledger)
        self.assertGreater(rep.mean_posterior_success, rep.mean_posterior_failure)
        self.assertIsNotNone(rep.auc)
        self.assertGreater(rep.auc, 0.5)

    def test_known_discoveries_are_recovered_blind(self):
        for r in bt.rediscovery(self.ledger):
            self.assertIsNotNone(r.rank, f"{r.id} not surfaced at all")
            self.assertLessEqual(r.rank, 3, f"{r.id} ranked {r.rank}")
            self.assertEqual(r.inferred_direction, "inhibit", r.id)


class LedgerIntegrityTests(unittest.TestCase):
    """The data has to stay honest for any of the above to mean anything."""

    def setUp(self):
        self.ledger = Ledger.load()

    def test_every_atom_carries_a_citation_and_a_year(self):
        for a in self.ledger.atoms:
            self.assertTrue(a.citation.strip(), a.id)
            self.assertGreater(a.year, 1900, a.id)

    def test_every_atom_names_a_known_target_and_disease(self):
        for a in self.ledger.atoms:
            self.assertIn(a.target, self.ledger.entities, a.id)
            self.assertIn(a.disease, self.ledger.entities, a.id)

    def test_atom_ids_are_unique(self):
        ids = [a.id for a in self.ledger.atoms]
        self.assertEqual(len(ids), len(set(ids)))

    def test_every_evidence_class_is_declared_in_priors(self):
        declared = set(self.ledger.priors["evidence_classes"])
        for a in self.ledger.atoms:
            self.assertIn(a.evidence_class, declared, a.id)

    def test_every_edge_connects_known_entities(self):
        for e in self.ledger.edges:
            self.assertIn(e.src, self.ledger.entities, f"{e.src}->{e.dst}")
            self.assertIn(e.dst, self.ledger.entities, f"{e.src}->{e.dst}")

    def test_rediscovery_targets_have_no_direct_evidence_before_cutoff(self):
        """If ground truth leaked into the ledger the rediscovery test is theatre."""
        import json

        cases = json.loads((Path(__file__).resolve().parent.parent / "data" / "discoveries.json").read_text())
        for case in cases["rediscovery_cases"]:
            past = self.ledger.as_of(case["cutoff_year"] + 1)
            for t in case["target"]:
                self.assertEqual(past.atoms_for(t, case["disease"]), [], f"{t}-{case['disease']} leaked")


if __name__ == "__main__":
    unittest.main()
