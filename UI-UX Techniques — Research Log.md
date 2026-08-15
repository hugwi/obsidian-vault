---
created: 2026-08-15
categories:
  - "[[Resources]]"
domain: engineering
tags: [ui, ux, frontend, accessibility, web-performance, design-systems, research-log]
---

# UI-UX Techniques — Research Log

Running log of emerging UI/UX techniques and patterns, one dated entry per research pass.
Purpose: catch genuinely *new* platform capabilities and interaction patterns early, before
they show up in the trend listicles. Related: [[Inspiration]] ·
[[Agentic Engineering — Trends 2026]] · [[Agentic Engineering]]

**How to use this note.** Each entry lists findings with a one-line "why it matters" and the
tools/frameworks involved. Before the next pass, read the *Covered so far* index at the
bottom — anything already there is a duplicate and should be skipped in favour of the
suggested next angles.

---

## 2026-08-15 — Pass 1 (baseline)

First pass. No prior research log existed in the vault, so everything here is new by
definition; the vault was grepped for each term first (`invoker`, `APCA`, `reading-flow`,
`speculation rules`, `scroll-driven`, `INP`, `anchor positioning`) and none of them appeared
in any existing note. The closest existing material — [[UI Components (01kqz9ms303f9ez2e4dxq2dx3p)]],
[[7 Rules for Creating Gorgeous UI (01kn9zv7vjs2fn3r9yksh1xez4)]],
[[What Makes a WebApp Feel Native? (Insider Secrets) (01kmws0fjds9hrkmmnqj44a29y)]] — is about
visual craft and native-feel, not about the platform primitives below.

### 1. Declarative behaviour without JavaScript: Invoker Commands + Interest Invokers

`<button commandfor="dialog-id" command="show-modal">` wires a button to another element's
behaviour with zero JavaScript. Built-in commands cover dialogs (`show-modal`, `close`),
popovers (`toggle-popover`, `show-popover`, `hide-popover`), and custom commands dispatch a
`CommandEvent` on the target. The companion `interestfor` attribute does the same for
"showing interest" — hover with a mouse, focus with a keyboard — which is the native answer
to hover-triggered tooltips and preview cards, with `:interest-source` available for styling
the trigger. Invoker commands reached Baseline across all major browsers in early 2026.

**Why it matters.** Every hand-rolled tooltip/modal trigger is an accessibility bug waiting
to happen: the JS version routinely misses keyboard activation, focus return, and the
hover-intent delay that keyboard and touch users need. The declarative version gets focus
management, `aria-expanded`, and dismissal semantics from the browser. It also deletes a
meaningful slice of interaction JS, which feeds directly into finding #3.

**Tools:** native HTML/CSS. Polyfill: `invokers` (oddbird). No framework needed.

### 2. `reading-flow` / `reading-order` — closing the visual-vs-tab-order gap

CSS `reading-flow` lets a flex or grid container declare that sequential focus navigation and
screen-reader order should follow the *visual* order rather than source order:
`reading-flow: flex-visual | flex-flow | grid-rows | grid-columns | grid-order | source-order`,
with `reading-order: <integer>` as a per-item manual override.

**Why it matters.** This is the single most common serious a11y defect in modern CSS layouts.
`order` and `grid-area` have let designers rearrange items visually since Grid shipped, while
the tab order silently stayed in DOM order — the standing advice was "don't do that", which
nobody follows. This is the first fix that doesn't require restructuring the DOM. Still
experimental outside Chromium, so treat as progressive enhancement: the layout must remain
usable when the property is ignored.

**Tools:** native CSS. Shipped in Chromium; check support before relying on it.

### 3. Responsiveness budget: `scheduler.yield()`, LoAF, and Speculation Rules

The INP threshold in 2026 is < 200 ms, and the diagnostic story has matured: Long Animation
Frames (LoAF) replaces the old Long Tasks API for attributing *which* script and which handler
caused a slow interaction. Three concrete levers: `scheduler.yield()` to break long handlers
into chunks that let queued input through while keeping continuation priority (unlike the old
`setTimeout(0)` trick, which sends you to the back of the queue); `contain: strict` /
`content-visibility` on independent sections to cut the presentation-delay phase; and the
Speculation Rules API to prerender the next document, which turns a navigation into an
effectively instant interaction. Speculation rules carry an `eagerness` knob
(`conservative` / `moderate` / `eager`) to trade wasted bandwidth against hit rate.

