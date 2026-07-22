---
categories:
  - "[[Resources]]"
domain: engineering
title: AI E2E Testing — Landscape and Build-vs-Buy
category: note
created: 2026-07-03
tags:
  - testing
  - e2e
  - agent-tools
  - build-vs-buy
---

# AI E2E Testing — Landscape and Build-vs-Buy

> Synthesis of 21 vault notes on AI-driven end-to-end testing, aimed at the
> decision: **build my own vs adopt an open-source alternative.** Two questions
> decide everything — **how the agent drives the browser** (a cost story) and
> **who owns the test suite over time** (the build-vs-buy story).

Companion to the trilogy: [[Agent-Driven Browser Verification]] (Layer 1 — driving),
[[AI E2E Testing Tooling]] (Layer 2 — the tool survey), and
[[Hermetic E2E and Faking Inaccessible Third-Party Sites]] (the merge-gate doctrine).

---

## 1. The mental model — separate the two layers first

Every tool below lives in one (or both) of these. Conflating them is why "which E2E
tool" feels muddy — they don't compete on the same axis.

- **Layer 1 · Execution — driving the browser.** How the agent perceives the page
  (vision / DOM / accessibility tree) and what protocol carries the clicks (CDP,
  Playwright/Puppeteer, an extension, or OS screen control). *This is where cost and
  reliability are won or lost.*
- **Layer 2 · Authoring — generating & maintaining the suite.** Who writes the tests
  and keeps them alive — an LLM authoring at runtime (self-healing, non-deterministic),
  an LLM emitting static Playwright you then own, or capture-replay from real traffic.

---

## 2. Layer 1 — the decisive number: perception cost hierarchy

From Reflex.dev's benchmark: same Claude Sonnet, same admin task, same data — **only
the interface varies.** This should drive your architecture more than any model choice.

| Perception | Token cost | Notes |
|---|---|---|
| **Structured API / tool-calls** | ~9–12k / task | 8 calls, deterministic (±27 tokens) |
| **A11y-tree snapshot + refs** | ~200–400 / page | agent-browser; re-snapshot after nav |
| Full-DOM serialization | ~3–5k / page | chrome-devtools-mcp |
| **Screenshots / vision** | **~550k / task** | 53 ± 13 steps, ~17 min |

