---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-05-27
tags: [refactoring, clean-code, legacy-code, ddd, hexagonal, kata, learning]
type: resource
status: reference
---

# Refactoring Examples — Bad to Good

Curated catalogue of open-source projects, katas, and production case studies that demonstrate **bad code refactored to good code using best practices**. Compiled from deep research across GitHub topics, refactoring book companions, conference talks, and engineering blogs.

> [!info] Decision tree
> - Want to **do** the refactor → Tier 1 + Tier 4 (katas + single-smell drills)
> - Want to **see** before/after fast → Tier 2 (parallel folders/branches)
> - Want **production-scale** lessons → Tier 6 (case studies)

---

## Tier 1 — Best Picks (Start Here)

| Repo | Why | Anti-pattern | Refactor target |
|------|-----|--------------|-----------------|
| [emilybache/GildedRose-Refactoring-Kata](https://github.com/emilybache/GildedRose-Refactoring-Kata) | Canonical entry kata. 60+ languages. 4.2k stars. | Nested conditionals, OCP violation | Characterization tests → Extract Method → Polymorphism |
| [emilybache/Theatrical-Players-Refactoring-Kata](https://github.com/emilybache/Theatrical-Players-Refactoring-Kata) | Fowler *Refactoring* 2nd ed Ch1 verbatim. Fowler-endorsed. | Calc + format tangled (SRP) | Extract Function, Split Phase, Polymorphism |
| [sandromancuso/trip-service-kata](https://github.com/sandromancuso/trip-service-kata) | Defining kata for static/singleton untestability. | Static `UserSession`/`TripDAO` calls | Extract & Override, Seam, DI |
| [jbrains/trivia](https://github.com/jbrains/trivia) | Legacy Code Retreat standard. Simulates real legacy. 40+ langs. | God-class procedural, no tests | Golden Master first, then carve seams |
| [emilybache/Racing-Car-Katas](https://github.com/emilybache/Racing-Car-Katas) | Direct SOLID-violation → testability mapping. 5 exercises. | Tight coupling, DIP violations | Extract Interface, Subclass-and-Override |

---

## Tier 2 — Before/After Side-by-Side (No Work Required)

- [CodelyTV/refactoring-code_smells-design_patterns](https://github.com/CodelyTV/refactoring-code_smells-design_patterns) — parallel smelly/clean subdirs. Full Fowler smell catalogue. PHP/JS/TS/Rust. 591★.
- [codurance/refactoring-bank-kata](https://github.com/codurance/refactoring-bank-kata) — `step_by_step_refactors/` folder ships each increment as separate file + tests. Python.
- [ArjanCodes/2021-code-smells](https://github.com/ArjanCodes/2021-code-smells) — `before.py` / `after.py` in root. 7 smells. Companion to YouTube series.
- [ZikaZaki/code-smells-python](https://github.com/ZikaZaki/code-smells-python) — `before_*/after_*` per smell folder.
- [christianhujer/expensereport](https://github.com/christianhujer/expensereport) — `trunk` vs `solutions` branch. 50+ langs. Level-2 variant adds HTML output mess.
- [emilybache/SupermarketReceipt-Refactoring-Kata](https://github.com/emilybache/SupermarketReceipt-Refactoring-Kata) — `main` (no tests) vs `with_tests` branch.

---

## Tier 3 — Style Guides w/ Inline Bad↔Good

- [ryanmcdermott/clean-code-javascript](https://github.com/ryanmcdermott/clean-code-javascript) — 90k★. Bad/Good per principle.
- [labs42io/clean-code-typescript](https://github.com/labs42io/clean-code-typescript) — TS port.
- [zedr/clean-code-python](https://github.com/zedr/clean-code-python) — Python port.
- [davified/clean-code-ml](https://github.com/davified/clean-code-ml) — ML/Jupyter notebooks. Underrated.

---

## Tier 4 — Single-Smell Drills

| Smell | Repo |
|-------|------|
| Conditional → Polymorphism | [emilybache/Parrot-Refactoring-Kata](https://github.com/emilybache/Parrot-Refactoring-Kata) |
| Primitive Obsession | [codecop/BankOCR-Refactoring-Kata](https://github.com/codecop/BankOCR-Refactoring-Kata) |
| Bumpy Road | [gregorriegler/payroll-refactoring-kata](https://github.com/gregorriegler/payroll-refactoring-kata) |
| Imperative → Functional | [matteobaglini/functional-structures-refactoring-kata](https://github.com/matteobaglini/functional-structures-refactoring-kata) — Scala solutions on `solution-*` branches |
| Hexagonal extraction (real DB) | [martinsson/Refactoring-Kata-Lift-Pass-Pricing](https://github.com/martinsson/Refactoring-Kata-Lift-Pass-Pricing) |
| Long Method, Duplication | [emilybache/Yatzy-Refactoring-Kata](https://github.com/emilybache/Yatzy-Refactoring-Kata) |
| Conditional chains (3 variants) | [emilybache/Tennis-Refactoring-Kata](https://github.com/emilybache/Tennis-Refactoring-Kata) |
| GildedRose w/ approval tests | [emilybache/GildedRose-Approval-Kata](https://github.com/emilybache/GildedRose-Approval-Kata) |

---

## Tier 5 — Framework-Specific Refactors

- [oliverjam/react-refactor-class-hooks](https://github.com/oliverjam/react-refactor-class-hooks) — class components → hooks.
- [appacademy/practice-for-week-15-react-refactoring-class-components-long-practice](https://github.com/appacademy/practice-for-week-15-react-refactoring-class-components-long-practice) — bootcamp curriculum w/ Jest validation.
- [intojs/refactor-nodejs-routes](https://github.com/intojs/refactor-nodejs-routes) — Express callbacks → async/await.
- [dtanzer/babystepstimer](https://github.com/dtanzer/babystepstimer) — commit history *is* the trail. C#/C++/Swift/TS.

---

## Tier 6 — Production Case Studies (Read, Don't Clone)

### Strangler Fig pattern
- [Thoughtworks 3-part series](https://www.thoughtworks.com/en-us/insights/articles/embracing-strangler-fig-pattern-legacy-modernization-part-one) — coupon system. Part 2 = org friction, not tech.
- [softwaremodernizationservices.com VB6 → .NET 8](https://softwaremodernizationservices.com/insights/strangler-fig-pattern-example/) — metrics-heavy. **92% failure rate** if <5% extracted in 90 days.
- [Martin Fowler canonical bliki](https://martinfowler.com/bliki/StranglerFigApplication.html).

### Monolith → Modular
- [Shopify "Deconstructing the Monolith"](https://shopify.engineering/deconstructing-monolith-designing-software-maximizes-developer-productivity) + [Packwerk repo](https://github.com/Shopify/packwerk) — boundary enforcement at CI time.
- [Shopify "State of Monolith"](https://shopify.engineering/shopify-monolith) — they deliberately did *not* go microservices.
- [GitHub microservices QCon talk writeup](https://blog.quastor.org/p/github-shifted-monolith-microservices) — "have a plan to hit 100% traffic or you support two paths forever."

### Production DDD reference
- [kgrzybek/modular-monolith-with-ddd](https://github.com/kgrzybek/modular-monolith-with-ddd) — 13.3k★. C#. Aggregates, ValueObjects, Domain Events. The *after* state at production grade.

### Legacy → Testable (Feathers)
- [Feathers' characterization-testing blog](https://michaelfeathers.silvrback.com/characterization-testing) — fail-first technique.
- [understandlegacycode.com summary](https://understandlegacycode.com/blog/key-points-of-working-effectively-with-legacy-code/) — seam preference order: **object > link > preprocessing**.

### God Class Breakdown
- [DigDeepRoots "Split God Class"](https://www.digdeeproots.com/articles/split-god-class/) — **field-access clustering** beats subjective "responsibility" debates.
- [Sandi Metz "All the Little Things" RailsConf 2014](https://www.rubyevents.org/talks/all-the-little-things) — live GildedRose refactor. Most-watched refactoring talk.

### Hexagonal at Scale
- [Netflix "Ready for Changes with Hexagonal Architecture"](https://netflixtechblog.com/ready-for-changes-with-hexagonal-architecture-b315ec967749) — Studio Workflow. Caveat: hexagonal = overhead for pure CRUD.

### Callback Hell → async/await
- [Thomas Hunter II — Node.js refactor](https://thomashunter.name/posts/2017-09-03-refactoring-a-nodejs-codebase-using-async-await) — 1714 → 1585 LOC, 5 nested callbacks → 1 function.

### Automated Mass Refactoring
- [openrewrite/rewrite](https://github.com/openrewrite/rewrite) — AST-level recipes. Study for "provable automated refactoring" at scale.

---

## Supporting Tools / Meta-Resources

- [InnovatingTeams/provable-refactorings](https://github.com/InnovatingTeams/provable-refactorings) — step-by-step recipes guaranteed behaviour-preserving if followed exactly.
- [RefactoringCombos/ArlosCommitNotation](https://github.com/RefactoringCombos/ArlosCommitNotation) — commit notation marking refactoring risk per commit (`r -` provable, `R!!` risky).
- [Refactoring.guru](https://refactoring.guru/refactoring) — Fowler smell + technique catalogue, online + searchable.
- [Martin Fowler refactoring code samples page](https://martinfowler.com/articles/2024-refactoring-code-samples.html) — official multi-language ports of book chapter 1.

---

## Suggested Learning Path

1. **Read first:** Fowler's Theatrical Players chapter → clone kata, walk through book.
2. **First kata:** GildedRose (start with characterization tests, not edits).
3. **Break statics:** Trip Service Kata. Watch Mancuso's video after attempt.
4. **SOLID drilling:** Racing Car Katas (5 small exercises).
5. **Legacy capstone:** jbrains/trivia (mentor or pair recommended).
6. **Architecture-scale:** Lift Pass Pricing (real DB, hexagonal extraction).
7. **Production reading:** Shopify Packwerk + Netflix hexagonal + DigDeepRoots God Class split.

---

## Key Insights

- **Cross-validation pattern.** Three research lenses agreed: katas (interactive practice), smell catalogues (browse-only), production case studies (architectural-scale). Most repos cluster around three pedagogical traditions:
	- Emily Bache (workshop pedigree, kata translations)
	- Sandro Mancuso / Codurance / London craftsmanship
	- Michael Feathers' seam-finding doctrine
- **Commit-history-as-tutorial** (babystepstimer, jbrains/trivia retreat branches) is the underrated form. Each commit = one provable refactoring step. Pairs perfectly with `provable-refactorings` recipes + Arlo's Commit Notation. This is how you train *discipline*, not just pattern recognition.
- **Workshop wisdom from Nicolas Carlo (understandlegacycode.com):** Do GildedRose + Tennis + Trip Service *before* attempting Trivia. Trivia is the capstone, not the entry.
- **Sandi Metz secret** (per Eric Normand review of *All the Little Things*): she's secretly doing domain modelling all along — the refactoring is the vehicle for discovering domain concepts, not cleaning syntax. Most teams miss this and stop at cosmetic cleanup.
- **Production failure mode:** 68% of strangler-fig migrations stall before day 90. Teams that extract <5% of monolith functionality in the first 90 days have a 92% failure rate.

---

## Related notes

- [[Clean Code]]
- [[Test-Driven Development]]
- [[Domain-Driven Design]]
- [[Hexagonal Architecture]]
