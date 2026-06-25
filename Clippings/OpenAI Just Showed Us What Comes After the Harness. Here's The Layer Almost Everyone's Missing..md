---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, ai-agents]
tags:
  - harness
  - orchestration
  - workflow-git
source: readwise
created: 2026-06-23
rating: 
action: 
theme: workflow-phases-gates
subtheme:
  - harness-loops
---

# OpenAI Just Showed Us What Comes After the Harness. Here's The Layer Almost Everyone's Missing.

![rw-book-cover](https://i.ytimg.com/vi/5p6h23Md4Zw/sddefault.jpg)

## Metadata
- Author: [[The AI Automators]]
- Full Title: OpenAI Just Showed Us What Comes After the Harness. Here's The Layer Almost Everyone's Missing.
- Category: #articles
- Summary: OpenAI created an open-source tool called Symphony to help many AI coding agents work together smoothly. They explain that AI agents need both inner and outer harness layers to manage tasks and improve results. This new approach reduces human bottlenecks and makes AI systems more reliable and scalable.
- URL: https://www.youtube.com/watch?v=5p6h23Md4Zw&t=47s

## Full Document
OpenAI just published a fascinatingarticle about their new open-sourceagent orchestrator to help overcome thebiggest bottlenecks they encounteredwhen trying to scale autonomous codingagents. And there are some interestinginsights here that could really help usall when we're building our own agenticsystems. Back in February, OpenAI showeda relatively controversial experimentthey were running internally to createsoftware with zero lines of manuallywritten code. Instead of micromanagingthe coding agents, the primary job ofthe engineer was now to createscaffolding around the coding agent toenable it to do work with less

supervision. As these systems becameincreasingly efficient, humans could nolonger keep up with coding agents, andall of a sudden, the humans were now thebiggest bottleneck in the process. Andthat was the birth of OpenAI'sopen-sourced Symphony orchestrationspec. So what exactly is Symfony? Well,At its core, Symfony is an agentorchestrator that takes an issue trackerlike Linear here and turns it into atool that can trigger coding agents. Theconcept here is pretty simple. For everyticket on this board, Symfony makessure there's a coding agent running forit in its own isolated workspace,

working continuously until the ticket isdone. And OpenAI are essentiallycreating a state machine flow usingLinear here. This can then potentiallyallow teams to work at a higher level ofabstraction rather than just babysittingand supervising individual codingsessions. And in theory, less technicalstaff members can also get involved inthe process. When you go to the GitHubrepo, the first thing you'll notice isthat this is mostly just a spec.md file,but they also have a prototype versionyou can use created in Elixir, whichI'll talk about in a few minutes. OpenAIencourage you to point your favorite

coding agent at the spec and then haveIt implements its own version in whateverlanguage you want and also get it toorchestrate against whatever codingagent you want, not just codecs. So youdon't have to have a codec subscriptionto run this. Surprisingly enough, eventhe OpenAI article shows some post on Xwhere people are showing how theyimplemented this to orchestrate cloudcode sessions. So you have two optionsto run with here. If you want to usetheir reference elixir implementation,you can clone the repo and then get yourcoding agent to help with the setup.

Then you can connect that to a linearaccount using your personal API key andthen that will continuously pull thetickets here. That then calls Codeex inapp server mode and app server mode runsthe Codeex CLI as a long-lived process andthen Symfony can then call thatprogrammatically. There's certainlyplenty of OpenAI marketing within thisarticle. Like they've stated that thishas resulted in a 500% increase inLanded pull requests on some teams, butcountless devs have converged on similartypes of systems to this. And OpenAI arecertainly not the first dev team tobuild orchestration around codingagents. I think the most importantlesson here is unpacking the

architectural layers that make a systemlike this work and how we can then makeeffective use of those systems in ourown projects. And many of you watchingthis will already know that attemptingto scale AI coding agents beyond a fewconcurrent chat sessions definitelycomes with its own set of challenges. Soyou may be staring at a coding chatwindow wondering how do I turn this intoa reliable autonomous agent at scale formy project. Or you may want to buildadvanced orchestration features intoyour AI powered apps but you're gettinglost in the architecture. I'm going toshare some great mental models andresources that I find really useful.

Let's start by clearing up someAmbiguity about the term agent harness,which at this point could mean manydifferent things. As Philip Schmid putit, "An agent harness is theinfrastructure that wraps around an AImodel."As you can see from his clearlyAI-generated image here, the agentharness manages the vast majority of thework within our AI systems. And hecompares the AI model to that of the CPUof a computer in that it is veryimportant, but it has a very specificfunction.

An LLM is really only able toreason about its responses and thengenerate an output such as text.Everything beyond that, from the illusionof memory and chat history to managingsub-agents to actually managing theexecution of tool calls, that's allactually managed within the harnesscode.

So the definition of an agentharness is incredibly broad. And to makebetter sense of this, we're going toborrow some mental models from VettaBerkeler's great article on harness.

Engineering, where she suggested that weshould view agent harnesses in twoseparate layers. The first is the innerharness. The inner harness is everythingthat ships inside your AI coding agent,whether it be cloud code or cursor orcodecs. Of course, they're very powerfulout of the box already. They ship insidewith the ability to manage sub-agents,sandbox code execution, skills, hooks,tools, permissions, and more. But asBrigitta writes in this article, to letcoding agents work with lesssupervision, we need ways to increaseour confidence in their result. But howexactly do we do that? As a startingpoint, we can try and give our codingagents better context of the overallcodebase. We can try and convince themto do a better job via better prompting.

And we can also use meta promptingframeworks such as superpowers or GSDversion one or VMAD. And those thingsabsolutely help, but they only go sofar. And that's where the realEngineering of the outer harness comesinto play. Coding agents such as Claudeor Codeex expose features that let usbuild an outer harness around them. Andthese harnesses are actual code thatcontrols the agent lifecycleprogrammatically. So, instead of using ameta prompting framework where we mightask the AI agent to reset the context,the outer harness can actuallydeterministically terminate the session,

clear the context, read the task statefrom disk, inject the relevant files,and then work from there. So, Ralph loopsor projects like Gas Town or Archon areall examples of systems that act asouter harnesses. In this article, itsaid that the harness acts like acybernetic governor, combining feedforward and feedback to regulate thecodebase towards the desired state. Thatfeedback mechanism is one of the mostimportant parts of this process. There'sa very useful distinction between guidesand sensors here, where the guides helpSteer the agent in the right direction.

So, these are anything that tries to makethe agent's first attempt better. So, youragent might read from an agent's MD file,or you may provide skills and playbooks,and examples that they can work from.But the AI agent is not always going toget things right, and even if so, notnecessarily according to your ownbehaviors and rules. And that's where thevery important feedback loop comes in.

And these are referred to as sensors. So,we might have deterministiccomputational-based sensors such aslinters, types, and schemas. So, forexample, whenever your coding agentcreates code, you can run those throughdeterministic checks,without using AI atall, and then feed that back to themodel. And one of the main argumentsmade within this article is that thesecomputational type checks are heavilyunderused by AI builders. Of course, youcan also have sensors powered by AI,known as inferential sensors, such as you.

Can feed code generated by an LLM intoanother call to an LLM, ideally anothermodel where it can act as a judge,and then that can be fed back into the model,and humans then continuously steer andoptimize the components of this outerharness. If we go back to our OpenAIarticle on harness engineering, they'verun with this type of concept where theagent is called in a Ralph Wigum loop,until all human reviewers are satisfied.

Running an external Ralph Wigum loop,not the one built into Claude codedirectly, by the way, is a very simpleexample of an outer harness. It justkeep spawning Claude sessions again andagain through brute forceiteration until a certain goal has beenmet. And other outer harnesses can justtake this thin orchestrator concept as astarting point and bring it many stepsfurther and potentially in manydifferent directions. Archon is a greatexample of a tool that allows you tocreate your own outer harnesses whichCan enforce your agents to act in acertain deterministic way. It alreadyincludes a lot of out-of-the-boxworkflows, and it even allows forparallel executions of tasks. We usethis inner-outer harness distinction as

a mental model not only for codingagents but also for agentic systems webuild. In our full stack AI builderseries, Daniel walks through thecreation of a contract review harness,that adds deterministic aspects to theagentic workflow. And this canessentially be seen as an outer harness,a configurable aspect that's layered ontop of the inner harness corefunctionality of the agentic system. Itcan have guides and sensors that areautomatically fed back into the agent,such as automated computational documentchecks that don't use AI at all, as wellas inferential checks, such as LLM as ajudge. And these harnesses will lie on aspectrum between either being verydeterministic or very probabilistic.

That contract review harness tends tofollow a very specific workflow. Butmany other harnesses will be a lot moreopen-ended, such as deep researchharnesses. And these are essentially theopposite shape. They're broad,open-ended, and agentic throughout, butthey can still have plenty ofdeterministic scaffolding around them,such as computational checking ofcitations or multiple layers of LMreviews before they’re passed back forhuman review. As we start building uponthe scaffolding on top of our AI agents,you may even consider that they startbecoming their own layer on top of themental model we've talked about already.And this layer could be seen as theoverarching orchestrator or schedulerlayer. And that's very much where OpenAIpositions systems created using theirnew symphony spec as this is reallymulti-agent orchestration at a higherlevel. These are all mental models andmetaphors. They just help our general

Understanding of the concepts and thelines can very much be blurred betweenthem. For example, Gas Town is anorchestration framework where it takesthe concept of a Ralph Wiggum loop havemany of them running at once along withautomated orchestration around thoseinstances. And this can certainly getquite chaotic. But frameworks like thisare trying to solve the problem ofgetting many agents to work reliably inparallel. And the two biggest issuesthat people face other than theirintense token usage and AI builds withsystems like this is twofold. It'smaking AI agents work reliably togetherwithout clashing and adding in thecorrect human in the loop layers wherehumans are in the most important partsof the process without micromanagingeverything because that becomes thebiggest bottleneck and again that'swhere we come back to this Symfony spec.

Symfony started with a concept that anyopen task should get picked up andCompleted by an agent instead ofdevelopers managing codec sessions inmultiple tabs. They made this issuetracker in linear and use that as thehuman interface. Those tickets thentrigger the coding agent to workautonomously on those tasks as requiredand then report back to the user whenrequired. If you want to get startedwith the Symfony open-source spec, it'savailable on the GitHub repo linkedbelow. And you can get your own codingagent to create an orchestration systembased on this spec in whatever languageyou want, or you can also use their

out-of-the-box demo example. In thisvideo, we went through a lot of AIarchitecture concepts. If you found thatuseful, you should definitely check outour AI architects course linked below,which will help give you a deeperunderstanding of AI systems, technicalfoundations, harness engineering,agentic retrieval, and more. And if youlike this video, you'll love thePrevious video on our channel whereDaniel goes through a deep dive into thevarious agent frameworks and servicesyou can use when building out AIsystems.
