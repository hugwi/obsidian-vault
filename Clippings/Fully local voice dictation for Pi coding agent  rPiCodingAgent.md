---
title: "Fully local voice dictation for Pi coding agent : r/PiCodingAgent"
source: "https://www.reddit.com/r/PiCodingAgent/comments/1ta97mk/fully_local_voice_dictation_for_pi_coding_agent/"
author:
  - "[[reddit.com]]"
published: 2026-05-11
created: 2026-06-29
description:
tags:
  - "clippings"
  - "pi-voice"
---
## Fully local voice dictation for Pi coding agent: no cloud, no API keys

`/voice` opens an overlay, you talk, live transcript appears, hit `Enter` and it drops into the agent's editor. Whisper runs on your CPU via sherpa-onnx. Nothing leaves the machine after the initial model download.

## What it does

- **100% on-device STT.** Whisper base multilingual (int8 quantized) runs on your CPU. No network calls after the first model download (~198 MB). Works offline after that.
- **Multilingual.** Your active locale (set via `/languages`) is pre-set as Whisper's language hint for better accuracy and lower first-utterance latency. Default is English.
- **Live transcript.** Committed lines render as you finish phrases, with a dim rolling partial for the still-active utterance. What you see is what gets pasted.
- **VAD-driven chunking.** Silero voice activity detection breaks your speech at natural pauses, so latency stays low even on long rants.
- **Hallucination filter.** Whisper sometimes outputs "Thanks for watching" or "\[Music\]" on silence. The filter strips that. Toggle it off in settings if it's too aggressive.
- **Pause/resume with Space.** Step away mid-thought, come back, keep going.

## How to install it

```md
pi install npm:@juicesharp/rpiv-voice
```

[https://www.npmjs.com/package/@juicesharp/rpiv-voice](https://www.npmjs.com/package/@juicesharp/rpiv-voice)

Restart your Pi session. Type `/voice`. That's it. The first run downloads the Whisper model (198MB), after that it loads from disk.

Controls

| Key | Action |
| --- | --- |
| Speak | Transcript fills in live |
| `Enter` | Commit transcript to editor |
| `Esc` | Cancel (nothing pasted) |
| `Space` | Pause / resume mic |
| `Tab` | Switch to settings screen |
| `Ctrl+S` | Save settings |

---

## Comments

> **TrackActive841** · [2026-05-11](https://reddit.com/r/PiCodingAgent/comments/1ta97mk/comment/ol92yaa/) · 2 points
> 
> I like your user question feature, will definitely add this too!
> 
> > **juicesharp** · [2026-05-11](https://reddit.com/r/PiCodingAgent/comments/1ta97mk/comment/ol983de/) · 1 points

> **Lpaydat** · [2026-05-18](https://reddit.com/r/PiCodingAgent/comments/1ta97mk/comment/omesmad/) · 2 points
> 
> Thank you for all your awesome extensions. 💪

> **TheCTRL** · [2026-05-11](https://reddit.com/r/PiCodingAgent/comments/1ta97mk/comment/ol875hm/) · 1 points
> 
> Good thanks but how to stop it? /voice again?
> 
> > **juicesharp** · [2026-05-11](https://reddit.com/r/PiCodingAgent/comments/1ta97mk/comment/ol8spjz/) · 1 points
> > 
> > ESC / Enter

> **leads\_leader** · [2026-05-15](https://reddit.com/r/PiCodingAgent/comments/1ta97mk/comment/olw7utj/) · 1 points
> 
> This is awesome, that fully local, on-device STT for a coding agent on a Pi is such a smart move for privacy and responsiveness. Getting Whisper running via \`sherpa-onnx\` right on the CPU sounds really solid. I'm curious, how's the real-time latency and accuracy with the int8 quantized base model on typical Pi hardware? That immediate drop into the editor without any network calls is a huge win for workflow.