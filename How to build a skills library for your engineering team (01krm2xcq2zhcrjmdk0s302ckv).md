---
categories:
  - "[[Resources]]"
domain: engineering
title: "How to build a skills library for your engineering team"
source: "https://thenewstack.io/engineering-team-skills-library/"
author: "Zohar Einy"
published: 2026-05-13
created: 2026-05-14
description: "How to build a skills library for your engineering team: standardize coding"
tags:
  - to-process
  - agent-skills
---

![Featued image for: How to build a skills library for your engineering team](https://cdn.thenewstack.io/media/2026/05/1aab128e-beatriz-camaleao-o_ezmwg-nfo-unsplash-1024x731.jpg)Beatriz Camaleão for Unsplash+
A few months ago, we realized that every engineer on our team was running a different version of their AI coding assistant.


Not the models, they were all using the latest ones.


But the skills their agents were using were all over the place. And skills make all the difference.


Some [engineers configured their own skills](https://thenewstack.io/5-engineering-skills-to-prioritize-in-the-ai-driven-era/). Others copied from older versions. And some just took some skills they found online.


And we had no visibility into any of it because skills are local config files.


So to solve it, we built a library. Now every engineer runs one command, and their agent starts from the same foundation.


They get the required company standards pulled automatically, and they can also load optional skills based on what they’re building.


Here’s how we built it:


## Step 1: We put all our skills in a library


Skill files are just [Markdown files that tell AI agents](https://thenewstack.io/skills-vs-mcp-agent-architecture/) how your company works. You might have one for security conventions, one for incident protocols, and one for coding standards.


Here’s an example of our triage incident skill:


![Screenshot of a triage incident skill example](https://cdn.thenewstack.io/media/2026/05/c23e914b-1-1024x712.png)Screenshot of a triage incident skill example
I’d suggest keeping them in version control and connecting them to the services and teams they’re relevant to.


There are a couple of reasons why you’d want to keep them in version control. Firstly, they change a lot, and you want to keep track of those changes. Second, the destination for these skills is usually an IDE, so having them in Git makes it easy for developers to sync them with their IDE.


Lastly, and most importantly for us, having skills with GitHub (or any version control system) lets us auto-discover them in Port, where we can connect them to everything else.


When skills are scattered (we call them “shadow skills”), we find it useful to draw on them from as many sources as possible.


![Screenshot of catalog discovery skill](https://cdn.thenewstack.io/media/2026/05/d270d5ae-2.png)Screenshot of catalog discovery skill
We also get inspiration for skills from other places, such as PR review comments, ADRs, incident postmortems, onboarding docs, and community libraries like skills.sh.


Once you have your library assembled, it’s time to organize it.


![Screenshot of skills library](https://cdn.thenewstack.io/media/2026/05/8c0d6eac-3-1024x689.png)Screenshot of skills library
## Step 2: Organize into groups and decide what’s required


A library of 200 individual skills isn’t really useful to anyone. Nobody wants to browse 200 files and find the few relevant ones.


To solve that, we group them by use case: engineering standards, frontend, backend, data, infrastructure, etc.


That way, when an engineer gets set up, they pick and import an entire group rather than individual files.


Skills should also be either required or optional.


Required skills are non-negotiable. Every engineer and agent gets them automatically, no opt-out:


* **Security**: monitors for prompt injection, flags attempts to exfiltrate sensitive data, and blocks unauthorized external API calls
* **Coding conventions**: how your team handles errors, names directories, structures TypeScript, writes tests
* **Rule governance**: where skill files live, how they get named, how changes get versioned


Optional skills are role-specific and load only when relevant:


* **Django backend**: fat models, thin views, migration discipline (expand-migrate-contract), idempotent Celery tasks. Activates for \*.py files in the backend.
* **React components**: component structure, RSC vs. client component rules, [Web Vitals priorities](https://thenewstack.io/html-priority-hints-help-etsy-rock-the-google-core-web-vitals/). Activates for `src/components/**/*.tsx`.
* **Incident triage**: walks through affected services, recent deployments, root-cause categories, and stakeholder update format. Only useful when something’s on fire.


## Step 3: Engineers get the skills automatically


Engineers can get all the updated skills by running the `port skill init` from their terminal. It connects to the library using their existing permissions, pulls the required groups automatically, then prompts them to choose which optional groups they want: frontend, data, and ML, whatever matches their work.


![Screenshot of Port's load skills feature](https://cdn.thenewstack.io/media/2026/05/53bff19d-4-1024x342.png)Screenshot of Port's load skills feature
![A screenshot showing port's load skills feature prompting the user to select AI tools which should have hooks installed ](https://cdn.thenewstack.io/media/2026/05/76147652-5-1024x432.png)A screenshot showing port's load skills feature prompting the user to select AI tools which should have hooks installed 
![A screenshot showing port's load skills feature prompting the user to select skill groups they would like to sync](https://cdn.thenewstack.io/media/2026/05/4a5cae93-6-1024x485.png)A screenshot showing port's load skills feature prompting the user to select skill groups they would like to sync
Skills land directly in `.cursor/` or whichever IDE config folder they use.


![Screenshot showing that skills land in the selected IDE config folder.](https://cdn.thenewstack.io/media/2026/05/ea996adc-7.png)Screenshot showing that skills land in the selected IDE config folder.
Two things make this work really well for us:


First, updates. Every engineer in Cursor has an automation that listens for changes to skills in Port and pulls new required skills and updates existing ones.


Second, we make it easy for developers to contribute back. Engineers can submit new skills directly from their IDE. Then they go through review, get merged, and get redistributed to the whole team, basically the same loop as an open source contribution. The library gets smarter over time without the platform team having to own every skill themselves.


## Step 4: The feedback loop


We also have a meta-skill: a skill whose job is to watch for repeated corrections. When you fix the agent on the same thing twice in a session, it surfaces: “You’ve corrected me on this twice. Want me to write a skill for it?” If you say yes, it automatically kicks off the skill-creator, preloaded with what it just observed.


The loop becomes self-closing. The agent notices its own gaps, proposes the fix, and routes it into the same review and distribution flow. The platform team still reviews everything, but they’re not waiting for engineers to notice and submit manually. The library improves in the background.



>  “The loop becomes self-closing. The agent notices its own gaps, proposes the fix, and routes it into the same review and distribution flow.”
> 
>  


![Example of the agent noticing a repeated correction from a user, and automatically kicking off the skill-creator.](https://cdn.thenewstack.io/media/2026/05/e0e4d004-8-1024x575.png)Example of the agent noticing a repeated correction from a user, and automatically kicking off the skill-creator.
## Step 5: Track if it’s working


Before the skills library, we had no idea what skill any agent on the team was running. Now we have a dashboard that tells us who’s set it up, which groups they pulled, and when they last synced. If someone is running on a six-month-old version of a skill, or never ran `skill init` at all, we see it.


We also track skill health: how old each skill is, when it was last updated, and who owns it. Skills go stale just like documentation does. Anything that hasn’t been touched in 90 days gets flagged.


![Screenshot showing Port's Skills Library interface](https://cdn.thenewstack.io/media/2026/05/83f2364b-9-1024x626.png)Screenshot showing Port's Skills Library interface
The contribution pipeline is basically a PR queue for the library. Skills submitted, in review, merged, rejected.


![Screenshot showing the contribution pipeline.](https://cdn.thenewstack.io/media/2026/05/e7646f32-10-1024x741.png)Screenshot showing the contribution pipeline.
The metric I find most interesting is agent quality signals. We track which review comments keep appearing on AI-generated PRs. If the same comment appears more than a few times among different engineers, it automatically contributes to a skill or creates a new one.


And we track coverage by team: which teams have required skills loaded, which optional groups they’ve pulled, or where the gaps are.


## Why this matters: agent sprawl


Your team probably already has an agent sprawl problem, but you may not know it yet: hundreds, if not thousands, of unofficial different skills, agents, and MCP servers are being created and used.



>  “Your team probably already has an agent sprawl problem, but you may not know it yet.”
> 
>  


A skills library is part of the fix. And once you have one, someone on your platform team can actually answer the question: what does every agent in this org know right now? At most companies, nobody can answer that.


## Build it yourself


If you want to set this up, the demo and full technical guide are in the comments. It’s just a few hours of work for one platform engineer, and once it’s running, the whole team benefits automatically.