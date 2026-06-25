---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-04
tags: [recipe, testing, mutation-testing, stryker, ethira]
project: ethira/api
related:
  - "[[Mutation Testing]]"
  - "[[Mutation Testing — Tandem Hardening]]"
---

# Stryker Recipe — Ethira api/

> Runnable how-to for mutation testing the `/Users/mindator/Ethira/monorepo/main/api/` NestJS codebase. Captures the workarounds discovered during the Tandem hardening case study at [[Mutation Testing — Tandem Hardening]].

## Prerequisites

Stryker is already installed in `api/`:

- Deps: `@stryker-mutator/core`, `@stryker-mutator/jest-runner`, `@stryker-mutator/typescript-checker`
- Scripts: `test:mutation` (`bunx stryker run`), `test:mutation:changed` (`bunx stryker run --since main`)
- Config: `/Users/mindator/Ethira/monorepo/main/api/stryker.config.mjs` — committed, memory caps + inPlace mode

Before any run:

```bash
cd /Users/mindator/Ethira/monorepo/main/api
bun run build:packages   # builds packages/*/dist outputs required by Jest moduleNameMapper
```

## 1 · Scoped run (recommended pattern)

Most useful pattern: a scoped override config extending the committed one. Narrows `mutate` and `testRegex` to the area of interest. Avoids the 16-hour full-suite trap.

```js
// /Users/mindator/Ethira/monorepo/main/api/.stryker-tmp/run-<area>.config.mjs
import base from '../stryker.config.mjs';

export default {
  ...base,
  mutate: [
    'src/application/services/<area>/**/*.ts',
    '!src/**/*.spec.ts',
    '!src/**/*.e2e-spec.ts',
  ],
  jest: {
    projectType: 'custom',
    enableFindRelatedTests: true,
    config: {
      moduleFileExtensions: ['js', 'json', 'ts'],
      rootDir: 'src',
      testRegex: '(application/services/<area>).*\\.spec\\.ts$',
      transform: {
        '^.+\\.(t|j)s$': ['ts-jest', { isolatedModules: true }],
      },
      moduleNameMapper: {
        '^@/(.*)$': '<rootDir>/$1',
        '^src/(.*)$': '<rootDir>/$1',
        '^@ethira/policy-eval$': '<rootDir>/../../packages/policy-eval/dist/index',
        '^@ethira/policy-eval/(.*)$': '<rootDir>/../../packages/policy-eval/dist/$1',
        '^@ethira/ai-endpoint-allowlist$': '<rootDir>/../../packages/ai-endpoint-allowlist/dist/index',
        '^@ethira/ai-endpoint-allowlist/(.*)$': '<rootDir>/../../packages/ai-endpoint-allowlist/dist/$1',
        '^@ethira/vendor-catalog$': '<rootDir>/../../packages/vendor-catalog/dist/index',
        '^@ethira/vendor-catalog/(.*)$': '<rootDir>/../../packages/vendor-catalog/dist/$1',
        '^@ethira-dev/shared$': '<rootDir>/../../packages/shared/dist/index',
        '^@ethira-dev/shared/(.*)$': '<rootDir>/../../packages/shared/dist/$1',
      },
      testEnvironment: 'node',
    },
  },
  reporters: ['html', 'clear-text', 'progress'],
  htmlReporter: {
    fileName: 'reports/mutation/<area>.html',
  },
};
```

Run:

```bash
cd /Users/mindator/Ethira/monorepo/main/api
bunx stryker run .stryker-tmp/run-<area>.config.mjs
open reports/mutation/<area>.html
```

## 2 · Committed config settings — why each exists

`/Users/mindator/Ethira/monorepo/main/api/stryker.config.mjs` contains hard-won workarounds. Do not strip them.

