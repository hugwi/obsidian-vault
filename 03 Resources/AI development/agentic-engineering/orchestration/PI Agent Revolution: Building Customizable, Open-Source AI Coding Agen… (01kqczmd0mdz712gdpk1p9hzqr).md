---
title: "PI Agent Revolution: Building Customizable, Open-Source AI Coding Agents That"
source: "https://atalupadhyay.wordpress.com/2026/02/24/pi-agent-revolution-building-customizable-open-source-ai-coding-agents-that-outperform-claude-code/"
author: "atal upadhyay"
published: 2026-02-24
created: 2026-04-29
description: "Introduction: Why Your Tools Are Limiting Your Potential Hey there, fellow"
tags:
  - to-process
  - orchestration
---

Hey there, fellow engineer.


If you’ve been building software in the last year, you’ve felt it. That subtle but persistent frustration when your AI coding assistant—no matter how powerful—just doesn’t quite do what you need it to do. Maybe it’s too opinionated. Maybe it won’t let you use your preferred model. Maybe it abstracts away the very details you need to control to solve your specific problem.


You’re not imagining things. And you’re not alone.


Every single engineer is limited by the tools they use. The tools you reach for shape what you believe is possible. They define your workflow, your mental model, and ultimately, the ceiling of what you can build.


So let me ask you a question that might feel uncomfortable:


**When was the last time you asked yourself: “How is my agentic coding tool limiting me?”**


If you want to expand beyond what everyone else is doing—if you want to break through the current limits of AI-assisted development—you’ve clicked on the right guide.


Because today, we’re going deep on something that’s quietly reshaping the agent coding landscape: **PI Agent**.


This isn’t just another tutorial. This is a comprehensive masterclass that will take you from absolute beginner to advanced practitioner in building customizable, open-source AI coding agents. We’ll cover:


**Conceptual foundations**: What makes an “agent harness” and why it matters more than the model  

**Tool comparison**: Claude Code vs. PI Agent—philosophy, capabilities, and trade-offs  

**Four hands-on labs**: From basic setup to meta-agent orchestration  

**Customization deep-dive**: Extensions, hooks, widgets, themes, and system prompts  

**Production considerations**: Security, scalability, and enterprise readiness  

**Strategic guidance**: When to use which tool, and how to hedge your bets  

**Interview prep**: Questions to test and demonstrate your agent engineering expertise


Whether you’re a junior developer curious about AI agents, a mid-level engineer evaluating tools for your team, or a senior technical leader responsible for production systems, this guide is structured to grow with you.


Grab your favorite beverage, open your terminal, and let’s build the future of agentic engineering—together.


## Part 1: Conceptual Foundations – Understanding the Agent Harness


Before we dive into specific tools, let’s establish a shared understanding of what we’re actually building when we create an “AI coding agent.”


### 1.1 What Is an Agent Harness, Really?


When most people think about AI coding tools, they focus on the **model**: Claude 3.5 Sonnet, GPT-4, Gemini, etc. And yes, the model matters. But there’s a deeper layer that determines what your agent can actually *do*:



>  **The agent harness is the framework that connects the model to tools, manages conversation state, handles tool execution, and orchestrates the reasoning loop.**
> 
>  


Think of it like this:


**Key Insight:** Two agents using the exact same model can behave completely differently based on their harness design. The harness determines:


* What tools the agent can access
* How it reasons about when to use them
* What information it sees about its own actions
* How it handles errors and recovery
* What the user experiences while interacting with it


### 1.2 The Four Pillars of Agent Design


Every agent harness makes foundational decisions across four dimensions:




| Pillar | Key Questions | Impact on User Experience |
| --- | --- | --- |
| **Philosophy** | Should the tool be opinionated or minimal? Should safety be enforced or delegated? | Determines how much control the user has vs. how much guidance they receive |
| **Observability** | What does the user see about the agent’s reasoning? How transparent is the tool execution? | Affects debugging, trust-building, and learning the system |
| **Extensibility** | Can users add custom tools, modify prompts, or change UI behavior? | Determines whether the tool can adapt to specialized workflows |
| **Model Agnosticism** | Is the harness tied to specific providers, or can it work with any model? | Affects cost, flexibility, and future-proofing |


### 1.3 Why “Minimal” Can Be Powerful


One of the most counterintuitive ideas in PI Agent’s design is this:



>  **If I don’t need it, it won’t be built.**
> 
>  


This philosophy stands in stark contrast to tools that ship with dozens of built-in features, modes, and safety guards. Instead, PI Agent starts with just four core tools:


