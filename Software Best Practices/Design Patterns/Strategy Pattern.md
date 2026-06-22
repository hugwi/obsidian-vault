# Strategy Pattern

**Summary:** Extract behavioral variance into pluggable strategy objects. Enables OCP compliance: new behaviors are extensions (new strategy classes), not modifications to existing code.

---

## Core Concept

**Strategy** — an object that encapsulates a specific algorithm or behavior. The context (main class) delegates to the strategy rather than implementing the behavior itself.

```typescript
interface RetryStrategy {
  isExhausted(job: Job): boolean;
  handleExhausted(job: Job, error: Error): Promise<void>;
}

class JobProcessor {
  constructor(private retryStrategy: RetryStrategy) {}
  
  async process(job: Job) {
    try {
      await job.execute();
    } catch (error) {
      if (this.retryStrategy.isExhausted(job)) {
        await this.retryStrategy.handleExhausted(job, error);
      }
      throw error;
    }
  }
}
```

---

## When to Use

Use strategies when:
- **Behavior varies by configuration** — different algorithms for the same problem
- **Behavior changes at runtime** — swap strategies based on user input, environment, A/B tests
- **You want to respect OCP** — new behaviors = new strategy classes, not modifications
- **You want testability** — inject mock strategies, no need to subclass or mock the entire processor

---

## Anti-Pattern: Inheritance When Strategy Applies

![[NestJS Signal Processors#OCP Violations & How to Fix]]

### The Problem

```typescript
// ❌ Violates OCP: modify abstract class to add new retry behavior
abstract class JobProcessor {
  async process(job: Job) {
    // ... shared logic ...
    if (this.isRetryExhausted(job)) {
      // Hard-coded retry logic
    }
  }
  
  // Subclasses override this to customize retry logic
  protected abstract isRetryExhausted(job: Job): boolean;
}

class ConservativeJobProcessor extends JobProcessor {
  protected isRetryExhausted(job: Job): boolean {
    return job.attempts > 3; // Different strategy, but code is scattered
  }
}
```

### The Fix

```typescript
// ✅ Respects OCP: new retry behaviors are new strategy classes
interface RetryStrategy {
  isExhausted(job: Job): boolean;
}

class ConservativeRetryStrategy implements RetryStrategy {
  isExhausted(job: Job): boolean {
    return job.attempts > 3;
  }
}

class StandardRetryStrategy implements RetryStrategy {
  isExhausted(job: Job): boolean {
    return job.attempts > 5;
  }
}

class JobProcessor {
  constructor(private retryStrategy: RetryStrategy) {}
  
  async process(job: Job) {
    // ... shared logic ...
    if (this.retryStrategy.isExhausted(job)) {
      // Uses injected strategy
    }
  }
}
```

---

## When to Defer Strategies

You don't need strategies when behavioral variance doesn't exist **yet**.

![[NestJS Signal Processors#OCP Violations & How to Fix#Trade-off: Currently unnecessary]]

**Guideline:** Implement strategies when you encounter the **second** variant of a behavior. The first one is implementation; the second one reveals the pattern.

---

## Common Strategies

| Pattern | Strategies |
|---------|-----------|
| **Retry logic** | exponential backoff, linear backoff, fixed delay, no retry |
| **Sorting** | by date, by name, by frequency, by relevance |
| **Caching** | in-memory, Redis, file-based, no cache |
| **Validation** | strict (all fields required), lenient (skip nulls), custom (by type) |
| **Logging** | console, file, Slack, structured (JSON), no logging |

---

## Related Patterns

- **Template Method** — define skeleton in abstract class, override specific steps
- **Decorator** — wrap an object to add behavior (similar goal, different structure)
- **Chain of Responsibility** — pass request through a chain of handlers
- **Command** — encapsulate a request as an object (more general than strategy)

---

## References

- See [[Composition vs Inheritance]] — why strategy injection is composition
- See [[Open-Closed Principle]] — the principle strategies enable
- See [[Abstract Classes]] — when inheritance is still appropriate (no variance yet)