| Setting | Why |
|---|---|
| `mutate` glob with `!src/**/*.spec.ts`, etc. | Mutate src only, exclude tests, modules, migrations, main.ts |
| `testRunner: 'jest'` | Codebase standard |
| `jest.configFile: 'package.json'` | Pull Jest config from package.json "jest" key |
| `jest.enableFindRelatedTests: true` | Per mutant, only run specs that import the mutated file. Big memory saving. |
| `checkers: []` | Pre-existing TS errors in `*.spec.ts` files crash the TypeScript checker dry run. Re-enable when count is zero. |
| `inPlace: true` | **Critical.** Stryker normally copies `api/` to `.stryker-tmp/sandbox-<id>/`. Jest's `moduleNameMapper` uses `<rootDir>/../../packages/*/dist` — relative paths that break after the copy. inPlace mutates source directly and restores from backup on exit. |
| `coverageAnalysis: 'off'` | Safest. `'perTest'` requires changing `testEnvironment` in `package.json` to the Stryker-wrapped one, which would affect normal `bun run test`. Migration path: ship the testEnvironment change first, verify suite stays green, then flip to `'perTest'` for ~5× speedup. |
| `ignorePatterns: ['.claude', '.cursor', ...]` | Stryker copies symlinks as regular files; `.claude/rules → ../.agents/rules` crashes with ENOTSUP. |
| `maxTestRunnerReuse: 20` | Recycle Jest worker every N mutants. Without this a single ts-jest worker grows past 40 GB. |
| `testRunnerNodeArgs: ['--max-old-space-size=2048']` | Hard cap per worker at 2 GB heap. Combined with concurrency: 1 → peak total ≈ 3–4 GB. |
| `timeoutMS: 30000` | Per-mutant timeout. Catches infinite-loop mutants, counted as killed. |
| `concurrency: 1` | Required for inPlace mode. |

## 3 · Pitfalls and workarounds

### 3.1 Babel parse errors on modern TypeScript

Symptom:

```
SyntaxError: 'readonly' type modifier is only permitted on array and tuple literal types.
  rows: readonly (readonly (string | number))[],
                  ^
```

Workaround — exclude the offending file from `mutate`:

```js
mutate: [
  // ...
  '!src/application/services/questionnaire/outstanding-questions-export.helpers.ts',
],
```

### 3.2 Dry run fails — 16 broken specs

`api/package.json` declares `disposable-email-domains` but it is missing from `node_modules`. About 16 spec suites that import `email.utils.ts` fail to load.

Workaround: scope `jest.config.testRegex` in the override config to specs you actually want to run. Or fix the dep:

```bash
cd /Users/mindator/Ethira/monorepo/main && bun install
```

### 3.3 TypeScript checker abort

If `checkers: ['typescript']` is enabled, Stryker runs a project-wide `tsc` dry run before mutating. Pre-existing TS errors in `*.spec.ts` files abort it.

```bash
# Count remaining TS errors
cd /Users/mindator/Ethira/monorepo/main/api
bunx tsc --noEmit -p tsconfig.json 2>&1 | grep -c 'error TS'
# Re-enable checker only when 0.
```

### 3.4 Workspace package resolution after sandbox copy

If `inPlace: false`, Jest cannot resolve `@ethira-dev/shared` etc. inside the sandbox. Keep `inPlace: true`. Do not clean up `.stryker-tmp/sandbox-XXX/` dirs while Stryker is running.

### 3.5 Symlink crash on `.claude/rules`

```
ENOTSUP: operation not supported on socket, copyfile '.../api/.claude/rules' -> ...
```

Already in `ignorePatterns`. Add new symlinks if you introduce them.

### 3.6 Long-run crashes near the end

Stryker writes HTML only after the run completes. Crash at 81 % = per-file data lost. Mitigations:

- Drop `maxTestRunnerReuse` to 10 and `--max-old-space-size` to 1536 for safer long runs.
- Prefer multiple scoped runs over one monolithic run.
- Pipe Stryker output through `tee` to capture aggregate stats: `bunx stryker run .stryker-tmp/run-<area>.config.mjs 2>&1 | tee .stryker-tmp/run-<area>.log`.

## 4 · Reading the report

Open `/Users/mindator/Ethira/monorepo/main/api/reports/mutation/<area>.html`. Each mutant has one of these statuses:

| Status | Meaning |
|---|---|
| **Killed** | At least one test failed. Good. |
| **Survived** | All tests passed despite the mutation. Real gap. |
| **Timeout** | Mutant ran past `timeoutMS`. Counts as killed. |
| **NoCoverage** | No test exercised the mutated region. Only with `'perTest'`. |
| **CompileError** | Babel could not parse the mutant. Stryker bug, not your code. |

Mutation score formula:

```
score = killed / (killed + survived + timeout + noCoverage)
```

Healthy bands:

| Band | Score |
|---|---|
| Excellent | ≥ 80 % |
| Healthy | 70–80 % |
| Needs work | 50–70 % |
| Bad | < 50 % |

The Ethira api/ baseline as of 2026-06-04 is **48 %**.

## 5 · Scoping recipes

### One file (sanity smoke, 30 sec – 5 min)

```bash
cd /Users/mindator/Ethira/monorepo/main/api
bunx stryker run --mutate "src/domain/utils/format-tag-label.util.ts"
```

