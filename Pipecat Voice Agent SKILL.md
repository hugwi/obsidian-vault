---
categories:
  - "[[Resources]]"
domain: engineering
name: pipecat-voice-agent
description: >
  Build voice AI agents with Pipecat, SmallWebRTC, RTVI, and Docker.
  Use when the user is building a voice agent, real-time audio AI, WebRTC bot,
  or integrating Pipecat with a React frontend. Covers the full stack: pipeline
  architecture, Docker TURN relay, React audio handling, and RTVI protocol.
created: 2026-06-23
---

# Pipecat Voice Agent — Rules & Patterns

Distilled from hands-on experience building a production voice AI sales agent
with Pipecat v0.0.108 / client-js v1.7.0, SmallWebRTC, FastAPI, React, and Docker on macOS.

---

## 1. Pipecat Pipeline Rules

### Pipeline order is not negotiable

The correct order with RTVI:

```
transport.input()
  → RTVIProcessor          ← must be BEFORE STT (decodes send-text messages)
  → STT
  → context_aggregator.user()
  → LLM
  → TTS
  → transport.output()
  → context_aggregator.assistant()
  # RTVIObserver is NOT in the pipeline list — see below
```

### RTVIProcessor vs RTVIObserver are two separate objects

| Object | Direction | Where to put it |
|--------|-----------|----------------|
| `RTVIProcessor` | Inbound (client → bot) | In pipeline list, before STT |
| `RTVIObserver` | Outbound (bot → client) | In `PipelineParams(observers=[...])`, NOT pipeline list |

```python
rtvi = RTVIProcessor(transport=transport)
rtvi_observer = rtvi.create_rtvi_observer()

pipeline = Pipeline([..., rtvi, ...])   # RTVIProcessor in list

task = PipelineTask(
    pipeline,
    params=PipelineParams(observers=[rtvi_observer])  # RTVIObserver in params
)
```

Forgetting `rtvi_observer` → bot audio plays but transcript panel is always blank.

### Transcript accumulation uses context aggregator events

```python
@context_aggregator.user().event_handler("on_user_turn_stopped")
async def on_user_turn(frame_processor, strategy, message):
    session.add_turn("user", message.content)

@context_aggregator.assistant().event_handler("on_assistant_turn_stopped")
async def on_assistant_turn(frame_processor, message):
    session.add_turn("assistant", message.content)
```

### Post-call analysis must be fire-and-forget

```python
@transport.event_handler("on_client_disconnected")
async def on_disconnected(transport_, client):
    session.end()
    asyncio.create_task(_analyze_session(session.id))  # non-blocking
    await task.cancel()
```

### Never leave the transport open without a pipeline

If `run_bot()` returns early (e.g. missing API key), the WebRTC connection
stays alive but no bot ever sends `bot-ready` → client eventually receives a
"Fatal error". Always either start a fallback pipeline or disconnect explicitly.

```python
# BAD — orphaned transport
async def run_bot(conn, mode="ultravox"):
    if not cfg.ultravox_api_key:
        logger.error("missing key")
        return  # transport still open, client hangs

# GOOD — fall back
async def run_bot(conn, mode="ultravox"):
    if mode == "ultravox" and not cfg.ultravox_api_key:
        logger.warning("falling back to cascaded pipeline")
        asyncio.create_task(_run_cascaded_pipeline(conn))
    else:
        asyncio.create_task(_run_ultravox_pipeline(conn))
```

---

## 2. RTVI Protocol Rules

### Use `startBotAndConnect()`, not `connect()` with endpoint

In `@pipecat-ai/client-js` v1.7.0+, passing an endpoint to `connect()` is
deprecated. Use `startBotAndConnect()` instead:

```typescript
// DEPRECATED — logs warning
await client.connect({ endpoint: '/start?mode=cascaded' })

// CORRECT
await client.startBotAndConnect({ endpoint: '/start?mode=cascaded' })
```

Both accept the same `APIRequest` type. The method name is the only change.

### Use `BotOutput` not `BotTranscript`

