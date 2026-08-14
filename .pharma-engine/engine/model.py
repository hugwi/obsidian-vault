"""Core data model for the target-hypothesis engine.

Everything the engine reasons about is one of four things:

    Entity        a target, disease, pathway, process or drug
    EvidenceAtom  a single typed, dated, sourced claim linking two entities
    Hypothesis    a target-disease pair plus the atoms that speak to it
    Experiment    something you could do next, with a cost and an information yield

The deliberate design choice is that **nothing is ever a bare number**. An
association score with no provenance is what current tooling gives a researcher,
and it is exactly what cannot be argued with in a portfolio meeting. Every score
here decomposes back into the atoms that produced it.
"""

from __future__ import annotations

import math
from dataclasses import dataclass, field
from enum import Enum
from typing import Any


class Direction(str, Enum):
    """Therapeutic direction implied by a piece of evidence.

    This is the field most often lost in aggregate scoring, and losing it is
    expensive: a target-disease association tells you the target matters, not
    whether you should inhibit or activate it. Programmes have been run in the
    wrong direction on strong association evidence.
    """

    INHIBIT = "inhibit"          # loss of function protects / gain of function causes
    ACTIVATE = "activate"        # loss of function causes / gain of function protects
    UNCLEAR = "unclear"          # association only, no direction of effect

    def opposes(self, other: "Direction") -> bool:
        if self is Direction.UNCLEAR or other is Direction.UNCLEAR:
            return False
        return self is not other


class EntityKind(str, Enum):
    TARGET = "target"
    DISEASE = "disease"
    PATHWAY = "pathway"
    PROCESS = "process"
    DRUG = "drug"


@dataclass(frozen=True)
class Entity:
    id: str
    kind: EntityKind
    name: str
    attrs: dict[str, Any] = field(default_factory=dict)

    # --- target-specific convenience accessors -----------------------------
    @property
    def tractability(self) -> dict[str, float]:
        return self.attrs.get("tractability", {})

    @property
    def contexts(self) -> list[str]:
        """Tissues / cell types this entity is relevant in.

        For a disease this is where the pathology lives; for a target, where it
        is expressed. A mismatch between the two is a real translational risk
        and the engine flags it rather than silently averaging it away.
        """
        return list(self.attrs.get("contexts", []))


@dataclass
class EvidenceAtom:
    """One dated, sourced claim.

    `strength` is the within-class strength of *this* observation on [0, 1] --
    a coding variant with a large effect in a well-powered cohort is near 1, an
    underpowered differential-expression result is near 0.2. It is NOT a
    probability and it is NOT comparable across classes; the class weight in
    priors.json is what makes classes commensurable.
    """

    id: str
    target: str
    disease: str
    evidence_class: str
    predicate: str
    direction: Direction
    strength: float
    year: int
    citation: str
    source_db: str = "curated"
    context: str | None = None
    replications: int = 1
    disputed: bool = False
    refutes: bool = False           # evidence *against* the hypothesis
    effect: str | None = None       # human-readable effect size
    notes: str | None = None

    @classmethod
    def from_dict(cls, d: dict[str, Any]) -> "EvidenceAtom":
        return cls(
            id=d["id"],
            target=d["target"],
            disease=d["disease"],
            evidence_class=d["evidence_class"],
            predicate=d["predicate"],
            direction=Direction(d.get("direction", "unclear")),
            strength=float(d["strength"]),
            year=int(d["year"]),
            citation=d["citation"],
            source_db=d.get("source_db", "curated"),
            context=d.get("context"),
            replications=int(d.get("replications", 1)),
            disputed=bool(d.get("disputed", False)),
            refutes=bool(d.get("refutes", False)),
            effect=d.get("effect"),
            notes=d.get("notes"),
        )

    def effective_strength(self) -> float:
        """Strength after replication and dispute adjustment.

        Replication moves an observation towards, but never to, certainty --
        the multiplier saturates. This is the Begley/Ellis correction: of 53
        landmark preclinical papers, 6 replicated, so a single unreplicated
        result is worth materially less than the same result seen twice by
        independent groups.
        """
        s = max(0.0, min(1.0, self.strength))
        rep = 1.0 + 0.35 * math.log(max(1, self.replications))
        s = min(1.0, s * rep)
        if self.disputed:
            s *= 0.45
        return s


@dataclass
class ClassScore:
    """The contribution of one evidence class to one hypothesis."""

    evidence_class: str
    saturated_strength: float       # [0, 1] after harmonic saturation
    log_lr: float                   # natural log likelihood ratio contribution
    atoms: list[EvidenceAtom]
    penalties: list[str] = field(default_factory=list)

    @property
    def lr(self) -> float:
        return math.exp(self.log_lr)


@dataclass
class SafetySignal:
    trait: str
    severity: str                   # low | moderate | high
    basis: str                      # how we know
    citation: str


@dataclass
class Experiment:
    """A next step, priced."""

    name: str
    evidence_class: str
    description: str
    cost_usd: float
    weeks: float
    sensitivity: float
    specificity: float
    expected_info_gain: float = 0.0     # bits
    bits_per_100k: float = 0.0
    p_positive: float = 0.0
    posterior_if_positive: float = 0.0
    posterior_if_negative: float = 0.0
    is_kill_experiment: bool = False


@dataclass
class Hypothesis:
    """A target-disease pair, scored and explained."""

    target: str
    disease: str
    direction: Direction
    prior: float
    posterior: float
    log_lr_total: float
    class_scores: list[ClassScore]
    flags: list[str] = field(default_factory=list)
    safety: list[SafetySignal] = field(default_factory=list)
    tractability: float = 0.0
    modality: str = "unknown"
    novelty: float = 0.0
    provenance: str = "ledger"          # ledger | abc_path
    path: list[str] = field(default_factory=list)
    experiments: list[Experiment] = field(default_factory=list)
    missing_classes: list[str] = field(default_factory=list)

    @property
    def key(self) -> str:
        return f"{self.target}--{self.disease}"

    def lr_display(self) -> str:
        lr = math.exp(self.log_lr_total)
        return f"{lr:.1f}x" if lr >= 1 else f"1/{1 / lr:.1f}x"

    @property
    def evidence_breadth(self) -> int:
        """How many independent evidence classes carry any signal.

        Breadth matters more than depth: ten papers of the same kind are one
        line of evidence with a citation count, not ten lines of evidence.
        """
        return sum(1 for c in self.class_scores if c.saturated_strength > 0.05)

    @property
    def atoms(self) -> list[EvidenceAtom]:
        out: list[EvidenceAtom] = []
        for c in self.class_scores:
            out.extend(c.atoms)
        return out

    def decision(self) -> str:
        """The portfolio call this hypothesis argues for."""
        if any(f.startswith("DIRECTION-CONFLICT") for f in self.flags):
            return "resolve-direction-first"
        if self.posterior >= 0.35 and self.tractability >= 0.5:
            return "advance"
        if self.posterior >= 0.35 and self.tractability < 0.5:
            return "advance-modality-limited"
        if self.posterior >= 0.18:
            return "de-risk"
        if self.novelty >= 0.6:
            return "explore"
        return "park"


def odds(p: float) -> float:
    p = min(max(p, 1e-9), 1 - 1e-9)
    return p / (1 - p)


def prob(o: float) -> float:
    return o / (1 + o)


def entropy(p: float) -> float:
    """Shannon entropy of a Bernoulli variable, in bits."""
    p = min(max(p, 1e-9), 1 - 1e-9)
    return -(p * math.log2(p) + (1 - p) * math.log2(1 - p))
