---
categories:
  - "[[Resources]]"
domain: engineering
title: "Karpathy's Skill Just Fixed Claude Code's Biggest Problem"
source: "https://www.youtube.com/watch?v=EsgUfrwsV5A"
author: "Eric Tech"
published: 2026-05-17
created: 2026-05-19
description: "Karpathy''s CLAUDE.md just hit 120K GitHub stars — so I dropped it into"
tags:
  - to-process
  - agent-configuration
---

In this video, we're going to go over this Andrej Karpathy skills, which got over 100,000 stars on GitHub. And this skill is derived from this expose that Andrej Karpathy has wrote. And if you don't know what Andrej Karpathy is, he is previously a director of AI at Tesla and a founding team at OpenAI. And currently, this expose has got over 7 million views on X. And essentially, what this skill does is addressing the problems that Andrej Karpathy sees on X. And the first problem we see is the model here always make the wrong assumption. So, it doesn't ask clarification questions. When you give 

it a problem, act on it. And the second problem that he sees is that model here often times over complicating things. Things can be wrote in 100 lines, often wrote in 1,000 lines. And often times, large language model here making changes that they're not supposed to without clear understanding about the full side effects. So, that's why in this video, we're going to take a look at what it is, how does it work, and how does it different compared to any other skills that we have used in the past. So, with that being said, if you're interested, let's get into the video. Now, before we continue, I recently launched our school community where help you to master AI 

agents, automations, and so much more. And that's all coming from someone who used to work as a senior AI software engineer at companies like Amazon and Microsoft. And in this community, you're going to get over 100 plus video materials like templates and workflows that I personally built and sold over 100 plus times. On top of that, you're also going to get access to our weekly live calls. And just to give you an idea, this week we're actually running a Claude call masterclass where we're going to dive into how to improve Claude call's accuracy, and we're going to use it to building applications. Plus, you're also going to get full community 

supports where you're going to get a chance to ask questions and get direct answers back. So, if you're ready to level up, make sure you jump right in, and I'll see you in a community. All right. So, to get started, let's take a look at what this skill is trying to offer. So, right here you can see this skill here offers four principles that we can use in our project, which will basically wrote inside of our Claude MD file. So, first principle here you can see is think before coding. Large language model here, like I said, makes wrong assumptions, doesn't clarify things. And by having this principle, it's going to force AI here to have to think before it's going to do the 

execution. And the second here is simplicity. Things that can be wrote in 100 lines of code never should be wrote like 500 or 1,000 lines of code, right? Never should be complicating things. And the success criteria here is that if a senior engineer says that this is over complicated, then we should definitely simplify. And that's exactly what this principle is trying to solve. And the third one here is surgical changes. So, let's say we're making changes. Large language models should never touch code that are not related to the instruction that we provide. And that's is actually what this principle does. And the last 

one that we have is goal-driven executions. We need to have a clear goal on exactly how large language models here perform before it's going to do the executions. And it's similar to the first one, but we need to have a clear success criteria for the expected behavior on the end result. And that's the four principles that the skill is trying to introduce, and they all compacted down into a single Claude MD file that we can add into a project to make sure that large language model here never hallucinates when writing code. Now, to put this into practice, here you can see it tells exactly how to install 

this. First of all, what we can do here is that we can install this in Claude plugins. Simply, we're just going to add the skill in our marketplace and install it. And the second option that we have is let's say if you want to install this not globally, but in a project level, simply you can just do with this curl command here and add this onto your new project. But if you have an existing project, you can simply just going to run this command right here, and simply it's going to write this rule onto your Claude MD file onto your existing project. Now, for my case here, I do have an existing project called bookzero.ai, where I help businesses here to manage receipts and transactions 

all using AI. And what I want to do here is I want to install this onto this project and see how does it work. Now, in order to install this, all I had to do here is just going to copy this command. It's going to install this on existing project. So, here I'm just going to come over to a project terminal, open a new terminal, and just going to paste that command here. And what this essentially this command does is going to modify my Claude MD file by simply adding those four rules onto there. So, in this case, I'm going to click click on enter, and you can see that it's going to modify my cloud MD file. So, now if I were to open the Git diff, and here you can see this is the 

changes that has applied. And for most of you guys, you probably already have your cloud MD file or your existing project. And by installing it, it might have some contradiction or conflict with your existing rules. So, what I highly recommend you to do is basically tell cloud code to basically try to modify your cloud MD file. Once you paste that, once you paste those four principles to see if there's any conflictions, any conflicts, anything that's not following what you have in your cloud MD file. Like try to merge the conflicts that you have. And you can see here that this is what it recommends. After it pasted from the original car party 

skills repository, here's some problem that I found. For example, we have the duplicate H1 tag for the cloud MD file because the cloud MD file already has that. And here you can see there's some meta framing here that really tells a human reader what a doc does, but the cloud MD file here doesn't really need that. It needs the instruction, a clear instruction on exactly what needs to do. And we has also have removed some redundant stuff that's not really relevant to our cloud MD file. And you can see cloud code has also removed that and make it more concise. So, again, 

same rule, less to read, so that we can be able to make our cloud MD file here more shorter. So, now you can see if I were to close this, this is exactly what it has modified, right? So, you can see we have our behavior guardrails. That's going to be an H2 tag. And now we have our think before coding and simplicity first, as well as the surgical changes and the goal-driven executions. So, you can see that all the four principles are still here, and there's no conflicts between what we have above versus what we have here. Okay? So, you can see that's exactly how this works. All right. So, now you know exactly how to 

install it, let's take a look at the clear difference between how they're different compared to all the skills that we have mentioned on this channel, like G stack, superpowers, GSD, all those spectrum development frameworks that we have introduced. And a clear difference is this. GSD, superpower, G stack, they are all skills. They're all skills that are being triggered whenever we trigger them, right? But Claude MD file is different is that we enforce those rules inside of a Claude MD file. I kind of like personality embedded into the model's brain. That every time when it do something, we don't have to 

mention it. It knows that because it's embedded into its personality, embedded into its soul that it's going to follow these four constraints every time we do something. When it asks to do I do anything, like maybe helping us to writing a blog post or helping us to generate images or helping us to writing code. It's going to embed that. It's going to do this exactly like we mentioned in our Claude MD file. So that's the clear difference between the two. Now, other than their types, let's talk about the functionalities, right? Because these four principles actually cover a lot of those things that we have 

