---
title: "Teaching an LLM to Watch Video: A General-Purpose Pattern for Frame-Level AI Analysis"
source: "https://dev.to/littler00t/teaching-an-llm-to-watch-video-a-general-purpose-pattern-for-frame-level-ai-analysis-2phm"
author:
  - "[[dev.to]]"
published: "2026-02-28"
created: "2026-08-01"
description: "How a personal frustration with workout form turned into a reusable MCP server for video... Tagged with ai, mcp, llm, openai."
tags:
  - "clippings"
  - "clip/video"
  - "video-gen"
---
*How a personal frustration with workout form turned into a reusable MCP server for video intelligence*

---

I got back into pilates exercises this year after a long break. The problem with training alone is obvious to anyone who has done it: you cannot see yourself. You know something feels off in your squat — a subtle forward lean, a knee tracking inward at the bottom — but without a coach watching, you are guessing. So I started recording my sessions.

Recording helped, but only partially. I now had footage, but reviewing it was its own friction. Scrubbing through videos on my phone, pausing, rewinding, trying to hold a mental image of rep three while watching rep seven. I found myself thinking: this is exactly the kind of visual pattern-matching task that a multimodal LLM should be able to help with.

What followed was a design process that started with a narrow personal problem and ended somewhere much more interesting: a general-purpose pattern for giving LLMs the ability to *reason about video* at a level of precision and efficiency that the obvious approaches do not deliver. The result is an open-source MCP server — `mcp-video-server` — with 14 tools covering frame extraction, motion analysis, scene detection, annotation, and audio transcription.

This post documents that journey — the problem, the core insight, the pattern that emerged, and what the server can actually do.

---

## The Problem With Video and LLMs

Modern vision-capable LLMs are genuinely impressive at analysing images. Give Claude a photograph and ask it to assess posture, identify objects, or measure angles — and you will get a thoughtful, accurate response.

Video is harder. Not because LLMs cannot process frames from video — they can — but because the naive approach fails in practice. The naive approach is: extract every frame, send them all to the model, ask for analysis.

This breaks for three reasons.

**Context window limits.** A 5-second clip at 30fps is 150 frames. At anything close to full resolution, you cannot fit 150 images into a context window. You can downsample aggressively, but then you lose the spatial detail that makes form analysis meaningful.

**Cost and latency.** Even if you could fit 150 frames, you would not want to. Sending 150 images per analysis request is expensive and slow. For an interactive tool — the kind where you want to iterate, zoom in, ask follow-up questions — this is a non-starter.

**The model does not know *when* to look.** Without temporal context, the LLM cannot distinguish between a frame that captures the critical moment (bar at maximum depth, knee at full extension) and a transitional frame showing nothing interesting. It must process everything with equal attention.

What was missing was a tool designed around *how an LLM reasons*, not around how a video editor works.

---

## The Core Insight: Hierarchical Temporal Inspection

When a knowledgeable human reviews training footage, they do not watch it frame by frame. They follow a natural hierarchy:

1. **Skim** — watch the clip at speed to understand its overall structure. How many reps? Where does each rep start and end? Is there a section where something looks different?
2. **Zoom** — scrub into the section of interest. Watch the descent phase more slowly. Find the moment where the knee starts to drift.
3. **Freeze** — pause at the critical frame. Study it. Measure the angle. Compare it to another rep.

The key design decision was to mirror this workflow exactly in the tool interface, and to make each stage return information in a format the LLM can natively reason about — not file paths on disk, but actual images embedded directly in the tool response.

### The Timestamped Grid Composite

The central representation is the **timestamped frame grid**. Instead of returning individual frames, the overview and section tools composite multiple frames into a single image, with the timestamp of each frame rendered directly onto its cell.

