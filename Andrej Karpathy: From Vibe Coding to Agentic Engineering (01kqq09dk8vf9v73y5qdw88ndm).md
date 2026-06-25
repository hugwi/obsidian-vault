---
categories:
  - "[[Resources]]"
domain: engineering
title: "Andrej Karpathy: From Vibe Coding to Agentic Engineering"
source: "https://m.youtube.com/watch?v=96jN2OCOfLs&pp=ugUEEgJlbg%3D%3D"
author: "Sequoia Capital"
published: 2026-04-29
created: 2026-05-03
description: "Andrej Karpathy (co-founder of OpenAI, former head of AI at Tesla, and now"
tags:
  - to-process
  - llm-foundations
---

We're so excited for our very first special guest. He has helped build modern AI, then explain modern AI, and then occasionally rename modern AI. He actually helped co-ound open AAI right inside of this office. Was the one who actually got Autopilot working at Tesla back in the day, and he has a rare gift of making the most complex technical shifts feel both accessible and inevitable. 

You all know him for having coined the term vibe coding last year, but just in the last few months, he said something even more startling. That he's never felt more behind as a programmer. That's where we're starting today. Thank you, Andre, for joining us. >> Yeah. Hello. Excited to be here and to kick us off. >> Okay. So, just a couple months ago, you said that you've never felt more behind as a programmer. That's startling to hear from you of all people. Um, can you help us unpack that? Was that feeling exhilarating or unsettling? 

>> Uh yeah, a mixture of both for sure. Uh well, first of all, um I guess like as many of you, I've been using agentic tools like lot code, adjacent things, uh for a while, maybe over the last year as it came out and it was very good at you know chunks of code and sometimes it would mess up and you have to edit them and it was kind of helpful and then I would say December was this uh clear point where for me I was on a break so I had a bit more time. I think many other people were similar and uh I just started to notice that with the latest models uh the chunks just came out fine and then I kept asking for more and it just came out 

fine and then I can't remember the last time I corrected it and then I was I just you know trusted the system more and more and then I was vibe coding [laughter] and uh so it was kind of a I do think that it was a very stark transition. I think that a lot of people actually I tried to I tried to stress this on uh Twitter and or X because I think a lot of people experienced AI last year as ChachiPT adjacent thing. Uh but you really had to look again and you had to look as of December uh because things have changed fundamentally and uh especially on this like agentic coherent 

workflow uh that really started to actually work. Um, and so I would say that um, yeah, it was just that realization that really uh, uh, had me um, go down their whole rabbit hole of just, you know, infinity side projects. Uh, my side projects folder is like extremely full with lots of random things and, uh, just, uh, V coding all the time. Uh, so, uh, yeah, that kind of happened in December, I would say, and I was looking at the repercussions of that since. >> Um, you've talked a lot about this idea of LLMs as a new computer. um that it 

isn't just better software, it's a whole new computing paradigm. And um software 1.0 was explicit rules, software 2.0 was learned weights, software 3.0 is this. Um if that's actually true, what does a team build differently the day they actually believe this, >> right? So uh yeah, exactly. So software 1.0, I'm writing code, software 2.0, I'm actually programming by creating data sets and training uh training neural networks. So the programming is kind of 

like arranging data sets and maybe some objectives and neural network architectures. And then what happened is that basically if you train one of these GPT models or LLMs on a sufficiently large set of tasks implicit basically um implicitly because by training on the internet you have to multitask all the things that are in the data set. Uh these actually become kind of like a programmable computer in a certain sense. So software 3.0 know is kind of about uh you know your programming now turns to prompting and what's in the context window is your lever over the interpreter that is the LLM that is kind 

of like interpreting your context and uh performing computation in the dig digital information space. So I guess um yeah that's kind of the transition and I think there's a few examples of that really drove it home for me and maybe that might be instructive. Uh so for example when you when openclaw came out when you want to install openclaw you would expect that normally this is a bash bash script like a shell script. So run the shell script to run to install open claw. Um but the thing is that in order to target lots of different platforms and lots of different types of 

computers you might run an open claw. This these shell scripts usually balloon up and become extremely complex. But the thing is you're still stuck in a software 1.0 universe of wanting to write the code. And actually the open claw installation is a is a copy paste of a b bunch of text that you're supposed to give to your agent. Uh so basically it's it's a little skill of uh you know copy paste this and give it to your agent and it will install open claw. And the reason this is a lot more powerful is you're working now in the software 3.0 paradigm where you don't have to precisely spell out you know all the individual details of that setup. The agent has its own intelligence that 

it packages up and then it kind of like follows the instructions and it looks at your environment, your computer and it kind of like performs intelligent actions to make things work and it debugs things in the loop and it's just like so much more powerful, right? So I think that's a very different kind of like way of thinking about it is just like what is the piece of text to copy paste to your agent? That's the programming paradigm. Now I think one more maybe uh example that comes to mind that is even more extreme than that is when I was building um menu genen. So, menu genen is this idea where you um you 

come to a restaurant, they give you a menu. There's no pictures usually. So, I don't know what any of these things are uh usually like 30% of the things I have no idea what they are, 50%. So, I wanted to take a photo of the restaurant menu and to get pictures of what those things might look like in a generic sense. And so I built I've vcoded this app that basically lets you upload a photo and it does all this stuff and it runs on Verscell and uh it basically rerenders the menu and it gives you like all the items and it gives you a picture that it uses an image um you know generator uh 

for to basically OCR all the different titles uh use the image generator to get pictures of them and then shows it to you. And then I saw the software 3.0 version of this which is which blew my mind which is literally just take your photo give it to Gemini and say use Nanobanana to overlay the the things onto the menu. Uh and Nanabanana basically returned an image that is exactly the picture of the menu that I took but it actually put into the pixels it rendered the different things in the menu and this blew my mind because 

actually all of my menu gen is spirious. It's working in the old paradigm that app shouldn't exist. uh and uh yeah the software 3.0 paradigm is a lot more kind of raw. It just um your neural network is doing more and more of the work and your prompt or context is just the image and the output is an image and there's no need to have any of the app in between. Um so I think that people have to kind of like reframe you know not to work in existing paradigm of what things existed and just think about it as a 

speed up of what exists. It's actually like new things are available now. And going back to your programming question, it's not even I think that's also an example of working in the in the old mindset because it's not just about programming and programming becoming faster. This is more general information processing that is automatable now. So um it's not just even about code. So previous code worked over kind of like structured data, right? And uh you write code over structured data. But like for example with my LLM knowledge basis project um basically you get LLMs to create wikis for your organization or 

for you in person etc. This is not even a program. This is not something that could exist before because there was no there was no code that would create a knowledge base based on a bunch of facts. But now you can just take these documents and uh basically uh recompile them in a different way and uh reorder them and create something that is uh new and interesting uh as a reframing of the data. And so these are new things that weren't possible. Uh and so I think this is uh something that I keep trying to get back to as to not only what can we do that existed that is faster now but I 

think there's new opportunities of just things that couldn't be possible before and I almost think that that's more exciting. >> I love the menu genen progression and dichotomy that you laid out and I think even I'm sure many folks here followed your own progression of programming from last October to early January February this year. Um, if you extrapolate that further, what is the 2026 equivalent um, for building websites in the '9s, building mobile apps in the 2010s, building SAS um, in the last cloud era, 

what will look completely obvious in hindsight that is still mostly unbuilt today? >> Um, [clears throat] well, going with the example of menu, I guess, uh, so a lot of this code shouldn't exist and it's just neural network doing most of the work. Um I do think that the extrapolation looks very weird because you could basically imagine I don't I yeah so you could imagine completely neural computers in a certain sense you feed raw videos like imagine a device you takes raw videos or audio 

into basically what's a neural net and uh uses diffusion to render a UI that is kind of like you know unique for that moment in a certain sense and um I kind of feel like in the early days of computing actually people were a little bit confused as to whether computers would look like calculators or computers would look like neural nets and in 50s and 60s it was not really obvious which way would go and of course we went down the calculator path and ended up building classical computing and then neural nets are currently running virtualized on existing computers but you could imagine I think that uh a lot 

of this will flip and that the neural net becomes kind of like the host process and uh the CPUs become kind of like the co-processor so we saw the diagram of you know intelligence compute is going to of neural networks is going to take over and become the dominant spend of flops so you could imagine something really weird and foreign when where neural nets are doing most of the heavy lifting. They're using tool use as this like you know um historical appendage for some kinds of like deterministic tasks. Uh but what's really running the show is these uh neural nets that are in a certain way. Um so you can imagine something 

extremely foreign as the extrapolation but I think we're going to probably get there uh sort of piece by piece. Um and I don't yeah that that progression is TBD I would say. >> [snorts] >> I'd like to talk a little bit about um uh this concept of verifiability, the fact that AI will automate faster and more easily domains where the output can be verified. Um if that framework is right, what work is about to move much faster than people realize and what professions do we have that people actually think are safe but that are 

actually highly verifiable? Uh yes. So I I spent uh some time writing about verifiability and um basically like traditional computers can easily automate what you can specify in code and uh kind of this latest round of LLMs can easily automate what you can uh verify in a certain in a certain sense because the way this works is that when frontier labs are training these LLMs these are giant reinforcement learning environments. So they are given verification rewards and then because of the way that these models are trained they end up basically uh progressing and 

creating these like jagged entities that really peak in capability in kind of like verifiable domains like math and code and adjacent and kind of like stagnate and are a little bit um you know rough around the edges when uh things are not kind of like in that in that space. So I think the reason I wrote about verifiability is I'm trying to understand why these things are so jagged. Um and some of it has to do with how the labs train the models but I think some of it also has to do with um the focus of the labs and what they happen to put into the data distribution. Uh because some things 

basically are significantly more valuable in economy and end up creating more environments because the labs wanted to work in those settings. So I think code is a good example of that. There's probably lots of verifiable environments they could think about that happen not to make it into the mix because they're just not that useful to have the capability around. Um, but I think to me the big um I guess like the big mystery is uh the favorite example for a while was that how many letters are are in a strawberry and the models would famously get this wrong and it's an example of jaggedness. Uh the models now patch this I think but the new one is I want to go to a car wash to wash my 

car and it's 50 meters away. Should I drive or should I walk? And state-of-the-art models today will tell you to walk because it's so close. How is it possible that state-of-the-art Opus 4.7 will simultaneously refactor a 100,000 like [laughter] codebase line codebase or find zero day vulnerabilities and yet tells me to walk to this car wash? This is insane. And to whatever extent these uh models are remain jagged, it's an indication that 

number one maybe something's slightly off or um number two you need to actually be in the loop a little bit and you need to treat them as tools and you do have to kind of stay in touch with what they're doing. And so I think all of my writing long story short about verifiability is just trying to understand um why these things are jacked. Is there any pattern to it? And I think it's some kind of a combination of verifiable plus labs care. Maybe one more anecdote that is instructive is uh from GPT 3.5 to GPT4 people noticed that 

chess improved a lot and I think a lot of people thought oh well it's just a progression of the capabilities but actually it's it's more that uh I think this is public information I think I saw it on the internet um a huge amount of like um data of chess made it into the pre-training set and just because it's in a data distribution uh basically the model improved a lot more than it would just by default. So someone at OpenAI decided to add this data and now you have a capability that just peaked a lot more. And so that's why I think I'm stressing this um dimension of it as we 

are slightly at the mercy of whatever the labs are doing, whatever they happen to put into the mix. And you have to actually explore this thing that they give you that has no manual. And it works in certain settings, but maybe not in some settings. And you have to kind of um explore it a little bit. And uh if you're in the circuits that were part of the RL, you fly. And if you're in the circuits that are out of the data distribution, uh you're going to struggle and you have to kind of figure out which which circuits you're in in your application. And if you and if you're not in the circuits, then you have to really look at fine-tuning and 

doing some of your own work because it's not going to necessarily come out of the LLM out of the box. >> I'd love to come back to the concept of jagged intelligence in a little bit. Um, if you are a founder today and thinking about building a company, you are trying to solve a problem that you think is tractable, something that uh is a domain that is verifiable, but you look around and you think, "Oh my gosh, well, the labs have really really started uh getting to escape velocity in the ones that seem most obvious, math, coding, 

and others." What would your advice be to to the founders in the audience? Um so I think maybe that comes to the previous question of I do think that verifiability because it um let me think. So verifiability makes something tractable in the current paradigm because you can throw a huge amount of RL at it. Um so maybe one way to see it is that uh that remains true even if the labs are not focusing on it directly. So if you are in a verifiable setting where 

you could create these RL environments or examples then that actually sets you up to potentially do your own fine tuning and you might benefit from that. But that is fundamentally technology that just works. You can pull a lever if you have huge amount of diverse data sets of RL environments etc. Uh you can use your favorite fine-tuning framework and um and uh pull the lever and get something that actually uh works pretty well. So um I don't know what the examples of this might be. Um, but I do think there are some very valuable uh reinforcement learning environments that people could think of that I think are not part of the Yeah, I don't want to 

give away the answer, but there is one domain that I think is very uh Oh, okay. Sorry, I don't mean to vape post on on the stage, but there are some examples of this. >> On the flip side, what do you think still feels automatable only from a distance? >> I do think that ultimately almost everything can be made uh verifiable to some extent. some things easier than others. Um because even for like things like writing or so on, you can imagine having a council of LLM judges and probably get get to some get get something uh reasonable out of the um 

from from this kind of an approach. So it's more about what's easy or hard. Um so I I do think that ultimately um uh yeah, I think uh >> everything [laughter] >> everything is automatable. >> Amazing. Okay. Um, so last year you coined the term vibe coding and today we're in a world that feels a little bit more serious, more regent engineering. What do you think is the difference between the two and what would you actually call what we're in today? >> Uh, yeah. So I would say vibe coding is about raising the floor for everyone in 

terms of what they can do in software. So the floor rises, everyone can vibe code anything and that's amazing, incredible. But then I would say agentic engineering is about preserving the quality bar of what existed before in professional software. So you're not allowed to introduce vulnerabilities due to VIP coding. Um you are um you're still responsible for your software just as before, but can you go faster? And spoiler is you can but how do you how do you do that properly? And so to me agentic engineering when I call it that because I do think it's kind of like an engineering discipline. You have these 

agents which are these like spiky entities. They're a bit fable, a little bit stocastic, but they are extremely powerful. is how do you how do you coordinate them to go faster without sacrificing your quality bar and doing that well and correctly um is the the realm of agentic engineering um so I kind of see them as as different like one is about maybe raising the raising the floor and the other is about um you know extrapolating and what I'm seeing I think is there is a very high ceiling on agentic engineer uh capability and you 

know people used to talk about the 10x engineer previously I think that this is magnified a lot more 10x is uh is not uh the speed up you gain. Um and I think uh it does seem to me like people who are very good at this um peak a lot more than 10x uh from from my perspective right now. >> I really like that framing. Um one thing that when Sam Alman came to AIN last year, one memorable thing he said was that people of different generations use chatpt differently. So if you're in your 30s, you use it as a Google search 

replacement. But if you're in your teens, tragic is your gateway to the internet. What is the parallel here in coding today? If we were to watch two people code using OpenClaw, Claude Code, Codeex, one you'd consider mediocre at it and one you would consider fully AI native. How would you describe the difference? >> [clears throat] >> I mean I think it's a just trying to get the most out of the tools that are available utilizing all of their features investing into your own um kind of setup. Uh so just like previously all 

the engineers are used to basically getting the most out of the tools you use either it's vim or v code or now it's you know cloth code or codec or so on. So um just investing into your setup um and um utilizing a lot of the you know uh tools that are available to you. Um and I think it just kind of looks like that. I do think that um maybe related thought is um a lot of people are maybe hiring um for this right because they want to hire strong agentic 

engineers. I do think that um what I'm seeing is that uh the you know most people have still not refactored their um their hiring process for a gentic engineer capability right like if you're giving out puzzles to solve and this is still the old paradigm I would say that hiring have to has to look like give me a really big project and see someone implement that big project like let's write say a Twitter clone uh for agents and then uh make it really good make it really secure and then have some agents 

