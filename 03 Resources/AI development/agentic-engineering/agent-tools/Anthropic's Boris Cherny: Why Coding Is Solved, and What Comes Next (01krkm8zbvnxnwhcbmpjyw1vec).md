---
title: "Anthropic''s Boris Cherny: Why Coding Is Solved, and What Comes Next"
source: "https://m.youtube.com/watch?v=SlGRN8jh2RI&pp=ugUEEgJlbg%3D%3D"
author: "Sequoia Capital"
published: 2026-05-04
created: 2026-05-14
description: "Boris Cherny, creator of Claude Code at Anthropic, joins Sequoia partner"
tags:
  - to-process
  - agent-tools
---

Okay, I'm excited to introduce our next speaker. Show of hands, who here uses Claude code? Okay, show of hands, who here has Claude code psychosis? Come on guys, [clears throat] it's okay. It's okay. Um my my my team lovingly says I have Claude code psychosis, which may or may not be true. Um we are delighted to have Boris Cherny with us today. Uh Boris is the creator, the father of Claude code. Um and uh in the process of doing that has just had a front row seat to to reinventing uh the modern way of of software development. 

Um and we're we're really grateful to you, Boris, for taking the time to speak with us today. We know that um the entirety of software development kind of rests on your shoulders. So, thank you for taking it out of your time to be with us today. And interviewing Boris is Lauren Reader from our team. Thank you. >> [applause] >> Giving our chairs. Um you took my you took my opening line, Asia. We asked who here uses Claude code. There's a lot of hands. That's 

awesome. Thank you for joining us, Boris. It's very special to have you here. Um as a roomful of builders, I think you are changing building entirely. And so, I'm very curious to explore how you think about the future of software, coding, and what we should spend all of our free time on. Um but I'll give you a me a tiny bit more background on you so that everyone has a little bit more context. So, beyond creating Claude code, Boris is very much an engineer's engineer. You were writing a lot of code 

through your whole career, writing textbooks about code, including programming in TypeScript. Um and I think last time we chatted you hadn't written a single line of code in the last year, or at least so far in 2026, which is quite the change. Um There's also a a little known thing back in middle school, I wrote a guide about uh writing BASIC for TI-83 Plus calculators. And I I just I I searched for it, it's actually still on the internet. It's extremely embarrassing, so please don't search it. But it [laughter] exists. We will definitely be finding that. Um so, 

we're going to do I'm going to start with a few questions here. Maybe we'll start with a little bit of the history of Claude code, how you started it, and then we're going to have a lot of audience Q&A for this one. And so, start thinking about your questions in the back of your head, uh and would love to turn it over to you all soon. Yeah. Um and also real quick, so for people that use Claude code, do people use the CLI mostly? Like okay, majority CLI? Okay. That's a lot. Majority desktop? Okay. Majority VS code or JetBrains IDE? 

Okay. That's actually not a lot. Okay. Other? I'm like iOS mostly these days. Yeah. >> [laughter] >> Okay. Cool. Um yeah, so I started Claude code kind of accidentally in a in a lot of ways. Um I joined this team back in late 2024. It was a sort of this incubator within Anthropic called Anthropic Labs. And uh the team kind of served its purpose. Um we created Claude code, uh MCP, and the desktop app. It was a team it was just a few of us. So, very much like innovation team. 

We built the thing that we wanted to build, we disbanded the team. Uh now the team's actually back together for round two. Mike Krieger, who's the you know, like the chief product officer at at Anthropic and used to be one of the founders at Instagram, so he's leading that right now. Um so the kind of the the the the reason that I started to work on coding is we felt like there was this product overhang. And I I'm guessing people here use that word a lot. Uh but we definitely use this word a lot in kind of within the lab. 

Uh there's this idea that the model can do all the stuff that no product has yet captured. And in late 2024, when we were looking at coding, the way that we did coding, the state of the art at the time was type ahead. It was you open your IDE and you press tab and you can like complete like one line at a time. And that was the thing that Sonnet 3.5 enabled for the first time. But the feeling was we could actually go a lot further than that. And the model was almost ready for the next big step. So, we don't have to do type ahead anymore, we can just have the agent write all of the code. 

And so, I built it, and it just really didn't work for the first 6 months. It was like not very good. It was barely usable. I wrote it from I used it for maybe 10% of my code or something like that. And even after we released Claude code initially, it was not a hit. There's a lot of people that used it, but it did not have this exponential growth that it has today. Um that started with Opus 4 in May. And I I remember that very clearly. That's like when the exponential growth started, and then it kind of inflected with every model release. Uh like it 

started with Opus 4, then 4.5, then 4.6, now 4.7. It just kind of keeps inflecting. But essentially, we were trying to build this thing that was like pre-PMF, and we knew that it wouldn't have PMF for 6 months because we were building for the next model. And that was the idea the pretty much the whole time. And you know, for Anthropic in general, we've always just been very focused. We've always cared about business and enterprise and safety and coding. That's just always been kind of the way that we wanted to build. And so, at some point we kind of knew that we wanted to build a product. We didn't know exactly what 

we wanted. So, this kind of ended up being the the product bet. It's an incredible story, especially that it was an accident. Um so, you've said on the record that you think coding is solved. Uh if this is one of the three best from Anthropic, can you tell us more about what you mean by that, and what might still not be solved, or what second-order problems might come? All right. I can ask another question for the room. Who writes 100% of their code by hand? Who writes 100% of their code using a agent like Claude code? 

Okay. Who's like somewhere in between? Okay. So, like 50% solved. >> [laughter] >> I mean, for me it's for me it's like for me it's 100%. Like the the Claude code code base, um you know, it leaked, so you know, people know. Uh it's pretty simple. It's just like TypeScript and it's React. Like there's no big secret. There's there's nothing really complicated. The the reason we picked TypeScript and React is it's very on distribution for the model. So, when we started, you know, building the code base, the model was not as intelligent 

as it is today, so the language and the framework mattered a lot. Nowadays, you know, it can write whatever, and it can pick up new languages, new frameworks it hasn't seen. But back then, you wanted to use something pretty on distribution. Because of that, I think fairly early we got to the point where the model just wrote 100% of the code. And for us, this happened sometime in October, November last year. And so, for me today, you know, like the model writes 100% of my code. I write somewhere, you know, usually a few dozen PRs every day. Uh there was a day last week I did like 150 PRs in a day. That was like that was 

a record. I was just trying to kind of push to see how far I can get it. Um but yeah, it's like for me for me it's just solved. Um but this is not the case everywhere. There's very big complicated code bases. There's kind of weird languages the model's not good at yet. Um and you know, as everyone here knows, it's it's getting there. Usually the answer is just wait for the next model. Can you actually tell us about your personal setup? You walked us through it the other day. It is pretty wild. Yeah. Um so, I shared my personal setup like 6 months ago or something on on 

Twitter. And it it's funny, I actually I shared it I didn't realize that it would be surprising for anyone. That was just like the way that I coded. >> [laughter] >> And it's changed since then. It's changed. Um and so, now actually most of my work I do from my phone. Um and so, I don't know if like you guys won't be able to see this, but I have um so, I have like the Claude app, and if you open the Claude app, on the left-hand side, there's this little code tab, and I just have a bunch of sessions going. 

Um you you probably can't see it. >> How many sessions? Uh usually have like maybe like five to 10 sessions. Uh and then the sessions usually have a bunch of agents, so I think currently probably like a few hundred agents going. Um usually every night I have like a few thousand that are doing kind of deeper work. There's a few ways to manage it. One is that you ask Claude to use a bunch of sub-agents to do work. Actually, the the thing that I've been finding myself using more and more is the loop. So, this is {slash} loop, and it's just like the coolest thing. It's 

like the simplest thing that works. All it is is you have Claude use cron to schedule a job for some point in the future, and it's a repeat job. And it can run every every minute, every 5 minutes, every day, kind of however often you want to schedule it. And at [snorts] this point, I have like dozens of loops that are running for stuff. So, I have one that's babysitting my PRs, like fixing CI, auto-rebasing. I have another one that keeps CI healthy. So, like if there's like a flaky test or whatever, it'll it'll go and fix it. Um I have another one that grabs uh 

feedback from Twitter and kind of clusters it for me every 30 minutes. So, I just have a bunch of these loops running at any time. I sort of feel like loops are the future at this point. If you haven't experimented with it, highly highly recommend it. And we also just launched routines, which is the same thing but kind of on the server. So, even if you close your laptop, it it keeps going. So, that's your personal setup. Tell us about what you think teams will look like in the future. How do you extrapolate from all the work you're doing to keep everyone on the team moving forward, understanding the context, or do you think we need to let 

go of a lot more to agents to make it work? Um I think so I you know, it's like it's so hard to make predictions, but um I'm here to make predictions, so I'll try to make some. I I I feel like the way that things are going is generally there's going to be a lot more generalists than there are today. And today when we talk about generalists, I think largely we're talking about people that are still engineers. So, they're still writing code, but maybe they're kind of product engineers. So, maybe when we say generalist, it's like a you know, they do iOS and web and server, 

for example. That's like a generalist in engineering. But I think the thing that we're going to start to see a lot more of is generalists that are cross-disciplinary. So, this is engineers that are really good at product engineering, but also really great at design. Or really great at product and data science and engineering. Um I don't know. It's it's something that we're starting to see on our team. So, actually like a lot of people on the Claude code team are generalists across disciplines. Everyone on our team codes. So, like our 

engineering manager, our product manager, our designers, our data scientist, our finance guy, our user researcher, every single person on our team writes code. And so, you know, like they're specialist in something, but now also everyone's just coding. And you know, I'm seeing some nods, but I bet also it's actually not that surprising to people in this room cuz I bet you're seeing the same things. Um [clears throat] I'll have one more favorite questions then we'll open up to the audience. So, we talked a bit about what's changing with coding. I'm curious about what you see changing in the world 

of software or software products. Um I think as we see AI making writing code 10 or 100x cheaper, what happens to the value of the products that are produced with software? Do we have a SAS apocalypse on our hands? How do you think this plays out? And again, you're going to have to make another prediction. The SAS apocalypse question is my favorite question then. Um I think there's two things that are going to happen and I I don't think either of them is the thing that people have been talking about. 

I think one is Is anyone here an acquired listener? Like the acquired podcast? Yeah, it's like the best podcast. Uh I actually I I got to do a unplugged with them the other week and I I just I I felt like I got to like meet my heroes cuz they're they're just like the hosts are the best. So, they have this idea of uh seven powers and and this is a this is like Hamilton. He kind of wrote he wrote a book about this and this is kind of the seven modes in business. And I think what's going to happen is because of AI, some of these modes are going to get 

more important and some are going to get less important. And so, like for example, one that gets less important is uh switching costs because you can just use the model and you can kind of port from one thing to a different thing. Another one that gets less important is process power because for companies whose mode is like workflows and process and things like this, Claude is getting really good at figuring out process. And especially with 4.7, it can just hill climb anything. So, if you give it a target and you tell it to iterate until it's done, it will just do it. I think this is the first model like that. 

So, I think these are going to get less important, but I think the previous modes actually still matter. So, this is like network effects, uh scale economies, cornered resources, things like that. These are not really changing with AI. I think the second thing is if you look at the number of startups today or like maybe in the next you know, the past 10 years, I think the number of startups in the next 10 years that are just going to like disrupt everything is going to increase like 10x. Because right now you can be a tiny startup, you could build a thing that's as valuable as a large company and you can actually compete head-to-head 

because the large company has to evolve their business process, they have to evolve the way they work, they have to retrain everyone to use technology, they're going to face a lot of internal resistance to that. But you know, no one here has that problem. If you're starting fresh, then you can kind of build with AI natively from the ground up. So, I don't know. I I think it's the best time to build. It's the best time to be a startup. It's there's so much disruption coming. So, there is hope for us after all. Thank you, Boris. Um I would love to open up to audience questions if anyone has anything they 

would like to ask. Dan? I Yeah, I'm curious. Um you said that you built uh 6 months before there was product market fit, but now given that the models are good enough, how much do you attribute the success of Claude code to the model versus like product decisions in the the like field of product? Uh I think it's probably a mix. Yeah, I think it's a mix. I think I think if you asked me maybe a year ago, the ratio was maybe something like 

50/50. Um maybe I don't know. If you asked me 6 months ago, the mix would be 50/50. >> What about in 2 years? Oh, 2 year I don't know, dude. We plan in like we plan in 1 week out. >> months. Sometime in the future. >> [laughter] >> And by the way, I think the reason it was 50/50 is um you know, I I I like I I did YC back in the day. I was like the first hire at a YC company and like I did a bunch of startups. And in startups like the thing that they drill into you and then especially in YC over and over is build something people love. And so, it it doesn't matter what the 

product is, it doesn't matter like the model and all this stuff. You still in the end have to build a thing that people love. And I think that's that's why the product matters is we we pay so much attention to the little details so that as you use it all day, it's a really great experience. I think as the model's gotten better, the harness kind of gets less important. And I I think like I think that we're thinking about right now is like how do we evolve the harness? So, like how do we make loops more of a first class thing? How do we make it easier to run a lot of agents? Uh you know, beside you know, like sub agents is one idea. 

There's a bunch more stuff that we're cooking. But I think in a year, the model will be much better aligned. And so, all the safety mechanisms that we have today around uh prompt injection and kind of static verification of commands and uh permission modes, human in the loop, all this kind of stuff is just going to be less important cuz the model will just do the right thing. Um So, yeah, that's that's my prediction. Thank you. You want to toss the box, Dan? >> [snorts] >> Great. 

Um To zoom to zoom out a little bit from software, I think Claude code did a cultural change a few months ago where it democratized like building software. You can see uh shop owners building their own um software for themselves or even uh programming microcontrollers to control the light when someone opens the door. Um do you see in the future um building software becoming a skill like uh I know uh Microsoft Office? Um so, it's a thing that ev- everybody can do, not just people in the tech industry? Oh 

my god, yes. Yes. Yes. I I I think it's going to be even more than that. I think it's going to be I don't know. It's going to be a skill like yeah, like I know how to send a text message. I I I think um you know, like I I read a my my two genres are essentially sci-fi and tech history. This is what I read a lot of. I I think in tech history, there's one thing which I think to me is the clearest parallel for what's happening right now. And this is in the 1400s, the printing press in Europe. And what what happened was before the printing press, essentially 10% of the 

