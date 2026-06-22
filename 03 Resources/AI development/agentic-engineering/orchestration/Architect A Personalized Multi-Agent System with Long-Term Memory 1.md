---
title: "Architect A Personalized Multi-Agent System with Long-Term Memory"
source: "https://dev.to/googleai/architect-a-personalized-multi-agent-system-with-long-term-memory-3o15?bb=263439"
author:
  - "[[dev.to]]"
published: 2026-05-07
created: 2026-06-12
description: "In support of our mission to accelerate the developer journey on Google Cloud, we built Dev Signal —... Tagged with ai, googlecloud, agents, mcp."
tags:
  - "to-process"
  - orchestration
---
In support of our mission to accelerate the developer journey on Google Cloud, we built **Dev Signal** — a multi-agent system designed to transform raw community signals into reliable technical guidance by automating the path from discovery to expert creation.

In the [first part](https://dev.to/googleai/building-capabilities-for-a-multi-agent-system-with-google-adk-mcp-and-cloud-run-ab9) of this series for the **Dev Signal**, we laid the essential groundwork for this system by establishing a project environment and equipping core capabilities through the Model Context Protocol (MCP). We standardized our external integrations, connecting to Reddit for trend discovery, Google Cloud Docs for technical grounding, and building a custom Nano Banana Pro MCP server for multimodal image generation. If you missed [Part 1](https://dev.to/googleai/building-capabilities-for-a-multi-agent-system-with-google-adk-mcp-and-cloud-run-ab9) or want to explore the code directly, you can find the complete project implementation in our [GitHub repository](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/dev-signal).

Now, in Part 2, we focus on building the multi-agent architecture and integrating the [Vertex AI memory bank](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview) to personalize these capabilities. We will implement a Root Orchestrator that manages three specialist agents: the Reddit Scanner, GCP Expert, and Blog Drafter, to provide a seamless flow from trend discovery to expert content creation. We will also integrate a long-term memory layer that enables the agent to learn from your feedback and persist your stylistic preferences across different conversations. This ensures that Dev Signal doesn't just process data, but actually learns to match your professional voice over time.

## Infrastructure and Model Setup

First, we initialize the environment and the shared Gemini model.

Paste this code in `dev_signal_agent/agent.py`:

```
from google.adk.agents import Agent
from google.adk.apps import App
from google.adk.models import Gemini
from google.adk.tools import google_search, AgentTool, load_memory_tool, preload_memory_tool
from google.adk.tools.tool_context import ToolContext
from google.genai import types
from dev_signal_agent.app_utils.env import init_environment
from dev_signal_agent.tools.mcp_config import (
    get_reddit_mcp_toolset,
    get_dk_mcp_toolset,
    get_nano_banana_mcp_toolset
)

PROJECT_ID, MODEL_LOC, SERVICE_LOC, SECRETS = init_environment()

shared_model = Gemini(
    model="gemini-3-flash-preview",
    vertexai=True,
    project=PROJECT_ID,
    location=MODEL_LOC,
    retry_options=types.HttpRetryOptions(attempts=3),
)
```

## Memory Ingestion Logic

We want Dev Signal to do more than just follow instructions — we want it to learn from you. By capturing your preferences, such as specific technical interests on Reddit or a preferred blogging style, the agent can personalize its output for future use. To achieve this, we use the [**Vertex AI memory bank**](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview) to persist session history across different conversations.

### Long-term Memory

We automate this through the `save_session_to_memory_callback` function. This callback is configured to run automatically after every turn, ensuring that session details are captured and stored in the memory bank without manual intervention.

#### How Managed Memory Works:

- **Ingestion**: The `save_session_to_memory_callback` sends the conversation data to Vertex AI.
- **Embedding**: Vertex AI converts the text into numerical vectors (embeddings) that capture the semantic meaning of your preferences.
- **Storage**: These vectors are stored in a managed index, enabling the agent to perform semantic searches and retrieve relevant history in future sessions.
- **Retrieval**: The agent recalls this history using built-in ADK tools. The PreloadMemoryTool proactively brings in context at the start of an interaction, while the LoadMemoryTool allows the agent to fetch specific memories on an as-needed basis.

Paste this code in `dev_signal_agent/agent.py`:

```python
async def save_session_to_memory_callback(*args, **kwargs) -> None:
    """
    Defensive callback to persist session history to the Vertex AI memory bank.
    """
    ctx = kwargs.get("callback_context") or (args[0] if args else None)
    # Check connection to Memory Service
    if ctx and hasattr(ctx, "_invocation_context") and ctx._invocation_context.memory_service:
        # Save the session!
        await ctx._invocation_context.memory_service.add_session_to_memory(
            ctx._invocation_context.session
        )
```

### Short-term Memory

The `add_info_to_state` function serves as the agent's short-term working memory, allowing the `gcp_expert` to reliably hand off its detailed findings to the `blog_drafter` within the same session. This working memory and the conversation transcript are managed by the Vertex AI Session Service to ensure that active context survives server restarts or transient failures.

**The boundary between session-based state and long-term persistence** — It is important to note that while this service provides stability during an active interaction, this short-term memory does not persist between different sessions. Starting a fresh session ID effectively resets this working state, ensuring a clean slate for new tasks. Cross-session continuity, where the agent remembers your stylistic preferences or past feedback, is handled by the Vertex AI Memory Bank.

Paste this code in `dev_signal_agent/agent.py`

```python
def add_info_to_state(tool_context: ToolContext, key: str, data: str) -> dict:
    tool_context.state[key] = data
    return {"status": "success", "message": f"Saved '{key}' to state."}
```

## Specialist 1: Reddit Scanner (Discovery)

The Reddit Scanner is our "Trend Spotter," it identifies high-engagement questions from the last 21 days (3 weeks) to ensure that all research findings remain both timely and relevant.

**Memory Usage:** It leverages `load_memory` to retrieve your past areas of interest and preferred topics from the Vertex AI memory bank. If relevant history exists, the agent prioritizes those specific topics in its search to provide a personalized discovery experience.

Beyond simple retrieval, each sub-agent actively updates its memories by listening for new preferences and explicitly acknowledging them during the chat. This process captures relevant information in the session history, where an automated callback then persists it to the long-term Vertex AI memory bank for future use.

This memory management is supported by two distinct retrieval patterns within the Google Agent Development Kit (ADK). The first is the `PreloadMemoryTool`, which proactively brings in historical context at the beginning of every interaction to ensure the agent is fully briefed before addressing the current request. The second is the `LoadMemoryTool`, which the agent uses on an as-needed basis, calling upon it only when it decides that deeper past knowledge would be beneficial for the current step in the workflow.

Paste this code in `dev_signal_agent/agent.py`

```
# Singleton toolsets
reddit_mcp = get_reddit_mcp_toolset(
    client_id=SECRETS.get("REDDIT_CLIENT_ID", ""),
    client_secret=SECRETS.get("REDDIT_CLIENT_SECRET", ""),
    user_agent=SECRETS.get("REDDIT_USER_AGENT", "")
)

reddit_scanner = Agent(
    name="reddit_scanner",
    model=shared_model,
    instruction="""
You are a Reddit research specialist. Your goal is to identify high-engagement questions
from the last 3 weeks on specific topics of interest, such as AI/agents on Cloud Run.

Follow these steps:
1. **MEMORY CHECK**: Use \`load_memory\` to retrieve the user's **past areas of interest** and **preferred topics**. Calibrate your search to align with these interests.
2. Use the Reddit MCP tools to search for relevant subreddits and posts.
3. Filter results for posts created within the last 21 days (3 weeks).
4. Analyze "high-engagement" based on upvote counts and the number of comments.
5. Recommend the most important and relevant questions for a technical audience.
6. **CRITICAL**: For each recommended question, provide a direct link to the original thread and a concise summary of the discussion.
7. **CAPTURE PREFERENCES**: Actively listen for user preferences, interests, or project details. Explicitly acknowledge them to ensure they are captured in the session history for future personalization.
""",
    tools=[reddit_mcp, load_memory_tool.LoadMemoryTool()],
    after_agent_callback=save_session_to_memory_callback,
)
```

## Specialist 2: GCP Expert (Grounding)

The GCP Expert is our "Technical Authority". It triangulates facts by synthesizing official documentation from the Google Cloud Developer Knowledge MCP Server, community sentiment from Reddit, and broader context from Google Search.

Paste this code in `dev_signal_agent/agent.py`

```
dk_mcp = get_dk_mcp_toolset(api_key=SECRETS.get("DK_API_KEY", ""))

search_agent = Agent(
    name="search_agent",
    model=shared_model,
    instruction="Execute Google Searches and return raw, structured results (Title, Link, Snippet).",
    tools=[google_search],
)

gcp_expert = Agent(
    name="gcp_expert",
    model=shared_model,
    instruction="""
You are a Google Cloud Platform (GCP) documentation expert.
Your goal is to provide accurate, detailed, and cited answers to technical questions by synthesizing official documentation with community insights.

For EVERY technical question, you MUST perform a comprehensive research sweep using ALL available tools:
1. **Official Docs (Grounding)**: Use DeveloperKnowledge MCP (\`search_documents\`) to find the definitive technical facts.
2. **Social Media Research (Reddit)**: Use the Reddit MCP to research the question on social media. This allows you to find real-world user discussions, common pain points, or alternative solutions that might not be in official documentation.
3. **Broader Context (Web/Social)**: Use the \`search_agent\` tool to find recent technical blogs, social media discussions, or tutorials.

Synthesize your answer:
- Start with the official answer based on GCP docs.
- Add "Social Media Insights" or "Common Issues" sections derived from Reddit and Web Search findings.
- **CRITICAL**: After providing your answer, you MUST use the \`add_info_to_state\` tool to save your full technical response under the key: \`technical_research_findings\`.
- Cite your sources specifically at the end of your response, providing **direct links** (URLs) to the official documentation, blog posts, and Reddit threads used.
- **CAPTURE PREFERENCES**: Actively listen for user preferences, interests, or project details. Explicitly acknowledge them to ensure they are captured in the session history for future personalization.
""",
    tools=[dk_mcp, AgentTool(search_agent), reddit_mcp, add_info_to_state],
    after_agent_callback=save_session_to_memory_callback,
)
```

## Specialist 3: Blog Drafter (Creativity)

The Blog Drafter is our Content Creator. It drafts the blog based on the expert's findings and offers to generate visuals.

**Memory Usage:** It checks `load_memory` for the user's **preferred writing style** (e.g. "Witty", "Rap") stored in the **Vertex AI memory bank**.

Paste this code in `dev_signal_agent/agent.py`

```
nano_mcp = get_nano_banana_mcp_toolset()

blog_drafter = Agent(
    name="blog_drafter",
    model=shared_model,
    instruction="""
You are a professional technical blogger specializing in Google Cloud Platform.
Your goal is to draft high-quality blog posts based on technical research provided by the GDE expert and reliable documentation.

You have access to the research findings from the gcp_expert_agent here:
{{ technical_research_findings }}

Follow these steps:
1. **MEMORY CHECK**: Use \`load_memory\` to retrieve past blog posts, **areas of interest**, and user feedback on writing style. Adopt the user's preferred style and depth.
2. **REVIEW & GROUND**: Review the technical research findings provided above. **CRITICAL**: Use the \`dk_mcp\` (Developer Knowledge) tool to verify key facts, technical limitations, and API details. Ensure every claim in your blog is grounded in official documentation.
3. Draft a blog post that is engaging, accurate, and helpful for a technical audience.
4. Include code snippets or architectural diagrams if relevant.
5. Provide a "Resources" section with links to the official documentation used.
6. Ensure the tone is professional yet accessible, while adhering to any style preferences found in memory.
7. **VISUALS**: After presenting the drafted blog post, explicitly ask the user: "Would you like me to generate an infographic-style header image to illustrate these key points?" If they agree, use the \`generate_image\` tool (Nano Banana).
8. **CAPTURE PREFERENCES**: Actively listen for user preferences, interests, or project details. Explicitly acknowledge them to ensure they are captured in the session history for future personalization.
""",
    tools=[dk_mcp, load_memory_tool.LoadMemoryTool(), nano_mcp],
    after_agent_callback=save_session_to_memory_callback,
)
```

## The Root Orchestrator

The root agent serves as the system's strategist, managing a team of specialist agents and orchestrating their actions based on the specific goals provided by the user. At the start of a conversation, the orchestrator retrieves memory to establish context by checking for the user's past areas of interest, preferred topics, or previous projects.

Paste this code in `dev_signal_agent/agent.py`

```
root_agent = Agent(
    name="root_orchestrator",
    model=shared_model,
    instruction="""
You are a technical content strategist. You manage three specialists:
1. reddit_scanner: Finds trending questions and high-engagement topics on Reddit.
2. gcp_expert: Provides technical answers based on official GCP documentation.
3. blog_drafter: Writes professional blog posts based on technical research.

Your responsibilities:
- **MEMORY CHECK**: At the start of a conversation, use \`load_memory\` to check if the user has specific **areas of interest**, preferred topics, or past projects. Tailor your suggestions accordingly.
- **CAPTURE PREFERENCES**: Actively listen for user preferences, interests, or project details. Explicitly acknowledge them to ensure they are captured in the session history for future personalization.
- If the user wants to find trending topics or questions from Reddit, delegate to reddit_scanner.
- If the user has a technical question or wants to research a specific theme, delegate to gcp_expert.
- **CRITICAL**: After the gcp_expert provides an answer, you MUST ask the user:
  "Would you like me to draft a technical blog post based on this answer?"
- If the user agrees or asks to write a blog, delegate to blog_drafter.
- Be proactive in helping the user navigate from discovery (Reddit) to research (Docs) to content creation (Blog).
""",
    tools=[load_memory_tool.LoadMemoryTool(), preload_memory_tool.PreloadMemoryTool()],
    after_agent_callback=save_session_to_memory_callback,
    sub_agents=[reddit_scanner, gcp_expert, blog_drafter]
)

app = App(root_agent=root_agent, name="dev_signal_agent")
```

## Summary

In this part of our series, we built multi-agent architecture and implemented a robust, dual-layered memory system. We established a Root Orchestrator, managing three specialist agents: a Reddit Scanner for trend discovery, a GCP Expert for technical grounding, and a Blog Drafter for creative content creation.

By utilizing short-term state to pass information reliably between specialists and integrating the Vertex AI memory bank for long-term persistence, we've enabled the agent to learn from your feedback and remember specific writing styles across different conversations.

In [Part 3](https://dev.to/googleai/local-testing-of-a-multi-agent-system-with-memory-37mm), we will show you how to test the agent locally to verify these components on your workstation, before transitioning to a full production deployment on Google Cloud Run in Part 4. Can't wait for part 3? The full implementation is already available for you to explore on [GitHub](https://github.com/GoogleCloudPlatform/devrel-demos/tree/main/ai-ml/dev-signal).

To learn more about the underlying technology, explore the [Vertex AI Memory Bank overview](https://docs.cloud.google.com/agent-builder/agent-engine/memory-bank/overview) or dive into the official [ADK Documentation](https://docs.cloud.google.com/agent-builder/agent-development-kit/overview) to see how to orchestrate complex multi-agent workflows.

***Special thanks to [Remigiusz Samborski](https://www.linkedin.com/in/remigiusz-samborski/) for the helpful review and feedback on this article.***

For more content like this, follow me on [LinkedIn](https://www.linkedin.com/in/shirmeirlador/) and [X](https://x.com/shirmeir86?lang=en).

[MongoDB](https://dev.to/mongodb)

Promoted

[![Gen AI apps are built with MongoDB Atlas](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fi.imgur.com%2FlGiI0TQ.png)](https://www.mongodb.com/cloud/atlas/lp/try3?utm_campaign=display_devto-broad_pl_flighted_atlas_tryatlaslp_prosp_gic-null_ww-all_dev_dv-all_eng_leadgen&utm_source=devto&utm_medium=display&utm_content=airevolution-v1&bb=241241)

## Gen AI apps are built with MongoDB Atlas

MongoDB Atlas is the developer-friendly database for building, scaling, and running gen AI & LLM apps—no separate vector DB needed. Enjoy native vector search, 115+ regions, and flexible document modeling. Build AI faster, all in one place.