---
categories:
  - "[[Resources]]"
domain: engineering
title: "Context Is the New Code — Patrick Debois, Tessl"
source: "https://m.youtube.com/watch?v=bSG9wUYaHWU&pp=ugUEEgJlbg%3D%3D"
author: "AI Engineer"
published: 2026-05-03
created: 2026-05-06
description: "As AI coding agents become more capable, context is starting to matter as"
tags:
  - to-process
  - context-management
---

[music] >> There's there's a few people who want to start earlier. I know I'm going to take the opportunity to officially open kind of the architect track. There's no track host, so I do it myself. So, thank you for coming here. I hope you already had like a good conference. Um It's amazing that like so many people 

showed up. Um maybe before I start, um who's used any AI coding agent in this room? Raise your hand. Like lower it. Who hasn't? Raise your hand. Okay, my kind of people. Perfect. All right. Um Okay. Context is a new code. Or context development life cycle. Um I feel honored to be here. Every time I try to do a different talk at the AI 

engineering. So, this is a little bit of um you know, thinking ahead. It's an unpolished thought. It's not like everything's there, but is there anything there in AI anyway? But So, let's start. I assume you all are now vibe coding with prompts. I barely touch anymore kind of the code. I just tell the AI to do something different. So, I would say like 

context is the new code because it's being generated. A little bit more advanced maybe is I see myself having a tendency is I had large pieces of code that I was using maybe some helpers and some other pieces. And I just turned them into a skill. We had that in our into our product. It was an onboarding from, you know, AI agents. Um People have Python, Node.js, all the various things. Then they have different 

tools for packaging and it is impossible to actually code that. Like it will require a lot of coding. But if I just say a skill says please first figure out what their package manager is, then figure out what their ecosystem is, and then do these steps together with the user. You know, it's solved a lot more problems that we could ever code. So, that is another piece that I would say code is also transforming back into 

context as a skill as well, as a workflow that's reusable. And leave that with you. I like to think in parallels. In 2009, I don't know if there is any DevOps people in the room. It was kind of me saying like what if ops looked more like dev? And then we got like, hey, collaboration, kind of our deployment, all that stuff. So, kind of, you know, last year I started thinking, what if context is the code? How do we deal with this in a more 

consistent way? And it's basically saying if we have a software development life cycle how does a context development life cycle look like? Because we're basically shifting somewhere else. It's context, it's not code. How does it look like? I came up with this, you know, of course an infinity loop with some DevOps background. But the whole idea is that we generate a lot of context. Then hopefully we test the context. We distribute context maybe to some 

colleagues, to some other parts of the organization. We observe whether it works, and if it doesn't work or works, we call like, you know, adapt and regenerate the context and then go from there. So, that's kind of the loop of the talk that I'll be going for with some examples. So, step by step going through. Generate. It's probably the one that you're all most familiar with. Because you're all prompting. You're like the human context creation 

typing things, right? I was actually amazed that I just asked, tell me when my talk is at AI engineer, that it would fetch the website and it would just say, here's your talk. Like blew my mind. But hey, I I said like the context that I've given it, I'm Patrick, all that stuff, right? So, very simple context. It's what you do probably a lot in your setup. If you get a little bit more advanced, you say that prompting is tedious. I want to have reusable prompts. So, you know, depending on the flavor of your 

coding agents, they call it instructions. Luckily, there's a little bit of a standardization now happening where it's like an agent.md and some pieces like that. Boo Claude for still calling it Claude.md, but anyway, you get the picture. There's like reusable prompts, reusable pieces of context that we're doing. We can also bring other context in. If we have documentation of libraries that we use day to day we want to pull that in because the LLMs 

might not have the latest documentation. And so it's hallucinating. Is it version two, version three? We don't know. So, we give it a context and say, please download the documentation. Hopefully then agent optimized. And then they will do a better job at generating the code for that version of the library. Another piece of getting better context and creating context from libraries. And of course, it wouldn't be complete if we would say pull context from wherever. MC 

Get it from your GitLab, GitHub, kind of Slack. All context we're pulling in, we're creating. Even a ticket is creating context because we're pulling that in while we go there. And then maybe the new kid on the block is, okay, what if we start like writing our prompts as specification spec-driven development which then gets broken down by the agent into a planning mode into step by step kind of prompts that it then kind of 

runs through. So, a lot creation happening in that field. You know, simple. This is probably what you're closest to. But when you're typing all that context and creating all that context you change two lines in your Claude.md. Do you know the impact? Is it like YOLO? Looks good to me. Let's do it. You have to think about how do we test things? It's not just about we have a piece of 

code and we have a piece of context now. We need to write tests to see what is the impact. New coding agent? We don't know where the lines still work. Now, it's not new in the world of AI engineering but it's not that common yet in the world of coding with AI that you start writing evals for which are tests for your kind of code context. Uh a little bit hard to read, but you 

know, if you think in parallels we have different levels of testing in code, and the simple one could be linting. Your IDE is has the swiggly lines like, hey, this is not like, you know there's some incorrect syntax or you could do better like that. Here's an example of a validation of a skill where we say, well, you need to have the description. It can only be so long. So, it's validating according to the spec of the format of the context in 

this case. Simple analogy, simple linter that you can run. And then you can do other things like and and I haven't found maybe the good coding equivalent, but think of this as a Grammarly. Right? So, if you write context um is it actually can the agent understand what you're writing? If you write two words, it's not verbose enough for it to actually understand the context. So, what you can do is you can say ask is 

like, okay, you know, given this context, what do you think about Do you understand this? And then you can get feedback like, oh, it's not explicitly enough written or it's not complete. Like you're missing pieces. So, that's kind of from tools as well. So, whenever you're writing now your context, you get a Grammarly saying, hey do this. That's why I like to voice code. For some reason, I'm way more 

elaborate voice coding than typing. I'm a bad typer, two fingers still after so many years. But when I talk, I was like, you know, I see the the sentences come on the screen, but it helps to get good context there. All right, another kind of test. So, imagine you put in your Claude.md or agent.md, I should say. Now, um every API point must use the prefix awesome. Right? You have some convention in your company. Right? Which is great. 

So, your prompter will be then, add me a new endpoint to save a user. And you expect actually your coding agent to just say the code that's being generated has kind of {slash} awesome {slash} user. That's great. But the way we can test this is by asking then an LLM the code that was generated does it actually start with {slash} awesome? Now, you can do that with 

regex, I know. This is just for example purposes, but you can ask it to kind of judge your code based on your criteria and whether it did the right thing. Right? So, imagine you would ask the same question without your context above. No LLM is ever going to prefix your URL with awesome. So, that's kind of where your content or your company specific, your team specific things come in, and that's why you still write those tests to see if this still works. Now, maybe 

Gemini kind of reacts differently than Copilot or something, and in your company you need to make it more, you know, switchable of context. With this, you run the tests, and you can actually tell. That's the difference. And then you can make like whole suites, and I would compare that almost to unit tests. I have a bunch of these tests, and they tell me whether that's actually, you know, good code, the code is following the rules, and everything's fine. In this case, it's even kind of 

infrastructure as code. It doesn't need to be code only. It could be various things. Could be config files as well. And I just have It's hard to read, but a bunch of kind of criteria that I just run every time to do that. But, if you want to test, you know, whether an endpoint has {slash} awesome {slash} user, there's a real test that we want to run, which is I want to test the endpoint. I just don't want only to check the code. I 

want to have it running. So, when you give the judge a tool, and the judge becomes an agent, and it can do things in a sandbox and execute stuff. It can actually do the do the curl. So, you can bind LLM as a judge with kind of some tooling, and then you can have multitude of tests actually, you know, in this case, it kind of ends up being an end-to-end test, right? Because it's not just looking at the file, it's actually 

running the piece with everything that it's supposed to do. And then I can do this like given a certain commit in my repo, I want to run this scenario given this piece of context, did it make a difference? Yes or no? So, you're kind of like building this up while you're committing context also within your repo. And because we now have tests, and it gives us feedback whether it's working yes or no, or what it's missing, we can 

optimize context. So, that's kind of the, you know, you we can put that in a code action or something that says like, "Okay, fix this context. Improve this context." With all the feedback the LLM has given us to improve that. So, you know, again, coding uh improvements, but we start thinking more in testing that piece as well. Now, one of the first reactions is once you have tests and optimizations, 

can we run this in a CI/CD system because that's perfect, right? That's where we run our all our tests and our test suites and do that. Now, there's a little bit of a weird thing. If you run evals, you run it once, you run it another time, it might not give the same result. Remember, undeterministic things. So, you cannot say, "Well, run it once, and then if it passes or not." You're going to be in 

for a treat because it's like, "Ah, I I can't debug that." So, think about this like you run it five times, and out of five, how many times does it succeed? And, you know, maybe in several cases it hits 100% all the time, which is great. But, in others not. And depending on how you change your context, it will influence which test actually work or not. I find it personally helpful to think about this as error budgets. 

I give a set of tests an error budget that I really care about, so it it's only allowed like, you know, to fail minimally, and other pieces are okay. So, that's how you have to think about testing context. You cannot do like exact testing all the time. It's a different way that this works. All right. So, generate. Hopefully, you understand what the testing could do for you. And distribute. 

Maybe that's also something you already did. If you maybe have checked context into your repo, right? Which is great, you know, all of a sudden it becomes available, your colleague checks it out. Uh zero friction, I can push, I can share. But, we have another mechanism for doing things. Think of this like Imagine you have a reusable context that you want to reuse across multiple projects, across multiple teams. We had 

the concept of a library. So, what if we package kind of pieces of context, and then we are able to install pieces of context that we need for this project. Guidelines, front end. It doesn't matter for that. And then if we take it that up a notch, how to discover what packages exists? That's a registry. Right? Now, in that way, it's no surprise that you'll see things like skills and kind 

of the Tesla registry in the marketplace, where you can find a multitude of skills. Now, the reality is 99.9, and I mean that in a very sincere way, of the skills is crap. But, it's good to learn from others to see what they're doing. But, hardly of them, if you run kind of any set of evals on there, is actually up to a quality standard. Now, 

that will likely improve. But, there's also a tendency is that a lot of the skills and pieces, people actually want to put that in their own registry. So, I'll come to that later again. But, so you start seeing the gist, a skill not only contains context, it can contain scripts, it can contain documents, contain bunch of things. So, is this kind of the package format? Probably, you know, plugins 

could now also contain MCP, but you see there's like a standard coming in. Skills all of a sudden, when that came out, all the coding agents said, "We're supporting this as almost like a package format for people to distribute their context on." And then when I have one piece of context, I have dependencies. And I'm sorry, but also with context we're going to have dependency hell. Right? I I'm I'm I'm going to download this for front end, and maybe it's conflicting what is in the React context 

package. And so, you start having to deal with that as well. So, you start seeing also uh packages that's uh mirror your library versions, your code ver like your context versions, and kind of pull that in as well. And of course, when we have packages and people are publishing things in registry, we need security. Right? Open claw. Thank you for that. Like everybody all of a sudden became aware that we need more secure things because we are able to run things 

on our laptop that are not and coming from strangers, right? So, Snyk has a way of scanning context, right? It's doing some credential handling. It's uh exposing some third-party pieces. So, you start seeing the scanners on the context as well. And then when you think about security, who actually built the skill? How was it built? With what model was this built? 

So, all kind of capturing what we learned in maybe with packaging, like the SBOM, is kind of the AI SBOM, like the packaged of context that we're putting in. So, you've seen still on the path, right? You generate, evaluate, distribute. Let's move into observe. When you are making libraries off skills and context for others, 

and I don't mean copy and paste this over Slack or something. But, when you actually want to maintain this as something somebody else can use, similar to a library, um when they start using that, how do you get feedback whether that still works? Now, a great place to get feedback is actually by looking at the agent logs. So, imagine developer one coding on the project, and the agent is not doing what they want. 

They could put this into their context, which is great, right? Okay, let let me do the TDD almost like, you know, I hit a problem. It's not TDD, but you get my gist. Um or what if we at a team or an organization scale would look at the logs every time an agent said, "We're missing this piece." And we surface that and say, "If everybody's missing this piece, we should create context for this." 

