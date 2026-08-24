---
title: "Claude Code is Expensive. This MCP Server Fixes It (Context Mode)"
source: "youtube"
url: "https://www.youtube.com/watch?v=QUHrntlfPo4"
author: "Better Stack"
published: "2026-03-13"
created: "2026-08-24"
duration: "0:06:09"
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
  - "engineering"
  - "local-llm"
  - "mcp"
  - "video-gen"
summary: "If you've been coding in Claude code, you've probably experienced context load. The problem is that every MCP tool call in Claude code is ridiculously expensive because every one of these calls dumps its full output directly into the model's 200k context window. And the more tools you have under the tool belt, the faster your context depletes."
---

# Claude Code is Expensive. This MCP Server Fixes It (Context Mode)

![Claude Code is Expensive. This MCP Server Fixes It (Context Mode)](https://www.youtube.com/embed/QUHrntlfPo4)

## Description

Stop letting "Context Bloat" ruin your AI coding sessions by turning every MCP tool call into a massive token drain. In this video, we dive into Context-mode, a virtualization layer for Claude Code that saves up to 99% of your context by indexing raw data into a local sandbox. Learn how to implement session continuity so your AI agent never forgets a task again, allowing you to extend your productive coding time from 30 minutes to over 3 hours.

🔗 Relevant Links
Context Mode: https://github.com/mksglu/context-mode

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
00:00 Intro
0:35 Introducing Context Mode
0:57 The Math Behind Token Waste
1:17 How Context Virtualization Works
1:56 Session Continuity & "Save Checkpoints"
2:40 Quick Installation Guide
3:07 Live Demo: Log Analysis
4:01 Cost Savings Review
5:11 Maintaining The Intelligence Of The Model
5:42 Outro

## Transcript

If you've been coding in Claude code, you've probably experienced context load. The problem is that every MCP tool call in Claude code is ridiculously expensive because every one of these calls dumps its full output directly into the model's 200k context window. And the more tools you have under the tool belt, the faster your context depletes. Under certain scenarios, you're looking at 30 minutes of active agent use before your context compacts. And that's when the AI starts forgetting files, tasks, and crucial decisions. Not to mention you're spending a lot of money on those tokens. But, there is an MCP server out there that solves this crucial issue. It's called context mode. In today's video, we'll take a look at what context mode does, how it works, and try it out for ourselves with a little demo. It's going to be a lot of fun, so let's dive into it. To understand why this happens, let's look at the math. A single Playwright snapshot of a web page is about 56 kilobytes. Reading 20 GitHub issues is 59 kilobytes. If we do these operations in the planning phase multiple times in a session, you've probably eaten 70% of your window before the agent has even written a single line of code. Context mode acts as a virtualization layer. Instead of the AI talking directly to your OS, it talks to a sandbox. And instead of dumping massive outputs, context mode indexes them in a local SQLite database using FTS5, aka full-text search. And the result is pretty significant. For example, that 56k Playwright snapshot is reduced to 299 bytes, a 99% reduction. Or for example, this analytics CSV is crunched down to 222 bytes, which is a near 100% reduction. But, saving tokens is just one part of the fix. The real utility here is the session continuity. We've all seen how the agents compact history and suddenly you lose track of the code it has written 10 minutes earlier, but context mode uses hooks to monitor every file edit, get operation, and sub agent task. When your conversation compacts, context mode builds a priority tiered snapshot, usually under 2 kilobytes, and injects it back in. It's essentially a save checkpoint for your coding session. So, you could hypothetically extend your session time from 30 minutes to approximately 3 hours. It also tracks decisions and errors. For example, if the AI tried a fix that failed 20 minutes ago, it won't repeat that mistake even after the context resets. And installing it is very straightforward. If you're on Claude Code, first add the context mode marketplace by running this following command, and then run the plugin install command. And once you're done, you're good to go. Once you've installed it, it handles the MCP server, the hooks, and the routing instructions automatically. If you're on Gemini CLI or VS Code Copilot, you can run npm install context mode and add the config to your settings. Now, let's see context mode in action. I have this simple Python command here that will create a dummy access log file that contains a list of a bunch of dummy API requests and their status codes, and every hundredth line is a 500 error log. Now, we can fire up Claude and ask, "Hey, use context mode to index access.log. I want to find all the 500 error patterns and summarize the IP addresses associated with them." And in the background, context mode chunks the 5,000 lines of the access.log file into its own SQLite FTS5 database. And Claude only receives confirmation that the file is indexed, not the raw 5,000 lines of the file. And now Claude can intelligently search the index database to query the contents instead of parsing the whole file. And here we can see the findings returned by Claude, but more importantly, let's look at the cost savings. We can do this by running context mode column CTS stats, and we can check out how much data is saved by context mode in this current session. And you can see the results right here. Instead of dumping the entire 20 kilobytes into the conversation, context mode kept about 5 kilobytes of that raw data in the sandbox. And this result is pretty impressive for a small file. It spared about 1,200 tokens from entering the context window. So, overall, we get a nice 25% reduction running this little test. That may not sound like much, but keep in mind that in a standard Claude session, the data would just sit there forever getting resent with every single message that you send. And by keeping it in the sandbox, we've already started to extend the life of the session. And this demo file is pretty small, but if you deal with larger files, the savings here could be massive. If you're running a massive repo research project or analyzing production-scale logs, that 1,200 token saving can easily turn into 100,000 tokens. But the goal here isn't just about saving money on API costs, though that is a nice bonus. It's also about maintaining the intelligence of the model. When you clear the noise out of the context window, you're leaving more room for actual reasoning. You're giving Claude the space it needs to be a better engineer. So, if you're building complex projects with AI agents, give this tool a shot and see how much longer you can extend the sessions before the agent starts compacting and forgetting things. And if you enjoyed this technical breakdown, please let me know by smashing that like button underneath the video. And also, don't forget to subscribe to our channel. This has been Andres from Better Stack, and I will see you in the next videos. >> [music] [music]
