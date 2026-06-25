---
categories:
  - "[[Resources]]"
domain: engineering
title: "Running AI Coding Agents From My Phone (it’s getting out of hand)"
source: "https://itnext.io/running-ai-coding-agents-from-my-phone-its-getting-out-of-hand-7149bcabd82f"
author: "Alexei Ledenev"
published: 2026-03-19
created: 2026-06-03
description: "I should probably start with a disclaimer: I am not a responsible person."
tags:
  - to-process
  - dev-tools
---

I should probably start with a disclaimer: I am not a responsible person. I program in bed. I review code while walking the dog. I once dictated architectural guidance to Claude Code while driving. (Don’t do this. I’m telling you as someone who did it and knows better.)


This is what happens when you build a tool that lets you control AI coding agents from anywhere you have your phone — and your machine is alive somewhere with a tmux session running. You can’t stop. The agents are always there, always ready, and now you’re always reachable.


This is the story of CCGram — how it started, how I use it, and how it quietly ate my free time.


## What Even Is This


CCGram is a Telegram bot that connects to tmux. That’s it. That’s the whole idea.


Claude Code, Codex CLI, Gemini CLI — they’re terminal programs. They print text, they read keystrokes. tmux can capture terminal output and send keystrokes. So I wrote a bot that bridges the two: tmux output goes to Telegram, your messages go back as keystrokes.



```
📱 Telegram Topics          tmux windows  
┌─────────────────┐        ┌──────────────┐  
│ 💬 api-refactor ├───────►│ @0: claude   │  
│ 💬 fix-auth     ├───────►│ @3: codex    │  
│ 💬 new-feature  ├───────►│ @5: gemini   │  
└─────────────────┘        └──────────────┘
```

One Telegram topic = one tmux window = one agent session. The agent doesn’t know CCGram exists. It’s running in tmux like it always does. When you want the real terminal back, `tmux attach` — full scrollback, nothing lost. Terminal is always the source of truth.


No SDK integration, no API wrapping, no rebuilding the agent inside some framework. Just tmux and Telegram.


## How I Actually Use It


I have multiple machines. iMac, laptops, a cloud VMs. Each machine runs its own CCGram instance connected to its own Telegram group. So in Telegram I have a group per machine. Inside each group, every topic is a session.


Right now on my desktop I have maybe 6–7 topics open. Some Claude Code, a couple Codex, one Gemini. Different projects, different tasks. I jump between them constantly.


The whole point is that it works from anywhere you have your phone. Your machine just needs to be on with tmux running. You’re at your desk, you’re in another room, you’re outside — doesn’t matter. The sessions are there.


Morning. I start sessions from the laptop, usually 2–3 Claude Code instances on different things. One is doing a refactor, one is writing tests, one is exploring a codebase. I give each a task and go make coffee. By the time I’m back, Claude read the spec, asked a question (I tapped a button on the inline keyboard while the coffee was brewing), and it’s already working.


Later. I’m away from the desk. Phone in hand, checking topics. Claude finished in one — topic emoji switched to 🟢 active, then 💤 idle, then the session ended. Codex is asking a question in another — inline keyboard, tap. Gemini needs direction — I type it or record a voice message.


Evening. In bed. Phone. Checking what finished, what’s stuck. One topic shows ❌ — Claude hit a rate limit and crashed. CCGram caught that the moment it happened and alerted me. I tap “▶ Continue” on the recovery keyboard and it picks up. I’ll check results tomorrow. (And then check again 10 minutes later. I have a problem.)


The result: my agents work way more hours than I sit at my desk. I’m the project manager now. Give instructions, check on progress, unblock when they’re stuck. Most of the actual coding happens while I’m doing something else.


## Claude, Codex, Gemini — Different Tools for Different Jobs


I run all three, and they’re not interchangeable.


Claude Code is the main one. Complex refactors, multi-file changes, anything that needs deep understanding of the codebase. It’s the workhorse.


