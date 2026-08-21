---
categories:
  - "[[Resources]]"
domain: engineering
title: "Harnesses in AI: A Deep Dive — Tejas Kumar, IBM"
source: "https://m.youtube.com/watch?v=C_GG5g38vLU&pp=ugUEEgJlbg%3D%3D"
author: "AI Engineer"
published: 2026-05-17
created: 2026-05-18
description: "The agent hit a login page, panicked, reported success anyway, and the upvote"
tags:
  - to-process
  - harness-engineering
---

[music] >> Hello everybody. Everybody's head turned up. Hello, hi. How was lunch? Was it good? You didn't like it, no? It's like British food. Anyway, hi. I'm Tejas. I'm I'll be your first speaker this afternoon. Tejas, that's pronounced like 

Tejas. Don't worry, I'm not Hopefully my my joy in AI is and I've had the privilege of working at a number of different places over my career in one form or the other. It's just been an absolute joy to learn from the best. Today, I'm a AI developer advocate at IBM where we we do things with AI, believe or not. We train frontier models, we build harnesses. It's really it's a fun lab to work in. But that's not what I'm here to talk to you about today. Today, I'm here to talk to you about AI harnesses. AI harnesses. Before I move forward, I would love to 

just have a show of hands. How many of you are like confident in your understanding of AI harnesses? Like you're like I could present this on stage today. Look around. Look around. No, seriously, look around. That's why we're doing this talk. Okay, this is my hope. I want you to If I ask you this at the end of the talk, right? I want you to be like, oh, I I I get it now. That's the whole point. I have literally nothing to gain from this other than I I shared knowledge, okay? Because also this term is kind of everywhere. You may have heard it used like 52,000 times today. And it means different things to 

different people cuz like in the machine learning world, it means like a glorified test suite for machine learning models. But in the AI in the AI world, it means something different. And so today, we're going to understand this in detail. It's a deep dive, but it's 18 minutes long. So let's let's move forward. Um I want to start by talking about why harness. Like why do we use harnesses? And the reason for this is because we pay rent to companies that give us compute, give us inference, give us tokens in return. Some of you maybe work for companies that have frontier models like Anthropic or Google or whatever and 

you maybe What was the term? Token billionaires, yeah? Um I'm not that. I am maybe with Watson models, but but the vast majority of us aren't token billionaires. We we pay rent. We literally $20 a month for Claude Pro. And then you get a context window that's limited and you get like, you know, you you don't get the full hog, so to speak. And the model you rent is is a black box. Like they could at any time, I'm not saying they do, but they could if Opus is somehow not available, they could serve you Sonnet even though it says Opus. You would 

never know, right? And so it's just a big There's too many variables that we cannot control. So why harness? Because the name of the game with harness is reliability. Um I really hope I'm not supposed to stand in front of this white line and then I'm just not in the camera. Anyway, whatever. It's reliability. It's it's making sure that the agents we build do what they do, period. Irrespective of the black box model, irrespective of the of the the thing we rent and so on, okay? Now that we understand why harness, let's 

talk about what a harness even is from first principles. Like let's let's take it all the way back to harnesses that we know and understand. If you've ever, you know, climbed a mountain or something or you've seen someone This is a harness. It's like mountain climbers literally will like harness themselves to what? To a mountain because it's stable. And they can't go off the rails, literally. They they anchor themselves in something stable so that they can't drift too far. Okay, that's that's what a harness is by 

design. When you have any dog owners here? You have dogs? You you walk your dog on a harness, okay? That's why? Because your dog doesn't go and bankrupt you with tokens. Okay? That's what a harness is. But the problem is if we think about what harness, there's really two types. There's one from the machine learning world, which as I mentioned is kind of like a test suite and a test runner. You would give a model some inputs and you see the quality of the outputs. That's not This is not ML engineer Europe. We're going to talk today about the agent harness that is common in AI 

engineering. Okay, so what what is an agent harness? An agent harness and and this is kind of the money shot here. The agent harness is I'm not making money off this. It's just an expression. The agent harness is everything around the model that gives it grounding in reality. It's literally the thing that ties it to a stable environment, okay? An agent So Claude code, for example, can be considered an agent harness. And some of you would say, oh, no, it's a coding agent. Absolutely, it's a coding agent. But it's a harnessed coding agent. An agent 

harness has more or less the same typical suspects, moving parts. Number one, it's got a tool registry. Almost like so Claude code, cursor, codex, they have tools to read from the file system, to write, to execute bash commands, right? They have a tool registry. They have a model and some of them allow you to choose a model, some of them allow you to not. They have a model. They have primitives for managing context. Almost every harnessed agent runtime today will 

compact its own context, right? That's that's that's the job of the harness. Guardrails are another part of a harness. For example, max steps. Anyone using max steps? Do not do more than five tool calls. That's a guardrail. And so if if you do that, you just kill the kill the run, right? An agent loop is another part of an agent harness, which is crazy. This is what some people I've spoken to preparing this talk will say, wait, isn't a harness just the agent loop? No, it's the stuff around the agent loop. In fact, it could be a loop 

around your agent loop. It could be an NM loop. And we'll look at that a little bit in some code. And then finally, there's a verify step. This is, for example, in a coding coding agent, after the work is done, a verify step would be, hey, let's let's run lint, let's run tests, let's make sure nothing broke, right? So almost every I'll use code coding agents as an example, but you could have a harness for anything. And it's it's amazing cuz it really grounds black box models in a stable environment that you control, okay? I'd like to show you 

a demo. And what we're going to do together is we're going to build a harness, a bare bone baby's first harness. Let's call it a poor man's AI harness together so we understand from first principles how this works. We're going to build a computer use agent that has a job. The job is go to Hacker News and upvote the first post, okay? It's a computer It's a browser use agent. We're going to use a really bad model intentionally. We're using GPT-3.5 Turbo, which is like 2023, right? But we're going to harness it so that it can actually do the job. And we're going to 

save money. So let's I've spoken too much. Let's just get into the demo. Uh And and so let's Welcome to my project. This is my project. Hello everybody. This is the entry point. Can you see that? Is it too Yeah? You want it bigger? Let's do bigger. Okay. So this is not Actually, this room is too bright. Let's do light mode. It's I It's not my nature, but sometimes. That's better, yeah? Okay. So we have we have a model and we're trying an old LG Sorry. 

We We shouldn't have seen that. No, we'll we'll try an old model. And this is the prompt. This is the This is the task. This is literally my prompt. Upvote a story I just described it. For the purpose of this demo, we will not change the prompt at all. Because a lot of us think, hey, my agent is not doing what it's supposed to do, so I just need to prompt it harder, right? That's not always true. I need to change the system prompt. We're not going to touch any prompts here. We're just going to build a harness and the outcome will change. We we log some things to the console and 

then we start a browser session. Okay, what's a browser session? It's literally just Playwright. Not Playwright MCP, like Playwright Playwright. Where this is just a class I made with an open method that launches Chromium and gets a context and makes a page. And then navigate We're just literally calling the Playwright functions, yeah? This is This is just traditional engineering. So we create a session, we open the session, meaning a browser window in a context. And then we create our tools and we give that browser session to the tools. And we create a context and we give the task, meaning the prompt here, 

to the context. Now, create tools is literally what it sounds like. It's here. There's just some types and create tools is a function that takes a browser session and gives you like tools. And these tools are not I didn't invent this. This is from OpenAI's SDK, okay? So you have the name, the description parameters, and execute, the way you actually call the tool in your runtime. And and there's just tools for I made this. It's very easy. Um So that's my tools. And then create context, you may think, whoa, context engineering. Absolutely not. It's This is my context. There's nothing here. 

It's just a system prompt. Literally, the most basic system prompt and the user's task. This is basic basic. And then we have run loop, which is just running the agent in a loop. So what it's doing here, we can actually just look at this, too. While true, so it is an agent loop. And we get a response from the agent and we see if the response says stop, meaning if the LLM says, I'm done, then we return the value. If we get any other response, we don't do anything except 

add these events into a trace. So we just push history into a big list of history. Does that make sense? And so that's all we're doing here. This is just a loop where we just collect events until we're done, okay? So this is super basic. Now let's see how it works. So I'm going to come over here and I'm going to do Are you okay, sir? Do you need water? I'm going to npm run agent. Um And so it's going to open Chromium. It's going to Okay, Hacker News, so far so good. Click upvote. Oh, no. So we we hit a login screen and then it kind of panicked and crashed. But look, it it lies. You see 

this? Um this is a problem. And so what's the solution? Prompt it harder? No. Change the system prompt. Always login with these credentials included in the system prompt. No. So how do we then solve this? And look, we because of my logging, we can actually see it just clicks the upvote button and then considers it a success. It doesn't verify. This is the job of a harness, okay? So now incrementally, we're going to slowly start building a harness. Um And so, let's just move I'm not going to 

write code here. I'm not going to live code because we don't write code anymore. We inspect diffs. Right? Anyone write code by hand? You don't Maybe actually you do belong here. Anyway, so um I'm kidding. So, this is um This is the first change we're going to make. This was our index file. And we have this run loop that I showed you, but now we're going to add one thing to it, which is default guardrails. We're going to create some guardrails, okay? Um what do our guardrails look like? Well, let's go and look at it in the editor um with guardrails over here. And 

so, we have some types, but these are our guardrails. We have two. Max iterations, meaning if you do more than six steps, I'mma kill you. And max messages, meaning if you have more than this many messages, I will compress the context. These are just guardrails, okay? A little utility to combine them, and we just we can compose them here. We could do like as many as we want. So, now let's go back to our changes. That's the guardrails. We if we go back to the agent loop we actually use the guardrails here in this diff. And so, we include the guardrail functions, and we can see that here what we're doing is 

we're checking how many messages have we accumulated, and we just like trim the context if it's too much. Um but what I did want to show you is here at the end um we we push context size, which is some more metadata about what we've done with our guardrails, okay? Um our context compressor is extremely basic and extremely naive. This is what it does. Um let me actually open this with syntax highlighting to spare Um this is what it does. So, what we're doing is if we always keep the system prompt and the user prompt and the most 

recent two messages. So, if the guardrail is triggered, we always remove everything after the system prompt and the user prompt in the middle, and we keep the last two messages. This is super naive. Don't do There's better ways, but this is where babies first. We're We're getting there. So, we we're starting to have a harness, but it's not called a harness, but this is really like a pregnant harness. Like it's almost born, okay? And so, what we're going to do is let's just call it a harness now. So, I'm going to show you another diff where we Here, check this out. Index, we've 

deleted almost everything. Um and we've moved it into this file called harness. Let's go look at our entry point now. It index, it's it's all gone. So, the prompt is there. But this is it's like 19 lines of code, and we just have run harness. We've taken all the logic from here and hidden it in a function called run harness. And as you would expect, run harness does exactly the same thing as we did in the index, okay? Nothing new is here except maybe like a print function, which is just console log. Is this clear so far? Yeah, we just moved stuff. Now that we have something called a harness, we can actually use it. 

