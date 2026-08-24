---
title: "Delete (most of) your docs"
source: "youtube"
url: "https://www.youtube.com/watch?v=Fj8DKMbdIzU"
author: "Matt Pocock"
published: "2026-07-16"
created: "2026-08-24"
duration: "0:02:04"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "skills"
summary: "There's this really annoying pattern that I see people do everywhere that I think is making their AI coding output worse, not better, and costing them tokens. Now, most of the time when I let AI explore my codebase, the only thing AI has to go on is the code itself. And it the code is supposed to be sort of self-explanatory."
---

# Delete (most of) your docs

![Delete (most of) your docs](https://www.youtube.com/embed/Fj8DKMbdIzU)

## Description

Stop Using Documentation as Your Codebase's Source of Truth. Learn why creating excessive documentation for AI to rely on is an anti-pattern that costs tokens and creates confusion.

https://aihero.dev/s/36jQdK

Keep up to date with my skills here:

https://aihero.dev/s/GwyLek

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://aihero.dev/s/6CJeAF

## Transcript

There's this really annoying pattern that I see people do everywhere that I think is making their AI coding output worse, not better, and costing them tokens. Now, most of the time when I let AI explore my codebase, the only thing AI has to go on is the code itself. And it the code is supposed to be sort of self-explanatory. It's supposed to be have enough information in the code so that AI can interpret it. That puts a lot of burden on my code, so I need to make sure my code is well-formatted, that it's in the right file systems, that it's organized into reasonable chunks so the AI can look at it, that there's interfaces and implementations and they're separated so AI can just take what it needs. However, a lot of folks are not doing this. They are taking a layer of docs, so they're creating docs for their code and getting the AI to primarily rely on those docs. The issue I have with this is those docs, like markdown files inside the repository, they're usually not executable. They're not testable against the code. And so they can drift away from the code. The docs can say one thing, but the actual code, the source of truth, can say another. And this is really bad because if there are two sources of truth and they conflict, then AI won't know which one is the real one. And so I consider this a really, really big problem and a massive antipattern to build this whole layer of docs just to explain what the code can anyway. Now, some people will read this and think that I'm against all docs, that the only thing you should have in your repo is code. No, that's not true. Code should be self-explanatory, but there are some things that code can't explain. code can't tell you what alternatives were considered instead of the code that's there. And so you need architectural decision records in your repo to capture those. It also can't really explain the domain language that you're using to work with your code. Does it know what an order is in your codebase? Probably not. And so a glossary is extremely helpful. And finally, a thin layer of docs just to navigate around the main aspects of your code is really helpful just to speed up AI's exploration of your code. But the concept of docs as the source of truth, as the thing that you read to understand the code, no, I don't like that at all.
