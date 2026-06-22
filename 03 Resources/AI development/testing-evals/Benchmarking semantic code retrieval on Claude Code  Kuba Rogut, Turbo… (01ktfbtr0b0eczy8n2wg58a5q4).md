---
title: "Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer"
source: "https://www.youtube.com/watch?v=zKk7sDMGDEQ"
author: "AI Engineer"
published: 2026-06-03
created: 2026-06-06
description: "By default, Claude Code wastes one in every three file reads. Add windowed"
tags:
  - to-process
  - testing-evals
---

[music] >> Hi everyone. Welcome to benchmarking semantic search or semantic code retrieval on cloud code. My name is Kuba. I'm here from Turbo Puffer. For those unfamiliar with Turbo Puffer, we are a serverless full text and vector search database built from first principles on top of object storage. We serve some of the fastest 

growing AI companies in the world and if you'd like to know more about the talk or any question about Turbo Puffer or anything, just find feel free to find me after. So let's get started. So for those of you who are unaware, cloud code by default or I mean yeah, by default doesn't use semantic code search. There's actually a tweet from Boris. Those unfamiliar with Boris, he's actually like the founding father of cloud code and he talks about how cloud the early versions of cloud code did actually use semantic search with a local vector DB, but they just kind of found agentic search which is actually you know, grepping through your file system kind of worked better and you 

know, seems to work simpler for for cloud code. However, one of Turbo Puffer's customers actually fun fact, one of our very first customer is Cursor does use semantic code search and does index code bases into Turbo Puffer and you may think like this seems like a lot of work and it kind of is, but the reason they do this is because they see real performance gains because of this. They have this amazing blog post about their semantic search. They also have one about indexing code bases which I highly recommend as well. But you can see on the right the kind of 

performance gains they see with their composer model is like 24% increase in relative improvement in answer accuracy and I think it's like 12 and a half or 13% across all models and you know, I this benchmark came up before composer two, but you can probably imagine there's some sort of similar performance gains with that that new model as well. And in the bottom right you can see this is from to the same blog post. They talk about how in they perform an online AB test where they found that adding semantic either allowing or disallowing 

semantic code search led to like a 2.6% increase in code retention in large code bases and then 2.2% decrease in dissatisfied user requests. And you may also think like these numbers seem kind of small like what 2.6% 2.2%? Well, keep in mind that you know, out of 100 queries not all queries will ever really need semantic search or like benefit from it. So these they even state in the blog post that these numbers look small because not every you know, you can imagine a very simple tool call or very simple query would not really use semantic search. 

So what we think about here at Turbo Puffer and why we kind of really think vector search and why Cursor probably sees this like real performance gain is we think about how embeddings are cache compute and you can also you know, what is what do you mean cache compute? This sounds like a bunch of baloney you're throwing at me. You know, if we were like walk through like a cloud code trace and like a Cursor type trace of kind of the same thing, you can imagine that on the left side this kind of like a you know, grepping through the file system or what they call agentic search. How it just 

has like grep through this is for finding metadata filtering and understanding it in your code base. That's essentially grep through, read the files, grep through more if it doesn't find the right things and again, this is repeated on every session across you know, every agent running in for the same code base so that even if you're asking the same question or trying to do the same thing multiple times, you always have to do this compute again and you can see like I mean in this case 6,000 tokens isn't a lot in one time, but across every session and every agent this really starts to add up. And if we you know, on 

the right of this is more of a like like Cursor style or Cursor level trace where you have this upfront cost where you have to chunk embed and index the code base, but then you would essentially have this cache of the semantic meaning so that when a when a agent wants to understand you know, where or how does metadata filtering work, it can simply query you know, how is metadata filtered and get a lot get the chunks it needs and kind of the understanding it needs a lot faster and with token savings and again, this doesn't it's not a lot of savings in one time, but we all you know, we're 

not really running one agent anymore. Like I'm running like three at one time. So there's definitely some long-term savings. So what we did is we built a simple CLI tool for cloud code. We call it Turbo Grep. It's essentially you can imagine it's just a simple way of using a tree splitter library to essentially parse through your code base, chunk it, embed it using the Voyage code model and then upload it to Turbo Puffer. This is just a simple file system walk through. There is an 

open source library for the V1 version and then soon the V2 version will be open sourced. Here's a little video of example a tool call trace for a cloud code where you'll see it will call the T Puffer tool. Now it's called T Puffer search password reset token generator. This is in the Django repo. This is one of the repos I was testing it on and you can see that it gets the contents and then is able to kind of give the full explanation to the user. 

And you know, it's very easy to say like oh this works better, but the important thing is obviously benchmark it. Let's see for real what what how much better does it work? Cursor has their own internal context bench and there's this paper this public paper called context bench where essentially the benchmark is not really testing whether or not the coding agent solved or didn't solve a problem. It tests when it in the process of solving the problem, did it find certain files? Did it find certain lines and it find certain symbols? Because they you 

know, they kind of have this this thesis that like it you know, it's also important how you get there not just like the end goal. The process really matters for understanding like are agents actually looking for the right files? So essentially it's a human labeled data set of like in order to complete this task they the agent should have looked at this file, these few lines and these few symbols in order to like actually complete the task well. And I tested with three conditions. Essentially raw cloud code out of the box. Then I tested it with cloud code with a 

max of 50 line reads at a time and then the same thing with a windowed reads with the T Puffer search tool. You may ask me like why this like 50 line read thing limit? It's because it it became really noisy really fast if it's just reading like long files. It's really hard to like understand and get a difference because it all if it just reads a whole like a thousand line file, it doesn't really make a lot of difference in the numbers. So we'll start with the first result of it. This is precision. Precision is essentially the 

the measure of of how many files did it read like in its total process? How many of them were actually golden files? So if there was if if cloud read 10 files and eight of them were needed, it hits 80% precision. You can see the baseline it hit like 65% precision, 33% on line precision and 43% on symbol and it kind of goes up as we add windowed grep and then windowed grep plus semantic search got it to like 87% file precision for example. And this is also due to the fact like cloud code by default like it's a really exploratory. It loves to read as much as 

it can and like try to read everything for example and it kind of shows up in the 65% precision. And you know, it's hard to like translate these numbers, but a more like English or like human version of it is that you know, cloud code one in every three file reads is actually just a completely wasted file and with windowed grep it was one in five reads was a irrelevant file and then with semantic search there's only one in eight files was a you know, quote unquote wasted or irrelevant file and it kind of like scales up as you kind of add these tools. 

And you know, obviously this this is already like pretty good. Then we have recall. Recall is essentially how many of the needed files did it find? So for example, if there was 10 files in the task that it should have found, if cloud found five of them five files in its total trajectory and only three of them were actually these golden files, it would hit 30% recall. By default again, cloud code actually does win the file recall and again, part of this is because it just loves to explore every single file it can. Then we have line recall where it drops 

a lot more. This is kind of because it loved to read a lot of files, but also read to really read a lot of files that didn't have a lot of golden context lines. So you can kind of see that even though it did explore a lot, it also kind of explored the wrong things a lot and then with grep and grep plus semantic or windowed grep and windowed grep plus semantic search kind of have the same recall. You can kind of see on the right like kind of the what happened with the behavior between these three conditions. And you may be thinking like well, you know, semantic search didn't really like add improvements here. Like what what 

went wrong? Like actually some decreases. And we can like dig in a little further into the recall numbers for certain tasks. This is across 50 tasks by default, but if we break it down into where semantic search won you know, quote unquote won and where just like windowed grep won, we see some stark differences between like certain tasks performed a lot better with semantic search allowed and then certain tasks performed a lot better with with no semantic search and this kind of proves you know, certain tasks requires different types of tools. For example, 

when semantic search won, it was really good at finding a lot of behavior adjacent files that didn't have the same kind of keywords. For example, it was like I think one example off top of my head was we're trying to like it was a multi like first handle lots of different ORMs that have to like handle across different libraries and it didn't by default the keyword search didn't by default find all of them, but behaviors semantic search was able to kind of like understand these are all related files. And then grep won when it was really good at just the task was a lot of it like tracing through imports and if it like was able to find the keywords in 

like the first or second tool call, it was able to like just keyword search through that and find the relevant files. So again, it's like two different types of how to find files, but they kind of lead to like really different results. So in summary like what does this mean? Well, we like we saw semantic search like did boost precision quite a bit and we like kind of understand like grep and semantic search kind of find different code different ways. And an interesting thing to note as well was um these numbers weren't as great as 

