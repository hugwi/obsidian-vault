---
title: Happy - Claude Code Mobile Client
source: https://happy.engineering/
author:
  - "[[Slopus]]"
published:
created: 2026-06-29
description: Free, open-source mobile app for Claude Code. Control Claude AI from your phone with end-to-end encryption and seamless workflow. Get started with npm install -g happy.
tags:
  - clippings
  - remote-code
---
## Claude Code Anywhere

Spawn and control multiple Claude Codes in parallel. Happy Coder runs on your hardware, works from your phone and desktop, and costs nothing. Open source.

<video src="https://happy.engineering/take-4-short-term.mp4" controls=""></video><video src="https://happy.engineering/take-4-short-sim.webm" controls=""></video>

$ `npm i -g happy && happy`

Hands-free control with voice agent—not just dictation

Multiple active sessions across multiple machines

Works seamlessly with your existing tools and workflow

Secure with end-to-end encryption

Open source (MIT licensed)

### Why Happy?

Zero workflow disruption

└─

Keep using your favorite tools, editors, and development environments exactly as before. Happy integrates with your existing setup without requiring any changes to how you work.

Multiple Active Sessions

└─

Run several Claude Code instances simultaneously across different projects. Switch between frontend, backend, and DevOps tasks without losing context or momentum.

Everything from the terminal, on your phone

└─

Access all Claude Code features on mobile. From plan mode to custom agents, if it works in the terminal, it works in Happy.

Open source and free

└─

Well organized codebase makes it easy to contribute. Friendly community.

Secure

└─

Happy uses End to End Encryption. No one can read your messages or code.

Smart Push Notifications

└─

Get alerted when your input is needed, when code is ready to review, or when something went wrong.

Real-Time Voice Execution

└─

Speak commands and watch them execute instantly. Not just transcription - true voice-to-action that lets you code, debug, and manage projects while completely hands-free.

### How does it work?

Start Happy CLI and you'll have a regular Claude Code session. But you can continue that same session from [iOS](https://apps.apple.com/us/app/happy-claude-code-client/id6748571505), [Android](https://play.google.com/store/apps/details?id=com.ex3ndr.happy), or [Web](https://app.happy.engineering/)

Happy has three parts that work together:

CLI Program (happy)

└─

This runs on your computer. It starts Claude Code and watches what it does. Then it encrypts this information and sends it to a server.

Mobile App

└─

This runs on your phone. It gets the encrypted data from the server and shows you what Claude Code is doing. All the display code lives here.

Relay Server

└─

This connects your computer and phone. It passes encrypted messages between them. The server can't read your data. It just moves encrypted blobs around.