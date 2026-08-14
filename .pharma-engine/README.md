# Target-hypothesis engine

A working prototype of a decision system for early drug discovery. It takes the
evidence linking a molecular target to a disease, and returns a calibrated
probability that the mechanism would survive clinical development, the direction
you would have to push the target, the on-target safety it implies, and the
cheapest experiment that could kill it.

Python 3.11, standard library only. No install step.

```bash
python3 -m unittest discover -s tests      # 43 tests
python3 cli.py rank                        # rank everything in the ledger
python3 cli.py explain SOST OSTEOPOROSIS   # the full argument for one pair
python3 cli.py discover DRY_AMD            # propose targets with no direct evidence
python3 cli.py plan TREM2 AD --budget 200000
python3 cli.py backtest                    # time-split evaluation
python3 cli.py rediscover                  # blind rediscovery of known findings
python3 cli.py export --out digest.md      # write an Obsidian note
python3 cli.py sources                     # probe the live data connectors
```

Every command takes `--as-of YEAR` to restrict the ledger to what was knowable
then.

---

## Why this rather than a better molecule generator

The economics say where the leverage is. Roughly 90% of programmes entering the
clinic never reach approval, Phase II is the worst gate at about 28%, and the
single largest cause of failure is lack of efficacy at 40–50%, with on-target
toxicity behind it at about 30%. Three quarters of clinical failure is therefore
biology: the target-disease hypothesis was wrong, or right in the wrong tissue,
or right in the wrong patients. Chemistry accounts for roughly 10–15%.

AI has been applied mostly to the 15%. As of early 2026 there are 170+
AI-discovered molecules in clinical development and no approvals; the field's own
retrospective is that AI discovery has shortened the design phase and has not
moved Phase II. Meanwhile the interventions that demonstrably move the odds are
all upstream and all evidential:

- **Human genetic support** roughly doubles the probability of approval — 2.6x in
  the refined estimate, strongest for coding variants and Mendelian disorders
  where the causal gene is unambiguous.
- **Biomarker-based patient stratification** in oncology takes probability of
  success from 1.6% to 10.7%.
- **Better target validation** is modelled to cut Phase II attrition by about a
  quarter.

So the prototype scores mechanisms, not molecules, and it is built to be argued
with rather than trusted.

## What it does that existing tooling does not

Open Targets is the reference implementation of target-disease scoring: it
integrates 20+ sources into ~7.8M associations and aggregates them with a
weighted harmonic sum across data sources and data types. It is excellent at what
it is for — finding what is known. It is not built to make a decision, and four
things get lost on the way to one.

**1. Correlated evidence compounds.** A GWAS hit and a coding-variant burden test
at the same locus are one human genetic signal read twice; a differential
expression result and a literature co-mention are largely the same fact about how
fashionable a gene is. Summing them is how a scoring system talks itself into a
target. Here, classes are grouped by *what they physically observe*, and inside a
group only the strongest class counts in full — the rest are damped to 35%. Across
groups, evidence multiplies as independent likelihood ratios.

**2. Scores only go up.** A ledger that can only accumulate will eventually rank
every well-studied target highly. CETP is the case: the HDL hypothesis had a
strong biomarker effect, a large literature and genetic association, and
torcetrapib raised HDL-C by 72% while increasing mortality. Atoms here can carry
`refutes: true` and contribute a negative log-likelihood-ratio, so a failed trial
or a failed replication pushes the mechanism down. CETP scores 6.6%, below the
10% base rate.

**3. Direction of effect is dropped.** An association says the target matters, not
whether to inhibit or activate it. GIPR is a live example: agonism is approved for
obesity, and loss-of-function variants also associate with lower BMI. The engine
refuses to average those, flags `DIRECTION-CONFLICT`, and puts a direction-
resolution study at the top of the plan instead of a number.

