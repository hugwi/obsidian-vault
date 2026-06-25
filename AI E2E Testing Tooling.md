---
categories:
  - "[[Resources]]"
domain: engineering
title: AI E2E Testing Tooling
category: note
created: 2026-06-16
tags:
  - agent-tools
  - testing
  - e2e
---

# AI E2E Testing Tooling

> Survey of tools that make end-to-end browser testing *automatic* — AI authors,
> drives, or self-heals the tests. Two classes: **MCP servers** (an agent
> generates/runs/heals spec files) and **libraries** (drop natural-language AI
> steps into an existing Playwright suite).

Companion to [[Agent-Driven Browser Verification]] — that note is about *driving*
a browser one step at a time; this note is about *generating and maintaining the
test suite*. Related doctrine: [[Hermetic E2E and Faking Inaccessible Third-Party Sites]].

---

## The cost model — "code is free, the brain costs"

Most of these are open-source (MIT) so the code installs free. The recurring cost
is the **LLM** unless you run a local model. SaaS backends bill separately.

The cheapest omp-style loop is **not** an AI E2E library at all — it's driving a
browser MCP (`chrome-devtools-mcp` / Playwright MCP) with the agent you already
pay for (Claude Code subscription). No extra token bill. AI E2E *libraries* spin
their **own** LLM calls, which in CI run on every test execution → token cost +
non-determinism.

---

## MCP servers — agent generates / heals spec files

| Tool | Persistent spec files | Self-heal | Backend | URL |
|---|---|---|---|---|
| **Octomind MCP** | Yes (cloud-managed Playwright) | **Yes** (auto-fix on locator break) | SaaS (MCP is OSS) | https://github.com/OctoMind-dev/octomind-mcp |
| Playwright MCP `--codegen typescript` + `saveSession` | Partial — records interaction → `.spec.ts` | No | OSS, local | https://github.com/microsoft/playwright-mcp |
| Midscene MCP | No (live NL driver, visual reports) | Partial (re-plans on selector fail) | OSS, local-capable | https://github.com/web-infra-dev/midscene |

- **Octomind** is the only purpose-built "agent creates + runs + auto-fixes E2E"
  MCP. Best fit if you want a managed self-healing suite. Backend is paid SaaS.
- **Playwright MCP** codegen is a record-from-interaction side-effect, not
  AI-authored test logic. No healing.

---

## Libraries — AI steps inside Playwright

| Lib | Style | Self-heal | Model | Maturity | URL |
|---|---|---|---|---|---|
| **Stagehand** | `act` / `observe` / `extract` NL primitives, TS SDK | Yes (no selectors) | OpenAI / Anthropic, local-capable | **23k★, v3.5.0, active** | https://github.com/browserbase/stagehand |
| **Midscene.js** | NL + vision, Playwright helper | Partial | **local open models** (Qwen / GLM / UI-TARS / Gemini) | 13k★, active | https://github.com/web-infra-dev/midscene |
| **Shortest** | pure English test strings, Claude computer-use | Yes | Anthropic | 5.6k★, young | https://github.com/antiwork/shortest |
| auto-playwright | `auto()` NL step in a PW test | runtime-resolve | OpenAI | 843★, last May 2025 | https://github.com/lucgagan/auto-playwright |
| ZeroStep | `ai()` NL step | runtime | **hosted model, cloud-only** | stale (~3 yr) | https://github.com/zerostep-ai/zerostep |

- **Stagehand** = most mature, cleanest drop-in into an existing Playwright suite,
  BYO Anthropic/OpenAI key, CI-safe, local Chromium (Browserbase cloud optional).
  Its `observe()` / `act()` is the closest library expression of the omp
  verification loop.
- **Midscene** = only library with a true $0 path (run a local vision model; pay
  GPU/CPU instead of API tokens). Vision-only — no DOM access required.
- **Shortest** = pure natural-language test files, no Playwright boilerplate;
  Claude computer-use under the hood.

Not real matches for "automatic test gen": browser-use (agent-internal, no raw JS
exec surface), Browserbase/Stagehand-MCP (NL `act`/`observe`, cloud), Steel /
Hyperbrowser (fixed micro-tools), QA Wolf / mabl / Reflect / TestDriver.ai
(closed SaaS, no MCP).

---

## "Are they free?" — the honest table

| Tool | Code | LLM cost | SaaS fee | Truly $0 path |
|---|---|---|---|---|
| chrome-devtools-mcp | free OSS | uses your Claude Code sub — **no extra** | none | **Yes** |
| Playwright MCP | free OSS | driven by your agent | none | **Yes** |
| Midscene.js | free MIT | $0 with local model, else API | none | **Yes** (local model) |
| Stagehand | free MIT | pay per token | Browserbase optional | No |
| Shortest | free MIT | Anthropic key | none | No |
| auto-playwright | free MIT | OpenAI key | none | No |
| ZeroStep | wrapper OSS | hosted-model token | cloud-only | No |
| Octomind | MCP OSS | bundled | paid platform (free tier unverified) | No |
| QA Wolf / mabl / Reflect / TestDriver | — | — | paid SaaS | No |

---

## Recommendation (for a TS monorepo already on Playwright)

1. **Free + omp-like verification:** drive `chrome-devtools-mcp` with Claude. No
   new bill, persistent tab, a11y snapshot loop. See [[Agent-Driven Browser Verification]].
2. **Self-healing reusable specs, willing to pay tokens:** **Stagehand** as an SDK
   inside existing `e2e/` specs.
3. **Zero API cost, self-hosted:** **Midscene.js** with a local vision model.
4. **Managed, hands-off:** **Octomind** (paid SaaS).

### Caution — clashes with the hermetic merge gate

AI-driven tests are **non-deterministic** and make **live LLM calls in CI** →
flake + cost on every run. The hermetic-E2E doctrine wants the merge gate
deterministic. So: use AI E2E for **authoring / exploratory / self-heal during
dev**, then **freeze to plain deterministic Playwright** for the gate. Never put
live-LLM tests on the merge path. See [[Hermetic E2E and Faking Inaccessible Third-Party Sites]].

---

## References

- Octomind MCP — https://github.com/OctoMind-dev/octomind-mcp · https://octomind.dev
- Microsoft Playwright MCP — https://github.com/microsoft/playwright-mcp
- Midscene.js — https://github.com/web-infra-dev/midscene · https://midscenejs.com
- Stagehand — https://github.com/browserbase/stagehand · https://stagehand.dev
- Shortest — https://github.com/antiwork/shortest
- auto-playwright — https://github.com/lucgagan/auto-playwright
- ZeroStep — https://github.com/zerostep-ai/zerostep
- **Captured:** 2026-06-16 (multi-agent research sweep)
