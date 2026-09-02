---
title: "A weird experiment I've been trying the last few weeks is having Claude take over day-to-day maintenance of our apps. Seeing early signs of life that this might be possible."
source: "x"
url: "https://x.com/bcherny/status/2088014489438621990"
author: "Boris Cherny"
published: "Thu Aug 13 21:27:02 +0000 2026"
created: "2026-08-13"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating: ""
tags:
  - "clip/x"
  - "claude"
  - "pr-automation"
  - "code-optimization"
  - "crash-fuzzing"
summary: "A weird experiment I've been trying the last few weeks is having Claude take over day-to-day maintenance of our apps. Seeing early signs of life that this might be possible."
theme:
  - "multi-agent-orchestration"
  - "work-breakdown-specs"
subtheme:
  - "pr-automation"
  - "code-optimization"
  - "crash-fuzzing"
domain: "agentic-engineering"
---

# A weird experiment I've been trying the last few weeks is having Claude take over day-to-day maintenance of our apps. Seeing early signs of life that this might be possible.

> Saved from X on 2026-08-13. Author: Boris Cherny.

A weird experiment I've been trying the last few weeks is having Claude take over day-to-day maintenance of our apps. Seeing early signs of life that this might be possible.

The setup is straightforward: we have a Slack channel called proj-claude-maintains-apps. In it, Claude Tag runs a bunch of daily routines across iOS, Android, Desktop, web, CLI, and Agent SDK:

- Crash fuzzer: open the app in a simulator and tap around to find ways to crash it, then root cause and fix the crashes
- Dup unifier: scans the codebase for similar-yet-slightly-divergent abstractions, and puts up PRs to unify them
- Dead-code remover: removes statically unreachable code, and adds logging to suspected dead code to check if it's really dead and if so, remove it the next day
- Abstraction police: fixes leaky abstractions
- a bunch more..

Results have been surprisingly positive. Over the last few weeks, these routines have opened 388 PRs across our repos, 180 of which we merged after Claude Code Review + human review. We're now thinking about how to streamline this to make merging these kinds of mechanical changes easier.

Claude generally gets these PRs right on the first shot, and if it doesn't, we ask Claude to tune its routines so it's better the next day. Sometimes it takes a few days of tuning. 

To try a similar workflow, ask Claude Code or Tag, or create some routines directly at https://t.co/Z70hStEBH6. A few of the actual prompts I used below.

Has anyone experimented with similar workflows?
