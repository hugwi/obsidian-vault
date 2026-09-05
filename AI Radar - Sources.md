---
created: 2026-09-05
categories:
  - "[[Projects]]"
project: "[[AI Radar]]"
domain: engineering
tags:
  - ai-radar
  - sources
  - monitoring
---

# AI Radar - Sources

This is the watchlist for [[AI Radar]]. `enabled: true` means a collector may fetch the source. The first version should prefer public pages, RSS, Atom, release feeds, and official APIs where available.

## Source registry

| Enabled | Source | Type | URL | Topics | Cadence | Notes |
|---|---|---|---|---|---|---|
| true | OpenAI News | official-news | https://openai.com/news/ | models, products, agents | daily | Primary announcements |
| true | Anthropic News | official-news | https://www.anthropic.com/news | models, safety, agents | daily | Primary announcements |
| true | Google DeepMind Blog | official-blog | https://deepmind.google/discover/blog/ | research, models, robotics | daily | Research and releases |
| true | Meta AI Blog | official-blog | https://ai.meta.com/blog/ | open models, research, products | daily | Primary announcements |
| true | Hugging Face Blog | ecosystem-blog | https://huggingface.co/blog | open source, tooling, models | daily | Practical ecosystem signals |
| true | GitHub Trending | code-discovery | https://github.com/trending | open source, tools, agents | daily | Adoption proxy; filter for AI |
| true | arXiv cs.AI | papers | https://arxiv.org/list/cs.AI/recent | agents, reasoning, AI systems | daily | Discovery only; validate important papers |
| true | arXiv cs.LG | papers | https://arxiv.org/list/cs.LG/recent | training, inference, ML | daily | Discovery only; validate important papers |
| true | Papers with Code | research-index | https://paperswithcode.com/ | benchmarks, models, research | daily | Compare claims with benchmarks |
| true | Product Hunt AI | product-discovery | https://www.producthunt.com/topics/artificial-intelligence | products, workflows, startups | daily | Weak signal; use for discovery |
| false | X expert list | x |  | practitioners, launches, experiments | hourly | Add handles after deciding whose signal is trusted |
| false | YouTube expert list | youtube |  | demos, tutorials, analysis | daily | Add channels after deciding which formats are useful |
| false | AI newsletters | newsletter |  | synthesis, products, funding | daily | Add RSS/email sources individually |
| false | AI podcasts | podcast |  | research, founders, applications | weekly | Transcribe only episodes likely to contain signal |
| false | Company changelogs | changelog |  | product capability changes | daily | Add only tools relevant to current work |

## Topic vocabulary

- `agents`
- `models`
- `open-source`
- `inference`
- `reasoning`
- `coding`
- `multimodal`
- `robotics`
- `research`
- `product`
- `startup`
- `workflow`
- `safety`

## Source properties

When this becomes machine-readable, each row should map to:

```yaml
name: OpenAI News
enabled: true
type: official-news
url: https://openai.com/news/
topics: [models, products, agents]
cadence: daily
priority: 1
collector: web | rss | youtube | x | manual
```

`priority` is an editorial trust/discovery setting, not a trend score. Trend scoring happens after capture and must consider evidence from multiple sources.

## Operating rules

- Start with the eight enabled public sources that have the clearest acquisition path.
- Treat official sources as primary evidence, not automatically as proof of importance.
- Treat X, YouTube, newsletters, and Product Hunt primarily as discovery surfaces until corroborated.
- Keep source items in `Raw/`; do not summarize them into this registry.
- Disable a source when it produces noise, duplicates, inaccessible content, or too many low-value items.

## Next actions

- [ ] Confirm the first collector target
- [ ] Add RSS/Atom URLs where available
- [ ] Add a small trusted X list
- [ ] Add a small trusted YouTube list
- [ ] Define maximum daily capture volume per source

## Related

- [[AI Radar]]
- [[Raw]]
