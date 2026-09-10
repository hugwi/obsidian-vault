---
created: 2026-09-08
categories:
  - "[[Raw]]"
domain:
  - agentic-engineering
theme: context-engineering
subtheme:
  - retrieval-rag
  - cost-tokens
  - system-prompt-rules
rating: 7
action: implement
read: true
tags:
  - agentic-engineering
  - code-graphs
  - codebase-intelligence
  - token-efficiency
  - architecture-enforcement
  - mcp
source:
  - https://github.com/trailhq/Graft
  - https://github.com/repowise-dev/repowise
  - https://github.com/sverweij/dependency-cruiser
---

# Code graph tools - Graft Repowise and Dependency Cruiser

> [!todo] Implementation candidate - rating 7
> Run a controlled pilot of **one** agent-context index, starting with Graft for the lowest operational cost. Keep linting or Dependency Cruiser as a separate deterministic architecture gate. Do not expose Graft and Repowise to the agent simultaneously during the pilot.

## Decision in one paragraph

These tools are related but do not all compete. **Graft and Repowise are substitutes at the agent-context layer**: both pre-index code so an agent performs fewer searches, file reads, and tool calls. Graft is the smaller, repo-native option; Repowise is a broader repository-intelligence system. **Dependency Cruiser and linters are complementary hard gates**: they reject forbidden dependency structures in CI. CodeQL or Joern remain complementary when semantic security or data-flow analysis is required. Tree-sitter, Babel, and compiler APIs are building blocks rather than finished alternatives.

## Capability map

| Layer | Examples | Primary job | Enforces CI? |
|---|---|---|---:|
| Syntax and semantic primitives | Tree-sitter, Babel, ts-morph, compiler APIs | Parse code for custom tools | No, not alone |
| Local lint rules | ESLint, `no-restricted-imports`, Nx boundaries | Immediate file/package constraints | Yes |
| Repository dependency policy | Dependency Cruiser | Direct/transitive module rules, cycles, orphans, visualisation | Yes |
| Agent context index | Graft **or** Repowise | Reduce rediscovery, source reads, tool calls, and context tokens | Usually advisory |
| System architecture conformance | Repowise workspace mode | Allow/deny relationships between services and repositories | Yes |
| Semantic security/data flow | CodeQL, Joern | Taint flow, vulnerability and semantic queries | Yes |

## Graft

**Best fit:** lightweight local context for Codex, Claude Code, Cursor, and other MCP agents.

- Builds a deterministic Tree-sitter symbol graph: files, functions, classes, methods, imports, calls, references, inheritance, and implementations.
- Stores a local, regenerable graph as JSON plus readable Markdown cards; no persistent database or indexing daemon is required.
- Refreshes the structural graph before a query, including working-tree edits.
- Retrieves code with lexical/BM25-style scoring plus personalised PageRank; no vector database.
- Offers focused operations for code search, exhaustive search, file API skeletons, callers, repository maps, freshness, blast radius, and visualisation.
- Optional `--deep` mode adds LLM-generated concept nodes, symbol summaries, and crux excerpts; the structural graph needs no model.
- MIT licensed.

### Token-efficiency claim

Graft positions token reduction as its central product outcome. Its repository reports **42% fewer tokens** in a controlled question benchmark and **23% fewer tokens** in its 50-instance SWE-bench comparison, alongside fewer tool calls and lower latency. These are self-published experiments and not a direct comparison with Repowise.

## Repowise

**Best fit:** a broader engineering-intelligence layer spanning agents, developers, pull requests, and multiple repositories.

- Builds a file-and-symbol graph with confidence-stamped resolution origins and framework-aware edges.
- Adds Git history, ownership, churn, co-change, bug history, test intelligence, coverage, decisions, dead-code analysis, security checks, and code-health/refactoring signals.
- Persists the index in SQLite or PostgreSQL, with LanceDB for vector retrieval.
- Uses full-text plus vector search, reciprocal-rank fusion, PageRank, and graph expansion.
- Exposes task-shaped MCP tools, CLI commands, hooks, a dashboard, VS Code integration, and a PR bot.
- Keyless `--no-prose` indexing is deterministic; model-written documentation is optional.
- AGPL-3.0, with a commercial licence available.

### Token-efficiency claim

Repowise explicitly targets token saving. It reports:

- **31.6% less agent output** across 43 Django questions, with 3.8 rather than 7.2 tool calls and 3.0 rather than 7.2 files opened.
- **97.2% smaller context payload** in a narrower `get_context` experiment: 393 rather than 13,984 tokens. Repowise correctly states that this is a retrieval-payload reduction, not end-to-end agent savings.
- Reversible `repowise distill` compression for noisy test, Git, and shell output, with reported examples of 61% fewer pytest-output tokens and 89% fewer Git-log tokens.

Graft and Repowise use different corpora, models, tasks, and denominators. Their headline percentages must not be compared as if they were a shared benchmark.

## Dependency Cruiser and linters

**Best fit:** deterministic architecture enforcement inside JavaScript and TypeScript repositories.

A local linter can efficiently reject direct imports such as `ui -> database`. Dependency Cruiser becomes useful when the rule needs the whole module graph:

