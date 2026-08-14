"""Loading and querying the evidence ledger.

The ledger is deliberately append-only in spirit: an atom is never edited to
change a score, it is superseded by a later atom (including a refuting one).
That is what makes the time-split backtest meaningful -- `as_of(year)` gives
you exactly the ledger a researcher would have had in that year.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from pathlib import Path
from typing import Iterable

from .model import Entity, EntityKind, EvidenceAtom

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


@dataclass
class Edge:
    src: str
    dst: str
    type: str
    year: int = 0
    note: str | None = None
    polarity: int | None = None     # +1 raises, -1 lowers; None falls back to the edge type


@dataclass
class Ledger:
    entities: dict[str, Entity]
    atoms: list[EvidenceAtom]
    edges: list[Edge]
    priors: dict
    drugs: list[dict] = field(default_factory=list)

    # --- construction ------------------------------------------------------
    @classmethod
    def load(cls, data_dir: Path | str = DATA_DIR) -> "Ledger":
        data_dir = Path(data_dir)
        raw = json.loads((data_dir / "entities.json").read_text())
        priors = json.loads((data_dir / "priors.json").read_text())

        entities: dict[str, Entity] = {}
        for kind, key in (
            (EntityKind.TARGET, "targets"),
            (EntityKind.DISEASE, "diseases"),
            (EntityKind.PATHWAY, "pathways"),
            (EntityKind.PROCESS, "processes"),
        ):
            for d in raw.get(key, []):
                attrs = {k: v for k, v in d.items() if k not in {"id", "name"}}
                entities[d["id"]] = Entity(id=d["id"], kind=kind, name=d["name"], attrs=attrs)

        edges = [
            Edge(
                src=e["from"],
                dst=e["to"],
                type=e["type"],
                year=int(e.get("year", 0)),
                note=e.get("note"),
                polarity=e.get("polarity"),
            )
            for e in raw.get("edges", [])
        ]

        atoms: list[EvidenceAtom] = []
        for line in (data_dir / "evidence.jsonl").read_text().splitlines():
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            atoms.append(EvidenceAtom.from_dict(json.loads(line)))

        return cls(entities=entities, atoms=atoms, edges=edges, priors=priors, drugs=raw.get("drugs", []))

    # --- temporal slicing --------------------------------------------------
    def as_of(self, year: int | None, keep_node_edges: str | None = None) -> "Ledger":
        """A copy of the ledger containing only what was known before `year`.

        Edges with year 0 are structural (no publication date recorded) and are
        kept. Everything else is filtered strictly: `as_of(2020)` means "the
        literature up to and including 2019".

        `keep_node_edges` exempts one node's edges from the cutoff. It exists for
        a specific and narrow case: evaluating whether the engine could have
        connected an *existing* mechanism to a disease that did not exist as a
        node before the cutoff. Testing whether a 2019 graph predicts COVID-19
        is only meaningful if COVID-19 is allowed to be in the graph; what is
        being tested is the bridge, not clairvoyance about the pandemic.
        """
        if year is None:
            return self
        return Ledger(
            entities=self.entities,
            atoms=[a for a in self.atoms if a.year < year],
            edges=[
                e
                for e in self.edges
                if e.year == 0
                or e.year < year
                or (keep_node_edges is not None and keep_node_edges in (e.src, e.dst))
            ],
            priors=self.priors,
            drugs=[d for d in self.drugs if int(d.get("first_approval", d.get("failed_year", 0)) or 0) < year],
        )

    # --- queries -----------------------------------------------------------
    def atoms_for(self, target: str, disease: str) -> list[EvidenceAtom]:
        return [a for a in self.atoms if a.target == target and a.disease == disease]

    def pairs(self) -> list[tuple[str, str]]:
        seen: dict[tuple[str, str], None] = {}
        for a in self.atoms:
            seen.setdefault((a.target, a.disease), None)
        return list(seen)

    def targets(self) -> list[Entity]:
        return [e for e in self.entities.values() if e.kind is EntityKind.TARGET]

    def diseases(self) -> list[Entity]:
        return [e for e in self.entities.values() if e.kind is EntityKind.DISEASE]

    def name(self, entity_id: str) -> str:
        e = self.entities.get(entity_id)
        return e.name if e else entity_id

    def contexts_of(self, entity_id: str) -> list[str]:
        e = self.entities.get(entity_id)
        return e.contexts if e else []

    def drugs_for(self, target: str) -> list[dict]:
        return [d for d in self.drugs if target in d.get("targets", [])]

    def cooccurrence(self, target: str, disease: str) -> float:
        """Proxy for how well trodden a pair already is, on [0, 1]."""
        lit = [a for a in self.atoms_for(target, disease) if a.evidence_class == "literature_cooccurrence"]
        if lit:
            return max(a.strength for a in lit)
        n = len(self.atoms_for(target, disease))
        return min(1.0, n / 6.0)

    def out_edges(self, node: str) -> list[Edge]:
        return [e for e in self.edges if e.src == node]

    def in_edges(self, node: str) -> list[Edge]:
        return [e for e in self.edges if e.dst == node]

    def neighbours(self, node: str) -> Iterable[str]:
        for e in self.edges:
            if e.src == node:
                yield e.dst
            elif e.dst == node:
                yield e.src
