---
title: "🎙️ Building a Local Voice-Controlled AI Agent"
source: "https://dev.to/akshat_saxena_53bee826693/building-a-local-voice-controlled-ai-agent-4967"
author:
  - "[[dev.to]]"
published: 2026-04-15
created: 2026-06-29
description: "I Built a Voice-Controlled AI Agent That Runs Locally — Here's Everything I Learned   From raw audio... Tagged with python, ai, rag, webdev."
tags:
  - "clippings"
---
**I Built a Voice-Controlled AI Agent That Runs Locally — Here's Everything I Learned**

> From raw audio to code written on your disk — the architecture, the model choices, and the parts that nearly broke me.

There's a particular kind of frustration that comes from building something that *should* work in theory but keeps surprising you in practice. That's the best way I can describe the two days I spent building a voice-controlled AI agent from scratch — one that listens to what you say, figures out what you want, and actually does it. Creates files. Writes code. Summarises documents. Answers questions. All from a single spoken sentence.

This isn't a tutorial about stringing together three API calls and calling it a day. This is the real story — the architecture decisions, the model tradeoffs, the bugs that made me laugh, and the one problem that took me six hours to solve because I was looking in entirely the wrong place.

Let's get into it.

## What I Was Actually Trying to Build

The goal was straightforward on paper: an agent that accepts voice input (either from a microphone or an uploaded audio file), converts it to text, classifies the user's intent, and then executes the right action on the local filesystem — all displayed through a clean web UI.

