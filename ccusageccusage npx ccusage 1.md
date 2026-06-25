---
categories:
  - "[[Resources]]"
domain: engineering
title: "ccusage/ccusage: npx ccusage"
source: "https://github.com/ccusage/ccusage"
author:
published:
created: 2026-06-12
description: "npx ccusage. Contribute to ccusage/ccusage development by creating an account on GitHub."
tags:
  - "to-process"
  - context-management
---
[![ccusage logo](https://camo.githubusercontent.com/c7676749b9555285615a446b94b7fc9a468bfa47aa2e0c296bc1d4b9bbf134d5/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f636375736167652f63637573616765406d61696e2f646f63732f7075626c69632f6c6f676f2e737667)](https://camo.githubusercontent.com/c7676749b9555285615a446b94b7fc9a468bfa47aa2e0c296bc1d4b9bbf134d5/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f636375736167652f63637573616765406d61696e2f646f63732f7075626c69632f6c6f676f2e737667)

## ccusage

[![ccusage%2Fccusage | Trendshift](https://camo.githubusercontent.com/092e6193ebbb88ca8b607d04f25d45300ae43bff351d8b904d1f38fcf37bc4b9/68747470733a2f2f7472656e6473686966742e696f2f6170692f62616467652f7265706f7369746f726965732f3138353333)](https://trendshift.io/repositories/18533)

[![ccusage terminal report screenshot](https://camo.githubusercontent.com/3db4cc294fc7492b2f1a412f22d985b91ffaa84a2b7dd89751bc731db470fc74/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f636375736167652f63637573616765406d61696e2f646f63732f7075626c69632f73637265656e73686f742e706e67)](https://camo.githubusercontent.com/3db4cc294fc7492b2f1a412f22d985b91ffaa84a2b7dd89751bc731db470fc74/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f636375736167652f63637573616765406d61696e2f646f63732f7075626c69632f73637265656e73686f742e706e67)

> Analyze coding (agent) CLI token usage and costs from local data.

## Major Sponsors[![CodeRabbit](https://camo.githubusercontent.com/1abed4120da199625559d6b603690614b8d0f2dea3a690859f33a632ac02a8ef/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f636375736167652f63637573616765406d61696e2f646f63732f7075626c69632f636f64657261626269742d6c6f676f2e737667)](https://coderabbit.link/ryoppippi)[![Blacksmith](https://camo.githubusercontent.com/44c8c527ae601e03456b47ea22120989008ebe3657cfe638ce12b7c620bc85ca/68747470733a2f2f63646e2e6a7364656c6976722e6e65742f67682f636375736167652f63637573616765406d61696e2f646f63732f7075626c69632f626c61636b736d6974682e706e67)](https://blacksmith.sh/)

## Quick Start

```
npx ccusage@latest
```

## Supported Sources

ccusage reads local usage data from coding agent CLIs and turns it into daily, weekly, monthly, and session reports.

| Source | Focused command example |
| --- | --- |
| Claude Code | `ccusage claude daily` |
| Codex | `ccusage codex daily` |
| OpenCode | `ccusage opencode daily` |
| Amp | `ccusage amp daily` |
| Droid | `ccusage droid daily` |
| Codebuff | `ccusage codebuff daily` |
| Hermes Agent | `ccusage hermes daily` |
| pi-agent | `ccusage pi daily` |
| Goose | `ccusage goose daily` |
| OpenClaw | `ccusage openclaw daily` |
| Kilo | `ccusage kilo daily` |
| Kimi | `ccusage kimi daily` |
| Qwen | `ccusage qwen daily` |
| GitHub Copilot CLI | `ccusage copilot daily` |
| Gemini CLI | `ccusage gemini daily` |

Use `ccusage daily`, `ccusage weekly`, `ccusage monthly`, or `ccusage session` to include every detected source in one report.

## Installation

### Package Runners

You can run ccusage directly without a global installation:

```
# npm
npx ccusage@latest

# Nix
nix run github:ccusage/ccusage -- daily

# Alternative package runners
bunx ccusage
pnpm dlx ccusage
pnpx ccusage

# PR preview builds
bunx -p https://pkg.pr.new/ccusage/ccusage@<pr-number> ccusage --offline
```

> [bunx](https://bun.com/docs/pm/bunx) caches the downloaded package, so repeated runs are faster after the first launch.

## Usage

```
# Basic usage
bunx ccusage          # Show all detected sources by day (default)
bunx ccusage daily    # All detected sources by day
bunx ccusage weekly   # All detected sources by week
bunx ccusage monthly  # All detected sources by month
bunx ccusage session  # All detected sources by session
bunx ccusage blocks   # Claude Code 5-hour billing windows
bunx ccusage statusline  # Claude Code status line for hooks (Beta)

# Source-focused reports and options
bunx ccusage claude daily --mode display
bunx ccusage codex daily --speed fast
bunx ccusage opencode weekly
bunx ccusage amp session
bunx ccusage droid daily
bunx ccusage codebuff daily
bunx ccusage hermes daily
bunx ccusage goose daily
bunx ccusage openclaw daily
bunx ccusage kilo daily
bunx ccusage kimi daily
bunx ccusage qwen daily
bunx ccusage copilot daily
bunx ccusage gemini daily
bunx ccusage pi daily --pi-path /path/to/sessions
bunx ccusage pi daily --pi-path /path/to/sessions,/archive/pi/sessions

# Explicit unified report
bunx ccusage daily --all

# Filters and options
bunx ccusage daily --since 2026-04-25 --until 2026-05-16
bunx ccusage daily --json  # JSON output
bunx ccusage daily --no-cost  # Hide cost columns and JSON cost fields
bunx ccusage daily --timezone UTC  # Use UTC timezone

# Project analysis
bunx ccusage claude daily --instances  # Group Claude Code by project/instance
bunx ccusage claude daily --project myproject  # Filter to specific Claude project
bunx ccusage claude daily --instances --project myproject --json  # Combined usage

# Compact mode for screenshots/sharing
bunx ccusage --compact  # Force compact table mode
bunx ccusage monthly --compact  # Compact monthly report
```

## Features

- 📊 **Daily Report**: View token usage and costs aggregated by date
- 📅 **Monthly Report**: View token usage and costs aggregated by month
- 💬 **Session Report**: View usage grouped by conversation sessions
- 🤖 **Unified CLI Reports**: View Claude Code, Codex, OpenCode, Amp, Droid, Codebuff, Hermes Agent, pi-agent, Goose, OpenClaw, Kilo, Kimi, Qwen, GitHub Copilot CLI, and Gemini CLI usage from one CLI
- ⏰ **5-Hour Blocks Report**: Track usage within Claude's billing windows with active block monitoring
- 🚀 **Statusline Integration**: Compact usage display for Claude Code status bar hooks (Beta)
- 🤖 **Model Tracking**: See which models are used across supported sources
- 📊 **Model Breakdown**: View per-model cost breakdown with `--breakdown` flag
- 📅 **Date Filtering**: Filter reports by date range using `--since` and `--until`
- 📁 **Custom Paths**: Support for custom local data directory locations
- 🎨 **Beautiful Output**: Colorful table-formatted display with automatic responsive layout
- 📱 **Smart Tables**: Automatic compact mode for narrow terminals (< 100 characters) with essential columns
- 📸 **Compact Mode**: Use `--compact` flag to force compact table layout, perfect for screenshots and sharing
- 📋 **Enhanced Model Display**: Model names shown as bulleted lists for better readability
- 📄 **JSON Output**: Export data in structured JSON format with `--json`
- 💰 **Cost Tracking**: Shows costs in USD for each day/month/session
- 🔒 **Cost Hiding**: Remove cost columns and JSON cost fields with `--no-cost`
- 🔄 **Cache Token Support**: Tracks and displays cache creation and cache read tokens separately
- 🌐 **Offline Mode**: Use pre-cached pricing data without network connectivity with `--offline`
- 🧩 **Custom Pricing Overrides**: Override token pricing per raw model name in `ccusage.json` without rebuilding
- 🏗️ **Claude Instance Support**: Group Claude Code usage by project with `--instances` and filter by specific projects
- 🌍 **Timezone Support**: Configure timezone for date grouping with `--timezone` option
- ⚙️ **Configuration Files**: Set defaults with JSON configuration files, complete with IDE autocomplete and validation

## Documentation

Full documentation is available at **[ccusage.com](https://ccusage.com/)**

## Development

Contributor setup

Contributor setup uses the Nix flake development environment with [nix-direnv](https://github.com/nix-community/nix-direnv) for pinned tools, and `just` for everyday development tasks. Install [Nix](https://nixos.org/) with the `nix-command` and `flakes` experimental features enabled, then let nix-direnv load the dev shell automatically when you enter the directory:

```
# Clone the repository
git clone https://github.com/ccusage/ccusage.git
cd ccusage

# Allow direnv to load the Nix dev shell
direnv allow
```

The dev shell provides the pinned `pnpm`, Rust toolchain, GitHub CLI, git hooks, generated local agent skills, and project utilities from `flake.nix`. It also installs package dependencies from `pnpm-lock.yaml` when needed.

Run project tasks with `just` from inside the Nix environment (`just --list` shows every recipe):

```
just fmt
just test
just check
```

### Nix Package

The flake exposes `ccusage` as the default package and app:

```
nix run github:ccusage/ccusage
nix run github:ccusage/ccusage -- codex daily --offline
nix build github:ccusage/ccusage
```

Nix builds embed the LiteLLM pricing file from the locked `litellm` flake input, so sandboxed builds do not fetch pricing at build time. To update the locked pricing snapshot:

Non-Nix Cargo builds read the same locked LiteLLM revision from `flake.lock` and fetch the pricing file from that revision at build time.

```
just update-litellm-pricing
```

The scheduled `update pricing` workflow runs the same update and validation, then opens a PR when the pricing snapshot changes.

## GitHub Sponsors

[![Sponsors](https://camo.githubusercontent.com/69e9498c1e2c48c04ccc59405429cc543b37af5a44f530d1c385b6831752cf7c/68747470733a2f2f73706f6e736f72732e72796f7070697070692e636f6d2f73706f6e736f72732e706e67)](https://github.com/sponsors/ryoppippi)

## Star History

[

![Star History Chart](https://camo.githubusercontent.com/160ae7a9115f6478711a7fc1eefaaa17af8e54d2161df5198d719f077a53e346/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d636375736167652f6363757361676526747970653d44617465)

](https://www.star-history.com/#ccusage/ccusage&Date)

## License

[MIT](https://github.com/ccusage/ccusage/blob/main/LICENSE) © [@ryoppippi](https://github.com/ryoppippi)