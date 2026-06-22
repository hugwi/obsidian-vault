---
title: "Panel: Does AI lead us back to a beautiful document based waterfall approach"
source: "https://www.youtube.com/watch?v=iW-4faoku8A"
author: "Agile meets Architecture"
published: 2026-05-04
created: 2026-05-06
description: "The current approach to AI development is heavily based on writing lot's\"
tags:
  - to-process
  - llm-foundations
---

Welcome to the panel at the Azure meets architecture. Um we intentionally kept the focus of this conference to uh what this conference is about to agile to uh modern organization stuff to software architecture. But there's of course an elephant in the room and uh some talks uh did already address uh the elephant 

uh this time and um yeah that's what we are doing here on the panel. So we will be talking about this elephant and about the AI and how it's going to change our industry. Um if all the AI optimists will be right then probably the way we are doing uh or we are organizing software development and uh software architecture will change fundamentally somehow in the next time if they are right uh we might discuss about that so um that's why we do the 

panel that's why I invent invited the people usually I would say I invited a lot of experts in this field to talk about the field well honestly there is really no expert on this field uh and there's really no experts. So even if somebody claims on LinkedIn he's an expert in this field, he's just lying. Nobody knows about it really. Um uh but still I uh we have invited some very nice people that are very experienced in our industry uh to 

discuss this uh today and uh yeah maybe just introduce yourself and please quick we have a lot of topics. >> Yes. >> To cover. >> Oh yeah, it's on. Hi, I'm Bea. I'm a distinguished engineer at uh ThoughtWorks and I'm a domain expert in effective software delivery and I'm trying to figure out how to use AI in that domain. >> Hi, I'm Daniel Teror North. I've been kicking around the computing industry for about 35 years or something. Um I 

spent a lot of that writing what we would now call artisal software with my actual hands. Um, and I I'm the I think I'm the token grumpy person on the panel. I'm grumpy that this tiny tiny tiny niche of AI called LLMs has co-opted the term AI, which is a huge, rich, exciting, vibrant field. Uh, I'm grumpy that people think there's a trillion dollar industry to be 

had and they're convinced that we don't need junior developers. I'm grumpy about many things. I'm sure they'll come up. But yeah, so I've been around software and people and teams and organizations for a while. Um, and I'm I'm not sure why I'm on this panel. I know nothing about LLMs, but I'm prepared to have an opinion because I'm a middle-aged white guy. [laughter] Um, yeah. Hello. I'm Sasha. I'm working as principal engineer and architect currently at Interport. I have experience in retail and wholesale for 

about 10 years now mainly with a focus on web architecture and building software but also building organizations. So yes, AI is changing how we're working and I'm looking forward to the exchange. I'm Corey. I'm the grumpy old woman. >> [laughter] >> I am uh >> besides all the other things that I'm doing, I'm also teaching the teachers in computer science how to teach computer science to the computer science students 

which is becoming really interesting with AI. So I'm optimistic and extremely worried. Hi, I'm Emily Bich. I'm a technical coach. I'm an independent consultant and I I'm very interested in test-driven development. I've been teaching it these past like 25 years and it seems to have fundamentally shifted in just the past few months and it's turned into something else which is very exciting and very scary. 

>> Okay, great. So, um already quite some interesting topics that you teased on here. Uh I only have six questions but I already learned that I'm very optimistic that we will uh um discuss them all. Uh we'll start with the actually with the title of this panel which we chose uh few months ago uh because there was a trend and still there is a trend which is called specdriven development um which um to me sounds suspiciously like um yeah back to waterfall because 

if you specify all the things very well then uh the AI will do the rest uh after it. Um Biga, you wrote a pretty nice blog post and pretty popular blog post which is cited quite a lot uh uh about this topic. Um so are we going back to waterfall? What's your take on that? >> Yeah, it's interesting because that article gets shared a lot in a way like oh look I did it like that article describes but I actually have a lot of 

open and critical questions at the end of the article about this topic. Um but yeah, I think uh I I see kind of like both directions happening in some way. Like one is this like yeah more pull towards waterfall. I recently caught myself thinking about the V model and I was like oh my god what's happening? So kind of this yeah we're like uh I see Eric there Eric you wrote like I don't know a year ago about like are we just trying to do offshoring again right? If only we write the right specifications give it to something and then verify afterwards. 

So there's definitely this trend of like just writing again figuring out how do we just write better specifications which we've actually learned that we're not good at but you know so that's the the one pull but then on the other side I've recently also seen people discovering that when you want to create a lot of throughput you have to do all of these things like automation continuous delivery or I saw this thing about somebody saying oh the the SDLC which is actually like Simon was talking about it today is a very waterfall term 

right that has had resurgence with AI. And this person was writing about, oh, is the SDLC collapsing? Do we not need detailed requirements for the developers anymore because they can do them with AI now? And I was like, but you know, shouldn't a story always be a placeholder for a conversation? Shouldn't that have always been the case? So, there's some people actually discovering these things that I think are actually good ideas that you have to do to get good throughput and good feedback loops. So, there seem to be both of those things happening at the same time. maybe speedrun to rediscover 

good practices. I don't know. Hopefully, that's where it will keep going. >> But are there also reasons not to do it this way, >> not to do it with the >> the let's say spec in the beginning and then just Well, >> yeah, I think it's ultimately it's all about feedback loops, right? And I still I still think working in small batches is valid but because we have this increased level of automation now I was talking about this today as well right that people try to reduce the 

supervision by the human and then you have like much longer feedback loops right like an agent going away for 20 minutes 30 minutes and then you have like lots of stuff to verify lots of things that can go the wrong way in between so I think still think small batches in some way are still super valuable and for that you would still have to have small specifications in a way Right. So, >> so still agile. >> Yeah. Can I pick up on this with reference to test-driven development because this is that the the kind of premise of TDD is that you you learn 

during the development process and you use that uh to adjust what you build. So, spec driven development if you if you don't have that feedback during the the cycles then you you're you're missing out. But what I have observed now with with TDD practitioners, I mean I talked to about half a dozen technical coaches who I know and trust and know that they were doing TDD in the before times and they've all adopted agentic coding now. And they all told me we are 

not writing any code by hand anymore. And I'm like that is that is huge. You know what is even what even is TDD if you're not writing the code by hand? And some of them were doing a bit of refactoring. Some of them said I'd do some refactoring by hand, particularly preparatory refactoring, but not not the coding part because the agents are so good at that. But what what has remained so I've kind of questioned them, what does your process look like? And what has remained is the short cycles that are characteristic of TDD that you you slice the functionality 

and you build it a piece at a time and you adjust between slices. So the the kind of the typical cycle time in TDD would be less than 10 minutes. um probably a lot less than 10 minutes for a refactoring, but they're saying that yeah, with the angentic AI writing the code, my cycle time is the same or or even faster now, which is very different from traditional development, but it's still recognizably TDD, I think, even though they're not writing the code by hand. 

>> So, I I I just want to call out some kind of terminology. I think there's a straw man going on here. When we talk about spec driven, I mean TDD is entirely spec driven. The spec is executable. You start with the spec. You write it in Python or Java or whatever you're going to be using and then you or some genies or something generates produces some code that satisfies that spec and then you might if you like a tidy kitchen do some tidying up of that code while it still continues. So spec 

driven doesn't necessarily mean and I think and so I want to separate the idea of using a spec from this idea of oneshotting. So oneshotting is you write the whole spec and you say go on then genius go and do your magic and then you come back and you have a a product for the kids. um vodel from the 60s I believe or possibly 70s was this uh it was it was roughly a two-year cycle because you do a release every two years because you were like you know cutting 

edge and what you would do at the point when you were writing the specification you had your high level functional spec and at the at the same time sorry business requirements and at the same time you would write your high level um uh testing frame uh requirements uh testing plan and then as you got into more detailed functional design, so high level functional design, low level functional design, you would then have corresponding tests for those. And this V, it was sort of called a V model. So you'd you'd fill in the V, you'd meet at the middle, write the code, and then make sure it all worked. And the 

original scope for this was two years. Now, if you look at what you're doing with TDD, it's the same thing, but it's 20 minutes, right? So it's still the V model. the spiral model which was its contemporary by a guy called Barry Bone was the idea that you would design something you would then uh do your analysis you'd then come out with the the technical design the functional design you'd implement it and then you test it and it was like a little circle and his idea was that you had these concentric circles like a spiral where you'd start in the middle and you'd end 

up with the product and again each each go around the spiral would be 18 months and again if you say well actually BDD is that but it's 18 minutes [laughter] then we're still doing v modelel and spiral and it's but but just the the time scales have have massively condensed um so I guess in terms of like what are we doing with um with spectriven I think the idea of oneshotting for a prototype is brilliant right and it and it does it's uh Eric Mayer has this wonderful 

language he uses talks about democratizing so he likes to democratize programming democratize whatever and oneotting with with prompts democratize izes that prototyping activity for nontechnical people who've got a bit of an idea. But you absolutely do not want that for evolving code. So going into code that exists and make it do a new thing as well or make it do a thing differently. For that you need very different guard rails and we're right back to TDD again. >> Yeah. So I agree with everything being 

said and I think that it's definitely not going back to waterfall. It's if anything it's becoming much more agile and to follow up on all the things that has been said to me the code now is a bit like metal. Metal used to be hard to get by and difficult to work with. And when you made something in metal, it was made to last. You probably have something of metal from your grandparents. But the metal that we use right now, we just throw it away after we've used it once. If we 

look at the garbage cans, it's just throw away. Well, it's reuse of course because we're in Germany, but you know what I mean. And and I think code is becoming that. And I don't know whether that's good or bad. It could be a way of democratizing the code. It could be a way of spending a lot of energy for nothing. But it is interesting that the whole value of code and the whole blood, sweat and tears about code is changing. I think >> maybe just to like unless you I just 

wanted to with the spec driven just for the record I think there's no satisfactory definition of the term spectriven development right now. So I actually don't like talking about I try to figure out what it is that's why I wrote the blog post but I just had to like with like a lot of discussion convince my colleagues last week to not put this on the thoughtworks technology radar again because I kept saying there's no good definition for this. It's just like something people say and everybody means something else by spec. So, and that's also one of the challenges right now in the space because it's moving so fast that people come up with these terms and then 

immediately there's like a hundred different definitions of it. So, um yeah, I wish the term would just go away to be honest. Yeah. And for me it sounds a little bit like just we call it because we now call it spec we think about waterfall but if we would call it user story that someone takes understands then plans what to do and then implements it we are doing that for years and we call it agile but as soon as we don't call it any longer user story but spec we say it's waterfall so I'm like we just do the same as we did 

before in a different technological way but it's for me it's still the same a way but if I you believe writing a book of specs and user stories and then give it to a team and come back half a year later and for sure you will not get what you wanted. Right? So and this iterative cycles need to be still there. They are just getting faster hopefully. >> I just want to add as well um as someone who spent the first at least the first 20 years of his career writing code for money um and the la latter 15 or so uh 

talking to people about how they can write code for money. Um, I don't care about code. I care about what the code does. I care about the business capability I get from code. And if you can give me that business capability with less code, you win. If you can give me that capability with no code at all, you win at programming. Right? So I am absolutely fine with a an agent or a LLM or a human being throwing away code and rewriting 

chunks of it if that will get to the goal faster than trying to manipulate the code that's already there. The code is not an asset. The code is the liability. The business capability is the asset. So if I can get something that can tank through that code and make it be the thing I want it to be, I kind of don't care what what's doing that. That's a that's a good uh bridge, let's say, or segue or something to my next uh uh topic. I'm jumping a little bit here 

in my list, but uh I think that fits very well. So, it's uh about trust in code. Um the first thing you hear always when you when you discuss with somebody about uh AI generated code is uh can I trust it? Uh do I know whether that's the correct code or it's not the correct code? Do I review or do I need to review each line of code that I've written there? Actually, when thinking about it, I realized that um this is not a really new problem in our industry. I have 

discussed that uh many years ago uh regarding for instance open source libraries you're using uh which is also part of your system and where uh you need or where there was the discussion whether you need to read every line of code of your open source library that you are using. That said, those libraries were usually crowd tested. So many so you use them and hope that somebody else uh already found the bug that uh uh was risky. Um but still uh we 

have generated code and how do we create trust onto the code that uh a machine generates for us? How do we do that? Any ideas? >> Beer explain the concept of harnesses. This is this is just breakthrough idea that's appeared in like the last couple of weeks and I'm so excited about the idea of harnesses. >> Yeah, it's maybe not a breakthrough idea but like it's like now a name that is coming out for it. It's it's just like 

basically not just giving the um uh the agents like the feed forward of like here's like our coding conventions, here's how we want our code to be structured and all of that. But also the same as developers just giving the agent direct access to the feedback right to the static code analysis and all of that type of stuff. And I was just saying to Emily before that um I was for like a long time a bit always a bit dismissive of static code analysis because it was it's not the full guarantee that the code is actually good and all of that. 

But then like some years ago I had a uh junior developer on my team uh who like we paired with uh her a lot but then also we she was working by herself to like you know build up you know that you know as a junior you can code without like a senior next to you right and um she had access to like a sonar setup and it was actually super useful for her right and then I was like oh yeah right like I forgot this is actually this can actually catch a lot of things that you might be doing wrong and I was thinking about that now And um there's this like 

more and more chatter about building custom llinters and more making more use of structural tests like arcunit style and also the fact that these types of things we can also now custom build a lot easier. So we can build a lot more custom structural tests and stuff like that. So this would all be about like the internal code quality mostly, right? And I think maybe that might even make agents build better modular code bases than humans do. 

So it still doesn't solve the problem of a lot of other quality attributes or like just is the behavior there, but um there's definitely like a lot of like more traditional stuff that we can throw at the agents and make like a better feedback loop for them that will increase our trust. And then depending on the use case, we can decide if that harness that we have is actually good enough for the risk profile of the use case that we have or not. And so all of those things will determine how much confidence I have in the output. I just have something very short to say 

and that is that every time we need to transform something people want it to be perfect. So but can it solve this? Can it solve this? Will this be perfect? And what I normally say is that as long as we don't make it worse and I think the fact about trust we already as you said we already have that problem. So I don't think that we should expect it to be perfect because it can never be and it never was. 

Most of my job as a technical coach has been helping developers to write better quality code and and it's it's a very skilled activity particularly when you have a very old difficult code base to be able to raise the code quality. So it's so exciting to think that that now you can get these deterministic tools that can measure the code quality at least a minimum kind of make sure it doesn't make the worst mistakes and and it has a ratchet. it can access refactoring tools, proper refactoring tools. It's starting to to actually get 

a wide variety of refactoring tools. And this idea that actually the code quality can be improved without human skill with just uh static analysis tools and refactoring tools and and an agent in a loop. That that is that is amazing if that's actually going to work and I'm really hopeful that it will. >> I think the risk and this is going to keep happening, right? And I'm going to keep saying it and it's still going to keep happening. The risk is that we're anthropomorphizing a machine, right? 

Um, Claude doesn't give a crap. C-Pilot doesn't give a crap. Not because it doesn't like you, because it doesn't have the capability to give a crap. That's not there. CL Claude can't program. It doesn't know how to program. It knows how to produce things that look like code in response to things that look like questions. It has no domain 

awareness. When you're doing a financial billing system, right? It doesn't know the domain of finance, the domain of billing. It doesn't know any of that stuff. It just knows how to produce convincing looking output based on convincing looking input. And what we're doing is we're getting better at more convincing looking input which constrains and again the feedback loops mean we're more likely to get convincing looking output. I can't not mention Hanland's razor, right? Don't ascribe to malice what can be explained by incompetence. 

And the the key difference this LLM that is not a person and will never be a person is not a junior developer. Right? The LLM there's two things about the LLM. One, it doesn't care about your code. Two, it will not it doesn't want to learn. It has no valition. Right? a junior developer is really most of the ones I've worked with and hired and train and whatever is desperately eager to learn and grow and practice and do those things and they're going to mess up and they're going to mess up again and again and again but the you can 

think of them as like chaotic good they're finding their way but they have good intentions whereas an LLM is at best chaotic neutral right it will never care about your thing it can't be made to care about your thing. Um, so, so I think that's kind of where we're at. >> I I just wanted to I wasn't trying to say that the LLM was some kind of junior developer, just that it you can get this ratchet effect. >> Oh, yeah. No, sorry. 

Yeah. >> To raise code quality and that that I haven't really had before. Some deterministic way to raise code quality. It's interesting what what what I love and someone someone who I I would love to be able to site her because I can't remember who it was that said it recently that the if you take the ven diagram of things that improve developer experience and things that improve agent experience it's a circle and I just thought that was a wonderful observation is we're now investing in things like static analysis things like tooling things like whatever else documenting stuff writing down how we do things 

being explicit about our ways of working and our code style and our um for a machine in a way that we've never ever invested this much in the human beings around us and what does that tell us about us what um yeah what I'm missing a little bit here in the discussion is the uh one of aspect of trust is uh we were talking about how do we deal with the machine 

and so on and so on but trust is not the problem of the machine as you said trust is our problem So, how do we get to a situation where we say, "Okay, we can trust it." Or can we say, "Okay, we we don't trust the the stuff that's there." Um, >> well, I think Emily nailed it with with this this idea of ratchets. I think that is so critical is, you know, you've got this thing and the elephant in the room about the elephant in the room is that it has a chronic memory problem, right? It will forget things you've told it. It 

will forget very important detailed instructions you've given it while you're talking to it. It's called compaction. It's baked in. You can't not have this, right? And if you know what you're doing, you can decide when it's going to forget and when you're going to have to summarize everything it's ever heard. Or sometimes it will just do it. And there's that wonderful slashhartbreaking story of one a senior AI engineer like a director of engineering um who was using like a claudebot or whatever uh to um to to to manage her 

email. And she said, "Right, the one thing you must never ever do is delete email." And it went, "Okay." And then it deleted her entire email archive. [laughter] She I told you not to. Yeah. Oh, did you? Oh, there's a thing. And she said she was basically she ended up doing this kind of walking on eggshell things with the one machine she still had that had her email on it to try to get it back. And like, you know, this isn't again this isn't malice. This is pathological incompetence. How? And so so given that that is 

literally baked in, we can't that's part of the design. Hallucinating is part of the design. Compaction is part of the design. We have to build these checks and balances and harnesses to manage if that's the tool we're going to use. But it's again about risk assessment and the use case, right? Like in this case, of course, I would not give an agent access to my email, [laughter] right? like especially not write access or delete access or any of those things, right? 

>> Yeah. So, and uh so and in the case of like coding like um like I agree with everything you said like it doesn't care about the code and all of that but if it does the thing that I need do I care that it cares and that it's a machine and not you know like I also don't think we should anthropomorphize it and it's like easily happening because the large language models are trained on our language. So that's why it's also like all the things that are good for us in the code are good for the model because it's trained on how we've been writing code, right? Um 

but yeah, I mean does it matter why that is the case if it gives me something useful, right? And the risk assessment part that's the like what's the use case like how much footprint do I give it like impact what it what it can access and stuff like that and that's kind of like then how you wield the tool, right? Okay. Well, um talking about learning and skills and so on. Uh coming to one of the questions that always comes up uh again after reviewing uh the code is the 

Yeah. And and Kevin talked about it uh today too. Um are we going to get more stupid because uh we are using those AI engines? is is like uh GPS um that uh lets me not being able to navigate uh a city without uh looking at a machine. Um and uh yeah of course also connected to the question what do we do with the new 

developers that might take the easy way and uh just um I mean then you just said you had um developers that are always eager to learn but what if they are not eager to learn what if they are just using it so you >> yeah I think I recently had an experience with one of our students and he tried out some new technology and it looked good it was working and at one point it stopped working and I asked him 

okay what did you do I I wasn't I didn't know anything about it as well but I realized he didn't even had a clue how to start debugging this thing he doesn't know anything about it even on something like system outprint line right so the very most basic thing that I would expect works in every technology some he was just like I tried again and again and maybe he would ask again and again um his chat pot but nothing happened and I'm thinking this is something 

maybe we need to find a way to teach people that explicitly again but they will not learn it by themselves like we were like with compiler errors we started and we were like okay how where how can I start and go forward and they don't have the problem now because they just ask so how can I fix this compile error and they copy paste and I think it it was a similar story when stick overflow comes into the play right so you could start copying from St overflow but you still realize that it's not working forever. So there is something 

changing for them and but I think they will need to learn how to debug and how to analyze a problem when the machine cannot help any longer. >> The short answer is yes.  I forgot my question. >> Okay. So your question was will people still develop these skills or will they forget them? And the short answer is they will forget them. And I I hope not. But as I said being a teacher for teachers in computer science and also 

talking to other people who are teachers not just at the university but at different kind of uh there's a at least in Denmark there's different ways of being educated in it and there are some schools where you are learning how to program based on a specification and there are some schools where you learn to create the specification and things like that and we're really talking about I don't know how to translate this to English but uh in Danish we say fo and that means content sorrow or 

something like that that some of us are really really sad that some of our skills that we've worked with for so many years might be forgotten and if we think back to other things that have been taken over by machines if we call this a machine that they have been very sad and at the university that I am at we are working in two different directions at the same time and I don't know where we'll go. One direction is we will make sure that when they hand in 

something they have to hand it in orally so they have to explain what they've done and when they go to the exam they do it with paper and pencil and they cannot use the computer. So that's one direction but we have another direction which is debating do we even need to teach them these skills and if we don't then the whole education is going to change tremendously and what we're going to teach them is something different than what our wonderful professors have been talking about for 

30 years on stage and that's really scary and I don't know what the answer is but it's like two out of three of my children are either computer scientists or becoming that. So, it's a very personal question >> right there. [laughter] >> Yeah. >> Bad parenting. We're both computer scientists. Yeah. Sorry. >> I I want to speak directly to the question. Uh are we going to get more stupid? I think it only matters losing a 

skill if it's a skill you're ever going to need again. Right. And if we are, and I think we are exactly to your point, we are at risk already of losing skills we are still going to need. That's a problem. That's a material problem. Uh I've been in software for 35 years. I suspect as long or more longer than a lot of people in this room, but I'm still pretty, you know, I'm still pretty new. It's a quite an old field now. Um so who here is any good at punching uh 

cards? Who has a card hole punch? Right, there's a skill and it used to be an important skill. How fast you could punch holes in a card was how fast you could literally how fast you could program, right? Uh what about changing a paper in a teletype? No. You know the TTY, the letters TTY when you have a TTY that's a thing that's a physical mechanical thing. Uh who can program in machine code? No, not assembler machine code. 

Ah, gotcha. Right. So again, some of you will know assembler and some of you need to know assembler. Most of us don't. Practically no one will know how to program in machine code. So there are skills where as the technology has improved and again um Tiono founder one of the founder of the Toyota production system he has this wonderful term he calls it autonom with a human element right and for me any technology advance the the ones that 

wins are the ones that allow humans to do stuff better to make it easier for them to do things not to replace them. And if you look at the most successful technologies in history, they allow us to do stuff, whatever that stuff is, medicine, you know, research, science, climate, whatever it is, right? Better um sometimes not entirely better, right? But by and large, they they augment humans. Yeah. So if we're losing skills where we still where we're likely to still need them 

and you know, we we are in a world of cobalt, right? Cobalt is still one of the most prevalent languages. whatever code is out there has an enormously long tail ahead of it. And so the ability to go in, manipulate code with your hands, that's not going away in my lifetime, probably in the lifetime of anyone in this room. And if we allow those skills to atrophy, right, we're in trouble. One other thing, and then I'm going to shut up. One other thing I think is really key and I'm really excited about this and I'm looking to know particularly and 

Emily who are the people in the world who are bringing up the people in the world is the word native. So my I've got a three-year-old son. He is mobile native. He's never lived in a world without mobile technology. He got disappointed when he was two that he couldn't do that on the TV screen and it would do stuff right. He because it's just like his a little screen, but it just doesn't doesn't work. Yeah. We're all old, right? All of us are old. You know, I'm really old, but like all of us 

are old. Yeah. Um the kids coming through now will never have been in a world that didn't have AI. They will be AI native. They will be Gen AI native. They will think about problems differently than I can. I can probably learn to do it, but I'll keep falling back on my old artist and programming habits. Yeah. And that's exciting, right? So, let's bring those junior engineers. Let's give them the space to learn this new world and make sure they can still drive with a stick shift. 

>> I disagree on two points. >> Nice. >> I'll make it short. One is I don't think there'll be a long tale of the programs that we do right now. It's so easy to go into a really old program and find the smallest thing. So, the truck number is dead as a concept as well. I don't think the code will get old, but that's just I mean what do I know about the future? And the other thing is if we look at the young people who are mobile native, they're still falling into a lot of the traps that are because of the mobile. 

They're still falling into the sexual predators. They're still falling into um losing their parents' money. So, so yes, they can use it, but not in a safe way. So, that's what I wanted to say. >> Yeah. Yeah, I think one of the tricky things is like when we draw like history from computer science and then the the assembler comparison and all all of that, right? Is that we've always gone like up in the abstraction level but like real abstraction in the sense of that we've had deterministic tools that 

add the technical details and translate from the new abstraction level to the next abstraction level. Right? But this is not the same thing like the natural language thing because we don't have like a compiler compiler that translates to the level down. Like I always say it's kind of like moving to the side because we can use LLMs on all of the abstraction levels. Like I recently talked to Uva Fredson about this and he said like yeah it's not a closed abstraction. It's not closed. So we cannot forget like what's under underneath. And that goes to what you were saying like we'll still have to to 

a certain extent actually edit or understand the existing code but we don't have as much practice anymore for like what's potentially going wrong right like so how do you build up the the mental model the in in your head the shortcuts like to understand everything. I uh read this um article a few years ago on like uh what do what what programmers need to learn about learning um and there was a thing there about how you learn those shortcuts those abstract concepts and maybe yeah I know not he 

maybe knows about this better than me by actually going detail abstraction detail abstraction right you write the syntax of a for loop and then you do that a few times and then you start understanding the concept of a for loop and you have a shortcut in your head but then how do you learn those like highle abstract things if like everything's still running on code but we're not. Yeah. So I don't know it's not an answer to the question what we do but and um maybe my last point um there's like um arguably I 

would say like clawed code itself right now is a really good example of a piece of software that is being built entirely by people using agents and not typing code anymore and it's a piece of software that has maybe had one incident over the past year that was quickly resolved and it works really really well right like from what I understand I think like the people on the cloud code team are all really really experienced developers and I think that is currently uh covering up some of the you know what the situation will be like in maybe five 

to 10 years right the teams that are really successful with this at the moment um are like really experienced and have all of these mental models in their head and I also wonder and there's a lot of technical descriptions when you prompt right it's not just the functional stuff there's a lot of technical stuff so yeah I really wonder about what that will be like in a few Can I come in on this a little about so how you >> engineering skills? I'm convinced that we still need engineering skills even when we're using an AI to write all the 

code. And the the reliable way that I know to teach people engineering skills is having them build stuff and toy projects. and and I'm looking at my my daughter, she's like 17, 18, and she's building things with Arduinos and and wires and 3D printing stuff and she's learning engineering skills by doing it. And I think that those skills are transferable to the AI age, but I think that the way we know to teach those is 

is not using the AI. So that's the the the the interesting part to me is that I think students benefit a great deal from not using the AI in in to learn engineering, but at some point they need to learn the AI specific skills. Um and I'm not sure we really know what those are yet. >> Well, oh maybe you do. >> Maybe let me uh mix some opinion with a question about that. Sorry, I know >> just talk over 

>> um but because uh for that point isn't I mean I think curiosity is always uh the key to learn new things and uh trying to wanting to understand something. So the opposite of what you Sylvia described uh of uh well I got a solution but I don't know how it works but however it works that's just the opposite thing there and my experience very very personally is that if you use the LLM stuff to really 

dig deep into what is it actually what I'm seeing here please explain that to me more and more and more like you would maybe look into whatever um diction dictionary or something to understand the word Then you can even learn more uh if if you go this way. Sorry, was that something you want? >> Yeah. Yeah. So that yes, the the LLM can help you to understand a topic and and help you to research it and and that's 

that's useful. You need to understanding and knowledge, but a lot of engineering is practical. It's it's doing it and it's filling around with wires and why does this break and how do I debug that and you know and that practical it comes from experience not from talking to an LLM. >> Okay, >> just very short. >> I got the microphone. [laughter] So um again in the university in in teaching we um if we if we're 

looking at the motivation for students to learn I think we're a bit biased up here and maybe down here as well that we are learning because we're curious we want to improve our skills but about 60% of the students are there as a means to an end >> and that's a that's a very different motivation and it creates a very different um way of working with it and the way that I try to explain it to my students is the difference between just in case and just in time learning. So what we try to do at the university is just in case learning just in case you 

need to understand the compiler you need to learn this just in case you need to understand this type system. But what AI can give you is the just in time learning. So just in time to hand in that assignment you can learn that. But if you look at that like the deep neuro science ways of learning that's not real learning. But let's not go into that here. I just want to reinforce something that that Emily said. Um, so there's a model that's been kicking around that sort of education circles for decades 

called var visual auditory reading and kinesthetic. And the idea is that there's different modes of learning. And some people are visual learners and they like pictures and some people are auditory learners. They want to hear stories. Some people like to read and do self-paced stuff. And then some people kinesesthetic, they like to interact with this thing. And it's a very appealing model and it has some very bogus research around it. And it turns out it's complete nonsense, right? That absolutely falls apart as soon as you start to touch the edges because it turns out that everybody everybody is a kinesthetic learner, right? You're a 

