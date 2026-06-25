---
categories:
  - "[[Clippings]]"
title: "Claude Code /goal: A Field Guide with Games"
source: "https://medium.com/@jason.croucher/claude-code-goal-a-field-guide-with-games-f6f3b617ce5b"
author:
  - "[[Jason Croucher]]"
published: 2026-05-18
created: 2026-06-15
rating: 
action: 
description: "/goal sets a completion condition, and Claude Code keeps working across turns on its own until a separate model decides the condition is met"
tags:
  - "to-process"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*kET80LKtdLoseKNTjA0ZVQ.png)

## What it is

`/goal` sets a completion condition, and Claude Code keeps working across turns on its own until a separate model decides the condition is met. It is the built-in version of the keep-going loops people hand-roll for long multiturn work.

## Requirements

- Claude Code v2.1.139 or later.
- The workspace trust dialog must be accepted (the evaluator is part of the hooks system).
- Unavailable if `disableAllHooks` is set at any level, or `allowManagedHooksOnly` is set in managed settings. The command tells you why if so.

## The commands

```c
/goal <condition>     set or replace the active goal (starts a turn immediately)
/goal                 show status: condition, turns, tokens, last evaluator reason
/goal clear           clear the active goal (aliases: stop, off, reset, none, cancel)
/clear                starting a new conversation also clears any active goal
--resume / --continue restores an active goal when you resume a session
                      (turn count, timer, token baseline reset; achieved or
                      cleared goals are not restored)
claude -p "/goal <condition>"
                      run the loop to completion non-interactively (Ctrl+C to stop)
```

One goal per session. A new `/goal` replaces the current one. The condition can be up to 4,000 characters.

## How to use it

1. Get clear on what you want first. Vague in, vague out. Before you set a goal, pin down the requirements and the definition of done. Use a planning or interrogation skill for this: superpowers’ `brainstorming` and `writing-plans`, or a Grill-Me-style skill that interviews you until the requirements are unambiguous, or plan mode. The output you want is to know exactly what "done" is and how it will show up in the transcript (a test result, an exit code, a file count).
2. Set the goal with `/goal <condition>`. It starts a turn immediately; you do not send a separate prompt.
3. Let it run. After each turn a small fast model (Haiku by default) reads the transcript and answers yes or no. “No” feeds its reason back as guidance and another turn starts. “Yes” clears the goal and records it as achieved.
4. Check progress with `/goal` (no argument): turns, tokens, and the evaluator's last reason.
5. Audit “achieved” yourself. The evaluator only read the transcript. Verify the result the way you would verify a colleague’s pull request before you trust it.
6. Stop early with `/goal clear` if you need to.

For unattended runs, pair it with auto mode: auto mode approves tool calls within a turn, `/goal` starts the next turn. For scheduled or headless work use `claude -p`. Do not leave an open-ended goal running overnight. Put a turn or time limit in the condition (see How to write the condition) and be ready to Ctrl+C.

## How to write the condition

A workable condition has:

- One measurable end state: a test result, a build exit code, a file count, an empty queue.
- A stated check: how Claude proves it (`npm test` exits 0, `git status` is clean).
- Constraints that must hold: anything that must not change on the way (no other test file is modified).
- A turn or time limit. Optional, but use one for any unattended run: add `or stop after 20 turns` or `or stop after 30 minutes` to the condition. The model judges this from the conversation, so it is not a hard mechanical stop; also be ready to Ctrl+C.

Bad: `improve the dashboard`. Nothing measurable, so the agent wanders. Good: `all tests in test/auth pass and the lint step is clean, or stop after 15 turns`.

The rule that matters most: write the condition as what you want, not only how you will check it. The agent does exactly what the condition measures and nothing else. If the condition only measures correctness, you can get a correct result that is still useless. State what “good” looks like, including the parts that are harder to assert than an exit code. The most reliable way to do that is to point the condition at a known-good reference (an example, a built prototype, a design file) instead of describing quality in adjectives.

A PRD or spec is useful as the context the work runs against, but it is not the goal. Keep the PRD as background and the condition itself short, precise, and measurable. A long document pasted in as the goal is not a goal; the agent still needs one clear statement of when to stop.

## When to use it, when not to

Use it when “done” is something Claude can prove mechanically and the proof lands in the transcript: tests pass, build is green, a queue is empty, every module is under a size budget.

## Get Jason Croucher’s stories in your inbox

Join Medium for free to get updates from this writer.

