---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
# Composition vs Inheritance

**Summary:** Composition (object delegation) is theoretically superior for code reuse, but inheritance is pragmatically necessary when frameworks enforce constraints that forbid parameterization at runtime.

---

## Core Philosophy

**Composition** — "has-a" relationship. Object A contains objects B and C; delegates behavior to them.
- Pro: Flexible, testable, respects OCP (open for extension, closed for modification)
- Con: More indirection, more objects in memory

**Inheritance** — "is-a" relationship. Class B extends Class A; inherits behavior and can override.
- Pro: Simple, direct, requires fewer abstractions
- Con: Tightly coupled, violates substitutability principle if subclasses aren't true polymorphic types

---

## When Composition Wins

Use composition when:
- Multiple behaviors can be mixed (strategy pattern, chain of responsibility)
- Behavior is optional or swappable at runtime
- You want to respect OCP and SOLID principles
- The framework doesn't impose decorator-time constraints

---

## When Inheritance is Pragmatic

Use inheritance when:
- Framework reads decorators at **bootstrap time**, not runtime
- All subclasses are identical (no polymorphism intended)
- Composition would break IDE support or developer experience
- The constraint is architectural (the framework doesn't allow parameterization)

---

## Real-World Case Study

![[NestJS Signal Processors#Exploration]]

### Key Insight

The NestJS `@Processor(queueName)` decorator is read at bootstrap time and cannot be parameterized at runtime. This single constraint invalidates composition factories:

- ❌ **Factory approach** (theoretically superior) — breaks IDE support, unconventional, harder to debug
- ✅ **Inheritance approach** (pragmatically superior) — idiomatic NestJS, full IDE support, easy to test

![[NestJS Signal Processors#Final Decision & Why Document It]]

---

## Trade-offs Summary

| Scenario | Composition | Inheritance |
|----------|-------------|-------------|
| Behavioral variance exists | ✅ YES | ❌ NO (violates OCP) |
| Framework allows runtime parameterization | ✅ YES | ❌ Unnecessary |
| Framework enforces bootstrap-time decorators | ❌ NO (can't parameterize) | ✅ YES (required) |
| All subclasses are identical | ❌ Over-engineered | ✅ Pragmatic |
| IDE support matters | ❌ Broken (factory) | ✅ Excellent |

---

## References

- See [[Abstract Classes]] — when inheritance is appropriate for contracts
- See [[Strategy Pattern]] — how to achieve behavioral variance without inheritance
- See [[Open-Closed Principle]] — why composition is theoretically superior
