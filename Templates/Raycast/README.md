# Raycast capture

Capture into a project **from anywhere** — a terminal, a browser, a call — without
Obsidian being focused or even running. These are
[Raycast Script Commands](https://github.com/raycast/script-commands): plain Node files
that write straight to the vault on disk. Obsidian picks up the change next time it
looks.

```
Templates/Raycast/capture-to-project.js   Capture to project   🎯
Templates/Raycast/open-project.js         Open project         📂
Templates/Raycast/lib/vault.js            shared, not a command
```

## Setup

1. **Raycast → Extensions → Script Commands → Add Directories** → pick
   `<vault>/Templates/Raycast`.
2. Both commands now appear in Raycast. Give **Capture to project** a hotkey or an
   alias — it is the one worth reaching for without thinking.
3. On a fresh clone, if Raycast says the script is not executable:
   `chmod +x Templates/Raycast/*.js`.

Requires `node` on your `PATH` (the shebang is `#!/usr/bin/env node`). Nothing else —
no npm, no `node_modules`, no Obsidian plugin.

## Capture to project

Two fields, filled inline in Raycast:

| Field | |
|---|---|
| **project** | Optional. Fuzzy-matched: `eth` finds `Ethira`. Leave it blank for a plain new note. |
| **what happened** | The text. |

- **With a project** → appends `- YYYY-MM-DD — your text` to that project's `## Log`,
  creating the section above the `## Desk` block if it is missing. Prints `→ Ethira`.
  Obsidian never takes focus.
- **Blank project** → creates a note at the vault root titled from your text, with
  `created:` and `categories: "[[Inbox]]"`. Never overwrites: a second capture with the
  same first line becomes `… 2.md`.
- **Ambiguous or unknown project** → writes nothing, exits non-zero, and tells you what
  it did match. Silently capturing into the wrong note is the one failure worth being
  strict about.

## Open project

One field, same fuzzy match, then fires `obsidian://open`. This one *is* meant to pull
you into Obsidian. The vault's display name defaults to `hugwi`; override it with the
`OBSIDIAN_VAULT` environment variable if you add the vault under another name elsewhere.

## Why the filesystem and not `obsidian://`

Obsidian's URI scheme can append to a note, but opening any URL activates Obsidian on
macOS — the exact context switch this is meant to avoid. Writing the file directly keeps
the capture invisible, and works with Obsidian quit.

## Shared with the in-app commands

Nothing here reimplements the capture rules. Both scripts import the functions the
Templater commands already use:

- `logInsertion` from `Templates/Templater/captureToProject.js` — finds or creates
  `## Log`, keeps it above the desk block.
- `isProjectHub` from `Templates/Templater/projects.js` — the single definition of what
  counts as a project note.

`lib/vault.js` adds only what Obsidian's API normally provides and cannot here: reading
frontmatter off disk (a deliberately small YAML subset — scalars and block lists),
walking the vault, and fuzzy-matching a typed name. It lives in `lib/` so Raycast's
directory scan does not mistake it for a command.

## Two things to know

- **Do not capture into a note you are actively editing in Obsidian.** Obsidian reloads
  external changes, but a pending in-app save can overwrite an append made seconds
  earlier. In practice you are in another app, which is the point.
- **`findHubs` skips `Attachments/`, `Templates/`, `Daily/` and `Raw/`** for speed.
  Project notes live at the vault root, so this is free — but a project note filed inside
  one of those folders would be invisible to Raycast.

Verify with `node Templates/Raycast/lib/vault.test.js` (38 checks against a throwaway
vault in a temp dir). The scripts take the vault root as an optional second argument to
`main()` purely so the test can point them somewhere safe; Raycast never passes it.

## Running from a git worktree

`vaultRoot()` resolves upwards from the script's own path, so in a worktree it finds the
**worktree's** copy of the vault — captures would land in a checkout Obsidian never
opens. Set `OBSIDIAN_VAULT_PATH` to the real vault to point them back:

```bash
OBSIDIAN_VAULT_PATH=~/vaults/hugwi ./capture-to-project.js eth "from the worktree"
```

Raycast has no per-command environment, so for a worktree you would set it in the shell
Raycast inherits — or simpler, only point Raycast at a directory inside the live vault
and use the worktree for reading the code.