Cursor's because part of like part of Claude code is it's built for just grepping. Like that's that's what Anthropic kind of focuses on. Like it's not built to under like to really understand like when to call semantic search or how to call it. Uh we kind of like add as an extra tool and it's like, "Hey, like here's this cool tool. You probably should use it sometimes." But it's very hard for it to have a true understanding of when to use it, why to use it uh versus like for example Cursor's composer they understand this is a built-in tool that um it knows when and how to use it and 

that's why they saw it's like 23 and 1/2 per uh percent uh performance gain. Uh so like in summary, uh you know, we think long-term winners were like kind of provide these lightweight tools to find the right context in various different ways. I think it's something important to think about. Uh you can't just like grep through everything unfortunately in a file system. Uh we think there's a lot of different ways to access lots of different types of information. Uh and the people that provide these like easy tools to provide to shrink down these billion context windows into the right million uh will win in the long term. 

Um that's the general talk. Thank you. If you have any questions, feel free to come up. >> [applause] >> I have my own idea of what semantic search is, but could you define what you what's your definition is of semantic search? >> Sure. Uh so this was just uh just doing vector search. It was just performing vector search using embedding it using Voyage's code model and then just embedding the the the query um query sentences or query tokens and just sending them back to to Turbo puffer. Yeah. Uh sorry, the 

uh embedding model Uh Voyage code three. Okay. And which vector DB? Turbo puffer. Yeah. >> Sorry. Uh no worries. Yeah, yeah. Yeah, for those for those who are unfamiliar with Turbo puffer, we are the we are the vector database that powers companies like Cursor, Anthropic, Notion. So when you use something like Cursor uh you have by proxy used Turbo puffer. Um so you may know us just not by name, I guess. I was just going to ask 

You may not have a benchmark for this, but how does it perform on code? Oh, that's that's tough. I mean it's hard to say >> better or is semantic better if the code's like a mess and you need to go and sort it out? Uh so I think it works best when there's a lot of like comments on code uh because it kind of finds that semantic meaning. >> like the documentation is kind of inline. Yeah, if it's like inline documentation, that was like a big um boost. I believe one of the repos I remember like looking through some directories and like asking Claude be 

like, "Why did it perform so well here versus not?" And it was one of it kind of explains me like um when I was looking through as well like those with like really good comments, for example, just like comments above the function, it's able to like really understand a lot more cuz you you kind of give this context to the model and the embedding model. So then it can like actually search better. Um cuz that's that's part of it. Like the the embedding it and is not the hard part. It's like figuring out what meaning really is of that chunk. Yeah. Yeah, you may have you you've mentioned 

some of it now, but of course semantic search is just similarity search. So if your query it doesn't really match the format of what you're querying against then you get some kind of innate distance. Do you do any kind of preprocessing on what your of the target data before you like do you do an parent-child where the parent is query-ish and the child is the real code or how do you >> In in this case it was just simple just just the code. Yeah, just the raw code just as a thing, but 

I can't speak for like how these more complicated and sophisticated customers use this, but I can imagine it's definitely something of providing not just code level meaning, but you know, as you said at least a parent-child relationship of like authentication flow, like that could be a good query to do a similarity search against, but the code itself is more like raw. Yeah. Yeah. Like Cursor has their own embedding model, which I think kind of helps with this of like how do you translate code into more of like a human level query. And I mean they're kind of been experts on that. I can't speak for how they do it, but I just know they do do it. 

I think they actually do what you said like they create fake comments on top of of your code and then embed the code with the comments. Yeah. So that's how they can have like their high recall when they So they add they kind of inject comments. Yes. Yeah, it's something that I think definitely could work. Yeah. In the back? Yeah. I was going to ask like how do you see uh I guess the vector database kind of working with the partners 

and how like when do you code like long-term or need to reduce the size I mean I think it depends. Like obviously the easiest way like people love grepping because it's zero cost. Like if you're able to like download everything to your local file system and just like grep through it, like yeah, that works. Um I think vector DBs are built for actually like multiplayer and like this like super maybe in a sense like hard to understand or uh complicated relationships between lots of data. For example, like a knowledge base like a Notion, like you 

can imagine kind of hard to like really grep through that really easily on your local machine. Like it's in a sense best to like have that vectorize uh for the agents. Um and even stuff like we have customers doing stuff like with multimodal data. You can't really grep through a video file. You can't grep through an audio file. You can't grep through an an image file. Like maybe you can glob on the on the file name, um but like get a true understanding of kind of multimodal data as well is that something that we find a lot of customers are doing. Um so it just kind of depends on the workload and um I I yeah, if you if you're hitting 

like at some sort of even like miniature scale like a vector DB kind of like helps offload a lot of this this work into like you know, cache computer cache this semantic meaning. Any other questions? Okay. Thank you all. >> [applause] 

<p>
 <span data-rw-start="7.205" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="15.12" data-rw-transcript-version="2">
 &gt;&gt; Hi everyone. Welcome to benchmarking semantic search or semantic code retrieval on cloud code.
 </span>
 <span data-rw-start="17.24" data-rw-transcript-version="2">
 My name is Kuba. I'm here from Turbo Puffer.
 </span>
 <span data-rw-start="18.52" data-rw-transcript-version="2">
 For those unfamiliar with Turbo Puffer, we are a serverless full text and vector search database built from first principles on top of object storage.
 </span>
 <span data-rw-start="20.28" data-rw-transcript-version="2">
 We serve some of the fastest growing AI companies in the world, and if you'd like to know more about the talk or any questions about Turbo Puffer or anything, just feel free to find me afterwards.
 </span>
 <span data-rw-start="22.2" data-rw-transcript-version="2">
 So, let's get started.
 </span>
</p>
<p>
 <span data-rw-start="40.12" data-rw-transcript-version="2">
 So, for those of you who are unaware, cloud code by default, or I mean, yeah, doesn't, doesn't use semantic code search.
 </span>
 <span data-rw-start="42.24" data-rw-transcript-version="2">
 There's actually a tweet from Boris. Those unfamiliar with Boris, he's actually like the founding father of cloud code.
 </span>
 <span data-rw-start="44.12" data-rw-transcript-version="2">
 And he talks about how cloud, the early versions of cloud code did actually use semantic search with a
 </span>
 <span data-rw-start="55.2" data-rw-transcript-version="2">
 Local vector DB, but they just kind of
 </span>
 <span data-rw-start="57" data-rw-transcript-version="2">
 found agentic search, which is actually
 </span>
 <span data-rw-start="58.52" data-rw-transcript-version="2">
 you know, grepping through your file
 </span>
 <span data-rw-start="59.44" data-rw-transcript-version="2">
 system, kind of worked better and you
 </span>
 <span data-rw-start="61.56" data-rw-transcript-version="2">
 know, seems to work simpler for, for
 </span>
 <span data-rw-start="62.92" data-rw-transcript-version="2">
 cloud code.
 </span>
</p>
<p>
 <span data-rw-start="64.519" data-rw-transcript-version="2">
 However,
 </span>
 <span data-rw-start="65.48" data-rw-transcript-version="2">
 one of Turbo Puffer's customers actually
 </span>
 <span data-rw-start="67.84" data-rw-transcript-version="2">
 fun fact, one of our very first customers
 </span>
 <span data-rw-start="69.24" data-rw-transcript-version="2">
 is Cursor.
 </span>
 <span data-rw-start="70.4" data-rw-transcript-version="2">
 They do use semantic code search and
 </span>
 <span data-rw-start="72.32" data-rw-transcript-version="2">
 index code bases into Turbo Puffer, and
 </span>
 <span data-rw-start="75.08" data-rw-transcript-version="2">
 you may think, like, this seems like a lot
 </span>
 <span data-rw-start="76.4" data-rw-transcript-version="2">
 of work, and it kind of is, but the
 </span>
 <span data-rw-start="78.48" data-rw-transcript-version="2">
 reason they do this is because they see
 </span>
 <span data-rw-start="80.72" data-rw-transcript-version="2">
 real performance gains because of this.
 </span>
