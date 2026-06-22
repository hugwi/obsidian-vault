---
title: "Code Remix Weekly | Better grep, better agents"
source: "https://www.youtube.com/watch?v=yggJTecOl1k&t=543s"
author:
  - "[[youtube.com]]"
published: 2026-04-23
created: 2026-06-08
description: "Bryan Friedman from Moderne is showing why grep and IDE features fall short when you're working across large, decentralized codebases. Traditional tools can'..."
tags:
  - "to-process"
  - dev-tools
---
![](https://www.youtube.com/watch?v=yggJTecOl1k)

Bryan Friedman from Moderne is showing why grep and IDE features fall short when you're working across large, decentralized codebases. Traditional tools can'...

## Transcript

**0:54** · Hello and welcome to another edition of Code Remix Weekly. I'm your usual host Sam and with me is your other usual host Tim to be. How you doing, Tim?

**1:03** · I'm doing just fine. I I look and sound completely different than normal as you might notice. Yeah, yeah. How are How are the Netherlands this time of year?

**1:12** · Mhm.

**1:13** · I have no I actually have no idea. I can't even make anything up. I've never been to the Netherlands Netherlands.

**1:18** · Well, that's I I have been to the Netherlands and it's it's beautiful but flat.

**1:22** · Okay. And in in danger of in danger of being flooded it's so flat like by the ocean. Oh, got you. Okay.

**1:29** · At least it's somewhere nice. Of course I'm not Tim. It's This is Brian. How's it going everybody?

**1:34** · What? Okay, well, this is pretty it's it's pretty beyond the pale of you to misrepresent yourself that way, Tim.

**1:42** · I mean, Brian.

**1:44** · Well, we're there I mean, we're really really coming out the gate strong on a on a foundation of of lies and deception. So, I where we where we go from here it's already oof.

**1:54** · Everybody was completely fooled for at least a whole minute. I don't know. Okay, fine. So, you're Brian. Uh that's that's good. Tim is Tim is as usual at a conference. I think uh I think uh this one is in uh I think he's in France right now. I'm trying to keep up. Paris, yeah. Paris is very nice. Have you been to Paris? I have been to Paris. Lots of good food and Yeah.

**2:22** · and beautiful things.

**2:23** · Yeah, for sure. The uh I've been to I've been to Paris twice. Uh Tim often imitated but never duplicated. Yeah, everyone's trying to trying to copy Tim. I don't know. It's uh it's it it's it must be a compulsion cuz he's so he's so clever and handsome.

**2:38** · Everyone just wants to be him. But yeah, I've I've remember going to Paris a couple times uh and uh once was before they had banned uh kind of cars or most cars from like their downtown like so you know, core area. And once was after and I got to say it was a much nicer city to be a pedestrian in and and and walk around and see the sights and ride on bikes after like noticeably less air pollution and such. When was the last time you were in France? Was it before or after they had had made that change?

**3:06** · It was after that, yeah. We heard about it. People Some people who were really happy about it and some people who were complaining about it as as as ever but um As ever.

**3:15** · Yeah. Yeah, the the the my first impression of Paris the first time I went was how uh aggressive and angry the drivers were cuz the traffic was very densely gridlocked and everybody was mad about it, you know, and and and uh so there was lots of lots of honking and even some swearing out of windows between, you know, taxi drivers and such. So, uh All right, let's get into the announces for this week and then we can get on to our main subject.

**3:47** · First thing, new Open Rear release 8.80. That feels kind of auspicious. Maybe we can get a few patch releases in there and get an eight. But, you know, this is this would like my birthday is 7 8 88 and there's like if my parents had had me in August instead of July, I could have gone 8 8 88 and that would have been fun, but it didn't happen in this timeline.

**4:11** · Uh presumably that other timeline is better in every way. Um mostly bug fixes in this release, uh although there's a lot of changes into downstream recipe modules as well. Uh so, look forward to that. I'll probably get a tweet out about it at some point if we haven't already. We've got a new article on the Modding blog. I'm just going to put a link in the chat here.

**4:33** · Uh about finding every way a Spring controller commits a response too early about a big kind of CVE that popped up recently that a lot of companies are scrambling to fix and this is talking about how um how to use the taint analysis and data flow capabilities in Open Rewrite and the uh recipe module we've put out specifically for this fix in order to uh find and remediate it. So, if you are using Spring applications, you might well be vulnerable to this.

**5:07** · So, it would be a good idea to go read this article and run that recipe and uh not have all of your applications get uh you know, turn into Bitcoin mines or what have you uh by whoever might come across them and notice them being unpatched. So, uh yeah, excellent article to read.

**5:26** · And then this, here we go. This is uh local Modding MCP deterministic tools for coding agents by I'm not sure who this is, Brian Friedeman. I don't know. Some some strange guy.

**5:39** · Yeah, it must be some new guy. Never heard of him. Um but, I'm sure it's a great article and relevant to today's uh code remix discussion. So, uh I think Brian will be telling us all about that shortly and about how, you know, you can integrate the Modern CLI with your coding agents and make both better and more powerful in the process.

**6:04** · So, let's see.

**6:07** · And on a kind of a related theme, we have this upcoming don't blame the agent, blame the context webinar that you can register to attend. It is a a free webinar and this will show how you can make your agents better and faster.

**6:23** · I've certainly had the experience of, you know, repeatedly firing up agents in the same repository to tackle different different issues then seeing them always begin with a lot of like some very similar grepping and slurping up of of context and that takes time and tokens. And so, if anything could cut down on that, they could get to work faster and better. And I don't know, do you have any any remarks on this, Brian? It seems like you're a featured speaker.

**6:53** · I'm saving it all for tomorrow. You got to come come check out the webinar. So. All right. Well, yeah, go sign up for this right now so that you can attend tomorrow. Yeah. Yeah, excellent sound effect. And and learn all about it.

**7:08** · Okay.

**7:09** · We also have an upcoming introduction open rewrite training coming up Tuesday, April 28th. This is also a webinar. And let's see. And this will be Tim and Merlin. So, just seeing that it's them listed and not me makes me suspect that this is probably in a yeah, a Europe-convenient time zone. 11:00 a.m. you know, EDT. So, if you uh if you're in the US, this might work okay for you in the East Coast. West Coast, probably not unless you're a real early bird.

**7:39** · But, if this time doesn't work for you, fret not. There will be more. Okay. So, I think that is all of the kind of announcements that we have for the week in terms of new stuff. So, Brian, welcome welcoming into the program. I understand you're now you're now tied for our second second most recurring guest.

**8:02** · Yes, I was right on Thank you. Thank you. Thank you. I am I was right on Kevin's heels, but he was on a couple weeks ago and he beat me, so. Yeah. And and you'll and you'll still have to catch up cuz like I was mentioning earlier, Kevin participates actively enough in the comments most streams that that he wins a tie. So, you'll have to appear two more times to to get ahead of Kevin.

**8:24** · Yeah.

**8:24** · And I know that's I know this is what's most important to you, your position the position in that leaderboard. This is the reason I'm here. Yeah. Yeah, absolutely. Very good. Very wise.

**8:34** · Um so, so what what what brings you here today? What's a What's a trigrep?

**8:39** · What What is a trigrep? Well, um yeah, we announced this a couple months ago and it's it's an index. So, actually, I was on this very show um a few few months ago now, I think it was, talking about semantic code search and we were running some really helpful semantic code search recipes like find types and find deprecated uses and all these different kinds of recipes to do searches.

**9:10** · Um But, now with trigrep there's also capability to do searches without even having to run a recipe just based off of a of an index, which they call a trigram index, hence the name trigrep. Um and so not just running grep three times. Well, I mean, you could run grep three times, but you're going to get the same response and you're just going to take three times as long.

**9:36** · Okay, fair enough. Yeah. But uh but yeah, so that that's that's the the secret behind the name. It's it's based on the trigram index, which is actually like a technology that's that's been used in many code search tools. Like I know Git I believe GitHub search uses it. It's sort of like um a very effective way to search big swaths of or big code bases. Um Yeah. But you're not going to Yeah.

**10:00** · Aware like it gives you ways Is this Is this type aware? Does this know Does this take into account what types of objects are? What How does this Like help me help me kind of understand where this sits between a pure text-based search and between running a recipe?

**10:15** · Perfect. Yeah, that's where That's where I was headed next. So, I think um I was just saying it's used in, you know, other other places. Um in those places, I think it's essentially just, you know, text search. It doesn't have that much more uh um information. Um does have I guess there's a little bit about struct- some of the structural searches, which we can talk about that as well.

**10:37** · Um but in in the case of uh trigrep, we actually have even more information because it's built on the loss of semantic tree. So, it's actually does have some type awareness. Um it does not have the full semantic power of a recipe necessarily, but it does have more than your average uh code search and certainly more than your your average text search. Mhm. Mhm.

**11:01** · Okay, cool. And um How How How do I do it? How do I do a a trigram a trigrep search?

**11:15** · How do we do it? Well, um there's a couple different ways, and we can show uh we can show in a demo certainly. Um right now it's available in the modern CLI, so you can just run a mod search command.

**11:27** · Um after Essentially, what happens is after an LST is built, once you have a built LST, you can just run a um a command to quickly build the search index. And once you've got that, you can just run mod search. And um so we can show some examples of how that looks.

**11:42** · Um and then the other way is uh you know, this is actually quite turns out to be quite a helpful tool for agents to use because um in case you haven't noticed, if you code with agents a lot, and I'm sure you can speak very much to this, Sam.

**11:56** · Uh agents search code a lot. They search code, they grep code, they recode quite frequently to understand what they you know, what they're trying to do, what they need to do. So, it turns out that try grep is actually a quite an effective tool for uh for agents as well to do more um uh more efficient searches because they will get, you know, sort of the same uh even even a little bit faster, certainly, than than just your average your regular grep, but it's also getting back that type in some of that type information.

**12:26** · So, it can actually limit the amount of like full scans and full reads that it has to do on top of that. So, faster search, fewer tokens. That sounds pretty good. Let's uh let's let's see it. It's a common theme. Okay. Cool. So, let's uh let me start with We've got to build up to the agent. So, let let's just start with that basic mod search. Uh Yeah, yeah. Let's start with the mod search. Yeah.

**12:53** · Window.

**12:56** · Terminal.

**12:57** · Okay. Cool.

**13:01** · Um all right. I've got a a a white terminal for us today, so we can see perhaps a little bit better.

**13:07** · Um How unusual. I feel like this I feel like there's something unnatural and and and subtly wrong about a white terminal, but I'll I'll try not to let that distract me from the the content of your presentation. Yeah, thank you. It it does it does uh does feel a little unnatural, but I've found that the the dark terminal is sometimes hard to hard to see on video, so For sure.

**13:29** · Yeah. So, I've got a a set of um Let's just show you that there's nothing magic happening here, but um I've already synced uh you know, a number of repositories into this directory, so um these all have been synced and um LSTs have been built, and we've already indexed with search, so we can easily just do sort of a mod search.

**13:55** · And we can just do something basic like let's find anybody who's maybe has written to do comments in various places. This is just like basic string matching. This is not doing anything super uh complicated uh But it was quite fast.

**14:09** · It's matching, but it was quite fast, and you can see it actually um unlike, you know, if you run grep, you're going to get sort of one line. It'll tell you what line number it's on, but in this case, you're actually getting even more information. You're getting a little bit of additional context around what uh you know, around what is the result, as well as, you know, where the file is, and the line numbers. Yeah, this is nice for human readability or for agent readability as you get to see a little bit of a little bit of context uh to decide if that if that individual result is relevant or not.

**14:39** · Absolutely. Um and of course, I'm going to copy a regex cuz I don't want to fumble it, but we can also do um things like this like if we want to do find whatever by uh methods, um they can you do a sort of a regex search which will show us like find specialty by ID, find pet type by ID, find visit by ID. So, basic regex searches are are also possible.

**15:06** · Um Now, this is the this is sort of the the cooler example. We were talking about how it has uh type search. Mhm. type awareness, right? So, we can use this this uh SYM, which is of course stands for symbol, and say, "Hey, show me all of the actual places that the clinic service type shows up as a symbol."

**15:29** · And so, it's actually look you can see it's actually showing you the functions that also return that type. And it's got anything that's related to that symbol is all here.

**15:43** · So, that's go to the query for that was again?

**15:46** · Just like press up in your terminal. I just want to see what Okay, yeah. So, it's sim colon and the type name. All right, that's pretty handy. Yeah, and you can also do things like um Wait, why is it why is it highlighting these these these void functions? Where where is clinic service related to those? I believe they return I believe they are um Well, they're type void.

**16:08** · They don't return anything. Is there something inside them that that has a clinic service in it? That's a great question. Oh, it's just cuz these are part of class clinic service test.

**16:18** · Yeah.

**16:18** · So, these guys exercise the clinic service in some way. Okay. Yes, that's right. Um the other thing you can do is things like uh I like this one a lot as well.

**16:29** · You can do things like extends, right?

**16:31** · So, um I think this one will work.

**16:35** · Nope.

**16:36** · Um person is perhaps a better one. Yeah, there we go. So, um yeah. So, any types that extend person, you're actually exposing those as well. So, that's coming from that type information uh as well.

**16:52** · Mhm. Mhm.

**16:54** · Um and then the other thing I'll show you here before we get into the agent piece is there's um the the concept of structural search. So, there's a syntax like I think it's called comby. I don't know how to pronounce it. c o m b y. Mhm.

**17:08** · And you can do sort of complicated um structural searches. So, it's not so much a semantic search because it doesn't necessarily know the code means, but it does allow you to find certain things. Like for example, if you wanted to find any empty catch blocks, this is a how it would look. So, you've got you know, you're telling it, "Hey, it's a structural search.

**17:31** · We want to find uh a catch. And we want to find something, you know, and this is where a type variable, and a variable name, and a block. Exactly. So, even more specific than a regex, which is which would just say like, "Hey, anything in between the print parens."

**17:45** · Here we can say where are there actual specific uh you know, empty empty catch blocks. And you can do other you can do other, you know, fun complicated things like uh you know, find empty array list collections. So, um anyway, so the structural search is really powerful. As you can see that you can sort of really get um granular as far as what you want to discover.

**18:17** · Yeah. Yeah, it's very cool. And so, you're saying so, we can wire this up to a coding agent so that it can do these fast searches and such. How do we How do we do that?

**18:26** · Yep. I got one more thing to show you before we get to that.

**18:28** · Okay.

**18:28** · Okay, please. So, yeah. So, so we were talking about semantic search earlier. And uh one of the nice things about this is you know, if you if you do need to get more accurate, you need to get sort of specific. This is you know, this has the potential, even though it knows a lot about types, um you know, more more about types than a regular text search. It does have the potential to give you some false positives, certain things that maybe you know, go beyond actual the the the level of detail that the recipe can can follow.

**18:58** · Mhm.

**18:58** · So, you can do some certain things where um you start with a trigraph search and sort of limit the scope. Let's say you have like 400 repositories or something instead of the eight that I have here or whatever it is. Right. Because all the commands you're showing us can be run over one repository or many. Right, and this is running over many, right? Mhm.

**19:17** · Mhm. Uh well, I guess this is even says five repositories. So, but if you have 500 repositories, Right.

**19:24** · and you want to run a semantic code search recipe, it's going to take could could take some time and it might find nothing in most of the repositories. So, if you wanted to say start with a trigraph search, um So, like if we wanted to find any uh any place where rest controller shows up, um we can start with that search and you're going to see it didn't show up in in in this repository, but it did show up in this repository.

**19:48** · Uh and looks like there's plenty of occurrences in here. Mhm.

**19:55** · And also up in here. So, now what we can do is we can say, "Okay, now we need to get even more specific. Um we need to we need to find anything where there's a rest controller annotation and I need I need this to be super accurate." So, I'm going to just going to run the find annotations recipe. Um And I see you're scoping it with this {dash} {dash} last search.

**20:18** · Exactly.

**20:18** · Right, so this last search instead of like last recipe run, you can say, "Hey, I'm going to do this against the last search." And what will happen is it will run the recipe, but you'll see it's skipping the repositories that didn't actually have any results.

**20:34** · Yeah.

**20:37** · Uh yeah. And so, this is the recipe output here uh for this one and for this recipe here, but here it skipped it. No search results were found. So, it didn't even it didn't even run waste sort of waste cycles on on that. So, that's a that's a pretty neat use case.

**20:54** · convenient getting to to getting even, you know, a recipe that finds no results is still, you know, iterating over all the files and and save capacity. So, if you can skip that, then uh yeah, you can make all of your recipe runs that much faster. That's great. Yeah. So, um all right. Now we can get to the the agent piece.

**21:13** · Um So, I think I can't remember if we've talked about Have you talked about You've talked about our agent tools and and sort of uh in install Yeah, we've talked about agent tools before, but you know, we we might as well kind of take it from the take it from the top. Yep. Okay, so Yeah, you Yeah, you bet. So, with uh we've got this config agent tools command.

**21:41** · Mhm.

**21:42** · Um that lets you install or uninstall uh various agent tools. So, if we just do a full install, it's going to kind of investigate and see what agents I've got and install those. And then important thing here is that we're going to show that I'm going to show off and use is this MCP server piece.

**22:03** · Mhm.

**22:04** · Because this basically means every time we launch a an agent uh session, it'll have access to a set of tools that give it access to um Maddern, and one of those tools is basically a trigraph search. So, if we go here, um let me get some example queries so we actually get something back.

**22:36** · Um well, we can just start with like you know, where does person show up?

**22:46** · So, this is like very explicitly asking for a search instead of asking for something uh more general where might actually use a search. It also kind of sounds like a like a small child asking a confused question. Where Where does person show up? Yeah, absolutely. Uh it's taking us taking us some time to think about this one.

**23:13** · It's a difficult question. Where does person show up? Person Person potentially shows up lots of places. I mean, there's there's billions of them, so it's Oh, you know what? Actually, this isn't even the This isn't even the pet clinic anymore. So, it might not even find person at all in in in this particular repository. It might not, yeah. It's uh But uh yeah, is the Netflix Eureka repository have any person? I guess we'll find out. Probably not.

**23:38** · Uh forgot which context I was in for a sec. Um It's so easy to do with uh with all of these IDE windows and and terminals floating around. Um I have I have been finding uh more success recently. Oh. I got to see if it just hasn't registered yet. I'm going to have to go and register them. Cool.

**24:03** · It's connected.

**24:08** · Um okay. Well, let's try it in a different repository.

**24:20** · Yeah, I got a pet clinic and data/mcp and Do you need to run something on the CLI to to like start the MCP server or that should start automatically on on the Mac, right?

**24:30** · start Should start automatically, yeah.

**24:32** · Yeah, this was, you know, definitely working when I tested it earlier, but this is the nature of live demos. That's how things go. Um I thought you could do that, but I guess I have to type it. So, why don't you Why don't you uh take a look at that? Unless we got a a question in the comments from someone who says, "I'm in the A agent building.

**24:53** · Wanted to know what kind of projects or skills does a team like you look for when hiring someone as a dev? Um So, one thing I want to be clear about is that we are not a company that creates large language models or and or the or the agents themselves. Uh what we are focused on is providing tools that agents and the humans who use agents uh can use to author software better.

**25:19** · So, if your interest is in like working on something like Claude itself, that's not a question I can really answer for you, although knowing something about linear algebra would probably help if you want to really get into the get it get into the guts of uh back propagations and what have you.

**25:38** · Now, as for working on agent tools, the question is kind of well, anything that uh anything that is useful to an agent, anything that an agent does slowly or poorly right now that you can create a tool that does it faster or more efficiently that that agent can be that could be described to that agent how to use um could be uh could be a good choice for that.

**26:06** · Uh So, hopefully that uh hopefully that helps out.

**26:11** · Yeah. All right.

**26:13** · So, did did did did we find where a person shows up? It did find it. Yeah, and and it actually you can see it called uh it called Maddern. It called the tool, the Trigrap tool.

**26:22** · All right. Can we do a control auto expand? I'm I'm curious to see what it what what's inside that. Okay, so this put together a couple Trigrap queries for a person in the in Java source files, and it was able to configure the output mode to list files with matches, and then it repeated that uh with output mode content. That's kind of interesting. I wonder I wonder what wonder the difference is. Why?

**26:52** · Interesting. Yeah. Cool.

**26:56** · If we Yeah, I'm not sure what the output mode Um All right, I'm just looking at the the content shows matching lines with optional context. Files with matches shows only file paths. There's your answer.

**27:12** · Yeah, I might have I might have expected that an AI agent might skip straight to straight to content as that gives it a little bit more to go off of, but I mean files with matches Yeah, and files with matches would be Um well, I guess let you know if you wanted the content, right? Cuz if you got a billion matches, like if you if this if this appeared in a ton of files, you might not want the content from all of them. Uh you know, just to just to Please start with just narrowing it down basically. Yeah. Yeah.

**27:44** · Yeah, so I think that first query was probably so it could figure out if it needed to narrow it down or not.

**27:50** · Yeah. Yeah.

**27:53** · Um so also, you know, we don't have to be as explicit as this. We could say like um you know what will change if I need to add a field to person?

**28:10** · Maybe it'll actually figure out what I meant by perons there, too. I think it'll figure out what you meant by perons. It's it's pretty good at typos, particularly when the word even intentionally used is you know, or um that you mistyped is is already kind of like in its context. Yeah, exactly. Yeah, no, it definitely. So you can see it's calling a Um It's calling a turn quite a bit. It's doing some queries.

**28:39** · And and what's pretty impressive not perons. I think I see it figured it out.

**28:44** · Um And you can see like that's pretty quick. It does It doesn't have to go read. We'll We'll do a I've got a sort of a comparison we can go take a look at, too, but it doesn't have to sort of read a bunch of files. It really only read one file and then used the tool to kind of figure out the rest. Mhm. Mhm. So, um yeah, so it's pretty powerful.

**29:06** · Um I think one of the things you said earlier, which is very true, is, you know, fewer tokens.

**29:12** · Right.

**29:13** · certainly we can see how that works in uh I was on a couple weeks ago here talking about Prethink with uh with Kevin when you guys were uh Yeah. traveling. Um and we sort of did a side-by-side demo where we said, "Okay, let's try it with Prethink, try it without Prethink, and kind of look at the token count."

**29:30** · So, I thought it might be fun to to try to do that again and only use try grep as the uh um Brian, I would love to see that. Okay, let's do it.

**29:41** · Uh and let's see if this is on the Eureka repository, so let's see if this works. Uh I'm going to ask, you know, "If I modify instance info class, what other classes and services would be affected?" And this side does not have try grep, so it's going to go do a whole bunch of searches and stuff. Let's see if this side does have try grep. It should.

**30:10** · So, you can see it's It's uh searching here. This is basically using grep. I'm probably having to restart this because most of Oh, no. There we go. It's looking for MCP, at least. So, yeah, look at this. This is the grep command. It's doing, you know, grep, and then it's going to uh it's probably going to end up reading a bunch of files after it finds those files as well.

**30:47** · Yeah, I would I would assume so. And uh it seems like on our on our right side, maybe it um it got slowed down by it deciding that it needed to uh enumerate the MCP servers that were available to it. Yeah, let me just start the whole thing again. I tried to make this easy on myself, but you have to watch me type a lot. Okay. Let's try this again.

**31:30** · And did we do anything to make sure that it was aware of the MCP servers in this session?

**31:37** · I see you calling it there. So, I guess it's decided it didn't need to enumerate its MCP uh resources this time. Yeah, I think I just had a stale session. That's what ended up happening.

**32:02** · Um so, you can see this took 2 minutes and 10 seconds and came back with a whole bunch of suggestions. This took 41 seconds. Um so, right away you can see that the time of course uh was um quite a bit less. But, we can also go and take a look at how many tokens it it uh it used up. So, this is the one without try grep.

**32:34** · This is the same tool I used last uh on on the last session to sort of count tokens from all of the all of the log files. Okay, so total tokens 1.6 million.

**32:46** · What do we have on this other side?

**32:58** · Quite considerably.

**33:00** · Yeah.

**33:00** · 250,000.

**33:02** · You know, I was I was seeing I was seeing it people saying online that bilingual programmers who know Chinese had been starting to prompt Claude and their agents in Mandarin instead as they were finding that it was Yeah, they're just finding that they could get similar results with like some you know, it wasn't super precisely

**33:27** · measured, but like let's say 30% fewer tokens, which could be real, you know, if you're paying for for API access and not one of these subscriptions, it could really matter how many how many tokens you're using. But this is this is much more dramatic than that.

**33:41** · true. Is that just because the there's just fewer characters in in Mandarin or is it what's the I mean, I I I can only speculate, but if I were to speculate, then it might be that an individual Mandarin character is more information dense than a single English word. That's what I mean.

**34:03** · you if you could express more stuff in fewer characters, that would translate to lower token usage. So uh that is that is my speculation, which is as unadulterated by any true knowledge of Mandarin or the inner workings of these LM systems. But that feels plausible. And in this day and age, isn't that the same as being true? 100%.

**34:28** · And then it actually makes me think about um, I've got uh two ki- two young kids. My I've got a 14-year-old uh, and a and 11-year-old and they it seems like that generation is all Almost got the ages wrong there. That was good. Your daughter is almost there. So, almost or whoever they are almost learning that you didn't love them or remember their age. Well, I just uh, it just seems like time goes by so fast.

**34:48** · That's why I can never keep track. But uh, it seems like that that younger generation is all about fitting as ma- as much information into as few characters as possible. It seems like they cannot text in complete sentences or even complete words. So, maybe they're they maybe they're perfectly efficient with agents. Yeah, exactly. Um, so yeah, anyway, this is uh, you know, pretty pretty dramatic difference. Um, I was going to say pretty big.

**35:15** · Yeah.

**35:15** · and which which repository is this in?

**35:17** · Was this in pet clinic? This is Eureka.

**35:19** · This was Eureka.

**35:20** · Eureka. Okay, that's that's that's a slightly larger project. Yeah, I would I would fully expect that this uh, the benefit here would only get more dramatic as the size of the repository increase. Right? Like cuz you just have to search through more and more files to try and find what you're looking for and you know, lots of people have have had the experience of being like, our our code base is really big and interconnected. AI agents kind of struggle to work with it. Right.

**35:46** · And uh, and tools like this that um, mean that you don't have to treat it like a blob of text, but can you know, present a little bit more information on the actual structure uh, to the agent helps to get better results more efficiently.

**36:05** · Yeah.

**36:06** · Yeah, wow. I've just uh, that's a that's a really dramatic difference in in token cost. Yeah, it's like that's like 1 uh, that's like 1/6 the And I know there's you know, there's different different tokens are you know, sort of worth different uh, amounts. There's obviously quite quite a bit We can see it's having to to read the cache uh, quite a bit more in particular, but but everything is is increased.

**36:28** · And it's interesting this this example didn't um didn't launch a sub-agent, but often times like you like you mentioned depending on the size of the repository, it will kick off a sub-agent and go explore and do a whole bunch more reads even than than this example did. Um so we've seen that we've seen that happen quite a bit as well. Yeah, that's really cool.

**36:52** · Yeah.

**36:53** · What uh do you have do you have any other any other cool demos to show us?

**36:58** · I mean, that was uh that was sort of the bulk of it. I wanted to lead up to this, you know, dramatic comparison. Uh so Yeah, and it is good. It is it is very dramatic. I just wanted to wanted to make sure that if you had anything else that we were were were taking that taking the time to to to give it its due.

**37:17** · Uh but yeah, this is this is this is really cool. I think there is a lot of a lot of potential here to make these agents better at the things that they are bad at, right? Agents are are they're so good at at at fuzzy tasks. It's the task that's stochastic tasks at at tasks where you want to guess and check a bunch of times or you want to try a bunch of different things and and keep what works.

**37:43** · Uh but where precision or correctness are uh are really important, you might want something deterministic. But deterministic tools lack the flexibility and the fuzziness of the stochastic tools. So if you can complement the stochastic tools with deterministic tools that uh that that address their weaknesses, then you can uh and you know, use the use the agents to for the the gaps where you don't have a deterministic tool, then you can uh get the best of both worlds a lot of the time.

**38:15** · And I think that's what we're what we're really looking to do, you know, get the get the correctness. Yeah, I the correctness, get the precision, get the comprehensiveness, and something deterministic, and make all of that rigor, precision, and speed available to the agents. That's right. And there's a vocabulary lesson in there, too, I think, Sam, cuz there's some good some good words.

**38:36** · Stochastic is a good word, right? It just means It just means It's just That's just a fancy way of saying kind of random. Yeah, that's good that's a good one. But yeah, that's No, that's exactly it. There's sort of this spectrum of speed versus accuracy, and like, you know, we've talked about before how the recipes are going to get you the most accurate most accurate results.

**38:58** · Um but this sort of helps bridge the gap for the for the agents. And for humans, too. I mean, you you I'm sure you've done your fair share of searching code.

**39:06** · Uh Oh, yeah.

**39:08** · You remember some some some quite bad code search tools that were still a godsend, like still so much better than nothing, years ago. And this And these are all so much better than that. Um Sorry, I'm still stuck on the word stochastic. Are you Are you a gambling man, Brian? Do you Do you like to go to go to Vegas, hit the craps, do a little blackjack?

**39:29** · I I will play blackjack from time to time. I'm more of a poker person. I like to play the the person, not the house so much. Yeah, yeah. Yeah, for sure. For sure. Well, the person doesn't necessarily have have a have a baked-in advantage like the like the house does.

**39:41** · Yeah, exactly. But what I was what I was going to say is if you ever needed to um creatively account for for your gambling losses, you you would say it's not gambling, it was it was stochastic finance.

**39:56** · Stochastic finance? Yeah.

**39:58** · That's good that's a good one.

**40:01** · Yeah. Many of Many of Vegas trips have have ended with stochastic finance.

**40:09** · Exactly. Exactly.

**40:11** · All right. Well, good stuff, Brian.

**40:14** · And do you want to take a second uh to tell the people about the about the class tomorrow. I mean, it sounds like this should be pretty thematically aligned with what you were discussing today, but in more depth, covering more things. Like should some Why should the people who are watching you here today go and rush and sign up for that to see you again tomorrow?

**40:35** · Well, so tomorrow we're talking specifically about pre-think, which has some of the same principles here. All right, you'll see similar dramatic difference to the compliments right?

**40:44** · Yeah, but but yes, I mean definitely complimentary. You could you could see even if you have pre-think, you're still going to have to search the code. So, maybe maybe the agent will use pre-think to find, you know, which files have certain characteristics and then use trigraph to to search those files and then use, you know, use its native tools to to go from there. So, yeah, so so tomorrow we're going to be talking specifically about pre-think, but we'll we'll take a look sort of at some similar use cases as this as well.

**41:17** · Right on. Yeah, so complimentary.

**41:20** · You could benefit from both and for similar reasons. So, if you liked what you saw about trigraph today, go check out the stuff on pre-think tomorrow or go watch the back episode of of code remix on YouTube where we where we talked about pre-think then or if you're just like really lazy but good at just showing up every Wednesday, I'm sure we'll talk about pre-think and these related technologies again because we're we're continuing to iterate.

**41:44** · There's already been additions to pre-think since since I was on this since Kevin and I talked about it particularly around some serious code quality metrics that pre-think has.

**41:55** · Yeah, yeah, I I I actually looked at some of those last week on the on the stream and I didn't have didn't have Tim or any other guest here. I I ran pre-think on some of our repositories and and looked through specifically the code quality metrics it came up with which I found which I found very interesting.

**42:12** · You can refer to last week's episode for for for all the details. But one one thing that was interesting was some of the the the metrics pointed to classes that were like very much designed to be that way.

**42:26** · Um, like both on like the high end and the low end of like coupling or coverage some of these some of these metrics. And um And yes, it was so so that was that was interesting for me seeing that the the metrics were like well, in a lot of cases this would be bad design, but that's but like in when I was looking at a particular it's like well, that's very much exactly how the visitor pattern is like designed to be implemented. Um And so there there are places where it is where it is intentional as well. So it's not necessarily specific.

**42:57** · Yeah.

**42:58** · Yeah, use case specific, design specific.

**43:01** · But it's the it's the kind of thing where you would definitely you definitely kind of learn about your code base by looking at looking at where these where these certain classes show up on these code quality metrics. And um Yeah, that's a it's an interesting subject to delve into. But I think for this week we'll we'll just about call it here. Thanks for thanks for coming on Brian. Yeah, you bet.

**43:22** · it's been a pleasure to have you. Thanks for having me. Yeah, see you next time. All right, see you all next time. Bye.

**43:28** · Bye.

**44:05** · I'm a G.

**44:30** · I'm a G.