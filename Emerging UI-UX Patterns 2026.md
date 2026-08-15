---
created: 2026-08-15
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - ui
  - ux
  - frontend
  - accessibility
  - web-platform
  - design-patterns
---

Running research note on **new UI/UX techniques and patterns** — what the browser
now does natively, what accessibility is gaining, and where agent-driven interfaces
are heading. Companion to [[Inspiration]] (visual reference) and
[[Agentic Engineering — Trends 2026]] (the agent side). Existing vault notes on
UI craft: [[7 Rules for Creating Gorgeous UI (01kn9zv7vjs2fn3r9yksh1xez4)]],
[[UX UI tips: A guide to creating buttons (01kna3aq4ey3vchmq67ra50t5r)]],
[[The comprehensive guide to making your web app feel native (01kn9w7j1qv79yte6nxjnbzg2m)]].

The through-line for 2026: **capability keeps moving down the stack**. Patterns that
needed a JS library in 2023 — tooltips, carousels, page transitions, styled selects —
are becoming declarative HTML/CSS primitives that are accessible and keyboard-correct
*by default*, because the user agent owns the behaviour instead of each app
reimplementing it badly.

---

## 1. Interest Invokers — declarative hovercards and tooltips (`interestfor`)

An element gets `interestfor="popover-id"` and the browser decides what "showing
interest" means per input modality: **hover** with a mouse, a **hotkey** on the
keyboard, **long-press** on touch. No JS, no `mouseenter` timers, no "tooltip is
unreachable by keyboard and invisible on mobile" bug that ships in almost every
hand-rolled implementation.

- Timing is CSS, not JS: `interest-delay` (shorthand for `interest-delay-start` /
  `interest-delay-end`), e.g. `interest-delay: 400ms 200ms` — the show/hide hysteresis
  that hand-rolled tooltips almost always get wrong.
- Styling both ends of the relationship: `:interest-source` matches the trigger while
  it has interest, `:interest-target` matches the popover — accepted by the CSS WG.
- The UA also picks the right a11y semantics for a *plain hint* vs a *rich hovercard*
  (interactive content inside), which is the distinction `aria-describedby` can't express.

**Why it matters:** hover-revealed UI is the single most reliably broken pattern on the
web for keyboard and touch users. This moves the correct multi-modal behaviour into the
platform, so the accessible version is also the least code.

