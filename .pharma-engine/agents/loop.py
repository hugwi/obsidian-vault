"""The discovery loop: agent proposes, engine adjudicates.

One iteration:

    1. engine   score the candidates for a disease (or a named pair)
    2. AGENT    choose which hypothesis to pursue, and say why
    3. engine   plan the next experiment by information per dollar
    4. AGENT    search the corpus for evidence in the class that plan names
    5. agents   ingest -> extract -> criticise -> validate -> staged atoms
    6. engine   rescore with the new evidence
    7. AGENT    continue or stop, against the pre-registered kill criterion

The division of labour is the whole design. Steps 1, 3 and 6 are arithmetic and
stay deterministic — the same evidence always produces the same posterior, which
is what makes the output arguable. Steps 2, 4 and 7 are judgement, and judgement
is what a model is for.

The loop cannot talk itself into a target. It can only find evidence and let the
engine rescore; if the evidence is weak the number does not move, and the stop
condition fires. That is deliberate: the failure mode of an agentic research
system is a confident narrative built on nothing, and the cheapest structural
defence is to keep the scoring out of the model's reach.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

from engine import experiments as exp
from engine import safety as safety_mod
from engine.graph import discover, inferred_evidence, repurposing_candidates
from engine.ledger import Ledger
from engine.model import Hypothesis
from engine.scoring import score_pair

from . import contract, ingest
from .ingest import IngestResult, SourceDoc
from .llm import LLMBackend, LLMError

SELECT_SYSTEM = """You are the research lead in a drug-target triage loop.

You are shown scored target-disease hypotheses. The scores come from a
deterministic evidence engine; you cannot change them and should not re-derive
them. Your job is to choose which ONE hypothesis is worth spending the next
experiment on.

Return ONLY JSON:

{"choice": "<TARGET id>", "reason": "<two sentences at most>"}

Judge on what the numbers do not capture:
- a hypothesis whose target already has an approved molecule can be tested in a
  trial rather than a discovery programme, which is worth years;
- a direction conflict must be resolved before anything else is worth doing;
- novelty is only valuable if the mechanism path is coherent;
- a high posterior with nothing left to learn is not where the next experiment
  belongs.

Choose from the given identifiers only."""

CONTINUE_SYSTEM = """You are the research lead in a drug-target triage loop.

You are shown a hypothesis before and after new evidence was added, plus its
pre-registered kill criterion. Decide whether to keep going.

Return ONLY JSON:

{"decision": "continue" | "stop", "reason": "<two sentences at most>"}

