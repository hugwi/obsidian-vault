---
title: "Someone Built Ollama for Audio… and It Runs Locally"
source: youtube
url: https://www.youtube.com/watch?v=CvZuuKkT3Sw
author: "Better Stack"
published: 2026-08-14
created: 2026-08-24
duration: "0:05:48"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# Someone Built Ollama for Audio… and It Runs Locally

![Someone Built Ollama for Audio… and It Runs Locally](https://www.youtube.com/embed/CvZuuKkT3Sw)

## Description

audio.cpp is a new open-source C++ project trying to do for audio AI what llama.cpp and Ollama did for local language models: make models easier to run on your own machine with one native runtime, no cloud dependency, and no Python required at inference time. 

In this video, we take a hands-on look at audio.cpp and test local voice cloning, text-to-speech, speech-to-text, voice conversion, and other audio AI workflows on Apple Silicon.

🔗 Relevant Links
Audio CPP Repo - https://github.com/0xShug0/audio.cpp

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
0:00 Ollama for Audio?
0:26 Why Local AI Was a Python Nightmare
0:54 What whisper.cpp Can’t Do
1:30 Local Voice Cloning Demo
2:23 How audio.cpp Works
2:45 OpenAI Audio API on Localhost
3:00 audio.cpp vs Ollama, whisper.cpp & Piper
3:35 The Problems With audio.cpp
4:33 Who Should Use audio.cpp?
5:20 The llama.cpp Moment for Audio AI

## Transcript

Somebody is quietly trying to do for audio what llama.cpp did for chat bots. Run every model on your own machine. One binary, zero Python. This is audio.cpp and it's doing just that. While it's only about a month old and it still crashes sometimes, it still might be where all this is headed. Let's take a look. Now, rewind a couple of years. Running an AI model locally used to be a pain. A fresh environment for every model, PyTorch versions clashing, CUDA never matching. Then a tiny C++ library called GGML showed up. It's the engine under llama.cpp and whisper.cpp and suddenly you could run a language model or transcribe an hour of audio as a single native binary. No Python, no cloud. It was just fast, local, and it got done. But there was a hole nobody was filling. Whisper.cpp only listens. Speech in, text out, it's done. It can't speak back. It can't clone a voice. It can't make a sound that wasn't already there. So this project, audio.cpp, asked the obvious question everyone skipped. What if one binary did the whole job? Text-to-speech, speech-to-text, voice cloning, voice conversion, figuring out who's talking, even generating music. Roughly 30 model families, one runtime, it's all in this. If you enjoy coding tools that speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now, it's easier if I just show you guys. Here is a 10-second clip of my own voice. I hand that reference straight to audio.cpp. Pure C++ inference on GGML, no Python runtime, nothing really leaving the machine at all here. I type a sentence I just made up. >> This is me talking on my MacBook about audio.cpp. The weather is beautiful. >> And that's me, cloned, reading words that didn't exist a few seconds ago, running entirely on my Mac with the metal back-end. Nothing is leaving the machine. One more different input so you can hear the consistency or where it kind of fails. This is another AI voice test for local voice generation. And there we go. Quick important note, I'm timing this live on purpose. Every speed number this project brags about was measured on an Nvidia 5090, not a Mac. Hold that thought so I can come back to it in a second. So, how does this even pull it off? Well, underneath it's GGML doing the math with back-ends you can swap out. Regular CPU, Nvidia, Vulcan, and metal for Apple silicon. You drive it with flags, pick a task, pick a model family, pick a back-end. There's a command line tool for quick runs and this is the kind of sneaky part we could say. A server mode that speaks the exact same API as OpenAI's audio endpoints. So, code you already wrote for the cloud, point it at localhost, it's the same shape, it's just without the bill. Now, here's why its position is actually really cool. Whisper CPP only listens. Ollama and Llama CPP are text brains. They're not for audio. Cokie and Piper only talk. FFmpeg shoves audio around, but doesn't run a single neural model. Audio CPP is the first thing standing in the middle trying to be all of them in one static file you can copy to another machine and just run. Now, one catch here. A couple models wear an MLX label, but it doesn't actually use Apple's MLX. It's plain GGML on a metal back-end. All right, it's too new to even preach this, so I'm just going to hit on the things that aren't that great yet. Still early. First up, those big numbers. 10 hours of audio in 3 minutes, five times faster than PyTorch. Every single one is a 5090. There's no one single published on an Apple silicon yet. That's the real reason I timed this right now instead of just reading from the state of this. Next up, there's no ready-made download for this. The only pre-built releases are Windows. On a Mac, you compile it yourself with a metal build script and Xcode tools. It's doable, took a little bit of time though. It's not just one click. Then, that no Python promise, it's true when you run it. Downloading and converting the models still leans on a Python helper, but it's not quite there. And lastly, this is essentially one person. A few people are running this now at a very early version and the issue tracker is full of real crashes, memory leaks, and a few models that come out sounding like robotic. This is a fast-moving experiment, so we're going to treat it like one. So, who should actually use this? Well, it's really early, right? So, if you love local AI, you don't flinch at compiling something, and you'll test the output out yourself, this is a blast and the license was clean. It's Apache 2.0. GitHub says no license, but open the file, it's plain Apache. The detector just tripped over the copyright line, it looks like. So, you can legally build a product out of this, but if you need something rock solid to ship now, let it work out its issues, right? It's not quite there yet. But, zoom out though, Llama CPP didn't change everything because its first release was flawless. It wasn't. It changed everything because it took a complete Python mess and it turned it into one fast local binary and the whole ecosystem just piled on top of that. Audio CPP is making the exact same bet, but for sound. Local audio AI collapsing from a dozen fragile Python setups down to a single binary you own. That's the shift that we're kind of watching here, even while the binary's still rough. I've dropped the links for this in the description below. Head on down, check it out. Takes a little bit of time to set up, but it might be worth it. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We'll see you in another video.
