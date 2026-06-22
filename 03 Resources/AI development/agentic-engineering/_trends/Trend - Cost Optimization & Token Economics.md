---
title: "Trend: Cost Optimization & Token Economics"
category: trend-synthesis
created: 2026-06-14
tags:
  - agentic-engineering
  - cost-optimization
  - token-economics
  - trend
---

# Cost Optimization & Token Economics

## Core Insight

At scale, agent cost is dominated by three things: context window utilization, vision API calls, and uncontrolled tool loops. The 5-layer defense stack (harness → hooks → compact → model selection → retrieval) reduces cost by 60–80% without reducing output quality — often improving it, because leaner context means less noise.

## Why It's Emerging Now

Early agent adopters ignored cost because usage was low. As organizations scale to hundreds of daily agent sessions, token costs compound fast. A single unconstrained agent session can consume $5–20 in API calls. At 200 sessions/day, that's $1–4k/day. The economics demand a principled approach.

## Key Mental Models

- **Instructions are advisory; hooks are physics**: A model can ignore an instruction to stop after N tool calls. A shell hook that kills the process after N calls cannot be ignored. Cost control belongs in hooks, not prompts.
- **CLAUDE.md as per-turn cost**: Every word in CLAUDE.md costs tokens on every single turn. A 1,000-token CLAUDE.md × 50 turns = 50,000 tokens of overhead per session. Audit ruthlessly.
- **Vision agents are 45x more expensive**: Using vision APIs (screenshot analysis, image description) costs roughly 45x more per call than structured text APIs for equivalent information. If the data can be extracted as text (DOM, JSON, structured output), never use vision.
- **Model selection as cost lever**: Haiku 4.5 = ~90% of Sonnet capability at ~33% of the cost. For high-frequency lightweight tasks (code completion, simple generation, worker agents in multi-agent systems), Haiku is the default choice. Sonnet for orchestration and complex reasoning. Opus only for maximum reasoning tasks.

## The 5-Layer Defense Stack

1. **Harness layer**: Hook-enforced turn limits, tool call rate limiting, automatic session termination on cost threshold breach.
2. **Context layer**: Intentional compaction at phase boundaries, progressive disclosure, backpressure wrappers on large tool outputs.
3. **Model selection layer**: Route tasks to the cheapest model capable of the job. Use model selection as a per-task decision, not a session-level one.
4. **Retrieval layer**: Fetch only what's needed when it's needed. Avoid front-loading entire codebases. Iterative retrieval > upfront context dump.
5. **Audit layer**: Log token usage per session with task labels. Identify which task types are expensive outliers. Iterate on harness config based on empirical data.

## Specific Techniques & Implementations

- **TOON Serialization**: "Text Object Outline Notation" — a compact intermediate format for serializing agent state and tool outputs that reduces token overhead vs. raw JSON or markdown.
- **Haiku for Worker Agents**: In multi-agent pipelines, use Haiku for leaf-node workers (code generation, simple edits, classification) and Sonnet for the orchestrator. Cost reduction: 3–5x on the worker portion of the bill.
- **Cache-Aware Scheduling**: Anthropic's prompt cache has a 5-minute TTL. Sessions that take frequent short breaks (under 5 minutes) stay cached; sessions that pause >5 minutes pay full cache-miss costs on resume. Scheduling iterations to stay within the 5-minute TTL is a real optimization.
- **Turn Limit Hooks**: Shell hook that counts tool calls and terminates or pauses the session after N calls. Forces intentional checkpointing that also serves as cost control.
- **Structured Output over Vision**: Replace screenshot analysis with DOM extraction. Replace image description with JSON API calls. The 45x cost difference justifies significant engineering investment in structured alternatives.
- **Session Cost Dashboard**: Track cost per session, per task type, per model. Identify the P90 expensive sessions and audit what caused them.

## Key Tensions / Debates

- **Quality vs. cost for orchestrators**: Using Haiku as the orchestrator saves money but risks coordination errors that require expensive rework. Sonnet or Opus for orchestrators, Haiku for workers, is the emerging consensus.
- **Compaction frequency vs. context coherence**: Compacting more often reduces context costs but risks losing coherence across phases. The optimal compaction frequency is task-dependent.
- **Caching vs. freshness**: Aggressive caching reduces cost but risks serving stale context. For rapidly-changing codebases, cache TTL needs to be calibrated to commit frequency.

## Surprising / Non-Obvious Findings

- Vision agents being 45x more expensive is widely unknown. Many teams use screenshots for "convenience" with no awareness of the cost differential.
- CLAUDE.md per-turn cost means a well-intentioned CLAUDE.md expansion (adding more rules for better behavior) can increase session costs by 20–30% with no visible quality benefit.
- The cache TTL cliff at 5 minutes means agents that pause to "think" or wait for user input between turns are paying full cache-miss costs on every resume.
- Hooks-as-physics is a mental model shift — most practitioners think of cost control as a prompt engineering problem when it's actually a harness engineering problem.

## Key Quotes

> "Instructions are advisory. Hooks are physics. Cost control belongs in hooks."

> "Vision agents cost 45x more than structured APIs. If the data can be text, make it text."

> "Your CLAUDE.md is billed on every turn. 500 words × 100 turns = $$$."

> "We cut agent costs 70% without touching the model. We touched the harness."

## Connected Themes

- [[Trend - Harness Engineering]] — cost control is a harness-layer responsibility
- [[Trend - Context Engineering]] — context size is the primary per-turn cost driver
- [[Trend - Multi-Agent Architecture & Orchestration]] — model selection per agent role
- [[Trend - Skills Architecture]] — progressive disclosure reduces context overhead
