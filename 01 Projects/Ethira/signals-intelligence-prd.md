# Signals Intelligence — Product Requirements Document

> [!note] Guidance document
> This PRD covers the next major capabilities for the Signals Intelligence team. It builds on what already exists (browser extension v0.1.3) and is aligned with the [Vision, Mission & Strategy](vision-mission-strategy.md) and [Roadmap](signals-intelligence-roadmap.md).
>
> **Linear mapping:** Each PRD section corresponds to a Linear **project** under the SI team's "AI Monitoring & Governance" initiative. Issues within each project should reference the relevant requirement IDs (R1, R2, etc.) from this document.

---

## Table of Contents
- [Transitive Third-Party Chain Mapping](#transitive-third-party-chain-mapping) — Phase 2, Linear Project
- [Policy Enforcement Engine](#policy-enforcement-engine) — Phase 2, Linear Project
- [Risk Signal Integration](#risk-signal-integration) — Phase 2, Linear Project
- [Shadow IT Detection Improvements](#shadow-it-detection-improvements) — Phase 1, Linear Project

---

## Transitive Third-Party Chain Mapping

> **Linear:** Project under SI team, Phase 2 (Q3 2026)
> **Why this matters:** This is our **key differentiator** — what separates Ethira from every shadow AI tool on the market. Every competitor tells you "your employees are using ChatGPT." We tell you what ChatGPT calls underneath.
>
> **Sources:**
> - [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a): "in which countries are the endpoints based, what vendors are configured in the DNS domains, who are their sub-processors, which are the scripts collecting data when they access the pages"
> - [Strategy 2026](https://www.notion.so/337671bead5c80829f9fd254bbea72d0), Layer 2: "Agentic dependency stack — First-party agents depend on components you did not build: MCP servers, open-source agent frameworks, model registries... This is an SBOM problem applied to AI — and unlike software SBOMs, no standard or tooling exists."
> - Hugo's vision input: "not only monitor which applications a user uses, but also what third-party system that application is using"
> - DORA Article 30 sub-outsourcing requirements — customers need to report the full chain of ICT service providers

### Problem

Today the browser extension tells us "User X spent 45 minutes on ChatGPT and submitted data containing email addresses." What it doesn't tell us is:
- ChatGPT routed the conversation through an Azure OpenAI endpoint in East US
- The page loaded scripts from 3 analytics providers (Segment, Amplitude, Datadog)
- A browser plugin API call was made to a third-party service hosted in a jurisdiction with no GDPR adequacy decision
- The AI tool's backend called a sub-processor for embeddings search hosted in Singapore

This is the **transitive third-party chain** — the invisible supply chain behind every AI interaction. Customers need this to fulfil DORA Article 30 requirements around sub-outsourcing and to understand their true data exposure.

### Current State

The extension already intercepts outbound requests via `outbound-request-pii-interceptor.content.ts` — it patches `fetch`, `XMLHttpRequest`, and `form.submit` in the MAIN world. However, it only scans request **bodies** for PII. It does not:
- Record the destination domains of these outbound requests (beyond the page domain)
- Analyze response headers for infrastructure signals
- Track script origins loaded on the page
- Resolve IP addresses to jurisdictions

The API side already has `unverified_nth_parties` for auto-discovered domains. This can be extended to model transitive relationships (parent → sub-processor).

### Requirements

#### Extension Side

**R1 — Outbound request domain capture**
When the user is on a monitored page (provider score >= `medium`), capture the **destination domains** of all outbound network requests (fetch, XHR, WebSocket connections). Store only the hostname, not the full URL or payload.

Data to collect per request:
- `sourceDomain`: the page the user is on
- `destinationDomain`: where the request is going
- `requestType`: `fetch` | `xhr` | `websocket` | `script` | `stylesheet` | `image`
- `responseContentType`: from response headers (especially `text/event-stream` for AI inference calls)
- `detectedAt`: timestamp

Privacy constraint: No request/response bodies captured for this feature. PII scanning remains a separate pipeline.

**R2 — Script origin tracking**
On monitored pages, enumerate all `<script>` elements and their `src` domains. This reveals which third-party scripts are loaded (analytics, tracking, A/B testing, AI widgets). Collect once per page load, not continuously.

**R3 — Infrastructure signal extraction**
From response headers of outbound requests, extract:
- `Server` header (e.g., `cloudflare`, `AmazonS3`, `gws`)
- `X-Powered-By` header
- `Via` header (proxy/CDN chain)
- `CF-RAY` or similar CDN identifiers
- TLS certificate issuer and subject (via `chrome.webRequest` if available, or `SecurityInfo` API on Firefox)

These signals help identify the hosting provider and CDN layer without DNS resolution.

**R4 — Batched ingestion**
New API endpoint: `POST /v1/browser-monitoring/third-party-signals`
```json
{
  "userEmail": "jane@company.com",
  "signals": [
    {
      "sourceDomain": "chatgpt.com",
      "destinationDomain": "browser-intake-datadoghq.com",
      "requestType": "fetch",
      "responseContentType": "application/json",
      "infrastructureHints": { "server": "cloudflare", "via": "1.1 google" },
      "detectedAt": 1744208525000,
      "clientRecordId": "uuid"
    }
  ]
}
```

Flush interval: align with PII flush (every 5 minutes). Buffer cap: 300 signals.

#### API Side

**R5 — Third-party signal ingestion service**
New controller + service mirroring the existing ingestion pattern:
- Deduplicate by `clientRecordId`
- Store in new `third_party_signals` table
- Auto-discover destination domains into `unverified_nth_parties`

**R6 — Transitive relationship model**
Extend the entity model to represent: "Domain A loads/calls Domain B":
- New table or relation: `nth_party_dependencies(source_domain, destination_domain, relationship_type, first_seen_at, last_seen_at, signal_count, workspace_id)`
- `relationship_type`: `api_call` | `script_load` | `websocket` | `redirect` | `cdn`
- Aggregated from raw signals — a background job or materialized view

**R7 — Jurisdiction mapping**
For each unique destination domain, resolve the IP and map to a country via GeoIP (MaxMind GeoLite2 or similar):
- Run as a background enrichment job, not real-time in the extension
- Store `country_code`, `region`, `hosting_provider` on the `unverified_nth_parties` record
- Flag domains in jurisdictions without GDPR adequacy decisions

**R8 — Sub-processor discovery dashboard**
Extend the Discovered Applications view:
- For each discovered application, show its detected sub-processors/third-party dependencies
- Visualize the dependency chain (app → sub-processors → their sub-processors)
- Highlight jurisdiction mismatches and unassessed dependencies
- Link sub-processors to existing TPRM entities if they match

### Technical Approach

The existing MAIN world content script (`outbound-request-pii-interceptor.content.ts`) already patches `fetch` and `XMLHttpRequest`. The request domain capture (R1) can be added to the same interception layer — when a request is intercepted for PII scanning, also extract the destination domain and response headers.

Script origin tracking (R2) is a new lightweight content script that runs once at `document_idle` — enumerates `document.querySelectorAll('script[src]')` and extracts hostnames.

Infrastructure signals (R3) are extracted from the response object already available in the patched `fetch` — `response.headers.get('server')`, etc.

The key architectural decision is **where to do the aggregation**: raw signals are high-volume (every outbound request on every monitored page). Options:
1. **Aggregate in extension**: group signals by (source, destination) pair before sending. Pro: lower API volume. Con: more extension complexity.
2. **Send raw, aggregate server-side**: simpler extension, API handles dedup and aggregation. Pro: richer data. Con: higher ingestion volume.

**Recommendation**: Aggregate in extension — group by (source, destination, requestType) per flush interval, send counts instead of individual events. Keeps the ingestion volume manageable and follows the existing batching pattern.

### Success Criteria
- For a monitored AI tool (e.g., ChatGPT), the dashboard shows its detected third-party dependencies within 24h of first use
- Jurisdiction mapping identifies at least the hosting country for 80%+ of detected endpoints
- Sub-processor relationships are visible in the Discovered Applications view

### Open Questions
- Should we capture WebSocket frame metadata (not content) for real-time AI streaming detection?
- How deep should the transitive chain go? (App → sub-processor is one hop; sub-processor → their dependencies is two hops — likely out of scope for Phase 2)
- Do we need consent/acknowledgment UI changes for this additional data collection?

---

## Policy Enforcement Engine

> **Linear:** Project under SI team, Phase 2 (Q3 2026)
> **Why this matters:** Monitoring without enforcement is a half-solution. The Q2 objective says it explicitly — and this is what closes the deal for customers who need more than visibility.
>
> **Sources:**
> - [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a), Q2 objective 3: "Collect signals that enable ethira to build an enforcement capability which will allow customers to centrally define what AI is allowed or not to execute and enforce it across workstations and browsers in the organizations"
> - [Strategy 2026](https://www.notion.so/337671bead5c80829f9fd254bbea72d0), mission: "enforcing policies & contracts in real time"
> - Strategy 2026, competitive gap: nobody combines runtime forensics + enforcement + EU regulatory depth

### Problem

Monitoring without enforcement is a half-solution. Customers say "I can see my employees are using unauthorized AI tools — now how do I stop them?" Today, the extension is read-only. Customers need the ability to centrally define policies and enforce them at the browser level.

### Current State

The extension has no enforcement capability. It observes and reports. The `background.ts` service worker handles tab navigation events but takes no blocking action.

The provider catalog and Noisy-OR scoring engine provide the classification foundation — we already know if a domain is a known AI tool, what category it belongs to, and how confident we are.

### Requirements

**R1 — Policy definition (API side)**
New entity: `browser_enforcement_policy`
```
- id: UUID
- workspaceId: UUID
- name: string
- type: 'block_domain' | 'block_category' | 'warn_domain' | 'warn_category' | 'allow_domain'
- target: string (domain or category name)
- action: 'block' | 'warn' | 'allow'
- message: string (shown to user on block/warn)
- isEnabled: boolean
- createdBy: UUID
- createdAt, updatedAt: timestamps
```

Admin UI: CRUD for policies. Preset templates: "Block all AI tools", "Allow approved AI tools only", "Warn on unknown SaaS".

**R2 — Policy sync (extension side)**
- On startup and every 15 minutes, extension fetches active policies: `GET /v1/browser-monitoring/enforcement-policies`
- Policies cached in `browser.storage.local`
- Policies evaluated locally — no API call per navigation

**R3 — Navigation-time enforcement**
When a tab navigates to a new domain:
1. Check domain against `allow` policies (explicit allowlist takes priority)
2. Check domain against `block_domain` policies
3. Check category (from provider catalog or Noisy-OR classification) against `block_category` policies
4. Check against `warn` policies

Actions:
- **Block**: Redirect to an extension-hosted interstitial page explaining the policy and offering a "Request exception" button
- **Warn**: Show a banner/overlay on the page with the warning message and a "Continue anyway" button. Log the user's choice.
- **Allow**: No action (explicitly permitted)
- **No matching policy**: Default behavior (monitor only, as today)

**R4 — Contextual policies (future)**
Phase 2.5 — more granular enforcement:
- "Allow ChatGPT but block file uploads" — intercept form submissions with file inputs
- "Allow AI tools but warn when PII is detected in the request" — combine PII scanner with enforcement
- "Block AI tools outside business hours" — time-based policies

Start with domain/category block/warn/allow in Phase 2. Contextual policies in a follow-up.

**R5 — Enforcement audit trail**
Every enforcement action logged:
```json
{
  "userEmail": "jane@company.com",
  "domain": "chatgpt.com",
  "policyId": "uuid",
  "action": "blocked",
  "userResponse": null,  // or "requested_exception" / "continued_anyway"
  "timestamp": 1744208525000
}
```

New ingestion endpoint: `POST /v1/browser-monitoring/enforcement-events`

**R6 — Exception request flow**
When blocked, users can request an exception:
- Click "Request exception" on interstitial page
- Extension sends request to API with user email, domain, reason (optional text field)
- Admin sees pending exception requests in dashboard
- Admin approves/rejects → creates a user-specific or workspace-wide `allow_domain` policy

### Technical Approach

Navigation-time enforcement uses `chrome.webNavigation.onBeforeNavigate` (or `browser.webNavigation`) to intercept before the page loads. For blocking, redirect to `chrome-extension://<id>/blocked.html?domain=...&policy=...&message=...`.

Warning overlays use a content script injected at `document_start` that checks the domain against cached policies and shows a dismissible banner.

Policy evaluation is a simple priority-based matcher:
1. User-specific allow (from approved exception) → allow
2. Domain-level block → block
3. Category-level block → block
4. Domain-level warn → warn
5. Category-level warn → warn
6. Default → monitor only

### Success Criteria
- Admin can define a "Block all AI tools" policy and it takes effect within 15 minutes on all managed extensions
- Blocked users see a clear interstitial explaining why and how to request an exception
- All enforcement actions appear in the audit trail within 5 minutes

### Open Questions
- Should enforcement policies sync via Chrome managed storage (GPO/MDM) for enterprises that don't want users to be able to disable the extension?
- Do we need an "emergency kill switch" that immediately blocks all AI tools workspace-wide (e.g., during an incident)?
- How do we handle domains that are both legitimate work tools and AI tools (e.g., Microsoft Teams with Copilot embedded)?

---

## Risk Signal Integration

> **Linear:** Project under SI team, Phase 2 (Q3 2026)
> **Why this matters:** This closes the **SIGINT → Operational Platform loop** — the entire premise of the three-team structure. Without this, signals intelligence is a standalone dashboard that doesn't drive action. With this, every shadow AI discovery automatically becomes a risk assessment in the customer's TPRM workflow.
>
> **Sources:**
> - [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a): "Those signals shall be converted into intelligence and then be placed into the operational platform so customers can act"
> - [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a), Operational Platform overview: "The operational platform team will be central in enabling the work of signals intelligence, since those signals will be converted into information and inserted in the platform"
> - [Strategy 2026](https://www.notion.so/337671bead5c80829f9fd254bbea72d0): "We will need to prove... we have the technical depth to be a trust and assurance layer on a technical level, which becomes an enabler of AI adoption rather than a compliance tool"

### Problem

Today, discovered applications live in a silo — the browser monitoring dashboard shows what's been found, but it doesn't connect to the TPRM workflow. When a new shadow AI tool is discovered, no one is automatically notified, no risk assessment is triggered, and no one is assigned to evaluate it. The signal dies in the dashboard.

### Current State

The ingestion service already auto-upserts discovered domains into `unverified_nth_parties` with `integrationType = BROWSER_EXTENSION`. The `DiscoveredApplicationQueryService` joins activity data with pre-screening status. But there's no event/trigger system — it's pull-only (admin has to open the dashboard and look).

### Requirements

**R1 — New third-party detection event**
When `BrowsingActivityIngestionService.upsertDiscoveredDomains()` creates a **new** `unverified_nth_parties` record (not an update to existing), emit a domain event: `NewThirdPartyDiscoveredEvent { domain, category, providerClassification, firstSeenByUser, workspaceId }`.

**R2 — Automatic risk entity creation**
On `NewThirdPartyDiscoveredEvent`:
- If the domain matches an existing third party in the workspace's TPRM inventory → link the browser monitoring data to that entity
- If no match → create a new third-party entity in "pending review" status with the data from the extension (category, classification, PII exposure if any, user count)

**R3 — Risk assessment workflow trigger**
When a new third party is created from browser monitoring:
- If the provider is classified as `high` confidence AI tool → auto-trigger a risk assessment workflow (create a risk assessment task assigned to the workspace's default risk owner)
- If classified as `medium` → create a "review needed" item in the risk backlog
- If classified as `low` → log only, no workflow trigger

**R4 — PII exposure as risk finding**
When PII submission events are ingested for a third party:
- Create or update a risk finding on the linked third-party entity
- Finding type: "PII Data Exposure"
- Severity based on GDPR tier: special categories (health, biometric, genetic) → Critical; standard identifiers (email, phone, credit card) → High; basic fields (name, address) → Medium
- Include: PII categories detected, user count, date range, destination domain

**R5 — Notification to stakeholders**
On new high-confidence shadow AI discovery:
- Notify workspace risk owners via `NotificationService.sendWithFallback()` (Slack + email fallback)
- Template: "New AI tool detected: {domain} — {userCount} users, {piiCategories} data exposure detected. Review in Ethira."
- Follow the notification architecture in CLAUDE.md (template in `domain/notification/templates/`, target builder, NotificationService router)

**R6 — Dashboard integration**
Extend the Discovered Applications view:
- Show TPRM status for each discovered app (linked to risk entity? assessment in progress? approved? blocked?)
- One-click "Start risk assessment" button for unreviewed discoveries
- Filter: "Show only unreviewed AI tools with PII exposure"

### Technical Approach

The domain event can use the existing NestJS EventEmitter pattern or a BullMQ job. Since this is a side-effect of ingestion (not latency-sensitive for the extension response), a BullMQ job is preferable — it decouples ingestion from downstream processing and handles retries.

The risk entity creation and linking touches the existing third-party domain model. Need to coordinate with the Operational Platform team on the entity model extension (new `source` field or `discoveredVia` enum on the third-party entity).

### Success Criteria
- Within 30 minutes of a new AI tool being detected by the extension, a risk assessment task exists in the TPRM module
- PII exposure events automatically create risk findings with correct severity
- Risk owners receive Slack notification for high-confidence AI tool discoveries
- Discovered Applications view shows live TPRM status for every entry

### Dependencies
- Operational Platform team: third-party entity model extension, risk assessment workflow API
- Notification system: template for shadow AI discovery notification

---

## Shadow IT Detection Improvements

> **Linear:** Project under SI team, Phase 1 (Q2 2026) — this is a **Q2 deliverable**
> **Why this matters:** Classification accuracy is table stakes. If the product reports false positives, customers lose trust. If it misses real shadow AI, it fails its core purpose. This is the foundation everything else builds on.
>
> **Sources:**
> - [Engineering Direction](https://www.notion.so/335671bead5c8049a824d8ed9a7a759a), Q2 deliverable: "Shadow IT detection improvement"
> - Lucas (#all-demos-and-feedback, Apr 4): "The algorithm for detecting PII and to define if something is shadow IT is a bit weak yet, but something we'll need to plan in more details later how to improve and collect signals that will make it more accurate"
> - Juni beta (CS-101) will produce the first real-world accuracy signal

### Problem

The current Noisy-OR scoring engine works but has known accuracy gaps. Lucas flagged that "the algorithm for detecting PII and to define if something is shadow IT is a bit weak yet." The signal weights are initial estimates, not data-driven. The provider catalog is static and manually maintained.

### Current State

9 signals, Noisy-OR combination:
- Domain layer: known provider catalog (0.90), hostname pattern (0.15)
- Network layer: login flow (0.55), OAuth/SSO (0.45), API endpoint (0.35), SSE streaming (0.40)
- Engagement layer: sustained session (0.20), active form input (0.25), deep interaction ratio (0.15)

70+ known providers across 6 categories.

### Requirements

**R1 — Data-driven weight calibration**
- Export a labeled dataset from internal dogfooding + Juni beta: (domain, signals fired, manual classification)
- Use logistic regression or gradient boosting to learn optimal signal weights
- A/B test new weights against current weights on internal traffic before rolling out

**R2 — Expand provider catalog**
- Grow from 70 to 200+ entries, prioritizing AI tools
- Sources: Product Hunt AI launches, AlternativeTo AI category, GitHub trending AI repos, Crunchbase AI companies
- Make catalog updatable via API (not hardcoded) — extension fetches latest catalog on startup

**R3 — New detection signals**
Candidates to add:
- **Response header analysis**: `X-Powered-By`, `Server` headers revealing framework/platform
- **Cookie domain analysis**: third-party cookies indicating identity federation
- **Service worker detection**: modern SaaS apps register service workers
- **Favicon/manifest analysis**: `manifest.json` presence and content (app name, icons)
- **Content Security Policy headers**: reveal allowed script sources and API domains

**R4 — Confidence calibration framework**
- Track classification accuracy over time (admin marks discovered apps as "correct" or "incorrect" in dashboard)
- Feedback loop: incorrect classifications inform weight adjustments
- Per-workspace calibration: allow workspaces to mark known internal tools as "ignore"

**R5 — Dynamic AI tool detection**
Beyond the static catalog, detect likely AI tools dynamically:
- SSE streaming (`text/event-stream`) is a strong AI inference signal (already in signals, weight 0.40)
- LLM-specific response patterns: streaming JSON chunks, token-by-token delivery
- Request patterns: large text payloads sent, streaming responses received
- Model API URL patterns: `/v1/chat/completions`, `/v1/embeddings`, `/generate`, `/predict`

### Success Criteria
- Classification accuracy (measured against manually labeled ground truth) improves from current baseline to 85%+
- False positive rate for "high confidence" classification drops below 5%
- New AI tools are detected within 1 week of gaining significant usage (without catalog update)

---

## Implementation Priority

| Feature | Phase | Effort | Impact | Priority |
|---|---|---|---|---|
| Shadow IT detection improvements | 1 | Medium | High — accuracy is table stakes | P0 |
| AI usage insights dashboard | 1 | Medium | High — customers need to see value | P0 |
| Juni beta feedback loop | 1 | Low | High — real customer signal | P0 |
| Risk signal integration | 2 | Medium | High — closes the SIGINT→TPRM loop | P1 |
| Policy enforcement engine | 2 | High | High — customers asking for it | P1 |
| Transitive third-party mapping | 2 | High | Very high — key differentiator | P1 |
| SDK/workstation monitoring | 3 | High | Medium — expands surface | P2 |
| SaaS-embedded agent detection | 3 | High | Medium — expands surface | P2 |
| Agentic behavior classification | 3 | Medium | Medium — future differentiator | P2 |
