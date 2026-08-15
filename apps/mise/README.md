# Mise

A recipe companion that plates every dish in 3D and talks you through the cook.

Browsing feels like a streaming service — one dish held at centre, a shelf you
travel along, a billboard that names what you are looking at. The shell is glass
sitting in front of a live kitchen rather than a page with panels on it. And the
companion on the right is not a search box: every reply re-forms the shelf behind
the glass, so the conversation and the room are the same thing.

```bash
npm install
npm run dev        # the app
npm run build      # typecheck + production build
npm run reel:studio  # Remotion studio for the method reel
npm run reel       # render a dish's method to out/step-reel.mp4
```

## What's actually here

**Dishes are geometry, not photographs.** There is no image directory. Each
recipe carries a `plate`: an ordered list of edible forms — a sauce pooled under,
a mound, wedges laid down, capers scattered, dust over the top — and
`src/three/plating.ts` builds that into a real composition, placed on a
golden-angle spiral because that is how a cook scatters a garnish. Everything is
seeded off the recipe id, so a dish plates identically on every load. A new
recipe arrives plated instead of waiting on a photo shoot.

**The carousel is the continuity device.** When the companion narrows the shelf,
dishes are not swapped out underneath you: the arc re-forms and the survivors
travel to their new seats, so you can see where your dish went. That is the whole
reason it is 3D rather than a grid.

**The reel is a real Remotion composition.** `src/remotion/StepReel.tsx` is
mounted through `<Player>` inside cook mode *and* registered for the CLI, so the
timeline in the glass panel and the timeline in the exported MP4 are the same
code. The timing ring drains across each step's own duration, so a 20-minute
reduction visibly takes longer on screen than a 40-second bloom.

**The companion is deterministic and offline.** It reads the catalogue, not a
model — it never stalls, never needs a key, and never invents a step that would
ruin someone's dinner. It handles time and diet constraints, ingredient search,
naming a dish, in-cook navigation (`next`, `back`, `how long`), scaling, and
substitutions with the consequence stated.

### Putting a real model behind it

Everything in `src/companion/engine.ts` implements one interface:

```ts
interface CompanionEngine {
  respond(input: string, ctx: CompanionContext): Promise<CompanionReply>;
  greeting(ctx: CompanionContext): CompanionReply;
}
```

Write a second implementation and pass it to `<ChatPanel engine={...} />`. The
reply shape is what the UI animates against, so a model-backed engine has to
return the same `moves` — that is what keeps "something vegetarian, twenty
minutes" driving the carousel instead of just printing a paragraph.

## Layout

```
src/
  data/recipes.ts        nine recipes: method, ingredients, and plating description
  three/plating.ts       generative plating — spiral placement, vessel profiles
  three/Dish.tsx         one plated dish: vessel + instanced layers
  three/Carousel.tsx     the arc, drag/keyboard control, depth falloff
  three/Scene.tsx        canvas, studio light rig, WebGL fallback
  remotion/StepReel.tsx  the method reel composition
  companion/engine.ts    intent engine + the swap-in seam
  ui/                    billboard, rail, cook mode, chat panel, icon set
  styles/                tokens · base · glass · layout
```

## Notes for whoever picks this up

- **Fonts are self-hosted** through fontsource (Fraunces for the display voice,
  Geist for every control and number). Nothing is fetched from a font CDN.
- **Lighting ships with the app.** The studio rig is three `Lightformer` emitters
  rendered into an environment map rather than a downloaded HDR, so the app works
  offline. It lives at the scene root on purpose — parented inside the carousel
  group, which re-mounts whenever the shelf is filtered, drei's portal lost its
  virtual scene and the emitter quads leaked into the render as giant beige
  planes.
- **Nothing user-visible depends on a frame arriving.** Entrance animations are
  attached for a timer-bounded window (`ui/useEntrance.ts`), the companion's
  reply reveals on a timer rather than `requestAnimationFrame`, and the view
  transition in `App.tsx` runs on a short fuse. A full-viewport WebGL canvas can
  starve compositor animations, rAF callbacks and view-transition captures — all
  three were observed stalling indefinitely — and a stalled animation must never
  be the reason a headline, a step, or an answer is invisible.
- **No WebGL, no problem.** `Scene.tsx` catches the failure and the glass shell
  keeps working. This is a recipe app before it is a 3D one.
- **Swapping in photography**, if you ever want it: give `Recipe` an optional
  image and render it on the vessel in `Dish.tsx`. The plating system stays
  useful for anything you have not shot yet.

## Design

The visual world, the palette, the type scale and the motion thesis are written
up in [DESIGN.md](./DESIGN.md).
