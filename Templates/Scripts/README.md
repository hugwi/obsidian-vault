# Scripts

Reusable JavaScript for Dataview's `dv.view()`. One folder per view:

```
Templates/Scripts/<name>/view.js      # required entry point
Templates/Scripts/<name>/view.css     # optional, auto-injected
```

Call it from a note with:

````markdown
```dataviewjs
await dv.view("Templates/Scripts/<name>");
```
````

## Two settings are required

`dv.view()` resolves the path through `metadataCache.getFirstLinkpathDest`, so the
file has to be **indexed by Obsidian**. Two things must be on, or you get
`Dataview: custom view not found for '...'`:

1. **Settings → Files & Links → Detect all file extensions** — off by default, and
   while it is off Obsidian does not index `.js` at all, so the view is invisible
   even though the file is on disk. Stored as `showUnsupportedFiles` in
   `.obsidian/app.json`.
2. **Settings → Dataview → Enable JavaScript Queries** — stored as
   `enableDataviewJs` in `.obsidian/plugins/dataview/data.json`.

Both are committed to this vault, so a fresh clone works after one Obsidian reload
(Cmd/Ctrl+R).

## Why this folder

Scripts cannot live in `.obsidian/` or any dot-prefixed folder — Obsidian does not
index those, so `dv.view()` can never resolve them. That rules out the vault's usual
hiding place for machine files (`.multilabel.py`, `.cluster_work/`). `Templates/`
already holds the other non-note technical files (`Bases/`, `Web Clipper/`), so
scripts go here rather than in a new root folder.

## Views

| View | Used by |
|---|---|
| `remote-media/` | `type: inspiration` clippings — still image, or thumbnail + on-demand remote video |
| `remote-video/` | compatibility shim forwarding to `remote-media` (see below) |

`remote-media` was called `remote-video` until it grew still-image support, at which point
the name was actively misleading on an image-only clipping. `remote-video/view.js` is now a
one-line forwarder so notes clipped before the rename keep working. Delete that folder once
nothing references it:

```bash
grep -rl 'Scripts/remote-video' --include='*.md' .
```

`remote-media/` ships a `SITES` table at the top of `view.js` holding per-site URL rules
(Dribbble, Pinterest, 21st.dev today). Adding a site means appending one entry — see
*Adding another site* in `Templates/Web Clipper/README.md`.

`remote-media/test.js` runs the renderer against a stubbed Dataview/DOM:

```bash
node Templates/Scripts/remote-media/test.js
```

93 assertions, no dependencies. It stubs both engines Obsidian runs on (Electron/Chromium
and iOS/WKWebView) so HLS behaviour is covered in both directions. Run it after editing
`view.js`; Obsidian ignores `test.js` since `dv.view()` only loads `view.js`.
