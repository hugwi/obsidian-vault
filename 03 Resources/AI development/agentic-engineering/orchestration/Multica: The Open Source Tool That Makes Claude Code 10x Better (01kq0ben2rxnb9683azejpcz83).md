---
title: "Multica: The Open Source Tool That Makes Claude Code 10x Better"
source: "https://www.youtube.com/watch?v=WdGSXQPwwmo&time_continue=11&source_ve_path=NzY3NTg&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.google.com"
author: "Better Stack"
published: 2026-04-21
created: 2026-04-24
description: "Multica claims to turn your coding agents, Claude Code, OpenClaw, OpenCode,"
tags:
  - to-process
  - orchestration
---

Okay, Multimodal claims to be the tool that can turn your agents into real teammates. So, Claude Code, Open Code, Code CLI, Hermes, and more can be set up with their own system prompts and their own skills and be assigned tasks with status updates. They can alert you if they need your help, schedule recurring tasks, and you can talk directly to your agent. But, is this open-source version of Claude routines and managed [music] agents actually worth your time? Hit subscribe and let's find out. 

Now, the intended way to use Multimodal is to install it on your working machine, which ideally has a terminal coding agent like Claude Code or Open Code, and then connect that to the Multimodal Cloud UI. But, we're not going to do that. We're going to go the completely self-hosted route, so we'll install Multimodal on a VPS, which I'll explain why later. In fact, I usually skip the whole setup stage, but for self-hosting with Multimodal, there are a few things I had to figure out that weren't 

in the documentation. So, we'll go through that first before running through some examples on how to use it. So, I've already set up Multimodal on a fresh Hetzner VPS by running this command, and that will use Docker to install Multimodal. So, make sure you have Docker installed on your VPS, and when you run everything, you should have three containers running. The Multimodal backend, which I believe is written in Go, the Multimodal frontend, which is TypeScript and Next.js, and the Postgres database that is used to store session information. You next need to run Multimodal setup self-host. But, I had a 

few issues with that. So, if we run Multimodal self-host and if I were to reset my current configuration and my workspace, you'll see it's asking me to authenticate with this URL, which will take you to this screen. And if you add your email address and hit continue, you'll have to put in a recent code. Now, I had a lot of trouble with this section. So, I'd recommend you avoid the whole recent side of things altogether by going into the {dot}multimodal server directory, opening the env file, make sure the app environment is set to development, and also make sure the 

value for the recent API key is empty. This will make the code this value. Once you've done that, stay inside this directory and run this command to restart the containers with the updated environment variables file. And after you've done that, you should be able to log in with six eights. Now, we're not quite done yet. From here, go to runtimes, and you can see that I have two different runtimes installed, but you should have nothing because that hasn't been set up. If you run Multimodal daemon status, you can see right now mine is running and using these agents with one workspace, but 

yours should have an error. And that's because first on your VPS, you'll need to have a terminal coding tool installed. So, I have Claude Code and Open Code installed, and in order to connect that runtime to your Multimodal instance, you'd have to go into settings, then API tokens, then create a new API token, then run Multimodal login with the token flag and paste your token here. Then, if you have a Multimodal daemon running, stop it before starting it again. The daemon in Multimodal checks for installed harness binaries, polls for tasks from Multimodal to give 

to the agents, and spawns multiple agents using work trees in order to get these tasks done. So, once you've done that, the daemon should now be showing your available runtimes, and the beauty of connecting it this way is that you can add multiple machines to your Multimodal instance. So, if you have multiple VPSs, you can install Multimodal on all of them and connect them to a single UI using your different API tokens. Okay, with the setup out of the way, let's go through some simple tasks with Multimodal. And I'm not going to go through the full potential so 

having multiple agents with multiple projects and adding multiple tasks. I just want to show you individual features so you can picture how powerful Multimodal is if that's the way you like to work. So, before you can do anything with Multimodal, you'd have to create an agent, and I've already created one here called Medibot, but you can do one by clicking on this plus button and following the instructions. So, this medical bot is similar or has the similar system prompt to the one that I made in the Claude managed agents video that simply gets my medical information 

from a private GitHub repo, and I can talk to it via Slack. Now, because I have a bit more freedom with Multimodal in the sense that I have my own VPS and I can manage that directly, instead of getting this agent to clone that repo from GitHub, I've gone ahead and cloned it myself into this directory. Now, as well as the system prompt, you can give your agent custom skills. Note that the agent will have access to skills you have installed on your CLI, but you can add skills directly in the UI if you want to here, which I have done as a test skill, but I'm not going to add it to the agent. There's also environments 

and also custom arguments. Since the agent uses the CLI tool, in this case it's going to use Open Code run, I can add custom flags but if I want this agent to only use a specific model and so on. But, by default, the agent will use the model you have in your CLI. So, if I run Open Code right now, you can see it's using the big pickle model from Open Code Zen. Now, I can create a task or issue by clicking here, and I'm going to call this issue medical question with a prompt of "Can you check my medical information and let me know if I can eat calamari?" Now, if you've ever used any 

issue tracking tool, this will look very familiar. You can set priorities, assign people, add due dates, and so on. But, I would highly recommend you always create the issue before you assign someone because the second you assign a bot to this issue, it gets started working on it right away. So, make sure you're comfortable with everything you've written, double-check, and once you're done, assign it to a bot, so I'll assign it to Medibot, and create the issue. And from there, the bot will get started on it. I can keep track of it inside issues over here, and if we click on the issue, 

