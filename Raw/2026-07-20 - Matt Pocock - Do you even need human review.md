---
title: "Do you even need human review?"
source: "youtube"
url: "https://www.youtube.com/watch?v=Yn8h5Ip-L9c"
author: "Matt Pocock"
published: "2026-07-20"
created: "2026-08-24"
duration: "0:01:59"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "context-engineering"
  - "mcp"
  - "skills"
summary: "Everyone's obsessed with automating work with engineers. And the way you do it best is to figure out where you need human review. Let's say you have a process that looks like this."
---

# Do you even need human review?

![Do you even need human review?](https://www.youtube.com/embed/Yn8h5Ip-L9c)

## Description

Learn how to strategically shift human review checkpoints in AI-powered development workflows. Discover when to involve humans early for alignment and when to let AI handle work autonomously before final review.

Learn more about /grill-me and /grill-with-docs:

https://aihero.dev/s/rEc4SQ

Keep up to date with my skills here:

https://aihero.dev/s/mcPCON

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://aihero.dev/s/ROix88

## Transcript

Everyone's obsessed with automating work with engineers. And the way you do it best is to figure out where you need human review. Let's say you have a process that looks like this. Imagine totally pre-AI where maybe you plan some work and then you ship some work and then maybe you review some work. And all of these checkpoints, all of the moments where you check the work, these are all human. A lot of people's dream, I think, is to have these all translated over to AI at once. But for me, that doesn't really make sense. On very large pieces of work, you probably want to align with the AI first. In other words, you want to be involved at the initial planning stage. That's what my skills like Grill Me and Grill with Docs and Wayfinder all do. And then you probably also want some human review right at the end before you ship it to production. However, there are some situations where you don't need that much human review at the end because maybe it's just a refactor, just an internal documentation rename. Maybe the human can just align early on, basically consider that the plan is done, and then the AI can ship it all the way to prod. That is good for some cases. There are also some cases where you can just specify the work that needs doing in like a single prompt, not bother really aligning with the AI, not bother grilling, and just let it ship through the process, and then just review it before it goes live. That can be really effective for very simple changes, very small diffs, stuff that's not going to make a big splash or a big impact, you know, just changing the color of a button or changing the name of a title or something. Even things like fix a small bug here that's just a couple of lines change, you should probably shift that checkpoint to the right. And that's the right language to use here. You shift checkpoints left for big work, for stuff you need to align on first, and you can shift it to the right for small work. The reason for that is that the smaller the diff, the easier it is to totally regenerate the code and hold it all in context. So, if you have really massive work, you want to align beforehand because fixing it is really expensive when you get to a later stage. So, that's the theory. For big work, you shift the review left. For small work, you shift the review right.
