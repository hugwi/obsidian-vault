---
created: 2026-09-08
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - agentic-engineering
  - harness-loops
  - skill-tool-extension
  - observability-traces
---

# Agentic Engineering — Current Setup

What is **actually running** on my machines today, as a baseline to compare the vault's
theory against. The sister notes say what exists ([[Agentic Engineering]]), what's worth
building ([[Agentic Engineering — Implementation Guide]]), and what's trending
([[Agentic Engineering — Trends 2026]]). This one says what I already have.

> Two boxes: a primary GPU workstation and a secondary (frequently offline). Everything is
> reachable over Tailscale via `tailscale serve`, tailnet-only — never funnel.

## Harnesses in use

| Harness | Config | Model | Notes |
|---|---|---|---|
| Claude Code | `~/.claude/settings.json` | Opus 5 / Sonnet; subagents pinned to Sonnet | Primary driver |
| OpenCode | `~/.config/opencode/opencode.json` → `~/.agents/opencode/` | local `llama-swap/qwen-3.8-27b` | Auto-compaction on, prune, 10k reserved |
| Codex | `~/.codex/config.toml` | `gpt-5.5`, reasoning effort low | `sandbox_mode = workspace-write`, `auto_review` |
| Cursor | `~/.cursor/` | — | Shares the same skills directory |
| Hermes | `~/.hermes-coder`, `~/.hermes-researcher` | — | Research/coding split |
| Happier | `/tmp/opencode/happier` | — | Mobile/web client for Claude Code, Codex, OpenCode |

## Single source of truth: `~/.agents`

One git repo holds skills, rules, subagents, slash commands, and plugin manifests; each
harness gets a symlink instead of its own copy.

- `~/.claude/skills` and `~/.cursor/skills` → `~/.agents/skills` (~131 skills)
- `~/.agents/agents` (9) plus `~/.claude/agents` (15 subagents), 40 slash commands
- `scripts/setup-links.sh` rebuilds every symlink on a new machine
- `sync-agents-to-harnesses.py` runs on **SessionStart** (`--quiet --prune`) so a skill
  edit propagates to all harnesses without manual copying
- `SKILL_INDEX.md` is a routing table: request → capability, so discovery doesn't depend
  on the model guessing skill names

This is the concrete answer to *skill-tool-extension* + *environment-isolation*: extension
lives in one versioned place, harnesses are disposable clients of it.

## Claude Code specifics

- **Plugins**: `superpowers`, `ralph-loop`, `code-review`, `code-simplifier`,
  `frontend-design`, `context7`, `chrome-devtools-mcp`, `pyright-lsp`, `prisma`, `caveman`
- **Hooks**
  - `PreToolUse(Bash)` → `rtk hook claude` — rewrites commands through RTK, a token-killing
    CLI proxy (60–90% saving on dev output); `rtk gain` reports the savings
  - `PreToolUse(Read)` → `read-guard.py`
  - `block-tailscale-funnel.sh` — refuses to expose anything publicly
  - `token-baseline.py` — token accounting
- **Permissions**: broad allow-list, `defaultMode: acceptEdits`, sandbox on with
  `autoAllowBashIfSandboxed`; deny covers `.env`, `secrets/**`, `rm -rf`, `wget`
- **`AskUserQuestion` is denied** on purpose — multiple-choice pickers get blocked, so the
  agent asks in plain prose and I type a free-form answer. Cheap fix, big UX difference.
- Editor mode `vim`, `verbose: true`, thinking enabled, statusline from the caveman plugin

## Context engineering in practice

- RTK on every Bash call — the biggest single token lever, applied at the harness layer
  rather than by asking the model to be brief
- OpenCode auto-compaction + prune
- `CLAUDE.md` / `AGENTS.md` as durable rules; `AGENTS.full.md` (26k) holds the long form,
  the short file stays loaded
- Auto-memory disabled (`CLAUDE_CODE_DISABLE_AUTO_MEMORY=1`) — memory is curated by hand

## Observability — the part most setups skip

Full OTLP pipeline for agent sessions, all Docker with persistent volumes and
`restart: unless-stopped`:

```
OpenCode CLI ──OTLP :5318──▶ otel-collector ──scrape──▶ Prometheus (30d)
                                                          ├─▶ Grafana (dashboards only)
                                                          └─▶ Alertmanager ──▶ Discord
```

- 19 `opencode_*` metric families: cost, tokens, tool duration, cache, sessions, model usage
- Dashboards: `opencode.json` (subscription quota, freshness, cost/token rollups),
  `vocis-voice-worker.json`
- **Alerting lives in Prometheus + Alertmanager, not Grafana** — rule files hot-reload with
  no downtime and no missed evaluations; Grafana owns zero alerts
- Discord webhook stored as a `0600` file read via `webhook_url_file`, so it never reaches
  config, env, or `docker inspect`
- Everything behind an nginx gateway on the tailnet host root

This covers *observability-traces* and *cost-optimization* concretely: per-session cost and
token counts are queryable, not guessed.

## Loops and workflow phases

- `ralph-loop` plugin + a `/loop` dynamic-pacing mode for self-paced iteration
- `superpowers` supplies the process spine: brainstorming → writing-plans → TDD →
  requesting-code-review → verification-before-completion
- Quality gates as commands: `/cleanup`, `/verify`, `/code-review`, `security-review`,
  `test-coverage`, plus a `cleanup-specialist` agent scoped to branch-changed files only
- Human-in-the-loop is deliberately *textual* (see the `AskUserQuestion` deny above)

## Gaps vs. the Implementation Guide

- No eval harness yet — nothing measuring whether a prompt/skill change helped
- No DORA-style delivery instrumentation; telemetry covers cost and tokens, not lead time
- Skill sprawl: ~131 skills, routing leans on `SKILL_INDEX.md` rather than retrieval
- Secrets hygiene is uneven — some harness configs still hold bearer tokens inline, while the
  Discord webhook is properly file-scoped. Worth normalising on file-scoped secrets.

---

## Related
- [[Agentic Engineering]] — theme hub
- [[Agentic Engineering — Implementation Guide]] — what to build next, ranked
- [[Agentic Engineering — Trends 2026]] — current landscape
- [[agentic-systems-architecture]]
