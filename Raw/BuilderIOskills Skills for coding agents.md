---
categories:
  - "[[Clippings]]"
title: "BuilderIO/skills: Skills for coding agents"
source: "https://github.com/BuilderIO/skills/tree/main"
author:
published:
created: 2026-06-18
rating: 
action: 
description: "Skills for coding agents. Contribute to BuilderIO/skills development by creating an account on GitHub."
tags:
  - "clippings"
---
## Skills for coding agents

Small, composable skills for coding agents.

These skills are for teams that want the agent to stay sharp where judgment matters: orchestration, review, planning, validation, docs discipline, and clear communication. They are not a giant process framework. Install the pieces you want, adapt them to your project, and let the model keep room to think.

```
npx @agent-native/skills@latest add
```

The interactive picker puts `/visual-plan` and `/visual-recap` first and selects only those by default. See the [full CLI docs below](#install).

## Skills

### /visual-plan

Turn ordinary text plans into rich interactive visual plans with diagrams, file maps, annotated code, open questions, and UI/prototype review when useful.

Solves for plans that are too important to bury in chat. The output is scannable, commentable, and intuitive enough for a human to approve before code changes start.

![Visual plan review surface](https://github.com/BuilderIO/skills/raw/main/media/visual-plan.png)

Visual plans are MDX, customizable with your own components, and are viewed with the [Agent-Native plans app](https://www.agent-native.com/docs/template-plan). [Source here](https://github.com/BuilderIO/agent-native/)

### /visual-recap

Turn a branch, commit, or PR diff into an interactive visual recap with annotated diffs, diagrams, API/schema summaries, file maps, UI state summaries, and focused review notes.

Solves for diffs that hide the shape of the change. Reviewers can understand contracts, architecture moves, schema changes, and UI impact before diving into raw line-by-line review.

![Visual recap review surface animation](https://github.com/BuilderIO/skills/raw/main/media/visual-recap.gif)

Visual recaps are MDX, customizable with your own components, and are viewed with the [Agent-Native plans app](https://www.agent-native.com/docs/template-plan). [Source here](https://github.com/BuilderIO/agent-native/)

You can also install a GitHub action for these to be automatically generated for every PR with

```
npx @agent-native/skills@latest add
```

[![Example of a visual plan posted to a PR](https://camo.githubusercontent.com/2b02f760f55b2b67d93b8c2b48d2dc7e7336a1df4a2de0e853d5f5ae2a43080b/68747470733a2f2f63646e2e6275696c6465722e696f2f6170692f76312f696d6167652f617373657473253246594a494762346930316a7677305352644c3542742532466366396261633339366366323461346261393736666333333161663666633564)](https://camo.githubusercontent.com/2b02f760f55b2b67d93b8c2b48d2dc7e7336a1df4a2de0e853d5f5ae2a43080b/68747470733a2f2f63646e2e6275696c6465722e696f2f6170692f76312f696d6167652f617373657473253246594a494762346930316a7677305352644c3542742532466366396261633339366366323461346261393736666333333161663666633564)

### /agent-watchdog

Audit another agent's work from a Codex session, Claude Code transcript, PR, branch, or run summary.

Solves for cross-agent handoffs: watch until done, reconstruct what was asked, check what actually changed and verified, report gaps, and optionally make narrow fixes.

### /plan-arbiter

Compare competing agent plans and choose one executable direction.

Solves for multi-agent planning loops where Codex, Claude Code, or other agents produce separate strategies. The output is a decision memo with the winning or hybrid plan, rejected alternatives, verification gates, and executor recommendation.

### /plow-ahead

Keep working through ordinary ambiguity and finish with a clear decision recap.

Solves for explicit autonomy requests: the agent converts routine questions into assumptions, proceeds with conservative choices, validates the work, and recaps the decisions it made without stopping.

### /efficient-fable

Use Claude Fable as the orchestrator, architect, synthesizer, and final judge while lighter agents handle token-heavy research, coding, testing, and log reduction.

Solves for expensive-model waste: Fable should spend tokens on judgment, not on reading every file, reducing every log, or manually running every browser check.

![Fable orchestrator diagram](https://github.com/BuilderIO/skills/raw/main/skills/efficient-fable/assets/fable-orchestrator-dark.png)

### /efficient-frontier

Apply the same orchestration as `/efficient-fable` to any high-cost frontier model: preserve the expensive model for planning, tradeoffs, integration, validation strategy, and final review; use cheaper agents for bounded heavy lifting.

Solves for broad work that can be parallelized without asking the most expensive model to do every scan and every edit itself.

### /stay-within-limits

Check current 5-hour and weekly usage before substantial work and between parallel waves, then pause new execution at 95% until the active window is clear enough to continue.

Solves for long-running agent sessions that accidentally exhaust the current budget window mid-task instead of pausing cleanly and resuming with a self-contained plan.

### /quick-recap

Add a concise final status block convention so every completed response ends with a clear green, yellow, or red work-state signal.

Solves for ambiguity at the end of agent work: done, pending a specific non-routine step, or blocked on the user.

Example green status:

```
🟢 Updated quick recap docs with output examples
```

Example yellow status:

```
🟡 Code updated, set PROVIDER_WEBHOOK_SECRET before testing webhooks
```

### /read-the-damn-docs

Make agents web-search for authoritative docs before they guess from stale model memory.

Solves for version drift and API folklore: package installs, framework config, SDK imports, provider limits, auth, security, billing, data, migrations, deploys, and repo-specific contracts all require a docs pass before implementation. For external APIs and current product behavior, web search for official docs is usually the first move.

## Install

Run the installer:

```
npx @agent-native/skills@latest add
```

The picker shows the full catalog, with `/visual-plan` and `/visual-recap` at the top and preselected by default. Toggle any additional skills you want.

The installer walks you through the choices:

- Which skills to install.
- Where visual plans and recaps should live: hosted shareable links (recommended), local files only, or a self-hosted/custom Plan app.
- Agent Skills through the shared `.agents` path for Codex, Pi, Cursor, OpenCode, GitHub Copilot / VS Code, and similar agents, plus Claude Code's native skills path when selected.
- User-level or project-level install.
- Whether to add managed `AGENTS.md` / `CLAUDE.md` instruction blocks when the selected skills have always-on guidance.
- Whether to add the PR Visual Recap GitHub Action when `/visual-recap` is selected.

Skip the picker with `--skill`:

```
npx @agent-native/skills@latest add --skill quick-recap
npx @agent-native/skills@latest add --skill visual-recap --with-github-action
```

You can also use Vercel's `skills` CLI for a plain skill-folder copy:

```
npx skills@latest add BuilderIO/skills --skill quick-recap
```

That installer is useful for quick copying, but it does not add the managed `AGENTS.md` / `CLAUDE.md` instruction blocks or the PR Visual Recap GitHub Action that pair well with these skills.