---
title: "From Template to Production-Shaped: An AI-Native Dev Flow for Go Side Projects"
source: "https://dev.to/kanchen_lin_331136af621d/from-template-to-production-shaped-an-ai-native-dev-flow-for-go-side-projects-245g"
author:
  - "[[dev.to]]"
published: 2026-05-26
created: 2026-06-07
description: "I wanted my next side project to look like the kind of code I'd ship at work — hexagonal... Tagged with go, architecture, ai, showdev."
tags:
  - "to-process"
  - orchestration
---
I wanted my next side project to *look* like the kind of code I'd ship at work — hexagonal architecture, sqlc, depguard, integration tests — without the usual side-project tax of spending three evenings on scaffolding before writing the first line of domain logic. So I built it twice. First, I forked a Go backend template I'd been hardening for months. Then I drove every feature on top of it through a structured AI workflow I call **qrspi**: *question → research → structure → plan → implement*.

The product itself is unremarkable on purpose: a QR code generator. Paste a URL, get back a scannable PNG and a `/r/:token` redirect, with per-link scan counts and a soft-delete kill switch. The interesting part — the part I'd want a reviewer to look at — is the *process* that produced it.

Repo: [linkc0829/go-qrcode-generator](https://github.com/linkc0829/go-qrcode-generator). Every artifact mentioned in this post is committed there.

## Step 1: Choose the template, then commit to its rules

Step zero was actually choosing what to build on. I shortlisted several Go backend templates, walked through each one with Claude to pressure-test the architecture, and landed on the one I'd been hardening for a while: [linkc0829/go-backend-template](https://github.com/linkc0829/go-backend-template).

The template is a feature-first hexagonal Go backend. Each feature lives in a single package under `internal/<feature>/`, and inside that package, `domain.go`, `service.go`, `ports.go`, and the adapters sit side-by-side as separate files. The Go package boundary *is* the hexagon edge.

What makes it stick is `depguard` in `.golangci.yml`. The build fails if:

- `domain.go` imports anything beyond stdlib and shared value objects
- `service.go` reaches for a driver or web framework
- `handler_*.go` touches a repo or cache directly
- one feature imports another feature

That last rule is the one that pays the most rent. Cross-feature dependencies are forced through **capability ports** — feature A defines an interface named after the capability it needs, and the composition root in `internal/bootstrap/wire.go` injects feature B's service to satisfy it. The features never know about each other.

This was the first decision I had to actually live with. The template ships with demo `user`, `order`, and `payment` slices. My project has no orders and no payments. The rule is: don't leave dead code as "future scaffolding." Delete the whole slice — the package, the wire block, the SQL queries, the migration tables, the OpenAPI paths, the depguard block. `make lint && make test` after each removal flushes out dangling references. By the time I started writing QR code logic, the repo only knew about things that existed.

## Step 2: Build the spec from a real system-design prompt

The functional spec came from a system-design exercise I'd worked through separately:

- Generate a QR code from a URL
- 302 redirect through our server on every scan (so we can count, and so we can kill a link)
- Targets: redirect latency < 100 ms, 1B codes, 100M users

The high-level design called out the load shape — read-heavy, one write to thousands of reads — and the levers that fall out of it: stateless API behind a gateway, cache `qr_token → image_url`, CDN the PNGs, index on `qr_token`. Tokens were originally specified as `base62(SHA-256(url + user_secret))`.

For the local build, I wrote down explicit **deviations** from the spec rather than pretending they didn't exist:

- Tokens use 96-bit `crypto/rand` → `base64url`. Loses idempotency for repeated (user, url) pairs but avoids the deterministic-token leak surface.
- The CDN tier is dropped. The browser fetches PNGs directly from MinIO using its anonymous `download` bucket policy. Same architectural shape as S3+CloudFront, minus the edge cache.
- Soft delete and PUT/DELETE endpoints land in a later slice.

Writing the deviations down up front is the part that makes the design honest. It's also the part that makes a portfolio reviewer's job easier — they can see *what was traded and why*, not just what got built.

## Step 3: qrspi — the workflow that does the actual building

The workflow idea started from [Research-Plan-Implement](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents) (RPI). QRSPI is an 8-phase extension of it that I picked up from community discussions and adapted for this project.

Once the spec was on paper, every feature went through the same eight phases. Each phase is a slash command backed by a skill, and each one writes its artifact to `thoughts/qrspi/<date>-<slug>/`:

1. **`/qrspi:1_question`** — decompose the ticket into neutral research questions. No opinions yet.
2. **`/qrspi:2_research`** — answer the questions by reading the codebase. Facts only.
3. **`/qrspi:3_design`** — discuss *where* we're going before *how*. Trade-offs surface here.
4. **`/qrspi:4_structure`** — outline vertical slices with test checkpoints.
5. **`/qrspi:5_plan`** — the tactical implementation plan; my working document.
6. **`/qrspi:6_worktree`** — isolated git worktree so the main checkout stays clean.
7. **`/qrspi:7_implement`** — execute the plan phase by phase, verifying at each checkpoint.
8. **`/qrspi:8_pr`** — open a PR that carries the design context forward into review.

The MinIO feature shows the whole thing on disk: a `ticket.md` pulled from the Notion source via MCP, then `questions.md`, `research.md`, `design.md`, `structure.md`, and `plan.md`. Each one builds on the last. By the time implementation starts, the agent isn't guessing — it's executing a plan I already agreed with.

The follow-up Redis redirect cache shipped the same way. The plan called out the read-heavy shape, picked a write-behind click-count buffer to avoid hammering Postgres on every scan, and named the cache invariants explicitly. The implementation was almost mechanical because the design phase had already resolved the interesting questions.

## What this buys, and what it costs

The cost is real: each feature carries five or six markdown files of design artifacts. For a single-developer side project, that's overhead I wouldn't tolerate in a freeform sketch.

What it buys:

- **The diff is reviewable.** Every commit is small, scoped, and traceable back to a design decision.
- **The architecture holds.** depguard catches the slow-drift violations (handler reaches into a repo, feature A imports feature B) the moment they appear, not three months later.
- **The agent stays useful past 2,000 LOC.** Most AI-coding flows degrade as the codebase grows because the model loses the plot. Writing the plot down — in `design.md`, in `plan.md` — keeps the next session grounded.
- **The portfolio story is the *process*, not the artifact.** Anyone can ship a QR code generator. Shipping one where the architecture, the trade-offs, and the deviations from spec are all written down on disk is a different signal.

The template is on GitHub; the qrspi artifacts are committed alongside the code. If you want to see how a single feature flows from ticket to PR, [the MinIO slice](https://github.com/linkc0829/go-qrcode-generator/tree/main/thoughts/qrspi/2026-05-15-minio-local-object-storage) is the cleanest example. The architecture ADRs in `docs/adr/` cover the two foundational decisions: feature-first hexagonal, and sqlc over an ORM.

Next up: a metrics slice (Prometheus + a Grafana dashboard for redirect latency), and a proper deletion follow-up so the spec's full CRUD surface lands. Both will go through qrspi. That's the point.

[Sentry](https://dev.to/sentry)

Promoted

[![Sentry image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FrO1GO78.png)](https://sentry.io/product/seer/?utm_source=devto&utm_medium=paid-social&utm_campaign=seer-fy26q2-seerlaunch&utm_content=video-ad-vibecoding-trysentry&bb=237782)