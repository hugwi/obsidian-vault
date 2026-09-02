---
title: "amazing release. it's a web UI with multiple harnesses inside it, you can spawn claude code and codex agent through their SDK"
source: "x"
url: "https://x.com/eliebakouch/status/2087904176357437820"
author: "elie"
published: "Thu Aug 13 14:08:41 +0000 2026"
created: "2026-08-13"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating: ""
tags:
  - "clip/x"
  - "multi-agent-orchestration"
  - "ui-trajectory-view"
  - "harnesses-modes"
  - "agent-logging"
summary: "amazing release. it's a web UI with multiple harnesses inside it, you can spawn claude code and codex agent through their SDK

\"deepseek harness\" supports different \"modes\" by default (which are harnesses): code mode with programmatic tool calling (in typescript), bash+edit (usually used in evals), or standard with write/read tool etc.."
theme:
  - "multi-agent-orchestration"
  - "work-breakdown-specs"
  - "human-ux-frontend"
subtheme:
  - "code-mode-harnesses"
  - "kv-cache-design"
  - "agent-decision-logging"
domain: "agentic-engineering"
---

# amazing release. it's a web UI with multiple harnesses inside it, you can spawn claude code and codex agent through their SDK

> Saved from X on 2026-08-13. Author: elie.

amazing release. it's a web UI with multiple harnesses inside it, you can spawn claude code and codex agent through their SDK

"deepseek harness" supports different "modes" by default (which are harnesses): code mode with programmatic tool calling (in typescript), bash+edit (usually used in evals), or standard with write/read tool etc..

there is first class KV cache aware design, basically making sure the KV cache is never altered. for every change they don't modify previous history (prefix) but append something at the end that states the modification. i expect other harnesses to do the same but you never know?

very interesting how this harness was developed too. it was HEAVILY agent first coded, there is an entire folder called ".agents/notes" that records every decision and proposal that agents left there (including some cool info like the fact that they also use it for post training)

the UI is beautiful, especially the trajectory view. they have a full paper detailing composability and their system design for "plugins", this is going to be super helpful
