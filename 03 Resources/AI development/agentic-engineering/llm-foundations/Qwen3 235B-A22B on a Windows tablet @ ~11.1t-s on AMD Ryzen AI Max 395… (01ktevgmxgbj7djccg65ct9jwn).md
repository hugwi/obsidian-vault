---
title: "Qwen3 235B-A22B on a Windows tablet @ ~11.1t/s on AMD Ryzen AI Max 395+ 128GB"
source: "https://www.reddit.com/r/LocalLLaMA/comments/1kd5rua/qwen3_235ba22b_on_a_windows_tablet_111ts_on_amd/"
author: "Invuska"
published: 2025-05-02
created: 2026-06-06
description: "The fact you can run the full 235B-A33B model fully in iGPU without CPU offload,"
tags:
  - to-process
  - llm-foundations
---

**[r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)**


# [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 16:49:48)


The fact you can run the full 235B-A33B model fully in iGPU without CPU offload, on a portable machine, at a reasonable token speed is nuts! (Yes, I know Apple M-series can probably also do this too, lol). This is using the Vulkan backend; ROCm is only supported on Linux, but you can get it to work on this device if you decide to go that route and you self-compile llama.cpp


This is all with the caveat that I'm using an aggressive quant, using Q2\_K\_XL with Unsloth Dynamic 2.0 quantization.


Leaving the LLM on leaves ~30GB RAM left over (I had VS Code, OBS, and a few Chrome tabs open), and CPU usage stays completely unused with the GPU taking over all LLM compute needs. Feels very usable to be able to do work while doing LLM inference on the side, without the LLM completely taking your entire machine over.


Weakness of AMD Strix Halo for LLMs, despite 'on-die' memory like Apple M-series, is that memory bandwidth is still very slow in comparison (M4 Max @ 546Gb/s, Ryzen 395+ @ 256Gb/s). Strix Halo products do undercut Macbooks with similar RAM size in price brand-new (~$2800 for a Flow Z13 Tablet with 128GB RAM).


This is my llama.cpp params (same params used for LM Studio):  

`-m Qwen3-235B-A22B-UD-Q2\_K\_XL-00001-of-00002.gguf -c 12288 --batch-size 320 -ngl 95 --temp 0.6 --top-k 20 --top-p .95 --min-p 0 --repeat-penalty 1.2 --no-mmap --jinja --chat-template-file ./qwen3-workaround.jinja`. 


`--batch-size 320` is important for Vulkan inference due to a bug outlined here: <https://github.com/ggml-org/llama.cpp/issues/13164>, you need to set evaluation batch size under 365 or you will get a model crash.





## [sourceholder](https://www.reddit.com/user/sourceholder/)



 (2025-05-02 17:11:38)


A Windows **tablet** running a 235B model at this speed is insane.





### [offlinesir](https://www.reddit.com/user/offlinesir/)



 (2025-05-02 17:17:34)


well, it's a really powerful windows "tablet" specifically the Asus Z 13 (I'm assuming) which is close to $2000. It's in a similar look to a Microsoft Surface Device.





#### [fallingdowndizzyvr](https://www.reddit.com/user/fallingdowndizzyvr/)



 (2025-05-02 18:07:30)



