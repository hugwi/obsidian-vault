---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - code-quality
  - context-management
  - harness
source: readwise
created: 2026-06-23
rating: 
action: 
theme: workflow-phases-gates
subtheme:
  - harness-loops
  - plan-phase
  - event-driven
---

# Stop Writing Rules in AGENTS.md: Use Agent Hooks and Nano-Staged Instead

![rw-book-cover](https://evilmartians.com/social-cards/chronicles/stop-writing-rules-in-agents-md-use-agent-hooks-and-nano-staged-instead.jpg)

## Metadata
- Author: [[Andrey Sitnik]]
- Full Title: Stop Writing Rules in AGENTS.md: Use Agent Hooks and Nano-Staged Instead
- Category: #articles
- Summary: Using agent hooks and tools like nano-staged to run linters is faster and more reliable than writing rules in AGENTS.md. Automating code style checks in scripts saves tokens and prevents errors that LLMs might forget. This setup improves feedback speed and keeps both humans and LLMs focused on shipping code.
- URL: https://evilmartians.com/chronicles/stop-writing-rules-in-agents-md-use-agent-hooks-and-nano-staged-instead

## Full Document
![Cover for Stop writing rules in AGENTS.md: use agent hooks and nano-staged instead](https://evilmartians.com/static/cf4b818259fcc3146a7d918147b4455f/cover.png?v=74078c49)
Small life hack: using agent hooks and pre-commit managers like [nano-staged](https://github.com/usmanyunusov/nano-staged) to run linters and safeguards is far more reliable—and faster—than asking an agent to do it in `AGENTS.md`. Read how five minutes of setup can mean a tighter loop and fewer tokens.

#### The extremely short version

1: Install `nano-staged` (or use [lefthook](https://lefthook.dev) if you have a non-JS project).

```
pnpm add --save-dev nano-staged
```

2: Create `.nano-staged.json` and use the right linters for each file type:

```
{
  "*": "oxfmt --no-error-on-unmatched-pattern",
  "**/*.{js,ts,jsx,tsx}": "oxlint",
  "**/*.css": "stylelint --fix"
}
```

```
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "./node_modules/.bin/nano-staged --unstaged --quiet --bail || exit 2"
          }
        ]
      }
    ]
  }
}
```

4: Since you’re already adding `nano-staged`, we recommend adding [husky](https://github.com/typicode/husky) to run it on `git commit` as well:

```
pnpm add --save-dev husky
pnpm husky init
echo "./node_modules/.bin/nano-staged" > .husky/pre-commit
```

#### Automatic safeguards

It’s fascinating how best practices for LLMs are similar to classic recommendations for human developers. And there’s an old rule:

>  If possible, an automation script (on CI or in a pre-commit hook) is better than an instruction in documentation.
> 
>  Code style rules, in particular, should live in a formatter or linter rather than in docs.
> 
>  

The same rule applies to LLM safeguards: it’s better to move a rule into a formatter config or a custom linter rule than to add it to `AGENTS.md`. LLMs often forget `AGENTS.md` instructions, and scripts are much more reliable and cheaper in tokens.

As an example, never put code format rules into `AGENTS.md`—it’s better to run [Prettier](https://prettier.io) or [oxfmt](https://oxc.rs/docs/guide/usage/formatter.html).

**If you see an LLM making the same error a few times, ask it to write a custom ESLint rule for it. LLMs are pretty good at that.**

Why does safeguard performance matter if it’s the LLM waiting for the result?

Safeguards may run multiple times. After every check, the LLM needs to check results and may call tools multiple times.

Faster tools mean a faster feedback loop for the LLM. Thirty seconds per hook × a dozen hooks per session × every engineer on your team is real money—both in terms of the clock on the wall’s hands spinning away and the psychological momentum your team loses watching a spinner instead of shipping.

The next-gen JS linters and formatters, [Biome](https://biomejs.dev), [oxlint](https://oxc.rs/docs/guide/usage/linter.html), and [oxfmt](https://oxc.rs/docs/guide/usage/formatter.html) run [**5-10 times faster**](https://github.com/oxc-project/bench-linter) than ESLint and Prettier.

oxfmt now has 1:1 compatibility with Prettier, and while plugin support is still in development, it already works with Vue and Svelte files.

[PostCSS creator shares how to make your open source popular](https://evilmartians.com/chronicles/how-to-make-your-open-source-popular)
oxlint is also production-ready, with one notable bonus: it supports custom JS plugins written for ESLint, so existing rules can be reused. It also has built-in TypeScript support. And because it uses the Go version of TypeScript, and since type checking and `.ts` file linting share the same type processing, running `oxlint` with TS can be 1.5-2× faster than calling `tsgo` and `oxlint` separately.

Another amazing feature of oxlint is built-in TypeScript support. First, it uses the Go version of TypeScript, which is significantly faster. But also, both type checking and `.ts` file linting need the same type processing. So using `oxlint` with TS can be 1.5-2 times faster than calling `tsgo` and `oxlint` without TS.

So, this is why we recommend using oxfmt and oxlint to speed up the feedback loop for the LLM.

At Evil Martians, we already use oxlint—including on the website you’re reading right now!

Modern agents have a very useful hooks feature that lets you run a script after specific events:

I highly recommend learning more about this feature; it’s the foundation for many clever tricks and optimizations.

I also recommend looking into `PostToolUse`/`PreToolUse` and `FileChanged` events.

For our task, we’ll need the `Stop` event, which fires when the LLM stops processing the prompt.

The hook’s script receives JSON on `stdin` with the data from the process.

Exit code `2` prevents Claude Code from stopping and continues the conversation. For Codex, you may need a `nano-staged` wrapper that prints `{"continue":true}\n` or `{"decision":"block","reason":"$out"}`.

The simple solution above has an issue if the LLM runs without human supervision: if it can’t fix a linter error, it will get stuck in an infinite loop burning tokens.

So for software factory usage, we recommend wrapping `nano-staged` with a custom script to prevent that:

```
#!/bin/bash

INPUT=$(cat)
ACTIVE=$(echo "$INPUT" | jq -r '.stop_hook_active')

# If we're already in a forced-continuation loop, don't block again
if [ "$ACTIVE" = "true" ]; then
  nano-staged || true
  exit 0
fi

nano-staged || exit 2
```

Why run linters against all of a project’s files if you’ve only changed one? This is why pre-commit managers were created. They run on the git `pre-commit` hook and only run linters/formatters on the changes staged for the new commit.

There have been experiments with finding tests related to changed files. But they weren’t trustworthy enough, and tests are still too slow for a `pre-commit` hook.

Pre-commit hooks are just as useful for LLMs as they are for people:

1. Why spend tokens on code style rules in `AGENTS.md` if code style can be auto-fixed by a script without boring the LLM (or the human)?
2. Before running long-running tests, it’s better to do quick linting and type checking on the changed files. That way, many small issues get caught with a quick feedback loop, and the long test task (maybe at the end of the session) is still there to run.

[lint-staged](https://github.com/lint-staged/lint-staged) is [the most popular tool](https://npmx.dev/compare?packages=lint-staged,nano-staged#trends-comparison-heading), but we recommend [nano-staged](https://github.com/usmanyunusov/nano-staged) instead because:

1. `nano-staged` has 0 dependencies vs. 24 dependencies in `lint-staged`. With the rising risk of supply chain attacks, it’s important to keep the attack surface as small as possible.
2. `nano-staged` has a few special optimizations for LLMs that reduce token usage.

For non-JS projects, we recommend [lefthook](https://lefthook.dev).

In the agent’s hook, we run `nano-staged` with special arguments:

* `--unstaged`: by default, `pre-commit` managers check staged files added for the next commit via `git add`. For this use case, we need to check all changed files.

If you want to use `nano-staged` not only in an LLM hook but also in a Git hook, you need a Git hook manager. We recommend the aforementioned [husky](https://typicode.github.io/husky/get-started.html) or [simple-git-hooks](https://github.com/toplenboren/simple-git-hooks) (if you don’t want an extra folder).

Adding a Claude Code hook with `nano-staged` is the perfect little task to start off the working day.

The bigger pattern: every rule you can encode as a tool is a rule the LLM can’t forget and a token you don’t have to spend reminding it. As agents “take” more of the keyboard, the difference between teams who automate their guardrails and teams who write them down in `AGENTS.md` will rapidly widen.

Hooks and pre-commit managers are the cheap, boring infrastructure that will keep you on the right side of things.

At Evil Martians, we’ve spent years building the OSS that quietly powers devtools: PostCSS, Lefthook, Nano Stores, plus dozens more. That said, the shift toward agentic coding doesn’t change the rule that automation beats documentation. LLMs need good DX just as much as any human.