European population was literate. They knew how to read and write. They were often employed by like kings and lords that were not literate. And their job was to you know, their their job was to read and write and this is not something that everyone knew how to do. >> [snorts] >> The printing press was invented, then there were two more presses and in the 50 years after the first printing press, there was more literature published in Europe than in the thousand years before. And over the same period, the cost of literature, the cost of a book went down like a 100x. And then, you know, it took 

a couple hundred years cuz you know, learning to read and write is hard. You need education systems and government and everyone can't be working on farms and so on. But over the next few hundred years, literacy globally went up to like 70%. And so, you know, now we can all read and write and you don't need a a degree in reading and writing to know how to read and write. Although still there are professional writers and that is a thing that you can do. So, I I think the thing that's about to happen and it's going to be much faster than 50 years is software will be a thing that is fully democratized, that anyone can do. And you know, there's a lot of 

corollaries to this. So, for example, let's say you're writing accounting software. The best person to write accounting software, I think maybe even today, is not an engineer, it's a really good accountant because they know the domain really well and coding is the easy part. It's knowing the domain that's the hard part. And I I think this is just obviously the the future. So, uh one of the things Greg said was that you guys are living in the future a little bit cuz you get to have access to the models and the agents. Claude code 

was an internal tool before you released it. Um is the gap between where you guys are in engineering and the rest of the world, is that a month? Is it 3 months? Is it 6 months? And is that is that gap getting bigger or smaller over time? Yeah, so so internally, we use the same models everyone else does. Um for us, the dog fooding is really really important. So, we use the thing that everyone else here does. Um you know, we use like a little bit of mythos to try it and then we use a lot of Opus 4.7 to to dog food it and to write most of our code. Um I think on the model side, there 

isn't really a gap. Um you know, it's like it's pretty much mythos and you know, that will become some version of some descendant of that will become available at some point to everyone. I think on the product side, there's probably a far larger gap. And that's just related to us changing all of our processes. Like if you talk to people at Anthropic, we use Claude for literally everything. And our Claudes are talking all day like as as I'm coding, as my Claudes are coding in a loop, they will communicate over Slack to talk to other people's Claudes that are also running in a loop to kind of figure out unknowns. 

We have no more manually written code anywhere at the company. All of the SQL is written by uh by models. Everything is just built by the models. So, I I I think actually the place that we're ahead is not the technology cuz the same technology available to us is available to everyone here because fundamentally, we are building a platform. And so, for us, it's really important that developers can use the same thing that we're using and that we we dog food everything that we put out there. But I think there's actually a far bigger weed in kind of the organizational structure and organizational process. And this is a place where you know, hopefully we can 

talk about it in places like this and uh everyone can kind of learn from it and and also evolve. Yeah, and I think that's one of the advantages startups have. It's so much easier to start there. Jared? Yeah, um last time we talked, I think I think you'd mentioned we talked a little bit about multi-agent and it was very in code at the time at a prior Sequoia event and you mentioned that there were some things going down the pipeline and thing you're talking you're thinking about. Now obviously there's slash batch, there's slash loop, there's sub teams, there's teams. Can you speak some to either at the model level and at the 

harness level, how you're injecting priors in the harness level, how the objective function is changing the model level to kind of make this experience around delegating work, spinning up agents better? Cuz so much of the work is parallelizable. You can do so many things so much faster and I feel like I have to overlay my own intuition for when to parallelize things rather than the model kind of understanding that you can spin up 10 sub agents for something. Yeah, I mean on on the product side, it really just comes down to prompting. That's That's how it is. And so, you know, we we tweak prompts to kind of help the model do stuff in parallel more. But also, honestly, as the model gets 

better, it just naturally does this. And so, something like loop, I found actually 4.7, it just starts doing. Uh which is really cool. It's like it does something like uh you know, I'll I'll I'll tell it, "Go uh pull this data query." And it's like, "Hey, I noticed that the data is changing over time. I'll start a loop and I'll give you a report every 30 minutes." And I'm like, "Great. Can you send it to me over Slack?" And then it uses the Slack MCP to do that. So, so I think actually over time, it's not on users to figure out how to hold the tools better. And if that's the case, it's actually a product design problem 

and like I'm not doing a good job. It's really on the model to do this stuff better and on us kind of prompting it so it naturally does this. Um so, right now it seems like a lot of us use um like Claude or Codex or these uh tools in the cloud to do a lot of our computing. But then, there are some very vocal advocates of uh having your AI be local. And I could imagine over time as um open way models and other things catch up that this could be more of a 

possibility for people get really high-quality coding assistance. So, I'm curious your vision of say over the next like years or something like that. Do you see the trajectory of everyone still really relying on the like cloud centralized compute or uh is there a pivot to oh, we all just have our local agents that we can rely on and they don't get throttled and other benefits? Yeah, I think it um I don't know. There's maybe a few ways to answer that. I think maybe like kind of the the most fundamental way to 

answer that is it doesn't matter. Cuz Cuz I think now we're getting to the point where the model is just able to figure it out. So, I think like by a couple years from now, the model is just going to be doing all the code. It's going to be starting the agents. It's going to be building the environments. And so, like if it decides like actually I'll use like local models to do this, then you know, that's what it'll do. These I I don't think these will be decisions that we are making as engineers anymore. We have time for a couple more questions, so I can toss this out. Jamie. Nester. Thank you. It feels like one of the great uh 

decisions with Claude Code was making use of the fact that a lot of developers' tools and workflows are local. But um that isn't necessarily always the case for sort of general knowledge work with, you know, cloud tools. I'm curious how you're thinking about this with Co-work of how do you give Co-work enough access to the tools that we use to be powerful the same way that Claude Code is for developers? Yeah, it's That's a really great question. Um I know I know when I was uh when I was at a big company, we took like 5 years moving all the environments to remote. It's just like so much work, 

especially at a big scale. Um but for knowledge work, largely, it's there already with like Salesforce and Docs and things like that. Um for us, it's always just the simplest answer. It's just MCP. So, the same MCP connector that you have in Claude AI, you hook up like, you know, Salesforce, you hook up Google Docs, Google Calendar. Uh and then Co-work can use that. Claude CLI can use it. Claude Code everywhere can use it. And for the for the systems that don't have MCPs, like do you think that's where computer use is going to be a big 

opportunity? Yeah, I think computer use is kind of a catchall. Um so, I think currently, for as far as I know, I think Anthropic is like pretty far ahead on computers. And so, like if you use it through Co-work, it's quite good. Um so, it's able to use pretty much any piece of software that you have on your computer. It's very slow, but it does it quite well now, especially with 4.7. Um Yeah, but I think I think otherwise like MCP is is kind of the answer. It's And you know, all this stuff just doesn't matter that much. It could be MCPs, APIs, just some sort of programmatic access cuz the the model 

doesn't care. It's to mo- To the model, it's just tokens. All right, we have time for one more question. Um Ryan. Sean, do you want to toss the Thank you. Um you've kind of alluded to this, but if like sometime ago you saw the probabil- the product overhang and thought to build a product that would then become more interesting once models got better, could you just talk even in vague terms about the shape of a product you'd build today that you think could becomes a much more interesting as models get 

better in 6 months to a year? Yeah, Claude design I I think is a really good example. It's uh it's pretty good today. It's going to get a lot better. Um there's also a few things that we're cooking up for Claude Code uh that are going to be landing over the coming weeks. So, you'll see those. Um and then I think uh I think loop and batch and things like this around like massively parallelizing agents, that's going to get better. And computer use is another good one. All right, Boris. Thank you so much for joining us. I think we'll be here for a little longer if anyone has questions. 

>> [applause] >> Thanks, guys. 

<p>
 <span data-rw-start="2" data-rw-transcript-version="2">
 Okay, I'm excited to introduce our next
 </span>
 <span data-rw-start="3.72" data-rw-transcript-version="2">
 speaker. Show of hands, who here uses
 </span>
 <span data-rw-start="5.48" data-rw-transcript-version="2">
 Claude code?
 </span>
 <span data-rw-start="7.56" data-rw-transcript-version="2">
 Okay, show of hands, who here has Claude
 </span>
 <span data-rw-start="9.2" data-rw-transcript-version="2">
 code psychosis?
 </span>
 <span data-rw-start="11.44" data-rw-transcript-version="2">
 Come on, guys, [clears throat] it's okay.
 </span>
 <span data-rw-start="12.36" data-rw-transcript-version="2">
 It's okay. Um, my team lovingly
 </span>
 <span data-rw-start="14.76" data-rw-transcript-version="2">
 says I have Claude code psychosis, which
 </span>
 <span data-rw-start="16.36" data-rw-transcript-version="2">
 may or may not be true.
 </span>
 <span data-rw-start="18.16" data-rw-transcript-version="2">
 Um, we are
 </span>
 <span data-rw-start="19.8" data-rw-transcript-version="2">
 delighted to have Boris Cherny with us
 </span>
 <span data-rw-start="22.32" data-rw-transcript-version="2">
 today. Uh, Boris is the creator, the
 </span>
 <span data-rw-start="25.32" data-rw-transcript-version="2">
 father of Claude code. Um, and in the
 </span>
 <span data-rw-start="26.64" data-rw-transcript-version="2">
 process of doing that, he has just had a
 </span>
 <span data-rw-start="29.72" data-rw-transcript-version="2">
 front-row seat to reinventing the
 </span>
 <span data-rw-start="32.439" data-rw-transcript-version="2">
 modern way of software development.
 </span>
 <span data-rw-start="34.12" data-rw-transcript-version="2">
 Um, and we're really grateful to
 </span>
 <span data-rw-start="35.52" data-rw-transcript-version="2">
 you, Boris, for taking the time to speak
 </span>
 <span data-rw-start="38.08" data-rw-transcript-version="2">
 with us today. We know that the
 </span>
 <span data-rw-start="39.92" data-rw-transcript-version="2">
 entirety of software development kind of
 </span>
 <span data-rw-start="41.16" data-rw-transcript-version="2">
 rests on your shoulders. So, thank you
 </span>
 <span data-rw-start="42.36" data-rw-transcript-version="2">
 for taking the time out of your schedule to be
 </span>
 <span data-rw-start="44.12" data-rw-transcript-version="2">
 with us today. And interviewing Boris is
 </span>
 <span data-rw-start="45.88" data-rw-transcript-version="2">
 Lauren Reader from our team.
 </span>
 <span data-rw-start="45.88" data-rw-transcript-version="2">
 Thank you.
 </span>
</p>
<p>
 <span data-rw-start="48.47" data-rw-transcript-version="2">
 &gt;&gt; [applause]
 </span>
 <span data-rw-start="52.36" data-rw-transcript-version="2">
 &gt;&gt; Giving our chairs.
 </span>
</p>
<p>
 <span data-rw-start="55.36" data-rw-transcript-version="2">
 Um, you took my opening line,
 </span>
 <span data-rw-start="57.32" data-rw-transcript-version="2">
 Asia. We asked who here uses Claude
 </span>
 <span data-rw-start="58.72" data-rw-transcript-version="2">
 code. There's a lot of hands. That's
 </span>
 <span data-rw-start="60.36" data-rw-transcript-version="2">
 awesome.
 </span>
 <span data-rw-start="61.84" data-rw-transcript-version="2">
 Thank you for joining us, Boris. It's
 </span>
 <span data-rw-start="63.2" data-rw-transcript-version="2">
 very special to have you here. Um,
 </span>
 <span data-rw-start="66.16" data-rw-transcript-version="2">
 as a roomful of builders, I think you
 </span>
 <span data-rw-start="68.8" data-rw-transcript-version="2">
 are changing building entirely. And so,
 </span>
 <span data-rw-start="71.24" data-rw-transcript-version="2">
 I'm very curious to explore how you
 </span>
 <span data-rw-start="73.08" data-rw-transcript-version="2">
 think about the future of software,
 </span>
 <span data-rw-start="74.84" data-rw-transcript-version="2">
 coding, and what we should spend all of
 </span>
 <span data-rw-start="77.2" data-rw-transcript-version="2">
 our free time on. Um, but I'll give you a
 </span>
 <span data-rw-start="80.12" data-rw-transcript-version="2">
 me a tiny bit more background on you so
 </span>
 <span data-rw-start="81.6" data-rw-transcript-version="2">
 that everyone has a little bit more
 </span>
 <span data-rw-start="82.92" data-rw-transcript-version="2">
 context. So, beyond creating Claude
 </span>
</p>
<p>
 <span data-rw-start="84.48" data-rw-transcript-version="2">
 code, Boris is very much an engineer's
 </span>
 <span data-rw-start="86.96" data-rw-transcript-version="2">
 engineer. You were writing a lot of code
 </span>
 <span data-rw-start="90.08" data-rw-transcript-version="2">
 through your whole career, writing
 </span>
 <span data-rw-start="91.32" data-rw-transcript-version="2">
 textbooks about code, including
 </span>
 <span data-rw-start="93.76" data-rw-transcript-version="2">
 programming in TypeScript. Um, and I
 </span>
 <span data-rw-start="96.64" data-rw-transcript-version="2">
 think last time we chatted you hadn't
 </span>
 <span data-rw-start="98.04" data-rw-transcript-version="2">
 written a single line of code in the
 </span>
 <span data-rw-start="99.4" data-rw-transcript-version="2">
 last year, or at least so far in 2026,
 </span>
 <span data-rw-start="102.16" data-rw-transcript-version="2">
 which is quite the change. Um, there's
 </span>
 <span data-rw-start="105.36" data-rw-transcript-version="2">
 Also, a little known thing back in
 </span>
 <span data-rw-start="107.04" data-rw-transcript-version="2">
 middle school, I wrote a guide about uh
 </span>
 <span data-rw-start="109" data-rw-transcript-version="2">
 writing BASIC for TI-83 Plus
 </span>
 <span data-rw-start="110.76" data-rw-transcript-version="2">
 calculators.
 </span>
