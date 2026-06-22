---
title: "Pi to Pi: Two-Way Agent Orchestration with the Pi Coding Agent"
source: "https://www.youtube.com/watch?v=PIdETjcXNIk"
author: "IndyDevDan"
published: 2026-05-18
created: 2026-06-06
description: "Subagents are the LOCAL MAXIMUM of multi-agent orchestration and most engineers\"
tags:
  - to-process
  - orchestration
---

What's up engineers? Indie Dev Dan here. I have a simple question for you. What's better than one GPT 5.5 Pi coding agent? You guessed it, two GPT 5.5 Pi coding agents. Let's push it further. What's better than two isolated side-by-side GPT 5.5 agents? Sure, you could add another agent. Sure, you could change the model, but we can do much better than this. What about two GPT 5.5 agents that actually work together? 

What about three agents that work together with unique models? What about four models? So, here we have four Pi coding agents and none of them is the orchestrator. Instead, they're equals. They're co-workers pinging every agent. In this video, we'll understand what type of agentic engineering we can achieve if we gave our agents a true two-way communication channel. By the end of this video, you'll have a simple 

yet powerful way to coordinate your multi-agent systems. This gives us a powerful flat agent hierarchy where the best information wins, where the best ideas win, and where your agents can truly coordinate together to outperform each other alone. Let's talk about Pi-to-Pi two-way agent communication. So, let's go ahead and reset here. Let's de-hype this a little bit. Let's close 

our agents. As you can see, one by one as we close them, they leave the chat room. They leave the communication pool. We've got a production database on my Mac mini. And this production database has an issue. Some ProTier users are getting locked out of pro features. So, in order to fix this issue, I need to reproduce it on my local developer environment. This is a common engineering workflow. You don't fix things in production, and fix things on your developer environment, and then you deploy through staging, and then eventually it hits production. The trick 

here is there is sensitive information on my Mac mini production environment here, and I can't leak any PII while I'm fixing this issue. We're not live coding here, we're doing real engineering work in production systems. Our pie-to-pie agent-to-agent communication system is perfect for this. So, I'll boot up two agents here, one on my Mac mini, the production server, and one on my M5 MacBook Pro, my dev machine. We'll do J coms two, and we'll give this a name. This is going to be production. J coms 

one, name dev. We'll run some basic pings to make sure both agents are up and online. And then we're going to paste in a production prompt here. This is a prod gatekeeper agent. It has a production database it's working with that's been seeded. We're not going to recreate it or anything. And you have a team name. And then key piece here, we have PII inside of this production code base that we're not going to break. This is personal identifiable information. So, our production agent understands the system, it understands what's available, and it knows that it's not going to 

expose any information to any other agent on the network, okay? And now our developer agent is going to get to work. We need to reproduce this issue locally. Here's our developer prompt. The key here is this. Bring the affected slice from production over with PII stripped into your local dev DB so an engineer can reproduce the issue locally. First, in order to reproduce a production database issue, you need the production data. Here's where the magic happens. Our agent sees the peer on the network, 

right? It knows that it has connection to a prod agent, and now it's going to start working through things. So, it's going to send a message, it's going to send a prompt, and it's going to get returned an ID, a message ID. Our agent can now await this message, and our production agent, as you can see here, is getting to work on the production side. But it's getting to work with all redactions applied, right? It's not going to expose any personal identifiable information. Our agent is going to work back and forth here, not as individual agents, not as a sub 

agent, not as workers, right? They're going to work together as a team. It's a simple, beautiful pattern, and it really reflects how great work is done. And so, our agent is learning about the local DB. It's making sure that it's clean, and it's starting to sync things while keeping everything PII safe, right? So, this is yet another place where if you engineer things properly, if you prompt things properly, you can do extraordinary things in your agentic systems. There are endless use cases for 

agents that actually communicate and work together. You can see there we got another message back, and this process is going to continue. So, we're going to let our agents cook here. I want to take the time to like highlight why agent-to-agent communication is so important, and highlight, of course, once again, why the Pi Coding Agent is really the only way that you get this level of control out of your agents here. I think the most important thing to 

start with here is understanding the current problem, right? Agents can't talk to each other. We know that there is sub agent delegation and sub agent prompting, right? And this is a great pattern. It's a great start. Like if you agree with this statement, we are just scratching the surface of what the true developer experience looks like for agentic engineering, right? We don't really even know what that form factor is. I think very clearly in terminal agents the center point, but everything around 

that from the agent harness to how we manage contexts, models, agent scale, tools, this is all a work in progress. So, if we're not exploring the state space of what's possible with our agent communication and other agentic workflows and patterns, uh we're going to be stuck in the normal distribution, the very beginning of what's possible. So, sub agents, very important, very cool, but this is just the beginning, right? When you push further, you can find a message queue, and this is what the Cloud Code agent teams uses. So, you have one agent that kind of sets up all 

the message queue, and then it serves as a message broker between agents. Another great powerful pattern. You then have things like agent chains, where you have a deterministic set up workflow that have individual nodes of agents. When you combine this with code, you get powerful AI developer workflows or blueprints or representations of agents plus code. This is a very, very powerful framework, because it adds determinism into the process, right? At any one of these steps, you can insert code, and it'll enhance what your agents can do. 

So, very powerful stuff here, right? But, um there's a problem with this. As you can see, in every one of these workflows, it is traveling information in basically one direction, and it's always a top-down way. Even if the information comes back, it's a one-way stream, right? It's never bidirectional. So, what's the solution? It's quite simple. Let your agents talk to each other, right? Prompt response, and then prompt response, okay? Peer-to-peer, not orchestrator-to-worker, changes things. Here, agents are equals. 

They're not parent and child, and this unlocks, of course, bidirectional flows of information, okay? Just two agents communicating to each other. As you can see here, our agents are still working together to figure out these issues, to really work through how to perfectly reproduce the production slice. But, you can push this across devices and across multiple agents, right? And this looks like exactly what you'd imagine, right? Now, we have three agents in the network. You might have a researcher, coder, planner. These can be anything 

under the sun. In our case, we have a prod agent, and we have a developer agent talking to each other across the network, okay? But, you can just keep scaling this up, right? And at some point, it's going to be uh harmful, right? Like there is a limit to how useful this is. Um I'm not just trying to sell you the upside here. There's downsides to every approach. Great engineering is all about managing tradeoffs. At some level, you're not going to want to use this pattern anymore. And at some level, adding agents doesn't help anything. But, there 

is certainly a useful level to this where you want to have bidirectional agent-to-agent communication, where it's very, very useful to have every agent have access to every other agent, okay? And so, why is this useful, right? Let's let's really hit on this. Like I think at the core of this, it comes down to information hierarchies. If you have a traditional software engineering job, you work at a company that has a hierarchy, right? For one reason or another, there is someone at the top, okay? And information usually travels downstream, commands travel downstream, 

objectives travel downstream, and then it hits the person, usually the engineers, who are actually building the thing, right? And oftentimes, the best information, the best decisions, the best awareness about the system is all the way down here, right? It's on the worker level, right? It's It's you and I, the engineers with their boots on the ground every single day, putting in the work to understand the system, understand the objectives, and then actually building it, right? The best information is often times down here. When you have these hierarchical information systems, and I'm speaking in 

a generic way, it doesn't just need to be about the job. It doesn't just need to be in a career setting. But, just information structures like this, often times the best ideas are down here. They get stuck down here because they don't have the right title, they don't have the right authority, they don't have the right say, right? And you've, you know, you've probably heard this, right? But, the best companies, the best structures are flat, where there's communication happening on every single level, where everyone can just talk to the other to get the job done, right? Nvidia is 

really famous for this, very flat reporting structures. Of course, Jensen at the top, commanding that insane company. But, then he has uh very few direct reports, and then it spans from there, right? But, startups are famous for this, right? You have very, very flat structures. All the best information systems are flat. Why is that? It's because you get valuable information wins always over titles and politics, okay? Ideas die in hierarchies. So, that's why this is so important. And And, you know, maybe you 

think I'm anthropomorphizing this too much. Maybe you think I am trying to apply something where it doesn't belong. I completely disagree. I think when you really boil things down, everything is a system. And a key part about every system is that there is flows of information inside of systems, and how things flow, how the structures, the nodes, and the actors in the system communicate information matters, right? This matters because oftentimes the best ideas are down here. They're at the bottom level. And so, this means that as 

much as you can, you want to have flat hierarchy structures, okay? But, on a functional level, we can see that this is uh useful for other reasons as well. We have cross-device agent-to-agent communication, right? We have a production service. Say this is in the EU, right? Where everything has to be redacted, everything has to be perfect, and nothing can escape the device. But, you still need to fix things, right? We still need to do real engineering work. So, this is a great system. We have redacted information properly, transferred it to our developer machine. 

And as you can see here, the repro is ready, the bug has been imported, okay? PII is clean, okay? So, legitimate engineering work happening here. Obviously, this is not a real production server. I'm using this as an example. And now I can go ahead, debug, look at my code, look at this slice of the production database that has been reproduced from production. And now I can actually resolve the bug. And our agents are really great at communicating information like this. And that's exactly what they've done, okay? So, we have very simple two-way bidirectional 

agent-to-agent communication. If I needed to, I could come in here and validate that everything looks good on the production agent side, right? Do one final check with the dev agent PRI safe. The issue has been repro'd. We can talk to any side that we need to, and they can then communicate together to get the job done. So, I hope you can see the value proposition of this. I hope you can see why agent-to-agent communication is useful, even if you don't think that the flat information hierarchies are more performant for making sure that the best ideas are the ones that always win. 

This is great because now we have simple multi-agent communication on different devices, okay? And whenever we need to, you know, let me just be clear about this. Whenever we need to, I can add an agent to the pool. So, if I type J Comms, let's use four, I think that's the GLM agent. You can see GLM added here, and now it is part of the pool, right? So, fantastic. How else can we use this? Agent-to-agent communication, it seems very powerful. We're not just delegating work, which is in its own right a very powerful communication pattern, right? This isn't a replacement. This is another option for 

your agentic engineering. We can solve other problems with it, right? Let let let's walk through another example. So, let's fire up a E2B agent. And in fact, let's open up a new project here, sandbox. Same deal, J Comms 2, and name EXC dev agent project sandbox. So, we're just getting our agents off this network. This is a different pool to communicate in, right? So, we still 

still have our previous set there. And you can actually see that this work here was done. PII is safe. All the findings are there. So, we verified by having our production agent prompt our developer agent. Fantastic. There we got the pass. Everything looks great. Both context windows are sharp and focused. There's no spillover between issues. This system has completed successfully. So, I've been using the E2B agent sandbox tool for quite some time now. It's been a great tool. It's also expensive, and it has some downsides like there's a limit to the total duration that you can have 

your agents up in a sandbox. You have to pause them to manage that. So, I've been looking at exe.dev as a new agent sandbox tool to replace or use additionally right next to e2b. And so, this is another agent sandbox tool. It's got a couple of different benefits. I'll link both of these in the description for you. But, the idea here is I already have my e2b agent in this sandbox skill, right? So, I have agent sandboxes and this is my e2b skill where I can just quickly spin up an agent sandbox that my agent can fully own and operate on my 

behalf. We've talked about agent sandboxes on the channel in the past. I'll link those in the description for you as well. But, what I want to do here is spin up a brand new skill for exe.dev that mirrors and matches and has feature parity to my e2b agent skill. And anything that doesn't match, I want to know about it, right? I want to understand the feature differences, but I want my agent to fail forward. the skill to be built so that I can prototype and experiment with it right away, okay? So, I don't just want a simple research comparison. I want a new 

skill I can use that has feature parity with my existing skill. That's exactly what I'm going to prompt here. In my e2b agent, I'm going to fire this off. You're the e2b agent. Your teammate is exe.dev. They'll be building this skill against exe.dev's persistent VM platform. Your job is to answer their questions, okay? So, we have a teammate set up specifically to understand this feature set. It's putting up a sandbox. It's reminding itself of all the features. And when this completes, I'm going to kick off the exe.dev agent to 

communicate, work with, and sync up a brand new skill. You know, a lot of the agent-to-agent communication and multi-agent orchestration comes down to expanding your context window in a useful way such that your agents can specialize what they're focused on, okay? A lot of engineers do think that you just throw everything in one agent, wait for for models to get better, wait for that 5 million contacts window, and then all your problems will be solved. I don't agree with this approach at all. I think you should lean on the models, you should expect them to get better, you 

should plan for that in your products and services, but at the same time you should be learning how to focus your agents on one problem so that the chance that they cause an issue, so that the chance something goes wrong drops down to near zero. And how can you do that? You can do that by having focused context windows, okay? And by effectively specializing your agent to focus on one problem and one problem only. Spinning up and comparing two different tools with likely very similar APIs is going to get the context window pretty big. You can see here this agent 

is loading, refreshing itself on all of the E2B agent skill functionality, right? You can see sandbox remove, download dir, so on and so forth. We're almost at 10% context already. That's 100k tokens, okay? If you're using agents on a daily basis, you understand this fact, right? A focused agent is a performant agent. you add to that context window, the higher the chance something goes wrong is. Specifically, when you start muddying unrelated context together, okay? This is the art 

of context engineering. It's not just getting all the right things, it's getting just the right things. This agent's booting up, it should be complete pretty soon here, and then we can prompt our exe.dev to create this new skill so that we can boot up brand new sandboxes for exe.dev, and we can really see what this is all about. Moving forward, it's not just about these two sandbox tools, right? It's about every sandbox tool moving forward and our ability to deploy agents to understand the tools, to understand the technology, and then deploy them into 

valuable use cases on our behalf. So, we can use this system over and over and over, we can compare the features between every specialized agent. I hope you get the point, right? If this is all making sense, you know, make sure you drop a like. This is like really our bread and butter on the channel. We're scaling our compute to scale our impact. It's all about scaling up what our agents can do and focusing our agents to solve real business problems on our behalf via agentic engineering, not vibe coding. We're not shooting prompts and not looking. We know what our agents are 

doing, okay? And this just stacks up on previous videos we've had on the channel where we're making our agents secure. We're not letting them crush production assets when they should not be able to. We're adding security to our bash tool when they need it. Just like in last week's video, we're preventing catastrophic commands from running. And then, you know, we're letting our agents rip on all the tools, all the skills, all the commands that we actually want our agents to execute, right? As you can see here, a lot of that sandbox tool 

running, our agent is understanding what it can do here. And soon it's going to write this uh presentation file for us. And this is one of the great things and one of the annoying things about GPT 5.5. This model really chews up tokens and it just goes and goes and goes to really get you the most comprehensive result possible. Whereas, I found that Opus 4.7 will do that as well, but it also will really just focus on the goal, right? I think Opus is more goal-oriented and really focuses on accomplishing the goal. If you prompt it wide enough to capture more of that 

state, more of that scope, it'll certainly capture that as well, okay? But here we go. We're getting that inventory file that really compresses all the observations. Now, we should be able to kick off our exe.dev agent pretty soon here. There we go. Nice write-up. Look at that detailed write-up of all the features, inputs, and outputs, the commands, E2B quirks, right? This is great. And this was part of the prompt, right? We wanted at the end a feature inventory. And this is going to allow our exe.dev agent to really map everything out one-to-one. And again, like focus context is so 

important here, right? In tactically agentic coding, it's so important. This is an entire tactic. We talk about this for an entire lesson. A focused agent is a performant agent. We have 20% context of the 1 million context window GPT 5.5 focus on just understanding this tool and understanding this skill and this whole sandbox system. Okay, so there you go. Validating its work, making sure that that file exists and now we're going to boot up our exe.dev agent. There we go, perfect. So, it's all primed, it's all good to go. Now we're 

going to fire off this prompt inside of our exe.dev agent. I actually haven't run this before so I'm really curious to see how how this executes and how well this mirrors. So, you're the exe.dev agent. There is no agent sandbox exe.dev skill yet. Your job is to build one. Okay, so there's the purpose and then your reference target is this existing skill here which your teammate understands is already standing by to answer questions about. You're the driver of this collaboration. E2B will not initiate, you reach out. So, I'm setting this up so that in this specific scenario, I want my exe.dev agent to be 

the one driving this. I'm giving it a couple skills, fire crawl, meta skill to really build on this and then we have our clear deliverable. So, I want that new skill, right? And I'm making it super clear here, a new working skill that mirrors the {slash} agent sandbox is against exe.dev primitives and I also want a feature parity document just like the E2B agent has as well for us, okay? And so, it's starting to get to work here. Grabbing all the docs, it's going to start building this skill and this is the Opus 4.7 running in the Pi agent harness. This is going to be some pretty 

fantastic results as this gets to work here. So, right now it's gobbling up all the documentation, starting to stack up that proper context and at some point here it's going to begin again, it's communicating with our exe.dev agent here. So, there it is, we have live access confirmed, SSH exe.dev. It's now checking out all my VMs, no current VMs set up yet but my agent is going to go through this process, figure everything out and it has all the documentation and it has the feature parity it's trying to get equal to, okay? So, this is a really 

great way to in general, you know, it doesn't really matter what agent agent communication system you're using, this is a great way to mirror systems together, right? In the age of agents, we're going to have a hundred different services available to us for agent sandboxing and frankly, you know, for agent harnessing, cloud databases, Turso, things like Neon DB, and a lot of them are going to be swappable, right? Composable. And so, this is a great pattern. Once you have one skill against one specific service, you can quickly create a feature parity document and then build directly against another 

service. Asian agent communication is a great way to do that because you get that focused agent context window and then your agent can just quickly communicate when they need to. But let's go ahead and dig a little bit deeper into this system, right? Like how does this system really work? There's four tools here. There's basically no magic. It's really simple. You list all the agents on the network, send command, or you send the prompt, and then optionally, you can await a response, right? Sometimes you send off 

