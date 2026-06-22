---
title: "nedcodes-ok/rule-porter: Convert AI IDE rules between Cursor, Windsurf, CLAUDE.md,"
source: "https://github.com/nedcodes-ok/rule-porter"
author: "github.com/nedcodes-ok"
published: 
created: 2026-05-10
description: "Convert AI IDE rules between Cursor, Windsurf, CLAUDE.md, AGENTS.md, and"
tags:
  - to-process
  - agent-configuration
---

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/nedcodes-ok/rule-porter?resume=1) 


## Create list


# nedcodes-ok/rule-porter


main


tT


Go to file


Code


Open more actions menu


# rule-porter


[![Cursor Rules](https://camo.githubusercontent.com/eff8594e544a5b2f38630760aa59330d8656d7484b8d7f157753e8bbb402ad58/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f437572736f7225323052756c65732d76616c6964617465642d627269676874677265656e)](https://camo.githubusercontent.com/eff8594e544a5b2f38630760aa59330d8656d7484b8d7f157753e8bbb402ad58/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f437572736f7225323052756c65732d76616c6964617465642d627269676874677265656e)
[![npm version](https://camo.githubusercontent.com/fbda902ca643a09b417f331e3f91d7df5b1bca66e1941e3ea62eda0ee34149e2/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72756c652d706f72746572)](https://www.npmjs.com/package/rule-porter)
[![npm downloads](https://camo.githubusercontent.com/40e3828862357d4b4260cd0192d8fa56a7d16f8d1840dd9769c62a2e61809d23/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64772f72756c652d706f72746572)](https://www.npmjs.com/package/rule-porter)
[![license](https://camo.githubusercontent.com/48c6418322f280c3c6ad077de3f69821dfd9b17365a6dde9e9123d82b99d240a/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f72756c652d706f72746572)](https://github.com/nedcodes-ok/rule-porter/blob/main/LICENSE)
**Switch AI editors without rewriting all your rules.**


Convert Cursor rules to Claude Code, GitHub Copilot, Windsurf, or AGENTS.md. And back. Bidirectional. Zero dependencies.



```
npx rule-porter --to agents-md
```

## The problem


Your rules are locked into one tool's format. Cursor uses `.mdc` files with YAML frontmatter and glob patterns. Claude Code uses `CLAUDE.md`. Copilot uses `.github/copilot-instructions.md`. None of them understand each other.


## What you get



```
$ npx rule-porter --to agents-md

Converting 12 Cursor rules → AGENTS.md

  ✓ 9 rules converted cleanly
  ⚠ 3 rules had glob patterns (preserved as comments)

Written: AGENTS.md

```

Converting back works too:



```
npx rule-porter --from agents-md --to cursor
# → 12 individual .mdc files with frontmatter and globs restored
```

## Supported formats




| Format | Read | Write | File |
| --- | --- | --- | --- |
| Cursor | ✅ | ✅ | `.cursor/rules/*.mdc` |
| Cursor (legacy) | ✅ | — | `.cursorrules` |
| AGENTS.md | ✅ | ✅ | `AGENTS.md` |
| Claude Code | ✅ | ✅ | `CLAUDE.md` |
| GitHub Copilot | ✅ | ✅ | `.github/copilot-instructions.md` |
| Windsurf | ✅ | ✅ | `.windsurfrules` |


## Common conversions



```
# Cursor → other formats
npx rule-porter --to agents-md
npx rule-porter --to claude-md
npx rule-porter --to copilot
npx rule-porter --to windsurf

# Other formats → Cursor
npx rule-porter --from agents-md --to cursor
npx rule-porter --from claude-md --to cursor

# Between any two formats
npx rule-porter --from agents-md --to claude-md

# Migrate legacy .cursorrules to .mdc
npx rule-porter --from cursorrules-legacy --to cursor

# Preview without writing
npx rule-porter --to agents-md --dry-run
```

## What converts cleanly


* Rule names, descriptions, and body content
* Global vs conditional rule separation
* `alwaysApply` rules become top-level sections
* Globs are restored when converting back to Cursor


## What gets flagged


* **Glob patterns** become comments in flat formats (markdown doesn't support file scoping)
* **Manual-attach rules** (no globs, not alwaysApply) get flagged for review
* **No silent data loss.** Every non-1:1 conversion produces a warning.


## Options



```
--to <format>       Target format (required)
--from <format>     Source format (default: auto-detect)
--out <path>        Output file path
--dry-run           Preview without writing

```

## Next step: check your converted rules


After converting, make sure they actually work:



```
npx cursor-doctor scan    # Health check with letter grade
npx cursor-doctor lint    # Detailed rule-by-rule linting
```

**[cursor-doctor](https://github.com/nedcodes-ok/cursor-doctor)** catches broken frontmatter, conflicting instructions, and 100+ other issues. Also: **[rule-gen](https://github.com/nedcodes-ok/rule-gen)** generates rules from your codebase using AI. `npx rulegen-ai`


## License


MIT