---
title: "I Built 63 Design Skills For Claude - and They're Free"
source: "https://marieclairedean.substack.com/p/i-built-63-design-skills-for-claude"
author: "MC Dean"
published: 2026-03-09
created: 2026-03-25
description: "Teaching AI what designers know so it can work with us, not around us."
tags:
  - to-process
  - design-automation
---

[Code & Projects](https://marieclairedean.substack.com/s/code-and-projects/?utm_source=substack&utm_medium=menu)


### Teaching AI what designers know so it can work with us, not around us.


[![](https://substackcdn.com/image/fetch/$s_!SaPV!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb21c747-91ae-482e-8952-40dedf683600_7111x7111.jpeg)](https://substackcdn.com/image/fetch/$s_!SaPV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Feb21c747-91ae-482e-8952-40dedf683600_7111x7111.jpeg)Photo by Google DeepMind: https://www.pexels.com/photo/an-artist-s-illustration-of-artificial-intelligence-ai-this-image-depicts-how-ai-tools-can-democratise-education-and-make-learning-more-efficient-it-was-created-by-martina-stiftinger-a-18069231/
I’ve been writing about how design is changing in the AI era. About how the processes we rely on are failing us. About how the craft is getting serious again.


This week I did something different. I stopped writing about the shift and started building for it.


I created an open-source collection (with my friend Claude) of 63 design skills and 27 commands for Claude Code. They’re organised into 8 plugins that cover the full breadth of what designers typically do: research, systems, strategy, UI, interaction design, prototyping and testing, design ops, and the everyday toolkit stuff like writing rationale and building case studies.


It’s called the Designer Skills Collection, and it’s [free on GitHub](https://github.com/Owl-Listener/designer-skills).


## Why this exists


Most AI tools treat design as image generation. That’s never been what design is.


Design is knowing when to run a heuristic evaluation instead of a usability test. It’s understanding that a design token isn’t just a hex code: it’s a decision about how a system scales. It’s writing a problem statement that’s specific enough to be useful and broad enough to leave room.


None of that knowledge existed inside Claude so I taught it.


Each skill is a structured markdown file that gives Claude deep, specific knowledge about a design domain. When you ask Claude to help you create a user persona, it doesn’t guess. It draws on the same frameworks an experienced researcher would: demographics, goals, frustrations, behavioural patterns, context of use. When you ask it to audit a design system, it works through token coverage, naming consistency, accessibility compliance, and theming support.


The commands chain these skills together into workflows.


Type `/discover` and Claude runs a full research discovery cycle. Type `/strategize` and it builds a UX strategy from vision through to metrics. Type `/handoff` and it generates a developer handoff package with measurements, behaviours, edge cases, and a QA checklist.


## What I learned building it


Building this taught me something I wasn’t expecting.


The act of encoding design knowledge (I mean really encoding it, not summarising it) forces you to articulate what you actually know. What’s essential to a component spec versus what’s habit. What makes a design principle genuinely useful versus decoratively aspirational. Where your expertise is deep and where it’s shallow.


It’s a strange kind of audit. Not of a design system, but of yourself as a designer.


I also learned that the structure matters more than the content. Claude doesn’t need paragraphs of theory. It needs clear frameworks, decision criteria, and an understanding of when to apply what. The skills that work best are the ones that mirror how an experienced designer actually thinks through a problem, not how a textbook explains it.


## This isn’t about replacing designers


I want to be clear about what this is and isn’t.


This isn’t a replacement for design judgment. It’s an amplifier for it. A junior designer using these skills will get better scaffolding. A senior designer will get a faster starting point for the parts of their work that are structurally predictable, freeing up attention for the parts that aren’t.


The creative leaps, the taste, the intuition, the ability to read a room and know which research finding actually matters…that’s still ours. But the frameworks, the checklists, the structural knowledge that we carry around in our heads and deploy when needed? That can be shared with a tool that’s already in our workflow.


## How to use it


You’ll need [Claude Code](https://code.claude.com/docs) — Anthropic’s agentic coding tool that works in your terminal, VS Code, or browser. If you haven’t used plugins before, the [marketplace guide](https://code.claude.com/docs/en/discover-plugins) walks you through it. Once you’re set up, add the collection:


/plugin marketplace add Owl-Listener/designer-skills


Then browse and install whichever plugins you want through the /plugin menu. If you just want to look at the structure, everything is on [GitHub](https://github.com/Owl-Listener/designer-skills).


It’s MIT licensed. Use it, fork it, improve it. If you build a skill that’s missing, I’d genuinely love a contribution.


Here’s a few examples:


**1. Run a full research discovery cycle** type **/design-research:discover** then tell Claude: *"I'm designing a habit-tracking app for people recovering from burnout. Run a full discovery cycle — personas, empathy map, and journey map."*


**2. Generate an accessible colour palette** type **/ui-design:color-palette**: then tell Claude: *"Create a colour system for a health and wellness brand. I need primary, secondary, neutral, and semantic colours, all passing WCAG AA."*


**3. Build a developer handoff package** type **/design-ops:handoff**: then tell Claude: *"Generate a handoff spec for a settings page with a profile section, notification preferences, and a danger zone for account deletion."*


**4. Run a heuristic evaluation** type **/prototyping-testing:evaluate**: then tell Claude: *"Run a heuristic evaluation of a checkout flow with these steps: cart review, shipping address, payment, and confirmation. Flag usability issues by severity."*


**5. Write a case study for your portfolio** type **/designer-toolkit**: write-case-study: then tell Claude: *"Help me write a portfolio case study. The project was a redesign of an internal dashboard for a logistics company. We reduced task completion time by 40%. Walk me through the full structure."*


Each one gives you something tangible in a few minutes: a full persona set, a production-ready colour system, a handoff doc engineers can actually use.


## What’s next


I’m curious what happens when designers start encoding their own knowledge this way. Not just using AI, but teaching it. Shaping what it knows about our discipline so that when it’s asked a design question, the answer reflects real craft and not a surface-level approximation.


Obviously (need I say) this is no workaround for having experienced researchers and designers on your team.


If you try it, I’d love to hear what works, what’s missing, and what you’d build differently.


*The opinions expressed in this article are solely those of the author and do not reflect the official position of any institution or organization.*



PreviousNext


### Ready for more?


Subscribe