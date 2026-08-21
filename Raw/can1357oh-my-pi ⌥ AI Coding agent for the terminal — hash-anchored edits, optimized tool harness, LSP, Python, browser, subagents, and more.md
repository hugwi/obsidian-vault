---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, ai-agents]
tags:
  - computer-use
  - harness
  - memory
source: readwise
created: 2026-06-23
rating: 
action: 
theme: workflow-phases-gates
subtheme:
  - harness-loops
---

# can1357/oh-my-pi: ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more

![rw-book-cover](https://opengraph.githubassets.com/32b0a0ee7154e93ddc7beca979ac23632541c9e30c1a5c11fc2daf25db6d1f58/can1357/oh-my-pi)

## Metadata
- Author: [[https://github.com/can1357/]]
- Full Title: can1357/oh-my-pi: ⌥ AI Coding agent for the terminal — hash-anchored edits, optimized tool harness, LSP, Python, browser, subagents, and more
- Category: #articles
- Summary: Oh-my-pi is a powerful AI coding agent for the terminal that integrates many tools and runs code with advanced features like persistent Python and embedded bash. It supports fast searches across multiple providers, remembers your code between sessions, and works inside editors like Zed. The project is open-source, built mainly in Rust and TypeScript, and extends the original Pi agent with many coding-focused improvements.
- URL: https://github.com/can1357/oh-my-pi

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/can1357/oh-my-pi?resume=1) 

#### Create list

### can1357/oh-my-pi

main

tT

Go to file

Code

Open more actions menu

[![omp](https://github.com/can1357/oh-my-pi/raw/main/assets/hero.png?raw=true)](https://github.com/can1357/oh-my-pi/blob/main/assets/hero.png?raw=true)
**A coding agent with the IDE wired in.** **[omp.sh](https://omp.sh)**

[![npm version](https://camo.githubusercontent.com/b8a083e616374fef74d0b9ebd588995f822a99ed296174578edf0bc46ec47588/68747470733a2f2f696d672e736869656c64732e696f2f6e706d2f762f406f682d6d792d70692f70692d636f64696e672d6167656e743f7374796c653d666c617426636f6c6f72413d32323232323226636f6c6f72423d434233383337)](https://www.npmjs.com/package/@oh-my-pi/pi-coding-agent)
[![Changelog](https://camo.githubusercontent.com/21eeb8505db29c67bdf2650ec8153478fe24b639d815a08854fab993bfb6d57a/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6368616e67656c6f672d6b6565702d4530353733353f7374796c653d666c617426636f6c6f72413d323232323232)](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/CHANGELOG.md)
[![CI](https://camo.githubusercontent.com/9bd2292813e2b45af0f4869ef38aec58a038d3707ad94b56cf6967fa7998c775/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f616374696f6e732f776f726b666c6f772f7374617475732f63616e313335372f6f682d6d792d70692f63692e796d6c3f7374796c653d666c617426636f6c6f72413d32323232323226636f6c6f72423d334642393530)](https://github.com/can1357/oh-my-pi/actions)
[![License](https://camo.githubusercontent.com/827375b21da126b06032e667b1fd6e0cc029313cb5c2f11514b67bda4e10d41c/68747470733a2f2f696d672e736869656c64732e696f2f6769746875622f6c6963656e73652f63616e313335372f6f682d6d792d70693f7374796c653d666c617426636f6c6f72413d32323232323226636f6c6f72423d353841364646)](https://github.com/can1357/oh-my-pi/blob/main/LICENSE)
[![TypeScript](https://camo.githubusercontent.com/33bd453bd527ee565a8585436f768e1a665a223b4f942b097a3b419dbdf2b56f/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f547970655363726970742d3331373843363f7374796c653d666c617426636f6c6f72413d323232323232266c6f676f3d74797065736372697074266c6f676f436f6c6f723d7768697465)](https://www.typescriptlang.org)
[![Rust](https://camo.githubusercontent.com/10d4aef57926179330d45cec17cae084fca27eebfb91139e33173d84d8c034c2/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f527573742d4445413538343f7374796c653d666c617426636f6c6f72413d323232323232266c6f676f3d72757374266c6f676f436f6c6f723d7768697465)](https://www.rust-lang.org)
[![Bun](https://camo.githubusercontent.com/6724240696d93885eb396868eb051e07abb5d14539e782ffcf77b7c267bdad54/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f72756e74696d652d42756e2d6634373262363f7374796c653d666c617426636f6c6f72413d323232323232)](https://bun.sh)
[![Discord](https://camo.githubusercontent.com/768c129c92db4ec40a857173a559c08919651631da92c41911091083010722fd/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f446973636f72642d3538363546323f7374796c653d666c617426636f6c6f72413d323232323232266c6f676f3d646973636f7264266c6f676f436f6c6f723d7768697465)](https://discord.gg/4NMW9cdXZa)
Fork of [Pi](https://github.com/badlogic/pi-mono) by [@mariozechner](https://github.com/mariozechner)

The most capable agent surface that ships. Continuously tuned by real-world use — complete out of the box, open all the way down.

**40+** providers · **32** built-in tools · **13** lsp ops · **27** dap ops · **~27k** lines of Rust core.

#### Install

**macOS · Linux**

```
curl -fsSL https://omp.sh/install | sh
```

**Bun (recommended)**

```
bun install -g @oh-my-pi/pi-coding-agent
```

**Windows (PowerShell)**

```
irm https://omp.sh/install.ps1 | iex
```

**Pinned versions (mise)**

```
mise use -g github:can1357/oh-my-pi
```

macOS · Linux · Windows · bun ≥ 1.3.14

##### Shell completions

`omp` generates its own completion scripts for **bash**, **zsh**, and **fish** from the live command/flag metadata, so they never drift from the actual CLI. Subcommands, flags, and enum values complete statically; model names (`--model`, `--smol`, `--slow`, `--plan`) resolve against the bundled model catalog and `--resume` against your on-disk sessions.

```
# zsh — add to ~/.zshrc (or write the output into a file on your $fpath)
eval "$(omp completions zsh)"

# bash — add to ~/.bashrc
eval "$(omp completions bash)"

# fish
omp completions fish > ~/.config/fish/completions/omp.fish
```

#### Every tool, *benchmaxxed*.

Edits that land on the first attempt. Reads that summarize files instead of dumping their content. Searches that return instantly. Pick any model — omp will get it right.

| model | metric | what |
| --- | --- | --- |
| Grok Code Fast 1 | 6.7% → 68.3% | Tenfold lift the moment the edit format stops eating the model alive. |
| Gemini 3 Flash | +5 pp | Over str\_replace — beats Google's own best attempt at the format. |
| Grok 4 Fast | −61% tokens | Output collapses once the retry loop on bad diffs disappears. |
| MiniMax | 2.1× | Pass rate more than doubles. Same weights, same prompt. |

* `read` : summarized snippets · ideal defaults · selector hit rate
* `search` : fastest in the west
* `lsp` : everything your IDE knows, the agent knows
* `prompts` : adjusted relentlessly for each model

[Read the full post ↗](https://blog.can.ac/2026/02/12/the-harness-problem/)

#### The Pi *you love*, with **batteries included**.

Originally built on [Mario Zechner](https://github.com/mariozechner)'s wonderful [Pi](https://github.com/badlogic/pi-mono), omp adds everything you're missing.

##### 01 · Code execution w/ tool-calling

Most harnesses give the agent a Python sandbox and call it done. Ours runs persistent Python and a Bun worker, and either kernel can call back into the agent's own tools — read, search, task — over a loopback bridge. The agent loads a CSV with tool.read from inside Python, charts it from JavaScript, and never leaves the cell.

[![omp TUI: a single eval session with [1/2] pandas describe (Python) printing a real DataFrame.describe() table, followed by [2/2] top scorer (JavaScript) running a reduce. Footer: 'Both kernels ran in one session.'](https://camo.githubusercontent.com/140e81b2d44d47aca4af55fde0f6f37758a750769cb7c1f1d6bf6a988cd3ab97/68747470733a2f2f6f6d702e73682f63617074757265732f6576616c2e77656270)](https://camo.githubusercontent.com/140e81b2d44d47aca4af55fde0f6f37758a750769cb7c1f1d6bf6a988cd3ab97/68747470733a2f2f6f6d702e73682f63617074757265732f6576616c2e77656270)
##### 02 · LSP wired into every write

Ask for a rename and you get a rename. The call goes through workspace/willRenameFiles, so re-exports, barrel files, and aliased imports update before the file moves. Everything your IDE knows, the agent knows.

[![omp TUI: LSP references returns five hits across three files for the symbol formatBytes, then LSP rename applies the change with edits to format.ts/report.ts/cli.ts, then a Search formatBytes 0 matches confirmation. Final line: 'Rename complete. Five edits across three files…'.](https://camo.githubusercontent.com/3dbe99b01a010edabf6de5364489a1c61bbb4cb59a689748fc4906c3243f8604/68747470733a2f2f6f6d702e73682f63617074757265732f6c73702e77656270)](https://camo.githubusercontent.com/3dbe99b01a010edabf6de5364489a1c61bbb4cb59a689748fc4906c3243f8604/68747470733a2f2f6f6d702e73682f63617074757265732f6c73702e77656270)
##### 03 · Drives a real debugger

A C binary segfaults: the agent attaches lldb, steps to the bad pointer, reads the frame. A Go service hangs: it attaches dlv and walks the goroutines. A Python process is wedged: debugpy, pause, inspect, evaluate. Most agents are still sprinkling print statements.

[![omp TUI: a live lldb-dap session against a native binary at /tmp/omp-native/demo. Adapter=lldb-dap, Status=stopped, Frame=xorshift32, Instruction pointer 0x10000055C, Location demo.c:6:10. Debug scopes and Debug variables cards show locals (x = 57351) and the agent confirms the math: x went from 7 → 57351 (= 7 ^ (7<<13)).](https://camo.githubusercontent.com/27b5dcfd2bae8066791bcc0a50c8600e370bf9a42e03acc82896754c5bf28e10/68747470733a2f2f6f6d702e73682f636c6970732f6461702d706f737465722e77656270)](https://camo.githubusercontent.com/27b5dcfd2bae8066791bcc0a50c8600e370bf9a42e03acc82896754c5bf28e10/68747470733a2f2f6f6d702e73682f636c6970732f6461702d706f737465722e77656270)
*[Watch the capture ↗](https://omp.sh/clips/dap.mp4)*

##### 04 · Time-traveling stream rules

Your rules sit dormant until the model goes off-script. A regex match aborts the stream mid-token, injects the rule as a system reminder, and retries from the same point. You get course-correction without paying context tax on every turn. Injections survive compaction, so the fix sticks.

[![omp TUI: agent reading src.rs and about to write Box::leak when the request aborts (red Error: Request was aborted), an amber ⚠ Injecting rule: box-leak card injects the rule body Don't reach for Box::leak in production code paths, and the agent then course-corrects by proposing Arc<str> and asking the user to confirm.](https://camo.githubusercontent.com/a5d87ceace2baf77ce69b737f03368d2ee6cee335c7c32d2c46c6cf6f00c20ec/68747470733a2f2f6f6d702e73682f636c6970732f747473722d706f737465722e77656270)](https://camo.githubusercontent.com/a5d87ceace2baf77ce69b737f03368d2ee6cee335c7c32d2c46c6cf6f00c20ec/68747470733a2f2f6f6d702e73682f636c6970732f747473722d706f737465722e77656270)
*[Watch the capture ↗](https://omp.sh/clips/ttsr.mp4)*

##### 05 · First-class subagents

Split a job across workers and get typed results back. task fans out into isolated worktrees, each worker runs its own tool surface, and the final yield is a schema-validated object the parent reads directly. No prose to parse, no merge conflicts between siblings, no orphaned edits.

[![omp TUI showing task spawning two subagents ComponentsExports and RoutesExports, the constraints block requiring an IRC DM between peers, the per-subagent status cards with cost and duration, and a final Findings section listing both exports plus an honest 'IRC coordination note' about a one-sided handshake.](https://camo.githubusercontent.com/d2700f7fdc5f0f2df9dab74268cfd9949f790fde2fc68ab7a9d0c1ec8e06f5f3/68747470733a2f2f6f6d702e73682f636c6970732f6972632d706f737465722e77656270)](https://camo.githubusercontent.com/d2700f7fdc5f0f2df9dab74268cfd9949f790fde2fc68ab7a9d0c1ec8e06f5f3/68747470733a2f2f6f6d702e73682f636c6970732f6972632d706f737465722e77656270)
*[Watch the capture ↗](https://omp.sh/clips/irc.mp4)*

##### 06 · Read a pdf on arxiv, why not?

web\_search chains fourteen ranked providers and hands whatever URLs it finds straight to read. Arxiv PDFs, GitHub pages, Stack Overflow threads come back as structured markdown with anchors intact — the same tool surface you use on local files. Cite, follow, quote, never lose where you came from.

[![omp TUI: web_search returns 10 ranked Perplexity sources for inference-time compute scaling, the agent picks an arxiv paper, calls read https://arxiv.org/pdf/2604.10739v1, and summarizes the paper's headline result with real numbers.](https://camo.githubusercontent.com/77055efff7f017e3bed90b21d0012359ef606f2da2ca564ade81b718bf52d45e/68747470733a2f2f6f6d702e73682f636c6970732f7765622d706f737465722e77656270)](https://camo.githubusercontent.com/77055efff7f017e3bed90b21d0012359ef606f2da2ca564ade81b718bf52d45e/68747470733a2f2f6f6d702e73682f636c6970732f7765622d706f737465722e77656270)
*[Watch the capture ↗](https://omp.sh/clips/web.mp4)*

##### 07 · Unapologetically native. Even on Windows.

Other agents shell out to rg, grep, find, and bash. On many machines those binaries don't exist, and on the ones where they do, every call costs a fork-exec round-trip. omp links the real implementations into the process. ripgrep, glob, find: in-process. brush is the bash, with sessions that survive across calls. The same omp binary runs on macOS, Linux, and Windows — no WSL bridge.

##### 08 · Code review with priorities and a verdict

Get a clear verdict on whether the change ships, with every issue ranked P0 through P3 and scored for confidence. /review spawns dedicated reviewer subagents that sweep branches, single commits, or uncommitted work in parallel. You tackle what blocks release first; nothing important hides in a wall of prose.

##### 09 · Hashline: edit by content hash

Perfect edits, fewer tokens. The model points at anchors instead of retyping the lines it wants to change, so whitespace battles and string-not-found loops just stop happening. Edit a stale file and the anchors diverge — we reject the patch before it corrupts anything. Grok 4 Fast spends 61% fewer output tokens on the same work.

##### 10 · GitHub is just another filesystem

Other harnesses bolt on gh\_issue\_view, gh\_pr\_view, gh\_search — each with its own parameters the agent has to learn and you have to debug. We skipped that. read already handles paths; PRs are paths. One interface to teach the model, one surface to keep correct.

##### 11 · Hindsight: memory the agent curates

The agent remembers your codebase between sessions. It writes facts mid-run with retain, pulls them back with recall, and compresses each session into a mental model that loads on the first turn of the next one. Project-scoped by default, so what it learns about this repo stays with this repo.

##### 12 · ACP: editor-drivable agent

Run omp inside Zed and you get the same agent you drive from the terminal — reading the buffer you're actually looking at, writing through the editor's save path, spawning shells in the editor's terminal. Destructive tools pause for a permission prompt you can answer once and forget. No bridge, no plugin, no second brain to keep in sync.

##### 13 · Inherits what your other tools already wrote

Every other agent ships an importer and expects you to convert. omp reads the eight formats already on disk in their native shape — Cursor MDC, Cline .clinerules, Codex AGENTS.md, Copilot applyTo, and the rest. No migration script, no YAML-to-TOML port, no "supported subset" footnotes. The config your team wrote last quarter still works tonight.

##### 14 · omp commit: atomic splits, validated messages

omp reads the working tree through git-overview, git-file-diff, and git-hunk, then splits unrelated changes into atomic commits ordered by their dependencies. Cycles are rejected before anything is written. Source files score above tests, docs, and configs, so the headline commit is the one that matters. Lock files are excluded from analysis entirely.

##### 15 · Read PRs. *Walk skills.* Pull JSON out of subagents.

Ten internal schemes — `pr://`, `issue://`, `agent://`, `skill://`, `rule://`, and the rest — resolve transparently inside every FS-shaped tool the agent already calls. `read pr://1428` returns the same shape as `read src/foo.ts`. `search` walks a diff like a directory. `agent://<id>/findings.0.path` pulls a field out of a subagent's output by path.

[![omp TUI reading pr://can1357/oh-my-pi/1063 and then /diff/1, showing hunk headers, added lines, and a [MODIFIED] (+12 -0) summary.](https://camo.githubusercontent.com/d90f3688c20fb248cc0c98cd8fa779f010c5eb19c2c9afc702ce5b900d25f09b/68747470733a2f2f6f6d702e73682f63617074757265732f70722e77656270)](https://camo.githubusercontent.com/d90f3688c20fb248cc0c98cd8fa779f010c5eb19c2c9afc702ce5b900d25f09b/68747470733a2f2f6f6d702e73682f63617074757265732f70722e77656270)
##### 16 · Conflict resolution, made easy.

Each merge conflict becomes one URL. The agent writes `@theirs`, `@ours`, or `@base` to `conflict://N` and the file resolves cleanly. Bulk form: `conflict://*`.

[![omp TUI: ✓ Read src/session.ts (⚠ 1 conflict), then ✓ Write conflict://1 · 1 line with content @theirs, then a confirmation 'Resolved.'](https://camo.githubusercontent.com/b56059db6a4ff3610d8d6b15f42d9c868d1a5904af0aee0d49160411a6fc4bd9/68747470733a2f2f6f6d702e73682f636c6970732f636f6e666c6963742d706f737465722e77656270)](https://camo.githubusercontent.com/b56059db6a4ff3610d8d6b15f42d9c868d1a5904af0aee0d49160411a6fc4bd9/68747470733a2f2f6f6d702e73682f636c6970732f636f6e666c6963742d706f737465722e77656270)
*[Watch the capture ↗](https://omp.sh/clips/conflict.mp4)*

##### 17 · Preview, then accept.

`ast_edit` returns a *(proposed)* card with the replacement count. The change is staged. The agent calls `resolve` with a reason; the TUI turns it into an **Accept** card and the disk move happens — atomic, all or nothing.

[![omp TUI: ✓ AST Edit: console.log($X) (proposed) 3 replacements · 1 file, then ✓ Accept: 3 replacements in 1 file (AST Edit), followed by 'Applied 3 replacements in src/auth.ts.'](https://camo.githubusercontent.com/1a4962d03c97ffbbb32d538f6a960f2e7f7af2e89e42b3d25a2fe3de702f0fbb/68747470733a2f2f6f6d702e73682f636c6970732f636f64656d6f642d706f737465722e77656270)](https://camo.githubusercontent.com/1a4962d03c97ffbbb32d538f6a960f2e7f7af2e89e42b3d25a2fe3de702f0fbb/68747470733a2f2f6f6d702e73682f636c6970732f636f64656d6f642d706f737465722e77656270)
*[Watch the capture ↗](https://omp.sh/clips/codemod.mp4)*

##### 18 · Drives a *real browser*. *Or your Slack?*

Stealth's on by default, so pages see a normal user instead of a headless bot. The same API drives any Electron app in place — point it at Slack and the agent reads your DMs the way it reads the web.

[![omp TUI driving the browser tool against DuckDuckGo](https://camo.githubusercontent.com/db4584829fae7b69646566f89f031dd15278e8348b1f1c4018a97349a3f8b24a/68747470733a2f2f6f6d702e73682f63617074757265732f62726f777365722e77656270)](https://camo.githubusercontent.com/db4584829fae7b69646566f89f031dd15278e8348b1f1c4018a97349a3f8b24a/68747470733a2f2f6f6d702e73682f63617074757265732f62726f777365722e77656270)
#### Whatever the task needs, *it's already in the box*.

32 tools live in the same namespace as `read` and `bash`. Pin the active set with `--tools read,edit,bash,…` and the rest stay hidden but indexed — `search_tool_bm25` pulls them back in mid-session when `tools.discoveryMode` says so.

**Files & search**

* `read` — files, dirs, archives, SQLite, PDFs, notebooks, URLs, and internal `://` schemes through one path.
* `write` — create or overwrite a file, archive entry, or SQLite row.
* `edit` — hashline patches with content-hash anchors and stale-anchor recovery.
* `ast_edit` — structural rewrites previewed before apply, via ast-grep.
* `ast_grep` — structural code queries over 50+ tree-sitter grammars.
* `search` — regex over files, globs, and internal URLs.
* `find` — glob-based path lookup; reach for `search` when you need content matches.

**Runtime**

* `bash` — workspace shell, with optional PTY or background-job dispatch.
* `eval` — persistent Python and JavaScript cells with shared prelude and tool re-entry.
* `ssh` — one remote command against a configured host.

**Code intelligence**

* `lsp` — diagnostics, navigation, symbols, renames, code actions, raw requests.
* `debug` — drive a DAP session — breakpoints, stepping, threads, stack, variables.

**Coordination**

* `task` — fan out subagents in parallel, optionally workspace-isolated.
* `irc` — short prose between live agents in this process.
* `todo` — ordered mutations over the session todo list with phase tracking.
* `job` — wait on or cancel background jobs.
* `ask` — structured follow-up questions for interactive runs.

**Outside the box**

* `browser` — Puppeteer tabs over headless Chromium or CDP-attached apps.
* `web_search` — one query across configured providers, returning answer plus citations.
* `github` — GitHub CLI ops — repo, PR, issues, code search, Actions run-watch.
* `generate_image` — generate or edit raster images via Gemini image models.
* `inspect_image` — vision-model analysis of a local image file.
* `render_mermaid` — Mermaid source to terminal-friendly ASCII or PNG.

**Memory & state**

* `checkpoint` — mark conversation state for a later collapse-and-report.
* `rewind` — prune exploratory context, keep a concise report.
* `retain` — queue durable facts into the active Hindsight bank.
* `recall` — search the Hindsight bank for raw memories.
* `reflect` — ask Hindsight to synthesize an answer over the bank.

**Misc**

* `resolve` — apply or discard a queued preview action.
* `search_tool_bm25` — BM25 over the hidden tool index; activates top matches mid-session.

Setting-gated, off by default: `github`, `inspect_image`, `render_mermaid`, `checkpoint`, `rewind`, `search_tool_bm25`, `retain`, `recall`, `reflect`. Flip them on once, scoped per project.

[Full reference →](https://omp.sh/docs/tools)

#### Forty-plus providers, hundreds of models, *one /model away*.

Roles route work by intent. `default` for normal turns. `smol` for cheap subagent fan-out. `slow` for deep reasoning. `plan` for plan mode. `commit` for changelogs. Override at launch with `--smol`, `--slow`, or `--plan`; cycle through the configured models for the active role with `Ctrl+P`. Swap the active model mid-session with the `/model` slash command.

Auth tags below: `oauth` signs in with your provider account, `plan` routes through a coding-plan subscription, `local` runs against a local server with the key optional.

##### Frontier APIs

Direct APIs and gateways. Mix providers per role.

Anthropic `oauth` · OpenAI · OpenAI Codex `oauth` · Google Gemini · Google Antigravity `oauth` · xAI · Mistral · Groq · Cerebras · Fireworks · Together · Hugging Face · NVIDIA · OpenRouter · Synthetic · Vercel AI Gateway · Cloudflare AI Gateway · Wafer Serverless · Perplexity `oauth`

##### Coding plans

Subscription-routed. `/login` attaches the session.

Cursor `oauth` · GitHub Copilot `oauth` · GitLab Duo · Kimi Code `plan` · Moonshot · MiniMax Coding Plan `plan` · MiniMax Coding Plan CN `plan` · Alibaba Coding Plan `plan` · Qwen Portal · Z.AI / GLM Coding Plan `plan` · Xiaomi MiMo · Qianfan · NanoGPT · Venice · Kilo · ZenMux · Wafer Pass `plan` · OpenCode Go · OpenCode Zen

##### Run it yourself

OpenAI-compatible `/v1/models`. Local instances skip the key.

Ollama `local` · Ollama Cloud · LM Studio `local` · llama.cpp `local` · vLLM `local` · LiteLLM

##### Four knobs that make routing useful

* **Custom providers** — Declare anything that speaks `openai-completions`, `openai-responses`, `openai-codex-responses`, `azure-openai-responses`, `anthropic-messages`, `google-generative-ai`, or `google-vertex` in `~/.omp/agent/models.yml`.
* **Fallback chains** — Per-role chains under `retry.fallbackChains`. When the primary throws 429s or hits a quota wall, the next entry takes the rest of the turn — restored on cooldown.
* **Path-scoped roles** — Nest `paths:` under `modelRoles` to pin a heavier `default` on one repo without touching the global config. Closest path wins.
* **Round-robin credentials** — Stack API keys per provider and the runtime rotates with session affinity and per-credential backoff. Useful when one key would burn its quota by lunch.

Full provider & routing reference at [omp.sh/docs/providers](https://omp.sh/docs/providers).

#### Fourteen backends. *One tool the agent already knows*.

`web_search` is built in, not bolted on. `auto` walks a fourteen-provider chain; pin one by name if you already pay for it. Behind every hit, site-aware extraction turns GitHub, registries, arXiv, Stack Overflow, and docs into structured markdown — anchors and link targets survive.

##### Search providers

Fourteen backends. Pin one, or let `auto` walk the chain in order.

| provider | auth |
| --- | --- |
| `auto` | chain |
| `exa` | `EXA_API_KEY` (or mcp) |
| `brave` | `BRAVE_API_KEY` |
| `jina` | `JINA_API_KEY` |
| `kimi` | `MOONSHOT_API_KEY` |
| `zai` | `ZAI_API_KEY` |
| `anthropic` | oauth |
| `perplexity` | `PERPLEXITY_API_KEY` |
| `gemini` | oauth |
| `codex` | oauth |
| `tavily` | `TAVILY_API_KEY` |
| `parallel` | `PARALLEL_API_KEY` |
| `kagi` | `KAGI_API_KEY` |
| `synthetic` | `SYNTHETIC_API_KEY` |
| `searxng` | self-hosted |

##### Specialised handlers

The agent gets structured content, not stripped HTML.

* **Code hosts** — github, gitlab
* **Package registries** — npm, PyPI, crates.io, Hex, Hackage, NuGet, Maven, RubyGems, Packagist, pub.dev, Go packages
* **Research sources** — arxiv, semantic scholar
* **Forums** — stack overflow, reddit, hn
* **Docs** — mdn, readthedocs, docs.rs

Pages convert to markdown with link structure intact. The agent can cite, follow, and quote without losing anchors.

##### Security databases

Vuln lookups answer with vendor data, not blog summaries.

* **NVD** — national vulnerability database
* **OSV** — open source vuln feed
* **CISA KEV** — known exploited vulns

[`web_search` reference ↗](https://omp.sh/docs/tools#web_search)

#### Roughly **~27,000** lines of Rust, doing the work other harnesses shell out for.

Three crates, one platform-tagged N-API addon. Search, shell, AST, highlight, PTY, image decode, BPE counting — all in-process on the libuv pool. No fork/exec on the hot path.

* Crates: `pi-natives`, `pi-shell`, `pi-ast`
* Platforms: `linux-x64`, `linux-arm64`, `darwin-x64`, `darwin-arm64`, `win32-x64`

The table below is a per-module breakdown that intentionally omits glue and tests.

| Module | What it does | Powered by | ~LoC |
| --- | --- | --- | --- |
| shell | Embedded bash · persistent sessions · timeout/abort · custom builtins | brush-shell (vendored) | 3,700 |
| grep | Regex search · parallel/sequential · glob & type filters · fuzzy find | grep-regex · grep-searcher | 1,900 |
| keys | Kitty keyboard protocol with xterm fallback · PHF perfect-hash lookup | phf | 1,490 |
| text | ANSI-aware width · truncation · column slicing · SGR-preserving wrap | unicode-width · segmentation | 1,450 |
| summarize | Tree-sitter structural source summaries with elision controls | tree-sitter · ast-grep-core | 1,040 |
| ast | ast-grep pattern matching and structural rewrites | ast-grep-core | 1,000 |
| fs\_cache | Mtime-keyed file cache shared by read · grep · lsp | in-tree | 840 |
| highlight | Syntax highlighting · 11 semantic categories · 30+ aliases | syntect | 470 |
| pty | Native PTY allocation for sudo · ssh interactive prompts | portable-pty | 455 |
| glob | Discovery with glob · type filters · mtime sort · gitignore respect | ignore · globset | 410 |
| workspace | Workspace walker with gitignore + AGENTS.md discovery in one pass | ignore · git2 | 385 |
| appearance | Mode 2031 + native macOS dark/light via CoreFoundation FFI | core-foundation | 270 |
| power | macOS power-assertion API for idle/system/display-sleep prevention | IOKit FFI | 270 |
| task | Blocking work on libuv thread pool · cancellation · timeout · profiling | tokio · napi | 260 |
| fd | Filesystem walker for find-tool replacement | ignore | 250 |
| iso | Workspace isolation shim · apfs · btrfs · zfs · reflink · overlayfs · projfs · rcopy | pi-iso (PAL) | 245 |
| prof | Circular buffer profiler with folded-stack and SVG flamegraph output | inferno | 240 |
| ps | Cross-platform process-tree kill and descendant listing | libc · libproc · CreateToolhelp32Snapshot | 195 |
| image | Decode/encode PNG · JPEG · WebP · GIF · resize with 5 filters | image | 190 |
| clipboard | Text copy and image read from system clipboard · no xclip/pbcopy | arboard | 80 |
| tokens | O200k / Cl100k BPE token counting · both tables embedded | tiktoken-rs | 65 |
| html | HTML to Markdown with optional content cleaning | html-to-markdown-rs | 50 |

#### Four entry points: *interactive*, *one-shot*, RPC, and ACP.

Same engine, four wrappers. `omp` runs the TUI. `omp -p` answers a single prompt and exits. The Node SDK embeds the session in your process. `omp --mode rpc` and `omp acp` hand the wheel to another program over stdio.

##### Interactive — when in doubt, the agent asks

The TUI is the default surface. Tool calls render as cards, edits preview before they land, and ambiguity routes through the `ask` tool — a structured option picker the agent can call mid-turn. The keyboard handles the rest.

The same prompt cards surface over ACP, so editors get the picker without writing one.

[![omp TUI: the ask tool renders an option picker with three choices, a (Recommended) badge on the first, and 'up/down navigate · enter select · esc cancel' footer.](https://camo.githubusercontent.com/69cfe3c2397af4d4a71828377ec274c0d7e7edd646ef45bd27f550a2c688b751/68747470733a2f2f6f6d702e73682f63617074757265732f61736b2e77656270)](https://camo.githubusercontent.com/69cfe3c2397af4d4a71828377ec274c0d7e7edd646ef45bd27f550a2c688b751/68747470733a2f2f6f6d702e73682f63617074757265732f61736b2e77656270)
##### SDK — embed in Node

`@oh-my-pi/pi-coding-agent`

Node and TypeScript hosts pull the engine in directly. The package exposes `ModelRegistry`, `SessionManager`, `createAgentSession`, and `discoverAuthStorage`; the session emits typed events you subscribe to.

```
import { ModelRegistry, SessionManager, createAgentSession, discoverAuthStorage } from "@oh-my-pi/pi-coding-agent";

const auth = await discoverAuthStorage();
const models = new ModelRegistry(auth);
await models.refresh();

const { session } = await createAgentSession({
	sessionManager: SessionManager.inMemory(),
	authStorage: auth,
	modelRegistry: models,
});
await session.prompt("list .ts files");
```

##### RPC — drive over stdio

`omp --mode rpc`

For non-Node embedders, or when you want process isolation. NDJSON commands in, response and event frames out. `--mode rpc-ui` adds tool cards, selectors, and dialogs as `extension_ui_request` frames the host must answer.

```
$ omp --mode rpc --no-session
> {"id":"r1","type":"prompt","message":"list .ts files"}
< {"id":"r1","type":"response", ...}
> {"id":"r2","type":"set_model","provider":"anthropic","modelId":"sonnet-4.5"}
> {"id":"r3","type":"abort"}

```

##### ACP — speak to editors

`omp acp`

The [Agent Client Protocol](https://github.com/zed-industries/agent-client-protocol) over JSON-RPC. When the editor advertises capabilities, tool I/O routes through it and writes are gated by `session/request_permission`.

| omp tool | ACP route |
| --- | --- |
| `bash` | `terminal/create + terminal/output` |
| `read` | `fs/read_text_file` |
| `write` | `fs/write_text_file` |
| `edit, ast_edit, write, bash` | `session/request_permission` |

Full reference: [omp.sh/docs/sdk](https://omp.sh/docs/sdk).

#### A harness worth keeping is one you *don't* outgrow.

Pick it up at **[omp.sh](https://omp.sh)**.

omp is a fork of [Pi](https://github.com/badlogic/pi-mono) by [Mario Zechner](https://github.com/mariozechner), rewritten as a coding-first surface: sessions, subagents, slash commands, extensions — all TypeScript, all MIT, all on [GitHub](https://github.com/can1357/oh-my-pi). Shape it from config, hook it from outside, or read the source when you need to.

##### Primitives

An extension is a TypeScript module. Same tool API, same slash-command registry, same hotkey table, same TUI primitives the built-ins use. Nothing is reserved.

##### Discovery

On first run omp inherits whatever is already on disk: rules, skills, and MCP servers from `.claude`, `.cursor`, `.windsurf`, `.gemini`, `.codex`, `.cline`, `.github/copilot`, and `.vscode`. No migration script.

##### Extensibility

Ask omp to write the piece you're missing, then `/reload-plugins`. Keep it local, ship it in a `marketplace`, or publish it to npm.

#### Philosophy

omp is a fork of [pi-mono](https://github.com/badlogic/pi-mono) by [Mario Zechner](https://github.com/mariozechner), extended with a batteries-included coding workflow.

Key ideas:

* Keep interactive terminal-first UX for real coding work
* Include practical built-ins (tools, sessions, branching, subagents, extensibility)
* Make advanced behavior configurable rather than hidden

#### Development

##### Debug Command

`/debug` opens tools for debugging, reporting, and profiling.

For architecture and contribution guidelines, see [packages/coding-agent/DEVELOPMENT.md](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/DEVELOPMENT.md).

#### Monorepo Packages

| Package | Description |
| --- | --- |
| **[@oh-my-pi/pi-ai](https://github.com/can1357/oh-my-pi/blob/main/packages/ai)** | Multi-provider LLM client with streaming and model/provider integration |
| **[@oh-my-pi/pi-agent-core](https://github.com/can1357/oh-my-pi/blob/main/packages/agent)** | Agent runtime with tool calling and state management |
| **[@oh-my-pi/pi-coding-agent](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent)** | Interactive coding agent CLI and SDK |
| **[@oh-my-pi/pi-tui](https://github.com/can1357/oh-my-pi/blob/main/packages/tui)** | Terminal UI library with differential rendering |
| **[@oh-my-pi/pi-natives](https://github.com/can1357/oh-my-pi/blob/main/packages/natives)** | N-API bindings for grep, shell, image, text, syntax highlighting, and more |
| **[@oh-my-pi/omp-stats](https://github.com/can1357/oh-my-pi/blob/main/packages/stats)** | Local observability dashboard for AI usage statistics |
| **[@oh-my-pi/pi-utils](https://github.com/can1357/oh-my-pi/blob/main/packages/utils)** | Shared utilities (logging, streams, dirs/env/process helpers) |
| **[@oh-my-pi/swarm-extension](https://github.com/can1357/oh-my-pi/blob/main/packages/swarm-extension)** | Swarm orchestration extension package |

##### Rust Crates

| Crate | Description |
| --- | --- |
| **[pi-natives](https://github.com/can1357/oh-my-pi/blob/main/crates/pi-natives)** | Core Rust native addon (N-API `cdylib`) used by `@oh-my-pi/pi-natives`; aggregates the crates below |
| **[pi-shell](https://github.com/can1357/oh-my-pi/blob/main/crates/pi-shell)** | Embedded shell / PTY / process management split out of `pi-natives` (wraps `brush-*`) |
| **[pi-ast](https://github.com/can1357/oh-my-pi/blob/main/crates/pi-ast)** | tree-sitter-based code summarizer and AST utilities (50+ language grammars) |
| **[pi-iso](https://github.com/can1357/oh-my-pi/blob/main/crates/pi-iso)** | Task isolation backend resolver: APFS clones, btrfs/zfs reflinks, overlayfs, projfs, rcopy |
| **[brush-core-vendored](https://github.com/can1357/oh-my-pi/blob/main/crates/brush-core-vendored)** | Vendored fork of [brush-shell](https://github.com/reubeno/brush) for embedded bash execution |
| **[brush-builtins-vendored](https://github.com/can1357/oh-my-pi/blob/main/crates/brush-builtins-vendored)** | Vendored bash builtins (cd, echo, test, printf, read, export, etc.) |

#### License

MIT. See [LICENSE](https://github.com/can1357/oh-my-pi/blob/main/LICENSE).

© 2025 Mario Zechner  

 © 2025-2026 Can Bölük

*made for terminals that stay open*

* [omp.sh](https://omp.sh)
* [GitHub](https://github.com/can1357/oh-my-pi)
* [Changelog](https://github.com/can1357/oh-my-pi/blob/main/packages/coding-agent/CHANGELOG.md)
* [npm](https://www.npmjs.com/package/@oh-my-pi/pi-coding-agent)
* [Discord](https://discord.gg/4NMW9cdXZa)
* [MIT](https://github.com/can1357/oh-my-pi/blob/main/LICENSE)
