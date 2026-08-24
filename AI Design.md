---
created: 2026-08-23
categories:
  - "[[Resources]]"
project: "[[Blog ideas]]"
theme: human-ux-frontend
subtheme:
  - design-systems-ui
  - skill-tool-extension
  - browser-automation
tags:
  - agentic-engineering
  - ux-ui
  - design-automation
  - frontend
  - web-design
  - skills
  - claude-code
  - workflow
domain:
  - agentic-engineering
  - design
type: note
---

# AI Design

> Hub: [[Design]] · human-side craft: [[Design Fundamentals]] · taste library: [[Inspiration]]

The cross-section: **design × agents**. How to get an agent to produce frontend that
doesn't look agent-made — the method, and the inventory of tools it draws on. Written
for [[Blog ideas]] Idea 1 (reducing AI UX/UI slop) and the [[Netlight]] UX/UI audit
offer; it is [[Agentic Engineering]]'s `human-ux-frontend` theme read end to end.

Anything tool-agnostic — Kennedy's rules, button anatomy, native-feel guides — lives in
[[Design Fundamentals]] instead.

---

## 0. The two source articles

Almost everything below traces back to these two. Read them first; both are unpacked
step by step in §2 and §4.

**[[7 Claude Code Design Skills That Follow a Real Design Process]]** — Julian
Oczkowski, 29 years across Adobe/IBM/Danone as IC, design manager and dev team lead.
Readwise clip, 2026-06-23. **A process**: seven sequential Claude Code skills
(`npx skills add julianoczkowski/designer-skills`), Grill Me through Design Review.
The line worth stealing whole: *AI is not replacing the tool, it is replacing the
process* — prompt-and-pray gives you **faster chaos**.

**[[Turn Claude Into A Design GENIUS In 3 Simple Steps]]** — `@devanshsharma6865`,
YouTube transcript, 2026-07-23. **A taste-and-iteration loop**: cultivate a personal
taste library → pick flexible skills and MCPs (where Impeccable comes from, §5) → run
the anti-one-shot 5 → 3 → tweak-bar sequence. Its diagnosis is the sharper one — the
failure is not technical, it is *generic*.

### Why both, and where they disagree

They are not two versions of the same advice, and the gap between them is the point.

| | 7 skills | 3 steps |
|---|---|---|
| Shape | Sequential gates, one path | Parallel variants, then converge |
| Fixes slop by | Removing the freedom to invent | Supplying taste worth imitating |
| Weak spot | Nothing supplies the taste the brief asks for | No requirements gate before building |
| Design review | Step 7, automated via Playwright MCP | The tweak bar, human-driven |

Each covers the other's gap, which is why the method below merges them instead of
picking one: the seven-step spine (§2), with the 5 → 3 → tweak funnel dropped in where
the build step sits (§3).

---

# Part I — The method

## The spine

Five stages, each handing a concrete artefact to the next. Skip a stage and the next one
has nothing to constrain it — which is exactly how "prompt and pray" happens.

1. **Taste** → a curated reference library (screenshots + vocabulary + copyable prompts/briefs)
2. **Brief** → a design brief + tokens + task file, grounded in the taste library and the actual codebase
3. **Divergence** → five built pages in five aesthetics, side by side
4. **Convergence** → one aesthetic, three layout variants, then a live tweak panel
5. **Verification** → Playwright screenshots + Lighthouse scores + a slop checklist, not a gut check

The throughline: **each stage constrains the next so the build step executes decisions
instead of inventing them.** That's the difference between this and "build me a
dashboard" — same model, same skills even, radically different output because the
inputs to the build step are no longer empty.

---

## 1. Stage 1 — Taste: two different mechanisms, don't conflate them

**Extraction from a live site** pulls a specific site's DNA into a report you build
from. Two tools clipped, both with open questions:

