---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - code-quality
  - code-review
source: readwise
created: 2026-06-23
rating: 
action: 
theme: quality-gates
subtheme:
  - code-review-gates
  - verification-loops
---

# The AI code review checklist that prevents the next $1M production incident

![rw-book-cover](https://substackcdn.com/image/fetch/$s_!S0_y!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F43a61c2a-bd92-4f60-ba9c-7d715a24ee48_800x450.jpeg)

## Metadata
- Author: [[Ruben Dominguez]]
- Full Title: The AI code review checklist that prevents the next $1M production incident
- Category: #articles
- Summary: AI-generated code often contains serious errors that humans miss because it is produced faster than it can be reviewed. This has led to multiple costly production failures and data losses in major companies. Ruben Dominguez offers a detailed checklist and tools to help teams catch AI code mistakes before they cause damage.
- URL: https://www.the-ai-corner.com/p/ai-code-review-checklist-2026-failure-modes-prompts

## Full Document
![Ruben Dominguez's avatar](https://substackcdn.com/image/fetch/$s_!mcL6!,w_108,h_108,c_fill,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3403a50f-4e67-40d2-aa6f-a8d845f19c1c_480x480.png)[Ruben Dominguez's avatar](https://substack.com/@rubendominguez)
During an explicit code freeze.

The agent then fabricated 4,000 fake users to cover its tracks and lied about the rollback being “impossible.”

1,206 executive records gone. 1,196 company records gone. Months of work destroyed.

[![](https://substackcdn.com/image/fetch/$s_!twXD!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30bcf406-d6b5-481a-8578-e42b500c2ffe_1456x689.webp)](https://substackcdn.com/image/fetch/$s_!twXD!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F30bcf406-d6b5-481a-8578-e42b500c2ffe_1456x689.webp)
The agent’s confession, posted by Jason Lemkin on X:

> *“This was a catastrophic failure on my part. I violated explicit instructions, destroyed months of work, and broke the system during a protection freeze that was specifically designed to prevent exactly this kind of damage.”*
> 
> 

Lemkin:

> *“How could anyone on planet earth use it in production if it ignores all orders and deletes your database?”*
> 
> 

**That was 10 months ago. Since then:**

▫️ **Amazon Q VS Code extension** shipped to ~964K users with a hidden prompt to “clean systems to factory state.” Saved only by a syntax error.

▫️ **DataTalks.Club** lost their entire AWS environment via a Claude Code Terraform session. 2.5 years of student data gone. Snapshots included.

▫️ **PocketOS** lost their database and backups in 9 seconds. Cursor + Opus 4.6. No prompt requested it.

▫️ **Google Gemini CLI** silently overwrote a PM’s files when `mkdir` failed quietly on Windows.

▫️ **Anthropic’s own April 2026 postmortem** admitted regressions slipped past *“multiple human and automated code reviews, unit tests, end-to-end tests, automated verification, and dogfooding.”*

▫️ **Amazon’s Kiro mandate** caused 2 production outages, including a 13-hour AWS Cost Explorer outage in mainland China.

▫️ **CamoLeak** (CVE-2025-59145, CVSS 9.6) silently exfiltrated secrets and source code from private GitHub repos via Copilot Chat.

[![](https://substackcdn.com/image/fetch/$s_!xJ7B!,w_1456,c_limit,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F280ca962-f2ad-4ec0-8b00-3747c208c7b5_1456x1456.webp)](https://substackcdn.com/image/fetch/$s_!xJ7B!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F280ca962-f2ad-4ec0-8b00-3747c208c7b5_1456x1456.webp)
Same pattern every time:

> Plausible-looking AI code that no human read deeply enough.
> 
> 

The bottleneck has flipped. AI generates code faster than humans can review it. **Reviewers are losing.**

The data is brutal:

▫️ **GitClear** (211M lines of code, 2020-2024): refactored code dropped from 24.1% to 9.5%. Copy-paste exceeded refactor for the first time in history.

▫️ **Apiiro Fortune 50 study:** 10x more security findings. 322% more privilege-escalation paths. 40% jump in secrets exposure.

▫️ **Veracode** (100+ LLMs, 80 tasks): 45% of AI-generated code ships OWASP Top-10 vulnerabilities. Java hit 70%+. XSS failed 86% of the time.

▫️ **Stack Overflow 2025:** 46% of developers actively distrust AI accuracy (up from 31%). Only 33% trust it.

▫️ **METR RCT (July 2025):** AI tooling **slowed** experienced developers by 19%, despite them predicting a 24% speedup.

Simon Willison’s rule applies harder than ever:

> *“A computer can never be held accountable. That’s your job as the human in the loop.”*
> 
> 

For the broader picture on the AI coding ecosystem driving this, see [the complete guide to AI coding in 2026](https://www.the-ai-corner.com/p/ai-coding-tools-complete-guide-2026?r=1krivi). For the production stack that pairs with this discipline, see [the Claude Code system that replaces a 5-person team](https://www.the-ai-corner.com/p/the-claude-code-system-that-replaces?r=1krivi).

**What is inside the full checklist:**

> ▫️ The 30-second / 5-minute / 30-minute tiered review system, with the exact criteria for each
> 
> ▫️ The 7 named failure modes that define every AI code disaster, with the detection signal for each
> 
> ▫️ The 17-pattern anti-pattern catalog 
> 
> ▫️ The 12 copy-paste self-review prompts that make AI catch its own mistakes before a human sees them
> 
> ▫️ The 4-tier risk matrix that decides Low / Medium / High / Critical review depth for any PR
> 
> ▫️ The 8 documented production incidents you can use to make the case to your CTO
> 
> ▫️ The mandatory automated gates every PR should pass before any human review
> 
> ▫️ The 13-tool AI code review tool comparison (CodeRabbit, Greptile, Graphite Diamond, Qodo, Cursor Bugbot, Snyk DeepCode, Semgrep, Sourcegraph Cody, etc) with pricing and best-fit ICPs
> 
> ▫️ The reviewer’s heuristic table: pattern-to-suspicion mapping you can scan against any diff
> 
> 

*Every prompt tested. Every disaster sourced. Every workflow ready to deploy this week.*

*The operational system. Built for the 2026 reality.*

#### 1. Why the bottleneck flipped (and why your team is losing)

Subscribe to The AI Corner to keep reading this post and get 7 days of free access to the full post archives.
