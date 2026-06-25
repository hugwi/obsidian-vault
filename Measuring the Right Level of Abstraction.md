---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
# Measuring the Right Level of Abstraction

How do you know if code is at the right abstraction level? We explored this through a hands-on experiment: taking one real production handler, rewriting it at three different abstraction levels, questioning every name, and then building an LLM-based technique to measure name-to-implementation alignment.

Related: [[Levels of Abstraction]], [[Abstraction Level Best Practices]]

## The Question

The best practice says: "Top-level code should read like a book — intention-revealing steps in domain language, no low-level operations." But that raises a harder question: how do you know when you've hit the right level? Too low and the reader is decoding mechanics. Too high and the reader is guessing what the abstractions actually mean.

The sweet spot is where a reader can explain what the function does from its name and body, without opening any children, and without feeling like the names are hiding the story behind vague containers.

## Three Levels of the Same Handler

We used `BrowserSessionSignalHandlerService.handle()` — a production handler that processes browser session signals — as the test case.

### Too Low: The Current Handler

```ts
async handle(job: SignalDispatchJobData): Promise<void> {
  this.assertJobShape(job);
  const payload = job.envelope.payload as unknown as BrowserSessionPayload;
  const observedAt = new Date(job.envelope.observedAt);
  const decision = await this.triageService.classify(job.workspaceId, { ... });
  const vendorEntry = resolveByDomain(payload.domain) ?? null;

  await this.dataSource.transaction(async (manager) => {
    // 40 lines of branching, persistence, dedup
  });

  await this.recordCacheVisitIfAttributed(job, vendorEntry, decision);
  await this.upsertDiscoveredPrimaryDomain(job, payload, decision);
  await this.evaluateDomainPromotion(...);
  await this.notifyDiscoveredVendorUsageIfApplicable(...);
}
```

The post-commit steps read well. But the transaction block mixes abstraction levels — it inlines triage branching, persistence sequencing, and dedup logic. The `let` mutations leak implementation state. A reader has to mentally execute the transaction to understand what happens.

Where it sits on the ladder:
- Orchestration pattern: ⚠️ — transaction block computes instead of delegating
- Summary Test: mostly passes, but the transaction block requires opening
- Same-Level Rule: ❌ — mixes domain branching with persistence mechanics
- Vocabulary Ratio: mixed — `dataSource`, `manager`, `isNew` leak upward
- DDD layers: ⚠️ — `DataSource.transaction` is infrastructure in the application layer

### Too High: The Over-Compressed Version

```ts
async handle(job: SignalDispatchJobData): Promise<void> {
  const command = this.buildIngestionCommand(job);
  const outcome = await this.browserSessionIngestion.persist(command);
  await this.browserSessionPostCommitEffects.run(outcome);
}
```

Three lines. No branching. No mechanism words. Passes every mechanical checklist. But can you explain what it does?

- `buildIngestionCommand` — what does ingestion mean here? What goes into a "command"?
- `browserSessionIngestion.persist` — persist what? Evidence? Raw rows? Audit logs? All of them?
- `browserSessionPostCommitEffects.run` — what effects? Cache? Notifications? Promotion?

This is the "bad abstraction" case from the best practices note:

```ts
processData(input)
handleStuff(result)
performOperation(context)
```

It passes the form but fails the substance. The names are clean but they hide the story behind vague containers. A reader who wants to understand what this handler does has to open every child.

### The Right Level: Intention-Revealing Orchestration

```ts
async handle(job: SignalDispatchJobData): Promise<void> {
  const signal = this.validateAndParseSignal(job);

  if (await this.shouldDropSignal(signal)) {
    await this.recordDropAuditLog(signal);
    return;
  }

  const identityPolicy = await this.resolveIdentityPolicy(signal);
  const evidence = await this.persistEvidence(signal, identityPolicy);

  if (evidence === null) return;

  await this.updateUserSignalCache(signal, evidence, identityPolicy);
  await this.upsertDiscoveredDomain(signal);
  await this.evaluateDiscoveredDomainPromotion(signal, evidence);
  await this.notifyDiscoveredVendorUsage(signal);
}
```

A reader can say: "It validates the signal, checks if it should be dropped, resolves what identity policy applies, persists evidence, then updates cache, domain discovery, promotion, and notification." No child needs to be opened. No vague containers. The decision space (drop vs keep) is visible at the top level.

Where it sits:
- Orchestration pattern: ✅ — every line is a domain step
- Summary Test: ✅ — fully explainable without opening children
- Same-Level Rule: ✅ — all lines at application level
- Vocabulary Ratio: ✅ — domain words only
- DDD layers: ✅ — transaction hidden behind `persistEvidence`

## Questioning the Names

The right-level version surfaced a deeper question. Even with good structure, individual names can mislead.

### "What does `classifyThroughTriage` do?"

"It classifies the signal through triage."

### "What is triage? What does it classify?"

The name assumes you know what "triage" means in this domain. Triage is a medical term meaning "sort by priority under scarcity." What this code actually does is decide what happens to the signal's personal data.

### "Is 'triage' the clearest word?"

No. The three outcomes are:
- **Drop** — discard the signal, keep no data
- **Anonymize** — keep the signal but strip the person's identity
- **Attribute** — keep the signal with the person's identity attached

