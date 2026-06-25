---
categories:
  - "[[Resources]]"
title: "MOC: Harness Engineering"
category: moc
created: 2026-06-13
tags:
  - moc
  - harness-engineering
---

# Harness Engineering

> Map of Content — 19 notes

## Notes

- [[# Skill Issue: Harness Engineering for Coding Agents (01ktgrqtkbb93eq29tsqg9jzh9).md|# Skill Issue: Harness Engineering for Coding Agents]] — Harness engineering is the art and science of leveraging your coding agent's
- [[# Writing a good CLAUDE.md (01knz6zbkjmg5dr42qbmzjet25).md|# Writing a good CLAUDE.md]] — `CLAUDE.md` is a high-leverage configuration point for Claude Code. Learning
- [[Agent Harness Engineering (01krkd6ghz8q0j5p9pn31jdxhs).md|Agent Harness Engineering]] — A coding agent is the model plus everything you build around it: prompts,
- [[Building Claude Code with Harness Engineering (01krtjqfspzfdchqatdyz8d9vk).md|Building Claude Code with Harness Engineering]] — Multi-agents, MCP, skills system, context pipelines and more
- [[GitHub - HKUDS-OpenHarness: "OpenHarness: Open Agent Harness -- Ultra… (01knd2dj15ds5z1npbmnzx5vyj).md|GitHub - HKUDS/OpenHarness: \"OpenHarness: Open Agent Harness -- Ultra-Lightweight]] — OpenHarness: Open Agent Harness -- Ultra-Lightweight Claude Code\" - HKUDS/OpenHarness
- [[GitHub - aiming-lab-AutoHarness: AutoHarness: Automated Harness Engine… (01kr4q2s9ceznehjjyv70rfbjb).md|GitHub - aiming-lab/AutoHarness: AutoHarness: Automated Harness Engineering]] — AutoHarness: Automated Harness Engineering for AI Agents - aiming-lab/AutoHarness
- [[Harness engineering for coding agent users (01kqzbtzxywvasn849tsrq3ya8).md|Harness engineering for coding agent users]] — A mental model for building trust in coding agents through feedforward guides,
- [[Harness engineering: leveraging Codex in an agent-first world | OpenAI (01kr4qdgje4agq8ga36x5931s7).md|Harness engineering: leveraging Codex in an agent-first world | OpenAI]] — By Ryan Lopopolo, Member of the Technical Staff
- [[Harnesses in AI: A Deep Dive  Tejas Kumar, IBM (01kryd5baj0vybmb83d44ehqjd).md|Harnesses in AI: A Deep Dive — Tejas Kumar, IBM]] — The agent hit a login page, panicked, reported success anyway, and the upvote
- [[How to Harness Coding Agents with the Right Infrastructure (01ktcmyyfatnb3vgjd85bsg98x).md|How to Harness Coding Agents with the Right Infrastructure]] — OpenAI’s harness engineering team built a million-line codebase with three
- [[I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Change… (01ktcc6ddhqwb948gxtge2kr3w).md|I Improved 15 LLMs at Coding in One Afternoon. Only the Harness Changed.]] — Cross-posted from X / @_can1357 In fact only the edit tool changed. That’s
- [[I ditched Claude Code and OpenCode for Pi, and my coding workflow beca… (01kn97w5zxafvd0pty0ctpdeve).md|I ditched Claude Code and OpenCode for Pi, and my coding workflow became predictable]] — It might not be everyone's first choice, but I like it
- [[I was tired of AI coding agents breaking my projects. Here is the "Har… (01krc0tfzhc5x2x93etkecqqpg).md|I was tired of AI coding agents breaking my projects. Here is the \"Harness]] — If you're using AI agents (Cursor, Claude Code, GitHub Copilot Workspaces)
- [[Rethinking AI Agents: The Rise of Harness Engineering (01kqzd06mpj5tjxag1cfp5beg9).md|Rethinking AI Agents: The Rise of Harness Engineering]] — Same model. Same benchmark. 6× the performance difference. If you are building
- [[Skill Issue Harness Engineering for Coding Agents.md|Skill Issue: Harness Engineering for Coding Agents]] — Harness engineering is the art and science of leveraging your coding agent's configuration points to improve output qual
- [[What is AI Harness Engineering? Your Guide to Controlling Autonomous S… (01kr4mqdne5hdp0y3cx4gs3209).md|What is AI Harness Engineering? Your Guide to Controlling Autonomous Systems]] — From Constraints to Feedback Loops, the Core of Trustworthy AI.
- [[Why agent harnesses fail inside cloud-native systems (01krkhqxyws5b6ebajgm1n4z03).md|Why agent harnesses fail inside cloud-native systems]] — Coding agents need feedback loops to self-correct. In cloud native systems,
- [[agentspluginsdeveloper-essentialsskillse2e-testing-patternsSKILL.md at main.md|agents/plugins/developer-essentials/skills/e2e-testing-patterns/SKILL.md at main]] — Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor, OpenCode, and Gemini CLI - agents/plugins/d
- [[agentspluginsdeveloper-essentialsskillserror-handling-patternsSKILL.md at main.md|agents/plugins/developer-essentials/skills/error-handling-patterns/SKILL.md at main]] — Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor, OpenCode, and Gemini CLI - agents/plugins/d

---

## TODO — To Build

### Hard enforcement: hooks + linters

> Captured 2026-06-14 from the `plankton-code-quality` ECC skill before deleting it (skill was a dormant reference doc, never wired). Source tool: **Plankton** by @alxfazio — https://github.com/alexfazio/plankton

**Goal:** upgrade ECC quality hooks from *synchronous reporters* to *hard enforcement*. Steal the pattern, not the whole tool — my repo is a TS monorepo with its own CI lint/format/typecheck, so Plankton's Python/uv/bun/polyglot linter zoo is mostly N/A.

**Three things to build (priority order):**

1. **Async subprocess auto-fix (model-routed)** — biggest win. Current ECC hooks (`post-edit-format`, `post-edit-typecheck`, `quality-gate`) *report* violations into my main context, so I burn tokens fixing lint. Plankton spawns a separate `claude -p` subprocess to fix them off-context, routed by complexity: Haiku=style, Sonnet=refactor, Opus=types. Main agent only sees what the subprocess couldn't fix.
2. **Hard config-tamper block (preventive, not detective)** — current ECC only *flags* config edits at the Stop hook (after the fact). Plankton uses a PreToolUse hook that *blocks* edits to `.ruff.toml` / `biome.json` / `tsconfig.json` before they land, so the agent can't disable a rule instead of fixing the code. Security-relevant: detective → preventive.
3. **(Lower priority) breadth + PM enforcement** — Plankton runs 20+ linters (shellcheck, hadolint, yamllint, markdownlint, bandit, semgrep, knip, vulture) and blocks legacy package managers (`pip`/`npm` → `uv`/`bun`). Mostly redundant/N-A for the TS monorepo; cherry-pick `knip` (dead exports) and a PreToolUse PM guard if useful.

**Architectural note:** the one idea worth stealing even without adopting Plankton = move quality from a synchronous reporter (violation → my context → I fix) to an async fixer (violation → subprocess fixes → I only see the remainder).

**Next step:** prototype #1 as an ECC PostToolUse hook in `~/.agents/scripts/hooks/` that calls `claude -p` with the violations JSON and a tiered `--model` flag.