</p>
<p>
 <span data-rw-start="112.52" data-rw-transcript-version="2">
 And I, I just, I searched for it, it's
 </span>
 <span data-rw-start="114.4" data-rw-transcript-version="2">
 actually still on the internet. It's
 </span>
 <span data-rw-start="115.52" data-rw-transcript-version="2">
 extremely embarrassing, so please don't
 </span>
 <span data-rw-start="116.84" data-rw-transcript-version="2">
 search it. But it [laughter] exists. We
 </span>
 <span data-rw-start="118.96" data-rw-transcript-version="2">
 will definitely be finding that. Um, so,
 </span>
 <span data-rw-start="121.4" data-rw-transcript-version="2">
 we're going to do, I’m going to start
 </span>
 <span data-rw-start="122.68" data-rw-transcript-version="2">
 with a few questions here. Maybe we'll
 </span>
 <span data-rw-start="123.96" data-rw-transcript-version="2">
 start with a little bit of the history
 </span>
 <span data-rw-start="125.44" data-rw-transcript-version="2">
 of Claude code, how you started it, and
 </span>
 <span data-rw-start="127.44" data-rw-transcript-version="2">
 then we're going to have a lot of
 </span>
 <span data-rw-start="128.119" data-rw-transcript-version="2">
 audience Q&amp;A for this one. And so, start
 </span>
 <span data-rw-start="130.039" data-rw-transcript-version="2">
 thinking about your questions in the
 </span>
 <span data-rw-start="131.24" data-rw-transcript-version="2">
 back of your head, uh, and would love to
 </span>
 <span data-rw-start="133.32" data-rw-transcript-version="2">
 turn it over to you all soon.
 </span>
</p>
<p>
 <span data-rw-start="135.28" data-rw-transcript-version="2">
 Yeah. Um, and also, real quick, so for
 </span>
 <span data-rw-start="137.6" data-rw-transcript-version="2">
 people that use Claude code, do people
 </span>
 <span data-rw-start="138.96" data-rw-transcript-version="2">
 use the CLI mostly? Like, okay, majority
 </span>
 <span data-rw-start="141.28" data-rw-transcript-version="2">
 CLI?
 </span>
 <span data-rw-start="143.12" data-rw-transcript-version="2">
 Okay. That's a lot. Majority desktop?
 </span>
</p>
<p>
 <span data-rw-start="146.72" data-rw-transcript-version="2">
 Okay. Majority VS code or JetBrains IDE?
 </span>
 <span data-rw-start="150.52" data-rw-transcript-version="2">
 Okay. That's actually not a lot. Okay.
 </span>
</p>
<p>
 <span data-rw-start="152.6" data-rw-transcript-version="2">
 Other?
 </span>
 <span data-rw-start="154.36" data-rw-transcript-version="2">
 I'm like iOS mostly these days. Yeah.
 </span>
 <span data-rw-start="157.201" data-rw-transcript-version="2">
 &gt;&gt; [laughter]
 </span>
 <span data-rw-start="157.8" data-rw-transcript-version="2">
 &gt;&gt; Okay. Cool.
 </span>
 <span data-rw-start="159.28" data-rw-transcript-version="2">
 Um yeah, so I started Claude code kind of accidentally in a lot of ways.
 </span>
 <span data-rw-start="164.28" data-rw-transcript-version="2">
 Um, I joined this team back in late 2024.
 </span>
 <span data-rw-start="167.48" data-rw-transcript-version="2">
 It was a sort of this incubator within Anthropic called Anthropic Labs.
 </span>
 <span data-rw-start="171.4" data-rw-transcript-version="2">
 And, uh, the team kind of served its purpose.
 </span>
</p>
<p>
 <span data-rw-start="172.96" data-rw-transcript-version="2">
 Um, we created Claude code, MCP, and the desktop app.
 </span>
 <span data-rw-start="175.48" data-rw-transcript-version="2">
 It was a team that was just a few of us.
 </span>
 <span data-rw-start="177.48" data-rw-transcript-version="2">
 So, very much like an innovation team.
 </span>
 <span data-rw-start="179.12" data-rw-transcript-version="2">
 We built the thing that we wanted to build,
 </span>
 <span data-rw-start="182.72" data-rw-transcript-version="2">
 we disbanded the team.
 </span>
</p>
<p>
 <span data-rw-start="184.84" data-rw-transcript-version="2">
 Uh, now the team's actually back together for round two.
 </span>
 <span data-rw-start="186.16" data-rw-transcript-version="2">
 Mike Krieger, who's the, you know,
 </span>
 <span data-rw-start="188.2" data-rw-transcript-version="2">
 like the chief product officer at Anthropic,
 </span>
 <span data-rw-start="190" data-rw-transcript-version="2">
 and used to be one of the founders at Instagram,
 </span>
 <span data-rw-start="191.68" data-rw-transcript-version="2">
 so he's leading that right now.
 </span>
</p>
<p>
 <span data-rw-start="194.92" data-rw-transcript-version="2">
 Um, so, the kind of the reason that I started to work on coding is we felt like there was this product.
 </span>
</p>
<p>
 <span data-rw-start="202.36" data-rw-transcript-version="2">
 Overhang. And I, I'm guessing people here
 </span>
 <span data-rw-start="205.32" data-rw-transcript-version="2">
 use that word a lot. Uh, but we
 </span>
 <span data-rw-start="207.52" data-rw-transcript-version="2">
 definitely use this word a lot in kind
 </span>
 <span data-rw-start="209.44" data-rw-transcript-version="2">
 of within the lab.
 </span>
 <span data-rw-start="210.96" data-rw-transcript-version="2">
 Uh, there's this idea that the model can
 </span>
 <span data-rw-start="212.64" data-rw-transcript-version="2">
 do all the stuff that no product has yet
 </span>
 <span data-rw-start="214.6" data-rw-transcript-version="2">
 captured. And in late 2024, when we were
 </span>
 <span data-rw-start="217.52" data-rw-transcript-version="2">
 looking at coding, the way that we did
 </span>
 <span data-rw-start="219.08" data-rw-transcript-version="2">
 coding, the state of the art at the time
 </span>
 <span data-rw-start="220.44" data-rw-transcript-version="2">
 was type ahead. It was you open your IDE
 </span>
 <span data-rw-start="222.32" data-rw-transcript-version="2">
 and you press tab, and you can like
 </span>
 <span data-rw-start="223.56" data-rw-transcript-version="2">
 complete like one line at a time. And
 </span>
 <span data-rw-start="226.08" data-rw-transcript-version="2">
 that was the thing that Sonnet 3.5
 </span>
 <span data-rw-start="227.44" data-rw-transcript-version="2">
 enabled for the first time. But the
 </span>
 <span data-rw-start="229.48" data-rw-transcript-version="2">
 feeling was, we could actually go a lot
 </span>
 <span data-rw-start="230.72" data-rw-transcript-version="2">
 further than that. And the model was
 </span>
 <span data-rw-start="232.72" data-rw-transcript-version="2">
 almost ready for the next big step. So,
 </span>
 <span data-rw-start="235.44" data-rw-transcript-version="2">
 we don't have to do type ahead anymore,
 </span>
 <span data-rw-start="236.96" data-rw-transcript-version="2">
 we can just have the agent write all of
 </span>
 <span data-rw-start="238.72" data-rw-transcript-version="2">
 the code.
 </span>
</p>
<p>
 <span data-rw-start="240.8" data-rw-transcript-version="2">
 And so, I built it, and it just really
 </span>
 <span data-rw-start="244.32" data-rw-transcript-version="2">
 didn't work for the first 6 months. It
 </span>
 <span data-rw-start="246.52" data-rw-transcript-version="2">
 was like not very good. It was barely
 </span>
 <span data-rw-start="247.88" data-rw-transcript-version="2">
 usable. I wrote it from, I used it for
 </span>
 <span data-rw-start="249.8" data-rw-transcript-version="2">
 maybe 10% of my code or something like that.
 </span>
</p>
<p>
 <span data-rw-start="251.92" data-rw-transcript-version="2">
 That. And even after we released Claude
 </span>
 <span data-rw-start="253.72" data-rw-transcript-version="2">
 code initially, it was not a hit.
 </span>
 <span data-rw-start="256.16" data-rw-transcript-version="2">
 There's a lot of people that used it,
 </span>
 <span data-rw-start="257.56" data-rw-transcript-version="2">
 but it did not have this exponential
 </span>
 <span data-rw-start="259.48" data-rw-transcript-version="2">
 growth that it has today.
 </span>
 <span data-rw-start="261.359" data-rw-transcript-version="2">
 Um, that started with Opus 4 in May. And
 </span>
 <span data-rw-start="264.16" data-rw-transcript-version="2">
 I, I remember that very clearly. That's
 </span>
 <span data-rw-start="265.56" data-rw-transcript-version="2">
 like when the exponential growth
 </span>
 <span data-rw-start="266.52" data-rw-transcript-version="2">
 started, and then it kind of inflected
 </span>
 <span data-rw-start="268.04" data-rw-transcript-version="2">
 with every model release. Uh, like it
 </span>
 <span data-rw-start="270.36" data-rw-transcript-version="2">
 started with Opus 4, then 4.5, then 4.6,
 </span>
 <span data-rw-start="272.56" data-rw-transcript-version="2">
 now 4.7. It just kind of keeps
 </span>
 <span data-rw-start="274.48" data-rw-transcript-version="2">
 inflecting.
 </span>
</p>
<p>
 <span data-rw-start="276.88" data-rw-transcript-version="2">
 But, essentially, we were trying to build
 </span>
 <span data-rw-start="278" data-rw-transcript-version="2">
 this thing that was like pre-PMF, and we
 </span>
 <span data-rw-start="280.04" data-rw-transcript-version="2">
 knew that it wouldn't have PMF for 6
 </span>
 <span data-rw-start="281.44" data-rw-transcript-version="2">
 months because we were building for the
 </span>
 <span data-rw-start="283" data-rw-transcript-version="2">
 next model. And that was the idea, the
 </span>
 <span data-rw-start="285" data-rw-transcript-version="2">
 pretty much the whole time.
 </span>
</p>
<p>
 <span data-rw-start="286.68" data-rw-transcript-version="2">
 And, you know, for Anthropic in general,
 </span>
 <span data-rw-start="288.64" data-rw-transcript-version="2">
 we've always just been very focused.
 </span>
 <span data-rw-start="290.28" data-rw-transcript-version="2">
 We've always cared about business and
 </span>
 <span data-rw-start="292.04" data-rw-transcript-version="2">
 enterprise, and safety, and coding. That's
 </span>
 <span data-rw-start="294.36" data-rw-transcript-version="2">
 just always been kind of the way that we
 </span>
 <span data-rw-start="296" data-rw-transcript-version="2">
 wanted to build. And so, at some point,
 </span>
 <span data-rw-start="297.72" data-rw-transcript-version="2">
 We kind of knew that we wanted to build
 </span>
 <span data-rw-start="298.88" data-rw-transcript-version="2">
 a product. We didn't know exactly what
 </span>
 <span data-rw-start="300.12" data-rw-transcript-version="2">
 we wanted. So, this kind of ended up
 </span>
 <span data-rw-start="301.96" data-rw-transcript-version="2">
 being the product bet.
 </span>
</p>
<p>
 <span data-rw-start="304.36" data-rw-transcript-version="2">
 It's an incredible story, especially
 </span>
 <span data-rw-start="305.72" data-rw-transcript-version="2">
 that it was an accident.
 </span>
 <span data-rw-start="307.92" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="309.04" data-rw-transcript-version="2">
 so, you've said on the record that you
 </span>
 <span data-rw-start="310.64" data-rw-transcript-version="2">
 think coding is solved. Uh, if this is
 </span>
 <span data-rw-start="312.92" data-rw-transcript-version="2">
 one of the three best from Anthropic,
 </span>
 <span data-rw-start="314.08" data-rw-transcript-version="2">
 can you tell us more about what you mean
 </span>
 <span data-rw-start="315.44" data-rw-transcript-version="2">
 by that, and what might still not be
 </span>
 <span data-rw-start="317.52" data-rw-transcript-version="2">
 solved, or what second-order problems
 </span>
 <span data-rw-start="319.24" data-rw-transcript-version="2">
 might come? All right. I can ask another
 </span>
 <span data-rw-start="321.28" data-rw-transcript-version="2">
 question for the room. Who writes 100%
 </span>
 <span data-rw-start="323.28" data-rw-transcript-version="2">
 of their code by hand?
 </span>
 <span data-rw-start="327.52" data-rw-transcript-version="2">
 Who writes 100% of their code using an
 </span>
 <span data-rw-start="329.8" data-rw-transcript-version="2">
 agent like Claude code?
 </span>
 <span data-rw-start="332.32" data-rw-transcript-version="2">
 Okay. Who's like somewhere in between?
 </span>
 <span data-rw-start="335.36" data-rw-transcript-version="2">
 Okay. So, like 50% solved.
 </span>
 <span data-rw-start="338.638" data-rw-transcript-version="2">
 &gt;&gt; [laughter]
 </span>
 <span data-rw-start="341.16" data-rw-transcript-version="2">
 &gt;&gt; I mean, for me it's like, for
 </span>
 <span data-rw-start="342.52" data-rw-transcript-version="2">
 me, it's 100%. Like the Claude code
 </span>
 <span data-rw-start="344.36" data-rw-transcript-version="2">
 base, um, you know, it leaked, so
 </span>
 <span data-rw-start="346.36" data-rw-transcript-version="2">
 you know, people know. Uh, it's pretty.
 </span>
