---
categories:
  - "[[Resources]]"
domain: engineering
title: "Flux: A Kanban Board That Speaks MCP"
source: "https://paddo.dev/blog/flux-kanban-for-ai-agents"
author: "paddo.dev"
published: 2026-01-14
created: 2026-03-15
description: "Task management designed for AI coding agents. CLI-first, git-native sync,"
tags:
  - to-process
  - agent-configuration
---

AI coding agents are good at writing code. They’re bad at knowing what to work on next.


Give Claude Code a well-scoped task and it executes. But ask it to “work on the project” and it flounders. There’s no shared understanding of priorities, dependencies, or what’s actually ready to be worked on.


My mate Steve had an idea: a Kanban board designed for AI agents. I loved it so much I chipped in. The result is [Flux](https://github.com/sirsjg/flux).


## What Flux Does


Flux is task management with first-class AI integration:


* **MCP server** - Claude Code (and other MCP clients) can read tasks, update status, add comments
* **CLI-first** - `flux ready` shows unblocked tasks sorted by priority. Pipe it to your agent.
* **Git-native sync** - Tasks sync via `flux pull` / `flux push` on a dedicated branch. JSON or SQLite storage - your choice.
* **Dependencies** - Tasks can depend on other tasks. Blocked tasks don’t show up in `flux ready`.
* **Priorities** - P0/P1/P2 levels. Agents work on P0s first.
* **Web dashboard** - View the board, drag tasks, manage projects. Public users get readonly, authenticated users get full access.
* **Agent-friendly** - Agents can work the board too. [Momentum](https://github.com/sirsjg/momentum), a companion TUI, lets agents pick tasks reactively. More on that soon.



>   Flux isn’t just another Kanban board - it’s the open-source engine for the future of work. 
> 
>  — Steve, Flux creator 


## Why Not Linear/Jira/GitHub Issues?


Those tools are designed for humans coordinating with humans. They have:


* Complex UIs with lots of features agents don’t need
* OAuth flows and API tokens that are painful to configure
* No native MCP support
* Sync models that don’t map to local-first development


Flux is deliberately minimal. A CLI that works offline, stores to a local database, syncs via git or a remote server, and exposes tasks via MCP.


  Two ways in

 **MCP**: Add Flux as an MCP server and agents interact with tasks directly in conversation. **CLI**: Agents can shell out to `flux ready`, `flux task create`, etc. Both are first-class. Pick what fits your workflow.

  
## The CLI



```
# Initialize in a repo
flux init

# Show unblocked tasks sorted by priority
flux ready

# Create a task
flux task create "Fix login bug" -P 0

# Mark it in progress
flux task start abc123

# Mark it done
flux task done abc123 --note "Fixed null check in auth handler"

# Sync with team
flux pull && flux push "Completed auth fixes"
```

The `--note` flag is useful for agent memory. Comments persist on tasks, so context survives across sessions.


## Infra? Your Call


Flux adapts to how you want to work:


* **Git-only** - No server needed. `flux pull` / `flux push` syncs via a `flux-data` branch. Zero infra.
* **Self-hosted** - Run the server for a web dashboard and SSE updates. Your machine, your data.


Storage is similarly unopinionated - JSON for simplicity, SQLite for concurrency. Pick what fits.



>   Tasks live here, but how they get done? That’s up to you. 
> 
>  — Steve 


  Works offline

 Everything works locally. The server and web UI are optional - useful for dashboards or multi-repo aggregation, but the CLI is self-contained.

  
## What Flux Doesn’t Do


Being honest about scope:


* **Not a full PM tool** - No sprints, story points, or burndown charts
* **No user accounts** - Single API key auth, no team permissions (yet)
* **No mobile app** - CLI and web only
* **Early stage** - We’re actively building this


## Dogfooding


We’re using Flux to build Flux. The public board is at [app.getflux.dev](https://app.getflux.dev).


Current tasks include multi-API key support, web authentication, and publishing workflows. All managed in Flux, executed by AI agents, visible on the board.


It’s a good test of whether the tool actually works for AI-assisted development.


## Try It


**Docker/Podman** (quickest):



```
curl -fsSL https://raw.githubusercontent.com/sirsjg/flux/main/scripts/quickstart.sh | bash
```

Starts the web UI at [localhost:3000](http://localhost:3000) and MCP server. Add to Claude Code:



```
claude mcp add flux -- docker run -i --rm -v flux-data:/app/packages/data sirsjg/flux-mcp
```

**npm** (CLI-first):



```
npm install -g flux-tasks # or: bun install -g flux-tasks
flux init # in your project
```

**From source**:



```
git clone https://github.com/sirsjg/flux && cd flux
bun install && bun run build
cd packages/cli && bun link
```

Check the [installation docs](https://github.com/sirsjg/flux/tree/main/docs) for more options.


## Links