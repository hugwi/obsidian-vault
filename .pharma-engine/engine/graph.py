"""Open discovery over the mechanism graph -- Swanson's ABC model, with signs.

Classical literature-based discovery finds A-B and B-C in disjoint literatures
and proposes A-C. That produces plausible-sounding pairs at enormous volume and
leaves the researcher to sort them, which is why LBD has a long history and a
short list of accepted discoveries.

Two changes make the output actionable:

**Signs propagate.** Every edge carries a polarity. The product along the path
says whether the target pushes the disease up or down, which turns a bare "these
are related" into "inhibit this" or "activate this". A path whose sign is
ambiguous is reported as ambiguous rather than being scored as a hit.

**The output is priced, not just ranked.** A generated hypothesis enters the
same evidence engine as everything else, as a single pathway-inference atom --
the weakest class there is. It therefore lands near the base rate, which is
honest: an unevidenced inference is not competitive with a human knockout. What
makes it worth reading is the pairing with experiments.py, which says what the
cheapest decisive test would be.
"""

from __future__ import annotations

from dataclasses import dataclass

from .ledger import Edge, Ledger
from .model import Direction, EntityKind, EvidenceAtom, Hypothesis
from .scoring import score_pair

# How much of the claim survives each edge type. "adjacent" is deliberately
# punitive: co-membership in a broad category is not a mechanism.
EDGE_TRANSMISSION = {
    "member": 0.85,
    "drives": 0.90,
    "prevents": 0.90,
    "instance": 0.85,
    "enables": 0.80,
    "inhibits": 0.85,
    "opposes": 0.75,
    "transduces": 0.75,
    "downstream": 0.70,
    "upstream": 0.70,
    "regulates": 0.70,
    "substrate": 0.60,
    "modulates": 0.55,
    "adjacent": 0.25,
}
DEFAULT_TRANSMISSION = 0.5
PATH_DECAY = 0.75


def polarity(edge: Edge) -> int:
    explicit = getattr(edge, "polarity", None)
    if explicit is not None:
        return int(explicit)
    return -1 if edge.type in {"prevents", "inhibits", "opposes"} else 1


@dataclass
class Path:
    nodes: list[str]
    edges: list[Edge]

    @property
    def strength(self) -> float:
        s = 1.0
        for e in self.edges:
            s *= EDGE_TRANSMISSION.get(e.type, DEFAULT_TRANSMISSION)
        return s * (PATH_DECAY ** max(0, len(self.edges) - 2))

    @property
    def sign(self) -> int:
        s = 1
        for e in self.edges:
            s *= polarity(e)
        return s

    def describe(self, ledger: Ledger) -> str:
        parts: list[str] = [ledger.name(self.nodes[0])]
        for e, node in zip(self.edges, self.nodes[1:]):
            arrow = "--|" if polarity(e) < 0 else "-->"
            parts.append(f" {arrow}[{e.type}] {ledger.name(node)}")
        return "".join(parts)


def _adjacency(ledger: Ledger) -> dict[str, list[tuple[str, Edge]]]:
    adj: dict[str, list[tuple[str, Edge]]] = {}
    for e in ledger.edges:
        adj.setdefault(e.src, []).append((e.dst, e))
        # Traversal is undirected -- mechanism reasoning runs both ways, from
        # target down to phenotype and from phenotype back up to candidates --
        # but polarity is a property of the edge, so the sign is preserved
        # whichever way it is crossed.
        adj.setdefault(e.dst, []).append((e.src, e))
    return adj


def paths_between(ledger: Ledger, src: str, dst: str, max_len: int = 4, limit: int = 12) -> list[Path]:
    """All simple paths from src to dst up to max_len edges, strongest first.

    Disease nodes may only be endpoints, never waypoints. Without that rule the
    walk routes through whichever disease has the most edges and manufactures
    chains like `HMGCR -> LDL clearance -> cardiovascular disease -> NLRP3
    inflammasome -> Alzheimer's`, which reads as an argument for statins in
    dementia and is nothing of the kind. Hub-hopping through popular nodes is
    the standard way literature-based discovery generates plausible nonsense at
    volume, and forbidding it costs nothing real: a genuine mechanism connects
    through pathways and processes, not through a second diagnosis.
    """
    adj = _adjacency(ledger)
    found: list[Path] = []

    def is_disease(node: str) -> bool:
        e = ledger.entities.get(node)
        return e is not None and e.kind is EntityKind.DISEASE

    def walk(node: str, nodes: list[str], edges: list[Edge]) -> None:
        if len(found) >= 400 or len(edges) > max_len:
            return
        if node == dst and edges:
            found.append(Path(nodes=list(nodes), edges=list(edges)))
            return
        if len(edges) and is_disease(node):
            return  # reached some other disease: dead end, not a waypoint
        for nxt, edge in adj.get(node, []):
            if nxt in nodes:
                continue
            walk(nxt, nodes + [nxt], edges + [edge])

    walk(src, [src], [])
    found.sort(key=lambda p: p.strength, reverse=True)
    return found[:limit]


