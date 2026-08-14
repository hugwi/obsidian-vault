"""Evidence aggregation.

Four levels, in order:

    atoms  ->  class score      saturating combination inside one evidence class
    class  ->  class log-LR     class score x the class's calibrated ceiling
    class  ->  group log-LR     strongest class in full, correlated siblings damped
    group  ->  posterior        sum of group log-LRs applied to the base rate

The two things this does that a weighted-sum association score does not:

1. **Correlated evidence stops compounding.** GWAS support and coding-variant
   support at the same locus are one human genetic signal read twice. Summing
   them is how a scoring system talks itself into a target. Classes are grouped
   by what they actually observe, and inside a group only the strongest counts
   in full.

2. **Evidence can point down.** A refuted replication or a negative clinical
   readout carries a negative log-LR. A ledger that can only accumulate is a
   ledger that will eventually rank every well-studied target highly, which is
   the failure mode of literature-derived scores.
"""

from __future__ import annotations

import math

from .ledger import Ledger
from .model import (
    ClassScore,
    Direction,
    EvidenceAtom,
    Hypothesis,
    odds,
    prob,
)

UNCLEAR_DIRECTION_FACTOR = 0.8
AGONISM_TRACTABILITY_FACTOR = 0.7

# Classes whose evidence is generated in a particular tissue, so a mismatch
# with the pathology's tissue is meaningful. Human genetics is excluded: a
# germline variant is not generated "in" a tissue.
CONTEXT_SENSITIVE_CLASSES = {
    "perturbation_biology",
    "model_organism",
    "expression_correlative",
    "pathway_inference",
    "clinical_precedent",
}


def saturate(strengths: list[float], mode: str = "noisy_or") -> float:
    """Combine within-class strengths with diminishing returns.

    `noisy_or` (default) treats each observation as an independent chance to
    establish the claim, discounted by rank so that the fifth paper counts for
    much less than the first: 1 - prod(1 - s_i / i^2).

    `harmonic` reproduces the Open Targets normalisation (sum s_i / i^2, over
    ~1.6449) for comparability with Platform scores. It is not the default
    because it is calibrated for data sources carrying hundreds of evidence
    strings; against a curated ledger of a handful of atoms it deflates a
    single decisive observation to ~0.6 of its strength, which would make a
    Mendelian human knockout look like weak evidence.
    """
    ordered = sorted((max(0.0, min(1.0, s)) for s in strengths), reverse=True)
    if not ordered:
        return 0.0
    if mode == "harmonic":
        total = sum(s / ((i + 1) ** 2) for i, s in enumerate(ordered))
        return min(1.0, total / 1.6449)
    residual = 1.0
    for i, s in enumerate(ordered):
        residual *= 1.0 - s / ((i + 1) ** 2)
    return 1.0 - residual


def _atom_weight(atom: EvidenceAtom, ledger: Ledger, disease: str) -> tuple[float, list[str]]:
    """Effective strength of one atom for this hypothesis, plus any penalties applied."""
    penalties: list[str] = []
    s = atom.effective_strength()

    if atom.direction is Direction.UNCLEAR and not atom.refutes:
        s *= UNCLEAR_DIRECTION_FACTOR
        penalties.append(f"{atom.id}: no direction of effect")

    if atom.evidence_class in CONTEXT_SENSITIVE_CLASSES and atom.context:
        disease_contexts = set(ledger.contexts_of(disease))
        target_contexts = set(ledger.contexts_of(atom.target))
        if disease_contexts and atom.context not in disease_contexts:
            factor = ledger.priors["penalties"]["context_mismatch"]["factor"]
            s *= factor
            where = "target tissue" if atom.context in target_contexts else "unrelated tissue"
            penalties.append(
                f"{atom.id}: generated in {atom.context} ({where}), pathology is in "
                f"{'/'.join(sorted(disease_contexts))}"
            )
    return s, penalties


