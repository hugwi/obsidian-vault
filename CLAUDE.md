# Claude Instructions — Second Brain Vault

## Vault Structure (flat, property-driven — "file over app" / Steph Ango model)
Organization is by the `categories` property + the [[Vault.base]], **not** by folders.
Most notes live at the vault root. Only a handful of structural folders exist.
```
obsidian-vault/
├── Categories/    → one hub note per category; each embeds its `.base` (navigation hubs)
├── (root)         → your own notes: projects, areas, resources, captures, evergreen
├── References/    → notes ABOUT external people/things (colleagues, contacts, companies)
├── Clippings/     → articles written by others (web clips + Readwise highlights)
├── Attachments/   → images, PDFs, audio, recordings
├── Daily/         → daily notes, nested YYYY/MM-MMMM/YYYY-MM-DD-dddd.md (core plugin)
├── Templates/     → note templates + Templates/Bases/ (per-category .base files)
└── Vault.base     → Bases file: one filtered view per category
```

> **No MOCs.** Navigation is category hubs + backlinks + `[[wikilinks]]` + quick switcher
> (kepano model). There is no `_MOC/` folder and no `moc` category.

## Organize by `categories`, not folders
Every note carries a `categories` list whose values are **wikilinks to the category hub**
(kepano "category trick"), e.g. `categories:\n  - "[[Projects]]"`. Each hub in `Categories/`
embeds a `.base` listing its members; `Vault.base` also turns each into a view:

| `categories` value | Extra props |
|---|---|
| `"[[Projects]]"` | `project: "[[Name]]"` |
| `"[[Areas]]"` | `domain:` engineering/career/clients/finance/health/interests/personal |
| `"[[Resources]]"` | `domain:` engineering/compliance |
| `"[[People]]"` | (lives in `References/`) |
| `"[[Clippings]]"` | (lives in `Clippings/`) |
| `"[[Inbox]]"` | unprocessed captures (at root) |
| `"[[Archive]]"` | inactive/completed |
| `"[[Daily]]"` | (lives in `Daily/`) |

## How to Help

### Processing inbox
When asked to "process inbox":
1. Review notes with `categories: [inbox]` (at root) and files in `Clippings/`
2. Set the right `categories`/`domain` (move clips out of `Clippings/` only if they become your own note)
3. Suggest `[[wikilinks]]` to related notes
4. Update `status:` frontmatter `inbox` → `processed` where present

### Finding related notes
- Filter by `categories`/`domain` via [[Vault.base]] or a `Categories/` hub, or search the flat root
- Suggest `[[wikilinks]]` using the note's filename (filename = title in this vault)
- Open the relevant hub in `Categories/` to see all notes of that type

### Adding new notes
Place at root (or `References/` for a person, `Clippings/` for others' articles). Frontmatter:
```yaml
---
created: YYYY-MM-DD
categories:
  - "[[Projects]]"   # or [[Areas]] | [[Resources]] | [[People]] | [[Inbox]] | [[Clippings]] | [[Archive]] | [[Daily]]
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
| Web clips (unprocessed) | `Clippings/` | `"[[Clippings]]"` |
| Quick ideas | root | `"[[Inbox]]"` |
| Personal life | root | `"[[Areas]]"` + `domain: personal/finance/health/interests` |

## Key Notes to Know
- **Ethira architecture**: `agentic-systems-architecture.md` (root)
- **Ethira tools catalog**: `agentic-systems-tools-and-prompts.md` (root)
- **Vault navigation**: `Home.md` (root) + `Categories/` hubs · **All views**: `Vault.base`
- **Daily notes template**: `Templates/daily_note_template.md`
- **Web clip template**: `Templates/web-clip-template.md`

## Clippings triage props
Every note in `Clippings/` carries two extra props for triage:
- `rating:` — 1–7 (number), how valuable the content is
- `action:` — one of `review` (todo, look at it) · `implement` (will build) · `insight` (good, not implementing)
Browse via `Clippings.base` (📋 To review / 🔨 To implement / 💡 Insights / ⭐ Top rated)
and `Agentic Engineering.base` (same action views + ⭐ Top rated).

## Agentic-engineering theming
The 221 `domain: agentic-engineering` clippings are organised by the **problem they solve**
(not by tool type — a library/skill/MCP/harness is classified by the capability it adds).
Each carries `theme:` (one slug) + `subtheme:` (1–3 finer tags). The 10 themes:
`context-engineering` · `work-breakdown-specs` · `quality-gates` ·
`comprehension-maintainability` · `multi-agent-orchestration` · `workflow-phases-gates` ·
`productivity-measurement` · `human-ux-frontend` · `industry-product` ·
`agents-models` (catch-all). Hub: [[Agentic Engineering]] (one view per theme, grouped by
sub-theme). Current landscape: [[Agentic Engineering — Trends 2026]]. When adding a new
agentic clipping, set `theme` + `subtheme` to match.

## Preferences
- ISO dates: `YYYY-MM-DD` (daily notes named `YYYY-MM-DD.md`, no weekday suffix)
- `categories`: wikilinks to a hub, TitleCase plural (`"[[Resources]]"`); tags: `lowercase-hyphenated`
- Internal links: `[[wikilinks]]` (shorthand by filename) preferred over URLs
- File names: human-readable; filename is the note title
- Commit message format: `type: description` (feat/fix/docs/chore)
```
