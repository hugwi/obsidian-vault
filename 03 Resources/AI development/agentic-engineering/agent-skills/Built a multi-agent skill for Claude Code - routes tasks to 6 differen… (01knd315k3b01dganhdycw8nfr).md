---
title: "Built a multi-agent skill for Claude Code - routes tasks to 6 different AI"
source: "https://www.reddit.com/r/ClaudeAI/comments/1qgxzbb/built_a_multiagent_skill_for_claude_code_routes/?share_id=_Wj3bfzYPqTEn3YCmGd3l&utm_content=2&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1"
author: "Past-Ad-6215"
published: 2026-01-19
created: 2026-04-04
description: "I've been using Claude Code daily and noticed different tasks need different"
tags:
  - to-process
  - agent-skills
---

**[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)**


# [Past-Ad-6215](https://www.reddit.com/user/Past-Ad-6215/)



 (2026-01-19 07:44:00)


I've been using Claude Code daily and noticed different tasks need different strengths - deep reasoning vs fast execution vs specialized knowledge. So I built a skill that orchestrates multiple models.


**What I Built**


**OmO** is a Claude Code skill that acts as an orchestrator. When you run `/omo <task>`, it analyzes what you need and routes to specialized agents:



```
- oracle (Claude Opus 4.5) - Architecture decisions, complex analysis   
- librarian (Claude Sonnet) - External docs/API research   
- explore (Grok) - Codebase search   
- develop (GPT-5.2) - Code implementation   
- frontend-ui-ux-engineer (Gemini 3 Pro) - UI work   
- document-writer (Gemini 3 Flash) - Documentation

```

**How Claude Code Helped**


The orchestrator runs inside Claude Code as a skill. Claude Code's skill system made it possible to:


- Define routing logic in markdown


- Pass structured context between agent calls via `codeagent-wrapper`


- Let Claude decide which agents to invoke based on task signals


The core insight: Claude is great at understanding what kind of task something is, so it can route effectively.


**How Routing Works**


Signal-based, not fixed pipeline:


- Location unclear? → explore first


- External API? → librarian


- Risky change? → oracle for analysis


- Need code? → develop


Key rule: skip agents when not needed. Simple fix = just develop. Complex refactor = explore → oracle → develop.


**Example**


/omo fix undefined error in auth module


→ explore finds the bug location


→ develop implements the fix


→ done


**Free & Open**


The skill is part of my open source Claude Code skills collection. No paid tiers, just markdown files you drop into your skills folder.





## [krullulon](https://www.reddit.com/user/krullulon/)



 (2026-01-19 08:37:42)


This seems more like something you did because you could, not because it’s solving a problem.


There’s no need to use this many different models for these tasks, it’s not bringing anything to the table.





### [Past-Ad-6215](https://www.reddit.com/user/Past-Ad-6215/)



 (2026-01-19 14:00:09)


Let different models do what they excel at.





### [Past-Ad-6215](https://www.reddit.com/user/Past-Ad-6215/)



 (2026-01-19 14:02:00)


If you don't believe it, just watch my orchestration of agents.





## [OkTimeTraveller1337](https://www.reddit.com/user/OkTimeTraveller1337/)



 (2026-01-19 08:22:38)


Ok?





### [Past-Ad-6215](https://www.reddit.com/user/Past-Ad-6215/)



 (2026-01-19 08:26:04)


ya





#### [OkTimeTraveller1337](https://www.reddit.com/user/OkTimeTraveller1337/)



 (2026-01-19 08:55:20)


What are you expecting from the post? There’s no urls to use or see anything