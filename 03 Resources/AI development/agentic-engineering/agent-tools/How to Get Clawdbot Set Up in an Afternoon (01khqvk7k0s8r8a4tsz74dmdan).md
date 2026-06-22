---
title: "How to Get Clawdbot Set Up in an Afternoon"
source: "https://amankhan1.substack.com/p/how-to-get-clawdbotmoltbotopenclaw"
author: "Aman Khan"
published: 2026-01-30
created: 2026-02-18
description: "Some painful lessons and advice along the way"
tags:
  - to-process
  - agent-tools
---

### Some painful lessons and advice along the way


*Just a quick heads up! I’m actually running **two** free lightning lessons next week ahead of our second cohort of [Building AI Product Sense](https://maven.com/aman-khan/build-ai-product-sense?promoCode=aman500), where we’re going to cover:*


* [How to interview product managers for AI fluency](https://maven.com/p/b2bb65/how-to-interview-product-managers-for-ai-fluency)


	+ *How to interview as an AI product manager (i.e. How to get hired as an AI PM)*
* [How to Know What AI Products to Build](https://maven.com/p/593d71/how-to-know-what-ai-products-to-build)


	+ *How to think about new ideas and motivate a team as an AI PM*


You can sign up for the lightning lessons by following the links above!


Also, Build AI Product Sense has been selected for Lenny’s List of Top AI courses (and we hit #1 on Maven in 2025!). [Follow the link for $500 off the sticker price (valid until next Thursday).](https://maven.com/aman-khan/build-ai-product-sense?promoCode=aman500)


[![](https://substackcdn.com/image/fetch/$s_!WLqk!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28271877-146e-44be-81a5-866c292951e1_1600x1600.jpeg)](https://substackcdn.com/image/fetch/$s_!WLqk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F28271877-146e-44be-81a5-866c292951e1_1600x1600.jpeg)
If you are interested but not able to cover the costs because you are not employed, or are a student, we have something for you as well, [just fill out this form](https://forms.gle/xgCr8FB7A7YwFuru7)


Now, on to the post!


## What is Clawdbot?


By now you’ve definitely heard of [Clawdbot/moltbot/openclaw/whatever they decide to name it tomorrow.](https://openclaw.ai/) It feels like this term has broken the internet.


[![](https://substackcdn.com/image/fetch/$s_!6RXT!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3004ace0-e579-4b7e-bad1-18b724bb158e_4364x1440.png)](https://substackcdn.com/image/fetch/$s_!6RXT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3004ace0-e579-4b7e-bad1-18b724bb158e_4364x1440.png)
Here’s my 2 second definition of what this system is. It is basically:


* Claude code running on/as a server
* With “`dangerously-skip-permissions”` turned on (i.e. it can auto accept running commands and making changes without human intervention needed)


In my case, it’s a full agent running on a dedicated machine in my apartment, connected to me via WhatsApp. I text it like I’d text a friend and it texts back. Between our conversations, it can look things up, review my calendar, do research, draft content, and basically act like a chief of staff that never sleeps.


I want to walk you through exactly how I set this up, because the software installation is honestly the easy part. **The tricky part is all the stuff nobody talks about: the hardware, the accounts, the phone number situation.** That’s what this post is really about.


## How I’ve been using Clawdbot + Why this matters


Honestly, the biggest unlock for me for using Clawdbot has been three main use cases:


1. Using it to **manage my [personal operating system on my phone](https://github.com/amanaiproduct/personal-os)**. I’ve been using this from Claude Code (terminal) directly for the past few months, but being able to interact with it from WhatsApp has been super powerful.
2. **Multi-Player Mode:** Adding Clawdbot to WhatsApp groups with friends and just seeing what happens, at least, has some super hilarious conversations as people figure out that this bot can build websites, write code, and overhaul. It is a more powerful version than using the Claude app/web interface because it can take action on your computer.
3. **I built a lot of websites on the go.** For instance, I wanted to understand the Ralph loop better and ask Clawdbot to do research on [Ralph loop](https://ralph-loops.surge.sh/) and build a personal website. I could use it to understand the topic, and it did that in a matter of five to ten minutes. This type of interactive HTML style of learning is something I find super helpful on the go, and it just feels like I can access this agent that can actually take action whenever I need to. I don’t need to be in front of my computer as much anymore.


Clawdbot also accepts voice messages with the OpenAI Speech-to-text API, which is super powerful.


[![](https://substackcdn.com/image/fetch/$s_!wagD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83117236-3eae-4463-ae6d-e19df3b91fef_1185x2375.png)](https://substackcdn.com/image/fetch/$s_!wagD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F83117236-3eae-4463-ae6d-e19df3b91fef_1185x2375.png)
We’re at this inflection point where AI agents aren’t just chat windows you visit. They’re persistent, background entities that live on your computer and do things on your behalf, and I love the ideas this is giving me and others of having the reality of background agents become real. The difference between “I use ChatGPT sometimes” and “I have an AI assistant” is the difference between visiting a library and having a research analyst on staff.


[Peter Yang wrote a great tutorial](https://creatoreconomy.so/p/full-tutorial-set-up-your-247-ai-employee-clawd-molt) that covers the software installation well. I’d recommend reading that alongside this post.


But here’s the thing: Most tutorials start at “install the software.” Nobody talks about the decisions you have to make **before** that. What machine do you run it on? What accounts do you use? How do you get a phone number for WhatsApp without giving up your personal one?


Those are the questions I got stuck on. So that’s what this post focuses on.


## My setup journey (and the problems I hit)


**⚠️ Important disclaimer! ⚠️** [There are a](https://www.reddit.com/r/ClaudeAI/comments/1qn53gl/warning_i_tried_clawdbot_powered_by_claude/) **[lot](https://www.reddit.com/r/ClaudeAI/comments/1qn53gl/warning_i_tried_clawdbot_powered_by_claude/)** [of very legitimate and scary security risks to using Clawdbot,](https://www.reddit.com/r/ClaudeAI/comments/1qn53gl/warning_i_tried_clawdbot_powered_by_claude/) on both your personal and enterprise machines. You should do your own research here before embarking on this journey. My suggestion is to read up on how to harden your own clawdbot before using it so it doesn’t inadvertently leak your personal information on the internet (or worse). None of this is advice.


With that said, let me tell you the story of how I actually got started, including the mistakes, so you can learn from them.


### Step 1: You need a dedicated, always-on computer


Clawdbot runs as a daemon, which is just a fancy word for “a program that stays running in the background, all the time.” Think of it like a server. Your AI assistant needs a computer that’s always on, always connected to the internet, and always available.


Your laptop doesn’t work for this. You close it, it goes to sleep. You take it to a coffee shop, it changes networks. You need a machine that just sits there, plugged in, doing its thing 24/7.


I bought a Mac Mini specifically for this. Here’s why:


- **It’s relatively cheap.** A base model Mac Mini is around $500-600. For what you get, that’s wild.


- **It’s always on.** No battery to die, no lid to close. Plug it in, connect ethernet or WiFi, and it runs.


- **It runs macOS.** This matters if you ever want to use iMessage as a channel (more on that later). macOS is also just a solid Unix-based system for running developer tools. You also get the benefit of airdrop and [screen share](https://www.reddit.com/r/MacOS/comments/1ifss5t/is_there_an_app_built_into_mac_to_remote_desktop/) baked in.


You could also use a Linux machine, an old laptop you keep plugged in, or even a cloud server. But for simplicity and future flexibility, I went with the Mac Mini. Honestly, if you’re already an apple/mac user, this part feels like a no brainer.


### Step 2: Set up a separate Apple ID and email address


Okay so here’s something I thought about after the fact and I’m glad I did. When you set up your Mac Mini, **create a new Apple ID for it.** Don’t sign in with your personal one.


Why? Because Clawdbot is going to have access to this machine’s filesystem. It can read files, run commands, browse the web. It’s powerful, and that’s the whole point. But **you don’t want your personal iCloud (photos, notes, passwords, messages) syncing to a machine that an AI agent has access to**.


Creating a new Apple ID takes about 5 minutes. Just go to appleid.apple.com, make a new one with a different email, and use that to set up the Mac Mini. Keep your personal Apple ID on your personal devices where it belongs.


(I used a simple, separate Gmail alias for this. Nothing fancy.)


### Step 3: The phone number problem (this is the tricky part)


Here’s where most people get stuck, and honestly, I went back and forth on this for a bit too.


I use Clawdbot via Whatsapp to text it from my phone. WhatsApp is the primary channel because it works everywhere, on any phone, with notifications, media support, all of it.


But WhatsApp is tied to a phone number. And here’s the catch: **if you link Clawdbot to your personal WhatsApp, it essentially takes over your WhatsApp account.** Your personal messages, your group chats, everything gets funneled through the Clawdbot connection. You don’t want that.


So you need a separate phone number for Clawdbot’s WhatsApp. And most people’s first thought is “do I need to buy a second phone?” No. You don’t.


Here’s exactly what I did:


**Get an eSIM with a new phone number**


An eSIM is a digital SIM card. Modern iPhones (and most Android phones) support having two phone numbers at once: your regular SIM and an eSIM. You don’t need a second physical phone.


I signed up with a cheap eSIM provider: [tello.com](http://tello.com). There are a bunch of them (Airalo, Holafly, US Mobile, Mint Mobile, etc.). What you want is a plan that gives you an actual US phone number with SMS capability. **This runs about $5-10/month for a basic plan**.


Once you purchase the eSIM plan, you’ll get a QR code or activation link. On your iPhone, go to Settings > Cellular > Add eSIM, and follow the prompts. Within a few minutes, your phone now has two numbers: your personal one and the new one.


**Install WhatsApp Business (separate app)**


This is my personal recommendation, because I use Whatsapp to communicate already. Turns out, there are actually two WhatsApp apps:


1. WhatsApp (green icon) - this is your personal one, keep it on your main number


2. WhatsApp Business (green icon with a “B”) - this is a completely separate app


Download WhatsApp Business from the App Store. When it asks you to register, use your new eSIM phone number. It’ll send a verification code to that number (which your phone receives, since the eSIM is on your phone).


Now you have:


- Personal WhatsApp on your main number (untouched, exactly as before)


- WhatsApp Business on your new eSIM number (this is what Clawdbot will connect to)


You text your AI assistant through WhatsApp Business. Your regular WhatsApp stays completely separate. Nobody in your personal contacts will even know you set this up.


(Pro tip: When WhatsApp Business asks for a business name during setup, just put whatever you want. I put “Aman’s AI.” It doesn’t matter. Nobody else sees this unless you message them from it.)


If you don’t want to use WhatsApp, there are alternatives.


### Step 4: Install Clawdbot on the Mac Mini


Now we get to the software. You’ll need Node.js installed on your Mac Mini first. If you don’t have it, the simplest way is to open Terminal and run:



```
# Install Homebrew (Mac package manager) if you don’t have it
/bin/bash -c “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)”

# Install Node.js
brew install node
```

Then install Clawdbot:



```
npm install -g clawdbot
```

Now run the onboarding wizard:



```
clawdbot onboard
```

This walks you through the setup interactively. It’ll ask you for:


1. **Your Anthropic API key** - This is what powers the AI brain. You can either login with the account you use for Claude Code and provide that key, or go to [console.anthropic.com,](http://console.anthropic.com) create an account, add a payment method, and generate an API key. You’ll pay per usage (roughly $0.1-1 per conversation turn depending on complexity). For most people this works out to a few dollars a day at most.


2. **Channel setup** - This is where you connect WhatsApp.



```
clawdbot channels login --channel whatsapp
```

A QR code will appear in your terminal. Now:


1. Open WhatsApp Business on your phone (the one registered with your eSIM number)


2. Go to Settings > Linked Devices > Link a Device


3. Scan the QR code on your Mac Mini’s screen


That’s it. Your phone and your Mac Mini are now connected. You can open WhatsApp Business on your phone, find the Clawdbot chat, and start texting.


### Step 6: Start the gateway


The gateway is the always-running process that keeps Clawdbot alive and listening:



```
clawdbot gateway start
```

This starts Clawdbot as a background daemon. It’ll keep running even if you close the terminal. Now you can text your AI assistant from anywhere in the world, and it’ll respond.


### Step 7: Set up remote GUI access


Here’s something I didn’t think about until I needed it: you’re going to want a way to see your Mac Mini’s screen from your phone or laptop. Some things (like logging into Google, enabling permissions, or approving system dialogs) require the GUI. And if the Mac Mini is tucked behind a shelf somewhere, you don’t want to go dig it out every time.


The easiest way is to enable Screen Sharing, which is built into macOS. Here’s how:


1. On the Mac Mini, go to \*\*System Settings > General > Sharing\*\*


2. Toggle on \*\*Screen Sharing\*\* (or \*\*Remote Management\*\*)


3. Make sure your user account has access


Important note for macOS Sequoia (15+): Even after enabling Remote Management via the command line, you may still need to toggle Screen Sharing on in System Settings > General > Sharing manually. Sequoia added a system-level permission gate that can’t be bypassed from Terminal alone. If you get “screen sharing is not permitted” errors, that toggle is the fix.


[![](https://substackcdn.com/image/fetch/$s_!gUge!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe4fc6a7-6683-4561-80d1-a2519d0f30f4_2570x1439.png)](https://substackcdn.com/image/fetch/$s_!gUge!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fbe4fc6a7-6683-4561-80d1-a2519d0f30f4_2570x1439.png)Claude Code on tailscale
To use screensharing when you aren’t on the same wifi: Install [Tailscale](https://tailscale.com) on both devices. It creates a secure private network between your devices, so you can VNC into your Mac Mini from anywhere in the world without exposing it to the public internet.


💡 If you get stuck at all, you can also simply copy paste screenshots of tailscale errors or issues into claude code and it should help you debug. Tailscale has a CLI


(Pro tip: Set up Tailscale early. You’ll thank yourself the first time you need to approve a permission dialog from your phone while you’re at a coffee shop.)


## Gotchas and tips (learn from my mistakes)


A few things I wish someone had told me upfront:


**The Mac Mini needs to stay on.** Obvious, but worth saying. Go into System Settings > Energy and make sure it never sleeps. Also make sure it auto-restarts after a power failure (there’s a setting for this). And ideally connect it via ethernet, not WiFi, for reliability. You can also run an app called [amphetamine](https://apps.apple.com/us/app/amphetamine/id937984704?mt=12) to keep the mac awake.


**Set up auto-start on reboot.** You want the Clawdbot gateway to start automatically if the Mac Mini ever restarts. Set it up as a LaunchAgent so it boots up with the machine. The Clawdbot docs cover how to do this, and `clawdbot onboard` might handle it for you.


**Start with WhatsApp, expand later**. Once you’re comfortable, you can add other channels: iMessage (if you’re on a Mac), Slack, Discord. But WhatsApp is the easiest starting point and the one you’ll use most from your phone. Get that working first before adding complexity.


**WhatsApp sessions expire.** Every few weeks (sometimes sooner), the WhatsApp connection will drop and you’ll need to re-scan the QR code. It’s mildly annoying but takes 30 seconds. Just run `clawdbot channels login --channel whatsapp` again and scan from your phone.


**Your API costs will vary.** If you’re just having casual conversations and occasional tasks, expect $2-5/day. **This can go up to much much higher if you are running in API usage mode, instead of using the CLI API key**. If you’re running heavy workloads (long research tasks, lots of web browsing, complex coding), it could be more. Monitor your Anthropic dashboard for the first week to get a sense of your usage.


### Getting started (the shopping list)


Here’s everything you need, all in:


1. Mac Mini (~$500-600, one-time, optional but recommended unless you know what you’re doing


2. eSIM plan with phone number (~$5-10/month)


3. WhatsApp Business app (free)


4. New Apple ID (free)


5. Anthropic API key or Claude Code CLI (pay-per-use, ~$2-5/day for moderate use)


6. Clawdbot and Tailscale (free - npm install)


Total ongoing cost for me: roughly $15-25/day depending on how much I use it. That’s the price of a coffee or two for a 24/7 AI assistant I can text from anywhere.


I genuinely think this kind of setup, a personal AI agent running on your own hardware, is going to become as normal as having a smartphone. We’re early to a wave of personalized agents you can build yourself. The people who set this up now are going to have months of context, memory, and workflow built up by the time everyone else catches on.


If you set this up successfully (or got stuck), drop a message below. I want to hear how it goes. 🤙



### Ready for more?


Subscribe