kinesthetic learner from birth. The way you learn anything is by interacting with it, by playing with it. Exactly to your point, building with it. And if I ask an LLM for the answer, I'll get the answer. But no learning took place. And even if I ask an LLM to teach me, still no learning takes place, right? Not until you are interacting with the thing, making the mistakes because learning is about making mistakes and understanding why that thing was a mistake. Getting that experience, putting in those hours and then going, "Oh, right. Okay, this thing makes sense now." The the write the for loop, 

understand a for loop, write another for loop in a different language, understand, oh right, now I get iteration. This is making sense. And without actually getting your hands in there doing stuff, no learning is happening. I mean, one of my hopes is that that will be the thing that will be happening that we have that the the next generation will learn through the pain of making mistakes the same way that we did and then they will be forced to like understand certain things and hopefully 

that period of time will be as short as possible. [laughter] But yeah, you know, there will be like I did I made mistakes. I once during an internship deleted the whole production database because there was only production. >> Put your hands up if you ever deleted [laughter] It was the user It was the user database as well. Yeah. But um this was yeah a long time ago. They they they shouldn't have let an intern you know mess around in the PHP my admin. [laughter] 

Anyway, I learned from that. Right. >> Okay. Learning uh is one of the human aspects. Another one is uh how do we actually work and how would uh teams uh maybe change or not change. I don't know that's uh another discussion that I hear quite a lot. I think Yung Abalo talked about that last year in the keynote here. He said well we will probably be moving to other team sizes uh which might become smaller. Uh there's also 

another aspect um that I actually hear a lot when I talk to people that work in an environment or or try to use with uh uh to use those agents which is they don't actually pair program anymore. Uh they mostly sit alone and uh try to work with their agents somehow. So what are your thoughts about how will work life and teamwork actually change if it comes like it comes maybe 

everything will be back to uh to normal in a year but uh it doesn't really look like that so what do you think how teamwork will change how team sizes will change >> all the things I'm thinking about that are disagreeing being with each other. >> Okay. So what are some of them? >> Okay. So one is I so one part of me thinks the teams will definitely get 

smaller because we can use some agent as a team member and we can use those to learn. I can see that also coming back to the teaching that the students can use to learn in the same way as peer programming and peer reviews would would be good. On the other hand, I'm I'm thinking that it might be easier to to cope with the big cognitive load of a big team if you have the help of uh an artificial intelligence in some way. So those two things are disagreeing with each other. I'm also thinking that it's a shame that people will start using 

well an AI instead of pair programming with another human being. But on the other hand, I know a lot of people are suffering in the pair programming style and they might actually benefit from just sitting with the computer. So I'm completely torn about this. I've got a lot of other things going on in my brain, but I'll leave it with that. I I can talk about I I don't think we've we've solved this. I mean, the the experience of of working in an ensemble. 

I do a lot of working in an ensemble as as a technical coach and it's such a good forum for for sharing knowledge and communicating about code and teaching and there's so many benefits to it. But my experience of sticking an AI into that forum as an agentic AI is that it it somehow collapses if you're not careful. It just collapses the whole conversation and it all turns into us staring at text scrolling past on the agentic AI and suddenly we're not 

communicating, we're not learning and this AI has turned into this the most horrible pair ensemble member ever who just takes over. Um, and I I don't have any really good solutions for this yet, but it the trend at the moment is very much towards me and my AI or my fleet of agents and and suddenly we've lost all this collaborative programming and we've got to get it back. I mean >> I mean that's >> I had yesterday evening an interesting 

discussion and one said if I'm programming with other people in an ensemble mop whatever you call it he said it's even better than AI because the people are foreseeing which problems will come up and they already solving the problems this is what AI can currently maybe currently not foresee what will be the next challenges coming up because they all know where it will going. So this is something I think really interesting. But on the other hand, he said, "But when I'm alone, then 

it's better to have someone next to me." So if sometimes there is no ensemble available for whatever reason, I'm I'm working later than the others, whatever. So I think you are having more flexibility maybe now. You you have a pair if you want or you need one. Um but yeah, on the other side, I'm thinking yes, you can have smaller teams, but your PO is also speeding up. So he's producing more user stories and so maybe you still need the same size amount of developers. On the other hand, you can 

maybe easily start something new with two developers already which you have never done in the past because two were too small but now you can start something. So I think there are opportunities to have different team sizes but still you will have the team sizes you had before maybe as well. So maybe there's not this one single answer. I mean there's these different scenarios that we can play through right will teams get smaller and then potentially the ind individual cognitive load will 

go up or will we give existing team sizes more topics to work on and then the whole team's cognitive load will potentially go up or will there be something about teams and systems being able to collaborate with each other easier or something like that. I think in part it will depend on this like kind of like break neck speed and throughput that people are trying to do right now to like if that will collapse at some point or if we will figure out some way to do it sustainably and if that even makes sense right like all of this like 

throughput do we even want that what is the goldilocks speed and throughput that actually makes sense to create value and to not burn people out and to so I think it will depend a lot on on that and I mean there's also organ organizational things, right? Like you can't make a team so small that you can't be on call anymore and stuff like that, right? So that also plays into it. So similar to I know I also keep going back and forth. There's so many pros and cons to different scenarios or like yeah it's um 

there's also of course everybody thinking now every developer just does all the different jobs and everybody can do anything, right? Everybody can do design and the product owner can code and um yeah it definitely I think it would be good if more people would experiment more with this. I think a lot of people are very careful about it right now, but there's not a lot of data yet. I think >> so. I I when when someone asks me something like this, I go back to first 

principles. The question I ask myself is, so we're talking about how team sizes are going to change, the question I ask myself is why are they the size they are now, right? Because they weren't always that and there isn't I mean I know there's some religion around, you know, seven plus or minus two nonsense. Um but the point is you know if I go back in history even for relatively recently you'd have the DBAs over here the systems folks over here the uh functional people over here the UI people over here in completely different teams maybe organizations 

either in silos or whatever and and they weren't there because we thought that was the right thing to do and now we think it's a different thing to do. A lot of it is because of tooling and because of language change and because of just the environment we're in. Suddenly things where we would have had to taken something and split it into pieces and farm those pieces out and then bring them back together in the end which is how we used to do software becomes tractable for me to say hey Bagita can you add this field to this report and she has the skills to make 

the UI change make the functional change make the calculation change make the database change and and make sure all the glue in the middle is working and and write tests for it and be confident that it's changed right so that's now a thing that a that a human being can do or a pair human beings in a small team. And so I don't necessarily think we're going to get smaller teams or bigger teams or anything like that. I think the nature of work is going to change. So why why do we have user stories, right? Why do we have why do we work in small chunks? Uh risk, it comes back to risk and blast 

radius and how much stuff we can hold in our heads. By the way, complete sidebar, we're doing cognitive load all wrong, right? Everything you think you know about cognitive load is completely wrong. Um ask me later. I get really cross about this, but not now. We only have eight minutes and 30 seconds left to change the world. Um, so I I suspect what's going to happen is we're going to be more ambitious in the size of a unit of work because we can 

be, right? We can say I want to make this significant. I want to implement this entire feature because I can with my little team and some superpowered robots in a way that would have taken weeks or months or would have need to be split up into much finer slices before. Your elephant carpacio becomes more like an elephant pasta, right? You can you can just take take bigger chunks of it. Sorry vegetarians and anyone who likes elephants. Um there's I did want to mention though domain driven design is a real passion 

of mine and the kind of the core the core idea in domain driven design is the goal of what we do as people in organizations doing stuff is to understand what the stuff is and to figure out ways to meet that need and by modeling the domain and particular isn't like a perfect model for any domain. It's like what's the model for the domain for to solve this problem. By modeling the domain, the software is kind of a side effect of that. And this 

comes back to learning again, right? So the more we learn about the domain, the more we can articulate the about the domain, the more we can build little software constructs that that are our projection of what we understand about the domain, the more problems we can solve in that domain. And you know the the so so the point is the learning. And if the way in which we're engaging with work isn't doing the learning, isn't doing the knowledge crunching, then we're not going to be able to solve those problems. 

Wow. [laughter] I'm I'm thinking about uh whether I asked the last question or not because I'm not sure we moved in the right direction, but I still do it. uh we were talking about teams, we were talking about team sizes and communication with other um uh teams and so on and and our agents. And one thing that comes to my mind when I talk about that is uh a topic that we always 

mentioned at this conference, Conway's law. Will we I mean I I I think com law still will still hold up because we will still have some kind of communication uh and this will still shape the structure of our architecture and so on but will uh maybe we need to look differently on Conway's law in the future because we 

have [snorts] if I enter or however you say that in English uh uh the agents Will will it change? What do you think about Conway's law in the future? >> I I want to slightly derail this to go back to something I know touched on earlier and I think is okay absolutely vital to this conversation. Conway's law is already happening. Conway's law for those who don't know Melvin Conway 1967 he said he wrote a wonderful paper and he said but he what he'd observed is 

that the architecture of systems in large organizations tend to model the communication structure in those organizations. So it's nothing to do with or or structure it's to do with how people communicate. And for me, the glaring illustration of Conway's law is that the information in an LLM is a projection of the communication of the types of people and organizations that built those LLMs, which takes us right back to bias, takes 

us right back to toxic. There's, you know, there are live court cases right now where I think it was Google Gemini. I'll probably get sued for this. One of the big LLMs uh told somebody to kill himself and gave him ways to kill himself. It said, "Well, you should probably end it, right?" This wasn't even a he was already thinking that and it gave him it. It made the suggestion, right? And this is baked into the stuff we've got. And and I's point when I was talking about kids being like cloud 

native or whatever, I'm talking about the folks designing systems having always had that. It's like being water native and saying, "What do you mean you have a well?" I just turn on the tap. That's what I mean. Obviously the things you build with that. Yes, we need online safety, right? We don't need the online safety act. That is massively misund mis misplaced in the UK, but anyone who's from the UK and just going why are you doing this? It's very very easy for politicians to get derailed totally by by this stuff. But we have, you know, apart from all the ethics of should we 

be running these things in, you know, energy hungry water trouncing whatever places. So apart from the ethics of even running them, the stuff that's in those models, the content of those models is entirely Conway's law and it is hiding in plain sight and it is terrifying. >> Very good point. I like that. Anybody else got any thoughts about that? >> And maybe a software related example of that is that they uh they all assume 

pull requests because all their training data is full of the concept of pull requests. That is a communication pattern that we have, right? So >> they also assume that all code is just like the code you find on GitHub, which is really heartbreaking. >> Yeah. Um open source maintainers do have a problem. We we discussed that um yeah on that. How do we deal with all these AI 

slop then in the future that uh all the uh pull requests that are generated and um overwhelm the people that try to maintain the systems? Well, I mean the famous example is curl stopped giving bug bounties because they got too many slop furious security pull requests whatever things. So, so yeah, I don't think we there's a lot of these things problems that the AI being so cheap now to 

generate code to generate pull requests. Um, and the the there's a bunch of problems being caused by that and I don't think I have the answers I'm afraid. So, uh, but yeah, it's it's clear that we're moving into it's creating as many problems as it's solving probably. So I'm I'm running around facilitating retrospectives for a lot of different IT companies around the world online and not and one of the things that we're really discussing right now is how do we use AI within our team 

and for those teams who are not already discussing it I'm I'm trying to encourage them to discuss how are we using AI in our team trying it out as you said bikita try it out everybody and and talk about your experience experiences, talk to each other, talk about how you use it, how you want to use it. Because the things that I see right now is it's really bad in a team if some people in the team is using it in one way and other people are expecting them to use it in a different way. That's the worst. So, continue to 

communicate and try it out, I think, is what I would say in general. >> Yeah. and and that kind of um architect I spoke to recently was like monitoring who was using the AI the most and it was the most junior developers were using it the most and that was kind of worrying. It's like um yeah and and there needs to be some consistency in in how development teams agree to use these tools because otherwise they're going to be uh delivering slop to one another and it's going to cause a lot of kind of the 

same kind of tension that the Carl project is getting now. You know, I I'm not reviewing this. That's a 40,000line pull request. Go away. Yeah, >> it comes to my mind something you mentioned some weeks ago but like is is the value they are creating worth the money we are spending right because right now it's cheap to create all these pull requests but how long will they be as cheap as they are and like I think 

maybe currently it's nice just to try out everything and just do all of that but the question is how long are we still spending time to do things And the question is if the money answers at one point maybe the question and we don't produce just anything because we can but because it will be too expensive at one point it's at least a tiny hope at one point but it will become too expensive. >> I don't have an answer to the question. I have a a really what I thought was an 

insightful reframing of it. Um which is Mitch Hashimoto. He's he he wrote all of the Hashi well he started all the Hashi core stuff so terraform vault console all these amazing bits of software and recently he's been writing a terminal emulator called Ghosty and I use it and it's brilliant and he his observation he said particularly in the PR world of open source is that we've had to move from a um a default accept model to a 

default deny model. Mhm. >> So you know the default is someone submits a PR they do it with good intent you know positive intent and there's almost like there's a proof of work element to it right they had to do some work to write the to create to make the change pull the pull request fill it in so you can generally assume good intent right or well disguised malice yeah but it's a human being in there doing stuff when it's all AI generated 

um then you have to assume the default has to be denied until someone can until a a PR contributor can prove its uh worth if you like and he's got a he's started a new open source project called Vouch and Vouch is effectively a web of trust for open-source projects to then vouch for contributors and you can either vouch for someone who's a committer a contributor or you can uh accept someone else's vouch list so I go 

to Emily's project and she's got a really good voucher list of loads of contributors and I subscribe to that list. So where so so his his counter is to start creating a web of trust where we assume default deny and then unless you're vouched for and I I don't know if that's the model it's a model I suspect there's going to be an awful lot more hard thinking in that space. >> Thank you. One more shot. Yeah. >> Yeah. And it's a little bit Yeah. I 

don't know if heartbreaking or something. I mean, these models and the coding capabilities only exist because so many people spend so much of their free time over years like contributing to this foundation that we have, right? And something like this vouch might actually make it more exclusionary and harder for people to get into this to contribute and all of that because you have to like get into this network and you have to like somebody has to vouch for you at some point, right? And so in a way it's like also yeah heartbreaking in a way [laughter] 

but >> yeah I don't know sorry that >> yeah those have to be the last I'm just trying to find last words and I'm now getting from default deny mode to heartbreaking [laughter] which is really really low to get uh to this maybe I should have stopped when I said something about uh yeah try the things and and learn uh the stuff and experiment uh with everything because we it it will change and we all need to learn how it will work. I'm trying to 

stick with that now. >> There's lots of exciting stuff as well like that's lot >> lots of people rediscover their excitement in some stuff. So [laughter] >> thank you very much for that. Okay, thanks a lot. Uh I think that was I hopefully also for everybody here a very interesting discussion with some food for thought and uh now enjoy u some more drinks. Thank you. >> [applause] 

<p>
 <span data-rw-start="7.04" data-rw-transcript-version="2">
 Welcome to the panel at the Azure meets
 </span>
 <span data-rw-start="9.599" data-rw-transcript-version="2">
 architecture.
 </span>
 <span data-rw-start="11.36" data-rw-transcript-version="2">
 Um, we intentionally kept the focus of
 </span>
 <span data-rw-start="14.639" data-rw-transcript-version="2">
 this conference on, uh, what this
 </span>
 <span data-rw-start="16.72" data-rw-transcript-version="2">
 conference is about—agile, modern organization stuff, and software
 </span>
 <span data-rw-start="23.039" data-rw-transcript-version="2">
 architecture. But there's, of course, an
 </span>
 <span data-rw-start="25.279" data-rw-transcript-version="2">
 elephant in the room, and, uh, some talks
 </span>
 <span data-rw-start="28.32" data-rw-transcript-version="2">
 uh, already addressed, uh, the elephant
 </span>
 <span data-rw-start="31.599" data-rw-transcript-version="2">
 uh, this time. And, um, yeah, that's what we
 </span>
 <span data-rw-start="34.88" data-rw-transcript-version="2">
 are doing here on the panel. So, we will
 </span>
 <span data-rw-start="36.88" data-rw-transcript-version="2">
 be talking about this elephant and about
 </span>
 <span data-rw-start="39.04" data-rw-transcript-version="2">
 the AI and how it's going to change our
 </span>
 <span data-rw-start="41.68" data-rw-transcript-version="2">
 industry.
 </span>
</p>
<p>
 <span data-rw-start="43.2" data-rw-transcript-version="2">
 Um, if all the AI optimists will be right,
 </span>
 <span data-rw-start="46.719" data-rw-transcript-version="2">
 then probably the way we are doing, uh, or
 </span>
 <span data-rw-start="49.36" data-rw-transcript-version="2">
 we are organizing software development
 </span>
 <span data-rw-start="51.44" data-rw-transcript-version="2">
 and, uh, software architecture, will change
 </span>
 <span data-rw-start="53.68" data-rw-transcript-version="2">
 fundamentally, somehow, in the next time.
 </span>
 <span data-rw-start="56" data-rw-transcript-version="2">
 If they are right, uh, we might discuss
 </span>
 <span data-rw-start="58.48" data-rw-transcript-version="2">
 that, so, um, that's why we do the
 </span>
 <span data-rw-start="61.199" data-rw-transcript-version="2">
 panel. That's why I, I invited the
 </span>
 <span data-rw-start="63.44" data-rw-transcript-version="2">
 people. Usually, I would say, I invited a
 </span>
 <span data-rw-start="66.4" data-rw-transcript-version="2">
 lot of experts in this field to talk
 </span>
 <span data-rw-start="68.159" data-rw-transcript-version="2">
 about the field. Well, honestly, there is
 </span>
 <span data-rw-start="70.159" data-rw-transcript-version="2">
 Really, no expert on this field,
 </span>
 <span data-rw-start="73.439" data-rw-transcript-version="2">
 uh, and there are really no experts. So,
 </span>
 <span data-rw-start="75.52" data-rw-transcript-version="2">
 even if somebody claims on LinkedIn he's
 </span>
 <span data-rw-start="77.6" data-rw-transcript-version="2">
 an expert in this field, he's just
 </span>
 <span data-rw-start="79.119" data-rw-transcript-version="2">
 lying. Nobody knows about it, really. Um,
 </span>
 <span data-rw-start="83.2" data-rw-transcript-version="2">
 uh, but still, I, uh, we have invited some
 </span>
 <span data-rw-start="85.759" data-rw-transcript-version="2">
 very nice people that are very
 </span>
 <span data-rw-start="87.92" data-rw-transcript-version="2">
 experienced in our industry, uh, to
 </span>
 <span data-rw-start="90.32" data-rw-transcript-version="2">
 discuss this, uh, today, and, uh, yeah, maybe
 </span>
 <span data-rw-start="93.84" data-rw-transcript-version="2">
 just introduce yourself, and please, quick,
 </span>
 <span data-rw-start="95.92" data-rw-transcript-version="2">
 we have a lot of topics.
 </span>
</p>
<p>
 <span data-rw-start="97.439" data-rw-transcript-version="2">
 &gt;&gt; Yes.
 </span>
 <span data-rw-start="97.759" data-rw-transcript-version="2">
 &gt;&gt; To cover.
 </span>
 <span data-rw-start="98.24" data-rw-transcript-version="2">
 &gt;&gt; Oh yeah, it's on. Hi, I'm Bea. I'm a
 </span>
 <span data-rw-start="100.799" data-rw-transcript-version="2">
 distinguished engineer at, uh,
 </span>
 <span data-rw-start="102.479" data-rw-transcript-version="2">
 ThoughtWorks, and I'm a domain expert
 </span>
 <span data-rw-start="106.32" data-rw-transcript-version="2">
 in effective software delivery, and I'm
 </span>
 <span data-rw-start="109.2" data-rw-transcript-version="2">
 trying to figure out how to use AI in
 </span>
 <span data-rw-start="110.96" data-rw-transcript-version="2">
 that domain.
 </span>
 <span data-rw-start="113.68" data-rw-transcript-version="2">
 &gt;&gt; Hi, I'm Daniel Teror North. I 've been
 </span>
 <span data-rw-start="116.399" data-rw-transcript-version="2">
 kicking around the computing industry
 </span>
 <span data-rw-start="118.88" data-rw-transcript-version="2">
 for about 35 years or something. Um, I
 </span>
 <span data-rw-start="122.399" data-rw-transcript-version="2">
 spent a lot of that writing what we
 </span>
 <span data-rw-start="124.24" data-rw-transcript-version="2">
 would now call artisan software, with my
 </span>
 <span data-rw-start="127.36" data-rw-transcript-version="2">
 actual hands.
 </span>
</p>
<p>
 <span data-rw-start="129.2" data-rw-transcript-version="2">
 Um, and I think I'm the token
 </span>
 <span data-rw-start="133.2" data-rw-transcript-version="2">
 grumpy person on the panel. I’m grumpy
 </span>
 <span data-rw-start="136.239" data-rw-transcript-version="2">
 that this tiny, tiny, tiny niche of AI
 </span>
 <span data-rw-start="140" data-rw-transcript-version="2">
 called LLMs has co-opted the term AI,
 </span>
 <span data-rw-start="143.84" data-rw-transcript-version="2">
 which is a huge, rich, exciting, vibrant
 </span>
 <span data-rw-start="146.8" data-rw-transcript-version="2">
 field. Uh, I'm grumpy that people think
 </span>
 <span data-rw-start="149.92" data-rw-transcript-version="2">
 there's a trillion dollar industry to be
 </span>
 <span data-rw-start="151.68" data-rw-transcript-version="2">
 had and they’re convinced that we don’t
 </span>
 <span data-rw-start="153.68" data-rw-transcript-version="2">
 need junior developers. I’m grumpy about
 </span>
 <span data-rw-start="156.08" data-rw-transcript-version="2">
 many things. I’m sure they’ll come up.
 </span>
</p>
<p>
 <span data-rw-start="157.92" data-rw-transcript-version="2">
 But yeah, so I’ve been around software
 </span>
 <span data-rw-start="159.44" data-rw-transcript-version="2">
 and people and teams and organizations
 </span>
 <span data-rw-start="161.12" data-rw-transcript-version="2">
 for a while. Um, and I’m not sure
 </span>
 <span data-rw-start="164.08" data-rw-transcript-version="2">
 why I’m on this panel. I know nothing
 </span>
 <span data-rw-start="165.92" data-rw-transcript-version="2">
 about LLMs, but I’m prepared to have an
 </span>
 <span data-rw-start="168.48" data-rw-transcript-version="2">
 opinion because I’m a middle-aged white
 </span>
 <span data-rw-start="169.92" data-rw-transcript-version="2">
 guy.
 </span>
 <span data-rw-start="171.611" data-rw-transcript-version="2">
 [laughter]
 </span>
 <span data-rw-start="173.44" data-rw-transcript-version="2">
 Um, yeah. Hello. I’m Sasha. I’m working
 </span>
 <span data-rw-start="176" data-rw-transcript-version="2">
 as principal engineer and architect
 </span>
 <span data-rw-start="177.76" data-rw-transcript-version="2">
 currently at Interport. I have
 </span>
 <span data-rw-start="179.76" data-rw-transcript-version="2">
 experience in retail and wholesale for
 </span>
 <span data-rw-start="182.4" data-rw-transcript-version="2">
 about 10 years now, mainly with a focus
 </span>
 <span data-rw-start="184.56" data-rw-transcript-version="2">
 on web architecture and building
 </span>
 <span data-rw-start="186.8" data-rw-transcript-version="2">
 software but also building
 </span>
 <span data-rw-start="187.84" data-rw-transcript-version="2">
 Organizations. So yes, AI is changing
 </span>
 <span data-rw-start="190.72" data-rw-transcript-version="2">
 how we're working and I’m looking
 </span>
 <span data-rw-start="192.159" data-rw-transcript-version="2">
 forward to the exchange.
 </span>
</p>
<p>
 <span data-rw-start="194.879" data-rw-transcript-version="2">
 I'm Corey. I'm the grumpy old woman.
 </span>
 <span data-rw-start="198.467" data-rw-transcript-version="2">
 &gt;&gt; [laughter]
 </span>
 <span data-rw-start="198.959" data-rw-transcript-version="2">
 &gt;&gt; I am, uh,
 </span>
 <span data-rw-start="201.599" data-rw-transcript-version="2">
 &gt;&gt; Besides all the other things that I’m
 </span>
 <span data-rw-start="203.04" data-rw-transcript-version="2">
 doing, I’m also teaching the teachers in
 </span>
 <span data-rw-start="205.44" data-rw-transcript-version="2">
 computer science how to teach computer
 </span>
 <span data-rw-start="207.04" data-rw-transcript-version="2">
 science to the computer science students,
 </span>
 <span data-rw-start="210.239" data-rw-transcript-version="2">
 which is becoming really interesting
 </span>
 <span data-rw-start="212.799" data-rw-transcript-version="2">
 with AI. So I’m optimistic and extremely
 </span>
 <span data-rw-start="216.799" data-rw-transcript-version="2">
 worried.
 </span>
</p>
<p>
 <span data-rw-start="219.599" data-rw-transcript-version="2">
 Hi, I’m Emily Bich. I’m a technical
 </span>
 <span data-rw-start="222" data-rw-transcript-version="2">
 coach. I’m an independent consultant, and
 </span>
 <span data-rw-start="224.799" data-rw-transcript-version="2">
 I’m very interested in test-driven
 </span>
 <span data-rw-start="227.36" data-rw-transcript-version="2">
 development. I’ve been teaching it these
 </span>
 <span data-rw-start="229.36" data-rw-transcript-version="2">
 past, like, 25 years, and it seems to have
 </span>
 <span data-rw-start="232.4" data-rw-transcript-version="2">
 fundamentally shifted in just the past
 </span>
 <span data-rw-start="234.319" data-rw-transcript-version="2">
 few months, and it’s turned into
 </span>
 <span data-rw-start="236.319" data-rw-transcript-version="2">
 something else, which is very exciting
 </span>
 <span data-rw-start="238.08" data-rw-transcript-version="2">
 and very scary.
 </span>
</p>
<p>
 <span data-rw-start="240.56" data-rw-transcript-version="2">
 &gt;&gt; Okay, great. So, um, already quite some
 </span>
 <span data-rw-start="243.76" data-rw-transcript-version="2">
 interesting topics that you teased on
 </span>
 <span data-rw-start="245.519" data-rw-transcript-version="2">
 here. Uh, I only have six questions, but I
 </span>
 <span data-rw-start="248.56" data-rw-transcript-version="2">
 I've already learned that I'm very optimistic
 </span>
 <span data-rw-start="250.4" data-rw-transcript-version="2">
 that we will, uh, um, discuss them all. Uh,
 </span>
 <span data-rw-start="254.48" data-rw-transcript-version="2">
 We'll start with the, actually, with the
 </span>
 <span data-rw-start="257.04" data-rw-transcript-version="2">
 title of this panel, which we chose, uh
 </span>
 <span data-rw-start="260.16" data-rw-transcript-version="2">
 a few months ago, uh, because there was a
 </span>
 <span data-rw-start="262.639" data-rw-transcript-version="2">
 trend, and still there is a trend, which
 </span>
 <span data-rw-start="264.24" data-rw-transcript-version="2">
 is called spec-driven development,
 </span>
 <span data-rw-start="267.04" data-rw-transcript-version="2">
 um, which, um, to me sounds suspiciously
 </span>
 <span data-rw-start="269.919" data-rw-transcript-version="2">
 like, um, yeah, back to waterfall, because
 </span>
 <span data-rw-start="272.96" data-rw-transcript-version="2">
 if you specify all the things very well,
 </span>
 <span data-rw-start="275.199" data-rw-transcript-version="2">
 then, uh, the AI will do the rest, uh, after
 </span>
 <span data-rw-start="278.56" data-rw-transcript-version="2">
 it. Um, Biga, you wrote a pretty nice
 </span>
 <span data-rw-start="282.639" data-rw-transcript-version="2">
 blog post, and a pretty popular blog post,
 </span>
 <span data-rw-start="284.639" data-rw-transcript-version="2">
 which is cited quite a lot, uh, uh, about
 </span>
 <span data-rw-start="287.44" data-rw-transcript-version="2">
 this topic. Um, so are we going back to
 </span>
 <span data-rw-start="290.16" data-rw-transcript-version="2">
 waterfall? What’s your take on that?
 </span>
</p>
<p>
 <span data-rw-start="292.639" data-rw-transcript-version="2">
 &gt;&gt; Yeah, it’s interesting because that
 </span>
 <span data-rw-start="293.919" data-rw-transcript-version="2">
 article gets shared a lot in a way like,
 </span>
 <span data-rw-start="296.479" data-rw-transcript-version="2">
 oh, look, I did it. Like, that article
 </span>
 <span data-rw-start="298.08" data-rw-transcript-version="2">
 describes, but I actually have a lot of
 </span>
 <span data-rw-start="300.4" data-rw-transcript-version="2">
 open and critical questions at the end
 </span>
 <span data-rw-start="302.24" data-rw-transcript-version="2">
 of the article about this topic. Um, but
 </span>
 <span data-rw-start="305.6" data-rw-transcript-version="2">
 yeah, I think, uh, I see kind of like
 </span>
 <span data-rw-start="308.56" data-rw-transcript-version="2">
 both
 </span>
 <span data-rw-start="310.16" data-rw-transcript-version="2">
 directions happening in some way.
 </span>
