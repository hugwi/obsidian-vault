#!/usr/bin/env python3
"""Command line for the target-hypothesis engine.

    python3 cli.py rank                          rank everything in the ledger
    python3 cli.py explain PCSK9 ASCVD           the full argument for one pair
    python3 cli.py discover DRY_AMD              propose targets with no direct evidence
    python3 cli.py plan TREM2 AD --budget 200000 what to do next, priced
    python3 cli.py backtest                      time-split evaluation
    python3 cli.py rediscover                    can it find known discoveries blind
    python3 cli.py export --out digest.md        write an Obsidian note
    python3 cli.py sources                       which live data sources are reachable

Every command takes --as-of YEAR to restrict the ledger to what was knowable then.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from engine import backtest as bt  # noqa: E402
from engine import experiments as exp  # noqa: E402
from engine import report  # noqa: E402
from engine import safety as safety_mod  # noqa: E402
from engine.graph import bridges, discover  # noqa: E402
from engine.ledger import Ledger  # noqa: E402
from engine.scoring import rank, score_pair  # noqa: E402


def enrich(h, ledger, budget=None):
    """Attach safety and experiment plan to a scored hypothesis."""
    h.safety = safety_mod.scan(ledger, h)
    h.experiments = exp.plan(ledger, h, budget_usd=budget)
    return h


def cmd_rank(args, ledger: Ledger) -> int:
    hyps = rank(ledger, saturation=args.saturation)
    if args.disease:
        hyps = [h for h in hyps if h.disease == args.disease]
    if args.min_breadth:
        hyps = [h for h in hyps if h.evidence_breadth >= args.min_breadth]
    print(report.table(hyps, ledger, limit=args.limit))
    print()
    print(f"{len(hyps)} hypotheses scored from {len(ledger.atoms)} evidence atoms."
          f"{f'  Ledger restricted to before {args.as_of}.' if args.as_of else ''}")
    return 0


def cmd_explain(args, ledger: Ledger) -> int:
    h = enrich(score_pair(ledger, args.target, args.disease, saturation=args.saturation), ledger, args.budget)
    if not h.class_scores:
        print(f"No evidence in the ledger for {args.target} -- {args.disease}.")
        paths = bridges(ledger, args.target, args.disease)
        if paths:
            print("\nMechanism paths that do exist:")
            for p in paths[:5]:
                print(f"  {p}")
            print("\nRun `discover` on the disease to score this as a generated hypothesis.")
        return 1
    print(report.card(h, ledger))
    return 0


def cmd_discover(args, ledger: Ledger) -> int:
    proposals = discover(ledger, args.disease, max_len=args.max_path, require_sign=not args.allow_ambiguous)
    if not proposals:
        print(f"No unevidenced targets reachable from {args.disease} within {args.max_path} edges.")
        return 1
    for h in proposals[: args.limit]:
        enrich(h, ledger, args.budget)
    print(f"# Generated hypotheses for {ledger.name(args.disease)}")
    print()
    print(f"{len(proposals)} targets have a mechanism path to this disease and no direct evidence in the "
          f"ledger. Showing {min(args.limit, len(proposals))}, ranked by posterior weighted by tractability.")
    print()
    print(report.table(proposals, ledger, limit=args.limit))
    print()
    for h in proposals[: args.limit]:
        print(report.card(h, ledger))
        print("---")
        print()
    return 0


def cmd_plan(args, ledger: Ledger) -> int:
    h = enrich(score_pair(ledger, args.target, args.disease), ledger, args.budget)
    print(f"{h.target} -- {ledger.name(h.disease)}   posterior {h.posterior:.1%}, direction {h.direction.value}")
    print()
    if not h.experiments:
        print("Nothing left to measure: every evidence class is already answered.")
        return 0
    for e in h.experiments:
        mark = "  <- KILL EXPERIMENT" if e.is_kill_experiment else ""
        print(f"{e.bits_per_100k:>6.2f} bits/$100k  {e.expected_info_gain:>5.2f} bits  "
              f"${e.cost_usd:>9,.0f}  {e.weeks:>3.0f}w  {e.name}{mark}")
        print(f"{'':>14}if positive {e.posterior_if_positive:.0%} / if negative {e.posterior_if_negative:.0%}")
    print()
    print(exp.summarise(h))
    return 0


def cmd_backtest(args, ledger: Ledger) -> int:
    rep = bt.run(ledger)
    print("# Time-split backtest")
    print()
    print("Each programme scored using only evidence published before its clinical entry year.")
    print()
    print(f"{'PROGRAMME':<28} {'ENTRY':>5} {'P(SUCC)':>8} {'BREADTH':>8}  OUTCOME")
    print("-" * 82)
    for r in sorted(rep.results, key=lambda r: -r.posterior):
        print(f"{r.id:<28} {r.entry_year:>5} {r.posterior:>7.1%} {r.breadth:>8}  {r.outcome}")
    print()
    scored_n = rep.n_positive + rep.n_negative
    print(f"n = {rep.n_positive} approved, {rep.n_negative} failed "
          f"({len(rep.results) - scored_n} still running, excluded)")
    if rep.auc is not None:
        print(f"AUC {rep.auc:.2f} over all {scored_n}  |  "
              f"AUC {rep.auc_covered:.2f} over the {rep.n_covered} where the ledger held any pre-entry evidence")
        print(f"Brier {rep.brier:.3f}  |  mean posterior {rep.mean_posterior_success:.1%} approved vs "
              f"{rep.mean_posterior_failure:.1%} failed (separation {rep.separation:+.1%})")
    print()
    print("Calibration by predicted band:")
    for c in rep.calibration:
        print(f"  {c['band']:>8}  n={c['n']:<3} predicted {c['predicted']:.0%}  observed {c['observed']:.0%}")
    print()
    print("Read that calibration table with care, and preferably not at all. outcomes.json is a list of")
    print("programmes famous enough to curate, so it is roughly 80% approvals against a true base rate")
    print("nearer 10%. Observed frequencies in it measure the sampling, not the engine. Discrimination")
    print("(AUC) survives that bias; calibration does not, and would need a full unselected cohort.")
    print()
    print("Two dozen hand-curated programmes is a sanity check, not a validation. It says the ordering")
    print("is not accidental. It does not say the probabilities are right.")
    return 0


def cmd_rediscover(args, ledger: Ledger) -> int:
    results = bt.rediscovery(ledger)
    print("# Rediscovery")
    print()
    print("Ground truth lives in data/discoveries.json and is never read by the scoring path.")
    print()
    for r in results:
        status = f"rank {r.rank} of {r.total_candidates}" if r.rank else f"NOT FOUND ({r.total_candidates} candidates)"
        print(f"## {r.id}  [{status}]")
        print(f"   targets       {', '.join(r.targets)}  ->  {ledger.name(r.disease)}")
        print(f"   ledger cutoff {r.cutoff_year} (everything from {r.cutoff_year + 1} onwards hidden)")
        if r.found_path:
            print(f"   bridge        {r.found_path}")
            print(f"   direction     {r.inferred_direction}")
        print(f"   actually      {r.citation}")
        print()
    return 0


def cmd_export(args, ledger: Ledger) -> int:
    if args.disease:
        hyps = discover(ledger, args.disease, max_len=args.max_path)[: args.limit]
        title = f"Target hypotheses — {ledger.name(args.disease)}"
        subtitle = (
            f"Generated hypotheses for {ledger.name(args.disease)}: targets with a mechanism path to the "
            f"disease and no direct evidence linking them to it."
        )
    else:
        hyps = rank(ledger)[: args.limit]
        title = "Target hypothesis digest"
        subtitle = "Every target-disease pair the ledger holds evidence for, ranked."
    for h in hyps:
        enrich(h, ledger, args.budget)
    out = Path(args.out)
    out.write_text(report.digest_note(hyps, ledger, title=title, subtitle=subtitle))
    print(f"Wrote {out} ({len(hyps)} hypotheses)")
    return 0


def cmd_sources(args, ledger: Ledger) -> int:
    from engine import connectors

    print("Live data sources:")
    print()
    any_down = False
    for p in connectors.probe():
        mark = "ok  " if p.reachable else "DOWN"
        print(f"  [{mark}] {p.source:<20} {p.detail}")
        any_down = any_down or not p.reachable
    print()
    if any_down:
        print("Unreachable sources fall back to data/ -- the curated snapshot described in README.md.")
        print("Nothing here silently returns empty results when a source is blocked.")
    return 0


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--as-of", type=int, default=None, metavar="YEAR",
                   help="restrict the ledger to evidence published before YEAR")
    p.add_argument("--saturation", choices=["noisy_or", "harmonic"], default="noisy_or",
                   help="within-class aggregation (harmonic reproduces Open Targets)")
    p.add_argument("--budget", type=float, default=None, help="experiment budget in USD")
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("rank", help="rank every scored pair")
    s.add_argument("--disease", default=None)
    s.add_argument("--limit", type=int, default=25)
    s.add_argument("--min-breadth", type=int, default=0)
    s.set_defaults(fn=cmd_rank)

    s = sub.add_parser("explain", help="full argument for one target-disease pair")
    s.add_argument("target")
    s.add_argument("disease")
    s.set_defaults(fn=cmd_explain)

    s = sub.add_parser("discover", help="propose targets with no direct evidence")
    s.add_argument("disease")
    s.add_argument("--limit", type=int, default=5)
    s.add_argument("--max-path", type=int, default=4)
    s.add_argument("--allow-ambiguous", action="store_true",
                   help="include candidates whose mechanism paths disagree on direction")
    s.set_defaults(fn=cmd_discover)

    s = sub.add_parser("plan", help="rank next experiments by information per dollar")
    s.add_argument("target")
    s.add_argument("disease")
    s.set_defaults(fn=cmd_plan)

    s = sub.add_parser("backtest", help="time-split retrospective evaluation")
    s.set_defaults(fn=cmd_backtest)

    s = sub.add_parser("rediscover", help="blind rediscovery of known findings")
    s.set_defaults(fn=cmd_rediscover)

    s = sub.add_parser("export", help="write an Obsidian note")
    s.add_argument("--out", default="digest.md")
    s.add_argument("--disease", default=None)
    s.add_argument("--limit", type=int, default=10)
    s.add_argument("--max-path", type=int, default=4)
    s.set_defaults(fn=cmd_export)

    s = sub.add_parser("sources", help="probe live data sources")
    s.set_defaults(fn=cmd_sources)

    args = p.parse_args(argv)
    ledger = Ledger.load().as_of(args.as_of)
    if not hasattr(args, "saturation"):
        args.saturation = "noisy_or"
    return args.fn(args, ledger)


if __name__ == "__main__":
    raise SystemExit(main())
