---
created: 2026-08-23
categories:
  - "[[Resources]]"
domain: design
project: "[[Blog ideas]]"
theme: human-ux-frontend
subtheme:
  - design-systems-ui
tags:
  - agentic-engineering
  - ux-ui
  - design-automation
  - frontend
  - web-design
---

# Design with Agents

Hub for everything in the vault about getting agents to produce frontend that doesn't
look agent-made. Two notes carry the substance and they are deliberately at different
altitudes — read them in this order:

| Note | Altitude | Answers |
|---|---|---|
| [[Designing with Agents — A Working Method]] | Method | *How do I run a design session?* Five stages, what artefact each hands to the next, the 5 → 3 → tweak-bar funnel, the verification gate. |
| [[Frontend and UI-UX Design — Agent Toolkit]] | Inventory | *What exists and which one do I install?* Every skill, plugin and MCP the vault has clipped, with sources, star counts and unverified flags. |

The method note is the spine; the toolkit note is the parts bin it draws from. Neither
repeats the other — if you find yourself needing a tool's detail while reading the
method, that detail lives in the toolkit, and vice versa.

> Everything below is a live view over `domain: design` — see [[Design.base]].

## The pipeline in one screen

1. **Taste** → curated reference library (screenshots + vocabulary + copyable briefs)
2. **Brief** → design brief + tokens + task file, grounded in the library *and* the codebase
3. **Divergence** → five built pages in five aesthetics, side by side
4. **Convergence** → one aesthetic, three layout variants, then a live tweak panel
5. **Verification** → browser screenshots + Lighthouse + a slop checklist, not a gut check

Each stage constrains the next. Skipping one is how "build me a dashboard" turns into
faster chaos.

## Purpose → where to look

| I need… | Go to |
|---|---|
| A direction, from nothing | Method §A + §C — taste library, then 5-way divergence |
| To match a specific site's feel | Method §A — Design Extract, AIDesigner, reference URLs |
| Components rather than pages | Toolkit §5 — 21st.dev, shadcn-ui |
| A repeatable process, not prompts | Method §B — the seven-skill sequence |
| To stop it looking AI-made | Toolkit §1 — Impeccable, taste-skill |
| Proof it actually works | Method §D — Playwright or `chrome-devtools` MCP + Lighthouse |
| Human design fundamentals | Method §E — Kennedy's rules, buttons, native-feel guides |

---

## 📐 Method & toolkit
![[Design.base#📐 Method & toolkit]]

## 🛠 Tools & skills
![[Design.base#🛠 Tools & skills]]

## 🖼 Inspiration
Only **3 clips** so far — the bottleneck for every stage that assumes a taste library.
Full gallery and capture instructions: [[Inspiration]].
![[Design.base#🖼 Inspiration]]

## 🎨 Craft references
![[Design.base#🎨 Craft references]]

## 🔨 To implement
![[Design.base#🔨 To implement]]

## ⭐ Top rated
![[Design.base#⭐ Top rated]]

---

## Properties used here

No bespoke properties — the pair is held together by the vault's existing vocabulary,
so a single filter gathers them and nothing new has to be maintained:

```yaml
categories: ["[[Resources]]"]
domain: design                    # what Design.base filters on
project: "[[Blog ideas]]"         # lands them on that project's desk
theme: human-ux-frontend          # matches the [[Agentic Engineering]] taxonomy
subtheme: [design-systems-ui, …]
tags:
  - agentic-engineering           # 20 notes — the parent cluster
  - ux-ui                         # 45 notes — the settled tag, not `ux` + `ui`
  - design-automation             # 28 notes — what the 📐 view filters on
  - frontend                      # 21 notes
  - web-design                    # 7 notes
```

Add `design-automation` at the vault root to anything new that belongs to this pair and
it joins the 📐 view automatically. Note there is **no `design` tag** in this vault —
design is a `domain:` value, which is what `Design.base` filters on.

## Related
- [[Blog ideas]] — Idea 1 (reducing AI UX/UI slop) is what this material feeds
- [[Netlight]] — the UX/UI audit offer; rubric candidates are in Method §D
- [[Inspiration]] — the taste library, and its capture pipeline
- [[Agentic Engineering]] — this is its `human-ux-frontend` theme, read end to end
- [[AI Transformation]] — open question on where the audit offer sits