a Slack message and you're just sending useful information to someone or a confirmation or something, and that's it. But if you need to, you can await the response. You can check in on the message. You can do a block wait or you can do a non-blocking poll. I have two versions of this. It's going to be available to you. You can see our agents are starting to chat together here. I'll have two versions of this available to you. Both are going to be available in the Pi versus Cloud Code code base. This is a code base that has been live for quite some time and it's where I posted and shared a lot of extensions 

from simple to complex cross multiple different agent harness use cases for the Pi agent harness, all right? And so, the whole idea here is just to hedge against Cloud Code, the agentic coding market leader, and get control of the agent harness. This code base builds on that very idea and I'm going to add these two extensions for you into this code base. And so, you know, what are these two extensions? We can just go ahead and crack these open here. Coms version, so this is the non-network version. This operates on a single device. But then we have a coms net 

where we basically boot up a simple simple simple lightweight bun server here that accepts requests over the network. And you can imagine we have a simple set that let the agent connect, get messages, list agents, process events, so on and so forth here, right? This is a very simple implementation. Secure it, make it more legitimate for your specific use case. Every piece of code you see now, I really think it's really about read and adapt, right? Through your agents add it and have them transform it for your specific use case. 

And always understand the code. 25% here on our E2B agent. See, it just responded directly here. Kind of looks good. Browser. Okay, SBX tool. Nice. So, it looks like exi.dev agent was asking about the browser tool. All three questions cleanly answered. Quick recap. Templates versus images. Okay, so confirm partial support. Let's see. Captured artifacts, arbitrary container images. Okay. Browser, two primary files, zero E2B import fix, drop in 

portability. Great. Snapshot, no E2B equivalent. CP is unique to exi.dev. Okay. So, there we go. Here he's writing that feature parity doc. This is looking great. Yeah, nice. Looks like we had a couple chats here to showcase everything. Sent this to E2B. Why now? The parity has their claims is to flag as many E2B claims that's wrong before I bake them into the new skill. Very cool. Okay. Very nice. So, our agents here are doing the work that I would do myself, which is validate the claims, right? 

This is something we talked about in the verifier agent video we did a couple weeks ago where you have an agent basically double-checking all the claims and all the statements that the primary agent is making to make sure that they're right. This is a really powerful pattern. I like to run my Pi agents, my primary Pi agent with a validator on top of it, which basically, you know, increases the tokens used, but in exchange it saves me time because the validator is validating everything my agent just said, right? It makes sure that everything it said is actually true. And then it also makes sure that 

the work it said it did is exactly what was done. I'll link that in the description as well. There we go. There's a nice write back to our eexi.dev agent. It's like it's asking for a recursive flag there, too. Wow, so much detail here. Like in the side here, this is a great way to just watch these models work together, right? GPT-5.5, Claude 4.7, gave them a decent size prompt, maybe 80 lines each, and a skill, and now they're just like hashing it out, recreating this new skill. And this is again just one of millions and 

millions of different ways to coordinate agents to work toward a goal, to work toward something, right? So, okay, so we got 10 corrections from that exchange, right? This is a valuable exchange of information. 10 corrections. There's a couple comments in my videos recently, especially when I talk about multi-agent orchestration, some engineers, probably a decent amount of vibe coders as well, asking, "Why can't you just do all this in one agent?" You certainly can. You certainly can. But you have to remember that couple things. There is a limit to the context window. The more problems, the more different problems, APIs, 

systems you put into that context window, your error rate will go up. Okay, this is just a fact. If you don't believe that, you don't understand that, do more research on the context window, okay? And then second, with every unique model that you add to your system, right? I'm running Claude right next to GPT-5.5. These models are trained in a completely different way. They have different RL loops running on top of them. Putting these agents together creates something greater. It creates a system that outperforms either of them alone. Just like code plus agent beats 

either alone, unique agent one plus unique agent two communicating beats either alone, right? And and that's like really the gift and really the value proposition of multi-agent orchestration. It's not just the 10 parallel agents you boot up to like write all those files or generate all those images at the same time. It's doing serious engineering work where your agents are checking in on each other, double checking the work, coordinating on a solution, so on and so forth, okay? So, that's the idea. And so, we got one more message coming back here. Hopefully, this wraps it up. And 

yeah, look at this like Opus is just being really, really great here with the verification. So, please reread the doc and either send review complete or flag remaining issues. All right, so this is just like, you know, it's teamwork, right? This is teamwork, okay? Sign off one non-blocking knit, okay? And then after this, we can proceed with uh scaffolding. So, there we go. So, yeah, it's loading that meta skill. This is my skill that helps me create skills. I'm going to let this cook. Comment down below if you're interested in my agent 

sandbox skills, the E2B skill, or this new exa.dev skill, and I'll add it to this codebase. But, that's the idea, right? It's it's it's simple, yet it's very, very important, okay? Now, you know, quickly just talking about pros and cons of this system. Every system has pros and cons. If you don't address them, you'll be exposed to them. What are the pros here? It's just an agent, right? I just can at any time now boot up two agents, three agents, five 

agents on my device, my Mac mini, my M4, right? My cloud VMs, all my services, all my servers. I can just boot up an agent now with the extension, have them connect, have them talk to each other. It's just an agent. It's that simple. As you say, it's just an agent and extension. It's permanent, okay? There's no you know, no subagent delegation, no spin-up or spin-down, no resume. Claude has this resume flag where you can reboot the agent. These are just agents in the terminal. That's it, right? Uh 

customizable, right? End-to-end. Obviously, this is like a key value prop of why I keep talking about the Python coding agent and why I keep bringing it up. The the state space of agentic engineering is unknown. You know, the way I see this is only uh 1% of it has been discovered and understood and deployed into production, right? I talking like really, really low numbers here. Customization and extensibility is core to the future of agentic engineers. And so, this tool becomes more and more important to me every single day. The tool you use limits what you believe is 

possible. And with the pie agent harness, I see no limits. You know, all the limitations of of how things work, they're just falling away. I don't see the same workflows. I don't see the same implementations anymore. And I think if you're stuck using one agentic coding tool, especially one that tells you how to do everything, hint hint Claude code, hint hint Codex, hint hint, you know, Gemini C alive if anyone's using that, open code, like whatever it is, right? You are not getting, you know, you're not pushing into that 99% the rest of 

the value that we can unlock with agents, with the right agentic technology, okay? So, um that's a big one, obviously, right? Uh bidirectional comms are flat. No hierarchy, right? No information loss. No one agent to rule them all, which is a con in another way, right? We've talked about the one agent to rule them all, the orchestrator. Let's be super clear about this. This is the orchestrator. Um and this is like the current wave of multi-agent orchestration. This is super powerful. It's a great pattern. I'm going to continue to use it, but um 

bidirectional is great cuz it's flat, it's two-way, no information gets lost, right? Um another great part about this is that uh this is a primitive over composition approach, right? Once again, this kind of ties back into that first idea. This is just an agent. It's just a pie coding agent, right? Or just simplify it, right? Let's not hyper fixate on pie, right? This is just an agent. I just open up an agent, and then I can compose as many agents as I want to, okay? So, once again, we're engineering. Composition is an engineering pattern. We're creating slices of things we can combine to make 

something bigger, right? Primitives into compositions. But you want the primitive first so that you can compose it. That's enough glaze. Uh let's go to cons. Uh you have to build this yourself or get it from any dev Dan for free. Link in the description. But, you know, you know what I mean, right? You have to build this, you have to vet this, you have to control the way your agents communicate. You need to prompt engineer everything, contact engineer thing everything, and you need to deal with the the cases, right? The edge cases is where really where great 

agentic engineering patterns are made, and great products in general, right? Another con here, loops are possible if prompts are sloppy, right? So, you can you can really generate some bad loops that that are going to really chew up your token usage if your prompts are sloppy, right? You need an end state, right? Let's see if our agents have hit their end state yet. Okay, great. So, yeah, so we are approaching the end state, right? My agent is making progress. It is creating this agent sandbox EXE dev skill. Okay, so that's great. So, this prompt obviously was not sloppy. I don't write very a ton of sloppy prompts anymore, but this is a 

risk of this strategy, right? And then there's just like general costs, right? Cost scales linearly with agent count plus communication bounce. And so, there a bunch of laws around the perfect number of actors to have in a team, right? Inside of your communication channel. That's kind of what this, you know, showcases, right? There's some magical number, Dunbar's number, or something. I wouldn't worry about that too much. I would just worry about like, what's useful? How can I deploy bidirectional agents, bidirectional peer-to-peer agents that it's actually useful across devices, or on the same 

device, right? The key here is peer-to-peer. And just make it as useful as possible. If you find that three agents, 10 agents, whatever is too much, then just trim them. So, it's not a huge con, but it's important to uh take into account, right? And I think the last con is, be careful not to just fall back into the orchestration pattern. Unless you need it, right? If you need orchestration pattern, just build that. This is kind of nice though still cuz you can compose peer-to-peer agent communication back into a orchestration pattern where you have more of a top-down format where one agent's 

leading the rest. That's fine, too, right? As I mentioned, you know, we're exploring the state space of what's possible. This is equally as valuable, but peer-to-peer's advantage is that it is flat and there's no hierarchy, right? That's the advantage, right? Your agents are working together. It's not a delegation stream. So, these are some of the pros and the cons of this system. I think it's important to address the upside and the downside, right? Again, if you're doing engineering, you need to address both of them. So, this is yet another multi-agent orchestration system that you can use to push what you can do with your agents in the age of agents, 

right? And the goal is the same. We're not really changing We're not doing anything new here on the channel. What we are doing week after week is we're increasing trust and scale of our agentic systems. All right? You can see this final reviews coming in. This is coordinated agents working together, double-checking their work. And you can see here our tokens are starting to stack up. We have 2 million available, but it's split in half. One is focused on exe.dev, one is focused on e2b, but our agents are still coordinating on the same information. We're making sure that 

we're hitting feature parity. We're making sure that everything looks good. Of course, I'm going to run more tests on this and make sure that this looks good, but I can almost guarantee you this is going to work out of the box because I had two agents two state-of-the-art agents working together to get this shipped out. Enabling specialized agents that chat together on device and across devices is a unique advantage you can add to your agentic systems, specifically to your agent harness. This pattern and patterns like this more and more of these patterns are going to emerge. They're impossible if you're using, you know, the 

out-of-the-box agents from Anthropic, from OpenAI, from Google. It's impossible when you're renting your agent harness, okay? To be clear, I still use Claude Code all the time. It's a great tool. I'm going to continue to use it, but more and more I'm reaching for the Pi agent harness to build the exact experience and products that I'm looking for, right? And this pattern adds to that bag of tricks that you and I can now deploy in our agent harness if you own your agent harness. I'm going to be adding these two extensions to the Pi versus Claude Code codebase here 

available to you, link in the description. I'm really excited for some of the big ideas I have to share with you here on the channel coming up. I'm waiting for that next Gemini model launch to really showcase one of these next-gen patterns. So, make sure you like, make sure you subscribe, join the journey so you don't miss that. You know where to find me every single Monday. Stay focused and keep building. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 What's up, engineers? Indie Dev Dan here.
 </span>
 <span data-rw-start="2.36" data-rw-transcript-version="2">
 I have a simple question for you. What's
 </span>
 <span data-rw-start="4.8" data-rw-transcript-version="2">
 better than one GPT 5.5 Pi coding agent?
 </span>
 <span data-rw-start="9.96" data-rw-transcript-version="2">
 You guessed it, two GPT 5.5 Pi coding
 </span>
 <span data-rw-start="13.64" data-rw-transcript-version="2">
 agents. Let's push it further. What’s
 </span>
 <span data-rw-start="15.48" data-rw-transcript-version="2">
 better than two isolated side-by-side
 </span>
 <span data-rw-start="17.96" data-rw-transcript-version="2">
 GPT 5.5 agents? Sure, you could add
 </span>
 <span data-rw-start="20.68" data-rw-transcript-version="2">
 another agent. Sure, you could change
 </span>
 <span data-rw-start="22.32" data-rw-transcript-version="2">
 the model, but we can do much better
 </span>
 <span data-rw-start="24.68" data-rw-transcript-version="2">
 than this. What about two GPT 5.5 agents
 </span>
 <span data-rw-start="28.52" data-rw-transcript-version="2">
 that actually work together?
 </span>
</p>
<p>
 <span data-rw-start="31.56" data-rw-transcript-version="2">
 What about three agents that work
 </span>
 <span data-rw-start="33.24" data-rw-transcript-version="2">
 together with unique models? What about
 </span>
 <span data-rw-start="36.2" data-rw-transcript-version="2">
 four models? So, here we have four Pi
 </span>
 <span data-rw-start="39.24" data-rw-transcript-version="2">
 coding agents and none of them is the
 </span>
 <span data-rw-start="41.72" data-rw-transcript-version="2">
 orchestrator. Instead, they're equals.
 </span>
 <span data-rw-start="44.36" data-rw-transcript-version="2">
 They're co-workers pinging every agent.
 </span>
 <span data-rw-start="47.84" data-rw-transcript-version="2">
 In this video, we'll understand what
 </span>
 <span data-rw-start="50.32" data-rw-transcript-version="2">
 type of agentic engineering we can
 </span>
 <span data-rw-start="52.12" data-rw-transcript-version="2">
 achieve if we gave our agents a true
 </span>
 <span data-rw-start="55.56" data-rw-transcript-version="2">
 two-way communication channel. By the
 </span>
 <span data-rw-start="58.44" data-rw-transcript-version="2">
 end of this video, you'll have a simple
 </span>
 <span data-rw-start="60.4" data-rw-transcript-version="2">
 yet powerful way to coordinate your
 </span>
 <span data-rw-start="63.08" data-rw-transcript-version="2">
 multi-agent systems. This gives us a
 </span>
 <span data-rw-start="65.92" data-rw-transcript-version="2">
 powerful flat agent hierarchy where the
 </span>
 <span data-rw-start="69.2" data-rw-transcript-version="2">
 Best information wins, where the best
 </span>
 <span data-rw-start="71.36" data-rw-transcript-version="2">
 ideas win, and where your agents can
 </span>
 <span data-rw-start="73.12" data-rw-transcript-version="2">
 truly coordinate together to outperform
 </span>
 <span data-rw-start="76.52" data-rw-transcript-version="2">
 each other alone. Let's talk about
 </span>
 <span data-rw-start="78.4" data-rw-transcript-version="2">
 Pi-to-Pi two-way agent communication.
 </span>
</p>
<p>
 <span data-rw-start="87.24" data-rw-transcript-version="2">
 So, let's go ahead and reset here. Let's
 </span>
 <span data-rw-start="89.48" data-rw-transcript-version="2">
 de-hype this a little bit. Let's close
 </span>
 <span data-rw-start="91.36" data-rw-transcript-version="2">
 our agents. As you can see, one by one
 </span>
 <span data-rw-start="93.2" data-rw-transcript-version="2">
 as we close them, they leave the chat
 </span>
 <span data-rw-start="95.68" data-rw-transcript-version="2">
 room. They leave the communication pool.
 </span>
 <span data-rw-start="98.2" data-rw-transcript-version="2">
 We've got a production database on my
 </span>
 <span data-rw-start="100.12" data-rw-transcript-version="2">
 Mac mini. And this production database
 </span>
 <span data-rw-start="102.64" data-rw-transcript-version="2">
 has an issue. Some ProTier users are
 </span>
 <span data-rw-start="104.68" data-rw-transcript-version="2">
 getting locked out of pro features. So,
 </span>
 <span data-rw-start="107.24" data-rw-transcript-version="2">
 in order to fix this issue, I need to
 </span>
 <span data-rw-start="108.64" data-rw-transcript-version="2">
 reproduce it on my local developer
 </span>
 <span data-rw-start="110.92" data-rw-transcript-version="2">
 environment. This is a common
 </span>
 <span data-rw-start="112.48" data-rw-transcript-version="2">
 engineering workflow. You don't fix
 </span>
 <span data-rw-start="114.24" data-rw-transcript-version="2">
 things in production, and fix things on
 </span>
 <span data-rw-start="115.88" data-rw-transcript-version="2">
 your developer environment, and then you
 </span>
</p>
<p>
 <span data-rw-start="117.2" data-rw-transcript-version="2">
 deploy through staging, and then
 </span>
 <span data-rw-start="119.12" data-rw-transcript-version="2">
 eventually it hits production. The trick
 </span>
 <span data-rw-start="121" data-rw-transcript-version="2">
 here is, there is sensitive information
 </span>
 <span data-rw-start="123.72" data-rw-transcript-version="2">
 on my Mac mini production environment,
 </span>
 <span data-rw-start="126.24" data-rw-transcript-version="2">
 and I can't leak any PII while I'm
 </span>
 <span data-rw-start="130.039" data-rw-transcript-version="2">
 fixing this issue. We're not live coding
 </span>
 <span data-rw-start="131.959" data-rw-transcript-version="2">
 here, we're doing real engineering work
 </span>
 <span data-rw-start="133.72" data-rw-transcript-version="2">
 in production systems. Our pie-to-pie
 </span>
 <span data-rw-start="136.4" data-rw-transcript-version="2">
 agent-to-agent communication system is
 </span>
 <span data-rw-start="138.6" data-rw-transcript-version="2">
 perfect for this. So, I'll boot up two
 </span>
 <span data-rw-start="140.28" data-rw-transcript-version="2">
 agents here, one on my Mac mini, the
 </span>
 <span data-rw-start="142.2" data-rw-transcript-version="2">
 production server, and one on my M5
 </span>
 <span data-rw-start="144.28" data-rw-transcript-version="2">
 MacBook Pro, my dev machine. We'll do J
 </span>
 <span data-rw-start="146.44" data-rw-transcript-version="2">
 coms two, and we'll give this a name.
 </span>
