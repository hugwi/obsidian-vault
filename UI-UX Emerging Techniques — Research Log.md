---
created: 2026-08-16
categories:
  - "[[Resources]]"
domain: engineering
project: "[[Blog ideas]]"
tags:
  - ui-ux
  - web-platform
  - accessibility
  - performance
  - research-log
---

# UI/UX Emerging Techniques — Research Log

Running log for the recurring "emerging UI/UX techniques" research sweep. **Append a new
`## Run YYYY-MM-DD` section each time**; use the [[#Coverage ledger]] at the bottom to avoid
re-reporting the same findings. Companion to [[Agentic Engineering — Trends 2026]], which
covers the agent side; this one covers the *interface* side.

> [!note] Why this note exists
> Before this log, the vault's UI/UX material was almost entirely **AI-tooling-oriented** —
> Claude design skills, 21st.dev, Dribbble, "make your web app feel native", button
> guidelines. Almost nothing on the **web platform primitives** underneath. This log tracks
> that layer: interaction APIs, accessibility standards, and interaction-latency work.

Raw material for [[Blog ideas]] Idea 1 (AI UX/UI slop → motion slop) — §2 in particular.
Remove the `project:` property if it clutters that desk.

---

## Run 2026-08-16

Five findings, none of which had any prior coverage in the vault (see [[#Coverage ledger]]).
The through-line: **behaviour that used to require JavaScript is moving into HTML and CSS**,
and the UX win is less about the code saved than about the *accessibility and latency
contract* moving from app code into the browser.

### 1. Declarative interaction primitives — dialogs, popovers, tooltips with no JS

Three separate specs landed close enough together to be usable as one pattern:

| Feature | What it does | Support |
|---|---|---|
| **Invoker Commands** — `command` / `commandfor` on `<button>` | Buttons drive dialogs/popovers declaratively: `<button commandfor="dlg" command="show-modal">` | **Baseline Newly Available 2025-12-12.** Chrome/Edge 135, Firefox 144, Safari 26.2 |
| **Interest Invokers** — `interestfor` on `<button>`/`<a>` | Hover cards, tooltips, hover menus. The UA detects "interest" — mouse hover, a keyboard hotkey, **or touchscreen long-press** | Chromium 142 (Oct 2025). Not yet in Firefox/Safari; Mozilla standards-position still open |
| **CSS Anchor Positioning** — `anchor()`, `position-anchor`, `position-area`, `@position-try` | Tethers a floating element to an anchor, with declarative flip/fallback when it would overflow | Chrome/Edge 125+, Safari 26+, Firefox 147+ (145–146 behind a flag). ~81–83% global |

Built-in command values include `show-modal`, `close`, `request-close`, `toggle-popover`,
`show-popover`, `hide-popover`. Custom commands use a `--` prefix and dispatch a
`CommandEvent`, so the declarative wiring degrades into your own handler when you need one.

**Why it improves UX.** The things hand-rolled dropdowns and modals get wrong are
depressingly consistent: focus is never moved into the dialog, Escape doesn't close it,
light-dismiss doesn't work, the ARIA relationship is missing, and hover-only affordances are
unreachable by keyboard or touch. All of that is exactly what these APIs move into the user
agent. `interestfor` is the sharpest example — it is the first time the platform has given
hover-triggered UI a *specified* keyboard and touch equivalent instead of leaving each team
to reinvent one badly. Secondary win: buttons are interactive before any script parses, which
takes work off the interaction path (see §4).

**Tools/frameworks.** Displaces **Floating UI** for the common cases — tooltips, dropdowns,
context menus, popovers. A JS `interestfor` polyfill exists on npm. Still reach for a JS
library for deeply nested dynamic menus, shadow-DOM/cross-origin cases, and virtualised lists
where the anchor can unmount.

**Sources.** [MDN: Invoker Commands API](https://developer.mozilla.org/en-US/docs/Web/API/Invoker_Commands_API) ·
[Web platform features explorer](https://web-platform-dx.github.io/web-features-explorer/features/invoker-commands/) ·
[CSS-Tricks: first look at the Interest Invoker API](https://css-tricks.com/a-first-look-at-the-interest-invoker-api-for-hover-triggered-popovers/) ·
[Intent to Ship: Interest Invokers](https://groups.google.com/a/chromium.org/g/blink-dev/c/bX1G_yDt6W4) ·
[Josh Comeau: Getting Started with Anchor Positioning](https://www.joshwcomeau.com/css/anchor-positioning/) ·
[OddBird: Anchor Positioning updates](https://www.oddbird.net/2025/10/13/anchor-position-area-update/)

### 2. Scroll-*triggered* animations (`animation-trigger`) — distinct from scroll-driven

Chrome 145 ships `animation-trigger`, `timeline-trigger` and `trigger-scope`. This is **not**
the same as scroll-driven animation:

- **Scroll-driven** (`animation-timeline`, shipped earlier) — animation *progress is scrubbed
  by scroll position*. Scroll back, it rewinds. This is the scroll-hijacking primitive.
- **Scroll-triggered** (`animation-trigger`, new) — a **normal time-based animation that
  fires when a scroll offset is crossed**, then plays at its own speed:
  `animation-trigger: --t play-forwards play-backwards;` — `play-forwards` on activation,
  `play-backwards` on deactivation. `trigger-scope` bounds a trigger declared on a rule that
  matches many elements.

**Why it improves UX.** Reveal-on-scroll is the single most common motion pattern on the web
and until now every instance of it was a bespoke `IntersectionObserver` plus a class toggle.
Moving it into CSS means it is declarative, off the main thread, and — the part that matters
— **one `prefers-reduced-motion` media query disables all of it**, instead of reduced-motion
support depending on whoever wrote the observer remembering to check. It also draws a clean
line for the [[Blog ideas]] motion-slop argument: scroll-*triggered* reveal is benign, scroll-
*driven* scrubbing is the thing that disorients people.

Support caveat worth keeping straight: **scroll-driven animations are Chromium (2023) + Safari
(2025); Firefox has them fully implemented but behind `layout.css.scroll-driven-animations.enabled`
and not shipped by default** (~85% caniuse). Scroll-*triggered* is Chrome-only for now.

**Tools/frameworks.** Directly targets what **GSAP ScrollTrigger** and **Framer Motion** are
used for. Bundle-size context: Framer Motion ~30–50 KB gzipped, GSAP ~70 KB.

**Sources.** [Chrome for Developers: CSS scroll-triggered animations are coming](https://developer.chrome.com/blog/scroll-triggered-animations) ·
[Bram.us](https://www.bram.us/2025/12/12/css-scroll-triggered-animations-are-coming-to-chrome/) ·
[Explainer](https://github.com/explainers-by-googlers/scroll-triggered-animations) ·
[CSS-Tricks: A First Look at Scroll-Triggered Animations](https://css-tricks.com/css-scroll-triggered-animations-first-look/) ·
[Josh Comeau: Scroll-Driven Animations](https://www.joshwcomeau.com/animation/scroll-driven-animations/)

### 3. Cross-document View Transitions for multi-page apps

`@view-transition { navigation: auto; }` on both participating same-origin pages, and the
browser snapshots the old document, swaps in the new one, and animates between them — **no
SPA framework, no client-side router**.

- Chromium 126+, Safari 18.2+. Not in Firefox yet.
- Named an **Interop 2026 focus area**, so the Firefox gap is actively funded work.
- Pure progressive enhancement: an unsupporting browser just does a hard cut.

**Why it improves UX.** This removes the main *experiential* reason teams adopt an SPA. The
"feels like an app" quality that [[The comprehensive guide to making your web app feel native (01kn9w7j1qv79yte6nxjnbzg2m).md|The comprehensive guide to making your web app feel native]]
and [[What Makes a WebApp Feel Native? (Insider Secrets) (01kmws0fjds9hrkmmnqj44a29y).md|What Makes a WebApp Feel Native? (Insider Secrets)]] chase with client-side routing is
now available to a plain server-rendered MPA — while keeping real URLs, back/forward, and no
router bundle. Pair it with §4's speculation rules and an MPA is genuinely competitive.

**Sources.** [Chrome for Developers: cross-document view transitions](https://developer.chrome.com/docs/web-platform/view-transitions/cross-document) ·
[MDN: View Transition API](https://developer.mozilla.org/en-US/docs/Web/API/View_Transition_API) ·
[Interop 2026 (web.dev)](https://web.dev/blog/interop-2026) · [WebKit: Announcing Interop 2026](https://webkit.org/blog/17818/announcing-interop-2026/) ·
[CSS-Tricks: cross-document view transitions gotchas](https://css-tricks.com/cross-document-view-transitions-part-1/)

### 4. Treating interaction latency, not load time, as the UX metric

Two complementary levers, both under-adopted:

**`scheduler.yield()` for long tasks.** Chrome 129+ (Sept 2024) and Firefox; **not Safari**, so
always ship a `setTimeout` fallback. `await scheduler.yield()` inside a long loop hands the
main thread back so queued input can be processed, then resumes with priority — unlike
`setTimeout(0)`, which goes to the back of the queue. Note it does *not* move work off the
main thread; it only carves it up.

**Speculation Rules for navigation.** A JSON `<script type="speculationrules">` block
declaring `prefetch`/`prerender` targets with an `eagerness` level (`conservative` /
`moderate` / `eager` / `immediate`) — e.g. `moderate` prerenders on hover, so the next page is
already rendered when the click lands.

**Why it improves UX.** INP is the Core Web Vital that most sites still fail — the threshold
is 200 ms at p75, and anything slower reads to a user as "the page is broken", which is a much
more direct UX signal than a load-time number. Speculation rules attack the other half: the
reported p75 LCP for prerendered navigations is ~320 ms against ~1,800 ms for normal ones on
the same sites. Both are *configuration-level* wins that need no redesign, which makes them
unusually cheap relative to their effect.

**Tools/frameworks.** DebugBear and CrUX/RUM dashboards for measurement; `scheduler.postTask()`
for priority control; the Chrome speculation-rules codelab for implementation.

**Sources.** [Chrome for Developers: use scheduler.yield()](https://developer.chrome.com/blog/use-scheduler-yield) ·
[MDN: Scheduler.yield()](https://developer.mozilla.org/en-US/docs/Web/API/Scheduler/yield) ·
[web.dev: Optimize long tasks](https://web.dev/articles/optimize-long-tasks) ·
[Chrome: Prerender pages](https://developer.chrome.com/docs/web-platform/prerender-pages) ·
[MDN: Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API) ·
[Google Codelab](https://codelabs.developers.google.com/speculation-rules) ·
[DebugBear: measuring INP](https://www.debugbear.com/docs/metrics/interaction-to-next-paint)

### 5. Accessibility moving from checklist to outcome — and from guideline to law

Three currents, and the third is the one with a deadline attached:

**WCAG 3.0** (Working Draft, updated March 2026; expected 2027–28) restructures the standard:
outcomes **rated on a scale** rather than binary pass/fail, a set of "critical errors" that
stay non-negotiable (missing alt text, insufficient contrast), guidance grouped by disability
type, and two test styles — **atomic** (one element) and **holistic** (a whole journey with
assistive tech). Cognitive accessibility gets first-class treatment via the Cognitive
Accessibility Research Modules — dyslexia, ADHD, memory impairment.

**European Accessibility Act enforcement is live.** WCAG 2.1 AA is now a legal requirement for
consumer-facing digital services sold into the EU. First lawsuits filed in France (Nov 2025);
enforcement broadening through 2026. **Reported maximum fines in Sweden are around €900k**,
against ~€60k in Ireland — worth flagging given the vault's Nordic client work.

**W3C's AI-accessibility work.** The APA/RQTF Editor's Draft *Accessibility of machine learning
and generative AI* treats AI-generated interfaces, automated accessibility evaluation, and
personalised interfaces as open problems — explicitly naming the risk that AI-assisted
interface generation produces inaccessible output at scale.

**Why it improves UX.** The outcome-scale model is the substantive change: today an interface
can pass every WCAG 2.x success criterion and still be unusable end-to-end, because the
criteria are element-level. Holistic journey testing is what closes that gap. And the third
current makes this concrete for the vault's own subject matter — the accessibility risk of
agent-generated UI is now both a documented W3C concern *and* a legally enforceable exposure,
which is a sharper version of the [[Blog ideas]] slop argument than "it looks generic".

**Sources.** [W3C WAI](https://www.w3.org/WAI/) ·
[W3C Editor's Draft: Accessibility of ML and generative AI](https://w3c.github.io/ai-accessibility/) ·
[Level Access: EAA compliance in 2026](https://www.levelaccess.com/blog/eaa-compliance-in-2026-how-enforcement-has-evolved-and-what-to-expect-next/) ·
[Davis Wright Tremaine: EAA goes live](https://www.dwt.com/insights/2025/07/european-accessibility-act-digital-products)

---

### 🔨 Most actionable single item: Chrome's Modern Web Guidance

Not a UI pattern, but the highest-leverage find of this run given the rest of the vault.
**[GoogleChrome/modern-web-guidance](https://github.com/GoogleChrome/modern-web-guidance)** is
a Chrome-team **agent skill** that keeps coding agents off legacy frontend patterns:

- ~128 web platform features across 100+ expert-verified use cases, including the
  declarative dialog/popover control guide behind §1.
- Queries live **Baseline** compatibility data, so guidance adapts to your stated browser
  support floor rather than to the model's training cutoff.
- Retrieval runs **locally** — an offline TensorFlow.js embedding model, no API key, no
  network — via a `modern-web-guidance` CLI the agent calls.
- Google's internal benchmark claims a **37 percentage-point** improvement in web
  best-practice adherence for a generic coding agent equipped with it.

This is the direct answer to the failure mode in [[Blog ideas]] Idea 1: agents write the
statistical average of the web, which is 2019 frontend. Fits alongside
[[Top 8 Claude Skills for UI-UX Engineers (01kmjvkfe409s931319nmnrtvg).md|Top 8 Claude Skills for UI-UX Engineers]] and [[I Built 63 Design Skills For Claude - and They're Free (01kmjvnp1y7sxvqcyz5yg4b4ds).md|I Built 63 Design Skills For Claude - and They're Free]],
but it is first-party and compat-data-backed rather than taste-based — a different category of
tool. **Candidate for `action: implement`.**

Also see [LogRocket's write-up](https://blog.logrocket.com/chromes-modern-web-guidance-prevent-ai-coding-agents/)
and the [Chrome docs](https://developer.chrome.com/docs/modern-web-guidance).

### 👀 Watch list (not yet worth a note)

**Agent-facing UI protocols.** A protocol layer is forming for interfaces where the *agent*
is the actor: **AG-UI** (streams agent output to a frontend as it is generated), **A2UI /
Open-JSON-UI** (the agent *describes* UI declaratively), **MCP-UI** (interactive components
inside an agent surface), alongside A2A and MCP. AG-UI reportedly has adapters across
LangGraph, CrewAI, Microsoft Agent Framework, Google ADK, AWS Strands, Pydantic AI and
LlamaIndex. The design questions — how an agent communicates status, uncertainty, and
reversibility, and how a user overrides an in-flight action — are real and largely unsolved.
Held back from the main list because the sourcing was thin and the space is visibly churning.

**Calm / attention-respecting interfaces.** Widely claimed as the 2026 mood — fewer
notifications, less motion, "why am I seeing this?" explanation layers on AI features, adaptive
UI that reshapes controls to context. Genuinely interesting, but every source found was a
trends listicle with no research behind it. Re-check against NN/g/Baymard primary work before
promoting.

---

## ⚠️ Sourcing caveat for this run

Two constraints worth recording, because they bound how much to trust the numbers above:

1. **`WebFetch` was blocked by the network egress proxy for every domain tried** —
   `developer.chrome.com`, `developer.mozilla.org`, `w3c.github.io`, `css-tricks.com` and
   others all returned `EGRESS_BLOCKED`. Only `WebSearch` was available, so **every finding
   here rests on search-result summaries, not on primary documents read end-to-end.** Links are
   given so the primary sources can be opened by hand.
2. **The 2026 SEO-blog layer is actively unreliable on browser support.** First-round results
   confidently reported CSS Anchor Positioning as "Firefox 132+, Safari 18.2+ / Baseline 2026,
   91% coverage". Targeted follow-up searches contradicted this: **Firefox 147+, Safari 26+,
   ~81–83%**. The same sources also gave "Firefox 132+" for scroll-driven animations, which are
   in fact still behind a flag in Firefox. Version numbers in this note were re-checked with a
   second independent query; treat any figure not re-checked as provisional.

Lower-confidence figures, all from secondary sources and unverified against CrUX/HTTP Archive:
"43% of sites fail INP", "p75 LCP 320 ms vs 1,800 ms prerendered", "~28% of navigations
successfully speculated", the Framer Motion/GSAP removal figures, and the 37-point Modern Web
Guidance benchmark.

---

## Coverage ledger

Checked against the vault before reporting. Prior UI/UX material is concentrated in
[[MOC - Design Automation]], the `Clippings/` folder, and the Claude-design-skill notes.

**Already covered in the vault — deliberately not repeated:**
- Claude/AI design skills and generators — [[Top 8 Claude Skills for UI-UX Engineers (01kmjvkfe409s931319nmnrtvg).md|Top 8 Claude Skills for UI-UX Engineers]],
  [[I Built 63 Design Skills For Claude - and They're Free (01kmjvnp1y7sxvqcyz5yg4b4ds).md|I Built 63 Design Skills For Claude - and They're Free]],
  [[Must-Have UX-UI Design Skills for Claude Code (01knacby9a2jde4th3a72jqsmr).md|Must-Have UX-UI Design Skills for Claude Code]],
  [[7 Claude Code Design Skills That Follow a Real Design Process (01kqrxg70rhkty6zkmxpff4xb6).md|7 Claude Code Design Skills That Follow a Real Design Process]], [[AIDesigner (01kp3xv7y6k8tptwm1th9a6m07).md|AIDesigner]],
  [[Open Design is Here: The Open-Source Claude Code Design Alternative (01kqt5hr45brng7dadsf88kgb5).md|Open Design is Here: The Open-Source Claude Code Design Alternative]]
- Component/inspiration sources — [[UI Components (01kqz9ms303f9ez2e4dxq2dx3p).md|UI Components]], [21st.dev community UI components](Discover%20community-made%20UI%20components%20%7C%2021st%20%2801kqza5gygycn69zta0e6dwwjq%29.md),
  [[Dribbble - Discover the Worlds Top Designers & Creative Professionals (01kna0m6yfnys6m6ngdgh93d3g).md|Dribbble - Discover the Worlds Top Designers & Creative Professionals]], [[Inspiration]]
- "Feel native" / PWA — [[The comprehensive guide to making your web app feel native (01kn9w7j1qv79yte6nxjnbzg2m).md|The comprehensive guide to making your web app feel native]],
  [[What Makes a WebApp Feel Native? (Insider Secrets) (01kmws0fjds9hrkmmnqj44a29y).md|What Makes a WebApp Feel Native? (Insider Secrets)]], [[How can you make website feel like a native app? (01kmwrzcdkw1059h1f6nry6gjn).md|How can you make website feel like a native app?]]
- Visual craft fundamentals — [[7 Rules for Creating Gorgeous UI (01kn9zv7vjs2fn3r9yksh1xez4).md|7 Rules for Creating Gorgeous UI]],
  [[UX UI tips: A guide to creating buttons (01kna3aq4ey3vchmq67ra50t5r).md|UX UI tips: A guide to creating buttons]], [[Every UI-UX Concept Explained in Under 10 Minutes (01kna4wk4axs6p6078mytd9pnr).md|Every UI-UX Concept Explained in Under 10 Minutes]],
  [[142 JavaScript Text Effects (01krvdtb6ddrgyqdbqf5xv0h1f).md|142 JavaScript Text Effects]]

**Confirmed absent before this run** (grep across the vault returned nothing): `commandfor`,
`interestfor`, invoker commands, anchor positioning, `animation-trigger`, scroll-triggered,
speculation rules, `scheduler.yield`, WCAG 3.0, European Accessibility Act, AG-UI, A2UI, MCP-UI.
Only three incidental hits existed: View Transitions named in passing in
[[What Makes a WebApp Feel Native? (Insider Secrets) (01kmws0fjds9hrkmmnqj44a29y).md|What Makes a WebApp Feel Native? (Insider Secrets)]], "scroll-driven timelines" in
[[Blog ideas]], and INP mentioned in an [[Angular v16 is here! (01kanvey5p8xgv62vjtd0cnmtr).md|Angular v16 is here!]] clipping.

### Search angles already used (vary these next run)

Scroll-driven/triggered animation · view transitions · CSS replacing JS · WCAG 3 + cognitive
accessibility · INP/Core Web Vitals · generative & adaptive UI · invoker commands · anchor
positioning · speculation rules · NN/g AI chat usability · European Accessibility Act ·
calm technology · Interop 2026 · agent-facing UI protocols.

### Suggested angles for next run

- **Primary sources only** — restrict searches to `web.dev`, `developer.chrome.com`,
  `webkit.org`, `hacks.mozilla.org`, `nngroup.com`, `smashingmagazine.com`, `baymard.com`.
  This run showed the generic 2026 blog layer is actively wrong on facts.
- **Chrome/Safari/Firefox release notes** for the last two quarters, read directly, rather
  than trend articles — Safari 26.x and Chrome 146–148 notes.
- **Design-system engineering**, untouched so far: design tokens (DTCG format), Style
  Dictionary, theming/`light-dark()`, container queries in component APIs.
- **Forms and input** — the most-used and least-discussed surface: `<selectmenu>`/customisable
  `<select>`, Popover-based comboboxes, the Digital Credentials API, passkey UX.
- **Non-visual and multimodal** — voice-first interaction patterns, `prefers-reduced-*`
  media-query family beyond motion, screen-reader-specific interaction research.
- **Measured evidence rather than trends** — Baymard Institute UX research, HTTP Archive Web
  Almanac chapters, actual A/B case studies. This run was thin on primary research.
- **Motion accessibility specifically** — vestibular-disorder research, to sharpen
  [[Blog ideas]] Idea 1 beyond the NN/g scrolljacking finding already cited there.
