---
title: "AI Sorcery: Demo of a Claude Code Plugin"
source: "https://www.youtube.com/watch?v=TBQKR9ZO9zc"
author: "Nicholas Westby"
published: 2026-05-06
created: 2026-05-06
description: "A demo of each skill within ai-sorcery, which is a Claude Code plugin (https://github.com/ai-sorcery/ai-sorcery)"
tags:
  - to-process
  - agent-plugins-mcp
---

This is a demo of AI sorcery. So what this is is a repository which has a few claude plugins. Uh one plugin in particular called AI sorcery which has a series of skills. And each of these skills has helped me build some tools with Claude and AI in general. And I thought I would share that with all of you. And so the way this video will work is I actually built a skill that will run through all of the other skills. And 

so this is a a meta skill of sorts. And as I go through each skill and it demonstrates them, I'll give you a little bit of extra insights into what's happening. Before any of these skills can actually be demonstrated, we need something to apply them to. And that's what's happening right now. It's initializing a workspace. And the idea behind this workspace is that we're going to be creating a tool that allows you to track code snippets. So kind of a contrived 

example, but it should serve our purposes for this demo. All right, looks like it has loaded the using.claude skill. This one is intended to bypass an issue which may not be fixed which is a um sort of permission quirk of claude that despite using the bypass permission modes it will um prompt you when it tries to write to thecloud path. Um I think in the last week it's maybe fixed that but this skill can be used when you want to 

bypass permissions for doclaude uh in certain permission modes. Launching Claude is simple but pretty useful. So, it just creates a claw.sh shell script that has some of my presets that launch Claude exactly how I like it to be launched. Looks like this is running the best practices skill, which is just kind of a hodgepodge of useful things for new projects. So, a few of them it looks like it noticed, which was it didn't 

read me and there weren't any starter scripts. So just some shorthand scripts that I like to see in repositories that I work in. And now it's loading the LLM tasks. So this is something super helpful as a workflow approach that I do. Instead of asking Claude to work on each thing as I think of it, I write it down as an LLM task and then have Claude work through those in batches. Um, the kind of 

advantage that I've noticed with this is that it's frees me up to think about new things and just jot them down as I think of them and then don't get distracted with trying to steer Claude. If I do it in a batch, then Claude will do its best and then I can review that batch and if I find any issues, I can then create new LLM tasks for its next batch. So the guarding commits skill does two things. One is that it will prevent you 

from committing something which you don't want to commit. So you can create a file that lists those things. This might be something like passwords or email um certain keywords that you don't want to appear in your repository. And then another thing it does is that it enforces conventional commits. And it does both of these at commit time. So it will literally prevent you from committing anything that you don't want to be committed. And that applies to both the content and the commit messages themselves. 

So the enforcing periodic upgrade skill will enforce that you should upgrade every so often. So by default it um sets that to once a week. So, if you uh attempt to make a commit and it's been more than a week since your last upgrade, it's going to prevent that commit and tell you to perform some sort of upgrade. Uh the idea behind this is that Claude can keep churning away and then, you know, it'll 

prevent a few months from going by without you doing any sort of upgrades. This is going to keep that cadence pretty frequent. So the summarizing session skill will listen for when your session ends and it's going to send that off to Claude and have Claude summarize that session and then place that into a markdown file. The idea is that if you're using something like Obsidian, that directory can automatically be monitored by Obsidian and then you'll have notes for your sessions wherever you are. So you 

can look at those notes on your phone or wherever you might have Obsidian or a similar markdown tool installed. So, the self-improvement loop just got installed and I'm now running it. And what this does is uh basically lets Claw do all the work. This is similar to something you might have heard of called the Ralph Wigum loop. I had some issues with that one. I found it to not be too 

robust. It kept getting confused on the stock conditions. The way this one works is that you define a set of personas and this this will install a few example ones for you, but you can create arbitrary personas. So these are things like uh you're improving tests or you're going to add a new feature or you're refining how some other feature works. Um, the idea being that it toggles between each of these personas through 

each iteration of the loop and makes some sort of improvement. And it runs continuously until you tell it to stop. So, um, there are a few things that make this work a little more reliably than other tools that I've seen that do similar. One is that it will stop sessions that are taking too long. So this is a sign that maybe um there's uh for example claude has gone down the the API or 

maybe it's just getting confused about something. So you can cut that loop loop off automatically. And then another thing it'll do is warn when it's getting near that time. So it's not just going to stop work and interrupt it. It's going to give Claude a chance to finish things up, tidy them up before it actually does that final cut off. And then it'll take a little gap in between each iteration. So depending on your subscription level, you might want to adjust that gap and do it at whatever pace makes sense to, you know, use tokens at the rate that you would like. 

Um, and yeah, so it looks like it's a minute or so into its iteration. It outputs some of the stuffs it's doing as it does them. Um, I like to have the the runtime going just to get a sense of how long it's been going because I'll step away for maybe up to a few days and then come back and then see, you know, did it do what it was supposed to do. 

This is installing the SF symbol skill and the associated scripts that allow you to convert Mac OS's built-in SF symbols, which are basically icons, into actual SVG image files. It looks like it's loading the learning new skill or learning new text skill. And the idea behind this one is that it offers a sort of dynamic approach to learning new technologies. Uh so in this case it's it's using bun and if you wanted to learn bun you could use this 

skill to go through a sort of tutorial style that dynamically adapts to your existing skill set and gives you many exercises to work on and to learn that new tech. So the capturing test fixture skill is used to capture things like web pages that you would incorporate into automated tests. And the idea behind this is that usually you don't need to capture a full real web page to run in the test. If you do that, it thing 

things might run a little slow. It's going to be loading full libraries, maybe some uh analytics thing, some extra junk that's not relevant to the test. So this will capture the original, store the URL and other metadata related to that original snapshot, but then it's going to provide um some refinement to that. So one refinement is that it's going to automatically strip away the common stuff that's not needed. And then it's going to further do another refinement that uh uses the LLM to 

actually strip away conceptual bits that are not important to the test that you're building. So the claiming authorship skill that just got installed uh creates a mi.sh shell script and when you run it, it will rewrite the commit history to replace all those cloud commits with your own commit credentials. So now that the demo has run through all of the skills that are part of AI 

sorcery, it actually noticed a few things that occurred during the demo itself and then created an improvements file for suggestions to improve that. And I'm going to review those and have it fix some of those.