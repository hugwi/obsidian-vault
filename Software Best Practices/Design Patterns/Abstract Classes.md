# Abstract Classes

**Summary:** Abstract classes define contracts (interfaces) that also serve as dependency injection tokens. Use them for shared infrastructure behavior when all subclasses are functionally identical.

---

## Purpose

Abstract classes in TypeScript/NestJS serve two roles:

1. **Contract** — declare the interface that subclasses must implement
2. **DI Token** — TypeScript interfaces are erased at runtime; abstract classes remain and can be injected

---

## When to Use Abstract Classes

### ✅ Appropriate Uses

- **Infrastructure contracts in DI systems** — where a single interface must be injected but multiple implementations exist
- **Shared utility behavior** — when all subclasses are identical except for configuration (decorators, constructor params)
- **Framework-imposed inheritance** — when the framework requires separate decorated classes (e.g., NestJS `@Processor()`)
- **Template method pattern** — define skeleton in abstract class, let subclasses fill in one or two specific steps

### ❌ Inappropriate Uses

- **Polymorphic behavior** — when subclasses have different implementations of the same method, use composition instead
- **Multiple unrelated capabilities** — if subclasses don't share all methods, you're trying to force unrelated types into a false hierarchy
- **Avoidable code reuse** — if you can avoid inheritance by extracting a helper service, do that instead

---

## Case Study: Signal Processors

![[NestJS Signal Processors#Option 4: Abstract Class + Thin Subclasses (Chosen)]]

### Why This Works

All 6 concrete processors:
- Inherit identical retry logic ✅
- Inherit identical DLQ routing ✅
- Inherit identical logging ✅
- Differ only in: signal type (config), handler service (DI param), event prefix (config)

**Inheritance is appropriate here because:**
1. Framework constraint forces separate `@Processor()`-decorated classes
2. All subclasses have zero behavioral variance
3. Each subclass is ~20 lines (just decorator + super call)
4. Abstract base consolidates 163 lines of infrastructure

---

## Constraint Documentation

![[NestJS Signal Processors#The Constraint]]

Future maintainers will ask: "Why inheritance instead of one generic class?"

**Document the constraint in the abstract class JSDoc:**

```typescript
/**
 * AbstractSignalProcessor consolidates boilerplate retry/DLQ/logging.
 * 
 * Why inheritance instead of composition?
 * 
 * NestJS's @Processor(queueName) decorator is read at bootstrap time
 * and cannot accept runtime parameters. Each queue needs its own
 * class definition with its own decorator.
 * 
 * We evaluated:
 * - Factory-generated classes: breaks IDE support
 * - Decorator factory: minimal savings, still 6 classes
 * - Custom registry: loses NestJS automagic discovery
 * 
 * Inheritance is pragmatic given the constraint.
 */
export abstract class AbstractSignalProcessor extends WorkerHost {
  // ...
}
```

---

## Anti-Pattern: Inheritance for Code Reuse When Composition Works

❌ **BAD:** Using inheritance to reuse behavior when composition is available

```typescript
// Violates OCP — can only override, can't swap
class BaseValidator {
  validateEmail(email: string): boolean { ... }
  validatePhone(phone: string): boolean { ... }
}

class StrictValidator extends BaseValidator {
  override validateEmail(email: string): boolean {
    // Custom logic, but can't use a different validator service
  }
}
```

✅ **BETTER:** Inject validators as dependencies

```typescript
class ValidationService {
  constructor(
    private emailValidator: EmailValidator,
    private phoneValidator: PhoneValidator,
  ) {}
  
  validate(data) {
    this.emailValidator.validate(data.email);
    this.phoneValidator.validate(data.phone);
  }
}
```

---

## Rule of Thumb

**Use abstract classes when:**
1. Framework constraint forces separate class definitions, OR
2. Template method pattern (only a few methods are meant to vary), AND
3. All subclasses are functionally identical except for configuration

**Use composition when:**
1. You have a choice, AND
2. Behavior varies or is optional

---

## References

- See [[Composition vs Inheritance]] — when composition is available, prefer it
- See [[Strategy Pattern]] — composition pattern for behavior variance
- See [[Template Method Pattern]] — when inheritance is part of the pattern itself