we can see Medibot is working straight away. Now, while this is going, I'm going to click on autopilot, and this is the open-source version of Claude routines. We can click on start from scratch, and we can select an agent, and we can set how often we want this task to run. Now, unlike Claude routines, there's no option for API triggers or GitHub event triggers. Maybe that will come in the future, but I'm going to give this a similar prompt to the Claude routine video to fetch the latest issues of these three newsletters via RSS. And 

once you get these issues, find the best 10 articles that can be used in a YouTube video. This will happen daily at 9:00 a.m. London time, and ideally, you'd want a research-specific agent that is good at picking topics for YouTube. But for now, we'll stick with Medibot and we'll hit create. Then, we can click into this autopilot and click run now just to see it in action. It will create a new issue in to do, and we'll leave that to run for a few minutes and check back on our other issue, which has now been moved to in review by the agent. So, over here, it 

says, "Based on my medical records, I have a shellfish allergy," which is true, "and should not eat calamari." It then gives more information here about my allergy, and we can also click here to see exactly what the agent did. So, we can expand the execution history and see that it made a few bash tool calls, in fact, a lot of bash tool calls to look for the medical info directory, and then it searched the whole home directory before finding it and checking my medical info to give the agent the right information. Awesome. And from 

here, I can leave a reply, "Thanks for the information. Why have you put this in review instead of moving it to done?" So, we'll leave that with the agent, and if you don't want to manually keep track of what the agent is saying, you can also get notifications from the agent. So, here is the response from medical agent, and I've also got an update from our autopilot. Here's one that ran automatically an hour ago, but here's one that we just triggered and it's just finished. So, we can see here that this is the prompt I gave it. It's run through the prompt and it's giving me a response. So, here are the top 10 picks 

with burn, temporal API, and so on. Now, what's interesting here is that an agent will not move a task once it's in review back into in progress and to do. You as a human could of course do that automatically, so I can move this into in progress or move that into blocked if I wanted to. But, even though I asked the medical agent a question, it hasn't gone back to in progress while it's answering the question. It just stays in review, and so I need to click on it to know when it's done, and we can see why it moved it to in review since it's the standard workflow step instead of moving 

it to done. So, it's waiting for me, the human, to move it to done, which kind of makes sense. From here, I can continue talking to the agent, leave a reply, leave a comments, ask a one-off question without going through the whole issue tracking process, I could click here and talk to my agent directly. Now, to be honest, I'm not the biggest fan of communicating with agents by assigning tasks and watching them progress through a Kanban board. This is why I haven't tried out projects like Paperclip or Vibe Kanban. I don't really care about priorities or 

due dates. I tend to work on one or maybe two projects at a time with agents, and I like to have more of a dialogue with my agents, actually seeing what they do, the tools they use, and the problems they come across so I can help debug with them. But, this is not to say I don't like the idea of Multimodal. In fact, I do like the scheduled tasks feature. I like the fact you can completely self-host it. And also, I think it's a very solid tool that is much cheaper if you use a different model than using some of the Claude managed agents or Claude 

routines. But, I will say it's fairly technical in its setup process. You kind of have to know what you're doing, especially if you want to keep things secure, and that is the benefit of the managed agents or routines, which takes care of all these things for you by hosting things on Anthropic's infrastructure, and the fact that you can use connectors to communicate with your agent does make things a bit easier because if you wanted to do the same thing in Multimodal, okay, you could use the responsive site on your phone, but you'd have to manually put things together if you want to use Slack, 

Telegram, or Discord. And this is why I went down the self-hosted route purely because of security. If something is connected to the internet, then it's definitely hackable. I mean, you could use Multimodal completely locally, so install it on your local machine and run the UI locally, so it won't be connected to the internet, but if you do want to connect it to the internet, I recommend going down the self-hosted route using Tailscale so your server isn't completely exposed and making sure you're always up to date with the latest versions. 

<p>
 <span data-rw-start="0.48" data-rw-transcript-version="2">
 Okay, Multimodal claims to be the tool
 </span>
 <span data-rw-start="2.88" data-rw-transcript-version="2">
 that can turn your agents into real
 </span>
 <span data-rw-start="5.12" data-rw-transcript-version="2">
 teammates. So, Claude Code, Open Code,
 </span>
 <span data-rw-start="7.44" data-rw-transcript-version="2">
 Code CLI, Hermes, and more can be set up
 </span>
 <span data-rw-start="10.32" data-rw-transcript-version="2">
 with their own system prompts and their
 </span>
 <span data-rw-start="12.24" data-rw-transcript-version="2">
 own skills and be assigned tasks with
 </span>
 <span data-rw-start="14.72" data-rw-transcript-version="2">
 status updates. They can alert you if
 </span>
 <span data-rw-start="16.6" data-rw-transcript-version="2">
 they need your help, schedule recurring
 </span>
 <span data-rw-start="18.28" data-rw-transcript-version="2">
 tasks, and you can talk directly to your
 </span>
 <span data-rw-start="20.48" data-rw-transcript-version="2">
 agent. But, is this open-source version
 </span>
 <span data-rw-start="22.64" data-rw-transcript-version="2">
 of Claude routines and managed [music]
 </span>
 <span data-rw-start="24.56" data-rw-transcript-version="2">
 agents actually worth your time? Hit
 </span>
 <span data-rw-start="27.16" data-rw-transcript-version="2">
 subscribe and let's find out.
 </span>
