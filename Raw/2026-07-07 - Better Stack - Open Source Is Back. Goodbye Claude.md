---
title: "Open Source Is Back. Goodbye Claude."
source: "youtube"
url: "https://www.youtube.com/watch?v=wOfm7x0i3sw"
author: "Better Stack"
published: "2026-07-07"
created: "2026-08-24"
duration: "0:07:06"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "anthropic"
  - "context-engineering"
  - "evaluation"
  - "google"
  - "harness-engineering"
  - "local-llm"
  - "openai"
  - "security"
summary: "Open code is an open source coding agent that just crossed 180,000 stars on GitHub and it's a direct replacement for tools like Claude code without the glitchy UI and expensive subscriptions. You'll get access to hundreds of models including free and local models, which is pretty cool. Today, we're going to pull apart open code and we're going to compare it to some of the paid alternatives and test whether free and open source really holds up when you're trying to push to production."
---

# Open Source Is Back. Goodbye Claude.

![Open Source Is Back. Goodbye Claude.](https://www.youtube.com/embed/wOfm7x0i3sw)

## Description

If you're looking for a free, open-source alternative to Claude Code and Cursor, OpenCode is worth a look. It's a terminal-based AI coding agent that lets you bring your own model. Running anything from Anthropic, Google, and OpenAI to cheaper options like GLM 5.2 and Deepseek 4, or even local models. Here's how it holds up as a daily coding tool in 2026, and whether open source can really compete with the paid incumbents.

🔗 Relevant Links
https://opencode.ai

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

## Transcript

Open code is an open source coding agent that just crossed 180,000 stars on GitHub and it's a direct replacement for tools like Claude code without the glitchy UI and expensive subscriptions. You'll get access to hundreds of models including free and local models, which is pretty cool. So, you're not vendor locked into one platform. Today, we're going to pull apart open code and we're going to compare it to some of the paid alternatives and test whether free and open source really holds up when you're trying to push to production. And we cover a huge amount of dev content on this channel. So, if you want to stay up-to-date, then subscribe. >> [music] >> Open code is a coding agent that lives in your terminal and it comes with a huge array of tools like bash, edit, grep, web fetch, and web search. These are all the things that made Claude code so useful. So, seeing them in a free and open source tool is really nice. Once installed, we can run the open code command to enter our terminal. Here, I'm using Ghosty, which is one of open code's recommended terminals. You can see immediately the terminal UI here is really clean, but the big difference is bringing your own models. By default, I'm using a free model called Big Pickle. But, using the {slash} models command, I can easily switch to other free alternatives or paid models from companies like Google, Anthropic, and OpenAI. Hitting control I, I can also see a huge list of models which come from models.dev, a directory officially supported by open code. Here, you'll have access to models like GLM 5.2 and Deep Seek 4. Even with paid models, this can be considerably cheaper than sticking to API only pricing with labs like Anthropic because models like GLM 5.2 are much, much cheaper with comparable results to models like Fable 5. GLM 5.2 even beat Fable 5 at web design according to design arena. At the time of recording, there is no auto mode for open code to select a suitable model based on its assigned task. Features you'd see in harnesses like Copilot, but what you can do instead is configure custom sub agents to use a specific model. Then call on those for specific tasks. And this is a great way to segue into configuring Open Code's agents. In Open Code, agents come in two types, primary and sub agents. Primary are the top-level agents you'd always use. You get build and plan exactly as you would expect from harnesses like Copilot or Claude Code. You can use tab to change this or just use the slash agents command. So, plan is exactly as you would expect for planning large features without actually making those changes, and then you could switch to the build agent to actually implement that plan. Or if you just want to make changes directly, stick into the build agent. Sub agents on the other hand are for specialist tasks, and they'll be invoked automatically depending on your prompt. But you can tag them manually by using the at character. By default, you'll have access to the general agent for researching complex questions and executing multi-step tasks. And then we have the explore agent, which has read-only access for exploring large code bases. Now, the really interesting and powerful part of Open Code is that you can configure your own custom agents. So, there are a few ways that you can set up custom agents with Open Code. You can use the JSON file which I just explained earlier. And if you want all your config in one place, this is the right way to do it. So, I'll just enlarge this. We can see that under the agents config, we've got a build agent, we've got the plan agent. So, these are the ones that come as default, but you can change these if you like. And then we've got a custom agent here called code review, and this just happens to be using Claude Sonic 4. And then we got a little description of what it does, and then a prompt that would automatically be injected into the agent when you ask to perform a specific task. If you don't want all of your config in one place, instead you can have a dot open code folder with an agents folder, and inside that you can describe the specific agent that you want as a markdown. So, here we have the UI engineer.md. And the description is it handles UI component implementation, styling, and front-end engineering tasks. The mode for this would be a sub-agent. We're using GLM 5.2 just because that is very, very good at doing design based on the design benchmarks. You can also change the temperature as well to modify the sort of randomness of the output that you would get from the model. And then you can also modify any of the default permissions. So, in this case, we always want to allow edits and always allow bash commands. Within the markdown file, you then can give further instructions on exactly what this agent does. So, here we say, "You're a UI engineer specializing in front-end development. You excel at" and then you can give as much detail as you like to guide your agent in the correct direction. So, next time that you trigger a prompt that requires design work, it's going to do exactly what you want. So, here as another example, we have review.md, and this will just do code review for us. In this case, we set the temperature as a really low number because we want more of a deterministic output from the model. We provide the same sort of permissions. This time, we're using Claude Sonic 4, and then we give a little description of what it does: review code for quality and best practices. Again, the mode is going to be sub-agent. And then again, a short or long description to explain exactly what the model does. And the more detail you give here, the less likely it is to do the wrong thing or hallucinate. Now, when I'm working on a UI task, I can tag my agent and let GLM handle all of the design work. Now, here are a few things to improve quality of life when using open code. Flip on AliceP in your config, and it will auto-start the correct language server per file. So, the model gets real-time information and errors, not just raw text. And this is off by default, so you do need to flip it on. Using the at character also gives you fuzzy file search to pull in files into context. You can use undo or redo to reverse the agent's changes, and they do stack. Share can give you a link to the whole session for debugging or handing to a teammate. You can also use inits, which writes an agents.md, a checked-in file that teaches the agents your project's conventions. And this is just exactly like the Claude MD file in Claude code. So, my verdict here is that the UI is considerably better than Claude code. Plus, it has access to all of the same tools with the added benefit that you can use your own models and configure custom tools and agents. On cost, it's actually not black and white. If you're on API-only pricing, then Open Code wins easily because you have access to so many more much cheaper models. But, if you're on a subscription with Anthropic's Pro or Max plan, for example, you cannot use third-party harnesses like Open Code because Anthropic specifically block access to them. But, if you are on that subscription, then Claude Code bundles in a huge discounts compared to raw API rates. So, if you're on API-only pricing, then stick to Open Code. But, if you do have that subscription, then Claude Code is the winner on pure cost. If you enjoy hearing about the latest AI tooling, then we've done a breakdown of GLM 5.2 you can watch here. Otherwise, I've been Warren from Better Stack. Thanks for watching, and I'll see you in the next one.
