---
title: "Claude Code's system tools are SO BLOATED"
source: youtube
url: https://www.youtube.com/watch?v=oLx4yCbeklQ
author: "Matt Pocock"
published: 2026-07-16
created: 2026-08-24
duration: "0:01:38"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# Claude Code's system tools are SO BLOATED

![Claude Code's system tools are SO BLOATED](https://www.youtube.com/embed/oLx4yCbeklQ)

## Description

Learn how to dramatically reduce unnecessary bloat in Claude Code's system prompt by disabling unused features and tools. In this video, I show you how to drop your system prompt size from 25,000 tokens down to just 8,000 by customizing your global settings.json file.

The guide: https://aihero.dev/s/D9UXCK

Keep up to date with my skills here:

https://aihero.dev/s/fCJUhY

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://aihero.dev/s/MVQJ5M

## Transcript

Most harnesses, but especially Claude Code, ship with a ton of bloat in the system prompt. There is very likely thousands and thousands of tokens of stuff you're not using in your system prompt. So, when I did mine, I found that I had an whole stuff with workflow, with design sync, with monitor, that I simply wasn't using. And that is about, you know, 8,000, 10,000 tokens per request. Fortunately, Claude Code allows you to customize this stuff, so you can actually put this in your global settings.json file, and you can disable all sorts of useless stuff. So, I didn't want it to control when I entered and exited plan mode. So, I just disabled those tools, and the tool definitions get removed from the system prompt. I personally really hate the ask user question tool, so I never use it, or I never want to see it, and so I just removed the tool definition from Claude system prompt. Equally, I don't want it to schedule crons for me, so I just deleted those as well. I don't use the custom code review skill that ships with it, so I disabled the bundled skills. I disabled everything to do with dynamic workflows. I don't use those either. I even disabled remote control, because there was a lot actually in the system prompt for that. Disabled Claude AI connectors, which were burning a ton of tokens I didn't even realize. And I disabled the artifacts feature. All of that means that I dropped my initial starting system prompt, or the system tools, from 25K down to around 8K. I put this in an article so that you can use a proxy to see what you're actually shipping, which is really, really useful. Then, you can tune the settings to choose just the bits of the system prompt that you need. The less you send over the wire, the better your outputs are going to be, because the agent has less stuff distracting it.
