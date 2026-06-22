---
title: "New AI coding paradiagm - OpenAI Symphony"
source: "https://www.youtube.com/watch?v=M_AmPWmkpwA"
author: "AI Jason"
published: 2026-05-02
created: 2026-05-13
description: "Get my codebase harness setup & skills: https://www.aibuilderclub.com/"
tags:
  - to-process
  - orchestration
---

So, Open AI just released this open-source repo called Symphony. On the surface level, it looks like a orchestrator that allow you to manage coding agents through ticket tracker like linear, but it is a lot more than just connecting linear. It's a totally different way of interacting with agents. So, the way we use coding agent has shifted a lot for the past few months. From initially just the auto-complete to primarily interactive session with coding agent to now most of us around two or three different sessions in parallel, each working isolated work tree for different features or bug fixing. And then new 

tooling like Super set or conductor that has been introduced to help you run and manage different interactive coding sessions easier. The problem is that even with those tools, many people, including myself, will feel this burden when we are working on more than like three different sessions cuz we just can't context switch every minute. And I personally have had multiple times sending the wrong instruction to the wrong thread. So, ceiling of how much we can get out from those coding agent is no longer the model capability, but our own attention and cognitive load. And the recent project Symphony is so 

interesting is that Open AI's engineering team had this realization that the current experience has been orienting around coding session, merge PRs, but in reality for the past decades, software workflow are largely organized around deliverables, things like issues, tasks, tickets, milestones. Engineer leaders have been managing massive amount of tasks across thousands of workers, not by reviewing everyone's PR, but looking at final outcomes using tools like linear and Atlassian. And Open AI's proposed solution is move human up a level. Instead of managing two three interactive sessions, you 

manage tickets. The agent works at ticket level, report back through the ticket itself, and you stay in the loop without monitoring individual sessions. The ticket tracker becomes state machine itself. And the way Symphony makes this work is almost embarrassingly simple, but very effective. It's a background process. You run it once, point to a workflow file, which we'll talk a bit more, and then it runs forever. Every 30 seconds, this background process will glance through your linear board. If it finds any ticket in to-do slots, it will set up an isolated workspace and start agent in that workspace. And the whole 

system has three key components. One is the scheduler, the background process that is pulling ticket data and set up workspace, manage session life cycle, and a workflow.md file that lives inside your repo. It contains configuration of scheduler and detailed instruction for coding agent to know how to work with those ticketing system. And those external system like linear is a durable state machine for human to interact with agent. And this whole setup is actually very flexible. You don't have to use linear. You don't have to use Code X. You can actually customize to whatever you want. But overall implementation 

concept is what's interesting. And the most interesting part is this workflow.md file. It basically break down into two parts. The top part is the YAML front matter. It configures scheduler directly, like which linear project it is, what type of ticket it should pick up, where should agent create isolated workspace, and even programmatic hooks to run after it set up the workspace. And this is very useful, so you no longer need to rely on agent to set those things up. As well as how many agents can be run in parallel and specific agent settings. And after that, the bottom half is a markdown file. This is the prompt agent every 

single turn details rendered in. It's a standard operating procedure for handling tickets in this repo. How should agent plan task? How should agent go validate its work? And what would be considered as done? And when should outreach for human review? And what I love about this design is that the same file just live inside your repo, so it's version controlled and can be changed through normal pull request. And the file itself contains some programmatic rule that controls scheduler and also what an agent does. There's no separate config service, no admin panel, no UI at all. And the team only code base on this 

workflow. So, when you onboard a new agent capability of adding new step in the process, you just very easily change this markdown file, and the rest will just follow. And this whole system is designed very flexible. You don't have to use Code X, and you don't have to use linear. They have one example implementation in Elixir, which is a programming language. But they have this spec.md file that's detailing how this framework or system is designed. So, you can just drop this file to any coding agent and ask it to build and design a system in any programming language. There are already a lot of different 

community attempts. Like someone building custom TUI based on the task data. And also another person already rebuilt it to support Cloud Code as agent harness. And I'm going to show you step by step how you can set these things up. But orchestrating agent is only part of the work. As Open AI mentioned, this whole thing only works if your coding agent's environment is set up properly in a way that it can complete tickets end-to-end atomically, which you can call it harness engineer, but fundamentally just whether your environment or code base has been set up in the right way, so agent has everything it needs to complete task 

end-to-end. And typical things like is the system bootable, so agent can just run a script to get everything set up without spending time to figure that part out. And does the system has a proper documentation structure for different things. And I think most people does have these two things properly set up in your code.md or agent.md file. But the part I think most of team didn't set up is those self-verifying tools. They allow agent to do an end-to-end test after implementing something. And even submit a video recording to prove that it have tested and it's working in the ticket directly just like in their demo. But in 

the doc, they didn't really mention how they were handling this part. So, I did some research across many major skills. And the best one I found is this Playwright CRI tool. So, I believe many of us are pretty familiar with Playwright MCP, which allow agent to use the browser and do a task, check the logs. But the problem before was that Playwright with MCP setup, it took a huge amount of tokens in context window even when it's not needed. But they have released this Playwright CRI tool alongside agent skill that detailing every single comment. And the most interesting comment is this video 

recording CRI. So, Playwright allow agent to run commands like video start and video stop to capture browser session into a MP4 or WebM video. They even have some pretty advanced video rendering capability where they can add different chapter on the screen. Like here's one example video where it can record its own session and even add new HTML element on top of the screen to annotate the action the agent took. And then upload session into linear, so you can very easily verify if things actually work. And as far as I know, 

other tools like Chrome DevTools MCP or agent browser don't have this video capability out of box. So, this is one very important skill that will make your whole experience complete. And meanwhile, there are also other skills that you should add. And I just take one of the repo I have as example. We have this Playwright CRI tool that has a skill as well as a list of reference for agent to know how to like record a video and tracing the debug logs. And we also have a skill here to tell agent how to start server locally. And because ours is pretty straightforward, so it's just a skill file. But sometimes for more complicated things, you can create 

predefined script as well. So, agent no longer spends cognitive power on those type of stuff. And meanwhile, I also created this linear skill that allow agent to know how to operate linear tickets by using linear API as well as things like upload video evidence of the test. And we actually have more documentations about different parts of system. And in the agent.md or cloud.md file, this is where we have a proper index of different documentation systems, so you can always go and find the relevant information. We also give more detailed debugging skills. For example, we use Grafana to track and store all the logging in production. And 

we add a relevant Grafana log skill in our repo, so the agent can fetch real production logs for bug fixing. And all those things are try to serve one purpose, which is setting up your code base so that your agent can fix bug, building new features, verify things are working fully atomically end-to-end. I put all skills inside AI Build Club, so you can copy-paste and ask your agent to customize for your own code base. I put the link in the description below, so you can join and access. And once you set this up, even though you don't use Symphony, they're still going to be really useful. But after that, this is 

where we can start setting up the Symphony, connect to linear, as well as this workflow.md file. So, once you clone the Symphony repo, you'll see folder like this. You'll have this folder of Elixir. So, this is one version implementing Elixir programming language from Open AI. And most of the time, you can just use this Elixir directly. But if you want to customize it to like connect not linear, but connect to Trello or Jira, you can ask coding agent to customize it or even building a different language by pointing to spec.md file. And here's basically what I did in Python folder. I just point to spec.md file and ask it to 

