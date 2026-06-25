---
categories:
  - "[[Resources]]"
domain: engineering
title: "I Replaced $90/Month in AI Coding Tools With 3 Free GitHub Repos. Here's the"
source: "https://webafterai.substack.com/p/i-replaced-90month-in-ai-coding-tools"
author: "Shilpa Mitra"
published: 2026-05-19
created: 2026-05-24
description: "9router + agentmemory + agent-skills. Built a Full SaaS App in 5 Sessions,"
tags:
  - to-process
  - agent-tools
---

[![](https://substackcdn.com/image/fetch/$s_!iffg!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b2a158f-190a-4a14-9e9b-3cace9ad8ec1_1536x1024.png)](https://substackcdn.com/image/fetch/$s_!iffg!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7b2a158f-190a-4a14-9e9b-3cace9ad8ec1_1536x1024.png)
 *Last week I shared 7 GitHub repos that replace $1,380/month in AI subscriptions in my subreddit. That post hit 80K+ views, 1600+ shares, and hundreds of upvotes on Reddit. A lot of you asked: “Cool list, but how do these actually work together in practice?”*


*This is the answer. Today I’m walking you through a complete zero-cost AI coding stack, step by step. No subscriptions. No API keys. No “it depends.” Just three repos chained together into something you can set up in under 20 minutes.*


## The Stack


Here’s what we’re building:


**9router** handles the AI models. It routes your coding tools through free providers so you never pay for API calls or hit rate limits.


**agentmemory** handles persistence. It gives your agent memory across sessions, so it doesn’t start from scratch every time you open a new terminal.


**agent-skills** handles quality. It gives your agent structured engineering workflows so it doesn’t just write code, it follows a real development process.


Each one solves a different problem. Together they cover the three biggest pain points of AI-assisted coding: cost, context loss, and inconsistent quality.


## Layer 1: 9router (Free AI Models)


### The problem it solves


Claude Code requires a Pro subscription ($20/month) or API credits. Cursor is $20/month. Copilot is $10-19/month. If you’re using multiple tools across projects, you’re easily spending $50-90/month just on AI access.


### What 9router does


It’s a local proxy that sits between your coding tool and the AI backend. You install it, point your tool at localhost:20128, and 9router handles routing your requests to free model providers. When one provider hits a rate limit, it automatically falls back to the next one. You never notice the switch.


### Setup (5 minutes)


**Step 1: Install and start**



```
`npm install -g 9router
9router`
```

This starts the proxy server and opens a dashboard at http://localhost:20128. The dashboard is where you’ll add providers and grab your local API key.


**Step 2: Add free providers**


Open the dashboard and connect these (in order of reliability):


1. **Kiro AI** - Free tier gives you 50 credits/month with access to Claude Sonnet 4.5, Qwen3 Coder Next, DeepSeek v3.2, and MiniMax 2.1. Auth via AWS Builder ID, GitHub, or Google OAuth. Not unlimited, but the low credit multipliers on open-weight models stretch those 50 credits further than you'd expect. This is your primary.
2. **OpenCode Free** - No authentication at all. Quality varies, so use it as fallback. Good for lighter tasks.
3. **Vertex AI** - Google Cloud gives $300 in free credits for new accounts (90-day window). Gemini models. Save this for heavier tasks if you have a fresh GCP account.


A heads-up: iFlow, Qwen free tier, and Gemini CLI free were all discontinued in 2026. Don’t waste time on those.


**Step 3: Connect your coding tool**


For Claude Code (with API key mode):



```
`export ANTHROPIC_BASE_URL=http://localhost:20128/v1
export ANTHROPIC_API_KEY=<key from 9router dashboard>
claude`
```

For Cursor: Settings > Models > OpenAI API Base > set to `http://localhost:20128/v1`, paste the key from the dashboard.


For Codex CLI: same pattern. Any tool that accepts an OpenAI-compatible endpoint works.


**Step 4: Enable RTK Token Saver**


In the dashboard, go to Endpoint Settings and make sure RTK is toggled on (it should be by default). This compresses tool output (git diffs, grep results, directory listings, logs) before sending it to the model. Typical reduction: 40%. A 47K-token request drops to 28K tokens. This means longer conversations before you hit any limits, and faster responses.


### What you end up with


Your coding tool works exactly like before. Same interface, same commands, same workflow. But the requests route through free providers with automatic fallback and 40% fewer tokens per request. Monthly cost: $0.


## Layer 2: agentmemory (Persistent Context)


### The problem it solves


Every AI coding agent has some form of built-in memory. Claude Code has MEMORY.md. Cursor has notepads. But these are like sticky notes. They’re flat, not searchable, and they don’t connect related information across sessions. So you pay for Mem0($50), here’s how to replace it.


You’ve felt this if you’ve ever started a new session and the agent re-does work from yesterday, or asks you questions you already answered, or forgets that you chose a specific architecture three sessions ago.


### What agentmemory does


It runs a persistent memory server on localhost that any agent can read from and write to. It captures what your agent does during each session, compresses it into structured memories (facts, patterns, session summaries), indexes everything with hybrid search (BM25 keywords + vector embeddings + knowledge graph), and injects the right context when the next session starts.


The key insight: when you search for “database performance optimization,” it finds your N+1 query fix from last week, even though those words never appeared together in that session. Keyword search can’t do that. agentmemory’s hybrid retrieval can.


### Setup (5 minutes)


**Step 1: Start the memory server**



```
`npx @agentmemory/agentmemory`
```

This starts the server on port 3111. A real-time viewer opens at http://localhost:3113 where you can watch memories being created and searched.


**Step 2: Connect to Claude Code**


If you’re using Claude Code:



```
`agentmemory connect claude-code`
```

This registers 12 lifecycle hooks that automatically capture session activity. You also get 4 slash commands: `/recall` (search memories), `/remember` (manually save something important), `/session-history` (browse past sessions), and `/forget` (delete specific memories).


For other agents (Cursor, Codex CLI, Gemini CLI, Cline, Windsurf): agentmemory supports MCP, REST API, and hooks. The connect command wires the appropriate integration.


**Step 3: Verify**



```
`curl http://localhost:3111/agentmemory/health`
```

If that returns OK, you’re set. The agent will now automatically remember what it did across sessions and retrieve relevant context at the start of each new one.


### How it works with 9router


This is where the chain starts paying off. 9router handles the AI model routing for free. agentmemory handles the context. The agent talks to the model through 9router (free), and reads/writes memory through agentmemory (local). Two layers, zero external costs.


And because RTK cuts tokens by 40%, the context that agentmemory injects at session start costs fewer tokens than it would normally. The tools complement each other without knowing about each other.


## Layer 3: agent-skills


### The problem it solves


Even with free models and persistent memory, the agent still needs to know *how* to work properly. Without structure, agents skip tests, half-finish features, declare victory too early, and produce code that technically runs but doesn’t follow engineering best practices.


### What agent-skills does


It’s a pack of 23 production-grade engineering skills created by Addy Osmani (the Google engineer behind Chrome DevTools). Each skill is a structured workflow with steps, verification gates, and checkpoints that produce evidence. They cover the full development lifecycle: spec, plan, build, test, review, ship.


This isn’t a course you read. It’s a set of files you install that change how the agent works.


### Setup (5 minutes)


**For Claude Code (easiest):**



```
`/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills`
```

This gives you 7 slash commands that map to the dev lifecycle:


* `/spec` - Define what you’re building
* `/plan` - Plan the implementation
* `/build` - Write the code
* `/test` - Verify it works
* `/review` - Review for quality
* `/ship` - Prepare for deployment
* `/code-simplify` - Refactor for clarity


**For other tools:**



```
`git clone https://github.com/addyosmani/agent-skills.git`
```

Copy the relevant SKILL.md files into your project or agent’s rules directory. A meta-skill called `using-agent-skills` acts as a router that activates the right skill based on what you’re currently doing. Don’t load all 23 at once. Let the router handle it.


### What changes in practice


Before agent-skills: You say “add user authentication.” The agent writes login code, says “done,” and you discover it has no tests, no error handling, and it broke two existing features.


After agent-skills: You say `/build add user authentication.` The agent follows the build skill, which has explicit steps: understand the codebase first, write the feature, write tests, run the test suite, check for regressions, and only mark it done when verification passes. If tests fail, it fixes and re-runs. The evidence is logged.


This is harness engineering applied at the skill level. The agent doesn’t get smarter. It gets more disciplined.


## The Complete Setup (Under 20 Minutes)


Here’s the full sequence:



```
`# Layer 1: Free AI models
npm install -g 9router
9router
# → Open dashboard, add Kiro AI + OpenCode Free
# → Copy API key, set ANTHROPIC_BASE_URL=http://localhost:20128/v1

# Layer 2: Persistent memory
npx @agentmemory/agentmemory
# → In another terminal:
agentmemory connect claude-code

# Layer 3: Engineering skills (inside Claude Code)
/plugin marketplace add addyosmani/agent-skills
/plugin install agent-skills@addy-agent-skills`
```

Three terminals. Three tools. Zero subscriptions.


## A Real Week With This Stack


Abstract explanations only go so far. Here’s what this actually looks like across a real week of building a SaaS side project (a task management app with teams, auth, and Stripe billing).


**Monday evening (Session 1 - 45 mins)**


You open Claude Code after work. All three layers are running. This is a fresh project, so agentmemory has no prior context yet.



```
`You: /spec Build a task management app. Teams, user auth,
 Stripe billing, PostgreSQL, Next.js, deployed on Vercel.`
```

agent-skills activates the spec workflow. The agent asks clarifying questions (free tier or paid-only? invite-based teams or open signup?), then produces a structured spec with features, data models, and acceptance criteria. You refine it, approve it.



```
`You: /plan`
```

The agent breaks the spec into 8 features, ordered by dependency. Auth first, then teams, then tasks CRUD, then billing. Each feature has a definition of done.


You close the session. agentmemory saves: project name, tech stack decisions, the full feature list, and the planned order. Total API cost through 9router: $0.


**Tuesday evening (Session 2 - 1 hour)**


You open a new terminal. agentmemory injects Monday’s context. The agent already knows the stack is Next.js + PostgreSQL + Stripe, that auth comes first, and what the spec says.



```
`You: /build Implement email/password auth with JWT tokens`
```

The build skill kicks in. The agent sets up Prisma with a User model, writes the signup/login API routes, adds JWT middleware, creates the login page, writes 6 tests (happy path, wrong password, expired token, duplicate email, missing fields, token refresh), runs the test suite, and all 6 pass. It commits.


Behind the scenes: 9router routes to Kiro AI. The test output (verbose, full stack traces from the passing tests) gets compressed 40% by RTK before hitting the model for the commit message. You see none of this.


agentmemory saves: auth is done, Prisma is configured, JWT approach chosen over sessions, 6 tests passing.


**Wednesday (no coding)**


You don’t touch the project. Nothing happens. The memory and state sit on disk.


**Thursday evening (Session 3 - 1 hour)**


You open Claude Code. agentmemory surfaces: auth is complete (6 tests passing), teams feature is next per the plan, stack is Next.js + Prisma + PostgreSQL.



```
`You: /build Add team creation and invite system`
```

The agent builds the Team and TeamMember models, writes the invite flow with email tokens, adds the API routes, and writes tests. One test fails: the invite acceptance endpoint doesn’t properly handle expired tokens. The build skill catches this, the agent fixes the edge case, re-runs, all tests pass. It commits.


Now here’s where agentmemory earns its keep. While building the invite flow, the agent needed to touch the auth middleware (to check team membership). It recalled from Session 2 that you’re using JWT with a specific token structure, so it extended the token payload correctly without asking you how auth works. Without memory, it would have either asked you to explain the auth setup again or guessed wrong.


**Friday evening (Session 4 - 30 mins)**


Quick session. You want to add Stripe billing but you’re not sure about the pricing model yet.



```
`You: /spec Define the billing model. Two tiers:
 Free (up to 3 users, 50 tasks) and Pro ($12/user/month, unlimited).`
```

The agent produces the billing spec, referencing the existing Team model from agentmemory’s knowledge of Session 3. It notes that the free tier limit needs enforcement at the task creation endpoint and the team invites endpoint, not just the billing page.


You didn’t think of that. The agent connected billing constraints to existing features because it remembers what those features look like.


You approve the spec but don’t start building. agentmemory saves the billing spec and links it to the existing features.


**Saturday afternoon (Session 5 - 2 hours)**


Longer session. You knock out billing.



```
`You: /build Implement Stripe billing with the approved spec`
```

The agent sets up Stripe webhooks, creates the subscription flow, adds the usage limits, writes the upgrade/downgrade logic, and adds 11 tests. Two fail initially (webhook signature verification was wrong, and the free-tier task limit was off by one). The build skill catches both, agent fixes, re-runs, all 11 pass.



```
`You: /review`
```

agent-skills activates the review workflow. The agent reviews its own code for security issues, finds that the Stripe webhook endpoint doesn’t verify the event source properly, fixes it, adds a test for it. Now 12 tests passing.


You look at the git log. Five clean sessions, each building on the last. Zero dollars spent on AI. The agent remembers every decision, every architecture choice, every test result. You haven’t re-explained anything since Monday.


**The point:** Each session is 30 minutes to 2 hours. You give a single command. The agent knows what was built before, what comes next, follows a real engineering workflow, and you’re not paying for any of it. That’s the stack working together.


## Where This Breaks Down


This setup isn’t perfect. Here’s what to expect:


**Free model quality varies.** Kiro AI is solid for most coding tasks, but it’s not identical to a direct Claude Pro subscription. Complex multi-file refactors or very long context tasks might hit quality ceilings. OpenCode Free is noticeably weaker and works best as fallback, not primary.


**agentmemory has a learning curve.** The first few sessions are thin on memory. It gets dramatically better after 5-10 sessions once the knowledge graph has enough data points. If you switch projects frequently, the memories from one project won’t help on another (by design, but it means each project needs a ramp-up period).


**agent-skills add overhead.** The verification gates and structured workflows mean the agent takes longer per task. It’s doing more work (writing tests, checking regressions, logging evidence). That’s the point, but if you just want a quick code snippet, the full `/build` workflow is overkill. Use the agent casually for small stuff and invoke the skills for real feature work.


**You’re running three local services.** 9router, agentmemory, and your coding tool. If you’re on a lower-spec machine, that’s something to think about. None of them are resource-heavy individually, but it adds up.


## The Bottom Line


The paid AI coding stack (Claude Pro + Cursor + Copilot) runs about $50-90/month and gives you good models, no memory across sessions, and no structured workflows.


This stack runs $0/month and gives you good-enough models (with automatic fallback), persistent memory that gets better over time, and production-grade engineering workflows from one of Google’s best engineers.


The trade-off is setup time (20 minutes), some quality variance on the models, and running a few local services. For most individual developers and side projects, that’s a trade worth making.


If you want me to do a similar breakdown for the other combos from the original 7 repos list (like UI-TARS-desktop for automation or the financial-services templates for fintech), let me know. I’ll cover whichever gets the most interest.


*If you found this useful, share it with someone who’s still paying $90/month for AI coding tools. And if you’re new here, I write about practical AI workflows every week. No hype, just stuff you can actually use.  

  

— Cheers!*


### 9router + agentmemory + agent-skills. Built a Full SaaS App in 5 Sessions, Full setup guide.