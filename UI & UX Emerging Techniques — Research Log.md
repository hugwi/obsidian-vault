---
created: 2026-08-15
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - ux-ui
  - frontend
  - accessibility
  - web-platform
  - research-log
---

# UI & UX Emerging Techniques — Research Log

Rolling log of emerging UI/UX techniques, patterns and platform primitives. One section
per research round. Each round records **what was found** and **what was already known**,
so later rounds can skip ground already covered.

Related: [[Inspiration]] · [[Agentic Engineering — Trends 2026]] · [[Agentic Engineering]]

## Covered-topics index (check before adding a new round)

`scroll-state container queries` · `ariaNotify` · `reading-flow` / `reading-order` ·
`popover + invoker commands + anchor positioning` · `customizable select` ·
`A2UI` / `AG-UI` / generative-UI protocols · `progressive disclosure of agent reasoning` ·
`prerender_until_script` · `Interop 2026 focus areas` · `APCA` / WCAG 3 status

---

# Round 1 — 2026-08-15

Angle: shipped/shipping web-platform primitives and agent-era interaction patterns, rather
than the trend-listicle layer ("liquid glass", "spatial UI", "zero UI"), which is
well-covered and low-signal. Five findings below, all new to this vault.

## 1. Scroll-state container queries — sticky/snap state without a scroll listener

`@container scroll-state()` lets CSS ask the browser three questions it previously only
answered to JavaScript: is this `position: sticky` element **currently stuck** to an edge
(`stuck: top`), is this item **snapped** in its scroll-snap container (`snapped: x`), and is
this container **scrollable** in a given direction (`scrollable: down`). Opt in with
`container-type: scroll-state`, then style descendants inside the at-rule.

**Why it matters.** The "add a shadow to the header once it sticks" and "highlight the
snapped card" patterns are near-universal, and until now each one meant an
IntersectionObserver with a sentinel element or a scroll listener — main-thread work,
sentinel hacks, and jank on cheap devices. This moves the state the browser *already knows*
into the compositor-friendly declarative layer. The `scrollable:` query is the sleeper: it
gives you a real answer to "is there more content below?" so scroll affordances (fade edges,
down-chevrons) can finally be correct instead of guessed.

**Status.** Chrome 133+. Not yet Baseline — treat as progressive enhancement, since a
missing shadow degrades harmlessly.