build a new version in Python. But most of the time, you actually don't need to do that. You can just reuse what Open AI provided. And firstly, you can confirm whether the script is So, you can run script by doing this, which point to the Symphony program that has been built. And run help. So, this should show you the actual command about how to run Symphony. You basically just do Symphony and point to a path to workflow.md file. And by default, you can't just run the Symphony like this. You can run this to bind Symphony command to the specific path. So, just run this. And then you 

can do Symphony, point to a specific workflow.md file. And by default, it will give you this warning. Then you can add this argument to the command, which will set our Symphony background process like this. It will track all the tasks, show you the project, and next refresh time. It will track a specific linear project you set up every 30 seconds. If there any ticket in to-do, it will pick up and show up in this list. And all those configurations are actually defined in workflow.md file. So, in workflow.md file, at the front matter, there is a project slug. And Symphony script will basically read that 

metadata, importing information from a specific project. Same thing for all the other configurations, like how frequently it should pull the ticket data, what are things it should do after setting up a new workspace, how many agent can be run at the same time, and the Code X configuration. But once you set up this, it's basically monitoring the specific Symphony repo with Elixir implementation. What we want to do is apply this to your own workspace. It's actually pretty straightforward. You can just open any coding agent like Code X or Cloud Code, point to the spec.md file and say, "I want to set up Symphony for 

my repo, and we will reuse the Elixir implementation here, and help me build the workflow.md file for my repo." With just one command, coding agent is smart enough to look at your own repo and design a workflow.md file inside there. And this is the one it created for me, including the project slug and API key and all the other configurations. But you do need to set up linear first. If you haven't created linear account yet, just go create a one and then add a new project. And in this project, click on the button here, you can just paste into your coding agent. This thing in the 

middle here is a project slot, or you can manually paste into the workflow.md file as well. And meanwhile, you need to get a linear API key, which you can get by clicking on settings, security and access, and add a new personal API key here. And once you did that, you should run this command, which will save the linear API key globally on your computer. So, every time when agent try to use linear, it can access any projects you have access to. And there are some configuration you should do, which is status. So, Symphony out-of-box are designed for some specials status control flow, like human review status 

and also merging status. Once you put a ticket into do, Symphony will automatically pick up and put that in progress and trigger an agent session. And once agent finish the work, it will change to human review status, so that you can review the work. And once finished, you can set the status to be merging, which will trigger the agent automatically raise a PR from this work. And once you did all that, you can do run Symphony past through your workflow.md file, plus this I understand that this will be running without the usual guardrail comment. And now Symphony will be working and picking up all the tickets in your project here. To 

make it easier, you can also create a new view, set up this board, so that you get this kind of Kanban experience. But to just test, I can just create ticket change the landing page hero copy from your company on autopilot to your AI growth team, and the set up the status to be to do. And this should trigger our agent here. If I go back here, you can see this time it pick up this ticket, and then you can see the agent session show up, and then last agent message here. And depends on your settings, you can also go check this workspace. You can see inside this workspace, it has one workspace per ticket. So, each one 

is running isolated environment. And this example implementation also has uh kind of web UI dashboard that you can visit, and this will list out similar information you will see in terminal here. Not particularly useful, but I just thought I'd mention this. And you can see after a while, this agent changes ticket to in progress status, which reflect in our linear board as well. And if I click on that, agent made a plan and logged all the steps it did. After a few minutes, the agent check off every single items on the checklist, and upload a video recording to verify 

things are working. And as a human, I can just very easily see if things are working or not. And once I mark something as merging, it will also create a PR for me. So, this is a whole end-to-end process and how you set things up. It definitely feels like future. If you hit any blockers, I have more detailed step-by-step breakdown, as well as all skills posted in the AI Build Club. Every week, we have workshop to go through those latest learnings and answer any questions. So, if you're interested, you can click on the link below and join our next batch. But this is project Symphony, how it works and what's the implications. If you found this video useful, please give me a 

subscribe and comment below. Thank you, and I see you next time. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 So, OpenAI just released this
 </span>
 <span data-rw-start="1.28" data-rw-transcript-version="2">
 open-source repo called Symphony. On the
 </span>
 <span data-rw-start="3.76" data-rw-transcript-version="2">
 surface level, it looks like a
 </span>
 <span data-rw-start="5.28" data-rw-transcript-version="2">
 orchestrator that allows you to manage
 </span>
 <span data-rw-start="7.04" data-rw-transcript-version="2">
 coding agents through ticket tracker
 </span>
 <span data-rw-start="8.8" data-rw-transcript-version="2">
 like Linear, but it is a lot more than
 </span>
 <span data-rw-start="10.92" data-rw-transcript-version="2">
 just connecting Linear. It’s a totally
 </span>
 <span data-rw-start="13.08" data-rw-transcript-version="2">
 different way of interacting with
 </span>
 <span data-rw-start="14.76" data-rw-transcript-version="2">
 agents. So, the way we use coding agents
 </span>
 <span data-rw-start="16.76" data-rw-transcript-version="2">
 has shifted a lot for the past few
 </span>
 <span data-rw-start="18.2" data-rw-transcript-version="2">
 months. From initially just the
 </span>
 <span data-rw-start="19.72" data-rw-transcript-version="2">
 auto-complete to primarily interactive
 </span>
 <span data-rw-start="21.68" data-rw-transcript-version="2">
 sessions with coding agents to now most of
 </span>
 <span data-rw-start="23.84" data-rw-transcript-version="2">
 us around two or three different
 </span>
 <span data-rw-start="25.28" data-rw-transcript-version="2">
 sessions in parallel, each working
 </span>
 <span data-rw-start="27.16" data-rw-transcript-version="2">
 on isolated work trees for different
 </span>
 <span data-rw-start="28.64" data-rw-transcript-version="2">
 features or bug fixing. And then new
 </span>
 <span data-rw-start="30.36" data-rw-transcript-version="2">
 tooling like SuperSet or Conductor that
 </span>
 <span data-rw-start="32.64" data-rw-transcript-version="2">
 has been introduced to help you run and
 </span>
 <span data-rw-start="34.56" data-rw-transcript-version="2">
 manage different interactive coding
 </span>
 <span data-rw-start="36.4" data-rw-transcript-version="2">
 sessions easier. The problem is that
 </span>