STRONG_CLASSES = {"human_genetics_causal", "human_genetics_gwas", "human_perturbation", "perturbation_biology"}
TRANSFER_CEILING = 0.85


def transfer_atoms(ledger: Ledger, target: str, disease: str, max_len: int = 4, top_n: int = 2) -> list[EvidenceAtom]:
    """Evidence borrowed from pathway siblings, with the sign carried across.

    If another target on the same mechanism already has strong human evidence for
    this disease, that says something about this target -- how much depends on
    how tightly the two are coupled and on whether the path between them flips
    the sign. IL-23 p19 was worth pursuing in Crohn's because the protective
    coding variant sat in IL23R, one node away.

    The sign flip is the part that earns its keep. A target that *constrains* a
    process which a sibling *drives* inherits the opposite therapeutic
    direction, so borrowing 'restore this' correctly produces 'block that'.

    Transferred evidence lands in the pathway-inference class, which has the
    lowest ceiling of any class. Borrowed evidence should be able to put a
    hypothesis on the list; it should never be able to justify a programme.
    """
    out: list[tuple[float, EvidenceAtom]] = []
    for sibling, sib_disease in ledger.pairs():
        if sib_disease != disease or sibling == target:
            continue
        sib_atoms = [a for a in ledger.atoms_for(sibling, disease)
                     if a.evidence_class in STRONG_CLASSES and not a.refutes]
        if not sib_atoms:
            continue
        best_atom = max(sib_atoms, key=lambda a: a.effective_strength())
        if best_atom.direction is Direction.UNCLEAR:
            continue

        paths = paths_between(ledger, target, sibling, max_len=max_len, limit=6)
        # Only paths that actually run through shared mechanism, not straight
        # through the disease node itself -- that would be circular.
        paths = [p for p in paths if disease not in p.nodes]
        if not paths:
            continue
        best = paths[0]

        strength = min(TRANSFER_CEILING, best.strength * best_atom.effective_strength())
        if strength < 0.12:
            continue

        direction = best_atom.direction if best.sign > 0 else (
            Direction.ACTIVATE if best_atom.direction is Direction.INHIBIT else Direction.INHIBIT
        )
        flip = "" if best.sign > 0 else " (sign flips along the path, so the direction inverts)"

        out.append(
            (
                strength,
                EvidenceAtom(
                    id=f"XFER-{target}-{sibling}-{disease}",
                    target=target,
                    disease=disease,
                    evidence_class="pathway_inference",
                    predicate="transferred_from_pathway_sibling",
                    direction=direction,
                    strength=round(strength, 3),
                    year=max(best_atom.year, max((e.year for e in best.edges), default=0)),
                    citation=f"Transferred from {sibling}: {best_atom.citation}",
                    source_db="pathway_transfer",
                    context=_shared_context(ledger, target, disease),
                    notes=f"{best.describe(ledger)}{flip}",
                ),
            )
        )

    out.sort(key=lambda t: t[0], reverse=True)
    return [a for _, a in out[:top_n]]