> 
> the Asus Z 13 (I'm assuming) which is close to $2000.
> 
> 
> 


That's the cheap model with only 32GB. This is the 128GB model, it costs way more than that.





##### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 18:22:14)


Yep. For people wondering (sorry that I didn't make this more clear in the post) I'm using a ROG Flow Z13. I paid $2800 before tax and shipping.





###### [658016796](https://www.reddit.com/user/658016796/)



 (2025-05-02 20:32:17)


Where did you buy the model 128GB model? I've been searching for weeks for it, and I can only find the 32GB one.





###### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 20:45:20)


I pre-ordered on Asus' website basically within the hour it first became available on the eStore a few months ago, sorry :( Yeah, I've heard it's been quite rough.





###### [lochyw](https://www.reddit.com/user/lochyw/)



 (2025-05-03 00:28:38)


why do americans always mention before tax pricing. everyone pays tax so that price is irrelevant.. ? include the tax in your prices people :P





###### [offlinesir](https://www.reddit.com/user/offlinesir/)



 (2025-05-03 00:59:38)


Sales taxes aren't a baseline price across all of the US. Some states have a sales tax of 0, while others have it at 9.5 percent! It's usually in the 6-8 percent though.





###### [PermanentLiminality](https://www.reddit.com/user/PermanentLiminality/)



 (2025-05-03 03:48:16)


You forgot about California. It can be 10.25% here.





###### [sassydodo](https://www.reddit.com/user/sassydodo/)



 (2025-05-03 07:36:32)


So how is it, from UX side? Is it uncomfortably thick, how about the weight? Thinking about replacing my daily driver ultrabook with something that can be used both at home and for office needs





##### [ketchupadmirer](https://www.reddit.com/user/ketchupadmirer/)



 (2025-05-03 04:21:16)


There are tablets with 128 gb of ram? Outside of LLM enthusiasts (apparently), who the f buys them, and what do they do





###### [cangaroo\_hamam](https://www.reddit.com/user/cangaroo_hamam/)



 (2025-05-03 05:24:09)


This is actually a very powerful PC, in the form of a (thick) tablet. It's not a typical tablet.





###### [fallingdowndizzyvr](https://www.reddit.com/user/fallingdowndizzyvr/)



 (2025-05-03 06:34:15)


There are now. Remember when it was silly that tablets had 16GB. Why does a tablet need 16GB? What a waste. Now it's a tablet only has 16GB? What's the point?


It's a chicken and an egg situation. You have to have 128GB first, then people will figure out what to do with it.





###### [ketchupadmirer](https://www.reddit.com/user/ketchupadmirer/)



 (2025-05-03 06:37:02)


yeah, you are right, good point, just from my consumer POV, if I want that much firepower, I want a desktop, but that is just me





### [Semi\_Tech](https://www.reddit.com/user/Semi_Tech/)



 (2025-05-03 08:47:33)


Kind of a sad state that AI inferencing is more capable on a tablet than the 9070.


Anyways, glad it works for OP.





#### [MMAgeezer](https://www.reddit.com/user/MMAgeezer/)



 (2025-05-03 10:55:45)


Is it? You could always get better speeds from a reasonably sized MOE that fits into your RAM vs. a dense model that fits into your VRAM.





## [danielhanchen](https://www.reddit.com/user/danielhanchen/)



 (2025-05-02 17:01:35)


Super cool! :)





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 17:06:33)


Big thanks for all your hard work at Unsloth! 🙇





#### [danielhanchen](https://www.reddit.com/user/danielhanchen/)



 (2025-05-02 17:07:51)


Thank you!





##### [kor34l](https://www.reddit.com/user/kor34l/)



 (2025-05-02 21:02:57)


Yes! Y'all kick ass, I always check unsloth first for Quantized GGUFs of new models.


Then I go find someone that took your GGUF and Abliterated it, because I get unreasonably upset when I have to sit around and argue with my AI assistant to get it to play a damn song because it doesn't like the name of the song.


Ugh I hate that. Like, AI buddy, I promise nothing bad will happen if you play "Fuck The World" by ICP like I asked you to.


I prefer my AI to do what I tell it to do and leave the moral and ethical considerations to me, the person that actually understands them.





## [qualverse](https://www.reddit.com/user/qualverse/)



 (2025-05-02 17:58:08)


ROCm works actually with a few tweaks! Just follow the instructions from [this repo](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU), including their [LM Studio guide](https://github.com/likelovewant/ROCmLibs-for-gfx1103-AMD780M-APU/wiki/Unlock-LM-Studio-on-Any-AMD-GPU-with-ROCm-Guide). Also you might need to increase the Windows pagefile size. With these changes LM Studio is working great on ROCm.





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 18:20:25)


Oh man, this is really cool. I'll need to dig into this - thanks for sharing!





#### [jwingy](https://www.reddit.com/user/jwingy/)



 (2025-05-02 18:42:33)


If you get ROCm working would you mind updating the post if the speed improves? Thanks!





##### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 18:45:52)


Sure thing, will let you know :)





### [TSG-AYAN](https://www.reddit.com/user/TSG-AYAN/)



 (2025-05-02 21:16:15)