</p>
<p>
 <span data-rw-start="83.04" data-rw-transcript-version="2">
 They have this amazing blog post about
 </span>
 <span data-rw-start="85.44" data-rw-transcript-version="2">
 their semantic search. They also have
 </span>
 <span data-rw-start="86.44" data-rw-transcript-version="2">
 one about indexing code bases, which I
 </span>
 <span data-rw-start="88.04" data-rw-transcript-version="2">
 highly recommend as well.
 </span>
 <span data-rw-start="89.48" data-rw-transcript-version="2">
 But you can see, on the right, the kind of
 </span>
 <span data-rw-start="91.16" data-rw-transcript-version="2">
 performance gains they see with their
 </span>
 <span data-rw-start="92.6" data-rw-transcript-version="2">
 composer model, which is like a 24% increase in
 </span>
 <span data-rw-start="95.76" data-rw-transcript-version="2">
 relative improvement in answer accuracy,
 </span>
 <span data-rw-start="97.88" data-rw-transcript-version="2">
 and I think it's like 12.5% or
 </span>
 <span data-rw-start="99.4" data-rw-transcript-version="2">
 13% across all models and, you know, I
 </span>
 <span data-rw-start="102.52" data-rw-transcript-version="2">
 this benchmark came up before composer
 </span>
 <span data-rw-start="104.96" data-rw-transcript-version="2">
 two, but you can probably imagine
 </span>
 <span data-rw-start="106.44" data-rw-transcript-version="2">
 there's some sort of similar performance
 </span>
 <span data-rw-start="107.64" data-rw-transcript-version="2">
 gains with that new model as well.
 </span>
</p>
<p>
 <span data-rw-start="109.56" data-rw-transcript-version="2">
 And in the bottom right, you can see this
 </span>
 <span data-rw-start="111.44" data-rw-transcript-version="2">
 is from the same blog post. They talk
 </span>
 <span data-rw-start="113.96" data-rw-transcript-version="2">
 about how in they perform an online AB
 </span>
 <span data-rw-start="116.12" data-rw-transcript-version="2">
 test, where they found that adding
 </span>
 <span data-rw-start="117.8" data-rw-transcript-version="2">
 semantic, either allowing or disallowing
 </span>
 <span data-rw-start="120.04" data-rw-transcript-version="2">
 semantic code search, led to a like a 2.6%
 </span>
 <span data-rw-start="123.2" data-rw-transcript-version="2">
 increase in code retention in large code
 </span>
 <span data-rw-start="124.64" data-rw-transcript-version="2">
 bases, and then a 2.2% decrease in
 </span>
 <span data-rw-start="127.6" data-rw-transcript-version="2">
 dissatisfied user requests. And you may
 </span>
 <span data-rw-start="129.6" data-rw-transcript-version="2">
 also think, like, these numbers seem kind
 </span>
 <span data-rw-start="131.32" data-rw-transcript-version="2">
 of small. Like, what, 2.6%, 2.2%?
 </span>
 <span data-rw-start="134.8" data-rw-transcript-version="2">
 Well, keep in mind that, you know, out of
 </span>
 <span data-rw-start="136.6" data-rw-transcript-version="2">
 100 queries, not all queries will ever
 </span>
 <span data-rw-start="138.64" data-rw-transcript-version="2">
 really need semantic search or like,
 </span>
 <span data-rw-start="140.04" data-rw-transcript-version="2">
 benefit from it. So, these, they even
 </span>
 <span data-rw-start="142.16" data-rw-transcript-version="2">
 state in the blog post that
 </span>
 <span data-rw-start="144.08" data-rw-transcript-version="2">
 these numbers look small because not
 </span>
 <span data-rw-start="145.92" data-rw-transcript-version="2">
 every, you know, you can imagine a very
 </span>
 <span data-rw-start="147.48" data-rw-transcript-version="2">
 simple tool call or very simple query
 </span>
 <span data-rw-start="149.36" data-rw-transcript-version="2">
 would not really use semantic search.
 </span>
</p>
<p>
 <span data-rw-start="151.32" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="153.4" data-rw-transcript-version="2">
 what we think about here at Turbo Puffer
 </span>
 <span data-rw-start="154.64" data-rw-transcript-version="2">
 and why we kind of really think vector
 </span>
 <span data-rw-start="157.96" data-rw-transcript-version="2">
 search and why Cursor probably sees this
 </span>
 <span data-rw-start="159.6" data-rw-transcript-version="2">
 like real performance gain is, we think
 </span>
 <span data-rw-start="162" data-rw-transcript-version="2">
 about how embeddings are cache compute,
 </span>
 <span data-rw-start="163.96" data-rw-transcript-version="2">
 and you can also, you know, what is, what
 </span>
 <span data-rw-start="165.8" data-rw-transcript-version="2">
 do you mean cache compute? This sounds
 </span>
 <span data-rw-start="166.92" data-rw-transcript-version="2">
 like a bunch of baloney you're throwing
 </span>
 <span data-rw-start="168.16" data-rw-transcript-version="2">
 at me.
 </span>
</p>
<p>
 <span data-rw-start="169.84" data-rw-transcript-version="2">
 You know, if we were like walk through
 </span>
 <span data-rw-start="170.64" data-rw-transcript-version="2">
 like a cloud code trace and like a
 </span>
 <span data-rw-start="172" data-rw-transcript-version="2">
 Cursor type trace of kind of the same
 </span>
 <span data-rw-start="174.04" data-rw-transcript-version="2">
 thing, you can imagine that on the left
 </span>
 <span data-rw-start="176.12" data-rw-transcript-version="2">
 side this kind of like a, you know,
 </span>
 <span data-rw-start="177.08" data-rw-transcript-version="2">
 grepping through the file system or what
 </span>
 <span data-rw-start="178.56" data-rw-transcript-version="2">
 they call agentic search. How it just
 </span>
 <span data-rw-start="181.04" data-rw-transcript-version="2">
 has like grep through, this is for
 </span>
 <span data-rw-start="182.84" data-rw-transcript-version="2">
 finding metadata, filtering, and
 </span>
 <span data-rw-start="184.12" data-rw-transcript-version="2">
 understanding it in your code base.
 </span>
</p>
<p>
 <span data-rw-start="185.64" data-rw-transcript-version="2">
 That's essentially grep through, read
 </span>
 <span data-rw-start="187.36" data-rw-transcript-version="2">
 the files, grep through more if it
 </span>
 <span data-rw-start="189.24" data-rw-transcript-version="2">
 doesn't find the right things, and again,
 </span>
 <span data-rw-start="191" data-rw-transcript-version="2">
 this is repeated on every session across
 </span>
 <span data-rw-start="193.2" data-rw-transcript-version="2">
 you know, every agent.
 </span>
</p>
<p>
 <span data-rw-start="195.08" data-rw-transcript-version="2">
 Running in for the same code base, so
 </span>
 <span data-rw-start="197.68" data-rw-transcript-version="2">
 that even if you're asking the same
 </span>
 <span data-rw-start="199.12" data-rw-transcript-version="2">
 question or trying to do the same thing
 </span>
 <span data-rw-start="200.2" data-rw-transcript-version="2">
 multiple times, you always have to do
 </span>
 <span data-rw-start="202.04" data-rw-transcript-version="2">
 this compute again, and you can see like
 </span>
 <span data-rw-start="203.68" data-rw-transcript-version="2">
 I mean, in this case, 6,000 tokens isn't a
 </span>
 <span data-rw-start="205.36" data-rw-transcript-version="2">
 lot in one time, but across every
 </span>
 <span data-rw-start="207.16" data-rw-transcript-version="2">
 session and every agent, this really
 </span>
 <span data-rw-start="208.4" data-rw-transcript-version="2">
 starts to add up. And if we, you know, on
 </span>
 <span data-rw-start="210.64" data-rw-transcript-version="2">
 the right of this is more of a like, like
 </span>
 <span data-rw-start="211.88" data-rw-transcript-version="2">
 Cursor style or cursor level trace, where
 </span>
 <span data-rw-start="214" data-rw-transcript-version="2">
 you have this upfront cost, where you
 </span>
 <span data-rw-start="215.24" data-rw-transcript-version="2">
 have to chunk, embed, and index the code
 </span>
 <span data-rw-start="216.96" data-rw-transcript-version="2">
 base. But then, you would essentially
 </span>
 <span data-rw-start="218.56" data-rw-transcript-version="2">
 have this cache of the semantic meaning,
 </span>
 <span data-rw-start="220.8" data-rw-transcript-version="2">
 so that when an agent wants to
 </span>
 <span data-rw-start="223.04" data-rw-transcript-version="2">
 understand, you know, where or how does
 </span>
 <span data-rw-start="225.16" data-rw-transcript-version="2">
 metadata filtering work,
 </span>
 <span data-rw-start="226.76" data-rw-transcript-version="2">
 it can simply query, you know, how is
 </span>
 <span data-rw-start="228.08" data-rw-transcript-version="2">
 metadata filtered and get the chunks it needs,
 </span>
 <span data-rw-start="231" data-rw-transcript-version="2">
 and kind of the understanding it needs,
 </span>
 <span data-rw-start="232.44" data-rw-transcript-version="2">
 a lot faster, and
 </span>
 <span data-rw-start="234.88" data-rw-transcript-version="2">
 with token savings. And again,
 </span>
 <span data-rw-start="236.6" data-rw-transcript-version="2">
 this isn't a lot of savings in one time, but we, you know, we're
 </span>
 <span data-rw-start="241.36" data-rw-transcript-version="2">
 Not really running one agent anymore.
 </span>
