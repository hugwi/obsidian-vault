---
title: "GitHub - shep-ai/cli: Multi-Session SDLC Control Center for AI Coding Agents"
source: "https://github.com/shep-ai/cli"
author: "github.com/shep-ai"
published: 
created: 2026-03-23
description: "Multi-Session SDLC Control Center for AI Coding Agents - shep-ai/cli"
tags:
  - to-process
  - orchestration
---

# shep-ai/cli


main


Go to file


Code


Open more actions menu


# Shep AI


### One command. Full lifecycle. Merged PR.


*Describe a feature in plain English — Shep researches, plans, codes, tests, and opens a PR. You approve when you want to, or let it run hands-free.*


[![CI](https://github.com/shep-ai/cli/actions/workflows/ci.yml/badge.svg)](https://github.com/shep-ai/cli/actions/workflows/ci.yml)
[![npm version](https://camo.githubusercontent.com/c98101b881b1c68f630c490ad1d74a39127348ac908ca90f9ec9c4a7ebba6d79/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f407368657061692f636c692e7376673f636f6c6f723d636233383337266c6f676f3d6e706d)](https://www.npmjs.com/package/@shepai/cli)
[![License: MIT](https://camo.githubusercontent.com/fdf2982b9f5d7489dcf44570e714e3a15fce6253e0cc6b5aa61a075aac2ff71b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)](https://opensource.org/licenses/MIT)
[![TypeScript](https://camo.githubusercontent.com/395ddc41dfd83dd12893aa893927b83cb9bd085877bf5cc4140c9cdbb2ad6d7f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f547970655363726970742d352e332b2d3331373863362e7376673f6c6f676f3d74797065736372697074266c6f676f436f6c6f723d7768697465)](https://www.typescriptlang.org/)
[![Node.js](https://camo.githubusercontent.com/cd6f31016a8911e73cf694d3e7fc6b03da52f1f475e8bcad843f83cbaa7858ea/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4e6f64652e6a732d25453225383925413531382d3333393933332e7376673f6c6f676f3d6e6f64652e6a73266c6f676f436f6c6f723d7768697465)](https://nodejs.org/)
[![pnpm](https://camo.githubusercontent.com/7e26fd6e79f2c463866b5a6606b4b1cc261305f1c482a87ae64a696da7135460/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f706e706d2d254532253839254135382d6636393232302e7376673f6c6f676f3d706e706d266c6f676f436f6c6f723d7768697465)](https://pnpm.io/)
[![PRs Welcome](https://camo.githubusercontent.com/dd0b24c1e6776719edb2c273548a510d6490d8d25269a043dfabbd38419905da/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5052732d77656c636f6d652d627269676874677265656e2e737667)](https://github.com/shep-ai/cli/pulls)
[![Conventional Commits](https://camo.githubusercontent.com/5497733cb48db7a6799abcf3b19071e4024caee5cc78544970ce686017b7adcd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6e76656e74696f6e616c253230436f6d6d6974732d312e302e302d6665353139362e7376673f6c6f676f3d636f6e76656e74696f6e616c636f6d6d697473266c6f676f436f6c6f723d7768697465)](https://conventionalcommits.org)
[Features](https://github.com/shep-ai/cli/#features) · [Quick Start](https://github.com/shep-ai/cli/#quick-start) · [CLI Reference](https://github.com/shep-ai/cli/#cli-reference) · [Architecture](https://github.com/shep-ai/cli/#architecture) · [Contributing](https://github.com/shep-ai/cli/#contributing)


[![Shep AI](https://github.com/shep-ai/cli/raw/main/docs/screenshots/cover.png)](https://github.com/shep-ai/cli/blob/main/docs/screenshots/cover.png)
## Quick Start



```
# Try it instantly — no install needed
npx @shepai/cli

# Or install globally
npm i -g @shepai/cli
shep

# Browser opens at http://localhost:4050 — you're in
```

## Features



```
shep feat new "add stripe payments" --allow-all --push --pr
# ↳ PRD → research → plan → code → tests → PR → CI watch — done.
```

* **Full lifecycle in one shot** — From idea to merged PR: requirements, technical research, implementation plan, code with tests, PR creation, and CI fix loop
* **Approve or go hands-free** — Three review gates (PRD, Plan, Merge) you can enable, disable, or skip entirely with `--allow-all`
* **Run 10 features in parallel** — Each gets its own git worktree — switch context instantly, no stashing, no branch juggling, no conflicts
* **Pick your agent** — Claude Code, Cursor CLI, or Gemini CLI — swap per feature, per repo, anytime
* **Live dashboard** — Interactive graph of every repo and feature — review diffs, approve merges, launch dev servers, all in-browser
* **100% local, zero signup** — SQLite in `~/.shep/`, nothing leaves your machine, no account needed



>  **[See the full Features Guide with screenshots →](https://github.com/shep-ai/cli/blob/main/docs/FEATURES.md)**
> 
>  


## CLI Reference


### Daemon



```
shep                                  Start daemon + onboarding (first run)
shep start [--port <number>]          Start web UI daemon (background, default port 4050)
shep stop                             Stop the running daemon
shep restart                          Restart the daemon
shep status                           Show daemon status and live metrics
shep ui [--port] [--no-open]          Start the web UI in the foreground

```

### Feature Management



```
shep feat new <description>           Create a new feature
      [--repo] [--push] [--pr]
      [--allow-prd] [--allow-plan] [--allow-merge] [--allow-all]
      [--parent] [--fast] [--model] [--attach]
shep feat ls [--repo]                 List features
shep feat show <id>                   Show feature details
shep feat del <id>                    Delete a feature
shep feat resume <id>                 Resume a paused feature
shep feat review <id>                 Review a feature
shep feat approve <id> [--comments]   Approve a feature
shep feat reject <id> [--feedback]    Reject a feature
shep feat logs <id>                   View feature logs

```

### Agent Management



```
shep agent ls                         List agents
shep agent show <id>                  Show agent details
shep agent stop <id>                  Stop a running agent
shep agent logs <id>                  View agent logs
shep agent delete <id>                Delete an agent
shep agent approve <id>               Approve an agent action
shep agent reject <id>                Reject an agent action

```

### Repository & Session Management



```
shep repo ls                          List repositories
shep repo show <id>                   Show repository details
shep session ls                       List sessions
shep session show <id>                Show session details

```

### Settings



```
shep settings                         Launch setup wizard
shep settings show                    Display current configuration
shep settings init                    Initialize settings
shep settings agent                   Configure AI coding agent
shep settings ide                     Configure IDE
shep settings workflow                Configure workflow
shep settings model                   Configure model

```

### Tools



```
shep tools list                       List tools with install status
shep install <tool> [--how]           Install a dev tool
shep ide-open [--ide] [--dir]         Open IDE in directory

```

### Other



```
shep version                          Show version info
shep upgrade                          Upgrade to latest version
shep run <agent> [-p prompt] [-r repo] [-s]   Run an agent directly

```

## Architecture


Clean Architecture with four layers. Dependencies point inward — domain has zero external deps.


Some content could not be imported from the original document. [View content ↗](https://viewscreen.githubusercontent.com/markdown/mermaid?docs_host=https%3A%2F%2Fdocs.github.com&color_mode=light#1b103c08-3ab8-49d7-8c16-f255728b77bf) 


 Loading 



```
flowchart TB
    P["<b>Presentation</b><br/>CLI · Web UI · TUI"]
    A["<b>Application</b><br/>Use Cases · Orchestration · Ports"]
    D["<b>Domain</b><br/>Entities · Value Objects · Services"]
    I["<b>Infrastructure</b><br/>SQLite · LangGraph · DI"]

    P --> A --> D
    I --> A

    style P fill:#dbeafe,stroke:#3b82f6,color:#1e3a5f
    style A fill:#fef3c7,stroke:#f59e0b,color:#78350f
    style D fill:#d1fae5,stroke:#10b981,color:#064e3b
    style I fill:#ede9fe,stroke:#8b5cf6,color:#4c1d95

```



| Layer | Path | Responsibility |
| --- | --- | --- |
| Domain | `packages/core/src/domain/` | Business logic, TypeSpec-generated types |
| Application | `packages/core/src/application/` | Use cases, output port interfaces |
| Infrastructure | `packages/core/src/infrastructure/` | SQLite repos, LangGraph agents, DI (tsyringe) |
| Presentation | `src/presentation/` | CLI (Commander), TUI (Inquirer), Web UI (Next.js) |


### Feature Lifecycle


Every feature progresses through a structured SDLC pipeline with 9 states:



```
Started -> Analyze -> Requirements -> Research -> Planning -> Implementation -> Review -> Maintain
                                                                                   |
                                                                               (Blocked)

```

Human approval gates are configurable at PRD, Plan, and Merge phases. In `--allow-all` mode the agent handles everything autonomously.


### Tech Stack




| Component | Technology |
| --- | --- |
| Language | TypeScript (ES2022) |
| Package Manager | pnpm |
| CLI Framework | Commander |
| TUI Framework | [@inquirer/prompts](https://github.com/SBoudrias/Inquirer.js) |
| Web UI | Next.js 16 + React 19 + shadcn/ui + Tailwind CSS 4 |
| Graph Viz | React Flow (XYFlow) 12 |
| Design System | Storybook 8.x |
| Build Tool | tsc + tsc-alias (prod), tsx (CLI dev), Next.js (web dev) |
| Database | SQLite (better-sqlite3, per-repo) |
| Domain Models | TypeSpec -> generated TypeScript |
| Agent System | [LangGraph](https://www.langchain.com/langgraph) (`@langchain/langgraph`) |
| DI Container | tsyringe |
| Testing | Vitest (unit/integration) + Playwright (e2e) |
| Methodology | TDD (Red-Green-Refactor) |


### Supported Tools


Shep can detect, install, and manage the following tools:




| Category | Tools |
| --- | --- |
| IDEs | Alacritty, Antigravity, Cursor, iTerm2, Kitty, TMux, VS Code, Warp, Windsurf, Zed |
| CLI Agents | Claude Code, Cursor CLI, Gemini CLI |
| Dev Tools | Git, GitHub CLI |


### Web UI


The web dashboard runs at `http://localhost:4050` and provides:


* **Dashboard canvas** — Interactive React Flow graph with feature and repository nodes
* **Feature drawer** — Tabs for overview, activity, approval, rejection, PR info, deployment, and timeline
* **Create feature form** — Start new features from the UI
* **Settings, Tools, Skills, and Version pages**
* **Real-time updates** via Server-Sent Events (SSE)


### Data Model



```
Repository --+-- Feature --+-- Plan --+-- Task -- ActionItem
             |             |          +-- Artifact
             |             +-- Requirement -- Research

```

All data lives locally in `~/.shep/`. Per-repo SQLite databases. No cloud dependency.


## Documentation




| Document | Description |
| --- | --- |
| [Features Guide](https://github.com/shep-ai/cli/blob/main/docs/FEATURES.md) | Full features overview with screenshots |
| [Competitive Landscape](https://github.com/shep-ai/cli/blob/main/docs/competitors) | How Shep fits in the AI dev tool ecosystem |
| [CLAUDE.md](https://github.com/shep-ai/cli/blob/main/CLAUDE.md) | Guidance for Claude Code instances |
| [AGENTS.md](https://github.com/shep-ai/cli/blob/main/AGENTS.md) | Agent system architecture |
| [CONTRIBUTING-AGENTS.md](https://github.com/shep-ai/cli/blob/main/CONTRIBUTING-AGENTS.md) | AI agent contribution guidelines |
| [Architecture](https://github.com/shep-ai/cli/blob/main/docs/architecture) | System design and patterns |
| [Concepts](https://github.com/shep-ai/cli/blob/main/docs/concepts) | Core domain concepts |
| [UI](https://github.com/shep-ai/cli/blob/main/docs/ui) | Web UI architecture and design system |
| [Guides](https://github.com/shep-ai/cli/blob/main/docs/guides) | User guides and tutorials |
| [Development](https://github.com/shep-ai/cli/blob/main/docs/development) | Contributing and development setup |
| [API Reference](https://github.com/shep-ai/cli/blob/main/docs/api) | Interface and model documentation |


## Contributing


We welcome contributions from humans and AI agents alike.


* **Humans**: See [CONTRIBUTING.md](https://github.com/shep-ai/cli/blob/main/CONTRIBUTING.md)
* **AI Agents**: See [CONTRIBUTING-AGENTS.md](https://github.com/shep-ai/cli/blob/main/CONTRIBUTING-AGENTS.md)
* **Spec-driven workflow**: All features start with `/shep-kit:new-feature` — see [Spec-Driven Workflow](https://github.com/shep-ai/cli/blob/main/docs/development/spec-driven-workflow.md)


## License


MIT — see [LICENSE](https://github.com/shep-ai/cli/blob/main/LICENSE).