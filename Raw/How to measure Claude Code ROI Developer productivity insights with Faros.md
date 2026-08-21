---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - claude-code
  - metrics
source: readwise
created: 2026-06-23
rating: 
action: 
theme: productivity-measurement
subtheme:
  - dora-delivery-metrics
  - cost-optimization
---

# How to measure Claude Code ROI: Developer productivity insights with Faros

![rw-book-cover](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69b44800a13bac082935e029_PB5-gpzXF93in1AaMY3060hDrhUQnlycjMMfpL7T07M.avif)

## Metadata
- Author: [[Thierry Donneau-Golencer]]
- Full Title: How to measure Claude Code ROI: Developer productivity insights with Faros
- Category: #articles
- Summary: Claude Code helps developers write code faster, but organizations often don't see overall delivery improve. Faros tracks how teams use Claude Code and links this data to real productivity and quality metrics. This helps companies measure true ROI and optimize AI tools for better software delivery.
- URL: https://www.faros.ai/blog/how-to-measure-claude-code-roi-developer-productivity-insights-with-faros-ai

## Full Document
![Illustration showing Claude Code measuring Usage, Impact, and ROI with three circular gauge meters on an orange gradient background.](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69b44800a13bac082935e029_PB5-gpzXF93in1AaMY3060hDrhUQnlycjMMfpL7T07M.avif)Illustration showing Claude Code measuring Usage, Impact, and ROI with three circular gauge meters on an orange gradient background.
#### AI coding assistants promise faster development. But do they deliver?

