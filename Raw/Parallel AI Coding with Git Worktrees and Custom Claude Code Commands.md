---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - claude-code
  - harness
  - workflow-git
source: readwise
created: 2026-06-23
rating: 
action: 
theme: workflow-phases-gates
subtheme:
  - plan-phase
---

# Parallel AI Coding with Git Worktrees and Custom Claude Code Commands

![rw-book-cover](https://docs.agentinterviews.com/img/agent-interviews-logo-zip-file/png/logo-color.png)

## Metadata
- Author: [[Agent Interviews Team]]
- Full Title: Parallel AI Coding with Git Worktrees and Custom Claude Code Commands
- Category: #articles
- Summary: This text explains how to use Claude Code's custom commands with git worktrees to run multiple AI agents coding in parallel on different branches. This method helps create several versions of the same feature at once, allowing you to pick the best one. It makes AI coding faster, more flexible, and scalable for teams.
- URL: https://docs.agentinterviews.com/blog/parallel-ai-coding-with-gitworktrees/

## Full Document
AI coding is evolving fast. With Claude Code support for custom commands, it's time to upgrade your workflows. One of the most powerful advanced agentic coding techniques is **parallel development with Git worktrees**—running multiple Claude agents simultaneously on different branches of your codebase using custom slash commands. Our adoption of this technique is inspired by the [benchy repository](https://github.com/disler/benchy) from this [video](https://youtube.com/watch?v=f8RnRuaxee8).

Let's break it down step-by-step so you can replicate this advanced workflow in your own repo using **custom Claude Code commands**.

#### What is Parallel AI Coding?

**Parallel AI coding** is an advanced development technique where you run multiple AI agents simultaneously on isolated copies of your codebase to implement the same feature. Using git worktrees and custom Claude Code commands, each agent works independently on its own branch, producing different implementations of the same specification.

This approach leverages the non-deterministic nature of Large Language Models (LLMs) as a feature rather than a limitation. Since the same prompt can produce different valid solutions, parallel AI coding lets you explore multiple solution paths simultaneously and choose the best result.

The key components are:

* **Git worktrees** for isolated development environments
* **Custom Claude Code commands** for orchestrating multiple agents
* **Parallel execution** using Claude's Task tool
* **Comparative analysis** to select the optimal implementation

Also known as AI imagines, you pick your vision...

![Parallel AI Coding Workflow](https://docs.agentinterviews.com/assets/images/ChatGPT%20Image%20Jun%207,%202025,%2008_29_49%20PM-28f84e15a9cb0953eb98a4e8a816e997.png)Parallel AI Coding Workflow
#### Why Parallel Workflows?

Large Language Models (LLMs) are non-deterministic. The same prompt run twice can produce different results. With Claude 4, these results are often good—but they'll be **different**. Running **N parallel agents** gives you:

* Redundancy if one agent fails
* Multiple design perspectives
* Better final code by picking the best result

#### Project Structure

We'll use custom Claude Code commands with git worktrees. Git worktrees allow you to check out multiple branches from the same repository into separate directories - perfect for parallel development. Here's the essential directory structure:

```
project/  
├── .claude/  
│   └── commands/  
│       ├── init-parallel.md  
│       └── exe-parallel.md  
├── client/  
├── docs/  
├── server/  
├── specs/  
│   └── interview-dashboard.md  
└── trees/  
    ├── interview-dashboard-1/  
    ├── interview-dashboard-2/  
    └── interview-dashboard-3/  

```

#### Step 1: Set Up Custom Claude Code Commands

##### **Understanding Custom Commands**

Claude Code supports custom slash commands that you can create to quickly execute specific prompts or tasks. When you create a command file in `.claude/commands/`, it becomes available as a slash command with the `/project:` prefix.

Here's how the system works:

* Command names are derived from the filename (e.g., `init-parallel.md` becomes `/project:init-parallel`)
* You can use `$ARGUMENTS` placeholders that get replaced with user input
* Commands are version controlled and shareable with your team
* The markdown content becomes the prompt sent to Claude when invoked

For the complete guide on creating custom slash commands, see the [official Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code/tutorials#create-custom-slash-commands).

Let's set this up:

##### **Create the Commands Directory**

```
mkdir -p .claude/commands  

```

##### **Create the Initialization Command**

Create `.claude/commands/init-parallel.md`:

```
# Initialize Parallel Worktrees  
## Variables  
FEATURE_NAME: $ARGUMENTS  
NUMBER_OF_TREES: $ARGUMENTS  
## Instructions  
Create NUMBER_OF_TREES git worktrees for parallel development of FEATURE_NAME.  
1. Create the trees directory if it doesn't exist  
2. For each tree (1 to NUMBER_OF_TREES):  
- Create a new git worktree at `trees/FEATURE_NAME-{i}/`  
- Create a new branch named `FEATURE_NAME-{i}`  
- Copy environment files to each worktree  
- Set up development environment in each worktree  
Each worktree will be an isolated copy of the codebase on its own branch, ready for independent development.  
RUN `mkdir -p trees`  
For each worktree:  
```bash  
git worktree add trees/FEATURE_NAME-1 -b FEATURE_NAME-1  
git worktree add trees/FEATURE_NAME-2 -b FEATURE_NAME-2  
git worktree add trees/FEATURE_NAME-3 -b FEATURE_NAME-3  
```  
Copy environment variables and setup each environment:  
```bash  
cp .env trees/FEATURE_NAME-1/.env 2>/dev/null || true  
cp .env trees/FEATURE_NAME-2/.env 2>/dev/null || true  
cp .env trees/FEATURE_NAME-3/.env 2>/dev/null || true  
```  
List the created worktrees:  
RUN `git worktree list`  

```

##### **Create the Execution Command**

Create `.claude/commands/exe-parallel.md`:

```
# Parallel Task Execution  
## Variables  
PLAN_TO_EXECUTE: $ARGUMENTS  
NUMBER_OF_PARALLEL_WORKTREES: $ARGUMENTS  
## Run these commands first  
RUN `ls -la trees/`  
RUN `git worktree list`  
READ: PLAN_TO_EXECUTE  
## Instructions  
We're going to create NUMBER_OF_PARALLEL_WORKTREES new subagents that use the Task tool to create N versions of the same feature in parallel.  
This enables us to concurrently build the same feature in parallel so we can test and validate each subagent's changes in isolation then pick the best changes.  
The first agent will run in trees/<feature_name>-1/  
The second agent will run in trees/<feature_name>-2/  
...  
The last agent will run in trees/<feature_name>-<NUMBER_OF_PARALLEL_WORKTREES>/  
The code in each worktree will be identical to the code in the current branch. It will be setup and ready for you to build the feature end to end.  
Each agent will independently implement the engineering plan detailed in PLAN_TO_EXECUTE in their respective workspace.  
When each subagent completes their work, have them report their final changes in a `RESULTS.md` file at the root of their respective workspace.  
Make sure agents don't run start.sh or any other scripts that would start servers - focus on the code changes only.  

```

#### Step 2: Create Your Development Plan

Create a clear specification in `specs/interview-dashboard.md`:

#### Step 3: Execute the Parallel Workflow

Now you can use your custom commands to orchestrate parallel development:

##### **Initialize the Worktrees**

This command will:

* Create 3 git worktrees in the `trees/` directory
* Set up branches `interview-dashboard-1`, `interview-dashboard-2`, `interview-dashboard-3`
* Copy environment files to each worktree
* Prepare isolated development environments

##### **Execute Parallel Development**

This command will:

* Read your development plan from `specs/interview-dashboard.md`
* Create 3 parallel subagents using Claude Code's Task tool
* Each agent works independently in their own worktree
* Generate isolated versions of your feature

#### Step 4: Compare and Test Results

Create a helper script `start-parallel-clients.sh` to run all versions:

Run the script:

#### Step 5: Merge the Best Version

After comparing all versions:

##### **Clean Up Worktrees**

For more details on git worktree management, see the [official git worktree documentation](https://git-scm.com/docs/git-worktree).

#### Advanced: Managing Custom Commands

##### **Command Organization**

You can organize commands in subdirectories:

##### **Using Arguments Effectively**

Create flexible commands with `$ARGUMENTS`:

`.claude/commands/setup-feature.md`:

Usage:

#### Summary: Advanced Agentic Workflows

This approach gives you:

* **Custom slash commands** for repeatable workflows
* **Variable system** for flexible automation
* **Parallel subagent execution** using Claude Code's Task tool
* **Isolated environments** with git worktrees
* **Multiple implementation perspectives** to choose from

This is **agentic engineering at scale**—not just generating code, but orchestrating multiple AI agents to explore different solutions in parallel.

Huge credit to [@disler](https://github.com/disler) for his video here [video demonstration](https://youtube.com/watch?v=f8RnRuaxee8&t=1454s) showing a complete parallel development process.

#### Final Thoughts

With Claude Code's custom command system and git worktrees, you're not just prompting. You're **engineering** with AI tools at scale. This workflow gives you **compute-level parallelism** to ship faster and better.

>  *"Don't just generate code. Multiply AI creativity—and choose the one that matches your vision."*
> 
>  

The custom command system makes this workflow repeatable, shareable, and scalable across your entire team.

Happy shipping.

*Want to learn more about advanced AI coding workflows? This technique combines Claude Code's custom commands with git's powerful worktree feature to enable true parallel development.*