- **Design Extract** (Claude Code plugin) — [[3 New Claude Code Repos Will 100x Your Next Project]].
  Pulls components in use, **motion language** (the clip's claim: it's the only tool that
  extracts scroll-driven animation behaviour), brand voice, responsive behaviour, and
  interaction states (hover/focus/active), output as a full report rather than a code
  dump. **UNVERIFIED** — the source is a YouTube Short that never gives the repo URL;
  confirm the actual repository before installing anything.
- **AIDesigner** (aidesigner.ai) — [[AIDesigner]]. MCP + agent-skills package
  (`npx -y @aidesigner/agent-skills init`; hosts: Claude Code, Cursor, Codex, VS
  Code/Copilot, Windsurf). `generate_design`/`refine_design` take a `mode` of
  `inspire | clone | enhance` plus a required `url`, but the docs mark reference modes
  **"coming soon"** — treat as unverified whether they shipped.

**Curated browsing / component libraries** is lower-fidelity and lower-risk — you're
collecting, not extracting:

- **Dribbble, Pinterest, X/Twitter** for whole-page aesthetics — search "web design",
  screenshot or save links to whatever reads as good ([[Turn Claude Into A Design GENIUS In 3 Simple Steps]]).
- **21st.dev** for component-level inspiration — buttons, cards, pricing sections,
  heroes, shaders. Each component has a **copy-prompt button** that pastes straight into
  Claude Code ([[Discover community-made UI components 21st]]).

**The vault's own taste library already exists and is the bottleneck.** The
"Inspiration - Media" Web Clipper template writes `type: inspiration` clips into `Raw/`
(remote URLs only, rendered by `Templates/Scripts/remote-media`), feeding [[Inspiration]].
Every later stage in this pipeline assumes a taste library with real coverage —
divergence needs multiple aesthetic families to draw from, convergence needs reference
images to match a feel against. This is the single most actionable gap in the whole
method.

**The taste-library-as-app idea** (from the design-genius clip, step 1): don't just
collect screenshots — build a small app around them. Group by design type, store the
design vocabulary/keywords per item, and attach two copyable artefacts to each: an
**image prompt** (for hero/asset generation) and a **brief** (for building the page).
Then point the agent at *your library* instead of letting it default to the average of
the public web — which is where generic AI-slop aesthetics come from in the first place.

**Reference vs. replication — the line that matters for the blog post.** Matching a
*feel* — "take a look at the formatting of that website, Claude can see it, apply that
formatting to my page" — is craft; it's literally what the design-genius clip endorses,
applied to body layout as much as heroes. Extract-and-rebuild (Design Extract's whole
value proposition) is the *same mechanism* that manufactures gen-2 AI slop at scale, and
only the intent separates the two uses. Worth saying plainly: none of these tools reach
server-side logic — they operate on the presentation layer only, so "extraction" here
never means cloning a product's actual functionality, only its surface.

---

## 2. Stage 2 — The seven-skill design process

Source: [[7 Claude Code Design Skills That Follow a Real Design Process]]. His framing,
worth stealing whole: **AI is not replacing the tool, it is replacing the process** —
and skipping straight to "type a prompt, watch code appear" is how you get **faster
chaos**. These seven Claude Code skills (`npx skills add
julianoczkowski/designer-skills`) encode a professional design process end to end.

1. **Grill Me** — relentless requirements interrogation before any code is written,
   ~20 minutes, decision trees that probe deeper based on your answers (app type, users,
   scale, edge cases). Output: a **grill summary** — the requirements handshake between
   you and the LLM. Credited to Matt Pocock's skills work (`github.com/mattpocock/skills`).
2. **Design Brief** — reads the actual codebase for existing components, design system,
   patterns already in the repo; asks how the thing should *feel* (emotional tone,
   visual inspiration), sometimes suggesting references like Linear or the Google Admin
   Console. Output: a design brief document saved into the project.
3. **Information Architecture** — pages, navigation patterns, content hierarchy; asks
   more clarifying questions if the flow is complex (multi-page, full nav redesign).
