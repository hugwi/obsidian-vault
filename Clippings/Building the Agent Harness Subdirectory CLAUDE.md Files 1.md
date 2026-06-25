---
title: "Building the Agent Harness: Subdirectory CLAUDE.md Files"
source: https://dev.to/tacoda/building-the-agent-harness-subdirectory-claudemd-files-dcl
author:
  - "[[dev.to]]"
published: 2026-04-08
created: 2026-06-25
rating: 
action: 
description: The technical deep-dive on the harness system. Why one big instruction file doesn't scale, how subdirectory CLAUDE.md files scope guidance, and what goes in each one. Tagged with ai, architecture, programming, claude.
tags:
  - clippings
  - agentic-engineering
  - subdirectory-structure
  - claude-md
  - automatic-feedback
---
## One Big File Doesn't Scale

Claude Code reads a `CLAUDE.md` file at the root of your project. It's the primary way to give the agent project-specific instructions. And for small projects, it works great.

For this project, it didn't.

The root `CLAUDE.md` grew to cover architecture, testing conventions, API patterns, legacy patterns, SPA patterns, service design, migration strategy, authorization rules, database conventions, and more. The file was huge. Every time Claude started working in *any* part of the codebase, it loaded *all* the instructions into context.

Two problems:

1. **Context window bloat.** Instructions about database migrations are irrelevant when writing React components. But they're eating context tokens.
2. **Signal-to-noise ratio.** When everything is important, nothing is. The agent has to parse 500 lines of instructions to find the 20 that matter for the current task.

The solution: subdirectory `CLAUDE.md` files.

## The Harness Architecture

Claude Code loads `CLAUDE.md` files hierarchically. If you're working in `app/Actions/`, it loads:

1. The root `CLAUDE.md`
2. `app/Actions/CLAUDE.md` (if it exists)

This means you can put *scoped* guidance in subdirectories. The agent only loads instructions relevant to where it's working. The root file has the big picture. The subdirectory files have the specifics.

Here's the harness layout:

```swift
CLAUDE.md                              ← Project overview, architecture, shared rules
app/Http/Controllers/Api/CLAUDE.md     ← API controller patterns
app/Http/Controllers/Web/CLAUDE.md     ← Legacy controller rules (bug fixes only)
app/Actions/CLAUDE.md                  ← Action class patterns, Result DTOs
app/Services/CLAUDE.md                 ← Service contracts, strategy pattern
app/Http/Resources/CLAUDE.md           ← API Resource conventions
app/Policies/CLAUDE.md                 ← Authorization patterns
database/migrations/CLAUDE.md          ← Migration naming, column types
tests/CLAUDE.md                        ← Test patterns, UserFactory, TDD workflow
resources/js/spa/CLAUDE.md             ← SPA architecture, Interim wrappers
```

## Agent Harness Structure

Subdirectory `CLAUDE.md` files provide scoped guidance. The agent loads only the files relevant to its current working directory.

## Directory Layout:

```nix
CLAUDE.md                                ← Root: project overview, architecture, shared rules
├── app/
│   ├── Http/
│   │   ├── Controllers/
│   │   │   ├── Api/CLAUDE.md            ← API controller patterns (growth direction)
│   │   │   └── Web/CLAUDE.md            ← Legacy controllers (bug fixes only)
│   │   └── Resources/CLAUDE.md          ← API Resource conventions
│   ├── Actions/CLAUDE.md                ← Action pattern, Result DTOs
│   ├── Services/CLAUDE.md               ← Contract-first design, strategy pattern
│   └── Policies/CLAUDE.md               ← Authorization patterns
├── database/
│   └── migrations/CLAUDE.md             ← Migration naming, column types
├── tests/CLAUDE.md                      ← Test patterns, UserFactory, TDD
└── resources/
    └── js/spa/CLAUDE.md                 ← SPA architecture, Interim wrappers
```

## Harness Table Excerpt (from root CLAUDE.md)

Subdirectory `CLAUDE.md` files provide detailed patterns and constraints for each layer of the codebase. Read the relevant file before working in that area.

