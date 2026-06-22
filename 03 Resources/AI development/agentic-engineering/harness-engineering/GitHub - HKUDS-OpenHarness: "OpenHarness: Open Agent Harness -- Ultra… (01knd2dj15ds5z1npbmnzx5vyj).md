---
title: "GitHub - HKUDS/OpenHarness: \"OpenHarness: Open Agent Harness -- Ultra-Lightweight"
source: "https://github.com/HKUDS/OpenHarness"
author: "github.com/HKUDS"
published: 
created: 2026-04-04
description: "OpenHarness: Open Agent Harness -- Ultra-Lightweight Claude Code\" - HKUDS/OpenHarness"
tags:
  - to-process
  - harness-engineering
---

# HKUDS/OpenHarness


main


Go to file


Code


Open more actions menu


# [OpenHarness](https://github.com/HKUDS/OpenHarness/blob/main/assets/logo.png) `oh` — OpenHarness: Open Agent Harness


• **O**pen**H**arness (**oh**) is an ultra-lightweight alternative to Claude Code with pure Python implementation


• **OpenHarness** delivers approximately 80% of essential agent functionality


• **OpenHarness** achieves this using just 3% of the lines of code compared to Claude Code


[![Quick Start](https://camo.githubusercontent.com/18c3f5ac06054dbfca3df1eb20a71cf748c05e13ab8007b7c80bf09bd9578f01/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f517569636b5f53746172742d355f6d696e2d626c75653f7374796c653d666f722d7468652d6261646765)](https://github.com/HKUDS/OpenHarness/#-quick-start)
[![Architecture](https://camo.githubusercontent.com/2f568dd2a9ecfae4811f5d134d5513acb1724764fe47cfb635f2062afa3cf7e6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4861726e6573732d4172636869746563747572652d6666363962343f7374796c653d666f722d7468652d6261646765)](https://github.com/HKUDS/OpenHarness/#-harness-architecture)
[![Tools](https://camo.githubusercontent.com/51cf8899903755832d67b527dffee6e2417bd4794f22c6d53fc80fa4ed6d8517/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f546f6f6c732d34332b2d677265656e3f7374796c653d666f722d7468652d6261646765)](https://github.com/HKUDS/OpenHarness/#-features)
[![Tests](https://camo.githubusercontent.com/68aa60d421b5dec2a896532c4dee964e9b6e60e41bf070e3857ee3ef404e08b3/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f54657374732d3131345f50617373696e672d627269676874677265656e3f7374796c653d666f722d7468652d6261646765)](https://github.com/HKUDS/OpenHarness/#-test-results)
[![License](https://camo.githubusercontent.com/2792a6b590e1b7fbcc5f7c80df8da3149453c596df80f16fa86bd82c487bec8d/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d4d49542d79656c6c6f773f7374796c653d666f722d7468652d6261646765)](https://github.com/HKUDS/OpenHarness/blob/main/LICENSE)
[![Python](https://camo.githubusercontent.com/d3abf9bd79c1832b5a624531e3d02fe7a7c4a663e98ff3da4dbb8a936b7af292/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2de289a5332e31312d626c75653f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/d3abf9bd79c1832b5a624531e3d02fe7a7c4a663e98ff3da4dbb8a936b7af292/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2de289a5332e31312d626c75653f6c6f676f3d707974686f6e266c6f676f436f6c6f723d7768697465)
[![React](https://camo.githubusercontent.com/1c9e9116d8fcfa8db329c1163954535d01fefd21ea4b1f823b690d80b6ef459c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742b496e6b2d5455492d3631444146423f6c6f676f3d7265616374266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/1c9e9116d8fcfa8db329c1163954535d01fefd21ea4b1f823b690d80b6ef459c/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f52656163742b496e6b2d5455492d3631444146423f6c6f676f3d7265616374266c6f676f436f6c6f723d7768697465)
[![Pytest](https://camo.githubusercontent.com/8249a84df54a4d702050a87a1a0717697a14600c397dcadacd6702e2760bc7f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7079746573742d3131345f706173732d627269676874677265656e)](https://camo.githubusercontent.com/8249a84df54a4d702050a87a1a0717697a14600c397dcadacd6702e2760bc7f1/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f7079746573742d3131345f706173732d627269676874677265656e)
[![E2E](https://camo.githubusercontent.com/85df2cd099b9873917856f50a386b0b8f2234acd30123f132dbcec2149b6c301/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4532452d365f7375697465732d6f72616e6765)](https://camo.githubusercontent.com/85df2cd099b9873917856f50a386b0b8f2234acd30123f132dbcec2149b6c301/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4532452d365f7375697465732d6f72616e6765)
[![Output](https://camo.githubusercontent.com/1e0982f7cc92ba33229342173a093de06653fa8d64e3a0ac1a3201da918ebb95/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6f75747075742d746578745f7c5f6a736f6e5f7c5f73747265616d2d2d6a736f6e2d626c756576696f6c6574)](https://camo.githubusercontent.com/1e0982f7cc92ba33229342173a093de06653fa8d64e3a0ac1a3201da918ebb95/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6f75747075742d746578745f7c5f6a736f6e5f7c5f73747265616d2d2d6a736f6e2d626c756576696f6c6574)
[![Feishu](https://camo.githubusercontent.com/bd35c9ed9293c731eb7291729ccf72034a9f1fe9f840d4d8668e84cd4333010e/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4665697368752d47726f75702d4539444246433f7374796c653d666c6174266c6f676f3d666569736875266c6f676f436f6c6f723d7768697465)](https://github.com/HKUDS/.github/blob/main/profile/README.md)
[![WeChat](https://camo.githubusercontent.com/08ab611a06d7426a0b4d1c949dfe5acc00edc85da0e5ecb242c7ce2a9652d1a8/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f5765436861742d47726f75702d4335454142343f7374796c653d666c6174266c6f676f3d776563686174266c6f676f436f6c6f723d7768697465)](https://github.com/HKUDS/.github/blob/main/profile/README.md)
One Command (**oh**) to Launch **OpenHarness** and Unlock All Agent Harnesses.


Supports CLI agent integration including OpenClaw, nanobot, Cursor, and more.


[![OpenHarness Terminal Demo](https://github.com/HKUDS/OpenHarness/raw/main/assets/cli-typing.gif)](https://github.com/HKUDS/OpenHarness/blob/main/assets/cli-typing.gif)
  [![OpenHarness Terminal Demo](https://github.com/HKUDS/OpenHarness/raw/main/assets/cli-typing.gif)](https://github.com/HKUDS/OpenHarness/blob/main/assets/cli-typing.gif)  


[![How Agent Harness Works](https://github.com/HKUDS/OpenHarness/raw/main/assets/architecture-comic.png)](https://github.com/HKUDS/OpenHarness/blob/main/assets/architecture-comic.png)
## 🚀 44x Lighter Than Claude Code




|  | Claude Code | OpenHarness |
| --- | --- | --- |
| **Lines of Code** | 512,664 | **11,733** (44x lighter) |
| **Files** | 1,884 | **163** |
| **Language** | TypeScript | Python |
| **Tools** | ~44 | 43 (98%) |
| **Commands** | ~88 | 54 (61%) |
| **Skills Compatible** | ✅ | ✅ anthropics/skills |
| **Plugin Compatible** | ✅ | ✅ claude-code/plugins |
| **Tests** | — | 114 unit + 6 E2E suites |


**Just 2.3% of the code, 98% of the essential tools**. Leverages Python's power with pure focus on Harness architecture—stripped of enterprise overhead like telemetry, OAuth complexity, and hundreds of React components.


## 🤔 What is an Agent Harness?


An **Agent Harness** is the complete infrastructure that wraps around an LLM to make it a functional agent. The model provides intelligence; the harness provides **hands, eyes, memory, and safety boundaries**.


[![Harness = Tools + Knowledge + Observation + Action + Permissions](https://github.com/HKUDS/OpenHarness/raw/main/assets/harness-equation.png)](https://github.com/HKUDS/OpenHarness/blob/main/assets/harness-equation.png)
OpenHarness is an open-source Python implementation designed for **researchers, builders, and the community**:


* **Understand** how production AI agents work under the hood
* **Experiment** with cutting-edge tools, skills, and agent coordination patterns
* **Extend** the harness with custom plugins, providers, and domain knowledge
* **Build** specialized agents on top of proven architecture


## 📰 What's New


* **2026-04-01** 🎨 **v0.1.0** — Initial **OpenHarness** open-source release featuring complete Harness architecture:


## 🚀 Quick Start


### Prerequisites


* **Python 3.11+** and [uv](https://docs.astral.sh/uv/)
* **Node.js 18+** (for the React terminal UI)
* An LLM API key


### Install & Run



```
# Clone and install
git clone https://github.com/HKUDS/OpenHarness.git
cd OpenHarness
uv sync --extra dev

# Example: use Kimi as the backend
export ANTHROPIC_BASE_URL=https://api.moonshot.cn/anthropic
export ANTHROPIC_API_KEY=your_kimi_api_key
export ANTHROPIC_MODEL=kimi-k2.5

# Launch
oh                    # if venv is activated
uv run oh             # without activating venv
```

[![OpenHarness Landing Screen](https://github.com/HKUDS/OpenHarness/raw/main/assets/landing.png)](https://github.com/HKUDS/OpenHarness/blob/main/assets/landing.png)
### Non-Interactive Mode (Pipes & Scripts)



```
# Single prompt → stdout
oh -p "Explain this codebase"

# JSON output for programmatic use
oh -p "List all functions in main.py" --output-format json

# Stream JSON events in real-time
oh -p "Fix the bug" --output-format stream-json
```

## 🏗️ Harness Architecture


OpenHarness implements the core Agent Harness pattern with 10 subsystems:



```
openharness/
  engine/          # 🧠 Agent Loop — query → stream → tool-call → loop
  tools/           # 🔧 43 Tools — file I/O, shell, search, web, MCP
  skills/          # 📚 Knowledge — on-demand skill loading (.md files)
  plugins/         # 🔌 Extensions — commands, hooks, agents, MCP servers
  permissions/     # 🛡️ Safety — multi-level modes, path rules, command deny
  hooks/           # ⚡ Lifecycle — PreToolUse/PostToolUse event hooks
  commands/        # 💬 54 Commands — /help, /commit, /plan, /resume, ...
  mcp/             # 🌐 MCP — Model Context Protocol client
  memory/          # 🧠 Memory — persistent cross-session knowledge
  tasks/           # 📋 Tasks — background task management
  coordinator/     # 🤝 Multi-Agent — subagent spawning, team coordination
  prompts/         # 📝 Context — system prompt assembly, CLAUDE.md, skills
  config/          # ⚙️ Settings — multi-layer config, migrations
  ui/              # 🖥️ React TUI — backend protocol + frontend

```

### The Agent Loop


The heart of the harness. One loop, endlessly composable:



```
while True:
    response = await api.stream(messages, tools)
    
    if response.stop_reason != "tool_use":
        break  # Model is done
    
    for tool_call in response.tool_uses:
        # Permission check → Hook → Execute → Hook → Result
        result = await harness.execute_tool(tool_call)
    
    messages.append(tool_results)
    # Loop continues — model sees results, decides next action
```

The model decides **what** to do. The harness handles **how** — safely, efficiently, with full observability.


## ✨ Features


### 🔧 Tools (43+)




| Category | Tools | Description |
| --- | --- | --- |
| **File I/O** | Bash, Read, Write, Edit, Glob, Grep | Core file operations with permission checks |
| **Search** | WebFetch, WebSearch, ToolSearch, LSP | Web and code search capabilities |
| **Notebook** | NotebookEdit | Jupyter notebook cell editing |
| **Agent** | Agent, SendMessage, TeamCreate/Delete | Subagent spawning and coordination |
| **Task** | TaskCreate/Get/List/Update/Stop/Output | Background task management |
| **MCP** | MCPTool, ListMcpResources, ReadMcpResource | Model Context Protocol integration |
| **Mode** | EnterPlanMode, ExitPlanMode, Worktree | Workflow mode switching |
| **Schedule** | CronCreate/List/Delete, RemoteTrigger | Scheduled and remote execution |
| **Meta** | Skill, Config, Brief, Sleep, AskUser | Knowledge loading, configuration, interaction |


Every tool has:


* **Pydantic input validation** — structured, type-safe inputs
* **Self-describing JSON Schema** — models understand tools automatically
* **Permission integration** — checked before every execution
* **Hook support** — PreToolUse/PostToolUse lifecycle events


### 📚 Skills System


Skills are **on-demand knowledge** — loaded only when the model needs them:



```
Available Skills:
- commit: Create clean, well-structured git commits
- review: Review code for bugs, security issues, and quality
- debug: Diagnose and fix bugs systematically
- plan: Design an implementation plan before coding
- test: Write and run tests for code
- simplify: Refactor code to be simpler and more maintainable
- pdf: PDF processing with pypdf (from anthropics/skills)
- xlsx: Excel operations (from anthropics/skills)
- ... 40+ more

```

**Compatible with [anthropics/skills](https://github.com/anthropics/skills)** — just copy `.md` files to `~/.openharness/skills/`.


### 🔌 Plugin System


**Compatible with [claude-code plugins](https://github.com/anthropics/claude-code/tree/main/plugins)**. Tested with 12 official plugins:




| Plugin | Type | What it does |
| --- | --- | --- |
| `commit-commands` | Commands | Git commit, push, PR workflows |
| `security-guidance` | Hooks | Security warnings on file edits |
| `hookify` | Commands + Agents | Create custom behavior hooks |
| `feature-dev` | Commands | Feature development workflow |
| `code-review` | Agents | Multi-agent PR review |
| `pr-review-toolkit` | Agents | Specialized PR review agents |



```
# Manage plugins
oh plugin list
oh plugin install <source>
oh plugin enable <name>
```

### 🛡️ Permissions


Multi-level safety with fine-grained control:




| Mode | Behavior | Use Case |
| --- | --- | --- |
| **Default** | Ask before write/execute | Daily development |
| **Auto** | Allow everything | Sandboxed environments |
| **Plan Mode** | Block all writes | Large refactors, review first |


**Path-level rules** in `settings.json`:



```
{
  "permission": {
    "mode": "default",
    "path_rules": [{"pattern": "/etc/*", "allow": false}],
    "denied_commands": ["rm -rf /", "DROP TABLE *"]
  }
}
```

### 🖥️ Terminal UI


React/Ink TUI with full interactive experience:


* **Command picker**: Type `/` → arrow keys to select → Enter
* **Permission dialog**: Interactive y/n with tool details
* **Mode switcher**: `/permissions` → select from list
* **Session resume**: `/resume` → pick from history
* **Animated spinner**: Real-time feedback during tool execution
* **Keyboard shortcuts**: Shown at the bottom, context-aware


### 📡 CLI



```
oh [OPTIONS] COMMAND [ARGS]

Session:     -c/--continue, -r/--resume, -n/--name
Model:       -m/--model, --effort, --max-turns
Output:      -p/--print, --output-format text|json|stream-json
Permissions: --permission-mode, --dangerously-skip-permissions
Context:     -s/--system-prompt, --append-system-prompt, --settings
Advanced:    -d/--debug, --mcp-config, --bare

Subcommands: oh mcp | oh plugin | oh auth

```

## 📊 Test Results




| Suite | Tests | Status |
| --- | --- | --- |
| Unit + Integration | 114 | ✅ All passing |
| CLI Flags E2E | 6 | ✅ Real model calls |
| Harness Features E2E | 9 | ✅ Retry, skills, parallel, permissions |
| React TUI E2E | 3 | ✅ Welcome, conversation, status |
| TUI Interactions E2E | 4 | ✅ Commands, permissions, shortcuts |
| Real Skills + Plugins | 12 | ✅ anthropics/skills + claude-code/plugins |



```
# Run all tests
uv run pytest -q                           # 114 unit/integration
python scripts/test_harness_features.py     # Harness E2E
python scripts/test_real_skills_plugins.py  # Real plugins E2E
```

## 🔧 Extending OpenHarness


### Add a Custom Tool



```
from pydantic import BaseModel, Field
from openharness.tools.base import BaseTool, ToolExecutionContext, ToolResult

class MyToolInput(BaseModel):
    query: str = Field(description="Search query")

class MyTool(BaseTool):
    name = "my_tool"
    description = "Does something useful"
    input_model = MyToolInput

    async def execute(self, arguments: MyToolInput, context: ToolExecutionContext) -> ToolResult:
        return ToolResult(output=f"Result for: {arguments.query}")
```

### Add a Custom Skill


Create `~/.openharness/skills/my-skill.md`:



```
---
name: my-skill
description: Expert guidance for my specific domain
---

# My Skill

## When to use
Use when the user asks about [your domain].

## Workflow
1. Step one
2. Step two
...
```

### Add a Plugin


Create `.openharness/plugins/my-plugin/.claude-plugin/plugin.json`:



```
{
  "name": "my-plugin",
  "version": "1.0.0",
  "description": "My custom plugin"
}
```

Add commands in `commands/*.md`, hooks in `hooks/hooks.json`, agents in `agents/*.md`.


## 🤝 Contributing


OpenHarness is a **community-driven research project**. We welcome contributions in:




| Area | Examples |
| --- | --- |
| **Tools** | New tool implementations for specific domains |
| **Skills** | Domain knowledge `.md` files (finance, science, DevOps...) |
| **Plugins** | Workflow plugins with commands, hooks, agents |
| **Providers** | Support for more LLM backends (OpenAI, Ollama, etc.) |
| **Multi-Agent** | Coordination protocols, team patterns |
| **Testing** | E2E scenarios, edge cases, benchmarks |
| **Documentation** | Architecture guides, tutorials, translations |



```
# Development setup
git clone https://github.com/HKUDS/OpenHarness.git
cd openharness
uv sync --extra dev
uv run pytest -q  # Verify everything works
```

## 📄 License


MIT — see [LICENSE](https://github.com/HKUDS/OpenHarness/blob/main/LICENSE).


[![OpenHarness](https://github.com/HKUDS/OpenHarness/raw/main/assets/logo.png)](https://github.com/HKUDS/OpenHarness/blob/main/assets/logo.png)
**Oh my Harness!**   

*The model is the agent. The code is the harness.*


 *Thanks for visiting ✨ OpenHarness!*


[![Views](https://camo.githubusercontent.com/ab07739706a4442375a45205aedf90ef7093408aa8aec59801c944b81ae64089/68747470733a2f2f76697369746f722d62616467652e6c616f62692e6963752f62616467653f706167655f69643d484b5544532e4f70656e4861726e657373267374796c653d666f722d7468652d626164676526636f6c6f723d303064346666)](https://camo.githubusercontent.com/ab07739706a4442375a45205aedf90ef7093408aa8aec59801c944b81ae64089/68747470733a2f2f76697369746f722d62616467652e6c616f62692e6963752f62616467653f706167655f69643d484b5544532e4f70656e4861726e657373267374796c653d666f722d7468652d626164676526636f6c6f723d303064346666)