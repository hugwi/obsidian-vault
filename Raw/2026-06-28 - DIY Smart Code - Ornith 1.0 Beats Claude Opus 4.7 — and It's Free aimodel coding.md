---
title: "Ornith 1.0 Beats Claude Opus 4.7 — and It's Free #aimodel #coding"
source: "youtube"
url: "https://www.youtube.com/watch?v=8Cw1jX6o9w0"
author: "DIY Smart Code"
published: "2026-06-28"
created: "2026-08-24"
duration: "0:02:13"
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
  - "evaluation"
  - "harness-engineering"
  - "local-llm"
summary: "An open source model just matched Claude Opus on coding. And you can download it tonight. And the team says it taught itself how to code."
---

# Ornith 1.0 Beats Claude Opus 4.7 — and It's Free #aimodel #coding

![Ornith 1.0 Beats Claude Opus 4.7 — and It's Free #aimodel #coding](https://www.youtube.com/embed/8Cw1jX6o9w0)

## Description

Ornith-1.0: the open-source coding LLM that matches Claude Opus 4.7 — and runs on your laptop. This open-weights agentic-coding model hits 77.5 on Terminal-Bench and 82.4 on SWE-bench Verified, beating Claude Opus on both, then ships a 9B size you can `ollama run` locally. MIT licensed, four sizes, and it taught itself the harness.

----
🚀 DYNAMOUS AI COMMUNITY

Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount

⚡ HOSTINGER — RELIABLE HOSTING FOR YOUR PROJECTS (10% OFF)

Whether you're shipping a portfolio, a side project, n8n flows, or AI agents — I use Hostinger for fast, affordable VPS + web hosting.

Get 10% off here 👉 https://hostinger.com/DIYSMARTCODE

(Affiliate link — costs you nothing, supports the channel.)
----

What you'll see in this 2-minute breakdown:
→ Ornith-1.0 — an open-source family of agentic-coding models from DeepReinforce
→ `ollama run ornith` — the 9B size is 5.6 GB, no API key, weights on your machine
→ Benchmarks vs Claude Opus 4.7: 77.5 vs 70.3 on Terminal-Bench, 82.4 vs 80.8 on SWE-bench Verified
→ Not cherry-picked: 78.9 multilingual SWE-bench, 77.1 ClawEval, clears Minimax & DeepSeek
→ Four sizes: 9B Dense, 31B Dense, 35B MoE, 397B MoE — one self-improving recipe
→ Self-scaffolding RL: the model writes its own harness, then the reward trains both
→ Reward-hacking defense: frozen environment + deterministic monitor + frozen LLM judge
→ The honest part: the 397B flagship needs datacenter hardware — the 9B runs on your laptop
→ MIT licensed, top to bottom: commercial use and fine-tuning, no strings

The receipts:
→ Tech blog: https://deep-reinforce.com/ornith_1_0.html
→ Run it: https://ollama.com/library/ornith
→ Weights: https://huggingface.co/collections/deepreinforce-ai/ornith-10
→ Announcement: https://x.com/ornith_

Open weights now trade blows with Claude on coding. So — would you switch your daily driver to an open model you run yourself, or stay closed? Drop your pick in the comments.

#ornith #ornith1 #deepreinforce #opensourceai #agenticcoding #localllm #ollama #claudeopus #openweights #swebench #terminalbench #aimodel #codingai #llm2026 #mixtureofexperts #selfhostedai #aicoding #mitlicense #opensourcellm #diysmartcode

## Transcript

An open source model just matched Claude Opus on coding. And you can download it tonight. It's called Open Earth. And the team says it taught itself how to code. One command pulls it. Ollama run Open Earth. The 9 billion size is 5 GB. Small enough for a laptop. No API key. No rate limit. The weights are yours. Here's the part that turned heads. The flagship Open Earth scores 77.5 on Terminal Bench and 82.4 on SweetBench verified. Claude Opus 4.7 70.3 and 80.8. An open model sitting ahead on both. And it's not just two cherry-picked benchmarks. 78.9 on multilingual SweetBench. 77 on Claude Eval. It clears the leading open models its size like MiniMax and DeepSeek across the board. It ships in four sizes. 9 billion, 31 billion, a 35 billion mixture of experts, and a 397 billion flagship. Same training recipe top to bottom. So, how does an open model catch Claude? Most training uses a human-written harness to steer the model. Open Earth throws that out. Each step, it writes its own scaffold, then solves the task, and the reward trains both. The orchestration that finds the answer, the model learns that, too. Now, letting a model write its own scaffold is dangerous. It can cheat. Read the test file, hardcode the answer, fake the pass. So, the team locks the environment, runs a monitor that zeros out any trajectory that peeks where it shouldn't, and adds a frozen judge on top. Self-improvement without the reward hacking. Now, the honest part. That 397 billion model runs on data center hardware, not your machine. But, the 9 billion size, it scores 69.4 on SweetBench verified and matches Gemma 4 at 31 billion. That one runs on your laptop. The big model proves the method. The small one ships to you, and every size is MIT licensed. Commercial use, fine-tuning, all of it. No strings attached. Pull it from ollama.com/library/ornith. Open weights now trade blows with Claude. So, would you switch your daily driver to an open model or stay closed? Tell me below.
