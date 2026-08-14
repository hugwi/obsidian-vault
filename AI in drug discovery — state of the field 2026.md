---
created: 2026-08-14
categories:
  - "[[Resources]]"
domain: health
tags:
  - pharma
  - ai
  - drug-discovery
project: "[[Pharma target-hypothesis engine]]"
---

# AI in drug discovery — state of the field 2026

Where the field actually is, gathered while building
[[Pharma target-hypothesis engine]]. The summary: AI has demonstrably compressed
the discovery phase and has not yet moved the phase that fails.

## The pipeline

- **170+ AI-discovered programmes** in clinical development as of early 2026;
  15–20 expected to enter pivotal trials during the year.
- First approvals anticipated 2026–2027.
- **No approved AI-discovered drug yet.**

## The honest split

The field has bifurcated cleanly:

**On the discovery side, it works.** Molecules designed with AI reach the clinic
faster and cheaper than industry benchmarks. Exscientia's DSP-1181 completed
exploratory research in under 12 months against a several-year norm. Recursion's
REC-4881 (MEK1/2, familial adenomatous polyposis) produced the first published
clinical validation of a full-stack AI discovery platform: polyp burden reduced in
75% of evaluable patients, 43% median reduction at 12 weeks.

**On the clinical side, nothing has changed.** AI discovery does not shorten Phase
II or Phase III, does not avoid the underlying biology of efficacy and safety, and
has not produced an approval. DSP-1181 itself was discontinued after Phase I
results disappointed. Recursion discontinued three clinical-stage programmes in
May 2025, including REC-994 in cerebral cavernous malformation — despite a Phase 2
readout showing lesion volume reduced in 50% of high-dose patients against 28% on
placebo.

## Why that is exactly what the base rates predict

From [[Why drug programmes fail]]: 40–50% of clinical failure is lack of efficacy
and ~30% is toxicity, against 10–15% for drug-like properties. **AI has been
applied hardest to the 10–15%.** Faster, better molecules against a wrong target
fail faster and better.

Speeding up the cheap part of a process whose expensive part is a wrong hypothesis
does not fix the economics. This is the whole argument for pointing effort at
target and mechanism selection instead.

## Consolidation

Recursion acquired Exscientia in November 2024; BenevolentAI was acquired by Osaka
Holdings in March 2025. The read: pure-play AI biotechs need scale, because
running a discovery engine *and* a real clinical pipeline is expensive enough that
small companies cannot do both. The platform-only business model has largely not
survived contact with clinical timelines.

## What has actually produced new biology

Agent systems working on *hypotheses* rather than molecules, in 2025–2026:

- **Robin** (FutureHouse) — autonomously generated the hypothesis, chose the
  intervention class, analysed the data and wrote the figures for a genuinely new
  finding: ripasudil, an approved glaucoma drug, enhances RPE phagocytosis and is
  a candidate for dry AMD. Humans ran the assays. Two and a half months.
- **Co-Scientist** (Google DeepMind) — found approved drugs repurposable for a
  leukaemia subtype within hours, with human guidance.
- **BenevolentAI, 2020** — baricitinib for COVID-19 from a knowledge graph, later
  confirmed in ACTT-2 and COV-BARRIER.

All three are hypothesis generation over structured biological knowledge, not
molecule generation. All three kept a human in the loop. See
[[Literature-based discovery and hypothesis generation]].

## What this implies for building anything here

1. **Don't build another molecule generator.** That part is served and is not the
   bottleneck.
2. **Target selection, direction of effect, patient selection and falsification
   are where the value is** — the three interventions with published effect sizes
   (genetic support 2.6x, biomarker stratification 1.6% → 10.7%, better target
   validation ≈24% less Phase II attrition) are all in that band.
3. **The output has to be a decision, with its reasoning exposed.** Both validated
   successes above were expert-augmented. A ranked list that cannot be argued with
   is not usable by the people who have to sign for a programme.

## Sources

- [AI-discovered drugs in clinical trials 2026 — pipeline](https://intuitionlabs.ai/articles/ai-discovered-drugs-clinical-trials-2026)
- [Recursion / Exscientia combination](https://ir.recursion.com/news-releases/news-release-details/recursion-and-exscientia-two-leaders-ai-drug-discovery-space)
- [AI lab partners are rewiring the hunt for new drugs, 2026](https://singularityhub.com/2026/05/21/ai-lab-partners-are-rewiring-the-hunt-for-new-drugs/)
- [AI companies introduce agent-based research tools, C&EN 2026](https://cen.acs.org/pharmaceuticals/drug-discovery/ai-companies-introduce-agent-based-research-tools/104/web/2026/05)
- [FutureHouse Robin announcement](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system)

Related: [[Why drug programmes fail]] · [[Pharma target-hypothesis engine]]
