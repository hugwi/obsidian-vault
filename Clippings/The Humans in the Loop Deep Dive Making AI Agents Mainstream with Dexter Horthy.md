---
categories:
  - "[[Clippings]]"
title: "The Humans in the Loop Deep Dive: Making AI Agents Mainstream with Dexter Horthy"
source: "https://thehumansintheloop.substack.com/p/making-agents-mainstream-for-dev-with-dexter-horthy"
author:
  - "[[The Humans In The Loop]]"
published: 2026-03-26
created: 2026-06-24
rating: 
action: 
description: "A Special-Edition Interview on What's Needed to Drive Mainstream Agentic Adoption"
tags:
  - "clippings"
---
*This special edition of The Humans in the Loop features an in-depth interview on a specific topic for builders working in AI. If you have thoughts or feedback on this format, please feel free to email [andrew@heavybit.com](mailto:andrew@heavybit.com).*

**Deep Dive:** Interview with founder Dexter Horthy on what’s needed to make AI agents mainstream for developers

While AI in development seems like a foregone conclusion, not every developer is using agents in their daily workflows. What’s missing? Trust? Consistently deterministic outcomes? Security and compliance? This week, we spoke with HumanLayer founder [Dexter Horthy](https://www.linkedin.com/in/dexterihorthy/) to discuss what’s needed to normalize agentic software development.

---

2025 was to be [the year of AI agents](https://finance.yahoo.com/news/jensen-huang-declares-age-agentic-154517698.html?guccounter=1), a prediction that may or may not have come true, depending on which people you ask. For a time, it seemed like the open-standard [MCP](https://modelcontextprotocol.io/docs/getting-started/intro) would become *the* standard for orchestrating multiple autonomous AI agents (and perhaps it will), but not before it addresses its [known security vulnerabilities](https://www.darkreading.com/application-security/microsoft-anthropic-mcp-servers-risk-takeovers).

For more perspective on putting agents into production for real-world engineering teams, we spoke with founder Dexter Horthy of [HumanLayer](https://www.humanlayer.dev/) to understand how agentic coding will evolve past its many questions about security, reliability, and token economics into full adoption into mainstream software development.

## Evolving Agentic Products for Real-World Engineering Teams

Horthy acknowledges the breakneck pace at which agentic has evolved even in the past year. His own organization rolled out a “ [Research, Plan, Implement](https://github.com/humanlayer/advanced-context-engineering-for-coding-agents/blob/main/ace-fca.md) “ (RPI) framework to help engineers break complex coding tasks into discrete phases: research the codebase first, plan the approach, then implement, rather than throwing an entire ticket at a coding agent and hoping for the best.

“We rolled this out last year, but I tell people: ‘Look, I don’t know *if we’ll even be using* these same techniques in six months.’” Still, the founder notes that the RPI framework and his team’s original work on context engineering and [12-factor agents](https://news.ycombinator.com/item?id=43699271) seemed to become much more relevant as coding agents improved by leaps and bounds in the back half of 2025.

“I wanted to make it clear that there was no ‘magic’ or ‘silver bullet.’ Under the hood, we were fundamentally helping people do better context engineering, and that’s what we’ve started productizing.”

![](https://substackcdn.com/image/fetch/$s_!EOYt!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81df66f5-773c-45ad-a949-a41c7db90a7f_3840x1583.jpeg)

*Dexter Horthy discusses the importance of managing context windows in software engineering. Image courtesy [AI Engineer World’s Fair](https://www.youtube.com/watch?v=rmvDxxNubIg)*

## The Adoption Gap: When Expert Tools Meet Real Teams

The founder candidly admits that his team saw a consistent pattern when rolling out RPI across engineering organizations. Expert engineers who invested deeply in learning the tools started shipping like crazy, but when those experts handed the same tools to their teams, the results were inconsistent at best.

“We had people who loved what we did and became very good at it just by finding our stuff online, or sitting down and doing a workshop with us.” But when the early adopters tried to share the new knowledge and frameworks with their colleagues who weren’t as invested, those folks didn’t get the incredible results that were possible with a lot of time investment, and the adoption didn’t spread.

When Horthy’s team investigated, they found specific, diagnosable problems. The first was bad research: A skilled engineer would naturally break a ticket into targeted codebase questions, but most people would just paste the entire ticket into the research tool and get back opinions instead of facts.

“The problem is, if you tell the model *what you’re building*, you get opinions. The model starts making implementation decisions instead of proposing options to you around how to proceed.”

The second problem was bad plans. The team’s planning prompt had 85+ instructions, and buried inside were critical interactive steps like “present design options to the user” and “get feedback before writing the plan.” For about half of users, the agent would skip all of that and just hand back a finished plan with all decisions already made.

“When we investigated, we found the difference between good and bad results was a single line: ‘Work back and forth with me, starting with your open questions and outline before writing the plan.’ I found myself standing in workshops full of enterprise engineers saying, ‘Folks, yeah, here’s the software, but don’t forget to say the magic words.’ It was, quite frankly, embarrassing.”

The founder notes that this wasn’t the user’s fault. It was a tooling problem. His co-founder [Kyle](https://x.com/0xBlacklight) wrote a [blog post](https://www.hlyr.dev/blog/writing-a-good-claude-md) citing research showing that frontier LLMs can only follow about 150 to 200 instructions with good consistency. Their planning prompt alone had 85 instructions. Add in the system prompt, tool definitions, and MCP servers, and the model was simply over budget.

“Solving these problems is actually still pretty hard. I don’t think any of this stuff has been commoditized yet, though maybe it will be. But that’s why we’re excited about building collaboration features and changing the SDLC by creating a Google Docs/Notion/Figma-like experience around coding agents.”

## The Instruction Budget: Why Less Context Means Better Code

This diagnosis (that LLMs have a finite instruction budget) became the foundation for Horthy’s fix. As [Geoff Huntley](https://x.com/GeoffreyHuntley) puts it, the less of the context window you use, the better results you’ll get. But it’s not just about stuffing in too much information. You can also overload the model with too many instructions.

Huntley’s [Ralph Wiggum loop](https://ghuntley.com/ralph), an ultra-viral technique of wrapping a coding agent in a [Bash](https://en.wikipedia.org/wiki/Bash_\(Unix_shell\)) *while* loop to periodically refresh its context, took off because it addressed the performance-eroding [context rot](https://www.understandingai.org/p/context-rot-the-emerging-challenge) that creeps in over successive runs. Horthy sees the lessons as more durable than the technique itself.

“The thing about Ralph is that we might not be using the same prompts in six months. It might not be the same technique in six months. This stuff is going to evolve. I think the most valuable thing about Ralph is the lessons that it teaches about context engineering.”

“If what you’re doing is grounded in understanding context engineering and the limitations of attention, you don’t actually have to do any of that complicated stuff. If you just take care of keeping your context window small, you can get really good results.”

Horthy suggests the broader conversation around Ralph ultimately reinforced a principle his team was already learning the hard way: giving the model fewer instructions, simpler tasks, and smaller context windows. “I don’t know if I actually recommend that people should use Ralph to write production software.”

“It’s more about understanding *how* it works and *why* it’s good and then applying those lessons for your workflow. For example, our implementer agent uses faster, smaller models for writing the code and running the tests, and then a bigger, smarter model spot checks changes, keeping context usage in the parent session low, allowing for resteering.”

![](https://substackcdn.com/image/fetch/$s_!k23S!,w_1456,c_limit,f_webp,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F79ea17d2-caaa-4007-bf02-404aa0d96758_1100x601.jpeg)

*Geoff Huntley’s viral Ralph loop is a clever hack, but does it represent the actual future of agentic coding? Image courtesy [Geoff Huntley](https://ghuntley.com/loop)*

## Will Coding Agents Help Everyone Roll Their Own Everything?

While use cases for different verticals emerge frequently, AI’s strongest proof of concept still seems to be in code generation. Yet as users attempt to build in more multi-step [long-horizon tasks](https://research.google/pubs/modelling-long-horizon-tasks-as-sequential-interaction-landscapes) with their coding agents, they continue to bump up against the limitations of long context windows, including rot and hallucinations.

“I think the thing that everyone will agree on is that you will always get better results if you use less of the context. And ‘using less of the context’ is a thing that you, the engineer, have to think about. How do you want to do this, and how do you fit that into your workflow?”

Will models and coding agents eventually hit an inflection point past which organizations stop relying on packaged software and start simply rolling their own? “I think we’re going to see a lot more hand-rolled versions of software. The 2010 ZIRP-era practice of ‘get a SaaS for everything’ is probably going to look very different in the coming years.”

“I got really excited a few years back when Klarna claimed it would drop Salesforce and Workday and just build it all themselves. Those are the two vendors that *nobody* ever fires! I think they ended up like [walking that back](https://diginomica.com/those-shutting-down-salesforce-and-workday-rumors-klarna-no-we-didnt-replace-saas-llm-admits-ceo) a bit.” However, the founder suggests that orgs rolling their own internal tools may still be the right direction.

“I’m not going to say that the change will happen through vibe coding because I’m sure engineering will need to be done. There’s a difference between spending 20 years building a piece of software and building an internal version in a hurry. There are just things that happen when you spend 20 years on something that you will not get for a while no matter how much AI you point at it.”

## Please Read the Code: Why Reviewing Plans Wasn’t Enough

Perhaps the most candid reversal in Horthy’s updated thinking concerns code review. In the original RPI framework, he advocated for reading plans instead of code, with the logic being that an engineer can’t easily review 2,000 lines of generated code, but *can* review a 200-line plan.

“I was wrong. I am humble enough to admit when I was wrong.” The founder explains that after six months of reviewing plans instead of code, the team had to rip out and replace large parts of their system. A 1,000-line plan tends to produce about 1,000 lines of code, so there was no actual reading “savings.” Worse, the implementation would sometimes diverge from the plan, forcing the reviewer to hold both in their head.

“The new advice is: Don’t read the plans. Please read the code. It’s the same amount of work, there may be surprises that cause drift between the plan and the code, and the code is the thing that actually ships.”

Horthy acknowledges the elephant in the room, namely high-profile open-source projects like [Beads](https://github.com/steveyegge/beads) where allegedly nobody reads all the code. “These are very cool projects. But nobody gets paged at 3 a.m. if they’re broken. Nobody gets fined millions of dollars if it’s done wrong.”

The founder describes how this realization shaped the team’s approach to feedback loops. “How do you increase the odds that the code being reviewed is correct and needs no iteration?”

Rather than reviewing faster, the goal became aligning the agent *before* it writes code. The team now surfaces all codebase patterns that might apply to a problem and lets humans decide between old patterns that shouldn’t be used anymore and newer approaches that should inform future decisions.

“LLMs are really good at finding patterns and following them. In a way, this is all they do. They take some input, some text, and translate it. ‘Match the format of this code we found in the codebase in this other file over here.’”

Horthy also wrote [a blog post](https://www.humanlayer.dev/blog/context-efficient-backpressure) about making testing feedback more context-efficient, giving the model deterministic signals about what’s broken rather than dumping entire test outputs into the context window. “No matter how big context windows get, you always get better results if you use less of them.”

> *“No matter how big context windows get, you always get better results if you use less of them.” -Dexter Horthy, Founder/HumanLayer*

## From RPI to QRSPI: Splitting the Monolith

Before going deep on coding agents, Horthy wrote [12 Factor Agents](https://hlyr.dev/12fa), which was arguably the first deep dive on “context engineering.” The paper’s core argument: Don’t use prompts for control flow. If you know what the workflow is, use actual control flow. Classify the input, then feed it to a series of smaller, more-focused prompts with fewer instructions and fewer actions to choose from.

The irony was not lost. “We got on stage and said ‘full-fat agents don’t work, build workflows and micro agents, use control flow for control flow.’ Then we turned around and wrote a giant monolithic 85-instruction prompt. It was time to drink our own Kool-Aid.”

So his team split it. Their original three-step workflow (Research, Plan, Implement) became a seven-step pipeline: **Questions, Research, Design, Structure, Plan, Worktree, Implement**, each step with fewer than 40 instructions.

The key innovation is where the human review now happens. Rather than reviewing a 1,000-line plan or 1,000 lines of code after the fact, the new workflow front-loads alignment into two short artifacts: a **design discussion** (~200 lines) and a **structure outline** (~2 pages).

The design discussion captures current state, desired end state, patterns found in the codebase, resolved decisions, and open questions. The structure outline maps out the order of phases and how to validate along the way.

“You’re forcing the agent to brain-dump everything it found, everything it wants to do, everything it *thinks* you want, and ask you questions about things it doesn’t know. You get to do brain surgery on the agent *before* you proceed downstream. 200 lines instead of 1,000. That’s leverage.”

The acronym didn’t work out so well (QRDSPWIP), so the team picked a subset and started calling it **QRSPI**.

## The Future of Orchestration

Regarding the future of managing agents, Horthy cautions against making absolute judgements about whether one agentic technique or framework is uniformly “better” without considering the details.

What’s more important is knowing *when* to decompose. “Sometimes you hit a wall, so you decide to decompose your workflow and make it more reliable, more robust, but maybe a little bit less able to handle everything in the input space.”

“But once you get to know what the input space would *be*, you can give people a happy path that’s much more reliable. And then you can always still eject out of the situation and say, ‘Hey, something unexpected happened. Let’s see if the LLM can figure it out.’”

On the question of whether agentic frameworks could be declared uniformly ‘good’ or ‘bad,’ the founder concedes that using them like properly-specified tools in a loop, with proper expectations, can work well...provided you’re prepared to decompose longer workflows into smaller slices and manage context across each step. “These are tools in your arsenal. You need to know where on that autonomy slider you want to be.”

*This interview originally appeared on [Heavybit.com](https://www.heavybit.com/library/article/whats-missing-to-make-ai-agents-mainstream).*