---
title: "a coding agent with the IDE wired in"
source: "https://omp.sh/docs/"
author:
  - "[[can1357]]"
published:
created: 2026-06-07
description: "Oh My Pi (omp) is a coding agent for the terminal: subagents, plan mode, LSP, DAP, hindsight memory, hashline edits, and time-traveling rules — with a native Rust engine doing the heavy lifting."
tags:
  - "to-process"
  - agent-plugins-mcp
---
## What omp is

omp (pronounced “oh-em-pi”, binary `omp`) is a fork of Mario Zechner’s [Pi](https://github.com/badlogic/pi-mono). It runs as a single Bun process, drives any model provider you have credentials for, and ships a flat tool surface the model uses to read code, run commands, edit files, drive a debugger, and spawn subagents that coordinate over an in-process IRC bus.

Sessions persist as JSONL under `~/.omp/agent/sessions/`. You resume, fork, branch, and share them. Settings, credentials, plugins, and caches all live under `~/.omp/agent/`. Nothing leaves the machine unless you call a tool that does.

New here? Jump to [Quickstart](https://omp.sh/docs/quickstart) for install and first prompt, or [Using omp](https://omp.sh/docs/using) for the interactive-mode anatomy.

## Who it’s for

Engineers who live in a terminal, work across more than one repo, and want a coding agent that reaches for the same affordances they do: `read`, `search`, a debugger, an LSP, subprocesses, GitHub. omp is dry by default and configurable everywhere — a single config file (`~/.omp/agent/config.yml`), one CLI flag, or one slash command away from any behavioural change.

## What’s distinctive

[Sessions branch like git](https://omp.sh/docs/sessions)

Every session is a JSONL file. `/branch` creates a new leaf from any prior message in the same file; `/fork` spawns a new file. `/tree` walks them. Resume from the CLI with `omp -c` or `omp -r`.

[Subagents that DM each other](https://omp.sh/docs/subagents)

The `task` tool fans work out to child `omp` processes. Siblings see each other in their IRC peer list and exchange messages directly — no parent round-trip.

[Hashline edits with stale-anchor recovery](https://omp.sh/docs/editing)

Every line carries a short content-hash anchor. The model edits by anchor instead of reproducing whitespace, and stale anchors are caught before a file is corrupted.

[LSP and DAP, in-process](https://omp.sh/docs/code-intelligence)

[lsp](https://omp.sh/docs/code-intelligence) drives rename, references, code actions, diagnostics, hover. The [debug](https://omp.sh/docs/debugging) tool wraps DAP for breakpoints, step, and locals across bundled adapters (gdb, lldb-dap, debugpy, dlv, js-debug-adapter, …).

[GitHub as a virtual filesystem](https://omp.sh/docs/github)

`read pr://1428`, `read issue://1234`, `read pr://1428/diff/3`. Issues, PRs, and diffs are virtual markdown the agent reads with the same `read` tool it uses for local files.

[Bring any provider](https://omp.sh/docs/providers)

OAuth into Claude Pro/Max, ChatGPT, Copilot, Cursor, Z.AI, and others; or drop an API key in the environment. Per-role models (`main`, `smol`, `slow`, `plan`) resolve automatically against what you’re authenticated for.

[Plan mode](https://omp.sh/docs/plan)

`/plan` sandboxes a planning turn against a separate planner model. On approval you choose: execute and purge, keep the transcript, or compact context.

## Where to go next

- [Quickstart](https://omp.sh/docs/quickstart) — install, log in, first prompt.
- [Using omp](https://omp.sh/docs/using) — interactive mode, editor, message queue, modes.
- [Sessions](https://omp.sh/docs/sessions) — resume, fork, branch, share.
- [Slash commands](https://omp.sh/docs/slash) and [Keybindings](https://omp.sh/docs/keybindings) — in-chat controls.
- [Providers](https://omp.sh/docs/providers) and [Environment variables](https://omp.sh/docs/env) — credentials and configuration.
- [CLI reference](https://omp.sh/docs/cli) — every flag and subcommand.

## Conventions

- The binary is `omp`. The package is `@oh-my-pi/pi-coding-agent`. The agent dir is `~/.omp/agent/`; settings live in `~/.omp/agent/config.yml`; credentials in `~/.omp/agent/agent.db`.
- Slash commands are written like `/plan` and run inside an active session.
- CLI flags use long form (`--resume`); short aliases are listed where they exist on [the CLI page](https://omp.sh/docs/cli).
- Settings keys are dotted paths into `config.yml`, e.g. `memory.backend`.
- Internal URLs use `scheme://` form and resolve through the `read` tool: `pr://`, `issue://`, `skill://`, `artifact://`, `conflict://`.