---
title: "Stop babysitting your agents... — Brandon Walsenuk, Unblocked"
source: "https://www.youtube.com/watch?v=BiG2ssibKGc"
author: "AI Engineer"
published: 2026-05-26
created: 2026-05-26
description: "Same prompt. Same agent. Same model. Without a context engine: 2.5 hours,"
tags:
  - to-process
  - orchestration
---

Hello everybody. It's good to see you. I'm Brandon. I work at Unblocked. It's a great place. Uh and my goal is to make it so that you don't have to babysit your agents anymore. Um I'm sure we all have a different take on what that means. What I think of is care and feeding. Basically agents whenever you spawn it by typing claude in your CLI 

let's assume whatever tool you may use they exist and it's like a brilliant software engineer has just spawned and it knows nothing about what it needs to do. It knows nothing about your org. It's completely zero context in its head. So typically what happens is people have to move through building that context which we'll go through in the beginning. But first, what I'm going to cover today pretty quickly is three myths about how you can stop babysitting your your agents and then three lessons that we learned the hard way building a context engine at unblocked. So our 

product basically provides this context for agents and we'll tell you a bit about how we built that techniques to care about and I'll show you a repo we actually constructed at our workshop yesterday that will be open source at the end of the week uh which has one component of what's in a context engine which you can lift for yourself and bring into your org if you'd like. So not long ago, you were the context engine. If you think about that, when you're writing code, you thought about everything. You knew everything. You figured it all out. You were dealing with that. And now what's weird is 

you're in a weird state where you are actually the context engine for your agents. So a useful way to think about this is how did you build context when you showed up at a company? So day one, you had probably nothing, but you were really smart. You finished school, I don't know, maybe some self-learning. Then over time you accumulate context by doing stuff at work, meeting market, meeting your team, being like, "Here's a PR, getting it rejected." All these good things built up a lot of your capabilities. And then finally, you became very good at your job because you asked good questions and you knew how to 

gather accurate context and shred stuff that wasn't helpful for you. This is where we're at right now. Most people here if you look at the bottom is in the you are the context engine stage because you're either dealing with the early phases of AI which was just fancy autocomplete or you're in an agentic IDE where you're triggering every job. What we see with all these businesses that work with us in their AI adoption is it's usually at a varying level of this. This has been adapted from Basim Eld's work. um if you 

check him out later, great engineer. But basically, this is the type of ladder that we're dreaming for. And far on the side is like a dreamy future that maybe codeex figured out. I think I didn't see Ryan's talk, unfortunately, but everyone else is kind of trying to get there. In order to move through this, you want to get to the curated context layer. That is typically what a lot of teams are doing by creating static repos. So, static stores of a bunch of context that says key things about their company. These can include of course cloud MD files, agents MD, that those types of 

tooling, but usually people start to put a bunch of other key corporate context into an area that agents can access to pull data from. The issue with that is those are static content pieces of course. So someone has to maintain and up them or sorry update them as well as they don't have uh the availability of you know actual raw runtime data. There's just a bunch of information that engineers obviously need that don't go into these static layers that you're starting to see which typically look like a file system. Wow. Context engine. What this needs to do is basically have 

all that static content of course but also be able to at runtime when a query comes through from the software engineer typically how do I implement this feature at runtime it's able to pull all that static source across your entire corporate knowledge corpus essentially whether it's any many SAS apps different systems or records and pull in the runtime singles in order to analyze reason across all those surfaces all those different data stores and then run exhaustively to actually find all of the things that are important and then send 

a token optimized aka small response to the agent with all the details it needs to then execute its next steps. So you'll see through this but typically that means getting the best context up front makes all agent choices and actions after that even better. So if you give it for example a key research packet of like hey I want to do a new integration and it you drop a packet so that it creates a good plan and that information says here's our patterns we use factory pattern we do these things like all the things about your organization it's then able to trigger 

its background agent jobs to go gp your codebase to do the things it needs to with higher accuracy which means it's more token efficient and it gets the job done faster. This is the problem from our our friend Kaparthi. The gap is not intelligence at this point. It is context though mythos sounds pretty cool. Um so the problem is people think that access is the answer but it is not understanding. So providing your agent tools with MCPs with pipes to different 

sets allows it to access that. But you have to remember you day one when you showed up at work you don't know where things are and you definitely don't know what you don't know. So there's probably some service over there you've never heard of before in your life. You're working on a thing, your agent's like, "Oh, I did it. I wrote the whole code from scratch." And then your senior engineer is like, "Hey, bro, we have a service." And denies you. So, one thing you'll see is we actually triggered this task. That's a real prompt. You'll see 

data later in this uh slide about the outcomes. We did it with unblocked a context engine, and then without one, but it had an MCP access to each SAS tool that was required to get the job done. And I'll show you the differences. The short story is you kind of get this. The naive run which just had the MCP access basically passed all the code checks. It compiled but the senior engineer was like this is totally wrong and what it tried to do would have broken our entire system if we had shipped it. So three myths about building context. 

The first if I do naive rag over my docs that is context. Unfortunately that does not work. Naive rag picks a bunch of things. is it puts a data store there and the agent can then crawl across that data store but it typically falls down because there's something known as satisfaction of search. This is a known phenomenon in radiology but the short story is if you get an X-ray because let's say you have a lung problem the radiologist will scan and when they find something they're like oh there's something on your lung they stop looking 

because they think they found the answer to the symptoms you have told them and this is very bad in medical health of course because there may be other things wrong. So what happens with an agent is if you say make a zenesk integration it will go it might call an MCP and the first piece of data it finds it goes oh this this must be the pattern it stops looking so the issue is if it's not exhaustive it will not find the actual root cause or it may not find the correct best way to implement and just a bunch of other problems can happen and basically by the time the agent output is done you read it as an engineer and 

go no and then you're in a doom loop where you're like let me correct you it's actually over here I'm going to point a file and so you're babysitting If I just connect enough MCPs, I'm done. I think I've spoken to that. They're there. They're pipes. That's great. But they don't provide understanding or reasoning across it. And then finally, we did think this for a while. We dreamed of the 1 million context window. It's here. I don't know if anyone's ever whacked it full with something and then tried to get the agent to do anything. It can't. Um, it basically just can't 

reason over that much data. It's just not super helpful. It just sits there. there's no entities and relationships and there's all these things that we need for these agents to be most effective. Um, so the bigger context window does not solve it. There's a bunch of compute reasons why even if we got to 100 million in a context window, it's still not going to help other than needle and haystack problems if you're obviously like fine fine waldo. So basically this is what we see the classic waterfall code that compiles is what the agent can see. But typically today, they miss all of this because it 

can't see it. It doesn't know if it's there. It would have to run for so long grepping in a session to actually get your factory patterns or other things across your codebase that you'd burn a bajillion tokens and then when you close that terminal window, bye-bye. You got to just do it again. And no one wants to repeat this cost. So this is why you need a context engine. It understands who you are and what information actually matters. So a key component of this is a social graph because you use that as a pivot point 

because if I ask how to do the Zenesk integration, the context engine should know which code bases I work in, where my PR history is, who I work with, and what I mean when I say that because at a large or we deal with companies that have 20,000 members at our that are customers of ours, it's very different. So you need to be able to reason that. And by the way, a context graph is an incredibly useful technique for building these things. We'll talk about it. It should resolve conflicts. I don't know how many times I've looked at source code that's running in Maine and we go yeah that's the source of truth but 

there's a Slack conversation where the CTO says that was implemented wrong which is right a context engine must be able to settle that debate and by the way a a graph of social graph helps with that because if you see the CTO saying in the Slack thread that's wrong the CTO is probably right. So the context engine reasons about that and goes well the code says this, Slack says this, that's the CTO. We should probably tell the agent what the CTO said and of course provided the source code etc. So it passes what's truth. So it handles 

truthiness. That's a tough problem. We have a lot of techniques in our product to solve it. It is not fully solved. It should respect permissions and governments. This is pretty basic. It's one of the reasons this is delivered over MCP is you can carry the OOTH model through for data governance and a bunch of other reasons that matter in scaling businesses. I mean, as soon as you're 20 plus, typically this matters because some data should not be accessible to others. So, when you build your engine, you do not want to put everything in there, especially when you think about we ingest Slack conversations and Microsoft Teams convos. So, if it's you, 

we will return responses from private chats, but if someone else asks a question, we will never show them private chats that aren't theirs. That's just one easy way to think about it. And it should deliver the right context, the right model at the right time in a token optimized way. This is how ours works. So the short is we ingest a bunch of data sources. It sits in our engine. We have six key differentiators which I'll go into in a sec. And then on the output side, there should be many surface areas where agents and humans are able to 

interact with the context engine. One of ours is simple. Human engineers in Slack just chat with it and ask it questions all the time to get data they need. I'll show you an example. Um, but then of course agents as you move to background agents, they need a context engine in order to run headlessly or to run in the background or run in the cloud because they have to be able to ask questions of a machine, not a person because otherwise you're not going to wake up to a PR. You're going to wake up to a am I allowed to use this tool? And that's not helpful. So these are the six. We're going to move at pace. But the short is 

I've talked to a lot of these, but these are kind of marketing terms. Unified system context. So it should be able to reason across all of your systems of records. It has to be able to do targeted retrieval. Conflict resolution as described there are many times where the docs and this and that are conflicting. So how do you settle that? That data governance problem. So secure access model, personalized relevance, building social graphs, knowing who you are, who you work with. And finally, of course, token optimization. This is becoming a pretty big issue. A lot of benefits you get on token optimization is just by having a 

context engine because you don't rerun those GPS for the agent to know. But also with an engine, if you reason across everything, it's then able to compress the response into exactly what the agent needs and only send that back as an answer. That task I talked about, I'm not going to lie, we asked Claude to do the comparison, so it made these bar charts and numbers, but it did pull out all the key points of this. That same prompt, one was naive. It had all the MCPS it needed to get the data and the other had 

