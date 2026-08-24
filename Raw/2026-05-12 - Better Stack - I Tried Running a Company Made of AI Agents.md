---
title: "I Tried Running a Company Made of AI Agents"
source: "youtube"
url: "https://www.youtube.com/watch?v=xZ7OmRz2i7o"
author: "Better Stack"
published: "2026-05-12"
created: "2026-08-24"
duration: "0:07:27"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "business"
  - "local-llm"
  - "skills"
  - "video-gen"
summary: "I gave three AI agents the same repo and together they formed a company. One tried to build the feature, one rewrote the architecture, and one opened and dealt with all the tickets. With no structure, every multi-agent setup slowly turns into confusion and racks up the bill."
---

# I Tried Running a Company Made of AI Agents

![I Tried Running a Company Made of AI Agents](https://www.youtube.com/embed/xZ7OmRz2i7o)

## Description

In this video, I test Paperclip, the open source control plane for AI agent teams that just exploded on GitHub, and show how it turns isolated AI agents into a structured AI company with org charts, tickets, budgets, heartbeats, audit logs, and persistent workflows.

AI agents are getting insanely good at writing code but the second you try running multiple agents together, everything falls apart. Paperclip fixes that with AI companies.

🔗 Relevant Links
Paperclip Repo - https://github.com/paperclipai/paperclip
Paperclip - https://paperclip.ing/

❤️ More about us
Radically better observability stack: https://betterstack.com/
Written tutorials: https://betterstack.com/community/
Example projects: https://github.com/BetterStackHQ

📱 Socials
Twitter: https://twitter.com/betterstackhq
Instagram: https://www.instagram.com/betterstackhq/
TikTok: https://www.tiktok.com/@betterstack
LinkedIn: https://www.linkedin.com/company/betterstack

📌 Chapters:
0:00 Why AI Agents Fail in Real Projects
0:39 The Real Problem With Multi-Agent AI Workflows
1:46 Setting Up Paperclip Locally (npx paperclipai onboard)
2:00 Creating an AI Dev Team With CTO + Engineer Agents
3:17 Looking at the Company Codebase
3:29 Testing the Output of the Company
3:40 Why Paperclip Is Different From CrewAI & AutoGen
4:50 What Developers Actually Like About Paperclip
4:12 The Biggest Problems With AI Agent Companies
6:00 Why AI Agents Still Burn Tokens & Go Rogue
6:30 Write Better SKILLS.md Files
7:00 Do You Even Need This?
7:15 Final Thoughts

## Transcript

I gave three AI agents the same repo and together they formed a company. One tried to build the feature, one rewrote the architecture, and one opened and dealt with all the tickets. With no structure, every multi-agent setup slowly turns into confusion and racks up the bill. This is paperclip and it's trying to fix that. One command gives you local control plane for AI agents with organizational charts, tickets, budgets, audit logs, and even heartbeats. It's just crossed over 64,000 stars on GitHub. Let's set up our own company with a few AI agents in a couple minutes. Now, here's the thing with agents. A single agent feels nice. You give it a task, it writes some code. Great job. Then you give a second agent, maybe even a third agent. And what happens is suddenly that just turns into management work. Who owns the task? That's the question. Who's remembering the goal out of this and who stops the agent when it starts doing the wrong thing? That's the problem paperclip is trying to solve. Raw agents working alone are great, useful, but hard to coordinate. Paperclip turns them into a team or I guess in this case it's called a company. We define a company goal, we create an organizational chart, maybe there's a CEO, a CTO, two engineers, and a research agent. Then paperclip coordinates the work through tickets, heartbeats, your budgets, approvals, and traceability. We can see the task, who assigned it, how much it actually spent on that task, and whether it's still connects to the end goal. Less vibes-based orchestration, let's actually see this live. If you enjoy coding tools to speed up your workflow, be sure to subscribe. We have videos coming out all the time. All right, now watch this. In a clean terminal, I'm just going to run NPX paperclip AI onboard. That starts up the local setup. Now, a few moments later, Paperclip is running with a dashboard. I have local services, Postgres comes with it, and off. This is the whole UI here now, where I can actually create a new company. I'm going to create a new company and call it Dev Tools Company, or really whatever you're trying to build. For this, I'm going to say this goal. The goal is simple. I want to build and ship a URL shortener MVP this week. Now, I can add a CTO agent, then I can add two engineers through adapters. One of these engineer agents owns the backend, the other owns the frontend and test coverage. Now, before I hit start, I'm going to set the budget. And this part's what really matters, because the goal is to not let the agents cook my API till it will explode. No, the goal is controlled autonomy. I also need to set the path to my working directory where the code is going to be output. So, I'm going to set that here. Now, I can hit those heartbeats, and I can start it. And let's watch the board. The agents wake up on heartbeat. The CTO breaks the goal into tickets. Our engineers here, they're now picking up work. So, you can see delegation, tickets ancestry, status changes, the budget counter, all of this tied together. And now, the first implementation task is already moving toward a code commit. This actually took quite a bit of time to run. But, I guess having all these agents together, that makes a little sense. But, still, it's not the fastest, especially if you're trying to scale this even more. This is not one agent sitting in a chat box anymore. This is now a small company that's running by us creating these agents. CEO, CTO, all these engineers. Now, this is where people get confused. At first glance, Paperclip sounds like another agent framework, another CrewAI, another AutoGen, another LangGraph style workflow. That's not really the point. Those tools are great when you want a workflow, right? So, for example, I want a researcher, then planner, then writer, then reviewer. Yeah, sure. Of course, that's useful. That's why we use them. But, Paperclip is aiming at a level higher. It's not just the workers anymore. It's the company that's kind of surrounding these workers in this organizational chart to really help things build out. Think of it like this. A single agent is just an employee. A workflow is like your checklist. Paperclip is the manager, the organizational chart, the ticket board, the budget system, the audit log. That is Paperclip as the manager. So, questions you're already asking yourself now, can an agent write code? Well, we already know it can. That's the purpose of this. It's generating that now. The harder questions are, can it work on the right task? Can it stop when it actually should? Can it hand off work clearly? Can I inspect what is even happening here? And the short answer to all of those is yeah, it can. Paperclip gives you state, heartbeats, budget, hierarchy, logs. It even gives you portable templates and a dashboard that feels more like Jira or Linear for agents than another chat window. You stop prompting one agent and start controlling this mini organization. Many of us probably still bounce between terminals and setups. One terminal for Claude code, a tab for Cursor, an agent for research, one script for GitHub issues, right? All of these different windows we're bouncing between, but Paperclip gives all of that a shared operating model. Now, the mental model for all of this actually changes for us. So, instead of saying, "Hey, please build this future." What we're actually saying now is something more along the lines of, "This company's goal is to ship this product. Here are the rules in the company. Here's the organizational chart, and here's the budget. Here's what needs approval. Now, run." Now, being honest here, the structure is nice, right? Tickets, ancestry, delegation, all of that, right? Multi-agent work is easier to reason about by having this instead of saying the agent did something, bravo. You can actually see who assigned that work, why it exists, and where it fits into our code. Being able to set budgets is also huge. A lot of agent tools treat costs like something you check after the fact. Paperclip makes cost part of the whole control loop. We set the budget before we execute. It's self-hosted and open-source, again, huge win there. So, you can run it locally, inspect it, modify it, and connect it to the agents you're already using. But, at the same time of all this good stuff, the same structure that makes Paperclip powerful can also be really annoying. If your rules are bad, agents can create tickets about nonsense. I wanted a URL shortener here, simple, but now maybe my CTO agent has opened this whole other plan that I didn't even want. So, no thanks to that. Token burn is also real, right? This is why we have budgets to control this, but it doesn't fix sloppy prompts or vague rule definitions. And guys, if your skill MD files suck, your company behaves like a confused startup, right? So, skills MD, that's what needs the strength here, right? And finally, honestly, if you're doing a simple script, this is a complete overkill. I just wanted to test this out. I did not need this for this project, but if you just want one agent to summarize a file or patch a bug, you don't need this, right? This is for building out a lot more, having more of these agents working together. It's definitely worth using, but it's not for everything. If you enjoy coding tools and tips like this, be sure to subscribe. We'll see you in another video.
