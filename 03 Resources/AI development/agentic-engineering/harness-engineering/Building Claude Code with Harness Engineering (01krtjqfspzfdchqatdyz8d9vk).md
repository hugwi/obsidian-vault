---
title: "Building Claude Code with Harness Engineering"
source: "https://freedium-mirror.cfd/https://levelup.gitconnected.com/building-claude-code-with-harness-engineering-d2e8c0da85f0"
author: "freedium-mirror.cfd"
published: 2026-04-06
created: 2026-05-17
description: "Multi-agents, MCP, skills system, context pipelines and more"
tags:
  - to-process
  - harness-engineering
---

[![Fareed Khan](https://miro.medium.com/v2/resize:fill:88:88/1*feiUXOR8sid6IPHSHufA-g.jpeg)](https://medium.com/@fareedkhandev)[Fareed Khan](https://medium.com/@fareedkhandev)
Read this story for free: [link](https://medium.com/@fareedkhandev/d2e8c0da85f0?source=friends_link&sk=f67a164f042bf73b89077b71e8d76370)


As of early 2026, [Claude Code crossed $1 billion in annualized revenue](https://www.anthropic.com/news/anthropic-acquires-bun-as-claude-code-reaches-usd1b-milestone) within six months of launch. It did not get there because of better prompts. It got there because **Anthropic built the right harness around the right model**, a streaming agent loop, a permission-governed tool dispatch system, and a context management layer that keeps the model focused across arbitrarily long sessions. That harness is fully reproducible, and that is exactly what we are going to build.


Claude Code is built from five core components that work together:


and within these components there is a lot more ….


All code is available in the GitHub repository:


Our codebase is structured as follows …


I have separated each component of our Claude code architecture into different scripts so that we can run and test each component individually.


Harness engineering is the discipline of building the environment that surrounds an AI model, not the model itself. The model reasons and decides. The harness executes, constrains, and connects. A well-designed harness gives the model precisely the tools it needs, nothing more, and governs exactly what it is allowed to do with them.


If i break down the concept of harness engineering into four core principles, they would be:


Claude Code is not an agent framework. It is a harness, one of the most carefully engineered ones ever deployed in production. Anthropic did not build logic to decide when to read files or when to run tests. They gave Claude the tools to do those things and trusted the model to decide when they were needed.


Claude Code architecture follows the principles of harness engineering in several ways:


![None](https://miro.medium.com/v2/resize:fit:700/1*US6xsZVUlUGmcSRGB85-xw.png)
The agent loop is the single architectural primitive that everything else builds on. Before tools, before permissions, before multi-agent coordination, there is a loop that calls the model, observes what it wants to do, executes it, and feeds the result back.


![None](https://miro.medium.com/v2/resize:fit:700/1*S2RQmaoIE4uIwLC1udVYpA.png)
The most fundamental principle of any agentic system is the perception-action-observation cycle.


![None](https://miro.medium.com/v2/resize:fit:700/1*F6BHuz1GSXDGre72vphf6w.png)
This is not a retry loop or a fallback mechanism. It is the core reasoning engine. In Claude Code, this is the `nO` master loop, the same loop that runs whether you ask Claude to fix a one-line bug or refactor an entire codebase. The code never changes. Only what the model decides to do inside it changes.


To build the most basic phenomenon of Claude code using anthropic model we first have to initialize the client along with the model.


Since we are building claude we are using the anthropic model but you can use `litellm` to swap in any model you like, my github codebase is flexible to support any model provider.


As I previously mentioned the claude is build around tools, so we need to define some basic tools for our agent to interact with the world. These tools will be the interface through which the model can perform actions and gather information.


In here we are defining a single tool called `bash` that allows the model to execute shell commands. The tool has a name, a description, and an input schema that specifies the expected format of the input.


Dispatch is the mechanism that connects the model's tool calls to actual code execution. It is a dictionary mapping tool names to handler functions. This is important for bigger architectures like claude code which contains tons of tools, it allows us to keep the tool definitions separate from their implementations and makes it easy to add new tools without changing the core loop.


`dispatch_tools` is a helper function that takes the model's response content, identifies any tool calls, executes them using the provided dispatch map, and collects the results. It also includes logging for visibility into what tools are being called and their outputs.


Our agent loop is a simple while loop that continues until the model indicates it has reached a final answer.


Let's run this component with a simple task to see how it works.


In this code, we initialize an empty conversation history and enter a loop that continuously prompts the user for input. Each user query is added to the conversation history, and then we call the `agent_loop` function to handle the interaction with the model. After the loop finishes, we print the final answer provided by the assistant.


I ran it in a directory with some Python files. On the first attempt, the agent used an incorrect command and got an error. It then self-corrected, used the appropriate `find` command, and successfully retrieved the list of Python files, demonstrating the perception-action-observation cycle with real-world error recovery in action.


**In Claude Code's internal architecture, the tool registry is one of the most studied components by engineers** who have reverse-engineered its execution traces.


![None](https://miro.medium.com/v2/resize:fit:700/1*WITgExEqBm7qwRlFu6noDA.png)
The dispatch map is a dictionary that connects what the model wants to do to the code that does it. The loop is completely agnostic about what tools exist — it only knows how to call `dispatch[tool_name](input)`.


This separation means Claude Code can have 18 tools, 30 tools, or 5 tools, and the loop itself never changes. It is the same principle that makes Claude Code extensible through MCP, new tools are just new entries in the registry, regardless of whether they are local Python functions or remote servers.


Each key is exactly the name the model will use in its tool call. Each value is the Python function that executes it. When Claude decides to read a file, the loop does one dictionary lookup and calls the handler. There are no conditionals, no class hierarchies, no framework routing logic. The entire dispatch mechanism is a single line: `output = handler(tool_input)`.


The tool definitions are equally important. These are what the model reads to decide which tool to call — and the description field is not documentation, it is an instruction.


A poorly written description causes the model to pick the wrong tool. If `grep` says "search files" and `bash` says "run commands", the model will use bash for every search operation because the description does not constrain it precisely enough.


**Claude Code's internal tool descriptions are extremely specific about when each tool should be used this specificity is what produces consistent, predictable tool selection across millions of executions.**


The handler functions themselves follow a consistent contract — they accept a dict of inputs, return a string, and never raise exceptions to the loop. Errors are returned as strings, not thrown.


Notice that `run_read` returns numbered lines. This is intentional — when the model calls `write` to modify a file, it references line numbers from the previous `read`. The numbered output is what allows Claude to say "replace lines 45 through 67" with precision. Claude Code's read tool works exactly the same way.


The model chose `grep` over `bash` because the tool description was precise enough to make the right choice obvious. That is the dispatch map working exactly as intended. The intelligence of tool selection lives entirely in the model — the harness just has to describe tools well enough for the model to match intent to capability.


One of the most revealing findings from reverse-engineered Claude Code execution traces is what Claude does before it writes a single line of code or reads a single file on a complex task. It calls `TodoWrite`. Every time.


![None](https://miro.medium.com/v2/resize:fit:700/1*rbAIQUtzXWmJJN8RVmjIXw.png)
Claude Code injects the current todo state as a system reminder after every tool call. The model cannot forget what it planned to do because the plan is continuously re-injected into its context. This is what allows Claude Code to reliably complete tasks that span dozens of tool calls without losing track of the goal.


Three tools work together as a unit. `todo_write` commits the full plan at the start. `todo_update` marks each step as the agent moves through it. `todo_read` lets the model check its own progress at any point.


Together they create an external working memory that keeps the execution honest — the model cannot silently skip steps because each step has a status that persists across turns.


The system prompt is updated to make planning mandatory.


The word ALWAYS is load-bearing here. Without it, the model plans sometimes. With it, the model plans consistently. System prompt instructions that use strong imperative language produce more reliable behavior than ones that suggest or recommend.


The model committed to five steps before touching a single file. It executed them in order. It verified its work. This is not the model being careful by nature, it is the harness giving the model a structure that makes careful execution the path of least resistance.


Claude Code's execution traces reveal something interesting about how it handles large codebase exploration.


![None](https://miro.medium.com/v2/resize:fit:700/1*xkPyw8aqshub4US5tqL_vA.png)
This is subagent context isolation, the pattern that allows Claude Code to work on arbitrarily large codebases without the main conversation window filling with noise. Every intermediate result that is irrelevant to the final answer stays inside the subagent and is discarded when it finishes. The parent only pays for the context it actually needs.


The isolation is implemented by giving each subagent a completely independent `messages[]` list. There is no shared state between parent and child except the final text response that the child returns.


The subagent runs the exact same agent loop as the parent. It has access to the exact same tools. The only difference is its `messages[]` list starts empty and its system prompt focuses it on a bounded task. When it finishes, everything it accumulated, every file read, every grep output, every intermediate reasoning step is discarded. Only the final summary crosses back into the parent.


This is registered as a tool so the model can decide when to use it.


Let's test this .....


The parent conversation contained one tool call. The subagent ran twenty-five. The parent's context grew by exactly one summary paragraph. Without subagent isolation, the parent would have accumulated all twenty-five file reads and its subsequent reasoning would have been reasoning about file contents rather than about architecture.


The third phase is about the cognitive infrastructure where the agent moves beyond single-session execution loading domain knowledge only when it is needed.


![None](https://miro.medium.com/v2/resize:fit:700/1*lc36mqeJS7a0QKIwGNru_w.png)
Compressing conversation history before it degrades reasoning quality, and persisting task state to disk so that work survives process restarts. This is where Claude Code's skill system, compressor `wU2`, and long-term memory file come from.


One of the most expensive mistakes in harness engineering is putting everything the model might need into the system prompt.


![None](https://miro.medium.com/v2/resize:fit:700/1*mE4DYZqBy95RTq0D5cESDQ.png)
The model system prompt contains only one-line descriptions of available skills. When the model recognises it needs domain expertise for the current task, it calls `load_skill()` and the full instructions are injected via a tool result directly into the conversation at the exact moment they are needed. The model pays the context cost only when the knowledge is actually relevant. Install a hundred skills and the system prompt grows by a hundred lines, not a hundred pages.


The skill files themselves follow a consistent format — a metadata header for discovery, and a full body of procedural instructions that the model reads and applies.


The discovery mechanism scans the skills directory at startup, reads only the metadata header from each SKILL.md, and builds a lightweight registry that goes into the system prompt.


The system prompt references all available skills without loading any of them.


Let's test the skills methodology ....


The model loaded the skill, applied its structured methodology, and produced findings with file-and-line citations. Without the skill, the model would have reviewed code but inconsistently, without enforced categorisation, and without the deploy-readiness summary. The skill does not make the model smarter. It makes the model's output consistent and structured across every code review it will ever perform.


Every long-running session hits the same wall. The context window fills with tool outputs, intermediate results, and conversation turns that were relevant ten minutes ago but are now just noise.


It does not discard history, it summarises it, keeping the information while dramatically reducing the token footprint. The summary is then written to a persistent markdown file on disk, making the agent's memory durable across session restarts.


![None](https://miro.medium.com/v2/resize:fit:700/1*k9DSBXhUjoCKrZ5dFIM0-Q.png)
The implementation uses three explicit layers that process history in order. Recent messages are kept verbatim because they contain the active reasoning context. Older messages are collapsed into a single summary block via a dedicated compression API call. That summary is written to `.agent_memory.md` so the next session can load it and continue without starting from scratch.


The compression function is called after every agent response turn not on a timer, but based on measured context size.


At session startup, the agent checks for an existing memory file and loads it before the first user message.


After a long session of reading, writing, and testing, compression triggered automatically. The 18 accumulated messages — file contents, test outputs, intermediate reasoning — collapsed into one summary block. The next time this session starts, it loads that summary and continues with full context about what was accomplished, without paying for 18 turns of history on every subsequent API call.


Context compression keeps the conversation window manageable. But it solves a different problem from task tracking. Compression is about what the model remembers.


The task graph is about what the agent commits to doing across sessions, across restarts, and eventually across multiple agents working in parallel.


![None](https://miro.medium.com/v2/resize:fit:700/1*Pom5e7PVWfOoMpHP94oztQ.png)
Claude Code TodoWrite system is session-scoped. Close the terminal and the plan is gone. The task graph in this session extends that into a persistent, dependency-aware structure. Each task carries an ID, a description, a status, a priority level, and an explicit list of upstream task IDs that must be completed before it becomes available.


This is the foundation that Phase 4 multi-agent system builds on. When multiple agents run in parallel, they all read from and write to the same task graph. The dependency system ensures they never execute a task before its prerequisites are complete, and the atomic claiming mechanism in Phase 4 ensures no two agents claim the same task simultaneously.


The threading lock on every read-write operation is critical. In Phase 4, multiple agents will call `_load()` and `_save()` concurrently.


Without the lock, two agents can read the same state simultaneously, each modify it independently, and the second write silently overwrites the first agent's changes. The lock makes every task state transition atomic.


This is the behaviour that makes the task graph a fundamentally different mechanism from TodoWrite not just planning for one session, but a durable project state that survives anything.


The fourth phase is about breaking the single-agent ceiling where one context window and one execution thread are no longer enough running slow operations in background threads without blocking the main loop, delegating parallel workstreams to persistent specialist agents, governing inter-agent communication with a finite state machine, enabling autonomous task claiming without a central coordinator, and isolating parallel file writes at the git worktree level.


![None](https://miro.medium.com/v2/resize:fit:700/1*brkgb_ZvZ5dqNsdluhpT_g.png)
**In Claude Code's internal architecture, the** **`h2A`** **async queue is one of its most practical performance mechanisms.** When Claude runs a test suite, compiles a project, or performs a long database migration, it does not sit idle waiting for the result.


It pushes the operation into the background, continues planning the next steps, and receives a notification when the operation completes. The main reasoning loop never blocks on I/O.


Without this mechanism, a coding agent is only as fast as its slowest tool call. A test suite that takes 45 seconds means 45 seconds of silence no planning, no parallel work, no progress. Background execution eliminates that ceiling entirely by decoupling operation execution from the agent's reasoning cycle.


In our function `agent_loop_with_bg()`, we use `stream_loop()` as the main agent loop, but after every turn we check the `_BG_QUEUE` for any completed background tasks. If there are any, we inject them into the conversation as user messages so the model can react to them in its next turn.


The agent loop is wrapped to drain notifications between turns.


We are basically giving the model a new tool `run_bash_background()` that it can call whenever it wants to start a long-running operation without blocking. The model can continue reasoning, planning, and even executing other tasks while the background operation runs.


When the operation finishes, the model receives a notification with the result and can react to it in its next turn.


You can see that when our agent started a 45-second test suite, immediately pivoted to adding docstrings, finished all documentation work, and then received the test results when they arrived. In a blocking model this would have taken sequential time.


**With background execution the wall time was bounded by the slower of the two operations, not their sum**. This is exactly how Claude Code handles long-running operations in practice.


Claude Code parallel subagent system spawns ephemeral agents, they are created for one task and discarded. But real engineering work has specialisations that persist across many tasks.


A file exploration specialist, a code writing specialist, and a testing specialist each benefit from accumulated context about the codebase they are working in. Persistent teammates preserve that context across multiple delegated tasks.


![None](https://miro.medium.com/v2/resize:fit:700/1*wpeK5NEmLzR8bqd2Mi1JdA.png)
Each teammate runs continuously in a background thread with a defined specialisation and a JSONL file as its inbox. The lead agent writes a task to the teammate's inbox file. The teammate reads it, executes a full agent loop, and writes the result back to the lead's inbox.


The communication is fully asynchronous, the lead can continue working while the teammate executes and the teammate's accumulated knowledge about the codebase grows with every task it handles.


In our `TEAMMATES` dict, we define two specialist agents, an explorer and a writer, each with their own system prompt that focuses them on their specialisation. The lead agent can delegate tasks to these teammates by writing messages to their respective JSONL inbox files.


Each teammate runs its own agent loop in a background thread, polling its inbox continuously.


The teammate loop continuously checks its inbox for new messages. When it receives a message, it processes it with a full agent loop, generates a response, and sends the result back to the sender.


The lead delegated exploration to a specialist and implementation to another. Neither task polluted the lead's context. The explorer accumulated codebase knowledge in its own thread.


The writer used that output to make precise edits. The lead synthesised the results. This is multi-agent collaboration working at the architectural level, not the prompt level.


With multiple agents sending and receiving messages simultaneously, uncoordinated communication creates race conditions and deadlocks. An agent might send a second request before receiving the response to the first. Two agents might wait on each other indefinitely.


**Without a protocol governing when agents can communicate, the team is unreliable at exactly the moments when it is under the most load.**


![None](https://miro.medium.com/v2/resize:fit:700/1*RS-EM8rwA7fJbalUuvMspA.png)
Claude Code solves inter-agent coordination implicitly through the synchronous nature of tool calls the model issues a dispatch\_agent call and waits for the result before continuing.


The FSM makes this protocol explicit and enforced for persistent teammate architectures where communication is asynchronous. Each agent has four states IDLE, REQUESTING, WAITING, RESPONDING and one strict rule: no agent transitions to REQUESTING while already in WAITING. This single rule eliminates the entire class of coordination deadlocks.


We can test the FSM by simulating two agents sending messages to each other and verifying that they never violate the protocol. In this test, we attempt to send a second message while the first is still waiting for a response, and we check that the FSM correctly blocks that action.


When i ran this test, every state transition is logged. No agent sent a second request before receiving a response to the first. The protocol enforced this at the architectural level without requiring the model to reason about coordination — the model just calls `delegate`, and the FSM handles the rest.


The FSM protocol governs communication between agents but still requires a lead to assign work. For very large workloads migrating an entire codebase, generating documentation for hundreds of functions, running analysis across thousands of files even the lead becomes a bottleneck. Autonomous self-assignment removes the coordinator entirely.


![None](https://miro.medium.com/v2/resize:fit:700/1*7HO-HToah0evgWfLhPQ90A.png)
Each agent runs a continuous scan loop against the shared task graph from Phase 3. When it finds an unblocked pending task, it atomically claims it using a threading lock and begins execution.


The lock is critical without it, two agents scanning simultaneously would both find the same task available, both claim it, and both execute it, wasting compute and potentially producing conflicting results.


Lets test this by posting several tasks with dependencies and then starting two autonomous agents to execute them.


Two agents claimed tasks the moment they became available, worked in parallel, and the mypy verification task stayed blocked until all six annotation tasks were marked done.


**No lead assigned a single task after the initial posting.** This is the pattern that makes large-scale autonomous work tractable the intelligence of task ordering lives in the dependency graph, not in a coordinator agent.


Parallel agents writing to the same files in the same directory will eventually conflict. Two agents editing `core.py` simultaneously will produce a corrupted file regardless of how carefully each one works.


![None](https://miro.medium.com/v2/resize:fit:700/1*w6Hn-KU_zsrU-8LLMyIx5w.png)
Git worktrees give each agent its own complete checkout of the repository its own directory, its own branch, its own working tree. Two agents working in parallel are literally writing to different files in different directories.


There is no possibility of a write conflict because the files themselves are separate. When both tasks complete, the harness compares which files each branch modified and surfaces any overlapping changes for human review before merging.


We can test this by posting two tasks that both modify `core.py` and then starting two agents to execute them.


Each agent will create its own worktree, make changes to `core.py` in isolation, and when both complete, the harness will detect that both branches modified `core.py` and flag it for human review before merging.


Both agents read and modified `core.py` simultaneously but because they were working in separate worktrees, neither write interfered with the other. Each agent ran its test suite against its own branch and got clean results.


The conflict detection ran after both completed and correctly identified that a human needs to review the merge before either branch lands on main. This is the strongest isolation model in the repo parallel execution with zero possibility of mid-task interference.


The fifth phase is about the gap between a working agent and a deployable one where streaming makes the model's output visible in real time, file tools become reversible through automatic snapshotting, permission governance becomes declarative through a YAML rule system, every tool call becomes observable through a lifecycle event bus, and conversations become durable through session persistence.


![None](https://miro.medium.com/v2/resize:fit:700/1*G41h8rACpfEFYLIGjWR7dA.png)
In Claude Code, streaming is not a feature, it is the default. Every interaction streams tokens to the terminal as they are generated. The difference between a streaming agent and a blocking one is the difference between a tool that feels like a collaborator and one that feels like a batch job. For short responses the gap is imperceptible.


For long reasoning chains that span dozens of tool calls, a blocking agent sits silent for minutes while a streaming one shows its thinking in real time.


![None](https://miro.medium.com/v2/resize:fit:700/1*vTWlVsvKd0c6nhv1DG9NxA.png)
The change from blocking to streaming is a single swap `client.messages.create()` becomes `client.messages.stream()`. The loop logic stays identical. The dispatch logic stays identical. Only the way the response is consumed changes.


The `stream.get_final_message()` call at the end is important — it blocks until the stream is fully consumed and returns the complete response object with the same structure as `messages.create()`.


**This means all downstream logic, stop reason checking, tool use parsing, content block extraction works identically whether the loop uses streaming or blocking.**


We can test this by refactoring an existing agent loop to use streaming and verifying that the output is correct and the test suite still passes.


Notice the response above streamed token by token — "I'll start by reading", "The current s01 uses", "The key change is" all appeared progressively on screen. In a blocking model all of that text would have appeared simultaneously after a multi-second wait. This is the behaviour Claude Code users experience on every single interaction.


Claude Code ships with dedicated file tools Read, Write, Edit, Glob, Grep not because bash cannot do file operations, but because dedicated tools give the model precise semantic operations with structured outputs. When the model calls `read`, it gets back numbered lines it can reference by number in a subsequent `write`.


When it calls `grep`, it gets back file paths and line numbersl, not raw terminal output. This structure is what allows Claude to make precise, targeted edits rather than overwriting entire files.


The snapshot mechanism is equally important. Every `write` call in Claude Code silently saves the previous file content before overwriting. If the model's change breaks something, `revert` restores the original in one call. There is no need to use git, no need to manually copy files — the harness handles reversibility automatically.


In our `run_write` function, we check if the file already exists. If it does, we read its content and save it in the `SNAPSHOTS` dictionary before overwriting it. If the file does not exist, we mark it as newly created by setting its snapshot to `None`. The `run_revert` function checks the snapshot if it's `None`, it knows to delete the file; otherwise, it restores the original content.


The numbered line output from `run_read` is what makes precise edits possible.


In order to test this, we can run a sequence of tool calls that write to a file, verify the content, then call revert and verify the original content is restored.


The model read the file with numbered lines, identified the exact line with the problem, made a targeted fix, read the result back to verify the change looked correct, then ran tests. This is the extended tool arsenal working as designed — structured read output enabling precise write operations, followed by automatic snapshot that would allow instant revert if the tests had failed.


Claude Code permission system is one of its most studied architectural components. When you run Claude Code for the first time, it asks whether to run in auto-approve mode or confirmation mode.


**That choice maps directly to a permission tier system some commands always run silently**, some always require explicit approval, and some are blocked outright regardless of context.


This section implements that same three-tier model as a YAML configuration file. Security policy lives in configuration, not in code. Changing what requires approval is an edit to a config file, not a deployment. The rule evaluation runs as a pre-execution wrapper around every tool call.


The permission check wraps every dispatch call before execution.


Let's test this feature …


Two permission prompts appeared one for package installation, one for file deletion. Both required explicit approval before the harness executed them. The `ls`, `read`, and `pip freeze` calls ran silently because they matched `always_allow` patterns. This is exactly how Claude Code's permission system behaves in confirmation mode the model works uninterrupted on safe operations and pauses only when an action has real consequences.


Claude Code exposes a hooks system that lets users attach custom logic to any point in the agent lifecycle before a tool runs, after it completes, when an error occurs, when a session ends.


**This is how teams add cost tracking, audit logging, custom approval workflows, and integration with external monitoring systems without modifying the agent loop itself.**


![None](https://miro.medium.com/v2/resize:fit:700/1*J9qv0tGApSb3kPlnnOi2hg.png)
The event bus makes observability a structural property of the harness rather than something bolted on after the fact. Every significant moment fires a named event. Any function registered as a handler receives the full payload. A `pre_tool_use` hook that returns `{"block": True}` can prevent a tool from running — this is how policy enforcement layers cleanly on top of permission governance.


Three built-in hooks cover the most common production needs.


The agent loop fires events around every tool call.


In our test, we can verify that every tool call is logged with timestamps and input previews, that the timer flags any calls that take longer than 5 seconds, and that the stats hook prints a summary of tool usage at the end of the session.


The session-end stats hook printed automatically after the loop exited. Every tool call was logged to `.agent_events.log` with timestamps and input previews. The timer hook ran on every call and would have flagged any that exceeded 5 seconds.


**All of this happened without a single line of observability code inside the agent loop itself**, the loop only fires events, the hooks decide what to do with them. This is exactly how Claude Code's hooks architecture separates concerns.


A session that cannot be resumed is a session that cannot be trusted with long tasks. If the model is 30 minutes into a complex refactor and the terminal closes, everything is lost not just the conversation, but the reasoning context that led to every decision made.


![None](https://miro.medium.com/v2/resize:fit:700/1*CKz7Txi5XFYe3R5TEgga_g.png)
Claude Code stores every message, tool call, and result locally as you work. This section implements the same mechanism with three REPL commands that make persistence actionable.


Three REPL commands make persistence actionable — `:resume` continues an existing session, `:fork` branches from any point without affecting the original, `:sessions` lists everything saved.


This can be tested by starting a session, making some changes, then resuming it to verify the state is intact. The fork command can be tested by forking an existing session, making different changes in the original and the fork, and verifying that both states are preserved independently.


The terminal closed mid-session and resumed exactly where it left off — 14 messages of context, full todo state, complete history of what was done. The fork created an independent branch where additional changes could be explored without affecting the original. Claude Code provides this exact capability natively, this session is the explicit implementation of the pattern that makes long autonomous sessions trustworthy.


The sixth phase is about performance and control where the agent moves from correct to fast and steerable — collapsing multi-tool turns from sequential to concurrent with `asyncio.gather`, giving users real-time steering through interrupt injection, eliminating redundant token spend through prompt caching, and opening the tool registry to any external server through the official MCP runtime.


One of the most significant performance characteristics of Claude Code, revealed through execution trace analysis, is that it never runs tool calls sequentially when it does not have to.


![None](https://miro.medium.com/v2/resize:fit:700/1*N5AUKXkP1GtO1NzLkIdeSw.png)
The implementation requires refactoring the synchronous dispatch loop into an async one. Every tool handler gets an async wrapper. The streaming call runs in an executor to keep the asyncio event loop free. And `asyncio.gather()` replaces the sequential for loop over tool blocks.


The async tool implementations use `asyncio.create_subprocess_shell` instead of `subprocess.run` so bash commands are truly non-blocking. File operations run in a thread executor since they are inherently synchronous I/O. Write operations get a per-path lock to prevent two parallel writes to the same file.


Let's test this ...


Three greps ran simultaneously. Then five reads and bash calls ran simultaneously. The model received all results at once and synthesised them in a single reasoning step. In sequential execution this would have been eight separate turns. In parallel it was two.


Claude Code lets you press Ctrl+C mid-task to redirect the agent without losing any of the work it has done. The agent does not crash, it reads your interrupt, summarises its current progress, and waits for new instruction. This is the `h2A` steering queue: an async channel that sits alongside the agent loop and accepts messages from any source at any time.


![None](https://miro.medium.com/v2/resize:fit:700/1*cYZYGmalvsfMF6toir33Cg.png)
Without this mechanism, a long-running task is a commitment. You start it, walk away, come back twenty minutes later, and either it finished correctly or it did not you had no way to steer it once it started. With interrupt injection, you can redirect mid-execution, add context the agent did not have when it started, or tell it to stop and summarise where it got to.


The interrupt arrived mid-task, the agent stopped cleanly, summarised exactly what it had done and what remained, and waited. Then the user redirected skip s03, jump to s04–s06. The agent continued with the new instruction without losing any of the completed work. This is the interaction model Claude Code provides — long tasks stay steerable rather than becoming commitments.


Reverse-engineered Claude Code execution traces show a 92% prompt prefix reuse rate across all internal agent calls. This is not accidental — it is the result of structuring every prompt so that stable content comes first and variable content comes last.


**Anthropic prompt caching serves those stable prefixes at approximately 10% of the normal token cost**. For an agent that makes hundreds of API calls in a long session, this compounds into very significant savings.


![None](https://miro.medium.com/v2/resize:fit:700/1*aJKNBASn3cnbO24opbTPOg.png)
The system prompt and tool definitions are the most stable content in any agent session they never change between turns. Marking them as cacheable means every call after the first gets those tokens from cache rather than paying full price.


The `cache_control` marker tells Anthropic's infrastructure to build a KV cache entry on the first call and serve it on all subsequent calls that share the same prefix.


A token usage tracker makes cache performance visible on every call.


The first call wrote 1,847 tokens to cache the system prompt and tool definitions. Every subsequent call served those same tokens from cache at 10% cost. Across 6 calls, 8,310 tokens were saved. In a full Claude Code session that makes hundreds of calls, this same mechanism is what produces the 92% prefix reuse rate observed in execution traces.


Claude Code supports MCP natively — any compliant server's tools become first-class citizens in the agent's tool registry. A filesystem server adds file tools. A git server adds git operation tools.


A database server adds query tools. The model calls all of them identically to built-in tools, with no awareness of whether a tool is a local Python function or a remote server process.


![None](https://miro.medium.com/v2/resize:fit:700/1*MGSUS1FY58V3YNM_5A3xpw.png)
The MCP runtime reads server configurations from `config/mcp_config.yaml`, connects to each server at startup using the official MCP Python SDK, calls `list_tools()` to discover what each server provides, and registers everything under a prefixed name `mcp__<server>__<tool>` — in the dispatch map alongside the built-in tools.


The dispatch router handles MCP tools identically to built-in tools — a prefix check is the only difference.


The model called `mcp__git__git_log`, `mcp__git__git_diff`, and `mcp__filesystem__read_file` exactly as it would call bash or grep — same tool call structure, same result injection, same loop. The MCP prefix is purely a routing detail in the dispatch map.


From the model's perspective, the tool registry simply grew from 14 to 28 tools when the servers connected at startup.


**This is how Claude Code's MCP support works external servers extend the tool registry transparently, with zero changes to the agent loop or the model's interaction pattern.**


**The seventh phase is about replacing teaching implementations with production-grade alternatives** where file-based mailboxes become Redis pub/sub channels with instant delivery and cross-machine support, basic worktree creation becomes a full lifecycle manager that handles every edge case a real codebase surfaces, and the entire system is assembled into a single deployable reference that wires all mechanisms together.


![None](https://miro.medium.com/v2/resize:fit:700/1*CbmRgi5V294U0J1_eHWb9Q.png)
This is where the gap between a working prototype and a system you can run in production closes.


The JSONL mailbox system from Phase 4 works as a teaching mechanism but has three fundamental production problems. It requires polling teammates check their inbox file on a timer, introducing artificial latency between message send and message receive.


It needs file locking for concurrent access two agents writing to the same file simultaneously produce corrupted JSONL. And it is single-machine the mailbox files live on one filesystem, making distributed deployment impossible.


Claude Code's internal agent coordination uses message passing that is instant, lock-free, and works across process boundaries. Redis pub/sub provides exactly these properties. An agent publishes to a channel and any subscriber receives it within milliseconds no polling loop, no file locking, no filesystem dependency.


The implementation wraps both backends behind a common interface so the teammate and lead agent logic from Phase 4 stays completely unchanged.


We need to build a fallback for local development when Redis is not available — an in-process `asyncio.Queue` that provides the same interface but without cross-machine support or instant delivery.


The teammate loop and lead agent logic are completely agnostic to the mailbox implementation they call `send()` and `receive()` and do not care how those are implemented.


The teammate loop is identical to Phase 4, the mailbox interface hides all transport details.


In our `teammate_loop()` implementation, the agent receives messages from its mailbox, processes them with the model and tools, and sends results back to the sender via the same mailbox interface.


The lead agent can send tasks to teammates without caring about the underlying transport it just calls `mailbox.send()` and waits for responses.


Now we can run multiple teammates in parallel, each on their own Redis channel …


The latency difference is visible in the output, Redis delivers messages in under 10ms compared to the 500ms polling interval of the JSONL approach. For a session with dozens of inter-agent messages, this compounds into meaningful wall-time savings. More importantly, the Redis backend works identically whether both agents run on the same machine or on different machines in a cluster — the JSONL approach cannot do this at all.


The basic worktree implementation from Phase 4 creates and removes worktrees but fails silently on every edge case that production use surfaces. A repository with uncommitted changes behaves differently when creating a worktree.


**A branch that already exists from a previous crashed run causes** **`git worktree add`** **to fail**. A repository in detached HEAD state cannot create new branches. And two agents that both modify the same file in separate branches create a merge conflict that neither agent will catch.


![None](https://miro.medium.com/v2/resize:fit:700/1*YdBaGbO-4auI7-ThpIgIHw.png)
Claude Code avoids most of these issues by using file snapshots rather than worktrees. But worktrees provide stronger isolation an agent literally cannot touch another agent's files making them the right choice for large parallel tasks. The production worktree manager handles every edge case systematically before any task execution begins.


We also need to create a safe wrapper around worktree creation that handles every edge case and provides clear error messages when it cannot proceed.


This is critical for a good user experience because if the model tries to create a worktree and it fails silently due to an edge case, the agent will be confused and likely fail the task without any indication of what went wrong.


Similarly we create `conflicts` detection that runs before any task execution begins to check if any parallel tasks modified overlapping files. If they did, we can either fail fast with a clear message or alert the model and let it decide how to proceed.


And in order to run a task in an isolated worktree with full lifecycle management, we need to wrap the entire execution in a try/finally block that ensures the worktree is always cleaned up even if the task fails with an exception.


Let's run the execution trace for two parallel tasks …


The pre-flight check ran before any worktree was created. Both tasks executed fully in parallel in isolated directories. Both ran their test suites independently and got clean results because they were writing to different files. The conflict detector ran after both completed and correctly identified the overlap.


The branches were preserved rather than deleted so the merge can be done deliberately. This is production-grade worktree management every edge case handled, every failure mode accounted for, cleanup guaranteed regardless of what happens during execution.


With twenty-three individual sessions implemented, this file answers the question every engineer asks after reading through the phases: what does it look like when all of them run at once?


The combined file wires every mechanism from Phases 2 through 4 together using the shared foundation from Phase 1 todo planning, task graph dependency tracking, subagent context isolation, on-demand skill loading, three-layer context compression, background task execution, persistent agent teams, FSM communication protocols, and git worktree isolation all active simultaneously.


I created a file is 280 lines because `core.py` handles everything shared. Each mechanism contributes only its unique logic.


We can simulate a complex session that uses every mechanism such as:


Every mechanism contributed something visible: skill loading shaped the debugging approach, subagent isolation handled the JSON analysis without polluting the main context, background execution ran the test suite while the agent wrote new tests, context compression triggered automatically when the session grew large.


So far we have built a complete Claude Code harness from a minimal agent loop all the way to a production-grade multi-agent system with streaming, parallel execution, prompt caching, Redis mailboxes, permission governance, session persistence, and an official MCP runtime.


The architecture is clean, non-repetitive, and fully tested. There is still room to push it further.