- [MDN — container scroll-state queries](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Conditional_rules/Container_scroll-state_queries)
- [Chrome for Developers — CSS scroll-state()](https://developer.chrome.com/blog/css-scroll-state-queries)
- [utilitybend — Is the sticky thing stuck? Is the snappy item snapped?](https://utilitybend.com/blog/is-the-sticky-thing-stuck-is-the-snappy-item-snapped-a-look-at-state-queries-in-css/)

## 2. `ariaNotify()` — imperative screen-reader announcements

An accessibility API (WICG / Microsoft Edge explainer) that lets you tell a screen reader
what to say directly: `element.ariaNotify("Message sent", { priority: "normal" })`, rather
than mutating a hidden `aria-live` div and hoping the assistive tech notices.

**Why it matters.** Live regions are one of the most consistently mis-implemented parts of
accessible UI. They only fire on *DOM change*, so every codebase ends up with the same
hidden-node hack, and behaviour varies across screen readers. Two limitations disappear
here: announcements can fire at any time (not only after a mutation), and there is no
requirement for a corresponding *visible* region — which is exactly the case for
"copied to clipboard", "3 results filtered", "autosaved". It is a complement to `aria-live`,
not a replacement: where the announcement *should* also be visible, a live region is still
right.

**Status.** Early — Edge shipped it as a developer/origin trial; W3C TAG review is in
progress. Worth wiring behind a capability check now, since the fallback is the live region
you already have.

- [WICG — Accessibility Notification API spec](https://wicg.github.io/aom/notification-api.html)
- [MDN — Element.ariaNotify()](https://developer.mozilla.org/en-US/docs/Web/API/Element/ariaNotify)
- [Make Screen Readers talk with the ARIA Notify API](https://www.oidaisdes.org/blog/aria-notify-first-look/)

## 3. `reading-flow` / `reading-order` — fixing the flex/grid tab-order trap

Two CSS properties that control the order in which children of a flex, grid or block
container are exposed to assistive tech and reached by <kbd>Tab</kbd>.
`reading-flow: flex-visual | flex-flow | grid-rows | grid-columns | grid-order | source-order`
on the container, plus `reading-order: <integer>` to override an individual child.

**Why it matters.** This closes a fifteen-year-old accessibility hole. `order`,
`flex-direction: row-reverse` and grid auto-placement all let visual order diverge from DOM
order, which silently breaks WCAG 2.4.3 (Focus Order) — the tab sequence jumps around the
screen. The standing advice was "never reorder visually", which quietly forbade a large
slice of responsive layout. Now the reorder can be *declared* so focus follows the eye.
Notably this is the rare CSS feature that makes a layout **more** accessible rather than
demanding restraint.

**Status.** Chrome 137+. Chromium-only for now.

- [Chrome for Developers — Use CSS reading-flow for logical sequential focus navigation](https://developer.chrome.com/blog/reading-flow)
- [MDN — reading-flow](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-flow)
- [CSS-Tricks — What we know so far about CSS reading order](https://css-tricks.com/what-we-know-so-far-about-css-reading-order/)

## 4. The declarative interaction stack is now assembled

Individually these shipped over three years and read as small; together they are the first
credible replacement for the headless-UI dependency. Four pieces now interlock:

- **Popover API** (`popover`, `popovertarget`) — top-layer, light-dismiss, focus management.
- **Invoker commands** (`command` / `commandfor`) — a button acts on another element
  declaratively: open a dialog, toggle a popover, close it. No click handler.
- **CSS anchor positioning** (`anchor-name`, `position-anchor`, `position-try`) — tether the
  popover to its trigger, with automatic flipping when it would overflow.
- **Customizable `<select>`** (`appearance: base-select`, `::picker(select)`) — style the
  native dropdown instead of rebuilding it.

The connective detail that makes this more than a list: a popover and its invoker get an
**implicit anchor reference**, so you often don't declare `anchor-name` at all. Same for a
customizable select and its picker.

**Why it matters.** Dropdowns, tooltips, menus and comboboxes are where custom
implementations most often break keyboard and screen-reader support, and they are what most
of a UI-library bundle is actually paying for. Native versions get focus trapping,
top-layer stacking (no more `z-index` wars), Esc handling and the accessibility tree for
free — and `@starting-style` covers the entry animation that used to justify the library on
its own. **Both "Dialogs and popovers" and "CSS anchor positioning" are Interop 2026 focus
areas**, so the remaining cross-engine gaps are actively being closed this year.

- [Interop 2026 focus areas (web-platform-tests)](https://github.com/web-platform-tests/interop/blob/main/2026/README.md)
- [MDN — Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)
- [CSS { In Real Life } — Anchor positioning and the Popover API for a JS-free site menu](https://css-irl.info/anchor-positioning-and-the-popover-api/)
- [Why CSS anchor positioning and the Popover API matter in 2026](https://kvassiliou.com/tech/css-anchor-positioning-popover-api-2026)

## 5. Generative UI is standardising on *constrained* protocols, not generated code

The 2025–26 production wave settled a design question that looked open a year ago: agents
that render UI do **not** emit code. They emit a declarative description that names
components from a client-side **allow-list**.

- **A2UI** (Google, v0.9) — framework-agnostic, streaming JSONL spec for declaring UI
  *intent*; the client renders natively (Flutter, Angular, Lit). Data, not executable code.
- **AG-UI** — event protocol carrying agent activity and shared state to the frontend over
  Server-Sent Events.
- **MCP Apps** — official MCP extension letting a tool return a UI resource that renders
  inline in the host client.
- SDK layer: Vercel AI SDK (`streamUI()`), CopilotKit, assistant-ui, Tambo, Thesys C1 —
  most built on a shadcn/ui-style component registry.

**Why it matters.** The allow-list is the whole point, and it is a *design-system* argument
as much as a security one: constraining the agent to registry components is what keeps a
dynamically-assembled interface consistent with the rest of the product, and keeps the
output reviewable. This is also the practical bridge between a design system and an agent —
the registry becomes the contract.

**Pair it with the trust layer.** NN/g's *State of UX 2026* frames trust, not capability, as
the central AI design problem: adoption is rising while trust falls. The pattern that keeps
recurring is **progressive disclosure of agent reasoning** in three layers — (1) the result
plus a confidence signal, (2) one click to a plain-English account of what the agent did,
(3) the full trace for power users and compliance. Reported to beat both black-box output
and full-transparency reasoning dumps, because most users want *what did it do / how sure is
it / can I verify it* rather than a transcript.

- [awesome-generative-ui (protocol & SDK landscape)](https://github.com/narrowin/awesome-generative-ui)
- [Google Developers Blog — A2UI v0.9](https://developers.googleblog.com/a2ui-v0-9-generative-ui/)
- [CopilotKit — The developer's guide to generative UI in 2026](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026)
- [Progressive disclosure matters: applying 90s UX wisdom to 2026 AI agents](https://aipositive.substack.com/p/progressive-disclosure-matters)
- [Notch — What is Agentic Experience (AX)](https://wearenotch.com/blog/what-is-agentic-experience/)

---

## Also noted (not developed this round)

- **`prerender_until_script`** (Chrome 144, Jan 2026) — a speculation-rules middle ground:
  fetches HTML and begins rendering CSS/images/fonts, but **pauses at the first blocking
  script**, so analytics and other side effects don't fire on a page the user never visits.
  Resolves the main objection to full prerender. Speculation Rules were at ~35% of mobile
  sites in the 2025 Web Almanac.
  [corewebvitals.io](https://www.corewebvitals.io/pagespeed/prerender-until-script-speculation-rule) ·
  [Chrome docs](https://developer.chrome.com/docs/web-platform/prerender-pages)
- **WCAG 3 / APCA — resist the hype.** APCA (perceptual contrast, `Lc` scale accounting for
  font size, weight and polarity) is still a *candidate* method; the WCAG 3 draft says the
  contrast algorithm is undetermined, and WCAG 3 is not expected to reach Recommendation
  before ~2028–2030. **WCAG 2.2 AA remains the operative legal benchmark.** The genuinely
  new idea worth tracking is the shift from binary pass/fail to graded scoring.
  [Adrian Roselli — WCAG3 contrast as of April 2026](https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html)
- **`interactivity: inert`** — inertness from a stylesheet rather than an attribute; useful
  for carousels/paginated content where only the visible page should be reachable.
  Chromium-only, not Baseline.
- **Interop 2026** — 20 focus areas. Beyond those above, the UI-relevant ones are container
  style queries, `contrast-color()`, custom highlights, `CSS shape()`, scroll-driven
  animations, scroll snap, Navigation API, scoped custom element registries and view
  transitions. Investigations include **accessibility testing** (consistent accessibility
  trees across browsers).

## What was already well-covered elsewhere (skipped)

View Transitions and scroll-driven animations as bundle-size wins (~25–45 KB of JS
displaced) are real but already in the vault's orbit; the 2026 trend lists (adaptive
interfaces, liquid glass, spatial/3D, zero UI, motion-as-structure) recycle each other and
carry little actionable detail.

## Angles for next round

1. **Primary sources over listicles** — several high-value domains (web.dev, webkit.org,
   MDN, WebAIM) were blocked by the egress proxy this round; findings above lean on search
   summaries and reachable mirrors. Retry those directly.
2. State of CSS / State of HTML 2026 survey results — pain points, not predictions.
3. Design-system tokens ↔ agent registries: how teams expose a component contract to an LLM.
4. Post-Core-Web-Vitals interaction quality: INP field data, long animation frames (LoAF).
5. Local-first / offline-first UX patterns (sync status, conflict UI) — absent from this vault.
6. Non-Western and non-visual interaction research; voice/multimodal beyond the hype layer.