```typescript
// DEPRECATED
client.on(RTVIEvent.BotTranscript, handler)

// CORRECT
client.on(RTVIEvent.BotOutput, (data) => {
  handler(data.text, true)
})
```

`UserTranscript` (for user speech-to-text) is still current and not deprecated.

### The two-URL TURN pattern

Backend and browser use different URLs to reach the same coturn container:

```
Backend env:  TURN_SERVER_URL=turn:coturn:3478      (Docker service DNS)
Browser:      turn:localhost:3478                   (Docker port forward)
```

Return the browser-facing URL from `/start`:

```python
@router.post("/start")
async def start():
    cfg = get_settings()
    ice_servers = [{"urls": ["stun:stun.l.google.com:19302"]}]
    if cfg.turn_client_url:
        ice_servers.append({
            "urls": cfg.turn_client_url,   # ← localhost URL for browser
            "username": cfg.turn_username,
            "credential": cfg.turn_credential,
        })
    return {"sessionId": str(uuid.uuid4()), "iceConfig": {"iceServers": ice_servers}}
```

### SmallWebRTCTransport connect() URL routing

`client.startBotAndConnect({ endpoint: '/start' })` calls `/start`, reads
`sessionId` from the response, then builds the offer URL automatically as
`/sessions/{sessionId}/api/offer`. Add a shim route:

```python
@router.api_route("/sessions/{session_id}/{path:path}", methods=["POST", "PATCH"])
async def session_proxy(session_id: str, path: str, request: Request):
    if path == "api/offer":
        if request.method == "POST": ...  # handle offer
        if request.method == "PATCH": ... # handle ICE candidates
```

---

## 3. Docker WebRTC Rules (macOS)

### coturn is mandatory on macOS Docker

Docker Desktop on macOS uses a Linux VM. `network_mode: host` doesn't work
(Linux-only). Container IPs (172.x.x.x) are unreachable from the macOS browser.
A TURN relay is the only solution.

### coturn service template

```yaml
coturn:
  image: coturn/coturn:latest
  restart: unless-stopped
  ports:
    - "127.0.0.1:3478:3478"
    - "127.0.0.1:3478:3478/udp"
    - "127.0.0.1:39000-39050:39000-39050/udp"  # relay media range
  entrypoint: []    # REQUIRED: bypass broken docker-entrypoint.sh
  command:
    - "sh"
    - "-c"
    - |
      HOST=$(getent hosts host.docker.internal | awk '{print $1}')
      [ -z "$HOST" ] && HOST=0.0.0.0
      exec turnserver -n --log-file=stdout \
        --listening-ip=0.0.0.0 \
        --external-ip=$HOST \
        --min-port=39000 --max-port=39050 \
        --no-dtls --no-tls \
        --lt-cred-mech \
        --realm=myapp.local \
        --user=myuser:mypassword
```

**Why `entrypoint: []` is required**: coturn's `docker-entrypoint.sh` does
`eval "echo $i"` on each command argument, executing any embedded shell
subexpressions. Bypassing the entrypoint avoids this.

**Why `--lt-cred-mech` not `--auth-secret`**: Static credentials
(`username:password`) are simpler for dev. HMAC auth (`--auth-secret`) requires
a shared secret file mounted into the container and time-based token generation
on the client side — more complex and unnecessary for local dev.

### `--external-ip` must be `host.docker.internal` resolved IP

`192.168.65.254` is the standard `host.docker.internal` IP in Docker Desktop
on macOS. This IP is reachable from both:
- The macOS host (browser) — because it's a Docker Desktop virtual interface
- All Docker containers — because it's the host gateway

Using `0.0.0.0` as external-ip would advertise container-internal IPs instead.

### Port range: expose enough relay ports

Each active WebRTC session uses 2 UDP ports (one per media direction). Expose
at least `N*2 + buffer` ports where N is your expected concurrent sessions.
`39000-39050` = 51 ports = ~25 simultaneous sessions.

---

## 4. Frontend Audio Rules (React)

### Always intercept getUserMedia to strip video

