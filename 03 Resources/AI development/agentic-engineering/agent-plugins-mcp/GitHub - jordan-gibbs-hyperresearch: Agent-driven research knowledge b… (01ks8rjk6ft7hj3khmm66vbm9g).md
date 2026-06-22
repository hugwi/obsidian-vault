---
title: "GitHub - jordan-gibbs/hyperresearch: Agent-driven research knowledge base."
source: "https://github.com/jordan-gibbs/hyperresearch"
author: "github.com/jordan-gibbs"
published: 
created: 2026-05-22
description: "Agent-driven research knowledge base. Agents collect, search, and synthesize"
tags:
  - to-process
  - agent-plugins-mcp
---

# jordan-gibbs/hyperresearch


main


Go to file


Code


Open more actions menu


[![HYPERRESEARCH](https://github.com/jordan-gibbs/hyperresearch/raw/main/assets/banner.png)](https://github.com/jordan-gibbs/hyperresearch/blob/main/assets/banner.png)
### The Most Powerful Deep Research Harness


[![PyPI version](https://camo.githubusercontent.com/6e9e3515f53cf8974e896cd16ffb9af3d0fe6364387d5e9da6f73c94e5cb21cd/68747470733a2f2f696d672e736869656c64732e696f2f707970692f762f68797065727265736561726368)](https://pypi.org/project/hyperresearch/)
[![Python 3.11+](https://camo.githubusercontent.com/aaf15095ed0e9699b9395ca307297dd39ec3216e546d0d8d7b827a312e9aad9a/68747470733a2f2f696d672e736869656c64732e696f2f707970692f707976657273696f6e732f68797065727265736561726368)](https://pypi.org/project/hyperresearch/)
[![License: MIT](https://camo.githubusercontent.com/414f1c3a72fc22c390a27aad9eddfb867adfbd508656d0df4572231830cd1b0e/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f6a6f7264616e2d67696262732f68797065727265736561726368)](https://github.com/jordan-gibbs/hyperresearch/blob/main/LICENSE)
[![GitHub stars](https://camo.githubusercontent.com/0fc006217ef3ae58f57a9d2a2dd0ffe05a622ce373a288e3ff3206a0cf790cdd/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f6a6f7264616e2d67696262732f687970657272657365617263683f7374796c653d736f6369616c)](https://github.com/jordan-gibbs/hyperresearch)
**Hyperresearch turns Claude Code into a deep research agent. and currently leads the DeepResearch-Bench RACE leaderboard (benchmarked internally).** A tier-adaptive 16-step pipeline produces adversarially-audited reports with full source provenance. Every fetched source lands in a persistent, searchable vault that compounds across sessions.


[![DeepResearch-Bench top-5 — hyperresearch leads the chart ahead of Grep Deep Research, Cellcog Max, nvidia-aiq, Gemini Deep Research, and OpenAI Deep Research](https://github.com/jordan-gibbs/hyperresearch/raw/main/assets/benchmark.png)](https://github.com/jordan-gibbs/hyperresearch/blob/main/assets/benchmark.png)
Forward-looking projection from a stratified pilot against the DeepResearch-Bench leaderboard snapshot (<https://huggingface.co/spaces/muset-ai/DeepResearch-Bench-Leaderboard>). Third party validation is pending.


## Install



```
cd your-project
pip install hyperresearch && hyperresearch install
```

Then `/hyperresearch <anything>` in Claude Code.



>  Python 3.11–3.13. (3.14 not yet supported — use `pyenv install 3.13`, `uv venv -p 3.13`, or `py -3.13 -m venv .venv`.)
> 
>  Power users: `hyperresearch install --global` makes `/hyperresearch` reachable from every Claude Code session anywhere, at the cost of ~15 lines in every session's system reminder. Per-project install (above) keeps unrelated CC sessions clean.
> 
>  


## The 16-step research pipeline


The entry skill is a thin router. It bootstraps the canonical research query, then invokes one step skill per pipeline phase via Claude Code's `Skill` tool. Each step's procedure is loaded fresh into context only when needed defeating context-rot problems that makes long pipelines silently drop steps.




| # | Step | What it does | Tiers |
| --- | --- | --- | --- |
| 1 | Decompose | Canonical query → atomic items + coverage matrix + tier classification | both |
| 2 | Width sweep | Multi-perspective search plan + parallel fetcher waves (Haiku) | both |
| 3 | Contradiction graph | Pair contradictions across the corpus into ranked clusters | full |
| 4 | Loci analysis | Two parallel loci-analysts → scored loci with source budgets | full |
| 5 | Depth investigation | K parallel depth-investigators → interim notes with committed positions | full |
| 6 | Cross-locus reconcile | Reconcile committed positions → comparisons.md | full |
| 7 | Source tensions | Extract expert disagreements → source-tensions.json | full |
| 8 | Corpus critic | "What source would overturn this?" + targeted gap-fill fetch | full |
| 9 | Evidence digest | Top claims + verbatim quotes → evidence-digest.md | full |
| 10 | Triple draft | Per-angle source curation + 3 parallel draft sub-orchestrators (light: single draft) | both |
| 11 | Synthesize | Plan + outline + spawn synthesizer subagent → final\_report.md | full |
| 12 | Critics | 4 adversarial critics in parallel → findings JSONs | full |
| 13 | Gap-fetch | Targeted fetch wave for critic-identified vault gaps | full |
| 14 | Patcher | Surgical Edit hunks applied to draft (tool-locked Read+Edit) | full |
| 15 | Polish | Hygiene + filler pass (tool-locked Read+Edit subagent) | both |
| 16 | Readability audit | Recommender writes JSON suggestions; orchestrator selectively applies | both |


### Depth Modes


In your prompt, you can request one of two tiers and the rest of the pipeline scales accordingly. Full mode is default.




| Tier | Steps that run | Typical time |
| --- | --- | --- |
| `light` | bounded factual queries, surveys, comparisons — 1 → 2 → 10 → 15 → 16 | ~30–40 min |
| `full` | deep argumentative analysis with adversarial review — all 16 steps | ~1.5–2.5 hours |


### The two load-bearing principles


1. **Patch, never regenerate.** After step 11 produces the synthesized report (or step 10 for light tier), the only modifications are surgical Edit hunks. The patcher and polish auditor are tool-locked to `[Read, Edit]` at the Claude Code allowlist level so they physically cannot Write a new draft. Per-hunk caps make "just rewrite it" mechanically impossible. Critic findings that don't fit a small hunk escalate as structural issues.
2. **Canonical research query is gospel.** The verbatim user prompt is persisted to `research/query-<vault_tag>.md` once and re-read by every subsequent step and every spawned subagent. Wrapper requirements (save paths, citation format, terminal sections) are a separate contract.


### Subagent roster




| Agent | Model | Role |
| --- | --- | --- |
| `hyperresearch-fetcher` | Sonnet | URL fetching via crawl4ai; runs 8–12 in parallel per wave |
| `hyperresearch-source-analyst` | Sonnet (1M ctx) | End-to-end digest of any single long source >5000 words |
| `hyperresearch-loci-analyst` | Sonnet | Reads the width corpus, returns 1–8 depth loci with rationale |
| `hyperresearch-depth-investigator` | Sonnet | Investigates one locus, writes one interim note with a committed position |
| `hyperresearch-corpus-critic` | Sonnet | "What source would overturn the current direction?" pre-draft gap analysis |
| `hyperresearch-draft-orchestrator` | Opus | One per draft angle; reads its curated source list and writes one draft |
| `hyperresearch-synthesizer` | Opus | Reads all 3 drafts, writes the final report (two-pass write, Read+Write locked) |
| `hyperresearch-dialectic-critic` | Opus | Counter-evidence the draft missed |
| `hyperresearch-depth-critic` | Opus | Shallow spots interim notes could fill |
| `hyperresearch-width-critic` | Opus | Topical corners the corpus supports but the draft ignores |
| `hyperresearch-instruction-critic` | Opus | Structural mismatches against the prompt's atomic items |
| `hyperresearch-patcher` | Opus | Tool-locked `[Read, Edit]`. Applies critic findings as surgical Edit hunks |
| `hyperresearch-polish-auditor` | Opus | Tool-locked `[Read, Edit]`. Cuts filler, strips hygiene leaks |
| `hyperresearch-readability-recommender` | Opus | Writes JSON suggestions for paragraph rhythm and list/table conversion |


## The vault: persistent, searchable, compounding


Hyperresearch is not a one-shot report generator like most other Deep research harnesses. Every fetched source lands in a SQLite-indexed vault that every future research session can reuse.



```
hyperresearch search "ion-trap gate fidelity" -j           # Full-text search
hyperresearch search "quantum" --include-body -j           # Full-body search
hyperresearch note show <id1> <id2> <id3> -j               # Batch-read notes
hyperresearch graph hubs -j                                # Most-connected notes
hyperresearch graph backlinks <id> -j                      # Reverse links
hyperresearch lint -j                                      # Health check (broken links, missing tags)
```

**Markdown is truth, SQLite is cache.** Notes live as plain markdown with YAML frontmatter in `research/notes/`. The SQLite index is fully rebuildable. Delete it and `hyperresearch sync` reconstructs it from the markdown. The vault is inspectable in any editor, version-controllable in git, and readable without the tool installed.


**PDFs fetch directly.** `hyperresearch fetch` auto-detects PDF URLs (arXiv, NBER, SSRN, direct `.pdf` links) and extracts full text via pymupdf. Raw PDFs land in `research/raw/<note-id>.pdf` and the note's `raw_file:` frontmatter links back.


**Provenance breadcrumbs.** Every fetched source carries a `--suggested-by` link back to whatever surfaced it. The chain forms a rooted tree from seed fetches; the `provenance` lint rule catches disconnected components.


## What's structurally enforced


* **Verbatim prompt as gospel** — `scaffold-prompt` lint blocks if the scaffold doesn't open with the user's exact prompt
* **Locus coverage** — every step 4 locus must have a step 5 interim note; missing interims flag as errors
* **Patch-only modification** — steps 14, 15, 16 are tool-locked to `[Read, Edit]`. They cannot regenerate the draft
* **Critical findings never silently skip** — `patch-surgery` lint surfaces any critical finding the patcher couldn't apply
* **Schema integrity** — `tier`, `content_type`, and `type` are SQLite CHECK-constrained vocabularies; corrupted frontmatter cannot poison the index
* **Hygiene leaks caught on the way out** — scaffold sections, YAML frontmatter, and prompt echoes are stripped by step 15 before ship


## Authenticated crawling


Fetch from LinkedIn, Twitter, paywalled sites or anything you can log into:



```
hyperresearch setup       # Browser opens. Log into your sites. Done.
```

LinkedIn, Twitter, Facebook, Instagram, and TikTok automatically use a visible browser to avoid session kills.


## Academic APIs before web search


For any topic with a research literature, hit academic APIs BEFORE web search. They return citation-ranked canonical papers; web search returns derivative commentary.


* **Semantic Scholar** — `https://api.semanticscholar.org/graph/v1/paper/search`
* **arXiv** — `https://export.arxiv.org/api/query`
* **OpenAlex** — `https://api.openalex.org/works`
* **PubMed** — `https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi`


After the academic sweep, run web searches for context, news, non-academic angles, and at least one adversarial search ("criticism of X", "limitations of X").


## What it doesn't do


* It doesn't replace your judgment on which sources matter. The agent picks, you steer.
* It can't fetch what's behind a paywall you haven't logged into.
* It runs on Anthropic models Opus + Sonnet + Haiku via the subagent roster. Costs scale with tier and corpus size. If anyone wants to port this to Codex, put up a PR!
* The lint gate catches **structural** failures (missing scaffold, broken provenance, unresolved CRITICALs). It cannot guarantee factual accuracy, that's still your call.


## Requirements


* Python 3.11+
* [Claude Code](https://claude.com/claude-code)


## License


[MIT](https://github.com/jordan-gibbs/hyperresearch/blob/main/LICENSE)


## Star History


[![Star History Chart](https://camo.githubusercontent.com/7d98656eb5d8a8e7ffe08581273116211102ae7fb45b4a78f1cdfaa5c60ac929/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6a6f7264616e2d67696262732f6879706572726573656172636826747970653d44617465)](https://star-history.com/#jordan-gibbs/hyperresearch&Date)