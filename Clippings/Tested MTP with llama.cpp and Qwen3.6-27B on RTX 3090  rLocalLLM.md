---
title: "Tested MTP with llama.cpp and Qwen3.6-27B on RTX 3090 : r/LocalLLM"
source: "https://www.reddit.com/r/LocalLLM/comments/1tf002j/tested_mtp_with_llamacpp_and_qwen3627b_on_rtx_3090/"
author:
  - "[[reddit.com]]"
published: 2026-05-16
created: 2026-07-13
description:
tags:
  - "clippings"
---
I have just compiled the new release of llama.cpp that includes MTP and tried it for agentic coding on my RTX 3090.

Model: Qwen3.6-27B-Q4\_K\_M

MTP config: --spec-type draft-mtp --spec-draft-n-max 2 --parallel 1

Without MTP: 100K context with mmproj enabled -> 21.5 GB VRAM usage

With MTP: 100K context with mmproj enabled -> 22.1 GB VRAM usage

Numeric results with llama-benchy:

- Without MTP: 1020 t/s for prompt processing and 42 t/s for token generation
- With MTP: 830 t/s for prompt processing and 60 t/s for token generation

Using MTP results in -18% t/s in prompt processing and +42% in token generation

I think MTP is a good improvement but is only usable if you currently (without MTP) have at least 2 GB of memory free. If your setup is memory constrained don't even try it.

EDIT:

Retried everything with a more conservative and adequate config (previously using --spec-draft-n-max 6)

---

## Comments

> **am17an** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om63ad0/) · 9 points
> 
> Follow the guidelines. -spec-draft-n-max 3 and -np 1
> 
> > **nunodonato** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om7qsa9/) · 2 points
> > 
> > Where are the guidelines?
> > 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6ck0w/) · 2 points
> > 
> > Retried with -np 1. Now it's usable on my config

> **sukazu** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om67821/) · 7 points
> 
> Personnally for me 4090 same amount of vram
> 
> The choices are:
> 
> No mtp about 172k ctx kv q8.
> 
> No mtp+ vision min token 2048 about 132k
> 
> MTP no vision 132k -np 1
> 
> I use all 3 depending on what i need
> 
> Maybe you are plugging your monitor to gpu? Saves about 1,5 to plug to motherboard
> 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6d5sd/) · 1 points
> > 
> > No monitor at all plugged to the machine (it’s just a server). How are you able to use that context size? Me with 120K I get OOMs occasionally
> > 
> > > **sukazu** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6nmpt/) · 1 points
> > > 
> > > Weird, but then again, it's not the same exact card
> > > 
> > > > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6q36a/) · 1 points
> > > > 
> > > > How much RAM do you have?
> > > > 
> > > > > **sukazu** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om753zd/) · 1 points
> > > > > 
> > > > > 9600x 32go ram  
> > > > > I run this for no mtp with vision  
> > > > > \-m "Qwen3.6-27B-UD-Q4\_K\_XL.gguf"
> > > > > 
> > > > > \-ngl 99 ^
> > > > > 
> > > > > \-c 131072 ^
> > > > > 
> > > > > \-ctk q8\_0 -ctv q8\_0 ^
> > > > > 
> > > > > \-fa on ^
> > > > > 
> > > > > \--mmproj "mmproj-BF16.gguf" ^
> > > > > 
> > > > > \--no-mmap ^
> > > > > 
> > > > > \--temp 0.6 ^
> > > > > 
> > > > > \--top-p 0.95 ^
> > > > > 
> > > > > \--top-k 20 ^
> > > > > 
> > > > > \--min-p 0.00 ^
> > > > > 
> > > > > \--presence-penalty 0.0 ^
> > > > > 
> > > > > \--repeat-penalty 1.0 ^
> > > > > 
> > > > > \--jinja ^
> > > > > 
> > > > > \--image-min-tokens 2048 ^
> > > > > 
> > > > > no vision, the same but -c 172032  
> > > > > and MTP -c 131072 --spec-draft-n-max 2 -np 1
> > > > > 
> > > > > **JustSayin\_thatuknow** · [2026-05-17](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/omdm2a4/) · 1 points
> > > > > 
> > > > > Even if you use -fa, are you sure that your flash attention is really being enabled?

> **Boricua-vet** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om61xl3/) · 6 points
> 
> I was confused, now I am more confused....
> 
> Previously without MTP and then Now without MTP.....
> 
> Are you criticizing the build or MTP for ram comsumption? Or did you made a typo and meant without MTP?
> 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6389y/) · 2 points
> > 
> > It's a typo. First without MTP and then with MTP.

