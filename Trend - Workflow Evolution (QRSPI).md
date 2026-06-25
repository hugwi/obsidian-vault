---
categories:
  - "[[Resources]]"
domain: engineering
title: "Trend: Workflow Evolution (QRSPI)"
category: trend-synthesis
created: 2026-06-14
tags:
  - agentic-engineering
  - workflow
  - qrspi
  - trend
---

# Workflow Evolution — From RPI to QRSPI

## Core Insight

The standard "Research → Plan → Implement" (RPI) workflow is a local maximum. Its own creator publicly reversed his recommendation. The emerging standard is **QRSPI** — an 8-phase workflow that front-loads clarification, adds explicit research and security checkpoints, and separates commit discipline from implementation. The key insight: most agent failures happen not in implementation but in premature implementation.

## Why It's Emerging Now

RPI was good enough when agents were used for single-session, single-file tasks. As agents take on multi-day, multi-file work — and as the cost of context-window thrashing became measurable — the community recognized that front-loading disambiguation and context-loading pays for itself many times over. QRSPI emerged from practitioner synthesis across multiple agent-heavy teams.

## Key Mental Models

- **Phase separation prevents premature implementation**: Starting to code before clarifying ambiguities is the #1 cause of agent rework. Every phase in QRSPI has an explicit "gate" — proceed only when the output of that phase is verified.
- **Instruction budget (~150–200 max)**: The agent's ability to follow instructions degrades after roughly 150–200 distinct rules. Beyond this, instructions are silently dropped or mixed up. QRSPI instructs practitioners to audit and compress their instruction sets.
- **Dumb Zone above 40%**: Context utilization above ~40% correlates with instruction-following degradation. QRSPI phases are designed to complete before context fills — with explicit compaction gates between phases.
- **Session = Throwaway Unit**: Each QRSPI session is bounded. A session is not a project — it's a unit of context. When a session ends, handoff artifacts (state file, decision log) preserve continuity without relying on conversation history.

## The 8 QRSPI Phases

1. **Query/Clarify** — Resolve all ambiguities before touching code. Output: written acceptance criteria.
2. **Research** — Search existing codebase, docs, and external sources. Output: research notes, relevant file list.
3. **Strategize** — Choose implementation approach, identify risks. Output: strategy doc with explicit tradeoffs.
4. **Plan** — Break strategy into atomic steps. Output: numbered task list with verifiable checkpoints.
5. **Implement** — Execute against plan, one step at a time. Gate: each step verifies before proceeding.
6. **Security Review** — Explicit security pass (OWASP top 10, input validation, auth boundaries). Not optional.
7. **Test** — TDD retroactively if needed; verify coverage against acceptance criteria.
8. **Commit** — Atomic commits, conventional format, no "cleanup commits" mixing unrelated changes.

## Specific Techniques & Implementations

- **Acceptance Criteria as Gate**: QRSPI's Q phase produces written acceptance criteria. If the agent can't write them, the task isn't well-defined enough to implement.
- **Research-First Norm**: Check npm/PyPI/crates.io before writing utility code. Search GitHub code before writing new patterns. Prefer adapting proven implementations over net-new.
- **Strategy Doc**: A 1-page markdown capturing: chosen approach, rejected alternatives with reasons, identified risks. Lives in the session handoff file.
- **Compaction Between Phases**: Explicitly compact context at phase boundaries (especially R→S and S→P transitions) to enter each phase with a clean window.
- **Security as Non-Optional Phase**: Adding a dedicated security phase prevented teams from treating it as optional. The placement (after implementation, before test) lets it catch implementation-specific issues.
- **CRISPY**: An open-source implementation of QRSPI-like workflow as a Claude Code skill set.

## Key Tensions / Debates

- **QRSPI overhead on small tasks**: For a 10-line bugfix, running 8 phases is absurd. The community convention: apply full QRSPI for tasks estimated at >2 hours or >3 files. Use abbreviated RPI or direct implementation for smaller tasks.
- **RPI creator's reversal**: The public acknowledgment that "RPI is a local maximum" was controversial — many practitioners have RPI deeply embedded in their CLAUDE.md. The transition to QRSPI requires updating harness config, not just workflow intent.
- **Phase purity vs. pragmatism**: In practice, phases blur. A strict QRSPI practitioner compacts between each phase; a pragmatic one compacts only at the R→P boundary.

## Surprising / Non-Obvious Findings

- The creator of RPI publicly reversed his recommendation — a rare instance of a practitioner openly admitting their own framework was suboptimal.
- The silent instruction-drop threshold (~150–200 rules) means practitioners with exhaustive CLAUDE.md files may be getting worse agent behavior than those with minimal, curated ones.
- The "dumb zone" starting at 40% context is earlier than most practitioners realize — many assume degradation only happens near 90%+.
- Security phase placement (post-implementation, not post-plan) is counterintuitive but more effective — it catches real implementation issues rather than theoretical risks.

## Key Quotes

> "RPI is a local maximum. I should know — I invented it." — RPI creator

> "If you can't write acceptance criteria, you can't implement it. Full stop."

> "150 instructions. After that, the agent stops listening."

> "QRSPI isn't a workflow, it's a context management strategy that happens to produce code."

## Connected Themes

- [[Trend - Context Engineering]] — QRSPI phases are designed around context budget
- [[Trend - Skills Architecture]] — QRSPI phases can be encoded as skills
- [[Trend - Human Oversight & Comprehension Debt]] — each phase gate is an oversight checkpoint
- [[Trend - Cost Optimization & Token Economics]] — compaction between phases reduces cost