* `read` – Read file contents
* `write` – Write new files
* `edit` – Modify existing files
* `bash` – Execute shell commands


And a ~200 token system prompt that essentially says: “You’re a helpful coding assistant. Use these tools to help the user.”


**Why does minimalism work?**


1. **Reduced cognitive load**: Fewer built-in features means less to learn upfront
2. **Clearer mental model**: You understand exactly what the agent can do
3. **Maximum flexibility**: Nothing is “baked in” that you can’t change
4. **Faster iteration**: Adding a feature you actually need is easier than removing one you don’t


**The trade-off**: You need to know what you’re doing. PI Agent doesn’t hold your hand. It assumes you’re an engineer who understands the implications of giving an AI agent access to your filesystem.


### 1.4 The Customization Spectrum


One of PI Agent’s most powerful concepts is **composable extensions**. Instead of a monolithic application with configuration flags, PI Agent lets you build your agent experience by stacking modular extensions.


**The magic**: Each extension is a self-contained TypeScript module that hooks into the agent lifecycle. You can mix, match, and stack them to create an agent experience tailored to your exact workflow.


**Human Insight**: Think of extensions like LEGO bricks. The base agent is the foundation plate. Each extension is a specialized brick. You build the agent you need, not the agent someone else decided you should have.


## Part 2: Claude Code vs. PI Agent – A Detailed Comparison


Now that we understand the conceptual foundations, let’s compare the two tools head-to-head. This isn’t about declaring a “winner”—it’s about understanding trade-offs so you can choose the right tool for your specific needs.


### 2.1 Design Philosophy: Opinionated vs. Minimal


#### Claude Code: Great Out-of-the-Box Defaults


Claude Code is designed for **broad accessibility**. When you open it:


**Low floor**: Anyone—engineer, PM, designer, “vibe coder”—can start getting value immediately  

**Built-in safety**: Five confirmation modes, permission gates, and guardrails  

**Opinionated system prompt**: ~10,000 tokens of best practices, patterns, and constraints baked in  

**Polished UX**: Clean terminal UI, intuitive commands, helpful status indicators  

**Enterprise-ready**: SOC 2 compliance, audit logging, team management features


**The philosophy**: “We’ve figured out what works for most people. Start here, and customize within the boundaries we’ve defined.”


#### PI Agent: Minimal Core, Maximum Control


PI Agent is designed for **advanced engineers who want control**. When you open it:


**Minimal system prompt**: ~200 tokens that let the model “cook” without excessive constraints  

**YOLO mode by default**: Full filesystem access unless you build restrictions yourself  

**Transparent internals**: Everything is exposed; nothing is hidden behind abstraction  

**Model agnostic**: Use any provider—Claude, GPT, Gemini, open-source, local models  

**Extension-based customization**: Build your agent experience from composable modules


**The philosophy**: “You know what you’re doing. We provide the harness; you build the agent you need.”


### 2.2 Side-by-Side Feature Comparison




| Feature | Claude Code | PI Agent | Why It Matters |
| --- | --- | --- | --- |
| **Source Model** | Closed source | Open source (MIT) | Open source = auditability, forkability, no vendor lock-in |
| **System Prompt** | ~10k tokens, opinionated | ~200 tokens, minimal | More prompt control = more behavioral control |
| **Default Tools** | 8+ built-in tools | 4 core tools + custom | Fewer defaults = less bloat, more intentional customization |
| **Safety Modes** | 5 confirmation modes | None by default (build your own) | Safety vs. speed trade-off; advanced users may prefer control |
| **Observability** | Abstracted; requires digging | Fully exposed; everything visible | Transparency aids debugging and learning |
| **Model Support** | Anthropic models prioritized | Any model via API or local | Flexibility for cost, performance, or privacy needs |
| **Customization** | Config files, limited hooks | Full TypeScript extensions, 25+ hooks | Depth of customization determines specialization potential |
| **Sub-Agent Support** | Native via `task` tool | Build your own via extensions | Native = easier; custom = more flexible |
| **Multi-Agent Orchestration** | Built-in agent teams | Build your own via extensions | Same trade-off: convenience vs. control |
| **Programmatic Mode** | Bash + SDK | Bash + TypeScript SDK | SDK quality affects out-of-loop automation potential |
| **Enterprise Features** | SOC 2, audit logs, SSO | Experimental; build your own | Critical for regulated industries |
| **Version Pinning** | Limited | Full (it’s open source) | Stability for production deployments |


