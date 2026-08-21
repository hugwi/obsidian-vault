---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, ai-agents]
tags:
  - harness
  - orchestration
source: readwise
created: 2026-06-23
rating: 
action: 
theme: multi-agent-orchestration
subtheme:
  - sub-agents
---

# pi-remote-agent

![rw-book-cover](https://pi.dev/social.png)

## Metadata
- Author: [[pi.dev]]
- Full Title: pi-remote-agent
- Category: #articles
- Summary: pi-remote-agent is a pi extension that lets you connect your pi session to a friend's pi instance for collaboration. It uses secure Tailscale connections and allows both manual and automatic task delegation. You can install it from npm and configure remote peers easily to share work in real-time.
- URL: https://pi.dev/packages/pi-remote-agent

## Full Document
#### Package details

Install `pi-remote-agent` from npm and Pi will load the resources declared by the package manifest.

`$ pi install npm:pi-remote-agent`Copy

`pi-remote-agent`0 dependencies · 2 peers
Pi manifest JSON
```
{
  "extensions": [
    "./index.ts"
  ],
  "image": "https://placehold.co/600x200/6C5CE7/white?text=pi-remote-agent+bridge"
}
```

#### Security note

Pi packages can execute code and influence agent behavior. Review the source before installing third-party packages.

#### README

#### 🧠 What is this?

**pi-remote-agent** is a pi extension that lets your pi session talk to another pi instance running on a friend's machine. Think pair programming, second opinions, or delegating subtasks — all from within your pi TUI.

Your LLM can even call the remote agent *automatically* via the `ask_remote_agent` tool.

#### 🚀 Quick Start

##### 1. Your friend sets up the bridge

On their machine, they run pi with the bridge enabled:

```
pi --bridge --rpc-port 18777

```

Their bridge will be reachable at `https://<their-tailscale-node>.ts.net/rpc`.

##### 2. You configure the peer

Add their bridge URL to your remote agents config:

```
# ~/.pi/agent/remote-agents.json
{
  "friend": "https://friend-mac.tail1234.ts.net/rpc"
}

```

Or set it once via environment variable:

```
export REMOTE_AGENT_URL="https://friend-mac.tail1234.ts.net/rpc"

```

##### 3. Install the extension

```
pi install npm:@aman-asmuei/pi-remote-agent

```

##### 4. Start delegating

```
# Command (manual)
/ask-agent @friend Refactor the auth module to use JWT instead of sessions

# Tool (LLM auto-invokes)
"When should I use a connection pool vs a single connection?"
→ LLM automatically calls ask_remote_agent

```

#### 📖 Usage

##### `/ask-agent` Command

```
/ask-agent <prompt>                → Uses default peer (REMOTE_AGENT_URL)
/ask-agent @friend <prompt>        → Targets a named peer from remote-agents.json

```

The command streams the response in real-time, showing which tools the remote agent is using (read, bash, edit, write).

##### `ask_remote_agent` Tool

The LLM can also call the remote agent automatically. It's registered as a tool in your session, so you don't need to manually decide when to delegate — your model routes tasks that benefit from an external perspective.

```
┌──────────────────────────────────────────────────┐
│  You: "Is this SQL query vulnerable to injection?"│
│                                                   │
│  Arienz: 🔒 Asking Security SME (remote)...        │
│  Remote: ❌ Yes — 3 vulnerabilities found.        │
│          • Unsanitized input on line 12            │
│          • No parameterized query on line 18       │
│          • User input in ORDER BY clause           │
└──────────────────────────────────────────────────┘

```

#### ⚙️ Configuration

| Key | Location | Description |
| --- | --- | --- |
| `REMOTE_AGENT_URL` | Environment | Default bridge URL (fallback) |
| `remote-agents.json` | `~/.pi/agent/` | Named peers with bridge URLs |

```
// ~/.pi/agent/remote-agents.json
{
  "alice":   "https://alice-dev.tail1234.ts.net/rpc",
  "bob":     "https://bob-server.tail1234.ts.net/rpc",
  "work":    "https://ci-bot.work-net.ts.net/rpc"
}

```

#### 🔒 Security

* All traffic routes through **Tailscale's encrypted mesh** — no open ports, no public exposure
* Sessions are ephemeral — created, used, and destroyed per-request
* Your API keys and credentials are never sent to the remote agent
* Extensions have full system access — review the source before installing (this repo is MIT-licensed and auditable at [index.ts](https://cdn.jsdelivr.net/npm/pi-remote-agent@1.0.0/index.ts))

#### 📁 Project Structure

```
pi-remote-agent/
├── index.ts          # Extension entry point (single file)
├── package.json      # pi package manifest
└── README.md         # You are here

```

#### 🛠️ Development

```
# Clone and test locally
git clone https://github.com/aman-asmuei/pi-remote-agent
cd pi-remote-agent
pi install ./    # Install from local path

# Or test without installing
pi -e ./index.ts

```

#### 📄 License

MIT © Aman — share, remix, and build on it freely.