our context engine only. This is the difference across key principles of engineering. But these are funny. It like didn't catch that we use bedrock as a a fallback. It shipped like bugs. There was one that broke the custom callers. The short story is if you're working at any form of scale again 20 plus agents are just going to try to mock things and it'll look like prototype. It's not mergeable. if you get a context engine. When I put up this PR, our senior engineer for the one with the engine basically gave me a nitpick 

and was like, "Yep, you can merge this. Just just fix that." Great. These are some of our hard lessons. We did try to optimize for access, not understand. We like the bottle will handle this. Like the agent's totally going to figure it out. It'll collapse into mythos or whatever. It it hasn't. It's been years. So, we were like, "We have to solve this problem another way." And I think that's correct based on actually Anthropics launched last night with cloud agents and Ryan's talk this morning. You have to get context into the harness and an engine is the way to do that. We hid conflicts instead of servicing them. The agent would actually 

just pick when we found conflicts at first because we like it can't be that bad. It's that bad. So solving solving conflicts is an important problem. And then finally, this is a really fun one. We thought as good answers happened, we actually got feedback loops on those. So we were caching them for latency. If you cache a good answer, basically it's like when you write docs, right? The moment you write it, it's no longer valid because things are changing. So if you cache a correct answer and then tomorrow someone asks the same question and you answer it, you you probably lied to them now because things probably changed in a 

24-hour clock. So the system is not the same. Obviously, some questions I'm sure are stable, but this led to a lot of problems. So I highly recommend against even if it's optimized. This is where AI forward teams are. They're using context engines in all of these cases. So I know we're all engineers, but I'm sure that we support others in our orgs like a ask engineering channel. Our context engine is sits in every customer's ask engineering channel. It detects if a question is asked, it scores confidently 

and then it responds automatically. So when support teams, sales teams, whoever is like, hey, what's running in prod? What's this? The context engine just answers them and deals with the issue just like it would answer an agent asking for data. Um, so there's a lot of ways like that use case I just talked about, but then ticket enrichment, triage, incident management, obviously working with your agents and coding. These are all great ways that you get tons of leverage out of getting one of these into place. Teams then customize them. So most fork, 

we have like a cookbook. They take that repo, the cookbooks full of skills. Um, but then you devise your skills with your standard operating procedures. You obviously can build your own workflows, whether you do that as a skill or some other technique. And then of course custom agents. All of these can leverage that same context engine. So you just get a huge amount of leverage. This is what I'm trying to leave you with. An agent should write code that feels like it was written by someone who's been on your team for years. Like that's just like we should expect that by now. And this is one of those techniques to get you there. 

I can do a brief QA and I can give a demo. I have three minutes left. So what's your preference? Demo. >> Cool. So this is the tool I talked about at the workshop. We're going to open source it. This is one component of a key of a social graph. And so when you run it, this will be available. I think it's Monday. We're going to actually open source closed source right now. There's a whole setup, but we had a bunch of teams hack against it and ship code. But basically, it will build you one of these. Uh I'm going to zoom in. 

This is our engineering or as you can see there's different nodes and edge. It's a basic graph, but it's a social graph. Rasheen is a goddamn machine. So he that's how much he ships is by the size of the node. If you go look at this is algorithmic procedurally generated. So you'll see the tool but in short you can see on the right who he's working with. Sorry the screen is like kind of small. Great. Kind of worked. Um so you can see who he works with whose code he reviews what area uh he worked in. We use labeling with an API key from Enthropic. Oh god now it looks terrible. Let's zoom 

in a little better. Um, sorry, it's a fun tool, but basically this expert graph would allow you to when a query comes across, we go, "Oh, you're Rashine. You work with these people." Great. It'll pivot on that data. It'll then zoom into the code bases that he's dealing with. So, when you as an engineer ask maybe not the best prompt of all time, but you're like, "Hey, I got to get this done. There's a bug. Got to fix it." It'll know who you are. It'll pivot on that. It'll probably find the bug that's like correct. And again, it'll use this 

component to do a bunch of things and make decisions as it traverses in order to reason to give the agent the exact answer that it needs. So this this tool like generates this for you. You just point it at your code repo. It'll do a construction. Um but it does things like creates experts across like various areas in the business. So in our libs, our services, I'm quick scrolling, apologies, we got time. You can check a heat map gr of who works with each other, like who reviews what, who authors what. You can check peer tables, you know, who Andre works with, etc. So, 

this data available in a context engine, very useful. And again, this will be open source. Uh, if I think you got a badge scan, I'll I'll just email you all as soon as it's open source. That's cool. Another quick demo. Ghosty, my boy. So, in this one, I actually used our MCP and I just straight up said, how do I make a new first class integration to Zenesk? I just said, use the MCP. it would probably have picked it up, but I want to make sure for this demo that it did. It ran it chose to use our research task 

tool. You can see that it constructed a query. So the agent did that based on the shape of our MCP. So it wrote the right query, ran that. It did effort high for reasoning. It got the data back. Then it triggered its explore agents. This is key because now they're exploring the right place after this research packet came in. Great research results. Did the thing, did the thing, wrote me a plan. So if you look at this plan, you do not know my source. That's fair. But if we just scan it, like it found all the things that matter like registering our provider, obviously we have a factory pattern. Um, I'll just 

pull through, but like the library modules, client, like this is like one hell of a plan is the short story. And it's like pretty correct. I would probably prompt this a couple more times to get it totally right, but at any time while it's executing, it's able to keep calling our MCP. So typically what we see is use the engine for planning, run execution, and then basically as you get to code review, leverage your engine again because that engine is very good at code review and it's extremely good at planning. That's all the time I have. So thank you 

all very much. I appreciate it. Uh I'm at a booth at G16, so come by if you have questions. 

<p>
 <span data-rw-start="15.28" data-rw-transcript-version="2">
 Hello, everybody. It's good to see you.
 </span>
 <span data-rw-start="18.08" data-rw-transcript-version="2">
 I'm Brandon. I work at Unblocked. It's a
 </span>
 <span data-rw-start="20.24" data-rw-transcript-version="2">
 great place. Uh, and my goal is to make
 </span>
 <span data-rw-start="21.92" data-rw-transcript-version="2">
 it so that you don't have to babysit
 </span>
 <span data-rw-start="23.199" data-rw-transcript-version="2">
 your agents anymore. Um, I'm sure we all
 </span>
 <span data-rw-start="25.279" data-rw-transcript-version="2">
 have a different take on what that
 </span>
 <span data-rw-start="26.24" data-rw-transcript-version="2">
 means. What I think of is care and
 </span>
 <span data-rw-start="27.68" data-rw-transcript-version="2">
 feeding. Basically, agents whenever you
 </span>
 <span data-rw-start="29.92" data-rw-transcript-version="2">
 spawn it by typing Claude in your CLI.
 </span>
 <span data-rw-start="32.239" data-rw-transcript-version="2">
 Let's assume whatever tool you may use
 </span>
 <span data-rw-start="34.32" data-rw-transcript-version="2">
 they exist, and it’s like a brilliant
 </span>
 <span data-rw-start="36.399" data-rw-transcript-version="2">
 software engineer has just spawned, and
 </span>
 <span data-rw-start="38.239" data-rw-transcript-version="2">
 it knows nothing about what it needs to
 </span>
 <span data-rw-start="39.84" data-rw-transcript-version="2">
 do. It knows nothing about your org.
 </span>
</p>
<p>
 <span data-rw-start="41.6" data-rw-transcript-version="2">
 It’s completely zero context in its
 </span>
 <span data-rw-start="43.6" data-rw-transcript-version="2">
 head. So, typically, what happens is
 </span>
 <span data-rw-start="46.32" data-rw-transcript-version="2">
 people have to move through building
 </span>
 <span data-rw-start="48.16" data-rw-transcript-version="2">
 that context, which we’ll go through in
 </span>
 <span data-rw-start="49.6" data-rw-transcript-version="2">
 the beginning. But first, what I’m going
 </span>
 <span data-rw-start="50.96" data-rw-transcript-version="2">
 to cover today pretty quickly is three
 </span>
 <span data-rw-start="52.879" data-rw-transcript-version="2">
 myths about how you can stop babysitting
 </span>
 <span data-rw-start="55.92" data-rw-transcript-version="2">
 your, your agents, and then three lessons
 </span>
 <span data-rw-start="58.399" data-rw-transcript-version="2">
 that we learned the hard way building a
 </span>
 <span data-rw-start="59.92" data-rw-transcript-version="2">
 context engine at Unblocked. So, our
 </span>
 <span data-rw-start="62.239" data-rw-transcript-version="2">
 product basically provides this context.
 </span>
