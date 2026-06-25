---
categories:
  - "[[Resources]]"
domain: engineering
title: "WebMCP — The Web Just Got a Bit Smarter (Whether It Wanted To or Not)"
source: "https://deloughry.co.uk/posts/webmcp-the-web-just-got-a-bit-smarter/"
author: "Matthew Peck-Deloughry"
published: 2026-02-19
created: 2026-04-04
description: "WebMCP is Google's browser-native API that lets sites expose tools AI agents"
tags:
  - to-process
  - agent-plugins-mcp
---

>  As with all my technical documents, I like to preface the articles, that I don’t pretend to be a master in said topic, nor always do stuff the best way, these articles are here as a documentation of my exploration, and if you find this useful then awesome! If you see something you want to discuss please hit me up on twitter as I’m always up for a good chat!
> 
>  


Another week another, yet another blog post boy do I spoil you! Well spoil in a strong word to use here, maybe torture?! I’ll let you decided on that. What started as me seeing “WebMCP” shoot along on my feeds at ‘alf eleven at night, when the household has 1 under 1 surely I should absolutely should have been asleep. Well whatever happened, happened and a quick article read turned into about three hours of reading specs and going “o’riiiight that’s actually quite smart”.


![Should be sleeping ](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExd2ozZzJ2a29kYjJrNm5jMGFxcGs4cmtic3Jja3VkN3JiMWN2Z2JoMSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/akRvoiZ1gCgo/giphy.gif)Should be sleeping 
So grab a brew, I’m going to have a chat about i now


## First, a quick bit of context (bear with me)


