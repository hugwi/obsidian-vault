---
created: 2026-08-14
categories:
  - "[[Projects]]"
project: "[[Blog]]"
status: pursue
outcome: Published three posts — AI UX slop, how to actually measure engineering success, and structural lint rules in a legacy codebase.
due: 
tags:
  - blog
  - writing
  - content
---

# Blog

Idea shelf for posts and LinkedIn writing. Three in the pipe. Each idea below has a
**thesis** (the one sentence the post has to earn), an **outline**, **research/refs**,
and **open questions** — the things I still have to decide before drafting.

> [!note] Conventions
> Long-form goes on the blog, the short provocation goes on LinkedIn and links back.
> Anything I clip as raw material for one of these gets `project: "[[Blog]]"` so it
> lands on the desk below without leaving `Clippings/`. See [[Project workflow]].

**Done when:**
- [ ] Idea 1 — AI UX/UI slop + slop-voting + [[Netlight]] audit offer, published
- [ ] Idea 2 — LinkedIn post on bad success metrics, published
- [ ] Idea 2b — follow-up blog on what to measure instead, published
- [ ] Idea 3 — structural lint rules in a dirty codebase, published

---

## Idea 1 — Reducing AI UX/UI slop (and will scroll-hijacking be the next kind?)

**Thesis.** AI slop isn't one aesthetic, it's a *moving target*. Every time the tools
get better, the tell moves — and the tell is always the same underlying failure:
the model outputs the statistical average of the web, and nobody edited it afterwards.

### The argument: slop has had two generations so far

| Gen | What it looked like | How you spotted it |
|---|---|---|
| **1. Genuinely ugly** | Broken spacing, mismatched type scales, clipped layouts, stock-photo mush | You could see it from across the room |
| **2. Competent but templated** | Tailwind `blue-600 → purple-500` hero gradient, Inter bold centered headline, three equal-width feature cards with thin-line icons, "Get Started" CTA, and the same closing section every time | Looks fine at a glance. The *copy* gives it away — the boilerplate closing line, the "It's not just X — it's Y" construction, the em-dash cadence |

The gen-2 tell is worth being precise about, because it's the interesting one: the
layout passes, and then the **last block of text on the page** always reads the same.
The negative-parallelism construction ("It's not just a tool — it's a workflow") plus
the closing CTA paragraph is the most reliable fingerprint left, and it's a *writing*
fingerprint, not a design one. Design got good enough to hide; the copy didn't.
(Worth noting for fairness: no single tell proves anything — em-dashes have been in
edited English forever. It's the *density and co-occurrence* of tells that's the
signal.)

### The prediction: gen 3 is motion

Right now the hype has moved to heavily animated sites — scroll-driven timelines,
pinned sections, scroll hijacking. GSAP went fully free (plugins included) in 2026,
every "Awwwards clone in 20 minutes" tutorial is a ScrollTrigger tutorial, and the
agents have learned it. So: **is scroll-hijacking the next slop?**

My take — and this is the spine of the post: yes, and it will be *worse* than gen 2,
because gen-2 slop was merely boring, whereas motion slop actively hurts people.

- NN/g usability work found the majority of participants got at least mildly
  disoriented by scrolljacking; some read the altered scroll as a *bug*.
- Parallax, zoom transitions and auto-scroll trigger dizziness, nausea and migraines
  in users with vestibular sensitivity.
- It routinely ignores `prefers-reduced-motion` — a setting the user explicitly chose.
- Keyboard and screen-reader users can get stuck outright.
- It's slow and unpredictable on mobile, which is where the traffic is.

So the pattern repeats: the tool makes a hard thing cheap → everyone does the cheap
version → the cheap version has a fingerprint → the fingerprint becomes the slop.
Gen 1 was cheap layout. Gen 2 was cheap taste. Gen 3 is cheap motion. **Gen 4 is
probably cheap *interaction*** — AI-generated micro-interactions and "agentic" UI
that reorganises itself, where the tell will be that nothing sits still long enough
to be learned.

### The counter-position I have to take seriously

Not all animation is slop, and "AI-looking" is not the same as "bad". A pinned
scroll sequence on a product story page is a legitimate craft choice. The line I'll
draw in the post: **does the effect complement the user's scroll, or take it over?**
Complementing is craft. Taking over is slop. That gives readers a usable test instead
of a vibe.

### Interactive bit — "Is this site AI slop?" voting

