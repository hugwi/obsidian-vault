---
categories:
  - "[[Resources]]"
domain: engineering
title: "Claude Code Cost Tracking: Monitor and Cut Your Spending"
source: "https://avinashsangle.com/blog/claude-code-cost-tracking"
author:
  - "[[Avinash Sangle]]"
published: 2026-04-16
created: 2026-06-12
description: "Track Claude Code costs with built-in commands, local JSONL logs, and tools like ccusage. Plus 7 practical tips to cut your token spending by 50% or more."
tags:
  - "to-process"
  - context-management
---
The complete guide to tracking what you spend in Claude Code - from built-in commands and hidden JSONL logs to third-party dashboards and budget controls. Plus practical tips that cut my token costs by half.

## How Much Does Claude Code Actually Cost?

Claude Code costs about $6 per developer per day on average, according to Anthropic's own data. But that number hides a wide range. Some days I spend under $2. Other days - usually when I'm doing a heavy refactoring session with Opus - it spikes past $20. The problem isn't the cost itself. It's that most developers have no idea what they're actually spending.

TL;DR

- **Track costs with built-in commands:** `/cost` for API users, `/stats` for subscribers, `/usage` for rate limit status
- **Find your hidden usage data:** Claude Code logs every session to `~/.claude/projects/` as JSONL files with full token counts
- **Use third-party tools for real visibility:** ccusage (4.8k GitHub stars) gives you daily, monthly, and per-session cost reports
- **Cut costs by 50% with 7 practical changes:** default to Sonnet, cap thinking tokens, clear context between tasks, and write specific prompts

The pricing structure itself is straightforward. Claude Code Pro runs $20 per month (or $17 annually). The Max plan comes in two tiers: $100/month for 5x the Pro usage allowance, and $200/month for 20x. If you're on the API, you pay per token - Sonnet 4.6 at $3/$15 per million input/output tokens, and Opus 4.6 at $15/$75.

Across enterprise deployments, the average lands between $150 and $250 per developer per month, according to Anthropic's published benchmarks. Ninety percent of users stay under $12 per day. But that top 10% can burn through tokens fast, especially with extended thinking enabled and Opus as the default model.

The real issue? Tracking is scattered across multiple surfaces. Subscription users can't see dollar costs in the Console. API users get billing data but not per-session breakdowns. And everyone has local JSONL files sitting on their machine that most people don't even know exist. This guide covers every tracking method available - built-in, hidden, and third-party.

## Built-In Cost Tracking Commands You Should Know

Claude Code ships with three commands for checking usage. Which one you should use depends on whether you're paying through the API or a subscription plan. I run `/cost` at the end of every session to build intuition about what different task types actually cost.

### /cost - Session API Spend

The `/cost` command shows your current session's token usage and estimated dollar cost. It's designed for API users. If you're on a subscription plan, it'll remind you that cost data isn't relevant for billing purposes. But it still shows token counts, which is useful for understanding your consumption patterns.

```
Total cost:            $0.55
Total duration (API):  6m 19.7s
Total duration (wall): 6h 33m 10.2s
Total code changes:    127 lines added, 43 lines removed
```

### /stats - Subscriber Usage Dashboard