</p>
<p>
 <span data-rw-start="32.56" data-rw-transcript-version="2">
 Now, the intended way to use Multimodal
 </span>
 <span data-rw-start="34.76" data-rw-transcript-version="2">
 is to install it on your working
 </span>
 <span data-rw-start="36.4" data-rw-transcript-version="2">
 machine, which ideally has a terminal
 </span>
 <span data-rw-start="38.64" data-rw-transcript-version="2">
 coding agent like Claude Code or Open
 </span>
 <span data-rw-start="40.64" data-rw-transcript-version="2">
 Code, and then connect that to the
 </span>
 <span data-rw-start="42.72" data-rw-transcript-version="2">
 Multimodal Cloud UI. But, we're not
 </span>
 <span data-rw-start="44.76" data-rw-transcript-version="2">
 going to do that. We're going to go the
 </span>
 <span data-rw-start="46.28" data-rw-transcript-version="2">
 completely self-hosted route, so we'll
 </span>
 <span data-rw-start="48.4" data-rw-transcript-version="2">
 install Multimodal on a VPS, which I'll
 </span>
 <span data-rw-start="51.12" data-rw-transcript-version="2">
 explain why later. In fact, I usually
 </span>
 <span data-rw-start="53.76" data-rw-transcript-version="2">
 skip the whole setup stage, but for
 </span>
 <span data-rw-start="56.24" data-rw-transcript-version="2">
 self-hosting with Multimodal, there are
 </span>
 <span data-rw-start="58.12" data-rw-transcript-version="2">
 A few things I had to figure out that weren't in the documentation. So, we'll go through that first before running through some examples on how to use it.
 </span>
</p>
<p>
 <span data-rw-start="59.84" data-rw-transcript-version="2">
 So, I've already set up Multimodal on a fresh Hetzner VPS by running this command, and that will use Docker to install Multimodal.
 </span>
 <span data-rw-start="61.8" data-rw-transcript-version="2">
 Make sure you have Docker installed on your VPS, and when you run everything, you should have three containers running: the Multimodal backend, which I believe is written in Go, the Multimodal frontend, which is TypeScript and Next.js, and the Postgres database that is used to store session information.
 </span>
</p>
<p>
 <span data-rw-start="65.08" data-rw-transcript-version="2">
 You next need to run Multimodal setup self-host. But, I had a few issues with that.
 </span>
 <span data-rw-start="66.88" data-rw-transcript-version="2">
 So, if we run Multimodal self-host and if I were to reset my current configuration and my workspace, you'll see it's asking me to authenticate with this URL, which will take you to this screen.
 </span>
 <span data-rw-start="69.44" data-rw-transcript-version="2">
 And if you add your email address and hit continue,
 </span>
 <span data-rw-start="103.32" data-rw-transcript-version="2">
 You'll have to put in a recent code.
 </span>
</p>
<p>
 <span data-rw-start="105.68" data-rw-transcript-version="2">
 Now, I had a lot of trouble with this
 </span>
 <span data-rw-start="107.92" data-rw-transcript-version="2">
 section. So, I'd recommend you avoid the
 </span>
 <span data-rw-start="110" data-rw-transcript-version="2">
 whole recent side of things altogether
 </span>
 <span data-rw-start="112.2" data-rw-transcript-version="2">
 by going into the {dot}multimodal server
 </span>
 <span data-rw-start="114.08" data-rw-transcript-version="2">
 directory, opening the env file, make
 </span>
 <span data-rw-start="116.64" data-rw-transcript-version="2">
 sure the app environment is set to
 </span>
 <span data-rw-start="118.84" data-rw-transcript-version="2">
 development, and also make sure the
 </span>
 <span data-rw-start="120.4" data-rw-transcript-version="2">
 value for the recent API key is empty.
 </span>
 <span data-rw-start="122.76" data-rw-transcript-version="2">
 This will make the code this value. Once
 </span>
 <span data-rw-start="124.72" data-rw-transcript-version="2">
 you've done that, stay inside this
 </span>
 <span data-rw-start="126.12" data-rw-transcript-version="2">
 directory and run this command to
 </span>
 <span data-rw-start="128.039" data-rw-transcript-version="2">
 restart the containers with the updated
 </span>
 <span data-rw-start="130.28" data-rw-transcript-version="2">
 environment variables file. And after
 </span>
 <span data-rw-start="132.32" data-rw-transcript-version="2">
 you've done that, you should be able to
 </span>
 <span data-rw-start="133.8" data-rw-transcript-version="2">
 log in with six eights. Now, we's not
 </span>
 <span data-rw-start="136.32" data-rw-transcript-version="2">
 quite done yet. From here, go to
 </span>
 <span data-rw-start="137.92" data-rw-transcript-version="2">
 runtimes, and you can see that I have
 </span>
 <span data-rw-start="139.68" data-rw-transcript-version="2">
 two different runtimes installed, but
 </span>
 <span data-rw-start="141.68" data-rw-transcript-version="2">
 you should have nothing because that
 </span>
 <span data-rw-start="143.36" data-rw-transcript-version="2">
 hasn't been set up. If you run
 </span>
