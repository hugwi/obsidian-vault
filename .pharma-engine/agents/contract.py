"""The structured-output contract between the agents and the ledger.

Source documents are untrusted text. A paper, a preprint, a clipping or a
scraped abstract can contain anything, including instructions addressed to
whatever is reading it. The defence is not a sterner prompt — it is that
**nothing reaches the ledger except through this validator**, and the validator
constrains what an atom is allowed to be:

- it may only concern targets and diseases that already exist in the graph, so a
  document cannot introduce entities;
- its citation must match the citation the document declares, so a document
  cannot invent a source;
- its class must be one of the declared evidence classes, its direction one of
  three values, its strength a number in [0, 1], its year no later than the
  document's;
- and the rule-based backend is capped separately, because a keyword match is
  not a reading.

Everything rejected is kept with its reason. A validator that silently drops
rows is a validator nobody audits.
"""

from __future__ import annotations

import datetime as _dt
import json
import re
from dataclasses import dataclass, field
from typing import Any

from engine.ledger import Ledger
from engine.model import Direction, EntityKind, EvidenceAtom

REQUIRED = ("target", "disease", "evidence_class", "direction", "strength", "year", "citation")
OFFLINE_STRENGTH_CAP = 0.6
MAX_STRENGTH_WITHOUT_EFFECT = 0.85

EXTRACTION_SCHEMA = """{
  "atoms": [
    {
      "target": "<one of KNOWN TARGETS, exact id>",
      "disease": "<one of KNOWN DISEASES, exact id>",
      "evidence_class": "<one of KNOWN EVIDENCE CLASSES, exact id>",
      "predicate": "<short snake_case description of the finding>",
      "direction": "inhibit | activate | unclear",
      "strength": <number 0-1>,
      "year": <publication year>,
      "citation": "<must match the document's citation line exactly>",
      "context": "<tissue or cell type the evidence was generated in, or null>",
      "effect": "<the effect size in the document's own words, or null>",
      "replications": <integer, 1 unless the document itself reports replication>,
      "refutes": <true if this finding argues AGAINST the target being useful here>,
      "rationale": "<one sentence: which part of the document supports this>"
    }
  ]
}"""


@dataclass
class Rejection:
    payload: dict[str, Any]
    reason: str
    stage: str = "validation"


@dataclass
class ValidationResult:
    atoms: list[EvidenceAtom] = field(default_factory=list)
    rejections: list[Rejection] = field(default_factory=list)
    rationales: dict[str, str] = field(default_factory=dict)

    @property
    def ok(self) -> bool:
        return bool(self.atoms)


def parse_json(text: str) -> Any:
    """Tolerate fenced blocks and leading prose; fail loudly otherwise."""
    text = text.strip()
    fence = re.search(r"```(?:json)?\s*(.*?)```", text, re.DOTALL)
    if fence:
        text = fence.group(1).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        start = text.find("{")
        end = text.rfind("}")
        if start != -1 and end > start:
            return json.loads(text[start : end + 1])
        raise


def _citation_matches(claimed: str, declared: str) -> bool:
    """Loose match on the declared citation: a model may reformat, not invent."""
    def norm(s: str) -> set[str]:
        return {w for w in re.findall(r"[a-z0-9]+", s.lower()) if len(w) > 2}

    c, d = norm(claimed), norm(declared)
    if not c or not d:
        return False
    return len(c & d) / len(c) >= 0.5


