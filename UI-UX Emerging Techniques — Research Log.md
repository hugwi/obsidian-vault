---
created: 2026-08-16
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - ux-ui
  - frontend
  - accessibility
  - performance
  - research-log
---

# UI-UX Emerging Techniques — Research Log

> Running log from a recurring research task on emerging UI/UX techniques and patterns.
> **Each run appends a dated section** and updates the *Covered so far* ledger below, so the
> next run can tell genuinely new findings from repeats without re-reading the whole note.
>
> Companion to [[Agentic Engineering — Trends 2026]] (same "snapshot of where things are
> heading" format, different problem domain).

## Covered so far — dedupe ledger

Check new findings against this list first. If a search returns only these, it's a repeat.

| Technique / pattern | First logged |
|---|---|
| Declarative interactivity (Popover, anchor positioning, invoker commands, interest invokers) | 2026-08-16 |
| CSS carousels + scroll-driven animations (`::scroll-button()`, `::scroll-marker`, `scroll-timeline`) | 2026-08-16 |
| Speculation Rules API (prefetch/prerender as a UX lever) | 2026-08-16 |
| Agentic UX patterns (planning visibility, progressive delegation, intent preview, action audit) | 2026-08-16 |
| WCAG 3.0 outcome model + component-level a11y assertions in CI | 2026-08-16 |
| Baseline as a build target (browserslist / eslint / stylelint) | 2026-08-16 |

---

## Run 2026-08-16

**Theme of this run: the platform absorbed the libraries.** Four of the five findings are the
same move — behaviour that used to need JavaScript (tooltips, carousels, transitions, instant
navigation) is now declarative, browser-owned, and accessible by default. The fifth is the
other half of the shift: what "accessible" and "trustworthy" now mean when the interface is
driving an agent rather than a form.

### 1. Declarative interactivity — Popover, anchor positioning, invoker commands, interest invokers

The tooltip/dropdown/modal stack is moving into HTML. **Popover API** gives the browser
ownership of open/close, Escape handling, light-dismiss, and focus semantics. **CSS anchor
positioning** tethers an element to any other element regardless of DOM parentage, with
`position-try-fallbacks` for viewport collision — it reached **Baseline Newly available in
January 2026** when Firefox 147 shipped it (Chrome since 125, Safari since 26). **Invoker
commands** (`command` / `commandfor`, Chrome 135+) let a button act on another element with no
JS at all. The experimental **Interest Invoker API** (`interestfor`, Chrome 139 origin trial)
extends that to hover/focus intent — the browser handles `mouseenter`/`mouseleave` and the
dwell timing that hand-rolled tooltips almost always get wrong.

**Why it matters for UX:** these are the components teams most reliably ship broken. Keyboard
dismissal, focus return, and hover-intent delays are exactly the details that get dropped under
deadline, and moving them into the platform makes the accessible version the default rather
than the diligent version. It also deletes a positioning library from the bundle.

**Caveat worth keeping:** better defaults are not automatic correctness — roles, labels, and
focus management still need deliberate choices, and native tools can be misused just as well.

- [Getting Started With The Popover API](https://www.smashingmagazine.com/2026/03/getting-started-popover-api/) — Smashing, 2026-03
- [A First Look at the Interest Invoker API](https://css-tricks.com/a-first-look-at-the-interest-invoker-api-for-hover-triggered-popovers/) — CSS-Tricks
- [Invoker Commands API](https://developer.mozilla.org/docs/Web/API/Invoker_Commands_API) — MDN

### 2. CSS carousels and scroll-driven animation — compositor-thread motion, zero JS

Two pseudo-element families make carousels a CSS-only construct: **`::scroll-button()`** (up to
four browser-generated, stateful, styleable scroll buttons per scroll container) and
**`::scroll-marker` / `::scroll-marker-group`** (per-item markers that behave like anchor links,
so users can jump directly to an item). The browser supplies the keyboard and focus behaviour.

Alongside it, **scroll-driven animations** split into `scroll-timeline` (progress tied to scroll
position — reading indicators, progress bars, parallax) and `view-timeline` (triggered by an
element entering the scrollport — reveal-on-scroll). Animating `transform`/`opacity` this way
runs on the **compositor thread**, the same thread that handles scrolling, so it neither blocks
the main thread nor forces layout recalculation. Support is Chrome/Edge 115+, Firefox 132+,
Safari 18+ — roughly **84% global as of mid-2026**.

**Why it matters for UX:** this replaces GSAP ScrollTrigger, AOS, and the pile of
IntersectionObserver setups behind most reveal effects, which is both a bundle-size win and an
INP win — the two Core Web Vitals failures most tied to janky scroll experiences. And a
carousel is one of the classic accessibility disasters; a native one starts correct.

- [Carousels with CSS](https://developer.chrome.com/blog/carousels-with-css) — Chrome for Developers
- [Creating CSS carousels](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_overflow/CSS_carousels) · [`::scroll-marker`](https://developer.mozilla.org/en-US/docs/Web/CSS/::scroll-marker) · [`::scroll-button()`](https://developer.mozilla.org/en-US/docs/Web/CSS/::scroll-button) — MDN
- [View Transitions API and CSS Scroll-Driven Animations: The Browser Wins of 2026](https://www.frontendhorizon.com/blog/view-transitions-api-and-css-scroll-driven-animations-the-browser-wins-of-2026)

### 3. Speculation Rules API — buying perceived speed without an SPA

A JSON block declares which links to **prefetch** (HTML only) or **prerender** (full page,
scripts executed, rendered offscreen), with eagerness levels controlling how aggressively the
browser acts on hover/pointerdown/viewport signals.

The reported numbers are unusually strong for a single API: prerendered navigations show a
**p75 LCP of ~320ms vs ~1,800ms** for standard navigations on the same sites (~82% better), with
roughly **28% of navigations** successfully speculated at moderate eagerness.

**Why it matters for UX:** it hands a multi-page app the perceived-instant navigation that was
the main experiential argument for going SPA — without the client-side router, the hydration
cost, or the accessibility regressions that come with hijacking navigation. Given that **LCP's
"good" threshold tightened from 2.5s to 2.0s in Google's March 2026 core update**, it is also
one of the few remaining large, cheap wins.

Worth pairing with the INP picture: **43% of sites still fail the 200ms INP threshold**, making
it the most commonly failed Core Web Vital in 2026 — and prerendering does nothing for INP, so
the two need separate work.

- [Speculation Rules API](https://developer.mozilla.org/en-US/docs/Web/API/Speculation_Rules_API) — MDN · [Prerender pages in Chrome](https://developer.chrome.com/docs/web-platform/prerender-pages)
- [Instant Loading Pages with Speculation Rules](https://www.corewebvitals.io/pagespeed/speculation-rules) · [LogRocket test](https://blog.logrocket.com/speculation-rules-api-web-speed-test/)

### 4. Agentic UX — the interface as accountability layer

The most genuinely new *design* material this run, and the least settled. A recurring pattern
vocabulary is forming across independent sources:

- **Planning visibility** — the user sees the intended action sequence *before* execution.
- **Tool-use disclosure** — what the agent reached for, surfaced rather than buried.
- **Progressive delegation** — autonomy expands as approval history accumulates. New users
  confirm every file write; trusted ones auto-approve everything short of a production deploy.
  Trust is *earned through demonstrated reliability* rather than demanded at launch.
- **High-risk action gates / intent preview** — execution pauses before irreversible operations,
  presenting what, why, and consequences, and waits for explicit approval.
- **Action audit** — a retrospective record so errors are diagnosable after the fact.
- **Recovery routing** — clear undo and easy correction, on the premise that trust survives
  errors only when they're recoverable.

The sharpest idea is the anti-pattern: **"agentic sludge"** — removing friction so thoroughly
that users breeze through approvals serving the business rather than themselves. It's a useful
inversion, since UX reflexes say friction is always the enemy, and consent is the case where
it isn't.

**Why it matters:** NN/g's *State of UX 2026* frames trust as the central design problem for AI
experiences — users burned by premature AI features resist the next one, and both over-trust
and under-trust are dangerous. The framing to steal: the interface is the accountability layer
between user intent and autonomous action, designed alongside the model rather than bolted on
after it works.

- [Designing For Agentic AI: Practical UX Patterns For Control, Consent, And Accountability](https://www.smashingmagazine.com/2026/02/designing-agentic-ai-practical-ux-patterns/) — Smashing, 2026-02 (Victor Yocco)
- [Identifying Necessary Transparency Moments In Agentic AI (Part 1)](https://www.smashingmagazine.com/2026/04/identifying-necessary-transparency-moments-agentic-ai-part1/) — Smashing, 2026-04
- [Designing for Autonomy: UX Principles for Agentic AI](https://www.uxmatters.com/mt/archives/2025/12/designing-for-autonomy-ux-principles-for-agentic-ai.php) — UXmatters
- [Secrets of Agentic UX](https://uxmag.com/articles/secrets-of-agentic-ux-emerging-design-patterns-for-human-interaction-with-ai-agents) — UX Magazine

### 5. Accessibility moves from page audits to component assertions

**WCAG 3.0** (Editor's Draft 2026-01-05, Working Draft 2026-02-26) restructures guidance into
**outcome statements, requirements, assertions, and technology-specific methods** — and the
acronym now expands to *W3C Accessibility Guidelines*, covering desktop, mobile, wearables,
IoT, VR/AR rather than web content alone. It is **not expected to reach Recommendation until
~2029**, so this is a direction-of-travel signal, not a compliance deadline.

The actionable part lands sooner: the practical advice is to fix **component defaults** and add
**component-level accessibility assertions to unit and integration tests** — axe via
Jest/Testing Library, Playwright accessibility snapshots — rather than auditing finished pages.

The data argues the same thing. From the 2025 WebAIM Million / Web Almanac: **94.8%** of top-1M
home pages have detectable WCAG 2 A/AA failures; **six issue types account for 96.4%** of all
detected errors (low contrast, missing alt text, missing form labels, empty links, empty
buttons, missing language attribute); low contrast alone rose from 79.1% to **83.9%** of
homepages; **67%** of sites remove focus outlines. Most damning: pages using ARIA averaged **57
errors — more than double** those without it, with ARIA usage up 18.5% year over year. ARIA is
being used to patch inaccessible components after the fact, and it is making things worse.

**Why it matters:** the failure profile is overwhelmingly a small set of *component-level*
defects repeated at scale, which is precisely what a fixed component library plus CI assertions
eliminates and what a page-level audit finds too late. Related and worth tracking: cognitive
accessibility becomes a compliance expectation with **ADA Title II requirements in 2027**, and
the W3C's COGA task force treats *personalization* — user-preference media queries such as
`prefers-reduced-motion`, `prefers-contrast`, `prefers-reduced-transparency` — as the mechanism
rather than a nice-to-have.

- [WCAG 3.0 Working Draft 2026-02-26](https://www.w3.org/TR/2026/WD-wcag-3.0-20260226/) — W3C
- [Accessibility · Web Almanac 2025](https://almanac.httparchive.org/en/2025/accessibility) — HTTP Archive
- [Using media queries for accessibility](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using_for_accessibility) — MDN
- [Cognitive Accessibility in 2026](https://mn.gov/mnit/media/blog/?id=38-742904) — MN IT Services

---

### Tools & frameworks mentioned

- **Baseline as a build target** — the enabler for findings 1–3, and arguably a technique in its
  own right. Browserslist accepts `baseline widely available` (features interoperable across the
  core browser set for 30+ months); ESLint's `use-baseline` rule now targets **Baseline years**,
  not just `newly`/`widely`; **stylelint-browser-compat** flags CSS outside Baseline Widely
  available. Translating a support policy into a Browserslist query drives polyfill strategy,
  so the target choice directly removes shipped code.
  *(2024's JS batch — array grouping, Set methods — is on track for Widely available in late 2026.)*
- **Testing** — axe + Jest/Testing Library, Playwright accessibility snapshots (finding 5).
- **Being displaced** — GSAP ScrollTrigger, AOS, IntersectionObserver reveal setups, tooltip/
  popper positioning libraries, client-side routers used mainly for perceived speed.
- **Design tokens as an AI contract** — *semantic* tokens (`button-primary-background`) over
  literal ones (`blue-500`), so generated UI is constrained by intent. Logged as context rather
  than a finding: the vault already covers tokens, and the sourcing here was weak (see below).

### Cross-reference against prior vault coverage

Checked before writing — all five findings are new to the vault:

- [[How can you make website feel like a native app? (01kmwrzcdkw1059h1f6nry6gjn)]] and
  [[What Makes a WebApp Feel Native? (Insider Secrets) (01kmws0fjds9hrkmmnqj44a29y)]] mention
  View Transitions and popovers in **one line each** ("use the View Transitions API",
  "implement sheets or popovers") — no anchor positioning, invokers, or scroll-driven work.
- Zero prior hits for `scroll-marker`, `scroll-button`, `prerender`, `anchor positioning`,
  `commandfor`, `invoker`, `generative UI`, `progressive delegation`.
- "Speculation rules" appeared only inside an SEO-skill README, never as a UX technique.
- All 13 `WCAG` hits are in AI-design-skill clippings ([[I Built 63 Design Skills For Claude - and They're Free (01kmjvnp1y7sxvqcyz5yg4b4ds)]], [[Top 8 Claude Skills for UI-UX Engineers (01kmjvkfe409s931319nmnrtvg)]]) — WCAG as a
  checklist an AI skill claims to follow, not accessibility technique.
- Existing fundamentals to build on: [[7 Rules for Creating Gorgeous UI (01kn9zv7vjs2fn3r9yksh1xez4)]],
  [[Every UI-UX Concept Explained in Under 10 Minutes (01kna4wk4axs6p6078mytd9pnr)]],
  [[UX UI tips: A guide to creating buttons (01kna3aq4ey3vchmq67ra50t5r)]], [[Inspiration]].

### Sourcing caveat

This environment's egress proxy blocked direct page fetches (smashingmagazine.com,
developer.chrome.com, developer.mozilla.org all refused), so findings come from **search-result
summaries rather than full-text reads**. The technique descriptions and version numbers are
consistent across multiple independent sources and are safe to act on. The **specific
statistics** — the 320ms/1,800ms LCP figures, 28% speculated navigations, 84% scroll-timeline
support, the 40–60% "ship faster" claims that appeared in the design-systems searches — should
be verified against the primary source before being repeated anywhere that matters. Several
2026 "trends" results were SEO content farms recycling each other; those were dropped rather
than logged, which is why generative UI / adaptive interfaces are noted as context above
instead of promoted to a finding.

### Search angles used this run

`scroll-driven animations + view transitions` · `WCAG 3 + browser primitives` ·
`INP / Core Web Vitals 2026` · `design systems + tokens + generative UI` ·
`CSS carousels / invokers` (domain-limited to Chrome/MDN) · `NN/g generative UI research` ·
`Smashing anchor positioning + popover` · `speculation rules real-world results` ·
`agentic AI UX patterns` · `cognitive accessibility + preference media queries` ·
`Baseline tooling` · `Web Almanac 2025 accessibility`.

**Angles to try next run** (deliberately away from the above, since "2026 trends" queries are
now exhausted and return content farms):

- Interop 2026 focus areas — the negotiated list of what browsers commit to fixing is a
  higher-signal predictor than any trends listicle.
- Conference talks over articles: CSS Day, Smashing Conf, An Event Apart successors, Nordic.js
  (the vault already has [[Nordic.js 2025 Tobias Ahlin - Finding Signal in the AI Noise (01krvdzk62fd5kehz6c0gs8zkx)]]).
- Named design-system release notes (GOV.UK, USWDS, Adobe Spectrum 2, Material) — real migration
  writeups instead of trend speculation.
- CHI / UIST 2026 proceedings for interaction techniques 12–18 months ahead of industry.
- Case studies with *numbers* — post-redesign conversion/task-completion deltas — rather than
  pattern catalogues.
- Deliberately underexplored: form UX and error recovery, data-density/enterprise tables,
  offline-first and local-first UX, internationalisation and RTL, motion accessibility,
  voice/multimodal input.
