---
title: "Jira and Linear are legacy software"
source: "https://m.youtube.com/watch?v=pzUn9wTCgcw&list=WL&index=3"
author: "Theo - t3․gg"
published: 2026-03-27
created: 2026-05-14
description: "The current shape of JIRA and Linear isn't going to last. \n\nThank you\"
tags:
  - to-process
  - dev-tools
---

If you're anything like me, you probably hate issue trackers, which is why it's so exciting to see them die. That said, I'm a little scared of what's next. I need to address something really quick though. You might have thought the thumbnail was clickbait. I know I use fake tweets sometimes to get your guys attention. This time it wasn't. Even Linear is saying that issue tracking is dead. Kind of crazy that they are trying to kill the industry category that they have been leading for a while, but I'm actually really excited about the direction that they're going in. They just posted an article all about this and I couldn't agree more. It seems like the future of development is not a pile 

of issues on Jira and Linear that you slowly go through as a team, and instead it's going to look and feel a lot different. It's really hard to say what the future's going to look like, but I'm excited to explore what Linear is working on. But there is something I know is useful right now. Today's sponsor. Two years ago I had a conversation that has stuck with me since. It was a conversation with Guillermo, the CEO of Vercel. We were talking about things that we did right and wrong with our businesses. And the thing that he said that shocked me is that he deeply regrets rolling his own off at Vercel. That might sound insane 

with a company the size of Vercel. Like, obviously you should be rolling your own everything. It's your platform, right? Well, it turns out there's a lot of problems when you own your off layer, and they're not things like setting up Google to sign in correctly as annoying as that is. Problems go deeper. What happens when real companies want to onboard onto your product and they don't have the weird niche expectations their IT team expects to make it so their business employees can sign into your service using their existing authentication. Spoiler, I'm not the only one Guillermo's had this conversation with. And as he says here, 

"I think we could have done even more business if we had partnered with WorkOS earlier. It's been incredibly well received." I'm sure you've guessed by now, but today's sponsor is WorkOS, the off platform used by OpenAI and Anthropic, Vercel, T3 Chat, and many, many more. WorkOS has found an incredible balance of developer experience and enterprise readiness, where they have everything you need to onboard these real companies. Never having to think about identity provision again is a gift from the heavens, and I am so thankful for WorkOS making it so that I never have to configure ADP again for the rest of my life. If that's all 

they offered it would be worth it, but there's so much more to the platform. AuthKit makes it really easy to set up the buttons and panels that you need for your users. MCP Auth means you can finally add authorization to your MCP servers. Directory sync makes it trivial for companies to keep things in sync between their dashboards and your product. Vault's one of the best ways to store user-specific encrypted values, things like API keys that they might be using in your service. And there's so much more to explore. Your next fear going to be the price cuz there's no way it can be that good for cheap, right? Well, you have nothing to worry about 

cuz the first million users are free. Get yourself enterprise ready at soidiv.link/workos. I'm very excited to read into what Linear is cooking here. You know they're cooking something different cuz this is the only not dark mode page I've ever seen Linear ship. They actually took the time to make it so when you read this particular page, it is light mode and they flipped the logo and everything in the top nav. They also did the usual Linear thing of trying way too hard in design for something that doesn't matter that much with the logo. You can move your cursor through like a fluid and click to pulse it. It's cool. It's very 

uh Linear of them. Anyways, issue tracking is dead. It was built for a handoff model of software development. A PM would scope the work, engineers would pick it up later, and the system was filled with prioritization, negotiation, and workflows to bridge the gap. That ceremony came from real constraints. Engineering time was scarce. Teams needed a way to route work carefully across roles and functions. Absolutely agree. This is my whole life when I was an engineer back at Twitch. It was the chaos of breaking up large piles of work into small tickets, throwing those into 

a queue, and then going through them, assigning them to people, and trying to guesstimate when all of the work necessary would be done to ship the thing they all lean into. But over time, complexity started to look like sophistication. The more process a system could absorb, the more advanced it seemed. Overhead kept growing and the process became work itself. Yep, my Jira dashboard back at Twitch would take over 2 minutes to load. Technically saying that is against the terms of service for Jira, but thankfully I have been out of Twitch for over 5 years now, so I can say whatever the [ \_\_ ] I want. Yeah, Jira 

ran like [ \_\_ ] garbage, and that was because we had filled it with so much complex [ \_\_ ] across the absurd number of tickets in different fields and data links across things at Twitch. And that's just what happens. When you have a system like this, every single feature is going to be used and abused until it breaks at the seams. People are confused about why I can't talk about Jira's performance. They did a terms of service update back in the day when I was at Twitch that explicitly banned 

talking about the performance characteristics of Jira and sharing benchmarks for its performance when I was at Twitch. But now it's been long enough that I will tell you guys Jira performs like [ \_\_ ] garbage at real companies. Also, yes, I do have Jira as a banned term on my switch streams because I thought it was funny to do. I might need to go remove that if one of the moderators can go figure out how to do that, please do. At least for now. Yeah, Jira, the correct spelling with the star. We need to not say the J-word if we can avoid it. Back to the article. Linear's always been built on the 

opposite belief, the opposite of the system continuing to grow and get more complex. The best systems should remove overhead so the teams can focus on building. That's absolutely how Linear felt. It felt like they were trying to remove as much weight as possible. So getting in, looking at the issues, filtering through things, and getting the data you need to go back to work was as easy as possible. And that's why so many engineers preferred Linear. It was kind of a bet on engineers being the ones who made important decisions at companies because Jira was the thing that product managers picked because that's who it was marketed to, to be clear. And Linear wanted something the 

engineers liked because they hated using Jira at the companies they were at. So they made Linear to make something nice and simple and elegant for enges, and it more than succeeded and is now doing quite well. I would bet they have a similar number of users and a significantly higher number of startups than a Jira ever has or will. But now we're in the AI era and things are changing fast. Again, their goal is to remove overhead and according to them, agents push the removal of that overhead even further. They can make software dev a lot simpler. Planning, implementation, and code review begin to compress as agents absorb more of the procedural 

work. You'll get to spend more time on intent, judgment, and taste, and less time managing the mechanics of the process. This one's particularly interesting to me because I actually kind of worked the same way when I was at Twitch. It was so common to have tickets that just didn't correctly estimate how hard things were and missed a bunch of subtasks that were important. And to be frank, I never read a spec that was written before the product was made that even came close to describing what the product actually would be, how it should be implemented, and how long 

it would take. It was almost always entirely inaccurate. So, what I did instead is I would go build a small version of what we were aiming for in 1 to 3 days just to force out whatever could let us test the UX. And through that process, I'd be able to identify any tech shortcomings we have to touch out of a very clear service area of things we have to know about and be involved in order to make this work. Out of a demoable, usable version of the product that we could use for testing both internally and in front of users when we brought users into the office. And through that, we were able to collect a ton of information in order to 

make sure that we steered the product and its design in the right direction. The result of this is that we could write way better specs because we actually had a rough idea of what the product would look like and how it would work. The more surprising part for me, though, was how often we would just ship that quickly built version. And to be very clear, the point of this process wasn't to get the feature out faster. It was to develop a working prototype of it to know what was required to do it and to make a better spec and most importantly, have a version that people could start testing to make sure this is 

even worth doing. And I would say about half the time we ended up slightly polishing that first pass and just shipping it because we had no reason to go much further with it. The amount of times I had a a that should have been a huge 20-page spec that we spent weeks writing and debating that just took me a few days and we ended up shipping as is is hilarious. To be frank, this hurt my career growth to an extent because we didn't have all these fancy documents we could point out during my promotion process that was built all around that [ \_\_ ] But it did make me pretty well regarded internally and this is still 

referred to as the Theo method or the Theo prototype at Twitch to this day. Depending on the team, of course, but a lot of teams still do things this way. I know I fully overhauled a handful of teams process around product design by just refusing to write a boring useless spec. There's nothing I hate more than useless [ \_\_ ] being done by engineers that doesn't even make them feel good. Engineers love useless [ \_\_ ] as long as it's inside of their terminal. They hate it when it's inside of Google Docs. So trying to get them away from those things and instead back into their editor was always beneficial. And it 

turns out a lot of people agree, they just weren't good enough devs to agree. Okay, I shouldn't say good cuz this is a different skill. There's a lot of very talented devs that don't build very fast. There's a lot of average devs that happen to build really fast. That's how I would have described myself when I was at Twitch. I was a okay to decent dev, but I was really good at trimming the fat, identifying where in the system we can insert the thing to make it way easier to build, and then building the thing. That was one of the things that made me unique. But it's also a capability that almost all engineers now have because of agents. Benefits and negatives. That said, I think that way 

of building is so much better. Make a first version of the thing, then make the spec, then build it correctly, rather than write a spec assuming you know how it will work, and build it wrong because you were incorrect with the spec, and then keep [ \_\_ ] throwing band-aids on it until it kind of works, and then you ship a broken thing. Hate that strategy. The first version of software will always be less than ideal. Do it first to figure it out, throw it away, and then make a good version after. Now that is much more viable. And it's nice to see Linear realizing the same thing, too. I almost feel as though these types of issues tracking systems 

discourage that type of exploration building because it's so valuable. According to Linear, the shift with agents is already underway. Coding agents are installed in more than 75% of Linear's enterprise workspaces. Not just side projects, not just people playing around with it. The enterprise deals they have with big businesses using them. 75% or more are already using agents as integrations in Linear. I bet you the other 25% are largely copy-pasting the issues into their agent of choice to get 

the code built. In the last 3 months, the volume of work completed by agents grew 5x. Do you understand how crazy that is in particular? That's the Opus 4.5 effect when people woke up to how powerful these models could be and the level of work they could get done. And obviously now with Codex, we can go even further. They also noted that agents authored nearly 25% of new issues, which is very interesting to me. I still haven't gotten into the letting AI make the issues side of things. I let them close them, but I don't let them open them yet. Maybe I need to get over that. 

In this new world, the next system is not designed around hand-offs. It's designed around context and agents. Agents aren't mind readers. They become useful through context. Customer feedback, internal ideas, strategic direction, decisions, and code all need to be captured in a system that humans and agents can work from together. Very interesting. That system should understand intent, route work to the right actor, escalate when needed, and keep execution moving. It should help teams move work forward, not trap them inside the process. The number of people 

I know whose jobs are effectively just using Linear or Jira is heartbreaking. Like those apps are good. Okay, one of those apps is good, but none of those apps are good enough to spend your day in them. As somebody who spends their day in email lately, I I empathize. And this is apparently what Linear plans to become. Linear is the shared product system that turns context into execution. That's a really cringe one-liner. I don't like that. I hope they rethink that. It holds feedback, intent, decisions, plans, and code, shapes that context into work, and helps 

humans and agents carry it all the way to production. So, you have customer requests, bug reports, and feedback. Those become the context with the plans, discussions, specs, all the above. That becomes rules that are used to actually command the agents within the context, like automation skills and permissions. That is handed to the agents, and the output is the product. Notice that there are no issues here. Notice that there is no sprint planning here. This is incentive, context, rules, developer, effectively. In order to get there, they just launched a bunch of new things. They have a linear agent that you can 

use to actually do a lot of the work against your context. They have a new skills product, which lets you codify things that are being done over and over. And then automations, which will allow you to automatically trigger things remotely. I'm assuming. Yeah, triage will trigger agent workflows the moment an issue enters the system. Every new issue adds context to your workspace, and Linear can now intelligently refine, synthesize, or take action on the context the moment it arrives. Cool. I think automations are more and more going to become like the next new thing. Do I not even have the Codex app installed on this computer? I 

don't. I just formatted this, and I've been using a a better app recently, believe it or not. Uh certain T3 code. I want to show a feature in here. Back in this lackluster, laggy app that broke my brain because of how cool it is to build this way, but just doesn't handle the scale that we build at, sadly. So, it does have some really cool things in it. I think the skills browser and creator thing is relatively cool. I've been able to make some useful things in this. It's not my favorite thing, but it's decent. I don't think the official OpenAI docs skill should be included by default. 

That's cringe. Happy I went to this page. I had a bunch of useless skills that were on by default. That is fixed now, though. But that's not the time I'm here for. I'm here for automations. I will be honest, I overlooked automations when I started using the Codex app, and I've noticed that most devs have as well. For whatever reason, devs just aren't as into this side of things. And I kind of get why. A lot of the examples are just not very good for developers. Like, what dev wants to summarize yesterday's get activity for a stand up? They don't, I promise you. What dev 

wants to synthesize this week's PRs, rollouts, and incidents and reviews into a weekly update? The kind that's not very good at coding and is on a quick path to become a PM or a designer of some form. And then release prep. Draft weekly release notes for merged PRs. Before tagging, verify change logs, migrations, feature flags, and tests. Let's say I want to set up one of these. I click it. I can set a schedule, so I can choose when I want it to fire. If I want it to fire daily at 9:00 a.m., I can choose what project it fires in. It will spin up a work tree and then go do 

the thing. You can even choose which model and reasoning levels with this really weird pinned thing there. God, I hate this UI. Whatever, you get the idea. This is a concept that I personally didn't think was the coolest thing ever. It wasn't a big, oh yeah, this is great. Something I learned recently is that there's an increasing number of non-devs using the Codex app lately. A lot of them are doing it because they have things on their computer that they wanted to be able to do, but even more using it from what I've seen because they love automations. 

I know a comms person at a startup that's using an automation to go check a bunch of different websites and news sources for mentions of their company in order to then bring it into Slack. So, the automation will fire, go find all of this info, and then DM her on Slack the results. And this person's never been a dev before. They had friends at the company using Codex app. They thought it was cool to check out, and they just fell in love with automations. They have like 30 plus of them now doing all sorts of [ \_\_ ] To normies, this is the first time they could automate part of their 