def resolve_direction(atoms: list[EvidenceAtom], ledger: Ledger) -> tuple[Direction, float, list[str]]:
    """Decide whether the hypothesis says inhibit or activate, and how contested that is.

    Returns (direction, contest_fraction, flags). `contest_fraction` is the share
    of directional evidence weight arguing the other way. A programme that starts
    before this is resolved is choosing its molecule by coin flip.
    """
    weights: dict[Direction, float] = {Direction.INHIBIT: 0.0, Direction.ACTIVATE: 0.0}
    for a in atoms:
        if a.direction is Direction.UNCLEAR:
            continue
        ceiling = ledger.priors["evidence_classes"].get(a.evidence_class, {}).get("max_lr", 1.0)
        weights[a.direction] += a.effective_strength() * math.log(max(ceiling, 1.0001))

    total = weights[Direction.INHIBIT] + weights[Direction.ACTIVATE]
    if total <= 0:
        return Direction.UNCLEAR, 0.0, ["DIRECTION-UNKNOWN: no evidence carries a direction of effect"]

    winner = max(weights, key=lambda d: weights[d])
    contest = weights[Direction.INHIBIT if winner is Direction.ACTIVATE else Direction.ACTIVATE] / total

    flags: list[str] = []
    if contest >= 0.25:
        flags.append(
            f"DIRECTION-CONFLICT: {contest:.0%} of directional evidence argues for "
            f"{'activate' if winner is Direction.INHIBIT else 'inhibit'} instead of {winner.value}"
        )
    return winner, contest, flags


def score_classes(
    atoms: list[EvidenceAtom],
    ledger: Ledger,
    disease: str,
    direction: Direction,
    saturation: str = "noisy_or",
) -> list[ClassScore]:
    """One ClassScore per evidence class present, with refutation netted out."""
    classes = ledger.priors["evidence_classes"]
    by_class: dict[str, list[EvidenceAtom]] = {}
    for a in atoms:
        by_class.setdefault(a.evidence_class, []).append(a)

    out: list[ClassScore] = []
    for cls, cls_atoms in by_class.items():
        spec = classes.get(cls)
        if spec is None:
            continue
        ceiling = math.log(max(spec["max_lr"], 1.0001))

        support_s: list[float] = []
        refute_s: list[float] = []
        penalties: list[str] = []
        for a in cls_atoms:
            w, pen = _atom_weight(a, ledger, disease)
            penalties.extend(pen)
            if a.refutes:
                refute_s.append(w)
            else:
                # Evidence pointing the opposite way to the resolved direction
                # supports the hypothesis' importance but not its plan of action.
                if direction is not Direction.UNCLEAR and a.direction.opposes(direction):
                    w *= ledger.priors["penalties"]["direction_conflict"]["factor"]
                    penalties.append(f"{a.id}: argues for {a.direction.value}, hypothesis is {direction.value}")
                support_s.append(w)

        net = saturate(support_s, saturation) - saturate(refute_s, saturation)
        out.append(
            ClassScore(
                evidence_class=cls,
                saturated_strength=net,
                log_lr=net * ceiling,
                atoms=cls_atoms,
                penalties=penalties,
            )
        )

    out.sort(key=lambda c: c.log_lr, reverse=True)
    return out


def combine_groups(class_scores: list[ClassScore], ledger: Ledger) -> float:
    """Sum group log-LRs, damping correlated classes inside each group."""
    classes = ledger.priors["evidence_classes"]
    damping = ledger.priors["within_group_damping"]["value"]

    groups: dict[str, list[float]] = {}
    for cs in class_scores:
        group = classes.get(cs.evidence_class, {}).get("group", cs.evidence_class)
        groups.setdefault(group, []).append(cs.log_lr)

    total = 0.0
    for contributions in groups.values():
        positives = sorted((c for c in contributions if c > 0), reverse=True)
        negatives = [c for c in contributions if c <= 0]
        if positives:
            total += positives[0] + damping * sum(positives[1:])
        # Negative evidence is not damped. If two independent things say the
        # mechanism is wrong, both count -- the asymmetry is deliberate.
        total += sum(negatives)
    return total


