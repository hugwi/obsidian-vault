---
created: 2026-08-23
categories:
  - "[[Resources]]"
project: "[[Blog ideas]]"
theme: human-ux-frontend
subtheme:
  - design-systems-ui
tags:
  - ux-ui
  - design-automation
  - frontend
  - web-design
domain:
  - design
type: note
---

# Design

Everything design in this vault lives under one property — `domain: design` — so it is
one search, not five. Three subpages carry the substance; the table at the bottom is the
live index of every note that carries the domain.

| Subpage | What it holds |
|---|---|
| [[AI Design]] | The cross-section: design × agents. The method, the skills, the review loop. |
| [[Design Fundamentals]] | Human craft, tool-agnostic. Kennedy's rules, buttons, native feel. |
| [[Inspiration]] | The taste library — every `type: inspiration` clip, with its gallery. |

## Blogs

[[Blog ideas]] — Idea 1, *reducing AI UX/UI slop*, is what this material feeds. Every
design note in the vault carries `project: "[[Blog ideas]]"` or shows up on its desk.

## Projects

Only [[Blog ideas]] and the [[Netlight]] UX/UI audit offer touch design. The other
active projects ([[PII]], [[Datahub]], [[Ethira]], tprm-lifecycle-roadmap,
e2e-deployment-pipeline) are data and platform work with no frontend surface.

- **[[Blog ideas]]** — the anti-slop post. [[AI Design]] §10 is its constructive half.
- **[[Netlight]]** — the audit offer. Needs a rubric; candidates are in [[AI Design]] §4
  and all of [[Design Fundamentals]]. Positioning still open vs. [[AI Transformation]].

## Design Fundamentals

[[Design Fundamentals]] — the human-side judgment the tools are trying to encode. Light
comes from the sky, design in black and white first, double the whitespace, every
interaction gets a response state. Read it once; it is what makes a review a reason
rather than a vibe.

## Everything with `domain: design`

Sorted by rating, then publish date, then the date it landed in the vault. **Rating is
blank until you set it** — unrated notes sink to the bottom by date rather than
pretending to a score. `published` is filled only where the source exposes it (YouTube
does; Medium, Dribbble, 21st.dev and GitHub do not).

![[Design.base#All design]]

## Inspiration

[[Inspiration]] — the taste library, its gallery, and the capture pipeline. Every stage
of [[AI Design]] assumes this exists with real coverage, which makes growing it the
single most actionable item in the whole cluster.

---

## Properties used here

```yaml
domain: design          # the only thing Design.base filters on
type:                   # article | video | skill | tool | inspiration | note
rating:                 # 1–7, yours to set
published:              # source publish date where the site exposes it
stars:                  # GitHub stars, for repo notes
```

There is **no `design` tag** — design is a `domain:` value. Add `design` to any new
note's `domain` list and it joins the table automatically, keeping whatever other
domains it already has.