life or work. And I don't think most developers think this way because to an extent, we already learned how to automate things. That's why we're developers. But, we know work it is to automate things, so we often don't bother because writing the code to automate something like grabbing all of the commits that you did in the last week and dumping that as in some information to you on Slack or whatever. That's code all of us can write. We're all devs. Almost every single person watching this is good enough at writing code to do something like that. But, it's also a lot of work to do it. So, 

we've kind of trained our brains to ignore the urge to automate things that aren't super useful. People who have never had this experience before are all of a sudden able, and now that it's easier, they're doing it even more. I know way more people doing automations outside of the dev world than inside of it. And if I'm being frank, and this is not meant to be an insult, this is an observation, the devs I find who are using automations a lot, who are using open claw a lot, and using those types of things, tend to be the less good devs that I've worked with. No offense to these two particular people, but two of the actual worst devs I've ever seen in 

my life are open claw gods. One of them built their own equivalent of open claw before it came out, and it barely worked, and it resulted in her spam texting me dozens of times a day as she was trying to make it function at all. It's kind of weird. Them liking automations doesn't make them bad, but it almost seems like we as devs have wired our brain against this type of thing. And people who are less wired into the dev world are more wired in a way where they're willing to do this type of thing. So, while the linear automations that they're describing here might seem not that cool to us as devs, 

I know to me it's like my instinct is, "Oh, whatever. What is it actually going to add?" I promise you the PMs, the leads, the people who don't code are going to love this, and they're going to massage it into something useful almost certainly. I will say the end here is kind of cringe. These updates build on our early work in triage intelligence, deep integrations with cloud coding agents, and other AI tools. By grounding agents in the full context of your product and code base, we're collapsing the distance between an idea and its implementation. Issue tracking was built 

for hand-offs. Linear turns context into execution. So, here's my hot take. I personally not found much value in things like G stack. If you're not familiar, I might do a whole video on it in the near future. The point of G stack is it gives you a bunch of skills that are effectively different characters that are being played by the models to do specific types of things. Gary built these specialists. The CEO founder, the eng manager, the senior designer, the design partner. It should be clear, these aren't like code or anything 

complex. These are just markdown. These are just text files that describe how the model should behave in these times and in these particular requests. For what it is worth, I think this is [snorts] cringe as [ \_\_ ] There are some fun ideas in here like {slash} codex, which cuz this is built for Claude code. This will call the codex CLI from Claude code to review the changes and give a second pass saying, "Yeah, I'm codex. I think that's good or bad." Chat's already figured it out. So, this is how devs role play. Yeah. My hottest take is that the way we have broken up work 

historically only made sense because developers and other fields that we interfaced with were different enough and hard enough to find and level up in that we needed to have these roles so that we could get the work done and meet the quality bars that we needed to. But, let's be real here. If the model is smart enough to be the CEO, to be the eng manager, to be the designer, to be the design partner, to be the staff engineer, to be the debugger, to be a designer who also knows how to code, to be the QA lead and reporter. If the model is smart enough to be all of these things, why are we still defining these 

things? Why do we need to have a thing for this anymore? My hot take is that the way we have broken up all these pieces made sense when humans did it and a given human could only do one of these things. Now that AI is smart enough to do most of these things, the way we break up the work no longer makes sense. And I see this all over the place. One of the place I see it the most is multi-step planning processes. There's no reason for planning to take hours. 

There's no reason for planning to fill your entire context. There's no reason that planning should have lots of different sub plans and steps and process and specs and all of that [ \_\_ ] Models are for the most part good enough. So, instead of spending all of this time after you take in the request, bug report, or whatever, to build all of these additional pieces in for context, like the specs, technical design, the plans, the decisions, the summaries, and all that [ \_\_ ] just for the model to go do the build, why not have it start with a build but accessing all of these things as tools? What if 

the model could do a first pass, use these things, figure out what doesn't doesn't work, and then have the first pass be the plan, so to speak? Not that the code is going to be used directly, but the process of it building and touching all of those things is enough for you to realize, oh, I guess that's how this works. I guess that's where the flaws are. And then from there, make a much simpler plan that actually touches the things you need, and then go build it again. We've went through this loop already with MCP, funny enough, where we thought this new standard was going to be the best way for models to access 

data and do things, and then it sucked. So, we ended up moving it back to code, because it models are really good at writing code. And once the models could use code to use MCP, all of a sudden it got way, way better and way more performant and reliable. I think we're going to go through the same thing here. We're in a weird spot now, where we're going to reinvent everything based on how it always worked, even though it doesn't [ \_\_ ] matter. And what we're going to end up back at is code as planning. We're going to reinvent plans a million [ \_\_ ] times over the next year, and then we're going to just go 

back to code. I like what Naman had to say here. This is the functional versus product divisions at companies. I absolutely agree there. Here's a fun fact I learned recently. Did you know that GitHub has a separate product and engineering org? Did you know that they share zero leadership? That product and eng, the people who actually build the product, cannot interact with each other? Cuz I didn't know that until recently, and it explained a lot of why GitHub is a [ \_\_ ] disaster. I don't see how GitHub can ever get better if the product people don't code and the devs don't make product decisions. Kind of makes sense that GitHub is an 

absolute [ \_\_ ] [ \_\_ ] show. And if we keep pretending that way of building makes sense, we're going to keep reinventing shitty processes that only worked for humans. There is a way I could be wrong here though, and I don't know cuz I haven't done enough of this like code as planned type thing because I'm too busy to do either coding as a plan or coding in general. I have way too much [ \_\_ ] [ \_\_ ] going on. I do plan to do this, pun intended, but there is a potential failure case in the way I'm thinking of this that I am imagining now, which is that the reason agents can work better this way is because they're trained on data from humans and there's enough data of humans working this way 

that eventually the AI can do it too. Perhaps. And it might be better for the AI to behave like a human than for it to behave like an AI because the AI is trained on humans in the first place. Yeah. I don't think that will be the case though. I still pretty firmly believe that the best plan is a prototype and if you still need a plan after that, you'll be able to write a much more informed one after you make a first trial version of the thing. So instead of all of this nonsense, I would take the handful of useful pieces of context here, throw those into a tool call of some form, and then tell the model, "I want to build a scrappy 

prototype of this feature that was described in whatever request bug reporter feedback was provided. Help me identify the scope of this and then build this first version so that we can understand what foot guns and other shortcomings might exist in the code base as we implement this." You get this early version, you get a bunch of the things that were hard about it, and then you can go build the right one. I think that's probably going to be a better bet. I could be wrong, but having built with a lot of this [ \_\_ ] myself, that has been generally the direction that has worked for me. Hell, I've been building this way since before AI. I cannot tell 

you how many times I filed a shitty PR to one of our repos just to showcase the UX or DX that I had in mind and then poor Julius had to go make it into actual production ready code. As Flambo said in shot, "Love this. Build it three times and throw away the first two." Yeah. This didn't make sense when code was expensive, but now code is cheap as [ \_\_ ] Build the code. Stop inventing all this [ \_\_ ] So in some senses, Linear is far ahead of the curve here. In others, I think they're still thinking a little too much about how teams were split up historically and not enough about how that's going to change. And 

I've also never been so confident that Jira is [ \_\_ ] cuz you know they aren't thinking about any of this. They are thinking so little about this that they bought one of my least favorite companies, the browser company, which is a very good fit if you know anything about how Jira and Atlassian work as well as how much the browser company doesn't work. Think I've said all I have to here. As you can tell, I have a lot of feelings and hopefully this will be useful to you guys. I know a lot of you work at real companies where you're using things like issue trackers and I would love to hear from y'all. What are you guys doing now and how is it changed with AI? Are you using AI with your issues? What does 

that look like? I'm actually really curious and want to hear more. Let me know and until next time, peace nerds. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 If you're anything like me, you probably
 </span>
 <span data-rw-start="1.72" data-rw-transcript-version="2">
 hate issue trackers, which is why it's
 </span>
 <span data-rw-start="3.36" data-rw-transcript-version="2">
 so exciting to see them die. That said,
 </span>
 <span data-rw-start="5.56" data-rw-transcript-version="2">
 I'm a little scared of what's next. I
 </span>
 <span data-rw-start="7.28" data-rw-transcript-version="2">
 need to address something really quick
 </span>
 <span data-rw-start="8.64" data-rw-transcript-version="2">
 though. You might have thought the
 </span>
 <span data-rw-start="9.76" data-rw-transcript-version="2">
 thumbnail was clickbait. I know I use
 </span>
 <span data-rw-start="11.48" data-rw-transcript-version="2">
 fake tweets sometimes to get your guys
 </span>
 <span data-rw-start="12.88" data-rw-transcript-version="2">
 attention. This time it wasn't. Even
 </span>
 <span data-rw-start="15.04" data-rw-transcript-version="2">
 Linear is saying that issue tracking is
 </span>
 <span data-rw-start="17.16" data-rw-transcript-version="2">
 dead. Kind of crazy that they are trying
 </span>
 <span data-rw-start="19.32" data-rw-transcript-version="2">
 to kill the industry category that they
 </span>
 <span data-rw-start="21.08" data-rw-transcript-version="2">
 have been leading for a while, but I'm
 </span>
 <span data-rw-start="22.88" data-rw-transcript-version="2">
 actually really excited about the
 </span>
 <span data-rw-start="24.36" data-rw-transcript-version="2">
 direction that they're going in. They
 </span>
 <span data-rw-start="26.12" data-rw-transcript-version="2">
 just posted an article all about this
 </span>
 <span data-rw-start="28.04" data-rw-transcript-version="2">
 and I couldn't agree more. It seems like
 </span>
 <span data-rw-start="29.96" data-rw-transcript-version="2">
 the future of development is not a pile
 </span>
 <span data-rw-start="32.36" data-rw-transcript-version="2">
 of issues on Jira and Linear that you
 </span>
 <span data-rw-start="34.68" data-rw-transcript-version="2">
 slowly go through as a team, and instead
 </span>
</p>
<p>
 <span data-rw-start="36.8" data-rw-transcript-version="2">
 it's going to look and feel a lot
 </span>
 <span data-rw-start="39" data-rw-transcript-version="2">
 different. It's really hard to say what
 </span>
 <span data-rw-start="40.6" data-rw-transcript-version="2">
 the future's going to look like, but I'm
 </span>
 <span data-rw-start="41.92" data-rw-transcript-version="2">
 excited to explore what Linear is
 </span>
 <span data-rw-start="43.36" data-rw-transcript-version="2">
 working on. But there is something I
 </span>
 <span data-rw-start="44.8" data-rw-transcript-version="2">
 Know is useful right now. Today's
 </span>
 <span data-rw-start="46.52" data-rw-transcript-version="2">
 sponsor. Two years ago, I had a
 </span>
 <span data-rw-start="47.8" data-rw-transcript-version="2">
 conversation that has stuck with me
 </span>
 <span data-rw-start="49.28" data-rw-transcript-version="2">
 since. It was a conversation with
 </span>
 <span data-rw-start="50.6" data-rw-transcript-version="2">
 Guillermo, the CEO of Vercel. We were
 </span>
 <span data-rw-start="52.36" data-rw-transcript-version="2">
 talking about things that we did right
 </span>
 <span data-rw-start="53.76" data-rw-transcript-version="2">
 and wrong with our businesses. And the
 </span>
 <span data-rw-start="55.24" data-rw-transcript-version="2">
 thing that he said that shocked me is
 </span>
 <span data-rw-start="57.04" data-rw-transcript-version="2">
 that he deeply regrets rolling his own
 </span>
 <span data-rw-start="59" data-rw-transcript-version="2">
 off at Vercel. That might sound insane
 </span>
 <span data-rw-start="61.16" data-rw-transcript-version="2">
 with a company the size of Vercel. Like,
 </span>
 <span data-rw-start="62.64" data-rw-transcript-version="2">
 obviously, you should be rolling your own
 </span>
 <span data-rw-start="64.4" data-rw-transcript-version="2">
 everything. It's your platform, right?
 </span>
</p>
<p>
 <span data-rw-start="66.28" data-rw-transcript-version="2">
 Well, it turns out there's a lot of
 </span>
 <span data-rw-start="67.6" data-rw-transcript-version="2">
 problems when you own your own layer,
 </span>
 <span data-rw-start="69.64" data-rw-transcript-version="2">
 and they're not things like setting up
 </span>
 <span data-rw-start="71.08" data-rw-transcript-version="2">
 Google to sign in correctly, as annoying
 </span>
 <span data-rw-start="72.72" data-rw-transcript-version="2">
 as that is. Problems go deeper. What
 </span>
 <span data-rw-start="74.72" data-rw-transcript-version="2">
 happens when real companies want to
 </span>
 <span data-rw-start="76.24" data-rw-transcript-version="2">
 onboard onto your product, and they don't
 </span>
 <span data-rw-start="78.16" data-rw-transcript-version="2">
 have the weird niche expectations their
 </span>
 <span data-rw-start="80.08" data-rw-transcript-version="2">
 IT team expects to make it so their
 </span>
 <span data-rw-start="82" data-rw-transcript-version="2">
 business employees can sign into your
 </span>
 <span data-rw-start="83.88" data-rw-transcript-version="2">
 service using their existing
 </span>
 <span data-rw-start="85.32" data-rw-transcript-version="2">
 authentication. Spoiler, I'm not the
 </span>
 <span data-rw-start="87.12" data-rw-transcript-version="2">
 Only one Guillermo's had this
 </span>
 <span data-rw-start="88.28" data-rw-transcript-version="2">
 conversation with. And as he says here,
 </span>
 <span data-rw-start="90.64" data-rw-transcript-version="2">
 "I think we could have done even more
 </span>
 <span data-rw-start="92.08" data-rw-transcript-version="2">
 business if we had partnered with WorkOS
 </span>
 <span data-rw-start="93.96" data-rw-transcript-version="2">
 earlier. It's been incredibly well
 </span>
 <span data-rw-start="95.72" data-rw-transcript-version="2">
 received."
 </span>
