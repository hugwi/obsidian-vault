---
title: "The Future of MCP — David Soria Parra, Anthropic"
source: "https://m.youtube.com/watch?v=v3Fr2JR47KA&t=467s"
author: "AI Engineer"
published: 2026-04-19
created: 2026-04-26
description: "In this Keynote, I will lay out what I believe will be true for agents in"
tags:
  - to-process
  - agent-plugins-mcp
---

[music] >> Well, welcome. Let's get started. This is an MCP application. That's an agent shipping its own interface not through like a plugin, not through an SDK, 

not rendered on the fly by the model on the client side, or hardcoded into the product. That is something that is served over an MCP server, and you can take the server, put it into cloud, you can put it into ChatGPT, you can put it into VS Code Cursor, and it will just  work. And that I think it's kind of cool because for doing that, you need something that a lot of things that we're want in the ecosystem do not offer. You need semantics, you need to have both sides, 

client and the server, to understand what each side is talking, to understand how you render this, understand that there's a UI coming. And for that, you need a protocol. And the best part about this, an MCP server doesn't just ship an app, or can ship an app, it can also ship tools with it, and so you can interact with it with the application as a human, and you can have the model interact with it through tools, which is I think a very unique thing that I think we have 

not explored much just yet. Okay. But, let's quickly rewind a little bit from this what I think is a really cool glimpse into the future of MCP into over a year ago, 18 months, an eternity in AI life cycle, um all of this did not exist. There was just a little spec document, a few SDKs, uh mostly written by Claude, local only with little more than just tools. And in that last 18 or 

12 months, you guys have been absolutely crazy building stuff, um building servers, building um an crazy ecosystem around this, and we on our side have been busy busy taking this local only thing, added remote capabilities, added centralized authorization, added new primitive like elicitation and tasks, and last but not least, added new experimental features to the protocol like the MCP applications that you've just seen. 

And in the meantime, we have reached, I think, a really cool milestone because again, you all of you have been absolutely crazy building, building, and building. Of course, luckily with the help of a a bunch of agents. Um we're now like at 110 million monthly downloads. And that's just, of course, not us using it in our clients and servers. That's like OpenAI's agent SDK, that's Google's ADK, that's LangChain, thousands of frameworks and tools that you might have never ever heard of it pulling it as a as a dependency, which means there's one 

common standard that all of us have at our disposal to speak to each other. Um just a bit for context, uh React, one of the most successful um open source projects probably of the last decades, took roughly double the amount of time to reach that download volume. And in the meantime, of course, you all have been building really, really cool servers from like little toy projects of WhatsApp servers and Blender servers, uh to building SAS integrations like Linear, Slack, and Notion that are 

really powering what everyone does every day when they use MCPs. But most importantly, the vast majority of MCP server most of all of us have built are behind closed doors uh connecting company systems to agents uh and AI applications. But I still think this is just the absolute beginning of where we are. Because I think 2025 was all about exploring, and 2026 is all about putting these agents into production. Because if you really think about it, in my mind, 

2024, we just built a bunch of like demos and showed some cool stuff to people, and there was a little bit of a buzz there. 2025 was really all about coding agents. But coding agent, if you really think about it, are the most ideal scenario for an agent. It's local, it's verifiable, you can call a compiler, like you have a developer who can fix if it goes wrong in front of the in front of the computer, uh and you can display a UI interface, and the user's quite happy. 

But I think now with the capabilities of the model increasing, we're going into a new era, which I think this year will be we will see the start, where we're not just doing coding agents, we're going to have general agents that will do real knowledge worker stuff, like things a financial analysis analyst want to do, uh a marketing person want to do. And they need one thing in particular. They don't need a local agent that calls a compiler. What they need is something that could connect to like five SAS applications and a and a shared drive 

because the most important part for them for an agent is connectivity. And in my mind, connectivity is not one thing. If one if someone tells you there's one solution to all your connectivity problem, be it computer use, be it CLIs, be it MCP, they are probably pretty wrong because the right because the right thing, of course, is that it always means it depends, and there's a real a big connectivity stack, and there's a right tool for the right job. And in my mind, there are three major things that you 

want to consider building an agent in 2026. It's skills, MCP, and of course, like CLI or computer use depending on your use case. And they have three very distinct things that they can do in three different things you want to consider when you build your agent. Number one, skills, of course, is just like domain knowledge, it's just like capture-specific capabilities put into a very simple file, and it's mostly reusable. There are some minor differences between the different platform. Of course, CLIs very popular when local 

coding agents. It's an amazing tool to get simply started, to have something that you can pose in a bash, that you that automatically discover where the model can automatically discover what the CLI is capable of. And most importantly, if you have things that are like CLIs, like GitHub, Git, and other things that are in pre-training, CLI is an amazing solution for your connectivity part, and they're particularly good when you have a local agent where you can assume a sandbox, where you can assume a code execution 

environment. But if you don't have this, if you need rich semantics, when you need a UI that can display long-running tasks, when you can have when you need things like resources, when you need to build something that is full decoupled and needs platform independence, or you don't have a sandbox, when you need things like authorization, governance, policies, or short to say boring enter boring but important enterprise stuff, or if you want to have experiments like MCP applications or what comes soon, 

skills over MCP, then I think MCP is just like additional connective tissue that is just yet another tool in the toolbox for you to build an amazing agent. And so this is all to say that I think in 2026, we're going to start building agents that use all of it. They don't use one thing, they use all of it, and they use them quite seamlessly together. But I don't think we're quite there just yet. Because we need to build a lot of stuff 

partially um because our agents kind of still suck. Um and partially because I think we just haven't talked enough about like some of the techniques you can do uh to really put this connective tissue together. The number one thing that we need to go and start building is on the client side, on the on the agent harness side, on the things that powers the connective parts, that be it a cloud code, uh be it a pie, be it whatever application you're 

going to build. And the number one thing we're going to do there, and what we all have to do, and something I want to really get across today, is that we need to go and start building something called progressive discovery. Most people when they think about like, "Oh, I MCP," they can't think about like context load. But if you really consider what a protocol does, the protocol just puts information across the wire, but the client is responsible for dealing with that information. And what everybody so far has done because we're 

in this very early experimentation phase, is to simply put all the tools into the context window, and then be quite surprised that maybe the context window gets large. Um but what you can do instead, and what you should do instead, you should start using this progressive discovery pattern, which is to say, use something like tool search to defer the loading of the tools, and start loading the tools when the model needs it. And we have this in 

the Anthropic API, and people can use this uh on on competitors' APIs as well. But also, you can just build this in yourself where you just download the tool directly, and the moment you give the you give the model a tool loading tool, basically, and the model goes like, "Ah, maybe I need a tool now. Let me look up what tools I need." And then you load them on demand. And here in this example, what you're seeing is on the left side is uh Claude Code before we added this to Claude Code, and then after it uh to Claude Code. So you see a massive 

reduction in tool uh use uh tool context usage. The second part of that is is something called programmatic tool calling, or what other people usually refer to um to code mode. Um this is the idea that one thing that you really want to do is you want to compose things together. You don't want the model to go call a tool, take the result, then go and talk, call another 

tool, take the result, call another tool. Because what you're effectively doing is you're letting the model orchestrate things together, and in that orchestration, you're using inference, you're it's it's latency sensitive, and all of it stuff could be done way more effective if you would instead write a script. Um and in fact, that's actually what you constantly do and what you constantly see things like hard code do when it writes the bash command. But you can of course do this with everything, and you can do this with MCP, and you should do 

this with MCP. So, what does this mean? So, what you want instead of having one tool at another, you want to give the model a repple tool, provide like a like a execution environment, like a V8 isolate or a monty or something like that, or a lua interpreter, and just have the model write the code for you, and the model just executes that code, and then composes them together. And there's a neat little feature in MCP called structured output that tells you 

what the return value of the output will be, and the model can use this information to to figure out type information, which then mean it can really nicely compose these things together. And in this example here, instead of doing two different calls, you do one call, and you can filter that the model will automatically remove things from a JSON and just continue. Of course, if you don't have uh structured output, you can always just 

ask the model to give you structured output um uh by just extracting it and saying, "Hey, call us cheap model and say, 'I want this expected type, give it back to me.'" And bam, you have a type, the model can compose things together, and I think this is something we're just not doing enough yet, and this is I think something where we can improve our agent harnesses. And then last but not least, of course, you can just compile compose these things together with executables, like with CLIs, with other components, with APIs as well. Um next, what we need to do besides the 

client work, which is progressive discovery and um programmatic tool calling, we need to go and start building properly for agents. And that means we all need to stop taking rest APIs and put them one-to-one into uh an MCP server. Every time I see someone building another rest to MCP server a conversion tool, I'm it's a bit cringe because I think it's just it just results in horrible things. Um and what you should do instead, you 

should design for an agent. Or basically, you can start designing for you as a human, how you would want to interact with this, because that's actually a very, very good start for an agent. If you want to orchestrate things together, you should reach, of course, for programmatic tool calling, and you can do this on the client side, as I said before, but you can also do this on the server side. The Cloudflare MCP server and others like that are great examples how you can have, instead of providing tools, provide an execution environment to the model and then just 

