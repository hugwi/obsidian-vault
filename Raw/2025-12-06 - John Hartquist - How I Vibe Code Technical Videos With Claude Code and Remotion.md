---
title: "How I Vibe Code Technical Videos With Claude Code and Remotion"
source: "youtube"
url: "https://www.youtube.com/watch?v=z7Bkf3Vc63U"
author: "John Hartquist"
published: "2025-12-06"
created: "2026-08-24"
duration: "0:08:06"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "anthropic"
  - "engineering"
  - "mcp"
  - "video-gen"
  - "voice-ai"
summary: "In this video, I'm going to show you how I create and edit videos with natural language using Claude Code and Remotion. If you've ever tried creating videos, even simple ones, you know the pain. Scrubbing through timeline footage, slicing out the awkward pauses, gathering all the assets, sequencing them in the right place, exporting."
---

# How I Vibe Code Technical Videos With Claude Code and Remotion

![How I Vibe Code Technical Videos With Claude Code and Remotion](https://www.youtube.com/embed/z7Bkf3Vc63U)

## Description

In this video, I show how I create and edit videos with natural language using Claude Code, and Remotion. The entire video was built using the starter template linked below.

GitHub Repo: https://github.com/jhartquist/claude-remotion-kickstart
Inspired by: https://x.com/trq212/status/1947706205172068624

─────────────────────────────
THE STACK
─────────────────────────────
• Claude Code — AI coding assistant in the terminal
• Wispr Flow — voice dictation to Claude Code
• Remotion — React framework for programmatic video
• Playwright MCP — browser automation, screenshots
• Replicate MCP — Veo 3.1 video generation, Nano Banana Pro images
• ElevenLabs MCP — text-to-speech voiceovers
• Deepgram — word-level transcription for timing

─────────────────────────────
CHAPTERS
─────────────────────────────
0:00 Introduction
0:37 Why Remotion + Claude Code
1:16 MCP server integrations
2:01 Getting started with the template
2:13 Remotion Studio overview
2:38 Demo: Building slides step-by-step
3:33 Demo: Generating AI video with Veo 3
4:59 Demo: Generating images with Nano Banana
5:35 Demo: Creating voiceovers with ElevenLabs
6:34 Demo: Transcription and timing with Deepgram
7:11 Final result showcase
7:56 Closing thoughts

─────────────────────────────
CONNECT
─────────────────────────────
GitHub: https://github.com/jhartquist
X/Twitter: https://x.com/johnhartquist
Bluesky: https://bsky.app/profile/johnhartquist.com
LinkedIn: https://www.linkedin.com/in/john-hartquist/

─────────────────────────────

What kind of videos would you make with this? Let me know in the comments—if there's interest, I'll do a deeper tutorial.

#ClaudeCode #Remotion #AIVideoEditing #Veo3 #NanoBanana #ElevenLabs #WisprFlow #Deepgram #MCP #Anthropic #ReactJS #TypeScript #DeveloperTools #TextToVideo #ContentCreation #CodingTutorial #WebDev #AITools #ProgrammaticVideo #replicate

## Transcript

In this video, I'm going to show you how I create and edit videos with natural language using Claude Code and Remotion. If you've ever tried creating videos, even simple ones, you know the pain. Scrubbing through timeline footage, slicing out the awkward pauses, gathering all the assets, sequencing them in the right place, exporting. It's tedious, time-consuming, and it breaks your flow. As a software engineer, I use Claude Code every day to help me understand code bases, track down bugs, and vibe code, I mean, architect new features. I also use it to automate workflows and quickly spin up prototypes. It can be a very powerful tool. Recently, I've been experimenting with Remotion, which is a React library for rendering videos programmatically, frame by frame. Here's the thing, Claude Code is really good at writing React code. React is one of the most popular web frameworks today, and Claude excels at creating visuals with it. When you combine Claude Code with Remotion, you can automate the tedious parts of video editing in a similar way to how it's used for general programming. I'm mainly interested in creating technical videos, tutorials, demos, that sort of thing. With Remotion, you get all the benefits of the web ecosystem. Code snippets with syntax highlighting, diagrams, smooth animations, anything you can build with React. With Claude Code, you also get the full power of MCP servers. I can tell Claude to use the Playwright MCP to open a browser, navigate to a documentation page, and take a screenshot. Then that goes straight into my video. With the Replicate MCP, I can use a library of models to generate audio, images, b-roll footage, or even talking head videos using tools such as Nano Banana, VO3, Eleven Labs, etc., all without leaving the command line. And because it's all code-based, I can create reusable templates and tweak them just by telling Claude what I want. Everything is stored in Git, and I can continue using the tools that I already love. I've put together a Claude and Remotion starter template that you can use to make your own videos. The link is in the description. After downloading the code from GitHub and installing the dependencies, we can run Claude straight away. Run the dev server in the background. This pulls up the Remotion Studio, where you can preview while editing the video. There's a few examples included for reference, so we can see this one has a title segment and then a content segment. And then there's also some pre-built components with some previews. For example, title slide with a fade in, content slide. Let's add a title slide that says, "How to explain things to programmers." Let's create a new step component. On each step, we'll have the text in the top left say, "Step one." And then some supporting text. We'll have three steps. Step one, add some diagrams. Step two, show some code. Step three, sprinkle in some AI. For step one, let's add a fancy mermaid diagram. For step two, let's add a code snippet from this repository and have it animate over time. For step three, let's generate a video. Generate a 6-second clip of the most advanced AI imaginable. For this step, Claude is going to use our generate video command, which calls the Replicate API, and we'll generate a video using VO3.1 fast by default. We can look in our assets folder here. Once the video is ready, it'll show up, and we can preview it. Okay, let's preview that video. Cool. And back to our composition. It looks a little small. Let's make the video a little bit bigger. Let's add one more slide to the end that just says, "Thanks for watching." Let's update the font to be monospace and update the color scheme to be gruvbox. Make sure the text is centered on the first title slide. Maybe make the font slightly smaller. Let's generate a better background image. It should still follow the gruvbox color scheme and look technical, but clean and modern, and use it for the background for all of the slides. Again, Claude is using the Replicate API to generate images using the new Nano Banana Pro, and it'll place them images in the assets folder that we can preview over here. Let's actually darken the background image. It's a little too bright for my taste. Now, let's create a voiceover for the video. First, let's come up with a draft script. Each slide should say, "Step one." Then the text, like add some diagrams, and then make some kind of comment related to the slide. Let's try to make it a little funnier. That looks great. Now, let's generate the voiceover using Eleven Labs. So, now we can preview those audio files in our assets folder. See what it sounds like. How to explain things to programmers. Spoiler, it's not with words. Okay. And it's already added the audio to our slides. However, we need to update the durations and timings for everything to line up nicely. Run the {slash} transcribe command on each clip to generate word-level timestamps. Next, update the transition durations for each animation so that the different text fades in at the correct time. This command uses the Deepgram API to generate word-level timestamps. Then once you're done, you just click render, and here's the final video in all its glory. How to explain things to programmers. Spoiler, it's not with words. Step one, add some diagrams. Programmers are visual creatures. We can't read documentation, but we'll stare at a flowchart for hours. Step two, show some code. Forget paragraphs, just throw in a code snippet and watch their eyes light up like it's Christmas morning. Step three, sprinkle in some AI, because nothing says, "I'm a serious professional." like generating a video of a glowing robot brain. Thanks for watching. Now, go explain something to a programmer. Good luck. So, that's the workflow. I'm curious, what kind of videos would you make with something like this? If you'd like a deeper tutorial, let me know in the comments. For me, this isn't about AI-generated content. It's about removing friction so you can focus on what you actually want to say.