```
┌─────────────┬─────────────┬─────────────┬─────────────┬─────────────┐
│  0:00.00    │  0:00.25    │  0:00.51    │  0:00.76    │  0:01.01    │
│  [frame]    │  [frame]    │  [frame]    │  [frame]    │  [frame]    │
├─────────────┼─────────────┼─────────────┼─────────────┼─────────────┤
│  0:01.27    │  0:01.52    │  0:01.77    │  0:02.03    │  0:02.28    │
│  [frame]    │  [frame]    │  [frame]    │  [frame]    │  [frame]    │
└─────────────┴─────────────┴─────────────┴─────────────┴─────────────┘
```

This single image communicates two things simultaneously: *what is in each frame* and *when in the video it occurs*. The LLM can respond with precise temporal references — "the knee starts drifting inward at approximately 1.52 seconds" — and immediately use that timestamp to drive the next tool call.

The timestamps are burned into the pixels, not attached as separate metadata. This matters because LLMs reason about what they see. Embedding the temporal information visually means it participates directly in the model's visual reasoning rather than sitting in a field the model must mentally correlate with the image.

---

## The Three-Tool Core

The foundation of the server is three tools that implement the hierarchical inspection workflow.

### get\_video\_overview

Returns a JPEG grid of evenly-distributed frames spanning the full video, each cell labeled with its timestamp. This is the entry point for any analysis session.

The tool supports two frame selection modes: `"even"` (the default, evenly distributed in time) and `"keyframe"`, which uses Bhattacharyya histogram comparison to select frames that are visually most distinct from one another — useful for longer videos where you want to capture the widest range of visual states rather than a uniform temporal sample.

### get\_video\_section

Given a `start_seconds` and `end_seconds`, returns a denser grid of that window. This is the zoom layer — called after the overview to examine specific phases in detail. It supports the same `"even"` and `"keyframe"` frame selection modes as the overview tool.

### get\_precise\_frame

Extracts a single full-resolution frame at an exact timestamp, using sub-frame precision. Returns lossless PNG — because this tool is specifically intended for moments where spatial accuracy matters: measuring joint angles, assessing contact positions, reading fine detail.

---

## A Real Analysis Session: Push-Up Timing

Here is a complete tool call log from analyzing a 13.6-second push-up tutorial video. The task: identify the timestamp where each rep begins.

```
✓ list_videos
✓ get_video_metadata      — Duration: 13.6s | FPS: 24.0 | Resolution: 1920x1080
✓ get_video_overview      — Full video | Frames shown: 20 | Grid: 5x4
✓ detect_motion_events    — sensitivity: 0.5
✓ detect_pauses           — sensitivity: 0.5, min_duration: 0.2s
✓ get_video_section       — Section 0.00s–7.00s | Frames shown: 14
✓ get_video_section       — Section 7.00s–13.50s | Frames shown: 14
✓ compare_frames          — 12 candidate timestamps
✓ compare_frames          — 8 rep start candidates (top position before descent)
```

Nine tool calls. The LLM navigated from a full overview to precise rep boundaries — identifying that motion spikes at 3.46s and 10.43s corresponded to camera repositioning between reps, not the athletic movement itself. It correctly distinguished abrupt camera movement (a scene detection event) from the gradual motion signature of the push-up descents.

The final output was a clean timestamped table: Rep 1 at 0:00, Rep 2 at ~3:50, Rep 3 at ~7:00, Rep 4 at ~10:48 — with the reasoning behind each call visible in the intermediate tool results.

---

## The Analysis Tools: Finding Where to Look

The three inspection tools are powerful but they require the LLM to know where to direct its attention. For short clips this is manageable. For longer recordings — a 20-minute training session, a full day of trail camera footage, a 2-hour security recording — it is not practical to rely on the overview alone.

The motion analysis tools solve this by computing lightweight signals that tell the LLM *where* the interesting content is before any expensive visual inspection occurs.

### detect\_motion\_events

Identifies timestamps where significant activity occurs, returning events with `start`, `peak`, and `end` timestamps plus a normalised intensity score. Sensitivity is adaptive to the video's own motion characteristics — it scales the detection threshold relative to the video's own baseline, so the same sensitivity setting works sensibly across a slow yoga session and an explosive Olympic lift without manual calibration.