</p>
<p>
 <span data-rw-start="242.92" data-rw-transcript-version="2">
 Like, I'm running like three at one time.
 </span>
 <span data-rw-start="244.28" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="245.52" data-rw-transcript-version="2">
 there's definitely some long-term
 </span>
 <span data-rw-start="247.08" data-rw-transcript-version="2">
 savings.
 </span>
 <span data-rw-start="248.36" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="249.68" data-rw-transcript-version="2">
 what we did is, we built a simple CLI
 </span>
 <span data-rw-start="251.6" data-rw-transcript-version="2">
 tool for cloud code. We call it Turbo
 </span>
 <span data-rw-start="253.52" data-rw-transcript-version="2">
 Grep.
 </span>
 <span data-rw-start="254.92" data-rw-transcript-version="2">
 It's essentially, you can imagine, it's
 </span>
 <span data-rw-start="256.32" data-rw-transcript-version="2">
 just a simple way of
 </span>
 <span data-rw-start="258.48" data-rw-transcript-version="2">
 using a tree splitter library to
 </span>
 <span data-rw-start="260.12" data-rw-transcript-version="2">
 essentially parse through your code
 </span>
 <span data-rw-start="261" data-rw-transcript-version="2">
 base,
 </span>
 <span data-rw-start="261.959" data-rw-transcript-version="2">
 chunk it, embed it using the Voyage code
 </span>
 <span data-rw-start="264.2" data-rw-transcript-version="2">
 model, and then upload it to Turbo
 </span>
 <span data-rw-start="265.48" data-rw-transcript-version="2">
 Puffer.
 </span>
 <span data-rw-start="267" data-rw-transcript-version="2">
 This is just a simple
 </span>
 <span data-rw-start="269.08" data-rw-transcript-version="2">
 file system walk through. There is an
 </span>
 <span data-rw-start="270.76" data-rw-transcript-version="2">
 open source library for the V1 version,
 </span>
 <span data-rw-start="272.8" data-rw-transcript-version="2">
 and then soon the V2 version will be
 </span>
 <span data-rw-start="275.48" data-rw-transcript-version="2">
 open sourced.
 </span>
 <span data-rw-start="278.52" data-rw-transcript-version="2">
 Here's a little video of an example, a
 </span>
 <span data-rw-start="281.6" data-rw-transcript-version="2">
 tool call trace for a cloud code where
 </span>
 <span data-rw-start="283.28" data-rw-transcript-version="2">
 you'll see.
 </span>
</p>
<p>
 <span data-rw-start="284.64" data-rw-transcript-version="2">
 It will call the T Puffer tool. Now,
 </span>
 <span data-rw-start="287.24" data-rw-transcript-version="2">
 it's called T Puffer search password reset token generator.
 </span>
 <span data-rw-start="289.08" data-rw-transcript-version="2">
 This is in the Django repo.
 </span>
 <span data-rw-start="291.12" data-rw-transcript-version="2">
 This is one of the repos I was testing it on,
 </span>
 <span data-rw-start="293.04" data-rw-transcript-version="2">
 and you can see that it gets the contents and then is able to
 </span>
 <span data-rw-start="295.28" data-rw-transcript-version="2">
 kind of give the full explanation to the user.
 </span>
 <span data-rw-start="297" data-rw-transcript-version="2">
 And
 </span>
 <span data-rw-start="302.96" data-rw-transcript-version="2">
 you know, it's very easy to say like, oh,
 </span>
 <span data-rw-start="304.44" data-rw-transcript-version="2">
 this works better, but the important thing is obviously benchmarking it.
 </span>
</p>
<p>
 <span data-rw-start="306.28" data-rw-transcript-version="2">
 Let's
 </span>
 <span data-rw-start="307.68" data-rw-transcript-version="2">
 see for real how much better
 </span>
 <span data-rw-start="309.96" data-rw-transcript-version="2">
 it works. Cursor has their own
 </span>
 <span data-rw-start="311.64" data-rw-transcript-version="2">
 internal
 </span>
 <span data-rw-start="312.68" data-rw-transcript-version="2">
 context bench, and there's this paper
 </span>
 <span data-rw-start="314.68" data-rw-transcript-version="2">
 this public paper called context bench,
 </span>
 <span data-rw-start="316.8" data-rw-transcript-version="2">
 where essentially the benchmark is not
 </span>
 <span data-rw-start="318.64" data-rw-transcript-version="2">
 really testing whether or not the coding
 </span>
 <span data-rw-start="320.16" data-rw-transcript-version="2">
 agent solved or didn't solve a problem.
 </span>
</p>
<p>
 <span data-rw-start="322.32" data-rw-transcript-version="2">
 It tests when it, in the process of
 </span>
 <span data-rw-start="325.68" data-rw-transcript-version="2">
 solving the problem, did it find certain
 </span>
 <span data-rw-start="327.68" data-rw-transcript-version="2">
 files? Did it find certain lines, and it
 </span>
 <span data-rw-start="329.92" data-rw-transcript-version="2">
 find certain symbols? Because they, you
 </span>
 <span data-rw-start="332" data-rw-transcript-version="2">
 know, they kind of have this, this thesis.
 </span>
</p>
<p>
 <span data-rw-start="334.12" data-rw-transcript-version="2">
 That, like,
 </span>
 <span data-rw-start="335.24" data-rw-transcript-version="2">
 it's also important how you
 </span>
 <span data-rw-start="337.12" data-rw-transcript-version="2">
 get there, not just
 </span>
 <span data-rw-start="338.64" data-rw-transcript-version="2">
 the end goal. The process really
 </span>
 <span data-rw-start="340.08" data-rw-transcript-version="2">
 matters for understanding if
 </span>
 <span data-rw-start="341.52" data-rw-transcript-version="2">
 agents are actually looking for the right
 </span>
 <span data-rw-start="343.04" data-rw-transcript-version="2">
 files. So, essentially, it's a human
 </span>
 <span data-rw-start="345.04" data-rw-transcript-version="2">
 labeled dataset, in order to
 </span>
 <span data-rw-start="346.64" data-rw-transcript-version="2">
 complete this task, the agent should
 </span>
 <span data-rw-start="348.4" data-rw-transcript-version="2">
 have looked at this file, these few
 </span>
 <span data-rw-start="350.04" data-rw-transcript-version="2">
 lines, and these few symbols to
 </span>
 <span data-rw-start="351.96" data-rw-transcript-version="2">
 actually complete the task well.
 </span>
</p>
<p>
 <span data-rw-start="353.96" data-rw-transcript-version="2">
 And I tested with three conditions.
 </span>
 <span data-rw-start="355.76" data-rw-transcript-version="2">
 Essentially, raw cloud code out of the
 </span>
 <span data-rw-start="357.2" data-rw-transcript-version="2">
 box.
 </span>
 <span data-rw-start="358.2" data-rw-transcript-version="2">
 Then I tested it with cloud code with a
 </span>
 <span data-rw-start="360.6" data-rw-transcript-version="2">
 max of 50 line reads at a time, and then
 </span>
 <span data-rw-start="363.68" data-rw-transcript-version="2">
 the same thing with a windowed reads,
 </span>
 <span data-rw-start="365.84" data-rw-transcript-version="2">
 with the T Puffer search tool. You may
 </span>
 <span data-rw-start="367.6" data-rw-transcript-version="2">
 ask me, like, why this like 50 line read
 </span>
 <span data-rw-start="370" data-rw-transcript-version="2">
 thing?
 </span>
 <span data-rw-start="371.08" data-rw-transcript-version="2">
 It's because it became really
 </span>
 <span data-rw-start="372.76" data-rw-transcript-version="2">
 noisy really fast if it just reads
 </span>
 <span data-rw-start="374.4" data-rw-transcript-version="2">
 long files. It's really hard to
 </span>
 <span data-rw-start="375.76" data-rw-transcript-version="2">
 understand.
 </span>