</p>
<p>
 <span data-rw-start="97.08" data-rw-transcript-version="2">
 I'm sure you've guessed by
 </span>
 <span data-rw-start="97.08" data-rw-transcript-version="2">
 now, but today's sponsor is WorkOS, the
 </span>
 <span data-rw-start="98.8" data-rw-transcript-version="2">
 off platform used by OpenAI and
 </span>
 <span data-rw-start="100.6" data-rw-transcript-version="2">
 Anthropic, Vercel, T3 Chat, and many,
 </span>
 <span data-rw-start="103.08" data-rw-transcript-version="2">
 many more. WorkOS has found an
 </span>
 <span data-rw-start="104.76" data-rw-transcript-version="2">
 incredible balance of developer
 </span>
 <span data-rw-start="106.28" data-rw-transcript-version="2">
 experience and enterprise readiness,
 </span>
 <span data-rw-start="108.48" data-rw-transcript-version="2">
 where they have everything you need to
 </span>
 <span data-rw-start="109.8" data-rw-transcript-version="2">
 onboard these real companies. Never
 </span>
 <span data-rw-start="111.64" data-rw-transcript-version="2">
 having to think about identity provision
 </span>
 <span data-rw-start="113.12" data-rw-transcript-version="2">
 again is a gift from the heavens, and I
 </span>
 <span data-rw-start="115.12" data-rw-transcript-version="2">
 am so thankful for WorkOS making it so
 </span>
 <span data-rw-start="117.4" data-rw-transcript-version="2">
 that I never have to configure ADP again
 </span>
 <span data-rw-start="119.76" data-rw-transcript-version="2">
 for the rest of my life. If that's all
 </span>
 <span data-rw-start="121.24" data-rw-transcript-version="2">
 they offered, it would be worth it, but
 </span>
 <span data-rw-start="122.52" data-rw-transcript-version="2">
 there's so much more to the platform.
 </span>
</p>
<p>
 <span data-rw-start="124.08" data-rw-transcript-version="2">
 AuthKit makes it really easy to set up
 </span>
 <span data-rw-start="125.68" data-rw-transcript-version="2">
 the buttons and panels that you need for
 </span>
 <span data-rw-start="127.28" data-rw-transcript-version="2">
 your users. MCP Auth means you can
 </span>
 <span data-rw-start="129.119" data-rw-transcript-version="2">
 finally add authorization to your MCP.
 </span>
</p>
<p>
 <span data-rw-start="131.12" data-rw-transcript-version="2">
 Servers. Directory sync makes it trivial
 </span>
 <span data-rw-start="133.12" data-rw-transcript-version="2">
 for companies to keep things in sync
 </span>
 <span data-rw-start="134.84" data-rw-transcript-version="2">
 between their dashboards and your
 </span>
 <span data-rw-start="136.6" data-rw-transcript-version="2">
 product. Vault's one of the best ways to
 </span>
 <span data-rw-start="138.44" data-rw-transcript-version="2">
 store user-specific encrypted values,
 </span>
 <span data-rw-start="140.72" data-rw-transcript-version="2">
 things like API keys that they might be
 </span>
 <span data-rw-start="142.48" data-rw-transcript-version="2">
 using in your service. And there's so
 </span>
 <span data-rw-start="144.12" data-rw-transcript-version="2">
 much more to explore. Your next fear
 </span>
 <span data-rw-start="146.4" data-rw-transcript-version="2">
 going to be the price because there's no way
 </span>
 <span data-rw-start="147.84" data-rw-transcript-version="2">
 it can be that good for cheap, right?
 </span>
</p>
<p>
 <span data-rw-start="149.4" data-rw-transcript-version="2">
 Well, you have nothing to worry about
 </span>
 <span data-rw-start="150.76" data-rw-transcript-version="2">
 because the first million users are free.
 </span>
 <span data-rw-start="153.56" data-rw-transcript-version="2">
 Get yourself enterprise-ready at
 </span>
 <span data-rw-start="154.92" data-rw-transcript-version="2">
 soidiv.link/workos.
 </span>
 <span data-rw-start="156.68" data-rw-transcript-version="2">
 I'm very excited to read into what
 </span>
 <span data-rw-start="158" data-rw-transcript-version="2">
 Linear is cooking here. You know they're
 </span>
 <span data-rw-start="159.56" data-rw-transcript-version="2">
 cooking something different because this is
 </span>
 <span data-rw-start="160.56" data-rw-transcript-version="2">
 the only not dark mode page I've ever
 </span>
 <span data-rw-start="162.72" data-rw-transcript-version="2">
 seen Linear ship. They actually took the
 </span>
 <span data-rw-start="164.56" data-rw-transcript-version="2">
 time to make it so when you read this
 </span>
 <span data-rw-start="166.36" data-rw-transcript-version="2">
 particular page, it is light mode and
 </span>
 <span data-rw-start="168.28" data-rw-transcript-version="2">
 they flipped the logo and everything in
 </span>
 <span data-rw-start="169.48" data-rw-transcript-version="2">
 the top nav. They also did the usual
 </span>
 <span data-rw-start="171.4" data-rw-transcript-version="2">
 Linear thing of trying way too hard in
 </span>
 <span data-rw-start="173" data-rw-transcript-version="2">
 design for something that doesn't matter.
 </span>
</p>
<p>
 <span data-rw-start="174.04" data-rw-transcript-version="2">
 That much with the logo. You can move
 </span>
 <span data-rw-start="175.84" data-rw-transcript-version="2">
 your cursor through like a fluid and
 </span>
 <span data-rw-start="177.72" data-rw-transcript-version="2">
 click to pulse it. It's cool. It's very
 </span>
 <span data-rw-start="180.239" data-rw-transcript-version="2">
 uh Linear of them. Anyways, issue
 </span>
 <span data-rw-start="182.64" data-rw-transcript-version="2">
 tracking is dead. It was built for a
 </span>
 <span data-rw-start="184.92" data-rw-transcript-version="2">
 handoff model of software development. A
 </span>
 <span data-rw-start="187.12" data-rw-transcript-version="2">
 PM would scope the work, engineers would
 </span>
 <span data-rw-start="188.88" data-rw-transcript-version="2">
 pick it up later, and the system was
 </span>
 <span data-rw-start="190.8" data-rw-transcript-version="2">
 filled with prioritization, negotiation,
 </span>
 <span data-rw-start="193.04" data-rw-transcript-version="2">
 and workflows to bridge the gap. That
 </span>
 <span data-rw-start="194.92" data-rw-transcript-version="2">
 ceremony came from real constraints.
 </span>
</p>
<p>
 <span data-rw-start="197.08" data-rw-transcript-version="2">
 Engineering time was scarce. Teams
 </span>
 <span data-rw-start="199.08" data-rw-transcript-version="2">
 needed a way to route work carefully
 </span>
 <span data-rw-start="200.88" data-rw-transcript-version="2">
 across roles and functions. Absolutely
 </span>
 <span data-rw-start="203.519" data-rw-transcript-version="2">
 agree. This is my whole life when I was
 </span>
 <span data-rw-start="204.8" data-rw-transcript-version="2">
 an engineer back at Twitch. It was the
 </span>
 <span data-rw-start="206.4" data-rw-transcript-version="2">
 chaos of breaking up large piles of work
 </span>
 <span data-rw-start="209.16" data-rw-transcript-version="2">
 into small tickets, throwing those into
 </span>
 <span data-rw-start="210.88" data-rw-transcript-version="2">
 a queue, and then going through them,
 </span>
 <span data-rw-start="212.6" data-rw-transcript-version="2">
 assigning them to people, and trying to
 </span>
 <span data-rw-start="214.239" data-rw-transcript-version="2">
 guesstimate when all of the work
 </span>
 <span data-rw-start="215.76" data-rw-transcript-version="2">
 necessary would be done to ship the
 </span>
 <span data-rw-start="217" data-rw-transcript-version="2">
 thing they all lean into. But over time,
 </span>
 <span data-rw-start="219.16" data-rw-transcript-version="2">
 complexity started to look like
 </span>
 <span data-rw-start="220.88" data-rw-transcript-version="2">
 sophistication. The more process a
 </span>
 <span data-rw-start="222.44" data-rw-transcript-version="2">
 System could absorb, the more advanced
 </span>
</p>
<p>
 <span data-rw-start="224.239" data-rw-transcript-version="2">
 it seemed. Overhead kept growing and the
 </span>
 <span data-rw-start="226.519" data-rw-transcript-version="2">
 process became work itself. Yep, my Jira
 </span>
 <span data-rw-start="229.519" data-rw-transcript-version="2">
 dashboard back at Twitch would take over
 </span>
 <span data-rw-start="231.76" data-rw-transcript-version="2">
 2 minutes to load. Technically saying
 </span>
 <span data-rw-start="234.32" data-rw-transcript-version="2">
 that is against the terms of service for
 </span>
 <span data-rw-start="236.08" data-rw-transcript-version="2">
 Jira, but thankfully I have been out of
 </span>
 <span data-rw-start="238.12" data-rw-transcript-version="2">
 Twitch for over 5 years now, so I can
 </span>
 <span data-rw-start="239.88" data-rw-transcript-version="2">
 say whatever the [ \_\_ ] I want. Yeah, Jira
 </span>
 <span data-rw-start="242.6" data-rw-transcript-version="2">
 ran like [ \_\_ ] garbage, and that was
 </span>
 <span data-rw-start="245.84" data-rw-transcript-version="2">
 because we had filled it with so much
 </span>
 <span data-rw-start="247.68" data-rw-transcript-version="2">
 complex [ \_\_ ] across the absurd
 </span>
 <span data-rw-start="249.92" data-rw-transcript-version="2">
 number of tickets in different fields
 </span>
 <span data-rw-start="251.76" data-rw-transcript-version="2">
 and data links across things at Twitch.
 </span>
</p>
<p>
 <span data-rw-start="254.48" data-rw-transcript-version="2">
 And that's just what happens when you
 </span>
 <span data-rw-start="255.959" data-rw-transcript-version="2">
 have a system like this, every single
 </span>
 <span data-rw-start="257.799" data-rw-transcript-version="2">
 feature is going to be used and abused
 </span>
 <span data-rw-start="260.12" data-rw-transcript-version="2">
 until it breaks at the seams. People are
 </span>
 <span data-rw-start="262.16" data-rw-transcript-version="2">
 confused about why I can't talk about
 </span>
 <span data-rw-start="265.04" data-rw-transcript-version="2">
 Jira's performance. They did a terms of
 </span>
 <span data-rw-start="266.88" data-rw-transcript-version="2">
 service update back in the day when I
 </span>
 <span data-rw-start="268.84" data-rw-transcript-version="2">
 was at Twitch that explicitly banned
 </span>
 <span data-rw-start="272.04" data-rw-transcript-version="2">
 talking about the performance
 </span>
 <span data-rw-start="273.68" data-rw-transcript-version="2">
 characteristics of Jira and sharing
 </span>
 <span data-rw-start="275.44" data-rw-transcript-version="2">
 benchmarks for its performance when I
 </span>
 <span data-rw-start="277.52" data-rw-transcript-version="2">
 Was at Twitch. But now, it's been long enough that I will tell you guys, Jira
 </span>
 <span data-rw-start="279.6" data-rw-transcript-version="2">
 performs like [ \_\_ ] garbage at real
 </span>
 <span data-rw-start="281.16" data-rw-transcript-version="2">
 companies. Also, yes, I do have Jira as
 </span>
 <span data-rw-start="285" data-rw-transcript-version="2">
 a banned term on my switch streams,
 </span>
 <span data-rw-start="287.28" data-rw-transcript-version="2">
 because I thought it was funny to do. I
 </span>
 <span data-rw-start="288.88" data-rw-transcript-version="2">
 might need to go remove that if one of
 </span>
 <span data-rw-start="290.32" data-rw-transcript-version="2">
 the moderators can go figure out how to
 </span>
 <span data-rw-start="291.72" data-rw-transcript-version="2">
 do that, please do. At least for now.
 </span>