def validate(
    payload: Any,
    ledger: Ledger,
    doc_citation: str,
    doc_year: int,
    backend_name: str,
    atom_prefix: str,
) -> ValidationResult:
    result = ValidationResult()
    classes = set(ledger.priors["evidence_classes"])
    this_year = _dt.date.today().year

    if not isinstance(payload, dict) or not isinstance(payload.get("atoms"), list):
        result.rejections.append(Rejection({"raw": str(payload)[:400]}, "no 'atoms' list in the response"))
        return result

    for i, raw in enumerate(payload["atoms"]):
        if not isinstance(raw, dict):
            result.rejections.append(Rejection({"raw": str(raw)[:200]}, "atom is not an object"))
            continue

        missing = [k for k in REQUIRED if raw.get(k) in (None, "")]
        if missing:
            result.rejections.append(Rejection(raw, f"missing required fields: {', '.join(missing)}"))
            continue

        target, disease = str(raw["target"]), str(raw["disease"])
        t_entity, d_entity = ledger.entities.get(target), ledger.entities.get(disease)

        # A document may not introduce entities. If a paper is genuinely about a
        # target the graph lacks, that is a curation decision for a human, not
        # something an extractor gets to do on the strength of one abstract.
        if t_entity is None or t_entity.kind is not EntityKind.TARGET:
            result.rejections.append(Rejection(raw, f"unknown target '{target}' — not in the entity graph"))
            continue
        if d_entity is None or d_entity.kind is not EntityKind.DISEASE:
            result.rejections.append(Rejection(raw, f"unknown disease '{disease}' — not in the entity graph"))
            continue

        cls = str(raw["evidence_class"])
        if cls not in classes:
            result.rejections.append(Rejection(raw, f"undeclared evidence class '{cls}'"))
            continue

        try:
            direction = Direction(str(raw["direction"]).strip().lower())
        except ValueError:
            result.rejections.append(Rejection(raw, f"invalid direction '{raw['direction']}'"))
            continue

        try:
            strength = float(raw["strength"])
        except (TypeError, ValueError):
            result.rejections.append(Rejection(raw, f"non-numeric strength '{raw['strength']}'"))
            continue
        if not 0.0 <= strength <= 1.0:
            result.rejections.append(Rejection(raw, f"strength {strength} outside [0, 1]"))
            continue

        try:
            year = int(raw["year"])
        except (TypeError, ValueError):
            result.rejections.append(Rejection(raw, f"non-integer year '{raw['year']}'"))
            continue
        if not 1900 <= year <= this_year + 1:
            result.rejections.append(Rejection(raw, f"implausible year {year}"))
            continue
        if doc_year and year > doc_year:
            result.rejections.append(
                Rejection(raw, f"atom dated {year} but the document is from {doc_year}")
            )
            continue

        citation = str(raw["citation"]).strip()
        if not _citation_matches(citation, doc_citation):
            result.rejections.append(
                Rejection(raw, f"citation '{citation[:60]}' does not match the document's '{doc_citation[:60]}'")
            )
            continue

        # Backend-specific ceilings. Both are about not letting a weak reading
        # masquerade as a strong one.
        if backend_name == "offline_rules":
            strength = min(strength, OFFLINE_STRENGTH_CAP)
        if not raw.get("effect"):
            strength = min(strength, MAX_STRENGTH_WITHOUT_EFFECT)

        atom_id = f"{atom_prefix}-{i:02d}"
        result.atoms.append(
            EvidenceAtom(
                id=atom_id,
                target=target,
                disease=disease,
                evidence_class=cls,
                predicate=str(raw.get("predicate") or "extracted_finding"),
                direction=direction,
                strength=round(strength, 3),
                year=year,
                citation=citation,
                source_db=f"agent:{backend_name}",
                context=(str(raw["context"]) if raw.get("context") else None),
                replications=max(1, int(raw.get("replications") or 1)),
                refutes=bool(raw.get("refutes")),
                effect=(str(raw["effect"]) if raw.get("effect") else None),
                notes=(str(raw["rationale"]) if raw.get("rationale") else None),
            )
        )
        if raw.get("rationale"):
            result.rationales[atom_id] = str(raw["rationale"])

    return result


def atom_to_dict(atom: EvidenceAtom) -> dict[str, Any]:
    d = {
        "id": atom.id,
        "target": atom.target,
        "disease": atom.disease,
        "evidence_class": atom.evidence_class,
        "predicate": atom.predicate,
        "direction": atom.direction.value,
        "strength": atom.strength,
        "year": atom.year,
        "citation": atom.citation,
        "source_db": atom.source_db,
    }
    for key, value in (
        ("context", atom.context),
        ("effect", atom.effect),
        ("notes", atom.notes),
    ):
        if value:
            d[key] = value
    if atom.replications > 1:
        d["replications"] = atom.replications
    if atom.refutes:
        d["refutes"] = True
    if atom.disputed:
        d["disputed"] = True
    return d


def duplicate_of(atom: EvidenceAtom, ledger: Ledger) -> EvidenceAtom | None:
    """Is this claim already in the ledger?

    Matching on (target, disease, class, direction) plus a citation overlap.
    Re-ingesting the same paper must not manufacture a second independent line
    of evidence — that is precisely the compounding the scoring engine exists to
    prevent, and it would be embarrassing to reintroduce it at the front door.
    """
    for existing in ledger.atoms_for(atom.target, atom.disease):
        if existing.evidence_class != atom.evidence_class:
            continue
        if existing.direction is not atom.direction:
            continue
        if _citation_matches(atom.citation, existing.citation):
            return existing
    return None
