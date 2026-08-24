---
title: "Microsoft Just Open-Sourced a Cheat Code for AI Agents (SkillOpt) #microsoft #ai #aiagents"
source: "youtube"
url: "https://www.youtube.com/watch?v=jjze-8Wia38"
author: "Better Stack"
published: "2026-07-05"
created: "2026-08-24"
duration: "0:02:40"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "evaluation"
  - "hardware"
  - "harness-engineering"
  - "microsoft"
  - "skills"
summary: "Microsoft Research just open-sourced a tool called Skill Opt that makes AI agents measurably smarter, and it does this without retraining the model or fine-tuning weights or even touching the prompt by hand. What they trained instead was a markdown file. Right now, if you want an AI agent to perform better on a task, you basically got two options."
---

# Microsoft Just Open-Sourced a Cheat Code for AI Agents (SkillOpt) #microsoft #ai #aiagents

![Microsoft Just Open-Sourced a Cheat Code for AI Agents (SkillOpt) #microsoft #ai #aiagents](https://www.youtube.com/embed/jjze-8Wia38)

## Description

SkillOpt: https://microsoft.github.io/SkillOpt
Github Repo: https://github.com/microsoft/SkillOpt

## Transcript

Microsoft Research just open-sourced a tool called Skill Opt that makes AI agents measurably smarter, and it does this without retraining the model or fine-tuning weights or even touching the prompt by hand. What they trained instead was a markdown file. Let me explain. So, here's what's happening. Right now, if you want an AI agent to perform better on a task, you basically got two options. So, option one, fine-tune the model, but that is expensive and requires access to the weights and locks you into one model. Option two is to handwrite a better prompt, but that could be brittle, manual, and you're mostly guessing at that point. But, Skill Opt proposes a third path. Treat the agent's skill document as the thing you actually train. And the way it does this looks almost exactly like a machine learning training loop. The agent runs a batch of tasks with its current skill file and records everything, every message, every tool call, every final score. And that's called a rollout. Then, a separate optimizer model reads through the wins and the failures and looks for reusable patterns it can turn into concrete rules. And that is called the reflection step. And from there, the optimizer proposes edits to the skill file, so it can add a rule, it can delete a rule, replace one under a strict edit budget. And that budget acts like a learning rate, but for text. It stops the optimizer from overriding rules that already work, but leaves room for improvement for new ones. But, here's what makes the whole thing actually hold together. No edit gets accepted just because an optimizer likes it. Every candidate has to beat a held-out validation set before it becomes the new skill. And rejected edits get stored in a buffer. So, the optimizer remembers what didn't work and stops going in the same bad direction twice. So, does it actually work? Well, across seven target models, six benchmarks, and two execution harnesses, Codex and Claude Code, Skill Opt landed best or tied best in all 52 settings they tested, every single one of them. And what's really interesting is that the final skill file is portable. So, in this particular example they did, they took the best skill.md file trained inside Codex and dropped it straight into Claude Code with no extra training and it still worked and picked up a 31.8 point gain on spreadsheet tasks. They also took a skill trained on a larger model and handed it to a smaller one and that gained a 15 point boost without any retraining. So that proves that this skill isn't capturing quirks of a specific model. It's capturing how to actually solve the task. So for years we've treated prompts as disposable text you tweak by hand until something works, but skill opt treats them as trainable artifacts and gets results that compete with fine-tuning without ever spinning up a GPU. So I think that's genuinely a very clever solution solved in a very efficient way. I'll put the links to the GitHub repo in the description below. If you want to stay up to date with the latest open source tools and frameworks, be sure to subscribe to the Better Stack channel.
