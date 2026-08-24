---
title: "One Developer Just Made NVIDIA Optional"
source: youtube
url: https://www.youtube.com/watch?v=raUm7RAS7Qs
author: "TheVibeFounder"
published: 2026-07-13
created: 2026-08-24
duration: "0:01:08"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# One Developer Just Made NVIDIA Optional

![One Developer Just Made NVIDIA Optional](https://www.youtube.com/embed/raUm7RAS7Qs)

## Description

What if you could run one of the world's largest AI models...

Without an NVIDIA GPU?

That's exactly what Colibri makes possible.

A developer built a new inference engine that runs GLM-5.2 (744B parameters) on a laptop with just 25GB of RAM.

No CUDA.
No PyTorch.
No cloud.

Here's the trick.

Instead of loading the entire model into memory, Colibri only keeps the active "experts" in RAM and streams the rest from your SSD when they're needed.

Think of it like Netflix.

You don't download the whole movie.

You stream only the part you're watching.

Setup is simple:

• Clone the repository
• Download the GLM-5.2 INT4 model
• Point Colibri to the model
• Start chatting locally

Or run it as an OpenAI-compatible API endpoint and connect your existing apps with a single Base URL change.

The biggest shift isn't replacing GPUs.

It's making frontier AI accessible on commodity hardware.

Every month, the hardware barrier gets lower.

And that's great news for builders.

Comment AI and I'll send you the GitHub link.

#AI #GLM52 #Colibri #OpenSourceAI #LocalAI

## Transcript

Nvidia CEO [music] did not sleep last night. Because one developer in Italy just proved you do not need his GPUs. He took GLM 5.2, the 744 billion parameter model that beats the ones you pay for, and ran it on [music] a laptop with 25 gigs of RAM. Zero graphics card. And he gave the code away. So, welcome back guys. This is day 159 building you 100 X. [music] The project is called Colibri. Zero dependencies. Only about 10 gigs of that model is actually thinking at any moment. The rest is 21,000 experts just sitting there waiting to be called. So, he keeps the thinker in your RAM and streams the experts off your SSD on demand. Like Netflix streams a movie instead of downloading it. Now, here is how you run it. Step one, clone the repo, go into the C folder, and run setup.sh. It builds itself. No Python, no CUDA, no PyTorch. Step two, download the model, GLM 5.2, the INT4 version. 370 gigs on your drive. Step three, point Colai at that folder and type Colai chat. And boom, you are talking to a 744 billion parameter model on your own laptop, [music] offline. Step four, type Colai serve instead and it turns into an OpenAI endpoint. Change one line in your code, the base URL. Same app, zero token bill. Nothing ever leaves your machine. Nvidia sells you the GPU. One developer just made your hard drive do the job. And he gave it away for free. Comment AI and I will send you the GitHub link with the full install guide. Follow for more such videos.
