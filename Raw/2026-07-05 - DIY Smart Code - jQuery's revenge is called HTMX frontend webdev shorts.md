---
title: "jQuery's revenge is called HTMX #frontend #webdev #shorts"
source: "youtube"
url: "https://www.youtube.com/watch?v=A9nSfCFgQ3U"
author: "DIY Smart Code"
published: "2026-07-05"
created: "2026-08-24"
duration: "0:01:08"
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
  - "video-gen"
summary: "React isn't the only way to build a modern web app anymore. This is HTMX, and one company rewrote their React app with it and deleted 67% of their code. React plus React DOM ship before your app does anything."
---

# jQuery's revenge is called HTMX #frontend #webdev #shorts

![jQuery's revenge is called HTMX #frontend #webdev #shorts](https://www.youtube.com/embed/A9nSfCFgQ3U)

## Description

HTMX explained — and put on trial. Is HTMX really killing React, or is it just jQuery with better marketing? This is the honest HTMX vs React verdict: what HTMX actually is, the four hx- attributes that are the whole language, why returning HTML instead of JSON revives real REST, and the receipts — one company cut 67% of their code and dropped from 255 JavaScript dependencies to 9. Then we settle the fight in the comments section, steelman the critics, and tell you exactly when NOT to use it.

----
🚀 DYNAMOUS AI COMMUNITY

Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount

⚡ HOSTINGER — RELIABLE HOSTING FOR YOUR PROJECTS (10% OFF)

Whether you're shipping a portfolio, a side project, n8n flows, or AI agents — I use Hostinger for fast, affordable VPS + web hosting.

Get 10% off here 👉 https://hostinger.com/DIYSMARTCODE

(Affiliate link — costs you nothing, supports the channel.)
----

Chapters
0:00 Is "Dumb HTML" Really Killing React? (67% Less Code)
0:24 What HTMX Actually Is: One Attribute Instead of Five
1:05 The Weight: HTMX 16KB vs a React SPA
1:47 The Four hx- Attributes: The Whole Language
2:40 Hypermedia & Real REST: Why HTML, Not JSON
3:25 The Receipt: Contexte Cut 67% of Their Code
4:36 The HOWL Stack: Any Backend, Plus Alpine & Turbo
5:27 The Comments War: AJAX Reinvented? Is "No JS" a Lie?
6:20 When NOT to Use HTMX (React's Home Turf)
7:08 The Verdict — Breakthrough or jQuery 2.0?

What you'll get in this ~8-minute breakdown:
- The proof first: a real hx-get button updating the page with zero JavaScript you wrote — before any explanation
- What HTMX actually is: instead of a component + state + a fetch call + a JSON endpoint + a re-render, you add one attribute and let plain HTML talk to the server
- The weight comparison: HTMX ships around 16KB with zero dependencies, versus React + React-DOM before your app does anything, versus the hundreds of KB of a real single-page app
- The whole language in four attributes — hx-get/hx-post (where), hx-target (which element), hx-swap (how), hx-trigger (when) — on any element, any event, any HTTP verb
- Why HTML beats JSON: the server sends the next actions baked into the markup — hypermedia — which is real REST the way Roy Fielding actually defined it, before the word got hijacked to mean "a JSON API"
- The receipts: Contexte rewrote their React app in HTMX and cut 67% of their code, dropped from 255 JS dependencies to 9, and cut build times ~90% — with 48k GitHub stars behind it
- The HOWL stack (Hypermedia On Whatever you'd Like): Django, Flask, FastAPI, Rails, Laravel, Go, Express — plus tiny partners like Alpine.js and Hyperscript, and how it compares to Rails' Hotwire and Turbo
- The honest debate from the comments: "isn't this just AJAX and jQuery reinvented?", "'no JavaScript' is a lie", and the real technical one — every action is now a network request
- When NOT to use it: spreadsheets, real-time maps, offline apps, thousands of interdependent widgets — that's React's home turf, and it isn't close

Resources:
- HTMX (official site + docs): https://htmx.org
- Essays by Carson Gross (creator of HTMX): https://htmx.org/essays/
- HTMX on GitHub: https://github.com/bigskysoftware/htmx
- Hypermedia Systems (free book): https://hypermedia.systems/

So here's the real question — the one the whole internet is arguing about: Is HTMX a genuine breakthrough, or just jQuery with better marketing? Drop your verdict in the comments.

#HTMX #HTMXvsReact #React #WebDevelopment #JavaScript #FrontendDevelopment #Hypermedia #REST #CarsonGross #HOWLStack #Django #Flask #Rails #Alpinejs #Hotwire #WebDev #Programming #SoftwareEngineering #FullStack #HTMLFirst #NoBuildStep #DevTools #CodingTutorial #HTMXTutorial

## Transcript

React isn't the only way to build a modern web app anymore. This is HTMX, and one company rewrote their React app with it and deleted 67% of their code. Start with the weight. React plus React DOM ship before your app does anything. HTMX is about 16 kilobytes with zero dependencies, and the whole language is just four attributes. Where to send the request, which element changes, how to swap the response in, and when to fire it. Any element, any event, any HTTP verb. The trick? The server sends back HTML, not JSON. The page carries its own next actions. That's real REST, the way it was originally defined. It's how Context dropped from 255 JavaScript dependencies down to nine. So, is it just jQuery reinvented? Kind of, but turned into a clean declarative system. It's not magic, though. Every action is now a network request, and for spreadsheets or offline apps, you still reach for React. So, is HTMX a real breakthrough or just jQuery with better marketing? I break down the whole debate in the full video. Link is right here.