And then we distribute the context to everybody, and all of a sudden the impact of improvement is for everybody. Luckily, like the agent and D, there's now our standards becoming for logs. So, we can read from logs, and that's part of our feedback channel to see if the agent is actually using or missing some of the context. Any feedback you get on a PR that's not complete, that's feedback on your context because 

that PR was created with certain pieces of context. If you say this is not correct, you can kind of keep arguing on the PR, or you can just say, "Let's improve the context." So, the next iteration actually improves, uh and you don't hit that same problem again. What about running code in production that was generated from context. And that's not correct because yes, we do our PR reviews and we say thumbs up, thumbs down and we give the 

feedback, but the actual feedback is also in production when it's running. So, this is a tool that actually instruments your code, pushes it out, it's almost like a wrapper, it pushes it out to production. When it fails, it says, "These pieces of code were changed and were failing. Hey, in this case, input, output, it did something wrong. Can we create a test case for this? So, the next time we don't hit this again in production?" Feedback loop. 

Now, these are all kind of pretty trivial like missing pieces of context or improvements. But, if you run agents and the equivalent of scanning maybe, you know, in the CICD is you need to make sure when it's running in production, is it not doing strange things? So, we need kind of a way of looking at that. Now, I've been toying myself with uh you know, sandboxing agents and it is a very resourceful 

at finding things. I like, okay, you know, run this thing, try to figure out like anything useful to get break out of the system. And okay, it uses my environment variables. Okay, stupid. Let's let me remove the secret. Let me look at your memory files. So, you have to really make make sure that like whatever it's doing, you can have a way of tracing this as well. And uh apologize again for kind of the 

slide, but the gist is we can have a sandbox where the agent runs inside. But, your code agent by default without any restrictions loads your agent.md, you load your skill.md. Like, nothing is blocking that. So, if you download this, immediately it's loaded. So, you can't filter that with sandboxes. You need to have another way. 

I call that a context filter. Think of this as a web application firewall that just filters out any patterns or prompt injections or stuff that is coming in directly in that piece. And if you take that, there's a lot of talk here as well on harness engineering. Harness engineering itself also has this kind of full observability, looking at logs, looking at traces, looking at feedback. So, it's kind of, you know, useful for training pieces, but as much useful for 

running your own pieces well. Those were the pieces for me today. I would say for a lot of people, there's like create context, test context. Think of this as your library authoring tool loop. And then when you push this into the enterprise, there's an organizational loop. Hey, I made a library, somebody else is using it. I'm looking at whatever that's useful, whether that's still working, whether that's still working for all the other pieces. So, 

that's kind of like the kind of improvement almost like sonar CICD model for context. And then you're currently probably doing a lot at the individual solo model, you're improving, you're honing, crafting your own kind of markdown. What if you start doing this more with your team? Make that a reflex. If it's missing, add some context. What if you put that out to a team of teams and you start having a flywheel, you know, if you fix it here, 

the other team can reuse it and and that's kind of like, you know, scaling things out into the organization as well. And so, there's a lot of talk about LLMs and coding agents and I all love them, but the way that I see it is they're just the engine. If you give the engine the wrong fuel, which is context, they're not going to perform. So, and you can't do anything on the LLMs, at least not me, right? I'm just using the coding agent, I'm using whatever they 

give me, but I can optimize my context uh and that's I think the message uh doing this more in an engineered way than just copy and pasting things and hoping for the best in there. If you like this talk, connect on LinkedIn for the slides. Uh give me some feedback, good and bad. If you want to try Tessel where we implement some of the pieces of this, uh have a go. And if you're also interested in another conference, I know, you can never have enough conferences, uh visit uh AI 

DevCon, which I curate the content for uh here in London first and second of June. And that's it. I can maybe take a few questions. >> [applause] >> Any questions? Sure. So, I was wondering if you have any thoughts about like more exotic forms of context like I don't know, the traditional ones. So, for example, one 

of the things I'm working on is automated system for uh scoping out architectural problems and like trying to create hard definitions for them so that you can feed that to the agent and, you know, create actual objectives uh tests. Cool. Yeah. Microphones. Um and one of the things I've been testing out is like the ability to create consistency as a form of context or as a form of eval. So, um given this rough like very loose definition of what the plan is, if can you put that if you try that agent 

system, turn that into a really crisp definition, and you just have that done in parallel, how often do you get the same crisp definition? And if they're all over the place, then the original definition was so poor, you need to like go back to base principles or to an architect. But, if they're all the same, then it's probably a pretty good definition and you can carry on with the downstream process. So, I think it's like besides just code and typical evals, um any other sources of context for generating context that you think is useful? Um I don't have maybe a a specific answer 

to your like exotic case, but uh I would say that maybe the piece that people are underestimating is that once you you know, you thought you were going to save time by writing actually your context uh instead of all your code, but if you take this rigorously, you're going to spend time on writing the right evals. Right. And that's kind of like, you know, a lot of work to kind of because now you don't only have one prompt that you're trying to get right. It's like all the prompts of the evals 

and that like if people do almost like a like the more advanced people, they almost have their own process and they they build their own process on top of like for building the right evals on your business case as well. So, yeah. Good question. Thank you. Any other questions? If not, I'll be around. Um say hi. I'll also going to be at the Tessel booth. So, thank you very much and I'm going to make space for the next speaker. Thank you. 

>> [music] 

<p>
 <span data-rw-start="7.205" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="14.92" data-rw-transcript-version="2">
 &gt;&gt; There’s a few people who want to
 </span>
 <span data-rw-start="16.44" data-rw-transcript-version="2">
 start earlier.
 </span>
 <span data-rw-start="17.92" data-rw-transcript-version="2">
 I know I’m going to take the opportunity
 </span>
 <span data-rw-start="19.56" data-rw-transcript-version="2">
 to officially open kind of the
 </span>
 <span data-rw-start="22.24" data-rw-transcript-version="2">
 architect track. There’s no track host,
 </span>
 <span data-rw-start="24" data-rw-transcript-version="2">
 so I do it myself. So, thank you for
 </span>
 <span data-rw-start="25.64" data-rw-transcript-version="2">
 coming here. I hope you already had like
 </span>
 <span data-rw-start="27.56" data-rw-transcript-version="2">
 a good conference. Um
 </span>
 <span data-rw-start="30" data-rw-transcript-version="2">
 It’s amazing that like so many people
 </span>
 <span data-rw-start="31.4" data-rw-transcript-version="2">
 showed up. Um maybe before I start, um
 </span>
 <span data-rw-start="35.04" data-rw-transcript-version="2">
 who’s used any AI coding agent in this
 </span>
 <span data-rw-start="37.76" data-rw-transcript-version="2">
 room? Raise your hand.
 </span>
 <span data-rw-start="40.36" data-rw-transcript-version="2">
 Like lower it. Who hasn’t? Raise your
 </span>
 <span data-rw-start="43.04" data-rw-transcript-version="2">
 hand.
 </span>
 <span data-rw-start="44.8" data-rw-transcript-version="2">
 Okay, my kind of people. Perfect. All
 </span>
 <span data-rw-start="46.76" data-rw-transcript-version="2">
 right.
 </span>
 <span data-rw-start="48.24" data-rw-transcript-version="2">
 Um
 </span>
 <span data-rw-start="50.88" data-rw-transcript-version="2">
 Okay. Context is a new code.
 </span>
 <span data-rw-start="54.64" data-rw-transcript-version="2">
 Or context development life cycle. Um I
 </span>
 <span data-rw-start="56.8" data-rw-transcript-version="2">
 feel honored to be here. Every time I
 </span>
 <span data-rw-start="58.92" data-rw-transcript-version="2">
 try to do a different talk at the AI
 </span>
 <span data-rw-start="60.8" data-rw-transcript-version="2">
 engineering.
 </span>
 <span data-rw-start="61.92" data-rw-transcript-version="2">
 So, this is a little bit of, um
 </span>
 <span data-rw-start="64.12" data-rw-transcript-version="2">
 you know, thinking ahead. It's an
 </span>
 <span data-rw-start="65.84" data-rw-transcript-version="2">
 Unpolished thought. It's not like
 </span>
 <span data-rw-start="68.72" data-rw-transcript-version="2">
 everything's there, but is there
 </span>
 <span data-rw-start="70.2" data-rw-transcript-version="2">
 anything there in AI anyway? But
 </span>
 <span data-rw-start="74" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="75.8" data-rw-transcript-version="2">
 let's start.
 </span>
</p>
<p>
 <span data-rw-start="77.4" data-rw-transcript-version="2">
 I assume
 </span>
 <span data-rw-start="79.2" data-rw-transcript-version="2">
 you all are now vibe coding with
 </span>
 <span data-rw-start="81.08" data-rw-transcript-version="2">
 prompts. I barely touch anymore kind of
 </span>
 <span data-rw-start="84.32" data-rw-transcript-version="2">
 the code. I just tell the AI to do
 </span>
 <span data-rw-start="86.84" data-rw-transcript-version="2">
 something different.
 </span>
</p>
<p>
 <span data-rw-start="88.52" data-rw-transcript-version="2">
 So, I would say like
 </span>
 <span data-rw-start="91.28" data-rw-transcript-version="2">
 context is the new code because it's
 </span>
 <span data-rw-start="93.8" data-rw-transcript-version="2">
 being generated.
 </span>
 <span data-rw-start="95.6" data-rw-transcript-version="2">
 A little bit more advanced maybe is
 </span>
 <span data-rw-start="98.68" data-rw-transcript-version="2">
 I see myself having a tendency is I had
 </span>
 <span data-rw-start="101.4" data-rw-transcript-version="2">
 large pieces of code that I was using
 </span>
 <span data-rw-start="104.36" data-rw-transcript-version="2">
 maybe some helpers and some other
 </span>
 <span data-rw-start="105.92" data-rw-transcript-version="2">
 pieces.
 </span>
 <span data-rw-start="107.36" data-rw-transcript-version="2">
 And I just turned them into a skill.
 </span>
 <span data-rw-start="110.4" data-rw-transcript-version="2">
 We had that in our into our product. It
 </span>
 <span data-rw-start="112.44" data-rw-transcript-version="2">
 was an onboarding from, you know, AI
 </span>
 <span data-rw-start="115.16" data-rw-transcript-version="2">
 agents. Um
 </span>
 <span data-rw-start="116.88" data-rw-transcript-version="2">
 People have Python, Node.js, all the
 </span>
 <span data-rw-start="119.64" data-rw-transcript-version="2">
 various things. Then they have different
 </span>
 <span data-rw-start="121.48" data-rw-transcript-version="2">
 tools for packaging and
 </span>
 <span data-rw-start="124" data-rw-transcript-version="2">
 It is impossible to actually code that.
 </span>
</p>
<p>
 <span data-rw-start="126.28" data-rw-transcript-version="2">
 Like, it will require a lot of coding.
 </span>
 <span data-rw-start="128.92" data-rw-transcript-version="2">
 But if I just say a skill says,
 </span>
 <span data-rw-start="132.4" data-rw-transcript-version="2">
 please first figure out what their
 </span>
 <span data-rw-start="133.92" data-rw-transcript-version="2">
 package manager is, then figure out what
 </span>
 <span data-rw-start="136.28" data-rw-transcript-version="2">
 their ecosystem is, and then do these
 </span>
 <span data-rw-start="138.44" data-rw-transcript-version="2">
 steps together with the user.
 </span>
</p>
<p>
 <span data-rw-start="140.64" data-rw-transcript-version="2">
 You know, it's solved a lot more
 </span>
 <span data-rw-start="142.4" data-rw-transcript-version="2">
 problems that we could ever code. So,
 </span>
 <span data-rw-start="144.96" data-rw-transcript-version="2">
 that is another piece that I would say
 </span>
 <span data-rw-start="147.2" data-rw-transcript-version="2">
 code is also transforming back into
 </span>
 <span data-rw-start="150.92" data-rw-transcript-version="2">
 context as a skill as well, as a
 </span>
 <span data-rw-start="153.4" data-rw-transcript-version="2">
 workflow that's reusable. And
 </span>
 <span data-rw-start="155.8" data-rw-transcript-version="2">
 leave that with you.
 </span>