Is ROCm actually faster on windows than vulkan? I get much better performance on tg ~50% on linux with vulkan than rocm, which has faster processing but slower inference.





#### [qualverse](https://www.reddit.com/user/qualverse/)



 (2025-05-02 22:41:13)


In the specific case of the Qwen3 MoE models it does seem like Vulkan is faster, but this isn't the case with other models I've tried.





##### [randomfoo2](https://www.reddit.com/user/randomfoo2/)



 (2025-05-03 04:53:58)


In my testing on Linux, Vulkan is faster on all the architectures I've tested so far: Llama 2, Llama 3, Llama 4, Qwen 3, Qwen 3 MoE.


There is a known gfx1151 bug that may be causing bad perf for ROCm: <https://github.com/ROCm/MIOpen/pull/3685>


Also, I don't have a working hipBLASlt on my current setup.


(If I HSA\_OVERRIDE to gfx1100 I can get a mamf\_finder max of 25 TFLOPS vs 5 TFLOPS but it'll crash a few hours in. mamf-finder runs for gfx1151 but uh, takes over 1 day to run and the perf 10-20% of what it should be from hardware specs).





### [Historical-Camera972](https://www.reddit.com/user/Historical-Camera972/)



 (2025-05-03 17:23:45)


ROCm should work without tweaks, but I guess AMD's dev team has better things to work on than optimization for the one utility that's making their AI products sell like hot cakes.


Does Dr. Lisa Su even know the ROCm support compatibility is abysmal at official levels?





#### [05032-MendicantBias](https://www.reddit.com/user/05032-MendicantBias/)



 (2025-05-04 07:38:35)


Lots of work is going into DirectML and ONNX support. Last I checked AMD didn't even bother to add ROCm support to the 9070 XT.


I really, REALLY wish AMD picked one stack. ONE STACK. and made it work flawlessly.


Just like you have one adrenaline driver, not five different drivers none of which works well.





### [05032-MendicantBias](https://www.reddit.com/user/05032-MendicantBias/)



 (2025-05-04 07:36:43)


I'm going to try it! I am running lots of LLMs on my 7640u framework 13.





## [fallingdowndizzyvr](https://www.reddit.com/user/fallingdowndizzyvr/)



 (2025-05-02 18:05:06)



> 
> Weakness of AMD Strix Halo for LLMs, despite 'on-die' memory like Apple M-series, is that memory bandwidth is still very slow in comparison (M4 Max @ 546Gb/s, Ryzen 395+ @ 256Gb/s). 
> 
> 
> 


You're comparing it to the wrong M4. It's a M4 Pro competitor, not M4 Max. It's memory bandwidth is the same as the M4 Pro.





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 19:07:08)


Oops, good to know; thanks





## [bennmann](https://www.reddit.com/user/bennmann/)



 (2025-05-02 17:24:25)


Will you please attempt setting your batch size to intervals of 64 and retest prompt processing speeds at each one?


ie --batch-size 64, --batch-size 256


i suspect there is a small model perplexity loss for these settings too, but perhaps the tradeoffs are worth it.





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 18:19:07)


Sure, quickly did 64, 256, and 320 (64 \* 5). May do more comprehensive testing/longer prompt when I get time later.


Prompt is 3 messages (user, model, user) at 1618 prompt tokens total:


* BS = 64: 48.62s time to first token
* BS = 256: 45.24s
* BS = 320: 49.09s (surprisingly the slowest)





#### [FullstackSensei](https://www.reddit.com/user/FullstackSensei/)



 (2025-05-02 20:31:19)


The 8060s has 2560 double-pumped shading units(think of them as 5120). That's evenly divisible by 256 but not by 320. Generally speaking you want to stick to powers of 2 to avoid partially occupied compute units.





##### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 20:35:40)


Ah, makes sense, thanks for the info!





## [tinbtb](https://www.reddit.com/user/tinbtb/)



 (2025-05-02 18:43:10)


Is q2 any good? It'd be interesting to see how it compares to 30B with less aggressive quantisation on the same platform. The performance would definitely be improved.





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-05-02 18:54:41)


