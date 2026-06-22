# Ethira — Vision, Mission & Strategy

> [!note] Guidance for what we're building
> This document, together with [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a), [Strategy 2026 + Objectives Q2-Q3](https://www.notion.so/337671bead5c80829f9fd254bbea72d0), and the [Browser Extension — Sales Guide](https://www.notion.so/33a671bead5c817ebabae0f9a43ee87c), serves as guidance for what we're building. Refer to these when making architectural decisions, prioritizing features, or evaluating trade-offs.

---

## Vision

Ethira becomes the governance and intelligence layer for enterprise AI adoption — enabling organizations to discover, monitor, and control how AI agents and third-party dependencies operate across their environment, while building the audit trails that compliance requires.

Enterprises are adopting AI at a pace that outstrips their ability to govern it. Employees use ChatGPT, Perplexity, Claude, and dozens of niche AI tools without security or compliance teams ever knowing. These tools, in turn, call sub-processors, route data through third-party APIs, and store information in jurisdictions the company has never assessed. The result is an invisible, unmanaged supply chain of AI services growing inside every organization.

The existing security tooling landscape is fragmented. EDR vendors see endpoints but don't understand AI-specific behavior. CNAPP vendors cover cloud workloads but are blind to what happens in the browser. DSPM vendors track data flows but lack runtime visibility into agent actions. Identity vendors know credentials but not intent. No single platform connects the dots from endpoint behavior to third-party risk to governance action.

Ethira bridges this gap by combining real-time signals intelligence with an operational GRC platform — from detection to action in one system. We don't just tell you what AI tools your people are using; we map the entire transitive supply chain behind each interaction and give you the controls to act on it.

**Key market signals:**
- 79% of enterprises have adopted AI agents, yet only 1 in 9 runs them in production — a 68-percentage-point deployment backlog
- 92% of organizations lack full visibility into their AI identities; 95% doubt they could detect or contain misuse
- 48% of cybersecurity professionals identify agentic AI as the single most dangerous attack vector
- Pure-play AI/LLM security has raised $414M — less than 5% of total cybersecurity funding in 2025. The protection gap is enormous.

---

## Mission

We help organizations govern their AI agents and third-party dependencies by discovering what's running, tracing what it does, enforcing policies and contracts in real time, and building the audit trails that compliance requires — all without slowing down engineering.

---

## Strategy

### Market positioning

We own the **third-party AI visibility gap** — the space where no existing vendor operates.

Nobody combines:
- **Runtime forensics and attribution** — what happened and can you prove it
- **Supply chain dependency attestation** — were those components clean at execution time
- **European regulatory depth** — GDPR-native, EU data residency, DORA/NIS2 alignment

First-party monitoring (what the company builds and controls) is increasingly served by adjacent vendors — Geordie, Onyx, JetStream and others are building agent observability for first-party deployments. Third-party monitoring (what the workforce uses, and what those tools use underneath) is the blind spot. This is our wedge.

Our EU positioning is a structural advantage. Competitors are overwhelmingly US/Israel-based. DORA, NIS2, GDPR, and the EU AI Act create regulatory forcing functions that demand local depth. We're GDPR-native and building for European regulatory requirements from day one.

### Three pillars of execution

Engineering is organized into three teams, each a strategic vector:

1. **Signals Intelligence** — Monitors and maps the AI landscape. Places sensors at the point of interaction to detect what tools are being used, what data flows into them, and what risks they represent. Feeds intelligence into the operational platform.
2. **Operational Platform** — Where intelligence becomes action. Custom risk taxonomies, outsourcing register maintenance, onboarding optimization. The platform where customers do their governance work.
3. **Workflow Automation** — Puts operational work on autopilot. Trust Exchange for accelerating sales cycles, custom agentic automations, AI-powered questionnaire answering. Removes friction from governance workflows.

### Go-to-market

We follow a **land-and-expand** model:

- **Land** with Shadow AI visibility + TPRM — low friction, high urgency, priced below the procurement threshold. Every CISO wants to know what AI their people are using.
- **Expand** into PII detection, policy enforcement, AI usage insights, outsourcing register — upsell modules that deepen governance once the sensor is deployed.
- **Lock in** with operational platform integration — signals feed into risk assessments, compliance workflows, and audit trails. Switching cost rises with integration depth. Ethira becomes embedded in the customer's compliance operations.

### Success metrics (2026)

- 120–180 new customers by EOY (3–6% of the DORA-liable market)
- 1.5M–3.0M ARR (enables Series A raise)
- AI monitoring + Trust Exchange expands our addressable market beyond DORA-regulated companies

### Competitive context

Three layers of third-party risk that nobody owns end-to-end:

**Layer 1 — Vendor-deployed agents**
SaaS vendors are deploying AI agents into customer environments. Existing TPRM assessed the vendor as an organization. It has no mechanism to assess the agents they now run inside your systems, what data those agents can access, or how they behave.

**Layer 2 — Agentic dependency stack**
First-party agents depend on components you didn't build: MCP servers, open-source agent frameworks, model registries, third-party agent skills, and foundation models hosted by external providers. This is an SBOM problem applied to AI — and unlike software SBOMs, no standard or tooling exists. Real incidents in early 2026: 1,184 malicious skills in the OpenClaw marketplace, 492 MCP servers exposed with zero auth, RCE in Claude Code via poisoned repo configs, supply chain attack on LiteLLM affecting Mercor and Cisco.

**Layer 3 — Multi-agent cascade risk**
In complex multi-agent workflows, a compromised orchestration agent can access credentials for all downstream agents. The attack surface is not a single agent — it is the trust chain between agents. One 2026 incident found compromised agent credentials harvested from 47 enterprise deployments through a single supply chain attack.

See [Strategy 2026](https://www.notion.so/337671bead5c80829f9fd254bbea72d0) for the full competitor table (Geordie, Onyx Security, JetStream, Chainguard, CyberArk, Obsidian Security, Lakera, ServiceNow, Palo Alto Networks, OneTrust/Archer).

---

## Signals Intelligence — Deep Dive

### Team vision

Inspired by the military disciplines of SIGINT (signals intelligence) and OSINT (open-source intelligence). We place lightweight sensors at the point of interaction — starting with the browser — to monitor network signals, classify data exposure, map the transitive third-party chain, and convert raw signals into actionable intelligence inside the Ethira platform.

The insight doesn't stop at "User X visited ChatGPT." It reveals what that AI tool calls underneath — sub-processors, API endpoints, data routing jurisdictions, scripts collecting data — and flags this as structured risk intelligence in the customer's operational platform where they can act on it.

### Three deployment patterns we target

From the [Zenity RSA 2026 analysis](https://zenity.io/blog/events/comprehensive-agentic-ai-security-rsa-2026) — three enterprise agent deployment patterns that need securing. The current market addresses them in fragments; nobody provides unified coverage:

1. **Endpoint agents** (targeting NOW) — Coding assistants (Cursor, Copilot, Claude Code), agentic browsers, and web-based AI tools. Our Chrome extension is the initial sensor. This is where the workforce interacts with AI daily.
2. **SaaS and embedded agents** (targeting NEXT) — AI capabilities bundled inside enterprise platforms organizations already use: CRMs, HR tools, collaboration suites. These are harder to detect because they're embedded in trusted applications. Extend coverage via API integrations and network analysis.
3. **Homegrown/custom agents** (targeting LATER) — Agents organizations build internally for their own workflows, deployed in cloud environments (AWS, Azure, GCP). SDK and workstation-level monitoring.

### Technical strategy

- **Browser-first, platform-agnostic**: Chrome extension as the initial sensor. Lightweight, deployable via MDM (Google Workspace Admin, Microsoft Intune), no network changes required. Works out of the box.
- **Transitive third-party mapping**: Go beyond surface-level URL tracking. Intercept network requests, analyze DNS/TLS to identify underlying infrastructure, detect sub-processors and data routing paths, classify endpoint jurisdictions. Not just "which app" but "what does that app use underneath."
- **Classification at the edge**: PII detection by GDPR tiers (names, emails, credit cards, government IDs, health data), shadow IT scoring based on engagement signals and authentication patterns, behavioral risk classification using fine-tuned models (e.g., nanomind-security-classifier for agentic behavior).
- **Intelligence pipeline to GRC**: Raw signals are enriched, deduplicated, and delivered to the Ethira operational platform as structured risk intelligence. Customers see actionable insights — discovered applications, PII submission events, risk signals — not raw logs. Detected third parties auto-populate in the TPRM module and trigger risk assessment workflows.

### Roadmap

**Phase 1 — Solidify the foundation (Q2 2026)**
- Harden Chrome extension PoC into production v1 (EU legal compliance completed — E-1802)
- Improve shadow IT detection accuracy — the classification algorithm needs better signals to reduce false positives
- Ship AI usage insights dashboard — surface collected data (usage times, user-to-tool mapping, PII tiers) in the Ethira UI
- Close Juni beta feedback loop (CS-101) — gather structured feedback from Josef, identify gaps, iterate

**Phase 2 — Deepen the intelligence**
- Transitive third-party chain mapping — sub-processor detection, network request analysis, jurisdiction mapping
- Policy enforcement engine — customers define what AI is allowed/blocked, the extension enforces at the browser level. Start with block/allow lists, evolve toward contextual policies (e.g., "allow ChatGPT but block file uploads containing PII")
- Risk signal integration — detected third parties auto-populate in TPRM module, new shadow AI discovery triggers risk assessment workflows in the operational platform

**Phase 3 — Expand the sensor surface**
- SDK and workstation-level monitoring — extend beyond the browser to detect coding assistants (Cursor, Copilot, Claude Code) and local AI agents
- SaaS-embedded agent detection — monitor enterprise platforms for embedded AI features and their data flows
- Agentic behavior classification — not just "which tool" but "what is the agent doing." Detect prompt injection patterns, unusual data exfiltration, risky autonomous actions

**Phase 4 — Unified AI governance**
- Cross-pattern visibility — single pane of glass across endpoint, SaaS, and homegrown agents
- Automated compliance mapping — AI usage automatically mapped to regulatory requirements (DORA, GDPR, AI Act). Compliance gaps flagged and remediation suggested
- Enforcement at scale — centralized policy engine that enforces AI governance across all deployment patterns

---

## References

- [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a) — Team structure, Q2 objectives, constraints
- [Strategy 2026 + Objectives Q2-Q3](https://www.notion.so/337671bead5c80829f9fd254bbea72d0) — Full competitive landscape, market analysis, strategic decisions
- [Browser Extension — Sales Guide](https://www.notion.so/33a671bead5c817ebabae0f9a43ee87c) — Current extension capabilities, deployment options, sales FAQ
- [Zenity: Comprehensive Agentic AI Security RSA 2026](https://zenity.io/blog/events/comprehensive-agentic-ai-security-rsa-2026) — Market landscape, three deployment patterns, fragmentation analysis
