"""Rendering: terminal tables, hypothesis cards, and Obsidian-shaped notes.

A hypothesis card is written so that the argument can be attacked. Every number
is followed by the atoms that produced it, with citations, and every penalty the
engine applied is stated rather than absorbed. If a reader disagrees with the
conclusion they should be able to find the exact atom they disagree with.
"""

from __future__ import annotations

import datetime as _dt

from . import experiments as exp
from .graph import repurposing_candidates
from .ledger import Ledger
from .model import Hypothesis
from .safety import safety_discount

DECISION_LABEL = {
    "advance": "Advance",
    "advance-modality-limited": "Advance, modality-limited",
    "resolve-direction-first": "Resolve direction first",
    "de-risk": "De-risk",
    "explore": "Explore",
    "park": "Park",
}


def table(hypotheses: list[Hypothesis], ledger: Ledger, limit: int = 20) -> str:
    rows = [
        f"{'TARGET':<10} {'INDICATION':<26} {'DIR':<9} {'P(SUCC)':>8} {'LR':>7} "
        f"{'BREADTH':>8} {'TRACT':>6}  DECISION",
        "-" * 104,
    ]
    for h in hypotheses[:limit]:
        rows.append(
            f"{h.target:<10} {ledger.name(h.disease)[:25]:<26} {h.direction.value:<9} "
            f"{h.posterior:>7.1%} {h.lr_display():>7} {h.evidence_breadth:>8} "
            f"{h.tractability:>6.2f}  {DECISION_LABEL.get(h.decision(), h.decision())}"
        )
    return "\n".join(rows)


def card(h: Hypothesis, ledger: Ledger) -> str:
    classes = ledger.priors["evidence_classes"]
    lines: list[str] = []
    disease = ledger.name(h.disease)
    target_name = ledger.name(h.target)

    lines.append(f"## {h.target} -- {disease}")
    lines.append("")
    lines.append(f"**{target_name}** | therapeutic direction: **{h.direction.value}** | "
                 f"best modality: {h.modality} (tractability {h.tractability:.2f})")
    lines.append("")
    lines.append(
        f"Prior {h.prior:.0%} -> **posterior {h.posterior:.1%}** "
        f"(total likelihood ratio {h.lr_display()}, {h.evidence_breadth} independent evidence "
        f"class{'es' if h.evidence_breadth != 1 else ''})"
    )
    lines.append("")
    lines.append(f"**Decision: {DECISION_LABEL.get(h.decision(), h.decision())}**")
    lines.append("")

    if h.provenance == "abc_path" and h.path:
        lines.append(f"> Generated hypothesis. Mechanism path: {' -> '.join(h.path)}")
        lines.append("")
        repurposing = repurposing_candidates(ledger, h)
        approved = [r for r in repurposing if r["approved_for_other_indication"]]
        if approved:
            names = ", ".join(f"{r['drug']} ({r['first_approval']})" for r in approved)
            lines.append(
                f"> **Already drugged:** {names}. Testing this hypothesis is a trial, "
                f"not a discovery programme."
            )
            lines.append("")

    # --- evidence -----------------------------------------------------------
    lines.append("### Evidence")
    lines.append("")
    lines.append("| Class | Net | log-LR | Atoms |")
    lines.append("|---|---:|---:|---|")
    for cs in h.class_scores:
        label = classes.get(cs.evidence_class, {}).get("label", cs.evidence_class)
        lines.append(
            f"| {label} | {cs.saturated_strength:+.2f} | {cs.log_lr:+.2f} | {len(cs.atoms)} |"
        )
    lines.append("")

    for cs in h.class_scores:
        label = classes.get(cs.evidence_class, {}).get("label", cs.evidence_class)
        lines.append(f"**{label}**")
        lines.append("")
        for a in sorted(cs.atoms, key=lambda a: a.year):
            marker = "REFUTES" if a.refutes else a.direction.value
            bits = [f"`{a.id}` ({a.year}, {marker}, s={a.strength:.2f}"]
            if a.replications > 1:
                bits.append(f", {a.replications} replications")
            if a.disputed:
                bits.append(", disputed")
            bits.append(")")
            head = "".join(bits)
            lines.append(f"- {head} — {a.effect or a.predicate.replace('_', ' ')}")
            lines.append(f"  - {a.citation}")
            if a.notes:
                lines.append(f"  - *{a.notes}*")
        lines.append("")

    # --- what the engine did to the numbers ---------------------------------
    if h.flags:
        lines.append("### Adjustments and warnings")
        lines.append("")
        for f in h.flags:
            lines.append(f"- {f}")
        lines.append("")

    # --- safety -------------------------------------------------------------
    if h.safety:
        discount = safety_discount(h.safety)
        lines.append(f"### On-target safety (expected-value discount {discount:.2f})")
        lines.append("")
        for s in h.safety:
            lines.append(f"- **{s.trait}** ({s.severity}) — {s.basis}")
            lines.append(f"  - {s.citation}")
        lines.append("")

    # --- next experiments ---------------------------------------------------
    if h.experiments:
        lines.append("### What to do next")
        lines.append("")
        lines.append("| Experiment | Bits | Cost | Weeks | Bits/$100k | If negative |")
        lines.append("|---|---:|---:|---:|---:|---:|")
        for e in h.experiments[:6]:
            mark = " **(kill)**" if e.is_kill_experiment else ""
            lines.append(
                f"| {e.name}{mark} | {e.expected_info_gain:.2f} | ${e.cost_usd:,.0f} | "
                f"{e.weeks:.0f} | {e.bits_per_100k:.2f} | {e.posterior_if_negative:.0%} |"
            )
        lines.append("")
        lines.append(exp.summarise(h))
        lines.append("")
        top = h.experiments[0]
        lines.append(f"> {top.description}")
        lines.append("")

    if h.missing_classes:
        readable = [classes.get(c, {}).get("label", c) for c in h.missing_classes]
        lines.append(f"*No evidence at all in: {', '.join(readable)}.*")
        lines.append("")

    return "\n".join(lines)


def digest_note(
    hypotheses: list[Hypothesis],
    ledger: Ledger,
    title: str,
    project: str = "Pharma target-hypothesis engine",
    subtitle: str = "",
) -> str:
    """An Obsidian note: frontmatter per the vault's conventions, then cards."""
    today = _dt.date.today().isoformat()
    front = [
        "---",
        f"created: {today}",
        "categories:",
        '  - "[[Projects]]"',
        f'project: "[[{project}]]"',
        "tags:",
        "  - pharma",
        "  - target-validation",
        "  - generated",
        "---",
        "",
        f"# {title}",
        "",
    ]
    if subtitle:
        front += [subtitle, ""]
    front += [
        f"Generated by `.pharma-engine` on {today}. Every number below decomposes into the "
        "atoms listed under it; disagree with an atom rather than with the score.",
        "",
        "## Ranking",
        "",
        "| # | Target | Indication | Direction | P(success) | Breadth | Decision |",
        "|---:|---|---|---|---:|---:|---|",
    ]
    for i, h in enumerate(hypotheses, start=1):
        front.append(
            f"| {i} | {h.target} | {ledger.name(h.disease)} | {h.direction.value} | "
            f"{h.posterior:.1%} | {h.evidence_breadth} | {DECISION_LABEL.get(h.decision(), h.decision())} |"
        )
    front.append("")
    front.append("---")
    front.append("")

    for h in hypotheses:
        front.append(card(h, ledger))
        front.append("---")
        front.append("")

    return "\n".join(front)
