# Claude Instructions — Second Brain Vault

## Vault Structure (flat, property-driven — "file over app" / Steph Ango model)
Organization is by the `categories` property + the [[Vault.base]], **not** by folders.
Most notes live at the vault root. Only a handful of structural folders exist.
```
obsidian-vault/
├── Categories/    → one hub note per category; each embeds its `.base` (navigation hubs)
├── (root)         → your own notes: projects, areas, resources, captures, evergreen
├── References/    → notes ABOUT external people/things (colleagues, contacts, companies)
├── Raw/           → external source notes (web captures + Readwise highlights)
├── Attachments/   → images, PDFs, audio, recordings
├── Daily/         → daily notes, nested YYYY/MM-MMMM/YYYY-MM-DD-dddd.md (core plugin)
├── Templates/     → note templates + Templates/Bases/ (per-category .base files)
│                    + Templates/Web Clipper/ (clipper JSON) + Templates/Scripts/ (JS)
└── Vault.base     → Bases file: one filtered view per category
```

> **Reusable scripts live in `Templates/Scripts/<name>/view.js`.** They must sit in a
> normal, indexed folder — `dv.view()` resolves via `metadataCache.getFirstLinkpathDest`,
> so it cannot load from `.obsidian/` or any dot-prefixed folder (unlike `.multilabel.py`
> and `.cluster_work/`, which are hidden on purpose). `Templates/` already holds the
> vault's other non-note technical files, so scripts go there rather than in a new root
> folder. **`.js` also needs Settings → Files & Links → *Detect all file extensions*
> (`showUnsupportedFiles`)** — while that is off Obsidian doesn't index `.js` at all and
> `dv.view()` fails with "custom view not found". See `Templates/Scripts/README.md`.

> **No MOCs.** Navigation is category hubs + backlinks + `[[wikilinks]]` + quick switcher
> (kepano model). There is no `_MOC/` folder and no `moc` category.

## Organize by `categories`, not folders
Every note carries a `categories` list whose values are **wikilinks to the category hub**
(kepano "category trick"), e.g. `categories:\n  - "[[Projects]]"`. Each hub in `Categories/`
embeds a `.base` listing its members; `Vault.base` also turns each into a view:

| `categories` value | Extra props |
|---|---|
| `"[[Projects]]"` | `project: "[[Name]]"` + `status:`/`outcome:`/`due:` on the hub note |
| `"[[Areas]]"` | `domain:` engineering/career/clients/finance/health/interests/personal |
| `"[[Resources]]"` | `domain:` engineering/compliance |
| `"[[People]]"` | (lives in `References/`) |
| `"[[Raw]]"` | (lives in `Raw/`) |
| `"[[Inbox]]"` | unprocessed captures (at root) |
| `"[[Archive]]"` | inactive/completed |
| `"[[Daily]]"` | (lives in `Daily/`) |

## How to Help

### Processing inbox
When asked to "process inbox":
1. Review notes with `categories: [inbox]` (at root) and files in `Raw/`
2. Set the right `categories`/`domain` (rewrite a raw note at the root only when it becomes your own note)
3. Suggest `[[wikilinks]]` to related notes
4. Update `status:` frontmatter `inbox` → `processed` where present

### Working a project
Projects follow Forte: an `outcome:` (one sentence, past tense), a `due:`, a
`status:` (`active` · `pursue` · `paused` · `done` — missing counts as active), and
progress measured in **intermediate packets** (own notes carrying the project's
`project:`). `status: pursue` is the "want to pursue, not started" shelf.

**`project:` attaches any note to a project without moving or recategorising it** —
an external source note keeps `categories: "[[Raw]]"` and stays in `Raw/` while showing
up as that project's raw material. `project: name/slice` scopes to a sub-area of
`name`. A plain `[[wikilink]]` to the project note counts too (that is how daily notes
land on the desk). When asked to attach material to a project, add the `project:`
property — never move the file. By hand the user does this with the **Attach note to
project** command (Cmd+P → "project"); every capture template ships an empty
`project:` field to fill at save time.

