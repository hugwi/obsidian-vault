# caliber-ai-org/ai-setup: Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files for Claude Code, Cursor, and Codex.

![rw-book-cover](https://repository-images.githubusercontent.com/1178198291/70be5bf9-076a-49fc-aaa7-07cdab8ee077)

## Metadata
- Author: [[https://github.com/caliber-ai-org/]]
- Full Title: caliber-ai-org/ai-setup: Continuously sync your AI setups with one command. Codebase tailor suited agent skills, MCPs and config files for Claude Code, Cursor, and Codex.
- Category: #articles
- Summary: Caliber is a tool that keeps AI setup files accurate and in sync as your code changes. It works with many AI coding tools like Claude Code, Cursor, and GitHub Copilot. Caliber audits, improves, and updates configs automatically without overwriting your work.
- URL: https://github.com/caliber-ai-org/ai-setup

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/caliber-ai-org/ai-setup?resume=1) 

#### Create list

### caliber-ai-org/ai-setup

master

tT

Go to file

Code

Open more actions menu

### Caliber

**Hand-written `CLAUDE.md` files go stale the moment you refactor.** Your AI agent hallucinates paths that no longer exist, misses new dependencies, and gives advice based on yesterday's architecture. Caliber generates and maintains your AI context files (`CLAUDE.md`, `.cursor/rules/`, `AGENTS.md`, `copilot-instructions.md`) so they stay accurate as your code evolves — and keeps every agent on your team in sync, whether they use Claude Code, Cursor, Codex, OpenCode, or GitHub Copilot.

[![Caliber product demo](https://github.com/caliber-ai-org/ai-setup/raw/master/assets/demo-header.gif)](https://github.com/caliber-ai-org/ai-setup/blob/master/assets/demo-header.gif)
  [![Caliber product demo](https://github.com/caliber-ai-org/ai-setup/raw/master/assets/demo-header.gif)](https://github.com/caliber-ai-org/ai-setup/blob/master/assets/demo-header.gif)  

[![npm version](https://camo.githubusercontent.com/fa3eaef1e6a79ab26728cb8c810dbe1b34d7b5ce27a9aa7d19db4951f2707231/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f4072656c792d61692f63616c69626572)](https://www.npmjs.com/package/@rely-ai/caliber)
[![license](https://camo.githubusercontent.com/9345b7376f5e8bc9c93a223a2d70090f24798d453446bf730e8833935e433a64/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f6c2f4072656c792d61692f63616c69626572)](https://github.com/caliber-ai-org/ai-setup/blob/master/LICENSE)
[![node](https://camo.githubusercontent.com/b38a4b3f6efbd6065f8d124cac2e47590f5d0a9321d087861309497abec2b432/68747470733a2f2f696d672e736869656c64732e696f2f6e6f64652f762f4072656c792d61692f63616c69626572)](https://nodejs.org)
[![Caliber Score](https://camo.githubusercontent.com/08f10330f06cf024e51511175509d708e49a8f7c465310e17375d6cf14ba59b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f63616c696265722d39342532463130302d627269676874677265656e)](https://camo.githubusercontent.com/08f10330f06cf024e51511175509d708e49a8f7c465310e17375d6cf14ba59b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f63616c696265722d39342532463130302d627269676874677265656e)
[![Claude Code](https://camo.githubusercontent.com/d8b7717d3c1ed886282d6323fecefeec18e6f6d76c5ba2304b3b513a2c84645b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436c617564655f436f64652d737570706f727465642d626c7565)](https://camo.githubusercontent.com/d8b7717d3c1ed886282d6323fecefeec18e6f6d76c5ba2304b3b513a2c84645b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436c617564655f436f64652d737570706f727465642d626c7565)
[![Cursor](https://camo.githubusercontent.com/d87381c63c80fc7fc2ca4573d097ba72e5da76fc5cb77b766efb15dbcc718940/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f437572736f722d737570706f727465642d626c7565)](https://camo.githubusercontent.com/d87381c63c80fc7fc2ca4573d097ba72e5da76fc5cb77b766efb15dbcc718940/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f437572736f722d737570706f727465642d626c7565)
[![Codex](https://camo.githubusercontent.com/67e8c292a7f261466ba515ff2b4ed9161325e6b8aa7c7da44357d484127e706d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d737570706f727465642d626c7565)](https://camo.githubusercontent.com/67e8c292a7f261466ba515ff2b4ed9161325e6b8aa7c7da44357d484127e706d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f6465782d737570706f727465642d626c7565)
[![OpenCode](https://camo.githubusercontent.com/54999cb0d15fa45aa1dc914530b236e7be403fbffa68398f4c9534866a42f298/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f70656e436f64652d737570706f727465642d626c7565)](https://camo.githubusercontent.com/54999cb0d15fa45aa1dc914530b236e7be403fbffa68398f4c9534866a42f298/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4f70656e436f64652d737570706f727465642d626c7565)
[![GitHub Copilot](https://camo.githubusercontent.com/f1305b06d3111f0231267a1ed0e278f298237add376ddf3a2aa2db3c761f9119/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875625f436f70696c6f742d737570706f727465642d626c7565)](https://camo.githubusercontent.com/f1305b06d3111f0231267a1ed0e278f298237add376ddf3a2aa2db3c761f9119/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875625f436f70696c6f742d737570706f727465642d626c7565)
#### Before / After

Most repos start with a hand-written `CLAUDE.md` and nothing else. Here's what Caliber finds — and fixes:

```
  Before                                    After /setup-caliber
  ──────────────────────────────            ──────────────────────────────

  Agent Config Score    35 / 100            Agent Config Score    94 / 100
  Grade D                                   Grade A

  FILES & SETUP           6 / 25            FILES & SETUP          24 / 25
  QUALITY                12 / 25            QUALITY                22 / 25
  GROUNDING               7 / 20            GROUNDING              19 / 20
  ACCURACY                5 / 15            ACCURACY               13 / 15
  FRESHNESS               5 / 10            FRESHNESS              10 / 10
  BONUS                   0 / 5             BONUS                   5 / 5

```

Scoring is deterministic — no LLM, no API calls. It cross-references your config files against your actual project filesystem: do referenced paths exist? Are code blocks present? Is there config drift since your last commit?

```
caliber score --compare main    # See how your branch changed the score
```

#### Get Started

Requires **Node.js >= 20**.

```
npx @rely-ai/caliber bootstrap
```

Then, in your terminal (not the IDE chat), start a Claude Code or Cursor CLI session and type:

>  **/setup-caliber**
> 
>  

Your agent detects your stack, generates tailored configs for every platform your team uses, sets up pre-commit hooks, and enables continuous sync — all from inside your normal workflow.

**Don't use Claude Code or Cursor?** Run `caliber init` instead — it's the same setup as a CLI wizard. Works with any LLM provider: bring your own Anthropic, OpenAI, or Vertex AI key.

>  **Your code stays on your machine.** Bootstrap is 100% local — no LLM calls, no code sent anywhere. Generation uses your own AI subscription or API key. Caliber never sees your code.
> 
>  

 **Windows Users** Caliber works on Windows with a few notes:

 * **Run from your terminal** (PowerShell, CMD, or Git Bash) — not from inside an IDE chat window. Open a terminal, `cd` into your project folder, then run `npx @rely-ai/caliber bootstrap`.
* **Git Bash is recommended.** Caliber's pre-commit hooks and auto-sync scripts use shell syntax. Git for Windows includes Git Bash, which handles this automatically. If you only use PowerShell, hooks may be skipped silently.
* **Cursor Agent CLI:** If prompted to install it, download from [cursor.com/downloads](https://www.cursor.com/downloads) instead of the `curl | bash` command shown on macOS/Linux. Then run `agent login` in your terminal to authenticate.
* **One terminal at a time.** Avoid running Caliber from multiple terminals simultaneously — this can cause conflicting state and unexpected provider detection.

 
#### Audits first, writes second

Caliber never overwrites your existing configs without asking. The workflow mirrors code review:

1. **Score** — read-only audit of your current setup
2. **Propose** — generate or improve configs, shown as a diff
3. **Review** — accept, refine via chat, or decline each change
4. **Backup** — originals saved to `.caliber/backups/` before every write
5. **Undo** — `caliber undo` restores everything to its previous state

If your existing config scores **95+**, Caliber skips full regeneration and applies targeted fixes to the specific checks that are failing.

#### How It Works

Bootstrap gives your agent the `/setup-caliber` skill. Your agent analyzes your project — languages, frameworks, dependencies, architecture — generates configs, and installs hooks. From there, it's a loop:

```
  npx @rely-ai/caliber bootstrap       ← one-time, 2 seconds
              │
              ▼
  agent runs /setup-caliber             ← agent handles everything
              │
              ▼
  ┌──── configs generated ◄────────────┐
  │           │                        │
  │           ▼                        │
  │     your code evolves              │
  │     (new deps, renamed files,      │
  │      changed architecture)         │
  │           │                        │
  │           ▼                        │
  └──► caliber refresh ──────────────►─┘
       (auto, on every commit)

```

Pre-commit hooks run the refresh loop automatically. New team members get nudged to bootstrap on their first session.

##### What It Generates

**Claude Code**

* `CLAUDE.md` — Project context, build/test commands, architecture, conventions
* `CALIBER_LEARNINGS.md` — Patterns learned from your AI coding sessions
* `.claude/skills/*/SKILL.md` — Reusable skills ([OpenSkills](https://agentskills.io) format)
* `.mcp.json` — Auto-discovered MCP server configurations
* `.claude/settings.json` — Permissions and hooks

**Cursor**

* `.cursor/rules/*.mdc` — Modern rules with frontmatter (description, globs, alwaysApply)
* `.cursor/skills/*/SKILL.md` — Skills for Cursor
* `.cursor/mcp.json` — MCP server configurations

**OpenAI Codex**

* `AGENTS.md` — Project context for Codex
* `.agents/skills/*/SKILL.md` — Skills for Codex

**OpenCode**

* `AGENTS.md` — Project context (shared with Codex when both are targeted)
* `.opencode/skills/*/SKILL.md` — Skills for OpenCode

**GitHub Copilot**

* `.github/copilot-instructions.md` — Project context for Copilot

#### Key Features

 **Any Codebase** TypeScript, Python, Go, Rust, Java, Ruby, Terraform, and more. Language and framework detection is fully LLM-driven — no hardcoded mappings. Caliber works on any project.

 
 **Any AI Tool** `caliber bootstrap` auto-detects which agents you have installed. For manual control:

 
```
caliber init --agent claude        # Claude Code only
caliber init --agent cursor        # Cursor only
caliber init --agent codex         # Codex only
caliber init --agent opencode        # OpenCode only
caliber init --agent github-copilot  # GitHub Copilot only
caliber init --agent all             # All platforms
caliber init --agent claude,cursor   # Comma-separated
```
 
 **Chat-Based Refinement** Not happy with the generated output? During review, refine via natural language — describe what you want changed and Caliber iterates until you're satisfied.

 
 **MCP Server Discovery** Caliber detects the tools your project uses (databases, APIs, services) and auto-configures matching MCP servers for Claude Code and Cursor.

 
 **Deterministic Scoring** `caliber score` evaluates your config quality without any LLM calls — purely by cross-referencing config files against your actual project filesystem.

 

| Category | Points | What it checks |
| --- | --- | --- |
| **Files & Setup** | 25 | Config files exist, skills present, MCP servers, cross-platform parity |
| **Quality** | 25 | Code blocks, concise token budget, concrete instructions, structured headings |
| **Grounding** | 20 | Config references actual project directories and files |
| **Accuracy** | 15 | Referenced paths exist on disk, config freshness vs. git history |
| **Freshness & Safety** | 10 | Recently updated, no leaked secrets, permissions configured |
| **Bonus** | 5 | Auto-refresh hooks, AGENTS.md, OpenSkills format |

 Every failing check includes structured fix data — when `caliber init` runs, the LLM receives exactly what's wrong and how to fix it.

 
 **Session Learning** Caliber watches your AI coding sessions and learns from them. Hooks capture tool usage, failures, and your corrections — then an LLM distills operational patterns into `CALIBER_LEARNINGS.md`.

 
```
caliber learn install      # Install hooks for Claude Code and Cursor
caliber learn status       # View hook status, event count, and ROI summary
caliber learn finalize     # Manually trigger analysis (auto-runs on session end)
caliber learn remove       # Remove hooks
```
 Learned items are categorized by type — **[correction]**, **[gotcha]**, **[fix]**, **[pattern]**, **[env]**, **[convention]** — and automatically deduplicated.

 
 **Auto-Refresh** Keep configs in sync with your codebase automatically:

 

| Hook | Trigger | What it does |
| --- | --- | --- |
| **Git pre-commit** | Before each commit | Refreshes docs and stages updated files |
| **Claude Code session end** | End of each session | Runs `caliber refresh` and updates docs |
| **Learning hooks** | During each session | Captures events for session learning |

 
```
caliber hooks --install    # Enable refresh hooks
caliber hooks --remove     # Disable refresh hooks
```
 The `refresh` command analyzes your git diff (committed, staged, and unstaged changes) and updates config files to reflect what changed.

 
 **Team Onboarding** When Caliber is set up in a repo, it automatically nudges new team members to configure it on their machine. A lightweight session hook checks whether the pre-commit hook is installed and prompts setup if not — no manual coordination needed.

 
 **Fully Reversible** * **Automatic backups** — originals saved to `.caliber/backups/` before every write
* **Score regression guard** — if a regeneration produces a lower score, changes are auto-reverted
* **Full undo** — `caliber undo` restores everything to its previous state
* **Clean uninstall** — `caliber uninstall` removes everything Caliber added (hooks, generated sections, skills, learnings) while preserving your own content
* **Dry run** — preview changes with `--dry-run` before applying

 
#### Commands

| Command | Description |
| --- | --- |
| `caliber bootstrap` | Install agent skills — the fastest way to get started |
| `caliber init` | Full setup wizard — analyze, generate, review, install hooks |
| `caliber score` | Score config quality (deterministic, no LLM) |
| `caliber score --compare <ref>` | Compare current score against a git ref |
| `caliber regenerate` | Re-analyze and regenerate configs (aliases: `regen`, `re`) |
| `caliber refresh` | Update docs based on recent code changes |
| `caliber skills` | Discover and install community skills |
| `caliber learn` | Session learning — install hooks, view status, finalize analysis |
| `caliber hooks` | Manage auto-refresh hooks |
| `caliber config` | Configure LLM provider, API key, and model |
| `caliber status` | Show current setup status |
| `caliber uninstall` | Remove all Caliber resources from a project |
| `caliber undo` | Revert all changes made by Caliber |

#### FAQ

 **Does it overwrite my existing configs?** No. Caliber shows you a diff of every proposed change. You accept, refine, or decline each one. Originals are backed up automatically.

 
 **Does it need an API key?** **Bootstrap & scoring:** No. Both run 100% locally with no LLM.

 **Generation** (via `/setup-caliber` or `caliber init`): Uses your existing Claude Code or Cursor subscription (no API key needed), or bring your own key for Anthropic, OpenAI, or Vertex AI.

 
 **What's the difference between bootstrap and init?** `caliber bootstrap` installs agent skills in 2 seconds — your agent then runs `/setup-caliber` to handle the rest from inside your session. `caliber init` is the full interactive wizard for users who prefer a CLI-driven setup. Both end up in the same place.

 
 **What if I don't like what it generates?** Refine it via chat during review, or decline the changes entirely. If you already accepted, `caliber undo` restores everything. You can also preview with `--dry-run`.

 
 **Does it work with monorepos?** Yes. Run `caliber init` from any directory. `caliber refresh` can update configs across multiple repos when run from a parent directory.

 
 **Does it send my code anywhere?** Scoring is fully local. Generation sends a project summary (languages, structure, dependencies — not source code) to whatever LLM provider you configure — the same provider your AI editor already uses. Anonymous usage analytics (command names, durations — no code, no file contents) are collected via PostHog. To opt out:

 * **Per-run**: `caliber --no-traces <command>`
* **Persistent env var**: `export CALIBER_TELEMETRY_DISABLED=1`

 
#### LLM Providers

No API key? No problem. Caliber works with your existing AI tool subscription:

| Provider | Setup | Default Model |
| --- | --- | --- |
| **Claude Code** (your seat) | `caliber config` → Claude Code | Inherited from Claude Code |
| **Cursor** (your seat) | `caliber config` → Cursor | Inherited from Cursor |
| **Anthropic** | `export ANTHROPIC_API_KEY=sk-ant-...` | `claude-sonnet-4-6` |
| **OpenAI** | `export OPENAI_API_KEY=sk-...` | `gpt-5.4-mini` |
| **Vertex AI** | `export VERTEX_PROJECT_ID=my-project` | `claude-sonnet-4-6` |
| **Custom endpoint** | `OPENAI_API_KEY` + `OPENAI_BASE_URL` | `gpt-5.4-mini` |

Override the model for any provider: `export CALIBER_MODEL=<model-name>` or use `caliber config`.

Caliber uses a **two-tier model system** — lightweight tasks (classification, scoring) auto-use a faster model, while heavy tasks (generation, refinement) use the default. This keeps costs low and speed high.

Configuration is stored in `~/.caliber/config.json` with restricted permissions (`0600`). API keys are never written to project files.

 Vertex AI advanced setup 
```
# Custom region
export VERTEX_PROJECT_ID=my-gcp-project
export VERTEX_REGION=europe-west1

# Service account credentials (inline JSON)
export VERTEX_PROJECT_ID=my-gcp-project
export VERTEX_SA_CREDENTIALS='{"type":"service_account",...}'

# Service account credentials (file path)
export VERTEX_PROJECT_ID=my-gcp-project
export GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
```
 
 Environment variables reference 

| Variable | Purpose |
| --- | --- |
| `ANTHROPIC_API_KEY` | Anthropic API key |
| `OPENAI_API_KEY` | OpenAI API key |
| `OPENAI_BASE_URL` | Custom OpenAI-compatible endpoint |
| `VERTEX_PROJECT_ID` | GCP project ID for Vertex AI |
| `VERTEX_REGION` | Vertex AI region (default: `us-east5`) |
| `VERTEX_SA_CREDENTIALS` | Service account JSON (inline) |
| `GOOGLE_APPLICATION_CREDENTIALS` | Service account JSON file path |
| `CALIBER_USE_CLAUDE_CLI` | Use Claude Code CLI (`1` to enable) |
| `CALIBER_USE_CURSOR_SEAT` | Use Cursor subscription (`1` to enable) |
| `CALIBER_MODEL` | Override model for any provider |
| `CALIBER_FAST_MODEL` | Override fast model for any provider |

 
#### Contributing

See [CONTRIBUTING.md](https://github.com/caliber-ai-org/ai-setup/blob/master/CONTRIBUTING.md) for detailed guidelines.

```
git clone https://github.com/caliber-ai-org/ai-setup.git
cd caliber
npm install
npm run dev      # Watch mode
npm run test     # Run tests
npm run build    # Compile
```

Uses [conventional commits](https://www.conventionalcommits.org/) — `feat:` for features, `fix:` for bug fixes.

#### Add a Caliber badge to your repo

After scoring your project, add a badge to your README:

[![Caliber Score](https://camo.githubusercontent.com/08f10330f06cf024e51511175509d708e49a8f7c465310e17375d6cf14ba59b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f63616c696265722d39342532463130302d627269676874677265656e)](https://camo.githubusercontent.com/08f10330f06cf024e51511175509d708e49a8f7c465310e17375d6cf14ba59b1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f63616c696265722d39342532463130302d627269676874677265656e)
Copy this markdown and replace `94` with your actual score:

```
![Caliber Score](https://img.shields.io/badge/caliber-SCORE%2F100-COLOR)

```

Color guide: `brightgreen` (90+), `green` (70-89), `yellow` (40-69), `red` (<40).

#### License

MIT
