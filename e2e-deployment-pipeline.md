---
categories:
  - "[[Projects]]"
created: 2026-05-01
project: Ethira
tags: [engineering, e2e, ci-cd, devops, architecture, dora]
status: in-progress
---

# E2E + Deployment Pipeline — Strategy & Roadmap

Plan for end-to-end testing infrastructure and the broader deployment pipeline, calibrated to Ethira's current size (~5-10 devs, GRC SaaS, AWS-backed).

Lots of decisions locked in this plan came from a grilling session on what counts as a "core flow", how to structure tests, how to balance velocity with safety, and where industry best practice 2026 has moved relative to older guidance.

---

## Core principles (locked)

### Definition of "core flow"
**Reliability-tied (signals from real customer pain) + revenue-tied (paid feature) override.**

Selection rubric:
- Customer-blocking URGENT Linear ticket: +5
- Rollback / hotfix triggered: +5
- Each additional unique customer hit: +2
- Standard CS ticket (High/Medium): +3
- Sentry error rate breach: +3
- Bull queue failure spike: +2
- Mention in `#feed-customer-support` digest: +1
- **Revenue override**: contracted/paid feature → mandatory regardless of score

**Threshold: ≥6 → mandatory E2E.** Below = integration test.

**Module cap: 3 E2E max per module** (sidebar nav grouping). New flow displaces lowest-scored existing test.

### Test design rules
- One longer happy-path E2E per spec, inline `expect()` per `test.step()`. Split only when business outcomes diverge fundamentally (happy vs reject).
- 60s hard timeout per test. No `test.setTimeout()` overrides.
- Mock LLM at boundary (cross-process). Real LLM in eval suite only.
- 5 consecutive green runs before merging new test.
- Quarantine threshold: 3 fails / 20 runs → moved to `e2e/quarantine/`, deleted if not fixed in 2 weeks.
- Every test needs JSDoc motivation block (signal sources cited, score breakdown, module slot, alternatives rejected).
- Mandatory critique gate (`e2e-critique-reviewer` agent) before write + before commit. Default REJECT. Override only via explicit `OVERRIDE: <reason>` keyword recorded as JSDoc.

### Banner pattern
Every test must have:
- `showTestIntro(page, title, description)` at start — full-screen card describing what will be tested
- `showStep(page, ...)` at start of every `test.step()` — persistent header (survives `page.goto()` via `addInitScript`)
- `showTestOutro(page, title, [verifiedItems])` at end — full-screen summary

### Test isolation
Ephemeral workspace per test (fresh DB-direct created workspace, deleted after) for any test depending on workspace-derived state (onboarding completion, settings). Default `authedPage` fixture only OK for tests creating fresh entities.

---

## Current architecture (built in 2026-04-30 → 2026-05-01)

### Local stack (`make docker-up-detached`)
- `postgres` — 15-alpine
- `redis` + `redis-cache` — 7-alpine
- `bullboard` — Bull queue UI
- `minio` + `minio-init` — S3-compatible blob store, auto-creates `ethira-dev` bucket
- `llm-mock` — custom Express server replacing OpenAI/Requesty
- `api`, `app`, `admin` — NestJS API, React app, Admin React app

### Storage abstraction
- Single `S3StorageService` for all environments
- `S3_ENDPOINT=http://minio:9000` in dev, unset in staging/prod
- `S3_PUBLIC_ENDPOINT=http://localhost:9000` for browser-reachable presigned URLs (host swap via `toPublicUrl()`)
- `S3_FORCE_PATH_STYLE=true` only in dev
- Code path identical across envs — only env vars differ

### LLM abstraction
- `OPENAI_BASE_URL=http://llm-mock:3030/v1` in dev/CI
- Mock returns shape-valid OpenAI responses
- JSON mode detection (json_schema, json_object) returns synthesized JSON from schema
- Catch-all returns 200 stub for unhandled endpoints
- Real OpenAI/Requesty in staging/prod

### Test suite (post-migration)
8 specs, modular cap respected:

| Spec | Module slot | Status |
|---|---|---|
| risk-assessment | Risks 1/3 | ✅ passing |
| signup happy path | Auth 1/3 | ⏭️ skipped (needs `EMAIL_VERIFICATION_BYPASS_CODE` env) |
| relationship-onboarding | Supply Chain 1/3 | ✅ passing |
| pre-screening-lifecycle | Supply Chain 2/3 | ✅ passing |
| vendor-onboarding | Supply Chain 3/3 | ❌ rewrite pending |
| questionnaire-lifecycle (×2: happy + reject) | Trust Exchange 1/3 | ❌ workflow-dep on onboarding |
| trust-exchange-onboarding | Trust Exchange 2/3 | ❌ frontend upload-session bug |
| trust-exchange-external-questionnaires | Trust Exchange 3/3 | ✅ passing |

