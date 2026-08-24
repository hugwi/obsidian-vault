---
title: "Developers Might Finally Have a Local TTS Model That Doesn’t Suck"
source: "youtube"
url: "https://www.youtube.com/watch?v=pbsTTxKTuts"
author: "Better Stack"
published: "2026-05-22"
created: "2026-08-24"
duration: "0:07:58"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "engineering"
  - "evaluation"
  - "hardware"
  - "local-llm"
  - "openai"
  - "video-gen"
  - "voice-ai"
summary: "It's a local text-to-speech model that gets surprisingly close to 11 Labs for a lot of developer use cases. Except, it runs on your machine, works offline, and costs nothing every time your app says a sentence. There's no API key, no cloud request, no GPU."
---

# Developers Might Finally Have a Local TTS Model That Doesn’t Suck

![Developers Might Finally Have a Local TTS Model That Doesn’t Suck](https://www.youtube.com/embed/pbsTTxKTuts)

## Description

In this video, I test Supertonic 3, a fast local text-to-speech model for developers that runs fully offline with no API key, no cloud request, and no GPU required. 

If you are building local AI voice agents, privacy-first apps, offline e-readers, or high-volume products where cloud TTS costs, latency, and privacy become a problem, this is worth paying attention to. I run Supertonic 3 on real developer text, including money, dates, phone numbers, expression tags, English, Spanish, French, and Arabic, to see if it can handle the messy strings that normal apps actually generate.

🔗 Relevant Links
Supertonic Repo - https://github.com/supertone-inc/supertonic
Supertonic HuggingFace - https://huggingface.co/spaces/Supertone/supertonic-3

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
0:00 Supertonic 3 local TTS demo
0:37 Why cloud TTS is expensive for developers
1:58 Running Supertonic 3 offline on an M4 Mac
4:00 What is Supertonic 3?
4:30 Why Supertonic 3 is different from other TTS models
6:08 Supertonic 3 vs cloud TTS and local TTS models
6:50 Supertonic 3 pros and cons
7:14 Should developers use Supertonic 3 in 2026?

## Transcript

This is Supertonic. It's a local text-to-speech model that gets surprisingly close to 11 Labs for a lot of developer use cases. Except, it runs on your machine, works offline, and costs nothing every time your app says a sentence. There's no API key, no cloud request, no GPU. And the real test is not whether it can say some really good script, it's whether it can handle the ugly stuff our app actually spits out. So, I'm going to run it locally, throw weird text at it, and see if Supertonic is actually something devs can ship with. We all know how TTS is and the problem that comes with it. Cloud TTS is easy at first, you call an API and you get audio back. It's done. But, that simple setup has three hidden costs: money, latency, and privacy. Every request leaves our device, sure. Every user action becomes an API call, and every time your app grows, your speech bill grows with it. That might be fine for a simple project, but honestly, it just becomes a big pain. But, if you are building a voice agent sending text to a third-party server, that's going to become a serious problem. So, then what do we do? Well, we try local TTS. And now we get these different types of problems. Some models are huge, some need a GPU, and some start really slow. And some sound okay on a clean demo, but break the second you feed them what apps actually produce. Let's say your balance is $12,575 cents, due on June 15th. Call this number by 5:30 p.m. Those are a bunch of numbers. That's not some benchmark, that's what a normal app text might produce. Money, dates, phone numbers, time, just weird formatting. Hello, I'm Josh. That's easy. Production text is a lot more messy. So, here's the question I'm trying to answer here. Can Supertonic 3 handle all that ugly real-world stuff we actually need? Let's find out. If you enjoy coding tools that speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now, here's a Python script that I wrote up and all I needed to do was pip install Supertone. I made a simple TTS object and some data structures for the voice, voice styles, and the demos that I want to run. To get it to run, I just took the TTS object and linked the synthesize method and passing in those keyword arguments. I also set these here to run automatically. Now, first is just normal English. Let's play it. This is Supertone running here on my Mac. If you like this, subscribe to the Better Stack channel. Yeah, that's exactly what we'd expect. That's the easy one. Now, let's make it annoying with prices, phone numbers, and dates. I'm going to run it here again. The total invoice is 12,000 458.75 due on June 15, 2026. No, right? Major lag when it comes to prices. That was actually pretty bad. This is where a lot of TTS systems start making weird choices and Supertone was not an exception here. Also, expressions are not going to work here either. This is on the local version, which is good as we're seeing, but if you want expressions, they're going to charge you for an API key and that's where they get us. I want a good local TTS that does expressions really well and that is still free and those are hard to come by. Now, let's test multiple languages. I'm going to start here with Arabic. Arabic Now, my Arabic level is basic, but it sounded overall pretty clean. Here's some French we're going to output. French Okay, again, sounded good. And then finally, here's some Korean. Korean Okay, good, right? Those multiple languages, they sounded really good. I don't speak those languages, but they sounded clean. Everything I just ran was local and honestly, it was insanely fast. No internet, no API key, no hidden cloud request. But, the deal is this. It handles normal text in other languages incredibly well. It was super fast, so I loved that. But, when it came to numbers and expressions, the local version was not good or great by any means. So, what is Supertonic 3? At a high level, it's an on-device text-to-speech model from Supertone. It has 99 million parameters. It runs locally on CPU through ONNX runtime. Supports 31 languages and I don't need a GPU, a cloud server, or an API key, unless you want those expressions. Now, it's small enough to actually think about shipping in real local tools. Not every app, obviously, but desktop apps, controlled environments, and cached local setups, this starts to make sense. Version 3 also expands language support, improves reading stability compared to Supertonic 2, and it does support expression style tags like laugh, breath, sigh, but again, what are we doing? We have to pay for those. I don't want that. Now, this is the part devs actually care about. It's not just a model file dumped on the internet. There are examples for Python, browser, Java, C++, C#, a bunch of other languages. So, it's not just here's the research model, good luck with that. The pitch here is here is local TTS you can actually wire into your app, and honestly, the scripting, everything was really fast. There are two big reasons Supertonic 3 stands out. Speed and deployment. A lot of TTS models sound impressive. This sounded good, but then you try to use them in a product, and suddenly you're dealing with big downloads, slow generations, cold starts, or hardware requirements your users don't have. Then, deployment is incredibly simple, right? pip install supertonic. There is a Python SDK, CLI usage, and a local HTTP server. And the local server includes an OpenAI compatible V1 audio speech alias. So, OpenAI, boom. That means if your app already expects an OpenAI style speech API, you don't have to redesign everything. I can point the app at the local server and start testing. That is not just a nice detail, it's actually pretty great. Now, let's compare it without pretending this tool wins every category. Cloud TTS from OpenAI, Eleven Labs, and other ones are great. If you want really good voices, hosted infrastructure, emotions, and zero model management, they're hard to beat. But, the trade-off is clear. It costs money per use. It needs the internet. It adds network latency. And the user text leaves the device. So, local TTS gives you privacy and control, but local models can bring their own problems. The setup pain, big files, inconsistent quality, and sometimes around deployment can be tough. Supertone is interesting because it handles most of this really well. It's not the fanciest cloud voice. Uh well, it's not even a cloud voice, right? But, it's not the fanciest by any means, but it's small enough, fast enough, and easy enough to test in a real app. But, honestly, it kind of failed the tests that I actually cared about for this on a local version, which was emotions and prices or numbers. So, run your own test on this. You could try invoices, support tickets, markdown, long paragraphs. That is how you find out if this TTS model works for you where you need it. All right, so my take is this. This may be one of the most practical local TTS options for devs who just want to ship faster. But, that API key is no bueno. I wanted emotion and numbers handled well, and this did not do that. So, should you use Supertone 3? Well, yeah, sure, why not? Try it. If you're building a local voice agent, sure, give it a test. But, skip it if your top priority is good narration, you want those emotions, you want the easiest possible voice cloning workflow, maybe not that, right? For that, a cloud platform is still going to be a better choice. If you want to ship faster, you want to keep it private, local, this is really good. This is worth testing. If you enjoy coding tools like this, be sure to subscribe to the Better Stack channel. We'll see you in another video.
