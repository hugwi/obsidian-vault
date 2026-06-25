---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
# Documenting Constraints

**Summary:** Architectural decisions are often constrained by external systems (frameworks, libraries, infrastructure). Document the constraint in the code. Without it, future developers will waste time re-exploring the same alternatives.

---

## Why Document Constraints

When you choose architecture A over B, it's because:
1. **No constraint** — A is objectively better (faster, simpler, more testable)
2. **Framework constraint** — B would work better, but the framework forbids it
3. **Team convention** — A aligns with how the team works
4. **Legacy debt** — A is dictated by existing systems

**Case 2 and 3 are invisible in the code.** Future maintainers will see A and think: "Why not use B?" Then they'll spend weeks re-exploring the same decision, implementing B, hitting the same constraint, and reverting.

---

## The Cost of Undocumented Constraints

**Scenario:** You inherit a codebase using inheritance instead of composition for code reuse.

### Without Constraint Documentation

```typescript
// Vague comment — doesn't explain WHY
abstract class JobProcessor {
  async process(job: Job) { ... }
}

class SignalProcessor extends JobProcessor { ... }
```

**Developer's thoughts:** "This should be composition. Inheritance for code reuse violates OCP. Let me refactor it..."

After 3 days of work:
- Tries factory-generated classes → realizes IDE breaks
- Tries custom registry → realizes BullMQ expects decorated classes
- Reverts changes, confused about why the original author chose inheritance

**Result:** Wasted 3 days, PR rejected, team frustrated

### With Constraint Documentation

```typescript
/**
 * AbstractJobProcessor consolidates retry/DLQ/logging logic.
 * 
 * Why inheritance instead of composition?
 * 
 * BullMQ requires queue names in @Processor() decorators, applied
 * at bootstrap time. TypeScript doesn't support runtime decorator
 * parameterization. Each queue MUST have its own class definition.
 * 
 * Explored alternatives:
 * - Factory-generated classes: breaks IDE support (go-to-definition, completion)
 * - Custom registry: loses BullMQ automagic queue discovery
 * - Decorator factory: minimal savings, still 6 classes
 * 
 * Inheritance is pragmatic given the framework constraint.
 */
export abstract class AbstractJobProcessor { ... }
```

**Developer's thoughts:** "Ah, the decorator constraint. Makes sense. I won't re-explore this."

**Result:** 2 minutes to understand, zero wasted effort

---

## Real-World Case Study

![[NestJS Signal Processors#Final Decision & Why Document It]]

### The Constraint

NestJS reads decorators at **bootstrap time**. This means:

```typescript
// ❌ Doesn't work — decorator can't read a runtime value
@Processor(getQueueName(signalType))  // signalType is not defined yet
class MyProcessor { }

// ❌ Doesn't work — decorator is applied before constructor runs
@Processor(this.config.getQueueName())  // `this` doesn't exist at decorator time
class MyProcessor { }
```

**Result:** You cannot parameterize `@Processor()` at runtime. Each queue requires its own class definition.

### Impact on Design

This single constraint eliminates all composition-based approaches:
- ❌ Factory-generated classes (can't apply decorators dynamically)
- ❌ Parameterized base class (can't parameterize `@Processor()`)
- ✅ Inheritance with thin subclasses (each subclass has its own `@Processor()` decorator)

---

## What to Document

### Framework/Library Constraints

```typescript
/**
 * Why we use [choice A] instead of [choice B]:
 * 
 * [Library/Framework] [version] [constraint].
 * 
 * We evaluated [B], but [specific reason it fails].
 * 
 * Explored [alternative C]:
 * - Pro: [benefit]
 * - Con: [drawback that eliminates it]
 */
```

**Example:**

```typescript
/**
 * TypeScript interfaces are erased at runtime. To serve as a DI token
 * in NestJS, we use an abstract class instead, even though the actual
 * use case (consolidating identical code) would normally call for composition.
 */
export abstract class IEmailValidator {
  abstract validate(email: string): boolean;
}
```

### Team Convention Decisions

```typescript
/**
 * Why we use [choice A] instead of [choice B]:
 * 
 * Team convention: [reason].
 * 
 * We prefer [choice A] because:
 * - [reason 1]
 * - [reason 2]
 */
```

**Example:**

```typescript
/**
 * NestJS team convention: use decorators + DI over custom registries.
 * Keeps code idiomatic and lets new team members recognize patterns instantly.
 */
@Processor(getQueueName(signalType))
export class SignalProcessor { ... }
```

### Legacy Debt

```typescript
/**
 * This implementation deviates from [standard pattern] because
 * [legacy system / external API / existing contract] requires it.
 * 
 * Refactoring blocked by [blocker]. When [condition] changes, revisit.
 */
```

**Example:**

```typescript
/**
 * We accept string union types instead of enums because the API
 * returns raw strings and TypeScript enums would require casting.
 * 
 * Refactoring blocked by: API changes need coordination with backend team.
 * Revisit when API enum support ships.
 */
type UserRole = 'admin' | 'member' | 'viewer';
```

---

## Documentation Placement

### In Code (for future maintainers)

- **Class/interface JSDoc** — explain the architectural choice and constraint
- **File-level comment** — if the decision affects the entire file
- **ADR (Architecture Decision Record)** — if it affects the entire module

### In Git (for code review)

- **Commit message body** — explain alternatives and why you chose A
- **PR description** — surface the constraint to reviewers

### In Team Docs

- **Architecture guide** — document framework constraints once, reference in code
- **Decision log** — keep a searchable record (see [[Architecture Decision Records]])

---

## When Not to Document

You don't need extensive constraint documentation when:
- The choice is objectively better (faster, simpler, more testable)
- It's a common pattern that the team already knows
- It's trivial (e.g., naming conventions)

**Rule of thumb:** If you had to think about or research the decision, future maintainers will too. Document it.

---

## Benefits

| Benefit | Impact |
|---------|--------|
| **Prevents re-exploration** | Saves 3+ days per developer per decision |
| **Enables confident refactoring** | When constraints change, refactoring is safe and intentional |
| **Onboarding new team members** | New developers understand why without asking |
| **Code review clarity** | Reviewers understand the tradeoff upfront |
| **Reduces technical debt perception** | Code that looks "wrong" is understood as constrained, not ignorant |

---

## References

- See [[Architecture Decision Records]] — how to document decisions systematically
- See [[Design Patterns/Composition vs Inheritance]] — example of constrained choice
- See [[Design Patterns/Abstract Classes]] — when inheritance is pragmatic despite ideals