</p>
<p>
 <span data-rw-start="144.8" data-rw-transcript-version="2">
 Multimodal daemon status, you can see
 </span>
 <span data-rw-start="146.52" data-rw-transcript-version="2">
 right now mine is running and using
 </span>
 <span data-rw-start="148.28" data-rw-transcript-version="2">
 these agents with one workspace, but
 </span>
 <span data-rw-start="150.68" data-rw-transcript-version="2">
 yours should have an error. And that's
 </span>
 <span data-rw-start="152.12" data-rw-transcript-version="2">
 Because first, on your VPS, you'll need
 </span>
 <span data-rw-start="153.84" data-rw-transcript-version="2">
 to have a terminal coding tool
 </span>
 <span data-rw-start="155.48" data-rw-transcript-version="2">
 installed. So, I have Claude Code and
 </span>
 <span data-rw-start="157.8" data-rw-transcript-version="2">
 Open Code installed, and in order to
 </span>
 <span data-rw-start="159.92" data-rw-transcript-version="2">
 connect that runtime to your Multimodal
 </span>
 <span data-rw-start="161.96" data-rw-transcript-version="2">
 instance, you'd have to go into
 </span>
 <span data-rw-start="163.8" data-rw-transcript-version="2">
 settings, then API tokens, then create a
 </span>
 <span data-rw-start="166.88" data-rw-transcript-version="2">
 new API token, then run Multimodal login
 </span>
 <span data-rw-start="169.48" data-rw-transcript-version="2">
 with the token flag and paste your token
 </span>
 <span data-rw-start="171.96" data-rw-transcript-version="2">
 here. Then, if you have a Multimodal
 </span>
 <span data-rw-start="173.64" data-rw-transcript-version="2">
 daemon running, stop it before starting
 </span>
 <span data-rw-start="175.6" data-rw-transcript-version="2">
 it again. The daemon in Multimodal
 </span>
 <span data-rw-start="177.52" data-rw-transcript-version="2">
 checks for installed harness binaries,
 </span>
 <span data-rw-start="179.96" data-rw-transcript-version="2">
 polls for tasks from Multimodal to give
 </span>
</p>
<p>
 <span data-rw-start="182.24" data-rw-transcript-version="2">
 to the agents, and spawns multiple
 </span>
 <span data-rw-start="184.44" data-rw-transcript-version="2">
 agents using work trees in order to get
 </span>
 <span data-rw-start="186.68" data-rw-transcript-version="2">
 these tasks done. So, once you've done
 </span>
 <span data-rw-start="188.68" data-rw-transcript-version="2">
 that, the daemon should now be showing
 </span>
 <span data-rw-start="190.24" data-rw-transcript-version="2">
 your available runtimes, and the beauty
 </span>
 <span data-rw-start="192.52" data-rw-transcript-version="2">
 of connecting it this way is that you
 </span>
 <span data-rw-start="194" data-rw-transcript-version="2">
 can add multiple machines to your
 </span>
 <span data-rw-start="195.96" data-rw-transcript-version="2">
 Multimodal instance. So, if you have
 </span>
 <span data-rw-start="197.52" data-rw-transcript-version="2">
 multiple VPSs, you can install
 </span>
 <span data-rw-start="198.96" data-rw-transcript-version="2">
 Multimodal on all of them and connect
 </span>
 <span data-rw-start="200.6" data-rw-transcript-version="2">
 them to a single UI using your different
 </span>
 <span data-rw-start="203.12" data-rw-transcript-version="2">
 API tokens. Okay, with the setup out of
 </span>
 <span data-rw-start="205.4" data-rw-transcript-version="2">
 the way, let's go through some simple
 </span>
 <span data-rw-start="206.84" data-rw-transcript-version="2">
 tasks with Multimodal. And I'm not going
 </span>
 <span data-rw-start="208.8" data-rw-transcript-version="2">
 to go through the full potential so
 </span>
 <span data-rw-start="210.44" data-rw-transcript-version="2">
 having multiple agents with multiple
 </span>
 <span data-rw-start="211.88" data-rw-transcript-version="2">
 projects and adding multiple tasks. I
 </span>
 <span data-rw-start="214.48" data-rw-transcript-version="2">
 just want to show you individual
 </span>
 <span data-rw-start="215.88" data-rw-transcript-version="2">
 features so you can picture how powerful
 </span>
</p>
<p>
 <span data-rw-start="218.16" data-rw-transcript-version="2">
 Multimodal is if that's the way you like
 </span>
 <span data-rw-start="220.04" data-rw-transcript-version="2">
 to work. So, before you can do anything
 </span>
 <span data-rw-start="221.88" data-rw-transcript-version="2">
 with Multimodal, you'd have to create an
 </span>
 <span data-rw-start="223.6" data-rw-transcript-version="2">
 agent, and I've already created one here
 </span>
 <span data-rw-start="225.56" data-rw-transcript-version="2">
 called Medibot, but you can do one by
 </span>
 <span data-rw-start="227.4" data-rw-transcript-version="2">
 clicking on this plus button and
 </span>
 <span data-rw-start="228.8" data-rw-transcript-version="2">
 following the instructions. So, this
 </span>
 <span data-rw-start="230.84" data-rw-transcript-version="2">
 medical bot is similar or has the
 </span>
 <span data-rw-start="232.92" data-rw-transcript-version="2">
 similar system prompt to the one that I
 </span>
 <span data-rw-start="235.4" data-rw-transcript-version="2">
 made in the Claude managed agents video,
 </span>
 <span data-rw-start="238.04" data-rw-transcript-version="2">
 that simply gets my medical information
 </span>
 <span data-rw-start="240.12" data-rw-transcript-version="2">
 from a private GitHub repo, and I can
 </span>
 <span data-rw-start="242.64" data-rw-transcript-version="2">
 talk to it via Slack. Now, because I
 </span>
 <span data-rw-start="244.76" data-rw-transcript-version="2">
 have a bit more freedom with Multimodal,
 </span>
 <span data-rw-start="247.12" data-rw-transcript-version="2">
 in the sense that I have my own VPS,
 </span>
 <span data-rw-start="248.68" data-rw-transcript-version="2">
 and I can manage that directly, instead of
 </span>
 <span data-rw-start="250.56" data-rw-transcript-version="2">
 getting this agent to clone that repo.
 </span>