**The 45× headline:** vision drove the task in **53 steps / ~17 min / 550k input tokens**;
the API path did it in **8 steps / ~20s / 12k tokens** (Haiku: 7.7s / 9.5k — and Haiku
*couldn't complete the vision path at all*). Vision also silently missed 3 of 4
below-the-fold items (no signal to scroll).

> **"Better models narrow cost per step. They will not narrow the step count, because
> the step count is set by the interface."**

---

## 3. Layer 1 — driver comparison

Reliability lesson: **CDP beats extensions** (CDP lives outside the browser process,
survives idle/restart; extensions drop silently overnight). Prefer accessibility-tree
over full DOM when you must read the page.

| Tool | Protocol / browser | Perception | Token cost | Notes |
|---|---|---|---|---|
| **chrome-devtools-mcp** (Google, OSS) | MCP over **CDP**, Chromium | Full DOM into context | ~3–5k/pg | Deep DevTools (perf, Lighthouse). Node ≥22.12. Drive with your Claude sub → no extra token bill. |
| **Playwright MCP** (MS, OSS) | MCP over Playwright | Snapshot / can eval JS | med | `browser_evaluate` / `run_code_unsafe` → mimic omp's one-call flow. Parallelism needs per-worker profiles (issue #893). |
| **agent-browser** (Vercel, OSS) | CLI, native **CDP** | **A11y snapshot + element refs** | ~200–400/pg | ~90% fewer tokens. Auth vault (LLM never sees passwords), sessions, video, visual diff. Ships a CC skill. |
| **oh-my-pi `browser`** (can1357, MIT) | **Puppeteer / CDP** | a11y-tree observe | low | Stealth-first; **CDP-attaches to Electron apps**. See §5. |
| **Steel Browser** (Apache-2.0) | Puppeteer + CDP; also PW/Selenium | agnostic (plumbing) | n/a | Batteries-included **sandbox**: sessions, proxy rotation, stealth, fingerprints. Self-host or cloud. BYO agent brain. |
| **browser-use** (MIT) | Own Chromium; real Chrome profiles | Vision + indexed elements | high | The tool measured in the 45× study. Chrome memory-hungry; parallelism hard → they push Cloud. |
| **midscene.js** (MIT) | PW/Puppeteer or Bridge (your Chrome) | **Pure vision** (DOM removed for actions) | high* | Only true $0 path via **local VLMs** (Qwen/UI-TARS/Gemini). Works on canvas & native. |
| **computer-use** (CC built-in) | OS screen control (macOS a11y) | Pure vision + OS input | highest | Fallback tier. macOS + interactive only (**not `-p`**). Browsers view-only. |
| **agent-stuff skill** (mitsuhiko) | CDP on `:9222` | DOM via `eval.js` | DIY | Proof of how little a competent driver needs: a few Node scripts around JS-eval + screenshot + picker. |

\* vision drops to $0 only if you self-host the model — pay GPU instead of API.

**Claude Code's own tool-precedence ladder codifies the hierarchy:** MCP > Bash >
Chrome (CDP) > computer-use/vision. Vision is reserved for surfaces you don't control.

**The Chromium single-instance trap** (from the "When Claude Code's Browser Plugin
Wasn't Enough" war story): launching N profiles each with its own
`--remote-debugging-port` **does not work** — Chromium is single-instance, later
launches just IPC the parent and ignore the new port. No clean CDP tab→profile mapping.
Plan around contexts on one port, not port-per-profile.

---

## 4. Layer 2 — authoring comparison

NL runners win on resilience & readability; lose on speed, cost, determinism. Reserve
them for high-value complex flows; freeze to plain Playwright for the regression gate.

| Approach | Drives via | Model | Validation | Self-heal | Deterministic |
|---|---|---|---|---|---|
| devassure tutorial | Direct Playwright + tool-use API | Sonnet 4.6 | LLM-as-judge | yes | no |
| arielb135 demo | Playwright MCP | **Haiku** | LLM-judge or re-read URL | yes | no |
| firstloop test-runner | Playwright MCP + **Test-State MCP** | default / Haiku 3.5 | LLM-judge + step tracking | yes | no |
| Stagehand | Playwright (SDK primitives) | OpenAI/Anthropic/local | code assertions | yes | partial |
| Octomind MCP | cloud-managed Playwright | bundled | managed | yes | SaaS |
| keploy | **eBPF proxy** (no browser) | none | replay recorded mocks | n/a | yes |
| codegen skill / "pro-tip" | emits static Playwright | any | page assertions | no | yes |

**The field is skeptical of AI self-healing** (Reddit r/QualityAssurance): practitioners
spent months on it, "the AI guesses wrong half the time," Testim/Functionize "expensive,
didn't save time." Consensus fix instead: **data-testid selectors, explicit waits,
PR-gate + auto-rerun ×2.** The one endorsed AI pattern is **an agentic fallback wrapping
a deterministic script** — script first, AI only on failure. Also: self-healing can
*mask a real regression* (the app changed, not the test).

---

## 5. oh-my-pi's approach to driving E2E (the one to study)

Why it's genuinely different: instead of ~30 fixed MCP tools (one action per
round-trip), omp exposes **one `run` tool** that executes a whole async JS body with the
real driver in scope. A full multi-step flow — login, navigate, wait, observe, assert —
runs in a **single tool call**, and the tab persists across calls *and subagents*.

```
open (1 tab, reused)  →  run — JS: observe() · act · assert · display()  →  close
```

- **observe() over screenshots** — default to the **accessibility tree**, screenshot
  only when appearance matters. `page.accessibility.snapshot()` → interactive nodes with
  **stable ids** cached to live handles; act via `tab.id(4).click()`. Structured, cheap,
  deterministic — and doubles as an a11y smoke check. Navigation invalidates ids →
  re-observe.
- **Puppeteer / CDP, stealth-first** — not Playwright. Stealth on by default so real
  production sites see a normal user. The same API **CDP-attaches to any Electron app** —
  "point it at Slack and it reads your DMs the way it reads the web." 13 stealth patches
  injected at launch.

**You don't need omp to steal the pattern.** Playwright MCP's `browser_evaluate` /
`browser_run_code_unsafe` already run arbitrary page JS in one call. Mimic it:
**observe → act → assert, one call, persistent context**; select by role+name
(`aria/Sign in`), never coordinates; re-observe after nav. This is exactly the recipe in
[[Agent-Driven Browser Verification]].

---

## 6. The landscape — every source in one line

### Natural-language / LLM test runners
- **How to Build an E2E Web Testing Agent with Claude** (Divya Manohar, devassure.io) —
  from-scratch Python agent: YAML spec → headless Chromium → Claude tool-use (7 tools)
  drives & judges. Clearest statement of **intent vs mechanism**. Direct Playwright, not
  MCP. Sonnet 4.6, ~$0.10–0.30 / 12-test run.
- **Automating e2e manual labor with Claude Code** (Ariel Beck; repo
  arielb135/claude-code-e2e-demo) — NL tests as Claude Code commands, no test code.
  Playwright MCP, all-Haiku, dual validation. Parallelism via per-worker profiles.
  **Pro-tip everyone echoes:** for non-complex flows, let Claude run it once then emit
  the Playwright script — author with AI, run deterministically. Secure creds via a
  login subagent + Playwright MCP secret injection (LLM never sees passwords).
- **firstloophq/claude-code-test-runner** — most engineered: packaged Bun CLI on the
  Claude Code SDK, adds a custom **Test-State MCP** (`get_test_plan` / `update_test_step`)
  so the agent tracks plan progress and reports back. CTRF + Markdown reports, Playwright
  traces, Docker/GHA. Positions **between** automated E2E and manual sanity. maxTurns 30.
- **E2e Test Framework** (Skills Directory) — the odd one out: **codegen, not a runtime
  runner.** Generates conventional Playwright/Cypress/Selenium scripts you own and run.

### Adjacent — capture-replay & evals (no browser)
- **keploy** (CNCF) — record real traffic via **eBPF proxy** (API + DB/Redis/Kafka) →
  integration tests + mocks; replay with real deps off. Code-less, language-agnostic. The
  traffic-capture analog to hermetic E2E. Separate `ut-gen` (LLM unit-test gen, Meta paper).
- **deepeval** (confident-ai, Apache-2.0) — "Pytest for LLM apps." G-Eval/DAG judges,
  agentic + RAG + MCP metrics, 0–1 scores with thresholds. Relevant if tests assert on
  *AI output quality*, not just UI state.
- **How we use Claude Agents to automate test coverage** (dev.to) — 30%→~50% coverage in
  a week. Opus plan-mode roadmap by criticality → two specialized agents: a **writer**
  (with IDE diagnostics MCP) and a **reviewer** (deliberately no write tools).
- **Exploring Self-Healing Playwright** (Reddit) — the skeptic's file (see §4).

---

## 7. Build your own vs adopt open source

3-year TCO (from the devassure post — a vendor, read with salt, but shape matches the notes):

| | Build your own (DIY) | Adopt / managed |
|---|---|---|
| Up-front | $22k–$45k to build | ~0 |
| Ongoing | $3k–$4.5k / yr | ~$2,400 / yr managed, or token cost (OSS) |
| You must build | iframes, tabs, upload/download, SSO, OTP, parallelism, reporting | included |
| Gets you | control, data residency, proprietary-flow fit | speed to value, someone's edge cases |

**Build your own when:** strict data residency (pages/creds can't leave your infra —
relevant to Ethira tenant isolation); deeply proprietary workflows; you have platform-eng
capacity and E2E is strategic; you want the observe-first pattern as a first-class primitive.

**Adopt OSS when:** you want a $0-extra path today (drive chrome-devtools-mcp / Playwright
MCP with the Claude sub you already pay for); self-healing SDK inside an existing suite →
**Stagehand** (23k★, most mature drop-in); infra solved → **Steel Browser** under a thin
driver; hands-off managed → **Octomind** (paid SaaS).

**The pragmatic middle (what the notes actually recommend):** don't build the *infra* or
the *driver framework* from scratch. Build the **thin orchestration layer** that encodes
your opinion (observe→act→assert, hermetic gate, canary) on top of an existing CDP
driver. A few hundred lines, not $30k — the agent-stuff skill proves how little a
competent CDP driver needs.

---

## 8. If you build — recommended architecture

Synthesis of [[Agent-Driven Browser Verification]] + [[Hermetic E2E and Faking Inaccessible Third-Party Sites]]
with the driver evidence above. Most likely to be cheap, reliable, and CI-safe.

1. **Drive over CDP, not an extension.** Chromium via CDP (chrome-devtools-mcp,
   agent-browser, or a thin Puppeteer script). Survives idle/restart; headless-CI safe.
   Mind the single-instance trap — one port + contexts, not port-per-profile.
2. **Perceive via the accessibility tree; screenshot only for appearance.** observe() →
   interactive nodes with stable refs → act by role+name → re-observe after nav.
   ~200–400 tok/page vs ~550k for vision. This one choice is your cost story.
3. **Collapse a flow into one call.** observe → act → assert inline, single run against a
   persistent context. Playwright MCP's `browser_evaluate` gives this without adopting omp.
4. **NL/LLM authoring for dev; freeze to Playwright for the gate.** Live-LLM tests are
   non-deterministic and bill every CI run. Author & explore with AI; emit deterministic
   Playwright; keep only frozen scripts on the merge path. Cheap model (Haiku) for the runner.
5. **Make the merge gate hermetic — "real pipe, fake ends."** Fake only input source +
   output sink; run the real system between. Beware the hermetic trap: a mocked test can't
   catch the thing it mocked from changing.
6. **Add a nightly real-traffic canary + prod monitoring.** The only mechanisms that catch
   third-party drift. Non-gating (flaky by nature) — on pass refresh the fixture, on fail
   alert loud. Browser for auth, raw fetch for the capture.

---

## Sources
21 notes under `obsidian-vault`, tag agentic-engineering / e2e. Core references:
[[AI E2E Testing Tooling]], [[Agent-Driven Browser Verification]],
[[Hermetic E2E and Faking Inaccessible Third-Party Sites]], oh-my-pi (can1357),
Reflex "45×" benchmark, the arielb135 / firstloop / devassure NL runners.