Now use AMD QUARK followed up by GAIA-CLI to convert it for hybrid execution using CPU+iGPU+NPU on 395 😀





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-05-02 20:18:29)


Windows tablet with 128gb of ram is crazy





## [TacGibs](https://www.reddit.com/user/TacGibs/)



 (2025-05-02 20:54:18)


Pretty sure that the 32B would be better and not much slower at the end (prompt processing speed must be absolutely awful with the 235B).


Q2 is destroying the model.





### [a\_beautiful\_rhind](https://www.reddit.com/user/a_beautiful_rhind/)



 (2025-05-02 22:10:33)


These funky quants on large enough models are surprisingly usable.





## [Thomas-Lore](https://www.reddit.com/user/Thomas-Lore/)



 (2025-05-02 18:05:52)


What is the speed on CPU only, for comparison?





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 22:08:46)


Same prompt, params (CPU thread pool size 16/16, 395+ having 16 physical cores), and Turbo mode:


* CPU only: 4.69 tokens/sec for 1079 tokens
* 64/94 layers GPU, rest CPU (for fun): 7.07 tokens/sec for 1123 tokens





## [ThisNameWasUnused](https://www.reddit.com/user/ThisNameWasUnused/)



 (2025-05-02 18:33:37)


I have the same Z13 tablet, but I'm unable to to have it use any of the 'Shared GPU memory'. The model just crashes in LM Studio.  

It uses the 64GB VRAM set, but once the model reaches to this load point, it just crashes and unloads. It should seep into the system RAM available once the VRAM has been filled, but it's not doing that on my system.


Did you set the 64GB VRAM allocation within the Adrenalin software and leaving the BIOS setting to default? Or did you set the VRAM allocation within BIOS?





### [KageYume](https://www.reddit.com/user/KageYume/)



 (2025-05-03 01:14:23)


If the Z13 is anything like the ROG Ally, you set VRAM allocation in Armory Crate.





#### [ThisNameWasUnused](https://www.reddit.com/user/ThisNameWasUnused/)



 (2025-05-03 01:52:23)


Yeah, I've done that; I've set the VRAM to 64GB which is the same as the OP's. But somehow, their device is able to use the 'Shared GPU memory' (system RAM) if the GPU VRAM is not enough to load a model completely as evident in the video.  

Mine doesn't use any of the shared GPU memory. It just produces an out of system memory error and the model crashes unloads from LM Studio.





## [Healthy-Toe-9622](https://www.reddit.com/user/Healthy-Toe-9622/)



 (2025-05-02 18:09:05)


How did you solve the stars markdown issue? for me it remains like \*\*this\*\*





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 18:27:15)


Are you perhaps referring to an inference issue? I didn't do anything special with the model or software :\ pretty much just the parameters I shared in the post, and using the Unsloth UD Q2\_K\_XL quant. 


LM Studio and its runtime both at their latest current versions for Windows (0.3.15 Build 11, llama.cpp Vulkan '1.28.0' release b5173). 


For llama.cpp bare (using ./llama-server or ./llama-cli), I use release b5261 found on their GitHub releases.





## [DunderSunder](https://www.reddit.com/user/DunderSunder/)



 (2025-05-02 18:25:41)


very interesting. Is it feasible with battery? Do you think the temp is a concern?





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-02 21:44:22)


So I just did some quick testing on battery using the same prompt in the video. Very unscientific battery discharge numbers, but here goes.


* Turbo is disabled (not selectable) as a power mode on battery (~70-80W)
* Performance mode (~52 W)
	+ 7.37 tokens/sec for 928 tokens
	+ 79% -> 74% battery
* Silent mode (~39W)
	+ 6.26 tokens/sec for 1174 tokens
	+ 74% -> 71% battery


Manual mode (where I get to crank the wattages to 90W+ manually) doesn't do any better than performance mode on battery, meaning it's likely getting throttled by the batteries' max output.


Yeah, I should really get a battery meter that shows the exact discharge, sorry about that. 


As for temperature, I'm not particularly concerned. That's because the default manual mode fan curve is actually very tame; it defaults to 60% speed at 80C and 70% at 90C, then ramps up to 100% at 100C. The fan curve on Turbo mode (which this video was ran on) seems to be even \*more\* tame than manual mode, so it seems there's definitely a lot of extra fan speed headroom if you want to keep temps in check.





