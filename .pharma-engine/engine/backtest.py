"""Retrospective evaluation: does the engine know things before the field did?

The standard way to validate a hypothesis-generation system is to restrict it
to literature before a cutoff and check what it says about what happened after.
Two tests are implemented, because they answer different questions.

**Discrimination.** Score real programmes using only evidence that predates
their clinical entry, and ask whether the ones that were approved score above
the ones that failed. Reported as AUC plus a Brier score, with the sample size
stated -- a couple of dozen programmes is a sanity check, not a validation, and
a system that claims more from this than it can support is a system that will
be trusted at exactly the wrong moment.

**Rediscovery.** Restrict the graph to before a known discovery and ask whether
open discovery surfaces it. Ground truth lives in data/discoveries.json, which
the scoring path never reads, so it cannot leak.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path

from .graph import discover, inferred_evidence
from .ledger import DATA_DIR, Ledger
from .scoring import score_pair


@dataclass
class ProgrammeResult:
    id: str
    target: str
    disease: str
    entry_year: int
    outcome: str
    label: int | None
    posterior: float
    breadth: int
    flags: list[str] = field(default_factory=list)


@dataclass
class BacktestReport:
    results: list[ProgrammeResult]
    auc: float | None
    auc_covered: float | None
    n_covered: int
    brier: float | None
    n_positive: int
    n_negative: int
    mean_posterior_success: float
    mean_posterior_failure: float
    calibration: list[dict]

    @property
    def separation(self) -> float:
        return self.mean_posterior_success - self.mean_posterior_failure


def _auc(scores_pos: list[float], scores_neg: list[float]) -> float | None:
    """Mann-Whitney U / rank-sum AUC, ties counted as half."""
    if not scores_pos or not scores_neg:
        return None
    wins = 0.0
    for p in scores_pos:
        for n in scores_neg:
            wins += 1.0 if p > n else (0.5 if p == n else 0.0)
    return wins / (len(scores_pos) * len(scores_neg))


def run(ledger: Ledger, data_dir: Path | str = DATA_DIR, infer: bool = True) -> BacktestReport:
    programmes = json.loads((Path(data_dir) / "outcomes.json").read_text())["programmes"]
    results: list[ProgrammeResult] = []

    for prog in programmes:
        historical = ledger.as_of(prog["entry_year"])
        extra = inferred_evidence(historical, prog["target"], prog["disease"]) if infer else []
        h = score_pair(historical, prog["target"], prog["disease"], extra_atoms=extra)
        results.append(
            ProgrammeResult(
                id=prog["id"],
                target=prog["target"],
                disease=prog["disease"],
                entry_year=prog["entry_year"],
                outcome=prog["outcome"],
                label=prog["label"],
                posterior=round(h.posterior, 4),
                breadth=h.evidence_breadth,
                flags=[f for f in h.flags if not f.startswith("PENALTY")],
            )
        )

    scored = [r for r in results if r.label is not None]
    pos = [r.posterior for r in scored if r.label == 1]
    neg = [r.posterior for r in scored if r.label == 0]

    # Programmes where the ledger held nothing at all before clinical entry are
    # scored at the base rate by construction. Leaving them in the headline AUC
    # would report the snapshot's coverage as if it were the engine's judgement,
    # so they are counted separately and stated.
    covered = [r for r in scored if r.breadth > 0]
    cov_pos = [r.posterior for r in covered if r.label == 1]
    cov_neg = [r.posterior for r in covered if r.label == 0]

    brier = (
        sum((r.posterior - r.label) ** 2 for r in scored) / len(scored) if scored else None
    )

    calibration = []
    for lo, hi in ((0.0, 0.15), (0.15, 0.3), (0.3, 0.5), (0.5, 1.0)):
        bucket = [r for r in scored if lo <= r.posterior < hi]
        if bucket:
            calibration.append(
                {
                    "band": f"{lo:.0%}-{hi:.0%}",
                    "n": len(bucket),
                    "predicted": round(sum(r.posterior for r in bucket) / len(bucket), 3),
                    "observed": round(sum(r.label for r in bucket) / len(bucket), 3),
                }
            )

    return BacktestReport(
        results=results,
        auc=_auc(pos, neg),
        auc_covered=_auc(cov_pos, cov_neg),
        n_covered=len(covered),
        brier=round(brier, 4) if brier is not None else None,
        n_positive=len(pos),
        n_negative=len(neg),
        mean_posterior_success=round(sum(pos) / len(pos), 4) if pos else 0.0,
        mean_posterior_failure=round(sum(neg) / len(neg), 4) if neg else 0.0,
        calibration=calibration,
    )


@dataclass
class RediscoveryResult:
    id: str
    disease: str
    targets: list[str]
    cutoff_year: int
    rank: int | None
    total_candidates: int
    found_path: str | None
    inferred_direction: str | None
    citation: str


def rediscovery(ledger: Ledger, data_dir: Path | str = DATA_DIR) -> list[RediscoveryResult]:
    cases = json.loads((Path(data_dir) / "discoveries.json").read_text())["rediscovery_cases"]
    out: list[RediscoveryResult] = []

    for case in cases:
        historical = ledger.as_of(
            case["cutoff_year"] + 1,
            keep_node_edges=case["disease"] if case.get("allow_new_disease_node") else None,
        )
        proposals = discover(historical, case["disease"])
        wanted = set(case["target"])

        rank_found: int | None = None
        path: str | None = None
        direction: str | None = None
        for i, h in enumerate(proposals, start=1):
            if h.target in wanted:
                rank_found = i
                path = " -> ".join(h.path)
                direction = h.direction.value
                break

        out.append(
            RediscoveryResult(
                id=case["id"],
                disease=case["disease"],
                targets=case["target"],
                cutoff_year=case["cutoff_year"],
                rank=rank_found,
                total_candidates=len(proposals),
                found_path=path,
                inferred_direction=direction,
                citation=case["citation"],
            )
        )
    return out