**4. The output is a ranking, not a decision.** A researcher cannot act on
"association score 0.72". They can act on "sclerostin in osteoporosis: 48%
chance this mechanism survives; you must inhibit; the antibody route is open; the
vascular calcification path is a real risk; and a $120k CRISPR study in
patient-derived cells is the cheapest thing that could kill it, taking 48% to 25%
if it reads negative."

## How the score is built

Four levels:

```
atoms  ->  class score     saturating combination within one evidence class
class  ->  class log-LR    class score x that class's calibrated ceiling
class  ->  group log-LR    strongest class in full, correlated siblings damped 0.35
group  ->  posterior       sum of group log-LRs applied to a 10% base rate
```

Class ceilings are anchored to published estimates, not chosen for effect —
causal-grade human genetics tops out at 2.6x because that is the measured figure,
human perturbation (an actual drug, or Mendelian randomisation) at 3.2x, mouse
knockout at 1.35x, literature co-occurrence at 1.12x. The total likelihood ratio
is capped at 26x, so no accumulation of evidence can push a mechanism past ~74%.
Even textbook mechanisms fail for reasons no evidence model contains.

Within-class aggregation defaults to a rank-damped noisy-OR,
`1 - prod(1 - s_i / i^2)`. `--saturation harmonic` reproduces the Open Targets
normalisation for comparability; it is not the default because dividing by the
maximum theoretical harmonic sum (~1.6449) is calibrated for data sources carrying
hundreds of evidence strings, and against a curated handful it would deflate a
Mendelian human knockout to 0.6 of its strength.

Two things are deliberately kept **out** of the probability and reported as
separate coordinates:

- **Tractability**, because under 5% of the human proteome has been successfully
  drugged and a mechanism can be true and undevelopable. Agonism carries an extra
  penalty — "the genetics is beautiful, the molecule is impossible" is a real and
  common failure mode, and TREM2 is its current exemplar.
- **Safety**, because folding it in destroys the one thing a portfolio committee
  needs, which is *which* of the two is the problem.

## Mechanism paths, and the signs on them

The graph carries polarity on every edge, so the product of signs along a path
gives the therapeutic direction. `SOST --|inhibits Wnt --> drives bone formation
--| prevents osteoporosis` is two negatives: inhibit sclerostin. The same
machinery, walked outward instead of inward, is what predicts on-target harm:
`SOST --| Wnt --> vascular calcification` was in the literature years before
romosozumab's cardiovascular imbalance in ARCH became a boxed warning. The engine
reports it as a moderate signal from the graph, clearly labelled as derived from
mechanism rather than from a trial.

Disease nodes may only be endpoints, never waypoints. Without that rule the walk
routes through whichever disease has the most edges and manufactures chains like
`HMGCR -> LDL clearance -> cardiovascular disease -> NLRP3 -> Alzheimer's`, which
reads as an argument for statins in dementia and is nothing of the kind.
Hub-hopping is the standard way literature-based discovery produces plausible
nonsense at volume.

## Generating hypotheses, not just scoring them

`discover DISEASE` is the open-discovery form of Swanson's ABC model: fix the
disease, walk out through pathways and processes, and collect targets with no
direct evidence linking them to it. Two additions make the output usable.

Generated hypotheses enter the same scoring engine as a single pathway-inference
atom — the weakest class there is — so they land near the base rate. That is
correct and it is the point: an inference is not competitive with a human
knockout, and a system that lets generated hypotheses outrank evidenced ones is
generating enthusiasm, not knowledge. What makes them worth reading is the pairing
with the experiment planner, and the note when the target already has an approved
molecule — then the test is a trial, not a decade.

**Evidence transfer** carries what is known about pathway siblings across, with
the sign. If MERTK must be *activated* to restore retinal pigment epithelium
phagocytosis, and ROCK *constrains* the same process, then the borrowed direction
inverts and the engine says *inhibit* ROCK. That is not a coincidence of the
example — it is the mechanism by which pathway reasoning produces real
candidates, made explicit so it can be weighted and audited instead of arriving
as an unexamined intuition.

