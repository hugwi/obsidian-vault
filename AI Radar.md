---
categories:
  - "[[Projects]]"
project: "[[AI Radar]]"
status: active
domain: engineering
outcome: Established a Markdown-first personal feed that surfaces and ranks emerging AI trends.
due:
created: 2026-09-05
tags:
  - project
  - ai-radar
  - trend-monitoring
---

# AI Radar

## Outcome

Build a personal feed that gathers AI developments from selected sources and turns them into a small, controllable review queue.

**Done when:**
- [ ] A source registry controls what is watched
- [ ] A local collector writes idempotent notes into `Raw/`
- [ ] Analysis produces observations, signals, and trend hypotheses
- [ ] A daily feed contains a finite number of ranked items
- [ ] Feedback can tune future ranking

## Domain model

- **Source** — a configured place or person to watch, such as an X account, YouTube channel, RSS feed, paper index, or product changelog.
- **Observation** — one captured source item in `Raw/`; it records what was published and where it came from.
- **Signal** — an observation or group of observations that indicates something worth watching.
- **Trend hypothesis** — a provisional explanation of a repeated or accelerating signal. It must show evidence and confidence.
- **Trend** — a validated pattern that remains useful over time and has a clear implication for my work.
- **Feed item** — a selected observation, signal, or trend hypothesis presented for review.
- **Feedback** — my response to a feed item: relevant, irrelevant, watch, investigate, implement, or ignored.

## Markdown-first architecture

```text
AI Radar - Sources.md
        |
        v
local collector
        |
        v
Raw/*.md  --->  analysis  --->  AI Radar - Today.md
                              |
                              v
                         trend notes
```

Markdown is the source of truth. Local scripts may maintain indexes or caches, but they must be rebuildable from the notes. There is no API or database in the first slice.

## Raw capture contract

Every collected source item should preserve:

```yaml
categories:
  - "[[Raw]]"
source_url: https://example.com/item
source_id: stable-source-specific-id
source_type: x | youtube | rss | paper | changelog | web
author: name-or-channel
published: 2026-09-05
captured: 2026-09-05
extraction_status: pending | complete | failed
rating:
action: review
```

The filename must be deterministic enough that collecting the same item twice updates or skips the existing note instead of creating a duplicate.

## Vertical slices

| Slice | Checkpoint | Scope | Verification | Depends on |
|---|---|---|---|---|
| 1. Source registry and manual feed | Edit a source list and generate a feed from existing Raw notes | `AI Radar - Sources.md`, `AI Radar - Today.md`, one local script | Run the script twice; same inputs produce no duplicates and a finite feed | - |
| 2. One public collector | A selected public source creates valid Raw notes | One collector, Raw writer, tests | Fixture test validates frontmatter, safe filenames, and idempotency | 1 |
| 3. Observation analysis | Raw notes become linked observations/signals with evidence | Analysis script and note templates | Fixture set produces stable links and preserves source URLs | 2 |
| 4. Feedback loop | Feed decisions are recorded and ranking changes | Feed properties/script | A labelled fixture changes ordering predictably | 3 |

## Next actions

- [ ] Create `AI Radar - Sources.md` with 10–20 initial sources and topic tags
- [ ] Choose one low-friction public source for the first collector
- [ ] Define the exact `AI Radar - Today.md` feed format
- [ ] Build the idempotent Raw writer and fixture tests
- [ ] Decide where the collector is scheduled locally

## Boundaries

- Do not add an API or database before the Markdown workflow proves useful.
- Do not rely on authenticated X/YouTube acquisition until access, rate limits, credentials, and terms are checked.
- Keep external source notes in `Raw/`; rewrite into a root note only when it becomes my own analysis.

## Desk

```dataviewjs
await dv.view("Templates/Scripts/project-desk");
```
