---
categories:
  - "[[Resources]]"
domain: engineering
title: "tirth8205/code-review-graph: Local knowledge graph for Claude Code. Builds"
source: "https://github.com/tirth8205/code-review-graph"
author: "github.com/tirth8205"
published: 
created: 2026-04-08
description: "Local knowledge graph for Claude Code. Builds a persistent map of your codebase"
tags:
  - to-process
  - agent-tools
---

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/tirth8205/code-review-graph?resume=1) 


## Create list


# tirth8205/code-review-graph


main


t


Go to file


Code


Open more actions menu


# code-review-graph


**Stop burning tokens. Start reviewing smarter.**


[![Website](https://camo.githubusercontent.com/0db07f43d64f4c28b52e9704dff9710f8323f99c5bd9644b19f0a47caf199590/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f776562736974652d636f64652d2d7265766965772d2d67726170682e636f6d2d626c75653f7374796c653d666c61742d737175617265)](https://code-review-graph.com)
[![Discord](https://camo.githubusercontent.com/c7248de77195a01ee5531c7f58f5547a9d3e20f0c71be7bb90b3162fc63bc884/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f646973636f72642d6a6f696e2d3538363546323f7374796c653d666c61742d737175617265266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/3p58KXqGFN)
[![Stars](https://camo.githubusercontent.com/f2896786113bb854bc12ec134f497a66d88fc970934d765a325e3acf12d1c89d/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f73746172732f7469727468383230352f636f64652d7265766965772d67726170683f7374796c653d666c61742d737175617265)](https://github.com/tirth8205/code-review-graph/stargazers)
[![MIT Licence](https://camo.githubusercontent.com/1b01ef0024ba0866c115986b895301f657c1b21fc29f05c4844b7f2e8d89204d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e7376673f7374796c653d666c61742d737175617265)](https://opensource.org/licenses/MIT)
[![CI](https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml/badge.svg)](https://github.com/tirth8205/code-review-graph/actions/workflows/ci.yml)
[![Python 3.10+](https://camo.githubusercontent.com/c4487da0dcf60c0d77426812666d51f0ab0194496b87c80e527f4ad205d77de5/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d332e31302532422d626c75652e7376673f7374796c653d666c61742d737175617265)](https://www.python.org/)
[![MCP](https://camo.githubusercontent.com/256ab71117ac6e2be08ba549e095566fcf968f955a7920bedfa4e2a547d0d284/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d43502d636f6d70617469626c652d677265656e2e7376673f7374796c653d666c61742d737175617265)](https://modelcontextprotocol.io/)
[![v2.1.0](https://camo.githubusercontent.com/7641f1c4ae39d44dcd0035e8cad651a0664f230be5dfbf7fa71486637aeac4a8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f76657273696f6e2d322e312e302d707572706c652e7376673f7374796c653d666c61742d737175617265)](https://github.com/tirth8205/code-review-graph/#)
AI coding tools re-read your entire codebase on every task. `code-review-graph` fixes that. It builds a structural map of your code with [Tree-sitter](https://tree-sitter.github.io/tree-sitter/), tracks changes incrementally, and gives your AI assistant precise context via [MCP](https://modelcontextprotocol.io/) so it reads only what matters.


[![The Token Problem: 8.2x average token reduction across 6 real repositories](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram1_before_vs_after.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram1_before_vs_after.png)
## Quick Start



```
pip install code-review-graph                     # or: pipx install code-review-graph
code-review-graph install          # auto-detects and configures all supported platforms
code-review-graph build            # parse your codebase
```

One command sets up everything. `install` detects which AI coding tools you have, writes the correct MCP configuration for each one, and injects graph-aware instructions into your platform rules. It auto-detects whether you installed via `uvx` or `pip`/`pipx` and generates the right config. Restart your editor/tool after installing.


[![One Install, Every Platform: auto-detects Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, and Antigravity](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram8_supported_platforms.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram8_supported_platforms.png)
To target a specific platform:



```
code-review-graph install --platform cursor      # configure only Cursor
code-review-graph install --platform claude-code  # configure only Claude Code
```

Requires Python 3.10+. For the best experience, install [uv](https://docs.astral.sh/uv/) (the MCP config will use `uvx` if available, otherwise falls back to the `code-review-graph` command directly).


Then open your project and ask your AI assistant:



```
Build the code review graph for this project

```

The initial build takes ~10 seconds for a 500-file project. After that, the graph updates automatically on every file edit and git commit.


## How It Works


[![How your AI assistant uses the graph: User asks for review, AI checks MCP tools, graph returns blast radius and risk scores, AI reads only what matters](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram7_mcp_integration_flow.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram7_mcp_integration_flow.png)
Your repository is parsed into an AST with Tree-sitter, stored as a graph of nodes (functions, classes, imports) and edges (calls, inheritance, test coverage), then queried at review time to compute the minimal set of files your AI assistant needs to read.


[![Architecture pipeline: Repository to Tree-sitter Parser to SQLite Graph to Blast Radius to Minimal Review Set](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram2_architecture_pipeline.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram2_architecture_pipeline.png)
### Blast-radius analysis


When a file changes, the graph traces every caller, dependent, and test that could be affected. This is the "blast radius" of the change. Your AI reads only these files instead of scanning the whole project.


[![Blast radius visualization showing how a change to login() propagates to callers, dependents, and tests](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram3_blast_radius.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram3_blast_radius.png)
### Incremental updates in < 2 seconds


On every git commit or file save, a hook fires. The graph diffs changed files, finds their dependents via SHA-256 hash checks, and re-parses only what changed. A 2,900-file project re-indexes in under 2 seconds.


[![Incremental update flow: git commit triggers diff, finds dependents, re-parses only 5 files while 2,910 are skipped](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram4_incremental_update.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram4_incremental_update.png)
### The monorepo problem, solved


Large monorepos are where token waste is most painful. The graph cuts through the noise — 27,700+ files excluded from review context, only ~15 files actually read.


[![Next.js monorepo: 27,732 files funnelled through code-review-graph down to ~15 files — 49x fewer tokens](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram6_monorepo_funnel.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram6_monorepo_funnel.png)
### 19 languages + Jupyter notebooks


[![19 languages organized by category: Web, Backend, Systems, Mobile, Scripting, plus Jupyter/Databricks notebook support](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram9_language_coverage.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram9_language_coverage.png)
Full Tree-sitter grammar support for functions, classes, imports, call sites, inheritance, and test detection in every language. Plus Jupyter/Databricks notebook parsing (`.ipynb`) with multi-language cell support (Python, R, SQL), and Perl XS files (`.xs`).


## Benchmarks


[![Benchmarks across real repos: 4.9x to 27.3x fewer tokens, higher review quality](https://github.com/tirth8205/code-review-graph/raw/main/diagrams/diagram5_benchmark_board.png)](https://github.com/tirth8205/code-review-graph/blob/main/diagrams/diagram5_benchmark_board.png)
All numbers come from the automated evaluation runner against 6 real open-source repositories (13 commits total). Reproduce with `code-review-graph eval --all`. Raw data in [`evaluate/reports/summary.md`](https://github.com/tirth8205/code-review-graph/blob/main/evaluate/reports/summary.md).


 **Token efficiency: 8.2x average reduction (naive vs graph)**   
 The graph replaces reading entire source files with a compact structural context covering blast radius, dependency chains, and test coverage gaps.

 

| Repo | Commits | Avg Naive Tokens | Avg Graph Tokens | Reduction |
| --- | --- | --- | --- | --- |
| express | 2 | 693 | 983 | 0.7x |
| fastapi | 2 | 4,944 | 614 | 8.1x |
| flask | 2 | 44,751 | 4,252 | 9.1x |
| gin | 3 | 21,972 | 1,153 | 16.4x |
| httpx | 2 | 12,044 | 1,728 | 6.9x |
| nextjs | 2 | 9,882 | 1,249 | 8.0x |
| **Average** | **13** |  |  | **8.2x** |

 **Why express shows <1x:** For single-file changes in small packages, the graph context (metadata, edges, review guidance) can exceed the raw file size. The graph approach pays off on multi-file changes where it prunes irrelevant code.

 
 **Impact accuracy: 100% recall, 0.54 average F1**   
 The blast-radius analysis never misses an actually impacted file (perfect recall). It over-predicts in some cases, which is a conservative trade-off — better to flag too many files than miss a broken dependency.

 

| Repo | Commits | Avg F1 | Avg Precision | Recall |
| --- | --- | --- | --- | --- |
| express | 2 | 0.667 | 0.50 | 1.0 |
| fastapi | 2 | 0.584 | 0.42 | 1.0 |
| flask | 2 | 0.475 | 0.34 | 1.0 |
| gin | 3 | 0.429 | 0.29 | 1.0 |
| httpx | 2 | 0.762 | 0.63 | 1.0 |
| nextjs | 2 | 0.331 | 0.20 | 1.0 |
| **Average** | **13** | **0.54** | **0.38** | **1.0** |

 
 **Build performance**   
 

| Repo | Files | Nodes | Edges | Flow Detection | Search Latency |
| --- | --- | --- | --- | --- | --- |
| express | 141 | 1,910 | 17,553 | 106ms | 0.7ms |
| fastapi | 1,122 | 6,285 | 27,117 | 128ms | 1.5ms |
| flask | 83 | 1,446 | 7,974 | 95ms | 0.7ms |
| gin | 99 | 1,286 | 16,762 | 111ms | 0.5ms |
| httpx | 60 | 1,253 | 7,896 | 96ms | 0.4ms |

 
 **Limitations and known weaknesses**   
 * **Small single-file changes:** Graph context can exceed naive file reads for trivial edits (see express results above). The overhead is the structural metadata that enables multi-file analysis.
* **Search quality (MRR 0.35):** Keyword search finds the right result in the top-4 for most queries, but ranking needs improvement. Express queries return 0 hits due to module-pattern naming.
* **Flow detection (33% recall):** Only reliably detects entry points in Python repos (fastapi, httpx) where framework patterns are recognized. JavaScript and Go flow detection needs work.
* **Precision vs recall trade-off:** Impact analysis is deliberately conservative. It flags files that *might* be affected, which means some false positives in large dependency graphs.

 
## Features




| Feature | Details |
| --- | --- |
| **Incremental updates** | Re-parses only changed files. Subsequent updates complete in under 2 seconds. |
| **19 languages + notebooks** | Python, TypeScript/TSX, JavaScript, Vue, Go, Rust, Java, Scala, C#, Ruby, Kotlin, Swift, PHP, Solidity, C/C++, Dart, R, Perl, Lua, Jupyter/Databricks (.ipynb) |
| **Blast-radius analysis** | Shows exactly which functions, classes, and files are affected by any change |
| **Auto-update hooks** | Graph updates on every file edit and git commit without manual intervention |
| **Semantic search** | Optional vector embeddings via sentence-transformers, Google Gemini, or MiniMax |
| **Interactive visualisation** | D3.js force-directed graph with edge-type toggles and search |
| **Local storage** | SQLite file in `.code-review-graph/`. No external database, no cloud dependency. |
| **Watch mode** | Continuous graph updates as you work |
| **Execution flows** | Trace call chains from entry points, sorted by criticality |
| **Community detection** | Cluster related code via Leiden algorithm or file grouping |
| **Architecture overview** | Auto-generated architecture map with coupling warnings |
| **Risk-scored reviews** | `detect_changes` maps diffs to affected functions, flows, and test gaps |
| **Refactoring tools** | Rename preview, dead code detection, community-driven suggestions |
| **Wiki generation** | Auto-generate markdown wiki from community structure |
| **Multi-repo registry** | Register multiple repos, search across all of them |
| **MCP prompts** | 5 workflow templates: review, architecture, debug, onboard, pre-merge |
| **Full-text search** | FTS5-powered hybrid search combining keyword and vector similarity |


## Usage


 **Slash commands**   
 

| Command | Description |
| --- | --- |
| `/code-review-graph:build-graph` | Build or rebuild the code graph |
| `/code-review-graph:review-delta` | Review changes since last commit |
| `/code-review-graph:review-pr` | Full PR review with blast-radius analysis |

 
 **CLI reference**   
 
```
code-review-graph install          # Auto-detect and configure all platforms
code-review-graph install --platform <name>  # Target a specific platform
code-review-graph build            # Parse entire codebase
code-review-graph update           # Incremental update (changed files only)
code-review-graph status           # Graph statistics
code-review-graph watch            # Auto-update on file changes
code-review-graph visualize        # Generate interactive HTML graph
code-review-graph wiki             # Generate markdown wiki from communities
code-review-graph detect-changes   # Risk-scored change impact analysis
code-review-graph register <path>  # Register repo in multi-repo registry
code-review-graph unregister <id>  # Remove repo from registry
code-review-graph repos            # List registered repositories
code-review-graph eval             # Run evaluation benchmarks
code-review-graph serve            # Start MCP server
```
 
 **22 MCP tools**   
 Your AI assistant uses these automatically once the graph is built.

 

| Tool | Description |
| --- | --- |
| `build_or_update_graph_tool` | Build or incrementally update the graph |
| `get_impact_radius_tool` | Blast radius of changed files |
| `get_review_context_tool` | Token-optimised review context with structural summary |
| `query_graph_tool` | Callers, callees, tests, imports, inheritance queries |
| `semantic_search_nodes_tool` | Search code entities by name or meaning |
| `embed_graph_tool` | Compute vector embeddings for semantic search |
| `list_graph_stats_tool` | Graph size and health |
| `get_docs_section_tool` | Retrieve documentation sections |
| `find_large_functions_tool` | Find functions/classes exceeding a line-count threshold |
| `list_flows_tool` | List execution flows sorted by criticality |
| `get_flow_tool` | Get details of a single execution flow |
| `get_affected_flows_tool` | Find flows affected by changed files |
| `list_communities_tool` | List detected code communities |
| `get_community_tool` | Get details of a single community |
| `get_architecture_overview_tool` | Architecture overview from community structure |
| `detect_changes_tool` | Risk-scored change impact analysis for code review |
| `refactor_tool` | Rename preview, dead code detection, suggestions |
| `apply_refactor_tool` | Apply a previously previewed refactoring |
| `generate_wiki_tool` | Generate markdown wiki from communities |
| `get_wiki_page_tool` | Retrieve a specific wiki page |
| `list_repos_tool` | List registered repositories |
| `cross_repo_search_tool` | Search across all registered repositories |

 **MCP Prompts** (5 workflow templates): `review_changes`, `architecture_map`, `debug_issue`, `onboard_developer`, `pre_merge_check`

 
 **Configuration**   
 To exclude paths from indexing, create a `.code-review-graphignore` file in your repository root:

 
```
generated/**
*.generated.ts
vendor/**
node_modules/**

```
 Optional dependency groups:

 
```
pip install code-review-graph[embeddings]          # Local vector embeddings (sentence-transformers)
pip install code-review-graph[google-embeddings]   # Google Gemini embeddings
pip install code-review-graph[communities]         # Community detection (igraph)
pip install code-review-graph[eval]                # Evaluation benchmarks (matplotlib)
pip install code-review-graph[wiki]                # Wiki generation with LLM summaries (ollama)
pip install code-review-graph[all]                 # All optional dependencies
```
 
## Contributing



```
git clone https://github.com/tirth8205/code-review-graph.git
cd code-review-graph
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
pytest
```

 **Adding a new language**   
 Edit `code_review_graph/parser.py` and add your extension to `EXTENSION_TO_LANGUAGE` along with node type mappings in `_CLASS_TYPES`, `_FUNCTION_TYPES`, `_IMPORT_TYPES`, and `_CALL_TYPES`. Include a test fixture and open a PR.

 
## Licence


MIT. See [LICENSE](https://github.com/tirth8205/code-review-graph/blob/main/LICENSE).


[code-review-graph.com](https://code-review-graph.com)


`pip install code-review-graph && code-review-graph install`  

Works with Claude Code, Cursor, Windsurf, Zed, Continue, OpenCode, and Antigravity