## Deciding what to do next

Each evidence class carries a sensitivity, a specificity and an acquisition cost,
which makes any experiment a noisy test of the hypothesis and its value ordinary
expected information gain:

```
p+   = P(H)*sens + (1-P(H))*(1-spec)
EIG  = H(P(H)) - [ p+ * H(P(H|+)) + (1-p+) * H(P(H|-)) ]      bits
```

Divided by cost, this gives bits per $100k — the number that should drive a
discovery budget and rarely does. Differential expression is usually the cheapest
item on the list and almost always near the bottom of it, because specificity of
0.30 buys very little information however little it costs. A mouse knockout costs
$250k, takes a year, and has specificity 0.45.

The **kill experiment** is named separately: the work whose negative result would
most reduce the posterior per dollar, with the number you would have to accept
printed before you start. Pre-registering the stopping rule is what converts a
hypothesis into something falsifiable, and it is the difference between a
programme that stops in year two and one that stops in Phase II.

## Does it work? — the two evaluations

`backtest` scores real programmes using only evidence published **before** their
clinical entry year, then asks whether approvals outrank failures.

```
AUC 0.63 over all 19 scored programmes
AUC 0.38 over the 15 where the ledger held any pre-entry evidence
mean posterior 15.2% approved vs 14.2% failed
```

The second number is below chance and is the most useful output of the whole
exercise, so it is reported rather than buried. It has two causes.

The trivial one is sample size: the covered subset contains 2 failures. An AUC
over 13 positives and 2 negatives is not a statistic, and one case moves it
across chance.