</p>
<p>
 <span data-rw-start="311.84" data-rw-transcript-version="2">
 One is this like yeah more pull towards
 </span>
 <span data-rw-start="314.479" data-rw-transcript-version="2">
 waterfall. I recently caught myself
 </span>
 <span data-rw-start="316.88" data-rw-transcript-version="2">
 thinking about the V model and I was
 </span>
 <span data-rw-start="318.96" data-rw-transcript-version="2">
 like oh my god what's happening? So kind
 </span>
 <span data-rw-start="320.72" data-rw-transcript-version="2">
 of this, yeah, we're like uh, I see Eric
 </span>
 <span data-rw-start="323.12" data-rw-transcript-version="2">
 there. Eric, you wrote like I don't know a
 </span>
 <span data-rw-start="324.72" data-rw-transcript-version="2">
 year ago about like are we just trying
 </span>
 <span data-rw-start="326" data-rw-transcript-version="2">
 to do offshoring again, right? If only we
 </span>
 <span data-rw-start="327.919" data-rw-transcript-version="2">
 write the right specifications, give it
 </span>
 <span data-rw-start="329.6" data-rw-transcript-version="2">
 to something, and then verify afterwards.
 </span>
</p>
<p>
 <span data-rw-start="331.36" data-rw-transcript-version="2">
 So there's definitely this trend of like
 </span>
 <span data-rw-start="332.88" data-rw-transcript-version="2">
 just writing again, figuring out how do
 </span>
 <span data-rw-start="335.6" data-rw-transcript-version="2">
 we just write better specifications,
 </span>
 <span data-rw-start="337.44" data-rw-transcript-version="2">
 which we've actually learned that we're
 </span>
 <span data-rw-start="339.039" data-rw-transcript-version="2">
 not good at, but you know, so that's the
 </span>
 <span data-rw-start="340.88" data-rw-transcript-version="2">
 the one pull. But then on the other side,
 </span>
 <span data-rw-start="342.88" data-rw-transcript-version="2">
 I've recently also seen people
 </span>
 <span data-rw-start="344.88" data-rw-transcript-version="2">
 discovering that when you want to create
 </span>
 <span data-rw-start="346.639" data-rw-transcript-version="2">
 a lot of throughput, you have to do all
 </span>
 <span data-rw-start="349.12" data-rw-transcript-version="2">
 of these things like automation,
 </span>
 <span data-rw-start="350.639" data-rw-transcript-version="2">
 continuous delivery, or I saw this thing
 </span>
 <span data-rw-start="352.96" data-rw-transcript-version="2">
 about somebody saying, oh, the SDLC,
 </span>
 <span data-rw-start="356" data-rw-transcript-version="2">
 which is actually like Simon was talking
 </span>
 <span data-rw-start="358.4" data-rw-transcript-version="2">
 about it today, is a very waterfall term,
 </span>
 <span data-rw-start="360.16" data-rw-transcript-version="2">
 right, that has had resurgence with AI.
 </span>
</p>
<p>
 <span data-rw-start="362.72" data-rw-transcript-version="2">
 And this person was writing about, oh,
 </span>
 <span data-rw-start="364.16" data-rw-transcript-version="2">
 is the SDLC collapsing? Do we not need
 </span>
 <span data-rw-start="367.039" data-rw-transcript-version="2">
 detailed requirements for the developers
 </span>
 <span data-rw-start="368.88" data-rw-transcript-version="2">
 anymore because they can do them with AI
 </span>
 <span data-rw-start="370.639" data-rw-transcript-version="2">
 now? And I was like, but you know,
 </span>
 <span data-rw-start="373.199" data-rw-transcript-version="2">
 shouldn't a story always be a
 </span>
 <span data-rw-start="374.56" data-rw-transcript-version="2">
 placeholder for a conversation?
 </span>
 <span data-rw-start="376.08" data-rw-transcript-version="2">
 Shouldn't that have always been the
 </span>
 <span data-rw-start="377.28" data-rw-transcript-version="2">
 case? So, there are some people actually
 </span>
 <span data-rw-start="378.96" data-rw-transcript-version="2">
 discovering these things that I think
 </span>
 <span data-rw-start="380.8" data-rw-transcript-version="2">
 are actually good ideas that you have to
 </span>
 <span data-rw-start="382.72" data-rw-transcript-version="2">
 do to get good throughput and good
 </span>
 <span data-rw-start="384.96" data-rw-transcript-version="2">
 feedback loops. So, there seem to be
 </span>
 <span data-rw-start="386.4" data-rw-transcript-version="2">
 both of those things happening at the
 </span>
 <span data-rw-start="388.4" data-rw-transcript-version="2">
 same time. Maybe speedrun to rediscover
 </span>
 <span data-rw-start="391.759" data-rw-transcript-version="2">
 good practices. I don't know. Hopefully,
 </span>
 <span data-rw-start="393.84" data-rw-transcript-version="2">
 that's where it will keep going.
 </span>
</p>
<p>
 <span data-rw-start="397.44" data-rw-transcript-version="2">
 &gt;&gt; But are there also reasons not to do it
 </span>
 <span data-rw-start="400.16" data-rw-transcript-version="2">
 this way,
 </span>
 <span data-rw-start="402.08" data-rw-transcript-version="2">
 &gt;&gt; not to do it with the
 </span>
 <span data-rw-start="403.52" data-rw-transcript-version="2">
 &gt;&gt; let's say spec in the beginning and
 </span>
 <span data-rw-start="406.24" data-rw-transcript-version="2">
 then just well,
 </span>
 <span data-rw-start="407.52" data-rw-transcript-version="2">
 &gt;&gt; yeah, I think it's ultimately it's all
 </span>
 <span data-rw-start="409.12" data-rw-transcript-version="2">
 about feedback loops, right? And I still
 </span>
 <span data-rw-start="410.72" data-rw-transcript-version="2">
 I still think working in small batches.
 </span>
</p>
<p>
 <span data-rw-start="413.12" data-rw-transcript-version="2">
 is valid but because we have this
 </span>
 <span data-rw-start="415.6" data-rw-transcript-version="2">
 increased level of automation now I was
 </span>
 <span data-rw-start="417.759" data-rw-transcript-version="2">
 talking about this today as well right
 </span>
 <span data-rw-start="419.039" data-rw-transcript-version="2">
 that people try to reduce the
 </span>
 <span data-rw-start="421.039" data-rw-transcript-version="2">
 supervision by the human and then you
 </span>
 <span data-rw-start="422.96" data-rw-transcript-version="2">
 have like much longer feedback loops
 </span>
 <span data-rw-start="424.4" data-rw-transcript-version="2">
 right like an agent going away for 20
 </span>
 <span data-rw-start="426" data-rw-transcript-version="2">
 minutes, 30 minutes, and then you have
 </span>
 <span data-rw-start="428.16" data-rw-transcript-version="2">
 like lots of stuff to verify, lots of
 </span>
 <span data-rw-start="430.08" data-rw-transcript-version="2">
 things that can go the wrong way in
 </span>
 <span data-rw-start="431.759" data-rw-transcript-version="2">
 between, so I think still think small
 </span>
 <span data-rw-start="433.84" data-rw-transcript-version="2">
 batches in some way are still super
 </span>
 <span data-rw-start="435.919" data-rw-transcript-version="2">
 valuable, and for that you would still
 </span>
 <span data-rw-start="437.28" data-rw-transcript-version="2">
 have to have small specifications in a
 </span>
 <span data-rw-start="439.68" data-rw-transcript-version="2">
 way. Right. So,
 </span>
 <span data-rw-start="441.84" data-rw-transcript-version="2">
 &gt;&gt; so still agile.
 </span>
</p>
<p>
 <span data-rw-start="443.199" data-rw-transcript-version="2">
 &gt;&gt; Yeah. Can I pick up on this with
 </span>
 <span data-rw-start="444.96" data-rw-transcript-version="2">
 reference to test-driven development?
 </span>
 <span data-rw-start="447.039" data-rw-transcript-version="2">
 Because this is that the kind of
 </span>
 <span data-rw-start="448.88" data-rw-transcript-version="2">
 premise of TDD is that you, you learn
 </span>
 <span data-rw-start="451.039" data-rw-transcript-version="2">
 during the development process and you
 </span>
 <span data-rw-start="453.52" data-rw-transcript-version="2">
 use that uh to adjust what you build.
 </span>
 <span data-rw-start="456.4" data-rw-transcript-version="2">
 So, spec driven development, if you, if
 </span>
 <span data-rw-start="458.88" data-rw-transcript-version="2">
 you don't have that feedback during the
 </span>
 <span data-rw-start="460.96" data-rw-transcript-version="2">
 the cycles, then you, you're, you're
 </span>
 <span data-rw-start="463.28" data-rw-transcript-version="2">
 Missing out. But what I have observed
 </span>
 <span data-rw-start="465.84" data-rw-transcript-version="2">
 now with, with TDD practitioners, I mean
 </span>
 <span data-rw-start="468.4" data-rw-transcript-version="2">
 I talked to about half a dozen technical
 </span>
 <span data-rw-start="471.28" data-rw-transcript-version="2">
 coaches who I know and trust, and know
 </span>
 <span data-rw-start="472.88" data-rw-transcript-version="2">
 that they were doing TDD in the before
 </span>
 <span data-rw-start="474.879" data-rw-transcript-version="2">
 times, and they've all adopted agentic
 </span>
 <span data-rw-start="478" data-rw-transcript-version="2">
 coding now. And they all told me, we are
 </span>
 <span data-rw-start="480.72" data-rw-transcript-version="2">
 not writing any code by hand anymore.
 </span>
</p>
<p>
 <span data-rw-start="483.44" data-rw-transcript-version="2">
 And I'm like, that is, that is huge. You
 </span>
 <span data-rw-start="486" data-rw-transcript-version="2">
 know what is even, what even is TDD if
 </span>
 <span data-rw-start="488" data-rw-transcript-version="2">
 you're not writing the code by hand? And
 </span>
 <span data-rw-start="489.84" data-rw-transcript-version="2">
 some of them were doing a bit of
 </span>
 <span data-rw-start="490.96" data-rw-transcript-version="2">
 refactoring. Some of them said, I do
 </span>
 <span data-rw-start="492.56" data-rw-transcript-version="2">
 some refactoring by hand, particularly
 </span>
 <span data-rw-start="494.4" data-rw-transcript-version="2">
 preparatory refactoring,
 </span>
 <span data-rw-start="496.879" data-rw-transcript-version="2">
 but not the coding part, because the
 </span>
 <span data-rw-start="498.639" data-rw-transcript-version="2">
 agents are so good at that. But what
 </span>
 <span data-rw-start="500.639" data-rw-transcript-version="2">
 what has remained is, so I've kind of
 </span>
 <span data-rw-start="502.4" data-rw-transcript-version="2">
 questioned them, what does your process
 </span>
 <span data-rw-start="504.08" data-rw-transcript-version="2">
 look like? And what has remained is the
 </span>
 <span data-rw-start="506.879" data-rw-transcript-version="2">
 short cycles that are characteristic of
 </span>
 <span data-rw-start="509.039" data-rw-transcript-version="2">
 TDD that you slice the functionality
 </span>
 <span data-rw-start="511.759" data-rw-transcript-version="2">
 and you build it a piece at a time, and
 </span>
 <span data-rw-start="513.44" data-rw-transcript-version="2">
 you adjust between slices. So, the, the
 </span>
 <span data-rw-start="516.56" data-rw-transcript-version="2">
 kind of the typical cycle time in TDD
 </span>
 <span data-rw-start="519.039" data-rw-transcript-version="2">
 Would be less than 10 minutes.
 </span>
</p>
<p>
 <span data-rw-start="521.2" data-rw-transcript-version="2">
 Um, probably a lot less than 10 minutes
 </span>
 <span data-rw-start="523.599" data-rw-transcript-version="2">
 for a refactoring, but they're saying
 </span>
 <span data-rw-start="525.6" data-rw-transcript-version="2">
 that, yeah, with the agentic AI writing
 </span>
 <span data-rw-start="527.519" data-rw-transcript-version="2">
 the code, my cycle time is the same or
 </span>
 <span data-rw-start="530.399" data-rw-transcript-version="2">
 or even faster now, which is very
 </span>
 <span data-rw-start="533.2" data-rw-transcript-version="2">
 different from traditional development,
 </span>
 <span data-rw-start="535.6" data-rw-transcript-version="2">
 but it's still recognizably TDD, I
 </span>
 <span data-rw-start="537.76" data-rw-transcript-version="2">
 think, even though they're not writing
 </span>
 <span data-rw-start="538.88" data-rw-transcript-version="2">
 the code by hand.
 </span>
</p>
<p>
 <span data-rw-start="541.279" data-rw-transcript-version="2">
 &gt;&gt; So, I just want to call out some
 </span>
 <span data-rw-start="543.44" data-rw-transcript-version="2">
 kind of terminology. I think there's a
 </span>
 <span data-rw-start="545.04" data-rw-transcript-version="2">
 straw man going on here. When we talk
 </span>
 <span data-rw-start="547.12" data-rw-transcript-version="2">
 about spec-driven, I mean TDD is
 </span>
 <span data-rw-start="549.68" data-rw-transcript-version="2">
 entirely spec-driven. The spec is
 </span>
 <span data-rw-start="551.92" data-rw-transcript-version="2">
 executable. You start with the spec. You
 </span>
 <span data-rw-start="554.16" data-rw-transcript-version="2">
 write it in Python or Java or whatever
 </span>
 <span data-rw-start="556.24" data-rw-transcript-version="2">
 you're going to be using, and then you or
 </span>
 <span data-rw-start="559.44" data-rw-transcript-version="2">
 some genies or something generate
 </span>
 <span data-rw-start="561.76" data-rw-transcript-version="2">
 produces some code that satisfies that
 </span>
 <span data-rw-start="564.399" data-rw-transcript-version="2">
 spec, and then you might, if you like, a
 </span>
 <span data-rw-start="567.12" data-rw-transcript-version="2">
 tidy kitchen, do some tidying up of that
 </span>
 <span data-rw-start="568.959" data-rw-transcript-version="2">
 code while it still continues. So, spec
 </span>
 <span data-rw-start="571.44" data-rw-transcript-version="2">
 driven doesn't necessarily mean—and I
 </span>
 <span data-rw-start="573.2" data-rw-transcript-version="2">
 think, and so I want to separate the idea.
 </span>
</p>
<p>
 <span data-rw-start="575.04" data-rw-transcript-version="2">
 Of using a spec from this idea of
 </span>
 <span data-rw-start="576.48" data-rw-transcript-version="2">
 oneshotting. So, oneshotting is you write
 </span>
 <span data-rw-start="579.04" data-rw-transcript-version="2">
 the whole spec and you say go on then,
 </span>
 <span data-rw-start="580.88" data-rw-transcript-version="2">
 genius, go and do your magic. Then you
 </span>
 <span data-rw-start="583.12" data-rw-transcript-version="2">
 come back and you have a product for
 </span>
 <span data-rw-start="586.08" data-rw-transcript-version="2">
 the kids. Um, Vodel from the 60s, I
 </span>
 <span data-rw-start="590.399" data-rw-transcript-version="2">
 believe, or possibly 70s, was this, uh, it
 </span>
 <span data-rw-start="593.76" data-rw-transcript-version="2">
 was, it was roughly a two-year cycle,
 </span>
 <span data-rw-start="597.44" data-rw-transcript-version="2">
 because you do a release every two years.
 </span>
</p>
<p>
 <span data-rw-start="599.12" data-rw-transcript-version="2">
 Because you were like, you know, cutting
 </span>
 <span data-rw-start="600.72" data-rw-transcript-version="2">
 edge. And what you would do at the point
 </span>
 <span data-rw-start="602.8" data-rw-transcript-version="2">
 when you were writing the specification,
 </span>
 <span data-rw-start="604.64" data-rw-transcript-version="2">
 you had your high-level functional spec,
 </span>
 <span data-rw-start="606.8" data-rw-transcript-version="2">
 and at the same time, sorry,
 </span>
 <span data-rw-start="608.32" data-rw-transcript-version="2">
 business requirements. And at the same
 </span>
 <span data-rw-start="609.519" data-rw-transcript-version="2">
 time, you would write your high-level, um,
 </span>
 <span data-rw-start="613.04" data-rw-transcript-version="2">
 testing frame, uh, requirements, uh,
 </span>
 <span data-rw-start="616.399" data-rw-transcript-version="2">
 testing plan. Then, as you got into
 </span>
 <span data-rw-start="618.24" data-rw-transcript-version="2">
 more detailed functional design—so high
 </span>
 <span data-rw-start="620.16" data-rw-transcript-version="2">
 level functional design, low-level
 </span>
 <span data-rw-start="621.279" data-rw-transcript-version="2">
 functional design—you would then have
 </span>
 <span data-rw-start="622.8" data-rw-transcript-version="2">
 corresponding tests for those. And this
 </span>
 <span data-rw-start="624.959" data-rw-transcript-version="2">
 V, it was sort of called a V model. So
 </span>
 <span data-rw-start="626.399" data-rw-transcript-version="2">
 you’d, you’d fill in the V, you’d meet at
 </span>
 <span data-rw-start="627.839" data-rw-transcript-version="2">
 the middle, write the code, and then
 </span>
 <span data-rw-start="628.88" data-rw-transcript-version="2">
 Make sure it all worked. And the
 </span>
 <span data-rw-start="631.279" data-rw-transcript-version="2">
 original scope for this was two years.
 </span>
</p>
<p>
 <span data-rw-start="633.44" data-rw-transcript-version="2">
 Now, if you look at what you're doing
 </span>
 <span data-rw-start="634.48" data-rw-transcript-version="2">
 with TDD, it's the same thing, but it's
 </span>
 <span data-rw-start="638" data-rw-transcript-version="2">
 20 minutes, right? So it's still the V
 </span>
 <span data-rw-start="640.64" data-rw-transcript-version="2">
 model. The spiral model, which was its
 </span>
 <span data-rw-start="642.959" data-rw-transcript-version="2">
 contemporary, by a guy called Barry Boehm,
 </span>
 <span data-rw-start="644.959" data-rw-transcript-version="2">
 was the idea that you would design
 </span>
 <span data-rw-start="646.8" data-rw-transcript-version="2">
 something, you would then, uh, do your
 </span>
 <span data-rw-start="649.519" data-rw-transcript-version="2">
 analysis. You'd then come out with the
 </span>
 <span data-rw-start="650.8" data-rw-transcript-version="2">
 technical design, the functional
 </span>
 <span data-rw-start="652.64" data-rw-transcript-version="2">
 design. You'd implement it and then you
 </span>
 <span data-rw-start="654" data-rw-transcript-version="2">
 test it, and it was like a little circle.
 </span>
 <span data-rw-start="655.68" data-rw-transcript-version="2">
 And his idea was that you had these
 </span>
 <span data-rw-start="656.959" data-rw-transcript-version="2">
 concentric circles, like a spiral, where
 </span>
 <span data-rw-start="659.279" data-rw-transcript-version="2">
 you'd start in the middle and you'd end
 </span>
 <span data-rw-start="660.48" data-rw-transcript-version="2">
 up with the product. And again, each
 </span>
 <span data-rw-start="662.72" data-rw-transcript-version="2">
 go around the spiral would be 18 months.
 </span>
</p>
<p>
 <span data-rw-start="665.519" data-rw-transcript-version="2">
 And again, if you say, well, actually, BDD
 </span>
 <span data-rw-start="667.519" data-rw-transcript-version="2">
 is that, but it's 18 minutes [laughter].
 </span>
 <span data-rw-start="670" data-rw-transcript-version="2">
 Then we're still doing V model and
 </span>
 <span data-rw-start="671.76" data-rw-transcript-version="2">
 spiral, and it's just that the
 </span>
 <span data-rw-start="673.68" data-rw-transcript-version="2">
 time scales have massively
 </span>
 <span data-rw-start="675.36" data-rw-transcript-version="2">
 condensed.
 </span>
 <span data-rw-start="677.76" data-rw-transcript-version="2">
 So, I guess, in terms of, like, what are
 </span>
 <span data-rw-start="680.56" data-rw-transcript-version="2">
 We're doing with, um, with Spectriven. I think
 </span>
 <span data-rw-start="683.68" data-rw-transcript-version="2">
 the idea of oneshotting for a prototype
 </span>
 <span data-rw-start="685.839" data-rw-transcript-version="2">
 is brilliant, right? And it does
 </span>
 <span data-rw-start="688.24" data-rw-transcript-version="2">
 it's, uh, Eric Mayer has this wonderful
 </span>
 <span data-rw-start="690.16" data-rw-transcript-version="2">
 language he uses. Talks about
 </span>
 <span data-rw-start="691.36" data-rw-transcript-version="2">
 democratizing. So, he likes to democratize
 </span>
 <span data-rw-start="694.399" data-rw-transcript-version="2">
 programming, democratize whatever, and
 </span>
 <span data-rw-start="697.519" data-rw-transcript-version="2">
 one-upping with prompts. Democratize
 </span>
 <span data-rw-start="700.48" data-rw-transcript-version="2">
 that prototyping activity for
 </span>
 <span data-rw-start="702.8" data-rw-transcript-version="2">
 non-technical people who've got a bit of
 </span>
 <span data-rw-start="704.16" data-rw-transcript-version="2">
 an idea. But you absolutely do not want
 </span>
 <span data-rw-start="707.44" data-rw-transcript-version="2">
 that for evolving code. So, going into
 </span>
 <span data-rw-start="710" data-rw-transcript-version="2">
 code that exists and make it do a new
 </span>
 <span data-rw-start="711.76" data-rw-transcript-version="2">
 thing as well, or make it do a thing
 </span>
 <span data-rw-start="713.279" data-rw-transcript-version="2">
 differently. For that, you need very
 </span>
 <span data-rw-start="715.2" data-rw-transcript-version="2">
 different guard rails, and we're right
 </span>
 <span data-rw-start="716.32" data-rw-transcript-version="2">
 back to TDD again.
 </span>
</p>
<p>
 <span data-rw-start="719.36" data-rw-transcript-version="2">
 &gt;&gt; Yeah. So, I agree with everything being
 </span>
 <span data-rw-start="722" data-rw-transcript-version="2">
 said, and I think that it's definitely
 </span>
 <span data-rw-start="724.8" data-rw-transcript-version="2">
 not going back to waterfall. It's, if
 </span>
 <span data-rw-start="726.959" data-rw-transcript-version="2">
 anything, it's becoming much more agile.
 </span>
 <span data-rw-start="729.279" data-rw-transcript-version="2">
 And to follow up on all the things that
 </span>
 <span data-rw-start="731.12" data-rw-transcript-version="2">
 have been said to me, the code now is a
 </span>
 <span data-rw-start="733.839" data-rw-transcript-version="2">
 bit like metal. Metal used to be hard to
 </span>
 <span data-rw-start="736.959" data-rw-transcript-version="2">
 get by and difficult to work with. And
 </span>
 <span data-rw-start="739.68" data-rw-transcript-version="2">
 When you made something in metal, it was
 </span>
 <span data-rw-start="741.36" data-rw-transcript-version="2">
 made to last.
 </span>
</p>
<p>
 <span data-rw-start="743.44" data-rw-transcript-version="2">
 You probably have something of metal
 </span>
 <span data-rw-start="745.04" data-rw-transcript-version="2">
 from your grandparents. But the metal
 </span>
 <span data-rw-start="747.36" data-rw-transcript-version="2">
 that we use right now, we just throw it
 </span>
 <span data-rw-start="749.12" data-rw-transcript-version="2">
 away after we've used it once. If we
 </span>
 <span data-rw-start="750.959" data-rw-transcript-version="2">
 look at the garbage cans, it's just
 </span>
 <span data-rw-start="752.959" data-rw-transcript-version="2">
 throw away. Well, it's reuse of course
 </span>
 <span data-rw-start="754.639" data-rw-transcript-version="2">
 because we're in Germany, but you know
 </span>
 <span data-rw-start="756.399" data-rw-transcript-version="2">
 what I mean. And I think code is
 </span>
 <span data-rw-start="758.72" data-rw-transcript-version="2">
 becoming that. And I don't know whether
 </span>
 <span data-rw-start="760.48" data-rw-transcript-version="2">
 that's good or bad. It could be a way of
 </span>
 <span data-rw-start="762.24" data-rw-transcript-version="2">
 democratizing the code. It could be a
 </span>
 <span data-rw-start="764.48" data-rw-transcript-version="2">
 way of spending a lot of energy for
 </span>
 <span data-rw-start="766.16" data-rw-transcript-version="2">
 nothing. But it is interesting that the
 </span>
 <span data-rw-start="769.2" data-rw-transcript-version="2">
 whole value of code and the whole blood,
 </span>
 <span data-rw-start="772.639" data-rw-transcript-version="2">
 sweat and tears about code is changing.
 </span>
</p>
<p>
 <span data-rw-start="775.04" data-rw-transcript-version="2">
 I think
 </span>
 <span data-rw-start="778.32" data-rw-transcript-version="2">
 &gt;&gt; Maybe just to like, unless you, I just
 </span>
 <span data-rw-start="780.32" data-rw-transcript-version="2">
 wanted to, with the spec-driven, just for
 </span>
 <span data-rw-start="782.88" data-rw-transcript-version="2">
 the record, I think there's no
 </span>
 <span data-rw-start="784.079" data-rw-transcript-version="2">
 satisfactory definition of the term
 </span>
 <span data-rw-start="785.76" data-rw-transcript-version="2">
 speculative development right now. So I
 </span>
 <span data-rw-start="787.2" data-rw-transcript-version="2">
 actually don't like talking about it. I try
 </span>
 <span data-rw-start="788.72" data-rw-transcript-version="2">
 to figure out what it is that’s why I
 </span>
 <span data-rw-start="790.88" data-rw-transcript-version="2">
 Wrote the blog post, but I just had to
 </span>
 <span data-rw-start="792.959" data-rw-transcript-version="2">
 like, with like, a lot of discussion
 </span>
 <span data-rw-start="795.04" data-rw-transcript-version="2">
 convince my colleagues last week to not
 </span>
 <span data-rw-start="797.04" data-rw-transcript-version="2">
 put this on the ThoughtWorks technology
 </span>
 <span data-rw-start="798.72" data-rw-transcript-version="2">
 radar again, because I kept saying
 </span>
 <span data-rw-start="800.24" data-rw-transcript-version="2">
 there's no good definition for this.
 </span>
</p>
<p>
 <span data-rw-start="801.839" data-rw-transcript-version="2">
 It's just like something people say, and
 </span>
 <span data-rw-start="803.36" data-rw-transcript-version="2">
 everybody means something else by spec.
 </span>
 <span data-rw-start="805.2" data-rw-transcript-version="2">
 So, and that's also one of the
 </span>
 <span data-rw-start="806.32" data-rw-transcript-version="2">
 challenges right now in the space,
 </span>
 <span data-rw-start="807.44" data-rw-transcript-version="2">
 because it's moving so fast that people
 </span>
 <span data-rw-start="809.04" data-rw-transcript-version="2">
 come up with these terms and then
 </span>
 <span data-rw-start="810.399" data-rw-transcript-version="2">
 immediately, there's like a hundred
 </span>
 <span data-rw-start="812" data-rw-transcript-version="2">
 different definitions of it. So, um,
 </span>
 <span data-rw-start="815.04" data-rw-transcript-version="2">
 yeah, I wish the term would just go away
 </span>
 <span data-rw-start="816.88" data-rw-transcript-version="2">
 to be honest.
 </span>
 <span data-rw-start="818.639" data-rw-transcript-version="2">
 Yeah. And for me, it sounds a little bit
 </span>
 <span data-rw-start="820.079" data-rw-transcript-version="2">
 like, just we call it because we now call
 </span>
 <span data-rw-start="822.399" data-rw-transcript-version="2">
 it spec. We think about waterfall, but if
 </span>
 <span data-rw-start="824.8" data-rw-transcript-version="2">
 we would call it user story that someone
 </span>
 <span data-rw-start="828" data-rw-transcript-version="2">
 takes, understands, then plans what to do,
 </span>
 <span data-rw-start="830.399" data-rw-transcript-version="2">
 and then implements it, we are doing that
 </span>
 <span data-rw-start="832.399" data-rw-transcript-version="2">
 for years, and we call it agile. But as
 </span>
 <span data-rw-start="834.16" data-rw-transcript-version="2">
 soon as we don’t call it any longer user
 </span>
 <span data-rw-start="835.839" data-rw-transcript-version="2">
 story but spec, we say it’s waterfall. So
 </span>
 <span data-rw-start="838.48" data-rw-transcript-version="2">
 I'm like we just do the same as we did before in a different technological way,
 </span>
 <span data-rw-start="840.56" data-rw-transcript-version="2">
 but it's, for me, it's still the same a way.
 </span>
</p>
<p>
 <span data-rw-start="844.16" data-rw-transcript-version="2">
 But if I, you believe, writing a book of specs and user stories and then give it to a team and come back half a year later,
 </span>
 <span data-rw-start="846.639" data-rw-transcript-version="2">
 and for sure, you will not get what you wanted.
 </span>
 <span data-rw-start="849.68" data-rw-transcript-version="2">
 Right?
 </span>
 <span data-rw-start="851.839" data-rw-transcript-version="2">
 So, and this iterative cycles need to be still there.
 </span>
 <span data-rw-start="854.399" data-rw-transcript-version="2">
 They are just getting faster, hopefully.
 </span>