</p>
<p>
 <span data-rw-start="348.12" data-rw-transcript-version="2">
 Simple. It's just like TypeScript and
 </span>
 <span data-rw-start="349.76" data-rw-transcript-version="2">
 it's React. Like there's no big secret.
 </span>
 <span data-rw-start="351.56" data-rw-transcript-version="2">
 There's nothing really
 </span>
 <span data-rw-start="352.48" data-rw-transcript-version="2">
 complicated. The reason we picked
 </span>
 <span data-rw-start="354.68" data-rw-transcript-version="2">
 TypeScript and React is it's very on
 </span>
 <span data-rw-start="356.24" data-rw-transcript-version="2">
 distribution for the model. So, when we
 </span>
 <span data-rw-start="358" data-rw-transcript-version="2">
 started, you know, building the code
 </span>
 <span data-rw-start="359.48" data-rw-transcript-version="2">
 base, the model was not as intelligent
 </span>
 <span data-rw-start="361.08" data-rw-transcript-version="2">
 as it is today, so the language and the
 </span>
 <span data-rw-start="362.84" data-rw-transcript-version="2">
 framework mattered a lot. Nowadays, you
 </span>
 <span data-rw-start="364.88" data-rw-transcript-version="2">
 know, it can write whatever, and it can
 </span>
 <span data-rw-start="366.32" data-rw-transcript-version="2">
 pick up new languages, new frameworks it
 </span>
 <span data-rw-start="367.8" data-rw-transcript-version="2">
 hasn't seen. But back then, you wanted
 </span>
 <span data-rw-start="369.72" data-rw-transcript-version="2">
 to use something pretty on distribution.
 </span>
</p>
<p>
 <span data-rw-start="372.24" data-rw-transcript-version="2">
 Because of that, I think fairly early we
 </span>
 <span data-rw-start="374.52" data-rw-transcript-version="2">
 got to the point where the model just
 </span>
 <span data-rw-start="375.68" data-rw-transcript-version="2">
 wrote 100% of the code. And for us, this
 </span>
 <span data-rw-start="378.52" data-rw-transcript-version="2">
 happened sometime in October, November
 </span>
 <span data-rw-start="380.4" data-rw-transcript-version="2">
 last year.
 </span>
 <span data-rw-start="381.56" data-rw-transcript-version="2">
 And so, for me today, you know, like the
 </span>
 <span data-rw-start="383.32" data-rw-transcript-version="2">
 model writes 100% of my code. I write
 </span>
 <span data-rw-start="385.72" data-rw-transcript-version="2">
 somewhere, you know, usually a few dozen
 </span>
 <span data-rw-start="387.12" data-rw-transcript-version="2">
 PRs every day.
 </span>
 <span data-rw-start="388.56" data-rw-transcript-version="2">
 Uh, there was a day last week I did like
 </span>
 <span data-rw-start="389.8" data-rw-transcript-version="2">
 150 PRs in a day. That was like, that was
 </span>
 <span data-rw-start="392.04" data-rw-transcript-version="2">
 A record. I was just trying to kind of
 </span>
 <span data-rw-start="393.12" data-rw-transcript-version="2">
 push to see how far I can get it.
 </span>
</p>
<p>
 <span data-rw-start="395.12" data-rw-transcript-version="2">
 Um, but yeah, it's like for me, for me
 </span>
 <span data-rw-start="396.52" data-rw-transcript-version="2">
 it's just solved. Um, but this is not the
 </span>
 <span data-rw-start="398.16" data-rw-transcript-version="2">
 case everywhere. There are very big
 </span>
 <span data-rw-start="400" data-rw-transcript-version="2">
 complicated code bases. There's kind of
 </span>
 <span data-rw-start="402.04" data-rw-transcript-version="2">
 weird languages, the model's not good at
 </span>
 <span data-rw-start="403.52" data-rw-transcript-version="2">
 yet. Um, and you know, as everyone here
 </span>
 <span data-rw-start="405.36" data-rw-transcript-version="2">
 knows, it's getting there. Usually
 </span>
 <span data-rw-start="407.44" data-rw-transcript-version="2">
 the answer is just wait for the next
 </span>
 <span data-rw-start="408.6" data-rw-transcript-version="2">
 model.
 </span>
</p>
<p>
 <span data-rw-start="410.08" data-rw-transcript-version="2">
 Can you actually tell us about your
 </span>
 <span data-rw-start="411.28" data-rw-transcript-version="2">
 personal setup? You walked us through it
 </span>
 <span data-rw-start="413.04" data-rw-transcript-version="2">
 the other day. It is pretty wild.
 </span>
</p>
<p>
 <span data-rw-start="415.76" data-rw-transcript-version="2">
 Yeah. Um, so, I shared my personal setup
 </span>
 <span data-rw-start="418.48" data-rw-transcript-version="2">
 like six months ago or something on Twitter. And it it's funny, I actually, I
 </span>
 <span data-rw-start="421.08" data-rw-transcript-version="2">
 shared it, I didn't realize that it would
 </span>
 <span data-rw-start="422.64" data-rw-transcript-version="2">
 be surprising for anyone. That was just
 </span>
 <span data-rw-start="424.24" data-rw-transcript-version="2">
 like the way that I coded.
 </span>
</p>
<p>
 <span data-rw-start="427.719" data-rw-transcript-version="2">
 &gt;&gt; [laughter]
 </span>
 <span data-rw-start="428.36" data-rw-transcript-version="2">
 &gt;&gt; And it's changed since then. It's
 </span>
 <span data-rw-start="429.88" data-rw-transcript-version="2">
 changed. Um, and so, now actually most of
 </span>
 <span data-rw-start="432.4" data-rw-transcript-version="2">
 my work I do from my phone.
 </span>
</p>
<p>
 <span data-rw-start="436.76" data-rw-transcript-version="2">
 I don't know if like you guys won't be
 </span>
 <span data-rw-start="437.84" data-rw-transcript-version="2">
 able to see this, but I have, um,
 </span>
 <span data-rw-start="440.68" data-rw-transcript-version="2">
 so, I have like the Claude app, and if
 </span>
 <span data-rw-start="443.08" data-rw-transcript-version="2">
 you open the Claude app,
 </span>
 <span data-rw-start="445.12" data-rw-transcript-version="2">
 on the left-hand side, there's this
 </span>
 <span data-rw-start="446.4" data-rw-transcript-version="2">
 little code tab,
 </span>
 <span data-rw-start="448.16" data-rw-transcript-version="2">
 and I just have a bunch of sessions
 </span>
 <span data-rw-start="449.48" data-rw-transcript-version="2">
 going.
 </span>
 <span data-rw-start="451.08" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="452.08" data-rw-transcript-version="2">
 you probably can't see it.
 </span>
 <span data-rw-start="453.2" data-rw-transcript-version="2">
 &gt;&gt; How many sessions?
 </span>
 <span data-rw-start="454.76" data-rw-transcript-version="2">
 Uh, usually I have like maybe five to
 </span>
 <span data-rw-start="456.84" data-rw-transcript-version="2">
 10 sessions. Uh, and then the sessions
 </span>
 <span data-rw-start="458.72" data-rw-transcript-version="2">
 usually have a bunch of agents, so I
 </span>
 <span data-rw-start="460.64" data-rw-transcript-version="2">
 think, currently probably like a few
 </span>
 <span data-rw-start="461.72" data-rw-transcript-version="2">
 hundred agents going.
 </span>
 <span data-rw-start="463.32" data-rw-transcript-version="2">
 Um, usually every night I have like a few
 </span>
 <span data-rw-start="464.92" data-rw-transcript-version="2">
 thousand that are doing kind of deeper
 </span>
 <span data-rw-start="466.48" data-rw-transcript-version="2">
 work. There are a few ways to manage it.
 </span>
 <span data-rw-start="468.92" data-rw-transcript-version="2">
 One is that you ask Claude to use a
 </span>
 <span data-rw-start="470.52" data-rw-transcript-version="2">
 bunch of sub-agents to do work.
 </span>
 <span data-rw-start="472.52" data-rw-transcript-version="2">
 Actually, the thing that I've been
 </span>
 <span data-rw-start="474.72" data-rw-transcript-version="2">
 finding myself using more and more is
 </span>
 <span data-rw-start="476.64" data-rw-transcript-version="2">
 the loop. So, this is {slash} loop, and
 </span>
 <span data-rw-start="479.84" data-rw-transcript-version="2">
 it's just like the coolest thing. It's
 </span>
 <span data-rw-start="480.88" data-rw-transcript-version="2">
 Like the simplest thing that works. All
 </span>
 <span data-rw-start="482.76" data-rw-transcript-version="2">
 it is, is you have Claude use cron to
 </span>
 <span data-rw-start="485.96" data-rw-transcript-version="2">
 schedule a job for some point in the
 </span>
 <span data-rw-start="487.72" data-rw-transcript-version="2">
 future, and it's a repeat job.
 </span>
</p>
<p>
 <span data-rw-start="489.48" data-rw-transcript-version="2">
 And it can run every, every minute, every
 </span>
 <span data-rw-start="491.44" data-rw-transcript-version="2">
 5 minutes, every day, kind of however
 </span>
 <span data-rw-start="493.4" data-rw-transcript-version="2">
 often you want to schedule it.
 </span>
 <span data-rw-start="495.64" data-rw-transcript-version="2">
 And at [snorts], this point, I have like
 </span>
 <span data-rw-start="496.64" data-rw-transcript-version="2">
 dozens of loops that are running for
 </span>
 <span data-rw-start="498.12" data-rw-transcript-version="2">
 stuff. So, I have one that's babysitting
 </span>
 <span data-rw-start="500" data-rw-transcript-version="2">
 my PRs, like fixing CI, auto-rebasing. I
 </span>
 <span data-rw-start="503.08" data-rw-transcript-version="2">
 have another one that keeps CI healthy.
 </span>
</p>
<p>
 <span data-rw-start="504.8" data-rw-transcript-version="2">
 So, like if there's like a flaky test or
 </span>
 <span data-rw-start="506.28" data-rw-transcript-version="2">
 whatever, it'll go and fix it. Um,
 </span>
 <span data-rw-start="508.84" data-rw-transcript-version="2">
 I have another one that grabs, uh,
 </span>
 <span data-rw-start="510.36" data-rw-transcript-version="2">
 feedback from Twitter and kind of
 </span>
 <span data-rw-start="511.84" data-rw-transcript-version="2">
 clusters it for me every 30 minutes. So,
 </span>
 <span data-rw-start="514.28" data-rw-transcript-version="2">
 I just have a bunch of these loops
 </span>
 <span data-rw-start="515.68" data-rw-transcript-version="2">
 running at any time. I sort of feel like
 </span>
 <span data-rw-start="517.68" data-rw-transcript-version="2">
 loops are the future at this point. If
 </span>
 <span data-rw-start="519.52" data-rw-transcript-version="2">
 you haven't experimented with it, highly
 </span>
 <span data-rw-start="520.919" data-rw-transcript-version="2">
 highly recommend it. And we also just
 </span>
 <span data-rw-start="522.919" data-rw-transcript-version="2">
 launched routines, which is the same
 </span>
 <span data-rw-start="524.68" data-rw-transcript-version="2">
 thing but kind of on the server. So,
 </span>
 <span data-rw-start="526.72" data-rw-transcript-version="2">
 even if you close your laptop, it, it
 </span>
 <span data-rw-start="528.24" data-rw-transcript-version="2">
 Keeps going.
 </span>
</p>
<p>
 <span data-rw-start="530.28" data-rw-transcript-version="2">
 So, that's your personal setup. Tell us
 </span>
 <span data-rw-start="531.92" data-rw-transcript-version="2">
 about what you think teams will look
 </span>
 <span data-rw-start="533.52" data-rw-transcript-version="2">
 like in the future. How do you
 </span>
 <span data-rw-start="535.24" data-rw-transcript-version="2">
 extrapolate from all the work you're
 </span>
 <span data-rw-start="536.4" data-rw-transcript-version="2">
 doing to keep everyone on the team
 </span>
 <span data-rw-start="538.36" data-rw-transcript-version="2">
 moving forward, understanding the
 </span>
 <span data-rw-start="539.64" data-rw-transcript-version="2">
 context, or do you think we need to let
 </span>
 <span data-rw-start="541.08" data-rw-transcript-version="2">
 go of a lot more to agents to make it
 </span>
 <span data-rw-start="543.24" data-rw-transcript-version="2">
 work?
 </span>
 <span data-rw-start="544.68" data-rw-transcript-version="2">
 Um, I think so. I, you know, it's like it's
 </span>
 <span data-rw-start="546.72" data-rw-transcript-version="2">
 so hard to make predictions, but, um
 </span>
 <span data-rw-start="549.32" data-rw-transcript-version="2">
 I'm here to make predictions, so I'll
 </span>
 <span data-rw-start="550.6" data-rw-transcript-version="2">
 try to make some.
 </span>
 <span data-rw-start="552.36" data-rw-transcript-version="2">
 I feel like the way that things are
 </span>
 <span data-rw-start="554" data-rw-transcript-version="2">
 going is generally there's going to be a
 </span>
 <span data-rw-start="556.96" data-rw-transcript-version="2">
 lot more generalists than there are
 </span>
 <span data-rw-start="558.36" data-rw-transcript-version="2">
 today.
 </span>
 <span data-rw-start="559.4" data-rw-transcript-version="2">
 And
 </span>
 <span data-rw-start="560.4" data-rw-transcript-version="2">
 today, when we talk about generalists, I
 </span>
 <span data-rw-start="562.12" data-rw-transcript-version="2">
 think largely we're talking about people
 </span>
 <span data-rw-start="563.44" data-rw-transcript-version="2">
 that are still engineers. So, they're
 </span>
 <span data-rw-start="565.2" data-rw-transcript-version="2">
 still writing code, but maybe they're
 </span>
 <span data-rw-start="566.6" data-rw-transcript-version="2">
 kind of product engineers. So, maybe
 </span>
 <span data-rw-start="568.6" data-rw-transcript-version="2">
 when we say "generalist," it's like a you
 </span>
 <span data-rw-start="569.92" data-rw-transcript-version="2">
 know, they do iOS and web and server,
 </span>
 <span data-rw-start="571.88" data-rw-transcript-version="2">
 for example. That's like a generalist in
 </span>
 <span data-rw-start="573.28" data-rw-transcript-version="2">
 engineering.
 </span>
</p>
<p>
 <span data-rw-start="575.28" data-rw-transcript-version="2">
 But I think the thing that we're going
 </span>
 <span data-rw-start="576.16" data-rw-transcript-version="2">
 to start to see a lot more of is
 </span>
 <span data-rw-start="578.2" data-rw-transcript-version="2">
 generalists that are cross-disciplinary.
 </span>
 <span data-rw-start="580.72" data-rw-transcript-version="2">
 So, this is engineers that are really
 </span>
 <span data-rw-start="582.12" data-rw-transcript-version="2">
 good at product engineering, but also
 </span>
 <span data-rw-start="583.4" data-rw-transcript-version="2">
 really great at design. Or really great
 </span>
 <span data-rw-start="585.32" data-rw-transcript-version="2">
 at product and data science and
 </span>
 <span data-rw-start="587.16" data-rw-transcript-version="2">
 engineering.
 </span>