</p>
<p>
 <span data-rw-start="157.64" data-rw-transcript-version="2">
 I like to think in parallels.
 </span>
 <span data-rw-start="159.72" data-rw-transcript-version="2">
 In 2009, I don't know if there are any
 </span>
 <span data-rw-start="161.44" data-rw-transcript-version="2">
 DevOps people in the room. It was kind
 </span>
 <span data-rw-start="163.44" data-rw-transcript-version="2">
 of me saying, like, what if ops looked
 </span>
 <span data-rw-start="165.32" data-rw-transcript-version="2">
 more like dev? And then we got,
 </span>
 <span data-rw-start="167.68" data-rw-transcript-version="2">
 hey, collaboration, kind of our
 </span>
 <span data-rw-start="169.72" data-rw-transcript-version="2">
 deployment, all that stuff. So, kind of,
 </span>
 <span data-rw-start="172.64" data-rw-transcript-version="2">
 you know, last year I started thinking,
 </span>
 <span data-rw-start="174.04" data-rw-transcript-version="2">
 what if context
 </span>
 <span data-rw-start="176.68" data-rw-transcript-version="2">
 is the code?
 </span>
</p>
<p>
 <span data-rw-start="178.56" data-rw-transcript-version="2">
 How do we deal with this in a more
 </span>
 <span data-rw-start="180.52" data-rw-transcript-version="2">
 Consistent way?
 </span>
</p>
<p>
 <span data-rw-start="182.88" data-rw-transcript-version="2">
 And
 </span>
 <span data-rw-start="184" data-rw-transcript-version="2">
 it's basically saying if we have a
 </span>
 <span data-rw-start="185.88" data-rw-transcript-version="2">
 software development life cycle,
 </span>
 <span data-rw-start="188.72" data-rw-transcript-version="2">
 how does a context development life
 </span>
 <span data-rw-start="190.32" data-rw-transcript-version="2">
 cycle look like? Because we're basically
 </span>
 <span data-rw-start="192.76" data-rw-transcript-version="2">
 shifting somewhere else. It's context,
 </span>
 <span data-rw-start="195.32" data-rw-transcript-version="2">
 it's not code. How does it look like?
 </span>
</p>
<p>
 <span data-rw-start="198.56" data-rw-transcript-version="2">
 I came up with this, you know, of course
 </span>
 <span data-rw-start="200.36" data-rw-transcript-version="2">
 an infinity loop with some DevOps
 </span>
 <span data-rw-start="201.92" data-rw-transcript-version="2">
 background. But the whole idea is that
 </span>
 <span data-rw-start="204.4" data-rw-transcript-version="2">
 we generate a lot of context.
 </span>
 <span data-rw-start="206.96" data-rw-transcript-version="2">
 Then, hopefully, we test the context. We
 </span>
 <span data-rw-start="209.2" data-rw-transcript-version="2">
 distribute context, maybe to some
 </span>
 <span data-rw-start="211.24" data-rw-transcript-version="2">
 colleagues, to some other parts of the
 </span>
 <span data-rw-start="212.96" data-rw-transcript-version="2">
 organization. We observe whether it
 </span>
 <span data-rw-start="215.32" data-rw-transcript-version="2">
 works, and if it doesn't work or works,
 </span>
 <span data-rw-start="217.52" data-rw-transcript-version="2">
 we call, like, you know, adapt and
 </span>
 <span data-rw-start="219.88" data-rw-transcript-version="2">
 regenerate the context, and then go from
 </span>
 <span data-rw-start="221.84" data-rw-transcript-version="2">
 there. So, that's kind of the
 </span>
 <span data-rw-start="223.64" data-rw-transcript-version="2">
 loop of the talk that I'll be going for,
 </span>
 <span data-rw-start="225.84" data-rw-transcript-version="2">
 with some examples.
 </span>
</p>
<p>
 <span data-rw-start="227.52" data-rw-transcript-version="2">
 So, step by step, going through.
 </span>
 <span data-rw-start="230.28" data-rw-transcript-version="2">
 Generate. It's probably the one that
 </span>
 <span data-rw-start="232.76" data-rw-transcript-version="2">
 you're all most familiar with.
 </span>
</p>
<p>
 <span data-rw-start="235.16" data-rw-transcript-version="2">
 Because you're all prompting,
 </span>
 <span data-rw-start="237.52" data-rw-transcript-version="2">
 you're like the human context creation.
 </span>
 <span data-rw-start="240.92" data-rw-transcript-version="2">
 Typing things, right? I was actually
 </span>
 <span data-rw-start="243.6" data-rw-transcript-version="2">
 amazed that I just asked, tell me when
 </span>
 <span data-rw-start="245.44" data-rw-transcript-version="2">
 my talk is at AI engineer, that it would
 </span>
 <span data-rw-start="247.56" data-rw-transcript-version="2">
 fetch the website and it would just say,
 </span>
 <span data-rw-start="249.16" data-rw-transcript-version="2">
 here's your talk. Like blew my mind. But
 </span>
 <span data-rw-start="252" data-rw-transcript-version="2">
 hey, I I said like the context that I've
 </span>
 <span data-rw-start="253.88" data-rw-transcript-version="2">
 given it, I'm Patrick, all that stuff,
 </span>
 <span data-rw-start="256.079" data-rw-transcript-version="2">
 right? So, very simple context. It's
 </span>
 <span data-rw-start="258.12" data-rw-transcript-version="2">
 what you do probably a lot in your
 </span>
 <span data-rw-start="260.959" data-rw-transcript-version="2">
 setup.
 </span>
</p>
<p>
 <span data-rw-start="263.16" data-rw-transcript-version="2">
 If you get a little bit more advanced,
 </span>
 <span data-rw-start="264.52" data-rw-transcript-version="2">
 you say that prompting is tedious. I
 </span>
 <span data-rw-start="266.52" data-rw-transcript-version="2">
 want to have reusable prompts. So, you
 </span>
 <span data-rw-start="269.24" data-rw-transcript-version="2">
 know, depending on the flavor of your
 </span>
 <span data-rw-start="271.16" data-rw-transcript-version="2">
 coding agents, they call it
 </span>
 <span data-rw-start="272.28" data-rw-transcript-version="2">
 instructions.
 </span>
 <span data-rw-start="273.84" data-rw-transcript-version="2">
 Luckily, there's a little bit of a
 </span>
 <span data-rw-start="275.32" data-rw-transcript-version="2">
 standardization now happening where it's
 </span>
 <span data-rw-start="277.28" data-rw-transcript-version="2">
 like an agent.md and some pieces like
 </span>
 <span data-rw-start="279.88" data-rw-transcript-version="2">
 that. Boo Claude for still calling it
 </span>
 <span data-rw-start="282.12" data-rw-transcript-version="2">
 Claude.md, but anyway, you get the
 </span>
 <span data-rw-start="284.24" data-rw-transcript-version="2">
 picture. There's like reusable prompts,
 </span>
 <span data-rw-start="286.72" data-rw-transcript-version="2">
 reusable pieces of context that we're
 </span>
 <span data-rw-start="288.84" data-rw-transcript-version="2">
 Doing.
 </span>
</p>
<p>
 <span data-rw-start="291.2" data-rw-transcript-version="2">
 We can also bring other context in.
 </span>
 <span data-rw-start="294.4" data-rw-transcript-version="2">
 If we have documentation of libraries
 </span>
 <span data-rw-start="296.76" data-rw-transcript-version="2">
 that we use day to day,
 </span>
 <span data-rw-start="298.6" data-rw-transcript-version="2">
 we want to pull that in because the LLMs
 </span>
 <span data-rw-start="300.56" data-rw-transcript-version="2">
 might not have the latest documentation.
 </span>
 <span data-rw-start="303.04" data-rw-transcript-version="2">
 And so it's hallucinating. Is it version
 </span>
 <span data-rw-start="305.08" data-rw-transcript-version="2">
 two, version three? We don't know. So,
 </span>
 <span data-rw-start="307.08" data-rw-transcript-version="2">
 we give it a context and say, please
 </span>
 <span data-rw-start="309.52" data-rw-transcript-version="2">
 download the documentation. Hopefully
 </span>
 <span data-rw-start="311.84" data-rw-transcript-version="2">
 then the agent is optimized. And then they will
 </span>
 <span data-rw-start="314.44" data-rw-transcript-version="2">
 do a better job at generating the code
 </span>
 <span data-rw-start="316.68" data-rw-transcript-version="2">
 for that version of the library.
 </span>
</p>
<p>
 <span data-rw-start="318.8" data-rw-transcript-version="2">
 Another piece of getting better context
 </span>
 <span data-rw-start="320.96" data-rw-transcript-version="2">
 and creating context from libraries.
 </span>
 <span data-rw-start="324.08" data-rw-transcript-version="2">
 And of course, it wouldn't be complete
 </span>
 <span data-rw-start="325.96" data-rw-transcript-version="2">
 if we would say
 </span>
 <span data-rw-start="327.6" data-rw-transcript-version="2">
 pull context from wherever. MC
 </span>
 <span data-rw-start="332.08" data-rw-transcript-version="2">
 Get it from your GitLab, GitHub, kind of
 </span>
 <span data-rw-start="334.56" data-rw-transcript-version="2">
 Slack.
 </span>
 <span data-rw-start="335.92" data-rw-transcript-version="2">
 All context we're pulling in, we're
 </span>
 <span data-rw-start="337.72" data-rw-transcript-version="2">
 creating. Even a ticket is creating
 </span>
 <span data-rw-start="339.84" data-rw-transcript-version="2">
 context because we're pulling that in
 </span>
 <span data-rw-start="342.64" data-rw-transcript-version="2">
 while we go there.
 </span>
 <span data-rw-start="345.72" data-rw-transcript-version="2">
 And then maybe the new kid on the block
 </span>
 <span data-rw-start="347.96" data-rw-transcript-version="2">
 Is, okay, what if we
 </span>
 <span data-rw-start="349.92" data-rw-transcript-version="2">
 start like writing our prompts as
 </span>
 <span data-rw-start="351.52" data-rw-transcript-version="2">
 specification, specification-driven development,
 </span>
 <span data-rw-start="354.24" data-rw-transcript-version="2">
 which then gets broken down by the agent
 </span>
 <span data-rw-start="356.28" data-rw-transcript-version="2">
 into a planning mode, into step-by-step
 </span>
 <span data-rw-start="358.92" data-rw-transcript-version="2">
 kind of prompts that it then kind of
 </span>
 <span data-rw-start="361.4" data-rw-transcript-version="2">
 runs through. So, a lot creation
 </span>
 <span data-rw-start="363.68" data-rw-transcript-version="2">
 happening in that field.
 </span>
</p>
<p>
 <span data-rw-start="366.36" data-rw-transcript-version="2">
 You know, simple. This is probably what
 </span>
 <span data-rw-start="368.72" data-rw-transcript-version="2">
 you're closest to.
 </span>
</p>
<p>
 <span data-rw-start="370.84" data-rw-transcript-version="2">
 But
 </span>
 <span data-rw-start="372.28" data-rw-transcript-version="2">
 when you're typing all that context and
 </span>
 <span data-rw-start="374.12" data-rw-transcript-version="2">
 creating all that context,
 </span>
 <span data-rw-start="376.44" data-rw-transcript-version="2">
 you change two lines in your Claude.md.
 </span>
 <span data-rw-start="379.92" data-rw-transcript-version="2">
 Do you know the impact?
 </span>
 <span data-rw-start="381.96" data-rw-transcript-version="2">
 Is it like YOLO? Looks good to me. Let's
 </span>
 <span data-rw-start="384.16" data-rw-transcript-version="2">
 do it. You have to think about how do we
 </span>
 <span data-rw-start="387.16" data-rw-transcript-version="2">
 test things?
 </span>
 <span data-rw-start="388.88" data-rw-transcript-version="2">
 It's not just about we have a piece of
 </span>
 <span data-rw-start="391.72" data-rw-transcript-version="2">
 code and we have a piece of context now.
 </span>
 <span data-rw-start="394.44" data-rw-transcript-version="2">
 We need to write tests to see what is
 </span>
 <span data-rw-start="397.08" data-rw-transcript-version="2">
 the impact. New coding agent? We don't
 </span>
 <span data-rw-start="399.96" data-rw-transcript-version="2">
 know where the lines still work.
 </span>
 <span data-rw-start="402.56" data-rw-transcript-version="2">
 Now, it's not new in the world of AI
 </span>
 <span data-rw-start="405.56" data-rw-transcript-version="2">
 engineering, but it's not that common yet.
 </span>
