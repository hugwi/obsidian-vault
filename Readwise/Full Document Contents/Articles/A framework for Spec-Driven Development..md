# A framework for Spec-Driven Development.

![rw-book-cover](https://sdd-pilot.szaszattila.com/og-image.png?v=2)

## Metadata
- Author: [[SDD Pilot]]
- Full Title: A framework for Spec-Driven Development.
- Category: #articles
- Summary: Spec-Driven Development (SDD) is a workflow that starts with clear product vision and feature specifications, then moves through structured planning, tasking, and quality control. It uses AI tools and shared skills to enforce consistency, traceability, and quality at every step of feature delivery. This framework supports multiple AI coding tools with a unified, tool-agnostic core to streamline project governance and implementation.
- URL: https://sdd-pilot.szaszattila.com/

## Full Document
Enhance your AI coding tool with optional project bootstrap and a structured, spec-driven feature-delivery workflow. Define your product vision, create reusable system design context when needed, then move from specification to QC with quality built in, not bolted on.

#### Built for Structured Delivery

Projects can optionally bootstrap shared product vision and technical context first. Then every feature moves through enforced phases with dedicated agents, structured artifacts, and quality gates.

Define your product vision with `/sddp-prd`, establish a reusable technical baseline with `/sddp-systemdesign`, then enter a strict gated lifecycle. You still can't plan without a spec or implement without tasks.

Each phase has a dedicated persona — Product Strategist, Solution Architect, Product Manager, Software Architect, QA Engineer, QC Agent, Project Manager — plus sub-agents for delegation.

Tasks link to functional requirements (`{FR-###}`) and user stories (`[US#]`). Nothing gets lost between spec and code.

"Unit Tests for English" — checklists that test *requirements quality*, not code behavior. Auto-evaluated with PASS / RESOLVE / ASK outcomes.

Shared, tool-agnostic skill files power GitHub Copilot, Claude Code, Windsurf, Antigravity, and OpenCode through thin wrapper layers.

Cross-artifact consistency checks: spec vs. plan alignment, plan vs. tasks alignment, project instructions compliance — up to 50 findings with severity levels.

A dedicated Technical Researcher agent fetches best practices, official docs, and industry standards from the web — then distills findings into a concise `research.md` so your plan is evidence-backed.

Run the entire feature-delivery pipeline with `/sddp-autopilot`. Bootstrap stays explicit, while downstream phases auto-resolve decisions and record every choice.

Projects can optionally bootstrap shared product and architecture context before the strict feature-delivery lifecycle begins. Each feature phase still produces structured artifacts and must pass quality gates.

%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#BB86FC', 'primaryTextColor': '#121212', 'primaryBorderColor': '#985EFF', 'lineColor': '#6A6A6A', 'secondaryColor': '#1E1E1E', 'tertiaryColor': '#03DAC6', 'background': '#1E1E1E', 'mainBkg': '#1E1E1E', 'nodeBorder': '#333', 'clusterBkg': '#121212', 'titleColor': '#E0E0E0', 'edgeLabelBackground': '#1E1E1E' }}}%% graph TD B(("Start")) -.-> PRD["/sddp-prd  

Product Strategist"] B -.-> SA["/sddp-systemdesign  

Solution Architect"] PRD -.-> SA SA -.-> DO["/sddp-devops  

DevOps Strategist"] DO -.-> PP["/sddp-projectplan  

Project Planner"] B --> Init["/sddp-init  

Project Initializer"] PP -.-> Init style B fill:#5D4037,stroke:#8D6E63,color:#fff style PRD fill:#6D4C41,stroke:#A1887F,color:#fff style SA fill:#5D4037,stroke:#8D6E63,color:#fff style DO fill:#FF8F00,stroke:#FFCA28,color:#fff style PP fill:#0277BD,stroke:#40C4FF,color:#fff style Init fill:#7C4DFF,stroke:#BB86FC,color:#fff

%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#BB86FC', 'primaryTextColor': '#121212', 'primaryBorderColor': '#985EFF', 'lineColor': '#6A6A6A', 'secondaryColor': '#1E1E1E', 'tertiaryColor': '#03DAC6', 'background': '#1E1E1E', 'mainBkg': '#1E1E1E', 'nodeBorder': '#333', 'clusterBkg': '#121212', 'titleColor': '#E0E0E0', 'edgeLabelBackground': '#1E1E1E' }}}%% graph TD S["/sddp-specify  

Product Manager"] --> C["/sddp-clarify  

Business Analyst"] S --> P["/sddp-plan  

Software Architect"] C --> P P --> K["/sddp-checklist  

QA Engineer"] P --> T["/sddp-tasks  

Project Manager"] K --> T T --> A["/sddp-analyze  

Compliance Auditor"] A --> I["/sddp-implement  

Software Engineer"] I --> QC["/sddp-qc  

QC Agent"] QC -->|PASS| Release["Release Ready"] QC -->|FAIL| I T -.->|optional| Loop["/sddp-implement-qc-loop"] Loop --> Release S -.->|unattended| AP["/sddp-autopilot"] AP --> Release style S fill:#448AFF,stroke:#82B1FF,color:#fff style C fill:#FF6E40,stroke:#FFAB91,color:#fff style P fill:#00897B,stroke:#03DAC6,color:#fff style K fill:#8E24AA,stroke:#CE93D8,color:#fff style T fill:#E53935,stroke:#CF6679,color:#fff style A fill:#0288D1,stroke:#80D8FF,color:#fff style I fill:#37474F,stroke:#B0BEC5,color:#fff style QC fill:#2E7D32,stroke:#69F0AE,color:#fff style Release fill:#00C853,stroke:#69F0AE,color:#121212 style Loop fill:#5C6BC0,stroke:#7986CB,color:#fff style AP fill:#00695C,stroke:#03DAC6,color:#fff

Product Strategist creates or refines `docs/prd.md` as the canonical Product Requirements Document and registers it in `.github/sddp-config.md`.

Project Manager agent decomposes spec + plan into dependency-ordered `tasks.md`. Each task is atomic, testable, and traceable to requirements.

QC Agent runs tests, static analysis, security audits, and story verification. Failures loop back as `[BUG]` tasks. Pass creates a `.qc-passed` marker.

#### Structured Artifacts,Full Traceability

Project bootstrap writes shared artifacts outside feature folders. Feature delivery then produces a complete set of traceable documents per feature, from requirements through QC.

```
docs/
├── prd.md              # Canonical product requirements
├── sad.md              # Canonical technical context
├── dod.md              # Canonical deployment & operations
└── project-plan.md     # Canonical project implementation plan
project-instructions.md # Project governance
.github/
└── sddp-config.md      # Shared document registration + autopilot settings

specs/00001-user-auth/
├── spec.md             # Feature specification
├── plan.md             # Implementation plan
├── tasks.md            # Phased task list
├── research.md         # Technology research
├── data-model.md       # Entity definitions
├── quickstart.md       # Integration guide
├── contracts/          # API contracts
│   └── auth-api.md
├── checklists/         # Quality checklists
│   ├── spec-quality.md
│   └── plan-quality.md
├── .completed          # Implementation done marker
├── autopilot-log.md    # Autopilot audit log
└── .qc-passed          # QC gate passed marker
```

Up and running in under 5 minutes. Bootstrap shared technical context when you need it, then start feature delivery with the same command sequence across supported tools.

Use the GitHub template or download the release for your AI tool.

Start feature delivery with a natural-language description, then remove ambiguity before planning.

7

##### Plan, task, and implement

Walk through the remaining phases. Each command produces structured artifacts and enforces quality gates.

```
# Design the technical approach
/sddp-plan

# Generate quality checklists (optional but recommended)
/sddp-checklist

# Decompose into dependency-ordered tasks
/sddp-tasks

# Run compliance analysis (optional but recommended)
/sddp-analyze

# Execute implementation — fully resumable
/sddp-implement

# Run quality control — tests, security, story verification
/sddp-qc

# Or loop implement + QC automatically (max 10 cycles)
/sddp-implement-qc-loop
```

**Autopilot alternative:** Run `/sddp-autopilot Build user auth` to execute the feature-delivery pipeline unattended. Bootstrap remains explicit.

| Command | Agent | Produces | Requires |
| --- | --- | --- | --- |
| /sddp-prd | Product Strategist | docs/prd.md | Product ideas / attached docs |
| /sddp-systemdesign | Solution Architect | docs/sad.md | Repo context / attached docs |
| /sddp-devops | DevOps Strategist | `docs/dod.md` | — | Deployment & operations plan |
| /sddp-projectplan | Project Planner | `docs/project-plan.md` | — | Epic decomposition & sequence |
| /sddp-init | Project Initializer | project-instructions.md | PRD / governance principles |
| /sddp-specify | Product Manager | spec.md | Feature description |
| /sddp-clarify | Business Analyst | Updated spec.md | spec.md |
| /sddp-plan | Software Architect | plan.md, research.md | spec.md |
| /sddp-checklist | QA Engineer | checklists/\*.md | spec.md + plan.md |
| /sddp-tasks | Project Manager | tasks.md | spec.md + plan.md |
| /sddp-analyze | Compliance Auditor | Markdown report | spec + plan + tasks |
| /sddp-implement | Software Engineer | Source code | spec + plan + tasks |
| /sddp-qc | QC Agent | .qc-passed / [BUG] tasks | .completed + spec + tasks |
| /sddp-implement-qc-loop | Software Engineer (looping) | Source code + .qc-passed | spec + plan + tasks |
| /sddp-autopilot | Pipeline Orchestrator | All artifacts + autopilot-log.md | Autopilot enabled + Product Document + Technical Context Document |

#### Multi-Tool Wrapper Architecture

%%{init: {'theme': 'dark', 'themeVariables': { 'primaryColor': '#BB86FC', 'primaryTextColor': '#121212', 'primaryBorderColor': '#985EFF', 'lineColor': '#6A6A6A', 'secondaryColor': '#1E1E1E', 'tertiaryColor': '#03DAC6', 'background': '#1E1E1E', 'mainBkg': '#1E1E1E', 'nodeBorder': '#333', 'clusterBkg': '#1A1A1A', 'titleColor': '#E0E0E0', 'edgeLabelBackground': '#1E1E1E' }}}%% graph TB subgraph Tools["AI Coding Tools"] CP["GitHub Copilot  

.github/prompts/"] CC["Claude Code  

.claude/agents/ + skills/"] WS["Windsurf  

.windsurf/workflows/"] AG["Antigravity  

.agents/workflows/"] OC["OpenCode  

.opencode/commands/"] end subgraph Core["Shared Skill Engine"] SK[".github/skills/  

System Design • Methodology  

Spec Authoring • Plan Authoring  

Task Generation • Quality Control"] AG2[".github/agents/  

Sub-agent definitions"] IN[".github/instructions/  

Governance rules"] end CP --> SK CC --> SK WS --> SK AG --> SK OC --> SK SK --> AG2 SK --> IN style CP fill:#7C4DFF,stroke:#BB86FC,color:#fff style CC fill:#D4A054,stroke:#FFD180,color:#121212 style WS fill:#0288D1,stroke:#80D8FF,color:#fff style AG fill:#E53935,stroke:#CF6679,color:#fff style OC fill:#00897B,stroke:#03DAC6,color:#fff style SK fill:#2E7D32,stroke:#69F0AE,color:#fff style AG2 fill:#37474F,stroke:#B0BEC5,color:#fff style IN fill:#37474F,stroke:#B0BEC5,color:#fff

All methodology logic lives in `.github/skills/` — tool-agnostic Markdown files that define how each SDD phase works. Write once, run everywhere.

Each AI tool gets a minimal wrapper in its native format — Copilot prompts, Antigravity workflows, Claude agents, Windsurf workflows, and OpenCode commands — that delegates to the shared skills.

```
sdd-pilot/
      ├── .github/                    # Shared core (all tools read from here)
      │   ├── skills/                 # Shared skills, including system-design
      │   ├── agents/                 # Sub-agent definitions + Copilot agents
      │   ├── instructions/           # Governance rules
      │   ├── prompts/                # Copilot prompt wrappers
      │   └── sddp-config.md          # Product / technical context registration
      │
      ├── docs/
      │   ├── prd.md                  # Canonical product requirements document
      │   └── sad.md                  # Canonical technical context document
      ├── .agents/workflows/          # Antigravity workflow wrappers
      ├── .windsurf/workflows/        # Windsurf workflow wrappers
      ├── .claude/agents/ + skills/   # Claude Code agent + skill wrappers
      ├── .opencode/agents/ + cmds/   # OpenCode agent + command wrappers
      │
      ├── project-instructions.md     # Project governance (shared)
      └── AGENTS.md                   # Agent conventions (shared)
```