</p>
<p>
 <span data-rw-start="38.36" data-rw-transcript-version="2">
 even with those tools, many people,
 </span>
 <span data-rw-start="40" data-rw-transcript-version="2">
 including myself, will feel this burden
 </span>
 <span data-rw-start="42" data-rw-transcript-version="2">
 when we are working on more than three different sessions because we just
 </span>
 <span data-rw-start="45.52" data-rw-transcript-version="2">
 Can't context switch every minute. And I
 </span>
 <span data-rw-start="47.8" data-rw-transcript-version="2">
 personally have had multiple times
 </span>
 <span data-rw-start="49.4" data-rw-transcript-version="2">
 sending the wrong instruction to the
 </span>
 <span data-rw-start="50.96" data-rw-transcript-version="2">
 wrong thread. So, the ceiling of how much we
 </span>
 <span data-rw-start="52.96" data-rw-transcript-version="2">
 can get out from those coding agents is
 </span>
 <span data-rw-start="54.96" data-rw-transcript-version="2">
 no longer the model capability, but our
 </span>
 <span data-rw-start="57.2" data-rw-transcript-version="2">
 own attention and cognitive load. And
 </span>
 <span data-rw-start="59" data-rw-transcript-version="2">
 the recent project Symphony is so
 </span>
 <span data-rw-start="60.44" data-rw-transcript-version="2">
 interesting that Open AI's
 </span>
 <span data-rw-start="62" data-rw-transcript-version="2">
 engineering team had this realization
 </span>
 <span data-rw-start="63.88" data-rw-transcript-version="2">
 that the current experience has been
 </span>
 <span data-rw-start="65.36" data-rw-transcript-version="2">
 oriented around coding sessions, merge
 </span>
 <span data-rw-start="67.32" data-rw-transcript-version="2">
 PRs, but in reality, for the past
 </span>
 <span data-rw-start="69.64" data-rw-transcript-version="2">
 decades, software workflows are largely
 </span>
 <span data-rw-start="71.8" data-rw-transcript-version="2">
 organized around deliverables, things
 </span>
 <span data-rw-start="73.48" data-rw-transcript-version="2">
 like issues, tasks, tickets, milestones.
 </span>
</p>
<p>
 <span data-rw-start="75.92" data-rw-transcript-version="2">
 Engineer leaders have been managing
 </span>
 <span data-rw-start="77.48" data-rw-transcript-version="2">
 massive amounts of tasks across thousands
 </span>
 <span data-rw-start="79.32" data-rw-transcript-version="2">
 of workers, not by reviewing everyone's
 </span>
 <span data-rw-start="81.44" data-rw-transcript-version="2">
 PRs, but by looking at final outcomes using
 </span>
 <span data-rw-start="83.88" data-rw-transcript-version="2">
 tools like Linear and Atlassian. And
 </span>
 <span data-rw-start="85.76" data-rw-transcript-version="2">
 Open AI's proposed solution is to move
 </span>
 <span data-rw-start="87.36" data-rw-transcript-version="2">
 human up a level. Instead of managing
 </span>
 <span data-rw-start="89.6" data-rw-transcript-version="2">
 two, three interactive sessions, you
 </span>
 <span data-rw-start="91.52" data-rw-transcript-version="2">
 manage tickets. The agent works at
 </span>
 <span data-rw-start="93.52" data-rw-transcript-version="2">
 Ticket level, report back through the
 </span>
 <span data-rw-start="95.28" data-rw-transcript-version="2">
 ticket itself, and you stay in the loop
 </span>
 <span data-rw-start="97.04" data-rw-transcript-version="2">
 without monitoring individual sessions.
 </span>
</p>
<p>
 <span data-rw-start="98.92" data-rw-transcript-version="2">
 The ticket tracker becomes a state machine
 </span>
 <span data-rw-start="100.6" data-rw-transcript-version="2">
 itself. And the way Symphony makes this
 </span>
 <span data-rw-start="102.52" data-rw-transcript-version="2">
 work is almost embarrassingly simple,
 </span>
 <span data-rw-start="104.76" data-rw-transcript-version="2">
 but very effective. It's a background
 </span>
 <span data-rw-start="106.28" data-rw-transcript-version="2">
 process. You run it once, point to a
 </span>
 <span data-rw-start="108.24" data-rw-transcript-version="2">
 workflow file, which we'll talk a bit
 </span>
 <span data-rw-start="109.96" data-rw-transcript-version="2">
 more about, and then it runs forever. Every 30
 </span>
 <span data-rw-start="111.88" data-rw-transcript-version="2">
 seconds, this background process will
 </span>
 <span data-rw-start="113.36" data-rw-transcript-version="2">
 glance through your linear board. If it
 </span>
 <span data-rw-start="115" data-rw-transcript-version="2">
 finds any ticket in to-do slots, it will
 </span>
 <span data-rw-start="117.44" data-rw-transcript-version="2">
 set up an isolated workspace and start
 </span>
 <span data-rw-start="119.92" data-rw-transcript-version="2">
 agent in that workspace. And the whole
 </span>
 <span data-rw-start="121.48" data-rw-transcript-version="2">
 system has three key components. One is
 </span>
 <span data-rw-start="123.68" data-rw-transcript-version="2">
 the scheduler, the background process
 </span>
 <span data-rw-start="125.16" data-rw-transcript-version="2">
 that is pulling ticket data and set up
 </span>
 <span data-rw-start="127.08" data-rw-transcript-version="2">
 workspace, manage session life cycle,
 </span>
 <span data-rw-start="129.2" data-rw-transcript-version="2">
 and a workflow.md file that lives inside
 </span>
 <span data-rw-start="131.52" data-rw-transcript-version="2">
 your repo. It contains configuration of
 </span>
 <span data-rw-start="133.32" data-rw-transcript-version="2">
 scheduler and detailed instruction for
 </span>
 <span data-rw-start="135" data-rw-transcript-version="2">
 coding agent to know how to work with
 </span>
 <span data-rw-start="136.68" data-rw-transcript-version="2">
 those ticketing systems. And those
 </span>
 <span data-rw-start="138.04" data-rw-transcript-version="2">
 external systems like linear are durable.
 </span>
</p>
<p>
 <span data-rw-start="140.32" data-rw-transcript-version="2">
 State machine for human to interact with
 </span>
 <span data-rw-start="142.12" data-rw-transcript-version="2">
 agent. And this whole setup is actually
 </span>
 <span data-rw-start="143.72" data-rw-transcript-version="2">
 very flexible. You don't have to use
 </span>
 <span data-rw-start="145.36" data-rw-transcript-version="2">
 linear. You don't have to use Code X.
 </span>
 <span data-rw-start="147.2" data-rw-transcript-version="2">
 You can actually customize to whatever
 </span>
 <span data-rw-start="148.92" data-rw-transcript-version="2">
 you want. But overall implementation
 </span>
 <span data-rw-start="150.32" data-rw-transcript-version="2">
 concept is what's interesting. And the
 </span>
 <span data-rw-start="151.76" data-rw-transcript-version="2">
 most interesting part is this
 </span>
 <span data-rw-start="152.92" data-rw-transcript-version="2">
 workflow.md file. It basically breaks
 </span>
 <span data-rw-start="155.2" data-rw-transcript-version="2">
 down into two parts. The top part is the
 </span>
 <span data-rw-start="156.96" data-rw-transcript-version="2">
 YAML front matter. It configures
 </span>
 <span data-rw-start="158.64" data-rw-transcript-version="2">
 scheduler directly, like which linear
 </span>
 <span data-rw-start="160.32" data-rw-transcript-version="2">
 project it is, what type of ticket it
 </span>
 <span data-rw-start="161.96" data-rw-transcript-version="2">
 should pick up, where should agent
 </span>
