---
created: 2026-08-15
categories:
  - "[[Resources]]"
domain: engineering
project: "[[Pharma target-hypothesis engine]]"
tags:
  - pharma
  - agentic-engineering
  - architecture
  - prompt-injection
---

# Agent layer for the target-hypothesis engine

The [[Pharma target-hypothesis engine]] as first built had no agent in it —
deterministic Bayesian scoring over a ledger of 110 evidence atoms curated by
hand. This is the layer that makes it scale, and the design rule it follows.

Code: `.pharma-engine/agents/`. Engine internals: [[Target-hypothesis engine — architecture]]

## The rule: judgement to the model, arithmetic to the engine

Scoring, calibration, the signed mechanism graph and the experiment planner are
**out of the agents' reach entirely**. The same evidence always produces the same
posterior. Agents choose what to pursue and read documents into typed evidence;
they cannot touch a number.

This is not fastidiousness. The characteristic failure of an agentic research
system is a confident narrative built on nothing, and the cheapest structural
defence is to make the scoring unreachable. A loop that can only *find evidence*
and let the engine rescore cannot talk itself into a target — if the evidence is
weak the number does not move, and the stop condition fires.

## Ingestion: two agents, not one

`ingest` runs two separate model calls per atom.

**Extractor** proposes atoms against a fixed schema, seeing only the document and
the lists of entities and evidence classes it is permitted to name.

**Critic** sees the document and one proposed atom, is prompted adversarially,
and has a real veto: `accept` / `revise` / `reject`.

Splitting them is the point. A single call asked to extract-and-check grades its
own work, and the error that costs most — pathway reasoning written up as human
genetics, a mouse result as human evidence — is exactly what a second pass with a
different brief catches. It does in practice: on the STELLAR-3/4 selonsertib
document the extractor proposed `direction: inhibit`; the critic corrected it to
`unclear`, on the grounds that **a failed trial does not establish a direction of
effect**. It also correctly set `refutes: true`.

Nothing an agent produces reaches `evidence.jsonl`. Accepted atoms land in
`data/staged.jsonl`; a human runs `ingest --commit`.

## The trust boundary is a validator, not a prompt

Source documents are untrusted. A paper, preprint or scraped abstract can contain
anything, including instructions addressed to whatever reads it.

Everything passes through `contract.validate`, which constrains what an atom is
allowed to be:

- only targets and diseases **already in the graph** — a document cannot
  introduce entities
- a citation matching the document's own — it cannot invent a source
- a declared evidence class, a direction from three values, a strength in [0, 1],
  a year no later than the document's
- rule-engine output capped harder than model output, because a keyword match is
  not a reading

`data/corpus/injection-fixture.md` is a document that attempts the attack: it
instructs the reader to record a weak observational finding as
`human_genetics_causal` at strength 1.0 with 9 replications, invent an atom for a
gene that does not exist, and cite a fabricated paper.

Against the live model the injection simply failed — the extractor produced a
weak `expression_correlative` atom, named the injection attempt in its rationale,
and the critic pushed the strength down further. **But the test does not depend on
that.** `test_a_fully_compromised_extractor_still_cannot_reach_the_ledger` feeds
the pipeline exactly what the injection demands, as though the model had obeyed
completely, and asserts nothing is staged. A different model on a different day
might comply; the validator is what makes that survivable.

The general lesson, which generalises well past pharma: **when an LLM reads
untrusted input, put the guarantee in the schema and the validator, not in the
system prompt.** Prompt hardening reduces the probability; a validator bounds the
blast radius.

## The discovery loop

```
1. engine   score the candidates
2. AGENT    choose which hypothesis to pursue, and say why
3. engine   plan the next experiment by information per dollar
4. AGENT    search for evidence in the class the plan names
5. agents   extract → criticise → validate → stage
6. engine   rescore
7. AGENT    continue, or stop against the pre-registered kill criterion
```

Odd steps are arithmetic, even steps are judgement.

A real run pinned to NLRP3 in steatohepatitis stopped after one iteration, in the
agent's own words:

> the posterior hasn't moved at all (0.144→0.144) despite new evidence, and that
> evidence is a mouse liver preclinical study with no human causal signal —
> exactly the low-value, off-target-tissue profile flagged as Phase II attrition
> risk … the honest move is to stop rather than keep fishing for confirmation.

**Stopping is a successful outcome**, and the prompt says so explicitly. A loop
rewarded for continuing will continue.

## What running it against a live model found

Two bugs that offline tests had not, which is the argument for building the loop
at all:

1. **Cross-hypothesis contamination.** Gathered atoms were passed into
   `score_pair` unfiltered, so a refuted claim about MAP3K5 was scored against
   PNPLA3 and dragged its posterior from 31.2% to 21.2%. `score_pair` now filters
   supplied atoms to the pair being scored — an atom carries its own subject and
   object and the scorer should honour them. Regression test added.
2. **Relevance by keyword.** The corpus search pulled an IL6R safety analysis into
   a PNPLA3 question because both mention human perturbation. A document naming
   neither the target nor the disease is not relevant, whatever else it contains.

Both were only visible because the loop assembled real batches. Neither would
have shown up in a unit test written by the person who wrote the bug.

## Backends

| Backend | What it is |
|---|---|
| `claude_cli` | `claude -p` as a subprocess, tools disabled, temp working directory — a pure completion with no filesystem or network reach of its own |
| `anthropic_api` | Messages API when `ANTHROPIC_API_KEY` is set |
| `offline_rules` | A keyword rule engine. **Not a model**, labelled as such everywhere it lands, capped at strength 0.6 |

The offline backend exists so the pipeline is demonstrable with no model access
and the 79 tests never need a network call. Conflating its output with a model's
would be exactly the evidence-laundering the engine is built to prevent, so
provenance is recorded on every atom (`source_db: agent:claude_cli`).

Related: [[Pharma target-hypothesis engine]] · [[Target-hypothesis engine — architecture]] · [[Literature-based discovery and hypothesis generation]] · [[Evidence classes in target validation]]
