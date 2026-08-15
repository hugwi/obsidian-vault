# Mise — design

Built with [impeccable](https://github.com/pbakaus/impeccable) as the working
design language. Mode is split by surface: browse is **Experience** (the dish
leads from the first viewport, the interface recedes), cook is **Operate** (you
are at a stove with wet hands, scanability outranks expression).

## The world

**A night kitchen seen through glass.** Warm near-black ground, a single ember
accent, and a shell of lenses floating in front of a live 3D kitchen.

The brief pinned an Apple-style glass feel, and the brief wins — but glass here
had to earn its place rather than arrive as decoration. So it is the app's
material, not its finish: every panel is a lens in front of the scene, and its
thickness says how far in front. What separates a lens from a translucent
rectangle is the specular lip along the top edge, the saturation lift, the warm
bounce off the surface below, and a slow caustic band that crosses only the
focused pane. A bare `backdrop-filter: blur()` reads as fog, and that is exactly
the version this world had to beat.

Where long copy sits on a pane, the material takes an opaque ground first
(`.glass--dense`). A dish passing behind a 40px blur still moves the backdrop
enough to drop body text under 4.5:1, and legibility outranks the view.

## Colour

Ground `#0a0907` — warm near-black, never `#000`, because the scene supplies the
light and the render has to sit inside the page rather than on it.

One accent: **ember** `#ff8b3d`, for primary actions, the current selection, and
live state. Never decoration, never a full-saturation inactive state. Netflix red
was the obvious move and the wrong one — ember is what a kitchen actually looks
like at night, and it belongs to food.

Secondary ink is tinted from the ground's hue rather than grey (`#c3b5a8` at
9.1:1, `#8d8177` at 4.6:1). Sage and plum appear only where they carry meaning.

## Type

**Fraunces** carries the display voice — dish names, the billboard, the reel.
Its SOFT and WONK axes are what keep it from reading as a default serif, and the
food-magazine register is the point.

**Geist** carries every label, control, step and number. Cook mode is an Operate
surface, so it runs on one workhorse family with a fixed rem scale — a fluid
heading that shrinks inside a panel looks worse, not better. Anything measured
(grams, minutes, servings, step counts) is set in tabular lining figures so
columns do not jitter as they count.

Display tops out at 4.25rem, tracking floor -0.032em, prose at 68ch.

## Motion

**Focal moment:** the dish name is uncovered from below as the plate lands at
centre, so the title and the arc arrive together. One authored entrance, not a
reveal on every element.

**Continuity:** when the companion narrows the shelf the arc re-forms and the
surviving dishes travel to their new seats. Filtering as travel, not as a swap.

**Feedback:** 140ms on controls, 220ms on state, 420ms on view changes. Exits run
faster than entrances. Everything eases on `cubic-bezier(0.16, 1, 0.3, 1)` from
an already-visible default, and the 3D side damps on the same curve so the CSS
and the scene agree.

**Reduced motion** cuts travel, not meaning: opacity, colour and state changes
survive, the caustic and the slow dish rotation stop, and the view transition is
skipped entirely.

## Browser surfaces

Selection, caret, scrollbar, focus ring, underline offset and tabular numerals
are all themed from the palette. These ship with no design system of their own,
and leaving them at browser defaults is the cheapest tell that a page was
assembled rather than built.

## What this deliberately does not do

- No stock photography and no gradient stand-ins for food — the dish is geometry.
- No emoji or unicode glyph anywhere an icon belongs; the set in `ui/Icon.tsx` is
  drawn at one weight, including the three-bar heat scale shared with the reel.
- No cards inside cards, no eyebrow above a heading, no gradient text.
- No modal. Cook mode is a surface, not an interruption.
- No orchestrated page-load sequence. The app loads into a task.
- No fake latency. The companion answers immediately; the reveal you see is the
  text arriving, not a staged wait.
