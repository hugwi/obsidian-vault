---
categories:
  - "[[Resources]]"
domain: engineering
title: "OpenAI Just Showed Us What Comes After the Harness. Here's The Layer Almost"
source: "https://www.youtube.com/watch?v=5p6h23Md4Zw&t=47s"
author: "The AI Automators"
published: 2026-04-30
created: 2026-05-13
description: "👉 Access our AI Architects course & join hundreds of serious AI builders"
tags:
  - to-process
  - orchestration
---

OpenAI just published a fascinating article about their new open-source agent orchestrator to help overcome the biggest bottlenecks they encountered when trying to scale autonomous coding agents. And there are some interesting insights here that could really help us all when we're building our own agentic systems. Back in February, OpenAI showed a relatively controversial experiment they were running internally to create software with zero lines of manually written code. Instead of micromanaging the coding agents, the primary job of the engineer was now to create scaffolding around the coding agent to 

enable it to do work with less supervision. As these systems became increasingly efficient, humans could no longer keep up with coding agents and all of a sudden the humans were now the biggest bottleneck in the process. And that was the birth of OpenAI's open-sourced Symphony orchestration spec. So what exactly is Symfony? Well, at its core, Symfony is an agent orchestrator that takes an issue tracker like Linear here and turns it into a tool that can trigger coding agents. The concept here is pretty simple. For every ticket on this board, Symphfony makes 

sure there's a coding agent running for it in its own isolated workspace, working continuously until the ticket is done. And OpenAI are essentially creating a state machine flow using linear here. This can then potentially allow teams to work at a higher level of abstraction rather than just babysitting and supervising individual coding sessions. And in theory, less technical staff members can also get involved in the process. When you go to the GitHub repo, the first thing you'll notice is that this is mostly just a spec.md file, but they also have a prototype version you can use created in Elixir, which 

I'll talk about in a few minutes. OpenAI encourage you to point your favorite coding agent at the spec and then have it implement its own version in whatever language you want and also get it to orchestrate against whatever coding agent you want, not just codecs. So you don't have to have a codec subscription to run this. Surprisingly enough, even the OpenAI article shows some post on X where people are showing how they implemented this to orchestrate cloud code sessions. So you have two options to run with here. If you want to use their reference elixir implementation, you can clone the repo and then get your 

coding agent to help with the setup. Then you can connect that to a linear account using your personal API key and then that will continuously pull the tickets here. That then calls Codeex in app server mode and app server mode runs the codeex CLI as a longived process and then Symfony can then call that programmatically. There's certainly plenty of OpenAI marketing within this article. Like they've stated that this has resulted in a 500% increase in landed pull requests on some teams, but countless devs have converged on similar types of systems to this. And OpenAI are 

certainly not the first dev team to build orchestration around coding agents. I think the most important lesson here is unpacking the architectural layers that make a system like this work and how we can then make effective use of those systems in our own projects. And many of you watching this will already know that attempting to scale AI coding agents beyond a few concurrent chat sessions definitely comes with its own set of challenges. So you may be staring at a coding chat window wondering how do I turn this into a reliable autonomous agent at scale for 

my project. Or you may want to build advanced orchestration features into your AI powered apps but you're getting lost in the architecture. I'm going to share some great mental models and resources that I find really useful. Let's start by clearing up some ambiguity about the term agent harness, which at this point could mean many different things. As Philip Schmid put it, "An agent harness is the infrastructure that wraps around an AI model." As you can see from his clearly AI generated image here, the agent harness manages the vast majority of the work within our AI systems. And he compares the AI model to that of the CPU 

of a computer in that it is very important, but it has a very specific function. An LLM is really only able to reason about its responses and then generate an output such as text. Everything beyond that from the illusion of memory and chat history to managing sub agents to actually managing the execution of tool calls that's all actually managed within the harness code. So the definition of an agent harness is incredibly broad. And to make better sense of this we're going to borrow some mental models from Vetta Berkeler's great article on harness 

engineering where she suggested that we should view agent harnesses in two separate layers. The first is the inner harness. The inner harness is everything that ships inside your AI coding agent, whether it be cloud code or cursor or codecs. Of course, they're very powerful out of the box already. They ship inside with the ability to manage sub agents, sandbox code execution, skills, hooks, tools, permissions, and more. But as Brigitta writes in this article, to let coding agents work with less supervision, we need ways to increase our confidence in their result. But how 

exactly do we do that? As a starting point, we can try and give our coding agents better context of the overall code base. We can try and convince them to do a better job via better prompting. And we can also use meta prompting frameworks such as superpowers or GSD version one or VMAD. And those things absolutely help, but they only go so far. And that's where the real engineering of the outer harness comes into play. Coding agents such as Claude or Codeex expose features that let us build an outer harness around them. And these harnesses are actual code that 

controls the agent life cycle programmatically. So instead of using a meta prompting framework where we might ask the AI agent to reset the context, the outer harness can actually deterministically terminate the session, clear the context, read the task state from disk, inject the relevant files, and then work from there. So Ralph loops or projects like Gas Town or Archon are all examples of systems that act as outer harnesses. In this article, it said that the harness acts like a cybernetic governor combining feed forward and feedback to regulate the 

codebase towards the desired state. That feedback mechanism is one of the most important parts of this process. There's a very useful distinction between guides and sensors here where the guides help steer the agent in the right direction. So these are anything that tries to make the agents first attempt better. So your agent might read from an agent's MD file or you may provide skills and playbooks and examples that they can work from. But the AI agent is not always going to get things right and even if so not necessarily according to your own behaviors and rules and that's where the 

very important feedback loop comes in and these are referred to as sensors. So we might have deterministic computationalbased sensors such as llinters and types and schemas. So for example whenever your coding agent creates code you can run those through deterministic checks without using AI at all and then feed that back to the model. And one of the main arguments made within this article is that these computational type checks are heavily underused by AI builders. Of course, you can also have sensors powered by AI 