</p>
<p>
 <span data-rw-start="408.76" data-rw-transcript-version="2">
 In the world of coding with AI that you
 </span>
 <span data-rw-start="411.44" data-rw-transcript-version="2">
 start writing evals for which are tests
 </span>
 <span data-rw-start="415.68" data-rw-transcript-version="2">
 for your kind of code context.
 </span>
 <span data-rw-start="419.72" data-rw-transcript-version="2">
 Uh, a little bit hard to read, but you
 </span>
 <span data-rw-start="421.24" data-rw-transcript-version="2">
 know, if you think in parallels,
 </span>
 <span data-rw-start="423.8" data-rw-transcript-version="2">
 we have different levels of testing in
 </span>
 <span data-rw-start="425.88" data-rw-transcript-version="2">
 code, and the simple one could be
 </span>
 <span data-rw-start="428.04" data-rw-transcript-version="2">
 linting. Your IDE has the swiggly
 </span>
 <span data-rw-start="430.92" data-rw-transcript-version="2">
 lines like, hey, this is not like, you
 </span>
 <span data-rw-start="432.76" data-rw-transcript-version="2">
 know,
 </span>
 <span data-rw-start="433.56" data-rw-transcript-version="2">
 there's some
 </span>
 <span data-rw-start="434.8" data-rw-transcript-version="2">
 incorrect syntax or you could do better
 </span>
 <span data-rw-start="436.88" data-rw-transcript-version="2">
 like that.
 </span>
</p>
<p>
 <span data-rw-start="438.36" data-rw-transcript-version="2">
 Here's an example of a validation of a
 </span>
 <span data-rw-start="440.44" data-rw-transcript-version="2">
 skill, where we say, well, you need to
 </span>
 <span data-rw-start="443.12" data-rw-transcript-version="2">
 have the description. It can only be so
 </span>
 <span data-rw-start="445.92" data-rw-transcript-version="2">
 long. So, it's validating according to
 </span>
 <span data-rw-start="448.28" data-rw-transcript-version="2">
 the spec of the format of the context in
 </span>
 <span data-rw-start="450.88" data-rw-transcript-version="2">
 this case.
 </span>
</p>
<p>
 <span data-rw-start="452.16" data-rw-transcript-version="2">
 Simple analogy, simple linter that you
 </span>
 <span data-rw-start="455.24" data-rw-transcript-version="2">
 can run.
 </span>
 <span data-rw-start="458.12" data-rw-transcript-version="2">
 And then you can do other things like
 </span>
 <span data-rw-start="460.12" data-rw-transcript-version="2">
 and, and I haven't found maybe the good
 </span>
 <span data-rw-start="461.84" data-rw-transcript-version="2">
 coding equivalent, but think of this as
 </span>
 <span data-rw-start="463.6" data-rw-transcript-version="2">
 a Grammarly.
 </span>
</p>
<p>
 <span data-rw-start="465.72" data-rw-transcript-version="2">
 Right? So, if you write context
 </span>
 <span data-rw-start="468.52" data-rw-transcript-version="2">
 um
 </span>
 <span data-rw-start="469.72" data-rw-transcript-version="2">
 is it actually can the agent understand
 </span>
 <span data-rw-start="472.68" data-rw-transcript-version="2">
 what you're writing? If you write two
 </span>
 <span data-rw-start="474.2" data-rw-transcript-version="2">
 words, it's not verbose enough for it to
 </span>
 <span data-rw-start="477.36" data-rw-transcript-version="2">
 actually understand the context. So,
 </span>
 <span data-rw-start="479.64" data-rw-transcript-version="2">
 what you can do is, you can say ask, is
 </span>
 <span data-rw-start="482.52" data-rw-transcript-version="2">
 like, okay, you know, given this
 </span>
 <span data-rw-start="484.24" data-rw-transcript-version="2">
 context, what do you think about? Do you
 </span>
 <span data-rw-start="486.52" data-rw-transcript-version="2">
 understand this? And then you can get
 </span>
 <span data-rw-start="488.36" data-rw-transcript-version="2">
 feedback like,
 </span>
 <span data-rw-start="491.96" data-rw-transcript-version="2">
 oh, it's not explicitly enough written
 </span>
 <span data-rw-start="495.28" data-rw-transcript-version="2">
 or it's not complete. Like, you're
 </span>
 <span data-rw-start="497.32" data-rw-transcript-version="2">
 missing pieces. So, that's kind of from
 </span>
 <span data-rw-start="500.08" data-rw-transcript-version="2">
 tools as well. So, whenever you're
 </span>
 <span data-rw-start="501.72" data-rw-transcript-version="2">
 writing now your context, you get a
 </span>
 <span data-rw-start="504.16" data-rw-transcript-version="2">
 Grammarly saying, hey,
 </span>
 <span data-rw-start="506.04" data-rw-transcript-version="2">
 do this. That's why I like to voice
 </span>
 <span data-rw-start="507.84" data-rw-transcript-version="2">
 code. For some reason, I’m way more
 </span>
 <span data-rw-start="510.12" data-rw-transcript-version="2">
 elaborate in voice coding than typing. I'm
 </span>
 <span data-rw-start="512.56" data-rw-transcript-version="2">
 a bad typer, still after so many years. But when I
 </span>
 <span data-rw-start="516.479" data-rw-transcript-version="2">
 talk, I was like, you know, I see the
 </span>
 <span data-rw-start="518.88" data-rw-transcript-version="2">
 sentences come on the screen, but it
 </span>
 <span data-rw-start="520.8" data-rw-transcript-version="2">
 helps to get good context there.
 </span>
</p>
<p>
 <span data-rw-start="523.68" data-rw-transcript-version="2">
 All right, another kind of test.
 </span>
 <span data-rw-start="526.24" data-rw-transcript-version="2">
 So, imagine you put in your Claude.md or agent.md, I should say. Now,
 </span>
 <span data-rw-start="528.72" data-rw-transcript-version="2">
 every API point must use the prefix
 </span>
 <span data-rw-start="531.2" data-rw-transcript-version="2">
 awesome.
 </span>
 <span data-rw-start="534.84" data-rw-transcript-version="2">
 Right? You have some convention in your
 </span>
 <span data-rw-start="536.12" data-rw-transcript-version="2">
 company. Right? Which is great.
 </span>
 <span data-rw-start="540.72" data-rw-transcript-version="2">
 So, your prompter will be then, add me a
 </span>
 <span data-rw-start="542.76" data-rw-transcript-version="2">
 new endpoint to save a user.
 </span>
 <span data-rw-start="545.6" data-rw-transcript-version="2">
 And you expect actually your coding
 </span>
 <span data-rw-start="548.36" data-rw-transcript-version="2">
 agent to just say the code that's being
 </span>
 <span data-rw-start="550.84" data-rw-transcript-version="2">
 generated has kind of {slash} awesome
 </span>
 <span data-rw-start="553.76" data-rw-transcript-version="2">
 {slash} user.
 </span>
 <span data-rw-start="555.44" data-rw-transcript-version="2">
 That's great.
 </span>
 <span data-rw-start="556.84" data-rw-transcript-version="2">
 But the way we can test this is by
 </span>
 <span data-rw-start="559.64" data-rw-transcript-version="2">
 asking then
 </span>
 <span data-rw-start="562.08" data-rw-transcript-version="2">
 an LLM
 </span>
 <span data-rw-start="563.72" data-rw-transcript-version="2">
 the code that was generated
 </span>
 <span data-rw-start="566" data-rw-transcript-version="2">
 does it actually start with {slash}
 </span>
 <span data-rw-start="568.96" data-rw-transcript-version="2">
 awesome? Now, you can do that with
 </span>
 <span data-rw-start="570.56" data-rw-transcript-version="2">
 regex, I know. This is just for example
 </span>
 <span data-rw-start="572.68" data-rw-transcript-version="2">
 purposes, but you can ask it to kind of
 </span>
 <span data-rw-start="575.72" data-rw-transcript-version="2">
 judge your code based on your criteria
 </span>
 <span data-rw-start="578.92" data-rw-transcript-version="2">
 and whether it did the right thing.
 </span>
 <span data-rw-start="580.8" data-rw-transcript-version="2">
 Right? So, imagine you would ask the
 </span>
 <span data-rw-start="583.6" data-rw-transcript-version="2">
 Same question without your context,
 </span>
 <span data-rw-start="585.52" data-rw-transcript-version="2">
 above.
 </span>
</p>
<p>
 <span data-rw-start="587" data-rw-transcript-version="2">
 No LLM is ever going to prefix your URL
 </span>
 <span data-rw-start="590" data-rw-transcript-version="2">
 with awesome. So, that's kind of where
 </span>
 <span data-rw-start="592.08" data-rw-transcript-version="2">
 your content or your company-specific,
 </span>
 <span data-rw-start="594.48" data-rw-transcript-version="2">
 your team-specific things come in, and
 </span>
 <span data-rw-start="596.6" data-rw-transcript-version="2">
 that's why you still write those tests
 </span>
 <span data-rw-start="598.88" data-rw-transcript-version="2">
 to see if this still works. Now, maybe
 </span>
 <span data-rw-start="601.72" data-rw-transcript-version="2">
 Gemini kind of reacts differently than
 </span>
 <span data-rw-start="605.4" data-rw-transcript-version="2">
 Copilot or something, and in your
 </span>
 <span data-rw-start="606.8" data-rw-transcript-version="2">
 company, you need to make it more, you
 </span>
 <span data-rw-start="608.76" data-rw-transcript-version="2">
 know, switchable of context. With this,
 </span>
 <span data-rw-start="611.72" data-rw-transcript-version="2">
 you run the tests, and you can actually
 </span>
 <span data-rw-start="613.36" data-rw-transcript-version="2">
 tell.
 </span>
 <span data-rw-start="614.36" data-rw-transcript-version="2">
 That's the difference.
 </span>
 <span data-rw-start="616.52" data-rw-transcript-version="2">
 And then you can make like whole suites,
 </span>
 <span data-rw-start="618.12" data-rw-transcript-version="2">
 and I would compare that almost to unit
 </span>
 <span data-rw-start="620" data-rw-transcript-version="2">
 tests. I have a bunch of these tests,
 </span>
 <span data-rw-start="621.92" data-rw-transcript-version="2">
 and they tell me whether that's
 </span>
 <span data-rw-start="623.52" data-rw-transcript-version="2">
 actually, you know, good code, the code
 </span>
 <span data-rw-start="625.84" data-rw-transcript-version="2">
 is following the rules, and everything's
 </span>
 <span data-rw-start="627.88" data-rw-transcript-version="2">
 fine. In this case, it's even kind of
 </span>
 <span data-rw-start="630.08" data-rw-transcript-version="2">
 infrastructure as code. It doesn't need
 </span>
 <span data-rw-start="631.72" data-rw-transcript-version="2">
 to be code only. It could be various
 </span>
 <span data-rw-start="633.72" data-rw-transcript-version="2">
 things. Could be config files as well.
 </span>
</p>
<p>
 <span data-rw-start="635.92" data-rw-transcript-version="2">
 And I just have It's hard to read, but a
 </span>
 <span data-rw-start="637.88" data-rw-transcript-version="2">
 bunch of kind of criteria that I just
 </span>
 <span data-rw-start="640.6" data-rw-transcript-version="2">
 run every time to do that.
 </span>
