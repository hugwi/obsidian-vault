---
title: "Stop Building Subagents. Start Writing Skills."
source: "https://alexlavaee.me/blog/skills-over-subagents/"
author: "alexlavaee.me"
published: 
created: 2026-06-07
description: "We had a code review subagent. A generation subagent."
tags:
  - to-process
  - agent-configuration
---

![Stop Building Subagents. Start Writing Skills.](https://alexlavaee.me/_astro/cover.BMOf0r-U_ZNa8yO.webp)
Your context window is a budget. Subagents blow through it. Skills don’t.


We had a code review subagent. A generation subagent. A research subagent. A style consistency subagent. Each carried its own system prompt, its own context window, its own initialization cost. They worked — until managing them became the bottleneck.


We replaced all of them with skills. Same capabilities. A fraction of the overhead.


The difference isn’t cosmetic. It’s architectural. And if you’re building AI-assisted development workflows in Claude Code, Cursor, or any of the 30+ tools that now support the [Agent Skills standard](https://agentskills.io/specification), understanding this difference will save you real context budget and real complexity.


## Your context window is a budget. Skills respect it.


Subagents are **eager-loaded**. Every invocation spins up a fresh context window carrying the full system prompt, tool definitions, and conversation context — whether you need all of it or not. Ten subagents means ten separate context windows, each paying the full cost upfront.


Skills are **lazy-loaded** through a mechanism the [Agent Skills specification](https://agentskills.io/specification) calls **progressive context disclosure**. It works in three stages:


#mermaid-0{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;fill:#cdd6f4;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-0 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-0 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-0 .error-icon{fill:#cba6f7;}#mermaid-0 .error-text{fill:#1e1e2e;stroke:#1e1e2e;}#mermaid-0 .edge-thickness-normal{stroke-width:1px;}#mermaid-0 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-0 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-0 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-0 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-0 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-0 .marker{fill:#bac2de;stroke:#bac2de;}#mermaid-0 .marker.cross{stroke:#bac2de;}#mermaid-0 svg{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;}#mermaid-0 p{margin:0;}#mermaid-0 .label{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;color:#1e1e2e;}#mermaid-0 .cluster-label text{fill:#cdd6f4;}#mermaid-0 .cluster-label span{color:#cdd6f4;}#mermaid-0 .cluster-label span p{background-color:transparent;}#mermaid-0 .label text,#mermaid-0 span{fill:#1e1e2e;color:#1e1e2e;}#mermaid-0 .node rect,#mermaid-0 .node circle,#mermaid-0 .node ellipse,#mermaid-0 .node polygon,#mermaid-0 .node path{fill:#89b4fa;stroke:#74c7ec;stroke-width:1px;}#mermaid-0 .rough-node .label text,#mermaid-0 .node .label text,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-anchor:middle;}#mermaid-0 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-0 .rough-node .label,#mermaid-0 .node .label,#mermaid-0 .image-shape .label,#mermaid-0 .icon-shape .label{text-align:center;}#mermaid-0 .node.clickable{cursor:pointer;}#mermaid-0 .root .anchor path{fill:#bac2de!important;stroke-width:0;stroke:#bac2de;}#mermaid-0 .arrowheadPath{fill:#e1e1d1;}#mermaid-0 .edgePath .path{stroke:#bac2de;stroke-width:1px;}#mermaid-0 .flowchart-link{stroke:#bac2de;fill:none;}#mermaid-0 .edgeLabel{background-color:#313244;text-align:center;}#mermaid-0 .edgeLabel p{background-color:#313244;}#mermaid-0 .edgeLabel rect{opacity:0.5;background-color:#313244;fill:#313244;}#mermaid-0 .labelBkg{background-color:rgba(49, 50, 68, 0.5);}#mermaid-0 .cluster rect{fill:rgba(137, 180, 250, 0.1);stroke:#89b4fa;stroke-width:1px;}#mermaid-0 .cluster text{fill:#cdd6f4;}#mermaid-0 .cluster span{color:#cdd6f4;}#mermaid-0 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:12px;background:#cba6f7;border:1px solid #8839ef;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-0 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#cdd6f4;}#mermaid-0 rect.text{fill:none;stroke-width:0;}#mermaid-0 .icon-shape,#mermaid-0 .image-shape{background-color:#313244;text-align:center;}#mermaid-0 .icon-shape p,#mermaid-0 .image-shape p{background-color:#313244;padding:2px;}#mermaid-0 .icon-shape .label rect,#mermaid-0 .image-shape .label rect{opacity:0.5;background-color:#313244;fill:#313244;}#mermaid-0 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-0 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-0 .node .neo-node{stroke:#74c7ec;}#mermaid-0 [data-look=&quot;neo&quot;].node rect,#mermaid-0 [data-look=&quot;neo&quot;].cluster rect,#mermaid-0 [data-look=&quot;neo&quot;].node polygon{stroke:url(#mermaid-0-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-0 [data-look=&quot;neo&quot;].node path{stroke:url(#mermaid-0-gradient);stroke-width:1px;}#mermaid-0 [data-look=&quot;neo&quot;].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-0 [data-look=&quot;neo&quot;].node .neo-line path{stroke:#74c7ec;filter:none;}#mermaid-0 [data-look=&quot;neo&quot;].node circle{stroke:url(#mermaid-0-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-0 [data-look=&quot;neo&quot;].node circle .state-start{fill:#000000;}#mermaid-0 [data-look=&quot;neo&quot;].icon-shape .icon{fill:url(#mermaid-0-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-0 [data-look=&quot;neo&quot;].icon-shape .icon-neo path{stroke:url(#mermaid-0-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-0 :root{--mermaid-font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;}Subagents: Eager Loading

Every invocation

Full system prompt  
+ context window  
+ tool definitions

Skills: Lazy Loading

Skill invoked

Resource needed

Session start  
Load metadata only  
~100 tokens per skill

Load full instructions  
< 5,000 tokens

Load supporting files  
on demand

When Claude Code starts a session, it loads only the `name` and `description` from each installed skill — roughly 100 tokens per skill. The full instruction body (recommended under 5,000 tokens) loads only when the skill is invoked. Supporting files — scripts, reference docs, templates — load on demand, only when the agent determines they’re needed during execution.


You can have dozens of skills installed and pay almost nothing until one is actually called. The [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/skills) specifies the budget explicitly: skill descriptions consume approximately **2% of the context window**, with a 16,000-character fallback.


Compare that to spinning up a subagent with a multi-thousand-token system prompt every time you need a code review.


Here’s the complete structure of a skill:


And here’s the `SKILL.md` itself:


That’s it. A directory with a Markdown file. No framework. No SDK. No orchestration layer. The metadata frontmatter stays in context so the agent knows the skill exists. The instruction body loads only when you need it.


## Folder structure replaces orchestration logic


The second advantage is project-scoped expertise through automatic discovery.


Claude Code resolves skills hierarchically, with higher-priority locations winning when names conflict:




| Priority | Location | Path | Scope |
| --- | --- | --- | --- |
| Highest | Enterprise | Managed settings | All users in org |
|  | Personal | `~/.claude/skills/` | All your projects |
|  | Project | `.claude/skills/` | This project only |
| Lowest | Plugin | `<plugin>/skills/` | Where plugin is enabled |


The feature that matters for teams: **nested directory auto-discovery**. From the [Claude Code docs](https://docs.anthropic.com/en/docs/claude-code/skills): *“When you work with files in subdirectories, Claude Code automatically discovers skills from nested `.claude/skills/` directories.”*


In practice, a monorepo looks like this:


When you’re editing a file in `packages/frontend/`, Claude loads the frontend skills automatically. Switch to backend code, and the backend skills activate instead.


No routing logic. No subagent orchestration. No conditional dispatch based on file paths. The folder structure **is** the routing.


This eliminates an entire class of problems: the code reviewer that applies React conventions to Go code, the generator that doesn’t know which framework you’re in, the style enforcer that fights your team’s actual conventions.


## Portable expertise, not isolated workers


A skill works identically whether invoked from a code generation workflow, a review pass, or a deployment pipeline. It’s expertise that makes the agent better everywhere it’s loaded.


This portability extends beyond a single tool. The Agent Skills format is an [open standard](https://agentskills.io/specification) maintained at [agentskills.io](https://agentskills.io/home), with adoption from **over 30 tools** — Claude Code, Cursor, GitHub Copilot, OpenAI Codex, Gemini CLI, JetBrains Junie, Roo Code, Amp, and more.


Installation is one command via the [Vercel-backed CLI](https://github.com/vercel-labs/skills):


Or skip the CLI and create one by hand:


One caveat worth noting honestly: the open standard specifies a minimal base — `name`, `description`, and Markdown instructions. Claude Code’s advanced features like `context: fork`, `disable-model-invocation`, hooks, and model selection are extensions, not part of the portable spec. A skill using only base fields works across all 30+ tools. A skill using Claude-specific features won’t.


Write to the base spec by default. Use extensions when you need them. Your skills stay portable.


## Subagents still have a job — a smaller one


Skills don’t replace subagents entirely. Subagents are the right choice when you need:


* **Parallel execution with isolated context** — running tests, builds, and linting simultaneously without cross-contamination
* **Tool isolation** — restricting which tools an agent can access for security or scoping
* **Long-running tasks** — work that produces verbose output you don’t want polluting the main conversation
* **Different model selection** — using a faster, cheaper model for simple tasks


The mental model that emerged from our switch: **skills are portable expertise, subagents are isolated workers.** And subagents should *use* skills, not replace them.


Claude Code supports this directly — subagent definitions can preload skills via a `skills` field in their frontmatter, giving the isolated worker access to specialized knowledge without duplicating it into the system prompt. One important constraint: [subagents cannot spawn other subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents). They’re leaf nodes, not orchestrators.


Here’s a decision framework:


#mermaid-1{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;fill:#cdd6f4;}@keyframes edge-animation-frame{from{stroke-dashoffset:0;}}@keyframes dash{to{stroke-dashoffset:0;}}#mermaid-1 .edge-animation-slow{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 50s linear infinite;stroke-linecap:round;}#mermaid-1 .edge-animation-fast{stroke-dasharray:9,5!important;stroke-dashoffset:900;animation:dash 20s linear infinite;stroke-linecap:round;}#mermaid-1 .error-icon{fill:#cba6f7;}#mermaid-1 .error-text{fill:#1e1e2e;stroke:#1e1e2e;}#mermaid-1 .edge-thickness-normal{stroke-width:1px;}#mermaid-1 .edge-thickness-thick{stroke-width:3.5px;}#mermaid-1 .edge-pattern-solid{stroke-dasharray:0;}#mermaid-1 .edge-thickness-invisible{stroke-width:0;fill:none;}#mermaid-1 .edge-pattern-dashed{stroke-dasharray:3;}#mermaid-1 .edge-pattern-dotted{stroke-dasharray:2;}#mermaid-1 .marker{fill:#bac2de;stroke:#bac2de;}#mermaid-1 .marker.cross{stroke:#bac2de;}#mermaid-1 svg{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:16px;}#mermaid-1 p{margin:0;}#mermaid-1 .label{font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;color:#1e1e2e;}#mermaid-1 .cluster-label text{fill:#cdd6f4;}#mermaid-1 .cluster-label span{color:#cdd6f4;}#mermaid-1 .cluster-label span p{background-color:transparent;}#mermaid-1 .label text,#mermaid-1 span{fill:#1e1e2e;color:#1e1e2e;}#mermaid-1 .node rect,#mermaid-1 .node circle,#mermaid-1 .node ellipse,#mermaid-1 .node polygon,#mermaid-1 .node path{fill:#89b4fa;stroke:#74c7ec;stroke-width:1px;}#mermaid-1 .rough-node .label text,#mermaid-1 .node .label text,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-anchor:middle;}#mermaid-1 .node .katex path{fill:#000;stroke:#000;stroke-width:1px;}#mermaid-1 .rough-node .label,#mermaid-1 .node .label,#mermaid-1 .image-shape .label,#mermaid-1 .icon-shape .label{text-align:center;}#mermaid-1 .node.clickable{cursor:pointer;}#mermaid-1 .root .anchor path{fill:#bac2de!important;stroke-width:0;stroke:#bac2de;}#mermaid-1 .arrowheadPath{fill:#e1e1d1;}#mermaid-1 .edgePath .path{stroke:#bac2de;stroke-width:1px;}#mermaid-1 .flowchart-link{stroke:#bac2de;fill:none;}#mermaid-1 .edgeLabel{background-color:#313244;text-align:center;}#mermaid-1 .edgeLabel p{background-color:#313244;}#mermaid-1 .edgeLabel rect{opacity:0.5;background-color:#313244;fill:#313244;}#mermaid-1 .labelBkg{background-color:rgba(49, 50, 68, 0.5);}#mermaid-1 .cluster rect{fill:rgba(137, 180, 250, 0.1);stroke:#89b4fa;stroke-width:1px;}#mermaid-1 .cluster text{fill:#cdd6f4;}#mermaid-1 .cluster span{color:#cdd6f4;}#mermaid-1 div.mermaidTooltip{position:absolute;text-align:center;max-width:200px;padding:2px;font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;font-size:12px;background:#cba6f7;border:1px solid #8839ef;border-radius:2px;pointer-events:none;z-index:100;}#mermaid-1 .flowchartTitleText{text-anchor:middle;font-size:18px;fill:#cdd6f4;}#mermaid-1 rect.text{fill:none;stroke-width:0;}#mermaid-1 .icon-shape,#mermaid-1 .image-shape{background-color:#313244;text-align:center;}#mermaid-1 .icon-shape p,#mermaid-1 .image-shape p{background-color:#313244;padding:2px;}#mermaid-1 .icon-shape .label rect,#mermaid-1 .image-shape .label rect{opacity:0.5;background-color:#313244;fill:#313244;}#mermaid-1 .label-icon{display:inline-block;height:1em;overflow:visible;vertical-align:-0.125em;}#mermaid-1 .node .label-icon path{fill:currentColor;stroke:revert;stroke-width:revert;}#mermaid-1 .node .neo-node{stroke:#74c7ec;}#mermaid-1 [data-look=&quot;neo&quot;].node rect,#mermaid-1 [data-look=&quot;neo&quot;].cluster rect,#mermaid-1 [data-look=&quot;neo&quot;].node polygon{stroke:url(#mermaid-1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-1 [data-look=&quot;neo&quot;].node path{stroke:url(#mermaid-1-gradient);stroke-width:1px;}#mermaid-1 [data-look=&quot;neo&quot;].node .outer-path{filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-1 [data-look=&quot;neo&quot;].node .neo-line path{stroke:#74c7ec;filter:none;}#mermaid-1 [data-look=&quot;neo&quot;].node circle{stroke:url(#mermaid-1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-1 [data-look=&quot;neo&quot;].node circle .state-start{fill:#000000;}#mermaid-1 [data-look=&quot;neo&quot;].icon-shape .icon{fill:url(#mermaid-1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-1 [data-look=&quot;neo&quot;].icon-shape .icon-neo path{stroke:url(#mermaid-1-gradient);filter:drop-shadow( 1px 2px 2px rgba(185,185,185,1));}#mermaid-1 :root{--mermaid-font-family:&quot;trebuchet ms&quot;,verdana,arial,sans-serif;}Yes

No

Yes

No

Yes

No

Need parallel execution  
or isolated context?

Use a Subagent

Need tool isolation  
or permission scoping?

Output too verbose for  
main conversation?

Use a Skill

Preload relevant skills  
into your subagent

## The ecosystem already moved


Anthropic’s [skills repository](https://github.com/anthropics/skills) is the most-starred repo in their GitHub org with over 90,000 stars. The [open standard](https://github.com/agentskills/agentskills) has over 13,000 stars and 34 contributors. Multiple third-party directories have emerged — [skills.sh](https://skills.sh) backed by Vercel Labs, [agentskill.sh](https://agentskill.sh), and others — collectively indexing tens of thousands of community-contributed skills.


This isn’t a feature announcement. It’s an ecosystem shift. When 30+ tools converge on the same primitive, the tooling and community resources compound fast.


The barrier to entry is a Markdown file in the right directory. The ceiling is as high as your workflow demands.


Start with a skill. Upgrade to a subagent only when you need isolation or parallelism. Your context window is too valuable to spend on infrastructure that could be lazy-loaded.


## References


1. [Claude Code Skills Documentation](https://docs.anthropic.com/en/docs/claude-code/skills) — Anthropic’s official reference for skill architecture, loading behavior, and configuration
2. [Claude Code Sub-agents Documentation](https://docs.anthropic.com/en/docs/claude-code/sub-agents) — Official guide for when and how to use subagents
3. [Agent Skills Specification](https://agentskills.io/specification) — The open standard for cross-tool skill portability
4. [Agent Skills Adopters](https://agentskills.io/home) — Full list of 30+ tools supporting the Agent Skills format
5. [anthropics/skills](https://github.com/anthropics/skills) — Anthropic’s official skills repository with example implementations
6. [Vercel Labs Skills CLI](https://github.com/vercel-labs/skills) — CLI tool for installing and managing skills across agents