---
categories:
  - "[[Projects]]"
project: "[[Pharma target-hypothesis engine]]"
status: active
domain: engineering
outcome: Built a working engine that scores, generates and prices drug target hypotheses, and evaluated it against real historical outcomes
due: 
created: 2026-08-14
tags:
  - project
  - pharma
  - drug-discovery
---

# Pharma target-hypothesis engine

A decision system for early drug discovery. Give it a target and a disease and it
returns a calibrated probability that the mechanism survives clinical development,
the direction you would have to push the target, the on-target safety that
implies, and the cheapest experiment that could kill it.

Code: `.pharma-engine/` (dot-prefixed so Obsidian does not index it, like
`.multilabel.py`). Python 3.11, standard library only, 43 tests.

## Outcome

Built a working engine that scores, generates and prices drug target hypotheses,
and evaluated it against real historical outcomes.

**Done when:**
- [x] Research the actual bottleneck in pharma R&D and the published effect sizes
- [x] Evidence ledger with provenance, replication and refutation
- [x] Scoring that refuses to compound correlated evidence
- [x] Signed mechanism graph — direction of effect propagates along paths
- [x] Open discovery (Swanson ABC) with evidence transfer across pathway siblings
- [x] On-target safety from pleiotropy and mechanism paths
- [x] Experiment planner: expected information gain per dollar, named kill criterion
- [x] Retrospective backtest and blind rediscovery
- [x] Findings written up in the vault
- [ ] Replace the curated snapshot with live Open Targets / Europe PMC / ChEMBL pulls
- [ ] Backtest against a full unselected programme cohort rather than 23 curated ones

## The thesis in one paragraph

Roughly 90% of programmes entering the clinic fail, Phase II is the worst gate at
28%, and 40–50% of failure is lack of efficacy with another 30% on-target
toxicity. **Three quarters of clinical failure is biology, not chemistry** — the
mechanism was wrong, or right in the wrong tissue, or right in the wrong patients.
AI has been aimed mostly at the 10–15% that is chemistry: 170+ AI-discovered
molecules are in the clinic and none has been approved. The interventions with
published effect sizes are all upstream and all evidential — genetic support 2.6x,
biomarker stratification 1.6% → 10.7%, better target validation ≈24% less Phase II
attrition. So: score mechanisms, not molecules, and build it to be argued with.

Full working: [[Why drug programmes fail]] · [[AI in drug discovery — state of the field 2026]]

## What it does differently

Four things get lost between "what is known" and "what should we do", and each is
a design decision:

1. **Correlated evidence stops compounding.** Classes are grouped by what they
   physically observe; inside a group only the strongest counts in full, the rest
   damp to 35%. A GWAS hit and a coding-variant burden test at one locus are one
   signal read twice.
2. **Scores can go down.** Refuting atoms carry negative log-likelihood-ratios.
   CETP lands at 6.6%, below the 10% base rate, because torcetrapib killed people
   while raising HDL-C by 72%.
3. **Direction of effect is first-class.** GIPR gets `DIRECTION-CONFLICT` and a
   direction-resolution study at the top of its plan, because agonism is approved
   for obesity *and* loss-of-function variants associate with lower BMI.
4. **The output is a decision.** Not "association score 0.72" but, for sclerostin
   in osteoporosis: "48%, inhibit, antibody route open, vascular calcification is a
   real risk, and a $120k CRISPR study in patient-derived cells is the cheapest
   thing that could kill it — 48% down to 25% if it reads negative."

Detail: [[Target-hypothesis engine — architecture]] · [[Evidence classes in target validation]]

## Does it work

**Blind rediscovery — both hit rank 1.**

| Case | Cutoff | Result |
|---|---|---|
| ROCK inhibition in dry AMD | 2024 | rank 1 of 3, direction `inhibit`, via ROCK → Rho/ROCK actin regulation ⊣ phagocytosis → RPE phagocytosis ⊣ dry AMD |
| AAK1 in COVID-19 | 2019 | rank 1 of 1, direction `inhibit`, via AAK1 → clathrin-mediated endocytosis → viral entry → COVID-19 |

The first is FutureHouse Robin's 2025 autonomous discovery, confirmed at the bench
(ripasudil increases RPE phagocytosis). The second is BenevolentAI's 2020
identification of baricitinib. Both recovered from a graph restricted to before
the discovery, with ground truth held in a file the scoring path never reads.

**Time-split backtest — AUC 0.63 over 19 programmes**, scored using only evidence
published before each one entered the clinic. Over the 15 with any pre-entry
evidence, AUC is **0.38** — below chance, and the most useful result of the
exercise. Two causes: the covered subset has 2 failures (not a statistic), and one
of them is BACE1, which the engine scores *above* PCSK9 on identical genetic
evidence plus a mouse knockout. Nothing in the model distinguishes lifelong 40%
reduction from birth from 90% inhibition started in symptomatic disease — which is
precisely what killed verubecestat. That gap is now flagged (`GENETIC-ONLY`) rather
than priced, because quantifying it would mean inventing a number.

## Next actions

- [ ] Populate the ledger from live sources — the connectors exist and are blocked
      by the egress policy in the build environment, not by anything in the design
- [ ] Add an evidence class for intervention timing / degree of engagement, which
      is the named blind spot above
- [ ] Backtest against an unselected cohort so calibration means something
- [ ] Consider a patient-stratification axis — biomarker selection is the largest
      published effect size in the whole picture and the engine currently ignores it

## Log

- 2026-08-14 — Research, design, prototype, evaluation and vault write-up.
  43 tests passing. Both rediscovery cases recovered at rank 1.

---

## Desk

```dataviewjs
await dv.view("Templates/Scripts/project-desk");
```
