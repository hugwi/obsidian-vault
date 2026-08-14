---
created: 2026-08-14
categories:
  - "[[Resources]]"
domain: engineering
project: "[[Pharma target-hypothesis engine]]"
tags:
  - pharma
  - architecture
  - bayesian
---

# Target-hypothesis engine — architecture

How `.pharma-engine/` is put together and why each piece is shaped the way it is.
Context: [[Pharma target-hypothesis engine]] · science: [[Evidence classes in target validation]]

## Data model

Everything is one of four things, and **nothing is ever a bare number**:

- **Entity** — target, disease, pathway, process, drug
- **EvidenceAtom** — one dated, sourced, typed claim: subject, predicate, object,
  direction, evidence class, strength, year, citation, replication count,
  `disputed`, `refutes`
- **Hypothesis** — a target-disease pair, its class scores, flags, safety signals,
  tractability and experiment plan
- **Experiment** — a next step with a cost, a sensitivity, a specificity and an
  information yield

An association score with no provenance is what current tooling hands a
researcher, and it is exactly what cannot be argued with in a portfolio meeting.
Every score here decomposes back into the atoms that produced it, so a
disagreement lands on a specific piece of evidence rather than on a number.

## The scoring pipeline

```
atoms  ->  class score     saturating combination within one evidence class
class  ->  class log-LR    class score x that class's calibrated ceiling
class  ->  group log-LR    strongest class in full, correlated siblings damped 0.35
group  ->  posterior       sum of group log-LRs applied to a 10% base rate
```

**Within-class saturation** is a rank-damped noisy-OR: `1 - Π(1 - sᵢ/i²)`. Each
observation is an independent chance to establish the claim, discounted by rank so
the fifth paper counts for much less than the first. `--saturation harmonic`
reproduces Open Targets' normalisation (`Σ sᵢ/i²` over ~1.6449) for comparability;
it is not the default because dividing by the maximum theoretical harmonic sum is
calibrated for data sources carrying hundreds of evidence strings, and against a
curated handful it deflates a Mendelian human knockout to 0.6 of its strength.

**Cross-group combination** is where this departs most from a weighted sum.
Classes are grouped by what they physically observe — `human_genetics`,
`human_perturbation`, `experimental_biology`, `correlative`. Within a group the
strongest class counts fully and the rest damp to 35%; across groups log-LRs add
as independent evidence. Negative contributions are *not* damped: if two
independent things say the mechanism is wrong, both count. The asymmetry is
deliberate.

**The cap.** Total LR is capped at 26x, so no accumulation can push a mechanism
past ~74% from a 10% prior. Even textbook mechanisms fail for reasons no evidence
model contains — formulation, competitive landscape, trial execution. An uncapped
multiplicative model is the classic route to being confidently wrong.

## Kept out of the probability, on purpose

**Tractability** is a separate coordinate, with an extra penalty for agonism.
Under 5% of the human proteome has been successfully drugged; a mechanism can be
true and undevelopable, and TREM2 is the current exemplar — beautiful genetics,
requires receptor agonism.

**Safety** is a separate axis with its own expected-value discount. Folding it in
destroys the one thing a decision needs: *which* of the two is the problem.

## The signed mechanism graph

Every edge carries a polarity. The product of signs along a path gives the
therapeutic direction:

```
SOST  ⊣[inhibits] Wnt/osteoblast  →[drives] bone formation  ⊣[prevents] osteoporosis
  = (-1)(+1)(-1) = +1   →  sclerostin raises osteoporosis risk  →  inhibit it
```

Walked outward instead of inward, the same machinery predicts on-target harm:
`SOST ⊣ Wnt → vascular calcification`, which is the boxed warning romosozumab
carries. The engine reports it as a moderate signal clearly labelled as derived
from mechanism rather than from a trial.

**Disease nodes may be endpoints, never waypoints.** Without that rule the walk
routes through whichever disease has the most edges and manufactures
`HMGCR → LDL clearance → cardiovascular disease → NLRP3 → Alzheimer's`, which reads
as an argument for statins in dementia. Hub-hopping is how literature-based
discovery produces plausible nonsense at volume — see
[[Literature-based discovery and hypothesis generation]]. This was a real bug
caught by looking at the generated output, not by a test.

## Generation and transfer

`discover DISEASE` is open-form Swanson ABC: fix the disease, walk out through
pathways and processes, collect targets with no direct evidence. Generated
hypotheses enter the *same* engine as a single pathway-inference atom — the
weakest class — so they land near the base rate. That is the point: a system that
lets inference outrank a human knockout is generating enthusiasm, not knowledge.

**Evidence transfer** carries what is known about pathway siblings across, *with
the sign*. MERTK must be activated to restore RPE phagocytosis; ROCK constrains the
same process; the path flips sign, so the borrowed direction inverts and the engine
says inhibit ROCK. That is the reasoning that actually drives target selection —
IL-23 p19 was pursued in Crohn's because the protective coding variant sat in
IL23R, one node away — made explicit so it can be weighted and audited instead of
arriving as an unexamined intuition. It lands in the lowest-ceiling class:
borrowed evidence should put a hypothesis on the list, never justify a programme.

## Pricing the next experiment

Every evidence class carries a sensitivity, a specificity and an acquisition cost,
which makes any experiment a noisy test and its value ordinary expected
information gain:

```
p+   = P(H)·sens + (1-P(H))·(1-spec)
EIG  = H(P(H)) - [ p+·H(P(H|+)) + (1-p+)·H(P(H|-)) ]      bits
```

Divided by cost: **bits per $100k**. Differential expression is usually the
cheapest item and near the bottom of the ranking, because specificity 0.30 buys
almost nothing however little it costs. A mouse knockout is $250k, 52 weeks and
specificity 0.45.

The **kill experiment** is named separately — the work whose negative result most
reduces the posterior per dollar, with the number you would have to accept printed
before you start. Pre-registering the stopping rule is what makes a hypothesis
falsifiable, and it is the difference between stopping in year two and stopping in
Phase II.

## Evaluation, built in

`Ledger.as_of(year)` returns exactly the ledger a researcher would have had that
year. Two tests run on top of it:

- **`backtest`** — score real programmes on pre-entry evidence only, check
  approvals outrank failures. AUC 0.63 over 19; 0.38 over the 15 with any
  coverage, which surfaced a genuine blind spot rather than a bug.
- **`rediscover`** — restrict the graph to before a known discovery and see if
  open discovery surfaces it. Ground truth sits in `discoveries.json`, which the
  scoring path never reads, and a test asserts it has not leaked.

## Live data

`connectors.py` targets Open Targets (evidence by datatype, tractability, and the
Platform's own association score as a comparator), Europe PMC (co-occurrence for
the novelty term), ClinicalTrials.gov (what has already been tried — an
"unprecedented" target with six terminated Phase II trials is not unprecedented,
it is unpublished) and ChEMBL (does a chemical probe exist).

All four are blocked by the egress policy in the build environment.
`cli.py sources` reports which are reachable and why. **A connector that fails
quietly is worse than one that fails loudly**, because the scores it produces
still look reasonable.

## Decisions worth revisiting

- Noisy-OR vs harmonic saturation — chosen for small curated ledgers; with live
  Open Targets volumes the harmonic form may be the better default
- Damping factor 0.35 and the 26x cap are assumptions, marked as such in
  `priors.json`; nothing calibrates them yet
- No patient-stratification axis, despite biomarker selection being the single
  largest published effect size in the whole picture

Related: [[Pharma target-hypothesis engine]] · [[Evidence classes in target validation]] · [[Why drug programmes fail]]