uh simulate some activity uh on this Twitter and then I'm going to use 10 codecs 5.4x for X high to try to break your break your um uh this website that you deployed and they're going to try to basically break it and they should not be able to break it. And so maybe it looks like that, right? And so yeah, watching people in that that setting and building bigger uh projects and uh utilize utilizing the tooling is maybe what I would uh look at for the most part. >> And as agents do more, what human skill 

do you think becomes more valuable, not less? >> Uh so um yeah, it's a good question. I think um well right now the answer is that the agents are kind of like these intern entities right so it's remarkable um you basically still have to be in charge of the aesthetics the the judgment the taste and a little bit of oversight maybe one one of my favorite examples of like the the weirdness of agents is um for menu genen uh you sign up with a Google Google account but you 

um purchase credits using a stripe account and both of them have email addresses and my agent actually tried to basically um like when you purchase credits, it assigned it using the email address from Stripe to the Google email address like there wasn't a persistent user ID that that uh for people it was trying to match up the email addresses, but you could use different email address for your Stripe and your Google and basically would not associate the funds. And so this is the kind of thing that these agents still will make mistakes about is like why would you use email 

addresses to try to crossorrelate the funds? They can be arbitrary. You can use different emails, etc. Like this is such a weird thing to do. So I think people have to be in charge of this spec, this plan. And um I actually don't even like the plan mode. I I would I mean obviously it's very useful, but I think there's something more general here where you have to work with your agent to design a spec that is very detailed and maybe it's uh maybe basically the docs and then get the agents to write them and you're in charge of the oversight and the top level categories, but the agents are 

doing a lot of the under the hood. And um so I think you're not caring about some of the details. So as an example also with um arrays or tensors in neural networks. Um there's a ton of details between PyTorch and NumPy and all the different like pandas and so on for all the different little API details. And I I already forgot about the keep dims versus keep dim or whether it's dim or axis or reshape or permute or transpose. I don't remember this stuff anymore, right? Because you don't have to. This is the kind of details that are handled by the intern because they have very good recall and but you still have to know for example that um you know 

there's underlying tensor there's an underlying view and then you can manipulate view of the same storage or you can have different storage which would be less efficient and so you still have to have an understanding of what this stuff is doing and some of the fundamentals um so that you're not copying memory around unnecessarily and so on but uh the details of the APIs are now handed off so it um you're in charge of the taste the engineering the design um and that it makes sense and that you're asking for the right things and that you're saying that okay that these have to be unique user IDs that we're 

going to tie everything to um and so you're doing some of the design and development and the engineers are doing the fill in the blanks and that's currently kind of like where we are and I think that's what everyone of course is seeing I think right now >> do you think there's a chance that this um taste and judgment matters less over time or will the ceiling just keep rising >> um yeah it's a good question I would Okay. Um, I mean, I'm hoping that the that it improves. I think probably the reason it 

doesn't improve right now is again, it's not part of the RL. There's probably no aesthetics cost or reward or it's not good enough or something like that. Um, I do think that when you actually look at the code, sometimes I get a little bit of a heart attack because it's not like super amazing code necessarily all the time and it's very bloaty and there's a lot of copy paste and there's awkward abstractions that are brittle and like it works but it's just really gross. Um, and I do I do hope that this can improve in future models. Um, a good example also is this uh you know micro GPT project which where I was trying to 

simplify uh LLM training to be as simple as possible. The models hate this. They can't do it. I tried to I keep I kept trying to prompt an LLM to simplify more simplify more and it just can't you feel like you're outside of the RL circuits. It feels like you're obviously you know you're pulling teeth. It's not like light speed. So I think um I do think that people are still remain in charge of this. But I do think that there's nothing fundamental again that's preventing it. It's just the labs haven't done it yet almost. 

>> Yeah. >> So I'd love to come back to this idea of uh jagged forms of intelligence. you wrote a little bit about this with a very thoughtprovoking piece around animals versus ghosts. Um, and the idea is that we're not building animals, we are summoning ghosts. Um, and these are jagged forms of intelligence that are shaped by data and reward functions, but not by intrinsic motivation or fun or curiosity or empowerment. Uh, things that kind of came about via evolution. um why does that framing matter and what 

does it actually change about how you build and deploy and evaluate or even trust them? >> Uh yeah, so yeah, I think the reason I wrote about this is because I'm trying to wrap my head around what these things are, right? Because if you have a good model of what they are or are not, then you're going to be more competent at uh using them. Um and I do think that um I don't know if it has I'm not sure if it actually has like real power. [laughter] I think it's a little bit of philosophizing. Um, but I do think that 

um I think it's just um coming to terms with the fact that these things are not, you know, animal intelligences. Like if you yell at them, they're not going to work better or worse or it doesn't have any impact. Um, and uh it's all just kind of like these statistical simulation circuits where the the substrate is pre-training so like statistics and then but then there's RL bolting on top. So, it kind of like increases the dispendages and um maybe 

it's just kind of like a mindset of what I'm coming into or what's likely to work or not likely to work or how to modify it. But I don't actually I don't know that I have like here are the five obvious outcomes of how to make your system better. It's more just being suspicious of it and um >> figuring out over time. >> That's where it starts. Um okay, so you are so deep in working with agents that don't just chat. They have um real permissions. They have local context. they actually take action on your be your behalf. What does the world look like when we all start to live in that 

world? >> Uh yeah, I think I think every a lot of people probably here are excited about what this agent uh you know native agentic environment looks like and everything has to be rewritten. Everything is still fundamentally written for humans and has to be moved around. I still use most of the time when I use uh different frameworks or libraries or things like that, they still have docs that are fundamentally written for humans. This is my favorite pet peeve. Like I don't uh why are people still telling me what to do? Like I don't want to do anything. What is the thing I should copy paste to my agent? 

[laughter] Like uh so it's just um every time I'm told, you know, go to this URL or something like that, it's just like ah [laughter] you know. [snorts] So um everyone is I think excited about how do we decompose the workloads that need to happen into fundamentally sensors over the world, actuators over the world. How do we make it agent native? Uh basically describe it to agents first. um and then have a lot of automation around um you know the um yeah around data structures that are 

very legible to the LLMs. Uh so I think um yeah I'm hoping that there's a lot of agent first um infrastructure out there and that you know for Menuguen famously when I wrote the uh not I'm not sure how famously but when I wrote the blog post about Menuguen [laughter] um a lot of the work a lot of the trouble was not even writing the code for Menugen it was deploying it in versell because I had to work with all these different services and I had to string them up and I had to go to their settings and the menus and you know configure my DNS and it was just so annoying and so that's a good example of I would hope that menu gen that I could 

give a prompt to an LLM build menu genen and then I didn't have to touch anything and it's deployed in that same way on the internet. Uh I think that would be a good kind of a test for whether or not uh a lot of our infrastructure is becoming more and more agent native. And then ultimately I would say yeah I I do think we're going towards a world where um there's agent representation for people and for organizations and um you know I'll have my agent talk to your agent uh to figure out some of the details of our meetings or or things 

like that. So, [laughter] um I do think that that's uh roughly where things are going, but um yeah, I think everyone here is excited about that. >> I really like the visual analogy of sensors and actuators. I actually hadn't thought of that. That's super interesting, >> right? >> Um okay, I think we have to end on a question about education. Um because you are probably one of the very best in the world at making complex technical concepts simple and deeply thoughtful about how we design education around it. Um, what still remains worth learning deeply when intelligence gets cheap as 

we move into the next a era of AI? >> Yeah. Uh, there was a tweet that blew my mind recently and I keep thinking about it like every other day. It was something along the lines of um, you can outsource your thinking but you can't outsource your understanding. And um, >> I think that's really nicely put. I so yeah because I still I'm still part of the system and I still I still have to somehow information still has to make it into my brain and I feel like I'm becoming a bottleneck of just even knowing what are we trying to build why 

is it worth doing uh how do I direct you know how do I direct my my agents and so on so I do still think that ultimately something has to direct the thinking and the processing and so on and um that's still kind of fundamentally constrained somehow by understanding and this is one reason I also was very excited about all the LM knowledge bases because I feel like that's that's a way for me to process information and anytime I see a different projection onto information. I always like feel like I gain insight. So it's really just a lot of prompts for me to do synthetic data generation kind of 

over over some fixed data. Uh so I I really enjoy uh whenever I read an article I have my uh you know my wiki that's being built up from these articles and I love asking questions about things or um and I I think that ultimately these are tools to enhance understanding in a certain way and this is still kind of like a bit of a bottleneck because then you can't direct the you can't be a good director if you still uh because the LM certainly don't excel at understanding you still are uniquely in charge of that. So, uh, yeah, I think, uh, tools to that effect, 

I think are incredibly interesting and exciting. >> I'm excited to be back here in a couple years and to see if we've been fully automated out of the loop and they actually take care of understanding as well. Uh, thank you so much for joining us, Andre. We really appreciate it. [applause] 

<p>
 <span data-rw-start="2.08" data-rw-transcript-version="2">
 We're so excited for our very first
 </span>
 <span data-rw-start="3.679" data-rw-transcript-version="2">
 special guest. He has helped build
 </span>
 <span data-rw-start="6.319" data-rw-transcript-version="2">
 modern AI, then explain modern AI, and
 </span>
 <span data-rw-start="10.32" data-rw-transcript-version="2">
 then occasionally rename modern AI. He
 </span>
 <span data-rw-start="14.88" data-rw-transcript-version="2">
 actually helped co-found open AI. Right
 </span>
 <span data-rw-start="16.64" data-rw-transcript-version="2">
 inside of this office. Was the one who
 </span>
 <span data-rw-start="18.64" data-rw-transcript-version="2">
 actually got Autopilot working at Tesla
 </span>
 <span data-rw-start="21.039" data-rw-transcript-version="2">
 back in the day, and he has a rare gift
 </span>
 <span data-rw-start="23.76" data-rw-transcript-version="2">
 of making the most complex technical
 </span>
 <span data-rw-start="26.48" data-rw-transcript-version="2">
 shifts feel both accessible and
 </span>
 <span data-rw-start="28.64" data-rw-transcript-version="2">
 inevitable.
 </span>
</p>
<p>
 <span data-rw-start="30.16" data-rw-transcript-version="2">
 You all know him for having coined the
 </span>
 <span data-rw-start="31.76" data-rw-transcript-version="2">
 term vibe coding last year, but just in
 </span>
 <span data-rw-start="35.04" data-rw-transcript-version="2">
 the last few months, he said something
 </span>
 <span data-rw-start="36.48" data-rw-transcript-version="2">
 even more startling. That he's never
 </span>
 <span data-rw-start="38.879" data-rw-transcript-version="2">
 felt more behind as a programmer. That's
 </span>
 <span data-rw-start="41.52" data-rw-transcript-version="2">
 where we're starting today. Thank you,
 </span>
 <span data-rw-start="43.04" data-rw-transcript-version="2">
 Andre, for joining us.
 </span>
</p>
<p>
 <span data-rw-start="44.16" data-rw-transcript-version="2">
 &gt;&gt; Yeah. Hello. Excited to be here and to
 </span>
 <span data-rw-start="46" data-rw-transcript-version="2">
 kick us off.
 </span>
</p>
<p>
 <span data-rw-start="47.12" data-rw-transcript-version="2">
 &gt;&gt; Okay. So, just a couple of months ago, you
 </span>
 <span data-rw-start="49.52" data-rw-transcript-version="2">
 said that you've never felt more behind
 </span>
 <span data-rw-start="51.12" data-rw-transcript-version="2">
 as a programmer. That's startling to
 </span>
 <span data-rw-start="53.039" data-rw-transcript-version="2">
 hear from you of all people. Um, can you
 </span>
 <span data-rw-start="55.36" data-rw-transcript-version="2">
 help us unpack that? Was that feeling
 </span>
 <span data-rw-start="57.199" data-rw-transcript-version="2">
 Exhilarating or unsettling?
 </span>
</p>
<p>
 <span data-rw-start="60.16" data-rw-transcript-version="2">
 &gt;&gt; Uh, yeah, a mixture of both, for sure. Uh,
 </span>
 <span data-rw-start="62.48" data-rw-transcript-version="2">
 Well, first of all, um,
 </span>
 <span data-rw-start="65.28" data-rw-transcript-version="2">
 I guess, like, as many of you, I've been
 </span>
 <span data-rw-start="66.96" data-rw-transcript-version="2">
 using agentic tools like lots of code,
 </span>
 <span data-rw-start="68.4" data-rw-transcript-version="2">
 adjacent things, uh, for a while, maybe
 </span>
 <span data-rw-start="70" data-rw-transcript-version="2">
 over the last year as it came out, and it
 </span>
 <span data-rw-start="72" data-rw-transcript-version="2">
 was very good at, you know, chunks of code,
 </span>
 <span data-rw-start="73.68" data-rw-transcript-version="2">
 and sometimes it would mess up, and you
 </span>
 <span data-rw-start="75.2" data-rw-transcript-version="2">
 have to edit them, and it was kind of
 </span>
 <span data-rw-start="76.32" data-rw-transcript-version="2">
 helpful. Then I would say December
 </span>
 <span data-rw-start="78.4" data-rw-transcript-version="2">
 was this, uh, clear point where, for me, I
 </span>
 <span data-rw-start="81.439" data-rw-transcript-version="2">
 was on a break, so I had a bit more time.
 </span>
</p>
<p>
 <span data-rw-start="82.799" data-rw-transcript-version="2">
 I think many other people were similar,
 </span>
 <span data-rw-start="84.96" data-rw-transcript-version="2">
 and, uh, I just started to notice that
 </span>
 <span data-rw-start="86.88" data-rw-transcript-version="2">
 with the latest models, uh, the chunks
 </span>
 <span data-rw-start="88.64" data-rw-transcript-version="2">
 just came out fine, and then I kept
 </span>
 <span data-rw-start="90" data-rw-transcript-version="2">
 asking for more, and it just came out
 </span>
 <span data-rw-start="91.28" data-rw-transcript-version="2">
 fine. Then I can't remember the last
 </span>
 <span data-rw-start="92.64" data-rw-transcript-version="2">
 time I corrected it, and then I was, I
 </span>
 <span data-rw-start="94.799" data-rw-transcript-version="2">
 just, you know, trusted the system more
 </span>
 <span data-rw-start="96.479" data-rw-transcript-version="2">
 and more. Then I was vibe coding,
 </span>
 <span data-rw-start="98.251" data-rw-transcript-version="2">
 [laughter],
 </span>
 <span data-rw-start="99.04" data-rw-transcript-version="2">
 and, uh, so it was kind of a, I do think
 </span>
 <span data-rw-start="102.079" data-rw-transcript-version="2">
 that it was a very stark transition.
 </span>