</p>
<p>
 <span data-rw-start="163.16" data-rw-transcript-version="2">
 create isolated workspace, and even
 </span>
 <span data-rw-start="165.36" data-rw-transcript-version="2">
 programmatic hooks to run after it sets
 </span>
 <span data-rw-start="167.4" data-rw-transcript-version="2">
 up the workspace. And this is very
 </span>
 <span data-rw-start="168.88" data-rw-transcript-version="2">
 useful, so you no longer need to rely on
 </span>
 <span data-rw-start="170.96" data-rw-transcript-version="2">
 agent to set those things up. As well as
 </span>
 <span data-rw-start="172.64" data-rw-transcript-version="2">
 how many agents can be run in parallel
 </span>
 <span data-rw-start="174.76" data-rw-transcript-version="2">
 and specific agent settings. And after
 </span>
 <span data-rw-start="176.56" data-rw-transcript-version="2">
 that, the bottom half is a markdown
 </span>
 <span data-rw-start="178.24" data-rw-transcript-version="2">
 file. This is the prompt agent every
 </span>
 <span data-rw-start="180.72" data-rw-transcript-version="2">
 single turn detail is rendered in. It's a
 </span>
 <span data-rw-start="183" data-rw-transcript-version="2">
 standard operating procedure for
 </span>
 <span data-rw-start="184.64" data-rw-transcript-version="2">
 Handling tickets in this repo. How should agent plan task? How should agent
 </span>
 <span data-rw-start="186.4" data-rw-transcript-version="2">
 go validate its work? And what would be
 </span>
</p>
<p>
 <span data-rw-start="188.28" data-rw-transcript-version="2">
 considered as done? And when should
 </span>
 <span data-rw-start="190.24" data-rw-transcript-version="2">
 outreach for human review? And what I
 </span>
 <span data-rw-start="191.64" data-rw-transcript-version="2">
 love about this design is that the same
 </span>
 <span data-rw-start="193.68" data-rw-transcript-version="2">
 file just live inside your repo, so it's
 </span>
 <span data-rw-start="195.52" data-rw-transcript-version="2">
 version controlled and can be changed
 </span>
 <span data-rw-start="197.64" data-rw-transcript-version="2">
 through normal pull request. And the
 </span>
 <span data-rw-start="199.32" data-rw-transcript-version="2">
 file itself contains some programmatic
 </span>
 <span data-rw-start="202.64" data-rw-transcript-version="2">
 rule that controls scheduler and also
 </span>
 <span data-rw-start="204.72" data-rw-transcript-version="2">
 what an agent does. There's no separate
 </span>
 <span data-rw-start="206.56" data-rw-transcript-version="2">
 config service, no admin panel, no UI at
 </span>
 <span data-rw-start="208.96" data-rw-transcript-version="2">
 all. And the team only code base on this
 </span>
 <span data-rw-start="210.72" data-rw-transcript-version="2">
 workflow. So, when you onboard a new
 </span>
 <span data-rw-start="212.4" data-rw-transcript-version="2">
 agent capability of adding new step in
 </span>
 <span data-rw-start="214.24" data-rw-transcript-version="2">
 the process, you just very easily change
 </span>
</p>
<p>
 <span data-rw-start="216.32" data-rw-transcript-version="2">
 this markdown file, and the rest will
 </span>
 <span data-rw-start="217.68" data-rw-transcript-version="2">
 just follow. And this whole system is
 </span>
 <span data-rw-start="219.36" data-rw-transcript-version="2">
 designed very flexible. You don't have
 </span>
 <span data-rw-start="221.2" data-rw-transcript-version="2">
 to use Code X, and you don't have to use
 </span>
 <span data-rw-start="223.16" data-rw-transcript-version="2">
 linear. They have one example
 </span>
 <span data-rw-start="224.64" data-rw-transcript-version="2">
 implementation in Elixir, which is a
 </span>
 <span data-rw-start="226.24" data-rw-transcript-version="2">
 programming language. But they have this
 </span>
 <span data-rw-start="228.04" data-rw-transcript-version="2">
 spec.md file that's detailing how this
 </span>
 <span data-rw-start="230.88" data-rw-transcript-version="2">
 Framework or system is designed. So, you
 </span>
 <span data-rw-start="233.2" data-rw-transcript-version="2">
 can just drop this file to any coding
 </span>
 <span data-rw-start="235" data-rw-transcript-version="2">
 agent and ask it to build and design a
 </span>
 <span data-rw-start="237.08" data-rw-transcript-version="2">
 system in any programming language.
 </span>
</p>
<p>
 <span data-rw-start="239.08" data-rw-transcript-version="2">
 There are already a lot of different
 </span>
 <span data-rw-start="240.28" data-rw-transcript-version="2">
 community attempts. Like someone
 </span>
 <span data-rw-start="241.84" data-rw-transcript-version="2">
 building custom TUI based on the task
 </span>
 <span data-rw-start="243.8" data-rw-transcript-version="2">
 data. And also another person already
 </span>
 <span data-rw-start="245.64" data-rw-transcript-version="2">
 rebuilt it to support Cloud Code as
 </span>
 <span data-rw-start="247.44" data-rw-transcript-version="2">
 agent harness. And I'm going to show you
 </span>
 <span data-rw-start="249.08" data-rw-transcript-version="2">
 step by step how you can set these
 </span>
 <span data-rw-start="250.96" data-rw-transcript-version="2">
 things up. But orchestrating agent is
 </span>
 <span data-rw-start="252.44" data-rw-transcript-version="2">
 only part of the work. As Open AI
 </span>
 <span data-rw-start="254.2" data-rw-transcript-version="2">
 mentioned, this whole thing only works
 </span>
 <span data-rw-start="256.239" data-rw-transcript-version="2">
 if your coding agent's environment is
 </span>
 <span data-rw-start="258.239" data-rw-transcript-version="2">
 set up properly in a way that it can
 </span>
 <span data-rw-start="260.16" data-rw-transcript-version="2">
 complete tickets end-to-end atomically,
 </span>
 <span data-rw-start="262.32" data-rw-transcript-version="2">
 which you can call it harness engineer,
 </span>
 <span data-rw-start="263.72" data-rw-transcript-version="2">
 but fundamentally just whether your
 </span>
 <span data-rw-start="265.48" data-rw-transcript-version="2">
 environment or code base has been set up
 </span>
 <span data-rw-start="267.48" data-rw-transcript-version="2">
 in the right way, so agent has
 </span>
 <span data-rw-start="269" data-rw-transcript-version="2">
 everything it needs to complete task
 </span>
 <span data-rw-start="270.88" data-rw-transcript-version="2">
 end-to-end. And typical things like is
 </span>
 <span data-rw-start="272.6" data-rw-transcript-version="2">
 the system bootable, so agent can just
 </span>
 <span data-rw-start="274.16" data-rw-transcript-version="2">
 run a script to get everything set up.
 </span>