</p>
<p>
 <span data-rw-start="252.2" data-rw-transcript-version="2">
 From GitHub, I've gone ahead and cloned
 </span>
 <span data-rw-start="254.4" data-rw-transcript-version="2">
 it myself into this directory. Now, as
 </span>
 <span data-rw-start="256.56" data-rw-transcript-version="2">
 well as the system prompt, you can give
 </span>
 <span data-rw-start="258.239" data-rw-transcript-version="2">
 your agent custom skills. Note that the
 </span>
 <span data-rw-start="260.28" data-rw-transcript-version="2">
 agent will have access to skills you
 </span>
 <span data-rw-start="261.64" data-rw-transcript-version="2">
 have installed on your CLI, but you can
 </span>
 <span data-rw-start="264.12" data-rw-transcript-version="2">
 add skills directly in the UI if you
 </span>
 <span data-rw-start="265.88" data-rw-transcript-version="2">
 want to here, which I have done as a
 </span>
 <span data-rw-start="268.08" data-rw-transcript-version="2">
 test skill, but I'm not going to add it
 </span>
 <span data-rw-start="269.88" data-rw-transcript-version="2">
 to the agent. There are also environments
 </span>
 <span data-rw-start="271.88" data-rw-transcript-version="2">
 and also custom arguments. Since the
 </span>
 <span data-rw-start="273.88" data-rw-transcript-version="2">
 agent uses the CLI tool, in this case
 </span>
 <span data-rw-start="276.16" data-rw-transcript-version="2">
 it's going to use Open Code run. I can
 </span>
 <span data-rw-start="277.76" data-rw-transcript-version="2">
 add custom flags, but if I want this
 </span>
 <span data-rw-start="279.56" data-rw-transcript-version="2">
 agent to only use a specific model, and
 </span>
 <span data-rw-start="281.76" data-rw-transcript-version="2">
 so on. But, by default, the agent will
 </span>
 <span data-rw-start="283.92" data-rw-transcript-version="2">
 use the model you have in your CLI. So,
 </span>
 <span data-rw-start="286.16" data-rw-transcript-version="2">
 if I run Open Code right now, you can
 </span>
 <span data-rw-start="288.04" data-rw-transcript-version="2">
 see it's using the big pickle model from
 </span>
 <span data-rw-start="290" data-rw-transcript-version="2">
 Open Code Zen. Now, I can create a task
 </span>
 <span data-rw-start="292" data-rw-transcript-version="2">
 or issue by clicking here, and I'm going
 </span>
</p>
<p>
 <span data-rw-start="293.76" data-rw-transcript-version="2">
 to call this issue medical question with
 </span>
 <span data-rw-start="295.56" data-rw-transcript-version="2">
 a prompt of "Can you check my medical
 </span>
 <span data-rw-start="297.32" data-rw-transcript-version="2">
 information and let me know if I can eat
 </span>
 <span data-rw-start="299.4" data-rw-transcript-version="2">
 calamari?"
 </span>
 <span data-rw-start="301.72" data-rw-transcript-version="2">
 Issue tracking tool, this will look very familiar. You can set priorities, assign
 </span>
 <span data-rw-start="303.56" data-rw-transcript-version="2">
 people, add due dates, and so on. But, I
 </span>
 <span data-rw-start="305.88" data-rw-transcript-version="2">
 would highly recommend you always create
 </span>
 <span data-rw-start="310.56" data-rw-transcript-version="2">
 the issue before you assign someone because the second you assign a bot to
 </span>
 <span data-rw-start="313.08" data-rw-transcript-version="2">
 this issue, it gets started working on
 </span>
 <span data-rw-start="316.72" data-rw-transcript-version="2">
 it right away. So, make sure you're
 </span>
 <span data-rw-start="318.2" data-rw-transcript-version="2">
 comfortable with everything you've
 </span>
 <span data-rw-start="319.72" data-rw-transcript-version="2">
 written, double-check, and once you're
 </span>
 <span data-rw-start="321.48" data-rw-transcript-version="2">
 done, assign it to a bot, so I'll assign
 </span>
 <span data-rw-start="323.56" data-rw-transcript-version="2">
 it to Medibot, and create the issue. And
 </span>
 <span data-rw-start="325.96" data-rw-transcript-version="2">
 from there, the bot will get started on
 </span>
 <span data-rw-start="327.84" data-rw-transcript-version="2">
 it. I can keep track of it inside issues
 </span>
 <span data-rw-start="329.68" data-rw-transcript-version="2">
 over here, and if we click on the issue,
 </span>
 <span data-rw-start="331.68" data-rw-transcript-version="2">
 we can see Medibot is working straight
 </span>
 <span data-rw-start="333.28" data-rw-transcript-version="2">
 away.
 </span>
