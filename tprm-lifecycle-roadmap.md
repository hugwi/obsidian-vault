---
categories:
  - "[[Projects]]"
project: "[[Ethira]]"
title: "TPRM Lifecycle Roadmap"
date_created: 2026-04-14
type: concept
status: active
tags:
  - tprm
  - roadmap
  - shadow-provider
  - ai-governance
---

# TPRM Lifecycle Roadmap

> [!info] Source
> Whiteboard session (2026-04-14). Photos in [[roadmap/20260414_093650.jpg|roadmap/]]. This captures the **full TPRM product lifecycle** — broader than the [[signals-intelligence-roadmap]] which focuses on the Signals Intelligence (browser extension) detection layer.

---

## TPRM Lifecycle Stages

The product lifecycle follows six stages in a continuous loop:

```
Detect (4) --> Pre-Screen (3) --> Dashboard (3) --> Monitor (2) --> Enforce (3) --> Offboard
  ^                                                                                   |
  |___________________________________________________________________________________|
```

### 1. Detect — Shadow Provider Discovery

Discover unauthorized/unknown third-party services across multiple surfaces.

**Discovery dimensions:**
- **Country** — where the provider operates / endpoints are hosted
- **Type of Data** — what data categories flow to the provider

**Detection methods (sensor surface):**
- **Browser Extension** — current primary sensor ([[signals-intelligence-roadmap#Phase 1]])
- **CLI** — command-line tooling detection (coding assistants, terminal-based AI)
- **Workstation Monitoring** — OS-level observation of local agents and processes
- **SDK** — instrumentation for first-party apps calling AI services
- **Proxy Integration** (maybe) — integration with CrowdStrike, etc. for network-level detection

**AI-specific shadow provider problems:**
The detection challenge spans three overlapping domains — browser, OS, and server/production. Each surface has unique risks, and the intersection of all three is where the hardest problems live. No single sensor covers everything.

### 2. Monitor / Alert

Continuous monitoring of discovered providers. Track usage patterns, data flows, and behavioral changes over time. Alert on anomalies and policy violations.

### 3. Pre-Screen

Evaluate newly discovered providers before they reach full risk assessment. Automated triage based on:
- Provider category and risk profile
- Data types being sent
- Jurisdiction and adequacy status
- Existing relationship in TPRM module

### 4. Dashboard

Central visibility layer. Single pane of glass for:
- All discovered providers and their status
- Usage trends and data flow mapping
- Risk scores and compliance gaps
- Links through to the [[signals-intelligence-roadmap#1.3 AI Usage Insights Dashboard|AI Usage Insights Dashboard]]

### 5. Enforce

Policy enforcement across all sensor surfaces:
- **Policy** — centrally defined allow/block rules
- **Banned sites** — domain-level blocking
- **Banned MCP connections** — block specific AI agent-to-tool connections (MCP protocol level)

Maps to [[signals-intelligence-roadmap#2.2 Policy Enforcement Engine|Policy Enforcement Engine (Phase 2)]].

### 6. Offboard

Decommission providers that are no longer authorized or in use:
- Revoke access and integrations
- Archive monitoring data
- Verify no residual data flows
- Update inventory status

---

## Inventory Model

What gets tracked across the entire lifecycle:

### Assets
- **System** — infrastructure and platform components
- **App** — applications (SaaS, internal)
- **Microservice** — individual service components
- **Agent** — AI agents (autonomous or semi-autonomous)
- **Model** — AI/ML models in use
- **MCP Server** — Model Context Protocol servers connecting agents to tools

### Ownership
- **People** — individual owners and users
- **Teams** — team-level ownership and responsibility

### Business Context
- **Function** — business function (Engineering, Sales, HR, etc.)
- **Process** — business process the asset supports

---

## Relationship to Existing Roadmap

This lifecycle view is the **product-level frame** that the [[signals-intelligence-roadmap]] implements technically:

| Lifecycle Stage | Signals Intelligence Coverage |
|---|---|
| Detect | Phase 1 (browser ext), Phase 3 (SDK, workstation) |
| Pre-Screen | Phase 1.3 (dashboard basics) |
| Dashboard | Phase 1.3, Phase 4.1 (cross-pattern) |
| Monitor | Phase 1 (data collection), Phase 2.3 (risk signals) |
| Enforce | Phase 2.2 (policy engine), Phase 4.3 (at scale) |
| Offboard | Not yet covered — new workstream needed |

### Gaps identified from whiteboard vs existing roadmap

1. **Offboarding workflow** — not in the current roadmap at all
2. **MCP connection enforcement** — blocking at MCP protocol level is a new concept beyond domain-level blocking
3. **Inventory model** — the asset/ownership/business taxonomy is more structured than what's currently planned
4. **Proxy integration** — CrowdStrike/EDR integration as a detection surface (marked "maybe" on whiteboard)
5. **Agent and Model as first-class inventory items** — current roadmap tracks apps/domains but not individual agents or models as distinct entities