And let's solve the problem of lying first before we solve the problem of logging in as me. Yeah, because it says I I upvoted, it did not. I want to know. So, what we're going to do is we're going to add some guardrails and and have it tell the truth. Like if you failed, tell me the truth. Um how might we do that? Well, we'll check it out here. So, many many things changed. Um Or not. I don't know. Hang on a second. Yeah, okay. 

Did Many many things changed. So, we run harness and we added a third argument here, which is a verify step and max attempts. Max attempts goes to our guardrail. So, if if you took more than three tries to do this, just give up. And if we go to the harness, we added a lot of things um that are just manual code. This is not different prompt. This is my logic. Um the main logic is run harness no longer wraps over the code we moved, but we moved that to a different function called run harness attempt. So, if we if we 

come to run harness Let's go here. I need to check the branch out, sorry. Yeah. So, now if we go to run harness attempt, we'll collapse this. I'll collapse this. I'll collapse all of these. And if we go to run harness attempt, now this is the same thing from our index. We just moved it into a function called run harness attempt because our main run harness is just a loop that runs no more than three times, okay? Is this clear? So, we're just enforcing the max steps, but at the harness level for safety. Um then we have run harness attempt that calls it. We have this function called 

verify successful upvote. I wrote this. This is deterministic. That's what I want to show you. What does this do? Well, we see if You remember we were tracing in the agent loop, we're just adding history events. So, we reflect on that, and we see if there was a browser click on the upvote and if it's successful, but really successful, then we say true. But there's a huge butt here, which is we have now cases for failed login. If there's a tool named harness auto login, and if the message starts with failed 

then we return early and we say no no, this failed. We're We're removing the lie, okay? Similarly, unrecovered login redirect. We look over our agent loops tools that we've been pushing into. Um and if we see that the harness auto login didn't run and now we're on the page that is the login URL, then again, we just fail. Okay? Um and so, we're what we're doing is we're just adding like if this happened, if this happened, you just just fail. Return early. Is this clear? This is what a harness does. And so, let's run this now with the harness. 

Uh npm run agent. And now it's going to go on Hacker News, and we're going to repeat the same cycle. Okay, it's going to come here, and now it's still failed, but look, it stopped lying because our harness checks the tool history and actually sees what happened. This is what a harness is supposed to do. Great. This is already like half the battle won because step one to solving a problem is admitting you have one, okay? Test-driven development vibes. So, now that we we're failing correctly, we can 

succeed. And I'd like to show you that in the last diff, and then we'll finish the talk here. So, number four. Um we have a whole new function. It's called login handler. Uh I'll add some syntax highlighting here so you don't go blind. Uh but here, create login handler. This is This is all it does. It runs every agent loop just before we push to the traces, and it This is what it do It checks the browser session's current URL. And if we're not on a login page, it just says cool, I don't I return I have nothing for you. This computationally is not costly at all, right? If you're not on the login page, but if you are on the 

login page then it we fill in a temporary This can be an environment variable. It can be secure, you get the idea. But we fill in credentials and submit the button programmatically from the harness, not from the agent, deterministically and securely because this file has access to any secrets I want it to, right? And so, this How How is this called? Well, this is called in the agent loop. So, if we go back to our agent loop and notice we were pushing traces, yeah? This is where we push the traces. Just before, if we have a login handler 

we call the login handler just before this in the agent loop. What does the login handler do? Well, if we're not on the login page, it does nothing. If we are on a login page, then it quickly will inject credentials and submit the form and then take you back. It will also add, as we can see here, it pushes a message into the queue saying, "Hey, I'm the harness. I logged in. You're good now." Is this clear? Yeah? So, the the harness is is is literally harnessing the agent to something stable, something deterministic. That's what it's for, okay? Let's run this now and see what happens. 

So, npm run agent. It's going to open Hacker News, and when it gets to the login, now that harness step, it logged in and it upvoted the first one, and it closed. Amazing. So, successfully upvoted a little snitch for nilux, uh rank two, uh succeeded after six iterations, and I can click this and go into Hacker News and actually see indeed it was upvoted, um and it I can unvote now, which means it was upvoted, right? So, um the agent used the computer, logged in as me with my harness that I just made here on stage. That's the purpose. Is this clear 

so far? Do you understand the role of a harness? Look at you nodding. This is music to my ears. Fantastic. Something to my eyes. I don't know the It's beauty to my eyes, kind of weird. We don't have a expression for that. Let's land the plane. I'm done. I think my work here is done. What does this look like in practice? Why Why do I care so much about harnesses? Because they run the world. Models are non-deterministic. And you want to do more with less. You want to use a cheap model. Use like Quinn or something, or even something smaller. Use GPT-OSS. It's free. And with a great harness, you 

can go very far. That's why. At IBM, we create a open-source project that we deploy in the enterprise that allows very large companies, huge companies, in their private like data-sensitive areas to perform rag operations on all kinds of things, teams, calls, and PDFs, and invoices. Um We We build It's called open rag, and it's it's rag I don't know if rag is cool or not anymore, but open rag has a hell of a harness that provides enterprise-level security to like asking questions with internal very 

very siloed data. And And that's kind of where the harness engineering comes in. So, let's summarize. We covered a lot of content. Was it a deep I think it was a deep dive. It was a deep dive in like 18 minutes or so. Um we went pretty far. I It's not It should not be lost on you that I did not touch the prompt once. I did not change the system prompt. We just built a harness and the outcome radically changed. And of course, we can add secrets, we can add tokens. Um yeah, we did a lot. In the end, I hope you understand what a harness is, the value it can present, 

and how you can use it. What's next? Um Look, I I don't have a crystal ball like everyone else here, um but it's not lost on me that 2025 was the year of agents. Yes? Uh 2026 is the year of harnesses, I'm pretty sure. Everybody How many times is this word used here? Um I think I would hope I think it'd be pretty cool if 2027 was the year of dynamic on-the-fly generated harnesses. How cool would that Like you tell an agent, "Hey, do this for me. Buy me a flight ticket." 

Whatever it may be. And then before doing the work, the agent creates a harness. This similar to plan mode. Any of you using plan mode? But But on steroids. The The agent creates an actual harness, self-aware. It knows, "Oh, I can maybe hallucinate here. I can maybe" Creates a harness, does the job, and returns back to you, guardrailed and everything. That is so cool. Dynamic on-the-fly harnesses. I would I I this is honestly the next logical step towards AGI, and I would love to see it. I don't know if this is just me being uh you know weird guy with ideas, but um I think that's kind of the direction. So, with that um I'm almost out of time. I would 

be really remiss if I didn't spend the last like 30 seconds saying thank you so much. The slides are on GitHub uh as uh am I uh and so I'd love to chat more. Thank you. >> [music] 

<p>
 <span data-rw-start="7.205" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="14.72" data-rw-transcript-version="2">
 &gt;&gt; Hello everybody.
 </span>
 <span data-rw-start="16.88" data-rw-transcript-version="2">
 Everybody's head turned up. Hello, hi.
 </span>
 <span data-rw-start="19.36" data-rw-transcript-version="2">
 How was lunch? Was it good?
 </span>
 <span data-rw-start="21.88" data-rw-transcript-version="2">
 You didn't like it, no?
 </span>
 <span data-rw-start="23.12" data-rw-transcript-version="2">
 It's like
 </span>
 <span data-rw-start="24.12" data-rw-transcript-version="2">
 British food. Anyway, hi. I'm Tejas. I
 </span>
 <span data-rw-start="27.16" data-rw-transcript-version="2">
 I'll be your first speaker this
 </span>
 <span data-rw-start="28.36" data-rw-transcript-version="2">
 afternoon. Tejas, that's pronounced like
 </span>
 <span data-rw-start="30.04" data-rw-transcript-version="2">
 Tejas.
 </span>
</p>
<p>
 <span data-rw-start="31.12" data-rw-transcript-version="2">
 Don't worry, I'm not
 </span>
 <span data-rw-start="32.599" data-rw-transcript-version="2">
 hopefully my joy in AI is, and I've
 </span>
 <span data-rw-start="34.76" data-rw-transcript-version="2">
 had the privilege of working at a number
 </span>
 <span data-rw-start="36.6" data-rw-transcript-version="2">
 of different places over my career in
 </span>
 <span data-rw-start="37.92" data-rw-transcript-version="2">
 one form or the other. It's just been an
 </span>
 <span data-rw-start="39.36" data-rw-transcript-version="2">
 absolute joy to learn from the best.
 </span>
</p>
<p>
 <span data-rw-start="41.68" data-rw-transcript-version="2">
 Today, I'm an AI developer advocate at
 </span>
 <span data-rw-start="43.84" data-rw-transcript-version="2">
 IBM,
 </span>
 <span data-rw-start="45.32" data-rw-transcript-version="2">
 where we do things with AI, believe
 </span>
 <span data-rw-start="47.56" data-rw-transcript-version="2">
 it or not. We train frontier models, we
 </span>
 <span data-rw-start="48.84" data-rw-transcript-version="2">
 build harnesses. It's really, it's a fun
 </span>
 <span data-rw-start="51.28" data-rw-transcript-version="2">
 lab to work in.
 </span>
</p>
<p>
 <span data-rw-start="52.92" data-rw-transcript-version="2">
 But that's not what I'm here to talk to
 </span>
 <span data-rw-start="53.96" data-rw-transcript-version="2">
 you about today. Today, I'm here to talk
 </span>
 <span data-rw-start="55.36" data-rw-transcript-version="2">
 to you about AI harnesses. AI harnesses.
 </span>
</p>
<p>
 <span data-rw-start="58.24" data-rw-transcript-version="2">
 Before I move forward, I would love to
 </span>
 <span data-rw-start="60.6" data-rw-transcript-version="2">
 just have a show of hands.
 </span>
 <span data-rw-start="62.72" data-rw-transcript-version="2">
 How many of you are like confident in
 </span>
 <span data-rw-start="64.44" data-rw-transcript-version="2">
 your understanding of AI harnesses? Like
 </span>
 <span data-rw-start="65.84" data-rw-transcript-version="2">
 you're like I could present this on
 </span>
 <span data-rw-start="67.2" data-rw-transcript-version="2">
 stage today.
 </span>
 <span data-rw-start="68.72" data-rw-transcript-version="2">
 Look around. Look around. No, seriously,
 </span>
 <span data-rw-start="70.08" data-rw-transcript-version="2">
 look around. That's why we're doing this
 </span>
 <span data-rw-start="71.84" data-rw-transcript-version="2">
 talk. Okay, this is my hope. I want you
 </span>
 <span data-rw-start="73.64" data-rw-transcript-version="2">
 to; if I ask you this at the end of the
 </span>
 <span data-rw-start="75.56" data-rw-transcript-version="2">
 talk, right? I want you to be like, oh,
 </span>
 <span data-rw-start="76.72" data-rw-transcript-version="2">
 I—I—I get it now. That's the whole
 </span>
 <span data-rw-start="78.28" data-rw-transcript-version="2">
 point. I have literally nothing to gain
 </span>
 <span data-rw-start="80" data-rw-transcript-version="2">
 from this other than I—I shared
 </span>
 <span data-rw-start="81.6" data-rw-transcript-version="2">
 knowledge, okay? Because also, this term
 </span>
 <span data-rw-start="84" data-rw-transcript-version="2">
 is kind of everywhere. You may have
 </span>
 <span data-rw-start="85.28" data-rw-transcript-version="2">
 heard it used like 52,000 times today.
 </span>