Stop when the loop has stopped learning: the posterior is not moving, the
remaining experiments are poor value, or the kill criterion has been met and the
honest answer is to abandon the hypothesis. Continuing to search for evidence
that would confirm a hypothesis after the evidence has stopped arriving is the
failure this loop exists to avoid. Stopping is a successful outcome."""


@dataclass
class Iteration:
    n: int
    target: str
    disease: str
    selection_reason: str
    posterior_before: float
    posterior_after: float
    experiment: str | None
    evidence_class: str | None
    documents_searched: list[str] = field(default_factory=list)
    atoms_added: list[str] = field(default_factory=list)
    atoms_elsewhere: list[str] = field(default_factory=list)
    atoms_rejected: list[str] = field(default_factory=list)
    duplicates: list[str] = field(default_factory=list)
    decision: str = "continue"
    decision_reason: str = ""

    @property
    def delta(self) -> float:
        return self.posterior_after - self.posterior_before


@dataclass
class LoopRun:
    disease: str
    backend: str
    iterations: list[Iteration] = field(default_factory=list)
    final: Hypothesis | None = None
    staged: list[Any] = field(default_factory=list)
    stopped_because: str = ""


def _summarise_candidates(ledger: Ledger, hypotheses: list[Hypothesis]) -> str:
    rows = []
    for h in hypotheses:
        drugs = repurposing_candidates(ledger, h)
        approved = [d["drug"] for d in drugs if d["approved_for_other_indication"]]
        rows.append(
            json.dumps(
                {
                    "target": h.target,
                    "target_name": ledger.name(h.target),
                    "posterior": round(h.posterior, 3),
                    "direction": h.direction.value,
                    "tractability": h.tractability,
                    "modality": h.modality,
                    "novelty": h.novelty,
                    "evidence_breadth": h.evidence_breadth,
                    "engine_decision": h.decision(),
                    "flags": h.flags[:3],
                    "mechanism_path": " -> ".join(h.path) if h.path else None,
                    "approved_drugs_on_this_target": approved,
                }
            )
        )
    return "\n".join(rows)


def _choose(
    ledger: Ledger, hypotheses: list[Hypothesis], backend: LLMBackend
) -> tuple[Hypothesis, str]:
    if len(hypotheses) == 1:
        return hypotheses[0], "only candidate"
    user = (
        f"<CANDIDATES>\n{_summarise_candidates(ledger, hypotheses)}\n</CANDIDATES>\n\n"
        f"Indication: {ledger.name(hypotheses[0].disease)}.\n"
        "Which one hypothesis should the next experiment be spent on? JSON only."
    )
    try:
        payload = contract.parse_json(backend.complete(SELECT_SYSTEM, user, max_tokens=512).text)
        choice = str(payload.get("choice", "")).strip()
        reason = str(payload.get("reason", "")).strip()
        for h in hypotheses:
            if h.target == choice:
                return h, reason or "selected by agent"
    except (LLMError, json.JSONDecodeError, KeyError):
        pass
    # The engine's own ranking is the fallback, and it is a good one.
    return hypotheses[0], "agent selection unavailable; fell back to engine ranking"


def _should_continue(
    ledger: Ledger, before: Hypothesis, after: Hypothesis, backend: LLMBackend
) -> tuple[str, str]:
    kill = next((e for e in before.experiments if e.is_kill_experiment), None)
    user = json.dumps(
        {
            "target": after.target,
            "disease": ledger.name(after.disease),
            "posterior_before": round(before.posterior, 3),
            "posterior_after": round(after.posterior, 3),
            "evidence_breadth": after.evidence_breadth,
            "engine_decision": after.decision(),
            "kill_criterion": (
                {
                    "experiment": kill.name,
                    "stop_if_posterior_falls_to": kill.posterior_if_negative,
                }
                if kill
                else None
            ),
            "remaining_experiments": [
                {"name": e.name, "bits_per_100k": e.bits_per_100k} for e in after.experiments[:3]
            ],
            "flags": after.flags[:4],
        },
        indent=2,
    )
    try:
        payload = contract.parse_json(
            backend.complete(CONTINUE_SYSTEM, user, max_tokens=512).text
        )
        decision = str(payload.get("decision", "stop")).lower().strip()
        if decision not in {"continue", "stop"}:
            decision = "stop"
        return decision, str(payload.get("reason", "")).strip() or "no reason given"
    except (LLMError, json.JSONDecodeError) as e:
        return "stop", (
            f"agent unavailable ({type(e).__name__}: {str(e)[:120]}); "
            f"stopping rather than looping blind"
        )


def _rescore(ledger: Ledger, target: str, disease: str, extra: list) -> Hypothesis:
    inferred = inferred_evidence(ledger, target, disease)
    h = score_pair(ledger, target, disease, extra_atoms=inferred + extra)
    h.safety = safety_mod.scan(ledger, h)
    h.experiments = exp.plan(ledger, h)
    return h


def run(
    ledger: Ledger,
    disease: str,
    backend: LLMBackend,
    target: str | None = None,
    max_iterations: int = 3,
    corpus_dir: Path | str = ingest.CORPUS_DIR,
    stage_atoms: bool = True,
) -> LoopRun:
    corpus = ingest.load_corpus(corpus_dir)
    run_log = LoopRun(disease=disease, backend=backend.name)
    accumulated: list = []
    seen_docs: set[str] = set()

    for n in range(1, max_iterations + 1):
        # 1. engine: candidates
        if target:
            candidates = [_rescore(ledger, target, disease, accumulated)]
        else:
            evidenced = [
                _rescore(ledger, t, d, accumulated) for t, d in ledger.pairs() if d == disease
            ]
            generated = discover(ledger, disease)[:3]
            for g in generated:
                g.safety = safety_mod.scan(ledger, g)
                g.experiments = exp.plan(ledger, g)
            candidates = sorted(evidenced + generated, key=lambda h: h.posterior, reverse=True)[:6]
        if not candidates:
            run_log.stopped_because = f"no candidates for {disease}"
            break

        # 2. agent: choose
        chosen, reason = _choose(ledger, candidates, backend)
        before = chosen

        it = Iteration(
            n=n,
            target=before.target,
            disease=disease,
            selection_reason=reason,
            posterior_before=round(before.posterior, 4),
            posterior_after=round(before.posterior, 4),
            experiment=None,
            evidence_class=None,
        )

        # 3. engine: what to measure next
        if not before.experiments:
            it.decision = "stop"
            it.decision_reason = "every evidence class is already answered"
            run_log.iterations.append(it)
            run_log.stopped_because = it.decision_reason
            run_log.final = before
            break
        top = before.experiments[0]
        it.experiment, it.evidence_class = top.name, top.evidence_class

        # 4-5. agent: search and ingest
        docs = [
            d
            for d in ingest.search_corpus(
                corpus,
                target=before.target,
                disease_name=ledger.name(disease),
                evidence_class=top.evidence_class,
            )
            if d.id not in seen_docs
        ]
        it.documents_searched = [d.id for d in docs]

        results: list[IngestResult] = []
        for doc in docs:
            seen_docs.add(doc.id)
            r = ingest.ingest_document(doc, ledger, backend)
            results.append(r)
            for atom in r.staged:
                accumulated.append(atom)
                label = (f"{atom.id} [{atom.evidence_class}"
                         f"{', refutes' if atom.refutes else ''}]")
                if atom.target == before.target and atom.disease == disease:
                    it.atoms_added.append(label)
                else:
                    it.atoms_elsewhere.append(f"{label} -> {atom.target}-{atom.disease}")
            it.atoms_rejected += [rej.reason[:90] for rej in r.rejected]
            it.duplicates += [f"{a.id} duplicates {e.id}" for a, e in r.duplicates]

        if stage_atoms and results:
            ingest.stage(results)
            ingest.record_rejections(results)
        run_log.staged.extend(a for r in results for a in r.staged)

        # 6. engine: rescore
        after = _rescore(ledger, before.target, disease, accumulated)
        it.posterior_after = round(after.posterior, 4)
        run_log.final = after

        # 7. agent: continue?
        if not it.atoms_added:
            it.decision = "stop"
            it.decision_reason = "no new admissible evidence found for this hypothesis"
        else:
            it.decision, it.decision_reason = _should_continue(ledger, before, after, backend)

        run_log.iterations.append(it)
        if it.decision == "stop":
            run_log.stopped_because = it.decision_reason or "agent stopped the loop"
            break
    else:
        run_log.stopped_because = f"reached the {max_iterations}-iteration limit"

    return run_log


def transcript(run_log: LoopRun, ledger: Ledger) -> str:
    lines = [
        f"# Discovery loop — {ledger.name(run_log.disease)}",
        "",
        f"Backend: `{run_log.backend}` · {len(run_log.iterations)} iteration(s)",
        "",
        "Scoring is deterministic and out of the agent's reach; the agent chooses what to "
        "pursue and what to read, the engine decides what it is worth.",
        "",
    ]
    for it in run_log.iterations:
        lines += [
            f"## Iteration {it.n} — {it.target}",
            "",
            f"**Chose {it.target}** — {it.selection_reason}",
            "",
            f"- Engine says next: **{it.experiment}** (class `{it.evidence_class}`)",
            f"- Searched: {', '.join(it.documents_searched) or 'nothing matched'}",
        ]
        if it.atoms_added:
            lines.append(f"- Admitted for this hypothesis: {', '.join(it.atoms_added)}")
        if it.atoms_elsewhere:
            lines.append(
                f"- Admitted, but about other pairs (they do not touch this score): "
                f"{', '.join(it.atoms_elsewhere)}"
            )
        if it.duplicates:
            lines.append(f"- Already in the ledger: {', '.join(it.duplicates)}")
        if it.atoms_rejected:
            lines.append(f"- Rejected: {len(it.atoms_rejected)}")
            for r in it.atoms_rejected[:4]:
                lines.append(f"  - {r}")
        arrow = "no change" if abs(it.delta) < 5e-4 else f"{it.delta:+.1%}"
        lines += [
            f"- Posterior {it.posterior_before:.1%} → {it.posterior_after:.1%} ({arrow})",
            "",
            f"**{it.decision.upper()}** — {it.decision_reason}",
            "",
        ]
    lines += [f"Stopped: {run_log.stopped_because}", ""]
    return "\n".join(lines)