</p>
<p>
 <span data-rw-start="103.6" data-rw-transcript-version="2">
 I think that a lot of people actually, I
 </span>
 <span data-rw-start="105.04" data-rw-transcript-version="2">
 tried to, I tried to stress this on uh,
 </span>
 <span data-rw-start="107.28" data-rw-transcript-version="2">
 Twitter and or X because I think a lot
 </span>
 <span data-rw-start="109.68" data-rw-transcript-version="2">
 of people experienced AI last year as
 </span>
 <span data-rw-start="112.079" data-rw-transcript-version="2">
 ChatGPT adjacent thing. Uh, but you
 </span>
 <span data-rw-start="114.32" data-rw-transcript-version="2">
 really had to look again and you had to
 </span>
 <span data-rw-start="115.92" data-rw-transcript-version="2">
 look as of December, uh, because things
 </span>
 <span data-rw-start="118" data-rw-transcript-version="2">
 have changed fundamentally, and uh,
 </span>
 <span data-rw-start="119.68" data-rw-transcript-version="2">
 especially on this like agentic, coherent
 </span>
 <span data-rw-start="121.92" data-rw-transcript-version="2">
 workflow, uh, that really started to
 </span>
 <span data-rw-start="124.079" data-rw-transcript-version="2">
 actually work. Um, and so I would say
 </span>
 <span data-rw-start="127.36" data-rw-transcript-version="2">
 that, uh, yeah, it was just that
 </span>
 <span data-rw-start="129.36" data-rw-transcript-version="2">
 realization that really, uh, uh, had me
 </span>
 <span data-rw-start="132.56" data-rw-transcript-version="2">
 go down their whole rabbit hole of
 </span>
 <span data-rw-start="134.239" data-rw-transcript-version="2">
 just, you know, infinity side projects.
 </span>
 <span data-rw-start="136.239" data-rw-transcript-version="2">
 Uh, my side projects folder is like
 </span>
 <span data-rw-start="138.16" data-rw-transcript-version="2">
 extremely full with lots of random
 </span>
 <span data-rw-start="139.599" data-rw-transcript-version="2">
 things and, uh, just, uh, V coding all
 </span>
 <span data-rw-start="141.76" data-rw-transcript-version="2">
 the time. Uh, so, uh, yeah, that kind of
 </span>
 <span data-rw-start="143.76" data-rw-transcript-version="2">
 happened in December, I would say, and I
 </span>
 <span data-rw-start="145.68" data-rw-transcript-version="2">
 was looking at the repercussions of that
 </span>
 <span data-rw-start="146.8" data-rw-transcript-version="2">
 since.
 </span>
</p>
<p>
 <span data-rw-start="148.08" data-rw-transcript-version="2">
 &gt;&gt; Um, you've talked a lot about this idea
 </span>
 <span data-rw-start="150" data-rw-transcript-version="2">
 of LLMs as a new computer. Um, that it
 </span>
 <span data-rw-start="153.12" data-rw-transcript-version="2">
 isn't just better software, it's a whole
 </span>
 <span data-rw-start="155.36" data-rw-transcript-version="2">
 New computing paradigm. And um software
 </span>
 <span data-rw-start="158.08" data-rw-transcript-version="2">
 1.0 was explicit rules, software 2.0 was
 </span>
 <span data-rw-start="161.04" data-rw-transcript-version="2">
 learned weights, software 3.0 is this.
 </span>
</p>
<p>
 <span data-rw-start="163.92" data-rw-transcript-version="2">
 Um, if that's actually true, what does a
 </span>
 <span data-rw-start="166.48" data-rw-transcript-version="2">
 team build differently the day they
 </span>
 <span data-rw-start="168.879" data-rw-transcript-version="2">
 actually believe this?
 </span>
</p>
<p>
 <span data-rw-start="170.8" data-rw-transcript-version="2">
 &gt;&gt; Right? So, uh, yeah, exactly. So, software
 </span>
 <span data-rw-start="173.28" data-rw-transcript-version="2">
 1.0, I'm writing code; software 2.0, I'
 </span>
 <span data-rw-start="176" data-rw-transcript-version="2">
 am actually programming by creating data
 </span>
 <span data-rw-start="177.68" data-rw-transcript-version="2">
 sets and training, uh, training neural
 </span>
 <span data-rw-start="179.599" data-rw-transcript-version="2">
 networks. So, the programming is kind of
 </span>
 <span data-rw-start="181.04" data-rw-transcript-version="2">
 like arranging data sets and maybe some
 </span>
 <span data-rw-start="182.48" data-rw-transcript-version="2">
 objectives and neural network
 </span>
 <span data-rw-start="183.519" data-rw-transcript-version="2">
 architectures. And then what happened is
 </span>
 <span data-rw-start="185.28" data-rw-transcript-version="2">
 that basically, if you train one of these
 </span>
 <span data-rw-start="187.44" data-rw-transcript-version="2">
 GPT models or LLMs on a sufficiently
 </span>
 <span data-rw-start="189.76" data-rw-transcript-version="2">
 large set of tasks, implicit, basically, um
 </span>
 <span data-rw-start="192.4" data-rw-transcript-version="2">
 implicitly, because by training on the
 </span>
 <span data-rw-start="194.4" data-rw-transcript-version="2">
 internet, you have to multitask all the
 </span>
 <span data-rw-start="195.68" data-rw-transcript-version="2">
 things that are in the dataset. Uh,
 </span>
 <span data-rw-start="197.28" data-rw-transcript-version="2">
 these actually become kind of like a
 </span>
 <span data-rw-start="198.8" data-rw-transcript-version="2">
 programmable computer, in a certain
 </span>
 <span data-rw-start="200" data-rw-transcript-version="2">
 sense. So, software 3.0 now is kind of
 </span>
 <span data-rw-start="201.76" data-rw-transcript-version="2">
 about, uh, you know, your programming now,
 </span>
 <span data-rw-start="204" data-rw-transcript-version="2">
 turns to prompting, and what's in the
 </span>
</p>
<p>
 <span data-rw-start="205.84" data-rw-transcript-version="2">
 Context window is your lever over the
 </span>
 <span data-rw-start="208.48" data-rw-transcript-version="2">
 interpreter that is the LLM that is kind
 </span>
 <span data-rw-start="210.48" data-rw-transcript-version="2">
 of like interpreting your context and uh
 </span>
 <span data-rw-start="212.4" data-rw-transcript-version="2">
 performing computation in the dig
 </span>
 <span data-rw-start="214.159" data-rw-transcript-version="2">
 digital information space. So I guess um
 </span>
 <span data-rw-start="217.76" data-rw-transcript-version="2">
 yeah that's kind of the transition and I
 </span>
 <span data-rw-start="219.84" data-rw-transcript-version="2">
 think there's a few examples of that
 </span>
 <span data-rw-start="221.12" data-rw-transcript-version="2">
 really drove it home for me and maybe
 </span>
 <span data-rw-start="222.56" data-rw-transcript-version="2">
 that might be instructive. Uh so for
 </span>
 <span data-rw-start="224.879" data-rw-transcript-version="2">
 example, when you when openclaw came out,
 </span>
 <span data-rw-start="228" data-rw-transcript-version="2">
 when you want to install openclaw, you
 </span>
 <span data-rw-start="229.76" data-rw-transcript-version="2">
 would expect that normally this is a
 </span>
 <span data-rw-start="230.879" data-rw-transcript-version="2">
 bash script, like a shell script. So
 </span>
 <span data-rw-start="232.72" data-rw-transcript-version="2">
 run the shell script to install
 </span>
 <span data-rw-start="234.64" data-rw-transcript-version="2">
 openclaw. Um, but the thing is that in
 </span>
 <span data-rw-start="237.36" data-rw-transcript-version="2">
 order to target lots of different
 </span>
 <span data-rw-start="238.56" data-rw-transcript-version="2">
 platforms and lots of different types of
 </span>
 <span data-rw-start="240.08" data-rw-transcript-version="2">
 computers, you might run openclaw.
 </span>
</p>
<p>
 <span data-rw-start="241.68" data-rw-transcript-version="2">
 These shell scripts usually balloon
 </span>
 <span data-rw-start="243.2" data-rw-transcript-version="2">
 up and become extremely complex. But the
 </span>
 <span data-rw-start="245.12" data-rw-transcript-version="2">
 thing is, you're still stuck in a
 </span>
 <span data-rw-start="246.159" data-rw-transcript-version="2">
 software 1.0 universe of wanting to
 </span>
 <span data-rw-start="247.84" data-rw-transcript-version="2">
 write the code. And actually, the open
 </span>
 <span data-rw-start="249.84" data-rw-transcript-version="2">
 claw installation is a copy paste
 </span>
 <span data-rw-start="252" data-rw-transcript-version="2">
 of a bunch of text that you're
 </span>
 <span data-rw-start="253.92" data-rw-transcript-version="2">
 Supposed to give to your agent. Uh, so
 </span>
 <span data-rw-start="255.76" data-rw-transcript-version="2">
 basically, it's a little skill of, uh,
 </span>
 <span data-rw-start="258.079" data-rw-transcript-version="2">
 you know, copy-paste this and give it to
 </span>
 <span data-rw-start="259.28" data-rw-transcript-version="2">
 your agent, and it will install Open
 </span>
 <span data-rw-start="260.639" data-rw-transcript-version="2">
 Claw. And the reason this is a lot more
 </span>
 <span data-rw-start="262.079" data-rw-transcript-version="2">
 powerful is you're working now in the
 </span>
 <span data-rw-start="263.6" data-rw-transcript-version="2">
 software 3.0 paradigm where you don't
 </span>
 <span data-rw-start="265.199" data-rw-transcript-version="2">
 have to precisely spell out, you know, all
 </span>
 <span data-rw-start="267.759" data-rw-transcript-version="2">
 the individual details of that setup.
 </span>
</p>
<p>
 <span data-rw-start="269.44" data-rw-transcript-version="2">
 The agent has its own intelligence that
 </span>
 <span data-rw-start="270.96" data-rw-transcript-version="2">
 it packages up, and then it kind of like
 </span>
 <span data-rw-start="272.56" data-rw-transcript-version="2">
 follows the instructions, and it looks at
 </span>
 <span data-rw-start="274.639" data-rw-transcript-version="2">
 your environment, your computer, and it
 </span>
 <span data-rw-start="276.4" data-rw-transcript-version="2">
 kind of like performs intelligent
 </span>
 <span data-rw-start="277.44" data-rw-transcript-version="2">
 actions to make things work, and it
 </span>
 <span data-rw-start="278.639" data-rw-transcript-version="2">
 debugs things in the loop, and it's just
 </span>
 <span data-rw-start="280.4" data-rw-transcript-version="2">
 like so much more powerful, right? So I
 </span>
 <span data-rw-start="282.96" data-rw-transcript-version="2">
 think that's a very different kind of
 </span>
 <span data-rw-start="284.479" data-rw-transcript-version="2">
 way of thinking about it, just
 </span>
 <span data-rw-start="286" data-rw-transcript-version="2">
 like, what is the piece of text to copy,
 </span>
 <span data-rw-start="287.52" data-rw-transcript-version="2">
 paste to your agent? That's the
 </span>
 <span data-rw-start="288.72" data-rw-transcript-version="2">
 programming paradigm. Now I think one
 </span>
 <span data-rw-start="290.56" data-rw-transcript-version="2">
 more, maybe, uh, example that comes to mind
 </span>
 <span data-rw-start="292.56" data-rw-transcript-version="2">
 that is even more extreme than that, is
 </span>
 <span data-rw-start="294.16" data-rw-transcript-version="2">
 when I was building, um, menu genen. So,
 </span>
 <span data-rw-start="296.72" data-rw-transcript-version="2">
 Menu genen is this idea where you, um, you
 </span>
 <span data-rw-start="300.4" data-rw-transcript-version="2">
 come to a restaurant, they give you a
 </span>
 <span data-rw-start="301.919" data-rw-transcript-version="2">
 menu. There's no pictures usually. So, I
 </span>
 <span data-rw-start="303.68" data-rw-transcript-version="2">
 don't know what any of these things are.
 </span>
</p>
<p>
 <span data-rw-start="305.28" data-rw-transcript-version="2">
 Usually like 30% of the things I have
 </span>
 <span data-rw-start="307.68" data-rw-transcript-version="2">
 no idea what they are, 50%. So, I wanted
 </span>
 <span data-rw-start="309.68" data-rw-transcript-version="2">
 to take a photo of the restaurant menu
 </span>
 <span data-rw-start="312" data-rw-transcript-version="2">
 and to get pictures of what those things
 </span>
 <span data-rw-start="313.84" data-rw-transcript-version="2">
 might look like in a generic sense. And
 </span>
 <span data-rw-start="316.24" data-rw-transcript-version="2">
 so I built, I've coded this app that
 </span>
 <span data-rw-start="318.24" data-rw-transcript-version="2">
 basically lets you upload a photo and it
 </span>
 <span data-rw-start="320.08" data-rw-transcript-version="2">
 does all this stuff and it runs on
 </span>
 <span data-rw-start="321.44" data-rw-transcript-version="2">
 Verscell, and, uh, it basically re-renders
 </span>
 <span data-rw-start="324.88" data-rw-transcript-version="2">
 the menu, and it gives you all the
 </span>
 <span data-rw-start="326.72" data-rw-transcript-version="2">
 items, and it gives you a picture that it
 </span>
 <span data-rw-start="328.32" data-rw-transcript-version="2">
 uses an image, um, you know, generator, uh,
 </span>
 <span data-rw-start="331.039" data-rw-transcript-version="2">
 for, to basically OCR all the different
 </span>
 <span data-rw-start="333.84" data-rw-transcript-version="2">
 titles, uh, use the image generator to get
 </span>
 <span data-rw-start="335.919" data-rw-transcript-version="2">
 pictures of them, and then shows it to
 </span>
 <span data-rw-start="337.039" data-rw-transcript-version="2">
 you. And then I saw the software 3.0
 </span>
 <span data-rw-start="339.84" data-rw-transcript-version="2">
 version of this, which is, which blew my
 </span>
 <span data-rw-start="341.68" data-rw-transcript-version="2">
 mind, which is literally just take your
 </span>
 <span data-rw-start="343.199" data-rw-transcript-version="2">
 photo, give it to Gemini and say, use
 </span>
 <span data-rw-start="346" data-rw-transcript-version="2">
 Nanobanana to overlay the things
 </span>
 <span data-rw-start="348.88" data-rw-transcript-version="2">
 onto the menu. Uh, and Nanobanana,
 </span>
 <span data-rw-start="351.44" data-rw-transcript-version="2">
 Basically, it returned an image that is
 </span>
 <span data-rw-start="352.96" data-rw-transcript-version="2">
 exactly the picture of the menu that I
 </span>
 <span data-rw-start="354.32" data-rw-transcript-version="2">
 took, but it actually put into the pixels.
 </span>
</p>
<p>
 <span data-rw-start="356.639" data-rw-transcript-version="2">
 It rendered the different things in the
 </span>
 <span data-rw-start="358.479" data-rw-transcript-version="2">
 menu, and this blew my mind because
 </span>
 <span data-rw-start="362.08" data-rw-transcript-version="2">
 actually, all of my menu generation is spurious.
 </span>
 <span data-rw-start="364.319" data-rw-transcript-version="2">
 It's working in the old paradigm that
 </span>
 <span data-rw-start="366.16" data-rw-transcript-version="2">
 app shouldn't exist, uh, and uh, yeah, the
 </span>
 <span data-rw-start="369.039" data-rw-transcript-version="2">
 software 3.0 paradigm is a lot more kind
 </span>
 <span data-rw-start="371.36" data-rw-transcript-version="2">
 of raw. It just, um, your neural network
 </span>
 <span data-rw-start="374" data-rw-transcript-version="2">
 is doing more and more of the work, and
 </span>
 <span data-rw-start="375.84" data-rw-transcript-version="2">
 your prompt or context is just the image,
 </span>
 <span data-rw-start="378.08" data-rw-transcript-version="2">
 and the output is an image. There's
 </span>
 <span data-rw-start="379.84" data-rw-transcript-version="2">
 no need to have any of the app in
 </span>
 <span data-rw-start="381.44" data-rw-transcript-version="2">
 between. Um, so I think that people have
 </span>
 <span data-rw-start="384.96" data-rw-transcript-version="2">
 to kind of like reframe, you know, not to
 </span>
 <span data-rw-start="387.84" data-rw-transcript-version="2">
 work in the existing paradigm of what things
 </span>
 <span data-rw-start="390" data-rw-transcript-version="2">
 existed and just think about it as a
 </span>
 <span data-rw-start="391.44" data-rw-transcript-version="2">
 speed-up of what exists. It's actually
 </span>
 <span data-rw-start="393.84" data-rw-transcript-version="2">
 like new things are available now. And
 </span>
 <span data-rw-start="396" data-rw-transcript-version="2">
 going back to your programming question,
 </span>
 <span data-rw-start="397.36" data-rw-transcript-version="2">
 it's not even, I think, that's also an
 </span>
 <span data-rw-start="398.88" data-rw-transcript-version="2">
 example of working in the old
 </span>
 <span data-rw-start="400.479" data-rw-transcript-version="2">
 mindset because it's not just about
 </span>
 <span data-rw-start="401.68" data-rw-transcript-version="2">
 programming and programming becoming.
 </span>