</p>
<p>
 <span data-rw-start="644.68" data-rw-transcript-version="2">
 But,
 </span>
 <span data-rw-start="645.92" data-rw-transcript-version="2">
 if you want to test,
 </span>
 <span data-rw-start="647.92" data-rw-transcript-version="2">
 you know, whether an endpoint has
 </span>
 <span data-rw-start="649.76" data-rw-transcript-version="2">
 {slash} awesome
 </span>
 <span data-rw-start="651.52" data-rw-transcript-version="2">
 {slash} user,
 </span>
 <span data-rw-start="653.48" data-rw-transcript-version="2">
 there's a real test that we want to run,
 </span>
 <span data-rw-start="655.48" data-rw-transcript-version="2">
 which is
 </span>
 <span data-rw-start="656.68" data-rw-transcript-version="2">
 I want to test the endpoint. I just
 </span>
 <span data-rw-start="658.88" data-rw-transcript-version="2">
 don't want only to check the code. I
 </span>
 <span data-rw-start="661.92" data-rw-transcript-version="2">
 want to have it running. So, when you
 </span>
 <span data-rw-start="664.92" data-rw-transcript-version="2">
 give the judge a tool, and the judge
 </span>
 <span data-rw-start="667.6" data-rw-transcript-version="2">
 becomes an agent, and it can do things
 </span>
 <span data-rw-start="670.6" data-rw-transcript-version="2">
 in a sandbox and execute stuff.
 </span>
</p>
<p>
 <span data-rw-start="674.36" data-rw-transcript-version="2">
 It can actually do the do the curl. So,
 </span>
 <span data-rw-start="676.12" data-rw-transcript-version="2">
 you can bind
 </span>
 <span data-rw-start="677.88" data-rw-transcript-version="2">
 LLM as a judge with kind of some
 </span>
 <span data-rw-start="680.4" data-rw-transcript-version="2">
 tooling, and then you can have multitude
 </span>
 <span data-rw-start="682.96" data-rw-transcript-version="2">
 of tests actually, you know, in this
 </span>
 <span data-rw-start="685.16" data-rw-transcript-version="2">
 case,
 </span>
 <span data-rw-start="686.24" data-rw-transcript-version="2">
 it kind of ends up being an end-to-end
 </span>
 <span data-rw-start="688.04" data-rw-transcript-version="2">
 test, right? Because it's not just
 </span>
 <span data-rw-start="689.6" data-rw-transcript-version="2">
 looking at the file, it's actually
 </span>
 <span data-rw-start="691.56" data-rw-transcript-version="2">
 Running the piece with everything that
 </span>
 <span data-rw-start="694.04" data-rw-transcript-version="2">
 it's supposed to do.
 </span>
</p>
<p>
 <span data-rw-start="696.48" data-rw-transcript-version="2">
 And then I can do this, like, given a
 </span>
 <span data-rw-start="698.72" data-rw-transcript-version="2">
 certain commit in my repo,
 </span>
 <span data-rw-start="701.56" data-rw-transcript-version="2">
 I want to run this scenario,
 </span>
 <span data-rw-start="703.92" data-rw-transcript-version="2">
 given this piece of context,
 </span>
 <span data-rw-start="706.32" data-rw-transcript-version="2">
 did it make a difference? Yes or no? So,
 </span>
 <span data-rw-start="708.04" data-rw-transcript-version="2">
 you're kind of like building this up
 </span>
 <span data-rw-start="709.52" data-rw-transcript-version="2">
 while you're committing context also
 </span>
 <span data-rw-start="711.8" data-rw-transcript-version="2">
 within your repo.
 </span>
</p>
<p>
 <span data-rw-start="715.04" data-rw-transcript-version="2">
 And because we now have tests, and it
 </span>
 <span data-rw-start="717.4" data-rw-transcript-version="2">
 gives us feedback whether it's working
 </span>
 <span data-rw-start="719.2" data-rw-transcript-version="2">
 yes or no, or what it's missing, we can
 </span>
 <span data-rw-start="722.08" data-rw-transcript-version="2">
 optimize context. So, that's kind of
 </span>
 <span data-rw-start="724.839" data-rw-transcript-version="2">
 the, you know, you, we can put that in a
 </span>
 <span data-rw-start="726.88" data-rw-transcript-version="2">
 code action or something that says like,
 </span>
 <span data-rw-start="728.68" data-rw-transcript-version="2">
 "Okay, fix this context. Improve this
 </span>
 <span data-rw-start="731.56" data-rw-transcript-version="2">
 context." With all the feedback the LLM
 </span>
 <span data-rw-start="734.48" data-rw-transcript-version="2">
 has given us
 </span>
 <span data-rw-start="736.04" data-rw-transcript-version="2">
 to improve that.
 </span>
</p>
<p>
 <span data-rw-start="737.56" data-rw-transcript-version="2">
 So, you know, again, coding
 </span>
 <span data-rw-start="740.32" data-rw-transcript-version="2">
 improvements, but we start thinking
 </span>
 <span data-rw-start="742.88" data-rw-transcript-version="2">
 more in testing that piece as well.
 </span>
 <span data-rw-start="746.72" data-rw-transcript-version="2">
 Now, one of the first reactions is, once
 </span>
 <span data-rw-start="748.8" data-rw-transcript-version="2">
 you have tests and optimizations,
 </span>
 <span data-rw-start="751.32" data-rw-transcript-version="2">
 Can we run this in a CI/CD system
 </span>
 <span data-rw-start="753.72" data-rw-transcript-version="2">
 ? Because
 </span>
 <span data-rw-start="754.72" data-rw-transcript-version="2">
 that's perfect, right? That's where we
 </span>
 <span data-rw-start="756.64" data-rw-transcript-version="2">
 run all our tests and our test
 </span>
 <span data-rw-start="758.48" data-rw-transcript-version="2">
 suites and do that.
 </span>
</p>
<p>
 <span data-rw-start="760.4" data-rw-transcript-version="2">
 Now, there's a little bit of a weird
 </span>
 <span data-rw-start="761.88" data-rw-transcript-version="2">
 thing.
 </span>
 <span data-rw-start="763.32" data-rw-transcript-version="2">
 If you run evals,
 </span>
 <span data-rw-start="766.44" data-rw-transcript-version="2">
 you run it once, you run it another
 </span>
 <span data-rw-start="768.28" data-rw-transcript-version="2">
 time, it might not give the same result.
 </span>
</p>
<p>
 <span data-rw-start="770.44" data-rw-transcript-version="2">
 Remember, undeterministic things.
 </span>
 <span data-rw-start="774" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="775.44" data-rw-transcript-version="2">
 you cannot
 </span>
 <span data-rw-start="776.72" data-rw-transcript-version="2">
 say, "Well, run it once, and then if it
 </span>
 <span data-rw-start="779.28" data-rw-transcript-version="2">
 passes or not." You're going to be in
 </span>
 <span data-rw-start="780.839" data-rw-transcript-version="2">
 for a treat because it's like, "Ah, I, I
 </span>
 <span data-rw-start="782.92" data-rw-transcript-version="2">
 can't debug that." So,
 </span>
 <span data-rw-start="785.32" data-rw-transcript-version="2">
 think about this like you run it five
 </span>
 <span data-rw-start="787.36" data-rw-transcript-version="2">
 times,
 </span>
 <span data-rw-start="788.92" data-rw-transcript-version="2">
 and out of five, how many times does it
 </span>
 <span data-rw-start="791.16" data-rw-transcript-version="2">
 succeed?
 </span>
</p>
<p>
 <span data-rw-start="792.32" data-rw-transcript-version="2">
 And, you know, maybe
 </span>
 <span data-rw-start="794.56" data-rw-transcript-version="2">
 in several cases it hits 100% all the
 </span>
 <span data-rw-start="797.04" data-rw-transcript-version="2">
 time, which is great.
 </span>
 <span data-rw-start="798.56" data-rw-transcript-version="2">
 But, in others not. And depending on how
 </span>
 <span data-rw-start="800.56" data-rw-transcript-version="2">
 You change your context,
 </span>
 <span data-rw-start="802.48" data-rw-transcript-version="2">
 it will influence which test actually
 </span>
 <span data-rw-start="804.4" data-rw-transcript-version="2">
 work or not.
 </span>
</p>
<p>
 <span data-rw-start="806.08" data-rw-transcript-version="2">
 I find it personally helpful to think
 </span>
 <span data-rw-start="808" data-rw-transcript-version="2">
 about this as error budgets.
 </span>
 <span data-rw-start="810.96" data-rw-transcript-version="2">
 I give a set of tests an error budget
 </span>
 <span data-rw-start="813.56" data-rw-transcript-version="2">
 that I really care about, so it is
 </span>
 <span data-rw-start="815.88" data-rw-transcript-version="2">
 only allowed like, you know,
 </span>
 <span data-rw-start="817.72" data-rw-transcript-version="2">
 to fail minimally, and other pieces are
 </span>
 <span data-rw-start="820.36" data-rw-transcript-version="2">
 okay. So, that's how you have to think
 </span>
 <span data-rw-start="822.76" data-rw-transcript-version="2">
 about testing context. You cannot do
 </span>
 <span data-rw-start="825.88" data-rw-transcript-version="2">
 like exact testing all the time. It’s a
 </span>
 <span data-rw-start="828.08" data-rw-transcript-version="2">
 different way that this works.
 </span>
</p>
<p>
 <span data-rw-start="832.52" data-rw-transcript-version="2">
 All right. So,
 </span>
 <span data-rw-start="834.16" data-rw-transcript-version="2">
 generate. Hopefully, you understand what
 </span>
 <span data-rw-start="836.52" data-rw-transcript-version="2">
 the testing could do for you.
 </span>
 <span data-rw-start="839.28" data-rw-transcript-version="2">
 And distribute.
 </span>
 <span data-rw-start="840.56" data-rw-transcript-version="2">
 Maybe that's also something you already
 </span>
 <span data-rw-start="842.36" data-rw-transcript-version="2">
 did.
 </span>
</p>
<p>
 <span data-rw-start="843.52" data-rw-transcript-version="2">
 If you maybe have checked context into
 </span>
 <span data-rw-start="846.12" data-rw-transcript-version="2">
 your repo, right? Which is great, you
 </span>
 <span data-rw-start="848.52" data-rw-transcript-version="2">
 know, all of a sudden it becomes
 </span>
 <span data-rw-start="849.96" data-rw-transcript-version="2">
 available, your colleague checks it out.
 </span>
 <span data-rw-start="852.44" data-rw-transcript-version="2">
 Uh, zero friction, I can push, I can
 </span>
 <span data-rw-start="854.4" data-rw-transcript-version="2">
 share.
 </span>
</p>
<p>
 <span data-rw-start="855.76" data-rw-transcript-version="2">
 But,
 </span>
 <span data-rw-start="857.52" data-rw-transcript-version="2">
 we have another mechanism for doing
 </span>
 <span data-rw-start="859.64" data-rw-transcript-version="2">
 things. Think of this like, imagine you
 </span>
 <span data-rw-start="861.92" data-rw-transcript-version="2">
 have a reusable context
 </span>
 <span data-rw-start="864.2" data-rw-transcript-version="2">
 that you want to reuse across multiple
 </span>
 <span data-rw-start="867.04" data-rw-transcript-version="2">
 projects, across multiple teams. We had
 </span>
 <span data-rw-start="870.32" data-rw-transcript-version="2">
 the concept of a library.
 </span>
 <span data-rw-start="872.48" data-rw-transcript-version="2">
 So, what if we package
 </span>
 <span data-rw-start="875.52" data-rw-transcript-version="2">
 kind of pieces of context, and then we
 </span>
 <span data-rw-start="878.52" data-rw-transcript-version="2">
 are able to install pieces of context
 </span>
 <span data-rw-start="880.959" data-rw-transcript-version="2">
 that we need for this project.
 </span>
 <span data-rw-start="883.32" data-rw-transcript-version="2">
 Guidelines, front end. It doesn't matter
 </span>
 <span data-rw-start="886.959" data-rw-transcript-version="2">
 for that. And then if we take it that up
 </span>
 <span data-rw-start="888.839" data-rw-transcript-version="2">
 a notch, how to discover what packages
 </span>
 <span data-rw-start="892.2" data-rw-transcript-version="2">
 exists?
 </span>
 <span data-rw-start="893.44" data-rw-transcript-version="2">
 That's a registry.
 </span>
 <span data-rw-start="895.12" data-rw-transcript-version="2">
 Right?
 </span>
 <span data-rw-start="895.92" data-rw-transcript-version="2">
 Now,
 </span>
 <span data-rw-start="896.959" data-rw-transcript-version="2">
 in that way, it's no surprise that
 </span>
 <span data-rw-start="898.92" data-rw-transcript-version="2">
 you'll see things like skills and kind
 </span>
 <span data-rw-start="901.48" data-rw-transcript-version="2">
 of the Tesla registry in the
 </span>
 <span data-rw-start="903.12" data-rw-transcript-version="2">
 marketplace,
 </span>
 <span data-rw-start="905.16" data-rw-transcript-version="2">
 where you can find a multitude of
 </span>
 <span data-rw-start="906.6" data-rw-transcript-version="2">
 skills. Now, the reality is
 </span>
 <span data-rw-start="909.48" data-rw-transcript-version="2">
 99.9,
 </span>
 <span data-rw-start="911" data-rw-transcript-version="2">
 And I mean that in a very sincere way,
 </span>
 <span data-rw-start="913.8" data-rw-transcript-version="2">
 the skills are crap.
 </span>
