---
categories:
  - "[[Resources]]"
domain: engineering
title: "Claude Code is Expensive. This MCP Server Fixes It (Context Mode)"
source: "https://www.youtube.com/watch?v=QUHrntlfPo4"
author: "Better Stack"
published: 2026-03-12
created: 2026-06-05
description: "Stop letting \"Context Bloat\" ruin your AI coding sessions by turning every"
tags:
  - to-process
  - agent-plugins-mcp
---

If you've been coding in Claude code, you've probably experienced context load. The problem is that every MCP tool call in Claude code is ridiculously expensive because every one of these calls dumps its full output directly into the model's 200k context window. And the more tools you have under the tool belt, the faster your context depletes. Under certain scenarios, you're looking at 30 minutes of active agent use before your context compacts. And that's when the AI starts forgetting 

files, tasks, and crucial decisions. Not to mention you're spending a lot of money on those tokens. But, there is an MCP server out there that solves this crucial issue. It's called context mode. In today's video, we'll take a look at what context mode does, how it works, and try it out for ourselves with a little demo. It's going to be a lot of fun, so let's dive into it. To understand why this happens, let's look at the math. A single Playwright snapshot of a web page is about 56 

kilobytes. Reading 20 GitHub issues is 59 kilobytes. If we do these operations in the planning phase multiple times in a session, you've probably eaten 70% of your window before the agent has even written a single line of code. Context mode acts as a virtualization layer. Instead of the AI talking directly to your OS, it talks to a sandbox. And instead of dumping massive outputs, context mode indexes them in a local SQLite database using FTS5, aka 

full-text search. And the result is pretty significant. For example, that 56k Playwright snapshot is reduced to 299 bytes, a 99% reduction. Or for example, this analytics CSV is crunched down to 222 bytes, which is a near 100% reduction. But, saving tokens is just one part of the fix. The real utility here is the session continuity. We've all seen how the agents compact history 

and suddenly you lose track of the code it has written 10 minutes earlier, but context mode uses hooks to monitor every file edit, get operation, and sub agent task. When your conversation compacts, context mode builds a priority tiered snapshot, usually under 2 kilobytes, and injects it back in. It's essentially a save checkpoint for your coding session. So, you could hypothetically extend your session time from 30 minutes to approximately 3 hours. It also tracks 

decisions and errors. For example, if the AI tried a fix that failed 20 minutes ago, it won't repeat that mistake even after the context resets. And installing it is very straightforward. If you're on Claude Code, first add the context mode marketplace by running this following command, and then run the plugin install command. And once you're done, you're good to go. Once you've installed it, it handles the MCP server, the hooks, and the routing instructions automatically. If you're on 

Gemini CLI or VS Code Copilot, you can run npm install context mode and add the config to your settings. Now, let's see context mode in action. I have this simple Python command here that will create a dummy access log file that contains a list of a bunch of dummy API requests and their status codes, and every hundredth line is a 500 error log. Now, we can fire up Claude and ask, "Hey, use context mode to index access.log. I want to find all the 500 error 

patterns and summarize the IP addresses associated with them." And in the background, context mode chunks the 5,000 lines of the access.log file into its own SQLite FTS5 database. And Claude only receives confirmation that the file is indexed, not the raw 5,000 lines of the file. And now Claude can intelligently search the index database to query the contents instead of parsing the whole file. And here we can see the findings returned by Claude, but more 

importantly, let's look at the cost savings. We can do this by running context mode column CTS stats, and we can check out how much data is saved by context mode in this current session. And you can see the results right here. Instead of dumping the entire 20 kilobytes into the conversation, context mode kept about 5 kilobytes of that raw data in the sandbox. And this result is pretty impressive for a small file. It spared about 1,200 tokens from entering 

the context window. So, overall, we get a nice 25% reduction running this little test. That may not sound like much, but keep in mind that in a standard Claude session, the data would just sit there forever getting resent with every single message that you send. And by keeping it in the sandbox, we've already started to extend the life of the session. And this demo file is pretty small, but if you deal with larger files, the savings here could be massive. If you're running a 

massive repo research project or analyzing production-scale logs, that 1,200 token saving can easily turn into 100,000 tokens. But the goal here isn't just about saving money on API costs, though that is a nice bonus. It's also about maintaining the intelligence of the model. When you clear the noise out of the context window, you're leaving more room for actual reasoning. You're giving Claude the space it needs to be a better engineer. So, if you're building 