mentioned previously on this channel for those skills that we have mentioned like G stack, superpower, and GSD. How is it different, right? In terms of functionality. And you can see here that I asked AI on exactly the difference. And you can see here that rule number two and rule number three here has pointed out by AI that is uniquely different compared to superpower and G stack because none of them has mentioned anything about like adding extra stuff or staying your lane or they don't really mention about these things as like the constraints. They both teach how to work carefully, but they don't 

know how much like to do, right? Your guardrails here, which is, you know, our Claude MD file here fix that gap by mentioning these things, right? And we also have something that's similar to what we have with superpower and G stack is rule number one and rule number four, which is think before coding and goal driven, right? That's exactly what spectrum development does is creating the plan before doing executions. And what superpower and G stack does a different is not just bunch of text sets inside of a Claude MD file is a framework that we have to first write 

our spec, from spec create a to-do list, and from to-do list creating a action, right? That's exactly what superpower and G stack does is creating a framework that large language model here follow, but it doesn't build into the brain. But most of them are very similar, right? The same rule, the same concept is very similar between the two. But that's why my recommendation, my workflow is combining the all of them, right? Combining the two. Not just showing them the constraints, but also giving them the path on exactly which skill to trigger. For example, each of the 

principles that Karpathy has mentioned, like think before coding, like don't assume, like service the the trade-off before writing code, we will give them the path on exactly what skill to trigger. For example, just a couple empty files not going to cut it. We're going to let them to basically direct them to trigger the superpower skills. Like for example, the superpower brainstorming skill for adding new features. Or if it's like bug, error, or test like test error, like test failure, we're going to have them to trigger the superpower system debugging skill. If 

it's a multi-step, like three files, we're just going to directly having them to trigger the writing plan skill or the GSD planning phase skill. Basically try to execute it really fast. Creating a to-do list and try to execute it, right? And for simplicity first, there's actually bunch of skills for simplicity, like making code more simplified, like minimize the code that solves the problem, nothing speculative. So you can see before committing, polish. So whenever we try to commit things, okay, well, let's trigger the simplify skill and try to simplify everything. All right, so pretty much that's it for this 

video and All right, so you can see that's pretty much it for this video. And if you do find my this video, please make sure to like this video, consider subscribe for more content like this. But with that being said, I'll see you in this video. And honestly, don't even stop there. You can also include in G stock, like the auto plan skill, where you can you have different rules here to introduce for think before coding. The possibility here is is endless, right? You can actually add a lot of things in here. For example, there's also surgical changes, you can also add like using different work trees for, you know, breaking it into different environments. And there's also 

goal-driven executions, right? Making sure that we're setting a clear goal, right? For the success criteria. So implement a feature or a bug fix. Okay, well, let's trigger the test driven developments here. If it's like executing a written plan, well, let's do the executing plan, right? So, there's actually a lot of skills that does that. For example, if we want to do a security review, there's also security review, there's also data audits, there's also QA. So, we'll give them path to the skills that we have and making sure that not only following the constraints, but also calling the right skills to act on 

it, right? So, you can see the possibility here is endless and you can just pick the skill that you want and just add it into your Claude MD file and Claude knows exactly what skill it's going to trigger based on your preference. Okay, so, pretty much that's it for this video and honestly, I don't want to have my Claude MD file here to be too long, so, I just wanted to keep it short. Just keep some skills that I really like inside of a Claude MD file. All right, so, you can see that's exactly the end of our skills. And of course, if you're interested in learning more about spectrum development models, be sure to check out the playlist here inside of the description below, where I 

show you all the spectrum development models that I talk about on this channel on how you can be able to make your large language model here to be highly accurate when performing task on your project, right? So, if you're interested for that, make sure to check it out in the link in the description below. With that being said, if you do feel my this video, please make sure to like this video, consider to subscribe for more content like this. With that being said, I'll see you in the next video. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 In this video, we're going to go over
 </span>
 <span data-rw-start="1.12" data-rw-transcript-version="2">
 this Andrej Karpathy skills, which got
 </span>
 <span data-rw-start="2.8" data-rw-transcript-version="2">
 over 100,000 stars on GitHub. And this
 </span>
 <span data-rw-start="5.6" data-rw-transcript-version="2">
 skill is derived from this expose that
 </span>
 <span data-rw-start="7.76" data-rw-transcript-version="2">
 Andrej Karpathy has wrote. And if you
 </span>
 <span data-rw-start="9.56" data-rw-transcript-version="2">
 don't know what Andrej Karpathy is, he
 </span>
 <span data-rw-start="11.08" data-rw-transcript-version="2">
 was previously a director of AI at Tesla
 </span>
 <span data-rw-start="13.56" data-rw-transcript-version="2">
 and a founding team member at OpenAI.
 </span>
 <span data-rw-start="15.8" data-rw-transcript-version="2">
 Currently, this expose has got over 7
 </span>
 <span data-rw-start="17.72" data-rw-transcript-version="2">
 million views on X. And essentially,
 </span>
 <span data-rw-start="19.88" data-rw-transcript-version="2">
 what this skill does is address the
 </span>
 <span data-rw-start="21.76" data-rw-transcript-version="2">
 problems that Andrej Karpathy sees on X.
 </span>
 <span data-rw-start="24.2" data-rw-transcript-version="2">
 And the first problem we see is that the
 </span>
 <span data-rw-start="25.6" data-rw-transcript-version="2">
 model here always makes the wrong
 </span>
 <span data-rw-start="26.92" data-rw-transcript-version="2">
 assumption. So, it doesn't ask
 </span>
 <span data-rw-start="29" data-rw-transcript-version="2">
 clarification questions. When you give
 </span>
 <span data-rw-start="30.52" data-rw-transcript-version="2">
 it a problem, act on it. And the second
 </span>
 <span data-rw-start="32.84" data-rw-transcript-version="2">
 problem that he sees is that the model here
 </span>
 <span data-rw-start="35" data-rw-transcript-version="2">
 often times overcomplicates things.
 </span>
