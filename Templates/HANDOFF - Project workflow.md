# Handoff — Project workflow & capture

Written 2026-08-04. Last commit: `4763ac9` on `main`. Working tree clean, pushed.

Read this alongside `Project workflow.md` (root), which is the permanent reference.
This file is the temporary "where we are right now" — delete it once the verification
below is done and the open items are closed or dropped.

---

## What we built

Working a project meant remembering which raw notes belonged to it and hand-editing
frontmatter to attach them. Now:

1. **A note joins a project** by carrying `project: "[[Name]]"` — on *any* note, in *any*
   folder, with its `categories` untouched. A wikilink to the project note counts too.
2. **The project note renders a desk** gathering all of it: intermediate packets, raw
   material split by triage `action:`, resources/areas/people, recent daily mentions,
   open tasks.
3. **Three ways to capture**, all writing the same `## Log` section: a Templater command
   inside Obsidian, an attach command for the note you are reading, and Raycast Script
   Commands that work with Obsidian **quit**.

Structure follows Tiago Forte: `outcome:` (one sentence, past tense), `due:`, `status:`
(`active` · `pursue` · `paused` · `done`, missing = active), progress measured in
intermediate packets. `status: pursue` is the "want to pursue, not started" shelf.

## Current state: built and unit-tested, **nothing verified in the real apps**

| Piece | State |
|---|---|
| `Templates/Scripts/project-desk/view.js` — desk + `{mode:"board"}` | 22 checks green, **never rendered in Obsidian** |
| `Templates/Templater/projects.js` + `captureToProject.js` | 20 checks green, **modal never opened** |
| `Templates/Commands/*.md` — the two palette commands | written, **never run** |
| `Templates/Raycast/*.js` — capture + open | 38 checks green; capture run once for real from the CLI, **never run from Raycast** |
| `Templates/Bases/Projects.base` — status views + 📎 Material | **never opened**; see `hasProperty` risk below |
| `project:` on all capture templates | committed; **the 6 clipper JSONs need re-importing into the browser extension** |
| Ethira, Datahub, PII wired to the desk | done. PII was created — 17 notes pointed at a project with no note |

**This is the single most important thing to know:** every test in this work runs against
a fake Obsidian API or a temp-dir vault. There is no Obsidian and no Raycast in the
container it was built in. The logic is exercised; the integration is not.

## Pick up here — verify, in this order

```bash
git pull origin main
git config merge.ours.driver true    # REQUIRED per clone, cannot be committed
chmod +x Templates/Raycast/*.js
```

Then **reload Obsidian (Cmd/Ctrl+R)** — the Templater config changed and the commands do
not register until you do.

1. **Desk renders.** Open `Ethira.md`. Expect packet/material sections and counts. If it
   says *"custom view not found"*, the cause is one of the two settings in
   `Templates/Scripts/README.md`, both already committed.
2. **Board renders.** Open `Categories/Projects.md`. Expect projects grouped by status
   plus a ⚠️ row for `project:` values with no note.
3. **Bases views open.** `Templates/Bases/Projects.base` — especially **📎 Material**,
   which filters on `file.hasProperty("project")`. That function could not be verified
   offline (obsidian.md 403s from the container). **If the view errors, swap it for
   `project != null`** — noted in `Project workflow.md` too.
4. **Palette commands.** Cmd+P → `project`. They appear as *Templater: Insert
   Commands/Capture to project*. Run both. Expect: a fresh `- YYYY-MM-DD — ` bullet under
   `## Log` with the cursor on it; and `project: "[[…]]"` written into a raw note's
   frontmatter.
5. **Raycast.** Settings → Extensions → `+` → Add Script Directory →
   `<vault>/Templates/Raycast`. **Most likely failure: `env: node: No such file or
   directory`** — Raycast does not use your login shell's PATH, so Homebrew/nvm node is
   invisible. Fix with `sudo ln -s "$(which node)" /usr/local/bin/node`, or convert the
   scripts to `#!/bin/bash` wrappers that prepend the usual node locations (offered,
   never built).
6. **Clipper.** Re-import all six JSONs into the browser extension — it keeps its own
   copy, so the repo change alone does nothing. Clip something; confirm it lands in
   `Raw/` with `categories`, `read: false`, `rating`, `action: review`, `project`.

## Constraints — do not relax these

- **Never move a file to attach it to a project.** The `project:` property is the whole
  mechanism; a raw note stays in `Raw/` and keeps `categories: "[[Raw]]"`.
