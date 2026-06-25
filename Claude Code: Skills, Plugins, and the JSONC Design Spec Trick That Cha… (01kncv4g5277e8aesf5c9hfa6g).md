---
categories:
  - "[[Resources]]"
domain: engineering
title: "Claude Code: Skills, Plugins, and the JSONC Design Spec Trick That Changed"
source: "https://deloughry.co.uk/posts/claude-code--skills-plugins"
author: "Matthew Peck-Deloughry"
published: 2026-02-15
created: 2026-04-04
description: "How I've been using CLAUDE.md, the frontend-design plugin, and AI-generated"
tags:
  - to-process
  - agent-configuration
---

First of all, yes, I’m writing another blog post. Two in a relatively short span? Who am I? *Checks pulse.* Don’t get used to it.


![Pretend It Never Happened](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZmE3dTY0aDZ6YnV5bXFzZWlrcHU1cjF0cmQ3eTE3dGcyZmZicm9ubSZlcD12MV9naWZzX3NlYXJjaCZjdD1n/YgafgVwEDw5MV1EZRT/giphy.gif)Pretend It Never Happened
Right, so. I’ve been deep in Claude Code lately and I need to talk about it because the way I’m building tools and yes even frontends now would have made me laugh six months ago. Not because it’s funny, because if you know me I cant! It’s like asking Me to go for a jog next to a busy road and not fall over nearly killing me (yes this really happened to me).


If you’ve been vibeai assisted-coding with Claude and getting the same Inter font, purple gradient, white background output every time, this one’s for you. There’s a better way, and it involves Skills, Plugins, a well-crafted `CLAUDE.md`, and a little JSONC trick I’ve been using to get genuinely good designs out of AI.


First of all if you are reading my content I presume you should know what it is but, if you’re my mum (👋🏻 hey mum thanks for the support), or actually someone who doesn’t


Quick primer for anyone who hasn’t tried it yet: Claude Code is Anthropic’s agentic coding tool. It lives in your terminal (or VS Code, or the desktop app, or the browser) and it reads your codebase, edits files, runs commands, and generally acts like a very competent pair programmer who never gets tired (unless you run out of credits) and never judges your commit history (well for the most part more on that later).


The key thing to understand is that it’s not just a chatbot that writes code. It’s an agent. It plans, it executes, it verifies. It’ll read your files, trace through your architecture, write code across multiple files, run your tests, and commit the changes. It’s the real deal.


But out of the box, it doesn’t know *your* project. It doesn’t know your conventions, your file structure, your tooling. That’s where the good stuff starts.