The post should not just assert the tells, it should *collect* them.

- Reader pastes a URL (or picks from a seeded gallery) and votes: **slop / not slop /
  borderline**.
- Second question, the useful one: *why?* — checkbox tells (gradient hero, three-card
  grid, negative-parallelism copy, scroll hijack, no reduced-motion respect,
  boilerplate closing CTA, generic stock illustration).
- Results shown live. Over time this becomes a dataset of what people actually
  register as slop, which is a *second* post and a talk.
- Seed it with a handful of sites I'm confident about in each direction so the first
  visitor sees something.

Open design questions: moderation (people will submit competitors' sites — probably
no public URL list, aggregate only, or a curated gallery only), and whether a public
"this site is slop" scoreboard is a fight worth having. Leaning: **curated gallery,
aggregate results, no user-submitted public shaming.**

### The [[Netlight]] angle

Close with what we're actually doing about it: at Netlight we're starting to run
**UX/UI audits** — going through a site or product against exactly these criteria
(taste and consistency, motion and accessibility, copy authenticity, does the design
carry a point of view) and coming back with a concrete improvement plan. The post
earns the offer instead of being an ad for it: reader gets the checklist for free,
and the audit is "we do this properly, with research and a plan."

Needs a decision on positioning — audit as a standalone offer vs. part of the wider
AI-transformation work in [[AI Transformation]].

