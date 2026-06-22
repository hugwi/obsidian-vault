---
title: "We Automated Our AI Review Loop and It Failed 86% of the Time"
source: "https://medium.com/@radupana/we-automated-our-ai-review-loop-and-it-failed-86-of-the-time-15a4f9702bb7"
author: "Radu Pana"
published: 2026-05-25
created: 2026-06-03
description: "We took an agent-driven code review/fix/repeat workflow that worked well"
tags:
  - to-process
  - llm-foundations
---

We took an agent-driven code review/fix/repeat workflow that worked well when humans triggered it, wired it together with a Python script in GitHub Actions, and ran it unattended on every PR for three weeks. Out of 50 workflow runs, 43 failed. The pipeline never stabilized enough to produce useful results at scale.

This post is about what that failure taught us and specifically about the gap between “**agent that works interactively**” and “**agent that works autonomously in CI**,” and what humans are actually providing when they orchestrate agent workflows.

#### Context

We’re a small team (< 10 engineers) working in a monorepo on GitHub. Two backend services — one in Kotlin, one in Python, both pre-production, about 40k lines combined. The team uses AI coding agents and re-usable skills extensively for feature implementation and review.

All of our skills leverage a plethora of AGENTS.md and other md files scattered across the monorepo, which provide plentiful context about the codebase, including technical and product requirements/decisions.

Our workflow before the experiment:

1. Developer plans the implementation details of a GitHub issue, using a **/plan-issue** skill. The plan is agreed upon between the developer and the agent and posted to the GH issue as a comment.
2. Developer instructs an agent to implement a feature, linked to a GitHub issue’s implementation plan, using an **/implement-issue** skill.
3. Agent writes code, self-reviews, opens a PR, using a **/commit-and-pr** skill.
4. Developer invokes a reviewer agent with a **/review-pr** skill that runs a multi-pass review against the project’s decision records, engineering standards, and linked issues.
5. Developer invokes a fixer agent using the **/address-review-comments** skill to address the review comments.
6. Human reviews the final state, merges.

The human at step 6 still catches things, as does GitHub’s native Copilot reviewer. But the orchestration of steps 4–5 — telling one agent to run, waiting, telling another agent to run — felt like it could be automated with a script. The agents and the skills were the same. The human was just clicking buttons in sequence (or so we thought).

We scoped a 4-week experiment: automate steps 4–5 as a CI workflow. Human still approves at the end. We just wanted to remove the human from the middle of the review-fix loop. At ~15–20 in-scope PRs per week and zero marginal LLM cost (everything ran through our existing GitHub Copilot subscription — rate limits were the constraint, not billing), it seemed low-risk.

#### What We Built

A GitHub Actions workflow triggered on every PR touching our in-scope paths. A Python orchestrator (66 unit tests, deliberately thin) coordinated the loop:

1. PR opens
2. Orchestrator invokes the reviewer agent command (same one developers use locally)
3. If blockers found, orchestrator invokes the fixer agent command
4. Loop up to 3 iterations
5. Label the PR based on outcome

PRs over 3000 lines were auto-skipped. Draft PRs skipped. Bot-authored pushes skipped. Per-agent timeouts (10 min reviewer, 15 min fixer). Concurrency controls so a new push cancels stale reviews.

#### The Stdout Parsing Problem

Our first architecture had the reviewer agent emit a structured verdict to stdout — delimiters wrapping JSON that the orchestrator would parse. This caused six consecutive pipeline failures. The agent would get distracted by permission messages at startup and never emit the verdict. Or it would see existing review comments on the PR and switch into “triage mode.” Or it would just not emit the delimiters — exit code 0, no error, no usable output.

We couldn’t even diagnose why until we added full session transcripts (every tool call, every LLM message) as workflow artifacts. Without that, we were debugging a black box. This is true for any autonomous agent work — **session transcripts are as necessary as application logs for a production service.**

The fix was to stop fighting the agent’s natural behavior. Instead of making it emit structured output, let it post its review directly to GitHub (which is what it wants to do anyway) and have the orchestrator read the posted review from the API. If a review exists with the expected verdict format in its body, we succeeded. If it doesn’t exist, we detect that and error out. Make the deliverable something the agent naturally produces; verify through a stable API, not ephemeral stdout.