</p>
<p>
 <span data-rw-start="88.84" data-rw-transcript-version="2">
 And it means different things to
 </span>
 <span data-rw-start="90.6" data-rw-transcript-version="2">
 different people, because, like, in the machine
 </span>
 <span data-rw-start="91.88" data-rw-transcript-version="2">
 learning world, it means like a
 </span>
 <span data-rw-start="93.12" data-rw-transcript-version="2">
 glorified test suite for machine
 </span>
 <span data-rw-start="94.44" data-rw-transcript-version="2">
 learning models. But in the AI
 </span>
 <span data-rw-start="96.64" data-rw-transcript-version="2">
 world, it means something different. And
 </span>
 <span data-rw-start="97.52" data-rw-transcript-version="2">
 so today, we're going to understand this
 </span>
 <span data-rw-start="99.12" data-rw-transcript-version="2">
 in detail. It's a deep dive, but it's 18
 </span>
 <span data-rw-start="101.52" data-rw-transcript-version="2">
 Minutes long. So let's move
 </span>
 <span data-rw-start="102.72" data-rw-transcript-version="2">
 forward. Um,
 </span>
 <span data-rw-start="104.44" data-rw-transcript-version="2">
 I want to start by talking about why
 </span>
 <span data-rw-start="105.56" data-rw-transcript-version="2">
 harness. Like why do we use harnesses?
 </span>
</p>
<p>
 <span data-rw-start="107.76" data-rw-transcript-version="2">
 And the reason for this is because we
 </span>
 <span data-rw-start="109.24" data-rw-transcript-version="2">
 pay rent to companies that give us
 </span>
 <span data-rw-start="113" data-rw-transcript-version="2">
 compute, give us inference, give us
 </span>
 <span data-rw-start="114.76" data-rw-transcript-version="2">
 tokens in return. Some of you maybe work
 </span>
 <span data-rw-start="117.16" data-rw-transcript-version="2">
 for companies that have frontier models
 </span>
 <span data-rw-start="118.76" data-rw-transcript-version="2">
 like Anthropic or Google or whatever, and
 </span>
 <span data-rw-start="121.12" data-rw-transcript-version="2">
 you maybe—what was the term? Token
 </span>
 <span data-rw-start="122.68" data-rw-transcript-version="2">
 billionaires, yeah?
 </span>
 <span data-rw-start="124.36" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="125.2" data-rw-transcript-version="2">
 I'm not that. I am maybe with Watson
 </span>
 <span data-rw-start="127.88" data-rw-transcript-version="2">
 models, but the vast majority of us
 </span>
 <span data-rw-start="129.96" data-rw-transcript-version="2">
 aren't token billionaires. We pay
 </span>
 <span data-rw-start="131.76" data-rw-transcript-version="2">
 rent. We literally pay $20 a month for
 </span>
 <span data-rw-start="133.4" data-rw-transcript-version="2">
 Claude Pro. And then you get a context
 </span>
 <span data-rw-start="135.68" data-rw-transcript-version="2">
 window that's limited, and you get like,
 </span>
 <span data-rw-start="137.52" data-rw-transcript-version="2">
 you know, you don't get the full
 </span>
 <span data-rw-start="138.96" data-rw-transcript-version="2">
 hog, so to speak. And the model you rent
 </span>
 <span data-rw-start="142.04" data-rw-transcript-version="2">
 is a black box. Like they could at
 </span>
 <span data-rw-start="144.28" data-rw-transcript-version="2">
 any time, I'm not saying they do, but
 </span>
 <span data-rw-start="145.76" data-rw-transcript-version="2">
 they could if Opus is somehow not
 </span>
 <span data-rw-start="147.8" data-rw-transcript-version="2">
 available, they could serve you Sonnet.
 </span>
</p>
<p>
 <span data-rw-start="149.4" data-rw-transcript-version="2">
 Even though it says Opus, you would
 </span>
 <span data-rw-start="150.84" data-rw-transcript-version="2">
 never know, right?
 </span>
 <span data-rw-start="152.24" data-rw-transcript-version="2">
 And so it's just a big. There are too many
 </span>
 <span data-rw-start="154.2" data-rw-transcript-version="2">
 variables that we cannot control. So why
 </span>
 <span data-rw-start="156.76" data-rw-transcript-version="2">
 harness? Because the name of the game
 </span>
 <span data-rw-start="159.16" data-rw-transcript-version="2">
 with harness is reliability. Um,
 </span>
 <span data-rw-start="162.6" data-rw-transcript-version="2">
 I really hope I'm not supposed to stand
 </span>
 <span data-rw-start="164.16" data-rw-transcript-version="2">
 in front of this white line and then I'm
 </span>
 <span data-rw-start="166.12" data-rw-transcript-version="2">
 just not in the camera. Anyway,
 </span>
 <span data-rw-start="167.56" data-rw-transcript-version="2">
 whatever.
 </span>
</p>
<p>
 <span data-rw-start="169.08" data-rw-transcript-version="2">
 It's reliability. It's, it's making sure
 </span>
 <span data-rw-start="171.12" data-rw-transcript-version="2">
 that the agents we build do what they
 </span>
 <span data-rw-start="173.36" data-rw-transcript-version="2">
 do, period. Irrespective of the black
 </span>
 <span data-rw-start="175.52" data-rw-transcript-version="2">
 box model, irrespective of the, of the
 </span>
 <span data-rw-start="177.72" data-rw-transcript-version="2">
 thing we rent and so on, okay? Now
 </span>
 <span data-rw-start="179.88" data-rw-transcript-version="2">
 that we understand why harness, let's
 </span>
 <span data-rw-start="181.2" data-rw-transcript-version="2">
 talk about what a harness even is from
 </span>
 <span data-rw-start="183.64" data-rw-transcript-version="2">
 first principles. Like, let's, let's take
 </span>
 <span data-rw-start="185.36" data-rw-transcript-version="2">
 it all the way back to harnesses that we
 </span>
 <span data-rw-start="186.8" data-rw-transcript-version="2">
 know and understand. If you've ever, you
 </span>
 <span data-rw-start="189.92" data-rw-transcript-version="2">
 know, climbed a mountain or something, or
 </span>
 <span data-rw-start="191.6" data-rw-transcript-version="2">
 you've seen someone. This is a harness.
 </span>
</p>
<p>
 <span data-rw-start="193.4" data-rw-transcript-version="2">
 It's like mountain climbers literally
 </span>
 <span data-rw-start="195.04" data-rw-transcript-version="2">
 will harness themselves to what? To
 </span>
 <span data-rw-start="197.92" data-rw-transcript-version="2">
 a mountain, because it's stable. And they
 </span>
 <span data-rw-start="200.2" data-rw-transcript-version="2">
 Can't go off the rails, literally.
 </span>
</p>
<p>
 <span data-rw-start="202.88" data-rw-transcript-version="2">
 They, they
 </span>
 <span data-rw-start="203.52" data-rw-transcript-version="2">
 anchor themselves in something stable so
 </span>
 <span data-rw-start="206.52" data-rw-transcript-version="2">
 that they can't drift too far.
 </span>
 <span data-rw-start="208.92" data-rw-transcript-version="2">
 Okay, that's what a harness is by
 </span>
 <span data-rw-start="210.68" data-rw-transcript-version="2">
 design. When you have any dog owners
 </span>
 <span data-rw-start="212.56" data-rw-transcript-version="2">
 here? You have dogs? You, you walk your
 </span>
 <span data-rw-start="214.36" data-rw-transcript-version="2">
 dog on a harness, okay? That's why?
 </span>
 <span data-rw-start="216.6" data-rw-transcript-version="2">
 Because your dog doesn't go and bankrupt
 </span>
 <span data-rw-start="218.44" data-rw-transcript-version="2">
 you with tokens. Okay?
 </span>
</p>
<p>
 <span data-rw-start="221.08" data-rw-transcript-version="2">
 That's what a harness is.
 </span>
 <span data-rw-start="223.64" data-rw-transcript-version="2">
 But the problem is, if we think about
 </span>
 <span data-rw-start="225.6" data-rw-transcript-version="2">
 what harness, there're really two types.
 </span>
 <span data-rw-start="227.8" data-rw-transcript-version="2">
 There’s one from the machine learning
 </span>
 <span data-rw-start="229.28" data-rw-transcript-version="2">
 world, which, as I mentioned, is kind of
 </span>
 <span data-rw-start="230.52" data-rw-transcript-version="2">
 like a test suite and a test runner.
 </span>
 <span data-rw-start="232.84" data-rw-transcript-version="2">
 You would give a model some inputs, and
 </span>
 <span data-rw-start="234.24" data-rw-transcript-version="2">
 you see the quality of the outputs.
 </span>
 <span data-rw-start="235.36" data-rw-transcript-version="2">
 That's not. This is not ML engineer
 </span>
 <span data-rw-start="237.44" data-rw-transcript-version="2">
 Europe. We're going to talk today about
 </span>
 <span data-rw-start="239.6" data-rw-transcript-version="2">
 the agent harness that is common in AI
 </span>
 <span data-rw-start="241.8" data-rw-transcript-version="2">
 engineering. Okay, so what is an
 </span>
 <span data-rw-start="243.6" data-rw-transcript-version="2">
 agent harness?
 </span>
</p>
<p>
 <span data-rw-start="245.56" data-rw-transcript-version="2">
 An agent harness, and this is kind of
 </span>
 <span data-rw-start="247.76" data-rw-transcript-version="2">
 the money shot here. The agent harness
 </span>
 <span data-rw-start="250.16" data-rw-transcript-version="2">
 I'm not making money off this. It's
 </span>
 <span data-rw-start="251.52" data-rw-transcript-version="2">
 just an expression. The agent harness is
 </span>
 <span data-rw-start="254.96" data-rw-transcript-version="2">
 everything around the model that gives
 </span>
 <span data-rw-start="257.6" data-rw-transcript-version="2">
 it grounding in reality. It's literally
 </span>
 <span data-rw-start="259.84" data-rw-transcript-version="2">
 the thing that ties it to a stable
 </span>
 <span data-rw-start="261.519" data-rw-transcript-version="2">
 environment, okay? An agent. So Claude
 </span>
 <span data-rw-start="263.88" data-rw-transcript-version="2">
 code, for example, can be considered an
 </span>
 <span data-rw-start="265.64" data-rw-transcript-version="2">
 agent harness. And some of you would
 </span>
 <span data-rw-start="266.64" data-rw-transcript-version="2">
 say, oh, no, it's a coding agent.
 </span>
