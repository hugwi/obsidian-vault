---
categories:
  - "[[Resources]]"
domain: engineering
title: "4 Claude Code slash commands I use daily that make me more productive"
source: "https://www.xda-developers.com/claude-code-slash-commands-use-daily-more-productive/"
author: "Shekhar Vaidya"
published: 2026-04-02
created: 2026-04-04
description: "Small commands, massive workflow gains."
tags:
  - to-process
  - agent-tools
---

![Claude code ](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/03/claude-code.jpg?&fit=crop&w=1600&h=900)
I use Claude Code in two very different ways: managing my home lab server and building web apps. Most people treat Claude as a [smart terminal](https://www.xda-developers.com/replaced-putty-with-ssh-client-managing-servers-never-felt-smooth/) and focus only on prompts. In a few instances, treating it like a chatbot means missing built-in controls like slash commands.


The slash commands are one of the most under-used features that Claude Code ships with and can substantially improve workflow efficiency. Slash commands aren’t Easter eggs; they are useful built-in commands that I use daily to be more efficient and productive. If you’re not moving beyond the basic prompts, you are missing out on a layer that fundamentally changes how you interact with it.


Here are a few slash commands that I rely on every day:


##  — /model


###  Switching brains mid-task is more powerful than it sounds


   ![Claude Code CLI showing /model command used to switch between models in terminal](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/04/claude-code-model-command.jpg?q=49&fit=crop&w=825&dpr=2) 
Most Claude users stick to one model for everything, whether it’s brainstorming a complex idea, planning implementation, or handling casual prompts. That usually means the model is either overkill or underpowered for the task. In the Claude app, switching the model forces you into a new session, breaking the flow; the Claude Code CLI handles it differently. It ships with a built-in /model command to switch instantly without breaking the flow.


This is one of my most-used commands when I am deep in development. When starting a new project, I begin with the Haiku model for quick exploration (cheap and fast) and then switch to the Opus model for deeper reasoning (design, algo, and architecture). Once I have a solid plan, I switch to the Sonnet model for [execution and iteration](https://www.xda-developers.com/finally-found-local-llm-want-use-coding/) (balanced and efficient). Sonnet for execution, since Opus has already done the hard thinking. All of this happens with a single command: /model. You can either browse the available models by executing /model or switch directly by name – /model Opus.


This helps me keep my workflow efficient. Token usage matters too, since you are still limited by tokens under a subscription. Larger models like Opus are best suited for brainstorming complex ideas, but they also consume significantly more tokens. Lighter models like Haiku are more efficient for everyday tasks, whereas Sonnet is a good balance between cost and capability. The real benefit of the /model command isn’t switching models; it’s using the right model at the right time.


##  — /mcp


###  This is where Claude stops being just a chatbot


I am a homelab enthusiast and love the hobby; the fun stops when Docker container numbers grow. In my local homelab Debian server, I have 17 containers, each for different services I self-host.


For a simple issue or routine checkup, I had to open Portainer and check each container one by one to diagnose any issues. This is where /mcp comes in. I installed a Docker MCP server inside my homelab, and the /mcp command helps me manage that connection. I can now check which servers are connected, their status, and what tools they expose without leaving the Claude Code interface. The /mcp command not only helps me monitor MCP servers connected to my server locally but also all remote connections tied to my Claude account.


Now, I don’t log into various dashboards like Portainer, Uptime Kuma, [Beszel](https://www.xda-developers.com/this-lightweight-server-monitor-uses-less-ram-than-a-browser-tab/), and Speedtest Tracker just to check status anymore; I ask Claude now. For example, I can ask things like, “What’s running healthy on my server?" or “Do any containers need an update?" The docker-mcp server handles all the queries, and /mcp helps keep the connection managed. Eventually, it stops being a chatbot and starts acting like a neural interface between the server and everything I have connected to it.


##  — /memory and /context


###  Stop repeating yourself every single session


   ![Claude Code CLI displaying /context command with detailed token usage breakdown, including system prompt, tools, memory files, and available context space](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/04/claude-code-context-command.jpg?q=49&fit=crop&w=825&dpr=2) 
Working with LLMs feels like I am repeating myself on every new session. AI assistants like Claude don’t store anything from previous sessions; the project feature in the Claude app keeps a small fragment of context. It also gets pushed out when the conversations grow. Whether I am managing my homelab server or building a web app, I always have to restate the boundaries for the server or workflow instructions for development.


This is where the /memory command helps me by opening and managing my CLAUDE.md file. The file contains my persistent instructions, which Claude reads at the start of every new session. For example, I always keep sensitive containers such as Vaultwarden and the Omada controller either out of context entirely or read-only. The same applies to web development as well: my tech stack preferences, directory conventions, and file nomenclature. This isn’t a hard technical lock but instruction-based enforcement.


The /context command comes in handy when I am using the /memory command. Even with memory, the context can still grow, and sometimes it becomes difficult to manage, especially when I have long sessions. For example, every new session starts with similar sets of instructions, but I also instruct Claude to update the file on every new milestone, and by the end, the context becomes overloaded. What the /context command does is visualize my entire context window and categorize the token usage. It is smart enough to suggest pruning when memory files consume too many tokens. When /context flags the bloat, /compact summarizes the conversation to keep it as context and clears the rest.


##  — /agents


###  When one Claude isn’t enough


   ![Claude Code CLI showing /agents command with multiple subagents](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/04/claude-code-agents-command.jpg?q=49&fit=crop&w=825&dpr=2) 
When working with Claude, there is always a moment when I instruct a multi-step prompt, and I’m stuck waiting for one task to finish before starting the next. Most users use Claude Code in the same pattern, that is, linearly: one prompt, one response, and one task at a time. Managing workflows that require simultaneous tasks gets messy fast. For example, while running a code review, I need to generate an implementation plan for another module. Doing these sequentially takes more time than it should.


###  Subscribe for deeper Claude Code command guides


Get hands-on Claude Code guidance: subscribe to the newsletter for in-depth slash-command tutorials, practical setups, and configuration examples that show how to use /model, /mcp, /memory, /context and /agents to streamline workflows.


 Get Updates


By subscribing, you agree to receive newsletter and marketing emails, and accept our [Terms of Use](https://www.valnetinc.com/en/terms-of-use) and [Privacy Policy](https://www.valnetinc.com/en/privacy-policy). You can unsubscribe anytime.


This is where the /agents command changes the equation completely. The command can spin up a new instance that runs parallel to the previous task without changing the session. These are separate assistants for specific tasks. All these happen in the same running session, which means the agents have all the context of the project. There are two subagents that I use almost every session: code-reviewer and implementation-plan. These are custom subagents that I created via /agents for my development sessions. Both are available across all my projects.


For example, I can use both of them to run simultaneously, invoked with a prompt like: “Use the code-reviewer agent to review my current auth module, and use the implementation-plan agent to draft a plan for the payments module." Both subagents will run in parallel with the same context as the whole project. Though it is extremely useful when used properly, you also need to note that each subagent will consume tokens as per its usage. Multi-agent sessions can exhaust your Pro plan within 15 minutes.


###  Stop prompting and start controlling


Most Claude users focus on prompts, which is also the most limited way to use it. When you stop assuming it is a smarter terminal and start treating it as an environment you control, you change the way you interact with it. Slash commands are one of the examples. None of the commands I mentioned are glamorous; you won't find them in any onboarding guide either. But by using these small built-in commands together, you can reduce a lot of friction from your daily workflow. After involving these in my daily workflow, I stopped thinking about prompts and started thinking about control over my workflow.