---
title: "I Cut My Claude Code Token Usage by 90% — Here’s the Layered System That Worked"
source: "https://freedium-mirror.cfd/https://medium.com/all-about-claude/i-cut-my-claude-code-token-usage-by-90-heres-the-layered-system-that-worked-e3b1fefac009"
author:
published:
created: 2026-06-12
description: "Five tools, custom hooks, and one painful realisation: telling Claude to be efficient doesn’t work. Forcing it to be does."
tags:
  - "to-process"
  - agent-configuration
---
![Post cover image](https://freedium-mirror.cfd/img/700/1*kJfrq0urQUN8wUvXzbxG1g.png)

Five tools, custom hooks, and one painful realisation: telling Claude to be efficient doesn’t work. Forcing it to be does.

![](https://freedium-mirror.cfd/img/700/1*RrP_cGk_H-HeW_31JI1-xw.jpeg)

Mohit Aggarwal

It was a Tuesday in late March. I was three prompts into reviewing a pull request for our self-service config portal at Sportradar, and Claude Code was already at 47% context. Three prompts. On the Max plan.

I genuinely thought I'd misread the status line. I hadn't. It had pulled the diff, then opened twelve files to "understand the surrounding code," and now there was barely room to have the conversation. I closed the session, started a new one. Same thing.

What followed was a ten-day rabbit hole. By the end of it I'd cut my token usage by something north of 90% on most workflows. Not by being more careful. Not by writing better prompts. By accepting one uncomfortable truth: Claude Code, left to its own devices, will read everything, dump everything into context, and politely apologise when you run out of headroom. The fix is layers. And enforcement.

Here's what actually worked.

### The thing nobody tells you about "context window" optimisation

Most articles on Claude Code token usage tell you to write a tighter CLAUDE.md, use `/compact`, and switch to Sonnet for boring tasks. All true. All useful. None of it touches the actual problem.

The actual problem is that every message you send re-processes the entire conversation history. Every file Claude reads gets injected as a tool result. Every shell command output sits in the conversation forever, even after you've stopped caring about it. It's not reading a log, it's literally re-processing the full history on every turn. So when Claude reads a 500-line file to find a 12-line function, those 500 lines now travel with you for the rest of the session. Forever. Or until `/compact`, which is its own kind of lossy compromise.

I was treating Claude Code like a chat interface. It isn't. It's a transformer that pays the bill on every turn for everything that has ever been said. Once that clicked, the whole optimisation framing changed for me. The question stopped being "how do I prompt better" and started being "how do I stop garbage from entering the context window in the first place — and how do I make sure Claude can't sneak it back in when I'm not looking?"

That second half is where hooks come in.

### The five-layer stack (and why each one matters)

I'll be honest — I didn't design this from scratch. The community has been building these tools for months and I cherry-picked what worked for my workflow. What I did do is wire them together with hooks so Claude can't cheat its way around them.

Here's the mental model. Every layer attacks a different source of token bloat:

**1\. Replace file reads with a knowledge graph.** This is the big one. Tools in this space — Codebase Memory MCP is the one I landed on — index your codebase into a graph of symbols, references, and relationships. When Claude needs to know "where is `validateOddsFeed` called from," it queries the graph and gets back a 200-token answer instead of reading six files for 18,000 tokens. The savings on code exploration are roughly 99% in my experience, which sounds made up but isn't.

**2\. Sandbox your large outputs.** When you run `pytest` and 4,000 lines of stack traces flood in, that's now permanent context. A "context-mode" pattern (or sandboxed bash, or a custom subagent — there are several flavours) runs the command in an isolated environment and returns only a summary to your main session. The 4,000 lines stay out of the window. This alone saved me from a particularly horrendous integration test loop last month.

**3\. Compress CLI output in place.** Not every command warrants a full sandbox. For the ones that don't, a wrapper that pipes through a compressor (RTK is what I use) trims redundant lines, deduplicates repeated errors, and strips ANSI codes before the output ever hits Claude. Saved me 60–80% on most shell-heavy tasks.

**4\. Use a proxy that compresses the prompt itself.** This one feels like cheating. There's a class of tools — Headroom is one — that sit between your Claude Code instance and the API, and compress the entire outgoing prompt before it leaves your machine. The model still receives intelligible context. You just pay for fewer tokens. It's not free (you'll pay some quality cost on edge cases) but for routine work it's been transparent.

**5\. Force Claude's own responses to be shorter.** This is the easiest layer to miss. Output tokens cost roughly 5x what input tokens cost. Tools like Caveman (silly name, serious tool) inject rules that make Claude reply tersely by default. Most people never control how Claude responds — they just get whatever the model decides to output. A few config lines knocked my output volume in half.

That's the stack. Each layer attacks a different leak. The compounding is what gets you to 90%.

### Why I stopped trusting Claude to "just be efficient"

Here's the thing though. I tried the polite version of all of this first. CLAUDE.md rules. Standing instructions. "Always prefer the graph query over file reads." "Never read files larger than 200 lines without confirming first." I wrote a small novel of these instructions over the course of a weekend.

It mostly worked. Until it didn't.

The pattern was always the same: Claude would behave for the first hour, then it would hit some task where reading the file felt like the easier path, and it'd just… do it. No malice. Just transformer behaviour. The path of least resistance won. And once it had read the file, the file was in context, and the savings I'd planned for that session were gone.

The penny dropped during a refactor of one of our bookmaker onboarding flows. I had explicit instructions to use the codebase graph for any cross-file lookup. Claude read four files anyway. When I asked why, it said something reasonable about wanting to verify type definitions. Reasonable! Also six thousand tokens I didn't have to spare.

That's when I switched from instructions to enforcement.

### How custom hooks change the game

Starting in v2.0.10, PreToolUse hooks can modify tool inputs before execution. Instead of blocking Claude's actions and forcing retries, hooks intercept tool calls, modify the JSON input, and let execution proceed with corrected parameters. This is the bit most people miss. Hooks aren't just for blocking — they're for silently rewriting what Claude is about to do.

A few hooks that have paid for themselves many times over:

A `PreToolUse` hook on the `Read` tool that intercepts any file read over 300 lines and rewrites it to a graph query against my codebase index. Claude thinks it read the file. It got a summary. Context stays clean.

A `PreToolUse` hook on `Bash` that wraps any command likely to produce verbose output (`pytest`, `npm run build`, `docker logs`) in my sandbox wrapper. Claude doesn't have to remember to do this. It just happens.

A `PostToolUse` hook that strips repeated error lines from any tool result before it hits the conversation. If your linter spits out the same warning 47 times, Claude sees it once.

A `Stop` hook that, when context crosses 60%, automatically writes a handoff note capturing decisions made, files touched, and current task state — so when I `/clear` and start fresh, I can re-orient in a few hundred tokens instead of a few thousand.

The pattern across all of these: bad approach is "NEVER use WebSearch, use gemini\_web\_search instead" written into instructions. Good approach is a PreToolUse hook that blocks WebSearch and silently suggests the alternative. Instructions are advisory. Hooks are physics. Claude can rationalise its way around an instruction. It cannot rationalise its way around a hook that rewrote its tool call before it ran.

### What didn't work (and what I'd do differently)

Not everything in my first pass survived. A few honest admissions:

**Aggressive auto-compaction was a disaster.** I set up a hook that triggered `/compact` at 50% context. It compacted *constantly*, including in the middle of complex tasks where the granular history actually mattered. The session would forget which approach we'd just rejected and try it again. I now compact manually, at natural breakpoints, the way the docs suggest. Should've listened the first time.

**The proxy compression caused one genuinely weird bug.** During a debugging session involving regex patterns, the compression mangled some escape characters in the prompt. Claude got confused, I got confused, we lost about 40 minutes before I realised. For anything involving exact string matching, I now bypass the proxy. It's an environment toggle.

**My first CLAUDE.md was 4,200 tokens of "best practices."** Which means every single message paid 4,200 tokens before I'd typed a word. CLAUDE.md loads before Claude reads your code, before it reads your task, before anything. Every turn. Every session. I cut mine to 600 tokens of essentials. The rest moved into skill files that load on demand.

**I underestimated how much Opus was costing me on trivia.** I had it set as my default for ages because it felt smarter. For 80% of what I do — refactors, test writing, sprint board updates, drafting Slack messages from JIRA tickets — Sonnet is genuinely indistinguishable. I now reserve Opus for actual architectural decisions.

### The principles, if you don't care about my specific stack

You don't need my exact tools. The vendors will change, someone reading this in nine months will be using something different. The principles are what matter:

**Stop garbage from entering context.** Every file read, every command output, every paste from a chat window is permanent. Treat the context window like a backpack on a long hike — every item you put in, you carry the rest of the way. Replace large reads with summaries. Replace file dumps with graph queries. Replace verbose tool output with compressed output.

**Make efficiency the default, not the request.** Anything you have to remember to do, you'll forget when you're tired. Hooks, wrappers, and sandboxes turn good habits into infrastructure. The goal is to make the efficient path the only path.

**Match model to task ruthlessly.** Sonnet for the 80%. Opus for genuinely hard reasoning. Haiku is roughly 80% cheaper and sufficient for any subagent doing exploration, file reading, or test running.

**Treat session length as a budget.** Long sessions accumulate cruft. Shorter, scoped sessions with explicit handoffs (a scratch file, a JIRA comment, anything) are dramatically more efficient than one monster session limping along on `/compact`.

**Measure something.** I run `/cost` at the end of every session and keep a rough log. Without a baseline you're just vibing about whether your changes worked.

### Was it worth the ten days?

Yes — and I think a lot of people in product roles writing code with Claude Code (which, increasingly, is most of us) are silently burning through their plans without realising the leak is plugable.

What used to be a 30-minute session before I hit annoying context degradation is now comfortably 2–3 hours of focused work. I haven't hit my Max limit since I set this up. I caught myself yesterday running a refactor across nine files that, last quarter, I genuinely wouldn't have attempted in a single session. That's the actual win — not the cost saving, but the surface area of work that becomes possible when context isn't a scarce resource.

The slightly uncomfortable part: I still don't fully trust Claude to be efficient on its own. I trust the hooks, the wrappers, the proxy. The model is a brilliant collaborator surrounded by guardrails I built because I learned, the expensive way, what happens without them.

I'm curious whether this gets easier over the next year, or whether the layered-stack-plus-enforcement pattern just becomes how everyone works with agentic coding tools. My money is on the second one.

What's working in your setup? I'd love to hear what you're enforcing that I'm not.