| Area | Harness File | Summary |
| --- | --- | --- |
| API Controllers | `app/Http/Controllers/Api/CLAUDE.md` | QueryBuilder, Resources, thin controllers |
| Web Controllers | `app/Http/Controllers/Web/CLAUDE.md` | Legacy. Bug fixes only, no new features. |
| React SPA | `resources/js/spa/CLAUDE.md` | SPA source of truth; Interim wrappers |
| Services | `app/Services/CLAUDE.md` | Contract-first, strategy pattern |
| Actions | `app/Actions/CLAUDE.md` | Single execute(), Result DTOs |
| Tests | `tests/CLAUDE.md` | UserFactory, ApiTestCase, TDD workflow |
| API Resources | `app/Http/Resources/CLAUDE.md` | allowedIncludes(), casting conventions |
| Policies | `app/Policies/CLAUDE.md` | Role helpers, scoping patterns |
| Migrations | `database/migrations/CLAUDE.md` | Naming, nullability, soft deletes |

When building a new feature, the typical flow touches these harness files:

1. **Migrations** — schema changes
2. **Actions/Services** — business logic
3. **API Controllers + Resources** — expose via API
4. **SPA** — React page, API client, types
5. **Tests** — PHP and JS tests throughout (TDD)

## Pre-Commit Verification (from root CLAUDE.md)

Before a change can be committed, complete these steps in order:

1. **Code quality**: `make lint` — all checks must pass
2. **PHP tests**: `make test` — all PHPUnit tests must pass
3. **JS tests**: `make test-js` — all Vitest tests must pass
4. **Browser verification** (UI changes only): Puppeteer MCP
5. **E2E tests**: Ask before running. If approved, `make e2e`.

Fix any failures before proceeding to the next step.

## Feedback Protocol (from root CLAUDE.md)

All feedback about code quality, patterns, or practices follows this loop:

1. Update the appropriate `CLAUDE.md` harness file to capture the pattern
2. Reload that harness file into context
3. Re-attempt the change using the updated guidance

This ensures the harness evolves with every review and the team benefits from accumulated decisions.

When Claude works on an API controller, it sees the root CLAUDE.md (architecture, roles, domain model) plus the API controller harness (QueryBuilder patterns, Resources, thin controllers). It doesn't see the migration naming rules or the SPA component patterns. Clean context. Relevant guidance.

## What Goes in Each Harness File

Each harness file follows the same structure:

1. **What this area is** — one sentence
2. **Design direction** — where we're headed (growth area vs. legacy)
3. **Patterns** — code examples the agent should follow
4. **Rules** — explicit do/don't constraints
5. **What NOT to do** — anti-patterns with explanations

Let me walk through a few.

### Actions Harness

The Actions harness defines the single-execute pattern:

```
## Action Class Pattern

- One public method: \`execute()\`
- Accept a Form Request or typed parameters — not raw arrays
- Return a Result DTO — not a model or array
- Inject services via constructor
- Fire domain events for audit trails and side effects
```

It includes the Result DTO pattern with named constructors:

```php
public static function succeeded(Thing $thing): self
{
    return new self(success: true, thing: $thing);
}

public static function failed(string $error): self
{
    return new self(success: false, error: $error);
}
```

And explicit anti-patterns:

```
## What NOT to Do

- Do not put HTTP concerns in Actions — no response codes, redirects, or JSON
- Do not access \`Request\` objects directly — accept Form Requests passed by the controller
- Do not create Actions for simple CRUD that the controller can handle
- Do not add multiple public methods — one Action, one execute(), one responsibility
- Do not return raw models or arrays — always return a Result DTO
```

## app/Actions/CLAUDE.md

This is a real harness file from the project. It tells the agent exactly how to write Action classes.

## Actions

Actions encapsulate a single domain operation. They are the primary pattern for complex write operations that go beyond simple CRUD.

## When to Use an Action

- The operation involves multiple models, side effects, or conditional logic
- The operation is called from a controller but the logic is too complex
- The operation needs to be reusable across web and API controllers