known as inferential sensors such as you can feed code generated by an LLM into another call to an LLM, ideally another model where it can act as a judge and then that can be fed back into the model and humans then continuously steer and optimize the components of this outer harness. If we go back to our OpenAI article on harness engineering, they've run with this type of concept where the agent is called in a Ralph Wigum loop until all human reviewers are satisfied. Running an external Ralph Wigum loop, not the one built into Claude code 

directly, by the way, is a very simple example of an outer harness. It can just keep spawning Claude sessions again and again and again through brute force iteration until a certain goal has been met. and other outer harnesses can just take this thin orchestrator concept as a starting point and bring it many steps further and potentially in many different directions. Archon is a great example of a tool that allows you to create your own outer harnesses which can enforce your agents to act in a certain deterministic way. It already includes a lot of out ofthe-box workflows and it even allows for 

parallel executions of tasks. We use this inner outer harness distinction as a mental model not only for coding agents but also for agentic systems we build. In our full stack AI builder series, Daniel walks through the creation of a contract review harness that adds deterministic aspects to the agentic workflow. And this can essentially be seen as an outer harness, a configurable aspect that's layered on top of the inner harness core functionality of the agentic system. It can have guides and sensors that are automatically fed back into the agent 

such as automated computational document checks that don't use AI at all as well as inferential checks such as LLM as a judge. And these harnesses will lie on a spectrum between either being very deterministic or very probabilistic. That contract review harness tends to follow a very specific workflow. But many other harnesses will be a lot more open-ended, such as deep research harnesses. And these are essentially the opposite shape. They're broad, open-ended, and agentic throughout, but they can still have plenty of deterministic scaffolding around them, 

such as computational checking of citations or multiple layers of LM reviews before they're passed back for human review. As we start building upon the scaffolding on top of our AI agents, you may even consider that they start becoming their own layer on top of the mental model we've talked about already. And this layer could be seen as the overarching orchestrator or scheduler layer. And that's very much where OpenAI positions systems created using their new symphony spec as this is really multi-agent orchestration at a higher level. These are all mental models and 

metaphors. They just help our general understanding of the concepts and the lines can very much be blurred between them. For example, Gas Town is an orchestration framework where it takes the concept of a Ralph Wiggum loop have many of them running at once along with automated orchestration around those instances. And this can certainly get quite chaotic. But frameworks like this are trying to solve the problem of getting many agents to work reliably in parallel. And the two biggest issues that people face other than their intense token usage and AI builds with 

systems like this is twofold. It's making AI agents work reliably together without clashing and adding in the correct human in the loop layers where humans are in the most important parts of the process without micromanaging everything because that becomes the biggest bottleneck and again that's where we come back to this Symfony spec. Symfony started with a concept that any open task should get picked up and completed by an agent instead of developers managing codec sessions in multiple tabs. They made this issue tracker in linear and use that as the 

human interface. Those tickets then trigger the coding agent to work autonomously on those tasks as required and then report back to the user when required. If you want to get started with the Symfony open-source spec, it's available on the GitHub repo linked below. And you can get your own coding agent to create an orchestration system based on this spec in whatever language you want, or you can also use their out-of-the-box demo example. In this video, we went through a lot of AI architecture concepts. If you found that useful, you should definitely check out our AI architects course linked below, 

which will help give you a deeper understanding of AI systems, technical foundations, harness engineering, agentic retrieval, and more. And if you like this video, you'll love the previous video on our channel where Daniel goes through a deep dive into the various agent frameworks and services you can use when building out AI systems. 

<p>
 <span data-rw-start="0.08" data-rw-transcript-version="2">
 OpenAI just published a fascinating
 </span>
 <span data-rw-start="1.839" data-rw-transcript-version="2">
 article about their new open-source
 </span>
 <span data-rw-start="3.84" data-rw-transcript-version="2">
 agent orchestrator to help overcome the
 </span>
 <span data-rw-start="6.319" data-rw-transcript-version="2">
 biggest bottlenecks they encountered
 </span>
 <span data-rw-start="8.48" data-rw-transcript-version="2">
 when trying to scale autonomous coding
 </span>
 <span data-rw-start="10.559" data-rw-transcript-version="2">
 agents. And there are some interesting
 </span>
 <span data-rw-start="12.24" data-rw-transcript-version="2">
 insights here that could really help us
 </span>
 <span data-rw-start="14" data-rw-transcript-version="2">
 all when we're building our own agentic
 </span>
 <span data-rw-start="15.839" data-rw-transcript-version="2">
 systems. Back in February, OpenAI showed
 </span>
 <span data-rw-start="18.08" data-rw-transcript-version="2">
 a relatively controversial experiment
 </span>
 <span data-rw-start="19.84" data-rw-transcript-version="2">
 they were running internally to create
 </span>
 <span data-rw-start="21.84" data-rw-transcript-version="2">
 software with zero lines of manually
 </span>
 <span data-rw-start="24" data-rw-transcript-version="2">
 written code. Instead of micromanaging
 </span>
 <span data-rw-start="26.08" data-rw-transcript-version="2">
 the coding agents, the primary job of
 </span>
 <span data-rw-start="27.92" data-rw-transcript-version="2">
 the engineer was now to create
 </span>
 <span data-rw-start="29.76" data-rw-transcript-version="2">
 scaffolding around the coding agent to
 </span>
 <span data-rw-start="32.32" data-rw-transcript-version="2">
 enable it to do work with less
 </span>