</p>
<p>
 <span data-rw-start="402.88" data-rw-transcript-version="2">
 Faster. This is more general information
 </span>
 <span data-rw-start="404.96" data-rw-transcript-version="2">
 processing that is automatable now. So
 </span>
 <span data-rw-start="407.36" data-rw-transcript-version="2">
 Um, it’s not just even about code. So
 </span>
 <span data-rw-start="409.44" data-rw-transcript-version="2">
 Previous code worked over kind of like
 </span>
 <span data-rw-start="411.6" data-rw-transcript-version="2">
 structured data, right? And, uh, you write
 </span>
 <span data-rw-start="413.44" data-rw-transcript-version="2">
 code over structured data. But like, for
 </span>
 <span data-rw-start="415.199" data-rw-transcript-version="2">
 example, with my LLM knowledge basis
 </span>
 <span data-rw-start="416.8" data-rw-transcript-version="2">
 project, um, basically, you get LLMs to
 </span>
 <span data-rw-start="419.759" data-rw-transcript-version="2">
 create wikis for your organization or
 </span>
 <span data-rw-start="421.44" data-rw-transcript-version="2">
 for you in person, etc. This is not even
 </span>
 <span data-rw-start="423.12" data-rw-transcript-version="2">
 a program. This is not something that
 </span>
 <span data-rw-start="424.319" data-rw-transcript-version="2">
 could exist before because there was no
 </span>
 <span data-rw-start="426.72" data-rw-transcript-version="2">
 there was no code that would create a
 </span>
 <span data-rw-start="428.08" data-rw-transcript-version="2">
 knowledge base based on a bunch of
 </span>
 <span data-rw-start="429.36" data-rw-transcript-version="2">
 facts. But now, you can just take these
 </span>
</p>
<p>
 <span data-rw-start="430.96" data-rw-transcript-version="2">
 documents and, uh, basically, uh, recompile
 </span>
 <span data-rw-start="434" data-rw-transcript-version="2">
 them in a different way and, uh, reorder
 </span>
 <span data-rw-start="435.919" data-rw-transcript-version="2">
 them and create something that is, uh, new
 </span>
 <span data-rw-start="437.68" data-rw-transcript-version="2">
 and interesting, uh, as a reframing of the
 </span>
 <span data-rw-start="439.68" data-rw-transcript-version="2">
 data. And so, these are new things that
 </span>
 <span data-rw-start="442.4" data-rw-transcript-version="2">
 weren't possible. Uh, and so I think this
 </span>
 <span data-rw-start="444.639" data-rw-transcript-version="2">
 is, uh, something that I keep trying to
 </span>
 <span data-rw-start="446.56" data-rw-transcript-version="2">
 get back to, as to not only what can we
 </span>
 <span data-rw-start="449.039" data-rw-transcript-version="2">
 do that existed that is faster now, but I
 </span>
 <span data-rw-start="451.039" data-rw-transcript-version="2">
 think there are new opportunities of just
 </span>
 <span data-rw-start="453.52" data-rw-transcript-version="2">
 Things that couldn't be possible before,
 </span>
 <span data-rw-start="455.039" data-rw-transcript-version="2">
 and I almost think that that's more
 </span>
 <span data-rw-start="456.24" data-rw-transcript-version="2">
 exciting.
 </span>
</p>
<p>
 <span data-rw-start="457.199" data-rw-transcript-version="2">
 &gt;&gt; I love the menu generation progression and
 </span>
 <span data-rw-start="460" data-rw-transcript-version="2">
 dichotomy that you laid out, and I think
 </span>
 <span data-rw-start="461.84" data-rw-transcript-version="2">
 even I'm sure many folks here followed
 </span>
 <span data-rw-start="463.84" data-rw-transcript-version="2">
 your own progression of programming from
 </span>
 <span data-rw-start="465.52" data-rw-transcript-version="2">
 last October to early January or February,
 </span>
 <span data-rw-start="468.88" data-rw-transcript-version="2">
 this year. Um, if you extrapolate that
 </span>
 <span data-rw-start="471.039" data-rw-transcript-version="2">
 further, what is the 2026 equivalent, um,
 </span>
 <span data-rw-start="474.56" data-rw-transcript-version="2">
 for building websites in the '90s,
 </span>
 <span data-rw-start="476.96" data-rw-transcript-version="2">
 building mobile apps in the 2010s,
 </span>
 <span data-rw-start="479.52" data-rw-transcript-version="2">
 building SaaS in the last cloud era,
 </span>
 <span data-rw-start="482.56" data-rw-transcript-version="2">
 what will look completely obvious in
 </span>
 <span data-rw-start="484.56" data-rw-transcript-version="2">
 hindsight that is still mostly unbuilt
 </span>
 <span data-rw-start="486.72" data-rw-transcript-version="2">
 today?
 </span>
</p>
<p>
 <span data-rw-start="488" data-rw-transcript-version="2">
 &gt;&gt; Um, [clears throat] well, going with the
 </span>
 <span data-rw-start="490.24" data-rw-transcript-version="2">
 example of menu, I guess, uh, so a lot
 </span>
 <span data-rw-start="492.4" data-rw-transcript-version="2">
 of this code shouldn't exist, and it's
 </span>
 <span data-rw-start="493.52" data-rw-transcript-version="2">
 just neural network doing most of the
 </span>
 <span data-rw-start="495.199" data-rw-transcript-version="2">
 work. Um, I do think that the
 </span>
 <span data-rw-start="497.12" data-rw-transcript-version="2">
 extrapolation looks very weird because
 </span>
 <span data-rw-start="499.12" data-rw-transcript-version="2">
 you could basically imagine
 </span>
 <span data-rw-start="501.44" data-rw-transcript-version="2">
 I don't, I... so you could imagine
 </span>
 <span data-rw-start="503.599" data-rw-transcript-version="2">
 completely neural computers in a certain
 </span>
 <span data-rw-start="505.44" data-rw-transcript-version="2">
 Sense you feed raw videos like imagine a
 </span>
 <span data-rw-start="508.8" data-rw-transcript-version="2">
 device. You take raw videos or audio
 </span>
 <span data-rw-start="510.479" data-rw-transcript-version="2">
 into basically what's a neural net, and
 </span>
 <span data-rw-start="512.719" data-rw-transcript-version="2">
 uh uses diffusion to render a UI that is
 </span>
 <span data-rw-start="515.2" data-rw-transcript-version="2">
 kind of like you know, unique for that
 </span>
 <span data-rw-start="517.44" data-rw-transcript-version="2">
 moment in a certain sense. And, um, I kind
 </span>
 <span data-rw-start="520.56" data-rw-transcript-version="2">
 of feel like in the early days of
 </span>
 <span data-rw-start="522.159" data-rw-transcript-version="2">
 computing, actually, people were a little
 </span>
 <span data-rw-start="523.36" data-rw-transcript-version="2">
 bit confused as to whether computers
 </span>
</p>
<p>
 <span data-rw-start="525.04" data-rw-transcript-version="2">
 would look like calculators or computers
 </span>
 <span data-rw-start="526.8" data-rw-transcript-version="2">
 would look like neural nets. And, in the 50s
 </span>
 <span data-rw-start="528.48" data-rw-transcript-version="2">
 and 60s, it was not really obvious which
 </span>
 <span data-rw-start="530.32" data-rw-transcript-version="2">
 way would go. And, of course, we went down
 </span>
 <span data-rw-start="532.16" data-rw-transcript-version="2">
 the calculator path and ended up
 </span>
 <span data-rw-start="533.36" data-rw-transcript-version="2">
 building classical computing. And then,
 </span>
 <span data-rw-start="535.12" data-rw-transcript-version="2">
 neural nets are currently running
 </span>
 <span data-rw-start="536.32" data-rw-transcript-version="2">
 virtually on existing computers. But
 </span>
 <span data-rw-start="538.16" data-rw-transcript-version="2">
 you could imagine, I think, that
 </span>
 <span data-rw-start="540.24" data-rw-transcript-version="2">
 a lot of this will flip and that the neural
 </span>
 <span data-rw-start="541.6" data-rw-transcript-version="2">
 net becomes kind of like the host
 </span>
 <span data-rw-start="542.959" data-rw-transcript-version="2">
 process, and, uh, the CPUs become kind of
 </span>
 <span data-rw-start="545.6" data-rw-transcript-version="2">
 like the co-processor. So, we saw the
 </span>
 <span data-rw-start="547.6" data-rw-transcript-version="2">
 diagram of, you know, intelligence, compute,
 </span>
 <span data-rw-start="549.279" data-rw-transcript-version="2">
 is going to, of neural networks, is going
 </span>
 <span data-rw-start="550.8" data-rw-transcript-version="2">
 to take over and become the dominant.
 </span>
</p>
<p>
 <span data-rw-start="552.959" data-rw-transcript-version="2">
 Spend of flops so you could imagine something really weird and foreign when
 </span>
 <span data-rw-start="554.88" data-rw-transcript-version="2">
 where neural nets are doing most of the
 </span>
 <span data-rw-start="557.2" data-rw-transcript-version="2">
 heavy lifting. They're using tool use as
 </span>
 <span data-rw-start="558.8" data-rw-transcript-version="2">
 this like, you know, um, historical
 </span>
 <span data-rw-start="560.32" data-rw-transcript-version="2">
 appendage for some kinds of like
 </span>
 <span data-rw-start="562.88" data-rw-transcript-version="2">
 deterministic tasks. Uh, but what's
 </span>
 <span data-rw-start="565.76" data-rw-transcript-version="2">
 really running the show is these, uh,
 </span>
 <span data-rw-start="567.6" data-rw-transcript-version="2">
 neural nets that are in a certain way.
 </span>
 <span data-rw-start="569.92" data-rw-transcript-version="2">
 Um, so you can imagine something
 </span>
 <span data-rw-start="571.279" data-rw-transcript-version="2">
 extremely foreign as the extrapolation,
 </span>
 <span data-rw-start="573.12" data-rw-transcript-version="2">
 but I think we're going to probably get
 </span>
 <span data-rw-start="574.64" data-rw-transcript-version="2">
 there, uh, sort of piece by piece. Um, and
 </span>
 <span data-rw-start="576.72" data-rw-transcript-version="2">
 I don't, yeah, that progression is
 </span>
 <span data-rw-start="579.12" data-rw-transcript-version="2">
 TBD, I would say.
 </span>
</p>
<p>
 <span data-rw-start="580.991" data-rw-transcript-version="2">
 &gt;&gt; [snorts]
 </span>
 <span data-rw-start="581.12" data-rw-transcript-version="2">
 &gt;&gt; I'd like to talk a little bit about, um
 </span>
 <span data-rw-start="583.279" data-rw-transcript-version="2">
 this concept of verifiability, the
 </span>
 <span data-rw-start="585.279" data-rw-transcript-version="2">
 fact that AI will automate faster and
 </span>
 <span data-rw-start="587.519" data-rw-transcript-version="2">
 more easily domains where the output can
 </span>
 <span data-rw-start="589.839" data-rw-transcript-version="2">
 be verified. Um, if that framework is
 </span>
 <span data-rw-start="592.48" data-rw-transcript-version="2">
 right, what work is about to move much
 </span>
 <span data-rw-start="594.32" data-rw-transcript-version="2">
 faster than people realize, and what
 </span>
 <span data-rw-start="596.399" data-rw-transcript-version="2">
 professions do we have that people
 </span>
 <span data-rw-start="598.64" data-rw-transcript-version="2">
 actually think are safe but that are
 </span>
 <span data-rw-start="600.48" data-rw-transcript-version="2">
 Actually, highly verifiable?
 </span>
</p>
<p>
 <span data-rw-start="602.8" data-rw-transcript-version="2">
 Uh, yes. So I spent some time
 </span>
 <span data-rw-start="605.36" data-rw-transcript-version="2">
 writing about verifiability and,
 </span>
 <span data-rw-start="607.519" data-rw-transcript-version="2">
 basically, like, traditional computers can
 </span>
 <span data-rw-start="609.68" data-rw-transcript-version="2">
 easily automate what you can specify in
 </span>
 <span data-rw-start="612.399" data-rw-transcript-version="2">
 code. And, uh, kind of, this latest round of
 </span>
 <span data-rw-start="614.959" data-rw-transcript-version="2">
 LLMs can easily automate what you can, uh,
 </span>
 <span data-rw-start="616.959" data-rw-transcript-version="2">
 verify in a certain, in a certain sense,
 </span>
 <span data-rw-start="619.519" data-rw-transcript-version="2">
 because, the way that this works is that when
 </span>
 <span data-rw-start="620.959" data-rw-transcript-version="2">
 frontier labs are training these LLMs,
 </span>
 <span data-rw-start="622.72" data-rw-transcript-version="2">
 these are giant reinforcement learning
 </span>
 <span data-rw-start="624.079" data-rw-transcript-version="2">
 environments. So, they are given
 </span>
 <span data-rw-start="625.519" data-rw-transcript-version="2">
 verification rewards, and then, because of
 </span>
 <span data-rw-start="628.16" data-rw-transcript-version="2">
 the way that these models are trained,
 </span>
 <span data-rw-start="629.68" data-rw-transcript-version="2">
 they end up basically, uh, progressing and
 </span>
 <span data-rw-start="632" data-rw-transcript-version="2">
 creating these, like, jagged entities that
 </span>
 <span data-rw-start="634.24" data-rw-transcript-version="2">
 really peak in capability, in kind of
 </span>
 <span data-rw-start="636.32" data-rw-transcript-version="2">
 verifiable domains, like math and
 </span>
 <span data-rw-start="637.76" data-rw-transcript-version="2">
 code, and adjacent and, kind of, like,
 </span>
</p>
<p>
 <span data-rw-start="639.44" data-rw-transcript-version="2">
 stagnate, and are a little bit, uh, you
 </span>
 <span data-rw-start="641.6" data-rw-transcript-version="2">
 know, rough around the edges when, uh,
 </span>
 <span data-rw-start="643.279" data-rw-transcript-version="2">
 things are not, kind of, like, in that space. So, I think the reason I
 </span>
 <span data-rw-start="644.959" data-rw-transcript-version="2">
 wrote about verifiability is, I’m trying
 </span>
 <span data-rw-start="646.48" data-rw-transcript-version="2">
 to understand why these things are so
 </span>
 <span data-rw-start="649.519" data-rw-transcript-version="2">
 Jagged. Um, and some of it has to do with
 </span>
 <span data-rw-start="652.16" data-rw-transcript-version="2">
 how the labs train the models, but I
 </span>
 <span data-rw-start="654" data-rw-transcript-version="2">
 think some of it also has to do with, um
 </span>
 <span data-rw-start="655.839" data-rw-transcript-version="2">
 the focus of the labs and what they
 </span>
 <span data-rw-start="657.519" data-rw-transcript-version="2">
 happen to put into the data
 </span>
 <span data-rw-start="658.88" data-rw-transcript-version="2">
 distribution. Uh, because some things
 </span>
 <span data-rw-start="660.8" data-rw-transcript-version="2">
 basically are significantly more
 </span>
 <span data-rw-start="661.92" data-rw-transcript-version="2">
 valuable in economy and end up creating
 </span>
 <span data-rw-start="663.76" data-rw-transcript-version="2">
 more environments, because the labs
 </span>
 <span data-rw-start="665.04" data-rw-transcript-version="2">
 wanted to work in those settings. So, I
 </span>
 <span data-rw-start="666.72" data-rw-transcript-version="2">
 think code is a good example of that.
 </span>