4. **Design Tokens** — CSS custom properties for colour, typography, spacing, elevation,
   border radius, saved to a theme file the frontend skill consumes later. **Auto-skipped**
   if step 2 already detected an existing design system.
5. **Brief to Tasks** — reads everything generated so far, identifies dependencies, and
   writes a task file tracking status per task: foundation → core UI → responsive → polish.
6. **Frontend Design** — the build. Consumes 1–5. Not random code — code that follows
   the decisions already made.
7. **Design Review** — screenshots analysed, either pasted manually or captured
   automatically via a **Playwright MCP server**: headless browser opens, navigates every
   page, screenshots each one, then the review skill runs against those screenshots
   autonomously. Catches sparse layouts, wrong chart ordering, missing dark mode,
   accessibility gaps — and can propose *and apply* fixes.

**Reported result:** from "I want an asset management application" to a working tool
(dashboard, asset tracking, categories, reports, filtering, sorting, empty states, edit
dialogs, navigation) scoring **91 Lighthouse performance / 100 Lighthouse accessibility**.

**Why the order works:** each step narrows what the next step is allowed to invent. Grill
Me fixes the requirements so the brief isn't guessing at users. The brief fixes the feel
and inventory of existing components so tokens aren't guessing at a palette from
scratch. Tokens fix the vocabulary so the task list isn't guessing at what "polish" means.
The task list fixes the sequence so the build isn't guessing at what to do first. By the
time step 6 runs, it's executing a chain of decisions, not making them — which is the
actual difference between this and "build me a dashboard."

---

## 3. Stage 3+4 — The 5 → 3 → tweak bar sequence

Source: [[Turn Claude Into A Design GENIUS In 3 Simple Steps]], step 3. This is the
deliberately anti-one-shot funnel: you cannot judge a design direction from a single
terminal output, so the method forces comparison before commitment.

**5 — cast wide.** Ask for five versions of the same page in five *different aesthetic
families* at once, rendered so all five are visible on one screen simultaneously. The
clip's own example (a fake AI company, "Kestrel"): "print-tech paper", "vast quiet"
(minimal, cinematic), "dither mono", "classical remix" — plus a fifth. The point isn't
the specific families, it's that comparison makes taste legible in a way that iterating
one output at a time in a terminal never does.

**3 — narrow to one aesthetic, vary the layout.** Pick a direction (the clip picked
"vast quiet"), then ask for three variants *of that aesthetic*, explicitly varying the
body layout. What came back: the original vertical-minimal, a fuller body, a "ledger"
version with a scroll-following left index, and "frames" with section edging around each
block. Pick one (the clip picked the ledger).

**Tweak bar — stop asking for more versions, start looking.** Once a direction is
locked, have the agent build a **controls panel into the dev server itself** — heading
font, font size, accent colours, hero imagery, motion weight, reveal distance: anything
that is an aesthetic decision becomes a live control instead of another prompt. Explicitly
modelled on Claude design's tweaks panel. The rationale, in the clip's own words: you
don't know in advance which font will look good, so don't sit there asking the agent for
ten more full-page regenerations — put the decision in a panel and just look at it change.

**Asset generation slots in after the direction is locked, not before.** The clip used
the Higgsfield MCP for hero imagery: generate 4 hero images → pick one → generate
recolour variants of that one → pick "alpenglow." Generating assets before a direction is
chosen wastes the generation on a direction you might not keep.

**The four things every design prompt carries**, regardless of stage:
1. **Aesthetic** — the general design family being targeted.
2. **Reference image or live URL** — pulled from the taste library; match the *feel*,
   never the content (this is the reference/replication line from §1 again).
3. **Intent** — what is this, who is it for, what should they do (read everything and
   leave? click through? fill a form?).
4. **Guardrails** — the never-list: no purple gradients, no Inter, no 3D SaaS blobs, etc.