The substantive one is that case. Restricted to pre-2013 evidence, the engine
scores BACE1 in Alzheimer's at 25.7%, above PCSK9 in cardiovascular disease at
22.4% — and BACE1 failed while PCSK9 was approved. The reason is instructive:
both rest on the same class of evidence, correctly directioned human genetics
(APP A673T reduces BACE1 cleavage ~40% and protects against Alzheimer's), and
BACE1 edges ahead only on a mouse knockout. Nothing in the model distinguishes a
lifelong 40% reduction present from birth from 90% pharmacological inhibition
started in symptomatic disease. That distinction is exactly what killed
verubecestat.

The engine now flags this rather than pretending to price it. Any hypothesis
supported by germline genetics with no human perturbation evidence carries
`GENETIC-ONLY`, stating that the evidence fixes direction but not the effect size
obtainable from intervening late. Quantifying the gap would mean inventing a
number; naming it puts the question in front of whoever reads the card. The
honest position is that this is a known blind spot with a warning attached, and
closing it properly needs an evidence class for intervention timing that the
current ledger has no data to populate.

The other limitation is coverage rather than scoring: the snapshot holds little
pre-2005 evidence for programmes that entered the clinic in the 1990s, and those
score at the base rate by construction.

The calibration table the command prints should be ignored — `outcomes.json` is a
list of programmes famous enough to curate, so it is ~80% approvals against a true
base rate nearer 10%. Observed frequencies in it measure the sampling, not the
engine. Discrimination survives that bias; calibration does not.

`rediscover` is the stronger test. Ground truth lives in `data/discoveries.json`,
which the scoring path never reads.

| Case | Cutoff | Result |
|---|---|---|
| ROCK inhibition in dry AMD | 2024 | **rank 1 of 3**, direction `inhibit`, via `ROCK -> Rho/ROCK actin regulation -\| phagocytosis -> RPE phagocytosis -\| dry AMD` |
| AAK1 in COVID-19 | 2019 | **rank 1 of 1**, direction `inhibit`, via `AAK1 -> clathrin-mediated endocytosis -> viral entry -> COVID-19` |

The first is the hypothesis FutureHouse's Robin system generated autonomously in
2025 and then confirmed at the bench — ripasudil, an approved glaucoma drug,
increased RPE phagocytosis. The second is BenevolentAI's 2020 identification of
baricitinib, which went on to reduce mortality in ACTT-2 and COV-BARRIER. Both
were recovered from a graph restricted to before the discovery.

Read the COVID case with its caveat: the disease node's edges are dated 2020, so
`allow_new_disease_node` exempts them from the cutoff. What is being tested is
whether the engine can bridge an existing mechanism to a new disease, not whether
it could have anticipated a pandemic. And "rank 1 of 1" means the candidate pool
was one — a clean hit, but a small test.

## On the data

`data/` is a hand-curated snapshot of about 110 evidence atoms across 40 targets,
15 diseases, 14 pathways and 9 processes, drawn from the published literature.
Every atom carries a citation and a year. Citations are given as
author/journal/year rather than as accession numbers, deliberately: a
hand-assembled identifier that looks authoritative and is wrong is worse than a
reference a reader can check.

This snapshot exists so the prototype runs and can be evaluated. It is not a
knowledge base. The real ledger comes from `engine/connectors.py`, which pulls
Open Targets (evidence by datatype, tractability buckets, and the Platform's own
association score as a comparator), Europe PMC (co-occurrence, for the novelty
term), ClinicalTrials.gov (what has already been tried — an "unprecedented" target
with six terminated Phase II trials is not unprecedented, it is unpublished) and
ChEMBL (whether a chemical probe exists).

**In this environment those connectors do not run.** The egress policy refuses
CONNECT to `api.platform.opentargets.org`, `www.ebi.ac.uk` and
`clinicaltrials.gov`. `python3 cli.py sources` reports exactly which sources are
reachable and why, rather than silently returning empty results — a connector that
fails quietly is worse than one that fails loudly, because the scores it produces
still look reasonable.

## What this prototype is not

- **Not validated.** Two dozen curated programmes and two rediscovery cases
  demonstrate that the reasoning is sound and the ordering is not accidental. They
  do not establish that the probabilities are right. That needs a full unselected
  cohort of programmes with entry dates and outcomes.
- **Not a replacement for Open Targets.** It consumes that kind of data. The
  contribution is the decision layer on top.
- **Not automated science.** It ranks and prices hypotheses. Humans run the
  experiments, and the framing throughout is that the engine's job is to be
  argued with — every number decomposes into atoms with citations, so a
  disagreement can be located at a specific piece of evidence rather than at a
  score.
- **Not safe against a bad ledger.** Curation quality is the ceiling on
  everything here. `LedgerIntegrityTests` enforces that atoms carry citations,
  years, known entities and declared classes, and that rediscovery ground truth
  has not leaked — but nothing checks that a strength of 0.9 was deserved.

## Layout

```
cli.py                    commands
engine/model.py           Entity, EvidenceAtom, Hypothesis, Experiment
engine/ledger.py          loading, temporal slicing (as_of), queries
engine/scoring.py         saturation, direction resolution, group combination
engine/graph.py           signed mechanism paths, ABC discovery, evidence transfer
engine/safety.py          pleiotropy and mechanism-path safety
engine/experiments.py     expected information gain per dollar, kill criterion
engine/backtest.py        time-split discrimination, blind rediscovery
engine/report.py          terminal tables, hypothesis cards, Obsidian notes
engine/connectors.py      live sources, with honest failure
data/priors.json          every calibration constant, cited or marked an assumption
data/evidence.jsonl       the atoms
data/entities.json        targets, diseases, pathways, processes, drugs, signed edges
data/outcomes.json        backtest ground truth
data/discoveries.json     rediscovery ground truth (never read by the scoring path)
tests/test_engine.py      43 invariant tests
```

The folder is dot-prefixed so Obsidian does not index it, following
`.multilabel.py` and `.cluster_work/` in this vault. Findings and design notes
live in the vault as ordinary notes — see `[[Pharma target-hypothesis engine]]`.