A clearer name would reflect that: `classifySignalPrivacy` or `resolveIdentityDisposition`.

### "But can you tell what the outcome is?"

No. No function name can tell you the decision space. You know a "decision" comes back, but not that it's one of DROP, ANONYMIZE, or ATTRIBUTE. That matters because the entire handler branches on it.

For decision spaces, the branching should be visible at the level where it matters:

```ts
if (await this.shouldDropSignal(signal)) {
  await this.recordDropAuditLog(signal);
  return;
}
```

Now the reader discovers the decision space by reading the handler. "Drop" is one path. "Keep" is the other.

### "It feels like it does two things"

Yes. "Triage" is really two sequential decisions:
1. **Should we keep this signal?** (keep or drop)
2. **If we keep it, should we attach the user's identity?** (attribute or anonymize)

The current code collapses that into one enum with three values. But the domain is two questions. Decomposing the concept correctly matters more than choosing better words for a muddled concept.

## Can a Rule Encode This?

Not deterministically. A linter can catch symptoms — mechanism words in high-level code, high complexity, forbidden imports. It cannot judge whether a name accurately reflects the domain concept, whether a single enum hides two decisions, or whether the abstraction is drawn at the right seam.

| Deterministic (lintable)                    | Human review (not lintable)                            |
| ------------------------------------------- | ------------------------------------------------------ |
| No low-level operations in orchestrators    | Does the name reveal the real domain concept?          |
| Cognitive complexity ≤ N                    | Is the concept itself correctly decomposed?            |
| No infrastructure imports in application    | Does the function tell a story a domain expert recognizes? |
| Max constructor dependencies                | Is one enum hiding two separate decisions?             |

The floor is lintable. The ceiling requires judgment.

## LLM-as-Judge: Measuring the Ceiling

Since the ceiling can't be pattern-matched, we tested whether an LLM could ask the right questions systematically.

### The Setup

**Agent A** sees only the function body. Name, class, types — all removed. It describes what the code does in one sentence.

**Agent B** sees only the bare function name. Nothing else. It describes what it expects.

**Judge** compares the two and scores alignment (0-100).

Strict isolation matters. An earlier iteration gave Agent B the full signature (class name, parameter types, return type). That leaked too much context — type names like `SignalTriageInput` let the agent infer domain details, inflating the score.

### Results: `classify` on `DefaultSignalTriageService`

**Agent A (saw body):**
> This code looks up a signal's domain in a vendor catalog and classifies it as an attribute with its matched category if found, or marks it for anonymization if the domain is not in the catalog.

**Agent B (saw name: "classify"):**
> I expect this function to assign an input item to one or more predefined categories or classes based on its characteristics or features.

**Judge:** Score 52. The name is too generic. The implementation is a specific vendor catalog lookup with two outcomes. Agent B expected multi-factor classification. The name over-promises.

### Alternative Names Scoreboard

| Name                              | Score |
| --------------------------------- | ----: |
| `classify` (current)              |    52 |
| `resolveIdentityPolicy`           |    20 |
| `classifySignalByVendorCatalog`   |    72 |
| `resolveSignalPrivacyDisposition` |    62 |
| `triageSignal`                    |    62 |

`resolveIdentityPolicy` scored worst (20) — we thought it was a good name earlier, but it implies IAM/auth policy resolution, which is nothing like a vendor catalog lookup.

`classifySignalByVendorCatalog` scored best (72) — it names both the mechanism and the action. Docked for not mentioning the anonymization fallback.

The judge kept converging on `classifySignalByVendorCatalog` across multiple runs, which suggests the implementation has a natural name.

## What We Learned

**The right abstraction level is between "too low" and "too high."** Too low forces the reader to decode mechanics. Too high forces the reader to guess what the abstractions mean. The sweet spot is where every line names a real domain step and the reader can tell the story without opening children.

**Over-compression is as bad as under-abstraction.** Three lines of vague containers is not better than twenty lines of readable domain steps. Good abstraction reveals meaning; bad abstraction hides it behind words that sound clean but say nothing.

**Intention-revealing names only work when the intentions are defined.** The function name points at a concept. If the concept doesn't exist in the ubiquitous language, no renaming makes the code self-documenting. Define the concept first, then the name writes itself.

**Names can't encode decision spaces.** For decision outcomes, the branching must be visible at the level where it matters, or the decision space must be documented in the glossary.

**Decompose the concept before naming it.** If a single concept hides two separate questions (keep/drop and attribute/anonymize), no name will be clear. Get the concept right first, then the name almost writes itself.

**LLM-as-judge can measure name quality.** It caught that `classify` over-promises, that `resolveIdentityPolicy` points at the wrong domain, and that `classifySignalByVendorCatalog` most accurately describes what the code does. Use it as an advisory CI signal, not a gate — the ceiling still belongs to human judgment.

## Related

- [[Levels of Abstraction]] — the core principle: naming mechanics buys back reader attention
- [[Abstraction Level Best Practices]] — measurement framework, review checklist, enforcement model
- [[Composed Method]] — Beck's pattern: one identifiable task per method, same abstraction level
- [[Domain-Driven Design]] — ubiquitous language as the source of intention-revealing names
- [[How long before we stop reading the code?]] — the article that prompted this investigation