</p>
<p>
 <span data-rw-start="267.76" data-rw-transcript-version="2">
 Absolutely, it's a coding agent. But
 </span>
 <span data-rw-start="269.32" data-rw-transcript-version="2">
 it's a harnessed coding agent. An agent
 </span>
 <span data-rw-start="272.28" data-rw-transcript-version="2">
 harness has more or less the same
 </span>
 <span data-rw-start="274.84" data-rw-transcript-version="2">
 typical suspects, moving parts. Number
 </span>
 <span data-rw-start="276.76" data-rw-transcript-version="2">
 one, it's got
 </span>
 <span data-rw-start="278.64" data-rw-transcript-version="2">
 a tool registry. Almost like so Claude
 </span>
 <span data-rw-start="281.2" data-rw-transcript-version="2">
 code, cursor, Codex, they have tools to
 </span>
 <span data-rw-start="283.6" data-rw-transcript-version="2">
 read from the file system, to write, to
 </span>
 <span data-rw-start="285.32" data-rw-transcript-version="2">
 execute bash commands, right? They have
 </span>
 <span data-rw-start="286.68" data-rw-transcript-version="2">
 a tool registry. They have a model and
 </span>
 <span data-rw-start="289.08" data-rw-transcript-version="2">
 some of them allow you to choose a
 </span>
 <span data-rw-start="290.28" data-rw-transcript-version="2">
 model, some of them allow you to not.
 </span>
 <span data-rw-start="291.88" data-rw-transcript-version="2">
 They have a model. They have primitives
 </span>
 <span data-rw-start="293.96" data-rw-transcript-version="2">
 for managing context. Almost every
 </span>
 <span data-rw-start="297.4" data-rw-transcript-version="2">
 harnessed agent runtime today will
 </span>
 <span data-rw-start="300.12" data-rw-transcript-version="2">
 compact its own context, right? That's
 </span>
 <span data-rw-start="302.2" data-rw-transcript-version="2">
 That's that’s the job of the harness.
 </span>
</p>
<p>
 <span data-rw-start="304.88" data-rw-transcript-version="2">
 Guardrails are another part of a
 </span>
 <span data-rw-start="306.16" data-rw-transcript-version="2">
 harness. For example, max steps. Anyone
 </span>
 <span data-rw-start="308.64" data-rw-transcript-version="2">
 using max steps? Do not do more than
 </span>
 <span data-rw-start="310.8" data-rw-transcript-version="2">
 five tool calls. That’s a guardrail. And
 </span>
 <span data-rw-start="312.8" data-rw-transcript-version="2">
 so if you do that, you just kill the
 </span>
 <span data-rw-start="314.56" data-rw-transcript-version="2">
 kill the run, right?
 </span>
 <span data-rw-start="316.2" data-rw-transcript-version="2">
 An agent loop is another part of an
 </span>
 <span data-rw-start="318.12" data-rw-transcript-version="2">
 agent harness, which is crazy. This is
 </span>
 <span data-rw-start="319.88" data-rw-transcript-version="2">
 what some people I've spoken to
 </span>
 <span data-rw-start="321.04" data-rw-transcript-version="2">
 prepare for this talk
 </span>
 <span data-rw-start="322.52" data-rw-transcript-version="2">
 will say,
 </span>
 <span data-rw-start="323.76" data-rw-transcript-version="2">
 wait, isn't a harness just the agent
 </span>
 <span data-rw-start="325.48" data-rw-transcript-version="2">
 loop? No, it's the stuff around the
 </span>
 <span data-rw-start="327.92" data-rw-transcript-version="2">
 agent loop. In fact, it could be a loop
 </span>
 <span data-rw-start="330.08" data-rw-transcript-version="2">
 around your agent loop. It could be an
 </span>
 <span data-rw-start="331.44" data-rw-transcript-version="2">
 NM loop. And we'll look at that a little
 </span>
 <span data-rw-start="333.12" data-rw-transcript-version="2">
 bit in some code. And then finally,
 </span>
 <span data-rw-start="334.92" data-rw-transcript-version="2">
 there's a verify step. This is, for
 </span>
 <span data-rw-start="337.28" data-rw-transcript-version="2">
 example, in a coding coding agent, after
 </span>
 <span data-rw-start="339.56" data-rw-transcript-version="2">
 the work is done, a verify step would
 </span>
 <span data-rw-start="341.68" data-rw-transcript-version="2">
 be, hey, let's run lint, let's run
 </span>
 <span data-rw-start="344.36" data-rw-transcript-version="2">
 tests, let's make sure nothing broke,
 </span>
 <span data-rw-start="345.76" data-rw-transcript-version="2">
 right? So almost every code
 </span>
 <span data-rw-start="348.32" data-rw-transcript-version="2">
 coding agents as an example, but you
 </span>
</p>
<p>
 <span data-rw-start="349.68" data-rw-transcript-version="2">
 Could have a harness for anything. And
 </span>
 <span data-rw-start="351.36" data-rw-transcript-version="2">
 it's, it's amazing because it really grounds
 </span>
 <span data-rw-start="353.6" data-rw-transcript-version="2">
 black box models in a stable environment
 </span>
 <span data-rw-start="356" data-rw-transcript-version="2">
 that you control. Okay? I'd like to show
 </span>
 <span data-rw-start="359" data-rw-transcript-version="2">
 you
 </span>
 <span data-rw-start="360.08" data-rw-transcript-version="2">
 a demo. And what we're going to do
 </span>
 <span data-rw-start="361.16" data-rw-transcript-version="2">
 together is we're going to build a
 </span>
 <span data-rw-start="362.36" data-rw-transcript-version="2">
 harness, a bare-bones baby's first
 </span>
 <span data-rw-start="364.24" data-rw-transcript-version="2">
 harness. Let's call it a poor man's AI
 </span>
 <span data-rw-start="366.88" data-rw-transcript-version="2">
 harness together so we understand from
 </span>
 <span data-rw-start="368.48" data-rw-transcript-version="2">
 first principles how this works. We're
 </span>
 <span data-rw-start="370.12" data-rw-transcript-version="2">
 going to build a computer use agent that
 </span>
 <span data-rw-start="372.32" data-rw-transcript-version="2">
 has a job. The job is to go to Hacker News
 </span>
 <span data-rw-start="374.88" data-rw-transcript-version="2">
 and upvote the first post, okay? It's a
 </span>
 <span data-rw-start="376.88" data-rw-transcript-version="2">
 computer. It's a browser use agent. We're
 </span>
 <span data-rw-start="379.04" data-rw-transcript-version="2">
 going to use a really bad model
 </span>
 <span data-rw-start="381.04" data-rw-transcript-version="2">
 intentionally. We're using GPT-3.5
 </span>
 <span data-rw-start="383.64" data-rw-transcript-version="2">
 Turbo, which is like 2023, right? But
 </span>
 <span data-rw-start="387.24" data-rw-transcript-version="2">
 we're going to harness it so that it can
 </span>
 <span data-rw-start="388.68" data-rw-transcript-version="2">
 actually do the job. And we're going to
 </span>
 <span data-rw-start="390.4" data-rw-transcript-version="2">
 save money. So let's I' ve spoken too
 </span>
 <span data-rw-start="392.24" data-rw-transcript-version="2">
 much. Let's just get into the demo.
 </span>
</p>
<p>
 <span data-rw-start="396.04" data-rw-transcript-version="2">
 Uh
 </span>
 <span data-rw-start="397.12" data-rw-transcript-version="2">
 And so let's. Welcome to my project.
 </span>
 <span data-rw-start="399.2" data-rw-transcript-version="2">
 This is my project. Hello everybody.
 </span>
</p>
<p>
 <span data-rw-start="400.76" data-rw-transcript-version="2">
 This is the entry point. Can you see
 </span>
 <span data-rw-start="402.44" data-rw-transcript-version="2">
 that? Is it too
 </span>
 <span data-rw-start="404.32" data-rw-transcript-version="2">
 Yeah? You want it bigger?
 </span>
 <span data-rw-start="406.16" data-rw-transcript-version="2">
 Let's do bigger. Okay. So this is not
 </span>
 <span data-rw-start="408.52" data-rw-transcript-version="2">
 actually, this room is too bright. Let's
 </span>
 <span data-rw-start="410.44" data-rw-transcript-version="2">
 do light mode. It's not my
 </span>
 <span data-rw-start="412.96" data-rw-transcript-version="2">
 nature, but sometimes. That's better,
 </span>
 <span data-rw-start="415.36" data-rw-transcript-version="2">
 yeah? Okay. So we have a model
 </span>
 <span data-rw-start="418.04" data-rw-transcript-version="2">
 and we're
 </span>
 <span data-rw-start="418.92" data-rw-transcript-version="2">
 trying an old LG. Sorry,
 </span>
 <span data-rw-start="421.2" data-rw-transcript-version="2">
 we
 </span>
 <span data-rw-start="423.16" data-rw-transcript-version="2">
 shouldn't have seen that. No, we'll
 </span>
 <span data-rw-start="425.4" data-rw-transcript-version="2">
 try an old model. And this is the
 </span>
 <span data-rw-start="426.8" data-rw-transcript-version="2">
 prompt. This is the task.
 </span>
</p>
<p>
 <span data-rw-start="429.32" data-rw-transcript-version="2">
 This is literally my prompt. Upvote a
 </span>
 <span data-rw-start="430.72" data-rw-transcript-version="2">
 story I just described it. For the
 </span>
 <span data-rw-start="432.92" data-rw-transcript-version="2">
 purpose of this demo, we will not change
 </span>
 <span data-rw-start="435.44" data-rw-transcript-version="2">
 the prompt at all.
 </span>
</p>
<p>
 <span data-rw-start="437.28" data-rw-transcript-version="2">
 Because a lot of us think, hey, my agent
 </span>
 <span data-rw-start="438.8" data-rw-transcript-version="2">
 is not doing what it's supposed to do,
 </span>
 <span data-rw-start="440.08" data-rw-transcript-version="2">
 so I just need to prompt it harder,
 </span>
 <span data-rw-start="442.08" data-rw-transcript-version="2">
 right? That's not always true. I need to
 </span>
 <span data-rw-start="444.48" data-rw-transcript-version="2">
 change the system prompt. We're not
 </span>
 <span data-rw-start="445.4" data-rw-transcript-version="2">
 going to touch any prompts here. We're
 </span>
 <span data-rw-start="446.68" data-rw-transcript-version="2">
 just going to build a harness and the
 </span>
 <span data-rw-start="448.12" data-rw-transcript-version="2">
 Outcome will change.
 </span>
