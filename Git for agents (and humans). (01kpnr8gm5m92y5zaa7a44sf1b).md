---
categories:
  - "[[Resources]]"
domain: engineering
title: "Git for agents (and humans)."
source: "https://oobo.ai/"
author: "NoCode, Inc."
published: 
created: 2026-04-20
description: "A transparent git decorator that enriches every commit with AI context:"
tags:
  - to-process
  - dev-tools
---

[oobo.ai](https://oobo.ai/)


open source · Apache 2.0 / MIT


Oobo gives every commit memory. Which AI session led to the change, what it cost, who wrote what. Git stays the code ledger. Oobo becomes the work ledger.


## Git tracks code.Nobody tracks work.


AI agents now write significant portions of production code. They commit, push, open PRs, run pipelines. But the trail of how software gets built is fragmented and mostly lost.


What's invisible


* What the agent was trying to do
* Which prompt produced the change
* How many agents were involved
* Why a technical decision was made
* Whether code advanced a business goal
* What conversations and retries led here


## The anchor.


Oobo's core primitive. It extends a git commit with AI context: which sessions contributed, token counts, code attribution (AI vs human lines), model used, session duration. Anchors sync via a git orphan branch that travels with your repo.



```
Git:   commit = diff(files)
Oobo:  anchor = commit + sessions + tokens + attribution
```

what happens on commit



```
$ oobo commit -m "fix auth middleware"

# under the hood:
1. Execute real git commit
2. Detect write operation
3. Read AI sessions from local tool storage
4. Build anchor: commit + sessions + tokens + attribution
5. Write anchor to local DB + git orphan branch
6. Fire event to endpoint (if configured)
7. Return git's exit code unchanged
```

Read operations (status, log, diff) pass straight through to git with zero overhead.


## Two memories.


Oobo captures two kinds of memory. Together they turn disposable local history into a durable, searchable work record.


Repo memory


Travels with git.


Anchor metadata syncs via the orphan branch. Clone a repo that was used with oobo and the full enriched history is already there. Shared when desired.


Developer memory


Lives locally. Spans all projects.


Local SQLite with transcripts, cross-project search, token analytics, cost tracking. Useful every day. Which repo did I fix auth in last week? How many tokens did I spend today?


## Quick start.


Install, setup, use. Then explore what happened.



```
$ curl -fsSL https://oobo.ai/install.sh | bash
$ oobo setup                        # detects your tools, configures endpoint
```

macOS · Linux



```
$ oobo commit -m "fix auth middleware"
$ oobo push origin main
$ oobo status                       # reads pass through to git
```

see what happened



```
$ oobo anchors                      # enriched commit history with AI context
$ oobo sessions                     # browse AI chat sessions (interactive TUI)
$ oobo sessions search "auth bug"   # search by keyword
$ oobo stats                        # token usage, attribution, analytics
$ oobo stats --tool cursor --since 7d
```


```
$ oobo alias install                # adds alias git=oobo to your shell rc
$ git commit -m "now this is oobo"  # transparent, you don't think about it
$ oobo card                         # shareable developer stats card
```

## Built for agents.


Agents commit code constantly, across tools, often in parallel. Without oobo, there is no record of which agent wrote what, how many tokens it took, or which conversation produced a given function.


Every command supports `--agent` for compact, pipe-delimited output (minimal tokens) and `--json` for full structured JSON. The installer has a silent mode. Agent lifecycle hooks track sessions in real time for Cursor, Claude Code, Gemini CLI, and OpenCode.



```
$ curl -fsSL https://oobo.ai/install.sh | bash -s -- --agent
{"status":"ok","version":"0.1.0","binary":"/home/agent/.oobo/bin/oobo","platform":"linux-x86_64"}
```

--agent and --json



```
$ oobo sessions list --agent         # compact pipe-delimited text (low token cost)
$ oobo sessions list --json          # full structured JSON with messages
$ oobo anchors --agent               # compact enriched commit history
$ oobo stats --json                  # analytics as structured JSON
```


```
$ oobo agent                         # prints skill file to stdout
# Symlinked into ~/.agents/, ~/.claude/, ~/.codex/, ~/.cursor/, ~/.gemini/
# Auto-discovered by all major AI coding tools during setup.
```

## The bigger picture.


The CLI is the foundation. On top of it, Oobo builds a full engineering intelligence layer for teams where humans and agents build software together.


A causal trace of work and decisions.


Not just what changed, but why. Connects commits to sessions, prompts to outcomes, agent actions to human decisions. Includes handoffs, reversals, and retries.


Directional coherence across humans, agents, and goals.


Understand whether engineering effort is advancing business goals or drifting. Visibility into what humans and agents are actually working on, and whether it lines up.


Risk & Health


Latent system stress before it surfaces.


Detect fragmentation, ownership gaps, and areas where agent-generated code is accumulating without human review. Signals that something needs attention before it becomes a problem.


Executive-grade engineering intelligence.


Automated reports that answer: what was shipped, why, by whom (human or agent), and whether it moved a goal forward. Built from anchors and session data, not self-reported status updates.


The more autonomous software creation becomes, the more valuable execution truth becomes.


## 15 tools. Zero plugins.


Oobo discovers and indexes AI sessions by reading existing local data. All access is read-only. No plugins, no browser extensions, no API keys required.


## Private by default.


* **Read-only.** never writes to AI tool directories
* **Local by default.** everything stays in ~/.oobo/. Nothing leaves your machine unless you configure an endpoint
* **Secret redaction.** sessions are scrubbed with gitleaks patterns before any sharing
* **No telemetry.** oobo never collects or sends data unless you explicitly opt in
* **Transparency is opt-in.** anchor metadata always syncs via git. Transcripts stay local unless you turn transparency on


One product. Two memories.


## Give every commit memory.


## Built in the open


Oobo is open source. Join contributors earning points, climbing tiers, and shaping the future of AI code clarity.