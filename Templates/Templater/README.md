# Templater scripts

JavaScript that Templater exposes as `tp.user.<filename>`. One file per function:

```
Templates/Templater/projects.js          -> tp.user.projects(tp, options)
Templates/Templater/captureToProject.js  -> tp.user.captureToProject(file, date)
```

## Why not `Templates/Scripts/`

That folder holds Dataview views, which are all named `view.js` inside a folder per
view. Templater scans its scripts folder **recursively and keys scripts by basename**,
so pointing it at `Templates/Scripts` would register two different `view` functions and
one would win at random. Separate folder, no collision.

## Two settings are required

Both are committed, so a fresh clone works after one Obsidian reload (Cmd/Ctrl+R):

1. **Settings → Templater → User Scripts Folder** = `Templates/Templater`
   (`user_scripts_folder` in the plugin's `data.json`).
2. **Settings → Templater → Template Hotkeys** must list each command template
   (`enabled_templates_hotkeys`). That is what turns a template into a command-palette
   entry; without it the file is just a template you have to insert by hand.

`.js` also needs **Files & Links → Detect all file extensions**, already on for the
Dataview views.

## Commands

Both live in `Templates/Commands/` and appear in the palette as
*Templater: Insert Templates/Commands/…* — type **project** to find either. Assign real
hotkeys in Settings → Hotkeys (search "project").

| Command | What it does |
|---|---|
| `Capture to project` | Pick a project → opens it with the cursor on a fresh `- YYYY-MM-DD — ` bullet under `## Log`. Pick *➕ New note* → prompts for a title and creates a root note in `[[Inbox]]`. Esc cancels. |
| `Attach note to project` | Pick a project → writes `project: "[[Name]]"` into the frontmatter of the note you are currently reading. Nothing moves folders. |

`Attach note to project` is the fast path for clippings: read it, hit the hotkey, pick
the project, and it shows up under 🧱 Raw material on that project's desk.

## Two things worth knowing

- **The host note gets marked dirty.** Templater's "insert template" writes the
  template's output at your cursor. Both commands output the empty string, so nothing
  is inserted — but Obsidian still marks the note you ran it from as modified. That is
  expected, not a bug.
- **The project rule is written twice.** What counts as a project note (rather than a
  note *inside* one) is implemented in `projects.js` against Obsidian's metadataCache
  and in `Templates/Scripts/project-desk/view.js` against Dataview. Different APIs,
  same rule — change both. It is stated once in prose in [[Project workflow]].

Verify with `node Templates/Templater/projects.test.js`.
