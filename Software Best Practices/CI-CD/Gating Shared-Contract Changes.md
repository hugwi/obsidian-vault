---
tags: [ci, monorepo, best-practice]
---

# Gating Shared-Contract Changes in a Monorepo

## Core principle

In a monorepo, a CI workflow's trigger filter encodes a claim about a package's
blast radius. **A consumer's CI must trigger on its upstream dependencies, not
only on its own directory.** If `app/` compiles `packages/shared` as source, then
a `packages/shared` change can break `app/` — so `app-ci` must run when
`packages/shared/**` changes, even if zero `app/**` files are in the diff.

Two distinct failure modes must both be closed:

- **Unchecked consumer** — the consumer's CI never runs because the changed
  package is outside its path-filter.
- **Wrong tree** — each PR is green against an old `main`; the broken state exists
  only in the merged tree, which no per-branch CI ever compiles.

## The canonical failure

See the full incident: [[Path-Filtered CI — The Shared-Contract Blind Spot]].

A required field added to a shared schema reached `main` while every PR stayed
green:

![[Path-Filtered CI — The Shared-Contract Blind Spot#Why it occurred — two independent failures, stacked]]

## How to close both gaps

![[Path-Filtered CI — The Shared-Contract Blind Spot#Exploration — the fixes, by aspect]]

## Decision rules

![[Path-Filtered CI — The Shared-Contract Blind Spot#Decision: a path-filter must include the change's upstream dependencies, not just its own directory]]

![[Path-Filtered CI — The Shared-Contract Blind Spot#Decision: "green on the branch" ≠ "green on main"]]

## Checklist for any new path-filtered workflow

- [ ] Does this package consume a shared workspace package as source? If yes, add that package's glob to **both** `pull_request.paths` and `push.paths`.
- [ ] Is there a merge queue or a "require branches up to date" rule for the shared contract surface?
- [ ] Is the same gate reproducible locally (e.g. consumer `tsc -b` runs in `verify` when the shared package is in the diff)?
- [ ] Are new **required** fields on shared types either staged optional or shipped with all consumer updates in the same PR?

## Related

- [[Path-Filtered CI — The Shared-Contract Blind Spot]] — the full case study
- [[tests/Mutation Testing]] — another CI-gate hardening story
- [[Architecture Decisions/Documenting Constraints]] — why decisions like path-filter scope must be written down