### detect\_scenes

Identifies hard cuts and abrupt transitions. Uses the same underlying motion analysis as event detection but looks for instantaneous spikes rather than sustained activity — the temporal signature of a camera cut versus an athletic movement. One shared computation serves both tools.

### detect\_pauses

The inverse of event detection: finds timestamps where the subject is stationary for a sustained period. For movement analysis, pauses are often the analytically richest moments — the lockout, the catch, the bottom position. Each pause includes a `representative_timestamp` you can pass directly to `get_precise_frame`.

### get\_motion\_timeline

Returns a chart image showing motion intensity over time across the full video. Communicates the entire temporal activity structure in a single image — useful as a first step on any longer recording before committing to section-level analysis.

### get\_motion\_heatmap

Returns an annotated image showing where in the frame movement is spatially concentrated over a given time window. For a barbell squat this reveals hot zones at the hips and bar; for a swimming stroke, at the hands and feet. This spatial perspective is genuinely difficult to extract from frame grids alone.

---

## Completing the Toolkit

### compare\_frames

Takes a list of arbitrary timestamps and returns them side by side. This closes the loop on the inspection workflow: identify candidate moments with the motion and overview tools, then call `compare_frames` to see them simultaneously. Rep-to-rep consistency, left/right symmetry, current session versus a prior baseline — all require seeing specific moments together rather than sequentially.

### annotate\_frame

Accepts a timestamp plus drawing instructions — line segments between coordinates, three-point angle arcs with automatic degree calculation, and text labels — and returns an annotated PNG. The LLM identifies landmark coordinates from a `get_precise_frame` result, provides them to `annotate_frame`, and receives back an image with joint angles measured and labeled. No custom application code needed.

### get\_audio\_transcript

Extracts and transcribes the audio track with word-level timestamps. Transcription runs once per video and the result is cached; subsequent calls with different time windows query the saved transcript instantly. Supports both local Whisper and the Groq API (`whisper-large-v3-turbo`) — the latter is selected automatically when a `GROQ_API_KEY` is present.

---

## When Audio and Video Combine

The most surprising capability to emerge from building this server was what happens when `get_audio_transcript` and the visual tools are used together in the same analysis.

Consider this exchange in Claude Code. First, a simple transcription request:

> *"Use the video MCP server to analyze the video in `audio_transcript.mov`. ONLY use the MCP server. Goal: transcribe the entire video text and output it verbatim."*

Claude calls `list_videos`, then immediately calls `get_audio_transcript`. The transcript comes back — in German, automatically detected — timestamped to the segment level:

```prolog
[0.0s – 4.1s]
Dies ist ein Testvideo für die Audiottranskription.

[8.44s – 13.38s]
Daumen hoch, Daumen runter.

[15.9s – 19.72s]
Daumen hoch, Daumen runter.

Language detected: German
Transcribed by: Groq Whisper large-v3-turbo
```

Two tool calls. Done.

Then, in the same session, a follow-up prompt that combines both channels:

> *"Analyze the video images and detect whether the thumb was actually up when it was said. I.e. does the spoken statement about the thumb match what the speaker does in the video?"*

Claude already has the transcript with its timestamps. It calls `get_video_overview` to see the full 23-second video, then calls `get_video_section` twice — zooming into `8.0s–14.0s` and `15.0s–21.0s`, the windows the transcript established as the two phrases. Three more tool calls.

The result was a structured analysis that neither the audio nor the video alone could have produced:

**Phrase 1 — "Daumen hoch, Daumen runter" \[8.44s–13.38s\]:**

- "Daumen hoch" (~8.4–10.9s): Thumb UP ✅
- "Daumen runter" (~10.9–13.4s): Thumb still UP — gesture never performed ❌

**Phrase 2 — "Daumen hoch, Daumen runter" \[15.9s–19.72s\]:**

- "Daumen hoch" (~15.9–17.8s): Thumb briefly up at 15.25s, already DOWN by 16.25s ❌
- "Daumen runter" (~17.8–19.7s): Thumb DOWN throughout ✅