</p>
<p>
 <span data-rw-start="334.16" data-rw-transcript-version="2">
 Now, while this is going, I'm going to
 </span>
 <span data-rw-start="335.36" data-rw-transcript-version="2">
 click on autopilot, and this is the
 </span>
 <span data-rw-start="337.4" data-rw-transcript-version="2">
 open-source version of Claude routines.
 </span>
 <span data-rw-start="339.68" data-rw-transcript-version="2">
 We can click on start from scratch, and
 </span>
 <span data-rw-start="341.84" data-rw-transcript-version="2">
 we can select an agent, and we can set
 </span>
 <span data-rw-start="343.56" data-rw-transcript-version="2">
 how often we want this task to run. Now,
 </span>
 <span data-rw-start="345.88" data-rw-transcript-version="2">
 unlike Claude routines, there's no
 </span>
 <span data-rw-start="348" data-rw-transcript-version="2">
 option for API triggers or GitHub event.
 </span>
</p>
<p>
 <span data-rw-start="350.84" data-rw-transcript-version="2">
 Triggers. Maybe that will come in the
 </span>
 <span data-rw-start="352.28" data-rw-transcript-version="2">
 future, but I'm going to give this a
 </span>
 <span data-rw-start="353.8" data-rw-transcript-version="2">
 similar prompt to the Claude routine
 </span>
 <span data-rw-start="355.52" data-rw-transcript-version="2">
 video to fetch the latest issues of
 </span>
 <span data-rw-start="357.84" data-rw-transcript-version="2">
 these three newsletters via RSS. And
 </span>
 <span data-rw-start="360.24" data-rw-transcript-version="2">
 once you get these issues, find the best
 </span>
 <span data-rw-start="362.84" data-rw-transcript-version="2">
 10 articles that can be used in a
 </span>
 <span data-rw-start="365" data-rw-transcript-version="2">
 YouTube video. This will happen daily at
 </span>
 <span data-rw-start="367.2" data-rw-transcript-version="2">
 9:00 a.m. London time, and ideally,
 </span>
 <span data-rw-start="369.48" data-rw-transcript-version="2">
 you'd want a research-specific agent
 </span>
 <span data-rw-start="371.96" data-rw-transcript-version="2">
 that is good at picking topics for
 </span>
 <span data-rw-start="373.72" data-rw-transcript-version="2">
 YouTube. But for now, we'll stick with
 </span>
 <span data-rw-start="375.52" data-rw-transcript-version="2">
 Medibot, and we'll hit create. Then, we
 </span>
 <span data-rw-start="377.76" data-rw-transcript-version="2">
 can click into this autopilot and click
 </span>
 <span data-rw-start="379.52" data-rw-transcript-version="2">
 run now, just to see it in action. It
 </span>
 <span data-rw-start="381.52" data-rw-transcript-version="2">
 will create a new issue in To Do, and
 </span>
 <span data-rw-start="383.88" data-rw-transcript-version="2">
 we'll leave that to run for a few
 </span>
 <span data-rw-start="385.16" data-rw-transcript-version="2">
 minutes and check back on our other
 </span>
 <span data-rw-start="387.04" data-rw-transcript-version="2">
 issue, which has now been moved to In
 </span>
 <span data-rw-start="389.32" data-rw-transcript-version="2">
 Review by the agent. So, over here, it
 </span>
 <span data-rw-start="391.36" data-rw-transcript-version="2">
 says, "Based on my medical records, I
 </span>
 <span data-rw-start="393.16" data-rw-transcript-version="2">
 have a shellfish allergy," which is
 </span>
 <span data-rw-start="395.08" data-rw-transcript-version="2">
 true, "and should not eat calamari." It
 </span>
 <span data-rw-start="397.68" data-rw-transcript-version="2">
 then gives more information here about
 </span>
 <span data-rw-start="399.12" data-rw-transcript-version="2">
 my allergy, and we can also click here.
 </span>
