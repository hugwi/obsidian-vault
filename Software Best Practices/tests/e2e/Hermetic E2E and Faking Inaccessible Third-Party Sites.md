# Hermetic E2E and Faking Inaccessible Third-Party Sites

> How to write trustworthy end-to-end tests for a feature whose behaviour depends
> on a third-party website you cannot drive in CI (login walls, captchas, rate
> limits, private/undocumented endpoints, or simply "don't hammer their prod").

This note covers two linked topics:

1. **Hermetic E2E** — what it means and why it's the default for CI gating.
2. **Replicating an inaccessible external** (e.g. `claude.ai`) — the taxonomy of
   strategies, and how to combine them so the test suite doesn't quietly rot when
   the third party changes.

---

## 1. Hermetic E2E

**Definition.** A hermetic test produces the same result regardless of network,
time, machine, or external service state. It has **no live external dependency**.
Everything outside the system-under-test is faked at a boundary you control.

**Why it's the default for the merge gate:**

- **Deterministic** — no flakes from a third party being slow, down, or A/B-testing.
- **Fast** — no network round-trips, no real auth handshakes.
- **Parallel-safe** — no shared remote state two workers can corrupt.
- **Always runnable** — works offline, in a locked-down CI sandbox, on a fork PR.

**The core principle: real pipe, fake ends.**

> Run the *real* system-under-test end to end. Fake only the two ends — the
> *input source* and the *output sink*. Everything between them is production code.

For a browser extension whose job is "detect X on a page, send it to our backend,"
that means: fake the **page** (the input) and the **backend endpoint** (the
output sink), but let the real content script, message-passing, background
worker, buffering, and request-builder all execute unchanged. You assert on the
bytes captured at the sink.

```
   FAKE (you control)            REAL (system under test)
   ┌──────────────┐   input   ┌────────────────────────────┐  output  ┌──────────┐
   │ fixture page  ├──────────►│ detector → relay → worker →  ├─────────►│ captured │
   │ + fake stream │           │ buffer → builder → fetch()   │          │  request │
   └──────────────┘           └────────────────────────────┘          └────┬─────┘
                                                                            │ assert
```

### The hermetic trap

A hermetic test for a third-party-dependent feature has a **fundamental blind
spot**: you faked the third party, so the test validates your code against a
shape **you invented**, not the shape the third party actually emits. If they
change their format, the test stays **green** while production breaks **silently**.

> A mocked test can never catch the thing it mocked from changing.

This is why hermetic E2E is **necessary but not sufficient**. It must be paired
with mechanisms that observe the *real* external (§3, §4) — see §5.

---

## 2. The "can't access the real site" problem

You cannot point a CI test at the real third party when any of these hold:

- **Auth wall** — login requires email codes, SSO, MFA, captcha.
- **Rate limits / ToS** — automated hits risk bans or are disallowed.
- **Private/undocumented endpoints** — internal web APIs with no stability contract.
- **Cost or side-effects** — each call costs money or mutates real state.
- **Flakiness** — their uptime becomes your test's uptime.

So you must **replicate** the relevant slice of the external. The art is
replicating *enough* to exercise your code, *faithfully enough* that the replica
doesn't drift from reality, and *cheaply enough* to run on every PR.

---

## 3. Strategies to replicate an inaccessible external

Ordered from "cheapest, least faithful" to "most faithful, least gating."

### S1 — Network-layer interception + URL spoofing

Intercept at the network boundary so the real server is never contacted, but the
client still *believes* it's talking to the real origin. Critical when behaviour
is keyed on the URL/origin (e.g. a browser content script that only injects on
`https://claude.ai/*`, or CORS/cookie scoping).

- **Browser (Playwright/Puppeteer):** `page.route('https://real-site/**', fulfill
  fixture)` then `page.goto('https://real-site/')`. The URL bar says the real
  origin → origin-gated code activates → but your fixture is served.
- **Node/server:** Mock Service Worker (`msw`), `nock`, or a local stub server.

**Faithfulness:** low-to-medium. You wrote the fixture, so it's a *guess* unless
combined with S2.

### S2 — Recorded / golden fixtures (capture-replay)

Capture the real response **once** from the real external, commit the raw bytes,
and replay them through S1. Replaces hand-written guesses with real samples.

- Tools: Playwright/Puppeteer recording, browser DevTools "save as HAR", `vcr`-style
  cassette libraries, or a one-off capture script (§4).
- **Single source of truth:** one fixture file consumed by *both* unit tests and
  E2E. One place to update when the external changes.
- **Staleness window** = time between captures. Shrink it by auto-refreshing the
  fixture from the canary (§4).

**Faithfulness:** medium-to-high *at capture time*; decays until re-captured.

### S3 — Contract / schema pinning

Pin the *shape* of the exchange to an explicit, checkable schema (zod, JSON
Schema, protobuf). Two distinct contracts to guard:

- **Inbound contract** (third party → you): validate recorded fixtures against the
  schema your parser expects. If a refreshed fixture fails the schema, you learn
  the external changed *and* in what way.
- **Outbound contract** (you → your own backend): validate the request your code
  builds against your backend's accepted schema, ideally a schema **shared**
  between client and server. Catches your-side drift as a red test instead of a
  prod 4xx.

**Faithfulness:** structural only — guards shape, not semantics.

### S4 — Real-traffic canary (non-gating)

A scheduled job (nightly) that *does* hit the real external — the **only**
mechanism that detects third-party drift before users do.