</p>
<p>
 <span data-rw-start="916.959" data-rw-transcript-version="2">
 But, it's good to learn from others to
 </span>
 <span data-rw-start="919.64" data-rw-transcript-version="2">
 see what they're doing.
 </span>
 <span data-rw-start="921.8" data-rw-transcript-version="2">
 But, hardly any of them, if you run kind of
 </span>
 <span data-rw-start="923.92" data-rw-transcript-version="2">
 any set of evals on there, is actually
 </span>
 <span data-rw-start="927" data-rw-transcript-version="2">
 up to a quality standard.
 </span>
 <span data-rw-start="929.6" data-rw-transcript-version="2">
 Now,
 </span>
 <span data-rw-start="930.52" data-rw-transcript-version="2">
 that will likely improve. But, there's
 </span>
 <span data-rw-start="932.56" data-rw-transcript-version="2">
 also a tendency that
 </span>
 <span data-rw-start="934.72" data-rw-transcript-version="2">
 a lot of the skills and pieces,
 </span>
 <span data-rw-start="937.36" data-rw-transcript-version="2">
 people actually want to put that in
 </span>
 <span data-rw-start="939.48" data-rw-transcript-version="2">
 their own registry.
 </span>
</p>
<p>
 <span data-rw-start="941.8" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="943.48" data-rw-transcript-version="2">
 I'll come to that later again. But,
 </span>
 <span data-rw-start="946.2" data-rw-transcript-version="2">
 so you start seeing the gist, a skill
 </span>
 <span data-rw-start="949.6" data-rw-transcript-version="2">
 not only contains context, it can
 </span>
 <span data-rw-start="951.76" data-rw-transcript-version="2">
 contain scripts, it can contain
 </span>
 <span data-rw-start="953.44" data-rw-transcript-version="2">
 documents, contain bunch of things. So,
 </span>
 <span data-rw-start="956.28" data-rw-transcript-version="2">
 is this kind of the package format?
 </span>
</p>
<p>
 <span data-rw-start="958.4" data-rw-transcript-version="2">
 Probably, you know, plugins
 </span>
 <span data-rw-start="961.4" data-rw-transcript-version="2">
 could now also contain MCP, but you see
 </span>
 <span data-rw-start="964.2" data-rw-transcript-version="2">
 there's like a standard coming in.
 </span>
 <span data-rw-start="965.76" data-rw-transcript-version="2">
 Skills all of a sudden, when that came
 </span>
 <span data-rw-start="967.32" data-rw-transcript-version="2">
 out, all the coding agents said, "We'
 </span>
 <span data-rw-start="969.48" data-rw-transcript-version="2">
 Supporting this as almost like a package format for people to distribute their context on.
 </span>
</p>
<p>
 <span data-rw-start="971.28" data-rw-transcript-version="2">
 And then when I have one piece of
 </span>
 <span data-rw-start="973.32" data-rw-transcript-version="2">
 context,
 </span>
 <span data-rw-start="980.079" data-rw-transcript-version="2">
 I have dependencies. And I'm sorry, but
 </span>
 <span data-rw-start="983.079" data-rw-transcript-version="2">
 also with context, we're going to have
 </span>
 <span data-rw-start="984.36" data-rw-transcript-version="2">
 dependency hell.
 </span>
 <span data-rw-start="985.88" data-rw-transcript-version="2">
 Right? I, I'm, I'm going to download
 </span>
 <span data-rw-start="987.88" data-rw-transcript-version="2">
 this for front end, and maybe it's
 </span>
 <span data-rw-start="989.8" data-rw-transcript-version="2">
 conflicting what is in the React context
 </span>
 <span data-rw-start="992.24" data-rw-transcript-version="2">
 package. And so, you start having to
 </span>
 <span data-rw-start="994.959" data-rw-transcript-version="2">
 deal with that as well. So, you start
 </span>
 <span data-rw-start="997.36" data-rw-transcript-version="2">
 seeing also, uh, packages that's, uh, mirror
 </span>
 <span data-rw-start="1001.4" data-rw-transcript-version="2">
 your library versions, your code ver
 </span>
 <span data-rw-start="1003.6" data-rw-transcript-version="2">
 like your context versions, and kind of
 </span>
 <span data-rw-start="1005.48" data-rw-transcript-version="2">
 pull that in as well.
 </span>
</p>
<p>
 <span data-rw-start="1008.88" data-rw-transcript-version="2">
 And of course, when we have packages and
 </span>
 <span data-rw-start="1010.24" data-rw-transcript-version="2">
 people are publishing things in
 </span>
 <span data-rw-start="1011.36" data-rw-transcript-version="2">
 registry, we need security.
 </span>
 <span data-rw-start="1013.64" data-rw-transcript-version="2">
 Right? Open claw. Thank you for that.
 </span>
</p>
<p>
 <span data-rw-start="1015.839" data-rw-transcript-version="2">
 Like everybody, all of a sudden, became
 </span>
 <span data-rw-start="1017.28" data-rw-transcript-version="2">
 aware that we need more secure
 </span>
 <span data-rw-start="1019.4" data-rw-transcript-version="2">
 things because we are able to run things
 </span>
 <span data-rw-start="1021.76" data-rw-transcript-version="2">
 on our laptop that are not, and coming.
 </span>
</p>
<p>
 <span data-rw-start="1024.6" data-rw-transcript-version="2">
 From strangers, right? So,
 </span>
 <span data-rw-start="1027.36" data-rw-transcript-version="2">
 Snyk has a way of scanning context,
 </span>
 <span data-rw-start="1030.079" data-rw-transcript-version="2">
 right? It's doing some credential
 </span>
 <span data-rw-start="1032.12" data-rw-transcript-version="2">
 handling. It's uh exposing some
 </span>
 <span data-rw-start="1034.28" data-rw-transcript-version="2">
 third-party pieces. So, you start seeing
 </span>
 <span data-rw-start="1036.92" data-rw-transcript-version="2">
 the scanners on the context as well.
 </span>
 <span data-rw-start="1042.32" data-rw-transcript-version="2">
 And then when you think about security,
 </span>
 <span data-rw-start="1044.64" data-rw-transcript-version="2">
 who actually built the skill? How was it
 </span>
 <span data-rw-start="1047.52" data-rw-transcript-version="2">
 built? With what model was this built?
 </span>
 <span data-rw-start="1050.48" data-rw-transcript-version="2">
 So, all kind of capturing what we
 </span>
 <span data-rw-start="1052.8" data-rw-transcript-version="2">
 learned in maybe with packaging, like
 </span>
 <span data-rw-start="1055.44" data-rw-transcript-version="2">
 the SBOM, is kind of the AI SBOM, like
 </span>
 <span data-rw-start="1058.6" data-rw-transcript-version="2">
 the packaged of context that we're
 </span>
 <span data-rw-start="1060.44" data-rw-transcript-version="2">
 putting in.
 </span>
 <span data-rw-start="1062.64" data-rw-transcript-version="2">
 So, you've seen
 </span>
 <span data-rw-start="1064.2" data-rw-transcript-version="2">
 still on the path, right? You generate,
 </span>
 <span data-rw-start="1066.52" data-rw-transcript-version="2">
 evaluate, distribute.
 </span>
 <span data-rw-start="1068.679" data-rw-transcript-version="2">
 Let's move into observe.
 </span>
 <span data-rw-start="1074.08" data-rw-transcript-version="2">
 When you
 </span>
 <span data-rw-start="1075.679" data-rw-transcript-version="2">
 are making libraries of skills and
 </span>
 <span data-rw-start="1078.4" data-rw-transcript-version="2">
 context for others,
 </span>
 <span data-rw-start="1080.28" data-rw-transcript-version="2">
 and I don't mean copy and paste this
 </span>
 <span data-rw-start="1081.88" data-rw-transcript-version="2">
 over Slack or something.
 </span>
 <span data-rw-start="1083.96" data-rw-transcript-version="2">
 But, when you actually want to maintain
 </span>
 <span data-rw-start="1085.48" data-rw-transcript-version="2">
 this as something somebody else can use,
 </span>
 <span data-rw-start="1087.56" data-rw-transcript-version="2">
 Similar to a library,
 </span>
 <span data-rw-start="1089.56" data-rw-transcript-version="2">
 um, when they start using that, how do
 </span>
 <span data-rw-start="1092.56" data-rw-transcript-version="2">
 you get feedback whether that still
 </span>
 <span data-rw-start="1094.48" data-rw-transcript-version="2">
 works?
 </span>
</p>
<p>
 <span data-rw-start="1095.72" data-rw-transcript-version="2">
 Now, a great place to get feedback is
 </span>
 <span data-rw-start="1097.72" data-rw-transcript-version="2">
 actually by looking at the agent logs.
 </span>
 <span data-rw-start="1101.08" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="1105" data-rw-transcript-version="2">
 imagine developer one
 </span>
 <span data-rw-start="1106.96" data-rw-transcript-version="2">
 coding on the project, and the agent is
 </span>
 <span data-rw-start="1109.84" data-rw-transcript-version="2">
 not doing what they want.
 </span>
 <span data-rw-start="1113.04" data-rw-transcript-version="2">
 They could put this into their context,
 </span>
 <span data-rw-start="1115.28" data-rw-transcript-version="2">
 which is great, right? Okay, let, let me
 </span>
 <span data-rw-start="1117.64" data-rw-transcript-version="2">
 do the TDD almost like, you know, I hit
 </span>
 <span data-rw-start="1119.919" data-rw-transcript-version="2">
 a problem. It's not TDD, but you get my
 </span>
 <span data-rw-start="1122.36" data-rw-transcript-version="2">
 gist.
 </span>
 <span data-rw-start="1123.28" data-rw-transcript-version="2">
 Um
 </span>
 <span data-rw-start="1124.159" data-rw-transcript-version="2">
 or
 </span>
 <span data-rw-start="1125.24" data-rw-transcript-version="2">
 what if we, at a team or an organization
 </span>
 <span data-rw-start="1128.08" data-rw-transcript-version="2">
 scale, would look at the logs every time
 </span>
 <span data-rw-start="1130.84" data-rw-transcript-version="2">
 an agent said, "We're missing this
 </span>
 <span data-rw-start="1132.52" data-rw-transcript-version="2">
 piece."
 </span>
 <span data-rw-start="1134.04" data-rw-transcript-version="2">
 And we surface that and say,
 </span>
 <span data-rw-start="1136.12" data-rw-transcript-version="2">
 "If everybody's missing this piece, we
 </span>
 <span data-rw-start="1138.32" data-rw-transcript-version="2">
 should create context for this."
 </span>
 <span data-rw-start="1140.84" data-rw-transcript-version="2">
 And then we distribute the context to
 </span>
 <span data-rw-start="1142.679" data-rw-transcript-version="2">
 Everybody, and all of a sudden, the
 </span>
 <span data-rw-start="1144.4" data-rw-transcript-version="2">
 impact of improvement is for everybody.
 </span>