### 2.3 The “Cancer of Success” Problem


One of the most insightful observations from the knowledge base is this:



>  *“Successful products must grow to meet new profit motives. Remember, this is a for-profit tool. That means doing things that maximize profit over user satisfaction.”*
> 
>  


This isn’t a criticism of Anthropic—it’s a fundamental reality of software businesses. As Claude Code grows:


**It must serve broader audiences**: Features that help beginners may frustrate advanced users  

**It must maximize revenue**: Incentivizing use of Anthropic models over competitors  

**It must reduce support burden**: Opinionated defaults reduce edge cases but limit flexibility  

**It must move fast**: Breaking changes happen; you can’t always pin to a stable version


**The result**: A tool that’s excellent for 80% of use cases but increasingly frustrating for the 20% of users who need specialized workflows.


**PI Agent’s counter-strategy**: Stay minimal, stay open, stay composable. Let the community build the features they need, when they need them.


### 2.4 When to Use Which Tool: A Decision Framework


Instead of asking “Which tool is better?”, ask “Which tool is better *for my specific situation*?”


####  Use Claude Code When:


* You’re new to agent coding and want a gentle on-ramp
* You need enterprise compliance (SOC 2, audit logs, SSO)
* You want polished UX with minimal configuration
* Your team needs consistency and guardrails
* You’re okay with Anthropic’s model ecosystem


####  Use PI Agent When:


* You’re an advanced engineer who wants full control
* You need to use non-Anthropic models (cost, privacy, performance)
* You want to build specialized agents for niche workflows
* You need to pin versions for production stability
* You’re comfortable building your own safety guards and extensions


####  Use Both (The Hedge Strategy):


* **80% Claude Code**: For standard tasks, team collaboration, enterprise workflows
* **20% PI Agent**: For experimental projects, specialized agents, model flexibility, deep customization


**Key Principle**: Tools aren’t religions. Use the right tool for the job. And remember: you can always migrate workflows between tools as your needs evolve.


## Part 3: Hands-On Lab 1 – Getting Started with PI Agent (Beginner)


Now let’s get hands-on. This first lab assumes no prior experience with PI Agent. We’ll install it, run a basic session, and understand the core workflow.


### 3.1 Prerequisites


Before we begin, ensure you have:


### 3.2 Step 1: Install PI Agent


PI Agent is distributed via npm. Installation is straightforward:


**Alternative: Install from source** (if you want to modify the core):



```
git clone https://github.com/mariozhan/pi-agent.git
```

### 3.3 Step 2: Configure Your Environment


PI Agent uses environment variables for configuration. Create a `.env` file in your project directory:



```
PI_MODEL=claude-sonnet-4  
ANTHROPIC_API_KEY=sk-ant-...  
# PI_MODEL=gpt-4-turbo  
# OPENAI_API_KEY=sk-...  
# PI_MODEL=gemini-1.5-pro  
# GOOGLE_API_KEY=...  
# PI_MODEL=ollama/llama3.1  
# OLLAMA_BASE_URL=http://localhost:11434
```

**Security Note**: Never commit `.env` files to version control. Add to `.gitignore`:


### 3.4 Step 3: Run Your First PI Agent Session


Start a basic session:


You should see a terminal interface like this:



```
│ PI Agent v1.0.0                     │
```

**Key UI Elements**:


* **Header**: Shows agent version, model, and context usage
* **Prompt**: Where you type commands and questions
* **Thinking indicator**: Shows when the agent is reasoning
* **Status line (footer)**: Displays real-time information (customizable)


### 3.5 Step 4: Basic Interaction


Try these commands to understand the workflow:


**Observation Exercise**: Watch how the agent:


1. **Thinks**: You’ll see its reasoning steps in real-time
2. **Acts**: Tool calls are displayed before execution
3. **Observes**: Results are shown and incorporated into context
4. **Responds**: Final answer synthesizes the workflow


### 3.6 Step 5: Built-in Commands


PI Agent includes slash commands for common operations:


**Try This**: Type `/tools` to see the minimal toolset:


**Compare to Claude Code**: Claude Code ships with 8+ tools including web search, code execution sandbox, and more. PI Agent’s minimalism is intentional—you add only what you need.


### 3.7 Step 6: Understanding the Agent Loop


Every PI Agent interaction follows this cycle:


**Key Insight**: The harness manages this loop. The model just decides *what* to do; the harness decides *how* to do it.


### 3.8 Lab 1 Reflection: What You’ve Learned


**Installation and setup**: You can now install and configure PI Agent  