</p>
<p>
 <span data-rw-start="64.239" data-rw-transcript-version="2">
 For agents, and we'll tell you a bit
 </span>
 <span data-rw-start="66.08" data-rw-transcript-version="2">
 about how we built that techniques to
 </span>
 <span data-rw-start="67.92" data-rw-transcript-version="2">
 care about, and I'll show you a repo we
 </span>
 <span data-rw-start="69.68" data-rw-transcript-version="2">
 actually constructed at our workshop
 </span>
 <span data-rw-start="71.04" data-rw-transcript-version="2">
 yesterday that will be open source at
 </span>
 <span data-rw-start="72.64" data-rw-transcript-version="2">
 the end of the week, which has one
 </span>
 <span data-rw-start="74.08" data-rw-transcript-version="2">
 component of what's in a context engine,
 </span>
 <span data-rw-start="76.56" data-rw-transcript-version="2">
 which you can lift for yourself and
 </span>
 <span data-rw-start="77.68" data-rw-transcript-version="2">
 bring into your org if you'd like. So
 </span>
 <span data-rw-start="80.4" data-rw-transcript-version="2">
 Not long ago, you were the context
 </span>
 <span data-rw-start="82.96" data-rw-transcript-version="2">
 engine. If you think about that, when
 </span>
 <span data-rw-start="84.64" data-rw-transcript-version="2">
 you're writing code, you thought about
 </span>
 <span data-rw-start="86.4" data-rw-transcript-version="2">
 everything. You knew everything. You
 </span>
 <span data-rw-start="87.439" data-rw-transcript-version="2">
 figured it all out. You were dealing
 </span>
 <span data-rw-start="88.96" data-rw-transcript-version="2">
 with that. And now what's weird is
 </span>
 <span data-rw-start="90.479" data-rw-transcript-version="2">
 you're in a weird state where you are
 </span>
 <span data-rw-start="92.32" data-rw-transcript-version="2">
 actually the context engine for your
 </span>
 <span data-rw-start="94.079" data-rw-transcript-version="2">
 agents. So, a useful way to think about
 </span>
 <span data-rw-start="96.079" data-rw-transcript-version="2">
 this is how did you build context when
 </span>
 <span data-rw-start="98.159" data-rw-transcript-version="2">
 you showed up at a company? So, day one,
 </span>
 <span data-rw-start="101.36" data-rw-transcript-version="2">
 you had probably nothing, but you were
 </span>
 <span data-rw-start="102.88" data-rw-transcript-version="2">
 really smart. You finished school, I
 </span>
 <span data-rw-start="103.92" data-rw-transcript-version="2">
 don't know, maybe some self-learning.
 </span>
</p>
<p>
 <span data-rw-start="105.92" data-rw-transcript-version="2">
 Then, over time, you accumulate context by
 </span>
 <span data-rw-start="108" data-rw-transcript-version="2">
 doing stuff at work, meeting market,
 </span>
 <span data-rw-start="111.119" data-rw-transcript-version="2">
 Meeting your team, being like, "Here's a
 </span>
 <span data-rw-start="112.399" data-rw-transcript-version="2">
 PR, getting it rejected." All these good
 </span>
 <span data-rw-start="114.24" data-rw-transcript-version="2">
 things built up a lot of your
 </span>
 <span data-rw-start="115.36" data-rw-transcript-version="2">
 capabilities. And then finally, you
 </span>
 <span data-rw-start="117.6" data-rw-transcript-version="2">
 became very good at your job because you
 </span>
 <span data-rw-start="119.439" data-rw-transcript-version="2">
 asked good questions and you knew how to
 </span>
 <span data-rw-start="121.439" data-rw-transcript-version="2">
 gather accurate context and shred stuff
 </span>
 <span data-rw-start="123.52" data-rw-transcript-version="2">
 that wasn't helpful for you.
 </span>
</p>
<p>
 <span data-rw-start="127.119" data-rw-transcript-version="2">
 This is where we're at right now.
 </span>
 <span data-rw-start="130" data-rw-transcript-version="2">
 Most people here, if you look at the
 </span>
 <span data-rw-start="131.76" data-rw-transcript-version="2">
 bottom, is in the "you are the context
 </span>
 <span data-rw-start="133.68" data-rw-transcript-version="2">
 engine" stage because you're either
 </span>
 <span data-rw-start="135.28" data-rw-transcript-version="2">
 dealing with the early phases of AI,
 </span>
 <span data-rw-start="137.2" data-rw-transcript-version="2">
 which was just fancy autocomplete,
 </span>
 <span data-rw-start="139.68" data-rw-transcript-version="2">
 or you're in an agentic IDE where you're
 </span>
 <span data-rw-start="141.52" data-rw-transcript-version="2">
 triggering every job. What we see with
 </span>
 <span data-rw-start="143.52" data-rw-transcript-version="2">
 all these businesses that work with us
 </span>
 <span data-rw-start="144.879" data-rw-transcript-version="2">
 in their AI adoption is it's usually at
 </span>
 <span data-rw-start="146.48" data-rw-transcript-version="2">
 a varying level of this. This has been
 </span>
 <span data-rw-start="148.239" data-rw-transcript-version="2">
 adapted from Basim Eld's work. Um, if you
 </span>
 <span data-rw-start="150.72" data-rw-transcript-version="2">
 check him out later, great engineer. But
 </span>
 <span data-rw-start="152.72" data-rw-transcript-version="2">
 basically, this is the type of ladder
 </span>
 <span data-rw-start="154.08" data-rw-transcript-version="2">
 that we're dreaming for. And far on the
 </span>
 <span data-rw-start="156" data-rw-transcript-version="2">
 side is like a dreamy future that maybe
 </span>
 <span data-rw-start="158.8" data-rw-transcript-version="2">
 codeex figured out. I think I didn't see
 </span>
 <span data-rw-start="160.56" data-rw-transcript-version="2">
 Ryan's talk, unfortunately, but everyone else is kind of trying to get there.
 </span>
</p>
<p>
 <span data-rw-start="162.8" data-rw-transcript-version="2">
 In order to move through this, you want to get to the curated context layer.
 </span>
 <span data-rw-start="165.04" data-rw-transcript-version="2">
 That is typically what a lot of teams are doing by creating static repos.
 </span>
 <span data-rw-start="167.04" data-rw-transcript-version="2">
 So, static stores of a bunch of context that says key things about their company.
 </span>
 <span data-rw-start="169.28" data-rw-transcript-version="2">
 These can include, of course, cloud MD files, agents MD, that those types of tooling,
 </span>
 <span data-rw-start="170.64" data-rw-transcript-version="2">
 but usually people start to put a bunch of other key corporate context into an area that agents can access to pull data from.
 </span>
 <span data-rw-start="172.56" data-rw-transcript-version="2">
 The issue with that is those are static content pieces, of course.
 </span>
 <span data-rw-start="174.48" data-rw-transcript-version="2">
 So, someone has to maintain and update them, or sorry, update them as well,
 </span>
 <span data-rw-start="176.48" data-rw-transcript-version="2">
 as they don’t have, uh, the availability of actual raw runtime data.
 </span>
 <span data-rw-start="178.56" data-rw-transcript-version="2">
 There’s just a bunch of information that engineers obviously need that doesn’t go into these static layers.
 </span>
</p>
<p>
 <span data-rw-start="180.48" data-rw-transcript-version="2">
 that you’re starting to see, which typically look like a file system.
 </span>
 <span data-rw-start="182.64" data-rw-transcript-version="2">
 Wow, context engine.
 </span>
 <span data-rw-start="184.319" data-rw-transcript-version="2">
 What this needs to do is basically have
 </span>
 <span data-rw-start="211.12" data-rw-transcript-version="2">
 All that static content, of course, but
 </span>
 <span data-rw-start="212.799" data-rw-transcript-version="2">
 also be able to, at runtime, when a query
 </span>
 <span data-rw-start="214.959" data-rw-transcript-version="2">
 comes through from the software engineer,
 </span>
 <span data-rw-start="217.12" data-rw-transcript-version="2">
 typically, how do I implement this
 </span>
 <span data-rw-start="218.56" data-rw-transcript-version="2">
 feature at runtime? It’s able to pull all
 </span>
 <span data-rw-start="221.04" data-rw-transcript-version="2">
 that static source across your entire
 </span>
 <span data-rw-start="222.72" data-rw-transcript-version="2">
 corporate knowledge corpus, essentially,
 </span>
 <span data-rw-start="225.04" data-rw-transcript-version="2">
 whether it’s any many SaaS apps, different
 </span>
 <span data-rw-start="227.2" data-rw-transcript-version="2">
 systems or records, and pull in the
 </span>
 <span data-rw-start="229.04" data-rw-transcript-version="2">
 runtime signals in order to analyze,
 </span>
 <span data-rw-start="232.239" data-rw-transcript-version="2">
 reason across all those surfaces, all
 </span>
 <span data-rw-start="234.239" data-rw-transcript-version="2">
 those different data stores, and then run
 </span>
 <span data-rw-start="236.64" data-rw-transcript-version="2">
 exhaustively to actually find all of the
 </span>
 <span data-rw-start="238.56" data-rw-transcript-version="2">
 things that are important, and then send
 </span>
 <span data-rw-start="240.4" data-rw-transcript-version="2">
 a token-optimized, aka small, response to
 </span>
</p>
<p>
 <span data-rw-start="243.599" data-rw-transcript-version="2">
 the agent with all the details it needs,
 </span>
 <span data-rw-start="245.76" data-rw-transcript-version="2">
 to then execute its next steps. So
 </span>
 <span data-rw-start="248.319" data-rw-transcript-version="2">
 you'll see through this, but typically,
 </span>
 <span data-rw-start="249.84" data-rw-transcript-version="2">
 that means getting the best context up
 </span>
 <span data-rw-start="252.159" data-rw-transcript-version="2">
 front, which makes all agent choices and
 </span>
 <span data-rw-start="254.64" data-rw-transcript-version="2">
 actions after that even better. So,
 </span>
 <span data-rw-start="257.919" data-rw-transcript-version="2">
 if you give it, for example, a key research
 </span>
 <span data-rw-start="259.6" data-rw-transcript-version="2">
 packet, like, hey, I want to do a new
 </span>
 <span data-rw-start="261.359" data-rw-transcript-version="2">
 integration, and if you drop a packet so
 </span>
 <span data-rw-start="264" data-rw-transcript-version="2">
 that it creates a good plan, then that
 </span>
 <span data-rw-start="265.84" data-rw-transcript-version="2">
 Information says here's our patterns we
 </span>
 <span data-rw-start="267.28" data-rw-transcript-version="2">
 use factory pattern. We do these things
 </span>
 <span data-rw-start="268.88" data-rw-transcript-version="2">
 like all the things about your
 </span>
 <span data-rw-start="269.919" data-rw-transcript-version="2">
 organization. It's then able to trigger
 </span>
 <span data-rw-start="272.4" data-rw-transcript-version="2">
 its background agent jobs to go and
 </span>
 <span data-rw-start="274.56" data-rw-transcript-version="2">
 do the things it needs to.
 </span>
