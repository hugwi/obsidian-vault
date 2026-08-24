---
title: "Do This Before AI Writes Any Code #aicoding #claude #vibecoding"
source: "youtube"
url: "https://www.youtube.com/watch?v=MV-Mw5npOJk"
author: "Better Stack"
published: "2026-06-05"
created: "2026-08-24"
duration: "0:01:47"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
summary: "Everyone is vibe coding with AI right now, but here's the part nobody talks about. It feels great for the first 10 minutes, we know that, and eventually your code base turns into nothing. You describe the feature, the AI starts writing code, it looks good, it even feels like you're moving fast, but then state starts leaking off, flows break, and somehow the AI has created 17 versions of the same object."
---

# Do This Before AI Writes Any Code #aicoding #claude #vibecoding

![Do This Before AI Writes Any Code #aicoding #claude #vibecoding](https://www.youtube.com/embed/MV-Mw5npOJk)

## Description

*No description.*

## Transcript

Everyone is vibe coding with AI right now, but here's the part nobody talks about. It feels great for the first 10 minutes, we know that, and eventually your code base turns into nothing. It turns into a mess. You describe the feature, the AI starts writing code, it looks good, it even feels like you're moving fast, but then state starts leaking off, flows break, and somehow the AI has created 17 versions of the same object. And now you're not shipping any faster, you're just debugging faster. The problem is not the AI is bad at coding, problem is that it has no map. It doesn't understand how data is supposed to move through your app, so a lot of times it guesses. And those guesses become technical debt, wasting our time and minutes, because now we're debugging. The fix is simple. Before you ask AI to write the code, map the data flow first. Not some giant architecture doc, just a quick 60-second outline. What are the main entities? Where does the data come from? Where is the data going to? And what changes, for instance, in this? User creates an order, order triggers payment, payment updates the database, then notification sends the receipt. Those are just a structured order. Then paste that map into the prompt and say something like, "Here's the exact data flow, generate code that strictly follows it. Don't try to introduce new entities, state, or flows unless I ask." That one line gives the AI rails, so it follows your architecture instead of in just inventing its own. And this is the real change from vibe coding to now smart agented coding. Structure should come first, speed is second, because real speed is not generating 500 lines in 10 seconds, real speed is not spending the next 3 hours deleting them. If you enjoy coding tips and tricks like this, be sure to subscribe to the Better Stack channel.
