---
title: "GitHub - millionco/react-doctor: Let coding agents diagnose and fix your React"
source: "https://github.com/millionco/react-doctor"
author: "github.com/millionco"
published: 
created: 2026-05-06
description: "Let coding agents diagnose and fix your React code - millionco/react-doctor"
tags:
  - to-process
  - agent-tools
---

# millionco/react-doctor


main


Go to file


Code


Open more actions menu


   ![React Doctor](https://github.com/millionco/react-doctor/raw/main/assets/react-doctor-readme-logo-light.svg) 
[![version](https://camo.githubusercontent.com/a2f20836c9a09f01be67a4c9a8612081f600d6b2f58bf9d57c8eb3d3da5dff0e/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f72656163742d646f63746f723f7374796c653d666c617426636f6c6f72413d30303030303026636f6c6f72423d303030303030)](https://npmjs.com/package/react-doctor)
[![downloads](https://camo.githubusercontent.com/10d93476c875ba85e5ae9fa3eeb183686a6c6fa6f02c2df8741c3313235ca2c5/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f64742f72656163742d646f63746f722e7376673f7374796c653d666c617426636f6c6f72413d30303030303026636f6c6f72423d303030303030)](https://npmjs.com/package/react-doctor)
Let coding agents diagnose and fix your React code.


One command scans your codebase for security, performance, correctness, and architecture issues, then outputs a **0–100 score** with actionable diagnostics.


### [See it in action →](https://react.doctor)


  Main.mp4    
## Install


Run this at your project root:



```
npx -y react-doctor@latest .
```

Use `--verbose` to see affected files and line numbers:



```
npx -y react-doctor@latest . --verbose
```

## Install as a skill


Add React Doctor's rules as a [skill](https://skills.sh) for your coding agent:



```
npx skills add millionco/react-doctor
```

This gives agents like Cursor, Claude Code, Copilot, and others access to all 47+ React best practice rules. The CLI will also prompt to install the skill on first run.


## Options



```
Usage: react-doctor [directory] [options]

Options:
  -v, --version     display the version number
  --no-lint         skip linting
  --no-dead-code    skip dead code detection
  --verbose         show file details per rule
  --score           output only the score
  -y, --yes         skip prompts, scan all workspace projects
  --project <name>  select workspace project (comma-separated for multiple)
  --fix             open Ami to auto-fix all issues
  --prompt          copy latest scan output to clipboard
  -h, --help        display help for command

```

## Node.js API


You can also use React Doctor programmatically:



```
import { diagnose } from "react-doctor/api";

const result = await diagnose("./path/to/your/react-project");

console.log(result.score); // { score: 82, label: "Good" } or null
console.log(result.diagnostics); // Array of Diagnostic objects
console.log(result.project); // Detected framework, React version, etc.
```

The `diagnose` function accepts an optional second argument:



```
const result = await diagnose(".", {
  lint: true, // run lint checks (default: true)
  deadCode: true, // run dead code detection (default: true)
});
```

Each diagnostic has the following shape:



```
interface Diagnostic {
  filePath: string;
  plugin: string;
  rule: string;
  severity: "error" | "warning";
  message: string;
  help: string;
  line: number;
  column: number;
  category: string;
}
```

## [Scores for popular open-source projects](https://react.doctor/leaderboard)




| Project | Score | Share |
| --- | --- | --- |
| [tldraw](https://github.com/tldraw/tldraw) | **84** | [view](https://www.react.doctor/share?p=tldraw&s=84&e=98&w=139&f=40) |
| [excalidraw](https://github.com/excalidraw/excalidraw) | **84** | [view](https://www.react.doctor/share?p=%40excalidraw%2Fexcalidraw&s=84&e=2&w=196&f=80) |
| [twenty](https://github.com/twentyhq/twenty) | **78** | [view](https://www.react.doctor/share?p=twenty-front&s=78&e=99&w=293&f=268) |
| [plane](https://github.com/makeplane/plane) | **78** | [view](https://www.react.doctor/share?p=web&s=78&e=7&w=525&f=292) |
| [formbricks](https://github.com/formbricks/formbricks) | **75** | [view](https://www.react.doctor/share?p=%40formbricks%2Fweb&s=75&e=15&w=389&f=242) |
| [posthog](https://github.com/PostHog/posthog) | **72** | [view](https://www.react.doctor/share?p=%40posthog%2Ffrontend&s=72&e=82&w=1177&f=585) |
| [supabase](https://github.com/supabase/supabase) | **69** | [view](https://www.react.doctor/share?p=studio&s=69&e=74&w=1087&f=566) |
| [onlook](https://github.com/onlook-dev/onlook) | **69** | [view](https://www.react.doctor/share?p=%40onlook%2Fweb-client&s=69&e=64&w=418&f=178) |
| [payload](https://github.com/payloadcms/payload) | **68** | [view](https://www.react.doctor/share?p=%40payloadcms%2Fui&s=68&e=139&w=408&f=298) |
| [sentry](https://github.com/getsentry/sentry) | **64** | [view](https://www.react.doctor/share?p=sentry&s=64&e=94&w=1345&f=818) |
| [cal.com](https://github.com/calcom/cal.com) | **63** | [view](https://www.react.doctor/share?p=%40calcom%2Fweb&s=63&e=31&w=558&f=311) |
| [dub](https://github.com/dubinc/dub) | **62** | [view](https://www.react.doctor/share?p=web&s=62&e=52&w=966&f=457) |


## Contributing


Want to contribute? Check out the codebase and submit a PR.



```
git clone https://github.com/millionco/react-doctor
cd react-doctor
pnpm install
pnpm -r run build
```

Run locally:



```
node packages/react-doctor/dist/cli.js /path/to/your/react-project
```

### License


React Doctor is MIT-licensed open-source software.