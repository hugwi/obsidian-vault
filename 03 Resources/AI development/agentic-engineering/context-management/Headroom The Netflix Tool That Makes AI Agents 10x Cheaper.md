---
title: "Headroom: The Netflix Tool That Makes AI Agents 10x Cheaper"
source: "https://www.youtube.com/watch?v=KqdRWE1en8k"
author:
  - "[[youtube.com]]"
published: 2026-06-08
created: 2026-06-08
description: "Headroom is an open-source tool that compresses everything your AI agent reads, tool outputs, code files, and RAG results, before it reaches the LLM, cutting..."
tags:
  - "to-process"
  - context-management
---
![](https://www.youtube.com/watch?v=KqdRWE1en8k)

Headroom is an open-source tool that compresses everything your AI agent reads, tool outputs, code files, and RAG results, before it reaches the LLM, cutting...

## Transcript

**0:00** · This is Headroom, an open-source tool that compresses everything your AI agent reads. So, that's tool calls, code files, and rag before it reaches the LLM, meaning you can reduce tokens by 60 or even 95% to get the exact same answer. And the clever part is it's reversible, so the model can ask for the full information back whenever actually needs it. But compression usually means you lose something. So, how do you remove most of the context and still get the right \[music\] answer? This is genuinely an interesting question. So, hit subscribe and let's find out.

**0:31** · If you've ever used a harness like Claude Code, you know it uses a lot of tokens. Every tool call could dump huge JSON logs, which are mostly noise detracting from the important information. And all of this gets stuffed into the context window, which is what you're paying for. Especially if you use something like Opus on ultra code mode, which runs dynamic workflows spinning up parallel sub agents with no token cap. This is why Tejas Chopra, a senior dev at Netflix, created Headroom, which works by detecting the content type and keeping the important information.

**1:01** · So, for JSON arrays, it keeps the anomalies and edge cases. It has a code compressor that reads the actual syntax tree. And when it reads build logs, it keeps the failures and throws away the passing tests. But, here's the interesting part. For plain text, Headroom uses its own model called Compress Base, which Tejas trained himself just for compression, and this model runs locally on your machine.

**1:22** · Headroom claims it's already saved users around $700,000 in tokens. And what's really clever is that it leaves a breadcrumb in the compressed text containing a hash that the model can use to retrieve the uncompressed data if it ever needs it. Now, if you've watched James's video on Caveman, that also reduces context but from the opposite direction. And I'll explain more of that later on in the video. But for now, let's see a basic example of Headroom to understand how it works. Now, Headroom works by using a Python server that sits between your app, so this could be Claude Code, and for example, the Anthropic servers.

**1:53** · So, when a tool call result comes back, the proxy compresses it using Rust under the hood and just sends the compressed version to the API.

**2:01** · So, you can install the server with pip, but I'm going to use UV and make sure the version of Python is 3.12 because it won't work on newer versions than that.

**2:09** · Then, run the Headroom proxy command from this library, which triggers the proxy on this port. Headroom also has a TypeScript or Python SDK, and for the demo, we're going to use the Python one to create an app using the Claude SDK.

**2:22** · So, we can install both like this, and then we're ready to go through the app.

**2:26** · Now, the plan is to show you how to use Headroom with Claude's code later on, but I just wanted to show you how it works behind the scenes first. So, for this app, we have a user prompt to read all the log files and find out the error as well as the root cause. And from here, we're going to fake the tool call.

**2:40** · So, we're going to get Claude to make a bash tool call to cat the server log file, which contains a bunch of fake logs and is imported up here. And then, we're going to return the tool call results. Now, the reason we're not just giving Headroom the text file directly is because it only compresses tool call output. So, here we specify the model, and below it, we're using the Headroom compress function to take the message with the model for accurate token counting. Headroom does not actually use Haiku. And then, we give it the base URL of the proxy.

**3:05** · And then, we have a bunch of console logs for testing purposes, showing you the message before and after Headroom, and some more console logs showing the percentage saving. And after that, we pass the compressed message from Headroom into Claude's code, which also contains the user prompt. So, now if we run that file, we can see Headroom has saved 98% of the tokens. So, here are the tokens before, and here are the tokens afterwards. So, it saves over 17,000 tokens, and it's obvious to see when we look at the before and after.

**3:31** · So, if we scroll up, this is the before, so this is what normally is sent to Claude's code. We get the user prompt, the tool call, and the tool response, which is the whole log file. And if we look here at what Headroom sends, we can see we get the same user message and tool call, but the tool response is way less. And what it's done here is used statistical compression to drop redundant tokens. So, it's removed 419 similar info logs and compressed them to a summary. Now, here we can see below Headroom tells Claude that this is the compressed output. It can retrieve it using this hash.

**3:59** · Now, here we see one of the immediate disadvantages of Headroom is that Claude thinks it doesn't have enough information to complete the task, but it definitely does. So, what we're going to do is run our file again, and we can see that this time we still have the 98% savings, but we have way more information from Claude. Let's try another demo. As usual, we need to run the Headroom proxy. But, this time I'm giving it more parameters.

**4:20** · So, here we can see I'm adding the ML value, which uses the compressed model locally for compressing plain text, and I've added code to make available the code aware compressor, and then I've added the code aware flag to turn it on. So, now we can see it's enabled here. Then, I'm going to run Claude's code, but first I'm going to set the base URL to the proxy.

**4:39** · And so, with that in place, I'm going to give Claude a prompt of read every single TS file in this project and give me a deep overview of what this project is doing with citations to the relevant code. And after a while, it gives me a response telling me it's read all the TypeScript files across the five packages, and it's given me a detailed overview. But, if we run the context slash command, which I've done earlier, we can see it used 89.1k tokens.

**4:59** · Now, I actually went ahead and ran a similar prompt in Claude without using Headroom, and if we scroll down to the bottom and see where we called the context slash command, this has used a bit more tokens. Now, I'm not sure why it's chose the easy Opus 1M context window here, and has chosen the 200k context window here, but we can curl this endpoint and format with a JQ to see exactly where the compression was from the proxy.

**5:22** · Now, this contains a lot of information, so it took me a while to find it, but if we scroll up, we can see how many tokens were saved by the Headroom compressor, and even see how much money the compression saved us. Now, of course, all of this was just from one prompt, but imagine if I had multiple Claude code sessions running, and I had Headroom compressing all the tool calls.

**5:40** · Imagine just how many more tokens I would save. I also want to point out that when I ran the exact prompt with low effort on Opus, Headroom didn't actually make any token savings. It's only when I moved from low to medium that the token savings were visible. So, maybe if I was on high, extra high, or even max, then it would save even more tokens. But anyway, that was a quick overview of Headroom, and of course, there are so many more features I could have gone through, like cross-agent memory, which lets Claude, Codex, and other harnesses share the exact same compressed contexts.

**6:08** · Headroom learn, which mines your failed sessions to figure out what it compressed too hard and learns so it doesn't do the same mistake in the future, as well as integrations with popular SDKs. But, there is one kind of important thing to consider about Headroom. Each time the model doesn't get the information it needs and asks Headroom to provide the full data, it makes a second round trip, which kind of means you end up using more tokens with Headroom in some cases than without. But, I guess this is the advantage of using the Headroom learn feature, which tries to prevent that from happening more and more in the future.

**6:38** · But, remember when I spoke about Caveman earlier on in the video? Well, Caveman reduces tokens by instructing the model to respond in short fragments, dropping filler words, and so on. But, as you've just seen in the demo, Headroom shrinks what the model reads before it even gets to the model. So, one cuts the output while the other one cuts the input, which means technically, you can use them together for maximum token saving if you really care about saving tokens that much.