</p>
<p>
 <span data-rw-start="293.52" data-rw-transcript-version="2">
 Yeah, Jira, the correct spelling with
 </span>
 <span data-rw-start="295.56" data-rw-transcript-version="2">
 the star. We need to not say the J-word
 </span>
 <span data-rw-start="297.36" data-rw-transcript-version="2">
 if we can avoid it. Back to the article.
 </span>
 <span data-rw-start="299.16" data-rw-transcript-version="2">
 Linear's always been built on the
 </span>
 <span data-rw-start="300.28" data-rw-transcript-version="2">
 opposite belief, the opposite of the
 </span>
 <span data-rw-start="302.24" data-rw-transcript-version="2">
 system continuing to grow and get more
 </span>
 <span data-rw-start="303.56" data-rw-transcript-version="2">
 complex. The best systems should remove
 </span>
 <span data-rw-start="305.64" data-rw-transcript-version="2">
 overhead so the teams can focus on
 </span>
 <span data-rw-start="307.4" data-rw-transcript-version="2">
 building. That's absolutely how Linear
 </span>
 <span data-rw-start="309.04" data-rw-transcript-version="2">
 felt. It felt like they were trying to
 </span>
 <span data-rw-start="310.24" data-rw-transcript-version="2">
 remove as much weight as possible. So
 </span>
 <span data-rw-start="312.4" data-rw-transcript-version="2">
 getting in, looking at the issues,
 </span>
 <span data-rw-start="314.2" data-rw-transcript-version="2">
 filtering through things, and getting
 </span>
 <span data-rw-start="315.44" data-rw-transcript-version="2">
 the data you need to go back to work was
 </span>
 <span data-rw-start="317.48" data-rw-transcript-version="2">
 as easy as possible. And that's why so
 </span>
 <span data-rw-start="319.2" data-rw-transcript-version="2">
 many engineers preferred Linear. It was
 </span>
 <span data-rw-start="320.919" data-rw-transcript-version="2">
 Kind of a bet on engineers being the
 </span>
 <span data-rw-start="322.76" data-rw-transcript-version="2">
 ones who made important decisions at
 </span>
 <span data-rw-start="324.08" data-rw-transcript-version="2">
 companies because Jira was the thing
 </span>
 <span data-rw-start="326.04" data-rw-transcript-version="2">
 that product managers picked because
 </span>
 <span data-rw-start="327.64" data-rw-transcript-version="2">
 that's who it was marketed to, to be
 </span>
 <span data-rw-start="328.72" data-rw-transcript-version="2">
 clear. And Linear wanted something the
 </span>
 <span data-rw-start="330.44" data-rw-transcript-version="2">
 engineers liked because they hated using
 </span>
 <span data-rw-start="332.56" data-rw-transcript-version="2">
 Jira at the companies they were at. So
 </span>
 <span data-rw-start="334.44" data-rw-transcript-version="2">
 they made Linear to make something nice
 </span>
</p>
<p>
 <span data-rw-start="336" data-rw-transcript-version="2">
 and simple and elegant for enges, and it
 </span>
 <span data-rw-start="338" data-rw-transcript-version="2">
 more than succeeded and is now doing
 </span>
 <span data-rw-start="339.52" data-rw-transcript-version="2">
 quite well. I would bet they have a
 </span>
 <span data-rw-start="340.76" data-rw-transcript-version="2">
 similar number of users and a
 </span>
 <span data-rw-start="342" data-rw-transcript-version="2">
 significantly higher number of startups
 </span>
 <span data-rw-start="343.919" data-rw-transcript-version="2">
 than Jira ever has or will. But now
 </span>
 <span data-rw-start="346.52" data-rw-transcript-version="2">
 we're in the AI era, and things are
 </span>
 <span data-rw-start="348.04" data-rw-transcript-version="2">
 changing fast. Again, their goal is to
 </span>
 <span data-rw-start="350" data-rw-transcript-version="2">
 remove overhead, and according to them,
 </span>
 <span data-rw-start="351.52" data-rw-transcript-version="2">
 agents push the removal of that overhead
 </span>
 <span data-rw-start="353.2" data-rw-transcript-version="2">
 even further. They can make software dev
 </span>
 <span data-rw-start="354.84" data-rw-transcript-version="2">
 a lot simpler. Planning, implementation,
 </span>
 <span data-rw-start="356.96" data-rw-transcript-version="2">
 and code review begin to compress as
 </span>
 <span data-rw-start="359.2" data-rw-transcript-version="2">
 agents absorb more of the procedural
 </span>
 <span data-rw-start="361.24" data-rw-transcript-version="2">
 work. You'll get to spend more time on
 </span>
 <span data-rw-start="362.56" data-rw-transcript-version="2">
 intent, judgment, and taste, and less
 </span>
 <span data-rw-start="364.64" data-rw-transcript-version="2">
 Time managing the mechanics of the
 </span>
 <span data-rw-start="366.52" data-rw-transcript-version="2">
 process. This one's particularly
 </span>
 <span data-rw-start="368.32" data-rw-transcript-version="2">
 interesting to me because I actually
 </span>
 <span data-rw-start="370.48" data-rw-transcript-version="2">
 kind of worked the same way when I was
 </span>
 <span data-rw-start="372.44" data-rw-transcript-version="2">
 at Twitch. It was so common to have
 </span>
 <span data-rw-start="374.52" data-rw-transcript-version="2">
 tickets that just didn't correctly
 </span>
 <span data-rw-start="376.2" data-rw-transcript-version="2">
 estimate how hard things were and missed
 </span>
 <span data-rw-start="378.12" data-rw-transcript-version="2">
 a bunch of subtasks that were important.
 </span>
</p>
<p>
 <span data-rw-start="380.68" data-rw-transcript-version="2">
 And to be frank, I never read a spec
 </span>
 <span data-rw-start="383.52" data-rw-transcript-version="2">
 that was written before the product was
 </span>
 <span data-rw-start="385.08" data-rw-transcript-version="2">
 made that even came close to describing
 </span>
 <span data-rw-start="387.48" data-rw-transcript-version="2">
 what the product actually would be, how
 </span>
 <span data-rw-start="388.919" data-rw-transcript-version="2">
 it should be implemented, and how long
 </span>
 <span data-rw-start="390.24" data-rw-transcript-version="2">
 it would take. It was almost always
 </span>
 <span data-rw-start="391.72" data-rw-transcript-version="2">
 entirely inaccurate. So, what I did
 </span>
 <span data-rw-start="394.04" data-rw-transcript-version="2">
 instead is I would go build a small
 </span>
 <span data-rw-start="396" data-rw-transcript-version="2">
 version of what we were aiming for in 1
 </span>
 <span data-rw-start="398.08" data-rw-transcript-version="2">
 to 3 days just to force out whatever
 </span>
 <span data-rw-start="400.919" data-rw-transcript-version="2">
 could let us test the UX. And through
 </span>
 <span data-rw-start="402.88" data-rw-transcript-version="2">
 that process, I’d be able to identify
 </span>
 <span data-rw-start="404.48" data-rw-transcript-version="2">
 any tech shortcomings we have to touch
 </span>
 <span data-rw-start="406.919" data-rw-transcript-version="2">
 out of a very clear service area of
 </span>
 <span data-rw-start="408.68" data-rw-transcript-version="2">
 things we have to know about and be
 </span>
 <span data-rw-start="410.44" data-rw-transcript-version="2">
 involved in order to make this work. Out
 </span>
 <span data-rw-start="412.28" data-rw-transcript-version="2">
 of a demoable, usable version of the
 </span>
 <span data-rw-start="414.04" data-rw-transcript-version="2">
 Product that we could use for testing
 </span>
 <span data-rw-start="415.44" data-rw-transcript-version="2">
 both internally and in front of users
 </span>
 <span data-rw-start="417.16" data-rw-transcript-version="2">
 when we brought users into the office.
 </span>
</p>
<p>
 <span data-rw-start="418.64" data-rw-transcript-version="2">
 And through that, we were able to
 </span>
 <span data-rw-start="419.84" data-rw-transcript-version="2">
 collect a ton of information in order to
 </span>
 <span data-rw-start="422.48" data-rw-transcript-version="2">
 make sure that we steered the product
 </span>
 <span data-rw-start="424.32" data-rw-transcript-version="2">
 and its design in the right direction.
 </span>
</p>
<p>
 <span data-rw-start="426.16" data-rw-transcript-version="2">
 The result of this is that we could
 </span>
 <span data-rw-start="427.24" data-rw-transcript-version="2">
 write way better specs because we
 </span>
 <span data-rw-start="428.72" data-rw-transcript-version="2">
 actually had a rough idea of what the
 </span>
 <span data-rw-start="430.48" data-rw-transcript-version="2">
 product would look like and how it would
 </span>
 <span data-rw-start="432.12" data-rw-transcript-version="2">
 work. The more surprising part for me,
 </span>
 <span data-rw-start="434.28" data-rw-transcript-version="2">
 though, was how often we would just ship
 </span>
 <span data-rw-start="436.32" data-rw-transcript-version="2">
 that quickly built version. And to be
 </span>
 <span data-rw-start="438.24" data-rw-transcript-version="2">
 very clear, the point of this process
 </span>
 <span data-rw-start="439.8" data-rw-transcript-version="2">
 wasn't to get the feature out faster. It
 </span>
 <span data-rw-start="441.72" data-rw-transcript-version="2">
 was to develop a working prototype of it
 </span>
 <span data-rw-start="444.36" data-rw-transcript-version="2">
 to know what was required to do it and
 </span>
 <span data-rw-start="446.28" data-rw-transcript-version="2">
 to make a better spec and, most
 </span>
 <span data-rw-start="447.96" data-rw-transcript-version="2">
 importantly, have a version that people
 </span>
 <span data-rw-start="449.28" data-rw-transcript-version="2">
 could start testing to make sure this is
 </span>
 <span data-rw-start="450.36" data-rw-transcript-version="2">
 even worth doing. And I would say about
 </span>
 <span data-rw-start="452.16" data-rw-transcript-version="2">
 half the time we ended up slightly
 </span>
 <span data-rw-start="453.76" data-rw-transcript-version="2">
 polishing that first pass and just
 </span>
</p>
<p>
 <span data-rw-start="455.6" data-rw-transcript-version="2">
 shipping it because we had no reason to
 </span>
 <span data-rw-start="457.36" data-rw-transcript-version="2">
 Go much further with it. The amount of
 </span>
 <span data-rw-start="459.2" data-rw-transcript-version="2">
 times I had a that should have been a
 </span>
 <span data-rw-start="460.96" data-rw-transcript-version="2">
 huge 20-page spec that we spent weeks
 </span>
 <span data-rw-start="464.12" data-rw-transcript-version="2">
 writing and debating that just took me a
 </span>
 <span data-rw-start="466.16" data-rw-transcript-version="2">
 few days and we ended up shipping as is
 </span>
 <span data-rw-start="468.16" data-rw-transcript-version="2">
 is hilarious. To be frank, this hurt my
 </span>
 <span data-rw-start="470.64" data-rw-transcript-version="2">
 career growth to an extent because we
 </span>
 <span data-rw-start="472.08" data-rw-transcript-version="2">
 didn't have all these fancy documents we
 </span>
 <span data-rw-start="473.84" data-rw-transcript-version="2">
 could point out during my promotion
 </span>
 <span data-rw-start="475.24" data-rw-transcript-version="2">
 process that was built all around that
 </span>
 <span data-rw-start="476.8" data-rw-transcript-version="2">
 [ \_\_ ]. But it did make me pretty well
 </span>
 <span data-rw-start="478.8" data-rw-transcript-version="2">
 regarded internally, and this is still
 </span>
 <span data-rw-start="480.56" data-rw-transcript-version="2">
 referred to as the Theo method or the
 </span>
 <span data-rw-start="482.68" data-rw-transcript-version="2">
 Theo prototype at Twitch to this day.
 </span>
</p>
<p>
 <span data-rw-start="484.88" data-rw-transcript-version="2">
 Depending on the team, of course, but a
 </span>
 <span data-rw-start="486.12" data-rw-transcript-version="2">
 lot of teams still do things this way. I
 </span>
 <span data-rw-start="487.88" data-rw-transcript-version="2">
 know I fully overhauled a handful of
 </span>
 <span data-rw-start="489.6" data-rw-transcript-version="2">
 teams' process around product design by
 </span>
 <span data-rw-start="491.48" data-rw-transcript-version="2">
 just refusing to write a boring useless
 </span>
 <span data-rw-start="493.48" data-rw-transcript-version="2">
 spec. There’s nothing I hate more than
 </span>
 <span data-rw-start="495.6" data-rw-transcript-version="2">
 useless [ \_\_ ] being done by engineers
 </span>
 <span data-rw-start="498" data-rw-transcript-version="2">
 that doesn’t even make them feel good.
 </span>
 <span data-rw-start="500.32" data-rw-transcript-version="2">
 Engineers love useless [ \_\_ ] as long
 </span>
 <span data-rw-start="501.88" data-rw-transcript-version="2">
 as it’s inside of their terminal. They
 </span>
 <span data-rw-start="503.24" data-rw-transcript-version="2">
 hate it when it’s inside of Google Docs.
 </span>
</p>
<p>
 <span data-rw-start="504.84" data-rw-transcript-version="2">
 So trying to get them away from those
 </span>
 <span data-rw-start="506.4" data-rw-transcript-version="2">
 things and instead back into their
 </span>
 <span data-rw-start="508.28" data-rw-transcript-version="2">
 editor was always beneficial. And it
 </span>
 <span data-rw-start="510.2" data-rw-transcript-version="2">
 turns out a lot of people agree, they
 </span>
 <span data-rw-start="511.72" data-rw-transcript-version="2">
 just weren't good enough devs to agree.
 </span>
</p>
<p>
 <span data-rw-start="513.36" data-rw-transcript-version="2">
 Okay, I shouldn't say good cuz this is a
 </span>
 <span data-rw-start="514.8" data-rw-transcript-version="2">
 different skill. There's a lot of very
 </span>
 <span data-rw-start="516.159" data-rw-transcript-version="2">
 talented devs that don't build very
 </span>
 <span data-rw-start="517.599" data-rw-transcript-version="2">
 fast. There's a lot of average devs that
 </span>
 <span data-rw-start="519.479" data-rw-transcript-version="2">
 happen to build really fast. That's how
 </span>
 <span data-rw-start="520.88" data-rw-transcript-version="2">
 I would have described myself when I was
 </span>
 <span data-rw-start="522.24" data-rw-transcript-version="2">
 at Twitch. I was a okay to decent dev,
 </span>
 <span data-rw-start="525" data-rw-transcript-version="2">
 but I was really good at trimming the
 </span>
 <span data-rw-start="526.96" data-rw-transcript-version="2">
 fat, identifying where in the system we
 </span>
 <span data-rw-start="528.88" data-rw-transcript-version="2">
 can insert the thing to make it way
 </span>
 <span data-rw-start="530.2" data-rw-transcript-version="2">
 easier to build, and then building the
 </span>
 <span data-rw-start="532.36" data-rw-transcript-version="2">
 thing. That was one of the things that
 </span>
 <span data-rw-start="533.64" data-rw-transcript-version="2">
 made me unique. But it's also a
 </span>
 <span data-rw-start="534.92" data-rw-transcript-version="2">
 capability that almost all engineers now
 </span>
