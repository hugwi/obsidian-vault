---
title: "Getting Claude to Actually Read Your CLAUDE.md"
source: "https://www.humanlayer.dev/blog/stop-claude-from-ignoring-your-claude-md"
author:
published: 2026-03-17
created: 2026-06-07
description: "Using conditional XML blocks to make Claude pay attention to the right instructions at the right time."
tags:
  - "to-process"
  - agent-configuration
---
Claude Code wraps your CLAUDE.md in a `<system_reminder>` that explicitly tells the model the contents "may or may not be relevant." The longer your file gets, the more Claude seems to treat individual sections as optional.

We [wrote before](https://www.humanlayer.dev/blog/writing-a-good-claude-md) about keeping these files concise and avoiding stuff that belongs in a linter. But even after trimming things down, I kept running into cases where Claude would ignore testing instructions while writing tests, or skip our API conventions when building endpoints.

## \## Conditional <important if> blocks

==What's been working for me: wrapping sections in `<important if="condition">` tags.==

```
<important if="you are writing or modifying tests">
- Use \`createTestApp()\` helper for integration tests
- Mock database with \`dbMock\` from \`packages/db/test\`
- Test fixtures live in \`__fixtures__/\` directories
</important>
```

We don't have a rigorous explanation for why this helps. My guess is that the explicit condition gives Claude a clearer signal about when to apply the instructions, rather than leaving it to decide relevance on its own. Whatever the mechanism, we've seen noticeably better adherence on tasks where only some sections of my CLAUDE.md should apply.

A few things I've learned:

**Don't wrap everything.** Project identity, directory structure, and tech stack are relevant to basically every task. The conditional blocks are for testing setup or deployment procedures that only matter sometimes.

**Make conditions specific.** `<important if="you are writing code">` matches almost everything and defeats the purpose. I try to make each condition narrow enough that it only fires when I actually want those rules applied.

## \## A skill to automate this

I did a lot of restructuring CLAUDE.md files by hand, so I made a Claude Code skill that does the rewrite. It pulls out the foundational stuff, wraps domain-specific sections in conditional blocks, and cleans up some common problems (stale code snippets, style rules that should be in a linter, vague instructions that don't actually help).

It's not perfect—you'll probably want to review what it produces—but it's a decent starting point.

## \## Try it

```dockerfile
npx skills add humanlayer/skills --skill improve-claude-md
```

Then in your project:

```bash
/improve-claude-md
```

It reads your existing CLAUDE.md and outputs a rewritten version. Source is at [github.com/humanlayer/skills](https://github.com/humanlayer/skills/tree/main/plugins/improve-claude-md).