Codex I use for planning and review — it’s very pedantic about following instructions, which is exactly what you want for those tasks. Also good when I hit Claude’s rate limits, which happens when you’re running multiple sessions. And it does happen.


Gemini is my third option. I’m still learning it, giving it smaller tasks, seeing how it handles things. Not the main tool yet, but it’s there and it’s getting better.


CCGram treats them all the same — each one is just a tmux window with a process in it. The bot auto-detects which agent is running from the process name. When I create a new topic, I pick the provider (🟠 Claude, 🟢 Codex, 🔵 Gemini). When I discover an existing tmux session, CCGram figures out what’s in it.


Switching between agents is just switching Telegram topics. Each topic has its own history, so I know what I told Claude 3 hours ago, what it did, what it asked. Same for the others.


Running 5+ agents in parallel changes how you think about work. You stop thinking “what should I do next” and start thinking “what can I delegate next.” Different mode entirely.


## Claude Remote Control — The Other Way


I should mention Claude Code’s remote-control feature because I use both and they solve different problems.


Remote control is great. Polished UI, nice mobile experience, feels like a proper app. But:


* You can’t start a new session from it — you need to be at your laptop to launch Claude Code first
* No voice input


CCGram is the opposite trade-off. The UI is Telegram — it’s a chat app, not a purpose-built interface. But I can start new sessions from my phone. I can run 10 sessions across 3 machines. I can send voice messages. I can see at a glance which sessions are active, which are done, which crashed.


So I use both. Remote control when I want a nice focused single-session experience with beautiful rendering on my iPhone. CCGram when I’m juggling multiple agents across machines. They complement each other — CCGram can detect when remote control is active and shows a 📡 badge on the topic. I can even start an RC session from Telegram.


## Voice: Still Getting Used to It