</p>
<p>
 <span data-rw-start="276.16" data-rw-transcript-version="2">
 With higher accuracy, which means it's
 </span>
 <span data-rw-start="278.16" data-rw-transcript-version="2">
 more token efficient, and it gets the job
 </span>
 <span data-rw-start="279.84" data-rw-transcript-version="2">
 done faster.
 </span>
</p>
<p>
 <span data-rw-start="282.72" data-rw-transcript-version="2">
 This is the problem from our friend
 </span>
 <span data-rw-start="284.479" data-rw-transcript-version="2">
 Kaparthi. The gap is not intelligence at
 </span>
 <span data-rw-start="286.479" data-rw-transcript-version="2">
 this point. It is context,
 </span>
 <span data-rw-start="289.199" data-rw-transcript-version="2">
 though mythos sounds pretty cool. Um, so
 </span>
 <span data-rw-start="291.919" data-rw-transcript-version="2">
 the problem is people think that access
 </span>
 <span data-rw-start="294.72" data-rw-transcript-version="2">
 is the answer, but it is not.
 </span>
</p>
<p>
 <span data-rw-start="296.88" data-rw-transcript-version="2">
 Understanding is. So, providing your agent
 </span>
 <span data-rw-start="299.759" data-rw-transcript-version="2">
 tools with MCPs, with pipes to different
 </span>
 <span data-rw-start="302.4" data-rw-transcript-version="2">
 sets allows it to access that. But you
 </span>
 <span data-rw-start="305.199" data-rw-transcript-version="2">
 have to remember, on day one when you
 </span>
 <span data-rw-start="307.12" data-rw-transcript-version="2">
 show up at work, you don't know where
 </span>
 <span data-rw-start="309.28" data-rw-transcript-version="2">
 things are, and you definitely don't know
 </span>
 <span data-rw-start="311.44" data-rw-transcript-version="2">
 what you don't know. So, there's probably
 </span>
 <span data-rw-start="313.199" data-rw-transcript-version="2">
 some service over there you've never
 </span>
 <span data-rw-start="314.639" data-rw-transcript-version="2">
 heard of before in your life. You're
 </span>
 <span data-rw-start="316.479" data-rw-transcript-version="2">
 working on a thing, your agent's like,
 </span>
 <span data-rw-start="318.08" data-rw-transcript-version="2">
 "Oh, I did it. I wrote the whole code
 </span>
 <span data-rw-start="319.759" data-rw-transcript-version="2">
 from scratch." And then your senior
 </span>
 <span data-rw-start="321.039" data-rw-transcript-version="2">
 engineer is like, "Hey, bro, we have a
 </span>
 <span data-rw-start="323.759" data-rw-transcript-version="2">
 service." And denies you. So, one thing
 </span>
 <span data-rw-start="326.639" data-rw-transcript-version="2">
 you'll see is we actually triggered this
 </span>
 <span data-rw-start="328.56" data-rw-transcript-version="2">
 task. That's a real prompt. You'll see
 </span>
 <span data-rw-start="330.479" data-rw-transcript-version="2">
 data later in this uh slide about the
 </span>
 <span data-rw-start="332.639" data-rw-transcript-version="2">
 outcomes. We did it with unblocked a
 </span>
 <span data-rw-start="334.32" data-rw-transcript-version="2">
 context engine, and then without one,
 </span>
 <span data-rw-start="336.08" data-rw-transcript-version="2">
 but it had an MCP access to each SAS
 </span>
 <span data-rw-start="339.12" data-rw-transcript-version="2">
 tool that was required to get the job
 </span>
 <span data-rw-start="340.88" data-rw-transcript-version="2">
 done. And I'll show you the differences.
 </span>
</p>
<p>
 <span data-rw-start="342.639" data-rw-transcript-version="2">
 The short story is you kind of get this.
 </span>
 <span data-rw-start="344.88" data-rw-transcript-version="2">
 The naive run which just had the MCP
 </span>
 <span data-rw-start="347.039" data-rw-transcript-version="2">
 access basically passed all the code
 </span>
 <span data-rw-start="349.6" data-rw-transcript-version="2">
 checks. It compiled but the senior
 </span>
 <span data-rw-start="352" data-rw-transcript-version="2">
 engineer was like this is totally wrong
 </span>
 <span data-rw-start="353.52" data-rw-transcript-version="2">
 and what it tried to do would have
 </span>
 <span data-rw-start="354.639" data-rw-transcript-version="2">
 broken our entire system if we had
 </span>
 <span data-rw-start="356.16" data-rw-transcript-version="2">
 shipped it.
 </span>
 <span data-rw-start="358.16" data-rw-transcript-version="2">
 So three myths about building context.
 </span>
 <span data-rw-start="360.32" data-rw-transcript-version="2">
 The first: if I do naive rag over my docs,
 </span>
 <span data-rw-start="363.52" data-rw-transcript-version="2">
 that is context. Unfortunately, that does
 </span>
 <span data-rw-start="366.56" data-rw-transcript-version="2">
 not work. Naive rag picks a bunch of
 </span>
 <span data-rw-start="368.8" data-rw-transcript-version="2">
 things, and it puts a data store there.
 </span>
</p>
<p>
 <span data-rw-start="370" data-rw-transcript-version="2">
 And the agent can then crawl across that
 </span>
 <span data-rw-start="371.6" data-rw-transcript-version="2">
 data store, but it typically falls down
 </span>
 <span data-rw-start="374.16" data-rw-transcript-version="2">
 because there's something known as
 </span>
 <span data-rw-start="375.28" data-rw-transcript-version="2">
 satisfaction of search. This is a known
 </span>
 <span data-rw-start="377.6" data-rw-transcript-version="2">
 phenomenon in radiology, but the short
 </span>
 <span data-rw-start="379.759" data-rw-transcript-version="2">
 story is, if you get an X-ray because
 </span>
 <span data-rw-start="381.6" data-rw-transcript-version="2">
 let's say you have a lung problem, the
 </span>
 <span data-rw-start="383.84" data-rw-transcript-version="2">
 radiologist will scan, and when they find
 </span>
 <span data-rw-start="386.16" data-rw-transcript-version="2">
 something, they’re like, "Oh, there's
 </span>
 <span data-rw-start="387.44" data-rw-transcript-version="2">
 something on your lung." They stop looking
 </span>
 <span data-rw-start="390.24" data-rw-transcript-version="2">
 because they think they found the answer
 </span>
 <span data-rw-start="391.68" data-rw-transcript-version="2">
 to the symptoms you have told them, and
 </span>
 <span data-rw-start="393.6" data-rw-transcript-version="2">
 this is very bad in medical health, of
 </span>
 <span data-rw-start="395.28" data-rw-transcript-version="2">
 course, because there may be other things
 </span>
 <span data-rw-start="396.72" data-rw-transcript-version="2">
 wrong. So, what happens with an agent is,
 </span>
</p>
<p>
 <span data-rw-start="399.28" data-rw-transcript-version="2">
 if you say, "Make a Zenesk integration," it
 </span>
 <span data-rw-start="401.759" data-rw-transcript-version="2">
 will go, it might call an MCP, and the
 </span>
 <span data-rw-start="404.4" data-rw-transcript-version="2">
 first piece of data it finds, it goes, "Oh,
 </span>
 <span data-rw-start="406.16" data-rw-transcript-version="2">
 this must be the pattern." It stops
 </span>
 <span data-rw-start="408.4" data-rw-transcript-version="2">
 looking, so the issue is, if it's not
 </span>
 <span data-rw-start="411.039" data-rw-transcript-version="2">
 exhaustive, it will not find the actual
 </span>
 <span data-rw-start="412.88" data-rw-transcript-version="2">
 root cause, or it may not find the
 </span>
 <span data-rw-start="414.479" data-rw-transcript-version="2">
 correct, best way to implement, and just a
 </span>
 <span data-rw-start="416.4" data-rw-transcript-version="2">
 bunch of other problems can happen, and
 </span>
 <span data-rw-start="417.84" data-rw-transcript-version="2">
 basically, by the time the agent output,
 </span>
 <span data-rw-start="419.199" data-rw-transcript-version="2">
 Is done, you read it as an engineer, and
 </span>
 <span data-rw-start="420.72" data-rw-transcript-version="2">
 go, no, and then you're in a doom loop,
 </span>
 <span data-rw-start="422.88" data-rw-transcript-version="2">
 where you're like, let me correct you.
 </span>
</p>
<p>
 <span data-rw-start="424.16" data-rw-transcript-version="2">
 It's actually over here. I'm going to
 </span>
 <span data-rw-start="425.52" data-rw-transcript-version="2">
 point a file, and so you're babysitting.
 </span>
</p>
<p>
 <span data-rw-start="428.08" data-rw-transcript-version="2">
 If I just connect enough MCPs, I'm done.
 </span>
 <span data-rw-start="430.479" data-rw-transcript-version="2">
 I think I've spoken to that. They're
 </span>
 <span data-rw-start="432.319" data-rw-transcript-version="2">
 there. They're pipes. That's great. But
 </span>
 <span data-rw-start="434.08" data-rw-transcript-version="2">
 they don't provide understanding or
 </span>
 <span data-rw-start="436" data-rw-transcript-version="2">
 reasoning across it. And then finally,
 </span>
 <span data-rw-start="438.56" data-rw-transcript-version="2">
 we did think this for a while. We
 </span>
 <span data-rw-start="440.16" data-rw-transcript-version="2">
 dreamed of the 1 million context window.
 </span>
</p>
<p>
 <span data-rw-start="442.479" data-rw-transcript-version="2">
 It's here. I don't know if anyone's ever
 </span>
 <span data-rw-start="444.16" data-rw-transcript-version="2">
 whacked it full with something, and then
 </span>
 <span data-rw-start="445.599" data-rw-transcript-version="2">
 tried to get the agent to do anything.
 </span>
