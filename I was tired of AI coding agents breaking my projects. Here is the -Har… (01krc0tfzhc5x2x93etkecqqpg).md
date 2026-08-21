---
categories:
  - "[[Resources]]"
domain: engineering
title: "I was tired of AI coding agents breaking my projects. Here is the \"Harness"
source: "https://www.reddit.com/r/PromptEngineering/comments/1s7od3u/i_was_tired_of_ai_coding_agents_breaking_my/"
author: "Exact_Pen_8973"
published: 2026-03-30
created: 2026-05-11
description: "If you're using AI agents (Cursor, Claude Code, GitHub Copilot Workspaces)"
tags:
  - to-process
  - harness-engineering
---

**[r/PromptEngineering](https://www.reddit.com/r/PromptEngineering/)**


# [Exact\_Pen\_8973](https://www.reddit.com/user/Exact_Pen_8973/)



 (2026-03-30 11:52:16)


If you're using AI agents (Cursor, Claude Code, GitHub Copilot Workspaces) to build your side projects, you've probably hit "the wall." The AI is amazing for the first 80%, but once the codebase gets complex, it starts chasing its own tail, breaking old features, and losing context.


I spent some time researching how massive companies like Stripe manage to let AI autonomously merge 1,300 PRs a week without taking down their payment systems. The secret isn't a better model. It's a system called **Harness Engineering**.


A harness is the environment, constraints, and verification loops you build *around* the AI.


Here is the exact folder structure you should drop into your side project today to keep your AI agents on track:


* [`CLAUDE.md`](http://CLAUDE.md) (or `.cursorrules`): Your root instruction file. Project overview, tech stack, and non-negotiable rules.
* `.claude/rules/`: Top-level governance. Put your security policies and strict coding conventions here.
* `.claude/skills/`: Repeatable task patterns (e.g., exactly how you want your database migrations run).
* `docs/progress.md`: **This is the game-changer.** Have your agent read this at the start of a session and update it at the end. It acts as a "handoff" so the AI never loses its train of thought between sessions.


Instead of writing a giant prompt every time, you build this harness. When the AI makes a mistake, you don't just fix the code—you update a rule in the harness. The system gets more reliable every single day.


I put together a full, practical guide on how to set this up, including case studies from Anthropic and OpenAI.


Read the full breakdown here: [Harness Engineering: The Discipline That Makes AI Agents Actually Reliable](https://mindwiredai.com/2026/03/30/harness-engineering-guide-reliable-ai-agents/)


Are you guys using any specific rules or architectures to keep your AI agents from hallucinating in your side projects? Let's discuss.





## [Substantial-Cost-429](https://www.reddit.com/user/Substantial-Cost-429/)



 (2026-03-30 16:33:38)


Harness engineering is basically what I ended up doing too. The secret sauce isn’t a bigger model but a harness that matches your repo. Generic folder structures and rules are a starting point, but every project is different. I turned my harness work into a CLI called Caliber that walks your repo, suggests the right skills, config and MCP stuff, and lets you run Claude locally with your own keys under an MIT licence. Repo has around 250 stars if you want to check it out: <https://github.com/rely-ai-org/caliber>





## [Senior\_Hamster\_58](https://www.reddit.com/user/Senior_Hamster_58/)



 (2026-03-30 14:42:01)


Single prompt fixes are how people get a false sense of control. A docs/progress.md handoff plus hard rules is the part that survives when the agent decides to remix your repo at 2am. I've seen this movie: the harness matters more than the model right up until someone starts calling it magic again.