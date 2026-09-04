---
categories:
  - "[[Raw]]"
title: "I created the cheapest AI voice agent possible ($0.28 per hour)"
source: "https://freedium-mirror.cfd/https://medium.com/@jordan_gibbs/i-created-the-cheapest-ai-voice-agent-possible-0-28-per-hour-e896f9e5b0c9"
author:
published:
created: "2026-07-13"
description: "30x cheaper than Elevenlabs and OpenAI. Code Included!"
tags:
  - raw
  - "agents"
  - "clip/video"
  - "voice-ai"
---
![Post cover image](https://freedium-mirror.cfd/img/700/1*Xw3CNLxo5MgHt7FxZx605g.png)

I like unsexy engineering: pick the right parts, wire them cleanly, measure the result. That's how this project happened. I built a real-time voice agent that's fast, natural, and — most importantly — costs about **$0.28 per hour** to run.

> *Code: [github.com/jordan-gibbs/hypercheap-voiceAI](https://github.com/jordan-gibbs/hypercheap-voiceAI)*

### The Nitty Gritty Details

- **All-in cost:** ~$0.25–$0.35 per session hour
- **Speech-to-text:** [Fennec streaming](https://www.fennec-asr.com/pricing) at **$0.16/hr** (Starter) or **$0.11/hr** (Scale). Comes with 10 hours free.
- **Text-to-speech:** [Inworld TTS](https://inworld.ai/tts) **$5 / 1M characters** (≈ **$0.25 per audio‑hour**). The agent typically speaks ~40–60% of the time → ~ **$0.10–$0.15/hr**. Inworld also comes with a generous free tier.
- **LLM:** [Qwen3‑235B‑A22B via Baseten](https://www.baseten.co/pricing/) at **$0.22/M input** and **$0.80/M output** tokens. Basten gives you a dollar free, so you can chat for hours.
- **Latency (measured):** ~600–800 ms from end‑of‑speech to first audio frame. Feels instant enough for realistic conversation.

### Architecture at a Glance

This is a chained architecture, stringing three AI models together to form one. While this isn't as low-latency as some blended multi-modal models (i.e., GPT-Realtime), it's ridiculously lower cost. There is also an interruption capability, which makes for a super snappy experience.

#### Fennec ASR (real‑time speech‑to‑text)

I needed **cheap, controllable streaming** with strong VAD for tight turn‑taking. Fennec's WebSocket streaming + fully tunable VAD (voice activity detection) let me end turns quickly without talking over the user. The pricing is simple and low, and there's a free tier to get you started with 10 hours free. See the [pricing](https://www.fennec-asr.com/pricing) page for details.

#### Qwen3‑235B‑A22B via Baseten's OpenAI‑compatible API

Qwen3‑235B‑A22B is a **Mixture‑of‑Experts** model (235B total, ~22B active per token). It gives excellent instruction following and reasoning at a **budget token price** when accessed through Baseten's Model APIs. Baseten is drop‑in **OpenAI‑compatible**, so swapping models is trivial.

It's crazy cheap, with a time-to-first-token latency as low as 200 ms, and performs at an intelligence level [similar to GPT-5](https://artificialanalysis.ai/leaderboards/models) at a fraction of the cost.

#### Inworld TTS (the voice)

TTS is where "cheap" usually goes to die. Inworld flipped that with **$5 per 1M characters** (≈ **$0.25 per audio‑hour**), real‑time streaming, multilingual support, and instant voice cloning. That pricing is so good, I forsee it killing entire companies (Elevenlabs, looking at you).

### The cost math (how $0.28/hr is possible)

- **ASR:** ~$0.11/hr (Scale) or $0.16/hr (Starter) with [Fennec](https://www.fennec-asr.com/pricing).
- **TTS:** ~$0.25 per audio‑hour × ~0.5 talk ratio ≈ **$0.125/hr** with [Inworld](https://inworld.ai/tts).
- **LLM:** Short replies (50–120 tokens) + capped history → **$0.01–$0.03/hr** with [Qwen3 on Baseten](https://www.baseten.co/pricing/).
- **Total:** ~$0.25–$0.35/hr → I tuned the defaults to land near **$0.28/hr**. Your exact cost depends on the verbosity and talk ratio.

### Why not other stacks?

If you need voice agents that work out of the box, with simple API endpoints and fancy UX, you'll pay dearly for them. My target was "good voice + good reasoning for pocket change."

This stack hits that. Sure, if you want to integrate, it'll take some serious work. However, if your use case is at scale, it could save your business thousands.

### Reproduce it

1. Clone [hypercheap‑voiceAI](https://github.com/jordan-gibbs/hypercheap-voiceAI).
2. Grab API keys for [Fennec](https://www.fennec-asr.com/), [Baseten](https://www.baseten.co/products/model-apis/), and [Inworld TTS](https://inworld.ai/tts) (free tier works to start).
3. Set env vars, build the front and backends, run the server, and talk.
![Cheapest voice AI agent](https://freedium-mirror.cfd/img/4000/1*Xw3CNLxo5MgHt7FxZx605g.png)

**Thanks for reading, and happy building!**

\-Jordan