</p>
<p>
 <span data-rw-start="37.4" data-rw-transcript-version="2">
 Things can be written in 100 lines, often
 </span>
 <span data-rw-start="39.48" data-rw-transcript-version="2">
 written in 1,000 lines. And often times,
 </span>
 <span data-rw-start="41.96" data-rw-transcript-version="2">
 large language models here make changes
 </span>
 <span data-rw-start="43.84" data-rw-transcript-version="2">
 that they're not supposed to without
 </span>
 <span data-rw-start="45.44" data-rw-transcript-version="2">
 clear understanding of the full side
 </span>
 <span data-rw-start="47.04" data-rw-transcript-version="2">
 effects. So, that's why in this video,
 </span>
 <span data-rw-start="48.52" data-rw-transcript-version="2">
 We're going to take a look at what it
 </span>
 <span data-rw-start="49.52" data-rw-transcript-version="2">
 is, how does it work, and how does it
 </span>
 <span data-rw-start="51.36" data-rw-transcript-version="2">
 different compared to any other skills
 </span>
 <span data-rw-start="52.96" data-rw-transcript-version="2">
 that we have used in the past. So, with
 </span>
 <span data-rw-start="54.48" data-rw-transcript-version="2">
 that being said, if you're interested,
 </span>
 <span data-rw-start="55.96" data-rw-transcript-version="2">
 let's get into the video. Now, before we
 </span>
 <span data-rw-start="57.48" data-rw-transcript-version="2">
 continue, I recently launched our school
 </span>
 <span data-rw-start="59.2" data-rw-transcript-version="2">
 community where I help you to master AI
 </span>
 <span data-rw-start="60.92" data-rw-transcript-version="2">
 agents, automations, and so much more.
 </span>
</p>
<p>
 <span data-rw-start="63.48" data-rw-transcript-version="2">
 And that's all coming from someone who
 </span>
 <span data-rw-start="64.879" data-rw-transcript-version="2">
 used to work as a senior AI software
 </span>
 <span data-rw-start="66.72" data-rw-transcript-version="2">
 engineer at companies like Amazon and
 </span>
 <span data-rw-start="69.04" data-rw-transcript-version="2">
 Microsoft. And in this community, you're
 </span>
 <span data-rw-start="71" data-rw-transcript-version="2">
 going to get over 100 plus video
 </span>
 <span data-rw-start="72.36" data-rw-transcript-version="2">
 materials like templates and workflows
 </span>
 <span data-rw-start="74.56" data-rw-transcript-version="2">
 that I personally built and sold over
 </span>
 <span data-rw-start="76.44" data-rw-transcript-version="2">
 100 plus times. On top of that, you're
 </span>
 <span data-rw-start="78.32" data-rw-transcript-version="2">
 also going to get access to our weekly
 </span>
 <span data-rw-start="80.04" data-rw-transcript-version="2">
 live calls. And just to give you an
 </span>
 <span data-rw-start="81.44" data-rw-transcript-version="2">
 idea, this week's actually running a
 </span>
 <span data-rw-start="83.2" data-rw-transcript-version="2">
 Claude call masterclass where we're
 </span>
 <span data-rw-start="84.56" data-rw-transcript-version="2">
 going to dive into how to improve Claude
 </span>
 <span data-rw-start="86.6" data-rw-transcript-version="2">
 call's accuracy, and we're going to use
 </span>
 <span data-rw-start="88.16" data-rw-transcript-version="2">
 it to build applications. Plus,
 </span>
 <span data-rw-start="90" data-rw-transcript-version="2">
 you're also going to get full community.
 </span>
</p>
<p>
 <span data-rw-start="91.04" data-rw-transcript-version="2">
 Supports where you're going to get a
 </span>
 <span data-rw-start="92.24" data-rw-transcript-version="2">
 chance to ask questions and get direct
 </span>
 <span data-rw-start="94.04" data-rw-transcript-version="2">
 answers back. So, if you're ready to
 </span>
 <span data-rw-start="95.44" data-rw-transcript-version="2">
 level up, make sure you jump right in,
 </span>
 <span data-rw-start="97.04" data-rw-transcript-version="2">
 and I'll see you in a community. All
 </span>
 <span data-rw-start="98.6" data-rw-transcript-version="2">
 right. So, to get started, let's take a
 </span>
 <span data-rw-start="99.92" data-rw-transcript-version="2">
 look at what this skill is trying to
 </span>
 <span data-rw-start="101.16" data-rw-transcript-version="2">
 offer. So, right here you can see this
 </span>
 <span data-rw-start="102.76" data-rw-transcript-version="2">
 skill here offers four principles that
 </span>
 <span data-rw-start="104.84" data-rw-transcript-version="2">
 we can use in our project, which will
 </span>
 <span data-rw-start="106.4" data-rw-transcript-version="2">
 basically write inside of our Claude MD
 </span>
 <span data-rw-start="108.28" data-rw-transcript-version="2">
 file. So, the first principle here you can
 </span>
 <span data-rw-start="109.92" data-rw-transcript-version="2">
 see is think before coding. Large
 </span>
 <span data-rw-start="112" data-rw-transcript-version="2">
 language model here, like I said, makes
 </span>
 <span data-rw-start="113.6" data-rw-transcript-version="2">
 wrong assumptions, doesn't clarify
 </span>
 <span data-rw-start="115.16" data-rw-transcript-version="2">
 things. And by having this principle,
 </span>
 <span data-rw-start="116.92" data-rw-transcript-version="2">
 it's going to force AI here to have to
 </span>
 <span data-rw-start="119.36" data-rw-transcript-version="2">
 think before it's going to do the
 </span>
 <span data-rw-start="121" data-rw-transcript-version="2">
 execution. And the second here is
 </span>
 <span data-rw-start="123.32" data-rw-transcript-version="2">
 simplicity. Things that can be written in
 </span>
 <span data-rw-start="125.32" data-rw-transcript-version="2">
 100 lines of code never should be written
 </span>
 <span data-rw-start="127.16" data-rw-transcript-version="2">
 like 500 or 1,000 lines of code, right?
 </span>