</p>
<p>
 <span data-rw-start="862.24" data-rw-transcript-version="2">
 &gt;&gt; I just want to add as well, um, as someone who spent the first, at least the first 20 years of his career writing code for money,
 </span>
 <span data-rw-start="866.56" data-rw-transcript-version="2">
 and the latter 15 or so, uh, talking to people about how they can write code for money.
 </span>
 <span data-rw-start="868.399" data-rw-transcript-version="2">
 Um, I don't care about code.
 </span>
 <span data-rw-start="872.72" data-rw-transcript-version="2">
 I care about what the code does.
 </span>
 <span data-rw-start="874.24" data-rw-transcript-version="2">
 I care about the business capability I get from code.
 </span>
 <span data-rw-start="876.959" data-rw-transcript-version="2">
 And if you can give me that business capability with less code,
 </span>
 <span data-rw-start="878.72" data-rw-transcript-version="2">
 you win.
 </span>
 <span data-rw-start="880.959" data-rw-transcript-version="2">
 If you can give me that capability with no code at all,
 </span>
 <span data-rw-start="882.639" data-rw-transcript-version="2">
 you win at programming.
 </span>
 <span data-rw-start="885.36" data-rw-transcript-version="2">
 Right?
 </span>
 <span data-rw-start="887.76" data-rw-transcript-version="2">
 So, I am absolutely fine with an agent or a LLM or a human.
 </span>
</p>
<p>
 <span data-rw-start="898.959" data-rw-transcript-version="2">
 Being throwing away code and rewriting
 </span>
 <span data-rw-start="901.6" data-rw-transcript-version="2">
 chunks of it if that will get to the
 </span>
 <span data-rw-start="903.76" data-rw-transcript-version="2">
 goal faster than trying to manipulate
 </span>
 <span data-rw-start="905.519" data-rw-transcript-version="2">
 the code that's already there. The code
 </span>
 <span data-rw-start="907.12" data-rw-transcript-version="2">
 is not an asset. The code is the
 </span>
 <span data-rw-start="909.04" data-rw-transcript-version="2">
 liability. The business capability is
 </span>
 <span data-rw-start="911.92" data-rw-transcript-version="2">
 the asset. So if I can get something
 </span>
 <span data-rw-start="914.079" data-rw-transcript-version="2">
 that can tank through that code and make
 </span>
 <span data-rw-start="916.639" data-rw-transcript-version="2">
 it be the thing I want it to be, I kind
 </span>
 <span data-rw-start="918.959" data-rw-transcript-version="2">
 of don’t care what what’s doing that.
 </span>
</p>
<p>
 <span data-rw-start="923.36" data-rw-transcript-version="2">
 That’s a that’s a good uh bridge, let’s
 </span>
 <span data-rw-start="926.079" data-rw-transcript-version="2">
 say, or segue or something to my next uh
 </span>
 <span data-rw-start="929.6" data-rw-transcript-version="2">
 topic. I’m jumping a little bit here
 </span>
 <span data-rw-start="931.92" data-rw-transcript-version="2">
 in my list, but uh I think that fits
 </span>
 <span data-rw-start="933.76" data-rw-transcript-version="2">
 very well. So, it’s uh about trust in
 </span>
 <span data-rw-start="936.88" data-rw-transcript-version="2">
 code. Um, the first thing you hear always
 </span>
 <span data-rw-start="940.72" data-rw-transcript-version="2">
 when you discuss with somebody
 </span>
 <span data-rw-start="942.399" data-rw-transcript-version="2">
 about uh AI-generated code is uh can I
 </span>
 <span data-rw-start="945.519" data-rw-transcript-version="2">
 trust it? Uh, do I know whether that’s
 </span>
 <span data-rw-start="947.92" data-rw-transcript-version="2">
 the correct code or it’s not the correct
 </span>
 <span data-rw-start="949.44" data-rw-transcript-version="2">
 code? Do I review or do I need to review
 </span>
 <span data-rw-start="952.16" data-rw-transcript-version="2">
 each line of code that I’ve written
 </span>
 <span data-rw-start="953.759" data-rw-transcript-version="2">
 there? Actually, when thinking about it,
 </span>
 <span data-rw-start="955.92" data-rw-transcript-version="2">
 I realized that, um, this is not a really
 </span>
 <span data-rw-start="958.8" data-rw-transcript-version="2">
 new problem in our industry.
 </span>
</p>
<p>
 <span data-rw-start="961.199" data-rw-transcript-version="2">
 Discussed that, uh, many years ago, uh,
 </span>
 <span data-rw-start="964.399" data-rw-transcript-version="2">
 regarding, for instance, open source
 </span>
 <span data-rw-start="966.16" data-rw-transcript-version="2">
 libraries you're using, uh, which is also
 </span>
 <span data-rw-start="968.639" data-rw-transcript-version="2">
 part of your system, and where, uh, you
 </span>
 <span data-rw-start="971.839" data-rw-transcript-version="2">
 need or where there was the discussion
 </span>
 <span data-rw-start="974" data-rw-transcript-version="2">
 whether you need to read every line of
 </span>
 <span data-rw-start="975.519" data-rw-transcript-version="2">
 code of your open source library that
 </span>
 <span data-rw-start="977.12" data-rw-transcript-version="2">
 you are using. That said, those
 </span>
 <span data-rw-start="979.759" data-rw-transcript-version="2">
 libraries were usually crowd tested. So
 </span>
 <span data-rw-start="982.24" data-rw-transcript-version="2">
 many, so you use them and hope that
 </span>
 <span data-rw-start="985.279" data-rw-transcript-version="2">
 somebody else, uh, already found the bug
 </span>
 <span data-rw-start="987.6" data-rw-transcript-version="2">
 that, uh, uh, was risky. Um, but still, uh, we
 </span>
 <span data-rw-start="992.48" data-rw-transcript-version="2">
 have generated code, and how do we create
 </span>
 <span data-rw-start="995.839" data-rw-transcript-version="2">
 trust in the code that, uh, a machine
 </span>
 <span data-rw-start="999.92" data-rw-transcript-version="2">
 generates for us? How do we do that? Any
 </span>
 <span data-rw-start="1002.639" data-rw-transcript-version="2">
 ideas?
 </span>
</p>
<p>
 <span data-rw-start="1005.519" data-rw-transcript-version="2">
 &gt;&gt; Beer explains the concept of harnesses.
 </span>
 <span data-rw-start="1007.759" data-rw-transcript-version="2">
 This is just a breakthrough idea
 </span>
 <span data-rw-start="1009.839" data-rw-transcript-version="2">
 that has appeared in, like, the last couple
 </span>
 <span data-rw-start="1011.279" data-rw-transcript-version="2">
 of weeks, and I'm so excited about the
 </span>
 <span data-rw-start="1013.279" data-rw-transcript-version="2">
 idea of harnesses.
 </span>
</p>
<p>
 <span data-rw-start="1015.519" data-rw-transcript-version="2">
 &gt;&gt; Yeah, it's maybe not a breakthrough idea
 </span>
 <span data-rw-start="1016.959" data-rw-transcript-version="2">
 but, like, it's like now a name that is
 </span>
 <span data-rw-start="1019.759" data-rw-transcript-version="2">
 coming out for it. It's just, like,
 </span>
 <span data-rw-start="1022.56" data-rw-transcript-version="2">
 basically not just giving the, um, uh, the
 </span>
 <span data-rw-start="1026.48" data-rw-transcript-version="2">
 Agents like the feed forward of like here's like our coding conventions,
 </span>
 <span data-rw-start="1028.4" data-rw-transcript-version="2">
 here's how we want our code to be
 </span>
 <span data-rw-start="1030.16" data-rw-transcript-version="2">
 structured and all of that. But also the
 </span>
 <span data-rw-start="1031.28" data-rw-transcript-version="2">
 same as developers just giving the agent
 </span>
 <span data-rw-start="1032.959" data-rw-transcript-version="2">
 direct access to the feedback right to
 </span>
 <span data-rw-start="1034.559" data-rw-transcript-version="2">
 the static code analysis and all of that.
 </span>
</p>
<p>
 <span data-rw-start="1036.319" data-rw-transcript-version="2">
 And I was just saying to
 </span>
 <span data-rw-start="1038.559" data-rw-transcript-version="2">
 Emily before that, um, I was for like a
 </span>
 <span data-rw-start="1040.319" data-rw-transcript-version="2">
 long time a bit always a bit dismissive
 </span>
 <span data-rw-start="1042.959" data-rw-transcript-version="2">
 of static code analysis because it was
 </span>
 <span data-rw-start="1045.28" data-rw-transcript-version="2">
 it's not the full guarantee that the
 </span>
 <span data-rw-start="1047.28" data-rw-transcript-version="2">
 code is actually good and all of that.
 </span>
</p>
<p>
 <span data-rw-start="1049.12" data-rw-transcript-version="2">
 But then, like, some years ago I had a, uh
 </span>
 <span data-rw-start="1054" data-rw-transcript-version="2">
 junior developer on my team, uh, who, like,
 </span>
 <span data-rw-start="1057.12" data-rw-transcript-version="2">
 we paired with, uh, her a lot, but then
 </span>
 <span data-rw-start="1059.6" data-rw-transcript-version="2">
 also we, she was working by herself to
 </span>
 <span data-rw-start="1061.84" data-rw-transcript-version="2">
 like, you know, build up, you know, that you
 </span>
 <span data-rw-start="1064.72" data-rw-transcript-version="2">
 know, as a junior, you can code without
 </span>
 <span data-rw-start="1066.16" data-rw-transcript-version="2">
 like, a senior next to you, right? And, um,
 </span>
 <span data-rw-start="1068.96" data-rw-transcript-version="2">
 she had access to, like, a Sonar setup, and
 </span>
 <span data-rw-start="1071.12" data-rw-transcript-version="2">
 it was actually super useful for her,
 </span>
 <span data-rw-start="1072.72" data-rw-transcript-version="2">
 right? And then I was like, oh yeah, right,
 </span>
 <span data-rw-start="1074.08" data-rw-transcript-version="2">
 like I forgot, this is actually, this can
 </span>
 <span data-rw-start="1076.48" data-rw-transcript-version="2">
 actually catch a lot of things that you
 </span>
 <span data-rw-start="1078.32" data-rw-transcript-version="2">
 Might be doing wrong, and I was thinking
 </span>
 <span data-rw-start="1079.84" data-rw-transcript-version="2">
 about that now. And, um, there's this like
 </span>
 <span data-rw-start="1083.039" data-rw-transcript-version="2">
 more and more chatter about building
 </span>
 <span data-rw-start="1084.4" data-rw-transcript-version="2">
 custom linter and more, making more use
 </span>
 <span data-rw-start="1086.96" data-rw-transcript-version="2">
 of structural tests like ArcUnit style,
 </span>
 <span data-rw-start="1089.52" data-rw-transcript-version="2">
 and also the fact that these types of
 </span>
 <span data-rw-start="1092.32" data-rw-transcript-version="2">
 things, we can also now custom build a
 </span>
 <span data-rw-start="1094.32" data-rw-transcript-version="2">
 lot easier. So, we can build a lot more
 </span>
 <span data-rw-start="1096.64" data-rw-transcript-version="2">
 custom structural tests and stuff like
 </span>
 <span data-rw-start="1099.12" data-rw-transcript-version="2">
 that. So, this would all be about, like
 </span>
 <span data-rw-start="1100.64" data-rw-transcript-version="2">
 the internal code quality mostly, right?
 </span>
</p>
<p>
 <span data-rw-start="1103.36" data-rw-transcript-version="2">
 And I think maybe that might even make
 </span>
 <span data-rw-start="1105.2" data-rw-transcript-version="2">
 agents build better, more modular code bases
 </span>
 <span data-rw-start="1107.679" data-rw-transcript-version="2">
 than humans do.
 </span>
 <span data-rw-start="1110.24" data-rw-transcript-version="2">
 So, it still doesn't solve the problem of
 </span>
 <span data-rw-start="1112.16" data-rw-transcript-version="2">
 a lot of other quality attributes or
 </span>
 <span data-rw-start="1113.679" data-rw-transcript-version="2">
 like just, is the behavior there? But, um,
 </span>
 <span data-rw-start="1116.88" data-rw-transcript-version="2">
 there's definitely, like, a lot of, like
 </span>
 <span data-rw-start="1119.12" data-rw-transcript-version="2">
 more traditional stuff that we can throw
 </span>
 <span data-rw-start="1120.72" data-rw-transcript-version="2">
 at the agents and make, like, a better
 </span>
 <span data-rw-start="1122.24" data-rw-transcript-version="2">
 feedback loop for them that will
 </span>
 <span data-rw-start="1124.08" data-rw-transcript-version="2">
 increase our trust. And then, depending
 </span>
 <span data-rw-start="1125.679" data-rw-transcript-version="2">
 on the use case, we can decide if that
 </span>
 <span data-rw-start="1128.24" data-rw-transcript-version="2">
 harness that we have is actually good
 </span>
 <span data-rw-start="1129.919" data-rw-transcript-version="2">
 enough for the risk profile of the use.
 </span>
</p>
<p>
 <span data-rw-start="1132.32" data-rw-transcript-version="2">
 The case that we have or not. And so all of
 </span>
 <span data-rw-start="1134.4" data-rw-transcript-version="2">
 those things will determine how much
 </span>
 <span data-rw-start="1136.4" data-rw-transcript-version="2">
 confidence I have in the output.
 </span>
 <span data-rw-start="1139.52" data-rw-transcript-version="2">
 I just have something very short to say
 </span>
 <span data-rw-start="1141.52" data-rw-transcript-version="2">
 and that is that every time we need to
 </span>
 <span data-rw-start="1144.16" data-rw-transcript-version="2">
 transform something people want it to be
 </span>
 <span data-rw-start="1147.2" data-rw-transcript-version="2">
 perfect. So but can it solve this? Can
 </span>
 <span data-rw-start="1150.16" data-rw-transcript-version="2">
 it solve this? Will this be perfect? And
 </span>
 <span data-rw-start="1152.48" data-rw-transcript-version="2">
 what I normally say is that as long as
 </span>
 <span data-rw-start="1154.72" data-rw-transcript-version="2">
 we don't make it worse and I think the
 </span>
 <span data-rw-start="1156.559" data-rw-transcript-version="2">
 fact about trust we already, as you said,
 </span>
 <span data-rw-start="1159.039" data-rw-transcript-version="2">
 we already have that problem. So I don't
 </span>
 <span data-rw-start="1161.28" data-rw-transcript-version="2">
 think that we should
 </span>
 <span data-rw-start="1163.28" data-rw-transcript-version="2">
 expect it to be perfect because it can
 </span>
 <span data-rw-start="1166.32" data-rw-transcript-version="2">
 never be, and it never was.
 </span>
</p>
<p>
 <span data-rw-start="1170.16" data-rw-transcript-version="2">
 Most of my job as a technical coach has
 </span>
 <span data-rw-start="1172.32" data-rw-transcript-version="2">
 been helping developers to write better
 </span>
 <span data-rw-start="1174.32" data-rw-transcript-version="2">
 quality code, and it’s a very
 </span>
 <span data-rw-start="1177.44" data-rw-transcript-version="2">
 skilled activity, particularly when you
 </span>
 <span data-rw-start="1179.2" data-rw-transcript-version="2">
 have a very old, difficult code base, to
 </span>
 <span data-rw-start="1181.84" data-rw-transcript-version="2">
 be able to raise the code quality. So
 </span>
 <span data-rw-start="1184.24" data-rw-transcript-version="2">
 it’s so exciting to think that now
 </span>
 <span data-rw-start="1186.72" data-rw-transcript-version="2">
 you can get these deterministic tools
 </span>
 <span data-rw-start="1188.4" data-rw-transcript-version="2">
 that can measure the code quality at
 </span>
 <span data-rw-start="1190.08" data-rw-transcript-version="2">
 least a minimum, kind of, make sure it
 </span>
 <span data-rw-start="1192.88" data-rw-transcript-version="2">
 Doesn't make the worst mistakes, and it has a ratchet. It can access
 </span>
 <span data-rw-start="1195.28" data-rw-transcript-version="2">
 refactoring tools, proper refactoring
 </span>
 <span data-rw-start="1197.52" data-rw-transcript-version="2">
 tools. It's starting to actually get
 </span>
 <span data-rw-start="1199.2" data-rw-transcript-version="2">
 a wide variety of refactoring tools. And
 </span>
 <span data-rw-start="1201.919" data-rw-transcript-version="2">
 this idea that actually the code quality
 </span>
 <span data-rw-start="1204.32" data-rw-transcript-version="2">
 can be improved without human skill with
 </span>
 <span data-rw-start="1206.48" data-rw-transcript-version="2">
 just static analysis tools and
 </span>
 <span data-rw-start="1209.6" data-rw-transcript-version="2">
 refactoring tools and an agent in a
 </span>
 <span data-rw-start="1211.84" data-rw-transcript-version="2">
 loop. That is, that is amazing if
 </span>
 <span data-rw-start="1214" data-rw-transcript-version="2">
 that's actually going to work, and I'm
 </span>
 <span data-rw-start="1216.72" data-rw-transcript-version="2">
 really hopeful that it will.
 </span>
</p>
<p>
 <span data-rw-start="1218" data-rw-transcript-version="2">
 &gt;&gt; I think the risk, and this is going to
 </span>
 <span data-rw-start="1220.4" data-rw-transcript-version="2">
 keep happening, right? And I’m going to
 </span>
 <span data-rw-start="1222.48" data-rw-transcript-version="2">
 keep saying it, and it’s still going to
 </span>
 <span data-rw-start="1224.24" data-rw-transcript-version="2">
 keep happening. The risk is that we’re
 </span>
 <span data-rw-start="1225.6" data-rw-transcript-version="2">
 anthropomorphizing a machine, right?
 </span>
</p>
<p>
 <span data-rw-start="1232.64" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="1234.64" data-rw-transcript-version="2">
 Claude doesn’t give a crap.
 </span>
 <span data-rw-start="1238.24" data-rw-transcript-version="2">
 C-Pilot doesn’t give a crap. Not because
 </span>
 <span data-rw-start="1240.96" data-rw-transcript-version="2">
 it doesn’t like you, because it doesn’t
 </span>
 <span data-rw-start="1243.28" data-rw-transcript-version="2">
 have the capability to give a crap.
 </span>
 <span data-rw-start="1246.559" data-rw-transcript-version="2">
 That’s not there. Claude can’t
 </span>
 <span data-rw-start="1249.52" data-rw-transcript-version="2">
 program. It doesn’t know how to program.
 </span>
 <span data-rw-start="1252.559" data-rw-transcript-version="2">
 It knows how to produce things that look
 </span>
 <span data-rw-start="1255.52" data-rw-transcript-version="2">
 Like code in response to things that
 </span>
 <span data-rw-start="1258.32" data-rw-transcript-version="2">
 look like questions. It has no domain
 </span>
 <span data-rw-start="1261.12" data-rw-transcript-version="2">
 awareness. When you're doing a financial
 </span>
 <span data-rw-start="1264.08" data-rw-transcript-version="2">
 billing system, right? It doesn't know
 </span>
 <span data-rw-start="1266.799" data-rw-transcript-version="2">
 the domain of finance, the domain of
 </span>
 <span data-rw-start="1268.559" data-rw-transcript-version="2">
 billing. It doesn't know any of that
 </span>
 <span data-rw-start="1269.6" data-rw-transcript-version="2">
 stuff. It just knows how to produce
 </span>
 <span data-rw-start="1272.96" data-rw-transcript-version="2">
 convincing looking output based on
 </span>
 <span data-rw-start="1274.64" data-rw-transcript-version="2">
 convincing looking input. And what we're
 </span>
 <span data-rw-start="1276.64" data-rw-transcript-version="2">
 doing is we're getting better at more
 </span>
 <span data-rw-start="1278.559" data-rw-transcript-version="2">
 convincing looking input which
 </span>
 <span data-rw-start="1280.4" data-rw-transcript-version="2">
 constrains and again the feedback loops
 </span>
 <span data-rw-start="1282.08" data-rw-transcript-version="2">
 mean we're more likely to get convincing
 </span>
 <span data-rw-start="1283.44" data-rw-transcript-version="2">
 looking output. I can't not mention
 </span>
 <span data-rw-start="1286" data-rw-transcript-version="2">
 Hanland's razor, right? Don't ascribe to
 </span>
 <span data-rw-start="1287.6" data-rw-transcript-version="2">
 malice what can be explained by
 </span>
 <span data-rw-start="1289.28" data-rw-transcript-version="2">
 incompetence.
 </span>
</p>
<p>
 <span data-rw-start="1291.12" data-rw-transcript-version="2">
 And the key difference this LLM that
 </span>
 <span data-rw-start="1293.76" data-rw-transcript-version="2">
 is not a person and will never be a
 </span>
 <span data-rw-start="1296.64" data-rw-transcript-version="2">
 person is not a junior developer. Right?
 </span>
 <span data-rw-start="1299.2" data-rw-transcript-version="2">
 The LLM there's two things about the
 </span>
 <span data-rw-start="1300.559" data-rw-transcript-version="2">
 LLM. One, it doesn't care about your
 </span>
 <span data-rw-start="1302.24" data-rw-transcript-version="2">
 code. Two, it will not it doesn't want
 </span>
 <span data-rw-start="1305.44" data-rw-transcript-version="2">
 to learn. It has no valition. Right? A
 </span>
 <span data-rw-start="1308.72" data-rw-transcript-version="2">
 junior developer is really most of the
 </span>
 <span data-rw-start="1310.559" data-rw-transcript-version="2">
 The ones I've worked with and hired and
 </span>
 <span data-rw-start="1312" data-rw-transcript-version="2">
 trained and whatever are desperately eager
 </span>
 <span data-rw-start="1314.64" data-rw-transcript-version="2">
 to learn, grow, and practice, and do
 </span>
 <span data-rw-start="1316.72" data-rw-transcript-version="2">
 those things. They're going to mess
 </span>
 <span data-rw-start="1317.76" data-rw-transcript-version="2">
 up, and they're going to mess up again
 </span>
 <span data-rw-start="1318.799" data-rw-transcript-version="2">
 and again. But you can
 </span>
 <span data-rw-start="1321.52" data-rw-transcript-version="2">
 think of them as chaotic good,
 </span>
 <span data-rw-start="1324.96" data-rw-transcript-version="2">
 they're finding their way, but they have
 </span>
 <span data-rw-start="1326.559" data-rw-transcript-version="2">
 good intentions. Whereas
 </span>
 <span data-rw-start="1329.679" data-rw-transcript-version="2">
 an LLM is at best chaotic neutral, right?
 </span>
</p>
<p>
 <span data-rw-start="1332.96" data-rw-transcript-version="2">
 It will never care about your thing. It
 </span>
 <span data-rw-start="1334.799" data-rw-transcript-version="2">
 can't be made to care about your thing.
 </span>
 <span data-rw-start="1338.08" data-rw-transcript-version="2">
 Um, so, I think that's kind of where
 </span>
 <span data-rw-start="1340.559" data-rw-transcript-version="2">
 we're at.
 </span>
</p>
<p>
 <span data-rw-start="1343.2" data-rw-transcript-version="2">
 &gt;&gt; I, I just wanted to, I wasn't trying to
 </span>
 <span data-rw-start="1345.039" data-rw-transcript-version="2">
 say that the LLM was some kind of junior
 </span>
 <span data-rw-start="1346.88" data-rw-transcript-version="2">
 developer, just that it, you can get this
 </span>
 <span data-rw-start="1348.48" data-rw-transcript-version="2">
 ratchet effect.
 </span>
</p>
<p>
 <span data-rw-start="1349.52" data-rw-transcript-version="2">
 &gt;&gt; Oh, yeah. No, sorry.
 </span>
 <span data-rw-start="1351.52" data-rw-transcript-version="2">
 Yeah.
 </span>
</p>
<p>
 <span data-rw-start="1351.84" data-rw-transcript-version="2">
 &gt;&gt; To raise code quality, and that, that I
 </span>
 <span data-rw-start="1353.84" data-rw-transcript-version="2">
 haven't really had before. Some
 </span>
 <span data-rw-start="1355.76" data-rw-transcript-version="2">
 deterministic way to raise code quality.
 </span>
 <span data-rw-start="1358.32" data-rw-transcript-version="2">
 It's interesting what, what, what I love
 </span>
 <span data-rw-start="1359.84" data-rw-transcript-version="2">
 and someone, someone who I, I would love.
 </span>
</p>
<p>
 <span data-rw-start="1361.919" data-rw-transcript-version="2">
 To be able to cite her because I can't
 </span>
 <span data-rw-start="1363.039" data-rw-transcript-version="2">
 remember who it was that said it
 </span>
 <span data-rw-start="1363.919" data-rw-transcript-version="2">
 recently that the if you take the ven
 </span>
 <span data-rw-start="1366.159" data-rw-transcript-version="2">
 diagram of things that improve developer
 </span>
 <span data-rw-start="1368.08" data-rw-transcript-version="2">
 experience and things that improve agent
 </span>
 <span data-rw-start="1369.44" data-rw-transcript-version="2">
 experience, it's a circle, and I just
 </span>
 <span data-rw-start="1371.44" data-rw-transcript-version="2">
 thought that was a wonderful observation.
 </span>
 <span data-rw-start="1373.28" data-rw-transcript-version="2">
 Is we’re now investing in things like
 </span>
 <span data-rw-start="1375.36" data-rw-transcript-version="2">
 static analysis, things like tooling,
 </span>
 <span data-rw-start="1377.039" data-rw-transcript-version="2">
 things like whatever else, documenting
 </span>
 <span data-rw-start="1378.48" data-rw-transcript-version="2">
 stuff, writing down how we do things,
 </span>
 <span data-rw-start="1380.32" data-rw-transcript-version="2">
 being explicit about our ways of working,
 </span>
 <span data-rw-start="1382.08" data-rw-transcript-version="2">
 and our code style, and our um, for a
 </span>
 <span data-rw-start="1385.36" data-rw-transcript-version="2">
 machine.
 </span>
</p>
<p>
 <span data-rw-start="1386.96" data-rw-transcript-version="2">
 In a way that we’ve never, ever invested
 </span>
 <span data-rw-start="1389.36" data-rw-transcript-version="2">
 this much in the human beings around us.
 </span>
 <span data-rw-start="1391.44" data-rw-transcript-version="2">
 And what does that tell us about us?
 </span>
</p>
<p>
 <span data-rw-start="1395.2" data-rw-transcript-version="2">
 What?
 </span>
 <span data-rw-start="1399.12" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="1401.039" data-rw-transcript-version="2">
 yeah, what I’m missing a little bit here,
 </span>
 <span data-rw-start="1403.36" data-rw-transcript-version="2">
 in the discussion, is the uh, one of
 </span>
 <span data-rw-start="1405.919" data-rw-transcript-version="2">
 aspect of trust. We were talking
 </span>
 <span data-rw-start="1408.72" data-rw-transcript-version="2">
 about how do we deal with the machine,
 </span>
 <span data-rw-start="1410.559" data-rw-transcript-version="2">
 and so on and so on. But trust is not the
 </span>
 <span data-rw-start="1412.64" data-rw-transcript-version="2">
 problem of the machine, as you said.
 </span>
</p>
<p>
 <span data-rw-start="1414.559" data-rw-transcript-version="2">
 Is our problem. So, how do we get to a
 </span>
 <span data-rw-start="1418.72" data-rw-transcript-version="2">
 situation where we say, "Okay, we can
 </span>
 <span data-rw-start="1420.24" data-rw-transcript-version="2">
 trust it." Or can we say, "Okay, we we
 </span>
 <span data-rw-start="1421.919" data-rw-transcript-version="2">
 don't trust the the stuff that's there."
 </span>
 <span data-rw-start="1424.96" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="1426.48" data-rw-transcript-version="2">
 &gt;&gt; Well, I think Emily nailed it with this idea of ratchets. I think that
 </span>
 <span data-rw-start="1428" data-rw-transcript-version="2">
 is so critical, is, you know, you've got
 </span>
 <span data-rw-start="1432.88" data-rw-transcript-version="2">
 this thing and the elephant in the room
 </span>
 <span data-rw-start="1434.64" data-rw-transcript-version="2">
 about the elephant in the room is that
 </span>
 <span data-rw-start="1436.159" data-rw-transcript-version="2">
 it has a chronic memory problem, right?
 </span>
 <span data-rw-start="1438.799" data-rw-transcript-version="2">
 It will forget things you've told it. It
 </span>
 <span data-rw-start="1441.12" data-rw-transcript-version="2">
 will forget very important detailed
 </span>
 <span data-rw-start="1442.88" data-rw-transcript-version="2">
 instructions you've given it while
 </span>
 <span data-rw-start="1444.48" data-rw-transcript-version="2">
 you're talking to it. It's called
 </span>
 <span data-rw-start="1446.32" data-rw-transcript-version="2">
 compaction. It's baked in. You can't not
 </span>
 <span data-rw-start="1448.24" data-rw-transcript-version="2">
 have this, right? And if you know what
 </span>
 <span data-rw-start="1450.559" data-rw-transcript-version="2">
 you're doing, you can decide when it's
 </span>
 <span data-rw-start="1452.4" data-rw-transcript-version="2">
 going to forget and when you're going to
 </span>
 <span data-rw-start="1453.679" data-rw-transcript-version="2">
 have to summarize everything it's ever
 </span>
 <span data-rw-start="1454.96" data-rw-transcript-version="2">
 heard. Or sometimes it will just do it.
 </span>
 <span data-rw-start="1457.44" data-rw-transcript-version="2">
 And there's that wonderful
 </span>
 <span data-rw-start="1458.88" data-rw-transcript-version="2">
 slash heartbreaking story of one senior
 </span>
 <span data-rw-start="1461.52" data-rw-transcript-version="2">
 AI engineer like a director of
 </span>
 <span data-rw-start="1463.279" data-rw-transcript-version="2">
 engineering.
 </span>
