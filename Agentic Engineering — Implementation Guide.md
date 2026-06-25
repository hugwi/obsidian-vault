---
created: 2026-06-25
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - agentic-engineering
  - implementation
---

# Agentic Engineering — Implementation Guide

What to actually **build/adopt** from the 220 clipped notes, organised by the same problem-themes
as [[Agentic Engineering]]. Each theme lists ranked implementables (with effort + source note +
repo), a **comparison table** where 2+ notes pitch competing tools for the same job, and quick wins.

> Derived by reading every note per theme. Repos/URLs are only those cited in the notes.
> Sister notes: [[Agentic Engineering]] (browse by theme) · [[Agentic Engineering — Trends 2026]] (landscape).

---

## ⭐ Start here — highest leverage across all themes
Ranked by impact ÷ effort. Most are <1 day.

1. **Lean CLAUDE.md + progressive disclosure** (Low) — root <60 lines, push domain rules to `docs/*.md` with trigger pointers. Cuts every-session context. → *context-engineering*
2. **Prompt/prefix caching + static↔dynamic prompt boundary** (Low) — 10% cache cost vs 100%; split stable instructions from per-task. → *context-engineering, agents-models*
3. **RTK output compressor** (Low) — `rtk init -g --auto-patch`; 60–90% fewer tokens on git/test/lint output. → *context-engineering* · https://github.com/rtk-ai/rtk
4. **Karpathy 4 rules in CLAUDE.md** (Low) — think-first / simplicity / surgical / goal-driven. Stops overengineering. → *workflow-phases-gates* · https://github.com/multica-ai/andrej-karpathy-skills
5. **Mutation testing on changed files** (Low) — Stryker on the PR diff; proves tests catch bugs, keeps agents honest. → *quality-gates* · https://stryker-mutator.io
6. **ESLint 5-rule guardrail** (Low) — no-comments, max-2-params, 50 lines/fn, 250 lines/file, no-magic-numbers; agent can't edit the config. → *quality-gates*
7. **Adversarial self-review prompt** (Low) — "pretend you hate this diff — what's broken?" on `git diff`. Catches first-pass misses. → *quality-gates*
8. **TASK_STATE.md / progress.md handoff** (Low) — durable checkpoint file that survives compaction + session resets. → *context-engineering, workflow-phases-gates*
9. **Skills over subagents** (Low) — lazy-loaded `SKILL.md` (~100 tok at startup) instead of eager subagents; portable across tools. → *multi-agent-orchestration*
10. **LiteLLM model routing** (Low–Med) — cheap model for simple tasks, Opus for hard; 30–50% spend cut + fallback chains. → *agents-models, productivity-measurement* · https://github.com/BerriAI/litellm
11. **Git worktree + devcontainer isolation** (Med) — clean branch/sandbox per parallel agent task. → *multi-agent-orchestration*
12. **Browser MCPs for E2E** (Low) — `claude mcp add playwright` / `chrome-devtools`; English-language UI tests. → *human-ux-frontend*
13. **Prompt Coach skill** (Low) — audits your `~/.claude` logs for model overspend + prompt quality. → *productivity-measurement* · https://github.com/hancengiz/claude-code-prompt-coach-skill

> **Biggest structural bets (Med–High, schedule deliberately):** a knowledge-graph index for
> token reduction at scale (code-review-graph / Graphify), a structured workflow (QRSPI / BMAD /
> Craftsman), an eval harness (DeepEval / OpenAI Evals), and DORA instrumentation (middleware/Faros).

---

## 🧠 Context engineering

