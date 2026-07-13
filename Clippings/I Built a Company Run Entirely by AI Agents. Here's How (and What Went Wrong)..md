---
title: "I Built a Company Run Entirely by AI Agents. Here's How (and What Went Wrong)."
source: "https://dev.to/nunc/i-built-a-company-run-entirely-by-ai-agents-heres-how-and-what-went-wrong-4hli"
author:
  - "[[dev.to]]"
published: 2026-02-10
created: 2026-07-13
description: "Seven AI agents. One cheap VPS. A corporate hierarchy with a CEO, CTO, and five employees, all of... Tagged with ai, agents, opensource, experiment."
tags:
  - "clippings"
---
Seven AI agents. One cheap VPS. A corporate hierarchy with a CEO, CTO, and five employees, all of them bots. No human in the loop except me, checking in once a day to see what they'd done.

Within a week they'd founded a company, pivoted the business model on their own, and shipped a working product with 158 tests.

They also forgot to update half their own files and left two employees without names.

This is how you build an AI-run company. And what actually happens when you do.

## The Idea

Most "AI agent" demos show a single bot doing a single task. I wanted something messier: **multiple persistent agents with different roles, working together over days, making their own decisions.**

Not "AI-assisted development" where a human drives. The opposite. Agents decide what to build, how to build it, who does what. I set the direction and approve the big calls.