</p>
<p>
 <span data-rw-start="378.08" data-rw-transcript-version="2">
 And get a difference because it all—if
 </span>
 <span data-rw-start="379.6" data-rw-transcript-version="2">
 it just reads a whole like a thousand
 </span>
 <span data-rw-start="380.84" data-rw-transcript-version="2">
 line file, it doesn't really make a lot
 </span>
 <span data-rw-start="382.6" data-rw-transcript-version="2">
 of difference in the numbers.
 </span>
 <span data-rw-start="384.84" data-rw-transcript-version="2">
 So we'll start with the first result of
 </span>
 <span data-rw-start="386.72" data-rw-transcript-version="2">
 it. This is precision. Precision is
 </span>
 <span data-rw-start="388.92" data-rw-transcript-version="2">
 essentially the
 </span>
 <span data-rw-start="390.56" data-rw-transcript-version="2">
 the measure of how many files did it
 </span>
 <span data-rw-start="393.12" data-rw-transcript-version="2">
 read in its total process? How many
 </span>
 <span data-rw-start="395.28" data-rw-transcript-version="2">
 of them were actually golden files? So
 </span>
 <span data-rw-start="397.24" data-rw-transcript-version="2">
 if there was, if cloud read 10 files
 </span>
 <span data-rw-start="400.32" data-rw-transcript-version="2">
 and eight of them were needed, it hits
 </span>
 <span data-rw-start="401.72" data-rw-transcript-version="2">
 80% precision. You can see the baseline
 </span>
 <span data-rw-start="404.76" data-rw-transcript-version="2">
 it hit like 65% precision, 33% on line
 </span>
 <span data-rw-start="407.68" data-rw-transcript-version="2">
 precision and 43% on symbol, and it kind
 </span>
 <span data-rw-start="410.28" data-rw-transcript-version="2">
 of goes up as we add windowed grep and
 </span>
 <span data-rw-start="411.96" data-rw-transcript-version="2">
 then windowed grep plus semantic search.
 </span>
 <span data-rw-start="413.84" data-rw-transcript-version="2">
 Got it to like 87% file precision, for
 </span>
 <span data-rw-start="415.6" data-rw-transcript-version="2">
 example.
 </span>
 <span data-rw-start="416.76" data-rw-transcript-version="2">
 And this is also due to the fact, like
 </span>
 <span data-rw-start="418.16" data-rw-transcript-version="2">
 cloud code, by default, like it's a really
 </span>
 <span data-rw-start="419.72" data-rw-transcript-version="2">
 exploratory. It loves to read as much as
 </span>
 <span data-rw-start="421.92" data-rw-transcript-version="2">
 it can, and like try to read everything
 </span>
 <span data-rw-start="423.96" data-rw-transcript-version="2">
 for example, and it kind of shows up in
 </span>
 <span data-rw-start="425.16" data-rw-transcript-version="2">
 the 65% precision.
 </span>
</p>
<p>
 <span data-rw-start="427.28" data-rw-transcript-version="2">
 And you know,
 </span>
 <span data-rw-start="428.12" data-rw-transcript-version="2">
 it's hard to like translate these
 </span>
 <span data-rw-start="428.92" data-rw-transcript-version="2">
 numbers, but a more like English or like
 </span>
 <span data-rw-start="431.36" data-rw-transcript-version="2">
 human version of it is that you know,
 </span>
 <span data-rw-start="432.8" data-rw-transcript-version="2">
 cloud code one in every three file reads
 </span>
 <span data-rw-start="434.88" data-rw-transcript-version="2">
 is actually just a completely wasted
 </span>
 <span data-rw-start="436.4" data-rw-transcript-version="2">
 file.
 </span>
</p>
<p>
 <span data-rw-start="437.68" data-rw-transcript-version="2">
 And with windowed grep, it was one in
 </span>
 <span data-rw-start="439" data-rw-transcript-version="2">
 five reads was an irrelevant file,
 </span>
 <span data-rw-start="441.36" data-rw-transcript-version="2">
 and then with semantic search, there’s only
 </span>
 <span data-rw-start="442.32" data-rw-transcript-version="2">
 one in eight files was a, you know, quote
 </span>
 <span data-rw-start="444.88" data-rw-transcript-version="2">
 unquote, wasted or irrelevant file,
 </span>
 <span data-rw-start="447.2" data-rw-transcript-version="2">
 and it kind of like scales up as you kind of
 </span>
 <span data-rw-start="448.68" data-rw-transcript-version="2">
 add these tools.
 </span>
</p>
<p>
 <span data-rw-start="450.84" data-rw-transcript-version="2">
 And you know, obviously, this, this is
 </span>
 <span data-rw-start="451.96" data-rw-transcript-version="2">
 already, like, pretty good.
 </span>
 <span data-rw-start="453.56" data-rw-transcript-version="2">
 Then we have recall. Recall is
 </span>
 <span data-rw-start="455.08" data-rw-transcript-version="2">
 essentially how many of the needed files
 </span>
 <span data-rw-start="456.92" data-rw-transcript-version="2">
 did it find? So, for example, if there
 </span>
 <span data-rw-start="459.2" data-rw-transcript-version="2">
 was 10 files in the task that it should
 </span>
 <span data-rw-start="460.68" data-rw-transcript-version="2">
 have found, if cloud found five of them,
 </span>
 <span data-rw-start="463.2" data-rw-transcript-version="2">
 five files in its total trajectory,
 </span>
 <span data-rw-start="465.48" data-rw-transcript-version="2">
 and only three of them were actually these
 </span>
 <span data-rw-start="467.48" data-rw-transcript-version="2">
 golden files, it would hit 30% recall.
 </span>
 <span data-rw-start="469.96" data-rw-transcript-version="2">
 By default again,
 </span>
 <span data-rw-start="472.56" data-rw-transcript-version="2">
 Cloud code actually does win the file
 </span>
 <span data-rw-start="474.08" data-rw-transcript-version="2">
 recall, and again, part of this is
 </span>
 <span data-rw-start="475.64" data-rw-transcript-version="2">
 because it just loves to explore every
 </span>
 <span data-rw-start="477" data-rw-transcript-version="2">
 single file it can.
 </span>
</p>
<p>
 <span data-rw-start="478.96" data-rw-transcript-version="2">
 Then we have line recall, where it drops
 </span>
 <span data-rw-start="480.36" data-rw-transcript-version="2">
 a lot more.
 </span>
 <span data-rw-start="483.52" data-rw-transcript-version="2">
 This is kind of because it loved to read a lot of files,
 </span>
 <span data-rw-start="485.28" data-rw-transcript-version="2">
 but also read, to really read, a lot of
 </span>
 <span data-rw-start="486.72" data-rw-transcript-version="2">
 files that didn't have a lot of
 </span>
 <span data-rw-start="488.68" data-rw-transcript-version="2">
 golden context lines.
 </span>
</p>
<p>
 <span data-rw-start="490.88" data-rw-transcript-version="2">
 So, you can kind of see that even though it did explore a
 </span>
 <span data-rw-start="492.16" data-rw-transcript-version="2">
 lot, it also kind of explored the wrong
 </span>
 <span data-rw-start="493.48" data-rw-transcript-version="2">
 things a lot.
 </span>
 <span data-rw-start="495.6" data-rw-transcript-version="2">
 And then, with grep and grep
 </span>
 <span data-rw-start="497" data-rw-transcript-version="2">
 plus semantic, or windowed grep, and
 </span>
 <span data-rw-start="498.72" data-rw-transcript-version="2">
 windowed grep plus semantic search, kind
 </span>
 <span data-rw-start="500.84" data-rw-transcript-version="2">
 of have the same recall.
 </span>
</p>
<p>
 <span data-rw-start="503.04" data-rw-transcript-version="2">
 You can kind of see on the right, like, kind of the what
 </span>
 <span data-rw-start="504.48" data-rw-transcript-version="2">
 happened with the behavior between these
 </span>
 <span data-rw-start="506" data-rw-transcript-version="2">
 three conditions.
 </span>
</p>
<p>
 <span data-rw-start="507.2" data-rw-transcript-version="2">
 And you may be thinking, like, well, you
 </span>
 <span data-rw-start="508.68" data-rw-transcript-version="2">
 know, semantic search didn't really like
 </span>
 <span data-rw-start="510.16" data-rw-transcript-version="2">
 add improvements here. Like, what, what
 </span>
 <span data-rw-start="511.04" data-rw-transcript-version="2">
 went wrong? Like, actually, some
 </span>
 <span data-rw-start="512.88" data-rw-transcript-version="2">
 decreases. And we can like dig in a
 </span>
 <span data-rw-start="513.92" data-rw-transcript-version="2">
 little further into the recall numbers.
 </span>
