---
title: "He live-coded a feature for 90 minutes in front of a packed room and never read the plan the AI wrote for him."
source: "x"
url: "https://x.com/ZaneOnAI/status/2092349378543444241"
author: "Zane"
published: "Tue Aug 25 20:32:20 +0000 2026"
created: "2026-08-25"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating: ""
tags:
  - "clip/x"
  - "agentic-ai"
  - "real-time-interrogation"
  - "vertical-slicing"
  - "dependency-graphs"
  - "qa-taste"
summary: "He live-coded a feature for 90 minutes in front of a packed room and never read the plan the AI wrote for him. Not skimmed."
theme:
  - "comprehension-maintainability"
  - "workflow-phases-gates"
  - "productivity-measurement"
  - "human-ux-frontend"
subtheme:
  - "real-time-interrogation"
  - "vertical-slicing"
  - "dependency-graphs"
domain: "agentic-engineering"
---

# He live-coded a feature for 90 minutes in front of a packed room and never read the plan the AI wrote for him.

> Saved from X on 2026-08-25. Author: Zane.

He live-coded a feature for 90 minutes in front of a packed room and never read the plan the AI wrote for him.

Not skimmed. Did not open it.

His reasoning: the alignment already happened in the conversation. Reading the document only tests whether the model can summarize, and models are good at summarizing.

Here is what he does instead.

Get interrogated first. Before any plan, he runs a skill that makes the model interview him one question at a time. It asked 22 in the demo. He says 40 to 100 is normal. The questions surface decisions nobody had made yet - backfill old records or not, do streaks count separately. The client never considered them. Neither had he.

Then freeze it. A doc with problem, user stories, and an explicit out-of-scope section. That last part is where rejected options go so a future agent does not resurrect them.

Cut vertically, not horizontally. Left alone the model builds all the schema, then all the API, then the UI - nothing testable until the third layer. He forces every slice to touch database, service, and something visible. The model proposed a horizontal slice anyway. He pushed back and it corrected.

Split into tasks that declare what blocks them. A numbered plan can only be worked by one agent. A dependency graph can be worked by several.

Then leave. A loop in a container picks the next unblocked task, writes a failing test, implements until it passes, runs the type checker, commits.

Come back and break it. He logs in as a student and hits an error in under a minute. This is the part he says cannot be automated - not because models cannot test, but because QA is where taste re-enters. Automate everything and you get software that runs and is bad.

Underneath all of it: he keeps every task inside roughly the first 100k tokens of a session, whether the window is 200k or a million. His read on the million-token window is that it did not raise the ceiling, it shipped more room below it.

That 100k is his heuristic from practice, not a measurement, and he contradicts the number once himself.