The key word is *local*. I wanted this to run on a normal laptop, without sending everything to the cloud, without requiring a GPU, and without needing to pay per token just to rename a file. The final stack supports four different LLM backends (Gemini, OpenAI-compatible endpoints, Groq, and Ollama) and two STT backends (local Whisper and Groq's hosted API), so you can tune the privacy/cost/latency tradeoff to whatever your machine and budget allow.

The pipeline looks like this:

```
Audio Input → STT → Intent Classification → Tool Dispatch → UI Output
                                   ↓
                          Session Memory (sidebar)
```

Simple enough. Except nothing about implementing it was.

## The Architecture, Layer by Layer

### Layer 1: Getting Audio In

I started with the easiest-looking problem: accepting audio. Streamlit doesn't ship with a microphone component out of the box, so I used `streamlit-mic-recorder`, a small community package that wraps the browser's MediaRecorder API. It returns raw WAV bytes, which is exactly what Whisper wants.

For uploaded files, Streamlit's native `file_uploader` handles WAV, MP3, OGG, and M4A just fine. The only thing I had to be careful about was preserving the file extension as a hint to downstream processors — Whisper handles format detection internally, but Groq's STT API needs the filename to include the right extension so it knows what codec to expect.

One small thing that tripped me up: `streamlit-mic-recorder` returns audio in its own dictionary format (`recording["bytes"]`), not as a plain bytes object. Reading the source code for two hours before noticing this in the docs felt like a very specific kind of stupidity that I suspect I'm not alone in experiencing.

### Layer 2: Speech-to-Text

This is where the first serious tradeoff lives.

**OpenAI Whisper (local)** is remarkable for what it is — a model that can run entirely on CPU, handles multiple languages without configuration, and produces transcriptions that are genuinely good even with background noise. The `base` model (74 MB) is the sweet spot for most hardware. On a modern CPU it transcribes a 10-second clip in about 5–8 seconds. That's acceptable. The `tiny` model is faster but starts making mistakes on accented speech and technical vocabulary. The `small` model is noticeably better but slower — 20 to 30 seconds on CPU starts to feel like waiting.

**Groq's hosted Whisper** (large-v3) does the same job in under a second. It's cloud-based, which means audio leaves your machine, but the quality is the best available and the latency is almost magical compared to local inference. For anyone who can't run Whisper locally — either because of slow hardware or RAM constraints — this is the practical fallback.

I made the backend configurable through a single environment variable (`STT_BACKEND=whisper` or `STT_BACKEND=groq`) so switching is a one-line change in `.env`.

The abstraction layer is clean:

```perl
def transcribe(audio_bytes: bytes, file_ext: str = ".wav") -> str:
    if config.STT_BACKEND == "groq":
        return _transcribe_groq(audio_bytes, file_ext)
    return _transcribe_whisper(audio_bytes, file_ext)
```

That's it. The rest of the pipeline doesn't need to care.

### Layer 3: Intent Classification — The Hard Part

Once you have text, you need to understand what the user actually wants. This is where LLMs earn their place in the pipeline.

My first instinct was to do this with a simple keyword matcher — if the text contains "create" and "file", route to the file creation tool. This works for the obvious cases and fails spectacularly for everything else. "Can you make a script that creates files in a loop?" triggers the wrong branch. "Write me something that opens a new document" is ambiguous. Natural language is messy.

So I handed the problem to an LLM with a structured prompt that asks for JSON output:

```json
{
  "intents": ["write_code"],
  "filename": "retry.py",
  "language": "python",
  "description": "A function that retries a failed HTTP request up to 3 times",
  "text_to_summarize": null
}
```

The prompt is careful about what it asks for. It defines exactly five valid intent strings, gives explicit rules about when to combine them (compound commands like "write a script and save it as utils.py" map to `["write_code"]` not `["write_code", "create_file"]` — because code writing implies file creation), and tells the model to return nothing but the JSON object.

Getting reliable JSON out of LLMs took more iteration than I expected. Gemini, when configured with `response_mime_type="application/json"`, is excellent — it almost never wraps output in markdown fences or adds preamble. Other models are less disciplined. My JSON extractor strips fences, searches for the first `{...}` block, and parses it — a belt-and-suspenders approach that handles most misbehaviour.

The bigger challenge was **compound commands**. Say something like "summarise this article and save it to notes.txt" — the agent needs to recognise two things happening: a summarisation and a file write. The LLM handles this well when prompted correctly, returning `["summarize"]` with `filename: "notes.txt"`. The tool dispatcher then routes to the summarise tool, which detects the filename and saves automatically.

#### Which LLM to Use?

I tested four backends extensively. Here's my honest take:

**Gemini 2.5 Flash** is where I landed as the default recommendation. It's fast (typically under two seconds for intent classification), produces clean structured JSON, has a generous free tier (15 requests per minute, one million tokens per day via Google AI Studio), and handles the kinds of instructions I'm giving it without complaint. The `google-generativeai` SDK is well-maintained and the JSON mode is first-class.

**Groq with Llama 3 (8B)** is the speed champion — sub-second responses, genuinely impressive for a hosted service, and the free tier is very usable (6,000 requests per day). The 8B model is slightly less reliable on complex compound commands compared to Gemini, but for straightforward single-intent commands it's excellent.

**OpenAI's GPT-3.5-turbo** works well but costs money and has no free tier. I kept it in the codebase because many developers already have API credits, and the JSON mode is rock-solid. I also wired in support for any OpenAI-compatible endpoint — which means OpenRouter, which gives you free access to Llama, Mistral, Gemma, and Qwen models with a free account and no credit card.

**Ollama** (local) is the most private option and the one I had originally planned to use as the primary backend. It works beautifully once you have a model pulled. The problem is "once you have a model pulled" — Mistral is 4 GB, Llama 3 is larger, and pulling them requires a fast internet connection and available disk space. For anyone who can't meet those requirements, the cloud backends are the practical answer.

### Layer 4: Tool Execution

Once the intent is classified, one of four tools runs:

**`create_file`** — creates an empty file or directory at the specified path inside `output/`. There's a path traversal check on every operation: the resolved path must start with the resolved `OUTPUT_DIR`, or the operation is rejected. This is non-negotiable safety plumbing.

**`write_code`** — sends a code-generation prompt to the LLM, receives the result, strips any markdown fences if the model got enthusiastic, and writes the file. The prompt is explicit: "Return ONLY the code — no markdown fences, no explanation." Gemini follows this instruction reliably. Some models need gentle reminding via the fence-stripping fallback.

**`summarize`** — passes the text to the LLM with a summarisation prompt. If a filename was detected in the original command, it saves the summary to that file automatically. This is the compound command case mentioned above.

**`chat`** — just talks. Passes the transcription directly to the LLM and returns the response. No file operations.

Every tool returns an `ActionResult` dataclass with `success`, `action_taken`, `output`, `file_path`, and `error`. The UI renders these uniformly regardless of which tool ran.

### Layer 5: Human-in-the-Loop

This was a bonus feature but ended up being one of the things I'm most glad I built.

Before any file operation executes, if the HITL toggle is on (it's on by default), the UI shows a confirmation card with the detected intent, the planned filename, and the description. The user can approve or cancel.

This turns out to be genuinely useful — not just as a safety feature, but as a debugging tool. When the LLM misclassifies something, you see it before anything happens. You can cancel and rephrase. It makes the agent feel less like a black box and more like a collaborator.

The implementation stores the `ParsedIntent` object in Streamlit session state between runs and re-uses it when the user confirms. The pipeline generator yields an `awaiting_confirmation` stage that pauses execution until the user interacts with the confirmation UI.

## The Challenges That Actually Hurt

### The Whisper Memory Spike

The first time I loaded the Whisper `small` model during a Streamlit session, it worked. The second time, I got an out-of-memory error. The third time it worked again.

The issue: I was loading the model inside the transcription function on every call, which meant it was being garbage-collected and reallocated unpredictably. The fix was lazy loading with a module-level singleton:

```python
_whisper_model = None

def _load_whisper():
    global _whisper_model
    if _whisper_model is None:
        _whisper_model = whisper.load_model(config.WHISPER_MODEL)
    return _whisper_model
```

Load once, reuse forever within the process. Memory stable. This is the kind of thing that's obvious in hindsight and invisible until you spend three hours staring at memory profiler output.

### Streamlit's Execution Model

Streamlit re-runs your entire script on every user interaction. This is elegant for simple apps and a source of creative suffering for anything stateful.

The pipeline I built is a generator — it `yield` s status updates as each stage completes, which lets the UI show live progress. But when the Human-in-the-Loop confirmation splits the pipeline across two Streamlit runs, you can't just hold the generator open. It gets garbage-collected.

The solution was to decouple the two phases completely. The first run (STT + intent classification) stores its result in `st.session_state`. The confirmation UI reads from session state. The second run (tool execution) pulls the stored intent and executes it. No generator spans the boundary — each run is self-contained.

This is the right pattern for Streamlit, and it took longer to arrive at than I'd like to admit.

### Getting LLMs to Always Return Valid JSON

This sounds like a solved problem and mostly is — if you use JSON mode. But not every backend has a native JSON mode, and even models that do occasionally produce something that looks like JSON but isn't: trailing commas, unquoted keys, truncated output because the response hit a token limit.

My extraction function (`_extract_json`) is deliberately robust:

1. Strip markdown code fences with a regex
2. Find the first `{...}` block (handles preamble like "Sure! Here's the JSON:")
3. Parse it
4. If it fails, return an `unknown` intent with the raw output as the error

The most important lesson: **never crash on bad LLM output**. Log it, degrade gracefully, show the user something useful. The pipeline continues even if intent classification fails — it just routes to the `unknown` handler, which tells the user to try rephrasing.

### The streamlit-mic-recorder Silence Problem

If a user hits record and immediately hits stop without saying anything, the recorded audio is a few hundred milliseconds of silence. Whisper transcribes this as `" "` (a single space) or `""`. The pipeline then tries to classify an empty string.

I added a guard: if the transcription is empty or whitespace-only, show a friendly message ("I didn't catch that — please try again") and stop the pipeline. This sounds trivial. It took an embarrassingly long time to track down because Whisper was producing a non-empty string (the single space), which passed the initial `if not transcription` check.

The fix is `if not transcribed_text.strip()`. Always strip.

## What I Would Do Differently

**Build the test harness first.** I wrote `test_pipeline.py` — a headless CLI that injects text directly and skips the audio step — halfway through the project. Having it from day one would have saved enormous time. Testing audio input requires a browser session and an audio recording. Testing intent classification just requires a string. Decouple them.

**Invest more in prompt engineering early.** The intent classification prompt went through about eight revisions. Each revision improved reliability measurably. I wish I had spent the first day on nothing but prompt iteration instead of building UI scaffolding that I later changed.

**Add streaming LLM output to the UI.** For code generation especially, watching the response arrive token by token feels much better than a spinner that says "generating..." for ten seconds. Gemini and OpenAI both support streaming. It's not architecturally difficult — I just ran out of time.

## The Free Tier Situation

One thing I want to be direct about because the confusion here is real:

**OpenAI has no free tier.** You need a paid account and purchased credits to use `api.openai.com`. Full stop. If you want free access to capable LLMs with an OpenAI-compatible API, use OpenRouter. You sign up, get free initial credits, and can access Llama 3, Mistral, and Gemma models without entering a credit card. The endpoint is drop-in compatible — just change `OPENAI_BASE_URL` to `https://openrouter.ai/api/v1` and use a free model name like `meta-llama/llama-3-8b-instruct:free`.

**Gemini is genuinely free for this use case.** 15 requests per minute and one million tokens per day on `gemini-2.5-flash` via Google AI Studio. For a voice agent that processes one command at a time, you will never hit the rate limit under normal use. This is why I made Gemini the default backend.

**Groq is also genuinely free.** 6,000 requests per day on the LLM endpoint, and similar limits for STT. If you want fast cloud inference with no local model setup and no money, Groq + Whisper-large-v3 for STT and Groq + Llama 3 for intent is a fully free, performant stack.

## The Piece I'm Proudest Of

The compound command handling. When you say "write a Python retry function and save it to utils/retry.py", the agent correctly identifies that this is a `write_code` intent (not `write_code` + `create_file` — because code writing implies file creation), extracts `utils/retry.py` as the filename, infers Python as the language, generates the function, creates the `utils/` subdirectory if it doesn't exist, and writes the file. All of that happens from twelve words of speech.

The path traversal guard runs on `utils/retry.py` as the filename, resolves it to an absolute path, and verifies it's inside `output/` before touching the filesystem. The subdirectory creation is automatic. The whole operation is atomic from the user's perspective.

That's the moment where the project felt less like a demo and more like something real.

## Running It Yourself

The project is structured to be cloneable and runnable in under ten minutes, assuming you have Python 3.10+ installed:

```bash
git clone https://github.com/akshat-2600/voice-agent.git
cd voice-agent
bash setup.sh          # creates venv, installs deps, copies .env
# Edit .env: add your GOOGLE_API_KEY
streamlit run app.py
```

For the LLM, the fastest path to working is:

1. Get a free Gemini API key from [aistudio.google.com](https://aistudio.google.com/)
2. Set `LLM_BACKEND=gemini` and `GOOGLE_API_KEY=your_key` in `.env`

For STT, Whisper `base` runs on any modern CPU. If you want faster transcription, get a free Groq key from [console.groq.com](https://console.groq.com/) and set `STT_BACKEND=groq`.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgu2sw3f3yfbigoab4tus.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fgu2sw3f3yfbigoab4tus.png)

## Closing Thoughts

Building this reinforced something I already suspected: the *easy* part of an AI agent is calling the LLM. The hard parts are everything around it — handling unexpected input gracefully, making state management work across a reactive UI framework, deciding where the safety boundaries are and enforcing them consistently, and writing the kind of prompt that reliably extracts structure from natural language.

The architecture I landed on is deliberately simple. Each layer does one thing: audio comes in, text comes out, intent is classified, tool runs, result is displayed. There's no magic. The LLM is a sophisticated text transformer sitting in the middle of a pipeline that, at its heart, is just a series of function calls.

If you build something on top of this or run into something I got wrong, I'd genuinely like to hear about it.

*Built with: Python, Streamlit, OpenAI Whisper, Google Gemini API, Groq, and more coffee than was probably advisable.*

[MongoDB](https://dev.to/mongodb)

Promoted

[![MongoDB Atlas image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FIf0YWd6.jpeg)](https://www.mongodb.com/cloud/atlas/lp/try3?utm_campaign=display_dev.to-broad_pl_flighted_atlas_tryatlaslp_prosp_gic-null_ww-all_dev_dv-all_eng_leadgen&utm_source=dev.to&utm_medium=display&utm_content=fastcode&bb=263708)

## 3 reasons why developers scale faster on MongoDB Atlas.

A flexible schema, integrated search, and automated global distribution so you can innovate and innovate with speed and agility. Build gen AI apps that run anywhere and scale everywhere.