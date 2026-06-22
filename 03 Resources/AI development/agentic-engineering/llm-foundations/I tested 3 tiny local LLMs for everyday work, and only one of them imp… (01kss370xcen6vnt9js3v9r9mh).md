---
title: "I tested 3 tiny local LLMs for everyday work, and only one of them impressed"
source: "https://www.xda-developers.com/tested-tiny-local-llms-for-everyday-work-only-one-impressed-me/"
author: "Nolen Jonker"
published: 2026-05-23
created: 2026-05-29
description: "Small but not useless"
tags:
  - to-process
  - llm-foundations
---

![lfm2.5 1.2b in lm studio on desktop  pc,  lego and lamp in  view](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/lfm2-5-1-2b-in-lm-studio-on-desktop-pc-lego-and-lamp-in-view.jpeg?&fit=crop&w=1600&h=900)
The local models that get talked about most tend to sit in the 7B to 12B range, which is also where most setups land if you've got decent hardware. Anything smaller usually gets written off as a toy before it gets a fair try. But not everyone has 16GB+ of VRAM to work with, and the really tiny models, the under-2B crowd, are [getting more capable](https://www.xda-developers.com/local-llms-are-good-now-wasted-months-not-realizing-it/) than their size suggests, and I wanted to see if they're worth poking at despite being able to run the mid-size ones.


The two models I keep coming back to are Qwen 3.5 9B and Gemma 4 E4B, both running fine on my 8GB VRAM, so hardware isn't really the bottleneck for me. The question was more about how far down you can go before a local model just becomes useless. So I grabbed three of the smallest options I could find that still claim to do real work, and put them through two tests: a structured weekend study guide, and a real-time weather query through my [Brave Search MCP](https://www.xda-developers.com/added-one-tool-to-local-llm-setup-and-it-stopped-making-things-up/).


Want to stay in the loop with the latest in AI? The XDA AI Insider newsletter drops weekly with deep dives, tool recommendations, and hands-on coverage you won't find anywhere else on the site. Subscribe by [modifying your newsletter](https://www.xda-developers.com/profile/account/).


##  Gemma 4 E2B


###  Small footprint, big personality quirks