### What to implement (ranked)
1. **Prompt & prefix caching** (Low) — cache repeated system prompts/rules; 10% cache cost vs 100% input. — [[Effective Context Engineering for AI Agents|Effective Context Engineering for AI Agents]] · https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
2. *[[tirth8205code-review-graph Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8× fewer tokens on reviews and up to 49× on daily coding tasks.|code-review-graph]]* (Med) — tree-sitter AST → SQLite knowledge graph; blast-radius analysis, 6.8× fewer tokens on reviews, 49× on daily tasks, 19 languages. — [[tirth8205code-review-graph Local knowledge graph for Claude Code. Builds a persistent map of your codebase so Claude reads only what matters — 6.8× fewer tokens on reviews and up to 49× on daily coding tasks.|code-review-graph]], [[Graphify + code-review-graph Build a Self-Updating Knowledge Graph for Claude Code and other AI Coding Agent|Graphify + code-review-graph]] · https://github.com/tirth8205/code-review-graph
3. **Context Mode MCP** (Med) — sandboxes tool outputs (56KB→299B), FTS5 index, survives compaction, up to 99% per-file reduction. — [[Claude Code is Expensive. This MCP Server Fixes It (Context Mode)|Claude Code is Expensive. This MCP Server Fixes It]]
4. **Session handoff files (TASK_STATE.md + SESSION_HANDOFF.md)** (Low) — structured checkpoint surviving compaction. — [[Why Claude Code Forgets What It Was Doing (And How to Fix It)|Why Claude Code Forgets What It Was Doing]]
5. **RTK (Rust Token Killer)** (Low) — CLI proxy cutting git/test/lint output 60–90%; single binary, auto-rewrite hook. — [[rtk-airtk CLI proxy that reduces LLM token consumption by 60-90% on common dev commands. Single Rust binary, zero dependencies|rtk]] · https://github.com/rtk-ai/rtk
6. **Dirac (hash-anchored edits)** (Med) — AST-aware edits avoid line-drift; ~64.8% cheaper, multi-file batching. — [[GitHub - dirac-rundirac Open Source Coding Agent singularly focused efficiency. Reduces API costs by 50-80% vs other agent AND improves the code quality at the same time. Uses Hash Anchored edits, massively parallel operations, AST manipulation and m|dirac]] · https://github.com/dirac-run/dirac
7. **CLAUDE.md progressive disclosure** (Low) — root <60–100 lines; move task rules to `docs/`, point with triggers. — [[CLAUDE.md Writing Guide Context Engineering for AI CLI Tools|CLAUDE.md Writing Guide]], [[Stop Bloating Your CLAUDE.md Progressive Disclosure for AI Coding Tools|Stop Bloating Your CLAUDE.md]]
8. **Graphify** (Med) — multi-modal knowledge graph (code + PDFs/images), 70× fewer tokens at scale. — [[This Tool Fixes AI Coding at Scale with 70x Fewer Tokens (Graphify)|This Tool Fixes AI Coding at Scale with 70x Fewer Tokens]] · https://github.com/safishamsi/graphify
9. **Mem0 + reflection layer** (Med) — persistent layered memory (raw → summary → insight), prevents memory rot. — [[I built Claude's Dreams feature myself using Mem0 and Codex, and it changed how I code|I built Claude's Dreams feature… using Mem0]] · https://mem0.ai
10. **Semantic retrieval (Turbopuffer + Voyage)** (Med) — embeddings cut wasted file reads on unknown codebases. — [[Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer|Benchmarking semantic code retrieval on Claude Code]] · https://turbopuffer.com
11. **TOON (Token-Oriented Object Notation)** (Low) — JSON replacement for prompts; <50% tokens on uniform arrays. — [[Stop Wasting Tokens A Smarter Alternative to JSON for LLM Pipelines|Stop Wasting Tokens]] · https://toon-format.dev
12. **Caliber / rule-porter** (Low) — auto-generate & sync CLAUDE.md ↔ `.cursor/rules` ↔ AGENTS.md. — [[caliber-ai-orgai-setup Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files for Claude Code, Cursor, and Codex.|caliber]], [[nedcodes-okrule-porter Convert AI IDE rules between Cursor, Windsurf, CLAUDE.md, AGENTS.md, and Copilot. Bidirectional. Zero dependencies.|rule-porter]] · https://github.com/caliber-ai-org/ai-setup · https://github.com/nedcodes-ok/rule-porter

### Comparisons
| Option | Best for | Tradeoff | Repo |
|---|---|---|---|
| code-review-graph | pure code (backend/monorepo) | code only; 6.8× | https://github.com/tirth8205/code-review-graph |
| Graphify | multi-modal (code + docs + images) | heavier; 70× at scale | https://github.com/safishamsi/graphify |
| Mem0 (layered) | control: filters, raw/summary/insight | manual upkeep | https://mem0.ai |
| Anthropic native memory | auto-synced, project-scoped | less control, 24h sync | — |
| RTK (CLI proxy) | command output compression | per-command | https://github.com/rtk-ai/rtk |
| Context Mode (MCP) | tool-output sandboxing | per-file, MCP setup | — |
| Turbopuffer (semantic) | fuzzy/behavioural queries | higher token cost | https://turbopuffer.com |
| AST graph (CRG) | structural (callers/imports) | precise, less fuzzy recall | https://github.com/tirth8205/code-review-graph |