</p>
<p>
 <span data-rw-start="148.24" data-rw-transcript-version="2">
 This is going to be production. J coms
 </span>
 <span data-rw-start="150.28" data-rw-transcript-version="2">
 one, name dev. We'll run some basic
 </span>
 <span data-rw-start="152.8" data-rw-transcript-version="2">
 pings to make sure both agents are up
 </span>
 <span data-rw-start="154.48" data-rw-transcript-version="2">
 and online. And then we're going to
 </span>
 <span data-rw-start="155.64" data-rw-transcript-version="2">
 paste in a production prompt here. This
 </span>
 <span data-rw-start="158.04" data-rw-transcript-version="2">
 is a prod gatekeeper agent. It has a
 </span>
 <span data-rw-start="160.84" data-rw-transcript-version="2">
 production database it's working with
 </span>
 <span data-rw-start="162.76" data-rw-transcript-version="2">
 that's been seeded. We're not going to
 </span>
 <span data-rw-start="163.92" data-rw-transcript-version="2">
 recreate it or anything. And you have a
 </span>
 <span data-rw-start="166.08" data-rw-transcript-version="2">
 team name. And then key piece here, we
 </span>
 <span data-rw-start="168.12" data-rw-transcript-version="2">
 have PII inside of this production code
 </span>
 <span data-rw-start="171.04" data-rw-transcript-version="2">
 base that we're not going to break. This
 </span>
 <span data-rw-start="172.72" data-rw-transcript-version="2">
 is personal identifiable information.
 </span>
</p>
<p>
 <span data-rw-start="176.12" data-rw-transcript-version="2">
 So, our production agent understands the
 </span>
 <span data-rw-start="177.84" data-rw-transcript-version="2">
 system, it understands what's available,
 </span>
 <span data-rw-start="179.8" data-rw-transcript-version="2">
 and it knows that it's not going to
 </span>
 <span data-rw-start="181.4" data-rw-transcript-version="2">
 Expose any information to any other
 </span>
 <span data-rw-start="184.56" data-rw-transcript-version="2">
 agent on the network, okay? And now our
 </span>
 <span data-rw-start="187" data-rw-transcript-version="2">
 developer agent is going to get to work.
 </span>
</p>
<p>
 <span data-rw-start="188.6" data-rw-transcript-version="2">
 We need to reproduce this issue locally.
 </span>
 <span data-rw-start="191.04" data-rw-transcript-version="2">
 Here's our developer prompt. The key
 </span>
 <span data-rw-start="192.68" data-rw-transcript-version="2">
 here is this. Bring the affected slice
 </span>
 <span data-rw-start="195.12" data-rw-transcript-version="2">
 from production over with PII stripped
 </span>
 <span data-rw-start="197.76" data-rw-transcript-version="2">
 into your local dev DB so an engineer
 </span>
 <span data-rw-start="200.12" data-rw-transcript-version="2">
 can reproduce the issue locally. First,
 </span>
 <span data-rw-start="202.8" data-rw-transcript-version="2">
 in order to reproduce a production
 </span>
 <span data-rw-start="204.44" data-rw-transcript-version="2">
 database issue, you need the production
 </span>
 <span data-rw-start="206.4" data-rw-transcript-version="2">
 data. Here's where the magic happens.
 </span>
</p>
<p>
 <span data-rw-start="208.64" data-rw-transcript-version="2">
 Our agent sees the peer on the network,
 </span>
 <span data-rw-start="211.2" data-rw-transcript-version="2">
 right? It knows that it has connection
 </span>
 <span data-rw-start="212.48" data-rw-transcript-version="2">
 to a prod agent, and now it's going to
 </span>
 <span data-rw-start="214.2" data-rw-transcript-version="2">
 start working through things. So, it's
 </span>
 <span data-rw-start="216.239" data-rw-transcript-version="2">
 going to send a message, it's going to
 </span>
 <span data-rw-start="217.32" data-rw-transcript-version="2">
 send a prompt, and it's going to get
 </span>
 <span data-rw-start="218.76" data-rw-transcript-version="2">
 returned an ID, a message ID. Our agent
 </span>
 <span data-rw-start="221.68" data-rw-transcript-version="2">
 can now await this message, and our
 </span>
 <span data-rw-start="223.84" data-rw-transcript-version="2">
 production agent, as you can see here,
 </span>
 <span data-rw-start="226.12" data-rw-transcript-version="2">
 is getting to work on the production
 </span>
 <span data-rw-start="228.44" data-rw-transcript-version="2">
 side. But it's getting to work with all
 </span>
 <span data-rw-start="230.64" data-rw-transcript-version="2">
 redactions applied, right? It's not
 </span>
 <span data-rw-start="232.96" data-rw-transcript-version="2">
 going to expose any personal
 </span>
 <span data-rw-start="234.68" data-rw-transcript-version="2">
 Identifiable information. Our agent is
 </span>
 <span data-rw-start="236.96" data-rw-transcript-version="2">
 going to work back and forth here, not
 </span>
 <span data-rw-start="238.56" data-rw-transcript-version="2">
 as individual agents, not as a sub
 </span>
 <span data-rw-start="241" data-rw-transcript-version="2">
 agent, not as workers, right? They're
 </span>
 <span data-rw-start="243.2" data-rw-transcript-version="2">
 going to work together as a team. It's a
 </span>
 <span data-rw-start="246.28" data-rw-transcript-version="2">
 simple, beautiful pattern, and it really
 </span>
 <span data-rw-start="248.68" data-rw-transcript-version="2">
 reflects how great work is done. And so,
 </span>
 <span data-rw-start="251.72" data-rw-transcript-version="2">
 our agent is learning about the local
 </span>
</p>
<p>
 <span data-rw-start="253.6" data-rw-transcript-version="2">
 DB. It's making sure that it's clean,
 </span>
 <span data-rw-start="255.8" data-rw-transcript-version="2">
 and it's starting to sync things while
 </span>
 <span data-rw-start="257.959" data-rw-transcript-version="2">
 keeping everything PII safe, right? So,
 </span>
 <span data-rw-start="260.28" data-rw-transcript-version="2">
 this is yet another place where if you
 </span>
 <span data-rw-start="262.88" data-rw-transcript-version="2">
 engineer things properly, if you prompt
 </span>
 <span data-rw-start="265.32" data-rw-transcript-version="2">
 things properly, you can do
 </span>
 <span data-rw-start="266.52" data-rw-transcript-version="2">
 extraordinary things in your agentic
 </span>
 <span data-rw-start="269.2" data-rw-transcript-version="2">
 systems. There are endless use cases for
 </span>
 <span data-rw-start="272.04" data-rw-transcript-version="2">
 agents that actually communicate and
 </span>
 <span data-rw-start="274.32" data-rw-transcript-version="2">
 work together. You can see there we got
 </span>
 <span data-rw-start="275.84" data-rw-transcript-version="2">
 another message back, and this process
 </span>
 <span data-rw-start="278.56" data-rw-transcript-version="2">
 is going to continue. So, we're going to
 </span>
 <span data-rw-start="280.48" data-rw-transcript-version="2">
 let our agents cook here. I want to take
 </span>
 <span data-rw-start="282.04" data-rw-transcript-version="2">
 the time to like highlight why
 </span>
 <span data-rw-start="284.2" data-rw-transcript-version="2">
 agent-to-agent communication is so
 </span>
 <span data-rw-start="285.68" data-rw-transcript-version="2">
 important, and highlight, of course,
 </span>
 <span data-rw-start="287.4" data-rw-transcript-version="2">
 once again, why the Pi Coding Agent is
 </span>
 <span data-rw-start="289.76" data-rw-transcript-version="2">
 Really, the only way that you get this
 </span>
 <span data-rw-start="291.52" data-rw-transcript-version="2">
 level of control out of your agents
 </span>
 <span data-rw-start="293.76" data-rw-transcript-version="2">
 here.
 </span>
</p>
<p>
 <span data-rw-start="299.28" data-rw-transcript-version="2">
 I think the most important thing to
 </span>
 <span data-rw-start="300.4" data-rw-transcript-version="2">
 start with here is understanding the
 </span>
 <span data-rw-start="302.6" data-rw-transcript-version="2">
 current problem, right? Agents can't
 </span>
 <span data-rw-start="304.72" data-rw-transcript-version="2">
 talk to each other. We know that there
 </span>
 <span data-rw-start="306.24" data-rw-transcript-version="2">
 is sub-agent delegation and sub-agent
 </span>
 <span data-rw-start="309.2" data-rw-transcript-version="2">
 prompting, right? And this is a great
 </span>
 <span data-rw-start="310.84" data-rw-transcript-version="2">
 pattern. It's a great start. Like if you
 </span>
 <span data-rw-start="312.919" data-rw-transcript-version="2">
 agree with this statement, we are just
 </span>
 <span data-rw-start="314.44" data-rw-transcript-version="2">
 scratching the surface of what the true
 </span>
 <span data-rw-start="317.04" data-rw-transcript-version="2">
 developer experience looks like for
 </span>
 <span data-rw-start="319.6" data-rw-transcript-version="2">
 agentic engineering, right? We don't
 </span>
 <span data-rw-start="322" data-rw-transcript-version="2">
 really even know what that form factor
 </span>
 <span data-rw-start="323.68" data-rw-transcript-version="2">
 is. I think very clearly in terminal
 </span>
 <span data-rw-start="327.44" data-rw-transcript-version="2">
 agents,
 </span>
 <span data-rw-start="329.28" data-rw-transcript-version="2">
 the center point, but everything around
 </span>
 <span data-rw-start="331.32" data-rw-transcript-version="2">
 that—from the agent harness to how we
 </span>
 <span data-rw-start="333.44" data-rw-transcript-version="2">
 manage contexts, models, agent scale,
 </span>
 <span data-rw-start="335.919" data-rw-transcript-version="2">
 tools—this is all a work in progress.
 </span>
</p>
<p>
 <span data-rw-start="338.28" data-rw-transcript-version="2">
 So, if we're not exploring the state
 </span>
 <span data-rw-start="339.84" data-rw-transcript-version="2">
 space of what's possible with our agent
 </span>
 <span data-rw-start="341.919" data-rw-transcript-version="2">
 communication and other agentic
 </span>
 <span data-rw-start="344.68" data-rw-transcript-version="2">
 workflows and patterns, uh, we're going
 </span>
 <span data-rw-start="346.48" data-rw-transcript-version="2">
 To be stuck in the normal distribution,
 </span>
 <span data-rw-start="348.36" data-rw-transcript-version="2">
 the very beginning of what's possible.
 </span>
</p>
<p>
 <span data-rw-start="350.32" data-rw-transcript-version="2">
 So, sub-agents are very important, very
 </span>
 <span data-rw-start="352.2" data-rw-transcript-version="2">
 cool, but this is just the beginning,
 </span>
 <span data-rw-start="353.8" data-rw-transcript-version="2">
 right? When you push further, you can
 </span>
 <span data-rw-start="355.28" data-rw-transcript-version="2">
 find a message queue, and this is what
 </span>
 <span data-rw-start="357.52" data-rw-transcript-version="2">
 the Cloud Code agent teams use. So, you
 </span>
 <span data-rw-start="359.72" data-rw-transcript-version="2">
 have one agent that kind of sets up all
 </span>
 <span data-rw-start="361.36" data-rw-transcript-version="2">
 the message queue, and then it serves as
 </span>
 <span data-rw-start="363.08" data-rw-transcript-version="2">
 a message broker between agents. Another
 </span>
 <span data-rw-start="365.52" data-rw-transcript-version="2">
 great powerful pattern. You then have
 </span>
 <span data-rw-start="367.08" data-rw-transcript-version="2">
 things like agent chains, where you have
 </span>
 <span data-rw-start="368.96" data-rw-transcript-version="2">
 a deterministic set-up workflow that
 </span>
 <span data-rw-start="371.16" data-rw-transcript-version="2">
 has individual nodes of agents. When
 </span>
 <span data-rw-start="373.4" data-rw-transcript-version="2">
 you combine this with code, you get
 </span>
 <span data-rw-start="374.8" data-rw-transcript-version="2">
 powerful AI developer workflows or
 </span>
</p>
<p>
 <span data-rw-start="377.08" data-rw-transcript-version="2">
 blueprints or representations of agents
 </span>
 <span data-rw-start="380.44" data-rw-transcript-version="2">
 plus code. This is a very, very powerful
 </span>
 <span data-rw-start="382.6" data-rw-transcript-version="2">
 framework because it adds determinism
 </span>
 <span data-rw-start="385" data-rw-transcript-version="2">
 into the process, right? At any one of
 </span>
 <span data-rw-start="386.68" data-rw-transcript-version="2">
 these steps, you can insert code, and
 </span>
 <span data-rw-start="388.44" data-rw-transcript-version="2">
 it'll enhance what your agents can do.
 </span>
 <span data-rw-start="390.08" data-rw-transcript-version="2">
 So, very powerful stuff here, right?
 </span>
 <span data-rw-start="391.52" data-rw-transcript-version="2">
 But, um, there's a problem with this. As
 </span>
 <span data-rw-start="393.28" data-rw-transcript-version="2">
 you can see, in every one of these
 </span>
 <span data-rw-start="394.52" data-rw-transcript-version="2">
 Workflows, it is traveling information in basically one direction, and it's
 </span>
 <span data-rw-start="397.16" data-rw-transcript-version="2">
 always a top-down way. Even if the
 </span>
 <span data-rw-start="399.36" data-rw-transcript-version="2">
 information comes back, it's a one-way
 </span>
 <span data-rw-start="401.24" data-rw-transcript-version="2">
 stream, right? It's never bidirectional.
 </span>
</p>
<p>
 <span data-rw-start="403.48" data-rw-transcript-version="2">
 So, what's the solution?
 </span>
 <span data-rw-start="405.64" data-rw-transcript-version="2">
 It's quite simple. Let your agents talk
 </span>
 <span data-rw-start="407.8" data-rw-transcript-version="2">
 to each other, right? Prompt response,
 </span>
 <span data-rw-start="410.24" data-rw-transcript-version="2">
 and then prompt response, okay?
 </span>
 <span data-rw-start="412.72" data-rw-transcript-version="2">
 Peer-to-peer, not
 </span>
 <span data-rw-start="414.44" data-rw-transcript-version="2">
 orchestrator-to-worker,
 </span>
 <span data-rw-start="417.44" data-rw-transcript-version="2">
 changes things. Here, agents are equals.
 </span>
 <span data-rw-start="422.4" data-rw-transcript-version="2">
 They're not parent and child, and this
 </span>
 <span data-rw-start="424.04" data-rw-transcript-version="2">
 unlocks, of course, bidirectional flows
 </span>
 <span data-rw-start="426.52" data-rw-transcript-version="2">
 of information, okay? Just two agents
 </span>
 <span data-rw-start="428.64" data-rw-transcript-version="2">
 communicating to each other. As you can
 </span>
 <span data-rw-start="430.04" data-rw-transcript-version="2">
 see here, our agents are still working
 </span>
 <span data-rw-start="432" data-rw-transcript-version="2">
 together to figure out these issues, to
 </span>
 <span data-rw-start="434.52" data-rw-transcript-version="2">
 really work through how to perfectly
 </span>
 <span data-rw-start="436.88" data-rw-transcript-version="2">
 reproduce the production slice. But, you
 </span>
 <span data-rw-start="439.68" data-rw-transcript-version="2">
 can push this across devices and across
 </span>
 <span data-rw-start="442.2" data-rw-transcript-version="2">
 multiple agents, right? And this looks
 </span>
 <span data-rw-start="443.919" data-rw-transcript-version="2">
 like exactly what you'd imagine, right?
 </span>
</p>
<p>
 <span data-rw-start="445.64" data-rw-transcript-version="2">
 Now, we have three agents in the
 </span>
 <span data-rw-start="447.32" data-rw-transcript-version="2">
 network. You might have a researcher,
 </span>
 <span data-rw-start="448.8" data-rw-transcript-version="2">
 Coder, planner. These can be anything
 </span>
 <span data-rw-start="450.88" data-rw-transcript-version="2">
 under the sun. In our case, we have a
 </span>
 <span data-rw-start="453.12" data-rw-transcript-version="2">
 prod agent, and we have a developer
 </span>
 <span data-rw-start="455.68" data-rw-transcript-version="2">
 agent talking to each other across the
 </span>
 <span data-rw-start="458.12" data-rw-transcript-version="2">
 network, okay? But, you can just keep
 </span>
 <span data-rw-start="459.919" data-rw-transcript-version="2">
 scaling this up, right? And at some
 </span>
 <span data-rw-start="461.6" data-rw-transcript-version="2">
 point, it's going to be uh harmful,
 </span>
 <span data-rw-start="464.08" data-rw-transcript-version="2">
 right? Like there is a limit to how
 </span>
 <span data-rw-start="465.4" data-rw-transcript-version="2">
 useful this is. Um I'm not just trying
 </span>
 <span data-rw-start="467.68" data-rw-transcript-version="2">
 to sell you the upside here. There’s
 </span>
 <span data-rw-start="469.08" data-rw-transcript-version="2">
 downsides to every approach. Great
 </span>
 <span data-rw-start="470.92" data-rw-transcript-version="2">
 engineering is all about managing
 </span>
 <span data-rw-start="472.48" data-rw-transcript-version="2">
 tradeoffs. At some level, you’re not
 </span>
 <span data-rw-start="474.4" data-rw-transcript-version="2">
 going to want to use this pattern
 </span>
 <span data-rw-start="475.52" data-rw-transcript-version="2">
 anymore. And at some level, adding
 </span>
 <span data-rw-start="477.44" data-rw-transcript-version="2">
 agents doesn’t help anything. But, there
 </span>
 <span data-rw-start="480.04" data-rw-transcript-version="2">
 is certainly a useful level to this
 </span>
 <span data-rw-start="482.68" data-rw-transcript-version="2">
 where you want to have bidirectional
 </span>
 <span data-rw-start="484.88" data-rw-transcript-version="2">
 agent-to-agent communication, where it’s
 </span>
 <span data-rw-start="486.84" data-rw-transcript-version="2">
 very, very useful to have every agent
 </span>
 <span data-rw-start="488.92" data-rw-transcript-version="2">
 have access to every other agent, okay?
 </span>
