---
created: 2026-08-15
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - ui-ux
  - web-platform
  - accessibility
  - performance
  - trend
---

# UI & UX — Emerging Techniques 2026

Running research note on **emerging UI/UX techniques and patterns** — the counterpart to
[[Agentic Engineering — Trends 2026]], but for the interface layer. Bias is towards
*novel or underexplored* mechanisms with a primary source, not listicle trend words.

The through-line of 2026: **capabilities that used to require a JavaScript library are
becoming browser primitives** — and the browser version ships the accessibility semantics
with it. The second line: **agents are becoming a UI-producing client**, which needs its
own interaction grammar.

Existing vault coverage this builds on: [[The comprehensive guide to making your web app feel native (01kn9w7j1qv79yte6nxjnbzg2m)]] ·
[[Every UI-UX Concept Explained in Under 10 Minutes (01kna4wk4axs6p6078mytd9pnr)]] ·
[[UX UI tips: A guide to creating buttons (01kna3aq4ey3vchmq67ra50t5r)]] ·
[[7 Rules for Creating Gorgeous UI (01kn9zv7vjs2fn3r9yksh1xez4)]] · [[MOC - Design Automation]]

---

## 1. Interest Invokers — declarative hover UI with built-in a11y

**What.** A new HTML attribute, `interestfor`, points a `<button>`/`<a>` at the `id` of a
target element. The *browser* decides what "showing interest" means per input modality —
hover for mouse, focus for keyboard, long-press for touch — and fires `interest` /
`loseinterest` events, whose default action shows and hides a popover. Paired with
`popover="hint"` (a popover type that does *not* dismiss unrelated popovers) and CSS anchor
positioning, this is a tooltip / hover-card / preview-popup with no JavaScript at all.

```html
<button interestfor="my-tooltip">Learn more</button>
<div popover="hint" id="my-tooltip">Additional information here</div>
```

```css
button[interestfor="my-tooltip"] { anchor-name: --my-tooltip; }
#my-tooltip {
  position-anchor: --my-tooltip;
  top: anchor(bottom);
  left: anchor(center);
  position-try: flip-block;   /* reposition instead of overflowing */
  margin: unset;
}
```

`interest-delay` (and the longhands `interest-delay-start` / `-end`) tune the show/hide
delay in CSS — the thing every hand-rolled tooltip gets wrong on a link-dense page.

**Why it matters for UX.** Hover UI is where accessibility quietly dies: JS tooltips
routinely miss keyboard users, are unreachable on touch, vanish before they can be read, and
ship the wrong ARIA. Here the browser **implicitly wires `aria-describedby`/`aria-details`
(you must not add them yourself)** and the modality handling is the platform's problem, not
yours. That makes WCAG 1.4.13 (dismissible / hoverable / persistent) the default rather than
an audit finding. It also removes a whole category of `mouseenter`/`mouseleave` state bugs.

**Maturity — the caveat.** Narrow: **Chrome/Edge 142+ only** at time of writing. Google's own
guidance still recommends the `@oddbird/css-anchor-positioning` and `@oddbird/popover-polyfill`
polyfills (feature-detect before loading), though anchor positioning is an Interop 2026 focus
area so that should move fast. Note also the rename: early prototypes used `interesttarget`;
the shipped attribute is **`interestfor`**.

