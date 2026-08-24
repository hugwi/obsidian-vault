---
title: "These AI Glasses Let Me Code Anywhere"
source: youtube
url: https://www.youtube.com/watch?v=Uh7JoAGTfHc
author: "Mile High Engineer"
published: 2026-01-20
created: 2026-08-24
duration: "0:07:08"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# These AI Glasses Let Me Code Anywhere

![These AI Glasses Let Me Code Anywhere](https://www.youtube.com/embed/Uh7JoAGTfHc)

## Description

My dog needs two walks a day, and she isn't afraid to let you know about it. I wanted to use Claude Code while walking her, so I built a portable coding setup by plugging the AR glasses into a Raspberry Pi. Now I can code on the go!

In this video, I'll show you the build in action using Viture XR glasses and a Raspberry Pi 5. Watch me ship a feature on a little CLI todo list app — all while walking the dog.

I’m already working on my next project, so don’t forget to subscribe to catch that one when it comes out.

Github repo: https://github.com/MileHighEngineer/code-glasses

Instagram: https://www.instagram.com/milehighengineer/
Patreon: https://patreon.com/c/MileHighEngineer

## Transcript

I'd love to tell you that the inspiration for this project was some grand vision for how we'll interact with coding agents in the future, but honestly, it was her. She's a demanding dog. I recently worked on a really interesting software project with a tight timeline. She didn't care if I was in a flow or not. It was time for the walk. She is very persuasive. Before I left the house, I would try to kick off a couple of clawed code tasks to finish while I was out. But these AI agents are like interns. If you leave them alone, they panic. So, I built these glasses. They let you take your agent with you. They actually work great. You can also use them while you do the dishes or while you exercise and lift weights or eat lunch with your wife, playing with your kids, driving a car. All right, now let's get into how this came to be. Okay, here's my plan for this. We have our user and some small computer that's running our software agent. In this case, I'm going to use clawed code. We need some sort of display so that the user can see and monitor the output. We need some headphones so the user can both speak to the agent and listen to the response. And last, we might need some keyboard or other interaction device so that the user can interact more deeply with the agent. This should satisfy the main requirements of being able to use an agent on the go and be able to interact with that agent. All right, let's take a look at the hardware I came up with. I settled on using a Raspberry Pi to run the agent. The output of that Pi is connected to these augmented reality glasses, which are small and lightweight. The two are connected with this dock which provides power to the whole system. For audio, we're just using a standard pair of headphones. And last, we have a pushto talk button, which is connected to the GPIO pins on the Pi and allows you to select when you want to speak to the agent. All of the hardware fits nicely into this extremely good-looking fanny pack. This is the one I could find that has a mesh front so that the electronics can breathe. It's called the Sand Dipper, and it's made for streamlining your shell collecting excursions. See, all this just fits right in and zip it up. And that's all there is to it. Okay, now let's take a quick look at the software. The user talks into the microphone and that's recorded by this audio service. Those files are written to disk and picked up by the transcription and processing service. We use open AI whisper to convert that audio into text and send any commands to claude code. Alongside that, the texttospech service monitors the output of the claude's code session and speaks any relevant output back to the user. And with that, let's go on a little adventure and see how this works in the real world. All right, here's the plan. We're going to take a walk, me and Pup, and uh we're going to ship a feature on this demo app. I built and take you along. I'll be showing a recording of the Raspberry Pi screen, but this is what it would look like if you were wearing the glasses. Also, you'll be able to hear the output from the text to speech service that reads out the claud code messages. I did botch the screen recording, so some of the right part of the screen is cut off. The demo app is a simple CLI to-do list. I want to build a feature that adds prioritization to the tasks. Can you put together a plan for this? I've sped up some of the sections like this one where Claude's just sitting here thinking. >> I'll help you plan a prioritization feature for the tasks. Let me enter plan mode to explore the codebase and design a comprehensive implementation approach. Great. I now understand the current task manager structure before I design the implementation plan. I need to clarify a few things about how you want prioritization to work. To >> navigate the screens like this, you can either use voice commands or the keyboard. So you could say down arrow, enter, etc. >> User answered Claude's questions. Perfect. Now I understand your requirements. Let me design the implementation approach. One major thing I overlooked in the software for this V1 is scrolling. So there's no way to scroll using voice commands. Um here I'm just blindly accepting the changes um as we usually do, but you know, it'd be nice to be able to see this and all the code snippets as well. So, I'll get that taken care of in the V2. Now, let me run the tests to verify everything works correctly. Perfect. All 28 tests passed. Now, let me verify the functionality works with the actual CLI commands. Excellent. The migration worked. All existing tasks now have medium priority. Let me test adding a new task with gig. All right. We made it to our normal turnaround point and uh feature's done. So I'm going to tell it to commit it and push it. Can you commit and push this? Start walking back. >> Perfect. Now I'll commit and push these changes. The changes have a comprehensive task prioritization feature. Great. The commit was successful. Now let me push to the remote repository. mostly a success. There's a few things I need to work on. The uh the speech back is filtering out a lot of things. Scrolling. Need to be able to scroll. Keyboard is helpful, but it's hard to use. Well, it's mostly cuz it's cold. I don't know. That's about it. The button works great. I can see really well through the screen. I can see the screen, too. Really, really pleased here. I'm really pleased with this solution. I think it'll provide me uh a nice way to ruin my walks with my dog. All right, see you later. All right, and that's it. There's plenty of improvements we could make for a V2, but what do you think? Any improvements you'd like to see? If there are some good ideas, maybe I can do a follow-up. Anyway, thanks for watching.