Simple CRUD (create a record, update a field) can stay in the controller.

## Action Class Pattern

```php
namespace App\Actions\{Domain};

class DoThingAction
{
    public function __construct(
        private SomeDependency $dependency,
    ) {}

    public function execute(DoThingRequest $request, User $user): DoThingResult
    {
        // Orchestrate the operation
        return new DoThingResult(thing: $thing, shouldDoMore: $flag);
    }
}
```

### Rules

- One public method: `execute()`
- Accept a Form Request or typed parameters — not raw arrays
- Return a Result DTO — not a model or array
- Inject services via constructor
- Fire domain events for audit trails and side effects

## Result DTO Pattern

```php
class DoThingResult
{
    public function __construct(
        public readonly bool $success,
        public readonly ?Thing $thing = null,
        public readonly ?string $error = null,
    ) {}

    public static function succeeded(Thing $thing): self
    {
        return new self(success: true, thing: $thing);
    }

    public static function failed(string $error): self
    {
        return new self(success: false, error: $error);
    }
}
```

## What NOT to Do

- Do not put HTTP concerns in Actions (response codes, redirects, JSON)
- Do not access `Request` objects directly
- Do not create Actions for simple CRUD
- Do not add multiple public methods
- Do not return raw models or arrays
- Do not catch authorization exceptions inside Actions
- Do not put query/listing logic in Actions

When Claude creates a new Action, it reads this file and follows the pattern. Every time. It doesn't invent its own approach. It doesn't return raw models. It doesn't add multiple public methods. Because the harness says not to.

### Tests Harness

The Tests harness is one of the most detailed because tests are the quality gate:

```markdown
## Performance

- **CRITICAL: Never run multiple test processes simultaneously**
- **Run \`make test\` exactly once** as a final check before commit
- **TIMEOUT MUST BE AT LEAST 20 MINUTES**
- **Frontend-only changes**: Skip \`make test\` — run \`make test-js\` and \`make lint\` only
```

It defines the `UserFactory` pattern so the agent never uses the wrong factory:

```livescript
### UserFactory (Test Facade)

Always use the test UserFactory facade for creating test users:

    use Facades\Tests\Setup\UserFactory;

    $admin = UserFactory::admin()->create();
    $user = UserFactory::withPermissions('things.manage')->create();

Do NOT use \`User::factory()->create()\` directly in tests.
```

And it prioritizes test coverage:

```markdown
### Test Coverage Priorities

1. Authentication (401 for unauthenticated)
2. Authorization (403 for unauthorized)
3. Validation (422 for invalid input)
4. Happy path (200/201 for valid operations)
5. Edge cases and business rules
6. Event/notification firing
```

### Web Controllers Harness

This is the shortest harness file, and that's intentional:

```
# Web Controllers (Legacy)

Bug fixes only. No new features. No new routes. No new views.

New features go in API controllers + React SPA pages.
```

The brevity is the message. When Claude opens a web controller, the harness immediately tells it: you're in legacy territory. Fix bugs. Don't build here.

### SPA Harness

The SPA harness covers the interim wrapper pattern, component structure, and the relationship between SPA and legacy contexts:

```
## Interim Wrappers

Interim wrappers are a release mechanism, not a separate architecture.
The SPA component is always the source of truth.

The wrapper only passes URL props that differ between contexts.
New features and bug fixes go into the SPA component.
```

This prevents a common mistake: Claude building features in the interim wrapper instead of the SPA component. The harness makes the hierarchy explicit.

## The Root CLAUDE.md

The root file handles the big picture:

- Project overview and tech stack
- The two-frontend architecture and migration direction
- Scoping rules (what goes where)
- Domain model overview (User roles, Order lifecycle, etc.)
- Makefile commands
- Pre-commit verification steps
- The TDD workflow

It also contains a **harness table** that maps areas to their harness files:

