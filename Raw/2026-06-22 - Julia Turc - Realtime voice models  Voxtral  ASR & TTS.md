---
title: "Realtime voice models | Voxtral | ASR & TTS"
source: "youtube"
url: "https://www.youtube.com/watch?v=hyhANozV9Nw"
author: "Julia Turc"
published: "2026-06-22"
created: "2026-08-24"
duration: "0:26:37"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "context-engineering"
  - "engineering"
  - "google"
  - "hardware"
  - "nvidia"
  - "openai"
  - "video-gen"
  - "voice-ai"
  - "youtube-strategy"
summary: "Voice agents are in their Renaissance era. We're moving away from clunky
interactions with Alexa and Siri towards more natural real-time conversations. Could you order my usual
margarita from Luigi's?"
---

# Realtime voice models | Voxtral | ASR & TTS

![Realtime voice models | Voxtral | ASR & TTS](https://www.youtube.com/embed/hyhANozV9Nw)

## Description

This video dissects Voxtral Realtime and Voxtral TTS from Mistral as case studies for modern *realtime* voice models.

Mistral Studio: https://mistr.al/audio-juliaturc-yt
Voxtral Realtime: https://arxiv.org/abs/2602.11298
Voxtral TTS: https://arxiv.org/abs/2603.25551

We also cover important milestones in the history of speech models, including:
• OpenAI's Whisper
• Whisper Streaming
• WaveNet

And a few foundational concepts:
• Audio samples vs frames
• Audio quantization:
    →Vector Quantization / VQ
    →Residual Vector Quantization / RVQ
    →Finite Scalar Quantization / FSQ
• Semantic vs acoustic audio tokens

00:00 Intro
01:03 Modular vs end-to-end speech models
03:30 Speech-to-Text
06:07 Delayed Streams Modeling (DSM)
09:41 Whisper Streaming
10:33 Voxtral Realtime
13:07 Voxtral Text-to-Speech
14:28 Throwback: WaveNet
15:24 Audio tokenization
20:39 The Voxtral Codec
21:49 Back to Voxtral TTS
25:30 Outro

## Transcript

Voice agents are in their Renaissance era. We're moving away from clunky
interactions with Alexa and Siri towards more natural real-time conversations. Could you order my usual
margarita from Luigi's? Delivery here. Sure thing. Your usual medium
margarita with thin crust. On your office address? Yeah. But what exactly is hiding
behind these new voice agents? How are they taking advantage
of the LLM revolution? And also, why are they so late? At this point, even GPT-4
is about three years old. To answer these questions, we'll look at Voxtral, an
open-weights family of real-time voice models from Mistral, who
are also sponsoring this video. In an increasingly opaque industry, their
detailed technical reports are the reason why I can keep making educational content. So let's see what's hiding
behind this trench coat. When building voice agents with a
speech-to-speech interface, there are actually two schools of thought. One is modular, nesting an LLM
between two other powerful models. This is the more practical approach
embraced among others by Voxtral and will be the focus for this video. The alternative is end-to-end models,
which treat speech as a first-class citizen and remove the text bottleneck. Thinking Machines is one of the most
visible proponents for this approach, and we'll talk about it in the next video. A modular voice agent is really
three modules chained together. A speech-to-text model
transcribes the audio into text. It's also commonly known as an automated
speech recognition model or ASR. Its output is fed into a standard
LLM, which does the heavy reasoning. The response finally goes through a
text-to-speech or a TTS model, which maps it back to an audio output. These three components are
trained separately and only communicate through text. The most obvious benefit of this loose
decoupling is that you can mix and match. For each stage, you're free to pick the
single best model for your use case. Say you're running customer
support for a European bank that serves a dozen countries. Then you'll prioritize an ASR
model that does well on European languages and are probably willing
to compromise on Chinese quality. Then you'll take the LLM and
fine-tune it on the bank's playbooks. Also, for the text-to-speech
model, you might want to prioritize latency as opposed to emotional
nuance or rich acoustics. On the one hand, having text as an
intermediate representation is convenient for debugging and provides an auditable
paper trail in regulated settings. But on the other hand, it
throws away all the non-verbal information in the audio input, like
frustration, sarcasm, or hesitation. And chaining three models means
latency accumulates at every stage. There's just no free lunch. The Voxtral voice models from
Mistral can be plugged in as components of a modular pipeline. We'll look at two of them, Voxtral
Realtime for speech-to-text and Voxtral TTS for text-to-speech. In isolation, they're both streaming
models, meaning they start producing output almost immediately rather
than waiting for the full input. For speech-to-text, that means
Voxtral Realtime starts transcribing almost as soon as you're talking. Compare this to an offline transcription
model like OpenAI's Whisper. It waits for the entire voice recording
to be ready before starting to process it. And the entire transcription
shows up all at once. So what's the difference then? What does it take for an audio
model to work in real-time? But perhaps the better question
to start with is what exactly qualifies as real-time? What's an acceptable delay between speech
and its corresponding transcription? Is it under a second? Three seconds? Thirty seconds? The truth is there's no supreme
authority that draws the line, but most of us would probably place
it somewhere around three seconds. OpenAI's Whisper sits at the
very end of the spectrum with a context window of thirty seconds. It's an open source speech-to-text
model trained on 680,000 hours of weakly supervised audio. That means imperfect transcriptions
curated from the Internet or generated automatically without manual curation. Even though it was released back in 2022,
Whisper remains the most widely deployed offline transcription model in the
world and is a strong overall baseline. Voxtral Realtime allows a user-tunable
delay between 80 milliseconds and 2.4 seconds, and we'll see shortly how
they implemented this adjustability. Obviously, we're trading
latency for quality. Somewhere after the 480 millisecond mark,
Voxtral's word error rate becomes on par with Whisper, despite not having access
to a full thirty-second window of audio. So what exactly enables this performance? Well, let's work it out
backwards from the output. Here, I've modified Voxtral's
official Hugging Face space to surface the raw output tokens. If you look at their timestamps,
you'll notice that a new output token is emitted every 80 milliseconds. This is the cadence of a streaming model
. You'll also notice two special tokens, a padding which communicates, "I'm still
listening," or, "I'm still processing," and the word boundary placed right
before a stream of actual text tokens. These are all artifacts of a
recent modeling framework called Delayed Streams Modeling or DSM. It comes from a Paris-based
company called Kyutai. We'll hear more from
them in the next video. DSM introduced this idea of a heartbeat. Both audio and text streams advance at
a regular cadence, say 80 milliseconds. So on each heartbeat, a speech-to-text
model processes an audio frame of 80 milliseconds and also outputs a text token
corresponding to a previous audio frame. The text stream is therefore
delayed by a few heartbeats since obviously you can only transcribe
things that have already been said. That's why Voxtral's output starts
with a bunch of padding tokens. Say we set the desired
delay to 160 milliseconds. Then the first two pads enforce this
delay, and the rest are just accounting for silence since I didn't start speaking
immediately after pressing record. If you're a machine learning
practitioner, your first question might be, how do you even train
such a thing in the first place? Well, the first requirement is training
data that aligns audio and text at a word level so that the model learns
precisely what to say and when. You'll need something like this JSON
file where every word comes with its own start and end timestamps. And what about the configurable
delay between audio and text? Say that the model supports delays
between 80 to 2400 milliseconds. That is from 1 to 30 heartbeats. To support this entire range, the
DSM framework picks a random delay for each training batch, offsets
the text stream by that amount, and fills the gap with padding tokens. Delayed streams modeling is a
huge enabler for streaming models. But if we're being realistic,
it's not rocket science. It's quite an obvious algorithm. So why did it take so long for
it to be published in 2024? Well, the truth is streaming models
have existed for a long time, but they used to be implemented with
recurrent neural networks, which are a very natural architectural fit. The original Transformer,
however, was less so. So the true value of DSM is to
bring streaming to the Transformer in a way that enables pre-trained
LLMs to bootstrap speech models. Contrary to common belief, the original
Transformer, as published in 2017, was intended for offline machine
translation, mapping a piece of text from a source to a target language. The language modeling revolution
actually happened later. I covered this in one
of my previous videos. Now, speech-to-text is inherently
a translation problem, not between languages, but between modalities. That's why offline speech-to-text models
like OpenAI's Whisper were based on the original Transformer architecture. At the time, it had two core components:
an encoder to process the source sentence  and a decoder to generate
the translation auto-regressively. Because the source sentence was
assumed to be available in full, the encoder used bidirectional attention,
where each token embedding depended both on its left and right context. This is what limited Whisper's
real-time capabilities . It needed a full thirty-second context window
before it could start transcribing. Of course, people have hacked
around this limitation. Take Whisper Streaming, for example. It wraps the existing offline model
with an API that mimics real-time behavior by keeping an internal audio
buffer capped at thirty seconds. Once the audio buffer is filled, Whisper
Streaming makes its first call to Whisper. When a new chunk arrives, it displaces
the oldest one in the queue and triggers yet another call to Whisper. This did simulate real-time behavior
with just a few hundred milliseconds delay and only a small hit in accuracy. But it was ultimately still a
wasteful hack since the same audio chunks were transcribed repeatedly. Plus, there was a mismatch
between training and inference. Whisper was trained on full
sentences, but Whisper Streaming was calling it with incomplete
sentences and even incomplete words. In contrast, modern speech-to-text
models like Voxtral Realtime treat streaming as a first-class citizen. The first step is to completely
rethink the encoder, toss away the bidirectional attention, and replace it
with causal attention so that each audio chunk only depends on previous ones. In theory, this should be enough
to enable streaming behavior. But as I mentioned earlier, the
biggest value proposition of DSM is to enable preexisting pre-trained
LLMs to bootstrap speech models. Since most LLMs today are shaped as
a Transformer decoder, the decoder is a natural place to plug them in. In particular, Voxtral Realtime
leverages Ministral-3B. This is a completely different
LLM from the one that sits in the middle of a modular voice assistant. It's an internal component of
the speech-to-text model, and it gets fine-tuned for this task. Given the presence of this LLM, we
also need to reconsider how the encoder connects to the decoder, since this
cross-attention doesn't come with the LLM. Instead, we'll move the
audio encoder downstream. Once contextualized, audio
embeddings are directly added to the corresponding token embeddings. This way, audio and text are
processed at the same pace by design. From the point of view of the LLM, there's
a single input token for each heartbeat. It's just that under the wraps,
that input token is the sum of audio and text embeddings. And this is the architecture of
real-time speech-to-text models that follow the DSM framework. This is what Voxtral Realtime builds
upon, making additional adjustments that ensure training stability. One of their innovations is a
technique called adaptive RMSNorm. It's a new way of communicating to
the model the desired delay selected by the user at inference time. If you're familiar with such architectural
details, you'll immediately think of adaptive LayerNorm, a similar trick
used by the Diffusion Transformer to inject the diffusion step, which
I've covered in this other video. So once audio is transcribed by a
speech-to-text model like Voxtral Realtime, it can then be fed into an LLM,
again, different from the internal one. This LLM reasons over the user query,
maybe even call some tools in the process, and outputs a text response. Then a text-to-speech model turns it into
audio, which brings us to Voxtral TTS. Just like its sibling, Voxtral TTS
is, in isolation, a real-time model that produces audio auto-regressively. Its time to first audio is around
70 milliseconds on an H200 GPU. So how does audio generation work? Voxtral TTS accepts two inputs: a
piece of text and an audio recording with a voice reference somewhere
between 3 and 30 seconds that will guide what the output sounds like. It's what we call voice cloning. Under the hood, it's an auto-regressive
LLM that additionally takes in its previously generated audio
tokens and predicts the next one. But what exactly is an audio token? How can it be fed into an LLM, and
how does it compare to a text token? To understand that, we need
to start with the basics. When we digitize sound, the microphone
takes discrete measurements or samples of the wave's amplitude
at regular intervals in time. The sample rate, that is the
number of samples per second, is measured in Hertz (Hz). High-quality speech
requires at least 24 kHz. DeepMind's WaveNet was the first
neural network that attempted to model a raw waveform directly. Given that this was about a
decade ago, its outputs were remarkably natural sounding. Here's one example. However, WaveNet was notoriously
slow since it had to generate 24,000 samples per second sequentially. For real time, a new sample would have
to be generated every 42 microseconds. NVIDIA actually pulled it off with a
V100 GPU by fusing the whole WaveNet model into a single kernel and
caching the weights in the registers. But that's already scraping the
bottom of the barrel in terms of optimization headroom, and we
know that model sizes scale a lot faster than hardware capabilities. A more pragmatic approach came five
years later with models like SoundStream from Google and EnCodeC from Meta. Instead of predicting individual
samples, they worked with frames. These were sequences of 240 samples
or 10 milliseconds of audio, and this strategy survived until today. Now, we've already encountered audio
frames in the context of speech-to-text, where the audio stream was split into
fixed size windows, and each window was converted into a continuous embedding. In contrast, in the TTS world, audio
frames are treated as indivisible units, much like text tokens. Predicting a single audio token ID
instead of all the values in the frame makes the problem more tractable. For instance, Voxtral TTS uses
80 millisecond audio frames. This brings the real-time requirement
down from 24,000 to only 12.5 sequential predictions per second. But this brings an interesting
challenge, audio tokenization. We know, of course, that text tokenization
relies on a vocabulary that maps integer indices to character strings. What exactly is the audio equivalent
of character strings here? In theory, we could simply store
raw sequences of amplitudes, but their space is combinatorially huge. Plus, raw amplitude captures
the wrong level of abstraction. The same word spoken at a slightly
different volume or speed becomes an almost entirely different vector. Instead, audio tokens are
compressed in a latent space where vector similarity is meaningful. Because these entries are
called codes, the vocabulary is actually called a codebook. So how is this codebook built? Well, first of all, we need a
way to induce this latent space. The standard machine learning
solution across all modalities is an encoder-decoder model. It takes in the raw signal,
which is high dimensional, passes it through a low dimensional
bottleneck, and then reconstructs it. In the audio world, this model is known as
a codec, which comes from coder-decoder. It plays a similar role to the VAE model
used for image generation, though it's trained with a very different loss. Modern codecs apply vector quantization
or VQ right after the bottleneck. They define a codebook
of the desired size. In Voxtral's case, a bit over eight
thousand codes with 256 dimensions each. The compressed latent is then snapped
to the nearest entry in the codebook. This gives us a code, which is a vector of
256 values, as well as an integer index. The code is then passed on to the
decoder to complete the forward pass. This way, the codebook entries
are learned together with a codec. The integer index will only
serve later when training the actual text-to-speech model. Now, this is a valid tokenization
scheme, but arguably, audio is too rich of a signal to be
captured in around 8,000 tokens. One option would be to simply
increase the codebook size. After all, a text vocabulary
can go up to 250,000 tokens. However, empirically, large audio
codebooks lead to a phenomenon called codebook collapse, where
most entries remain unused. There are two effective
alternatives to Vector Quantization. One is Residual Vector
Quantization or RVQ. After the first level of
quantization, there's inevitably a small error, or residual. That's the difference between the
original embedding and the code we picked. Instead of ignoring it, RVQ
quantizes the residual with a second codebook, then a third, and so on. This way, each layer of quantization
captures finer and finer detail. The second alternative to vector
quantization makes a different trade-off. Finite Scalar Quantization, or FSQ,
treats vector dimensions independently. For any particular feature, its range of
values is split into N buckets, say 20. For simplicity, let's assume all
features fall between -1 and +1. Quantizing an input feature means
snapping it to the middle of its bucket. So for instance, -0.72 turns into -0.75. FSQ is more memory efficient since
there's no codebook needed, and you can trivially tweak its precision
by increasing the number of buckets. However, it fails to capture
correlations between dimensions. Plus, every single feature in the original
latent now gets its own integer index. This is different from vector
quantization, where the entire input embedding is mapped to a single integer. Since these three types of quantization
make different trade-offs, modern audio models mix and match them
in various ways without having converged to a standard solution. Let's see how Voxtral
tackles this challenge. The quantization strategy used
by the Voxtral Codec reflects an older philosophy about speech. The philosophy comes from AudioLM, a
Google model from 2022 that decomposes audio into two orthogonal aspects: what
is being said and how it's being said. Every audio frame is
decomposed into two embeddings. The semantic part captures phonemes or
words and their meaning, and the acoustic part reflects aspects like the speaker
timbre, prosody, emotion, microphone characteristics, breath sounds, and so on. The Voxtral Codec quantizes the two
latents separately, the semantic one with vector quantization and the acoustic
one with finite scalar quantization. This choice is quite intuitive. Semantics are tied to words
which are naturally clustered by meaning and can more credibly
be organized into a codebook. Intuitively, similar words
should map to the same code. Acoustics, on the other hand, are more
continuous in nature and require higher precision, which is what FSQ offers. So the codec is an auxiliary model
that can take an audio frame as a sequence of amplitudes and turn it
into an audio token, which is the basic building block of the actual TTS model. But at this point, there's
still a discrepancy between the codec and the TTS model. The codec factorizes tokens into
semantic and acoustic parts, but the auto-regressive prediction
model expects indivisible audio tokens. Here's how this conflict gets resolved. After quantization, each audio frame
gets one semantic token ID, which comes from the VQ codebook, and multiple
acoustic IDs because FSQ gives you a separate integer for every dimension. From here, we'll treat audio
tokens, or rather audio subtokens, similarly to text tokens. Remember, an LLM contains an
embedding table that maps token IDs to internal continuous representations. All we need to do is extend this table
with new entries for audio tokens. That is about 8,000 more for the
codebook tokens and groups of 20 buckets for each acoustic feature. Once semantic and acoustic tokens
are looked up in the LLM embedding table, we can collapse their stacks
by summing up the embeddings. And from here on, all tokens
share the same interface and can therefore flow through a regular LLM. Well, almost regular, because we'll
have to change its output dictionary, swap out the text vocabulary, and
swap in the semantic codebook. This way, on each iteration, the
LLM produces a semantic token ID. The acoustic part, though,
needs special treatment. As we discussed earlier, acoustics
don't have the same clustered nature. It's a lot harder to discretize
and predict them using an inherently discrete LLM. If you've been following my
channel, you already know about flow matching, the generative algorithm
behind modern image generation. It learns a velocity field that
transports noise directly towards the data distribution in a fixed number of steps. The same idea applies to audio. Starting with a noisy vector and refining
it eight times, the output becomes a clean prediction of the acoustic latent. The conditioning signal is the
last hidden state of the LLM, which has been shaped by the voice
reference from the context window. This is how the speaker's timbre and
acoustic character get transferred, because the LLM has been attending
to the voice reference all along. By applying FSQ to the flow
matching output, we get our stack of acoustic token IDs. In the next auto-regressive step, all
output token IDs make their way back to the input, and the cycle repeats exactly 12.5 times per second. To produce an actual waveform, the
output token IDs are de-quantized into real values and passed through
the decoder part of the codec. This is quite an involved journey
for the clean acoustic latent. Initially, it's a continuous
vector, then quantized, immediately dequantized, then expanded into another
latent space by the codec decoder. A similar complexity is
present in the loss function. The codec loss has five separate terms,
including distillation from Whisper and an adversarial term, and the full Voxtral TTS
adds cross-entropy for semantic tokens, flow matching loss on acoustics,  and
direct preference optimization for both. This goes to show that text-to-speech
is a really difficult problem. It's an active field of research
that hasn't yet converged to a simple and canonical solution. Today, most voice systems in production take the modular approach because
it's customizable and interpretable. Now, the Voxtral speech-to-text
and text-to-speech models are real-time in isolation, but the
LLM in the middle is a limiting factor for a voice-to-voice system. The text bottleneck drops the audio and
together with it, emotions like sarcasm or frustration that might actually be
relevant in addressing the user query. In the next video, we'll look at models
that were trained end-to-end with streaming and interactivity in mind. If Voxtral piqued your interest,
you can play with both models right now in Mistral Studio, same place
you'll find Mistral's LLMs and tools for building agents and workflows. In the meantime, you can find
my full reading list and my Miro board for this video on Patreon. Thanks for watching, and
I'll see you next time.