</p>
<p>
 <span data-rw-start="449.52" data-rw-transcript-version="2">
 We log some things to the console and
 </span>
 <span data-rw-start="451.76" data-rw-transcript-version="2">
 then we start a browser session. Okay?
 </span>
 <span data-rw-start="453.24" data-rw-transcript-version="2">
 What's a browser session? It's literally
 </span>
 <span data-rw-start="454.52" data-rw-transcript-version="2">
 just Playwright. Not Playwright MCP,
 </span>
 <span data-rw-start="456.44" data-rw-transcript-version="2">
 like Playwright Playwright. Where this
 </span>
 <span data-rw-start="457.92" data-rw-transcript-version="2">
 is just a class I made with an open
 </span>
 <span data-rw-start="459.96" data-rw-transcript-version="2">
 method that launches Chromium and gets a
 </span>
 <span data-rw-start="462.36" data-rw-transcript-version="2">
 context and makes a page. And then
 </span>
 <span data-rw-start="463.44" data-rw-transcript-version="2">
 navigate. We're just literally calling
 </span>
 <span data-rw-start="464.92" data-rw-transcript-version="2">
 the Playwright functions, yeah? This is
 </span>
 <span data-rw-start="466.68" data-rw-transcript-version="2">
 this is just traditional engineering. So
 </span>
 <span data-rw-start="469.84" data-rw-transcript-version="2">
 we create a session, we open the
 </span>
 <span data-rw-start="471.44" data-rw-transcript-version="2">
 session, meaning a browser window in a
 </span>
 <span data-rw-start="472.8" data-rw-transcript-version="2">
 context. And then we create our tools
 </span>
 <span data-rw-start="474.96" data-rw-transcript-version="2">
 and we give that browser session to the
 </span>
 <span data-rw-start="476.52" data-rw-transcript-version="2">
 tools. And we create a context and we
 </span>
 <span data-rw-start="478.6" data-rw-transcript-version="2">
 give the task, meaning the prompt here,
 </span>
 <span data-rw-start="481.32" data-rw-transcript-version="2">
 to the context. Now, create tools is
 </span>
 <span data-rw-start="483.32" data-rw-transcript-version="2">
 literally what it sounds like. It’s
 </span>
 <span data-rw-start="485" data-rw-transcript-version="2">
 here. There’s just some types and create
 </span>
 <span data-rw-start="487.2" data-rw-transcript-version="2">
 tools is a function that takes a browser
 </span>
 <span data-rw-start="488.84" data-rw-transcript-version="2">
 session and gives you like tools. And
 </span>
 <span data-rw-start="491.6" data-rw-transcript-version="2">
 these tools are not—I didn’t invent
 </span>
 <span data-rw-start="492.92" data-rw-transcript-version="2">
 this. This is from OpenAI’s SDK, okay?
 </span>
</p>
<p>
 <span data-rw-start="495.64" data-rw-transcript-version="2">
 So you have the name, the description
 </span>
 <span data-rw-start="497.56" data-rw-transcript-version="2">
 parameters, and execute, the way you
 </span>
 <span data-rw-start="498.84" data-rw-transcript-version="2">
 actually call the tool in your runtime.
 </span>
 <span data-rw-start="500.56" data-rw-transcript-version="2">
 And there's just tools for, I made
 </span>
 <span data-rw-start="502" data-rw-transcript-version="2">
 this. It's very easy. Um,
 </span>
 <span data-rw-start="504.08" data-rw-transcript-version="2">
 so that's my tools, and then create
 </span>
 <span data-rw-start="505.92" data-rw-transcript-version="2">
 context. You may think, whoa, it's
 </span>
 <span data-rw-start="507.92" data-rw-transcript-version="2">
 context engineering. Absolutely not.
 </span>
 <span data-rw-start="509.68" data-rw-transcript-version="2">
 It's just my context. There's nothing here.
 </span>
 <span data-rw-start="511.28" data-rw-transcript-version="2">
 It's just a system prompt.
 </span>
</p>
<p>
 <span data-rw-start="513.24" data-rw-transcript-version="2">
 Literally, the most basic system prompt
 </span>
 <span data-rw-start="515.4" data-rw-transcript-version="2">
 and the user's task. This is basic,
 </span>
 <span data-rw-start="517.84" data-rw-transcript-version="2">
 basic. And then we have the run loop, which
 </span>
 <span data-rw-start="520.36" data-rw-transcript-version="2">
 is just running the agent in a loop. So
 </span>
 <span data-rw-start="521.919" data-rw-transcript-version="2">
 what it's doing here, we can actually
 </span>
 <span data-rw-start="523.599" data-rw-transcript-version="2">
 just look at this, too.
 </span>
 <span data-rw-start="524.88" data-rw-transcript-version="2">
 While true, so it is an agent loop. And
 </span>
 <span data-rw-start="527.04" data-rw-transcript-version="2">
 we get a response from the agent, and we
 </span>
 <span data-rw-start="529.24" data-rw-transcript-version="2">
 see if the response says stop, meaning
 </span>
 <span data-rw-start="531.8" data-rw-transcript-version="2">
 if the LLM says, I'm done, then we
 </span>
 <span data-rw-start="534.12" data-rw-transcript-version="2">
 return the value.
 </span>
</p>
<p>
 <span data-rw-start="535.92" data-rw-transcript-version="2">
 If we get any other response, we don't
 </span>
 <span data-rw-start="538.08" data-rw-transcript-version="2">
 do anything except
 </span>
 <span data-rw-start="540.08" data-rw-transcript-version="2">
 add these events into a trace. So we
 </span>
 <span data-rw-start="542.08" data-rw-transcript-version="2">
 just push history into a big list of
 </span>
 <span data-rw-start="543.84" data-rw-transcript-version="2">
 History. Does that make sense? And so
 </span>
 <span data-rw-start="545.28" data-rw-transcript-version="2">
 that's all we're doing here. This is
 </span>
 <span data-rw-start="546.52" data-rw-transcript-version="2">
 just a loop where we just collect events
 </span>
 <span data-rw-start="548.44" data-rw-transcript-version="2">
 until we're done, okay? So this is super
 </span>
 <span data-rw-start="551.32" data-rw-transcript-version="2">
 basic. Now let's see how it works. So
 </span>
 <span data-rw-start="552.92" data-rw-transcript-version="2">
 I'm going to come over here and I'm
 </span>
 <span data-rw-start="554.44" data-rw-transcript-version="2">
 going to do, Are you okay, sir? Do you
 </span>
 <span data-rw-start="556" data-rw-transcript-version="2">
 need water? I'm going to
 </span>
 <span data-rw-start="557.96" data-rw-transcript-version="2">
 npm run agent. Um, and so it's going to
 </span>
 <span data-rw-start="561.24" data-rw-transcript-version="2">
 open Chromium. It's going to, okay,
 </span>
 <span data-rw-start="563" data-rw-transcript-version="2">
 Hacker News, so far so good. Click
 </span>
 <span data-rw-start="564.36" data-rw-transcript-version="2">
 upvote. Oh, no. So we hit a login
 </span>
 <span data-rw-start="567.36" data-rw-transcript-version="2">
 screen and then it kind of panicked and
 </span>
 <span data-rw-start="568.76" data-rw-transcript-version="2">
 crashed. But look, it lies. You see
 </span>
 <span data-rw-start="572" data-rw-transcript-version="2">
 this?
 </span>
</p>
<p>
 <span data-rw-start="573.08" data-rw-transcript-version="2">
 Um, this is a problem. And so what's the
 </span>
 <span data-rw-start="575.52" data-rw-transcript-version="2">
 solution? Prompt it harder? No. Change
 </span>
 <span data-rw-start="578" data-rw-transcript-version="2">
 the system prompt. Always login with
 </span>
 <span data-rw-start="579.6" data-rw-transcript-version="2">
 these credentials included in the system
 </span>
 <span data-rw-start="581.12" data-rw-transcript-version="2">
 prompt. No.
 </span>
 <span data-rw-start="583.24" data-rw-transcript-version="2">
 So, how do we then solve this? And look,
 </span>
 <span data-rw-start="585.36" data-rw-transcript-version="2">
 we, because of my logging, we can
 </span>
 <span data-rw-start="586.76" data-rw-transcript-version="2">
 actually see it just clicks the upvote
 </span>
 <span data-rw-start="589.28" data-rw-transcript-version="2">
 button and then considers it a success.
 </span>
 <span data-rw-start="591.32" data-rw-transcript-version="2">
 It doesn't verify. This is the job of a
 </span>
 <span data-rw-start="593.36" data-rw-transcript-version="2">
 Harness, okay? So now incrementally,
 </span>
 <span data-rw-start="595.52" data-rw-transcript-version="2">
 we're going to slowly start building a
 </span>
 <span data-rw-start="597.16" data-rw-transcript-version="2">
 harness. Um,
 </span>
 <span data-rw-start="598.8" data-rw-transcript-version="2">
 and so, let's just move. I'm not going to
 </span>
 <span data-rw-start="601.04" data-rw-transcript-version="2">
 write code here. I'm not going to live
 </span>
 <span data-rw-start="602.16" data-rw-transcript-version="2">
 code because we don't write code
 </span>
 <span data-rw-start="603.44" data-rw-transcript-version="2">
 anymore. We inspect diffs.
 </span>
</p>
<p>
 <span data-rw-start="605.72" data-rw-transcript-version="2">
 Right? Anyone write code by hand? You
 </span>
 <span data-rw-start="607.2" data-rw-transcript-version="2">
 don't. Maybe actually you do belong here.
 </span>
 <span data-rw-start="608.64" data-rw-transcript-version="2">
 Anyway, so, um,
 </span>
 <span data-rw-start="611.12" data-rw-transcript-version="2">
 I'm kidding. So, this is, um,
 </span>
 <span data-rw-start="613.2" data-rw-transcript-version="2">
 this is the first change we're going to
 </span>
 <span data-rw-start="614.52" data-rw-transcript-version="2">
 make. This was our index file.
 </span>
 <span data-rw-start="616.64" data-rw-transcript-version="2">
 And we have this run loop that I showed
 </span>
 <span data-rw-start="618.56" data-rw-transcript-version="2">
 you, but now we're going to add one
 </span>
 <span data-rw-start="620.32" data-rw-transcript-version="2">
 thing to it, which is default
 </span>
 <span data-rw-start="621.56" data-rw-transcript-version="2">
 guardrails. We're going to create some
 </span>
 <span data-rw-start="622.76" data-rw-transcript-version="2">
 guardrails, okay?
 </span>
 <span data-rw-start="624.16" data-rw-transcript-version="2">
 Um, what do our guardrails look like?
 </span>
 <span data-rw-start="626.4" data-rw-transcript-version="2">
 Well, let's go and look at it in the
 </span>
 <span data-rw-start="627.64" data-rw-transcript-version="2">
 editor, um, with guardrails over here. And
 </span>
 <span data-rw-start="631" data-rw-transcript-version="2">
 so, we have some types, but these are
 </span>
 <span data-rw-start="632.24" data-rw-transcript-version="2">
 our guardrails. We have two. Max
 </span>
 <span data-rw-start="633.48" data-rw-transcript-version="2">
 iterations, meaning if you do more than
 </span>
 <span data-rw-start="635.04" data-rw-transcript-version="2">
 six steps, I'm gonna kill you.
 </span>
