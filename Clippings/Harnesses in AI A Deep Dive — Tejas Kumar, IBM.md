---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - harness
source: readwise
created: 2026-06-23
rating: 
action: 
theme: workflow-phases-gates
subtheme:
  - harness-loops
---

# Harnesses in AI: A Deep Dive — Tejas Kumar, IBM

![rw-book-cover](https://i.ytimg.com/vi/C_GG5g38vLU/sddefault.jpg?v=6a0a974e)

## Metadata
- Author: [[AI Engineer]]
- Full Title: Harnesses in AI: A Deep Dive — Tejas Kumar, IBM
- Category: #articles
- Summary: An AI harness is a system that controls and guides AI models to work safely and reliably. It adds rules and checks to keep the AI grounded in reality and prevent errors like lying. Building a harness helps make AI agents more stable and trustworthy when doing tasks.
- URL: https://m.youtube.com/watch?v=C_GG5g38vLU&pp=ugUEEgJlbg%3D%3D

## Full Document
[music]>> Hello everybody.Everybody's head turned up. Hello, hi.How was lunch? Was it good?You didn't like it, no?It's likeBritish food. Anyway, hi. I'm Tejas. II'll be your first speaker thisafternoon. Tejas, that's pronounced likeTejas.

Don't worry, I'm nothopefully my joy in AI is, and I'vehad the privilege of working at a numberof different places over my career inone form or the other. It's just been anabsolute joy to learn from the best.

Today, I'm an AI developer advocate atIBM,where we do things with AI, believeit or not. We train frontier models, webuild harnesses. It's really, it's a funlab to work in.

But that's not what I'm here to talk toyou about today. Today, I'm here to talkto you about AI harnesses. AI harnesses.

Before I move forward, I would love tojust have a show of hands.How many of you are like confident inyour understanding of AI harnesses? Likeyou're like I could present this onstage today.Look around. Look around. No, seriously,look around. That's why we're doing thistalk. Okay, this is my hope. I want youto; if I ask you this at the end of thetalk, right? I want you to be like, oh,I—I—I get it now. That's the wholepoint. I have literally nothing to gainfrom this other than I—I sharedknowledge, okay? Because also, this termis kind of everywhere. You may haveheard it used like 52,000 times today.

And it means different things todifferent people, because, like, in the machinelearning world, it means like aglorified test suite for machinelearning models. But in the AIworld, it means something different. Andso today, we're going to understand thisin detail. It's a deep dive, but it's 18Minutes long. So let's moveforward. Um,I want to start by talking about whyharness. Like why do we use harnesses?

And the reason for this is because wepay rent to companies that give uscompute, give us inference, give ustokens in return. Some of you maybe workfor companies that have frontier modelslike Anthropic or Google or whatever, andyou maybe—what was the term? Tokenbillionaires, yeah?Um,I'm not that. I am maybe with Watsonmodels, but the vast majority of usaren't token billionaires. We payrent. We literally pay $20 a month forClaude Pro. And then you get a contextwindow that's limited, and you get like,you know, you don't get the fullhog, so to speak. And the model you rentis a black box. Like they could atany time, I'm not saying they do, butthey could if Opus is somehow notavailable, they could serve you Sonnet.

Even though it says Opus, you wouldnever know, right?And so it's just a big. There are too manyvariables that we cannot control. So whyharness? Because the name of the gamewith harness is reliability. Um,I really hope I'm not supposed to standin front of this white line and then I'mjust not in the camera. Anyway,whatever.

It's reliability. It's, it's making surethat the agents we build do what theydo, period. Irrespective of the blackbox model, irrespective of the, of thething we rent and so on, okay? Nowthat we understand why harness, let'stalk about what a harness even is fromfirst principles. Like, let's, let's takeit all the way back to harnesses that weknow and understand. If you've ever, youknow, climbed a mountain or something, oryou've seen someone. This is a harness.

It's like mountain climbers literallywill harness themselves to what? Toa mountain, because it's stable. And theyCan't go off the rails, literally.

They, theyanchor themselves in something stable sothat they can't drift too far.Okay, that's what a harness is bydesign. When you have any dog ownershere? You have dogs? You, you walk yourdog on a harness, okay? That's why?Because your dog doesn't go and bankruptyou with tokens. Okay?

That's what a harness is.But the problem is, if we think aboutwhat harness, there're really two types.There’s one from the machine learningworld, which, as I mentioned, is kind oflike a test suite and a test runner.You would give a model some inputs, andyou see the quality of the outputs.That's not. This is not ML engineerEurope. We're going to talk today aboutthe agent harness that is common in AIengineering. Okay, so what is anagent harness?

An agent harness, and this is kind ofthe money shot here. The agent harnessI'm not making money off this. It'sjust an expression. The agent harness iseverything around the model that givesit grounding in reality. It's literallythe thing that ties it to a stableenvironment, okay? An agent. So Claudecode, for example, can be considered anagent harness. And some of you wouldsay, oh, no, it's a coding agent.

Absolutely, it's a coding agent. Butit's a harnessed coding agent. An agentharness has more or less the sametypical suspects, moving parts. Numberone, it's gota tool registry. Almost like so Claudecode, cursor, Codex, they have tools toread from the file system, to write, toexecute bash commands, right? They havea tool registry. They have a model andsome of them allow you to choose amodel, some of them allow you to not.They have a model. They have primitivesfor managing context. Almost everyharnessed agent runtime today willcompact its own context, right? That'sThat's that’s the job of the harness.

Guardrails are another part of aharness. For example, max steps. Anyoneusing max steps? Do not do more thanfive tool calls. That’s a guardrail. Andso if you do that, you just kill thekill the run, right?An agent loop is another part of anagent harness, which is crazy. This iswhat some people I've spoken toprepare for this talkwill say,wait, isn't a harness just the agentloop? No, it's the stuff around theagent loop. In fact, it could be a looparound your agent loop. It could be anNM loop. And we'll look at that a littlebit in some code. And then finally,there's a verify step. This is, forexample, in a coding coding agent, afterthe work is done, a verify step wouldbe, hey, let's run lint, let's runtests, let's make sure nothing broke,right? So almost every codecoding agents as an example, but you

Could have a harness for anything. Andit's, it's amazing because it really groundsblack box models in a stable environmentthat you control. Okay? I'd like to showyoua demo. And what we're going to dotogether is we're going to build aharness, a bare-bones baby's firstharness. Let's call it a poor man's AIharness together so we understand fromfirst principles how this works. We'regoing to build a computer use agent thathas a job. The job is to go to Hacker Newsand upvote the first post, okay? It's acomputer. It's a browser use agent. We'regoing to use a really bad modelintentionally. We're using GPT-3.5Turbo, which is like 2023, right? Butwe're going to harness it so that it canactually do the job. And we're going tosave money. So let's I' ve spoken toomuch. Let's just get into the demo.

UhAnd so let's. Welcome to my project.This is my project. Hello everybody.

This is the entry point. Can you seethat? Is it tooYeah? You want it bigger?Let's do bigger. Okay. So this is notactually, this room is too bright. Let'sdo light mode. It's not mynature, but sometimes. That's better,yeah? Okay. So we have a modeland we'retrying an old LG. Sorry,weshouldn't have seen that. No, we'lltry an old model. And this is theprompt. This is the task.

This is literally my prompt. Upvote astory I just described it. For thepurpose of this demo, we will not changethe prompt at all.

Because a lot of us think, hey, my agentis not doing what it's supposed to do,so I just need to prompt it harder,right? That's not always true. I need tochange the system prompt. We're notgoing to touch any prompts here. We'rejust going to build a harness and theOutcome will change.

We log some things to the console andthen we start a browser session. Okay?What's a browser session? It's literallyjust Playwright. Not Playwright MCP,like Playwright Playwright. Where thisis just a class I made with an openmethod that launches Chromium and gets acontext and makes a page. And thennavigate. We're just literally callingthe Playwright functions, yeah? This isthis is just traditional engineering. Sowe create a session, we open thesession, meaning a browser window in acontext. And then we create our toolsand we give that browser session to thetools. And we create a context and wegive the task, meaning the prompt here,to the context. Now, create tools isliterally what it sounds like. It’shere. There’s just some types and createtools is a function that takes a browsersession and gives you like tools. Andthese tools are not—I didn’t inventthis. This is from OpenAI’s SDK, okay?

So you have the name, the descriptionparameters, and execute, the way youactually call the tool in your runtime.And there's just tools for, I madethis. It's very easy. Um,so that's my tools, and then createcontext. You may think, whoa, it'scontext engineering. Absolutely not.It's just my context. There's nothing here.It's just a system prompt.

Literally, the most basic system promptand the user's task. This is basic,basic. And then we have the run loop, whichis just running the agent in a loop. Sowhat it's doing here, we can actuallyjust look at this, too.While true, so it is an agent loop. Andwe get a response from the agent, and wesee if the response says stop, meaningif the LLM says, I'm done, then wereturn the value.

If we get any other response, we don'tdo anything exceptadd these events into a trace. So wejust push history into a big list ofHistory. Does that make sense? And sothat's all we're doing here. This isjust a loop where we just collect eventsuntil we're done, okay? So this is superbasic. Now let's see how it works. SoI'm going to come over here and I'mgoing to do, Are you okay, sir? Do youneed water? I'm going tonpm run agent. Um, and so it's going toopen Chromium. It's going to, okay,Hacker News, so far so good. Clickupvote. Oh, no. So we hit a loginscreen and then it kind of panicked andcrashed. But look, it lies. You seethis?

Um, this is a problem. And so what's thesolution? Prompt it harder? No. Changethe system prompt. Always login withthese credentials included in the systemprompt. No.So, how do we then solve this? And look,we, because of my logging, we canactually see it just clicks the upvotebutton and then considers it a success.It doesn't verify. This is the job of aHarness, okay? So now incrementally,we're going to slowly start building aharness. Um,and so, let's just move. I'm not going towrite code here. I'm not going to livecode because we don't write codeanymore. We inspect diffs.

Right? Anyone write code by hand? Youdon't. Maybe actually you do belong here.Anyway, so, um,I'm kidding. So, this is, um,this is the first change we're going tomake. This was our index file.And we have this run loop that I showedyou, but now we're going to add onething to it, which is defaultguardrails. We're going to create someguardrails, okay?Um, what do our guardrails look like?Well, let's go and look at it in theeditor, um, with guardrails over here. Andso, we have some types, but these areour guardrails. We have two. Maxiterations, meaning if you do more thansix steps, I'm gonna kill you.

And max messages, meaning if you havemore than this many messages, I willcompress the context. These are justguardrails, okay? A little utility tocombine them, and we just, we can composethem here. We could do as many aswe want. So, nowlet's go back to our changes. That’s theguardrails. We, if we go back to theagent loop, we actually use theguardrails here in this diff. And so, weinclude the guardrail functions, and wecan see that here what we're doing iswe're checking how many messages have weaccumulated, and we just like trim thecontext if it's too much. Um but what Idid want to show you is here at the endum we, we push context size, which issome more metadata about what we've donewith our guardrails, okay?

Um, our context compressor is extremelybasic and extremely naive. This is whatit does. Um, let me actually open thiswith syntax highlighting to spare. Umthis is what it does. So, what we'reDoing is, if we always keep the systemprompt and the user prompt and the mostrecent two messages,so, if theguardrail is triggered, we always removeeverything after the system prompt andthe user prompt in the middle, and wekeep the last two messages. This issuper naive. Don't do — there's betterways, but this is where babies first.

We're, we're getting there.So, we're starting to have a harness,but it's not called a harness, but thisis really likea pregnant harness. Like it's almostborn, okay? And so, what we're going todo is let's just call it a harness now.So, I'm going to show you another diffwhere wedeleted almost everything.Um, and we've moved it into this filecalled harness. Let's go look at ourentry point now.It, index, it's — it's all gone. So, theprompt is there. But this is, it's like19 lines of code, and we just have runharness. We've taken all the logic fromhere and hidden it in a function calledrun harness. And as you would expect,run harness does exactly the same thingas we did in the index, okay? Nothingnew is here except maybe like a printfunction, which is just console log. Isthis clear so far? Yeah, we just movedstuff. Now that we have something calleda harness, we can actually use it.

And let's solve the problem of lyingfirst before we solve the problem oflogging in as me. Yeah, because it saysI upvoted, it did not. I want to know.So, what we're going to do is we'regoing to add some guardrails and have it tell the truth. Like if youfailed, tell me the truth. Umhow might we do that? Well, we'll checkit out here. So,many, many things changed. UmOr not. I don't know. Hang on a second.Yeah, okay.Did many, many things change? So, we run.

Harness and we added a third argumenthere, which is a verify step and maxattempts. Max attempts goes to ourguardrail. So, if you took more thanthree tries to do this, just give up.

And if we go to the harness, we added alot of things, um, that are just manualcode. This is not a different prompt. Thisis my logic. Um, the main logic is runharness, no longer wraps over the code wemoved, but we moved that to a differentfunction calledrun harness attempt. So, if we, if wecome to run harness, let's go here. Ineed to check the branch out, sorry.

Yeah. So, now if we go to run harnessattempt, we'll collapse this. I'llcollapse this.I'll collapse all of these. And if we goto run harness attempt, now this is thesame thing from our index. We just movedit into a function called run harnessattempt because our main run harness isjust a loop that runs no more than threetimes, okay? Is this clear? So, we'reJust enforcing the max steps, but at theharness level for safety. UmThen we have run harness attempt thatcalls it. We have this function calledverify successful upvote. I wrote this.

This is deterministic. That's what Iwant to show you. What does this do?Well, we see if you remember we weretracing in the agent loop, we're justadding history events. So, we reflect onthat, and we see if there was a browserclickon the upvote and if it's successful,but really successful, then we say true.But there's a huge but here, which iswe have now cases for failed login. Ifthere's a tool named harness auto login,and if the message starts with failed,then we return early and we say no, no,this failed. We're removing thelie, okay? Similarly, unrecovered loginredirect. We look over our agent loopstools that we've been pushing into.Um, and if we see that the harness autologin didn't run.

And now we're on the page that is thelogin URL, then again, we just fail.Okay?Um, and so, we're what we're doing iswe're just adding like if this happened,if this happened, you just just fail.Return early. Is this clear? This iswhat a harness does. And so, let's runthis now with the harness.

Uh, npm run agent.Andnow it's going to go on Hacker News, andwe're going to repeat the same cycle.

Okay, it's going to come here, and nowit's still failed, but look, it stoppedlying because our harness checks thetool history and actually sees whathappened. This is what a harness issupposed to do. Great. This is alreadylike half the battle won because stepone to solving a problem is admittingyou have one, okay?

Test-driven development vibes. So, nowthat we're failing correctly, we cansucceed. And I'd like to show you thatIn the last diff, and then we'll finishthe talk here. So, number four.

Um, we have a whole new function. It'scalled login handler. Uh, I'll add somesyntax highlighting here so you don't goblind. Uh, but here, create loginhandler. This is all it does. Itruns every agent loop just before wepush to the traces, and it — this is whatit do. It checks the browser session'scurrent URL.

And if we're not on a login page, itjust says cool, I don't I return I havenothing for you. This computationally isnot costly at all, right? If you're noton the login page, but if you are on thelogin page,then it we fill ina temporary. This can be an environmentvariable. It can be secure, you get theidea. But we fill in credentials andsubmit the button programmatically fromthe harness, not from the agent,deterministically and securely becausethis file has access to any secrets.

Want it to, right? And so, this how howis this called? Well, this is called inthe agent loop. So, if we go back to ouragent loop and notice we were pushingtraces, yeah? This is where we push thetraces.Just before, if we have a login handlerwe call the login handler just beforethis in the agent loop. What does thelogin handler do? Well, if we're not onthe login page, it does nothing.

If we are on a login page, then itquickly will inject credentials andsubmit the form and then take you back.It will also add, as we can see here, itpushes a message into the queue saying,"Hey, I'm the harness. I logged in.You're good now." Is this clear? Yeah?

So, the harness is literallyharnessing the agent to somethingstable, something deterministic. That'swhat it's for, okay?Let's run this now and see what happens.

So, npm run agent.It's going to open Hacker News, and whenIt gets to the login. Now that harnessstep, it logged in and it upvoted thefirst one, and it closed.

Amazing. So, successfully upvoted alittle snitch for nilux, uh rank two, uhsucceeded after six iterations, and Ican click this and go into Hacker Newsand actually see indeed it was upvoted,um and it I can unvote now, which meansit was upvoted, right? So, um the agentused the computer, logged in as me withmy harness that I just made here onstage. That's the purpose. Is this clearso far? Do you understand the role of aharness? Look at you nodding. This ismusic to my ears. Fantastic.Something to my eyes. I don't know theIt's beauty to my eyes, kind of weird.We don't have an expression for that.Let's land the plane. I'm done. I thinkmy work here is done. What does thislook like in practice? Why? Why do I careso much about harnesses? Because theyrun the world. Models arenon-deterministic. And you want to doMore with less. You want to use a cheapmodel. Use something like Quinn or even something smaller. Use GPT-OSS.

It's free. And with a great harness, youcan go very far. That's why, at IBM, wecreate an open-source project that wedeploy in the enterprise that allowsvery large companies, huge companies, intheir private, data-sensitive areas,to perform RAG operations on all kindsof things, teams, calls, PDFs, andinvoices. Um, we build it. It's calledOpen RAG, and it's, it's RAG. I don't knowif RAG is cool or not anymore, butOpen RAG has a hell of a harness thatprovides enterprise-level security tolike asking questions with internal, veryvery siloed data. And, and that's kind ofwhere the harness engineering comes in.So, let's summarize. We covered a lot ofcontent. Was it a deep? I think it was adeep dive. It was a deep dive in like 18minutes or so. Um,we went pretty far. IIt's not. It should not be lost on you.

That I did not touch the prompt once.I did not change the system prompt. Wejust built a harnessand the outcome radically changed. Andof course, we can add secrets, we canadd tokens. Um yeah, we did a lot. Inthe end, I hope you understand what aharness is, the value it can present,and how you can use it. What's next? UmLook, Idon't have a crystal ball likeeveryone else here, um but it's not loston me that 2025 was the year of agents.

Yes? Uh 2026is the year of harnesses, I'm prettysure. Everybody. How many times is thisword used here? Um I thinkI would hope. I think it'd be pretty coolif 2027 was the year of dynamicon-the-fly generated harnesses. How coolwould that be? Like, you tell an agent, "Hey,do this for me. Buy me a flight ticket."Whatever it may be. And then, beforedoing the work, the agent creates aharness. This is similar to plan mode. AnyOf you using plan mode? But, but on steroids, the agent creates anactual harness, self-aware. It knows,"Oh, I can maybe hallucinate here. I can maybe," creates a harness, does the job,and returns back to you, guardrailed and everything. That is so cool.

Dynamic on-the-fly harnesses. I would, I, I think thisis honestly the next logical step towards AGI, and I would love to see it.

I don't know if this is just me being, uh,you know,weird guy with ideas, but, um, I thinkthat's kind of the direction.

So, with that, um, I'm almost out of time. I wouldbe really remiss if I didn't spend thelast, like, 30 seconds saying thank you somuch. The slides are on GitHub, uh, as, uh,am I, uh, and so I'd love to chat more.

Thank you.

>> [music]
