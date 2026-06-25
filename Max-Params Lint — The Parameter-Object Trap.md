---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-16
tags: [case-study, refactoring, lint, max-params, srp, feature-envy, ethira]
project: ethira/api
related:
  - "[[Single Responsibility Principle]]"
  - "[[Feature Envy]]"
  - "[[Lint as a Smell Detector]]"
  - "[[Discriminated Unions]]"
---

# Case Study: `max-params` and the Parameter-Object Trap

> ESLint `max-params` fired on a signal-handler service method. The first refactor satisfied the rule by wrapping the arguments in a single object — lint went green, the design did not improve. This documents why a green lint can still be an invalid refactor, and how the same rule, read as a smell detector, pointed at the correct fix: split the responsibility, and the arguments fall away as a consequence.

## Context

`ClientVendorLinkerService.linkServerToClientVendor` lives in the browser-MCP-server-discovered signal handler chain (`api/src/modules/signals/application/services/signals/handlers/browser-mcp-server-discovered/`). It linked a discovered MCP server to a client vendor (creating the vendor if absent), then announced a newly-discovered third-party domain via `EventEmitter2`.

The method took four positional arguments:

```ts
async linkServerToClientVendor(
  workspaceId: string,
  mcpServerId: string,
  pageOrigin: string | undefined,
  observedAt: Date,
): Promise<void>
```

ESLint `max-params` flagged it: too many positional parameters.

## The signal `max-params` actually sends

`max-params` is a **proxy metric**. It does not care about commas. A high positional-argument count is a *symptom* — the usual root causes are:

- the function knows about too many independent things (low cohesion), or
- it owns more than one responsibility, each dragging in its own data, or
- one of the arguments is **Feature Envy** — passed in only to be forwarded somewhere else, never used by the function's core job.

The rule fires on the symptom. The fix has to address the cause, or the rule was right for nothing.

## Exploration

### Iteration 1 — The parameter-object (the invalid refactor)

The instinctive fix: collapse the four arguments into one params object.

```ts
interface LinkServerToClientVendorParams {
  workspaceId: string;
  mcpServerId: string;
  pageOrigin: string | undefined;
  observedAt: Date;
}

async linkServerToClientVendor(
  params: LinkServerToClientVendorParams,
): Promise<void> { ... }
```

`max-params` now counts **one** parameter. Lint is green. CI is happy.

**Why this is an invalid refactor:**

1. **Coupling is unchanged.** The method still *depends on* the same four facts. They moved from the parameter list into a property bag. The number the rule reported went down; the knowledge the rule was worried about did not.
2. **It hides the real smell instead of removing it.** `observedAt` is never used to *link* anything. The linker only forwards it into the domain-discovered event payload. That is textbook **Feature Envy** — the argument belongs to the announcement concern, not the linking concern. The parameter object made that envy *harder* to see, because now it is buried inside a struct that looks deliberate.
3. **It optimises the metric, not the design.** A reviewer skimming the diff sees "args reduced 4 → 1" and reads it as a design win. It is bookkeeping. The cohesion of the method is identical before and after.

> A parameter object is a legitimate tool **when the fields genuinely travel together as one concept** (a value object). It is a trap when it is used purely to silence an arity rule while the fields remain unrelated responsibilities.

### Iteration 2 — Ask why the count is high (the valid refactor)

Reframe the question from "how do I get under the limit?" to "*why* is this method holding four facts?"

Answer: the method has **two responsibilities** crammed together.

| Responsibility | Data it needs |
|---|---|
| Link server → client vendor (create vendor if absent) | `workspaceId`, `mcpServerId`, `pageOrigin` |
| Announce the newly-discovered domain | `workspaceId`, `domain`, `observedAt` |

`observedAt` exists in the signature **only** to serve the second responsibility. So does the `EventEmitter2` dependency injected into the service. Remove the second responsibility and both vanish.

## The correct rewrite

Give the linker a single responsibility — link, and *report the outcome*. Let the caller (the handler) own the announcement, since the handler already runs synchronously in the same unit of work and already has `observedAt` in scope.

### Linker — returns an outcome, emits nothing

```ts
export interface LinkServerToClientVendorParams {
  readonly workspaceId: string;
  readonly mcpServerId: string;
  readonly pageOrigin: string | undefined;
}

export type LinkResult =
  | { readonly linked: false }
  | {
      readonly linked: true;
      readonly vendorId: string;
      readonly domain: string;
      readonly wasCreated: boolean;
    };

async linkServerToClientVendor({
  workspaceId,
  mcpServerId,
  pageOrigin,
}: LinkServerToClientVendorParams): Promise<LinkResult> {
  const domain = resolveAiClientDomain(pageOrigin);
  if (domain === null) {
    return { linked: false };
  }
  const { vendorId, wasCreated } = await this.resolveOrCreateClientVendor(
    workspaceId,
    domain,
    mcpServerId,
  );
  return { linked: true, vendorId, domain, wasCreated };
}
```

- `observedAt` is **gone** — the linker never needed it.
- The `EventEmitter2` constructor dependency is **gone** — emitting was never the linker's job.
- The return type is a **discriminated union**. The "couldn't link" path is now explicit in the type, and the caller is *forced to narrow* before reading `domain`/`wasCreated`.

### Handler — owns the announcement