</p>
<p>
 <span data-rw-start="276.12" data-rw-transcript-version="2">
 Without spending time to figure that
 </span>
 <span data-rw-start="277.32" data-rw-transcript-version="2">
 part out, and does the system have a
 </span>
 <span data-rw-start="279" data-rw-transcript-version="2">
 proper documentation structure for
 </span>
 <span data-rw-start="280.88" data-rw-transcript-version="2">
 different things? And I think most
 </span>
 <span data-rw-start="282.16" data-rw-transcript-version="2">
 people do have these two things
 </span>
 <span data-rw-start="283.48" data-rw-transcript-version="2">
 properly set up in your code.md or
 </span>
 <span data-rw-start="285.32" data-rw-transcript-version="2">
 agent.md file. But the part I think most
 </span>
 <span data-rw-start="287.72" data-rw-transcript-version="2">
 of the team didn't set up is those
 </span>
 <span data-rw-start="288.88" data-rw-transcript-version="2">
 self-verifying tools. They allow the agent
 </span>
 <span data-rw-start="291.48" data-rw-transcript-version="2">
 to do an end-to-end test after
 </span>
 <span data-rw-start="293" data-rw-transcript-version="2">
 implementing something. And even submit
 </span>
 <span data-rw-start="294.8" data-rw-transcript-version="2">
 a video recording to prove that it has
 </span>
 <span data-rw-start="297.16" data-rw-transcript-version="2">
 been tested and it's working in the ticket
 </span>
 <span data-rw-start="299.4" data-rw-transcript-version="2">
 directly, just like in their demo. But in
 </span>
 <span data-rw-start="301.52" data-rw-transcript-version="2">
 the documentation, they didn't really mention how
 </span>
 <span data-rw-start="302.84" data-rw-transcript-version="2">
 they were handling this part. So, I did
 </span>
 <span data-rw-start="304.64" data-rw-transcript-version="2">
 some research across many major skills.
 </span>
 <span data-rw-start="307" data-rw-transcript-version="2">
 And the best one I found is this
 </span>
 <span data-rw-start="308.2" data-rw-transcript-version="2">
 Playwright CRI tool. So, I believe many
 </span>
 <span data-rw-start="310.44" data-rw-transcript-version="2">
 of us are pretty familiar with
 </span>
 <span data-rw-start="312" data-rw-transcript-version="2">
 Playwright MCP, which allows the agent to use
 </span>
 <span data-rw-start="314.52" data-rw-transcript-version="2">
 the browser and do a task, check the
 </span>
 <span data-rw-start="316.4" data-rw-transcript-version="2">
 logs. But the problem before was that
 </span>
 <span data-rw-start="317.96" data-rw-transcript-version="2">
 Playwright with MCP setup, it took a
 </span>
 <span data-rw-start="320.04" data-rw-transcript-version="2">
 huge amount of tokens in the context window.
 </span>
</p>
<p>
 <span data-rw-start="321.96" data-rw-transcript-version="2">
 Even when it's not needed, but they have
 </span>
 <span data-rw-start="323.72" data-rw-transcript-version="2">
 released this Playwright CRI tool
 </span>
 <span data-rw-start="325.56" data-rw-transcript-version="2">
 alongside agent skill that detailing
 </span>
 <span data-rw-start="327.64" data-rw-transcript-version="2">
 every single comment. And the most
 </span>
 <span data-rw-start="329.36" data-rw-transcript-version="2">
 interesting comment is this video
 </span>
 <span data-rw-start="330.84" data-rw-transcript-version="2">
 recording CRI. So, Playwright allows
 </span>
 <span data-rw-start="332.92" data-rw-transcript-version="2">
 agent to run commands like video start
 </span>
 <span data-rw-start="335.08" data-rw-transcript-version="2">
 and video stop to capture browser
 </span>
 <span data-rw-start="336.84" data-rw-transcript-version="2">
 session into an MP4 or WebM video.
 </span>
</p>
<p>
 <span data-rw-start="339.52" data-rw-transcript-version="2">
 They even have some pretty advanced video
 </span>
 <span data-rw-start="341.4" data-rw-transcript-version="2">
 rendering capability, where they can add
 </span>
 <span data-rw-start="343.56" data-rw-transcript-version="2">
 different chapters on the screen. Like
 </span>
 <span data-rw-start="345.28" data-rw-transcript-version="2">
 here's one example video where it can
 </span>
 <span data-rw-start="347.52" data-rw-transcript-version="2">
 record its own session and even add new
 </span>
 <span data-rw-start="349.92" data-rw-transcript-version="2">
 HTML elements on top of the screen to
 </span>
 <span data-rw-start="352.4" data-rw-transcript-version="2">
 annotate the actions the agent took. And
 </span>
 <span data-rw-start="354.44" data-rw-transcript-version="2">
 then upload the session into Linear, so you
 </span>
 <span data-rw-start="356.48" data-rw-transcript-version="2">
 can very easily verify if things
 </span>
 <span data-rw-start="358.4" data-rw-transcript-version="2">
 actually work. And as far as I know,
 </span>
 <span data-rw-start="360.36" data-rw-transcript-version="2">
 other tools like Chrome DevTools MCP or
 </span>
 <span data-rw-start="362.6" data-rw-transcript-version="2">
 agent browser don't have this video
 </span>
 <span data-rw-start="364.56" data-rw-transcript-version="2">
 capability out of the box. So, this is one
 </span>
 <span data-rw-start="366.28" data-rw-transcript-version="2">
 very important skill that will make your
 </span>
 <span data-rw-start="367.64" data-rw-transcript-version="2">
 whole experience complete. And
 </span>
 <span data-rw-start="368.96" data-rw-transcript-version="2">
 meanwhile, there are also other skills.
 </span>
</p>
<p>
 <span data-rw-start="370.4" data-rw-transcript-version="2">
 That you should add. And I just take one
 </span>
 <span data-rw-start="371.88" data-rw-transcript-version="2">
 of the repo I have as example. We have
 </span>
 <span data-rw-start="373.68" data-rw-transcript-version="2">
 this Playwright CRI tool that has a
 </span>
 <span data-rw-start="375.24" data-rw-transcript-version="2">
 skill as well as a list of references for
 </span>
 <span data-rw-start="377.24" data-rw-transcript-version="2">
 agent to know how to like record a video
 </span>
 <span data-rw-start="379.32" data-rw-transcript-version="2">
 and tracing the debug logs. And we also
 </span>
 <span data-rw-start="381.48" data-rw-transcript-version="2">
 have a skill here to tell the agent how to
 </span>
 <span data-rw-start="383.28" data-rw-transcript-version="2">
 start server locally. And because ours
 </span>
 <span data-rw-start="385.36" data-rw-transcript-version="2">
 is pretty straightforward, so it's just
 </span>
 <span data-rw-start="387.04" data-rw-transcript-version="2">
 a skill file. But sometimes, for more
 </span>
 <span data-rw-start="388.76" data-rw-transcript-version="2">
 complicated things, you can create
 </span>
 <span data-rw-start="390.32" data-rw-transcript-version="2">
 predefined scripts as well. So, the agent no
 </span>
 <span data-rw-start="392.2" data-rw-transcript-version="2">
 longer spends cognitive power on those
 </span>
 <span data-rw-start="393.84" data-rw-transcript-version="2">
 types of stuff. And meanwhile, I also
 </span>
 <span data-rw-start="395.16" data-rw-transcript-version="2">
 created this linear skill that allows
 </span>
 <span data-rw-start="397.2" data-rw-transcript-version="2">
 the agent to know how to operate linear
 </span>
 <span data-rw-start="398.8" data-rw-transcript-version="2">
 tickets by using linear API as well as
 </span>
 <span data-rw-start="401" data-rw-transcript-version="2">
 things like upload video evidence of the
 </span>
 <span data-rw-start="403.32" data-rw-transcript-version="2">
 test. And we actually have more
 </span>
 <span data-rw-start="404.76" data-rw-transcript-version="2">
 documents about different parts of
 </span>
 <span data-rw-start="406.44" data-rw-transcript-version="2">
 system. And in the agent.md or cloud.md
 </span>
 <span data-rw-start="409" data-rw-transcript-version="2">
 file, this is where we have a proper
 </span>
 <span data-rw-start="410.48" data-rw-transcript-version="2">
 index of different documentation
 </span>
 <span data-rw-start="412.08" data-rw-transcript-version="2">
 systems, so you can always go and find
 </span>
 <span data-rw-start="413.84" data-rw-transcript-version="2">
 the relevant information.
 </span>
