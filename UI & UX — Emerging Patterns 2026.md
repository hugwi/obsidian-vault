---
created: 2026-08-15
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - ui
  - ux
  - web-platform
  - accessibility
  - performance
  - generative-ui
  - research-log
---

# UI & UX — Emerging Patterns 2026

Running research log on **emerging UI/UX techniques and patterns**, kept the same way as
[[Agentic Engineering — Trends 2026]]: one dated round per research pass, newest at the
top, so the next round can cross-reference what was already found instead of rediscovering
it.

The bias of this log is deliberately away from the annual "design trends" listicle
(*glassmorphism, bento grids, bold typography*) and toward things that are **new
capability rather than new taste** — platform primitives, protocols, standards and
measurement changes that alter what an interface can *do*. Trends age out in a year;
primitives change how you build for a decade.

> Visual inspiration library lives separately in [[Inspiration]] · design-automation
> tooling in [[MOC - Design Automation]].

---

## Round 1 — 2026-08-15

First round of this log. Five findings, spread across interaction, accessibility,
performance and the AI/interface boundary.

### 1. Native CSS carousels — `::scroll-button()` / `::scroll-marker()`

**What it is.** CSS Overflow Level 5 adds pseudo-elements that generate carousel
chrome from the scroll container itself: `::scroll-button()` for prev/next controls,
`::scroll-marker()` for the dot indicators, and `::scroll-marker-group` for the group
that holds them. Combined with scroll snapping and Scroll-Driven Animations Level 1
(scroll progress bars, entrance animations), a full carousel — controls, dots, snap,
active-state tracking — becomes pure CSS with no JavaScript library.

The related `scroll-target-group` property does the same job for *existing* HTML
anchors, which is what makes a CSS-only scrollspy possible: real links get scroll-marker
behaviour and `:target-current` styles the active one.

**Why it matters for UX.** Carousels and scrollspies are among the most consistently
badly-implemented components on the web, precisely because everyone hand-rolls the
state tracking. Moving it into the engine means the active-item state is always correct,
it never desyncs from the scroll position, and it costs no main-thread work — which is
also an INP win on scroll-heavy pages.

**The caveat that makes this worth reading twice.** These were billed as
"accessible by default" — the marker group is exposed as a `tablist` and each marker as
a `tab`, with keyboard arrow navigation for free. Sara Soueidan's teardown argues that
is the *wrong* semantic in most real cases: markers that navigate to content should be
exposed as **links, not tabs**, and the tab semantics introduce their own usability
problems. Accessible names also have to come from CSS `content`, which is an odd place
to put user-facing text. Treat "semantics for free" as "semantics you now have less
control over."

**Status.** Not Baseline. Chrome 135+ and Safari 19+; Firefox still partial/behind flags
as of mid-2026. Wrap in `@supports` and ship a fallback.

