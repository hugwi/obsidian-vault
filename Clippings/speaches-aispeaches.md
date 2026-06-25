---
categories:
  - "[[Clippings]]"
domain: [ai-agents]
tags:
  - models
  - voice
source: readwise
created: 2026-06-23
rating: 
action: 
---

# speaches-ai/speaches

![rw-book-cover](https://repository-images.githubusercontent.com/802330841/4cffb4ad-314f-4f97-aa4c-9b62a32c3a39)

## Metadata
- Author: [[https://github.com/speaches-ai/]]
- Full Title: speaches-ai/speaches
- Category: #articles
- Summary: Speaches is a server that works like the OpenAI API for speech transcription, translation, and generation. It uses fast models like faster-whisper for speech-to-text and kokoro and piper for text-to-speech. The project supports streaming, dynamic model loading, and works on both GPU and CPU.
- URL: https://github.com/speaches-ai/speaches

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/speaches-ai/speaches?resume=1) 

#### Create list

### speaches-ai/speaches

master

t

Go to file

Code

Open more actions menu

### Speaches

`speaches` is an OpenAI API-compatible server supporting streaming transcription, translation, and speech generation. Speach-to-Text is powered by [faster-whisper](https://github.com/SYSTRAN/faster-whisper) and for Text-to-Speech [piper](https://github.com/rhasspy/piper) and [Kokoro](https://huggingface.co/hexgrad/Kokoro-82M) are used. This project aims to be Ollama, but for TTS/STT models.

See the documentation for installation instructions and usage: [speaches.ai](https://speaches.ai/)

#### Features:

* OpenAI API compatible. All tools and SDKs that work with OpenAI's API should work with `speaches`.
* Audio generation (chat completions endpoint) | [OpenAI Documentation](https://platform.openai.com/docs/guides/realtime)
	+ Generate a spoken audio summary of a body of text (text in, audio out)
	+ Perform sentiment analysis on a recording (audio in, text out)
	+ Async speech to speech interactions with a model (audio in, audio out)
* Streaming support (transcription is sent via SSE as the audio is transcribed. You don't need to wait for the audio to fully be transcribed before receiving it).
* Dynamic model loading / offloading. Just specify which model you want to use in the request and it will be loaded automatically. It will then be unloaded after a period of inactivity.
* Text-to-Speech via `kokoro`(Ranked #1 in the [TTS Arena](https://huggingface.co/spaces/Pendrokar/TTS-Spaces-Arena)) and `piper` models.
* GPU and CPU support.
* [Deployable via Docker Compose / Docker](https://speaches.ai/installation/)
* [Realtime API](https://speaches.ai/usage/realtime-api)
* [Highly configurable](https://speaches.ai/configuration/)

Please create an issue if you find a bug, have a question, or a feature suggestion.

#### Demos

##### Realtime API

  2025-05-29\_21-40-00.webm    
(Excuse the breathing lol. Didn't have enough time to record a better demo)

##### Streaming Transcription

TODO

##### Speech Generation

  2025-01-12\_13-20-58.webm
