---
created: 2026-06-04
tags: [case-study, testing, mutation-testing, stryker, ethira, tandem]
project: ethira/api
related:
  - "[[Mutation Testing]]"
  - "[[Stryker Recipe]]"
  - "[[Test Quality Metrics]]"
---

# Case Study: Mutation Testing on the Ethira api/

> Multi-week investigation triggered by the Tandem questionnaire-failure incident (SIGMA-211). Used mutation testing, branch coverage, and assert density as three independent signals to quantify how badly the codebase is under-asserted. Discovered a **48 % baseline mutation kill rate** that held across two unrelated scopes — pointing at a systemic test-quality issue, not a feature-specific one.

## Context

Tandem is one of three priority customers explicitly named by Jasper Mills (head of customer success) as critical for Ethira's funding round in 2026-04. On 2026-05-26, Tandem's Louise Berntsson reported 38+ vendor questionnaire failures with a Friday deadline. The cluster traced back to a Q9 encryption answer path that had been silently broken for over a week — tests had been passing.

This case study documents what we found when we instrumented Tandem-priority code with three independent test-quality signals.

## Signal stack

We measured three signals that complement each other:

| Signal | What it measures | How we collected it |
|---|---|---|
| **Statement / branch / line coverage** | Did any test execute this code? | `bun run test:cov` scoped to Tandem paths |
| **Assert density** | How many assertions per line of spec? | `grep -cE '\bexpect\(' <spec>` ÷ spec line count |
| **Mutation score** | Would a code change actually break a test? | Stryker scoped run |

The three signals stack in increasing strictness:

```
Coverage:      "Did the test touch this line?"
Density:       "When it touched, did it assert anything?"
Mutation:      "When it asserted, did the assert depend on what the line does?"
```

## Exploration

### Iteration 1 — Coverage alone

Initial scoped coverage on 14 Tandem-priority source files yielded:

```
Statements   76.73 %
Branches     65.14 %     ← 35 % of conditional paths untested
Functions    67.43 %     ← 1 in 3 functions never called by tests
Lines        76.74 %
```

This already showed the problem but felt incomplete. 77 % statement coverage looks decent. Most teams would stop here.

### Iteration 2 — Assert density

Counting `expect()` calls per spec line revealed all 13 measured specs sat at **0.055 – 0.099** assert density. Healthy band is 0.10 – 0.20. Every Tandem spec was below the floor.

Worst case: `contractual-relationship.service.spec.ts` — 6 654 spec lines, only 369 asserts → 0.055. The spec was massive fixture setup with sparse assertions.

This refined the picture: tests run the code but don't check what it does.

### Iteration 3 — Mutation testing

Ran Stryker scoped to Tandem files (questionnaire, trust-center, chat-message paths). Generated **11 281 mutants** across the scope. Run took 15 h 49 m and crashed at 81 % completion (workers exhausted memory on the heavy `chat-message.processor.ts` mutants).

Aggregate at crash point: **48.2 % mutation kill rate** across 9 228 mutants tested. Stryker writes its HTML report only at completion, so per-file numbers were lost. But 9 228 mutants is a huge sample — the aggregate is statistically representative.

Earlier baseline run on a completely unrelated scope (`src/domain/utils`, 773 mutants) had landed at **48.25 %**. The two numbers matching across unrelated code is the most important finding: this is the codebase baseline, not a Tandem-specific issue.

## Final ranked picture

Per-file rank by branch coverage ascending — the file most likely to silently break:

```
Rank  Branch %   Stmt %    Density   Bug %    File
─────────────────────────────────────────────────────────────────────────────
 1    15.4       25.8      0 (no spec)  —     received-questionnaire-single-answer-generation.helpers
 2    35.7       41.3      0.091        69 %  answer.repository
 3    53.1       53.3      0.069        73 %  questionnaire-autofill-orchestrator.service
 4    58.3       51.7      0.094        —     trust-portal-received-questionnaire.repository
 5    63.1       67.8      0.071        59 %  chat-message.processor
 6    65.3       95.4 ⚡   0.074        —     trust-portal-agent-answering.service
 7    66.3       71.5      0.069        70 %  questionnaire-assignment-answer.service
 8    68.5       95.2 ⚡   0.063        —     trust-portal-answering-slack-provisioning.service
 9    71.1       89.0      0.099        —     submit-external-questionnaire-url.service
10    71.7       93.0      0.071        77 %  questionnaire-assignment-trigger.service
11    71.7       86.9      0.072        73 %  save-questionnaire-answer.tool
12    83.7       96.4      0.067        80 %  questionnaire-assignment-query.service
13    87.5      100.0      0.084        —     reviewer-digest-dispatch-worker-listeners
14    87.9      100.0      0.060        75 %  questionnaire-assignment-sync.service
```

⚡ marks **hidden gaps**: high statement coverage (≥ 95 %) but low branch coverage (≤ 70 %). Tests execute the lines but never the alternates. This is where mutation testing earns its keep — coverage alone passes these as healthy.

## Decision rules emerging

Three patterns crystallised from this exercise.

### Decision: How to triage a file

```
spec exists?      No  →   WRITE-SPEC (rank 1 above)
branch < 60 %?    Yes →   ADD-TESTS  (ranks 2–5)
spec/src ≥ 1.5?   Yes →   MUTATION-DRIVEN (ranks 6–14)
                          run Stryker, kill survivors with new asserts
```

A 100 %-line-coverage file with sparse asserts is **not** safe. Mutation testing pulls it apart.

### Decision: When to run Stryker

Full-package runs are CI-nightly territory only. Hands-on iteration uses three patterns:

