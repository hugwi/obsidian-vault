---
title: "“I built Claude Code. Use Subagents.” (HACKS)"
source: "youtube"
url: "https://www.youtube.com/watch?v=Nn0OyCWer1k"
author: "Charlie Automates"
published: "2026-02-02"
created: "2026-08-24"
duration: "0:01:51"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "context-engineering"
summary: "If you are using Claude code and you're not intentionally using sub agents, you're leaving about 99% of its power on the table. Claude code will naturally use sub agents as you ask it to do things. However, learning how to use them intentionally in your workflows is going to make you a better Claude code operator in general."
---

# “I built Claude Code. Use Subagents.” (HACKS)

![“I built Claude Code. Use Subagents.” (HACKS)](https://www.youtube.com/embed/Nn0OyCWer1k)

## Description

*No description.*

## Transcript

If you are using Claude code and you're not intentionally using sub agents, you're leaving about 99% of its power on the table. And here's why. Claude code will naturally use sub agents as you ask it to do things. However, learning how to use them intentionally in your workflows is going to make you a better Claude code operator in general. When you open up a main Claude session asking it to do things mid workflow is just going to waste context. So, the best thing to do is to ask it to open up sub agents to do individual tasks to keep context clean in the main session window so we can feed those results back to the main session. Now, of course, there are different types of sub agents that you can use. And if you guys have seen any of my other content, I talk about the claude.md file and I've trained mine to use sub agents in a very specific way. So, whenever I ask something a little complex, it'll go ahead and ask me if I want to open up multiple sub agents in parallel to the main window session. And there's two ways to really operate with sub agents. Parallel spawning, which one session will send out multiple agents and give you all the results at the same time. And then you have sequential spawning, which will operate one, send back data, use the second one to iterate off of that data, and then go on to the third and so on and so forth to give you the ultimate data back to you. So, as you can see in my claude.md file, I've mentioned how I'd like to use sub agents. And there are some data here about sequential versus parallel sub agents. And based off of my preferences, it's going to suggest parallel versus sequential based off of certain questions that I'm asking. And it has an execution strategy that I installed. And this is something that Boris Cherney, who's the creator of Claude code, recommends doing. And he lays out different strategies. So, if you'd like to learn more about how to use sub agents and customize your claude.md file, comment AI agent below and I'll send you some resources. Take care.