`SmallWebRTCTransport` uses `DailyMediaManager` internally. During device
enumeration, it calls `getUserMedia({video: true})` regardless of `enableCam`.
Without interception, the browser shows a camera permission prompt and if
denied, bot audio is never wired up.

```typescript
// In lib/pipecat.ts — runs at module load time, before any client is created
if (typeof navigator !== 'undefined' && navigator.mediaDevices) {
  const _gum = navigator.mediaDevices.getUserMedia.bind(navigator.mediaDevices)
  navigator.mediaDevices.getUserMedia = (constraints?) => {
    const safe = constraints ? { ...constraints, video: false } : constraints
    if (!safe?.audio) return Promise.resolve(new MediaStream())
    return _gum(safe)
  }
}
```

### Always add a TrackStarted fallback for bot audio

Even after fixing getUserMedia, `DailyMediaManager` can fail silently leaving
the remote audio track unattached (bot speaks but user hears nothing).

```typescript
client.on(RTVIEvent.TrackStarted, (track: MediaStreamTrack, participant: any) => {
  if (track.kind === 'audio' && !participant?.local) {
    let el = document.getElementById('pipecat-bot-audio') as HTMLAudioElement
    if (!el) {
      el = document.createElement('audio')
      el.id = 'pipecat-bot-audio'
      el.autoplay = true
      document.body.appendChild(el)
    }
    el.srcObject = new MediaStream([track])
    el.play().catch(() => undefined)
  }
})
```

Note: `participant` can be `undefined` — use `!participant?.local` not
`participant && !participant.local` (the latter evaluates false for undefined).

### Text input mode

The Pipecat `sendText()` API injects user messages into the pipeline directly,
bypassing STT. Bot still speaks TTS back:

```typescript
await client.sendText(text)
```

On the backend, `RTVIProcessor` handles the `send-text` RTVI message and
injects it as an `LLMMessagesAppendFrame` into the pipeline.

---

## 5. Version-Specific Gotchas

### `@pipecat-ai/client-js` v1.7.0

| Old API | New API |
|---------|---------|
| `RTVIClient` | `PipecatClient` |
| `RTVIClientOptions` | `PipecatClientOptions` |
| `client.connect({ endpoint })` | `client.startBotAndConnect({ endpoint })` |
| `RTVIEvent.BotTranscript` | `RTVIEvent.BotOutput` |

### Pipecat Python SDK (v0.0.108)

- `RTVIObserver` is exported from `pipecat.processors.frameworks.rtvi.processor`
  (not its own module): `from pipecat.processors.frameworks.rtvi.processor import RTVIProcessor, RTVIObserver`
- `RTVIObserver` goes in `PipelineParams(observers=[...])`, not in the pipeline list
- The Python SDK still emits `botTranscript` RTVI events alongside `botOutput`,
  causing a deprecation warning in the browser console. This is cosmetic only.

---

## 6. Checklist for a New Voice Agent

- [ ] Pipeline order: `input → RTVIProcessor → STT → user_agg → LLM → TTS → output → assistant_agg`
- [ ] `RTVIObserver` in `PipelineParams(observers=[...])`, not pipeline
- [ ] `startBotAndConnect()` in frontend (not `connect()`)
- [ ] `RTVIEvent.BotOutput` listener for transcript (not deprecated `BotTranscript`)
- [ ] `getUserMedia` interception strips video at module level
- [ ] `RTVIEvent.TrackStarted` fallback creates `<audio>` element for remote track
- [ ] coturn service with `entrypoint: []` and `--lt-cred-mech`
- [ ] coturn `--external-ip` set to `host.docker.internal` resolved IP
- [ ] Backend `/start` endpoint returns `iceConfig.iceServers` with `turn:localhost:XXXX`
- [ ] Backend `run_bot()` never leaves transport open without starting a pipeline
- [ ] Session transcript accumulated via context aggregator events, not RTVI events
- [ ] Post-call analysis wrapped in `asyncio.create_task()` (non-blocking)
- [ ] Check `lsof -i :PORT` before starting Docker to ensure no native process holds the port