</p>
<p>
 <span data-rw-start="1464.799" data-rw-transcript-version="2">
 Um, who was using like a Claudebot or
 </span>
 <span data-rw-start="1466.799" data-rw-transcript-version="2">
 whatever, uh, to manage her
 </span>
 <span data-rw-start="1470.88" data-rw-transcript-version="2">
 email. And she said, "Right, the one
 </span>
 <span data-rw-start="1472.799" data-rw-transcript-version="2">
 thing you must never ever do is delete
 </span>
 <span data-rw-start="1474.32" data-rw-transcript-version="2">
 email." And it went, "Okay." And then it
 </span>
 <span data-rw-start="1476.4" data-rw-transcript-version="2">
 deleted her entire email archive.
 </span>
 <span data-rw-start="1479.007" data-rw-transcript-version="2">
 [Laughter]
 </span>
 <span data-rw-start="1479.76" data-rw-transcript-version="2">
 She, I told you not to. Yeah. Oh, did
 </span>
 <span data-rw-start="1481.76" data-rw-transcript-version="2">
 you? Oh, there's a thing. And she said
 </span>
 <span data-rw-start="1485.6" data-rw-transcript-version="2">
 she was basically she ended up doing
 </span>
 <span data-rw-start="1486.96" data-rw-transcript-version="2">
 this kind of walking on eggshells with
 </span>
 <span data-rw-start="1488.559" data-rw-transcript-version="2">
 the one machine she still had that
 </span>
 <span data-rw-start="1490.559" data-rw-transcript-version="2">
 had her email on it to try to get it
 </span>
 <span data-rw-start="1492.88" data-rw-transcript-version="2">
 back. And, like, you know, this isn't
 </span>
 <span data-rw-start="1495.52" data-rw-transcript-version="2">
 again, this isn't malice. This is
 </span>
 <span data-rw-start="1497.039" data-rw-transcript-version="2">
 pathological incompetence.
 </span>
</p>
<p>
 <span data-rw-start="1499.76" data-rw-transcript-version="2">
 How? And so, given that that is
 </span>
 <span data-rw-start="1502.32" data-rw-transcript-version="2">
 literally baked in, we can't, that's part
 </span>
 <span data-rw-start="1504" data-rw-transcript-version="2">
 of the design. Hallucinating is part of
 </span>
 <span data-rw-start="1506" data-rw-transcript-version="2">
 the design. Compression is part of the
 </span>
 <span data-rw-start="1507.52" data-rw-transcript-version="2">
 design. We have to build these checks
 </span>
 <span data-rw-start="1509.919" data-rw-transcript-version="2">
 and balances and harnesses to manage. If
 </span>
 <span data-rw-start="1512.24" data-rw-transcript-version="2">
 that's the tool we're going to use.
 </span>
 <span data-rw-start="1517.44" data-rw-transcript-version="2">
 But, it's again about risk assessment and
 </span>
 <span data-rw-start="1519.039" data-rw-transcript-version="2">
 the use case, right? Like in this case,
 </span>
 <span data-rw-start="1520.799" data-rw-transcript-version="2">
 Of course, I would not give an agent
 </span>
 <span data-rw-start="1523.36" data-rw-transcript-version="2">
 access to my email, [laughter] right?
 </span>
</p>
<p>
 <span data-rw-start="1525.52" data-rw-transcript-version="2">
 Like especially not write access or
 </span>
 <span data-rw-start="1527.679" data-rw-transcript-version="2">
 delete access or any of those things,
 </span>
 <span data-rw-start="1529.44" data-rw-transcript-version="2">
 right?
 </span>
</p>
<p>
 <span data-rw-start="1530.48" data-rw-transcript-version="2">
 &gt;&gt; Yeah. So, and uh so and in the case of
 </span>
 <span data-rw-start="1533.039" data-rw-transcript-version="2">
 like coding like um like I agree with
 </span>
 <span data-rw-start="1535.919" data-rw-transcript-version="2">
 everything you said like it doesn't care
 </span>
 <span data-rw-start="1537.279" data-rw-transcript-version="2">
 about the code and all of that but if it
 </span>
 <span data-rw-start="1539.76" data-rw-transcript-version="2">
 does the thing that I need do I care
 </span>
 <span data-rw-start="1541.6" data-rw-transcript-version="2">
 that it cares and that it's a machine
 </span>
 <span data-rw-start="1543.44" data-rw-transcript-version="2">
 and not you know like I also don't think
 </span>
 <span data-rw-start="1545.36" data-rw-transcript-version="2">
 we should anthropomorphize it and it's
 </span>
 <span data-rw-start="1547.679" data-rw-transcript-version="2">
 like easily happening because the large
 </span>
 <span data-rw-start="1549.6" data-rw-transcript-version="2">
 language models are trained on our
 </span>
 <span data-rw-start="1551.6" data-rw-transcript-version="2">
 language. So that's why it's also like
 </span>
 <span data-rw-start="1553.76" data-rw-transcript-version="2">
 all the things that are good for us in
 </span>
 <span data-rw-start="1555.279" data-rw-transcript-version="2">
 the code are good for the model because
 </span>
 <span data-rw-start="1556.799" data-rw-transcript-version="2">
 it's trained on how we've been writing
 </span>
 <span data-rw-start="1558.559" data-rw-transcript-version="2">
 code, right? Um
 </span>
 <span data-rw-start="1561.12" data-rw-transcript-version="2">
 but yeah, I mean does it matter why that
 </span>
 <span data-rw-start="1563.6" data-rw-transcript-version="2">
 is the case if it gives me something
 </span>
 <span data-rw-start="1565.039" data-rw-transcript-version="2">
 useful, right? And the risk assessment
 </span>
 <span data-rw-start="1567.52" data-rw-transcript-version="2">
 part that's the like what's the use case
 </span>
 <span data-rw-start="1569.84" data-rw-transcript-version="2">
 like how much footprint do I give it
 </span>
 <span data-rw-start="1572.64" data-rw-transcript-version="2">
 Like impact, what it—what it can access
 </span>
 <span data-rw-start="1574.64" data-rw-transcript-version="2">
 and stuff like that. That's kind of
 </span>
 <span data-rw-start="1576.08" data-rw-transcript-version="2">
 like then how you wield the tool, right?
 </span>
</p>
<p>
 <span data-rw-start="1581.039" data-rw-transcript-version="2">
 Okay. Well, um, talking about learning
 </span>
 <span data-rw-start="1584.32" data-rw-transcript-version="2">
 and skills and so on. Uh, coming to one
 </span>
 <span data-rw-start="1586.96" data-rw-transcript-version="2">
 of the questions that always come up, uh,
 </span>
 <span data-rw-start="1589.36" data-rw-transcript-version="2">
 again, after reviewing uh, the code is, the
 </span>
 <span data-rw-start="1593.679" data-rw-transcript-version="2">
 Yeah. And, and Kevin talked about it, uh,
 </span>
 <span data-rw-start="1596.4" data-rw-transcript-version="2">
 today too. Um, are we going to get more
 </span>
 <span data-rw-start="1600.24" data-rw-transcript-version="2">
 stupid because, uh, we are using those AI
 </span>
 <span data-rw-start="1603.039" data-rw-transcript-version="2">
 engines? Is it like, uh, GPS, uh, that, uh,
 </span>
 <span data-rw-start="1608.96" data-rw-transcript-version="2">
 lets me not being able to navigate, uh, a
 </span>
 <span data-rw-start="1613.039" data-rw-transcript-version="2">
 city without, uh, looking at a machine. Um
 </span>
 <span data-rw-start="1616.72" data-rw-transcript-version="2">
 And, uh, yeah, of course, also connected to
 </span>
 <span data-rw-start="1619.36" data-rw-transcript-version="2">
 the question: what do we do with the new
 </span>
 <span data-rw-start="1620.96" data-rw-transcript-version="2">
 developers that might take the easy way
 </span>
 <span data-rw-start="1624.08" data-rw-transcript-version="2">
 and, uh, just, um, I mean, then you just said
 </span>
 <span data-rw-start="1629.679" data-rw-transcript-version="2">
 you had, um, developers that are always
 </span>
 <span data-rw-start="1632.72" data-rw-transcript-version="2">
 eager to learn, but what if they are not
 </span>
 <span data-rw-start="1635.6" data-rw-transcript-version="2">
 eager to learn? What if they are just
 </span>
 <span data-rw-start="1637.12" data-rw-transcript-version="2">
 using it, so you
 </span>
 <span data-rw-start="1639.2" data-rw-transcript-version="2">
 &gt;&gt; yeah, I think I recently had an
 </span>
 <span data-rw-start="1640.559" data-rw-transcript-version="2">
 experience with one of our students, and
 </span>
 <span data-rw-start="1642.24" data-rw-transcript-version="2">
 he tried out some new technology, and it
 </span>
 <span data-rw-start="1644.799" data-rw-transcript-version="2">
 looked good. It was working, and at one
 </span>
 <span data-rw-start="1648" data-rw-transcript-version="2">
 Point it stopped working and I asked him,
 </span>
 <span data-rw-start="1650.799" data-rw-transcript-version="2">
 okay, what did you do? I wasn’t,
 </span>
</p>
<p>
 <span data-rw-start="1653.44" data-rw-transcript-version="2">
 I didn’t know anything about it as well, but I
 </span>
 <span data-rw-start="1656.24" data-rw-transcript-version="2">
 realized he didn’t even have a clue how
 </span>
 <span data-rw-start="1658.48" data-rw-transcript-version="2">
 to start debugging this thing. He doesn’t
 </span>
 <span data-rw-start="1661.52" data-rw-transcript-version="2">
 know anything about it, even on something
 </span>
 <span data-rw-start="1663.84" data-rw-transcript-version="2">
 like system outprint line, right? So, the
 </span>
 <span data-rw-start="1665.76" data-rw-transcript-version="2">
 very most basic thing that I would
 </span>
 <span data-rw-start="1667.279" data-rw-transcript-version="2">
 expect works in every technology, some he
 </span>
 <span data-rw-start="1669.76" data-rw-transcript-version="2">
 was just like I tried again and again,
 </span>
 <span data-rw-start="1672.48" data-rw-transcript-version="2">
 and maybe he would ask again and again,
 </span>
 <span data-rw-start="1674.72" data-rw-transcript-version="2">
 um, his chat bot, but nothing happened, and
 </span>
 <span data-rw-start="1677.36" data-rw-transcript-version="2">
 I’m thinking this is something,
 </span>
 <span data-rw-start="1681.12" data-rw-transcript-version="2">
 maybe we need to find a way to teach
 </span>
 <span data-rw-start="1682.88" data-rw-transcript-version="2">
 people that explicitly again, but they
 </span>
 <span data-rw-start="1685.6" data-rw-transcript-version="2">
 will not learn it by themselves, like we
 </span>
 <span data-rw-start="1687.919" data-rw-transcript-version="2">
 were like with compiler errors. We
 </span>
 <span data-rw-start="1689.84" data-rw-transcript-version="2">
 started, and we were like, okay, how, where
 </span>
 <span data-rw-start="1691.679" data-rw-transcript-version="2">
 can I start and go forward, and they
 </span>
 <span data-rw-start="1694.64" data-rw-transcript-version="2">
 don’t have the problem now, because they
 </span>
 <span data-rw-start="1696" data-rw-transcript-version="2">
 just ask, so how can I fix this compile
 </span>
 <span data-rw-start="1697.84" data-rw-transcript-version="2">
 error? And they copy-paste, and I think it
 </span>
 <span data-rw-start="1699.84" data-rw-transcript-version="2">
 was a similar story when stack
 </span>
 <span data-rw-start="1701.44" data-rw-transcript-version="2">
 overflow comes into play, right? So,
 </span>
 <span data-rw-start="1703.919" data-rw-transcript-version="2">
 you could start copying from Stack overflow.
 </span>
</p>
<p>
 <span data-rw-start="1706.399" data-rw-transcript-version="2">
 But you still realize that it's not
 </span>
 <span data-rw-start="1707.919" data-rw-transcript-version="2">
 working forever. So, there is something
 </span>
 <span data-rw-start="1710.72" data-rw-transcript-version="2">
 changing for them, and I think they
 </span>
 <span data-rw-start="1712.799" data-rw-transcript-version="2">
 will need to learn how to debug and how
 </span>
 <span data-rw-start="1715.279" data-rw-transcript-version="2">
 to analyze a problem when the machine
 </span>
 <span data-rw-start="1717.679" data-rw-transcript-version="2">
 cannot help any longer.
 </span>
</p>
<p>
 <span data-rw-start="1720" data-rw-transcript-version="2">
 &gt;&gt; The short answer is yes.
 </span>
 <span data-rw-start="1723.2" data-rw-transcript-version="2">
 I forgot my question.
 </span>
</p>
<p>
 <span data-rw-start="1724.64" data-rw-transcript-version="2">
 &gt;&gt; Okay. So, your question was will people
 </span>
 <span data-rw-start="1726.72" data-rw-transcript-version="2">
 still develop these skills or will they
 </span>
 <span data-rw-start="1729.84" data-rw-transcript-version="2">
 forget them? And the short answer is
 </span>
 <span data-rw-start="1731.44" data-rw-transcript-version="2">
 they will forget them. And I, I hope not.
 </span>
</p>
<p>
 <span data-rw-start="1736.08" data-rw-transcript-version="2">
 But as I said, being a teacher for
 </span>
 <span data-rw-start="1738.159" data-rw-transcript-version="2">
 teachers in computer science, and also
 </span>
 <span data-rw-start="1740.64" data-rw-transcript-version="2">
 talking to other people who are teachers
 </span>
 <span data-rw-start="1743.36" data-rw-transcript-version="2">
 not just at the university but at
 </span>
 <span data-rw-start="1745.52" data-rw-transcript-version="2">
 different kinds of uh, there's a—at least
 </span>
 <span data-rw-start="1749.039" data-rw-transcript-version="2">
 in Denmark, there are different ways of
 </span>
 <span data-rw-start="1750.799" data-rw-transcript-version="2">
 being educated in IT, and there are some
 </span>
 <span data-rw-start="1752.72" data-rw-transcript-version="2">
 schools where you are learning how to
 </span>
 <span data-rw-start="1754.399" data-rw-transcript-version="2">
 program based on a specification, and
 </span>
 <span data-rw-start="1756.72" data-rw-transcript-version="2">
 there are some schools where you learn
 </span>
 <span data-rw-start="1757.84" data-rw-transcript-version="2">
 to create the specification and things
 </span>
 <span data-rw-start="1759.76" data-rw-transcript-version="2">
 like that. And we're really talking about
 </span>
 <span data-rw-start="1762.32" data-rw-transcript-version="2">
 I don’t know how to translate this to
 </span>
 <span data-rw-start="1764.159" data-rw-transcript-version="2">
 English, but uh, in Danish, we say fo
 </span>
 <span data-rw-start="1768.399" data-rw-transcript-version="2">
 and that means content sorrow or
 </span>
 <span data-rw-start="1771.279" data-rw-transcript-version="2">
 something like that. That some of us are
 </span>
 <span data-rw-start="1773.6" data-rw-transcript-version="2">
 really, really sad that some of our
 </span>
 <span data-rw-start="1776.08" data-rw-transcript-version="2">
 skills, that we've worked with for so
 </span>
</p>
<p>
 <span data-rw-start="1777.76" data-rw-transcript-version="2">
 many years, might be forgotten. And if we
 </span>
 <span data-rw-start="1781.6" data-rw-transcript-version="2">
 think back to other things that have
 </span>
 <span data-rw-start="1784.32" data-rw-transcript-version="2">
 been taken over by machines, if we call
 </span>
 <span data-rw-start="1786.96" data-rw-transcript-version="2">
 this a machine, they have been very
 </span>
 <span data-rw-start="1789.279" data-rw-transcript-version="2">
 sad. And at the university that I am at,
 </span>
 <span data-rw-start="1792.24" data-rw-transcript-version="2">
 we are working in two different
 </span>
 <span data-rw-start="1794.08" data-rw-transcript-version="2">
 directions at the same time, and I don't
 </span>
 <span data-rw-start="1795.919" data-rw-transcript-version="2">
 know where we'll go. One direction is
 </span>
 <span data-rw-start="1799.52" data-rw-transcript-version="2">
 we will make sure that when they hand in
 </span>
 <span data-rw-start="1801.84" data-rw-transcript-version="2">
 something, they have to hand it in orally,
 </span>
 <span data-rw-start="1804.48" data-rw-transcript-version="2">
 so they have to explain what they've
 </span>
 <span data-rw-start="1806.159" data-rw-transcript-version="2">
 done. And when they go to the exam, they
 </span>
 <span data-rw-start="1808.48" data-rw-transcript-version="2">
 do it with paper and pencil, and they
 </span>
 <span data-rw-start="1810.48" data-rw-transcript-version="2">
 cannot use the computer. So that's one
 </span>
 <span data-rw-start="1812.48" data-rw-transcript-version="2">
 direction. But we have another direction,
 </span>
 <span data-rw-start="1815.039" data-rw-transcript-version="2">
 which is debating: do we even need to
 </span>
 <span data-rw-start="1817.44" data-rw-transcript-version="2">
 teach them these skills?
 </span>
</p>
<p>
 <span data-rw-start="1819.919" data-rw-transcript-version="2">
 And if we don't, then the whole education
 </span>
 <span data-rw-start="1822.64" data-rw-transcript-version="2">
 is going to change tremendously, and what
 </span>
 <span data-rw-start="1825.52" data-rw-transcript-version="2">
 we're going to teach them is something.
 </span>
</p>
<p>
 <span data-rw-start="1826.96" data-rw-transcript-version="2">
 Different than what our wonderful
 </span>
 <span data-rw-start="1829.039" data-rw-transcript-version="2">
 professors have been talking about for
 </span>
 <span data-rw-start="1830.559" data-rw-transcript-version="2">
 30 years on stage, and that's really
 </span>
 <span data-rw-start="1833.12" data-rw-transcript-version="2">
 scary. I don't know what the answer
 </span>
 <span data-rw-start="1834.96" data-rw-transcript-version="2">
 is, but it's like two out of three of my
 </span>
 <span data-rw-start="1838.159" data-rw-transcript-version="2">
 children are either computer scientists
 </span>
 <span data-rw-start="1841.039" data-rw-transcript-version="2">
 or becoming.
 </span>
</p>
<p>
 <span data-rw-start="1842.48" data-rw-transcript-version="2">
 So, it's a very personal question
 </span>
 <span data-rw-start="1844.799" data-rw-transcript-version="2">
 &gt;&gt;
 </span>
 <span data-rw-start="1848.48" data-rw-transcript-version="2">
 &gt; Yeah.
 </span>
 <span data-rw-start="1849.36" data-rw-transcript-version="2">
 &gt; Bad parenting. We're both computer
 </span>
 <span data-rw-start="1850.88" data-rw-transcript-version="2">
 scientists. Yeah. Sorry.
 </span>
</p>
<p>
 <span data-rw-start="1853.84" data-rw-transcript-version="2">
 I want to speak directly to the
 </span>
 <span data-rw-start="1855.279" data-rw-transcript-version="2">
 question. Uh, are we going to get more
 </span>
 <span data-rw-start="1857.12" data-rw-transcript-version="2">
 stupid? I think it only matters losing a
 </span>
 <span data-rw-start="1861.2" data-rw-transcript-version="2">
 skill if it's a skill you'll ever need again.
 </span>
</p>
<p>
 <span data-rw-start="1863.36" data-rw-transcript-version="2">
 Right. And if we are, and
 </span>
 <span data-rw-start="1866.88" data-rw-transcript-version="2">
 I think we are exactly to your point, we
 </span>
 <span data-rw-start="1869.679" data-rw-transcript-version="2">
 are at risk already of losing skills we
 </span>
 <span data-rw-start="1872.72" data-rw-transcript-version="2">
 are still going to need. That's a
 </span>
 <span data-rw-start="1874.799" data-rw-transcript-version="2">
 problem. That's a material problem. Uh,
 </span>
 <span data-rw-start="1877.6" data-rw-transcript-version="2">
 I've been in software for 35 years. I
 </span>
 <span data-rw-start="1880.799" data-rw-transcript-version="2">
 suspect as long or longer than a
 </span>
 <span data-rw-start="1882.72" data-rw-transcript-version="2">
 lot of people in this room, but I'm
 </span>
 <span data-rw-start="1884.08" data-rw-transcript-version="2">
 still pretty, you know, I'm still pretty
 </span>
 <span data-rw-start="1885.44" data-rw-transcript-version="2">
 New. It's a quite an old field now. Um
 </span>
 <span data-rw-start="1888.72" data-rw-transcript-version="2">
 So, who here is any good at punching uh
 </span>
 <span data-rw-start="1892.48" data-rw-transcript-version="2">
 cards?
 </span>
</p>
<p>
 <span data-rw-start="1894.64" data-rw-transcript-version="2">
 Who has a card hole punch? Right,
 </span>
 <span data-rw-start="1897.44" data-rw-transcript-version="2">
 there's a skill, and it used to be an
 </span>
 <span data-rw-start="1899.12" data-rw-transcript-version="2">
 important skill. How fast you could
 </span>
 <span data-rw-start="1900.48" data-rw-transcript-version="2">
 punch holes in a card was how fast you
 </span>
 <span data-rw-start="1902.399" data-rw-transcript-version="2">
 could literally, how fast you could
 </span>
 <span data-rw-start="1903.519" data-rw-transcript-version="2">
 program, right? Uh, what about changing a
 </span>
 <span data-rw-start="1906.08" data-rw-transcript-version="2">
 paper in a teletype?
 </span>
</p>
<p>
 <span data-rw-start="1908.08" data-rw-transcript-version="2">
 No. You know the TTY, the letters TTY
 </span>
 <span data-rw-start="1910.24" data-rw-transcript-version="2">
 when you have a TTY, that's a thing
 </span>
 <span data-rw-start="1912.08" data-rw-transcript-version="2">
 that's a physical, mechanical thing. Uh
 </span>
 <span data-rw-start="1914.32" data-rw-transcript-version="2">
 Who can program in machine code? No, not
 </span>
 <span data-rw-start="1917.84" data-rw-transcript-version="2">
 assembler machine code.
 </span>
 <span data-rw-start="1920.88" data-rw-transcript-version="2">
 Ah, gotcha. Right. So again, some of you
 </span>
 <span data-rw-start="1924.48" data-rw-transcript-version="2">
 will know assembler, and some of you need
 </span>
 <span data-rw-start="1925.76" data-rw-transcript-version="2">
 to know assembler. Most of us don't.
 </span>
 <span data-rw-start="1927.519" data-rw-transcript-version="2">
 Practically no one will know how to
 </span>
 <span data-rw-start="1928.88" data-rw-transcript-version="2">
 program in machine code. So, there are
 </span>
 <span data-rw-start="1930.96" data-rw-transcript-version="2">
 skills where, as the technology has
 </span>
 <span data-rw-start="1934" data-rw-transcript-version="2">
 improved, and again, um, Tiono, founder, one
 </span>
 <span data-rw-start="1938.08" data-rw-transcript-version="2">
 of the founders of the Toyota production
 </span>
 <span data-rw-start="1939.6" data-rw-transcript-version="2">
 system, has this wonderful term he
 </span>
 <span data-rw-start="1942.559" data-rw-transcript-version="2">
 calls it autonom.
 </span>
</p>
<p>
 <span data-rw-start="1945.36" data-rw-transcript-version="2">
 With a human element, right? And for me,
 </span>
 <span data-rw-start="1948.559" data-rw-transcript-version="2">
 any technology advance, the ones that
 </span>
 <span data-rw-start="1951.36" data-rw-transcript-version="2">
 win are the ones that allow humans to
 </span>
 <span data-rw-start="1954.08" data-rw-transcript-version="2">
 do stuff better, to make it easier for
 </span>
 <span data-rw-start="1956.799" data-rw-transcript-version="2">
 them to do things, not to replace them.
 </span>
 <span data-rw-start="1959.6" data-rw-transcript-version="2">
 And if you look at the most successful
 </span>
 <span data-rw-start="1961.12" data-rw-transcript-version="2">
 technologies in history, they allow us
 </span>
 <span data-rw-start="1962.72" data-rw-transcript-version="2">
 to do stuff, whatever that stuff is,
 </span>
 <span data-rw-start="1964.64" data-rw-transcript-version="2">
 medicine, research, science,
 </span>
 <span data-rw-start="1966.399" data-rw-transcript-version="2">
 climate, whatever it is, right? Better
 </span>
 <span data-rw-start="1969.2" data-rw-transcript-version="2">
 Um, sometimes not entirely better, right?
 </span>
</p>
<p>
 <span data-rw-start="1971.36" data-rw-transcript-version="2">
 But by and large, they augment
 </span>
 <span data-rw-start="1972.88" data-rw-transcript-version="2">
 humans. Yeah.
 </span>
 <span data-rw-start="1975.12" data-rw-transcript-version="2">
 So if we're losing skills, where we still
 </span>
 <span data-rw-start="1978.64" data-rw-transcript-version="2">
 where we're likely to still need them,
 </span>
 <span data-rw-start="1980.32" data-rw-transcript-version="2">
 and you know, we are in a world of
 </span>
 <span data-rw-start="1982.88" data-rw-transcript-version="2">
 cobalt, right? Cobalt is still one of
 </span>
 <span data-rw-start="1985.44" data-rw-transcript-version="2">
 the most prevalent languages. Whatever
 </span>
 <span data-rw-start="1987.36" data-rw-transcript-version="2">
 code is out there has an enormously long
 </span>
 <span data-rw-start="1989.6" data-rw-transcript-version="2">
 tail ahead of it. And so, the ability to
 </span>
 <span data-rw-start="1993.679" data-rw-transcript-version="2">
 go in, manipulate code with your hands,
 </span>
 <span data-rw-start="1996.64" data-rw-transcript-version="2">
 that's not going away in my lifetime,
 </span>
 <span data-rw-start="1998.64" data-rw-transcript-version="2">
 probably in the lifetime of anyone in
 </span>
 <span data-rw-start="1999.919" data-rw-transcript-version="2">
 this room. And if we allow those skills
 </span>
 <span data-rw-start="2002.24" data-rw-transcript-version="2">
 to atrophy, right? We're in trouble.
 </span>
</p>
<p>
 <span data-rw-start="2004.48" data-rw-transcript-version="2">
 Other thing, and then I'm going to shut
 </span>
 <span data-rw-start="2005.36" data-rw-transcript-version="2">
 up. One other thing I think is really
 </span>
 <span data-rw-start="2006.799" data-rw-transcript-version="2">
 key, and I'm really excited about this,
 </span>
 <span data-rw-start="2008.48" data-rw-transcript-version="2">
 and I'm looking to know particularly, and
 </span>
 <span data-rw-start="2011.519" data-rw-transcript-version="2">
 Emily, who are the people in the world
 </span>
 <span data-rw-start="2013.519" data-rw-transcript-version="2">
 who are bringing up the people in the
 </span>
 <span data-rw-start="2014.96" data-rw-transcript-version="2">
 world? Is the word native?
 </span>
 <span data-rw-start="2020" data-rw-transcript-version="2">
 So, my, I've got
 </span>
 <span data-rw-start="2022.799" data-rw-transcript-version="2">
 a three-year-old son. He is mobile
 </span>
 <span data-rw-start="2025.279" data-rw-transcript-version="2">
 native. He's never lived in a world
 </span>
 <span data-rw-start="2027.279" data-rw-transcript-version="2">
 without mobile technology. He got
 </span>
 <span data-rw-start="2029.039" data-rw-transcript-version="2">
 disappointed when he was two that he
 </span>
 <span data-rw-start="2030.64" data-rw-transcript-version="2">
 couldn't do that on the TV screen, and it
 </span>
 <span data-rw-start="2032.559" data-rw-transcript-version="2">
 would do stuff right. He, because it's
 </span>
 <span data-rw-start="2034.24" data-rw-transcript-version="2">
 just like his a little screen, but it
 </span>
 <span data-rw-start="2036.72" data-rw-transcript-version="2">
 just doesn't, doesn't work. Yeah. We're
 </span>
 <span data-rw-start="2039.2" data-rw-transcript-version="2">
 all old, right? All of us are old. You
 </span>
 <span data-rw-start="2040.64" data-rw-transcript-version="2">
 know, I'm really old, but like, all of us
 </span>
 <span data-rw-start="2043.679" data-rw-transcript-version="2">
 are old. Yeah. Um, the kids coming
 </span>
 <span data-rw-start="2046.32" data-rw-transcript-version="2">
 through now will never have been in a
 </span>
 <span data-rw-start="2049.359" data-rw-transcript-version="2">
 world that didn't have AI. They will be
 </span>
 <span data-rw-start="2051.76" data-rw-transcript-version="2">
 AI native. They will be Gen AI native.
 </span>
 <span data-rw-start="2053.359" data-rw-transcript-version="2">
 They will think about problems
 </span>
 <span data-rw-start="2056.399" data-rw-transcript-version="2">
 differently than I can. I can probably
 </span>
 <span data-rw-start="2057.679" data-rw-transcript-version="2">
 learn to do it, but I'll keep falling
 </span>
 <span data-rw-start="2059.679" data-rw-transcript-version="2">
 back on my old artist and programming.
 </span>