have them orchestrate things together, which again cuts on token usages, cuts on latency, and is way more powerful in its composition. And then last but not least, you should start and we should start as server authors to use this rich semantics that MCP offers over alternatives. This means shipping MCP applications, it means shipping skills over MCP, it means um using things like task and other aspects that the protocol offers that we're currently slightly underused, or 

things like elicitations. Things that only MCP can do for you. And of course, that's all the work you all need to do, and maybe some of our product people need to do, we also need to do a lot of work on MCP itself. And there's a few things down the line that we're going to go and have to go and solve. The number one thing is we need to improve the core. There's a few things that, as we have developed the protocol over the last year, that are just not in a good shape. Number one is that the current streamable HTTP is very hard to 

scale if you're a large hyperscaler. >> [snorts] >> And so, we have a proposal from our friends at Google, who are working on something called a stateless transport protocol, which make it significantly easier to just treat MCP servers like you know, another stateless uh rest server or something like that and we are used to know how to deploy to like cloud runs or kubernetes and so on. So, that's coming down in June and hopefully lining in the SDKs very soon. 

In addition, we need to improve our asynchronous task primitive, which basically is a very fancy way to say we just want to have agent-to-agent communication. We have a very experimental version of the protocol that very few clients support, so we're going to start building more clients out like that, and most importantly, we are improving some of the little semantics that we need to do. We're going to ship a TypeScript version SDK version two and Python SDK version two based on a lot of the lessons learned over the last year. 

There's a there's a SDK called fast MCP. Who's using fast MCP? Yeah. It's just way better than Python SDK that we're shipping, right? And that's on me because I wrote the Python SDK. Um and and so, I have a bunch of people who are way better Python developers than me help me write it better. Um the second part is we need to start integrating everywhere. We're going to ship for particularly for enterprises something called cross-app access. It's a new thing that we're working closely together with identity providers, which 

just allows you It's a very fancy way to say once you log in once with your local company identity provider, be it a Google, be it an Okta, you will be able to just use MCP servers without having to re-login. So, it's a bit more smoothness. Um in addition, we're going to add something called a server discovery by by specifying how you can discover servers on well-known URLs automatically. So, crawlers, browsers, um agents can just go to a website and say, 

"Oh, I'm instead of just parsing the website, is there also an MCP server I can use?" And we will be able to automatically discover this. This is a really cool thing that will come down also in June when we launch the next specification and will be supported there. And then last but not least, we're starting to use our extension mechanisms in in MCP, which means that some clients will support this, like for example, MCP applications will only be supported by web-based interfaces, because if you're a CLI, you just have a hard time rendering HTML, right? Um and we will do 

more of these extensions. One of the most exciting extensions that I think is is cool, we're just going to ship skills over MCP, because it's very obvious that if you have a large MCP server with tons and tons of tools, you just want to ship the main knowledge with it and say, "Oh, this is how you're supposed to use this. This is how you're supposed to use this." And it allows you as a server author to continuously ship updated skills without having to rely on plugin mechanisms on registries and other stuff. So, that's coming down. Um 

there's a lot a lot of experimentation from people already in that space. You can already do some of that today if you just give the model a load skills tool. Like there you can you can build primitives or versions of this today without having to rely on the semantics, but of course, we're going to define the semantics. Okay. So, that's for me a long-winded way to think to say that I think MCP is actually in a really good shape, and I think in this year, we're going to push uh agents to full connectivity, um MCP will continue to play a major, 

major, major role. And we want, of course, your feedback. We are very open community. We are just have created a foundation. We're mostly running as an open-source community with a discord, with issues. Um just come to us and tell us where the are we wrong, what are we getting right, um so that we can improve this on a continuous basis. So, 2026, I think is all about connectivity, and the best agents use every available method. Like they will use computer use, they will use CLIs, they will use MCPs, and they will use will use skills. 

Because they want to have a wide variety of things they can do, and then they can ship cool stuff like this, um which is um one of the product features we shipped recently. Uh under the hood, it's nothing but an MCP application um that renders stuff, right? Cool. So, we can now look at uh the model writing graphs. Anyway, thank you. 

>> [music] 

<p>
 <span data-rw-start="7.205" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="15.36" data-rw-transcript-version="2">
 &gt;&gt; Well,
 </span>
 <span data-rw-start="16.76" data-rw-transcript-version="2">
 welcome.
 </span>
 <span data-rw-start="18.84" data-rw-transcript-version="2">
 Let's get started.
 </span>
 <span data-rw-start="21.28" data-rw-transcript-version="2">
 This is an MCP application.
 </span>
 <span data-rw-start="22.8" data-rw-transcript-version="2">
 That's an agent shipping its own
 </span>
 <span data-rw-start="25.52" data-rw-transcript-version="2">
 interface not through like a plugin, not
 </span>
 <span data-rw-start="27.48" data-rw-transcript-version="2">
 through an SDK,
 </span>
 <span data-rw-start="29.52" data-rw-transcript-version="2">
 not rendered on the fly by the model on
 </span>
 <span data-rw-start="30.88" data-rw-transcript-version="2">
 the client side, or hardcoded into the
 </span>
 <span data-rw-start="33.96" data-rw-transcript-version="2">
 product. That is something that is
 </span>
 <span data-rw-start="36.36" data-rw-transcript-version="2">
 served over an MCP server, and you can
 </span>
 <span data-rw-start="38.36" data-rw-transcript-version="2">
 take the server, put it into the cloud, you
 </span>
 <span data-rw-start="40.92" data-rw-transcript-version="2">
 can put it into ChatGPT, you can put it
 </span>
 <span data-rw-start="42.68" data-rw-transcript-version="2">
 into VS Code Cursor, and it will just
 </span>
 <span data-rw-start="44.68" data-rw-transcript-version="2">
 work.
 </span>
</p>
<p>
 <span data-rw-start="50.12" data-rw-transcript-version="2">
 And that, I think, is kind of cool because for
 </span>
 <span data-rw-start="52.36" data-rw-transcript-version="2">
 doing that, you need something that a
 </span>
 <span data-rw-start="53.84" data-rw-transcript-version="2">
 lot of things that we're want in the
 </span>
 <span data-rw-start="55.8" data-rw-transcript-version="2">
 ecosystem do not offer. You need
 </span>
 <span data-rw-start="58.2" data-rw-transcript-version="2">
 semantics, you need to have both sides,
 </span>
 <span data-rw-start="59.96" data-rw-transcript-version="2">
 client and the server, to understand
 </span>
 <span data-rw-start="61.88" data-rw-transcript-version="2">
 what each side is talking about, to understand.
 </span>
</p>
<p>
 <span data-rw-start="66.48" data-rw-transcript-version="2">
 How you render this, understand that
 </span>
 <span data-rw-start="68.4" data-rw-transcript-version="2">
 there's a UI coming.
 </span>
 <span data-rw-start="70.36" data-rw-transcript-version="2">
 And for that, you need a protocol.
 </span>
 <span data-rw-start="73.72" data-rw-transcript-version="2">
 And the best part about this,
 </span>
 <span data-rw-start="75.84" data-rw-transcript-version="2">
 an MCP server doesn't just ship an app,
 </span>
 <span data-rw-start="78.12" data-rw-transcript-version="2">
 or can ship an app, it can also ship
 </span>
 <span data-rw-start="80.32" data-rw-transcript-version="2">
 tools with it, and so you can interact
 </span>
 <span data-rw-start="82.52" data-rw-transcript-version="2">
 with it with the application as a human,
 </span>
 <span data-rw-start="85.2" data-rw-transcript-version="2">
 and you can have the model interact with
 </span>
 <span data-rw-start="86.64" data-rw-transcript-version="2">
 it through tools, which is I think a
 </span>
 <span data-rw-start="88.6" data-rw-transcript-version="2">
 very unique thing that I think we have
 </span>
 <span data-rw-start="90.68" data-rw-transcript-version="2">
 not explored much.
 </span>
 <span data-rw-start="92.92" data-rw-transcript-version="2">
 Just yet.
 </span>
</p>
<p>
 <span data-rw-start="94.76" data-rw-transcript-version="2">
 Okay.
 </span>
 <span data-rw-start="95.76" data-rw-transcript-version="2">
 But, let's quickly rewind a little bit
 </span>
 <span data-rw-start="97.56" data-rw-transcript-version="2">
 from this, what I think is a really cool
 </span>
 <span data-rw-start="100" data-rw-transcript-version="2">
 glimpse into the future of MCP into over
 </span>
 <span data-rw-start="103.84" data-rw-transcript-version="2">
 a year ago, 18 months, an eternity in AI
 </span>
 <span data-rw-start="106.76" data-rw-transcript-version="2">
 life cycle, uh, all of this did not
 </span>
 <span data-rw-start="109.28" data-rw-transcript-version="2">
 exist. There was just a little spec
 </span>
 <span data-rw-start="111.24" data-rw-transcript-version="2">
 document, a few SDKs, uh, mostly written
 </span>
 <span data-rw-start="114.28" data-rw-transcript-version="2">
 by Claude, local-only with little more
 </span>
 <span data-rw-start="117.76" data-rw-transcript-version="2">
 than just tools. And in that last 18 or
 </span>
 <span data-rw-start="120.8" data-rw-transcript-version="2">
 12 months, you guys have been absolutely
 </span>
 <span data-rw-start="122.88" data-rw-transcript-version="2">
 crazy building stuff.
 </span>