</p>
<p>
 <span data-rw-start="1147.64" data-rw-transcript-version="2">
 Luckily, like the agent and D, there's
 </span>
 <span data-rw-start="1150.28" data-rw-transcript-version="2">
 now our standards becoming for logs. So,
 </span>
 <span data-rw-start="1152.919" data-rw-transcript-version="2">
 we can read from logs, and that's part
 </span>
 <span data-rw-start="1155.76" data-rw-transcript-version="2">
 of our feedback channel to see if the
 </span>
 <span data-rw-start="1158.159" data-rw-transcript-version="2">
 agent is actually using or missing some
 </span>
 <span data-rw-start="1161.6" data-rw-transcript-version="2">
 of the context.
 </span>
</p>
<p>
 <span data-rw-start="1164.72" data-rw-transcript-version="2">
 Any feedback you get on a PR that's not
 </span>
 <span data-rw-start="1167.52" data-rw-transcript-version="2">
 complete, that's feedback on your
 </span>
 <span data-rw-start="1169.44" data-rw-transcript-version="2">
 context because
 </span>
 <span data-rw-start="1171.04" data-rw-transcript-version="2">
 that PR was created with certain pieces
 </span>
 <span data-rw-start="1172.919" data-rw-transcript-version="2">
 of context. If you say this is not
 </span>
 <span data-rw-start="1174.84" data-rw-transcript-version="2">
 correct, you can kind of keep arguing on
 </span>
 <span data-rw-start="1177.32" data-rw-transcript-version="2">
 the PR, or you can just say, "Let's
 </span>
 <span data-rw-start="1179.48" data-rw-transcript-version="2">
 improve the context." So, the next
 </span>
 <span data-rw-start="1180.8" data-rw-transcript-version="2">
 iteration actually
 </span>
 <span data-rw-start="1182.76" data-rw-transcript-version="2">
 improves, uh, and you don't hit that same
 </span>
 <span data-rw-start="1184.96" data-rw-transcript-version="2">
 problem again.
 </span>
</p>
<p>
 <span data-rw-start="1188" data-rw-transcript-version="2">
 What about
 </span>
 <span data-rw-start="1189.8" data-rw-transcript-version="2">
 running code in production that was
 </span>
 <span data-rw-start="1191.64" data-rw-transcript-version="2">
 generated from context?
 </span>
 <span data-rw-start="1194.56" data-rw-transcript-version="2">
 And that's not correct because
 </span>
 <span data-rw-start="1196.68" data-rw-transcript-version="2">
 yes, we do our PR reviews and we say
 </span>
 <span data-rw-start="1198.68" data-rw-transcript-version="2">
 thumbs up, thumbs down, and we give the
 </span>
 <span data-rw-start="1200.32" data-rw-transcript-version="2">
 Feedback, but the actual feedback is
 </span>
 <span data-rw-start="1202.36" data-rw-transcript-version="2">
 also in production when it's running.
 </span>
</p>
<p>
 <span data-rw-start="1204.64" data-rw-transcript-version="2">
 So, this is a tool that actually
 </span>
 <span data-rw-start="1206.28" data-rw-transcript-version="2">
 instruments your code,
 </span>
 <span data-rw-start="1208.8" data-rw-transcript-version="2">
 pushes it out, it's almost like a
 </span>
 <span data-rw-start="1210.28" data-rw-transcript-version="2">
 wrapper, it pushes it out to production.
 </span>
 <span data-rw-start="1212.64" data-rw-transcript-version="2">
 When it fails, it says, "These pieces of
 </span>
 <span data-rw-start="1214.68" data-rw-transcript-version="2">
 code were changed and were failing.
 </span>
 <span data-rw-start="1217.92" data-rw-transcript-version="2">
 Hey, in this case, input, output,
 </span>
 <span data-rw-start="1220.76" data-rw-transcript-version="2">
 it did something wrong.
 </span>
</p>
<p>
 <span data-rw-start="1222.96" data-rw-transcript-version="2">
 Can we create a test case for this? So,
 </span>
 <span data-rw-start="1225.56" data-rw-transcript-version="2">
 the next time we don't hit this again in
 </span>
 <span data-rw-start="1227.44" data-rw-transcript-version="2">
 production?"
 </span>
 <span data-rw-start="1229" data-rw-transcript-version="2">
 Feedback loop.
 </span>
 <span data-rw-start="1231.88" data-rw-transcript-version="2">
 Now, these are all kind of pretty
 </span>
 <span data-rw-start="1233.48" data-rw-transcript-version="2">
 trivial, like missing pieces of context
 </span>
 <span data-rw-start="1235.92" data-rw-transcript-version="2">
 or improvements.
 </span>
</p>
<p>
 <span data-rw-start="1238.08" data-rw-transcript-version="2">
 But, if you run agents and the
 </span>
 <span data-rw-start="1241.08" data-rw-transcript-version="2">
 equivalent of scanning, maybe, you know,
 </span>
 <span data-rw-start="1243.24" data-rw-transcript-version="2">
 in the CICD is
 </span>
 <span data-rw-start="1245.36" data-rw-transcript-version="2">
 you need to make sure when it's running
 </span>
 <span data-rw-start="1247" data-rw-transcript-version="2">
 in production,
 </span>
 <span data-rw-start="1249.52" data-rw-transcript-version="2">
 it is not doing strange things. So, we
 </span>
 <span data-rw-start="1251.68" data-rw-transcript-version="2">
 need kind of a way of looking at that.
 </span>
 <span data-rw-start="1253.64" data-rw-transcript-version="2">
 Now,
 </span>
 <span data-rw-start="1255.08" data-rw-transcript-version="2">
 I've been toying myself with uh
 </span>
 <span data-rw-start="1257.12" data-rw-transcript-version="2">
 you know, sandboxing agents, and it is very resourceful
 </span>
 <span data-rw-start="1259.52" data-rw-transcript-version="2">
 at finding things.
 </span>
</p>
<p>
 <span data-rw-start="1261.56" data-rw-transcript-version="2">
 I like, okay, you know, run this thing,
 </span>
 <span data-rw-start="1263.68" data-rw-transcript-version="2">
 try to figure out like anything useful
 </span>
 <span data-rw-start="1266.88" data-rw-transcript-version="2">
 to get break out of the system.
 </span>
 <span data-rw-start="1268.96" data-rw-transcript-version="2">
 And okay, it uses my environment
 </span>
 <span data-rw-start="1271.12" data-rw-transcript-version="2">
 variables. Okay, stupid. Let me
 </span>
 <span data-rw-start="1273.6" data-rw-transcript-version="2">
 remove the secret. Let me look at your
 </span>
 <span data-rw-start="1275.92" data-rw-transcript-version="2">
 memory files. So, you have to really
 </span>
 <span data-rw-start="1278.08" data-rw-transcript-version="2">
 make sure that like whatever it’s
 </span>
 <span data-rw-start="1281" data-rw-transcript-version="2">
 doing, you can have a way of tracing
 </span>
 <span data-rw-start="1282.84" data-rw-transcript-version="2">
 this as well.
 </span>
</p>
<p>
 <span data-rw-start="1288.08" data-rw-transcript-version="2">
 And uh, apologize again for kind of the
 </span>
 <span data-rw-start="1290.44" data-rw-transcript-version="2">
 slide, but
 </span>
 <span data-rw-start="1293.4" data-rw-transcript-version="2">
 the gist is
 </span>
 <span data-rw-start="1294.96" data-rw-transcript-version="2">
 we can have a sandbox where the agent
 </span>
 <span data-rw-start="1296.92" data-rw-transcript-version="2">
 runs inside.
 </span>
 <span data-rw-start="1299.52" data-rw-transcript-version="2">
 But, your code agent by default without
 </span>
 <span data-rw-start="1303.36" data-rw-transcript-version="2">
 any restrictions loads your agent.md,
 </span>
 <span data-rw-start="1306.84" data-rw-transcript-version="2">
 you load your skill.md.
 </span>
 <span data-rw-start="1309.76" data-rw-transcript-version="2">
 Like, nothing is blocking that.
 </span>
 <span data-rw-start="1312.68" data-rw-transcript-version="2">
 So, if you download this,
 </span>
 <span data-rw-start="1314.88" data-rw-transcript-version="2">
 immediately it’s loaded.
 </span>
</p>
<p>
 <span data-rw-start="1317.52" data-rw-transcript-version="2">
 So, you can't filter that with
 </span>
 <span data-rw-start="1319.84" data-rw-transcript-version="2">
 sandboxes. You need to have another way.
 </span>
 <span data-rw-start="1322.48" data-rw-transcript-version="2">
 I call that a context filter. Think of
 </span>
 <span data-rw-start="1324.36" data-rw-transcript-version="2">
 this as a web application firewall that
 </span>
 <span data-rw-start="1326.4" data-rw-transcript-version="2">
 just filters out any patterns or prompt
 </span>
 <span data-rw-start="1328.52" data-rw-transcript-version="2">
 injections or stuff that is coming in
 </span>
 <span data-rw-start="1330.64" data-rw-transcript-version="2">
 directly in that piece.
 </span>
 <span data-rw-start="1333.76" data-rw-transcript-version="2">
 And if you take that, there's a lot of
 </span>
 <span data-rw-start="1335.08" data-rw-transcript-version="2">
 talk here as well on harness
 </span>
 <span data-rw-start="1336.48" data-rw-transcript-version="2">
 engineering. Harness engineering itself
 </span>
 <span data-rw-start="1338.52" data-rw-transcript-version="2">
 also has this kind of full
 </span>
 <span data-rw-start="1340.24" data-rw-transcript-version="2">
 observability, looking at logs, looking
 </span>
 <span data-rw-start="1342.56" data-rw-transcript-version="2">
 at traces, looking at feedback.
 </span>
 <span data-rw-start="1344.88" data-rw-transcript-version="2">
 So, it's kind of, you know, useful for
 </span>
 <span data-rw-start="1348" data-rw-transcript-version="2">
 training pieces, but as much useful for
 </span>
 <span data-rw-start="1350.44" data-rw-transcript-version="2">
 running your own pieces well.
 </span>
 <span data-rw-start="1353.4" data-rw-transcript-version="2">
 Those were the pieces for me today.
 </span>
 <span data-rw-start="1356.64" data-rw-transcript-version="2">
 I would say
 </span>
 <span data-rw-start="1358.52" data-rw-transcript-version="2">
 for a lot of people, there's like create
 </span>
 <span data-rw-start="1360.76" data-rw-transcript-version="2">
 context,
 </span>
 <span data-rw-start="1362.08" data-rw-transcript-version="2">
 test context. Think of this as your
 </span>
 <span data-rw-start="1363.92" data-rw-transcript-version="2">
 library authoring tool loop.
 </span>
</p>
<p>
 <span data-rw-start="1367.32" data-rw-transcript-version="2">
 And then when you push this into the
 </span>
 <span data-rw-start="1368.64" data-rw-transcript-version="2">
 enterprise, there's an organizational
 </span>
 <span data-rw-start="1370.76" data-rw-transcript-version="2">
 loop. Hey, I made a library, somebody
 </span>
 <span data-rw-start="1373.08" data-rw-transcript-version="2">
 Else is using it. I'm looking at
 </span>
 <span data-rw-start="1374.679" data-rw-transcript-version="2">
 whatever that's useful, whether that's
 </span>
 <span data-rw-start="1376.24" data-rw-transcript-version="2">
 still working, whether that's still
 </span>
 <span data-rw-start="1378" data-rw-transcript-version="2">
 working for all the other pieces. So,
 </span>
 <span data-rw-start="1380.2" data-rw-transcript-version="2">
 that's kind of like
 </span>
 <span data-rw-start="1381.92" data-rw-transcript-version="2">
 the kind of
 </span>
 <span data-rw-start="1384.32" data-rw-transcript-version="2">
 improvement, almost like sonar CICD model
 </span>
 <span data-rw-start="1387.36" data-rw-transcript-version="2">
 for context. And then
 </span>
 <span data-rw-start="1391.28" data-rw-transcript-version="2">
 you're currently probably doing a lot at
 </span>
 <span data-rw-start="1393" data-rw-transcript-version="2">
 the individual solo model, you're
 </span>
 <span data-rw-start="1394.88" data-rw-transcript-version="2">
 improving, you're honing, crafting your
 </span>
 <span data-rw-start="1397.52" data-rw-transcript-version="2">
 own kind of markdown. What if you start
 </span>
 <span data-rw-start="1399.72" data-rw-transcript-version="2">
 doing this more with your team? Make
 </span>
 <span data-rw-start="1401.76" data-rw-transcript-version="2">
 that a reflex. If it's missing, add some
 </span>
 <span data-rw-start="1404.12" data-rw-transcript-version="2">
 context. What if you put that out to a
 </span>
 <span data-rw-start="1406.6" data-rw-transcript-version="2">
 team of teams and you start having a
 </span>
 <span data-rw-start="1408.76" data-rw-transcript-version="2">
 flywheel, you know, if you fix it here,
 </span>
 <span data-rw-start="1411.56" data-rw-transcript-version="2">
 the other team can reuse it and, and
 </span>
 <span data-rw-start="1413.84" data-rw-transcript-version="2">
 that's kind of like,
 </span>
 <span data-rw-start="1415.08" data-rw-transcript-version="2">
 you know, scaling things out into the
 </span>
 <span data-rw-start="1416.92" data-rw-transcript-version="2">
 organization as well.
 </span>