### Quick wins
- Trim CLAUDE.md to <60 lines, move gotchas to `docs/` with IMPORTANT triggers (~30 min).
- `rtk init -g --auto-patch` — 60–90% off git/test/lint output (~45 min).
- Add `.claude/task-state.md` (current/done/next/open-questions), update each step — survives compaction.

---

## 📋 Work breakdown & specs

### What to implement (ranked)
1. **Spec-driven lifecycle (Specify→Clarify→Plan→Tasks→Analyze→Implement→QC)** (High) — gated workflow producing `spec.md`/`plan.md`/`tasks.md` + `.qc-passed` markers. — [[A framework for Spec-Driven Development.|A framework for Spec-Driven Development]] · https://sdd-pilot.szaszattila.com
2. **JSONC design-spec + codegen** (Low) — machine-readable JSON-with-comments bridging design intent → code. — [[Claude Code Skills, Plugins, and the JSONC Design Spec Trick That Changed My Workflow|Claude Code Skills: JSONC Design Spec Trick]] · https://deloughry.co.uk/posts/claude-code--skills-plugins
3. **PRD → tasks decomposition pipeline** (Med) — PRD → Socratic clarify → multi-approach → sub-agent feedback → traceable tasks. — [[2.1 Write a PRD|2.1 Write a PRD]] · https://ccforpms.com/advanced/write-prd
4. **Living-spec orchestration (Intent)** (High) — bidirectional spec↔code sync across services; stops spec drift. — [[6 Best Spec-Driven Development Tools for AI Coding in 2026|6 Best SDD Tools]] · https://www.augmentcode.com/product/intent
5. **EARS notation + Given/When/Then + delta markers** (Low) — requirements syntax & ADDED/MODIFIED/REMOVED for brownfield. — [[Understanding Spec-Driven-Development Kiro, spec-kit, and Tessl|Understanding Spec-Driven-Development]] · https://kiro.dev · https://github.com/github/spec-kit
6. **Context lifecycle (CDLC)** (Med) — treat skills/prompts/rules as artifacts: lint, eval suites, CI, error budgets. — [[Context Is the New Code — Patrick Debois, Tessl|Context Is the New Code (Tessl)]]

### Comparisons
| Aspect | Living/bidirectional | Static one-shot | Delta/proposal |
|---|---|---|---|
| Tool | Intent | Kiro, Spec-Kit | OpenSpec |
| Best for | multi-service sync | single-repo | brownfield iteration |
| Tradeoff | heavier, parallel agents | manual reconcile | proposal gates |
| Link | augmentcode.com/product/intent | https://github.com/github/spec-kit | https://github.com/Fission-AI/OpenSpec |

Contracts: **Pydantic models** (optional validation, Python-native) vs **JSON-Schema tool defs** (language-agnostic, required validation) — pick by stack.

### Quick wins
- Reusable `design.jsonc` template (typography/colors/layout/motion); test on one page.
- Delta-marker task template (ADDED/MODIFIED/REMOVED) for every feature.
- Generate Given/When/Then acceptance criteria from a YAML feature def; embed FR-### traceability.

---

## ✅ Quality gates