#### [DunderSunder](https://www.reddit.com/user/DunderSunder/)



 (2025-05-02 22:34:16)


battery usage seems ok. good for non-thinking, i can live with 6 t/s for chatting and stuff.


apparently M4 max 128gb gets 20 t/s (for double the price ofc)


still, not sure it it's all really useful for use cases like programming rather than using API.





## [NZT33](https://www.reddit.com/user/NZT33/)



 (2025-05-03 06:13:14)


This device is damn difficult to buy





## [Vostroya](https://www.reddit.com/user/Vostroya/)



 (2025-05-02 21:34:56)


If one is available you might try a low quant EXL3 version. Since that should help with the loss of accuracy





## [Zestyclose-Ad-6147](https://www.reddit.com/user/Zestyclose-Ad-6147/)



 (2025-05-02 23:39:50)


That’s really cool! Same specs as the framework desktop I believe.





## [Thellton](https://www.reddit.com/user/Thellton/)



 (2025-05-02 23:54:47)


[u/Invuska](https://reddit.com/u/Invuska), you should be able to get --batch-size up a little more to 384.





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-03 01:09:20)


Thanks for the tip! Also, thanks for your investigatory work on the Vulkan assert issue on GitHub! I was pretty lost until I stumbled upon your comment.





## [bennmann](https://www.reddit.com/user/bennmann/)



 (2025-05-03 01:18:45)


You could also try setting your Vram allocation to the lowest amount, and running -ngl 1 or 0


Might be you could fit the q3 or q4 that way, which are a few percentages more accurate and smarter.





## [OmarBessa](https://www.reddit.com/user/OmarBessa/)



 (2025-05-02 19:13:01)


jesus christ





## [Historical-Camera972](https://www.reddit.com/user/Historical-Camera972/)



 (2025-05-02 23:55:49)


What are you doing with your 235B model?  

Like, what's your use case, or an example similar to your use case?  

I want a Strix Halo system, and I'm just in ponderance of what exactly an AI model in this tier can actually do?





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-05-03 00:18:23)


[removed]





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-03 00:20:12)


This is actually on the Asus ROG Flow Z13 - a Microsoft Surface-like tablet :) Hope you enjoy your Framework 13!





## [moozoo64](https://www.reddit.com/user/moozoo64/)



 (2025-05-03 04:11:28)


Please benchmark Qwen3 -30B-A3B Q8 16k context window





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-05-03 07:11:47)


Prompt Processing Speed?


Update: OK I saw your numbers thanks. So about 40 tok/s prompt eval...





## [hackeristi](https://www.reddit.com/user/hackeristi/)



 (2025-05-03 09:48:31)


How do you get rid of “thinking…” and use it as a chatbot instead?





### [wiznko](https://www.reddit.com/user/wiznko/)



 (2025-05-03 11:20:27)


<no\\_think>





## [mnemoflame](https://www.reddit.com/user/mnemoflame/)



 (2025-05-27 05:10:21)


How much faster would that be if the software stack was supporting CPU + GPU + NPU...





## [wh33t](https://www.reddit.com/user/wh33t/)



 (2025-05-03 00:12:24)


They have AI Ryzen Max chips in tablets with 128gb of ram?
Please link this tablet.





### [Invuska](https://www.reddit.com/user/Invuska/)



 (2025-05-03 00:18:12)


Yep, I have the Asus ROG Flow Z13 2025: <https://rog.asus.com/laptops/rog-flow/rog-flow-z13-2025/spec/> . Comes in 32, 64, and 128GB RAM variants. 


That said, people have been struggling to find the tablet in stock for a while now.





## [vulcan4d](https://www.reddit.com/user/vulcan4d/)



 (2025-05-08 05:59:40)


These 395+ AMD APUs are a step in the right direction but they seriously should have done 4 channel memory otherwise it is far from a serious LLM option.





### [Mar2ck](https://www.reddit.com/user/Mar2ck/)



 (2025-05-08 09:14:51)


It is 4 channel memory