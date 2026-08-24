---
title: "1,000+ Tokens/Sec: Google Just Shattered the AI Speed Limit (DiffusionGemma)"
source: "youtube"
url: "https://www.youtube.com/watch?v=Dxn3BcSgsMY"
author: "Better Stack"
published: "2026-06-13"
created: "2026-08-24"
duration: "0:12:39"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "business"
  - "context-engineering"
  - "evaluation"
  - "google"
  - "hardware"
  - "local-llm"
  - "video-gen"
summary: "Google has been on fire lately. Last week I did a video on their groundbreaking encoder-free Gemma 4 model, and this week they dropped another shockingly innovative model. It's called Diffusion Gemma, and this model is blazingly fast."
---

# 1,000+ Tokens/Sec: Google Just Shattered the AI Speed Limit (DiffusionGemma)

![1,000+ Tokens/Sec: Google Just Shattered the AI Speed Limit (DiffusionGemma)](https://www.youtube.com/embed/Dxn3BcSgsMY)

## Description

In this video, we explore Google DeepMind's newly released DiffusionGemma model, a revolutionary paradigm shift that applies image-generation techniques to text by using uniform state diffusion to refine a canvas of pure noise over multiple bidirectional passes. This structural shift flips local LLMs from being memory-bound to compute-bound, theoretically unlocking generation speeds exceeding 1,000 tokens per second on an H100 GPU. To see how this architecture holds up in the real world, we deploy the model inside a RunPod container and benchmark it against practical engineering tasks prompting it to build a personal finance dashboard and a fully functional arcade game to see if its blazing speed is worth the quality tradeoff.

🔗 Relevant Links
DiffusionGemma: https://blog.google/innovation-and-ai/technology/developers-tools/diffusion-gemma-faster-text-generation/
Visual Guide to DiffusionGemma: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-diffusiongemma

❤️ More about us
Radically better observability stack: https://betterstack.com/
Written tutorials: https://betterstack.com/community/
Example projects: https://github.com/BetterStackHQ

📱 Socials
Twitter: https://twitter.com/betterstackhq
Instagram: https://www.instagram.com/betterstackhq/
TikTok: https://www.tiktok.com/@betterstack
LinkedIn: https://www.linkedin.com/company/betterstack

📌 Chapters:
00:00 Google's New Innovative Model
00:41 The Problem with Auto-Regressive LLMs
01:00 What Does Memory-Bound Mean?
01:41 The Core Concept Behind DiffusionGemma
02:25 The Challenge of Long-Context Tokens
03:17 How Multi-Pass Token Correction Works
03:48 The Connection to AI Image Generators
04:08 What Does "Noise" Mean for Text?
04:25 Uniform State Diffusion Explained
04:45 Mask Diffusion vs. Uniform State Diffusion
05:14 The Catch: Encoder Mode vs. Denoising Mode
05:52 DeepMind's Architecture & Logit Retention
06:19 Explaining Bidirectional Attention
06:44 How Architecture Unlocks 1,000+ Tokens/Sec
07:02 The Tradeoff: Speed vs. Maximum Quality
07:26 Setting Up the RunPod Local Test (Hugging Face & vLLM)
08:13 Deploying the H100 Container On-Demand
09:17 Test 1: Personal Finance Dashboard
10:19 Test 2: Arcade-Style Game
11:11 Benchmark Results & Reality Check
11:31 A New Generation Paradigm
11:51 The Future of Local AI Paradigms
12:02 Outro

## Transcript

Google has been on fire lately. Last week I did a video on their groundbreaking encoder-free Gemma 4 model, and this week they dropped another shockingly innovative model. It's called Diffusion Gemma, and this model is blazingly fast. It is capable of generating more than 1,000 tokens per second, and the reason why it's able to do that is because it generates text in a completely different way than any other model you've ever used before. So, in this video, we'll take a look at Diffusion Gemma, see how it works, and I'll show you how you can test it out for yourself as well. It's going to be a lot of fun, so let's dive into it. So, every language model you've ever talked to works the same fundamental way. They're auto aggressive, and that's a fancy word for saying they generate one token at a time left to right. They write a word, then they look at everything written so far, and then they predict the next word, and the cycle just repeats. And the way it works for large commercial models like Claude or GPT is that when a server generates a token, most of the time isn't spent on computing, it's spent loading the model's weights out of memory. And that's kind of wasteful if you're serving just one user. So, the servers batch hundreds of users together, load the weights once, and run them against everybody in the same time. And that way, you can serve 256 users with one memory load. But when you run a model locally, you're just one user. So, there's nobody to batch you with. The GPU loads the massive portion of weights, does a tiny little computation to produce one token, and then it sits there idle before doing it all again. In technical terms, this is called being memory bound. Your expensive GPU spends most of its life waiting for the next token instead of actually computing. So, Google DeepMind looked at this problem and asked a clever question. If the cloud fills the idle time by serving 256 users at once, what if we filled that idle time for a single user instead? So, instead of one token for 256 people, what if we generated 256 tokens for one person all at once? And that's the entire idea behind Diffusion Gemma. Instead of writing word by word, the model starts with which is a row of 256 completely random placeholder tokens. So, it's just noise. And its job is to fix that canvas all positions at once and turn it into real text. So, by predicting all 256 tokens in one shot, you're giving your GPU a big chunk of real work instead of letting it idle. In that way, you flip the model from being memory bound to compute bound. And all that wasted firepower finally gets used. But, this is not as straight forward as it sounds. Predicting 256 tokens at once is actually really hard. Because how does the model guess token number 254 when it has no idea what tokens 1 through 253 turned out to be? And that's exactly what happens. The first few tokens come out good, but the further down it goes, the more it falls apart into nonsense. But, what if instead of just doing one pass, what if the model does multiple passes? And this is the key trick. The model passes over the canvas again and again, but now it can see its own previous guesses. The tokens it predicted with confidence become context clues that help fix the messier ones. And the coolest thing is that it only needs a few passes, way less passes than the total token count of 256. And that's exactly where the model speed comes from. And you've probably seen this trick before. It's called diffusion. You start with noise and then you refine it step by step. And that is the exact same idea that powers AI image generators. And the way the model learns it is by deliberately adding noise to real images in training and then learning to predict and subtract that noise back out. But how do you apply that same concept to text? That is the tricky part because with an image, noise is easy. Make a pixel a little more red or blue, but with text, how do you make the word "the" be a little bit less "the"? What does that noise even mean for a word? Well, DeepMind came up with something called uniform state diffusion. So instead of fiddling with letters, you treat the randomly swapped out word as the noise. And to corrupt your training text, you replace some real words with random ones and the model's job is to figure out which words are garbage and eventually fix them with multiple passes. There's actually a simpler version to do this called masked diffusion that just blanks out tokens, but that one has a big flaw. Once the model commits to a word, it's locked in forever. It has the same problem auto-regressive models have. But uniform state diffusion fixes this by always holding some kind of token in every position. So a model can look at a word it accepted three steps ago, decide if it doesn't fit anymore, and swap it out. So it can basically self-correct it all the way through. But this solution also has a catch. Diffusion needs an encoder to understand and a denoiser to clean the canvas. So DeepMind developed an encoder-denoiser patch. It's built on top of their existing 26 billion Gemini 4 model and it switches between the two modes when it's generating your response. In encoder mode, the model reads your prompt, tries to extract some context and guidance for it. It collects all of that in KV cache and then passes that directly to the denoiser. And the denoiser's job is essentially to clean the canvas, and it does that by doing two things. First, remember how a normal LLM produces a confidence score or a logit for every position, but throws all of them away except the last one? By the way, if you're getting confused here, I also made a video a while back explaining how LLMs work in more detail, so check that video out if you're interested. So, essentially, Diffusion Gemma doesn't throw out the scores, it keeps all those confidence scores because every canvas position needs its own prediction. And secondly, this denoiser doesn't use causal attention, which is the rule that a word can only look backward, which is how autoregressive models work. So, instead, it swaps it with a bidirectional attention. So, now every token can see every other token in all directions. So, for every position, you apply those confidence scores, look at other tokens, and clean out the canvas slowly, step-by-step. And this is how Diffusion Gemma is able to achieve its incredible speed of 1,000 plus tokens per second on an H100 GPU. Now, I have to be straight with you. This isn't a silver bullet. With these new tactics, Diffusion Gemma is basically trading quality for speed. For maximum quality work, standard Gemma 4 is still a better pick. This model is built specifically for critical local stuff like inline editing or code filling or rapid iteration. And it is especially strong at non-linear tasks like filling in the middle of a code block or even solving a Sudoku puzzle, which normal left-to-right models are genuinely quite bad at. So, all of that sounds fascinating, but let's test it out for ourselves and see how it works in action. So, Google has open-sourced the weights under Apache 2.0 license on Hugging Face. So, if you have a beefy GPU like an RTX 5090, you could try to run it locally. And there's also a special recipe for VLLM you can run on Docker to streamline that process. But I am really curious to see if this model can really reach thousand plus tokens per second. So for this test, I will actually try to run it on an H100 GPU using a RunPod container and see how it goes. And by the way, I have also published a Diffusion Gemma template for running it on RunPod. So if you want to replicate this test, all you have to do is run that template when creating a new pod. So to do this test on RunPod, I'm going to choose the H100 container. And as I mentioned before, I created a Diffusion Gemma template you can reuse. So you can just click that. We click on a volume disk and then just click deploy on demand. And it will take a few minutes until it downloads the container and launches everything. And if we go to the logs, if you see application startup complete, that means that VLLM is ready and it is now accessible through port 8000. If we open this, you will see detail not found, but don't worry about it. This means it is actually working. We just need to copy this URL. So to configure Diffusion Gemma to run in an AI agent terminal, something like Open Code, you need to configure your Open Code settings to access the remote server. So you can do that with this simple command and this will open up the config file. And in here, I'm just specifying our RunPod server and it has the Diffusion Gemma model selected and you can just save this file and fire up Open Code. So in this test, I'm going to prompt it to generate a personal finance tracking dashboard called Ledger and let's see how fast it can generate that. Look at that. Instantly it starts streaming right away. Look how blazingly fast that is. Holy moly. Wow. That is insane. And here in the logs, we can see that it's averaging 700 tokens per second. So for the output phase, it dropped a bit, but during the reasoning phase, it did go up to 700 tokens per second. That is insane. So let's open it up. Okay. So this looks like a dashboard. That's nice. Okay, we actually get some categories and stuff going on here. If we add something over here, oh, it actually adds it as an expense. So the expenses are not actually updating. So it's not fully functional, but at least some parts are interactive. For this next task, let's see if it can actually make an arcade-style game. So let's fire it up. Once again, the speed is just insane. Okay, this one is taking a bit longer. We actually got two files here. Interesting. Interesting. Okay, so it noticed a typo and then it reprocessed the HTML file again, which is pretty good. Okay. All right, let's open up this one. Restart. Oh, wow. This one is it's working. Oh, wow. This is cool. Wow. Very nice. That is impressive. So the game is fully functional and it took 14 seconds to generate this game. 14 seconds to generate a game like this. So although their marketing page said that we could expect 1,000 token per second speeds on the H100, um that was not my observation. Um I don't know, maybe there's something that I should tweak in the template or in my prompts, but nonetheless, I am truly impressed. It is a beast. So there you have it, folks. That is Diffusion Gemma in a nutshell. I think this one is one of the most interesting releases of the year because it proves you can take a totally different generation paradigm from the image world, slap it onto an existing model you already trained, and unlock real speed gains for single local user setups. And I think this also opens the door for a whole new family of fast, interactive, local models that utilizes the full potential of your hardware instead of leaving it idle. So, what do you think about Diffusion Gemma? Have you tried it? Will you use it? Let us know in the comment section down below. And folks, if you like these types of technical breakdowns, please let me know by smashing that like button underneath the video. And also, don't forget to subscribe to our channel. This has been Andras from Better Stack, and I will see you in the next videos. >> [music] [music] [music]