Sources: [Open UI explainer](https://open-ui.org/components/interest-invokers.explainer/) ·
[Google's modern-web-guidance guide](https://github.com/GoogleChrome/modern-web-guidance/blob/main/skills/modern-web-guidance/guides/ui-behaviors/interest-triggered-tooltips.md) ·
[CSS-Tricks first look](https://css-tricks.com/a-first-look-at-the-interest-invoker-api-for-hover-triggered-popovers/) ·
[MDN: Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers)

## 2. `contrast-color()` — self-correcting colour systems

**What.** A CSS function that hands the *browser* responsibility for picking an accessible
foreground colour: `color: contrast-color(var(--surface))` returns black or white — whichever
contrasts more with the given background. Shipped across all three engines during 2026
(Smashing reports Chrome 147 in April 2026, Firefox 146, Safari 26.0; other write-ups cite
Firefox 147 / Safari 26.2 — **check Baseline before relying on a specific floor**).

**Why it matters for UX.** Smashing's framing is the useful one: ~70% of sites still fail
basic WCAG contrast checks, and a decade of linters, design-token tooling and JS colour
libraries didn't move that number — because all of them run *before* the colour is known.
`contrast-color()` runs at render time, so it survives user-generated theme colours, brand
colours injected per tenant, and dark-mode token swaps. This is the enabling primitive for
**"algorithmic theming engines"**: a design system where the accessible pairing is computed,
not enumerated, and a bad brand colour can no longer produce an inaccessible component.

**Limits — read these before evangelising it.** The shipped Level 5 syntax is **binary
black-or-white only**, and it **cannot see font-size or font-weight**, so it does not satisfy
the WCAG large-text carve-outs and is not a replacement for a contrast audit. Ties default to
white. CSS Color Level 6 adds candidate colour lists and explicit target ratios, but is still
a Working Draft.

**Adjacent, and worth not getting wrong:** APCA — the perceptual contrast algorithm that
accounts for weight and spatial frequency — **was pulled from the WCAG 3 draft in mid-2023**
and the current draft says the contrast algorithm is undetermined. WCAG 3 is not expected to
land before ~2030. Tools that market APCA as "the WCAG 3 method" are ahead of the spec; keep
passing WCAG 2 contrast.

Sources: [Smashing: Algorithmic Theming Engines](https://www.smashingmagazine.com/2026/05/building-self-correcting-color-systems-contrast-color/) ·
[Una Kravets: Automated accessible text](https://una.im/contrast-color) ·
[MDN contrast-color()](https://developer.mozilla.org/docs/Web/CSS/color_value/contrast-color) ·
[Adrian Roselli: WCAG3 Contrast as of April 2026](https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html)

## 3. CSS carousels — `::scroll-button()` and `::scroll-marker`

**What.** CSS Overflow Level 5 generates *real interactive controls* as pseudo-elements
inside a scroll container. `::scroll-button(inline-start / inline-end)` produces prev/next
buttons that behave like native `<button>`s (focus, keyboard, disabled state at the ends);
`::scroll-marker` produces one dot per item, grouped by `::scroll-marker-group`, with
`:target-current` styling the active one. Combined with scroll-snap and scroll-driven
animations you get a carousel — arrows, dots, snapping, progress bar, entrance animations —
with **zero JavaScript**.

**Why it matters for UX.** Carousels are the single most reliably-broken component on the
web, and the breakage is almost always in the hand-rolled control layer: focus escaping the
viewport, dots that aren't buttons, arrows with no disabled state, keyboard users trapped in
a horizontally scrolling region. Moving the controls into the browser means the semantics
arrive with them — Chrome's implementation now derives the `::scroll-marker` accessible name
from its `content` value and fixed a bug that announced every marker as "selected".

**Maturity + the honest counterpoint.** Chrome/Edge 150, Opera 136; Safari 26.6 expected
late August 2026; Firefox in development. **Guard everything in `@supports`** so unsupported
browsers degrade to a plain scroll container. And the accessibility win is partial, not
total: CSS-only carousels still **don't announce slide changes to screen readers**, and
Adrian Roselli's longstanding critique of scrolling regions applies unchanged — a horizontal
scroller is not a content strategy, keyboard-only users need an explicit path through it, and
you should test with real users rather than trust that "the browser handles it now."

Sources: [MDN: Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_overflow/CSS_carousels) ·
[Sara Soueidan: Are 'CSS Carousels' accessible?](https://www.sarasoueidan.com/blog/css-carousels-accessibility/) ·
[Adrian Roselli: Horizontal Scrolling Containers Are Not a Content Strategy](https://adrianroselli.com/2025/08/horizontal-scrolling-containers-are-not-a-content-strategy.html) ·
[SitePoint: Scroll-Driven CSS in 2026](https://www.sitepoint.com/scrolldriven-css-in-2026-building-carousels-without-javascript/)

## 4. Instant *and* smooth navigation — view transitions + speculation rules + `rel=expect`

**What.** Three separate features that only pay off when combined, which is why they're
underused individually:

1. `@view-transition { navigation: auto; }` — **cross-document** view transitions, i.e.
   animated page-to-page transitions on a plain MPA with **no JavaScript and no SPA router**.
2. **Speculation Rules** — declaratively tell the browser to prerender likely-next pages in
   an invisible background tab; the click becomes an activation of an already-rendered page.
3. `<link rel="expect" href="#main-content" blocking="render">` — the underexplored one.
   It **blocks the first paint until a named DOM element has parsed**, so the transition
   animates between two *complete* states instead of flashing a half-built page.

```css
@view-transition { navigation: auto; }

@media (prefers-reduced-motion: reduce) {
  @view-transition { navigation: none; }   /* non-negotiable */
}
```

**Why it matters for UX.** This is the current best answer to "make the web app feel native"
(see [[The comprehensive guide to making your web app feel native (01kn9w7j1qv79yte6nxjnbzg2m)]]) —
and it gets there by *deleting* the SPA framework rather than adding to it. Prerendering is
reported as the highest-ROI performance change available in 2026 (60–80% median LCP
improvement on hot navigation paths for ~10 lines of HTML, no build tooling), and the
transition converts the remaining gap into a compositor crossfade. It degrades gracefully:
older browsers just navigate normally.

**Caveats worth writing down**, from Google's own guidance:
- Only block on resources/elements **in the initial viewport** — over-blocking delays the
  transition and makes perceived performance *worse*.
- Render-blocking can delay screen-reader initialisation.
- A 4-second blocking timeout skips the transition entirely.
- Duplicate `view-transition-name` values silently break the transition; **clean up
  dynamically assigned names or you lose bfcache eligibility**.
- Prerendering executes the destination page — audit analytics and side-effectful code.

Sources: [Google modern-web-guidance: consistent cross-document transitions](https://github.com/GoogleChrome/modern-web-guidance/blob/main/skills/modern-web-guidance/guides/ui-behaviors/consistent-cross-document-transitions.md) ·
[MDN View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) ·
[DebugBear: View Transitions without a framework](https://www.debugbear.com/blog/view-transitions-spa-without-framework)

## 5. Agent-declared UI — A2UI + AG-UI

**What.** The interface counterpart to the vault's agentic-engineering material, and the most
genuinely *new* item here.

- **AG-UI** (Agent-User Interaction Protocol, CopilotKit) — an open, event-based protocol
  for the **bi-directional runtime stream** between an agent backend and a frontend: token
  streaming, tool-call progress, state sync, human interrupts. It is the transport, not the UI.
- **A2UI** (Google, early 2026, Apache 2.0) — a declarative spec where the agent **emits JSON
  describing UI surfaces** from a *curated catalogue of pre-approved components* the client
  already implements. Flat component list with id references, designed so an LLM can generate
  it incrementally and the surface can render progressively. Renderers exist for Lit, Angular,
  React and Flutter (GenUI SDK), with SwiftUI and Jetpack Compose emerging. Status: early
  public preview, v0.9.1 shipping, v1.0 RC.

The division of labour that's crystallising: *Agent Spec defines what runs, AG-UI carries the
interaction, A2UI defines what the user touches.*

**Why it matters for UX.** Two reasons. First, **security posture**: "generative UI" done the
obvious way means an LLM emitting executable code into your page. A2UI is a data format
against a fixed component catalogue — the agent can only *request* components you already
shipped, so the blast radius is a bad layout rather than arbitrary code execution. Second, it
gives the emerging agentic interaction patterns a place to live. The patterns that reportedly
survive enterprise user testing are **plan-and-execute** (show the plan before acting),
**confidence signalling**, **progressive delegation** (earn autonomy incrementally), and
**rollback affordances**. The recurring research finding: *surface-level* explanations don't
build trust — the interface has to expose reasoning **at the decision level** and allow
mid-stream intervention. And over-trust is as dangerous as under-trust: an interface that
presents an agent as infallible causes operators to stop applying judgement.

Sources: [Google Developers Blog: Introducing A2UI](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) ·
[google/A2UI on GitHub](https://github.com/google/A2UI) ·
[CopilotKit: AG-UI and A2UI, the differences](https://www.copilotkit.ai/ag-ui-and-a2ui) ·
[Zylos: Agentic UX frontend design patterns](https://zylos.ai/research/2026-05-28-agentic-ux-frontend-design-patterns-ai-agents/)

---

## Also on the radar (thinner evidence, worth a look next round)

- **`sibling-index()` / `sibling-count()`** — an element can finally know its own position in
  CSS. Staggered list animations in one `calc()` instead of a wall of `:nth-child` rules or
  script-injected custom properties; works for 5 items or 5,000. Chrome since March 2025;
  **Firefox 154 (18 Aug 2026) tips it into Baseline Newly Available**. Needs a fallback until
  then. *(This is the cheapest win on the list.)*
- **Customizable `<select>`** (`appearance: base-select`) — style the native dropdown,
  including rich option content, with native anchor positioning and keyboard/a11y intact.
  Chrome 135 stable; Safari TP 238; Firefox Nightly behind a flag.
- **`@scope`** — production-ready scoped styling with *deliberately weak* specificity, so
  scoped rules stay easy to override. Kills a class of BEM/CSS-modules naming ceremony.
- **`prefers-reduced-transparency`** — joins `prefers-reduced-motion`, `prefers-contrast`,
  `forced-colors`, `inverted-colors`. The 2026 accessibility framing worth internalising:
  a single "accessible" design is the *floor*, and adapting to declared user preferences per
  environment is the actual target. Directly relevant to the Liquid-Glass/glassmorphism
  revival — `backdrop-filter` effects need a reduced-transparency branch.
- **Interop 2026** — 20 focus areas, 15 of them new: anchor positioning, advanced `attr()`,
  view transitions (incl. cross-document), style queries, custom highlights, scroll snap,
  `contrast-color()`. Plus an **accessibility-tree consistency investigation** — cross-browser
  a11y-tree parity is finally being treated as a testable interop problem.

## Tools & frameworks encountered

| Tool | What it's for |
|---|---|
| [`GoogleChrome/modern-web-guidance`](https://github.com/GoogleChrome/modern-web-guidance) | **Skill for coding agents** that injects modern-web-platform guidance so the agent stops emitting 2018 patterns. 51 CSS/layout, 20 HTML/DOM, 32 JS/API features, 131 practical guides. Offline semantic search, no API calls. `npx modern-web-guidance@latest install`. **Highest-value item in this note for our setup** — see [[MOC - Design Automation]]. |
| `@oddbird/css-anchor-positioning`, `@oddbird/popover-polyfill` | Polyfills for anchor positioning + popover; feature-detect before loading |
| CopilotKit / AG-UI | Agent↔frontend event streaming protocol; 40+ framework integrations |
| Google A2UI + GenUI SDK | Agent-declared UI as JSON; Lit / Angular / React / Flutter renderers |
| DebugBear | View-transition and Core Web Vitals measurement |

## What to do with this

1. **Install `modern-web-guidance`** into the Claude Code setup — it's the one item that
   changes output quality immediately rather than needing a project to apply it to.
2. **`sibling-index()` after 18 Aug 2026** — cheapest visible polish available.
3. **Speculation rules + `@view-transition`** — highest ROI on any multi-page site;
   test the `prefers-reduced-motion` branch, it's the one people skip.
4. Treat `contrast-color()` as a **theming primitive**, not an audit replacement.
5. Interest invokers and CSS carousels: **prototype now, ship behind `@supports`** —
   both are Chromium-only or near-enough today.

---

## Research log

### 2026-08-15 — first run
**Angles searched:** emerging CSS/UI primitives 2026 · accessibility innovations 2026 ·
Interop 2026 focus areas · interest invokers / `interestfor` · `contrast-color()` ·
CSS carousels (`::scroll-marker`, `::scroll-button`) · cross-document view transitions +
speculation rules + INP · agentic UX / generative UI patterns · AG-UI + A2UI ·
APCA / WCAG 3 status · adaptive preference media queries · `sibling-index()`.

**Cross-reference against existing vault:** no prior note on any of the five findings.
Nearest existing coverage is PWA/native-feel (view transitions and popover are *mentioned*
in [[The comprehensive guide to making your web app feel native (01kn9w7j1qv79yte6nxjnbzg2m)]]
and the "What Makes a WebApp Feel Native" clipping, and speculation rules appear only inside
an SEO-skill clipping) — none of it covers `interestfor`, `contrast-color()`, the carousel
pseudo-elements, `rel=expect`, or agent-declared UI. The vault's existing UI/UX material is
almost entirely *AI-assisted-design tooling* (design skills, 21st.dev, Dribbble, Open Design)
rather than web-platform capability, so this note fills a real gap rather than duplicating.

**Method note:** direct page fetches to `developer.chrome.com`, `web.dev`, `developer.mozilla.org`,
`open-ui.org`, `css-tricks.com`, `una.im`, `sarasoueidan.com` and `zylos.ai` were blocked by
the network egress policy in this environment; `github.com` / `raw.githubusercontent.com` was
reachable, so the two deepest sources (interest invokers, cross-document transitions) are
verbatim from Google's own guidance repo. Everything else is from search-result synthesis —
**version numbers in particular are worth re-verifying against Baseline** before acting.
Where sources disagreed (contrast-color browser versions; whether anchor positioning still
needs a polyfill) both readings are recorded above rather than resolved.

**Suggested angles for next run** (deliberately away from what's now covered):
- Form UX specifically: `field-sizing`, `<selectedcontent>`, Invoker Commands
  (`command`/`commandfor`), the customizable-select migration path.
- **Motion & perception**: scroll-driven animations in production, `@starting-style`,
  `transition-behavior: allow-discrete`, and the reduced-motion story for each.
- **Non-visual / multimodal**: voice-first and conversational UI patterns, the Web Speech
  landscape, screen-reader UX of streaming AI output (an obvious hole in the agentic patterns).
- **Cognitive accessibility** — the least-covered WCAG dimension; plain-language and
  progressive-disclosure research.
- **Measurement**: how teams are actually instrumenting INP and soft-navigation metrics,
  and whether "AI-assisted remediation" tooling holds up under audit.
- **Design systems**: how token pipelines are adapting to runtime-computed colour
  (`contrast-color()`, relative colour syntax, OKLCH) — does the token layer shrink?
- Primary sources to try when egress allows: Chrome for Developers release notes,
  webkit.org blog, Mozilla Hacks, Adrian Roselli, Sara Soueidan, Smashing Magazine.