**Status/tools:** Chromium shipped behind/with `interestfor` from ~139; polyfill
[`mfreed7/interestfor`](https://github.com/mfreed7/interestfor) (npm: `interestfor`) for
production use today. Spec: [Open UI explainer](https://open-ui.org/components/interest-invokers.explainer/) ·
[MDN](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers).
Pairs with the **Invoker Commands API** (`command` / `commandfor`) which does the same
job for click-activation — declarative "this button opens/closes that dialog".

---

## 2. `ariaNotify()` — telling a screen reader something directly

A new API to announce text to assistive tech without a live region:
`element.ariaNotify("Draft saved", { priority: "normal" })`. Live regions are notoriously
inconsistent — announcement depends on how the region was created, when it was inserted,
whether the mutation counts, and which screen reader is running. `ariaNotify` removes the
guesswork. It's async (no guarantee of *when*, or that any AT is even present), and infers
language from the nearest ancestor `lang`.

**Why it matters:** the honest fix for status messaging in SPAs — "5 results", "upload
failed", "sorted by date" — where the visual change is obvious and the non-visual one
currently isn't.

**Counterpoint worth keeping** (Adrian Roselli, *The Siren Song of ariaNotify*, CSS-Tricks):
an easy announce-anything API invites papering over bad semantics. If a control's role,
name and state were right, most announcements wouldn't be needed. Treat it as a last
resort for genuinely event-shaped information, not as a narration channel.

**Status/tools:** Edge origin trial + `--enable-blink-features=AriaNotify`; explainer in
[MSEdgeExplainers](https://microsoftedge.github.io/MSEdgeExplainers/Accessibility/AriaNotify/explainer.html),
incubated at [WICG/accessible-notifications](https://github.com/WICG/accessible-notifications).

---

## 3. CSS-only carousels and tabs — `::scroll-marker`, `::scroll-button()`

CSS Overflow Level 5 gives a scroll container browser-generated affordances:
`::scroll-button(left|right|*)` renders real, stateful, auto-disabling scroll buttons
(one press scrolls ~85% of the scroll area), and `::scroll-marker` /
`::scroll-marker-group` generate the dot/tab indicator group — focusable, arrow-key
navigable, with `:target-current` marking the active one. Combined with scroll-snap and
`animation-timeline: scroll()/view()`, a carousel, a tab strip or a scrollspy table of
contents becomes zero-JS: no `scrollLeft` maths, no IntersectionObserver, no
`aria-selected` bookkeeping.

**Why it matters:** carousels are an accessibility graveyard — the markers are the part
everyone gets wrong. UA-generated markers come with roving focus and correct semantics
for free, and the whole thing keeps working with JS disabled or still loading.

**Status:** Chrome/Edge 135+ full support; Safari 19+ (WebKit landed early 2026);
Firefox still partial behind `layout.css.scroll-driven-animations.enabled`. Same family
as **customizable `<select>`** (`appearance: base-select` + `::picker(select)`), which
finally kills the "rebuild a listbox in JS to style it" pattern.

---

## 4. Speculation Rules × cross-document View Transitions

Two features that are ordinary on their own and transformative together. A
`<script type="speculationrules">` block prerenders likely-next documents; cross-document
view transitions (`@view-transition { navigation: auto; }` + `view-transition-name`)
animate between them. Because the destination is *already rendered*, the transition runs
between two live documents and navigation feels instant — the multi-page-app answer to
"why does the SPA feel nicer".

**Why it matters:** it's perceived-performance work with a near-zero cost profile — ten
lines of HTML, no build step, no framework, no client-side router to maintain. Reported
median LCP improvements of 60–80% on hot navigation paths. Notably this makes plain
server-rendered sites competitive with SPAs on *feel*, which weakens the main UX argument
for adopting a client router at all.

**Related metric shift:** INP (Interaction to Next Paint) is the Core Web Vital that
actually correlates with "feels laggy" — long tasks, hydration, heavy event handlers —
and a large share of sites still fail the 200 ms threshold. Budget INP, not just LCP.

**Tools:** Interop 2026 landed cross-document view transitions, popover anchor
positioning and a usable WebGPU baseline across engines. Measure with DebugBear /
CrUX / `web-vitals`.

---

## 5. Agentic UX: AG-UI and A2UI as the interface layer for agents

The interesting frontend question of 2026 isn't "how do I style a chat bubble" but
**how does an agent render UI, and how does the user stay in control**. Two complementary
protocols have emerged:

- **AG-UI** (Agent–User Interaction Protocol, CopilotKit) — the bi-directional event
  stream between any agentic backend and the frontend: token streaming, tool-call state,
  shared mutable state, human-in-the-loop interrupts. Runs natively on Amazon Bedrock
  AgentCore.
- **A2UI** (Agent-to-User Interface, Google, v0.9) — agents declare UI as **structured
  JSON components**, not generated executable code. That distinction is the whole security
  story: a declarative component vocabulary can be validated and sandboxed; model-authored
  JSX cannot. AG-UI carries A2UI payloads and handshakes with A2A.

The UX patterns that go with them are worth stealing regardless of stack:
**progressive delegation** (agent starts with narrow autonomy and earns more — reportedly
much higher adoption than offering full autonomy on day one), plus the four things every
agent surface needs: show what it's doing, explain *why* it chose that action, allow
override at any point, and recover legibly from failure.

**Why it matters:** directly applicable to the Ethira work — see
[[agentic-systems-architecture]] and [[Agentic Engineering — Trends 2026]]. Generative UI
is the point where agent design stops being a prompt problem and becomes an interface
contract.

---

## Cross-cutting: contrast, calm, and the regulatory floor

- **APCA / WCAG 3 contrast — don't get ahead of it.** APCA replaces the 4.5:1 ratio with
  a perceptual `Lc` score (0–100+) that accounts for font size, weight and polarity, and
  it is genuinely better vision science. But WCAG 3.0 is a Working Draft (latest March
  2026) not expected to reach Recommendation before ~2029, and **the APCA method is not
  normative even within that draft**. WCAG 2.1/2.2 AA remains what the EAA, ADA Title II
  and Section 508 actually require. Use APCA to *design*, ship 2.2 AA to *comply*.
- **Calm interfaces as a differentiator.** The "give attention back" turn — fewer
  interruptions, contextual and prioritised notifications, fewer decisions per session —
  moved from manifesto to product positioning this year.
- **And it now has legal teeth:** the Consumer Rights Directive amendments banning dark
  patterns applied from **19 June 2026**, alongside DSA Art. 25 (deception, manipulation,
  impairment of autonomy) and the Digital Fairness Act work. Consent flows, cancellation
  paths, urgency countdowns and preselected upsells are compliance surface now, not just
  taste.

---

## Research log — coverage and next angles

Covered in this pass (2026-08-15): interest invokers / invoker commands · `ariaNotify` ·
CSS scroll markers & buttons, customizable select · speculation rules + cross-document
view transitions, INP · AG-UI / A2UI agentic UX · APCA & WCAG 3 status · calm UI + EU
dark-pattern rules.

Angles deliberately **not** yet searched — use these next to avoid re-retrieving the same
"2026 design trends" listicles:

- Spatial / visionOS-style depth and hover semantics on the open web
- Local-first UX: optimistic UI, conflict surfaces, offline state as a first-class design problem
- Design tokens as a build artefact — DTCG format, token pipelines, theming at scale
- Motion accessibility beyond `prefers-reduced-motion`: `prefers-reduced-transparency`,
  vestibular-safe easing, and the new `@media` user-preference queries
- Typography engineering: variable-font `GRAD` axis, `text-wrap: pretty/balance`, fluid type without media queries
- Form UX research: passkeys and the post-password sign-in flow
- Empirical sources rather than trend posts — NN/g study write-ups, CHI 2026 proceedings,
  the HTTP Archive Web Almanac, browser-vendor developer-signals surveys

*Search-source note:* the generic "UI/UX trends 2026" query space is dominated by
near-identical agency listicles. Higher signal came from spec/vendor sources (Open UI,
MDN, WebKit blog, MSEdgeExplainers, Interop) and from named critics (Adrian Roselli) —
weight those first next time.