</p>
<p>
 <span data-rw-start="536.88" data-rw-transcript-version="2">
 have because of agents. Benefits and
 </span>
 <span data-rw-start="538.56" data-rw-transcript-version="2">
 negatives. That said, I think that way
 </span>
 <span data-rw-start="540.56" data-rw-transcript-version="2">
 of building is so much better. Make a
 </span>
 <span data-rw-start="542.48" data-rw-transcript-version="2">
 first version of the thing, then make
 </span>
 <span data-rw-start="544.56" data-rw-transcript-version="2">
 the spec, then build it correctly,
 </span>
 <span data-rw-start="546.6" data-rw-transcript-version="2">
 rather than write a spec assuming you
 </span>
 <span data-rw-start="548.56" data-rw-transcript-version="2">
 Know how it will work, and build it wrong because you were incorrect with
 </span>
 <span data-rw-start="550" data-rw-transcript-version="2">
 the spec, and then keep [\_\_] throwing
 </span>
 <span data-rw-start="551.32" data-rw-transcript-version="2">
 band-aids on it until it kind of works,
 </span>
 <span data-rw-start="554.92" data-rw-transcript-version="2">
 and then you ship a broken thing. Hate
 </span>
 <span data-rw-start="556.56" data-rw-transcript-version="2">
 that strategy. The first version of
 </span>
 <span data-rw-start="558.12" data-rw-transcript-version="2">
 software will always be less than ideal.
 </span>
</p>
<p>
 <span data-rw-start="560.16" data-rw-transcript-version="2">
 Do it first to figure it out, throw it
 </span>
 <span data-rw-start="562.16" data-rw-transcript-version="2">
 away, and then make a good version
 </span>
 <span data-rw-start="563.56" data-rw-transcript-version="2">
 after. Now that is much more viable. And
 </span>
 <span data-rw-start="565.72" data-rw-transcript-version="2">
 it's nice to see Linear realizing the
 </span>
 <span data-rw-start="567.56" data-rw-transcript-version="2">
 same thing, too. I almost feel as though
 </span>
 <span data-rw-start="569.6" data-rw-transcript-version="2">
 these types of issues tracking systems
 </span>
 <span data-rw-start="571.88" data-rw-transcript-version="2">
 discourage that type of exploration
 </span>
 <span data-rw-start="573.6" data-rw-transcript-version="2">
 building because it's so valuable.
 </span>
 <span data-rw-start="575.96" data-rw-transcript-version="2">
 According to Linear, the shift with
 </span>
 <span data-rw-start="578" data-rw-transcript-version="2">
 agents is already underway. Coding
 </span>
 <span data-rw-start="579.76" data-rw-transcript-version="2">
 agents are installed in more than 75% of
 </span>
 <span data-rw-start="582.72" data-rw-transcript-version="2">
 Linear's enterprise workspaces. Not just
 </span>
 <span data-rw-start="585.4" data-rw-transcript-version="2">
 side projects, not just people playing
 </span>
 <span data-rw-start="586.64" data-rw-transcript-version="2">
 around with it. The enterprise deals
 </span>
 <span data-rw-start="588.32" data-rw-transcript-version="2">
 they have with big businesses using
 </span>
 <span data-rw-start="589.84" data-rw-transcript-version="2">
 them. 75%
 </span>
 <span data-rw-start="591.8" data-rw-transcript-version="2">
 or more are already using agents as
 </span>
 <span data-rw-start="594.08" data-rw-transcript-version="2">
 integrations in Linear. I bet you the
 </span>
</p>
<p>
 <span data-rw-start="595.96" data-rw-transcript-version="2">
 Other 25% are largely copy-pasting the
 </span>
 <span data-rw-start="598" data-rw-transcript-version="2">
 issues into their agent of choice to get
 </span>
 <span data-rw-start="600.32" data-rw-transcript-version="2">
 the code built. In the last 3 months,
 </span>
 <span data-rw-start="602.48" data-rw-transcript-version="2">
 the volume of work completed by agents
 </span>
 <span data-rw-start="604.72" data-rw-transcript-version="2">
 grew 5x. Do you understand how crazy
 </span>
 <span data-rw-start="608" data-rw-transcript-version="2">
 that is in particular? That’s the Opus
 </span>
 <span data-rw-start="610.4" data-rw-transcript-version="2">
 4.5 effect when people woke up to how
 </span>
 <span data-rw-start="612.76" data-rw-transcript-version="2">
 powerful these models could be and the
 </span>
 <span data-rw-start="614.64" data-rw-transcript-version="2">
 level of work they could get done. And
 </span>
 <span data-rw-start="616.84" data-rw-transcript-version="2">
 obviously now with Codex, we can go even
 </span>
 <span data-rw-start="618.52" data-rw-transcript-version="2">
 further. They also noted that agents
 </span>
 <span data-rw-start="620.24" data-rw-transcript-version="2">
 authored nearly 25% of new issues, which
 </span>
 <span data-rw-start="622.92" data-rw-transcript-version="2">
 is very interesting to me. I still
 </span>
 <span data-rw-start="624.36" data-rw-transcript-version="2">
 haven’t gotten into the letting AI make
 </span>
 <span data-rw-start="626.4" data-rw-transcript-version="2">
 the issues side of things. I let them
 </span>
 <span data-rw-start="628.12" data-rw-transcript-version="2">
 close them, but I don’t let them open
 </span>
 <span data-rw-start="629.2" data-rw-transcript-version="2">
 them yet. Maybe I need to get over that.
 </span>
</p>
<p>
 <span data-rw-start="630.84" data-rw-transcript-version="2">
 In this new world, the next system is
 </span>
 <span data-rw-start="632.72" data-rw-transcript-version="2">
 not designed around hand-offs. It’s
 </span>
 <span data-rw-start="634.28" data-rw-transcript-version="2">
 designed around context and agents.
 </span>
</p>
<p>
 <span data-rw-start="636.32" data-rw-transcript-version="2">
 Agents aren’t mind readers. They become
 </span>
 <span data-rw-start="638.04" data-rw-transcript-version="2">
 useful through context. Customer
 </span>
 <span data-rw-start="639.92" data-rw-transcript-version="2">
 feedback, internal ideas, strategic
 </span>
 <span data-rw-start="641.88" data-rw-transcript-version="2">
 direction, decisions, and code all need
 </span>
 <span data-rw-start="644.44" data-rw-transcript-version="2">
 to be captured in a system that humans
 </span>
 <span data-rw-start="646.56" data-rw-transcript-version="2">
 and agents can work from together. Very
 </span>
 <span data-rw-start="649.04" data-rw-transcript-version="2">
 interesting. That system should
 </span>
 <span data-rw-start="650.64" data-rw-transcript-version="2">
 understand intent, route work to the
 </span>
 <span data-rw-start="652.52" data-rw-transcript-version="2">
 right actor, escalate when needed, and
 </span>
 <span data-rw-start="654.839" data-rw-transcript-version="2">
 keep execution moving. It should help
 </span>
 <span data-rw-start="656.839" data-rw-transcript-version="2">
 teams move work forward, not trap them
 </span>
 <span data-rw-start="659.16" data-rw-transcript-version="2">
 inside the process. The number of people
 </span>
 <span data-rw-start="661.4" data-rw-transcript-version="2">
 I know whose jobs are effectively just
 </span>
 <span data-rw-start="663.72" data-rw-transcript-version="2">
 using Linear or Jira is heartbreaking.
 </span>
</p>
<p>
 <span data-rw-start="666.28" data-rw-transcript-version="2">
 Like, those apps are good. Okay, one of
 </span>
 <span data-rw-start="668.52" data-rw-transcript-version="2">
 those apps is good, but none of those
 </span>
 <span data-rw-start="670.2" data-rw-transcript-version="2">
 apps are good enough to spend your day
 </span>
 <span data-rw-start="672" data-rw-transcript-version="2">
 in them. As somebody who spends their
 </span>
 <span data-rw-start="673.2" data-rw-transcript-version="2">
 day in email lately, I empathize. And
 </span>
 <span data-rw-start="676" data-rw-transcript-version="2">
 this is apparently what Linear plans to
 </span>
 <span data-rw-start="677.8" data-rw-transcript-version="2">
 become. Linear is the shared product
 </span>
 <span data-rw-start="679.68" data-rw-transcript-version="2">
 system that turns context into
 </span>
 <span data-rw-start="681.2" data-rw-transcript-version="2">
 execution. That's a really cringe
 </span>
 <span data-rw-start="682.96" data-rw-transcript-version="2">
 one-liner. I don't like that. I hope
 </span>
 <span data-rw-start="684.48" data-rw-transcript-version="2">
 they rethink that. It holds feedback,
 </span>
 <span data-rw-start="686.6" data-rw-transcript-version="2">
 intent, decisions, plans, and code,
 </span>
 <span data-rw-start="688.24" data-rw-transcript-version="2">
 shapes that context into work, and helps
 </span>
 <span data-rw-start="690.64" data-rw-transcript-version="2">
 humans and agents carry it all the way
 </span>
 <span data-rw-start="692.56" data-rw-transcript-version="2">
 to production. So, you have customer
 </span>
 <span data-rw-start="694.04" data-rw-transcript-version="2">
 requests, bug reports, and feedback.
 </span>
</p>
<p>
 <span data-rw-start="695.56" data-rw-transcript-version="2">
 Those become the context with the plans,
 </span>
 <span data-rw-start="697.32" data-rw-transcript-version="2">
 discussions, specs, all the above. That
 </span>
 <span data-rw-start="699.12" data-rw-transcript-version="2">
 becomes rules that are used to actually
 </span>
 <span data-rw-start="701.32" data-rw-transcript-version="2">
 command the agents within the context,
 </span>
 <span data-rw-start="703" data-rw-transcript-version="2">
 like automation skills and permissions.
 </span>
 <span data-rw-start="704.48" data-rw-transcript-version="2">
 That is handed to the agents, and the
 </span>
 <span data-rw-start="705.88" data-rw-transcript-version="2">
 output is the product. Notice that there
 </span>
 <span data-rw-start="707.52" data-rw-transcript-version="2">
 are no issues here. Notice that there is
 </span>
 <span data-rw-start="710.16" data-rw-transcript-version="2">
 no sprint planning here. This is
 </span>
 <span data-rw-start="712.12" data-rw-transcript-version="2">
 incentive, context, rules, developer,
 </span>
 <span data-rw-start="715.24" data-rw-transcript-version="2">
 effectively. In order to get there, they
 </span>
 <span data-rw-start="717.24" data-rw-transcript-version="2">
 just launched a bunch of new things.
 </span>
</p>
<p>
 <span data-rw-start="718.48" data-rw-transcript-version="2">
 They have a linear agent that you can
 </span>
 <span data-rw-start="720.96" data-rw-transcript-version="2">
 use to actually do a lot of the work
 </span>
 <span data-rw-start="723.08" data-rw-transcript-version="2">
 against your context. They have a new
 </span>
 <span data-rw-start="724.84" data-rw-transcript-version="2">
 skills product, which lets you codify
 </span>
 <span data-rw-start="726.96" data-rw-transcript-version="2">
 things that are being done over and
 </span>
 <span data-rw-start="728.48" data-rw-transcript-version="2">
 over. And then automations, which will
 </span>
 <span data-rw-start="730.36" data-rw-transcript-version="2">
 allow you to automatically trigger
 </span>
 <span data-rw-start="732.44" data-rw-transcript-version="2">
 things remotely. I’m assuming. Yeah,
 </span>
 <span data-rw-start="734.28" data-rw-transcript-version="2">
 triage will trigger agent workflows the
 </span>
 <span data-rw-start="735.84" data-rw-transcript-version="2">
 moment an issue enters the system. Every
 </span>
 <span data-rw-start="737.64" data-rw-transcript-version="2">
 new issue adds context to your
 </span>
 <span data-rw-start="738.92" data-rw-transcript-version="2">
 workspace, and Linear can now
 </span>
 <span data-rw-start="740.08" data-rw-transcript-version="2">
 intelligently refine, synthesize, or
 </span>
 <span data-rw-start="741.72" data-rw-transcript-version="2">
 Take action on the context the moment it
 </span>
 <span data-rw-start="743.56" data-rw-transcript-version="2">
 arrives.
 </span>