If you're on Pro or Max, `/stats` is your go-to. It opens a dashboard with a usage heatmap, session counts, token totals broken down by model, and activity streaks. It doesn't show dollar costs (since you're on a flat-rate plan), but it shows you exactly how much of your allowance you're burning through.

### /usage - Rate Limit Status

The `/usage` command shows your plan limits and current rate limit status. This is the command to check when Claude Code starts feeling slow or when you suspect you're hitting throttling. It shows both your 5-hour and 1-week usage windows.

### Status Line Configuration

Instead of running commands manually, you can configure Claude Code's status line to show cost information continuously. This keeps token usage visible at all times without interrupting your workflow.

```
# Show cost in the status line (API users)
claude config set status_line.show_cost true

# Show token count in the status line
claude config set status_line.show_tokens true
```

- **API users:** Use `/cost` for dollar amounts and `/usage` for rate limits
- **Pro/Max subscribers:** Use `/stats` for usage patterns and `/usage` for rate limit status
- **Everyone:** Configure the status line for passive monitoring

## Where Claude Code Stores Your Usage Data

Here's something most Claude Code users don't know: every session gets logged to your local filesystem as JSONL files. These files contain detailed token counts for every API call - input tokens, output tokens, cache creation tokens, cache read tokens, and the model used. This is the same data that third-party tools read to build their dashboards.

### Session Logs

Claude Code writes one JSONL file per session to `~/.claude/projects/`. Each line in the file represents a single API call with complete token metadata. If you're on a subscription plan, these local logs are the only way to get granular cost data since the Console doesn't expose it.

```
# Find your session logs
ls ~/.claude/projects/

# Look at the most recent session
ls -lt ~/.claude/projects/ | head -5

# Count tokens in a session with jq
cat ~/.claude/projects/<session-file>.jsonl | \
  jq -s '[.[].message.usage // empty] |
    { total_input: (map(.input_tokens) | add),
      total_output: (map(.output_tokens) | add),
      cache_read: (map(.cache_read_input_tokens // 0) | add),
      cache_creation: (map(.cache_creation_input_tokens // 0) | add) }'
```

### Status Line Snapshots

There's a second file most people miss: `~/.claude/statusline.jsonl`. This contains periodic snapshots from Claude Code's status line, including the server-reported cumulative cost and your 5-hour and 1-week rate-limit usage percentages. This data isn't available anywhere else. Not in the Console, not through the API. Only in this local file.

```
# View recent status line snapshots
tail -5 ~/.claude/statusline.jsonl | jq .

# Extract cost progression over time
cat ~/.claude/statusline.jsonl | \
  jq -r '[.timestamp, .cost_usd] | @csv'
```

I check these files about once a week. The status line snapshots are particularly useful because they show how your rate-limit usage percentage changes throughout the day. If you're regularly hitting 80%+ of your 5-hour window, that's a sign you might need the Max plan or need to adjust your workflow.

## Third-Party Tools for Claude Code Usage Analytics

The built-in commands give you a snapshot. For real visibility into trends over time, per-project breakdowns, and cost forecasting, you need something more. The open-source community has built several solid tools that parse those local JSONL files. I've tested four of them.

### ccusage - The Most Popular Option

With 4,800+ GitHub stars, ccusage is the tool most developers reach for. It's a CLI that reads your local JSONL files and produces clean tables with daily, monthly, or per-session cost breakdowns. It tracks cache tokens separately, supports billing window analysis, and works entirely offline with cached pricing data.

```
# Install and run - no setup needed
npx ccusage              # Daily report (default)
npx ccusage daily        # Detailed daily breakdown
npx ccusage monthly      # Monthly aggregated totals
npx ccusage session      # Cost per conversation session
npx ccusage blocks       # 5-hour billing window analysis

# Filter by project
npx ccusage --instances  # Group usage by project
```

### claude-usage - Local Web Dashboard

If you prefer a visual dashboard over CLI tables, claude-usage is worth a look. It reads the same local log files but renders them as charts with cost estimates, session timelines, and model breakdowns. Pro and Max subscribers get a progress bar showing how much of their allowance they've used.

### Claude-Code-Usage-Monitor - Real-Time Alerts

This tool takes a different approach. Instead of historical reports, it gives you a real-time chart of token consumption with predictions about when you'll hit your limits. If you're on a Max plan and want early warnings before you get throttled, this is the one to try.

### ccost - Per-Request Granularity

For the most granular view, ccost analyzes per-request JSONL logs with detailed token counts and computes costs using LiteLLM pricing data. I use this when I want to understand exactly which requests in a session were the most expensive. Usually it's the ones with large context windows or extended thinking enabled.

Tool Comparison

| Tool | Interface | Best For | GitHub Stars |
| --- | --- | --- | --- |
| ccusage | CLI | Daily/monthly reports, billing windows | 4,800+ |
| claude-usage | Web dashboard | Visual charts, subscriber progress bars | 1,200+ |
| Usage-Monitor | CLI (real-time) | Limit predictions, early warnings | 500+ |
| ccost | CLI | Per-request cost analysis | 200+ |

## How to Set a Budget Limit for Claude Code

Tracking is half the problem. The other half is making sure you don't overshoot. Claude Code offers several ways to cap spending, depending on whether you're an individual developer or managing a team.

### Per-Command Budget Cap

The `--max-budget-usd` flag caps the maximum dollar amount for a single print-mode command. This is useful in CI/CD pipelines or automated scripts where a runaway agent could burn through tokens unexpectedly. I set this on every automated Claude Code call in my build pipelines.

```
# Cap a single command at $5
claude -p --max-budget-usd 5.00 "Refactor the auth module"

# Combine with max-turns for double protection
claude -p --max-budget-usd 10.00 --max-turns 5 "Fix failing tests in src/"
```

### Workspace Rate Limits for Teams

When you first authenticate Claude Code with a Claude Console account, it automatically creates a workspace called "Claude Code." You can set rate limits on this workspace through the Console's Limits page. This caps Claude Code's share of your API allocation, preventing it from starving other production workloads.

### Agent SDK Cost Tracking

If you're building on the [Claude Agent SDK](https://avinashsangle.com/blog/claude-managed-agents), every result message includes a `total_cost_usd` field. You can aggregate this across multiple calls to track cumulative spend programmatically.

```
import { query } from "@anthropic-ai/claude-agent-sdk";

let totalSpend = 0;

const prompts = [
  "Read the files in src/ and summarize the architecture",
  "List all exported functions in src/auth.ts"
];

for (const prompt of prompts) {
  for await (const message of query({ prompt })) {
    if (message.type === "result") {
      totalSpend += message.total_cost_usd;
      console.log(\`This call: $${message.total_cost_usd}\`);
    }
  }
}

console.log(\`Total spend: $${totalSpend.toFixed(4)}\`);
```

## 7 Ways to Cut Claude Code Costs by 50%

After tracking my spending for a few weeks, I identified the patterns that were burning through tokens fastest. These seven changes brought my daily average from about $12 down to $5-6. None of them require sacrificing output quality.

Sonnet 4.6 costs $3/$15 per million input/output tokens. Opus 4.6 costs $15/$75. That's 5x more expensive. For the majority of coding tasks, Sonnet produces results that are just as good. I only switch to Opus for complex architectural decisions, tricky debugging sessions, or tasks where first-pass accuracy really matters.

```
# Switch models on the fly
/model sonnet    # For everyday tasks
/model opus      # For complex reasoning only
```

Extended thinking is the single biggest cost lever in Claude Code. Uncapped thinking tokens can generate tens of thousands of tokens per request. Setting a limit of 10,000 still gives Claude enough room to reason through problems while preventing runaway costs. For simpler tasks, you can drop this further or disable thinking entirely.

```
# Set thinking token limit
export MAX_THINKING_TOKENS=10000

# Or lower the effort level for simple tasks
/effort low       # Significant token savings
/effort medium    # Balance of cost and quality
```

Stale context is a silent cost multiplier. Every message you send includes the full conversation history as input tokens. If you've been working on auth code for an hour and then switch to fixing CSS, all that auth context is still being sent with every request. Run `/clear` when you switch to unrelated work. Use `/rename` first if you want to come back to the session later with `/resume`.

If you're mid-task and can't clear the session, use `/compact` to summarize the conversation history. This reduces the token count while preserving the important context. Claude Code also does this automatically when approaching the context limit, but running it manually at the right time gives you more control.

Vague prompts are expensive. "Make this better" forces Claude to spend tokens figuring out what you want. "Extract the hardcoded strings in src/auth.js into constants" gets the job done in one pass. The more specific your prompt, the fewer tokens wasted on clarification or wrong approaches.

I write my prompts the same way I'd write a [CLAUDE.md instruction](https://avinashsangle.com/blog/claude-md-guide): specific file paths, specific outcomes, specific constraints.

Press Shift+Tab twice to enter plan mode before starting a big task. This makes Claude outline its approach before writing any code. It costs a few hundred tokens for the plan but can save thousands by preventing costly rework. I use this before any refactoring that touches more than three files.

One session for everything is the most expensive way to use Claude Code. Context accumulates, cache misses increase, and irrelevant history gets sent with every request. Instead, work in task-scoped sessions: one for fixing the login bug, another for adding the new API endpoint, a third for writing tests. Each fresh session starts with a clean context window.

## Claude Code API vs Subscription: Which Costs Less?

This depends entirely on how much you use Claude Code. I've run the numbers for three usage profiles, and the breakeven points are clear.

| Usage Profile | API Cost/Month | Best Plan | Savings |
| --- | --- | --- | --- |
| Light (1-2 hrs/day) | $30-50/mo | API or Pro ($20) | Pay-per-use wins |
| Moderate (3-5 hrs/day) | $100-180/mo | Max 5x ($100) | Up to 44% savings |
| Heavy (6+ hrs/day) | $200-400/mo | Max 20x ($200) | Up to 50% savings |

The API makes more sense when you have sporadic usage or need fine-grained budget controls like `--max-budget-usd` on individual commands. It's also the only option if you need per-project cost allocation for billing clients. The subscription wins on predictability: you know exactly what you'll pay each month, and there's no risk of a bad session doubling your bill.

My approach: I use the Max 5x plan for day-to-day work and keep an API key configured for automated scripts and CI pipelines where I want hard budget caps. That hybrid setup gives me the best of both - predictable costs for interactive work and strict controls for automated spending.