</p>
<p>
 <span data-rw-start="33.92" data-rw-transcript-version="2">
 supervision. As these systems became
 </span>
 <span data-rw-start="35.84" data-rw-transcript-version="2">
 increasingly efficient, humans could no
 </span>
 <span data-rw-start="37.68" data-rw-transcript-version="2">
 longer keep up with coding agents, and
 </span>
 <span data-rw-start="39.68" data-rw-transcript-version="2">
 all of a sudden, the humans were now the
 </span>
 <span data-rw-start="41.44" data-rw-transcript-version="2">
 biggest bottleneck in the process. And
 </span>
 <span data-rw-start="43.2" data-rw-transcript-version="2">
 that was the birth of OpenAI's
 </span>
 <span data-rw-start="44.8" data-rw-transcript-version="2">
 open-sourced Symphony orchestration
 </span>
 <span data-rw-start="46.719" data-rw-transcript-version="2">
 spec. So what exactly is Symfony? Well,
 </span>
 <span data-rw-start="49.2" data-rw-transcript-version="2">
 At its core, Symfony is an agent
 </span>
 <span data-rw-start="51.12" data-rw-transcript-version="2">
 orchestrator that takes an issue tracker
 </span>
 <span data-rw-start="53.28" data-rw-transcript-version="2">
 like Linear here and turns it into a
 </span>
 <span data-rw-start="55.44" data-rw-transcript-version="2">
 tool that can trigger coding agents. The
 </span>
 <span data-rw-start="57.6" data-rw-transcript-version="2">
 concept here is pretty simple. For every
 </span>
 <span data-rw-start="59.359" data-rw-transcript-version="2">
 ticket on this board, Symfony makes
 </span>
 <span data-rw-start="61.359" data-rw-transcript-version="2">
 sure there's a coding agent running for
 </span>
 <span data-rw-start="63.039" data-rw-transcript-version="2">
 it in its own isolated workspace,
 </span>
</p>
<p>
 <span data-rw-start="65.28" data-rw-transcript-version="2">
 working continuously until the ticket is
 </span>
 <span data-rw-start="67.2" data-rw-transcript-version="2">
 done. And OpenAI are essentially
 </span>
 <span data-rw-start="68.799" data-rw-transcript-version="2">
 creating a state machine flow using
 </span>
 <span data-rw-start="70.72" data-rw-transcript-version="2">
 Linear here. This can then potentially
 </span>
 <span data-rw-start="72.72" data-rw-transcript-version="2">
 allow teams to work at a higher level of
 </span>
 <span data-rw-start="74.64" data-rw-transcript-version="2">
 abstraction rather than just babysitting
 </span>
 <span data-rw-start="76.56" data-rw-transcript-version="2">
 and supervising individual coding
 </span>
 <span data-rw-start="78.4" data-rw-transcript-version="2">
 sessions. And in theory, less technical
 </span>
 <span data-rw-start="80.799" data-rw-transcript-version="2">
 staff members can also get involved in
 </span>
 <span data-rw-start="82.479" data-rw-transcript-version="2">
 the process. When you go to the GitHub
 </span>
 <span data-rw-start="84.159" data-rw-transcript-version="2">
 repo, the first thing you'll notice is
 </span>
 <span data-rw-start="85.52" data-rw-transcript-version="2">
 that this is mostly just a spec.md file,
 </span>
 <span data-rw-start="87.92" data-rw-transcript-version="2">
 but they also have a prototype version
 </span>
 <span data-rw-start="89.52" data-rw-transcript-version="2">
 you can use created in Elixir, which
 </span>
 <span data-rw-start="91.2" data-rw-transcript-version="2">
 I'll talk about in a few minutes. OpenAI
 </span>
 <span data-rw-start="93.119" data-rw-transcript-version="2">
 encourage you to point your favorite
 </span>
</p>
<p>
 <span data-rw-start="94.4" data-rw-transcript-version="2">
 coding agent at the spec and then have
 </span>
 <span data-rw-start="96.24" data-rw-transcript-version="2">
 It implements its own version in whatever
 </span>
 <span data-rw-start="98.159" data-rw-transcript-version="2">
 language you want and also get it to
 </span>
 <span data-rw-start="99.92" data-rw-transcript-version="2">
 orchestrate against whatever coding
 </span>
 <span data-rw-start="101.439" data-rw-transcript-version="2">
 agent you want, not just codecs. So you
 </span>
 <span data-rw-start="103.759" data-rw-transcript-version="2">
 don't have to have a codec subscription
 </span>
 <span data-rw-start="105.68" data-rw-transcript-version="2">
 to run this. Surprisingly enough, even
 </span>
 <span data-rw-start="107.68" data-rw-transcript-version="2">
 the OpenAI article shows some post on X
 </span>
 <span data-rw-start="110.399" data-rw-transcript-version="2">
 where people are showing how they
 </span>
 <span data-rw-start="112.079" data-rw-transcript-version="2">
 implemented this to orchestrate cloud
 </span>
 <span data-rw-start="113.92" data-rw-transcript-version="2">
 code sessions. So you have two options
 </span>
 <span data-rw-start="115.68" data-rw-transcript-version="2">
 to run with here. If you want to use
 </span>
 <span data-rw-start="117.2" data-rw-transcript-version="2">
 their reference elixir implementation,
 </span>
 <span data-rw-start="119.36" data-rw-transcript-version="2">
 you can clone the repo and then get your
 </span>
 <span data-rw-start="121.04" data-rw-transcript-version="2">
 coding agent to help with the setup.
 </span>
</p>
<p>
 <span data-rw-start="122.64" data-rw-transcript-version="2">
 Then you can connect that to a linear
 </span>
 <span data-rw-start="124.159" data-rw-transcript-version="2">
 account using your personal API key and
 </span>
 <span data-rw-start="126.479" data-rw-transcript-version="2">
 then that will continuously pull the
 </span>
 <span data-rw-start="128" data-rw-transcript-version="2">
 tickets here. That then calls Codeex in
 </span>
 <span data-rw-start="130.08" data-rw-transcript-version="2">
 app server mode and app server mode runs
 </span>
 <span data-rw-start="132.56" data-rw-transcript-version="2">
 the Codeex CLI as a long-lived process and
 </span>
 <span data-rw-start="135.68" data-rw-transcript-version="2">
 then Symfony can then call that
 </span>
 <span data-rw-start="137.2" data-rw-transcript-version="2">
 programmatically. There's certainly
 </span>
 <span data-rw-start="138.72" data-rw-transcript-version="2">
 plenty of OpenAI marketing within this
 </span>
 <span data-rw-start="140.56" data-rw-transcript-version="2">
 article. Like they've stated that this
 </span>
 <span data-rw-start="142.319" data-rw-transcript-version="2">
 has resulted in a 500% increase in
 </span>
 <span data-rw-start="144.48" data-rw-transcript-version="2">
 Landed pull requests on some teams, but
 </span>
 <span data-rw-start="146.8" data-rw-transcript-version="2">
 countless devs have converged on similar
 </span>
 <span data-rw-start="148.959" data-rw-transcript-version="2">
 types of systems to this. And OpenAI are
 </span>
 <span data-rw-start="151.36" data-rw-transcript-version="2">
 certainly not the first dev team to
 </span>
 <span data-rw-start="153.04" data-rw-transcript-version="2">
 build orchestration around coding
 </span>
 <span data-rw-start="154.64" data-rw-transcript-version="2">
 agents. I think the most important
 </span>
 <span data-rw-start="156.56" data-rw-transcript-version="2">
 lesson here is unpacking the
 </span>