</p>
<p>
 <span data-rw-start="668.16" data-rw-transcript-version="2">
 There’s probably lots of verifiable
 </span>
 <span data-rw-start="669.44" data-rw-transcript-version="2">
 environments they could think about that
 </span>
 <span data-rw-start="670.88" data-rw-transcript-version="2">
 happen not to make it into the mix
 </span>
 <span data-rw-start="672.079" data-rw-transcript-version="2">
 because they’re just not that useful to
 </span>
 <span data-rw-start="673.279" data-rw-transcript-version="2">
 have the capability around. Um, but I
 </span>
 <span data-rw-start="675.92" data-rw-transcript-version="2">
 think, to me, the big, um, I guess, like the
 </span>
 <span data-rw-start="678.48" data-rw-transcript-version="2">
 big mystery is, uh, the favorite example
 </span>
 <span data-rw-start="681.12" data-rw-transcript-version="2">
 for a while was that how many letters
 </span>
 <span data-rw-start="682.959" data-rw-transcript-version="2">
 are in a strawberry, and the models
 </span>
 <span data-rw-start="684.56" data-rw-transcript-version="2">
 would famously get this wrong, and it’s
 </span>
 <span data-rw-start="686" data-rw-transcript-version="2">
 an example of jaggedness. Uh, the models
 </span>
 <span data-rw-start="687.92" data-rw-transcript-version="2">
 now patch this, I think, but the new one
 </span>
 <span data-rw-start="689.76" data-rw-transcript-version="2">
 is, I want to go to a car wash to wash my
 </span>
 <span data-rw-start="692.16" data-rw-transcript-version="2">
 car, and it’s 50 meters away. Should I
 </span>
 <span data-rw-start="694.48" data-rw-transcript-version="2">
 Drive or should I walk? And
 </span>
 <span data-rw-start="696.8" data-rw-transcript-version="2">
 state-of-the-art models today will tell
 </span>
 <span data-rw-start="698.399" data-rw-transcript-version="2">
 you to walk because it's so close. How
 </span>
 <span data-rw-start="700.959" data-rw-transcript-version="2">
 is it possible that state-of-the-art
 </span>
 <span data-rw-start="702.959" data-rw-transcript-version="2">
 Opus 4.7 will simultaneously refactor a
 </span>
 <span data-rw-start="706.079" data-rw-transcript-version="2">
 100,000 line [laughter] codebase or find zero day
 </span>
</p>
<p>
 <span data-rw-start="708.8" data-rw-transcript-version="2">
 vulnerabilities, and yet tells me to walk
 </span>
 <span data-rw-start="712.56" data-rw-transcript-version="2">
 to this car wash? This is insane. And to
 </span>
 <span data-rw-start="716.48" data-rw-transcript-version="2">
 whatever extent these models are
 </span>
 <span data-rw-start="718.959" data-rw-transcript-version="2">
 remain jagged, it's an indication that
 </span>
 <span data-rw-start="721.279" data-rw-transcript-version="2">
 number one maybe something's slightly
 </span>
 <span data-rw-start="722.48" data-rw-transcript-version="2">
 off or, um, number two, you need to
 </span>
 <span data-rw-start="725.6" data-rw-transcript-version="2">
 actually be in the loop a little bit, and
 </span>
 <span data-rw-start="727.76" data-rw-transcript-version="2">
 you need to treat them as tools, and you
 </span>
 <span data-rw-start="729.36" data-rw-transcript-version="2">
 do have to kind of stay in touch with
 </span>
 <span data-rw-start="731.2" data-rw-transcript-version="2">
 what they're doing. And so, I think all
 </span>
 <span data-rw-start="732.88" data-rw-transcript-version="2">
 of my writing, long story short, about
 </span>
 <span data-rw-start="734.48" data-rw-transcript-version="2">
 verifiability is just trying to
 </span>
 <span data-rw-start="736.079" data-rw-transcript-version="2">
 understand why these things are
 </span>
 <span data-rw-start="738.48" data-rw-transcript-version="2">
 jacked. Is there any pattern to it? And
 </span>
 <span data-rw-start="740.399" data-rw-transcript-version="2">
 I think it's some kind of a combination
 </span>
 <span data-rw-start="742.079" data-rw-transcript-version="2">
 of verifiable plus labs care. Maybe one
 </span>
 <span data-rw-start="745.2" data-rw-transcript-version="2">
 more anecdote that is instructive is, uh,
 </span>
 <span data-rw-start="748.079" data-rw-transcript-version="2">
 from GPT 3.5 to GPT 4, people noticed that.
 </span>
</p>
<p>
 <span data-rw-start="751.04" data-rw-transcript-version="2">
 Chess improved a lot, and I think a lot
 </span>
 <span data-rw-start="753.2" data-rw-transcript-version="2">
 of people thought, oh well, it's just a
 </span>
 <span data-rw-start="754.48" data-rw-transcript-version="2">
 progression of the capabilities, but
 </span>
 <span data-rw-start="756.24" data-rw-transcript-version="2">
 actually, it's more that, uh, I think
 </span>
 <span data-rw-start="758" data-rw-transcript-version="2">
 this is public information. I think I saw
 </span>
 <span data-rw-start="759.36" data-rw-transcript-version="2">
 it on the internet. Um, a huge amount of
 </span>
 <span data-rw-start="761.12" data-rw-transcript-version="2">
 like, um, data of chess made it into the
 </span>
 <span data-rw-start="763.76" data-rw-transcript-version="2">
 pre-training set, and just because it's
 </span>
 <span data-rw-start="766" data-rw-transcript-version="2">
 in a data distribution, uh, basically the
 </span>
 <span data-rw-start="768.32" data-rw-transcript-version="2">
 model improved a lot more than it would
 </span>
 <span data-rw-start="770.16" data-rw-transcript-version="2">
 just by default. So, someone at OpenAI
 </span>
 <span data-rw-start="773.12" data-rw-transcript-version="2">
 decided to add this data, and now you
 </span>
 <span data-rw-start="775.12" data-rw-transcript-version="2">
 have a capability that just peaked a lot
 </span>
 <span data-rw-start="776.8" data-rw-transcript-version="2">
 more. And so, that's why I think I'm
 </span>
 <span data-rw-start="778.32" data-rw-transcript-version="2">
 stressing this, um, dimension of it, as we
 </span>
 <span data-rw-start="781.519" data-rw-transcript-version="2">
 are slightly at the mercy of whatever
 </span>
 <span data-rw-start="783.04" data-rw-transcript-version="2">
 the labs are doing, whatever they happen
 </span>
 <span data-rw-start="784.639" data-rw-transcript-version="2">
 to put into the mix. And you have to
 </span>
</p>
<p>
 <span data-rw-start="786.24" data-rw-transcript-version="2">
 actually explore this thing that they
 </span>
 <span data-rw-start="788" data-rw-transcript-version="2">
 give you, that has no manual, and it
 </span>
 <span data-rw-start="790.16" data-rw-transcript-version="2">
 works in certain settings, but maybe not
 </span>
 <span data-rw-start="791.68" data-rw-transcript-version="2">
 in some settings. And you have to kind
 </span>
 <span data-rw-start="793.68" data-rw-transcript-version="2">
 of, um, explore it a little bit. And, uh, if
 </span>
 <span data-rw-start="796.56" data-rw-transcript-version="2">
 you're in the circuits that were part of
 </span>
 <span data-rw-start="797.839" data-rw-transcript-version="2">
 the RL, you fly. And if you're in the
 </span>
 <span data-rw-start="799.92" data-rw-transcript-version="2">
 Circuits that are out of the data
 </span>
 <span data-rw-start="801.519" data-rw-transcript-version="2">
 distribution, uh you're going to
 </span>
 <span data-rw-start="802.88" data-rw-transcript-version="2">
 struggle, and you have to kind of figure
 </span>
 <span data-rw-start="804.24" data-rw-transcript-version="2">
 out which circuits you're in in
 </span>
 <span data-rw-start="806.16" data-rw-transcript-version="2">
 your application. And if you, and if
 </span>
 <span data-rw-start="808.16" data-rw-transcript-version="2">
 you're not in the circuits, then you
 </span>
 <span data-rw-start="809.519" data-rw-transcript-version="2">
 have to really look at fine-tuning and
 </span>
 <span data-rw-start="810.959" data-rw-transcript-version="2">
 doing some of your own work because it's
 </span>
 <span data-rw-start="812.88" data-rw-transcript-version="2">
 not going to necessarily come out of the
 </span>
 <span data-rw-start="814.079" data-rw-transcript-version="2">
 LLM out of the box.
 </span>
</p>
<p>
 <span data-rw-start="816.639" data-rw-transcript-version="2">
 &gt;&gt;&gt; I'd love to come back to the concept of
 </span>
 <span data-rw-start="818.079" data-rw-transcript-version="2">
 jagged intelligence in a little bit. Um,
 </span>
 <span data-rw-start="820.24" data-rw-transcript-version="2">
 if you are a founder today and thinking
 </span>
 <span data-rw-start="822.48" data-rw-transcript-version="2">
 about building a company, you are trying
 </span>
 <span data-rw-start="824.8" data-rw-transcript-version="2">
 to solve a problem that you think is
 </span>
 <span data-rw-start="826.8" data-rw-transcript-version="2">
 tractable, something that uh is a domain
 </span>
 <span data-rw-start="829.04" data-rw-transcript-version="2">
 that is verifiable, but you look around
 </span>
 <span data-rw-start="831.36" data-rw-transcript-version="2">
 and you think, "Oh my gosh, well, the
 </span>
 <span data-rw-start="833.12" data-rw-transcript-version="2">
 labs have really really started uh
 </span>
 <span data-rw-start="836.56" data-rw-transcript-version="2">
 getting to escape velocity in the ones
 </span>
 <span data-rw-start="838.56" data-rw-transcript-version="2">
 that seem most obvious, math, coding,
 </span>
 <span data-rw-start="840.8" data-rw-transcript-version="2">
 and others." What would your advice be
 </span>
 <span data-rw-start="842.639" data-rw-transcript-version="2">
 to to the founders in the audience?
 </span>
</p>
<p>
 <span data-rw-start="845.68" data-rw-transcript-version="2">
 Um
 </span>
 <span data-rw-start="848.639" data-rw-transcript-version="2">
 so I think maybe that comes to the
 </span>
 <span data-rw-start="850.48" data-rw-transcript-version="2">
 Previous question of I do think that
 </span>
 <span data-rw-start="852.079" data-rw-transcript-version="2">
 verifiability because it, um, let me
 </span>
 <span data-rw-start="854.8" data-rw-transcript-version="2">
 think. So verifiability makes something
 </span>
 <span data-rw-start="857.04" data-rw-transcript-version="2">
 tractable in the current paradigm
 </span>
 <span data-rw-start="858.639" data-rw-transcript-version="2">
 because you can throw a huge amount of
 </span>
 <span data-rw-start="860.32" data-rw-transcript-version="2">
 RL at it. Um, so maybe one way to see it
 </span>
 <span data-rw-start="864.56" data-rw-transcript-version="2">
 is that, uh, that remains true even if the
 </span>
 <span data-rw-start="866.8" data-rw-transcript-version="2">
 labs are not focusing on it directly. So
 </span>
 <span data-rw-start="868.639" data-rw-transcript-version="2">
 if you are in a verifiable setting where
 </span>
 <span data-rw-start="870.56" data-rw-transcript-version="2">
 you could create these RL environments
 </span>
 <span data-rw-start="871.839" data-rw-transcript-version="2">
 or examples, then that actually sets you
 </span>
 <span data-rw-start="874.079" data-rw-transcript-version="2">
 up to potentially do your own fine
 </span>
 <span data-rw-start="875.279" data-rw-transcript-version="2">
 tuning, and you might benefit from that.
 </span>
</p>
<p>
 <span data-rw-start="876.72" data-rw-transcript-version="2">
 But that is fundamentally technology
 </span>
 <span data-rw-start="878.079" data-rw-transcript-version="2">
 that just works. You can pull a lever if
 </span>
 <span data-rw-start="879.76" data-rw-transcript-version="2">
 you have huge amount of diverse data
 </span>
 <span data-rw-start="881.199" data-rw-transcript-version="2">
 sets of RL environments, etc. Uh, you can
 </span>
 <span data-rw-start="883.44" data-rw-transcript-version="2">
 use your favorite fine-tuning framework
 </span>
 <span data-rw-start="884.959" data-rw-transcript-version="2">
 and, um, and, uh, pull the lever and get
 </span>
 <span data-rw-start="887.92" data-rw-transcript-version="2">
 something that actually, uh, works pretty
 </span>
 <span data-rw-start="889.199" data-rw-transcript-version="2">
 well. So, um, I don't know what the
 </span>
 <span data-rw-start="891.92" data-rw-transcript-version="2">
 examples of this might be. Um, but I do
 </span>
 <span data-rw-start="894.959" data-rw-transcript-version="2">
 think there are some very valuable, uh,
 </span>
 <span data-rw-start="896.48" data-rw-transcript-version="2">
 reinforcement learning environments that
 </span>
 <span data-rw-start="898.16" data-rw-transcript-version="2">
 people could think of that I think are
 </span>
 <span data-rw-start="899.519" data-rw-transcript-version="2">
 Not part of the. Yeah, I don't want to
 </span>
 <span data-rw-start="901.279" data-rw-transcript-version="2">
 give away the answer, but there is one
 </span>
 <span data-rw-start="902.72" data-rw-transcript-version="2">
 domain that I think is very, uh. Oh, okay.
 </span>
</p>
<p>
 <span data-rw-start="904.8" data-rw-transcript-version="2">
 Sorry, I don't mean to vape post on the stage, but there are some examples
 </span>
 <span data-rw-start="906.48" data-rw-transcript-version="2">
 of this.
 </span>
 <span data-rw-start="908.639" data-rw-transcript-version="2">
 &gt;&gt; On the flip side, what do you think
 </span>
 <span data-rw-start="911.04" data-rw-transcript-version="2">
 still feels automatable only from a
 </span>
 <span data-rw-start="913.04" data-rw-transcript-version="2">
 distance?
 </span>
 <span data-rw-start="914.959" data-rw-transcript-version="2">
 &gt;&gt; I do think that ultimately, almost
 </span>
 <span data-rw-start="917.279" data-rw-transcript-version="2">
 everything can be made, uh, verifiable to
 </span>
 <span data-rw-start="919.44" data-rw-transcript-version="2">
 some extent,
 </span>
 <span data-rw-start="921.04" data-rw-transcript-version="2">
 some things easier than
 </span>
 <span data-rw-start="923.839" data-rw-transcript-version="2">
 others. Because even for like things
 </span>
 <span data-rw-start="925.68" data-rw-transcript-version="2">
 like writing or so on, you can imagine
 </span>
 <span data-rw-start="927.839" data-rw-transcript-version="2">
 having a council of LLM judges and
 </span>
 <span data-rw-start="929.76" data-rw-transcript-version="2">
 probably get, get to some, get, get
 </span>
 <span data-rw-start="931.76" data-rw-transcript-version="2">
 something, uh, reasonable out of the, um,
 </span>
 <span data-rw-start="933.36" data-rw-transcript-version="2">
 from this kind of an approach. So
 </span>
 <span data-rw-start="936.639" data-rw-transcript-version="2">
 it's more about what's easy or hard. Uh,
 </span>
 <span data-rw-start="940.32" data-rw-transcript-version="2">
 so I, I do think that ultimately, uh, uh,
 </span>
 <span data-rw-start="942" data-rw-transcript-version="2">
 &gt;&gt; everything [laughter]
 </span>
 <span data-rw-start="943.199" data-rw-transcript-version="2">
 &gt;&gt; everything is automatable.
 </span>
 <span data-rw-start="945.68" data-rw-transcript-version="2">
 &gt;&gt; Amazing. Okay. Um, so last year you
 </span>
 <span data-rw-start="947.6" data-rw-transcript-version="2">
 coined the term vibe coding and today
 </span>
 <span data-rw-start="949.279" data-rw-transcript-version="2">
 We're in a world that feels a little bit
 </span>
 <span data-rw-start="950.8" data-rw-transcript-version="2">
 more serious, more regent engineering.
 </span>
