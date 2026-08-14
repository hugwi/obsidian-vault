---
created: 2026-08-14
categories:
  - "[[Resources]]"
domain: health
tags:
  - pharma
  - knowledge-graph
  - hypothesis-generation
  - drug-repurposing
project: "[[Pharma target-hypothesis engine]]"
---

# Literature-based discovery and hypothesis generation

How you generate a *new* target-disease hypothesis rather than re-ranking the ones
that already exist. Background for [[Pharma target-hypothesis engine]].

## Swanson's ABC model

Don Swanson's original insight, from the 1980s: two literatures can each be
complete and correct and still contain a discovery neither has noticed. If
literature 1 links A to B, and a disjoint literature 2 links B to C, then A–C is
implied and may never have been written down.

- **Closed discovery** — A and C given, find the B that connects them.
- **Open discovery** — fix A (or C), find B, collect the C terms (or A terms).

For drug discovery the useful direction is open: fix the disease, walk out through
pathways and processes, collect targets nobody has connected to it.

## Why LBD has a long history and a short list of discoveries

The method generates plausible pairs at enormous volume and leaves a human to sort
them. Three specific failure modes:

**Hub-hopping.** Paths route through whichever node has the most edges. Chains
like `HMGCR → LDL clearance → cardiovascular disease → NLRP3 inflammasome →
Alzheimer's` read as an argument for statins in dementia and are an artefact of
graph topology. The fix is structural: **disease nodes may be endpoints, never
waypoints.** A real mechanism connects through pathways and processes, not through
a second diagnosis.

**No sign.** "These are related" is not a hypothesis. Whether the target should be
inhibited or activated is the entire content of the proposal, and pairwise
co-occurrence graphs cannot carry it. Putting a polarity on every edge and taking
the product along the path recovers it: `SOST ⊣ Wnt → bone formation ⊣
osteoporosis` is two negatives, so inhibit sclerostin.

**Flat representation.** The 2025 literature makes this point directly: modern LBD
systems scale up by relying on entity co-occurrence or bare semantic triples, and
that pairwise representation is where the inference quality is lost.

## What worked, twice

**Baricitinib in COVID-19 (BenevolentAI, 2020).** A knowledge graph built from
dozens of databases plus machine-read text over ~30M PubMed papers, queried
iteratively by humans. It identified clathrin-mediated endocytosis as the likely
SARS-CoV-2 entry route, and baricitinib — a rheumatoid arthritis JAK inhibitor
that also inhibits the numb-associated kinases AAK1 and GAK — as an agent that
would block entry while damping the cytokine response. ACTT-2 and COV-BARRIER
confirmed a mortality reduction; emergency authorisation followed.

Note the paper's own framing: **expert-augmented** computational repurposing. The
graph proposed; humans steered.

**Ripasudil in dry AMD (FutureHouse "Robin", 2025).** A multi-agent system
autonomously hypothesised that enhancing retinal pigment epithelium phagocytosis
could treat dry AMD, selected ROCK inhibitors as the intervention class, and
nominated ripasudil, an approved glaucoma drug. Humans ran the assays; ripasudil
increased RPE phagocytosis. Concept to paper: about two and a half months.

Google DeepMind's Co-Scientist has done something similar for leukaemia
repurposing — described by its authors as a "structured scientific thinking
engine", which is the right level of claim.

**The shared shape of both successes:** an existing approved molecule, a
mechanistic bridge that was already public, and the A–C edge simply never written
down. That is a much better bet than proposing an undrugged target, because the
test is a trial rather than a decade.

## Evaluating a hypothesis generator

Wet-lab validation does not scale, so the field uses time splits: train on
literature before a cutoff, test against what was published after. Datasets get
partitioned by publication year (e.g. train 2000–2020, validate 2021–2022, test
2023–2024). The **Dyport** benchmark adds a measure of discovery *importance*, on
the argument that predicting a trivial link is not the same accomplishment as
predicting a consequential one.

Rediscovering a handful of historical findings is the weaker but more legible
test: expensive, unscalable, and worth doing anyway because it is checkable by a
reader. Both cases above are used that way in the prototype, with the ground truth
held in a file the scoring path never reads.

## The design conclusion

Generated hypotheses should enter the *same* scoring engine as everything else, as
the weakest class of evidence, and land near the base rate. A system that lets
inference outrank a human knockout is generating enthusiasm, not knowledge.

What makes a generated hypothesis worth reading is not its score. It is the
combination of a stated mechanism path, a direction of effect, a note that the
target already has an approved molecule, and a priced next experiment.

## Sources

- [LBD survey and the ABC model](https://arxiv.org/pdf/2310.03766)
- [Enriched knowledge representation in LBD, J Biomed Semantics 2025](https://link.springer.com/article/10.1186/s13326-025-00328-3)
- [Dyport benchmarking framework, BMC Bioinformatics 2024](https://bmcbioinformatics.biomedcentral.com/articles/10.1186/s12859-024-05812-8)
- [Stebbing et al., expert-augmented repurposing → baricitinib](https://pmc.ncbi.nlm.nih.gov/articles/PMC8356560/)
- [FutureHouse: end-to-end scientific discovery with Robin](https://www.futurehouse.org/research-announcements/demonstrating-end-to-end-scientific-discovery-with-robin-a-multi-agent-system)

Related: [[Why drug programmes fail]] · [[Evidence classes in target validation]] · [[AI in drug discovery — state of the field 2026]]