**Basic workflow**: You understand the agent loop and UI elements  

**Tool awareness**: You know the four core tools and how to invoke them  

**Command familiarity**: You can use built-in slash commands


**What’s Next**: Customization! The base agent is minimal by design. The real power comes from extensions.


**Beginner Challenge**: Before moving to Lab 2, try this:


1. Create a simple TypeScript project with PI Agent
2. Ask it to add a new feature (e.g., a utility function)
3. Observe how it uses the four core tools
4. Note any limitations you encounter


## Part 4: Hands-On Lab 2 – Customizing Your Agent with Extensions (Intermediate)


Now that you understand the basics, let’s unlock PI Agent’s superpower: **composable extensions**. This lab will teach you how to customize your agent’s behavior, UI, and capabilities.


### 4.1 Understanding Extensions


An extension in PI Agent is a TypeScript module that:


* Hooks into the agent lifecycle (input, tool call, output, etc.)
* Registers new commands, tools, or UI components
* Modifies the system prompt or agent behavior
* Adds custom widgets or footer elements


**Extension Anatomy**:



```
        handler: async (args: string[]) => { /* ... */ }  
        handler: async (params: any) => { /* ... */ }
```

### 4.2 Step 1: Enable Your First Extension – Pure Focus


Let’s start with a simple extension that minimizes UI distractions.


**Goal**: Create a “flow state” mode with no header, no footer, just you and the agent.


**What you’ll see**:



```
> _
```

That’s it. No header. No footer. No context display. Just the prompt.


**Why this matters**: For focused coding sessions, extra UI elements can be distracting. This extension strips everything away.


**Behind the scenes**: The extension hooks into the UI rendering lifecycle and returns minimal output.


### 4.3 Step 2: Stack Extensions – Context Footer


Now let’s add useful information back—but on our terms.


**What you’ll see**:



```
claude-sonnet-4 | Context: 12.4k/200k
```

**Customization**: The footer shows:


* Current model name
* Token usage (used / total)
* (Optional) Project name and Git branch


**Try This**: Type a few commands and watch the context counter update in real-time.


### 4.4 Step 3: Load Custom Skills from Multiple Directories


One powerful extension lets you organize your skills (reusable prompts) across multiple locations.


**Configuration**: Create a `pi.config.ts` file:



```
      './skills/global',      // Team-wide skills
```

**Skill File Example** (`./skills/project/code-review.md`):


**Usage**:


### 4.5 Step 4: Add a Purpose Widget


Sometimes you lose track of your goal mid-session. A persistent purpose widget helps.


**How it works**:


1. On startup, the agent asks: “What is the purpose of this session?”
2. You respond: “Refactor the authentication module”
3. The purpose appears in a persistent UI widget
4. The purpose is appended to the system prompt for ongoing steering


**UI Example**:


**Behind the scenes**: The extension:


* Adds a UI widget that persists across messages
* Modifies the system prompt dynamically: `Current goal: ${purpose}`
* Provides a command to update the purpose mid-session


### 4.6 Step 5: Theme Cyclinder – Customize Your UI


PI Agent lets you define custom themes via extensions.


**Usage**: Press `Ctrl+X` to cycle through themes.


**Example Themes**:


**Why this matters**: Personalization isn’t just aesthetic. A comfortable UI reduces cognitive load and improves focus.


### 4.7 Step 6: Tool Counter – Track Agent Activity


Want to understand what your agent is actually doing? Add a tool counter.


**UI Example**:



```
│ Tools: 3 | read(1), edit(1), bash(1)│  
│ Tokens: In: 8.2k | Out: 3.1k        │
```

**Features**:


* Real-time count of tool calls by type
* Token usage breakdown (input/output)
* Optional: Cost estimation based on model pricing


**Use Case**: Debugging unexpected behavior. If your agent is calling `bash` 20 times for a simple task, you’ll see it immediately.


### 4.8 Step 7: Build Your First Custom Extension


Now let’s create a simple extension from scratch.


**Goal**: Add a `/ping` command that responds with “pong” and logs the interaction.



```
    context.logger.debug('User input received', { input: input.slice(0, 100) });
```

**In your PI session**:


**Key Takeaway**: Extensions are just TypeScript classes. If you can write TypeScript, you can extend PI Agent.


### 4.9 Lab 2 Reflection: The Power of Composition


**Extension basics**: You understand how extensions hook into the agent lifecycle  

**UI customization**: You can modify headers, footers, themes, and widgets  

