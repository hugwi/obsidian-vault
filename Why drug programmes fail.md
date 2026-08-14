---
created: 2026-08-14
categories:
  - "[[Resources]]"
domain: health
tags:
  - pharma
  - drug-discovery
  - target-validation
project: "[[Pharma target-hypothesis engine]]"
---

# Why drug programmes fail

The base rates that any system aimed at helping researchers find new medicines has
to be built around. Everything here is the empirical picture as of 2026, gathered
while building [[Pharma target-hypothesis engine]].

## The numbers

| Stage | Success rate |
|---|---|
| Phase I | ~47% |
| **Phase II** | **~28%** |
| Phase III | ~55% |
| Phase I → approval | ~5–10%, stable |

Phase II is the wall. A 2025 analysis of more than 20,000 clinical development
programmes puts the overall Phase I → approval rate at around 5%, and it has not
improved.

## What actually kills programmes

| Cause | Share |
|---|---|
| Lack of clinical efficacy | 40–50% |
| Unmanageable toxicity | ~30% |
| Poor drug-like properties | 10–15% |
| Commercial / strategic | ~10% |

**Three quarters of clinical failure is biology, not chemistry.** The molecule
did what it was designed to do and the mechanism was wrong — wrong target, wrong
direction, wrong tissue, or wrong patients. Only 10–15% is the molecule itself.

This is the single most important fact for anyone deciding where to point tooling,
and it points upstream of everything AI drug discovery has mostly been aimed at.
See [[AI in drug discovery — state of the field 2026]].

## Eroom's law

Coined by Scannell and colleagues in 2012: new drugs approved per billion dollars
of R&D has roughly **halved every nine years since the 1950s** — the inverse of
Moore's law, hence the name. Cost per approved therapy now averages around $2.6bn
over 10–15 years, compounding at 8–9% per year in real terms for seven decades
while approval counts stayed roughly flat.

The decline is not explained by the science getting harder in any simple sense.
Attrition being concentrated in Phase II says the industry is spending most of its
money finding out that hypotheses formed years earlier were wrong.

## What demonstrably moves the odds

Three interventions with published effect sizes, all upstream, all about evidence
rather than chemistry:

**Human genetic support ≈ 2.6x.** Nelson et al. (2015) found targets with human
genetic evidence about twice as likely to reach approval; Minikel et al. (2024)
refined it to 2.6x. The effect is strongest for severe Mendelian disorders and
protein-altering variants where the causal gene is unambiguous, and materially
weaker for non-coding GWAS association where it is not. Modelling suggests raising
the share of pipeline drugs with genetic support from 15% to 50% would cut R&D
cost per launched drug by 22 ± 13%.

**Biomarker stratification: 1.6% → 10.7%.** In oncology, programmes that select
patients on a biomarker reach a 10.7% probability of success against 1.6% for
those that do not — nearly seven-fold. Enrolling the wrong patients, not a weak
molecule, is a leading cause of late-stage failure.

**Better target validation ≈ 24% less Phase II attrition**, with about 30% lower
development cost, on modelled estimates.

## The reproducibility floor under all of this

Begley and Ellis (Nature, 2012): Amgen's oncology group tried to replicate 53
landmark preclinical papers and reproduced **6**. Twenty of the attempts involved
travelling to the original lab to watch the experiment redone blinded. Forty-seven
irreproducible studies had already spawned whole subfields and hundreds of
secondary publications.

The consequence for tooling: **an unreplicated result and a replicated one cannot
be weighted the same**, and a system that counts papers is counting citations of a
possibly-false original. This is why the engine's atoms carry a replication count
and a `disputed` flag, and why refuting evidence has to be able to lower a score.

## The pattern behind the failures worth studying

- **CETP / torcetrapib** — strong biomarker effect (HDL-C +72%), large literature,
  genetic association. Increased mortality. The surrogate moved and the outcome
  did not follow. Correlative evidence dressed as causal.
- **IL-17A in Crohn's** — correct pathway, replicated biology, spectacular
  efficacy in psoriasis. Secukinumab worsened Crohn's and the trial stopped early:
  IL-17A protects the intestinal barrier while driving skin pathology. *Same
  pathway, opposite sign, different tissue.*
- **BACE1 in Alzheimer's** — genuinely correct, correctly directioned human
  genetics (APP A673T reduces cleavage ~40% and protects). Verubecestat and
  atabecestat failed with worsened cognition. Lifelong 40% reduction from birth is
  not the same intervention as 90% inhibition in symptomatic disease. **Genetic
  support fixes direction, not the effect size available from intervening late.**
- **SOST / romosozumab** — worked, and carries a boxed cardiovascular warning.
  Wnt signalling acts on vascular calcification as well as bone, and that edge was
  in the literature before ARCH read out.

Three of the four were predictable from evidence structure rather than from new
experiments. That is the opening.

## Sources

- Phase transition probabilities: 2025 analyses of >20,000 development programmes
- Failure attribution: standard 40–50% / 30% / 10–15% / 10% breakdown
- [Minikel et al. 2024, refining the impact of genetic evidence on clinical success](https://pubmed.ncbi.nlm.nih.gov/38632401/)
- [Nelson et al. 2015 / King et al. 2019, PLOS Genetics](https://journals.plos.org/plosgenetics/article?id=10.1371%2Fjournal.pgen.1008489)
- [Begley & Ellis 2012 and the reproducibility literature](https://issues.org/ending-reproducibility-crisis-medical-research-brownlee-bielekova/)
- [Eroom's law](https://en.wikipedia.org/wiki/Eroom's_law), Scannell et al., Nat Rev Drug Discov 2012
- Biomarker stratification POS: oncology probability-of-success analyses

Related: [[Evidence classes in target validation]] · [[Literature-based discovery and hypothesis generation]] · [[Pharma target-hypothesis engine]]
