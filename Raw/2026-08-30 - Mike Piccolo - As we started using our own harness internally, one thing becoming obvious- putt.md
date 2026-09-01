---
title: "As we started using our own harness internally, one thing becoming obvious: putting multiple coding agents in tabs is not multi-agent orchestration."
source: "x"
url: "https://x.com/mfpiccolo/status/2094003705418789237"
author: "Mike Piccolo"
published: "Sun Aug 30 10:06:02 +0000 2026"
created: "2026-08-30"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating: ""
tags:
  - "clip/x"
  - "multi-agent"
  - "orchestration"
  - "agents"
  - "harness"
summary: "As we started using our own harness internally, one thing becoming obvious: putting multiple coding agents in tabs is not multi-agent orchestration. In our harness, Pi, Claude Code, Codex and even VS Code are workers on the same engine."
theme: "multi-agent-orchestration"
subtheme:
  - "coordinator-patterns"
  - "parallel-fan-out"
domain: "agentic-engineering"
---

# As we started using our own harness internally, one thing becoming obvious: putting multiple coding agents in tabs is not multi-agent orchestration.

> Saved from X on 2026-08-30. Author: Mike Piccolo.

As we started using our own harness internally, one thing becoming obvious: putting multiple coding agents in tabs is not multi-agent orchestration.

In our harness, Pi, Claude Code, Codex and even VS Code are workers on the same engine.

A trigger can wake Pi, give it the workspace, let it do its part, then have its output or an event trigger Claude Code or Codex to continue the work.

The interesting part is not that you can run every coding agent. It is that the harness can orchestrate them.

Multi-agent should mean agents can trigger, call and hand work to each other.

Not a nicer tab multiplexer.