</p>
<p>
 <span data-rw-start="129.36" data-rw-transcript-version="2">
 Never should be complicating things. And
 </span>
 <span data-rw-start="131.32" data-rw-transcript-version="2">
 the success criteria here is that if a
 </span>
 <span data-rw-start="134.76" data-rw-transcript-version="2">
 Complicated, then we should definitely
 </span>
 <span data-rw-start="136.28" data-rw-transcript-version="2">
 simplify. And that's exactly what this
 </span>
 <span data-rw-start="138.08" data-rw-transcript-version="2">
 principle is trying to solve. And the
 </span>
 <span data-rw-start="139.68" data-rw-transcript-version="2">
 third one here is surgical changes. So,
 </span>
 <span data-rw-start="141.92" data-rw-transcript-version="2">
 let's say we're making changes. Large
 </span>
 <span data-rw-start="143.52" data-rw-transcript-version="2">
 language models should never touch code
 </span>
 <span data-rw-start="145.08" data-rw-transcript-version="2">
 that are not related to the instruction
 </span>
 <span data-rw-start="146.92" data-rw-transcript-version="2">
 that we provide. And that's what this principle does. And the
 </span>
 <span data-rw-start="148.76" data-rw-transcript-version="2">
 last
 </span>
 <span data-rw-start="150.36" data-rw-transcript-version="2">
 one that we have is goal-driven
 </span>
 <span data-rw-start="151.84" data-rw-transcript-version="2">
 executions. We need to have a clear goal
 </span>
 <span data-rw-start="154.36" data-rw-transcript-version="2">
 on exactly how large language models
 </span>
 <span data-rw-start="156.04" data-rw-transcript-version="2">
 here perform before it's going to do the
 </span>
 <span data-rw-start="158.12" data-rw-transcript-version="2">
 executions. And it's similar to the
 </span>
 <span data-rw-start="160.2" data-rw-transcript-version="2">
 first one, but we need to have a clear
 </span>
 <span data-rw-start="162.44" data-rw-transcript-version="2">
 success criteria for the expected
 </span>
 <span data-rw-start="164.44" data-rw-transcript-version="2">
 behavior on the end result. And that's
 </span>
 <span data-rw-start="166.6" data-rw-transcript-version="2">
 the four principles that the skill is
 </span>
 <span data-rw-start="168.32" data-rw-transcript-version="2">
 trying to introduce, and they all
 </span>
 <span data-rw-start="169.8" data-rw-transcript-version="2">
 are compacted down into a single Claude MD
 </span>
 <span data-rw-start="171.84" data-rw-transcript-version="2">
 file that we can add into a project to
 </span>
 <span data-rw-start="174.12" data-rw-transcript-version="2">
 make sure that large language model here
 </span>
 <span data-rw-start="175.4" data-rw-transcript-version="2">
 never hallucinates when writing code.
 </span>
</p>
<p>
 <span data-rw-start="177.44" data-rw-transcript-version="2">
 Now, to put this into practice, here you
 </span>
 <span data-rw-start="178.92" data-rw-transcript-version="2">
 can see it tells exactly how to install.
 </span>
</p>
<p>
 <span data-rw-start="180.56" data-rw-transcript-version="2">
 This. First of all, what we can do here
 </span>
 <span data-rw-start="182.12" data-rw-transcript-version="2">
 is that we can install this in Claude
 </span>
 <span data-rw-start="183.56" data-rw-transcript-version="2">
 plugins. Simply, we're just going to add
 </span>
 <span data-rw-start="185.12" data-rw-transcript-version="2">
 the skill in our marketplace and install
 </span>
 <span data-rw-start="186.76" data-rw-transcript-version="2">
 it. And the second option that we have
 </span>
 <span data-rw-start="188.88" data-rw-transcript-version="2">
 is let's say if you want to install this
 </span>
 <span data-rw-start="190.4" data-rw-transcript-version="2">
 not globally, but in a project level,
 </span>
 <span data-rw-start="192.8" data-rw-transcript-version="2">
 simply you can just do with this curl
 </span>
 <span data-rw-start="194.239" data-rw-transcript-version="2">
 command here and add this onto your new
 </span>
 <span data-rw-start="195.84" data-rw-transcript-version="2">
 project. But if you have an existing
 </span>
 <span data-rw-start="197.48" data-rw-transcript-version="2">
 project, you can simply just go to
 </span>
 <span data-rw-start="199" data-rw-transcript-version="2">
 run this command right here, and simply
 </span>
 <span data-rw-start="200.84" data-rw-transcript-version="2">
 it's going to write this rule onto your
 </span>
 <span data-rw-start="202.12" data-rw-transcript-version="2">
 Claude MD file onto your existing
 </span>
 <span data-rw-start="203.92" data-rw-transcript-version="2">
 project. Now, for my case here, I do
 </span>
 <span data-rw-start="205.56" data-rw-transcript-version="2">
 have an existing project called
 </span>
 <span data-rw-start="206.72" data-rw-transcript-version="2">
 bookzero.ai, where I help businesses
 </span>
 <span data-rw-start="208.6" data-rw-transcript-version="2">
 here to manage receipts and transactions
 </span>
</p>
<p>
 <span data-rw-start="210.44" data-rw-transcript-version="2">
 all using AI. And what I want to do here
 </span>
 <span data-rw-start="212.28" data-rw-transcript-version="2">
 is I want to install this onto this
 </span>
 <span data-rw-start="213.6" data-rw-transcript-version="2">
 project and see how does it work. Now,
 </span>
 <span data-rw-start="215.44" data-rw-transcript-version="2">
 in order to install this, all I had to
 </span>
 <span data-rw-start="216.76" data-rw-transcript-version="2">
 do here is just going to copy this
 </span>
 <span data-rw-start="217.72" data-rw-transcript-version="2">
 command. It's going to install this on
 </span>
 <span data-rw-start="219.239" data-rw-transcript-version="2">
 existing project. So, here I'm just
 </span>
 <span data-rw-start="220.959" data-rw-transcript-version="2">
 Going to come over to a project
 </span>
 <span data-rw-start="222.88" data-rw-transcript-version="2">
 terminal, open a new terminal, and just
 </span>
 <span data-rw-start="224.519" data-rw-transcript-version="2">
 going to paste that command here. And
 </span>
 <span data-rw-start="226.12" data-rw-transcript-version="2">
 what this essentially does
 </span>
 <span data-rw-start="227.6" data-rw-transcript-version="2">
 is going to modify my Claude MD file by
 </span>
 <span data-rw-start="230.12" data-rw-transcript-version="2">
 simply adding those four rules onto
 </span>
 <span data-rw-start="231.68" data-rw-transcript-version="2">
 there. So, in this case, I'm going to
 </span>
 <span data-rw-start="233.32" data-rw-transcript-version="2">
 click on enter, and you can see
 </span>
 <span data-rw-start="235.12" data-rw-transcript-version="2">
 that it's going to modify my cloud MD
 </span>
 <span data-rw-start="236.88" data-rw-transcript-version="2">
 file.
 </span>
