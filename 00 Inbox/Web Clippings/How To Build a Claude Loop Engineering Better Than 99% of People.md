---
title: "How To Build a Claude Loop Engineering Better Than 99% of People"
source: "https://freedium-mirror.cfd/https://medium.com/@GaoDalie_AI/how-to-build-a-claude-loop-engineering-better-than-99-of-people-3ab8701d176c"
author:
published: 2026-06-02
created: 2026-06-15
description: "I’m no longer prompting Claude. I’m just running a loop that prompts him and then thinks about what to do next. My job is to write loops."
tags:
  - "to-process"
---
![Post cover image](https://freedium-mirror.cfd/img/700/1*z-VXxpR7mPlT_NbvCtnDnA.png)

I’m no longer prompting Claude. I’m just running a loop that prompts him and then thinks about what to do next. My job is to write loops.

![](https://freedium-mirror.cfd/img/700/1*drBiQzO68eWvJ_Mot-m1oQ.png)

Gao Dalie (高達烈)

In 2024, the key to success was "writing good prompts." 2025 was the era of running multiple AI agents in parallel. And in June 2026, another evolution will occur in how we interact with AI.

Recently, the term "loop" has become quite a hot topic in the AI community.

The whole thing started with a post by Peter, the creator of OpenClaw.

![None](https://freedium-mirror.cfd/img/4000/1*AMcDZWid_HfxetUQ5DeLKQ.png)

In the world of AI agents, the term Loop Engineering is suddenly gaining attention.

Humans would enter prompts each time, read the results, and then enter the next prompt. In most cases of AI utilization up until now, humans were trapped in a loop.

AI was the worker. Humans were the directors, supervisors, and inspectors.

This is where Loop Engineering reversed the situation.

Instead of a human having to enter prompts each time, the task is assigned to the AI, executed, the results are reviewed, and if it's not finished yet, it's executed again. This entire iterative process is designed as a system.

In other words, humans will shift from being "people who type prompts" to "people who create systems for typing prompts."

### Before we start! 🦸🏻♀️

If you like this topic and you want to support me:

1. **Clap** my article 50 times; that will really help me out.👏
2. [Follow](https://medium.com/@mr.tarik098) me on Medium and subscribe to get my latest article for Free🫶
3. Join the family — Subscribe to the [YouTube channel](https://www.youtube.com/channel/UC6P5WCWjqhhXVFBqbJHNxyw)

### What is a loop?

For the past two years, we've been prompting our agents for one task at a time. That assumption is now changing.

Instead of simply instructing someone to "create a landing page" and then personally overseeing every subsequent step, **design a self-sustaining loop of discovery, planning, execution, verification, and improvement**. Repeat this loop until the goal is reached.

Loops are something you design yourself. They can be implemented in most agent harnesses. The question isn't "what to use," but "how to wire it."

### Single agent loop

The simplest form is a single agent looping through itself.

You don't need to click prompts at each step. The agent handles the cycle. It's like a human rewriting a draft multiple times.

### Fleet loop (multiple agents)

In larger configurations, a swarm of agents runs in a loop.

The goal is passed to the orchestrator agent. The orchestrator breaks down the goal into pieces and passes each piece to a specialist agent. The specialist then passes on even more detailed jobs to sub-agents.

This entire tree structure represents a continuous cycle of "discovery → planning → execution → verification" until the goal is achieved.

If a single-loop is "a person who rewrites the draft alone," then a fleet-loop is "an organization that runs a project end-to-end as a team."

### Open-loop and closed-loop

There are two types of loops. Understanding this difference is crucial for success in practical applications.

### Open-loop: Exploratory

While there are conditions and goals, it gives the agent a wide exploratory space. It can try and discover multiple paths, and create something that wasn't fully speculated out initially.

This is a promising area. Creative results are likely to emerge here.

However, **cost becomes an issue**. A truly open-loop system that allows free exploration consumes a massive amount of tokens. For the 90% of people who don't have unlimited budgets, it's not realistic at this point. Furthermore, if applied to projects with loose criteria, it simply becomes a slop machine.

### Closed-loop: Constraining

Humans pre-design the end-to-end passes.

The agent runs in a loop, but within a human-made framework. Each run passes on the learning to the next run, so accuracy improves with each execution. Because the paths are limited, it runs on a normal budget.

**This is almost entirely what's producing results in today's work.**

The division of roles in a closed-loop system can be simplified.

Open-loop is "exploration," closed-loop is "execution." The latter is designed first, and the former is released when the budget and accuracy are in place. That's the realistic order these days.

### "loop" built into the tool

This concept of "repeating the same task" has now been incorporated as a formal feature of coding agents. Taking Claude Code as an example, several commands have been added.

- `/loop`: Repeats the prompt or command at regular intervals
- `/goal`: Defines a completion condition and continues working over multiple turns until that condition is met (added in version 2.1.139 on May 11, 2026)
- Dynamic Workflows: The AI itself writes the work procedure and divides it into dozens to hundreds of sub-agents to carry it out in parallel (added in version 2.1.154 on May 28, 2026. Called using the keyword `ultracode`).

What they all have in common is that they reduce the back-and-forth process of a person giving instructions, checking the results, and then giving further instructions. If you provide the conditions and procedures in advance, the AI will handle the rest on its own.

### The Foundation of the Agent Loop — ReAct and Reflexion

Loop engineering isn't a concept that just fell out of nowhere. It's based on two important patterns that emerged from research.

### ReAct (Reason + Act)

This pattern, which originated from a joint research project between Princeton University and Google, is an architecture **that alternates between reasoning and action**.

In the context of coding:

1. Understanding the goal
2. Write code
3. Run the code and observe the output (or error).
4. Infer what went wrong.
5. Correct and rerun
6. **Repeat until the test passes.**

### Reflexion

This is an advanced version of ReAct, a pattern **where failures are verbalized and used to inform future attempts**.

In loop engineering, this concept of Reflexion is implemented as **external memory (SKILL.md and progress.txt).**

### 5\. Inner Loop vs. Outer Loop

A loop has **two layers**. Understanding this distinction is the core of loop engineering.

### Inner loop (validation loop within a single task)

Within a single task, **the agent validates their work before responding**.

> **Key point**: Both use the exact same tool loop infrastructure. The difference is **whether the model "chose" to call the validation tool**.

### Outer loop (cross-session learning loop)

**This is a cycle where agents learn from past experiences** across multiple sessions.

Comparison items Inner loop Outer loop **scope** Within a single taskCross-session **the purpose** Improving task reliabilityImprovement over time **Maintaining the state** Within the context windowPersistent files (AGENTS.md, SKILL.md, etc.) **Current maturity** Many agents **Still under development**

**Loop engineering encompasses both of these aspects in its design.**

### The "5+1" components that make up the loop

Addy Osmani summarized that a working loop consists of **five components + memory.**

### big picture

### Details of each part

#### 1- Automated execution

The heart of the loop. It's the mechanism **that periodically discovers tasks and activates agents**.

#### 2- Worktrees

When multiple agents work on the same repository simultaneously, it provides independent workspaces to **prevent conflicts in file changes between them.**

#### 3- Skills

Rules and procedures such as "This is how you write things in this project." This avoids having **to explain everything from scratch every time.**

#### 4- Plugins / Connectors

This is a mechanism for **connecting AI with existing tools** such as GitHub, Jira, Slack, and databases.

#### Sub-agents

**This pattern separates the roles of "creator" and "verifier**." It's inspired by the concept of GANs (Generative Adversarial Networks).

> *This three-agent cycle is adopted by Anthropic and achieves a level of quality that cannot be attained with a single agent.*

#### Memory

The lifeline of the loop. By **persisting state outside of the conversation**, it transcends the limitations of the context window.

> ***"The agent forgets, the repository doesn't."*** \_ — Addy Osmani\_

### Example of an end-to-end loop design

#### Practical example: Daily issue triage + automatic correction loop

### Loop flow

#### Finally: This is not just about AI development.

If I were to summarize its essence in one word,

> **Instead of giving freedom to highly capable individuals, the goal is to design an environment where they can achieve results.**

The same applies to human teams. Simply hiring talented people isn't enough; context, rules, feedback, evaluation criteria, and progress management are also necessary.

Management in the age of AI is moving away from giving detailed instructions **to designing good constraints.**

Design loops, not prompts.

🧙♂️ I am an AI Generative expert! If you want to collaborate on a project, drop an [inquiry here](https://docs.google.com/forms/d/e/1FAIpQLSelxGSNOdTXULOG0HbhM21lIW_mTgq7NsDbUTbx4qw-xLEkMQ/viewform) or book a [1-on-1 Consulting](https://calendly.com/gao-dalie/ai-consulting-call) Call With Me.

[**How To Build a Claude Routines Better Than 99% of People**](https://medium.com/data-science-collective/how-to-build-a-claude-routines-better-than-99-of-people-6a7739680d29) *I wake up in the morning and check my unread Slack messages. I open my emails and pick out only the important ones. I…*

[**How To Build a Claude Dynamic Workflows Better Than 99% of People**](https://medium.com/data-science-collective/how-to-build-a-claude-dynamic-workflows-better-than-99-of-people-552b9c4cd09b) *On June 2, 2026, Anthropic announced "dynamic workflows" for Claude Code. This feature allows Claude Code to write…*

[**How to build a Claude Code/goal Better than 99% of People**](https://medium.com/data-science-collective/how-to-build-a-claude-code-goal-better-than-99-of-people-5a4490095cf4) *On May 13, 2026, Anthropic's official account @ClaudeDevs announced a new command for Claude Code: "Claude Code /goal"!*