**Sources.** [Carousels with CSS — Chrome for Developers](https://developer.chrome.com/blog/carousels-with-css) ·
[Are 'CSS Carousels' accessible? — Sara Soueidan](https://www.sarasoueidan.com/blog/css-carousels-accessibility/) ·
[CSS-only scrollspy with `scroll-marker-group`](https://www.sarasoueidan.com/blog/css-scrollspy/) ·
[MDN `::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Selectors/::scroll-marker) ·
[CSS Carousels — CSS-Tricks](https://css-tricks.com/css-carousels/)

### 2. Interest invokers — `interestfor` and the death of the JS tooltip

**What it is.** A new HTML attribute, `interestfor`, on `<button>` and `<a>` that binds
the element to a popover target. The browser — not your code — decides what "showing
interest" means per input modality: **hover** with a mouse, a **hotkey** on keyboard
focus, **long-press** on touch. Paired CSS properties `interest-show-delay` /
`interest-hide-delay` (default 0.5s) control the timing, and `:interest-source` /
`:interest-target` pseudo-classes let you style both ends of the relationship. It sits
alongside the Invoker Commands API (`command` / `commandfor`) as the "light touch"
sibling of the click-to-activate case, and pairs with `popover="hint"`.

**Why it matters for UX.** Tooltips and hover cards are the classic example of a
component that is trivial to build badly. Hand-rolled versions almost always break on
touch (no hover), break on keyboard (no focus path), fire instantly and flicker (no
delay hysteresis), and expose nothing sane to a screen reader. `interestfor` makes the
*modality-correct* behaviour the default and the broken version the one you'd have to
work for. This is the same structural move as `<dialog>` and the Popover API: taking a
pattern where the accessible implementation was expert-only and making it declarative.

**Status.** Chrome 139+ (experimental/shipping), driven through Open UI. Mozilla has an
open standards-position issue — worth watching before depending on it.

**Sources.** [Interest Invokers explainer — Open UI](https://open-ui.org/components/interest-invokers.explainer/) ·
[MDN: Using interest invokers](https://developer.mozilla.org/en-US/docs/Web/API/Popover_API/Using_interest_invokers) ·
[A First Look at the Interest Invoker API — CSS-Tricks](https://css-tricks.com/a-first-look-at-the-interest-invoker-api-for-hover-triggered-popovers/) ·
[What is `popover=hint`? — Una Kravets](https://una.im/popover-hint/) ·
[Mozilla standards-positions #1181](https://github.com/mozilla/standards-positions/issues/1181)

### 3. Generative UI as *data*, not code — A2UI and AG-UI

**What it is.** Two complementary protocols for the agent↔interface boundary:

- **AG-UI** (Agent–User Interaction Protocol, CopilotKit) standardises the **real-time
  event stream** between an agent backend and a frontend. As of mid-2026 it has
  integrations across LangGraph, CrewAI, Microsoft Agent Framework, Google ADK, AWS
  Strands, Pydantic AI and LlamaIndex, with SDKs in Python, TypeScript, Kotlin, Go,
  Rust, Java and Dart.
- **A2UI** (Agent-to-User Interface, open-sourced by Google, v0.9 as of 2026) specifies
  how an agent **declares** UI: a flat JSON list of components with id references plus a
  data model, which the client maps onto its *own* native widgets (React, Angular,
  Flutter, SwiftUI, web components).

**Why it matters for UX.** The security and consistency argument is the interesting part.
The previous way to render UI from an untrusted remote source was to ship HTML/JS and
sandbox it in an iframe — heavy, and visually foreign to the host app. A2UI treats **UI
as data, not code**: the agent can only reference a client-controlled component catalog,
so there's no arbitrary script execution and no UI-injection surface, *and* the rendered
result is automatically in the host app's design system. The flat-list-with-ids shape
(rather than a nested tree) exists so models can emit and *patch* interfaces
incrementally — which is what makes streaming generative UI render progressively instead
of popping in at the end.

The practical spectrum worth internalising: **static generative UI** (agent picks from a
predefined catalog and fills in data — high control) at one end, fully model-authored
markup at the other. Almost everything shippable today lives at the static end, with
component props constrained by Zod schemas.

**Why it's relevant here specifically.** This is the point where "agentic engineering"
and "UI/UX" stop being separate topics — it connects directly to
[[Agentic Engineering — Trends 2026]]. Gartner-style figures floating around claim 30%
of new applications will use AI-driven adaptive UI by 2026, up from <5%; treat the
number as directional, not evidence.

**Tools/frameworks.** AG-UI · A2UI (`a2ui.org`) · CopilotKit · Vercel AI SDK Elements ·
Zod-schema component catalogs · `createSpecCompiler` for streaming JSON fragments.

**Sources.** [Introducing A2UI — Google Developers Blog](https://developers.googleblog.com/introducing-a2ui-an-open-project-for-agent-driven-interfaces/) ·
[A2UI protocol site](https://a2ui.org/) ·
[Developer's Guide to Generative UI in 2026 — CopilotKit](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026) ·
[Agentic UX: Frontend Design Patterns for AI Agents — Zylos](https://zylos.ai/research/2026-05-28-agentic-ux-frontend-design-patterns-ai-agents/) ·
[AG-UI and A2UI explained — Ken Huang](https://kenhuangus.substack.com/p/ag-ui-and-a2ui-protocols-explained)

### 4. APCA / WCAG 3 — contrast stops being a ratio

**What it is.** WCAG 3.0 replaces the WCAG 2.x `4.5:1` contrast *ratio* with **APCA**
(Accessible Perceptual Contrast Algorithm), which outputs a **lightness contrast value
`Lc`** on a roughly 0 to ±106 scale. Sign carries polarity: positive `Lc` is dark text on
light, negative is light text on dark. Rough landmarks: `Lc 30` absolute floor for any
text, `Lc 45` ≈ the old 3:1 for large text, `Lc 60` ≈ the old 4.5:1 for body text,
`Lc 75` preferred for body text.

**Why it matters for UX.** WCAG 2's ratio treats every colour pair with the same number
as perceptually equivalent, and ignores font size, weight and polarity entirely. That is
why "technically compliant" light-grey-on-white body text still reads badly, and why
dark mode passes the checker while being genuinely harder to read. APCA folds
size/weight/polarity into the score, so the metric finally matches the thing you're
actually trying to protect — legibility, not arithmetic. Practically it means contrast
becomes a **typography decision**, not a colour-picker decision: the same colour pair can
pass at 600 weight and fail at 300.

**The honest status.** WCAG 3.0 is a multi-year Working Draft, still being actively
reworked in 2026, and is not expected to reach Recommendation before roughly 2028–2030.
The scoring is *not* settled — Adrian Roselli's April 2026 status post is the corrective
to the many blog posts presenting APCA as decided. **Do not migrate compliance off
WCAG 2.2 yet.** Use APCA as a design-quality tool alongside it: it is better at telling
you what reads well; WCAG 2.2 is still what tells you what's legally defensible.

**Regulatory context.** The European Accessibility Act became enforceable in June 2025
and is being actively enforced through 2026 across e-commerce, consumer banking, e-books,
ticketing/transport and telecoms. Notably it pulls **chatbots** in scope — text and voice
chat widgets must be keyboard-operable and screen-reader compatible, which is a
requirement a large share of shipped AI chat UI currently fails.

**Sources.** [WCAG3 Contrast as of April 2026 — Adrian Roselli](https://adrianroselli.com/2026/04/wcag3-contrast-as-of-april-2026.html) ·
[WCAG 3.0 Explained: Tiers, APCA & What's Changing — accessiBe](https://accessibe.com/blog/knowledgebase/wcag-3-point-0) ·
[WCAG 3 and APCA — Dan Hollick](https://typefully.com/DanHollick/wcag-3-and-apca-sle13GMW2Brp) ·
[From agentic AI to the EAA: 5 accessibility trends for 2026 — The Drum](https://www.thedrum.com/industry-insight/from-agentic-ai-to-the-eaa-five-accessibility-trends-to-watch-in-2026)

### 5. `prerender_until_script` — the missing middle of speculative loading

**What it is.** Speculation Rules previously offered two blunt options: **prefetch** (grab
the HTML only — cheap, but CSS/JS/images still load on click) and **prerender** (render
the whole page in a hidden tab — instant, but it executes the page's JavaScript, firing
analytics, A/B assignment and any other side effect for a navigation that may never
happen). Chrome 144 (January 2026) adds **`prerender_until_script`**: fetch the HTML,
begin rendering and subresource loading — CSS, fonts, images — then **pause at the first
blocking `<script>`**. You get most of the perceived-instant benefit without the
side-effect problem that makes teams refuse to turn prerender on.

Also changed in January 2026: on mobile, `eager` eagerness now triggers **50ms after a
link enters the viewport** (desktop remains ~10ms of hover), which finally gives touch
devices a sensible speculation trigger — they have no hover to key off.

**Why it matters for UX.** Perceived performance is the largest single lever on
multi-page apps, and the reason speculation was under-adopted was risk, not disbelief.
This is a rare case of a spec change aimed squarely at the *organisational* blocker
rather than the technical one. Worth pairing with the standing INP caution: prerendered
pages look interactive before activation-time JavaScript has run, so deferring
everything to activation can *hurt* INP even while LCP looks perfect.

**Status.** Origin Trial, Chrome 144–150. Unknown keys are ignored by other browsers, so
declare a `prefetch` rule over the same URL set as fallback — Chrome dedupes and applies
the most capable available action.

**Sources.** [Prerender until script origin trial — Chrome for Developers](https://developer.chrome.com/blog/prerender-until-script-origin-trial) ·
[Prerender Until Script: the middle ground — Core Web Vitals](https://www.corewebvitals.io/pagespeed/prerender-until-script-speculation-rule) ·
[Implementing speculation rules for complex sites — Chrome](https://developer.chrome.com/docs/web-platform/implementing-speculation-rules) ·
[MDN: Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API)

---

## Cross-reference against what the vault already held

Checked before writing — none of the five above were already covered:

- Existing UI/UX material is either **timeless craft**
  ([[7 Rules for Creating Gorgeous UI (01kn9zv7vjs2fn3r9yksh1xez4)]],
  [[Every UI-UX Concept Explained in Under 10 Minutes (01kna4wk4axs6p6078mytd9pnr)]])
  or **AI-assisted design tooling** (the Claude design-skills cluster in
  [[MOC - Design Automation]]). Neither touches platform primitives.
- [[The comprehensive guide to making your web app feel native (01kn9w7j1qv79yte6nxjnbzg2m)]]
  and [[What Makes a WebApp Feel Native? (Insider Secrets) (01kmws0fjds9hrkmmnqj44a29y)]]
  are the closest neighbours — same *goal* (perceived quality), but pre-date all of
  these APIs and solve it with JS workarounds. Findings 1, 2 and 5 are largely the
  standards-track replacements for tricks described there.
- The agentic-engineering corpus (221 clippings) covers agents extensively but from the
  backend/harness side. Finding 3 is the first material on the **agent↔UI boundary** —
  it belongs to both bodies of work.

**Discarded as duplicate/low-value.** The 2026 "design trends" listicle genre
(*adaptive interfaces, calm UI, Liquid Glass, spatial interfaces, data storytelling,
motion-led design, multimodal search*) returned near-identical content across
eight or more sources with no primary reporting behind it. Recorded here only so the
next round recognises and skips it rather than re-reading it.

## Method note

WebFetch to external domains is blocked by this environment's egress policy, so the
above is compiled from search-result summaries plus primary-source URLs, not from
full-text reads of each article. Version numbers, `Lc` thresholds and browser-support
claims are reported as the sources stated them and are worth a direct check against the
spec before anything here is used in an implementation decision.

## Search angles for the next round

Angles deliberately *not* covered this round, ordered by expected yield:

1. **View Transitions API** — cross-document transitions and scoped view transitions;
   current Baseline status and what MPA-native transitions do to navigation UX.
2. **CSS `if()`, `@function` and custom functions** — conditional logic in CSS and what
   it removes from design-token build pipelines.
3. **Local-first / sync-engine UX** — optimistic UI, conflict surfacing, offline state
   as a design problem rather than an infrastructure one.
4. **Interop 2026 focus areas** — the highest-signal single list of what actually lands
   cross-browser this year; a good de-duplicator against hype.
5. **Anchor positioning + `popover=hint` in production** — a year on from shipping, what
   broke.
6. **The chatbot-accessibility gap under EAA enforcement** — concrete remediation
   patterns for AI chat UI, an area where demand clearly exceeds published guidance.
7. **Post-chat AI interaction models** — inline/ambient AI, diff-and-approve surfaces,
   agent progress disclosure; deliberately excluding anything that is just "add a prompt
   bar".

Source-diversity note for next time: lean on **Open UI, W3C/WHATWG, Interop, MDN,
browser release notes and named practitioners** (Roselli, Soueidan, Kravets,
Coyier, Bramus). Design-agency blogs and `dev.to` trend roundups produced nothing
first-hand this round.