- Project note body ends in ` ```dataviewjs / await dv.view("Templates/Scripts/project-desk") ` —
  renders packets, raw material split by `action:`, resources/areas/people, recent
  daily mentions, open tasks. Template: `Templates/Project Template.md`.
- Hub [[Projects]] runs the same view with `{mode: "board"}`: every project by status,
  with next action, material counts, and any `project:` value that has **no note yet**.
- Capture commands: `Templates/Commands/` + user scripts in `Templates/Templater/`
  (Templater `user_scripts_folder` + `enabled_templates_hotkeys` — see that README).
- Capture from outside Obsidian: Raycast Script Commands in `Templates/Raycast/`, which
  write to disk directly (no plugin, Obsidian need not run) and import the same
  `logInsertion`/`isProjectHub` — never fork that logic.
- Full description: [[Project workflow]] · views: `Templates/Bases/Projects.base` ·
  in-flight state: `Templates/HANDOFF - Project workflow.md` (delete once verified).

### Finding related notes
- Filter by `categories`/`domain` via [[Vault.base]] or a `Categories/` hub, or search the flat root
- Suggest `[[wikilinks]]` using the note's filename (filename = title in this vault)
- Open the relevant hub in `Categories/` to see all notes of that type

### Adding new notes
Place at root (or `References/` for a person, `Raw/` for others' articles). Frontmatter:
```yaml
---
created: YYYY-MM-DD
categories:
  - "[[Projects]]"   # or [[Areas]] | [[Resources]] | [[People]] | [[Inbox]] | [[Raw]] | [[Archive]] | [[Daily]]
domain: engineering   # if areas/resources: engineering|career|clients|finance|health|interests|compliance|personal
project: "[[Name]]"   # if projects
tags: [lowercase-hyphenated]
---
```
Do **not** add a redundant `title:` — the filename is the title.

## Note Placement Rules
| Content type | Where | `categories` |
|---|---|---|
| Architecture/technical patterns | root | `"[[Resources]]"` + `domain: engineering` |
| GDPR, PCI, data governance | root | `"[[Resources]]"` + `domain: compliance` |
| Active project work | root | `"[[Projects]]"` + `project:` |
| Architecture Decision Records | root, `adr-*.md` | `"[[Projects]]"` + `project:` |
| Meeting notes (client/work) | root | `"[[Areas]]"` + `domain: clients` |
| Career & growth notes | root | `"[[Areas]]"` + `domain: career` |
| People/contacts | `References/` | `"[[People]]"` |
| External source notes (unprocessed) | `Raw/` | `"[[Raw]]"` |
| Raw note that belongs to a project | stays in `Raw/` | `"[[Raw]]"` + `project:` |
| Quick ideas | root | `"[[Inbox]]"` |
| Personal life | root | `"[[Areas]]"` + `domain: personal/finance/health/interests` |

## Key Notes to Know
- **Ethira architecture**: `agentic-systems-architecture.md` (root)
- **Ethira tools catalog**: `agentic-systems-tools-and-prompts.md` (root)
- **Vault navigation**: `Home.md` (root) + `Categories/` hubs · **All views**: `Vault.base`
- **Daily notes template**: `Templates/daily_note_template.md`
- **Web clip template**: `Templates/web-clip-template.md`
- **Project workflow**: `Project workflow.md` (root) + `Templates/Project Template.md`
- **Design inspiration**: `Inspiration.md` (root) + `Templates/Bases/Inspiration.base`
- **Design**: hub `Design.md` (root) + `Templates/Bases/Design.base` · subpages
  `AI Design.md` (design × agents), `Design Fundamentals.md` (tool-agnostic craft),
  `Inspiration.md` (taste library). Everything design carries `domain: design` — there
  is no `design` tag. Design notes also carry `type:`
  (`article | video | skill | tool | inspiration | note`), and `rating:` is left blank
  for the user to set. `published:` is backfilled only where the source exposes it.

## Raw triage props
Every note in `Raw/` carries two extra props for triage:
- `rating:` — 1–7 (number), how valuable the content is
- `action:` — one of `review` (todo, look at it) · `implement` (will build) · `insight` (good, not implementing)
Browse via `Raw.base` (📋 To review / 🔨 To implement / 💡 Insights / ⭐ Top rated)
and `Agentic Engineering.base` (same action views + ⭐ Top rated).

## Inspiration media notes (`type: inspiration`)
Web-design inspiration from 21st.dev / Dribbble / Pinterest etc. is captured by the
**Inspiration - Media** Web Clipper template (`Templates/Web Clipper/inspiration-media.json`)
into `Raw/`. These notes store **remote URLs only — never download the media**.
- Video props, checked in this order by the renderer: `media_url_secure` → `media_url` →
  `media_url_twitter` → `media_url_schema` → `media_url_source` → `media_url_video`;
  `source_url` is also used when it ends in `.mp4`/`.webm`/`.mov`/`.m4v`.
- Image props, in precedence order: `media_url_srcset` (largest entry) → `media_url_image`
  (site-specific media container) → `thumbnail_url` (og:image) → `media_url_image_meta`
  (twitter:image / schema / poster) → `media_url_image_generic` (`figure`/`article`/`main`).
  **Page metadata deliberately outranks the generic DOM match**: a broad `article img`
  selector matches a neighbouring item in a related-content grid, which on a Dribbble shot
  page is somebody else's shot. Same reason every video selector is container-scoped.
  **Most Dribbble/Pinterest posts are stills**, so a saved item with no video is normal, not a
  failure — the renderer shows the image instead.
- Unplayable media is detected, not shown broken: `blob:`/`data:` URLs are rejected, an
  expired video URL falls back to the still with an explanation, and `.m3u8`/`.mpd`
  manifests are offered only where `canPlayType` says the engine supports them (no on
  desktop Electron/Chromium, yes on Obsidian iOS/WKWebView). The browser extension is
  irrelevant — the renderer runs in Obsidian, not the browser.
- Plus `type: inspiration`, `platform:`, `thumbnail_url:`, `saved_at:` (alongside the usual
  `categories: "[[Raw]]"`, `created:`, `rating:`, `action:`).
- Default tags: `inspiration`, `web-design`, `ui`, `ux`. Add finer ones by hand
  (`animation`, `navigation`, `mobile`, `landing-page`, `typography`, `dashboard`,
  `interaction-design`).
- Body calls ` ```dataviewjs / await dv.view("Templates/Scripts/remote-media") ` — video →
  thumbnail + **Load video** button (source attached only on click); still → full-width
  image, click-through to source; neither → message + source link. Needs Dataview →
  *Enable JavaScript Queries* **and** Files & Links → *Detect all file extensions*.