</p>
<p>
 <span data-rw-start="745.76" data-rw-transcript-version="2">
 Cool. I think automations are
 </span>
 <span data-rw-start="747.08" data-rw-transcript-version="2">
 more and more going to become like the
 </span>
 <span data-rw-start="748.92" data-rw-transcript-version="2">
 next new thing. Do I not even have the
 </span>
 <span data-rw-start="750.44" data-rw-transcript-version="2">
 Codex app installed on this computer?
 </span>
 <span data-rw-start="752.08" data-rw-transcript-version="2">
 I don't. I just formatted this, and I've
 </span>
 <span data-rw-start="753.88" data-rw-transcript-version="2">
 been using a better app recently,
 </span>
 <span data-rw-start="757.32" data-rw-transcript-version="2">
 believe it or not. Uh, certain T3 code. I
 </span>
 <span data-rw-start="759.16" data-rw-transcript-version="2">
 want to show a feature in here. Back in
 </span>
 <span data-rw-start="761.88" data-rw-transcript-version="2">
 this lackluster, laggy app that broke my
 </span>
 <span data-rw-start="763.44" data-rw-transcript-version="2">
 brain because of how cool it is to build
 </span>
 <span data-rw-start="765.36" data-rw-transcript-version="2">
 this way, but just doesn't handle the
 </span>
 <span data-rw-start="766.96" data-rw-transcript-version="2">
 scale that we build at, sadly.
 </span>
</p>
<p>
 <span data-rw-start="768.48" data-rw-transcript-version="2">
 So, it does have some really cool things in it.
 </span>
 <span data-rw-start="770.88" data-rw-transcript-version="2">
 I think the skills browser and creator
 </span>
 <span data-rw-start="772.8" data-rw-transcript-version="2">
 thing is relatively cool. I've been able
 </span>
 <span data-rw-start="774.4" data-rw-transcript-version="2">
 to make some useful things in this. It's
 </span>
 <span data-rw-start="776.44" data-rw-transcript-version="2">
 not my favorite thing, but it's decent.
 </span>
</p>
<p>
 <span data-rw-start="778.72" data-rw-transcript-version="2">
 I don't think the official OpenAI docs
 </span>
 <span data-rw-start="780.88" data-rw-transcript-version="2">
 skill should be included by default.
 </span>
 <span data-rw-start="782.36" data-rw-transcript-version="2">
 That's cringe. Happy I went to this
 </span>
 <span data-rw-start="783.88" data-rw-transcript-version="2">
 page. I had a bunch of useless skills
 </span>
 <span data-rw-start="785.48" data-rw-transcript-version="2">
 that were on by default. That is fixed
 </span>
 <span data-rw-start="786.72" data-rw-transcript-version="2">
 now, though. But that's not the time I'm
 </span>
 <span data-rw-start="786.72" data-rw-transcript-version="2">
 here for. I'm here for automations. I
 </span>
 <span data-rw-start="788.32" data-rw-transcript-version="2">
 Will be honest, I overlooked automations
 </span>
 <span data-rw-start="791.16" data-rw-transcript-version="2">
 when I started using the Codex app, and
 </span>
 <span data-rw-start="793.32" data-rw-transcript-version="2">
 I've noticed that most devs have as
 </span>
 <span data-rw-start="795.16" data-rw-transcript-version="2">
 well. For whatever reason, devs just
 </span>
 <span data-rw-start="797.2" data-rw-transcript-version="2">
 aren't as into this side of things. And
 </span>
 <span data-rw-start="800.12" data-rw-transcript-version="2">
 I kind of get why. A lot of the examples
 </span>
 <span data-rw-start="802.4" data-rw-transcript-version="2">
 are just not very good for developers.
 </span>
</p>
<p>
 <span data-rw-start="804.68" data-rw-transcript-version="2">
 Like, what dev wants to summarize
 </span>
 <span data-rw-start="807.12" data-rw-transcript-version="2">
 yesterday's get activity for a stand-up?
 </span>
 <span data-rw-start="809.36" data-rw-transcript-version="2">
 They don't, I promise you. What dev
 </span>
 <span data-rw-start="811.36" data-rw-transcript-version="2">
 wants to synthesize this week’s PRs,
 </span>
 <span data-rw-start="813.4" data-rw-transcript-version="2">
 rollouts, and incidents and reviews into
 </span>
 <span data-rw-start="815.2" data-rw-transcript-version="2">
 a weekly update? The kind that's not
 </span>
 <span data-rw-start="817" data-rw-transcript-version="2">
 very good at coding and is on a quick
 </span>
 <span data-rw-start="818.68" data-rw-transcript-version="2">
 path to become a PM or a designer of
 </span>
 <span data-rw-start="820.64" data-rw-transcript-version="2">
 some form. And then release prep. Draft
 </span>
 <span data-rw-start="823.24" data-rw-transcript-version="2">
 weekly release notes for merged PRs.
 </span>
</p>
<p>
 <span data-rw-start="825.32" data-rw-transcript-version="2">
 Before tagging, verify change logs,
 </span>
 <span data-rw-start="827.28" data-rw-transcript-version="2">
 migrations, feature flags, and tests.
 </span>
 <span data-rw-start="829.36" data-rw-transcript-version="2">
 Let's say I want to set up one of these.
 </span>
 <span data-rw-start="831.04" data-rw-transcript-version="2">
 I click it. I can set a schedule, so I
 </span>
 <span data-rw-start="833.76" data-rw-transcript-version="2">
 can choose when I want it to fire. If I
 </span>
 <span data-rw-start="835.4" data-rw-transcript-version="2">
 want it to fire daily at 9:00 a.m., I
 </span>
 <span data-rw-start="837.08" data-rw-transcript-version="2">
 can choose which project it fires in. It
 </span>
 <span data-rw-start="838.8" data-rw-transcript-version="2">
 will spin up a work tree and then go do
 </span>
 <span data-rw-start="840.28" data-rw-transcript-version="2">
 The thing. You can even choose which
 </span>
 <span data-rw-start="841.64" data-rw-transcript-version="2">
 model and reasoning levels with this
 </span>
 <span data-rw-start="843.16" data-rw-transcript-version="2">
 really weird pinned thing there. God, I
 </span>
 <span data-rw-start="845.36" data-rw-transcript-version="2">
 hate this UI. Whatever, you get the
 </span>
 <span data-rw-start="847.28" data-rw-transcript-version="2">
 idea. This is a concept that I
 </span>
 <span data-rw-start="849.68" data-rw-transcript-version="2">
 personally didn't think was the coolest
 </span>
 <span data-rw-start="852.48" data-rw-transcript-version="2">
 thing ever. It wasn't a big, oh yeah,
 </span>
 <span data-rw-start="854.84" data-rw-transcript-version="2">
 this is great. Something I learned
 </span>
 <span data-rw-start="856.52" data-rw-transcript-version="2">
 recently is that there's an increasing
 </span>
 <span data-rw-start="858.72" data-rw-transcript-version="2">
 number of non-devs using the Codex app
 </span>
 <span data-rw-start="861.6" data-rw-transcript-version="2">
 lately. A lot of them are doing it
 </span>
 <span data-rw-start="863.44" data-rw-transcript-version="2">
 because they have things on their
 </span>
 <span data-rw-start="864.8" data-rw-transcript-version="2">
 computer that they wanted to be able to
 </span>
 <span data-rw-start="866.52" data-rw-transcript-version="2">
 do, but even more using it from what
 </span>
 <span data-rw-start="868.32" data-rw-transcript-version="2">
 I've seen because they love automations.
 </span>
</p>
<p>
 <span data-rw-start="871.2" data-rw-transcript-version="2">
 I know a comms person at a startup
 </span>
 <span data-rw-start="872.48" data-rw-transcript-version="2">
 that's using an automation to go check a
 </span>
 <span data-rw-start="875" data-rw-transcript-version="2">
 bunch of different websites and news
 </span>
 <span data-rw-start="876.68" data-rw-transcript-version="2">
 sources for mentions of their company in
 </span>
 <span data-rw-start="879" data-rw-transcript-version="2">
 order to then bring it into Slack. So,
 </span>
 <span data-rw-start="881.88" data-rw-transcript-version="2">
 the automation will fire, go find all of
 </span>
 <span data-rw-start="884.08" data-rw-transcript-version="2">
 this info, and then DM her on Slack the
 </span>
 <span data-rw-start="886.24" data-rw-transcript-version="2">
 results. And this person's never been a
 </span>
 <span data-rw-start="888.16" data-rw-transcript-version="2">
 dev before. They had friends at the
 </span>
 <span data-rw-start="889.6" data-rw-transcript-version="2">
 company using Codex app. They thought it
 </span>
 <span data-rw-start="891.48" data-rw-transcript-version="2">
 It was cool to check out, and they just
 </span>
 <span data-rw-start="892.96" data-rw-transcript-version="2">
 fell in love with automations. They have
 </span>
 <span data-rw-start="894" data-rw-transcript-version="2">
 like 30 plus of them now doing all sorts
 </span>
 <span data-rw-start="895.92" data-rw-transcript-version="2">
 of [ \_\_ ] to normies. This is the first
 </span>
</p>
<p>
 <span data-rw-start="898.48" data-rw-transcript-version="2">
 time they could automate part of their
 </span>
 <span data-rw-start="900.56" data-rw-transcript-version="2">
 life or work. And I don't think most
 </span>
 <span data-rw-start="903.08" data-rw-transcript-version="2">
 developers think this way because, to an
 </span>
 <span data-rw-start="905.12" data-rw-transcript-version="2">
 extent, we already learned how to
 </span>
 <span data-rw-start="906.88" data-rw-transcript-version="2">
 automate things. That's why we're
 </span>
 <span data-rw-start="908.2" data-rw-transcript-version="2">
 developers. But, we know what work it is to
 </span>
 <span data-rw-start="911.12" data-rw-transcript-version="2">
 automate things, so we often don't
 </span>
 <span data-rw-start="912.92" data-rw-transcript-version="2">
 bother because writing the code to
 </span>
 <span data-rw-start="915.2" data-rw-transcript-version="2">
 automate something like grabbing all of
 </span>
 <span data-rw-start="917.12" data-rw-transcript-version="2">
 the commits that you did in the last
 </span>
 <span data-rw-start="918.56" data-rw-transcript-version="2">
 week and dumping that as in some
 </span>
 <span data-rw-start="920.36" data-rw-transcript-version="2">
 information to you on Slack or whatever.
 </span>
</p>
<p>
 <span data-rw-start="922.4" data-rw-transcript-version="2">
 That's code all of us can write. We're
 </span>
 <span data-rw-start="923.72" data-rw-transcript-version="2">
 all devs. Almost every single person
 </span>
 <span data-rw-start="925.16" data-rw-transcript-version="2">
 watching this is good enough at writing
 </span>
 <span data-rw-start="926.6" data-rw-transcript-version="2">
 code to do something like that. But,
 </span>
 <span data-rw-start="928.76" data-rw-transcript-version="2">
 it's also a lot of work to do it. So,
 </span>
 <span data-rw-start="930.2" data-rw-transcript-version="2">
 we've kind of trained our brains to
 </span>
 <span data-rw-start="931.64" data-rw-transcript-version="2">
 ignore the urge to automate things that
 </span>
 <span data-rw-start="933.6" data-rw-transcript-version="2">
 aren't super useful. People who have
 </span>
 <span data-rw-start="937.6" data-rw-transcript-version="2">
 Of a sudden able, and now that it's
 </span>
 <span data-rw-start="939.52" data-rw-transcript-version="2">
 easier, they're doing it even more. I
 </span>
 <span data-rw-start="941.6" data-rw-transcript-version="2">
 know way more people doing automations
 </span>
 <span data-rw-start="943.04" data-rw-transcript-version="2">
 outside of the dev world than inside of
 </span>
 <span data-rw-start="944.92" data-rw-transcript-version="2">
 it. And if I'm being frank, and this is
 </span>
 <span data-rw-start="946.56" data-rw-transcript-version="2">
 not meant to be an insult, this is
 </span>
</p>
<p>
 <span data-rw-start="947.88" data-rw-transcript-version="2">
 an observation. The devs I find who are
 </span>
 <span data-rw-start="949.72" data-rw-transcript-version="2">
 using automations a lot, who are using
 </span>
 <span data-rw-start="951.36" data-rw-transcript-version="2">
 open claw a lot, and using those types
 </span>
 <span data-rw-start="953" data-rw-transcript-version="2">
 of things, tend to be the less good devs
 </span>
 <span data-rw-start="955.68" data-rw-transcript-version="2">
 that I've worked with. No offense to
 </span>
 <span data-rw-start="957.32" data-rw-transcript-version="2">
 these two particular people, but two of
 </span>
 <span data-rw-start="958.8" data-rw-transcript-version="2">
 the actual worst devs I've ever seen in
 </span>
 <span data-rw-start="960.72" data-rw-transcript-version="2">
 my life are open claw gods. One of them
 </span>
 <span data-rw-start="963.96" data-rw-transcript-version="2">
 built their own equivalent of open claw
 </span>
 <span data-rw-start="965.72" data-rw-transcript-version="2">
 before it came out, and it barely
 </span>
 <span data-rw-start="967.24" data-rw-transcript-version="2">
 worked, and it resulted in her spam
 </span>
 <span data-rw-start="968.72" data-rw-transcript-version="2">
 texting me dozens of times a day as she
 </span>
 <span data-rw-start="970.4" data-rw-transcript-version="2">
 was trying to make it function at all.
 </span>
