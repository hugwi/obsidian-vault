"""Live data connectors, with the offline snapshot as the fallback.

The engine's design assumes the ledger is refreshed from primary sources. These
adapters do that where the network allows it, and say so plainly where it does
not, rather than silently returning empty results.

Sources and what each contributes:

  Open Targets GraphQL   target-disease evidence by datatype, tractability
                         buckets, and the Platform's own association scores
                         (useful as a comparator for this engine's posterior)
  Europe PMC REST        literature counts for the novelty term, and the
                         co-occurrence baseline an ABC proposal must beat
  ClinicalTrials.gov v2  what has already been tried against a target, which is
                         the difference between a novel hypothesis and one that
                         quietly failed in 2013
  ChEMBL REST            whether a chemical probe or clinical molecule exists

Every fetch is written back into the ledger as ordinary EvidenceAtoms with the
source recorded in `source_db`, so live and curated evidence are auditable the
same way and a run can always be reproduced from the ledger alone.

Note on this environment: outbound HTTPS is filtered by an egress policy that
currently refuses CONNECT to api.platform.opentargets.org, www.ebi.ac.uk and
clinicaltrials.gov. `probe()` reports that honestly instead of pretending the
sources are empty.
"""

from __future__ import annotations

import json
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any

TIMEOUT = 30

OPEN_TARGETS = "https://api.platform.opentargets.org/api/v4/graphql"
EUROPE_PMC = "https://www.ebi.ac.uk/europepmc/webservices/rest/search"
CLINICALTRIALS = "https://clinicaltrials.gov/api/v2/studies"
CHEMBL = "https://www.ebi.ac.uk/chembl/api/data"


class SourceUnavailable(RuntimeError):
    """Raised when a source cannot be reached, with the reason preserved."""


@dataclass
class ProbeResult:
    source: str
    reachable: bool
    detail: str


def _get(url: str, params: dict[str, Any] | None = None) -> Any:
    if params:
        url = f"{url}?{urllib.parse.urlencode(params)}"
    req = urllib.request.Request(url, headers={"Accept": "application/json", "User-Agent": "pharma-engine/0.1"})
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise SourceUnavailable(f"HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}") from e
    except Exception as e:  # noqa: BLE001 - the reason is what matters to the caller
        raise SourceUnavailable(f"{type(e).__name__}: {e}") from e


def _post_graphql(url: str, query: str, variables: dict[str, Any]) -> Any:
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(
        url, data=body, headers={"Content-Type": "application/json", "User-Agent": "pharma-engine/0.1"}
    )
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        raise SourceUnavailable(f"HTTP {e.code} from {urllib.parse.urlsplit(url).netloc}") from e
    except Exception as e:  # noqa: BLE001
        raise SourceUnavailable(f"{type(e).__name__}: {e}") from e


# --- individual sources ----------------------------------------------------

OT_ASSOCIATION_QUERY = """
query TargetDisease($ensemblId: String!, $efoId: String!) {
  target(ensemblId: $ensemblId) {
    approvedSymbol
    tractability { label modality value }
  }
  disease(efoId: $efoId) { name }
  evidences: target(ensemblId: $ensemblId) {
    associatedDiseases(efoIds: [$efoId]) {
      rows { score datatypeScores { id score } }
    }
  }
}
"""


def open_targets_association(ensembl_id: str, efo_id: str) -> dict:
    """Platform association score and per-datatype breakdown for one pair.

    Kept as a comparator rather than an input: the Platform's overall score is a
    weighted harmonic sum over correlated datatypes, which is the aggregation
    this engine deliberately does not do. Seeing both numbers side by side is
    the fastest way to see where the two disagree and why.
    """
    payload = _post_graphql(OPEN_TARGETS, OT_ASSOCIATION_QUERY, {"ensemblId": ensembl_id, "efoId": efo_id})
    if "errors" in payload:
        raise SourceUnavailable(f"GraphQL errors: {payload['errors']}")
    return payload["data"]


def europepmc_cooccurrence(target: str, disease_name: str) -> int:
    """Publication count for the pair -- the denominator of the novelty term."""
    q = f'("{target}") AND ("{disease_name}")'
    data = _get(EUROPE_PMC, {"query": q, "format": "json", "pageSize": 1})
    return int(data["hitCount"])


def clinicaltrials_for_target(intervention: str, condition: str) -> list[dict]:
    """What has already been tried. An 'unprecedented' target with six terminated
    Phase II trials is not unprecedented; it is unpublished."""
    data = _get(
        CLINICALTRIALS,
        {
            "query.intr": intervention,
            "query.cond": condition,
            "pageSize": 50,
            "fields": "NCTId,BriefTitle,OverallStatus,Phase,WhyStopped",
        },
    )
    return data.get("studies", [])


def chembl_target_search(symbol: str) -> list[dict]:
    data = _get(f"{CHEMBL}/target/search", {"q": symbol, "format": "json", "limit": 5})
    return data.get("targets", [])


# --- health check ----------------------------------------------------------

def probe() -> list[ProbeResult]:
    """Report which sources this environment can actually reach."""
    checks = [
        ("Open Targets", lambda: _post_graphql(OPEN_TARGETS, "{ meta { name } }", {})),
        ("Europe PMC", lambda: _get(EUROPE_PMC, {"query": "TREM2", "format": "json", "pageSize": 1})),
        ("ClinicalTrials.gov", lambda: _get(CLINICALTRIALS, {"query.cond": "asthma", "pageSize": 1})),
        ("ChEMBL", lambda: _get(f"{CHEMBL}/target/search", {"q": "TREM2", "format": "json", "limit": 1})),
    ]
    out: list[ProbeResult] = []
    for name, fn in checks:
        try:
            fn()
            out.append(ProbeResult(name, True, "reachable"))
        except SourceUnavailable as e:
            out.append(ProbeResult(name, False, str(e)))
    return out