**Skill management**: You can organize and load reusable prompts from multiple sources  

**Custom commands**: You can add new slash commands with custom logic


**What’s Next**: Multi-agent patterns! Extensions can do more than customize UI—they can orchestrate entire agent teams.


**Intermediate Challenge**: Before moving to Lab 3, try this:


1. Create a custom extension that adds a `/summary` command
2. The command should compress the last N messages into a bullet-point summary
3. Test it in a real coding session


## Part 5: Hands-On Lab 3 – Building Multi-Agent Orchestration (Advanced)


Now we’re entering advanced territory. This lab teaches you how to build **multi-agent systems** using PI Agent extensions—without native sub-agent support.


### 5.1 The Multi-Agent Pattern


Why would you want multiple agents?


### 5.2 Step 1: Sub-Agent Support Extension


Since PI Agent doesn’t have native sub-agent support, we build it.


**Usage**:


**Behind the scenes**: The extension:


1. Creates a new PI Agent instance with isolated context
2. Routes the sub-task to that instance
3. Captures output and displays it in a persistent widget
4. Allows the primary agent to incorporate results


### 5.3 Step 2: Agent Teams – YAML Configuration


For more complex workflows, define agent teams via configuration.


**Create `teams.yaml`**:


**Enable the agent-teams extension**:



```
pi -e agent-teams --config teams.yaml
```

**Usage**:


### 5.4 Step 3: Agent Chains (Pipelines)


Sometimes you want agents to work sequentially, not just in parallel.


**Create `chains.yaml`**:


**Enable the agent-chains extension**:



```
pi -e agent-chains --config chains.yaml
```

**Usage**:



```
 Step 1/3: scout-1 running...  
 Step 2/3: scout-2 running...  
 Step 3/3: scout-3 running...
```

**Key Insight**: Chains let you create “assembly lines” for complex tasks. Each agent focuses on one step, passing refined output to the next.


### 5.5 Step 4: Till-Done List – Task Management with Enforcement


One of the most powerful extensions enforces task completion.


**How it works**:


1. Agent must create a task list before executing certain actions
2. Each task has a status: `todo` → `in-progress` → `done`
3. Agent can’t mark a task `done` without evidence of completion
4. Primary agent enforces: “Work until the list is complete”


**Example Workflow**:


**Advanced Usage**: Multi-task workflows



```
│ ... (13 more)                       │
```

**Why this matters**: This extension adds **determinism** to agent behavior. Instead of hoping the agent remembers everything, you enforce a structured workflow.


### 5.6 Step 5: Damage Control – Blocking Dangerous Actions


With great power comes great responsibility. PI Agent runs in “YOLO mode” by default—full filesystem access.


**Enable the damage-control extension**:



```
pi -e damage-control
```

**What it does**:


* Blocks dangerous commands by default (`rm -rf`, `chmod 777`, etc.)
* Requires explicit confirmation for high-risk operations
* Logs all blocked attempts for audit
* Allows custom rules via configuration


**Configuration Example** (`damage-control.config.ts`):



```
    /rm\s+-rf/,           // Block recursive delete  
    /ls\s+/,            // Always allow directory listings
```

**Usage Example**:


**Key Principle**: Security isn’t about removing power—it’s about adding intentionality. The damage-control extension lets you define your own safety boundaries.


### 5.7 Step 6: System Prompt Selector – Become Any Agent


Sometimes you want your primary agent to temporarily adopt a different persona.


**Usage**:


**Behind the scenes**: The extension:


1. Maintains a library of system prompt templates
2. Swaps the active system prompt on command
3. Preserves conversation context across persona changes
4. Allows stacking personas (e.g., “security-auditor + docs-writer”)


### 5.8 Lab 3 Reflection: Orchestration Patterns


**Sub-agent support**: You can spawn child agents for parallel work  

**Agent teams**: You can define specialized agent groups via YAML  

**Agent chains**: You can create sequential pipelines for complex tasks  

**Task enforcement**: You can add determinism with till-done lists  

**Safety controls**: You can block dangerous actions with custom rules  

**Persona switching**: You can dynamically change agent behavior


**What’s Next**: Meta-agents! Agents that build and manage other agents.


**Advanced Challenge**: Before moving to Lab 4, try this:


1. Create a simple agent team for code review
2. Define three agents: finder (locates files), analyzer (checks for issues), reporter (formats feedback)
3. Test it on a real pull request


## Part 6: Hands-On Lab 4 – Meta-Agents and Agent Chains (Expert)


