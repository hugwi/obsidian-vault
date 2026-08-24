---
title: "This Tiny 82M Model Just Beat Most TTS APIs (Runs Locally)"
source: "youtube"
url: "https://www.youtube.com/watch?v=bdf6BxyxCnQ"
author: "Better Stack"
published: "2026-04-03"
created: "2026-08-24"
duration: "0:05:41"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "apple"
  - "context-engineering"
  - "engineering"
  - "hardware"
  - "local-llm"
  - "openai"
  - "video-gen"
  - "voice-ai"
summary: "An 82 million parameter model just beat much larger TTS systems and it runs locally on a laptop faster than most paid APIs. Last month I paid for a cloud TTS but still got some lag. How are some of these open-source models beating this?"
---

# This Tiny 82M Model Just Beat Most TTS APIs (Runs Locally)

![This Tiny 82M Model Just Beat Most TTS APIs (Runs Locally)](https://www.youtube.com/embed/bdf6BxyxCnQ)

## Description

Kokoro-82M is one of the most interesting open source text-to-speech (TTS) models right now, especially for devs building voice agents, local AI apps, and speech pipelines. 

In this video, we look at why this tiny 82 million parameter model is outperforming much larger models and even competing with paid cloud TTS APIs, while running locally on a Mac M4 Pro with no GPU required. You’ll see a demo, a simple setup, and how Kokoro compares to alternatives like XTTS, ElevenLabs, and other modern TTS systems in terms of speed, latency, cost, and privacy.

🔗 Relevant Links
Kokoro 82M HuggingFace - https://huggingface.co/hexgrad/Kokoro-82M
Kokoro Python Repo - https://github.com/hexgrad/kokoro

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
0:00 Stop Paying for TTS? Local Model vs Cloud APIs
0:30 Why Cloud TTS Is Expensive and Slow for Developers
1:03 Kokoro-82M Explained (Why Devs Are Switching)
1:31 Install Kokoro-82M (Python Setup Guide)
1:45 Live Demo: Local TTS on Mac M4 (No GPU)
2:39 Real-Time Speech Generation Demo (24kHz Output)
2:50 What Is Kokoro-82M? (Architecture + Size Breakdown)
3:25 Cons of Kokoro-82M (No Voice Cloning, Neutral Tone)
4:00 What Kokoro 82M Fixes
4:30 I Loved This and Hated This
5:20 Final Verdict: Best Local TTS for Developers?

## Transcript

An 82 million parameter model just beat much larger TTS systems and it runs locally on a laptop faster than most paid APIs. Last month I paid for a cloud TTS but still got some lag. That made no sense to me. How are some of these open-source models beating this? This is Kakoro 82M and it's already being shipped by some devs. Let's see how this works and better yet, how it sounds. >> [music] >> Okay, now if you're building with text to speech, you're usually choosing between two bad options. First option is obviously cloud API's, right? They're easy to start but now you've got these bills, latency spikes, and one more dependency every time your app speaks. Then the next option would be something like these big open models. But now you need a lot more hardware, more memory, and it's still, let's face it, not that fast. So the thing that's supposed to feel smooth ends up feeling slow, expensive, or it just plain breaks. This is where Kakoro fits in. It was trained on less than 100 hours of data but still ranks at the top of leaderboards. It beats much larger models with a fraction of the size. It's Apache 2.0, runs on a CPU, and it flies on Apple silicon. And generates speech honestly insanely fast. So now local voice apps and real-time agents actually start to make more sense. If you enjoy coding tools and tips like this, be sure to subscribe. We have videos coming out all the time. All right, now let me show you this. I'm running all this locally on a Mac M4 Pro. The setup takes like 30 seconds. I'll just run with this pip command here. I am in a conda environment but that's pretty much it. I've got this whole Python script from their official repo. I didn't have to change anything to test this out. It's just drag and drop. We get all these outputs. I can choose a voice and a language right here. But for the first round, I'm just going to leave it set as it is because honestly, it sounds really good. I'm going to run it and then let's listen. Better Stack is the leading observability platform. That makes monitoring simple. It has AI, SRE, logs, metrics, traces, error tracking, and incident response all in one place. Not going to lie, that was that was pretty good and it came out really fast. Now if I flip the switch, let's do French and switch to the French voice, change the text a little bit, and again let's run it. >> Better Stack est la plateforme d'observabilité propulsée par l'IA. Il simplifie enfin le monitoring. >> Okay, now my French is rusty so don't translate that word for word but that sounded pretty good as well. You guys can be the judge of that though. It all saves as a wave file so I can download them as I want. There's no cloud, there's no GPU. That was pretty crazy. So what actually is Kakoro 82M? At a high level, it's a style TTS 2 model with a lightweight vocoder. All that means is it's built to sound good without being huge and that's really the key difference here. Most other options go bigger. So XTTS, Cozy Voice, F5 TTS, hundreds of millions to over a billion parameters. Then cloud tools like 11 Labs or OpenAI, they do solve the hardware problem but now we're paying per request and sending our data out. Kakoro goes the other direction. It's small, it's fast to start, and it runs locally. Plus it uses way less memory. But the downfalls are it doesn't do zero-shot voice cloning out of the box. Instead, it focuses on efficiency and quality that we could actually ship a lot faster. We still get eight languages, 54 voices, and pretty good control with their import Misaki. I can see where all this is going to fit really well in different types of agents but you do not get any type of emotion, which is what I really wanted to see here. An AI without emotion is still going to sound heavily like AI, which I guess can be good at times, right? But it would be fun to play around with that emotion. So why are devs actually using this? Well, if I didn't show you, let's touch on it. Because it fixes the stuff that usually breaks voice features. First is the speed. If your agent pauses too long, it stops feeling real. Kakoro cuts that delay way down. Then the offline use is here. There's no internet, there's no API keys. I don't have any random failures. That's great. The privacy is pretty big because Kakoro keeps everything local. So for me, for a lot of you, that might be a huge win. And finally, cost at scale. Because it's so lightweight, you can run way more instances on one machine. What's great and what's not? I loved it's fast and small. It sounds natural for long-form content. That was really cool. I've played around with a bunch of these. It is Apache 2.0 so you could ship it and after setup, it's basically free. All of these are really, really nice. Now I love those. That was cool. But there are things that I didn't like. The no native voice cloning, it depends if you need voice cloning, okay? Could have had that. Emotion is pretty neutral. Great for narration, it's not great for anything dramatic. I mean, there really is no ability to change emotion here. Plus a non-English voices are still improving. So that needs to be added, maybe not, depends on how you view this. So is it perfect? No. But for the problems most of us actually have, cost, latency, privacy, deployment, it does seem to solve the right ones right now. Play around with it and let me know. Kakoro 82M proves you don't need a massive model to get really good TTS. Smaller means faster, faster means usable, and then usable usually means you can actually ship it. If you're building voice agents or local tools, this is worth trying out. If you enjoy coding tools and tips like this, be sure to subscribe to the Better Stack channel. We'll see you in another video.
