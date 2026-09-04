---
categories:
  - "[[Raw]]"
title: "PunithVT/ai-avatar-system: 🎭 AI Avatar / digital human platform — upload a photo, clone a voice, talk to any face in real time with lip-sync video. Open-source, self-hosted. Claude · Whisper · Chatterbox"
source: "https://github.com/PunithVT/ai-avatar-system"
author:
published:
created: "2026-08-01"
description: "🎭 AI Avatar / digital human platform — upload a photo, clone a voice, talk to any face in real time with lip-sync video. Open-source, self-hosted. Claude · Whisper · Chatterbox · MuseTalk. - PunithVT/ai-avatar-system"
tags:
  - raw
  - "clip/video"
  - "video-gen"
  - "voice-ai"
---
## 🎭 AvatarAI — Real-Time AI Avatar Platform

**Upload a photo · Clone a voice · Talk to any face in real time**

[Quick Start](#-quick-start) · [Features](#-features) · [Architecture](#-architecture) · [GPU / AWS Deploy](#-gpu--aws-deployment) · [API](#-api-reference) · [Roadmap](#-roadmap)

> **The most complete open-source AI avatar / digital human system.** Real-time talking-head lip-sync · Zero-shot voice cloning · Multi-LLM · Runs 100% locally or on AWS.

---

## 🎬 What is AvatarAI?

AvatarAI is an open-source, production-ready platform for building **photorealistic AI avatar conversations**. Upload any face photo, clone a voice from a 5-second audio clip, and have a real-time conversation — with **lip-sync video generated on every single response**.

```
[mic] → Whisper STT → Claude / GPT / Ollama (streaming) → Chatterbox TTS → MuseTalk lip-sync → [video]
                              < 2–4 s to first video chunk on AWS GPU >
```

**What makes AvatarAI different:**

- 🎤 **Zero-shot voice cloning** — 10 seconds of audio is all you need (Chatterbox Multilingual)
- 🎭 **Any face, any language** — upload a JPEG, pick from 23 languages, start talking
- ⚡ **Token-streaming pipeline** — the LLM streams live tokens while TTS + lip-sync run per sentence; the first video chunk plays before the model finishes its reply
- ✋ **Barge-in** — speak (or hit stop) mid-reply and the avatar yields instantly, like a real conversation
- 🔒 **100% local mode** — local storage, local Whisper, local LLM via Ollama: nothing leaves your machine
- 🔌 **Multi-LLM** — Claude (with prompt caching), GPT-4o, or any local model via Ollama / vLLM / LM Studio
- 🚀 **AWS GPU deployment** — one-command deploy to `g5.xlarge` for true real-time (~30 FPS)
- 🏗️ **Production-grade** — JWT + httpOnly-cookie auth, per-user rate limiting, Postgres + Alembic, S3/CloudFront, Prometheus, CI, a real test suite — the only project in this niche you can ship as a product, not just a demo

---

## ⚔️ How AvatarAI compares

|  | **AvatarAI** | Duix-Avatar | Linly-Talker | AIAvatarKit |
| --- | --- | --- | --- | --- |
| Real-time conversation | ✅ WebSocket streaming | ❌ offline video gen | ✅ (Gradio / WebRTC spin-off) | ✅ |
| Lip-sync video | ✅ MuseTalk V1.5 | ✅ proprietary models | ✅ multiple engines | ❌ (drives external avatars) |
| Voice cloning | ✅ 10 s, 23 languages | ✅ | ✅ | ❌ |
| Barge-in / interruption | ✅ | ❌ | ✅ (stream variant) | ✅ |
| Local / free LLM | ✅ Ollama, vLLM | ❌ | ✅ | ✅ |
| Web app with auth & history | ✅ Next.js + JWT + Postgres | ❌ Windows client | ❌ Gradio demo UI | ❌ library |
| Rate limiting, CI, tests, IaC | ✅ | ❌ | ❌ | ❌ |
| License | MIT | custom | MIT | Apache-2.0 |

> Toolkits like Linly-Talker are great research playgrounds; Duix ships a Windows product. **AvatarAI is the one you can deploy as a real multi-user web service.**

---

## ✨ Features

| Category | Details |
| --- | --- |
| 🤖 **LLM Backends** | Claude (prompt-cached) · GPT-4o · **Ollama / vLLM / LM Studio (local, free)** |
| 🎤 **Voice Cloning** | Record 10–60 s → Chatterbox Multilingual zero-shot cloning |
| 🗣️ **Speech-to-Text** | Whisper (`faster-whisper`, CUDA), decodes browser WebM natively |
| 🎬 **Lip-Sync Video** | MuseTalk V1.5 persistent worker (30 FPS on GPU) · FFmpeg fallback (CPU) |
| ⚡ **Streaming Pipeline** | Live LLM tokens + per-sentence video chunks over WebSocket |
| ✋ **Barge-In** | Speak or hit stop mid-reply — in-flight turn cancels in ms |
| 🔉 **TTS Fallback Chain** | chatterbox → edge-tts (free neural voices) → gTTS — never silent |
| 😊 **Emotion Detection** | Live emotion badges per message |
| 🌍 **23 Languages** | Whisper multilingual STT + Chatterbox multilingual TTS |
| 🏠 **Local-First Storage** | `USE_LOCAL_STORAGE=true` — no AWS needed for dev |
| 🔐 **Auth & Sessions** | JWT authentication, conversation history, persistent sessions |
| 📊 **Observability** | Prometheus · Celery Flower · Sentry · structured logging |
| 🧪 **Tested** | Full pytest suite — users, avatars, sessions, health checks |
| 🚀 **AWS GPU Deploy** | One-command `g5.xlarge` deploy with CUDA 11.8 + float16 |

---

## 🏗️ Architecture

```nix
┌──────────────────────────────────────────────────────────────┐
│                        Browser / Client                       │
│  ┌─────────────┐  ┌──────────────┐  ┌──────────────────────┐ │
│  │Avatar Studio│  │ Voice Studio │  │   Chat Interface     │ │
│  │  (upload)   │  │  (cloning)   │  │ Idle anim + chunks   │ │
│  └──────┬──────┘  └──────┬───────┘  └──────────┬───────────┘ │
└─────────┼───────────────┼─────────────────────┼─────────────┘
          │ REST           │ REST                │ WebSocket
          ▼                ▼                     ▼
┌──────────────────────────────────────────────────────────────┐
│                       FastAPI Backend                         │
│  ┌──────────────────────────────────────────────────────┐    │
│  │                  WebSocket Manager                    │    │
│  │  split sentences → TTS → MuseTalk → stream chunks    │    │
│  └──────────────────────────────────────────────────────┘    │
│  ┌──────────┐ ┌───────────┐ ┌──────────┐ ┌───────────────┐  │
│  │  Whisper │ │Claude/GPT │ │ XTTS v2  │ │  MuseTalk     │  │
│  │   STT    │ │  / Llama  │ │   TTS    │ │  (GPU/CPU)    │  │
│  └──────────┘ └───────────┘ └──────────┘ └───────────────┘  │
│  ┌──────────┐ ┌──────────┐  ┌──────────┐ ┌───────────────┐  │
│  │PostgreSQL│ │  Redis   │  │  Celery  │ │ Local FS / S3 │  │
│  └──────────┘ └──────────┘  └──────────┘ └───────────────┘  │
└──────────────────────────────────────────────────────────────┘
```

### Real-Time Data Flow (one conversation turn)

```
[User types / speaks]
        │
        ▼
  Whisper STT ─────────────────► transcript
        │
        ▼
  Claude / GPT / Llama ────────► full response text
        │
        ▼
  Split into sentences ────────► ["Hello!", "How are you?", ...]
        │
        ├── sentence 1 → XTTS → MuseTalk → video_chunk WS → browser plays
        ├── sentence 2 → XTTS → MuseTalk → video_chunk WS → queued
        └── sentence N → XTTS → MuseTalk → video_chunk WS → queued
```

---

## 📁 Project Structure

```nix
ai-avatar-system/
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── api/v1/             # REST endpoints (users, avatars, sessions, messages)
│   │   ├── services/           # Core services (LLM, TTS, STT, animator, storage)
│   │   ├── models/             # SQLAlchemy DB models
│   │   └── websocket.py        # Real-time WebSocket handler + sentence streaming
│   ├── alembic/                # Database migrations
│   ├── models/MuseTalk/        # MuseTalk V1.5 (lip-sync engine)
│   │   └── scripts/
│   │       └── musetalk_worker.py  # Persistent worker (models loaded once)
│   ├── tests/                  # pytest suite
│   ├── Dockerfile              # CUDA 11.8 base image
│   └── requirements.txt
├── frontend/                   # Next.js 14 application
│   ├── app/                    # App Router pages
│   ├── components/             # React components (ChatInterface, IdleAvatar, etc.)
│   ├── lib/api.ts              # Axios API client
│   └── store/                  # Zustand global state
├── nginx/
│   └── nginx.conf              # Reverse proxy (HTTP → backend/frontend, WebSocket)
├── infrastructure/
│   ├── main.tf                 # AWS Terraform (ECS, RDS, ElastiCache, S3, CloudFront)
│   └── variables.tf
├── scripts/
│   ├── setup_musetalk.sh       # Download MuseTalk models (~9 GB)
│   └── deploy-aws.sh           # One-command EC2 GPU deployment
├── docker-compose.yml          # Development (CPU) — all services
├── docker-compose.prod.yml     # Production overrides (GPU, no bind mounts, logging)
├── deploy.sh                   # ECR push + Terraform deploy (ECS path)
├── .env.example                # Development env template
└── .env.prod.example           # Production env template
```

---

## 🚀 Quick Start

### Prerequisites

- **Docker & Docker Compose** v2+ (recommended)
- OR: Python 3.10+, Node.js 18+, FFmpeg, PostgreSQL, Redis

### Option A — Docker / CPU (development)

```bash
git clone https://github.com/PunithVT/ai-avatar-system.git
cd ai-avatar-system
cp .env.example .env          # add your ANTHROPIC_API_KEY (or OPENAI_API_KEY)
docker compose up -d
```

| Service | URL |
| --- | --- |
| 🖥️ Frontend | [http://localhost:3000](http://localhost:3000/) |
| ⚙️ Backend API | [http://localhost:8000](http://localhost:8000/) |
| 📖 Swagger Docs | [http://localhost:8000/docs](http://localhost:8000/docs) |
| 🌸 Celery Flower | [http://localhost:5555](http://localhost:5555/) |

> **No AWS required.** Set `USE_LOCAL_STORAGE=true` (default) — uploads saved to `backend/uploads/`.

**Want something to talk to immediately?** Seed three ready-made demo avatars (AI-generated faces + personalities):

```nix
backend/venv/bin/python scripts/seed_demo.py            # or any python with \`requests\`
backend/venv/bin/python scripts/seed_demo.py --with-voices   # + cloned demo voices
```

Prebuilt images are also published on every release — `ghcr.io/punithvt/ai-avatar-system-backend` and `…-frontend`.

### Option B — Manual (development)

```bash
# Backend
cd backend
python -m venv venv && source venv/bin/activate
pip install -r requirements.txt
cp ../.env.example ../.env
alembic upgrade head
uvicorn main:app --reload --port 8000

# Frontend (new terminal)
cd frontend
npm install
npm run dev
```

### Option C — Enable MuseTalk Lip-Sync

```
# Download models (~9 GB, one-time)
bash scripts/setup_musetalk.sh

# Set in .env
AVATAR_ENGINE=musetalk

# Restart
docker compose restart backend
```

---

## 🚀 GPU & AWS Deployment

MuseTalk achieves **30 FPS at 256×256 on a V100-class GPU** (source: [MuseTalk paper](https://arxiv.org/abs/2410.10122)). On CPU it is 30–50× slower. Deploying on AWS gets you genuine real-time performance.

### Recommended Instance

| Instance | GPU | VRAM | Spot $/hr | MuseTalk FPS |
| --- | --- | --- | --- | --- |
| `g4dn.xlarge` | T4 | 16 GB | ~$0.16 | ~15–20 FPS |
| `g5.xlarge` | A10G | 24 GB | ~$0.30 | **~30 FPS** ✓ |
| `g6.xlarge` | L4 | 24 GB | ~$0.24 | **~30 FPS** ✓ |

**Recommended: `g5.xlarge` Spot** (~$72/mo at 8 hrs/day).

### One-Command EC2 Deploy

```
# 1. Launch g5.xlarge with Ubuntu 22.04 LTS, SSH in, then:
bash <(curl -fsSL https://raw.githubusercontent.com/PunithVT/ai-avatar-system/main/scripts/deploy-aws.sh)

# 2. Fill in API keys:
nano /opt/ai-avatar-system/.env.prod

# 3. Redeploy with your keys:
bash /opt/ai-avatar-system/scripts/deploy-aws.sh --update
```

The script automatically:

- Installs Docker + nvidia-docker2
- Verifies GPU is accessible
- Downloads MuseTalk models (~9 GB)
- Starts all services with GPU passthrough + float16 (2× faster via Tensor Cores)

### Manual Production Docker

```
cp .env.prod.example .env.prod   # fill in your values
docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d
```

**What `docker-compose.prod.yml` adds over development:**

- GPU reservation (`nvidia` driver, count=1) for backend + celery-worker
- `float16` inference enabled automatically on CUDA → ~2× speedup
- Persistent `musetalk_models` volume (survive container restarts)
- No source-code bind mounts (runs from built image)
- Log rotation (100 MB max, 5 files)
- Flower disabled (security)

### Verify GPU is Working

```
# Check GPU is visible in container
docker exec avatar-backend python -c "
import torch
print('CUDA:', torch.cuda.is_available())
print('GPU:', torch.cuda.get_device_name(0))
print('VRAM:', round(torch.cuda.get_device_properties(0).total_memory/1024**3,1), 'GB')
"

# Expected on g5.xlarge:
# CUDA: True
# GPU: NVIDIA A10G
# VRAM: 24.0 GB

# Live GPU utilisation
docker exec avatar-backend nvidia-smi
```

### AWS Terraform (ECS Path)

For a fully managed ECS deployment with RDS + ElastiCache + CloudFront:

```
cd infrastructure
terraform init
terraform apply -var="environment=production"
bash deploy.sh production
```

---

## 🎤 Voice Cloning

Powered by [Chatterbox Multilingual](https://github.com/resemble-ai/chatterbox) (Resemble AI) — zero-shot voice cloning from a 10-second sample, in 23 languages.

1. Go to **Voice** tab → **Clone Voice**
2. Record 10–60 s of clear speech (or upload a WAV/MP3/WebM)
3. Name it → **Clone** → select it for your session

Every TTS response then uses your cloned voice.

```powershell
# REST API
curl -X POST http://localhost:8000/api/v1/voices/clone \
  -F "audio=@my_voice.wav" -F "name=My Voice" -F "language=en"
```

---

## 📡 API Reference

### Authentication

```
POST /api/v1/users/register   { "email": "...", "username": "...", "password": "..." }
POST /api/v1/users/login      form: username=... password=...   → { "access_token": "..." }

# All protected routes:
Authorization: Bearer <access_token>
```

### Avatars

```bash
POST   /api/v1/avatars/upload        Upload photo (multipart: file + name)
GET    /api/v1/avatars/              List avatars
DELETE /api/v1/avatars/{id}          Delete avatar
PUT    /api/v1/avatars/{id}/voice    Assign voice to avatar
```

### Sessions & Messages

```bash
POST   /api/v1/sessions/create       { "avatar_id": "..." }
POST   /api/v1/sessions/{id}/end
GET    /api/v1/messages/session/{id}
```

### WebSocket

```
WS  /ws/session/{session_id}
```

**Client → Server:**

```json
{ "type": "text",         "text": "Hello!" }
{ "type": "audio",        "audio": "<base64-webm>" }
{ "type": "stop" }                                  // barge-in: cancel the in-flight reply
{ "type": "set_voice",    "voice_id": "<uuid>" }    // attach a cloned voice (owner-checked)
{ "type": "set_language", "language": "es" }
{ "type": "ping" }
```

**Server → Client:**

```json
{ "type": "token",            "token": "Hel" }       // live LLM stream
{ "type": "transcription",    "text": "Hello!" }
{ "type": "message",          "content": "Hi!", "role": "assistant" }
{ "type": "video_chunk_start","total_chunks": -1 }   // -1 = streaming, total unknown
{ "type": "video_chunk",      "chunk_index": 0, "video_url": "...", "text": "Hi!" }
{ "type": "video_chunk_end",  "sent_chunks": 3 }
{ "type": "status",           "message": "Animating…", "stage": "animation" }
{ "type": "tts_fallback",     "engine": "edge-tts", "voice_cloned": false, "message": "…" }
{ "type": "interrupted",      "message": "Previous response interrupted" }
{ "type": "error",            "message": "Something went wrong" }
```

---

## ⚙️ Configuration

Key `.env` variables:

```makefile
# LLM
LLM_PROVIDER=anthropic            # anthropic | openai | ollama (local & free)
LLM_MODEL=claude-sonnet-4-6       # or gpt-4o · llama3.1 · qwen2.5 …
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_BASE_URL=                  # e.g. http://localhost:11434/v1 for Ollama / vLLM / LM Studio

# Avatar engine
AVATAR_ENGINE=musetalk            # musetalk (GPU recommended) | simple (CPU fallback)
MUSETALK_PATH=models/MuseTalk

# TTS — automatic fallback chain: chatterbox → edge-tts → gtts
TTS_PROVIDER=chatterbox

# STT
WHISPER_MODEL=large-v3-turbo      # tiny | base | small | medium | large-v3 | large-v3-turbo

# Storage
USE_LOCAL_STORAGE=true            # false → AWS S3 (+ presigned URLs / CloudFront)
S3_BUCKET_NAME=...

# Auth (≥32 chars enforced at boot)
SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
JWT_SECRET_KEY=$(python -c "import secrets; print(secrets.token_hex(32))")
JWT_EXPIRATION_HOURS=24
```

---

## 🛠️ Tech Stack

### Frontend

| Library | Purpose |
| --- | --- |
| Next.js 14 + React 18 | App framework |
| TypeScript 5 | Type safety |
| Tailwind CSS | Styling |
| Zustand | Global state |

### Backend

| Library | Purpose |
| --- | --- |
| FastAPI | Async REST API + WebSocket |
| SQLAlchemy 2 (async) | ORM with asyncpg |
| PostgreSQL 15 | Primary database |
| Alembic | Migrations |
| Redis 7 | Cache + Celery broker |
| Celery | Background tasks |

### AI / ML

| Model | Purpose |
| --- | --- |
| Claude / GPT-4o / Ollama (local) | LLM conversation |
| Whisper (`faster-whisper`) | Speech-to-text |
| Chatterbox Multilingual (Resemble AI) | TTS + zero-shot voice cloning, 23 languages |
| Edge TTS → gTTS | Free no-GPU fallback voices |
| MuseTalk V1.5 | Photorealistic lip-sync (30 FPS on GPU) |

---

## 🧪 Running Tests

```
cd backend
pytest -v                           # all tests
pytest tests/test_health.py         # single module
pytest --cov=app --cov-report=html  # HTML coverage
```

---

## 📰 What's New

- **2026-06** — Edge-TTS neural fallback chain · local LLMs via Ollama/vLLM · demo avatar seeding · prebuilt GHCR images · cascade-delete + WebM-STT + 429 fixes · SEO/metadata pass
- **2026-05** — httpOnly-cookie auth (XSS-safe) · conversation resume from history · end-to-end WebSocket tests · perf indexes (migration 0002)
- **2026-03** — Chatterbox Multilingual replaces XTTS v2 (23 languages) · MuseTalk persistent worker (models load once) · barge-in interruption · live token streaming

---

## 🗺️ Roadmap

- **Streaming LLM** — TTS + lip-sync start before the LLM finishes (token-by-token) ✅
- **Barge-in** — interrupt the avatar mid-reply by speaking ✅
- **Local LLMs** — Ollama / vLLM / LM Studio via OpenAI-compatible API ✅
- **Hands-free mode** — VAD-driven always-listening with auto end-of-turn (no tap-to-record)
- **WebRTC streaming** — sub-second full-duplex audio/video instead of chunked MP4
- **Wav2Lip engine** — lighter lip-sync option for weaker GPUs
- **Emotion-driven animation** — detected emotion changes facial expression
- **Embeddable widget** — drop a talking avatar into any website with 3 lines of JS
- **Long-term memory** — RAG + vector DB for persistent context
- **UI i18n** — the pipeline speaks 23 languages; the UI should too

---

## ❓ FAQ

**Do I need a GPU?**

No — everything runs on CPU. MuseTalk takes 30–90 s/sentence on CPU (the `simple` engine is instant). For real-time lip-sync, use an AWS `g5.xlarge` (~$0.30/hr spot) or any 16 GB+ NVIDIA card.

**Can I run it with no API key, fully offline?**

Yes — set `LLM_PROVIDER=ollama`, run [Ollama](https://ollama.com/) (`ollama run llama3.1`), and you have a fully local, free conversation stack: Whisper STT, local LLM, Chatterbox TTS, MuseTalk video.

**How do I get something to talk to quickly?**

Run `python scripts/seed_demo.py` — it creates three demo avatars (AI-generated faces, distinct personalities) and optionally cloned demo voices with `--with-voices`.

**How do I get MuseTalk models?**

Run `bash scripts/setup_musetalk.sh` — downloads ~9 GB of models automatically.

**Why does the first response take longer?**

The MuseTalk persistent worker loads all models into GPU VRAM on the first request (~60 s on GPU, ~5 min on CPU). Subsequent requests reuse the loaded models.

**What happens if the TTS model can't load?**

The pipeline degrades gracefully: chatterbox → **edge-tts** (free Microsoft neural voices) → gTTS. The UI shows a one-time notice when a cloned voice couldn't be applied.

**What avatar photo works best?**

A clear, well-lit frontal face photo (JPEG/PNG/WebP). Avoid sunglasses or heavy occlusion.

---

## 🤝 Contributing

Contributions welcome! Read [CONTRIBUTING.md](https://github.com/PunithVT/ai-avatar-system/blob/main/CONTRIBUTING.md) before opening a PR.

```bash
git clone https://github.com/PunithVT/ai-avatar-system.git
git checkout -b feat/my-feature
# make changes + tests
git commit -m "feat(backend): add my feature"
git push origin feat/my-feature
```

---

## 📄 License

MIT © 2026 — see [LICENSE](https://github.com/PunithVT/ai-avatar-system/blob/main/LICENSE) for details.

---

**If AvatarAI saves you time or inspires your project, please ⭐ star the repo.**

[![Star History Chart](https://camo.githubusercontent.com/32dc05d783478ac8ba4cb0ed135e4c96ec13783d92c4eb17d1c22ea4a00f1ff9/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d50756e69746856542f61692d6176617461722d73797374656d26747970653d44617465)](https://star-history.com/#PunithVT/ai-avatar-system&Date)

<sub>Built with FastAPI · Next.js · MuseTalk V1.5 · Chatterbox · Whisper · Claude AI</sub>