- Runs **outside the merge gate** (it's flaky by nature: network, auth, captcha).
- Authenticates as a real test account *you own*, captures the real response, and
  runs your real parser against it.
- **On pass:** overwrite the recorded fixture (S2) → fixtures self-refresh.
- **On fail:** alert loudly ("the external changed") — never block merges.

**Accessing private/auth-walled externals programmatically:**

- Distinguish the **public documented API** (stable, API-key auth, but often
  *lacks* the exact surface your UI-driven feature depends on) from the **internal
  web API** (what the product's own frontend calls — session-cookie auth,
  undocumented, can change anytime).
- Cleanest capture pattern: let a **headless browser do the login** (handles the
  interactive/SSO/captcha flow), extract the session cookie/token from the
  context, then make a **raw `fetch`** to the internal endpoint with that
  credential. Browser for auth; plain HTTP for the capture.
- Treat credentials as secrets (CI secret store, rotate on expiry). Respect ToS
  and rate limits — own account, low frequency, fail loud on auth expiry.

**Faithfulness:** highest. It *is* the real external.

### S5 — Production monitoring (the final backstop)

Tests run on a schedule; **users run continuously**. The fastest detector of a
third-party change is your own telemetry.

- Alert on **volume anomalies**: "detections of X dropped to ~0 while traffic to
  the external stayed normal" → your detector silently stopped matching.
- Alert on **shape anomalies**: emit telemetry when a runtime input-guard (S6)
  sees an unrecognised field.

**Faithfulness:** catches *unknown unknowns* no test enumerated.

### S6 — Runtime input guards (defense in depth)

Have the production code itself validate inbound third-party data against the
expected schema and emit telemetry on mismatch. Turns a silent break into a
logged signal that feeds S5. Optional, but cheap insurance for high-value,
third-party-dependent paths.

---

## 4. Capture script pattern (S2 + S4)

```ts
// nightly canary: browser logs in, raw fetch captures the real stream, fixture refreshes
const ctx = await chromium.launchPersistentContext(tmpProfile, { /* ... */ })
await loginInteractively(ctx)                       // browser handles SSO/captcha
const { value: session } = (await ctx.cookies())
  .find(c => c.name === 'sessionKey')!
const res = await fetch(REAL_INTERNAL_ENDPOINT, {   // raw HTTP with captured cred
  headers: { Accept: 'text/event-stream', Cookie: `sessionKey=${session}` },
})
const bytes = await readStream(res.body)
assert(parserAccepts(bytes))                        // real parser vs real bytes
if (process.env.REFRESH_FIXTURE) writeFile(FIXTURE_PATH, bytes)  // self-refresh
```

---

## 5. The layering principle

Split every third-party-dependent test strategy into two jobs and make sure both
are covered:

| Job | "Guard MY code" | "Detect THEIR change" |
|-----|-----------------|------------------------|
| Mechanism | Hermetic E2E (S1+S2), contract test (S3), unit tests | Real-traffic canary (S4), prod monitoring (S5), input guard (S6) |
| Gates PRs? | Yes — fast, deterministic | No — flaky/external, alerts only |
| Catches | Your regressions | Third-party format/behaviour drift |
| If missing | Refactors break silently | Third party breaks you silently |

> The hermetic test guards against *your* regressions; the canary + volume alert
> guard against *their* change. Ship both, or you're testing a fossil.

---

## 6. Decision guide

- **Behaviour keyed on origin/URL/cookies?** → S1 URL-spoof interception (not just
  a stub server on localhost — that tests a *different* origin than prod).
- **Don't hand-write the external's payload** → S2 record it once from reality.
- **Shape matters and is validated downstream?** → S3 schema-pin both directions.
- **Feature depends on a third party that can change?** → S4 canary + S5 monitoring
  are mandatory, not optional. A hermetic suite alone gives false confidence.
- **High-value, silent-failure-prone path?** → add S6 runtime guard.

---

## 7. Anti-patterns

- **Hermetic-only confidence.** Treating a green faked E2E as proof the
  third-party integration works. It only proves *your* code didn't regress.
- **Hand-authored fixtures that drift.** Fixtures typed from memory rot fastest —
  nobody remembers they were guesses. Record from reality (S2).
- **Canary in the merge gate.** A real-network test gating PRs makes the gate
  flaky; people start ignoring red. Keep it nightly and loud.
- **Wrong-origin stub.** Serving the fixture on `localhost` when prod behaviour is
  gated on `https://real-site/*` tests a code path that doesn't exist in prod.
  Spoof the real origin (S1).
- **No outbound contract test.** Asserting the third-party parse but never checking
  your own request matches your backend's schema → symmetric silent break.
- **Multiple fixture copies.** Same sample duplicated across unit + E2E → they
  drift apart. One file, both consumers.

---

## Real example (Ethira)

The browser-extension MCP server-discovery send-path depends on `claude.ai`'s
**internal** bootstrap SSE endpoint (`/api/organizations/{org}/mcp/v2/bootstrap`)
— private, session-cookie-authed, not the public Anthropic API. The full layered
strategy (hermetic Playwright E2E with `claude.ai` URL-spoof + recorded SSE
fixture + nightly session-cookie canary + prod detection-volume alert + outbound
envelope contract test) is tracked in the engineering todo
`ethira/robust-mcp-vendor-send-path-testing`. It is the canonical worked example
of every strategy in §3.

---

## Related

- [[../../README]] — vault index
- Pattern source: hermetic testing, capture-replay, consumer-driven contracts
- See also: `Architecture Decisions/Documenting Constraints` (same "guard against
  drift" philosophy applied to internal constraints)