</p>
<p>
 <span data-rw-start="158" data-rw-transcript-version="2">
 architectural layers that make a system
 </span>
 <span data-rw-start="160" data-rw-transcript-version="2">
 like this work and how we can then make
 </span>
 <span data-rw-start="162" data-rw-transcript-version="2">
 effective use of those systems in our
 </span>
 <span data-rw-start="163.92" data-rw-transcript-version="2">
 own projects. And many of you watching
 </span>
 <span data-rw-start="165.76" data-rw-transcript-version="2">
 this will already know that attempting
 </span>
 <span data-rw-start="167.36" data-rw-transcript-version="2">
 to scale AI coding agents beyond a few
 </span>
 <span data-rw-start="170.08" data-rw-transcript-version="2">
 concurrent chat sessions definitely
 </span>
 <span data-rw-start="172" data-rw-transcript-version="2">
 comes with its own set of challenges. So
 </span>
 <span data-rw-start="174" data-rw-transcript-version="2">
 you may be staring at a coding chat
 </span>
 <span data-rw-start="175.599" data-rw-transcript-version="2">
 window wondering how do I turn this into
 </span>
 <span data-rw-start="177.76" data-rw-transcript-version="2">
 a reliable autonomous agent at scale for
 </span>
 <span data-rw-start="180.239" data-rw-transcript-version="2">
 my project. Or you may want to build
 </span>
 <span data-rw-start="182.159" data-rw-transcript-version="2">
 advanced orchestration features into
 </span>
 <span data-rw-start="184.319" data-rw-transcript-version="2">
 your AI powered apps but you're getting
 </span>
 <span data-rw-start="186.08" data-rw-transcript-version="2">
 lost in the architecture. I'm going to
 </span>
 <span data-rw-start="187.76" data-rw-transcript-version="2">
 share some great mental models and
 </span>
 <span data-rw-start="189.36" data-rw-transcript-version="2">
 resources that I find really useful.
 </span>
</p>
<p>
 <span data-rw-start="191.12" data-rw-transcript-version="2">
 Let's start by clearing up some
 </span>
 <span data-rw-start="192.4" data-rw-transcript-version="2">
 Ambiguity about the term agent harness,
 </span>
 <span data-rw-start="194.319" data-rw-transcript-version="2">
 which at this point could mean many
 </span>
 <span data-rw-start="195.76" data-rw-transcript-version="2">
 different things. As Philip Schmid put
 </span>
 <span data-rw-start="197.519" data-rw-transcript-version="2">
 it, "An agent harness is the
 </span>
 <span data-rw-start="198.959" data-rw-transcript-version="2">
 infrastructure that wraps around an AI
 </span>
 <span data-rw-start="200.8" data-rw-transcript-version="2">
 model."
 </span>
 <span data-rw-start="202.879" data-rw-transcript-version="2">
 As you can see from his clearly
 </span>
 <span data-rw-start="204.879" data-rw-transcript-version="2">
 AI-generated image here, the agent
 </span>
 <span data-rw-start="207.04" data-rw-transcript-version="2">
 harness manages the vast majority of the
 </span>
 <span data-rw-start="208.959" data-rw-transcript-version="2">
 work within our AI systems. And he
 </span>
 <span data-rw-start="211.12" data-rw-transcript-version="2">
 compares the AI model to that of the CPU
 </span>
 <span data-rw-start="213.36" data-rw-transcript-version="2">
 of a computer in that it is very
 </span>
 <span data-rw-start="215.04" data-rw-transcript-version="2">
 important, but it has a very specific
 </span>
 <span data-rw-start="217.28" data-rw-transcript-version="2">
 function.
 </span>
</p>
<p>
 <span data-rw-start="218.72" data-rw-transcript-version="2">
 An LLM is really only able to
 </span>
 <span data-rw-start="220.72" data-rw-transcript-version="2">
 reason about its responses and then
 </span>
 <span data-rw-start="222.319" data-rw-transcript-version="2">
 generate an output such as text.
 </span>
 <span data-rw-start="224.879" data-rw-transcript-version="2">
 Everything beyond that, from the illusion
 </span>
 <span data-rw-start="227.2" data-rw-transcript-version="2">
 of memory and chat history to managing
 </span>
 <span data-rw-start="229.519" data-rw-transcript-version="2">
 sub-agents to actually managing the
 </span>
 <span data-rw-start="231.36" data-rw-transcript-version="2">
 execution of tool calls, that's all
 </span>
 <span data-rw-start="233.2" data-rw-transcript-version="2">
 actually managed within the harness
 </span>
 <span data-rw-start="235.36" data-rw-transcript-version="2">
 code.
 </span>
</p>
<p>
 <span data-rw-start="236.64" data-rw-transcript-version="2">
 So the definition of an agent
 </span>
 <span data-rw-start="238.72" data-rw-transcript-version="2">
 harness is incredibly broad. And to make
 </span>
 <span data-rw-start="240.0" data-rw-transcript-version="2">
 better sense of this, we're going to
 </span>
 <span data-rw-start="242.0" data-rw-transcript-version="2">
 borrow some mental models from Vetta
 </span>
 <span data-rw-start="243.76" data-rw-transcript-version="2">
 Berkeler's great article on harness.
 </span>
