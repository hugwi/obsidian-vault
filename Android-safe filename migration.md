---
created: 2026-08-21
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - android
  - git
  - file-names
  - migration
---
# Android-safe filename migration

Android/Obsidian can reject filenames containing:

```text
" * / : < > ? \\ |
```

The remote `main` currently contains many legacy filenames using forbidden characters. The last audit found **283 tracked paths** whose filename component contains at least one of these characters. Rename them on a desktop, where all files can be checked out, then push the rename commit before syncing Android.

## Desktop procedure

1. Stop Obsidian Git automatic backup on Android and close Obsidian there.
2. On a desktop, fetch the latest branch and create a safety branch:

```bash
git fetch origin
git switch main
git pull --ff-only origin main
git switch -c chore/android-safe-filenames
```

3. Save the following as `rename-android-unsafe-files.py` in the repository root and run it:

```python
import re
import subprocess
from pathlib import PurePosixPath

FORBIDDEN = re.compile(r'["*:?<>\\|]')

paths = subprocess.check_output(["git", "ls-files", "-z"]).decode().split("\\0")
renames = []
seen = set(paths)

for path in filter(None, paths):
    posix = PurePosixPath(path)
    name = posix.name
    if not FORBIDDEN.search(name):
        continue

    safe_name = FORBIDDEN.sub("-", name)
    safe_name = re.sub(r"-{2,}", "-", safe_name).strip(" .-")
    target = str(posix.with_name(safe_name))

    if not safe_name or target in seen or target in {new for _, new in renames}:
        raise SystemExit(f"Rename collision or empty filename: {path} -> {target}")
    renames.append((path, target))

for old, new in renames:
    print(f"{old} -> {new}")

if renames:
    answer = input(f"Apply {len(renames)} renames? [y/N] ")
    if answer.lower() == "y":
        for old, new in renames:
            subprocess.run(["git", "mv", "--", old, new], check=True)
```

4. Review the printed rename list and the resulting `git status`.
5. Check that wikilinks, embeds, project properties, and clipping links still resolve. Use Obsidian’s link updater or search/replace where needed.
6. Commit and push the renames:

```bash
git add -A
git commit -m "chore: rename files for Android compatibility"
git push origin main
```

7. Sync Android only after the push succeeds.

## Ongoing prevention

- Web Clipper templates must use `safe_name` for every title-derived filename component.
- Keep the original title in note content/properties, not only in the filename.
- Agents must use only letters, numbers, spaces, hyphens, underscores, parentheses, and periods in new filenames.
- Never use raw external titles as filenames without sanitizing them first.