</p>
<p>
 <span data-rw-start="447.68" data-rw-transcript-version="2">
 It can't. Um, it basically just can't
 </span>
 <span data-rw-start="450.479" data-rw-transcript-version="2">
 reason over that much data. It's just
 </span>
 <span data-rw-start="452" data-rw-transcript-version="2">
 not super helpful. It just sits there.
 </span>
</p>
<p>
 <span data-rw-start="453.68" data-rw-transcript-version="2">
 There's no entities and relationships,
 </span>
 <span data-rw-start="455.36" data-rw-transcript-version="2">
 and there's all these things that we
 </span>
 <span data-rw-start="456.72" data-rw-transcript-version="2">
 need for these agents to be most
 </span>
 <span data-rw-start="458.479" data-rw-transcript-version="2">
 effective. Um, so the bigger context
 </span>
 <span data-rw-start="460.72" data-rw-transcript-version="2">
 window does not solve it. There's a
 </span>
 <span data-rw-start="462.08" data-rw-transcript-version="2">
 bunch of compute reasons why even if we
 </span>
 <span data-rw-start="463.68" data-rw-transcript-version="2">
 got to 100 million in a context window.
 </span>
</p>
<p>
 <span data-rw-start="466.24" data-rw-transcript-version="2">
 It's still not going to help other than
 </span>
 <span data-rw-start="467.68" data-rw-transcript-version="2">
 needle and haystack problems if you're
 </span>
 <span data-rw-start="469.28" data-rw-transcript-version="2">
 obviously like fine, fine Waldo.
 </span>
 <span data-rw-start="472.96" data-rw-transcript-version="2">
 So basically, this is what we see—the
 </span>
 <span data-rw-start="475.039" data-rw-transcript-version="2">
 classic waterfall code that compiles is
 </span>
 <span data-rw-start="477.039" data-rw-transcript-version="2">
 what the agent can see. But typically,
 </span>
 <span data-rw-start="479.919" data-rw-transcript-version="2">
 today, they miss all of this because it
 </span>
 <span data-rw-start="482.8" data-rw-transcript-version="2">
 can't see it. It doesn't know if it's
 </span>
 <span data-rw-start="484.16" data-rw-transcript-version="2">
 there. It would have to run for so long,
 </span>
 <span data-rw-start="486" data-rw-transcript-version="2">
 grepping in a session to actually get
 </span>
 <span data-rw-start="487.52" data-rw-transcript-version="2">
 your factory patterns or other things
 </span>
 <span data-rw-start="489.039" data-rw-transcript-version="2">
 across your codebase that you'd burn a
 </span>
 <span data-rw-start="490.879" data-rw-transcript-version="2">
 bajillion tokens, and then when you close
 </span>
 <span data-rw-start="492.879" data-rw-transcript-version="2">
 that terminal window, bye-bye. You got
 </span>
 <span data-rw-start="495.52" data-rw-transcript-version="2">
 to just do it again. And no one wants to
 </span>
 <span data-rw-start="497.199" data-rw-transcript-version="2">
 repeat this cost.
 </span>
</p>
<p>
 <span data-rw-start="499.28" data-rw-transcript-version="2">
 So this is why you need a context
 </span>
 <span data-rw-start="500.639" data-rw-transcript-version="2">
 engine. It understands who you are and
 </span>
 <span data-rw-start="504.24" data-rw-transcript-version="2">
 what information actually matters. So a
 </span>
 <span data-rw-start="506.319" data-rw-transcript-version="2">
 key component of this is a social graph,
 </span>
 <span data-rw-start="508.879" data-rw-transcript-version="2">
 because you use that as a pivot point.
 </span>
 <span data-rw-start="510.639" data-rw-transcript-version="2">
 Because if I ask how to do the Zenesk
 </span>
 <span data-rw-start="512.479" data-rw-transcript-version="2">
 integration, the context engine should
 </span>
 <span data-rw-start="514.399" data-rw-transcript-version="2">
 know which code bases I work in, where
 </span>
 <span data-rw-start="516.399" data-rw-transcript-version="2">
 my PR history is, who I work with, and
 </span>
 <span data-rw-start="518.64" data-rw-transcript-version="2">
 What I mean when I say that, because at a
 </span>
 <span data-rw-start="521.519" data-rw-transcript-version="2">
 large or we deal with companies that
 </span>
 <span data-rw-start="523.44" data-rw-transcript-version="2">
 have 20,000 members at our, that are
 </span>
 <span data-rw-start="525.519" data-rw-transcript-version="2">
 customers of ours, it's very different.
 </span>
</p>
<p>
 <span data-rw-start="528.56" data-rw-transcript-version="2">
 So, you need to be able to reason that.
 </span>
 <span data-rw-start="530.32" data-rw-transcript-version="2">
 And, by the way, a context graph is an
 </span>
 <span data-rw-start="532" data-rw-transcript-version="2">
 incredibly useful technique for building
 </span>
 <span data-rw-start="533.279" data-rw-transcript-version="2">
 these things. We'll talk about it. It
 </span>
 <span data-rw-start="535.12" data-rw-transcript-version="2">
 should resolve conflicts. I don't know
 </span>
 <span data-rw-start="537.04" data-rw-transcript-version="2">
 how many times I've looked at source
 </span>
 <span data-rw-start="538.32" data-rw-transcript-version="2">
 code that's running in Maine, and we go
 </span>
 <span data-rw-start="539.92" data-rw-transcript-version="2">
 yeah, that's the source of truth, but
 </span>
 <span data-rw-start="541.36" data-rw-transcript-version="2">
 there's a Slack conversation where the
 </span>
 <span data-rw-start="542.72" data-rw-transcript-version="2">
 CTO says that was implemented wrong,
 </span>
 <span data-rw-start="545.2" data-rw-transcript-version="2">
 which is right. A context engine must be
 </span>
 <span data-rw-start="548.08" data-rw-transcript-version="2">
 able to settle that debate, and by the
 </span>
 <span data-rw-start="550.72" data-rw-transcript-version="2">
 way, a social graph helps with
 </span>
 <span data-rw-start="553.44" data-rw-transcript-version="2">
 that because if you see the CTO saying
 </span>
 <span data-rw-start="555.36" data-rw-transcript-version="2">
 in the Slack thread that it's wrong, the CTO
 </span>
 <span data-rw-start="558.08" data-rw-transcript-version="2">
 is probably right. So, the context engine
 </span>
 <span data-rw-start="559.839" data-rw-transcript-version="2">
 reasons about that and goes, well, the
 </span>
 <span data-rw-start="561.04" data-rw-transcript-version="2">
 code says this, Slack says this, that's
 </span>
 <span data-rw-start="563.2" data-rw-transcript-version="2">
 the CTO. We should probably tell the
 </span>
 <span data-rw-start="565.12" data-rw-transcript-version="2">
 agent what the CTO said, and of course
 </span>
 <span data-rw-start="567.36" data-rw-transcript-version="2">
 provide the source code, etc.
 </span>
</p>
<p>
 <span data-rw-start="569.44" data-rw-transcript-version="2">
 Passes what's truth. So it handles
 </span>
 <span data-rw-start="571.519" data-rw-transcript-version="2">
 truthiness. That's a tough problem. We
 </span>
 <span data-rw-start="573.6" data-rw-transcript-version="2">
 have a lot of techniques in our product
 </span>
 <span data-rw-start="574.959" data-rw-transcript-version="2">
 to solve it. It is not fully solved. It
 </span>
 <span data-rw-start="578" data-rw-transcript-version="2">
 should respect permissions and
 </span>
 <span data-rw-start="578.959" data-rw-transcript-version="2">
 governments. This is pretty basic. It's
 </span>
 <span data-rw-start="580.24" data-rw-transcript-version="2">
 one of the reasons this is delivered
 </span>
 <span data-rw-start="581.44" data-rw-transcript-version="2">
 over MCP is you can carry the OOTH model
 </span>
 <span data-rw-start="584" data-rw-transcript-version="2">
 through for data governance and a bunch
 </span>
 <span data-rw-start="585.76" data-rw-transcript-version="2">
 of other reasons that matter in scaling
 </span>
 <span data-rw-start="587.68" data-rw-transcript-version="2">
 businesses. I mean, as soon as you're 20
 </span>
 <span data-rw-start="589.12" data-rw-transcript-version="2">
 plus, typically this matters because
 </span>
 <span data-rw-start="591.04" data-rw-transcript-version="2">
 some data should not be accessible to
 </span>
 <span data-rw-start="592.8" data-rw-transcript-version="2">
 others. So, when you build your engine,
 </span>
</p>
<p>
 <span data-rw-start="594.959" data-rw-transcript-version="2">
 you do not want to put everything in
 </span>
 <span data-rw-start="596.8" data-rw-transcript-version="2">
 there, especially when you think about
 </span>
 <span data-rw-start="598.32" data-rw-transcript-version="2">
 we ingest Slack conversations and
 </span>
 <span data-rw-start="600" data-rw-transcript-version="2">
 Microsoft Teams convos. So, if it's you,
 </span>
 <span data-rw-start="602.959" data-rw-transcript-version="2">
 we will return responses from private
 </span>
 <span data-rw-start="604.88" data-rw-transcript-version="2">
 chats, but if someone else asks a
 </span>
 <span data-rw-start="606.959" data-rw-transcript-version="2">
 question, we will never show them
 </span>
 <span data-rw-start="608.48" data-rw-transcript-version="2">
 private chats that aren't theirs. That’s
 </span>
 <span data-rw-start="610.48" data-rw-transcript-version="2">
 just one easy way to think about it. And
 </span>
 <span data-rw-start="613.12" data-rw-transcript-version="2">
 it should deliver the right context, the
 </span>
 <span data-rw-start="614.48" data-rw-transcript-version="2">
 right model at the right time in a token
 </span>
 <span data-rw-start="615.839" data-rw-transcript-version="2">
 Optimized way. This is how ours works.
 </span>
