---
title: "I Stopped Using Grep and My Agent Got 10x Faster"
source: "https://www.youtube.com/watch?v=gPeWb4_DMok&t=1s"
author:
  - "[[youtube.com]]"
published: 2026-04-25
created: 2026-06-08
description: "Claude Context is an MCP server that indexes your entire codebase into a vector database using AST parsing, Merkle DAG hashing, and hybrid semantic + BM25 se..."
tags:
  - "to-process"
  - dev-tools
---
![](https://www.youtube.com/watch?v=gPeWb4_DMok)

Claude Context is an MCP server that indexes your entire codebase into a vector database using AST parsing, Merkle DAG hashing, and hybrid semantic + BM25 se...

## Transcript

**0:00** · So, there's this MCP plugin called Claude Context that indexes your entire code base into a vector database, meaning your coding agent can get the exact code it needs quickly without \[music\] guessing using grep or glob and hoping it finds the right file. It even passes your code with ASTs and uses a hybrid search approach combining semantic vectors with keyword matching, which ends up using 40% less context.

**0:24** · But, it does need a Zilliz Cloud account and an OpenAI key for embeddings even if you use Claude Code. So, is the extra effort and cost worth the token savings?

**0:33** · Hit subscribe and let's find out.

**0:39** · Okay, so Claude Context, not sure about the name, is made by Zilliz, which is a company created by the founders of Milvus, a very performant vector database. It connects to your agent by MCP, so this means it can work with any agent harness and not just Claude Code.

**0:53** · But, it does three pretty complex things to make your code easily findable.

**0:58** · First, it uses Tree-sitter to pass through all of the code creating chunks of functions and classes, and this supports nine languages including TypeScript, Python, Rust, and Go. Then, it uses a custom Merkle DAG to hash each file with JSON snapshots, meaning it only re-indexes the files that have changed and not the whole code base. And then, when you actually want to search through the code, it does two different types of searches at the same time. A vector search to find the semantic meaning of the code and a BM25 index search for exact keyword matching.

**1:29** · This all results in an up to 40% context reduction, which is a lot for large code bases. In fact, let's see it in action by testing it against the VS Code code base, which has around 1.5 million lines of code. So, inside the current VS Code repo, I'm going to be using Open Code with GLM-5 Turbo because I don't want to burn through my Claude Pro weekly limits. And in order to get the MCP server set up, which you can see over here, I've already added the relevant information to my Open Code JSON file.

**2:01** · And for this information over here, you could run Milvus locally, but I've used Zilliz Cloud. So, I've got my API key from over here and I created a cluster, so this is an AWS cluster, and got the public endpoint from here. Now, while we're on clusters, I did try to use the free one first, but I kept on getting timeout issues. So, I have to get a serverless one, which does cost money, but did work a lot better. Now, once you have set up the MCP server, make sure you're running a version of Node below 24, but above or equal to 20.

**2:29** · I'm currently using version 22 just for this project, and that will give you access to four MCP tools: index code, search code, clear index, and get index status.

**2:40** · Now, the first thing you have to do is index the code base. And we can do that with this prompt. But, before we hit enter, let's take a look at how much money we've already spent on embeddings from OpenAI, which is just 1 cent and was for me testing a 23,000 line code base. We can also see in our cluster we already have information from the code base that was indexed. So, now if we index this code base, it does take some time and starts the indexing in the background. At this point, I don't recommend doing any searches. Now, because this is a large code base, it will take a while to index, so I'll come back later when the indexing is done.

**3:11** · And after about 50 minutes, the indexing is complete. And we can see we have a new chunk in our cluster with over 223,000 loaded entries. And for reference, the code that I was testing with that had 23,000 lines of code has about 1,000 lines of entries and took less than 1 minute to index. And with our OpenAI usage, we've gone from 1 cent to $1.06, which is a lot, but I don't imagine going through 1.5 million lines of code is something people will do regularly.

**3:43** · Okay, let's see how fast it is to make a search. Here we have one instance of Open Code using the Claude Context MCP server, and here we have one with no MCP server. So, it'll be using the regular grep and glob tools to search through the code. And we'll give it a prompt of use Claude Context to find the entry point of when this project starts up.

**4:01** · Let's see how long this takes. Okay, so it's using the index tool, and now it's using the search tool, and the whole thing took about 19 seconds to search through this whole project and find the main.ts file. And now we're going to give this Open Code a similar prompt, and it finds a response in 14 seconds.

**4:16** · So, it's like for this query, using just regular GLM is a lot faster. Let's start a new session, and then I'm going to give it a new prompt of what function opens a new untitled document. This one took a bit longer at 40 seconds and found the main function with a line number and used about 23K tokens. And the other instance did it in 12 seconds and used 18K tokens, but it looks like it found a different file. In fact, Claude Context gives way more information showing the code and other files related to opening the editor.

**4:43** · So, I'm going to ask them both to show me the exact code, and at this point Claude Context responds in 23 seconds with the code, and the non-Claude Context Open Code responds in 49 seconds, almost double the amount of time. And it gives you the exact same code as Claude Context did, which gives me an idea. I'm going to give it a more broad generalized prompt of look through the code and tell me how this project works.

**5:06** · Claude Context finishes in 49 seconds using 41K tokens, and the other instance finishes faster and uses less tokens.

**5:13** · But, if we have a look at the output produced, we can see there's much more detail from Claude Context giving the layered architecture and even some information about the Electron app and the processes it uses. And the non-Claude Context option does also give some architectural information, but it's not as detailed as the other one. In fact, I know it doesn't look like it, but I would say Claude Context is very good at getting code information up front quickly in lots of detail. I mean, take a look at this. So, from this prompt I asked a follow-up prompt to tell me more information about the main process in the Electron app, which it stated up here.

**5:45** · So, after I asked this prompt, it took about 1 minute and 47 seconds, but look at all that detail.

**5:53** · So, it started out with the boot sequence and then phase one, so the service creation and service initialization. And we've got so much more from phase two, the code application app with all the references to the relevant files. So, we've got app.ts line 185, and we could keep going on and on. Whereas, without Claude Context, Open Code is still going through all the files using multiple sub-agents, and this is a bit deceiving because we can't see exactly how many tokens each sub-agent is using.

**6:19** · But, if we wait for a bit and come back, we can see after about 5 minutes Open Code responds with a lot of information about the Electron process, but this isn't as much as what Claude Context provided, and it did take five times longer. Now, yes, maybe if I used a smarter model like Opus 4.7 with high effort, it would get more information, but it would still take a long time and use a lot of tokens. And these are the kind of differences, so 5 minutes and 1 minute, that I was seeing when I was testing before recording with the 23K line code base.

**6:51** · So, in the end, it's difficult to say who is the clear winner. I mean, Claude Context did always provide more detail, but it wasn't always the fastest and the most token efficient. And for large code bases, it did take a very long time to index. However, for average-size code bases, so 20 to 30,000 lines of code, the indexing time is really quick, and the difference in detail when it comes to results is very apparent. In fact, I would say I would much rather use Claude Context for average-size code bases than use it on large code bases. So, that's something to think about.

**7:23** · But, to be honest, this is more of a great sales tool for Zilliz because before using Claude Context, I had never heard of them, and now they have a new paying customer. But, even though it did take a while to set up and indexing large code bases took a very long while. As someone who regularly goes through open-source code bases and asks questions, I think this is a tool I'm going to be using a lot more. I mean, for an average-size code base, the serverless plan isn't too expensive as the OpenAI embeddings don't cost too much either. So, I'm happy to take the hit.

**7:52** · Speaking of data retrieval and AI, if you want to learn how to build a really good rag system from scratch that actually works, then check out this video from Andras. And if you're a Star Wars fan, you're especially going to like this video.