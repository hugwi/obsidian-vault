---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---

Prosurf/AWS to work on a data platform 
Rearchitecture
Data in general 
Slowly get everything under same umbrella
Old platforms up to standard
2 roles, data analytics architect, AI & ML consultant 

# Möte mikeal

produktivitet utvecklare 
säkerthet 
ai features

Mikael har vairt 
interrim CTO på 10 olika bolag


Tydliga mål för kostnad och effektivisering
7 månader från våra 
några front runners - effektiva support för att hitta, rätta till buggar. 70 procent kommer lämna
Använder materialet - delat seminar
enklare om det är konkret. vad innebär det för mig och hur kan man kan gå igång 
Satt upp det bredare. 
Intressant med att sätta upp webinar. Bombat med webinar
Lägg till autonom agenter. För oklart vad autonoma agenter faller in mot vanliga. 
Lite mer heltäckande 
agent platformen är något som kommer upp mycket 
bra och intressanta 


# Meeting Andreas
# Runtime 
Agent core run for the agentic runtime 
agent gateway - Many client that use it. Provide runtime and governance 
Application load balancer -  
(azure ai agent on azure corresponding)
agent run - runtime on kubernetes
We should bring up alternatives - check with Ognjen 

Andreas AI marketplace - One stop shop for AI 
hosting litellm proxy invoicing and monitoring
don't serve compliance governance. this comes from different teams 
Less the agent builders 

RnD is doing their own stuff 
AI foundations is doing their own stuff
Go one way because it's faster 
In AI foundations we look for it more holistically. That's was micheal ludwig is doing. He's looking at a golden path

AI marketplace - 
MCP servers  - AI connectors team that builds MCP servers  that we can reuse and blueprints 
Golden path for builders is something AI marketplace to 
Time to first token on our platform is a minute 

Patient data is not approved from our platform (it's a grey zone some people use it)

Business application - Good something Practice (GXP) good document practices 
Some use cases that are not sensitive

Make sure to get the onboarding compliance course 
Novo Access - access to github 
Get mac
Can do daily 

- Ping Micheal about the documents 
- Andreas Christenssen should ask him 

AI gateway is a kill switch - No central hub they need to go through. 
C level see's other tools than you're avergage worker 
Enforce guidelines 
AI gatway Novo owns - it's for Novo compliance 

Langfuse is what you own 
How many use your MCP you need to get yourself 

Not connected langfuse with the proxy. We have so much traffic on the proxy
Consume the LLM and senf the logs from tracing 




Goldfish can yo

Hey everyone! On **Monday**, Mark and I are starting a super exciting assignment where we’ll help build foundational AI capabilities for **Novo Nordisk’s Research Department.**
I’ve added the project scope for anyone who wants to take a look. It feels a bit AI-generated, to be honest, so you may need to read between the lines.

We’re especially excited because this is also an **important collaboration with ProServe**. We really want to show how one plus one can equal three, and why Netlight is the perfect partner for this kind of engagement.

I have a few questions where I’d love your help:

1. Is there somewhere we can get an overview of what the different teams at Novo are doing and which agent capabilities they’ve already built? We really don’t want to reinvent the wheel, and I’m sure there are many useful modules and learnings from the awesome Netlighters already working here.

We met with Andreas today, who gave us a lot of valuable insight. I also understand that Michael Ludwig has done quite a bit in this area, so I’d love to set up a meeting with you as soon as possible. If you can squeeze in some time before Monday, that would be a dream.

2. If you have any material, examples, repositories, or other resources that could help us ramp up and speed up delivery before Monday, please reach out or share them in this thread.

3. If you have experience with any of the areas below, or know someone who does, we’d really appreciate your input:

- Understanding available data and its sensitivity levels
- Data-classification enforcement and approval-gate patterns for each Golden Path archetype’s regulatory tier
- Reusable MCP components
- Data-classification and Good Practice (GxP) handling for each Golden Path archetype
- Evaluation harnesses
- CI/CD pipeline templates for assembling, testing, and deploying shared components

Any insights, existing solutions, or relevant contacts would be super helpful. Please drop a comment in the thread!