# truecourse-ai/truecourse: AI-powered architecture analysis and code intelligence. Detects circular deps, layer violations, dead modules, and more. Web UI + CLI.

![rw-book-cover](https://opengraph.githubassets.com/5a652e14469ac57f082089b355c559e1428eacc85aa34b93b098d137e0439189/truecourse-ai/truecourse)

## Metadata
- Author: [[https://github.com/truecourse-ai/]]
- Full Title: truecourse-ai/truecourse: AI-powered architecture analysis and code intelligence. Detects circular deps, layer violations, dead modules, and more. Web UI + CLI.
- Category: #articles
- Summary: TrueCourse is an AI tool that analyzes code architecture and quality to find hidden problems like circular dependencies and security risks. It uses many rules and AI to give clear reports and fix suggestions through a web UI or command line. The tool supports JavaScript, TypeScript, and Python, and helps teams keep code reliable and safe.
- URL: https://github.com/truecourse-ai/truecourse

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/truecourse-ai/truecourse?resume=1) 

#### Create list

### truecourse-ai/truecourse

main

tT

Go to file

Code

Open more actions menu

[![TrueCourse](https://github.com/truecourse-ai/truecourse/raw/main/assets/logo.svg)](https://github.com/truecourse-ai/truecourse/blob/main/assets/logo.svg)
**AI Architecture & Code Intelligence Platform**

*1,200+ deterministic rules, 100 LLM rules. JavaScript, TypeScript, Python.*

[![Tests](https://github.com/truecourse-ai/truecourse/actions/workflows/test.yml/badge.svg)](https://github.com/truecourse-ai/truecourse/actions/workflows/test.yml)
[![npm version](https://camo.githubusercontent.com/6535bf466461ea7b6b1f4eef50b79d167e23056538984fe0e9f3ca115f6b136e/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f74727565636f75727365)](https://www.npmjs.com/package/truecourse)
[![License](https://camo.githubusercontent.com/b126fab1d0daea05ab1213025ab928ff91f5b4befa1078674f51d1337de76fc6/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f74727565636f757273652d61692f74727565636f75727365)](https://github.com/truecourse-ai/truecourse/blob/main/LICENSE)
TrueCourse analyzes your codebase architecture and code to detect violations that traditional linters miss — circular dependencies, layer violations, dead modules, race conditions, security anti-patterns, and more. It combines tree-sitter static analysis with LLM-powered review to surface findings with fix suggestions.

[![TrueCourse Screenshot](https://github.com/truecourse-ai/truecourse/raw/main/assets/demo.gif)](https://github.com/truecourse-ai/truecourse/blob/main/assets/demo.gif)
  [![TrueCourse Screenshot](https://github.com/truecourse-ai/truecourse/raw/main/assets/demo.gif)](https://github.com/truecourse-ai/truecourse/blob/main/assets/demo.gif)  

#### What it catches

**Architecture** — Circular dependencies, layer violations, god modules, dead modules, tight coupling, cross-service imports

**Code quality** — Magic numbers, empty catch, console.log, cognitive complexity, unused variables, redundant code, missing type hints

**Security** — SQL injection, hardcoded secrets, eval usage, insecure random, XSS, path traversal, unsafe deserialization

**Bugs** — Race conditions, type mismatches, mutable defaults, implicit optional, off-by-one, unchecked returns

**Performance** — N+1 queries, O(n²) string concat, unnecessary allocations, missing pagination, sync I/O in async

**Reliability** — Unhandled promises, resource leaks, missing timeouts, swallowed exceptions, unsafe error handling

**Database** — Missing indexes, missing transactions, lazy loading in loops, raw SQL bypassing ORM, schema issues

**Style** — Import ordering, naming conventions, docstring completeness, formatting preferences

#### Quick Start

```
cd <your-repo>
npx truecourse analyze      # Runs the full analysis in-process
npx truecourse dashboard    # Opens the web UI in your browser
```

No setup step. TrueCourse creates `.truecourse/` in your repo on first analyze and stores everything there as plain JSON files — no database, no daemon.

TrueCourse uses the [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) for LLM-powered rules. If `claude` isn't on your PATH, deterministic rules still run and LLM rules are skipped.

#### CLI Commands

```
# Analysis
truecourse analyze                    # Analyze current repo (prompts before stashing dirty trees)
truecourse analyze --stash            # Pre-approve stashing pending changes (CI-friendly)
truecourse analyze --no-stash         # Analyze working tree as-is, no stash
truecourse analyze --diff             # New/resolved violations from your uncommitted changes
truecourse list                       # Show violations from latest analysis
truecourse list --all                 # Show all violations (no pagination)
truecourse list --diff                # Show diff check results
truecourse add                        # Register repo without analyzing

# Dashboard (web UI)
truecourse dashboard                  # Start + open the dashboard
truecourse dashboard --reconfigure    # Re-prompt for console vs background service mode
truecourse dashboard stop             # Stop the dashboard
truecourse dashboard status           # Show dashboard status
truecourse dashboard logs             # Tail dashboard logs (service mode only)
truecourse dashboard uninstall        # Remove the background service
```

##### Rules

Configure which rule categories and LLM-powered rules are enabled per repository:

```
# Categories
truecourse rules categories                    # Show enabled/disabled
truecourse rules categories --enable style     # Enable a category
truecourse rules categories --disable style    # Disable a category

# LLM-powered rules
truecourse rules llm                           # Show LLM rules status
truecourse rules llm --enable                  # Enable LLM rules
truecourse rules llm --disable                 # Disable LLM rules
```

##### Git Hooks

TrueCourse can install a pre-commit hook that blocks commits introducing new violations at or above a configured severity:

```
truecourse hooks install              # Install pre-commit hook
truecourse hooks uninstall            # Remove pre-commit hook
truecourse hooks status               # Show hook status + config
```

On every commit the hook runs `truecourse analyze --diff` against the repo's last full analysis and blocks if any newly-introduced violation matches the configured block severities. **Commits will take as long as a full diff analysis** — on large repos that can be tens of seconds per commit. `truecourse hooks install` warns you and requires confirmation before writing the hook.

**First-time setup:** run `truecourse analyze` once to establish a baseline. Without it the hook can't diff.

**Bypass:** `git commit --no-verify` (standard git).

**Configuration** — `hooks install` seeds `<repo>/.truecourse/hooks.yaml` with starter defaults; commit the file so your team shares one policy. The hook reads only from this file — if you delete it, the hook warns and passes every commit (no hidden code-level defaults). Current shape:

```
pre-commit:
  block-on: [critical, high]   # severities. Valid: info|low|medium|high|critical
  llm: false                   # run LLM rules on every commit (tokens per commit)
```

##### Telemetry

TrueCourse collects anonymous usage data to improve the product. It is automatically disabled in CI environments.

```
truecourse telemetry status           # Check telemetry status
truecourse telemetry disable          # Opt out of anonymous telemetry
truecourse telemetry enable           # Opt back in
```

#### Analysis Rules

TrueCourse ships with **1,200+ deterministic rules** and **100 LLM rules** across 8 categories:

| Category | Deterministic | LLM | Total |
| --- | --- | --- | --- |
| Security | 150+ | 1 | 150+ |
| Bugs | 250+ | 4 | 250+ |
| Architecture | 30+ | 7 | 40+ |
| Code Quality | 500+ | 3 | 500+ |
| Performance | 50+ | 10 | 60+ |
| Reliability | 40+ | 10 | 50+ |
| Database | 30+ | 5 | 35+ |
| Style | 50+ | — | 50+ |

**Deterministic rules** run via tree-sitter AST visitors — fast, zero-cost, no API calls.

**LLM rules** send source code to the configured LLM for semantic analysis — deeper but requires an LLM provider.

#### Claude Code Skills

TrueCourse includes [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills) for conversational analysis from within Claude Code.

The first `truecourse analyze` (or `truecourse add`) in a fresh repo asks whether to install skills into `.claude/skills/truecourse/`. Re-runs skip the prompt if skills are already present. Pass `--install-skills` / `--no-skills` to bypass the prompt explicitly.

| Skill | What it does |
| --- | --- |
| `/truecourse-analyze` | Runs analysis or diff check, summarizes results |
| `/truecourse-list` | Shows full violation details |
| `/truecourse-fix` | Lists fixable violations, applies changes |
| `/truecourse-hooks` | Installs, configures, or removes the pre-commit hook |

#### Language Support

| Language | Status |
| --- | --- |
| JavaScript / TypeScript | Supported |
| Python | Supported |
| C# | Planned |
| Go | Planned |
| Rust | Planned |
| PHP | Planned |

#### Prerequisites

* Node.js >= 20
* [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI on your PATH. Deterministic rules run without it, LLM-powered rules need it.

#### Configuration

TrueCourse talks to Claude Code via the `claude` CLI. You can tune how that interaction behaves — which binary to invoke, which model to pass, timeouts, retries, and how many `claude` processes to run in parallel — through environment variables.

For packaged installs (`npx truecourse` or `npm install -g truecourse`), the simplest place to set them is `~/.truecourse/.env`. The file is loaded automatically on every invocation:

```
CLAUDE_CODE_BINARY=claude             # override the `claude` binary on PATH
CLAUDE_CODE_MODEL=                    # Claude Code --model flag (empty = default)
CLAUDE_CODE_TIMEOUT_MS=120000         # per-call timeout (ms)
CLAUDE_CODE_MAX_RETRIES=2             # retry attempts on parse/validation failure
CLAUDE_CODE_MAX_CONCURRENCY=10        # max concurrent `claude` processes per run

```

**`CLAUDE_CODE_MAX_CONCURRENCY`** caps how many Claude CLI processes TrueCourse spawns in parallel during a single analyze. Default `10`. Raise it on CI runners with spare headroom; lower it on resource-constrained machines (e.g. 8 GB laptops, shared VMs) to avoid OOM on large repos. Must be a positive integer.

For a one-off override, prefix the command:

```
CLAUDE_CODE_MAX_CONCURRENCY=2 truecourse analyze
```

##### Excluding files from analysis

TrueCourse honors `.gitignore` automatically (including nested `.gitignore` files, `.git/info/exclude`, and your configured global excludes file).

For paths you want tracked in git but not analyzed — generated code, vendored snapshots, large fixtures — add a `.truecourseignore` at the repo root. Same syntax as `.gitignore`:

```
# generated
src/generated/
# vendored
third_party/
# specific files
scripts/ingest-epub.js

```

Patterns are anchored to the file's location, so `src/generated/` matches the top-level directory only; use `**/generated/` to match at any depth.

#### Development

```
git clone https://github.com/truecourse-ai/truecourse.git
cd truecourse
pnpm install
pnpm dev                # Start dashboard at http://localhost:3000 (server on :3001, Vite on :3000)
pnpm test               # Run tests
pnpm build              # Build all packages
```

`pnpm dev` expects a `.truecourse/` folder at the repo root — created automatically on the first `truecourse analyze` against the repo (or simply `mkdir -p .truecourse`).

#### Telemetry

TrueCourse collects anonymous usage data (event type, language, file count range, OS). No source code, file paths, or violation details are collected. Opt out with `truecourse telemetry disable` or `TRUECOURSE_TELEMETRY=0`.

#### Contact

Questions, feedback, or security reports: **Mushegh Gevorgyan** — [mushegh@truecourse.dev](mailto:mushegh@truecourse.dev).

#### License

MIT
