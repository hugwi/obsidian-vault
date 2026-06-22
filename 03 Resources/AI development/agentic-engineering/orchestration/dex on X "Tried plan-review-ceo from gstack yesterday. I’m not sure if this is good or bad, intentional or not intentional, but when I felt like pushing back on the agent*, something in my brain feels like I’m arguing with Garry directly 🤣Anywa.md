---
title: "dex on X: \"Tried plan-review-ceo from gstack yesterday. I’m not sure if this is good or bad, intentional or not intentional, but when I felt like pushing back on the agent*, something in my brain feels like I’m arguing with Garry directly 🤣Anyways milestone 1 of a big feature shipping\""
source: "https://x.com/dexhorthy/status/2034651637407687062"
author:
  - "[[x.com]]"
published: 2026-03-19
created: 2026-06-07
description:
tags:
  - "to-process"
  - orchestration
---
Tried plan-review-ceo from gstack yesterday. I’m not sure if this is good or bad, intentional or not intentional, but when I felt like pushing back on the agent\*, something in my brain feels like I’m arguing with Garry directly 🤣

Anyways milestone 1 of a big feature shipping with RPI/QRSPI + Gstack shipping today, will report back

\* (which @garrytan had stated is part of the process - “your job is to know when the model is gassing you up and call it out” or something)

I have some technical concerns with the sheer volume of instructions in the prompt and the amount of adherence you will actually get (@0xblacklight cited an interesting arxiv paper in post linked below) - I think we might be better served by a router that routes to specific modes, rather than explaining every single mode in a single monolithic prompt, but there’s tradeoffs to consider in plumbing and Ux for the end user.

I think some may complain that it’s overly verbose and thoughtful and brings up things that are irrelevant but I actually think that’s good. I want a clean braindump of everything that might be relevant so I can edit and prune down to just what’s important

---

[https://humanlayer.dev/blog/writing-a-good-claude-md…](https://humanlayer.dev/blog/writing-a-good-claude-md%E2%80%A6)

![Image](https://pbs.twimg.com/media/HDyM0WgaUAAQgas?format=jpg&name=large)

---

Overall there are n thousand ways to throw more tokens at the problem and we need better ways to eval “review this plan and find all the things I didn’t think about” vs a 100+ instruction monolithic mega prompt

---

## Comments

> **agusti @bleuonbase** · [2026-03-19](https://x.com/bleuonbase/status/2034731204855894023)
> 
> workflow/state machines are a much better solution than hoping the deterministic llm to play nice all the time

> **Luong NGUYEN @luongnv89** · [2026-03-19](https://x.com/luongnv89/status/2034664450314154004)
> 
> it is true that gstack is very token hungrry, you are the right person to fix it.
> 
> in the mean time, if we try very hard to limit the token, it could be like: find me the latest trending on X, but do not use internet.

> **Shard @madarasama17** · [2026-04-27](https://x.com/madarasama17/status/2048809213565256072)
> 
> lol yeah the “arguing with garry” thing is real… once the voice feels authoritative your brain just stops questioning it. also +1 on the monolithic prompt concern, we went down that path and it looks smart but adherence gets fuzzy fast splitting into modes ended up way more
> 
> [hud.io Hud | Runtime Code Sensor for Production-Safe AI Code](https://t.co/V8joX9avPW)

> **Nicholas Bardy @NicholasBardy** · [2026-03-19](https://x.com/NicholasBardy/status/2034662253568667918)
> 
> "too many instructions" is why I agree with the "llm psychosis" crowd
> 
> People finally realize how powerful LLMs are, Adapt their workflows to work better with them, accelerate even harder.
> 
> And then... They attribute it all to some mega prompt they stuffed a bunch of stuff in,