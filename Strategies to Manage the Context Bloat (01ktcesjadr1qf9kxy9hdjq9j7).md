---
categories:
  - "[[Resources]]"
domain: engineering
title: "Strategies to Manage the Context Bloat"
source: "https://www.reddit.com/r/PiCodingAgent/comments/1t6eth2/strategies_to_manage_the_context_bloat/"
author: "mtomas7"
published: 2026-05-07
created: 2026-06-05
description: "Hi all, I am pretty new to agentic workflows, but in my little experiments,"
tags:
  - to-process
  - context-management
---

**[r/PiCodingAgent](https://www.reddit.com/r/PiCodingAgent/)**


# [mtomas7](https://www.reddit.com/user/mtomas7/)



 (2026-05-07 16:00:59)


Hi all, I am pretty new to agentic workflows, but in my little experiments, I noticed that Pi would go to search for its docs, and those docs would quickly fill the larger portion of the context window.


Many users report that compaction usually has a negative effect, so I disabled compaction and now I would complete several logical parts, then manually instruct the Agent to prepare a "handing-off package" for the next session, where I would start with that summary and a fresh context window. Although I saw an interesting post about letting Agent handle its own context: <https://www.reddit.com/r/PiCodingAgent/comments/1t4ja1e/comment/ok8s3s9/>


It looks to me that subagents would be a solution to this issue, but I had an impression that Pi creator is not in favor of subagent idea. It would be interesting to hear from experienced folks which subagent plugins you use, what your workflow is, and whether it is effective at addressing context bloat. And how it would be better/worse than using Tmux (another concept I am trying to wrap my head around), or perhaps subagent, and Tmux can be used together?


Thank you!





## [Craiglal-](https://www.reddit.com/user/Craiglal-/)



 (2026-05-07 16:08:19)


I guess Pi is designed to have only tools you need and there are a few top rated packages for pi which add widely configurable subagents. I do use one of them to split the work to specialist agents with different models for each





### [TeijiW](https://www.reddit.com/user/TeijiW/)



 (2026-05-09 22:49:20)


How are you doing that? Just let the "orchestrator" decide or the instructions are more strict? 





#### [Craiglal-](https://www.reddit.com/user/Craiglal-/)



 (2026-05-09 23:01:40)


I have a role based separation for each subagent in the main instructions file, so orchestrator know in which explicit moment should one or another subagent be run. But still sometimes it misses and for huge tasks i use heavy models as orchestrator 





## [e9n-dev](https://www.reddit.com/user/e9n-dev/)



 (2026-05-07 16:22:15)


Heavy use of /tree and /new 😅





### [adamshand](https://www.reddit.com/user/adamshand/)



 (2026-05-09 08:39:44)


Tree is pi's super power for context management!





#### [e9n-dev](https://www.reddit.com/user/e9n-dev/)



 (2026-05-09 11:49:56)


Came handy last night when I tried telling a small model to forget something 🤦‍♂️


Wish I could do the same in real life, haha





## [jeffphil](https://www.reddit.com/user/jeffphil/)



 (2026-05-07 17:00:15)


Loads of discussions 2 days ago: <https://www.reddit.com/r/PiCodingAgent/s/9uGEtbmKfQ>





### [elpapi42](https://www.reddit.com/user/elpapi42/)



 (2026-05-10 00:02:23)


highly recommended!





## [ObjectiveActuator8](https://www.reddit.com/user/ObjectiveActuator8/)



 (2026-05-07 17:19:50)


I’m learning the dark arts of pausing before prompting. Using voice dictation surprisingly increases your prompt size with minimal effort which means the agent has to figure out less and therefore read less docs and keep context leaner.


On the leaner context note, I tried something last night that saved the agent about 12k tokens. Like, in a new session, I gave a prompt the normal way, it read about 5 files to find the answer and the context window was 40k out of 160k tokens (Sonnet 4.6 High). Then I started a new session, this time with my experiment active. Sent the same prompt, it only read 1 file (the right one) and context window was like 28k out of 160k.


The experiment is a tool the ai agent can use via MCP, adding a skill that says “if you don’t know where something is, query this MCP for the answer”. So instead of grepping and reading 5 files to find the function the agent is looking for, it just queries “where’s the authentication service” (for example).


How does it know? I’m calling it “compas”, it indexes your code base, separates chunks of code and embeds them with a local embedding model from Ollama. Then stores your indexed repo in your local Qdrant (you self host these, it makes it a lot faster than other online stuff). So when the agent queries the MCP (also local), MCP queries Qdrant and returns the most likely results for the keyword “authentication service”. Agent gets a preview of the code and what file it is located in, then it goes and reads that file for confirmation. So it’s nothing magical, it just saves the agent from reading 3 or 4 more irrelevant files, which keeps the context a tad smaller. Im thinking of open sourcing it so other people can adapt it to their favorite languages cuz currently it’s optimized for Dart.


TLDR: longer prompts saves you money, do /tree for side quests and experiment with embedding index of repos.





### [Due\_Ebb\_7115](https://www.reddit.com/user/Due_Ebb_7115/)



 (2026-05-07 18:30:49)


Qdrant team member here, hit me up if you ever decide to open source the project. Would love to take a look at it 





#### [ObjectiveActuator8](https://www.reddit.com/user/ObjectiveActuator8/)



 (2026-05-07 19:42:55)


Will do, just gotta finish up a codebase map feature I'm working on and create a new clean repo on gh. thanks for the interest!





##### [Due\_Ebb\_7115](https://www.reddit.com/user/Due_Ebb_7115/)



 (2026-05-07 20:19:03)


We have a community discord, if you wanna share the project there we’ll be happy to promote it 🙂





###### [ObjectiveActuator8](https://www.reddit.com/user/ObjectiveActuator8/)



 (2026-05-08 07:45:43)


got it live on gh https://github(dot)com/alexandroheredia/compas


what's your discord, I actually wanna learn more about Qdrant, see if any improvements can be made to the collection





###### [Due\_Ebb\_7115](https://www.reddit.com/user/Due_Ebb_7115/)



 (2026-05-12 00:04:53)


Just Google Qdrant discord and it should be the first link 





## [juicesharp](https://www.reddit.com/user/juicesharp/)



 (2026-05-07 16:59:23)


Maintainer of rpiv-pi here, so take this with the appropriate salt.


Your current workflow (disable compaction, write a manual handoff, start fresh) is the right instinct. Compaction tends to lose the threads that matter and keep the ones that don't. A summary you wrote yourself almost always beats one the system wrote for you. The real question is whether to keep doing it by hand or let tooling do it.


Subagents and tmux solve different problems and stack fine together. Subagents address context bloat by spawning a child with a narrow brief and a fresh window (could be twins but on different purpose), then collapsing the result back into the parent as a summary. The parent never has to load the docs the child read. Tmux addresses parallelism. Orthogonal. The skepticism you've heard about subagents is usually about general-purpose offloading, where they hide context problems instead of fixing them. Scoped subagents with a specific job (codebase-analyzer, codebase-locator, claim-verifier) earn their keep because each one has a known role and a known output shape.


If you want a worked-out version of all of this, rpiv-pi bundles named subagents with skills that automate the handoff pattern you're already doing manually (`/skill:create-handoff`, `/skill:resume-handoff`). Repo: <https://github.com/juicesharp/rpiv-mono>. Not the only option in this space and not pretending to be. Just the one I built because I had the same problem you do.





### [Craiglal-](https://www.reddit.com/user/Craiglal-/)



 (2026-05-07 17:19:37)


I’m using a few separate packages from this pack, really appreciate the work done





#### [juicesharp](https://www.reddit.com/user/juicesharp/)



 (2026-05-07 17:23:05)


You're welcome. That was the intent: each package stands alone, so people can pick the parts that fit their workflow without committing to subagents or anything else they don't want.





### [mtomas7](https://www.reddit.com/user/mtomas7/)



 (2026-05-07 18:41:29)


Thank you! Eager to try it out!





### [mtomas7](https://www.reddit.com/user/mtomas7/)



 (2026-05-07 19:18:58)


I realized that your 6-step routing reminds me of Daniel Miessler's 7-step algorithm: <https://github.com/danielmiessler/Personal_AI_Infrastructure/tree/main/Releases/Pi>





#### [juicesharp](https://www.reddit.com/user/juicesharp/)



 (2026-05-07 20:20:48)


Hadn't seen that one, thanks, I'll take a look. Most of it (but smaller part of the process) was ported from a plugin we already quite successfully use in house for Claude Code/Opus 4.7. The goal is to see how the same patterns hold up against Anthropic models outside the CC harness, and how far open-weight models like MiMo and GLM can be pushed on the same workflow.





## [aeroumbria](https://www.reddit.com/user/aeroumbria/)



 (2026-05-11 09:02:56)


I just don't trust compaction and ad-hoc subagent handoff. To me, they are two sides of the same coin - a point of failure for concept to drift and for critical information to be lost. I prefer something physical that persists throughout a standalone task (openspec plans are my personal choice, but temporary findings collection and progress tracking files are also helpful) and can be repeatedly validated against reality however many times you want. This way, you can always keep some amount of "restorative force" on your agent trajectory, while keeping the context small.





## [Hot\_Sentence2303](https://www.reddit.com/user/Hot_Sentence2303/)



 (2026-05-19 12:42:36)


[ Removed by Reddit ]