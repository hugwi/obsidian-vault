---
created: 2026-08-23
categories:
  - "[[Resources]]"
domain: design
project: "[[Blog ideas]]"
theme: human-ux-frontend
subtheme:
  - design-systems-ui
  - skill-tool-extension
tags:
  - agentic-engineering
  - ux-ui
  - design-automation
  - frontend
  - web-design
  - skills
  - claude-code
---

# Frontend and UI/UX Design — Agent Toolkit

> Hub: [[Design with Agents]] · method companion: [[Designing with Agents — A Working Method]]

Everything the vault holds on **making agents produce frontend that doesn't look
agent-made**: design skills, the website-imitation tooling, the craft references, and
the review loop. Swept from the whole vault (Raw clippings, project notes,
[[Inspiration]]) rather than one clip.

Attached to [[Blog ideas]] (`project:`) because Idea 1 — *Reducing AI UX/UI slop* — and
the [[Netlight]] UX/UI audit offer are the live projects this material feeds.

> Only [[Blog ideas]] touches design; the other active projects ([[PII]], [[Datahub]],
> [[Ethira]], tprm-lifecycle-roadmap, e2e-deployment-pipeline) are data/platform work
> with no frontend surface. All other evidence below sits in `Raw/`.

---

## 1. Impeccable — the front-end design skill

Source: [[Turn Claude Into A Design GENIUS In 3 Simple Steps]] (step 2).

- `impeccable.style` · open source · ~50k GitHub stars · now packaged as part of
  GitHub's AI tooling. Ships a CLI.
- **One skill, 23 commands** that transform existing UI rather than generate it:
  `bolder` ("pushes safe designs towards impact without sliding into chaos"),
  `overdrive`, `clarify`, plus critique/polish/quieter variants.
- Targets slop across **seven axes**: typography, colour, spatial design,
  responsiveness, interaction, motion, UX writing.
- Catalogues **46 slop patterns**. The CLI scans a codebase against them and renders
  findings on a dev server.
- **Live mode**: bring the site up, click component by component, adjust in place —
  Claude-design-like, but visual instead of terminal-only.
- Install: three options, or paste the URL into Claude Code and let it install.

**Sibling: taste-skill** (v2, experimental, ~66k stars) — same job, different hand:
strips AI tells, pushes layout, typography, motion, spacing. Install
`npx skills add https://github.com/Leonxlnx/taste-skill`
([[Must-Have UXUI Design Skills for Claude Code]]).

The clip's own verdict: Impeccable and taste-skill are the two worth having *because
they are flexible, not prescriptive*. Narrow "build a gorgeous site" skills give one
output shape forever. Both rated above Anthropic's own `frontend-design` and above
`ui-ux-pro-max`.

---

## 2. Imitating a website

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

## 3. Skill landscape

| Skill / collection | Source | What it adds |
|---|---|---|
| **Impeccable** | impeccable.style, ~50k★ | 23 transform commands, 46 slop patterns, CLI + live mode |
| **taste-skill** | Leonxlnx/taste-skill, ~66k★ | Anti-slop layout, type, motion, spacing |
| **frontend-design** (Anthropic) | anthropics/skills · anthropics/claude-code | The official anti-slop brief |
| **web-design-guidelines** (Vercel) | vercel-labs/agent-skills, MIT | 100+ design principles; triggers on "review my UI", "check accessibility" |
| **react-best-practices**, **composition-patterns**, **react-native-skills** | vercel-labs/agent-skills, MIT | Performance, component architecture, mobile |
| **ui-ux-pro-max** | nextlevelbuilder, ~29.6k★, MIT | v2 **Design System Generator** — pattern, style, palette, type pairing, effects, anti-patterns, pre-delivery checklist |
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

**Anthropic `frontend-design` in detail** — bans Inter, Roboto, Arial, system fonts and
Space Grotesk ("overused by AI"); demands four pre-code decisions (purpose, tone,
constraints, differentiation); pushes dominant colour with sharp accents over evenly
distributed palettes, one orchestrated page-load moment over scattered
micro-interactions, and asymmetric/grid-breaking composition.

⚠️ **Supply chain**: Snyk's *ToxicSkills* research found prompt injection in **36% of
skills tested** and 1,467 malicious payloads across the ecosystem. Read `SKILL.md` and
bundled scripts before installing anything above.

---

## 4. Process, not prompts

**Seven skills that encode a real design workflow** —
[[7 Claude Code Design Skills That Follow a Real Design Process]] (29-year designer,
Adobe/IBM/Danone):

1. **Grill Me** — stress-tests requirements before any code. ~20 minutes of decision-tree
   questioning; outputs a grill summary. Adapted from Matt Pocock's skills work.
2. **Design Brief** — reads the codebase for existing components/design system, asks how
   it should *feel*, suggests references (Linear, Google Admin Console).
3. **Information Architecture** — pages, navigation, hierarchy.
4. **Design Tokens** — CSS custom properties for colour, type, spacing, elevation,
   radius. Auto-skipped if a design system already exists.
5. **Brief to Tasks** — dependency-ordered task file: foundation → core UI → responsive → polish.
6. **Frontend Design** — the build, consuming 1–5.
7. **Design Review** — screenshots (manual or Playwright MCP headless) analysed for
   sparse layouts, chart ordering, dark mode, accessibility; proposes and applies fixes.