</p>
<p>
 <span data-rw-start="952.959" data-rw-transcript-version="2">
 What do you think is the difference
 </span>
 <span data-rw-start="954.16" data-rw-transcript-version="2">
 between the two and what would you
 </span>
 <span data-rw-start="955.36" data-rw-transcript-version="2">
 actually call what we're in today?
 </span>
</p>
<p>
 <span data-rw-start="957.36" data-rw-transcript-version="2">
 &gt;&gt; Uh, yeah. So I would say vibe coding is
 </span>
 <span data-rw-start="959.12" data-rw-transcript-version="2">
 about raising the floor for everyone in
 </span>
 <span data-rw-start="961.12" data-rw-transcript-version="2">
 terms of what they can do in software.
 </span>
 <span data-rw-start="963.04" data-rw-transcript-version="2">
 So the floor rises, everyone can vibe
 </span>
 <span data-rw-start="965.12" data-rw-transcript-version="2">
 code anything and that's amazing,
 </span>
 <span data-rw-start="966.639" data-rw-transcript-version="2">
 incredible. But then I would say agentic
 </span>
 <span data-rw-start="968.639" data-rw-transcript-version="2">
 engineering is about preserving the
 </span>
 <span data-rw-start="970.079" data-rw-transcript-version="2">
 quality bar of what existed before in
 </span>
 <span data-rw-start="971.92" data-rw-transcript-version="2">
 professional software. So you're not
 </span>
 <span data-rw-start="973.839" data-rw-transcript-version="2">
 allowed to introduce vulnerabilities due
 </span>
 <span data-rw-start="975.92" data-rw-transcript-version="2">
 to vibe coding. Um you are um you're
 </span>
 <span data-rw-start="978.88" data-rw-transcript-version="2">
 still responsible for your software just
 </span>
 <span data-rw-start="980.32" data-rw-transcript-version="2">
 as before, but can you go faster? And
 </span>
 <span data-rw-start="982.639" data-rw-transcript-version="2">
 spoiler is you can but how do you how do
 </span>
 <span data-rw-start="984.8" data-rw-transcript-version="2">
 you do that properly? And so to me
 </span>
 <span data-rw-start="986.24" data-rw-transcript-version="2">
 agentic engineering when I call it that
 </span>
 <span data-rw-start="988.24" data-rw-transcript-version="2">
 because I do think it's kind of like an
 </span>
 <span data-rw-start="989.6" data-rw-transcript-version="2">
 engineering discipline. You have these
 </span>
 <span data-rw-start="991.199" data-rw-transcript-version="2">
 agents which are these like spiky
 </span>
 <span data-rw-start="992.48" data-rw-transcript-version="2">
 entities. They're a bit fable, a little
 </span>
 <span data-rw-start="993.839" data-rw-transcript-version="2">
 Bit stochastic, but they are extremely
 </span>
</p>
<p>
 <span data-rw-start="995.759" data-rw-transcript-version="2">
 powerful. How do you, how do you
 </span>
 <span data-rw-start="997.68" data-rw-transcript-version="2">
 coordinate them to go faster without
 </span>
 <span data-rw-start="999.839" data-rw-transcript-version="2">
 sacrificing your quality bar? And doing
 </span>
 <span data-rw-start="1002.48" data-rw-transcript-version="2">
 that well and correctly, um, is the (the)
 </span>
 <span data-rw-start="1006" data-rw-transcript-version="2">
 realm of agentic engineering. Um, so I
 </span>
 <span data-rw-start="1008.88" data-rw-transcript-version="2">
 kind of see them as different — like
 </span>
 <span data-rw-start="1010.079" data-rw-transcript-version="2">
 one is about maybe raising the raise
 </span>
 <span data-rw-start="1011.759" data-rw-transcript-version="2">
 the floor, and the other is about, um, you
 </span>
 <span data-rw-start="1013.6" data-rw-transcript-version="2">
 know, extrapolating. And what I'm seeing, I
 </span>
 <span data-rw-start="1015.36" data-rw-transcript-version="2">
 think is there is a very high ceiling on
 </span>
 <span data-rw-start="1018.16" data-rw-transcript-version="2">
 agentic engineering, uh, capability, and you
 </span>
 <span data-rw-start="1021.199" data-rw-transcript-version="2">
 know, people used to talk about the 10x
 </span>
 <span data-rw-start="1022.72" data-rw-transcript-version="2">
 engineer. Previously, I think this is
 </span>
 <span data-rw-start="1024.72" data-rw-transcript-version="2">
 magnified a lot more — 10x is, uh, is not, uh,
 </span>
 <span data-rw-start="1028.559" data-rw-transcript-version="2">
 the speed-up you gain. Um, and I think, uh,
 </span>
 <span data-rw-start="1031.76" data-rw-transcript-version="2">
 it does seem to me like people who are
 </span>
 <span data-rw-start="1033.52" data-rw-transcript-version="2">
 very good at this, um, peak a lot more
 </span>
 <span data-rw-start="1036.16" data-rw-transcript-version="2">
 than 10x, uh, from my perspective
 </span>
 <span data-rw-start="1038.079" data-rw-transcript-version="2">
 right now.
 </span>
</p>
<p>
 <span data-rw-start="1038.559" data-rw-transcript-version="2">
 &gt;&gt; I really like that framing. Um, one thing
 </span>
 <span data-rw-start="1041.28" data-rw-transcript-version="2">
 that, when Sam Alman came to AIN last
 </span>
 <span data-rw-start="1043.52" data-rw-transcript-version="2">
 year, one memorable thing he said was
 </span>
 <span data-rw-start="1045.199" data-rw-transcript-version="2">
 that people of different generations use
 </span>
 <span data-rw-start="1047.199" data-rw-transcript-version="2">
 chatGPT differently. So, if you're in your
 </span>
 <span data-rw-start="1049.2" data-rw-transcript-version="2">
 30s, you use it as a Google search
 </span>
 <span data-rw-start="1051.2" data-rw-transcript-version="2">
 replacement. But if you're in your
 </span>
 <span data-rw-start="1052.799" data-rw-transcript-version="2">
 teens, tragic is your gateway to the
 </span>
 <span data-rw-start="1055.2" data-rw-transcript-version="2">
 internet. What is the parallel here in
 </span>
 <span data-rw-start="1057.44" data-rw-transcript-version="2">
 coding today? If we were to watch two
 </span>
 <span data-rw-start="1059.28" data-rw-transcript-version="2">
 people code using OpenClaw, Claude Code,
 </span>
 <span data-rw-start="1062.64" data-rw-transcript-version="2">
 Codeex, one you'd consider mediocre at
 </span>
 <span data-rw-start="1065.36" data-rw-transcript-version="2">
 it and one you would consider fully AI
 </span>
 <span data-rw-start="1067.84" data-rw-transcript-version="2">
 native. How would you describe the
 </span>
 <span data-rw-start="1069.6" data-rw-transcript-version="2">
 difference?
 </span>
</p>
<p>
 <span data-rw-start="1071.592" data-rw-transcript-version="2">
 &gt;&gt; [clears throat]
 </span>
 <span data-rw-start="1071.679" data-rw-transcript-version="2">
 &gt;&gt; I mean, I think it's just trying to get
 </span>
 <span data-rw-start="1073.6" data-rw-transcript-version="2">
 the most out of the tools that are
 </span>
 <span data-rw-start="1075.039" data-rw-transcript-version="2">
 available, utilizing all of their
 </span>
 <span data-rw-start="1076.799" data-rw-transcript-version="2">
 features, investing into your own um kind
 </span>
 <span data-rw-start="1079.679" data-rw-transcript-version="2">
 of setup. Uh, so just like previously, all
 </span>
 <span data-rw-start="1082.16" data-rw-transcript-version="2">
 the engineers are used to basically
 </span>
 <span data-rw-start="1083.44" data-rw-transcript-version="2">
 getting the most out of the tools you
 </span>
 <span data-rw-start="1084.48" data-rw-transcript-version="2">
 use, either it's vim or v code or now
 </span>
 <span data-rw-start="1086.559" data-rw-transcript-version="2">
 it's you know cloth code or codec or so
 </span>
 <span data-rw-start="1089.52" data-rw-transcript-version="2">
 on. So, um, just investing into your setup
 </span>
 <span data-rw-start="1093.039" data-rw-transcript-version="2">
 and utilizing a lot of the you
 </span>
 <span data-rw-start="1096.4" data-rw-transcript-version="2">
 know, uh, tools that are available to you.
 </span>
 <span data-rw-start="1098.559" data-rw-transcript-version="2">
 Um, and I think it just kind of looks
 </span>
 <span data-rw-start="1100.799" data-rw-transcript-version="2">
 like that. I do think that, um, maybe
 </span>
 <span data-rw-start="1103.12" data-rw-transcript-version="2">
 Related thought is, um, a lot of people
 </span>
 <span data-rw-start="1106.799" data-rw-transcript-version="2">
 are maybe hiring, um, for this, right?
 </span>
</p>
<p>
 <span data-rw-start="1109.84" data-rw-transcript-version="2">
 Because they want to hire strong agentic
 </span>
 <span data-rw-start="1111.919" data-rw-transcript-version="2">
 engineers. I do think that, um, what I'm
 </span>
 <span data-rw-start="1114.64" data-rw-transcript-version="2">
 seeing is that, uh, the, you know, most
 </span>
 <span data-rw-start="1117.28" data-rw-transcript-version="2">
 people have still not refactored their
 </span>
 <span data-rw-start="1119.44" data-rw-transcript-version="2">
 um, their hiring process for a genetic
 </span>
 <span data-rw-start="1121.919" data-rw-transcript-version="2">
 engineer capability, right? Like, if you're
 </span>
 <span data-rw-start="1124.24" data-rw-transcript-version="2">
 giving out puzzles to solve, and this is
 </span>
 <span data-rw-start="1126.4" data-rw-transcript-version="2">
 still the old paradigm, I would say that
 </span>
 <span data-rw-start="1128.24" data-rw-transcript-version="2">
 hiring has to look like: give me
 </span>
 <span data-rw-start="1130" data-rw-transcript-version="2">
 a really big project, and see someone
 </span>
 <span data-rw-start="1132.4" data-rw-transcript-version="2">
 implement that big project, like, let's
 </span>
 <span data-rw-start="1133.84" data-rw-transcript-version="2">
 write, say, a Twitter clone, uh, for agents,
 </span>
 <span data-rw-start="1137.28" data-rw-transcript-version="2">
 and then, uh, make it really good, make it
 </span>
 <span data-rw-start="1139.039" data-rw-transcript-version="2">
 really secure, and then have some agents
 </span>
</p>
<p>
 <span data-rw-start="1141.52" data-rw-transcript-version="2">
 uh, simulate some activity on this
 </span>
 <span data-rw-start="1143.84" data-rw-transcript-version="2">
 Twitter, and then I'm going to use 10
 </span>
 <span data-rw-start="1146.64" data-rw-transcript-version="2">
 codecs 5.4x for X high to try to break
 </span>
 <span data-rw-start="1149.039" data-rw-transcript-version="2">
 your, uh, break your, uh, this website that
 </span>
 <span data-rw-start="1152.96" data-rw-transcript-version="2">
 you deployed, and they're going to try to
 </span>
 <span data-rw-start="1155.44" data-rw-transcript-version="2">
 basically break it, and they should not
 </span>
 <span data-rw-start="1156.64" data-rw-transcript-version="2">
 be able to break it. And so, maybe it
 </span>
 <span data-rw-start="1158.32" data-rw-transcript-version="2">
 looks like that, right? And so, yeah,
 </span>
 <span data-rw-start="1160" data-rw-transcript-version="2">
 watching people in that setting and
 </span>
 <span data-rw-start="1161.679" data-rw-transcript-version="2">
 Building bigger, uh, projects and uh, utilizing the tooling is maybe
 </span>
 <span data-rw-start="1165.039" data-rw-transcript-version="2">
 what I would, uh, look at for the most
 </span>
 <span data-rw-start="1166.559" data-rw-transcript-version="2">
 part.
 </span>
</p>
<p>
 <span data-rw-start="1168.4" data-rw-transcript-version="2">
 &gt;&gt; And as agents do more, what human skill
 </span>
 <span data-rw-start="1171.28" data-rw-transcript-version="2">
 do you think becomes more valuable, not
 </span>
 <span data-rw-start="1173.679" data-rw-transcript-version="2">
 less?
 </span>
 <span data-rw-start="1174.88" data-rw-transcript-version="2">
 &gt;&gt; Uh, so, um, yeah, it's a good question. I
 </span>
 <span data-rw-start="1177.039" data-rw-transcript-version="2">
 think, um, well, right now the answer is
 </span>
 <span data-rw-start="1179.44" data-rw-transcript-version="2">
 that the agents are kind of like these
 </span>
 <span data-rw-start="1180.559" data-rw-transcript-version="2">
 intern entities, right? So it's remarkable
 </span>
 <span data-rw-start="1184.48" data-rw-transcript-version="2">
 um, you basically still have to be in
 </span>
 <span data-rw-start="1186.96" data-rw-transcript-version="2">
 charge of the aesthetics, the
 </span>
 <span data-rw-start="1188.559" data-rw-transcript-version="2">
 judgment, the taste, and a little bit of
 </span>
 <span data-rw-start="1190.4" data-rw-transcript-version="2">
 oversight, maybe. One of my favorite
 </span>
 <span data-rw-start="1192.48" data-rw-transcript-version="2">
 examples of the weirdness of
 </span>
 <span data-rw-start="1194.559" data-rw-transcript-version="2">
 agents is, um, for menu generation. Uh, you sign
 </span>
 <span data-rw-start="1197.679" data-rw-transcript-version="2">
 up with a Google account, but you
 </span>
 <span data-rw-start="1200.559" data-rw-transcript-version="2">
 purchase credits using a Stripe
 </span>
 <span data-rw-start="1202.559" data-rw-transcript-version="2">
 account, and both of them have email
 </span>
 <span data-rw-start="1204.16" data-rw-transcript-version="2">
 addresses, and my agent actually tried to
 </span>
 <span data-rw-start="1206.32" data-rw-transcript-version="2">
 basically,
 </span>
 <span data-rw-start="1208.4" data-rw-transcript-version="2">
 um, like when you purchase credits, it
 </span>
 <span data-rw-start="1210.88" data-rw-transcript-version="2">
 assigned it using the email address from
 </span>
 <span data-rw-start="1213.039" data-rw-transcript-version="2">
 Stripe to the Google email address, like
 </span>
 <span data-rw-start="1215.76" data-rw-transcript-version="2">
 There wasn't a persistent user ID that
 </span>
 <span data-rw-start="1218" data-rw-transcript-version="2">
 that uh for people it was trying to
 </span>
 <span data-rw-start="1220.32" data-rw-transcript-version="2">
 match up the email addresses, but you
 </span>
 <span data-rw-start="1221.6" data-rw-transcript-version="2">
 could use different email address for
 </span>
 <span data-rw-start="1222.72" data-rw-transcript-version="2">
 your Stripe and your Google and
 </span>
 <span data-rw-start="1224.48" data-rw-transcript-version="2">
 basically would not associate the funds.
 </span>