</p>
<p>
 <span data-rw-start="971.84" data-rw-transcript-version="2">
 It's kind of weird. Them liking
 </span>
 <span data-rw-start="973.6" data-rw-transcript-version="2">
 automations doesn't make them bad, but
 </span>
 <span data-rw-start="975.4" data-rw-transcript-version="2">
 it almost seems like we as devs have
 </span>
 <span data-rw-start="977.28" data-rw-transcript-version="2">
 wired our brain against this type of
 </span>
 <span data-rw-start="979.16" data-rw-transcript-version="2">
 thing. And people who are less wired
 </span>
 <span data-rw-start="980.8" data-rw-transcript-version="2">
 into the dev world are more wired in a
 </span>
 <span data-rw-start="983" data-rw-transcript-version="2">
 Way, where they're willing to do this
 </span>
 <span data-rw-start="984.08" data-rw-transcript-version="2">
 type of thing. So, while the linear
 </span>
 <span data-rw-start="985.8" data-rw-transcript-version="2">
 automations that they're describing here
 </span>
 <span data-rw-start="987.56" data-rw-transcript-version="2">
 might seem not that cool to us as devs,
 </span>
 <span data-rw-start="990.24" data-rw-transcript-version="2">
 I know, to me, it's like my instinct is,
 </span>
 <span data-rw-start="991.839" data-rw-transcript-version="2">
 "Oh, whatever. What is it actually going
 </span>
 <span data-rw-start="994" data-rw-transcript-version="2">
 to add?" I promise you, the PMs, the
 </span>
 <span data-rw-start="997" data-rw-transcript-version="2">
 leads, the people who don't code are
 </span>
 <span data-rw-start="999" data-rw-transcript-version="2">
 going to love this, and they're going to
 </span>
 <span data-rw-start="1000.96" data-rw-transcript-version="2">
 massage it into something useful almost
 </span>
 <span data-rw-start="1003.48" data-rw-transcript-version="2">
 certainly. I will say the end here is
 </span>
 <span data-rw-start="1005.72" data-rw-transcript-version="2">
 kind of cringe. These updates build on
 </span>
 <span data-rw-start="1007.839" data-rw-transcript-version="2">
 our early work in triage intelligence,
 </span>
 <span data-rw-start="1009.88" data-rw-transcript-version="2">
 deep integrations with cloud coding
 </span>
 <span data-rw-start="1011.8" data-rw-transcript-version="2">
 agents, and other AI tools. By grounding
 </span>
 <span data-rw-start="1013.88" data-rw-transcript-version="2">
 agents in the full context of your
 </span>
 <span data-rw-start="1015.36" data-rw-transcript-version="2">
 product and code base, we're collapsing
 </span>
 <span data-rw-start="1017.08" data-rw-transcript-version="2">
 the distance between an idea and its
 </span>
</p>
<p>
 <span data-rw-start="1018.6" data-rw-transcript-version="2">
 implementation. Issue tracking was built
 </span>
 <span data-rw-start="1020.4" data-rw-transcript-version="2">
 for hand-offs. Linear turns context into
 </span>
 <span data-rw-start="1023.08" data-rw-transcript-version="2">
 execution. So, here's my hot take. I
 </span>
 <span data-rw-start="1025.88" data-rw-transcript-version="2">
 personally have not found much value in
 </span>
 <span data-rw-start="1027.319" data-rw-transcript-version="2">
 things like G stack. If you're not
 </span>
 <span data-rw-start="1028.8" data-rw-transcript-version="2">
 familiar, I might do a whole video on it
 </span>
 <span data-rw-start="1030.439" data-rw-transcript-version="2">
 in the near future. The point of G stack
 </span>
 <span data-rw-start="1032.52" data-rw-transcript-version="2">
 Is it gives you a bunch of skills that
 </span>
 <span data-rw-start="1035.24" data-rw-transcript-version="2">
 are effectively different characters
 </span>
 <span data-rw-start="1037.72" data-rw-transcript-version="2">
 that are being played by the models to
 </span>
 <span data-rw-start="1040.12" data-rw-transcript-version="2">
 do specific types of things. Gary built
 </span>
 <span data-rw-start="1043" data-rw-transcript-version="2">
 these specialists. The CEO, founder, the
 </span>
 <span data-rw-start="1046.04" data-rw-transcript-version="2">
 eng manager, the senior designer, the
 </span>
 <span data-rw-start="1047.88" data-rw-transcript-version="2">
 design partner. It should be clear,
 </span>
 <span data-rw-start="1049.44" data-rw-transcript-version="2">
 these aren't like code or anything
 </span>
 <span data-rw-start="1050.68" data-rw-transcript-version="2">
 complex. These are just markdown. These
 </span>
 <span data-rw-start="1052.36" data-rw-transcript-version="2">
 are just text files that describe how
 </span>
 <span data-rw-start="1054.6" data-rw-transcript-version="2">
 the model should behave in these times
 </span>
 <span data-rw-start="1056.64" data-rw-transcript-version="2">
 and in these particular requests. For
 </span>
 <span data-rw-start="1059.12" data-rw-transcript-version="2">
 what it is worth, I think this is
 </span>
 <span data-rw-start="1060.46" data-rw-transcript-version="2">
 [snorts] cringe as [ \_\_ ] There are some
 </span>
 <span data-rw-start="1062.04" data-rw-transcript-version="2">
 fun ideas in here like {slash} codex,
 </span>
 <span data-rw-start="1064.2" data-rw-transcript-version="2">
 which cuz this is built for Claude code.
 </span>
</p>
<p>
 <span data-rw-start="1066.2" data-rw-transcript-version="2">
 This will call the codex CLI from Claude
 </span>
 <span data-rw-start="1068.68" data-rw-transcript-version="2">
 code to review the changes and give a
 </span>
 <span data-rw-start="1071.4" data-rw-transcript-version="2">
 second pass saying, "Yeah, I'm codex. I
 </span>
 <span data-rw-start="1073.4" data-rw-transcript-version="2">
 think that's good or bad." Chat's
 </span>
 <span data-rw-start="1074.72" data-rw-transcript-version="2">
 already figured it out. So, this is how
 </span>
 <span data-rw-start="1076.36" data-rw-transcript-version="2">
 devs role play. Yeah. My hottest take is
 </span>
 <span data-rw-start="1079.48" data-rw-transcript-version="2">
 that the way we have broken up work
 </span>
 <span data-rw-start="1081.72" data-rw-transcript-version="2">
 historically only made sense because
 </span>
 <span data-rw-start="1084.24" data-rw-transcript-version="2">
 developers and other fields that we
 </span>
 <span data-rw-start="1086.2" data-rw-transcript-version="2">
 Interfaced with were different enough
 </span>
 <span data-rw-start="1088.52" data-rw-transcript-version="2">
 and hard enough to find and level up in
 </span>
 <span data-rw-start="1090.72" data-rw-transcript-version="2">
 that we needed to have these roles so
 </span>
 <span data-rw-start="1092.52" data-rw-transcript-version="2">
 that we could get the work done and meet
 </span>
 <span data-rw-start="1095.08" data-rw-transcript-version="2">
 the quality bars that we needed to. But,
 </span>
 <span data-rw-start="1096.8" data-rw-transcript-version="2">
 let's be real here. If the model is
 </span>
 <span data-rw-start="1098.28" data-rw-transcript-version="2">
 smart enough to be the CEO, to be the
 </span>
</p>
<p>
 <span data-rw-start="1100.28" data-rw-transcript-version="2">
 eng manager, to be the designer, to be
 </span>
 <span data-rw-start="1101.88" data-rw-transcript-version="2">
 the design partner, to be the staff
 </span>
 <span data-rw-start="1103.44" data-rw-transcript-version="2">
 engineer, to be the debugger, to be a
 </span>
 <span data-rw-start="1104.84" data-rw-transcript-version="2">
 designer who also knows how to code, to
 </span>
 <span data-rw-start="1106.68" data-rw-transcript-version="2">
 be the QA lead and reporter. If the
 </span>
 <span data-rw-start="1108.36" data-rw-transcript-version="2">
 model is smart enough to be all of these
 </span>
 <span data-rw-start="1109.84" data-rw-transcript-version="2">
 things, why are we still defining these
 </span>
 <span data-rw-start="1112.52" data-rw-transcript-version="2">
 things? Why do we need to have a thing
 </span>
 <span data-rw-start="1115.8" data-rw-transcript-version="2">
 for this anymore? My hot take is that
 </span>
 <span data-rw-start="1118.4" data-rw-transcript-version="2">
 the way we have broken up all these
 </span>
 <span data-rw-start="1120.48" data-rw-transcript-version="2">
 pieces made sense when humans did it and
 </span>
 <span data-rw-start="1123.32" data-rw-transcript-version="2">
 a given human could only do one of these
 </span>
 <span data-rw-start="1125.4" data-rw-transcript-version="2">
 things. Now that AI is smart enough to
 </span>
 <span data-rw-start="1126.96" data-rw-transcript-version="2">
 do most of these things, the way we
 </span>
 <span data-rw-start="1129.04" data-rw-transcript-version="2">
 break up the work no longer makes sense.
 </span>
</p>
<p>
 <span data-rw-start="1131.6" data-rw-transcript-version="2">
 And I see this all over the place. One
 </span>
 <span data-rw-start="1133.6" data-rw-transcript-version="2">
 of the places I see it the most is
 </span>
 <span data-rw-start="1135.44" data-rw-transcript-version="2">
 multi-step planning processes. There’s
 </span>
 <span data-rw-start="1137.96" data-rw-transcript-version="2">
 No reason for planning to take hours.
 </span>
</p>
<p>
 <span data-rw-start="1140.52" data-rw-transcript-version="2">
 There's no reason for planning to fill
 </span>
 <span data-rw-start="1142.2" data-rw-transcript-version="2">
 your entire context. There's no reason
 </span>
 <span data-rw-start="1144.24" data-rw-transcript-version="2">
 that planning should have lots of
 </span>
 <span data-rw-start="1145.64" data-rw-transcript-version="2">
 different sub-plans and steps and
 </span>
 <span data-rw-start="1147.68" data-rw-transcript-version="2">
 process and specs and all of that.
 </span>
 <span data-rw-start="1149.36" data-rw-transcript-version="2">
 Models are for the most part
 </span>
 <span data-rw-start="1151.32" data-rw-transcript-version="2">
 good enough. So, instead of spending all
 </span>
 <span data-rw-start="1153.32" data-rw-transcript-version="2">
 of this time after you take in the
 </span>
 <span data-rw-start="1155.64" data-rw-transcript-version="2">
 request, bug report, or whatever, to
 </span>
 <span data-rw-start="1157.52" data-rw-transcript-version="2">
 build all of these additional pieces in
 </span>
 <span data-rw-start="1160.44" data-rw-transcript-version="2">
 for context, like the specs, technical
 </span>
 <span data-rw-start="1162.44" data-rw-transcript-version="2">
 design, the plans, the decisions, the
 </span>
 <span data-rw-start="1164.24" data-rw-transcript-version="2">
 summaries, and all that just for
 </span>
 <span data-rw-start="1165.72" data-rw-transcript-version="2">
 the model to go do the build, why not
 </span>
 <span data-rw-start="1167.72" data-rw-transcript-version="2">
 have it start with a build but accessing
 </span>
 <span data-rw-start="1169.68" data-rw-transcript-version="2">
 all of these things as tools? What if
 </span>
 <span data-rw-start="1171.68" data-rw-transcript-version="2">
 the model could do a first pass, use
 </span>
</p>
<p>
 <span data-rw-start="1174.08" data-rw-transcript-version="2">
 these things, figure out what doesn’t
 </span>
 <span data-rw-start="1175.52" data-rw-transcript-version="2">
 doesn’t work, and then have the first
 </span>
 <span data-rw-start="1177.36" data-rw-transcript-version="2">
 pass be the plan, so to speak? Not that
 </span>
 <span data-rw-start="1179.88" data-rw-transcript-version="2">
 the code is going to be used directly,
 </span>
 <span data-rw-start="1181.76" data-rw-transcript-version="2">
 but the process of it building and
 </span>
 <span data-rw-start="1183.52" data-rw-transcript-version="2">
 touching all of those things is enough
 </span>
 <span data-rw-start="1185.56" data-rw-transcript-version="2">
 for you to realize, oh, I guess that’s
 </span>
 <span data-rw-start="1187.32" data-rw-transcript-version="2">
 How this works. I guess that's where the
 </span>
 <span data-rw-start="1188.68" data-rw-transcript-version="2">
 flaws are. And then from there, make a
 </span>
 <span data-rw-start="1190.88" data-rw-transcript-version="2">
 much simpler plan that actually touches
 </span>
 <span data-rw-start="1193.28" data-rw-transcript-version="2">
 the things you need, and then go build
 </span>
 <span data-rw-start="1194.56" data-rw-transcript-version="2">
 it again. We've went through this loop
 </span>
 <span data-rw-start="1195.76" data-rw-transcript-version="2">
 already with MCP, funny enough, where we
 </span>
 <span data-rw-start="1197.4" data-rw-transcript-version="2">
 thought this new standard was going to
 </span>
 <span data-rw-start="1198.72" data-rw-transcript-version="2">
 be the best way for models to access
 </span>
 <span data-rw-start="1200.44" data-rw-transcript-version="2">
 data and do things, and then it sucked.
 </span>
</p>
<p>
 <span data-rw-start="1202.84" data-rw-transcript-version="2">
 So, we ended up moving it back to code,
 </span>
 <span data-rw-start="1204.84" data-rw-transcript-version="2">
 because models are really good at
 </span>
 <span data-rw-start="1206.12" data-rw-transcript-version="2">
 writing code. And once the models could
 </span>
 <span data-rw-start="1207.76" data-rw-transcript-version="2">
 use code to use MCP, all of a sudden it
 </span>
 <span data-rw-start="1210.08" data-rw-transcript-version="2">
 got way, way better and way more
 </span>
 <span data-rw-start="1212.08" data-rw-transcript-version="2">
 performant and reliable. I think we're
 </span>
 <span data-rw-start="1213.8" data-rw-transcript-version="2">
 going to go through the same thing here.
 </span>