```
1. --since main             daily PR loop, seconds to minutes
2. Scoped subdirectory      area-level audit, 5–30 min
3. Customer-priority subset overnight CI, 1–3 h (max)

Never:
   Whole api/ in one shot   16+ h, crashes near end, no incremental output
```

### Decision: Memory caps are non-negotiable on this codebase

Without `maxTestRunnerReuse` and `--max-old-space-size`, a single ts-jest worker grew to 40 GB during the first Tandem run. The committed `api/stryker.config.mjs` now caps at 2 GB heap and recycles every 20 mutants — peak total ≈ 3–4 GB.

```js
maxTestRunnerReuse: 20,
testRunnerNodeArgs: ['--max-old-space-size=2048'],
concurrency: 1,           // required by inPlace mode
inPlace: true,            // sandbox copy breaks workspace package paths
```

## What this changes

The 48 % kill rate puts hard numbers on something the team felt intuitively: tests are present but light. Specific consequences:

1. **`mutationPriorityFiles` list in `api/stryker.config.mjs` was incomplete.** It had 6 entries (Slack agent + onboarding tools). Updated list should add the 14 Tandem files above plus DORA regulatory files (separate hotspot cluster).

2. **`coverageAnalysis: 'off'` is the safe default for now.** Migration to `'perTest'` (5× faster, 6× less RAM) requires changing `testEnvironment` in `api/package.json` to `'@stryker-mutator/jest-runner/jest-env/node'`. Ship that change separately, watch CI stay green for a day, then flip.

3. **Pre-existing TS errors in `*.spec.ts` block the TypeScript checker.** `checkers: ['typescript']` was disabled. Re-enable only after spec TS errors are cleaned up:
   ```bash
   bunx tsc --noEmit -p tsconfig.json 2>&1 | grep -c 'error TS'
   # currently ~100, target 0
   ```

4. **INC-20 prevention** (Tandem login broken by merge-conflict deletion of routes in `app.module.ts`) is not a unit-test problem. Add an ESLint rule preventing removal of `@Module` import entries without an explicit marker comment.

## Three-week hardening sequence

Anchored to the rank table.

### Week 1 — fill widest gaps (no Stryker needed)

1. **Write** `received-questionnaire-single-answer-generation.helpers.spec.ts` from scratch. 15.4 % branch, no spec, 727 Sentry events.
2. **Thicken** `answer.repository.spec.ts` from 110 → 300+ lines. Add bulk re-trigger, NOT_FOUND state, soft-delete cases.
3. **Thicken** `questionnaire-autofill-orchestrator.spec.ts`. Cover fan-out cancellation, stuck-vendor reproduction (Mailgun/Notion/Proton/Snowflake), confidence-threshold path.
4. **Thicken** `questionnaire-assignment.controller.spec.ts`. DTO validation paths.

### Week 2 — mutation pass on top 5 only

Use scoped Stryker config. ~1 500 mutants, 30–60 min wall time. For each survived mutant, add the assertion that kills it. Target ≥ 70 % per file.

### Week 3 — mutation on ranks 6–14 + INC-20 guard

The ⚡ hidden-gap files (rank 6, 8) deserve attention first. Then ESLint rule + CI smoke test for `/v1/auth/*` route resolution.

## Stryker run mechanics

The skill at `[[Stryker Recipe]]` documents the full setup. Highlights:

- Run requires `bun run build:packages` first (workspace `packages/*/dist` outputs).
- `inPlace: true` is mandatory — Jest's `moduleNameMapper` uses `<rootDir>/../../packages/*/dist`, those relative paths break after Stryker's sandbox copy.
- Babel parse errors on modern TS syntax (`readonly (readonly T)[]`) crash Stryker. Exclude the offending file from `mutate`.
- 16 broken specs (missing `disposable-email-domains` in `node_modules`) crash the full-suite dry run. Scope `testRegex` in the override config to avoid them.

## Final score banner

```
═════════════════════════════════════════════════════════════════
  Mutation kill rate     48.2 %   ← 22 pp below healthy band
  Branch coverage        65.1 %   ← 10 pp below healthy band
  Assert density         0.073    ← 27 % below floor
═════════════════════════════════════════════════════════════════
  Healthy bands:  mutation ≥ 70 % · branch ≥ 75 % · density 0.10–0.20
```

The three signals converge on the same picture: half-tested at best, with the gap dominated by missing assertions, not missing executions.

## Run history

| Run | Scope | Mutants | Kill rate | Wall time | Outcome |
|---|---|---|---|---|---|
| 1 | `src/domain/utils` | 773 | 48.25 % | 26 m | Complete — HTML at `/Users/mindator/Ethira/monorepo/main/api/reports/mutation/mutation.html` |
| 2 | Tandem priority (questionnaire / trust-center / chat-message) | 9 228 / 11 281 | ~48.2 % | 15 h 49 m | Aborted at 81 % — aggregate only |

## Files of record

- `/Users/mindator/Ethira/monorepo/main/api/stryker.config.mjs` — committed config with memory caps
- `/Users/mindator/Ethira/monorepo/main/api/.stryker-tmp/run-tandem.config.mjs` — Tandem scoped override
- `/Users/mindator/Ethira/monorepo/main/api/src/.stryker-tmp/cov-tandem/coverage-summary.json` — coverage data
- `/Users/mindator/Ethira/monorepo/main/api/.stryker-tmp/cov-report.mjs` — per-file extractor script
- `/Users/mindator/Ethira/monorepo/main/api/.stryker-tmp/run-tandem2.log` — full 16 h log of aborted run
- `/Users/mindator/Ethira/monorepo/main/api/reports/mutation/mutation.html` — completed domain/utils report
- `/tmp/claude-501/tandem-final-report.html` — visual HTML summary
