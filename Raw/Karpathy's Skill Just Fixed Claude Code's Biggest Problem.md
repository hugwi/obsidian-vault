---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - context-management
  - skills
source: readwise
created: 2026-06-23
rating: 
action: 
theme: workflow-phases-gates
subtheme:
  - plan-phase
---

# Karpathy's Skill Just Fixed Claude Code's Biggest Problem

![rw-book-cover](https://i.ytimg.com/vi/EsgUfrwsV5A/sddefault.jpg)

## Metadata
- Author: [[Eric Tech]]
- Full Title: Karpathy's Skill Just Fixed Claude Code's Biggest Problem
- Category: #articles
- Summary: Karpathy's skill adds four clear rules to a Claude MD file that help AI think before coding and keep code simple and goal-driven. This stops the AI from making mistakes or changing unrelated code. It also guides the AI to use the right skills for each task, making coding smarter and faster.
- URL: https://www.youtube.com/watch?v=EsgUfrwsV5A

## Full Document
In this video, we're going to go overthis Andrej Karpathy skills, which gotover 100,000 stars on GitHub. And thisskill is derived from this expose thatAndrej Karpathy has wrote. And if youdon't know what Andrej Karpathy is, hewas previously a director of AI at Teslaand a founding team member at OpenAI.Currently, this expose has got over 7million views on X. And essentially,what this skill does is address theproblems that Andrej Karpathy sees on X.And the first problem we see is that themodel here always makes the wrongassumption. So, it doesn't askclarification questions. When you giveit a problem, act on it. And the secondproblem that he sees is that the model hereoften times overcomplicates things.

Things can be written in 100 lines, oftenwritten in 1,000 lines. And often times,large language models here make changesthat they're not supposed to withoutclear understanding of the full sideeffects. So, that's why in this video,We're going to take a look at what itis, how does it work, and how does itdifferent compared to any other skillsthat we have used in the past. So, withthat being said, if you're interested,let's get into the video. Now, before wecontinue, I recently launched our schoolcommunity where I help you to master AIagents, automations, and so much more.

And that's all coming from someone whoused to work as a senior AI softwareengineer at companies like Amazon andMicrosoft. And in this community, you'regoing to get over 100 plus videomaterials like templates and workflowsthat I personally built and sold over100 plus times. On top of that, you'realso going to get access to our weeklylive calls. And just to give you anidea, this week's actually running aClaude call masterclass where we'regoing to dive into how to improve Claudecall's accuracy, and we're going to useit to build applications. Plus,you're also going to get full community.

Supports where you're going to get achance to ask questions and get directanswers back. So, if you're ready tolevel up, make sure you jump right in,and I'll see you in a community. Allright. So, to get started, let's take alook at what this skill is trying tooffer. So, right here you can see thisskill here offers four principles thatwe can use in our project, which willbasically write inside of our Claude MDfile. So, the first principle here you cansee is think before coding. Largelanguage model here, like I said, makeswrong assumptions, doesn't clarifythings. And by having this principle,it's going to force AI here to have tothink before it's going to do theexecution. And the second here issimplicity. Things that can be written in100 lines of code never should be writtenlike 500 or 1,000 lines of code, right?

Never should be complicating things. Andthe success criteria here is that if aComplicated, then we should definitelysimplify. And that's exactly what thisprinciple is trying to solve. And thethird one here is surgical changes. So,let's say we're making changes. Largelanguage models should never touch codethat are not related to the instructionthat we provide. And that's what this principle does. And thelastone that we have is goal-drivenexecutions. We need to have a clear goalon exactly how large language modelshere perform before it's going to do theexecutions. And it's similar to thefirst one, but we need to have a clearsuccess criteria for the expectedbehavior on the end result. And that'sthe four principles that the skill istrying to introduce, and they allare compacted down into a single Claude MDfile that we can add into a project tomake sure that large language model herenever hallucinates when writing code.

Now, to put this into practice, here youcan see it tells exactly how to install.

This. First of all, what we can do hereis that we can install this in Claudeplugins. Simply, we're just going to addthe skill in our marketplace and installit. And the second option that we haveis let's say if you want to install thisnot globally, but in a project level,simply you can just do with this curlcommand here and add this onto your newproject. But if you have an existingproject, you can simply just go torun this command right here, and simplyit's going to write this rule onto yourClaude MD file onto your existingproject. Now, for my case here, I dohave an existing project calledbookzero.ai, where I help businesseshere to manage receipts and transactions

all using AI. And what I want to do hereis I want to install this onto thisproject and see how does it work. Now,in order to install this, all I had todo here is just going to copy thiscommand. It's going to install this onexisting project. So, here I'm justGoing to come over to a projectterminal, open a new terminal, and justgoing to paste that command here. Andwhat this essentially doesis going to modify my Claude MD file bysimply adding those four rules ontothere. So, in this case, I'm going toclick on enter, and you can seethat it's going to modify my cloud MDfile.

So, now if I were to open the Gitdiff, and here you can see this is thechanges that have been applied. And for mostof you guys, you probably already haveyour cloud MD file or your existingproject. And by installing it, it mighthave some contradiction or conflict withyour existing rules. So, what I highlyrecommend you do is basically tellcloud code to basically try to modifyyour cloud MD file. Once you paste that,once you paste those four principles tosee if there's any conflicts,any conflicts, or anything that's notfollowing what you have in your cloud MDfile. Like, try to merge the conflicts.

That you have. And you can see here thatthis is what it recommends. After itpasted from the original car partyskills repository, here's some problemthat I found. For example, we have theduplicate H1 tag for the cloud MD filebecause the cloud MD file already hasthat. And here you can see there's somemeta framing here that really tells ahuman reader what a doc does, but thecloud MD file here doesn't really needthat. It needs the instruction, a clearinstruction on exactly what needs to do.

And we have also removed someredundant stuff that's not reallyrelevant to our cloud MD file. And youcan see, cloud code has also removed thatand made it more concise. So, again,same rule, less to read, so that we canbe able to make our cloud MD file hereshorter. So, now you can see, if Iwere to close this, this is exactly whatit has modified, right? So, you can seewe have our behavior guardrails. That'sgoing to be an H2 tag. And now we haveOur think before coding and simplicity,first, as well as the surgical changesand the goal-driven executions.

So, you can see that all the four principles arestill here, and there's no conflictsbetween what we have above versus whatwe have here. Okay?So, you can seethat’s exactly how this works. Allright. So, now you know exactly how toinstall it, let’s take a look at theclear difference between how they’redifferent compared to all the skillsthat we have mentioned on this channel,like G stack, superpowers, GSD, allthose spectrum development frameworksthat we have introduced. And a cleardifference is this. GSD, superpower, Gstack, they are all skills. They’re allskills that are being triggered wheneverwe trigger them, right? But Claude MDfile is different, is that we enforcethose rules inside of a Claude MD file.

I kind of like personality embedded intothe model's brain. That every time whenit do something, we don't have toMention it. It knows that because it'sembedded into its personality, embeddedinto its soul that it's going to followthese four constraints every time we dosomething. When it asks to do I doanything, like maybe helping us towrite a blog post or helping us togenerate images or helping us to writingcode. It's going to embed that. It'sgoing to do this exactly like wementioned in our Claude MD file. Sothat's the clear difference between thetwo. Now, other than their types, let'stalk about the functionalities, right?

Because these four principles actuallycover a lot of those things that we havementioned previously on this channel forthose skills that we have mentioned likeG stack, superpower, and GSD. How is itdifferent, right? In terms offunctionality. And you can see here thatI asked AI on exactly the difference.And you can see here that rule numbertwo and rule number three here havebeen pointed out by AI that is uniquely.

Different compared to superpower and G stack because none of them has mentionedanything about like adding extra stuffor staying in your lane or they don'treally mention these things aslike the constraints. They both teachhow to work carefully, but they don'tknow how much to do, right? Yourguardrails here, which is, you know, ourClaude MD file here fixes that gap bymentioning these things, right? And wealso have something that's similar towhat we have with superpower and G stackis rule number one and rule number four,which is think before coding and goal

driven, right? That's exactly whatspectrum development does — creatingthe plan before doing executions. Andwhat superpower and G stack do differently is not just a bunch of text setsinside of a Claude MD file, but aframework that we have to first writeour spec, then create a to-do list from the spec,and from the to-do list, create an action.That's exactly what superpowerAnd G stack does is creating a frameworkthat large language model here follow,but it doesn't build into the brain. Butmost of them are very similar, right?

The same rule, the same concept is verysimilar between the two. But that's whymy recommendation, my workflow iscombining all of them, right?Combining the two. Not just showing themthe constraints, but also giving themthe path on exactly which skill totrigger. For example, each of theprinciples that Karpathy has mentioned,like think before coding, like don'tassume, like solve the trade-offbefore writing code, we will give themthe path on exactly what skill totrigger. For example, just a coupleempty files won't cut it. We'regoing to let them basically directthem to trigger the superpower skills.

Like, for example, the superpowerbrainstorming skill for adding newfeatures. Or if it's like bug, error, ortest, like test error, like test failure.

We're going to have them trigger the superpower system debugging skill. Ifit's a multi-step, like three files,we're just going to directly have themtrigger the writing plan skill or theGSD planning phase skill. Basically, tryto execute it really fast, creating ato-do list and trying to execute it, right?And for simplicity, first, there areactually a bunch of skills for simplicity,like making code more simplified, likeminimize the code that solves theproblem, nothing speculative. So, you cansee before committing, polish. So,whenever we try to commit things, okay,well, let's trigger the simplify skilland try to simplify everything. Allright, so pretty much that's it for thisvideo, and all right, so you can seethat's pretty much it for this video.

And if you do find this video, pleasemake sure to like this video, considersubscribing for more content like this.But with that being said, I'll see youin this video. And honestly, I don't evenStop there. You can also include in Gstock, like the auto plan skill, whereyou can have different rules here tointroduce for thinking before coding. Thepossibility here is endless, right?

You can actually add a lot of things inhere. For example, there are also surgicalchanges; you can also add, like, usingdifferent work trees for, you know,breaking it into different environments.

And there are alsogoal-driven executions, right? Makingsure that we're setting a clear goal,right? For the success criteria. Soimplement a feature or a bug fix. Okay,well, let's trigger the test-drivendevelopment here. If it's likeexecuting a written plan, well, let's dothe executing plan, right? So, there areactually a lot of skills that do that.

For example, if we want to conduct a securityreview, there's also a security review;there's also data audits; there are alsoQA. So, we'll give them a path to theskills that we have, and make sure thatNot only following the constraints, butalso calling the right skills to act onit, right? So, you can see thepossibility here is endless, and you canjust pick the skill that you want, andjust add it into your Claude MD file, andClaude knows exactly what skill it'sgoing to trigger based on yourpreference. Okay, so, pretty much that'sit for this video. And honestly, I don'twant to have my Claude MD file here tobe too long, so I just wanted to keepit short. Just keep some skills that Ireally like inside of a Claude MD file.

All right, so, you can see that’sexactly the end of our skills. And ofcourse, if you’re interested in learningmore about spectrum development models,be sure to check out the playlist here,inside the description below, where Ishow you all the spectrum developmentmodels that I talk about on this channel,on how you can be able to make yourlarge language model here to be highlyaccurate when performing tasks on yourProject, right? So, if you’re interested in that, make sure to check it out inthe link in the description below. Withthat being said, if you do feel my thisvideo, please make sure to like thisvideo, consider to subscribe for morecontent like this. With that being said,I’ll see you in the next video.
