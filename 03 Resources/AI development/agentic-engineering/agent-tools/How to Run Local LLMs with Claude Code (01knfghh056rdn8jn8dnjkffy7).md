---
title: "How to Run Local LLMs with Claude Code"
source: "https://unsloth.ai/docs/basics/claude-code"
author: "unsloth.ai"
published: 
created: 2026-04-05
description: "Guide to use open models with Claude Code on your local device."
tags:
  - to-process
  - agent-tools
---

This step-by-step guide shows you how to connect open LLMs and APIs to Claude Code entirely locally, complete with screenshots. Run using any open model like Qwen3.5, DeepSeek and Gemma.


For this tutorial, we’ll use [**Qwen3.5**](https://unsloth.ai/docs/models/qwen3.5) and [GLM-4.7-Flash](https://unsloth.ai/docs/models/glm-4.7-flash). Both are the strongest 35B MoE agentic & coding model as of Mar 2026 (which works great on a 24GB RAM/unified mem device) to autonomously fine-tune an LLM with [Unsloth](https://github.com/unslothai/unsloth). You can swap in [any other model](https://unsloth.ai/docs/models/tutorials), just update the model names in your scripts.


For model quants, we will utilize Unsloth [Dynamic GGUFs](https://unsloth.ai/docs/basics/unsloth-dynamic-2.0-ggufs) to run any LLM quantized, while retaining as much accuracy as possible.


Claude Code has changed quite a lot since Jan 2026. There are lots more settings and necessary features you will need to toggle.


Before we begin, we firstly need to complete setup for the specific model you're going to use. We use `llama.cpp` which is an open-source framework for running LLMs on your Mac, Linux, Windows etc. devices. Llama.cpp contains `llama-server` which allows you to serve and deploy LLMs efficiently. The model will be served on port 8001, with all agent tools routed through a single OpenAI-compatible endpoint.


We'll be using [Qwen3.5](https://unsloth.ai/docs/models/qwen3.5)-35B-A3B and specific settings for fast accurate coding tasks. If you don't have enough VRAM and want a **smarter** model, **Qwen3.5-27B** is a great choice, but it will be ~2x slower, or you can use other Qwen3.5 variants like 9B, 4B or 2B.


We need to install `llama.cpp` to deploy/serve local LLMs to use in Claude Code etc. We follow the official build instructions for correct GPU bindings and maximum performance. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F4DmycqgjxOz6TOQd9PLJ%252Fimage.png%3Falt%3Dmedia%26token%3Dc94db0b5-8e4a-4043-b2a3-c68bad93213e&width=768&dpr=3&quality=100&sign=bdf790c4&sv=2)
Download the model via `huggingface_hub` in Python (after installing via `pip install huggingface_hub hf_transfer`). We use the **UD-Q4\_K\_XL** quant for the best size/accuracy balance. You can find all Unsloth GGUF uploads in our [Collection here](https://unsloth.ai/docs/get-started/unsloth-model-catalog). If downloads get stuck, see [Hugging Face Hub, XET debugging](https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging)


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FRfXofrNzl1ypjfMTz15o%252Fimage.png%3Falt%3Dmedia%26token%3D8009de90-cd11-46ed-85b5-fca5c07b66fc&width=768&dpr=3&quality=100&sign=8ceb6478&sv=2)
![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FxlIrQGQ0cevb1ckkSFy5%252Fimage.png%3Falt%3Dmedia%26token%3Db1a42562-927a-4ad2-85f8-29c2993c46aa&width=768&dpr=3&quality=100&sign=f1f734a9&sv=2)
To deploy Qwen3.5 for agentic workloads, we use `llama-server`. We apply [Qwen's recommended sampling parameters](https://unsloth.ai/docs/models/qwen3.5#recommended-settings) for thinking mode: `temp 0.6`, `top_p 0.95` , `top-k 20`. Keep in mind these numbers change if you use non-thinking mode or other tasks.


Run this command in a new terminal (use `tmux` or open a new terminal). The below should **fit perfectly in a 24GB GPU (RTX 4090) (uses 23GB)** `--fit on` will also auto offload, but if you see bad performance, reduce `--ctx-size` .



```
./llama.cpp/llama-server \
--model unsloth/Qwen3.5-35B-A3B-GGUF/Qwen3.5-35B-A3B-UD-Q4_K_XL.gguf \
--alias "unsloth/Qwen3.5-35B-A3B" \
--temp 0.6 \
--top-p 0.95 \
--top-k 20 \
--min-p 0.00 \
--port 8001 \
--kv-unified \
--cache-type-k q8_0 --cache-type-v q8_0 \
--flash-attn on --fit on \
--ctx-size 131072 # change as required
```

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252F373wtRRbMcobtjV5e6xf%252Fkerkekke.png%3Falt%3Dmedia%26token%3D2cd3b8c7-93b6-41cb-8bce-41f1aee819eb&width=300&dpr=3&quality=100&sign=87bc252b&sv=2)
We need to install `llama.cpp` to deploy/serve local LLMs to use in Claude Code etc. We follow the official build instructions for correct GPU bindings and maximum performance. Change `-DGGML_CUDA=ON` to `-DGGML_CUDA=OFF` if you don't have a GPU or just want CPU inference. **For Apple Mac / Metal devices**, set `-DGGML_CUDA=OFF` then continue as usual - Metal support is on by default.


Download the model via `huggingface_hub` in Python (after installing via `pip install huggingface_hub hf_transfer`). We use the **UD-Q4\_K\_XL** quant for the best size/accuracy balance. You can find all Unsloth GGUF uploads in our [Collection here](https://unsloth.ai/docs/get-started/unsloth-model-catalog). If downloads get stuck, see [Hugging Face Hub, XET debugging](https://unsloth.ai/docs/basics/troubleshooting-and-faqs/hugging-face-hub-xet-debugging)


To deploy GLM-4.7-Flash for agentic workloads, we use `llama-server`. We apply Z.ai's recommended sampling parameters (`temp 1.0`, `top_p 0.95`).


Run this command in a new terminal (use `tmux` or open a new terminal). The below should **fit perfectly in a 24GB GPU (RTX 4090) (uses 23GB)** `--fit on` will also auto offload, but if you see bad performance, reduce `--ctx-size` .



```
./llama.cpp/llama-server \
--model unsloth/GLM-4.7-Flash-GGUF/GLM-4.7-Flash-UD-Q4_K_XL.gguf \
--alias "unsloth/GLM-4.7-Flash" \
--temp 1.0 \
--top-p 0.95 \
--min-p 0.01 \
--port 8001 \
--kv-unified \
--cache-type-k q8_0 --cache-type-v q8_0 \
--flash-attn on --fit on \
--batch-size 4096 --ubatch-size 1024 \
--ctx-size 131072 #change as required
```

![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FyKf6guCV8snRaAV16Zxc%252FG_16XLgXUAEnSWH.jpg%3Falt%3Dmedia%26token%3D3b557c6d-3f6f-4515-ba9f-4cc8b50bcef1&width=300&dpr=3&quality=100&sign=d1173ec1&sv=2)
Once you are done doing the first steps of setting up your local LLM, it's time to setup Claude Code. Claude Code is Anthropic's agentic coding tool that lives in your terminal, understands your codebase, and handles complex Git workflows via natural language.


#### **Install Claude Code and run it locally**


### 🕵️Fixing 90% slower inference in Claude Code


To solve this, edit `~/.claude/settings.json` to include `CLAUDE_CODE_ATTRIBUTION_HEADER` and set it to 0 within `"env"`


For example do `cat > ~/.claude/settings.json` then add the below (when pasted, do ENTER then CTRL+D to save it). If you have a previous `~/.claude/settings.json` file, just add `"CLAUDE_CODE_ATTRIBUTION_HEADER" : "0"` to the "env" section, and leave the rest of the settings file unchanged.


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252Fnyc5BnXQiXPRZnyuYZt3%252Fimage.png%3Falt%3Dmedia%26token%3D72011cb6-abed-4a41-99b0-104ef5d0111f&width=768&dpr=3&quality=100&sign=5dcb00c3&sv=2)
To set Claude Code to execute commands without any approvals do **(BEWARE this will make Claude Code do and execute code however it likes without any approvals!)**


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FBkpEsVssYZG9wHvvWMRH%252Fimage.png%3Falt%3Dmedia%26token%3De1a8283f-49ed-4b78-8052-d8970f069d5b&width=768&dpr=3&quality=100&sign=279e8939&sv=2)
After waiting a bit, Unsloth will be installed in a venv via uv, and loaded up:


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FHATFwDrR1gP44XFbzWcv%252Fimage.png%3Falt%3Dmedia%26token%3D6ff63733-686d-4b08-bdd5-66a6fa4aa34c&width=768&dpr=3&quality=100&sign=de83f9f7&sv=2)
and finally you will see a successfully finetuned model with Unsloth!


![](https://unsloth.ai/docs/~gitbook/image?url=https%3A%2F%2F3215535692-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FxhOjnexMCB3dmuQFQ2Zq%252Fuploads%252FZjQ6askaixcYOMrr2qMi%252Fimage.png%3Falt%3Dmedia%26token%3De0e0047d-b6a2-421f-a86b-68e093a3a17a&width=768&dpr=3&quality=100&sign=ded47210&sv=2)
You can also use Claude Code directly inside your editor via the official extension: