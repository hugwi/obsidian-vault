# Handoff — Inspiration clipping workflow

Written 2026-08-04. Last commit: `6438b7f` on `main`. Working tree clean, pushed.

Read this alongside `README.md` in this folder, which is the permanent reference.
This file is the temporary "where we are right now" — delete it once the open item
below is closed.

---

## What we are building

Save web-design inspiration (Dribbble, Pinterest, 21st.dev) into `Clippings/` with the
Obsidian Web Clipper alone, storing **remote URLs only**.

**Hard constraint, in force since the original brief — do not relax it:**
no media is ever downloaded into the vault. No MP4, no image files. The note stores
URLs; a DataviewJS renderer draws them at read time. A video is attached to the
`<video>` element only when the reader clicks "Load video", never on note open.

## Current state: working; Pinterest remains unverified

| Piece | State |
|---|---|
| Renderer `Templates/Scripts/remote-media/view.js` | done, regression suite green |
| Clipper template `Templates/Web Clipper/inspiration-media.json` | done |
| Overview `Templates/Bases/Inspiration.base` + `Inspiration.md` hub | done |
| Multi-image capture on Dribbble | confirmed end-to-end on a real seven-image clip |
| 21st.dev component + homepage capture | confirmed end-to-end on Phone Mockups 1 and the supplied homepage URL |
| Pinterest selectors | written, never observed |

## Set up a new machine before anything else

```bash
git clone <vault> && cd obsidian-vault
git config merge.ours.driver true    # REQUIRED, cannot be committed
```

Without that last line every `git pull` conflicts on `.obsidian/*.json`, because
Obsidian rewrites those files wholesale on any settings change. `.gitattributes`
marks them `merge=ours` but the driver has to exist locally. Verify with
`git config merge.ours.driver` → should print `true`.

Two Obsidian settings gate the renderer, both already committed in `.obsidian/` but
worth knowing:
- Dataview → **Enable JavaScript Queries** (`enableDataviewJs`)
- Files & Links → **Detect all file extensions** (`showUnsupportedFiles`).
  Without this Obsidian does not index `.js` at all and `dv.view()` fails with
  "custom view not found". This cost us a debugging round.

## Pick up here — remaining open item

Pinterest still needs one real clipping pass. Dribbble and 21st.dev have both been
confirmed from browser DOM through Web Clipper into an Obsidian note. For 21st.dev the
verified component was `@solaceui/components/phone-mockups-1`: direct poster, derived
MP4, live bundle, demo source, and description all landed correctly. The supplied
homepage URL also exposed and captured its native landing MP4/poster; CSS/SVG-only
motion intentionally remains represented by the source page.

## How the multi-image capture works

This is the subtle part and the easiest thing to break.

The clipper stores one array entry **per matched element**
(`extractContentBySelector` in the clipper's `src/utils/shared.ts`), using
`el.getAttribute(attr) || ''`. A lazy-loaded image below the fold therefore
contributes an **empty string that still occupies its slot**.

Three properties read the same element set through different attributes:

| Property | Attribute |
|---|---|
| `media_url_gallery` | `src` |
| `media_url_gallery_srcset` | `srcset` |
| `media_url_gallery_lazy` | `data-srcset` |
| `media_url_gallery_href` | Dribbble PhotoSwipe anchor `href` |

`view.js` resolves **each image from its own slot index**, taking the first capture
that has a URL at that index. Two tempting alternatives are both wrong and are
covered by tests:
- *"use whichever capture matched the most images"* — on a lazy-loaded page the `src`
  and `data-srcset` captures can hold different **halves** of the set, so picking one
  discards the other half.
- *"concatenate all three"* — renders one image's own srcset variants as separate
  pictures.

## Mistakes already made — do not repeat these

- **Do not prefix selectors with `#ssr-app`.** CDP sees that hydrated wrapper, but Web
  Clipper's extraction snapshot does not. Use `img[data-test="v-img"]`,
  `a[data-photoswipe-image]`, and `.formatted-text.content-block` directly.
- **Page metadata cannot rebuild a shot's image set.** On shot 27606181 `og:image` is
  upload `48556246`, while the real gallery uploads are `48556248` and `48556247`. This is
  why the container capture exists at all.
- **Keep video selectors container-scoped.** An unscoped `{{selector:video?src}}`
  pulled a video out of the "More by this designer" grid — someone else's work.
- **Page metadata outranks the generic DOM tier** in the image precedence chain. A
  broad `article img` once matched a neighbouring shot in a related-content grid.
  Order in `rawImageCandidates`: container selector → page metadata → generic → a
  still wrongly published in a video property.
- **Do not add a `schema:@VideoObject` trigger.** It made the template fire on every
  page. Triggers are URL regexes only.
- **Do not assume Chromium's media support.** HLS/`.m3u8` fails on desktop Electron
  but plays on Obsidian iOS/WKWebView, so the renderer feature-detects with
  `canPlayType` rather than hardcoding. The clipping *browser* is irrelevant — the
  renderer runs inside Obsidian.

## Blocked in the container, needs a real machine

Pinterest has not yet been observed in a real Web Clipper pass. Dribbble and 21st.dev
were inspected and clipped through the CDP-enabled Chrome profile on 2026-08-05.

Also unverified: whether the Bases `type: cards` / `image:` syntax renders in the
installed Obsidian version. A table view is in `Inspiration.base` as a fallback.

## Files

```
Templates/Scripts/remote-media/view.js        the renderer (SITES table at top = extension point)
Templates/Scripts/remote-media/test.js        128 assertions, no deps: node test.js
Templates/Scripts/remote-media/probe-lazy.js  paste into browser console to diagnose
Templates/Scripts/remote-video/view.js        one-line forwarder, for notes clipped before the rename
Templates/Web Clipper/inspiration-media.json  the clipper template
Templates/Web Clipper/README.md               permanent reference, incl. verified-container table
Templates/Bases/Inspiration.base              gallery views (thumbnails only, never embed remote video)
Inspiration.md                                the hub note
```

Run the tests after any change to `view.js`:

```bash
node Templates/Scripts/remote-media/test.js
```

Adding a site is documented in `README.md` → "Adding another site": a trigger regex in
`inspiration-media.json`, plus an entry in the `SITES` table in `view.js` only if the
site serves downscaled stills. A wrong upgrade guess is free — the renderer falls back
down the candidate list on load error.

## Loose ends, none blocking

- Three test notes in `Clippings/` can be deleted: `Remote video test.md`,
  `Remote video fallback test.md`. (`Landing Page for Yoga Platform.md` is a real clip
  worth keeping.)
- Seven existing Readwise design clippings could be backfilled with
  `type: inspiration` so they appear in the Inspiration base.
- An `AGENTS.md` pointing at `CLAUDE.md` was offered for cross-tool agents, never
  started.