- **The folder does not file anything — the property does.** A note in `Raw/`
  without `categories: "[[Raw]]"` is invisible to every view. This is why the five
  `*-summary.json` clipper templates got `categories` when they were repointed, not just
  a new `path`.
- **Do not fork `logInsertion` or `isProjectHub`.** The Raycast scripts `require()` them
  from `Templates/Templater/`. Three implementations of "where does the log line go"
  would drift within a week.
- **No new Obsidian plugins.** QuickAdd was considered for capture and rejected: it does
  what ~100 lines of Templater already does here, and its config lives in plugin JSON
  rather than in readable vault files.
- **`obsidian://` is wrong for capture.** Opening a URL activates Obsidian on macOS,
  which is the context switch Raycast capture exists to avoid. It is right for *opening*
  — that is what `open-project.js` uses.

## Known duplication, deliberate

The rule for what counts as a project note — `categories: "[[Projects]]"` **and** either
naming itself in `project:` or having no `project:` — exists in three places because
each reads a different API:

| File | Reads |
|---|---|
| `Templates/Scripts/project-desk/view.js` (`renderBoard`) | Dataview |
| `Templates/Templater/projects.js` (`isProjectHub`) | Obsidian metadataCache |
| `Templates/Raycast/lib/vault.js` (`findHubs`) | **imports `isProjectHub`** — not a third copy |

So two implementations, not three. Change both when the rule changes. It is stated once
in prose in `Project workflow.md`.

## Open items, none blocking

- **`Home.md` is stale** — describes `Inbox/Web Raw/` and `MOC-*` notes that no
  longer exist, and its hand-maintained Active Projects table duplicates the board.
  Offered, never done.
- **Clipper filenames** still carry date prefixes (`2026-08-04 - Title`) while the 444
  existing raw notes use bare titles. Left alone because X and Reddit titles are not
  unique without the snippet. One line each in `noteNameFormat` if wanted.
- **`clip/article` tags** are nested, not `lowercase-hyphenated` per CLAUDE.md, and
  redundant with `type:`. Cosmetic.
- **Hotkeys are unbound.** Suggested `Cmd+Shift+C` for capture, `Cmd+Shift+A` for attach;
  both free in this vault (`Cmd+Shift+P` is taken by the comments plugin). Raycast:
  alias `cap`.
- **A real Raycast extension** (searchable project list instead of a typed field) was
  offered. It needs an npm/TypeScript project and Raycast dev mode, and cannot live
  inside the vault repo — the capture logic would be reused as-is.
- **System-wide beyond Raycast** (Alfred, Shortcuts) works already: the scripts are plain
  Node with positional arguments.
- `OBSIDIAN_VAULT_PATH` overrides the resolved vault root — needed only if the scripts
  are ever run from a git worktree, where "up the tree" is the worktree's own copy.

## Files

```
Project workflow.md                        permanent reference — read this first
Templates/Scripts/project-desk/view.js     desk + board renderer  ({mode:"board"}, {project:"X"})
Templates/Scripts/project-desk/test.js     22 checks: node test.js
Templates/Templater/projects.js            the picker + isProjectHub (the rule)
Templates/Templater/captureToProject.js    logInsertion + open-and-place-cursor
Templates/Templater/projects.test.js       20 checks
Templates/Templater/README.md              why this folder is separate from Scripts/
Templates/Commands/Capture to project.md   palette command
Templates/Commands/Attach note to project.md
Templates/Raycast/capture-to-project.js    Script Command, two args
Templates/Raycast/open-project.js          Script Command, fires obsidian://open
Templates/Raycast/lib/vault.js             frontmatter off disk, vault walk, fuzzy match
Templates/Raycast/lib/vault.test.js        38 checks
Templates/Raycast/README.md                Raycast setup + the node PATH trap
Templates/Bases/Projects.base              status views + 📎 Material
Categories/Projects.md                     the board
Templates/Project Template.md              Forte-shaped: outcome, done-when, packets, desk
```

Run everything after any change:

```bash
node Templates/Scripts/project-desk/test.js
node Templates/Templater/projects.test.js
node Templates/Raycast/lib/vault.test.js
```

One caution learned the hard way: `Templates/Raycast/lib/vault.test.js` writes to a
temp-dir vault, and `main()` takes the vault root as an optional second argument purely
so it can. An early version without that seam wrote test captures into the **real**
`Ethira.md`. Keep passing `root` in tests.
