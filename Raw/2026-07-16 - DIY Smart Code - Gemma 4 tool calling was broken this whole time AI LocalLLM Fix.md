---
title: "Gemma 4 tool calling was broken this whole time #AI #LocalLLM #Fix"
source: "youtube"
url: "https://www.youtube.com/watch?v=yGTLgQ6pX48"
author: "DIY Smart Code"
published: "2026-07-16"
created: "2026-08-24"
duration: "0:00:59"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "google"
  - "hardware"
  - "local-llm"
summary: "Google Gemini just posted this. Big fixes are rolling out to Gemini 4. And if the model kept fumbling your tool calls, it was not your prompt."
---

# Gemma 4 tool calling was broken this whole time #AI #LocalLLM #Fix

![Gemma 4 tool calling was broken this whole time #AI #LocalLLM #Fix](https://www.youtube.com/embed/yGTLgQ6pX48)

## Description

Google Gemma 4 just got a big update — and if the local LLM kept fumbling function calling and tool calls, it wasn't your prompt. The chat template itself was broken. Here's the one-file fix (grab the updated chat_template.jinja from Hugging Face, run llama-server --jinja), plus what actually changed: tool calling patched, chat template rebalanced, vision tokens 280 → 1120, and Flash Attention 4 on Hopper.

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

What you will see in this 60-second breakdown:
→ Why Gemma 4 tool calls kept failing — the chat template was broken, not your prompt
→ The one-file fix: download chat_template.jinja from Google's Hugging Face repo
→ Point your runner at it: llama-server --jinja --chat-template-file chat_template.jinja
→ Four real fixes: tool calling patched, chat template rebalanced, vision 280 → 1120 tokens, Flash Attention 4
→ The catch: the weights never changed — only the chat template and the docs

Gemma 4 collection (Hugging Face): https://huggingface.co/collections/google/gemma-4

The weights didn't change — only the chat template and the docs. So: is this still Gemma 4, or should Google have called it 4.1? Drop your pick below.

#Gemma4 #GoogleGemma #LocalLLM #LocalAI #LLM #OpenSourceAI #FunctionCalling #ToolCalling #ChatTemplate #LlamaCpp #LMStudio #Ollama #AICoding #AgenticAI #GemmaInstall #RunLLMLocally #PrivateAI #GoogleAI #MachineLearning #AITools

## Transcript

Google Gemini just posted this. Big fixes are rolling out to Gemini 4. And if the model kept fumbling your tool calls, it was not your prompt. The chat template itself was broken. The fix is one file. Grab the updated chat template from Google's Hugging Face page. Point your runner at that file. Suddenly, tool calls line up and the laziness is gone. Here is what actually changed. Tool calling got patched for consistent runs. The template now keeps thinking and turn tags in order. Vision can climb from 280 tokens to 1120 for sharp detail. And flash attention 4 lands on Hopper data center chips, not your laptop. That is 25 to 70% faster prefill for the clouds you already pay for. One catch. The weights did not change. Only the chat template and the docs. Same model, cleaner instructions. So, the fight in the replies is simple. Is this still Gemini 4 or should Google have called it 4.1? Tell me your pick.