</p>
<p>
 <span data-rw-start="1226.799" data-rw-transcript-version="2">
 And so this is the kind of thing that
 </span>
 <span data-rw-start="1228.24" data-rw-transcript-version="2">
 these agents still will make mistakes
 </span>
 <span data-rw-start="1229.919" data-rw-transcript-version="2">
 about is like why would you use email
 </span>
 <span data-rw-start="1231.52" data-rw-transcript-version="2">
 addresses to try to crossorrelate the
 </span>
 <span data-rw-start="1233.039" data-rw-transcript-version="2">
 funds? They can be arbitrary. You can
 </span>
 <span data-rw-start="1234.559" data-rw-transcript-version="2">
 use different emails, etc. Like this is
 </span>
 <span data-rw-start="1236.72" data-rw-transcript-version="2">
 such a weird thing to do. So I think
 </span>
 <span data-rw-start="1239.039" data-rw-transcript-version="2">
 people have to be in charge of this
 </span>
 <span data-rw-start="1240.48" data-rw-transcript-version="2">
 spec, this plan. And um I actually'd
 </span>
 <span data-rw-start="1243.52" data-rw-transcript-version="2">
 even like the plan mode. I I would I
 </span>
 <span data-rw-start="1246" data-rw-transcript-version="2">
 mean obviously it's very useful, but I
 </span>
 <span data-rw-start="1247.36" data-rw-transcript-version="2">
 think there's something more general
 </span>
 <span data-rw-start="1248.24" data-rw-transcript-version="2">
 here where you have to work with your
 </span>
 <span data-rw-start="1249.6" data-rw-transcript-version="2">
 agent to design a spec that is very
 </span>
 <span data-rw-start="1251.44" data-rw-transcript-version="2">
 detailed and maybe it's uh maybe
 </span>
 <span data-rw-start="1253.6" data-rw-transcript-version="2">
 basically the docs and then get the
 </span>
</p>
<p>
 <span data-rw-start="1255.36" data-rw-transcript-version="2">
 agents to write them and you're in
 </span>
 <span data-rw-start="1256.96" data-rw-transcript-version="2">
 charge of the oversight and the top
 </span>
 <span data-rw-start="1258.72" data-rw-transcript-version="2">
 level categories, but the agents are
 </span>
 <span data-rw-start="1260.48" data-rw-transcript-version="2">
 Doing a lot of the under the hood. And
 </span>
 <span data-rw-start="1262.48" data-rw-transcript-version="2">
 um, so I think you're not caring about
 </span>
 <span data-rw-start="1264" data-rw-transcript-version="2">
 some of the details. So, as an example,
 </span>
 <span data-rw-start="1265.84" data-rw-transcript-version="2">
 also with arrayors or tensors in neural
 </span>
 <span data-rw-start="1269.2" data-rw-transcript-version="2">
 networks. Um, there's a ton of details
 </span>
 <span data-rw-start="1271.52" data-rw-transcript-version="2">
 between PyTorch and NumPy and all the
 </span>
 <span data-rw-start="1273.28" data-rw-transcript-version="2">
 different like pandas and so on for all
 </span>
 <span data-rw-start="1274.96" data-rw-transcript-version="2">
 the different little API details. And I
 </span>
 <span data-rw-start="1277.28" data-rw-transcript-version="2">
 already forgot about the keep dims
 </span>
 <span data-rw-start="1278.96" data-rw-transcript-version="2">
 versus keep dim or whether it's dim or
 </span>
 <span data-rw-start="1280.64" data-rw-transcript-version="2">
 axis or reshape or permute or transpose.
 </span>
</p>
<p>
 <span data-rw-start="1282.799" data-rw-transcript-version="2">
 I don't remember this stuff anymore,
 </span>
 <span data-rw-start="1284" data-rw-transcript-version="2">
 right? Because you don't have to. This
 </span>
 <span data-rw-start="1285.44" data-rw-transcript-version="2">
 is the kind of details that are handled
 </span>
 <span data-rw-start="1286.64" data-rw-transcript-version="2">
 by the intern because they have very
 </span>
 <span data-rw-start="1288" data-rw-transcript-version="2">
 good recall. And, but you still have to
 </span>
 <span data-rw-start="1290" data-rw-transcript-version="2">
 know, for example, that, um, you know,
 </span>
 <span data-rw-start="1292.08" data-rw-transcript-version="2">
 there's underlying tensor, there's an
 </span>
 <span data-rw-start="1293.679" data-rw-transcript-version="2">
 underlying view, and then you can
 </span>
 <span data-rw-start="1295.28" data-rw-transcript-version="2">
 manipulate view of the same storage or
 </span>
 <span data-rw-start="1297.2" data-rw-transcript-version="2">
 you can have different storage, which
 </span>
 <span data-rw-start="1298.32" data-rw-transcript-version="2">
 would be less efficient. And so, you still
 </span>
 <span data-rw-start="1300.08" data-rw-transcript-version="2">
 have to have an understanding of what
 </span>
 <span data-rw-start="1301.52" data-rw-transcript-version="2">
 this stuff is doing, and some of the
 </span>
 <span data-rw-start="1303.44" data-rw-transcript-version="2">
 fundamentals, um, so that you're not
 </span>
 <span data-rw-start="1305.76" data-rw-transcript-version="2">
 Copying memory around unnecessarily and
 </span>
 <span data-rw-start="1307.6" data-rw-transcript-version="2">
 so on, but uh the details of the APIs are
 </span>
 <span data-rw-start="1310.799" data-rw-transcript-version="2">
 now handed off, so it, um, you're in charge
 </span>
</p>
<p>
 <span data-rw-start="1313.28" data-rw-transcript-version="2">
 of the taste, the engineering, the design,
 </span>
 <span data-rw-start="1315.6" data-rw-transcript-version="2">
 um, and that it makes sense and that
 </span>
 <span data-rw-start="1317.039" data-rw-transcript-version="2">
 you're asking for the right things, and
 </span>
 <span data-rw-start="1318.24" data-rw-transcript-version="2">
 that you're saying that, okay, that these
 </span>
 <span data-rw-start="1319.52" data-rw-transcript-version="2">
 have to be unique user IDs that we're
 </span>
 <span data-rw-start="1321.28" data-rw-transcript-version="2">
 going to tie everything to, um, and so
 </span>
 <span data-rw-start="1323.919" data-rw-transcript-version="2">
 you're doing some of the design and
 </span>
 <span data-rw-start="1326.08" data-rw-transcript-version="2">
 development, and the engineers are doing
 </span>
 <span data-rw-start="1327.36" data-rw-transcript-version="2">
 the fill in the blanks, and that's
 </span>
 <span data-rw-start="1328.88" data-rw-transcript-version="2">
 currently kind of like where we are, and
 </span>
 <span data-rw-start="1330.159" data-rw-transcript-version="2">
 I think that's what everyone, of course,
 </span>
 <span data-rw-start="1331.6" data-rw-transcript-version="2">
 is seeing. I think, right now,
 </span>
 <span data-rw-start="1333.679" data-rw-transcript-version="2">
 &gt;&gt; Do you think there's a chance that this
 </span>
 <span data-rw-start="1335.36" data-rw-transcript-version="2">
 um, taste and judgment matter less over
 </span>
 <span data-rw-start="1338.559" data-rw-transcript-version="2">
 time, or will the ceiling just keep
 </span>
 <span data-rw-start="1340.08" data-rw-transcript-version="2">
 rising?
 </span>
</p>
<p>
 <span data-rw-start="1341.36" data-rw-transcript-version="2">
 &gt;&gt; Um, yeah, it's a good question. I would
 </span>
 <span data-rw-start="1342.72" data-rw-transcript-version="2">
 say, okay.
 </span>
 <span data-rw-start="1345.44" data-rw-transcript-version="2">
 Um, I mean, I hope that it
 </span>
 <span data-rw-start="1348.32" data-rw-transcript-version="2">
 improves. I think probably the reason it
 </span>
 <span data-rw-start="1350.24" data-rw-transcript-version="2">
 doesn't improve right now is, again, it's
 </span>
 <span data-rw-start="1351.52" data-rw-transcript-version="2">
 not part of the RL. There's probably no
 </span>
 <span data-rw-start="1353.2" data-rw-transcript-version="2">
 Aesthetics, cost, or reward, or it's not good enough or something like that. Um, I do think that when you actually look at the code, sometimes I get a little bit of a heart attack because it's not like super amazing code necessarily all the time, and it's very bloaty, and there's a lot of copy-paste, and there are awkward abstractions that are brittle and like it works, but it's just really gross.
 </span>
</p>
<p>
 <span data-rw-start="1375.76" data-rw-transcript-version="2">
 Um, and I do hope that this can improve in future models. Um, a good example also is this, uh, you know, micro GPT project, which I was trying to simplify, uh, LLM training to be as simple as possible.
 </span>
 <span data-rw-start="1379.84" data-rw-transcript-version="2">
 The models hate this. They can't do it. I tried to keep trying to prompt an LLM to simplify more, but it just can't.
 </span>
 <span data-rw-start="1382.08" data-rw-transcript-version="2">
 You feel like you're outside of the RL circuits.
 </span>
 <span data-rw-start="1384.64" data-rw-transcript-version="2">
 It feels like you're, obviously, you know, you're pulling teeth. It's not like light speed,
 </span>
 <span data-rw-start="1386.64" data-rw-transcript-version="2">
 so I think, um, I do think that people are still in charge of this. But I do think that there's
 </span>
 <span data-rw-start="1406.4" data-rw-transcript-version="2">
 Nothing fundamental again that's
 </span>
 <span data-rw-start="1407.6" data-rw-transcript-version="2">
 preventing it. It's just the labs
 </span>
 <span data-rw-start="1408.64" data-rw-transcript-version="2">
 haven't done it yet almost.
 </span>
</p>
<p>
 <span data-rw-start="1410.4" data-rw-transcript-version="2">
 &gt;&gt; Yeah.
 </span>
 <span data-rw-start="1411.039" data-rw-transcript-version="2">
 &gt;&gt; So I'd love to come back to this idea of
 </span>
 <span data-rw-start="1413.36" data-rw-transcript-version="2">
 uh jagged forms of intelligence. You
 </span>
 <span data-rw-start="1416.48" data-rw-transcript-version="2">
 wrote a little bit about this with a
 </span>
 <span data-rw-start="1418.159" data-rw-transcript-version="2">
 very thought-provoking piece around
 </span>
 <span data-rw-start="1419.52" data-rw-transcript-version="2">
 animals versus ghosts. Um, and the idea
 </span>
 <span data-rw-start="1422.64" data-rw-transcript-version="2">
 is that we're not building animals, we
 </span>
 <span data-rw-start="1424.4" data-rw-transcript-version="2">
 are summoning ghosts. Um, and these are
 </span>
 <span data-rw-start="1426.799" data-rw-transcript-version="2">
 jagged forms of intelligence that are
 </span>
 <span data-rw-start="1428.559" data-rw-transcript-version="2">
 shaped by data and reward functions, but
 </span>
 <span data-rw-start="1431.44" data-rw-transcript-version="2">
 not by intrinsic motivation or fun or
 </span>
 <span data-rw-start="1434" data-rw-transcript-version="2">
 curiosity or empowerment. Uh, things
 </span>
 <span data-rw-start="1437.039" data-rw-transcript-version="2">
 that kind of came about via evolution.
 </span>
 <span data-rw-start="1440" data-rw-transcript-version="2">
 Um, why does that framing matter and what
 </span>
 <span data-rw-start="1442.88" data-rw-transcript-version="2">
 does it actually change about how you
 </span>
 <span data-rw-start="1444.48" data-rw-transcript-version="2">
 build and deploy and evaluate or even
 </span>
 <span data-rw-start="1447.12" data-rw-transcript-version="2">
 trust them?
 </span>
 <span data-rw-start="1448.96" data-rw-transcript-version="2">
 &gt;&gt; Uh yeah, so yeah, I think the reason I
 </span>
 <span data-rw-start="1452.559" data-rw-transcript-version="2">
 wrote about this is because I'm trying
 </span>
 <span data-rw-start="1453.76" data-rw-transcript-version="2">
 to wrap my head around what these things
 </span>
 <span data-rw-start="1455.2" data-rw-transcript-version="2">
 are, right? Because if you have a good
 </span>
 <span data-rw-start="1456.64" data-rw-transcript-version="2">
 model of what they are or are not, then
 </span>
 <span data-rw-start="1458.32" data-rw-transcript-version="2">
 You're going to be more competent at uh
 </span>
 <span data-rw-start="1460.08" data-rw-transcript-version="2">
 using them. Um, and I do think that, um, I
 </span>
 <span data-rw-start="1463.76" data-rw-transcript-version="2">
 don't know if it has, I’m not sure if it
 </span>
 <span data-rw-start="1465.919" data-rw-transcript-version="2">
 actually has like real power. [laughter]
 </span>
</p>
<p>
 <span data-rw-start="1468.559" data-rw-transcript-version="2">
 I think it's a little bit of
 </span>
 <span data-rw-start="1469.52" data-rw-transcript-version="2">
 philosophizing. Um, but I do think that,
 </span>
 <span data-rw-start="1473.12" data-rw-transcript-version="2">
 um,
 </span>
 <span data-rw-start="1474.799" data-rw-transcript-version="2">
 I think it's just, um, coming to terms
 </span>
 <span data-rw-start="1476.88" data-rw-transcript-version="2">
 with the fact that these things are not,
 </span>
 <span data-rw-start="1478.64" data-rw-transcript-version="2">
 you know, animal intelligences. Like if
 </span>
 <span data-rw-start="1480.08" data-rw-transcript-version="2">
 you yell at them, they're not going to
 </span>
 <span data-rw-start="1481.279" data-rw-transcript-version="2">
 work better or worse or it doesn't have
 </span>
 <span data-rw-start="1483.2" data-rw-transcript-version="2">
 any impact. Um, and uh, it's all just
 </span>
 <span data-rw-start="1486.799" data-rw-transcript-version="2">
 kind of like these statistical
 </span>
 <span data-rw-start="1488.159" data-rw-transcript-version="2">
 simulation circuits where the the
 </span>
 <span data-rw-start="1490.96" data-rw-transcript-version="2">
 substrate is pre-training, so like
 </span>
 <span data-rw-start="1493.2" data-rw-transcript-version="2">
 statistics, and then but then there's RL
 </span>
 <span data-rw-start="1495.52" data-rw-transcript-version="2">
 bolting on top. So, it kind of like
 </span>
 <span data-rw-start="1497.919" data-rw-transcript-version="2">
 increases the dispendages, and um maybe
 </span>
 <span data-rw-start="1500.4" data-rw-transcript-version="2">
 it's just kind of like a mindset of what
 </span>
 <span data-rw-start="1502.159" data-rw-transcript-version="2">
 I'm coming into, or what's likely to work
 </span>
 <span data-rw-start="1504.08" data-rw-transcript-version="2">
 or not likely to work, or how to modify
 </span>
 <span data-rw-start="1505.84" data-rw-transcript-version="2">
 it. But, I don't actually, I don't know
 </span>
 <span data-rw-start="1507.76" data-rw-transcript-version="2">
 that I have, like, here are the five
 </span>
 <span data-rw-start="1509.36" data-rw-transcript-version="2">
 obvious outcomes of how to make your
 </span>
 <span data-rw-start="1511.279" data-rw-transcript-version="2">
 System better. It's more just being
 </span>
 <span data-rw-start="1512.64" data-rw-transcript-version="2">
 suspicious of it and um
 </span>
 <span data-rw-start="1514.64" data-rw-transcript-version="2">
 &gt;&gt; figuring out over time.
 </span>
</p>
<p>
 <span data-rw-start="1516.48" data-rw-transcript-version="2">
 &gt;&gt; That's where it starts. Um, okay, so you
 </span>
 <span data-rw-start="1518.4" data-rw-transcript-version="2">
 are so deep in working with agents that
 </span>
 <span data-rw-start="1520" data-rw-transcript-version="2">
 they don't just chat. They have um real
 </span>
 <span data-rw-start="1522.559" data-rw-transcript-version="2">
 permissions. They have local context.
 </span>
 <span data-rw-start="1524.88" data-rw-transcript-version="2">
 They actually take action on your be
 </span>
 <span data-rw-start="1526.24" data-rw-transcript-version="2">
 your behalf. What does the world look
 </span>
 <span data-rw-start="1528.24" data-rw-transcript-version="2">
 like when we all start to live in that
 </span>
 <span data-rw-start="1530.08" data-rw-transcript-version="2">
 world?
 </span>