</p>
<p>
 <span data-rw-start="636.72" data-rw-transcript-version="2">
 And max messages, meaning if you have
 </span>
 <span data-rw-start="638.6" data-rw-transcript-version="2">
 more than this many messages, I will
 </span>
 <span data-rw-start="639.92" data-rw-transcript-version="2">
 compress the context. These are just
 </span>
 <span data-rw-start="641.48" data-rw-transcript-version="2">
 guardrails, okay? A little utility to
 </span>
 <span data-rw-start="643.44" data-rw-transcript-version="2">
 combine them, and we just, we can compose
 </span>
 <span data-rw-start="645.52" data-rw-transcript-version="2">
 them here. We could do as many as
 </span>
 <span data-rw-start="646.72" data-rw-transcript-version="2">
 we want. So, now
 </span>
 <span data-rw-start="649.04" data-rw-transcript-version="2">
 let's go back to our changes. That’s the
 </span>
 <span data-rw-start="651.88" data-rw-transcript-version="2">
 guardrails. We, if we go back to the
 </span>
 <span data-rw-start="653.84" data-rw-transcript-version="2">
 agent loop, we actually use the
 </span>
 <span data-rw-start="655.72" data-rw-transcript-version="2">
 guardrails here in this diff. And so, we
 </span>
 <span data-rw-start="657.88" data-rw-transcript-version="2">
 include the guardrail functions, and we
 </span>
 <span data-rw-start="659.92" data-rw-transcript-version="2">
 can see that here what we're doing is
 </span>
 <span data-rw-start="661.96" data-rw-transcript-version="2">
 we're checking how many messages have we
 </span>
 <span data-rw-start="663.56" data-rw-transcript-version="2">
 accumulated, and we just like trim the
 </span>
 <span data-rw-start="665.16" data-rw-transcript-version="2">
 context if it's too much. Um but what I
 </span>
 <span data-rw-start="668.12" data-rw-transcript-version="2">
 did want to show you is here at the end
 </span>
 <span data-rw-start="670.48" data-rw-transcript-version="2">
 um we, we push context size, which is
 </span>
 <span data-rw-start="673.12" data-rw-transcript-version="2">
 some more metadata about what we've done
 </span>
 <span data-rw-start="674.68" data-rw-transcript-version="2">
 with our guardrails, okay?
 </span>
</p>
<p>
 <span data-rw-start="676.2" data-rw-transcript-version="2">
 Um, our context compressor is extremely
 </span>
 <span data-rw-start="679.28" data-rw-transcript-version="2">
 basic and extremely naive. This is what
 </span>
 <span data-rw-start="681.32" data-rw-transcript-version="2">
 it does. Um, let me actually open this
 </span>
 <span data-rw-start="683.52" data-rw-transcript-version="2">
 with syntax highlighting to spare. Um
 </span>
 <span data-rw-start="686.16" data-rw-transcript-version="2">
 this is what it does. So, what we're
 </span>
 <span data-rw-start="687.64" data-rw-transcript-version="2">
 Doing is, if we always keep the system
 </span>
 <span data-rw-start="689.52" data-rw-transcript-version="2">
 prompt and the user prompt and the most
 </span>
 <span data-rw-start="691.76" data-rw-transcript-version="2">
 recent two messages,
 </span>
 <span data-rw-start="694.08" data-rw-transcript-version="2">
 so, if the
 </span>
 <span data-rw-start="696.36" data-rw-transcript-version="2">
 guardrail is triggered, we always remove
 </span>
 <span data-rw-start="697.92" data-rw-transcript-version="2">
 everything after the system prompt and
 </span>
 <span data-rw-start="699.32" data-rw-transcript-version="2">
 the user prompt in the middle, and we
 </span>
 <span data-rw-start="700.68" data-rw-transcript-version="2">
 keep the last two messages. This is
 </span>
 <span data-rw-start="702.36" data-rw-transcript-version="2">
 super naive. Don't do — there's better
 </span>
 <span data-rw-start="704.2" data-rw-transcript-version="2">
 ways, but this is where babies first.
 </span>
</p>
<p>
 <span data-rw-start="705.52" data-rw-transcript-version="2">
 We're, we're getting there.
 </span>
 <span data-rw-start="707.88" data-rw-transcript-version="2">
 So, we're starting to have a harness,
 </span>
 <span data-rw-start="709.28" data-rw-transcript-version="2">
 but it's not called a harness, but this
 </span>
 <span data-rw-start="710.72" data-rw-transcript-version="2">
 is really like
 </span>
 <span data-rw-start="712.36" data-rw-transcript-version="2">
 a pregnant harness. Like it's almost
 </span>
 <span data-rw-start="714.44" data-rw-transcript-version="2">
 born, okay? And so, what we're going to
 </span>
 <span data-rw-start="716.36" data-rw-transcript-version="2">
 do is let's just call it a harness now.
 </span>
 <span data-rw-start="718.36" data-rw-transcript-version="2">
 So, I'm going to show you another diff
 </span>
 <span data-rw-start="719.88" data-rw-transcript-version="2">
 where we
 </span>
 <span data-rw-start="721.16" data-rw-transcript-version="2">
 deleted almost everything.
 </span>
 <span data-rw-start="722.92" data-rw-transcript-version="2">
 Um, and we've moved it into this file
 </span>
 <span data-rw-start="724.839" data-rw-transcript-version="2">
 called harness. Let's go look at our
 </span>
 <span data-rw-start="726.56" data-rw-transcript-version="2">
 entry point now.
 </span>
 <span data-rw-start="727.96" data-rw-transcript-version="2">
 It, index, it's — it's all gone. So, the
 </span>
 <span data-rw-start="729.839" data-rw-transcript-version="2">
 prompt is there. But this is, it's like
 </span>
 <span data-rw-start="732.2" data-rw-transcript-version="2">
 19 lines of code, and we just have run
 </span>
 <span data-rw-start="734.04" data-rw-transcript-version="2">
 harness. We've taken all the logic from
 </span>
 <span data-rw-start="735.6" data-rw-transcript-version="2">
 here and hidden it in a function called
 </span>
 <span data-rw-start="737.56" data-rw-transcript-version="2">
 run harness. And as you would expect,
 </span>
 <span data-rw-start="738.76" data-rw-transcript-version="2">
 run harness does exactly the same thing
 </span>
 <span data-rw-start="740.76" data-rw-transcript-version="2">
 as we did in the index, okay? Nothing
 </span>
 <span data-rw-start="742.56" data-rw-transcript-version="2">
 new is here except maybe like a print
 </span>
 <span data-rw-start="743.88" data-rw-transcript-version="2">
 function, which is just console log. Is
 </span>
 <span data-rw-start="745.16" data-rw-transcript-version="2">
 this clear so far? Yeah, we just moved
 </span>
 <span data-rw-start="746.92" data-rw-transcript-version="2">
 stuff. Now that we have something called
 </span>
 <span data-rw-start="748.8" data-rw-transcript-version="2">
 a harness, we can actually use it.
 </span>
</p>
<p>
 <span data-rw-start="751.44" data-rw-transcript-version="2">
 And let's solve the problem of lying
 </span>
 <span data-rw-start="753.839" data-rw-transcript-version="2">
 first before we solve the problem of
 </span>
 <span data-rw-start="755.52" data-rw-transcript-version="2">
 logging in as me. Yeah, because it says
 </span>
 <span data-rw-start="757.48" data-rw-transcript-version="2">
 I upvoted, it did not. I want to know.
 </span>
 <span data-rw-start="760.36" data-rw-transcript-version="2">
 So, what we're going to do is we're
 </span>
 <span data-rw-start="761.2" data-rw-transcript-version="2">
 going to add some guardrails and have it tell the truth. Like if you
 </span>
 <span data-rw-start="764.44" data-rw-transcript-version="2">
 failed, tell me the truth. Um
 </span>
 <span data-rw-start="767.36" data-rw-transcript-version="2">
 how might we do that? Well, we'll check
 </span>
 <span data-rw-start="769.6" data-rw-transcript-version="2">
 it out here. So,
 </span>
 <span data-rw-start="771.52" data-rw-transcript-version="2">
 many, many things changed. Um
 </span>
 <span data-rw-start="774.44" data-rw-transcript-version="2">
 Or not. I don't know. Hang on a second.
 </span>
 <span data-rw-start="779.68" data-rw-transcript-version="2">
 Yeah, okay.
 </span>
 <span data-rw-start="780.72" data-rw-transcript-version="2">
 Did many, many things change? So, we run.
 </span>
</p>
<p>
 <span data-rw-start="782.36" data-rw-transcript-version="2">
 Harness and we added a third argument
 </span>
 <span data-rw-start="784.52" data-rw-transcript-version="2">
 here, which is a verify step and max
 </span>
 <span data-rw-start="786.32" data-rw-transcript-version="2">
 attempts. Max attempts goes to our
 </span>
 <span data-rw-start="787.4" data-rw-transcript-version="2">
 guardrail. So, if you took more than
 </span>
 <span data-rw-start="788.96" data-rw-transcript-version="2">
 three tries to do this, just give up.
 </span>
</p>
<p>
 <span data-rw-start="791.08" data-rw-transcript-version="2">
 And if we go to the harness, we added a
 </span>
 <span data-rw-start="793.08" data-rw-transcript-version="2">
 lot of things, um, that are just manual
 </span>
 <span data-rw-start="796.16" data-rw-transcript-version="2">
 code. This is not a different prompt. This
 </span>
 <span data-rw-start="797.76" data-rw-transcript-version="2">
 is my logic. Um, the main logic is run
 </span>
 <span data-rw-start="801.04" data-rw-transcript-version="2">
 harness, no longer wraps over the code we
 </span>
 <span data-rw-start="803" data-rw-transcript-version="2">
 moved, but we moved that to a different
 </span>
 <span data-rw-start="804.96" data-rw-transcript-version="2">
 function called
 </span>
 <span data-rw-start="806.88" data-rw-transcript-version="2">
 run harness attempt. So, if we, if we
 </span>
 <span data-rw-start="810.44" data-rw-transcript-version="2">
 come to run harness, let's go here. I
 </span>
 <span data-rw-start="813.56" data-rw-transcript-version="2">
 need to check the branch out, sorry.
 </span>
</p>
<p>
 <span data-rw-start="815.12" data-rw-transcript-version="2">
 Yeah. So, now if we go to run harness
 </span>
 <span data-rw-start="817.4" data-rw-transcript-version="2">
 attempt, we'll collapse this. I'll
 </span>
 <span data-rw-start="818.839" data-rw-transcript-version="2">
 collapse this.
 </span>
 <span data-rw-start="820.4" data-rw-transcript-version="2">
 I'll collapse all of these. And if we go
 </span>
 <span data-rw-start="822.48" data-rw-transcript-version="2">
 to run harness attempt, now this is the
 </span>
 <span data-rw-start="823.839" data-rw-transcript-version="2">
 same thing from our index. We just moved
 </span>
 <span data-rw-start="825.48" data-rw-transcript-version="2">
 it into a function called run harness
 </span>
 <span data-rw-start="826.68" data-rw-transcript-version="2">
 attempt because our main run harness is
 </span>
 <span data-rw-start="829.24" data-rw-transcript-version="2">
 just a loop that runs no more than three
 </span>
 <span data-rw-start="831.48" data-rw-transcript-version="2">
 times, okay? Is this clear? So, we're
 </span>
 <span data-rw-start="832.76" data-rw-transcript-version="2">
 Just enforcing the max steps, but at the
 </span>
 <span data-rw-start="834.6" data-rw-transcript-version="2">
 harness level for safety. Um
 </span>
 <span data-rw-start="837.56" data-rw-transcript-version="2">
 Then we have run harness attempt that
 </span>
 <span data-rw-start="839.6" data-rw-transcript-version="2">
 calls it. We have this function called
 </span>
 <span data-rw-start="841.6" data-rw-transcript-version="2">
 verify successful upvote. I wrote this.
 </span>