complex projects with AI agents, give this tool a shot and see how much longer you can extend the sessions before the agent starts compacting and forgetting things. And if you enjoyed this technical breakdown, please let me know by smashing that like button underneath the video. And also, don't forget to subscribe to our channel. This has been Andres from Better Stack, and I will see you in the next videos. >> [music] 

[music] 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 If you've been coding in Claude code,
 </span>
 <span data-rw-start="2.08" data-rw-transcript-version="2">
 you've probably experienced context load. The problem is that every MCP tool
 </span>
 <span data-rw-start="4.4" data-rw-transcript-version="2">
 call in Claude code is ridiculously
 </span>
 <span data-rw-start="7.24" data-rw-transcript-version="2">
 expensive because every one of these
 </span>
 <span data-rw-start="9.68" data-rw-transcript-version="2">
 calls dumps its full output directly
 </span>
 <span data-rw-start="11.6" data-rw-transcript-version="2">
 into the model's 200k context window.
 </span>
 <span data-rw-start="13.88" data-rw-transcript-version="2">
 And the more tools you have under the
 </span>
 <span data-rw-start="16.84" data-rw-transcript-version="2">
 tool belt, the faster your context
 </span>
 <span data-rw-start="18.44" data-rw-transcript-version="2">
 depletes. Under certain scenarios,
 </span>
 <span data-rw-start="20.56" data-rw-transcript-version="2">
 you're looking at 30 minutes of active
 </span>
 <span data-rw-start="22.96" data-rw-transcript-version="2">
 agent use before your context compacts.
 </span>
</p>
<p>
 <span data-rw-start="25.2" data-rw-transcript-version="2">
 And that's when the AI starts forgetting
 </span>
 <span data-rw-start="28.36" data-rw-transcript-version="2">
 files, tasks, and crucial decisions. Not
 </span>
 <span data-rw-start="30.16" data-rw-transcript-version="2">
 to mention you're spending a lot of
 </span>
 <span data-rw-start="33.12" data-rw-transcript-version="2">
 money on those tokens. But, there is an
 </span>
 <span data-rw-start="34.64" data-rw-transcript-version="2">
 MCP server out there that solves this
 </span>
 <span data-rw-start="36.56" data-rw-transcript-version="2">
 crucial issue. It's called context mode.
 </span>
</p>
<p>
 <span data-rw-start="41.84" data-rw-transcript-version="2">
 In today's video, we'll take a look at
 </span>
 <span data-rw-start="43.6" data-rw-transcript-version="2">
 what context mode does, how it works,
 </span>
 <span data-rw-start="45.84" data-rw-transcript-version="2">
 and try it out for ourselves with a
 </span>
 <span data-rw-start="47.64" data-rw-transcript-version="2">
 little demo. It's going to be a lot of
 </span>
 <span data-rw-start="49.52" data-rw-transcript-version="2">
 fun, so let's dive into it.
 </span>
</p>
<p>
 <span data-rw-start="55.36" data-rw-transcript-version="2">
 To understand why this happens, let's
 </span>
 <span data-rw-start="57.48" data-rw-transcript-version="2">
 look at the math. A single Playwright
 </span>
 <span data-rw-start="59.4" data-rw-transcript-version="2">
 Snapshot of a web page is about 56
 </span>
 <span data-rw-start="62.04" data-rw-transcript-version="2">
 kilobytes. Reading 20 GitHub issues is
 </span>
 <span data-rw-start="64.8" data-rw-transcript-version="2">
 59 kilobytes. If we do these operations
 </span>
 <span data-rw-start="68" data-rw-transcript-version="2">
 in the planning phase multiple times in
 </span>
 <span data-rw-start="70.12" data-rw-transcript-version="2">
 a session, you've probably eaten 70% of
 </span>
 <span data-rw-start="73.16" data-rw-transcript-version="2">
 your window before the agent has even
 </span>
 <span data-rw-start="75.4" data-rw-transcript-version="2">
 written a single line of code. Context
 </span>
 <span data-rw-start="77.88" data-rw-transcript-version="2">
 mode acts as a virtualization layer.
 </span>