def tractability_of(target_id: str, direction: Direction, ledger: Ledger) -> tuple[float, str]:
    entity = ledger.entities.get(target_id)
    if entity is None:
        return 0.0, "unknown"
    weights = ledger.priors["tractability_weights"]
    best_score, best_modality = 0.0, "unknown"
    for modality, feasibility in entity.tractability.items():
        weight = weights.get(modality, 0.8 if modality == "peptide" else 0.7)
        score = feasibility * weight
        if score > best_score:
            best_score, best_modality = score, modality
    if direction is Direction.ACTIVATE:
        # Agonising a receptor or restoring a lost enzyme is a materially harder
        # brief than blocking something, and it is where "the genetics is
        # beautiful, the molecule is impossible" programmes come from.
        best_score *= AGONISM_TRACTABILITY_FACTOR
    return round(best_score, 3), best_modality


def score_pair(
    ledger: Ledger,
    target: str,
    disease: str,
    extra_atoms: list[EvidenceAtom] | None = None,
    provenance: str = "ledger",
    path: list[str] | None = None,
    saturation: str = "noisy_or",
) -> Hypothesis:
    atoms = ledger.atoms_for(target, disease) + list(extra_atoms or [])
    prior = ledger.priors["base_rates"]["p_approval_from_phase1"]

    direction, _contest, flags = resolve_direction(atoms, ledger)
    class_scores = score_classes(atoms, ledger, disease, direction, saturation)
    log_lr = combine_groups(class_scores, ledger)

    cap = math.log(ledger.priors["lr_cap"]["value"])
    if log_lr > cap:
        flags.append(f"LR-CAPPED: raw evidence implied {math.exp(log_lr):.0f}x, capped at {math.exp(cap):.0f}x")
        log_lr = cap

    posterior = prob(odds(prior) * math.exp(log_lr))

    tract, modality = tractability_of(target, direction, ledger)
    present = {c.evidence_class for c in class_scores if c.saturated_strength > 0.05}
    missing = [c for c in ledger.priors["evidence_classes"] if c not in present]

    for cs in class_scores:
        flags.extend(f"PENALTY {p}" for p in cs.penalties)

    strong = {c.evidence_class for c in class_scores if c.saturated_strength > 0.05}
    if not strong & {"human_genetics_causal", "human_perturbation"}:
        flags.append(
            "NO-HUMAN-CAUSAL-EVIDENCE: nothing here observes the target being changed in a human. "
            "This is the profile that Phase II attrition selects against."
        )
    elif "human_perturbation" not in strong:
        # Germline variation is a lifelong exposure of modest magnitude. It
        # establishes that the target is causal and in which direction, and it
        # says very little about what a large, late, pharmacological
        # intervention would achieve. APP A673T reduces BACE1 cleavage ~40% from
        # birth and protects against Alzheimer's; ~90% BACE1 inhibition in
        # symptomatic patients worsened cognition. Nothing in the evidence model
        # distinguishes those two interventions, so the gap is flagged rather
        # than scored -- quantifying it would be inventing a number.
        flags.append(
            "GENETIC-ONLY: support is lifelong germline exposure. It fixes the direction of effect, "
            "not the effect size obtainable by intervening in established disease. Where the pathology "
            "is progressive or irreversible, treat timing and degree of engagement as unresolved."
        )

    return Hypothesis(
        target=target,
        disease=disease,
        direction=direction,
        prior=prior,
        posterior=posterior,
        log_lr_total=log_lr,
        class_scores=class_scores,
        flags=flags,
        tractability=tract,
        modality=modality,
        novelty=round(1.0 - ledger.cooccurrence(target, disease), 3),
        provenance=provenance,
        path=path or [],
        missing_classes=missing,
    )


def rank(ledger: Ledger, saturation: str = "noisy_or") -> list[Hypothesis]:
    """Score every target-disease pair the ledger has evidence for."""
    out = [score_pair(ledger, t, d, saturation=saturation) for t, d in ledger.pairs()]
    out.sort(key=lambda h: h.posterior, reverse=True)
    return out
