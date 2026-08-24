---
title: "This Shouldn’t Be Able to Run 120B Locally"
source: "youtube"
url: "https://www.youtube.com/watch?v=RkzCAaIV_cQ"
author: "Alex Ziskind"
published: "2026-03-23"
created: "2026-08-24"
duration: "0:12:13"
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
  - "web-design"
  - "youtube-strategy"
summary: "If you want to carry a local and private 120 billion parameter large language model, you might need something like this. Big expensive GPUs and computers. But, what if I told you that 120 billion parameters can fit in your pocket?"
---

# This Shouldn’t Be Able to Run 120B Locally

![This Shouldn’t Be Able to Run 120B Locally](https://www.youtube.com/embed/RkzCAaIV_cQ)

## Description

I paired a tiny AI box with the MacBook Neo—and it seriously changed what I thought was possible with local AI.
Tiiny box: https://tiiny.ai

👀 My favorite external drive (dependable): https://amzn.to/3Os9Wi3
👀 Thunderbolt 4 dock: https://amzn.to/3yVRicC

⚡ *Other gear I use:* https://www.amazon.com/shop/alexziskind

🎥 Related Videos 🎥
🧬🐍 Mac Studio CLUSTER vs M3 Ultra 🤯 - https://youtu.be/d8yS-2OyJhw
🧳🧰 Mini PC portable setup - https://youtu.be/4RYmsrarOSw
🍎💻 Dev setup on Mac - https://youtu.be/KiKUN4i1SeU
💸🧠 Cheap mini runs a 70B LLM 🤯 - https://youtu.be/xyKEQjUzfAk
🧪🔥 RAM torture test on Mac - https://youtu.be/l3zIwPgan7M
🍏⚡ FREE Local LLMs on Apple Silicon | FAST! - https://youtu.be/bp2eev21Qfo
🧠📉 REALITY vs Apple’s Memory Claims | vs RTX4090m - https://youtu.be/fdvzQAWXU7A
⚡💥 Thunderbolt 5 BREAKS Apple’s Upcharge - https://youtu.be/nHqrvxcRc7o
🧠🚀 INSANE Machine Learning on Neural Engine - https://youtu.be/Y2FOUg_jo7k
🧱🖥️ Mac Mini Cluster - https://youtu.be/GBR6pHZ68Ho

* 🛠️ Developer productivity Playlist - https://www.youtube.com/playlist?list=PLPwbI_iIX3aQCRdFGM7j4TY_7STfv2aXX

— — — — — — — — —

❤️ SUBSCRIBE TO MY YOUTUBE CHANNEL 📺

Click here to subscribe: https://www.youtube.com/@AZisk?sub_confirmation=1

Join this channel to get access to perks:
https://www.youtube.com/channel/UCajiMK_CY9icRhLepS8_3ug/join

— — — — — — — — —

📱LET'S CONNECT ON SOCIAL MEDIA

ALEX ON TWITTER: https://twitter.com/digitalix

— — — — — — — — —


#macstudio #tiiny #llm

## Transcript

If you want to carry a local and private 120 billion parameter large language model, you might need something like this. Big expensive GPUs and computers. But, what if I told you that 120 billion parameters can fit in your pocket? The first time I heard of something like that, Steve Jobs was putting a thousand songs in my pocket. Well, this is a slightly nerdier version than that. And no, I was not happy about Steve Jobs putting stuff in my pocket. Stay out of my pocket, Steve. For the past few years, AI hardware has been moving in one direction. Bigger GPUs, bigger servers, bigger clusters. And if you watch this channel, you know I've built a few of those. Now, something very different is starting to show up. This is Tiny AI Pocket Lab. And according to the company, this thing can run models up to 120 billion parameters locally. And that's a wild claim. So, I need to check it out. And that matters because one of the best-known 120 billion parameter models right now is still GPT-OSS-120B. It's not the newest model, but it's well-known because it's OpenAI's first open weight model. And OpenAI says GPT-OSS-120B is best with at least 60 GB of VRAM. And it also says it runs more efficiently on a single 80 GB GPU. That means I won't be able to even run it on my expensive RTX 5090, which only has 32 GB of VRAM. So, I want to check out this Tiny AI Pocket Lab with this MacBook Neo that only has 8 GB of memory. Just to give you an example, this is a 4 billion parameter model running on the MacBook and getting about nine tokens per second. So, let's find out whether this little box can actually pull this off. First of all, this thing really lives up to its name. This is my iPhone 16. This is this thing. I also have to weigh it. My iPhone with the case weighs 228 kg. Kilograms, excuse me. 228 g. I could have guessed that. And Tiny weighs 305. And the reason I'm pairing it up with this MacBook Neo is because the MacBook only has 8 gigs of memory. There's no way you'll be able to run anything bigger than a 4 billion parameter model. Well, maybe. I'm doing a separate video on this. But one of the biggest things about large language models and running them locally is space. 256 GB SSD here. I'm already almost out of space here and I just have software development tools on there. >> [music] >> Imagine loading LLMs. This thing comes with 1 TB of SSD space. So, you'll be able to load up a bunch of models. It also has its own CPU and of course, it has the memory. 80 GB of it. So, it can run larger models. Now, to get going with this, I'm going to connect this thing with a USB-C cable to PC, it says. Now, it does operate up to 60 W, 30 W TDP. So, you can actually power this externally by plugging in a USB adapter here into the power section of it. And I'm going to power it on. There's a little light right there. It shows me that it's on. It shows it up as a drive and I just need to double-click on this to set up the software. Tiny OS, pop that open. And after login, you just get to the chat screen. And right there, I'm already chatting with this thing. I have chat available, I have agents available, I have an agent store. And all these different models that I can try. There's GPT-OSS-120B that I was talking about. Let's click on that. I'm going to try that out. And there it goes. Let's give it a little bit of a longer prompt. Just so you get a sense of how fast it's going on a 120 billion parameter model. This, by the way, is the default chat interface. Now, people watching this channel might be interested in the fact that they have an SDK, not just the chat interface. That way you can interact with the models programmatically. Pip install Tiny SDK. Boom. That's it. Now, I can use this in my programs, load up a device, load up the models in my Python code. Or I can use this right from the terminal. So, I can do tiny run OpenAI-GPT-OSS-120B. And now I can interact with this fully through the command line. And they weren't kidding. It's 18 tokens per second for this model. Now, this is completely offline and completely not connected to the internet. Everything is right here. You only have to connect to the internet if you want to download new models. And so far, these are the ones that I have available to me that I've already downloaded. GPT-OSS-120B, Qwen-3-30B, Qwen-3-Coder, image creation. We'll take a look at that. And out of the ones that are available that I haven't downloaded yet, GLM-4.7-Flash looks to be pretty interesting. So, I'm going to click on get. Network is offline. Please check your connection. So, before I can use anything else, I would need to connect this to Wi-Fi so I can download the new model. So, there I am downloading GLM-4.7-Flash. And what's nice here is that it's not going through the machine. Even though you think, oh, but isn't it just use the connection and use the Wi-Fi that's on this thing? Well, that's the whole idea is it's own device. We don't need to take up space on the computer to take up space on the device. So, the model goes directly to the device instead of going through the computer where you might not have enough space. So, there's 120B answering me. Let's ask it to write a story. And while it's thinking about it, you can see the approximate speed that it's going at. Look at our activity monitor. Look at the memory usage here. 5 GB, that's pretty normal. There is no spikes or anything here. No memory pressure. Nothing is being used on this computer. So, I can keep using this as is. All the processing is done on Tiny Pocket Lab. All right, thank you. That's a very long story. We don't need that. Let's load up a coding model. Did my GLM Flash download yet? It's still downloading. But we do have Qwen Coder 30B. Hey camera, what are you looking at? The screen? You like what you see? I like it. Qwen Coder downloading. Got to do something while it's loading, right? New chat and hello. And Qwen Coder is much faster, obviously, than 120 billion. This one is only 30. And this is not a thinking model, so it answers right away. But why would I be interested in a coder model? Well, because this is a software dev channel. So, how can we use this besides chatting with it as software developers? Well, first of all, there's a bunch of different agents you can use right here on the left. Stable Diffusion, chat memos, an AI assistant. There's a bit too many different agents to go into in this video, but let me know if you want to learn more about these and maybe I'll do a follow-up. But there's also a agent store where you can go in here. And obviously, this is the kind of thing that's going to keep getting updates. More and more stuff is going to be active here. Now, here is the dashboard. This shows me how many tokens I've used, which models I used, and how many tokens per model. This is really handy because it gives you a little bit of visibility and insight into how you're using your resources. For example, if you're developing a solution locally that's going to be deployed somewhere else, you can kind of gauge the token use and estimate costs later if you're using some third-party provider. Pretty handy. Now, one thing I have not tried yet that I'm about to. Always scary doing this first time on camera, but there's an API base URL and an API key that will allow you to use Tiny in an OpenAI compatible interface. And in fact, if I take that weird-looking base URL and I go to the browser and plug it in, it'll tell me exactly what's going on. So, here's /models endpoint. And yeah, that is an OpenAI compatible endpoint. It tells me that Qwen-3-Coder in fact is loaded. So, here I am in VS Code and I've configured Qwen-3-Coder-30B to be my custom AI agent inside my editor. And now, I can talk to it through my VS Code interface. What does this file do? This file is a batch script for Windows that automates the setup and execution of a Python project. That's right. So, it has tool calling enabled. It has the ability to read and edit files and so on. And the speed is not terrible. Now, I don't have to take my MacBook Pro on an airplane. I can travel light with this stuff. Here's an example of a smaller model. Qwen-3-8B. And that's pretty [music] fast. Try again. Write a story. Now, what's funny is that the MacBook doesn't have a fan at all. But the Tiny Box, the Pocket Lab, does make up for that because it has its own fan. It definitely needs to cool that NPU that's doing the processing. So, the only thing I hear here in this office is the Tiny Pocket Lab. It's just a persistent fan going. You can definitely hear it. It's not silent, but it's not like wildly annoying. By the way, when you use this inside VS Code as a coding agent, you go through a lot of tokens. Just that couple of queries that I made, I'm already over 20,000 tokens. Another win for local, right? Cuz you get an unlimited number. GLM-Flash finally downloaded and now I can start talking to it. So, now I have even more models stored on this thing that I can anytime just pull up and use whenever I want. Let's check out SD WebUI. A cat in a hat. Do you think it's going to draw a cat inside a hat or a cat wearing a hat? Instead, it draws a red square. So, it says here, please select a text-to-image model from the status bar. So, you can only have one model loaded at a time. And right now, I have GLM-4.7 loaded, as you can see here, Flash. Which makes that model available to all the different tools and agents. If I want a stable diffusion type of model to be available to the stable diffusion UI, then I need to load up the Z Image Turbo or another text-to-image model is going to be available, which unloads GLM-4.7-Flash. Makes sense, [music] right? You have a limited number of resources to work with, so unloading a model before loading a new one makes sense. All right, let's try generating that. And there it goes. Looks like stable diffusion, all right. Any guesses? I just see a cat. I see zero hats in that picture. A cat playing guitar. Now, if you know a little bit more about stable diffusion than I do, then you might know what all these things do and the best options to select, but you're not me and I don't. So, I'm going to just hit generate here. >> [laughter] >> Hey, look at that. We're getting a cat playing guitar. What a cute little cat. What's cool about this interface is that it actually tells you what models are available. What models you already have downloaded, the ones with the check mark, and the models that you could still get that'll work with stable diffusion. Now, one of the questions that comes to mind is how is it that such a tiny little device with an NPU can compete with, >> [music] >> I don't know, an internal GPU like, for example, Apple Silicon. So, here's Tiny on the left running Qwen-8B, which is a bigger model than the one I'm running on the right. That's quant 34B. And let's take a look at how that looks. I'm going to go enter and enter here. They're not at the same time, but close enough just to give us a sense of how quickly things are generating. Hello. There it goes. Okay, it's thinking. The one on the right is taking a little bit longer. And you tell me, which one do you think is faster here? I think the NPU one is faster even though it's a larger model. The one executing on the Mac is actually running MLX. Now, this is a MacBook Neo, so it's not going to be super fast like a M4 or M5 Max machine. But we're talking about really low power consumption, lasting a long time. How is it the Tiny is doing that? Well, the foundation of that can be found on GitHub. Tiny AI PowerInfer is the name of the repository. You can go check it out. This is kind of like the backbone of the product. Look at that. GitHub trending number one repository of the day. PowerInfer is basically a CPU/GPU LLM inference engine leveraging activation locality for your device. I don't know what that heck that means. But basically, that means keeping the actively used, the hot parts of the model constantly active and alive while putting some of the ones that are less commonly used to sleep. It's like a clever way of managing the model so that it can run faster. You can get more info on tiny.ai website as well as their Kickstarter campaign where you can sign up and get this thing at a discounted rate if you're an early backer. Now, I wanted to play with this thing ever since I saw this at CES, and I think it's really cool. Now, this thing is not going to be a replacement for a monster GPU rig. It's slower, and right now it's more curated than a fully open DIY setup. That's kind of clear. But if you want a small and private low-power box that can bring meaningful local AI to a much weaker laptop or perhaps a mini PC that's less capable, that's where this starts to make a lot of sense. And yes, being on Kickstarter makes it a harder sell for some people, which is totally fair. But the idea here is genuinely interesting. And in actual use, I think it makes a stronger case than you might expect. Let me know your thoughts in the comments down below. I look forward to checking it out and reading it. I do read all your comments. And I think you would like this video next. Thanks for watching, and I'll see you next time. >> [music] >> Yeah.