```ts
private async linkServerToClientVendor({
  workspaceId,
  mcpServerId,
  pageOrigin,
  observedAt,
}: LinkServerToClientVendorInput): Promise<void> {
  try {
    const result = await this.clientVendorLinker.linkServerToClientVendor({
      workspaceId,
      mcpServerId,
      pageOrigin,
    });
    if (result.linked && result.wasCreated) {
      this.emitDomainDiscovered(workspaceId, result.domain, observedAt);
    }
  } catch (error: unknown) {
    this.logger.error({
      event: 'signal.handler.browser_mcp_server_discovered.client_vendor_link_failed',
      workspaceId,
      mcpServerId,
      error: error instanceof Error ? error.message : String(error),
    });
  }
}

private emitDomainDiscovered(
  workspaceId: string,
  domain: string,
  discoveredAt: Date,
): void {
  const event: ThirdPartyDomainDiscoveredEvent = { workspaceId, domain, discoveredAt };
  try {
    this.eventEmitter.emit(THIRD_PARTY_DOMAIN_DISCOVERED_EVENT, event);
  } catch (error) {
    this.logger.warn({
      event: 'signal.handler.browser_mcp_server_discovered.domain_discovered_emit_failed',
      workspaceId,
      domain,
      error: error instanceof Error ? error.message : String(error),
    });
  }
}
```

`observedAt` lives where it is actually used — next to the emission it feeds. The Feature Envy is resolved by moving the *behaviour* to the data, not by repackaging the data.

## Why this still respects the side-effects boundary

The repo rule `server-side-effects.mdc` requires a server action's side-effects to stay server-side **in the same unit of work**. Moving the `emit` from the linker to the handler does **not** cross that boundary:

- the handler calls the linker **synchronously**, in-process,
- the `emit` happens in the same handler execution, before the handler returns,
- nothing is deferred to a queue and nothing is returned to a client to act on.

"Same unit of work" means the same synchronous handler execution — not literally the same method. Relocating the emit one frame up is still inside the unit of work. (Had the fix instead returned `LinkResult` to a controller for the *client* to emit, that would have violated the rule.)

## Comparison

| | Iteration 1 (param object) | Iteration 2 (responsibility split) |
|---|---|---|
| `max-params` satisfied? | Yes | Yes |
| Arguments the method *depends on* | 4 | 3 |
| `EventEmitter2` dependency | Still injected | Removed |
| Feature Envy (`observedAt`) | Hidden, not fixed | Removed |
| Responsibilities in the method | 2 | 1 |
| "Didn't link" path | Implicit (`void`) | Explicit (`{ linked: false }`) |
| Why the count dropped | Repackaging | Less knowledge |

Both pass lint. Only one is a refactor.

## Decision rules emerging

### Decision: how to respond to a threshold lint

```
threshold rule fires (max-params, complexity, max-lines, max-depth)
        │
        ▼
Ask: WHY is the number high?
        │
        ├─ fields form one real concept (value object)?
        │       → parameter object is legitimate. Wrap them.
        │
        ├─ one arg is only forwarded elsewhere (Feature Envy)?
        │       → move the behaviour to where the data is used.
        │         The arg disappears.
        │
        └─ method owns >1 responsibility?
                → split it. Each responsibility takes its own data.
                  The count falls out naturally.

Never: wrap-to-silence when the fields are unrelated.
       That games the metric and leaves the smell.
```

### Decision: the test for a valid "reduce arguments" refactor

> After the refactor, does the unit still *need to know* each removed fact?
>
> - If yes — you only moved the braces. Invalid.
> - If no — the responsibility that needed it left the building. Valid.

### Decision: a parameter object is not free

A params object is the right call when the bundle is a genuine value object whose fields always travel together. It is the wrong call when it is reached for *because* a lint rule is red and the fields are independent responsibilities. Same syntax, opposite intent.

## Lessons learned

1. **Green lint ≠ good refactor.** Threshold rules report symptoms. Silencing the symptom without diagnosing the cause is a no-op dressed as progress.
2. **Reducing argument *count* is not reducing *coupling*.** The honest metric is "how many facts does this unit still need to know," not "how many commas are in the signature."
3. **An argument that exists only to be passed through is a relocation signal.** Move the behaviour to the data (here: move the emit to the handler that owns `observedAt`), and the parameter evaporates.
4. **Splitting responsibility makes the metric satisfy itself.** We never targeted `max-params` in iteration 2 — we targeted SRP, and the arity dropped as a side effect. That is the shape of a real fix.
5. **Discriminated unions pay for the split.** Returning `LinkResult` instead of `void` relocates the emit *decision* to the responsibility owner and makes the no-op path unforgeable at the type level.

## Files of record

- `/Users/mindator/Ethira/monorepo/mcp-vendor-ingestion-link/api/src/modules/signals/application/services/signals/handlers/browser-mcp-server-discovered/client-vendor-linker.service.ts` — linker, single responsibility, returns `LinkResult`
- `/Users/mindator/Ethira/monorepo/mcp-vendor-ingestion-link/api/src/modules/signals/application/services/signals/handlers/browser-mcp-server-discovered/browser-mcp-server-discovered-signal-handler.service.ts` — handler, owns `emitDomainDiscovered`
- `.cursor/rules/server-side-effects.mdc` — the same-unit-of-work rule this refactor was checked against
- PR #2822 — `feat: auto-link discovered MCP server to client vendor`