</p>
<p>
 <span data-rw-start="240.64" data-rw-transcript-version="2">
 Engineering, where she suggested that we
 </span>
 <span data-rw-start="242.64" data-rw-transcript-version="2">
 should view agent harnesses in two
 </span>
 <span data-rw-start="244.08" data-rw-transcript-version="2">
 separate layers. The first is the inner
 </span>
 <span data-rw-start="246.159" data-rw-transcript-version="2">
 harness. The inner harness is everything
 </span>
 <span data-rw-start="247.84" data-rw-transcript-version="2">
 that ships inside your AI coding agent,
 </span>
 <span data-rw-start="249.92" data-rw-transcript-version="2">
 whether it be cloud code or cursor or
 </span>
 <span data-rw-start="251.92" data-rw-transcript-version="2">
 codecs. Of course, they're very powerful
 </span>
 <span data-rw-start="253.84" data-rw-transcript-version="2">
 out of the box already. They ship inside
 </span>
 <span data-rw-start="256" data-rw-transcript-version="2">
 with the ability to manage sub-agents,
 </span>
 <span data-rw-start="258.239" data-rw-transcript-version="2">
 sandbox code execution, skills, hooks,
 </span>
 <span data-rw-start="260.88" data-rw-transcript-version="2">
 tools, permissions, and more. But as
 </span>
 <span data-rw-start="263.36" data-rw-transcript-version="2">
 Brigitta writes in this article, to let
 </span>
 <span data-rw-start="265.6" data-rw-transcript-version="2">
 coding agents work with less
 </span>
 <span data-rw-start="266.96" data-rw-transcript-version="2">
 supervision, we need ways to increase
 </span>
 <span data-rw-start="268.8" data-rw-transcript-version="2">
 our confidence in their result. But how
 </span>
 <span data-rw-start="270.96" data-rw-transcript-version="2">
 exactly do we do that? As a starting
 </span>
 <span data-rw-start="272.96" data-rw-transcript-version="2">
 point, we can try and give our coding
 </span>
 <span data-rw-start="274.8" data-rw-transcript-version="2">
 agents better context of the overall
 </span>
 <span data-rw-start="276.88" data-rw-transcript-version="2">
 codebase. We can try and convince them
 </span>
 <span data-rw-start="279.04" data-rw-transcript-version="2">
 to do a better job via better prompting.
 </span>
</p>
<p>
 <span data-rw-start="281.52" data-rw-transcript-version="2">
 And we can also use meta prompting
 </span>
 <span data-rw-start="283.36" data-rw-transcript-version="2">
 frameworks such as superpowers or GSD
 </span>
 <span data-rw-start="285.52" data-rw-transcript-version="2">
 version one or VMAD. And those things
 </span>
 <span data-rw-start="287.6" data-rw-transcript-version="2">
 absolutely help, but they only go so
 </span>
 <span data-rw-start="289.36" data-rw-transcript-version="2">
 far. And that's where the real
 </span>
 <span data-rw-start="290.8" data-rw-transcript-version="2">
 Engineering of the outer harness comes
 </span>
 <span data-rw-start="292.56" data-rw-transcript-version="2">
 into play. Coding agents such as Claude
 </span>
 <span data-rw-start="294.72" data-rw-transcript-version="2">
 or Codeex expose features that let us
 </span>
 <span data-rw-start="297.199" data-rw-transcript-version="2">
 build an outer harness around them. And
 </span>
 <span data-rw-start="299.199" data-rw-transcript-version="2">
 these harnesses are actual code that
 </span>
 <span data-rw-start="300.96" data-rw-transcript-version="2">
 controls the agent lifecycle
 </span>
 <span data-rw-start="302.479" data-rw-transcript-version="2">
 programmatically. So, instead of using a
 </span>
 <span data-rw-start="304.4" data-rw-transcript-version="2">
 meta prompting framework where we might
 </span>
 <span data-rw-start="306.96" data-rw-transcript-version="2">
 ask the AI agent to reset the context,
 </span>
 <span data-rw-start="309.759" data-rw-transcript-version="2">
 the outer harness can actually
 </span>
 <span data-rw-start="311.039" data-rw-transcript-version="2">
 deterministically terminate the session,
 </span>
</p>
<p>
 <span data-rw-start="313.039" data-rw-transcript-version="2">
 clear the context, read the task state
 </span>
 <span data-rw-start="315.12" data-rw-transcript-version="2">
 from disk, inject the relevant files,
 </span>
 <span data-rw-start="317.199" data-rw-transcript-version="2">
 and then work from there. So, Ralph loops
 </span>
 <span data-rw-start="319.44" data-rw-transcript-version="2">
 or projects like Gas Town or Archon are
 </span>
 <span data-rw-start="321.84" data-rw-transcript-version="2">
 all examples of systems that act as
 </span>
 <span data-rw-start="323.919" data-rw-transcript-version="2">
 outer harnesses. In this article, it
 </span>
 <span data-rw-start="325.68" data-rw-transcript-version="2">
 said that the harness acts like a
 </span>
 <span data-rw-start="327.28" data-rw-transcript-version="2">
 cybernetic governor, combining feed
 </span>
 <span data-rw-start="329.52" data-rw-transcript-version="2">
 forward and feedback to regulate the
 </span>
 <span data-rw-start="331.52" data-rw-transcript-version="2">
 codebase towards the desired state. That
 </span>
 <span data-rw-start="334" data-rw-transcript-version="2">
 feedback mechanism is one of the most
 </span>
 <span data-rw-start="335.84" data-rw-transcript-version="2">
 important parts of this process. There's
 </span>
 <span data-rw-start="337.6" data-rw-transcript-version="2">
 a very useful distinction between guides
 </span>
 <span data-rw-start="339.44" data-rw-transcript-version="2">
 and sensors here, where the guides help
 </span>
 <span data-rw-start="341.6" data-rw-transcript-version="2">
 Steer the agent in the right direction.
 </span>