</p>
<p>
 <span data-rw-start="491.44" data-rw-transcript-version="2">
 And so, why is this useful, right? Let’s
 </span>
 <span data-rw-start="493.919" data-rw-transcript-version="2">
 let’s really hit on this. Like I think
 </span>
 <span data-rw-start="495.919" data-rw-transcript-version="2">
 at the core of this, it comes down to
 </span>
 <span data-rw-start="498.2" data-rw-transcript-version="2">
 information hierarchies. If you have a
 </span>
 <span data-rw-start="500.08" data-rw-transcript-version="2">
 Traditional software engineering job,
 </span>
 <span data-rw-start="501.48" data-rw-transcript-version="2">
 you work at a company that has a
 </span>
 <span data-rw-start="503.52" data-rw-transcript-version="2">
 hierarchy, right? For one reason or
 </span>
 <span data-rw-start="505.84" data-rw-transcript-version="2">
 another, there is someone at the top,
 </span>
 <span data-rw-start="507.6" data-rw-transcript-version="2">
 okay? And information usually travels
 </span>
 <span data-rw-start="509.72" data-rw-transcript-version="2">
 downstream, commands travel downstream,
 </span>
 <span data-rw-start="511.68" data-rw-transcript-version="2">
 objectives travel downstream, and then
 </span>
 <span data-rw-start="514.12" data-rw-transcript-version="2">
 it hits the person, usually the
 </span>
 <span data-rw-start="516" data-rw-transcript-version="2">
 engineers, who are actually building the
 </span>
 <span data-rw-start="517.599" data-rw-transcript-version="2">
 thing, right? And oftentimes, the best
 </span>
 <span data-rw-start="520" data-rw-transcript-version="2">
 information, the best decisions, the
 </span>
 <span data-rw-start="522.159" data-rw-transcript-version="2">
 best awareness about the system is all
 </span>
 <span data-rw-start="524.6" data-rw-transcript-version="2">
 the way down here, right? It's on the
 </span>
 <span data-rw-start="526.44" data-rw-transcript-version="2">
 worker level, right? It's It's you and
 </span>
 <span data-rw-start="528.32" data-rw-transcript-version="2">
 I, the engineers with their boots on the
 </span>
 <span data-rw-start="529.68" data-rw-transcript-version="2">
 ground every single day, putting in the
 </span>
 <span data-rw-start="531.24" data-rw-transcript-version="2">
 work to understand the system,
 </span>
 <span data-rw-start="532.4" data-rw-transcript-version="2">
 understand the objectives, and then
 </span>
 <span data-rw-start="533.6" data-rw-transcript-version="2">
 actually building it, right? The best
 </span>
 <span data-rw-start="535.6" data-rw-transcript-version="2">
 information is often times down here.
 </span>
</p>
<p>
 <span data-rw-start="538.04" data-rw-transcript-version="2">
 When you have these hierarchical
 </span>
 <span data-rw-start="539.76" data-rw-transcript-version="2">
 information systems, and I'm speaking in
 </span>
 <span data-rw-start="542.04" data-rw-transcript-version="2">
 a generic way, it doesn't just need to
 </span>
 <span data-rw-start="543.56" data-rw-transcript-version="2">
 be about the job. It doesn't just need
 </span>
 <span data-rw-start="545.12" data-rw-transcript-version="2">
 to be in a career setting. But, just
 </span>
 <span data-rw-start="547.4" data-rw-transcript-version="2">
 Information structures like this, often
 </span>
 <span data-rw-start="549.4" data-rw-transcript-version="2">
 times the best ideas are down here. They
 </span>
 <span data-rw-start="551.04" data-rw-transcript-version="2">
 get stuck down here because they don't
 </span>
 <span data-rw-start="552.56" data-rw-transcript-version="2">
 have the right title, they don't have
 </span>
 <span data-rw-start="554.4" data-rw-transcript-version="2">
 the right authority, they don't have the
 </span>
 <span data-rw-start="556.36" data-rw-transcript-version="2">
 right say, right? And you've, you know,
 </span>
 <span data-rw-start="558.4" data-rw-transcript-version="2">
 you've probably heard this, right? But,
 </span>
 <span data-rw-start="559.64" data-rw-transcript-version="2">
 the best companies, the best structures
 </span>
 <span data-rw-start="561.64" data-rw-transcript-version="2">
 are flat, where there's communication
 </span>
 <span data-rw-start="564.16" data-rw-transcript-version="2">
 happening on every single level, where
 </span>
 <span data-rw-start="566.2" data-rw-transcript-version="2">
 everyone can just talk to the other to
 </span>
 <span data-rw-start="568.28" data-rw-transcript-version="2">
 get the job done, right? Nvidia is
 </span>
 <span data-rw-start="570.2" data-rw-transcript-version="2">
 really famous for this, very flat
 </span>
</p>
<p>
 <span data-rw-start="571.96" data-rw-transcript-version="2">
 reporting structures. Of course, Jensen
 </span>
 <span data-rw-start="573.6" data-rw-transcript-version="2">
 at the top, commanding that insane
 </span>
 <span data-rw-start="576.64" data-rw-transcript-version="2">
 company. But, then he has uh very few
 </span>
 <span data-rw-start="578.28" data-rw-transcript-version="2">
 direct reports, and then it spans from
 </span>
 <span data-rw-start="580.36" data-rw-transcript-version="2">
 there, right? But, startups are famous
 </span>
 <span data-rw-start="581.92" data-rw-transcript-version="2">
 for this, right? You have very, very
 </span>
 <span data-rw-start="583.28" data-rw-transcript-version="2">
 flat structures. All the best
 </span>
 <span data-rw-start="585.52" data-rw-transcript-version="2">
 information systems are flat. Why is
 </span>
 <span data-rw-start="588.2" data-rw-transcript-version="2">
 that? It’s because you get valuable
 </span>
 <span data-rw-start="590.16" data-rw-transcript-version="2">
 information wins always over titles and
 </span>
 <span data-rw-start="593.48" data-rw-transcript-version="2">
 politics, okay? Ideas die in
 </span>
 <span data-rw-start="595.8" data-rw-transcript-version="2">
 hierarchies. So, that’s why this is so
 </span>
 <span data-rw-start="598.36" data-rw-transcript-version="2">
 Important. And, you know, maybe you
 </span>
 <span data-rw-start="600.28" data-rw-transcript-version="2">
 think I'm anthropomorphizing this too
 </span>
 <span data-rw-start="601.72" data-rw-transcript-version="2">
 much. Maybe you think I am trying to
 </span>
 <span data-rw-start="603.4" data-rw-transcript-version="2">
 apply something where it doesn't belong.
 </span>
</p>
<p>
 <span data-rw-start="605.32" data-rw-transcript-version="2">
 I completely disagree. I think when you
 </span>
 <span data-rw-start="607.12" data-rw-transcript-version="2">
 really boil things down, everything is a
 </span>
 <span data-rw-start="608.92" data-rw-transcript-version="2">
 system. And a key part about every
 </span>
 <span data-rw-start="611.84" data-rw-transcript-version="2">
 system is that there is flows of
 </span>
 <span data-rw-start="614" data-rw-transcript-version="2">
 information inside of systems, and how
 </span>
 <span data-rw-start="616.72" data-rw-transcript-version="2">
 things flow, how the structures, the
 </span>
 <span data-rw-start="619.04" data-rw-transcript-version="2">
 nodes, and the actors in the system
 </span>
 <span data-rw-start="621.32" data-rw-transcript-version="2">
 communicate information matters, right?
 </span>
 <span data-rw-start="623.8" data-rw-transcript-version="2">
 This matters because oftentimes the best
 </span>
 <span data-rw-start="626.44" data-rw-transcript-version="2">
 ideas are down here. They're at the
 </span>
 <span data-rw-start="628.88" data-rw-transcript-version="2">
 bottom level. And so, this means that as
 </span>
 <span data-rw-start="630.96" data-rw-transcript-version="2">
 much as you can, you want to have flat
 </span>
 <span data-rw-start="632.68" data-rw-transcript-version="2">
 hierarchy structures, okay? But, on a
 </span>
 <span data-rw-start="634.64" data-rw-transcript-version="2">
 functional level, we can see that this
 </span>
 <span data-rw-start="636.68" data-rw-transcript-version="2">
 is uh useful for other reasons as well.
 </span>
 <span data-rw-start="639.12" data-rw-transcript-version="2">
 We have cross-device agent-to-agent
 </span>
 <span data-rw-start="641.28" data-rw-transcript-version="2">
 communication, right? We have a
 </span>
 <span data-rw-start="642.8" data-rw-transcript-version="2">
 production service. Say this is in the
 </span>
 <span data-rw-start="645.12" data-rw-transcript-version="2">
 EU,
 </span>
 <span data-rw-start="646.44" data-rw-transcript-version="2">
 right? Where everything has to be
 </span>
 <span data-rw-start="647.839" data-rw-transcript-version="2">
 redacted, everything has to be perfect.
 </span>
</p>
<p>
 <span data-rw-start="650.16" data-rw-transcript-version="2">
 And nothing can escape the device. But,
 </span>
 <span data-rw-start="651.76" data-rw-transcript-version="2">
 you still need to fix things, right? We
 </span>
 <span data-rw-start="653.36" data-rw-transcript-version="2">
 still need to do real engineering work.
 </span>
 <span data-rw-start="655.04" data-rw-transcript-version="2">
 So, this is a great system. We have
 </span>
 <span data-rw-start="656.96" data-rw-transcript-version="2">
 redacted information properly,
 </span>
 <span data-rw-start="658.64" data-rw-transcript-version="2">
 transferred it to our developer machine.
 </span>
 <span data-rw-start="660.92" data-rw-transcript-version="2">
 And as you can see here, the repro is
 </span>
 <span data-rw-start="662.76" data-rw-transcript-version="2">
 ready, the bug has been imported, okay?
 </span>
 <span data-rw-start="664.92" data-rw-transcript-version="2">
 PII is clean, okay? So, legitimate
 </span>
 <span data-rw-start="667.6" data-rw-transcript-version="2">
 engineering work happening here.
 </span>
</p>
<p>
 <span data-rw-start="669.32" data-rw-transcript-version="2">
 Obviously, this is not a real production
 </span>
 <span data-rw-start="671.6" data-rw-transcript-version="2">
 server. I'm using this as an example.
 </span>
 <span data-rw-start="673.6" data-rw-transcript-version="2">
 And now I can go ahead, debug, look at
 </span>
 <span data-rw-start="675.52" data-rw-transcript-version="2">
 my code, look at this slice of the
 </span>
 <span data-rw-start="678.2" data-rw-transcript-version="2">
 production database that has been
 </span>
 <span data-rw-start="679.48" data-rw-transcript-version="2">
 reproduced from production. And now I
 </span>
 <span data-rw-start="681.28" data-rw-transcript-version="2">
 can actually resolve the bug. And our
 </span>
 <span data-rw-start="683.2" data-rw-transcript-version="2">
 agents are really great at communicating
 </span>
 <span data-rw-start="685.24" data-rw-transcript-version="2">
 information like this. And that's
 </span>
 <span data-rw-start="686.52" data-rw-transcript-version="2">
 exactly what they've done, okay? So, we
 </span>
 <span data-rw-start="687.88" data-rw-transcript-version="2">
 have very simple two-way bidirectional
 </span>
 <span data-rw-start="691.24" data-rw-transcript-version="2">
 agent-to-agent communication. If I
 </span>
 <span data-rw-start="692.72" data-rw-transcript-version="2">
 needed to, I could come in here and
 </span>
 <span data-rw-start="695" data-rw-transcript-version="2">
 validate that everything looks good on
 </span>
 <span data-rw-start="696.96" data-rw-transcript-version="2">
 the production agent side, right? Do one
 </span>
 <span data-rw-start="699.88" data-rw-transcript-version="2">
 Final check with the dev agent PRI safe.
 </span>
</p>
<p>
 <span data-rw-start="703.24" data-rw-transcript-version="2">
 The issue has been repro'd.
 </span>
 <span data-rw-start="705.84" data-rw-transcript-version="2">
 We can talk to any side that we need to, and they can then communicate together to get the job done.
 </span>
 <span data-rw-start="708.04" data-rw-transcript-version="2">
 So, I hope you can see the value proposition of this.
 </span>
 <span data-rw-start="710.16" data-rw-transcript-version="2">
 I hope you can see why agent-to-agent communication is useful, even if you don't think that the flat information hierarchies are more performant for making sure that the best ideas are the ones that always win.
 </span>
 <span data-rw-start="712.8" data-rw-transcript-version="2">
 This is great because now we have simple multi-agent communication on different devices, okay?
 </span>
 <span data-rw-start="715.88" data-rw-transcript-version="2">
 And whenever we need to, you know, let me just be clear about this.
 </span>
 <span data-rw-start="718.88" data-rw-transcript-version="2">
 Whenever we need to, I can add an agent to the pool.
 </span>
 <span data-rw-start="721.32" data-rw-transcript-version="2">
 So, if I type J Comms, let's use four, I think that's the GLM agent.
 </span>
 <span data-rw-start="727.24" data-rw-transcript-version="2">
 You can see GLM added here, and now it is part of the pool, right?
 </span>
 <span data-rw-start="730.64" data-rw-transcript-version="2">
 So, fantastic. How else can we use this?
 </span>
 <span data-rw-start="733.2" data-rw-transcript-version="2">
 Agent-to-agent communication, it seems very powerful.
 </span>
 <span data-rw-start="735.84" data-rw-transcript-version="2">
 We're not just delegating work, which is in its own right a very powerful communication.
 </span>
</p>
<p>
 <span data-rw-start="748.64" data-rw-transcript-version="2">
 Pattern, right? This isn't a
 </span>
 <span data-rw-start="749.6" data-rw-transcript-version="2">
 replacement. This is another option for
 </span>
 <span data-rw-start="751.88" data-rw-transcript-version="2">
 your agentic engineering. We can solve
 </span>
 <span data-rw-start="753.8" data-rw-transcript-version="2">
 other problems with it, right? Let let
 </span>
 <span data-rw-start="755.04" data-rw-transcript-version="2">
 let's walk through another example.
 </span>
</p>
<p>
 <span data-rw-start="761.44" data-rw-transcript-version="2">
 So, let's fire up a E2B agent. And in
 </span>
 <span data-rw-start="765.12" data-rw-transcript-version="2">
 fact, let's open up a new project here,
 </span>
 <span data-rw-start="767.8" data-rw-transcript-version="2">
 sandbox. Same deal, J Comms 2, and name
 </span>
 <span data-rw-start="771.72" data-rw-transcript-version="2">
 EXC dev agent project sandbox. So, we're
 </span>
 <span data-rw-start="775.32" data-rw-transcript-version="2">
 just getting our agents off this
 </span>
 <span data-rw-start="777.12" data-rw-transcript-version="2">
 network. This is a different pool to
 </span>
 <span data-rw-start="779.16" data-rw-transcript-version="2">
 communicate in, right? So, we still
 </span>
 <span data-rw-start="780.32" data-rw-transcript-version="2">
 still have our previous set there. And
 </span>
 <span data-rw-start="781.839" data-rw-transcript-version="2">
 you can actually see that this work here
 </span>
 <span data-rw-start="783.72" data-rw-transcript-version="2">
 was done. PII is safe. All the findings
 </span>
 <span data-rw-start="786.04" data-rw-transcript-version="2">
 are there. So, we verified by having our
 </span>
 <span data-rw-start="788.12" data-rw-transcript-version="2">
 production agent prompt our developer
 </span>
 <span data-rw-start="790" data-rw-transcript-version="2">
 agent. Fantastic. There we got the pass.
 </span>
 <span data-rw-start="791.88" data-rw-transcript-version="2">
 Everything looks great. Both context
 </span>
 <span data-rw-start="793.44" data-rw-transcript-version="2">
 windows are sharp and focused. There's
 </span>
 <span data-rw-start="795.839" data-rw-transcript-version="2">
 no spillover between issues. This system
 </span>
 <span data-rw-start="798.48" data-rw-transcript-version="2">
 has completed successfully. So, I've
 </span>
 <span data-rw-start="800.6" data-rw-transcript-version="2">
 been using the E2B agent sandbox tool
 </span>
 <span data-rw-start="803.52" data-rw-transcript-version="2">
 for quite some time now. It's been a
 </span>
 <span data-rw-start="804.68" data-rw-transcript-version="2">
 great tool. It's also expensive, and it
 </span>
</p>
<p>
 <span data-rw-start="806.72" data-rw-transcript-version="2">
 Has some downsides, like there's a limit
 </span>
 <span data-rw-start="808.84" data-rw-transcript-version="2">
 to the total duration that you can have
 </span>
 <span data-rw-start="810.92" data-rw-transcript-version="2">
 your agents up in a sandbox. You have to
 </span>
 <span data-rw-start="812.84" data-rw-transcript-version="2">
 pause them to manage that. So, I've been
 </span>
 <span data-rw-start="814.72" data-rw-transcript-version="2">
 looking at exe.dev as a new agent
 </span>
 <span data-rw-start="817.6" data-rw-transcript-version="2">
 sandbox tool to replace or use
 </span>
 <span data-rw-start="820.56" data-rw-transcript-version="2">
 additionally right next to e2b. And so,
 </span>
 <span data-rw-start="823.08" data-rw-transcript-version="2">
 this is another agent sandbox tool. It's
 </span>
 <span data-rw-start="824.92" data-rw-transcript-version="2">
 got a couple of different benefits. I'll
 </span>
 <span data-rw-start="826.56" data-rw-transcript-version="2">
 link both of these in the description
 </span>
 <span data-rw-start="828.12" data-rw-transcript-version="2">
 for you. But, the idea here is I already
 </span>
 <span data-rw-start="830.36" data-rw-transcript-version="2">
 have my e2b agent in this sandbox skill,
 </span>
 <span data-rw-start="833.2" data-rw-transcript-version="2">
 right? So, I have agent sandboxes and
 </span>
 <span data-rw-start="834.96" data-rw-transcript-version="2">
 this is my e2b skill where I can just
 </span>
 <span data-rw-start="836.88" data-rw-transcript-version="2">
 quickly spin up an agent sandbox that my
 </span>
 <span data-rw-start="839.2" data-rw-transcript-version="2">
 agent can fully own and operate on my
 </span>
 <span data-rw-start="841.08" data-rw-transcript-version="2">
 behalf. We've talked about agent
 </span>
 <span data-rw-start="842.48" data-rw-transcript-version="2">
 sandboxes on the channel in the past.
 </span>
