"""What to do next, priced in bits per dollar.

The output a researcher can act on is not a ranked list of targets. It is a
ranked list of *experiments*: given what is already known about this mechanism,
which single piece of work would change the decision most, and what does it
cost.

Each candidate experiment is a way of acquiring evidence in a class the
hypothesis is currently missing. Every class carries a sensitivity and a
specificity in priors.json, so an experiment is a noisy test of the hypothesis
and its value is ordinary expected information gain:

    p+   = P(H)*sens + (1-P(H))*(1-spec)
    EIG  = H(P(H)) - [ p+ * H(P(H|+)) + (1-p+) * H(P(H|-)) ]     bits

Dividing by cost gives bits per $100k, which is the number that should drive a
discovery budget and almost never does. The differential-expression study is
usually the cheapest thing on the list and almost always near the bottom of it,
because specificity of 0.3 buys very little information however little it costs.

The **kill experiment** is reported separately: the work whose negative result
would most reduce the posterior per dollar. Naming it before starting is what
converts a hypothesis into something falsifiable, and it is the discipline that
separates a programme that stops in year two from one that stops in Phase II.
"""

from __future__ import annotations

from .ledger import Ledger
from .model import Direction, Experiment, Hypothesis, entropy

# Below this, a class counts as "already answered" and is not re-proposed.
ANSWERED_THRESHOLD = 0.45


def _posteriors(p: float, sens: float, spec: float) -> tuple[float, float, float]:
    p_pos = p * sens + (1 - p) * (1 - spec)
    p_pos = min(max(p_pos, 1e-6), 1 - 1e-6)
    post_pos = (p * sens) / p_pos
    post_neg = (p * (1 - sens)) / (1 - p_pos)
    return p_pos, post_pos, post_neg


def plan(ledger: Ledger, hypothesis: Hypothesis, budget_usd: float | None = None) -> list[Experiment]:
    p = hypothesis.posterior
    classes = ledger.priors["evidence_classes"]

    # A class counts as answered if it is already strong -- and so does every
    # sibling in its independence group. Buying a GWAS fine-mapping study for a
    # target that already has a Mendelian human knockout adds almost nothing,
    # because the group it would land in is saturated. The information-gain
    # calculation cannot see that on its own: it treats each class as a fresh
    # independent test, which overstates the value of more of what you have.
    answered_groups = {
        classes.get(c.evidence_class, {}).get("group", c.evidence_class)
        for c in hypothesis.class_scores
        if c.saturated_strength >= ANSWERED_THRESHOLD
    }

    candidates: list[Experiment] = []
    for cls, spec in classes.items():
        if spec.get("group", cls) in answered_groups:
            continue
        acq = spec.get("acquisition")
        if not acq:
            continue
        sens, sp = float(acq["sensitivity"]), float(acq["specificity"])
        p_pos, post_pos, post_neg = _posteriors(p, sens, sp)
        eig = entropy(p) - (p_pos * entropy(post_pos) + (1 - p_pos) * entropy(post_neg))
        cost = float(acq["cost_usd"])
        candidates.append(
            Experiment(
                name=acq["name"],
                evidence_class=cls,
                description=acq["description"],
                cost_usd=cost,
                weeks=float(acq["weeks"]),
                sensitivity=sens,
                specificity=sp,
                expected_info_gain=round(eig, 4),
                bits_per_100k=round(eig / max(cost / 100_000, 0.01), 3),
                p_positive=round(p_pos, 3),
                posterior_if_positive=round(post_pos, 3),
                posterior_if_negative=round(post_neg, 3),
            )
        )

    if any(f.startswith("DIRECTION-CONFLICT") for f in hypothesis.flags):
        candidates.insert(
            0,
            Experiment(
                name="Direction-of-effect resolution",
                evidence_class="human_perturbation",
                description=(
                    "Before any molecule work: establish whether the therapeutic move is inhibition or "
                    "activation, using a cis-variant instrument in both directions plus a bidirectional "
                    "perturbation in the disease-relevant human cell type. The evidence currently "
                    "disagrees, and a programme started now is choosing its modality by coin flip."
                ),
                cost_usd=90_000,
                weeks=14,
                sensitivity=0.8,
                specificity=0.8,
                expected_info_gain=round(entropy(p), 4),
                bits_per_100k=round(entropy(p) / 0.9, 3),
                p_positive=0.5,
                posterior_if_positive=p,
                posterior_if_negative=p,
            ),
        )

    if hypothesis.direction is Direction.UNCLEAR and not candidates:
        return []

    candidates.sort(key=lambda e: e.bits_per_100k, reverse=True)

    kill = max(
        candidates,
        key=lambda e: (p - e.posterior_if_negative) / max(e.cost_usd / 100_000, 0.01),
        default=None,
    )
    if kill is not None:
        kill.is_kill_experiment = True

    if budget_usd is not None:
        chosen, spent = [], 0.0
        for e in candidates:
            if spent + e.cost_usd <= budget_usd:
                chosen.append(e)
                spent += e.cost_usd
        # The kill experiment stays on the list even if the greedy pass skipped it.
        if kill is not None and kill not in chosen and kill.cost_usd <= budget_usd:
            chosen.append(kill)
        return chosen

    return candidates


def summarise(hypothesis: Hypothesis) -> str:
    if not hypothesis.experiments:
        return "No further evidence class would change this decision materially."
    kill = next((e for e in hypothesis.experiments if e.is_kill_experiment), None)
    top = hypothesis.experiments[0]
    lines = [
        f"Best value: {top.name} -- {top.expected_info_gain:.2f} bits for ${top.cost_usd:,.0f} "
        f"({top.bits_per_100k:.2f} bits per $100k, {top.weeks:.0f} weeks)."
    ]
    if kill is not None:
        lines.append(
            f"Kill criterion: if {kill.name.lower()} comes back negative, the posterior falls "
            f"{hypothesis.posterior:.0%} -> {kill.posterior_if_negative:.0%}. Agree to stop at that number "
            f"before starting."
        )
    return " ".join(lines)
