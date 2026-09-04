---
categories:
  - "[[Raw]]"
title: "Coding with Local Agents on an RTX 3090"
source: "https://praeclarum.org/2026/05/05/coding-with-local-agents.html"
author:
  - "[[praeclarum.org]]"
published: "2026-05-05"
created: "2026-07-13"
description: "TL;DR Running coding agents on local machines has never been easier. This article gives easy setup instructions for running Qwen 3.6 27B on an RTX 3090 in Li..."
tags:
  - raw
  - "agents"
  - "clip/video"
  - "local-llm"
---
**TL;DR** Running coding agents on local machines has never been easier. This article gives easy setup instructions for running Qwen 3.6 27B on an RTX 3090 in Linux. I then show how to use the model in VS Code using the LLM Gateway extension. By the end of this guide, you’ll be free of service providers and able to run a variety of OSS models.

**Update (May 16, 2026)**: Over a week has gone by since posting this, so of course everything has changed. Well not *everything* but MTP is the new performance hotness and I’ve added a section about how I use it at the end.

## Overview

There are roughly two steps to running a local coding agent:

1. Get the model up and running serving the standard chat API.
2. Connect the model to your coding environment (e.g., VS Code).

There are hundreds of different OSS models, and hundreds of different model servers to choose from. You have, frankly, an overwhelming number of options to fulfill step #1. That said, if you’re looking to run these models on consumer-grade hardware, you will be looking at models in the 7B-31B parameter range. Here is one site, of many, that tries to rank these beasts: [Artificial Analysis](https://artificialanalysis.ai/models/open-source/small#intelligence)

For this guide, I will focus on **Qwen 3.6 27B** from Alibaba since it works well-enough. But **Gemma 4 31B** from Google is a champ and is worth also looking at.

There is a wonderful arms race happening with model servers right now too. A model server is a giant math library, optimized into oblivion, that deigns to run an HTTP server so it can service requests. But it also has one more crucial component: a caching layer that keeps as much of chat conversations in GPU memory as possible in order to minimize latency and compute time - the KV cache.