The voice feature is new — [Roy](https://github.com/royisme) contributed it. Record a voice message in Telegram, CCGram transcribes it via Whisper, shows you the text, you confirm or discard.


Honestly, I’m still getting used to it. My instinct is to type. But when I actually use voice, the instructions come out better. On a phone keyboard you type short because typing on glass is painful. “Fix the bug.” “Add tests.” Minimal.


When you talk, you explain. “Use exponential backoff with jitter, start at 100ms, cap at 30 seconds, respect the Retry-After header if the API returns one, and trip the circuit breaker after 5 consecutive failures.” That’s one sentence out loud. On a keyboard that’s autocorrect fighting you every word.


Better instructions = better code on first try. So I’m forcing myself to use it more.



```
CCGRAM_WHISPER_PROVIDER=groq  
GROQ_API_KEY=gsk_xxx
```

Two env vars. Groq has a free tier, transcription takes a couple of seconds.


## The Things You Don’t See


Some stuff that makes this work day-to-day:


Topic emojis. Each topic shows what’s happening at a glance: 🟢 active, 💤 idle (waiting for input), ❌ dead (crashed or killed). Badges too — 📡 when remote control is on, 🚀 when running in YOLO mode. You look at the group and know the state of everything without opening a single topic.


Session lifecycle. When Claude dies from a rate limit at 2am, CCGram sends you an alert immediately. Not when you check in the morning. You see it, tap “▶ Continue” or “📁 Resume” on the recovery keyboard, and it picks back up. Or ignore it and deal with it tomorrow. The point is you know.


Network resilience. [Miaoz](https://github.com/miaoz) fixed a bug where Telegram’s polling client would get stuck after a network hiccup. One bad connection, everything queues behind it forever. Now the client detects the failure and rebuilds itself. You never notice because it just works.


Agent discovery. [BLUE](https://github.com/blue-int) made it so CCGram finds any tmux session running AI agents, not just ones it created. Start Claude in some random tmux session, CCGram picks it up. Bind it to a topic and you’re connected.


## How This Project Happened


CCGram didn’t start as CCGram. It started as [ccbot](https://github.com/six-ddc/ccbot), a project by [six-ddc](https://github.com/six-ddc). He built the original idea — Telegram bot that talks to Claude Code through tmux. Simple, clever, worked.


I found it, liked it, contributed back. Tests, CI, config improvements. Normal open source workflow.


But then I needed more. Multi-provider support — Codex and Gemini, not just Claude. Topic-based architecture with proper session management. Interactive UI for agent prompts. Resume and continue. Hook-based events. Voice. The list kept growing fast.


Here’s the thing about open source: sometimes your direction diverges from the original. I needed features now, not after a discussion and review cycle. I needed to restructure things in ways that would change the original design completely. I needed to move fast and in my own direction.


So I forked. Rewrote most of it. Renamed it to CCGram. Published it as its own package.


I’m not going to dress this up. Someone built something good, I needed it to be different, so I took it and made it different. That’s what the MIT license is for. I kept the attribution, I credit six-ddc in the README, and I’m grateful for the starting point. Without ccbot there’s no CCGram.


The projects are completely separate now. Different architecture, different features, different direction. Over 280 commits since the fork, most of the original code rewritten. Sometimes the fork becomes its own thing. This one did.


## tmux: From “I Guess I Need This” to Actually Loving It


I’ll be honest — before this project, I barely used tmux. A few times for long-running SSH sessions on remote machines. That was it. Never needed it at home, never really understood the appeal. Prefix keys, scrollback buffers — felt like operating a submarine from the 1970s.


Building CCGram forced me to understand tmux for real. Window IDs, pane targeting, capture-pane with ANSI sequences, multi-pane scanning. And at some point I stopped fighting it and started appreciating it. tmux isn’t a UI. It’s an API for terminals. Every agent speaks terminal. tmux multiplexes it. CCGram bridges it to Telegram. Unix philosophy, 50 years old, still doing its job.


Now I use tmux for everything. Not because I have to. Because it’s actually good. Took me long enough.


## The Sleep Situation


CCGram increased my output a lot. But it also destroyed whatever boundary was left between work and not-work.


When you can start a coding session from bed, you start coding sessions from bed. When you can check on agents from anywhere, you check on agents from everywhere. It never stops. There’s always a topic to check, an agent to unblock, a task to start.


My agents collectively code maybe 14–16 hours a day now. I’m the bottleneck — the one who answers questions, reviews output, gives direction. CCGram made me reachable. Which means I’m kind of always on call for my own AI agents. This is a problem I created for myself and I don’t feel particularly bad about it.


Less sleep, more code. My GitHub graph is very green. My eye bags are also getting there. Trade-offs.


## What’s New in v2.1.0


For completeness:


* 🎤 Voice transcription — talk to your agents (Whisper via OpenAI/Groq)
* 📡 Remote Control — detect and start Claude Code RC from Telegram
* 🔌 Universal discovery — finds any tmux session running AI agents
* 🛡️ Resilient polling — auto-recovery from network failures
* ⚙️ StopFailure + SessionEnd hooks — instant alerts, clean session lifecycle
* 🔧 More commands — `/rc`, `/status`, `/mcp`, `/plan`, `/tasks`


## Contributors


Three people I’ve never met made this release better:


* [@royisme](https://github.com/royisme) (Roy Zhu) — voice transcription ([#24](https://github.com/alexei-led/ccgram/pull/24))
* [@blue-int](https://github.com/blue-int) (BLUE) — session discovery ([#27](https://github.com/alexei-led/ccgram/pull/27))
* [@miaoz](https://github.com/miaoz) (Miaoz) — resilient polling ([#26](https://github.com/alexei-led/ccgram/pull/26))


People show up, make your stuff better, and disappear back into the internet. That’s open source. Thank you.


## Try It



```
uv tool install ccgram  
# or  
brew install alexei-led/tap/ccgram
```

[*CCGram on GitHub*](https://github.com/alexei-led/ccgram) *|* [*PyPI*](https://pypi.org/project/ccgram/) *| MIT License*