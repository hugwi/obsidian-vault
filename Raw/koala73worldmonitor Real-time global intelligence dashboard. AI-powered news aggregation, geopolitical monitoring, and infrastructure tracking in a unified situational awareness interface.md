---
categories:
  - "[[Clippings]]"
title: "koala73/worldmonitor: Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface"
source: "https://github.com/koala73/worldmonitor"
author:
published:
created: 2026-06-21
rating: 
action: 
description: "Real-time global intelligence dashboard. AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface - koala73/worldmonitor"
tags:
  - "clippings"
---
## World Monitor

**Real-time global intelligence dashboard** — AI-powered news aggregation, geopolitical monitoring, and infrastructure tracking in a unified situational awareness interface.

[**Documentation**](https://www.worldmonitor.app/docs/documentation) · [**Releases**](https://github.com/koala73/worldmonitor/releases/latest) · [**Contributing**](https://www.worldmonitor.app/docs/contributing)

[![World Monitor Dashboard](https://github.com/koala73/worldmonitor/raw/main/docs/images/worldmonitor-7-mar-2026.jpg)](https://github.com/koala73/worldmonitor/blob/main/docs/images/worldmonitor-7-mar-2026.jpg)

---

## What It Does

- **500+ curated news feeds** across 15 categories, AI-synthesized into briefs
- **Dual map engine** — 3D globe (globe.gl) and WebGL flat map (deck.gl) with 56 map layer types
- **Cross-stream correlation** — military, economic, disaster, and escalation signal convergence
- **Country Instability Index (CII)** — server-authoritative CII v8 stress scoring for 31 Tier-1 countries
- **Finance radar** — 29 stock exchanges, commodities, crypto, and 7-signal market composite
- **Local AI** — run everything with Ollama, no API keys required
- **6 site variants** from a single codebase (world, tech, finance, commodity, happy, energy)
- **Native desktop app** (Tauri 2) for macOS, Windows, and Linux
- **24 languages** with native-language feeds and RTL support

For the full feature list, architecture, data sources, and algorithms, see the **[documentation](https://www.worldmonitor.app/docs/documentation)**.

---

## Support Status

All site variants and desktop binaries are built from a single codebase and ship from the same release process. The table below clarifies maintenance status so you know which surfaces are safe to depend on.

| Surface | Status | Notes |
| --- | --- | --- |
| `worldmonitor.app`, `tech.`, `finance.`, `commodity.`, `happy.`, `energy.` | Stable | Public deployments built from this repo, actively maintained |
| Desktop binaries (Windows / macOS Apple Silicon / macOS Intel / Linux AppImage) | Stable | One Tauri binary that switches variants in-app; current CI release targets are `full` and `tech` |

Issues filed against any of the above are triaged from the same backlog — see the [issues board](https://github.com/koala73/worldmonitor/issues) for currently-open work.

---

## Quick Start

```
git clone https://github.com/koala73/worldmonitor.git
cd worldmonitor
npm install
npm run dev
```

Open [localhost:3000](http://localhost:3000/). The app runs with no environment variables.

Feature-specific data sources may require credentials — for example, the flight-price command (`fly LON DXB`) needs `TRAVELPAYOUTS_API_TOKEN` to return live quotes; without it the command shows a "credentials required" message rather than synthetic data. See `.env.example` for the full list.

For variant-specific development:

```
npm run dev:tech       # tech.worldmonitor.app
npm run dev:finance    # finance.worldmonitor.app
npm run dev:commodity  # commodity.worldmonitor.app
npm run dev:happy      # happy.worldmonitor.app
npm run dev:energy     # energy.worldmonitor.app
```

See the **[self-hosting guide](https://www.worldmonitor.app/docs/getting-started)** for deployment options (Vercel, Docker, static).

---

## Tech Stack

| Category | Technologies |
| --- | --- |
| **Frontend** | Vanilla TypeScript, Vite, globe.gl + Three.js, deck.gl + MapLibre GL |
| **Desktop** | Tauri 2 (Rust) with Node.js sidecar |
| **AI/ML** | Ollama / Groq / OpenRouter, Transformers.js (browser-side) |
| **API Contracts** | Protocol Buffers (276 protos, 34 services), sebuf HTTP annotations |
| **Deployment** | Vercel Edge Functions (60+), Railway relay, Tauri, PWA |
| **Caching** | Redis (Upstash), 3-tier cache, CDN, service worker |

Full stack details in the **[architecture docs](https://www.worldmonitor.app/docs/architecture)**.

---

## Flight Data

Flight data provided gracefully by [Wingbits](https://wingbits.com/?utm_source=worldmonitor&utm_medium=referral&utm_campaign=worldmonitor), the most advanced ADS-B flight data solution.

---

## Data Sources

WorldMonitor aggregates 65+ external providers and APIs across geopolitics, finance, energy, climate, aviation, cyber, military, infrastructure, and news intelligence — surfaced through 500+ curated feeds and tracked by a freshness monitor covering 35 source groups. See the full [data sources catalog](https://www.worldmonitor.app/docs/data-sources) for providers, feed tiers, and collection methods.

---

## Contributing

Contributions welcome! See [CONTRIBUTING.md](https://github.com/koala73/worldmonitor/blob/main/CONTRIBUTING.md) for guidelines.

```
npm run typecheck        # Type checking
npm run build:full       # Production build
```

---

## License

**AGPL-3.0-only** for the source code. Commercial use is permitted under the AGPL when you comply with its copyleft and source-availability terms.

| Use Case | Allowed? |
| --- | --- |
| Personal / research / educational | Yes, under AGPL-3.0-only |
| Self-hosted instance | Yes, under AGPL-3.0-only |
| Fork and modify | Yes, share source under AGPL-3.0-only when required |
| Commercial use / SaaS | Yes, under AGPL-3.0-only when you comply with AGPL obligations |
| Private-source proprietary use or official branding rights | Separate commercial or trademark permission needed |

See [LICENSE](https://github.com/koala73/worldmonitor/blob/main/LICENSE) for the full code license and [docs/license.mdx](https://github.com/koala73/worldmonitor/blob/main/docs/license.mdx) for a plain-language summary. Commercial licensing is available as an alternative option for teams that need non-AGPL terms.

Copyright (C) 2024-2026 Elie Habib. All rights reserved.

---

## Contributors

[![](https://camo.githubusercontent.com/05804fdc513b8864fd0e6b5c2442e2dbb5b9ed956c948c3c64d48d50f2dcb435/68747470733a2f2f636f6e747269622e726f636b732f696d6167653f7265706f3d6b6f616c6137332f776f726c646d6f6e69746f72)](https://github.com/koala73/worldmonitor/graphs/contributors)

## Security Acknowledgments

We thank the following researchers for responsibly disclosing security issues:

- **Cody Richard** — Disclosed three security findings covering IPC command exposure, renderer-to-sidecar trust boundary analysis, and fetch patch credential injection architecture (2026)

See our [Security Policy](https://github.com/koala73/worldmonitor/blob/main/SECURITY.md) for responsible disclosure guidelines.

---

[worldmonitor.app](https://worldmonitor.app/) · [docs.worldmonitor.app](https://www.worldmonitor.app/docs/documentation) · [finance.worldmonitor.app](https://finance.worldmonitor.app/) · [commodity.worldmonitor.app](https://commodity.worldmonitor.app/)

[

![Star History Chart](https://camo.githubusercontent.com/e9cab248efd3b7e2740fe60f53cdcacc6aeff6c3607a3a2c0f7bdd734c8bc2d5/68747470733a2f2f6170692e737461722d686973746f72792e636f6d2f7376673f7265706f733d6b6f616c6137332f776f726c646d6f6e69746f7226747970653d4461746526747970653d44617465)

](https://api.star-history.com/svg?repos=koala73/worldmonitor&type=Date)