</p>
<p>
 <span data-rw-start="514.88" data-rw-transcript-version="2">
 For certain tasks. This is across 50
 </span>
 <span data-rw-start="517.039" data-rw-transcript-version="2">
 tasks by default, but if we break it
 </span>
 <span data-rw-start="519.08" data-rw-transcript-version="2">
 down into where semantic search won, you know, quote unquote, won, and where just
 </span>
 <span data-rw-start="521.52" data-rw-transcript-version="2">
 like windowed grep won, we see some
 </span>
 <span data-rw-start="522.8" data-rw-transcript-version="2">
 stark differences between, like, certain
 </span>
 <span data-rw-start="524.52" data-rw-transcript-version="2">
 tasks performed a lot better with
 </span>
 <span data-rw-start="526.88" data-rw-transcript-version="2">
 semantic search
 </span>
 <span data-rw-start="530" data-rw-transcript-version="2">
 allowed,
 </span>
 <span data-rw-start="530.64" data-rw-transcript-version="2">
 and then certain tasks performed a lot
 </span>
 <span data-rw-start="532.04" data-rw-transcript-version="2">
 better with no semantic search.
 </span>
</p>
<p>
 <span data-rw-start="534.12" data-rw-transcript-version="2">
 This kind of proves,
 </span>
 <span data-rw-start="536.68" data-rw-transcript-version="2">
 you know, certain tasks require
 </span>
 <span data-rw-start="538.68" data-rw-transcript-version="2">
 different types of tools. For example,
 </span>
 <span data-rw-start="540.28" data-rw-transcript-version="2">
 when semantic search won, it was really
 </span>
 <span data-rw-start="542.24" data-rw-transcript-version="2">
 good at finding a lot of behavior
 </span>
 <span data-rw-start="543.48" data-rw-transcript-version="2">
 adjacent files that didn't have the same
 </span>
 <span data-rw-start="544.88" data-rw-transcript-version="2">
 kind of keywords. For example, it was
 </span>
 <span data-rw-start="546.8" data-rw-transcript-version="2">
 like, I think, one example off the top of my
 </span>
 <span data-rw-start="548.2" data-rw-transcript-version="2">
 head was we were trying to, like, it was a
 </span>
 <span data-rw-start="549.72" data-rw-transcript-version="2">
 multi, like, first handle lots of
 </span>
 <span data-rw-start="551.96" data-rw-transcript-version="2">
 different ORMs that have to, like, handle
 </span>
 <span data-rw-start="553.6" data-rw-transcript-version="2">
 across
 </span>
 <span data-rw-start="554.68" data-rw-transcript-version="2">
 different libraries and it didn't, by
 </span>
 <span data-rw-start="556.16" data-rw-transcript-version="2">
 default, the keyword search didn't, by
 </span>
 <span data-rw-start="557.72" data-rw-transcript-version="2">
 Default, find all of them, but behaviors
 </span>
 <span data-rw-start="559.52" data-rw-transcript-version="2">
 semantic search was able to kind of like
 </span>
 <span data-rw-start="561.2" data-rw-transcript-version="2">
 understand these are all related files.
 </span>
</p>
<p>
 <span data-rw-start="563.8" data-rw-transcript-version="2">
 And then grep won when it was really
 </span>
 <span data-rw-start="565.36" data-rw-transcript-version="2">
 good at just the task was a lot of it
 </span>
 <span data-rw-start="567.4" data-rw-transcript-version="2">
 like tracing through imports and if it
 </span>
 <span data-rw-start="569.44" data-rw-transcript-version="2">
 like was able to find the keywords in
 </span>
 <span data-rw-start="571.52" data-rw-transcript-version="2">
 like the first or second tool call, it
 </span>
 <span data-rw-start="573.76" data-rw-transcript-version="2">
 was able to like just keyword search
 </span>
 <span data-rw-start="574.96" data-rw-transcript-version="2">
 through that and find the relevant
 </span>
 <span data-rw-start="576.08" data-rw-transcript-version="2">
 files. So again, it's like two different
 </span>
 <span data-rw-start="577.64" data-rw-transcript-version="2">
 types of how to find files, but they
 </span>
 <span data-rw-start="580.48" data-rw-transcript-version="2">
 kind of lead to like really different
 </span>
 <span data-rw-start="581.68" data-rw-transcript-version="2">
 results.
 </span>
 <span data-rw-start="583.76" data-rw-transcript-version="2">
 So, in summary, what does this mean?
 </span>
 <span data-rw-start="585.8" data-rw-transcript-version="2">
 Well, we saw semantic search
 </span>
 <span data-rw-start="587.32" data-rw-transcript-version="2">
 did boost precision quite a bit
 </span>
 <span data-rw-start="589.8" data-rw-transcript-version="2">
 and we kind of understand, like, grep
 </span>
 <span data-rw-start="591.52" data-rw-transcript-version="2">
 and semantic search kind of find
 </span>
 <span data-rw-start="592.96" data-rw-transcript-version="2">
 different code in different ways.
 </span>
 <span data-rw-start="595.64" data-rw-transcript-version="2">
 And an interesting thing to note as well
 </span>
 <span data-rw-start="597.8" data-rw-transcript-version="2">
 was,
 </span>
 <span data-rw-start="598.6" data-rw-transcript-version="2">
 these numbers weren't as great as
 </span>
 <span data-rw-start="600.4" data-rw-transcript-version="2">
 Cursor's because part of, like, part of
 </span>
 <span data-rw-start="603.08" data-rw-transcript-version="2">
 Claude code is it's
 </span>
 <span data-rw-start="604.56" data-rw-transcript-version="2">
 Built for just grepping. Like that's
 </span>
 <span data-rw-start="606.76" data-rw-transcript-version="2">
 what Anthropic kind of focuses
 </span>
 <span data-rw-start="608.32" data-rw-transcript-version="2">
 on. Like it's not built to understand, like, when to call
 </span>
 <span data-rw-start="610.48" data-rw-transcript-version="2">
 semantic search or how to call it. Uh, we
 </span>
 <span data-rw-start="612.52" data-rw-transcript-version="2">
 kind of like add it as an extra tool, and
 </span>
</p>
<p>
 <span data-rw-start="614.6" data-rw-transcript-version="2">
 it's like, "Hey, like, here's this cool
 </span>
 <span data-rw-start="617.64" data-rw-transcript-version="2">
 tool. You probably should use it
 </span>
 <span data-rw-start="618.68" data-rw-transcript-version="2">
 sometimes." But it's very hard for it to
 </span>
 <span data-rw-start="619.92" data-rw-transcript-version="2">
 have a true understanding of when to use
 </span>
 <span data-rw-start="622.12" data-rw-transcript-version="2">
 it, why to use it, uh, versus, like, for
 </span>
 <span data-rw-start="624.52" data-rw-transcript-version="2">
 example, Cursor's composer. They
 </span>
 <span data-rw-start="626.2" data-rw-transcript-version="2">
 understand this is a built-in tool that
 </span>
 <span data-rw-start="628.52" data-rw-transcript-version="2">
 um,
 </span>
 <span data-rw-start="629.16" data-rw-transcript-version="2">
 it knows when and how to use it, and
 </span>
 <span data-rw-start="630.52" data-rw-transcript-version="2">
 that's why they saw that it’s like 23 and a half
 </span>
 <span data-rw-start="632.04" data-rw-transcript-version="2">
 percent, uh, performance gain. Uh,
 </span>
 <span data-rw-start="634.88" data-rw-transcript-version="2">
 so, like, in summary,
 </span>
 <span data-rw-start="636.72" data-rw-transcript-version="2">
 uh, you know, we think long-term winners
 </span>
 <span data-rw-start="638.36" data-rw-transcript-version="2">
 were, like, kind of provide these
 </span>
 <span data-rw-start="639.72" data-rw-transcript-version="2">
 lightweight tools to find the right
 </span>
 <span data-rw-start="641.12" data-rw-transcript-version="2">
 context in various different ways. I
 </span>
 <span data-rw-start="642.96" data-rw-transcript-version="2">
 think it's something important to think
 </span>
 <span data-rw-start="643.88" data-rw-transcript-version="2">
 about. Uh, you can't just like grep
 </span>
 <span data-rw-start="646.2" data-rw-transcript-version="2">
 through everything, unfortunately, in a
 </span>
 <span data-rw-start="647.48" data-rw-transcript-version="2">
 File system. Uh, we think there's a lot
 </span>
 <span data-rw-start="649.76" data-rw-transcript-version="2">
 of different ways to access lots of
 </span>
 <span data-rw-start="651" data-rw-transcript-version="2">
 different types of information. Uh, and
 </span>
 <span data-rw-start="652.76" data-rw-transcript-version="2">
 the people that provide these, like, easy
 </span>
 <span data-rw-start="654.32" data-rw-transcript-version="2">
 tools to provide to shrink down these
 </span>
 <span data-rw-start="656.76" data-rw-transcript-version="2">
 billion context windows into the right
 </span>
 <span data-rw-start="658.44" data-rw-transcript-version="2">
 million, uh, will win in the long term.
 </span>