</p>
<p>
 <span data-rw-start="1419.76" data-rw-transcript-version="2">
 And so, there's a lot of talk about LLMs
 </span>
 <span data-rw-start="1422.28" data-rw-transcript-version="2">
 and coding agents, and I all love them,
 </span>
 <span data-rw-start="1424.92" data-rw-transcript-version="2">
 but the way that I see it is they're
 </span>
 <span data-rw-start="1426.36" data-rw-transcript-version="2">
 just the engine.
 </span>
</p>
<p>
 <span data-rw-start="1428.08" data-rw-transcript-version="2">
 If you give the engine the wrong fuel,
 </span>
 <span data-rw-start="1430.48" data-rw-transcript-version="2">
 which is context,
 </span>
 <span data-rw-start="1432.76" data-rw-transcript-version="2">
 they're not going to perform. So, and
 </span>
 <span data-rw-start="1434.679" data-rw-transcript-version="2">
 you can't do anything on the LLMs, at
 </span>
 <span data-rw-start="1436.36" data-rw-transcript-version="2">
 least not me, right? I'm just using the
 </span>
 <span data-rw-start="1438.12" data-rw-transcript-version="2">
 coding agent, I'm using whatever they
 </span>
 <span data-rw-start="1440.08" data-rw-transcript-version="2">
 give me, but I can optimize my context
 </span>
 <span data-rw-start="1443.48" data-rw-transcript-version="2">
 uh,
 </span>
 <span data-rw-start="1444.08" data-rw-transcript-version="2">
 and that's, I think, the message, uh, doing
 </span>
 <span data-rw-start="1446.6" data-rw-transcript-version="2">
 this more in an engineered way than just
 </span>
 <span data-rw-start="1448.64" data-rw-transcript-version="2">
 copying and pasting things and hoping for
 </span>
 <span data-rw-start="1450.6" data-rw-transcript-version="2">
 the best in there.
 </span>
</p>
<p>
 <span data-rw-start="1453.4" data-rw-transcript-version="2">
 If you like this talk, connect on
 </span>
 <span data-rw-start="1455.52" data-rw-transcript-version="2">
 LinkedIn for the slides. Uh,
 </span>
 <span data-rw-start="1457.679" data-rw-transcript-version="2">
 give me some feedback, good and bad.
 </span>
</p>
<p>
 <span data-rw-start="1460.12" data-rw-transcript-version="2">
 If you want to try Tessel where we
 </span>
 <span data-rw-start="1462.44" data-rw-transcript-version="2">
 implement some of the pieces of this, uh,
 </span>
 <span data-rw-start="1464.8" data-rw-transcript-version="2">
 have a go.
 </span>
</p>
<p>
 <span data-rw-start="1466.16" data-rw-transcript-version="2">
 And if you're also interested in another
 </span>
 <span data-rw-start="1468" data-rw-transcript-version="2">
 conference, I know, you can never have
 </span>
 <span data-rw-start="1469.64" data-rw-transcript-version="2">
 enough conferences, uh, visit uh AI
 </span>
 <span data-rw-start="1472.32" data-rw-transcript-version="2">
 DevCon, which I curate the content for
 </span>
 <span data-rw-start="1475.64" data-rw-transcript-version="2">
 uh, here in London, first and second of
 </span>
 <span data-rw-start="1477.56" data-rw-transcript-version="2">
 June.
 </span>
 <span data-rw-start="1478.8" data-rw-transcript-version="2">
 And that's it. I can maybe take a few
 </span>
 <span data-rw-start="1480.76" data-rw-transcript-version="2">
 Questions.
 </span>
</p>
<p>
 <span data-rw-start="1482.282" data-rw-transcript-version="2">
 &gt;&gt; [Applause]
 </span>
 <span data-rw-start="1489.32" data-rw-transcript-version="2">
 &gt;&gt; Any questions?
 </span>
 <span data-rw-start="1492.96" data-rw-transcript-version="2">
 Sure.
 </span>
 <span data-rw-start="1494.16" data-rw-transcript-version="2">
 So, I was wondering if you have any
 </span>
 <span data-rw-start="1495.4" data-rw-transcript-version="2">
 thoughts about, like, more exotic forms of
 </span>
 <span data-rw-start="1497.92" data-rw-transcript-version="2">
 context, like I don't know, the
 </span>
 <span data-rw-start="1499.6" data-rw-transcript-version="2">
 traditional ones. So, for example, one
 </span>
 <span data-rw-start="1501.56" data-rw-transcript-version="2">
 of the things I'm working on is
 </span>
 <span data-rw-start="1502.56" data-rw-transcript-version="2">
 an automated system for, uh, scoping out
 </span>
 <span data-rw-start="1505" data-rw-transcript-version="2">
 architectural problems and like trying
 </span>
 <span data-rw-start="1506.72" data-rw-transcript-version="2">
 to create hard definitions for them, so
 </span>
 <span data-rw-start="1508.24" data-rw-transcript-version="2">
 that you can feed that to the agent and,
 </span>
 <span data-rw-start="1509.76" data-rw-transcript-version="2">
 you know, create actual
 </span>
 <span data-rw-start="1511.52" data-rw-transcript-version="2">
 objectives, uh, tests.
 </span>
</p>
<p>
 <span data-rw-start="1513.92" data-rw-transcript-version="2">
 Cool. Yeah.
 </span>
 <span data-rw-start="1514.88" data-rw-transcript-version="2">
 Microphones.
 </span>
 <span data-rw-start="1516.2" data-rw-transcript-version="2">
 Um, and one of the things I’ve been
 </span>
 <span data-rw-start="1517.44" data-rw-transcript-version="2">
 testing out is, like,
 </span>
 <span data-rw-start="1519.16" data-rw-transcript-version="2">
 the ability to create consistency as a
 </span>
 <span data-rw-start="1521.84" data-rw-transcript-version="2">
 form of context or as a form of eval.
 </span>
 <span data-rw-start="1523.96" data-rw-transcript-version="2">
 So, um, given this rough, like, very loose
 </span>
 <span data-rw-start="1526.56" data-rw-transcript-version="2">
 definition of what the plan is, if you
 </span>
 <span data-rw-start="1529.08" data-rw-transcript-version="2">
 try that agent,
 </span>
 <span data-rw-start="1530.52" data-rw-transcript-version="2">
 turn that into a really crisp
 </span>
 <span data-rw-start="1532.28" data-rw-transcript-version="2">
 Definition, and you just have that done
 </span>
 <span data-rw-start="1534.16" data-rw-transcript-version="2">
 in parallel, how often do you get the
 </span>
 <span data-rw-start="1536.2" data-rw-transcript-version="2">
 same crisp definition? And if they're
 </span>
 <span data-rw-start="1539.04" data-rw-transcript-version="2">
 all over the place, then the original
 </span>
 <span data-rw-start="1540.56" data-rw-transcript-version="2">
 definition was so poor, you need to like
 </span>
 <span data-rw-start="1541.96" data-rw-transcript-version="2">
 go back to base principles or to an
 </span>
 <span data-rw-start="1543.679" data-rw-transcript-version="2">
 architect. But, if they're all the same,
 </span>
 <span data-rw-start="1545.12" data-rw-transcript-version="2">
 then it's probably a pretty good
 </span>
 <span data-rw-start="1546.92" data-rw-transcript-version="2">
 definition and you can carry on with the
 </span>
 <span data-rw-start="1549.2" data-rw-transcript-version="2">
 downstream process. So, I think it's
 </span>
 <span data-rw-start="1551" data-rw-transcript-version="2">
 like besides just code and typical
 </span>
 <span data-rw-start="1552.44" data-rw-transcript-version="2">
 evals, um, any other sources of context
 </span>
 <span data-rw-start="1554.92" data-rw-transcript-version="2">
 for generating context that you think is
 </span>
 <span data-rw-start="1556.4" data-rw-transcript-version="2">
 useful?
 </span>
</p>
<p>
 <span data-rw-start="1557.76" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="1559.52" data-rw-transcript-version="2">
 I don't have maybe a specific answer
 </span>
 <span data-rw-start="1561.36" data-rw-transcript-version="2">
 to your like exotic case, but uh,
 </span>
 <span data-rw-start="1564.52" data-rw-transcript-version="2">
 I would say that maybe the piece that
 </span>
 <span data-rw-start="1566.04" data-rw-transcript-version="2">
 people are underestimating is that once
 </span>
 <span data-rw-start="1567.84" data-rw-transcript-version="2">
 you, you know, you thought you were going
 </span>
 <span data-rw-start="1569.92" data-rw-transcript-version="2">
 to save time by writing actually your
 </span>
 <span data-rw-start="1572.2" data-rw-transcript-version="2">
 context, uh, instead of all your code,
 </span>
 <span data-rw-start="1575.04" data-rw-transcript-version="2">
 but if you take this rigorously, you're
 </span>
 <span data-rw-start="1577.44" data-rw-transcript-version="2">
 going to spend time on writing the right
 </span>
 <span data-rw-start="1578.84" data-rw-transcript-version="2">
 evals. Right. And that's kind of like,
 </span>
 <span data-rw-start="1581.24" data-rw-transcript-version="2">
 You know, a lot of work to kind of
 </span>
 <span data-rw-start="1583.44" data-rw-transcript-version="2">
 because now you don't only have one
 </span>
 <span data-rw-start="1585.44" data-rw-transcript-version="2">
 prompt that you're trying to get right.
 </span>
</p>
<p>
 <span data-rw-start="1587.8" data-rw-transcript-version="2">
 It's like all the prompts of the evals
 </span>
 <span data-rw-start="1590.16" data-rw-transcript-version="2">
 and that, like, if people do almost like a
 </span>
 <span data-rw-start="1593.04" data-rw-transcript-version="2">
 like the more advanced people, they
 </span>
 <span data-rw-start="1595.12" data-rw-transcript-version="2">
 almost have their own process and they
 </span>
 <span data-rw-start="1597.6" data-rw-transcript-version="2">
 build their own process on top of
 </span>
 <span data-rw-start="1599.48" data-rw-transcript-version="2">
 like for building the right evals on
 </span>
 <span data-rw-start="1601.76" data-rw-transcript-version="2">
 your business case as well. So,
 </span>
 <span data-rw-start="1603.92" data-rw-transcript-version="2">
 yeah.
 </span>
</p>
<p>
 <span data-rw-start="1604.72" data-rw-transcript-version="2">
 Good question. Thank you. Any other
 </span>
 <span data-rw-start="1606.08" data-rw-transcript-version="2">
 questions?
 </span>
 <span data-rw-start="1609.72" data-rw-transcript-version="2">
 If not, I'll be around. Um,
 </span>
 <span data-rw-start="1612.08" data-rw-transcript-version="2">
 say hi. I'll also be at the
 </span>
 <span data-rw-start="1613.72" data-rw-transcript-version="2">
 Tessel booth. So, thank you very much
 </span>
 <span data-rw-start="1615.2" data-rw-transcript-version="2">
 and I'm going to make space for the next
 </span>
 <span data-rw-start="1616.6" data-rw-transcript-version="2">
 speaker. Thank you.
 </span>
</p>
<p>
 <span data-rw-start="1623.763" data-rw-transcript-version="2">
 &gt;&gt; [music]
 </span>
</p>