def discover(
    ledger: Ledger,
    disease: str,
    max_len: int = 4,
    min_strength: float = 0.15,
    require_sign: bool = True,
) -> list[Hypothesis]:
    """Propose targets for `disease` that the ledger holds no direct evidence for.

    This is the open-discovery direction of the ABC model: fix the C term
    (disease), walk out through B terms (pathways and processes), and collect
    A terms (targets) with no existing A-C link.
    """
    known = {t for t, d in ledger.pairs() if d == disease}
    proposals: list[Hypothesis] = []

    for target in ledger.targets():
        if target.id in known:
            continue
        paths = paths_between(ledger, target.id, disease, max_len=max_len)
        if not paths:
            continue

        best = paths[0]
        if best.strength < min_strength:
            continue

        signs = {p.sign for p in paths if p.strength >= best.strength * 0.6}
        if require_sign and len(signs) > 1:
            # Competing paths disagree about whether the target raises or lowers
            # disease risk. Reporting a direction here would be inventing one.
            continue

        direction = Direction.INHIBIT if best.sign > 0 else Direction.ACTIVATE

        atom = EvidenceAtom(
            id=f"ABC-{target.id}-{disease}",
            target=target.id,
            disease=disease,
            evidence_class="pathway_inference",
            predicate="inferred_via_mechanism_path",
            direction=direction,
            strength=round(best.strength, 3),
            year=max((e.year for e in best.edges), default=0),
            citation="Inferred from the mechanism graph; no direct target-disease evidence exists",
            source_db="abc_inference",
            context=_shared_context(ledger, target.id, disease),
            notes=best.describe(ledger),
        )

        borrowed = transfer_atoms(ledger, target.id, disease)
        h = score_pair(
            ledger,
            target.id,
            disease,
            extra_atoms=[atom, *borrowed],
            provenance="abc_path",
            path=[ledger.name(n) for n in best.nodes],
        )
        h.flags.insert(0, f"GENERATED: no direct evidence links {target.id} to {disease} in this ledger")
        h.novelty = 1.0
        proposals.append(h)

    proposals.sort(key=lambda h: (h.posterior * (0.4 + 0.6 * h.tractability)), reverse=True)
    return proposals


def inferred_evidence(ledger: Ledger, target: str, disease: str, max_len: int = 4) -> list[EvidenceAtom]:
    """Graph-derived atoms for a pair that has no direct human or experimental evidence.

    This is the fallback a researcher applies without noticing: when nobody has
    tested the target in the disease, they reason from the mechanism it sits on
    and from what is known about its neighbours. Making that step explicit means
    it gets scored at the weight it deserves and shows up in the audit trail,
    instead of arriving as an unexamined intuition.

    Returns nothing when direct evidence already exists -- inference should never
    stack on top of measurement.
    """
    direct = ledger.atoms_for(target, disease)
    if any(a.evidence_class in STRONG_CLASSES for a in direct):
        return []

    atoms: list[EvidenceAtom] = []
    paths = paths_between(ledger, target, disease, max_len=max_len, limit=6)
    if paths:
        best = paths[0]
        signs = {p.sign for p in paths if p.strength >= best.strength * 0.6}
        if len(signs) == 1 and best.strength >= 0.15:
            atoms.append(
                EvidenceAtom(
                    id=f"ABC-{target}-{disease}",
                    target=target,
                    disease=disease,
                    evidence_class="pathway_inference",
                    predicate="inferred_via_mechanism_path",
                    direction=Direction.INHIBIT if best.sign > 0 else Direction.ACTIVATE,
                    strength=round(best.strength, 3),
                    year=max((e.year for e in best.edges), default=0),
                    citation="Inferred from the mechanism graph; no direct target-disease evidence",
                    source_db="abc_inference",
                    context=_shared_context(ledger, target, disease),
                    notes=best.describe(ledger),
                )
            )
    atoms.extend(transfer_atoms(ledger, target, disease, max_len=max_len))
    return atoms


def _shared_context(ledger: Ledger, target: str, disease: str) -> str | None:
    shared = set(ledger.contexts_of(target)) & set(ledger.contexts_of(disease))
    return sorted(shared)[0] if shared else None


def bridges(ledger: Ledger, target: str, disease: str, max_len: int = 4) -> list[str]:
    """The B terms connecting a target to a disease, as readable strings."""
    return [p.describe(ledger) for p in paths_between(ledger, target, disease, max_len=max_len)]


def repurposing_candidates(ledger: Ledger, hypothesis: Hypothesis) -> list[dict]:
    """Approved or investigational drugs that already hit this target.

    A generated hypothesis whose target already has a licensed molecule is worth
    far more than one that needs a discovery programme: the test is a trial, not
    a decade. This is the shape of both validated cases in data/discoveries.json.
    """
    out: list[dict] = []
    for drug in ledger.drugs_for(hypothesis.target):
        out.append(
            {
                "drug": drug["name"],
                "modality": drug.get("modality"),
                "status": drug.get("status"),
                "approved_for_other_indication": drug.get("status") == "approved",
                "first_approval": drug.get("first_approval"),
            }
        )
    return out


def entity_kind(ledger: Ledger, node: str) -> EntityKind | None:
    e = ledger.entities.get(node)
    return e.kind if e else None
