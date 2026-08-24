---
title: "From 28% to 54% — how Shepherd saves broken agent runs #aiagents #opensource"
source: youtube
url: https://www.youtube.com/watch?v=gA2xz5uQm-4
author: "DIY Smart Code"
published: 2026-07-05
created: 2026-08-24
duration: "0:02:38"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# From 28% to 54% — how Shepherd saves broken agent runs #aiagents #opensource

![From 28% to 54% — how Shepherd saves broken agent runs #aiagents #opensource](https://www.youtube.com/embed/gA2xz5uQm-4)

## Description

Shepherd is Git for coding agents — Stanford researchers built agent-native version control that checkpoints an agent's live state, not just files. When your AI coding agent breaks at step 10, fork the run and revert instead of restarting. Here's how it works, in 3 minutes.

----
🚀 DYNAMOUS AI COMMUNITY

Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount

⚡ HOSTINGER — RELIABLE HOSTING FOR YOUR PROJECTS (10% OFF)

Whether you're shipping a portfolio, a side project, n8n flows, or AI agents — I use Hostinger for fast, affordable VPS + web hosting.

Get 10% off here 👉 https://hostinger.com/DIYSMARTCODE

(Affiliate link — costs you nothing, supports the channel.)
----

What you will see in this 3-minute Shepherd breakdown:
- Why a long agent run builds real state — files, a dev server, a database, packages, the KV cache — that plain Git can't version
- The two bad options today when an agent derails: let it flail and burn tokens, or restart from step 1 and pay for every call again
- How Shepherd records each agent action as a typed event and commits the process + filesystem together, copy-on-write
- The speed: forking a run is ~5x faster than a docker commit, with over 95% KV-cache reuse on replay
- The meta-agent — a supervisor that watches the trace and reverts a bad step before it commits, in plain Python (fork, replay, revert)
- The honest limit: files and sandbox changes roll back cleanly, but database writes, sent emails, and real charges can't be undone
- The receipt: on CooperBench, an active supervisor took the pass rate from 28.8% to 54.7%

Shepherd (open source, MIT): https://github.com/shepherd-agents/shepherd

Would you let an automated supervisor auto-revert your agent's mistakes? Or hands off? Drop your pick below.

#Shepherd #AICodingAgent #AIAgents #VibeCoding #Git #VersionControl #CodingWithAI #AgenticAI #AIAutomationTools #AIProductivityTools #Stanford #AgentCheckpointing #CopyOnWrite #KVCache #CooperBench #DevTools #CodingShorts #ProgrammingShorts #DIYSmartCode #SoftwareEngineering #BuildAIAgents #AgentMemory #LLM #OpenSource

## Transcript

Stanford just built Git for coding agents. It fixes the most expensive problem in agent coding. Your agent runs 10 steps, then makes one bad edit. Watch what happens next. A long agent run builds up real estate. Files, a dev server, a database, installed packages, even the KV cache. Say it gets a traceback wrong at step 10 and rewrites a file that was fine. Everything through step eight was correct. But now the test failed and the whole run goes off track. So, what do you do? Option one, let it flail. It burns more tokens fixing its own mess. Option two, restart from step one. You pay for every model call again and the run is random, so it never reproduces the same path anyway. Why not just jump back to step eight? Because the trajectory is only a message log. It records what the agent said and which tools it called, not the state underneath. Memory, open file handles, child processes, the temp folder, the the KV cache. None of that is in the log. Git can version your files. It cannot snapshot a running process or a cold cache. Shepherd is a runtime layer that records the run as typed events. Each agent action becomes a commit, just like Git. But the commit captures the process and the file system together, copy on write. So, a branch carries the actual running state, not just the files. Going back is now a single call. It forks from that commit and resumes from the exact state. The fork is five times faster than a Docker commit. And because the prefix is unchanged, over 95% of the KV cache is reused on replay. The early steps are never reprocessed. Once you can fork, a meta agent can sit on top. It watches the trace and reverts the moment things look wrong. Before the bad write is even committed and this is not some heavy control plane. In practice, it is just Python calling fork, replay, and revert. But not everything undoes itself. Files in sandbox change roll back cleanly. A database right needs an undo step set up in advance, and a sent email or a real charge can never be reversed. The supervisor has to catch those before they fire. Does it actually work? On Cooper bench, two agents share one code base. Adding an active supervisor took the pass rate from 28.8% to 54.7%. It is early and labeled alpha. But the repo is open and MIT licensed. So here is the real question. Would you let an automated supervisor auto revert your agent's mistakes or hands off? Drop your pick below.
