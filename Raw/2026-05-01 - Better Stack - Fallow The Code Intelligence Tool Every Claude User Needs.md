---
title: "Fallow: The Code Intelligence Tool Every Claude User Needs"
source: "youtube"
url: "https://www.youtube.com/watch?v=-lCfwIoDXq8"
author: "Better Stack"
published: "2026-05-01"
created: "2026-08-24"
duration: "0:06:02"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "context-engineering"
  - "engineering"
  - "local-llm"
  - "mcp"
  - "skills"
  - "video-gen"
summary: "This is Follow, a code-based intelligence tool for TypeScript and JavaScript that analyzes your entire code base for dead code, duplication, unnecessary complexity, and much more, meaning there's no need to use a combination of nip, JSCPD, and ESLint just to stop your agents from shipping bad code. It's built in Rust and supports over 90 plugins, meaning it will work out of the box with most frameworks and popular packages. But, the fact that it only supports JavaScript and TypeScript make it less appealing for AI-assisted coders."
---

# Fallow: The Code Intelligence Tool Every Claude User Needs

![Fallow: The Code Intelligence Tool Every Claude User Needs](https://www.youtube.com/embed/-lCfwIoDXq8)

## Description

AI coding agents are great at shipping features fast, but they also ship a lot of slop: dead code, duplicated logic and tangled dependencies you only discover weeks later. Fallow (fallow-rs) is a Rust-built code intelligence tool for JavaScript and TypeScript that combines dead code detection, duplication finding, complexity analysis and architectural boundary enforcement into one zero-config command, replacing the usual jumble of knip, jscpd, and eslint. It auto-detects your framework from 90+ plugins, gives you line-level results that AI agents can fix in seconds. In this video, I run Fallow on a real Claude-built project, set it up as an agent skill for hands-off cleanup, and show how it works with GitHub Actions, pre-commit hooks, and PR audits.

🔗 Relevant Links
Cinematic tool - https://github.com/Orva-Studio/hance
Fallow - https://fallow.tools/
Fallow docs - https://docs.fallow.tools/

❤️ More about us
Radically better observability stack: https://betterstack.com/
Written tutorials: https://betterstack.com/community/
Example projects: https://github.com/BetterStackHQ

📱 Socials
Twitter: https://twitter.com/betterstackhq
Instagram: https://www.instagram.com/betterstackhq/
TikTok: https://www.tiktok.com/@betterstack
LinkedIn: https://www.linkedin.com/company/betterstack

## Transcript

This is Follow, a code-based intelligence tool for TypeScript and JavaScript that analyzes your entire code base for dead code, duplication, unnecessary complexity, and much more, meaning there's no need to use a combination of nip, JSCPD, and ESLint just to stop your agents from shipping bad code. It's built in Rust and supports over 90 plugins, meaning it will work out of the box with most frameworks and popular packages. But, the fact that it only supports JavaScript and TypeScript make it less appealing for AI-assisted coders. Hit subscribe, and let's find out. So, here is a project that I'm working on that adds a cinematic film look to videos and images. It's mostly been built with Claude Code, so it will have some level of AI slot. There's also a PR here for a new feature in that project, which I'll talk about later, as long as GitHub doesn't make it disappear by accident. So, to get started, I'm going to run Follow with the summary flag using bun x, which means I don't have to install it. And this gives a snapshot of my project showing the dead code summary, duplication, and a complexity health summary. And if we check the Git status, it adds a new .follow directory that contains the cache, so that means subsequent runs of this command will be faster and contains snapshot and any plugin information. Now, you may have noticed it here that the health is 41 above the threshold. Now, what does that mean? Well, the Follow health score is calculated by working out the cyclomatic complexity and the cognitive complexity. And it uses some formulas to calculate the complexity density, and down here, all this is used to figure out the maintainability index, which is the score that we see over here. So, based on this score, it's detected that 41 of my files need to be refactored. From here, we can run any of these commands to get a more detailed report about a specific area. So, if I wanted to focus on health, we could run this command, and after a while, it lists all the files that have different health issues. Note, if you want to know what CRAP stands for, this is an abbreviation for change risk antipatterns, which you can learn all about in the documentation. But, this level of detail is very easy for an agent to follow and know what to fix. In fact, the duplication is a lot easier to follow since it gives the exact file and the specific line numbers. So, we'll stick with that for now. And if we wanted to, we could add a Follow configuration file to give Follow information about certain patterns or dependencies you want to ignore, as well as setting some custom duplication settings, health setting, and adding boundaries, which is a very cool way of declaring which directories can import from which other ones. But, all of this is too complex for my needs, so for now, we'll stick with the defaults. Now, from here, we could run the Follow fix command, or we could add the dry run flag to see exactly what it's going to do, which is try to address all the fixable issue types. And you can see here that it's going to remove a bunch of exports. But, I actually don't trust Follow to run an automatic fix because it doesn't have much context of my code, what each function does, and how everything works together. So, instead of using the fix flag, I'm going to hook Follow up to my agents, which you can do using the MCP server, or by using the VS Code plugin, which I guess will work with Cursor. But, I'm going to keep things simple and just install the Follow skill, which contains some guardrails, some agent rules, and some common pitfalls. So, with the skill installed, I'm going to run Claude Code, and I'm going to give it a prompt of study this project to understand how the code works. Then, run Follow to deal with the duplicated code, making sure removing it doesn't break core functionality. And when you're done, put the changes in a feature branch and run tests to make sure the app works as expected. So, we can see here, it loads the Follow skill, then it runs the Follow dups command, and it gets the format to export JSON, which is a machine-friendly format. And after about 4 minutes, Claude has finished fixing three files instead of all the files Follow suggested, mainly because the others are test files, which are sometimes supposed to have duplicated code. I also asked it to create a PR, and if we have a look at it, it's added 54 lines of code and removed 43. But, this is because I've asked it to add a Follow configuration file, which is about 20 lines, to ignore all test files in future reports. And of course, we could continue going down this line using Claude Code or any other agent to fix complexity issues or any dead code. But, Follow can also review PRs. So, if we take a look at this PR I showed you earlier, running the Follow audit command will check any issues on this branch versus main, so that we can only fix specific issues. And if we wanted to base it off a different branch, we could just use the base flag. But, if we also didn't want to prompt Claude over and over again each time to use Follow, we could run the setup hooks command, which will generate some Claude Code hooks for Follow. Follow can also run as a GitHub action with PR annotations. It supports workspaces. It can export health badges and supports baselines, meaning the current issues can be fixed over time, and the CI only picks up new issues, which is great for fixing a big project with lots of issues. It basically has a lot of features, but all of them are pretty much static code analysis, which means it doesn't actually execute your functions. If you wanted to something that did that, then Follow supports something called runtime intelligence to tell you what functions are being triggered when your app in production encounters real traffic. It does this by using V8 runtime coverage and merges the results to an existing health report through a sidecar that can run locally or can be deployed anywhere you want. But, this of course is a paid feature, which kind of makes sense. Overall, Follow is a great tool that I'm going to be using a lot more of, even though I think it has a lot of features, and it only supports the JavaScript tech stack. Although other languages do have their own tools, I'm not sure it combines everything together as well as Follow does, and I think its creator, Bart, has done a good job of creating this tool, which actually uses Olexy for parsing, semantic analysis, and module resolution before the graph-based analysis begins. So, basically, it's never going to leave JavaScript, and I'm sure this makes Evan You very happy, not the JavaScript bit, but the Olexy bit, since it's a tool that he's funding with Void Zero. Speaking of Evan You, if you want to hear us grill him about Void Zero, the plus if React server components was a good idea, and everything in between, then check out this video, which is an hour-long podcast, and I think it's one of my favorite assets that we've done.
