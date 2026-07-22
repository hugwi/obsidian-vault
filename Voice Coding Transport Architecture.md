---
created: 2026-07-13
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - agentic-engineering
  - voice-coding
  - voice-agents
  - realtime-audio
  - webrtc
  - websocket
  - livekit
  - tailscale
  - networking
---

# Voice Coding Transport Architecture

Architecture notes from building a voice interface that routes spoken requests from Happy to coding agents. Related: [[Voice agent skills for coding assistants (01knfr34mg4644we46gp2svqc3)|Voice agent skills for coding assistants]], [[Networking]], [[Encryption]], [[TLS Protocol]], and [[Improving Performance with HTTP Streaming (01h0wsvvg3ddmjf3cv8wara2gb)|Improving Performance with HTTP Streaming]].

## Current prototype

```text
Happy phone
  -> Tailscale WireGuard tunnel
  -> Tailscale Serve (WSS)
  -> self-hosted LiveKit
  -> local voice worker
     -> Faster Whisper (STT)
     -> Qwen (routing/conversation)
     -> Kokoro (TTS)
     -> Happy coding session
```

The prototype is private and inexpensive, but its real-time media path depends on the phone maintaining a healthy direct Tailscale connection to the development machine.

## Reliability findings

- A direct Tailscale path was fast and voice worked normally.
- When the phone fell back to a DERP relay, LiveKit signaling experienced ping and WebSocket timeouts.
- Failed LiveKit rooms attempted to reconnect, leaving stale peer connections and tracks. Immediate retries then produced errors such as `could not establish pc connection`, `received leave request while trying to reconnect`, and negotiation timeouts.
- These failures happened before model inference. Recent healthy Qwen decisions completed in roughly 0.6 seconds; apparent model delays were often transport or reconnect delays.
- A fresh LiveKit `Room` should be used for each new session after failure. Reusing damaged room state compounds the problem.
- Voice Activity and native Happy conversation history are separate paths. Diagnostic events should remain visible while finalized voice turns are also encrypted and appended to the originating Happy conversation.

## Encryption layers

The layers are complementary rather than duplicates:

1. **Tailscale/WireGuard** protects and restricts access to the private network.
2. **TLS/WSS** protects LiveKit signaling.
3. **DTLS-SRTP** protects WebRTC media in transit.
4. **Happy session encryption** protects transcripts and messages when they are persisted and synchronized through Happy.

Voice audio does not pass through Happy's conversation synchronization path. It travels through LiveKit to a worker that must process the audio. Only the resulting transcript and assistant response are written into the encrypted Happy conversation.

DERP is Tailscale's encrypted fallback relay. It cannot inspect WireGuard traffic, but it adds another network hop and is less suitable for latency-sensitive, continuous media than a direct path.

## WebRTC versus WebSocket audio

### WebRTC

Benefits:

- UDP-oriented low-latency media transport.
- Built-in Opus negotiation, jitter buffering, packet-loss handling, congestion control, and secure media.
- ICE/STUN/TURN support for NAT traversal.
- Native support for tracks, subscriptions, multi-party rooms, and SFUs.
- Lost audio packets can be skipped instead of blocking newer audio.

Costs:

- ICE and peer-connection lifecycle are complex.
- Reliable remote hosting needs a public endpoint, TLS, UDP access, and usually TURN.
- Operating a global WebRTC service requires specialized monitoring and networking knowledge.

### Dedicated WebSocket audio

Benefits:

- Simpler outbound HTTPS-compatible connection.
- No ICE or TURN negotiation.
- Easier debugging and explicit reconnect semantics.
- Plausible for one phone talking to one agent.

Costs:

- TCP retransmission causes head-of-line blocking: one lost packet delays all later audio.
- We would own audio framing, codecs, jitter buffering, backpressure, reconnection, playback timing, interruptions, and mobile audio lifecycle.
- Audio should use a dedicated socket, not Happy's normal synchronization connection, to avoid delaying application messages.

WebRTC is the stronger default for production-quality real-time audio. A dedicated WebSocket transport is a valid future simplification if the product remains strictly one-user-to-one-agent and WebRTC operations become the larger cost.

## Hosting options

| Option | Strength | Main drawback |
|---|---|---|
| Local LiveKit over Tailscale | Private, self-hosted, no service bill | Mobile reliability depends on direct tailnet routing |
| LAN-only LiveKit | Fast and free on the same network | No remote access |
| Public self-hosted LiveKit | Open source and full control | Requires public infrastructure, TURN, TLS, security, monitoring, and bandwidth |
| LiveKit Cloud | Managed global WebRTC, TURN, observability, and scaling | Usage-based dependency on a vendor |
| Custom Happy WebSocket gateway | Full protocol control and simpler connection setup | We build and operate the complete audio transport layer |

LiveKit itself is open source. Replacing it with Janus, mediasoup, Pion, or Jitsi does not remove the need for public reachability, NAT traversal, TURN, TLS, and reliable hosting.

## LiveKit Cloud cost model

Pricing checked against [LiveKit's official pricing](https://livekit.com/pricing) on 2026-07-13.

- Build: $0/month, no credit card, 5,000 WebRTC participant-minutes and 1,000 hosted-agent minutes included.
- Ship: starts at $50/month, including 150,000 WebRTC participant-minutes and 5,000 hosted-agent minutes.
- Ship overage: $0.0005 per WebRTC participant-minute and $0.01 per hosted-agent minute.
- STT, TTS, and LLM inference are separate if purchased through LiveKit Inference.

With a self-hosted worker, one call minute generally consumes two participant-minutes: one for the phone and one for the worker. The free Build allowance therefore represents roughly 2,500 two-party voice minutes. After included usage, transport is approximately $0.001 per user voice minute.

Our local Faster Whisper, Qwen, and Kokoro services can continue to provide inference. In that configuration LiveKit Cloud supplies only media transport, so there is no LiveKit inference charge.

## Recommended evolution

### Development and early beta

- Use LiveKit Cloud's free transport tier.
- Keep Faster Whisper, Qwen, Kokoro, and the coding worker local.
- Move token issuance into Happy's authenticated backend.
- Issue short-lived, room-scoped tokens.
- Remove Tailscale and DERP from the user's media path while retaining Tailscale for development and administration.

### Private beta

- Deploy voice workers as replaceable cloud containers.
- Persist conversation, task, and delivery state outside worker memory.
- Add per-user quotas, latency metrics, retries, and durable result delivery.
- Keep model providers behind an abstraction so local, hosted, and customer-controlled inference can coexist.

### Production

- Autoscale workers close to media regions.
- Provide managed low-latency defaults with optional private inference.
- Track transport, STT, TTS, LLM, and coding-agent costs separately per user.
- Consider self-hosting LiveKit only when scale, economics, or compliance justify operating WebRTC and TURN infrastructure.

## Working recommendation

Use **LiveKit Cloud for transport**, **Happy for authenticated token issuance and durable conversation state**, and **our own model/worker stack initially**. This removes the unstable home-network path without forcing LiveKit-hosted inference or an immediate monthly bill.

Do not build the production user experience around a home-hosted LiveKit endpoint. Home power, ISP routing, VPN state, bandwidth, and one machine become a single shared failure domain.

## Open questions

- At what usage level does self-hosted public LiveKit become cheaper than managed transport after operational labor?
- Should production support LiveKit frame-level end-to-end encryption between Happy and the worker?
- Should a dedicated WebSocket audio prototype be benchmarked against WebRTC for one-user-to-one-agent latency and recovery?
- Which parts of the voice worker should remain local for privacy, and which should move close to users for latency and availability?