</p>
<p>
 <span data-rw-start="618.88" data-rw-transcript-version="2">
 So the short is, we ingest a bunch of
 </span>
 <span data-rw-start="620.48" data-rw-transcript-version="2">
 data sources. It sits in our engine. We
 </span>
 <span data-rw-start="622.56" data-rw-transcript-version="2">
 have six key differentiators, which I’ll
 </span>
 <span data-rw-start="624.24" data-rw-transcript-version="2">
 go into in a sec. And then on the output
 </span>
 <span data-rw-start="626.399" data-rw-transcript-version="2">
 side, there should be many surface areas
 </span>
 <span data-rw-start="628.16" data-rw-transcript-version="2">
 where agents and humans are able to
 </span>
 <span data-rw-start="630.079" data-rw-transcript-version="2">
 interact with the context engine. One of
 </span>
 <span data-rw-start="631.92" data-rw-transcript-version="2">
 ours is simple. Human engineers in Slack
 </span>
 <span data-rw-start="634.32" data-rw-transcript-version="2">
 just chat with it and ask it questions
 </span>
 <span data-rw-start="635.92" data-rw-transcript-version="2">
 all the time to get data they need. I’ll
 </span>
 <span data-rw-start="637.76" data-rw-transcript-version="2">
 show you an example. Um, but then of
 </span>
 <span data-rw-start="640" data-rw-transcript-version="2">
 course, agents as you move to background
 </span>
 <span data-rw-start="642" data-rw-transcript-version="2">
 agents, they need a context engine in
 </span>
 <span data-rw-start="644.64" data-rw-transcript-version="2">
 order to run headlessly or to run in the
 </span>
 <span data-rw-start="646.64" data-rw-transcript-version="2">
 background, or run in the cloud because
 </span>
</p>
<p>
 <span data-rw-start="647.839" data-rw-transcript-version="2">
 they have to be able to ask questions of
 </span>
 <span data-rw-start="649.36" data-rw-transcript-version="2">
 a machine, not a person, because
 </span>
 <span data-rw-start="651.44" data-rw-transcript-version="2">
 otherwise, you’re not going to wake up to
 </span>
 <span data-rw-start="652.56" data-rw-transcript-version="2">
 a PR. You’re going to wake up to an, “Am I
 </span>
 <span data-rw-start="654.32" data-rw-transcript-version="2">
 allowed to use this tool?” And that’s not
 </span>
 <span data-rw-start="656.32" data-rw-transcript-version="2">
 helpful. So these are the six. We’re
 </span>
 <span data-rw-start="659.279" data-rw-transcript-version="2">
 going to move at pace. But the short is,
 </span>
 <span data-rw-start="661.04" data-rw-transcript-version="2">
 I’ve talked to a lot of these, but these
 </span>
 <span data-rw-start="662.399" data-rw-transcript-version="2">
 are kind of marketing terms. Unified
 </span>
 <span data-rw-start="664.24" data-rw-transcript-version="2">
 System context. So it should be able to
 </span>
 <span data-rw-start="665.839" data-rw-transcript-version="2">
 reason across all of your systems of
 </span>
 <span data-rw-start="667.92" data-rw-transcript-version="2">
 records. It has to be able to do
 </span>
 <span data-rw-start="669.76" data-rw-transcript-version="2">
 targeted retrieval.
 </span>
</p>
<p>
 <span data-rw-start="672.16" data-rw-transcript-version="2">
 Conflict resolution, as described there,
 </span>
 <span data-rw-start="673.92" data-rw-transcript-version="2">
 are many times where the docs and this,
 </span>
 <span data-rw-start="675.76" data-rw-transcript-version="2">
 and that are conflicting. So how do you
 </span>
 <span data-rw-start="677.519" data-rw-transcript-version="2">
 settle that? That data governance
 </span>
 <span data-rw-start="679.2" data-rw-transcript-version="2">
 problem. So, secure access model,
 </span>
 <span data-rw-start="681.12" data-rw-transcript-version="2">
 personalized relevance, building social
 </span>
 <span data-rw-start="682.72" data-rw-transcript-version="2">
 graphs, knowing who you are, who you
 </span>
 <span data-rw-start="684.24" data-rw-transcript-version="2">
 work with. And finally, of course, token
 </span>
 <span data-rw-start="686.079" data-rw-transcript-version="2">
 optimization. This is becoming a pretty
 </span>
 <span data-rw-start="687.92" data-rw-transcript-version="2">
 big issue. A lot of benefits you get on
 </span>
 <span data-rw-start="690" data-rw-transcript-version="2">
 token optimization is just by having a
 </span>
 <span data-rw-start="692.399" data-rw-transcript-version="2">
 context engine because you don't rerun
 </span>
 <span data-rw-start="694.24" data-rw-transcript-version="2">
 those GPS for the agent to know. But
 </span>
 <span data-rw-start="696.959" data-rw-transcript-version="2">
 also, with an engine, if you reason
 </span>
 <span data-rw-start="699.04" data-rw-transcript-version="2">
 across everything, it's then able to
 </span>
 <span data-rw-start="700.88" data-rw-transcript-version="2">
 compress the response into exactly what
 </span>
 <span data-rw-start="702.88" data-rw-transcript-version="2">
 the agent needs and only send that back
 </span>
 <span data-rw-start="704.88" data-rw-transcript-version="2">
 as an answer.
 </span>
 <span data-rw-start="707.68" data-rw-transcript-version="2">
 That task I talked about, I'm not going
 </span>
 <span data-rw-start="710" data-rw-transcript-version="2">
 to lie, we asked Claude to do the
 </span>
 <span data-rw-start="711.36" data-rw-transcript-version="2">
 comparison, so it made these bar charts.
 </span>
</p>
<p>
 <span data-rw-start="712.959" data-rw-transcript-version="2">
 And numbers, but it did pull out all the
 </span>
 <span data-rw-start="714.959" data-rw-transcript-version="2">
 key points of this. That same prompt,
 </span>
 <span data-rw-start="717.2" data-rw-transcript-version="2">
 one was naive. It had all the MCPS it
 </span>
 <span data-rw-start="719.519" data-rw-transcript-version="2">
 needed to get the data, and the other had
 </span>
 <span data-rw-start="721.6" data-rw-transcript-version="2">
 our context engine only. This is the
 </span>
 <span data-rw-start="724.16" data-rw-transcript-version="2">
 difference across key principles of
 </span>
 <span data-rw-start="726" data-rw-transcript-version="2">
 engineering. But these are funny. It
 </span>
 <span data-rw-start="728.399" data-rw-transcript-version="2">
 like didn't catch that we use bedrock as
 </span>
 <span data-rw-start="730" data-rw-transcript-version="2">
 a fallback. It shipped like bugs.
 </span>
 <span data-rw-start="732.399" data-rw-transcript-version="2">
 There was one that broke the custom
 </span>
 <span data-rw-start="733.839" data-rw-transcript-version="2">
 callers. The short story is if you're
 </span>
 <span data-rw-start="736" data-rw-transcript-version="2">
 working at any form of scale, again 20
 </span>
 <span data-rw-start="738.32" data-rw-transcript-version="2">
 plus agents are just going to try to
 </span>
 <span data-rw-start="740.8" data-rw-transcript-version="2">
 mock things, and it'll look like
 </span>
 <span data-rw-start="742.24" data-rw-transcript-version="2">
 a prototype. It's not mergeable. If you
 </span>
 <span data-rw-start="744.079" data-rw-transcript-version="2">
 get a context engine. When I put up this
 </span>
 <span data-rw-start="746.16" data-rw-transcript-version="2">
 PR, our senior engineer for the one with
 </span>
 <span data-rw-start="748.32" data-rw-transcript-version="2">
 the engine basically gave me a nitpick,
 </span>
 <span data-rw-start="750.399" data-rw-transcript-version="2">
 and was like, "Yep, you can merge this.
 </span>
 <span data-rw-start="751.92" data-rw-transcript-version="2">
 Just fix that." Great.
 </span>
 <span data-rw-start="755.36" data-rw-transcript-version="2">
 These are some of our hard lessons.
 </span>
 <span data-rw-start="758.079" data-rw-transcript-version="2">
 We did try to optimize for access, not
 </span>
 <span data-rw-start="759.92" data-rw-transcript-version="2">
 understand. We like the bottle will
 </span>
 <span data-rw-start="760.959" data-rw-transcript-version="2">
 handle this. Like, the agent's totally
 </span>
 <span data-rw-start="762.24" data-rw-transcript-version="2">
 going to figure it out. It'll collapse.
 </span>
</p>
<p>
 <span data-rw-start="763.36" data-rw-transcript-version="2">
 Into mythos or whatever. It hasn't.
 </span>
 <span data-rw-start="766" data-rw-transcript-version="2">
 It's been years, so we were like, "We
 </span>
 <span data-rw-start="767.44" data-rw-transcript-version="2">
 have to solve this problem another way."
 </span>
 <span data-rw-start="768.639" data-rw-transcript-version="2">
 And I think that's correct, based on
 </span>
 <span data-rw-start="769.92" data-rw-transcript-version="2">
 actually, Anthropics launched last night
 </span>
 <span data-rw-start="771.36" data-rw-transcript-version="2">
 with cloud agents, and Ryan's talk this
 </span>
 <span data-rw-start="773.44" data-rw-transcript-version="2">
 morning. You have to get context into
 </span>
 <span data-rw-start="775.519" data-rw-transcript-version="2">
 the harness, and an engine is the way to
 </span>
 <span data-rw-start="777.76" data-rw-transcript-version="2">
 do that. We hid conflicts instead of
 </span>
 <span data-rw-start="779.92" data-rw-transcript-version="2">
 servicing them. The agent would actually
 </span>
 <span data-rw-start="781.279" data-rw-transcript-version="2">
 just pick when we found conflicts at
 </span>
 <span data-rw-start="782.88" data-rw-transcript-version="2">
 first because we like it can't be that
 </span>
 <span data-rw-start="784.24" data-rw-transcript-version="2">
 bad. It's that bad. So, solving conflicts is an important problem.
 </span>