</p>
<p>
 <span data-rw-start="125.16" data-rw-transcript-version="2">
 Servers, building an crazy ecosystem
 </span>
 <span data-rw-start="127.84" data-rw-transcript-version="2">
 around this, and we on our side have
 </span>
 <span data-rw-start="129.88" data-rw-transcript-version="2">
 been busy, busy taking this local only
 </span>
 <span data-rw-start="132.44" data-rw-transcript-version="2">
 thing, added remote capabilities, added
 </span>
 <span data-rw-start="135.84" data-rw-transcript-version="2">
 centralized authorization, added new
 </span>
 <span data-rw-start="138.64" data-rw-transcript-version="2">
 primitives like elicitation and tasks,
 </span>
 <span data-rw-start="141.2" data-rw-transcript-version="2">
 and last but not least, added new
 </span>
 <span data-rw-start="143.12" data-rw-transcript-version="2">
 experimental features to the protocol
 </span>
 <span data-rw-start="145" data-rw-transcript-version="2">
 like the MCP applications that you've
 </span>
 <span data-rw-start="147.32" data-rw-transcript-version="2">
 just seen.
 </span>
</p>
<p>
 <span data-rw-start="150.16" data-rw-transcript-version="2">
 And in the meantime,
 </span>
 <span data-rw-start="152.04" data-rw-transcript-version="2">
 we have reached, I think, a really cool
 </span>
 <span data-rw-start="153.52" data-rw-transcript-version="2">
 milestone because, again, all of you
 </span>
 <span data-rw-start="155.64" data-rw-transcript-version="2">
 have been absolutely crazy building,
 </span>
 <span data-rw-start="157.2" data-rw-transcript-version="2">
 building, and building. Of course,
 </span>
 <span data-rw-start="158.68" data-rw-transcript-version="2">
 luckily with the help of a bunch of
 </span>
 <span data-rw-start="160.84" data-rw-transcript-version="2">
 agents. Um,
 </span>
 <span data-rw-start="162.8" data-rw-transcript-version="2">
 We're now like at 110 million
 </span>
 <span data-rw-start="165.64" data-rw-transcript-version="2">
 monthly downloads. And that's just, of
 </span>
 <span data-rw-start="167.08" data-rw-transcript-version="2">
 course, not us using it in our clients
 </span>
 <span data-rw-start="169.68" data-rw-transcript-version="2">
 and servers. That's like OpenAI's agent
 </span>
 <span data-rw-start="172.2" data-rw-transcript-version="2">
 SDK, that's Google's SDK, that's
 </span>
 <span data-rw-start="174.08" data-rw-transcript-version="2">
 LangChain, thousands of frameworks and
 </span>
 <span data-rw-start="176.64" data-rw-transcript-version="2">
 tools that you might have never ever
 </span>
 <span data-rw-start="178.08" data-rw-transcript-version="2">
 heard of, pulling it as a
 </span>
 <span data-rw-start="179.96" data-rw-transcript-version="2">
 As a dependency, which means there's one
 </span>
 <span data-rw-start="182.4" data-rw-transcript-version="2">
 common standard that all of us have at
 </span>
 <span data-rw-start="185.76" data-rw-transcript-version="2">
 our disposal to speak to each other. Um,
 </span>
 <span data-rw-start="189.28" data-rw-transcript-version="2">
 just a bit for context, uh, React, one of
 </span>
 <span data-rw-start="191.52" data-rw-transcript-version="2">
 the most successful, um,
 </span>
 <span data-rw-start="193.92" data-rw-transcript-version="2">
 open source projects, probably of the
 </span>
 <span data-rw-start="195.56" data-rw-transcript-version="2">
 last decades, took roughly double the
 </span>
 <span data-rw-start="197.6" data-rw-transcript-version="2">
 amount of time to reach that download
 </span>
 <span data-rw-start="198.96" data-rw-transcript-version="2">
 volume.
 </span>
</p>
<p>
 <span data-rw-start="200.12" data-rw-transcript-version="2">
 And in the meantime, of course, you all
 </span>
 <span data-rw-start="201.32" data-rw-transcript-version="2">
 have been building really, really cool
 </span>
 <span data-rw-start="202.48" data-rw-transcript-version="2">
 servers from, like, little toy projects of
 </span>
 <span data-rw-start="204.8" data-rw-transcript-version="2">
 WhatsApp servers and Blender servers, uh,
 </span>
 <span data-rw-start="207.08" data-rw-transcript-version="2">
 to building SaaS integrations like
 </span>
 <span data-rw-start="208.92" data-rw-transcript-version="2">
 Linear, Slack, and Notion that are
 </span>
 <span data-rw-start="210.4" data-rw-transcript-version="2">
 really powering what everyone does every
 </span>
 <span data-rw-start="212.72" data-rw-transcript-version="2">
 day when they use MCPs. But most
 </span>
 <span data-rw-start="214.92" data-rw-transcript-version="2">
 importantly, the vast majority of MCP
 </span>
 <span data-rw-start="217.04" data-rw-transcript-version="2">
 server, most of all of us have built, are
 </span>
 <span data-rw-start="218.84" data-rw-transcript-version="2">
 behind closed doors, uh, connecting
 </span>
 <span data-rw-start="220.84" data-rw-transcript-version="2">
 company systems to agents, uh, and AI
 </span>
 <span data-rw-start="224.2" data-rw-transcript-version="2">
 applications.
 </span>
</p>
<p>
 <span data-rw-start="226.16" data-rw-transcript-version="2">
 But I still think this is just the
 </span>
 <span data-rw-start="227.76" data-rw-transcript-version="2">
 absolute beginning of where we are.
 </span>
</p>
<p>
 <span data-rw-start="231.48" data-rw-transcript-version="2">
 Because I think 2025 was all about
 </span>
 <span data-rw-start="234.24" data-rw-transcript-version="2">
 Exploring, and 2026 is all about putting
 </span>
 <span data-rw-start="237.08" data-rw-transcript-version="2">
 these agents into production. Because if
 </span>
 <span data-rw-start="239.68" data-rw-transcript-version="2">
 you really think about it, in my mind,
 </span>
 <span data-rw-start="241.2" data-rw-transcript-version="2">
 2024, we just built a bunch of like
 </span>
 <span data-rw-start="243.6" data-rw-transcript-version="2">
 demos and showed some cool stuff to
 </span>
 <span data-rw-start="245.48" data-rw-transcript-version="2">
 people, and there was a little bit of a
 </span>
 <span data-rw-start="247.28" data-rw-transcript-version="2">
 buzz there. 2025 was really all about
 </span>
 <span data-rw-start="250.24" data-rw-transcript-version="2">
 coding agents. But coding agent, if you
 </span>
 <span data-rw-start="252.08" data-rw-transcript-version="2">
 really think about it, are the most
 </span>
 <span data-rw-start="254.28" data-rw-transcript-version="2">
 ideal scenario for an agent. It's local,
 </span>
 <span data-rw-start="257.079" data-rw-transcript-version="2">
 it's verifiable, you can call a
 </span>
 <span data-rw-start="258.519" data-rw-transcript-version="2">
 compiler, like you have a developer who
 </span>
 <span data-rw-start="261.079" data-rw-transcript-version="2">
 can fix if it goes wrong in front
 </span>
 <span data-rw-start="263.56" data-rw-transcript-version="2">
 of the computer, uh, and
 </span>
 <span data-rw-start="266.12" data-rw-transcript-version="2">
 you can display a UI interface, and the
 </span>
 <span data-rw-start="268.68" data-rw-transcript-version="2">
 user's quite happy.
 </span>
</p>
<p>
 <span data-rw-start="270.92" data-rw-transcript-version="2">
 But I think now, with the capabilities of
 </span>
 <span data-rw-start="272.68" data-rw-transcript-version="2">
 the model increasing, we're going into a
 </span>
 <span data-rw-start="275.28" data-rw-transcript-version="2">
 new era, which I think this year will be
 </span>
 <span data-rw-start="277.52" data-rw-transcript-version="2">
 we will see the start, where we're not
 </span>
 <span data-rw-start="279.36" data-rw-transcript-version="2">
 just doing coding agents, we're going to
 </span>
 <span data-rw-start="281.28" data-rw-transcript-version="2">
 have general agents that will do real
 </span>
 <span data-rw-start="283.84" data-rw-transcript-version="2">
 knowledge worker stuff, like things a
 </span>
 <span data-rw-start="285.88" data-rw-transcript-version="2">
 financial analysis analyst wants to do,
 </span>
 <span data-rw-start="288.72" data-rw-transcript-version="2">
 uh, a marketing person wants to do.
 </span>
