---
title: "The winner of an Anthropic hackathon open sourced his entire Claude Code setup. 68 subagents, 286 skills, 94 commands, MIT license"
source: "x"
url: "https://x.com/undefinedKi/status/2094088284443992514"
author: "Yarchi"
published: "Sun Aug 30 15:42:07 +0000 2026"
created: "2026-08-30"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating: ""
tags:
  - "clip/x"
  - "context-engineering"
  - "agents"
  - "claude-code"
  - "comprehension"
summary: "The winner of an Anthropic hackathon open sourced his entire Claude Code setup. 68 subagents, 286 skills, 94 commands, MIT license

ECC turns Claude Code from one assistant into a full engineering team."
theme: "context-engineering"
subtheme:
  - "compaction-caching"
  - "comprehension-debt"
domain: "agentic-engineering"
---

# The winner of an Anthropic hackathon open sourced his entire Claude Code setup. 68 subagents, 286 skills, 94 commands, MIT license

> Saved from X on 2026-08-30. Author: Yarchi.

The winner of an Anthropic hackathon open sourced his entire Claude Code setup. 68 subagents, 286 skills, 94 commands, MIT license

ECC turns Claude Code from one assistant into a full engineering team. It plans before it builds, writes the failing test first, then reviews its own work from a fresh context.

The agents, by job:

Planning. Turns a one-line request into a blueprint you approve before any code exists.

Review. Reads your diff in a clean context, with separate reviewers for Go, Python, TypeScript, Rust, Java and more.

Build repair. One resolver per toolchain, down to PyTorch and CUDA errors.

Security. An OWASP pass on your code, plus a scanner that audits your own agent config for injection risks.

Architecture. System design calls before they turn into migrations.

Domain work. Database queries, ML pipelines, end-to-end tests, docs.

The skills, by category:

Testing. tdd-workflow gates you from red to green, with eval-harness and verification-loop sitting on top of it.

Language packs. Idioms, testing and security for Python, Go, Rust, C++, Django, Laravel, Spring Boot, Next.js.

Context. search-first makes it read the docs before writing, iterative-retrieval keeps subagents from dragging your whole repo into the window.

Shipping. Docker, CI/CD, health checks, rollbacks, and migration patterns for Prisma, Drizzle and Django.

Work that is not code. Writing in your voice, market research with sources, pitch decks, slide decks.

Start with one plan and one rules pack. Installing all 286 skills at once is the fastest way to make it worse.