### One directory (5–30 min)

```bash
bunx stryker run --mutate "src/domain/utils/**/*.ts"
```

### Customer-priority subset (1–3 h)

Use a scoped override config. Lesson learned from Tandem run: 11 281 mutants crashed at 16 h. Halve the scope and split into two batches.

### Only changed files (seconds to minutes)

```bash
cd /Users/mindator/Ethira/monorepo/main/api
bun run test:mutation:changed   # = bunx stryker run --since main
```

The daily-iteration workflow. Suitable for PR-level mutation gates.

## 6 · Background runs

Long runs should not block your terminal:

```bash
cd /Users/mindator/Ethira/monorepo/main/api
bunx stryker run .stryker-tmp/run-<area>.config.mjs \
  > .stryker-tmp/run-<area>.log 2>&1 &
echo $! > .stryker-tmp/run-<area>.pid
```

Check progress:

```bash
tail -1 /Users/mindator/Ethira/monorepo/main/api/.stryker-tmp/run-<area>.log
# Mutation testing 42% (elapsed: ~3h 2m, remaining: ~4h 8m) 3 218/7 654 tested (1 502 survived, 0 timed out)
```

Kill:

```bash
kill "$(cat /Users/mindator/Ethira/monorepo/main/api/.stryker-tmp/run-<area>.pid)"
```

## 7 · Acting on survived mutants

After completion, walk `/Users/mindator/Ethira/monorepo/main/api/reports/mutation/<area>.html`:

1. Open the HTML report.
2. Each survived mutant shows the diff and the line.
3. Open the spec file. Identify which test should have caught this mutation.
4. Add an assertion that fails on the mutant but passes on the original.
5. Re-run scoped Stryker against just that file: `bunx stryker run --mutate <path>`.
6. Loop until the file reaches ≥ 70 % mutation score.

Common mutation patterns and how to kill them:

| Mutation | How to kill |
|---|---|
| `ConditionalExpression` → `false`/`true` | Add a test where the condition is truthy that asserts the gated outcome |
| `EqualityOperator` `===`/`!==` swap | Two tests: one matching expected, one not |
| `ArithmeticOperator` `+`/`-` swap | Specific value assertion, not `.toBeGreaterThan(0)` |
| `StringLiteral` → `""` | Assert exact string, not `.toContain(...)` |
| `BooleanLiteral` swap | Tighten — `.toBe(true)`, not `.toBeTruthy()` |
| `MethodExpression` dropped | Test that the dropped step actually did something — include input that the step would change |

## 8 · CI integration (future)

Once a feature area sustains ≥ 70 %, lock it in by adding a scoped config with `thresholds.break`:

```js
thresholds: { high: 80, low: 70, break: 70 },
```

`break` causes Stryker to exit non-zero when the score drops below the value — a PR-level regression gate. Apply per-area rather than globally until the whole codebase is ready.

## 9 · Run reference

```bash
# Sanity smoke (one small file)
cd /Users/mindator/Ethira/monorepo/main/api
bunx stryker run --mutate "src/domain/utils/format-tag-label.util.ts"

# Scoped run via override config
cd /Users/mindator/Ethira/monorepo/main/api
bunx stryker run .stryker-tmp/run-<area>.config.mjs

# Only changed files (daily dev loop)
cd /Users/mindator/Ethira/monorepo/main/api
bun run test:mutation:changed

# Full package (CI-nightly only, ≥ 10 h, may crash)
cd /Users/mindator/Ethira/monorepo/main/api
bun run test:mutation
```

After a run:

```bash
# Open the HTML report
open /Users/mindator/Ethira/monorepo/main/api/reports/mutation/<area>.html

# Aggregate from log if HTML missing
grep -oE '[0-9]+/[0-9]+ tested|[0-9]+ survived|[0-9]+ timed out' \
  /Users/mindator/Ethira/monorepo/main/api/.stryker-tmp/run-<area>.log | tail -5
```

## 10 · Known baseline (2026-06-04)

| Scope | Mutants | Kill rate | Wall time | Status |
|---|---|---|---|---|
| `src/domain/utils` | 773 | 48.25 % | 26 min | Complete |
| Tandem priority (questionnaire / trust-center / chat) | 9 228 / 11 281 | ~48.2 % | 15 h 49 m | Aborted at 81 % |

The two unrelated codepaths matching at 48 % is the most important finding — see [[Mutation Testing — Tandem Hardening]] for the full case study.
