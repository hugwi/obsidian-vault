# Beck's Two-Hat Rule

Never wear both hats at the same time.

1. **Bug-fix hat**: change behavior without changing structure. Tests that fail start passing. Don't touch surrounding architecture.
2. **Refactor hat**: change structure without changing behavior. All tests stay green throughout. No new features, no bug fixes.

Mixing the two:
- Bug fixes hide behind structural noise — reviewers can't tell which line caused the fix.
- Refactors get blamed for regressions they didn't cause.
- Reverts become surgery instead of single-button.

Rule: fix → ship → tidy. Or: tidy → ship → fix. Two PRs, two commits, two reviews.

Related: "Make the change easy (warning: this may be hard), then make the easy change." — Kent Beck

See also: *Tidy First* (Beck, 2023), *Refactoring* (Fowler, 1999)
