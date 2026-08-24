---
title: "I Let Aider AI Refactor My App"
source: "youtube"
url: "https://www.youtube.com/watch?v=cTSvN0YLMgw"
author: "Better Stack"
published: "2026-02-19"
created: "2026-08-24"
duration: "0:04:44"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "engineering"
  - "local-llm"
  - "openai"
  - "video-gen"
summary: "This is Aider, an open-source AI pair programmer that lives in your terminal. And unlike Copilot, it's not autocomplete. It edits your repo directly using a structured file map built with a tree-sitter."
---

# I Let Aider AI Refactor My App

![I Let Aider AI Refactor My App](https://www.youtube.com/embed/cTSvN0YLMgw)

## Description

Most AI coding tools autocomplete. Aider edits your repo. 

In this video, I test Aider AI on a real project to see if it can add secure authentication with tests, handle multi-file refactors, pass builds without breaking everything, and commit clean Git history.  If you’re a dev working with Python, Flask, React, or TypeScript and wondering whether terminal AI tools actually save time, this is the test.

🔗 Relevant Links
Aider Repo - https://github.com/Aider-AI/aider 
Aider Docs - https://aider.chat/docs/ 
Aider - https://aider.chat/

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
00:00 Aider AI the Open Source AI Pair Programmer
00:30 What Is Aider AI? Terminal-Based Repo Editing Explained
01:03 Aider AI Live Demo – Build Flask Auth with Tests
02:13 Aider AI Speed  
02:42 Multi-File Refactor Demo (React + TypeScript with Aider)
03:28 Aider vs Cursor vs Copilot – Honest Developer Comparison
04:19 How to Use Aider Properly (Architect Mode + Git Workflow Tips)

## Transcript

This is Aider, an open-source AI pair programmer that lives in your terminal. And unlike Copilot, it's not autocomplete. It edits your repo directly using a structured file map built with a tree-sitter. It supports over 100 languages, and it works with models like Claude, DeepSeek, and OpenAI. We're going to see how this stacks up to Claude Code, for instance, and if it's even worth it. We have videos coming out all the time. Be sure to subscribe. All right. So, Aider works in the terminal. You can think of it kind of like autocomplete guesses the next line. Aider takes a repo-wide change request and turns it into real edits and commit. It's Git native. Every change is a commit, and you can undo it instantly. Aider itself reports 88% success solving 225 polygot coding tasks. That's a lot. It's not perfect, but the wild part is 88% of that code was written by Aider itself. I'm going to do this clean so you guys can hopefully replicate it. It's just a CLI. No IDE required, but I will do this in VS Code so you can see how all the code is processed. I just ran a curl command on here to get Aider installed. Then I went and I got my DeepSeek API key, and I ran the second command. If it is your first time, Aider will go through some setup steps for you. Super easy. It's yes or no. Then you're good to go with this chat window right here in the editor. Now, here's the app. I just added a basic setup for Flask with no authentication yet. I'm going to ask Aider to create a secure user off using Flask-Login and bcrypt, and add in some unit tests. Watch this right here. It builds a dynamic repo map. That's why it can edit across the whole code base instead of guessing in one [clears throat] file. It edits multiple files, add requirements, creates a test file, added secure authentication with tests. That's the real thing that this is doing. If it can't get up to a passing test in a clean commit, it's not really going to save you time. That was just about 45 seconds, maybe a bit more here, right? But everything was built, commence testing, all of it. Most autocomplete tools don't understand cross-file dependencies, so refactors are going to break silently. Aider was built for whole repo edits. It's handled projects over 20,000 lines of code. Devs report two to five times speed improvements with models like DeepSeek. Edits can also cost about a cent. This is about time, but also about money. If a tool makes you feel fast, but actually breaks things along the way, it's actually just slowing you down. There's been reports from devs cutting refactors from about an hour down to 10 minutes. That's what they say, right? There's no real evidence here. This isn't vibe coding, this is controlled, reviewable, Git safe development. So, what happens during a messy refactor? I'm going to push this a little harder. Here's a React and TypeScript to-do app. I want to add a dark mode and API sync. That's a multi-file refactor. First, I'm going to use architect mode, and I plan the change. It thinks there are no edits. I'm going to switch to code mode, implement the plan, and watch what happens. It edits the theme config, components, and the API client. Now, I'll ask it to generate tests for the new sync logic. Let's build it. If the build fails, that's where most tools leave you stuck. Aider's going to have that sometimes, but here, it can instantly undo clean Git repo changes, no damage, fix the prompt, run it again. My build passes. Now, we have a feature branch ready for PR. But, let's be honest, this is just another terminal tool, right? If we stack it up with Cursor, Cursor's great, right? It's strong, UI is good. But, for heavy multi-file refactors in a terminal workflow, Aider has the edge. Copilot is fast for inline autocomplete, but it struggled with repo-wide reasoning. Then, there's Claude Code, right? Great reasoning, strong reasoning, but sometimes, with Git workflow, it isn't always as tight. Aider's strength is structured repo editing plus Git. But, I mean, if we are looking at other tools that are already out there, I mean, this is okay. Sure, others are going to be much stronger and better for your use cases, maybe. But, I do like how I can swap them all around, and when I do, I can add DeepSeek. The calls are a lot cheaper, the responses are still quite strong. It's DeepSeek. I could have used Ollama here to make things completely free, but if you've used Ollama, then you know, I mean, it's good, but it's not great. do want to try this out, here's how you could probably try it properly. First, try the architect mode before any major refactors. Configure your YAML config file with your model or your preferences, and always review the diffs that it's going to be spitting out to us. Then, if you want, hook it into VS Code or any editor that you want. I put it in the terminal, but it was in the terminal in VS Code. We'll see you in another video.