For this guide, I will focus on [**llama.cpp**](https://llama-cpp.com/) since it is pretty popular, easy to use, and has good GPU support. But there are a number of other servers that are worth looking at, including [**vLLM**](https://vllm.ai/), [**Ollama**](https://ollama.com/), [**MLX-LM**](https://github.com/ml-explore/mlx-lm), [**MTPLX**](https://mtplx.com/), and on and on.

## Download the Model

This is both the easy part, and the hard part. Easy, because all you have to do is go to Hugging Face and download any of the thousands of models available. It’s hard because there are *so many models*! There’s model families, model sizes, model fine tunes, model quantizations, model formats. Oh my!

Most inference engines (like llama.cpp) support a specific set of model formats, so that will narrow down your options. For llama.cpp, the supported format is GGUF, so you’ll want to look for [models in that format](https://huggingface.co/models?search=gguf). For MLX models (to run on Apple Silicon), you’ll look in the [mlx-community](https://huggingface.co/mlx-community).

You’ll now need to pick a quantization size. Quantization is a compression method for model weights. If we took a 27 billion parameter model with 32-bit floating point weights, it would be 27B \* 32 bits = 108 GB in size. Unless you have a datacenter handy, you won’t be running that. Instead, you’ll choose, say a 4-bit quantized model. This will compress the weights down to 27B \* 4 bits = 13.5 GB, which is much more manageable for consumer hardware. The tradeoff is that quantization can reduce the model’s performance and accuracy, but it’s often a necessary compromise.

Now the RTX 3090 has 24 GB of VRAM so you might be tempted to pick a higher-bit quantization, but you have to keep in mind that the *context* and the *output* also have to fit in GPU memory. If you want long contexts and long outputs, you might have to go with a lower-bit quantization to ensure everything fits.

The `Q4_K_M` quantization format is a good compromise for a 27B model and a 24 GB GPU. So I’m going to download the `Qwen 3.6 27B Q4_K_M` model from Hugging Face:

```bash
wget "https://huggingface.co/unsloth/Qwen3.6-27B-GGUF/resolve/main/Qwen3.6-27B-Q4_K_M.gguf?download=true"
```

(`wget` is a little dumb, so you’ll need to rename the file after downloading it since it doesn’t handle the `?download=true` part of the URL very well.)

## Build llama.cpp

You can download prebuilt libraries of llama.cpp but if you want to ensure its optimized for your machine and hardware, you’ll want to build it yourself. Thankfully, it’s pretty easy to do:

```bash
git clone https://github.com/ggerganov/llama.cpp
cd llama.cpp
cmake -B build -DGGML_CUDA=ON
cmake --build build --config Release -j 8
```

Aside from the nastiness of having to use CMake, building software doesn’t get much easier than this.

I passed the `-DGGML_CUDA=ON` flag to ensure that I get NVIDIA CUDA support, which is crucial for running these large models on consumer-grade hardware. If you’re on an M-series Mac, you would want to pass `-DGGML_METAL=ON` instead to get support for Apple’s Metal API.

If all goes well, you will have a nice, shiny `build/bin/llama-server` executable that you can use to serve your model.

## Run the Server

You will want to run the server with a delicious soup of command line arguments. Something like this:

```bash
./build/bin/llama-server -m ~/Downloads/Qwen3.6-27B-Q4_K_M.gguf --host 0.0.0.0 -ngl 99 -c 262144 -fa on --cache-type-k q4_0 --cache-type-v q4_0
```

Let’s deconstruct that soup:

| Argument | Description |
| --- | --- |
| `-m` | The path to the model file you downloaded. |
| `--host 0.0.0.0` | This tells the server to listen on all network interfaces, which is necessary if you want to connect to it from another machine (e.g., your dev machine). |
| `-ngl 99` | This sets the number of GPU layers to use. Setting this to 99 tells the server to use as many GPU layers as possible, which will maximize performance. |
| `-c 262144` | This sets the context size to 262,144 tokens, which is the maximum context size for this model. You can adjust this based on your needs and GPU memory constraints. |
| `-fa on` | This enables the “faster auto-regressive decoding” feature, which can improve performance. |
| `--cache-type-k q4_0 --cache-type-v q4_0` | This sets the quantization type for the KV cache to `q4_0`, which is a good choice for performance and memory efficiency. |

Notice how we are quantizing the KV cache (context and outputs) as well. This is a crucial step for ensuring that the model runs efficiently on consumer-grade hardware, as the KV cache can consume a significant amount of GPU memory.

You’ll be greeted with typical programmer excretions:

```
ggml_cuda_init: found 1 CUDA devices (Total VRAM: 24159 MiB):
  Device 0: NVIDIA GeForce RTX 3090, compute capability 8.6, VMM: yes, VRAM: 24159 MiB
main: n_parallel is set to auto, using n_parallel = 4 and kv_unified = true
build_info: b9026-a817a22bc
system_info: n_threads = 6 (n_threads_batch = 6) / 12 | CUDA : ARCHS = 860 | USE_GRAPHS = 1 | PEER_MAX_BATCH_SIZE = 128 | CPU : SSE3 = 1 | SSSE3 = 1 | AVX = 1 | AVX2 = 1 | F16C = 1 | FMA = 1 | BMI2 = 1 | LLAMAFILE = 1 | OPENMP = 1 | REPACK = 1 | 
Running without SSL
init: using 11 threads for HTTP server
start: binding port with default address family
main: loading model
srv    load_model: loading model '/home/fak/Downloads/Qwen3.6-27B-Q4_K_M.gguf'
common_init_result: fitting params to device memory, for bugs during this step try to reproduce them with -fit off, or provide --verbose logs if the bug only occurs with -fit on
common_params_fit_impl: getting device memory data for initial parameters:
common_memory_breakdown_print: | memory breakdown [MiB] | total    free     self   model   context   compute    unaccounted |
common_memory_breakdown_print: |   - CUDA0 (RTX 3090)   | 24159 = 23257 + (21388 = 15345 +    5206 +     836) +      -20486 |
common_memory_breakdown_print: |   - Host               |                   1214 =   682 +       0 +     532                |
common_params_fit_impl: projected to use 21388 MiB of device memory vs. 23257 MiB of free device memory
common_params_fit_impl: will leave 1868 >= 1024 MiB of free device memory, no changes needed
common_fit_params: successfully fit params to free device memory
common_fit_params: fitting params to free memory took 0.66 seconds
llama_model_loader: loaded meta data with 51 key-value pairs and 851 tensors from /home/fak/Downloads/Qwen3.6-27B-Q4_K_M.gguf (version GGUF V3 (latest))
```

Congratulations. You’re now an AI service provider. I recommend getting some seed capital and start selling access to your model to the highest bidder.

But before you do that…

## Install LLM Gateway in VS Code

I rock VS Code for all my coding needs, and I want to be able to use my local model in its AI agent chat window thingy. To do that, I need to install an extension that connects VS Code to the standard chat API. (Why VS Code doesn’t support the API standard that literally *every* LLM server provides is beyond me.)

ANYWAY, I like the [LLM Gateway extension](https://marketplace.visualstudio.com/items?itemName=AndrewButson.github-copilot-llm-gateway) by Andrew Butson.

1. Install that extension.
2. Open the “GitHub Copilot LLM Gateway: Configure Server” UI from the command palette and enter the URL for your server (e.g., `http://my-awesome-server.local:8080`).
3. Test the connection with the “GitHub Copilot LLM Gateway: Test Server Connection” command. It should say “Found 1 model(s)” if everything is working. (If it’s not working, email James Montemagno and ask him for help.)
4. Open the “Chat: Manage Language Models” UI from the command palette. You should see your model listed but it will probably be grayed out for some reason. Click it, click the eye ball (gross!), and it should now be active and ready to use in the chat window.
5. Open the chat window, and click the model selector. Choose “Other Models”, scroll, and scroll, looking for your model. It’s there somewhere. I promise. You might doubt it, but have faith. When in doubt, keep scrolling. You can do it. You found it! Click it, and now you can use your local model in the chat window!

## MTP for Speed

(Added May 16, 2026)

Since posting this article, Multi-Token Prediction (MTP) has been released, and it is a game changer for performance. MTP is a new parallelism method that *somehow* makes things faster by doing more work. Weird, I know. Instead of the purely serial operation of (1) generate a token, (2) add it to the context, (3) GOTO 1, MTP uses a much smaller model to *quickly* do the 1-2-3 dance for a few tokens and then uses the real model **to verify the results**. Given the nature of these beasts, the smaller model takes up very little wall time but still has OK-ish accuracy. The big model, instead of being just a generator, is used to verify the probabilities of these new tokens. It can do that quickly because it doesn’t need to test them one at a time, but can test them all in parallel (vs serial). Since modern LLMs are memory bandwidth bound, not compute bound, this parallel execution is “free”. The result is a huge speed boost, about 1.4x-1.8x. It’s a crazy hack, and I’m here for it.

As of this writing, MTP is still a work-in-progress for llama.cpp, but it is available in PRs and forks. I’m compiling using [am17an’s fork](https://github.com/am17an/llama.cpp/tree/mtp-clean).

```bash
./build/bin/llama-server -hf unsloth/Qwen3.6-27B-MTP-GGUF:UD-Q4_K_XL --host 0.0.0.0 -c 150000 -ngl 99 -fa on --cache-type-k q4_0 --cache-type-v q4_0 --temp 0.6 --top-p 0.95 --top-k 20 --presence-penalty 0.0 --min-p 0.00 --spec-type draft-mtp --spec-draft-n-max 2
```

The important new args are:

| Argument | Description |
| --- | --- |
| `--spec-type draft-mtp` | This tells the server to use the MTP parallelism method. |
| `--spec-draft-n-max 2` | This sets the maximum number of tokens to predict in parallel. 2 is a very conservative choice. |

I’ve also modified a few other sampling parameters based on recommendations for coding environments:

| Argument | Description |
| --- | --- |
| `--temp 0.6` | This sets the temperature to 0.6, which is a good choice for coding tasks as it encourages more deterministic outputs while still allowing for some creativity. |
| `--top-p 0.95` | This sets the nucleus sampling parameter to 0.95, which helps to ensure that the model generates more relevant and coherent code by focusing on the most probable tokens. |
| `--top-k 20` | This sets the top-k sampling parameter to 20, which limits the number of tokens considered at each step to the 20 most likely, further improving the relevance of the generated code. |
| `--presence-penalty 0.0` | This sets the presence penalty to 0.0, which means that the model will not be penalized for generating tokens that have already appeared in the context, which can be beneficial for coding tasks where repetition of certain tokens (e.g., variable names, function names) is common. |
| `--min-p 0.00` | This sets the minimum probability threshold to 0.00, which means that the model will consider all tokens regardless of their probability, allowing for a wider range of potential outputs. |

I also switched to the `Qwen3.6-27B-MTP-GGUF` model, which includes the smaller MTP model needed for the parallel token prediction. And I switched to the `UD-Q4_K_XL` quantization format, because guessing which quantization format to use is half the fun of self-hosting models.

## Local Fleet Update — August 2026

The machine described in this note has moved beyond the original single-model
Qwen 3.6 setup. It now uses `llama-swap` in front of several `llama-server`
instances. Only one large model occupies the RTX 3090 at a time; requesting a
different model stops the current container and starts the requested one.

The default local coding model is now **Qwen 3.8 27B UD-Q4_K_XL**, served as
`local-coder`. Its measured configuration is:

```text
weights:              Qwen3.8-27B-UD-Q4_K_XL.gguf (17.56 GB)
server:               llama.cpp / llama-server
context:              131,072 tokens
KV cache:             Q4_0 for K and V
GPU layers:           99 (full offload)
speculative decoding: embedded MTP, draft length 2
reasoning budget:     2,048 tokens by default
measured decode:      49.13 tokens/s (SPEED-Bench coding, n=12)
MTP acceptance:       70.2%
measured peak VRAM:   20,586 MiB
```

### Verified GPU placement — 2026-09-03

The Qwen 3.8 service now uses explicit CUDA-only placement in Docker:

```text
--device CUDA0 --gpu-layers all --split-mode none --main-gpu 0
--kv-offload --op-offload --fit off
```

`--fit off` prevents llama.cpp from silently adjusting the configuration to
fit by moving work away from the GPU. The service recreated successfully on the
RTX 3090, passed its health check, and reported approximately 20.6 GiB VRAM in
use with only 1.4 GiB host RAM used by the container. A 256-token request
measured 57.7 generated tokens/s with MTP enabled, compared with the earlier
49.13 tokens/s SPEED-Bench coding result; these are different tests, so the
figures should not be treated as a strict apples-to-apples benchmark.

The host experienced an out-of-memory event on 2026-09-02 at 09:19 while the
27B model was running. Linux killed the Qwen container's `llama-server`, which
Docker restarted with exit code 137. GPU offload does not eliminate host RAM:
the process still needs system memory for runtime state, buffers, mapped data,
and pinned CUDA transfers. The RTX 3090 deployment therefore remains GPU-first,
but the 131K context and concurrent model services still require monitoring.

### Weight memory is not total inference memory

The model file is only one consumer of VRAM. A useful approximation is:

```text
total VRAM = weights + KV cache + recurrent state + compute workspace
             + speculative drafter/MTP state + runtime overhead
```

**Weight quantization** compresses the learned parameters. It answers: “How
much memory is needed to store what the model knows?” **KV-cache quantization**
compresses the attention state created while processing the current prompt and
conversation. It answers: “How much memory is needed to remember this active
sequence?” They are independent choices.

The KV cache stores key and value vectors used by attention so the server does
not recompute the whole prefix for every generated token. Its size grows roughly
linearly with:

```text
number of cached tokens × KV heads × head dimension × attention layers
× bytes per KV element × active sequences
```

This is why a 10 GB weight file can still nearly fill a 24 GB GPU at long
context. Smaller weights create headroom, but a 128K FP16 KV cache can consume
that headroom again. Conversely, the current 17.56 GB Qwen GGUF fits a 128K
context because its K and V caches are separately compressed to Q4_0 and the
server runs only one sequence (`--parallel 1`). Context and concurrency spend
the same memory pool: four simultaneous 32K conversations can cost roughly as
much cache memory as one 128K conversation, before runtime overhead.

Qwen 3.8 is a hybrid architecture: 16 of its 64 layers use full attention and
the other 48 use gated-delta/recurrent state. The recurrent part has a mostly
fixed per-sequence cost, while the full-attention KV cache grows with context.
That makes long context cheaper than it would be in a conventional 64-layer
full-attention model, but it does not make context free.

### Quantization levels: Q8, Q4, and W2 are different products

The number in a quantization name is a useful direction, not a complete quality
or size specification. Metadata, scales, tensors left at higher precision, and
mixed per-tensor rules mean actual bits per weight and file sizes differ from
the label.

| Format | What it means in practice | 27B-class weight size | RTX 3090 role |
| --- | --- | ---: | --- |
| BF16 | Original 16-bit weights | ~55 GB | Does not fit on one 24 GB card |
| FP8 / Q8 | Roughly 8-bit weights; high-fidelity reference | ~28–36 GB depending on format | Weights alone exceed VRAM; requires CPU offload or multiple GPUs |
| Q6 | Higher-fidelity GGUF compromise | ~22–25 GB | Leaves too little room for useful long-context cache |
| Q4_K_M / UD-Q4_K_XL | Mixed 4-bit GGUF with important tensors kept higher | ~15–18 GB | Current sweet spot for a 27B model plus long Q4 KV cache |
| Q3 | More aggressive GGUF | ~12–14 GB | More context headroom, but greater quality risk |
| Q2 / IQ2 | Very aggressive generic GGUF | ~9–11 GB | Fits easily, but generic 2-bit quants often degrade sharply |
| Escha W2 | Custom learned mixed 2/3-bit format, 2.469 bits/weight | 10.15 GB | Promising quality, but needs Escha's custom SGLang runtime |

**Q8 is valuable as a quality reference, not as the practical single-3090
configuration.** Q8/FP8 usually retains nearly all of the source model, but the
weights do not leave enough VRAM for a useful KV cache on a 24 GB card. CPU
offload would make it run, but PCIe transfers normally reduce interactive coding
speed. Two GPUs could hold it, but that changes the system and power budget.

The `K_M`, `K_XL`, `UD`, and `IQ` parts matter. A dynamic quantizer can keep
error-sensitive tensors at more bits and compress tolerant tensors harder. Two
files both advertised as “4-bit” can therefore differ in size, speed, MTP
contents, and benchmark quality. The earlier Qwen 3.6 comparison exposed this
directly: its plain `Q4_K_M` included the MTP head, while its `UD-Q4_K_XL` file
did not. Always inspect model metadata and benchmark the exact file rather than
reasoning from the label alone.

### Escha W2: why 10.15 GB can still use about 22 GB

`Qwen3.8-27B-Escha-W2` is not a normal `Q2_K` GGUF. Escha uses a learned custom
format: mixed 2/3-bit projections averaging 2.469 bits per weight, INT8 embedding
and output head, and selected FP16 tensors. It is served by an Escha-specific
SGLang wheel with custom CUDA kernels. The current release cannot simply replace
the GGUF path in `llama-server`.

The early result “~100% FP8 benchmark performance” means **approximately the
same benchmark quality**, not 100% of FP8 inference speed. It covers eight early
benchmarks and should not yet be treated as proof of identical behavior across
large repositories, tool use, obscure languages, or long agent sessions.

On a 24 GB card, Escha reports:

| Escha W2 configuration | Context/purpose | Peak VRAM or result |
| --- | --- | --- |
| Shipped default | 64K, single user | ~18.3 GB; 40.7 tok/s reported on RTX 3090 |
| Tuned long context | 128K, one stream | ~21.8 GB allocation |
| Measured 120K prompt | 128K recipe | ~22.1 GB peak |
| Practical maximum | ~147K | ~22.7 GB with little safety margin |

The apparent paradox is therefore expected:

```text
Escha W2: 10.15 GB weights + larger FP16 KV/state/workspace ≈ 22 GB
Our Q4 XL: 17.56 GB weights + compressed Q4 KV/workspace ≈ 20.6 GB
```

The smaller model file can use *more total VRAM* because the two deployments use
different cache precision and different runtimes. An apples-to-apples comparison
must hold context length, KV precision, concurrency, speculative decoding, and
runtime constant—not just the weight file.

### Current model trade-offs on this RTX 3090

| Model | Configured context | Best use | Main trade-off |
| --- | ---: | --- | --- |
| **Qwen 3.8 27B UD-Q4_K_XL + MTP** | 128K | Default local coder; strongest current Qwen option | ~20.6 GB VRAM; one active stream; 2,048-token reasoning cap prevents overthinking |
| Qwen 3.6 27B Q4_K_M + MTP | 128K with Q4 KV | Proven rollback; high MTP acceptance | Slightly older model; best tested `-ngl 99` config was 48.60 tok/s |
| Qwen 3.6 27B UD-Q4_K_XL | 128K | Quant-matched baseline | This exact file has no MTP head and decoded at only 29.60 tok/s |
| Gemma 4 31B Q4_K_M | 64K | Dense planner alternative | Shorter context and no measured MTP advantage here |
| Gemma 4 26B MoE Q5_K_M + external MTP | 128K | Builder/throughput alternative | Separate draft model and more moving parts |
| Gemma 4 E4B Q4_K_M | 128K | Small, fast general model | Lower effective capability than the dense 27B/31B choices |
| Gemma 4 12B Q4_K_M | 256K | Maximum configured context, cheaper utility work | Smaller model; long context does not compensate for weaker reasoning |
| **Escha Qwen 3.8 W2** | 64K default; 128K tuned | Experimental high-quality 2-bit deployment; possible concurrency headroom | Custom SGLang stack; early quality evidence; reported 3090 single-stream speed is below our measured MTP setup |
| Qwen 3.8 FP8/Q8 | Architecture supports long context, hardware does not fit it cleanly | Quality baseline or multi-GPU experiment | ~28–36 GB weights before KV cache; unsuitable for one 24 GB 3090 without offload |

The current recommendation is to keep **Qwen 3.8 UD-Q4_K_XL + MTP + Q4 KV** as
the production local coder. It delivered 49.13 tok/s on the local coding
benchmark and already fits 128K with safe VRAM headroom. Escha W2 is worth an
A/B test once its runtime is mature or its promised GGUF support arrives, but
its current advantage is weight compression—not a demonstrated improvement in
single-user coding speed or total 128K VRAM use on this machine.

Sources for this update:

- [Qwen3.8-27B official model](https://huggingface.co/Qwen/Qwen3.8-27B)
- [Escha W2 announcement](https://www.reddit.com/r/Qwen_AI/comments/1vtpqdr/2bit_qwen3827b_1015gb_100_fp8_benchmark/)
- [Escha W2 model card](https://huggingface.co/EschaLabs/Qwen3.8-27B-Escha-W2)
- [llama.cpp](https://github.com/ggml-org/llama.cpp)

Related: [[MOC - LLM Foundations]] · [[How to Run Local LLMs with Claude Code (01knfghh056rdn8jn8dnjkffy7)]] · [[Tested MTP with llama.cpp and Qwen3.6-27B on RTX 3090  rLocalLLM]]

## Is it Worth It?

What does an RTX machine cost these days?

| Component | Price (USD) |
| --- | --- |
| RTX 3090 | $1500 |
| CPU | $300 |
| 64 GB RAM | $700 (what has the world come to?) |
| HDD | $200 |
| PSU | $150 |
| Case | $100 |
| **Total** | **$2,950** |

So for about $3,000 you can have your very own local coding agent. That’s a pretty hefty price tag, but it’s also a one-time cost.

In a typical day, I burn through about 50,000,000 tokens. 500,000 output tokens, 1,750,000 input tokens, and the rest are cache hits. At 40 tok/second (typical for my RTX), my compute day is about `(500,000 + 1,750,000) / 40 = 56,250 seconds`, which is about **15.6 hours of compute time per day**. Ugh.

Right now, you can use DeepSeek for $3.48 per 1,000,000 output tokens, $1.74 for inputs, and $0.0145 for cache hits. So my daily cost would be `(500,000 / 1,000,000) * 3.48 + (1,750,000 / 1,000,000) * 1.74 + (47,750,000 / 1,000,000) * 0.0145 = $5.48` per day. That’s about $1,400 per year (five day work weeks). So in about 2 years, I would recoup the cost of running my own local agent. Hmmm…

So you might not want to run out and buy your own server. But, if you do have an over-provisioned gaming rig, well you might as well put it to use doing something useful.;-) X

## Conclusion

Since 2017 I have been advocating running local models. I’m amazed that it’s now possible to run 27B parameter variants on consumer hardware. (In my mind, 7B is still tremendous.) These are real models, able to write good code, in a fully agentic harness. Amazing.

While the up front hardware cost, the noise of fans, and the slower response rates are not ideal and don’t make this an easy win, I have a different perspective. AI coding has changed how I work. Permanently. I do not want to go back to writing every line of code by hand, it seems absurd now. But I also don’t like being at the mercy of large cloud providers. Having the ability to run my own local agent, even with its limitations, is a huge win for me. I know, even with no internet connection, I can still do what I love: code.

**Colophon:** Written by hand. Proofread and edited by Qwen 3.6 27B running on an RTX 3090.
