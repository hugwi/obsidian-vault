---
created: 2026-07-19
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - dev-tools
  - privacy
  - opencode
  - telemetry
---

# OpenCode Privacy Concerns

Source: [GitHub issue #459](https://github.com/anomalyco/opencode/issues/459) + community code audit

## What OpenCode sends by default (no opt-in)

Per a [community audit](https://github.com/anomalyco/opencode/issues/459#issuecomment-3822338336) by OpenToInnovate, the base app phones home to:

| Endpoint | What |
|----------|------|
| `api.opencode.ai` | Session content, prompts |
| `api.honeycomb.io` | Telemetry, IP, location |
| `us.i.posthog.com` | Usage analytics |
| `opencode.ai/zen/v1` | Prompts routed through their proxy |
| `models.dev` | Model list fetch (benign, documented, community-driven) |

The maintainer ([thdxr](https://github.com/anomalyco/opencode/issues/459#issuecomment-3013209863)) claims "there is no telemetry collected" but Honeycomb and PostHog are in the codebase. The `models.dev` fetch can be disabled (opencode bundles a snapshot in every release).

## OTel plugin is separate and clean

The `@devtheops/opencode-plugin-otel` plugin (third-party, MPL-2.0, [GitHub](https://github.com/DEVtheOPS/opencode-plugin-otel)) has **no hardcoded external endpoints**. It only sends to the `OPENCODE_OTLP_ENDPOINT` you configure.

`OPENCODE_ENABLE_TELEMETRY=1` activates **only** this plugin — it does not control opencode's own telemetry to Honeycomb/PostHog.

## Key distinction

- **Base app telemetry** (Honeycomb, PostHog, api.opencode.ai) — always on, hard to disable, separate from the plugin
- **OTel plugin** (`OPENCODE_ENABLE_TELEMETRY=1`) — fully local, you own the data pipeline, no third-party endpoints

The OTel observability path is safe and self-hostable via OpenTelemetry Collector → Grafana/Prometheus. But the base app still leaks data elsewhere regardless of the plugin configuration.