We’ve reached the frontier. This lab explores **meta-agents**: agents that build, manage, and orchestrate other agents.


### 6.1 The Meta-Agent Pattern


What if your agent could:


* Generate new agents based on task requirements?
* Compose specialized agents from reusable components?
* Self-improve by analyzing its own performance?


That’s the meta-agent pattern.


### 6.2 Step 1: Expert Agents – Domain-Specialized Components


Instead of one generalist agent, create a team of specialists.


**Create expert definitions** (`experts.yaml`):



```
    tools: [read, write, edit, bash]  
    tools: [read, write, edit, bash]
```

**Enable the meta-agent extension**:



```
pi -e meta-agent --experts experts.yaml
```

**Usage**:



```
  "system_prompt": "[Generated prompt...]",
```

### 6.3 Step 2: Agent Factory – Programmatic Agent Generation


Take meta-agents further with code-based agent generation.


**Create `agent-factory.ts`**:


**Usage in PI session**:


### 6.4 Step 3: Orchestrator Agent – The Conductor


The orchestrator doesn’t do the work—it manages the workers.


**Create `orchestrator-extension.ts`**:


**Usage**:


### 6.5 Step 4: Self-Improvement Loop – Learning from Feedback


The most advanced pattern: agents that improve themselves.


**Create `learning-extension.ts`**:


**Feedback Collection Strategies**:



```
  // • Accept the suggestion? (+1)  
  // • Abandon the session? (-2)
```

### 6.6 Step 5: Putting It All Together – A Self-Improving Meta-Agent System


Now let’s combine everything into a cohesive system.


**Project Structure**:



```
│   ├── security/             # Security-specific skills  
│   └── frontend/             # Frontend-specific skills
```

**Main Configuration** (`pi.config.ts`):



```
  experts: './config/experts.yaml',  
  teams: './config/teams.yaml',  
  chains: './config/chains.yaml',  
    blockedPatterns: [/rm\s+-rf/, /chmod\s+777/],
```

**Usage Example**:


### 6.7 Lab 4 Reflection: The Meta Frontier


**Expert agents**: You can create domain-specialized agent components  

**Agent factories**: You can generate agents programmatically from templates  

**Orchestrators**: You can build systems that delegate and synthesize  

**Self-improvement**: You can add feedback loops for continuous learning  

**System integration**: You can combine patterns into cohesive architectures


**What’s Next**: Production deployment! All this power needs responsible operation.


**Expert Challenge**: Before moving to production considerations, try this:


1. Build a simple meta-agent that can generate PI extensions
2. Give it a description of a desired feature
3. Have it output the TypeScript code for the extension
4. Test the generated extension in a real session


## Part 7: Production Considerations – Security, Scalability, and Enterprise Readiness


All this customization power is exciting—but how do you operate these systems responsibly in production?


### 7.1 Security: Beyond YOLO Mode


PI Agent’s default “YOLO mode” is great for experimentation but dangerous for production.


#### Essential Security Controls


**1. Principle of Least Privilege**



```
    allowedPaths: ['./src', './config', './docs'],  
    deniedPatterns: ['*.internal.corp', '10.0.0.0/8'],  
    denied: ['rm', 'curl', 'wget', 'eval'],
```

**2. Audit Logging**



```
      Object.entries(params).map(([k, v]) => 
```

**3. Immutable Audit Trail**


### 7.2 Scalability: From One Agent to Many


As your agent systems grow, you’ll need to scale.


#### Horizontal Scaling Pattern



```
│         (nginx, HAProxy)            │
```

**Kubernetes Deployment Example** (`agent-deployment.yaml`):



```
        image: my-registry/pi-agent:1.2.3
```

### 7.3 Enterprise Readiness: Bridging the Gap


PI Agent is open-source and experimental. Claude Code is enterprise-ready. How do you bridge that gap?


#### Hybrid Approach: PI for Innovation, Claude for Operations


#### Compliance Checklist for PI Agent in Production


### 7.4 Cost Management: Avoiding Surprise Bills


Agent systems can get expensive fast. Here’s how to control costs.



```
      'claude-sonnet-4': { input: 3.00, output: 15.00 }, // per 1M tokens  
      'gpt-4-turbo': { input: 10.00, output: 30.00 },  
    return (tokens.input * rates.input + tokens.output * rates.output) / 1_000_000;
```

#### Cost Optimization Strategies


1. **Model Tiering**: Use cheaper models for simple tasks



```
    model: claude-haiku  # $0.25/1M input, $1.25/1M output  
    model: claude-sonnet-4  # $3/1M input, $15/1M output
```

