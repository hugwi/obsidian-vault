---
created: 2026-07-22
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - agentic-engineering
  - voice-coding
  - mobile-coding
  - omnigent
  - happier
  - comparison
  - developer-tools
  - agent-orchestration
---

# OmniGent vs Happier — Comparison Report

Data collected 2026-07-22 from GitHub API, repo pages, and public docs.

## Overview

| | **OmniGent** | **Happier** |
|---|---|---|
| **URL** | [github.com/omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent) | [github.com/happier-dev/happier](https://github.com/happier-dev/happier) |
| **Pitch** | "Orchestrate Claude Code, Codex, Cursor, Pi, and custom agents — swap harnesses without rewriting, enforce policies, and collaborate in real time from any device." | "Web, Desktop & Mobile client for Codex, Claude Code, OpenCode, Kimi, Augment Code, Qwen — fully end-to-end encrypted." |
| **Mindset** | Agent orchestrator — multi-agent control plane with policy governance | Remote companion — control your local coding agents from any device |
| **Stars** | 7,580 | 1,378 |
| **Forks** | 1,088 | 111 |
| **Age** | 40 days (Jun 11, 2026) | 217 days (Dec 16, 2025) |
| **License** | Apache 2.0 | MIT |
| **Homepage** | omnigent.ai | happier.dev |

## Community & Contributors

### OmniGent
- **~200+ contributors** — broad community, distributed ownership
- Top 3 contributors only account for ~48% of commits (PattaraS 280, TomeHirata 272, serena-ruan 247)
- Many Databricks employees (serena-ruan-db, daniellok-db, dbczumar, championj-db, etc.)
- **381 open PRs, 662 open issues** — highly active but chaotic pipeline
- Viral growth: 7.6k stars in 5 weeks

### Happier
- **~47 contributors** — concentrated core team
- **1 person owns 78.5% of all commits** (leeroybrun: 6,116 of 7,789)
- Top 2 (leeroybrun + ex3ndr) account for ~88% of all commits
- **11 open PRs, 38 open issues** — tightly maintained
- Steady growth: 1.4k stars in 7 months

## Codebase & Velocity

| | **OmniGent** | **Happier** |
|---|---|---|
| **Primary language** | Python (82%) | TypeScript (90%) |
| **Source bytes** | 43.7 MB | 108.6 MB |
| **Total files** | 3,723 | 19,318 |
| **Python files** | 1,972 | — |
| **TS/TSX files** | 598 | 13,730 |
| **Est. lines of code** | ~924,000 | ~2,600,000 |
| **Commits/day** | **~42** | ~36 |
| **Source bytes/day** | **~1.09 MB** | ~0.50 MB |
| **LOC/day** | **~23,100** | ~12,000 |
| **LOC/week** | **~162,000** | ~84,000 |
| **Repo size on disk** | ~80 MB | ~350 MB |

> OmniGent produces ~2x more code per day right now, driven by a large community army. But early-project velocity inflation applies (40 days old vs 7 months).

## Stack & Architecture

### OmniGent
- **Core**: Python server (port 6767) spawning PTY/tmux sessions
- **Web UI**: TypeScript frontend built into the Python server
- **Desktop**: Native macOS app
- **Agent definition**: YAML — "Agent as a YAML file" with tools, sub-agents, MCP servers
- **Model access**: First-party API keys, subscriptions (Claude Pro/Max, ChatGPT), or any gateway (OpenRouter, LiteLLM, Ollama, Azure, Databricks)
- **Sandboxing**: Cloud sandboxes — Modal, Daytona, E2B, CoreWeave, Kubernetes, Docker, bwrap
- **Governance**: Policies at server/agent/session levels — spend caps, tool allowlists, approval gates
- **Deploy**: Docker, Render, Railway, Fly.io, HuggingFace, Modal, Cloudflare, Databricks
- **Teams**: Multi-user accounts, OIDC, session sharing, co-driving, forking

### Happier
- **Core**: TypeScript monorepo (Yarn) — relay server + daemon + web UI + mobile apps
- **Web UI**: React web client
- **Desktop**: Wrapped web UI
- **Mobile**: Native iOS (App Store) + native Android (Play Store beta) + APK
- **Agent model**: Wraps locally installed CLIs (`claude`, `codex`, `opencode`, `gemini`, `kilo`, `kimi`, `qwen`, `grok`)
- **Model access**: Uses your local CLI auth — whatever you already have installed
- **Relay**: Central coordination server (Happier Cloud or self-hosted Docker)
- **Security**: End-to-end encryption (TweetNaCl), zero-knowledge architecture, Swiss-based
- **Privacy**: Granular controls — per-session, per-machine, per-voice-provider

## Voice Capabilities — The Decisive Difference

### Happier Voice (EXTENSIVE — production-grade)

**4 voice modes**:
1. **Happier Voice** (managed ElevenLabs)
2. **BYO ElevenLabs** (bring your own API key)
3. **Local voice** — device STT/TTS, OpenAI-compatible endpoints, Google Cloud/Gemini, Kokoro neural TTS, Sherpa STT
4. **Off**

**Voice agent architecture** — not just speech-to-text, but a first-class AI colleague:
- Monitors **all running sessions** across all your machines
- Can **switch focus** between sessions on command
- Reads **pending permission requests** and answers them on your behalf
- Sends **messages to any session** you dictate to
- Can **discuss what agents are doing** with full access to recent context

**Two conversation modes**:
- **Direct to session** — speech → typed message in the current session
- **Agent mode** — intelligent voice layer with follow-up questions, summaries, structured actions

**Production features**:
- Real-time ElevenLabs with native **background audio on iOS** (works when phone is locked)
- Hands-free mode with configurable silence timeout and minimum speech duration
- Voice activity feed in the UI showing recent voice events
- Granular privacy toggles for what voice providers can see (session summaries, messages, file paths, tool args)
- Auto-provisioning: creates/updates ElevenLabs agents automatically

### OmniGent Voice (NONE)

No built-in voice capabilities. Zero code files matching "voice" in the repo. OmniGent's phone support is the **mobile web UI** — open your deployed server in a phone browser. Text-only. No STT, no TTS, no voice agent, no ElevenLabs integration.

## Feature Comparison

| Feature | OmniGent | Happier |
|---|---|---|
| Multi-agent orchestration | First-class (YAML agents + policies) | Multiple sessions, not orchestration |
| Native mobile apps | Web UI only | iOS + Android native |
| Voice coding | None | 4 modes + voice agent |
| E2E encryption | No | Yes (TweetNaCl) |
| Sandboxing | Cloud + bwrap, policy-enforced | Docker-based, not a focus |
| Governance policies | Spend caps, tool allowlists, approval gates | Privacy controls, not governance |
| Team collaboration | Multi-user, OIDC, co-driving | Session sharing, public links, friends |
| MCP servers | YAML-defined per agent | Managed in UI |
| Session handoff | Session sharing/forking | Session transfer between machines |
| Git integration | Via agent tools | Built-in file browser + git diff |
| Permission inbox | Approval gates | Inbox + pending queue + smart routing |
| Offline/remote | Deploy to cloud, access via web | Relay bridges mobile to local machine |
| Provider support | Claude, OpenCode, Codex, Cursor, Pi, Hermes, Gemini, Qwen | Claude, OpenCode, Codex, Gemini, Kilo, Kimi, Qwen, Augment, Grok |

## Can They Work Together?

**No direct integration exists.** Both wrap the same underlying CLIs — you can't have two wrappers managing the same `claude` session. They're competitors for the "remote coding agent" mindshare but solve different problems:

- **OmniGent**: Multi-agent orchestration, policy governance, cloud sandboxing. Phone UX is web-only, text-only.
- **Happier**: Single-agent remote control, voice-first mobile UX, E2E encryption.

They can **coexist on the same machine** managing different sessions, but there's no bridge or API between them.

## Verdict

**For voice coding from a phone**: Happier is the clear winner — and it's not close. OmniGent has zero voice capabilities. Happier's voice agent is a full AI colleague that manages your sessions, not just a speech-to-text wrapper.

**For multi-agent orchestration & governance**: OmniGent wins. YAML-defined agents, policy enforcement, cloud sandboxing, team multi-tenancy — purpose-built for the enterprise agent control plane.

**For community momentum**: OmniGent has viral energy (7.6k stars in 40 days) but shows growing pains (662 open issues, 381 open PRs). Happier has steady, focused growth with deeper engineering (2.6M LOC, 7-month track record).

**For overall maturity**: Happier has 7 months of sustained engineering behind it with 2.6M lines of code and a complete multi-platform product. OmniGent is newer, faster-moving, and community-driven — but less polished. If you want "battle-tested with voice," go Happier. If you want "agent governance platform with community velocity," go OmniGent.

## Related Notes

- [[Voice Coding Transport Architecture]] — real-time audio transport patterns for coding agents
- [[Voice agent skills for coding assistants (01knfr34mg4644we46gp2svqc3)]] — LiveKit voice agent skill patterns
- [[Omnigent bwrap sandbox — write-integrity, not exfil control]] — OmniGent sandbox internals
- [[State of Play: AI Coding Assistants (01kqzbtp29c313qynprmymhr6y)]] — broader landscape overview
- [[Agent Harness Engineering (01krkd6ghz8q0j5p9pn31jdxhs)]] — harness engineering as a discipline
- [[Running AI Coding Agents From My Phone (its getting out of hand) (01kt7mmv13dk7fgzd3za96k02y)]] — phone-based coding agent experience