[E2B](https://huggingface.co/google/gemma-4-E2B) is the smallest of [Google's edge-focused Gemma 4 models](https://www.xda-developers.com/found-open-source-local-llm-that-competes-with-cloud-ai-gemma-4/), designed to run on phones and laptops. The E stands for "effective" parameters, and it uses Per-Layer Embeddings to keep the active memory footprint low while the full weights live elsewhere. In practice that translates to around 5GB of RAM at 4-bit quantization, with a 128K context window, native function calling, configurable thinking modes, and proper system prompt support. So all the things E4B can do, just at a smaller scale.


On the structured study guide, it hit all six required sections, kept the format intact, and didn't hallucinate course names or book titles like the prompt explicitly asked. The catch is the same annoying behavior I've seen on E4B, where it bleeds its planning process straight into the response. My answer literally opened with "Planning Process - Analyze the Request…" I'd written a system prompt specifically telling it not to combine its thinking with the response and it ignored that completely, just like E4B. And after some digging, it appears to be an issue with LM Studio rather than the model. So it is what it is for now.


The real-time test with Brave Search went fine on the first try. I asked for the weather in Cape Town and got a sensible answer in Celsius. But when I started a new chat with the same question, it gave me the Fahrenheit number labeled as Celsius. So I asked for Celsius again and it still defaulted. Worth knowing if you're planning to use it for real-time data.


##  Qwen 3.5 0.8B


###  Confidently wrong on basically everything


   ![qwen  3.5 0.8b study guide in lm studio](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/qwen-3-5-0-8b-study-guide-in-lm-studio.png?q=49&fit=crop&w=825&dpr=2) 
The smallest entry in Alibaba's [Qwen 3.5](https://huggingface.co/Qwen/Qwen3.5-0.8B) Small Series, dropped in March 2026 alongside the 2B, 4B, and 9B variants. It's Apache 2.0 licensed, multimodal (text and vision at under 1GB is genuinely impressive for the size), and it uses the same Gated DeltaNet architecture as the [9B I'm already running](https://www.xda-developers.com/replaced-local-llm-with-smaller-model-better-results/). That last bit is the interesting part because GDN keeps the KV cache footprint small, and the 0.8B stretches to a 262K context natively, which is wild for a model this size. But I shouldn't have been impressed before actually using it...


The structured study guide came out worse than Gemma. It kept the section headers intact - Saturday Schedule, Sunday Schedule, Self-Check Questions - but the content underneath stopped matching the actual topic. Visual hierarchy somehow drifted into CSS grid, flexbox techniques, sticky navigation bars, hover states, and building e-commerce landing pages. I also explicitly told it not to name specific tools and it dropped Photoshop, Figma, Sketch, Amazon, and Google in as examples anyway (the last two as websites with visual cues, which is at least topic-relevant, just still violating the no-naming rule). It also added a summarizing closing paragraph after the Self-Check Questions section, another thing I'd explicitly told it not to do.


   ![qwen 3.5 0.8b incorrect  real time  data](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/qwen-3-5-0-8b-incorrect-real-time-data.png?q=49&fit=crop&w=825&dpr=2) 
The real-time test was the funnier one, in a bad way. It told me Cape Town was 57°C with a "real-feeling temperature" of 52°C. It's never been over 50 degrees Celsius in my region - I'm no temperature expert but I think 50+ would be uninhabitable. Qwen probably meant to say Fahrenheit, which would make more sense. So I pushed back, but it doubled down and then just started making stuff up. Confident, polite, and completely wrong.


At least it actually called the tool; models this size aren't usually reliable at invoking MCP tools. And its writing was also at least coherent.


##  LFM2.5-1.2B-Instruct


###  It failed loud but also won quiet


   ![lfm2.5 1.2b in lm studio study guide](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/lfm2-5-1-2b-in-lm-studio-study-guide.png?q=49&fit=crop&w=825&dpr=2) 
This one's the outlier of the bunch. It's from Liquid AI, so not Google, Alibaba, or Meta, and it's built on a completely different architecture than the other two. [LFM2](https://huggingface.co/LiquidAI/LFM2.5-1.2B-Instruct) is a hybrid model that combines multiplicative gates and short convolutions with grouped query attention blocks, rather than running on a standard transformer. The payoff is 2x faster prefill and decode on CPU compared to similarly sized models, under 1GB of memory, and a 32K context. Liquid is pretty upfront in their docs about what it's for and what it isn't - they recommend it for agentic tasks, data extraction, and RAG, and explicitly don't recommend it for knowledge-intensive work or programming. But I tried anyway…


The structured study guide was its worst showing by a wide margin, as I should have expected. It threw the entire format out the window; just four prose paragraphs covering what visual hierarchy is, Saturday advice, Sunday advice, and a closing. But it at least didn't hallucinate any tools, drift off-topic, or add a meta-conclusion after the closing. It just couldn't follow the structural formatting.


   ![lfm2.5 1.2b in lm studio  real time   data](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/lfm2-5-1-2b-in-lm-studio-real-time-data.png?q=49&fit=crop&w=825&dpr=2) 
The real-time test is where it actually pulled ahead of both Gemma and Qwen. It called the Brave Search tool cleanly and came back with "about 18°C with partly cloudy skies". It was one sentence, the correct unit, and within a couple of degrees of actual conditions. There was no hallucinating or being confidently wrong. Turns out the model that lost the creative task is the one I'd actually trust with the kind of work it was built to do.


###  Not toys, just specialists


To be fair, I ran all three through the same two tests instead of tailoring prompts to each model's strengths, so the results skew toward what they could do off the shelf rather than what they could do if you actually focus on their strengths. LFM2-1.2B is explicitly recommended for agentic tasks, data extraction, and RAG, which is probably why the Brave Search call was the cleanest part of the whole experiment. Qwen 3.5 0.8B is more of a fine-tuning base for things like classification and summarization, not a general-purpose chatbot.


Tiny models are just different tools with different jobs. LFM2-1.2B is the one I'd actually keep installed for the kind of work it was built to do, with Gemma 4 E2B a close second for anything that needs structure and a bit of creativity.