</p>
<p>
 <span data-rw-start="290.84" data-rw-transcript-version="2">
 They need one thing in particular. They
 </span>
 <span data-rw-start="294.12" data-rw-transcript-version="2">
 don't need a local agent that calls a
 </span>
 <span data-rw-start="295.56" data-rw-transcript-version="2">
 compiler. What they need is something
 </span>
 <span data-rw-start="297.56" data-rw-transcript-version="2">
 that could connect to like five SAS
 </span>
 <span data-rw-start="299.36" data-rw-transcript-version="2">
 applications and a shared drive,
 </span>
 <span data-rw-start="302.16" data-rw-transcript-version="2">
 because the most important part for them
 </span>
 <span data-rw-start="304.04" data-rw-transcript-version="2">
 for an agent is connectivity.
 </span>
 <span data-rw-start="306.56" data-rw-transcript-version="2">
 And in my mind, connectivity is not one
 </span>
 <span data-rw-start="309.16" data-rw-transcript-version="2">
 thing. If one if someone tells you
 </span>
 <span data-rw-start="311.04" data-rw-transcript-version="2">
 there's one solution to all your
 </span>
 <span data-rw-start="312.24" data-rw-transcript-version="2">
 connectivity problem, be it computer
 </span>
 <span data-rw-start="313.88" data-rw-transcript-version="2">
 use, be it CLIs, be it MCP,
 </span>
 <span data-rw-start="316.28" data-rw-transcript-version="2">
 they are probably pretty wrong because
 </span>
 <span data-rw-start="318.12" data-rw-transcript-version="2">
 the right because the right thing, of
 </span>
 <span data-rw-start="319.88" data-rw-transcript-version="2">
 course, is that it always means it
 </span>
 <span data-rw-start="321.88" data-rw-transcript-version="2">
 depends, and there's a real a big
 </span>
 <span data-rw-start="323.92" data-rw-transcript-version="2">
 connectivity stack, and there's a right
 </span>
 <span data-rw-start="326.12" data-rw-transcript-version="2">
 tool for the right job. And in my mind,
 </span>
 <span data-rw-start="328.76" data-rw-transcript-version="2">
 there are three major things that you
 </span>
 <span data-rw-start="330.32" data-rw-transcript-version="2">
 want to consider building an agent in
 </span>
 <span data-rw-start="331.88" data-rw-transcript-version="2">
 2026. It's skills, MCP, and of course,
 </span>
 <span data-rw-start="334.84" data-rw-transcript-version="2">
 like CLI or computer use depending on
 </span>
 <span data-rw-start="337.28" data-rw-transcript-version="2">
 your use case. And they have three very
 </span>
 <span data-rw-start="339.68" data-rw-transcript-version="2">
 distinct things that they can do in
 </span>
 <span data-rw-start="341.2" data-rw-transcript-version="2">
 three different things you want to
 </span>
 <span data-rw-start="343.2" data-rw-transcript-version="2">
 Consider when you build your agent.
 </span>
</p>
<p>
 <span data-rw-start="346.8" data-rw-transcript-version="2">
 Number one, skills, of course, is just
 </span>
 <span data-rw-start="348.8" data-rw-transcript-version="2">
 like domain knowledge, it's just like
 </span>
 <span data-rw-start="350.32" data-rw-transcript-version="2">
 capture-specific capabilities put into a
 </span>
 <span data-rw-start="352.88" data-rw-transcript-version="2">
 very simple file, and it's mostly
 </span>
 <span data-rw-start="354.48" data-rw-transcript-version="2">
 reusable. There are some minor
 </span>
 <span data-rw-start="356.16" data-rw-transcript-version="2">
 differences between the different
 </span>
 <span data-rw-start="357.32" data-rw-transcript-version="2">
 platform.
 </span>
 <span data-rw-start="359.08" data-rw-transcript-version="2">
 Of course, CLI is very popular when local
 </span>
 <span data-rw-start="361.76" data-rw-transcript-version="2">
 coding agents. It's an amazing tool to
 </span>
 <span data-rw-start="364.48" data-rw-transcript-version="2">
 get started, to have something
 </span>
 <span data-rw-start="366.6" data-rw-transcript-version="2">
 that you can pose in a bash, that you
 </span>
 <span data-rw-start="368.64" data-rw-transcript-version="2">
 that automatically discovers where the
 </span>
 <span data-rw-start="370.52" data-rw-transcript-version="2">
 model can automatically discover what
 </span>
 <span data-rw-start="371.88" data-rw-transcript-version="2">
 the CLI is capable of. And most
 </span>
 <span data-rw-start="373.8" data-rw-transcript-version="2">
 importantly, if you have things that are
 </span>
 <span data-rw-start="376.36" data-rw-transcript-version="2">
 like CLIs, like GitHub, Git, and other
 </span>
 <span data-rw-start="378.64" data-rw-transcript-version="2">
 things that are in pre-training, CLI is
 </span>
 <span data-rw-start="380.92" data-rw-transcript-version="2">
 an amazing solution for your
 </span>
 <span data-rw-start="382.68" data-rw-transcript-version="2">
 connectivity part, and they're
 </span>
 <span data-rw-start="384.36" data-rw-transcript-version="2">
 particularly good when you have a local
 </span>
 <span data-rw-start="386" data-rw-transcript-version="2">
 agent where you can assume a sandbox,
 </span>
 <span data-rw-start="388.48" data-rw-transcript-version="2">
 where you can assume a code execution
 </span>
 <span data-rw-start="390.08" data-rw-transcript-version="2">
 environment.
 </span>
</p>
<p>
 <span data-rw-start="391.56" data-rw-transcript-version="2">
 But if you don't have this, if you need
 </span>
 <span data-rw-start="393.24" data-rw-transcript-version="2">
 Rich semantics, when you need a UI that
 </span>
 <span data-rw-start="396.16" data-rw-transcript-version="2">
 can display long-running tasks, when you
 </span>
 <span data-rw-start="397.96" data-rw-transcript-version="2">
 can have, when you need things like
 </span>
 <span data-rw-start="399.52" data-rw-transcript-version="2">
 resources, when you need to build
 </span>
 <span data-rw-start="401.44" data-rw-transcript-version="2">
 something that is fully decoupled and
 </span>
 <span data-rw-start="403.64" data-rw-transcript-version="2">
 needs platform independence, or you
 </span>
 <span data-rw-start="405.32" data-rw-transcript-version="2">
 don't have a sandbox, when you need
 </span>
 <span data-rw-start="407.2" data-rw-transcript-version="2">
 things like authorization, governance,
 </span>
 <span data-rw-start="410.04" data-rw-transcript-version="2">
 policies, or, short to say, boring but important enterprise stuff,
 </span>
 <span data-rw-start="412.96" data-rw-transcript-version="2">
 or if you want to have experiments like
 </span>
 <span data-rw-start="418.2" data-rw-transcript-version="2">
 MCP applications or what comes soon,
 </span>
 <span data-rw-start="421.12" data-rw-transcript-version="2">
 skills over MCP, then I think MCP is
 </span>
 <span data-rw-start="424.68" data-rw-transcript-version="2">
 just like additional connective tissue
 </span>
 <span data-rw-start="426.64" data-rw-transcript-version="2">
 that is just yet another tool in the
 </span>
 <span data-rw-start="428.76" data-rw-transcript-version="2">
 toolbox for you to build an amazing
 </span>
 <span data-rw-start="430.92" data-rw-transcript-version="2">
 agent.
 </span>
</p>
<p>
 <span data-rw-start="432.12" data-rw-transcript-version="2">
 And so, this is all to say that I think
 </span>
 <span data-rw-start="433.96" data-rw-transcript-version="2">
 in 2026, we're going to start building
 </span>
 <span data-rw-start="436.28" data-rw-transcript-version="2">
 agents that use all of it. They don't
 </span>
 <span data-rw-start="438.56" data-rw-transcript-version="2">
 use one thing, they use all of it, and
 </span>
 <span data-rw-start="440.16" data-rw-transcript-version="2">
 they use them quite seamlessly together.
 </span>
 <span data-rw-start="444.88" data-rw-transcript-version="2">
 But I don't think we're quite there just
 </span>
 <span data-rw-start="447.32" data-rw-transcript-version="2">
 yet.
 </span>
 <span data-rw-start="448.88" data-rw-transcript-version="2">
 Because we need to build a lot of stuff.
 </span>