</p>
<p>
 <span data-rw-start="787.279" data-rw-transcript-version="2">
 And then finally, this is a really fun one.
 </span>
 <span data-rw-start="790.959" data-rw-transcript-version="2">
 We thought as good answers happened, we
 </span>
 <span data-rw-start="793.12" data-rw-transcript-version="2">
 actually got feedback loops on those. So
 </span>
 <span data-rw-start="794.56" data-rw-transcript-version="2">
 we were caching them for latency. If you
 </span>
 <span data-rw-start="796.8" data-rw-transcript-version="2">
 cache a good answer, basically it's like
 </span>
 <span data-rw-start="799.2" data-rw-transcript-version="2">
 when you write docs, right? The moment
 </span>
 <span data-rw-start="800.399" data-rw-transcript-version="2">
 you write it, it's no longer valid
 </span>
 <span data-rw-start="801.839" data-rw-transcript-version="2">
 because things are changing. So, if you
 </span>
 <span data-rw-start="803.68" data-rw-transcript-version="2">
 cache a correct answer, and then tomorrow
 </span>
 <span data-rw-start="805.279" data-rw-transcript-version="2">
 someone asks the same question, and you
 </span>
 <span data-rw-start="806.72" data-rw-transcript-version="2">
 answer it, you probably lied to them.
 </span>
</p>
<p>
 <span data-rw-start="808.56" data-rw-transcript-version="2">
 Now, because things probably changed in a
 </span>
 <span data-rw-start="810.16" data-rw-transcript-version="2">
 24-hour clock,
 </span>
 <span data-rw-start="812.16" data-rw-transcript-version="2">
 so the system is not the
 </span>
 <span data-rw-start="814.88" data-rw-transcript-version="2">
 same. Obviously, some questions I'm sure
 </span>
 <span data-rw-start="816.399" data-rw-transcript-version="2">
 are stable, but this led to a lot of
 </span>
 <span data-rw-start="818.16" data-rw-transcript-version="2">
 problems.
 </span>
 <span data-rw-start="820.8" data-rw-transcript-version="2">
 So I highly recommend against
 </span>
 <span data-rw-start="824.639" data-rw-transcript-version="2">
 even if it's optimized.
 </span>
 <span data-rw-start="826.88" data-rw-transcript-version="2">
 This is where AI forward teams are.
 </span>
 <span data-rw-start="828.56" data-rw-transcript-version="2">
 They're using context engines in all of
 </span>
 <span data-rw-start="830.56" data-rw-transcript-version="2">
 these cases. So I know we're all
 </span>
 <span data-rw-start="832.639" data-rw-transcript-version="2">
 engineers, but I’m sure that we support
 </span>
 <span data-rw-start="835.279" data-rw-transcript-version="2">
 others in our orgs, like a ask
 </span>
 <span data-rw-start="836.8" data-rw-transcript-version="2">
 engineering channel. Our context engine
 </span>
 <span data-rw-start="838.72" data-rw-transcript-version="2">
 sits in every customer’s ask,
 </span>
 <span data-rw-start="840.72" data-rw-transcript-version="2">
 the engineering channel. It detects if a
 </span>
 <span data-rw-start="842.72" data-rw-transcript-version="2">
 question is asked, it scores confidently,
 </span>
 <span data-rw-start="844.959" data-rw-transcript-version="2">
 and then it responds automatically. So
 </span>
 <span data-rw-start="846.72" data-rw-transcript-version="2">
 when support teams, sales teams, whoever
 </span>
 <span data-rw-start="848.88" data-rw-transcript-version="2">
 is like, hey, what's running in prod?
 </span>
</p>
<p>
 <span data-rw-start="850.32" data-rw-transcript-version="2">
 What's this? The context engine just
 </span>
 <span data-rw-start="852.32" data-rw-transcript-version="2">
 answers them and deals with the issue,
 </span>
 <span data-rw-start="854.959" data-rw-transcript-version="2">
 just like it would answer an agent asking for data.
 </span>
 <span data-rw-start="857.44" data-rw-transcript-version="2">
 Um, so there are many ways, like that use case I just talked
 </span>
 <span data-rw-start="859.44" data-rw-transcript-version="2">
 about, but then ticket enrichment,
 </span>
 <span data-rw-start="861.44" data-rw-transcript-version="2">
 triage, incident management, obviously.
 </span>
</p>
<p>
 <span data-rw-start="861.68" data-rw-transcript-version="2">
 Working with your agents and coding.
 </span>
 <span data-rw-start="862.88" data-rw-transcript-version="2">
 These are all great ways that you get
 </span>
 <span data-rw-start="864.399" data-rw-transcript-version="2">
 tons of leverage out of getting one of
 </span>
 <span data-rw-start="866.32" data-rw-transcript-version="2">
 these into place.
 </span>
 <span data-rw-start="869.04" data-rw-transcript-version="2">
 Teams then customize them. So most fork,
 </span>
 <span data-rw-start="871.199" data-rw-transcript-version="2">
 we have like a cookbook. They take that
 </span>
 <span data-rw-start="872.72" data-rw-transcript-version="2">
 repo, the cookbooks full of skills. Um,
 </span>
 <span data-rw-start="874.56" data-rw-transcript-version="2">
 but then you devise your skills with
 </span>
 <span data-rw-start="876.639" data-rw-transcript-version="2">
 your standard operating procedures. You
 </span>
 <span data-rw-start="878.48" data-rw-transcript-version="2">
 obviously can build your own workflows,
 </span>
 <span data-rw-start="880.079" data-rw-transcript-version="2">
 whether you do that as a skill or some
 </span>
 <span data-rw-start="881.76" data-rw-transcript-version="2">
 other technique. And then, of course,
 </span>
 <span data-rw-start="883.36" data-rw-transcript-version="2">
 custom agents. All of these can leverage
 </span>
 <span data-rw-start="885.519" data-rw-transcript-version="2">
 that same context engine. So you just
 </span>
 <span data-rw-start="887.519" data-rw-transcript-version="2">
 get a huge amount of leverage.
 </span>
</p>
<p>
 <span data-rw-start="890.24" data-rw-transcript-version="2">
 This is what I'm trying to leave you
 </span>
 <span data-rw-start="891.6" data-rw-transcript-version="2">
 with. An agent should write code that
 </span>
 <span data-rw-start="893.92" data-rw-transcript-version="2">
 feels like it was written by someone
 </span>
 <span data-rw-start="895.199" data-rw-transcript-version="2">
 who's been on your team for years. Like
 </span>
 <span data-rw-start="896.959" data-rw-transcript-version="2">
 that's just like we should expect that
 </span>
 <span data-rw-start="898.32" data-rw-transcript-version="2">
 by now. And this is one of those
 </span>
 <span data-rw-start="899.68" data-rw-transcript-version="2">
 techniques to get you there.
 </span>
</p>
<p>
 <span data-rw-start="902.24" data-rw-transcript-version="2">
 I can do a brief QA and I can give a
 </span>
 <span data-rw-start="904.079" data-rw-transcript-version="2">
 demo. I have three minutes left. So
 </span>
 <span data-rw-start="906.72" data-rw-transcript-version="2">
 what's your preference? Demo.
 </span>
</p>
<p>
 <span data-rw-start="909.6" data-rw-transcript-version="2">
 &gt;&gt; Cool. So this is the tool I talked about
 </span>
 <span data-rw-start="911.76" data-rw-transcript-version="2">
 at the workshop. We're going to open
 </span>
 <span data-rw-start="912.88" data-rw-transcript-version="2">
 source it. This is one component of a
 </span>
 <span data-rw-start="915.76" data-rw-transcript-version="2">
 key of a social graph. And so
 </span>
 <span data-rw-start="919.839" data-rw-transcript-version="2">
 when you run it, this will be available.
 </span>
 <span data-rw-start="921.36" data-rw-transcript-version="2">
 I think it's Monday. We're going to
 </span>
 <span data-rw-start="922.32" data-rw-transcript-version="2">
 actually open source. Currently, it's closed source.
 </span>
 <span data-rw-start="923.68" data-rw-transcript-version="2">
 There’s a whole setup, but we had a
 </span>
 <span data-rw-start="925.44" data-rw-transcript-version="2">
 bunch of teams hack against it and ship
 </span>
 <span data-rw-start="926.88" data-rw-transcript-version="2">
 code. But basically, it will build you
 </span>
 <span data-rw-start="928.88" data-rw-transcript-version="2">
 one of these. Uh, I’m going to zoom in.
 </span>
</p>
<p>
 <span data-rw-start="930.72" data-rw-transcript-version="2">
 This is our engineering or, as you can
 </span>
 <span data-rw-start="933.44" data-rw-transcript-version="2">
 see, there’s different nodes and edges.
 </span>
 <span data-rw-start="935.04" data-rw-transcript-version="2">
 It's a basic graph, but it's a social
 </span>
 <span data-rw-start="936.399" data-rw-transcript-version="2">
 graph. Rasheen is a goddamn machine. So
 </span>
 <span data-rw-start="940.079" data-rw-transcript-version="2">
 that's how much he ships, which is indicated by the
 </span>
 <span data-rw-start="941.92" data-rw-transcript-version="2">
 size of the node. If you go look at this,
 </span>
 <span data-rw-start="943.68" data-rw-transcript-version="2">
 it’s algorithmically procedurally generated.
 </span>
 <span data-rw-start="945.44" data-rw-transcript-version="2">
 So, you’ll see the tool, but in short, you
 </span>
 <span data-rw-start="947.279" data-rw-transcript-version="2">
 can see on the right who he's working
 </span>
 <span data-rw-start="948.639" data-rw-transcript-version="2">
 with. Sorry, the screen is like kind of
 </span>
 <span data-rw-start="950.32" data-rw-transcript-version="2">
 small.
 </span>