**The warning about the skill rabbit hole.** Highly prescriptive "build a gorgeous site"
skills give one output shape forever — impressive in a demo, useless once you want
something different. The clip rates Impeccable and taste-skill above the narrower
skills, above Anthropic's own `frontend-design`, and above `ui-ux-pro-max`, *specifically
because they're not prescriptive*. The trade-off is real, though: being flexible means
output quality falls back entirely on your prompting and your taste library — the tool
won't compensate for either being thin. Full writeup in §5.

---

## 4. Stage 5 — Verification and best practices

Design skills without a feedback loop just relocate the slop. Verification closes the
loop with something other than a vibe check.

**The review loop.** Playwright MCP headless browser opens the app, navigates every
page, screenshots each, then the design-review skill runs against the screenshots
autonomously (step 7 of §2) — catching sparse layouts, wrong ordering, missing dark
mode, accessibility gaps, and proposing/applying fixes. **Lighthouse** is the numeric
gate on top of that: the seven-skill process reported 91 performance / 100
accessibility as the target range.

**Playwright is not the only way to run this loop.** The `chrome-devtools` MCP server
(bundled as a Claude Code plugin) drives a real Chrome and covers the same review pass
without a separate Playwright install:

| Check | Tool call |
|---|---|
| Open the page, reload, back/forward | `navigate_page` |
| Screenshot, full-page or one element, saved to disk | `take_screenshot` |
| Breakpoints 375 / 768 / 1024 / 1440 | `resize_page` |
| Mobile, touch, DPR, landscape | `emulate` → `viewport: "375x812x3,mobile,touch"` |
| Dark mode | `emulate` → `colorScheme: dark` |
| Slow device / slow network | `emulate` → `cpuThrottlingRate`, `networkConditions` |
| Accessibility tree + element ids | `take_snapshot` |
| Drive a flow | `click`, `hover`, `fill_form`, `press_key`, `drag`, `wait_for` |
| Runtime errors | `list_console_messages`, `list_network_requests` |
| Accessibility / SEO / best-practices score | `lighthouse_audit` |
| Performance score and trace | `performance_start_trace` → `performance_stop_trace` → `performance_analyze_insight` |

> ⚠️ **Correction to the seven-skill numbers**: `lighthouse_audit` covers accessibility,
> SEO, best practices and agentic browsing — **not performance**. The 100-accessibility
> figure is one call; the 91-performance figure needs the trace tools instead. Two gates,
> not one.

**Motion cannot be verified from screenshots** — the one real gap in a screenshot-based
review, and the exact axis where gen-3 slop lives (see [[Blog ideas]] Idea 1). Screen
recording is the only honest check: capture the scroll, then watch whether the effect
*complements* the user's scroll or *takes it over*. Also assert `prefers-reduced-motion`
is respected by emulating it, rather than trusting that the CSS is there.

**The pre-delivery checklist**, from the ui-ux-pro-max skill
([[nextlevelbuilderui-ux-pro-max-skill An AI SKILL that provide design intelligence for building professional UIUX multiple platforms]]) —
worth adopting verbatim as a house gate regardless of which skill built the page:

- No emojis as icons — use SVG (Heroicons/Lucide)
- `cursor-pointer` on all clickable elements
- Hover states with 150–300ms transitions
- Light-mode text contrast ≥ 4.5:1
- Visible focus states for keyboard navigation
- `prefers-reduced-motion` respected
- Responsive at 375 / 768 / 1024 / 1440

**Other ways to see the result:**

- [[web-infra-devmidscene AI-powered, vision-driven UI automation for every platform.]] —
  vision-driven UI automation across platforms.
- [[browser-usebrowser-use 🌐 Make websites accessible for AI agents. Automate tasks online with ease.]]
- [[Automating e2e manual labor with Claude Code]] — plain-English E2E; good for complex
  flows, slower and costlier than traditional runners.
