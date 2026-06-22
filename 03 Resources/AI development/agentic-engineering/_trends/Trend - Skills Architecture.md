---
title: "Trend: Skills Architecture"
category: trend-synthesis
created: 2026-06-14
tags:
  - agentic-engineering
  - skills-architecture
  - trend
---

# Skills Architecture

## Core Insight

Skills are **portable expertise units** that load context on demand — not persistent agents, not generic prompts. The SKILL.md standard encodes what to do, when to invoke, and how much context to spend. The folder structure IS the orchestration logic; the agent reads the directory and routes itself.

## Why It's Emerging Now

As agent usage scales, teams discovered two failure modes: (1) monolithic prompts that try to encode all behavior and become unmaintainable, (2) subagent-per-task patterns that burn tokens and latency on context switches for work that doesn't need isolation. Skills occupy the middle ground — modular context injection without spawning new processes.

## Key Mental Models

- **Skills vs. Subagents**: Skills inject context into the current agent; subagents spawn isolated workers with separate context windows. Skills are cheaper (no fork overhead) and better for expertise that the current agent needs to apply directly. Subagents are better for parallel independent work or work requiring total isolation (e.g., destructive file ops).
- **Folder-as-Router**: The agent reads a skills directory, finds the matching SKILL.md for the current task, and loads it. No orchestration code needed — the filesystem structure encodes the routing logic.
- **Progressive Context Disclosure (3-Tier)**: Tier 1 (~200 tokens): always-loaded skill overview and invocation trigger. Tier 2 (~500 tokens): task-triggered pattern library, examples, common cases. Tier 3 (~2000 tokens): full implementation detail, edge cases, on-demand only. Total context budget ~2% of window.
- **Skill Retirement Signal**: When evals show a skill is no longer improving outcomes (or the base model has internalized the behavior), retire the skill. Skills are temporary scaffolding, not permanent infrastructure.

## Specific Techniques & Implementations

- **SKILL.md Standard**: A markdown file per skill containing: description (for agent matching), when-to-use criteria, context tiers (T1/T2/T3), examples, and anti-patterns. The format is consumed by Claude Code's `/skills` command.
- **Plugin Architecture**: The agents marketplace (`~/.agents/plugins/`) extends skills to multi-harness portability. A skill written for Claude Code can be adapted to Codex CLI, Cursor, Gemini CLI via the same SKILL.md format.
- **`/skills` slash command**: Loads available skills from the skills directory, letting the agent self-discover capabilities. The agent reads skill descriptions to decide which to invoke.
- **Skills for E2E Testing**: A dedicated SKILL.md for e2e testing patterns that activates when the agent is writing integration/browser tests. Encodes playwright patterns, viewport setup, network mocking idioms.
- **Skills for Error Handling**: Encodes the project's error handling conventions (custom error classes, boundary patterns, retry logic) so the agent applies them consistently without reading the entire codebase.
- **Harness-level skill injection**: CLAUDE.md can reference skills by path; the harness pre-loads them at session start for always-needed expertise.

## Key Tensions / Debates

- **Skills vs. RAG**: Skills are hand-curated, statically versioned, and always relevant when triggered. RAG is dynamic but retrieves noise alongside signal. For codified team conventions, skills win. For large knowledge bases, RAG scales better.
- **How many skills is too many**: Large skills directories slow agent initialization and increase context overhead at the directory-reading phase. Recommended: prune to ≤20 active skills, archive the rest.
- **Skills vs. just-good prompts**: A senior developer asking "when does a skill become worth the SKILL.md overhead?" — the break-even is roughly 3+ repeated uses of the same expertise pattern.

## Surprising / Non-Obvious Findings

- The folder structure itself carries routing logic — teams spending effort on orchestration code can often replace it with a well-organized skills directory that the agent navigates autonomously.
- The 3-tier loading structure means ~98% of skill content is never loaded for most tasks — the overhead of maintaining a rich SKILL.md is near-zero at runtime.
- Skills can encode "anti-patterns" explicitly (what NOT to do), which is more effective than positive instructions alone for preventing recurring mistakes.
- The retirement signal (evals-based) ensures skills don't accumulate indefinitely — the discipline of retiring skills is as important as creating them.

## Key Quotes

> "The folder structure is the orchestration. If you're writing orchestration code, your folder structure is wrong."

> "Skills = portable expertise. Subagents = isolated workers. Don't confuse the two."

> "A skill you can't explain in 200 tokens isn't a skill — it's a hidden workflow."

## Connected Themes

- [[Trend - Harness Engineering]] — SKILL.md is a feedforward control in the harness
- [[Trend - Context Engineering]] — progressive disclosure directly manages context budget
- [[Trend - Workflow Evolution (QRSPI)]] — skills encode workflow phases
- [[Trend - Multi-Agent Architecture & Orchestration]] — skills vs. subagents boundary