</p>
<p>
 <span data-rw-start="401.36" data-rw-transcript-version="2">
 To see exactly what the agent did. So,
 </span>
 <span data-rw-start="403.6" data-rw-transcript-version="2">
 we can expand the execution history and
 </span>
 <span data-rw-start="406.28" data-rw-transcript-version="2">
 see that it made a few bash tool calls,
 </span>
 <span data-rw-start="408.4" data-rw-transcript-version="2">
 in fact, a lot of bash tool calls to
 </span>
 <span data-rw-start="411.04" data-rw-transcript-version="2">
 look for the medical info directory, and
 </span>
 <span data-rw-start="413.24" data-rw-transcript-version="2">
 then it searched the whole home
 </span>
 <span data-rw-start="415.04" data-rw-transcript-version="2">
 directory before finding it and checking
 </span>
 <span data-rw-start="417.12" data-rw-transcript-version="2">
 my medical info to give the agent the
 </span>
 <span data-rw-start="419.4" data-rw-transcript-version="2">
 right information. Awesome. And from
 </span>
 <span data-rw-start="421.48" data-rw-transcript-version="2">
 here, I can leave a reply, "Thanks for
 </span>
 <span data-rw-start="423.32" data-rw-transcript-version="2">
 the information. Why have you put this
 </span>
 <span data-rw-start="425.04" data-rw-transcript-version="2">
 in review instead of moving it to done?"
 </span>
 <span data-rw-start="427.36" data-rw-transcript-version="2">
 So, we'll leave that with the agent, and
 </span>
 <span data-rw-start="429.16" data-rw-transcript-version="2">
 if you don't want to manually keep track
 </span>
 <span data-rw-start="430.72" data-rw-transcript-version="2">
 of what the agent is saying, you can
 </span>
 <span data-rw-start="432.2" data-rw-transcript-version="2">
 also get notifications from the agent.
 </span>
 <span data-rw-start="433.96" data-rw-transcript-version="2">
 So, here is the response from medical
 </span>
 <span data-rw-start="436.2" data-rw-transcript-version="2">
 agent, and I've also got an update from
 </span>
 <span data-rw-start="437.8" data-rw-transcript-version="2">
 our autopilot. Here's one that ran
 </span>
 <span data-rw-start="439.84" data-rw-transcript-version="2">
 automatically an hour ago, but here's
 </span>
 <span data-rw-start="441.44" data-rw-transcript-version="2">
 one that we just triggered, and it's just
 </span>
 <span data-rw-start="443.24" data-rw-transcript-version="2">
 finished. So, we can see here that this
 </span>
</p>
<p>
 <span data-rw-start="445" data-rw-transcript-version="2">
 is the prompt I gave it. It's run
 </span>
 <span data-rw-start="446.68" data-rw-transcript-version="2">
 through the prompt, and it's giving me a
 </span>
 <span data-rw-start="448.28" data-rw-transcript-version="2">
 response. So, here are the top 10 picks
 </span>
 <span data-rw-start="450.44" data-rw-transcript-version="2">
 With burn, temporal API, and so on. Now,
 </span>
 <span data-rw-start="453.28" data-rw-transcript-version="2">
 what's interesting here is that an agent
 </span>
 <span data-rw-start="454.96" data-rw-transcript-version="2">
 will not move a task once it's in review,
 </span>
 <span data-rw-start="457.6" data-rw-transcript-version="2">
 back into in progress and to do. You, as
 </span>
 <span data-rw-start="460.04" data-rw-transcript-version="2">
 a human, could of course do that
 </span>
 <span data-rw-start="461.04" data-rw-transcript-version="2">
 automatically, so I can move this into
 </span>
 <span data-rw-start="462.36" data-rw-transcript-version="2">
 in progress or move that into blocked if
 </span>
 <span data-rw-start="464.48" data-rw-transcript-version="2">
 I wanted to. But, even though I asked
 </span>
 <span data-rw-start="466.32" data-rw-transcript-version="2">
 the medical agent a question, it hasn't
 </span>
 <span data-rw-start="468.08" data-rw-transcript-version="2">
 gone back to in progress while it's
 </span>
 <span data-rw-start="469.84" data-rw-transcript-version="2">
 answering the question. It just stays in
 </span>
 <span data-rw-start="471.84" data-rw-transcript-version="2">
 review, and so I need to click on it to
 </span>
 <span data-rw-start="473.44" data-rw-transcript-version="2">
 know when it's done, and we can see why
 </span>
 <span data-rw-start="475.52" data-rw-transcript-version="2">
 it moved it to in review since it's the
 </span>
 <span data-rw-start="477.68" data-rw-transcript-version="2">
 standard workflow step instead of moving
 </span>
 <span data-rw-start="480.12" data-rw-transcript-version="2">
 it to done. So, it's waiting for me, the
 </span>
 <span data-rw-start="482.4" data-rw-transcript-version="2">
 human, to move it to done, which makes sense.
 </span>
</p>
<p>
 <span data-rw-start="484.44" data-rw-transcript-version="2">
 From here, I can continue
 </span>
 <span data-rw-start="486.04" data-rw-transcript-version="2">
 talking to the agent, leave a reply,
 </span>
 <span data-rw-start="488" data-rw-transcript-version="2">
 leave comments,
 </span>
 <span data-rw-start="491.52" data-rw-transcript-version="2">
 ask a one-off question without going
 </span>
 <span data-rw-start="493.6" data-rw-transcript-version="2">
 through the whole issue tracking
 </span>
 <span data-rw-start="495.12" data-rw-transcript-version="2">
 process, I could click here and talk to
 </span>
 <span data-rw-start="497.44" data-rw-transcript-version="2">
 my agent directly. Now, to be honest,
 </span>
 <span data-rw-start="499.32" data-rw-transcript-version="2">
 I'm not the biggest fan of communicating.
 </span>