</p>
<p>
 <span data-rw-start="451.4" data-rw-transcript-version="2">
 Partially, um, because
 </span>
 <span data-rw-start="454.84" data-rw-transcript-version="2">
 our agents kind of still suck.
 </span>
 <span data-rw-start="456.88" data-rw-transcript-version="2">
 Um, and partially because I think we just
 </span>
 <span data-rw-start="458.76" data-rw-transcript-version="2">
 haven't talked enough about, like, some of
 </span>
 <span data-rw-start="460.52" data-rw-transcript-version="2">
 the techniques you can do
 </span>
 <span data-rw-start="462.36" data-rw-transcript-version="2">
 uh, to really put this connective tissue
 </span>
 <span data-rw-start="464.36" data-rw-transcript-version="2">
 together.
 </span>
 <span data-rw-start="467.44" data-rw-transcript-version="2">
 The number one thing that we need to go
 </span>
 <span data-rw-start="469.72" data-rw-transcript-version="2">
 and start building is on the client
 </span>
 <span data-rw-start="471.64" data-rw-transcript-version="2">
 side, on the agent harness side,
 </span>
 <span data-rw-start="474.32" data-rw-transcript-version="2">
 on the things that power the connective
 </span>
 <span data-rw-start="476.44" data-rw-transcript-version="2">
 parts, that be it a cloud code, uh, be it
 </span>
 <span data-rw-start="480" data-rw-transcript-version="2">
 a pie, be it whatever application you're
 </span>
 <span data-rw-start="482.04" data-rw-transcript-version="2">
 going to build.
 </span>
 <span data-rw-start="484.68" data-rw-transcript-version="2">
 And the number one thing we're going to
 </span>
 <span data-rw-start="485.68" data-rw-transcript-version="2">
 do there, and what we all have to do,
 </span>
 <span data-rw-start="487.48" data-rw-transcript-version="2">
 and something I want to really get
 </span>
 <span data-rw-start="488.56" data-rw-transcript-version="2">
 across today, is that we need to go and
 </span>
 <span data-rw-start="490.64" data-rw-transcript-version="2">
 start building something called
 </span>
 <span data-rw-start="491.84" data-rw-transcript-version="2">
 progressive discovery.
 </span>
</p>
<p>
 <span data-rw-start="494.4" data-rw-transcript-version="2">
 Most people when they think about, like,
 </span>
 <span data-rw-start="496.04" data-rw-transcript-version="2">
 "Oh,
 </span>
 <span data-rw-start="497.28" data-rw-transcript-version="2">
 I MCP," they can't think about, like,
 </span>
 <span data-rw-start="499.88" data-rw-transcript-version="2">
 context load. But if you really consider
 </span>
 <span data-rw-start="502.12" data-rw-transcript-version="2">
 what a protocol does, the protocol just
 </span>
 <span data-rw-start="503.8" data-rw-transcript-version="2">
 puts information across the wire, but
 </span>
 <span data-rw-start="506.24" data-rw-transcript-version="2">
 the client is responsible for dealing
 </span>
 <span data-rw-start="508.08" data-rw-transcript-version="2">
 with that information. And what
 </span>
 <span data-rw-start="509.92" data-rw-transcript-version="2">
 everybody so far has done because we're
 </span>
 <span data-rw-start="511.68" data-rw-transcript-version="2">
 in this very early experimentation
 </span>
 <span data-rw-start="513.159" data-rw-transcript-version="2">
 phase, is to simply put all the tools
 </span>
 <span data-rw-start="515.44" data-rw-transcript-version="2">
 into the context window, and then be
 </span>
 <span data-rw-start="517.2" data-rw-transcript-version="2">
 quite surprised that maybe the context
 </span>
 <span data-rw-start="518.96" data-rw-transcript-version="2">
 window gets large. Um
 </span>
 <span data-rw-start="521.599" data-rw-transcript-version="2">
 but what you can do instead, and what
 </span>
 <span data-rw-start="523.56" data-rw-transcript-version="2">
 you should do instead, you should start
 </span>
 <span data-rw-start="525.96" data-rw-transcript-version="2">
 using this progressive discovery
 </span>
 <span data-rw-start="528.28" data-rw-transcript-version="2">
 pattern,
 </span>
 <span data-rw-start="529.48" data-rw-transcript-version="2">
 which is to say, use something like tool
 </span>
 <span data-rw-start="531.76" data-rw-transcript-version="2">
 search to defer the loading of the
 </span>
 <span data-rw-start="534.44" data-rw-transcript-version="2">
 tools, and start loading the tools when
 </span>
 <span data-rw-start="537.68" data-rw-transcript-version="2">
 the model needs it. And we have this in
 </span>
 <span data-rw-start="540.2" data-rw-transcript-version="2">
 the Anthropic API, and people can use
 </span>
 <span data-rw-start="543.44" data-rw-transcript-version="2">
 this uh on on competitors' APIs as well.
 </span>
</p>
<p>
 <span data-rw-start="546.44" data-rw-transcript-version="2">
 But also, you can just build this in
 </span>
 <span data-rw-start="547.84" data-rw-transcript-version="2">
 yourself where you just download the
 </span>
 <span data-rw-start="549.28" data-rw-transcript-version="2">
 tool directly, and the moment you give
 </span>
 <span data-rw-start="551.48" data-rw-transcript-version="2">
 the model a tool loading
 </span>
 <span data-rw-start="553.28" data-rw-transcript-version="2">
 tool, basically, and the model goes
 </span>
 <span data-rw-start="554.88" data-rw-transcript-version="2">
 like, "Ah, maybe I need a tool now. Let
 </span>
 <span data-rw-start="556.44" data-rw-transcript-version="2">
 Let's look up what tools I need.
 </span>
</p>
<p>
 <span data-rw-start="558.6" data-rw-transcript-version="2">
 And then you load them on demand.
 </span>
 <span data-rw-start="561.56" data-rw-transcript-version="2">
 And here, in this example, what you're
 </span>
 <span data-rw-start="562.88" data-rw-transcript-version="2">
 seeing is on the left side is uh Claude
 </span>
 <span data-rw-start="565.2" data-rw-transcript-version="2">
 Code before we added this to Claude
 </span>
 <span data-rw-start="567.32" data-rw-transcript-version="2">
 Code, and then after it, uh
 </span>
 <span data-rw-start="569.64" data-rw-transcript-version="2">
 to Claude Code. So you see a massive
 </span>
 <span data-rw-start="571.52" data-rw-transcript-version="2">
 reduction
 </span>
 <span data-rw-start="573.16" data-rw-transcript-version="2">
 in tool
 </span>
 <span data-rw-start="575.32" data-rw-transcript-version="2">
 uh use, uh tool context usage.
 </span>
</p>
<p>
 <span data-rw-start="579.24" data-rw-transcript-version="2">
 The second part of that is is something
 </span>
 <span data-rw-start="580.8" data-rw-transcript-version="2">
 called programmatic tool calling, or
 </span>
 <span data-rw-start="582.68" data-rw-transcript-version="2">
 what other people usually refer to, um
 </span>
 <span data-rw-start="585.48" data-rw-transcript-version="2">
 to code mode.
 </span>
 <span data-rw-start="586.96" data-rw-transcript-version="2">
 Um, this is the idea that one thing that
 </span>
 <span data-rw-start="590.96" data-rw-transcript-version="2">
 you really want to do is you want to
 </span>
 <span data-rw-start="592.56" data-rw-transcript-version="2">
 compose things together. You don't want
 </span>
 <span data-rw-start="596.12" data-rw-transcript-version="2">
 the model to go call a tool, take the
 </span>
 <span data-rw-start="598.52" data-rw-transcript-version="2">
 result, then go and talk, call another
 </span>
 <span data-rw-start="600.88" data-rw-transcript-version="2">
 tool,
 </span>
 <span data-rw-start="602.16" data-rw-transcript-version="2">
 take the result, call another tool.
 </span>
</p>
<p>
 <span data-rw-start="603.6" data-rw-transcript-version="2">
 Because what you're effectively doing is
 </span>
 <span data-rw-start="605.08" data-rw-transcript-version="2">
 you're letting the model orchestrate
 </span>
 <span data-rw-start="606.64" data-rw-transcript-version="2">
 things together, and in that
 </span>
 <span data-rw-start="608.16" data-rw-transcript-version="2">
 orchestration, you're using inference.
 </span>
</p>
<p>
 <span data-rw-start="609.76" data-rw-transcript-version="2">
 You're; it's; latency sensitive, and
 </span>
 <span data-rw-start="612.32" data-rw-transcript-version="2">
 all of it stuff could be done way more
 </span>
 <span data-rw-start="613.96" data-rw-transcript-version="2">
 effective if you would instead write
 </span>
 <span data-rw-start="618.92" data-rw-transcript-version="2">
 a script.
 </span>
 <span data-rw-start="620.52" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="621.76" data-rw-transcript-version="2">
 and in fact, that's actually what you
 </span>
 <span data-rw-start="622.88" data-rw-transcript-version="2">
 constantly do, and what you constantly
 </span>
 <span data-rw-start="624.2" data-rw-transcript-version="2">
 see, things like hard code do, when it
 </span>
 <span data-rw-start="626.56" data-rw-transcript-version="2">
 writes the bash command. But you can, of
 </span>
 <span data-rw-start="628.44" data-rw-transcript-version="2">
 course, do this with everything, and you
 </span>
 <span data-rw-start="629.8" data-rw-transcript-version="2">
 can do this with MCP, and you should do
 </span>
 <span data-rw-start="631.72" data-rw-transcript-version="2">
 this with MCP. So, what does this mean?
 </span>
