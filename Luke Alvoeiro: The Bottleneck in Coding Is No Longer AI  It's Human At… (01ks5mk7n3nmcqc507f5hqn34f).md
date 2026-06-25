---
categories:
  - "[[Resources]]"
domain: engineering
title: "Luke Alvoeiro: The Bottleneck in Coding Is No Longer AI — It''s Human Attention"
source: "https://finance.biggo.com/news/9ef5dbb40c870730"
author: "BigGo Finance"
published: 2026-05-06
created: 2026-05-21
description: "Factory's Luke Alvoeiro argues that multi-agent systems structured as long-running"
tags:
  - to-process
  - orchestration
---

![Luke Alvoeiro: The Bottleneck in Coding Is No Longer AI — It's Human Attention](https://img.biggo.com/USDW--ugCq96zLfYMt7udF2GsiBBKo1LIsGIZWzBSOo/fit/1720/0/sm/1/aHR0cHM6Ly9pbWcuYmdvLm9uZS9uZXdzLWltYWdlL2FpX2dlbmVyYXRlZC8yMDI2LTA1LzllZjVkYmI0MGM4NzA3MzBfMTc3ODA4OTQ3Nl9jb3Zlci5qcGc.jpg)
### The Attention Bottleneck


"The bottleneck in software engineering nowadays is not intelligence. It's now limited by human attention."


Luke Alvoeiro, speaking on the AI Engineer podcast, articulated a shift that upends the conventional wisdom of the AI coding race. For the past two years, the metric to watch was benchmark scores — which model can write cleaner code, fix more bugs, explain a complex function faster. But Alvoeiro, who created the open-source coding agent Goose at Block and now leads core agent infrastructure at enterprise AI company Factory, argues that model capability has already crossed the threshold required for practical work. The real constraint today is that even the best human engineer can only keep three or four threads of work active simultaneously.


Meanwhile, a cohort of large language models can reason across dozens of tasks concurrently — if someone can orchestrate them.


That orchestration is precisely what Factory's Missions system was built to deliver. Missions allows a team to increase its concurrent workstreams from roughly 10 to 30, not by hiring more engineers but by shifting human attention from execution to architecture and product decisions. The human defines *what* to build; the multi-agent system figures out *how*.


![](https://img.bgo.one/news-image/ai_generated/2026-05/9ef5dbb40c870730_1778089538_inline_1.jpg)
### A Taxonomy of Multi-Agent Patterns


Before explaining how Missions works, Alvoeiro cut through the proliferating taxonomy of multi-agent frameworks. He identified five fundamental patterns:




| Pattern | Description | Risk or Trade-off |
| --- | --- | --- |
| Delegation | A parent agent spawns a child agent for a subtask and receives a response | Simplest form; widely used in sub-agent coding tools |
| Creator-verifier | One agent builds, a separate agent checks the work with fresh context | Mirrors human code review; critical for catching errors |
| Direct communication | Agents message each other without a central coordinator | State fragments across conversations; no single source of truth |
| Negotiation | Agents communicate over a shared resource (API, code region) adversarially or cooperatively | Best when net positive-sum trades exist |
| Broadcast | One agent sends status updates, new context, or constraints to all others | Less flashy but essential for coherence over long tasks |


Missions combines four of these — delegation, creator-verifier, broadcast, and negotiation — into a single coherent workflow.


### Orchestrator, Workers, Validators


The architecture assigns three distinct roles:


* **Orchestrator** handles planning. It acts as a sounding board during initial scoping, asking strategic questions about ambiguous requirements, then produces a plan with features, milestones, and a **validation contract** — a set of assertions that define what "done" means before any code is written.
* **Workers** handle implementation. Each worker receives a single feature specification, implements it with clean context, commits via Git, and produces a structured handoff summary. The next worker inherits a clean codebase.
* **Validators** execute at milestone boundaries. The *scrutiny validator* runs linting, type-checking, the test suite, and spawns dedicated code review agents for each feature. The *user testing validator* spawns the live application, interacts with it through computer-use, fills forms, checks page rendering, and verifies functional flows end-to-end. Neither validator has seen the code beforehand — validation is adversarial by design.



```
#mermaid-1779379449872{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;fill:#333;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1779379449872 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1779379449872 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1779379449872 .error-icon{fill:#552222;}#mermaid-1779379449872 .error-text{fill:#552222;stroke:#552222;}#mermaid-1779379449872 .edge-thickness-normal{stroke-width:1px;}#mermaid-1779379449872 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1779379449872 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1779379449872 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1779379449872 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1779379449872 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1779379449872 .marker{fill:#262633;stroke:#262633;}#mermaid-1779379449872 .marker.cross{stroke:#262633;}#mermaid-1779379449872 svg{font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:16px;}#mermaid-1779379449872 p{margin:0;}#mermaid-1779379449872 .label{font-family:"trebuchet ms",verdana,arial,sans-serif;color:#333;}#mermaid-1779379449872 .cluster-label text{fill:#15171D;}#mermaid-1779379449872 .cluster-label span{color:#15171D;}#mermaid-1779379449872 .cluster-label span p{background-color:transparent;}#mermaid-1779379449872 .label text,#mermaid-1779379449872 span{fill:#333;color:#333;}#mermaid-1779379449872 .node rect,#mermaid-1779379449872 .node circle,#mermaid-1779379449872 .node ellipse,#mermaid-1779379449872 .node polygon,#mermaid-1779379449872 .node path{fill:#ECECFF;stroke:#9370DB;stroke-width:1px;}#mermaid-1779379449872 .rough-node .label text,#mermaid-1779379449872 .node .label text,#mermaid-1779379449872 .image-shape .label,#mermaid-1779379449872 .icon-shape .label{text-anchor:middle;}#mermaid-1779379449872 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1779379449872 .rough-node .label,#mermaid-1779379449872 .node .label,#mermaid-1779379449872 .image-shape .label,#mermaid-1779379449872 .icon-shape .label{text-align:center;}#mermaid-1779379449872 .node.clickable{cursor:pointer;}#mermaid-1779379449872 .root .anchor path{fill:#262633!important;stroke-width:0;stroke:#262633;}#mermaid-1779379449872 .arrowheadPath{fill:#333333;}#mermaid-1779379449872 .edgePath .path{stroke:#262633;stroke-width:2.0px;}#mermaid-1779379449872 .flowchart-link{stroke:#262633;fill:none;}#mermaid-1779379449872 .edgeLabel{background-color:#FFCB59;text-align:center;}#mermaid-1779379449872 .edgeLabel p{background-color:#FFCB59;}#mermaid-1779379449872 .edgeLabel rect{opacity:0.5;background-color:#FFCB59;fill:#FFCB59;}#mermaid-1779379449872 .labelBkg{background-color:rgba(255, 203, 89, 0.5);}#mermaid-1779379449872 .cluster rect{fill:#ffffde;stroke:#aaaa33;stroke-width:1px;}#mermaid-1779379449872 .cluster text{fill:#15171D;}#mermaid-1779379449872 .cluster span{color:#15171D;}#mermaid-1779379449872 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:"trebuchet ms",verdana,arial,sans-serif;font-size:12px;background:#A992F0;border:1px solid #aaaa33;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1779379449872 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#333;}#mermaid-1779379449872 rect.text{fill:none;stroke-width:0;}#mermaid-1779379449872 .icon-shape,#mermaid-1779379449872 .image-shape{background-color:#FFCB59;text-align:center;}#mermaid-1779379449872 .icon-shape p,#mermaid-1779379449872 .image-shape p{background-color:#FFCB59;padding:2px;}#mermaid-1779379449872 .icon-shape .label rect,#mermaid-1779379449872 .image-shape .label rect{opacity:0.5;background-color:#FFCB59;fill:#FFCB59;}#mermaid-1779379449872 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1779379449872 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1779379449872 :root{--mermaid-font-family:"trebuchet ms",verdana,arial,sans-serif;}Yes

No

Human describes goal

Orchestrator Plans & defines validation contract

Worker Implements single feature with clean context

Structured handoff summary

Scrutiny Validator Lint, type-check, tests, code review

User Testing Validator Spawns app, interacts via computer-use

Issues?

Corrective work scoped

Next feature or milestone


```

![](https://img.bgo.one/news-image/ai_generated/2026-05/9ef5dbb40c870730_1778089608_inline_3.jpg)
### Validation Contracts: Correctness Before Code


Alvoeiro identified a failure pattern that plagues most coding agents: tests written after the implementation confirm the decisions the model already made, rather than catching mistakes. Over time, this causes drift away from the original intent.


"Tests written after implementation don't catch bugs. They confirm decisions."


Missions inverts this. During the planning phase, the orchestrator writes the validation contract — often containing hundreds of assertions for a complex project. Each feature is mapped to specific assertions it must satisfy, and the sum of features must cover every assertion. After each milestone, the two validators verify against the contract, not against the implementation's own assumptions. In the Slack clone example, validation almost never succeeded on the first pass; every round surfaced follow-up features. The final result: 90% test coverage.


### Structured Handoffs and Self-Healing Loops


To prevent context decay across long runs, workers don't just signal completion. They fill out a structured handoff detailing what was completed, what was left undone, every command's exit code, any issues discovered, and whether the orchestrator's prescribed procedures were followed.


Errors surface at milestone boundaries through validator findings and handoff discrepancies. The orchestrator then scopes corrective features, pulling the mission back on track without relying on agent memory.


"The system self-heals. Not by hoping that agents remember what happened but by forcing them to write it down and then actually address issues."


### Serial Execution with Smart Parallelization


A naive instinct is to run multiple worker agents in parallel to multiply throughput. The Factory team tried it and found that in software development tasks, agents step on each other's changes, duplicate work, and make inconsistent architectural decisions. Coordination overhead negated speed gains while burning tokens.


Missions deliberately runs features **serially**: only one worker or validator is active at any given moment. Within a single feature, read-only operations — codebase search, API research — are parallelized; validators also parallelize read-only code review. Over multi-day runs, correctness compounds.


The serial model also keeps overhead low. In the Slack clone build, 60% of time and tokens went to implementation, not validation overhead — despite the rigorous two-validator system.


To support asynchronous oversight, the team built Mission Control, a dedicated view showing active worker status, handoff summaries, validator discoveries, budget consumption, and overall completion. A manager can review progress in minutes or simply disconnect and return later to finished work. The longest recorded mission ran 16 days — a full sprint's worth of sustained autonomous development.


### Model-Agnostic Orchestration and 'Droid Whispering'


No single model or provider excels at all three roles. Planning benefits from slow, careful reasoning; implementation from fast code fluency and creativity; validation from precise instruction following. The architecture explicitly allows different models — potentially from different providers — to fill each seat.


"You're only as strong as your weakest link. And if you're locked into one model provider, then you're constrained by that family's weakest capability."


The team developed a skill they call "droid whispering" — mentally modeling how different LLMs interact, where they fail, and how those failures compound over days. The system's structure also compensates for models that are not frontier-tier; validation contracts and milestone checkpoints allow successful missions even with open-weight models.


The orchestration itself is overwhelmingly prompt-driven. Around 700 lines of text define how features are decomposed, failures handled, and strategies set, with only a thin deterministic layer for bookkeeping. Worker behavior is controlled per mission by skills defined by the orchestrator.


Alvoeiro predicts that the competitive edge in this space will come from intuition:


"People who develop intuition for how different models compose under pressure in agent ecosystems will ship the next generation of innovation."


### Production Outcomes and Enterprise Use Cases


The Slack clone mission produced concrete metrics:




| Metric | Value |
| --- | --- |
| Time and tokens on implementation | 60% |
| Lines of code that were tests | 50% |
| Code covered by tests | 90% |
| Validation passes on first attempt | Almost never — always produced follow-up features |


Enterprise use cases at Factory include overnight feature prototyping, internal tooling for rapid development, large-scale refactors and migrations, codebase modernization to make agents more productive, and ML search research. The system takes heavy advantage of prompt caching to offset costs of long-running tasks.


"The codebase ends up cleaner than when you started. The end-to-end tests, the unit tests, the skills, the structure that missions provide means that agents and humans are more productive in that environment moving forward."


### Designing for Model Improvement


Alvoeiro addressed the fear that every multi-agent architecture will be obsoleted by the next model release. Missions was deliberately built so that better models make the system better. Because orchestration logic lives in prompts and skills rather than a hard-coded state machine, a few sentences can alter execution strategy. As models specialize, the ability to place the right model in the right role becomes a compounding advantage.


The team believes 30-day missions are within reach.


For investors and engineering leaders, the implication is straightforward: the value is shifting from raw model capability to the orchestration layer that coordinates multiple AI agents over days-long workflows. The teams that win will be those that build the plumbing — the validation contracts, structured handoffs, and adversarial checkpoints — that let a handful of engineers oversee the output of an entire squad of specialized models. The bottleneck is no longer whether the model can write good code. It's whether the system can keep it writing good code for three straight weeks without a human having to watch every line.