#### Allowlists vs Denylists

When you run an agent in CI, you need to constrain it. Our first attempt was a denylist:

“DO NOT use `gh api`for fetching reviews,”

“DO NOT load skills,”

“DO NOT debug CI failures.”

Failed across 8+ runs. The agent found commands not on the deny list and used them to go off-task. On PRs with failed CI checks, it spent 10+ tool calls investigating the CI failure instead of reviewing code.

Switched to an allowlist: “You may ONLY use `bash`with these specific commands, and `read`. Everything else is denied.”

Zero off-task behavior from that point forward. The space of things an agent could do that you didn’t think to prohibit is infinite — denylists don’t work for unattended execution. We layered this with workflow-level permissions blocking destructive operations for all agents. Both layers necessary.

#### The Results

Over two weeks of active running: 50 workflow runs, 43 failures, zero reviews that led to developer action. Even on the runs that succeeded, the output wasn’t worth the machinery.

The obvious question: maybe we just built this badly. Perhaps. The orchestrator was well-tested but the integration surface — agent invocation, authentication, GitHub API interactions, timeout handling, concurrency — was large and underestimated. At 50 runs over two weeks, each failure mode compounds.

But even when the pipeline worked, the results were underwhelming. On the most substantial PR the agent successfully reviewed — 10 files, a unified reason code mapping — we could compare it against GitHub’s native Copilot reviewer on the same PR. The native reviewer found 5+ real bugs: duplicate map keys, fallback logic errors, a silently removed exception handler that turned out to be a real defect. Our custom agent found 2 things, one of which was a false positive. Developers responded to Copilot’s comments and confirmed fixes. The custom agent’s findings went unaddressed — partly because the pipeline’s noise (ERROR banners on every failed run) had already eroded trust, and partly because we didn’t push the team to engage with them during the experiment.

#### Orchestration Intelligence

The surface-level answer for why it failed is reliability: 86% failure rate mostly due to agents going off-task. The deeper answer is more interesting.

When a developer invokes the reviewer agent interactively, they’re doing invisible work. They retry if the output looks wrong. They skip the review entirely on trivial PRs (judgment call, not a line-count threshold). They notice when the agent is reviewing old comments instead of new code and interrupt it. They read the review and decide “the fixer should handle items 1 and 3 but item 2 is wrong, ignore it.” They recognize when the agent is confused and rephrase.

None of this is “review.” It’s orchestration intelligence — the continuous judgment about whether the agent’s behaviour is correct, not just whether it produced output. It’s invisible when it’s working, which makes it look like ceremony you can automate away. But it isn’t.

The other thing is that the same agent genuinely behaves differently in CI than interactively. Same prompt, same model, same command. In CI, it got distracted by environment artifacts (permission messages, existing bot comments, CI check statuses) that aren’t present in interactive invocation.

#### Conclusion

**Don’t reinvent existing, working platform tooling.** Copilot’s native reviewer with a few instruction files got us better results than three weeks of custom pipeline engineering. The effort we put into codifying our engineering standards paid off — just not through the mechanism we expected.

**Don’t underestimate human-in-the-loop.** The human between steps 4 and 5 wasn’t performing ceremony. They were catching agent misbehavior early, before it propagated. In an autonomous loop, a confused agent in iteration 1 produces a bad review, which the fixer “addresses” in iteration 2, which the reviewer then evaluates in iteration 3 — each step compounding the original error. A human breaks that chain in seconds by noticing “that’s not right” and restarting. As [Daniel Braz puts it: “the human in the loop is not the bottleneck to be removed — it is the mechanism that preserves coherence.”](https://levelup.gitconnected.com/the-rush-nobody-asked-for-why-the-human-in-the-loop-was-never-the-bottleneck-1a554d90fce9)

**Autonomous chains are fragile in proportion to their length.** Every step that can fail slightly — not crash, just go subtly off-task — multiplies uncertainty through the remaining steps. A 90%-reliable agent invoked once is fine. The same agent invoked 6 times in sequence (3 review-fix iterations × 2 agents) gives you a 53% chance of a fully correct run. Our agents weren’t anywhere near 90% reliable in CI, which is how you get to 86% failure.