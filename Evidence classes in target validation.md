---
created: 2026-08-14
categories:
  - "[[Resources]]"
domain: health
tags:
  - pharma
  - target-validation
  - evidence
project: "[[Pharma target-hypothesis engine]]"
---

# Evidence classes in target validation

Not all evidence that a target matters in a disease is the same kind of evidence,
and the differences are large enough to decide programmes. This is the taxonomy
underneath [[Pharma target-hypothesis engine]], with the calibration each class
gets and why.

## The classes, ranked by what they buy

| Class | Ceiling (LR) | What it observes |
|---|---:|---|
| Human perturbation — drug or Mendelian randomisation | 3.2x | The target was actually modulated in a human and the phenotype moved |
| Human genetics, causal-grade | 2.6x | Coding/Mendelian variant, clear causal gene, known direction |
| Perturbation biology | 1.9x | CRISPR or tool compound in human disease-relevant cells |
| Clinical precedent in a related indication | 1.9x | A modulator worked in humans, in a different disease |
| Human genetics, common variant | 1.7x | GWAS association without confident gene assignment |
| Model organism | 1.35x | Mouse knockout phenotype |
| Expression correlation | 1.25x | Differentially expressed in patient tissue |
| Pathway inference | 1.2x | Sits on a pathway that is linked to the disease |
| Literature co-occurrence | 1.12x | Discussed together |

The 2.6x for causal-grade genetics is the [Minikel 2024 figure](https://pubmed.ncbi.nlm.nih.gov/38632401/),
not a chosen weight. The rest are ordered by translational track record.

## The four distinctions that matter most

### 1. Independence, not volume

Ten papers of the same kind are one line of evidence with a citation count. A GWAS
hit and a coding-variant burden test at the same locus read the *same human
genetic signal twice*; differential expression and literature co-mention are
largely the same fact about how fashionable a gene is.

Grouping classes by what they physically observe — human genetics, human
perturbation, experimental biology, correlative — and letting only the strongest
class in a group count in full is the difference between a system that accumulates
confidence and one that measures it. **Breadth across groups beats depth within
one.**

### 2. Direction of effect

An association says the target matters. It does not say whether to inhibit or
activate it, and that is the whole molecule.

- **PCSK9** — loss of function protective → inhibit. Evolocumab.
- **TREM2** — loss of function causes risk → *activate*. Agonism, which is much
  harder to drug.
- **GBA1** — loss of function causes risk → restore activity, not block it.
- **GIPR** — genuinely unresolved: agonism is approved for obesity (tirzepatide)
  and loss-of-function variants also associate with lower BMI.

A programme that starts before direction is settled is choosing its modality by
coin flip. Direction conflict is a finding, not a number to average.

### 3. Tissue context

Evidence generated where the pathology is not does not transfer. **IL-17A** is the
case: correct pathway, replicated biology, and secukinumab produced PASI75 in ~80%
of psoriasis patients — while worsening Crohn's disease badly enough to stop the
trial. IL-17A protects the intestinal epithelial barrier and drives skin
pathology. Same molecule, same pathway, opposite sign.

### 4. Evidence can point down

Failed replications and negative clinical readouts have to be able to *lower* a
score, or a knowledge base only ever ratchets upward and eventually ranks whatever
is best studied. Given that [6 of 53 landmark preclinical papers replicated](https://issues.org/ending-reproducibility-crisis-medical-research-brownlee-bielekova/),
this is not a corner case.

## The genetic-only caveat

Germline variation is a **lifelong exposure of modest magnitude**. It establishes
that a target is causal and in which direction. It says remarkably little about
what a large, late pharmacological intervention achieves.

APP A673T reduces BACE1 cleavage by ~40% from birth and protects against
Alzheimer's. Roughly 90% BACE1 inhibition started in symptomatic patients worsened
cognition. Both facts are true and the genetics did not predict the second.

No published effect size exists for this gap, so the engine flags it rather than
pricing it — inventing a number here would be worse than naming the question.

## On-target safety comes from the same evidence

Mendelian randomisation run phenome-wide (MR-PheWAS) predicts adverse effects
before dosing anyone: genetically proxied IL-6 signalling inhibition flags atopic
dermatitis, cellulitis, urinary tract infection and cholecystitis. The same
variant that proxies efficacy proxies the side effects.

Mechanism paths do the same work structurally. Sclerostin inhibition builds bone
through Wnt; Wnt also acts on vascular calcification; romosozumab carries a boxed
cardiovascular warning. That edge was public before ARCH read out.

**Safety belongs on its own axis, never folded into the efficacy probability.** A
mechanism can be true and undevelopable, and merging the two destroys the one
thing a portfolio decision needs: which of the two is the problem. Tractability is
separate for the same reason — under 5% of the human proteome has been
successfully drugged, which is why [Target 2035](https://pubs.rsc.org/md/article/13/1/13/731903/Target-2035-update-on-the-quest-for-a-probe-for)
exists.

## Sources

- [Minikel et al. 2024](https://pubmed.ncbi.nlm.nih.gov/38632401/) — genetic support 2.6x
- [Open Targets evidence datatypes and scoring](https://academic.oup.com/nar/article/49/D1/D1302/5983621)
- [Mendelian randomisation for adverse-event prediction](https://academic.oup.com/ije/article/46/6/2078/4430993)
- [Target 2035 — a probe for every protein](https://pubs.rsc.org/md/article/13/1/13/731903/Target-2035-update-on-the-quest-for-a-probe-for)
- Hueber et al., Gut 2012 (secukinumab in Crohn's); Jonsson et al., Nature 2012 (A673T); Egan et al., NEJM 2018/2019 (verubecestat)

Related: [[Why drug programmes fail]] · [[Pharma target-hypothesis engine]] · [[Target-hypothesis engine — architecture]]
