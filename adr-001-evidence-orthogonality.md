---
created: 2026-08-14
categories:
  - "[[Projects]]"
project: "[[Pharma target-hypothesis engine]]"
tags:
  - adr
  - pharma
  - scoring
---

# ADR-001 — Evidence combines by independence group, not by weighted sum

**Status:** accepted · 2026-08-14

## Context

The reference implementation of target-disease scoring is the Open Targets
Platform: 20+ sources, ~7.8M associations, aggregated with a weighted harmonic sum
across data sources and then across data types. It is very good at what it is for,
which is finding what is known about a pair.

We need something else: a number a portfolio decision can rest on. That exposes a
problem with summing. The data types are not independent. A GWAS hit and a
coding-variant burden test at the same locus read the same human genetic signal
twice. Differential expression and literature co-occurrence are both largely a
measure of how heavily studied a gene already is. Summing correlated evidence is
the mechanism by which a scoring system talks itself into a target, and it
systematically re-ranks crowded, fashionable targets to the top — the opposite of
what a discovery tool should do.

## Decision

Evidence classes are assigned to **independence groups** by what they physically
observe:

| Group | Classes |
|---|---|
| `human_genetics` | causal-grade, common-variant |
| `human_perturbation` | drug or MR in humans, clinical precedent |
| `experimental_biology` | perturbation biology, model organism |
| `correlative` | expression, pathway inference, literature |

Within a group, the strongest class contributes its full log-likelihood-ratio and
the remainder are damped to 35%. Across groups, log-LRs add as independent
evidence. Class ceilings are anchored to published estimates where they exist
(causal-grade human genetics at 2.6x from Minikel et al. 2024, not a chosen
weight).

Three riders:

1. **Negative contributions are not damped.** If two independent lines say the
   mechanism is wrong, both count in full. The asymmetry is deliberate: we would
   rather over-weight refutation than under-weight it.
2. **Total LR is capped at 26x**, bounding the posterior near 74% from a 10%
   prior. Mechanisms fail for reasons outside any evidence model.
3. **Tractability and safety stay off the probability axis** and are reported as
   separate coordinates.

## Consequences

**Good.** Breadth across independent lines now beats depth within one, which is
the actual epistemics of target validation. CETP falls to 6.6%, below the base
rate, on refutation it would otherwise have accumulated past. A pair with one
Mendelian human knockout outranks a pair with fifteen expression papers, which is
the correct ordering and not what a citation-weighted system produces.

**Costly.** The damping factor of 0.35 and the 26x cap are assumptions. They are
marked as such in `priors.json` alongside every cited constant, but nothing
calibrates them, and a full unselected programme cohort would be needed to.

**Diverges from Open Targets.** Two systems will disagree on the same evidence.
That is intended and the disagreement is informative, so `connectors.py` keeps the
Platform's own association score as a comparator rather than as an input, and
`--saturation harmonic` reproduces its within-class aggregation for a like-for-like
comparison.

## Alternatives rejected

- **Weighted sum with tuned weights** — the failure mode above, and tuning weights
  against 23 curated outcomes would fit noise.
- **A learned model over Open Targets evidence** — no training set of adequate
  size exists for programme outcomes, and it would destroy the audit trail, which
  is the feature that makes the output usable by someone who has to sign for it.
- **Full Bayesian network over evidence sources** — the correct answer if the
  correlation structure between sources were known. It is not, and asserting one
  would be a more elaborate way of making the same numbers up.

Related: [[Target-hypothesis engine — architecture]] · [[Evidence classes in target validation]] · [[Pharma target-hypothesis engine]]
