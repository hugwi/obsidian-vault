# Don’t buy GPUs for AI

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1400/0*9vvpIDkyLf9gfefT)

## Metadata
- Author: [[Mehul Gupta]]
- Full Title: Don’t buy GPUs for AI
- Category: #articles
- Summary: You don’t need to buy expensive GPUs for most AI tasks because smaller models run well on CPUs and edge devices. Renting cloud GPUs or using specialized chips is cheaper and more efficient than owning hardware. In the future, AI will mostly run on software and serverless platforms, making GPUs less important for most users.
- URL: https://medium.com/data-science-in-your-pocket/dont-buy-gpus-for-ai-65740b91d549

## Full Document
###### Why you won’t require GPUs in the future

![](https://miro.medium.com/v2/resize:fit:1400/0*9vvpIDkyLf9gfefT)Photo by [Andrey Matveev](https://unsplash.com/@zelebb?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)GPUs have become the shiny toy of AI. Everyone wants them: startups flaunt their GPU counts, researchers tweet about clusters, hobbyists justify blowing two salaries on a 4090. It feels like the only way to “do AI” is to hoard silicon.

> My new book on AI Agents is out
> 
> 

![](https://miro.medium.com/v2/resize:fit:320/0*L8TCupzNMvFkXyfK)[Model Context Protocol: Advanced AI Agents for Beginners (Generative AI books)](https://www.amazon.com/gp/product/B0FCCF348X)Amazon.com: Model Context Protocol: Advanced AI Agents for Beginners (Generative AI books) eBook : Gupta, Mehul, Sen…www.amazon.comBut that mindset is already outdated. Unless you’re one of the 10 companies training models with billions of parameters, odds are you don’t need a GPU.

###### Here’s why

##### Small LLMs are eating the big guys

OpenAI and Anthropic make the headlines with 70B or 400B parameter giants. But in practice? The most useful tools right now are smaller: Mistral 7B, Phi-3 Mini (3.8B), LLaMA-3 8B.

> ***Example:*** Phi-3 Mini runs on a CPU and still beats larger models on reasoning benchmarks. People have it running on Raspberry Pi-like boards. Why invest in GPUs when the “lightweight” models already deliver?
> 
> 

##### “Good enough” AI solves 90% of tasks

> Most companies don’t need perfection, they need *practical*.
> 
> 

Summarizing customer support chats. Generating boilerplate SQL. Drafting HR emails. These don’t require GPT-4 class intelligence.

> ***Example:*** a logistics firm swapped GPT-4 for a 7B distilled model to generate route summaries. Accuracy dropped a tiny bit, but inference costs fell by 20×. No GPU needed.
> 
> 

##### CPUs are making a comeback

Modern CPUs with quantized models can already do inference at decent speeds. Intel’s latest chips (with AMX extensions) and Apple’s M-series processors run models locally without touching a GPU.

> ***Example:*** Apple’s MLX framework runs LLaMA-3 8B on an M2 MacBook Air. It’s not instant, but for many tasks it’s perfectly usable.
> 
> 

##### 4. Edge devices are already AI-ready

You don’t need a GPU when your phone or tablet has its own Neural Processing Unit (NPU). Samsung, Apple, Qualcomm, all baking dedicated AI accelerators right into the hardware.

> **Example:** iPhone 15 runs on-device transcription and summarization with Whisper-like models. No external GPU.
> 
> 

##### 5. Renting beats owning

GPUs are expensive, hard to source, and depreciate faster than cars. Even if you need heavy compute once in a while, renting cloud GPUs (AWS, Lambda Labs, CoreWeave) is cheaper.

> **Example:** a startup training a domain-specific 13B model rented A100s for two weeks instead of buying $200k worth of GPUs. Training done, GPUs returned, costs capped.
> 
> 

##### Specialized hardware will eat GPUs

Google has TPUs. Amazon is pushing Trainium and Inferentia. Every cloud provider wants you off NVIDIA. These chips are optimized for LLM workloads and will undercut GPUs in price/performance.

> **Example**: AWS Inferentia2 already runs LLaMA models at lower cost per token than A100s. GPUs aren’t the long-term default.
> 
> 

##### Software > hardware

Every month, new efficiency tricks make models faster without new hardware. Quantization (4-bit), FlashAttention, speculative decoding, DoRA, LoRA. Software is bending the rules of compute.

> **Example:** 4-bit quantization lets LLaMA-13B run on a single consumer CPU with 16GB RAM. That would’ve been unthinkable two years ago.
> 
> 

##### The resale market is brutal

GPUs don’t hold value. AI evolves too fast. By the time you think you’ve future-proofed, a cheaper and better chip is out.

> **Example:** the RTX 3090 launched at $1,499 in 2020. Today it sells second-hand for less than $500. AI workloads made it obsolete fast.
> 
> 

##### Energy costs matter more than hype

Running GPUs 24/7 isn’t just expensive to buy, it’s expensive to *power*. Cooling, electricity, maintenance. Those costs quietly kill many GPU-based side projects.

> **Example:** one indie dev running Stable Diffusion on a 4090 found their power bill jumped by 25%. Renting cloud GPUs for bursts would’ve been cheaper.
> 
> 

##### The future is serverless AI

Inference APIs and serverless frameworks mean you won’t even think about hardware. You’ll call an endpoint, get results, and never care whether it ran on a GPU, TPU, or ASIC.

> **Example:** Fireworks.ai or Replicate already let you run fine-tuned LLaMAs with an HTTP call. Zero GPUs on your end.
> 
> 

##### Bottom line

GPUs are peaking. They’re useful if you’re OpenAI, Anthropic, or DeepMind. For everyone else? They’re a distraction, a money sink, and soon, a relic.

Small LLMs, optimized software, and specialized chips will cover 99% of use cases. Renting covers the rest. So before you sink thousands into a 4090 or start begging NVIDIA for supply, ask yourself a blunt question:

> Do you really need a GPU? Or do you just want one because it looks like the “real AI thing”?
> 
> 

> Chances are: you don’t.
> 
>