</p>
<p>
 <span data-rw-start="661.24" data-rw-transcript-version="2">
 Um, that's the general talk. Thank you.
 </span>
</p>
<p>
 <span data-rw-start="663.2" data-rw-transcript-version="2">
 If you have any questions, feel free to
 </span>
 <span data-rw-start="664.4" data-rw-transcript-version="2">
 come up.
 </span>
 <span data-rw-start="665.487" data-rw-transcript-version="2">
 &gt;&gt; [applause]
 </span>
 <span data-rw-start="667.76" data-rw-transcript-version="2">
 &gt;&gt; I have my own idea of what semantic
 </span>
 <span data-rw-start="669.48" data-rw-transcript-version="2">
 search is, but could you define what you
 </span>
 <span data-rw-start="671.52" data-rw-transcript-version="2">
 what's your definition is of semantic
 </span>
 <span data-rw-start="672.88" data-rw-transcript-version="2">
 search?
 </span>
 <span data-rw-start="673.24" data-rw-transcript-version="2">
 &gt;&gt; Sure. Uh, so this was just, uh, just doing
 </span>
 <span data-rw-start="675.4" data-rw-transcript-version="2">
 vector search. It was just performing
 </span>
 <span data-rw-start="676.839" data-rw-transcript-version="2">
 vector search using embedding, it using
 </span>
 <span data-rw-start="678.56" data-rw-transcript-version="2">
 Voyage's code model and then just
 </span>
 <span data-rw-start="680.08" data-rw-transcript-version="2">
 embedding the, the, the query, um
 </span>
 <span data-rw-start="684.48" data-rw-transcript-version="2">
 query sentences or
 </span>
 <span data-rw-start="685.68" data-rw-transcript-version="2">
 query tokens and just sending them back
 </span>
 <span data-rw-start="687.36" data-rw-transcript-version="2">
 to Turbo puffer. Yeah.
 </span>
 <span data-rw-start="689.56" data-rw-transcript-version="2">
 Uh, sorry, the
 </span>
 <span data-rw-start="690.8" data-rw-transcript-version="2">
 uh, embedding model, uh, Voyage code three.
 </span>
</p>
<p>
 <span data-rw-start="694.08" data-rw-transcript-version="2">
 Okay. And which vector DB? Turbo puffer.
 </span>
 <span data-rw-start="698.28" data-rw-transcript-version="2">
 Yeah.
 </span>
 <span data-rw-start="698.64" data-rw-transcript-version="2">
 &gt;&gt; Sorry. Uh no worries. Yeah, yeah. Yeah,
 </span>
 <span data-rw-start="700.52" data-rw-transcript-version="2">
 for those who are unfamiliar
 </span>
 <span data-rw-start="702.16" data-rw-transcript-version="2">
 with Turbo puffer, we are the vector database that powers companies
 </span>
 <span data-rw-start="704.28" data-rw-transcript-version="2">
 like Cursor, Anthropic, Notion. So when
 </span>
 <span data-rw-start="705.839" data-rw-transcript-version="2">
 you use something like Cursor, uh, you
 </span>
 <span data-rw-start="711.52" data-rw-transcript-version="2">
 have by proxy used Turbo puffer. Um, so
 </span>
 <span data-rw-start="714.44" data-rw-transcript-version="2">
 you may know us just not by name, I
 </span>
 <span data-rw-start="716.52" data-rw-transcript-version="2">
 guess.
 </span>
</p>
<p>
 <span data-rw-start="718.6" data-rw-transcript-version="2">
 I was just going to ask,
 </span>
 <span data-rw-start="720.2" data-rw-transcript-version="2">
 you may not have a benchmark for this,
 </span>
 <span data-rw-start="721.44" data-rw-transcript-version="2">
 but how does it perform
 </span>
 <span data-rw-start="723.28" data-rw-transcript-version="2">
 on code?
 </span>
 <span data-rw-start="724.52" data-rw-transcript-version="2">
 Oh, that's tough. I mean,
 </span>
 <span data-rw-start="727.08" data-rw-transcript-version="2">
 it's hard to say.
 </span>
 <span data-rw-start="728.32" data-rw-transcript-version="2">
 &gt;&gt; Better, or is semantic better if the
 </span>
 <span data-rw-start="730.36" data-rw-transcript-version="2">
 code's like a mess and you need to go
 </span>
 <span data-rw-start="731.839" data-rw-transcript-version="2">
 and sort it out? Uh,
 </span>
 <span data-rw-start="733.64" data-rw-transcript-version="2">
 so I think it works best when there's a
 </span>
 <span data-rw-start="736.04" data-rw-transcript-version="2">
 lot of comments on the code, uh, because
 </span>
 <span data-rw-start="738.88" data-rw-transcript-version="2">
 it kind of finds that semantic meaning.
 </span>
</p>
<p>
 <span data-rw-start="740.44" data-rw-transcript-version="2">
 &gt;&gt; Like the documentation is kind of
 </span>
 <span data-rw-start="742.32" data-rw-transcript-version="2">
 inline. Yeah, if it's like inline.
 </span>
</p>
<p>
 <span data-rw-start="743.52" data-rw-transcript-version="2">
 Documentation, that was like a big um boost. I believe one of the repos I
 </span>
 <span data-rw-start="746.04" data-rw-transcript-version="2">
 remember like looking through some
 </span>
 <span data-rw-start="747.64" data-rw-transcript-version="2">
 directories and like asking Claude be
 </span>
 <span data-rw-start="748.72" data-rw-transcript-version="2">
 like, "Why did it perform so well here versus not?" And it was one of its kind
 </span>
 <span data-rw-start="753.88" data-rw-transcript-version="2">
 of explains me like
 </span>
 <span data-rw-start="755.12" data-rw-transcript-version="2">
 um when I was looking through as well,
 </span>
 <span data-rw-start="756.36" data-rw-transcript-version="2">
 like those with like really good
 </span>
 <span data-rw-start="757.96" data-rw-transcript-version="2">
 comments, for example, just like
 </span>
 <span data-rw-start="759.6" data-rw-transcript-version="2">
 comments above the function, it's able
 </span>
 <span data-rw-start="760.88" data-rw-transcript-version="2">
 to like really understand a lot more because
 </span>
 <span data-rw-start="762.32" data-rw-transcript-version="2">
 you kind of give this context to the
 </span>
 <span data-rw-start="763.839" data-rw-transcript-version="2">
 model and the embedding model. So then
 </span>
 <span data-rw-start="765.6" data-rw-transcript-version="2">
 it can like actually search better. Um
 </span>
 <span data-rw-start="768.36" data-rw-transcript-version="2">
 because that's part of it. Like the
 </span>
 <span data-rw-start="769.8" data-rw-transcript-version="2">
 the embedding, it and is not the hard
 </span>
 <span data-rw-start="771.6" data-rw-transcript-version="2">
 part. It's like figuring out what
 </span>
 <span data-rw-start="773.56" data-rw-transcript-version="2">
 meaning really is of that chunk.
 </span>
</p>
<p>
 <span data-rw-start="776.48" data-rw-transcript-version="2">
 Yeah.
 </span>
 <span data-rw-start="778.44" data-rw-transcript-version="2">
 Yeah, you may have mentioned
 </span>
 <span data-rw-start="780.12" data-rw-transcript-version="2">
 some of it now, but of course, semantic
 </span>
 <span data-rw-start="782.24" data-rw-transcript-version="2">
 search is just similarity search. So if
 </span>
 <span data-rw-start="784.64" data-rw-transcript-version="2">
 your query doesn't really match the
 </span>
 <span data-rw-start="789.32" data-rw-transcript-version="2">
 Then, you get some kind of innate
 </span>
 <span data-rw-start="791.28" data-rw-transcript-version="2">
 distance. Do you do any kind of
 </span>
 <span data-rw-start="792.68" data-rw-transcript-version="2">
 preprocessing on
 </span>
 <span data-rw-start="794.2" data-rw-transcript-version="2">
 what your target data before you
 </span>
 <span data-rw-start="797.32" data-rw-transcript-version="2">
 like, do you do a parent-child where the
 </span>
 <span data-rw-start="798.839" data-rw-transcript-version="2">
 parent is
 </span>
 <span data-rw-start="800.44" data-rw-transcript-version="2">
 query-ish, and the child is the real code?
 </span>
