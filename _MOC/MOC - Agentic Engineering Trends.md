---
title: "MOC: Agentic Engineering Trends"
category: moc
created: 2026-06-14
tags:
  - moc
  - agentic-engineering
  - trends
---

# Agentic Engineering — Trend Synthesis

> Synthesized from ~275 articles categorized June 2026. Each trend note is a cross-article synthesis of emerging patterns, mental models, and techniques.

## The Central Equation

**Agent = Model × Harness**

Same model, 6× performance difference based purely on configuration. The leverage in agentic engineering is not in the model — it's in everything built around it: context management, workflow design, memory systems, oversight mechanisms, and protocol integrations.

---

## Trend Notes

### Foundation Layer

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Harness Engineering|Trend: Harness Engineering]]
  — Model + harness. Same LLM, #33 vs. #5 ranking. Changing one tool improved 15 models simultaneously.

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Context Engineering|Trend: Context Engineering]]
  — 40–60% context is the smart zone. U-curve attention. Intentional compaction beats automatic. Dumb zone above 40%.

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Skills Architecture|Trend: Skills Architecture]]
  — SKILL.md standard. Progressive 3-tier disclosure. Folder-as-router. Skills ≠ subagents.

### Workflow & Process Layer

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Workflow Evolution (QRSPI)|Trend: Workflow Evolution — QRSPI]]
  — RPI creator reversed his own advice. QRSPI 8-phase workflow. 150-instruction budget. Session = throwaway unit.

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Cost Optimization & Token Economics|Trend: Cost Optimization & Token Economics]]
  — 5-layer defense stack. Hooks are physics; instructions are advisory. Vision agents 45× more expensive.

### Infrastructure Layer

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Agent Memory & Persistence|Trend: Agent Memory & Persistence]]
  — State-in-file. Beads (JSONL-in-git). Near-limit agents lie. Deliberate session splits beat compaction.

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Multi-Agent Architecture & Orchestration|Trend: Multi-Agent Architecture & Orchestration]]
  — Parallelism is a local maximum. Adversarial validators. Thread taxonomy P/B/L/Z/F. Factory Missions (16-day sprint).

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - MCP Ecosystem & Protocol Layer|Trend: MCP Ecosystem & Protocol Layer]]
  — 110M monthly downloads. 82% path traversal vulnerabilities. More capable models = more vulnerable. WebMCP.

### Governance Layer

- [[03 Resources/AI development/agentic-engineering/_trends/Trend - Human Oversight & Comprehension Debt|Trend: Human Oversight & Comprehension Debt]]
  — Comprehension debt scoring 1–5. AI reviewing AI = mirror. Confused deputy problem. 7 agentic debt blocks.

---

## Cross-Theme Map

```
         HARNESS ENGINEERING
        /         |          \
CONTEXT ENG   SKILLS ARCH   COST OPT
       |            |            |
  WORKFLOW      MEMORY &      MULTI-AGENT
  (QRSPI)      PERSIST.      ORCHESTR.
       \            |            /
        \     MCP ECOSYSTEM    /
         \         |          /
          HUMAN OVERSIGHT
          (COMPREHENSION DEBT)
```

## Key Tensions Across Themes

| Tension | Stakes |
|---------|--------|
| Velocity vs. comprehension | Organizations accumulating oversight debt faster than technical debt |
| Parallelism vs. coherence | Parallel agents diverge in style/architecture without tight constraints |
| Capability vs. security | More capable models are more vulnerable to tool poisoning |
| Rich harness vs. maintainability | Complex harnesses become their own engineering burden |
| Long sessions vs. context degradation | Dumb zone vs. context richness for cross-file tasks |

## Practitioner Consensus (as of mid-2026)

- **Model selection**: Haiku for workers, Sonnet for orchestrators, Opus for max-reasoning tasks
- **Context budget**: Keep at 40–60%. Compact intentionally at phase boundaries, not reactively
- **Skills vs. subagents**: Skills for expertise injection, subagents for genuine isolation or parallelism
- **MCP security**: Least privilege, path traversal hardening, audit logging are non-negotiable
- **Oversight**: Human comprehension gate before production; AI review catches format errors, not semantic ones
- **Workflow**: QRSPI or equivalent; serial-first, adversarial validation, explicit compaction gates

---

## Related MOCs

- [[MOC - Harness Engineering]] — 19 source articles on harness engineering specifically
- [[MOC - Context Engineering]] — source articles on context management
- [[MOC - Skills, Plugins & Commands]] — SKILL.md implementations and plugin ecosystem
- [[MOC - Claude Code & Coding Agents]] — Claude Code-specific harness configuration