- [[firstloophqclaude-code-test-runner An automated E2E natural language test runner built on Claude Code]]
- [[Introducing visual-plan - rich plans for Claude Code + Codex]] — interactive visual
  plans and PR recaps; catches design mistakes before the build.
- [[Agents on the Canvas in tldraw — Steve Ruiz, tldraw]] — agents working on a canvas
  rather than in text.
- [[penpotpenpot Penpot The open-source design tool for design and code collaboration]] —
  open-source design/code collaboration if a real design file is ever needed.

---

# Part II — The toolkit

## 5. Impeccable — the front-end design skill

Source: [[Turn Claude Into A Design GENIUS In 3 Simple Steps]] (step 2).

- `impeccable.style` · open source (Apache-2.0) · `pbakaus/impeccable`. Ships a CLI.
  > **Verified against the installed package, 2026-08-24** — the clip's figures have
  > aged. Now **61.9k stars**, version **4.1.1**, and **59** detector rules rather than
  > the 46 slop patterns the clip quotes. The 23 commands and seven axes still hold.
  > Install: `npx impeccable install` (needs Node ≥ 22.12), then `/impeccable init`.
- **One skill, 23 commands** that transform existing UI rather than generate it:
  `bolder` ("pushes safe designs towards impact without sliding into chaos"),
  `overdrive`, `clarify`, plus critique/polish/quieter variants.
- Targets slop across **seven axes**: typography, colour, spatial design,
  responsiveness, interaction, motion, UX writing.
- The CLI scans a codebase against the detector rules and renders findings on a dev
  server. Exit code `2` when findings exist, `0` when clean — so it works as a gate.
- **Live mode**: bring the site up, click component by component, adjust in place —
  Claude-design-like, but visual instead of terminal-only.

It belongs at *verification* rather than build time: it is a transform over existing UI,
not a generator.

**Sibling: taste-skill** (v2, experimental, ~66k stars) — same job, different hand:
strips AI tells, pushes layout, typography, motion, spacing. Install
`npx skills add https://github.com/Leonxlnx/taste-skill`
([[Must-Have UXUI Design Skills for Claude Code]]).

The clip's own verdict: Impeccable and taste-skill are the two worth having *because
they are flexible, not prescriptive*. Both rated above Anthropic's own `frontend-design`
and above `ui-ux-pro-max`.

---

## 6. Imitating a website

Three different mechanisms in the vault, in decreasing order of fidelity:

**Design Extract** (Claude Code plugin) — [[3 New Claude Code Repos Will 100x Your Next Project]].
The strongest evidence for "imitate any site". It pulls from a target URL:

- components in use and how to rebuild them
- **motion language** — the scroll-driven animation behaviour, which the clip claims
  no other tool extracts
- brand voice, responsive behaviour, interaction states (hover / focus / active)
- output is a full report you build from, not a code dump

*Unverified:* the clip is a YouTube Short and never gives the repo URL. Confirm the
actual repository before installing.

**AIDesigner reference modes** — [[AIDesigner]]. MCP + agent-skills package
(`npx -y @aidesigner/agent-skills init`, hosts: Claude Code default, Cursor, Codex).
Takes a `mode` of `inspire` | `clone` | `enhance` with a required `url`, via MCP param
or `--mode`/`--url` on the CLI. Marked *coming soon* in the clipped docs — check
whether it shipped.

**Reference-by-prompt** — the low-tech version, and the one the design-genius clip
actually endorses: drop screenshots *and live URLs* into the prompt and ask to match
the **feel**, not the content. Explicitly framed as not copying. Applies to body
layout as much as heroes — "Claude can see it, apply that formatting to my page."

> Positioning note for [[Blog ideas]]: extract-and-rebuild is exactly the mechanism
> that manufactures gen-2 slop at scale. The interesting essay line is *reference vs.
> replication* — same tool, and only the intent differs.

---

## 7. Skill landscape

