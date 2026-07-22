---
created: 2026-07-13
categories:
  - "[[Resources]]"
domain: engineering
tags:
  - agentic-engineering
  - browser-automation
  - token-efficiency
  - mcp
---

# Gstack Browser vs Chrome DevTools and CDP

Gstack does not have more fundamental browser power than CDP. **Raw CDP is the lower-level superset.** Gstack adds workflow, conventions, and compact wrappers around it.

| Area | Gstack browser | Chrome DevTools/CDP |
|---|---|---|
| Browser capability | High-level subset | Full browser protocol |
| Setup | Separate CLI and browser daemon | Already available in your setup |
| Instructions | Opinionated QA recipes and guardrails | Mostly primitives; agent designs the workflow |
| Output | Compact snapshots, element references, diffs | Can produce large low-level JSON |
| Screenshots | Built-in responsive batches and annotations | Fully supported, but requires explicit commands |
| Authentication | Separate browser; cookies may need importing | Existing browser session can already be authenticated |
| Deep debugging | Basic console/network inspection | Better for traces, performance, protocol-level debugging |
| Repeatability | Strong standardized commands | Depends on the automation written around CDP |

## Token usage

It depends on the task:

- Gstack's skill instructions are large, so loading the complete `/browse` workflow costs extra context.
- After loading, commands such as `snapshot -i`, `responsive`, and `snapshot -D` can be token-efficient because they return compact, purpose-built output.
- Raw CDP responses can be extremely verbose, especially DOM trees, network events, and performance traces.
- A good Chrome DevTools MCP wrapper can already filter those responses, removing much of gstack's token advantage.
- For one page and three screenshots, an existing DevTools/CDP setup is likely cheaper.
- For repeated multi-page QA, gstack's compact snapshots and standardized workflow may save tokens overall.

## What “more instructions” means

Gstack includes an opinionated playbook:

- Inspect accessibility before clicking.
- Use stable element references.
- Check console and network failures.
- Capture mobile, tablet, and desktop layouts.
- Compare before and after states.
- Return screenshot evidence.
- Preserve a persistent browser session.

CDP only supplies the mechanics. It does not tell the agent what a good QA process looks like.

## Recommendation

Use **Chrome DevTools/CDP as the default** when it is already configured because:

- It can verify prototypes and capture screenshots.
- It avoids another local daemon and build.
- It can attach to an existing authenticated browser.
- It provides deeper debugging when needed.

Use gstack when its higher-level workflow is specifically useful, such as a repeatable `/qa` pass, responsive screenshot matrix, or structured before-and-after report.

For a small static prototype, gstack adds little value. Chrome DevTools/CDP is the better choice.

## Related

- [[Agent-Driven Browser Verification]]
- [[Agentic Engineering]]
- [gstack repository](https://github.com/garrytan/gstack)
