---
categories:
  - "[[Resources]]"
domain: engineering
title: "I ditched Claude Code and OpenCode for Pi, and my coding workflow became predictable"
source: "https://www.xda-developers.com/replaced-claude-code-and-opencode-with-pi/"
author: "Joe Rice-Jones"
published: 2026-04-01
created: 2026-04-03
description: "It might not be everyone's first choice, but I like it"
tags:
  - to-process
  - harness-engineering
---

![pi open in a terminal](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/03/pi-terminal.jpg?&fit=crop&w=1600&h=900)
Whatever your feelings about AI-coding are, it's not going away any time soon. Whether you're [self-hosting a local LLM](https://www.xda-developers.com/finally-found-local-llm-want-use-coding/) or using the heft of cloud-based models, they all work better when used [by a harness](https://parallel.ai/articles/what-is-an-agent-harness). That's a software stack that wraps around the LLM, handling tool calls, memory, and file usage. It's not that far off an IDE in practice, and most AI-first coding tools are harnesses, whether it's [Claude Code](https://www.xda-developers.com/set-up-claude-code-like-boris-cherny/), [OpenCode](https://www.xda-developers.com/found-a-free-open-source-alternative-to-claude-code/), or my current favorite, Pi.


That's partly because it starts as a very minimal Terminal app, letting you create the harness that your workflow needs. But it's also because it's part of a larger ecosystem for building AI agents and managing LLMs, which I jive with for vibe coding.


##  The spectrum of permissibility


###  It's a fight between locked-down and do-what-you-will


When you're using agentic coding tools, there are so many variables to consider beyond which one looks best. Model support is a huge factor, so is what sort of limitations and guardrails are in place so that your agent doesn't nuke your development repo.


And so is the GUI, TUI, or CLI that will be running your agents. Some prefer the hands-off approach, while others, like Mario Zechner, who created Pi, want to see every aspect of the agent at work.




|  | Pi | OpenCode | Claude Code |
| --- | --- | --- | --- |
| Creator | Mario Zechner | Large open-source project, many contributors | Anthropic's own CLI harness for Claude |
| Primary goal | Minimal, opinionated harness built to Zechner's own demands | Editor-agnostic agent that works in IDEs, terminals, or desktop apps | Low-level harness integrated into Claude's ecosystem |
| Model support | Muti-provider (Anthropic, OpenAI, Google, xAI, Groq, Cerebras, OpenRouter, OpenAI‑compatible/self‑hosted endpoints) | Over 75 supported providers/models via Models.dev, including locally-hosted ones | Mostly tied to Claude variants, but can be used with other LLMs with a little setup time |
| Tooling model | Four core tools: read, write, edit, bash (plus optional read-only tools of grep, find, ls) | "Claude-style" tool set, LSP, and MCP integrations | Huge range of built-in tools and structured workflows |
| Safety stance | YOLO, you're in charge of the keyboard (and the results) | Safer defaults, but option to make it more permissive | Deny-first by default, strong defaults for other guardrails |
| Integration | Node/TS packages meant to embed into other systems | TUI, desktop app, IDE/ACP plugins | CLI/terminal experience inside Anthropic's ecosystem, desktop app |


I've used all three, and can see why each have its own place in the market, but it really depends on which LLM ecosystem you are in already, and how much control over your harness (not just the code it creates).


###  I have to say that Pi's approach has grown on me


Pi's creator wrote this harness after [using mostly Claude Code](https://mariozechner.at/posts/2025-11-30-pi-coding-agent/) since Anthropic released it. As Anthropic added more and more functionality, he decided to write a harness to gain control. Not only being able to "inspect every aspect of my interactions with the model," but also controlling the inputs into the model's context.


Did you know that most harnesses inject things into the context window without your consent or knowledge? Some of those are probably important things the harness creator thought needed to be in every prompt, but when you're not in control of any changes, that makes your workflow unpredictable, as you never know when things will change.


##  Why I prefer using Pi


###  Pi gives me the freedom that other harnesses are lacking


   ![pi designing a webapp](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/03/pi-terminal-designing-webapp.jpg?q=49&fit=crop&w=825&dpr=2) 
Pi does a few things better than other coding harnesses I've used. For a start, it uses fewer than 1,000 tokens for its system prompt, which describes **bash, read, edit,** and **write** as core tools. Fewer tools mean a larger context window for your workload, as you often lose 10k tokens in rules, examples, and safety instructions built into OpenCode or Claude Code.


It's also a difference in methodology. Most harnesses try to solve context for you, while Pi expects you to create a structure with markdown files dedicated to planning, todo, and other aspects that are second-nature in Claude Code and others. It might take a little longer to set up, but it's more reproducible because the LLM gets the same structured files when prompted again.


Pi also shows you code differences as it rewrites them, with a streamed view. That's fantastic for me, because I'm still learning the languages that I use most, and being able to see fixes as they happen is almost as good as being in a lecture hall.


###  And will willingly self-modify


   ![pi telling me how to create new extensions](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/03/pi-telling-me-how-to-create-extensions.jpg?q=49&fit=crop&w=825&dpr=2) 
The other really cool thing about Pi for me is that I can think of an extension that I need to accomplish something, and Pi will create it for me. Yes, that's an LLM harness willingly self-modifying, in a similar way to OpenClaw. One of the existing extensions is **permission-gate.ts**, which lets you block dangerous commands. I haven't been brave enough to see if it can block **rm** but maybe it can.


###  Subscribe for LLM harness insights and tool reviews


The newsletter untangles practical tradeoffs across AI-coding harnesses—context injection, token budgets, tool sets, safety guardrails, and extension workflows. Subscribing delivers focused, comparative coverage to help you evaluate those options.


 Get Updates


By subscribing, you agree to receive newsletter and marketing emails, and accept our [Terms of Use](https://www.valnetinc.com/en/terms-of-use) and [Privacy Policy](https://www.valnetinc.com/en/privacy-policy). You can unsubscribe anytime.


They're written in TypeScript, which makes it almost as easy to read as the markdown files other harnesses prefer, but it really doesn't matter because Pi can create them for you. That, combined with being able to connect to multiple thinking models, is a game-changer for me, I know Skills work sort of in the same way, but being able to build the specific tools I need is awesome.


###  Pi is closer to the terminal coding assistant I want to use


I like being in control, but I also like that Pi drastically reduces the number of tokens of context fed from a prompt. That means I get more thinking for my bucks, and that's a fantastic feeling. But I also like that it's minimal and predictable, while still allowing extensions to add workflow-specific parts.