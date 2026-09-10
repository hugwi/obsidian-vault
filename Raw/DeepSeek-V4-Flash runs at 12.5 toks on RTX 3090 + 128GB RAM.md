---
title: "DeepSeek-V4-Flash runs at 12.5 tok/s on RTX 3090 + 128GB RAM"
source: "https://theneuralfeed.com/article/deepseek-v4-flash-0731-ud-iq3-s-12-5-tok-s-on-rtx-3090-128gb-ddr5/oYeO7Xg4"
author:
  - "[[The Neural Feed]]"
published: 2026-08-02
created: 2026-09-10
description: "A 136GB model fits in 24GB VRAM with a clever llama.cpp flag—outputs a voxel scene."
tags:
  - "raw"
---
⚡A 136GB model fits in 24GB VRAM with a clever llama.cpp flag—outputs a voxel scene.

Deep Dive

A hardware enthusiast pulled off what many thought impossible: running DeepSeek-V4-Flash-0731, a Mixture-of-Experts model with a ~136GB footprint, on a single RTX 3090 24GB. The key was combining the GPU with 128GB of DDR5 overclocked to 5600MHz and a lesser-known llama.cpp flag. By adding --n-cpu-moe 39, the loader keeps 39 MoE expert layers in system RAM instead of VRAM, leaving only the attention layers and shared experts on the GPU. The result is a usable 12.5 tokens per second—not blazing fast, but fully interactive.

The setup wasn't trivial. The developer had to replace text-generation-webui's bundled llama.cpp binaries with the latest official release from the llama.cpp GitHub repo, then carefully configure 44 GPU layers, a massive 384,000-token context window, FP16 cache, and split-mode layer. They overclocked DDR5 via AMD EXPO to hit 5600MHz, as RAM bandwidth is the real bottleneck when most of the model lives off-GPU. As a demo, they prompted the model and got a fully rendered Voxel Japanese Pagoda Garden—an interactive 3D scene—proving the local inference can handle complex generation tasks, not just chat.

Key Points

- \--n-cpu-moe 39 offloads 39 MoE expert layers to system RAM, enabling a 136GB model on 24GB VRAM
- Achieved 12.5 tok/s on RTX 3090 + 128GB DDR5 @5600MHz, plus 384k token context
- Required swapping in latest llama.cpp binaries into text-generation-webui; model generated a voxel Japanese pagoda garden

### Why It Matters

Proves frontier-scale MoE models can run on consumer hardware, democratizing access to advanced local AI.