</p>
<p>
 <span data-rw-start="80.52" data-rw-transcript-version="2">
 Instead of the AI talking directly to
 </span>
 <span data-rw-start="82.6" data-rw-transcript-version="2">
 your OS, it talks to a sandbox. And
 </span>
 <span data-rw-start="85.44" data-rw-transcript-version="2">
 instead of dumping massive outputs,
 </span>
 <span data-rw-start="87.56" data-rw-transcript-version="2">
 context mode indexes them in a local
 </span>
 <span data-rw-start="90" data-rw-transcript-version="2">
 SQLite database using FTS5, aka
 </span>
 <span data-rw-start="93.52" data-rw-transcript-version="2">
 full-text search. And the result is
 </span>
 <span data-rw-start="95.68" data-rw-transcript-version="2">
 pretty significant. For example, that
 </span>
 <span data-rw-start="97.48" data-rw-transcript-version="2">
 56k Playwright snapshot is reduced to
 </span>
 <span data-rw-start="100.16" data-rw-transcript-version="2">
 299 bytes, a 99% reduction. Or for
 </span>
 <span data-rw-start="104.36" data-rw-transcript-version="2">
 example, this analytics CSV is crunched
 </span>
 <span data-rw-start="106.88" data-rw-transcript-version="2">
 down to 222 bytes, which is a near 100%
 </span>
 <span data-rw-start="110.96" data-rw-transcript-version="2">
 reduction. But, saving tokens is just
 </span>
 <span data-rw-start="113.36" data-rw-transcript-version="2">
 one part of the fix. The real utility
 </span>
 <span data-rw-start="116" data-rw-transcript-version="2">
 here is the session continuity. We've
 </span>
 <span data-rw-start="118.96" data-rw-transcript-version="2">
 all seen how the agents compact history
 </span>
 <span data-rw-start="121.8" data-rw-transcript-version="2">
 and suddenly you lose track of the code
 </span>
 <span data-rw-start="123.92" data-rw-transcript-version="2">
 it has written 10 minutes earlier, but
 </span>
 <span data-rw-start="126.2" data-rw-transcript-version="2">
 Context mode uses hooks to monitor every
 </span>
 <span data-rw-start="128.88" data-rw-transcript-version="2">
 file edit, get operation, and sub agent
 </span>
 <span data-rw-start="131.84" data-rw-transcript-version="2">
 task. When your conversation compacts,
 </span>
 <span data-rw-start="134.28" data-rw-transcript-version="2">
 context mode builds a priority tiered
 </span>
 <span data-rw-start="136.68" data-rw-transcript-version="2">
 snapshot, usually under 2 kilobytes, and
 </span>
 <span data-rw-start="139.52" data-rw-transcript-version="2">
 injects it back in. It's essentially a
 </span>
 <span data-rw-start="142.04" data-rw-transcript-version="2">
 save checkpoint for your coding session.
 </span>
</p>
<p>
 <span data-rw-start="144.72" data-rw-transcript-version="2">
 So, you could hypothetically extend your
 </span>
 <span data-rw-start="146.52" data-rw-transcript-version="2">
 session time from 30 minutes to
 </span>
 <span data-rw-start="148.52" data-rw-transcript-version="2">
 approximately 3 hours. It also tracks
 </span>
 <span data-rw-start="151.28" data-rw-transcript-version="2">
 decisions and errors. For example, if
 </span>
 <span data-rw-start="153.52" data-rw-transcript-version="2">
 the AI tried a fix that failed 20
 </span>
 <span data-rw-start="155.72" data-rw-transcript-version="2">
 minutes ago, it won't repeat that
 </span>
 <span data-rw-start="157.68" data-rw-transcript-version="2">
 mistake even after the context resets.
 </span>
</p>
<p>
 <span data-rw-start="160.48" data-rw-transcript-version="2">
 And installing it is very
 </span>
 <span data-rw-start="161.8" data-rw-transcript-version="2">
 straightforward. If you're on Claude
 </span>
 <span data-rw-start="163.48" data-rw-transcript-version="2">
 Code, first add the context mode
 </span>
 <span data-rw-start="165.64" data-rw-transcript-version="2">
 marketplace by running this following
 </span>
 <span data-rw-start="167.64" data-rw-transcript-version="2">
 command,
 </span>
 <span data-rw-start="169.04" data-rw-transcript-version="2">
 and then run the plugin install command.
 </span>
