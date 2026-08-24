---
title: "Anthropic Just Solved The Biggest Claude Code Problem! /goals safes the day!"
source: "youtube"
url: "https://www.youtube.com/watch?v=v0zG69WGKAQ"
author: "DIY Smart Code"
published: "2026-05-12"
created: "2026-08-24"
duration: "0:01:46"
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
summary: "There's a new slash command in Cloud Code and Haiku judges Sonnet now. It's called slash goal and it just made typing keep going obsolete. You state one completion condition."
---

# Anthropic Just Solved The Biggest Claude Code Problem! /goals safes the day!

![Anthropic Just Solved The Biggest Claude Code Problem! /goals safes the day!](https://www.youtube.com/embed/v0zG69WGKAQ)

## Description

Claude Code's new `/goal` slash command sets a completion condition once and keeps Claude working, turn after turn, until Haiku confirms it's met. Shipped in v2.1.139.

----
🚀 Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount
----

Try it now:
```
/goal all tests in test/auth pass and the lint step is clean
```

Resources:
- Docs: https://code.claude.com/docs/en/goal
- Changelog (v2.1.139): https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md

How many times in a row have you typed "keep going"? Drop your number in the comments.

#ClaudeCode #Claude #Anthropic #SlashCommand #AICoding #AIAgents #AgenticCoding #ClaudeAI #DevTools #DeveloperTools #LLM #AICoder #AIWorkflow #ClaudeHaiku #Sonnet #Coding #Programming #v2_1_139

## Transcript

Great. There's a new slash command in Cloud Code and Haiku judges Sonnet now. It's called slash goal and it just made typing keep going obsolete. Because here's how it works. You state one completion condition. Claude does a turn, then a small fast model, Haiku by default, checks the transcript and returns yes or no with a short reason. No means keep working with that reason as guidance. Yes auto clears the goal and writes achieved. So here's what it looks like in your terminal. You type slash goal, then a condition, something like all tests in test/auth pass and the lint step is clean. Claude runs turn one. Two tests still fail. Haiku reads the transcript and returns no. Auth login still broken. That reason becomes turn two's directive. Claude fixes it. Haiku checks again. Yes. Achieved. The goal clears itself. Wait. Haiku just told Sonnet to keep working. That's the loop. And here's why it's not just another prompt. A prompt asks once. Claude answers, control returns to you and you reprompt to continue. Slash goal keeps checking. Every turn, a fresh model, not the one doing the work, judges your condition against the conversation. If you've ever typed keep going eight times in a row, this replaces all eight. So, next time you're about to type keep going for the eighth time, type slash goal instead. State the finish line once. Shipped in version 2.1.139. Quick question. How many times in a row have you typed keep going? Drop your number in the comments. If you want to learn more about AI, check out the dynamis.ai community.
