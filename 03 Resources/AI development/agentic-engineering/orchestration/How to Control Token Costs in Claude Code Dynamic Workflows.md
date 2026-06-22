---
title: "How to Control Token Costs in Claude Code Dynamic Workflows"
source: "https://www.mindstudio.ai/blog/how-to-control-token-costs-claude-code-dynamic-workflows"
author:
  - "[[MindStudio Team]]"
published: 2026-06-01
created: 2026-06-13
description: "Dynamic workflows can burn millions of tokens fast. Learn how to scope tasks, use Haiku sub-agents, and set boundaries to keep costs under control."
tags:
  - "to-process"
  - orchestration
---
## Why Token Costs Spiral in Dynamic Claude Workflows

Dynamic workflows are one of the most powerful patterns in modern AI development. Instead of a single prompt-response loop, you get agents that plan, delegate, loop back on themselves, and call sub-agents to handle specialized tasks. Claude handles this kind of orchestration remarkably well.

But there’s a catch. Claude’s context window doesn’t forget between steps — every sub-task, every intermediate result, every tool call response adds to the running token count. In a multi-agent workflow, that adds up fast. What starts as a $0.02 task can quietly become a $2.00 task after five or six hops, especially when you’re passing full documents or previous outputs back into the context at every step.

Token cost control in Claude dynamic workflows isn’t about cutting corners on capability. It’s about being deliberate — scoping tasks tightly, routing work to the right model, and drawing clear context boundaries before they become expensive mistakes.

This guide covers the most effective techniques for doing exactly that.

---

## Understand How Tokens Actually Accumulate

Before you can fix the problem, you need to understand where the cost comes from.

### Input tokens vs. output tokens

Claude charges separately for input and output tokens, and input tokens are almost always the bigger cost driver in agentic workflows. Every time an agent calls Claude — whether it’s the orchestrator or a sub-agent — the full context (system prompt, conversation history, tool results, injected documents) counts as input.

