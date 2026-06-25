---
categories:
  - "[[Resources]]"
domain: engineering
title: "pi-ai · pi-coding-agent · pi-tui"
source: "https://rpiv-pi.com/"
author: "rpiv-pi"
published: 
created: 2026-06-05
description: "A pipeline of skills and agents for the Pi coding agent. 19 skills, 13 specialist"
tags:
  - to-process
  - agent-tools
---

§ rpiv-pi · pi plugin


#  research design ship


A pipeline of skills and subagents for the Pi coding agent. Turns a vague task into research questions, into a design, into a plan, into shipped code.


## A six-step chain. One artifact between each.


Each node is a skill. The artifact one writes is the next one’s input.


   01 discover 02 research 03 design 04 plan 05 implement 06 validate 
1. Interviews you one question at a time to capture feature intent (Goals · Non-Goals · Functional Requirements · Acceptance Criteria · Decisions) into a Feature Requirements Document the research skill consumes.
2. 02 /skill:research open   
 Answers structured research questions about a codebase by formulating trace-quality questions, dispatching parallel analysis agents, and synthesizing a cited research document under `.rpiv/artifacts/research/`.
3. 03 /skill:design open   
 Decomposes a complex feature into vertical slices and produces a design artifact (architecture decisions, slice breakdown, file map) that the planning skills consume.
4. 04 /skill:plan open   
 Sequences a design artifact into parallelized atomic phases with explicit success criteria, written to `.rpiv/artifacts/plans/`.
5. 05 /skill:implement open   
 Executes an approved phased plan one phase at a time, applies changes, runs each phase's success criteria, and only advances when they pass.

  → working-tree changes (no `.rpiv/artifacts/` artifact)
6. 06 /skill:validate open   
 Independently re-runs each phase's success criteria against the working tree and emits a pass/fail validation report that catches half-finished phases the implement loop missed.


drag · scroll · ← → to advance


§ guidance · per-folder shadow docs


## Context that narrows as the agent descends.


Inline `CLAUDE.md` works on greenfield, but it doesn't scale to a codebase nobody can fit in their head. **`/skill:annotate-guidance` writes a parallel `.rpiv/guidance/` tree of compact `architecture.md` files**, one per folder you care about, resolved per-depth and injected at `session_start` and on every `tool_call`, so context narrows as the agent navigates deeper.


 Two parallel passes map the tree, name the architecture, and pull idiomatic patterns out of each layer. 

     packages/ pi/ site/ tools/ CLAUDE.md  BROWNFIELD  → scans current repo · respects `.gitignore` 

 SOURCE .rpiv/ SHADOW  packages/  pi/  skills/  annotate-…/   architecture.md   architecture.md   architecture.md   architecture.md                     d=0 d=1 d=2 d=3 INJECTION POINTS session\_start  tool\_call   A shadow tree mirrors the source. Each folder's `architecture.md` is the smallest thing the agent needs to act correctly *here*, not the whole repo. 

* context follows the agent into deep folders
* zero source-code noise: docs live alongside, not inside

### pi · per-depth context

 On `session_start`, root guidance loads. On every `read`/`edit`/`write`, the closest ancestor `architecture.md` for the touched path injects too, silently, as a hidden context message. 

  read   ▲ARCH d=3 edit   ▲ARCH d=2 write   ▲ARCH d=1 PER-DEPTH 
see also /skill:migrate-to-guidance convert an existing `CLAUDE.md` project into the guidance system.