| Skill / collection | Source | What it adds |
|---|---|---|
| **Impeccable** | impeccable.style, 61.9k★ | 23 transform commands, 59 detector rules, CLI + live mode |
| **taste-skill** | Leonxlnx/taste-skill, ~66k★ | Anti-slop layout, type, motion, spacing |
| **frontend-design** (Anthropic) | anthropics/skills · anthropics/claude-code | The official anti-slop brief |
| **web-design-guidelines** (Vercel) | vercel-labs/agent-skills, MIT | 100+ design principles; triggers on "review my UI", "check accessibility" |
| **react-best-practices**, **composition-patterns**, **react-native-skills** | vercel-labs/agent-skills, MIT | Performance, component architecture, mobile |
| **ui-ux-pro-max** | nextlevelbuilder, MIT | v2 **Design System Generator** — pattern, style, palette, type pairing, effects, anti-patterns, pre-delivery checklist |
| **Designer Skills Collection** | Owl-Listener/designer-skills, MIT | **63 skills + 27 commands in 8 plugins**: research, systems, strategy, UI, interaction, prototyping/testing, design ops, toolkit |
| **bencium UX designer** | bencium/…-design-skill | Two SKILL.md files: controlled + innovative UX designer |
| **AccessLint plugin** | accesslint/claude-marketplace, MIT | `contrast-checker`, `refactor`, `use-of-color`, `link-purpose` |
| **shadcn-ui** | developer-kit@shadcn-ui | Component-library fluency (Radix + Tailwind) |
| **ui-animation** | — | Motion, easing, timing, reduced-motion, framer-motion, springs |
| **AIDesigner** | aidesigner.ai | MCP: generate / refine / preview UI in-repo, stack-aware |
| **Open Design** | Next.js 16 app, self-hosted | Open-source Claude-design alternative |