</p>
<p>
 <span data-rw-start="588.8" data-rw-transcript-version="2">
 Um
 </span>
 <span data-rw-start="590" data-rw-transcript-version="2">
 I don't know. It's something that
 </span>
 <span data-rw-start="591.08" data-rw-transcript-version="2">
 we're starting to see on our team. So,
 </span>
 <span data-rw-start="592.88" data-rw-transcript-version="2">
 actually, like a lot of people on the
 </span>
 <span data-rw-start="594.36" data-rw-transcript-version="2">
 Claude code team
 </span>
 <span data-rw-start="596.28" data-rw-transcript-version="2">
 are generalists across disciplines.
 </span>
 <span data-rw-start="598.44" data-rw-transcript-version="2">
 Everyone on our team codes. So, like our
 </span>
 <span data-rw-start="600.32" data-rw-transcript-version="2">
 engineering manager, our product
 </span>
 <span data-rw-start="602.12" data-rw-transcript-version="2">
 manager, our designers, our data
 </span>
 <span data-rw-start="605" data-rw-transcript-version="2">
 scientist, our finance guy, our user
 </span>
 <span data-rw-start="607.32" data-rw-transcript-version="2">
 researcher, every single person on our
 </span>
 <span data-rw-start="609.4" data-rw-transcript-version="2">
 team writes code.
 </span>
</p>
<p>
 <span data-rw-start="613.96" data-rw-transcript-version="2">
 Everyone's just coding.
 </span>
 <span data-rw-start="615.32" data-rw-transcript-version="2">
 And you know,
 </span>
 <span data-rw-start="617.12" data-rw-transcript-version="2">
 I'm seeing some nods, but I bet also
 </span>
 <span data-rw-start="618.92" data-rw-transcript-version="2">
 it's actually not that surprising to
 </span>
 <span data-rw-start="620.12" data-rw-transcript-version="2">
 people in this room because I bet you're
 </span>
 <span data-rw-start="621.48" data-rw-transcript-version="2">
 seeing the same things.
 </span>
 <span data-rw-start="623.84" data-rw-transcript-version="2">
 Um [clears throat] I'll have one more
 </span>
 <span data-rw-start="624.8" data-rw-transcript-version="2">
 favorite question, then we'll open up to
 </span>
 <span data-rw-start="625.96" data-rw-transcript-version="2">
 the audience. So, we talked a bit about
 </span>
 <span data-rw-start="627.76" data-rw-transcript-version="2">
 what's changing with coding. I’m curious
 </span>
 <span data-rw-start="630" data-rw-transcript-version="2">
 about what you see changing in the world
 </span>
 <span data-rw-start="631.4" data-rw-transcript-version="2">
 of software or software products.
 </span>
 <span data-rw-start="634.04" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="634.6" data-rw-transcript-version="2">
 I think as we see AI making writing code
 </span>
 <span data-rw-start="636.52" data-rw-transcript-version="2">
 10 or 100 times cheaper,
 </span>
 <span data-rw-start="639.04" data-rw-transcript-version="2">
 what happens to the value of the
 </span>
 <span data-rw-start="640.16" data-rw-transcript-version="2">
 products that are produced with
 </span>
 <span data-rw-start="641.16" data-rw-transcript-version="2">
 software? Do we have a SAS apocalypse on
 </span>
 <span data-rw-start="643.52" data-rw-transcript-version="2">
 our hands? How do you think this plays
 </span>
 <span data-rw-start="645.16" data-rw-transcript-version="2">
 out? And again, you're going to have to
 </span>
 <span data-rw-start="646.48" data-rw-transcript-version="2">
 make another prediction.
 </span>
 <span data-rw-start="648.52" data-rw-transcript-version="2">
 The SAS apocalypse question is my
 </span>
 <span data-rw-start="649.92" data-rw-transcript-version="2">
 favorite question then.
 </span>
 <span data-rw-start="651.96" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="655.12" data-rw-transcript-version="2">
 I think there are two things that are
 </span>
 <span data-rw-start="656.36" data-rw-transcript-version="2">
 Going to happen, and I don't think
 </span>
 <span data-rw-start="657.68" data-rw-transcript-version="2">
 either of them is the thing that people
 </span>
 <span data-rw-start="659.04" data-rw-transcript-version="2">
 have been talking about.
 </span>
</p>
<p>
 <span data-rw-start="661.6" data-rw-transcript-version="2">
 I think one is, is anyone here an
 </span>
 <span data-rw-start="664.76" data-rw-transcript-version="2">
 acquired listener? Like the acquired
 </span>
 <span data-rw-start="666.64" data-rw-transcript-version="2">
 podcast?
 </span>
 <span data-rw-start="668" data-rw-transcript-version="2">
 Yeah, it's like the best podcast.
 </span>
 <span data-rw-start="670.2" data-rw-transcript-version="2">
 Uh, I actually, I got to do an unplugged
 </span>
 <span data-rw-start="672.88" data-rw-transcript-version="2">
 with them the other week, and I just, I
 </span>
 <span data-rw-start="675.08" data-rw-transcript-version="2">
 felt like I got to meet my heroes because they're just like the hosts are the best.
 </span>
</p>
<p>
 <span data-rw-start="680" data-rw-transcript-version="2">
 So, they have this idea of, uh, seven
 </span>
 <span data-rw-start="681.72" data-rw-transcript-version="2">
 powers, and this is a, this is like
 </span>
 <span data-rw-start="683.36" data-rw-transcript-version="2">
 Hamilton. He kind of wrote, he wrote a
 </span>
 <span data-rw-start="684.68" data-rw-transcript-version="2">
 book about this, and this is kind of the
 </span>
 <span data-rw-start="685.88" data-rw-transcript-version="2">
 seven modes in business. And I think
 </span>
 <span data-rw-start="688.12" data-rw-transcript-version="2">
 what's going to happen is because of AI,
 </span>
 <span data-rw-start="689.88" data-rw-transcript-version="2">
 some of these modes are going to get
 </span>
 <span data-rw-start="690.92" data-rw-transcript-version="2">
 more important, and some are going to get
 </span>
 <span data-rw-start="692.36" data-rw-transcript-version="2">
 less important. And so, like, for
 </span>
 <span data-rw-start="694.28" data-rw-transcript-version="2">
 example, one that gets less important is,
 </span>
 <span data-rw-start="696.32" data-rw-transcript-version="2">
 uh, switching costs because you can just
 </span>
 <span data-rw-start="698.16" data-rw-transcript-version="2">
 use the model and you can kind of port.
 </span>
</p>
<p>
 <span data-rw-start="700.08" data-rw-transcript-version="2">
 from one thing to a different thing.
 </span>
 <span data-rw-start="701.8" data-rw-transcript-version="2">
 Another one that gets less important is
 </span>
 <span data-rw-start="703.76" data-rw-transcript-version="2">
 process power,
 </span>
 <span data-rw-start="705.2" data-rw-transcript-version="2">
 because for companies whose mode is like
 </span>
 <span data-rw-start="707.24" data-rw-transcript-version="2">
 workflows and process and things like
 </span>
 <span data-rw-start="709.08" data-rw-transcript-version="2">
 this,
 </span>
 <span data-rw-start="710.04" data-rw-transcript-version="2">
 Claude is getting really good at
 </span>
 <span data-rw-start="711.24" data-rw-transcript-version="2">
 figuring out process. And especially
 </span>
 <span data-rw-start="713.08" data-rw-transcript-version="2">
 with 4.7, it can just hill climb
 </span>
 <span data-rw-start="715" data-rw-transcript-version="2">
 anything. So, if you give it a target
 </span>
 <span data-rw-start="716.839" data-rw-transcript-version="2">
 and you tell it to iterate until it's
 </span>
 <span data-rw-start="718.04" data-rw-transcript-version="2">
 done, it will just do it. I think this
 </span>
 <span data-rw-start="719.72" data-rw-transcript-version="2">
 is the first model like that.
 </span>
</p>
<p>
 <span data-rw-start="722.08" data-rw-transcript-version="2">
 So, I think these are going to get less
 </span>
 <span data-rw-start="723.08" data-rw-transcript-version="2">
 important, but I think the previous
 </span>
 <span data-rw-start="724.32" data-rw-transcript-version="2">
 modes actually still matter. So, this is
 </span>
 <span data-rw-start="725.839" data-rw-transcript-version="2">
 like network effects, uh scale
 </span>
 <span data-rw-start="728" data-rw-transcript-version="2">
 economies, cornered resources, things
 </span>
 <span data-rw-start="730.04" data-rw-transcript-version="2">
 like that. These are not really changing
 </span>
 <span data-rw-start="731.6" data-rw-transcript-version="2">
 with AI.
 </span>
</p>
<p>
 <span data-rw-start="733.44" data-rw-transcript-version="2">
 I think the second thing is, if you look
 </span>
 <span data-rw-start="735.2" data-rw-transcript-version="2">
 at the number of startups today or, like,
 </span>
 <span data-rw-start="736.52" data-rw-transcript-version="2">
 maybe in the next, you know, the past 10
 </span>
 <span data-rw-start="738.04" data-rw-transcript-version="2">
 years, I think the number of startups in
 </span>
 <span data-rw-start="739.48" data-rw-transcript-version="2">
 the next 10 years that are just going to
 </span>
 <span data-rw-start="740.8" data-rw-transcript-version="2">
 Like disrupt everything is going to
 </span>
 <span data-rw-start="742.48" data-rw-transcript-version="2">
 increase like 10x.
 </span>
</p>
<p>
 <span data-rw-start="744.4" data-rw-transcript-version="2">
 Because right now you can be a tiny
 </span>
 <span data-rw-start="746.32" data-rw-transcript-version="2">
 startup, you could build a thing that's
 </span>
 <span data-rw-start="747.8" data-rw-transcript-version="2">
 as valuable as a large company, and you
 </span>
 <span data-rw-start="750" data-rw-transcript-version="2">
 can actually compete head-to-head because the large company has to evolve
 </span>
 <span data-rw-start="751.88" data-rw-transcript-version="2">
 their business process, they have to
 </span>
 <span data-rw-start="753.44" data-rw-transcript-version="2">
 evolve the way they work, they have to
 </span>
 <span data-rw-start="754.839" data-rw-transcript-version="2">
 retrain everyone to use technology,
 </span>
 <span data-rw-start="756.6" data-rw-transcript-version="2">
 they're going to face a lot of internal resistance to that.
 </span>
</p>
<p>
 <span data-rw-start="760.76" data-rw-transcript-version="2">
 But
 </span>
 <span data-rw-start="761.6" data-rw-transcript-version="2">
 you know, no one here has that problem.
 </span>
 <span data-rw-start="764.04" data-rw-transcript-version="2">
 If you're starting fresh, then you can
 </span>
 <span data-rw-start="765.56" data-rw-transcript-version="2">
 kind of build with AI natively from the
 </span>
 <span data-rw-start="767.8" data-rw-transcript-version="2">
 ground up.
 </span>
 <span data-rw-start="768.96" data-rw-transcript-version="2">
 So, I don't know. I think it's the
 </span>
 <span data-rw-start="770.56" data-rw-transcript-version="2">
 best time to build. It's the best time
 </span>
 <span data-rw-start="771.72" data-rw-transcript-version="2">
 to be a startup. There's so much
 </span>
 <span data-rw-start="773.28" data-rw-transcript-version="2">
 disruption coming.
 </span>
 <span data-rw-start="775.04" data-rw-transcript-version="2">
 So, there is hope for us after all.
 </span>
</p>
<p>
 <span data-rw-start="776.72" data-rw-transcript-version="2">
 Thank you, Boris.
 </span>
 <span data-rw-start="778" data-rw-transcript-version="2">
 Um, I would love to open up to audience questions if anyone has anything they
 </span>
 <span data-rw-start="780.96" data-rw-transcript-version="2">
 Would like to ask.
 </span>
</p>
<p>
 <span data-rw-start="783.2" data-rw-transcript-version="2">
 Dan?
 </span>
 <span data-rw-start="788.08" data-rw-transcript-version="2">
 I, yeah, I'm curious.
 </span>
 <span data-rw-start="789.88" data-rw-transcript-version="2">
 Um, you said that you built, uh
 </span>
 <span data-rw-start="792.28" data-rw-transcript-version="2">
 6 months before there was product market
 </span>
 <span data-rw-start="793.96" data-rw-transcript-version="2">
 fit, but now given that the models are
 </span>
 <span data-rw-start="796.04" data-rw-transcript-version="2">
 good enough, how much do you attribute
 </span>
 <span data-rw-start="797.44" data-rw-transcript-version="2">
 the success of Claude code to the model
 </span>
 <span data-rw-start="799.96" data-rw-transcript-version="2">
 versus like product decisions in the
 </span>
 <span data-rw-start="802.12" data-rw-transcript-version="2">
 field of product?
 </span>
 <span data-rw-start="805.16" data-rw-transcript-version="2">
 Uh, I think it's probably a mix.
 </span>
 <span data-rw-start="807.28" data-rw-transcript-version="2">
 Yeah, I think it's a mix. I think,
 </span>
 <span data-rw-start="808.56" data-rw-transcript-version="2">
 if you asked me, maybe a year ago,
 </span>
 <span data-rw-start="809.72" data-rw-transcript-version="2">
 the ratio was maybe something like
 </span>
 <span data-rw-start="810.92" data-rw-transcript-version="2">
 50/50.
 </span>
 <span data-rw-start="812.24" data-rw-transcript-version="2">
 Um, maybe I don't know. If you asked me six
 </span>
 <span data-rw-start="813.8" data-rw-transcript-version="2">
 months ago, the mix would be 50/50.
 </span>
 <span data-rw-start="815.36" data-rw-transcript-version="2">
 &gt; &gt;&gt; What about in two years?
 </span>
 <span data-rw-start="817.16" data-rw-transcript-version="2">
 Oh, two years, I don't know, dude. We plan
 </span>
 <span data-rw-start="818.48" data-rw-transcript-version="2">
 in, like, we plan in one week out.
 </span>
 <span data-rw-start="820.08" data-rw-transcript-version="2">
 &gt;&gt; Months. Sometime in the future.
 </span>
 <span data-rw-start="821.379" data-rw-transcript-version="2">
 &gt;&gt; [Laughter]
 </span>
 <span data-rw-start="822.68" data-rw-transcript-version="2">
 &gt;&gt; And, by the way, I think the reason it
 </span>
 <span data-rw-start="823.96" data-rw-transcript-version="2">
 was 50/50 is, um
 </span>
 <span data-rw-start="826.28" data-rw-transcript-version="2">
 You know, I I I like I I did YC back in
 </span>
 <span data-rw-start="829.6" data-rw-transcript-version="2">
 the day. I was like the first hire at a
 </span>
 <span data-rw-start="831" data-rw-transcript-version="2">
 YC company, and like I did a bunch of
 </span>
 <span data-rw-start="832.6" data-rw-transcript-version="2">
 startups.
 </span>
