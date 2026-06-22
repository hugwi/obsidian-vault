# Software Best Practices

This vault contains case studies, design patterns, SOLID principles, and architectural decision documentation.

## Structure

### Case Studies
Real-world examples showing iteration, constraint analysis, and pragmatic decisions.

- **Case Studies/NestJS Signal Processors** — The full story of how 6 identical processors were consolidated while respecting framework constraints, exploring alternatives, and documenting the decision for future maintainers.

### Design Patterns
Foundational patterns for code reuse, behavior variation, and maintainability.

- **Design Patterns/Composition vs Inheritance** — When to use composition (preferred) and when inheritance is pragmatic despite framework constraints
- **Design Patterns/Abstract Classes** — Using inheritance for contracts and DI when frameworks force separate class definitions
- **Design Patterns/Strategy Pattern** — Extracting behavioral variance into pluggable strategies to respect OCP

### SOLID Principles
Principles for writing maintainable, extensible code.

- **SOLID Principles/Open-Closed Principle** — Why software should be open for extension, closed for modification, and how to achieve it

### Architecture Decisions
Patterns and practices for documenting architectural choices.

- **Architecture Decisions/Documenting Constraints** — Why future developers waste time re-exploring constrained decisions, and how to prevent it

### CI/CD
Continuous-integration gating, triggers, and how breaks slip through.

- **CI-CD/Gating Shared-Contract Changes** — Why a consumer's CI must trigger on its upstream package dependencies, not just its own directory, and how to close both the unchecked-consumer and the wrong-tree gaps. Backed by the case study below.

### Tests
Testing strategy and practices.

- **tests/e2e/Hermetic E2E and Faking Inaccessible Third-Party Sites** — What hermetic E2E is, and the layered strategy (URL-spoof interception, recorded fixtures, contract pinning, real-traffic canary, prod monitoring) for testing a feature that depends on a third-party site you can't drive in CI

---

## How to Navigate

All design pattern files embed relevant sections from case studies using Obsidian transclusion. This means:
- When a case study changes, all referenced files automatically reflect the changes
- Each design pattern file stands alone (readable without the case study) but links to real-world examples
- Case studies are the source of truth for "what happened and why"

**Example:** Read "Composition vs Inheritance" to understand the theory, then see `![[NestJS Signal Processors#Exploration]]` to see the real comparison between factory, decorator, registry, and inheritance approaches.

---

## Quick Reference

| Question | File |
|----------|------|
| "Should I use inheritance or composition?" | [[Composition vs Inheritance]] |
| "When is inheritance appropriate?" | [[Abstract Classes]] |
| "How do I respect OCP?" | [[Strategy Pattern]], [[Open-Closed Principle]] |
| "Should I document my architectural decision?" | [[Documenting Constraints]] |
| "Walk me through a real decision process" | [[NestJS Signal Processors]] (case study) |
| "How do I E2E-test against a site I can't access?" | [[Hermetic E2E and Faking Inaccessible Third-Party Sites]] |
| "Why did a green PR break main?" | [[Gating Shared-Contract Changes]], [[Path-Filtered CI — The Shared-Contract Blind Spot]] |
| "What should a path-filtered workflow trigger on?" | [[Gating Shared-Contract Changes]] |

---

## Principles

1. **Pragmatism over purity** — Theory matters, but framework constraints and team conventions matter more
2. **Document constraints** — Future developers will waste time re-exploring undocumented decisions
3. **Defer over-engineering** — Don't implement Strategy pattern for behavior that never varies (yet)
4. **Composition is preferred** — Inheritance is a tool for specific constraints, not a default
5. **Idiomatic > novel** — A boring design that the team recognizes is better than a clever one that surprises