</p>
<p>
 <span data-rw-start="844.2" data-rw-transcript-version="2">
 I'll link those in the description for
 </span>
 <span data-rw-start="845.64" data-rw-transcript-version="2">
 you as well. But, what I want to do here
 </span>
 <span data-rw-start="847.12" data-rw-transcript-version="2">
 is spin up a brand new skill for exe.dev
 </span>
 <span data-rw-start="851.36" data-rw-transcript-version="2">
 that mirrors and matches and has feature
 </span>
 <span data-rw-start="854.2" data-rw-transcript-version="2">
 parity to my e2b agent skill. And
 </span>
 <span data-rw-start="856.64" data-rw-transcript-version="2">
 anything that doesn't match, I want to
 </span>
 <span data-rw-start="858.8" data-rw-transcript-version="2">
 know about it, right? I want to
 </span>
 <span data-rw-start="860.32" data-rw-transcript-version="2">
 Understand the feature differences, but
 </span>
 <span data-rw-start="862.12" data-rw-transcript-version="2">
 I want my agent to fail forward. The
 </span>
 <span data-rw-start="864.68" data-rw-transcript-version="2">
 skill to be built so that I can
 </span>
 <span data-rw-start="866.04" data-rw-transcript-version="2">
 prototype and experiment with it right
 </span>
 <span data-rw-start="867.88" data-rw-transcript-version="2">
 away, okay? So, I don't just want a
 </span>
 <span data-rw-start="869.28" data-rw-transcript-version="2">
 simple research comparison. I want a new
 </span>
 <span data-rw-start="871.24" data-rw-transcript-version="2">
 skill I can use that has feature parity
 </span>
 <span data-rw-start="874" data-rw-transcript-version="2">
 with my existing skill. That's exactly
 </span>
 <span data-rw-start="875.64" data-rw-transcript-version="2">
 what I'm going to prompt here. In my e2b
 </span>
 <span data-rw-start="877.24" data-rw-transcript-version="2">
 agent, I'm going to fire this off.
 </span>
</p>
<p>
 <span data-rw-start="878.52" data-rw-transcript-version="2">
 You're the e2b agent. Your teammate is
 </span>
 <span data-rw-start="881.2" data-rw-transcript-version="2">
 exe.dev. They'll be building this skill
 </span>
 <span data-rw-start="884.6" data-rw-transcript-version="2">
 against exe.dev's persistent VM
 </span>
 <span data-rw-start="887.24" data-rw-transcript-version="2">
 platform. Your job is to answer their
 </span>
 <span data-rw-start="888.96" data-rw-transcript-version="2">
 questions, okay? So, we have a teammate
 </span>
 <span data-rw-start="891" data-rw-transcript-version="2">
 set up specifically to understand this
 </span>
 <span data-rw-start="893.28" data-rw-transcript-version="2">
 feature set. It's putting up a sandbox.
 </span>
</p>
<p>
 <span data-rw-start="895.2" data-rw-transcript-version="2">
 It's reminding itself of all the
 </span>
 <span data-rw-start="896.839" data-rw-transcript-version="2">
 features. And when this completes, I'm
 </span>
 <span data-rw-start="898.48" data-rw-transcript-version="2">
 going to kick off the exe.dev agent to
 </span>
 <span data-rw-start="901.44" data-rw-transcript-version="2">
 communicate, work with, and sync up a
 </span>
 <span data-rw-start="904.12" data-rw-transcript-version="2">
 brand new skill. You know, a lot of the
 </span>
 <span data-rw-start="906.12" data-rw-transcript-version="2">
 agent-to-agent communication and
 </span>
 <span data-rw-start="907.32" data-rw-transcript-version="2">
 multi-agent orchestration comes down to
 </span>
 <span data-rw-start="909.88" data-rw-transcript-version="2">
 expanding your context window in a
 </span>
 <span data-rw-start="911.96" data-rw-transcript-version="2">
 Useful way such that your agents can
 </span>
 <span data-rw-start="914.4" data-rw-transcript-version="2">
 specialize what they're focused on,
 </span>
 <span data-rw-start="916.4" data-rw-transcript-version="2">
 okay? A lot of engineers do think that
 </span>
 <span data-rw-start="918.32" data-rw-transcript-version="2">
 you just throw everything in one agent,
 </span>
 <span data-rw-start="919.76" data-rw-transcript-version="2">
 wait for models to get better, wait
 </span>
 <span data-rw-start="921.16" data-rw-transcript-version="2">
 for that 5 million contacts window, and
 </span>
 <span data-rw-start="923.28" data-rw-transcript-version="2">
 then all your problems will be solved. I
 </span>
 <span data-rw-start="925.04" data-rw-transcript-version="2">
 don't agree with this approach at all. I
 </span>
 <span data-rw-start="927.64" data-rw-transcript-version="2">
 think you should lean on the models, you
 </span>
 <span data-rw-start="929.2" data-rw-transcript-version="2">
 should expect them to get better, you
 </span>
 <span data-rw-start="930.56" data-rw-transcript-version="2">
 should plan for that in your products
 </span>
 <span data-rw-start="932.2" data-rw-transcript-version="2">
 and services, but at the same time you
 </span>
 <span data-rw-start="933.76" data-rw-transcript-version="2">
 should be learning how to focus your
 </span>
 <span data-rw-start="935.52" data-rw-transcript-version="2">
 agents on one problem so that the chance
 </span>
 <span data-rw-start="938.56" data-rw-transcript-version="2">
 that they cause an issue, so that the
 </span>
 <span data-rw-start="939.8" data-rw-transcript-version="2">
 chance something goes wrong drops down
 </span>
 <span data-rw-start="942.2" data-rw-transcript-version="2">
 to near zero. And how can you do that?
 </span>
</p>
<p>
 <span data-rw-start="944.4" data-rw-transcript-version="2">
 You can do that by having focused
 </span>
 <span data-rw-start="946.12" data-rw-transcript-version="2">
 context windows, okay? And by
 </span>
 <span data-rw-start="948.36" data-rw-transcript-version="2">
 effectively specializing your agent to
 </span>
 <span data-rw-start="950.68" data-rw-transcript-version="2">
 focus on one problem and one problem
 </span>
 <span data-rw-start="953.36" data-rw-transcript-version="2">
 only. Spinning up and comparing two
 </span>
 <span data-rw-start="955.36" data-rw-transcript-version="2">
 different tools with likely very similar
 </span>
 <span data-rw-start="957.64" data-rw-transcript-version="2">
 APIs is going to get the context window
 </span>
 <span data-rw-start="959.84" data-rw-transcript-version="2">
 pretty big. You can see here this agent
 </span>
 <span data-rw-start="961.32" data-rw-transcript-version="2">
 is loading, refreshing itself on all of
 </span>
 <span data-rw-start="964.08" data-rw-transcript-version="2">
 the E2B agent skill functionality,
 </span>
 <span data-rw-start="966.88" data-rw-transcript-version="2">
 right? You can see sandbox remove,
 </span>
 <span data-rw-start="968.56" data-rw-transcript-version="2">
 download dir, so on and so forth. We're
 </span>
 <span data-rw-start="970.04" data-rw-transcript-version="2">
 almost at 10% context already. That's
 </span>
 <span data-rw-start="971.72" data-rw-transcript-version="2">
 100k tokens, okay? If you're using
 </span>
 <span data-rw-start="974.08" data-rw-transcript-version="2">
 agents on a daily basis, you understand
 </span>
 <span data-rw-start="976.24" data-rw-transcript-version="2">
 this fact, right? A focused agent is a
 </span>
</p>
<p>
 <span data-rw-start="978.8" data-rw-transcript-version="2">
 performant agent. You add to that
 </span>
 <span data-rw-start="980.84" data-rw-transcript-version="2">
 context window, the higher the chance
 </span>
 <span data-rw-start="983.2" data-rw-transcript-version="2">
 something goes wrong. Specifically,
 </span>
 <span data-rw-start="985.8" data-rw-transcript-version="2">
 when you start muddying unrelated
 </span>
 <span data-rw-start="987.96" data-rw-transcript-version="2">
 context together, okay? This is the art
 </span>
 <span data-rw-start="990.839" data-rw-transcript-version="2">
 of context engineering. It's not just
 </span>
 <span data-rw-start="992.32" data-rw-transcript-version="2">
 getting all the right things, it's
 </span>
 <span data-rw-start="993.76" data-rw-transcript-version="2">
 getting just the right things. This
 </span>
 <span data-rw-start="996.2" data-rw-transcript-version="2">
 agent's booting up, it should be
 </span>
 <span data-rw-start="997.16" data-rw-transcript-version="2">
 complete pretty soon here, and then we
 </span>
 <span data-rw-start="999.04" data-rw-transcript-version="2">
 can prompt our exe.dev to create this
 </span>
 <span data-rw-start="1002.68" data-rw-transcript-version="2">
 new skill so that we can boot up brand
 </span>
 <span data-rw-start="1005.24" data-rw-transcript-version="2">
 new sandboxes for exe.dev, and we can
 </span>
 <span data-rw-start="1008.28" data-rw-transcript-version="2">
 really see what this is all about.
 </span>
</p>
<p>
 <span data-rw-start="1010" data-rw-transcript-version="2">
 Moving forward, it's not just about
 </span>
 <span data-rw-start="1011.4" data-rw-transcript-version="2">
 these two sandbox tools, right? It's
 </span>
 <span data-rw-start="1012.96" data-rw-transcript-version="2">
 about every sandbox tool moving forward.
 </span>
</p>
<p>
 <span data-rw-start="1015.12" data-rw-transcript-version="2">
 And our ability to deploy agents to
 </span>
 <span data-rw-start="1017.64" data-rw-transcript-version="2">
 understand the tools, to understand the
 </span>
 <span data-rw-start="1019.12" data-rw-transcript-version="2">
 technology, and then deploy them into
 </span>
 <span data-rw-start="1021.24" data-rw-transcript-version="2">
 valuable use cases on our behalf. So, we
 </span>
 <span data-rw-start="1024.199" data-rw-transcript-version="2">
 can use this system over and over and
 </span>
 <span data-rw-start="1025.76" data-rw-transcript-version="2">
 over, we can compare the features
 </span>
 <span data-rw-start="1027.16" data-rw-transcript-version="2">
 between every specialized agent. I hope
 </span>
 <span data-rw-start="1029.6" data-rw-transcript-version="2">
 you get the point, right? If this is all
 </span>
 <span data-rw-start="1031.079" data-rw-transcript-version="2">
 making sense, you know, make sure you
 </span>
 <span data-rw-start="1032.16" data-rw-transcript-version="2">
 drop a like. This is like really our
 </span>
 <span data-rw-start="1033.92" data-rw-transcript-version="2">
 bread and butter on the channel. We're
 </span>
 <span data-rw-start="1035.8" data-rw-transcript-version="2">
 scaling our compute to scale our impact.
 </span>
</p>
<p>
 <span data-rw-start="1038.36" data-rw-transcript-version="2">
 It's all about scaling up what our
 </span>
 <span data-rw-start="1040.199" data-rw-transcript-version="2">
 agents can do and focusing our agents to
 </span>
 <span data-rw-start="1042.56" data-rw-transcript-version="2">
 solve real business problems on our
 </span>
 <span data-rw-start="1044.88" data-rw-transcript-version="2">
 behalf via agentic engineering, not vibe
 </span>
 <span data-rw-start="1047.92" data-rw-transcript-version="2">
 coding. We're not shooting prompts and
 </span>
 <span data-rw-start="1049.72" data-rw-transcript-version="2">
 not looking. We know what our agents are
 </span>
 <span data-rw-start="1051.68" data-rw-transcript-version="2">
 doing, okay? And this just stacks up on
 </span>
 <span data-rw-start="1054.72" data-rw-transcript-version="2">
 previous videos we've had on the channel
 </span>
 <span data-rw-start="1056.44" data-rw-transcript-version="2">
 where we're making our agents secure.
 </span>
 <span data-rw-start="1058.52" data-rw-transcript-version="2">
 We're not letting them crush production
 </span>
 <span data-rw-start="1060.6" data-rw-transcript-version="2">
 assets when they should not be able to.
 </span>
 <span data-rw-start="1062.68" data-rw-transcript-version="2">
 We're adding security to our bash tool
 </span>
 <span data-rw-start="1064.8" data-rw-transcript-version="2">
 when they need it. Just like in last
 </span>
 <span data-rw-start="1067.08" data-rw-transcript-version="2">
 Week's video, we're preventing
 </span>
 <span data-rw-start="1068.4" data-rw-transcript-version="2">
 catastrophic commands from running. And
 </span>
 <span data-rw-start="1070.56" data-rw-transcript-version="2">
 then, you know, we're letting our agents
 </span>
 <span data-rw-start="1072.32" data-rw-transcript-version="2">
 rip on all the tools, all the skills,
 </span>
 <span data-rw-start="1074.6" data-rw-transcript-version="2">
 all the commands that we actually want
 </span>
 <span data-rw-start="1076.2" data-rw-transcript-version="2">
 our agents to execute, right? As you can
 </span>
 <span data-rw-start="1078.2" data-rw-transcript-version="2">
 see here, a lot of that sandbox tool
 </span>
 <span data-rw-start="1080.04" data-rw-transcript-version="2">
 running, our agent is understanding what
 </span>
 <span data-rw-start="1082.32" data-rw-transcript-version="2">
 it can do here. And soon it's going to
 </span>
 <span data-rw-start="1083.84" data-rw-transcript-version="2">
 write this uh presentation file for us.
 </span>
</p>
<p>
 <span data-rw-start="1086.24" data-rw-transcript-version="2">
 And this is one of the great things and
 </span>
 <span data-rw-start="1087.68" data-rw-transcript-version="2">
 one of the annoying things about GPT
 </span>
 <span data-rw-start="1089.4" data-rw-transcript-version="2">
 5.5. This model really chews up tokens
 </span>
 <span data-rw-start="1092" data-rw-transcript-version="2">
 and it just goes and goes and goes to
 </span>
 <span data-rw-start="1093.72" data-rw-transcript-version="2">
 really get you the most comprehensive
 </span>
 <span data-rw-start="1096.2" data-rw-transcript-version="2">
 result possible. Whereas, I found that
 </span>
 <span data-rw-start="1098.56" data-rw-transcript-version="2">
 Opus 4.7 will do that as well, but it
 </span>
 <span data-rw-start="1100.92" data-rw-transcript-version="2">
 also will really just focus on the goal,
 </span>
 <span data-rw-start="1103.92" data-rw-transcript-version="2">
 right? I think Opus is more
 </span>
 <span data-rw-start="1105.04" data-rw-transcript-version="2">
 goal-oriented and really focuses on
 </span>
 <span data-rw-start="1107.2" data-rw-transcript-version="2">
 accomplishing the goal. If you prompt it
 </span>
 <span data-rw-start="1109.04" data-rw-transcript-version="2">
 wide enough to capture more of that
 </span>
 <span data-rw-start="1111.04" data-rw-transcript-version="2">
 state, more of that scope, it'll
 </span>
 <span data-rw-start="1112.16" data-rw-transcript-version="2">
 certainly capture that as well, okay?
 </span>
 <span data-rw-start="1114.04" data-rw-transcript-version="2">
 But here we go. We're getting that
 </span>
 <span data-rw-start="1115.08" data-rw-transcript-version="2">
 Inventory file that really compresses
 </span>
 <span data-rw-start="1117.2" data-rw-transcript-version="2">
 all the observations. Now, we should be
 </span>
 <span data-rw-start="1119.16" data-rw-transcript-version="2">
 able to kick off our exe.dev agent
 </span>
 <span data-rw-start="1121.48" data-rw-transcript-version="2">
 pretty soon here. There we go. Nice
 </span>
 <span data-rw-start="1123.84" data-rw-transcript-version="2">
 write-up. Look at that detailed write-up
 </span>
 <span data-rw-start="1125.2" data-rw-transcript-version="2">
 of all the features, inputs, and
 </span>
 <span data-rw-start="1127.2" data-rw-transcript-version="2">
 outputs, the commands, E2B quirks.
 </span>
</p>
<p>
 <span data-rw-start="1129.64" data-rw-transcript-version="2">
 Right? This is great. And this was part
 </span>
 <span data-rw-start="1130.88" data-rw-transcript-version="2">
 of the prompt, right? We wanted at the
 </span>
 <span data-rw-start="1132.4" data-rw-transcript-version="2">
 end a feature inventory. And this is
 </span>
 <span data-rw-start="1134.48" data-rw-transcript-version="2">
 going to allow our exe.dev agent to
 </span>
 <span data-rw-start="1137" data-rw-transcript-version="2">
 really map everything out one-to-one.
 </span>
 <span data-rw-start="1139.28" data-rw-transcript-version="2">
 And again, like focus context is so
 </span>
 <span data-rw-start="1141.6" data-rw-transcript-version="2">
 important here, right? In tactically
 </span>
 <span data-rw-start="1143.4" data-rw-transcript-version="2">
 agentic coding, it's so important. This
 </span>
 <span data-rw-start="1145.04" data-rw-transcript-version="2">
 is an entire tactic. We talk about this
 </span>
 <span data-rw-start="1146.72" data-rw-transcript-version="2">
 for an entire lesson. A focused agent is
 </span>
 <span data-rw-start="1149.28" data-rw-transcript-version="2">
 a performant agent. We have 20% context
 </span>
 <span data-rw-start="1152.32" data-rw-transcript-version="2">
 of the 1 million context window GPT 5.5
 </span>
 <span data-rw-start="1155.44" data-rw-transcript-version="2">
 focus on just understanding this tool
 </span>
 <span data-rw-start="1157.8" data-rw-transcript-version="2">
 and understanding this skill and this
 </span>
 <span data-rw-start="1159.68" data-rw-transcript-version="2">
 whole sandbox system. Okay, so there
 </span>
 <span data-rw-start="1162.12" data-rw-transcript-version="2">
 go. Validating its work, making sure
 </span>
 <span data-rw-start="1163.56" data-rw-transcript-version="2">
 that that file exists and now we're
 </span>
 <span data-rw-start="1165.8" data-rw-transcript-version="2">
 going to boot up our exe.dev agent.
 </span>