</p>
<p>
 <span data-rw-start="833.72" data-rw-transcript-version="2">
 And in startups, like the thing that they
 </span>
 <span data-rw-start="835" data-rw-transcript-version="2">
 drill into you and then especially in YC
 </span>
 <span data-rw-start="836.56" data-rw-transcript-version="2">
 over and over is build something people
 </span>
 <span data-rw-start="838.04" data-rw-transcript-version="2">
 love.
 </span>
 <span data-rw-start="839.52" data-rw-transcript-version="2">
 And so, it doesn't matter what the
 </span>
 <span data-rw-start="840.839" data-rw-transcript-version="2">
 product is, it doesn't matter like the
 </span>
 <span data-rw-start="842.16" data-rw-transcript-version="2">
 model and all this stuff. You still in
 </span>
 <span data-rw-start="843.36" data-rw-transcript-version="2">
 the end have to build a thing that
 </span>
 <span data-rw-start="844.4" data-rw-transcript-version="2">
 people love. And I think that's that
 </span>
 <span data-rw-start="846.56" data-rw-transcript-version="2">
 why the product matters. We pay so
 </span>
 <span data-rw-start="848.56" data-rw-transcript-version="2">
 much attention to the little details so
 </span>
 <span data-rw-start="850.44" data-rw-transcript-version="2">
 that as you use it all day, it's a
 </span>
 <span data-rw-start="852.4" data-rw-transcript-version="2">
 really great experience.
 </span>
 <span data-rw-start="854.56" data-rw-transcript-version="2">
 I think as the model's gotten better,
 </span>
 <span data-rw-start="855.8" data-rw-transcript-version="2">
 the harness kind of gets less important.
 </span>
 <span data-rw-start="858" data-rw-transcript-version="2">
 And I think, like, I think that we're
 </span>
 <span data-rw-start="860.36" data-rw-transcript-version="2">
 thinking about right now is, like, how do
 </span>
 <span data-rw-start="861.36" data-rw-transcript-version="2">
 we evolve the harness? So, like, how do
 </span>
 <span data-rw-start="862.839" data-rw-transcript-version="2">
 we make loops more of a first-class
 </span>
 <span data-rw-start="864.36" data-rw-transcript-version="2">
 thing? How do we make it easier to run a
 </span>
 <span data-rw-start="866.48" data-rw-transcript-version="2">
 lot of agents? Uh, you know, besides you.
 </span>
</p>
<p>
 <span data-rw-start="868.64" data-rw-transcript-version="2">
 Know, like sub agents is one idea.
 </span>
 <span data-rw-start="870.4" data-rw-transcript-version="2">
 There's a bunch more stuff that we're
 </span>
 <span data-rw-start="871.4" data-rw-transcript-version="2">
 cooking.
 </span>
 <span data-rw-start="872.8" data-rw-transcript-version="2">
 But I think in a year, the model will be
 </span>
 <span data-rw-start="874.44" data-rw-transcript-version="2">
 much better aligned. And so, all the
 </span>
 <span data-rw-start="876.76" data-rw-transcript-version="2">
 safety mechanisms that we have today
 </span>
 <span data-rw-start="878.32" data-rw-transcript-version="2">
 around
 </span>
 <span data-rw-start="879.44" data-rw-transcript-version="2">
 uh prompt injection and kind of static
 </span>
 <span data-rw-start="881.52" data-rw-transcript-version="2">
 verification of commands and uh
 </span>
 <span data-rw-start="883.839" data-rw-transcript-version="2">
 permission modes, human in the loop, all
 </span>
 <span data-rw-start="885.44" data-rw-transcript-version="2">
 this kind of stuff is just going to be
 </span>
 <span data-rw-start="886.48" data-rw-transcript-version="2">
 less important cuz the model will just
 </span>
 <span data-rw-start="888.04" data-rw-transcript-version="2">
 do the right thing.
 </span>
 <span data-rw-start="889.6" data-rw-transcript-version="2">
 Um, so, yeah, that's that prediction.
 </span>
</p>
<p>
 <span data-rw-start="892.4" data-rw-transcript-version="2">
 Thank you.
 </span>
 <span data-rw-start="895.079" data-rw-transcript-version="2">
 You want to toss the box, Dan?
 </span>
 <span data-rw-start="897.36" data-rw-transcript-version="2">
 &gt;&gt; [snorts]
 </span>
 <span data-rw-start="899.959" data-rw-transcript-version="2">
 &gt;&gt; Great.
 </span>
</p>
<p>
 <span data-rw-start="901.28" data-rw-transcript-version="2">
 Um, to zoom out a little bit from
 </span>
 <span data-rw-start="903.52" data-rw-transcript-version="2">
 software, I think Claude code did a
 </span>
 <span data-rw-start="905.44" data-rw-transcript-version="2">
 cultural change a few months ago where
 </span>
 <span data-rw-start="907.8" data-rw-transcript-version="2">
 it democratized like building software.
 </span>
 <span data-rw-start="910.2" data-rw-transcript-version="2">
 You can see, uh, shop owners building
 </span>
 <span data-rw-start="912.32" data-rw-transcript-version="2">
 their own
 </span>
 <span data-rw-start="913.48" data-rw-transcript-version="2">
 Um, software for themselves or even uh
 </span>
 <span data-rw-start="915.72" data-rw-transcript-version="2">
 programming microcontrollers to control
 </span>
 <span data-rw-start="917.959" data-rw-transcript-version="2">
 the light when someone opens the door.
 </span>
</p>
<p>
 <span data-rw-start="919.6" data-rw-transcript-version="2">
 Um, do you see in the future, um,
 </span>
 <span data-rw-start="922.36" data-rw-transcript-version="2">
 building software becoming a skill like
 </span>
 <span data-rw-start="925.079" data-rw-transcript-version="2">
 uh, I know, uh, Microsoft Office?
 </span>
</p>
<p>
 <span data-rw-start="927.24" data-rw-transcript-version="2">
 Um, so, it's a thing that ev- everybody can do,
 </span>
 <span data-rw-start="929.079" data-rw-transcript-version="2">
 not just people in the tech industry. Oh,
 </span>
 <span data-rw-start="931.079" data-rw-transcript-version="2">
 my god, yes. Yes. Yes. I think it’s
 </span>
 <span data-rw-start="933.4" data-rw-transcript-version="2">
 going to be even more than that. I think
 </span>
 <span data-rw-start="934.48" data-rw-transcript-version="2">
 it's going to be—I don't know. It's
 </span>
 <span data-rw-start="935.959" data-rw-transcript-version="2">
 going to be a skill like yeah, like I
 </span>
 <span data-rw-start="936.959" data-rw-transcript-version="2">
 know how to send a text message.
 </span>
</p>
<p>
 <span data-rw-start="940.6" data-rw-transcript-version="2">
 I, I, I think, um,
 </span>
 <span data-rw-start="942.24" data-rw-transcript-version="2">
 you know, like I, I read a, my, my two
 </span>
 <span data-rw-start="943.68" data-rw-transcript-version="2">
 genres are essentially sci-fi and tech
 </span>
 <span data-rw-start="945.36" data-rw-transcript-version="2">
 history. This is what I read a lot of.
 </span>
</p>
<p>
 <span data-rw-start="947.56" data-rw-transcript-version="2">
 I, I think in tech history, there’s one
 </span>
 <span data-rw-start="949.36" data-rw-transcript-version="2">
 thing which I think to me is the
 </span>
 <span data-rw-start="950.52" data-rw-transcript-version="2">
 clearest parallel for what’s happening
 </span>
 <span data-rw-start="952.04" data-rw-transcript-version="2">
 right now. And this is in the 1400s,
 </span>
 <span data-rw-start="955.44" data-rw-transcript-version="2">
 the printing press in Europe.
 </span>
</p>
<p>
 <span data-rw-start="957.92" data-rw-transcript-version="2">
 And what happened was, before the
 </span>
 <span data-rw-start="959.56" data-rw-transcript-version="2">
 printing press, essentially 10% of the
 </span>
 <span data-rw-start="961.6" data-rw-transcript-version="2">
 European population was literate. They
 </span>
 <span data-rw-start="963.52" data-rw-transcript-version="2">
 Knew how to read and write.
 </span>
</p>
<p>
 <span data-rw-start="965.24" data-rw-transcript-version="2">
 They were often employed by like kings
 </span>
 <span data-rw-start="967.04" data-rw-transcript-version="2">
 and lords that were not literate.
 </span>
 <span data-rw-start="969.64" data-rw-transcript-version="2">
 And their job was to, you know, their
 </span>
 <span data-rw-start="971.24" data-rw-transcript-version="2">
 job was to read and write, and this
 </span>
 <span data-rw-start="972.44" data-rw-transcript-version="2">
 is not something that everyone knew how
 </span>
 <span data-rw-start="973.48" data-rw-transcript-version="2">
 to do.
 </span>
</p>
<p>
 <span data-rw-start="974.651" data-rw-transcript-version="2">
 &gt;&gt; [snorts]
 </span>
 <span data-rw-start="974.72" data-rw-transcript-version="2">
 &gt;&gt; The printing press was invented, then
 </span>
 <span data-rw-start="976.079" data-rw-transcript-version="2">
 there were two more presses, and in the
 </span>
 <span data-rw-start="978.04" data-rw-transcript-version="2">
 50 years after the first printing press,
 </span>
 <span data-rw-start="980.72" data-rw-transcript-version="2">
 there was more literature published in
 </span>
 <span data-rw-start="982.24" data-rw-transcript-version="2">
 Europe than in the thousand years
 </span>
 <span data-rw-start="983.64" data-rw-transcript-version="2">
 before.
 </span>
</p>
<p>
 <span data-rw-start="985.12" data-rw-transcript-version="2">
 And over the same period, the cost of
 </span>
 <span data-rw-start="986.68" data-rw-transcript-version="2">
 literature, the cost of a book, went down
 </span>
 <span data-rw-start="988" data-rw-transcript-version="2">
 like a 100x. And then, you know, it took
 </span>
 <span data-rw-start="990.28" data-rw-transcript-version="2">
 a couple hundred years because, you know,
 </span>
 <span data-rw-start="991.76" data-rw-transcript-version="2">
 learning to read and write is hard. You
 </span>
 <span data-rw-start="993.079" data-rw-transcript-version="2">
 need education systems and government
 </span>
 <span data-rw-start="995.32" data-rw-transcript-version="2">
 and everyone can't be working on farms,
 </span>
 <span data-rw-start="997.32" data-rw-transcript-version="2">
 and so on. But over the next few hundred
 </span>
 <span data-rw-start="999.28" data-rw-transcript-version="2">
 years, literacy globally went up to like
 </span>
 <span data-rw-start="1000.8" data-rw-transcript-version="2">
 70%. And so, you know, now we can all
 </span>
 <span data-rw-start="1003.079" data-rw-transcript-version="2">
 read and write, and you don't need a
 </span>
 <span data-rw-start="1004.88" data-rw-transcript-version="2">
 Degree in reading and writing to know
 </span>
 <span data-rw-start="1006.2" data-rw-transcript-version="2">
 how to read and write. Although still
 </span>
 <span data-rw-start="1007.8" data-rw-transcript-version="2">
 there are professional writers and that
 </span>
 <span data-rw-start="1009.16" data-rw-transcript-version="2">
 is a thing that you can do.
 </span>
</p>
<p>
 <span data-rw-start="1010.88" data-rw-transcript-version="2">
 So, I think the thing that's about to
 </span>
 <span data-rw-start="1013" data-rw-transcript-version="2">
 happen and it's going to be much faster
 </span>
 <span data-rw-start="1014.839" data-rw-transcript-version="2">
 than 50 years is software will be a
 </span>
 <span data-rw-start="1016.8" data-rw-transcript-version="2">
 thing that is fully democratized, that
 </span>
 <span data-rw-start="1018.56" data-rw-transcript-version="2">
 anyone can do.
 </span>
</p>
<p>
 <span data-rw-start="1019.959" data-rw-transcript-version="2">
 And you know, there's a lot of
 </span>
 <span data-rw-start="1021.48" data-rw-transcript-version="2">
 corollaries to this. So, for example,
 </span>
 <span data-rw-start="1024.24" data-rw-transcript-version="2">
 let's say you're writing accounting
 </span>
 <span data-rw-start="1025.16" data-rw-transcript-version="2">
 software.
 </span>
 <span data-rw-start="1026.76" data-rw-transcript-version="2">
 The best person to write accounting
 </span>
 <span data-rw-start="1028.12" data-rw-transcript-version="2">
 software, I think maybe even today, is
 </span>
 <span data-rw-start="1030.16" data-rw-transcript-version="2">
 not an engineer, it's a really good
 </span>
 <span data-rw-start="1031.64" data-rw-transcript-version="2">
 accountant because they know the domain
 </span>
 <span data-rw-start="1033.959" data-rw-transcript-version="2">
 really well, and coding is the easy part.
 </span>
 <span data-rw-start="1035.56" data-rw-transcript-version="2">
 It's knowing the domain that's the hard
 </span>
 <span data-rw-start="1036.839" data-rw-transcript-version="2">
 part. And I think this is just
 </span>
 <span data-rw-start="1038.92" data-rw-transcript-version="2">
 obviously the future.
 </span>