### What to implement (ranked)
1. **OpenAI Evals** (Med) — eval harness + benchmark registry for LLM/skill testing. — [[Testing Agent Skills Systematically with Evals OpenAI Developers|Testing Agent Skills Systematically with Evals]] · https://github.com/openai/evals
2. **DeepEval** (Med) — Python evals: G-Eval, RAG + agent metrics (task completion, tool correctness, plan adherence). — [[Practical Guide to Evaluating and Testing Agent Skills|Practical Guide to Evaluating Agent Skills]] · https://github.com/confident-ai/deepeval
3. **Claude Code E2E runner + Playwright** (Med) — natural-language browser tests, self-adapt to UI changes, no selectors. — [[Automating e2e manual labor with Claude Code|Automating e2e manual labor with Claude Code]] · https://github.com/arielb135/claude-code-e2e-demo
4. **Mutation testing (Stryker)** (Low) — break code to verify tests catch it; run on changed files only. — [[Keep your coding agent on task with mutation testing|Keep your coding agent on task with mutation testing]] · https://stryker-mutator.io
5. **Keploy** (Med) — record API/DB calls → auto-generate tests + mocks from real traffic. — [[GitHub - keploykeploy Shadow Test generation for Developers. Generate tests and stubs for your application that actually work!|keploy]] · https://github.com/keploy/keploy
6. **LLM-as-judge rubric grading** (Low) — structured-output schemas for qualitative checks beside deterministic regex. — [[Practical Guide to Evaluating and Testing Agent Skills|Practical Guide to Evaluating Agent Skills]]
7. **ESLint 5-rule guardrail** (Low) — no-comments, max-2-params, 50 lines/fn, 250 lines/file, no-magic-numbers; block config edits. — [[ESLint as AI Guardrails The Rules That Make AI Code Readable|ESLint as AI Guardrails]]
8. **Code Health MCP (CodeScene)** (Med) — health review → detect risk → refactor loop → re-measure. — [[Strengthening the Inner Developer Loop Turn AI Into a Reliable Engineering Partner|Strengthening the Inner Developer Loop]] · https://github.com/codescene-oss/codescene-mcp-server
9. **Greptile / Greploop** (Med) — PR review iterating to 5/5 confidence; GitHub/GitLab/Perforce. — [[skillsgreploopSKILL.md at main · greptileaiskills|greploop SKILL]] · https://github.com/greptileai/skills
10. **Mypy `assert_never()` exhaustiveness** (Low) — unhandled enum/union cases caught at type-check, gated in CI. — [[Exhaustiveness Checking with Mypy|Exhaustiveness Checking with Mypy]]
11. **Adversarial self-review prompt** (Low) — "pretend you hate this — what's broken?" on the diff. — [[So I stumbled across this prompt hack a couple weeks back and honestly I wish I could unlearn it.|So I stumbled across this prompt hack…]]
12. **Bumblebee supply-chain scanner** (Low) — read-only scan of npm/Go/Bun/MCP configs for exposure. — [[Perplexity Open-Sourced a Scanner Every Dev Should Know (Bumblebee)|Bumblebee]] · https://github.com/perplexity-ai/bumblebee

### Comparisons
| Option | Best for | Tradeoff | Repo |
|---|---|---|---|
| OpenAI Evals | benchmarks + registry | OpenAI-aligned | https://github.com/openai/evals |
| DeepEval | agentic metrics, private data | Python-first | https://github.com/confident-ai/deepeval |
| Greptile/Greploop | iterative PR review to 5/5 | enterprise, external | https://github.com/greptileai/skills |
| CodeRabbit | CI-first review | not iterative | — |
| native `/code-review` skill | free, local, full control | DIY upkeep | — |
| ESLint guardrails | enforced, no-escape | needs hooks | — |
| CLAUDE.md rules | flexible | agent can reason around | — |

### Quick wins
- Mypy `assert_never()` on enums/unions → CI gate (30 min).
- Stryker on PR diff — reveals 5–10% dead tests (~1 h).
- ESLint 5 core rules into pre-commit (45 min).
- DeepEval baseline: 1 skill, 10–15 cases, deterministic + 1 judge pass (2 h).

---

## 🔍 Comprehension & maintainability

### What to implement (ranked)
1. **dependency-cruiser** (Low) — enforce/visualise module architecture, circular deps, unused exports; ESLint + CI + PR Mermaid graphs. — [[Taking Frontend Architecture Serious with dependency-cruiser|Taking Frontend Architecture Serious]], [[Visualize TypeScript Dependencies of Changed Files in a Pull Request Using dependency-cruiser-report-action|Visualize TypeScript Dependencies]] · https://github.com/sverweij/dependency-cruiser
2. **Fallow** (Low) — dead code / duplication / complexity for JS-TS; MCP + VS Code; JSON for agents; baseline enforcement (fix new only). — [[Fallow The Code Intelligence Tool Every Claude User Needs|Fallow: The Code Intelligence Tool]]
3. **Custom exception hierarchies + `raise … from`** (Low) — domain-defined errors, preserved root cause; better tracebacks for AI code. — [[Should we use custom exceptions in Python|Should we use custom exceptions in Python]]
4. **Tree-sitter semantic graphs for deterministic review** (Med) — move ~75% of manual review feedback into automated AST checks. — [[How long before we stop reading the code|How long before we stop reading the code]]
5. **Spec-driven upstream review** (Low–Med) — review intent + acceptance criteria *before* generation; humans judge plan, machines validate impl. — [[How long before we stop reading the code|How long before we stop reading the code]]
6. **Theory-building docs** (Med) — capture *why* code exists (design rationale) alongside code/ADRs so humans + agents keep the theory. — [[Programming as Theory Building · GitHub|Programming as Theory Building]]