</p>
<p>
 <span data-rw-start="238.92" data-rw-transcript-version="2">
 So, now if I were to open the Git
 </span>
 <span data-rw-start="240.36" data-rw-transcript-version="2">
 diff, and here you can see this is the
 </span>
 <span data-rw-start="242.16" data-rw-transcript-version="2">
 changes that have been applied. And for most
 </span>
 <span data-rw-start="243.4" data-rw-transcript-version="2">
 of you guys, you probably already have
 </span>
 <span data-rw-start="245" data-rw-transcript-version="2">
 your cloud MD file or your existing
 </span>
 <span data-rw-start="247.52" data-rw-transcript-version="2">
 project. And by installing it, it might
 </span>
 <span data-rw-start="249.72" data-rw-transcript-version="2">
 have some contradiction or conflict with
 </span>
 <span data-rw-start="251.64" data-rw-transcript-version="2">
 your existing rules. So, what I highly
 </span>
 <span data-rw-start="253.36" data-rw-transcript-version="2">
 recommend you do is basically tell
 </span>
 <span data-rw-start="255.52" data-rw-transcript-version="2">
 cloud code to basically try to modify
 </span>
 <span data-rw-start="257.64" data-rw-transcript-version="2">
 your cloud MD file. Once you paste that,
 </span>
 <span data-rw-start="258.959" data-rw-transcript-version="2">
 once you paste those four principles to
 </span>
 <span data-rw-start="260.68" data-rw-transcript-version="2">
 see if there's any conflicts,
 </span>
 <span data-rw-start="263.16" data-rw-transcript-version="2">
 any conflicts, or anything that's not
 </span>
 <span data-rw-start="264.88" data-rw-transcript-version="2">
 following what you have in your cloud MD
 </span>
 <span data-rw-start="266.16" data-rw-transcript-version="2">
 file. Like, try to merge the conflicts.
 </span>
</p>
<p>
 <span data-rw-start="266.48" data-rw-transcript-version="2">
 That you have. And you can see here that
 </span>
 <span data-rw-start="268.12" data-rw-transcript-version="2">
 this is what it recommends. After it
 </span>
 <span data-rw-start="269.6" data-rw-transcript-version="2">
 pasted from the original car party
 </span>
 <span data-rw-start="271.76" data-rw-transcript-version="2">
 skills repository, here's some problem
 </span>
 <span data-rw-start="273.8" data-rw-transcript-version="2">
 that I found. For example, we have the
 </span>
 <span data-rw-start="275.6" data-rw-transcript-version="2">
 duplicate H1 tag for the cloud MD file
 </span>
 <span data-rw-start="278.44" data-rw-transcript-version="2">
 because the cloud MD file already has
 </span>
 <span data-rw-start="280.08" data-rw-transcript-version="2">
 that. And here you can see there's some
 </span>
 <span data-rw-start="281.8" data-rw-transcript-version="2">
 meta framing here that really tells a
 </span>
 <span data-rw-start="283.68" data-rw-transcript-version="2">
 human reader what a doc does, but the
 </span>
 <span data-rw-start="285.72" data-rw-transcript-version="2">
 cloud MD file here doesn't really need
 </span>
 <span data-rw-start="287.52" data-rw-transcript-version="2">
 that. It needs the instruction, a clear
 </span>
 <span data-rw-start="289.8" data-rw-transcript-version="2">
 instruction on exactly what needs to do.
 </span>
</p>
<p>
 <span data-rw-start="291.52" data-rw-transcript-version="2">
 And we have also removed some
 </span>
 <span data-rw-start="292.919" data-rw-transcript-version="2">
 redundant stuff that's not really
 </span>
 <span data-rw-start="294.36" data-rw-transcript-version="2">
 relevant to our cloud MD file. And you
 </span>
 <span data-rw-start="296.52" data-rw-transcript-version="2">
 can see, cloud code has also removed that
 </span>
 <span data-rw-start="298.32" data-rw-transcript-version="2">
 and made it more concise. So, again,
 </span>
 <span data-rw-start="300.48" data-rw-transcript-version="2">
 same rule, less to read, so that we can
 </span>
 <span data-rw-start="302.6" data-rw-transcript-version="2">
 be able to make our cloud MD file here
 </span>
 <span data-rw-start="304.04" data-rw-transcript-version="2">
 shorter. So, now you can see, if I
 </span>
 <span data-rw-start="305.68" data-rw-transcript-version="2">
 were to close this, this is exactly what
 </span>
 <span data-rw-start="307.68" data-rw-transcript-version="2">
 it has modified, right? So, you can see
 </span>
 <span data-rw-start="309.12" data-rw-transcript-version="2">
 we have our behavior guardrails. That's
 </span>
 <span data-rw-start="310.96" data-rw-transcript-version="2">
 going to be an H2 tag. And now we have
 </span>
 <span data-rw-start="313.52" data-rw-transcript-version="2">
 Our think before coding and simplicity,
 </span>
 <span data-rw-start="316.08" data-rw-transcript-version="2">
 first, as well as the surgical changes
 </span>
 <span data-rw-start="318.72" data-rw-transcript-version="2">
 and the goal-driven executions.
 </span>
</p>
<p>
 <span data-rw-start="321.08" data-rw-transcript-version="2">
 So, you can see that all the four principles are
 </span>
 <span data-rw-start="322.48" data-rw-transcript-version="2">
 still here, and there's no conflicts
 </span>
 <span data-rw-start="324.28" data-rw-transcript-version="2">
 between what we have above versus what
 </span>
 <span data-rw-start="326.04" data-rw-transcript-version="2">
 we have here. Okay?
 </span>
 <span data-rw-start="327.6" data-rw-transcript-version="2">
 So, you can see
 </span>
 <span data-rw-start="329" data-rw-transcript-version="2">
 that’s exactly how this works. All
 </span>
 <span data-rw-start="330.24" data-rw-transcript-version="2">
 right. So, now you know exactly how to
 </span>
 <span data-rw-start="331.68" data-rw-transcript-version="2">
 install it, let’s take a look at the
 </span>
 <span data-rw-start="333.12" data-rw-transcript-version="2">
 clear difference between how they’re
 </span>
 <span data-rw-start="334.32" data-rw-transcript-version="2">
 different compared to all the skills
 </span>
 <span data-rw-start="335.8" data-rw-transcript-version="2">
 that we have mentioned on this channel,
 </span>
 <span data-rw-start="338.28" data-rw-transcript-version="2">
 like G stack, superpowers, GSD, all
 </span>
 <span data-rw-start="339.76" data-rw-transcript-version="2">
 those spectrum development frameworks
 </span>
 <span data-rw-start="341.52" data-rw-transcript-version="2">
 that we have introduced. And a clear
 </span>
 <span data-rw-start="344.32" data-rw-transcript-version="2">
 difference is this. GSD, superpower, G
 </span>
 <span data-rw-start="346.44" data-rw-transcript-version="2">
 stack, they are all skills. They’re all
 </span>
 <span data-rw-start="348.2" data-rw-transcript-version="2">
 skills that are being triggered whenever
 </span>
 <span data-rw-start="350.72" data-rw-transcript-version="2">
 we trigger them, right? But Claude MD
 </span>
 <span data-rw-start="352.96" data-rw-transcript-version="2">
 file is different, is that we enforce
 </span>
 <span data-rw-start="354.8" data-rw-transcript-version="2">
 those rules inside of a Claude MD file.
 </span>