```
| Area | Harness File | Summary |
|------|-------------|---------|
| API Controllers | \`app/Http/Controllers/Api/CLAUDE.md\` | Growth direction |
| Web Controllers | \`app/Http/Controllers/Web/CLAUDE.md\` | Legacy, bug fixes only |
| React SPA | \`resources/js/spa/CLAUDE.md\` | SPA source of truth |
| Services | \`app/Services/CLAUDE.md\` | Contract-first design |
| Actions | \`app/Actions/CLAUDE.md\` | Single execute(), Result DTOs |
| Tests | \`tests/CLAUDE.md\` | UserFactory, TDD workflow |
```

This table is surprisingly important. It tells Claude, and human developers, that guidance exists and where to find it. Without the table, harness files might go unread.

## The Feedback Protocol

The harness isn't static. It evolves with every review.

```
## Feedback Protocol

1. Update the appropriate CLAUDE.md harness file
2. Reload that harness file into context
3. Re-attempt the change using the updated guidance
```

When Claude does something wrong:

- If it's a harness gap → update the harness
- If it's a one-off mistake → correct inline
- If it's a recurring pattern → add it to the "What NOT to Do" section

The reload step is key. After updating a harness file, Claude re-reads it in the same conversation. The correction applies immediately, not just in the next session. And because the harness file is committed to the repo, it applies to *all* future sessions.

This creates a ratchet effect. The harness gets better with every review. Mistakes that happen once get encoded as rules. Over time, the agent's first-attempt accuracy improves because the guidance accumulates lessons.

## The Harness Checks Its Own Work

The harness includes pre-commit verification steps:

```markdown
## Pre-Commit Verification

1. \`make lint\` — all checks must pass
2. \`make test\` — all PHPUnit tests must pass
3. \`make test-js\` — all Vitest tests must pass
4. Browser verification (UI changes only)
5. E2E tests (ask before running)
```

This is the harness checking its own output. The agent writes code, then runs the same quality gates that a human would. If anything fails, the agent fixes it before presenting the diff for review.

The agent doesn't need me to tell it "run the tests." The harness says to. It's part of the workflow, not an afterthought.

## Design Decisions

**Why CLAUDE.md files instead of custom tooling?**  
Simplest thing that works. `CLAUDE.md` files are plain Markdown, checked into the repo, version-controlled, reviewable in PRs. No custom tool to build, maintain, or explain. Any developer can read them. Any developer can update them.

**Why one file per directory instead of one giant file?**  
Context control. When you're in `app/Actions/`, you need Action patterns. When you're in `tests/`, you need test patterns. Loading everything everywhere wastes context and drowns the signal.

**Why include code examples?**  
Because patterns are easier to follow than rules. "Return a Result DTO" is a rule. Showing the `succeeded()` / `failed()` static constructors is a pattern the agent can copy. It'll copy the pattern before it reads the rule.

**Why include "What NOT to Do"?**  
Because agents learn from examples, including negative examples. If the harness only shows what to do, the agent might still do the wrong thing in novel situations. Anti-patterns draw explicit fences.

## The Takeaway

Building an agent harness:

1. **Start with the root CLAUDE.md.** Project overview, architecture, shared conventions.
2. **Add subdirectory files where patterns matter.** Actions, Services, Tests, SPA, and any other area with specific conventions.
3. **Keep each file focused.** Pattern + rules + anti-patterns. Nothing more.
4. **Include code examples.** The agent follows what it sees.
5. **Include a harness table** in the root file so nobody misses the guidance.
6. **Update the harness on every review.** Corrections become rules. Rules prevent recurrence.
7. **Let the harness check its own work.** Pre-commit verification built into the workflow.

The harness is not documentation for humans. It's guidance for an autonomous agent. Design it that way: specific, scoped, verifiable, and always evolving.

DEV Community

[![Google AI Education track image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu09y9fffqrb2one15j3g.png)](https://dev.to/deved/build-apps-with-google-ai-studio?bb=238784)

## Work through these 3 parts to earn the exclusive Google AI Studio Builder badge!

This track will guide you through Google AI Studio's new "Build apps with Gemini" feature, where you can turn a simple text prompt into a fully functional, deployed web application in minutes.