If you’ve been anywhere near the AI/developer space over the last year or so, you’ll have heard of MCP (if you haven’t some would say you’re a luck sod), [Anthropic’s **Model Context Protocol**](https://www.anthropic.com/news/model-context-protocol). It’s basically the way AI agents talk to backend services in a efficient and structured way. Your Claude Desktop can connect to a filesystem, a database, a Slack workspace, whatever has a MCP server you can connect to it, because they all speak the same language. It’s the AI equivalent of DLC (hopefully with less loot boxes down the line)


MCP lives on the backend. It needs a server some can be hosted locally but still needs a port to be taken up on your machine, It needs you to write Python or Node just to expose your app’s functionality. And honestly? That’s fine for big enterprise stuff, but for those of us building websites day to day, it’s a bit of a faff.


That’s where WebMCP walks in, sits down uninvited, and starts making itself at home…wait I can tell who built this…


![Suspicious](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExMWFoYzFlYWI2eWQydW8zaWQxY2x3aThocTIwMGh3OXI3bXVwbTZrbSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3gNotAoIRZsb9UHPnj/giphy.gif)
## So what actually *is* WebMCP?


WebMCP, announced by Google in early preview on February 10th, 2026 (literally last week as I write this…if I released it on time) is a browser-native JavaScript API that lets you expose your website’s functionality as structured **tool set** that AI agents can call directly.


Think of it like this. Right now, if an AI agent wants to interact with your website it basically… squints at it.


![](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExamt3bWRoZXhkbG1remRlMnc3b21ucjUyNXV4bnZ1d2RwbDFjamNjcyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/80mXWlPqTSU1y/giphy.gif)
It takes a screenshot, runs it through a vision model, guesses where the “Submit” button probably is, synthesises a click, and hopes for the best, heck may even scrape the site but only if robots.txt allows it (well it should listen to robots.txt…unlike some ai bot crawlers). It’s a bit like asking someone who’s never seen a car before to do your MOT, it’s going to a be a long process and will get it wrong somewhere down the line.


WebMCP flips that on its head. Instead of the agent guessing, *you* tell it what your site can do. Your site publishes a kind of “tool contract” here are the things I support, here’s how to call them, here’s what I’ll give back.


This is a theoretical example of my site.



```
// tools/playlists.ts — your single source of truth

export const playlistTools = {
  "find-playlist-by-year": {
    name: "find-playlist-by-year",
    description: "Find Matt's Spotify Jams playlist for a specific year. Each year has a themed title reflecting life events.",
    inputSchema: {
      type: "object",
      properties: {
        year: {
          type: "string",
          description: "The year to find a playlist for",
          enum: ["2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025", "2026"]
        }
      },
      required: ["year"]
    },
    // Pure logic — no browser or server dependencies
    execute: async ({ year }: { year: string }) => {
      const playlists = await getPlaylists(); // shared data fetcher
      return playlists[year] ?? { error: "No playlist found" };
    }
  },

  "get-all-playlists": {
    name: "get-all-playlists",
    description: "Get all of Matt's Spotify Jams playlists with track counts and life milestone titles",
    inputSchema: {
      type: "object",
      properties: {}
    },
    execute: async () => {
      return await getPlaylists();
    }
  },

  "find-playlist-by-mood": {
    name: "find-playlist-by-mood",
    description: "Find a playlist based on a life event or vibe — e.g. 'wedding', 'lockdown', 'new beginnings', 'baby'",
    inputSchema: {
      type: "object",
      properties: {
        query: {
          type: "string",
          description: "A mood, vibe, or life event to match against playlist titles"
        }
      },
      required: ["query"]
    },
    execute: async ({ query }: { query: string }) => {
      const playlists = await getPlaylists();
      const matches = Object.values(playlists).filter(p =>
        p.name.toLowerCase().includes(query.toLowerCase())
      );
      return matches.length ? matches : { error: "No matching playlist found" };
    }
  }
};
```

And suddenly instead of an agent spending 15 token-gobbling roundtrips fumbling through your UI, it makes one clean function call and gets structured JSON back. Lovely.


There’s a **Declarative API** for the straight forward stuff if you’ve got well-structured HTML forms on site you’re pretty much most of the way there. Slap some extra attributes on and agents can start using them. If your forms are clean (and let’s be honest, mine are… *fiiiiiine*, some of the time, don’t look too closely) you’re already like 80% done.


Then there’s the **Imperative API** for the more complex stuff like the example above, but also dynamic interactions, multi-step flows, anything that needs JavaScript to do its thing. That’s where `registerTool()` comes in and you define the full schema yourself. [Wes Bos of Syntax fame](https://www.youtube.com/watch?v=sOPhVSeimtI) had a good lil’demo of how to use it which recommend watching to see a example of a working example


## ”But Matt, isn’t this just MCP with glasses, big nose and moustache?”


Alright look, I asked myself the same thing. Spoiler: it’s not, but also kind of yes and the naming is going to cause SO much confusion.


WebMCP doesn’t follow the JSON-RPC spec that MCP uses. It runs entirely client-side in the browser. It shares the conceptual model, tools with schemas that agents can call, but it’s a completely different beast. The analogy I’ve seen floating around is “Java and JavaScript”, which again isn’t right and 100% accurate at the same time.


The key thing is they’re **complementary, not competing**. Your big enterprise travel booking site might have a full backend MCP server for direct Claude/ChatGPT integrations, *and* WebMCP tools on the consumer-facing site for when someone’s using a browser agent. Two different interaction patterns but 100% are both useful.


## Why should we actually care about this right now?


Alright this is early preview, It’s barely just got out of bed let alone just out the door. The spec is still being worked on by the W3C Web Machine Learning Community Group, so it’s going to be a while yet we even get a robust polyfil that wont break every 20 minutes. So why am I writing about it now?


Because I’ve seen this pattern before. Webmentions felt niche and weird until suddenly every personal site wanted them, I even wrote [about them](https://deloughry.co.uk/posts/integrating-webmentions-with-next-js/)(ooh don’t often get to self plug ). Structured data felt like extra homework until it became an SEO necessity. The devs who played with this stuff early were the ones who actually understood it when it mattered.


And the agentic web is coming whether we like it or not. AI assistants are already browsing on people’s behalf. The question is whether your site is going to be the one those agents interact with cleanly and confidently, or the one they fumble around on, hallucinate a button press, and give up.


On top of that and I genuinely hadn’t thought about this until I was falling fast down the rabbit hole on it, there’s a real **accessibility win** here too. The same tools that let an AI agent book a flight could let assistive technologies offer users higher-level actions on complex pages. That’s not a side effect, it’s baked into the spec’s goals.


It’s not all sunshine and well-typed function signatures though. There’s a genuinely scary architectural problem that’s been called [“the lethal trifecta”](https://martinfowler.com/articles/agentic-ai-security.html#lethal-trifecta) One that your Gran could easily find them (heck even I know even competent people to be caught out with stuff like this, so I’ll cut Granny some slack here).


Imagine you’ve got two tabs open. One is your bank. One is a dodgy site. A browser agent has context from both. The malicious tab could, in theory, instruct the agent to extract data from your banking tab, or worse, push the other way. It’s not theoretical. It’s architecturally almost inevitable with how browser agents work today, and WebMCP alone doesn’t solve it.


Security-wise, this is a space to watch and tread super carefully.


## How do I have a play?


Google’s Chrome early preview program is open for sign-ups over at the Chrome for Developers site. It’s early days, you’ll be prototype territory for now but honestly that’s the best time to get your hands on something like this. You can see how LLMs interpret your tool descriptions, find out which ones are too vague, and iterate before this becomes a standard everyone’s scrambling to implement at the last minute.


There’s also [webmcp.dev](https://webmcp.dev) and [docs.mcp-b.ai](https://docs.mcp-b.ai) for the MCP-B polyfill side of things, which bridges WebMCP into a spec-compliant MCP implementation running browser-side. Very clever work.


WebMCP isn’t going to change your site overnight. It’s a spec still finding its feet, the tooling is early, and half the industry is going to spend the next six months arguing about whether it conflicts with MCP (it doesn’t, mostly, the name is just unfortunate).


But the direction it’s pointing is genuinely exciting. The web becoming a first-class citizen in the agentic AI world and not something agents have to throw something at hope it sticks, but something that can actively communicate its own capabilities. and to me that’s a good thing.


A thing worth understanding early.


Right. I’m going to go and add `registerTool()` to this very website and see what breaks. Updates to follow, probably with a gif of something going catastrophically wrong.


![](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOXNxeWhrMXQ3dXh1cjZuejNxODczc29iODVxNm1uN2xjMzAzNW1rZiZlcD12MV9naWZzX3NlYXJjaCZjdD1n/3oKIPwoeGErMmaI43S/giphy.gif)
*If you found this useful, let me know! I’m [@dr\_dinomight](https://twitter.com/dr_dinomight) on Twitter/X, come say hello.*