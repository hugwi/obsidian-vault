# Two old GPUs I salvaged are doing more AI work than a brand new $2000 card, and I won't be upgrading anytime soon

![rw-book-cover](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/vs-code-llama-6.jpg?w=1600&h=900&fit=crop)

## Metadata
- Author: [[Ayush Pande]]
- Full Title: Two old GPUs I salvaged are doing more AI work than a brand new $2000 card, and I won't be upgrading anytime soon
- Category: #articles
- Summary: The author uses two old GPUs, an RTX 3080 Ti and a GTX 1080, to run powerful AI models locally without needing the newest expensive cards. They rely on special model designs that use less VRAM and can share work between the GPU and CPU. Running these AI tasks on older hardware saves energy and still delivers good performance for coding, image editing, and other AI workflows.
- URL: https://www.xda-developers.com/two-old-gpus-are-doing-more-ai-work-than-a-brand-new-card/

## Full Document
![Running queries in llama-vscode](https://static0.xdaimages.com/wordpress/wp-content/uploads/wm/2026/05/vs-code-llama-6.jpg?&fit=crop&w=1600&h=900)
Despite the productivity-oriented perks of large language models, there’s the misconception that local LLMs need a lot of computational horsepower to run. Well, it’s true to some extent, as you’ll need a decent amount of VRAM to run self-hosted AI models. Not to mention, conventional LLMs also require a fast GPU, or you’d end up with abysmally slow generation rates.

But contrary to what you might think, you don’t need a top-of-the-line card just to run bulky LLMs – and it’s something I learned after building a completely local AI pipeline with outdated GPUs that are technically unfit for hosting heavy models.

####  My RTX 3080 Ti tackles the demanding AI-hosting tasks

#####  It’s primarily responsible for running Qwen 3.6 (35B) for my coding tasks

The RTX 3080 Ti used to be quite the powerhouse back in the day, but its 12GB of VRAM is a bit of a problem for bulky models. After all, 7B-9B models are the only sweet spot for this much VRAM, and I'd have to tinker with the quantization rates if I wanted to go up to 14B models. But this limitation only applies to conventional LLMs, not Mixture-of-Experts models. Rather than relying on the entire model to process prompts like conventional LLMs, MoE clankers use a router + experts architecture to massively reduce the amount of VRAM needed for inference. You see, the router transfers the input to specific experts, and these independent neural networks specialize in specific workloads.

So, I can add the *--n-cpu-moe* flag to my llama.cpp commands to offload the lesser-used MoE layers to my CPU and RAM, while the attention mechanisms and router weights run on my GPU’s VRAM. And well, it’s thanks to this game-changing architecture that I can run something as bulky as [Qwen3.6-35B-A3B on my 5-year-old RTX 3080 Ti](https://www.xda-developers.com/i-replaced-chatgpt-and-claude-with-this-local-llm/) at a token generation rate of 24 t/s!

For reference, I use llama.cpp to host this LLM on my Windows system, which has a mere Ryzen 5 5600x CPU and 32GB of DDR4 RAM. And even with the king of bloated operating systems, I still have some RAM to spare for other applications like VS Code. While we’re on this subject, I primarily use my Qwen3.6-35B-A3B as a programming companion for VS Code via the llama-vscode extension. And having used it for everything from troubleshooting log files and inspecting repos for security flaws to reformatting YAML/JSON files and refactoring Python functions, I can confirm that it can trade blows with cloud-based models. I’ve even started using it with the agent harness Pi, and it’s just as impressive at creating plugins and executing complex commands using said plugins.

#####  But it’s just as useful for my AI-powered Krita + ComfyUI workflows

When you think about AI-powered tasks, you’d typically imagine LLM pipelines. But I also use image-centric models on my RTX 3080 Ti, and despite the general sentiment about AI-generated images, certain ComfyUI workflows are surprisingly useful. For example, I’ve been using 4xNomos8kDAT to upscale old low-resolution images, and it works exceedingly well for decade-old photos.

Heck, local image models can even replace Adobe’s generative fill tools, and it’s something I only realized after running the krita-ai-diffusion and krita-vision-tools plugins. On the performance front, they usually take a minute or two to process my prompts with the RTX 3080 Ti. Even if the first attempt results in less-than-satisfactory results sometimes, the wackiness of the image models goes away once I regenerate the output 2–3 times. I’ve been using them for prototyping poses, removing backgrounds, and minor edits for a few weeks, and as long as I don’t go too vague with my prompts, [Krita’s AI plugins](https://www.xda-developers.com/kritas-ai-plugins-do-what-photoshop-charges-120-a-year-for/) are surprisingly useful for manipulating images.

####  My aged GTX 1080 runs LLMs for the rest of my self-hosted FOSS stack

#####  Half of my productivity suite relies on this 10-year-old GPU

Since I use my RTX 3080 Ti on my gaming machine, I can’t keep it engaged in LLM processing tasks 24/7. In fact, I even shut down the llama-server hosting Qwen3.6-35B-A3B when I need to edit images with Krita. So, it’s not something I can use with tools like Home Assistant’s AI plugins that I’d rather keep running around the clock. Instead, my GTX 1080 hosts the embedding, TTS/STT, and MoE LLMs for the rest of my containerized services. And as unhinged as it may sound, this decade-old graphics card is a hidden gem for LLM processing tasks, even though it has zero tensor cores whatsoever.

 [![XDA logo](https://static0.xdaimages.com/assets/images/xda-logo-full-colored-light.svg?v=3.6)  Deals](https://www.xda-developers.com/deals/) 

##### Deals on PCs, GPUs, RAM and workstation gear

Grab discounts and limited-time offers on desktops, GPUs, RAM, SSDs, cooling, and networking gear to power local AI workloads—browse Computers & Work Setup deals to upgrade your workstation, cut costs, and squeeze more performance per dollar.

 [![XDA logo](https://static0.xdaimages.com/assets/images/xda-logo-full-colored-light.svg?v=3.6)  Deals](https://www.xda-developers.com/deals/)   [Explore Computers & Work Setup Deals](https://www.xda-developers.com/deals/category/computers-work-setup/) 

Again, I can thank the MoE architecture for breathing new life into my GTX 1080. Although I don’t use it to run Qwen3.6-35B-A3B, the 8GB of VRAM on the GPU + 32GB of DDR4 memory is plenty for [Gemma-4-26B-A4B](https://www.xda-developers.com/i-built-a-local-llm-workflow-that-runs-on-my-10-year-old-gpu/). I’ve paired it with an equally aged Ryzen 5 1600 processor that runs Proxmox, with llama.cpp configured as the LXC. The token generation speed is obviously lower than my RTX 3080 Ti, but getting 14 t/s isn’t bad by any means. I’ve got it hooked up to [Blinko](https://www.xda-developers.com/i-dont-use-obsidian-or-google-keep-after-i-came-across-this-note-taker/), [Karakeep](https://www.xda-developers.com/this-self-hosted-bookmark-manager-uses-my-local-llms/), Home Assistant, [Open Notebook](https://www.xda-developers.com/switched-from-notebooklm-to-open-source-tool-open-notebook/), [Open WebUI](https://www.xda-developers.com/i-built-the-central-ai-hub-ive-been-wanting-and-open-webui-made-it-simple/), and my [Paperless-ngx pipeline](https://www.xda-developers.com/i-use-local-llms-and-self-hosted-apps-to-manage-my-documents/). I also use this GPU to run nomic-embed-text as the embedding model, and a Speaches container hosts Kokoro-82M-v1.0-ONNX for STT tasks and faster-whisper-small for my TTS needs.

#####  Local LLMs need a lot less energy than you’d think

Before I’d started hosting my own AI models, I was afraid that they’d spike my electricity bills. Fortunately, unlike the LLM training operations that consume thousands of watts worth of power, simple inference tasks trigger my GPUs in short bursts. So, even if I keep the LXCs hosting AI models 24/7, they’d remain idle most of the time and activate my graphics card for a few minutes at most when I trigger an AI-heavy workload.
