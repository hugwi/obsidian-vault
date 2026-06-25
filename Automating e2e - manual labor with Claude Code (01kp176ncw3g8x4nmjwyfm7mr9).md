---
categories:
  - "[[Resources]]"
domain: engineering
title: "Automating e2e / manual labor with Claude Code"
source: "https://www.linkedin.com/pulse/automating-e2e-manual-labor-claude-code-ariel-beck-k1hac/"
author: "Ariel Beck"
published: 
created: 2026-04-12
description: "Demo - init repo command + test command Claude Code is an orchestration engine"
tags:
  - to-process
  - testing-evals
---

![Automating e2e / manual labor with Claude Code](https://media.licdn.com/dms/image/v2/D5612AQEDCMf6K2Sopg/article-cover_image-shrink_720_1280/B56ZuohDyqHUAI-/0/1768058800309?e=2147483647&v=beta&t=JV-IaV_0wsYkD8NuJBfd4ENU-pyXhqLR7f92MZNeaTQ)
###  Ariel Beck


 0:00/1:39 Demo - init repo command + test command 
Claude Code is an orchestration engine with a built-in agentic loop - it doesn't stop until the task is done.


So - I built an E2E testing framework that uses natural language instead of code. No Playwright scripts. No test frameworks. Just Claude Code commands.


Full repo: [https://github.com/arielb135/claude-code-e2e-demo](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Farielb135%2Fclaude-code-e2e-demo&urlhash=Spvm&trk=article-ssr-frontend-pulse_little-text-block)



> Pro tip: Natural language testing shines for complex flows worth the cost. For everything else, hook up Playwright MCP, let Claude Code run through a use case manually, then ask it to output the Playwright script. Same intelligence at authoring time, but faster and cheaper to run in the cost of maintaining script changes when UI changes.


##  𝗛𝗼𝘄 𝗜𝘁 𝗪𝗼𝗿𝗸𝘀


Tests are defined in plain English:



```
{
  "prompt": "add Clam Chowder to cart, go to checkout, fill name 'John Doe'",
  "validation": "Verify the success page shows 'Order Confirmed'"
}        
```

Claude interprets the intent, drives the browser via Playwright MCP, and validates results - either through LLM-as-a-judge reasoning or by navigating to the result URL and verifying the actual page content.


##  𝗧𝗵𝗲 𝗔𝗿𝗰𝗵𝗶𝘁𝗲𝗰𝘁𝘂𝗿𝗲


![Article content](https://media.licdn.com/dms/image/v2/D5612AQG0h3IjnMLGag/article-inline_image-shrink_400_744/B56ZuohbW5HgAY-/0/1768058895007?e=2147483647&v=beta&t=CvFGV-N7QLuzgUD61OnJraqWkisb-y6dkxc-hOOIycE)Code that runs Claude Code CLI in parallel (Optional - just to wrap the actual tests in friendly jsons) + 3 main claude components (2 commands + 1 subagent).
![Article content](https://media.licdn.com/dms/image/v2/D5612AQHYvtdKcw8Vzw/article-inline_image-shrink_400_744/B56ZuoercFIsAY-/0/1768058175637?e=2147483647&v=beta&t=QGTUZLLMKHlWEhf1FI863p8pVl3BbvFGty3PDKY8lfs)Main commands for the agent
All components run on Haiku for cost efficiency.


##  S𝗼𝗹𝘃𝗶𝗻𝗴 𝘁𝗵𝗲 𝗣𝗮𝗿𝗮𝗹𝗹𝗲𝗹𝗶𝘀𝗺 𝗣𝗿𝗼𝗯𝗹𝗲𝗺


Playwright MCP assumes one browser per session. Running tests in parallel caused conflicts.


Solution: Each worker gets an isolated browser profile. 



```
/tmp/playwright-e2e-worker-0
/tmp/playwright-e2e-worker-1        
```

A Python runner spawns parallel Claude CLI processes, each with its own MCP config pointing to a unique profile.


##  𝗦𝘁𝗼𝗽 𝗪𝗿𝗶𝘁𝗶𝗻𝗴 𝗥𝗘𝗔𝗗𝗠𝗘 𝗙𝗶𝗹𝗲𝘀


![Article content](https://media.licdn.com/dms/image/v2/D5612AQF-tr9fiUvfbw/article-inline_image-shrink_1500_2232/B56Zuoix_bIwAU-/0/1768059251984?e=2147483647&v=beta&t=fujxID51psC8S-DTgJv4sIipqqMh6695qjuZn8VQ8Fk)
Instead of a README with setup instructions that go stale, I created /init-cart - a Claude command that executes the setup:


1. Checks prerequisites (Node.js, npm, Claude CLI, Python)
2. Verifies secrets file exists (prompts you to create it if missing)
3. Installs dependencies
4. Starts the app in background
5. Validates everything is running
6. Offers to run a test


README tells you what to do 😔. Claude commands do it for you 🙂.


The command lives in .claude/commands/init-cart.md - just markdown with instructions that Claude follows. New contributor? Run /init-cart. Environment broke? Run /init-cart. No copy-pasting terminal commands from outdated docs.


##  Tip - Automate Any Manual Labor


This pattern extends beyond testing. Any repetitive manual task can become a Claude command + MCP.


* /init-repo - Clone repo, install dependencies, set up pre-commit hooks, configure IDE settings
* /migrate-db - Run migrations, validate schema, seed test data, verify constraints
* /onboard-dev - Create accounts, set up SSH keys, configure AWS credentials, join Slack channels
* /debug-prod - Pull logs, check metrics, compare against baseline, suggest fixes


Write the instructions once in markdown. Pair with the right MCP (Playwright, Postgres, AWS, Slack). Let Claude execute them forever.


##  So - Why even considering this over traditional testing?


### 𝗔𝗱𝘃𝗮𝗻𝘁𝗮𝗴𝗲𝘀


 ✅ Readable tests - Anyone can write and understand them


 ✅ Flexible validation - LLM judges intent, not exact selectors


 ✅ Rapid iteration - Change test behavior without touching code


 ✅ Self-healing - Claude adapts to minor UI changes


### 𝗗𝗶𝘀𝗮𝗱𝘃𝗮𝗻𝘁𝗮𝗴𝗲𝘀


 ❌ Slower - LLM latency adds up per test


 ❌ More expensive - Even with Haiku, LLM calls add up


 ❌ Non-deterministic - Same test can take different paths.


##  𝗪𝗵𝗲𝗻 𝘁𝗼 𝗨𝘀𝗲 𝗧𝗵𝗶𝘀


Use natural language testing for:


* Complex E2E flows worth the cost (checkout, onboarding)
* Exploratory testing of new features
* Tests that break frequently due to UI changes


Use traditional Playwright for:


* High-volume regression suites
* Performance-critical test runs
* Deterministic, repeatable assertions


 The sweet spot: Let Claude write your Playwright tests, then run those for CI. Use natural language testing for the flows that matter most.


 6 tests. 0 lines of the actual test code. All passing.


Full repo: [https://github.com/arielb135/claude-code-e2e-demo](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Fgithub%2Ecom%2Farielb135%2Fclaude-code-e2e-demo&urlhash=Spvm&trk=article-ssr-frontend-pulse_little-text-block)