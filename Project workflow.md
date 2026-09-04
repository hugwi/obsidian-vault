---
created: 2026-08-04
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - project
  - workflow
  - second-brain
---

# Project workflow

How a project gets worked in this vault: raw material stays where it was captured,
and the project note pulls it onto one page. Structure follows Tiago Forte — a
project is something with an **outcome** and a **deadline**, and progress is measured
in **intermediate packets**, not in hours.

## Start a project

Create a note at the root from `Templates/Project Template.md` and fill in four
properties:

```yaml
categories:
  - "[[Projects]]"
project: "[[Same name as the file]]"   # this is what marks it a project *hub*
status: active                          # active | pursue | paused | done
outcome: Ship the PII scanner to prod   # one sentence, past tense
due: 2026-09-30                         # optional
```

`status: pursue` is the "projects I want to pursue" shelf — a real project with a
real outcome that you have decided not to start yet. It stays off the active board
but keeps collecting material, so when you do start it the reading is already done.
A note with no `status` counts as active.

## Attach material to it

Two ways, both of which leave the source note where it is:

1. **`project: "[[Ethira]]"`** on any note — an external source note in `Raw/`, a person in
   `References/`, a resource at the root. The note keeps its own `categories`; the
   property is purely a "this belongs to that project" pointer. Use
   `project: ethira/api` to scope it to a slice — the parent project still shows it.
2. **A wikilink to the project note** from anywhere. Cheapest possible capture: type
   `[[Ethira]]` in today's daily note and it lands under *Recent mentions*.

Nothing moves folders. A raw note that becomes your own thinking gets rewritten into
a new note at the root — that is the only case where a file leaves `Raw/`.

## Capture into it

Two command-palette entries do the property-writing for you. Hit Cmd/Ctrl+P and type
**project** (or assign hotkeys in Settings → Hotkeys):

- **Capture to project** — a picker lists your projects, active first. Choose one and it
  opens with the cursor on a fresh `- YYYY-MM-DD — ` bullet under `## Log`, so you write
  with the project's own content in front of you. Choose *➕ New note* instead and it asks
  for a title and makes a plain root note in `[[Inbox]]`. Esc cancels.
- **Attach note to project** — run it while reading any note and pick a project; it writes
  `project: "[[Name]]"` into that note's frontmatter. This is the one for existing raw notes.

Both are Templater templates in `Templates/Commands/`, backed by user scripts in
`Templates/Templater/` — see the README there.

**From outside Obsidian**, the same capture runs through Raycast: *Capture to project*
takes a project name (fuzzy — `eth` finds Ethira) and a line of text, appends it to that
project's `## Log`, and never brings Obsidian to the front — it does not even need to be
running. Leave the project blank and you get a plain Inbox note instead. *Open project*
is the opposite: it fires `obsidian://open` and pulls you in. Both are Script Commands in
`Templates/Raycast/`, sharing the same log-insertion and project-detection code as the
in-app commands. What counts as a project note is defined
once, here: **a note with `categories: "[[Projects]]"` that either names itself in
`project:` or has no `project:` at all.** Anything pointing at a different project is a
note *inside* that project. That rule is implemented twice — `Templates/Templater/
projects.js` and `Templates/Scripts/project-desk/view.js` — because one reads Obsidian's
metadataCache and the other reads Dataview. Change both.

## Work it

The project note ends in:

````markdown
```dataviewjs
await dv.view("Templates/Scripts/project-desk");
```
````

which renders the desk:

| Section | What lands there |
|---|---|
| 📦 Intermediate packets | your own notes carrying this `project:` — specs, ADRs, benchmarks |
| 🧱 Raw material | attached raw notes, split by `action:` (implement / review / insight / untriaged) |
| 📚 Resources · 🗂️ Areas · 👤 People | supporting notes by category |
| 🗓️ Recent mentions | the last 10 daily notes that link the project |
| ✅ Open tasks | unchecked tasks across the project note and its packets |

The header line counts material and how much of it is **triaged** (has a `rating:` or
`action:`). A project whose raw pile keeps growing while the triaged count stays flat
is being collected into, not worked — that is the number to watch.

## Review it

[[Projects]] shows the board: every project grouped by status, with its outcome, its
material count, its next unchecked action and its due date. It also lists projects
that notes point at with `project:` but that have **no note yet** — the usual way a
project quietly disappears. Give each one a note or drop the property.

`Projects.base` (embedded on the same hub) is the same data as sortable tables,
including a 📎 Material view of everything attached to a project from outside it.
That view filters on `file.hasProperty("project")`; if your Obsidian version rejects
the function, swap it for `project != null`.

## Finish it

Set `status: done`, tick the outcome checkbox, and leave the note where it is. Move
it to `categories: "[[Archive]]"` only when you no longer want it on the board at
all — the packets it produced stay linked either way, which is the point of building
them as separate notes.