</p>
<p>
 <span data-rw-start="1167.4" data-rw-transcript-version="2">
 There we go, perfect. So, it's all
 </span>
 <span data-rw-start="1169.2" data-rw-transcript-version="2">
 primed, it's all good to go. Now we're
 </span>
 <span data-rw-start="1170.92" data-rw-transcript-version="2">
 going to fire off this prompt inside of
 </span>
 <span data-rw-start="1172.76" data-rw-transcript-version="2">
 our exe.dev agent. I actually haven't
 </span>
 <span data-rw-start="1174.52" data-rw-transcript-version="2">
 run this before, so I'm really curious to
 </span>
 <span data-rw-start="1176.04" data-rw-transcript-version="2">
 see how how this executes and how well
 </span>
 <span data-rw-start="1178" data-rw-transcript-version="2">
 this mirrors. So, you're the exe.dev
 </span>
 <span data-rw-start="1180.04" data-rw-transcript-version="2">
 agent. There is no agent sandbox exe.dev
 </span>
 <span data-rw-start="1182.48" data-rw-transcript-version="2">
 skill yet. Your job is to build one.
 </span>
</p>
<p>
 <span data-rw-start="1184.52" data-rw-transcript-version="2">
 Okay, so there's the purpose and then
 </span>
 <span data-rw-start="1186.04" data-rw-transcript-version="2">
 your reference target is this existing
 </span>
 <span data-rw-start="1188.32" data-rw-transcript-version="2">
 skill here, which your teammate
 </span>
 <span data-rw-start="1190.08" data-rw-transcript-version="2">
 understands is already standing by to
 </span>
 <span data-rw-start="1192.2" data-rw-transcript-version="2">
 answer questions about. You're the
 </span>
 <span data-rw-start="1193.48" data-rw-transcript-version="2">
 driver of this collaboration. E2B will
 </span>
 <span data-rw-start="1195.36" data-rw-transcript-version="2">
 not initiate; you reach out. So, I'm
 </span>
 <span data-rw-start="1197.04" data-rw-transcript-version="2">
 setting this up so that in this specific
 </span>
 <span data-rw-start="1198.72" data-rw-transcript-version="2">
 scenario, I want my exe.dev agent to be
 </span>
 <span data-rw-start="1201" data-rw-transcript-version="2">
 the one driving this. I'm giving it a
 </span>
 <span data-rw-start="1202.48" data-rw-transcript-version="2">
 couple skills, fire crawl, meta skill to
 </span>
 <span data-rw-start="1204.92" data-rw-transcript-version="2">
 really build on this, and then we have
 </span>
 <span data-rw-start="1206.56" data-rw-transcript-version="2">
 our clear deliverable. So, I want that
 </span>
 <span data-rw-start="1209.24" data-rw-transcript-version="2">
 new skill, right? And I'm making it
 </span>
 <span data-rw-start="1210.68" data-rw-transcript-version="2">
 super clear here, a new working skill
 </span>
 <span data-rw-start="1212.44" data-rw-transcript-version="2">
 that mirrors the {slash} agent sandbox.
 </span>
</p>
<p>
 <span data-rw-start="1214.4" data-rw-transcript-version="2">
 Is against exe.dev primitives, and I also
 </span>
 <span data-rw-start="1217.08" data-rw-transcript-version="2">
 want a feature parity document just like
 </span>
 <span data-rw-start="1220" data-rw-transcript-version="2">
 the E2B agent has as well for us, okay?
 </span>
 <span data-rw-start="1222.48" data-rw-transcript-version="2">
 And so, it's starting to get to work
 </span>
 <span data-rw-start="1223.52" data-rw-transcript-version="2">
 here. Grabbing all the docs, it's going
 </span>
 <span data-rw-start="1225.04" data-rw-transcript-version="2">
 to start building this skill, and this is
 </span>
 <span data-rw-start="1226.32" data-rw-transcript-version="2">
 the Opus 4.7 running in the Pi agent
 </span>
 <span data-rw-start="1228.4" data-rw-transcript-version="2">
 harness. This is going to be some pretty
 </span>
 <span data-rw-start="1230.2" data-rw-transcript-version="2">
 fantastic results as this gets to work
 </span>
 <span data-rw-start="1232.48" data-rw-transcript-version="2">
 here. So, right now, it's gobbling up all
 </span>
 <span data-rw-start="1234.56" data-rw-transcript-version="2">
 the documentation, starting to stack up
 </span>
 <span data-rw-start="1236.6" data-rw-transcript-version="2">
 that proper context, and at some point
 </span>
 <span data-rw-start="1238.88" data-rw-transcript-version="2">
 here, it's going to begin again. It's
 </span>
 <span data-rw-start="1240.56" data-rw-transcript-version="2">
 communicating with our exe.dev agent
 </span>
 <span data-rw-start="1243.6" data-rw-transcript-version="2">
 here. So, there it is, we have live
 </span>
 <span data-rw-start="1244.92" data-rw-transcript-version="2">
 access confirmed, SSH exe.dev. It's now
 </span>
 <span data-rw-start="1248.16" data-rw-transcript-version="2">
 checking out all my VMs. No current VMs
 </span>
</p>
<p>
 <span data-rw-start="1250.72" data-rw-transcript-version="2">
 set up yet, but my agent is going to go
 </span>
 <span data-rw-start="1252.6" data-rw-transcript-version="2">
 through this process, figure everything
 </span>
 <span data-rw-start="1254.2" data-rw-transcript-version="2">
 out, and it has all the documentation, and
 </span>
 <span data-rw-start="1256.56" data-rw-transcript-version="2">
 it has the feature parity it's trying to
 </span>
 <span data-rw-start="1258.04" data-rw-transcript-version="2">
 get equal to, okay? So, this is a really
 </span>
 <span data-rw-start="1260.2" data-rw-transcript-version="2">
 great way to, in general, you know, it
 </span>
 <span data-rw-start="1262.04" data-rw-transcript-version="2">
 doesn't really matter what agent, agent
 </span>
 <span data-rw-start="1263.24" data-rw-transcript-version="2">
 communication system you're using, this
 </span>
 <span data-rw-start="1265.12" data-rw-transcript-version="2">
 Is a great way to mirror systems
 </span>
 <span data-rw-start="1267.48" data-rw-transcript-version="2">
 together, right? In the age of agents,
 </span>
 <span data-rw-start="1269.32" data-rw-transcript-version="2">
 we're going to have a hundred different
 </span>
 <span data-rw-start="1270.52" data-rw-transcript-version="2">
 services available to us for agent
 </span>
 <span data-rw-start="1272.44" data-rw-transcript-version="2">
 sandboxing and frankly, you know, for
 </span>
 <span data-rw-start="1274.28" data-rw-transcript-version="2">
 agent harnessing, cloud databases,
 </span>
 <span data-rw-start="1276.08" data-rw-transcript-version="2">
 Turso, things like Neon DB, and a lot of
 </span>
 <span data-rw-start="1278.56" data-rw-transcript-version="2">
 them are going to be swappable, right?
 </span>
</p>
<p>
 <span data-rw-start="1280.56" data-rw-transcript-version="2">
 Composable. And so, this is a great
 </span>
 <span data-rw-start="1282.28" data-rw-transcript-version="2">
 pattern. Once you have one skill against
 </span>
 <span data-rw-start="1284.52" data-rw-transcript-version="2">
 one specific service, you can quickly
 </span>
 <span data-rw-start="1286.68" data-rw-transcript-version="2">
 create a feature parity document and
 </span>
 <span data-rw-start="1288.68" data-rw-transcript-version="2">
 then build directly against another
 </span>
 <span data-rw-start="1290.68" data-rw-transcript-version="2">
 service. Asian agent communication is a
 </span>
 <span data-rw-start="1292.8" data-rw-transcript-version="2">
 great way to do that because you get
 </span>
 <span data-rw-start="1293.92" data-rw-transcript-version="2">
 that focused agent context window and
 </span>
 <span data-rw-start="1295.92" data-rw-transcript-version="2">
 then your agent can just quickly
 </span>
 <span data-rw-start="1297" data-rw-transcript-version="2">
 communicate when they need to. But let's
 </span>
 <span data-rw-start="1298.72" data-rw-transcript-version="2">
 go ahead and dig a little bit deeper
 </span>
 <span data-rw-start="1300.28" data-rw-transcript-version="2">
 into this system, right? Like how does
 </span>
 <span data-rw-start="1301.56" data-rw-transcript-version="2">
 this system really work? There are four
 </span>
 <span data-rw-start="1302.96" data-rw-transcript-version="2">
 tools here. There's basically no magic.
 </span>
</p>
<p>
 <span data-rw-start="1304.84" data-rw-transcript-version="2">
 It's really simple.
 </span>
 <span data-rw-start="1310.96" data-rw-transcript-version="2">
 You list all the agents on the network,
 </span>
 <span data-rw-start="1313.44" data-rw-transcript-version="2">
 send command, or you send the prompt,
 </span>
 <span data-rw-start="1315.68" data-rw-transcript-version="2">
 And then optionally, you can await a
 </span>
 <span data-rw-start="1318" data-rw-transcript-version="2">
 response, right? Sometimes you send off
 </span>
 <span data-rw-start="1320.08" data-rw-transcript-version="2">
 a Slack message and you're just sending
 </span>
 <span data-rw-start="1322.08" data-rw-transcript-version="2">
 useful information to someone or a
 </span>
 <span data-rw-start="1323.88" data-rw-transcript-version="2">
 confirmation or something, and that's
 </span>
 <span data-rw-start="1325.72" data-rw-transcript-version="2">
 it. But if you need to, you can await
 </span>
 <span data-rw-start="1327.32" data-rw-transcript-version="2">
 the response. You can check in on the
 </span>
 <span data-rw-start="1329.28" data-rw-transcript-version="2">
 message. You can do a block wait or you
 </span>
 <span data-rw-start="1331.12" data-rw-transcript-version="2">
 can do a non-blocking poll. I have two
 </span>
 <span data-rw-start="1333.2" data-rw-transcript-version="2">
 versions of this. It's going to be
 </span>
 <span data-rw-start="1334.64" data-rw-transcript-version="2">
 available to you. You can see our agents
 </span>
 <span data-rw-start="1336.16" data-rw-transcript-version="2">
 are starting to chat together here. I'll
 </span>
 <span data-rw-start="1338.24" data-rw-transcript-version="2">
 have two versions of this available to
 </span>
 <span data-rw-start="1339.68" data-rw-transcript-version="2">
 you. Both are going to be available in
 </span>
 <span data-rw-start="1341.44" data-rw-transcript-version="2">
 the Pi versus Cloud Code code base.
 </span>
</p>
<p>
 <span data-rw-start="1345.52" data-rw-transcript-version="2">
 This is a code base that has been live
 </span>
 <span data-rw-start="1347.8" data-rw-transcript-version="2">
 for quite some time, and it's where I
 </span>
 <span data-rw-start="1349.4" data-rw-transcript-version="2">
 posted and shared a lot of extensions
 </span>
 <span data-rw-start="1352" data-rw-transcript-version="2">
 from simple to complex across multiple
 </span>
 <span data-rw-start="1354.68" data-rw-transcript-version="2">
 different agent harness use cases for
 </span>
 <span data-rw-start="1356.88" data-rw-transcript-version="2">
 the Pi agent harness, all right? And so,
 </span>
 <span data-rw-start="1359.04" data-rw-transcript-version="2">
 the whole idea here is just to hedge
 </span>
 <span data-rw-start="1360.72" data-rw-transcript-version="2">
 against Cloud Code, the agentic coding
 </span>
 <span data-rw-start="1363" data-rw-transcript-version="2">
 market leader, and get control of the
 </span>
 <span data-rw-start="1365.12" data-rw-transcript-version="2">
 agent harness. This code base builds on
 </span>
 <span data-rw-start="1367.32" data-rw-transcript-version="2">
 That very idea, and I'm going to add
 </span>
 <span data-rw-start="1369" data-rw-transcript-version="2">
 these two extensions for you into this
 </span>
 <span data-rw-start="1372.08" data-rw-transcript-version="2">
 code base. And so, you know, what are
 </span>
 <span data-rw-start="1373.24" data-rw-transcript-version="2">
 these two extensions? We can just go
 </span>
 <span data-rw-start="1374.48" data-rw-transcript-version="2">
 ahead and crack these open here. Coms
 </span>
 <span data-rw-start="1376.64" data-rw-transcript-version="2">
 version, so this is the non-network
 </span>
 <span data-rw-start="1378.28" data-rw-transcript-version="2">
 version. This operates on a single
 </span>
 <span data-rw-start="1380" data-rw-transcript-version="2">
 device. But then we have a coms net
 </span>
 <span data-rw-start="1381.88" data-rw-transcript-version="2">
 where we basically boot up a simple
 </span>
 <span data-rw-start="1384.52" data-rw-transcript-version="2">
 simple, lightweight bun server
 </span>
 <span data-rw-start="1386.44" data-rw-transcript-version="2">
 here that accepts requests over the
 </span>
 <span data-rw-start="1389.24" data-rw-transcript-version="2">
 network. And you can imagine we have a
 </span>
 <span data-rw-start="1390.4" data-rw-transcript-version="2">
 simple set that lets the agent connect,
 </span>
 <span data-rw-start="1393.72" data-rw-transcript-version="2">
 get messages, list agents, process
 </span>
 <span data-rw-start="1396.16" data-rw-transcript-version="2">
 events, so on and so forth here, right?
 </span>
</p>
<p>
 <span data-rw-start="1397.96" data-rw-transcript-version="2">
 This is a very simple implementation.
 </span>
 <span data-rw-start="1399.68" data-rw-transcript-version="2">
 Secure it, make it more legitimate for
 </span>
 <span data-rw-start="1401.48" data-rw-transcript-version="2">
 your specific use case. Every piece of
 </span>
 <span data-rw-start="1403.4" data-rw-transcript-version="2">
 code you see now, I really think it's
 </span>
 <span data-rw-start="1405.4" data-rw-transcript-version="2">
 really about read and adapt, right?
 </span>
 <span data-rw-start="1407.56" data-rw-transcript-version="2">
 Through your agents, add it and have them
 </span>
 <span data-rw-start="1409.16" data-rw-transcript-version="2">
 transform it for your specific use case.
 </span>
 <span data-rw-start="1411.68" data-rw-transcript-version="2">
 And always understand the code. 25% here
 </span>
 <span data-rw-start="1414.6" data-rw-transcript-version="2">
 on our E2B agent. See, it just responded
 </span>
 <span data-rw-start="1417" data-rw-transcript-version="2">
 directly here. Kind of looks good.
 </span>
</p>
<p>
 <span data-rw-start="1419.28" data-rw-transcript-version="2">
 Browser. Okay, SBX tool. Nice. So, it
 </span>
 <span data-rw-start="1422.56" data-rw-transcript-version="2">
 looks like exi.dev agent was asking
 </span>
 <span data-rw-start="1424.8" data-rw-transcript-version="2">
 about the browser tool. All three
 </span>
 <span data-rw-start="1426.64" data-rw-transcript-version="2">
 questions cleanly answered. Quick recap.
 </span>
 <span data-rw-start="1429.4" data-rw-transcript-version="2">
 Templates versus images. Okay, so
 </span>
 <span data-rw-start="1431.8" data-rw-transcript-version="2">
 confirm partial support. Let's see.
 </span>
 <span data-rw-start="1433.84" data-rw-transcript-version="2">
 Captured artifacts, arbitrary container
 </span>
 <span data-rw-start="1436.24" data-rw-transcript-version="2">
 images. Okay. Browser, two primary
 </span>
 <span data-rw-start="1438.56" data-rw-transcript-version="2">
 files, zero E2B import fix, drop in
 </span>
 <span data-rw-start="1441.6" data-rw-transcript-version="2">
 portability. Great. Snapshot, no E2B
 </span>
 <span data-rw-start="1443.76" data-rw-transcript-version="2">
 equivalent. CP is unique to exi.dev.
 </span>
 <span data-rw-start="1447.44" data-rw-transcript-version="2">
 Okay. So, there we go. Here he's writing
 </span>
 <span data-rw-start="1449.12" data-rw-transcript-version="2">
 that feature parity doc. This is looking
 </span>
 <span data-rw-start="1451.08" data-rw-transcript-version="2">
 great. Yeah, nice. Looks like we had a
 </span>
 <span data-rw-start="1452.6" data-rw-transcript-version="2">
 couple chats here to showcase
 </span>
 <span data-rw-start="1455.28" data-rw-transcript-version="2">
 everything. Sent this to E2B. Why now?
 </span>
 <span data-rw-start="1457.64" data-rw-transcript-version="2">
 The parity has their claims is to flag
 </span>
 <span data-rw-start="1460.08" data-rw-transcript-version="2">
 as many E2B claims that’s wrong before I
 </span>
 <span data-rw-start="1461.88" data-rw-transcript-version="2">
 bake them into the new skill. Very cool.
 </span>
 <span data-rw-start="1463.6" data-rw-transcript-version="2">
 Okay. Very nice. So, our agents here are
 </span>
 <span data-rw-start="1465.6" data-rw-transcript-version="2">
 doing the work that I would do myself,
 </span>
 <span data-rw-start="1468.2" data-rw-transcript-version="2">
 which is validate the claims, right?
 </span>
 <span data-rw-start="1471" data-rw-transcript-version="2">
 This is something we talked about in the
 </span>
 <span data-rw-start="1472.32" data-rw-transcript-version="2">
 verifier agent video we did a couple
 </span>
 <span data-rw-start="1473.88" data-rw-transcript-version="2">
 weeks ago where you have an agent.
 </span>