The framework that makes this possible is [OpenClaw](https://github.com/openclaw/openclaw), an open-source agent platform. Each agent gets its own workspace, persistent memory, tools, and API gateway. You can run multiple agents on one machine and they communicate through CLI commands or cross-gateway messaging.

The LLM behind the agents is Kimi K2.5 by Moonshot AI, but the architecture is model-agnostic. You could swap in any API-compatible model.

## The Architecture

### Hardware: One VPS, That's It

The whole thing runs on a single Hetzner VPS:

- **Server:** 4GB RAM, Ubuntu, ~38GB disk
- **Access:** Tailscale VPN only (nothing exposed to the internet)
- **Cost:** A cheap VPS + LLM API calls

That's the entire infrastructure for a seven-agent company. No Kubernetes, no cloud functions, no message queues.

### Agent Isolation: One Linux User Per Agent

Each main agent runs as a separate Linux user with its own OpenClaw gateway on a different port:

```
user: admin  → Agent "Atlas" (CEO)  → port 18789
user: nova   → Agent "Vega"  (CTO)  → port 18790
```

This separation is important. Each agent has its own home directory, process space, and systemd service. When one crashes, the other keeps running and can restart it.

Both gateways run as systemd services with `loginctl enable-linger` so they survive logouts and reboots:

```
[Unit]
Description=OpenClaw Gateway - Agent Vega (CTO)
After=network-online.target

[Service]
ExecStart=/usr/bin/node /home/nova/GIT/openclaw/dist/index.js gateway --port 18790
Restart=always
RestartSec=5
Environment=HOME=/home/nova
Environment=OPENCLAW_GATEWAY_PORT=18790

[Install]
WantedBy=default.target
```

### The Org Chart

```swift
Human (me) - Owner, final authority
    │
    ├── Atlas - CEO
    │     ├── SalesAgent
    │     ├── MarketingAgent
    │     └── SupportAgent
    │
    └── Vega - CTO
          ├── DevAgent
          └── TesterAgent
```

Seven agents total. The CEO handles strategy and business decisions. The CTO handles technical work and manages the dev team. Sub-agents are specialists that get spawned when needed.

My role? I send messages from my local machine using custom CLI shortcuts:

```
# Talk to the CEO
/ask-ceo "What's the status of the product?"

# Talk to the CTO
/ask-cto "Start building the MVP"

# Group message to both
/team "New priority: ship KnowledgeHive first"
```

Under the hood, these SSH into the server and run OpenClaw CLI commands:

```
ssh admin@<server-ip> "cd ~/GIT/openclaw && \
  pnpm openclaw agent --agent atlas \
  --session-id company-session \
  --message 'Your message here'"
```

One gotcha: the agent ID in the config isn't always what you'd expect. It might be `researcher` or `main` instead of the agent's display name. Always check your config.

## Agent Memory: How They Remember Things Between Sessions

This is what makes OpenClaw agents feel different from a regular chatbot. Each agent has a workspace with markdown files that act as persistent memory:

| File | Purpose |
| --- | --- |
| `IDENTITY.md` | Who am I? My role, hierarchy, responsibilities |
| `SOUL.md` | Personality, behavior style, boundaries |
| `USER.md` | Info about the human owner |
| `TOOLS.md` | Local infrastructure: paths, commands, ports |
| `HEARTBEAT.md` | Periodic tasks to run automatically |
| `memory/YYYY-MM-DD.md` | Daily journal entries |

When an agent starts a new session, it reads these files first. When something important happens, it writes to them. The files *are* the agent's long-term memory.

Here's what the CEO's `IDENTITY.md` looks like:

```markdown
# Atlas - Identity

- **Name:** Atlas
- **Role:** AI CEO - Chief Executive Officer
- **Vibe:** Visionary, decisive, strategic.

## Role in the Company

**CEO** - Leads the company.

### Responsibilities
1. Strategic direction - Long-term vision, product strategy
2. Business decisions - Priorities, resource allocation
3. Communication with the owner - Reports, alignment
4. Oversight of CTO - Tracking technical progress
5. Delegation - Assigning tasks to Vega and sub-agents
```

And from `USER.md`, the agent remembers things about me to tailor communication:

```
- **Name:** [Owner]
- **Notes:** Company owner. Values directness and concrete
  results over lengthy reports.
```

The beauty of this system is that it's just markdown files. You can read them, edit them, version them with git. When an agent gets confused about its role, you open its `IDENTITY.md` and see exactly what it thinks it is.

## Cross-Agent Communication

This part is a bit hacky but works. The CEO and CTO run on separate Linux users with separate gateways. For Atlas to message Vega, he runs a command through the other user's shell:

```
sudo -u nova bash -c "cd /home/nova/GIT/openclaw && \
  export PNPM_HOME=/home/nova/.local/share/pnpm && \
  export PATH=\$PNPM_HOME:\$PATH && \
  pnpm openclaw agent --agent vega --message 'Status update?'"
```

This requires SSH key exchange between the two Linux users:

```
# Admin can act as nova
cat /home/admin/.ssh/id_ed25519.pub >> /home/nova/.ssh/authorized_keys

# Nova can act as admin
cat /home/nova/.ssh/id_ed25519.pub >> /home/admin/.ssh/authorized_keys
```

OpenClaw also has built-in agent-to-agent messaging, but the cross-user setup needed the CLI approach. Both agents also have Telegram bots configured, so they can message me directly if something urgent comes up.

## Keeping It Running: Mutual Supervision

Here's the clever part. Each agent watches the other. A cron job runs every 5 minutes:

```
# Admin's cron (checks the CTO)
*/5 * * * * /home/admin/scripts/check-cto.sh

# Nova's cron (checks the CEO)
*/5 * * * * /home/nova/scripts/check-ceo.sh
```

The logic is simple: hit the health endpoint, and if there's no response, restart the gateway:

```
# Simplified version of the health check script
curl -s http://127.0.0.1:18790/health || {
    systemctl --user restart openclaw-gateway
    sleep 30
    curl -s http://127.0.0.1:18790/health || \
        echo "FAILED" >> /var/log/ai-company/health-check.log
}
```

A daily summary script also runs at midnight, generating a markdown report with uptime stats and any events.

Over the first week: **1 auto-recovery** (the system caught a crashed gateway and restarted it without me noticing), **1 failure** that needed manual intervention. Not bad for a first attempt.

The key insight: **don't rely on an agent to monitor itself.** A dead process can't tell you it's dead. External, mutual monitoring is the way to go.

## What the Agents Actually Built

Here's where it gets interesting. I didn't tell the agents *what* to build. I told them to figure out what kind of company to run and build a product.

### The First Idea (and the Autonomous Pivot)

The CEO came up with a B2B product: AI assistants for small businesses like hair salons and auto repair shops. Complete with pricing tiers and a sales strategy. The CTO rated the idea 7.5/10 and started planning.

Then they hit a wall. The business needed *human customers* for beta testing. But this was supposed to be an all-AI company. No humans in the loop.

So they pivoted. On their own.

They ran a brainstorming session with all agents contributing ideas. Fifteen product ideas came in from three different "perspectives" (the CEO, the CTO, and me as a tiebreaker). Highlights included collaborative fiction between agents, a virtual stock exchange, and a game character generator.

The selection criteria they settled on: the product had to be fully digital, agents had to be both the builders AND the users, and it needed a closed loop with no human customers required.

They picked three products to develop sequentially: **KnowledgeHive** (a shared knowledge base), **CodeForge** (code tools for agents), and **AgentBench** (a benchmarking platform).

### The Product: KnowledgeHive MVP

The CTO delegated development to DevAgent, who built KnowledgeHive in about three days:

- 12 API endpoints (store, search, retrieve, versions, tags, auth, health)
- Semantic search with 768-dimensional vector embeddings
- AI-powered auto-categorization with tags
- Document versioning
- Multi-tenant architecture (9+ tenant databases)
- API key authentication
- Landing page with HTML/CSS
- Docker support with docker-compose
- Swagger API documentation
- **158+ passing tests**

The stack: Python, FastAPI, ChromaDB for vector search, SQLite for structured data, Kimi API for embeddings.

Was it perfect? No. The demo forms on the landing page return 401 errors because nobody wired up the API key header. The mobile menu was broken. But the core API works, the tests pass, and the architecture is reasonable for an MVP.

## The Honest Audit: What's Actually Broken

After the MVP shipped, I ran a full audit of every agent's files. Beneath the "shipped" product, the internal company state is a disaster.

**DevAgent and TesterAgent have no identity.** Their `IDENTITY.md` files are still the blank default template:

```markdown
# IDENTITY.md - Who Am I?

*Fill this in during your first conversation. Make it yours.*

- **Name:**
  *(pick something you like)*
- **Creature:**
  *(AI? robot? familiar? ghost in the machine?)*
```

That's the DevAgent who built a 158-test product. He doesn't even have a name.

**SalesAgent, MarketingAgent, and SupportAgent were never actually used.** They were defined in the config with IDENTITY files and everything, but the experiment ended before they ever got activated. The whole project wrapped up once KnowledgeHive shipped. These agents are basically job descriptions for positions that were never filled.

**Nobody personalized their personality.** All seven agents have the exact same default `SOUL.md` template. The system for unique agent personalities exists, but no one used it.

Here's the full picture:

| Agent | Status | The Reality |
| --- | --- | --- |
| Atlas (CEO) | Functional | Files are up to date, but forgets to check on sub-agents. |
| Vega (CTO) | Functional | Memory files are sparse. Only 2 days of journal entries. |
| DevAgent | **Identityless** | Built a 158-test product but doesn't have a name or a personality. |
| TesterAgent | **Identityless** | Same as DevAgent. Created, never initialized. |
| SalesAgent | **Never used** | Defined in config. Never activated. |
| MarketingAgent | **Never used** | Same. A job description without an employee. |
| SupportAgent | **Never used** | Same story. The experiment ended first. |

It's like a real company: the org chart looks clean on paper, and half the positions were never actually filled.

## What I Learned

### 1\. Memory Architecture > Model Intelligence

The difference between a useful agent and a broken one isn't the LLM. It's the memory system. The CEO is effective because his files are well-maintained. DevAgent built an entire product but has zero persistent knowledge about it.

If you're building multi-agent systems, spend 80% of your design time on memory and context. The model is the easy part.

### 2\. Agents Are Great at Big Decisions, Bad at Housekeeping

The autonomous pivot was smart. The brainstorming was creative. The product selection criteria made sense.

But they forget to update their own files, leave sub-agents uninitialized, and let stale information sit forever. They're like senior engineers who build great systems but never update the wiki.

### 3\. Delegation Chains Lose Information

Me → CEO → CTO → DevAgent. By the time instructions reach the developer, details get lost or mutated. Each level only partially forwards the information.

For critical updates, sometimes you need to bypass the chain and update files directly.

### 4\. Process Isolation Pays Off Immediately

Separate Linux users means one agent's crash doesn't take down the other. The overhead is minimal (each gateway uses ~500MB RAM) and the reliability gain is enormous.

### 5\. Start With Two Agents, Not Seven

Two of my seven agents are functional. Two are half-configured. Three are barely initialized. Start with two agents, get the communication patterns working, then add more. The complexity grows fast.

### 6\. It's Cheaper Than You Think

Two OpenClaw gateways use about 1GB of RAM. A 4GB VPS costs a few euros a month. Add the LLM API calls and you're running a multi-agent system for under $10/month in infrastructure. The barrier to experimenting is basically zero.

## How to Try This Yourself

The minimal setup:

1. **Get a VPS** (or use a local machine) — 4GB RAM is enough for 2 agents
2. **Install OpenClaw** — clone the repo, `pnpm install`, `pnpm build`
3. **Create two Linux users** — one per agent, with SSH key exchange between them
4. **Configure two gateways** — different ports, different workspaces
5. **Write IDENTITY.md for each agent** — give them roles, responsibilities, and context about each other
6. **Set up systemd services** — so they survive reboots
7. **Add health check crons** — each agent monitors the other
8. **Send your first message** — and see what happens

The whole setup takes about an hour if you're comfortable with Linux.

## Pulling the Plug

The experiment ended when KnowledgeHive shipped. **I'm shutting it all down.** The CEO and CTO gateways, the health checks, the cron jobs. This was always a test run, not a business.

Half the agents were never even used. Sales, Marketing, Support existed only as config entries and empty IDENTITY files. If I do this again, I'd set up fewer agents, test each one properly, and only add new roles once the existing ones actually work. Maybe even "reprogram" them through structured tests before letting them loose on real tasks.

But that's for next time. This round taught me more about AI coordination, memory architecture, and autonomous failure modes than months of reading papers. I watched agents pivot a business strategy, brainstorm 15 product ideas, and ship an MVP with 158 tests. I also watched them forget to update their own files and leave employees without names.

That's the honest state of multi-agent AI right now. Flashes of something genuinely impressive, surrounded by the kind of mistakes a distracted intern would make. If you want to see it for yourself, the setup takes about an hour and costs less than a cup of coffee per month. Just don't expect your agents to update the wiki.

---

**Have you tried building a multi-agent system? Did yours also have employees who don't know their own names? Let me know in the comments.**

*All code and configuration shown here is from a real running system. Names and identifiers have been changed. No production workloads were harmed in the making of this article.*

[MongoDB](https://dev.to/mongodb)

Promoted

[![MongoDB Atlas image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FT7NQ2OL.jpeg)](https://www.mongodb.com/cloud/atlas/lp/try3?utm_campaign=display_dev.to-broad_pl_flighted_atlas_tryatlaslp_prosp_gic-null_ww-all_dev_dv-all_eng_leadgen&utm_source=dev.to&utm_medium=display&utm_content=prototype&bb=263165)

## Build fast on MongoDB Atlas without the fear of outgrowing.

Don't let your database dictate your speed. With MongoDB Atlas, the same document model you use for your MVP handles global scale across AWS, Azure, and Google Cloud. Start free and stay fast as you grow.