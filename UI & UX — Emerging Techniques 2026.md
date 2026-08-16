---
created: 2026-08-16
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - ui
  - ux
  - web-design
  - frontend
  - accessibility
  - performance
---

# UI & UX — Emerging Techniques 2026

Running research log on emerging UI/UX techniques and patterns, kept the same way as
[[Agentic Engineering — Trends 2026]]: a snapshot per research pass, newest first, with each
finding cross-checked against what the vault already holds. Visual references live in
[[Inspiration]]; this note is about *technique*, not taste.

Each pass records what was genuinely new, what turned out to be already covered, and which
search angles to try next so successive passes don't re-tread the same ground.

---

## Pass 1 — 2026-08-16

Vault coverage before this pass was almost entirely AI-agent-flavoured design content (design
skills for Claude Code, "gorgeous UI" rule lists, PWA native-feel guides). The web-platform
layer — what browsers now do natively — and the measurement layer were essentially absent.
All five findings below are new to the vault.

### 1. The interaction layer moved into CSS — anchor positioning, popover, customizable select

The tooltip/dropdown/menu stack that has justified a JS positioning library for a decade is now
a browser primitive. CSS Anchor Positioning is spec-stable with implementations across Chrome,
Safari, Firefox and Edge; the Popover API has gone from experiment to production-grade. The
important detail is the *implicit* wiring: associating a popover with its invoker automatically
creates an anchor reference, so the invoker becomes the popover's anchor element with no
explicit `anchor-name` plumbing. `<select>` opts into the same machinery via
`appearance: base-select`, which gives the element and its picker an implicit popover-invoker
relationship — and therefore an implicit anchor reference too.

**Why it matters for UX** — the top-layer, focus management, Esc-to-dismiss and light-dismiss
behaviour come from the browser rather than from whatever the component author remembered to
implement, so the accessible behaviour is the default rather than the diligent path. Positioning
runs off the main thread, and the whole category of "dropdown renders behind the modal" z-index
bugs disappears. Reported coverage: the tooltip and dropdown cases that drive roughly 90% of
Floating UI installs.

**Tools** — CSS Anchor Positioning (`anchor-name`, `position-anchor`, `position-area`,
`position-try-fallbacks`), Popover API (`popover`, `popovertarget`),
`appearance: base-select`. Displaces Floating UI / Popper for simple-to-moderate cases; a JS
library is still the answer for genuinely complex collision and virtual-element scenarios.

