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
| `remote-video/` | `type: inspiration` clippings — thumbnail + on-demand remote video player |
