# Levels of Abstraction

> A reader's attention is a budget. Every line that forces them to *reconstruct intent from mechanics* spends some of it. Naming the mechanics buys it back.

## The Core Idea

Code operates at **levels of abstraction**. A low level says *how* (loops, indexes, mutations). A high level says *what* (the intent). Mixing levels in one function forces the reader to constantly shift gears — they read a `what`, then suddenly have to decode a `how`, hold the result in their head, and resume.

Raising a fragment to a named function lets the reader stay at one level. They read the name, trust it, and move on. The *how* is still there — just demoted one level down, available when (and only when) they choose to look.

## The Example

Same behavior, two levels. Both mark every envelope in a failed batch as "give up — don't retry."

### Low level — the reader must decode mechanics

```ts
} catch (err) {
  if (err instanceof IngestHttpError && isPermanentIngestFailure(err.status)) {
    reportPermanentIngestFailure({ status: err.status, requestId: err.requestId, envelopes: chunk });
    for (const envelope of envelopes) {
      permanentlyFailed.add(envelope.clientRecordId);
    }
    continue;
  }
  throw err;
}
```

To understand the loop, the reader runs a small interpreter in their head:

1. "There's a `for`. What am I iterating? `envelopes`."
2. "For each one I read `.clientRecordId`."
3. "I `.add` it to `permanentlyFailed` — that's a Set."
4. "So... after the loop, every envelope's id is in that Set."
5. "*Therefore* — this marks the whole batch as permanently failed."

Step 5 is the **intent**. Steps 1–4 are overhead the reader pays to *recover* it. The meaning was never written down — it had to be reconstructed.

### High level — the intent is the line

```ts
} catch (err) {
  if (err instanceof IngestHttpError && isPermanentIngestFailure(err.status)) {
    reportPermanentIngestFailure({ status: err.status, requestId: err.requestId, envelopes: chunk });
    markAllPermanentlyFailed(chunk, permanentlyFailed);
    continue;
  }
  throw err;
}
```

```ts
function markAllPermanentlyFailed(
  envelopes: readonly SignalEnvelope[],
  permanentlyFailed: Set<string>,
): void {
  for (const envelope of envelopes) {
    permanentlyFailed.add(envelope.clientRecordId);
  }
}
```

The reader of the `catch` block reads `markAllPermanentlyFailed(chunk, permanentlyFailed)` and is **done** — they reach step 5 directly, with no interpreter run. Steps 1–4 still exist, but they live *inside* the function, one level down. The reader visits them only if they actively doubt the name.

## Why This Adds a Level of Abstraction

```
                        BEFORE                         AFTER
                  (one level, mixed)           (two levels, separated)

  catch block:    what … what … HOW(loop)      what … what … what
                                  ▲                            │
                                  └─ reader drops a level      │ name keeps reader
                                     mid-sentence, decodes,    │ at the "what" level
                                     climbs back up            ▼
                                                       markAllPermanentlyFailed()
                                                               │
                                                               ▼ (only if doubted)
                                                          HOW(loop) — isolated
```

The loop didn't disappear; it got a **name and a home**. The name is a contract ("this marks all as permanently failed"); the body is the proof. The caller consumes the contract; the proof waits below, ignored until needed. That separation *is* the new level of abstraction.

## The Test: Does the Reader Have to Simulate?

A reliable smell — **if understanding a line means mentally executing it, it's at too low a level for where it sits.**

- `markAllPermanentlyFailed(chunk, set)` — read, trust, move on. No simulation.
- `for (const e of chunk) set.add(e.clientRecordId)` — simulate the loop to learn its purpose.

Mechanics that demand simulation belong below a name, not inline next to intent.

## When NOT to Extract

Levels of abstraction is a *flexible* principle, not a rule. Don't extract when:

- **The mechanic IS the intent at that level.** A one-line `arr.map(x => x.id)` reads as "the ids" — already a `what`. Wrapping it in `extractIds()` adds a hop without buying clarity.
- **It's used once and the name says no more than the body.** `function addOne(n) { return n + 1 }` hides nothing.
- **Extraction would scatter tightly-coupled steps.** If the loop mutates three locals the caller also touches, a function with five out-params is *worse* — the seam is fake. (See [[Composition vs Inheritance]] for the "fake seam" trap.)

The win is real only when the name carries **more meaning than the mechanics** — when it names a *concept* (permanent failure, give-up semantics) the loop merely *implements*.

## Heuristics

- **One function, one level.** If a function mixes "orchestrate the batch" with "increment an index," split the low part out.
- **Name the concept, not the code.** `markAllPermanentlyFailed`, not `loopAndAddIds`. The name should survive a reimplementation of the body.
- **Extract at the point of doubt.** If a teammate would pause to decode a fragment, that pause is the signal to name it.
- **Prefer explicit names at risky call sites.** `markAllPermanentlyFailed` over a generic `markAll(chunk, set)` where the give-up semantics matter — clarity beats reuse where mistakes are costly.

## Related

- [[Composition vs Inheritance]] — abstraction boundaries that hold vs. leak
- [[Strategy Pattern]] — naming a *behavior* so callers stay at the "what" level
- [[Abstract Classes]] — contracts (the "what") separated from implementations (the "how")