### Comparisons
| Option | Best for | Tradeoff | Repo |
|---|---|---|---|
| dependency-cruiser | architecture enforce + viz | JS/TS only, no runtime | https://github.com/sverweij/dependency-cruiser |
| Fallow | dead code + complexity + dup | JS/TS, paid runtime tier | — |
| ESLint no-restricted-imports | quick import rules | editor-only, no viz | — |
| deterministic AST checks | consistency, repeatable | upfront rule investment | — |
| AI code review | flexible, semantic | non-deterministic, costly | — |

### Quick wins
- dependency-cruiser GitHub Action → Mermaid blast-radius on PRs (~30 min).
- Define 5–10 domain exceptions + `raise from` everywhere (~1 h).
- Bucket last 100 PR comments into deterministic / test-able / judgment → backlog of AST checks (~2 h).

---

## 🤖 Multi-agent orchestration

### What to implement (ranked)
1. **Skills-based capability dispatch** (Low) — modular lazy-loaded skills over subagents for context efficiency. — [[Stop Building Subagents. Start Writing Skills.|Stop Building Subagents. Start Writing Skills.]] · https://github.com/vercel-labs/skills
2. **QRSPI/CRISPY orchestration** (Med) — phased state machine with context firewalls between agents + approval gate. — [[dynaptikcrispy CRISPY (how QRSPI sounds to me phonetically) is a multi-agent orchestration plugin for agentic AI coding. It implements an 8-phase state machine based on the QRSPI methodology (Question, Research, Structure, Plan, Implement).|CRISPY]] · https://github.com/dynaptik/crispy
3. **Flux — Kanban board over MCP** (Med) — tasks exposed via MCP, CLI-first (`flux ready`), git-native, dependency tracking. — [[Flux A Kanban Board That Speaks MCP|Flux: A Kanban Board That Speaks MCP]] · https://github.com/sirsjg/flux
4. **Multica platform** (High) — self-hosted orchestration: assign/track tasks, spawn worktree-isolated agents, schedule recurring work. — [[multica-aimultica The open-source managed agents platform. Turn coding agents into real teammates — assign tasks, track progress, compound skills.|Multica]] · https://github.com/multica-ai/multica
5. **Git worktree + devcontainer isolation** (Med) — `git worktree add` + devcontainer per agent task; safe parallelism. — [[Playing Nicely With Git Worktrees And DevContainers|Playing Nicely With Git Worktrees And DevContainers]]
6. **Browser sandbox (browser-use / Steel)** (Med) — headless browser control, self-host or cloud. — [[browser-usebrowser-use 🌐 Make websites accessible for AI agents. Automate tasks online with ease.|browser-use]], [[steel-devsteel-browser 🔥 Open Source Browser API for AI Agents & Apps. Steel Browser is a batteries-included browser sandbox that lets you automate the web without worrying about infrastructure.|steel-browser]] · https://github.com/browser-use/browser-use · https://github.com/steel-dev/steel-browser
7. **Tessl skill package manager** (Low) — registry + eval/regression for skills; `npx tessl i <org>/<skill>`. — [[The package manager for agent skills and context|The package manager for agent skills]] · https://github.com/vercel-labs/skills

### Comparisons
| Axis | Option A | Option B | Verdict |
|---|---|---|---|
| capability unit | Skills (lazy, ~100 tok, portable) | Subagents (eager, isolated, parallel) | Skills for portability/cost; subagents for parallel isolation |
| topology | Hierarchical orchestrator-worker | Peer-to-peer flat | Hierarchy = simpler/traceable; P2P = flexible but needs firewalls |
| isolation | git worktree (cheap, local) | devcontainer (OS consistency) / cloud sandbox (scalable) | worktree default; cloud when remote/scale |
| task board | Flux (offline, git-native, MCP) | GitHub Issues (heavy) / Multica (full UI) | Flux for agent-first minimalism |