2. **Caching**: Avoid redundant model calls


3. **Context Management**: Keep prompts lean



```
        prompt.messages.slice(0, 10),  // Keep first 10
```

## Part 8: Strategic Guidance – When to Use Which Tool


Now that you understand both tools deeply, let’s talk strategy.


### 8.1 The Hedge Strategy: 80/20 Rule


Instead of betting everything on one tool, hedge your bets:


### 8.2 Decision Framework: Tool Selection Matrix


Use this matrix to choose the right tool for each task:




| Task Characteristic | Prefer Claude Code | Prefer PI Agent |
| --- | --- | --- |
| **Team Size** | Large team, need consistency | Small team or solo, need flexibility |
| **Compliance Needs** | Regulated industry, audit required | Internal tools, no compliance burden |
| **Model Preference** | Happy with Anthropic models | Need open-source, local, or multi-provider |
| **Customization Depth** | Basic prompts and skills sufficient | Need custom UI, tools, or orchestration |
| **Stability Requirements** | Need pinned versions, SLAs | Can tolerate bleeding-edge changes |
| **Budget Constraints** | Can afford Anthropic pricing | Need to optimize costs with model choice |
| **Innovation Pace** | Prefer stable, proven patterns | Want to experiment with novel agent designs |


### 8.3 Migration Strategy: Moving Between Tools


What if you start with one tool and need to switch?


#### Claude Code → PI Agent Migration



```
Phase 2: Skill Porting (Weeks 3-4)
```

#### PI Agent → Claude Code Migration


### 8.4 Future-Proofing: Preparing for What’s Next


The agent landscape evolves fast. Here’s how to stay adaptable:


#### Build Abstractions, Not Dependencies


#### Invest in Prompt Engineering Skills


Prompts are more portable than code. Skills you develop:


* Chain-of-thought prompting
* Few-shot example design
* Constraint specification
* Output formatting


These transfer between any LLM-based tool.


#### Monitor the Ecosystem


Stay informed about:


* New agent frameworks (AutoGen, CrewAI, LangGraph)
* Model advancements (open-source closing the gap)
* Security best practices (emerging standards)
* Enterprise requirements (compliance evolution)


#### Contribute Back


If you build useful extensions for PI Agent:


* Open-source them for the community
* Document patterns that others can reuse
* Share lessons learned from production use


This builds your reputation and improves the ecosystem for everyone.


## Part 9: Interview Questions – Agent Engineering Expertise


###  Beginner Level (Conceptual)


**Q1: What’s the difference between a model and an agent harness?**



```
"The model is the LLM that generates text—the 'brain.' The harness is the framework that connects the model to tools, manages conversation state, handles tool execution, and orchestrates the reasoning loop—the 'body and nervous system.' Two agents using the same model can behave completely differently based on their harness design."
```

**Q2: Why might a minimal agent harness be preferable to an opinionated one?**



```
"Minimal harnesses offer maximum flexibility. With fewer baked-in assumptions, advanced users can customize behavior precisely for their needs. They also reduce cognitive load—users understand exactly what the agent can do. The trade-off is that minimal harnesses require more expertise to use effectively."
```

**Q3: What does ‘model agnostic’ mean for an agent tool, and why does it matter?**



```
"Model agnostic means the harness can work with any LLM provider—Anthropic, OpenAI, Google, open-source, or local models. This matters for: cost optimization (choose cheaper models for simple tasks), privacy (use local models for sensitive data), performance (pick the best model for each task), and future-proofing (avoid vendor lock-in)."
```

###  Intermediate Level (Implementation)


**Q4: How would you add a custom tool to PI Agent that calls an external API?**


**Q5: Your agent is stuck in a reasoning loop. How do you debug and fix this?**



```
For PI Agent specifically: Check extension hooks for unintended side effects, verify system prompt isn't conflicting with tool behavior."
```

**Q6: How do you implement task enforcement like the ’till-done’ pattern?**



```
  private tasks: Task[] = [];
```

###  Advanced Level (Architecture & Strategy)


**Q7: Design a multi-agent system for automated code review that balances speed, accuracy, and safety.**


**Q8: How would you handle the cold-start problem for a new agentic system with no historical feedback?**



```
1. Synthetic feedback: Use rule-based validators as proxy feedback (e.g., 'if output contains X, assume low quality')
```

**Q9: What are the ethical considerations when deploying feedback-loop agents that adapt to user behavior?**