</p>
<p>
 <span data-rw-start="356.76" data-rw-transcript-version="2">
 I kind of like personality embedded into
 </span>
 <span data-rw-start="358.64" data-rw-transcript-version="2">
 the model's brain. That every time when
 </span>
 <span data-rw-start="360.0" data-rw-transcript-version="2">
 it do something, we don't have to
 </span>
 <span data-rw-start="360.12" data-rw-transcript-version="2">
 Mention it. It knows that because it's
 </span>
 <span data-rw-start="362.24" data-rw-transcript-version="2">
 embedded into its personality, embedded
 </span>
 <span data-rw-start="364.32" data-rw-transcript-version="2">
 into its soul that it's going to follow
 </span>
 <span data-rw-start="366.44" data-rw-transcript-version="2">
 these four constraints every time we do
 </span>
 <span data-rw-start="368.44" data-rw-transcript-version="2">
 something. When it asks to do I do
 </span>
 <span data-rw-start="369.76" data-rw-transcript-version="2">
 anything, like maybe helping us to
 </span>
 <span data-rw-start="372.24" data-rw-transcript-version="2">
 write a blog post or helping us to
 </span>
 <span data-rw-start="374.4" data-rw-transcript-version="2">
 generate images or helping us to writing
 </span>
 <span data-rw-start="376.08" data-rw-transcript-version="2">
 code. It's going to embed that. It's
 </span>
 <span data-rw-start="378.08" data-rw-transcript-version="2">
 going to do this exactly like we
 </span>
 <span data-rw-start="379.919" data-rw-transcript-version="2">
 mentioned in our Claude MD file. So
 </span>
 <span data-rw-start="381.52" data-rw-transcript-version="2">
 that's the clear difference between the
 </span>
 <span data-rw-start="382.68" data-rw-transcript-version="2">
 two. Now, other than their types, let's
 </span>
 <span data-rw-start="384.84" data-rw-transcript-version="2">
 talk about the functionalities, right?
 </span>
</p>
<p>
 <span data-rw-start="387.04" data-rw-transcript-version="2">
 Because these four principles actually
 </span>
 <span data-rw-start="389.08" data-rw-transcript-version="2">
 cover a lot of those things that we have
 </span>
 <span data-rw-start="390.96" data-rw-transcript-version="2">
 mentioned previously on this channel for
 </span>
 <span data-rw-start="392.919" data-rw-transcript-version="2">
 those skills that we have mentioned like
 </span>
 <span data-rw-start="394.28" data-rw-transcript-version="2">
 G stack, superpower, and GSD. How is it
 </span>
 <span data-rw-start="397.4" data-rw-transcript-version="2">
 different, right? In terms of
 </span>
 <span data-rw-start="398.919" data-rw-transcript-version="2">
 functionality. And you can see here that
 </span>
 <span data-rw-start="400.68" data-rw-transcript-version="2">
 I asked AI on exactly the difference.
 </span>
 <span data-rw-start="403.04" data-rw-transcript-version="2">
 And you can see here that rule number
 </span>
 <span data-rw-start="404.4" data-rw-transcript-version="2">
 two and rule number three here have
 </span>
 <span data-rw-start="405.68" data-rw-transcript-version="2">
 been pointed out by AI that is uniquely.
 </span>
</p>
<p>
 <span data-rw-start="407.44" data-rw-transcript-version="2">
 Different compared to superpower and G stack because none of them has mentioned
 </span>
 <span data-rw-start="409.24" data-rw-transcript-version="2">
 anything about like adding extra stuff
 </span>
 <span data-rw-start="411.56" data-rw-transcript-version="2">
 or staying in your lane or they don't
 </span>
 <span data-rw-start="414.08" data-rw-transcript-version="2">
 really mention these things as
 </span>
 <span data-rw-start="416" data-rw-transcript-version="2">
 like the constraints. They both teach
 </span>
 <span data-rw-start="417.76" data-rw-transcript-version="2">
 how to work carefully, but they don't
 </span>
 <span data-rw-start="419.56" data-rw-transcript-version="2">
 know how much to do, right? Your
 </span>
 <span data-rw-start="421.04" data-rw-transcript-version="2">
 guardrails here, which is, you know, our
 </span>
 <span data-rw-start="423.56" data-rw-transcript-version="2">
 Claude MD file here fixes that gap by
 </span>
 <span data-rw-start="425.16" data-rw-transcript-version="2">
 mentioning these things, right? And we
 </span>
 <span data-rw-start="427.4" data-rw-transcript-version="2">
 also have something that's similar to
 </span>
 <span data-rw-start="429.36" data-rw-transcript-version="2">
 what we have with superpower and G stack
 </span>
 <span data-rw-start="430.68" data-rw-transcript-version="2">
 is rule number one and rule number four,
 </span>
 <span data-rw-start="432.04" data-rw-transcript-version="2">
 which is think before coding and goal
 </span>
