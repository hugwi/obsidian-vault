---
title: "Measuring What Matters with Jules- Google Developers Blog"
source: "https://developers.googleblog.com/en/measuring-what-matters-with-jules/?utm_source=chatgpt.com"
author:
  - "[[Nghi Bui]]"
  - "[[Georgios Evangelopoulos]]"
  - "[[Zack Elliott]]"
published: 2026-06-22
created: 2026-09-07
description: "AI coding agents are rapidly shifting from reactive assistants that complete tasks when prompted to ..."
tags:
  - "raw"
---
## Measuring What Matters with Jules

[Nghi Bui](https://developers.googleblog.com/en/search/?author=Nghi+Bui) Research Scientist

[Georgios Evangelopoulos](https://developers.googleblog.com/en/search/?author=Georgios+Evangelopoulos) Research Scientist

[Zack Elliott](https://developers.googleblog.com/en/search/?author=Zack+Elliott) Software Engineer

![Measuring What Matters with Jules 1.0](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/Measuring_What_Matters_with_Jules_1.0.original.png)

AI coding agents are rapidly shifting from reactive assistants that complete tasks when prompted to proactive engines that continuously absorb context, spot emerging risks, and surface diagnostic insights before developers have to ask. At the center of this evolution is a shift from well-defined ***tasks*** to ***goals***, which require the agent to explore the codebase, discover what is relevant, and surface diagnostic observations that help guide developers toward a higher-level objective.

Public benchmarks like SWE-Bench test an agent’s ability to complete tasks, like fixing a narrowly defined bug, but no benchmarks currently exist for goals. In our most recent paper, [*Agentic Coding Needs Proactivity, Not Just Autonomy*](https://arxiv.org/abs/2605.06717), we argue that proactive agents must be graded on their insight policy—the ability to decide what matters, what evidence supports it, and whether to interrupt the developer or stay silent.

![overview-abstract](https://storage.googleapis.com/gweb-developer-goog-blog-assets/images/overview-abstract.original.png)

The Figure above shows the design of a proactive agentic coding engine. Context streams into an engine that maintains development state and a developer model, emits insights (notify, question, draft, stay silent), and learns from response.

## Leveraging real bug fixes as “ground truth”

Based on our work on continuous AI systems at Google Labs, we’ve found that building evaluations capable of grading a proactive agent on its insight policy requires establishing a “ground truth.” One way to build this “ground truth” is to analyze a team’s real bug-fixing history along two heuristics we term **temporal proximity** and **semantic similarity**.

Our hypothesis is simple: when engineers file and fix several related bugs within a short time period, those bugs are often symptoms of a single underlying engineering effort. A cluster of bugs around "sandbox timeout errors," "broker config failures," and "network isolation flaky tests" all point toward a common aspirational goal like *"Strengthen sandbox execution reliability."* Individually, each bug is too task-specific to serve as a goal. Together, they reveal the higher-level objective.

## Building and testing our preliminary eval set

To build our preliminary benchmark and test our hypothesis, we used 705 bugs (1,178 CLs) from internal Google codebases to:

- Cluster related historical bugs to reveal the higher-level "aspirational goals" developers were actually working toward.
- Set the individual bugs within each cluster as our "ground truth" targets and reverted the codebase to its exact pre-fix state so the agent began where the human engineer did.
- Allow the agent to investigate the codebase for up to three rounds (its "exploration budget," or N) before generating its final insights.
- Use an LLM to judge the agent’s predicted insights from 1 (irrelevant) to 5 (exact match) against our “ground truth” targets.
- Measure success by tracking the agent's average top score and how often it successfully produced a highly accurate match (Hit@K).

## Preliminary results and what we learned

The preliminary results of our testing are exciting for two primary reasons.

**The core diagnostic logic works:** Given a single exploration round, the agent consistently identified a highly relevant insight (averaging 4.5 out of 5). It successfully captured the primary signal for straightforward engineering problems.

**Exploration budgets matter:** Complex, multi-faceted problems are naturally harder, but giving the agent more resources to investigate pays off. By increasing the exploration budget from two rounds to three, the agent’s **Hit@5 accuracy** (defined as the rate at which a correct diagnostic insight appears within its top 5 recommendations) rebounded significantly from 33% to 57%. This proves that extra passes directly help the agent uncover secondary signals it initially missed.

## What’s next

These are preliminary results on an initial sample, and we are actively expanding coverage on multiple fronts. To start, we are expanding this evaluation to public GitHub data (issues and resolving PRs) to make this methodology broadly applicable to the wider AI community. We are also exploring how to ingest richer context streams like issue trackers, conversations, and design documents beyond just the codebase.

Read the full paper [here](https://arxiv.org/pdf/2605.06717) and follow along with us at [labs.google/code](http://labs.google/code) if you’re interested in learning more about our work on the future of coding at Google Labs.