</p>
<p>
 <span data-rw-start="172.12" data-rw-transcript-version="2">
 And once you're done, you're good to go.
 </span>
 <span data-rw-start="174.2" data-rw-transcript-version="2">
 Once you've installed it, it handles the
 </span>
 <span data-rw-start="175.959" data-rw-transcript-version="2">
 MCP server, the hooks, and the routing
 </span>
 <span data-rw-start="178.16" data-rw-transcript-version="2">
 instructions automatically. If you're on
 </span>
 <span data-rw-start="180.32" data-rw-transcript-version="2">
 Gemini CLI or VS Code Copilot, you can
 </span>
 <span data-rw-start="183.36" data-rw-transcript-version="2">
 Run npm install context mode and add the
 </span>
 <span data-rw-start="186.48" data-rw-transcript-version="2">
 config to your settings. Now, let's see
 </span>
 <span data-rw-start="188.48" data-rw-transcript-version="2">
 context mode in action. I have this
 </span>
 <span data-rw-start="190.6" data-rw-transcript-version="2">
 simple Python command here that will
 </span>
 <span data-rw-start="192.56" data-rw-transcript-version="2">
 create a dummy access log file that
 </span>
 <span data-rw-start="195.12" data-rw-transcript-version="2">
 contains a list of a bunch of dummy API
 </span>
 <span data-rw-start="197.88" data-rw-transcript-version="2">
 requests and their status codes, and
 </span>
 <span data-rw-start="200.239" data-rw-transcript-version="2">
 every hundredth line is a 500 error log.
 </span>
</p>
<p>
 <span data-rw-start="203.4" data-rw-transcript-version="2">
 Now, we can fire up Claude and ask,
 </span>
 <span data-rw-start="205.8" data-rw-transcript-version="2">
 "Hey, use context mode to index
 </span>
 <span data-rw-start="208.2" data-rw-transcript-version="2">
 access.log.
 </span>
 <span data-rw-start="209.8" data-rw-transcript-version="2">
 I want to find all the 500 error
 </span>
 <span data-rw-start="211.92" data-rw-transcript-version="2">
 patterns and summarize the IP addresses
 </span>
 <span data-rw-start="214.64" data-rw-transcript-version="2">
 associated with them." And in the
 </span>
 <span data-rw-start="216.32" data-rw-transcript-version="2">
 background, context mode chunks the
 </span>
 <span data-rw-start="218.92" data-rw-transcript-version="2">
 5,000 lines of the access.log file into
 </span>
 <span data-rw-start="222.68" data-rw-transcript-version="2">
 its own SQLite FTS5 database. And Claude
 </span>
 <span data-rw-start="226.2" data-rw-transcript-version="2">
 only receives confirmation that the file
 </span>
 <span data-rw-start="228.4" data-rw-transcript-version="2">
 is indexed, not the raw 5,000 lines of
 </span>
 <span data-rw-start="231.36" data-rw-transcript-version="2">
 the file. And now Claude can
 </span>
 <span data-rw-start="233.12" data-rw-transcript-version="2">
 intelligently search the index database
 </span>
 <span data-rw-start="235.76" data-rw-transcript-version="2">
 to query the contents instead of parsing
 </span>
 <span data-rw-start="237.92" data-rw-transcript-version="2">
 the whole file. And here we can see the
 </span>
 <span data-rw-start="240" data-rw-transcript-version="2">
 findings returned by Claude, but more
 </span>
 <span data-rw-start="242.12" data-rw-transcript-version="2">
 importantly, let's look at the cost.
 </span>
