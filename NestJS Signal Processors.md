---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
# Case Study: NestJS Signal Processors

**Date:** 2026-06-01  
**Context:** Eliminating code duplication across 6 BullMQ processors in a NestJS monorepo  
**Problem:** 6 processor classes, ~168 lines each = ~1,000 lines of identical boilerplate  
**Resolution:** Abstract class + thin subclasses (pragmatic), not composition (ideal)

---

## Problem Statement

Six signal processors (`BrowserSessionSignalProcessor`, `BrowserOauthFlowSignalProcessor`, etc.) had identical implementations:

- Job processing with async context (CLS) setup
- Retry logic with max-attempts tracking
- Dead-letter queue (DLQ) routing when retries exhausted
- Structured logging (failed, completed, routed to DLQ, error handling)
- Error handling + re-throw for BullMQ retry mechanism

Each processor was a nearly identical 168-line class, differing only in:
- Signal type (e.g., `BROWSER_SESSION`, `BROWSER_OAUTH_FLOW`)
- Handler service (e.g., `BrowserSessionSignalHandlerService`)
- Event prefix for logging (e.g., `signal.handler.browser_session`)

**Goal:** Consolidate the logic without sacrificing clarity or violating NestJS idioms.

---

## Exploration

### Option 1: Factory-Generated Classes

**Idea:** One `SignalProcessor` class instantiated 6 times via a factory function that applies `@Processor()` decorator dynamically.

```typescript
function createProcessor(signalType: SignalType, eventPrefix: string) {
  @Processor(getQueueName(signalType))
  @Injectable()
  class _Processor extends SignalProcessor {
    constructor(cls, registry) {
      super(signalType, eventPrefix, cls, handler, registry);
    }
  }
  return _Processor;
}

@Module({
  providers: [
    createProcessor(SignalType.BROWSER_SESSION, 'signal.handler.browser_session'),
    createProcessor(SignalType.BROWSER_OAUTH_FLOW, 'signal.handler.browser_oauth_flow'),
    // ... 4 more
  ],
})
```

**Advantages:**
- True composition (one class, multiple instances)
- Single source of truth for logic
- 978 fewer lines of boilerplate
- Easy to add new processors (one provider call)