![In 60 minutes, you'll know Hermes](https://i.mscdn.ai/1b7301c0-de42-4e46-b110-e9c55396e7ca/generated-images/6b6653fc-fa37-45fc-917d-0cd6c5f1f644.png?fm=auto&w=1200)

Output tokens are what Claude generates in response. These matter too, but in orchestration-heavy workflows, you’re usually reading far more than writing.

### The compounding context problem

Here’s what catches people off guard: in a multi-step workflow, each step often inherits the full context of the previous step. If step 1 returns 2,000 tokens of output and you pass that into step 2 as context, step 2 now starts with 2,000 extra input tokens. Add a third and fourth step and you’re compounding fast.

Some frameworks, particularly those using Claude’s [extended thinking](https://docs.anthropic.com/en/docs/build-with-claude/extended-thinking) mode, accumulate even more because they preserve reasoning traces in the context chain.

### Sub-agent spawning without boundaries

Agentic patterns where Claude can spawn sub-agents on-demand are powerful but risky from a cost perspective. If you don’t constrain what gets passed to each sub-agent, they’ll each receive the full upstream context by default. Five sub-agents with 10,000 input tokens each is 50,000 tokens for what might be five simple, discrete tasks.

---

## Scope Every Task Before You Assign It

The single most effective cost control is task scoping — defining exactly what each agent needs to know to complete its job, and nothing more.

### Write minimal system prompts

System prompts are charged as input tokens on every call. A 2,000-token system prompt repeated across 20 agent calls costs 40,000 tokens just in overhead. Keep system prompts under 500 tokens where possible. Focus on role and constraints, not lengthy background.

Instead of:

> You are an expert research assistant with deep knowledge of financial markets, regulatory environments, and macroeconomic trends. You have extensive experience summarizing complex information for executive stakeholders…

Try:

> You summarize financial documents for executives. Be concise. Focus on risk and opportunity. Output in bullet points.

### Pass only what the agent needs

Before injecting context into a sub-agent call, ask: does this agent actually need this? If an agent’s job is to format a table, it doesn’t need the 3,000-token research summary that produced the data. Strip it down to just the raw data.

A practical approach: write a lightweight “context extraction” step that runs before each sub-agent call. This step takes the full upstream context and returns only the relevant subset. Yes, this costs tokens — but a 200-token extract fed to three sub-agents beats a 3,000-token dump to three sub-agents every time.

### Use structured output to contain output size

When you ask Claude for unstructured prose, you often get more than you need. Output tokens cost money, and they become input tokens in the next step.

Specify your output format explicitly. Use JSON schemas, numbered lists, or bullet formats that constrain verbosity. Ask for the minimum viable answer: “Return only the three most important risks as JSON array items.”

---

## Route Tasks to the Right Model

One of the highest-leverage moves in multi-agent cost control is model routing. Not every task in a workflow needs Claude Sonnet or Opus. Many sub-tasks can run on Claude Haiku at a fraction of the cost.

### Build a model routing layer

Think of your workflow as having tiers:

- **Tier 1 (Haiku or equivalent):** Classification, extraction, formatting, simple retrieval, validation, boolean decisions
- **Tier 2 (Sonnet):** Summarization, moderate reasoning, multi-step analysis, code generation
- **Tier 3 (Opus or similar):** Complex reasoning, ambiguous problems, high-stakes outputs that require maximum accuracy
![Catch up on Hermes — free 60-minute live workshop](https://i.mscdn.ai/1b7301c0-de42-4e46-b110-e9c55396e7ca/generated-images/2f72d608-9e6a-4ec2-b2f1-5063df20ef36.png?fm=auto&w=1200)

Route sub-agent tasks to the appropriate tier based on complexity. A routing agent itself can be a lightweight Haiku call — ask it “what tier does this task fall into?” and dispatch accordingly.

### Haiku for sub-agents, Sonnet for orchestration

A common and effective pattern: use Claude Sonnet (or whichever mid-tier model fits your stack) as the orchestrator — the agent that plans, delegates, and synthesizes. Then spin up Haiku instances to handle individual, discrete sub-tasks.

The orchestrator needs reasoning capability. The sub-agents often just need to execute a simple, well-defined instruction. Haiku handles that reliably and cheaply.

Anthropic’s own [model comparison documentation](https://docs.anthropic.com/en/docs/about-claude/models) shows Haiku runs at roughly 1/10th the cost of Opus per token. On a workflow with 20 sub-agent calls, routing 15 of them to Haiku can cut sub-agent costs by 80–90%.

### Don’t default to the most capable model

It’s tempting to use your best model everywhere. But capable models are also verbose by default — they tend to produce longer, more thorough outputs even when you don’t need thoroughness. Cheaper models often produce tighter, more constrained outputs, which can actually be an advantage in structured workflows.

---

## Set Hard Context Boundaries

Without explicit limits, context windows balloon. Set boundaries at the architecture level, not as an afterthought.

### Implement context pruning at each step

Build a pruning function that runs between workflow steps. The job of this function is simple: take the accumulated context and drop anything that isn’t needed for the next step. Keep:

- The task description for the next step
- The minimum relevant output from previous steps
- Any persistent state the workflow needs (configuration, user preferences, etc.)

Discard:

- Full intermediate outputs once they’ve been summarized or acted on
- Tool call raw responses once they’ve been processed
- Conversation history beyond the most recent N exchanges if the workflow is long-running

### Cap document injection size

If your workflow involves reading documents — PDFs, web pages, database records — set explicit size caps before injection. Chunking is your friend here. Instead of injecting a full 50-page document, inject the most relevant chunk identified by a lightweight retrieval step.

A retrieval sub-agent using embeddings or keyword search to extract the right 500-word passage is far cheaper than injecting the full document repeatedly across multiple steps.

### Use summarization checkpoints

For long workflows, build in summarization checkpoints. At every N steps (or when context exceeds a threshold), run a summarization call that compresses the history into a concise state summary. From that point forward, the workflow runs on the summary rather than the raw history.

This is especially important for iterative workflows — things like research loops, revision cycles, or agent scratchpads that grow with each iteration.

---

## Use Caching Strategically

Claude supports prompt caching, and it’s one of the most underused cost controls in dynamic workflows.

### What caching does

When you mark part of a prompt for caching, Claude stores a processed version of that content. On subsequent calls that include the same cached content, you pay a reduced rate for cache reads instead of re-processing the full input. Cache writes cost slightly more than standard input, but cache reads are significantly cheaper.

![Hermes Crash Course — free 1-hour live workshop](https://i.mscdn.ai/1b7301c0-de42-4e46-b110-e9c55396e7ca/generated-images/957ba1d7-9c1c-417e-97da-2a97eac46966.png?fm=auto&w=1200)

This matters most for content that appears in many calls: system prompts, reference documents, instruction sets, static context.

### Where to apply caching

Good candidates for caching:

- System prompts that don’t change between calls
- Reference materials injected into multiple sub-agent calls (style guides, data schemas, knowledge base excerpts)
- Conversation history in long-running sessions
- Task instructions shared across parallel sub-agents

Poor candidates for caching:

- Dynamic user inputs
- Content that changes every call
- Short strings (cache overhead isn’t worth it under ~1,024 tokens)

### Cache the orchestrator’s context

In orchestrator-sub-agent patterns, the orchestrator’s system prompt and initial task description are often fed into every sub-agent call as context. If that shared content is 2,000+ tokens and you’re making 20+ sub-agent calls, caching it can meaningfully reduce input costs.

Structure your prompts so the cacheable static content appears first, followed by the dynamic per-call content. Claude’s caching system uses the earliest matching prefix, so position matters.

---

## Monitor and Audit Token Usage

You can’t optimize what you don’t measure. Build token monitoring into your workflow from the start.

### Log token counts at every step

Claude’s API responses include token usage data in the response metadata. Log input tokens, output tokens, and cache statistics for every call. Aggregate by workflow run so you can see total cost per execution.

Even a simple spreadsheet or dashboard tracking per-step token counts will quickly reveal where costs are concentrated. It’s almost always one or two steps that account for the majority of tokens.

### Set token budget alerts

Build token budget checks into your workflow logic. Before expensive steps — especially ones that inject large documents or run multiple parallel sub-agents — check whether the current run is on track to exceed your budget. If it is, trigger a fallback path: a cheaper model, a more aggressive context pruning step, or a human-in-the-loop escalation.

### Benchmark common paths

Run your most common workflow paths and record baseline token counts. When you change the workflow architecture, compare against baseline. This catches cost regressions before they hit production.

---

## How MindStudio Fits Into This

If you’re building dynamic Claude workflows and you want cost controls built into the architecture — not bolted on after the fact — MindStudio is worth looking at seriously.

MindStudio’s visual workflow builder lets you construct multi-step, multi-model agent workflows without writing orchestration code. Critically, it gives you explicit control over what context gets passed between steps, which model runs each step, and where to apply summarization or pruning logic — all within the same interface.

The model flexibility is directly relevant here: you can assign different models to different steps in the same workflow. Route your summarization steps to Claude Haiku. Run your complex reasoning steps on Sonnet. Mix in other models from the 200+ available on the platform without managing separate API keys or accounts.

Cursor

ChatGPT

Figma

Linear

GitHub

Vercel

Supabase

remy.msagent.ai

## Seven tools to build an app. Or just Remy.

Editor, preview, AI agents, deploy — all in one tab. Nothing to install.

The [Agent Skills Plugin](https://www.mindstudio.ai/blog/introducing-agent-skills) is useful for teams already building with Claude Code. It’s an npm SDK that lets Claude Code and other agentic frameworks call MindStudio’s capabilities — including workflow execution, search, and external integrations — as simple method calls. You get MindStudio’s infrastructure layer (rate limiting, retries, auth) without rebuilding it yourself.

You can start free at [mindstudio.ai](https://mindstudio.ai/) and build a working multi-step workflow in well under an hour.

---

## Common Mistakes and How to Fix Them

### Passing full conversation history to every sub-agent

This is the most common cause of runaway token costs. Sub-agents rarely need the full history — they need their specific task and the minimum relevant context to complete it. Fix this by writing an explicit context extraction step before each sub-agent call.

### Using the same model for everything

Defaulting to your most capable model across all steps is expensive and unnecessary. Audit your workflow steps and classify each one by complexity. Most steps in a production workflow are extraction, formatting, classification, or validation — all things Haiku handles well.

### Not specifying output format or length

Open-ended output instructions produce verbose responses. Every word in the response becomes an output token now and an input token in the next step. Be specific: “Return a JSON object with three fields” is cheaper than “Tell me what you found.”

### Forgetting that tool call results count as tokens

When agents use tools — web search, code execution, database queries — the results get injected back into the context as input tokens. If a search result returns 5,000 tokens of HTML content, that counts. Post-process tool results before injection: extract only the relevant section, summarize long results, or truncate to a character limit.

### Not testing token counts before scaling

Token costs in testing look manageable. At scale — thousands of workflow runs per day — they multiply fast. Always test with realistic data volumes and measure token usage before moving to production.

---

## Frequently Asked Questions

### How much can token costs vary in a multi-agent workflow?

Significantly. A single-step Claude Sonnet call for a simple task might cost fractions of a cent. A poorly scoped multi-agent workflow with no context pruning, using Opus throughout, passing full context between every step, can cost dollars per run. The difference between an optimized and unoptimized version of the same workflow can be 10–50x in token count.

### Is Claude Haiku reliable enough for production sub-agent tasks?

For well-defined, constrained tasks — yes. Haiku performs well on classification, extraction, formatting, simple Q&A, and validation tasks. It struggles with open-ended reasoning, complex multi-step logic, and ambiguous instructions. Use it where the task is clear and the output format is structured. Keep Sonnet or Opus for tasks that require judgment.

### What’s the best way to handle long documents in dynamic workflows?

Chunk and retrieve rather than inject in full. Use a lightweight retrieval step — semantic search or keyword matching — to identify the most relevant section of the document, then inject only that section. For documents that multiple sub-agents need, mark the chunk for caching to avoid re-processing costs.

### Does prompt caching work across different workflow runs?

## Other agents ship a demo. Remy ships an app.

UI

React + Tailwind ✓ LIVE

API

REST · typed contracts ✓ LIVE

DATABASE

real SQL, not mocked ✓ LIVE

AUTH

roles · sessions · tokens ✓ LIVE

DEPLOY

git-backed, live URL ✓ LIVE

Real backend. Real database. Real auth. Real plumbing. Remy has it all.

Yes, as long as the cached content matches. Claude’s cache persists for a defined period (currently around 5 minutes for standard cache, longer for extended cache tiers). For frequently reused system prompts or static reference documents, caching applies across runs, not just within a single workflow execution.

### How should I handle context in long-running iterative workflows?

Use summarization checkpoints. At regular intervals — every 10 steps, or when context exceeds a size threshold — run a dedicated summarization call that compresses accumulated history into a concise state representation. Continue the workflow on the summary. This prevents unbounded context growth in workflows with many iterations.

### Are there tools that automatically optimize token usage in Claude workflows?

No tool fully automates this — architectural decisions still require judgment. But observability tools like LangSmith, Helicone, and built-in platform analytics (including MindStudio’s) give you per-step token breakdowns that make optimization decisions much more tractable. You can also set up cost tracking via Claude’s API usage metadata directly.

---

## Key Takeaways

- Token costs in dynamic workflows compound at every step — input tokens from context accumulation are usually the biggest driver, not output.
- Scope tasks aggressively: pass only what each agent needs, keep system prompts short, and specify output format explicitly.
- Route sub-agent tasks to Claude Haiku or equivalent lightweight models wherever the task is structured and well-defined. Save Sonnet/Opus for complex reasoning.
- Apply prompt caching to static content — system prompts, shared reference documents, and task instructions that appear across multiple calls.
- Build summarization checkpoints and context pruning into long workflows before they ship, not after costs become visible.
- Monitor token counts at every step in development. Fix cost regressions before scale.

If you want a workflow environment with model routing, context control, and multi-step orchestration built in, [MindStudio](https://mindstudio.ai/) lets you build and test this kind of architecture without managing infrastructure from scratch.