</p>
<p>
 <span data-rw-start="2060.32" data-rw-transcript-version="2">
 Habits. Yeah. And that's exciting, right? So, let's bring those junior
 </span>
 <span data-rw-start="2063.2" data-rw-transcript-version="2">
 engineers. Let's give them the space to
 </span>
 <span data-rw-start="2064.96" data-rw-transcript-version="2">
 learn this new world and make sure they
 </span>
 <span data-rw-start="2066.879" data-rw-transcript-version="2">
 can still drive with a stick shift.
 </span>
</p>
<p>
 <span data-rw-start="2071.839" data-rw-transcript-version="2">
 &gt;&gt; I disagree on two points.
 </span>
 <span data-rw-start="2073.839" data-rw-transcript-version="2">
 &gt;&gt; Nice.
 </span>
 <span data-rw-start="2074.56" data-rw-transcript-version="2">
 &gt;&gt; I’ll make it short. One is I don’t think
 </span>
 <span data-rw-start="2077.119" data-rw-transcript-version="2">
 there’ll be a long tale of the programs
 </span>
 <span data-rw-start="2078.8" data-rw-transcript-version="2">
 that we do right now. It’s so easy to go
 </span>
 <span data-rw-start="2082" data-rw-transcript-version="2">
 into a really old program and find the
 </span>
 <span data-rw-start="2083.919" data-rw-transcript-version="2">
 smallest thing. So, the truck number is
 </span>
 <span data-rw-start="2086.48" data-rw-transcript-version="2">
 dead as a concept as well. I don’t think
 </span>
 <span data-rw-start="2088.879" data-rw-transcript-version="2">
 the code will get old, but that’s just I
 </span>
 <span data-rw-start="2091.679" data-rw-transcript-version="2">
 mean. What do I know about the future?
 </span>
</p>
<p>
 <span data-rw-start="2093.839" data-rw-transcript-version="2">
 And the other thing is, if we look at the
 </span>
 <span data-rw-start="2095.52" data-rw-transcript-version="2">
 young people who are mobile native,
 </span>
 <span data-rw-start="2097.599" data-rw-transcript-version="2">
 they're still falling into a lot of the
 </span>
 <span data-rw-start="2099.119" data-rw-transcript-version="2">
 traps that are because of the mobile.
 </span>
 <span data-rw-start="2101.119" data-rw-transcript-version="2">
 They’re still falling into the sexual
 </span>
 <span data-rw-start="2102.96" data-rw-transcript-version="2">
 predators. They’re still falling into, um,
 </span>
 <span data-rw-start="2105.839" data-rw-transcript-version="2">
 losing their parents' money. So, yes,
 </span>
 <span data-rw-start="2109.359" data-rw-transcript-version="2">
 they can use it, but not in a safe way.
 </span>
 <span data-rw-start="2111.839" data-rw-transcript-version="2">
 So, that’s what I wanted to say.
 </span>
</p>
<p>
 <span data-rw-start="2115.28" data-rw-transcript-version="2">
 &gt;&gt; Yeah. Yeah, I think one of the tricky
 </span>
 <span data-rw-start="2116.4" data-rw-transcript-version="2">
 Things is like when we draw like history
 </span>
 <span data-rw-start="2119.04" data-rw-transcript-version="2">
 from computer science and then the the
 </span>
 <span data-rw-start="2121.44" data-rw-transcript-version="2">
 assembler comparison and all all of
 </span>
 <span data-rw-start="2123.839" data-rw-transcript-version="2">
 that, right? Is that we've always gone
 </span>
 <span data-rw-start="2126.16" data-rw-transcript-version="2">
 like up in the abstraction level but
 </span>
 <span data-rw-start="2128" data-rw-transcript-version="2">
 like real abstraction in the sense of
 </span>
 <span data-rw-start="2129.839" data-rw-transcript-version="2">
 that we've had deterministic tools that
 </span>
 <span data-rw-start="2132.4" data-rw-transcript-version="2">
 add the technical details and translate
 </span>
 <span data-rw-start="2134.48" data-rw-transcript-version="2">
 from the new abstraction level to the
 </span>
 <span data-rw-start="2135.92" data-rw-transcript-version="2">
 next abstraction level. Right? But this
 </span>
 <span data-rw-start="2137.76" data-rw-transcript-version="2">
 is not the same thing like the natural
 </span>
 <span data-rw-start="2139.52" data-rw-transcript-version="2">
 language thing because we don't have
 </span>
 <span data-rw-start="2140.88" data-rw-transcript-version="2">
 like a compiler compiler that translates
 </span>
 <span data-rw-start="2143.92" data-rw-transcript-version="2">
 to the level down. Like I always say
 </span>
 <span data-rw-start="2145.68" data-rw-transcript-version="2">
 it's kind of like moving to the side
 </span>
</p>
<p>
 <span data-rw-start="2147.119" data-rw-transcript-version="2">
 because we can use LLMs on all of the
 </span>
 <span data-rw-start="2148.8" data-rw-transcript-version="2">
 abstraction levels. Like I recently
 </span>
 <span data-rw-start="2150.4" data-rw-transcript-version="2">
 talked to Uva Fredson about this and he
 </span>
 <span data-rw-start="2152.16" data-rw-transcript-version="2">
 said like yeah it's not a closed
 </span>
 <span data-rw-start="2153.68" data-rw-transcript-version="2">
 abstraction. It's not closed. So we
 </span>
 <span data-rw-start="2155.52" data-rw-transcript-version="2">
 cannot forget like what's under
 </span>
 <span data-rw-start="2158.16" data-rw-transcript-version="2">
 underneath. And that goes to what you
 </span>
 <span data-rw-start="2159.68" data-rw-transcript-version="2">
 were saying like we'll still have to to
 </span>
 <span data-rw-start="2162.56" data-rw-transcript-version="2">
 a certain extent actually edit or
 </span>
 <span data-rw-start="2164.079" data-rw-transcript-version="2">
 understand the existing code but we
 </span>
 <span data-rw-start="2166.16" data-rw-transcript-version="2">
 Don't have as much practice anymore for
 </span>
 <span data-rw-start="2168" data-rw-transcript-version="2">
 like what's potentially going wrong
 </span>
 <span data-rw-start="2170" data-rw-transcript-version="2">
 right, so how do you build up the
 </span>
 <span data-rw-start="2172.24" data-rw-transcript-version="2">
 the mental model, the in your head, the
 </span>
 <span data-rw-start="2175.2" data-rw-transcript-version="2">
 shortcuts, like to understand everything.
 </span>
</p>
<p>
 <span data-rw-start="2177.04" data-rw-transcript-version="2">
 I, uh, read this, um, article a few years
 </span>
 <span data-rw-start="2180.64" data-rw-transcript-version="2">
 ago on, like, uh, what do, what do
 </span>
 <span data-rw-start="2183.119" data-rw-transcript-version="2">
 programmers need to learn about learning.
 </span>
 <span data-rw-start="2185.44" data-rw-transcript-version="2">
 Um, and there was a thing there about how
 </span>
 <span data-rw-start="2187.359" data-rw-transcript-version="2">
 you learn those shortcuts, those abstract
 </span>
 <span data-rw-start="2189.44" data-rw-transcript-version="2">
 concepts, and maybe, yeah, I know not, he
 </span>
 <span data-rw-start="2191.359" data-rw-transcript-version="2">
 maybe knows about this better than me, by
 </span>
 <span data-rw-start="2193.68" data-rw-transcript-version="2">
 actually going into detail, abstraction, detail,
 </span>
 <span data-rw-start="2195.68" data-rw-transcript-version="2">
 abstraction, right? You write the syntax
 </span>
 <span data-rw-start="2197.52" data-rw-transcript-version="2">
 of a for loop, and then you do that a few
 </span>
 <span data-rw-start="2200" data-rw-transcript-version="2">
 times, and then you start understanding
 </span>
 <span data-rw-start="2201.44" data-rw-transcript-version="2">
 the concept of a for loop, and you have a
 </span>
 <span data-rw-start="2203.04" data-rw-transcript-version="2">
 shortcut in your head. But then, how do
 </span>
 <span data-rw-start="2204.64" data-rw-transcript-version="2">
 you learn those, like, highly abstract
 </span>
 <span data-rw-start="2206.8" data-rw-transcript-version="2">
 things if, like, everything's still
 </span>
 <span data-rw-start="2208.16" data-rw-transcript-version="2">
 running on code but we're not. Yeah. So
 </span>
 <span data-rw-start="2211.68" data-rw-transcript-version="2">
 I, don't know, it's not an answer to the
 </span>
 <span data-rw-start="2213.04" data-rw-transcript-version="2">
 question, what we do. But, and, um, maybe my
 </span>
 <span data-rw-start="2216.56" data-rw-transcript-version="2">
 last point, um, there's, like, um, arguably, I
 </span>
 <span data-rw-start="2221.68" data-rw-transcript-version="2">
 would say, like, clawed code itself, right?
 </span>
</p>
<p>
 <span data-rw-start="2223.68" data-rw-transcript-version="2">
 Now is a really good example of a piece
 </span>
 <span data-rw-start="2225.44" data-rw-transcript-version="2">
 of software that is being built entirely
 </span>
 <span data-rw-start="2227.44" data-rw-transcript-version="2">
 by people using agents and not typing
 </span>
 <span data-rw-start="2230" data-rw-transcript-version="2">
 code anymore, and it's a piece of
 </span>
 <span data-rw-start="2231.76" data-rw-transcript-version="2">
 software that has maybe had one incident
 </span>
 <span data-rw-start="2233.839" data-rw-transcript-version="2">
 over the past year that was quickly
 </span>
 <span data-rw-start="2235.68" data-rw-transcript-version="2">
 resolved, and it works really, really well.
 </span>
</p>
<p>
 <span data-rw-start="2237.839" data-rw-transcript-version="2">
 Right, like from what I understand, I
 </span>
 <span data-rw-start="2240.8" data-rw-transcript-version="2">
 think the people on the cloud code
 </span>
 <span data-rw-start="2242.4" data-rw-transcript-version="2">
 team are all really, really experienced
 </span>
 <span data-rw-start="2244.32" data-rw-transcript-version="2">
 developers, and I think that is currently
 </span>
 <span data-rw-start="2246.8" data-rw-transcript-version="2">
 covering up some of the, you know, what
 </span>
 <span data-rw-start="2249.68" data-rw-transcript-version="2">
 the situation will be like in maybe five
 </span>
 <span data-rw-start="2251.68" data-rw-transcript-version="2">
 to 10 years, right? The teams that are
 </span>
 <span data-rw-start="2253.76" data-rw-transcript-version="2">
 really successful with this at the
 </span>
 <span data-rw-start="2255.2" data-rw-transcript-version="2">
 moment are like really experienced
 </span>
 <span data-rw-start="2257.76" data-rw-transcript-version="2">
 and have all of these mental models in
 </span>
 <span data-rw-start="2259.28" data-rw-transcript-version="2">
 their head. And I also wonder, and there's
 </span>
 <span data-rw-start="2261.599" data-rw-transcript-version="2">
 a lot of technical descriptions when you
 </span>
 <span data-rw-start="2263.44" data-rw-transcript-version="2">
 prompt, right? It's not just the
 </span>
 <span data-rw-start="2264.72" data-rw-transcript-version="2">
 functional stuff, there's a lot of
 </span>
 <span data-rw-start="2266.72" data-rw-transcript-version="2">
 technical stuff. So yeah, I really wonder
 </span>
</p>
<p>
 <span data-rw-start="2268.24" data-rw-transcript-version="2">
 about what that will be like in a few
 </span>
 <span data-rw-start="2270.88" data-rw-transcript-version="2">
 years. Can I come in on this a little about, so
 </span>
 <span data-rw-start="2274.16" data-rw-transcript-version="2">
 how you
 </span>
 <span data-rw-start="2275.119" data-rw-transcript-version="2">
 &gt;&gt; engineering skills? I'm convinced that
 </span>
 <span data-rw-start="2277.119" data-rw-transcript-version="2">
 we still need engineering skills even
 </span>
 <span data-rw-start="2279.44" data-rw-transcript-version="2">
 when we're using an AI to write all the
 </span>
 <span data-rw-start="2281.359" data-rw-transcript-version="2">
 code. And the reliable way that I
 </span>
 <span data-rw-start="2284.96" data-rw-transcript-version="2">
 know to teach people engineering skills
 </span>
 <span data-rw-start="2286.8" data-rw-transcript-version="2">
 is having them build stuff and toy
 </span>
 <span data-rw-start="2290.24" data-rw-transcript-version="2">
 projects. And I'm looking at my
 </span>
 <span data-rw-start="2292.48" data-rw-transcript-version="2">
 daughter, she's like 17, 18, and she's
 </span>
 <span data-rw-start="2295.76" data-rw-transcript-version="2">
 building things with Arduinos and
 </span>
 <span data-rw-start="2298.32" data-rw-transcript-version="2">
 wires and 3D printing stuff, and she's
 </span>
 <span data-rw-start="2301.2" data-rw-transcript-version="2">
 learning engineering skills by doing it.
 </span>
</p>
<p>
 <span data-rw-start="2304.079" data-rw-transcript-version="2">
 And I think that those skills are
 </span>
 <span data-rw-start="2306.079" data-rw-transcript-version="2">
 transferable to the AI age, but I think
 </span>
 <span data-rw-start="2309.44" data-rw-transcript-version="2">
 that the way we know to teach those is
 </span>
 <span data-rw-start="2311.76" data-rw-transcript-version="2">
 not using the AI. So, that's the interesting part to me,
 </span>
 <span data-rw-start="2314.4" data-rw-transcript-version="2">
 is that I
 </span>
 <span data-rw-start="2316.88" data-rw-transcript-version="2">
 think students benefit a great deal from
 </span>
 <span data-rw-start="2319.04" data-rw-transcript-version="2">
 not using the AI in learning
 </span>
 <span data-rw-start="2322.16" data-rw-transcript-version="2">
 engineering, but at some point they need
 </span>
 <span data-rw-start="2323.52" data-rw-transcript-version="2">
 to learn the AI-specific skills. Um, and
 </span>
 <span data-rw-start="2326.24" data-rw-transcript-version="2">
 I'm not sure we really know what those
 </span>
 <span data-rw-start="2327.76" data-rw-transcript-version="2">
 are yet.
 </span>
</p>
<p>
 <span data-rw-start="2330.4" data-rw-transcript-version="2">
 &gt;&gt; Well, oh maybe you do.
 </span>
 <span data-rw-start="2332.56" data-rw-transcript-version="2">
 &gt;&gt; Maybe let me, uh, mix some opinion with a
 </span>
 <span data-rw-start="2336.32" data-rw-transcript-version="2">
 question about that. Sorry, I know
 </span>
 <span data-rw-start="2338.88" data-rw-transcript-version="2">
 &gt;&gt; Just talk over
 </span>
 <span data-rw-start="2341.76" data-rw-transcript-version="2">
 &gt;&gt; Um, but because uh, for that point isn't I
 </span>
 <span data-rw-start="2345.52" data-rw-transcript-version="2">
 mean, I think curiosity is always uh, the
 </span>
 <span data-rw-start="2348.8" data-rw-transcript-version="2">
 key to learn new things and uh, trying to
 </span>
 <span data-rw-start="2352.64" data-rw-transcript-version="2">
 wanting to understand something. So, the
 </span>
 <span data-rw-start="2354.56" data-rw-transcript-version="2">
 opposite of what you, Sylvia, described, uh,
 </span>
 <span data-rw-start="2357.119" data-rw-transcript-version="2">
 well, I got a solution but I don't
 </span>
 <span data-rw-start="2359.04" data-rw-transcript-version="2">
 know how it works, but however it works,
 </span>
 <span data-rw-start="2361.04" data-rw-transcript-version="2">
 that's just the opposite thing there.
 </span>
</p>
<p>
 <span data-rw-start="2364" data-rw-transcript-version="2">
 And, my experience, very, very personally, is
 </span>
 <span data-rw-start="2366.32" data-rw-transcript-version="2">
 that if you use the LLM stuff to really
 </span>
 <span data-rw-start="2370.88" data-rw-transcript-version="2">
 dig deep into what it is actually, what
 </span>
 <span data-rw-start="2373.28" data-rw-transcript-version="2">
 I'm seeing here, please explain that to
 </span>
 <span data-rw-start="2375.359" data-rw-transcript-version="2">
 me more and more and more, like you would
 </span>
 <span data-rw-start="2377.68" data-rw-transcript-version="2">
 maybe look into whatever, um, dictionary or something, to understand
 </span>
 <span data-rw-start="2381.68" data-rw-transcript-version="2">
 the word. Then, you can even learn more, uh,
 </span>
 <span data-rw-start="2383.119" data-rw-transcript-version="2">
 if you go this way. Sorry, was that
 </span>
 <span data-rw-start="2390.16" data-rw-transcript-version="2">
 something you want?
 </span>
</p>
<p>
 <span data-rw-start="2392.48" data-rw-transcript-version="2">
 &gt;&gt; Yeah. Yeah. So, that, yes, the LLM can
 </span>
 <span data-rw-start="2396.32" data-rw-transcript-version="2">
 help you to understand a topic and, and
 </span>
 <span data-rw-start="2398.48" data-rw-transcript-version="2">
 help you to research it, and, that's
 </span>
 <span data-rw-start="2401.119" data-rw-transcript-version="2">
 that's useful. You need to understand
 </span>
 <span data-rw-start="2403.92" data-rw-transcript-version="2">
 and, knowledge, but a lot of engineering
 </span>
 <span data-rw-start="2406.079" data-rw-transcript-version="2">
 is practical. It's doing it, and
 </span>
 <span data-rw-start="2408.48" data-rw-transcript-version="2">
 It's filling around with wires, and why
 </span>
 <span data-rw-start="2410.48" data-rw-transcript-version="2">
 does this break, and how do I debug that?
 </span>
</p>
<p>
 <span data-rw-start="2412.32" data-rw-transcript-version="2">
 And you know, and that practically comes
 </span>
 <span data-rw-start="2415.119" data-rw-transcript-version="2">
 from experience, not from talking to a
 </span>
 <span data-rw-start="2417.68" data-rw-transcript-version="2">
 LLM.
 </span>
</p>
<p>
 <span data-rw-start="2418.56" data-rw-transcript-version="2">
 &gt;&gt; Okay,
 </span>
 <span data-rw-start="2421.2" data-rw-transcript-version="2">
 &gt;&gt; just very short.
 </span>
 <span data-rw-start="2423.599" data-rw-transcript-version="2">
 &gt;&gt; I got the microphone.
 </span>
 <span data-rw-start="2426.148" data-rw-transcript-version="2">
 [laughter] So, um, again, in the university,
 </span>
 <span data-rw-start="2428.96" data-rw-transcript-version="2">
 in teaching, we, um, if we, if we’re
 </span>
 <span data-rw-start="2432.16" data-rw-transcript-version="2">
 looking at the motivation for students,
 </span>
 <span data-rw-start="2433.839" data-rw-transcript-version="2">
 I think we’re a bit biased up
 </span>
 <span data-rw-start="2435.92" data-rw-transcript-version="2">
 here, and maybe down here as well, that we
 </span>
 <span data-rw-start="2437.599" data-rw-transcript-version="2">
 are learning because we’re curious, we
 </span>
 <span data-rw-start="2439.2" data-rw-transcript-version="2">
 want to improve our skills. But about 60%
 </span>
 <span data-rw-start="2442.24" data-rw-transcript-version="2">
 of the students are there as a means to
 </span>
 <span data-rw-start="2444.8" data-rw-transcript-version="2">
 an end.
 </span>
</p>
<p>
 <span data-rw-start="2446.079" data-rw-transcript-version="2">
 &gt;&gt; And that's a, that's a very different
 </span>
 <span data-rw-start="2447.52" data-rw-transcript-version="2">
 motivation, and it creates a very
 </span>
 <span data-rw-start="2449.2" data-rw-transcript-version="2">
 different way of working with it. And
 </span>
 <span data-rw-start="2451.68" data-rw-transcript-version="2">
 the way that I try to explain it to my
 </span>
 <span data-rw-start="2453.52" data-rw-transcript-version="2">
 students is the difference between just
 </span>
 <span data-rw-start="2455.04" data-rw-transcript-version="2">
 in case and just-in-time learning. So
 </span>
 <span data-rw-start="2457.68" data-rw-transcript-version="2">
 what we try to do at the university is
 </span>
 <span data-rw-start="2459.52" data-rw-transcript-version="2">
 just-in-case learning, just in case you
 </span>
 <span data-rw-start="2461.52" data-rw-transcript-version="2">
 Need to understand the compiler, you need
 </span>
 <span data-rw-start="2463.2" data-rw-transcript-version="2">
 to learn this just in case you need to
 </span>
 <span data-rw-start="2464.8" data-rw-transcript-version="2">
 understand this type system. But what AI
 </span>
 <span data-rw-start="2467.52" data-rw-transcript-version="2">
 can give you is the just-in-time
 </span>
 <span data-rw-start="2469.28" data-rw-transcript-version="2">
 learning. So just in time to hand in
 </span>
 <span data-rw-start="2471.52" data-rw-transcript-version="2">
 that assignment, you can learn that. But
 </span>
 <span data-rw-start="2473.76" data-rw-transcript-version="2">
 if you look at that like the deep neuro
 </span>
 <span data-rw-start="2476.64" data-rw-transcript-version="2">
 science ways of learning, that's not real
 </span>
</p>
<p>
 <span data-rw-start="2479.839" data-rw-transcript-version="2">
 learning. But let's not go into that
 </span>
 <span data-rw-start="2482.16" data-rw-transcript-version="2">
 here. I just want to reinforce something
 </span>
 <span data-rw-start="2484.96" data-rw-transcript-version="2">
 that Emily said. Um, so there's a
 </span>
 <span data-rw-start="2487.44" data-rw-transcript-version="2">
 model that's been kicking around that
 </span>
 <span data-rw-start="2488.72" data-rw-transcript-version="2">
 sort of in education circles for decades,
 </span>
 <span data-rw-start="2490.96" data-rw-transcript-version="2">
 called var visual auditory reading, and
 </span>
 <span data-rw-start="2494" data-rw-transcript-version="2">
 kinesthetic. And the idea is that
 </span>
 <span data-rw-start="2495.44" data-rw-transcript-version="2">
 there are different modes of learning. And
 </span>
 <span data-rw-start="2497.04" data-rw-transcript-version="2">
 some people are visual learners, and they
 </span>
 <span data-rw-start="2498.64" data-rw-transcript-version="2">
 like pictures, and some people are
 </span>
 <span data-rw-start="2499.92" data-rw-transcript-version="2">
 auditory learners. They want to hear
 </span>
 <span data-rw-start="2501.119" data-rw-transcript-version="2">
 stories. Some people like to read and do
 </span>
 <span data-rw-start="2503.2" data-rw-transcript-version="2">
 self-paced stuff. And then some people
 </span>
 <span data-rw-start="2504.64" data-rw-transcript-version="2">
 are kinesthetic, they like to interact
 </span>
 <span data-rw-start="2506" data-rw-transcript-version="2">
 with this thing. And it's a very
 </span>
</p>
<p>
 <span data-rw-start="2507.599" data-rw-transcript-version="2">
 appealing model, and it has some very
 </span>
 <span data-rw-start="2509.44" data-rw-transcript-version="2">
 bogus research around it. And it turns
 </span>
 <span data-rw-start="2511.119" data-rw-transcript-version="2">
 Out of it's complete nonsense, right? That
 </span>
 <span data-rw-start="2513.359" data-rw-transcript-version="2">
 absolutely falls apart as soon as you
 </span>
 <span data-rw-start="2514.8" data-rw-transcript-version="2">
 start to touch the edges because it
 </span>
 <span data-rw-start="2516.56" data-rw-transcript-version="2">
 turns out that everybody, everybody is a
 </span>
 <span data-rw-start="2518.64" data-rw-transcript-version="2">
 kinesthetic learner, right? You're a
 </span>
 <span data-rw-start="2520.56" data-rw-transcript-version="2">
 kinesthetic learner from birth. The way
 </span>
 <span data-rw-start="2522.4" data-rw-transcript-version="2">
 you learn anything is by interacting
 </span>
 <span data-rw-start="2524.88" data-rw-transcript-version="2">
 with it, by playing with it. Exactly to
 </span>
 <span data-rw-start="2526.56" data-rw-transcript-version="2">
 your point, building with it. And if I
 </span>
 <span data-rw-start="2528.56" data-rw-transcript-version="2">
 ask an LLM for the answer, I'll get the
 </span>
 <span data-rw-start="2530.4" data-rw-transcript-version="2">
 answer. But no learning took place. And
 </span>
 <span data-rw-start="2532.4" data-rw-transcript-version="2">
 even if I ask an LLM to teach me, still
 </span>
 <span data-rw-start="2535.119" data-rw-transcript-version="2">
 no learning takes place, right? Not
 </span>
 <span data-rw-start="2536.96" data-rw-transcript-version="2">
 until you are interacting with the
 </span>
</p>
<p>
 <span data-rw-start="2538.8" data-rw-transcript-version="2">
 thing, making the mistakes because
 </span>
 <span data-rw-start="2541.04" data-rw-transcript-version="2">
 learning is about making mistakes and
 </span>
 <span data-rw-start="2542.72" data-rw-transcript-version="2">
 understanding why that thing was a
 </span>
 <span data-rw-start="2544.079" data-rw-transcript-version="2">
 mistake. Getting that experience,
 </span>
 <span data-rw-start="2546.24" data-rw-transcript-version="2">
 putting in those hours and then going,
 </span>
 <span data-rw-start="2547.92" data-rw-transcript-version="2">
 "Oh, right. Okay, this thing makes sense
 </span>
 <span data-rw-start="2549.599" data-rw-transcript-version="2">
 now." The the write the for loop,
 </span>
 <span data-rw-start="2552.319" data-rw-transcript-version="2">
 understand a for loop, write another for
 </span>
 <span data-rw-start="2553.92" data-rw-transcript-version="2">
 loop in a different language,
 </span>
 <span data-rw-start="2554.8" data-rw-transcript-version="2">
 understand, oh right, now I get
 </span>
 <span data-rw-start="2556.16" data-rw-transcript-version="2">
 iteration. This is making sense. And
 </span>
 <span data-rw-start="2558.4" data-rw-transcript-version="2">
 Without actually getting your hands in
 </span>
 <span data-rw-start="2561.359" data-rw-transcript-version="2">
 there doing stuff, no learning is
 </span>
 <span data-rw-start="2563.599" data-rw-transcript-version="2">
 happening.
 </span>
</p>
<p>
 <span data-rw-start="2568.24" data-rw-transcript-version="2">
 I mean, one of my hopes is that that
 </span>
 <span data-rw-start="2570.8" data-rw-transcript-version="2">
 will be the thing that will be happening
 </span>
 <span data-rw-start="2572.16" data-rw-transcript-version="2">
 that we have that the the next
 </span>
 <span data-rw-start="2574.72" data-rw-transcript-version="2">
 generation will learn through the pain
 </span>
 <span data-rw-start="2576.24" data-rw-transcript-version="2">
 of making mistakes the same way that we
 </span>
 <span data-rw-start="2578" data-rw-transcript-version="2">
 did, and then they will be forced to like
 </span>
 <span data-rw-start="2579.599" data-rw-transcript-version="2">
 understand certain things, and hopefully
 </span>
 <span data-rw-start="2581.2" data-rw-transcript-version="2">
 that period of time will be as short as
 </span>
 <span data-rw-start="2582.8" data-rw-transcript-version="2">
 possible. [laughter]
 </span>
 <span data-rw-start="2584.4" data-rw-transcript-version="2">
 But yeah, you know, there will be like I
 </span>
 <span data-rw-start="2587.76" data-rw-transcript-version="2">
 did, I made mistakes. I once, during an
 </span>
 <span data-rw-start="2589.839" data-rw-transcript-version="2">
 internship, deleted the whole production
 </span>
 <span data-rw-start="2591.92" data-rw-transcript-version="2">
 database because there was only
 </span>
 <span data-rw-start="2593.28" data-rw-transcript-version="2">
 production.
 </span>
</p>
<p>
 <span data-rw-start="2593.92" data-rw-transcript-version="2">
 &gt;&gt; Put your hands up if you ever deleted
 </span>
 <span data-rw-start="2595.794" data-rw-transcript-version="2">
 [laughter]
 </span>
 <span data-rw-start="2596.72" data-rw-transcript-version="2">
 It was the user database as well. Yeah. But, um, this was, yeah, a
 </span>
 <span data-rw-start="2603.28" data-rw-transcript-version="2">
 long time ago. They shouldn’t
 </span>
 <span data-rw-start="2606.24" data-rw-transcript-version="2">
 have let an intern, you know, mess around
 </span>
 <span data-rw-start="2608.48" data-rw-transcript-version="2">
 in the PHPMyAdmin. [laughter]
 </span>
 <span data-rw-start="2612.319" data-rw-transcript-version="2">
 Anyway, I learned from that. Right.
 </span>