- direct or transitive reachability;
- circular dependencies and constraints on what a cycle passes through;
- orphaned or unreachable modules;
- required, allowed, and forbidden relationships;
- runtime, type-only, npm, development, optional, and unresolved dependency types;
- TypeScript paths, package exports, workspaces, and Webpack aliases;
- baselines, CI reporting, and graph visualisation.

If ESLint, Nx, ArchUnit, Import Linter, or an equivalent native tool already expresses every required constraint, Dependency Cruiser may add little beyond graph-wide reporting and visualisation.

## Repowise architecture conformance

Repowise also provides a hard architecture check, but at a different altitude. In workspace mode it evaluates allow/deny rules over **service and repository relationships**, including HTTP, gRPC, event, package, and database edges. Rules use `*`, `tag:<name>`, or service/repository globs; explicit allow rules whitelist exceptions. `repowise workspace check` reports violations and service cycles and exits non-zero for CI.

Therefore:

- Use a linter or Dependency Cruiser for boundaries **within** a codebase.
- Use Repowise conformance for boundaries **between** services and repositories.
- Repowise excludes Git co-change edges from conformance because historical correlation is not proof of a structural dependency.

## Complementarity

| Combination | Verdict | Reason |
|---|---|---|
| Graft + Dependency Cruiser | Strongly complementary | Agent navigation plus deterministic module policy |
| Repowise + Dependency Cruiser | Complementary with some overlap | Repository intelligence plus fine-grained JS/TS policy |
| Graft + CodeQL | Strongly complementary | Agent context plus security/data flow |
| Repowise + CodeQL | Strongly complementary | Engineering intelligence plus deeper semantic security |
| Graft + Repowise | Mostly substitutes | Duplicate indexes and overlapping MCP choices |
| ESLint/Nx + Dependency Cruiser | Optional layering | Fast direct feedback plus graph-wide/transitive checks |

## Implementation plan

### Phase 1 - establish a baseline

- [ ] Select 10 representative tasks: navigation, bug diagnosis, multi-file change, test selection, and blast-radius questions.
- [ ] Record total model input/output tokens, tool calls, source-file reads, wall time, answer correctness, and missed/incorrect graph edges.
- [ ] Keep the agent, model, prompts, repository commit, and task order fixed.

### Phase 2 - pilot Graft

- [ ] Install Graft in one representative repository and build the deterministic graph without `--deep`.
- [ ] Expose only Graft's MCP context tools during the treatment run.
- [ ] Repeat the same 10 tasks and compare against the baseline.
- [ ] Inspect false or missing call edges before trusting blast-radius output.
- [ ] Accept if it reduces total task tokens or wall time by at least 20% without lowering correctness or hiding required companion changes.

### Phase 3 - decide whether Repowise is warranted

- [ ] Pilot Repowise separately only if Git risk, ownership, test selection, decisions, code health, dashboards, PR analysis, or cross-repository contracts are required.
- [ ] Start with `--no-prose` so optional indexing-model cost does not distort the comparison.
- [ ] Evaluate index time, memory, freshness workflow, MCP response quality, and AGPL/commercial implications alongside task metrics.

### Phase 4 - add deterministic architecture gates

- [ ] Keep existing linter boundaries for fast editor feedback.
- [ ] Add Dependency Cruiser only for missing graph-wide requirements such as transitive reachability, cycles, orphans, or visualisation.
- [ ] In a service estate, add Repowise workspace conformance for cross-service structural rules.
- [ ] Fail CI on new violations and baseline legacy violations rather than introducing a permanently noisy gate.

## Guardrails

- A generated graph is evidence, not truth. Reflection, dependency injection, runtime registration, constructed dynamic imports, generated code, and undocumented network calls can evade static resolution.
- Generated summaries and concept nodes must not be treated as authoritative architecture decisions.
- Measure total agent-loop cost, not a selectively small tool response.
- Keep one primary context provider so the agent has an unambiguous retrieval path.
- Preserve deterministic linters and tests as the enforcement layer; an MCP context tool is not a quality gate by itself.

## Related notes

- [[Agentic Engineering]]
- [[Agentic Engineering — Implementation Guide]]
- [[Taking Frontend Architecture Serious with dependency-cruiser]]
- [[Visualize TypeScript Dependencies of Changed Files in a Pull Request Using dependency-cruiser-report-action]]
- [[repowise-devrepowise Codebase intelligence for AI and humans code health scores, auto-generated docs, git analytics, dead code detection, and architectural decisions via MCP.|Repowise source capture]]
- [[Maintainability sensors for coding agents]]

## Sources

- [Graft](https://github.com/trailhq/Graft)
- [Repowise](https://github.com/repowise-dev/repowise)
- [Dependency Cruiser](https://github.com/sverweij/dependency-cruiser)
- [Dependency Cruiser rules reference](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-reference.md)
- [Repowise intelligence layers](https://github.com/repowise-dev/repowise/blob/main/docs/layers/INTELLIGENCE_LAYERS.md)
- [Repowise architecture conformance](https://github.com/repowise-dev/repowise/blob/main/docs/scale/WORKSPACES.md#architecture-conformance)

