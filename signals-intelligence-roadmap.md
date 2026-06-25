---
categories:
  - "[[Projects]]"
project: "[[Ethira]]"
created: 2026-06-23
---
# Signals Intelligence — Roadmap


## Sales 

- Risk assessment and PII detection 
- For regular users have a warning - Admin on a dashboard and user for the extension. Educate them. Track what they're clicking on and if they accept. 

- Go through the 

- Capture the signals 
- Restructure the architecture
- What do we do with the signals
-> No signals needed. Bringing the risk for the pre screening. 
- Install it on all browsers 
- Do pre screening on newly detected 
- What existing signals do we have. Do we have prescreening. 
- Visualize  risk with user and a vendor 

### High level 
Stänga deals 
- Email + Auth via DNS trafik -> Close deals 
- See till att användare 
+ Overprovision - Får mer data än vad som inkluderas i deras data. Ger för mycket provision. 

- Speed up the onboarding

![[Pasted image 20260413161421.png]]


> [!note] Guidance document
> This roadmap is derived from the [Vision, Mission & Strategy](vision-mission-strategy.md) and informed by the current state of the browser extension codebase. See also: [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a), [Strategy 2026](https://www.notion.so/337671bead5c80829f9fd254bbea72d0).

---

## Why this team exists

Enterprises are adopting AI faster than they can govern it. 79% have adopted AI agents, yet 92% lack full visibility into their AI identities. The existing security tooling landscape is fragmented — EDR, CNAPP, DSPM, and identity vendors each cover a slice but nobody provides **third-party AI visibility at the endpoint level**.

Ethira's Signals Intelligence team exists to fill this gap: place sensors at the point of interaction (starting with the browser), detect what AI tools the workforce is using, map the data flows and sub-processors behind each interaction, and feed actionable intelligence into the Ethira GRC platform. This is the **discovery and monitoring engine** that powers Ethira's AI governance story.

**Sources:**
- [Strategy 2026](https://www.notion.so/337671bead5c80829f9fd254bbea72d0) — Market analysis: "The real gap is still accountability... No commercial product owns this category."
- [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a) — "Inspired in the military discipline of SIGINT... merge SIGINT and OSINT data points to build a consolidated overview of relevant risk factors"
- [Zenity RSA 2026](https://zenity.io/blog/events/comprehensive-agentic-ai-security-rsa-2026) — Three agent deployment patterns (endpoint, SaaS-embedded, homegrown); market mirrors cloud security fragmentation circa 2015
- Lucas DM (Apr 1): "MVP: track which 3rd parties are being used, send back to ethira API to be onboarded, and then check main AI providers like GPT, Perplexity, Claude etc to see which types of data people are sending in the prompts/uploading"

---

## Linear Structure

> [!important] Linear setup needed
> Today there is **no Signals Intelligence team** in Linear. Browser extension issues (e.g., E-1802) are filed under the Engineering team. This needs to change to match the [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a) team structure.

### Team
Create a **Signals Intelligence** team in Linear (key: `SI`), mirroring AI Workflows (`AIW`) and Operational Platform (`OP`).

### Initiative
Create one initiative: **AI Monitoring & Governance**
- This is the long-term strategic bet described in Strategy 2026: "We are expanding our offering into AI observability & governance"
- Aligns with Objective 1, Focus Area 2: "Deliver a way for customers to discover what third party LLMs are used by their workforce, monitor how they are used ensuring its within policy"

### Projects (under the initiative)
Each phase of the roadmap maps to a Linear project:

| Linear Project | Phase | Target | Status |
|---|---|---|---|
| **Detection Accuracy & Data Quality** | Phase 1 | Q2 2026 | In Progress — TOP PRIORITY |
| **Browser Extension Production Hardening** | Phase 1 | Q2 2026 | In Progress |
| **AI Usage Insights Dashboard** | Phase 1 | Q2 2026 | Planned |
| **Transitive Third-Party Mapping** | Phase 2 | Q3 2026 | Backlog |
| **Policy Enforcement Engine** | Phase 2 | Q3 2026 | Backlog |
| **Risk Signal Integration** | Phase 2 | Q3 2026 | Backlog |
| **SDK & Workstation Monitoring** | Phase 3 | Q4 2026 | Backlog |

### Issues
Each project contains issues (user stories / tasks). For example, under "Browser Extension v1":
- `SI-XX: Performance audit — measure memory/CPU impact of PII scanner + AI model`
- `SI-XX: Validate Google Workspace Admin managed deployment end-to-end`
- `SI-XX: Firefox MV2 parity verification`

Existing Engineering issues should be **moved** to the SI team:
- E-1802 (EU Legal Compliance for Browser Extension) → SI team
- Any other browser-extension tagged issues

---

## Current State (as of April 2026)

### What exists today

**Browser Extension (v0.1.3)** — Chrome MV3 / Firefox MV2 / Edge MV3, built with WXT + Vite:
- **Shadow IT / SaaS discovery**: 9-signal Noisy-OR scoring engine with 70+ known providers across 6 categories (AI, SaaS, Dev Tools, Communication, Cloud, File Sharing). Detects login flows, OAuth/SSO redirects, API endpoint patterns, SSE streaming (strong AI indicator), sustained sessions, form input activity.
- **PII leak detection**: Intercepts outbound POST/PUT/PATCH/DELETE request bodies via MAIN world content script (patches `fetch`, `XMLHttpRequest`, `form.submit`). 11 recognizers with context-aware confidence boosting. Second-pass on-device AI verification via Piiranha DeBERTa-v3-base NER model (ONNX int8 quantized). Detects GDPR special categories by field name matching.
- **Privacy-by-design**: Only domain names stored (never full URLs). PII categories reported, never raw values. Body snippets used for AI verification then discarded.
- **Dual auth**: OAuth PKCE for individual users, enterprise ingest tokens for MDM deployment.
- **API integration**: Batched ingestion to `/v1/browser-monitoring/` endpoints with idempotent delivery (UUID client record IDs, deduplication server-side). Auto-discovers domains into `unverified_nth_parties` table.
- **Admin dashboard**: Discovered Applications view with activity aggregation, PII counts, user-level stats, pre-screening status.
- **EU legal compliance**: Acknowledgment flow, pause/resume, privacy controls (E-1802 completed).
- **Juni beta**: CS-101 in progress, gathering early feedback from Josef.

**Source:** Lucas demo in #all-demos-and-feedback (Apr 4): "Trying out the browser extension, captured a bunch of data in the background which is not in the UI yet, like PII detection according to GDPR PII tiers, usage times, pinpointing users to usage"

### What's weak or missing

- **Shadow IT classification accuracy** — the Noisy-OR algorithm needs better signals and tuning
  - *Source:* Lucas (Apr 4, #all-demos-and-feedback): "The algorithm for detecting PII and to define if something is shadow IT is a bit weak yet, but something we'll need to plan in more details later how to improve and collect signals that will make it more accurate"
- **No transitive third-party mapping** — we track which domains users visit, but not what those domains call underneath (sub-processors, API backends, data routing)
  - *Source:* Hugo's input + Strategy 2026 Layer 2 ("Agentic dependency stack... This is an SBOM problem applied to AI — and unlike software SBOMs, no standard or tooling exists")
- **No policy enforcement** — monitoring only, no block/allow capability
  - *Source:* Engineering Direction Q2 objective 3: "Collect signals that enable ethira to build an enforcement capability which will allow customers to centrally define what AI is allowed or not to execute and enforce it across workstations and browsers"
- **No risk signal integration** — discovered applications don't automatically trigger TPRM risk assessment workflows
  - *Source:* Strategy 2026: "We will need to prove... we have the technical depth to be a trust and assurance layer on a technical level, which becomes an enabler of AI adoption rather than a compliance tool"
- **No SDK/workstation monitoring** — browser-only, blind to coding assistants (Cursor, Copilot, Claude Code) and local AI agents
  - *Source:* Lucas (#team-engineering, Apr 8): "As we move from browser-only detection to SDK and Workstation analysis this will come in super handy to classify the behavior we spot" (re: nanomind-security-classifier)
- **Provider catalog is static** — 70+ domains hardcoded, no dynamic discovery or community-sourced updates
- **No jurisdiction mapping** — we know the domain but not where the endpoint is hosted or where data is routed
  - *Source:* Engineering Direction overview: "in which countries are the endpoints based, what vendors are configured in the DNS domains, who are their sub-processors"

---

## Phase 1 — Solidify the Foundation (Q2 2026, current)

> **Why now:** This is directly from the [Engineering Direction Q2 deliverables](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a): Chrome plugin, Shadow IT detection improvement, AI usage insights. We need a production-quality v1 to land our first customers on the AI monitoring module. Juni (CS-101) is already in beta — their feedback shapes what "production-ready" means.
>
> **Strategic connection:** Strategy 2026 Objective 1, Focus Area 2: "Deliver a way for customers to discover what third party LLMs are used by their workforce, monitor how they are used ensuring its within policy." Also supports the land-and-expand GTM — shadow AI visibility is the **land** module.
>
> **Linear:** Projects under initiative "AI Monitoring & Governance", owned by SI team.

**Goal**: Ship a production-quality v1 with accurate detection that customers can deploy and trust.

> **Team capacity**: 4 engineers. Work sequentially on high-priority items — don't spread across all 3 projects at once. Accuracy and correctness come first, then hardening, then dashboard.

### 1.1 Detection Accuracy & Data Quality (Linear Project — START HERE)

**Why this is #1:** If the data is wrong, nothing else matters. Two critical bugs exist today, plus the signal weights are uncalibrated. Lucas flagged accuracy directly (Apr 4). Fixing this is prerequisite to any customer demo or sales motion.

**Issues (ordered by priority):**

---

**SI-1: Normalize domains to a canonical provider identifier** `Urgent`

*Problem:* The ingestion service (`browsing-activity-ingestion.service.ts:upsertDiscoveredDomains()`) uses the raw hostname from the browser tab as `serviceIdentifier`. The provider catalog has duplicate entries for the same provider: `app.notion.so` + `notion.so`, `slack.com` + `app.slack.com`, `npmjs.com` + `www.npmjs.com`, `dropbox.com` + `www.dropbox.com`. This means the same provider appears **multiple times** in the Discovered Applications dashboard.

*Why it matters:* Customers immediately lose trust when they see Notion listed twice. It also inflates provider counts in reporting and breaks any aggregation that groups by domain.

*What to do:* When ingesting browsing activity, resolve the raw domain to a canonical form before upserting into `unverified_nth_parties`. For known catalog entries, use the catalog's base domain (e.g., `app.notion.so` → `notion.so`). For unknown domains, strip `www.` and common subdomains (`app.`, `dashboard.`, `console.`). Also write a one-time migration to merge existing duplicate records.

*Files:* `browsing-activity-ingestion.service.ts`, `provider-catalog.ts` or `url-anonymizer.ts` (new `canonicalizeDomain()`)

---

**SI-2: Remove duplicate entries from provider catalog** `High`

*Problem:* The catalog lists both subdomain and base domain for several providers. Since `lookupKnownProvider()` already walks up the domain tree, subdomain variants are unnecessary.

*Why it matters:* Inflates coverage numbers. Makes catalog maintenance confusing. Masks real gaps.

*What to do:* Keep only the canonical (shortest) domain per provider. Remove: `app.notion.so` (keep `notion.so`), `app.slack.com` (keep `slack.com`), `www.npmjs.com` (keep `npmjs.com`), `www.dropbox.com` (keep `dropbox.com`), `chat.openai.com` (keep `chatgpt.com`).

*Files:* `provider-catalog.ts`

---

**SI-3: Build labeled ground truth dataset and measure accuracy baseline** `High`

*Problem:* We don't know how accurate detection is. Lucas said "a bit weak" but we don't know the false positive rate, false negative rate, or where it fails.

*Why it matters:* Can't improve what we don't measure. This baseline tells us where to focus tuning.

*What to do:* Export 200+ domains from `browsing_activity_records` (internal dogfooding + Juni beta). Manually label each. Compare against extension's `providerClassification`. Calculate precision, recall, F1. Identify worst false positive/negative patterns.

*Blocked by:* Needs real usage data (start with internal dogfooding; add Juni data via CS-101 when available).

---

**SI-4: Tune Noisy-OR signal weights based on real data** `High`

*Problem:* Weights are gut estimates: `KNOWN_PROVIDER_DOMAIN: 0.90`, `LOGIN_FLOW: 0.55`, `SSE_STREAMING: 0.40`, etc. Classification thresholds (0.80/0.50/0.25) are also unvalidated.

*Why it matters:* Better weights directly improve accuracy. Highest-ROI change for detection quality.

*What to do:* Using labeled data from SI-3, find optimal weights via logistic regression or manual analysis. Test new vs old weights on the labeled set before deploying.

*Files:* `provider-detector.ts`, `constants.ts`
*Blocked by:* SI-3

---

**SI-5: Expand AI provider catalog to 150+ entries** `High`

*Problem:* ~30 AI entries in the catalog. Windsurf, Lovable, Devin, Codeium, Mistral Le Chat, xAI Grok, Amazon Q are all missing. Missing a known tool in a demo is a product embarrassment.

*Why it matters:* Known provider match = 0.90 weight (strongest signal). Expanding the catalog is the easiest way to improve recall. Low effort, high impact.

*What to do:* Research top 100+ AI tools. Sources: Product Hunt AI, AlternativeTo, G2 AI. Add with granular subcategories.

*Files:* `provider-catalog.ts`

---

**SI-6: Add dynamic AI detection for uncatalogued tools** `Medium`

*Problem:* Catalog can never be complete. For unknown domains, we rely on weak signals (hostname pattern: 0.15, engagement: 0.15-0.25).

*Why it matters:* This lets us claim "we detect unknown AI tools" — not just the ones we've listed.

*What to do:* Add network-layer signals: LLM URL patterns (`/v1/chat/completions`, `/v1/embeddings`, `/generate`), large text → streaming output ratio. Fire alongside existing SSE detection.

*Files:* `provider-detector.ts`, `outbound-request-pii-interceptor.content.ts`
*Depends on:* SI-4 (new weights should account for new signals)

---

### 1.2 Browser Extension Production Hardening (Linear Project)

**Why:** Enterprise customers need reliable, performant, MDM-deployable software. The [Sales Guide](https://www.notion.so/33a671bead5c817ebabae0f9a43ee87c) promises enterprise deployment — we need to deliver.

**Issues:**

---

**SI-7: Performance audit — memory/CPU impact** `High`

*Problem:* Extension runs on-device DeBERTa-v3 ONNX model, patches fetch/XHR on every page, tracks engagement per tab. Runtime cost is unknown.

*Why it matters:* If the extension slows the browser, employees complain and IT uninstalls it.

*What to do:* Profile memory, CPU spikes during flush, page load impact. Chrome DevTools + `chrome://extensions` inspector. Test with 10+ tabs. Document findings.

---

**SI-8: Validate managed deployment end-to-end** `High`

*Problem:* We promise Google Workspace Admin and Intune push but haven't validated the full flow.

*Why it matters:* Gate for enterprise customer acquisition. Juni won't self-install.

*What to do:* Test: silent MDM install, ingest token from managed storage, data flows without login, survives Chrome updates. Document setup for customers.

---

**SI-9: Patch onnxruntime-node vulnerability** `Medium` *(existing: E-1815)*

*What:* Lockfile resolves vulnerable `onnxruntime-node`. Crafted input → unintended memory reads.

*Why:* Security vulnerability in a security product.

---

**SI-10: Firefox MV2 and Edge MV3 parity** `Medium`

*What:* Verify extension on Firefox and Edge. Fix behavior differences.

*Why:* Sales Guide promises Chrome and Edge.

---

### 1.3 AI Usage Insights Dashboard (Linear Project)

**Why:** Q2 deliverable from [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a). Data collected but "not in the UI yet" (Lucas, Apr 4). Without a dashboard, the product is invisible.

> **Co-owned with Operational Platform** — SI owns data model and API; OP may own UI.

**Issues:**

---

**SI-11: Discovered Applications overview page** `High`

*What:* Dashboard listing all discovered apps: domain, category, classification, active users, active time, PII categories, first/last seen. Sortable, filterable ("AI tools only", "with PII exposure").

*Why:* Primary value screen. CISO opens Ethira → "here's every AI tool your people are using."

*Backed by:* Existing `DiscoveredApplicationQueryService` and API endpoints.

---

**SI-12: User-level activity drill-down** `High`

*What:* Click discovered app → which users, time per user, PII categories per user.

*Why:* "Who is using ChatGPT and what are they sending?" — the drill-down from overview.

*Backed by:* Existing `/:domain/user-stats` endpoint.

---

**SI-13: Time-series usage trends** `Medium`

*What:* Line charts: daily/weekly usage per app or category.

*Why:* Trends tell the compliance story over time.

---

**SI-14: Export for compliance reporting** `Medium`

*What:* CSV export of discovered apps and user activity. Optional PDF summary.

*Why:* Compliance teams attach evidence to audit reports.

---

### 1.4 Juni Beta Feedback (tracked under Detection Accuracy project)

**Why:** Juni is our first customer (CS-101). Feedback gets triaged into accuracy bugs (→ 1.1) or UI gaps (→ 1.3). Not a separate project.

- [ ] Structured feedback from Josef (CS-101, owned by Sales/CS)
- [ ] Triage into SI issues
- [ ] Weekly sync with Sales on status

---

## Phase 2 — Deepen the Intelligence (Q3 2026)

> **Why now:** Phase 1 gives us visibility (what AI tools are used). Phase 2 gives us **depth** (what those tools use underneath) and **control** (enforcement). This is what separates Ethira from every other shadow AI tool. Per Strategy 2026: "The real gap is still accountability — the ability to answer, after the fact, what an agent did, why, on whose behalf, with what data, and through which dependencies."
>
> **Strategic connection:** Strategy 2026, competitive gap: "nobody combines runtime forensics + supply chain attestation + EU regulatory depth." Phase 2 delivers the supply chain attestation (transitive mapping) and the enforcement layer.
>
> Engineering Direction Q2 objective 3 (enforcement) is aspirational for Q2 but will realistically land in Q3 given Phase 1 priorities.
>
> **Linear:** Three projects under initiative "AI Monitoring & Governance", owned by SI team.

**Goal**: Move from "which app" to "what does that app use underneath" + enable enforcement.

### 2.1 Transitive Third-Party Chain Mapping (Linear Project)

**Why:** This is our **key differentiator**. Every shadow AI tool on the market tells you "your employees are using ChatGPT." We tell you "ChatGPT routes through Azure OpenAI in East US, loads Datadog and Segment analytics scripts, and the browser plugin calls a third-party in Singapore with no GDPR adequacy decision." This is what DORA Article 30 requires for sub-outsourcing visibility and what no competitor delivers.

*Source:* Engineering Direction: "who are their sub-processors, which are the scripts collecting data when they access the pages." Hugo's vision: not just "which app" but "what does that app use underneath."

See [PRD: Transitive Third-Party Mapping](signals-intelligence-prd.md#transitive-third-party-chain-mapping) for full specification.

- [ ] Network request interception: capture outbound requests from monitored domains to third-party backends
- [ ] DNS/TLS analysis: resolve endpoint infrastructure, identify hosting providers and CDN layers
- [ ] Sub-processor detection: map which services a visited AI tool calls (e.g., ChatGPT → Azure OpenAI → Bing API)
- [ ] Jurisdiction mapping: GeoIP resolution of endpoint IPs, flag adequacy decision mismatches
- [ ] Feed discovered sub-processors back into the TPRM module as linked entities

### 2.2 Policy Enforcement Engine (Linear Project)

**Why:** Monitoring without enforcement is a half-solution. The Q2 objective says it explicitly: "Collect signals that enable ethira to build an enforcement capability which will allow customers to centrally define what AI is allowed or not to execute and enforce it across workstations and browsers in the organizations." Customers will ask "I can see my employees are using unauthorized AI — now how do I stop them?"

*Source:* Engineering Direction Q2 objective 3. Also Strategy 2026 mission: "enforcing policies & contracts in real time."

See [PRD: Policy Enforcement](signals-intelligence-prd.md#policy-enforcement-engine) for full specification.

- [ ] Block/allow list: admin defines permitted and blocked domains/categories
- [ ] Extension enforces at navigation time: blocked domains show an interstitial page
- [ ] Contextual policies: allow a tool but block specific actions (e.g., "allow ChatGPT but block file uploads")
- [ ] Policy sync: extension pulls latest policy set from API on startup and periodically
- [ ] Audit trail: all enforcement actions logged for compliance

### 2.3 Risk Signal Integration (Linear Project)

**Why:** Today, discovered applications live in a silo — the browser monitoring dashboard shows what's been found, but nothing connects to the TPRM workflow. When new shadow AI is detected, no risk assessment is triggered, no one is notified, no one evaluates. The signal dies in the dashboard. This closes the **SIGINT → Operational Platform loop** — the whole point of the three-team structure from Engineering Direction.

*Source:* Engineering Direction: "Those signals shall be converted into intelligence and then be placed into the operational platform so customers can act." Strategy 2026: the closed loop from detection to action is what makes us a platform, not a point tool.

See [PRD: Risk Signal Integration](signals-intelligence-prd.md#risk-signal-integration) for full specification.

- [ ] Auto-populate discovered third parties in TPRM module (extend existing `unverified_nth_parties` → risk entity pipeline)
- [ ] Trigger risk assessment workflows when new shadow AI is detected
- [ ] PII exposure events create risk findings linked to the third party
- [ ] Notification to risk owners when high-risk tools are detected (via NotificationService)

---

## Phase 3 — Expand the Sensor Surface (Q4 2026)

> **Why now:** By Q4, we'll have a proven browser-based monitoring + enforcement platform. But the Zenity RSA analysis shows three deployment patterns enterprises need to secure. We only cover pattern 1 (endpoint agents via browser). Phase 3 expands to cover patterns 1b (workstation-level) and 2 (SaaS-embedded). This moves us from "shadow AI detection tool" to "AI governance platform."
>
> **Strategic connection:** Strategy 2026 risk: "Partial solutioning risk — if we start solving the 3rd party risk, companies will still start by looking for a 1st party risk solution." Expanding the sensor surface is how we prevent being outflanked by first-party-focused competitors who eventually add third-party coverage.
>
> **Linear:** Projects under initiative "AI Monitoring & Governance", owned by SI team.

**Goal**: See beyond the browser — coding assistants, local agents, SaaS-embedded AI.

### 3.1 SDK / Workstation Monitoring (Linear Project)

**Why:** Lucas flagged this direction (Apr 8, #team-engineering): "As we move from browser-only detection to SDK and Workstation analysis this will come in super handy to classify the behavior we spot." Coding assistants (Cursor, Copilot, Claude Code) are the fastest-growing AI endpoint category. They operate outside the browser, so our current sensor is blind to them.

*Source:* Zenity RSA 2026: endpoint agents include "coding assistants and agentic browsers." Lucas shared nanomind-security-classifier + hackmyagent as tools for this.

- [ ] Research: how coding assistants expose telemetry or can be observed
- [ ] Approach options: OS-level network monitoring, IDE plugin integration, process-level observation
- [ ] Define data model: extend browsing activity schema or create new `workstation_activity_records`
- [ ] Privacy considerations: same privacy-by-design principles (no code content, only tool + metadata)

### 3.2 SaaS-Embedded Agent Detection (Linear Project)

**Why:** The second deployment pattern from Zenity: "SaaS and embedded agents that come bundled inside the enterprise platforms organizations already use, from CRMs to HR tools to collaboration suites." Salesforce Einstein, ServiceNow, Microsoft 365 Copilot — these are AI agents hidden inside trusted platforms. Customers don't even know they're active.

- [ ] Identify enterprise platforms with embedded AI features
- [ ] Detection approach: recognize AI-specific network patterns from within these platforms (SSE streaming, model API calls)
- [ ] API integration where platforms expose AI usage APIs
- [ ] Enrich provider catalog with embedded AI identifiers

### 3.3 Agentic Behavior Classification (Linear Project)

**Why:** Today we detect tool presence but not what the agent is doing. Strategy 2026 Layer 3 (multi-agent cascade risk) describes how a "compromised orchestration agent can access credentials for all downstream agents." To detect this, we need behavioral classification — not just "which tool" but "is this tool behaving normally or is it exfiltrating data?"

*Source:* Strategy 2026 market data: "47% have already seen unauthorised or unintended AI agent behaviour." Lucas shared nanomind-security-classifier and hackmyagent as relevant tools.

- [ ] Integrate behavioral classification model (nanomind-security-classifier or similar)
- [ ] Classify: normal usage, prompt injection attempt, data exfiltration pattern, autonomous action chain
- [ ] Severity scoring: map behavioral classifications to risk levels
- [ ] Alert generation: high-severity behaviors trigger immediate notification

---

## Phase 4 — Unified AI Governance (2027)

> **Why:** This is the end state described in the vision. Strategy 2026: "consolidate as a leader in secure AI adoption enablement." When we cover all three deployment patterns with unified visibility, enforcement, and compliance mapping, we own a category that no competitor has claimed.

**Goal**: Single pane of glass across all deployment patterns.

### 4.1 Cross-Pattern Visibility
- [ ] Unified dashboard: endpoint + SaaS + homegrown agents in one view
- [ ] Entity resolution: same third party seen across browser, SDK, and SaaS contexts linked as one entity
- [ ] Organization-wide AI inventory: complete map of all AI tools and agents in use

### 4.2 Automated Compliance Mapping
- [ ] Map AI usage to regulatory requirements (DORA Article 30, GDPR, EU AI Act)
- [ ] Gap detection: flag AI tools that don't meet regulatory requirements
- [ ] Evidence generation: automatic audit trail documentation for compliance reviews

### 4.3 Enforcement at Scale
- [ ] Centralized policy engine spanning all sensor types
- [ ] Graduated enforcement: warn → require justification → block
- [ ] Integration with identity providers for context-aware policies (role-based, department-based)

---

## Dependencies on Other Teams

| Dependency | Team | Phase | What's needed | Source |
|---|---|---|---|---|
| Dashboard UI for AI usage insights | Operational Platform | Phase 1 | New views in the Ethira frontend | Eng Direction Q2 deliverable: "AI usage insights" |
| Risk assessment workflow triggers | Operational Platform | Phase 2 | API to create risk findings from SIGINT signals | Eng Direction: "signals converted into intelligence placed into operational platform" |
| TPRM entity linking for sub-processors | Operational Platform | Phase 2 | Extend nth-party entity model for transitive relationships | Strategy 2026 Layer 2: agentic dependency stack |
| Custom automation triggers from SIGINT events | AI Workflows | Phase 2 | Event bus / webhook for "new shadow AI detected" | Eng Direction: AI Workflows team enables automations |
| Notification routing for enforcement alerts | Operational Platform | Phase 2 | NotificationService integration | CLAUDE.md notification architecture |