**Why it matters.** INP is the metric that actually correlates with "this app feels janky",
and unlike LCP it is almost entirely caused by your own application code — framework
hydration and event handlers — rather than by network or images. These are the first tools
that let you attribute and fix it rather than guess.

**Tools:** `scheduler.yield()`, LoAF via PerformanceObserver, Speculation Rules API,
Chrome DevTools performance panel, `web-vitals` library, Cloudflare Speculation Rules.

### 4. Perceptual contrast: APCA and the WCAG 3 scoring model

WCAG 3 replaces the binary 4.5:1 ratio with APCA (Advanced Perceptual Contrast Algorithm),
which outputs a lightness contrast value `Lc` on roughly a ±106 scale and accounts for font
size, font weight, and *polarity* (light-on-dark is perceived differently from dark-on-light —
something WCAG 2's symmetric ratio cannot express). WCAG 3 also swaps pass/fail for a graded
0–4 score.

**Why it matters — including the caveat.** APCA is the better model of how people actually
see, and it is worth using as a *design* tool, especially for dark mode where WCAG 2 reliably
passes text that is genuinely hard to read. But WCAG 3 is not expected to reach Recommendation
before 2028–2030, and WCAG 2.1/2.2 AA remains the operative legal benchmark for ADA and EAA
compliance today. The practical position: **ship to 2.2 AA, design with APCA**, and don't let
an APCA pass substitute for a 2.2 audit. Adrian Roselli's April 2026 status write-up is the
sober counterweight to the vendor blogs, several of which oversell APCA as current law.

**Tools:** APCA calculator (`apcacheck.com`), `apca-w3` npm package, Contrast/Polypane,
variable-font Grade axis for adjusting apparent weight without reflowing layout.

### 5. Agentic UX: five patterns that keep recurring

Across independent 2026 write-ups the same five structural patterns appear for agent-driven
interfaces: **planning visibility** (show the plan before executing), **tool-use disclosure**
(name the tool and the arguments), **memory surfacing** (make what the agent remembers
inspectable and editable), **multi-step workflow tracking**, and **recovery routing** (a
defined path when the agent fails, not a dead end). Two findings sharpen this: *progressive
delegation* — autonomy expands as a function of the user's approval history rather than being
demanded at launch — and the usability result that **binary high/low confidence indicators
outperform numerical percentages**, because users have no calibration for "73% confident".

**Why it matters.** This is the same progressive-disclosure discipline as any complex UI
(summary → detail → raw), but the failure mode is specific: the trust deficit from a bad
early AI feature is durable, and users who got burned don't come back. Relevant to
[[Ethira Future Improvements]] and anything in the vault under `theme: human-ux-frontend`.

**Tools:** CopilotKit, assistant-ui, Google A2UI (cross-platform components), MCP for tool
integration; schema validation (Pydantic/Zod) at the LLM→component boundary so a malformed
generation degrades instead of crashing the view.

### Also noted, lower confidence

- **DTCG design tokens hit a stable spec** (2025.10) with Figma, Penpot, Sketch, Framer,
  Supernova and zeroheight implementing it. The framing worth stealing: tokens as a *platform
  contract* between design, code and AI codegen, not a design deliverable. Stack: author in
  Figma Variables / Tokens Studio → DTCG JSON in the repo → Style Dictionary 4 per platform.
- **Generative UI** (interfaces assembled at runtime from pre-approved components) is real but
  the writing is mostly vendor-led. The one durable idea: the designer's job shifts from
  drawing screens to defining the constraint set the generator works within — which makes a
  rigorous design system a *precondition* for generative UI rather than a casualty of it.
- Trend-listicle terms seen repeatedly but with little substance behind them: "Liquid Glass",
  "spatial UX", "Zero UI", "calm interfaces". Filed as vocabulary, not technique.

### Method note / limitation

The research environment's egress proxy blocked direct fetches of primary sources
(MDN, adrianroselli.com, InfoQ), so findings rest on search-result summaries rather than
full-text reads. **Verify the specifics — especially browser-support claims and APCA `Lc`
thresholds — against MDN, Baseline, and caniuse before acting on any of this.**

---

## Covered so far (skip on the next pass)

Invoker Commands · `interestfor` / interest invokers · `reading-flow` / `reading-order` ·
`scheduler.yield()` · LoAF · Speculation Rules API · `content-visibility` / `contain: strict` ·
INP thresholds · APCA / WCAG 3 scoring · agentic-UX pattern set (planning visibility, tool
disclosure, memory surfacing, workflow tracking, recovery routing) · progressive delegation ·
DTCG token spec · generative-UI framing · scroll-driven animations · View Transitions ·
anchor positioning · customizable `<select>` / `appearance: base-select`.

## Angles to try next

The generic queries ("UI/UX trends 2026") returned near-identical listicles across eight
domains and produced almost nothing usable. Next pass should skip them entirely and go at it
sideways:

1. **Primary sources over blogs** — Chrome/WebKit/Mozilla release notes, `web-features` /
   Baseline changelog, TPAC and CSS WG minutes, Interop 2026 scorecard.
2. **Conference talks**, where the unpolished ideas surface first — Smashing Conf, CSS Day,
   Config, An Event Apart successors, ASE 2026 Harness4GenUI workshop.
3. **Named practitioners rather than topics** — Adrian Roselli, Sara Soueidan, Bramus Van
   Damme, Una Kravets, Jhey Tompkins, Josh Comeau, Vitaly Friedman.
4. **Under-searched niches**: local-first / optimistic UI and conflict-resolution UX (CRDTs
   surfaced to the user), offline-first state, motion-sensitivity and
   `prefers-reduced-motion` beyond the on/off switch, cognitive-accessibility (COGA) task
   force output, form UX and the new `<selectedcontent>`, Interop 2026 focus areas.
5. **Non-web surfaces** — visionOS/spatial, watch and glanceable UI, terminal/TUI design,
   voice-first — where interaction constraints force genuinely different patterns.
6. **Empirical over editorial** — HTTP Archive Web Almanac, Chrome UX Report data, Nielsen
   Norman Group study write-ups, published usability-test results.

## Sources — 2026-08-15

- [Invoker Commands API — MDN](https://developer.mozilla.org/en-US/docs/Web/API/Invoker_Commands_API)
- [HTML Invoker Commands Achieve Baseline Support — InfoQ](https://www.infoq.com/news/2026/01/html-invoker-commands/)
- [A First Look at the Interest Invoker API — CSS-Tricks](https://css-tricks.com/a-first-look-at-the-interest-invoker-api-for-hover-triggered-popovers/)
- [`:interest-source` — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/:interest-source)
- [`reading-flow` — MDN](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/reading-flow)
- [Use CSS reading-flow for logical sequential focus navigation — Chrome for Developers](https://developer.chrome.com/blog/reading-flow)
- [Solving the CSS layout and source order disconnect — Chrome for Developers](https://developer.chrome.com/blog/reading-order)
- [How to Fix INP in 2026 — modpagespeed](https://modpagespeed.com/core-web-vitals/inp/)
- [Core Web Vitals 2026: INP, LCP & CLS Optimization — Digital Applied](https://www.digitalapplied.com/blog/core-web-vitals-2026-inp-lcp-cls-optimization-guide)
- [Does the Speculation Rules API boost web speed? — LogRocket](https://blog.logrocket.com/speculation-rules-api-web-speed-test/)
- [WCAG3 Contrast as of April 2026 — Adrian Roselli](https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html)
- [WCAG 3.0 Explained: Tiers, APCA & What's Changing — accessiBe](https://accessibe.com/blog/knowledgebase/wcag-3-point-0)
- [The APCA Mirage: Why Premature WCAG 3 Adoption Creates Legal Risk — accessibility.chat](https://www.accessibility.chat/articles/the-apca-mirage-why-premature-wcag-3-adoption-creates-legal-risk)
- [Agentic UX: Frontend Design Patterns for AI Agents in 2026 — Zylos Research](https://zylos.ai/research/2026-05-28-agentic-ux-frontend-design-patterns-ai-agents/)
- [Designing for AI Agents: 10 UX Patterns (2026) — Mantlr](https://mantlr.com/blog/designing-for-ai-agents-ux-patterns-2026)
- [UI/UX & Human-AI Interaction — Agentic Design](https://agentic-design.ai/patterns/ui-ux-patterns)
- [Design Tokens specification reaches first stable version — W3C DTCG](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/)
- [The design tokens spec (DTCG) explained — zeroheight](https://zeroheight.com/learn/the-design-tokens-spec-dtcg-explained/)
- [The Complete Guide to Generative UI Frameworks in 2026 — Medium](https://medium.com/@akshaychame2/the-complete-guide-to-generative-ui-frameworks-in-2026-fde71c4fa8cc)
- [CSS Wrapped 2025 — Chrome Demos](https://chrome.dev/css-wrapped-2025/)
- [2026 CSS Features You Must Know — Riad Kilani](https://blog.riadkilani.com/2026-css-features-you-must-know/)
