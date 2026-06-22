# Open-Closed Principle (OCP)

**Statement:** Software entities (classes, modules, functions) should be **open for extension** but **closed for modification**.

**In plain language:** Add new behavior without changing existing code.

---

## The Problem It Solves

```typescript
// ❌ Violates OCP: Adding retry logic requires modifying the processor
class JobProcessor {
  async process(job: Job) {
    try {
      await job.execute();
    } catch (error) {
      // Hard-coded logic — to customize, you must override or modify
      if (job.attempts < 3) {
        throw error; // Retry
      } else {
        // Send to DLQ
      }
    }
  }
}

// To use a different retry threshold, you must override or rewrite
class ConservativeJobProcessor extends JobProcessor {
  // Need to override process() or handleFailure() — modifying the parent's logic
}
```

**Problem:** Every new retry strategy requires modifying the processor class or creating a subclass with duplicated logic.

---

## The Solution

Extract behavioral variance into strategies, injected at construction:

```typescript
// ✅ Respects OCP: New retry strategies don't modify the processor
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

// New retry strategies are **extensions**, not modifications
class ConservativeRetryStrategy implements RetryStrategy {
  isExhausted(job: Job): boolean {
    return job.attempts > 3;
  }
  async handleExhausted(job: Job, error: Error): Promise<void> {
    // ...
  }
}

class StandardRetryStrategy implements RetryStrategy {
  isExhausted(job: Job): boolean {
    return job.attempts > 5;
  }
  async handleExhausted(job: Job, error: Error): Promise<void> {
    // ...
  }
}
```

---

## Real-World Case Study

The signal processors initially violated OCP:

![[NestJS Signal Processors#OCP Violations & How to Fix]]

All 6 processors had identical retry, DLQ, and logging logic. To add a new retry strategy, you'd need to:
1. Modify the abstract processor class, OR
2. Override a method in a concrete subclass (duplicating logic across multiple subclasses)

**The fix:** Extract retry logic and logging into injected strategies. New behaviors become new strategy classes, not modifications to the processor.

---

## Why OCP Matters

| Scenario | Without OCP | With OCP |
|----------|------------|---------|
| **Add new retry strategy** | Modify processor + override in subclasses | Create new strategy class |
| **Change logging behavior** | Modify processor | Inject different logger |
| **Support A/B testing** | Hard-code feature flags | Inject different strategy per user |
| **Testing** | Mock or override processor | Inject test strategy |
| **Code reuse** | Copy-paste and modify | Reuse processor, swap strategies |

---

## Balancing OCP with Practicality

OCP is an **ideal**, not a law.

### ❌ Over-Application

Don't create strategies for behavior that never varies:

```typescript
// Over-engineered: "LoggingStrategy" for behavior that never changes
interface LoggingStrategy {
  log(message: string): void;
}

class ConsoleLogStrategy implements LoggingStrategy {
  log(message: string) { console.log(message); }
}

class JobProcessor {
  constructor(private loggingStrategy: LoggingStrategy) {}
  
  async process(job: Job) {
    this.loggingStrategy.log('Job started');
  }
}
```

**Better:** Just use a logger service directly. Wait for behavioral variance before extracting a strategy.

### ✅ Pragmatic Application

Extract strategies when you see the **second variant**:

```typescript
// First variant: just retry logic (no strategy yet)
class JobProcessor {
  async process(job: Job) {
    try {
      await job.execute();
    } catch (error) {
      if (job.attempts < MAX_ATTEMPTS) throw error;
      await this.routeToDlq(job, error);
    }
  }
}

// Second variant: need different retry logic → now extract a strategy
interface RetryStrategy {
  isExhausted(job: Job): boolean;
}

class JobProcessor {
  constructor(private retryStrategy: RetryStrategy) {}
  // ...
}
```

---

## Common OCP Violations

| Pattern | Why it Violates OCP | Fix |
|---------|-------------------|-----|
| **switch/case on type** | Adding a type requires modifying the switch | Polymorphism or strategy |
| **if/else for features** | Adding a feature requires new conditionals | Feature flags or strategies |
| **Inheritance for reuse** | Customizing behavior requires overriding | Composition (delegate behavior) |
| **Hard-coded config** | Changing behavior requires modifying code | Inject config or strategies |

---

## References

- See [[Strategy Pattern]] — the primary technique for achieving OCP
- See [[Composition vs Inheritance]] — why composition enables OCP
- See [[Dependency Inversion Principle]] — OCP requires inverting dependencies
