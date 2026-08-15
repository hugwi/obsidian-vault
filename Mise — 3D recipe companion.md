---
created: 2026-08-15
categories:
  - "[[Projects]]"
project: "[[Mise — 3D recipe companion]]"
status: active
outcome: Shipped a 3D recipe app with a chat companion, built with the impeccable design language
due: 2026-09-15
tags:
  - design-automation
  - agentic-engineering
  - three-js
  - remotion
---

A recipe app built as a test of [[impeccable]] — Paul Bakaus's design-language
skill — driving real production work rather than a toy page. Lives in
`apps/mise/` in this vault.

## The idea

Streaming-service browsing (one dish held at centre, a shelf you travel along, a
billboard naming it) with an Apple-style glass shell over a live 3D kitchen, and
a companion panel that is not a search box: every reply re-forms the shelf behind
the glass, so the conversation and the room are the same thing.

## Stack

- **three.js / react-three-fiber** — the arc carousel and a generative plating
  system. No photography: each recipe describes its dish as edible forms (sauce
  pooled under, a mound, wedges laid down, capers scattered) and the plating code
  builds that into geometry on a golden-angle spiral, seeded off the recipe id.
- **Remotion** — the method reel is a real composition, mounted through `<Player>`
  in cook mode and registered for the CLI, so the panel and the exported MP4 run
  the same timeline.
- **Local companion engine** — deterministic, offline, with a one-interface seam
  (`CompanionEngine`) to drop a real model in behind it.

## What impeccable actually changed

Reading `craft-floor.md` and `animate.md` before building, not after, is what
produced: one ember accent reserved for action and selection instead of a palette;
tabular figures on everything measured; themed selection, caret, scrollbar and
focus ring; a drawn icon set instead of emoji; and one authored motion moment
rather than an entrance on every element.

The rule that earned its keep was *"keep content visible in the default state so
failed scripts do not hide the page."* A full-viewport WebGL canvas turned out to
starve compositor animations, `requestAnimationFrame` callbacks and
View-Transition captures — all three stalled indefinitely — which silently hid
the headline, blanked the companion's replies, and made the primary button do
nothing. Every one of those was an entrance or a transition that owned its
content instead of decorating it. Worth remembering as a general pattern, not a
three.js quirk.

Its bans also cut against the brief in one place: glass-as-decoration is on the
refuse list, but the brief pinned it and impeccable's own rule is that the brief
wins. So glass became the app's material rather than its finish — specular lip,
saturation lift, warm bounce, a caustic only on the focused pane.

## Next

- [ ] Swap the local engine for a real model behind the same interface
- [ ] Timers on steps that have a duration, so cook mode can count down
- [ ] A second reel composition: the shelf as a trailer, for the billboard
- [ ] Try `/impeccable critique` against the built app and see what it flags

## Related

- [[Inspiration]] · [[Agentic Engineering]]
- Design write-up: `apps/mise/DESIGN.md` · setup: `apps/mise/README.md`

```dataviewjs
await dv.view("Templates/Scripts/project-desk")
```