**Verdict:** 2 out of 4 gesture-speech matches correct. The gestures are offset relative to the speech in both repetitions — the speaker's timing is inconsistent with their words.

This is not a capability you find in most video tools. It requires: transcription with accurate word-level timing, visual inspection of the specific frames corresponding to those words, and synthesis of both signals into a coherent conclusion. The server provides the mechanism; the LLM provides the cross-modal reasoning. Neither is sufficient alone.

---

## The Workout Judge: Visual Iteration in Practice

The most direct way to understand what this approach enables is to trace through a real analysis run. The following is from `workout-judge-mcp`, the example application in the repository that wraps the MCP server in a structured CLI — but every tool call it makes is a plain MCP call that you could issue from Claude Code or Claude Desktop with an identical result.

### Step 1: Orient

The session opens with a metadata call. The server reports back: portrait-orientation video (1080×1920px), 30fps, 8.5 seconds, H.264. That last detail matters — portrait video is common from phone recordings and the server handles the rotation automatically, so the LLM receives correctly-oriented frames regardless of how the container metadata stores it.

With duration and fps known, the model requests a full video overview: 20 frames distributed across the 8.5-second clip, each timestamped.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flxsvbmji0ga7zo8kqxlh.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Flxsvbmji0ga7zo8kqxlh.png)

### Step 2: Segment

From the overview, the model can see the video contains approximately three full repetitions. It issues three `get_video_section` calls to examine each rep in detail:

```
✓ get_video_section — Section 0.00s–2.50s  | Frames shown: 10 | Grid: 4×3
✓ get_video_section — Section 2.50s–5.50s  | Frames shown: 10 | Grid: 4×3
✓ get_video_section — Section 5.50s–8.47s  | Frames shown: 10 | Grid: 4×3
```

Each section grid gives a denser temporal view of one rep. The model is not guessing where reps begin and end — it is reading the timestamps off the grid cells and using that information to structure its subsequent calls.

### Step 3: Freeze

Having identified the analytically critical positions from the section grids, the model extracts four precise full-resolution frames:

```ada
✓ get_precise_frame — Precise frame at 0:00.62 (0.620s) — 1080×1920px PNG
✓ get_precise_frame — Precise frame at 0:01.38 (1.380s) — 1080×1920px PNG
✓ get_precise_frame — Precise frame at 0:02.75 (2.750s) — 1080×1920px PNG
✓ get_precise_frame — Precise frame at 0:05.35 (5.350s) — 1080×1920px PNG
```

These are not arbitrary timestamps — the model selected them by reading the section grids and identifying the frames that best represent specific positions in the movement cycle. Each precise frame is lossless PNG at full resolution, giving the model maximum spatial detail for the next step.

### Step 4: Annotate

This is where the approach becomes something qualitatively different from ordinary video analysis. Having extracted precise frames, the model identifies the pixel coordinates of anatomical landmarks directly from what it can see in those images. It then calls `annotate_frame` four times, providing those coordinates as drawing instructions:

```
✓ annotate_frame — Annotated frame at 0:01.38 | 5 lines, 2 angles, 7 labels (Knee ~85°: 107°) ...
✓ annotate_frame — Annotated frame at 0:00.62 | 4 lines, 2 angles, 4 labels (Trunk ~55°: 104°) ...
✓ annotate_frame — Annotated frame at 0:02.75 | 2 lines, 4 labels ...
✓ annotate_frame — Annotated frame at 0:05.35 | 4 lines, 1 angle, 4 labels (Knee ~88°: 115°) ...
```

The server draws lines between the specified coordinates, calculates the angles at the specified vertices, and renders the measurements directly onto the frame. The model receives back an annotated image — and that image becomes the input for the next layer of reasoning.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftg8tdnmc5r53i1dseoil.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ftg8tdnmc5r53i1dseoil.png)

