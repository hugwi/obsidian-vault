---
title: "Open-Source Dictation Is Here… Goodbye Subscriptions"
source: youtube
url: https://www.youtube.com/watch?v=mIL4sZa8M0E
author: "Better Stack"
published: 2026-07-10
created: 2026-08-24
duration: "0:04:33"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# Open-Source Dictation Is Here… Goodbye Subscriptions

![Open-Source Dictation Is Here… Goodbye Subscriptions](https://www.youtube.com/embed/mIL4sZa8M0E)

## Description

FluidVoice is a free, open-source AI dictation app for Mac that turns your voice into clean, polished text entirely on your own machine. 

In this video, we test how FluidVoice compares with Wispr Flow, Superwhisper, and Apple’s built-in Mac dictation, including its local voice-to-text performance, privacy benefits, smart punctuation and formatting. You’ll also see how FluidVoice uses local AI models such as Parakeet and Fluid Intelligence

🔗 Relevant Links
Brew Install Command - brew install --cask fluidvoice
FluidVoice Repo - https://github.com/altic-dev/FluidVoice
Altic - https://altic.dev/fluid


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
0:00 Why Mac Dictation Is Not Good Enough
0:27 FluidVoice: Free Open-Source AI Dictation for Mac
0:55 How FluidVoice Uses Parakeet and Local AI
1:21 FluidVoice Live Demo in VS Code
2:12 FluidVoice vs Apple Dictation, Wispr Flow and Superwhisper
2:43 FluidVoice Benefits: Free, Private and Fast
3:12 FluidVoice Limitations: Mac Only, Model Size and Intel Support
3:43 Is FluidVoice Worth It for Mac Developers?
3:55 Best Way to Use FluidVoice
4:19 FluidVoice GitHub Link and Homebrew Install Command

## Transcript

Just to talk to your computer instead of typing it all out, you end up with another subscription to something like Whisper Flow. And yeah, it's good. You'd think the free thing we already have on Mac would be good enough, but it's not. This is Fluid Voice. It runs completely on your own machine and it's growing in popularity as a strong competitor to Whisper Flow and all the others. Fluid Voice is a free open-source Mac app that turns your voice into text, and every part of that happens on your own computer. Nothing ever gets shipped off to a server somewhere, which is a huge win. Two reasons this is good for us, and they're the exact two things devs complain about. First, your voice and whatever you're dictating might be code or private, and this never leaves your Mac. Second, you're not paying another monthly bill to do it. Here's how simple this is. A model called Parakeet listens and writes down what you say. Then a second local model called Fluid Intelligence acts like an editor sitting right next to you, fixing your capitalization, punctuation, and structure as you talk. You hit one hot key that you set, speak, and the cleaned-up text drops into whatever your cursor is already at. Into Cursor, Cloud, Slack, Mail, Notes, doesn't really care which one. Now, this is super simple [snorts] to spin up, so I'll keep the demo short, too. It's a one-line install. You open it, give it mic and accessibility permissions. Every Mac app makes you do this, so you have to do it anyways, and then you can choose a hot key or use the one built in. So, there's no real difference here. Now, watch this. I hold the key and I just talk normally here. Can you check over my code and make sure it's set up with some good practices to prevent bugs? And it didn't just collapse. Look at what it just did. It capitalized the line, punctuated it, kept my technical words spelled right, and formatted it like an actual comment. I didn't fix one thing. No spinner, no waiting because there's no cloud to actually wait on here. So, where does this actually sit next to everything else? Well, this is actually four times faster than using other ones already out there. And on top of that, this is where it gets interesting. The dictation already on your Mac is free, and for a text message, it's fine. For a commit message or a doc someone actually going to read that, it's probably not so great. Whisper Flow is the paid, so you'd expect it just wins here, but it's subscription, your audio goes to a cloud. For a lot of us, that second part is a deal breaker before we even get to the price. Super Whisper and the rest are good tools. Still costs money, they don't quite match the local cleanup Fluid Voice is actually doing. So, the free one that was supposed to be the weakest is the only one that's free, open source, and does the smart formatting right there on our machine. On Apple Silicon, it's fast enough that you can forget it's even thinking. Now, before you run off and install this, it's great that it's free, right? There's no subscription. It's great that it's private. Our voice stays on our Mac. On M-series machines, it's fast and the formatting is actually pretty good. And it's open source and actively worked on, so problems are getting fixed. But on the flip side of things, it's Mac only right now. iOS and Windows are on the waitlist, so if you live on Windows, this isn't your tool just yet. The editor model is about 3 and 1/2 gigs, so it's a real download. It's not a quick one. It's best, like I said, on the silicon chips. It does run on Intel, it's just slower. And if you dictate in a language other than English, you might have to tune it to get it just right. But you should know all that now, not after you spend 10 minutes trying to download this the hard way. You probably expect me to say it's worth it now, but I won't. For most Mac devs, yeah, okay, this might be worth giving a shot. It's worth it if you don't want another monthly payment just to dictate things for which come on, who does want that? Use it for boring typing, email docs, code comments, Slack messages, heck, talk to Claude. With a Mac and four Pro, it's really nice because it's all local and it's quick. If you need Windows or iOS right now, sorry, but this can't help you. So, here's what you could actually do. Run it as your everyday tool in Mac and keep something cross-platform around for when you're not on Mac. You get the best of both worlds and it costs you nothing for you to back. The GitHub link and the Brew command are both in the description below. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel. We'll see you in another video. >> [music]
