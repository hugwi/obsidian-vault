---
title: "How I Built an AI Documentation Engine with Tree-sitter, Claude AI, and RAG"
source: "https://dev.to/liztacular/how-i-built-an-ai-documentation-engine-with-tree-sitter-claude-ai-and-rag-4jgk"
author: "Elizabeth Stein"
published: 2026-03-03
created: 2026-04-12
description: "Documentation is every developer’s least favorite task.  We all agree it’s"
tags:
  - to-process
  - agent-tools
---

Documentation is every developer’s least favorite task.


We all agree it’s important. We all intend to keep it updated. And yet… it’s usually the first thing to fall behind.


After watching this happen on every team I’ve worked with, I built **AutomaDocs** — an AI-powered documentation engine that connects to your GitHub repos and keeps docs in sync automatically.


Here’s how the system works and what I learned building it.


##  The Real Problem


Every engineering team has had this conversation:


* PM: “Are the docs updated?”
* Dev: “Uh… mostly.”
* PM: “The API endpoint changed last week.”
* Dev: “…I’ll update them tomorrow.”


The issue isn’t laziness. It’s architecture.


We treat documentation as a *separate artifact* from the code — but the code changes constantly. Keeping two parallel systems in sync manually doesn’t scale.


So I asked:



>  What if documentation wasn’t written manually at all?  
>   
>  What if it was generated directly from structured code understanding?
> 
>  


That became AutomaDocs.


#  The Architecture


AutomaDocs has three core layers:


1. **Structured code analysis**
2. **LLM-powered documentation generation**
3. **Continuous sync + retrieval (RAG)**


Let’s break it down.


##  1. Code Analysis with :contentReference[oaicite:0]{index=0}


Most AI documentation tools just feed raw source code into an LLM.


That works… but it’s noisy and unreliable.


Instead, I parse repositories into an **Abstract Syntax Tree (AST)** using Tree-sitter. This gives structured, language-aware understanding of the codebase:


* Function signatures with parameters and return types
* Class hierarchies
* Import/export graphs
* Docstring extraction
* Type information


Instead of seeing “text,” the AI sees structured architecture.


Example output:



```
{
  type: "function_declaration",
  name: "createUser",
  parameters: [
    { name: "email", type: "string" },
    { name: "role", type: "UserRole" }
  ],
  returnType: "Promise<User>",
  docstring: "Creates a new user account"
}

```

That structure dramatically improves documentation quality compared to raw code prompts.


**Key insight:**


LLMs perform significantly better when you reduce ambiguity before prompting them.


##  2. AI Generation with :contentReference[oaicite:1]{index=1}


Once we have structured AST data, we feed it into Claude with carefully designed prompts.


The system generates:


* API endpoint documentation
* Method/function descriptions
* Parameter breakdowns with types
* Usage examples
* High-level architecture summaries


Because the input is structured, the output is:


* More consistent
* Less hallucinated
* Easier to regenerate deterministically


This separation — *parser for understanding, LLM for explanation* — keeps responsibilities clean.


##  3. Auto-Sync with :contentReference[oaicite:2]{index=2} Webhooks + RAG


Documentation should never be stale.


Here’s what happens when you push code:


1. GitHub webhook fires
2. We detect changed files
3. Tree-sitter re-parses only affected nodes
4. Claude regenerates relevant documentation
5. Embeddings update in :contentReference[oaicite:3]{index=3}


Your docs are never more than one push behind your code.


No manual updates required.


#  The RAG Chat System


We also built an AI chat interface over your documentation.


Instead of basic vector search, we implemented **hybrid retrieval**:


* **BM25** → precise keyword matching (function names, error codes)
* Pinecone → semantic search (conceptual questions)
* **Reciprocal Rank Fusion (RRF)** → combines both ranking systems


That means users can ask:



>  “How does authentication work?”
> 
>  


Even if the word *authentication* doesn’t appear directly in code, the system still finds relevant logic, middleware, or config.


Hybrid search dramatically improves answer quality compared to pure embeddings.


#  Tech Stack




| Component | Technology |
| --- | --- |
| Frontend | Next.js 16 (App Router) |
| Backend | Express (ES Modules) |
| Database | PostgreSQL |
| Vector DB | Pinecone |
| AI | Claude (Anthropic) |
| Parser | Tree-sitter |
| Queue | BullMQ + Redis |
| Hosting | Vercel + Railway |


The biggest architectural decision was separating:


* **Parsing layer**
* **Generation layer**
* **Retrieval layer**


Keeping those decoupled made iteration much faster.


#  What I’d Do Differently


###  1. Start with fewer languages


Supporting 15+ languages from day one was overly ambitious.


If I rebuilt it today, I’d focus on:


* JavaScript / TypeScript
* Python


Nail those first. Expand later.


###  2. Build “Documentation Health Scores” earlier


We added a documentation health scoring system later — and surprisingly, it became one of the most loved features.


Gamification works.


Teams are far more likely to maintain docs when they can see:


* Coverage %
* Outdated endpoints
* Missing descriptions


If I were starting again, this would be v1.


###  3. Use WebSockets instead of polling


We currently poll for generation status updates.


WebSockets would make the system cleaner and more real-time.


Classic v1 tradeoff: ship now, refine later.


#  Lessons from Building AI Dev Tools


A few high-level takeaways:


* **Structured input > clever prompts**
* Retrieval quality matters more than model size
* Dev tools succeed when they reduce friction, not add AI novelty
* Automation only works if it’s invisible


AI is powerful — but only when wrapped in good architecture.


#  Try It


AutomaDocs is live with a free tier:


* 3 repositories
* 20 AI generations/month


👉 **<https://automadocs.com>**


I’d genuinely love feedback from the dev.to community:


**What’s your biggest documentation pain point right now?**