What you are looking at in that image is a precise measurement produced entirely through tool calls. The model identified the joint positions visually, translated them into pixel coordinates, and instructed the server to draw the measurement arcs and label them. No pose estimation model, no keypoint detection pipeline — just the LLM reading what it sees and calling a drawing tool with the coordinates.

This is what "visual iteration" means in practice: each tool call produces an image that the model reasons about to decide what to call next. The overview informs the section calls. The section grids inform the precise frame selections. The precise frames inform the annotation coordinates. The annotated frames inform the final analysis. At no point is the model reasoning blindly — every step is grounded in what it has actually seen.

### Step 5: Report

The final output is a structured assessment rendered in the terminal UI: an overall score, a timestamped observations table with severity ratings, a strengths section, areas for improvement, and prioritised recommendations.

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffeekmxg9dxp0zxoflgvs.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Ffeekmxg9dxp0zxoflgvs.png)

[![ ](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy0cuj5wk3qquasd6psgi.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fy0cuj5wk3qquasd6psgi.png)

The entire session — metadata, overview, three section grids, four precise frames, four annotated frames, and the final structured report — was driven by a single natural-language prompt to the `workout-judge-mcp` CLI. The tool call sequence emerged from the model's reasoning, not from hard-coded logic in the application.

---

## Using the Server from Claude Code

Getting started with Claude Code requires a single configuration file. The repository includes a `.mcp.json` that Claude Code auto-detects and offers to enable:

```
{
  "mcpServers": {
    "video": {
      "command": "uv",
      "args": ["run", "python", "-m", "mcp_video_server"],
      "env": {
        "MCP_VIDEO_ROOT": "/path/to/your/videos"
      }
    }
  }
}
```

Once enabled, you can run natural language analysis requests directly from the Claude Code terminal. No scaffolding, no application code, no custom tool definitions. Claude discovers the 14 available tools via the MCP protocol and orchestrates them based on your prompt.

Here are a few prompts that work well:

```
Use the video MCP server to analyze [filename].
Count the reps and identify where each one begins.
Only use the MCP server — no local file access.
```
```
Use the video MCP server to analyze [filename].
Identify any form breakdowns across the set.
Focus on depth, spinal alignment, and knee tracking.
Compare the first and last rep side by side.
```
```
Use the video MCP server to analyze [filename].
First transcribe any spoken audio.
Then check whether the visible actions match what is being said.
```

The instruction "only use the MCP server — no local file access" is worth including. It ensures Claude routes all video work through the server tools and does not attempt to read files directly, which keeps the analysis reproducible and the tool call log clean.

---

## Building Custom Skills for Repeated Workflows

For workflows you run repeatedly — weekly squat checks, patient assessment reviews, production quality audits — defining a reusable Claude skill pays off quickly. Claude Code supports project-level instructions via `CLAUDE.md`, and Claude Desktop supports custom instructions that are applied to every conversation.

A skill for workout analysis might look like this:

```
## Video Form Analysis Workflow

When asked to analyze a workout video using the MCP server:

1. Call list_videos to confirm the file is available
2. Call get_video_metadata for duration, fps, and resolution
3. Call get_video_overview with max_frames: 16 to see the full structure
4. Call detect_pauses (sensitivity: 0.6, min_duration: 0.3) to find hold positions
5. Call detect_motion_events (sensitivity: 0.5) to segment individual reps
6. For each rep: call get_video_section on its time window
7. Call compare_frames across the bottom positions of all reps
8. For any rep showing concern: call get_precise_frame at the deepest point
9. Call annotate_frame with joint angle measurements at that frame
10. Summarize: rep count, timestamps, notable differences between reps,
    specific form observations with timestamps as evidence
```

A skill like this transforms an open-ended capability into a reliable, repeatable procedure. The same principle applies to any domain: a property inspection skill, a surgical review skill, a wildlife observation skill — each defines the sequence of tools and the output format once, so every subsequent analysis follows the same rigorous workflow without re-specifying it.

---

## The General Pattern

Stepping back from the specific implementation, the design approach that makes this work is transferable to other domains.

**1\. Hierarchical temporal sampling.** Tools at decreasing granularity — full overview, time-range section, precise frame — mirror how a knowledgeable reviewer approaches footage and allow the LLM to progressively focus without redundant work.

**2\. Inline visual return.** Images returned directly in tool responses, not as file paths. The LLM is a visual reasoner; it cannot open files. Timestamps burned into pixels participate in visual reasoning rather than sitting in metadata the model must correlate manually.

**3\. Temporal orientation before spatial inspection.** Lightweight signals about *when* interesting content occurs — motion timelines, event lists, scene boundaries — enable targeted inspection and reduce expensive image calls to the moments that actually matter.

**4\. Audio as a first-class signal.** In many real-world recordings, the spoken content carries as much analytical value as the visual content. Transcription with word-level timestamps, cached after the first call, enables cross-modal analysis that neither channel alone could support.

**5\. Shared analytical primitives.** Multiple analysis tools share a single core computation that runs once and is reused. Efficiency follows from architecture, not from optimising individual tools in isolation.

This pattern applies to any domain where a human expert would currently review video manually, the interesting content is not uniformly distributed across the recording, and the output is a report, annotation, or decision rather than another video.

---

## Beyond the Gym: Ten Domains

The same tools that analyse a squat apply directly to a wide range of domains where video review is currently a manual, attention-intensive task.

**Physical therapy & rehabilitation.** Remote assessment of home exercise recordings. `detect_pauses` isolates end-range positions for ROM measurement; `compare_frames` places left and right sides of symmetric movements together; `annotate_frame` produces the joint angle documentation the therapist needs.

**Sports coaching.** Technique review between sessions. Motion event detection segments individual strokes or swings; the heatmap reveals which body segments are driving movement versus compensating; frame comparison across reps exposes consistency or progressive fatigue.

**Manufacturing quality control.** Assembly operation review. Scene detection segments each unit's cycle; the motion timeline makes inconsistent cycle times immediately visible; annotation marks the specific component in question for the quality report.

**Surgical training.** Laparoscopic procedure recordings reviewed by supervisors. Motion event detection maps instrument activity; pause detection identifies decision points before critical actions; precise frame extraction provides lossless-quality material for feedback discussions.

**Wildlife observation.** Trail camera footage filtered from hours to minutes. Motion event detection isolates animal appearances; the heatmap reveals movement paths across the frame and through habitat corridors.

**Property inspection.** Walkthrough video reviewed for condition reports. Scene detection segments room transitions; precise frames capture defect evidence; frame comparison across inspection dates tracks remediation.

**Recipe verification.** Demonstration videos cross-checked against written recipes. Word-level transcript timestamps correlate spoken instructions with visual state at each step; pause detection finds the stages where the instructor presents a completed result.

**Dance and choreography.** Performances reviewed against a reference. Frame comparison at beat-aligned timestamps places student and reference side by side; the heatmap per phrase reveals whether movement is initiating from the correct body parts.

**Security and incident review.** CCTV footage reviewed following an incident. Motion event detection filters long static recordings to active windows; the motion timeline maps activity across a long recording before any detailed inspection begins. Implement with appropriate access controls and privacy considerations.

**Fleet and driving behaviour.** Dashcam footage assessed for driver behaviour. The motion timeline surfaces abrupt changes corresponding to harsh braking; the audio transcript captures in-cab audio for distraction analysis.

---

## Multi-Video Architecture

The server is built for directories, not individual files. A single root directory is specified at startup via `MCP_VIDEO_ROOT`. All operations are scoped to this directory — path traversal attempts are rejected at validation, before any file operation occurs.

All caches and debug output use the filename as a segregation key, so the cached frame diff array for `squat_session_01.mp4` is stored separately from `deadlift_form.mp4` and can be cleared independently.

The `list_videos` tool provides discovery, returning filenames in the exact format all other tools expect. A session begins with `list_videos`, and every subsequent tool call references a filename from that listing. The server supports subdirectories, recursive listing, and optional per-file metadata and cache status in the listing response.

---

## Repository Structure

The project is a monorepo with two layers. The core package — `packages/mcp-video-server` — provides the 14 MCP tools and can be used standalone with any MCP-compatible client: Claude Desktop, Claude Code, MCP Inspector, or any Pydantic AI agent.

The `examples/` directory contains two implementations of the same workout analysis application that demonstrate different integration patterns:

`examples/workout-judge` uses `FrameExtractor` and `GridCompositor` directly as Python imports with three custom Pydantic AI tools — a minimal implementation that shows what the core library can do without the full MCP layer.

`examples/workout-judge-mcp` connects to the MCP Video Server as a subprocess via `MCPServerStdio`. All 14 tools are available to the agent automatically through the `toolsets` parameter — no local tool definitions needed. The contrast between the two examples is instructive: the direct import version requires you to define and maintain your own tool wrappers; the MCP version gets all 14 tools for free and stays in sync as the server evolves.

---

## What This Is Not

This server is not a video understanding model. It does not watch video the way a human does — continuously, with full temporal context, tracking objects across frames. It gives an LLM the ability to *inspect* video strategically. The intelligence is in the LLM; the server provides the access mechanism.

It is not a replacement for purpose-built computer vision pipelines in high-volume production contexts. Where the bottleneck is computation and you need to process thousands of hours with strict latency requirements, a dedicated CV system is the right tool. This server addresses the workflows where a human would currently be doing manual review — where the bottleneck is attention.

It does not handle real-time or streaming video. Every operation assumes a complete video file — a deliberate simplification that covers the overwhelming majority of the review and analysis scenarios described above.

---

## The Broader Point

The exercise of starting from a specific personal problem — evaluating my own squat — and following the design questions it raised produced something more general than I expected.

The most transferable insight is this: **when designing tools for LLM use, the right question is not "what does this data contain?" but "how would a knowledgeable human review this data, and what would they need to see at each stage?"**

The three-stage inspection hierarchy emerged from observing how a coach watches training footage. The timestamped grid representation emerged from asking what format makes temporal structure immediately visible to a visual reasoner. The motion timeline emerged from asking what a reviewer would want before committing full attention to a long recording. The audio transcript caching emerged from recognising that the same transcript would be needed repeatedly across an iterative analysis session.

None of these are computer vision questions. They are questions about human cognition and workflow. The interesting design work in LLM tooling is often less about the underlying capabilities — which are increasingly capable — and more about the interface layer: what to surface, in what form, at what stage, in response to which questions.

---

## Getting Started

Install the server and point it at a directory of videos:

```bash
# Clone the repo
git clone https://github.com/littler00t/mcp-deep-video
cd mcp-deep-video

# Install dependencies
uv sync

# Run the MCP server
MCP_VIDEO_ROOT=./example_videos uv run mcp-video-server
```

For Claude Desktop, add the server to `claude_desktop_config.json`. For Claude Code, update the included `.mcp.json` with your video root path — Claude Code will detect and offer to enable it automatically.

The `doc/tool_index.md` in the repository is a full reference for all 14 tools. The `SPECIFICATION.md` covers the security model, caching architecture, and recommended call sequences in detail.

If you build something with this, or adapt the pattern to a domain not covered here, I would be glad to hear about it.

---

*The MCP Video Analysis Server is open source, released under the MIT licence. Github: [https://github.com/littler00t/mcp-deep-video](https://github.com/littler00t/mcp-deep-video)*

[![Google article image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fi6mj0yymgm9gmhlz7l4y.png)](https://dev.to/googleai/building-capabilities-for-a-multi-agent-system-with-google-adk-mcp-and-cloud-run-ab9?bb=263437)

## Building Capabilities for a Multi-Agent System with Google ADK, MCP, and Cloud Run

My team's mission is to accelerate the developer journey from writing code to running secure AI workloads on Google Cloud. To help developers succeed, we focus on identifying their most pressing questions and building demos that provide straightforward, easy-to-implement solutions.