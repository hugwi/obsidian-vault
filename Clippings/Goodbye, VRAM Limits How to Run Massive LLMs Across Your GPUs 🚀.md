---
categories:
  - "[[Clippings]]"
domain: [ai-agents]
tags:
  - models
source: readwise
created: 2026-06-23
rating: 
action: 
---

# Goodbye, VRAM Limits: How to Run Massive LLMs Across Your GPUs 🚀

![rw-book-cover](https://freedium-mirror.cfd/apple-touch-icon.png)

## Metadata
- Author: [[Saman Chitsazian]]
- Full Title: Goodbye, VRAM Limits: How to Run Massive LLMs Across Your GPUs 🚀
- Category: #articles
- Summary: Ollama lets you run huge AI models by splitting them across multiple GPUs instead of just one. This stops slowdowns caused by using the CPU and makes the model run faster. You simply create a Modelfile to tell Ollama how many GPUs to use, and it handles the rest automatically.
- URL: https://freedium-mirror.cfd/https://medium.com/@samanch70/goodbye-vram-limits-how-to-run-massive-llms-across-your-gpus-b2636f6ae6cf

## Full Document
![Post cover image](https://freedium-mirror.cfd/img/700/1*XHSDBJIlabphE7exeAp_2Q.png)Post cover image
##### Stop offloading to your CPU. It's time to unleash the full parallel power of your rig for massive local LLMs.

The pace of AI is relentless. We've barely finished exploring the capabilities of Llama 3, and already the community is buzzing about what comes next. Imagine a model like "Llama 4: Maverick" — a hypothetical, ultra-capable model that pushes the VRAM limits of even the beefiest consumer GPUs.

Running a 70B model on a single 24GB card is already a stretch. So how can a developer or enthusiast hope to run a future 100B+ parameter model locally? The answer isn't necessarily a single, prohibitively expensive NVIDIA H100. The answer is likely already in your machine: multiple GPUs.

Thanks to the elegant simplicity of **Ollama**, harnessing the combined power of two, three, or even four GPUs to run a single, massive model is easier than you think. Let's explore how to achieve true model parallelism.

##### Why Ollama is a Game-Changer

If you're not yet familiar with it, [Ollama](https://ollama.com/) is a powerful tool that streamlines running open-source LLMs locally. It packages everything you need — model weights, configuration, and a server — into a simple, all-in-one experience. What used to be a complex process of wrangling Python dependencies and CUDA versions now boils down to a single command:

Its true power, however, lies in its flexible and straightforward configuration.

##### The Core Concept: Splitting the Load with a `Modelfile`

By default, when Ollama loads a model, it tries to fit all the model's layers onto a single GPU. If the model is too big, it places as many layers as it can on `gpu0` and then offloads the rest to your system's RAM, relying on the CPU to process them. This CPU offloading is a major bottleneck and leads to painfully slow inference speeds.

The solution is to tell Ollama to explicitly distribute the layers across *all* available GPUs. This is achieved using a custom configuration file called a `Modelfile`.

The `Modelfile` is a plain text recipe that tells Ollama how to build or modify a model. To enable multi-GPU support, we only need two key instructions:

1. `FROM`: This specifies the base model we want to use from the Ollama library.
2. `PARAMETER num_gpu`: This is the magic instruction. It tells Ollama how many layers of the model to offload to the GPU(s).

You might think you need to calculate the perfect number of layers per GPU, but Ollama is smarter than that. By setting `num_gpu` to a very high number (e.g., `999`), you essentially tell Ollama: "Use all the GPU power you can find. Distribute the layers across all available GPUs as efficiently as possible."

Here's what the `Modelfile` looks like to create a multi-GPU version of a hypothetical `llama4:maverick` model.

Ollama will then handle the complex task of splitting the model's tensor layers evenly. With two identical GPUs, it will put roughly 50% of the layers on the first GPU and 50% on the second.

##### Practical Walkthrough: Building and Running Your Multi-GPU Model

Let's turn theory into practice. Assume you have a model named `llama4:maverick` available in your Ollama library.

###### Step 1: Create the `Modelfile`

In an empty directory, create a new file named `Modelfile` (no file extension) and add the two lines of configuration from the example above.

###### Step 2: Create the New Model Version

Open your terminal in the same directory as your `Modelfile`. Use the `ollama create` command to build a new, multi-GPU-enabled version of the model. We'll give it a descriptive name like `llama4:maverick-multi`.

Ollama will instantly create a new model entry that inherits from `llama4:maverick` but applies your new `PARAMETER` setting.

###### Step 3: Run the Parallelized Model

You can now run your powerful new model with the standard `run` command.

```
ollama run llama4:maverick-multi
```

When Ollama starts, it will detect all your GPUs and begin loading the model layers, distributing them across each card's VRAM.

##### Verification: Is It Actually Working?

Don't just take our word for it — verify it! While the model is loading or running, open another terminal and use your system's GPU monitoring tool.

* **For NVIDIA GPUs:** `watch -n 1 nvidia-smi`
* **For AMD GPUs:** `watch -n 1 rocm-smi`

   ![None](https://freedium-mirror.cfd/img/700/1*XmVWyzj0uNKzz8C0gNzmWw.png) 
The `watch` command will refresh the stats every second. You should see two key indicators:

* **VRAM Usage:** Both (or all) of your GPUs will show significant VRAM being consumed. This is the model being loaded onto each card.
* **GPU Utilization:** As you send prompts to the model, you should see the `GPU-Util` percentage spike on all cards simultaneously.

If you see activity across multiple GPUs, you've done it! You are now running a single, massive LLM in parallel. Congratulations, you've unlocked a new level of local AI capability. 🚀

Sources:

* Advanced Micro Devices, Inc. (2025). *ROCm System Management Interface (rocm-smi)*. AMD ROCm™ Documentation. Retrieved July 16, 2025, from [https://rocm.docs.amd.com/en/latest/tools/rocm-smi.html](https://www.google.com/search?q=https://rocm.docs.amd.com/en/latest/tools/rocm-smi.html)
* Gerganov, G., et al. (2023). *GGUF File Format Documentation*. GGML Repository on GitHub. Retrieved July 16, 2025, from [https://github.com/ggerganov/ggml/blob/master/docs/gguf.md](https://www.google.com/search?q=https://github.com/ggerganov/ggml/blob/master/docs/gguf.md)
