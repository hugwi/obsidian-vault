---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - memory
source: readwise
created: 2026-06-23
rating: 
action: 
theme: context-engineering
subtheme:
  - memory-persistence
---

# I built Claude's Dreams feature myself using Mem0 and Codex, and it changed how I code

![rw-book-cover](https://static0.xdaimages.com/wordpress/wp-content/uploads/2026/04/claude-code.avif?w=1600&h=900&fit=crop)

## Metadata
- Author: [[Anurag Singh]]
- Full Title: I built Claude's Dreams feature myself using Mem0 and Codex, and it changed how I code
- Category: #articles
- Summary: Anthropic created a feature called Claude Dreams that helps AI agents learn from past conversations by reviewing and improving their memories. Since access was limited, the author built a similar system using Mem0 and Codex to give their agent long-term memory and reflection abilities. This approach separates raw memories, summaries, and insights to keep the memory useful and helps the AI improve over time.
- URL: https://www.xda-developers.com/built-claude-dreams-feature-mem0-codex-changed-code/

## Full Document
![Claude code running QWEN](https://static0.xdaimages.com/wordpress/wp-content/uploads/2026/04/claude-code.avif?&fit=crop&w=1600&h=900)
Anthropic recently [announced one of the most interesting AI features](https://www.xda-developers.com/claudes-leaked-dreaming-feature-is-now-live-and-it-lets-agents-learn-from-their-own-mistakes/) I've seen in a long time – Dreaming. When the agent is idle, this feature allows it to revisit past conversations, memories, and completed tasks, then reflect on them to improve its memory and future behavior. It can identify patterns, merge duplicate information, surface useful insights, and learn from previous mistakes. The next time it encounters a similar task, it can use those insights instead of repeating the same errors. That addresses one of the biggest challenges in agentic workflows today that is maintaining useful long-term memory without accumulating noise.

Unfortunately, the feature is currently available only as a research preview. Anthropic has not announced a public release timeline, and access is limited to select researchers and organizations building agentic systems. If you want to try it, you need to apply and be accepted into the program.

Since I couldn't get access, I decided to build something similar for my own workflow using Mem0 as the [memory layer](https://www.xda-developers.com/added-these-mcp-servers-local-llm-stack-one-replaces-paid-tool/) and [Codex](https://www.xda-developers.com/use-claude-code-and-codex-together-combination-does-something-neither-can-do-alone/) as the agent. I won't claim it's identical to Claude Dreaming, but it’s built around the same core idea, and it gets the job done.

####  Claude Dreams could be a game changer

#####  It solves one of the biggest problems of AI agents

   ![Claude Code on Mac](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/screenshot-2026-05-30-at-8-36-27-pm.png?q=49&fit=crop&w=825&dpr=2) 
Claude Dreams solves the problem of AI agents being stateless. Once a conversation ends, the agent may have access to stored memories, but it doesn't automatically reflect on what happened, learn from mistakes, or improve the quality of those memories over time. Claude Dreams aims to change that by introducing a background process that reviews past conversations and reorganizes what the agent knows.

Anthropic says the idea is inspired by how humans consolidate memories during sleep. Instead of simply storing everything forever, Claude periodically revisits old sessions, looks for patterns, identifies recurring mistakes, and extracts useful insights. The company calls these background jobs "dreams."

A dream takes two main inputs – the agent's existing memory store and up to 100 previous session transcripts. The process runs asynchronously in the background and can take several minutes depending on how much data needs to be analyzed. During that time, Claude looks for things like user preferences, successful workflows, repeated errors, and other patterns that could help it perform better in future sessions.

One of the most interesting aspects of the system is it also cleans the memory up. Duplicate information gets merged, contradictions are resolved, and vague references such as "last week" or "yesterday" can be converted into absolute dates. Anthropic describes this as a way to prevent memory rot, where a growing memory store becomes noisy and less useful over time.

####  Building my own Claude Dreams

#####  You need Codex, Mem0, and a Python script

I started with Codex for the agent loop and Mem0 for memory. Mem0 integrates directly with Codex through MCP, allowing the agent to search previous memories, retrieve relevant context, and store new information as it works. This gives the agent persistent memory across sessions instead of forcing it to start from scratch every time.

Getting that part working was relatively straightforward, but it only solved half the problem. The bigger challenge was helping the agent distinguish between useful information, outdated information, and noise. That's where Claude Dreams becomes interesting. Anthropic isn't just giving agents memory. It's giving them a way to periodically review and improve that memory.

To get closer, I added a separate reflection layer using a simple Python script. At regular intervals, the script pulls memories and previous session data from Mem0 and feeds them into another model for analysis. This model reviews past interactions and looks for recurring patterns, repeated mistakes, successful workflows, and long-term preferences. The output is then written back into Mem0 as a new set of higher-level memories. The system gradually builds a more distilled knowledge base that future sessions can draw from.

Mem0’s search layer is built for natural-language retrieval with filters, reranking, and thresholds, and its get\_memories API supports paginated retrieval with logical filters like AND, OR, and NOT. In practice, that means you can scope memories by user, project, category, or time instead of dumping everything into one pile. For a setup like this, that is the difference between useful context and a mess.

####  Adding a reflection layer

#####  The real trick is separating memory into layers

   ![Mem0 refraction layer in VS Code](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/06/screenshot-2026-06-03-at-2-22-05-am.png?q=49&fit=crop&w=825&dpr=2) 
The reflection layer runs independently of the main agent. At regular intervals, the script pulls memories and recent session data from Mem0 and sends them to another model for analysis. Instead of solving a user task, this model reviews the agent's own history and looks for recurring patterns, repeated mistakes, successful workflows, contradictions, and long-term preferences.

#####  Subscribe for practical agent-memory playbooks

Level up your agent builds by subscribing to the newsletter for deep dives, annotated code patterns, and practical architecture tips that focus on reflection layers, memory cleanup, and building Claude-like dreaming into your systems.

 Get Updates

By subscribing, you agree to receive newsletter and marketing emails, and accept our [Terms of Use](https://www.valnetinc.com/en/terms-of-use) and [Privacy Policy](https://www.valnetinc.com/en/privacy-policy). You can unsubscribe anytime.

The real trick is separating memory into layers. I would keep raw memories, session summaries, and synthesized insights in different buckets. Raw memories are the source material. Session summaries capture what happened. Synthesized insights are the higher-level stuff the reflection worker produces after it notices the same pattern showing up again and again. That separation is what stops the store from becoming a giant unreadable log.

For the batch job, do not treat get\_all() like a blind export. Mem0’s current docs require filters for get\_all(), which is useful here because it forces you to scope the reflection run by user, agent, app, or run. That makes the dream pass easier to control and easier to inspect later.

Keeping the reflection process separate from the agent also makes the system easier to reason about. Codex focuses on completing tasks, while the reflection worker focuses on improving the quality of the memory store. The result is an agent that doesn't just remember previous interactions, but can also learn from them over time.

#####  You can build so many features

Coding agents and AI tools have reached a point where almost anyone can build the features they want into their setup. And if building things from scratch isn't your thing, there are plenty of [mods for tools like Claude Code](https://www.xda-developers.com/connected-claude-terminal-does-things-script-hand/) that can help you take it to the next level.