</p>
<p>
 <span data-rw-start="634.28" data-rw-transcript-version="2">
 So, what you want, instead of having one
 </span>
 <span data-rw-start="637.32" data-rw-transcript-version="2">
 tool at another, is to give the
 </span>
 <span data-rw-start="639.04" data-rw-transcript-version="2">
 model a reusable tool, provide, like, a
 </span>
 <span data-rw-start="642.12" data-rw-transcript-version="2">
 execution environment, like a V8
 </span>
 <span data-rw-start="644.4" data-rw-transcript-version="2">
 isolate, or a Monty, or something like
 </span>
 <span data-rw-start="646.92" data-rw-transcript-version="2">
 that, or a Lua interpreter, and just
 </span>
 <span data-rw-start="649.48" data-rw-transcript-version="2">
 have the model write the code for you,
 </span>
 <span data-rw-start="651.8" data-rw-transcript-version="2">
 and the model just executes that code,
 </span>
 <span data-rw-start="654.2" data-rw-transcript-version="2">
 and then composes them together. And
 </span>
 <span data-rw-start="656.72" data-rw-transcript-version="2">
 there's a neat little feature in MCP
 </span>
 <span data-rw-start="658.96" data-rw-transcript-version="2">
 called structured output that tells you
 </span>
 <span data-rw-start="661.2" data-rw-transcript-version="2">
 what the return value of the output will
 </span>
 <span data-rw-start="664.48" data-rw-transcript-version="2">
 be, and the model can use this.
 </span>
</p>
<p>
 <span data-rw-start="666.2" data-rw-transcript-version="2">
 Information to figure out type
 </span>
 <span data-rw-start="668.36" data-rw-transcript-version="2">
 information, which then means it can
 </span>
 <span data-rw-start="670.28" data-rw-transcript-version="2">
 really nicely compose these things
 </span>
 <span data-rw-start="672.6" data-rw-transcript-version="2">
 together. And in this example here,
 </span>
 <span data-rw-start="675.08" data-rw-transcript-version="2">
 instead of doing two different calls,
 </span>
 <span data-rw-start="677.32" data-rw-transcript-version="2">
 you do one call, and you can filter that
 </span>
 <span data-rw-start="679.68" data-rw-transcript-version="2">
 the model will automatically
 </span>
 <span data-rw-start="681.88" data-rw-transcript-version="2">
 remove things from a JSON and just
 </span>
 <span data-rw-start="684.08" data-rw-transcript-version="2">
 continue.
 </span>
 <span data-rw-start="686.12" data-rw-transcript-version="2">
 Of course, if you don't have uh
 </span>
 <span data-rw-start="688.32" data-rw-transcript-version="2">
 structured output, you can always just
 </span>
 <span data-rw-start="690.04" data-rw-transcript-version="2">
 ask the model to give you structured
 </span>
 <span data-rw-start="691.4" data-rw-transcript-version="2">
 output
 </span>
 <span data-rw-start="692.68" data-rw-transcript-version="2">
 um
 </span>
 <span data-rw-start="693.56" data-rw-transcript-version="2">
 uh, by just extracting it and saying,
 </span>
 <span data-rw-start="695.6" data-rw-transcript-version="2">
 "Hey, call us cheap model and say, 'I
 </span>
 <span data-rw-start="697.68" data-rw-transcript-version="2">
 want this expected type, give it back to
 </span>
 <span data-rw-start="699.76" data-rw-transcript-version="2">
 me.'
 </span>
 <span data-rw-start="701.36" data-rw-transcript-version="2">
 And bam, you have a type, the
 </span>
 <span data-rw-start="703.24" data-rw-transcript-version="2">
 model can compose things together, and I
 </span>
 <span data-rw-start="704.72" data-rw-transcript-version="2">
 think this is something we're just not
 </span>
 <span data-rw-start="706.6" data-rw-transcript-version="2">
 doing enough yet, and this is I think
 </span>
 <span data-rw-start="708.24" data-rw-transcript-version="2">
 something where we can improve our agent
 </span>
 <span data-rw-start="709.88" data-rw-transcript-version="2">
 harnesses.
 </span>
 <span data-rw-start="711.32" data-rw-transcript-version="2">
 And then last but not least, of course,
 </span>
 <span data-rw-start="713.44" data-rw-transcript-version="2">
 you can just compile and compose these
 </span>
 <span data-rw-start="712.72" data-rw-transcript-version="2">
 Things together with executables, like
 </span>
 <span data-rw-start="714.56" data-rw-transcript-version="2">
 with CLIs, with other components, with
 </span>
 <span data-rw-start="716.88" data-rw-transcript-version="2">
 APIs as well.
 </span>
</p>
<p>
 <span data-rw-start="719.08" data-rw-transcript-version="2">
 Um, next, what we need to do besides the
 </span>
 <span data-rw-start="721.72" data-rw-transcript-version="2">
 client work, which is progressive
 </span>
 <span data-rw-start="723.2" data-rw-transcript-version="2">
 discovery and
 </span>
 <span data-rw-start="725.48" data-rw-transcript-version="2">
 um, programmatic tool calling, we need to
 </span>
 <span data-rw-start="727.88" data-rw-transcript-version="2">
 go and start building properly for
 </span>
 <span data-rw-start="729.92" data-rw-transcript-version="2">
 agents. And that means we all need to
 </span>
 <span data-rw-start="732.16" data-rw-transcript-version="2">
 stop taking REST APIs and put them
 </span>
 <span data-rw-start="734.76" data-rw-transcript-version="2">
 one-to-one
 </span>
 <span data-rw-start="736.24" data-rw-transcript-version="2">
 into
 </span>
 <span data-rw-start="737.88" data-rw-transcript-version="2">
 uh, an MCP server. Every time I see
 </span>
 <span data-rw-start="740.44" data-rw-transcript-version="2">
 someone building another REST to MCP
 </span>
 <span data-rw-start="742.64" data-rw-transcript-version="2">
 server, a conversion tool, I think it's
 </span>
 <span data-rw-start="744.92" data-rw-transcript-version="2">
 a bit
 </span>
 <span data-rw-start="746.52" data-rw-transcript-version="2">
 cringe because I think it's just, it just
 </span>
 <span data-rw-start="748.44" data-rw-transcript-version="2">
 results in horrible things.
 </span>
</p>
<p>
 <span data-rw-start="750.16" data-rw-transcript-version="2">
 Um, and what you should do instead, you
 </span>
 <span data-rw-start="750.16" data-rw-transcript-version="2">
 should design for an agent. Or
 </span>
 <span data-rw-start="751.28" data-rw-transcript-version="2">
 basically, you can start designing for
 </span>
 <span data-rw-start="753.24" data-rw-transcript-version="2">
 you as a human, how you would want to
 </span>
 <span data-rw-start="754.76" data-rw-transcript-version="2">
 interact with this, because that's
 </span>
 <span data-rw-start="756.44" data-rw-transcript-version="2">
 actually a very, very good start for an
 </span>
 <span data-rw-start="759.04" data-rw-transcript-version="2">
 agent.
 </span>
</p>
<p>
 <span data-rw-start="761.68" data-rw-transcript-version="2">
 Together, you should reach, of course,
 </span>
 <span data-rw-start="764.4" data-rw-transcript-version="2">
 for programmatic tool calling, and you
 </span>
 <span data-rw-start="765.72" data-rw-transcript-version="2">
 can do this on the client side, as I
 </span>
 <span data-rw-start="767.48" data-rw-transcript-version="2">
 said before, but you can also do this on
 </span>
 <span data-rw-start="769.4" data-rw-transcript-version="2">
 the server side. The Cloudflare
 </span>
 <span data-rw-start="771.52" data-rw-transcript-version="2">
 MCP server and others like that are
 </span>
 <span data-rw-start="773.839" data-rw-transcript-version="2">
 great examples of how you can have, instead
 </span>
 <span data-rw-start="776.44" data-rw-transcript-version="2">
 of providing tools, provide an execution
 </span>
 <span data-rw-start="779.4" data-rw-transcript-version="2">
 environment to the model and then just
 </span>
 <span data-rw-start="780.96" data-rw-transcript-version="2">
 have them orchestrate things together,
 </span>
 <span data-rw-start="782.8" data-rw-transcript-version="2">
 which again cuts on token usages,
 </span>
 <span data-rw-start="785.04" data-rw-transcript-version="2">
 cuts on latency, and is way more
 </span>
 <span data-rw-start="787.4" data-rw-transcript-version="2">
 powerful in its composition. And then
 </span>
 <span data-rw-start="789.56" data-rw-transcript-version="2">
 last but not least, you should start and
 </span>
 <span data-rw-start="791.8" data-rw-transcript-version="2">
 we should start as server authors to use
 </span>
 <span data-rw-start="793.8" data-rw-transcript-version="2">
 this rich semantics that MCP offers over
 </span>
