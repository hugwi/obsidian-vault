---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, ai-agents]
tags:
  - harness
  - skills
  - tools
source: readwise
created: 2026-06-23
rating: 
action: 
theme: multi-agent-orchestration
subtheme:
  - skill-tool-extension
  - coordinator-patterns
---

# Multica: The Open Source Tool That Makes Claude Code 10x Better

![rw-book-cover](https://i.ytimg.com/vi/WdGSXQPwwmo/sddefault.jpg)

## Metadata
- Author: [[Better Stack]]
- Full Title: Multica: The Open Source Tool That Makes Claude Code 10x Better
- Category: #articles
- Summary: Multimodal is a tool that helps you turn coding agents like Claude Code into helpful teammates. You can self-host it on your own server and manage tasks, skills, and alerts for your agents. It offers a flexible, cheaper way to work with AI agents through direct dialogue and task tracking.
- URL: https://www.youtube.com/watch?v=WdGSXQPwwmo&time_continue=11&source_ve_path=NzY3NTg&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.google.com

## Full Document
Okay, Multimodal claims to be the toolthat can turn your agents into realteammates. So, Claude Code, Open Code,Code CLI, Hermes, and more can be set upwith their own system prompts and theirown skills and be assigned tasks withstatus updates. They can alert you ifthey need your help, schedule recurringtasks, and you can talk directly to youragent. But, is this open-source versionof Claude routines and managed [music]agents actually worth your time? Hitsubscribe and let's find out.

Now, the intended way to use Multimodalis to install it on your workingmachine, which ideally has a terminalcoding agent like Claude Code or OpenCode, and then connect that to theMultimodal Cloud UI. But, we're notgoing to do that. We're going to go thecompletely self-hosted route, so we'llinstall Multimodal on a VPS, which I'llexplain why later. In fact, I usuallyskip the whole setup stage, but forself-hosting with Multimodal, there areA few things I had to figure out that weren't in the documentation. So, we'll go through that first before running through some examples on how to use it.

So, I've already set up Multimodal on a fresh Hetzner VPS by running this command, and that will use Docker to install Multimodal.Make sure you have Docker installed on your VPS, and when you run everything, you should have three containers running: the Multimodal backend, which I believe is written in Go, the Multimodal frontend, which is TypeScript and Next.js, and the Postgres database that is used to store session information.

You next need to run Multimodal setup self-host. But, I had a few issues with that.So, if we run Multimodal self-host and if I were to reset my current configuration and my workspace, you'll see it's asking me to authenticate with this URL, which will take you to this screen.And if you add your email address and hit continue,You'll have to put in a recent code.

Now, I had a lot of trouble with thissection. So, I'd recommend you avoid thewhole recent side of things altogetherby going into the {dot}multimodal serverdirectory, opening the env file, makesure the app environment is set todevelopment, and also make sure thevalue for the recent API key is empty.This will make the code this value. Onceyou've done that, stay inside thisdirectory and run this command torestart the containers with the updatedenvironment variables file. And afteryou've done that, you should be able tolog in with six eights. Now, we's notquite done yet. From here, go toruntimes, and you can see that I havetwo different runtimes installed, butyou should have nothing because thathasn't been set up. If you run

Multimodal daemon status, you can seeright now mine is running and usingthese agents with one workspace, butyours should have an error. And that'sBecause first, on your VPS, you'll needto have a terminal coding toolinstalled. So, I have Claude Code andOpen Code installed, and in order toconnect that runtime to your Multimodalinstance, you'd have to go intosettings, then API tokens, then create anew API token, then run Multimodal loginwith the token flag and paste your tokenhere. Then, if you have a Multimodaldaemon running, stop it before startingit again. The daemon in Multimodalchecks for installed harness binaries,polls for tasks from Multimodal to give

to the agents, and spawns multipleagents using work trees in order to getthese tasks done. So, once you've donethat, the daemon should now be showingyour available runtimes, and the beautyof connecting it this way is that youcan add multiple machines to yourMultimodal instance. So, if you havemultiple VPSs, you can installMultimodal on all of them and connectthem to a single UI using your differentAPI tokens. Okay, with the setup out ofthe way, let's go through some simpletasks with Multimodal. And I'm not goingto go through the full potential sohaving multiple agents with multipleprojects and adding multiple tasks. Ijust want to show you individualfeatures so you can picture how powerful

Multimodal is if that's the way you liketo work. So, before you can do anythingwith Multimodal, you'd have to create anagent, and I've already created one herecalled Medibot, but you can do one byclicking on this plus button andfollowing the instructions. So, thismedical bot is similar or has thesimilar system prompt to the one that Imade in the Claude managed agents video,that simply gets my medical informationfrom a private GitHub repo, and I cantalk to it via Slack. Now, because Ihave a bit more freedom with Multimodal,in the sense that I have my own VPS,and I can manage that directly, instead ofgetting this agent to clone that repo.

From GitHub, I've gone ahead and clonedit myself into this directory. Now, aswell as the system prompt, you can giveyour agent custom skills. Note that theagent will have access to skills youhave installed on your CLI, but you canadd skills directly in the UI if youwant to here, which I have done as atest skill, but I'm not going to add itto the agent. There are also environmentsand also custom arguments. Since theagent uses the CLI tool, in this caseit's going to use Open Code run. I canadd custom flags, but if I want thisagent to only use a specific model, andso on. But, by default, the agent willuse the model you have in your CLI. So,if I run Open Code right now, you cansee it's using the big pickle model fromOpen Code Zen. Now, I can create a taskor issue by clicking here, and I'm going

to call this issue medical question witha prompt of "Can you check my medicalinformation and let me know if I can eatcalamari?"Issue tracking tool, this will look very familiar. You can set priorities, assignpeople, add due dates, and so on. But, Iwould highly recommend you always createthe issue before you assign someone because the second you assign a bot tothis issue, it gets started working onit right away. So, make sure you'recomfortable with everything you'vewritten, double-check, and once you'redone, assign it to a bot, so I'll assignit to Medibot, and create the issue. Andfrom there, the bot will get started onit. I can keep track of it inside issuesover here, and if we click on the issue,we can see Medibot is working straightaway.

Now, while this is going, I'm going toclick on autopilot, and this is theopen-source version of Claude routines.We can click on start from scratch, andwe can select an agent, and we can sethow often we want this task to run. Now,unlike Claude routines, there's nooption for API triggers or GitHub event.

Triggers. Maybe that will come in thefuture, but I'm going to give this asimilar prompt to the Claude routinevideo to fetch the latest issues ofthese three newsletters via RSS. Andonce you get these issues, find the best10 articles that can be used in aYouTube video. This will happen daily at9:00 a.m. London time, and ideally,you'd want a research-specific agentthat is good at picking topics forYouTube. But for now, we'll stick withMedibot, and we'll hit create. Then, wecan click into this autopilot and clickrun now, just to see it in action. Itwill create a new issue in To Do, andwe'll leave that to run for a fewminutes and check back on our otherissue, which has now been moved to InReview by the agent. So, over here, itsays, "Based on my medical records, Ihave a shellfish allergy," which istrue, "and should not eat calamari." Itthen gives more information here aboutmy allergy, and we can also click here.

To see exactly what the agent did. So,we can expand the execution history andsee that it made a few bash tool calls,in fact, a lot of bash tool calls tolook for the medical info directory, andthen it searched the whole homedirectory before finding it and checkingmy medical info to give the agent theright information. Awesome. And fromhere, I can leave a reply, "Thanks forthe information. Why have you put thisin review instead of moving it to done?"So, we'll leave that with the agent, andif you don't want to manually keep trackof what the agent is saying, you canalso get notifications from the agent.So, here is the response from medicalagent, and I've also got an update fromour autopilot. Here's one that ranautomatically an hour ago, but here'sone that we just triggered, and it's justfinished. So, we can see here that this

is the prompt I gave it. It's runthrough the prompt, and it's giving me aresponse. So, here are the top 10 picksWith burn, temporal API, and so on. Now,what's interesting here is that an agentwill not move a task once it's in review,back into in progress and to do. You, asa human, could of course do thatautomatically, so I can move this intoin progress or move that into blocked ifI wanted to. But, even though I askedthe medical agent a question, it hasn'tgone back to in progress while it'sanswering the question. It just stays inreview, and so I need to click on it toknow when it's done, and we can see whyit moved it to in review since it's thestandard workflow step instead of movingit to done. So, it's waiting for me, thehuman, to move it to done, which makes sense.

From here, I can continuetalking to the agent, leave a reply,leave comments,ask a one-off question without goingthrough the whole issue trackingprocess, I could click here and talk tomy agent directly. Now, to be honest,I'm not the biggest fan of communicating.

With agents by assigning tasks andwatching them progress through a Kanbanboard, this is why I haven't tried outprojects like Paperclip or Vibe Kanban.I don't really care about priorities ordue dates. I tend to work on one ormaybe two projects at a time withagents, and I like to have more of adialogue with my agents, actually seeingwhat they do, the tools they use, andthe problems they come across so I canhelp debug with them. But, this is notto say I don't like the idea ofMultimodal. In fact, I do like thescheduled tasks feature. I like the factyou can completely self-host it. Andalso, I think it's a very solid toolthat is much cheaper if you use adifferent model than using some of theClaude managed agents or Clauderoutines. But, I will say it's fairlytechnical in its setup process. You kindof have to know what you're doing,especially if you want to keep thingssecure, and that is the benefit of theManaged agents or routines, which take

care of all these things for you byhosting things on Anthropic'sinfrastructure, and the fact that youcan use connectors to communicate withyour agent does make things a bit easierbecause if you wanted to do the samething in Multimodal, okay, you could usethe responsive site on your phone, butyou'd have to manually put thingstogether if you want to use Slack,Telegram, or Discord. And this is why Iwent down the self-hosted route purelybecause of security. If something isconnected to the internet, then it'sdefinitely hackable. I mean, you coulduse Multimodal completely locally, soinstall it on your local machine and runthe UI locally, so it won't be connectedto the internet, but if you do want toconnect it to the internet, I recommendgoing down the self-hosted route usingTailscale so your server isn'tcompletely exposed and making sureyou're always up to date with the latestVersions.