</p>
<p>
 <span data-rw-start="343.36" data-rw-transcript-version="2">
 So, these are anything that tries to make
 </span>
 <span data-rw-start="345.12" data-rw-transcript-version="2">
 the agent's first attempt better. So, your
 </span>
 <span data-rw-start="347.6" data-rw-transcript-version="2">
 agent might read from an agent's MD file,
 </span>
 <span data-rw-start="349.68" data-rw-transcript-version="2">
 or you may provide skills and playbooks,
 </span>
 <span data-rw-start="351.759" data-rw-transcript-version="2">
 and examples that they can work from.
 </span>
 <span data-rw-start="353.6" data-rw-transcript-version="2">
 But the AI agent is not always going to
 </span>
 <span data-rw-start="355.68" data-rw-transcript-version="2">
 get things right, and even if so, not
 </span>
 <span data-rw-start="357.919" data-rw-transcript-version="2">
 necessarily according to your own
 </span>
 <span data-rw-start="359.36" data-rw-transcript-version="2">
 behaviors and rules. And that's where the
 </span>
 <span data-rw-start="361.28" data-rw-transcript-version="2">
 very important feedback loop comes in.
 </span>
</p>
<p>
 <span data-rw-start="363.199" data-rw-transcript-version="2">
 And these are referred to as sensors. So,
 </span>
 <span data-rw-start="365.52" data-rw-transcript-version="2">
 we might have deterministic
 </span>
 <span data-rw-start="367.52" data-rw-transcript-version="2">
 computational-based sensors such as
 </span>
 <span data-rw-start="369.44" data-rw-transcript-version="2">
 linters, types, and schemas. So, for
 </span>
 <span data-rw-start="371.6" data-rw-transcript-version="2">
 example, whenever your coding agent
 </span>
 <span data-rw-start="373.6" data-rw-transcript-version="2">
 creates code, you can run those through
 </span>
 <span data-rw-start="376.08" data-rw-transcript-version="2">
 deterministic checks,
 </span>
 <span data-rw-start="378.56" data-rw-transcript-version="2">
 without using AI at
 </span>
 <span data-rw-start="380.24" data-rw-transcript-version="2">
 all, and then feed that back to the
 </span>
 <span data-rw-start="382" data-rw-transcript-version="2">
 model. And one of the main arguments
 </span>
 <span data-rw-start="383.919" data-rw-transcript-version="2">
 made within this article is that these
 </span>
 <span data-rw-start="386.479" data-rw-transcript-version="2">
 computational type checks are heavily
 </span>
 <span data-rw-start="389.039" data-rw-transcript-version="2">
 underused by AI builders. Of course, you
 </span>
 <span data-rw-start="390.96" data-rw-transcript-version="2">
 can also have sensors powered by AI,
 </span>
 <span data-rw-start="392.96" data-rw-transcript-version="2">
 known as inferential sensors, such as you.
 </span>
</p>
<p>
 <span data-rw-start="393.199" data-rw-transcript-version="2">
 Can feed code generated by an LLM into
 </span>
 <span data-rw-start="395.759" data-rw-transcript-version="2">
 another call to an LLM, ideally another
 </span>
 <span data-rw-start="398.16" data-rw-transcript-version="2">
 model where it can act as a judge,
 </span>
 <span data-rw-start="399.919" data-rw-transcript-version="2">
 and then that can be fed back into the model,
 </span>
 <span data-rw-start="402.24" data-rw-transcript-version="2">
 and humans then continuously steer and
 </span>
 <span data-rw-start="404.56" data-rw-transcript-version="2">
 optimize the components of this outer
 </span>
 <span data-rw-start="406.4" data-rw-transcript-version="2">
 harness. If we go back to our OpenAI
 </span>
 <span data-rw-start="408.4" data-rw-transcript-version="2">
 article on harness engineering, they've
 </span>
 <span data-rw-start="410.08" data-rw-transcript-version="2">
 run with this type of concept where the
 </span>
 <span data-rw-start="412.16" data-rw-transcript-version="2">
 agent is called in a Ralph Wigum loop,
 </span>
 <span data-rw-start="414.4" data-rw-transcript-version="2">
 until all human reviewers are satisfied.
 </span>
</p>
<p>
 <span data-rw-start="416.96" data-rw-transcript-version="2">
 Running an external Ralph Wigum loop,
 </span>
 <span data-rw-start="419.199" data-rw-transcript-version="2">
 not the one built into Claude code
 </span>
 <span data-rw-start="420.72" data-rw-transcript-version="2">
 directly, by the way, is a very simple
 </span>
 <span data-rw-start="422.56" data-rw-transcript-version="2">
 example of an outer harness. It just
 </span>
 <span data-rw-start="424.96" data-rw-transcript-version="2">
 keep spawning Claude sessions again and
 </span>
 <span data-rw-start="426.88" data-rw-transcript-version="2">
 again through brute force
 </span>
 <span data-rw-start="428.88" data-rw-transcript-version="2">
 iteration until a certain goal has been
 </span>
 <span data-rw-start="430.8" data-rw-transcript-version="2">
 met. And other outer harnesses can just
 </span>
 <span data-rw-start="432.88" data-rw-transcript-version="2">
 take this thin orchestrator concept as a
 </span>
 <span data-rw-start="435.44" data-rw-transcript-version="2">
 starting point and bring it many steps
 </span>
 <span data-rw-start="437.599" data-rw-transcript-version="2">
 further and potentially in many
 </span>
 <span data-rw-start="439.199" data-rw-transcript-version="2">
 different directions. Archon is a great
 </span>
 <span data-rw-start="441.12" data-rw-transcript-version="2">
 example of a tool that allows you to
 </span>
 <span data-rw-start="442.72" data-rw-transcript-version="2">
 create your own outer harnesses which
 </span>
 <span data-rw-start="444.639" data-rw-transcript-version="2">
 Can enforce your agents to act in a
 </span>
 <span data-rw-start="446.479" data-rw-transcript-version="2">
 certain deterministic way. It already
 </span>
 <span data-rw-start="448.479" data-rw-transcript-version="2">
 includes a lot of out-of-the-box
 </span>
 <span data-rw-start="449.919" data-rw-transcript-version="2">
 workflows, and it even allows for
 </span>
 <span data-rw-start="451.599" data-rw-transcript-version="2">
 parallel executions of tasks. We use
 </span>
 <span data-rw-start="454" data-rw-transcript-version="2">
 this inner-outer harness distinction as
 </span>