</p>
<p>
 <span data-rw-start="1475.84" data-rw-transcript-version="2">
 Basically, double-checking all the claims
 </span>
 <span data-rw-start="1478.2" data-rw-transcript-version="2">
 and all the statements that the primary
 </span>
 <span data-rw-start="1480.44" data-rw-transcript-version="2">
 agent is making to make sure that
 </span>
 <span data-rw-start="1482.12" data-rw-transcript-version="2">
 they're right. This is a really powerful
 </span>
 <span data-rw-start="1483.4" data-rw-transcript-version="2">
 pattern. I like to run my Pi agents, my
 </span>
 <span data-rw-start="1485.48" data-rw-transcript-version="2">
 primary Pi agent with a validator on top
 </span>
 <span data-rw-start="1488.24" data-rw-transcript-version="2">
 of it, which basically, you know,
 </span>
 <span data-rw-start="1489.52" data-rw-transcript-version="2">
 increases the tokens used, but in
 </span>
 <span data-rw-start="1491.28" data-rw-transcript-version="2">
 exchange it saves me time because the
 </span>
 <span data-rw-start="1493.56" data-rw-transcript-version="2">
 validator is validating everything my
 </span>
 <span data-rw-start="1495.68" data-rw-transcript-version="2">
 agent just said, right? It makes sure
 </span>
 <span data-rw-start="1497.2" data-rw-transcript-version="2">
 that everything it said is actually
 </span>
 <span data-rw-start="1499" data-rw-transcript-version="2">
 true. And then it also makes sure that
 </span>
 <span data-rw-start="1500.6" data-rw-transcript-version="2">
 the work it said it did is exactly what
 </span>
 <span data-rw-start="1502.76" data-rw-transcript-version="2">
 was done. I'll link that in the
 </span>
 <span data-rw-start="1503.88" data-rw-transcript-version="2">
 description as well. There we go.
 </span>
 <span data-rw-start="1505.28" data-rw-transcript-version="2">
 There's a nice write back to our
 </span>
 <span data-rw-start="1507.76" data-rw-transcript-version="2">
 eexi.dev agent. It's like it's asking
 </span>
 <span data-rw-start="1509.44" data-rw-transcript-version="2">
 for a recursive flag there, too. Wow, so
 </span>
 <span data-rw-start="1512.16" data-rw-transcript-version="2">
 much detail here. Like in the side here,
 </span>
 <span data-rw-start="1514.2" data-rw-transcript-version="2">
 this is a great way to just watch these
 </span>
 <span data-rw-start="1515.6" data-rw-transcript-version="2">
 models work together, right? GPT-5.5,
 </span>
 <span data-rw-start="1518.2" data-rw-transcript-version="2">
 Claude 4.7, gave them a decent size
 </span>
</p>
<p>
 <span data-rw-start="1520.72" data-rw-transcript-version="2">
 prompt, maybe 80 lines each, and a
 </span>
 <span data-rw-start="1523.44" data-rw-transcript-version="2">
 skill, and now they're just like hashing
 </span>
 <span data-rw-start="1525.68" data-rw-transcript-version="2">
 It out, recreating this new skill. And
 </span>
 <span data-rw-start="1528.36" data-rw-transcript-version="2">
 this is again just one of millions and
 </span>
 <span data-rw-start="1530.92" data-rw-transcript-version="2">
 millions of different ways to coordinate
 </span>
 <span data-rw-start="1533.6" data-rw-transcript-version="2">
 agents to work toward a goal, to work
 </span>
 <span data-rw-start="1536.04" data-rw-transcript-version="2">
 toward something, right? So, okay, so we
 </span>
 <span data-rw-start="1537.6" data-rw-transcript-version="2">
 got 10 corrections from that exchange,
 </span>
 <span data-rw-start="1539.64" data-rw-transcript-version="2">
 right? This is a valuable exchange of
 </span>
 <span data-rw-start="1541.28" data-rw-transcript-version="2">
 information. 10 corrections. There's a
 </span>
 <span data-rw-start="1543.16" data-rw-transcript-version="2">
 couple comments in my videos recently,
 </span>
 <span data-rw-start="1544.96" data-rw-transcript-version="2">
 especially when I talk about multi-agent
 </span>
 <span data-rw-start="1546.32" data-rw-transcript-version="2">
 orchestration, some engineers, probably
 </span>
 <span data-rw-start="1548.28" data-rw-transcript-version="2">
 a decent amount of vibe coders as well,
 </span>
 <span data-rw-start="1549.96" data-rw-transcript-version="2">
 asking, "Why can't you just do all this
 </span>
 <span data-rw-start="1551.44" data-rw-transcript-version="2">
 in one agent?" You certainly can. You
 </span>
 <span data-rw-start="1554.16" data-rw-transcript-version="2">
 certainly can. But you have to remember
 </span>
 <span data-rw-start="1556.04" data-rw-transcript-version="2">
 that couple of things. There is a limit to
 </span>
 <span data-rw-start="1557.6" data-rw-transcript-version="2">
 the context window. The more problems,
 </span>
 <span data-rw-start="1559.76" data-rw-transcript-version="2">
 the more different problems, APIs,
 </span>
 <span data-rw-start="1562.08" data-rw-transcript-version="2">
 systems you put into that context
 </span>
 <span data-rw-start="1563.6" data-rw-transcript-version="2">
 window, your error rate will go up.
 </span>
</p>
<p>
 <span data-rw-start="1565.72" data-rw-transcript-version="2">
 Okay, this is just a fact. If you don't
 </span>
 <span data-rw-start="1567.36" data-rw-transcript-version="2">
 believe that, you don't understand that,
 </span>
 <span data-rw-start="1568.8" data-rw-transcript-version="2">
 do more research on the context window,
 </span>
 <span data-rw-start="1570.32" data-rw-transcript-version="2">
 okay? And then second, with every unique
 </span>
 <span data-rw-start="1573.12" data-rw-transcript-version="2">
 model that you add to your system,
 </span>
 <span data-rw-start="1575.28" data-rw-transcript-version="2">
 Right? I'm running Claude right next to
 </span>
 <span data-rw-start="1577.16" data-rw-transcript-version="2">
 GPT-5.5. These models are trained in a
 </span>
 <span data-rw-start="1579.28" data-rw-transcript-version="2">
 completely different way. They have
 </span>
 <span data-rw-start="1580.52" data-rw-transcript-version="2">
 different RL loops running on top of
 </span>
 <span data-rw-start="1582.76" data-rw-transcript-version="2">
 them. Putting these agents together
 </span>
 <span data-rw-start="1584.4" data-rw-transcript-version="2">
 creates something greater. It creates a
 </span>
 <span data-rw-start="1586.96" data-rw-transcript-version="2">
 system that outperforms either of them
 </span>
 <span data-rw-start="1589.4" data-rw-transcript-version="2">
 alone. Just like code plus agent beats
 </span>
 <span data-rw-start="1591.72" data-rw-transcript-version="2">
 either alone, the unique agent one plus
 </span>
</p>
<p>
 <span data-rw-start="1593.52" data-rw-transcript-version="2">
 the unique agent two communicating beats
 </span>
 <span data-rw-start="1595.96" data-rw-transcript-version="2">
 either alone, right? And that's like
 </span>
 <span data-rw-start="1599" data-rw-transcript-version="2">
 really the gift and really the value
 </span>
 <span data-rw-start="1600.8" data-rw-transcript-version="2">
 proposition of multi-agent
 </span>
 <span data-rw-start="1602.36" data-rw-transcript-version="2">
 orchestration. It's not just the 10
 </span>
 <span data-rw-start="1604.8" data-rw-transcript-version="2">
 parallel agents you boot up to like
 </span>
 <span data-rw-start="1606.6" data-rw-transcript-version="2">
 write all those files or generate all
 </span>
 <span data-rw-start="1608.52" data-rw-transcript-version="2">
 those images at the same time. It's
 </span>
 <span data-rw-start="1610.08" data-rw-transcript-version="2">
 doing serious engineering work where
 </span>
 <span data-rw-start="1611.72" data-rw-transcript-version="2">
 your agents are checking in on each
 </span>
 <span data-rw-start="1613.2" data-rw-transcript-version="2">
 other, double checking the work,
 </span>
 <span data-rw-start="1614.2" data-rw-transcript-version="2">
 coordinating on a solution, so on and so
 </span>
 <span data-rw-start="1616.72" data-rw-transcript-version="2">
 forth, okay? So, that's the idea. And
 </span>
</p>
<p>
 <span data-rw-start="1618.44" data-rw-transcript-version="2">
 so, we got one more message coming back
 </span>
 <span data-rw-start="1619.84" data-rw-transcript-version="2">
 here. Hopefully, this wraps it up. And
 </span>
 <span data-rw-start="1621.84" data-rw-transcript-version="2">
 yeah, look at this like Opus is just
 </span>
 <span data-rw-start="1623.36" data-rw-transcript-version="2">
 Being really, really great here with the
 </span>
 <span data-rw-start="1625.16" data-rw-transcript-version="2">
 verification. So, please reread the doc
 </span>
 <span data-rw-start="1627.72" data-rw-transcript-version="2">
 and either send review complete or flag
 </span>
 <span data-rw-start="1630.2" data-rw-transcript-version="2">
 remaining issues. All right, so this is
 </span>
 <span data-rw-start="1631.88" data-rw-transcript-version="2">
 just like, you know, it's teamwork,
 </span>
 <span data-rw-start="1634.24" data-rw-transcript-version="2">
 right? This is teamwork, okay? Sign off
 </span>
 <span data-rw-start="1636.56" data-rw-transcript-version="2">
 one non-blocking knit, okay? And then
 </span>
 <span data-rw-start="1639.52" data-rw-transcript-version="2">
 after this, we can proceed with uh
 </span>
 <span data-rw-start="1641.64" data-rw-transcript-version="2">
 scaffolding. So, there we go. So, yeah,
 </span>
 <span data-rw-start="1643.32" data-rw-transcript-version="2">
 it's loading that meta skill. This is my
 </span>
 <span data-rw-start="1645.4" data-rw-transcript-version="2">
 skill that helps me create skills. I'm
 </span>
 <span data-rw-start="1647.4" data-rw-transcript-version="2">
 going to let this cook. Comment down
 </span>
 <span data-rw-start="1648.96" data-rw-transcript-version="2">
 below if you're interested in my agent
 </span>
 <span data-rw-start="1651.36" data-rw-transcript-version="2">
 sandbox skills, the E2B skill, or this
 </span>
 <span data-rw-start="1653.52" data-rw-transcript-version="2">
 new exa.dev skill, and I'll add it to
 </span>
 <span data-rw-start="1655.96" data-rw-transcript-version="2">
 this codebase. But, that's the idea,
 </span>
 <span data-rw-start="1658.04" data-rw-transcript-version="2">
 right? It's, it's, it's simple, yet it's
 </span>
 <span data-rw-start="1660.08" data-rw-transcript-version="2">
 very, very important, okay? Now, you
 </span>
 <span data-rw-start="1662.76" data-rw-transcript-version="2">
 know, quickly just talking about pros
 </span>
 <span data-rw-start="1664.44" data-rw-transcript-version="2">
 and cons of this system. Every system
 </span>
 <span data-rw-start="1666.08" data-rw-transcript-version="2">
 has pros and cons. If you don't address
 </span>
 <span data-rw-start="1668.04" data-rw-transcript-version="2">
 them, you'll be exposed to them.
 </span>
</p>
<p>
 <span data-rw-start="1675.64" data-rw-transcript-version="2">
 What are the pros here? It's just an
 </span>
 <span data-rw-start="1677.36" data-rw-transcript-version="2">
 agent, right? I just can at any time now
 </span>
 <span data-rw-start="1679.84" data-rw-transcript-version="2">
 boot up two agents, three agents, five
 </span>
 <span data-rw-start="1682.12" data-rw-transcript-version="2">
 Agents on my device, my Mac mini, my M4,
 </span>
 <span data-rw-start="1685.48" data-rw-transcript-version="2">
 right? My cloud VMs, all my services,
 </span>
 <span data-rw-start="1687.92" data-rw-transcript-version="2">
 all my servers. I can just boot up an
 </span>
 <span data-rw-start="1689.76" data-rw-transcript-version="2">
 agent now with the extension, have them
 </span>
 <span data-rw-start="1691.6" data-rw-transcript-version="2">
 connect, have them talk to each other.
 </span>
</p>
<p>
 <span data-rw-start="1693.64" data-rw-transcript-version="2">
 It's just an agent. It's that simple. As
 </span>
 <span data-rw-start="1695.48" data-rw-transcript-version="2">
 you say, it's just an agent and
 </span>
 <span data-rw-start="1697.04" data-rw-transcript-version="2">
 extension. It's permanent, okay? There
 </span>
 <span data-rw-start="1699.48" data-rw-transcript-version="2">
 is no, you know, no subagent delegation, no
 </span>
 <span data-rw-start="1702" data-rw-transcript-version="2">
 spin-up or spin-down, no resume. Claude
 </span>
 <span data-rw-start="1705.64" data-rw-transcript-version="2">
 has this resume flag where you can
 </span>
 <span data-rw-start="1707.12" data-rw-transcript-version="2">
 reboot the agent. These are just agents
 </span>
 <span data-rw-start="1709.16" data-rw-transcript-version="2">
 in the terminal. That's it, right? Uh
 </span>
 <span data-rw-start="1710.84" data-rw-transcript-version="2">
 customizable, right? End-to-end.
 </span>
 <span data-rw-start="1712.4" data-rw-transcript-version="2">
 Obviously, this is like a key value prop
 </span>
 <span data-rw-start="1714.56" data-rw-transcript-version="2">
 of why I keep talking about the Python
 </span>
 <span data-rw-start="1716.36" data-rw-transcript-version="2">
 coding agent and why I keep bringing it
 </span>
 <span data-rw-start="1718.04" data-rw-transcript-version="2">
 up. The state space of agentic
 </span>
 <span data-rw-start="1720.28" data-rw-transcript-version="2">
 engineering is unknown. You know, the
 </span>
 <span data-rw-start="1722.44" data-rw-transcript-version="2">
 way I see this is only, uh, 1% of it has
 </span>
 <span data-rw-start="1725.72" data-rw-transcript-version="2">
 been discovered and understood and
 </span>
 <span data-rw-start="1727.8" data-rw-transcript-version="2">
 deployed into production, right? I
 </span>
 <span data-rw-start="1729.32" data-rw-transcript-version="2">
 am talking like really, really low numbers
 </span>
 <span data-rw-start="1730.76" data-rw-transcript-version="2">
 here. Customization and extensibility is
 </span>
 <span data-rw-start="1732.96" data-rw-transcript-version="2">
 core to the future of agentic engineers.
 </span>
</p>
<p>
 <span data-rw-start="1736.04" data-rw-transcript-version="2">
 And so, this tool becomes more and more
 </span>
 <span data-rw-start="1738.12" data-rw-transcript-version="2">
 important to me every single day. The
 </span>
 <span data-rw-start="1739.56" data-rw-transcript-version="2">
 tool you use limits what you believe is
 </span>
 <span data-rw-start="1741.76" data-rw-transcript-version="2">
 possible. And with the pi agent
 </span>
 <span data-rw-start="1743.84" data-rw-transcript-version="2">
 harness, I see no limits. You know, all
 </span>
 <span data-rw-start="1747.48" data-rw-transcript-version="2">
 the limitations of how things work,
 </span>
 <span data-rw-start="1750.48" data-rw-transcript-version="2">
 they're just falling away. I don't see
 </span>
 <span data-rw-start="1752.12" data-rw-transcript-version="2">
 the same workflows. I don't see the same
 </span>
 <span data-rw-start="1754.28" data-rw-transcript-version="2">
 implementations anymore. And I think if
 </span>
 <span data-rw-start="1756.08" data-rw-transcript-version="2">
 you're stuck using one agentic coding
 </span>
 <span data-rw-start="1757.76" data-rw-transcript-version="2">
 tool, especially one that tells you how
 </span>
 <span data-rw-start="1759.28" data-rw-transcript-version="2">
 to do everything, hint hint Claude code,
 </span>
 <span data-rw-start="1761.16" data-rw-transcript-version="2">
 hint hint Codex, hint hint, you know,
 </span>
 <span data-rw-start="1762.76" data-rw-transcript-version="2">
 Gemini C alive if anyone's using that,
 </span>
 <span data-rw-start="1764.48" data-rw-transcript-version="2">
 open code, like whatever it is, right?
 </span>
</p>
<p>
 <span data-rw-start="1766.04" data-rw-transcript-version="2">
 You are not getting, you know, you're
 </span>
 <span data-rw-start="1767.76" data-rw-transcript-version="2">
 not pushing into that 99% the rest of
 </span>
 <span data-rw-start="1770.32" data-rw-transcript-version="2">
 the value that we can unlock with
 </span>
 <span data-rw-start="1772.4" data-rw-transcript-version="2">
 agents, with the right agentic
 </span>
 <span data-rw-start="1774.08" data-rw-transcript-version="2">
 technology, okay? So, um that’s a big
 </span>
 <span data-rw-start="1776.32" data-rw-transcript-version="2">
 one, obviously, right? Uh bidirectional
 </span>
 <span data-rw-start="1778.68" data-rw-transcript-version="2">
 comms are flat. No hierarchy, right? No
 </span>
 <span data-rw-start="1781.6" data-rw-transcript-version="2">
 information loss. No one agent to rule
 </span>
 <span data-rw-start="1785.12" data-rw-transcript-version="2">
 them all, which is a con in another way,
 </span>
 <span data-rw-start="1788.8" data-rw-transcript-version="2">
 right? We've talked about the one agent
 </span>
 <span data-rw-start="1789.96" data-rw-transcript-version="2">
 To rule them all, the orchestrator.
 </span>