</p>
<p>
 <span data-rw-start="243.88" data-rw-transcript-version="2">
 Savings. We can do this by running
 </span>
 <span data-rw-start="245.8" data-rw-transcript-version="2">
 context mode column CTS stats, and we
 </span>
 <span data-rw-start="249.16" data-rw-transcript-version="2">
 can check out how much data is saved by
 </span>
 <span data-rw-start="251.48" data-rw-transcript-version="2">
 context mode in this current session.
 </span>
 <span data-rw-start="253.76" data-rw-transcript-version="2">
 And you can see the results right here.
 </span>
 <span data-rw-start="256" data-rw-transcript-version="2">
 Instead of dumping the entire 20
 </span>
 <span data-rw-start="257.68" data-rw-transcript-version="2">
 kilobytes into the conversation, context
 </span>
 <span data-rw-start="260.359" data-rw-transcript-version="2">
 mode kept about 5 kilobytes of that raw
 </span>
 <span data-rw-start="263.52" data-rw-transcript-version="2">
 data in the sandbox. And this result is
 </span>
 <span data-rw-start="266.04" data-rw-transcript-version="2">
 pretty impressive for a small file. It
 </span>
 <span data-rw-start="268.16" data-rw-transcript-version="2">
 spared about 1,200 tokens from entering
 </span>
 <span data-rw-start="272.16" data-rw-transcript-version="2">
 the context window. So, overall, we get
 </span>
 <span data-rw-start="274.36" data-rw-transcript-version="2">
 a nice 25% reduction running this little
 </span>
 <span data-rw-start="277.44" data-rw-transcript-version="2">
 test. That may not sound like much, but
 </span>
 <span data-rw-start="280.28" data-rw-transcript-version="2">
 keep in mind that in a standard Claude
 </span>
 <span data-rw-start="282.48" data-rw-transcript-version="2">
 session, the data would just sit there
 </span>
 <span data-rw-start="284.68" data-rw-transcript-version="2">
 forever getting resent with every single
 </span>
 <span data-rw-start="287.76" data-rw-transcript-version="2">
 message that you send. And by keeping it
 </span>
 <span data-rw-start="290.16" data-rw-transcript-version="2">
 in the sandbox, we've already started to
 </span>
 <span data-rw-start="292.4" data-rw-transcript-version="2">
 extend the life of the session. And this
 </span>
 <span data-rw-start="294.919" data-rw-transcript-version="2">
 demo file is pretty small, but if you
 </span>
 <span data-rw-start="296.8" data-rw-transcript-version="2">
 deal with larger files, the savings here
 </span>
 <span data-rw-start="299.12" data-rw-transcript-version="2">
 could be massive. If you're running a
 </span>
 <span data-rw-start="301.12" data-rw-transcript-version="2">
 massive repo research project or
 </span>
</p>
<p>
 <span data-rw-start="303.36" data-rw-transcript-version="2">
 analyzing production-scale logs, that
 </span>
 <span data-rw-start="305.72" data-rw-transcript-version="2">
 1,200 token saving can easily turn into
 </span>
 <span data-rw-start="309.28" data-rw-transcript-version="2">
 100,000 tokens. But the goal here isn't
 </span>
 <span data-rw-start="312.16" data-rw-transcript-version="2">
 just about saving money on API costs,
 </span>
 <span data-rw-start="315" data-rw-transcript-version="2">
 though that is a nice bonus. It's also
 </span>
 <span data-rw-start="317.16" data-rw-transcript-version="2">
 about maintaining the intelligence of
 </span>
 <span data-rw-start="319.76" data-rw-transcript-version="2">
 the model. When you clear the noise out
 </span>
 <span data-rw-start="322.04" data-rw-transcript-version="2">
 of the context window, you're leaving
 </span>
 <span data-rw-start="324.2" data-rw-transcript-version="2">
 more room for actual reasoning. You're
 </span>
 <span data-rw-start="326.6" data-rw-transcript-version="2">
 giving Claude the space it needs to be a
 </span>
 <span data-rw-start="329.36" data-rw-transcript-version="2">
 better engineer. So, if you're building
 </span>
 <span data-rw-start="331.52" data-rw-transcript-version="2">
 complex projects with AI agents, give
 </span>
 <span data-rw-start="334.4" data-rw-transcript-version="2">
 this tool a shot and see how much longer
 </span>
 <span data-rw-start="336.4" data-rw-transcript-version="2">
 you can extend the sessions before the
 </span>
 <span data-rw-start="338.44" data-rw-transcript-version="2">
 agent starts compacting and forgetting
 </span>
 <span data-rw-start="340.8" data-rw-transcript-version="2">
 things. And if you enjoyed this
 </span>
 <span data-rw-start="342.36" data-rw-transcript-version="2">
 technical breakdown, please let me know
 </span>
 <span data-rw-start="344.2" data-rw-transcript-version="2">
 by smashing that like button underneath
 </span>
 <span data-rw-start="346.08" data-rw-transcript-version="2">
 the video. And also, don't forget to
 </span>
 <span data-rw-start="348.2" data-rw-transcript-version="2">
 subscribe to our channel. This has been
 </span>
 <span data-rw-start="350.28" data-rw-transcript-version="2">
 Andres from Better Stack, and I will see
 </span>
 <span data-rw-start="352.4" data-rw-transcript-version="2">
 you in the next videos.
 </span>
</p>
<p>
 <span data-rw-start="354.359" data-rw-transcript-version="2">
 &gt;&gt; [music]
 </span>
 <span data-rw-start="360.909" data-rw-transcript-version="2">
 [music]
 </span>
</p>