</p>
<p>
 <span data-rw-start="796.72" data-rw-transcript-version="2">
 alternatives. This means shipping MCP
 </span>
 <span data-rw-start="799.08" data-rw-transcript-version="2">
 applications, it means shipping
 </span>
 <span data-rw-start="801.96" data-rw-transcript-version="2">
 skills over MCP, it means
 </span>
 <span data-rw-start="804.56" data-rw-transcript-version="2">
 um, using things like task and other
 </span>
 <span data-rw-start="806.96" data-rw-transcript-version="2">
 aspects that the protocol offers that
 </span>
 <span data-rw-start="809.08" data-rw-transcript-version="2">
 we're currently slightly underused, or
 </span>
 <span data-rw-start="811.28" data-rw-transcript-version="2">
 things like elicitations.
 </span>
 <span data-rw-start="813.44" data-rw-transcript-version="2">
 Things that only MCP can do for you.
 </span>
 <span data-rw-start="815.92" data-rw-transcript-version="2">
 And of course,
 </span>
 <span data-rw-start="817.839" data-rw-transcript-version="2">
 That's all the work you all need to do,
 </span>
 <span data-rw-start="819.64" data-rw-transcript-version="2">
 and maybe some of our product people
 </span>
 <span data-rw-start="821.16" data-rw-transcript-version="2">
 need to do. We also need to do a lot of
 </span>
 <span data-rw-start="822.96" data-rw-transcript-version="2">
 work on MCP itself. And there are a few
 </span>
 <span data-rw-start="825.24" data-rw-transcript-version="2">
 things down the line that we're going to
 </span>
 <span data-rw-start="827.52" data-rw-transcript-version="2">
 go and have to go and solve.
 </span>
</p>
<p>
 <span data-rw-start="829.68" data-rw-transcript-version="2">
 The number one thing is we need to
 </span>
 <span data-rw-start="831.04" data-rw-transcript-version="2">
 improve the core. There are a few things
 </span>
 <span data-rw-start="833.12" data-rw-transcript-version="2">
 that, as we have developed the protocol
 </span>
 <span data-rw-start="835" data-rw-transcript-version="2">
 over the last year, are just not in
 </span>
 <span data-rw-start="837" data-rw-transcript-version="2">
 a good shape. Number one is that the
 </span>
 <span data-rw-start="839.04" data-rw-transcript-version="2">
 current streamable HTTP is very hard to
 </span>
 <span data-rw-start="841.52" data-rw-transcript-version="2">
 scale if you're a large hyperscaler.
 </span>
</p>
<p>
 <span data-rw-start="844.959" data-rw-transcript-version="2">
 &gt;&gt; [snorts]
 </span>
 <span data-rw-start="844.96" data-rw-transcript-version="2">
 &gt;&gt; And so, we have a proposal from our
 </span>
 <span data-rw-start="847.08" data-rw-transcript-version="2">
 friends at Google,
 </span>
 <span data-rw-start="848.56" data-rw-transcript-version="2">
 who are working on something called a
 </span>
 <span data-rw-start="850.44" data-rw-transcript-version="2">
 stateless transport protocol, which makes
 </span>
 <span data-rw-start="852.839" data-rw-transcript-version="2">
 it significantly easier to just treat
 </span>
 <span data-rw-start="856.2" data-rw-transcript-version="2">
 MCP servers like
 </span>
 <span data-rw-start="858.04" data-rw-transcript-version="2">
 you know, another stateless, uh, rest
 </span>
 <span data-rw-start="860.28" data-rw-transcript-version="2">
 server or something like that, and we are
 </span>
 <span data-rw-start="861.72" data-rw-transcript-version="2">
 used to know how to deploy to like cloud
 </span>
 <span data-rw-start="864.68" data-rw-transcript-version="2">
 runs or Kubernetes and so on. So, that's
 </span>
 <span data-rw-start="867.36" data-rw-transcript-version="2">
 coming down in June and hopefully lining.
 </span>
</p>
<p>
 <span data-rw-start="869.4" data-rw-transcript-version="2">
 In the SDKs very soon.
 </span>
 <span data-rw-start="871.32" data-rw-transcript-version="2">
 In addition, we need to improve our
 </span>
 <span data-rw-start="873.88" data-rw-transcript-version="2">
 asynchronous task primitive, which
 </span>
 <span data-rw-start="876.079" data-rw-transcript-version="2">
 basically is a very fancy way to say we
 </span>
 <span data-rw-start="878.56" data-rw-transcript-version="2">
 just want to have agent-to-agent
 </span>
 <span data-rw-start="879.72" data-rw-transcript-version="2">
 communication. We have a very
 </span>
 <span data-rw-start="881.32" data-rw-transcript-version="2">
 experimental version of the protocol
 </span>
 <span data-rw-start="882.8" data-rw-transcript-version="2">
 that very few clients support, so we're
 </span>
 <span data-rw-start="884.92" data-rw-transcript-version="2">
 going to start building more clients out
 </span>
 <span data-rw-start="887.52" data-rw-transcript-version="2">
 like that, and most importantly, we are
 </span>
 <span data-rw-start="889" data-rw-transcript-version="2">
 improving some of the little semantics
 </span>
 <span data-rw-start="891" data-rw-transcript-version="2">
 that we need to do. We're going to ship
 </span>
 <span data-rw-start="892.72" data-rw-transcript-version="2">
 a TypeScript version SDK version two and
 </span>
 <span data-rw-start="895.28" data-rw-transcript-version="2">
 Python SDK version two based on a lot of
 </span>
 <span data-rw-start="898.44" data-rw-transcript-version="2">
 the lessons learned over the last year.
 </span>
</p>
<p>
 <span data-rw-start="901.52" data-rw-transcript-version="2">
 There's a there’s a
 </span>
 <span data-rw-start="904.079" data-rw-transcript-version="2">
 SDK called fast MCP.
 </span>
 <span data-rw-start="906.6" data-rw-transcript-version="2">
 Who's using fast MCP? Yeah. It's just
 </span>
 <span data-rw-start="909.28" data-rw-transcript-version="2">
 way better than Python SDK that
 </span>
 <span data-rw-start="911" data-rw-transcript-version="2">
 we're shipping, right? And that's on me
 </span>
 <span data-rw-start="912.48" data-rw-transcript-version="2">
 because I wrote the Python SDK.
 </span>
</p>
<p>
 <span data-rw-start="914.92" data-rw-transcript-version="2">
 Um, and so, I have a bunch of people
 </span>
 <span data-rw-start="916.56" data-rw-transcript-version="2">
 who are way better Python developers
 </span>
 <span data-rw-start="917.839" data-rw-transcript-version="2">
 than me helping me write it better. Um, the
 </span>
 <span data-rw-start="920.839" data-rw-transcript-version="2">
 second part is we need to start
 </span>
 <span data-rw-start="923.24" data-rw-transcript-version="2">
 Integrating everywhere. We're going to
 </span>
 <span data-rw-start="924.36" data-rw-transcript-version="2">
 ship, particularly for enterprises,
 </span>
 <span data-rw-start="926.04" data-rw-transcript-version="2">
 something called cross-app access. It's
 </span>
 <span data-rw-start="928.16" data-rw-transcript-version="2">
 a new thing that we're working closely
 </span>
 <span data-rw-start="929.6" data-rw-transcript-version="2">
 together with identity providers, which
 </span>
 <span data-rw-start="931.52" data-rw-transcript-version="2">
 just allows you. It's a very fancy way to
 </span>
 <span data-rw-start="933.36" data-rw-transcript-version="2">
 say,
 </span>
 <span data-rw-start="934.24" data-rw-transcript-version="2">
 once you log in once with your local
 </span>
 <span data-rw-start="935.88" data-rw-transcript-version="2">
 company identity provider, be it a
 </span>
 <span data-rw-start="937.92" data-rw-transcript-version="2">
 Google, or be it an Okta, you will be able
 </span>
 <span data-rw-start="939.64" data-rw-transcript-version="2">
 to just use MCP servers without having
 </span>
 <span data-rw-start="941.4" data-rw-transcript-version="2">
 to re-login. So, it's a bit more
 </span>
 <span data-rw-start="943.04" data-rw-transcript-version="2">
 smooth. In addition, we're going
 </span>
 <span data-rw-start="945.6" data-rw-transcript-version="2">
 to add something called a server
 </span>
 <span data-rw-start="947.6" data-rw-transcript-version="2">
 discovery, by
 </span>
 <span data-rw-start="949.68" data-rw-transcript-version="2">
 specifying how you can discover
 </span>
 <span data-rw-start="953.2" data-rw-transcript-version="2">
 servers on well-known URLs,
 </span>
 <span data-rw-start="955.12" data-rw-transcript-version="2">
 automatically. So, crawlers, browsers,
 </span>
 <span data-rw-start="958.2" data-rw-transcript-version="2">
 um,
 </span>
 <span data-rw-start="958.76" data-rw-transcript-version="2">
 agents can just go to a website and say,
 </span>
 <span data-rw-start="961.24" data-rw-transcript-version="2">
 "Oh, I'm instead of just parsing the
 </span>
 <span data-rw-start="962.64" data-rw-transcript-version="2">
 website, is there also an MCP server I
 </span>
 <span data-rw-start="964.8" data-rw-transcript-version="2">
 can use?" And we will be able to
 </span>
 <span data-rw-start="966.079" data-rw-transcript-version="2">
 automatically discover this.
 </span>