Result claimed: 91 Lighthouse performance, 100 accessibility, from a one-line prompt.
Framing worth stealing: *"AI is not replacing the tool, it is replacing the process"* —
prompt-and-pray gives you **faster chaos**.

**The build sequence** (design-genius clip, step 3) — deliberately anti-one-shot:

1. Cast wide: **5 versions in 5 aesthetics**, all on one screen to compare.
2. Pick a direction → **3 variants** of it (vary body layout).
3. Pick one → generate hero assets → tweak.
4. Have the agent build a **tweaks bar on the dev server** (fonts, sizes, accent
   colours, motion weight, reveal distance) so iteration is visual, not another prompt.

**The four things every design prompt carries**: aesthetic · reference image or URL ·
intent (what/why/who/desired action) · guardrails (never purple gradients, never Inter).

---

## 5. Taste library — step 1, and the thing that actually differentiates

"AI has no taste." The counter is a **curated inspiration library**: screenshot from
Dribbble, Pinterest, X; group by design type; store vocabulary/keywords per item plus a
copyable image prompt and a copyable brief. Then point the agent at the library instead
of at the average of the web.

This already exists in the vault: [[Inspiration]] + the **Inspiration - Media** Web
Clipper template writing `type: inspiration` clips into `Raw/` (remote URLs only,
rendered by `Templates/Scripts/remote-media`). **Currently 3 clips** — the gap between
that and a working taste library is the single biggest actionable item here.

Component-level inspiration: [[Discover community-made UI components 21st]] (21st.dev —
copy-prompt per component: buttons, cards, pricing, heroes, shaders),
[[React Components, Templates & Themes — 12,000+ Crafted UI]], [[142 JavaScript Text Effects]].

---

## 6. Craft references (human-side, tool-agnostic)

- [[7 Rules for Creating Gorgeous UI]] — Erik Kennedy. Design in black and white first,
  heavy whitespace, lighting model, typography basics. No art background needed.
- [[Every UIUX Concept Explained in Under 10 Minutes]] — affordance via containers,
  colour and hierarchy; consistent spacing; feedback on every interaction.
- [[UX UI tips A guide to creating buttons]] — size, colour, label, and the full state set.
- [[The comprehensive guide to making your web app feel native]] +
  [[What Makes a WebApp Feel Native]] + [[How can you make website feel like a native app]]
  — install flow, update handling, manifest, smart loading, OS design conventions,
  swipe navigation.
- [[Beck Design Rules]] — simple design, applied to code rather than pixels; the
  underlying "minimal elements, clear intent" discipline.
- [[Claude Code Skills, Plugins, and the JSONC Design Spec Trick That Changed My Workflow]]
  — JSONC design spec as the bridge between vague description and pixel-perfect mock,
  without Figma.
- [[system-prompts-and-models-of-ai-toolsLovableAgent Prompt.txt at main · x1xhlolsystem-prompts-and-models-of-ai-tools]]
  — how a production design agent is actually prompted.
- Worked examples clipped as reference UI: [[Hotel Management Dashboard UI Design]],
  [[Landing Page for Yoga Platform]],
  [[Financial Dashboard - B2B Sales Pipeline & Revenue Tracking]], [[Phone Mockups 1]].

---

## 7. Seeing the result — the review loop

Design skills without a feedback loop just move the slop around. What the vault has:

- **Playwright MCP + design-review skill** — headless browse, screenshot every page,
  review autonomously (skill 7 above).
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

Also in the vault: [[Claude Code Just Killed $10,000 Websites (Here’s Proof)]] — the
four-step hype version (Claude Code + framer-motion + ui-ux-pro-max + 21st.dev). Kept as
an artefact of the genre, not as guidance.

---

## 8. Where this lands

- **[[Blog ideas]] Idea 1** — the anti-slop tooling above *is* the constructive half of
  that post. Impeccable's 46 slop patterns and 7 axes are a ready-made checklist to hand
  readers; the ui-ux-pro-max anti-pattern list ("no AI purple/pink gradients, no harsh
  animations, no emojis as icons") is a second, independent one. The gen-3 motion thesis
  is directly testable against `ui-animation` and Impeccable's motion axis.
- **[[Netlight]] UX/UI audits** — an audit needs a rubric. Candidate rubric = Impeccable's
  7 axes + Vercel's 100+ guidelines + AccessLint contrast/colour/link checks + the
  pre-delivery checklist (contrast 4.5:1, visible focus, `prefers-reduced-motion`,
  breakpoints at 375/768/1024/1440). Positioning still open vs. [[AI Transformation]].
- **[[Agentic Engineering]]** — this is the `theme: human-ux-frontend` slice, read
  end-to-end instead of one clip at a time.

## Open questions
- [ ] Find the real **Design Extract** repository and verify what it emits.
- [ ] Has **AIDesigner** shipped `clone`/`inspire`/`enhance` modes, or still "coming soon"?
- [ ] Impeccable vs. taste-skill — install both and run them on the same page, since
      every clip compares them side by side and none of them concludes.
- [ ] Grow [[Inspiration]] past 3 clips before any of this pays off.
- [ ] Audit any installed design skill against the ToxicSkills finding before use.