![Hacker typing on a computer](https://i.giphy.com/media/YQitE4YNQNahy/giphy.gif)Hacker vibes
## CLAUDE.md: Your Project’s Memory


Here’s the thing about LLMs, they’re stateless so LLMs aren’t T-1000 they wont enslave us. Every session starts from zero. Claude Code doesn’t remember that you prefer named exports, or that your test runner is PEST not PHP Unit, or that there’s a cursed workaround in your auth module that absolutely must not be touched.


`CLAUDE.md` fixes this. It’s a markdown file that sits in your project root (or your home directory for global settings) and Claude reads it automatically at the start of every session. Think of it as your project’s persistent brain.


![Tim and Eric mind blown](https://i.giphy.com/media/xT0xeJpnrWC4XWblEk/giphy.gif)Mind blown
Run `/init` in your project and Claude will generate a starter one by scanning your codebase. It’s a decent starting point, but you’ll want to trim it down and make it yours. The key insight I’ve picked up is: **less is more**. Every instruction in your `CLAUDE.md` competes for attention with the actual work you’re asking Claude to do. Stuff it with every possible instruction and the quality of *all* of them degrades. Keep it tight.


Here’s roughly what I focus on:


* **What the project is** — a one-liner that orients Claude immediately
* **Commands** — how to build, test, lint, deploy. Claude uses these exact commands when you ask it to do things, so get them right
* **Architecture** — where things live, what talks to what
* **The gotchas** — the stuff that’ll trip it up. “Never touch X”, “Y depends on Z”, that sort of thing
* **Workflow** — how you want Claude to approach tasks. Plan first? Test-driven? Commit conventions?


That’s it. Resist the urge to put your entire style guide in there, The more you have the more of those precious tokens you will use. If your codebase already follows consistent patterns, Claude will pick up on those through in-context learning without you having to spell them out.


You can also have a global `CLAUDE.md` in `~/.claude/CLAUDE.md` for preferences that apply everywhere; your universal development standards, preferred patterns, that kind of thing. The project-level file takes priority where they overlap.


Now we’re getting to the stuff that really changed things for me. Skills are essentially instruction sets that Claude can load when they’re relevant to a task. They live in your project (in `.claude/skills/`) or come bundled with plugins, and Claude automatically picks them up when the task matches.


The concept is beautifully simple: instead of cramming everything into your `CLAUDE.md` or repeating yourself every session, you create focused skill files for specific types of work. Need Claude to follow a particular testing strategy? That’s a skill. Want it to handle database migrations a certain way? Skill. Frontend design? Oh, that’s where things get really interesting.


If you are lucky enough to have two AI tools on the go, like i’ve been I’ve found as a bonus even Cursor will pick up these skills so the party doesn’t have to stop when you use the other temptress!


## The Frontend Design Plugin: Killing the AI Slop


Let me paint you a picture. You ask Claude to build you a landing page. What do you get? Inter font. Purple gradient on white. Rounded corners on everything. Maybe a subtle shadow…no theres always shadows. It’s… fine. It’s also exactly what every other AI-generated page looks like.


![They're the same picture](https://i.giphy.com/media/l36kU80xPf0ojG0Erg/giphy.gif)They're the same picture
This happens because of something called distributional convergence (hey mum look I used my big words) the model defaults to the most common patterns in its training data. Safe choices. Inoffensive choices. Bland, forgettable choices.


The `frontend-design` plugin exists specifically to smash through this. Install it via the plugin marketplace:


Or if you want to go manual, you can grab the SKILL.md and drop it into your project:


What this does is inject a set of design principles into Claude’s context whenever it detects frontend work. It pushes Claude away from the safe defaults and towards genuinely distinctive design choices. We’re talking:


* **Typography** — no more Inter and Roboto. It steers towards distinctive, characterful font choices with intentional pairings
* **Colour** — committed palettes with dominant colours and sharp accents, not timid, evenly-distributed pastels
* **Motion** — purposeful animations, staggered reveals, scroll-triggered interactions. CSS-only where possible
* **Layout** — asymmetry, overlap, unexpected compositions. Grid-breaking rather than grid-conforming
* **Backgrounds** — layered gradients, atmospheric depth, contextual effects. Not just `background: white`


The skill literally tells Claude to “NEVER use generic AI-generated aesthetics” and to make each design unforgettable. And honestly? It works. The difference between Claude’s output with and without this skill is night and day.


![Chef kiss](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExdDd0eDN4amhvOGoyY2h6c3B4OHkyb3YwcTBibXljN3RyM3V0enN5eCZlcD12MV9naWZzX3NlYXJjaCZjdD1n/bANsiL0SX8TSjJ7aZh/giphy.gif)
Right, so here’s the bit I’m most excited about, and the thing that’s properly transformed my workflow.


I’ve been getting AI (whether that’s Claude, ChatGPT, or whatever’s to hand) to generate **design specifications in JSONC format** and then feeding those specs directly into Claude Code to build the frontend.


Why JSONC? Because it’s structured enough for Claude to parse unambiguously, but flexible enough (thanks to the comments) to carry design intent and reasoning. It bridges the gap between “here’s a vague description of what I want” and “here’s a pixel-perfect mockup” — without needing Figma or any design tool.


Here’s what one of these specs might look like:



```
{
    // Page: Landing page for developer tool
    "meta": {
        "aesthetic": "neo-brutalist",
        "mood": "confident, technical, slightly irreverent",
        "target": "developers who are tired of generic SaaS pages",
    },
    "typography": {
        "heading": {
            "family": "Space Mono",
            "weight": 700,
            // Deliberately oversized for impact
            "heroSize": "clamp(3rem, 8vw, 6rem)",
        },
        "body": {
            "family": "IBM Plex Sans",
            "weight": 400,
            "size": "1.125rem",
            "lineHeight": 1.7,
        },
    },
    "colours": {
        "background": "#0a0a0a",
        "foreground": "#e8e8e8",
        // Accent is intentionally aggressive
        "accent": "#ff3e00",
        "accentSecondary": "#00ff88",
        "muted": "#1a1a1a",
    },
    "layout": {
        "hero": {
            "style": "full-viewport, text-left-aligned",
            "elements": ["headline", "subtext", "cta-button", "terminal-mockup"],
            // Terminal mockup should feel real, not decorative
            "terminalMockup": {
                "style": "actual-terminal-aesthetic",
                "content": "showing the tool in action",
            },
        },
        "sections": [
            {
                "name": "features",
                "layout": "asymmetric-grid",
                // Three features, but NOT in equal columns
                "cards": 3,
                "style": "one large, two stacked small",
            },
            {
                "name": "code-example",
                "layout": "split-screen",
                "left": "before-code",
                "right": "after-code",
                "transition": "slide-reveal-on-scroll",
            },
        ],
    },
    "motion": {
        "pageLoad": "staggered-fade-up, 100ms delay between elements",
        "scroll": "sections reveal as you scroll, parallax on background",
        "hover": {
            "buttons": "scale(1.02) with box-shadow expansion",
            "cards": "subtle border-colour shift",
        },
    },
}
```

The beauty of this approach is in the separation of concerns. You’re doing the *design thinking* in one step deciding the aesthetic direction, the layout structure, the motion philosophy, and then handing Claude a clear, unambiguous blueprint to *implement*.


No more “make it look nice” prompts. No more back-and-forth trying to describe what you see in your head. The spec *is* the design, expressed in a format that Claude can execute precisely.


And here’s the kicker: you can use AI to generate these specs too. I’ll sit with ChatGPT or Claude (actually shoutout to  [t3.chat](%22https://t3.chat%22) here ) and say something like “I need a design spec in JSONC for a documentation site. The vibe is clean, Japanese-influenced minimalism with lots of white space. Give me typography, colour palette, layout structure, and motion design.” It’ll generate a solid spec; or if it’s something personal that will never see public use I’ll grab a design off Dribble and supply that image along with a short breakdown (don’t actually do this if you want to use it for more that yourself, Pay for a mockup if you do!).


From the results, I’ll tweak the bits I care about, and then I feed the whole thing into Claude Code with the frontend-design plugin active.


The results have been genuinely impressive. We’re talking production-quality frontends that look like a designer was involved, built in a fraction of the time.


![Not bad Obama nodding](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExaWwxbmpsOGJ2cWF3d2o5ajZtbGNlMzRnbGJ3cXZ3ZHpybGthZGF5ZyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/oAkNXcL4QOag8/giphy.gif)Not bad at all
The frontend-design skill is just one plugin. Anthropic launched the plugin marketplace in late 2025, and the ecosystem has been growing fast. Plugins can bundle together skills, subagents, MCP servers, hooks, and custom commands.


Some of the ones worth knowing about:


* **frontend-design** — the one we’ve been talking about, for distinctive UI generation
* **Code review plugins** — for automated PR reviews with your standards baked in
* **Obsidian MCP** — Claude can read and update your second brain, and use plugins in obsidian (such as the Kanban board for todos!)
* **Figma MCP** — pull designs from Figma and implement them
* **Custom plugins** — roll your own for your team’s specific workflows


Installing from the marketplace is straightforward: run `/plugins` in Claude Code, add the marketplace, browse, and install. They’re stored in `~/.claude/plugins/` and persist across sessions.


The real power move is combining multiple plugins. Frontend-design skill active, Figma MCP connected for reference designs, Obsidian integration(with Kanban plugin) for ticket context Claude suddenly has the full picture of what it’s building, why, and to what standard.


## Putting It All Together: My Workflow


Here’s how a typical feature build looks for me now:


1. **Design spec** — I generate a JSONC design spec using AI, or write one myself. This captures the aesthetic direction, layout, colours, typography, and motion
2. **CLAUDE.md** — My project already has one with the architecture, commands, and conventions
3. **Frontend-design plugin** — Already installed, automatically kicks in for UI work
4. **Prompt** — I drop the JSONC spec into Claude Code: “Build this page based on the following design spec” and let it rip
5. **Iterate** — Review the output, tweak the spec or give direct feedback, and Claude refines


The whole loop from “I have an idea for a page” to “this is deployed” has gone from days to hours. And the quality is consistently higher than what I was getting with traditional vibe-coding prompts.


![Cat typing fast on keyboard](https://i.giphy.com/media/JIX9t2j0ZTN9S/giphy.gif)Speed coding
## It’s a Two-Way Street (Yes, the AI Is Better at Communicating Than You)


Here’s the thing nobody tells you about Claude Code: it’s not just waiting around for your instructions like some obedient little terminal butler. It *talks back*. And honestly? It’s usually right to.


When you give Claude a vague prompt, let’s be honest, my first drafts are usually somewhere between “make it good” and incoherent dyslexic ramblings that read like I typed them while falling down the stairs, Claude will ask clarifying questions. “What framework are you using?” “Should this be responsive?” “Do you want dark mode?” It’s not being difficult. It’s doing what a good colleague would do: making sure it actually understands what you want before burning through tokens building the wrong thing.


![Dog sitting at computer, this is fine](https://i.giphy.com/media/QMHoU66sBXqqLqYvGO/giphy.gif)Me reading my own prompts back
But here’s where it gets *really* good, and the bit that genuinely levelled up my workflow: **you can ask Claude for advice on how to work with it better.**


I know. Asking an AI how to talk to it sounds like the tech equivalent of asking your sat nav for relationship advice. But it works. I started doing things like:


* “How could I have structured that prompt better?”
* “What information were you missing that would have helped you get this right first time?”
* “Can you suggest a better way to describe what I want for next time?”
* “Roast my CLAUDE.md — what’s useless in here?”


And Claude will straight up tell you. No ego, no sugar-coating (well, okay, maybe a little sugar-coating, it’s super polite). It’ll say things like “if you’d specified the component library upfront I wouldn’t have defaulted to custom CSS” or “your architecture section says nothing about how routing works, which is why I kept getting it wrong.”


It’s humbling, honestly. I’ve been writing code for years and an AI is sat there going “mate, your instructions are rubbish”, and it’s *spot on*. My prompts have improved more from Claude’s feedback than from any blog post or course on prompt engineering. Including, ironically, this one.


The two-way street works both ways. Let Claude ask you questions at the start of a task, don’t just word-vomit through with “build the thing now.” And when it’s done, ask it what *you* could have done better. Swallow your pride. It stings a little knowing that an AI is judging you hard, but your code (and your prompts) will be better for it, And just remember back to your Jnr dev days, the advice is being given to improve not to stun the growth.


Think of it less like giving orders to a tool and more like pair programming with someone who’s smarter than you but too polite to say it. Because that’s basically what it is. And the sooner you accept that, the sooner you stop fighting the process and start getting genuinely great output.


![Man pointing to his head, thinking smart meme](https://i.giphy.com/media/d3mlE7uhX8KFgEmY/giphy.gif)Work smarter, not harder... for once
## Tips I’ve Picked Up Along The Way


A few things I’ve learned the hard way so you don’t have to:


**Keep your CLAUDE.md lean.** Every line competes for attention. If it’s not something Claude needs to know for *every* task, it probably doesn’t belong there.


**Use `/init` as a starting point, not an endpoint.** The generated file is always too verbose. Cut aggressively.


**The `#` shortcut is your friend.** In Claude Code, typing `#` followed by a note adds it to Claude’s memory for the session. Great for quick corrections without editing your CLAUDE.md.


**JSONC specs beat natural language for design.** Every time. The structure removes ambiguity, the comments carry intent. It’s the sweet spot between a Figma mockup and a text description.


**Combine the frontend-design skill with specific aesthetic direction.** The skill stops Claude from defaulting to generic choices, but you still need to tell it *what* direction to go. “Build a dashboard” plus the skill is good. “Build a dashboard with this JSONC spec” plus the skill is exceptional.


**Run `/plugins list` regularly.** The ecosystem moves fast. New plugins drop frequently and some of them are properly game-changing.


Look, I know “AI coding tool changes everything” is the most played-out headline in tech right now. But the combination of Skills, a well-maintained `CLAUDE.md`, the frontend-design plugin, and the JSONC design spec workflow has genuinely shifted how I build things. It’s not about replacing the thinking, it’s about expressing your thinking in a format that lets AI execute it brilliantly.


The JSONC spec approach in particular feels like a genuine unlock. It turns “vibe coding” into something more like “spec coding” you’re still moving fast, but with precision and intention behind every decision.


Give it a go. And if you come up with a better spec format than JSONC, I’m all ears.


Now, how long until my next blog post? Don’t ask. 🤫


![Elmo waving goodbye with fire behind him](https://i.giphy.com/media/yr7n0u3qzO9nG/giphy.gif)See you next time... whenever that is