### Quick wins
- Write one `.claude/skills/<x>/SKILL.md` (<5K tokens), test, reuse across tools (1–2 h).
- Stand up Flux MCP board, expose to agent config (2–3 h) · https://github.com/sirsjg/flux
- `git worktree add ./.work/agent main` + a devcontainer for parallel agent runs (1–2 h).

---

## 🔁 Workflow phases & gates

### What to implement (ranked)
1. **QRSPI phases (Question→Research→Structure→Plan→Implement)** (Med) — alignment before code; design review; vertical-slice execution. — [[From RPI to QRSPI Rebuilding the First Structured Workflow for Coding Agents|From RPI to QRSPI]] · https://alexlavaee.me/blog/from-rpi-to-qrspi
2. **Ralph loop** (Low) — bounded-context retry; fresh agent per cycle reads a progress file; reset before "overbaking" (~60% window). — [[# a brief history of ralph|a brief history of ralph]] · https://github.com/can1357/oh-my-pi
3. **Inner + outer harness architecture** (Med) — inner (model/tools/loop) + outer (lifecycle control, guides, sensors). — [[Harness engineering for coding agent users|Harness engineering for coding agent users]] · https://martinfowler.com/articles/harness-engineering.html
4. **Plan + Ralph + Verify (Craftsman)** (Med) — plan-mode spec → task files → coder subagent → inspector verify → retry, HITL at boundaries. — [[GitHub - gsemetCraftsman Craftsman is an powerful generic coding Agent for GitHub Copilot. It provides a Plan agent that does extensive interview to understand the need and a Ralph implementation loop to implement most plan in a single premium reques|Craftsman]] · https://github.com/gsemet/Craftsman
5. **Guides (feedforward) + sensors (feedback)** (Med) — computational sensors (lint/test/types) + inferential (LLM judge) run after each agent action. — [[Harness engineering for coding agent users|Harness engineering for coding agent users]]
6. **Hashline edit format** (Low) — high ROI; tag lines with content hash; edit by hash, reject on mismatch; 5–10× fewer edit failures, ~20% fewer output tokens. — [[I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed.|The Harness Problem]] · https://blog.can.ac/2026/02/12/the-harness-problem/
7. **Karpathy CLAUDE.md rules** (Low) — think / simplicity / surgical / goal-driven. — [[Karpathy's Skill Just Fixed Claude Code's Biggest Problem|Karpathy's Skill…]] · https://github.com/multica-ai/andrej-karpathy-skills
8. **Durable progress.md handoff** (Low) — completed/pending/next + verification notes; fresh session resumes from checkpoint.

### Comparisons
| Workflow | Best for | Tradeoff | Repo |
|---|---|---|---|
| QRSPI (8 stages) | complex greenfield | upfront ceremony | https://alexlavaee.me/blog/from-rpi-to-qrspi |
| Ralph (5-line loop) | refactors, bounded tasks | naive context mgmt | https://github.com/can1357/oh-my-pi |
| BMAD-METHOD | enterprise multi-team | heavy setup (PRD+arch) | https://github.com/bmad-code-org/BMAD-METHOD |
| Craftsman (plan+ralph) | Copilot/VS Code teams | task-file state machine | https://github.com/gsemet/Craftsman |
| computational sensors | deterministic tooling | misses semantic issues | — |
| inferential sensors | design/architecture debt | costly, non-deterministic | — |

### Quick wins
- Drop Karpathy rules into CLAUDE.md (5 min).
- Add `docs/progress.md` (current/completed/next); agent reads start, writes end (10 min).
- Write 3–5 self-contained `tasks-*.md` with acceptance criteria (15 min) → QRSPI/BMAD/Craftsman-ready.
- If running a custom harness: adopt hashline edits (~30 min, 5–10× fewer edit failures).

---

## 📈 Productivity & measurement

### What to implement (ranked)
1. **Middleware DORA platform** (Med) — open-source DORA collection (deploy freq, lead time, MTTR, CFR) from GitHub; dashboard. — [[GitHub - middlewarehqmiddleware ✨ Open-source DORA metrics platform for engineering teams ✨|middleware]] · https://github.com/middlewarehq/middleware
2. **Prompt Coach skill** (Low) — audits `~/.claude` JSONL: prompt quality, token spend by model, cache efficiency, productive hours. — [[Claude Code Prompt Coach Skill to analyse your AI-Assisted Coding Skills|Claude Code Prompt Coach Skill]] · https://github.com/hancengiz/claude-code-prompt-coach-skill
3. **Oobo — commits as decision ledger** (Low) — wraps git commit to capture sessions, tokens, AI-vs-human attribution, model. — [[Git for agents (and humans).|Git for agents (and humans)]] · https://oobo.ai
4. **OpenSync dashboards** (Med) — session activity/tool/token tracking for Claude/OpenCode; export sessions as eval datasets. — [[Dashboards for OpenCode and Claude coding sessions|Dashboards for OpenCode and Claude sessions]] · https://www.opensync.dev
5. *[[GitHub - mikaelvesavuorigithub-dora-metrics Instant, badge-ready DORA metrics for your GitHub repository. · GitHub|github-dora-metrics]]* (Low) — serverless, badge-ready DORA from GitHub deployments + labelled issues. — [[GitHub - mikaelvesavuorigithub-dora-metrics Instant, badge-ready DORA metrics for your GitHub repository. · GitHub|github-dora-metrics]] · https://github.com/mikaelvesavuori/github-dora-metrics
6. **Faros** (High) — links Claude Code adoption to DORA/SPACE, cost per PR; exposes the "AI productivity paradox" (throughput up, delivery flat). — [[How to measure Claude Code ROI Developer productivity insights with Faros|How to measure Claude Code ROI… with Faros]] · https://www.faros.ai

### Comparisons
| Option | Best for | Tradeoff | Link |
|---|---|---|---|
| Middleware | full-team DORA, integrations | Docker + 16GB RAM | https://github.com/middlewarehq/middleware |
| github-dora-metrics | lightweight badges, small repos | last 100 deploys only | https://github.com/mikaelvesavuori/github-dora-metrics |
| Faros | org ROI (DORA × spend) | enterprise integration | https://www.faros.ai |
| Prompt Coach | individual session efficiency | Claude Code only | https://github.com/hancengiz/claude-code-prompt-coach-skill |
| Oobo | git-native work ledger | local + orphan branch | https://oobo.ai |
| OpenSync | session search/export, evals | cloud or local Convex | https://www.opensync.dev |

### Quick wins
- Install Prompt Coach, ask "analyse my usage" → find Opus overspend + clarity gaps (30 s).
- Capture a DORA **baseline now** (github-dora-metrics/Middleware) before scaling AI — enables later A/B.
- `oobo commit` for a week → token cost per commit + AI/human attribution (30 min).

---

## 👤 Human, UX & frontend

### What to implement (ranked)
1. **Browser automation for E2E + UI debugging** (Med) — Playwright MCP / Chrome DevTools MCP / Claude-in-Chrome to drive flows & verify UI. — [[Automating e2e manual labor with Claude Code|Automating e2e manual labor]], [[Let Claude use your computer from the CLI|Let Claude use your computer]] · https://github.com/microsoft/playwright-mcp · https://github.com/ChromeDevTools/chrome-devtools-mcp
2. **Design skills following a real process** (High) — requirements→brief→IA→tokens→build→review, not "prompt and pray". — [[7 Claude Code Design Skills That Follow a Real Design Process|7 Claude Code Design Skills…]] · https://github.com/julianoczkowski/designer-skills
3. **visual-plan / visual-recap (MDX)** (Med) — interactive wireframes + API/schema diffs before code; visual PR recap. — [[Introducing visual-plan - rich plans for Claude Code + Codex|Introducing visual-plan]] · https://github.com/BuilderIO/visual-plan
4. **Natural-language E2E runner** (Med) — plain-English JSON tests; LLM-judge + page-content verify. — [[Automating e2e manual labor with Claude Code|Automating e2e manual labor]] · https://github.com/arielb135/claude-code-e2e-demo
5. **Design skills bundle (Anthropic + Vercel + Bencium)** (Low) — aesthetics, a11y, perf, composition. — [[Top 8 Claude Skills for UIUX Engineers|Top 8 Claude Skills for UI/UX Engineers]] · https://github.com/anthropics/skills · https://github.com/vercel-labs/agent-skills
6. **Live reasoning transparency (Ctrl+O)** (Low) — watch reads/tool calls to course-correct mid-flight. — [[Claude Code for Everything Keeping Up with the Claude Code Treadmill (30 Claude Code Tips & Tricks)|Claude Code for Everything (30 tips)]]

### Comparisons
| Option | Best for | Tradeoff | Repo |
|---|---|---|---|
| Playwright MCP | cross-browser, clean session | no login state | https://github.com/microsoft/playwright-mcp |
| Claude-in-Chrome | real UI w/ your login | shared cookies, your Chrome | — |
| Chrome DevTools MCP | perf/network inspect | read-only | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| Anthropic frontend-design | distinctive output | opinionated | https://github.com/anthropics/skills |
| Bencium UX skill | UX fundamentals | verbose (~28k chars) | — |
| Vercel web-design-guidelines | a11y/UX audit | quality-gate only | https://github.com/vercel-labs/agent-skills |
| visual-plan (MDX) | planning + PR review | author components | https://github.com/BuilderIO/visual-plan |

### Quick wins
- `claude mcp add playwright` + `chrome-devtools` → first E2E walkthrough in ~1 h.
- Toggle Ctrl+O while building UI (0 setup).
- Pair `/visual-plan` + `/visual-recap` on PRs so reviewers see intent + impl, not raw diffs (30 min).

---

## 🧩 Agents & models

### What to implement (ranked)
1. **LiteLLM provider-agnostic routing** (Low) — route per task, fallback chains, cost tracking; 30–50% savings. — [[OpenCode has been a gamechanger!|OpenCode has been a gamechanger!]], [[Deterministic vs. Non-Deterministic LLMs What's the Difference|Deterministic vs Non-Deterministic LLMs]] · https://github.com/BerriAI/litellm
2. **Multi-model orchestration** (Med) — cheap model plans, mid implements, strong validates; stack instances for parallel. — [[OpenCode has been a gamechanger!|OpenCode…]], [[Anthropic's Boris Cherny Why Coding Is Solved, and What Comes Next|Boris Cherny: Why Coding Is Solved]]
3. **Static↔dynamic prompt boundary** (Med) — split cached system prompt from per-task; reuse expensive tokens. — [[Diving into Claude Code's Source Code Leak|Diving into Claude Code's Source Code Leak]]
4. **Determinism toggle (temp 0 vs >0)** (Low) — temp=0 for extraction/factual, >0 for creative; per-task switch. — [[Deterministic vs. Non-Deterministic LLMs What's the Difference|Deterministic vs Non-Deterministic LLMs]]
5. **Research subagent for docs** (Low) — fetch `llms.txt` in a focused agent; keep main context clean. — [[Why You Don't Need the Nuxt MCP When You Use Claude Code|Why you don't need the Nuxt MCP]]

### Comparisons
| Layer | Option | Best for | Tradeoff |
|---|---|---|---|
| platform | Claude Code | quality + parallelism | proprietary harness |
| | Cursor | visual IDE editing | heavy VS Code fork |
| | OpenCode | budget, Chinese models | DIY multi-model |
| model | Opus | reasoning, orchestration | $$$ |
| | Sonnet | coding baseline | limited deep reasoning |
| | Haiku | fast workers | weaker edge cases |
| SDK | LiteLLM | unified API, fallback, CLI | proxy overhead |
| | Vercel AI SDK | React, streaming, types | React-only |

### Quick wins
- Stand up LiteLLM proxy; route cheap→plan, strong→hard bits (<4 h, ~30% savings).
- Split system prompt into cached static + dynamic; reuse across sessions.
- Add a `--deterministic` flag (temp=0) for extraction/factual tasks (30 min).

---

## 🏭 Industry & product
Mostly landscape/career, **little directly implementable**:
- **Particle** — reference for fast, source-transparent summary UIs over noisy feeds (study, don't build). — [[Best AI News Aggregators in 2026 7 Tools Compared|Best AI News Aggregators 2026]]
- [[15 steps to launch your own startup|15 Steps to Launch a Startup]], [[5 Things I Learned About Being a Technical Lead|5 Things… Technical Lead]], [[Microsoft accidentally told the truth about AI|Microsoft accidentally told the truth about AI]] — context, not actionable.

---

## Notes
- Repos/URLs are as cited in the source notes; verify before adopting (some are young projects).
- Mark a note `action: implement` once you commit to building it — the 🔨 view in [[Agentic Engineering]] tracks them.
- See [[Agentic Engineering — Trends 2026]] for where each theme is heading.
