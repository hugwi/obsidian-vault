---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
# Agent-Driven Browser Verification

> How a coding agent should drive a real browser to *verify* a change actually
> works — and why a single "run arbitrary page JS" tool with an
> accessibility-first observe loop beats a wall of fixed micro-tools.

This note compares two architectures for letting an LLM agent verify UI behaviour
in a live browser:

1. **oh-my-pi `browser` tool** — one persistent tab + a JS sandbox with full
   Puppeteer in scope.
2. **MCP browser servers** (Chrome DevTools MCP, Playwright MCP) — ~25-40 fixed
   tools, one action per call.

For *generating and self-healing* the test suite (rather than driving it live),
see the sibling survey [[AI E2E Testing Tooling]].

The lens is **verification testing**: not "does the unit pass" but "does the
feature actually behave correctly when a human-like driver exercises it." Related:
[[Hermetic E2E and Faking Inaccessible Third-Party Sites]].

---

## 1. Why this matters for verification

Verification = run the app, drive the exact reproduction steps, observe behaviour,
assert. Unit tests check code correctness; verification checks *feature*
correctness. An agent doing verification needs three things:

- **State that persists** across steps (a login survives into the next action).
- **A cheap, reliable way to read the page** (find "Submit", not eyeball pixels).
- **Inline assertions** so the verdict is built where the action happens.

The tool architecture decides whether the agent gets these cheaply or fights for
them every step.

---

## 2. The oh-my-pi model — 3 actions, not 30 tools

**Core idea.** One tab, reused. One `run` action that executes an async-function
body with the real driver in scope. A whole multi-step flow runs in a *single*
tool call — no per-step round-trip through the model.

```
┌──────────┐   ┌──────────┐   ┌──────────────────────────────┐
│  open    │──▶│  run     │──▶│  async fn body, in scope:    │
│ (1 tab,  │   │ (JS code)│   │  page, browser, tab,         │
│  reused) │   │          │   │  display, assert, wait       │
└──────────┘   └──────────┘   └──────────────────────────────┘
                    │ tab survives across run calls + subagents
                    ▼
                ┌──────────┐
                │  close   │
                └──────────┘
```

```ts
// ONE run call: login + navigate + assert — no per-step round-trips
await tab.goto('https://app.local/login');
await tab.fill('#email', 'cursor@ethira.dev');
await tab.fill('#password', 'cursor12345');
await tab.click('aria/Sign in');
await tab.waitForUrl('/dashboard');
const obs = await tab.observe();          // structured page state
assert(obs.elements.some(e => e.name === 'Risks'), 'nav missing');
display(await tab.screenshot());          // attach image only if it matters
```

`code` is the body of an async function with `page` (raw Puppeteer), `tab`
(ergonomic helpers), `display()` (accumulate text/images into the result),
`assert`, and `wait` in scope. Return value is JSON-stringified into the tool
result.

---

## 3. The key move — `observe()` over screenshots

**Default to the accessibility tree, screenshot only when visual appearance
matters.** This is the single most important design decision for verification.

```ts
tab.observe() → {
  url, title, viewport, scroll,
  elements: [
    { id: 4, role: "button",  name: "Sign in", states: ["focused"] },
    { id: 7, role: "textbox", name: "Email",   value: "" },
    ...
  ]
}
// then: tab.id(4).click()  — stable id from last observe
```

Under the hood (`tab-worker.ts`) it calls
`page.accessibility.snapshot({ interestingOnly: !includeAll })`, walks the tree,
keeps only interactive nodes (or all with `includeAll`), optionally filters to the
viewport, and assigns **stable element ids** cached to live `ElementHandle`s.
Navigation invalidates ids → the agent re-observes.

**Why it beats screenshots for verification:**

- Structured + actionable — "find the Submit button" is a list lookup, not vision.
- Cheap — no image tokens per step.
- Deterministic — element identity is the a11y role+name, not pixel coordinates.
- A11y-tree reads double as an accessibility smoke check.

---

## 4. Comparison

| Dimension      | oh-my-pi `browser`                            | MCP browser servers (Chrome DevTools / Playwright) |
| -------------- | --------------------------------------------- | -------------------------------------------------- |
| Tool surface   | 1 scripting tool (`run`) = arbitrary JS       | ~25-40 fixed tools, one action per call            |
| Steps per call | Whole flow in one `run`                       | One action per round-trip                          |
| State          | Persistent tab across calls **and subagents** | Snapshot/session churn between steps               |
| Page reading   | `observe()` a11y tree by default              | Often screenshot/snapshot-heavy                    |
| Escape hatch   | Drop to raw `page` for anything               | Limited to exposed tool surface                    |
| Assertions     | `assert` + `display` inline                   | Reconstructed in model context                     |
| Launch/attach  | Headless, CDP attach, spawn app, stealth      | Less control                                       |
| Token cost     | Low (structured returns)                      | Higher (images, many round-trips)                  |

**The two structural wins:** (1) **persistent tab + arbitrary-JS** collapses an
N-step flow into one call; (2) **observe-first** makes page reads cheap and
reliable. Fixed-tool MCP servers can do the same actions but pay a round-trip and
often a screenshot for each one.

---

## 5. What to adopt today

You don't need oh-my-pi to get most of the benefit. Playwright MCP already exposes
`browser_evaluate` / `browser_run_code_unsafe` — run arbitrary page JS in one
call instead of chaining micro-tools. Mimic the pattern:

> **observe → act → assert, in one call, against a persistent context.**

Recipe:
1. Read page state once via an a11y/DOM query (the `observe` step).
2. Act using role+name selectors (`aria/Sign in`, `text/Continue`), not coordinates.
3. Assert inline; only screenshot when *visual* appearance is the thing under test.
4. Re-observe after navigation — never reuse stale element handles.

This keeps verification fast, low-token, and deterministic — the same properties
that make [[Hermetic E2E and Faking Inaccessible Third-Party Sites|hermetic E2E]]
the merge gate.

---

## References

- **Repo:** [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) — AI coding
  agent for the terminal (hash-anchored edits, LSP, Python, browser, subagents).
- **Model-facing prompt:** `packages/coding-agent/src/prompts/tools/browser.md`
  — the instruction block the model reads (3 actions, observe-first rule).
- **Tool docs:** `docs/tools/browser.md` — full input/output schema and
  collaborator map.
- **Implementation:**
  - `packages/coding-agent/src/tools/browser.ts` — tool entry.
  - `packages/coding-agent/src/tools/browser/tab-worker.ts` — implements the `tab`
    helpers; `observe()` at the `page.accessibility.snapshot(...)` call (~line 904)
    and `collectObservationEntries` (~line 250) doing the interactive-node walk +
    stable id caching.
  - `packages/coding-agent/src/tools/browser/tab-supervisor.ts` — global tab
    registry, worker lifecycle.
  - `packages/coding-agent/src/tools/browser/readable.ts` — `tab.extract()`
    Readability extraction.
  - `packages/coding-agent/src/tools/puppeteer/*.txt` — 13 stealth patches
    injected at launch.
- **Comparable tools in this environment:**
  - Playwright MCP `browser_evaluate`, `browser_run_code_unsafe`,
    `browser_snapshot` (a11y snapshot).
  - Chrome DevTools MCP (`mcp__chrome-devtools__*`) — used in this repo's
    verify-before-claiming-a-fix rule.
- **Captured:** 2026-06-15
