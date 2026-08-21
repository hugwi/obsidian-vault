---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - harness
  - skills
source: readwise
created: 2026-06-23
rating: 
action: 
theme: multi-agent-orchestration
subtheme:
  - skill-tool-extension
---

# agent-stuff/skills/web-browser/SKILL.md at main · mitsuhiko/agent-stuff · GitHub

![rw-book-cover](https://opengraph.githubassets.com/70d3ffe1d1cfe5825539d0e9d571e3818fac0b4477b4d2106af04456af251a62/mitsuhiko/agent-stuff)

## Metadata
- Author: [[https://github.com/mitsuhiko/]]
- Full Title: agent-stuff/skills/web-browser/SKILL.md at main · mitsuhiko/agent-stuff · GitHub
- Category: #articles
- Summary: The web-browser skill lets Claude control Chrome or Chromium to browse web pages by clicking, filling forms, and navigating links. It uses Chrome DevTools Protocol and includes tools to start the browser, run JavaScript, take screenshots, and handle cookie dialogs. It also supports logging network activity and interactive element picking for easy site exploration.
- URL: https://github.com/mitsuhiko/agent-stuff/blob/main/skills/web-browser/SKILL.md

## Full Document
#### FilesExpand file tree

main

BlameMore file actions

BlameMore file actions

main

Top

| name | description | license |
| --- | --- | --- |
| web-browser | Allows to interact with web pages by performing actions such as clicking buttons, filling out forms, and navigating links. It works by remote controlling Google Chrome or Chromium browsers using the Chrome DevTools Protocol (CDP). When Claude needs to browse the web, it can use this skill to do so. | Stolen from Mario |

### Web Browser Skill

Minimal CDP tools for collaborative site exploration.

#### Start Chrome

```
./scripts/start.js              # Fresh profile
./scripts/start.js --profile    # Copy your profile (cookies, logins)
```

Start Chrome on `:9222` with remote debugging.

#### Navigate

```
./scripts/nav.js https://example.com
./scripts/nav.js https://example.com --new
```

Navigate current tab or open new tab.

#### Evaluate JavaScript

```
./scripts/eval.js 'document.title'
./scripts/eval.js 'document.querySelectorAll("a").length'
./scripts/eval.js 'JSON.stringify(Array.from(document.querySelectorAll("a")).map(a => ({ text: a.textContent.trim(), href: a.href })).filter(link => !link.href.startsWith("https://")))'
```

Execute JavaScript in active tab (async context). Be careful with string escaping, best to use single quotes.

#### Screenshot

```
./scripts/screenshot.js
```

Screenshot current viewport, returns temp file path

#### Pick Elements

```
./scripts/pick.js "Click the submit button"
```

Interactive element picker. Click to select, Cmd/Ctrl+Click for multi-select, Enter to finish.

#### Dismiss Cookie Dialogs

```
./scripts/dismiss-cookies.js          # Accept cookies
./scripts/dismiss-cookies.js --reject # Reject cookies (where possible)
```

Automatically dismisses EU cookie consent dialogs.

Run after navigating to a page:

```
./scripts/nav.js https://example.com && ./scripts/dismiss-cookies.js
```

#### Background Logging (Console + Errors + Network)

Automatically started by `start.js` and writes JSONL logs to:

```
~/.cache/agent-web/logs/YYYY-MM-DD/<targetId>.jsonl

```

Manually start:

```
./scripts/watch.js
```

Tail latest log:

```
./scripts/logs-tail.js           # dump current log and exit
./scripts/logs-tail.js --follow  # keep following
```

Summarize network responses:

```
./scripts/net-summary.js
```