</p>
<p>
 <span data-rw-start="844.28" data-rw-transcript-version="2">
 This is deterministic. That's what I
 </span>
 <span data-rw-start="845.76" data-rw-transcript-version="2">
 want to show you. What does this do?
 </span>
 <span data-rw-start="847.839" data-rw-transcript-version="2">
 Well, we see if you remember we were
 </span>
 <span data-rw-start="850.6" data-rw-transcript-version="2">
 tracing in the agent loop, we're just
 </span>
 <span data-rw-start="852.24" data-rw-transcript-version="2">
 adding history events. So, we reflect on
 </span>
 <span data-rw-start="854.56" data-rw-transcript-version="2">
 that, and we see if there was a browser
 </span>
 <span data-rw-start="856.36" data-rw-transcript-version="2">
 click
 </span>
 <span data-rw-start="857.48" data-rw-transcript-version="2">
 on the upvote and if it's successful,
 </span>
 <span data-rw-start="860.32" data-rw-transcript-version="2">
 but really successful, then we say true.
 </span>
 <span data-rw-start="862.28" data-rw-transcript-version="2">
 But there's a huge but here, which is
 </span>
 <span data-rw-start="864.92" data-rw-transcript-version="2">
 we have now cases for failed login. If
 </span>
 <span data-rw-start="867.2" data-rw-transcript-version="2">
 there's a tool named harness auto login,
 </span>
 <span data-rw-start="869.52" data-rw-transcript-version="2">
 and if the message starts with failed,
 </span>
 <span data-rw-start="871.68" data-rw-transcript-version="2">
 then we return early and we say no, no,
 </span>
 <span data-rw-start="872.959" data-rw-transcript-version="2">
 this failed. We're removing the
 </span>
 <span data-rw-start="874.72" data-rw-transcript-version="2">
 lie, okay? Similarly, unrecovered login
 </span>
 <span data-rw-start="877.64" data-rw-transcript-version="2">
 redirect. We look over our agent loops
 </span>
 <span data-rw-start="879.56" data-rw-transcript-version="2">
 tools that we've been pushing into.
 </span>
 <span data-rw-start="881.72" data-rw-transcript-version="2">
 Um, and if we see that the harness auto
 </span>
 <span data-rw-start="885.04" data-rw-transcript-version="2">
 login didn't run.
 </span>
</p>
<p>
 <span data-rw-start="886.64" data-rw-transcript-version="2">
 And now we're on the page that is the
 </span>
 <span data-rw-start="888.68" data-rw-transcript-version="2">
 login URL, then again, we just fail.
 </span>
 <span data-rw-start="891.16" data-rw-transcript-version="2">
 Okay?
 </span>
 <span data-rw-start="891.959" data-rw-transcript-version="2">
 Um, and so, we're what we're doing is
 </span>
 <span data-rw-start="893.6" data-rw-transcript-version="2">
 we're just adding like if this happened,
 </span>
 <span data-rw-start="894.76" data-rw-transcript-version="2">
 if this happened, you just just fail.
 </span>
 <span data-rw-start="896.079" data-rw-transcript-version="2">
 Return early. Is this clear? This is
 </span>
 <span data-rw-start="897.6" data-rw-transcript-version="2">
 what a harness does. And so, let's run
 </span>
 <span data-rw-start="899.2" data-rw-transcript-version="2">
 this now with the harness.
 </span>
</p>
<p>
 <span data-rw-start="901.32" data-rw-transcript-version="2">
 Uh, npm run agent.
 </span>
 <span data-rw-start="903.16" data-rw-transcript-version="2">
 And
 </span>
 <span data-rw-start="904.12" data-rw-transcript-version="2">
 now it's going to go on Hacker News, and
 </span>
 <span data-rw-start="905.48" data-rw-transcript-version="2">
 we're going to repeat the same cycle.
 </span>
</p>
<p>
 <span data-rw-start="908" data-rw-transcript-version="2">
 Okay, it's going to come here, and now
 </span>
 <span data-rw-start="909.64" data-rw-transcript-version="2">
 it's still failed, but look, it stopped
 </span>
 <span data-rw-start="911.52" data-rw-transcript-version="2">
 lying because our harness checks the
 </span>
 <span data-rw-start="914.12" data-rw-transcript-version="2">
 tool history and actually sees what
 </span>
 <span data-rw-start="915.72" data-rw-transcript-version="2">
 happened. This is what a harness is
 </span>
 <span data-rw-start="917.44" data-rw-transcript-version="2">
 supposed to do. Great. This is already
 </span>
 <span data-rw-start="919.839" data-rw-transcript-version="2">
 like half the battle won because step
 </span>
 <span data-rw-start="922.16" data-rw-transcript-version="2">
 one to solving a problem is admitting
 </span>
 <span data-rw-start="923.52" data-rw-transcript-version="2">
 you have one, okay?
 </span>
</p>
<p>
 <span data-rw-start="925.72" data-rw-transcript-version="2">
 Test-driven development vibes. So, now
 </span>
 <span data-rw-start="927.6" data-rw-transcript-version="2">
 that we're failing correctly, we can
 </span>
 <span data-rw-start="930.32" data-rw-transcript-version="2">
 succeed. And I'd like to show you that
 </span>
 <span data-rw-start="932.28" data-rw-transcript-version="2">
 In the last diff, and then we'll finish
 </span>
 <span data-rw-start="933.76" data-rw-transcript-version="2">
 the talk here. So, number four.
 </span>
</p>
<p>
 <span data-rw-start="936.52" data-rw-transcript-version="2">
 Um, we have a whole new function. It's
 </span>
 <span data-rw-start="937.88" data-rw-transcript-version="2">
 called login handler. Uh, I'll add some
 </span>
 <span data-rw-start="940.16" data-rw-transcript-version="2">
 syntax highlighting here so you don't go
 </span>
 <span data-rw-start="942.44" data-rw-transcript-version="2">
 blind. Uh, but here, create login
 </span>
 <span data-rw-start="944.28" data-rw-transcript-version="2">
 handler. This is all it does. It
 </span>
 <span data-rw-start="945.76" data-rw-transcript-version="2">
 runs every agent loop just before we
 </span>
 <span data-rw-start="947.92" data-rw-transcript-version="2">
 push to the traces, and it — this is what
 </span>
 <span data-rw-start="949.48" data-rw-transcript-version="2">
 it do. It checks the browser session's
 </span>
 <span data-rw-start="950.88" data-rw-transcript-version="2">
 current URL.
 </span>
</p>
<p>
 <span data-rw-start="952.2" data-rw-transcript-version="2">
 And if we're not on a login page, it
 </span>
 <span data-rw-start="953.64" data-rw-transcript-version="2">
 just says cool, I don't I return I have
 </span>
 <span data-rw-start="955.64" data-rw-transcript-version="2">
 nothing for you. This computationally is
 </span>
 <span data-rw-start="957.24" data-rw-transcript-version="2">
 not costly at all, right? If you're not
 </span>
 <span data-rw-start="958.76" data-rw-transcript-version="2">
 on the login page, but if you are on the
 </span>
 <span data-rw-start="960.44" data-rw-transcript-version="2">
 login page,
 </span>
 <span data-rw-start="961.839" data-rw-transcript-version="2">
 then it we fill in
 </span>
 <span data-rw-start="963.72" data-rw-transcript-version="2">
 a temporary. This can be an environment
 </span>
 <span data-rw-start="965.72" data-rw-transcript-version="2">
 variable. It can be secure, you get the
 </span>
 <span data-rw-start="967.079" data-rw-transcript-version="2">
 idea. But we fill in credentials and
 </span>
 <span data-rw-start="968.52" data-rw-transcript-version="2">
 submit the button programmatically from
 </span>
 <span data-rw-start="970.88" data-rw-transcript-version="2">
 the harness, not from the agent,
 </span>
 <span data-rw-start="973" data-rw-transcript-version="2">
 deterministically and securely because
 </span>
 <span data-rw-start="975.28" data-rw-transcript-version="2">
 this file has access to any secrets.
 </span>
</p>
<p>
 <span data-rw-start="977.44" data-rw-transcript-version="2">
 Want it to, right? And so, this how how
 </span>
 <span data-rw-start="979.959" data-rw-transcript-version="2">
 is this called? Well, this is called in
 </span>
 <span data-rw-start="981.64" data-rw-transcript-version="2">
 the agent loop. So, if we go back to our
 </span>
 <span data-rw-start="983.36" data-rw-transcript-version="2">
 agent loop and notice we were pushing
 </span>
 <span data-rw-start="985.8" data-rw-transcript-version="2">
 traces, yeah? This is where we push the
 </span>
 <span data-rw-start="987.36" data-rw-transcript-version="2">
 traces.
 </span>
 <span data-rw-start="988.48" data-rw-transcript-version="2">
 Just before, if we have a login handler
 </span>
 <span data-rw-start="991.839" data-rw-transcript-version="2">
 we call the login handler just before
 </span>
 <span data-rw-start="993.52" data-rw-transcript-version="2">
 this in the agent loop. What does the
 </span>
 <span data-rw-start="995.24" data-rw-transcript-version="2">
 login handler do? Well, if we're not on
 </span>
 <span data-rw-start="996.76" data-rw-transcript-version="2">
 the login page, it does nothing.
 </span>
</p>
<p>
 <span data-rw-start="998.8" data-rw-transcript-version="2">
 If we are on a login page, then it
 </span>
 <span data-rw-start="1000.44" data-rw-transcript-version="2">
 quickly will inject credentials and
 </span>
 <span data-rw-start="1001.72" data-rw-transcript-version="2">
 submit the form and then take you back.
 </span>
 <span data-rw-start="1003.16" data-rw-transcript-version="2">
 It will also add, as we can see here, it
 </span>
 <span data-rw-start="1004.88" data-rw-transcript-version="2">
 pushes a message into the queue saying,
 </span>
 <span data-rw-start="1007.32" data-rw-transcript-version="2">
 "Hey, I'm the harness. I logged in.
 </span>
 <span data-rw-start="1009.48" data-rw-transcript-version="2">
 You're good now." Is this clear? Yeah?
 </span>
</p>
<p>
 <span data-rw-start="1011.68" data-rw-transcript-version="2">
 So, the harness is literally
 </span>
 <span data-rw-start="1013.48" data-rw-transcript-version="2">
 harnessing the agent to something
 </span>
 <span data-rw-start="1015.16" data-rw-transcript-version="2">
 stable, something deterministic. That's
 </span>
 <span data-rw-start="1017" data-rw-transcript-version="2">
 what it's for, okay?
 </span>
 <span data-rw-start="1018.72" data-rw-transcript-version="2">
 Let's run this now and see what happens.
 </span>
</p>
<p>
 <span data-rw-start="1021.64" data-rw-transcript-version="2">
 So, npm run agent.
 </span>
 <span data-rw-start="1023.36" data-rw-transcript-version="2">
 It's going to open Hacker News, and when
 </span>
 <span data-rw-start="1025.4" data-rw-transcript-version="2">
 It gets to the login. Now that harness
 </span>
 <span data-rw-start="1026.8" data-rw-transcript-version="2">
 step, it logged in and it upvoted the
 </span>
 <span data-rw-start="1028.839" data-rw-transcript-version="2">
 first one, and it closed.
 </span>
