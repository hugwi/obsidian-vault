---
title: "The Rise of Generative UI for Developers (CopilotKit)"
source: "youtube"
url: "https://www.youtube.com/watch?v=kVL_7csy_ZM"
author: "Better Stack"
published: "2026-06-12"
created: "2026-08-24"
duration: "0:07:33"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "business"
  - "context-engineering"
  - "local-llm"
  - "video-gen"
summary: "Most AI features and apps have the same problem. They look good, but really they're just a chat box slapped to the side of the screen. You ask for something, it gives you markdown, maybe a table, maybe even a few paragraphs explaining the work you still have to do."
---

# The Rise of Generative UI for Developers (CopilotKit)

![The Rise of Generative UI for Developers (CopilotKit)](https://www.youtube.com/embed/kVL_7csy_ZM)

## Description

In this video, I take an dev-focused look at CopilotKit, generative UI, AG-UI, and the growing shift from basic AI chatbots to agent-native apps. 

I’ll look at why most AI features in SaaS apps still feel like a bolted-on chat window, how CopilotKit helps agents render real UI components, share state with your React or Next.js app, and support human-in-the-loop approval flows, and where it fits compared to tools like Vercel AI SDK, assistant-ui, and building everything yourself.

🔗 Relevant Links
CopilotKit Repo - https://github.com/copilotkit/copilotkit
CopilotKit - https://www.copilotkit.ai/

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
0:00 Why AI Chatbots Feel Broken in Apps
0:36 The Real Problem with AI Chatbots in SaaS
1:37 CopilotKit Demo: From Chatbot to Agentic UI
3:23 What CopilotKit Actually Does for Developers
3:28 AG-UI Explained: Connecting AI Agents to Frontends
4:09 Generative UI: AI That Renders Real Components
4:23 Shared State with CoAgents
4:44 Human-in-the-Loop AI Workflows
5:10 CopilotKit vs Vercel AI SDK vs Building Your Own
5:33 CopilotKit Tradeoffs, Bugs, and Limitations
6:25 Best Use Cases for CopilotKit and Agentic UI
7:00 Final Verdict: Is CopilotKit Worth It?

## Transcript

Most AI features and apps have the same problem. They look good, but really they're just a chat box slapped to the side of the screen. You ask for something, it gives you markdown, maybe a table, maybe even a few paragraphs explaining the work you still have to do. But what if the agent didn't just talk? This is Copilot Kit. It can render real components, share live state with your app, and stop to ask for approval before it changed anything. So, can this make an AI feature feel more like part of the product? Let's find out. Now, first off, a lot of people think they're adding AI to the app, but what they're really adding is a second app inside their app. Your product is over there, the AI is over there, and the user has to copy context back and forth in their head to really get anything working. Now, that's fine if all you really need is this basic Q&A structure, but the second you want the agent to update state, call tools, or work with the user inside a real workflow, we start to hit a wall. Now, you're building streaming events, state sync, approval flows, and everyone is rebuilding the same thing just slightly different. Copilot is going after this problem up front. Not, "How do we make another chatbot?" The better question is, "How do we make agents feel native inside the apps themselves?" So, let's start with the demo, then I'll break down what's real, what's useful, and what's just a little bit too much. If you enjoy coding tools to speed up your workflow, be sure to subscribe. We have videos coming out all the time. All right, now, watch this. I'm starting from a clean terminal, and we can just run our install I got from the Copilot Kit repo. This scaffolds the app and gives me a working starting point just like any other project that we really start up. Not just an empty chat bubble, but real pieces. The front-end pieces are already wired together enough that I can start testing the actual experience that we want. Now, I jump in and I run the development mode, and here's the app running locally. Now, of course, this part looks familiar. There's a chat surface, but that's not really the whole interesting part here. The really cool part is what happens when the agent is connected to the UI. I'm going to ask a question here in the interface. Okay, there we go. And notice the big thing here. The agent doesn't just answer with some blob of text. It can stream the response. It could call tools, and it could render an actual component inside the app. That's the first really big change here with Copilot Kit. The AI is not just describing the interface. It's now a piece of all of it. Now, let's push it a step further. I'm going to ask it a follow-up question here. Okay, and here's the part a lot of other agents are going to skip. Now, our agent pauses. It asks for approval. And it asking for approval is the part that matters. That's the part that I really like because in real software, control is not really optional. Our users still need the final say in really what's happening. Now, cool demo, right? Now, the easy way to explain Copilot Kit is really just this. Copilot Kit is a front-end stack for agentic apps. It's not just a chat component. It's not just a wrapper around another LLM API. It gives you the pieces we need for AI experiences that live inside of the product. There are four pieces to really understand here. First is AGUI. Now, AGUI is an open event-based protocol for how agents talk to front-ends. Right now, agent tooling has connection problems. You have LangGraph, Crew AI, Maestral, custom agents, and whatever new framework launched this morning. We're trying to drop that in our app. Then you have React apps, mobile apps, dashboards, all this other stuff that's happening. That's It's lot of different things to juggle. All of these things are being juggled without a shared protocol. Every back-end needs custom code for every front-end. AGUI is trying to become the shared language between the agent and the interface. Messages, state updates, tool calls, UI events, all moving through a common event stream. Then we have generative UI. Instead of the model only returning text, the agent can trigger real components. It's not random HTML, it's just your UI rendered at the right moment. Then is shared state, or what Copilot Kit calls co-agents. The front-end and the agent back-end can share state in both directions. When the user changes something, the agent can react. When the agent updates something, the UI can reflect it. This is huge when we're building out tools, dashboards, anything where the user and the agent are working on the same object. Then finally is the whole human in the loop thing. This is one of the most important parts with all of this. A lot of agents, a lot of agent demos, can act like the best experience is full autonomy. But really, that's not always the case, right? In real products, users want power and control. Confirm before sending, approve before creating, choose between options, all of this stuff. And Copilot gives us things for just that. Now, Copilot is not the right choice for everyone, right? If you compare it to something like Vercel AI SDK, Copilot Kit is more batteries included. If you want streaming chat, generative UI, shared state, and human approved patterns right out of the box, this is what Copilot Kit is getting closer to, a the full product layer. Vercel AI SDK is lighter. It gives you more low-level control. So, if you want to own every part of the architecture, then sure, that's honestly a much better fit. Now, if you compare Copilot Kit to building everything yourself, this is where it gets pretty hard to beat, because the hard part is not rendering out some chat bubble. That's now becoming the easy part, right? The hard part is everything surrounding that. But, of course, with any of this, there is a trade-off. It can feel heavier than a minimal AI SDK, of course. You are adopting Copilot Kit's patterns. Also, it's free to an extent. Honestly, if you're playing around in solo, okay, it's super cool, but it becomes annoying when you want to use this for scale, cuz then all of that is not free. Also, if you guys do know a complete open-source alternative to this, drop a comment and let me know, cuz I'm searching for just that. With Copilot Kit, you do need to understand what is open-source. You need to understand what needs keys, what's hosted, what's paid. This is not just a dunk on Copilot saying it's all bad, but you do need to understand what's free and what's not. If you only need a basic support chatbot, Copilot Kit is probably an overkill. But, if you want something that works really well for agentic UX, where the agents work with your UI and your app state, this is really cool. So, should you use Copilot Kit? Well, give it a shot if you're building some serious in-app AI, especially if you're in React or Next.js, and you want the AI to feel like a part of the product, not just a side panel. This is really cool. You can spin it up really fast, and with all the components we have, it makes it really practical to drop in the workflow. If you already built your own streaming state tool call UI, switching might not be worth it. And if your feature is a literally just ask a question, get an answer, Copilot Kit is going to be a big overkill for that. You probably don't need a full agentic front end stack. Just use something lighter, okay? Ship it, move on, get going. If you enjoy coding tools like this, be sure to subscribe to the Better Stack channel. We'll see you in another video.