</p>
<p>
 <span data-rw-start="433.96" data-rw-transcript-version="2">
 driven, right? That's exactly what
 </span>
 <span data-rw-start="435.84" data-rw-transcript-version="2">
 spectrum development does — creating
 </span>
 <span data-rw-start="437.64" data-rw-transcript-version="2">
 the plan before doing executions. And
 </span>
 <span data-rw-start="440.36" data-rw-transcript-version="2">
 what superpower and G stack do differently is not just a bunch of text sets
 </span>
 <span data-rw-start="446.76" data-rw-transcript-version="2">
 inside of a Claude MD file, but a
 </span>
 <span data-rw-start="448.56" data-rw-transcript-version="2">
 framework that we have to first write
 </span>
 <span data-rw-start="450.56" data-rw-transcript-version="2">
 our spec, then create a to-do list from the spec,
 </span>
 <span data-rw-start="453.36" data-rw-transcript-version="2">
 and from the to-do list, create an action.
 </span>
 <span data-rw-start="455.88" data-rw-transcript-version="2">
 That's exactly what superpower
 </span>
 <span data-rw-start="457.6" data-rw-transcript-version="2">
 And G stack does is creating a framework
 </span>
 <span data-rw-start="459.36" data-rw-transcript-version="2">
 that large language model here follow,
 </span>
 <span data-rw-start="461" data-rw-transcript-version="2">
 but it doesn't build into the brain. But
 </span>
 <span data-rw-start="463.08" data-rw-transcript-version="2">
 most of them are very similar, right?
 </span>
</p>
<p>
 <span data-rw-start="464.84" data-rw-transcript-version="2">
 The same rule, the same concept is very
 </span>
 <span data-rw-start="466.8" data-rw-transcript-version="2">
 similar between the two. But that's why
 </span>
 <span data-rw-start="468.68" data-rw-transcript-version="2">
 my recommendation, my workflow is
 </span>
 <span data-rw-start="470.88" data-rw-transcript-version="2">
 combining all of them, right?
 </span>
 <span data-rw-start="472.72" data-rw-transcript-version="2">
 Combining the two. Not just showing them
 </span>
 <span data-rw-start="475.2" data-rw-transcript-version="2">
 the constraints, but also giving them
 </span>
 <span data-rw-start="477.16" data-rw-transcript-version="2">
 the path on exactly which skill to
 </span>
 <span data-rw-start="479.16" data-rw-transcript-version="2">
 trigger. For example, each of the
 </span>
 <span data-rw-start="481.08" data-rw-transcript-version="2">
 principles that Karpathy has mentioned,
 </span>
 <span data-rw-start="483.24" data-rw-transcript-version="2">
 like think before coding, like don't
 </span>
 <span data-rw-start="485.24" data-rw-transcript-version="2">
 assume, like solve the trade-off
 </span>
 <span data-rw-start="487.48" data-rw-transcript-version="2">
 before writing code, we will give them
 </span>
 <span data-rw-start="489.48" data-rw-transcript-version="2">
 the path on exactly what skill to
 </span>
 <span data-rw-start="491.16" data-rw-transcript-version="2">
 trigger. For example, just a couple
 </span>
 <span data-rw-start="492.96" data-rw-transcript-version="2">
 empty files won't cut it. We're
 </span>
 <span data-rw-start="494.72" data-rw-transcript-version="2">
 going to let them basically direct
 </span>
 <span data-rw-start="496.24" data-rw-transcript-version="2">
 them to trigger the superpower skills.
 </span>
</p>
<p>
 <span data-rw-start="498.32" data-rw-transcript-version="2">
 Like, for example, the superpower
 </span>
 <span data-rw-start="499.56" data-rw-transcript-version="2">
 brainstorming skill for adding new
 </span>
 <span data-rw-start="501.36" data-rw-transcript-version="2">
 features. Or if it's like bug, error, or
 </span>
 <span data-rw-start="503.68" data-rw-transcript-version="2">
 test, like test error, like test failure.
 </span>
</p>
<p>
 <span data-rw-start="506.24" data-rw-transcript-version="2">
 We're going to have them trigger the superpower system debugging skill. If
 </span>
 <span data-rw-start="507.4" data-rw-transcript-version="2">
 it's a multi-step, like three files,
 </span>
 <span data-rw-start="510.08" data-rw-transcript-version="2">
 we're just going to directly have them
 </span>
 <span data-rw-start="512.2" data-rw-transcript-version="2">
 trigger the writing plan skill or the
 </span>
 <span data-rw-start="513.919" data-rw-transcript-version="2">
 GSD planning phase skill. Basically, try
 </span>
 <span data-rw-start="515.599" data-rw-transcript-version="2">
 to execute it really fast, creating a
 </span>
 <span data-rw-start="520.599" data-rw-transcript-version="2">
 to-do list and trying to execute it, right?
 </span>
 <span data-rw-start="522.4" data-rw-transcript-version="2">
 And for simplicity, first, there are
 </span>
 <span data-rw-start="524.12" data-rw-transcript-version="2">
 actually a bunch of skills for simplicity,
 </span>
 <span data-rw-start="526.32" data-rw-transcript-version="2">
 like making code more simplified, like
 </span>
 <span data-rw-start="528.36" data-rw-transcript-version="2">
 minimize the code that solves the
 </span>
 <span data-rw-start="530.16" data-rw-transcript-version="2">
 problem, nothing speculative. So, you can
 </span>
 <span data-rw-start="532.6" data-rw-transcript-version="2">
 see before committing, polish. So,
 </span>
 <span data-rw-start="534.6" data-rw-transcript-version="2">
 whenever we try to commit things, okay,
 </span>
 <span data-rw-start="536.32" data-rw-transcript-version="2">
 well, let's trigger the simplify skill
 </span>
 <span data-rw-start="537.839" data-rw-transcript-version="2">
 and try to simplify everything. All
 </span>
 <span data-rw-start="539.24" data-rw-transcript-version="2">
 right, so pretty much that's it for this
 </span>
 <span data-rw-start="540.28" data-rw-transcript-version="2">
 video, and all right, so you can see
 </span>
 <span data-rw-start="542.04" data-rw-transcript-version="2">
 that's pretty much it for this video.
 </span>
</p>
<p>
 <span data-rw-start="543.24" data-rw-transcript-version="2">
 And if you do find this video, please
 </span>
 <span data-rw-start="545.04" data-rw-transcript-version="2">
 make sure to like this video, consider
 </span>
 <span data-rw-start="546.76" data-rw-transcript-version="2">
 subscribing for more content like this.
 </span>
 <span data-rw-start="548.24" data-rw-transcript-version="2">
 But with that being said, I'll see you
 </span>
 <span data-rw-start="549.72" data-rw-transcript-version="2">
 in this video. And honestly, I don't even
 </span>
 <span data-rw-start="551.64" data-rw-transcript-version="2">
 Stop there. You can also include in G
 </span>
 <span data-rw-start="553.44" data-rw-transcript-version="2">
 stock, like the auto plan skill, where
 </span>
 <span data-rw-start="555.36" data-rw-transcript-version="2">
 you can have different rules here to
 </span>
 <span data-rw-start="556.88" data-rw-transcript-version="2">
 introduce for thinking before coding. The
 </span>
 <span data-rw-start="559.16" data-rw-transcript-version="2">
 possibility here is endless, right?
 </span>
