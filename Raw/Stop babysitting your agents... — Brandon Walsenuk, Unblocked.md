---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - context-management
  - harness
source: readwise
created: 2026-06-23
rating: 
action: 
theme: context-engineering
subtheme:
  - context-window
  - retrieval-rag
  - compaction-caching
---

# Stop babysitting your agents... — Brandon Walsenuk, Unblocked

![rw-book-cover](https://i.ytimg.com/vi/BiG2ssibKGc/sddefault.jpg?v=6a15437f)

## Metadata
- Author: [[AI Engineer]]
- Full Title: Stop babysitting your agents... — Brandon Walsenuk, Unblocked
- Category: #articles
- Summary: The speaker explains that AI agents need a smart context engine to understand and act without constant help. Simply giving agents access to data is not enough; they need reasoning across information like code and conversations. A good context engine improves agent performance and helps teams work better with AI tools.
- URL: https://www.youtube.com/watch?v=BiG2ssibKGc

## Full Document
Hello, everybody. It's good to see you.I'm Brandon. I work at Unblocked. It's agreat place. Uh, and my goal is to makeit so that you don't have to babysityour agents anymore. Um, I'm sure we allhave a different take on what thatmeans. What I think of is care andfeeding. Basically, agents whenever youspawn it by typing Claude in your CLI.Let's assume whatever tool you may usethey exist, and it’s like a brilliantsoftware engineer has just spawned, andit knows nothing about what it needs todo. It knows nothing about your org.

It’s completely zero context in itshead. So, typically, what happens ispeople have to move through buildingthat context, which we’ll go through inthe beginning. But first, what I’m goingto cover today pretty quickly is threemyths about how you can stop babysittingyour, your agents, and then three lessonsthat we learned the hard way building acontext engine at Unblocked. So, ourproduct basically provides this context.

For agents, and we'll tell you a bitabout how we built that techniques tocare about, and I'll show you a repo weactually constructed at our workshopyesterday that will be open source atthe end of the week, which has onecomponent of what's in a context engine,which you can lift for yourself andbring into your org if you'd like. SoNot long ago, you were the contextengine. If you think about that, whenyou're writing code, you thought abouteverything. You knew everything. Youfigured it all out. You were dealingwith that. And now what's weird isyou're in a weird state where you areactually the context engine for youragents. So, a useful way to think aboutthis is how did you build context whenyou showed up at a company? So, day one,you had probably nothing, but you werereally smart. You finished school, Idon't know, maybe some self-learning.

Then, over time, you accumulate context bydoing stuff at work, meeting market,Meeting your team, being like, "Here's aPR, getting it rejected." All these goodthings built up a lot of yourcapabilities. And then finally, youbecame very good at your job because youasked good questions and you knew how togather accurate context and shred stuffthat wasn't helpful for you.

This is where we're at right now.Most people here, if you look at thebottom, is in the "you are the contextengine" stage because you're eitherdealing with the early phases of AI,which was just fancy autocomplete,or you're in an agentic IDE where you'retriggering every job. What we see withall these businesses that work with usin their AI adoption is it's usually ata varying level of this. This has beenadapted from Basim Eld's work. Um, if youcheck him out later, great engineer. Butbasically, this is the type of ladderthat we're dreaming for. And far on theside is like a dreamy future that maybecodeex figured out. I think I didn't seeRyan's talk, unfortunately, but everyone else is kind of trying to get there.

In order to move through this, you want to get to the curated context layer.That is typically what a lot of teams are doing by creating static repos.So, static stores of a bunch of context that says key things about their company.These can include, of course, cloud MD files, agents MD, that those types of tooling,but usually people start to put a bunch of other key corporate context into an area that agents can access to pull data from.The issue with that is those are static content pieces, of course.So, someone has to maintain and update them, or sorry, update them as well,as they don’t have, uh, the availability of actual raw runtime data.There’s just a bunch of information that engineers obviously need that doesn’t go into these static layers.

that you’re starting to see, which typically look like a file system.Wow, context engine.What this needs to do is basically haveAll that static content, of course, butalso be able to, at runtime, when a querycomes through from the software engineer,typically, how do I implement thisfeature at runtime? It’s able to pull allthat static source across your entirecorporate knowledge corpus, essentially,whether it’s any many SaaS apps, differentsystems or records, and pull in theruntime signals in order to analyze,reason across all those surfaces, allthose different data stores, and then runexhaustively to actually find all of thethings that are important, and then senda token-optimized, aka small, response to

the agent with all the details it needs,to then execute its next steps. Soyou'll see through this, but typically,that means getting the best context upfront, which makes all agent choices andactions after that even better. So,if you give it, for example, a key researchpacket, like, hey, I want to do a newintegration, and if you drop a packet sothat it creates a good plan, then thatInformation says here's our patterns weuse factory pattern. We do these thingslike all the things about yourorganization. It's then able to triggerits background agent jobs to go anddo the things it needs to.

With higher accuracy, which means it'smore token efficient, and it gets the jobdone faster.

This is the problem from our friendKaparthi. The gap is not intelligence atthis point. It is context,though mythos sounds pretty cool. Um, sothe problem is people think that accessis the answer, but it is not.

Understanding is. So, providing your agenttools with MCPs, with pipes to differentsets allows it to access that. But youhave to remember, on day one when youshow up at work, you don't know wherethings are, and you definitely don't knowwhat you don't know. So, there's probablysome service over there you've neverheard of before in your life. You'reworking on a thing, your agent's like,"Oh, I did it. I wrote the whole codefrom scratch." And then your seniorengineer is like, "Hey, bro, we have aservice." And denies you. So, one thingyou'll see is we actually triggered thistask. That's a real prompt. You'll seedata later in this uh slide about theoutcomes. We did it with unblocked acontext engine, and then without one,but it had an MCP access to each SAStool that was required to get the jobdone. And I'll show you the differences.

The short story is you kind of get this.The naive run which just had the MCPaccess basically passed all the codechecks. It compiled but the seniorengineer was like this is totally wrongand what it tried to do would havebroken our entire system if we hadshipped it.So three myths about building context.The first: if I do naive rag over my docs,that is context. Unfortunately, that doesnot work. Naive rag picks a bunch ofthings, and it puts a data store there.

And the agent can then crawl across thatdata store, but it typically falls downbecause there's something known assatisfaction of search. This is a knownphenomenon in radiology, but the shortstory is, if you get an X-ray becauselet's say you have a lung problem, theradiologist will scan, and when they findsomething, they’re like, "Oh, there'ssomething on your lung." They stop lookingbecause they think they found the answerto the symptoms you have told them, andthis is very bad in medical health, ofcourse, because there may be other thingswrong. So, what happens with an agent is,

if you say, "Make a Zenesk integration," itwill go, it might call an MCP, and thefirst piece of data it finds, it goes, "Oh,this must be the pattern." It stopslooking, so the issue is, if it's notexhaustive, it will not find the actualroot cause, or it may not find thecorrect, best way to implement, and just abunch of other problems can happen, andbasically, by the time the agent output,Is done, you read it as an engineer, andgo, no, and then you're in a doom loop,where you're like, let me correct you.

It's actually over here. I'm going topoint a file, and so you're babysitting.

If I just connect enough MCPs, I'm done.I think I've spoken to that. They'rethere. They're pipes. That's great. Butthey don't provide understanding orreasoning across it. And then finally,we did think this for a while. Wedreamed of the 1 million context window.

It's here. I don't know if anyone's everwhacked it full with something, and thentried to get the agent to do anything.

It can't. Um, it basically just can'treason over that much data. It's justnot super helpful. It just sits there.

There's no entities and relationships,and there's all these things that weneed for these agents to be mosteffective. Um, so the bigger contextwindow does not solve it. There's abunch of compute reasons why even if wegot to 100 million in a context window.

It's still not going to help other thanneedle and haystack problems if you'reobviously like fine, fine Waldo.So basically, this is what we see—theclassic waterfall code that compiles iswhat the agent can see. But typically,today, they miss all of this because itcan't see it. It doesn't know if it'sthere. It would have to run for so long,grepping in a session to actually getyour factory patterns or other thingsacross your codebase that you'd burn abajillion tokens, and then when you closethat terminal window, bye-bye. You gotto just do it again. And no one wants torepeat this cost.

So this is why you need a contextengine. It understands who you are andwhat information actually matters. So akey component of this is a social graph,because you use that as a pivot point.Because if I ask how to do the Zeneskintegration, the context engine shouldknow which code bases I work in, wheremy PR history is, who I work with, andWhat I mean when I say that, because at alarge or we deal with companies thathave 20,000 members at our, that arecustomers of ours, it's very different.

So, you need to be able to reason that.And, by the way, a context graph is anincredibly useful technique for buildingthese things. We'll talk about it. Itshould resolve conflicts. I don't knowhow many times I've looked at sourcecode that's running in Maine, and we goyeah, that's the source of truth, butthere's a Slack conversation where theCTO says that was implemented wrong,which is right. A context engine must beable to settle that debate, and by theway, a social graph helps withthat because if you see the CTO sayingin the Slack thread that it's wrong, the CTOis probably right. So, the context enginereasons about that and goes, well, thecode says this, Slack says this, that'sthe CTO. We should probably tell theagent what the CTO said, and of courseprovide the source code, etc.

Passes what's truth. So it handlestruthiness. That's a tough problem. Wehave a lot of techniques in our productto solve it. It is not fully solved. Itshould respect permissions andgovernments. This is pretty basic. It'sone of the reasons this is deliveredover MCP is you can carry the OOTH modelthrough for data governance and a bunchof other reasons that matter in scalingbusinesses. I mean, as soon as you're 20plus, typically this matters becausesome data should not be accessible toothers. So, when you build your engine,

you do not want to put everything inthere, especially when you think aboutwe ingest Slack conversations andMicrosoft Teams convos. So, if it's you,we will return responses from privatechats, but if someone else asks aquestion, we will never show themprivate chats that aren't theirs. That’sjust one easy way to think about it. Andit should deliver the right context, theright model at the right time in a tokenOptimized way. This is how ours works.

So the short is, we ingest a bunch ofdata sources. It sits in our engine. Wehave six key differentiators, which I’llgo into in a sec. And then on the outputside, there should be many surface areaswhere agents and humans are able tointeract with the context engine. One ofours is simple. Human engineers in Slackjust chat with it and ask it questionsall the time to get data they need. I’llshow you an example. Um, but then ofcourse, agents as you move to backgroundagents, they need a context engine inorder to run headlessly or to run in thebackground, or run in the cloud because

they have to be able to ask questions ofa machine, not a person, becauseotherwise, you’re not going to wake up toa PR. You’re going to wake up to an, “Am Iallowed to use this tool?” And that’s nothelpful. So these are the six. We’regoing to move at pace. But the short is,I’ve talked to a lot of these, but theseare kind of marketing terms. UnifiedSystem context. So it should be able toreason across all of your systems ofrecords. It has to be able to dotargeted retrieval.

Conflict resolution, as described there,are many times where the docs and this,and that are conflicting. So how do yousettle that? That data governanceproblem. So, secure access model,personalized relevance, building socialgraphs, knowing who you are, who youwork with. And finally, of course, tokenoptimization. This is becoming a prettybig issue. A lot of benefits you get ontoken optimization is just by having acontext engine because you don't rerunthose GPS for the agent to know. Butalso, with an engine, if you reasonacross everything, it's then able tocompress the response into exactly whatthe agent needs and only send that backas an answer.That task I talked about, I'm not goingto lie, we asked Claude to do thecomparison, so it made these bar charts.

And numbers, but it did pull out all thekey points of this. That same prompt,one was naive. It had all the MCPS itneeded to get the data, and the other hadour context engine only. This is thedifference across key principles ofengineering. But these are funny. Itlike didn't catch that we use bedrock asa fallback. It shipped like bugs.There was one that broke the customcallers. The short story is if you'reworking at any form of scale, again 20plus agents are just going to try tomock things, and it'll look likea prototype. It's not mergeable. If youget a context engine. When I put up thisPR, our senior engineer for the one withthe engine basically gave me a nitpick,and was like, "Yep, you can merge this.Just fix that." Great.These are some of our hard lessons.We did try to optimize for access, notunderstand. We like the bottle willhandle this. Like, the agent's totallygoing to figure it out. It'll collapse.

Into mythos or whatever. It hasn't.It's been years, so we were like, "Wehave to solve this problem another way."And I think that's correct, based onactually, Anthropics launched last nightwith cloud agents, and Ryan's talk thismorning. You have to get context intothe harness, and an engine is the way todo that. We hid conflicts instead ofservicing them. The agent would actuallyjust pick when we found conflicts atfirst because we like it can't be thatbad. It's that bad. So, solving conflicts is an important problem.

And then finally, this is a really fun one.We thought as good answers happened, weactually got feedback loops on those. Sowe were caching them for latency. If youcache a good answer, basically it's likewhen you write docs, right? The momentyou write it, it's no longer validbecause things are changing. So, if youcache a correct answer, and then tomorrowsomeone asks the same question, and youanswer it, you probably lied to them.

Now, because things probably changed in a24-hour clock,so the system is not thesame. Obviously, some questions I'm sureare stable, but this led to a lot ofproblems.So I highly recommend againsteven if it's optimized.This is where AI forward teams are.They're using context engines in all ofthese cases. So I know we're allengineers, but I’m sure that we supportothers in our orgs, like a askengineering channel. Our context enginesits in every customer’s ask,the engineering channel. It detects if aquestion is asked, it scores confidently,and then it responds automatically. Sowhen support teams, sales teams, whoeveris like, hey, what's running in prod?

What's this? The context engine justanswers them and deals with the issue,just like it would answer an agent asking for data.Um, so there are many ways, like that use case I just talkedabout, but then ticket enrichment,triage, incident management, obviously.

Working with your agents and coding.These are all great ways that you gettons of leverage out of getting one ofthese into place.Teams then customize them. So most fork,we have like a cookbook. They take thatrepo, the cookbooks full of skills. Um,but then you devise your skills withyour standard operating procedures. Youobviously can build your own workflows,whether you do that as a skill or someother technique. And then, of course,custom agents. All of these can leveragethat same context engine. So you justget a huge amount of leverage.

This is what I'm trying to leave youwith. An agent should write code thatfeels like it was written by someonewho's been on your team for years. Likethat's just like we should expect thatby now. And this is one of thosetechniques to get you there.

I can do a brief QA and I can give ademo. I have three minutes left. Sowhat's your preference? Demo.

>> Cool. So this is the tool I talked aboutat the workshop. We're going to opensource it. This is one component of akey of a social graph. And sowhen you run it, this will be available.I think it's Monday. We're going toactually open source. Currently, it's closed source.There’s a whole setup, but we had abunch of teams hack against it and shipcode. But basically, it will build youone of these. Uh, I’m going to zoom in.

This is our engineering or, as you cansee, there’s different nodes and edges.It's a basic graph, but it's a socialgraph. Rasheen is a goddamn machine. Sothat's how much he ships, which is indicated by thesize of the node. If you go look at this,it’s algorithmically procedurally generated.So, you’ll see the tool, but in short, youcan see on the right who he's workingwith. Sorry, the screen is like kind ofsmall.

Great. Kind of worked. Uh, so you can seewho he works with, whose code he reviews,what area he worked in.

Labeling with an API key from Enthropic.Oh god, now it looks terrible. Let's zoomin a little better. Um, sorry, it's a funtool, but basically this expert graphwould allow you to, when a query comesacross, we go, "Oh, you're Rashine. Youwork with these people." Great. It'llpivot on that data. It'll then zoom intothe code bases that he's dealing with.

So, when you as an engineer ask maybenot the best prompt of all time, butyou're like, "Hey, I got to get thisdone. There's a bug. Got to fix it."It'll know who you are. It'll pivot onthat. It'll probably find the bug that'slike correct. And again, it'll use thiscomponent to do a bunch of things andmake decisions as it traverses in orderto reason to give the agent the exactanswer that it needs. So this, this toollike generates this for you. You justpoint it at your code repo. It'll do aconstruction. Um, but it does things likecreates experts across like various

Areas in the business. So, in our libs,our services, I'm quick scrolling,apologies, we got time. You can check aheat map of who works with eachother, like who reviews what, whoauthors what. You can check peer tables,you know, who Andre works with, etc. So,this data is available in a context engine,very useful. And again, this will beopen source. Uh, if I think you got abadge scan, I'll just email you allas soon as it's open source. That'scool.

Another quick demo. Ghosty, my boy. So,in this one, I actually used our MCP, andI just straight up said, how do I make anew first class integration to Zenesk?I just said, use the MCP. It wouldprobably have picked it up, but I wantto make sure for this demo that it did.It ran, it chose to use our research tasktool. You can see that it constructed aquery. So, the agent did that based onthe shape of our MCP. So, it wrote theright query, ran that. It did effort.

High for reasoning. It got the databack. Then it triggered its exploreagents. This is key because now they'reexploring the right place after thisresearch packet came in. Great researchresults. Did the thing, did the thing,wrote me a plan. So if you look at thisplan, you do not know my source. That'sfair. But if we just scan it, like itfound all the things that matter likeregistering our provider, obviously wehave a factory pattern. Um, I'll justpull through, but like the librarymodules, client, like this is like onehell of a plan is the short story. Andit's like pretty correct. I wouldprobably prompt this a couple more timesto get it totally right, but at any timewhile it's executing, it's able to keepcalling our MCP. So typically what wesee is use the engine for planning, runexecution,and then basically as you get to codereview, leverage your engine againbecause that engine is very good at code.

Review, and it's extremely good atplanning.That's all the time I have, so thank you all very much.I appreciate it. Uh, I'mat a booth at G16, so come by if youhave questions.
