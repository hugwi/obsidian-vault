---
title: "Context-Efficient Backpressure for Coding Agents"
source: "https://www.humanlayer.dev/blog/context-efficient-backpressure"
author:
  - "[[Dex]]"
published: 2025-12-09
created: 2026-06-07
description: "Verbose test and build output wastes tokens and confuses agents. A simple wrapper script can dramatically improve agent performance."
tags:
  - "to-process"
  - context-management
---
Here's a pattern we use constantly at HumanLayer: swallow all test/build/lint output and replace it with a single `✓` if the stage passes.

If `exitCode != 0`, dump the stashed output to stdout. Otherwise, the agent never sees it.

## \## stay in the smart zone

You should try hard to stay in the [~75k token "smart zone"](https://youtu.be/rmvDxxNubIg?si=bbPvQb6-etG5wD_I&t=347) for claude models - every line of `PASS src/utils/helper.test.ts` is waste.

A jest/maven/pytest run might dump 200+ lines of output, and then your agent has to parse all of that to find the one failure it actually needs to fix.

==Or worse, if all tests are passing, you just threw away 2-3% of your context window for an "all good" result you could have conveyed in less than 10 tokens.==

You're **wasting context** - every token you use is diminishing the results and moves you closer to "need to clear or compact to get back to the smart zone".

And you should forget the token cost and time-it-takes-to-run concerns for now (we'll come back to time in a second), since **human** time wasted on wrangling an agent in the dumb zone is likely more expensive by 10x or more.

## \## a pretty dumb fix

Not a full fix, but in the right direction:

Rather than letting the model decide what to truncate, we like to take control of output deterministically.

```
run_silent() {
    local description="$1"
    local command="$2"
    local tmp_file=$(mktemp)

    if eval "$command" > "$tmp_file" 2>&1; then
        printf "  ✓ %s\n" "$description"
        rm -f "$tmp_file"
        return 0
    else
        local exit_code=$?
        printf "  ✗ %s\n" "$description"
        cat "$tmp_file"
        rm -f "$tmp_file"
        return $exit_code
    fi
}
```

Invoke it with

```
run_silent "fe integration tests" "bun run test:integration"
```

==Instead of 200 lines of test output, the agent sees:==

```
✓ Auth tests
✓ Utils tests
✗ API tests

FAIL src/api/users.test.ts
● should validate email format
  Expected: true
  Received: false
```

The model doesn't need to decide whether to truncate. You've already made that decision. Success = ✓. Failure = full output.

Now your only job is to convince the model not to do its own truncation. Maybe you can [shout at it in your claude.md](https://www.humanlayer.dev/blog/writing-a-good-claude-md).

## \## make it smaller over time

Once you have the basic wrapper working, iterate:

**Enable failFast.** `pytest -x`, `jest --bail`, `go test -failfast`. One failure at a time. Don't make the agent context-switch between five different bugs, or re-read the same "tests 2-5 are failing" output when its still trying to fix test #1.

**Filter the output.** Strip generic stack frames that don't help your agent find the issue. Remove timing info. grep/sed/awk/cut/etc your way to just the assertion that failed.

**Framework-specific parsing.** even [a pretty-hacky run\_silent.sh](https://github.com/humanlayer/humanlayer/blob/main/hack/run_silent.sh) extracts test counts from pytest, jest, go test, and vitest so you still get visibility without the noise.

We use this pattern heavily when working with customers who have Maven and Gradle projects (notoriously verbose), and it works equally well for xcodebuild, cargo, and anything else that spews.

Here's the humanlayer/humanlayer checks and tests for a monorepo - we run these in a pre-push hook, and some subset of these projects for each plan phase.

![output](https://www.humanlayer.dev/blog/context-efficient-backpressure/full-suite.png)

This would easily be half a context window worth of output without the wrappers.

## \## im tired of context-anxious models

The latest generation of models has spent so much time in the RL dungeon that they've overcorrected way too far on being conservative with how much context they load.

here's some patterns I've seen in the last few months:

#### \#### output swallowing

piping output to `/dev/null` and using an `||` operator to just print a message based on the commands exit code

![model wrapping bash](https://www.humanlayer.dev/blog/context-efficient-backpressure/model-wrap.png)

while its cool that we're being conservative, remember what cat would have printed without the output swallowing:

![cat output without wrapping](https://www.humanlayer.dev/blog/context-efficient-backpressure/cat-output.png)

In this trivial example, the guardrails actually use MORE TOKENS:

![/blog/context-efficient-backpressure/token-compare.png](https://www.humanlayer.dev/blog/context-efficient-backpressure/token-compare.png)

Disclaimers - 1) yes if cat had repeated the whole filename, that would have been more tokens. 2) this is an [unofficial tokenizer](https://claude-tokenizer.vercel.app/) and probably out of date

but you get my point here - the real nasty one comes next -

#### \#### piping to head / tail

I hear so many complaints about "oh it ran a 5 minute test suite with `head -n 50` and now it has to run it again"

```
venv/bin/python -m pytest -n 4 | head -n 50
```

If your tests take less than 30 seconds, great you probably don't care, but that's not the case for most of us. And again, we're gonna focus on **human time** wasted while the agent runs and re-runs test suites, or wasted on compacting/restarting a context window because too many tokens got used.

Ironically, in trying to conserve context and serve us better, models end up burning more tokens, more human time, and more mental energy.

I won't opine on why the product teams that focus on model behavior have leaned into this behavior, but I can only assume its at least in-broad-strokes intentional. It helps models perform well in codebases that **are not** thoughtful about context-efficiency of their [backpressure mechanisms](https://ghuntley.com/secure-codegen/#in-practice)

## \## its not your fault

Okay fine, opining time: things are this way because labs have to take big swings and the majority of their potential user base doesn't know how (or want to learn how) to do context engineering well. Sure, "don't make me think". But also, **let me think if I want to**.

[![gareth-tweet](https://www.humanlayer.dev/blog/context-efficient-backpressure/gareth.png)](https://x.com/gingerhendrixai/status/1998082340019446203)

As we always say - deterministic is better than non-deterministic. If you already know what matters, don't leave it to a model to churn through 1000s of junk tokens to decide.