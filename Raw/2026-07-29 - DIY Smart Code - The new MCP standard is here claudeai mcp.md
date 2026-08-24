---
title: "The new MCP standard is here #claudeai #mcp"
source: "youtube"
url: "https://www.youtube.com/watch?v=OsEAEdxONlw"
author: "DIY Smart Code"
published: "2026-07-29"
created: "2026-08-24"
duration: "0:01:30"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "anthropic"
  - "context-engineering"
  - "mcp"
  - "web-design"
summary: "MCP just got a new spec, and the core change is that it stops holding state. Until now, MCP was a bidirectional stateful protocol. The protocol carried session state between client and server."
---

# The new MCP standard is here #claudeai #mcp

![The new MCP standard is here #claudeai #mcp](https://www.youtube.com/embed/OsEAEdxONlw)

## Description

MCP just went stateless. The 2026-07-28 spec moves Model Context Protocol from a bidirectional, stateful protocol to request/response—so MCP servers can deploy on serverless and edge infrastructure.

This Short covers the versioned MCP Apps and Tasks extensions, hardened OAuth 2.0/OIDC authorization, 400 million monthly SDK downloads, 4× growth this year, and more than 950 MCP servers in Claude's connectors directory.


----
🚀 DYNAMOUS AI COMMUNITY

Want to learn agentic coding with live daily events and workshops?
Check out Dynamous AI: https://dynamous.ai/?code=646a60
Get 10% off here 👉 https://shorturl.smartcode.diy/dynamous_ai_10_percent_discount

⚡ HOSTINGER — RELIABLE HOSTING FOR YOUR PROJECTS (10% OFF)

Whether you're shipping a portfolio, a side project, n8n flows, or AI agents — I use Hostinger for fast, affordable VPS + web hosting.

Get 10% off here 👉 https://hostinger.com/DIYSMARTCODE

(Affiliate link — costs you nothing, supports the channel.)
----

What you will see in this 90-second breakdown:
• The stateless core — bidirectional session out, request/response in
• Why that unlocks serverless and edge deployment for MCP servers
• MCP Apps: interactive UI rendered inside the conversation
• Tasks: work that keeps running after the call returns
• OAuth 2.0 + OIDC alignment — Entra and Okta with no workaround
• 400M monthly SDK downloads, 4× growth this year, 950+ MCP servers
• What Netlify, Intuit and Figma said about the release

• Anthropic announcement: https://claude.com/blog/bringing-mcp-2026-07-28-to-claude
• MCP 2026-07-28 specification: https://modelcontextprotocol.io/specification/2026-07-28/
• MCP release notes: https://blog.modelcontextprotocol.io/posts/2026-07-28/

Dropping sessions — a win, or did MCP just lose its best feature? Pick one below.

#mcp #modelcontextprotocol #anthropic #claude #claudeai #aiagents #agenticai #aitools #ai #devtools #serverless #edgecomputing #oauth #oidc #api #httpapi #softwareengineering #developer #coding #programming #aiengineering #llm #figma #netlify #intuit

## Transcript

MCP just got a new spec, and the core change is that it stops holding state. Until now, MCP was a bidirectional stateful protocol. The protocol carried session state between client and server. The new 2026 spec turns it into plain request and response, so it drops onto serverless and edge like any other HTTP workload. Second change, extensions are versioned now and two ship first. MCP apps renders interactive UIs straight inside the conversation. Tasks handles work that runs long. Third, authorization lines up with production OAuth 2.0 and OIDC. So, a server can sit behind Entra or Okta with no workaround. Scale check. The SDK has pulled 400 million downloads a month. A four-times increase this year. Cloud's directory lists over 950 connectors. And the teams running them signed off. Netlify's VP of applied artificial intelligence said the stateless core makes MCP a first-class HTTP workload with no session management to work around. Intuit called it the industry standard for connecting agents to tools and data. Figma says builders push generated output back onto its canvas. My take, stateless is the part that matters. Session management was the tax that kept MCP servers off cheap infrastructure, and that tax is gone. So, is dropping sessions a win or did MCP just lose its best feature? Pick one below.