</p>
<p>
 <span data-rw-start="560.92" data-rw-transcript-version="2">
 You can actually add a lot of things in
 </span>
 <span data-rw-start="562.36" data-rw-transcript-version="2">
 here. For example, there are also surgical
 </span>
 <span data-rw-start="564.2" data-rw-transcript-version="2">
 changes; you can also add, like, using
 </span>
 <span data-rw-start="566.16" data-rw-transcript-version="2">
 different work trees for, you know,
 </span>
 <span data-rw-start="567.839" data-rw-transcript-version="2">
 breaking it into different environments.
 </span>
</p>
<p>
 <span data-rw-start="569.68" data-rw-transcript-version="2">
 And there are also
 </span>
 <span data-rw-start="570.96" data-rw-transcript-version="2">
 goal-driven executions, right? Making
 </span>
 <span data-rw-start="572.8" data-rw-transcript-version="2">
 sure that we're setting a clear goal,
 </span>
 <span data-rw-start="575.12" data-rw-transcript-version="2">
 right? For the success criteria. So
 </span>
 <span data-rw-start="577.32" data-rw-transcript-version="2">
 implement a feature or a bug fix. Okay,
 </span>
 <span data-rw-start="579.32" data-rw-transcript-version="2">
 well, let's trigger the test-driven
 </span>
 <span data-rw-start="580.6" data-rw-transcript-version="2">
 development here. If it's like
 </span>
 <span data-rw-start="582.16" data-rw-transcript-version="2">
 executing a written plan, well, let's do
 </span>
 <span data-rw-start="584.48" data-rw-transcript-version="2">
 the executing plan, right? So, there are
 </span>
 <span data-rw-start="586.36" data-rw-transcript-version="2">
 actually a lot of skills that do that.
 </span>
</p>
<p>
 <span data-rw-start="588.16" data-rw-transcript-version="2">
 For example, if we want to conduct a security
 </span>
 <span data-rw-start="589.72" data-rw-transcript-version="2">
 review, there's also a security review;
 </span>
 <span data-rw-start="591.32" data-rw-transcript-version="2">
 there's also data audits; there are also
 </span>
 <span data-rw-start="593.12" data-rw-transcript-version="2">
 QA. So, we'll give them a path to the
 </span>
 <span data-rw-start="595.52" data-rw-transcript-version="2">
 skills that we have, and make sure that
 </span>
 <span data-rw-start="597.96" data-rw-transcript-version="2">
 Not only following the constraints, but
 </span>
 <span data-rw-start="599.32" data-rw-transcript-version="2">
 also calling the right skills to act on
 </span>
 <span data-rw-start="601.08" data-rw-transcript-version="2">
 it, right? So, you can see the
 </span>
 <span data-rw-start="602.44" data-rw-transcript-version="2">
 possibility here is endless, and you can
 </span>
 <span data-rw-start="604.04" data-rw-transcript-version="2">
 just pick the skill that you want, and
 </span>
 <span data-rw-start="605.64" data-rw-transcript-version="2">
 just add it into your Claude MD file, and
 </span>
 <span data-rw-start="607.52" data-rw-transcript-version="2">
 Claude knows exactly what skill it's
 </span>
 <span data-rw-start="608.8" data-rw-transcript-version="2">
 going to trigger based on your
 </span>
 <span data-rw-start="609.8" data-rw-transcript-version="2">
 preference. Okay, so, pretty much that's
 </span>
 <span data-rw-start="611.72" data-rw-transcript-version="2">
 it for this video. And honestly, I don't
 </span>
 <span data-rw-start="613.48" data-rw-transcript-version="2">
 want to have my Claude MD file here to
 </span>
 <span data-rw-start="615.24" data-rw-transcript-version="2">
 be too long, so I just wanted to keep
 </span>
 <span data-rw-start="617.24" data-rw-transcript-version="2">
 it short. Just keep some skills that I
 </span>
 <span data-rw-start="619.12" data-rw-transcript-version="2">
 really like inside of a Claude MD file.
 </span>
</p>
<p>
 <span data-rw-start="621.24" data-rw-transcript-version="2">
 All right, so, you can see that’s
 </span>
 <span data-rw-start="622.12" data-rw-transcript-version="2">
 exactly the end of our skills. And of
 </span>
 <span data-rw-start="624.24" data-rw-transcript-version="2">
 course, if you’re interested in learning
 </span>
 <span data-rw-start="625.48" data-rw-transcript-version="2">
 more about spectrum development models,
 </span>
 <span data-rw-start="627.2" data-rw-transcript-version="2">
 be sure to check out the playlist here,
 </span>
 <span data-rw-start="629.24" data-rw-transcript-version="2">
 inside the description below, where I
 </span>
 <span data-rw-start="630.96" data-rw-transcript-version="2">
 show you all the spectrum development
 </span>
 <span data-rw-start="632.48" data-rw-transcript-version="2">
 models that I talk about on this channel,
 </span>
 <span data-rw-start="633.76" data-rw-transcript-version="2">
 on how you can be able to make your
 </span>
 <span data-rw-start="635.08" data-rw-transcript-version="2">
 large language model here to be highly
 </span>
 <span data-rw-start="636.64" data-rw-transcript-version="2">
 accurate when performing tasks on your
 </span>
 <span data-rw-start="638.8" data-rw-transcript-version="2">
 Project, right? So, if you’re interested in that, make sure to check it out in
 </span>
 <span data-rw-start="640.68" data-rw-transcript-version="2">
 the link in the description below. With
 </span>
 <span data-rw-start="642.12" data-rw-transcript-version="2">
 that being said, if you do feel my this
 </span>
 <span data-rw-start="644.72" data-rw-transcript-version="2">
 video, please make sure to like this
 </span>
 <span data-rw-start="646" data-rw-transcript-version="2">
 video, consider to subscribe for more
 </span>
 <span data-rw-start="647.76" data-rw-transcript-version="2">
 content like this. With that being said,
 </span>
 <span data-rw-start="649.44" data-rw-transcript-version="2">
 I’ll see you in the next video.
 </span>
</p>