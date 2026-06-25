---
categories:
  - "[[Projects]]"
project: "[[Ethira]]"
created: 2026-06-23
---

# AI / Agentic Evaluation

## Scoring Method for Agentic AI Answers
Evaluated multiple scoring approaches (MCDA, ELO, Rubric, Binary, LLM-as-Judge, Trajectory-based).

**Recommendation: Hierarchical Gated MCDA**
- **Level 1 - Hard Gates:** Safety violations, hallucinated tool calls, invalid format → instant fail
- **Level 2 - Weighted MCDA:** Correctness (0.30), Tool Use (0.20), Efficiency (0.15), Robustness (0.15), Helpfulness (0.10), Code Quality (0.10)
- **Level 3 - Trajectory Bonus:** +0.05 for error recovery, +0.05 for proactive verification, -0.10 for unnecessary tool calls

**Key insight:** Pure MCDA is compensatory — a catastrophic safety failure gets masked by high scores elsewhere. Gating fixes this. Periodic ELO pairwise comparisons should validate that MCDA scores correlate with human preference.

Full analysis: [[Claude memory — agentic-ai-scoring]]

---

# Trust Exchange

## Minor bugs 
When inserting slug and company name and then upload logo it remove the slug and company name. 
![[Pasted image 20260326114110.png]]

# General
## Notification Service 

## Proper pattern
https://chatgpt.com/share/69c062c5-bb7c-8011-aa4f-d314ef844768
 `~/Ethira/monorepo/api/src/application/services/trust-exchange/revoke-trust-exchange-access-request.service.ts`
No proper formatting and not using notifcation service
Also no signature

```javascript
    await this.mailjetService.sendEmail({
      to: data.email,
      subject: 'Access request revoked',
      text: `
        Dear ${data.requesterName},
        
        We are writing to inform you that your access to the Trust Center has been revoked.
        
        As a result, you will no longer be able to access the Trust Portal or its resources. This action may have been taken due to security policies, organizational changes, or other administrative decisions.
        
        If you believe this action was taken in error, or if you have any questions regarding this decision, please feel free to contact us to discuss your case further.
        
        Contact Support: hello@ethira.dev
        
        Thank you for your understanding.
      `,
    });
  }
}
```

---

# Design System

## Email Template — Rebuild with New Design System

When the new design system is finalized, regenerate the email templates using the updated tokens. Reference template: [[email-template-preview.html]]

**Generation instructions:**
- **Layout:** 600px max-width wrapper, white card on `#F1F0EB` background, 12px border-radius, subtle box-shadow
- **Header:** Dark (`#10201F`) background, logo SVG (concentric circles in accent color) + wordmark, right-aligned uppercase badge pill with accent background at 15% opacity
- **Hero section:** Serif heading (DM Serif Display, 28px), sans-serif subtitle (DM Sans, 15px, `#494541`), bottom border separator
- **Status card:** `#F7F7F2` background, 10px border-radius, 3px left border in accent color, dot + uppercase label header, 2-column grid for key-value pairs (11px uppercase labels in `#B4AAA1`, 14px 500-weight values)
- **Body:** 15px/1.65 prose in `#494541`, 40px horizontal padding
- **CTA:** Centered dark button (`#10201F`, 14px 600-weight, 14px 32px padding, 8px radius), accent-colored arrow, secondary link below in `#B4AAA1`
- **Lifecycle bar:** `#F7F7F2` strip with uppercase 11px steps connected by 24px lines, active step gets accent background pill
- **Footer:** Centered muted logo, 12px link row in `#B4AAA1`, 11px tagline in `#DED8D8`
- **Typography:** DM Serif Display for headings, DM Sans for everything else
- **Color palette:** Dark `#10201F`, accent green `#A9FBC0`, deep green `#016853`, warm gray `#494541`, muted `#B4AAA1`, bone `#F1F0EB` / `#F7F7F2`, light border `#DED8D8`
- **Spacing:** 40px horizontal padding throughout, 32px vertical sections, 24px card padding
- **Always send both `text` and `html`**, use `escapeHtml()` for user data, include email signature from `email-signature.ts`

When the design system ships, swap hardcoded hex values for design tokens and update the logo SVG to the final version.

---

# CI/CD

## GitHub Action: Smart PR Slack Notifications
The official GitHub Slack app (`/github subscribe`) has very limited filtering -- no way to exclude draft PRs, filter by author, check CI status, or use negative label filters.

**Goal:** Create a GitHub Actions workflow (`.github/workflows/slack-pr-notify.yml`) that posts to Slack only for PRs matching specific criteria, replicating this GitHub search query:
```
is:open is:pr draft:false review:required -author:marcelo-ethira -label:":no_entry_sign: testing-failed" status:success
```

**Implementation:**
- Trigger on `pull_request` events: `opened`, `synchronize`, `ready_for_review`, `review_requested`
- Conditions: `draft == false`, exclude specific authors, exclude specific labels, require passing CI status
- Post to Slack via incoming webhook (`SLACK_PR_WEBHOOK_URL` GitHub secret)
- Use `slackapi/slack-github-action@v2` for the Slack message

**Setup required:**
1. Create a Slack Incoming Webhook for the target channel
2. Add it as a GitHub Actions secret (`SLACK_PR_WEBHOOK_URL`)
3. Decide which channel and which authors/labels to exclude

**Reference:** [GitHub Community Discussion #178699](https://github.com/orgs/community/discussions/178699) -- feature request for advanced filtering in the official app.