Do not use it when “done” is a judgement: looks good, feels right, is well designed, is fun. The evaluator runs no tools and only reads the transcript, so it cannot check those directly. For that kind of work, either encode the quality as something checkable (the rule above) or use a heavier setup with a separate evaluator that actually exercises the running result, for example a planner-generator-evaluator strategy that drives the app through Playwright. That is more to build and run, and it still does not guarantee a good result; it only catches what a transcript summary hides.

## The one failure mode to know

The agent optimises exactly what the condition measures and ignores everything else, because nothing unmeasured can fail the goal. A condition that is fully verifiable but measures the wrong things produces a provably correct, useless result. (A `/goal` build of a game whose condition specified determinism, invariants, and a completability playtest, but nothing about visuals, passed every clause and produced a working game with no art.) The fix is not a stricter evaluator. It is a condition that measures what you actually want.

## Gotchas

- The evaluator is a separate model, but not an independent check. It only reads the transcript, runs nothing, and sees only what the worker wrote down. A confident summary of broken work reads as “fine”.
- The turn or time bound is judged by the model from the conversation, not a hard mechanical stop.
- `/goal pause` and `/goal resume` do not exist in Claude Code. They belong to the Codex CLI's separate `/goal`. Claude Code has no pause or resume, and no "pursuing/paused/achieved/unmet/budget-limited" state vocabulary; it is active, then achieved (auto-clears) or cleared.
- `/clear` silently clears an active goal.

## A worked example: three games from one PRD

The full example is a public repo: [github.com/jason-c-dev/claude-slash-goal-example](https://github.com/jason-c-dev/claude-slash-goal-example). It builds the same side-scrolling space shooter three times, once per visual era (70s vector, 80s/90s 8-bit, modern), each an independent build verified by a deterministic headless playtest. `docs/PRD.md` is the spec; `docs/GOAL-PROMPT.md` is the prompt that produced it.

This is the failure mode and the fix from the sections above, run end to end. The first attempt at this game used a verification-only condition and produced a correct, unplayable result. The PRD opens by saying so, in its own words:

> *The first attempt at this game from a verification-only spec produced something correct but visually embarrassing (a 960×540 canvas with a triangle, a dot, and three starfield pixels). It passed every machine check and was still a shoebox. This PRD exists so that does not happen again.*

## The PRD is the product spec; the condition points at it

The PRD turns “what good looks like” into checkable requirements instead of adjectives. Two examples from it:

- A hard difficulty rule, not a feel: “Each boss is measurably harder than the previous: strictly more HP AND a strictly higher attack-rate,” written as `bossHP(k) > bossHP(k-1)` for k = 2..5.
- A per-version visual assertion: for the 70s build, an automated check asserts the renderer uses stroke and line primitives only, no filled sprites. The 8-bit and modern builds have their own.

The `/goal` condition stays short and points at the PRD: build exits 0; a deterministic headless playtest prints per-level `COMPLETABLE`; the invariants and determinism hold; a scripted bot proves challenge (a deliberately naive bot must fail the later levels while a skilled bot clears them); each version's visual assertion passes. The PRD is the context; the condition is the short, bounded statement of done.

## Results

Each version was a single `/goal` run.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*OIU_6QhrVu23Vu0q92FKeQ.png)

Each reached “achieved” in a single turn: the condition was met on the first pass, so the loop did not need to iterate. The modern build cost roughly twice the time and tokens of the other two, which tracks with its heavier rendering.

What matters is what “achieved” meant this time. With the first, verification-only condition, `/goal` also self-certified "achieved" on a shoebox. With the product-spec condition, "achieved" required a scripted bot to play all five levels, a naive bot to actually die on the later ones, each version's look to pass its own assertion, and determinism to hold across three runs. Same command and same loop both times. The only thing that changed was the condition.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*qb_pcUNK_zS-Pz_0.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*4BATYs1r_dFJZ6tZ.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*XWspzG_NpsJVm0hz.png)

One honest caveat carried from the build: the modern version’s headless playtest renderer stubs text drawing, so its headless screenshots show no HUD; it renders correctly in a browser (that capture is in the repo). The visual assertion passed without ever checking for the HUD, which is the same lesson one level down. It measured the effects it was told to measure, not the HUD it was not.

Try the games yourself, and if you are old enough, enjoy the trip down memory lane. They will not win any awards, but games are hard to build, and Claude read the spec, developed, play-tested, and worked towards a goal for all three in about 91 minutes across the three runs. That is a great example of `/goal` in action.

> Jason Croucher works at AWS helping customers build in the cloud using agentic solutions. He writes regularly about the practical realities of building AI agents on Medium. The views expressed here are his own and do not necessarily represent those of his employer, Amazon or its customers.