</p>
<p>
 <span data-rw-start="1531.279" data-rw-transcript-version="2">
 &gt;&gt; Uh yeah, I think, I think every, a lot of
 </span>
 <span data-rw-start="1534" data-rw-transcript-version="2">
 people probably here are excited about
 </span>
 <span data-rw-start="1535.6" data-rw-transcript-version="2">
 what this agent, uh, you know, native
 </span>
 <span data-rw-start="1538.24" data-rw-transcript-version="2">
 agentic environment looks like and
 </span>
 <span data-rw-start="1540.24" data-rw-transcript-version="2">
 everything has to be rewritten.
 </span>
 <span data-rw-start="1541.36" data-rw-transcript-version="2">
 Everything is still fundamentally
 </span>
 <span data-rw-start="1542.48" data-rw-transcript-version="2">
 written for humans and has to be moved
 </span>
 <span data-rw-start="1544.559" data-rw-transcript-version="2">
 around. I still use most of the time
 </span>
 <span data-rw-start="1546.799" data-rw-transcript-version="2">
 when I use, uh, different frameworks or
 </span>
 <span data-rw-start="1548.32" data-rw-transcript-version="2">
 libraries or things like that, they
 </span>
 <span data-rw-start="1549.679" data-rw-transcript-version="2">
 still have docs that are fundamentally
 </span>
 <span data-rw-start="1551.36" data-rw-transcript-version="2">
 written for humans. This is my favorite
 </span>
 <span data-rw-start="1553.12" data-rw-transcript-version="2">
 pet peeve. Like, I don't, uh, why are
 </span>
 <span data-rw-start="1555.679" data-rw-transcript-version="2">
 people still telling me what to do?
 </span>
</p>
<p>
 <span data-rw-start="1557.039" data-rw-transcript-version="2">
 I don't want to do anything. What is the
 </span>
 <span data-rw-start="1558.4" data-rw-transcript-version="2">
 thing I should copy and paste to my agent?
 </span>
 <span data-rw-start="1560.227" data-rw-transcript-version="2">
 [laughter] Like, uh, so it's just, um, every
 </span>
 <span data-rw-start="1562.88" data-rw-transcript-version="2">
 time I'm told, you know, go to this URL
 </span>
 <span data-rw-start="1564.799" data-rw-transcript-version="2">
 or something like that, it's just like
 </span>
 <span data-rw-start="1566" data-rw-transcript-version="2">
 ah [laughter].
 </span>
 <span data-rw-start="1567.36" data-rw-transcript-version="2">
 You know. [snorts] So, um, everyone is, I
 </span>
 <span data-rw-start="1570.32" data-rw-transcript-version="2">
 think, excited about how do we decompose
 </span>
 <span data-rw-start="1572.24" data-rw-transcript-version="2">
 the workloads that need to happen into
 </span>
 <span data-rw-start="1574.08" data-rw-transcript-version="2">
 fundamentally sensors over the world,
 </span>
 <span data-rw-start="1576.159" data-rw-transcript-version="2">
 actuators over the world. How do we make
 </span>
 <span data-rw-start="1578.24" data-rw-transcript-version="2">
 it agent native? Uh, basically describe
 </span>
 <span data-rw-start="1580.08" data-rw-transcript-version="2">
 it to agents first, and then have a
 </span>
 <span data-rw-start="1583.36" data-rw-transcript-version="2">
 lot of automation around, um, you know, the
 </span>
 <span data-rw-start="1587.84" data-rw-transcript-version="2">
 um, yeah, around data structures that are
 </span>
 <span data-rw-start="1590.159" data-rw-transcript-version="2">
 very legible to the LLMs. Uh, so I think,
 </span>
 <span data-rw-start="1592.96" data-rw-transcript-version="2">
 um, yeah, I'm hoping that there's a lot of
 </span>
 <span data-rw-start="1594.4" data-rw-transcript-version="2">
 agent-first, um, infrastructure out there.
 </span>
</p>
<p>
 <span data-rw-start="1596.96" data-rw-transcript-version="2">
 And that, you know, for Menuguen, famously,
 </span>
 <span data-rw-start="1599.039" data-rw-transcript-version="2">
 when I wrote the, uh, not, I'm not sure how
 </span>
 <span data-rw-start="1600.96" data-rw-transcript-version="2">
 famous, but when I wrote the blog post
 </span>
 <span data-rw-start="1602.4" data-rw-transcript-version="2">
 about Menuguen [laughter],
 </span>
 <span data-rw-start="1604.159" data-rw-transcript-version="2">
 um, a lot of the work, a lot of the
 </span>
 <span data-rw-start="1606.24" data-rw-transcript-version="2">
 trouble was not even writing the code
 </span>
 <span data-rw-start="1607.44" data-rw-transcript-version="2">
 for Menugen. It was deploying it in
 </span>
 <span data-rw-start="1608.72" data-rw-transcript-version="2">
 Versell, because I had to work with all
 </span>
 <span data-rw-start="1610.24" data-rw-transcript-version="2">
 these different services, and I had to
 </span>
 <span data-rw-start="1611.44" data-rw-transcript-version="2">
 string them up, and I had to go to their
 </span>
 <span data-rw-start="1612.64" data-rw-transcript-version="2">
 settings and the menus, and you know,
 </span>
 <span data-rw-start="1614.96" data-rw-transcript-version="2">
 configure my DNS, and it was just so
 </span>
 <span data-rw-start="1616.72" data-rw-transcript-version="2">
 annoying. That's a good example of
 </span>
 <span data-rw-start="1619.76" data-rw-transcript-version="2">
 where I would hope that menu gen, that I could
 </span>
 <span data-rw-start="1621.76" data-rw-transcript-version="2">
 give a prompt to an LLM, build menu gen,
 </span>
 <span data-rw-start="1624.48" data-rw-transcript-version="2">
 and then I wouldn't have to touch anything,
 </span>
</p>
<p>
 <span data-rw-start="1625.84" data-rw-transcript-version="2">
 and it's deployed in that same way on
 </span>
 <span data-rw-start="1627.84" data-rw-transcript-version="2">
 the internet. Uh, I think that would be a
 </span>
 <span data-rw-start="1629.679" data-rw-transcript-version="2">
 good kind of test for whether or not
 </span>
 <span data-rw-start="1632.159" data-rw-transcript-version="2">
 our infrastructure is
 </span>
 <span data-rw-start="1633.36" data-rw-transcript-version="2">
 becoming more and more agent native. And
 </span>
 <span data-rw-start="1634.96" data-rw-transcript-version="2">
 then, ultimately, I would say, yeah, I think we’re going towards a world where
 </span>
 <span data-rw-start="1637.279" data-rw-transcript-version="2">
 there's agent representation for
 </span>
 <span data-rw-start="1639.36" data-rw-transcript-version="2">
 people and for organizations, and, um, you
 </span>
 <span data-rw-start="1641.279" data-rw-transcript-version="2">
 know, I’ll have my agent talk to your
 </span>
 <span data-rw-start="1646.96" data-rw-transcript-version="2">
 agent, uh, to figure out some of the
 </span>
 <span data-rw-start="1648.72" data-rw-transcript-version="2">
 details of our meetings or things
 </span>
 <span data-rw-start="1650.799" data-rw-transcript-version="2">
 like that. So, [laughter],
 </span>
 <span data-rw-start="1653.039" data-rw-transcript-version="2">
 um, I do think that that's, uh, roughly
 </span>
 <span data-rw-start="1654.799" data-rw-transcript-version="2">
 where things are going, but, um, yeah, I
 </span>
 <span data-rw-start="1656.72" data-rw-transcript-version="2">
 think everyone here is excited about.
 </span>
</p>
<p>
 <span data-rw-start="1657.84" data-rw-transcript-version="2">
 That.
 </span>
 <span data-rw-start="1658.24" data-rw-transcript-version="2">
 &gt;&gt; I really like the visual analogy of
 </span>
 <span data-rw-start="1660" data-rw-transcript-version="2">
 sensors and actuators. I actually hadn't
 </span>
 <span data-rw-start="1661.679" data-rw-transcript-version="2">
 thought of that. That's super
 </span>
 <span data-rw-start="1662.64" data-rw-transcript-version="2">
 interesting.
 </span>
 <span data-rw-start="1663.039" data-rw-transcript-version="2">
 &gt;&gt; Right?
 </span>
 <span data-rw-start="1663.44" data-rw-transcript-version="2">
 &gt;&gt; Um, okay, I think we have to end on a
 </span>
 <span data-rw-start="1665.36" data-rw-transcript-version="2">
 question about education. Um, because you
 </span>
 <span data-rw-start="1667.679" data-rw-transcript-version="2">
 are probably one of the very best in the
 </span>
 <span data-rw-start="1669.36" data-rw-transcript-version="2">
 world at making complex technical
 </span>
 <span data-rw-start="1671.2" data-rw-transcript-version="2">
 concepts simple and deeply thoughtful
 </span>
 <span data-rw-start="1673.52" data-rw-transcript-version="2">
 about how we design education around it.
 </span>
 <span data-rw-start="1676.32" data-rw-transcript-version="2">
 Um, what still remains worth learning
 </span>
 <span data-rw-start="1679.76" data-rw-transcript-version="2">
 deeply when intelligence gets cheap as
 </span>
 <span data-rw-start="1682.48" data-rw-transcript-version="2">
 we move into the next era of AI?
 </span>
</p>
<p>
 <span data-rw-start="1685.44" data-rw-transcript-version="2">
 &gt;&gt; Yeah. Uh, there was a tweet that blew my
 </span>
 <span data-rw-start="1687.76" data-rw-transcript-version="2">
 mind recently, and I keep thinking about
 </span>
 <span data-rw-start="1689.2" data-rw-transcript-version="2">
 it like every other day. It was
 </span>
 <span data-rw-start="1690.559" data-rw-transcript-version="2">
 something along the lines of, um, you can
 </span>
 <span data-rw-start="1692.64" data-rw-transcript-version="2">
 outsource your thinking, but you can't
 </span>
 <span data-rw-start="1694.24" data-rw-transcript-version="2">
 outsource your understanding.
 </span>
 <span data-rw-start="1696.64" data-rw-transcript-version="2">
 And, um,
 </span>
 <span data-rw-start="1697.679" data-rw-transcript-version="2">
 &gt;&gt; I think that's really nicely put. I so
 </span>
 <span data-rw-start="1701.279" data-rw-transcript-version="2">
 yeah, because I still, I’m still part of
 </span>
 <span data-rw-start="1703.52" data-rw-transcript-version="2">
 the system, and I still, I still have to
 </span>
 <span data-rw-start="1705.12" data-rw-transcript-version="2">
 Somehow information still has to make it into my brain,
 </span>
 <span data-rw-start="1706.72" data-rw-transcript-version="2">
 and I feel like I'm
 </span>
 <span data-rw-start="1707.919" data-rw-transcript-version="2">
 becoming a bottleneck of just even
 </span>
 <span data-rw-start="1709.279" data-rw-transcript-version="2">
 knowing what are we trying to build, why
 </span>
 <span data-rw-start="1710.799" data-rw-transcript-version="2">
 is it worth doing? Uh, how do I direct you?
 </span>
</p>
<p>
 <span data-rw-start="1712.88" data-rw-transcript-version="2">
 How do I direct my agents? And so,
 </span>
 <span data-rw-start="1714.64" data-rw-transcript-version="2">
 I do still think that ultimately
 </span>
 <span data-rw-start="1717.84" data-rw-transcript-version="2">
 something has to direct the thinking and
 </span>
 <span data-rw-start="1719.76" data-rw-transcript-version="2">
 the processing, and so on,
 </span>
 <span data-rw-start="1723.279" data-rw-transcript-version="2">
 and um, that's
 </span>
 <span data-rw-start="1724.72" data-rw-transcript-version="2">
 still kind of fundamentally constrained
 </span>
 <span data-rw-start="1726.24" data-rw-transcript-version="2">
 somehow by understanding.
 </span>
</p>
<p>
 <span data-rw-start="1727.679" data-rw-transcript-version="2">
 And this is one
 </span>
 <span data-rw-start="1729.6" data-rw-transcript-version="2">
 reason I also was very excited about all
 </span>
 <span data-rw-start="1731.36" data-rw-transcript-version="2">
 the LM knowledge bases,
 </span>
 <span data-rw-start="1733.2" data-rw-transcript-version="2">
 because I feel
 </span>
 <span data-rw-start="1734.96" data-rw-transcript-version="2">
 like that's a way for me to
 </span>
 <span data-rw-start="1736.799" data-rw-transcript-version="2">
 process information,
 </span>
 <span data-rw-start="1738.72" data-rw-transcript-version="2">
 and anytime I see a
 </span>
 <span data-rw-start="1740.32" data-rw-transcript-version="2">
 different projection onto information,
 </span>
 <span data-rw-start="1743.36" data-rw-transcript-version="2">
 I always feel like I gain insight.
 </span>
</p>
<p>
 <span data-rw-start="1745.039" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="1746.72" data-rw-transcript-version="2">
 it's really just a lot of prompts for me
 </span>
 <span data-rw-start="1747.76" data-rw-transcript-version="2">
 to do synthetic data generation,
 </span>
 <span data-rw-start="1749.52" data-rw-transcript-version="2">
 kind of over some fixed data.
 </span>
 <span data-rw-start="1751.36" data-rw-transcript-version="2">
 Uh, so, I really enjoy,
 </span>
 <span data-rw-start="1753.039" data-rw-transcript-version="2">
 uh, whenever I read an
 </span>
 <span data-rw-start="1754.72" data-rw-transcript-version="2">
 article, I have my, you know, my wiki
 </span>
 <span data-rw-start="1756.16" data-rw-transcript-version="2">
 that's being built up from these
 </span>
 <span data-rw-start="1757.76" data-rw-transcript-version="2">
 articles, and I love asking questions
 </span>
 <span data-rw-start="1759.52" data-rw-transcript-version="2">
 about things, or, um, and I think that
 </span>
 <span data-rw-start="1752.64" data-rw-transcript-version="2">
 Ultimately, these are tools to enhance
 </span>
 <span data-rw-start="1755.12" data-rw-transcript-version="2">
 understanding in a certain way, and this
 </span>
 <span data-rw-start="1757.279" data-rw-transcript-version="2">
 is still kind of like a bit of a
 </span>
 <span data-rw-start="1758.559" data-rw-transcript-version="2">
 bottleneck because then you can't direct
 </span>
 <span data-rw-start="1760.08" data-rw-transcript-version="2">
 the. You can't be a good director if you
 </span>
 <span data-rw-start="1762.88" data-rw-transcript-version="2">
 still, uh, because the LM certainly doesn't
 </span>
 <span data-rw-start="1765.36" data-rw-transcript-version="2">
 excel at understanding. You still are
 </span>
 <span data-rw-start="1766.96" data-rw-transcript-version="2">
 uniquely in charge of that. So, uh,
 </span>
 <span data-rw-start="1768.96" data-rw-transcript-version="2">
 yeah, I think, uh, tools to that effect,
 </span>
 <span data-rw-start="1771.039" data-rw-transcript-version="2">
 I think are incredibly interesting and
 </span>
 <span data-rw-start="1772.559" data-rw-transcript-version="2">
 exciting.
 </span>
</p>
<p>
 <span data-rw-start="1773.2" data-rw-transcript-version="2">
 &gt;&gt; I'm excited to be back here in a couple
 </span>
 <span data-rw-start="1774.559" data-rw-transcript-version="2">
 years and to see if we've been fully
 </span>
 <span data-rw-start="1776.159" data-rw-transcript-version="2">
 automated out of the loop, and they
 </span>
 <span data-rw-start="1778.48" data-rw-transcript-version="2">
 actually take care of understanding as
 </span>
 <span data-rw-start="1780" data-rw-transcript-version="2">
 well. Uh, thank you so much for joining
 </span>
 <span data-rw-start="1781.44" data-rw-transcript-version="2">
 us, Andre. We really appreciate it.
 </span>
 <span data-rw-start="1782.93" data-rw-transcript-version="2">
 [applause]
 </span>
</p>