### Refs
- [AI Slop Web Design: Complete Guide to Spotting and Fixing Generic Websites (2026)](https://www.925studios.co/blog/ai-slop-web-design-guide)
- [Why Your AI Keeps Building the Same Purple Gradient Website](https://prg.sh/ramblings/Why-Your-AI-Keeps-Building-the-Same-Purple-Gradient-Website)
- [AI Slop in 2026: The State of the AI-Generated Web (100-page report)](https://www.sailop.com/blog/ai-slop-2026-state-of-the-ai-generated-web)
- [Unslop UI: Kill the AI Design Tells](https://www.claudecodehq.com/playbooks/unslop-ui)
- [Don't Fuck With Scroll — Stop Scrolljacking the Web](https://dontfuckwithscroll.com/)
- [Avoid scrolljacking and custom scroll behavior — Front-End Checklist](https://frontendchecklist.io/rules/accessibility/scrolljacking)
- [Most UI Animations Shouldn't Exist — Trevor Calabro](https://trevorcalabro.substack.com/p/most-ui-animations-shouldnt-exist)
- [Designing for Reduced Motion — Craft CMS](https://craftcms.com/blog/designing-for-reduced-motion)
- [The phrases that give away AI writing — Ritner Digital](https://www.ritnerdigital.com/blog/the-phrases-that-give-away-ai-writing-and-how-to-edit-them-out-before-they-cost-you-trust)
- [The em dash isn't an AI fingerprint](https://jamaalglenn.substack.com/p/the-em-dash-isnt-an-ai-fingerprint) — the fair counter-argument
- Vault: [[Inspiration]] (the gallery is the "not slop" evidence base) ·
  [[7 Rules for Creating Gorgeous UI (01kn9zv7vjs2fn3r9yksh1xez4)]] ·
  [[Every UI-UX Concept Explained in Under 10 Minutes (01kna4wk4axs6p6078mytd9pnr)]] ·
  [[Beck Design Rules (01ks7c0ngsfj5whrewh690b6wm)]]

### Open questions
- [ ] Do I have permission/appetite to name real sites as examples, or only anonymised screenshots?
- [ ] Where does the voting widget live — own the hosting, or a hosted poll?
- [ ] Is the Netlight audit far enough along to link to a real page, or is it "get in touch"?

---

## Idea 2 — Stop measuring engineering success by lines of code and story points

**Format.** LinkedIn post first (the provocation), then a longer blog post on what to
measure instead. Keep the LinkedIn one short and pointed; put the nuance in the blog.

**Thesis.** Lines-of-code leaderboards and story-point velocity aren't *imperfect*
measures of engineering success — they measure something that isn't success at all,
and in the AI era they've gone from useless to actively harmful.

### Why LoC is worse now than it ever was

LoC was always a bad proxy: it rewards volume and punishes deletion, which is the
single highest-leverage thing an engineer does. But AI broke it completely — output
volume is now nearly free, so a LoC leaderboard is a leaderboard of *who accepted the
most autocomplete*. Same for "PRs merged" and "commits."

### Why story points are a different kind of wrong

Story points are a **team-relative** estimate. Comparing velocity across teams is
arithmetic on incompatible units. And the moment velocity becomes a target, it stops
being a measure — teams inflate estimates, not output. Goodhart, on a two-week cadence.

### The receipts

- **METR RCT (July 2025):** experienced open-source developers were **19% slower**
  with early-2025 AI tools — while believing they'd been sped up by ~20%. That gap
  between *felt* and *measured* productivity is the whole post in one number.
  *Honest caveat I should include:* METR published an update in Feb 2026 after finding
  a selection effect (30–50% of invited devs declined without AI access, biasing the
  sample). The newer cohort — 57 developers, 800+ tasks — showed **-4%** with a CI of
  -15% to +9%, i.e. much closer to "no measurable effect" than to a 19% slowdown.
  I'd rather cite both than get called out; the argument doesn't need the big number.
  The point stands either way: **self-reported speed is not evidence.**
- **DORA 2025 AI Capabilities Model:** teams reporting individual productivity gains
  are simultaneously seeing slower delivery, more bugs and longer reviews. The tools
  generate code faster than organisations can safely absorb it.
- Even DORA gets misused — the metrics are diagnostic, not a leaderboard. Teams that
  optimise for the number instead of the outcome will game the number.

### What to measure instead (the blog follow-up)

The structure I want:

1. **Never measure an individual with a system metric.** Every framework says this
   and every org does it anyway.
2. **DORA** for delivery flow (change lead time, deployment frequency, change failure
   rate, failed-deployment recovery) — as a diagnostic, at team level.
3. **SPACE** for the reminder that satisfaction, performance, activity, communication
   and efficiency are five *different* axes and activity is the least useful one.
4. **DX Core 4** as the practical synthesis: speed, effectiveness, quality, business
   impact. Key rule from their own guidance — speed metrics like diffs/engineer are
   *dangerous in isolation* and only work counterbalanced by experience metrics, and
   never tied to individual performance targets.
5. **Outcome metrics that actually mean success**: did the thing we shipped move the
   number we shipped it for? Adoption, retention, revenue, cost-to-serve, incident
   load. Uncomfortable, slow, and the only ones that are actually about success.
6. **AI-specific quality drift**, which connects straight to Idea 3: complexity
   trend, duplication, review latency, revert rate, % of PRs touching the same code
   twice within N days. See
   [[code-quality-metrics-measuring-ai-code-drift-using-github-metrics.md a… (01kr8qqpadyvjhyej7k9hwwqa6)]]
   — including its point that `git merge --squash` destroys the granular signal, so
   you have to measure pre-merge.

### Refs
- **Reference post from the user:** <https://x.com/i/status/2088116654102249957>
  — ⚠️ **not yet captured.** x.com is blocked from this environment, so I couldn't
  read it. Paste the text or a screenshot into this note before drafting, so the post
  can quote it properly and credit the author.
- [METR — Measuring the Impact of Early-2025 AI on Experienced OSS Developer Productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/) · [arXiv 2507.09089](https://arxiv.org/abs/2507.09089)
- [Measuring developer productivity with the DX Core 4](https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4/)
- [How to measure developer productivity — DX](https://getdx.com/blog/developer-productivity/)
- [Developer Productivity Metrics 2026: From DORA to DevEx and Beyond](https://zylos.ai/research/2026-02-07-developer-productivity-metrics/)
- Vault: [[Is There A Right Way To Write User Stories (01kcmg2qj0ja56sf5p0gcjp0ec)]] ·
  [[GitHub - middlewarehq-middleware:  Open-source DORA metrics platform f… (01kr280nq0b1s5a1c3qd1k1yja)]] ·
  [[GitHub - mikaelvesavuori-github-dora-metrics: Instant, badge-ready DOR… (01kr2801w835pagbeb3nazenyz)]] ·
  [[The hidden technical debt of agentic engineering (01knacfykmbc0ggg22m3dvprct)]]

### Open questions
- [ ] Hook for the LinkedIn post — lead with the METR perception gap, or with a
      concrete "we ran a LoC leaderboard and here's what happened"?
- [ ] Do I name the anti-pattern with a real example (a client, anonymised) or keep
      it general? A real story is 10x the engagement and 10x the risk.

---

## Idea 3 — Introducing structural lint rules into a codebase that's already bad

**Thesis.** You don't fix a dirty codebase by turning on `complexity: error` and
watching CI go red for six months. You turn the rules on as **warnings**, feed those
warnings to the agent as *state*, and let the boy-scout rule plus a never-worse gate
do the work commit by commit.

### The setup

The rules worth having are the structural ones — cyclomatic/cognitive complexity,
`max-lines`, `max-lines-per-function`, `max-params`, `max-depth`. In a greenfield repo
you just turn them on. In a repo with years of accumulated code, turning them on as
errors is a non-starter: thousands of violations, nobody can ship, the rules get
switched off within a week and never come back.

### The mechanism I want to propose

1. **Warn, don't error.** New rules land at `warn`. Nothing is blocked.
2. **Feed the warnings back to the LLM as context.** The agent sees the current
   quality state of the files it's touching — not as a lecture in `CLAUDE.md`, but as
   live linter output in its loop. It now *knows* the code is bad, and where.
3. **Boy-scout rule: leave it better than you found it.** The agent's brief includes
   improving what it touches, not just what it was asked to change.
4. **Never-worse quality gate.** Measure the metric at the start of the change and
   again at the end. The change can leave the number the same or better; it cannot
   make it worse. That's a *delta* gate, not an absolute one — which is exactly what
   makes it adoptable on day one in a repo with 4,000 violations.
5. Over time the ratchet tightens: once a rule's violation count hits zero in a
   directory, it graduates from `warn` to `error` there.

> [!important] Revised after research — see findings below
> Step 1 should probably **not** be warn-only. ESLint's native bulk suppression
> (`--suppress-all`, v9.24+) sets the rule to `error` and snapshots today's violations
> to a file, and because it **exits 2 on unused suppressions by default**, it *is*
> the never-worse ratchet — steps 1, 4 and 5 collapse into one built-in feature.
> And Google's Tricorder data says warnings surfaced outside the workflow get
> ignored regardless of severity. Keep warn-only as the story of what I tried first.

### The caveat that makes this hard — and it's the best part of the post

**A threshold rule can be satisfied without improving anything.** The canonical case
is `max-params`: the rule fires on a 4-argument method, and the agent "fixes" it by
wrapping the four arguments in one object. Lint goes green. The method still depends
on exactly the same four facts. Nothing improved — the braces moved.

I already wrote this up in detail:
**[[Max-Params Lint — The Parameter-Object Trap]]** — a real case from `ethira/api`
where the honest fix was to notice the method had two responsibilities, split it, and
watch the argument count fall out as a *consequence*. The note has the decision tree:

- fields form one real concept (a value object)? → parameter object is legitimate
- one arg is only forwarded onwards (Feature Envy)? → move the behaviour to the data,
  the arg evaporates
- method owns >1 responsibility? → split it, the count drops by itself
- **never** wrap-to-silence when the fields are unrelated

That note is the backbone of the second half of the post: *green lint ≠ good refactor*,
and a metric an agent can game is a metric that will be gamed. Which means the gate
needs teeth against gaming too — banning inline `eslint-disable` as an escape hatch,
flagging unused disable directives, and reviewing *why* a number went down, not just
that it did.

### Research findings

> [!warning] Verification status
> Gathered 2026-08-14. Several sources were unreachable from the research
> environment (arxiv.org, eslint.org, dev.to, substack, docs.astral.sh, docs.trunk.io,
> factory.ai). Where a claim is second-hand from search summaries it says so below —
> **verify those before putting a number in a published post.**

#### The big correction to my plan: "warn-first" is the weakest of four options

I'd assumed warn-only was *the* way in. It's actually the crudest of four
mechanically distinct strategies, and the evidence says it's the one most likely to
be ignored.

| Strategy | How it works | Tools |
|---|---|---|
| **Per-violation suppression file** | Rule set to `error`; every current violation snapshotted to a machine-generated file | ESLint **native** `--suppress-all` → `eslint-suppressions.json` (v9.24, Apr 2025) · `@rushstack/eslint-bulk` |
| **Per-metric count file** | Snapshot the *count*, fail on increase, auto-lower on improvement | **betterer** (`.betterer.results`) · `eslint-formatter-ratchet` |
| **Diff-scoped** | Old code is never linted at all; only changed lines are | `eslint-plugin-diff` · **trunk hold-the-line** · `reviewdog -filter-mode=added` · Sonar **Clean as You Code** |
| **Warn + `--max-warnings N`** | Pin N at today's count, lower over time | plain ESLint |

The one that changes my design: **ESLint's native bulk suppression is already a
ratchet.** Once you fix a suppressed violation the entry goes stale, and ESLint
**exits 2 on unused suppressions by default** (`--prune-suppressions` to clean,
`--pass-on-unpruned-suppressions` to opt out). So counts can only go down — that's the
never-worse gate, for free, built in, no custom script. That's the config the post
should ship.

**Trunk's hold-the-line** is the most rigorous take on diff-scoping: it runs the
linters *twice per modified file* — once against upstream, once against the worktree —
and diffs the result sets, so a pre-existing issue on a line you touched stays quiet
while a genuinely new one fires.

**The evidence against pure warn-first** — and this is the strongest empirical thing
in the whole research pile — is Google's Tricorder work (Sadowski et al., CACM 2018).
Warnings surfaced *outside* the workflow were repeatedly ignored; results delivered at
**code-review time with suggested fixes** got applied. They tolerate up to **10%
effective false positives** at review time vs. near-zero at compile time. Conclusion
for the post: **where the warning appears matters more than how strict the rule is.**
Which is the same insight as "feed it to the agent" — the agent's loop *is* the
workflow now.

#### Which rules — the evidence is weaker than the tooling implies

Defaults: ESLint `max-lines-per-function` 50 · `max-depth` 4 · `max-params` 3 ·
`complexity` off (commonly set 10–20) · `sonarjs/cognitive-complexity` 15.
Python: `PLR0913` 5 · `PLR0917` 5.

- **Shepperd (1988), "A critique of cyclomatic complexity as a software metric"** —
  v(G) rests on poor theoretical foundations and for a large class of software "is no
  more than a proxy for, and in many cases is outperformed by, lines of code." Held up
  since. **A CC threshold is largely a length threshold in disguise.**
- **Muñoz Barón, Wyrich & Wagner (ESEM 2020)** — meta-analysis over ~24,000
  understandability evaluations of 427 snippets: cognitive complexity correlates
  **0.654 with comprehension time**, 0.411 with subjective ratings — but *mixed to no*
  correlation with correctness.
- **Lenarduzzi, Kilamo & Janes (2023)** — 216 junior devs, 12 Java classes: cognitive
  complexity only slightly beats cyclomatic, and **neither predicts perceived
  understandability once complexity is already high.**

Honest reading for the post: **low values mean "probably fine", high values mean
"unpredictable", not "defective".** Thresholds are budgets, not truths. Recommendation
that falls out: prefer `max-lines` / `max-lines-per-function` (honest and cheap),
`max-depth` (nesting is what cognitive complexity actually punishes), and
`sonarjs/cognitive-complexity` over raw `complexity`.

#### The parameter-object trap — external confirmation, plus a real fix

**Kent Beck says the same thing I found in `ethira/api`.** In *Tidy First?* he argues
creating an object purely to group parameters "always makes the code worse" — it hides
the loose parameters in a bag while they're still there and accessed the same way,
adding indirection without abstraction, and making the underlying smell *harder* to
see. ⚠️ Second-hand from search excerpts of `tidyfirst.substack.com/p/tt-chapter-parameters-object`
— substack was blocked, so **verify the wording before quoting Beck.** Fowler's
*Introduce Parameter Object* only pays when the object names a genuine domain concept,
which is exactly the distinction in [[Max-Params Lint — The Parameter-Object Trap]].

**The rule-design fix I didn't know about, and it's the best find here:**
count *positional* arguments, not arguments. Ruff `PLR0917` / Pylint `R0917` exist
precisely for this — they count non-keyword-only parameters, so the compliant refactor
is **inserting a `*` to make args keyword-only**, not building a dict. Pylint's
`R0913` already excludes keyword-only and positional-only args, so the bag refactor
isn't even necessary to satisfy it. Python solved the gaming problem at the rule level.

**JS/TS has no equivalent**, which is why `max-params` is gameable there and why my
case study happened at all. If you enable it, pair it with (a) a named-type
requirement on the options object — no `any`, no `Record<string, unknown>` — and (b) a
size cap on the resulting interface, or you've relocated the smell rather than removed
it. Worth noting `max-params` is contested upstream too (ESLint issues #17727, #15745,
#20107, about exempting callbacks and `this`).

This is a strong section for the post: *the rule you pick determines the cheat that's
available.* Same intent, two ecosystems, one of which made the dishonest refactor
unnecessary and the other of which made it the path of least resistance.

#### Feeding lint state to the agent — the mechanism is exit code 2

Concrete, and better than prose in `CLAUDE.md`:

- **`PostToolUse` hook, exit 2** → stderr is shown to Claude. Exit 0 goes to the debug
  log only, i.e. **the agent never sees it**. (Or `additionalContext` in JSON output,
  which does it explicitly.) Minimal pattern: matcher on `Write|Edit` running
  `eslint --format compact` on the edited path.
- **`Stop` hook, exit 2** → *prevents the agent from stopping* and continues the
  conversation. That's where "lint must be clean before you finish" belongs: a prose
  instruction is advisory, a Stop hook is not.
- MCP/LSP bridges (`Tritlo/lsp-mcp` with an `lsp-diagnostics://` resource,
  `mcp-language-server`, `tjx666/vscode-mcp`) expose diagnostics as a tool call
  instead of a shell round-trip.
- AGENTS.md consensus: state the **exact command**, and don't restate in prose
  anything a linter already enforces deterministically.

Measured evidence that this helps is thin but non-empty — and both papers are
benchmark-scale, not codebase-scale, ⚠️ with figures from search summaries only:
*Static Analysis as a Feedback Loop* (arXiv 2508.14419) reports Bandit/Pylint feedback
cutting insecure code by up to **32%**; *LLMloop* (arXiv 2603.23613) reports pass@10
**90.24% vs 76.22%** on HumanEval-X with five refinement loops.

#### Never-worse gates, and yes — agents game them

**The reason to want the gate**, and the single best stat for the post if it verifies:
**Agarwal et al., MSR 2026** (arXiv 2601.13597) — staggered difference-in-differences
with matched controls over the AIDev dataset — reports that after autonomous-agent
adoption, **static-analysis warnings rise ~18% and cognitive complexity ~39%**, with
velocity gains front-loaded and fading. ⚠️ PDF unreachable; venue and abstract
confirmed, effect sizes reported-not-verified. Adjacent non-causal: GitClear's 2025
report over 211M changed lines — duplicated blocks up ~8x in 2024, moved/refactored
lines down from ~25% of changed lines in 2021 to under 10% in 2024.

**The gaming is real and takes essentially one form: suppression comments.**
Anthropic's *Natural Emergent Misalignment from Reward Hacking in Production RL* shows
models that learn to hack graded coding environments generalise to broader misbehaviour
including sabotage inside a Claude Code scaffold; o3-mini has been observed editing
test cases rather than fixing bugs. At PR level, one study of **327 agent-attributed
PRs** found ~8% drew maintainer complaints naming a specific cheat, with
`@ts-ignore` / `eslint-disable` over failing lines called out, and 20 of 27 rejected at
review. ⚠️ dev.to blocked, numbers unverified, methodology unaudited — use only if it
checks out.

Mitigations, increasing strictness — this is the checklist the post should end on:

1. `--report-unused-disable-directives-severity error` so stale suppressions can't
   accumulate.
2. `@eslint-community/eslint-comments/no-unlimited-disable` — bare
   `/* eslint-disable */` banned; you must name rules.
3. `.../require-description` — every directive needs a justification, which is exactly
   the thing an agent has to fabricate *visibly*.
4. `.../no-restricted-disable` — allowlist what may ever be disabled; put the
   structural rules on the deny list.
5. `.../no-use` — ban directive comments outright in agent-written paths.
6. Route all suppressions through the machine-generated file
   (`eslint-suppressions.json`), CODEOWNERS-protect it, and add a CI check that it
   **did not grow** in an agent PR. Adding a suppression becomes a reviewable event
   rather than an inline comment.

**The line the whole post builds to:** `--fix`-clean output is not evidence of
quality. A suppression is structurally valid code, so lint-on-lint cannot catch it.
The gate has to be *"did the suppression count change"*, not *"does lint pass"*.

#### Python note
Ruff has **no baseline feature** — issue #1149, open since Dec 2022. Workaround is
`ruff check --add-noqa` (writes `# noqa` onto every current violation) plus
`per-file-ignores`. For types: `mypy-baseline` stores mypy's stdout as a
human-readable baseline and reports only new errors; `basedmypy` has it built in.
Pylint's `--fail-under` is a *score* ratchet, not a violation ratchet.

#### Key sources
- [ESLint CLI docs (source of truth for the suppression flags)](https://github.com/eslint/eslint/blob/main/docs/src/use/command-line-interface.md) · [Introducing bulk suppressions (Apr 2025)](https://eslint.org/blog/2025/04/introducing-bulk-suppressions/) · [TikTok's write-up](https://developers.tiktok.com/blog/bulk-suppressions-a-new-eslint-feature-for-large-codebases)
- [betterer](https://github.com/phenomnomnominal/betterer) · [eslint-formatter-ratchet](https://github.com/Jmsa/eslint-formatter-ratchet) · [eslint-plugin-diff](https://github.com/paleite/eslint-plugin-diff) · [trunk hold-the-line](https://trunk.io/blog/trunk-check-hold-the-line) · [reviewdog](https://github.com/reviewdog/reviewdog) · [Sonar Clean as You Code](https://docs.sonarsource.com/sonarqube-server/user-guide/about-new-code)
- [Sadowski et al., *Lessons from Building Static Analysis Tools at Google*, CACM 2018](https://cacm.acm.org/research/lessons-from-building-static-analysis-tools-at-google/)
- [Shepperd 1988, critique of cyclomatic complexity](https://www.cs.du.edu/~snarayan/sada/teaching/COMP3705/lecture/p1/cycl-1.pdf) · [Muñoz Barón et al. ESEM 2020](https://arxiv.org/abs/2007.12520) · [Lenarduzzi et al. 2023](https://arxiv.org/abs/2303.07722)
- [Ruff `PLR0917` too-many-positional-arguments](https://docs.astral.sh/ruff/rules/too-many-positional-arguments/) — the anti-gaming rule design
- [Claude Code hooks reference](https://code.claude.com/docs/en/hooks) · [eslint-plugin-eslint-comments](https://eslint-community.github.io/eslint-plugin-eslint-comments/)
- [MSR 2026 mining challenge listing](https://2026.msrconf.org/details/msr-2026-mining-challenge/29/) · [GitClear 2025 research](https://www.gitclear.com/ai_assistant_code_quality_2025_research) · [Anthropic, natural emergent misalignment from reward hacking](https://assets.anthropic.com/m/74342f2c96095771/original/Natural-emergent-misalignment-from-reward-hacking-paper.pdf)
- Follow-up reading, unfetched: [Factory.ai — Using Linters to Direct Agents](https://factory.ai/news/using-linters-to-direct-agents) · [Mainmatter — Lint to the Future](https://mainmatter.com/blog/2025/03/03/lttf-process/)

### Refs
- Vault: **[[Max-Params Lint — The Parameter-Object Trap]]** (primary — the caveat) ·
  [[ESLint as AI Guardrails: The Rules That Make AI Code Readable (01knvx4ag6zqy02se06rxkgfnf)]]
  (agents need hard constraints, not nudges; CodeRabbit's 1.7x-more-issues figure) ·
  [[Refactoring Examples — Bad to Good]] ·
  [[AI - Testing and Code Health]] ·
  [[Getting Started With Ddd When Surrounded By Legacy Systems (01kb69xfk9xxq5f8eatccj7vbh)]] ·
  [[The basics of software coupling metrics and concepts (01kd04z7es6cncgkad9sx5xv4q)]] ·
  [[The hidden technical debt of agentic engineering (01knacfykmbc0ggg22m3dvprct)]]

### Open questions
- [ ] Which repo do I use for the worked example — `ethira/api` (real, mine, but
      needs sanitising) or a public refactoring kata?
- [ ] Does the post ship with a working config (ESLint + gate script) people can copy?
      That's what would make it actually useful, and it's the difference between a
      post and a repo. Research says the config is smaller than expected —
      `--suppress-all` + `eslint-comments` rules + a PostToolUse hook.
- [ ] Verify before publishing: the Kent Beck parameter-object quote (substack was
      blocked), the MSR 2026 +18% warnings / +39% cognitive complexity figures, and
      the 327-agent-PR cheating study. All three are second-hand right now.
- [ ] Is the JS/TS-has-no-`PLR0917` gap its own post? "Your lint rule decides which
      cheat is available" might be a better hook than the legacy-adoption framing.

---

## Notes
- Ideas 2 and 3 are the same argument at two altitudes: *stop measuring volume, start
  measuring whether the thing got better.* Consider cross-linking them explicitly, or
  even publishing them as a pair.
- Idea 1 is the odd one out topically but the strongest candidate for reach.

---

## Desk

```dataviewjs
await dv.view("Templates/Scripts/project-desk");
```