</p>
<p>
 <span data-rw-start="1791.68" data-rw-transcript-version="2">
 Let's be super clear about this. This is
 </span>
 <span data-rw-start="1792.8" data-rw-transcript-version="2">
 the orchestrator. Um
 </span>
 <span data-rw-start="1794.4" data-rw-transcript-version="2">
 and this is like the current wave of
 </span>
 <span data-rw-start="1796.28" data-rw-transcript-version="2">
 multi-agent orchestration. This is super
 </span>
 <span data-rw-start="1797.72" data-rw-transcript-version="2">
 powerful. It's a great pattern. I'm
 </span>
 <span data-rw-start="1799.64" data-rw-transcript-version="2">
 going to continue to use it, but um
 </span>
 <span data-rw-start="1801.24" data-rw-transcript-version="2">
 bidirectional is great cuz it's flat,
 </span>
 <span data-rw-start="1803.16" data-rw-transcript-version="2">
 it's two-way, no information gets lost,
 </span>
 <span data-rw-start="1805.72" data-rw-transcript-version="2">
 right? Um another great part about this
 </span>
 <span data-rw-start="1807.2" data-rw-transcript-version="2">
 is that uh this is a primitive over
 </span>
 <span data-rw-start="1809.32" data-rw-transcript-version="2">
 composition approach, right? Once again,
 </span>
 <span data-rw-start="1811.4" data-rw-transcript-version="2">
 this kind of ties back into that first
 </span>
 <span data-rw-start="1812.8" data-rw-transcript-version="2">
 idea. This is just an agent. It's just a
 </span>
 <span data-rw-start="1815.6" data-rw-transcript-version="2">
 pie coding agent, right? Or just
 </span>
 <span data-rw-start="1817.48" data-rw-transcript-version="2">
 simplify it, right? Let's not hyper
 </span>
</p>
<p>
 <span data-rw-start="1819.12" data-rw-transcript-version="2">
 fixate on pie, right? This is just an
 </span>
 <span data-rw-start="1821.08" data-rw-transcript-version="2">
 agent. I just open up an agent, and then
 </span>
 <span data-rw-start="1822.88" data-rw-transcript-version="2">
 I can compose as many agents as I want
 </span>
 <span data-rw-start="1825" data-rw-transcript-version="2">
 to, okay? So, once again, we're
 </span>
 <span data-rw-start="1826.48" data-rw-transcript-version="2">
 engineering. Composition is an
 </span>
 <span data-rw-start="1828.44" data-rw-transcript-version="2">
 engineering pattern. We're creating
 </span>
 <span data-rw-start="1829.92" data-rw-transcript-version="2">
 slices of things we can combine to make
 </span>
 <span data-rw-start="1832.04" data-rw-transcript-version="2">
 something bigger, right? Primitives into
 </span>
 <span data-rw-start="1834" data-rw-transcript-version="2">
 compositions. But you want the primitive
 </span>
 <span data-rw-start="1835.96" data-rw-transcript-version="2">
 First, so that you can compose it. That's
 </span>
 <span data-rw-start="1838.16" data-rw-transcript-version="2">
 enough glaze. Uh, let's go to cons. Uh,
 </span>
 <span data-rw-start="1840.72" data-rw-transcript-version="2">
 you have to build this yourself or get
 </span>
 <span data-rw-start="1842.48" data-rw-transcript-version="2">
 it from any dev Dan for free. Link in
 </span>
 <span data-rw-start="1845.28" data-rw-transcript-version="2">
 the description.
 </span>
</p>
<p>
 <span data-rw-start="1847.32" data-rw-transcript-version="2">
 But, you know, you know what I mean,
 </span>
 <span data-rw-start="1848.28" data-rw-transcript-version="2">
 right? You have to build this, you have
 </span>
 <span data-rw-start="1849.44" data-rw-transcript-version="2">
 to vet this, you have to control the way
 </span>
 <span data-rw-start="1851.84" data-rw-transcript-version="2">
 your agents communicate. You need to
 </span>
 <span data-rw-start="1852.92" data-rw-transcript-version="2">
 prompt engineer everything, contact
 </span>
 <span data-rw-start="1854.44" data-rw-transcript-version="2">
 engineer thing everything, and you need
 </span>
 <span data-rw-start="1855.96" data-rw-transcript-version="2">
 to deal with the cases, right? The
 </span>
 <span data-rw-start="1857.84" data-rw-transcript-version="2">
 edge cases are really where great
 </span>
 <span data-rw-start="1860.16" data-rw-transcript-version="2">
 agentic engineering patterns are made,
 </span>
 <span data-rw-start="1862.2" data-rw-transcript-version="2">
 and great products in general, right?
 </span>
</p>
<p>
 <span data-rw-start="1863.96" data-rw-transcript-version="2">
 Another con here, loops are possible if
 </span>
 <span data-rw-start="1866.52" data-rw-transcript-version="2">
 prompts are sloppy, right? So, you can
 </span>
 <span data-rw-start="1868.48" data-rw-transcript-version="2">
 you can really generate some bad loops
 </span>
 <span data-rw-start="1870.44" data-rw-transcript-version="2">
 that are going to really chew up
 </span>
 <span data-rw-start="1871.68" data-rw-transcript-version="2">
 your token usage if your prompts are
 </span>
 <span data-rw-start="1873.44" data-rw-transcript-version="2">
 sloppy, right? You need an end state,
 </span>
 <span data-rw-start="1874.96" data-rw-transcript-version="2">
 right? Let's see if our agents have hit
 </span>
 <span data-rw-start="1876.12" data-rw-transcript-version="2">
 their end state yet. Okay, great. So,
 </span>
 <span data-rw-start="1877.48" data-rw-transcript-version="2">
 Yeah, so we are approaching the end
 </span>
 <span data-rw-start="1879.04" data-rw-transcript-version="2">
 state, right? My agent is making
 </span>
 <span data-rw-start="1881" data-rw-transcript-version="2">
 Progress. It is creating this agent sandbox EXE dev skill. Okay, so that's great.
 </span>
</p>
<p>
 <span data-rw-start="1883.52" data-rw-transcript-version="2">
 This prompt obviously was not sloppy. I don’t write very a ton of sloppy prompts anymore, but this is a risk of this strategy, right? And then there’s just like general costs, right?
 </span>
 <span data-rw-start="1889.48" data-rw-transcript-version="2">
 Cost scales linearly with agent count plus communication bounce. And so, there’s a bunch of laws around the perfect number of actors to have in a team, right? Inside of your communication channel.
 </span>
</p>
<p>
 <span data-rw-start="1892.76" data-rw-transcript-version="2">
 That’s kind of what this, you know, showcases, right? There’s some magical number, Dunbar’s number, or something. I wouldn’t worry about that too much.
 </span>
 <span data-rw-start="1894.28" data-rw-transcript-version="2">
 I would just worry about like, what’s useful? How can I deploy bidirectional agents, bidirectional peer-to-peer agents that it’s actually useful across devices, or on the same device, right?
 </span>
</p>
<p>
 <span data-rw-start="1911.8" data-rw-transcript-version="2">
 The key here is peer-to-peer. And just make it as useful as possible. If you find that three agents, ten agents, whatever is too much,
 </span>
 <span data-rw-start="1927.76" data-rw-transcript-version="2">
 Then just trim them. So, it's not a huge
 </span>
 <span data-rw-start="1929.16" data-rw-transcript-version="2">
 con, but it's important to uh take into
 </span>
 <span data-rw-start="1931.16" data-rw-transcript-version="2">
 account, right? And I think the last con
 </span>
 <span data-rw-start="1933.28" data-rw-transcript-version="2">
 is, be careful not to just fall back
 </span>
 <span data-rw-start="1936.4" data-rw-transcript-version="2">
 into the orchestration pattern. Unless
 </span>
 <span data-rw-start="1938.4" data-rw-transcript-version="2">
 you need it, right? If you need
 </span>
 <span data-rw-start="1939.4" data-rw-transcript-version="2">
 orchestration pattern, just build that.
 </span>
</p>
<p>
 <span data-rw-start="1940.92" data-rw-transcript-version="2">
 This is kind of nice though still cuz
 </span>
 <span data-rw-start="1942.96" data-rw-transcript-version="2">
 you can compose peer-to-peer agent
 </span>
 <span data-rw-start="1944.84" data-rw-transcript-version="2">
 communication back into a orchestration
 </span>
 <span data-rw-start="1947.52" data-rw-transcript-version="2">
 pattern where you have more of a
 </span>
 <span data-rw-start="1948.44" data-rw-transcript-version="2">
 top-down format where one agent's
 </span>
 <span data-rw-start="1950.2" data-rw-transcript-version="2">
 leading the rest. That's fine, too,
 </span>
 <span data-rw-start="1952.32" data-rw-transcript-version="2">
 right? As I mentioned, you know, we're
 </span>
 <span data-rw-start="1954" data-rw-transcript-version="2">
 exploring the state space of what's
 </span>
 <span data-rw-start="1955.48" data-rw-transcript-version="2">
 possible. This is equally as valuable,
 </span>
 <span data-rw-start="1957.88" data-rw-transcript-version="2">
 but peer-to-peer's advantage is that it
 </span>
 <span data-rw-start="1960.8" data-rw-transcript-version="2">
 is flat and there's no hierarchy, right?
 </span>
 <span data-rw-start="1963.28" data-rw-transcript-version="2">
 That's the advantage, right? Your agents
 </span>
 <span data-rw-start="1964.92" data-rw-transcript-version="2">
 are working together. It's not a
 </span>
 <span data-rw-start="1966.24" data-rw-transcript-version="2">
 delegation stream. So, these are some of
 </span>
 <span data-rw-start="1968.08" data-rw-transcript-version="2">
 the pros and the cons of this system. I
 </span>
 <span data-rw-start="1969.4" data-rw-transcript-version="2">
 think it's important to address the
 </span>
 <span data-rw-start="1970.68" data-rw-transcript-version="2">
 upside and the downside, right? Again,
 </span>
 <span data-rw-start="1972.12" data-rw-transcript-version="2">
 if you're doing engineering, you need to
 </span>
 <span data-rw-start="1973.2" data-rw-transcript-version="2">
 Address both of them. So, this is yet
 </span>
 <span data-rw-start="1974.92" data-rw-transcript-version="2">
 another multi-agent orchestration system
 </span>
 <span data-rw-start="1977.28" data-rw-transcript-version="2">
 that you can use to push what you can do
 </span>
 <span data-rw-start="1979.76" data-rw-transcript-version="2">
 with your agents in the age of agents.
 </span>
</p>
<p>
 <span data-rw-start="1981.6" data-rw-transcript-version="2">
 Right? And the goal is the same. We're
 </span>
 <span data-rw-start="1982.96" data-rw-transcript-version="2">
 not really changing. We're not doing
 </span>
 <span data-rw-start="1984.32" data-rw-transcript-version="2">
 anything new here on the channel. What
 </span>
 <span data-rw-start="1986.2" data-rw-transcript-version="2">
 we are doing week after week is, we're
 </span>
 <span data-rw-start="1987.68" data-rw-transcript-version="2">
 increasing trust and scale of our
 </span>
 <span data-rw-start="1990.68" data-rw-transcript-version="2">
 agentic systems. All right? You can see
 </span>
 <span data-rw-start="1992.92" data-rw-transcript-version="2">
 this final reviews coming in. This is
 </span>
 <span data-rw-start="1994.68" data-rw-transcript-version="2">
 coordinated agents working together.
 </span>
</p>
<p>
 <span data-rw-start="1996.52" data-rw-transcript-version="2">
 Double-checking their work. And you can
 </span>
 <span data-rw-start="1997.84" data-rw-transcript-version="2">
 see here, our tokens are starting to
 </span>
 <span data-rw-start="1999.68" data-rw-transcript-version="2">
 stack up. We have 2 million available,
 </span>
 <span data-rw-start="2002.4" data-rw-transcript-version="2">
 but it's split in half. One is focused
 </span>
 <span data-rw-start="2004.64" data-rw-transcript-version="2">
 on exe.dev, one is focused on e2b, but
 </span>
 <span data-rw-start="2007.6" data-rw-transcript-version="2">
 our agents are still coordinating on the
 </span>
 <span data-rw-start="2009.6" data-rw-transcript-version="2">
 same information. We're making sure that
 </span>
 <span data-rw-start="2011.12" data-rw-transcript-version="2">
 we're hitting feature parity. We're
 </span>
 <span data-rw-start="2012.2" data-rw-transcript-version="2">
 making sure that everything looks good.
 </span>
</p>
<p>
 <span data-rw-start="2013.72" data-rw-transcript-version="2">
 Of course, I'm going to run more tests
 </span>
 <span data-rw-start="2015.36" data-rw-transcript-version="2">
 on this and make sure that this looks
 </span>
 <span data-rw-start="2016.4" data-rw-transcript-version="2">
 good, but I can almost guarantee you
 </span>
 <span data-rw-start="2017.88" data-rw-transcript-version="2">
 this is going to work out of the box.
 </span>
</p>
<p>
 <span data-rw-start="2019.24" data-rw-transcript-version="2">
 Because I had two agents, two
 </span>
 <span data-rw-start="2020.8" data-rw-transcript-version="2">
 state-of-the-art agents working together
 </span>
 <span data-rw-start="2022.56" data-rw-transcript-version="2">
 to get this shipped out. Enabling
 </span>
 <span data-rw-start="2024.36" data-rw-transcript-version="2">
 specialized agents that chat together on
 </span>
 <span data-rw-start="2026.44" data-rw-transcript-version="2">
 device and across devices is a unique
 </span>
 <span data-rw-start="2028.68" data-rw-transcript-version="2">
 advantage you can add to your agentic
 </span>
 <span data-rw-start="2031.44" data-rw-transcript-version="2">
 systems, specifically to your agent
 </span>
 <span data-rw-start="2033.4" data-rw-transcript-version="2">
 harness. This pattern and patterns like
 </span>
 <span data-rw-start="2035.52" data-rw-transcript-version="2">
 this more and more of these patterns are
 </span>
 <span data-rw-start="2036.92" data-rw-transcript-version="2">
 going to emerge. They're impossible if
 </span>
 <span data-rw-start="2039.4" data-rw-transcript-version="2">
 you're using, you know, the
 </span>
 <span data-rw-start="2040.88" data-rw-transcript-version="2">
 out-of-the-box agents from Anthropic,
 </span>
 <span data-rw-start="2043.04" data-rw-transcript-version="2">
 from OpenAI, from Google. It's
 </span>
 <span data-rw-start="2044.56" data-rw-transcript-version="2">
 impossible when you're renting your
 </span>
 <span data-rw-start="2046.52" data-rw-transcript-version="2">
 agent harness, okay? To be clear, I
 </span>
 <span data-rw-start="2048.6" data-rw-transcript-version="2">
 still use Claude Code all the time. It's
 </span>
 <span data-rw-start="2050.159" data-rw-transcript-version="2">
 a great tool. I’m going to continue to
 </span>
 <span data-rw-start="2051.56" data-rw-transcript-version="2">
 use it, but more and more I’m reaching
 </span>
 <span data-rw-start="2053.12" data-rw-transcript-version="2">
 for the Pi agent harness to build the
 </span>
</p>
<p>
 <span data-rw-start="2054.879" data-rw-transcript-version="2">
 exact experience and products that I’m
 </span>
 <span data-rw-start="2057.48" data-rw-transcript-version="2">
 looking for, right? And this pattern
 </span>
 <span data-rw-start="2059.159" data-rw-transcript-version="2">
 adds to that bag of tricks that you and
 </span>
 <span data-rw-start="2061.6" data-rw-transcript-version="2">
 I can now deploy in our agent harness if
 </span>
 <span data-rw-start="2064.44" data-rw-transcript-version="2">
 you own your agent harness. I’m going to
 </span>
 <span data-rw-start="2066.159" data-rw-transcript-version="2">
 be adding these two extensions to the Pi
 </span>
 <span data-rw-start="2068.879" data-rw-transcript-version="2">
 Versus Claude Code codebase here,
 </span>
 <span data-rw-start="2070.679" data-rw-transcript-version="2">
 available to you, link in the
 </span>
 <span data-rw-start="2072.2" data-rw-transcript-version="2">
 description. I'm really excited for some
 </span>
 <span data-rw-start="2074.08" data-rw-transcript-version="2">
 of the big ideas I have to share with
 </span>
 <span data-rw-start="2075.399" data-rw-transcript-version="2">
 you here on the channel coming up. I'm
 </span>
 <span data-rw-start="2077.44" data-rw-transcript-version="2">
 waiting for that next Gemini model
 </span>
 <span data-rw-start="2079.04" data-rw-transcript-version="2">
 launch to really showcase one of these
 </span>
 <span data-rw-start="2080.8" data-rw-transcript-version="2">
 next-gen patterns. So, make sure you
 </span>
 <span data-rw-start="2082.28" data-rw-transcript-version="2">
 like, make sure you subscribe, join the
 </span>
 <span data-rw-start="2083.56" data-rw-transcript-version="2">
 journey so you don't miss that. You know
 </span>
 <span data-rw-start="2085.44" data-rw-transcript-version="2">
 where to find me every single Monday.
 </span>
</p>
<p>
 <span data-rw-start="2087.399" data-rw-transcript-version="2">
 Stay focused and keep building.
 </span>
</p>