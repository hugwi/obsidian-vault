# browser-use/browser-use: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.

![rw-book-cover](https://repository-images.githubusercontent.com/881458615/fddb1de9-5742-4037-8ea9-bf8f1cfd2f58)

## Metadata
- Author: [[https://github.com/browser-use/]]
- Full Title: browser-use/browser-use: 🌐 Make websites accessible for AI agents. Automate tasks online with ease.
- Category: #articles
- Summary: Browser-Use is an open-source tool that helps AI agents automate tasks on websites easily. It offers both self-hosted and cloud options for scalable, stealthy browser automation. Users can quickly set up and run agents to perform tasks like form-filling, shopping, and personal assistance.
- URL: https://github.com/browser-use/browser-use

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/browser-use/browser-use?resume=1) 

#### Create list

### browser-use/browser-use

main

tT

Go to file

Code

Open more actions menu

   ![Shows a black Browser Use Logo in light color mode and a white one in dark color mode.](https://github.com/user-attachments/assets/2ccdb752-22fb-41c7-8948-857fc1ad7e24) 
   ![The AI browser agent.](https://github.com/user-attachments/assets/9955dda9-ede3-4971-8ee0-91cbc3850125) 
[![Browser-Use Package Download Statistics](https://camo.githubusercontent.com/f67549cea6229347ae19319784e0bbd39a6f987cab1d48cd464017f02e955a04/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f7061636b616765)](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-downloads)
[![Demos](https://camo.githubusercontent.com/7e9025c343a4acd95c54d84d83b23f875323ee3f58cb4ec2c764f4c07c7835e7/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f64656d6f73)](https://github.com/browser-use/browser-use/#demos)
[![Docs](https://camo.githubusercontent.com/da24e49e145642fb3a3fe1910e856d59d6da1491afd35998b8624f6732262f49/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f646f6373)](https://docs.browser-use.com)
[![Blog](https://camo.githubusercontent.com/f59d6529dd474485d76d72dfa57622e93de03c2f2147d15645f237057d6ac1e2/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f626c6f67)](https://browser-use.com/posts)
[![Merch](https://camo.githubusercontent.com/6854add877f53678eb94c1903d14b88427b87dfcbc7b46fa04d9023826b4c2c2/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f6d65726368)](https://browsermerch.com)
[![Github Stars](https://camo.githubusercontent.com/6b321c4c3a0fe9ebd185f7e1ed0c34908ed763b0670359685038826220fa0c73/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f676974687562)](https://github.com/browser-use/browser-use)
[![Twitter](https://camo.githubusercontent.com/0c0d368a2b84e6c55dfa4b61dfcc6b20fc79911ddac2890188b6f5aa4d9e1ff9/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f74776974746572)](https://x.com/intent/user?screen_name=browser_use)
[![Discord](https://camo.githubusercontent.com/4924db0665fc88bd7ed197fa3535511406743b1025c5086a32e252a613ad1176/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f646973636f7264)](https://link.browser-use.com/discord)
[![Browser-Use Cloud](https://camo.githubusercontent.com/af449ec43f198f27fd42b59996473270e5dd2eeb482196bfca572ee48a2afbcc/68747470733a2f2f6d656469612e62726f777365722d7573652e746f6f6c732f6261646765732f636c6f7564)](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-badge-cloud)
🌤️ Want to skip the setup? Use our **[cloud](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-skip-setup)** for faster, scalable, stealth-enabled browser automation!

### 🤖 LLM Quickstart

1. Direct your favorite coding agent (Cursor, Claude Code, etc) to [Agents.md](https://docs.browser-use.com/llms-full.txt)
2. Prompt away!

### 👋 Human Quickstart

**1. Create environment and install Browser-Use with [uv](https://docs.astral.sh/uv/) (Python>=3.11):**

```
uv init && uv add browser-use && uv sync
# uvx browser-use install  # Run if you don't have Chromium installed
```

**2. [Optional] Get your API key from [Browser Use Cloud](https://cloud.browser-use.com/new-api-key?utm_source=github&utm_medium=readme-quickstart-api-key):**

```
# .env
BROWSER_USE_API_KEY=your-key
# GOOGLE_API_KEY=your-key
# ANTHROPIC_API_KEY=your-key

```

**3. Run your first agent:**

```
from browser_use import Agent, Browser, ChatBrowserUse
# from browser_use import ChatGoogle  # ChatGoogle(model='gemini-3-flash-preview')
# from browser_use import ChatAnthropic  # ChatAnthropic(model='claude-sonnet-4-6')
import asyncio

async def main():
    browser = Browser(
        # use_cloud=True,  # Use a stealth browser on Browser Use Cloud
    )

    agent = Agent(
        task="Find the number of stars of the browser-use repo",
        llm=ChatBrowserUse(),
        # llm=ChatGoogle(model='gemini-3-flash-preview'),
        # llm=ChatAnthropic(model='claude-sonnet-4-6'),
        browser=browser,
    )
    await agent.run()

if __name__ == "__main__":
    asyncio.run(main())
```

Check out the [library docs](https://docs.browser-use.com/open-source/introduction) and the [cloud docs](https://docs.cloud.browser-use.com?utm_source=github&utm_medium=readme-cloud-docs) for more!

### Open Source vs Cloud

   ![BU Bench V1 - LLM Success Rates](https://github.com/browser-use/browser-use/raw/main/static/accuracy_by_model_light.png) 
We benchmark Browser Use across 100 real-world browser tasks. Full benchmark is open source: **[browser-use/benchmark](https://github.com/browser-use/benchmark)**.

**Use the Open-Source Agent**

* You need [custom tools](https://docs.browser-use.com/customize/tools/basics) or deep code-level integration
* We recommend pairing with our [cloud browsers](https://docs.browser-use.com/open-source/customize/browser/remote) for leading stealth, proxy rotation, and scaling
* Or self-host the open-source agent fully on your own machines

**Use the [Fully-Hosted Cloud Agent](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-hosted-agent) (recommended)**

* Much more powerful agent for complex tasks (see plot above)
* Easiest way to start and scale
* Best stealth with proxy rotation and captcha solving
* 1000+ integrations (Gmail, Slack, Notion, and more)
* Persistent filesystem and memory

### Demos

##### 📋 Form-Filling

###### Task = "Fill in this job application with my resume and information."

[![Job Application Demo](https://private-user-images.githubusercontent.com/43824272/501209081-57865ee6-6004-49d5-b2c2-6dff39ec2ba9.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2NDUyODcsIm5iZiI6MTc3OTY0NDk4NywicGF0aCI6Ii80MzgyNDI3Mi81MDEyMDkwODEtNTc4NjVlZTYtNjAwNC00OWQ1LWIyYzItNmRmZjM5ZWMyYmE5LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTI0VDE3NDk0N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRkNmM2ZjIzZWI5ZjkwZjM1MzdmZmZmZmM1NDFjMGU1OWM1YmZjYzkyMjc1NDAyNTg4ZDdkYjc4NzFlNjI5MmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRmdpZiJ9.sRREQ9Th5hxLAOLXeH5FBxKwpe7XkhkHqVdbjNxSH9Y)](https://private-user-images.githubusercontent.com/43824272/501209081-57865ee6-6004-49d5-b2c2-6dff39ec2ba9.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2NDUyODcsIm5iZiI6MTc3OTY0NDk4NywicGF0aCI6Ii80MzgyNDI3Mi81MDEyMDkwODEtNTc4NjVlZTYtNjAwNC00OWQ1LWIyYzItNmRmZjM5ZWMyYmE5LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTI0VDE3NDk0N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRkNmM2ZjIzZWI5ZjkwZjM1MzdmZmZmZmM1NDFjMGU1OWM1YmZjYzkyMjc1NDAyNTg4ZDdkYjc4NzFlNjI5MmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRmdpZiJ9.sRREQ9Th5hxLAOLXeH5FBxKwpe7XkhkHqVdbjNxSH9Y)
  [![Job Application Demo](https://private-user-images.githubusercontent.com/43824272/501209081-57865ee6-6004-49d5-b2c2-6dff39ec2ba9.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2NDUyODcsIm5iZiI6MTc3OTY0NDk4NywicGF0aCI6Ii80MzgyNDI3Mi81MDEyMDkwODEtNTc4NjVlZTYtNjAwNC00OWQ1LWIyYzItNmRmZjM5ZWMyYmE5LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTI0VDE3NDk0N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRkNmM2ZjIzZWI5ZjkwZjM1MzdmZmZmZmM1NDFjMGU1OWM1YmZjYzkyMjc1NDAyNTg4ZDdkYjc4NzFlNjI5MmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRmdpZiJ9.sRREQ9Th5hxLAOLXeH5FBxKwpe7XkhkHqVdbjNxSH9Y)](https://private-user-images.githubusercontent.com/43824272/501209081-57865ee6-6004-49d5-b2c2-6dff39ec2ba9.gif?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2NDUyODcsIm5iZiI6MTc3OTY0NDk4NywicGF0aCI6Ii80MzgyNDI3Mi81MDEyMDkwODEtNTc4NjVlZTYtNjAwNC00OWQ1LWIyYzItNmRmZjM5ZWMyYmE5LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNjA1MjQlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjYwNTI0VDE3NDk0N1omWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTRkNmM2ZjIzZWI5ZjkwZjM1MzdmZmZmZmM1NDFjMGU1OWM1YmZjYzkyMjc1NDAyNTg4ZDdkYjc4NzFlNjI5MmQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JnJlc3BvbnNlLWNvbnRlbnQtdHlwZT1pbWFnZSUyRmdpZiJ9.sRREQ9Th5hxLAOLXeH5FBxKwpe7XkhkHqVdbjNxSH9Y)  [Example code ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/apply_to_job.py)

##### 🍎 Grocery-Shopping

###### Task = "Put this list of items into my instacart."

  grocery-use-large.mp4    
[Example code ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/buy_groceries.py)

##### 💻 Personal-Assistant.

###### Task = "Help me find parts for a custom PC."

  pc-use-large.mp4    
[Example code ↗](https://github.com/browser-use/browser-use/blob/main/examples/use-cases/pcpartpicker.py)

##### 💡See [more examples here ↗](https://docs.browser-use.com/examples) and give us a star!

### 🚀 Template Quickstart

**Want to get started even faster?** Generate a ready-to-run template:

```
uvx browser-use init --template default
```

This creates a `browser_use_default.py` file with a working example. Available templates:

* `default` - Minimal setup to get started quickly
* `advanced` - All configuration options with detailed comments
* `tools` - Examples of custom tools and extending the agent

You can also specify a custom output path:

```
uvx browser-use init --template default --output my_agent.py
```

### 💻 CLI

Fast, persistent browser automation from the command line:

```
browser-use open https://example.com    # Navigate to URL
browser-use state                       # See clickable elements
browser-use click 5                     # Click element by index
browser-use type "Hello"                # Type text
browser-use screenshot page.png         # Take screenshot
browser-use close                       # Close browser
```

The CLI keeps the browser running between commands for fast iteration. See [CLI docs](https://github.com/browser-use/browser-use/blob/main/browser_use/skill_cli/README.md) for all commands.

##### Claude Code Skill

For [Claude Code](https://claude.ai/code), install the skill to enable AI-assisted browser automation:

```
mkdir -p ~/.claude/skills/browser-use
curl -o ~/.claude/skills/browser-use/SKILL.md \
  https://raw.githubusercontent.com/browser-use/browser-use/main/skills/browser-use/SKILL.md
```

#### Integrations, hosting, custom tools, MCP, and more on our [Docs ↗](https://docs.browser-use.com)

### FAQ

 **What's the best model to use?** We optimized **ChatBrowserUse()** specifically for browser automation tasks. On avg it completes tasks 3-5x faster than other models with SOTA accuracy.

 **Pricing (per 1M tokens):**

 * Input tokens: $0.20
* Cached input tokens: $0.02
* Output tokens: $2.00

 For other LLM providers, see our [supported models documentation](https://docs.browser-use.com/supported-models).

 
 **Should I use the Browser Use system prompt with the open-source preview model?** Yes. If you use `ChatBrowserUse(model='browser-use/bu-30b-a3b-preview')` with a normal `Agent(...)`, Browser Use still sends its default agent system prompt for you.

 You do **not** need to add a separate custom "Browser Use system message" just because you switched to the open-source preview model. Only use `extend_system_message` or `override_system_message` when you intentionally want to customize the default behavior for your task.

 If you want the best default speed/accuracy, we still recommend the newer hosted `bu-*` models. If you want the open-source preview model, the setup stays the same apart from the `model=` value.

 
 **Can I use custom tools with the agent?** Yes! You can add custom tools to extend the agent's capabilities:

 
```
from browser_use import Tools

tools = Tools()

@tools.action(description='Description of what this tool does.')
def custom_tool(param: str) -> str:
    return f"Result: {param}"

agent = Agent(
    task="Your task",
    llm=llm,
    browser=browser,
    tools=tools,
)
```
 
 **Can I use this for free?** Yes! Browser-Use is open source and free to use. You only need to choose an LLM provider (like OpenAI, Google, ChatBrowserUse, or run local models with Ollama).

 
 **Terms of Service** This open-source library is licensed under the MIT License. For Browser Use services & data policy, see our [Terms of Service](https://browser-use.com/legal/terms-of-service) and [Privacy Policy](https://browser-use.com/privacy/).

 
 **How do I handle authentication?** Check out our authentication examples:

 * [Using real browser profiles](https://github.com/browser-use/browser-use/blob/main/examples/browser/real_browser.py) - Reuse your existing Chrome profile with saved logins
* If you want to use temporary accounts with inbox, choose AgentMail
* To sync your auth profile with the remote browser, run `curl -fsSL https://browser-use.com/profile.sh | BROWSER_USE_API_KEY=XXXX sh` (replace XXXX with your API key)

 These examples show how to maintain sessions and handle authentication seamlessly.

 
 **How do I solve CAPTCHAs?** For CAPTCHA handling, you need better browser fingerprinting and proxies. Use [Browser Use Cloud](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-faq-captcha) which provides stealth browsers designed to avoid detection and CAPTCHA challenges.

 
 **How do I go into production?** Chrome can consume a lot of memory, and running many agents in parallel can be tricky to manage.

 For production use cases, use our [Browser Use Cloud API](https://cloud.browser-use.com?utm_source=github&utm_medium=readme-faq-production) which handles:

 * Scalable browser infrastructure
* Memory management
* Proxy rotation
* Stealth browser fingerprinting
* High-performance parallel execution

 
**Tell your computer what to do, and it gets it done.**

[![](https://private-user-images.githubusercontent.com/67061560/425692580-06fa3078-8461-4560-b434-445510c1766f.jpeg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2NDUyODcsIm5iZiI6MTc3OTY0NDk4NywicGF0aCI6Ii82NzA2MTU2MC80MjU2OTI1ODAtMDZmYTMwNzgtODQ2MS00NTYwLWI0MzQtNDQ1NTEwYzE3NjZmLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUyNFQxNzQ5NDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jZDMwMTU4ZDNlNDVjNTgxZDY0YzExYWY5MmJkNjdmMWUzZjAxZGFiYjQyMmVmZDVlZjcxODU5MGZjYzVlOWVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0.UGTRPGax1gRv5CXdeZm0yXan-fBu85sggRexy7f2TXg)](https://private-user-images.githubusercontent.com/67061560/425692580-06fa3078-8461-4560-b434-445510c1766f.jpeg?jwt=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3Nzk2NDUyODcsIm5iZiI6MTc3OTY0NDk4NywicGF0aCI6Ii82NzA2MTU2MC80MjU2OTI1ODAtMDZmYTMwNzgtODQ2MS00NTYwLWI0MzQtNDQ1NTEwYzE3NjZmLmpwZWc_WC1BbXotQWxnb3JpdGhtPUFXUzQtSE1BQy1TSEEyNTYmWC1BbXotQ3JlZGVudGlhbD1BS0lBVkNPRFlMU0E1M1BRSzRaQSUyRjIwMjYwNTI0JTJGdXMtZWFzdC0xJTJGczMlMkZhd3M0X3JlcXVlc3QmWC1BbXotRGF0ZT0yMDI2MDUyNFQxNzQ5NDdaJlgtQW16LUV4cGlyZXM9MzAwJlgtQW16LVNpZ25hdHVyZT1jZDMwMTU4ZDNlNDVjNTgxZDY0YzExYWY5MmJkNjdmMWUzZjAxZGFiYjQyMmVmZDVlZjcxODU5MGZjYzVlOWVmJlgtQW16LVNpZ25lZEhlYWRlcnM9aG9zdCZyZXNwb25zZS1jb250ZW50LXR5cGU9aW1hZ2UlMkZqcGVnIn0.UGTRPGax1gRv5CXdeZm0yXan-fBu85sggRexy7f2TXg)
[![Twitter Follow](https://camo.githubusercontent.com/258b250cd1a66c0f3e47cb6280a83ab23ed0d8039bfd7b3b26a428a2550682cc/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f4d61676e75733f7374796c653d736f6369616c)](https://x.com/intent/user?screen_name=mamagnus00)
[![Twitter Follow](https://camo.githubusercontent.com/a0e8b2ed77d58af1a210d43db92aed35ed54cf7bb37564586e1fd647dcafb3dc/68747470733a2f2f696d672e736869656c64732e696f2f747769747465722f666f6c6c6f772f477265676f723f7374796c653d736f6369616c)](https://x.com/intent/user?screen_name=gregpr07)
Made with ❤️ in Zurich and San Francisco
