# CLAUDE.md Writing Guide: Context Engineering for AI CLI Tools

![rw-book-cover](https://www.termdock.com/apple-touch-icon.png)

## Metadata
- Author: [[Danny Huang]]
- Full Title: CLAUDE.md Writing Guide: Context Engineering for AI CLI Tools
- Category: #articles
- Summary: CLAUDE.md files provide essential, focused context that helps AI agents understand a project without overload. They should be concise, avoid redundancy, and include architecture, constraints, commands, and conventions. Keep CLAUDE.md under 100 lines, test it with real tasks, and move task-specific info to SKILL.md files.
- URL: https://www.termdock.com/en/blog/claude-md-writing-guide

## Full Document
In the early days of aviation, pilots carried handwritten checklists. Short, precise, tested against real failures. Then airlines started adding pages. Procedures for every conceivable scenario. The checklists grew so thick that pilots skipped them entirely during emergencies — the very moment they mattered most.

Context files for AI agents followed the same arc. In February 2026, ETH Zurich published [Evaluating AGENTS.md](https://arxiv.org/abs/2602.11988) — the first rigorous study on the subject. The finding that matters: LLM-generated context files *decreased* task success rates by 3% compared to using no context file at all. Human-written files improved success by only 4%, while increasing inference costs by over 20%.

The takeaway is not that context files are useless. It is that most are badly written. Too long, too redundant, filled with information the agent can already find by reading your code.

This guide shows you how to write a CLAUDE.md from scratch that lands on the right side of that 4% improvement — and avoids the patterns that push you into the negative. If you already have a CLAUDE.md and want to audit it for problems, start with [10 CLAUDE.md Mistakes That Hurt Your AI Agent](https://www.termdock.com/en/blog/claude-md-common-mistakes) first.

Before you start writing:

* **Claude Code installed and working.** If not, the [First Hour with Claude Code](https://www.termdock.com/en/blog/claude-code-first-hour) tutorial covers installation.
* **A real project to write for.** Do not write a CLAUDE.md in the abstract. Open the project you work on daily.
* **10 minutes.** A good CLAUDE.md is short. If it takes longer than 10 minutes, you are overwriting it.

Understanding the loading mechanism tells you what to put where. Think of it as a layered lens system — each lens adds focus, but too many lenses blur the image.

Claude Code reads CLAUDE.md at multiple levels, and they all combine:

1. **Global** — `~/.claude/CLAUDE.md` loads for every project. Put your personal coding preferences here (language, communication style, universal constraints).
2. **Project root** — `./CLAUDE.md` in the project root loads at session start. This is the main file. Architecture, conventions, commands.
3. **Subdirectories** — `./packages/api/CLAUDE.md` loads on demand when Claude accesses files in that directory. Use this for package-specific context in monorepos.
4. **Personal overrides** — `.CLAUDE.local.md` is gitignored. Use it for personal preferences that should not be shared with the team.

Levels combine without replacing each other. More specific levels override on conflict. This means your project root CLAUDE.md should not repeat anything from your global file, and subdirectory files should not repeat anything from the root.

Claude also reads `~/.claude/rules/*.md` files for modular rule sets. The rules directory is useful for separating concerns — a communication style file, a banned packages file, a workflow file — without cramming everything into one CLAUDE.md.

A good CLAUDE.md has five sections. Not every project needs all five, but this structure covers the full range of what the agent genuinely cannot infer from your code.

What it is, how it fits together, what decisions the code does not make obvious.

```
## Architecture
- Next.js 15 App Router, TypeScript strict, Tailwind CSS
- Database: PostgreSQL 16 via Drizzle ORM
- Auth: NextAuth.js v5 (GitHub + Google providers)
- Monorepo: apps/web, apps/api, packages/shared
- API layer: tRPC — all client-server calls go through tRPC routers

```

This section answers the question an agent asks on cold start: "What kind of project is this?" The code shows individual files. This section shows how they connect — like a wiring diagram for an unfamiliar building.

**What not to include:** Version numbers for every dependency (the agent reads `package.json`), framework features you use in standard ways (if you use Next.js App Router like the docs show, the agent knows), or anything a `package.json` scan reveals.

Patterns the agent should follow that are not enforced by linters or type checkers.

```
## Conventions
- Server components by default; 'use client' only for interactivity or browser APIs
- Error handling: Result<T, E> pattern (see src/lib/result.ts)
- Named exports preferred; default exports only for pages/layouts
- Database queries live in src/repositories/ — never in route handlers or components
- All new API endpoints need an integration test in tests/integration/

```

Each line states a preference and, where useful, the exception. "Prefer X; use Y only when Z" is the right format. Avoid bare "ALWAYS" and "NEVER" — they leave no room for legitimate exceptions and make the agent rigid. See [Mistake 5 in the common mistakes guide](https://www.termdock.com/en/blog/claude-md-common-mistakes) for detailed examples.

Hard boundaries. Things the agent must never do, because doing them causes damage that is expensive to fix.

```
## Constraints
- Never modify files in prisma/migrations/ — generate new migrations instead
- Never change the signature of functions exported from src/api/public/
- Never delete test fixture files in tests/fixtures/ (loaded dynamically by name)
- Never commit .env files or hardcode secrets
- GraphQL schema changes require running pnpm codegen after modification

```

Conventions are "prefer this." Constraints are "do not touch this, ever." The difference matters. Think of conventions as lane markings on a highway — they guide direction. Constraints are guardrails on a cliff edge — they prevent catastrophe. Keep constraints short, specific, and targeted at recoverable-but-costly mistakes. If a constraint is longer than one line, it probably belongs in a [skill](https://www.termdock.com/en/blog/skill-md-vs-claude-md-vs-agents-md) instead of CLAUDE.md.

How to build, test, lint, and run the project. The agent should never have to guess.

```
## Commands
- Install: pnpm install
- Dev: pnpm dev (starts all apps)
- Test unit: pnpm test:unit
- Test e2e: pnpm test:e2e (requires running dev server)
- Lint: pnpm lint
- Build: turbo build
- DB migrate: pnpm db:migrate
- DB seed: pnpm db:seed

```

If your project uses standard `npm test` and `npm run build`, you can skip this section — the agent knows the defaults. But the moment you have a monorepo, custom scripts, or non-standard test runners, these commands become the highest-value lines in your file.

Project-specific patterns that recur across tasks. Only include these if the pattern is non-obvious and the agent has gotten it wrong before.

```
## Patterns
- New pages: create route in app/(dashboard)/[route]/page.tsx, add nav entry in src/config/navigation.ts
- New API endpoint: define tRPC router in src/server/routers/, register in src/server/root.ts
- Feature flags: use src/lib/flags.ts — check with `isEnabled('flag-name')`, never hardcode booleans

```

This section is optional because many projects do not have recurring patterns complex enough to document. If you find yourself adding more than 5 patterns, move them to skills instead — they are task-specific knowledge that should load on demand, not always-on context. See [context engineering with skill layering](https://www.termdock.com/en/blog/context-engineering-skill-layering) for the full architecture.

Here is the full CLAUDE.md for a mid-size Next.js SaaS application, all five sections:

```
## Architecture
- Next.js 15 App Router, TypeScript strict, Tailwind CSS
- Database: PostgreSQL 16 via Drizzle ORM
- Auth: NextAuth.js v5 (GitHub + Google providers)
- API: tRPC routers in src/server/routers/
- Payments: Stripe SDK, webhooks in src/app/api/webhooks/stripe/

## Conventions
- Server components by default; 'use client' only for interactivity
- Error handling: Result<T, E> pattern (src/lib/result.ts)
- Named exports; default exports only for pages/layouts
- DB queries in src/repositories/, never in handlers or components
- New endpoints need integration tests in tests/integration/

## Constraints
- Never modify files in drizzle/migrations/
- Never change exported function signatures in src/lib/public-api/
- Never delete test fixtures in tests/fixtures/
- All Stripe webhook handlers must verify signature first

## Commands
- Dev: pnpm dev | Test: pnpm test | Lint: pnpm lint
- Build: pnpm build | DB migrate: pnpm db:migrate

## Patterns
- New page: app/(dashboard)/[route]/page.tsx + src/config/nav.ts
- New tRPC router: src/server/routers/ → register in root.ts
- Feature flag: isEnabled('name') from src/lib/flags.ts

```

Twenty-eight lines. It covers architecture, conventions, constraints, commands, and patterns. Everything the agent needs to make correct structural decisions on first contact. Everything else — detailed migration workflows, deployment checklists, API documentation — belongs in skills or actual documentation files.

Your CLAUDE.md loads into every session. Every token in it competes with the agent's reasoning capacity and the tokens available for your actual task.

The math is straightforward:

| File Size | Estimated Tokens | % of 200K Context Window |
| --- | --- | --- |
| 30 lines (lean) | ~450 | 0.2% |
| 100 lines (max recommended) | ~1,500 | 0.75% |
| 300 lines (too long) | ~4,500 | 2.3% |
| 1000 lines (harmful) | ~15,000 | 7.5% |

The ETH Zurich study found that context files increased inference costs by over 20% while providing minimal benefit. The root cause: most of those files were 200-500 lines of mixed-quality content. The 5% rule is a practical ceiling — your always-on context (CLAUDE.md + any global rules) should consume less than 5% of the model's effective context window. For a 200K token model, that is under 10,000 tokens.

At 30-100 lines, a well-written CLAUDE.md stays well under 1% — leaving virtually all the context window for your code and the agent's reasoning.

**When to move content to skills:** If a section of your CLAUDE.md applies to only one type of task (database migrations, deployment, code review), it belongs in a [SKILL.md](https://www.termdock.com/en/blog/skill-md-vs-claude-md-vs-agents-md). Skills load on demand, so they cost zero tokens when unused.

Writing the file is half the work. Testing it is the other half. Think of it the way an engineer tests a bridge — not by admiring the blueprints, but by driving a truck across it.

**Step 1: The cold start test.** Open a new Claude Code session in your project. Ask the agent to describe your project's architecture. If it correctly identifies your stack, patterns, and constraints without reading additional files, your CLAUDE.md is working.

**Step 2: The constraint test.** Ask the agent to do something your constraints forbid. "Modify the migration file to fix this column type." If the agent refuses and explains why, the constraint is being read. If it happily modifies the file, something is wrong — either the constraint is buried in too much text, or the wording is ambiguous.

**Step 3: The command test.** Ask the agent to run your test suite. If it uses the correct command on the first attempt, your commands section is working. If it guesses `npm test` when you need `pnpm test:unit`, the commands section is missing or not prominent enough.

**Step 4: The convention test.** Ask the agent to create a new component or endpoint. Check whether it follows your stated patterns — puts the file in the right directory, uses the right error handling approach, follows your export conventions. If it deviates, your conventions section needs sharper wording.

**Step 5: The noise test.** Remove a section you suspect might be redundant. Run the same tasks. If agent behavior does not change, that section was wasted tokens. Be aggressive about pruning.

A CLAUDE.md is a living document, not a write-once artifact. Like a well-maintained logbook, it records what matters and discards what does not.

**Add when:**

* The agent makes the same mistake twice. First time is a fluke. Second time means you need a constraint or convention.
* You introduce a new architectural pattern (new auth provider, new API layer, new database).
* A new team member joins and the agent gives them wrong guidance — this surfaces gaps.

**Prune when:**

* A convention has been followed perfectly for 20+ sessions. The agent may have internalized it from the code itself. Test by removing the line and checking.
* A tool or pattern is deprecated. Dead constraints about old libraries confuse the agent.
* The file exceeds 100 lines. Something in there does not need to be always-on.

**Review cadence:** Check your CLAUDE.md every 2 weeks. Read every line. For each one, ask: "If I remove this, will the agent make a mistake it cannot recover from by reading the code?" If the answer is no, delete it.

These three files solve different problems. A quick overview of when to use which:

| File | Purpose | Loaded | Best For |
| --- | --- | --- | --- |
| AGENTS.md | Cross-tool project context | Every session | Architecture, conventions, constraints (read by all AI CLI tools) |
| CLAUDE.md | Claude Code-specific context | Every session | Claude-specific behavior (compaction, subagents) + reference to AGENTS.md |
| SKILL.md | Task-specific capability | On demand | Workflows, checklists, templates that only apply to specific tasks |

If your team uses only Claude Code, you can put everything in CLAUDE.md. The moment anyone uses Codex CLI, Gemini CLI, or Cursor, the portable context should move to AGENTS.md.

For the full comparison with detailed examples, see [SKILL.md vs CLAUDE.md vs AGENTS.md](https://www.termdock.com/en/blog/skill-md-vs-claude-md-vs-agents-md). For advanced layering patterns — progressive disclosure, token budgeting across layers, monorepo configuration — see [context engineering with skill layering](https://www.termdock.com/en/blog/context-engineering-skill-layering).

Before you commit your CLAUDE.md, verify:

| Check |  |
| --- | --- |
| Under 100 lines total |  |
| Has Architecture section with non-obvious decisions |  |
| Has Constraints section targeting costly mistakes |  |
| Has Commands for build/test/lint |  |
| No content the agent can find in package.json or tsconfig |  |
| No linter rules restated (agent runs the linter) |  |
| Conventions use "prefer" with exceptions, not bare ALWAYS/NEVER |  |
| Task workflows moved to skills, not inlined |  |
| File is committed to version control |  |
| Tested with at least 3 representative tasks |  |

If more than 2 items fail, revise before committing. A bad CLAUDE.md is worse than no CLAUDE.md — the ETH Zurich research proved this quantitatively.

When you are testing CLAUDE.md changes iteratively, a multi-panel terminal layout helps — run the agent in one pane, view the CLAUDE.md in another, and compare behavior side by side. [Termdock's](https://www.termdock.com/en) split-panel workspace makes this workflow fast: modify the file, restart the session in the adjacent pane, test immediately.

Open your project. Create a `CLAUDE.md` at the root. Write the five sections. Keep it under 50 lines on the first draft — you can always add later, but removing is harder than not adding. Test it with three real tasks. Prune anything the agent did not need.

The goal is not a comprehensive document. It is the minimum context the agent needs to make correct decisions from a cold start. Everything beyond that minimum is noise — and noise, as the research shows, makes your agent worse.

For the complete picture of context engineering across all major AI CLI tools, see the [AI CLI Tools Guide](https://www.termdock.com/en/blog/ai-cli-tools-guide).
