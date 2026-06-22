---
created: 2026-06-04
tags: [pattern, testing, mutation-testing, quality-metric]
related:
  - "[[Mutation Testing — Tandem Hardening]]"
  - "[[Stryker Recipe]]"
  - "[[Test Quality Metrics]]"
---

# Mutation Testing

> Mutation testing measures whether your tests would actually fail if the code under test changed. It modifies the source ("mutates" it) and re-runs the tests — if no test fails, the mutation **survived** and your test suite has a coverage gap that line coverage cannot detect.

## Why it matters

Line coverage answers "did any test execute this line?" — a test with zero assertions still scores 100 %. Branch coverage answers "did any test execute both arms of this `if`?" — but still doesn't check what was asserted. Mutation testing answers the strictest question: "if I change what this line does, will any test notice?"

```
Line:        "Did the test touch this line?"               — weakest
Branch:      "Did the test touch both branches?"           — moderate
Mutation:    "If I change the semantics, will tests fail?" — strongest
```

A file can have 100 % line coverage and 0 % mutation score. Tests run the code, they just don't check what it does.

## How mutations work

The mutation engine (Stryker, PIT, Mutmut, etc.) walks the source AST and applies small semantic changes:

| Mutation | Example | Survival means |
|---|---|---|
| `ConditionalExpression` | `if (x > 0)` → `if (false)` | No test exercises the truthy branch with a checked outcome |
| `EqualityOperator` | `x === 5` → `x !== 5` | Test asserts existence but not specific value |
| `ArithmeticOperator` | `a + b` → `a - b` | Test uses `.toBeGreaterThan(0)` instead of specific result |
| `StringLiteral` | `'error'` → `''` | Test uses `.toContain('err')` instead of full string match |
| `BooleanLiteral` | `return true` → `return false` | Test uses `.toBeTruthy()` not `.toBe(true)` |
| `MethodExpression` | drops `.filter(...)` | No test covers the case the filter removes |

For each mutation, the engine runs the test suite. Mutations get classified as **Killed** (at least one test failed — good), **Survived** (all tests passed — bad), **Timeout** (counts as killed-by-infinite-loop), or **NoCoverage** (no test even ran on this region).

## Three signals stack together

In practice, line coverage, assert density, and mutation score complement each other:

```
Coverage:       "Did the test touch this line?"
Assert density: "When it touched, did it assert anything?"   = expect()/spec-lines
Mutation score: "When it asserted, did the assert depend on what the line does?"
```

The Ethira api/ case study below shows all three signals diverging significantly — a file with 95 % statement coverage landed at 65 % branch coverage and an estimated < 40 % mutation score because tests ran the happy path and asserted on shape, not behaviour.

## Real-world case study

The full investigation is at [[Mutation Testing — Tandem Hardening]] — a multi-week measurement of the Tandem-priority code paths in `api/src/`. Highlights pulled below.

### The 48 % baseline finding

![[Mutation Testing — Tandem Hardening#Iteration 3 — Mutation testing]]

### The hidden-gap pattern

![[Mutation Testing — Tandem Hardening#Final ranked picture]]

### Triage rules from the exercise

![[Mutation Testing — Tandem Hardening#Decision: How to triage a file]]

### Final scorecard

![[Mutation Testing — Tandem Hardening#Final score banner]]

## When to use mutation testing

```
Daily PR loop:        --since main   →  mutation only files changed vs base
Sprint hardening:     scoped subset  →  one feature area, 30–60 min
Quarterly audit:      area sweep     →  one team's owned modules, 1–3 h
CI nightly:           whole package  →  full surface, ≥ 10 h, may crash
```

Mutation testing is too slow for the test-driven-development inner loop. It is well suited for:

- A focused hardening pass on customer-critical code
- Lifting a freshly-thinned spec to confidence after adding asserts
- Validating that a "well-tested" codebase actually is
- Discovering test-suite smells (shared mocks, ordering dependencies, weak asserts)

## Operational gotchas

The case study documents the specific tax this codebase imposed:

- ts-jest workers leak memory without explicit caps — peak hit 40 GB on first run
- TypeScript checker bails on pre-existing spec-file TS errors
- Babel parser cannot handle modern `readonly (readonly T)[]` syntax
- Workspace `packages/*/dist` paths break after Stryker's sandbox copy
- Stryker writes the HTML report only at completion — crashing at 81 % loses per-file data

The recipe at [[Stryker Recipe]] captures the runnable workaround for each.

## Related patterns

- [[Test Quality Metrics]] — coverage vs density vs mutation, when each lies
- [[Assert First]] — write the assertion before the code; mutation testing makes weak asserts visible
- [[Stryker Recipe]] — the runnable how-to for this codebase