Final: 4 passing / 3 failing / 1 skipped. Failures are workflow dependencies + frontend bugs, not infra.

### CI workflows built
- `.github/workflows/e2e-tests.yml` — PR gate, change-detection driven, runs only affected specs
- `.github/workflows/e2e-nightly.yml` — full suite at 03:00 UTC daily

---

## Deployment pipeline strategy (the bigger picture)

### The four-layer defense (2026 industry best practice)

```
PR opens
  ↓
[1. PR-CI on localhost]   ← built (MinIO + llmock + ephemeral workspace)
  ↓
[2. PR preview env]       ← future: real infra per PR, gates merge
  ↓ merge
[3. Staging continuously deployed from main]
  ↓
[4. Production canary with progressive rollout + auto-rollback]
[5. Feature flags decouple deploy from release]
[6. Observability auto-flips flags / rolls back on metric breach]
```

Each layer catches different failure classes. Earlier layers are cheaper; later layers cover what earlier ones miss.

### Why each layer exists

| Layer | Catches | Misses |
|---|---|---|
| PR-CI (mocks) | code regressions, selectors, race conditions, fixture bugs | IAM/CORS/secrets/real-LLM behavior |
| PR preview env | infra/IAM/CORS bugs **before merge** | rare edge cases not in test suite |
| Staging E2E pre-cutover | deploy-config drift, env-specific bugs | ALB/DNS/cert problems |
| Staging E2E post-cutover | ALB routing, DNS, TLS | prod-only scale issues |
| Production canary | runtime regressions, latency, error rates | already-shipped logic bugs |
| Feature flags | bad feature stays dormant | requires discipline (flag debt) |
| Observability + auto-rollback | last line of defense | reactive only |

### Staging hostname strategy (blue/green aware)

Three hostnames in staging:
- `staging.ethira.dev` → ALB → currently-active color
- `app.blue.staging.ethira.dev` → always blue
- `app.green.staging.ethira.dev` → always green

E2E pipeline must:
1. Pre-cutover: hit color-specific URL (blue or green, whichever just deployed)
2. Cut over ALB after E2E green
3. Post-cutover: hit public URL to verify ALB+DNS+cert

Same E2E spec runs both times. `BASE_URL` is the only diff. Pass via workflow input, never hardcode.

### Where CI E2E runs

- **PR CI**: localhost in GitHub Actions runner (docker-compose stack). Mocks everything.
- **Staging E2E**: against deployed staging URL (real S3, real OpenAI, real DB). No docker stack in CI runner.
- **Prod E2E** (eventually): against deployed prod URL. Smoke subset only, schema-tolerant assertions.

Same Playwright specs, different `BASE_URL` per project config.

### Modern best practice (2026)

Per DORA Elite tier:
- Multiple deploys/hour
- MTTR <7 minutes
- Change failure rate <15%
- Lead time <1 day

Achievable only with:
- Automated gates (no manual approvals on hot path)
- Per-PR preview env (catches infra bugs **before** main breaks)
- Feature flags (decouple risky deploys from release)
- Canary with auto-rollback (detect issues at 1% before reaching 100%)
- Observability driving automation

Industry has shifted from "trunk-based + auto-revert as primary" to "preview env + flags + canary as primary, auto-revert as backstop".

---

## Roadmap for Ethira

Calibrated to current scale (small team, ~5-10 deploys/week). Don't over-invest in elite-tier infra before the pain justifies it.

### Phase 1 (✅ done)
- PR-CI on localhost with MinIO + llmock + ephemeral workspace
- Nightly full-suite run
- 8 core E2E specs scoped, ranked, motivated
- Quarantine + monthly score audit rules

### Phase 2 — Staging post-deploy E2E (next 30 days)
- Smoke E2E (3-5 specs) runs after each main deploy
- Pre-cutover (color URL) + post-cutover (public URL) split
- Auto-revert on failure as backstop
- Catches infra/IAM/CORS bugs that PR-CI cannot
- Cost: ~1 day to wire up

**Build this BEFORE preview envs.** Highest ROI for time investment.

### Phase 3 — Feature flags adoption
- Adopt **GrowthBook** (open source, self-hostable) — ~$0/month
- Wrap any new "risky" change going forward (new payment flow, new AI prompt, schema migration)
- Don't retrofit existing code — just don't add new without flags
- Discipline: flag debt sweep every quarter