</p>
<p>
 <span data-rw-start="952.24" data-rw-transcript-version="2">
 Great. Kind of worked. Uh, so you can see
 </span>
 <span data-rw-start="954.079" data-rw-transcript-version="2">
 who he works with, whose code he reviews,
 </span>
 <span data-rw-start="955.759" data-rw-transcript-version="2">
 what area he worked in.
 </span>
</p>
<p>
 <span data-rw-start="957.68" data-rw-transcript-version="2">
 Labeling with an API key from Enthropic.
 </span>
 <span data-rw-start="959.759" data-rw-transcript-version="2">
 Oh god, now it looks terrible. Let's zoom
 </span>
 <span data-rw-start="961.44" data-rw-transcript-version="2">
 in a little better. Um, sorry, it's a fun
 </span>
 <span data-rw-start="965.6" data-rw-transcript-version="2">
 tool, but basically this expert graph
 </span>
 <span data-rw-start="967.759" data-rw-transcript-version="2">
 would allow you to, when a query comes
 </span>
 <span data-rw-start="970.24" data-rw-transcript-version="2">
 across, we go, "Oh, you're Rashine. You
 </span>
 <span data-rw-start="972.24" data-rw-transcript-version="2">
 work with these people." Great. It'll
 </span>
 <span data-rw-start="974.16" data-rw-transcript-version="2">
 pivot on that data. It'll then zoom into
 </span>
 <span data-rw-start="976.56" data-rw-transcript-version="2">
 the code bases that he's dealing with.
 </span>
</p>
<p>
 <span data-rw-start="978.48" data-rw-transcript-version="2">
 So, when you as an engineer ask maybe
 </span>
 <span data-rw-start="980.639" data-rw-transcript-version="2">
 not the best prompt of all time, but
 </span>
 <span data-rw-start="982.16" data-rw-transcript-version="2">
 you're like, "Hey, I got to get this
 </span>
 <span data-rw-start="983.279" data-rw-transcript-version="2">
 done. There's a bug. Got to fix it."
 </span>
 <span data-rw-start="985.839" data-rw-transcript-version="2">
 It'll know who you are. It'll pivot on
 </span>
 <span data-rw-start="987.36" data-rw-transcript-version="2">
 that. It'll probably find the bug that's
 </span>
 <span data-rw-start="989.04" data-rw-transcript-version="2">
 like correct. And again, it'll use this
 </span>
 <span data-rw-start="991.279" data-rw-transcript-version="2">
 component to do a bunch of things and
 </span>
 <span data-rw-start="993.36" data-rw-transcript-version="2">
 make decisions as it traverses in order
 </span>
 <span data-rw-start="995.199" data-rw-transcript-version="2">
 to reason to give the agent the exact
 </span>
 <span data-rw-start="997.199" data-rw-transcript-version="2">
 answer that it needs. So this, this tool
 </span>
 <span data-rw-start="999.92" data-rw-transcript-version="2">
 like generates this for you. You just
 </span>
 <span data-rw-start="1001.199" data-rw-transcript-version="2">
 point it at your code repo. It'll do a
 </span>
 <span data-rw-start="1002.959" data-rw-transcript-version="2">
 construction. Um, but it does things like
 </span>
 <span data-rw-start="1005.44" data-rw-transcript-version="2">
 creates experts across like various
 </span>
</p>
<p>
 <span data-rw-start="1007.6" data-rw-transcript-version="2">
 Areas in the business. So, in our libs,
 </span>
 <span data-rw-start="1009.36" data-rw-transcript-version="2">
 our services, I'm quick scrolling,
 </span>
 <span data-rw-start="1011.12" data-rw-transcript-version="2">
 apologies, we got time. You can check a
 </span>
 <span data-rw-start="1013.519" data-rw-transcript-version="2">
 heat map of who works with each
 </span>
 <span data-rw-start="1015.04" data-rw-transcript-version="2">
 other, like who reviews what, who
 </span>
 <span data-rw-start="1016.56" data-rw-transcript-version="2">
 authors what. You can check peer tables,
 </span>
 <span data-rw-start="1019.04" data-rw-transcript-version="2">
 you know, who Andre works with, etc. So,
 </span>
 <span data-rw-start="1021.759" data-rw-transcript-version="2">
 this data is available in a context engine,
 </span>
 <span data-rw-start="1024.319" data-rw-transcript-version="2">
 very useful. And again, this will be
 </span>
 <span data-rw-start="1026.4" data-rw-transcript-version="2">
 open source. Uh, if I think you got a
 </span>
 <span data-rw-start="1028.24" data-rw-transcript-version="2">
 badge scan, I'll just email you all
 </span>
 <span data-rw-start="1029.76" data-rw-transcript-version="2">
 as soon as it's open source. That's
 </span>
 <span data-rw-start="1031.039" data-rw-transcript-version="2">
 cool.
 </span>
</p>
<p>
 <span data-rw-start="1032.64" data-rw-transcript-version="2">
 Another quick demo. Ghosty, my boy. So,
 </span>
 <span data-rw-start="1036.959" data-rw-transcript-version="2">
 in this one, I actually used our MCP, and
 </span>
 <span data-rw-start="1039.28" data-rw-transcript-version="2">
 I just straight up said, how do I make a
 </span>
 <span data-rw-start="1040.72" data-rw-transcript-version="2">
 new first class integration to Zenesk?
 </span>
 <span data-rw-start="1043.28" data-rw-transcript-version="2">
 I just said, use the MCP. It would
 </span>
 <span data-rw-start="1045.28" data-rw-transcript-version="2">
 probably have picked it up, but I want
 </span>
 <span data-rw-start="1046.64" data-rw-transcript-version="2">
 to make sure for this demo that it did.
 </span>
 <span data-rw-start="1048.48" data-rw-transcript-version="2">
 It ran, it chose to use our research task
 </span>
 <span data-rw-start="1050.72" data-rw-transcript-version="2">
 tool. You can see that it constructed a
 </span>
 <span data-rw-start="1052.799" data-rw-transcript-version="2">
 query. So, the agent did that based on
 </span>
 <span data-rw-start="1054.64" data-rw-transcript-version="2">
 the shape of our MCP. So, it wrote the
 </span>
 <span data-rw-start="1056.4" data-rw-transcript-version="2">
 right query, ran that. It did effort.
 </span>
</p>
<p>
 <span data-rw-start="1058.64" data-rw-transcript-version="2">
 High for reasoning. It got the data
 </span>
 <span data-rw-start="1060.16" data-rw-transcript-version="2">
 back. Then it triggered its explore
 </span>
 <span data-rw-start="1062" data-rw-transcript-version="2">
 agents. This is key because now they're
 </span>
 <span data-rw-start="1063.52" data-rw-transcript-version="2">
 exploring the right place after this
 </span>
 <span data-rw-start="1064.88" data-rw-transcript-version="2">
 research packet came in. Great research
 </span>
 <span data-rw-start="1067.12" data-rw-transcript-version="2">
 results. Did the thing, did the thing,
 </span>
 <span data-rw-start="1068.559" data-rw-transcript-version="2">
 wrote me a plan. So if you look at this
 </span>
 <span data-rw-start="1070.799" data-rw-transcript-version="2">
 plan, you do not know my source. That's
 </span>
 <span data-rw-start="1072.799" data-rw-transcript-version="2">
 fair. But if we just scan it, like it
 </span>
 <span data-rw-start="1075.76" data-rw-transcript-version="2">
 found all the things that matter like
 </span>
 <span data-rw-start="1077.2" data-rw-transcript-version="2">
 registering our provider, obviously we
 </span>
 <span data-rw-start="1079.28" data-rw-transcript-version="2">
 have a factory pattern. Um, I'll just
 </span>
 <span data-rw-start="1081.44" data-rw-transcript-version="2">
 pull through, but like the library
 </span>
 <span data-rw-start="1082.799" data-rw-transcript-version="2">
 modules, client, like this is like one
 </span>
 <span data-rw-start="1085.12" data-rw-transcript-version="2">
 hell of a plan is the short story. And
 </span>
 <span data-rw-start="1087.36" data-rw-transcript-version="2">
 it's like pretty correct. I would
 </span>
 <span data-rw-start="1088.72" data-rw-transcript-version="2">
 probably prompt this a couple more times
 </span>
 <span data-rw-start="1089.919" data-rw-transcript-version="2">
 to get it totally right, but at any time
 </span>
 <span data-rw-start="1092.08" data-rw-transcript-version="2">
 while it's executing, it's able to keep
 </span>
 <span data-rw-start="1093.919" data-rw-transcript-version="2">
 calling our MCP. So typically what we
 </span>
 <span data-rw-start="1096.16" data-rw-transcript-version="2">
 see is use the engine for planning, run
 </span>
 <span data-rw-start="1098.88" data-rw-transcript-version="2">
 execution,
 </span>
 <span data-rw-start="1100.48" data-rw-transcript-version="2">
 and then basically as you get to code
 </span>
 <span data-rw-start="1102.32" data-rw-transcript-version="2">
 review, leverage your engine again
 </span>
 <span data-rw-start="1104.32" data-rw-transcript-version="2">
 because that engine is very good at code.
 </span>
</p>
<p>
 <span data-rw-start="1106.08" data-rw-transcript-version="2">
 Review, and it's extremely good at
 </span>
 <span data-rw-start="1107.44" data-rw-transcript-version="2">
 planning.
 </span>
 <span data-rw-start="1109.039" data-rw-transcript-version="2">
 That's all the time I have, so thank you all very much.
 </span>
 <span data-rw-start="1111.6" data-rw-transcript-version="2">
 I appreciate it. Uh, I'm
 </span>
 <span data-rw-start="1113.679" data-rw-transcript-version="2">
 at a booth at G16, so come by if you
 </span>
 <span data-rw-start="1116" data-rw-transcript-version="2">
 have questions.
 </span>
</p>