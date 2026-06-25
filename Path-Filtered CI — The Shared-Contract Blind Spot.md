---
categories:
  - "[[Resources]]"
domain: engineering
tags: [ci, monorepo, type-safety, incident, case-study]
created: 2026-06-23
---

# Case Study: Path-Filtered CI and the Shared-Contract Blind Spot

> A required field added to a shared package broke a downstream app, and the break
> reached `main` undetected — every PR was green. Two independent CI gaps stacked:
> PRs were not built against current `main`, and the consumer's CI never ran
> because its path-filter excluded the package that changed.

## Context

Monorepo with a `packages/shared` workspace package that defines zod schemas and
their inferred TypeScript types. Consumers (`app/`, `admin/`, `api/`) import
`packages/shared` **as source** — `app/tsconfig.app.json` has
`include: ["../packages/shared/src/**/*"]`, so `app`'s `tsc -b` typechecks app
test fixtures directly against the *current* shared schema. There is no compiled
`.d.ts` boundary in between; the coupling is direct, source-to-source.

Each app workflow is **path-filtered**. `app-ci.yml`:

```yaml
on:
  pull_request:
    paths: ['app/**', '.github/workflows/app-ci.yml']
  push:
    branches: [main]
    paths: ['app/**', '.github/workflows/app-ci.yml']
```

The intent is cost control: don't run app CI when only the backend changed. The
hidden assumption is that *app correctness only depends on `app/**`*. That
assumption is false the moment `app` consumes `packages/shared`.

## The signal the build actually sends

On `origin/main` (`cce2da7e`), `cd app && bunx tsc -b` fails:

```
TS2741  assessment-section-card.spec.tsx  → fixture missing 'regeneratingAt'
TS2739  use-assessment-mutations.spec.ts  → fixture missing 'generationStatus','generatedAt'
TS2719  assessment-detail-drawer.spec.tsx → "two different types ... unrelated"
```

The first two are plain missing-property errors: a mock object literal no longer
satisfies the type it is assigned to. The third is a knock-on: once
`generationStatus` is required, a mock diverges from a component prop type and TS
reports the structural mismatch as a duplicate-identity error. All three trace to
one cause.

## What happened (timeline)

```
06-11 / 06-17 11:10   PR #3059 / #3061  set the app spec fixtures   → GREEN
                       (schema did not require the new fields yet)
06-18 07:59 UTC       PR #3076 (shared+api)  added 3 REQUIRED fields → GREEN
                       to packages/shared assessment.schema.ts
                       (diff touched api/ + packages/shared/ — 0 app/ files)
                      ─────────────────────────────────────────────
                       merge cce2da7e  =  new schema × old fixtures  =  RED, unseen
```

