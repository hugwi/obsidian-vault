---
title: "Gemma 4 Just Made My 3090 Three Times Faster"
source: "https://buttondown.com/insiderllm/archive/gemma-4-just-made-my-3090-three-times-faster/"
author:
  - "[[insiderllm team]]"
published: 2026-05-12
created: 2026-07-27
description: "I ran Gemma 4 on my own RTX 3090 today. Three times faster than Qwen 3.6 on the same hardware, same build. The numbers below, plus the flag combination that..."
tags:
  - "clippings"
---
I ran Gemma 4 on my own RTX 3090 today. Three times faster than Qwen 3.6 on the same hardware, same build. The numbers below, plus the flag combination that almost broke my bench.

---

## Gemma 4 Hit 3.10x Faster on My RTX 3090

Same RTX 3090, same llama.cpp mainline build, same bench script. Gemma 4 26B-A4B Q4\_K\_XL: 128 tok/s. Qwen 3.6-27B Q4\_K\_M: 41 tok/s. Both fit in roughly 17 GB VRAM. Same Q4 quant tier. Same nine prompts from am17an's gist bench. Speedup: 3.10x.

The architectural reason holds up under inspection. Qwen 3.6-27B is dense -- every token uses all 27B params for the forward pass. Gemma 4 26B-A4B activates 8 of 128 experts per token, plus shared layers. Effective active params per decode step is far less than the total 26B. The 3090 is bandwidth-bound on decode -- less weight moved per token directly buys more tokens per second. Total VRAM is similar because all experts must live in memory; only a fraction get used each step.

The catch: Gemma 4 forces a reasoning trace by default. Output goes to the `reasoning_content` field, so the bench script reads zero. The fix is `--jinja` plus `--chat-template-kwargs '{"enable_thinking":false}'`. Miss that combination and you'll spend an hour wondering why generation looks broken. The load log will still print `thinking = 1` -- cosmetic bug, output is correct.

Practical takeaway: if you're on a 3090 and want speed, Gemma 4 is the new pick. If you want simpler ergonomics with no flag dance, Qwen 3.6 is still rock-solid. The full bench -- all nine prompts, both models same day -- lives in the article.

📖 **The full firsthand bench is [here](https://insiderllm.com/guides/wicked-fast-gemma-4-26b-a4b-vs-qwen-3-6-27b-rtx-3090/?utm_source=insiderllm&utm_medium=email&utm_campaign=gemma-4-just-made-my-3090-three-times-faster).**

---

## DFlash vs MTP: I Tested Both on the Same 3090

Two speculative decoding methods for local inference, both shipping the same week. DFlash uses an external draft model plus tree verification; MTP uses extra layers baked into the same checkpoint. Both run on a single RTX 3090. Both speed up Qwen 3.6-27B Q4\_K\_M decode. Neither wins cleanly.

The numbers: DFlash 2.56x. MTP 1.50x. Same hardware, different prompt suites — DFlash on the LuceOrg academic benches (HumanEval, GSM8K, Math500), MTP on am17an's mixed-prompt gist. Treat as directional, not apples-to-apples. The full methodology caveats are in the article.

Where DFlash wins: raw decode speedup, mature 3.5 draft. Where MTP wins: single GGUF, mainline llama.cpp, no fork required. The composition experiment -- MTP draft tokens fed into DDTree verification -- is the obvious next bench. Nobody has built it yet.

📖 **The full head-to-head with methodology caveats is [here](https://insiderllm.com/guides/dflash-vs-mtp-rtx-3090-head-to-head/?utm_source=insiderllm&utm_medium=email&utm_campaign=gemma-4-just-made-my-3090-three-times-faster).**

---

## The Gemma 4 Launch Wave

Today's r/LocalLLaMA had three Gemma 4 reproductions in the top 20. Score-16: Gemma 4 26B at 600 tok/s on a single RTX 5090. Score-14: Qwen 3.6 35B-A3B hype thread (still kicking). Score-12: MTP for Gemma 4 in llama.cpp, ~40% additional speedup on top of the base numbers. Score-8: NVFP4 GGUFs shipping for Blackwell -- reportedly smaller than Q4\_K\_M with comparable quality.

On the architecture side, Chris Hay published a May 5 video showing decoupled attention via LARQL -- attention runs locally on a small GPU while FFN experts stream from a remote CPU server. Gemma 4 26B-A4B works in the setup, with the residual stream passing over HTTP at ~41 MB per token. Chris Hay's demo showed 24 tok/s on a laptop with the FFN server on the same LAN.

The pattern is clear. Speculative decoding, hybrid architectures, distributed inference -- the practical performance ceiling for consumer hardware just moved up about 3x in two weeks.

📖 **Full Gemma 4 guide is [here](https://insiderllm.com/guides/gemma-4-local-ai-guide/?utm_source=insiderllm&utm_medium=email&utm_campaign=gemma-4-just-made-my-3090-three-times-faster).** LARQL coverage is [here](https://insiderllm.com/guides/run-31b-models-laptop-larql/?utm_source=insiderllm&utm_medium=email&utm_campaign=gemma-4-just-made-my-3090-three-times-faster).

---

### Quick Hits

- **Unsloth releases MTP variants** (today's r/LocalLLaMA score-11). Qwen 3.6 MTP weights now available alongside the standard checkpoints.
- **DeepSeek V4 Flash at 85 tok/s @ 524K context** on dual RTX PRO 6000 (today's score-9). The long-context story is real.
- **FLUX.2 \[klein\] one-prompt-to-cinema** pipeline trending (today's score-16). Stitched generation plus interpolation for short-form video from a single prompt.
- **Qwen 3.6 35B-A3B** still the workhorse for 16GB-VRAM owners -- daily r/LocalLLaMA threads keep finding new configs.
- **NVFP4 GGUFs** shipping for Gemma 4. Memory savings on every card, native acceleration only on Blackwell.
- **Catalog housekeeping:** 10 article refreshes shipped this week. Freshness tracker now reads raw access logs instead of the top-20 markdown table -- coverage jumped from 20 to 273 articles flagged.

---

That's the week. Next edition drops next Monday.

\-- InsiderLLM

---

**Running local AI on weird hardware? Built something novel with it?** We're always looking for real benchmarks and creative local AI applications. Drop us a line at [hello@insiderllm.com](mailto:hello@insiderllm.com)

---

*You're getting this because you signed up at insiderllm.com. Unsubscribe*