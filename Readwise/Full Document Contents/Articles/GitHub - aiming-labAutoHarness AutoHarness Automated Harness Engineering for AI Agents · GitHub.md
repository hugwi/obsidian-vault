# GitHub - aiming-lab/AutoHarness: AutoHarness: Automated Harness Engineering for AI Agents · GitHub

![rw-book-cover](https://opengraph.githubassets.com/f03aa3dad45972bf13df6f32779b84eb6a8bb200ff98939adda4b61bed65d692/aiming-lab/AutoHarness)

## Metadata
- Author: [[https://github.com/aiming-lab/]]
- Full Title: GitHub - aiming-lab/AutoHarness: AutoHarness: Automated Harness Engineering for AI Agents · GitHub
- Category: #articles
- Summary: AutoHarness is a tool that helps AI agents become more reliable by managing risks, costs, and tools automatically. It uses a simple pipeline to check and control every action the agent takes, making sure it is safe and efficient. Users can easily add AutoHarness to their AI with just a few lines of code for better governance and audit trails.
- URL: https://github.com/aiming-lab/AutoHarness

## Full Document
### aiming-lab/AutoHarness

main

Go to file

Code

Open more actions menu

[![AutoHarness Logo](https://github.com/aiming-lab/AutoHarness/raw/main/images/logo.png)](https://github.com/aiming-lab/AutoHarness/blob/main/images/logo.png)
#### 「Aha」— AutoHarness: Automated Harness Engineering for AI Agents

##### *Every agent deserves an **aha** moment — the model reasons, we harness the rest.*

[![AutoHarness Poster](https://github.com/aiming-lab/AutoHarness/raw/main/images/poster.png)](https://github.com/aiming-lab/AutoHarness/blob/main/images/poster.png)
[![MIT License](https://camo.githubusercontent.com/fdf2982b9f5d7489dcf44570e714e3a15fce6253e0cc6b5aa61a075aac2ff71b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f772e737667)](https://github.com/aiming-lab/AutoHarness/blob/main/LICENSE)
[![Python 3.10+](https://camo.githubusercontent.com/2b6aa5b32389b93f49afea76fcbc0f2ff2a0090a347661fadba906d0d77c4010/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f507974686f6e2d332e31302532422d3337373641423f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](https://python.org)
[![958 Tests Passed](https://camo.githubusercontent.com/817a8c681cf50741972d7ce5556896c417ab7a8b8dfed359f40407b26c65579e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54657374732d3935382532307061737365642d627269676874677265656e3f6c6f676f3d707974657374266c6f676f436f6c6f723d7768697465)](https://github.com/aiming-lab/AutoHarness/#-quickstart)
[![GitHub](https://camo.githubusercontent.com/e6c1bc3f54442997f66ae61888272ae973ade270ce6a08ed52fa6975dc7810b6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4769744875622d4175746f4861726e6573732d3138313731373f6c6f676f3d676974687562)](https://github.com/aiming-lab/AutoHarness)
[![Ruff](https://camo.githubusercontent.com/c5fa1ce51bf2d8d23ba9d6adf4007b4fc4ef02183aba0da164a03198f2621275/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f436f64652532305374796c652d527566662d3030303030303f6c6f676f3d72756666266c6f676f436f6c6f723d7768697465)](https://github.com/astral-sh/ruff)
[![mypy](https://camo.githubusercontent.com/936d87764b991eb1cd48da5daffcb6871ac903364d1529471ef394fc9178e7a8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54797065253230436865636b2d6d7970792d626c75653f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](https://mypy-lang.org/)
[🇨🇳 简体中文](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_CN.md) · [🇯🇵 日本語](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_JA.md) · [🇰🇷 한국어](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_KO.md) · [🇪🇸 Español](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_ES.md) · [🇫🇷 Français](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_FR.md) · [🇩🇪 Deutsch](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_DE.md) · [🇵🇹 Português](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_PT.md) · [🇷🇺 Русский](https://github.com/aiming-lab/AutoHarness/blob/main/docs/README_RU.md)

#### 🤔 Why *Aha* (**A**uto**Ha**rness)?

>  In LLM training, the ***aha* moment** is when a model suddenly learns to reason.
> 
>  For agents, the ***aha* moment** is when they go from "demo-ready" to truly reliable.
> 
>  

The gap is enormous: context management, tool governance, cost control, observability, session persistence... These are the patterns that separate a toy from a system. We call this **harness engineering**.

AutoHarness is a lightweight governance framework **so every agent can have its *aha* moment.**

>  **Agent = Model + Harness.** The model reasons. The harness does everything else.
> 
>  

#### ⚡ Quick Install

```
git clone https://github.com/aiming-lab/AutoHarness.git
cd AutoHarness && pip install -e .
from openai import OpenAI
from autoharness import AutoHarness

client = AutoHarness.wrap(OpenAI())
# That's it. Your agent just had its aha moment.
```

#### 🔥 News

* **[04/01/2026]** [**v0.1.0 Released**](https://github.com/aiming-lab/AutoHarness/releases/tag/v0.1.0): Three-tier pipeline modes (Core / Standard / Enhanced ⚠️), 6-step governance pipeline, risk pattern matching, YAML constitution, trace-based diagnostics, multi-agent profiles, session persistence with cost tracking. **958 tests passing.**

#### 🚀 Quickstart

```
# Wrap any LLM client (2 lines, instant governance)
from openai import OpenAI
from autoharness import AutoHarness

client = AutoHarness.wrap(OpenAI())
response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[{"role": "user", "content": "Refactor auth.py"}],
    tools=[{"type": "function", "function": {"name": "Bash", "description": "Run shell commands",
            "parameters": {"type": "object", "properties": {"command": {"type": "string"}}}}}],
)
# Or use the full agent loop
from autoharness import AgentLoop

loop = AgentLoop(model="gpt-5.4", constitution="constitution.yaml")
result = loop.run("Fix the failing tests in auth.py")
```

>  **[More examples →](https://github.com/aiming-lab/AutoHarness/blob/main/docs/features.md#cli)**
> 
>  

#### 🔧 Pipeline Modes

AutoHarness supports three pipeline modes. Choose the level of governance that fits your needs:

| Mode | Pipeline | Hooks | Multi-Agent | Use Case |
| --- | --- | --- | --- | --- |
| **Core** | 6-step | Secret scanner + path guard + output sanitizer | Single agent | Lightweight governance |
| **Standard** | 8-step | + Risk classifier + pre-hooks | Basic profiles | Production agents |
| **Enhanced ⚠️** | 14-step | + Turn governor + alias resolution + failure hooks | Fork / Swarm / Background | Maximum governance |

```
# Switch modes via constitution
# constitution.yaml
mode: core      # or "standard" or "enhanced"
# Or via CLI
autoharness mode enhanced
```

>  **Enhanced ⚠️ is the default mode.** Users get the strongest governance out of the box. Switch to Core for minimal overhead.
> 
>  

>  **[Full mode comparison →](https://github.com/aiming-lab/AutoHarness/blob/main/docs/features.md#pipeline-modes)**
> 
>  

#### ✨ What You Get

| Without Harness | With AutoHarness |
| --- | --- |
| Agent runs `rm -rf /`, nothing stops it | **6-step pipeline** blocks it, logs it, explains why |
| Context explodes past token limit | **Token budget** + **truncation** keeps context under control |
| No idea which tool call cost how much | **Per-call cost attribution** with model-aware pricing |
| Prompt injection sneaks through | **Layered validation**: input rails, execution, output rails |
| No audit trail for compliance | **JSONL audit** logs every decision with full provenance |
| Agents share one permission set | **Multi-agent profiles** with role-based governance |

##### Core Architecture: 6-Step Governance Pipeline

Every tool call flows through a structured pipeline:

```
1. Parse & Validate  →  2. Risk Classify  →  3. Permission Check
4. Execute           →  5. Output Sanitize →  6. Audit Log

```

Built-in risk patterns detect dangerous operations, secret exposure, path traversal, and more.

##### By the Numbers

```
6-step governance pipeline   ·  Risk pattern matching      ·  YAML constitution
Token budget management      ·  Multi-agent profiles       ·  JSONL audit trail
2 lines to integrate         ·  0 vendor lock-in           ·  MIT licensed

```

#### 🖥️ CLI

```
autoharness init                          # Interactive wizard (agent type, LLM provider, security level, pipeline mode, etc.)
autoharness mode                          # Show current pipeline mode
autoharness mode enhanced                 # Switch pipeline mode
autoharness validate constitution.yaml    # Validate a constitution file
autoharness check --stdin --format json   # Check a tool call against your rules (tool_name/tool_input format)
autoharness audit summary                 # View audit summary
autoharness install --target claude-code  # Install as a Claude Code hook (one command)
autoharness export --format cursor        # Export cross-harness constitution
```

#### 📊 How We Compare

| Capability | AutoHarness | LangGraph | Guardrails AI | OpenAI SDK |
| --- | --- | --- | --- | --- |
| Tool governance pipeline | ✅ 6-step (up to 14) | ❌ | ⚠️ Output-only | ❌ |
| Context management | ✅ Multi-layer | ❌ | ❌ | ⚠️ Trimming |
| Multi-agent profiles | ✅ | ✅ Graph | ❌ | ⚠️ Handoff |
| Validation (input+output) | ✅ | ❌ | ✅ Rails | ❌ |
| Trace-based diagnostics | ✅ | ❌ | ❌ | ❌ |
| Cost attribution | ✅ Per-call | ❌ | ❌ | ❌ |
| Vendor lock-in | None | LangChain | None | OpenAI |
| Setup | 2 lines | Graph DSL | RAIL XML | SDK |

#### 🙏 Acknowledgments

* [Claude Code](https://docs.anthropic.com/en/docs/claude-code) by Anthropic: engineering patterns that inspired some of our features in the Enhanced ⚠️ mode
* [Codex](https://github.com/openai/codex) by OpenAI: context engineering practices that informed our context management design

#### 📌 Citation

If you use AutoHarness in your research, please cite:

```
@software{autoharness2026,
  title   = {AutoHarness: The Harness Engineering Framework for AI Agents},
  author  = {{AutoHarness Team}},
  year    = {2026},
  url     = {https://github.com/aiming-lab/AutoHarness},
  license = {MIT}
}
```

#### ⚠️ Disclaimer

Some architectural decisions in the Enhanced mode were informed by publicly available analysis and community discussion of Claude Code's design following its inadvertent publication via Anthropic's npm registry on 2026-03-31. We acknowledge that Claude Code's original source code is the intellectual property of Anthropic. AutoHarness does not contain, redistribute, or directly translate any of Anthropic's proprietary code. We respect Anthropic's IP rights and will promptly address any concerns — please contact us via [issue](https://github.com/aiming-lab/AutoHarness/issues) or [autoharness.aha@gmail.com](mailto:autoharness.aha@gmail.com).

#### 📄 License

MIT. See [LICENSE](https://github.com/aiming-lab/AutoHarness/blob/main/LICENSE) for details.
