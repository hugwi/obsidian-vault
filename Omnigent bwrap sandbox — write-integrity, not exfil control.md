---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-07-03
tags:
  - omnigent
  - sandbox
  - security
  - claude-code
---

# Omnigent bwrap sandbox — write-integrity, not exfil control

Verified facts about the `linux_bwrap` sandbox that Omnigent's `enforce_sandbox`
policy / `os_env.sandbox` produce (checked by inspecting the actual `bwrap` argv
from `omnigent.inner.sandbox.resolve_sandbox`, **not** by trusting agent output).

## What the sandbox actually does

- **Writes ARE confined** to `write_paths` — bwrap `--bind`s only those; useful,
  real control. Narrowing `~/.agents` → `~/.agents/{state,cache}` stops tool
  writes from rewriting skills/hooks/agents (self-modification vector).
- **Reads are NOT confined by default.** When `read_paths` is unset, the backend
  emits **`--ro-bind-try / /`** — the *whole host filesystem* is bound read-only
  inside the sandbox. So `~/.config/netlight/token`, `~/.ssh`, `.env` files are
  all **readable**, and network is open.
- ⇒ This is a **WRITE-integrity control, NOT an exfil/confidentiality one.**
  Stripping a secret from `env_passthrough` does nothing for exfil — a tool can
  just read the secret *file* and send it over the open network.
- To actually confine reads: set `read_paths` to an allowlist that excludes
  `~/.config/netlight` (flips `--ro-bind / /` into specific binds). Separate,
  riskier change — breaks tools that read arbitrary files. Needs its own test.

## Two-layer sandbox model (easy to get wrong)

- `os_env.sandbox` governs the **PRIMARY agent's** own tool calls.
- The `enforce_sandbox` **policy** only fires on the synthetic `__agent_start`
  tool call → it governs **SUB-AGENT spawns**, not the primary agent.
- So hardening the policy alone leaves the primary agent wide; must tighten
  **both**. (`claude_sdk_executor` builds the wrapped-CLI sandbox from
  `resolve_sandbox(spec)` = `os_env.sandbox`.)

## The docstring lied

`bwrap_sandbox.py`'s header says "`$HOME` is **never** mounted." That's false for
the resolved policy when `read_paths` is unset — the `--ro-bind / /` overrides it.
**Never trust a docstring for a security property — inspect the resolved argv.**

## Process lesson (the real takeaway)

- I validated the sandbox by having an agent run shell probes and report SET/
  UNSET, OK/BLOCKED. **The agent hallucinated the results** (claimed it could
  write to `/etc` as non-root — impossible). LLM self-reports of tool output are
  **not** ground truth.
- The reliable method was **deterministic**: call `resolve_sandbox(os_env, cwd)`,
  read `policy.write_roots` / `read_roots` / `env_passthrough`, and reconstruct
  the `bwrap` `--bind`/`--ro-bind`/`--tmpfs` triples. No model in the loop.
- Also: `--tools coding` gives Omnigent **client-side** tools (run in the runner),
  which do NOT exercise the bwrap sandbox that wraps the native `claude` CLI —
  so probing via `--tools coding` tests the wrong execution path.
- I over-claimed a security property (in a *pushed* commit message) before
  verifying. Corrected with an honest follow-up commit rather than a force-push.
  Repo: `github.com/hugwi/ai-tools` — `d51a220` (wrong) → `aa29495` (retraction).

## See also

- `~/.agents/omnigent/agents-home.yaml` + `agents-home.sdk.yaml` — the specs.
- `~/.agents/scripts/anthropic-token.sh` — single-source token helper (reads
  `~/.config/netlight/token`, `600`; dir `700`). Only sudo-writable would need
  relocating out of `$HOME` or `chattr +i` (file perms alone don't suffice —
  the user owns the containing dir).