</p>
<p>
 <span data-rw-start="2617.28" data-rw-transcript-version="2">
 &gt;&gt; Okay. Learning, uh, is one of the human
 </span>
 <span data-rw-start="2619.839" data-rw-transcript-version="2">
 aspects. Another one is, uh, how do we
 </span>
 <span data-rw-start="2622.079" data-rw-transcript-version="2">
 actually work and how would, uh, teams, uh,
 </span>
 <span data-rw-start="2626" data-rw-transcript-version="2">
 maybe change or not change. I don't know,
 </span>
 <span data-rw-start="2628.64" data-rw-transcript-version="2">
 that's, uh, another discussion that I hear
 </span>
 <span data-rw-start="2631.28" data-rw-transcript-version="2">
 quite a lot. I think Yung Abalo talked
 </span>
 <span data-rw-start="2633.599" data-rw-transcript-version="2">
 about that last year in the keynote
 </span>
 <span data-rw-start="2635.119" data-rw-transcript-version="2">
 here. He said, well, we will probably be
 </span>
 <span data-rw-start="2637.359" data-rw-transcript-version="2">
 moving to other team sizes, uh, which
 </span>
 <span data-rw-start="2639.839" data-rw-transcript-version="2">
 might become smaller. Uh, there's also
 </span>
 <span data-rw-start="2642.4" data-rw-transcript-version="2">
 another aspect, um, that I actually hear a
 </span>
 <span data-rw-start="2645.839" data-rw-transcript-version="2">
 lot when I talk to people that work in
 </span>
 <span data-rw-start="2648.079" data-rw-transcript-version="2">
 an environment or try to use, uh,
 </span>
 <span data-rw-start="2650.96" data-rw-transcript-version="2">
 uh, to use those agents, which is, they
 </span>
 <span data-rw-start="2653.76" data-rw-transcript-version="2">
 don't actually pair program anymore. Uh,
 </span>
 <span data-rw-start="2656.48" data-rw-transcript-version="2">
 they mostly sit alone, and, uh, try to work
 </span>
 <span data-rw-start="2660" data-rw-transcript-version="2">
 with their agents somehow. So, what are
 </span>
 <span data-rw-start="2663.2" data-rw-transcript-version="2">
 your thoughts about
 </span>
 <span data-rw-start="2665.2" data-rw-transcript-version="2">
 how work life and teamwork actually
 </span>
 <span data-rw-start="2669.04" data-rw-transcript-version="2">
 change if it comes, like it comes maybe,
 </span>
 <span data-rw-start="2672" data-rw-transcript-version="2">
 everything will be back to, uh, to normal
 </span>
 <span data-rw-start="2675.839" data-rw-transcript-version="2">
 in a year, but, uh, it doesn't really look
 </span>
 <span data-rw-start="2678.88" data-rw-transcript-version="2">
 like that. So, what do you think? How
 </span>
 <span data-rw-start="2682.56" data-rw-transcript-version="2">
 teamwork will change? How team sizes will
 </span>
 <span data-rw-start="2684.72" data-rw-transcript-version="2">
 change?
 </span>
</p>
<p>
 <span data-rw-start="2689.04" data-rw-transcript-version="2">
 &gt;&gt; All the things I'm thinking about that
 </span>
 <span data-rw-start="2690.72" data-rw-transcript-version="2">
 are disagreeing being with each other.
 </span>
 <span data-rw-start="2693.52" data-rw-transcript-version="2">
 &gt;&gt; Okay. So what are some of them?
 </span>
 <span data-rw-start="2695.359" data-rw-transcript-version="2">
 &gt;&gt; Okay. So one is I, so one part of me
 </span>
 <span data-rw-start="2698.96" data-rw-transcript-version="2">
 thinks the teams will definitely get
 </span>
 <span data-rw-start="2700.48" data-rw-transcript-version="2">
 smaller
 </span>
 <span data-rw-start="2702" data-rw-transcript-version="2">
 because we can use some agent as a team
 </span>
 <span data-rw-start="2705.44" data-rw-transcript-version="2">
 member, and we can use those to learn. I
 </span>
 <span data-rw-start="2707.359" data-rw-transcript-version="2">
 can see that also coming back to the
 </span>
 <span data-rw-start="2709.04" data-rw-transcript-version="2">
 teaching that the students can use to
 </span>
 <span data-rw-start="2710.88" data-rw-transcript-version="2">
 learn in the same way as peer
 </span>
 <span data-rw-start="2712.48" data-rw-transcript-version="2">
 programming, and peer reviews would be good. On the other hand, I'm
 </span>
 <span data-rw-start="2717.359" data-rw-transcript-version="2">
 thinking that it might be easier to
 </span>
 <span data-rw-start="2719.2" data-rw-transcript-version="2">
 cope with the big cognitive load of a
 </span>
 <span data-rw-start="2720.96" data-rw-transcript-version="2">
 big team if you have the help of an
 </span>
</p>
<p>
 <span data-rw-start="2724.16" data-rw-transcript-version="2">
 artificial intelligence in some way. So
 </span>
 <span data-rw-start="2725.92" data-rw-transcript-version="2">
 those two things are disagreeing with
 </span>
 <span data-rw-start="2727.44" data-rw-transcript-version="2">
 each other. I'm also thinking that it's
 </span>
 <span data-rw-start="2729.839" data-rw-transcript-version="2">
 a shame that people will start using
 </span>
 <span data-rw-start="2733.119" data-rw-transcript-version="2">
 well, an AI instead of pair programming
 </span>
 <span data-rw-start="2736.079" data-rw-transcript-version="2">
 with another human being. But on the
 </span>
 <span data-rw-start="2738.64" data-rw-transcript-version="2">
 other hand, I know a lot of people are
 </span>
 <span data-rw-start="2740.16" data-rw-transcript-version="2">
 suffering in the pair programming style,
 </span>
 <span data-rw-start="2741.92" data-rw-transcript-version="2">
 and they might actually benefit from
 </span>
 <span data-rw-start="2743.839" data-rw-transcript-version="2">
 Just sitting with the computer. So I'm
 </span>
 <span data-rw-start="2746.4" data-rw-transcript-version="2">
 completely torn about this. I have a
 </span>
 <span data-rw-start="2748.48" data-rw-transcript-version="2">
 lot of other things going on in my
 </span>
 <span data-rw-start="2750.56" data-rw-transcript-version="2">
 brain, but I'll leave it with that.
 </span>
</p>
<p>
 <span data-rw-start="2754.8" data-rw-transcript-version="2">
 I can talk about, I don't think we've
 </span>
 <span data-rw-start="2757.68" data-rw-transcript-version="2">
 solved this. I mean, the
 </span>
 <span data-rw-start="2759.76" data-rw-transcript-version="2">
 experience of working in an ensemble.
 </span>
 <span data-rw-start="2761.839" data-rw-transcript-version="2">
 I do a lot of working in an ensemble as
 </span>
 <span data-rw-start="2763.52" data-rw-transcript-version="2">
 a technical coach, and it's such a
 </span>
 <span data-rw-start="2765.68" data-rw-transcript-version="2">
 good forum for sharing knowledge and
 </span>
 <span data-rw-start="2767.839" data-rw-transcript-version="2">
 communicating about code and teaching, and
 </span>
 <span data-rw-start="2770.24" data-rw-transcript-version="2">
 there's so many benefits to it. But
 </span>
 <span data-rw-start="2773.04" data-rw-transcript-version="2">
 my experience of sticking an AI into
 </span>
 <span data-rw-start="2775.28" data-rw-transcript-version="2">
 that forum as an agentic AI is that it
 </span>
 <span data-rw-start="2779.28" data-rw-transcript-version="2">
 somehow collapses if you're not
 </span>
 <span data-rw-start="2782.16" data-rw-transcript-version="2">
 careful. It just collapses the whole
 </span>
 <span data-rw-start="2784.4" data-rw-transcript-version="2">
 conversation, and it all turns into us
 </span>
 <span data-rw-start="2786.319" data-rw-transcript-version="2">
 staring at text scrolling past on the
 </span>
 <span data-rw-start="2789.44" data-rw-transcript-version="2">
 agentic AI, and suddenly we're not
 </span>
 <span data-rw-start="2791.28" data-rw-transcript-version="2">
 communicating; we're not learning,
 </span>
 <span data-rw-start="2792.64" data-rw-transcript-version="2">
 and this AI has turned into the most
 </span>
 <span data-rw-start="2794.88" data-rw-transcript-version="2">
 horrible pair ensemble member ever, who
 </span>
 <span data-rw-start="2797.76" data-rw-transcript-version="2">
 just takes over. Um, and I don't have
 </span>
 <span data-rw-start="2801.76" data-rw-transcript-version="2">
 any really good solutions for this yet,
 </span>
 <span data-rw-start="2803.52" data-rw-transcript-version="2">
 but the trend at the moment is very.
 </span>
</p>
<p>
 <span data-rw-start="2806.4" data-rw-transcript-version="2">
 Much towards me and my AI or my fleet of
 </span>
 <span data-rw-start="2808.72" data-rw-transcript-version="2">
 agents, and and suddenly we've lost all
 </span>
 <span data-rw-start="2811.68" data-rw-transcript-version="2">
 this collaborative programming, and we've
 </span>
 <span data-rw-start="2814.48" data-rw-transcript-version="2">
 got to get it back. I mean,
 </span>
 <span data-rw-start="2817.68" data-rw-transcript-version="2">
 &gt;&gt; I mean that's
 </span>
 <span data-rw-start="2819.2" data-rw-transcript-version="2">
 &gt;&gt; I had yesterday evening an interesting
 </span>
 <span data-rw-start="2821.04" data-rw-transcript-version="2">
 discussion, and one said, if I’m
 </span>
 <span data-rw-start="2823.76" data-rw-transcript-version="2">
 programming with other people in an
 </span>
 <span data-rw-start="2825.599" data-rw-transcript-version="2">
 ensemble, mop, whatever you call it, he
 </span>
 <span data-rw-start="2827.839" data-rw-transcript-version="2">
 said it's even better than AI because
 </span>
 <span data-rw-start="2830.48" data-rw-transcript-version="2">
 the people are foreseeing which problems
 </span>
 <span data-rw-start="2833.04" data-rw-transcript-version="2">
 will come up, and they are already solving
 </span>
 <span data-rw-start="2835.44" data-rw-transcript-version="2">
 the problems. This is what AI can
 </span>
 <span data-rw-start="2837.839" data-rw-transcript-version="2">
 currently maybe not foresee,
 </span>
 <span data-rw-start="2840.96" data-rw-transcript-version="2">
 what will be the next challenges coming
 </span>
 <span data-rw-start="2842.8" data-rw-transcript-version="2">
 up because they all know where it will
 </span>
 <span data-rw-start="2844.88" data-rw-transcript-version="2">
 go. So, this is something I think
 </span>
 <span data-rw-start="2846.72" data-rw-transcript-version="2">
 really interesting. But on the other
 </span>
 <span data-rw-start="2847.76" data-rw-transcript-version="2">
 hand, he said, "But when I’m alone, then
 </span>
 <span data-rw-start="2850.64" data-rw-transcript-version="2">
 it’s better to have someone next to me."
 </span>
 <span data-rw-start="2853.119" data-rw-transcript-version="2">
 So if sometimes there is no ensemble
 </span>
 <span data-rw-start="2855.68" data-rw-transcript-version="2">
 available for whatever reason, I’m, I’m
 </span>
 <span data-rw-start="2857.839" data-rw-transcript-version="2">
 working later than the others, whatever.
 </span>
</p>
<p>
 <span data-rw-start="2859.68" data-rw-transcript-version="2">
 So, I think you are having more
 </span>
 <span data-rw-start="2861.359" data-rw-transcript-version="2">
 flexibility, maybe now. You, you have a
 </span>
 <span data-rw-start="2863.92" data-rw-transcript-version="2">
 Pair if you want or you need one. Um but,
 </span>
 <span data-rw-start="2867.76" data-rw-transcript-version="2">
 yeah, on the other side, I'm thinking
 </span>
 <span data-rw-start="2870.16" data-rw-transcript-version="2">
 yes, you can have smaller teams, but
 </span>
 <span data-rw-start="2871.76" data-rw-transcript-version="2">
 your PO is also speeding up. So he's
 </span>
 <span data-rw-start="2874.24" data-rw-transcript-version="2">
 producing more user stories, and so maybe
 </span>
 <span data-rw-start="2876.64" data-rw-transcript-version="2">
 you still need the same size amount of
 </span>
 <span data-rw-start="2878.96" data-rw-transcript-version="2">
 developers. On the other hand, you can
 </span>
 <span data-rw-start="2880.96" data-rw-transcript-version="2">
 maybe easily start something new with
 </span>
 <span data-rw-start="2884.079" data-rw-transcript-version="2">
 two developers already, which you have
 </span>
 <span data-rw-start="2885.76" data-rw-transcript-version="2">
 never done in the past because two were
 </span>
 <span data-rw-start="2887.839" data-rw-transcript-version="2">
 too small, but now you can start
 </span>
 <span data-rw-start="2890.48" data-rw-transcript-version="2">
 something. So I think there are
 </span>
 <span data-rw-start="2891.76" data-rw-transcript-version="2">
 opportunities to have different team
 </span>
 <span data-rw-start="2893.839" data-rw-transcript-version="2">
 sizes, but still you will have the team
 </span>
 <span data-rw-start="2896.72" data-rw-transcript-version="2">
 sizes you had before, maybe as well. So
 </span>
 <span data-rw-start="2898.64" data-rw-transcript-version="2">
 maybe there's not this one single
 </span>
 <span data-rw-start="2900.319" data-rw-transcript-version="2">
 answer.
 </span>
</p>
<p>
 <span data-rw-start="2902.319" data-rw-transcript-version="2">
 I mean, there are these different scenarios
 </span>
 <span data-rw-start="2903.92" data-rw-transcript-version="2">
 that we can play through, right? Will
 </span>
 <span data-rw-start="2905.44" data-rw-transcript-version="2">
 teams get smaller and then potentially
 </span>
 <span data-rw-start="2908.24" data-rw-transcript-version="2">
 the individual cognitive load will
 </span>
 <span data-rw-start="2911.119" data-rw-transcript-version="2">
 go up? Or will we give existing team
 </span>
 <span data-rw-start="2913.52" data-rw-transcript-version="2">
 sizes more topics to work on, and then
 </span>
 <span data-rw-start="2915.76" data-rw-transcript-version="2">
 the whole team's cognitive load will
 </span>
 <span data-rw-start="2917.839" data-rw-transcript-version="2">
 potentially go up?
 </span>
</p>
<p>
 <span data-rw-start="2919.92" data-rw-transcript-version="2">
 Something about teams and systems being
 </span>
 <span data-rw-start="2921.92" data-rw-transcript-version="2">
 able to collaborate with each other
 </span>
 <span data-rw-start="2923.44" data-rw-transcript-version="2">
 easier or something like that. I think
 </span>
 <span data-rw-start="2926" data-rw-transcript-version="2">
 in part it will depend on this like kind
 </span>
 <span data-rw-start="2928.16" data-rw-transcript-version="2">
 of like break neck speed and throughput
 </span>
 <span data-rw-start="2930.96" data-rw-transcript-version="2">
 that people are trying to do right now
 </span>
 <span data-rw-start="2933.76" data-rw-transcript-version="2">
 to like if that will collapse at some
 </span>
 <span data-rw-start="2935.76" data-rw-transcript-version="2">
 point or if we will figure out some way
 </span>
 <span data-rw-start="2937.44" data-rw-transcript-version="2">
 to do it sustainably and if that even
 </span>
 <span data-rw-start="2940" data-rw-transcript-version="2">
 makes sense right, like all of this like
 </span>
 <span data-rw-start="2942.64" data-rw-transcript-version="2">
 throughput. Do we even want that? What is
 </span>
 <span data-rw-start="2944.559" data-rw-transcript-version="2">
 the Goldilocks speed and throughput that
 </span>
 <span data-rw-start="2947.359" data-rw-transcript-version="2">
 actually makes sense to create value and
 </span>
</p>
<p>
 <span data-rw-start="2949.359" data-rw-transcript-version="2">
 to not burn people out? And so, I think
 </span>
 <span data-rw-start="2952" data-rw-transcript-version="2">
 it will depend a lot on that. And I
 </span>
 <span data-rw-start="2954.559" data-rw-transcript-version="2">
 mean, there’s also organizational
 </span>
 <span data-rw-start="2955.92" data-rw-transcript-version="2">
 things, right? Like you can't make a
 </span>
 <span data-rw-start="2957.359" data-rw-transcript-version="2">
 team so small that you can't be on call
 </span>
 <span data-rw-start="2959.359" data-rw-transcript-version="2">
 anymore and stuff like that, right? So
 </span>
 <span data-rw-start="2960.96" data-rw-transcript-version="2">
 that also plays into it. So similar to I
 </span>
 <span data-rw-start="2963.2" data-rw-transcript-version="2">
 know, I also keep going back and forth.
 </span>
 <span data-rw-start="2964.96" data-rw-transcript-version="2">
 There’s so many pros and cons to
 </span>
 <span data-rw-start="2966.64" data-rw-transcript-version="2">
 different scenarios or like, yeah, it’s um
 </span>
 <span data-rw-start="2970.559" data-rw-transcript-version="2">
 there’s also, of course, everybody
 </span>
 <span data-rw-start="2972" data-rw-transcript-version="2">
 thinking now, every developer just does.
 </span>
</p>
<p>
 <span data-rw-start="2975.119" data-rw-transcript-version="2">
 All the different jobs and everybody can
 </span>
 <span data-rw-start="2977.28" data-rw-transcript-version="2">
 do anything, right? Everybody can do
 </span>
 <span data-rw-start="2978.72" data-rw-transcript-version="2">
 design and the product owner can code,
 </span>
 <span data-rw-start="2981.2" data-rw-transcript-version="2">
 and, um, yeah, it definitely, I think it
 </span>
 <span data-rw-start="2985.119" data-rw-transcript-version="2">
 would be good if more people would
 </span>
 <span data-rw-start="2986.319" data-rw-transcript-version="2">
 experiment more with this. I think a lot
 </span>
 <span data-rw-start="2987.76" data-rw-transcript-version="2">
 of people are very careful about it
 </span>
 <span data-rw-start="2989.28" data-rw-transcript-version="2">
 right now, but there’s not a lot of data
 </span>
 <span data-rw-start="2991.04" data-rw-transcript-version="2">
 yet. I think.
 </span>
</p>
<p>
 <span data-rw-start="2996.4" data-rw-transcript-version="2">
 &gt;&gt; So. I, I, when someone asks me
 </span>
 <span data-rw-start="2998.88" data-rw-transcript-version="2">
 something like this, I go back to first
 </span>
 <span data-rw-start="3000.4" data-rw-transcript-version="2">
 principles. The question I ask myself
 </span>
 <span data-rw-start="3002" data-rw-transcript-version="2">
 is, so we’re talking about how team
 </span>
 <span data-rw-start="3004.24" data-rw-transcript-version="2">
 sizes are going to change. The question
 </span>
 <span data-rw-start="3005.44" data-rw-transcript-version="2">
 I ask myself is why are they the size
 </span>
 <span data-rw-start="3007.599" data-rw-transcript-version="2">
 they are now, right? Because they
 </span>
 <span data-rw-start="3010.16" data-rw-transcript-version="2">
 weren’t always that, and there’s I
 </span>
 <span data-rw-start="3012.079" data-rw-transcript-version="2">
 mean, I know there’s some religion
 </span>
 <span data-rw-start="3013.359" data-rw-transcript-version="2">
 around, you know, seven plus or minus
 </span>
 <span data-rw-start="3015.119" data-rw-transcript-version="2">
 two nonsense. Um, but the point is, you
 </span>
 <span data-rw-start="3018.8" data-rw-transcript-version="2">
 know, if I go back in history, even for
 </span>
 <span data-rw-start="3021.04" data-rw-transcript-version="2">
 relatively recently, you’d have the DBAs
 </span>
 <span data-rw-start="3023.599" data-rw-transcript-version="2">
 over here, the systems folks over here,
 </span>
 <span data-rw-start="3025.68" data-rw-transcript-version="2">
 the, uh, functional people over here, the
 </span>
 <span data-rw-start="3028.319" data-rw-transcript-version="2">
 UI people over here, in completely
 </span>
 <span data-rw-start="3029.839" data-rw-transcript-version="2">
 Different teams, maybe organizations,
 </span>
 <span data-rw-start="3032.4" data-rw-transcript-version="2">
 either in silos or whatever, and they
 </span>
 <span data-rw-start="3036" data-rw-transcript-version="2">
 weren't there because we thought that
 </span>
 <span data-rw-start="3037.44" data-rw-transcript-version="2">
 was the right thing to do, and now we
 </span>
 <span data-rw-start="3038.559" data-rw-transcript-version="2">
 think it's a different thing to do. A
 </span>
 <span data-rw-start="3040.24" data-rw-transcript-version="2">
 lot of it is because of tooling and
 </span>
 <span data-rw-start="3041.92" data-rw-transcript-version="2">
 because of language change and because
 </span>
 <span data-rw-start="3043.839" data-rw-transcript-version="2">
 of just the environment we're in.
 </span>
</p>
<p>
 <span data-rw-start="3046.16" data-rw-transcript-version="2">
 Suddenly, things where we would have had
 </span>
 <span data-rw-start="3048.079" data-rw-transcript-version="2">
 to take something and split it into
 </span>
 <span data-rw-start="3049.92" data-rw-transcript-version="2">
 pieces and farm those pieces out, and
 </span>
 <span data-rw-start="3051.92" data-rw-transcript-version="2">
 then bring them back together in the end,
 </span>
 <span data-rw-start="3053.119" data-rw-transcript-version="2">
 which is how we used to do software,
 </span>
 <span data-rw-start="3054.96" data-rw-transcript-version="2">
 becomes tractable for me to say,
 <br/>
 hey, Bagita, can you add this field to this
 </span>
 <span data-rw-start="3058.559" data-rw-transcript-version="2">
 report? And she has the skills to make
 </span>
 <span data-rw-start="3062.079" data-rw-transcript-version="2">
 the UI change, make the functional change,
 </span>
 <span data-rw-start="3064.319" data-rw-transcript-version="2">
 make the calculation change, make the
 </span>
 <span data-rw-start="3065.839" data-rw-transcript-version="2">
 database change, and make sure all
 </span>
 <span data-rw-start="3068.24" data-rw-transcript-version="2">
 the glue in the middle is working.
 </span>
 <span data-rw-start="3069.839" data-rw-transcript-version="2">
 And write tests for it, and be confident
 </span>
 <span data-rw-start="3071.44" data-rw-transcript-version="2">
 that it's changed right. So that's now a
 </span>
 <span data-rw-start="3073.68" data-rw-transcript-version="2">
 thing that a human being can do,
 </span>
 <span data-rw-start="3075.28" data-rw-transcript-version="2">
 or a pair of human beings in a small team.
 </span>
</p>
<p>
 <span data-rw-start="3080.079" data-rw-transcript-version="2">
 I don't necessarily think we're going to
 </span>
 <span data-rw-start="3081.2" data-rw-transcript-version="2">
 get smaller teams or bigger teams or
 </span>
 <span data-rw-start="3082.559" data-rw-transcript-version="2">
 anything like that. I think the nature
 </span>
 <span data-rw-start="3083.52" data-rw-transcript-version="2">
 of work is going to change. So why why
 </span>
 <span data-rw-start="3086.079" data-rw-transcript-version="2">
 do we have user stories, right? Why do
 </span>
 <span data-rw-start="3087.52" data-rw-transcript-version="2">
 we have why do we work in small chunks?
 </span>
 <span data-rw-start="3089.76" data-rw-transcript-version="2">
 Uh, risk, it comes back to risk and blast
 </span>
 <span data-rw-start="3092.559" data-rw-transcript-version="2">
 radius and how much stuff we can hold in
 </span>
 <span data-rw-start="3094.48" data-rw-transcript-version="2">
 our heads. By the way, complete sidebar,
 </span>
 <span data-rw-start="3096.88" data-rw-transcript-version="2">
 we're doing cognitive load all wrong,
 </span>
 <span data-rw-start="3099.119" data-rw-transcript-version="2">
 right? Everything you think you know
 </span>
 <span data-rw-start="3100.24" data-rw-transcript-version="2">
 about cognitive load is completely
 </span>
 <span data-rw-start="3101.839" data-rw-transcript-version="2">
 wrong. Um ask me later. I get really
 </span>
 <span data-rw-start="3104.96" data-rw-transcript-version="2">
 cross about this, but not now. We only
 </span>
</p>
<p>
 <span data-rw-start="3107.68" data-rw-transcript-version="2">
 have eight minutes and 30 seconds left
 </span>
 <span data-rw-start="3109.359" data-rw-transcript-version="2">
 to change the world. Um,
 </span>
 <span data-rw-start="3112.48" data-rw-transcript-version="2">
 so I, I suspect what's going to happen is
 </span>
 <span data-rw-start="3116.96" data-rw-transcript-version="2">
 we're going to be more ambitious in the
 </span>
 <span data-rw-start="3119.04" data-rw-transcript-version="2">
 size of a unit of work because we can
 </span>
 <span data-rw-start="3121.28" data-rw-transcript-version="2">
 be, right? We can say I want to make
 </span>
 <span data-rw-start="3124" data-rw-transcript-version="2">
 this significant. I want to implement
 </span>
 <span data-rw-start="3125.76" data-rw-transcript-version="2">
 this entire feature because I can with
 </span>
 <span data-rw-start="3127.76" data-rw-transcript-version="2">
 my little team and some superpowered
 </span>
 <span data-rw-start="3130.319" data-rw-transcript-version="2">
 robots in a way that would have taken
 </span>
 <span data-rw-start="3132.64" data-rw-transcript-version="2">
 weeks or months or would have need to be
 </span>
 <span data-rw-start="3134.079" data-rw-transcript-version="2">
 Split up into much finer slices before.
 </span>
</p>
<p>
 <span data-rw-start="3136.8" data-rw-transcript-version="2">
 Your elephant carpaccio becomes more like
 </span>
 <span data-rw-start="3139.04" data-rw-transcript-version="2">
 an elephant pasta, right? You can, you
 </span>
 <span data-rw-start="3141.68" data-rw-transcript-version="2">
 can just take bigger chunks of it.
 </span>
 <span data-rw-start="3143.2" data-rw-transcript-version="2">
 Sorry, vegetarians
 </span>
 <span data-rw-start="3144.96" data-rw-transcript-version="2">
 and anyone who likes elephants.
 </span>
 <span data-rw-start="3147.68" data-rw-transcript-version="2">
 Um, there’s I did want to mention though,
 </span>
 <span data-rw-start="3149.68" data-rw-transcript-version="2">
 domain-driven design is a real passion,
 </span>
 <span data-rw-start="3151.599" data-rw-transcript-version="2">
 and the kind of the core, the
 </span>
 <span data-rw-start="3155.28" data-rw-transcript-version="2">
 core idea in domain-driven design is the
 </span>
 <span data-rw-start="3158.079" data-rw-transcript-version="2">
 goal of what we do as people in
 </span>
 <span data-rw-start="3160.88" data-rw-transcript-version="2">
 organizations, doing stuff, is to
 </span>
 <span data-rw-start="3163.119" data-rw-transcript-version="2">
 understand what the stuff is and to
 </span>
 <span data-rw-start="3165.76" data-rw-transcript-version="2">
 figure out ways to meet that need.
 </span>
 <span data-rw-start="3169.359" data-rw-transcript-version="2">
 And by modeling the domain,
 </span>
 <span data-rw-start="3171.92" data-rw-transcript-version="2">
 particularly, isn’t
 </span>
 <span data-rw-start="3173.44" data-rw-transcript-version="2">
 like a perfect model for any domain.
 </span>
</p>
<p>
 <span data-rw-start="3174.559" data-rw-transcript-version="2">
 It's like, what’s the model for the domain for to solve this problem?
 </span>
 <span data-rw-start="3176.48" data-rw-transcript-version="2">
 By modeling the domain, the software is
 </span>
 <span data-rw-start="3177.839" data-rw-transcript-version="2">
 kind of a side effect of that. And this
 </span>
 <span data-rw-start="3180.079" data-rw-transcript-version="2">
 comes back to learning again, right? So
 </span>
 <span data-rw-start="3182.319" data-rw-transcript-version="2">
 the more we learn about the domain, the
 </span>
 <span data-rw-start="3184" data-rw-transcript-version="2">
 more we can articulate about the
 </span>
 <span data-rw-start="3185.76" data-rw-transcript-version="2">
 domain, the more we can build little
 </span>
 <span data-rw-start="3187.599" data-rw-transcript-version="2">
 software constructs that are our
 </span>
 <span data-rw-start="3189.68" data-rw-transcript-version="2">
 Projection of what we understand about
 </span>
 <span data-rw-start="3191.04" data-rw-transcript-version="2">
 the domain, the more problems we can
 </span>
 <span data-rw-start="3192.559" data-rw-transcript-version="2">
 solve in that domain. And you know the
 </span>
 <span data-rw-start="3195.599" data-rw-transcript-version="2">
 the, so the point is the learning. And
 </span>
 <span data-rw-start="3197.52" data-rw-transcript-version="2">
 if the way in which we're engaging with
 </span>
 <span data-rw-start="3200.16" data-rw-transcript-version="2">
 work isn't doing the learning, isn't
 </span>
 <span data-rw-start="3203.04" data-rw-transcript-version="2">
 doing the knowledge crunching, then
 </span>
 <span data-rw-start="3204.8" data-rw-transcript-version="2">
 we're not going to be able to solve
 </span>
 <span data-rw-start="3206.319" data-rw-transcript-version="2">
 those problems.
 </span>
</p>
<p>
 <span data-rw-start="3212.079" data-rw-transcript-version="2">
 Wow. [laughter]
 </span>
 <span data-rw-start="3216.64" data-rw-transcript-version="2">
 I'm, I think about, uh, whether I
 </span>
 <span data-rw-start="3219.599" data-rw-transcript-version="2">
 asked the last question or not, because
 </span>
 <span data-rw-start="3221.44" data-rw-transcript-version="2">
 I'm not sure we moved in the right
 </span>
 <span data-rw-start="3223.52" data-rw-transcript-version="2">
 direction, but I still do it.
 </span>
