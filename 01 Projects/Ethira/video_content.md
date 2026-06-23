# Ethira Agentic Architecture — Responsibilities & Portable Learnings

## Overview

Ethira design document covering agentic architecture, portable responsibilities, component structure, and evolution from MVP to production.

## Architecture — Five Layers

### Layer Diagram Structure

The architecture organizes into five distinct layers in hierarchical flow:

1. **Entry point** (top)
   - User interface entry point
   - Clear/Action buttons
   - External API/WebSocket connection

2. **Orchestration Hub** (second level)
   - Request path, end to end
   - Message routing and coordination

3. **Specialized Agents** (middle level)
   - Multiple agent implementations
   - Each with specific responsibility

4. **Domain Logic & Services** (fourth level)
   - Business logic execution
   - Data processing

5. **Infrastructure** (bottom)
   - Database access
   - External services
   - System persistence

## Request Path End to End

The complete request flow:

```
User Interface
    ↓
Orchestration/Routing
    ↓
Agent Selection & Dispatch
    ↓
Domain Logic Execution
    ↓
Infrastructure & Storage
    ↓
Response Back to User
```

### Architecture Diagram Details

**Top Level: Entry Point**
- Clear/Action buttons
- External API/WebSocket entry
- WebSocket + API Channel

**Orchestration Layer:**
- Message composition with AI coordination
- Request routing/dispatch

**Agent Layer:**
- Text-Agent + LLM Agent
- Specialized processor agents
- Context Management
- Tool/Action Execution

**Domain Layer:**
- Business logic implementation
- State management
- Tool execution framework

**Infrastructure:**
- LLM integration
- Workspace data
- External systems

## What Library is Actually Running the Agents?

The library running agents is **LangChain** (highlighted explicitly in document).

### Key Implementation Details:

**Undefined Agent/Coordinator roles:**
- LangChain is bundled but not used
- Agent responsibilities are scattered
- LangChain has specific patterns and pipelines

**Evidence of Challenges:**
- Some undefined chains following direct-based patterns
- Documentation mentions LangChain integration issues
- The last undefined chains suffer from a missing tool
- The architecture needed to decide: is LangChain being used or not?

### LangChain Integration Points:

The undefined chains follow a simplified pattern (not LCEL chains):
- Direct agent-to-tool execution
- Built-in semantic retrieval over workspace docs
- Agent-to-action routing without full chain orchestration

**Why undefined chains might be missing LangChain:**
- Initially trying to avoid LangChain complexity
- Attempting direct agent implementation
- Missing tool registration or chain definition
- Agent state not properly integrated into chain state

## Asynchronous Conversation — WebSocket + Queue Decoded

### Architecture Overview:

Core flow uses WebSocket + durable queue pattern:

```
User sends message via WebSocket
    ↓
Message enters distributed queue (FIFO)
    ↓
Agent consumes from queue (potentially async)
    ↓
Agent executes tools/logic
    ↓
Message posted back via WebSocket
    ↓
User receives response
```

### Key Components:

**Entry Layer:**
- WebSocket connection for real-time updates
- Queue-based message handling
- Task cards, status cards, activity tracking

**Chat UI Evolution:**
- Hard-coded UI interactions
- Queue strip, task cards, status cards
- Agent-driven updates

## Component Responsibilities

### Entry Point
- WebSocket server listening on port
- Queue publishing
- User message reception

### Orchestration Hub
- Message coordination
- Queue management
- Agent dispatch logic

### Specialized Agents
- Process queue messages asynchronously
- Execute domain logic
- Return results via WebSocket

### Domain & Business Logic
- Chat state machine
- Message processing
- Tool execution (document extraction, analysis)

### Infrastructure
- Queue persistence (Redis/similar)
- Database operations
- WebSocket broadcast

## Evolution — Hardened Chat UI

### Phase Timeline:

**P1: MVP (Jun-Jul 2025)**
- Working tool-calling chat agent
- WebSocket + first document-grounded extraction
- Basic document indexing

**P2: Scale & Transport (Aug-Oct 2025)**
- Semantic split from the socket into durable extraction
- Durable channel (Slack). Providers layer
- Cost calculation

**P3: Provider Maturity (Nov 2025-Jan 2026)**
- EZ-resident LLM routing through a single provider gateway
- Multi-provider support
- Cost optimization

**P4: RAG & Tools (Feb-Mar 2026)**
- Semantic retrieval over workspace docs
- Keywords + vector test
- Hashtag lookup
- Controlled modal chains and keyword routing

**P5: Cost (May-Jun 2026)**
- May 2026: Chat state machine
- Hardened implementation with cost monitoring
- Runtime evaluation

**P6: Hardening & Cost (Sep 2026 onwards)**
- Comprehensive cost tooling

### Evolution Rationale:

Each phase earned overarching capability:

