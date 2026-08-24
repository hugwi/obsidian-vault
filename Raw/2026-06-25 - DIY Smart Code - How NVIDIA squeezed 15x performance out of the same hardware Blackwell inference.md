---
title: "How NVIDIA squeezed 15x performance out of the same hardware #Blackwell #inference"
source: youtube
url: https://www.youtube.com/watch?v=_thteJ-pfYE
author: "DIY Smart Code"
published: 2026-06-25
created: 2026-08-24
duration: "0:02:33"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# How NVIDIA squeezed 15x performance out of the same hardware #Blackwell #inference

![How NVIDIA squeezed 15x performance out of the same hardware #Blackwell #inference](https://www.youtube.com/embed/_thteJ-pfYE)

## Description

NVIDIA DFlash delivers up to 15x faster LLM inference on Blackwell — same hardware, same quality. This open-source speculative decoding model drafts whole token blocks in parallel and is a drop-in swap for EAGLE-3 in vLLM, SGLang, and TensorRT-LLM.

----
🚀 DYNAMOUS AI COMMUNITY

Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount

⚡ HOSTINGER — RELIABLE HOSTING FOR YOUR PROJECTS

If you build with AI tools, you eventually deploy them somewhere. I use Hostinger for fast, affordable VPS + web hosting.

👉 https://hostinger.com/DIYSMARTCODE

(Affiliate link — costs you nothing, supports the channel.)
----

What you will see in this 60-second breakdown:

→ Why token-by-token speculative decoding is the inference bottleneck
→ How DFlash uses block-diffusion drafting to propose a whole block in one pass
→ The real chart: up to 15x vs autoregressive, 2.5x vs EAGLE-3 on gpt-oss-120b (8x B300)
→ The three techniques: block-diffusion drafting, hidden-state conditioning, K-V injection
→ Why output quality stays identical — the target model verifies every accepted token
→ Drop-in adoption in vLLM, SGLang, and TensorRT-LLM, plus 20 checkpoints on Hugging Face
→ Per-task gains: coding 2.6x, retrieval 2.3x, reasoning 2.3x, multilingual 2.6x

The post: https://x.com/NVIDIAAI
The blog: https://developer.nvidia.com/blog/boost-inference-performance-up-to-15x-on-nvidia-blackwell-using-dflash-speculative-decoding/

Is token-by-token drafting officially dead now that block diffusion exists — or is 15x just a best-case benchmark that collapses on your real workload? Drop your take below.

#NVIDIA #DFlash #Blackwell #LLM #AIinference #SpeculativeDecoding #vLLM #SGLang #TensorRT #GPU #MachineLearning #AI #DeepLearning #LLMinference #OpenSource #HuggingFace #gptoss #AIengineering #CUDA #InferenceOptimization #BlockDiffusion #EAGLE3

## Transcript

Nvidia just dropped a chart that's blowing up on X. Up to 15 times higher inference throughput on the exact same hardware. The trick is a tiny open source model called D flash. Here's the problem it kills. Normal speculative decoding drafts tokens one at a time, then the big model checks them in parallel. But if you draft sequentially, you are still stuck waiting step-by-step by step. This is the receipt. On GPTOSS 120 billion running on eight Blackwell B120 GPUs, D flash hits up to 15 times the throughput of plain decoding and two and a half times Eagle 3 at the same interactivity target. And adoption is almost free. In vLLM, you swap the Eagle 3 checkpoint for a D flash one with no code changes outside the config. So, how does it work? Three moves. Block diffusion drafting predicts a whole block of future tokens in a single pass. Target hidden state conditioning feeds the drafter the big model's own context. And KV injection keeps the whole thing cheap. Against Eagle 3, it isn't close. Averaged across every task, D flash lands 2.3 times faster versus Eagle 3's 1.7. The headline number is 15 times and the output quality is identical because the target model still verifies every single token it accepts. Nvidia put it simply. Increase inference performance by up to 15 times without sacrificing responsiveness. Why it matters. It's drop-in. It preserves output quality. It's built for Blackwell's dual die chips and it ships across every major serving stack on day one. Now, fair warning. This runs on data center Blackwell chips, not your laptop. But here is why it still matters for you. The cloud APIs and tools you already use can drop it in for free. Same quality, just served faster and cheaper. Even on a single Blackwell Ultra GPU, Gemma jumps up to 5.8 times faster on math with no cluster required. It's already wired into SGLang, VLLM, and TensorRT-LLM with 20 checkpoints live on Hugging Face covering Qwen, Llama, Gemma, and more. The swap really is one line. Point your config at the DeepFlash checkpoint and you are done. And per task, the gains stack up. Coding 2.6 times, retrieval 2.3. Reasoning 2.3. Multilingual 2.6. So, is token by token drafting officially dead? Or is 15 times just a best-case benchmark? Drop your take below.