</p>
<p>
 <span data-rw-start="967.8" data-rw-transcript-version="2">
 This is a really cool thing that will
 </span>
 <span data-rw-start="969.16" data-rw-transcript-version="2">
 Come down also in June when we launch
 </span>
 <span data-rw-start="971.36" data-rw-transcript-version="2">
 the next specification
 </span>
 <span data-rw-start="973.16" data-rw-transcript-version="2">
 and will be supported there.
 </span>
</p>
<p>
 <span data-rw-start="974.72" data-rw-transcript-version="2">
 And then last but not least, we're
 </span>
 <span data-rw-start="976.52" data-rw-transcript-version="2">
 starting to use our extension mechanisms
 </span>
 <span data-rw-start="978.76" data-rw-transcript-version="2">
 in MCP, which means that some clients
 </span>
 <span data-rw-start="981.16" data-rw-transcript-version="2">
 will support this, like for example, MCP
 </span>
 <span data-rw-start="983.04" data-rw-transcript-version="2">
 applications will only be supported by
 </span>
 <span data-rw-start="985.959" data-rw-transcript-version="2">
 web-based interfaces, because if you're
 </span>
 <span data-rw-start="988.16" data-rw-transcript-version="2">
 a CLI, you just have a hard time
 </span>
 <span data-rw-start="989.8" data-rw-transcript-version="2">
 rendering HTML, right? Um, and we will do
 </span>
 <span data-rw-start="992.2" data-rw-transcript-version="2">
 more of these extensions. One of the
 </span>
 <span data-rw-start="993.56" data-rw-transcript-version="2">
 most exciting extensions that I think is
 </span>
 <span data-rw-start="995.64" data-rw-transcript-version="2">
 is cool, we're just going to ship skills
 </span>
 <span data-rw-start="997.92" data-rw-transcript-version="2">
 over MCP, because it's very obvious that
 </span>
 <span data-rw-start="1000.12" data-rw-transcript-version="2">
 if you have a large MCP server with tons
 </span>
 <span data-rw-start="1002.079" data-rw-transcript-version="2">
 and tons of tools, you just want to ship
 </span>
 <span data-rw-start="1003.959" data-rw-transcript-version="2">
 the main knowledge with it and say, "Oh,
 </span>
 <span data-rw-start="1006.44" data-rw-transcript-version="2">
 this is how you're supposed to use this.
 </span>
</p>
<p>
 <span data-rw-start="1007.72" data-rw-transcript-version="2">
 This is how you're supposed to use
 </span>
 <span data-rw-start="1008.76" data-rw-transcript-version="2">
 this." And it allows you as a server
 </span>
 <span data-rw-start="1010.52" data-rw-transcript-version="2">
 author to continuously ship updated
 </span>
 <span data-rw-start="1013.32" data-rw-transcript-version="2">
 skills without having to rely on plugin
 </span>
 <span data-rw-start="1015.44" data-rw-transcript-version="2">
 mechanisms on registries and other
 </span>
 <span data-rw-start="1017" data-rw-transcript-version="2">
 stuff.
 </span>
</p>
<p>
 <span data-rw-start="1017.88" data-rw-transcript-version="2">
 So, that's coming down.
 </span>
 <span data-rw-start="1019.44" data-rw-transcript-version="2">
 Um, there's a lot of experimentation
 </span>
 <span data-rw-start="1021.839" data-rw-transcript-version="2">
 from people already in that space. You
 </span>
 <span data-rw-start="1023.44" data-rw-transcript-version="2">
 can already do some of that today if you
 </span>
 <span data-rw-start="1024.92" data-rw-transcript-version="2">
 just give the model a load skills tool.
 </span>
 <span data-rw-start="1027.28" data-rw-transcript-version="2">
 Like, there you can, you can build
 </span>
 <span data-rw-start="1028.48" data-rw-transcript-version="2">
 primitives or versions of this today
 </span>
 <span data-rw-start="1030.24" data-rw-transcript-version="2">
 without having to rely on the semantics,
 </span>
 <span data-rw-start="1032" data-rw-transcript-version="2">
 but, of course, we're going to define the
 </span>
 <span data-rw-start="1033.92" data-rw-transcript-version="2">
 semantics.
 </span>
</p>
<p>
 <span data-rw-start="1035.36" data-rw-transcript-version="2">
 Okay. So, that's for me a long-winded
 </span>
 <span data-rw-start="1037.52" data-rw-transcript-version="2">
 way to think, to say that I think MCP is
 </span>
 <span data-rw-start="1040.12" data-rw-transcript-version="2">
 actually in a really good shape, and I
 </span>
 <span data-rw-start="1041.8" data-rw-transcript-version="2">
 think in this year, we're going to push
 </span>
 <span data-rw-start="1044.8" data-rw-transcript-version="2">
 uh,
 </span>
 <span data-rw-start="1045.439" data-rw-transcript-version="2">
 agents to full connectivity.
 </span>
 <span data-rw-start="1047.88" data-rw-transcript-version="2">
 Um, MCP will continue to play a major,
 </span>
 <span data-rw-start="1050.32" data-rw-transcript-version="2">
 major, major role. And we want, of
 </span>
 <span data-rw-start="1052.72" data-rw-transcript-version="2">
 course, your feedback. We are very open
 </span>
 <span data-rw-start="1054.28" data-rw-transcript-version="2">
 community. We just have created a
 </span>
 <span data-rw-start="1055.8" data-rw-transcript-version="2">
 foundation. We're mostly running as an
 </span>
 <span data-rw-start="1058.48" data-rw-transcript-version="2">
 open-source community with a Discord,
 </span>
 <span data-rw-start="1060.52" data-rw-transcript-version="2">
 with issues. Um, just come to us and tell
 </span>
 <span data-rw-start="1063.04" data-rw-transcript-version="2">
 us where we are wrong, what are
 </span>
 <span data-rw-start="1065" data-rw-transcript-version="2">
 We’re getting right,
 </span>
 <span data-rw-start="1066.92" data-rw-transcript-version="2">
 uh, so that we can
 </span>
 <span data-rw-start="1069.32" data-rw-transcript-version="2">
 improve this on a continuous basis.
 </span>
</p>
<p>
 <span data-rw-start="1069.32" data-rw-transcript-version="2">
 So, 2026, I think is all about
 </span>
 <span data-rw-start="1071.08" data-rw-transcript-version="2">
 connectivity, and the best agents use
 </span>
 <span data-rw-start="1074.08" data-rw-transcript-version="2">
 every available method. Like they will
 </span>
 <span data-rw-start="1075.4" data-rw-transcript-version="2">
 use computer use, they will use CLIs,
 </span>
 <span data-rw-start="1077.12" data-rw-transcript-version="2">
 they will use MCPs, and they will use
 </span>
 <span data-rw-start="1079.36" data-rw-transcript-version="2">
 will use skills.
 </span>
</p>
<p>
 <span data-rw-start="1081.04" data-rw-transcript-version="2">
 Because they want to have a wide variety
 </span>
 <span data-rw-start="1083.2" data-rw-transcript-version="2">
 of things they can do, and then they can
 </span>
 <span data-rw-start="1085.36" data-rw-transcript-version="2">
 ship cool stuff like this,
 </span>
 <span data-rw-start="1087.8" data-rw-transcript-version="2">
 uh,
 </span>
 <span data-rw-start="1088.36" data-rw-transcript-version="2">
 which is
 </span>
 <span data-rw-start="1090" data-rw-transcript-version="2">
 uh,
 </span>
 <span data-rw-start="1091.76" data-rw-transcript-version="2">
 one of the product features we shipped
 </span>
 <span data-rw-start="1093.12" data-rw-transcript-version="2">
 recently.
 </span>
 <span data-rw-start="1094.28" data-rw-transcript-version="2">
 Uh, under the hood, it's nothing but an
 </span>
 <span data-rw-start="1096.72" data-rw-transcript-version="2">
 MCP application
 </span>
 <span data-rw-start="1098.56" data-rw-transcript-version="2">
 uh, that renders stuff, right?
 </span>
</p>
<p>
 <span data-rw-start="1101.32" data-rw-transcript-version="2">
 Cool.
 </span>
 <span data-rw-start="1103.92" data-rw-transcript-version="2">
 So, we can now look at,
 </span>
 <span data-rw-start="1105.52" data-rw-transcript-version="2">
 uh, the model
 </span>
 <span data-rw-start="1107.56" data-rw-transcript-version="2">
 writing graphs.
 </span>
 <span data-rw-start="1109.04" data-rw-transcript-version="2">
 Anyway,
 </span>
 <span data-rw-start="1109.04" data-rw-transcript-version="2">
 thank you.
 </span>
</p>
<p>
 <span data-rw-start="1118.097" data-rw-transcript-version="2">
 &gt;&gt; [music]
 </span>
</p>