- The breaking commit: `3d0bf5ac2` *feat(shared): assessment generation contract + DTO fields*, merged via **PR #3076**. It added `generationStatus`, `generatedAt` (on the assessment) and `regeneratingAt` (on the section answer) as **required** fields.
- The stale fixtures were last set by earlier PRs (#3059 / #3061), green at the time because the schema had no such fields.
- Each PR passed its own CI. The broken state exists **only in the combination** of the two — a textbook semantic merge conflict (no textual conflict, a type-level one).

## Why it occurred — two independent failures, stacked

```
A = "we tested the wrong tree"     PRs built against an OLD main, never the merged tree
B = "we never ran the right job"   consumer CI path-filtered out the package that changed
Either alone → break can slip. Both present → guaranteed-silent.
```

### Failure A — PRs not built against current `main`

PR #3076 was green against a `main` that still had the *old* fixtures it was
about to invalidate? No — it was green because it changed only schema+api and its
own CI never compiled `app`. And #3059 was green against the *old* schema. The
combination `new schema × current fixtures` was **never compiled by any CI run**,
because branch-protection did not require branches to be up to date with `main`,
and there was no merge queue building the post-merge tree.

### Failure B — consumer not gated (the path-filter blind spot)

`packages/shared` is an upstream contract for `app/`. But `app-ci.yml` triggers
only on `app/**`. PR #3076's diff had **zero** app files, so:

- app-ci did **not** run on the PR, and
- app-ci did **not** run on push-to-main (same path-filter on the `push` trigger).

`api-ci` ran only because #3076 happened to also touch `api/` — the api side of
the contract was checked by luck, the app side never was. The break therefore sits
on `main`, invisible, until the next PR that touches `app/**` triggers app-ci.

## Exploration — the fixes, by aspect

### Iteration 1 — Patch the fixtures (necessary, not sufficient)

Add the three missing fields to the three fixtures. Unblocks the immediate red.
But this only treats the symptom; the *next* required shared field re-creates the
exact same silent break.

### Iteration 2 — Consumer gating (fixes B)

Add the upstream dependency to the consumer's path-filter:

```yaml
# app-ci.yml + admin-ci.yml — both pull_request.paths AND push.paths
paths:
  - 'app/**'
  - 'packages/shared/**'
  - 'packages/shared-components/**'
  - '.github/workflows/app-ci.yml'
```

Or centralize: a `packages-ci` job that, on any `packages/**` change, runs
`tsc -b` for every consumer (`app`, `admin`, `api`). With this, PR #3076 goes red.

Limit: a path-filter sees *that* shared changed, not *which other PR it merges
next to*. It catches "shared changed in this PR," not "shared changed in PR-A,
fixture in PR-B." That residual is Failure A.

### Iteration 3 — Build the merged tree (fixes A)

Require branches up to date before merge, or adopt a **GitHub merge queue** that
builds each PR against the real post-merge tree. This is the only mechanism that
reliably catches two-green-PRs-one-red-main, because it compiles
`new schema × current fixtures` before the merge lands.

### Iteration 4 — Dependency-graph test selection (precise B)

A code dependency graph (reverse-deps from the changed symbol) can answer "which
consumers depend on `assessmentSectionAnswerSchema`?" and select exactly those
specs to re-typecheck — even on a 0-app-diff PR. More surgical than re-running all
of app-ci on any shared change. **Conditions to actually catch this bug:**

1. The graph must model **type-level and JSX-prop edges**, not just runtime
   imports — the TS2741 fixture reached the type through a component prop, not a
   direct import.
2. It must survive `z.infer<typeof schema>` and barrel (`index.ts`) re-exports —
   inference and re-export are exactly where naive graphs drop edges.
3. The branch must still be current with `main` (Failure A) — the graph runs on
   the PR tree; if the stale fixtures are not in that tree there is nothing to
   flag.

It is a **selector, not a verifier**: it decides *what* to compile; `tsc` still
produces the error. It does not replace the merge queue.

### Iteration 5 — Schema-shape discipline (shrink blast radius)

A new **required** field on a shared type is a breaking change to every existing
consumer fixture and call-site. Two valid responses:

- Stage additively: `z.string().datetime().nullable().optional()`, then tighten in
  a follow-up once consumers are updated; or
- Keep it required (so the compiler flags every call-site — often what you want)
  **but update all consumers in the same PR**, which #2/#3 then force through CI.

## Comparison

| Aspect | Catches A (merged tree)? | Catches B (unchecked consumer)? | Effort | Replaces `tsc`? |
|---|---|---|---|---|
| Patch fixtures | no | no | trivial | n/a (symptom only) |
| Consumer path-filter / `packages-ci` | no | **yes** | 5-line yaml | no |
| Up-to-date branch / merge queue | **yes** | partial | config | no |
| Dependency-graph selection | no (needs A) | yes, surgical | tooling | no (selector) |
| Schema staged-optional | reduces frequency | reduces frequency | per-change | n/a |

## Decision rules emerging

### Decision: a path-filter must include the change's upstream dependencies, not just its own directory

If `X` consumes `packages/shared` as source, then `X`'s CI trigger must include
`packages/shared/**`. A path-filter scoped to a consumer's own folder silently
assumes that folder has no external contract dependencies — almost never true in a
monorepo with shared packages.

### Decision: "green on the branch" ≠ "green on main"

Two PRs that each pass against an old `main` can produce a broken `main`. The only
authoritative signal is CI on the **post-merge tree**. Require up-to-date branches
or a merge queue for anything that shares a contract surface.

### Decision: every CI gate must be reproducible locally

A gate that fails CI but is absent from the local `verify` path is the failure mode
the harness exists to prevent. When `packages/shared` is in the diff, the local
pre-push / verify step should run consumer `tsc -b`.

### Decision: a dependency graph augments, never replaces, the gate

Use it to make the consumer trigger precise (run only impacted specs), but keep the
merge queue as the correctness guarantee. The graph chooses what to run; it does
not prove the types check.

## Lessons learned

- **Path-filters encode a dependency assumption.** Filtering CI by the changed
  directory assumes that directory is the full blast radius. In a monorepo with
  shared contracts, the blast radius is the dependency closure, not the folder.
- **Semantic merge conflicts are invisible to text-based git and to per-branch
  CI.** They only surface when the merged tree is compiled. Branch-up-to-date or a
  merge queue is the structural fix; nothing cheaper is reliable.
- **Source-level package coupling raises the stakes.** Because `app` compiles
  `packages/shared` as source, a shared type change is felt instantly with no
  versioning buffer — great for catching drift early, but only if the consumer's
  CI actually runs.
- **Required fields are breaking changes.** Treat adding a required field to a
  shared schema like an API break: update consumers in the same change, or stage it
  optional.
- **Defense in depth beats any single gate.** Consumer-trigger (B) and merge queue
  (A) each independently stop this bug; together they stop it twice. Pick the
  cheapest that closes your specific gap first (here: the 5-line path-filter), then
  add the structural guarantee.

## Files of record

- Breaking commit: `3d0bf5ac2` via PR #3076 — `packages/shared/src/dtos/assessment/assessment.schema.ts`
- Stale fixtures: `app/src/components/assessments/vendor-assessments-section/assessment-section-card.spec.tsx`, `app/src/pages/RelationshipProfile/hooks/use-assessment-mutations.spec.ts`, `app/src/pages/RelationshipProfile/tabs/assessments/assessment-detail-drawer.spec.tsx`
- Gate with the blind spot: `.github/workflows/app-ci.yml` (`paths: ['app/**', ...]`)
