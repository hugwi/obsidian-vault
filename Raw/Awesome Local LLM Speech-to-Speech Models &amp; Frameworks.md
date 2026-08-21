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

# Awesome Local LLM Speech-to-Speech Models &amp; Frameworks

![rw-book-cover](https://external-preview.redd.it/sv2a4YrAVR9g08yOa0AOrBrIqErmKKSQAYIjNTCx_eI.png?width=140&amp;height=70&amp;auto=webp&amp;s=43d70694055f093dfc6531bbb89c6a15dad87976)

## Metadata
- Author: [[tleyden]]
- Full Title: Awesome Local LLM Speech-to-Speech Models &amp; Frameworks
- Category: #articles
- Summary: The post shares a list of local speech-to-speech models that integrate large language models and work fully offline. It highlights two main types: cascading pipelines and end-to-end systems, each with pros and cons. The author and community discuss features, platforms, and improvements for these frameworks.
- URL: https://www.reddit.com/r/LocalLLaMA/comments/1nxqabe/awesome_local_llm_speechtospeech_models_frameworks/

## Full Document
**[r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)**

### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-04 10:19:27)

Did some digging into speech-to-speech models/frameworks for a project recently and ended up with a pretty comprehensive list. Figured I'd drop it here in case it helps anyone else avoid going down the same rabbit hole. 

What made the cut:

* Has **LLM integration** (built-in or via modules)
* Does **full speech-to-speech** pipeline, not just STT or TTS alone
* Works **locally/self-hosted**

Had to trim quite a bit to keep this readable, but the full list with more details is on GitHub at [tleyden/awesome-llm-speech-to-speech](https://github.com/tleyden/awesome-llm-speech-to-speech). PRs welcome if you spot anything wrong or missing! 

| **Project** | **Open Source** | **Type** | **LLM + Tool Calling** | **Platforms** |
| --- | --- | --- | --- | --- |
| [**Unmute.sh**](https://github.com/kyutai-labs/unmute) | ✅ Yes | Cascading | Works with any local LLM · Tool calling not yet but planned | Linux only |
| [**Ultravox (Fixie)**](https://github.com/fixie-ai/ultravox) | ✅ MIT | Hybrid (audio-native LLM + ASR + TTS) | Uses Llama/Mistral/Gemma · Full tool-calling via backend LLM | Windows / Linux |
| [**RealtimeVoiceChat**](https://github.com/KoljaB/RealtimeVoiceChat) | ✅ MIT | Cascading | Pluggable LLM (local or remote) · Likely supports tool calling | Linux recommended |
| [**Vocalis**](https://github.com/Lex-au/Vocalis) | ✅ Apache-2 | Cascading | Fine-tuned LLaMA-3-8B-Instruct · Tool calling via backend LLM | macOS / Windows / Linux (runs on Apple Silicon) |
| [**LFM2**](https://www.liquid.ai/blog/liquid-foundation-models-v2-our-second-series-of-generative-ai-models?ref=producthunt) | ✅ Yes | End-to-End | Built-in LLM (E2E) · Native tool calling | Windows / Linux |
| [**Mini-omni2**](https://github.com/gpt-omni/mini-omni2) | ✅ MIT | End-to-End | Built-in Qwen2 LLM · Tool calling TBD | Cross-platform |
| [**Pipecat**](https://github.com/pipecat-ai/pipecat) | ✅ Yes | Cascading | Pluggable LLM, ASR, TTS · Explicit tool-calling support | Windows / macOS / Linux / iOS / Android |

**Notes**

* “Cascading” = modular ASR → LLM → TTS
* “E2E” = end-to-end LLM that directly maps speech-to-speech

#### [nullnuller](https://www.reddit.com/user/nullnuller/)

 (2025-10-04 11:29:28)

Any of them supported by llama.cpp ?

##### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-04 12:03:22)

Vocalis definitely looks like it can run on llama.cpp, since it supports whisper.cpp for the STT, and any openai compatible endpoint for LLM, so ollama + llama.cpp would work fine. 

BTW, I think it mainly applies to the STT and LLM, because AFAIK llama.cpp is not used for TTS. If you're on Apple Silicon, Vocalis uses Kokoro-FastAPI for the TTS engine, which supports MPS acceleration.

Great question, I will try to update the table to call that out in the table.

##### [fish312](https://www.reddit.com/user/fish312/)

 (2025-10-04 18:25:17)

Koboldcpp supports kokoro

#### [drc1728](https://www.reddit.com/user/drc1728/)

 (2025-10-04 20:04:53)

Nice list — thanks for pulling this together. The interesting split I’ve noticed is between **cascading** vs. **end-to-end** architectures.

Cascading pipelines (ASR → LLM → TTS) are still dominant because they’re modular and easy to debug — you can swap models, add RAG, or inspect transcripts midstream. But they suffer from latency stacking and occasional semantic drift between stages.

End-to-end systems (like LFM2 and mini-omni2) are starting to close the gap, especially for short-turn dialog. Once they can reliably expose internal text embeddings or reasoning traces, they’ll probably outperform cascades in coherence and speed.

Would be curious if anyone’s seen real benchmarks comparing **semantic fidelity** or **latency** between these two classes — especially when local models are involved.

##### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-04 20:09:29)

From this [Kyutai blog post](https://kyutai.org/2025/05/22/unmute.html):

> 
> “But what about Moshi?” Last year we unveiled Moshi, the first audio-native model. While Moshi provides unmatched latency and naturalness, it doesn’t yet match the extended abilities of text models such as function-calling, stronger reasoning capabilities, and in-context learning. Unmute allows us to directly bring all of these from text to real-time voice conversations.
> 
> 
> 

#### [KaanTheChosenOne](https://www.reddit.com/user/KaanTheChosenOne/)

 (2025-10-04 12:47:21)

Some more <https://github.com/speaches-ai/speaches> and <https://github.com/dnhkng/GLaDOS>

##### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-04 13:02:32)

These look great! I'm adding now.

###### [Blizado](https://www.reddit.com/user/Blizado/)

 (2025-10-04 16:46:38)

That would be nice, a good actual overview would be very useful.

###### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-04 16:54:02)

Do you mean add a new column that summarizes each framework?

#### [christianweyer](https://www.reddit.com/user/christianweyer/)

 (2025-10-04 14:30:23)

AFAICT, LFM2 has no Tool Calling [u/tleyden](https://reddit.com/u/tleyden)

##### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-04 14:51:40)

It says it supports tool use [on their hugging face model card](https://huggingface.co/LiquidAI/LFM2-2.6B): 

1. **Function definition**: LFM2 takes JSON function definitions as input (JSON objects between `<|tool_list_start|>` and `<|tool_list_end|>` special tokens), usually in the system prompt
2. etc..

###### [christianweyer](https://www.reddit.com/user/christianweyer/)

 (2025-10-04 14:55:41)

Ahhhh - I was mixing this up with LFM2-Audio. My bad.

###### [christianweyer](https://www.reddit.com/user/christianweyer/)

 (2025-10-04 15:07:08)

Hm... maybe we are both confused [u/tleyden](https://reddit.com/u/tleyden)? 😅 

LFM2 is not speech-enabled. LFM2-Audio is.  

LFM2 does tool calling. LFM2-Audio does not.

The demo links for "LFM2" on your repo point to LFM2-Audio.  

The link about the model itself points to the blog post from [Liquid.ai](http://Liquid.ai) about LFM2.

Confusing, isn't it?

###### [christianweyer](https://www.reddit.com/user/christianweyer/)

 (2025-10-04 15:09:38)

This [comment](https://www.linkedin.com/feed/update/urn:li:ugcPost:7379151558485258241?commentUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7379151558485258241%2C7379157934766727168%29&replyUrn=urn%3Ali%3Acomment%3A%28ugcPost%3A7379151558485258241%2C7379212021336170496%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287379157934766727168%2Curn%3Ali%3AugcPost%3A7379151558485258241%29&dashReplyUrn=urn%3Ali%3Afsd_comment%3A%287379212021336170496%2Curn%3Ali%3AugcPost%3A7379151558485258241%29) (on LinkedIn) from the CEO could actually underpin it.

###### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-06 06:49:42)

Ok that definitely clarifies it. Nice digging! I'm updating the list to say no tool calling, and linking to that LI comment

#### [countAbsurdity](https://www.reddit.com/user/countAbsurdity/)

 (2025-10-05 01:50:30)

Hey, do you know if any of these support understanding and speaking in italian and run respectably on 8gb vram? I'd like to practice and preferably something that corrects me when I say something wrong (which is often)

#### [Mkengine](https://www.reddit.com/user/Mkengine/)

 (2025-10-04 17:45:50)

Why no Qwen3-Omni?

##### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-04 18:57:31)

Thank you for the call out. I'm updating it.

##### [phhusson](https://www.reddit.com/user/phhusson/)

 (2025-10-05 13:26:25)

Because noone has been able to run it as real-time speech-to-speech model yet 🙈

#### [rzvzn](https://www.reddit.com/user/rzvzn/)

 (2025-10-05 02:07:22)

> 
> What made the cut: 
> 
> 
> 

Works **locally/self-hosted**

Pipecat, hmm. Isn't that an API key party? i.e. will not work locally/self-hosted (offline) without API keys

##### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-05 06:09:48)

I honestly wasn’t 100% sure from their docs if a backend service was required, but from Ancient Jellyfish’s response to your question, looks like it can run without one.

#### [vamsammy](https://www.reddit.com/user/vamsammy/)

 (2025-10-05 17:45:57)

I really like this one because it works on the Mac (other platforms too, undoubtedly) in quasi-realtime if one uses quantized models, and the TTS is orpheus, which is my current favorite. It hasn't been updated in some time but works well. The LLM and the orpheus model (in GGUF quant) are both run using llama.cpp / llama-server.

<https://github.com/PkmX/orpheus-chat-webui>

##### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-06 06:43:46)

But it doesn't have the speech recognition side as far as I can tell, so it's not fully speech-to-speech

###### [vamsammy](https://www.reddit.com/user/vamsammy/)

 (2025-10-07 03:42:21)

Yes it does. You speak into the mic.

###### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-07 05:43:08)

Sorry my mistake, I didn’t read the readme closely enough. I will add it.

###### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-07 06:44:55)

Wow it even supports webrtc! Thanks again for calling this out

###### [vamsammy](https://www.reddit.com/user/vamsammy/)

 (2025-10-07 14:33:34)

Yes it does. I spent a lot of time attempting to make this truly local by using coturn to create my own stun servers, so that I could run it with wifi turned off. But in the end, it failed. As soon as I turn off my laptop's wifi, the gradio throws errors about lost connection. I think it's a limitation of webrtc/fastrtc... According to Claude ai , it's still safe in that no data are transmitted. Not sure one way or the other if that's true but I hope so.

###### [tleyden](https://www.reddit.com/user/tleyden/)

 (2025-10-07 14:37:05)

[u/freddyaboulton](https://reddit.com/u/freddyaboulton) tagging you in case you know if this is a known limitation of gradio or fastrtc

#### [zinyando](https://www.reddit.com/user/zinyando/)

 (2026-02-16 03:47:40)

I'm working on Izwi <https://github.com/agentem-ai/izwi> a local first audio LLM inference engine with voice playground. I'm adding support for models like these. Hope to support a lot of them soon.