</p>
<p>
 <span data-rw-start="1215.2" data-rw-transcript-version="2">
 We're in a weird spot now, where we're
 </span>
 <span data-rw-start="1216.96" data-rw-transcript-version="2">
 going to reinvent everything based on
 </span>
 <span data-rw-start="1219.16" data-rw-transcript-version="2">
 how it always worked, even though it
 </span>
 <span data-rw-start="1220.84" data-rw-transcript-version="2">
 doesn't [ \_\_ ] matter. And what we're
 </span>
 <span data-rw-start="1222.64" data-rw-transcript-version="2">
 going to end up back at is code as
 </span>
 <span data-rw-start="1224.8" data-rw-transcript-version="2">
 planning. We're going to reinvent plans
 </span>
 <span data-rw-start="1227.12" data-rw-transcript-version="2">
 a million [ \_\_ ] times over the next
 </span>
 <span data-rw-start="1228.92" data-rw-transcript-version="2">
 year, and then we're going to just go
 </span>
 <span data-rw-start="1230.6" data-rw-transcript-version="2">
 back to code. I like what Naman had to
 </span>
 <span data-rw-start="1232.56" data-rw-transcript-version="2">
 Say here. This is the functional versus
 </span>
 <span data-rw-start="1234.4" data-rw-transcript-version="2">
 product divisions at companies. I
 </span>
 <span data-rw-start="1236.44" data-rw-transcript-version="2">
 absolutely agree there. Here's a fun
 </span>
 <span data-rw-start="1238.24" data-rw-transcript-version="2">
 fact I learned recently. Did you know
 </span>
 <span data-rw-start="1239.76" data-rw-transcript-version="2">
 that GitHub has a separate product and
 </span>
 <span data-rw-start="1241.88" data-rw-transcript-version="2">
 engineering org? Did you know that they
 </span>
 <span data-rw-start="1243.56" data-rw-transcript-version="2">
 share zero leadership? That product and
 </span>
 <span data-rw-start="1245.96" data-rw-transcript-version="2">
 eng, the people who actually build the
 </span>
 <span data-rw-start="1247.44" data-rw-transcript-version="2">
 product, cannot interact with each
 </span>
 <span data-rw-start="1249.2" data-rw-transcript-version="2">
 other? Because I didn't know that until
 </span>
 <span data-rw-start="1250.76" data-rw-transcript-version="2">
 recently, and it explained a lot of why
 </span>
 <span data-rw-start="1252.44" data-rw-transcript-version="2">
 GitHub is a [ \_\_ ] disaster. I don't
 </span>
 <span data-rw-start="1254.24" data-rw-transcript-version="2">
 see how GitHub can ever get better if
 </span>
 <span data-rw-start="1255.88" data-rw-transcript-version="2">
 the product people don't code and the
 </span>
</p>
<p>
 <span data-rw-start="1257.48" data-rw-transcript-version="2">
 devs don't make product decisions. It kinda
 </span>
 <span data-rw-start="1259.2" data-rw-transcript-version="2">
 makes sense that GitHub is an
 </span>
 <span data-rw-start="1260.88" data-rw-transcript-version="2">
 absolute [ \_\_ ] [ \_\_ ] show. And if we
 </span>
 <span data-rw-start="1262.52" data-rw-transcript-version="2">
 keep pretending that way of building
 </span>
 <span data-rw-start="1264.04" data-rw-transcript-version="2">
 makes sense, we're going to keep
 </span>
 <span data-rw-start="1265.36" data-rw-transcript-version="2">
 reinventing shitty processes that only
 </span>
 <span data-rw-start="1267.6" data-rw-transcript-version="2">
 worked for humans. There is a way I
 </span>
 <span data-rw-start="1269.2" data-rw-transcript-version="2">
 could be wrong here though, and I don't
 </span>
 <span data-rw-start="1270.56" data-rw-transcript-version="2">
 know, because I haven't done enough of this
 </span>
 <span data-rw-start="1272.2" data-rw-transcript-version="2">
 like code-as-planned-type thing, because
 </span>
 <span data-rw-start="1274.16" data-rw-transcript-version="2">
 I'm too busy to do either coding as a
 </span>
 <span data-rw-start="1275.92" data-rw-transcript-version="2">
 Plan or coding in general. I have way
 </span>
 <span data-rw-start="1277.4" data-rw-transcript-version="2">
 too much [ \_\_ ] [ \_\_ ] going on. I do
 </span>
 <span data-rw-start="1278.8" data-rw-transcript-version="2">
 plan to do this, pun intended, but there
 </span>
 <span data-rw-start="1281" data-rw-transcript-version="2">
 is a potential failure case in the way
 </span>
 <span data-rw-start="1282.4" data-rw-transcript-version="2">
 I'm thinking of this that I am imagining
 </span>
 <span data-rw-start="1284.2" data-rw-transcript-version="2">
 now, which is that the reason agents can
 </span>
 <span data-rw-start="1286.28" data-rw-transcript-version="2">
 work better this way is because they’re
 </span>
 <span data-rw-start="1287.68" data-rw-transcript-version="2">
 trained on data from humans and there’s
 </span>
 <span data-rw-start="1289.48" data-rw-transcript-version="2">
 enough data of humans working this way
 </span>
 <span data-rw-start="1291.24" data-rw-transcript-version="2">
 that eventually the AI can do it too.
 </span>
</p>
<p>
 <span data-rw-start="1293.24" data-rw-transcript-version="2">
 Perhaps. And it might be better for the
 </span>
 <span data-rw-start="1294.88" data-rw-transcript-version="2">
 AI to behave like a human than for it to
 </span>
 <span data-rw-start="1296.56" data-rw-transcript-version="2">
 behave like an AI because the AI is
 </span>
 <span data-rw-start="1298.16" data-rw-transcript-version="2">
 trained on humans in the first place.
 </span>
</p>
<p>
 <span data-rw-start="1299.56" data-rw-transcript-version="2">
 Yeah. I don’t think that will be the
 </span>
 <span data-rw-start="1301.32" data-rw-transcript-version="2">
 case though. I still pretty firmly
 </span>
 <span data-rw-start="1302.88" data-rw-transcript-version="2">
 believe that the best plan is a
 </span>
 <span data-rw-start="1304.16" data-rw-transcript-version="2">
 prototype, and if you still need a plan
 </span>
 <span data-rw-start="1305.84" data-rw-transcript-version="2">
 after that, you’ll be able to write a
 </span>
 <span data-rw-start="1307.36" data-rw-transcript-version="2">
 much more informed one after you make a
 </span>
 <span data-rw-start="1309.76" data-rw-transcript-version="2">
 first trial version of the thing. So
 </span>
 <span data-rw-start="1311.96" data-rw-transcript-version="2">
 Instead of all of this nonsense, I would
 </span>
 <span data-rw-start="1313.8" data-rw-transcript-version="2">
 take the handful of useful pieces of
 </span>
 <span data-rw-start="1315.44" data-rw-transcript-version="2">
 context here, throw those into a tool
 </span>
 <span data-rw-start="1317.52" data-rw-transcript-version="2">
 call of some form, and then tell the
 </span>
 <span data-rw-start="1319.08" data-rw-transcript-version="2">
 Model, "I want to build a scrappy
 </span>
 <span data-rw-start="1320.92" data-rw-transcript-version="2">
 prototype of this feature that was
 </span>
 <span data-rw-start="1323.04" data-rw-transcript-version="2">
 described in whatever request bug
 </span>
 <span data-rw-start="1325.04" data-rw-transcript-version="2">
 reporter feedback was provided. Help me
 </span>
</p>
<p>
 <span data-rw-start="1327.24" data-rw-transcript-version="2">
 identify the scope of this and then
 </span>
 <span data-rw-start="1329.04" data-rw-transcript-version="2">
 build this first version so that we can
 </span>
 <span data-rw-start="1331" data-rw-transcript-version="2">
 understand what foot guns and other
 </span>
 <span data-rw-start="1332.84" data-rw-transcript-version="2">
 shortcomings might exist in the code
 </span>
 <span data-rw-start="1334.16" data-rw-transcript-version="2">
 base as we implement this."
 </span>
 <span data-rw-start="1335.72" data-rw-transcript-version="2">
 You get this early version, you get a bunch of the
 </span>
 <span data-rw-start="1337.28" data-rw-transcript-version="2">
 things that were hard about it, and then
 </span>
 <span data-rw-start="1338.84" data-rw-transcript-version="2">
 you can go build the right one. I think
 </span>
 <span data-rw-start="1340.36" data-rw-transcript-version="2">
 that's probably going to be a better
 </span>
 <span data-rw-start="1341.4" data-rw-transcript-version="2">
 bet. I could be wrong, but having built
 </span>
 <span data-rw-start="1343.12" data-rw-transcript-version="2">
 with a lot of this [ \_\_ ] myself, that has
 </span>
 <span data-rw-start="1344.64" data-rw-transcript-version="2">
 been generally the direction that has
 </span>
 <span data-rw-start="1346.72" data-rw-transcript-version="2">
 worked for me. Hell, I've been building
 </span>
</p>
<p>
 <span data-rw-start="1348.2" data-rw-transcript-version="2">
 this way since before AI. I cannot tell
 </span>
 <span data-rw-start="1350.08" data-rw-transcript-version="2">
 you how many times I filed a shitty PR
 </span>
 <span data-rw-start="1352.6" data-rw-transcript-version="2">
 to one of our repos just to showcase the
 </span>
 <span data-rw-start="1354.64" data-rw-transcript-version="2">
 UX or DX that I had in mind and then
 </span>
 <span data-rw-start="1357.16" data-rw-transcript-version="2">
 poor Julius had to go make it into
 </span>
 <span data-rw-start="1358.6" data-rw-transcript-version="2">
 actual production ready code. As Flambo
 </span>
 <span data-rw-start="1360.48" data-rw-transcript-version="2">
 said in shot, "Love this. Build it three
 </span>
 <span data-rw-start="1362.16" data-rw-transcript-version="2">
 times and throw away the first two."
 </span>
 <span data-rw-start="1363.72" data-rw-transcript-version="2">
 Yeah. This didn't make sense when code
 </span>
 <span data-rw-start="1365.4" data-rw-transcript-version="2">
 was expensive, but now code is cheap as
 </span>
 <span data-rw-start="1367.36" data-rw-transcript-version="2">
 [ \_\_ ] Build the code. Stop inventing all
 </span>
 <span data-rw-start="1369.2" data-rw-transcript-version="2">
 this [ \_\_ ]. So, in some senses, Linear
 </span>
 <span data-rw-start="1371.32" data-rw-transcript-version="2">
 is far ahead of the curve here. In
 </span>
 <span data-rw-start="1373.28" data-rw-transcript-version="2">
 others, I think they're still thinking a
 </span>
</p>
<p>
 <span data-rw-start="1374.96" data-rw-transcript-version="2">
 little too much about how teams were
 </span>
 <span data-rw-start="1377.4" data-rw-transcript-version="2">
 split up historically and not enough
 </span>
 <span data-rw-start="1379.24" data-rw-transcript-version="2">
 about how that's going to change. And
 </span>
 <span data-rw-start="1380.68" data-rw-transcript-version="2">
 I’ve also never been so confident that
 </span>
 <span data-rw-start="1381.92" data-rw-transcript-version="2">
 Jira is [ \_\_ ] because you know they aren’t
 </span>
 <span data-rw-start="1383.96" data-rw-transcript-version="2">
 thinking about any of this. They are
 </span>
 <span data-rw-start="1385.4" data-rw-transcript-version="2">
 thinking so little about this that they
 </span>
 <span data-rw-start="1387.12" data-rw-transcript-version="2">
 bought one of my least favorite
 </span>
 <span data-rw-start="1388.52" data-rw-transcript-version="2">
 companies, the browser company, which is
 </span>
 <span data-rw-start="1390.16" data-rw-transcript-version="2">
 a very good fit if you know anything
 </span>
 <span data-rw-start="1391.68" data-rw-transcript-version="2">
 about how Jira and Atlassian work as
 </span>
 <span data-rw-start="1393.48" data-rw-transcript-version="2">
 well as how much the browser company
 </span>
 <span data-rw-start="1395.36" data-rw-transcript-version="2">
 doesn't work.
 </span>
</p>
<p>
 <span data-rw-start="1397.16" data-rw-transcript-version="2">
 Think I’ve said all I have to here. As
 </span>
 <span data-rw-start="1398.72" data-rw-transcript-version="2">
 you can tell, I have a lot of feelings
 </span>
 <span data-rw-start="1400.64" data-rw-transcript-version="2">
 and hopefully this will be useful to you
 </span>
 <span data-rw-start="1402.08" data-rw-transcript-version="2">
 guys. I know a lot of you work at real
 </span>
 <span data-rw-start="1403.48" data-rw-transcript-version="2">
 companies where you're using things like
 </span>
 <span data-rw-start="1404.96" data-rw-transcript-version="2">
 issue trackers and I would love to hear
 </span>
 <span data-rw-start="1406.28" data-rw-transcript-version="2">
 From y'all, what are you guys doing now
 </span>
 <span data-rw-start="1407.72" data-rw-transcript-version="2">
 and how is it changed with AI? Are you
 </span>
 <span data-rw-start="1409.44" data-rw-transcript-version="2">
 using AI with your issues? What does
 </span>
 <span data-rw-start="1411.04" data-rw-transcript-version="2">
 that look like? I'm actually really
 </span>
 <span data-rw-start="1412.4" data-rw-transcript-version="2">
 curious and want to hear more. Let me
 </span>
 <span data-rw-start="1413.72" data-rw-transcript-version="2">
 know, and until next time,
 </span>
 <span data-rw-start="1415.52" data-rw-transcript-version="2">
 peace, nerds.
 </span>
</p>