**Disadvantages:**
- IDE support breaks (no code completion inside functions)
- Stack traces show `_Processor` instead of class name
- Unconventional in NestJS (community expects explicit class definitions)
- Harder to debug (can't set breakpoints on dynamically created classes)
- Surprises future maintainers ("Why is the class in a function?")

**Verdict:** Theoretically superior, pragmatically problematic for a typical NestJS team.

---

### Option 2: Decorator Factory

**Idea:** Custom `@Processor()` decorator factory reduces subclass boilerplate slightly.

```typescript
function Processor(signalType: SignalType, eventPrefix: string) {
  return (constructor: any) => {
    Injectable()(constructor);
    BullMQProcessor(getQueueName(signalType))(constructor);
    return constructor;
  };
}

@Processor(SignalType.BROWSER_SESSION, 'signal.handler.browser_session')
export class BrowserSessionSignalProcessor extends AbstractSignalProcessor {
  constructor(cls, handler, registry) {
    super(SignalType.BROWSER_SESSION, 'signal.handler.browser_session', cls, handler, registry);
  }
}
```

**Advantages:**
- Still idiomatic NestJS
- Reduces decorator boilerplate (no explicit `@Injectable()` + `@Processor()`)

**Disadvantages:**
- Still requires 6 class definitions
- Still 6 files
- Minimal reduction in boilerplate

**Verdict:** Incremental improvement, not a significant win.

---

### Option 3: Custom Processor Registry

**Idea:** Skip NestJS decorators entirely. Manually register processors in a custom registry.

```typescript
@Injectable()
export class SignalProcessorRegistry {
  private processors = new Map<SignalType, SignalProcessor>();

  register(signalType: SignalType, processor: SignalProcessor) {
    this.processors.set(signalType, processor);
  }

  async process(signalType: SignalType, job: Job) {
    return this.processors.get(signalType)?.process(job);
  }
}

@Module({
  providers: [
    {
      provide: SignalProcessorRegistry,
      useFactory: (cls, handlers, registry) => {
        const registry = new SignalProcessorRegistry();
        registry.register(SignalType.BROWSER_SESSION, 
          new SignalProcessor(SignalType.BROWSER_SESSION, 'signal.handler.browser_session', cls, handlers.session, registry));
        // ... 5 more registrations
        return registry;
      },
    },
  ],
})
```

**Advantages:**
- Pure composition (one class, 6 instances)
- Single class definition
- IDE support works

**Disadvantages:**
- Loses NestJS's `@Processor()` automagic discovery
- Manual BullMQ queue wiring required
- Not idiomatic (NestJS teams expect decorator-based processors)
- Higher coupling (registry must know all signal types)

**Verdict:** Valid, but trades NestJS idioms for composition purity.

---

### Option 4: Abstract Class + Thin Subclasses (Chosen)

**Idea:** Extract common logic into `AbstractSignalProcessor`. Concrete subclasses extend it, applying `@Processor()` decorator and passing config via constructor.

```typescript
export abstract class AbstractSignalProcessor extends WorkerHost implements OnModuleInit {
  constructor(
    private signalType: SignalType,
    private eventPrefix: string,
    private cls: ClsService,
    private handler: ISignalHandler,
    private signalQueueRegistry: SignalQueueRegistry,
  ) {
    super();
  }

  async process(job: Job<SignalDispatchJobData>): Promise<void> {
    return this.cls.run(async () => {
      initializeJobContext(this.cls, job);
      try {
        await this.handler.handle(job.data);
      } catch (error) {
        this.logFailure(job, error);
        throw error;
      }
    });
  }

  onModuleInit(): void {
    this.worker.on('failed', (job, error) => { ... });
    this.worker.on('completed', (job) => { ... });
  }

  // ... DLQ routing, logging (163 lines total)
}

@Processor(getSignalQueueName(SignalType.BROWSER_SESSION))
@Injectable()
export class BrowserSessionSignalProcessor extends AbstractSignalProcessor {
  constructor(
    cls: ClsService,
    handler: BrowserSessionSignalHandlerService,
    signalQueueRegistry: SignalQueueRegistry,
  ) {
    super(SignalType.BROWSER_SESSION, 'signal.handler.browser_session', cls, handler, signalQueueRegistry);
  }
}

// 5 more identical subclasses...
```

**Advantages:**
- Idiomatic NestJS (decorator-based discovery)
- Full IDE support (go-to-definition, refactoring, completion)
- Clear stack traces
- Easy to test (can import `BrowserSessionSignalProcessor` directly)
- Consolidates 1,000+ lines into 163 lines (abstract) + ~20 lines × 6 (subclasses)
- Minimal boilerplate per processor (just decorator + super call)

**Disadvantages:**
- Inheritance (philosophically less pure than composition)
- 6 thin subclasses (boilerplate, but minimal)
- Violates OCP spirit (inheritance for code reuse, not polymorphism)

**Verdict:** Pragmatic choice given NestJS constraints. Best trade-off for team maintainability.

---

## Trade-offs Analysis

| Dimension | Factory | Decorator | Registry | Abstract |
|-----------|---------|-----------|----------|----------|
| **Composition** | ✅ Yes | ❌ No | ✅ Yes | ❌ No |
| **IDE Support** | ❌ Broken | ✅ Good | ✅ Excellent | ✅ Excellent |
| **Idiomatic NestJS** | ❌ No | ✅ Yes | ❌ No | ✅ Yes |
| **Lines Saved** | 978 | ~50 | 978 | 837 |
| **Testability** | ⚠️ Hard | ✅ Easy | ✅ Easy | ✅ Easy |
| **Team Convention** | ❌ Surprises | ✅ Familiar | ⚠️ Different | ✅ Familiar |
| **Future-Proof** | ❌ Fragile | ✅ Stable | ⚠️ Coupled | ✅ Stable |

**Key insight:** Factory and Registry give composition but sacrifice developer experience. Abstract class gives good DX + pragmatic consolidation at the cost of inheritance (which is acceptable when all subclasses are identical).

---

## OCP Violations & How to Fix

**Current design violates OCP spirit:**
- All processors have identical behavior (retry, DLQ, logging)
- Inheritance suggests polymorphism; there is none
- If a processor needs custom retry logic, you override `isRetryExhausted()` → duplicate logic

**Fix: Strategy Injection**

Extract behavioral variance into pluggable strategies:

```typescript
interface RetryStrategy {
  isExhausted(job: Job): boolean;
  handleExhausted(job: Job, error: Error): Promise<void>;
}

interface LoggingStrategy {
  logFailure(job: Job, error: Error): void;
  logCompleted(job: Job): void;
  // ...
}

export class SignalProcessor extends WorkerHost {
  constructor(
    private retryStrategy: RetryStrategy,
    private loggingStrategy: LoggingStrategy,
    private handler: ISignalHandler,
  ) { }

  async process(job: Job) {
    try {
      await this.handler.handle(job.data);
      this.loggingStrategy.logCompleted(job);
    } catch (error) {
      this.loggingStrategy.logFailure(job, error);
      if (this.retryStrategy.isExhausted(job)) {
        await this.retryStrategy.handleExhausted(job, error);
      }
      throw error;
    }
  }
}
```

Now:
- `SignalProcessor` is closed for modification (retry/logging logic externalized)
- New behaviors are extensions (new strategy implementations)
- ✅ OCP-compliant

**Trade-off:** Currently unnecessary (all processors are identical). Implement only when behavioral variance emerges.

---

## Final Decision & Why Document It

**Chosen:** Abstract class + thin subclasses  
**Reason:** NestJS `@Processor()` decorator constraint

### The Constraint

NestJS reads decorators at **bootstrap time** (class definition), not runtime. You cannot:

```typescript
// ❌ Doesn't work — decorator runs at parse time
@Processor(getQueueName(signalType))  // ← signalType is undefined
class MyProcessor { }

// ❌ Doesn't work — decorator can't read constructor params
@Processor(this.config.getQueueName())  // ← Too late, decorator already applied
class MyProcessor { }
```

**Result:** Each queue requires its own class definition with its own decorator. You cannot parameterize `@Processor()`.

### Why Document This

Future maintainers might ask: "Why inheritance? Why not a single generic class?"

The answer is the decorator constraint. Without documenting it, they'll waste time re-exploring the factory approach.

**Documentation in code:**

```typescript
/**
 * AbstractSignalProcessor consolidates boilerplate retry/DLQ/logging logic.
 * 
 * Why inheritance instead of one generic SignalProcessor class?
 * 
 * NestJS's @Processor(queueName) decorator is read at bootstrap time and
 * cannot be parameterized at runtime. Each queue MUST have its own
 * decorated class definition.
 * 
 * We explored alternatives:
 * - Factory-generated classes: breaks IDE support, unconventional
 * - Custom registry: loses NestJS automagic, higher coupling
 * - Decorator factory: minimal boilerplate reduction, still 6 classes
 * 
 * Inheritance (while not ideal for 100% identical subclasses) is the
 * pragmatic choice given the constraint and team conventions.
 * 
 * If behavioral variance emerges (different retry strategies, logging),
 * refactor to strategy injection rather than overriding methods.
 */
export abstract class AbstractSignalProcessor extends WorkerHost { ... }
```

---

## Lessons

1. **Constraints shape design.** Decorators forced inheritance despite composition being theoretically better.
2. **Pragmatism > Purity.** Breaking IDE support to save 100 lines is a bad trade for a team.
3. **Document trade-offs.** Prevent future refactoring churn by explaining why you chose inheritance.
4. **Defer OCP compliance.** Strategy injection is unnecessary until behavioral variance emerges. Don't over-engineer for flexibility you don't need.
5. **Know when to break rules.** Inheritance for code reuse (not polymorphism) violates OCP spirit but is acceptable in constrained contexts.

---

## References

- See [[Composition vs Inheritance]] for design philosophy
- See [[Abstract Classes]] for when inheritance is appropriate
- See [[Open-Closed Principle]] for OCP violations and fixes
- See [[Strategy Pattern]] for behavioral variance
- See [[Documenting Constraints]] for why constraint documentation matters