### Phase 4 — Production canary deploy
- Blue/green at infra level (already exists from earlier session work)
- Add traffic ramp: 1% → 5% → 25% → 100%
- Auto-rollback on Sentry error spike, p99 latency breach, or business KPI drop
- Tools: Argo Rollouts (Kubernetes) or AWS-native (CodeDeploy + ALB weighted target groups)

### Phase 5 — Per-PR preview environments
- Defer until: team grows past ~10 devs OR multiple PRs/week conflict on staging
- Tooling: Northflank or Railway (full-stack incl. database — Vercel/Netlify don't isolate DB)
- Cost: ~$50-200/month at PR volume of 50-100/month
- Replaces "merge-and-pray" with "tested-real-infra-before-merge"

### Phase 6 — DORA tracking + error budgets
- Track deploy frequency, lead time, change failure rate, MTTR, rework rate
- SLOs per critical flow (DORA ROI export 99.9%, questionnaire upload 99.5%, etc.)
- Burn rate alerts (Sentry / DataDog)
- Error budget gates: freeze deploys when SLO burn high

---

## Open backlog items

1. **Frontend upload-session POST** not reaching API in trust-exchange-onboarding spec (frontend bug, separate from infra)
2. **`completeTrustExchangeOnboardingViaAPI()`** helper for ephemeral workspace + use in questionnaire-lifecycle setup (workflow dep)
3. **Vendor-onboarding spec rewrite** as proper happy path
4. **Staging E2E workflow** + per-project timeout config in playwright.config.ts
5. **`e2e-score-audit.ts` cron script** for monthly maintenance
6. **Schema-tolerant assertions** for tests that need to pass against real LLM in staging
7. **MinIO image digest pin** (currently using tag — security-reviewer recommended digest)
8. **Adopt GrowthBook** for feature flags

---

## Decision log

Decisions made during this session, with reasoning:

| Decision | Rationale |
|---|---|
| Reliability-tied + revenue-override scoring | Maps directly to existing signals (Slack `#ext-*`, Linear CS tickets, Sentry); prevents over-weighting low-traffic surfaces |
| 3 per module cap | Forces ruthless prioritization; each module owner manages their slice |
| 60s hard timeout, no override | Forces mocked AI + tight tests; tests >60s = doing too much |
| Mock LLM in E2E (not real) | DORA Elite teams do this (Anthropic/Vercel/Notion); deterministic, fast, cheap; eval pyramid covers AI quality |
| Ephemeral workspace per test | Eliminates state leak between tests; matches multi-tenant SaaS production model |
| MinIO over LocalStorageService | Single code path dev/prod; MinIO speaks S3 SigV4 exactly; deletes 150 LOC dead code; agents unanimously chose this (4/4) |
| Per-test critique gate (`e2e-critique-reviewer`) | Adversarial reviewer prevents low-value tests; default REJECT; override via explicit keyword |
| Auto-revert as backstop, not primary | At Ethira's scale, preview envs are over-investment; staging-E2E + auto-revert covers 95% of cases |
| Defer per-PR preview env to Phase 5 | Cost (~$200/mo + maintenance) > current pain; revisit when team or PR volume grows |

---

## Reference links

### Internal
- `/Users/mindator/Ethira/monorepo/e2e-test-functionality/e2e/CLAUDE.md` — full E2E rules
- `/Users/mindator/Ethira/monorepo/e2e-test-functionality/.agents/agents/e2e-runner.md` — runner agent rules
- `/Users/mindator/Ethira/monorepo/e2e-test-functionality/.agents/agents/e2e-critique-reviewer.md` — adversarial reviewer
- `/Users/mindator/Ethira/monorepo/e2e-test-functionality/e2e/flows.yaml` — flow definitions

### External
- [Trunk-based Development](https://trunkbaseddevelopment.com/)
- [DORA Metrics 2026](https://dora.dev/guides/dora-metrics/)
- [Preview Environments 2026 Guide (Autonoma)](https://www.getautonoma.com/blog/preview-environments)
- [Northflank — preview environment platforms](https://northflank.com/blog/preview-environment-platforms)
- [Anthropic — Demystifying evals for AI agents](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents)
- [Canary release vs progressive delivery — Unleash](https://www.getunleash.io/blog/canary-release-vs-progressive-delivery)
- [llmock — Cross-process LLM mock server](https://github.com/CopilotKit/llmock)
- [Mavik Labs — AI End-to-End Testing 2026](https://www.maviklabs.com/blog/ai-end-to-end-testing-2026/)
- [Kent C. Dodds — How to know what to test](https://kentcdodds.com/blog/how-to-know-what-to-test)
- [Shiplight — SaaS E2E testing 2026](https://www.shiplight.ai/blog/saas-e2e-testing)