</p>
<p>
 <span data-rw-start="1042.6" data-rw-transcript-version="2">
 So, uh, one of the things Greg said was
 </span>
 <span data-rw-start="1044.679" data-rw-transcript-version="2">
 that you guys are living in the future a
 </span>
 <span data-rw-start="1046.32" data-rw-transcript-version="2">
 little bit because you get to have access to
 </span>
 <span data-rw-start="1048.079" data-rw-transcript-version="2">
 the models and the agents. Claude code.
 </span>
</p>
<p>
 <span data-rw-start="1050.08" data-rw-transcript-version="2">
 Was an internal tool before you released
 </span>
 <span data-rw-start="1051.48" data-rw-transcript-version="2">
 it. Um, is the gap between where you guys
 </span>
 <span data-rw-start="1054.28" data-rw-transcript-version="2">
 are in engineering and the rest of the
 </span>
 <span data-rw-start="1055.92" data-rw-transcript-version="2">
 world, is that a month? Is it 3 months?
 </span>
 <span data-rw-start="1058.48" data-rw-transcript-version="2">
 Is it 6 months? And is that, is that gap
 </span>
 <span data-rw-start="1060.36" data-rw-transcript-version="2">
 getting bigger or smaller over time?
 </span>
</p>
<p>
 <span data-rw-start="1064.04" data-rw-transcript-version="2">
 Yeah, so, so internally, we use the same
 </span>
 <span data-rw-start="1065.92" data-rw-transcript-version="2">
 models everyone else does.
 </span>
 <span data-rw-start="1067.52" data-rw-transcript-version="2">
 Um, for us, the dogfooding is really
 </span>
 <span data-rw-start="1069.24" data-rw-transcript-version="2">
 really important. So, we use the thing
 </span>
 <span data-rw-start="1070.92" data-rw-transcript-version="2">
 that everyone else here does. Um, you
 </span>
 <span data-rw-start="1073.12" data-rw-transcript-version="2">
 know, we use a little bit of Mythos
 </span>
 <span data-rw-start="1074.48" data-rw-transcript-version="2">
 to try it and then we use a lot of Opus
 </span>
 <span data-rw-start="1076.32" data-rw-transcript-version="2">
 4.7 to dogfood it and to write most
 </span>
 <span data-rw-start="1078.48" data-rw-transcript-version="2">
 of our code.
 </span>
</p>
<p>
 <span data-rw-start="1079.88" data-rw-transcript-version="2">
 Um, I think on the model side, there
 </span>
 <span data-rw-start="1081.24" data-rw-transcript-version="2">
 isn't really a gap. Um, you know, it's
 </span>
 <span data-rw-start="1082.72" data-rw-transcript-version="2">
 like, it's pretty much Mythos, and you
 </span>
 <span data-rw-start="1084.16" data-rw-transcript-version="2">
 know, that will become some version of
 </span>
 <span data-rw-start="1086.4" data-rw-transcript-version="2">
 some descendant of that will become
 </span>
 <span data-rw-start="1087.679" data-rw-transcript-version="2">
 available at some point to everyone.
 </span>
</p>
<p>
 <span data-rw-start="1090.36" data-rw-transcript-version="2">
 I think on the product side, there's
 </span>
 <span data-rw-start="1091.52" data-rw-transcript-version="2">
 probably a far larger gap. And that's
 </span>
 <span data-rw-start="1093.8" data-rw-transcript-version="2">
 just related to us changing all of our
 </span>
 <span data-rw-start="1095.56" data-rw-transcript-version="2">
 processes. Like, if you talk to people at
 </span>
 <span data-rw-start="1097.56" data-rw-transcript-version="2">
 Anthropic, we use Claude for literally
 </span>
 <span data-rw-start="1099.16" data-rw-transcript-version="2">
 everything. And our Claudes are talking
 </span>
 <span data-rw-start="1101.36" data-rw-transcript-version="2">
 all day, like, as I'm coding, as my
 </span>
 <span data-rw-start="1103.28" data-rw-transcript-version="2">
 Claudes are coding in a loop, they will
 </span>
 <span data-rw-start="1105.12" data-rw-transcript-version="2">
 communicate over Slack to talk to other
 </span>
 <span data-rw-start="1106.72" data-rw-transcript-version="2">
 people's Claudes that are also running
 </span>
 <span data-rw-start="1108.4" data-rw-transcript-version="2">
 in a loop to kind of figure out
 </span>
 <span data-rw-start="1109.52" data-rw-transcript-version="2">
 unknowns.
 </span>
</p>
<p>
 <span data-rw-start="1110.88" data-rw-transcript-version="2">
 We have no more manually written code
 </span>
 <span data-rw-start="1112.56" data-rw-transcript-version="2">
 anywhere at the company. All of the SQL
 </span>
 <span data-rw-start="1114.679" data-rw-transcript-version="2">
 is written by, uh, by models. Everything
 </span>
 <span data-rw-start="1116.72" data-rw-transcript-version="2">
 is just built by the models. So, I, I, I
 </span>
 <span data-rw-start="1118.72" data-rw-transcript-version="2">
 think, actually, the place that we're
 </span>
 <span data-rw-start="1119.64" data-rw-transcript-version="2">
 ahead is not the technology, because the same
 </span>
 <span data-rw-start="1121.96" data-rw-transcript-version="2">
 technology available to us is available
 </span>
 <span data-rw-start="1123.56" data-rw-transcript-version="2">
 to everyone here because, fundamentally,
 </span>
 <span data-rw-start="1125.96" data-rw-transcript-version="2">
 we are building a platform. And so, for
 </span>
 <span data-rw-start="1127.919" data-rw-transcript-version="2">
 us, it's really important that
 </span>
 <span data-rw-start="1129.48" data-rw-transcript-version="2">
 developers can use the same thing that
 </span>
 <span data-rw-start="1130.76" data-rw-transcript-version="2">
 we're using and that we, we dog food
 </span>
 <span data-rw-start="1132.64" data-rw-transcript-version="2">
 everything that we put out there.
 </span>
 <span data-rw-start="1134.44" data-rw-transcript-version="2">
 But, I think there's actually a far
 </span>
 <span data-rw-start="1135.4" data-rw-transcript-version="2">
 bigger weed in, kind of, the
 </span>
 <span data-rw-start="1136.6" data-rw-transcript-version="2">
 organizational structure and
 </span>
 <span data-rw-start="1137.8" data-rw-transcript-version="2">
 organizational process. And, this is a
 </span>
 <span data-rw-start="1139.64" data-rw-transcript-version="2">
 Place where you know, hopefully we can
 </span>
 <span data-rw-start="1141.36" data-rw-transcript-version="2">
 talk about it in places like this and uh
 </span>
 <span data-rw-start="1143.52" data-rw-transcript-version="2">
 everyone can kind of learn from it and
 </span>
 <span data-rw-start="1145.32" data-rw-transcript-version="2">
 and also evolve.
 </span>
</p>
<p>
 <span data-rw-start="1146.6" data-rw-transcript-version="2">
 Yeah, and I think that's one of the
 </span>
 <span data-rw-start="1147.679" data-rw-transcript-version="2">
 advantages startups have. It's so much
 </span>
 <span data-rw-start="1149" data-rw-transcript-version="2">
 easier to start there.
 </span>
 <span data-rw-start="1150.52" data-rw-transcript-version="2">
 Jared?
 </span>
 <span data-rw-start="1152.159" data-rw-transcript-version="2">
 Yeah, um, last time we talked, I think I
 </span>
 <span data-rw-start="1154.12" data-rw-transcript-version="2">
 think you'd mentioned we talked a little
 </span>
 <span data-rw-start="1155.4" data-rw-transcript-version="2">
 bit about multi-agent, and it was very in
 </span>
 <span data-rw-start="1157" data-rw-transcript-version="2">
 code at the time, at a prior Sequoia
 </span>
 <span data-rw-start="1158.36" data-rw-transcript-version="2">
 event, and you mentioned that there were
 </span>
 <span data-rw-start="1160.04" data-rw-transcript-version="2">
 some things going down the pipeline, and
 </span>
 <span data-rw-start="1161.84" data-rw-transcript-version="2">
 things you're talking about, you're thinking
 </span>
 <span data-rw-start="1162.919" data-rw-transcript-version="2">
 about. Now, obviously, there's slash
 </span>
 <span data-rw-start="1164.32" data-rw-transcript-version="2">
 batch, there's slash loop, there's sub
 </span>
 <span data-rw-start="1166.08" data-rw-transcript-version="2">
 teams, there are teams. Can you speak some
 </span>
</p>
<p>
 <span data-rw-start="1167.8" data-rw-transcript-version="2">
 to either the model level or the
 </span>
 <span data-rw-start="1170.44" data-rw-transcript-version="2">
 harness level, how you're injecting
 </span>
 <span data-rw-start="1172.28" data-rw-transcript-version="2">
 priors in the harness level, and how the
 </span>
 <span data-rw-start="1173.72" data-rw-transcript-version="2">
 objective function is changing at the model
 </span>
 <span data-rw-start="1175.04" data-rw-transcript-version="2">
 level to make this experience
 </span>
 <span data-rw-start="1176.72" data-rw-transcript-version="2">
 around delegating work, spinning up
 </span>
 <span data-rw-start="1178.2" data-rw-transcript-version="2">
 agents better? Because so much of the work
 </span>
 <span data-rw-start="1179.96" data-rw-transcript-version="2">
 is parallelizable. You can do so many
 </span>
 <span data-rw-start="1181.88" data-rw-transcript-version="2">
 things so much faster, and I feel like I
 </span>
 <span data-rw-start="1183.44" data-rw-transcript-version="2">
 have to overlay my own intuition for
 </span>
 <span data-rw-start="1185.2" data-rw-transcript-version="2">
 when to parallelize things rather than
 </span>
 <span data-rw-start="1186.44" data-rw-transcript-version="2">
 the model kind of understanding that you
 </span>
 <span data-rw-start="1188.04" data-rw-transcript-version="2">
 can spin up 10 sub-agents for something.
 </span>
</p>
<p>
 <span data-rw-start="1190.52" data-rw-transcript-version="2">
 Yeah, I mean, on the product side, it
 </span>
 <span data-rw-start="1192" data-rw-transcript-version="2">
 really just comes down to prompting.
 </span>
 <span data-rw-start="1193.56" data-rw-transcript-version="2">
 That's how it is. And so, you
 </span>
 <span data-rw-start="1194.76" data-rw-transcript-version="2">
 know, we tweak prompts to kind of
 </span>
 <span data-rw-start="1196.6" data-rw-transcript-version="2">
 help the model do stuff in parallel
 </span>
 <span data-rw-start="1197.88" data-rw-transcript-version="2">
 more.
 </span>
</p>
<p>
 <span data-rw-start="1199.4" data-rw-transcript-version="2">
 But also, honestly, as the model gets
 </span>
 <span data-rw-start="1201.16" data-rw-transcript-version="2">
 better, it just naturally does this. And
 </span>
 <span data-rw-start="1203.16" data-rw-transcript-version="2">
 so, something like loop, I found
 </span>
 <span data-rw-start="1204.64" data-rw-transcript-version="2">
 actually 4.7, it just starts doing. Uh
 </span>
 <span data-rw-start="1207.24" data-rw-transcript-version="2">
 which is really cool. It's like it does
 </span>
 <span data-rw-start="1208.96" data-rw-transcript-version="2">
 something like, uh, you know, I'll I'll
 </span>
 <span data-rw-start="1210.88" data-rw-transcript-version="2">
 tell it, "Go, uh,
 </span>
 <span data-rw-start="1212.68" data-rw-transcript-version="2">
 pull this data query." And it's like,
 </span>
 <span data-rw-start="1214.8" data-rw-transcript-version="2">
 "Hey, I noticed that the data is
 </span>
 <span data-rw-start="1215.96" data-rw-transcript-version="2">
 changing over time. I'll start a loop
 </span>
 <span data-rw-start="1217.68" data-rw-transcript-version="2">
 and I'll give you a report every 30
 </span>
 <span data-rw-start="1218.8" data-rw-transcript-version="2">
 minutes." And I'm like, "Great. Can you
 </span>
 <span data-rw-start="1220.16" data-rw-transcript-version="2">
 send it to me over Slack?"
 </span>
 <span data-rw-start="1221.8" data-rw-transcript-version="2">
 Uses the Slack MCP to do that. So, I
 </span>
 <span data-rw-start="1224" data-rw-transcript-version="2">
 think actually over time, it's not on
 </span>
 <span data-rw-start="1225.92" data-rw-transcript-version="2">
 users to figure out how to hold the
 </span>
 <span data-rw-start="1227.4" data-rw-transcript-version="2">
 tools better. And if that's the case,
 </span>
 <span data-rw-start="1229.2" data-rw-transcript-version="2">
 it's actually a product design problem,
 </span>
 <span data-rw-start="1230.4" data-rw-transcript-version="2">
 and like I'm not doing a good job.
 </span>
</p>
<p>
 <span data-rw-start="1232.52" data-rw-transcript-version="2">
 It's really on the model to do this
 </span>
 <span data-rw-start="1234.12" data-rw-transcript-version="2">
 stuff better and on us, kind of prompting
 </span>
 <span data-rw-start="1236.12" data-rw-transcript-version="2">
 it so it naturally does this.
 </span>