</p>
<p>
 <span data-rw-start="3226.8" data-rw-transcript-version="2">
 Uh, we were talking about teams, we were
 </span>
 <span data-rw-start="3228.88" data-rw-transcript-version="2">
 talking about team sizes and
 </span>
 <span data-rw-start="3230.96" data-rw-transcript-version="2">
 communication with other, uh, teams and
 </span>
 <span data-rw-start="3235.44" data-rw-transcript-version="2">
 so on and, and our agents. And one thing
 </span>
 <span data-rw-start="3238.16" data-rw-transcript-version="2">
 that comes to my mind when I talk about
 </span>
 <span data-rw-start="3240" data-rw-transcript-version="2">
 that is, uh, a topic that we always
 </span>
 <span data-rw-start="3244.079" data-rw-transcript-version="2">
 mentioned at this conference, Conway's
 </span>
 <span data-rw-start="3245.92" data-rw-transcript-version="2">
 law.
 </span>
 <span data-rw-start="3248.319" data-rw-transcript-version="2">
 Will we, I mean, I think Conway's
 </span>
 <span data-rw-start="3252.72" data-rw-transcript-version="2">
 law still will hold up because we will still
 </span>
 <span data-rw-start="3255.68" data-rw-transcript-version="2">
 have some kind of communication, uh, and
 </span>
 <span data-rw-start="3258.24" data-rw-transcript-version="2">
 This will still shape the structure of
 </span>
 <span data-rw-start="3261.599" data-rw-transcript-version="2">
 our architecture and so on, but will, uh,
 </span>
 <span data-rw-start="3265.2" data-rw-transcript-version="2">
 maybe we need to look differently at
 </span>
 <span data-rw-start="3268" data-rw-transcript-version="2">
 Conway's law in the future because we
 </span>
 <span data-rw-start="3270.24" data-rw-transcript-version="2">
 have [snorts].
 </span>
</p>
<p>
 <span data-rw-start="3271.359" data-rw-transcript-version="2">
 If I enter, or however you say that in
 </span>
 <span data-rw-start="3274.72" data-rw-transcript-version="2">
 English, uh, uh, the agents
 </span>
 <span data-rw-start="3278.72" data-rw-transcript-version="2">
 will, will it change? What do you think?
 </span>
 <span data-rw-start="3280.319" data-rw-transcript-version="2">
 About Conway's law in the future?
 </span>
</p>
<p>
 <span data-rw-start="3283.2" data-rw-transcript-version="2">
 &gt;&gt; I, I want to slightly derail this to go
 </span>
 <span data-rw-start="3285.76" data-rw-transcript-version="2">
 back to something I know touched on
 </span>
 <span data-rw-start="3287.92" data-rw-transcript-version="2">
 earlier, and I think it is okay, absolutely
 </span>
 <span data-rw-start="3290.4" data-rw-transcript-version="2">
 vital to this conversation. Conway's law
 </span>
 <span data-rw-start="3292.88" data-rw-transcript-version="2">
 is already happening. Conway's law for
 </span>
 <span data-rw-start="3294.8" data-rw-transcript-version="2">
 those who don't know, Melvin Conway, 1967.
 </span>
 <span data-rw-start="3297.44" data-rw-transcript-version="2">
 He said he wrote a wonderful paper, and
 </span>
 <span data-rw-start="3299.2" data-rw-transcript-version="2">
 he said, but what he observed is
 </span>
 <span data-rw-start="3301.76" data-rw-transcript-version="2">
 that the architecture of systems in
 </span>
 <span data-rw-start="3304.24" data-rw-transcript-version="2">
 large organizations
 </span>
 <span data-rw-start="3306" data-rw-transcript-version="2">
 tend to model the communication
 </span>
 <span data-rw-start="3308.88" data-rw-transcript-version="2">
 structure in those organizations. So
 </span>
 <span data-rw-start="3310.88" data-rw-transcript-version="2">
 it's nothing to do with, or structure,
 </span>
 <span data-rw-start="3312.24" data-rw-transcript-version="2">
 it's to do with how people communicate.
 </span>
</p>
<p>
 <span data-rw-start="3314.8" data-rw-transcript-version="2">
 And for me, the glaring illustration of
 </span>
 <span data-rw-start="3317.92" data-rw-transcript-version="2">
 Conway's law is that the information in
 </span>
 <span data-rw-start="3321.599" data-rw-transcript-version="2">
 An LLM is a projection of the
 </span>
 <span data-rw-start="3324.64" data-rw-transcript-version="2">
 communication of the types of people and
 </span>
 <span data-rw-start="3326.559" data-rw-transcript-version="2">
 organizations that built those LLMs,
 </span>
 <span data-rw-start="3328.8" data-rw-transcript-version="2">
 which takes us right back to bias, takes
 </span>
 <span data-rw-start="3331.359" data-rw-transcript-version="2">
 us right back to toxic. There's, you
 </span>
 <span data-rw-start="3334.4" data-rw-transcript-version="2">
 know, there are live court cases right
 </span>
 <span data-rw-start="3336.4" data-rw-transcript-version="2">
 now where I think it was Google Gemini.
 </span>
</p>
<p>
 <span data-rw-start="3338.8" data-rw-transcript-version="2">
 I'll probably get sued for this. One of
 </span>
 <span data-rw-start="3340.16" data-rw-transcript-version="2">
 the big LLMs uh told somebody to kill
 </span>
 <span data-rw-start="3343.04" data-rw-transcript-version="2">
 himself and gave him ways to kill
 </span>
 <span data-rw-start="3345.68" data-rw-transcript-version="2">
 himself. It said, "Well, you should
 </span>
 <span data-rw-start="3346.96" data-rw-transcript-version="2">
 probably end it, right?" This wasn't
 </span>
 <span data-rw-start="3349.359" data-rw-transcript-version="2">
 even a he was already thinking that and
 </span>
 <span data-rw-start="3351.359" data-rw-transcript-version="2">
 it gave him it. It made the suggestion,
 </span>
 <span data-rw-start="3354.64" data-rw-transcript-version="2">
 right? And this is baked into the stuff
 </span>
 <span data-rw-start="3357.04" data-rw-transcript-version="2">
 we've got. And and I's point when I was
 </span>
 <span data-rw-start="3359.04" data-rw-transcript-version="2">
 talking about kids being like cloud
 </span>
 <span data-rw-start="3360.4" data-rw-transcript-version="2">
 native or whatever, I'm talking about
 </span>
 <span data-rw-start="3361.839" data-rw-transcript-version="2">
 the folks designing systems having
 </span>
 <span data-rw-start="3364.079" data-rw-transcript-version="2">
 always had that. It's like being water
 </span>
 <span data-rw-start="3365.52" data-rw-transcript-version="2">
 native and saying, "What do you mean you
 </span>
 <span data-rw-start="3366.64" data-rw-transcript-version="2">
 have a well?" I just turn on the tap.
 </span>
</p>
<p>
 <span data-rw-start="3368.559" data-rw-transcript-version="2">
 That's what I mean. Obviously the things
 </span>
 <span data-rw-start="3370" data-rw-transcript-version="2">
 you build with that. Yes, we need online
 </span>
 <span data-rw-start="3372.24" data-rw-transcript-version="2">
 safety, right? We don't need the online
 </span>
 <span data-rw-start="3374.079" data-rw-transcript-version="2">
 Safety act. That is massively misunderstood in the UK, but anyone who's
 </span>
 <span data-rw-start="3376.559" data-rw-transcript-version="2">
 from the UK and just going why are you
 </span>
 <span data-rw-start="3378.88" data-rw-transcript-version="2">
 doing this? It's very, very easy for
 </span>
 <span data-rw-start="3380.64" data-rw-transcript-version="2">
 politicians to get derailed totally by
 </span>
 <span data-rw-start="3382.559" data-rw-transcript-version="2">
 this stuff. But we have, you know,
 </span>
 <span data-rw-start="3385.119" data-rw-transcript-version="2">
 apart from all the ethics of should we
 </span>
 <span data-rw-start="3388.72" data-rw-transcript-version="2">
 be running these things in, you know,
 </span>
 <span data-rw-start="3390.48" data-rw-transcript-version="2">
 energy-hungry water trouncing whatever
 </span>
 <span data-rw-start="3392.64" data-rw-transcript-version="2">
 places. So apart from the ethics of even
 </span>
 <span data-rw-start="3395.92" data-rw-transcript-version="2">
 running them, the content of those models is
 </span>
 <span data-rw-start="3397.92" data-rw-transcript-version="2">
 entirely Conway's law and it is hiding
 </span>
 <span data-rw-start="3400.64" data-rw-transcript-version="2">
 in plain sight, and it is terrifying.
 </span>
</p>
<p>
 <span data-rw-start="3410.4" data-rw-transcript-version="2">
 &gt;&gt; Very good point. I like that. Anybody
 </span>
 <span data-rw-start="3413.359" data-rw-transcript-version="2">
 else got any thoughts about that?
 </span>
 <span data-rw-start="3416.48" data-rw-transcript-version="2">
 &gt;&gt; And maybe a software-related example of
 </span>
 <span data-rw-start="3418.16" data-rw-transcript-version="2">
 that is that they, uh, they all assume
 </span>
 <span data-rw-start="3420.88" data-rw-transcript-version="2">
 pull requests because all their training
 </span>
 <span data-rw-start="3423.359" data-rw-transcript-version="2">
 data is full of the concept of pull
 </span>
 <span data-rw-start="3425.04" data-rw-transcript-version="2">
 requests. That is a communication
 </span>
 <span data-rw-start="3426.96" data-rw-transcript-version="2">
 pattern that we have, right? So
 </span>
 <span data-rw-start="3432.079" data-rw-transcript-version="2">
 &gt;&gt; They also assume that all code is just
 </span>
 <span data-rw-start="3434" data-rw-transcript-version="2">
 like the code you find on GitHub, which
 </span>
 <span data-rw-start="3436" data-rw-transcript-version="2">
 is really heartbreaking.
 </span>
</p>
<p>
 <span data-rw-start="3440.16" data-rw-transcript-version="2">
 &gt;&gt; Yeah. Um
 </span>
 <span data-rw-start="3442.4" data-rw-transcript-version="2">
 Open source maintainers do have a
 </span>
 <span data-rw-start="3445.04" data-rw-transcript-version="2">
 problem. We discussed that, um, yeah, on
 </span>
 <span data-rw-start="3448.079" data-rw-transcript-version="2">
 that. How do we deal with all these AI
 </span>
 <span data-rw-start="3450.24" data-rw-transcript-version="2">
 slop, then, in the future? That, uh, all the
 </span>
 <span data-rw-start="3454" data-rw-transcript-version="2">
 pull requests that are generated and
 </span>
 <span data-rw-start="3457.839" data-rw-transcript-version="2">
 overwhelm the people that try to
 </span>
 <span data-rw-start="3459.76" data-rw-transcript-version="2">
 maintain the systems.
 </span>
</p>
<p>
 <span data-rw-start="3462.24" data-rw-transcript-version="2">
 Well, I mean, the famous example is curl
 </span>
 <span data-rw-start="3464.319" data-rw-transcript-version="2">
 stopped giving bug bounties because they
 </span>
 <span data-rw-start="3466.64" data-rw-transcript-version="2">
 got too many slop,
 </span>
 <span data-rw-start="3469.2" data-rw-transcript-version="2">
 furious security pull requests, whatever
 </span>
 <span data-rw-start="3473.2" data-rw-transcript-version="2">
 things. So, yeah, I don't think we
 </span>
 <span data-rw-start="3476.48" data-rw-transcript-version="2">
 there's a lot of these problems that the AI being so cheap now to
 </span>
 <span data-rw-start="3478.16" data-rw-transcript-version="2">
 generate code to generate pull requests.
 </span>
</p>
<p>
 <span data-rw-start="3482.48" data-rw-transcript-version="2">
 Um, and there's a bunch of
 </span>
 <span data-rw-start="3484.48" data-rw-transcript-version="2">
 problems being caused by that, and I
 </span>
 <span data-rw-start="3486.559" data-rw-transcript-version="2">
 don't think I have the answers, I'm
 </span>
 <span data-rw-start="3488.4" data-rw-transcript-version="2">
 afraid. So, uh, but yeah, it's, it's
 </span>
 <span data-rw-start="3491.359" data-rw-transcript-version="2">
 clear that we're moving into it,
 </span>
 <span data-rw-start="3493.68" data-rw-transcript-version="2">
 it's creating as many problems as it's
 </span>
 <span data-rw-start="3494.96" data-rw-transcript-version="2">
 probably solving.
 </span>
</p>
<p>
 <span data-rw-start="3497.92" data-rw-transcript-version="2">
 So, I'm running around facilitating
 </span>
 <span data-rw-start="3500.96" data-rw-transcript-version="2">
 retrospectives for a lot of different IT
 </span>
 <span data-rw-start="3503.52" data-rw-transcript-version="2">
 Companies around the world online and
 </span>
 <span data-rw-start="3505.76" data-rw-transcript-version="2">
 not, and one of the things that we're
 </span>
 <span data-rw-start="3507.119" data-rw-transcript-version="2">
 really discussing right now is how do we
 </span>
 <span data-rw-start="3509.2" data-rw-transcript-version="2">
 use AI within our team?
 </span>
</p>
<p>
 <span data-rw-start="3512.16" data-rw-transcript-version="2">
 And for those teams who are not already
 </span>
 <span data-rw-start="3514.319" data-rw-transcript-version="2">
 discussing it, I'm trying to
 </span>
 <span data-rw-start="3517.599" data-rw-transcript-version="2">
 encourage them to discuss how are we
 </span>
 <span data-rw-start="3519.839" data-rw-transcript-version="2">
 using AI in our team, trying it out as
 </span>
 <span data-rw-start="3522.559" data-rw-transcript-version="2">
 you said, Bikita, try it out everybody, and
 </span>
 <span data-rw-start="3524.88" data-rw-transcript-version="2">
 talk about your experience.
 </span>
</p>
<p>
 <span data-rw-start="3526.319" data-rw-transcript-version="2">
 Experiences, talk to each other, talk
 </span>
 <span data-rw-start="3527.839" data-rw-transcript-version="2">
 about how you use it, how you want to
 </span>
 <span data-rw-start="3529.359" data-rw-transcript-version="2">
 use it. Because the things that I see
 </span>
 <span data-rw-start="3531.28" data-rw-transcript-version="2">
 right now is it's really bad in a team
 </span>
 <span data-rw-start="3533.68" data-rw-transcript-version="2">
 if some people in the team are using it
 </span>
 <span data-rw-start="3535.76" data-rw-transcript-version="2">
 in one way, and other people are
 </span>
 <span data-rw-start="3537.2" data-rw-transcript-version="2">
 expecting them to use it in a different
 </span>
 <span data-rw-start="3538.88" data-rw-transcript-version="2">
 way. That's the worst. So, continue to
 </span>
 <span data-rw-start="3541.119" data-rw-transcript-version="2">
 communicate and try it out. I think, is
 </span>
 <span data-rw-start="3542.88" data-rw-transcript-version="2">
 what I would say in general.
 </span>
</p>
<p>
 <span data-rw-start="3546.88" data-rw-transcript-version="2">
 &gt;&gt; Yeah. And, and that kind of um architect
 </span>
 <span data-rw-start="3550.16" data-rw-transcript-version="2">
 I spoke to recently was like monitoring
 </span>
 <span data-rw-start="3552" data-rw-transcript-version="2">
 who was using the AI the most, and it was
 </span>
 <span data-rw-start="3554.4" data-rw-transcript-version="2">
 the most junior developers who were using it
 </span>
 <span data-rw-start="3556.4" data-rw-transcript-version="2">
 the most, and that was kind of worrying.
 </span>
</p>
<p>
 <span data-rw-start="3558.72" data-rw-transcript-version="2">
 It's like, um, yeah, and there needs to
 </span>
 <span data-rw-start="3562.16" data-rw-transcript-version="2">
 be some consistency in how
 </span>
 <span data-rw-start="3564.079" data-rw-transcript-version="2">
 development teams agree to use these
 </span>
 <span data-rw-start="3565.76" data-rw-transcript-version="2">
 tools because otherwise they're going to
 </span>
 <span data-rw-start="3567.599" data-rw-transcript-version="2">
 be, uh, delivering slop to one another, and
 </span>
 <span data-rw-start="3569.839" data-rw-transcript-version="2">
 it's going to cause a lot of, kind of, the
 </span>
 <span data-rw-start="3572" data-rw-transcript-version="2">
 same kind of tension that the Carl
 </span>
 <span data-rw-start="3573.76" data-rw-transcript-version="2">
 project is getting now. You know, I, I
 </span>
 <span data-rw-start="3575.52" data-rw-transcript-version="2">
 am not reviewing this. That's a 40,000-line
 </span>
 <span data-rw-start="3577.599" data-rw-transcript-version="2">
 pull request. Go away. Yeah,
 </span>
 <span data-rw-start="3582.64" data-rw-transcript-version="2">
 &gt;&gt; It comes to my mind, something you
 </span>
 <span data-rw-start="3584.16" data-rw-transcript-version="2">
 mentioned some weeks ago, but like, is
 </span>
 <span data-rw-start="3588.48" data-rw-transcript-version="2">
 the value they are creating worth the
 </span>
 <span data-rw-start="3590.96" data-rw-transcript-version="2">
 money we are spending, right? Because
 </span>
 <span data-rw-start="3592.799" data-rw-transcript-version="2">
 right now, it's cheap to create all these
 </span>
 <span data-rw-start="3595.44" data-rw-transcript-version="2">
 pull requests, but how long will they be
 </span>
 <span data-rw-start="3598.4" data-rw-transcript-version="2">
 as cheap as they are? And like, I think
 </span>
 <span data-rw-start="3601.44" data-rw-transcript-version="2">
 maybe currently, it's nice just to try
 </span>
 <span data-rw-start="3603.28" data-rw-transcript-version="2">
 out everything and just do all of that,
 </span>
 <span data-rw-start="3604.88" data-rw-transcript-version="2">
 but the question is, how long are we
 </span>
 <span data-rw-start="3606.72" data-rw-transcript-version="2">
 still spending time to do things? And the
 </span>
 <span data-rw-start="3609.76" data-rw-transcript-version="2">
 question is, if the money answers at one
 </span>
 <span data-rw-start="3611.76" data-rw-transcript-version="2">
 point, maybe the question, and we don't
 </span>
 <span data-rw-start="3614.799" data-rw-transcript-version="2">
 produce just anything because we can, but
 </span>
 <span data-rw-start="3618.079" data-rw-transcript-version="2">
 because it will be too expensive at one.
 </span>
</p>
<p>
 <span data-rw-start="3619.68" data-rw-transcript-version="2">
 Point, it's at least a tiny hope at one
 </span>
 <span data-rw-start="3622.799" data-rw-transcript-version="2">
 point, but it will become too expensive.
 </span>
 <span data-rw-start="3626.319" data-rw-transcript-version="2">
 &gt;&gt;&gt; I don't have an answer to the question.
 </span>
 <span data-rw-start="3627.68" data-rw-transcript-version="2">
 I have a really, what I thought was an
 </span>
 <span data-rw-start="3630.319" data-rw-transcript-version="2">
 insightful reframing of it. Um, which is
 </span>
 <span data-rw-start="3633.359" data-rw-transcript-version="2">
 Mitch Hashimoto. He's he, he wrote all of
 </span>
 <span data-rw-start="3637.119" data-rw-transcript-version="2">
 the Hashi, well, he started all the Hashi
 </span>
 <span data-rw-start="3638.96" data-rw-transcript-version="2">
 core stuff, so Terraform, Vault, Console,
 </span>
 <span data-rw-start="3641.839" data-rw-transcript-version="2">
 all these amazing bits of software.
 </span>
</p>
<p>
 <span data-rw-start="3644.48" data-rw-transcript-version="2">
 Recently, he's been writing a terminal
 </span>
 <span data-rw-start="3646.079" data-rw-transcript-version="2">
 emulator called Ghosty, and I use it, and
 </span>
 <span data-rw-start="3648.48" data-rw-transcript-version="2">
 it's brilliant. His observation, he
 </span>
 <span data-rw-start="3652.079" data-rw-transcript-version="2">
 said, particularly in the PR world of
 </span>
 <span data-rw-start="3654.16" data-rw-transcript-version="2">
 open source, is that we've had to move
 </span>
 <span data-rw-start="3657.68" data-rw-transcript-version="2">
 from a, uh, a default accept model to a
 </span>
 <span data-rw-start="3661.68" data-rw-transcript-version="2">
 default deny model. Mhm.
 </span>
</p>
<p>
 <span data-rw-start="3663.92" data-rw-transcript-version="2">
 &gt;&gt; So, you know, the default is someone
 </span>
 <span data-rw-start="3666.4" data-rw-transcript-version="2">
 submits a PR; they do it with good intent,
 </span>
 <span data-rw-start="3668.799" data-rw-transcript-version="2">
 you know, positive intent, and there's
 </span>
 <span data-rw-start="3671.04" data-rw-transcript-version="2">
 almost like there's a proof of work
 </span>
 <span data-rw-start="3672.72" data-rw-transcript-version="2">
 element to it, right? They had to do some
 </span>
 <span data-rw-start="3674.64" data-rw-transcript-version="2">
 work to write, to create, to make the
 </span>
 <span data-rw-start="3676.96" data-rw-transcript-version="2">
 change. Pull the pull request, fill it in,
 </span>
 <span data-rw-start="3679.599" data-rw-transcript-version="2">
 so, you can generally assume good intent,
 </span>
 <span data-rw-start="3682.72" data-rw-transcript-version="2">
 right? Or well-disguised malice, yeah, but
 </span>
 <span data-rw-start="3685.839" data-rw-transcript-version="2">
 It's a human being in there doing stuff
 </span>
 <span data-rw-start="3687.76" data-rw-transcript-version="2">
 when it's all AI generated.
 </span>
</p>
<p>
 <span data-rw-start="3691.119" data-rw-transcript-version="2">
 Um, then you have to assume the default
 </span>
 <span data-rw-start="3695.2" data-rw-transcript-version="2">
 has to be denied until someone can—until
 </span>
 <span data-rw-start="3697.28" data-rw-transcript-version="2">
 a PR contributor can prove its, uh,
 </span>
 <span data-rw-start="3701.68" data-rw-transcript-version="2">
 worth if you like, and he's
 </span>
 <span data-rw-start="3704.88" data-rw-transcript-version="2">
 started a new open-source project called
 </span>
 <span data-rw-start="3706.48" data-rw-transcript-version="2">
 Vouch, and Vouch is effectively a web of
 </span>
 <span data-rw-start="3709.44" data-rw-transcript-version="2">
 trust for open-source projects to then
 </span>
 <span data-rw-start="3712.799" data-rw-transcript-version="2">
 vouch for contributors. You can
 </span>
 <span data-rw-start="3714.96" data-rw-transcript-version="2">
 either vouch for someone who's a
 </span>
 <span data-rw-start="3716.88" data-rw-transcript-version="2">
 committer or a contributor, or you can, uh
 </span>
 <span data-rw-start="3719.839" data-rw-transcript-version="2">
 accept someone else's vouch list. So I go
 </span>
 <span data-rw-start="3721.839" data-rw-transcript-version="2">
 to Emily's project, and she's got a
 </span>
 <span data-rw-start="3723.839" data-rw-transcript-version="2">
 really good vouch list of loads of
 </span>
 <span data-rw-start="3725.2" data-rw-transcript-version="2">
 contributors, and I subscribe to that
 </span>
 <span data-rw-start="3727.68" data-rw-transcript-version="2">
 list. So, where, so, so, his, his counter is
 </span>
 <span data-rw-start="3730.88" data-rw-transcript-version="2">
 to start creating a web of trust where
 </span>
 <span data-rw-start="3733.119" data-rw-transcript-version="2">
 we assume default deny, and then unless
 </span>
 <span data-rw-start="3737.359" data-rw-transcript-version="2">
 you're vouched for, and I, I don't know if
 </span>
 <span data-rw-start="3740.319" data-rw-transcript-version="2">
 that's the model—it's a model. I suspect
 </span>
 <span data-rw-start="3742.48" data-rw-transcript-version="2">
 there's going to be an awful lot more
 </span>
 <span data-rw-start="3743.92" data-rw-transcript-version="2">
 hard thinking in that space.
 </span>
</p>
<p>
 <span data-rw-start="3746.559" data-rw-transcript-version="2">
 &gt;&gt; Thank you. One more shot. Yeah.
 </span>
</p>
<p>
 <span data-rw-start="3749.2" data-rw-transcript-version="2">
 &gt;&gt; Yeah. And it's a little bit... Yeah. I
 </span>
 <span data-rw-start="3751.119" data-rw-transcript-version="2">
 Don't know if heartbreaking or
 </span>
 <span data-rw-start="3752.72" data-rw-transcript-version="2">
 something. I mean, these models and the
 </span>
 <span data-rw-start="3754.16" data-rw-transcript-version="2">
 coding capabilities only exist because
 </span>
 <span data-rw-start="3756.16" data-rw-transcript-version="2">
 so many people spend so much of their
 </span>
 <span data-rw-start="3757.839" data-rw-transcript-version="2">
 free time over years like contributing
 </span>
 <span data-rw-start="3760.319" data-rw-transcript-version="2">
 to this foundation that we have, right?
 </span>
</p>
<p>
 <span data-rw-start="3762.88" data-rw-transcript-version="2">
 And something like this vouch might
 </span>
 <span data-rw-start="3764.96" data-rw-transcript-version="2">
 actually make it more exclusionary and
 </span>
 <span data-rw-start="3767.2" data-rw-transcript-version="2">
 harder for people to get into this to
 </span>
 <span data-rw-start="3768.88" data-rw-transcript-version="2">
 contribute and all of that because you
 </span>
 <span data-rw-start="3770.48" data-rw-transcript-version="2">
 have to like get into this network and
 </span>
 <span data-rw-start="3773.04" data-rw-transcript-version="2">
 you have to like somebody has to vouch
 </span>
 <span data-rw-start="3774.4" data-rw-transcript-version="2">
 for you at some point, right? And so in
 </span>
 <span data-rw-start="3775.92" data-rw-transcript-version="2">
 a way it's like also
 </span>
 <span data-rw-start="3778.24" data-rw-transcript-version="2">
 yeah, heartbreaking in a way [laughter],
 </span>
 <span data-rw-start="3780.319" data-rw-transcript-version="2">
 but
 </span>
 <span data-rw-start="3781.04" data-rw-transcript-version="2">
 &gt;&gt; Yeah, I don't know. Sorry, that
 </span>
 <span data-rw-start="3782.799" data-rw-transcript-version="2">
 &gt;&gt; Yeah, those have to be the last. I'm just
 </span>
 <span data-rw-start="3784.799" data-rw-transcript-version="2">
 trying to find last words, and I'm now
 </span>
 <span data-rw-start="3787.28" data-rw-transcript-version="2">
 getting from default deny mode to
 </span>
 <span data-rw-start="3789.839" data-rw-transcript-version="2">
 heartbreaking [laughter], which is really
 </span>
 <span data-rw-start="3792.799" data-rw-transcript-version="2">
 really low to get. Uh, to this, maybe I
 </span>
 <span data-rw-start="3796.64" data-rw-transcript-version="2">
 should have stopped when I said
 </span>
 <span data-rw-start="3798.24" data-rw-transcript-version="2">
 something about, uh, yeah, try the things
 </span>
 <span data-rw-start="3800.319" data-rw-transcript-version="2">
 and learn, uh, the stuff, and
 </span>
 <span data-rw-start="3802.72" data-rw-transcript-version="2">
 Experiment, uh, with everything because we
 </span>
 <span data-rw-start="3806.079" data-rw-transcript-version="2">
 it will change, and we all need to
 </span>
 <span data-rw-start="3808.319" data-rw-transcript-version="2">
 learn how it will work. I'm trying to
 </span>
 <span data-rw-start="3810.319" data-rw-transcript-version="2">
 stick with that now.
 </span>
</p>
<p>
 <span data-rw-start="3811.2" data-rw-transcript-version="2">
 &gt;&gt; There's lots of exciting stuff as well
 </span>
 <span data-rw-start="3812.799" data-rw-transcript-version="2">
 like that's a lot.
 </span>
</p>
<p>
 <span data-rw-start="3814.079" data-rw-transcript-version="2">
 &gt;&gt; Lots of people rediscover their
 </span>
 <span data-rw-start="3815.52" data-rw-transcript-version="2">
 excitement in some stuff. So [laughter].
 </span>
</p>
<p>
 <span data-rw-start="3818" data-rw-transcript-version="2">
 &gt;&gt; Thank you very much for that. Okay,
 </span>
 <span data-rw-start="3820.319" data-rw-transcript-version="2">
 thanks a lot. Uh, I think that was, I
 </span>
 <span data-rw-start="3822.72" data-rw-transcript-version="2">
 hopefully also for everybody here, a very
 </span>
 <span data-rw-start="3824.88" data-rw-transcript-version="2">
 interesting discussion with some food
 </span>
 <span data-rw-start="3826.96" data-rw-transcript-version="2">
 for thought, and uh, now enjoy some more
 </span>
 <span data-rw-start="3831.2" data-rw-transcript-version="2">
 drinks. Thank you.
 </span>
</p>
<p>
 <span data-rw-start="3833.759" data-rw-transcript-version="2">
 &gt;&gt; [applause]
 </span>
</p>