</p>
<p>
 <span data-rw-start="455.84" data-rw-transcript-version="2">
 a mental model not only for coding
 </span>
 <span data-rw-start="457.599" data-rw-transcript-version="2">
 agents but also for agentic systems we
 </span>
 <span data-rw-start="459.759" data-rw-transcript-version="2">
 build. In our full stack AI builder
 </span>
 <span data-rw-start="461.84" data-rw-transcript-version="2">
 series, Daniel walks through the
 </span>
 <span data-rw-start="463.36" data-rw-transcript-version="2">
 creation of a contract review harness,
 </span>
 <span data-rw-start="465.039" data-rw-transcript-version="2">
 that adds deterministic aspects to the
 </span>
 <span data-rw-start="467.199" data-rw-transcript-version="2">
 agentic workflow. And this can
 </span>
 <span data-rw-start="468.96" data-rw-transcript-version="2">
 essentially be seen as an outer harness,
 </span>
 <span data-rw-start="470.96" data-rw-transcript-version="2">
 a configurable aspect that's layered on
 </span>
 <span data-rw-start="473.039" data-rw-transcript-version="2">
 top of the inner harness core
 </span>
 <span data-rw-start="474.72" data-rw-transcript-version="2">
 functionality of the agentic system. It
 </span>
 <span data-rw-start="476.96" data-rw-transcript-version="2">
 can have guides and sensors that are
 </span>
 <span data-rw-start="478.319" data-rw-transcript-version="2">
 automatically fed back into the agent,
 </span>
 <span data-rw-start="480.56" data-rw-transcript-version="2">
 such as automated computational document
 </span>
 <span data-rw-start="482.72" data-rw-transcript-version="2">
 checks that don't use AI at all, as well
 </span>
 <span data-rw-start="485.36" data-rw-transcript-version="2">
 as inferential checks, such as LLM as a
 </span>
 <span data-rw-start="487.52" data-rw-transcript-version="2">
 judge. And these harnesses will lie on a
 </span>
 <span data-rw-start="489.36" data-rw-transcript-version="2">
 spectrum between either being very
 </span>
 <span data-rw-start="490.8" data-rw-transcript-version="2">
 deterministic or very probabilistic.
 </span>
</p>
<p>
 <span data-rw-start="493.199" data-rw-transcript-version="2">
 That contract review harness tends to
 </span>
 <span data-rw-start="495.039" data-rw-transcript-version="2">
 follow a very specific workflow. But
 </span>
 <span data-rw-start="497.52" data-rw-transcript-version="2">
 many other harnesses will be a lot more
 </span>
 <span data-rw-start="499.36" data-rw-transcript-version="2">
 open-ended, such as deep research
 </span>
 <span data-rw-start="501.039" data-rw-transcript-version="2">
 harnesses. And these are essentially the
 </span>
 <span data-rw-start="503.039" data-rw-transcript-version="2">
 opposite shape. They're broad,
 </span>
 <span data-rw-start="504.639" data-rw-transcript-version="2">
 open-ended, and agentic throughout, but
 </span>
 <span data-rw-start="507.12" data-rw-transcript-version="2">
 they can still have plenty of
 </span>
 <span data-rw-start="508.16" data-rw-transcript-version="2">
 deterministic scaffolding around them,
 </span>
 <span data-rw-start="510.24" data-rw-transcript-version="2">
 such as computational checking of
 </span>
 <span data-rw-start="512.24" data-rw-transcript-version="2">
 citations or multiple layers of LM
 </span>
 <span data-rw-start="514.959" data-rw-transcript-version="2">
 reviews before they’re passed back for
 </span>
 <span data-rw-start="516.8" data-rw-transcript-version="2">
 human review. As we start building upon
 </span>
 <span data-rw-start="518.88" data-rw-transcript-version="2">
 the scaffolding on top of our AI agents,
 </span>
 <span data-rw-start="521.12" data-rw-transcript-version="2">
 you may even consider that they start
 </span>
 <span data-rw-start="522.719" data-rw-transcript-version="2">
 becoming their own layer on top of the
 </span>
 <span data-rw-start="525.2" data-rw-transcript-version="2">
 mental model we've talked about already.
 </span>
 <span data-rw-start="527.04" data-rw-transcript-version="2">
 And this layer could be seen as the
 </span>
 <span data-rw-start="528.56" data-rw-transcript-version="2">
 overarching orchestrator or scheduler
 </span>
 <span data-rw-start="531.12" data-rw-transcript-version="2">
 layer. And that's very much where OpenAI
 </span>
 <span data-rw-start="533.12" data-rw-transcript-version="2">
 positions systems created using their
 </span>
 <span data-rw-start="535.36" data-rw-transcript-version="2">
 new symphony spec as this is really
 </span>
 <span data-rw-start="537.519" data-rw-transcript-version="2">
 multi-agent orchestration at a higher
 </span>
 <span data-rw-start="539.6" data-rw-transcript-version="2">
 level. These are all mental models and
 </span>
 <span data-rw-start="541.6" data-rw-transcript-version="2">
 metaphors. They just help our general
 </span>