- Hub: [[Inspiration]] · views: `Templates/Bases/Inspiration.base` (gallery is thumbnails
  only — never embed every remote video in the overview).
- **Adding a site**: add a regex trigger (+ container selector if needed) to
  `inspiration-media.json`, and — only if the site serves downscaled stills — one entry in
  the `SITES` table at the top of `view.js` (Dribbble drops `?resize=`, Pinterest rewrites
  `/236x/`→`/originals/`). A wrong upgrade guess is free: the renderer falls back down the
  candidate list on load error. Verify with `node Templates/Scripts/remote-media/test.js`.

## Agentic-engineering theming
The 221 `domain: agentic-engineering` raw notes are organised by the **problem they solve**
(not by tool type — a library/skill/MCP/harness is classified by the capability it adds).
Each carries `theme:` (one slug) + `subtheme:` (1–3 finer tags). The 10 themes:
`context-engineering` · `work-breakdown-specs` · `quality-gates` ·
`comprehension-maintainability` · `multi-agent-orchestration` · `workflow-phases-gates` ·
`productivity-measurement` · `human-ux-frontend` · `industry-product` ·
`agents-models` (catch-all). Hub: [[Agentic Engineering]] (one view per theme, grouped by
sub-theme). Current landscape: [[Agentic Engineering — Trends 2026]]. When adding a new
agentic raw note, set `theme` + `subtheme` to match.

## Git setup (run once per clone — check this before any git work)
This vault is synced by obsidian-git, which auto-commits on a timer. Obsidian and its
plugins rewrite `.obsidian/*.json` in full whenever a setting changes or a new property
appears (creating a raw note is enough to rewrite `types.json`), so those files collide on
almost every pull. `.gitattributes` marks them `merge=ours`, but **the driver has to be
enabled locally — it cannot be committed**:

```bash
git config merge.ours.driver true
```

**Always verify this is set before pulling, merging, or resolving conflicts** in a new
clone or a fresh container — `git config merge.ours.driver` should print `true`. If it is
empty, set it, then continue. Without it Git falls back to ordinary conflicts on machine
state nobody is trying to merge.

If a conflict does appear in `.obsidian/`, keep the local copy — Obsidian regenerates that
state anyway:

```bash
git checkout --ours .obsidian/ && git add .obsidian/
```

Real content — notes, templates, scripts, bases — merges normally, and a conflict there is
worth reading.

## Preferences
- ISO dates: `YYYY-MM-DD` (daily notes named `YYYY-MM-DD.md`, no weekday suffix)
- `categories`: wikilinks to a hub, TitleCase plural (`"[[Resources]]"`); tags: `lowercase-hyphenated`
- Internal links: `[[wikilinks]]` (shorthand by filename) preferred over URLs
- File names: human-readable; filename is the note title
- Commit message format: `type: description` (feat/fix/docs/chore)
```
