"""LLM backends for the agent layer.

The scoring engine is deterministic and must stay that way — a posterior that
changes between runs cannot be argued with in a portfolio meeting. The agents
sit *around* it: they read documents into typed evidence and decide what to
pursue next. Judgement goes to the model, arithmetic stays in the engine.

Three backends, in order of preference:

    ClaudeCLIBackend   shells out to `claude -p`, inheriting this session's auth.
                       Tools are disabled and the working directory is a temp
                       dir, so the subprocess is a pure text completion with no
                       filesystem or network reach of its own.
    AnthropicAPIBackend  direct Messages API when ANTHROPIC_API_KEY is set.
    OfflineBackend     a deterministic rule-based extractor. Not an LLM and it
                       does not pretend to be one: it exists so the pipeline is
                       testable and demonstrable with no model access at all,
                       and so the tests do not depend on a network call.

`available()` picks the best backend present rather than failing, and every
result records which backend produced it — an atom extracted by the offline
rule engine must never be mistaken for one a model read.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import tempfile
from dataclasses import dataclass, field
from typing import Protocol


class LLMError(RuntimeError):
    pass


@dataclass
class Completion:
    text: str
    backend: str
    model: str | None = None


class LLMBackend(Protocol):
    name: str

    def complete(self, system: str, user: str, max_tokens: int = 4096) -> Completion: ...


# --------------------------------------------------------------------------
# claude -p


@dataclass
class ClaudeCLIBackend:
    """Headless Claude Code. Inherits session auth; no tools, no repo access."""

    name: str = "claude_cli"
    model: str | None = None
    timeout: int = 180
    binary: str = "claude"

    def complete(self, system: str, user: str, max_tokens: int = 4096) -> Completion:
        cmd = [
            self.binary,
            "-p",
            "--output-format", "text",
            "--system-prompt", system,
            # A completion, not an agent session: nothing to call, nothing to touch.
            "--allowedTools", "",
            "--disallowedTools", "Bash", "Read", "Write", "Edit", "WebFetch", "WebSearch",
            "--permission-mode", "default",
        ]
        if self.model:
            cmd += ["--model", self.model]

        with tempfile.TemporaryDirectory() as cwd:
            try:
                proc = subprocess.run(
                    cmd, input=user, text=True, capture_output=True,
                    timeout=self.timeout, cwd=cwd,
                )
            except subprocess.TimeoutExpired as e:
                raise LLMError(f"claude -p timed out after {self.timeout}s") from e
        if proc.returncode != 0:
            raise LLMError(f"claude -p exited {proc.returncode}: {proc.stderr.strip()[:400]}")
        return Completion(text=proc.stdout.strip(), backend=self.name, model=self.model)

    @staticmethod
    def present() -> bool:
        return shutil.which("claude") is not None


# --------------------------------------------------------------------------
# Anthropic Messages API


@dataclass
class AnthropicAPIBackend:
    name: str = "anthropic_api"
    model: str = "claude-sonnet-5"
    timeout: int = 120

    def complete(self, system: str, user: str, max_tokens: int = 4096) -> Completion:
        import urllib.request

        key = os.environ.get("ANTHROPIC_API_KEY")
        if not key:
            raise LLMError("ANTHROPIC_API_KEY is not set")
        base = os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com").rstrip("/")
        body = json.dumps(
            {
                "model": self.model,
                "max_tokens": max_tokens,
                "system": system,
                "messages": [{"role": "user", "content": user}],
            }
        ).encode()
        req = urllib.request.Request(
            f"{base}/v1/messages",
            data=body,
            headers={
                "content-type": "application/json",
                "x-api-key": key,
                "anthropic-version": "2023-06-01",
            },
        )
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as resp:
                payload = json.loads(resp.read().decode())
        except Exception as e:  # noqa: BLE001
            raise LLMError(f"{type(e).__name__}: {e}") from e
        text = "".join(block.get("text", "") for block in payload.get("content", []))
        return Completion(text=text.strip(), backend=self.name, model=self.model)

    @staticmethod
    def present() -> bool:
        return bool(os.environ.get("ANTHROPIC_API_KEY"))


# --------------------------------------------------------------------------
# Offline rule engine


# Ordered most-specific first: the first pattern that matches decides the class,
# so "protein-truncating variant" must be tested before the bare word "variant".
CLASS_PATTERNS: list[tuple[str, str]] = [
    ("human_perturbation", r"randomi[sz]ed|phase (?:i{1,3}|[123])\b|placebo|mendelian randomi[sz]ation|"
                           r"treated patients|clinical trial|approved for"),
    ("human_genetics_causal", r"loss[- ]of[- ]function|protein[- ]truncating|coding variant|missense|"
                              r"nonsense|splice variant|mendelian|autosomal|homozygous|knockout carriers"),
    ("human_genetics_gwas", r"genome[- ]wide association|gwas|locus associated|common variant"),
    ("perturbation_biology", r"crispr|knockdown|sirna|patient[- ]derived|organoid|ipsc|primary human cells"),
    ("model_organism", r"\bmice\b|\bmouse\b|\brat\b|zebrafish|knockout animals|murine"),
    ("expression_correlative", r"differentially expressed|elevated in|expression was higher|"
                               r"immunohistochemistry|transcriptomic"),
    ("pathway_inference", r"pathway|downstream of|axis|signalling|signaling"),
]

REFUTE_PATTERNS = r"did not meet|failed to|no significant|terminated|discontinued|worsen|" \
                  r"increased mortality|stopped early|lack of efficacy|no benefit"

INHIBIT_PATTERNS = r"loss[- ]of[- ]function.{0,80}(protect|lower|reduc|decreas)|" \
                   r"(inhibit|blockade|antagonis|knockdown|lowering).{0,80}(improv|reduc|protect|benefit)|" \
                   r"gain[- ]of[- ]function.{0,80}(caus|increas|risk)|higher levels.{0,60}(risk|caus)"
ACTIVATE_PATTERNS = r"loss[- ]of[- ]function.{0,80}(caus|increas|risk|impair)|" \
                    r"(agonis|activation|restor|supplementation).{0,80}(improv|reduc|protect|benefit)|" \
                    r"deficiency.{0,60}(caus|leads to)"


@dataclass
class OfflineBackend:
    """Deterministic keyword extractor. Explicitly not a model.

    It exists so the ingestion and loop machinery can be tested and demonstrated
    without model access, and so the test suite never depends on a network call.
    Its output is tagged `offline_rules` everywhere it lands, because a rule hit
    is much weaker evidence of correct classification than a model that read the
    passage — and conflating the two would be exactly the kind of laundering this
    whole system is built to prevent.
    """

    name: str = "offline_rules"
    entity_hints: dict[str, list[str]] = field(default_factory=dict)

    def complete(self, system: str, user: str, max_tokens: int = 4096) -> Completion:
        if "CRITIC" in system:
            return Completion(text=self._criticise(user), backend=self.name)
        if "research lead" in system:
            # The loop's judgement calls. The rule engine declines them rather
            # than faking a rationale; the loop falls back to engine ranking and
            # stops after a pass, which is the correct behaviour with no model.
            if '"decision"' in system:
                return Completion(
                    text=json.dumps({
                        "decision": "stop",
                        "reason": "no model available to judge whether to continue; "
                                  "stopping after one pass rather than looping blind",
                    }),
                    backend=self.name,
                )
            return Completion(text=json.dumps({"choice": "", "reason": ""}), backend=self.name)
        return Completion(text=self._extract(user), backend=self.name)

    # -- extraction --------------------------------------------------------
    def _extract(self, user: str) -> str:
        doc = _section(user, "DOCUMENT")
        targets = _listed(user, "KNOWN TARGETS")
        # Diseases are listed one per line as "ID = Human readable name"; the id
        # is what an atom must carry.
        diseases = [line.split("=", 1)[0].strip() for line in _listed(user, "KNOWN DISEASES")]
        citation = _field(doc, "citation") or "unknown"
        year = _field(doc, "year") or "0"

        body = doc.lower()
        found_t = [t for t in targets if re.search(rf"\b{re.escape(t.lower())}\b", body)]
        found_d = [d for d in diseases if _disease_mentioned(d, body, user)]

        atoms = []
        for t in found_t[:3]:
            for d in found_d[:2]:
                cls = next((c for c, pat in CLASS_PATTERNS if re.search(pat, body)), "pathway_inference")
                refutes = bool(re.search(REFUTE_PATTERNS, body))
                inhibit = bool(re.search(INHIBIT_PATTERNS, body))
                activate = bool(re.search(ACTIVATE_PATTERNS, body))
                direction = "inhibit" if inhibit and not activate else (
                    "activate" if activate and not inhibit else "unclear"
                )
                atoms.append(
                    {
                        "target": t,
                        "disease": d,
                        "evidence_class": cls,
                        "predicate": "extracted_finding",
                        "direction": direction,
                        # Deliberately timid. A keyword match is not a reading.
                        "strength": 0.5,
                        "year": int(year) if year.isdigit() else 0,
                        "citation": citation,
                        "refutes": refutes,
                        "effect": None,
                        "context": None,
                        "rationale": "matched by offline rules, not read by a model",
                    }
                )
        return json.dumps({"atoms": atoms})

    # -- criticism ---------------------------------------------------------
    def _criticise(self, user: str) -> str:
        doc = _section(user, "DOCUMENT").lower()
        try:
            atom = json.loads(_section(user, "PROPOSED ATOM"))
        except json.JSONDecodeError:
            return json.dumps({"verdict": "reject", "reason": "unparseable proposal"})

        cls = atom.get("evidence_class", "")
        pat = dict(CLASS_PATTERNS).get(cls)
        if pat and not re.search(pat, doc):
            return json.dumps({
                "verdict": "reject",
                "reason": f"nothing in the document supports evidence class {cls}",
            })
        if atom.get("strength", 0) > 0.6:
            return json.dumps({
                "verdict": "revise",
                "reason": "offline rules cannot justify a strength above 0.6",
                "revised": {"strength": 0.5},
            })
        return json.dumps({"verdict": "accept", "reason": "consistent with the document's wording"})


def _section(text: str, header: str) -> str:
    m = re.search(rf"<{header}>(.*?)</{header}>", text, re.DOTALL)
    return m.group(1).strip() if m else ""


def _listed(text: str, header: str) -> list[str]:
    raw = _section(text, header)
    return [p.strip() for p in re.split(r"[,\n]", raw) if p.strip()]


def _field(doc: str, key: str) -> str | None:
    m = re.search(rf"^{key}:\s*(.+)$", doc, re.MULTILINE | re.IGNORECASE)
    return m.group(1).strip() if m else None


def _disease_mentioned(disease_id: str, body: str, user: str) -> bool:
    if re.search(rf"\b{re.escape(disease_id.lower())}\b", body):
        return True
    m = re.search(rf"^{re.escape(disease_id)}\s*=\s*(.+)$", user, re.MULTILINE)
    if m:
        name = m.group(1).strip().lower()
        if name and name in body:
            return True
        head = name.split("(")[0].strip()
        if len(head) > 6 and head in body:
            return True
    return False


# --------------------------------------------------------------------------


def available(prefer: str | None = None) -> LLMBackend:
    """Best backend present. Never raises — falls back to the rule engine."""
    if prefer == "offline":
        return OfflineBackend()
    if prefer == "claude_cli" or (prefer is None and ClaudeCLIBackend.present()):
        if ClaudeCLIBackend.present():
            return ClaudeCLIBackend()
    if prefer == "anthropic_api" or (prefer is None and AnthropicAPIBackend.present()):
        if AnthropicAPIBackend.present():
            return AnthropicAPIBackend()
    return OfflineBackend()


def describe(backend: LLMBackend) -> str:
    model = getattr(backend, "model", None)
    return f"{backend.name}" + (f" ({model})" if model else "")