</p>
<p>
 <span data-rw-start="1031.76" data-rw-transcript-version="2">
 Amazing. So, successfully upvoted a
 </span>
 <span data-rw-start="1034.28" data-rw-transcript-version="2">
 little snitch for nilux, uh rank two, uh
 </span>
 <span data-rw-start="1036.6" data-rw-transcript-version="2">
 succeeded after six iterations, and I
 </span>
 <span data-rw-start="1038" data-rw-transcript-version="2">
 can click this and go into Hacker News
 </span>
 <span data-rw-start="1039.56" data-rw-transcript-version="2">
 and actually see indeed it was upvoted,
 </span>
 <span data-rw-start="1042.52" data-rw-transcript-version="2">
 um and it I can unvote now, which means
 </span>
 <span data-rw-start="1043.959" data-rw-transcript-version="2">
 it was upvoted, right? So, um the agent
 </span>
 <span data-rw-start="1046.52" data-rw-transcript-version="2">
 used the computer, logged in as me with
 </span>
 <span data-rw-start="1048.439" data-rw-transcript-version="2">
 my harness that I just made here on
 </span>
 <span data-rw-start="1049.84" data-rw-transcript-version="2">
 stage. That's the purpose. Is this clear
 </span>
 <span data-rw-start="1051.84" data-rw-transcript-version="2">
 so far? Do you understand the role of a
 </span>
 <span data-rw-start="1052.96" data-rw-transcript-version="2">
 harness? Look at you nodding. This is
 </span>
 <span data-rw-start="1054.64" data-rw-transcript-version="2">
 music to my ears. Fantastic.
 </span>
 <span data-rw-start="1057.08" data-rw-transcript-version="2">
 Something to my eyes. I don't know the
 </span>
 <span data-rw-start="1059.12" data-rw-transcript-version="2">
 It's beauty to my eyes, kind of weird.
 </span>
 <span data-rw-start="1060.84" data-rw-transcript-version="2">
 We don't have an expression for that.
 </span>
 <span data-rw-start="1062.88" data-rw-transcript-version="2">
 Let's land the plane. I'm done. I think
 </span>
 <span data-rw-start="1065.88" data-rw-transcript-version="2">
 my work here is done. What does this
 </span>
 <span data-rw-start="1067.32" data-rw-transcript-version="2">
 look like in practice? Why? Why do I care
 </span>
 <span data-rw-start="1068.88" data-rw-transcript-version="2">
 so much about harnesses? Because they
 </span>
 <span data-rw-start="1070.56" data-rw-transcript-version="2">
 run the world. Models are
 </span>
 <span data-rw-start="1071.76" data-rw-transcript-version="2">
 non-deterministic. And you want to do
 </span>
 <span data-rw-start="1073.84" data-rw-transcript-version="2">
 More with less. You want to use a cheap
 </span>
 <span data-rw-start="1075.08" data-rw-transcript-version="2">
 model. Use something like Quinn or even something smaller. Use GPT-OSS.
 </span>
</p>
<p>
 <span data-rw-start="1077.08" data-rw-transcript-version="2">
 It's free. And with a great harness, you
 </span>
 <span data-rw-start="1079.28" data-rw-transcript-version="2">
 can go very far. That's why, at IBM, we
 </span>
 <span data-rw-start="1081.28" data-rw-transcript-version="2">
 create an open-source project that we
 </span>
 <span data-rw-start="1083.72" data-rw-transcript-version="2">
 deploy in the enterprise that allows
 </span>
 <span data-rw-start="1086.32" data-rw-transcript-version="2">
 very large companies, huge companies, in
 </span>
 <span data-rw-start="1088.16" data-rw-transcript-version="2">
 their private, data-sensitive areas,
 </span>
 <span data-rw-start="1090.48" data-rw-transcript-version="2">
 to perform RAG operations on all kinds
 </span>
 <span data-rw-start="1093.08" data-rw-transcript-version="2">
 of things, teams, calls, PDFs, and
 </span>
 <span data-rw-start="1094.88" data-rw-transcript-version="2">
 invoices. Um, we build it. It's called
 </span>
 <span data-rw-start="1099.36" data-rw-transcript-version="2">
 Open RAG, and it's, it's RAG. I don't know
 </span>
 <span data-rw-start="1101.56" data-rw-transcript-version="2">
 if RAG is cool or not anymore, but
 </span>
 <span data-rw-start="1104.44" data-rw-transcript-version="2">
 Open RAG has a hell of a harness that
 </span>
 <span data-rw-start="1106.84" data-rw-transcript-version="2">
 provides enterprise-level security to
 </span>
 <span data-rw-start="1108.4" data-rw-transcript-version="2">
 like asking questions with internal, very
 </span>
 <span data-rw-start="1110.4" data-rw-transcript-version="2">
 very siloed data. And, and that's kind of
 </span>
 <span data-rw-start="1112.52" data-rw-transcript-version="2">
 where the harness engineering comes in.
 </span>
 <span data-rw-start="1113.679" data-rw-transcript-version="2">
 So, let's summarize. We covered a lot of
 </span>
 <span data-rw-start="1115.24" data-rw-transcript-version="2">
 content. Was it a deep? I think it was a
 </span>
 <span data-rw-start="1117.28" data-rw-transcript-version="2">
 deep dive. It was a deep dive in like 18
 </span>
 <span data-rw-start="1118.8" data-rw-transcript-version="2">
 minutes or so. Um,
 </span>
 <span data-rw-start="1120.48" data-rw-transcript-version="2">
 we went pretty far. I
 </span>
 <span data-rw-start="1122.96" data-rw-transcript-version="2">
 It's not. It should not be lost on you.
 </span>
</p>
<p>
 <span data-rw-start="1124.56" data-rw-transcript-version="2">
 That I did not touch the prompt once.
 </span>
 <span data-rw-start="1127.159" data-rw-transcript-version="2">
 I did not change the system prompt. We
 </span>
 <span data-rw-start="1128.56" data-rw-transcript-version="2">
 just built a harness
 </span>
 <span data-rw-start="1130.44" data-rw-transcript-version="2">
 and the outcome radically changed. And
 </span>
 <span data-rw-start="1132.4" data-rw-transcript-version="2">
 of course, we can add secrets, we can
 </span>
 <span data-rw-start="1133.919" data-rw-transcript-version="2">
 add tokens. Um yeah, we did a lot. In
 </span>
 <span data-rw-start="1136.56" data-rw-transcript-version="2">
 the end, I hope you understand what a
 </span>
 <span data-rw-start="1138.44" data-rw-transcript-version="2">
 harness is, the value it can present,
 </span>
 <span data-rw-start="1140.12" data-rw-transcript-version="2">
 and how you can use it. What's next? Um
 </span>
 <span data-rw-start="1143.76" data-rw-transcript-version="2">
 Look, I
 </span>
 <span data-rw-start="1144.8" data-rw-transcript-version="2">
 don't have a crystal ball like
 </span>
 <span data-rw-start="1145.96" data-rw-transcript-version="2">
 everyone else here, um but it's not lost
 </span>
 <span data-rw-start="1148.4" data-rw-transcript-version="2">
 on me that 2025 was the year of agents.
 </span>
</p>
<p>
 <span data-rw-start="1151.159" data-rw-transcript-version="2">
 Yes? Uh 2026
 </span>
 <span data-rw-start="1153.72" data-rw-transcript-version="2">
 is the year of harnesses, I'm pretty
 </span>
 <span data-rw-start="1155.2" data-rw-transcript-version="2">
 sure. Everybody. How many times is this
 </span>
 <span data-rw-start="1156.64" data-rw-transcript-version="2">
 word used here? Um I think
 </span>
 <span data-rw-start="1159.36" data-rw-transcript-version="2">
 I would hope. I think it'd be pretty cool
 </span>
 <span data-rw-start="1160.84" data-rw-transcript-version="2">
 if 2027 was the year of dynamic
 </span>
 <span data-rw-start="1164.72" data-rw-transcript-version="2">
 on-the-fly generated harnesses. How cool
 </span>
 <span data-rw-start="1167.08" data-rw-transcript-version="2">
 would that be? Like, you tell an agent, "Hey,
 </span>
 <span data-rw-start="1168.8" data-rw-transcript-version="2">
 do this for me. Buy me a flight ticket."
 </span>
 <span data-rw-start="1170.8" data-rw-transcript-version="2">
 Whatever it may be. And then, before
 </span>
 <span data-rw-start="1172.56" data-rw-transcript-version="2">
 doing the work, the agent creates a
 </span>
 <span data-rw-start="1174" data-rw-transcript-version="2">
 harness. This is similar to plan mode. Any
 </span>
 <span data-rw-start="1175.64" data-rw-transcript-version="2">
 Of you using plan mode? But, but on steroids, the agent creates an
 </span>
 <span data-rw-start="1177.12" data-rw-transcript-version="2">
 actual harness, self-aware. It knows,
 </span>
 <span data-rw-start="1178.919" data-rw-transcript-version="2">
 "Oh, I can maybe hallucinate here. I can maybe," creates a harness, does the job,
 </span>
 <span data-rw-start="1181.08" data-rw-transcript-version="2">
 and returns back to you, guardrailed and everything. That is so cool.
 </span>
</p>
<p>
 <span data-rw-start="1184.6" data-rw-transcript-version="2">
 Dynamic on-the-fly harnesses. I would, I, I think this
 </span>
 <span data-rw-start="1186.64" data-rw-transcript-version="2">
 is honestly the next logical step towards AGI, and I would love to see it.
 </span>
</p>
<p>
 <span data-rw-start="1193.32" data-rw-transcript-version="2">
 I don't know if this is just me being, uh,
 </span>
 <span data-rw-start="1194.64" data-rw-transcript-version="2">
 you know,
 </span>
 <span data-rw-start="1195.8" data-rw-transcript-version="2">
 weird guy with ideas, but, um, I think
 </span>
 <span data-rw-start="1197.96" data-rw-transcript-version="2">
 that's kind of the direction.
 </span>
</p>
<p>
 <span data-rw-start="1199.6" data-rw-transcript-version="2">
 So, with that, um, I'm almost out of time. I would
 </span>
 <span data-rw-start="1201.32" data-rw-transcript-version="2">
 be really remiss if I didn't spend the
 </span>
 <span data-rw-start="1202.44" data-rw-transcript-version="2">
 last, like, 30 seconds saying thank you so
 </span>
 <span data-rw-start="1204.04" data-rw-transcript-version="2">
 much. The slides are on GitHub, uh, as, uh,
 </span>
 <span data-rw-start="1206.48" data-rw-transcript-version="2">
 am I, uh, and so I'd love to chat more.
 </span>
</p>
<p>
 <span data-rw-start="1208.28" data-rw-transcript-version="2">
 Thank you.
 </span>
</p>
<p>
 <span data-rw-start="1216.348" data-rw-transcript-version="2">
 &gt;&gt; [music]
 </span>
</p>