---
title: "Stop Using Claude Code CLI. Use THIS Instead! (Oh-My-Pi)"
source: "youtube"
url: "https://www.youtube.com/watch?v=8ukl-0tlVgM"
author: "Better Stack"
published: "2026-05-30"
created: "2026-08-24"
duration: "0:05:06"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "anthropic"
  - "context-engineering"
  - "engineering"
  - "evaluation"
  - "harness-engineering"
  - "video-gen"
summary: "It's a new AI agent harness built on top of the popular Pi framework, but supercharged with all sorts of goodies and useful features that makes this one of the most powerful AI agent harnesses I've ever used. [music] In this video, we'll take a look at Oh My Pi, see how it works, and check out all the cool features it offers. Now, if you've used other terminal AI tools like Claude Code CLI or standard LLM wrappers, you know how usually it goes."
---

# Stop Using Claude Code CLI. Use THIS Instead! (Oh-My-Pi)

![Stop Using Claude Code CLI. Use THIS Instead! (Oh-My-Pi)](https://www.youtube.com/embed/8ukl-0tlVgM)

## Description

In this video, we look at Oh-My-Pi, an open-source terminal AI agent harness that treats your project like a living, breathing application runtime instead of flat text files. We break down its four massive architectural upgrades, including native Language Server Protocol (LSP) integration, direct Debugger Adapter Protocol (DAP) support, and a highly efficient content-hash editing tool.

🔗 Relevant Links
Oh-My-Pi: https://omp.sh
Oh-My-Pi: Github Repo: https://github.com/can1357/oh-my-pi

❤️ More about us
Radically better observability stack: https://betterstack.com/
Written tutorials: https://betterstack.com/community/
Example projects: https://github.com/BetterStackHQ

📱 Socials
Twitter: https://twitter.com/betterstackhq
Instagram: https://www.instagram.com/betterstackhq/
TikTok: https://www.tiktok.com/@betterstack
LinkedIn: https://www.linkedin.com/company/betterstack

📌 Chapters:
00:00 - Intro
00:27 - Why Standard AI CLI Wrappers Fail
00:52 - Feature 1: Native LSP Integration (IDE Features)
01:31 - Feature 2: Built-in Debugger Adapter Protocol (DAP)
02:02 - Feature 3: Model Agnostic Architecture
02:24 - Feature 4: Hashline Edits (Saving 61% on Tokens)
02:58 - Testing it Out: Building a Rust App & Headless Browser
03:20 - TUI Design & Custom Extensions (Running Doom!)
04:07 - Advanced Features & Final Verdict

## Transcript

This is Oh My Pi. It's a new AI agent harness built on top of the popular Pi framework, but supercharged with all sorts of goodies and useful features that makes this one of the most powerful AI agent harnesses I've ever used. [music] In this video, we'll take a look at Oh My Pi, see how it works, and check out all the cool features it offers. Let's get into it. Now, if you've used other terminal AI tools like Claude Code CLI or standard LLM wrappers, you know how usually it goes. You ask it to fix a bug, it stares at your source code as a giant wall of text, guesses the fix, throws in a couple of print statements, and hopes for the best. But Oh My Pi doesn't treat your project like a collection of flat text files. It treats it like a living, breathing application runtime. And the way it does that is through four massive architectural upgrades. First up, it has a native LSP or language server protocol integration. When you ask Oh My Pi to do something like rename a core module or refactor a function that's imported across 50 different files, it hooks straight into your language server to perform a proper workspace-level structural refactor. It automatically updates your barrel files, handles aliased imports, and cleans up re-exports before it even touches the disk. So, it kind of works like an IDE, and that's what is missing in the standard Claude Code CLI harness. Secondly, it has a full debugger adapter protocol support built right into it. If your Go service deadlocks or your Python API throws a weird concurrent runtime error, or your C file breaks, Oh My Pi is able to boot up debugger tools like DLV or debugpy and attach them directly to your broken process. And then it can also hit breakpoints and evaluate the actual live memory state and stack frames. Thirdly, it's completely model agnostic. You can hook it up to so many providers. So, for example, I can log in with my Claude Code account, and it will automatically port all my plugins and settings from Claude Code to O my Pi. And another cool thing is that you can choose different models for different tasks. So, I can have a special vision model for vision tasks and a special designer model for design tasks, etc. And fourth, it has this cool feature called hash line edits. So, when Claude Code edits files, it sends the literal old string and the literal new string. And Opus reproduces every character it wants to change. But when O my Pi changes your code, it doesn't retype the whole file or send massive text diffs. It targets the exact line using a content hash anchor. This prevents whitespace syntax errors. And for example, for a model like Grok-4-Fast, it can save up to 61% on your LLM token usage. And I tested it out by asking it to build a Rust desktop application that lists ticker symbols from StockTwits. And one thing that I really liked is that O my Pi has its own browser tool. Whenever it needed to retrieve data from the web, it actually launched a Chrome browser instance on its own rather than trying to extract it via curl or fetch calls. And overall, I really like the aesthetic of it. It has these nice integrated task windows that are so much easier to read through compared to a harness like Claude Code CLI. So, you can really see that authors of O my Pi really put in a lot of effort into the design. And another cool thing is that since O my Pi is built on top of Pi, it also supports adding packages from the original Pi editor. And to add a package to O my Pi, you simply need to replace the first half of the install command with O my Pi plugin install followed by the package name. I managed to install the hilarious Doom package from the original pie onto O my pie. So, whenever I get bored, I can now launch Doom on the terminal by just typing {slash} Doom and play the classic game inside the terminal. That's just insane. And honestly, there are so many other features this harness has that I didn't even had a chance to cover. It has a really nice PR review tool. It supports running sub agents. It can easily read PDFs. And it uses hindsight for agent memory management. So, all in all, I would say it's a powerhouse tool and it's open source and it has tons of cool features. So, I definitely recommend trying it out if you haven't already. But, what do you think of O my pi? Have you tried it? Will you use it? Let us know in the comment section down below. And folks, if you like these types of technical breakdowns, please let me know by smashing that like button underneath the video. And also, don't forget to subscribe to our channel. This has been Andres from Better Stack and I will see you in the next videos. >> [music] [music]