</p>
<p>
 <span data-rw-start="501.36" data-rw-transcript-version="2">
 With agents by assigning tasks and
 </span>
 <span data-rw-start="503.4" data-rw-transcript-version="2">
 watching them progress through a Kanban
 </span>
 <span data-rw-start="505.04" data-rw-transcript-version="2">
 board, this is why I haven't tried out
 </span>
 <span data-rw-start="506.6" data-rw-transcript-version="2">
 projects like Paperclip or Vibe Kanban.
 </span>
 <span data-rw-start="509.08" data-rw-transcript-version="2">
 I don't really care about priorities or
 </span>
 <span data-rw-start="511.04" data-rw-transcript-version="2">
 due dates. I tend to work on one or
 </span>
 <span data-rw-start="513.159" data-rw-transcript-version="2">
 maybe two projects at a time with
 </span>
 <span data-rw-start="515.12" data-rw-transcript-version="2">
 agents, and I like to have more of a
 </span>
 <span data-rw-start="517.039" data-rw-transcript-version="2">
 dialogue with my agents, actually seeing
 </span>
 <span data-rw-start="519.44" data-rw-transcript-version="2">
 what they do, the tools they use, and
 </span>
 <span data-rw-start="521.4" data-rw-transcript-version="2">
 the problems they come across so I can
 </span>
 <span data-rw-start="523.159" data-rw-transcript-version="2">
 help debug with them. But, this is not
 </span>
 <span data-rw-start="525.72" data-rw-transcript-version="2">
 to say I don't like the idea of
 </span>
 <span data-rw-start="527.72" data-rw-transcript-version="2">
 Multimodal. In fact, I do like the
 </span>
 <span data-rw-start="529.56" data-rw-transcript-version="2">
 scheduled tasks feature. I like the fact
 </span>
 <span data-rw-start="531.8" data-rw-transcript-version="2">
 you can completely self-host it. And
 </span>
 <span data-rw-start="533.52" data-rw-transcript-version="2">
 also, I think it's a very solid tool
 </span>
 <span data-rw-start="535.64" data-rw-transcript-version="2">
 that is much cheaper if you use a
 </span>
 <span data-rw-start="537.4" data-rw-transcript-version="2">
 different model than using some of the
 </span>
 <span data-rw-start="539.04" data-rw-transcript-version="2">
 Claude managed agents or Claude
 </span>
 <span data-rw-start="541.04" data-rw-transcript-version="2">
 routines. But, I will say it's fairly
 </span>
 <span data-rw-start="543.72" data-rw-transcript-version="2">
 technical in its setup process. You kind
 </span>
 <span data-rw-start="546.12" data-rw-transcript-version="2">
 of have to know what you're doing,
 </span>
 <span data-rw-start="547.2" data-rw-transcript-version="2">
 especially if you want to keep things
 </span>
 <span data-rw-start="548.84" data-rw-transcript-version="2">
 secure, and that is the benefit of the
 </span>
 <span data-rw-start="551.2" data-rw-transcript-version="2">
 Managed agents or routines, which take
 </span>
</p>
<p>
 <span data-rw-start="553.44" data-rw-transcript-version="2">
 care of all these things for you by
 </span>
 <span data-rw-start="555.56" data-rw-transcript-version="2">
 hosting things on Anthropic's
 </span>
 <span data-rw-start="556.68" data-rw-transcript-version="2">
 infrastructure, and the fact that you
 </span>
 <span data-rw-start="558.32" data-rw-transcript-version="2">
 can use connectors to communicate with
 </span>
 <span data-rw-start="560.08" data-rw-transcript-version="2">
 your agent does make things a bit easier
 </span>
 <span data-rw-start="562.52" data-rw-transcript-version="2">
 because if you wanted to do the same
 </span>
 <span data-rw-start="563.76" data-rw-transcript-version="2">
 thing in Multimodal, okay, you could use
 </span>
 <span data-rw-start="565.88" data-rw-transcript-version="2">
 the responsive site on your phone, but
 </span>
 <span data-rw-start="568.36" data-rw-transcript-version="2">
 you'd have to manually put things
 </span>
 <span data-rw-start="569.96" data-rw-transcript-version="2">
 together if you want to use Slack,
 </span>
 <span data-rw-start="571.6" data-rw-transcript-version="2">
 Telegram, or Discord. And this is why I
 </span>
 <span data-rw-start="573.52" data-rw-transcript-version="2">
 went down the self-hosted route purely
 </span>
 <span data-rw-start="575.48" data-rw-transcript-version="2">
 because of security. If something is
 </span>
 <span data-rw-start="577.28" data-rw-transcript-version="2">
 connected to the internet, then it's
 </span>
 <span data-rw-start="578.84" data-rw-transcript-version="2">
 definitely hackable. I mean, you could
 </span>
 <span data-rw-start="580.6" data-rw-transcript-version="2">
 use Multimodal completely locally, so
 </span>
 <span data-rw-start="582.6" data-rw-transcript-version="2">
 install it on your local machine and run
 </span>
 <span data-rw-start="584.68" data-rw-transcript-version="2">
 the UI locally, so it won't be connected
 </span>
 <span data-rw-start="586.72" data-rw-transcript-version="2">
 to the internet, but if you do want to
 </span>
 <span data-rw-start="588.52" data-rw-transcript-version="2">
 connect it to the internet, I recommend
 </span>
 <span data-rw-start="589.96" data-rw-transcript-version="2">
 going down the self-hosted route using
 </span>
 <span data-rw-start="591.92" data-rw-transcript-version="2">
 Tailscale so your server isn't
 </span>
 <span data-rw-start="593.32" data-rw-transcript-version="2">
 completely exposed and making sure
 </span>
 <span data-rw-start="594.84" data-rw-transcript-version="2">
 you're always up to date with the latest
 </span>
 <span data-rw-start="596.4" data-rw-transcript-version="2">
 Versions.
 </span>
</p>