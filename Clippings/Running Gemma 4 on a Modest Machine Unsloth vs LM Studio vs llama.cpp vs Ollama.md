---
title: "Running Gemma 4 on a Modest Machine: Unsloth vs LM Studio vs llama.cpp vs Ollama"
source: "https://dev.to/skomfi/running-gemma-4-on-a-modest-machine-unsloth-vs-lm-studio-vs-llamacpp-vs-ollama-11cp"
author:
  - "[[dev.to]]"
published: 2026-05-24
created: 2026-07-13
description: "This is a submission for the Gemma 4 Challenge: Write About Gemma 4  When local AI conversations... Tagged with devchallenge, gemmachallenge, gemma."
tags:
  - "clippings"
---
Gemma 4 Challenge: Write about Gemma 4 Submission

*This is a submission for the [Gemma 4 Challenge: Write About Gemma 4](https://dev.to/challenges/google-gemma-2026-05-06)*

When local AI conversations happen online, they tend to sound like this: "I ran the 70B model on my dual-GPU workstation." or "You only need 64GB RAM and a 24GB graphics card."

Meanwhile, I'm sitting with an Intel i5, 16GB RAM, integrated graphics, roughly 350GB of storage, and no monster GPU hiding under my desk.  
That made me curious. If I wanted to build something with Gemma 4 locally, which stack actually makes sense on hardware that most developers realistically own?

So I looked at four names that keep coming up: Unsloth, LM Studio, llama.cpp, and Ollama.  
At first they looked like competing products. After spending time with them, I realised they solve different parts of the same problem.

## The first lesson: these tools aren't really competitors

My initial assumption was simple. Pick one, ignore the others.  
But they fit together more like a pipeline:

- Model fine-tuning → Unsloth
- Inference engine → llama.cpp
- Serving layer → Ollama
- Desktop UI → LM Studio

Rather than replacing each other, they stack. In fact, LM Studio and Ollama both use llama.cpp under the hood. You don't necessarily need to install llama.cpp separately unless you want direct, low-level control over quantization or server flags.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6emedxi2cp653sakggxl.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F6emedxi2cp653sakggxl.png)

## Unsloth: fine-tuning without the anxiety

Fine-tuning usually sounds expensive. Huge GPUs, large memory requirements, long training runs. Unsloth tries to cut that cost significantly.  
Would I train a large Gemma variant on my setup? Probably not. But smaller experiments and LoRA fine-tuning on the E2B or E4B models feel a lot less out of reach. The interesting thing about Unsloth isn't just the speed gains. It's that it makes the whole process feel less like something only research labs do.  
That said, on a CPU-only machine, even small fine-tuning jobs are slow. For anything beyond a quick experiment, I'd probably train in a free Google Colab session with a T4 GPU, then export the resulting GGUF to run locally.

## LM Studio: the least intimidating place to start

LM Studio removes almost all the friction. Download it, pick a model, run it, start testing. For a machine like mine, that matters.  
The tradeoffs are real though. Larger models hit hardware limits quickly, and you have less control than you'd get with lower-level tools. But if someone asked me where to start if they've never run a local model before, LM Studio would be my first recommendation.

## llama.cpp: the engine quietly powering everything

llama.cpp isn't flashy. No polished interface, no big buttons. But it shows up everywhere, and for good reason.  
The smallest Gemma 4 model needs roughly 4GB of RAM at Q4 quantization, and the largest can push to around 20GB. On a 16GB machine, that headroom matters. Quantized models running through llama.cpp are often what makes local AI possible on hardware that would otherwise be too constrained. Without that kind of optimization, things get difficult fast.

## Ollama: local AI that feels like infrastructure

Ollama was the tool that clicked immediately.

```
ollama run gemma4:e4b
```

That simplicity changes your relationship with the whole thing. Instead of spending time managing files and configs, you spend time building. When you're working with FastAPI, Django, LangChain, or agent systems, Ollama starts feeling less like software and more like infrastructure you just trust to be there.

## What I'd actually run on my machine

Gemma 4 comes in four sizes: E2B, E4B, the 26B MoE model, and the 31B dense model. Given my hardware, the 26B and 31B variants are effectively off the table unless I want to tolerate heavy disk offloading and painful slowdowns. The E2B and E4B models are specifically designed for edge and on-device deployment, which makes them the realistic options here. Quantized versions where possible.  
My stack would look like this:

- Experimentation: LM Studio
- Application serving: Ollama
- Optimized inference: llama.cpp (when I need direct control)
- Fine-tuning experiments: Unsloth

## The RAM reality check

Can you install all four on a 16GB machine? Yes. Can you run them all simultaneously while hosting a model? No.  
Loading an LLM into RAM is exclusive. You can't have LM Studio and Ollama both holding a 6GB model in memory at the same time and still leave headroom for your OS and browser. The practical workflow is switching between them: experiment in LM Studio, shut it down, then serve via Ollama when you're building.

## What I actually took away from this

The most useful discovery wasn't which tool is best. It was realising that local AI is becoming less about raw hardware and more about the tooling around it. I am building an EdgeTutor for kids in rural classroom in South Africa. It is an application that helps teachers be able to help kids with tailored knowledge of their needs. Models like Gemma 4 makes this possible as they run on small computing resources.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbin6yjj2dvtll4c68v1c.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fbin6yjj2dvtll4c68v1c.png)

A few years ago, a machine like mine wouldn't really be part of the conversation. The smaller Gemma 4 models are specifically designed for efficient local execution on laptops and mobile devices, which means developers who aren't sitting on workstation hardware can genuinely participate now.  
Maybe not with the biggest models. But enough to build. And sometimes that is all you need.

[![Google article image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi6mj0yymgm9gmhlz7l4y.png)](https://dev.to/googleai/building-capabilities-for-a-multi-agent-system-with-google-adk-mcp-and-cloud-run-ab9?bb=263437)

## Building Capabilities for a Multi-Agent System with Google ADK, MCP, and Cloud Run

My team's mission is to accelerate the developer journey from writing code to running secure AI workloads on Google Cloud. To help developers succeed, we focus on identifying their most pressing questions and building demos that provide straightforward, easy-to-implement solutions.