> **yes\_i\_tried\_google** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om64d77/) · 5 points
> 
> Give this model a go. You may find it recovers your lost overhead
> 
> It’s mine and my daily driver. On 3090 Ti, up to 192k ctx q8/q8 kv
> 
> [https://huggingface.co/localweights/Qwen3.6-27B-MTP-IMAT-IQ4\_XS-Q8nextn-GGUF](https://huggingface.co/localweights/Qwen3.6-27B-MTP-IMAT-IQ4_XS-Q8nextn-GGUF)
> 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6ge2m/) · 2 points
> > 
> > How do you feel it's response quality in comparison to the Q4\_K\_M?
> > 
> > > **yes\_i\_tried\_google** · [2026-05-17](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/oma72o2/) · 2 points
> > > 
> > > Haven’t noticed any regression at all. Feels like a free like-for-like swap for my workflow, for 3GB less memory

> **LORD\_CMDR\_INTERNET** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om64hol/) · 5 points
> 
> For me on a 5090, the slowest part of using Qwen3.6 27B was never tokens per second, it was prompt processing, which now takes MUCH longer. I was looking forward to MTP but overall using the model is *slower* for me now because of this so I disabled MTP.
> 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6bdto/) · 1 points
> > 
> > I have just done the numeric tests and for me it results in -18% in PP and +42% in TG
> > 
> > > **LORD\_CMDR\_INTERNET** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6d9zs/) · 1 points
> > > 
> > > percentages don't really mean anything though, it's the total time lost/gained that matters. also tokens generated varies by task quite a bit but prompt processing is more constant, so longer PP times mean MUCH longer overall workflow times. the impact might also be worse on a 5090 since token generation speed was pretty good already

> **urarthur** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6dfu3/) · 3 points
> 
> why would you enable mmproj for coding? I am running unsloth qwen3.6 26b q4 xl mtp model with 200k context at 50-60 tg/s. kv=q4. Also on 3090
> 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6dvm3/) · 1 points
> > 
> > Because sometimes I use the web ui and i have it enabled in case I need to process an image, but I think for that few cases I can just use ChatGPT
> > 
> > > **imgroot9** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6lvyd/) · 6 points
> > > 
> > > you can offload mmproj to cpu. it is fast and you get 1 gb free

> **DiscipleofDeceit666** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om62wm6/) · 2 points
> 
> I barely have more memory than you with my setup and I saw meaningful speed improvements.
> 
> 28 Gb VRAM across 2 RDNA 2 cards 6800 and 6700XT. MTP makes AI viable for the common folk. I should mention that I have the spec draft count set to 2 tokens.
> 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om63t3j/) · 2 points
> > 
> > If I had 28 GB I would use MTP without thinking about it. That extra 4 GB removes the memory constraint that I have

> **EbbNorth7735** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om65lu9/) · 2 points
> 
> Did you try setting kv to Q8?
> 
> > **JGeek00** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om65u8d/) · 2 points
> > 
> > I always used q8. There’s no way to fit that large context on that GPU without compressing the kv cache
> > 
> > > **JustSayin\_thatuknow** · [2026-05-17](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/omdmfar/) · 1 points
> > > 
> > > Check flash attention and check if RAM modules are running in double-channel or higher..

> **SGkhIDop** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om70eaj/) · 2 points
> 
> I have tested on 7900 XTX. The same model Qwen3.6-27B-Q4\_K\_M. Ubuntu without gui.
> 
> MTP config: --spec-type draft-mtp --spec-draft-n-max 2 --parallel 1
> 
> Without MTP: ~35t/s
> 
> With MTP: ~65t/s
> 
> Tested on the same prompt with logic puzzle. It keeps thinking for over 10k tokens, so speed is more or less real. Results are amazing!

> **caetydid** · [2026-05-16](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/om6t7bk/) · 1 points
> 
> rly looking fwd to see how MTP will benefit Gemma4

> **alexpolo3** · [2026-05-17](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/omagffq/) · 1 points
> 
> Check this out [https://github.com/noonghunna/club-3090](https://github.com/noonghunna/club-3090), [https://discord.gg/U3hDB8GAE](https://discord.gg/U3hDB8GAE)

> **Brilliant\_Anxiety\_36** · [2026-05-17](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/ombjl24/) · 1 points
> 
> Can this be combined with turboquant?

> **zkkzkk32312** · [2026-05-19](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/omlqn4t/) · 1 points
> 
> What's your KV quants at? Q8?
> 
> > **JGeek00** · [2026-05-19](https://reddit.com/r/LocalLLM/comments/1tf002j/comment/ommlag7/) · 1 points
> > 
> > Yes