</p>
<p>
 <span data-rw-start="415.4" data-rw-transcript-version="2">
 More detailed debugging skills. For
 </span>
 <span data-rw-start="417.48" data-rw-transcript-version="2">
 example, we use Grafana to track and
 </span>
 <span data-rw-start="419.12" data-rw-transcript-version="2">
 store all the logging in production. And
 </span>
 <span data-rw-start="420.8" data-rw-transcript-version="2">
 we add a relevant Grafana log skill in
 </span>
 <span data-rw-start="423.16" data-rw-transcript-version="2">
 our repo, so the agent can fetch real
 </span>
 <span data-rw-start="425.2" data-rw-transcript-version="2">
 production logs for bug fixing. And all
 </span>
 <span data-rw-start="427.36" data-rw-transcript-version="2">
 those things are try to serve one
 </span>
 <span data-rw-start="428.92" data-rw-transcript-version="2">
 purpose, which is setting up your code
 </span>
 <span data-rw-start="430.48" data-rw-transcript-version="2">
 base so that your agent can fix bug,
 </span>
 <span data-rw-start="432.28" data-rw-transcript-version="2">
 building new features, verify things are
 </span>
 <span data-rw-start="434.28" data-rw-transcript-version="2">
 working fully atomically end-to-end. I
 </span>
 <span data-rw-start="436.28" data-rw-transcript-version="2">
 put all skills inside AI Build Club, so
 </span>
 <span data-rw-start="438.52" data-rw-transcript-version="2">
 you can copy-paste and ask your agent to
 </span>
 <span data-rw-start="440.36" data-rw-transcript-version="2">
 customize for your own code base. I put
 </span>
 <span data-rw-start="442.32" data-rw-transcript-version="2">
 the link in the description below, so
 </span>
 <span data-rw-start="443.52" data-rw-transcript-version="2">
 you can join and access. And once you
 </span>
 <span data-rw-start="445.52" data-rw-transcript-version="2">
 set this up, even though you don't use
 </span>
 <span data-rw-start="447.4" data-rw-transcript-version="2">
 Symphony, they're still going to be
 </span>
 <span data-rw-start="448.68" data-rw-transcript-version="2">
 really useful. But after that, this is
 </span>
 <span data-rw-start="450.36" data-rw-transcript-version="2">
 where we can start setting up the
 </span>
 <span data-rw-start="451.48" data-rw-transcript-version="2">
 Symphony, connect to linear, as well as
 </span>
 <span data-rw-start="453.8" data-rw-transcript-version="2">
 this workflow.md file. So, once you
 </span>
</p>
<p>
 <span data-rw-start="455.6" data-rw-transcript-version="2">
 clone the Symphony repo, you'll see
 </span>
 <span data-rw-start="457.52" data-rw-transcript-version="2">
 folder like this. You'll have this
 </span>
 <span data-rw-start="458.6" data-rw-transcript-version="2">
 folder of Elixir. So, this is one
 </span>
 <span data-rw-start="460.36" data-rw-transcript-version="2">
 Version implementing Elixir programming
 </span>
 <span data-rw-start="462.56" data-rw-transcript-version="2">
 language from OpenAI. And most of the
 </span>
 <span data-rw-start="464.56" data-rw-transcript-version="2">
 time, you can just use this Elixir
 </span>
 <span data-rw-start="466.28" data-rw-transcript-version="2">
 directly. But if you want to customize
 </span>
 <span data-rw-start="467.88" data-rw-transcript-version="2">
 it to, like, connect not linear, but
 </span>
 <span data-rw-start="469.84" data-rw-transcript-version="2">
 connect to Trello or Jira, you can ask
 </span>
 <span data-rw-start="471.8" data-rw-transcript-version="2">
 the coding agent to customize it, or even
 </span>
 <span data-rw-start="474.2" data-rw-transcript-version="2">
 build a different language by
 </span>
 <span data-rw-start="475.44" data-rw-transcript-version="2">
 pointing to the spec.md file. And here's
 </span>
 <span data-rw-start="477.68" data-rw-transcript-version="2">
 basically what I did in the Python folder. I
 </span>
 <span data-rw-start="479.44" data-rw-transcript-version="2">
 just point to the spec.md file and ask it to
 </span>
 <span data-rw-start="482.08" data-rw-transcript-version="2">
 build a new version in Python. But most
 </span>
 <span data-rw-start="484.16" data-rw-transcript-version="2">
 of the time, you actually don't need to
 </span>
 <span data-rw-start="485.12" data-rw-transcript-version="2">
 do that. You can just reuse what OpenAI
 </span>
 <span data-rw-start="487.2" data-rw-transcript-version="2">
 provided. And firstly, you can confirm
 </span>
 <span data-rw-start="489" data-rw-transcript-version="2">
 whether the script is. So, you can run
 </span>
 <span data-rw-start="490.72" data-rw-transcript-version="2">
 the script by doing this, which points to the
 </span>
 <span data-rw-start="493.16" data-rw-transcript-version="2">
 Symphony program that has been built.
 </span>
</p>
<p>
 <span data-rw-start="494.6" data-rw-transcript-version="2">
 And run help. So, this should show you
 </span>
 <span data-rw-start="496.28" data-rw-transcript-version="2">
 the actual command about how to run
 </span>
 <span data-rw-start="498.28" data-rw-transcript-version="2">
 Symphony. You basically just do Symphony
 </span>
 <span data-rw-start="500.28" data-rw-transcript-version="2">
 and point to a path to workflow.md file.
 </span>
 <span data-rw-start="502.6" data-rw-transcript-version="2">
 And by default, you can't just run the
 </span>
 <span data-rw-start="503.72" data-rw-transcript-version="2">
 Symphony like this. You can run this to
 </span>
 <span data-rw-start="505.6" data-rw-transcript-version="2">
 bind the Symphony command to a specific
 </span>
 <span data-rw-start="508.4" data-rw-transcript-version="2">
 Path. So, just run this. And then you
 </span>
 <span data-rw-start="510.56" data-rw-transcript-version="2">
 can do Symphony, point to a specific
 </span>
 <span data-rw-start="512.4" data-rw-transcript-version="2">
 workflow.md file. And by default, it
 </span>
 <span data-rw-start="514.36" data-rw-transcript-version="2">
 will give you this warning. Then you can
 </span>
 <span data-rw-start="516.039" data-rw-transcript-version="2">
 add this argument to the command, which
 </span>
 <span data-rw-start="518.159" data-rw-transcript-version="2">
 will set our Symphony background process
 </span>
 <span data-rw-start="519.84" data-rw-transcript-version="2">
 like this. It will track all the tasks,
 </span>
 <span data-rw-start="521.88" data-rw-transcript-version="2">
 show you the project, and next refresh
 </span>
 <span data-rw-start="523.479" data-rw-transcript-version="2">
 time. It will track a specific linear
 </span>
 <span data-rw-start="525.12" data-rw-transcript-version="2">
 project you set up every 30 seconds. If
 </span>
 <span data-rw-start="527.52" data-rw-transcript-version="2">
 there are any tickets in to-do, it will pick
 </span>
 <span data-rw-start="529.48" data-rw-transcript-version="2">
 up and show up in this list. And all
 </span>
 <span data-rw-start="531.32" data-rw-transcript-version="2">
 those configurations are actually
 </span>
 <span data-rw-start="532.6" data-rw-transcript-version="2">
 defined in the workflow.md file. So, in
 </span>
 <span data-rw-start="534.8" data-rw-transcript-version="2">
 workflow.md file, at the front matter,
 </span>
 <span data-rw-start="536.6" data-rw-transcript-version="2">
 there is a project slug. And Symphony
 </span>
 <span data-rw-start="538.92" data-rw-transcript-version="2">
 script will basically read that
 </span>