Engineers and developers using Claude Code report dramatic individual gains. [Some cite a 164% increase](https://raymond-brunell.medium.com/from-overwhelmed-to-overdelivering-how-claude-code-saved-my-solo-project-when-nothing-else-worked-bea613380936) in story completion. Others [nearly doubled their pull request merge rates](https://www.faros.ai/blog/ai-software-engineering). Yet organizations struggle to see these improvements materialize in overall delivery metrics.

This issue is that the lack of observability creates a measurement crisis. In the past 12 months, we’ve seen engineering leaders and teams invest heavily in AI tools without clear ROI evidence. With new assistants and models released every month, AI adoption is significantly on the rise. But CFOs question six-figure licensing costs that don't translate to faster shipping. Teams produce more code but not necessarily better outcomes.

Why is that? The problem isn't the tools. It's mostly the lack of visibility into how they actually affect productivity at scale. Meaning, asking a simple question like “What is the impact of AI on developer productivity?” Another way to put it is “ Is AI accelerating delivery and/or improving quality?”

This article shows how to measure **Claude Code's real impact using Faros**. You'll learn to track adoption patterns across teams, calculate cost per engineering output, and identify where AI helps versus where it creates new bottlenecks. We cover the frameworks that matter (DORA and SPACE metrics), the common measurement failures to avoid, and the optimization strategies that turn raw usage data into actionable intelligence.

The goal is to transform vague productivity claims into defensible business cases backed by evidence.

#### What is Claude Code and why developers are turning to it

Claude Code is an agentic coding assistant that operates through your terminal rather than providing inline autocomplete suggestions. The Claude Code CLI lives in your command line. It understands entire codebases and executes multi-step tasks autonomously through natural language instructions.

So, how does it understand your project? [Claude Code](https://labs.adaline.ai/p/claude-code-for-productivity-workflow) uses **agentic search** to analyze repositories without requiring manual context selection. It documents discoveries in a CLAUDE.md file.

| Memory Type | Location | Purpose | Use Case Examples | Shared With |
| --- | --- | --- | --- | --- |
| Enterprise policy |  macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md` Linux: `/etc/claude-code/CLAUDE.md` Windows: `C:\ProgramData\ClaudeCode\CLAUDE.md` | Organization-wide instructions managed by IT/DevOps | Company coding standards, security policies, compliance requirements | All users in organization |
| Project memory | `./CLAUDE.md` | Team-shared instructions for the project | Project architecture, coding standards, common workflows | Team members via source control |
| User memory | `~/.claude/CLAUDE.md` | Personal preferences for all projects | Code styling preferences, personal tooling shortcuts | Just you (all projects) |
| Project memory (local) | `./CLAUDE.local.md` | Personal project-specific preferences | (Deprecated, see below) Your sandbox URLs, preferred test data | Just you (current project) |

Various purposes of the CLAUDE.md file | Source: Anthropic, as captured by Adaline

The CLAUDE.md files allows Claude to create persistent memory across different sessions. Claude Sonnet 4 and Sonnet 4.5 provide a 200,000-token default context window, with support for an extended 1,000,000-token context window in enabled or beta long-context modes. This expanded context makes it feasible to reason over large portions of a codebase in a single pass. While these context sizes are among the largest generally available, several other AI models also offer million-token-scale context support.

![Models provided by Claude Code in pro tier. Claude Code allows you to switch between Sonnet, Haiku and Opus if you are in a Max tier. ](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69a0956a66cb78d1e2b58a33_695c3c2c402915fe85617530_select%2520image.webp)Models provided by Claude Code in pro tier. Claude Code allows you to switch between Sonnet, Haiku and Opus if you are in a Max tier.
Claude has established itself as one of the leading AI coding assistants, capturing approximately half the code generation market in the last six months. This success stems from its sophisticated understanding of code structure and context. Beyond simple code generation—which Claude excels at—engineers use Claude Code for tasks beyond simple code generation. Common applications include:

1. Managing stacked PRs with automated testing and submission.
2. Spawning Claude Code agents that work in parallel on different components.
3. Integrating with external tools via Model Context Protocol (MCP) to read design docs or update tickets.

Is Claude Code free? No.

At the time of writing this article the pricing starts at $20 monthly for the Pro tier. In the Pro tier you can log **10-40 prompts per 5-hour window**. Then you have $100-200 monthly for [Max plans](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan), where you can log 200-800 prompts per window. Team plans cost $30 per user monthly with a five-user minimum and the premium seat costs $150 per person with access to Claude Code.

Now, let’s compare Claude Code with Cursor. Essentially, [Cursor](https://vladimirsiedykh.com/blog/ai-coding-assistant-comparison-claude-code-github-copilot-cursor-feature-analysis-2025) provides an AI-enhanced IDE with inline suggestions. Claude Code operates as an autonomous terminal agent with larger context windows and scriptable workflows for CI/CD integration. You can actually run Claude Code inside Cursor’s terminal, a popular use case.

![Claude Code extension in VS Code](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69a0956a66cb78d1e2b58a27_695c3c87e3e96e8a1a7728f3_claudecodeforvscode.webp)Claude Code extension in VS Code
And if you are using VS Code you can install and enable Code Code extension.

With so many software development capabilities across multiple tools, a measurement problem arises. When developers use 200 prompts daily at $100 monthly per seat, leadership needs proof that this investment improves organizational delivery, and not just individual productivity. Because not all the prompts can produce valuable results.

Also, apart from coders or software engineers, creative professionals have started using Claude Code for creative writing, SEO research, content generation, digital marketing, and more. An ideal setup these days is Cursor or VS Code with Claude Code (in the terminal) along with Obsidian, where Obsidian is used as a data management system.

#### Tracking Claude Code usage and adoption with Faros

How do you measure developer productivity when AI tools enter the workflow? Before you can tie usage to impact, you need a clear understanding of the usage itself and the ability to track it over time. Traditional metrics like lines of code or commit counts don't reveal whether developers are actually adopting AI tools or how they're using them in their daily workflows.

**Before you can measure impact, you need visibility into usage itself.** Understanding who is using Claude Code, how often, and in what ways provides the foundation for later connecting that usage to productivity outcomes. Without this baseline visibility, you're flying blind when trying to assess whether your AI investment is working.

Faros provides the visibility needed to understand Claude Code adoption patterns across your organization. The platform [integrates data](https://www.faros.ai/copilot-module) from over 100 development tools including GitHub, Jira, CircleCI, and PagerDuty, creating a unified view of how developers interact with AI coding assistants.

For Claude Code specifically, Faros tracks usage and adoption across three key dimensions:

1. **Dimension 1: Granular usage and adoption metrics.** You can monitor active sessions to understand who's using the tool and how frequently. Team-level usage data reveals adoption patterns across your organization.
2. **Dimension 2: Code trust and acceptance.** Suggestion acceptance rates indicate whether developers trust the generated code enough to commit it.
3. **Dimension 3: Team-level performance visibility.** This sort of visibility answers critical questions like "Which teams have frequently used or adopted Claude Code and which haven't?" Faros dashboards segment teams by adoption rate, making high and low performers immediately visible.

![Chart showing usage distribution across teams to identify patterns for cost savings opportunities.](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69a0956a66cb78d1e2b58a2c_695c3ce57a6e81fdd2ec8c5c_claudecodeactiveusers.webp)Chart showing usage distribution across teams to identify patterns for cost savings opportunities.
**Teams with declining or consistently low acceptance rates signal a need for targeted enablement efforts.** The platform helps you identify these struggling teams early so you can intervene with training or support.

Power users emerge in the data. Faros classifies users based on frequency and consistency of usage over time. Power users demonstrate at least 20 usage days per month or activity across 50 different hours monthly. These developers achieve measurably higher output and become potential champions for broader adoption.

Faros enables cohort tracking for how to measure developer productivity improvements. For instance, it:

1. Split similar teams into control and treatment groups.
2. Track one team using Claude Code against a baseline team without it.
3. Measure engineering efficiency through pull request velocity, review time, and cycle time across both cohorts.

Let's understand this with a practical example. Consider an engineering director. She sees Team A at 5% Claude Code adoption versus Team B at 60%. Faros data shows Team B merges 47% more pull requests daily but has 35% longer review times.

**What does this reveal?** Team B is writing code faster with Claude Code, but the increased volume is creating a new bottleneck in code review. The team that appeared more productive based on code generation alone is actually slowing down overall delivery because reviewers can't keep pace. This is why measuring the entire workflow matters, not just coding speed.

#### Claude Code pricing meets transparency

Claude Code pricing operates on a token-based model with tiered limits. Something we discussed previously. But what does this actually cost your organization?

Most engineering leads can't answer that question. They know the license fees but not the cost of **AI-generated code** per unit of output.

Faros answers this question by measuring token usage to specific engineering outputs. The solution tracks Claude Code token consumption by model type and correlates it with commits and pull requests. This creates visibility into the true cost per commit and cost per PR across your teams.

![Chart showing average cost per commit.](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69a0956a66cb78d1e2b58a24_695c3d461fee4950317f5955_claudecodecostpercommit.webp)Chart showing average cost per commit.
Here's a practical example. A team of 50 developers on Max plans costs $120,000 annually. Faros tracks 8,400 pull requests merged versus a baseline of 5,200. The cost per incremental PR is $37.50. If each PR saves two hours of developer time at $75 per hour, the value is $150. Your ROI is 4:1.

Note: This is a back-of-the-envelope calculation; real-world results vary significantly as PR value differs enormously across different changes.

Is Claude Code worth it? **The answer depends on utilization**. Faros identifies underused licenses where developers generate fewer than 20 PRs monthly despite Max plan access. The platform flags overspend where high token costs produce minimal output improvements or declining code quality.

![Dashboard showing Claude Code acceptance rates, commits, and PRs.](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/69a0956a66cb78d1e2b58a30_695c3ebb15a337629ef1be6d_claudecodevarietycharts.webp)Dashboard showing Claude Code acceptance rates, commits, and PRs.
Engineering efficiency metrics become actionable through this visibility. **Leaders can downgrade inactive users from Max to Pro plans**. They can reallocate licenses to high-value use cases like technical debt reduction or legacy modernization. They can calculate break-even points for different team sizes and usage patterns.

This is how you audit real ROI from Claude usage. Connect dollars spent to business outcomes delivered.

#### Developer productivity and software metrics

When measuring software productivity a lot of areas need to be considered. For instance, velocity metrics alone miss critical quality and stability signals that determine organizational delivery capacity.

Faros tracks velocity through pull requests merged, review time, and sprint completion rates. The platform monitors how Claude Code affects these software metrics in real time. Developers using AI coding assistants show 98% higher PR throughput, but does this translate to faster delivery?

The answer requires examining what happens to these PRs and how fast they can be deployed. Code quality plays an outsized role in this. Faros measures test coverage percentage; bugs per developer, team, and application; and PR size distribution. Research shows AI-generated code tends to be larger and contains more defects. This concludes that we are still far away from fully trusting AI. This inherently creates downstream bottlenecks in code review and quality assurance processes.

To mitigate this issue we can consider DORA. [DORA](https://dora.dev/guides/dora-metrics-four-keys/) metrics provide the framework for understanding organizational impact. The four key measurements are:

1. Deployment frequency
2. Lead time for changes
3. Change failure rate
4. Mean time to restore

Elite performers deploy on demand with lead times under one hour and change failure rates below 15%.

But how does Claude Code affect these DORA metrics? The evidence from Faros research shows mixed results. Despite individual developers completing [21% more tasks and merging 98% more pull requests](https://www.faros.ai/blog/ai-software-engineering), organizational DORA metrics remain largely unchanged. The productivity gains at the individual level don't translate to improvements in deployment frequency, lead time, change failure rate, or mean time to restore.

This is the AI Productivity Paradox. Individual output increases dramatically, but organizational delivery velocity stays flat. This is because, now, the bottleneck is shifting from code generation to code review and validation. Teams merge more PRs, but review times increase by 91%, creating new constraints downstream. The result is more code in the pipeline without faster delivery to production.

In order to resolve such issues, teams must invest in better testing infrastructure and review processes to capture productivity gains. The goal isn't just to write more code faster. It is to ensure that the increased individual output translates to faster organizational delivery without sacrificing quality.

#### Optimizing Claude Code adoption with Faros

Measurement enables optimization. Faros transforms Claude Code adoption from experimentation into systematic improvement of engineering productivity.

Start by [identifying](https://www.faros.ai/copilot-module) lagging teams in your Faros dashboards.

* **Teams with low weekly active user rates need targeted enablement efforts.** Use Faros to identify teams where fewer developers are actively engaging with Claude Code on a weekly basis. Survey these teams to understand barriers: cost concerns, use case confusion, or tool friction. Pair them with high-adoption champions for knowledge transfer. Track weekly adoption metrics to measure progress.
* A/B testing provides rigorous proof of impact. Split similar teams with one group using Claude Code and one control group. Match teams on **project complexity**, **tech stack,** and **developer seniority** for valid comparisons. Run tests for at least one quarter with minimum control groups of 20 to 30 developers.
* **Before-and-after performance comparisons require baseline data**. Capture deployment frequency, lead time, PR volume, and code quality metrics before Claude Code rollout. Plan measurement checkpoints at regular intervals over at least one quarter. This will enable tracking how adoption patterns and productivity impacts evolve as developers become more familiar with the tool.

How can team leads use Faros reports effectively?

Review adoption patterns weekly to spot disengagement early. Compare individual token costs against output metrics to identify negative ROI users. Monitor change failure rates to catch quality degradation before it compounds. Use dashboard data in one-on-one coaching to demonstrate impact and refine usage patterns.

Developer productivity measurement tools like Faros enable responsible AI investment decisions. You can reallocate licenses from low-value to high-value use cases. You can justify budget increases with concrete ROI data. You can increase developer productivity systematically rather than hoping adoption equals improvement.

Observability is critical for responsible AI tooling at scale. Without measurement, you're flying blind with six-figure investments and unclear returns.

#### Transform vague productivity claims into defensible, evidence-backed business cases with Faros

Claude Code delivers real productivity gains at the individual developer level. The organizational impact remains unclear without proper measurement infrastructure in place.

Faros solves this visibility problem by connecting Claude Code usage to business outcomes. The platform tracks adoption patterns, calculates cost per engineering output, and reveals where AI accelerates delivery versus where it creates new bottlenecks. Teams can prove ROI with data rather than relying on developer sentiment alone.

The evidence shows mixed results across organizational KPIs. Coding time decreases while review time increases. Pull request volume jumps but bugs per developer increase. These trade-offs require active management through quality gates and scaled review capacity.

Start with baseline measurements before rolling out Claude Code to additional teams. Run controlled experiments for at least one quarter. Track both velocity and quality metrics simultaneously. Use Faros to identify optimization opportunities and reallocate licenses to high-value use cases.

Responsible AI tool investment requires observability. Measure to optimize. Optimize to prove value. Prove value to scale confidently. [Reach out for a demo](https://www.faros.ai/blog/how-to-measure-claude-code-roi-developer-productivity-insights-with-faros-ai#contact) to learn more.

![Thierry Donneau-Golencer](https://cdn.prod.website-files.com/695be6d603b11be779b0b9b2/695be6d603b11be779b0bec9_fb8b7e718369d6124b95f934149ab7cc7c46e129-284x284.avif)Thierry Donneau-Golencer