- [Why CSS Anchor Positioning and the Popover API Matter in 2026](https://kvassiliou.com/tech/css-anchor-positioning-popover-api-2026)
- [Anchor Positioning and the Popover API for a JS-Free Site Menu — CSS { In Real Life }](https://css-irl.info/anchor-positioning-and-the-popover-api/)
- [Make your content pop with the Popover API and CSS Anchor Positioning](https://oidaisdes.org/blog/popover-api-accessibility/)
- [MDN — Using CSS anchor positioning](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Anchor_positioning/Using)

### 2. Compositor-driven motion — scroll-driven animations + View Transitions

Scroll-driven animations reached universal support, giving two timeline types:
`scroll-timeline` (progress tied to scroll position — reading indicators, progress bars,
parallax) and `view-timeline` (progress tied to an element's visibility in the scrollport —
reveal-on-scroll, entrance/exit). Both run on the compositor. The View Transitions API landed
cross-browser over 2025–26 and animates between two DOM states by snapshotting the old state,
applying the new one, and tweening — which in an SPA means route-to-route transitions.

**Why it matters for UX** — this is the rare case where the better-looking option is also the
faster one. `IntersectionObserver` plus scroll listeners plus a motion library is replaced by
declarative CSS that never touches the main thread, which directly protects INP (see finding 4).
Motion that used to be a performance tax is now roughly free, so the honest reason to skip it
stops being budget and starts being taste. `prefers-reduced-motion` remains a hard requirement,
not a nicety.

**Tools** — `animation-timeline`, `scroll-timeline`, `view-timeline`, `timeline-scope`,
`view-transition-name`, `@view-transition`. Also emerging: the Interest Invoker API
(`interesttarget`, `interest-delay`) for hover/focus intent at the browser level — early support,
worth watching rather than shipping.

- [View Transitions API and CSS Scroll-Driven Animations: The Browser Wins of 2026](https://www.frontendhorizon.com/blog/view-transitions-api-and-css-scroll-driven-animations-the-browser-wins-of-2026)
- [Creating Complex Scroll-driven Animations with Pure CSS in 2026](https://dev.to/nickbenksim/creating-complex-scroll-driven-animations-with-pure-css-in-2026-17l)
- [CSS Innovations 2026: Emerging Features That Replace JavaScript](https://locallylost.com/guides/css-innovations-2026-features-that-replace-javascript/)

### 3. Speculation Rules — perceived performance as a declarative config, not an optimisation project

Speculation Rules let a page declare which URLs the browser should prefetch or prerender, with
eagerness levels controlling how aggressively. Reported field data: prerendered navigations hit
a 75th-percentile LCP of ~320 ms against ~1,800 ms for standard navigations. Ray-Ban is cited as
increasing mobile product-page conversion by ~101% after prerendering key pages. Chrome 144
(January 2026) added **"prerender until script"**, which fetches HTML and starts rendering and
subresource loading but pauses at the first blocking `<script>` — so CSS, images and fonts are
preloaded without any JavaScript side effects firing on a page the user may never visit.

**Why it matters for UX** — instant navigation is the single largest perceived-speed win
available, and "prerender until script" removes the main reason teams held back: analytics
double-counting, premature session starts, and other side effects on speculatively loaded pages.
The trade-off is bandwidth and server load spent on navigations that never happen, which is why
eagerness tuning is the actual design decision.

**Tools** — `<script type="speculationrules">`, eagerness levels
(`immediate` / `eager` / `moderate` / `conservative`), document rules with `where`/`href_matches`,
the corewebvitals.io speculation-rules generator. Pairs naturally with View Transitions for MPAs.

- [Instant Loading Pages with Speculation Rules](https://www.corewebvitals.io/pagespeed/speculation-rules)
- [Prerender pages in Chrome for instant page navigations — Chrome for Developers](https://developer.chrome.com/docs/web-platform/prerender-pages)
- [How Monrif improved engagement by 8.9% and reduced LCP by 17.9% with Speculation Rules prerender and bfcache — web.dev](https://web.dev/case-studies/monrif-cwv)

### 4. Soft Navigations API — SPAs finally get honest Core Web Vitals

The long-standing measurement hole: in an SPA a route change updates the URL and repaints
without a page load, so LCP, CLS and INP for every view after the first are either missing or
attributed to the initial load. Chrome detects soft navigations heuristically — a user
interaction triggers `pushState`/`replaceState`, that leads to visible DOM change and a paint,
and a new history entry is created — so no developer-defined markers are required. Chrome 151
exposes two new `PerformanceEntry` types: `soft-navigation` and `interaction-contentful-paint`,
the latter being LCP-style behaviour measured from a user interaction rather than a page load.
Origin-trial work started in Chrome 139 (July 2025) and continued through Chrome 147.

**Why it matters for UX** — it closes the gap between "our dashboard feels slow after you click
into a record" and anything the RUM data could previously show. For app-shaped products the
in-app navigations are the whole experience and were the part nobody could measure; this makes
the second, third and tenth view first-class in performance budgets.

**Tools** — `PerformanceObserver` on `soft-navigation` and `interaction-contentful-paint`,
`web-vitals.js` soft-nav support, RUM vendors adding soft-nav attribution.

- [Measuring soft navigations — Chrome for Developers](https://developer.chrome.com/docs/web-platform/soft-navigations)
- [Final Soft Navigations origin trial starting in Chrome 147](https://developer.chrome.com/blog/final-soft-navigations-origin-trial)
- [Why the Soft Navigations API Enables Better SPA Core Web Vitals Auditing — SALT.agency](https://salt.agency/blog/why-the-soft-navigations-api-enables-better-spa-core-web-vitals-auditing/)
- [Soft Navigations in Chrome 151: How to Prepare and What to Measure](https://apogeewatcher.com/blog/soft-navigations-chrome-151-prepare-measure)

### 5. Agentic UX — a pattern language for interfaces where the software acts on its own

The most genuinely underexplored area found, and the one closest to this vault's centre of
gravity. As products embed agents, the design problem stops being buttons-pages-flows and
becomes collaboration between a person and something that acts between their turns. Five
patterns recur across enterprise agent UIs:

| Pattern | What it does |
|---|---|
| **Planning visibility** | show the plan before execution, not just the result |
| **Tool-use disclosure** | name which tool/data the agent reached for, and when |
| **Memory surfacing** | make what the agent remembers inspectable and editable |
| **Workflow tracking** | render multi-step progress, including steps not yet started |
| **Recovery routing** | a defined path back when the agent is wrong, beyond "undo" |

Adjacent to this is **generative UI**: parts of the interface generated, selected or controlled
by the agent at runtime, adapting to what it is doing and what it needs from the user. Gartner's
projection — ~40% of enterprise apps embedding task-specific agents by end of 2026, up from under
5% in 2025 — is the usual analyst number and should be treated as directional.

**Why it matters for UX** — traditional UI has no vocabulary for latency measured in minutes, for
partial autonomy, or for an interface state the user didn't cause. Every one of these five
patterns is a trust mechanism: an agent that shows its plan and discloses its tools can be
corrected early, which is far cheaper than an undo after the fact. Worth noting how much of this
is 1995 progressive disclosure re-derived — a 2026 study (Anik & Bunt) found progressive
disclosure improved *perceived* learning, i.e. people felt they understood a system better when
it revealed itself in stages.

**Tools** — CopilotKit (generative UI primitives), AI SDK / assistant-ui for streaming and tool
call rendering, LangGraph for the plan-and-step state the UI renders.

- [Agentic UX: Frontend Design Patterns for AI Agents in 2026 — Zylos Research](https://zylos.ai/research/2026-05-28-agentic-ux-frontend-design-patterns-ai-agents/)
- [Agent UX: UI Design for AI Agents in 2026 — Fuselab Creative](https://fuselabcreative.com/ui-design-for-ai-agents/)
- [The Developer's Guide to Generative UI in 2026 — CopilotKit](https://www.copilotkit.ai/blog/the-developer-s-guide-to-generative-ui-in-2026)
- [Progressive Disclosure Matters: Applying 90s UX Wisdom to 2026 AI Agents](https://aipositive.substack.com/p/progressive-disclosure-matters)

---

### Also tracked this pass (lower priority, still new)

- **DTCG design tokens spec hit first stable version (2025.10, published 2025-10-28)** — solved
  multi-file support, theming and advanced colour. Supported or being implemented by Penpot,
  Figma, Sketch, Framer, Knapsack, Supernova, zeroheight, with reference implementations in Style
  Dictionary, Tokens Studio and Terrazzo. The interesting framing: tokens stop being a design
  artefact and become a *platform contract* — the shared vocabulary between design, code and AI
  code generation, which is the first thing that makes an LLM emit on-brand UI by default. The
  cited "84% adoption" figure counts teams using tokens in any form, and most of those still have
  Figma variables and code variables that quietly disagree.
  → [DTCG announcement](https://www.w3.org/community/design-tokens/2025/10/28/design-tokens-specification-reaches-first-stable-version/) ·
  [The design tokens spec (DTCG) explained — zeroheight](https://zeroheight.com/learn/the-design-tokens-spec-dtcg-explained/) ·
  [The Design Token Spec Is Finally Real. Now What?](https://themotiondesign.com/writing/design-token-spec-finally-real-now-what)

- **Accessibility: enforcement arrived, the standard is still moving** — the European
  Accessibility Act has been enforced since 2025-06-28 against EN 301 549 (aligned to WCAG 2.1
  AA), with **EN 301 549 v4.1.1 expected to publish during 2026** and to become the compliance
  target once it lands in the Official Journal. WCAG 3.0 is *not* a compliance target: draft
  expected 2026, final 2028+. Its substantive shift is outcomes-based Bronze/Silver/Gold scoring
  plus far broader **cognitive** and low-vision coverage — the area WCAG 2.x under-serves, since
  it has leaned on sensory and physical impairment. Practical move now, ahead of any deadline:
  put cognitive checks into design review and content QA, and standardise the patterns for forms,
  navigation, errors and help content.
  → [WCAG 3.0 overview and update 2026 — AbilityNet](https://abilitynet.org.uk/resources/digital-accessibility/what-expect-wcag-30-web-content-accessibility-guidelines) ·
  [European Accessibility Act compliance guide — Level Access](https://www.levelaccess.com/compliance-overview/european-accessibility-act-eaa/) ·
  [Accessibility Trends to Watch in 2026](https://www.accessibility.com/blog/accessibility-trends-to-watch-in-2026)

- **Local-first has crossed from research to `npm install`** — PowerSync, ElectricSQL, Zero and
  Triplit. The UX claim worth testing: with local reads and writes the interface is *genuinely*
  instant, which removes the need for skeleton screens and optimistic-update rollback rather than
  making them easier. The design work shifts to representing sync state and conflict resolution
  honestly. Note the vault already has substantial local-first material — this is an update to it,
  not a new thread.
  → [The Architecture Of Local-First Web Development — Smashing Magazine](https://www.smashingmagazine.com/2026/05/architecture-local-first-web-development/) ·
  [Cool frontend arts of local-first — Evil Martians](https://evilmartians.com/chronicles/cool-front-end-arts-of-local-first-storage-sync-and-conflicts)

---

### ⚠️ One claim that did not survive checking

Multiple SEO blogs assert that a March 2026 Google update **tightened the "good" LCP threshold
from 2.5 s to 2.0 s** and promoted INP to an equal ranking signal, some citing a Search Central
post dated 2026-03-18 and quoting specific ranking-drop figures. A domain-restricted search
across `web.dev`, `developers.google.com` and `developer.chrome.com` still returns **2.5 s at the
75th percentile** as the current good threshold, with no trace of a 2.0 s revision. Treat the
2.0 s number as **unverified and probably fabricated** — it has the signature of SEO-blog
telephone. INP *has* been a Core Web Vital since March 2024, which is likely what the claim is
garbling. The genuinely useful number in that cluster: ~43% of sites reportedly fail INP, and the
dominant cause is main-thread-blocking JavaScript — which loops straight back to findings 2 and 4.
→ [Largest Contentful Paint (LCP) — web.dev](https://web.dev/articles/lcp)

---

### Cross-reference against prior vault research

| Topic | Prior coverage | Verdict |
|---|---|---|
| Anchor positioning, `base-select` | none | **new** |
| Soft Navigations API | none | **new** |
| Agentic UX / generative UI | none | **new** |
| Speculation Rules | 1 SEO-skill clipping, in passing | **new as a UX technique** |
| View Transitions | 4 notes, all "make a web app feel native" | **new framing** (compositor/INP) |
| Scroll-driven animations | 3 notes, incidental | **new as technique** |
| Design tokens | 11 notes, all AI-design-skill clippings | **new** (DTCG stable spec) |
| WCAG | 13 notes, all AI-design-skill clippings | **new** (EAA enforcement, WCAG 3 status) |
| Local-first | 17 notes | **update**, not new |

### Search angles for the next pass

Deliberately not repeating this pass's queries. Untried angles, roughly in order of expected
yield:

1. **Primary sources over listicles** — Chrome release notes, WebKit "News from WWDC"/release
   posts, Interop 2026 focus areas, `web.dev` blog. Most of this pass's results were SEO-farm
   restatements; go upstream.
2. **Conference talks** — Local-First Conf 2026, CSS Day, Smashing Conf, Config. Talk abstracts
   surface technique 6–12 months before the blog wave.
3. **Design-engineering practitioners by name** — Rauno Freiberg, Emil Kowalski, Adam Argyle, Una
   Kravets, Josh Comeau, Vaunt/Paco Coursey. Craft-level detail that never reaches trend posts.
4. **Failure literature** — "dark patterns 2026", regulatory action on deceptive design, AI
   interface failures, agent-UX post-mortems. What broke is more informative than what launched.
5. **Non-web surfaces** — spatial/visionOS interaction, voice and multimodal UI, in-car HMI, CLI
   and TUI design. Patterns migrate to the web with a lag.
6. **Named platform features not yet checked** — `@scope`, `interpolate-size`/`calc-size`,
   masonry layout, `<selectedcontent>`, Navigation API, container queries in production, CSS
   Carousels (`::scroll-button`, `::scroll-marker`).
7. **Empirical rather than editorial** — Baymard Institute, NN/g new studies, HTTP Archive Web
   Almanac 2026, Chrome UX Report analyses.
