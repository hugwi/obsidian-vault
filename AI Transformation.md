---
categories:
  - "[[Projects]]"
project: "[[AI Slides]]"
created: 2026-06-23
---

# TODO 
- Move slide 11 to appendix after creating an graveyeard slide (it's own slide)
-  Three streams. _This chapter: Agentic Engineering._ slide 10 Can also be moved to graveyeard
- slide 12  ## Reimagining the SDLC across _six surfaces_. -> can be moved after 4
- slide 9 feels a bit out of context. Either it should be in the beginning after the Reimagining the SDLC across _six surfaces_ or I think it should be closes to the method. But method could vary I think
-  Where you sit. _Where you start._  -> Should rather be, where we understand that you're today. 
- After that we should have the three stream saying something that in general these are what Netlight support with and the different stream 
	- Then in the same slide show -> What we understand you want to to focus. I'm not sure what would trigger this flow, let's talk about it. It should be highligted as a selection though so it's clear what we'll focus on 
## Success KPIs

I want at slide 16 "how we measure success" have a arrow points to the right, saying
   why me measure sucess like this. It should be very clear that you can click here to
   learn more and it should be a pulsing arrow so you can miss it. When you click on
  that one you get into a deep dive where you can drill deaper each time you press
  right. And anytime there is an arrow point down to escape the deep dive.

  On the deep dive I want to communicate with a 3d graph the problem. First start with
   a 2d graph with customer churn and user story points with the narrative that user
  story increases which might lead to the false conclusion that the ai transformation
  is a success. Then I want to add on the 2nd axis, customer churn and say that in the
   beginning the customer churn is stable and it doesn't show any correlation, but all
   of a sudden it drops and ask why? Then add the 3d dimension that is the number of
  bugs and show that after the double increase user story points they started to have
  increasingly bugs with lead to customer churn and this is the risk of using to few
  KPIs. Say that you wnat to follow the term MECE mutually exclusive collectively
  exhaustive

After that I want to show how DORA attempts to be a better metrics and also show how you can compute a DORA metrics to use the metrics together to arrive at what a good value is and the ability to change any number of the KPIs and see how that change the overall performance, for instance increasing the change failure rate. Here you can also show what are number for high performance team, avergage etc. But you should mention that these numbers needs to be adjusted for AI. 

After that highlight that DORA is a good start but if you want to measure long term success you need to involve metircs tied to your long term business goals. 
For instance show that DORA metrics on one axis, shitty product on one axis and recurring customer on the third and show that although your DORA metrics is skyrocketing if you have a shitty product the recurring customer won't grow. 

A good way of measuring success could be recurring customers, but if you measure for team, could for instance be feature adoption or similar. 

---

## Drive adoption 

Three categories of users 

- The skeptics 
- The average users - Use ai for coding, but don't actively work on imporving skill, rules, claude.md, not doing automations with AI ie automatic code reviews, easy bug fixing, parallell work, monitoring code quality and setting up guard rails
- The core users - actively work on imporving skill, rules, claude.md, not doing automations with AI ie automatic code reviews, easy bug fixing, parallell work, monitoring code quality and setting up guard rails. But haven't done the full harness. 

In order to drive AI transformations the success comes from targeting all of these three groups and they need different ways to target. 

I want to show the performance gain that you can have and with some kind of bar chart showcase that the total performacne gain is the amount of people in each group times the performacne increase in each group. 

For instance you might be able to increase the performance gain for the skeptics with 80% since they're not using it at all. average users 50% and only 30% for the core users. If the most people are in the average users, that make the most impact. 

---  

## Modules 

When we do AI transformations 


https://www.mckinsey.com/capabilities/mckinsey-technology/our-insights/building-the-foundations-for-agentic-ai-at-scale

![](https://www.mckinsey.com/~/media/mckinsey/business%20functions/technology/our%20insights/building%20the%20foundations%20for%20agentic%20ai%20at%20scale/agenticfoundations_ex1.svgz?cq=50&cpy=Center)

![](https://www.mckinsey.com/~/media/mckinsey/business%20functions/technology/our%20insights/building%20the%20foundations%20for%20agentic%20ai%20at%20scale/agenticfoundations_ex3-center-large.svgz?cq=50&cpy=Center)

i
https://www.youtube.com/watch?v=VMemhtlsoNk&list=WL&index=7
New scrum
![[Pasted image 20260516211319.png]]


![[Pasted image 20260516211440.png]]

![[Pasted image 20260516211513.png]]


# Agentic Harness 
![[Pasted image 20260516211626.png]]

![[Pasted image 20260516211815.png]]

![[Pasted image 20260516211843.png]]

![[Pasted image 20260516211914.png]]

![[Pasted image 20260516211950.png]]

https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality

Agents lack a reliable understanding of maintainability and change risk inside a real codebase. In practice, this means agents operate with incomplete context:

- **AI operates in a self-harm mode,** often writing code it cannot reliably maintain later.
- **[AI needs healthy code to reduce the defect risk](https://codescene.com/hubfs/whitepapers/AI-Ready-Code-How-Code-Health-Determines-AI-Performance.pdf),** yet will happily comply and start modifying any spaghetti mess, no matter how unlikely to result in functionally correct code.
- **Agents cannot verify their improvements.**  After a refactoring attempt, is the code objectively better or just a different arrangement of accidental complexity?

These problems share a common root cause. AI lacks an objective way of measuring “good”. The following patterns provide that missing context and turn agentic speed into reliable outcomes.


## Operational Patterns for Reliable Agentic Coding

When agents gain visibility into code quality, maintainability and change risk, their behavior shifts. The patterns below capture how that feedback is operationalized. The bulk of them are productified and implemented in our [Code Health MCP server,](https://github.com/codescene-oss/codescene-mcp-server) which we use ourselves as a mandatory requirement for agentic AI.

Together, the Code Health score, MCP safeguards, and AGENTS.md form the infrastructure layer behind these patterns. Code Health provides objective signals about maintainability and risk. MCP exposes those signals as actionable tools. [AGENTS.md](https://github.com/codescene-oss/codescene-mcp-server/blob/main/AGENTS.md) encodes how the tools are combined into predictable workflows. The result is: abstract engineering principles turn into executable guidance that agents can follow consistently.

[Want to know more about Code Health? It’s not just a concept, but the metric underpinning our AI tools and safeguards. Read all about it here.](https://codescene.io/docs/guides/technical/code-health.html#code-health-identifies-factors-known-to-impact-maintenance-costs-and-delivery-risks)

## 1. Pull Risk Forward: Assess AI Readiness

**Problem**Code lacking in quality isn’t AI-ready. Low Code Health increases the likelihood that agents fail on their task or, at best, burn excess tokens.

**Context**We know from [](https://arxiv.org/pdf/2601.02200) [peer-reviewed research](https://arxiv.org/pdf/2601.02200) that AI performs best in healthy code; agents get confused by the same patterns as humans. As evident from the following graph, you want to aim for a Code Health of at least 9.5, ideally a perfect 10.0.

![The non-linear relationship between Code Health and business value.-2](https://codescene.com/hubfs/The%20non-linear%20relationship%20between%20Code%20Health%20and%20business%20value.-2.svg)![AI-Friendly-Code_Chart](https://codescene.com/hs-fs/hubfs/AI-Friendly-Code_Chart.png?width=734&height=474&name=AI-Friendly-Code_Chart.png)_TL;DR lower code health → worse AI performance_

![[Pasted image 20260516220425.png]]


https://codescene.com/blog/strengthening-the-inner-developer-loop-turn-ai-into-a-reliable-engineering-partner

## Know the AI pitfalls 

Acceleration isn’t useful if it’s driving our projects straight into a brick wall of technical debt. Naively used, these promising AI agents will serve more as legacy code generators than genuine help unless we introduce proper guardrails. There’s now clear evidence to make any AI adoption  a serious concern:

- **More bugs**: Up to [41% more defects](https://resources.uplevelteam.com/gen-ai-for-coding) without any increase in throughput. (Someone’s getting fired).
- **Initial AI velocity gains are cancelled out:** Novel research demonstrates how the initial promising velocity gains from AI adoption are [fully cancelled out](https://arxiv.org/pdf/2511.04427) after just two months. The reason? A massive increase in code complexity.
- **AI makes you slower:** This is a fascinating one: developers self-estimated that their AI reduced completion time by 20%, whereas in reality [they needed 19% longer](https://arxiv.org/abs/2507.09089) (!) than a control group of devs without AI.

Given these damaging facts, why are people still claiming productivity gains? Most likely because not all code is equal. Our research at CodeScene shows this clearly: Code Health acts as a protective buffer. Healthy code reduces error-generation risk and gives AI the structural clarity it needs to act predictably. Really, this is important, so let me rephrase it: the same suboptimal coding decisions that confuse human programmers also confuse an AI.

Unfortunately, as shown by the findings above, AI often operates in self-harm mode; it writes checks its future self cannot cash. AI generates code that is inherently incompatible with, well, AI. A strange paradox indeed.

## Avoid the pitfalls: AI-acceleration without the risks

This is where the inner developer loop comes in. Instead of letting AI agents spray code like an overconfident intern, we put them into a guided, objective feedback cycle. The loop keeps quality high, complexity low, and future engineers un-traumatized.


--- 
## Enabling AI-friendly code - How it works 

![Inner Feedback Loop_deploying-AI-generated-that-is-safe](https://codescene.com/hs-fs/hubfs/Inner%20Feedback%20Loop_deploying-AI-generated-that-is-safe.png?width=500&height=500&name=Inner%20Feedback%20Loop_deploying-AI-generated-that-is-safe.png)

### Step 1: AI generates code, but guided by Code Health aware context

The agent starts with knowledge of what parts of the codebase are healthy, which are risky, and where complexity already hurts. Note that a key step here is to codify the rules, scenarios, and goals for agents. For the MCP, we do that using an [AGENTS.md file](https://github.com/codescene-oss/codescene-mcp-server/blob/main/AGENTS.md). (Think of this file as a contract for your AI).

### Step 2: The code is evaluated before it becomes your problem

Every change gets checked against objective Code Health signals: maintainability, complexity, hotspots, and [existing technical-debt goals](https://codescene.com/blog/how-to-manage-technical-debt-with-auto-supervised-goals-read-more). If the change increases risk, the loop doesn’t stop; rather it feeds the insights back to the agent for self-improvement.

### Step 3: The agent refactors based on objective metrics

The agent acts on the feedback from CodeScene’s MCP. For example, the AI might simplify the structure of the code, reduce nesting depth, or start to modularize overly complex classes while ensuring that all tests still pass. In short, the AI agent learns to behave like a responsible engineer.

### Step 4: The improvements are validated 

The updated code is reassessed. If the Code Health  improved, great. If not, the loop continues automatically until the change is safe, understandable, and ready for human review.

### Step 5: Enjoy the free lunch - speed with quality

By the time the AI agent completes its goals, the resulting code change is simpler to review, and future proof in the sense that change is easy. This means you and your team stay productive way beyond the initial AI boost.--- 

https://codescene.com/blog/agentic-ai-coding-best-practice-patterns-for-speed-with-quality
## 1. Pull Risk Forward: Assess AI Readiness

**Problem**Code lacking in quality isn’t AI-ready. Low Code Health increases the likelihood that agents fail on their task or, at best, burn excess tokens.

**Context**We know from [](https://arxiv.org/pdf/2601.02200) [peer-reviewed research](https://arxiv.org/pdf/2601.02200) that AI performs best in healthy code; agents get confused by the same patterns as humans. As evident from the following graph, you want to aim for a Code Health of at least 9.5, ideally a perfect 10.0.

![[Pasted image 20260516221518.png]]