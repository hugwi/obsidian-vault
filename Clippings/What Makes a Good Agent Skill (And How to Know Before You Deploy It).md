---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - efficiency
  - evals
  - skills
source: readwise
created: 2026-06-23
rating: 
action: 
theme: quality-gates
subtheme:
  - evals
  - code-review-gates
  - verification-loops
---

# What Makes a Good Agent Skill (And How to Know Before You Deploy It)

![rw-book-cover](https://cdn.sanity.io/images/hfpt3gww/production/c264e66ba8d46a00cfbc251d200985d719a7a1b6-1195x626.png?rect=0,1,1195,624&w=1200&h=627&fit=crop&auto=format)

## Metadata
- Author: [[sundae_bar]]
- Full Title: What Makes a Good Agent Skill (And How to Know Before You Deploy It)
- Category: #articles
- Summary: There are many agent skills available, but most are untested and may not improve performance. A good skill helps the agent complete tasks well, works with different inputs, uses few tokens, and applies broadly. Evaluating skills with real tests is essential to ensure quality before using them in important work.
- URL: https://www.sundaebar.ai/news/what-makes-a-good-agent-skill-and-how-to-know-before-you-deploy-it

## Full Document
![](https://www.sundaebar.ai/_next/image?url=https%3A%2F%2Fcdn.sanity.io%2Fimages%2Fhfpt3gww%2Fproduction%2Fc264e66ba8d46a00cfbc251d200985d719a7a1b6-1195x626.png%3Fw%3D1400%26fit%3Dmax%26auto%3Dformat&w=3840&q=100)
#### What Makes a Good Agent Skill (And How to Know Before You Deploy It)

There are over 800,000 agent skills indexed across public marketplaces right now. The number doubled in the last three months. Most of them have never been evaluated against a real task.

The [SKILL.md standard](https://agentskills.io/specification) made it trivially easy to write skills. That was the point. Anthropic released it as an open specification in December 2025, [OpenAI adopted it for Codex](https://developers.openai.com/codex/skills), Google integrated it into [ADK's SkillToolset](https://developers.googleblog.com/developers-guide-to-building-adk-agents-with-skills/), and now over 26 platforms support the same format. Distribution scaled fast. Quality assurance did not.

**This article is about what separates a skill that works from one that just looks like it should.**

![Post Image](https://cdn.sanity.io/images/hfpt3gww/production/357780b19a1e608a03fd8902d1a3801f0c0a6697-1189x622.png?w=3840&h=2009&q=100&fit=max&auto=format&dpr=2)Post Image
#### The quality signal problem

The primary quality signal in most skill marketplaces is GitHub star count. SkillsMP filters out repositories with fewer than two stars. LobeHub shows popularity metrics. A recent [KDnuggets roundup of the top five marketplaces](https://www.kdnuggets.com/top-5-agent-skill-marketplaces-for-building-powerful-ai-agents) describes platforms indexing hundreds of thousands of skills with discovery features, category tags, and install commands.

None of these tell you whether the skill actually improves the agent's output.

A [large-scale analysis of over 42,000 agent skills](https://arxiv.org/abs/2601.10338) found that 26.1% contained at least one security vulnerability. Of those, 5.2% exhibited high-severity patterns strongly suggesting malicious intent. That is the security floor of the problem. The bigger issue is the vast middle: skills that are syntactically correct, well-described, and completely untested against the kind of work they claim to support.

Star counts measure awareness. They do not measure performance. And for enterprise use cases, where an agent skill is supposed to handle expense policy, vendor evaluation, or client onboarding, deploying on the basis of awareness is a real risk.

![Post Image](https://cdn.sanity.io/images/hfpt3gww/production/c18c8dd292577d303706bfc751ade339276ce08b-1165x625.png?w=3840&h=2060&q=100&fit=max&auto=format&dpr=2)Post Image
#### What "good" actually means

A good agent skill does four things. They are not complicated, but they are rarely measured.

**It improves task completion over the baseline.** The most basic question: does the agent perform the task better with this skill than without it? This requires running the same prompt with and without the skill and comparing outputs against a known correct answer. The [agentskills.io evaluation guide](https://agentskills.io/skill-creation/evaluating-skills) describes this workflow in detail. If a skill does not demonstrably improve the result, it is overhead.

**It holds up under varied inputs.** A skill that works on the demo prompt but breaks on a slightly different version of the same task is fragile. Enterprise work is full of edge cases: unusual formatting, conflicting data, missing fields, ambiguous instructions. A good skill handles variation without hallucinating or silently dropping constraints.

**It is token-efficient.** Skills sit in the agent's context. They consume tokens at load time and influence the reasoning budget available for the actual task. A skill that is 8,000 tokens of exhaustive instructions might produce the same result as one that is 1,200 tokens of focused guidance. The leaner skill leaves more room for the agent to think. The SKILL.md specification [recommends keeping instructions under 5,000 tokens](https://agentskills.io/specification) for this reason. Token efficiency is not an optimization detail. It is a design quality.

**It generalizes beyond the training data.** This is the hardest criterion and the one most skills fail on. A skill built against a single company's policies will encode assumptions that break when applied to a different company. A skill built against a fixed dataset will perform well on that data and poorly on anything new. The skill needs to teach the agent *how* to approach a category of work, not memorize the answers to specific instances of it.

![Post Image](https://cdn.sanity.io/images/hfpt3gww/production/d421a7ade63a505675457753598322f542009a52-1172x616.png?w=3840&h=2018&q=100&fit=max&auto=format&dpr=2)Post Image
#### Where most skills fail

The dominant failure mode is not malice or incompetence. It is overfitting.

In our evaluation challenges on [SN121](https://sundaebar.ai/lab), we have observed this pattern repeatedly. Developers build agent configurations that score well on a known test suite by embedding specific answers, named employees, dollar thresholds, and policy details directly into the agent's instructions. The configuration scores high. Then we rotate the content, change the company, alter the thresholds, and the same configuration falls apart.

This is not unique to our challenge environment. It is the same dynamic playing out in the broader skills ecosystem. A skill that says "for expenses over $5,000, route to the CFO" is not teaching the agent how to handle expense routing. It is teaching it one company's specific rule. Deploy that skill at a different company and it confidently applies the wrong policy.

The skills that perform well under content rotation are the ones that teach retrieval and reasoning patterns. "Check the policy document for the relevant threshold" is harder to write than "the threshold is $5,000" but it actually transfers.

#### Evaluation is not optional

The SKILL.md specification includes a [built-in evaluation framework](https://agentskills.io/skill-creation/evaluating-skills). Google's ADK SkillToolset supports evaluation workflows. Anthropic's own engineering team has written about [the importance of structured evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents). The infrastructure for evaluating skills exists.

The marketplace layer has not caught up. Skills are published without evaluation results. Users install them on trust. And the feedback loop that would improve skill quality over time does not close, because there is no structured signal flowing back from real-world performance to the skill creator.

What evaluation-backed quality looks like in practice:

A skill is tested against a set of tasks that represent its claimed capability. The tasks include easy cases (baseline confirmation), medium cases (realistic complexity), and hard cases (edge conditions, conflicting information, multi-step reasoning). Each task has a known correct output and a rubric that weights different quality dimensions: accuracy, constraint adherence, format compliance, appropriate handling of ambiguity.

The skill's impact is measured as the delta between with-skill and without-skill performance across the full task set. If the delta is negative on hard cases, the skill is actually making the agent worse when things get complicated. That is a common finding and one that star counts will never surface.

#### Enterprise skills are a different category

Most of the skills ecosystem is oriented toward coding agents. Skills for Claude Code, Codex CLI, and similar tools. These are valuable, but they operate in a domain where the agent has concrete, verifiable feedback loops: does the code run? Does the test pass?

Enterprise agent skills operate in a domain where feedback is ambiguous. Did the agent apply the right policy? Was the escalation decision appropriate? Did it correctly synthesize information from three different source documents?

Evaluating enterprise skills requires test design that mirrors real business complexity. The task is not "write a function that sorts an array." The task is "a contractor in the APAC region wants to expense a client dinner that includes alcohol, paid on a personal card, submitted 45 days after the event, during a budget freeze, for a client with a pending contract dispute." The skill needs to guide the agent through retrieving the right policies, identifying the relevant constraints, and producing a decision that accounts for all of them.

This is the category of skill evaluation that we are building at [sundae\_bar](https://sundaebar.ai/). Our [Agent Evaluation Test Suite](https://sundaebar.ai/lab) runs agents through enterprise scenarios across finance, operations, HR, support, and legal domains. The tests are public. The rubrics are public. The results are measurable and comparable.

We are now extending this evaluation infrastructure to individual skills. Instead of evaluating a complete agent configuration, we evaluate discrete skill contributions: does this skill improve the agent's performance on the tasks it claims to support?

#### What comes next

The skills ecosystem will consolidate around quality. The current phase of unbounded growth is necessary but temporary. As enterprises start deploying agent skills in production, the question shifts from "does a skill for this exist?" to "which skill for this actually works, and how do I know?"

The platforms that answer that question with data will win. The ones that answer it with star counts will not.

We are publishing our skill evaluation methodology openly so that anyone building skills or building marketplaces can use it. Not because openness is virtuous in the abstract, but because evaluation infrastructure is more useful when it is shared. A skill rated on one platform should be comparable to the same skill rated on another.

The standard is not settled. But the direction is clear: agent skills need evaluation the same way software packages need tests. Not every skill needs the same rigor. But the default should be "tested" rather than "published."

That is what we are building toward.