**P1 → P2:**
- A working tool-calling chat agent
- WebSocket + first document-grounded extraction
- Long tool loops underpin the required interface

**P2 → P3:**
- Long tool loops outlying the requested pattern
- Standard single document flow
- Document-hand document output

**P3 → P4:**
- Data residency + removing manual document handling
- Keyword matching over important capabilities
- Durable extraction (+ removal)

**P4 → P5:**
- Data residency + removing manual document output
- Encapsulated subject + plan bubble (supporting it)
- Backend subject + plan bubble (supporting it)

**P5 → P6:**
- Standard subject + plan bubble
- Backend (+ removal)

## Component Responsibilities — Tools & Permissions

### Agent Router:

| Agent | Responsibility | Toolset | Eval/Sanctions |
|-------|----------------|---------|-----------------|
| Chief | Entry point | +1 Execution | +Execution |
| Router | Request dispatcher | Message routing | Audit verified |
| Extractor | Document analysis | PDF/text parsing | Sandbox isolated |
| Classifier | Intent detection | Pattern matching | Rules-based |
| Planner | Task orchestration | +1 Embedding | +Embedding verified |
| Executor | Tool execution | Workspace tools | Controlled token +1 sandbox |
| Safety keeper | Safety enforcement | guardrails | +Execution constraints |
| Controller | State machine | state_queue, stream | Controlled + deterministic |
| Embedding | Vector generation | +Embedding service | Sandbox isolated |
| Chat admin | Session management | session handlers | +Admin privileges |

### Evaluation — Tools & Permissions Table:

**Tool: chat_handler**
- Status: ✓ Working
- Eval: Chat-verified
- Details: Handles socket and push updates to clients

**Tool: doc_extractor**
- Status: ✓ Working
- Eval: Tested separately
- Details: Extracts text, images from documents

**Tool: intent_classifier**
- Status: ✓ Working
- Eval: Tested independently
- Details: Classifies intent via regex/ML patterns

**Tool: semantic_router**
- Status: ⚠ In progress
- Eval: Partial coverage
- Details: Routes based on semantic similarity

**Tool: plan_generator**
- Status: ⚠ In progress
- Eval: Limited testing
- Details: Generates multi-step execution plans

**Tool: workspace_resolver**
- Status: ✓ Working
- Eval: Sandbox tested
- Details: Resolves workspace file paths

**Tool: embedding_service**
- Status: ✓ Working
- Eval: Verified against benchmark
- Details: Generates embeddings for retrieval

**Tool: cost_monitor**
- Status: ✓ Working
- Eval: Budget-aware routing verified
- Details: Tracks cost per request, adjusts model selection

**Tool: safety_evaluator**
- Status: ⚠ In progress
- Eval: Rules-based filtering
- Details: Evaluates safety and compliance

**Tool: state_machine**
- Status: ✓ Working
- Eval: Message logging, context preservation
- Details: Maintains conversation state and history

## Cost Integration — The Full Toolbox

### What a Costs Section:

Cost monitoring across:
- **per_user_cost**: Cost attribution per user ID
- **session_cost**: Accumulated cost per session
- **model_routing**: Cost-aware model selection (cheaper cheaper models for simple tasks)
- **token_counting**: Precise token counting per request (cache aware)
- **budget_enforcement**: Hard limits per user or org tier

### Implementation Pattern:

```typescript
// Cost monitoring in agent execution
const cost = calculateCost(model, inputTokens, outputTokens);
costMonitor.recordCost(userId, sessionId, cost);

if (totalSessionCost > budgetLimit) {
  // Route to cheaper model or deny request
  switchToEconomyModel();
}
```

### Economic-Safety Review Gate — AI Reviewing All for Cost Runaway

Economic safety evaluation ensures:
- No accidental unbounded loops
- Costs tracked per decision tree
- Safety guardrails prevent runaway token usage
- Budget enforcement at model selection stage
- Cost anomaly detection and alerts

## Cost Integration — The Full Toolbox

### Tool-Specific Costs:

**Document processing (PDF extraction)**
- Cost per page: varies based on complexity
- Includes OCR, embedding, indexing
- Batching supported for efficiency

**LLM calls with routing**
- Small model: optimal for classification ($0.03 per 1M tokens)
- Large model: for complex reasoning ($0.15 per 1M tokens)
- Smart routing minimizes cost while maintaining quality

**Embedding generation**
- Batch embedding with caching
- Reuse embeddings across similar queries
- Cost optimization through intelligent scheduling

**WebSocket maintenance**
- Connection pooling with per-connection cost tracking
- Idle timeout to reduce infrastructure costs
- Circuit breaker pattern to prevent cascade failures

## Evolution — Backend Agent Stack (Cli-Verified)

### Phase Dates & Overarching Capability Earned

**Birth: Jun-Jul 2025**
- A plain chat bubble surface
- Message list, positioning, media container

