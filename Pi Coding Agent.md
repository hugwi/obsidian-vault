---
categories:
  - "[[Resources]]"
domain: engineering
title: "Pi Coding Agent"
source: "https://pi.dev/packages/@tifan/pi-inline-skills?name=inline"
author:
published:
created: 2026-06-10
description: "A terminal-based coding agent"
tags:
  - "to-process"
  - agent-tools
---
extension

Install `@tifan/pi-inline-skills` from npm and Pi will load the resources declared by the package manifest.

`$ pi install npm:@tifan/pi-inline-skills`

Package

`@tifan/pi-inline-skills`

Version

`1.0.3`

Published

Jun 5, 2026

Downloads

784/mo · 399/wk

Author

tifan

License

MIT

Types

extension

Size

16.5 KB

Dependencies

0 dependencies · 0 peers

Pi manifest JSON
```prolog
{
  "extensions": [
    "./src/index.ts"
  ]
}
```

## @tifan/pi-inline-skills

Load multiple skills from inside your prompt.

`pi-inline-skills` adds `/skill` autocomplete to the pi editor. Type `/` with part of a skill name, choose one or more matches, and keep writing. When you submit, the extension tells pi to load those skills for that turn.

![Inline skill autocomplete picker](https://raw.githubusercontent.com/tifandotme/pi-extensions/refs/heads/master/packages/pi-inline-skills/assets/skills-selector-triggered-inline.webp)

## Install

```bash
pi install npm:@tifan/pi-inline-skills
```

## How it works

- Type `/` followed by part of a skill name to open the picker.
- Choose one or more skills while writing your prompt.
- On submit, each `/name` token is replaced with the skill name, and one instruction to load the matching skills is added behind the scenes.
- Skills read during the session are tracked, so they are not loaded again.
- If the prompt starts with a registered pi command, that command wins. Otherwise, a starting token like `/tdd` is treated as an inline skill.

## Commands

- `/loaded-skills`: List skills loaded in the current session.

## Example

Typing this:

```fsharp
let's /tdd this and /review when done
```

submits the prompt with `tdd` and `review` selected as skills to load. The visible message stays readable, and the load instruction is handled outside your prompt text.

![Loaded skills command output](https://raw.githubusercontent.com/tifandotme/pi-extensions/refs/heads/master/packages/pi-inline-skills/assets/loaded-skills-output.webp)

Use `/loaded-skills` to see which skills have already been read in the current session.

## Release notes

See [CHANGELOG.md](https://cdn.jsdelivr.net/npm/@tifan/pi-inline-skills@1.0.3/CHANGELOG.md)

## License

[MIT](https://cdn.jsdelivr.net/npm/@tifan/pi-inline-skills@1.0.3/LICENSE)