</p>
<p>
 <span data-rw-start="1241.12" data-rw-transcript-version="2">
 Um, so right now it seems like a lot of
 </span>
 <span data-rw-start="1243.32" data-rw-transcript-version="2">
 us use, um, like Claude or Codex or these
 </span>
 <span data-rw-start="1248.32" data-rw-transcript-version="2">
 uh tools in the cloud to do a lot of our
 </span>
 <span data-rw-start="1250.08" data-rw-transcript-version="2">
 computing. But then, there are some very
 </span>
 <span data-rw-start="1251.68" data-rw-transcript-version="2">
 vocal advocates of, uh, having your AI be
 </span>
 <span data-rw-start="1254.32" data-rw-transcript-version="2">
 local. And I could imagine over time, as
 </span>
 <span data-rw-start="1257.32" data-rw-transcript-version="2">
 open way models and other things
 </span>
 <span data-rw-start="1259.24" data-rw-transcript-version="2">
 catch up, that this could be more of a
 </span>
 <span data-rw-start="1261.04" data-rw-transcript-version="2">
 possibility for people to get really
 </span>
 <span data-rw-start="1262.24" data-rw-transcript-version="2">
 high-quality coding assistance. So, I'm
 </span>
 <span data-rw-start="1264.52" data-rw-transcript-version="2">
 curious about your vision of, say, over the next
 </span>
 <span data-rw-start="1266.76" data-rw-transcript-version="2">
 like
 </span>
 <span data-rw-start="1268" data-rw-transcript-version="2">
 years or something like that. Do you see
 </span>
 <span data-rw-start="1270.04" data-rw-transcript-version="2">
 the trajectory of everyone still really
 </span>
 <span data-rw-start="1271.68" data-rw-transcript-version="2">
 relying on the cloud, centralized
 </span>
 <span data-rw-start="1274.68" data-rw-transcript-version="2">
 compute? Or, uh, is there a pivot to, oh, we
 </span>
 <span data-rw-start="1277.84" data-rw-transcript-version="2">
 All just have our local agents that we
 </span>
 <span data-rw-start="1279.52" data-rw-transcript-version="2">
 can rely on and they don't get throttled
 </span>
 <span data-rw-start="1281.04" data-rw-transcript-version="2">
 and other benefits?
 </span>
</p>
<p>
 <span data-rw-start="1283.72" data-rw-transcript-version="2">
 Yeah, I think it, um,
 </span>
 <span data-rw-start="1286.6" data-rw-transcript-version="2">
 I don't know. There's maybe a few ways
 </span>
 <span data-rw-start="1288.08" data-rw-transcript-version="2">
 to answer that. I think maybe like kind
 </span>
 <span data-rw-start="1289.28" data-rw-transcript-version="2">
 of the most fundamental way to
 </span>
 <span data-rw-start="1290.56" data-rw-transcript-version="2">
 answer that is it doesn't matter.
 </span>
</p>
<p>
 <span data-rw-start="1292.6" data-rw-transcript-version="2">
 Cause, cause I think now we're getting to the
 </span>
 <span data-rw-start="1294" data-rw-transcript-version="2">
 point where the model is just able to
 </span>
 <span data-rw-start="1295.12" data-rw-transcript-version="2">
 figure it out. So, I think like by a
 </span>
 <span data-rw-start="1297.2" data-rw-transcript-version="2">
 couple of years from now, the model is just
 </span>
 <span data-rw-start="1298.36" data-rw-transcript-version="2">
 going to be doing all the code. It's
 </span>
 <span data-rw-start="1299.44" data-rw-transcript-version="2">
 going to be starting the agents. It's
 </span>
 <span data-rw-start="1300.52" data-rw-transcript-version="2">
 going to be building the environments.
 </span>
</p>
<p>
 <span data-rw-start="1302.16" data-rw-transcript-version="2">
 And so, like if it decides, like, actually,
 </span>
 <span data-rw-start="1303.56" data-rw-transcript-version="2">
 I'll use, like, local models to do this,
 </span>
 <span data-rw-start="1304.92" data-rw-transcript-version="2">
 then you know, that's what it'll do.
 </span>
 <span data-rw-start="1306.64" data-rw-transcript-version="2">
 These, I don't think these will be
 </span>
 <span data-rw-start="1307.8" data-rw-transcript-version="2">
 decisions that we are making as
 </span>
 <span data-rw-start="1309.04" data-rw-transcript-version="2">
 engineers anymore.
 </span>
</p>
<p>
 <span data-rw-start="1311.16" data-rw-transcript-version="2">
 We have time for a couple more
 </span>
 <span data-rw-start="1312.08" data-rw-transcript-version="2">
 questions, so I can toss this out.
 </span>
 <span data-rw-start="1315.44" data-rw-transcript-version="2">
 Jamie,
 </span>
 <span data-rw-start="1317.76" data-rw-transcript-version="2">
 Nester. Thank you.
 </span>
</p>
<p>
 <span data-rw-start="1319.6" data-rw-transcript-version="2">
 It feels like one of the great uh decisions with Claude Code was making
 </span>
 <span data-rw-start="1321.12" data-rw-transcript-version="2">
 use of the fact that a lot of
 </span>
 <span data-rw-start="1323.16" data-rw-transcript-version="2">
 developers' tools and workflows are
 </span>
 <span data-rw-start="1324.52" data-rw-transcript-version="2">
 local.
 </span>
 <span data-rw-start="1327.28" data-rw-transcript-version="2">
 But um that isn't necessarily always the
 </span>
 <span data-rw-start="1329.28" data-rw-transcript-version="2">
 case for sort of general knowledge work
 </span>
 <span data-rw-start="1330.96" data-rw-transcript-version="2">
 with, you know, cloud tools. I’m curious
 </span>
 <span data-rw-start="1333.44" data-rw-transcript-version="2">
 how you're thinking about this with
 </span>
 <span data-rw-start="1334.76" data-rw-transcript-version="2">
 Co-work of how do you give Co-work
 </span>
 <span data-rw-start="1336.679" data-rw-transcript-version="2">
 enough access to the tools that we use
 </span>
 <span data-rw-start="1338.96" data-rw-transcript-version="2">
 to be powerful the same way that Claude
 </span>
 <span data-rw-start="1340.84" data-rw-transcript-version="2">
 Code is for developers?
 </span>
</p>
<p>
 <span data-rw-start="1342.64" data-rw-transcript-version="2">
 Yeah, it's That’s a really great
 </span>
 <span data-rw-start="1343.8" data-rw-transcript-version="2">
 question. Um I know I know when I was uh
 </span>
 <span data-rw-start="1346.16" data-rw-transcript-version="2">
 when I was at a big company, we took
 </span>
 <span data-rw-start="1347.28" data-rw-transcript-version="2">
 like 5 years moving all the environments
 </span>
 <span data-rw-start="1349.6" data-rw-transcript-version="2">
 to remote. It’s just like so much work,
 </span>
 <span data-rw-start="1352.08" data-rw-transcript-version="2">
 especially at a big scale.
 </span>
</p>
<p>
 <span data-rw-start="1353.679" data-rw-transcript-version="2">
 Um but for knowledge work, largely, it’s
 </span>
 <span data-rw-start="1355.36" data-rw-transcript-version="2">
 there already with like Salesforce and
 </span>
 <span data-rw-start="1357.32" data-rw-transcript-version="2">
 Docs and things like that.
 </span>
 <span data-rw-start="1359.2" data-rw-transcript-version="2">
 Um for us, it’s always just the simplest
 </span>
 <span data-rw-start="1361" data-rw-transcript-version="2">
 answer. It’s just MCP.
 </span>
 <span data-rw-start="1362.88" data-rw-transcript-version="2">
 So, the same MCP connector that you have
 </span>
 <span data-rw-start="1364.52" data-rw-transcript-version="2">
 In Claude AI, you hook up like, you
 </span>
 <span data-rw-start="1366.16" data-rw-transcript-version="2">
 know, Salesforce, you hook up Google
 </span>
 <span data-rw-start="1367.44" data-rw-transcript-version="2">
 Docs, Google Calendar. Uh, and then
 </span>
 <span data-rw-start="1369.56" data-rw-transcript-version="2">
 Co-work can use that. Claude CLI can use
 </span>
 <span data-rw-start="1371.12" data-rw-transcript-version="2">
 it. Claude Code everywhere can use it.
 </span>
</p>
<p>
 <span data-rw-start="1375.08" data-rw-transcript-version="2">
 And for the systems that don't
 </span>
 <span data-rw-start="1376.48" data-rw-transcript-version="2">
 have MCPs, like, do you think that's
 </span>
 <span data-rw-start="1378.56" data-rw-transcript-version="2">
 where computer use is going to be a big
 </span>
 <span data-rw-start="1380.88" data-rw-transcript-version="2">
 opportunity?
 </span>
</p>
<p>
 <span data-rw-start="1382.16" data-rw-transcript-version="2">
 Yeah, I think computer use is kind of a
 </span>
 <span data-rw-start="1383.6" data-rw-transcript-version="2">
 catch-all. Um, so, I think currently, for
 </span>
 <span data-rw-start="1386.44" data-rw-transcript-version="2">
 as far as I know, I think Anthropic is
 </span>
 <span data-rw-start="1387.84" data-rw-transcript-version="2">
 like pretty far ahead on computers. And
 </span>
 <span data-rw-start="1389.88" data-rw-transcript-version="2">
 so, like if you use it through Co-work,
 </span>
 <span data-rw-start="1391.2" data-rw-transcript-version="2">
 it's quite good. Um, so, it's able to use
 </span>
 <span data-rw-start="1393.52" data-rw-transcript-version="2">
 pretty much any piece of software that
 </span>
 <span data-rw-start="1395.04" data-rw-transcript-version="2">
 you have on your computer. It's very
 </span>
 <span data-rw-start="1396.92" data-rw-transcript-version="2">
 slow, but it does it quite well now,
 </span>
 <span data-rw-start="1398.679" data-rw-transcript-version="2">
 especially with 4.7.
 </span>
 <span data-rw-start="1400.76" data-rw-transcript-version="2">
 Um, yeah, but I think, I think otherwise,
 </span>
 <span data-rw-start="1403" data-rw-transcript-version="2">
 like MCP is kind of the answer. It's
 </span>
 <span data-rw-start="1404.8" data-rw-transcript-version="2">
 and you know, all this stuff just
 </span>
 <span data-rw-start="1405.96" data-rw-transcript-version="2">
 doesn't matter that much. It could be
 </span>
 <span data-rw-start="1407" data-rw-transcript-version="2">
 MCPs, APIs, just some sort of
 </span>
 <span data-rw-start="1409.36" data-rw-transcript-version="2">
 programmatic access because the model
 </span>
 <span data-rw-start="1411.44" data-rw-transcript-version="2">
 Doesn't care. It's to mo- to the model,
 </span>
 <span data-rw-start="1413.16" data-rw-transcript-version="2">
 it's just tokens.
 </span>
</p>
<p>
 <span data-rw-start="1415.48" data-rw-transcript-version="2">
 All right, we have time for one more
 </span>
 <span data-rw-start="1416.44" data-rw-transcript-version="2">
 question.
 </span>
 <span data-rw-start="1418.2" data-rw-transcript-version="2">
 Um, Ryan.
 </span>
 <span data-rw-start="1421.2" data-rw-transcript-version="2">
 Sean, do you want to toss the thank you?
 </span>
 <span data-rw-start="1425.28" data-rw-transcript-version="2">
 Um, you've kind of alluded to this, but
 </span>
 <span data-rw-start="1427.28" data-rw-transcript-version="2">
 if, like, sometime ago, you saw the
 </span>
 <span data-rw-start="1428.8" data-rw-transcript-version="2">
 probabil- the product overhang, and
 </span>
 <span data-rw-start="1431.04" data-rw-transcript-version="2">
 thought to build a product that would
 </span>
 <span data-rw-start="1432.6" data-rw-transcript-version="2">
 then become more interesting once models
 </span>
 <span data-rw-start="1434.4" data-rw-transcript-version="2">
 got better.
 </span>
 <span data-rw-start="1435.72" data-rw-transcript-version="2">
 Could you just talk, even in vague terms,
 </span>
 <span data-rw-start="1437.24" data-rw-transcript-version="2">
 about the shape of a product you'd build
 </span>
 <span data-rw-start="1438.4" data-rw-transcript-version="2">
 today that you think could become a
 </span>
 <span data-rw-start="1439.52" data-rw-transcript-version="2">
 much more interesting as models get
 </span>
 <span data-rw-start="1441.04" data-rw-transcript-version="2">
 better in six months to a year?
 </span>
 <span data-rw-start="1443.24" data-rw-transcript-version="2">
 Yeah, Claude design, I think, is a
 </span>
 <span data-rw-start="1445" data-rw-transcript-version="2">
 really good example. It's, uh, it's pretty
 </span>
 <span data-rw-start="1446.84" data-rw-transcript-version="2">
 good today. It's going to get a lot
 </span>
 <span data-rw-start="1448" data-rw-transcript-version="2">
 better.
 </span>
 <span data-rw-start="1448.96" data-rw-transcript-version="2">
 Um, there's also a few things that we're
 </span>
 <span data-rw-start="1450.28" data-rw-transcript-version="2">
 cooking up for Claude Code, uh, that are
 </span>
 <span data-rw-start="1451.92" data-rw-transcript-version="2">
 going to land over the coming
 </span>
 <span data-rw-start="1453.04" data-rw-transcript-version="2">
 weeks. So, you'll see those.
 </span>
</p>
<p>
 <span data-rw-start="1455.16" data-rw-transcript-version="2">
 Um, and then I think, uh, I think loop and
 </span>
 <span data-rw-start="1457.679" data-rw-transcript-version="2">
 batch and things like this around like
 </span>
 <span data-rw-start="1459.12" data-rw-transcript-version="2">
 massively parallelizing agents, that's
 </span>
 <span data-rw-start="1460.8" data-rw-transcript-version="2">
 going to get better.
 </span>
</p>
<p>
 <span data-rw-start="1462.96" data-rw-transcript-version="2">
 And computer use is another good one.
 </span>
</p>
<p>
 <span data-rw-start="1465.92" data-rw-transcript-version="2">
 All right, Boris. Thank you so much for
 </span>
 <span data-rw-start="1467.4" data-rw-transcript-version="2">
 joining us. I think we'll be here for a
 </span>
 <span data-rw-start="1468.72" data-rw-transcript-version="2">
 little longer if anyone has questions.
 </span>
 <span data-rw-start="1470.491" data-rw-transcript-version="2">
 &gt;&gt; [applause]
 </span>
 <span data-rw-start="1472.96" data-rw-transcript-version="2">
 &gt;&gt; Thanks, guys.
 </span>
</p>