</p>
<p>
 <span data-rw-start="803.04" data-rw-transcript-version="2">
 &gt;&gt; In this case, it was just simple, just
 </span>
 <span data-rw-start="806.08" data-rw-transcript-version="2">
 just the code. Yeah, just the raw code
 </span>
 <span data-rw-start="808.04" data-rw-transcript-version="2">
 just as a thing, but
 </span>
 <span data-rw-start="810.36" data-rw-transcript-version="2">
 I can't speak for how these more
 </span>
 <span data-rw-start="812" data-rw-transcript-version="2">
 complicated and sophisticated customers
 </span>
 <span data-rw-start="813.4" data-rw-transcript-version="2">
 use this, but I can imagine it's
 </span>
 <span data-rw-start="815.04" data-rw-transcript-version="2">
 definitely something of providing not
 </span>
 <span data-rw-start="816.36" data-rw-transcript-version="2">
 just code-level meaning, but
 </span>
 <span data-rw-start="818.4" data-rw-transcript-version="2">
 you know, as you said, at least a
 </span>
 <span data-rw-start="819.24" data-rw-transcript-version="2">
 parent-child relationship of like
 </span>
 <span data-rw-start="820.48" data-rw-transcript-version="2">
 authentication flow. Like that could be
 </span>
 <span data-rw-start="822.56" data-rw-transcript-version="2">
 a good query to do a similarity search
 </span>
 <span data-rw-start="825" data-rw-transcript-version="2">
 against, but the code itself is more
 </span>
 <span data-rw-start="826.76" data-rw-transcript-version="2">
 like raw. Yeah.
 </span>
 <span data-rw-start="828.52" data-rw-transcript-version="2">
 Yeah. Like Cursor has their own
 </span>
 <span data-rw-start="829.64" data-rw-transcript-version="2">
 embedding model, which I think kind of
 </span>
 <span data-rw-start="830.92" data-rw-transcript-version="2">
 helps with this of like how do you
 </span>
 <span data-rw-start="832.2" data-rw-transcript-version="2">
 Translate code into more of like a human
 </span>
 <span data-rw-start="834.2" data-rw-transcript-version="2">
 level query. And I mean they're kind of
 </span>
 <span data-rw-start="837.2" data-rw-transcript-version="2">
 been experts on that. I can't speak for
 </span>
 <span data-rw-start="838.52" data-rw-transcript-version="2">
 how they do it, but I just know they do
 </span>
 <span data-rw-start="839.88" data-rw-transcript-version="2">
 do it.
 </span>
</p>
<p>
 <span data-rw-start="841.76" data-rw-transcript-version="2">
 I think they actually do what you said
 </span>
 <span data-rw-start="843.2" data-rw-transcript-version="2">
 like they create fake comments on top of
 </span>
 <span data-rw-start="845.52" data-rw-transcript-version="2">
 of your code and then embed the code
 </span>
 <span data-rw-start="847.839" data-rw-transcript-version="2">
 with the comments. Yeah. So
 </span>
 <span data-rw-start="850.72" data-rw-transcript-version="2">
 that's how they can have like their high
 </span>
 <span data-rw-start="852.959" data-rw-transcript-version="2">
 recall when they
 </span>
 <span data-rw-start="855.28" data-rw-transcript-version="2">
 So they add, they kind of inject
 </span>
 <span data-rw-start="857" data-rw-transcript-version="2">
 comments. Yes.
 </span>
 <span data-rw-start="858.2" data-rw-transcript-version="2">
 Yeah, it's something that I think
 </span>
 <span data-rw-start="859.28" data-rw-transcript-version="2">
 definitely could work. Yeah.
 </span>
 <span data-rw-start="861.56" data-rw-transcript-version="2">
 In the back? Yeah.
 </span>
 <span data-rw-start="863.04" data-rw-transcript-version="2">
 I was going to ask, like, how do you see
 </span>
 <span data-rw-start="865.44" data-rw-transcript-version="2">
 uh, I guess, the vector database kind of
 </span>
 <span data-rw-start="868.48" data-rw-transcript-version="2">
 working with the partners,
 </span>
 <span data-rw-start="870.56" data-rw-transcript-version="2">
 and how
 </span>
 <span data-rw-start="871.32" data-rw-transcript-version="2">
 like, when do you
 </span>
 <span data-rw-start="872.52" data-rw-transcript-version="2">
 code, like,
 </span>
 <span data-rw-start="873.6" data-rw-transcript-version="2">
 long-term or need to reduce the size?
 </span>
</p>
<p>
 <span data-rw-start="877.88" data-rw-transcript-version="2">
 I mean, I think it depends. Like
 </span>
 <span data-rw-start="879.56" data-rw-transcript-version="2">
 obviously, the easiest way
 </span>
 <span data-rw-start="881.4" data-rw-transcript-version="2">
 Like, people love grepping because it's
 </span>
 <span data-rw-start="883.28" data-rw-transcript-version="2">
 zero cost. Like, if you're able to like
 </span>
 <span data-rw-start="884.76" data-rw-transcript-version="2">
 download everything to your local file
 </span>
 <span data-rw-start="885.88" data-rw-transcript-version="2">
 system and just like grep through it,
 </span>
 <span data-rw-start="886.88" data-rw-transcript-version="2">
 like, yeah, that works. Um, I think vector
 </span>
 <span data-rw-start="888.959" data-rw-transcript-version="2">
 DBs are built for actually like
 </span>
 <span data-rw-start="891.2" data-rw-transcript-version="2">
 multiplayer, and like this, like, super
 </span>
 <span data-rw-start="894.28" data-rw-transcript-version="2">
 maybe in a sense, like, hard to understand
 </span>
 <span data-rw-start="895.52" data-rw-transcript-version="2">
 or, uh, complicated relationships between
 </span>
 <span data-rw-start="897.839" data-rw-transcript-version="2">
 lots of data. For example, like a
 </span>
 <span data-rw-start="899.28" data-rw-transcript-version="2">
 knowledge base, like a Notion, like you
 </span>
 <span data-rw-start="900.76" data-rw-transcript-version="2">
 can imagine, kind of hard to like really
 </span>
 <span data-rw-start="903.079" data-rw-transcript-version="2">
 grep through that really easily on your
 </span>
 <span data-rw-start="904.28" data-rw-transcript-version="2">
 local machine. Like, it's in a sense, best
 </span>
 <span data-rw-start="906.44" data-rw-transcript-version="2">
 to like have that vectorize, uh, for the
 </span>
 <span data-rw-start="908.2" data-rw-transcript-version="2">
 agents. Um,
 </span>
 <span data-rw-start="909.839" data-rw-transcript-version="2">
 And even, stuff like, we have customers
 </span>
 <span data-rw-start="911.12" data-rw-transcript-version="2">
 doing stuff like with multimodal data.
 </span>
</p>
<p>
 <span data-rw-start="912.839" data-rw-transcript-version="2">
 You can't really grep through a video
 </span>
 <span data-rw-start="913.959" data-rw-transcript-version="2">
 file. You can't grep through an audio
 </span>
 <span data-rw-start="915.36" data-rw-transcript-version="2">
 file. You can't grep through an image
 </span>
 <span data-rw-start="916.88" data-rw-transcript-version="2">
 file. Like, maybe you can glob on the file name,
 </span>
 <span data-rw-start="919.079" data-rw-transcript-version="2">
 um, but like, get a true
 </span>
 <span data-rw-start="921.36" data-rw-transcript-version="2">
 understanding of, kind of, multimodal data
 </span>
 <span data-rw-start="922.72" data-rw-transcript-version="2">
 as well, is that something that we find a
 </span>
 <span data-rw-start="925.28" data-rw-transcript-version="2">
 A lot of customers are doing.
 </span>
</p>
<p>
 <span data-rw-start="926.88" data-rw-transcript-version="2">
 Um, so it just kind of depends on the
 </span>
 <span data-rw-start="928.32" data-rw-transcript-version="2">
 workload and
 </span>
 <span data-rw-start="929.76" data-rw-transcript-version="2">
 um, I, I, yeah, if you, if you're hitting
 </span>
 <span data-rw-start="932.56" data-rw-transcript-version="2">
 like, at some sort of even like miniature
 </span>
 <span data-rw-start="935" data-rw-transcript-version="2">
 scale, like a vector DB, kinda like
 </span>
 <span data-rw-start="936.6" data-rw-transcript-version="2">
 helps offload a lot of this work
 </span>
 <span data-rw-start="938.68" data-rw-transcript-version="2">
 into, you know, cache, computer cache,
 </span>
 <span data-rw-start="940.88" data-rw-transcript-version="2">
 this semantic meaning.
 </span>
</p>
<p>
 <span data-rw-start="944.36" data-rw-transcript-version="2">
 Any other questions?
 </span>
 <span data-rw-start="948.16" data-rw-transcript-version="2">
 Okay. Thank you all.
 </span>
 <span data-rw-start="950.415" data-rw-transcript-version="2">
 &gt;&gt; [applause]
 </span>
</p>