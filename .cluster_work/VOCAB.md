# Tag vocabulary for Readwise articles

Assign every tag that genuinely applies (multi-label). Most articles get 1–4 tags.
Prefer SPECIFIC cross-cutting tags (cost-optimization, token-efficiency, dora-metrics,
code-quality, web-security) IN ADDITION to the broad domain tag when the article is
really about that angle. Example: a "DORA metrics platform" → `dora-metrics observability`;
a "coding agent that cuts API cost 80% with better quality" → `alt-agents cost-optimization code-quality`.

Only use tags from this list. If an article is a login wall / error page / empty stub, tag it `non-content`.

## Agentic engineering
- harness-engineering — the loop/scaffolding/infra that makes an autonomous agent reliable & controllable
- context-engineering — managing the LLM context window, compaction, what tokens to include
- claude-md — writing/structuring CLAUDE.md / AGENTS.md instruction files
- token-efficiency — reducing token consumption / smaller context / token-efficient pipelines
- cost-optimization — reducing AI/API $ cost, cheaper inference, lowering tool spend
- code-intelligence — codebase indexing, semantic code retrieval, code knowledge graphs
- agent-memory — persistent memory across sessions for coding agents
- agent-skills — reusable agent skills/plugins, skill libraries & packages
- spec-driven-dev — PRD/spec-first workflows, AIDLC, BMAD, QRSPI, spec-kit, Kiro
- multi-agent — multiple agents / sub-agents collaborating, orchestration
- alt-agents — coding agents/IDEs: Pi, OpenClaw, OpenCode, Codex, Cursor, Copilot, Claude Code as a product
- claude-code-ops — operating Claude Code: sessions, permissions, slash commands, remote, CLI, daily workflow
- agent-git — worktrees, parallel branches, stacked PRs, devcontainers for agents
- agent-testing — automated E2E/Playwright testing, generating test coverage with agents
- evals — evaluating LLMs and agent skills, eval frameworks, benchmarks
- code-quality — readability, linters-as-guardrails, preventing bad/unreadable AI code
- code-review — AI code review, review loops, review checklists
- dora-metrics — DORA / delivery performance / developer-productivity metrics & dashboards, code-drift metrics
- observability — dashboards, monitoring, auditability of agent/coding sessions
- comprehension-debt — human attention bottleneck, understanding AI code, technical debt of agentic coding
- mcp — Model Context Protocol, MCP servers, tool integration
- browser-automation — browser/computer use for agents, Chrome DevTools, web UI automation
- voice-ai — voice agents, speech-to-speech, voice coding assistants
- media-generation — generating videos/slides/presentations with AI (Remotion etc.)
- local-llm — running local LLMs, GPUs/VRAM/Ollama/quantization, self-hosting, hardware
- llm-fundamentals — LLM overviews, deterministic vs non-deterministic, model capabilities

## Software craft & adjacent
- web-security — sanitizing input, injection, prompt/MCP security
- frontend-webapp — frontend, native-feel web apps, PWA, performance, streaming
- ux-ui-design — UI/UX design, interfaces, buttons, design systems & design skills
- ddd — domain-driven design, bounded contexts, ubiquitous language
- clean-architecture — clean/hexagonal architecture, layering, dependency rules
- software-patterns — design patterns, coupling, refactoring, code katas, TDD

## Data
- data-engineering — data mesh, dbt, change data capture, event sourcing
- mdm-governance — master data management, data governance, data democratization

## Business / product
- startup — founders, pitch decks, fundraising, YC, equity, moats
- product-management — customer interviews, user stories, epics, agile estimation, requirements
- ai-industry — AI bubble/economics/hype, executive strategy, opinion

## Personal / PKM
- pkm-obsidian — personal knowledge management, Obsidian, second brain
- productivity — task management, inbox zero, personal systems
- health — arthritis, joints, medicine, climbing injuries
- real-estate — selling a home, brokers, mäklare
- non-content — login wall, error page, empty/placeholder fragment
