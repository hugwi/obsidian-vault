---
categories:
  - "[[Resources]]"
domain: engineering
title: "Trend: Harness Engineering"
category: trend-synthesis
created: 2026-06-14
tags:
  - agentic-engineering
  - harness-engineering
  - trend
---

# Harness Engineering

## Core Insight

The agent is not the model — it is **model + harness**. Same model, ranked #33 on one benchmark harness and #5 on another. A single change to the edit tool (switching to a hashline-based diff format) improved 15 LLMs simultaneously. The model is the raw ingredient; the harness determines what gets cooked.

## Why It's Emerging Now

LLMs have plateaued enough that configuration arbitrage has become more valuable than model-switching. Organizations are realizing that prompt engineering at the turn level is a local maximum — the leverage is in the structural scaffolding around the model, not in individual prompt tweaks. The term "harness engineering" emerged from OpenAI's Codex team and has rapidly diffused through the practitioner community.

## Key Mental Models

- **Agent = Model × Harness**: Output quality is multiplicative, not additive. A weak harness caps even a strong model.
- **Ratchet Pattern**: Progress is locked in at checkpoints so a failing step doesn't erase prior work. The harness enforces monotonic forward movement.
- **Feedforward vs. Feedback Controls**: Feedforward = pre-loaded context (CLAUDE.md, SKILL.md, examples). Feedback = runtime correction loops (test runners, linters, validators that return structured signals).
- **Computational vs. Inferential Controls**: Computational = deterministic guards (regex, type checks, linters — cheap and reliable). Inferential = LLM-based checks (flexible but expensive and probabilistic). Good harnesses lean computational where possible.

## Specific Techniques & Implementations

- **Hashline Edit Tool**: Replace line-number-based diffs with hashline anchors. The model specifies context lines above/below the change, not absolute positions. Works across edits that shift line numbers. This single change was enough to lift 15 model rankings.
- **CLAUDE.md as Feedforward**: The file is loaded on every turn — treat it as persistent system prompt injection. Cost is per-turn, not per-session. Every instruction in it burns tokens every message.
- **Instruction Budget**: ~150–200 max instructions before silent degradation. Models don't error on overflow — they silently stop following rules. Fewer, more precise instructions outperform exhaustive rule lists.
- **Hooks as Physics, Instructions as Advisory**: Instructions can be ignored. Shell hooks that run before/after tool calls cannot be overridden by the model. Hook-enforced constraints are deterministic; instruction-based ones are probabilistic.
- **OpenHarness/AutoHarness**: Open-source harness frameworks have emerged. OpenHarness (HKUDS) is "ultra-lightweight" targeting Claude Code specifically.

## Key Tensions / Debates

- **Harness complexity vs. maintainability**: Elaborate harnesses become their own engineering burden. Teams underestimate maintenance cost of custom scaffolding.
- **Harness portability**: A harness tuned for one model degrades on another. As base models update, harnesses may silently break.
- **When to use subagents vs. harness controls**: Subagents add isolation but cost latency and context switches. Many use cases are better served by harness-level feedback loops.

## Surprising / Non-Obvious Findings

- The same model can rank #33 and #5 depending purely on the evaluation harness — not the model's actual capability.
- Changing only the edit tool (not the prompt, not the model) was sufficient to improve all 15 evaluated LLMs simultaneously.
- "Pi" (a minimal harness) beat Claude Code and OpenCode for one user specifically because predictability > capability for daily workflow.
- Harness failures in cloud-native systems happen because feedback loops require filesystem/process state that containers don't reliably provide.

## Key Quotes

> "I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed." — @_can1357

> "Same model. Same benchmark. 6× the performance difference." — Rethinking AI Agents post

> "Agent = Model + Harness. Most people only optimize half the equation."

## Connected Themes

- [[Trend - Context Engineering]] — harness controls what enters context
- [[Trend - Skills Architecture]] — SKILL.md is a harness-level feedforward control
- [[Trend - Cost Optimization & Token Economics]] — harness choices dominate cost
- [[Trend - Human Oversight & Comprehension Debt]] — hooks enforce oversight without relying on model compliance