</p>
<p>
 <span data-rw-start="540.4" data-rw-transcript-version="2">
 metadata,
 </span>
 <span data-rw-start="541.56" data-rw-transcript-version="2">
 importing information from a specific
 </span>
 <span data-rw-start="542.92" data-rw-transcript-version="2">
 project. Same thing for all the other
 </span>
 <span data-rw-start="544.64" data-rw-transcript-version="2">
 configurations, like how frequently it
 </span>
 <span data-rw-start="546.68" data-rw-transcript-version="2">
 should pull the ticket data, what are
 </span>
 <span data-rw-start="548.32" data-rw-transcript-version="2">
 things it should do after setting up a
 </span>
 <span data-rw-start="549.88" data-rw-transcript-version="2">
 new workspace, how many agents can be run
 </span>
 <span data-rw-start="551.88" data-rw-transcript-version="2">
 at the same time, and the Code X
 </span>
 <span data-rw-start="553.6" data-rw-transcript-version="2">
 Configuration. But once you set up this,
 </span>
 <span data-rw-start="555.16" data-rw-transcript-version="2">
 it's basically monitoring the specific
 </span>
 <span data-rw-start="556.96" data-rw-transcript-version="2">
 Symphony repo with Elixir
 </span>
 <span data-rw-start="558.76" data-rw-transcript-version="2">
 implementation. What we want to do is
 </span>
 <span data-rw-start="560.56" data-rw-transcript-version="2">
 apply this to your own workspace. It's
 </span>
 <span data-rw-start="562.76" data-rw-transcript-version="2">
 actually pretty straightforward. You can
 </span>
 <span data-rw-start="564.12" data-rw-transcript-version="2">
 just open any coding agent like Code X
 </span>
 <span data-rw-start="566.04" data-rw-transcript-version="2">
 or Cloud Code, point to the spec.md file
 </span>
 <span data-rw-start="568.16" data-rw-transcript-version="2">
 and say, "I want to set up Symphony for
 </span>
 <span data-rw-start="570.12" data-rw-transcript-version="2">
 my repo, and we will reuse the Elixir
 </span>
 <span data-rw-start="572.12" data-rw-transcript-version="2">
 implementation here, and help me build
 </span>
 <span data-rw-start="574.28" data-rw-transcript-version="2">
 the workflow.md file for my repo."
 </span>
 <span data-rw-start="576.4" data-rw-transcript-version="2">
 With just one command, coding agent is smart
 </span>
 <span data-rw-start="578.44" data-rw-transcript-version="2">
 enough to look at your own repo and
 </span>
 <span data-rw-start="581.04" data-rw-transcript-version="2">
 design a workflow.md file inside there.
 </span>
</p>
<p>
 <span data-rw-start="583.52" data-rw-transcript-version="2">
 And this is the one it created for me,
 </span>
 <span data-rw-start="584.84" data-rw-transcript-version="2">
 including the project slug and API key
 </span>
 <span data-rw-start="587.56" data-rw-transcript-version="2">
 and all the other configurations. But
 </span>
 <span data-rw-start="589.08" data-rw-transcript-version="2">
 you do need to set up linear first. If
 </span>
 <span data-rw-start="591.12" data-rw-transcript-version="2">
 you haven't created a linear account yet,
 </span>
 <span data-rw-start="592.64" data-rw-transcript-version="2">
 just go create one and then add a new
 </span>
 <span data-rw-start="594.28" data-rw-transcript-version="2">
 project. And in this project, click on
 </span>
 <span data-rw-start="596.12" data-rw-transcript-version="2">
 the button here, you can just paste into
 </span>
 <span data-rw-start="599.2" data-rw-transcript-version="2">
 your coding agent. This thing in the
 </span>
 <span data-rw-start="600.68" data-rw-transcript-version="2">
 middle here is a project slot, or you
 </span>
 <span data-rw-start="603" data-rw-transcript-version="2">
 can manually paste into the workflow.md
 </span>
 <span data-rw-start="604.92" data-rw-transcript-version="2">
 file as well. And meanwhile, you need to
 </span>
 <span data-rw-start="606.32" data-rw-transcript-version="2">
 get a linear API key, which you can get
 </span>
 <span data-rw-start="608.32" data-rw-transcript-version="2">
 by clicking on settings, security and
 </span>
 <span data-rw-start="610.32" data-rw-transcript-version="2">
 access, and add a new personal API key
 </span>
</p>
<p>
 <span data-rw-start="612.28" data-rw-transcript-version="2">
 here. And once you did that, you should
 </span>
 <span data-rw-start="613.4" data-rw-transcript-version="2">
 run this command, which will save the
 </span>
 <span data-rw-start="614.92" data-rw-transcript-version="2">
 linear API key globally on your
 </span>
 <span data-rw-start="616.56" data-rw-transcript-version="2">
 computer. So, every time when agent try
 </span>
 <span data-rw-start="618.44" data-rw-transcript-version="2">
 to use linear, it can access any
 </span>
 <span data-rw-start="620.2" data-rw-transcript-version="2">
 projects you have access to. And there
 </span>
 <span data-rw-start="621.84" data-rw-transcript-version="2">
 are some configuration you should do,
 </span>
 <span data-rw-start="623.44" data-rw-transcript-version="2">
 which is status. So, Symphony out-of-box
 </span>
 <span data-rw-start="626" data-rw-transcript-version="2">
 are designed for some special status
 </span>
 <span data-rw-start="627.88" data-rw-transcript-version="2">
 control flow, like human review status
 </span>
 <span data-rw-start="630.12" data-rw-transcript-version="2">
 and also merging status. Once you put a
 </span>
 <span data-rw-start="632.28" data-rw-transcript-version="2">
 ticket into do, Symphony will
 </span>
 <span data-rw-start="633.76" data-rw-transcript-version="2">
 automatically pick up and put that in
 </span>
 <span data-rw-start="635.16" data-rw-transcript-version="2">
 progress and trigger an agent session.
 </span>
