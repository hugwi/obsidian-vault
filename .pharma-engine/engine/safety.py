"""On-target safety, predicted before the trial rather than discovered in it.

Roughly 30% of clinical failure is unmanageable toxicity, and a large share of
that is on-target: the mechanism does exactly what it was designed to do, in a
tissue nobody was aiming at. Two sources predict it without dosing anyone:

**Pleiotropy.** If the same perturbation that helps in the indication moves
another trait the wrong way, the genetics usually says so first. This is the
MR-PheWAS logic -- genetically proxied IL-6 signalling inhibition flags atopic
dermatitis, cellulitis, urinary tract infection and cholecystitis before a
label does.

**Mechanism paths that leave the indication.** Sclerostin inhibition builds
bone through Wnt; Wnt also acts on vascular calcification. That edge existed in
the literature before romosozumab's cardiovascular imbalance appeared in ARCH
and became a boxed warning. Walking outward from the target and reading where
else the path lands is cheap, and it is the same graph the efficacy argument
already uses.
"""

from __future__ import annotations

from .graph import paths_between, polarity
from .ledger import Ledger
from .model import Direction, Hypothesis, SafetySignal

# Processes that are adverse wherever they appear downstream of a target.
ADVERSE_PROCESSES = {
    "VASCULAR_CALCIFICATION": "vascular calcification",
    "CYTOKINE_STORM": "immune dysregulation",
    "VIRAL_ENTRY": "host defence",
}


def scan(ledger: Ledger, hypothesis: Hypothesis) -> list[SafetySignal]:
    signals: list[SafetySignal] = []
    target = hypothesis.target
    indication = hypothesis.disease

    # 1. Pleiotropy: the same target, other traits.
    #
    # Two distinct things live here and they are not the same severity. An
    # observed harm on this target elsewhere is a fact. A second indication that
    # needs the *opposite* direction is an inference -- treating one disease by
    # pushing the target the other way is a plausible route to worsening it, and
    # worth stating, but it has not been observed.
    for atom in ledger.atoms:
        if atom.target != target or atom.disease == indication:
            continue

        if atom.refutes:
            severity = "high" if atom.evidence_class in {"human_perturbation", "human_genetics_causal"} else "moderate"
            signals.append(
                SafetySignal(
                    trait=f"observed harm in {ledger.name(atom.disease)}",
                    severity=severity,
                    basis=(
                        f"{ledger.priors['evidence_classes'][atom.evidence_class]['label']}: "
                        f"{atom.effect or atom.predicate.replace('_', ' ')}"
                    ),
                    citation=atom.citation,
                )
            )
            continue

        if hypothesis.direction is not Direction.UNCLEAR and atom.direction.opposes(hypothesis.direction):
            signals.append(
                SafetySignal(
                    trait=f"may worsen {ledger.name(atom.disease)}",
                    severity="moderate",
                    basis=(
                        f"that indication is treated by {atom.direction.value} of the same target, so "
                        f"{hypothesis.direction.value} here pushes it the wrong way "
                        f"({ledger.priors['evidence_classes'][atom.evidence_class]['label'].lower()})"
                    ),
                    citation=atom.citation,
                )
            )

    # 2. Mechanism paths from the target into adverse processes.
    for node, label in ADVERSE_PROCESSES.items():
        if node not in ledger.entities:
            continue
        paths = paths_between(ledger, target, node, max_len=3, limit=3)
        for p in paths:
            if p.strength < 0.2:
                continue
            sign = p.sign
            # Inhibiting a target that positively feeds an adverse process is
            # protective there; the risk is the opposite combination.
            risky = (hypothesis.direction is Direction.INHIBIT and sign < 0) or (
                hypothesis.direction is Direction.ACTIVATE and sign > 0
            )
            if not risky:
                continue
            signals.append(
                SafetySignal(
                    trait=label,
                    severity="moderate",
                    basis=f"mechanism path: {p.describe(ledger)}",
                    citation="derived from the mechanism graph, not from a trial",
                )
            )
            break

    # 3. Essentiality and expression breadth.
    entity = ledger.entities.get(target)
    if entity is not None:
        constraint = float(entity.attrs.get("constraint", 0.0))
        if constraint >= 0.7:
            signals.append(
                SafetySignal(
                    trait="narrow therapeutic window from gene essentiality",
                    severity="moderate",
                    basis=f"constraint score {constraint:.2f}: the gene is intolerant of loss of function in humans",
                    citation="population constraint metrics",
                )
            )
        breadth = len(entity.contexts)
        indication_contexts = set(ledger.contexts_of(indication))
        off_tissue = [c for c in entity.contexts if c not in indication_contexts]
        if breadth >= 3 and len(off_tissue) >= 2:
            signals.append(
                SafetySignal(
                    trait="off-tissue exposure",
                    severity="low",
                    basis=f"expressed in {', '.join(off_tissue)} in addition to the pathology tissue",
                    citation="expression breadth from the entity record",
                )
            )

    return _dedupe(signals)


def _dedupe(signals: list[SafetySignal]) -> list[SafetySignal]:
    order = {"high": 0, "moderate": 1, "low": 2}
    seen: dict[tuple[str, str], SafetySignal] = {}
    for s in signals:
        key = (s.trait, s.severity)
        seen.setdefault(key, s)
    return sorted(seen.values(), key=lambda s: order.get(s.severity, 3))


def safety_discount(signals: list[SafetySignal]) -> float:
    """Multiplier applied to expected value, never to the efficacy posterior.

    Keeping these apart matters: a mechanism can be true and still undevelopable.
    Folding safety into a single number destroys the information a portfolio
    committee actually needs, which is *which* of the two is the problem.
    """
    penalty = {"high": 0.45, "moderate": 0.2, "low": 0.05}
    discount = 1.0
    for s in signals:
        discount *= 1.0 - penalty.get(s.severity, 0.0)
    return round(max(discount, 0.05), 3)
