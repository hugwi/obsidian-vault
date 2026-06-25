---
categories:
  - "[[Resources]]"
domain: engineering
tags: [ai-development, claude-code, observability, rules, skills]
created: 2026-05-19
topic: Context Provenance
---

# Context Provenance — seeing which rules/skills/agents/AGENTS.md actually applied

**Term:** *Context Provenance* — tracking which rule files, skill definitions, agent personas, and `AGENTS.md` / `CLAUDE.md` directives shaped a given assistant turn. The "where did this behavior come from?" question. Related but distinct from **Observability** (system telemetry) and **Traceability** (cause → effect chain).

## Core insight

Rules in Claude Code do **not** fire events. They are not triggered, matched, or activated per turn. They are **static text injected at session start** as `<system-reminder>` blocks alongside the system prompt. Every turn carries every loaded rule in its context window.

Skills behave differently — they are dynamically invoked via the `Skill` tool, so each skill use IS an event you can observe.

Agents (subagents) are also dynamic — each `Agent` tool call is an observable event with inputs/outputs.

| Artifact | Loaded how | Per-turn event? | How to audit |
|---|---|---|---|
| `CLAUDE.md` / `AGENTS.md` (project) | Auto-injected as system prompt | No — always present | Read transcript |
| `~/.claude/CLAUDE.md` (global) | Auto-injected as system prompt | No — always present | Read transcript |
| `.agents/rules/*.md` | Auto-injected as system prompt | No — always present | Read transcript |
| `.cursor/rules/*.mdc` | Auto-applied by Cursor harness | No — always present in Cursor | Read transcript |
| Skills (`SKILL.md`) | Loaded on `Skill` tool invocation | **Yes** — discrete event | Telemetry / transcript |
| Subagents | Loaded on `Agent` tool invocation | **Yes** — discrete event | Telemetry / transcript |
| Hooks | Fire on harness events (UserPromptSubmit, etc.) | **Yes** — discrete event | Hook logs / transcript |

## So "applied" = "present in context" for rules

Cannot ask "did the no-eslint-disable rule fire?". Can only ask "was it loaded into context this session?" — answer is almost always yes.

What you CAN observe:
- **Was a skill invoked?** Yes — `Skill` tool calls in transcript.
- **Was a subagent spawned?** Yes — `Agent` tool calls in transcript.
- **Did a hook run?** Yes — hook output in transcript.
- **Did the model's output comply with a rule?** Only via review/lint/test — the rule itself doesn't signal.

## Ways to inspect Context Provenance

### 1. Session transcripts (most direct)

Every turn's full context lives in JSONL files:

```
~/.claude/projects/<project-hash-slug>/*.jsonl
```

Each line is one message including system reminders. Grep for rule filename, skill name, or agent name:

```bash
grep -l "no-eslint-disable" ~/.claude/projects/*/*.jsonl
grep -c "Skill tool" ~/.claude/projects/<hash>/<session>.jsonl
```

### 2. OpenTelemetry pipeline (Mindator's setup)

Local OpenObserve at <http://localhost:5080> ingests:
- Traces (with `CLAUDE_CODE_ENHANCED_TELEMETRY_BETA=1`)
- Metrics
- Logs/events (incl. unredacted prompts via `OTEL_LOG_USER_PROMPTS=1`)
- Tool detail + content (`OTEL_LOG_TOOL_DETAILS=1`, `OTEL_LOG_TOOL_CONTENT=1`)
- Raw API request/response bodies dumped to `~/.claude/telemetry/api-bodies/<uuid>.{request,response}.json`

CLI aggregator:

```bash
claude-usage [hours]
```

Filter OpenObserve stream by `service.name=claude-code`, search for skill names or rule text.

### 3. `/context` slash command

Shows what is currently loaded in the context window — including system prompt blocks, rules, recent messages. Closest to a real-time "what's active" view.

### 4. Verbose mode

```bash
claude --verbose
```

Or toggle in-session with **Ctrl+O**. Shows extended thinking + context flow.

### 5. Custom audit hook (proactive)

To get a true "which rules loaded this turn" log, add a `UserPromptSubmit` hook in `~/.claude/settings.json`:

```jsonc
{
  "hooks": {
    "UserPromptSubmit": [
      { "type": "shell", "command": "ls ~/.agents/rules/ > /tmp/rules-loaded-$(date +%s).log" }
    ]
  }
}
```

The harness — not the model — runs hooks, so they fire deterministically per event.

## Why this matters

Once your stack has 40+ rule files, 80+ skills, and a dozen subagents, behavior becomes emergent. When the assistant does something surprising — good or bad — you want to answer:

> "Was that because of `no-eslint-disable.md`? Or because the `tdd-workflow` skill self-invoked? Or because `code-reviewer` agent recommended it?"

That's the Context Provenance question. The infrastructure for answering it: transcripts + telemetry + hooks.

## The word

**Context Provenance** — concise, technically accurate, borrowed from data lineage. Alternatives:

- *Rule Lineage* — narrower, only rules
- *Observability* — too broad, conflates with metrics/traces
- *Introspection* — runtime self-examination, loose fit
- *Traceability* — cause-effect chain, useful but reactive

Use **Context Provenance** as the umbrella term, **Observability** for the telemetry that enables it.

## Related

- [[CLAUDE.md]] — global directives loaded every session
- `~/.agents/rules/` — single source of truth for shared rules
- OpenObserve dashboard (local): <http://localhost:5080>