</p>
<p>
 <span data-rw-start="637.28" data-rw-transcript-version="2">
 And once agent finish the work, it will
 </span>
 <span data-rw-start="638.88" data-rw-transcript-version="2">
 change to human review status, so that
 </span>
 <span data-rw-start="640.92" data-rw-transcript-version="2">
 you can review the work. And once
 </span>
 <span data-rw-start="642.28" data-rw-transcript-version="2">
 finished, you can set the status to be
 </span>
 <span data-rw-start="643.6" data-rw-transcript-version="2">
 merging, which will trigger the agent
 </span>
 <span data-rw-start="645.08" data-rw-transcript-version="2">
 automatically raise a PR from this work.
 </span>
</p>
<p>
 <span data-rw-start="647.24" data-rw-transcript-version="2">
 And once you did all that, you can do
 </span>
 <span data-rw-start="648.72" data-rw-transcript-version="2">
 run Symphony past through your
 </span>
 <span data-rw-start="650.48" data-rw-transcript-version="2">
 workflow.md file, plus this I understand
 </span>
 <span data-rw-start="653.12" data-rw-transcript-version="2">
 that this will be running without the
 </span>
 <span data-rw-start="655.04" data-rw-transcript-version="2">
 usual guardrail comment. And now
 </span>
 <span data-rw-start="657.08" data-rw-transcript-version="2">
 Symphony will be working and picking up
 </span>
 <span data-rw-start="658.96" data-rw-transcript-version="2">
 all the tickets in your project here. To
 </span>
 <span data-rw-start="660.72" data-rw-transcript-version="2">
 make it easier, you can also create a
 </span>
 <span data-rw-start="661.88" data-rw-transcript-version="2">
 new view, set up this board, so that you
 </span>
 <span data-rw-start="663.92" data-rw-transcript-version="2">
 get this kind of Kanban experience. But
 </span>
 <span data-rw-start="665.839" data-rw-transcript-version="2">
 to just test, I can just create ticket
 </span>
 <span data-rw-start="667.6" data-rw-transcript-version="2">
 change the landing page hero copy from
 </span>
 <span data-rw-start="669.76" data-rw-transcript-version="2">
 your company on autopilot to your AI
 </span>
 <span data-rw-start="671.839" data-rw-transcript-version="2">
 growth team, and then set up the status
 </span>
 <span data-rw-start="674" data-rw-transcript-version="2">
 to be 'to do'. And this should trigger our
 </span>
 <span data-rw-start="675.92" data-rw-transcript-version="2">
 agent here. If I go back here, you can
 </span>
 <span data-rw-start="677.64" data-rw-transcript-version="2">
 see this time it picks up this ticket,
 </span>
 <span data-rw-start="680" data-rw-transcript-version="2">
 and then you can see the agent session
 </span>
</p>
<p>
 <span data-rw-start="681.36" data-rw-transcript-version="2">
 show up, and then the last agent message
 </span>
 <span data-rw-start="683.48" data-rw-transcript-version="2">
 here. And depending on your settings, you
 </span>
 <span data-rw-start="685.08" data-rw-transcript-version="2">
 can also go check this workspace. You
 </span>
 <span data-rw-start="687.56" data-rw-transcript-version="2">
 can see inside this workspace, it has
 </span>
 <span data-rw-start="689.08" data-rw-transcript-version="2">
 one workspace per ticket. So, each one
 </span>
 <span data-rw-start="691.96" data-rw-transcript-version="2">
 is running in an isolated environment. And
 </span>
 <span data-rw-start="693.72" data-rw-transcript-version="2">
 this example implementation also has, uh
 </span>
 <span data-rw-start="695.92" data-rw-transcript-version="2">
 Kind of web UI dashboard that you can
 </span>
 <span data-rw-start="697.68" data-rw-transcript-version="2">
 visit, and this will list out similar
 </span>
 <span data-rw-start="699.8" data-rw-transcript-version="2">
 information you will see in terminal
 </span>
 <span data-rw-start="701.88" data-rw-transcript-version="2">
 here. Not particularly useful, but I
 </span>
 <span data-rw-start="703.76" data-rw-transcript-version="2">
 just thought I’d mention this. And you
 </span>
 <span data-rw-start="704.96" data-rw-transcript-version="2">
 can see after a while, this agent
 </span>
 <span data-rw-start="706.56" data-rw-transcript-version="2">
 changes ticket to in progress status,
 </span>
 <span data-rw-start="708.839" data-rw-transcript-version="2">
 which reflect in our linear board as
 </span>
 <span data-rw-start="710.8" data-rw-transcript-version="2">
 well. And if I click on that, agent made
 </span>
 <span data-rw-start="712.68" data-rw-transcript-version="2">
 a plan and logged all the steps it did.
 </span>
</p>
<p>
 <span data-rw-start="715.28" data-rw-transcript-version="2">
 After a few minutes, the agent check off
 </span>
 <span data-rw-start="717.2" data-rw-transcript-version="2">
 every single item on the checklist, and
 </span>
 <span data-rw-start="719.56" data-rw-transcript-version="2">
 uploads a video recording to verify
 </span>
 <span data-rw-start="722" data-rw-transcript-version="2">
 things are working. And as a human, I
 </span>
 <span data-rw-start="723.72" data-rw-transcript-version="2">
 can just very easily see if things are
 </span>
 <span data-rw-start="725.32" data-rw-transcript-version="2">
 working or not. And once I mark
 </span>
 <span data-rw-start="726.56" data-rw-transcript-version="2">
 something as merging, it will also
 </span>
 <span data-rw-start="728.04" data-rw-transcript-version="2">
 create a PR for me. So, this is a whole
 </span>
 <span data-rw-start="729.56" data-rw-transcript-version="2">
 end-to-end process and how you set
 </span>
 <span data-rw-start="731.16" data-rw-transcript-version="2">
 things up. It definitely feels like
 </span>
 <span data-rw-start="732.92" data-rw-transcript-version="2">
 future. If you hit any blockers, I have
 </span>
 <span data-rw-start="734.68" data-rw-transcript-version="2">
 more detailed step-by-step breakdown, as
 </span>
 <span data-rw-start="736.48" data-rw-transcript-version="2">
 well as all skills posted in the AI
 </span>
 <span data-rw-start="738.16" data-rw-transcript-version="2">
 Build Club. Every week, we have workshops
 </span>
 <span data-rw-start="740.08" data-rw-transcript-version="2">
 to go through those latest learnings and
 </span>
 <span data-rw-start="741.88" data-rw-transcript-version="2">
 Answer any questions. So, if you're
 </span>
 <span data-rw-start="743.32" data-rw-transcript-version="2">
 interested, you can click on the link
 </span>
 <span data-rw-start="744.68" data-rw-transcript-version="2">
 below and join our next batch. But this
 </span>
 <span data-rw-start="746.56" data-rw-transcript-version="2">
 is project Symphony, how it works and
 </span>
 <span data-rw-start="748.36" data-rw-transcript-version="2">
 what's the implications. If you found
 </span>
 <span data-rw-start="749.8" data-rw-transcript-version="2">
 this video useful, please give me a
 </span>
 <span data-rw-start="751.04" data-rw-transcript-version="2">
 subscribe and comment below. Thank you,
 </span>
 <span data-rw-start="752.8" data-rw-transcript-version="2">
 and I see you next time.
 </span>
</p>