Refs: [[Top 8 Claude Skills for UIUX Engineers]] ·
[[Must-Have UXUI Design Skills for Claude Code]] ·
[[I Built 63 Design Skills For Claude - and They're Free]] ·
[[nextlevelbuilderui-ux-pro-max-skill An AI SKILL that provide design intelligence for building professional UIUX multiple platforms]] ·
[[Open Design is Here The Open-Source Claude Code Design Alternative]] ·
[[AIDesigner]]

**Anthropic `frontend-design` conventions worth adopting as house rules**, independent
of whether that specific skill built the page:
- Banned fonts: Inter, Roboto, Arial, system fonts, Space Grotesk ("overused by AI")
- Four pre-code decisions: purpose, tone, constraints, differentiation
- Dominant colour with sharp accents beats an evenly distributed, timid palette
- One orchestrated page-load moment beats scattered micro-interactions
- Asymmetric, grid-breaking composition over safe centred layouts

⚠️ **Supply chain.** Snyk's *ToxicSkills* research found prompt injection in **36% of
skills tested** and **1,467 malicious payloads** across the ecosystem. Read `SKILL.md`
and any bundled scripts before installing — this applies as much to Grill Me / Design
Extract / ui-ux-pro-max as to anything unfamiliar. See
[[Top 8 Claude Skills for UIUX Engineers]] for the fuller install-hygiene checklist
(check the source, review `allowed-tools`, scan with Snyk if available).

---

## 8. Taste library — the thing that actually differentiates

"AI has no taste." The counter is a **curated inspiration library**: screenshot from
Dribbble, Pinterest, X; group by design type; store vocabulary/keywords per item plus a
copyable image prompt and a copyable brief. Then point the agent at the library instead
of at the average of the web.

This already exists in the vault: [[Inspiration]] + the **Inspiration - Media** Web
Clipper template writing `type: inspiration` clips into `Raw/` (remote URLs only,
rendered by `Templates/Scripts/remote-media`).

Component-level inspiration: [[Discover community-made UI components 21st]] (21st.dev —
copy-prompt per component: buttons, cards, pricing, heroes, shaders),
[[React Components, Templates & Themes — 12,000+ Crafted UI]], [[142 JavaScript Text Effects]].

Also in the vault: [[Claude Code Just Killed $10,000 Websites (Here’s Proof)]] — the
four-step hype version (Claude Code + framer-motion + ui-ux-pro-max + 21st.dev). Kept as
an artefact of the genre, not as guidance.

---

## 9. One recipe for tomorrow

1. **Grow the taste library first**, or the rest is theatre. Screenshot from Dribbble /
   Pinterest / X, group by type, note vocabulary, generate a copyable prompt + brief per
   item (§1). If you have a specific site to match, run it through Design Extract or
   drop the URL directly into the prompt (§6) — verify Design Extract's repo first.
2. **Run Grill Me → Design Brief → IA → Tokens → Brief-to-Tasks** before any component
   gets built (§2, 1–5). This is the artefact set that makes step 3 possible.
3. **Diverge**: five aesthetics, one screen, compare (§3). Pick one.
4. **Converge**: three layout variants of the winner, pick one, then build a tweak bar
   into the dev server for fonts/colour/motion/imagery instead of re-prompting (§3).
   Generate hero/asset imagery only now that the direction is locked.
5. **Build** (§2, step 6) — the skill has a brief, tokens, IA, and a task list to
   execute against.
6. **Verify**: screenshot review + Lighthouse (§4), then a slop pass with Impeccable or
   taste-skill and the pre-delivery checklist (§4, §5).

| Need | Reach for |
|---|---|
| A direction, from nothing | Taste library (§1) + 5-way divergence (§3) |
| To match one specific site's feel | Design Extract or drop the live URL/screenshot into the prompt (§6) |
| Components (buttons, cards, pricing, heroes) | 21st.dev copy-prompt, shadcn-ui |
| It to stop looking AI-made | Impeccable or taste-skill as a transform pass (§5) |
| A design system from a one-line brief | ui-ux-pro-max Design System Generator (§7) |
| Proof, not vibes | Playwright *or* `chrome-devtools` MCP + Lighthouse + perf trace + the pre-delivery checklist (§4) |
| Human design fundamentals | [[Design Fundamentals]] |

---

## 10. Where this lands

- **[[Blog ideas]] Idea 1** — the anti-slop tooling above *is* the constructive half of
  that post. Impeccable's detector rules and seven axes are a ready-made checklist to
  hand readers; the ui-ux-pro-max anti-pattern list ("no AI purple/pink gradients, no
  harsh animations, no emojis as icons") is a second, independent one. The gen-3 motion
  thesis is directly testable against `ui-animation` and Impeccable's motion axis.
- **[[Netlight]] UX/UI audits** — an audit needs a rubric. Candidate rubric = Impeccable's
  7 axes + Vercel's 100+ guidelines + AccessLint contrast/colour/link checks + the
  pre-delivery checklist (contrast 4.5:1, visible focus, `prefers-reduced-motion`,
  breakpoints at 375/768/1024/1440). Positioning still open vs. [[AI Transformation]].
- **[[Agentic Engineering]]** — this is the `theme: human-ux-frontend` slice, read
  end-to-end instead of one clip at a time.

## Open questions

- [ ] **Design Extract**'s actual repository is unverified — the only source is a
      YouTube Short with no URL given. Find it and confirm what the report format
      actually contains before treating the motion-language claim as fact.
- [ ] **AIDesigner**'s `inspire`/`clone`/`enhance` reference modes are marked "coming
      soon" in the clipped docs — check whether they've shipped.
- [ ] **Impeccable vs. taste-skill** — every clip compares them side by side and none
      concludes. Install both, run them on the same page, decide.
- [ ] Grow [[Inspiration]] before judging whether any of the rest of this pays off —
      every stage assumes a real taste library exists.
- [ ] Audit any skill named here against the ToxicSkills findings (36% prompt-injection
      rate in the tested set) before installing, not after.
