---
title: "Claude Wrote 50 Features. None of Them Worked Together"
source: youtube
url: https://www.youtube.com/watch?v=c-fqGHGh5_o
author: "Better Stack"
published: 2026-05-18
created: 2026-08-24
duration: "0:01:29"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# Claude Wrote 50 Features. None of Them Worked Together

![Claude Wrote 50 Features. None of Them Worked Together](https://www.youtube.com/embed/c-fqGHGh5_o)

## Description

*No description.*

## Transcript

Everyone is shipping at 10x speed because of five coding, but one developer found hand coding much better [clears throat] because of three big mistakes AI kept making over and over again. Shiv Bosal built K10s, a GPU aware Kubernetes dashboard like K9s, but for people running Nvidia clusters. He five coded the whole thing with Claude over seven months and each feature landed clean in a single session, but it all collapsed the moment he tried to use everything together. Switching views showed stale data, once populated tables were empty, and one key did three different things depending on which screen you were on. So he archived the entire code base and started again from scratch with the aim of avoiding the three big things that AI did to mess up his first attempt. One, AI builds features not architecture, meaning every prompt adds a feature and none of them know about the 49 other features sharing the same state. So he wrote the architecture himself by hand, put it in the Claude MD file, and got AI to do the boring task. Two, the god object is the default. AI always tries to take the shortest path like stuffing everything into a single struct or object known as the god object. So he avoided this by making sure the LLM split things into different views. Three, velocity tricks you into scope creep. Whenever a feature takes just one session, it feels free, so you keep adding more and more, which could result in AI rebuilding things you've already built before. So to fix this, he wrote down exactly who he wasn't building for and put scope boundaries inside the Claude MD file. This resulted in him having a much better project and an article that went viral on Hacker News. Subscribe for more AI tips.