**Identity: Mar-Apr 2026**
- A distinct chat identity and a composable input builder + following animation
- Streaming tokens, interleaving status cards, run-tracking

**Docs & Agents: May-Jun 2026**
- Long tool loops underpin the required interface
- Changed with chat, document handling affect
- Backend subject + plan bubble

**Build-order Takeaways: The Part Worth Stealing**

### Best Practices — followed vs missing (scorecard)

#### Best Practices Achieved:

| Area | Status | Implementation | Gap/Severity |
|------|--------|-----------------|----------------|
| Chat state machine | ✓ | In-code-guard | Low complexity |
| Workspace tooling | ✓ | Handle queries, embeddings | High semantics |
| User agent abstraction | ✓ | Independent single-sourced agents (not LLM chains) | No LLM stack |
| Structured extraction | ✓ | Parsing personal agent output | Minimal data validation |
| Streaming agent results | ✓ | Real-time updates via WebSocket | MLD incompatible |
| Multi-agent workflows | ⚠ | Conversations sometimes chained from previous state | Debugging difficult |
| Rate limiting | ✓ | Implemented per-user, per-session | Cascading context |
| Eval document clause | ⚠ | Missing chat history safety clause (OWASP) | Medium priority |
| Teleport/LLM module | ✓ | Clear: Teleport (+ decoupled) from module. Teleported module serializes safely | Low priority |

#### Best Practices — Followed vs Missing (Scorecard):

**Audit agent:system agent pattern:**
- Status: ✓ Working | Achieved
- Implementation: Audit agents validate system outputs
- Tool constraints: Apply policy guards
- Error recovery: Alert on guardrail violations

**Builder state machine in state_queue:**
- Status: ✓ Working | Verified
- Implementation: State transitions logged in queue
- Tool execution: Query allowed only in specific states
- Safety checks: Prevent invalid state transitions

**Observability-Dispatch with the provider mang stream (IL, not state): the cost visibility during the first [?]**
- Status: ✓ Working
- Implementation: Dispatch includes cost metadata
- Visibility: Cost breakdown visible in audit logs
- Optimization: Auto-switch to cheaper model if cost exceeds threshold

**Generalization & Teleport**:
- Status: ✓ Implemented
- Implementation: Agents can teleport to different contexts
- Safe states: Only teleport when state allows
- Cost implications: Track teleport overhead

**Build-order Takeaways: The Part Worth Stealing:**

1. **Asynchronous queue-based architecture** — allows scaling agents independently
2. **WebSocket for real-time updates** — streaming results back to client immediately
3. **Cost monitoring integrated from day 1** — prevents budget overruns
4. **Independent agent abstractions** — don't require LLM chains, simpler to test
5. **State machine for conversation flow** — deterministic and debuggable
6. **Semantic + keyword routing** — hybrid approach works well in practice
7. **Eval/safety scorecards** — track architectural debt and gaps

## Carrying It to the Next Project — the Tiered Playbook

### Build One Strategy at Any Step:

**Decoder part / Logic LLM model parts:**
- Declare a workflow in to the container for the first project (hardened)
- Think about its cost structure and declare its basic boundaries

**Evolving it aggressively from scratch:**
- Build the one-LLM at any step using Langchain patterns (skeleton only)
- Multi-vector transport with a model adaptor
- This specialist model can share single adaptive interfaces across many calls
- Special-use single-layer abstraction layer

**Explain Explicit Blocks & Tools:**
- Explicit `deepBlocking`/async await + queuing system
- Try tracking every turn day one  (planning decisions)

**Tracing routing from first day one:**
- OpenTelemetry details opens + the accumulates
- Queue/messaging layer isolated
- Middleware: Audit traces

**Carrying it to the next project — the tiered playbook:**

What things in a production backend belongs in project:

1. **Build one-simple strategy first** — use simple in-memory queuing, evolve to durable later
2. **Earn the part while in first run** — multi-vector transport with a model adaptor
3. **Special-use single-layer abstraction layer** — clear contracts between components
4. **Explain Explicit Blocks & Tools:**
   - Async/queue-based message handling
   - Cost tracking from day one
   - Safety evaluators as first-class components
5. **Tracing routing from first day** — OpenTelemetry instrumentation
6. **Queue/messaging layer isolated** — can swap Redis → PostgreSQL without changes
7. **Audit middleware from project start** — logging, cost attribution, safety checks

### Recommendation: Build the one-simple strategy first + earn the part while in first run

Either single contract + model adaptor framework — can share across many projects.

**Next: Declaring Recommendation & its the largest project!**

Edge: I do one only safety aspect in its declaration. But is a known pattern since the inception of SQL. Perhaps while I did trace through the application more, that would become clear: **Declaring one tiered strategy — build it cheap, validate early, iterate fast.**