</p>
<p>
 <span data-rw-start="543.6" data-rw-transcript-version="2">
 Understanding of the concepts and the
 </span>
 <span data-rw-start="545.36" data-rw-transcript-version="2">
 lines can very much be blurred between
 </span>
 <span data-rw-start="547.279" data-rw-transcript-version="2">
 them. For example, Gas Town is an
 </span>
 <span data-rw-start="549.2" data-rw-transcript-version="2">
 orchestration framework where it takes
 </span>
 <span data-rw-start="550.959" data-rw-transcript-version="2">
 the concept of a Ralph Wiggum loop have
 </span>
 <span data-rw-start="553.2" data-rw-transcript-version="2">
 many of them running at once along with
 </span>
 <span data-rw-start="555.2" data-rw-transcript-version="2">
 automated orchestration around those
 </span>
 <span data-rw-start="557.04" data-rw-transcript-version="2">
 instances. And this can certainly get
 </span>
 <span data-rw-start="558.959" data-rw-transcript-version="2">
 quite chaotic. But frameworks like this
 </span>
 <span data-rw-start="561.36" data-rw-transcript-version="2">
 are trying to solve the problem of
 </span>
 <span data-rw-start="562.72" data-rw-transcript-version="2">
 getting many agents to work reliably in
 </span>
 <span data-rw-start="564.959" data-rw-transcript-version="2">
 parallel. And the two biggest issues
 </span>
 <span data-rw-start="567.519" data-rw-transcript-version="2">
 that people face other than their
 </span>
 <span data-rw-start="569.2" data-rw-transcript-version="2">
 intense token usage and AI builds with
 </span>
 <span data-rw-start="571.76" data-rw-transcript-version="2">
 systems like this is twofold. It's
 </span>
 <span data-rw-start="573.839" data-rw-transcript-version="2">
 making AI agents work reliably together
 </span>
 <span data-rw-start="575.76" data-rw-transcript-version="2">
 without clashing and adding in the
 </span>
 <span data-rw-start="577.839" data-rw-transcript-version="2">
 correct human in the loop layers where
 </span>
 <span data-rw-start="579.68" data-rw-transcript-version="2">
 humans are in the most important parts
 </span>
 <span data-rw-start="581.519" data-rw-transcript-version="2">
 of the process without micromanaging
 </span>
 <span data-rw-start="584" data-rw-transcript-version="2">
 everything because that becomes the
 </span>
 <span data-rw-start="585.519" data-rw-transcript-version="2">
 biggest bottleneck and again that's
 </span>
 <span data-rw-start="587.04" data-rw-transcript-version="2">
 where we come back to this Symfony spec.
 </span>
</p>
<p>
 <span data-rw-start="589.04" data-rw-transcript-version="2">
 Symfony started with a concept that any
 </span>
 <span data-rw-start="591.04" data-rw-transcript-version="2">
 open task should get picked up and
 </span>
 <span data-rw-start="593.2" data-rw-transcript-version="2">
 Completed by an agent instead of
 </span>
 <span data-rw-start="595.04" data-rw-transcript-version="2">
 developers managing codec sessions in
 </span>
 <span data-rw-start="597.12" data-rw-transcript-version="2">
 multiple tabs. They made this issue
 </span>
 <span data-rw-start="599.12" data-rw-transcript-version="2">
 tracker in linear and use that as the
 </span>
 <span data-rw-start="601.36" data-rw-transcript-version="2">
 human interface. Those tickets then
 </span>
 <span data-rw-start="603.279" data-rw-transcript-version="2">
 trigger the coding agent to work
 </span>
 <span data-rw-start="604.72" data-rw-transcript-version="2">
 autonomously on those tasks as required
 </span>
 <span data-rw-start="606.88" data-rw-transcript-version="2">
 and then report back to the user when
 </span>
 <span data-rw-start="608.959" data-rw-transcript-version="2">
 required. If you want to get started
 </span>
 <span data-rw-start="610.48" data-rw-transcript-version="2">
 with the Symfony open-source spec, it's
 </span>
 <span data-rw-start="612.72" data-rw-transcript-version="2">
 available on the GitHub repo linked
 </span>
 <span data-rw-start="614.399" data-rw-transcript-version="2">
 below. And you can get your own coding
 </span>
 <span data-rw-start="616" data-rw-transcript-version="2">
 agent to create an orchestration system
 </span>
 <span data-rw-start="617.76" data-rw-transcript-version="2">
 based on this spec in whatever language
 </span>
 <span data-rw-start="619.839" data-rw-transcript-version="2">
 you want, or you can also use their
 </span>
</p>
<p>
 <span data-rw-start="621.6" data-rw-transcript-version="2">
 out-of-the-box demo example. In this
 </span>
 <span data-rw-start="623.68" data-rw-transcript-version="2">
 video, we went through a lot of AI
 </span>
 <span data-rw-start="625.44" data-rw-transcript-version="2">
 architecture concepts. If you found that
 </span>
 <span data-rw-start="627.44" data-rw-transcript-version="2">
 useful, you should definitely check out
 </span>
 <span data-rw-start="629.04" data-rw-transcript-version="2">
 our AI architects course linked below,
 </span>
 <span data-rw-start="631.44" data-rw-transcript-version="2">
 which will help give you a deeper
 </span>
 <span data-rw-start="632.72" data-rw-transcript-version="2">
 understanding of AI systems, technical
 </span>
 <span data-rw-start="634.56" data-rw-transcript-version="2">
 foundations, harness engineering,
 </span>
 <span data-rw-start="636.399" data-rw-transcript-version="2">
 agentic retrieval, and more. And if you
 </span>
 <span data-rw-start="638.48" data-rw-transcript-version="2">
 like this video, you'll love the
 </span>
 <span data-rw-start="639.839" data-rw-transcript-version="2">
 Previous video on our channel where
 </span>
 <span data-rw-start="641.36" data-rw-transcript-version="2">
 Daniel goes through a deep dive into the
 </span>
 <span data-rw-start="643.44" data-rw-transcript-version="2">
 various agent frameworks and services
 </span>
 <span data-rw-start="645.36" data-rw-transcript-version="2">
 you can use when building out AI
 </span>
 <span data-rw-start="647.12" data-rw-transcript-version="2">
 systems.
 </span>
</p>