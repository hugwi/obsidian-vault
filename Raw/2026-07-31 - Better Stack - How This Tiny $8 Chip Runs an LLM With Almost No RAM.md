---
title: "How This Tiny $8 Chip Runs an LLM With Almost No RAM"
source: youtube
url: https://www.youtube.com/watch?v=0qXVMt3pIjU
author: "Better Stack"
published: 2026-07-31
created: 2026-08-24
duration: "0:08:14"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# How This Tiny $8 Chip Runs an LLM With Almost No RAM

![How This Tiny $8 Chip Runs an LLM With Almost No RAM](https://www.youtube.com/embed/0qXVMt3pIjU)

## Description

A developer got a 28.9-million-parameter language model running entirely offline on an $8 ESP32-S3 microcontroller, a chip with just 512KB of RAM, using a memory trick borrowed from Google's Gemma architecture called Per-Layer Embeddings. In this video we break down how the trick actually works, reproduce the entire training and flashing process ourselves from a bare board, and put the model through some prompt tests of our own, including one it stubbornly refuses to follow. If you're curious how far you can push AI onto hardware that was never meant to run it, this one's for you.

🔗 Relevant Links
Esp32-ai: https://github.com/slvDev/esp32-ai
build_and_flash.sh: https://gist.github.com/andrisgauracs/ce459630660f82cf4ca7e43aa81604c7
run_prompt.sh: https://gist.github.com/andrisgauracs/e84b842d0f5e301485ecbf6654b0838e

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
00:00 Running an LLM on an $8 Chip
00:43 The ESP32’s Memory Problem
01:12 How Did They Make It Work?
01:30 The Per-Layer Embedding Trick
02:04 Fitting 28.9 Million Parameters
02:36 What This Tiny LLM Can Actually Do
02:58 TinyStories and Karpathy’s llama2.c
03:41 Building It Ourselves
03:47 Choosing the Right ESP32
04:23 The One-Shot Installation Script
04:52 Training and Flashing the Model
05:24 Testing the LLM at 9 Tokens per Second
05:38 Trying Custom Prompts
06:21 The Star Wars Prompt Test
06:51 Is an ESP32 LLM Actually Useful?
07:23 Final Thoughts

## Transcript

This is a 28.9 million parameter language model generating text right now one word at a time on a chip that costs about $8. There's no Wi-Fi, nothing is being sent to a server. Everything is happening inside an ESP32-S3, a microcontroller with less RAM than a computer from the '90s. This is insane. How is this actually possible? What's the magic behind it and how can we build something similar? Well, those are all good questions that we're going to look at in today's video. [music] It's going to be a lot of fun, so let's dive into it. So, the ESP32-S3 is a chip that gives you 512 KB of SRAM. And that is the amount of fast memory this chip can compute with. Normally, if you would attempt to run an LLM inside of it, the whole model would have to fit right in there. The last language model anyone got running on a chip like this topped out at 260,000 parameters. So, this one holds about 110 times more. And the person who pulled it off is a Ukrainian developer Slava S. So, what's the magic trick? How did they do it? How did they fit a 28.9 million parameter model on an $8 chip? Well, the workaround comes from an idea Google used in Gemma. It's called per-layer embeddings. Most of a language model's parameters do not compute anything. They sit in an embedding table that just gets read from. If most of your parameters are only ever looked up, they don't need fast memory. So, you can get away with leaving that table sitting in a slow cheap flash memory and only pull the rows the current token needs. And the small part that actually computes and thinks about the next token, the attention head and feed forward stays in SRAM. Okay, that's the compute part, but the question still remains, how do we fit such a big model onto such a tiny chip? So, the 25 million row table lives in flash memory, and that's the biggest chunk of the model's whole 28.9 million parameters. And flash is cheap and huge on this particular chip. It has 16 megabytes of it. So, instead of trying to squeeze that table into the same 512 kilobytes of SRAM, it just stays parked in flash. We pull out about six rows from it, one for each of the model's six layers. That's roughly 450 bytes total. Now, before you get too excited, I do have to address the fact that this is a very dumb simple model. This won't be your typical GPT-style LLM. It won't give you code generation or answer questions about difficult topics, because if you tried to train a normal model this size on a normal data set, 28 million parameters would just give you gibberish. But this model itself is trained on tiny stories, a data set built by researchers at Microsoft, written deliberately simple enough that even a tiny model a few million parameters can learn to write them coherently. And running it in plain C on a chip with no operating system and no Python interpreter, that idea comes from the famous Andre Karpathy's llama2.c project, which showed us that you could train a small language model and run inference on it using nothing but a few hundred lines of portable C. And that is the blueprint this entire project is built on. Without Karpathy, this probably wouldn't even be possible. So, that's how it works in a nutshell. Now, let's actually try to build it on our own and run it on the chip to see how it performs. To actually build this ourselves, the first thing you need is the right hardware. Specifically, an ESP32-S3 with 16 MB of flash and 8 MB of PS RAM. That's the N16R8 variant. And this is really important because remember when we talked about that 25 million row table living in flash? Well, by itself, once trained and exported, it comes to about 15 MB. But boards with 4 or 8 MB of flash simply won't hold it. So, if you're shopping for a board to follow along, that's the one spec you should check first. Now, when I first went through the project's actual instructions, the setup was scattered across a few different files and it assumed a fair amount of contacts I didn't have going into it. So, instead of walking you through it exactly as written, I put together a single one-shot script that does everything. Checks the board, installs the toolchain, prepares the data, trains it, exports it, verifies, builds, and flashes it all in one go. So, let's go ahead and run that script. And one quick heads-up, if you're following along, the whole script takes about 25 minutes to finish and probably that's the same time it would take you doing it step-by-step. It's just because there are so many separate commands you have to baby sit. And most of the time is actually spent on training the tiny stories model. That takes about 13 minutes on my MacBook. And once the training is done, you'll see the LEDs on the panel start flashing and that's an indication that we're about to load the model. And once it's loaded, here we can see the first basic example of a story of a little girl and indeed we're getting those nine tokens a second. But you'll notice that at a certain point it will restart the story again. So, the model is going in some kind of a loop. And if you want to give it a custom prompt, I've also included a sample script you can use to run your own custom prompts. So, for this example, let's start a story about a robot. And another thing to note is that if you change the prompt, you will have to reflash the ESP32 again, and that's a limitation of this method. It can only play back one prompt that is pre-flashed at a time. And as you can see, we do get a mention of the robot in the story, and the story is indeed a bit different this time. But notice what happens after the end of the paragraph. We get back to the story of the little girl. So, I have no idea why this is happening, but clearly the model tends to steer back to that one specific story about that little girl. And let's do another example, and this time let's use the famous phrase that is written at the very beginning of every Star Wars movie, and let's see where that takes us. So, this is an interesting one. We can see that the model immediately drifts back to the little girl narrative again, and I'm assuming that for a model of this size, it doesn't even understand what a galaxy is. So, probably that's why it's ignoring our specific prompt in this case. And once again, we see that the next paragraph starts the same story. So, although this experiment is impressive, and seeing a model produce nine tokens per second on a tiny microchip is genuinely mind-blowing, it's still very much a very limited proof of concept. As we saw, no matter what you ask the model, it will always drift back to storytelling because that's what it's trained on. But if you found this test interesting, I also did another video in a similar realm where I tested out if a first-gen Raspberry Pi could actually run a real LLM locally. So, go check out that video if you're interested. So, there you have it, folks. That's how you run a 28.9 million parameter language model on an ESP32 chip. We tested it, it works. So, kudos to Slava for making this project. But what are your thoughts on this experiment? Do you see any real-world examples where such an implementation might be useful. Give us your thoughts in the comments section down below. And folks, if you like these types of technical breakdowns, please let me know by smashing that like button underneath the video. And also, don't forget to subscribe to our channel. This has been Andres from Better Stack, and I will see you in the next videos. >> [music] [music]