```
Governance: Establish an ethics review board for significant adaptation changes, conduct bias audits, and publish adaptation principles."
```

## Part 10: Conclusion – Your Agentic Engineering Journey


We’ve covered a lot of ground together:


**Conceptual foundations**: What makes an agent harness and why it matters more than the model  

**Tool comparison**: Claude Code vs. PI Agent—philosophy, capabilities, and trade-offs  

**Four hands-on labs**: From basic setup to meta-agent orchestration  

**Customization deep-dive**: Extensions, hooks, widgets, themes, and system prompts  

**Production considerations**: Security, scalability, and enterprise readiness  

**Strategic guidance**: When to use which tool, and how to hedge your bets  

**Interview prep**: Questions to test and demonstrate your expertise


But knowledge without action is just trivia.


**Your next steps**:


1. **Start small**: Install PI Agent. Run the basic session. Get comfortable with the workflow.
2. **Add one extension**: Pick a simple customization (footer, theme, skill loader). Implement it.
3. **Build one custom tool**: Create a tool that solves a real problem in your workflow.
4. **Experiment with orchestration**: Try the sub-agent or till-done patterns on a real task.
5. **Document your learnings**: Share what works, what doesn’t, and what you wish existed.


### The Bigger Picture


The rise of customizable agent harnesses isn’t just a technical shift—it’s a philosophical one. We’re moving from:


This shift puts more power—and more responsibility—in your hands.


**Questions to carry with you**:


*What limitations in my current workflow could a custom agent solve?*  

*What safety controls do I need before deploying an agent to production?*  

*How can I measure whether my agent is actually adding value?*  

*What would happen if my agent made a mistake—and how would I recover?*


The most powerful agents won’t just be technically sophisticated—they’ll be thoughtfully designed, responsibly operated, and human-centered.


### Final Thought



>  *“Every engineer is limited by the tools they use.”*
> 
>  


But here’s the empowering corollary:



>  *“Every engineer can expand what’s possible by building better tools.”*
> 
>  


You now have the patterns, the code, and the mindset to build the next generation of agentic engineering systems.


Go create something amazing. And build it responsibly.


## Appendix A: Quick Reference – PI Agent Extension Cheat Sheet


## Appendix B: Resource Toolkit


**PI Agent Resources**:


* GitHub: <https://github.com/mariozhan/pi-agent>
* Documentation: <https://pi.dev/docs>
* Extension Examples: <https://github.com/pi-agent/extensions>
* Community Discord: <https://discord.gg/pi-agent>


**Learning Resources**:


* “Agentic Engineering” patterns course (internal)
* LangChain/LangGraph documentation for orchestration concepts
* Anthropic’s Claude Code docs for comparison patterns
* Open source agent frameworks: AutoGen, CrewAI, Microsoft Autogen


**Security & Compliance**:


* NIST AI Risk Management Framework
* OWASP Top 10 for Large Language Model Applications
* Cloud Security Alliance AI Security Guidelines
* SOC 2 compliance checklist for AI systems


**Observability**:


* Prometheus/Grafana for metrics
* Jaeger/Tempo for distributed tracing
* Loki for structured logging
* OpenTelemetry for standardized instrumentation


**Testing**:


* pytest + pytest-asyncio for extension testing
* Playwright for browser-based agent testing
* Mock service workers for API integration tests
* Property-based testing for agent behavior validation


## Appendix C: Troubleshooting Guide


### Common Issues & Solutions


**Issue: Extension not loading**


**Issue: Agent stuck in loop**


**Issue: Tool call fails silently**


**Issue: Context window fills too fast**


**Issue: Custom theme not applying**


## Appendix D: Glossary of Terms




| Term | Definition |
| --- | --- |
| **Skill** | Reusable prompt template that guides agent behavior for specific tasks |
| **Till-Done List** | Task management pattern enforcing completion before agent can finish |
| **Prompt Engineering** | Crafting effective instructions and examples to guide LLM behavior |


### A Final Note


Hey—thanks for making it this far.


If you’re reading this, you’re probably someone who doesn’t just want to use AI tools—you want to understand them, shape them, and push them further. That’s exactly the mindset that will define the next era of software engineering.


The tools we use don’t just help us build—they shape what we believe is possible. By choosing to explore customizable, open-source agent harnesses like PI Agent, you’re not just learning a new tool. You’re claiming agency over your own engineering practice.


Keep experimenting. Keep building. And keep asking: *“How could this be better?”*


The future of agentic engineering isn’t written yet. You’re helping to write it.