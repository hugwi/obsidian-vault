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
NNc Access - access to github 
Get mac
Can do daily 

- Ping Micheal about the documents 
- Andreas Christenssen should ask him 

AI gateway is a kill switch - No central hub they need to go through. 
C level see's other tools than you're avergage worker 
Enforce guidelines 
AI gatway NNc owns - it's for NNc compliance 

Langfuse is what you own 
How many use your MCP you need to get yourself 

Not connected langfuse with the proxy. We have so much traffic on the proxy
Consume the LLM and senf the logs from tracing 




Goldfish can you rephrase the text above so it's follow a good structured but still prserving my tone

Hey everyone, on Monday me and Mark is starting a super excited assignment where we will help to build fundamental AI capabilities for the research department.
I've added the scope of the project so you can all look at it. I think it's a bit agenerated, to be honest, but you need to read between the lines.
We are super excited for this project since it's also an important collaboration with Proserve.
Thus we really want to showcase how one plus one equals three. And why Netlight is a perfect partner for this kind of engagement.

I have some open questions that I would love to get help with.
1. Is there any place where you can see what all teams does on NNc and what kind of agenda capabilities they were building? We are really trying to not reinvent the wheel here and think we can use a lot of the modules that have already been built by you awesome Netlighters out there. We had a meeting today with Andreas, who helped us gain a lot of insight into this, and I think Mikael Ludwig has also done a lot of things related to this, so would love to set up a meeting ASAP with you. If we could already have this, if you have any time to squeeze out to help us with this before Monday, that would be a dream coming true.
2. And if you have anything out there that would help us speed up that delivery and getting more knowledgeable before our meeting on Monday, please reach out or write the thread here. That would be awesome.
3. And if there are any of the axes or education or anything related to that that you have know-how in and could help us with, that's also great.

Here are some of the fundamentals that we are also asked to build, so if you have any insights in this area, please drop a comment in the thread.
1. An important part of this project would also be understanding what kind of data we have and what data sensitivity we have, so if you have any knowledge in this, please reach out.
2. data-classification enforcement, and approval-gate patterns appropriate to each Golen Path archetype’s regulatory tier
3. reusable components for MCP
4. Defining the data-classification and Good Practice (“**GxP**”) handling approach for each Golden Path archetype
5. Developing an evaluation harness 
6. CI/CD pipeline templates for assembling,

# Micheal Ludwig 
Central IT where NL is 
Least patient and most technically capable  
RD are the free roamer 
AI marketplace was the first real success product team for AI 
Can be a direct competitor or a good collaboration 

Enterprise ai is a parallell organisation
Christian engelbrekt from NL 

Golden paths with 
We build guides and what to do? 

Understand who pays? 
Talk to people at Chirstoph eichelberger 

Ai spedning budget is stupid and don't check ROI 
Worry more about AWS Proserve 
Default AWS services are blocked  

Big novo incident
##  Who's gonna pay and how what did they come? 

## Crhistopher Herde 
He's doing similar to what Micheal is doing 
Golden agentic path 
It's very ambitious said Micheal 
It has to do with the london based team
## Johny birch 


# Meeting

Anna AWS - Practice manager from NNc Nordisk  

Anna - AI strategist 
Mohamed - AWS 

Mike NNc - Data solution engineer in the bianca team. Agentic capabilities 
Susu - Senior manager AGC 
Christoffer - project lead for the golden paths 
Lazlo - NNc teach lead agentic custom solution 
Buanca - NNc started the assignment Mike is the idea that started it 

##  We're not starting from scratch 

## Agentic golden paths for R&D 
Strategic partnership 7 year  PPA 4 year PSA 

Entarprise AI workstream 
R&D trnasformation okstream - this one 
cloud migration workstream 

WP5 - agentic golden paths 

## Gvoernance model 
Partnership board 
Prgoeraming steering - Anna will be position 
R&D steering committee 

Hugo and mark AI Engineer 
Susu Data & AI Engineer 
Michal - Senior machine learning engineer 
Mike - ead data solution engineer

Christoffer hjort - lear machine learning engineer 
head of data & AI Engineering - Bianca Gutu 

## Christoffer asked what the reasons for Netlight 

## Golden Path 
- reduce cognitive load 
- safe & compluant 
- self service 

## Value prop 
- target ds and de 
- Builders can spend 40% on plumbing 
- Solution: select service interactive tool 

## Golden path tenets 
- Governance encoded in the infra 
- Where will we use the golden paths

## Key terms - what are we building 
- archetype - business domain
	- patterns 
		- technology building blocks 
- research agent and 



## We should try to decompose it - christoph 
- we need to make them decomposable so they can cater to mulitple businesses
- **mindset - we will not build new infrastructure, build on top of existing infra** 
- We shouldn't compete with what already there  

# Lazlo - NNc teach lead agentic custom solution 
- Needs to be segregated - 


## Golden path look like 
- Solution can give reference architecture 
- you put in your constraints: confidential, public 
- We cant wire it how can we wire it 
- identity & acccess - aws iam
- Data platform - NNEDH - datacore 
- file storage - amazon s3  
- vector database - opensearch 
- LLM provider  - NN AI marketplace 
- deployment 

**Lazlo is composability** 

Charles - graph traversal algorithm  

## Golden path success Metrics 
- Speed
	- time to mvp 6 -> 2 month
	- <1 week 
- Efficiency 

## What's outside of golden path scope 
- configuration of the project
- **it risk assessment - 90% implemented can we automate. design the systems with the questinos that are in the IT RISK**
- connecting to any systems or data sources


# Engagement Deliverables 
- NNc AI Landscape - 9 selected use cases 5 different archetypes 
- solution map - overview of AI landscpae with componenets, readiness, dependencies 
- Content authoring & Research Agent 

### Golden path finder 
- interative tool to query solution map 
- golden paths and building blocks catalogs 
- raci for shared foundation componentents - operation model


## Shared foundation 

- golden path use case instantiation
- validatio nand friction detection - migrate to paths 
- golden path - operationalization


What's different between golden path finder application arhcitecture and golden path finder application on aws 

**Defintition is more about the design** - application is where a user select 
Shared foundation is more about implementing - it's the building blocks after you selected

## Engagement Timeline 
- NNc AI Landscape 
- SOlution Map 
- Finder architecture 
- Sahred foundation architecture 
- One team for the shared foundation and one to governing the templates 

## Agile Engagement Approach 
- planning 
- review bi weekly 
- taks management - daily tickets 
- code review - customer and peer reivew 
- bug managemnt - daily and weekly locked bug 
- 2 weeks sprinst 
- standup two a week 
- one status meeting 
- sprint review end of sprint


- Morpheus molecular agentic ai - Bianca raises why we look at it. Christoph means that want variabnes. Morpheus we shouldn't look into  

3 AWS engineers need to be onboarded 

- **Why aren't we talking about AI marketplace and Enterprise AI -> Bianca think we should look into it**

AI compliance is not part of this initiative 
# Archetypes
- 2 archtypes and not 3 x. IT SEEMS LIKE THIS IS THE AGENT ARCHTECTYPE

Michail will be back from our side

# AWS Collaboration
- Transparent communication 
- Communication channels  
- Plan they have made that we don't know already
- Materials 
- Paternity leave


## Meeting golden point

- MAP SOP terms to technical requiremenett
- these is already a golden path prototype, we can put it in the sharepoint
- **clear definition what is its meant if it's research agent and content authorhing**. Looks at the discover we had 
- Research agent is known archetpyes. Content is drafting based on different sources
- **Enterprise AI**: <mark style="background: #FF5582A6;">Meeting with Martin who own the AI marketplace and AI agent runtime</mark>. Setup a meeting with him. 
- **IT risk assessment**: Don't provide solution but guidelines. <mark style="background: #FF5582A6;">SEE IF THEY GOT recommended paths </mark>
- We will work on the High level design. This will be after the discovery. ==We will work on the discovery and scope now== 
- Interfaces between technologies. Constraints. What rules we have to play buy given the constraints. 
- Use case can be quite overwhelmed. Look at the problem they're trying to solve. We want to build something that generalises. Don't want to build something that overfits


# Discovery Session - Open GDS


## Business Use Case 

- Taoxigolist which reaserach  of molecules 
- Regulatory aspect what kind of experiment did you contact before giving it too humans. Try to improve this 
- Two featues 
	- Search engine
	- docuemnt
	- Was fiddly and non technical 
	- There are specs  
	- Latency issue is need to get data in the right format
	- 500 users and 50 person use it in the same scalability 
	- Need to have the right component. 
	- Data is in databricks. structure and unstructured dat and binary volumens and search indexes 
	- Important Data is confidential and strictly confidential . We need to operate in a way that it never leaks 
	- No one should now or could patent it
	- There is a backend that is the agentic part. Same architecture that molecular reasoning. Told ai to copy ti with the same restrictions 
	- frontend is in view. pineat and novo ui kit. Heavily customized. Nono ui are certain components that are not availble. Project has data engineer and ux designer to 
	- It's a way to find studies that have components. It's a querying of various compounds.  A lot of studies what has been giving and what is the affect. 
	- Aggregate for regulatory approval
	- One of the goals is have a data product and can aggregate of the project in the relvant format. Experiment of what has been done. 
	- How is Molecular structure: don't refer to them as molecular structure. molecular design. 
	- Effect, symptoms, components. 
	- RA agent -> knowledge agnet. chat bot that is capable of running sql to the databricks resources. Alos rec, planning and supervisor capabilities. Surface and aggregate data. 
	- Dbus through prisma postgres data (RDS in aws). reseearcher design the structure and how they want to represent the data.  
	- Don't use mcp little value of it. 
- **Piepeline**  - Broschure generation agent
	- Less of a chat agent 
	- filtering and querying interface 
	- they take study ids and run filtering process are the source of the input of the IB workflow 
	- same dbus orchestration 
	- Doucment is saved into the s3 
	- frontend is django app fastapi server is setup  
	- aws secrets define how to set it. to enable experimentation adapters 
	- experiment locally without having access to dataabricks 
	- every llm call is going through all the same call going through gateway. Use the adapters so you can easily change it. 
	- kubernetes cluster 
	- Backend is not a microservice it's monolith we just need many of these. 
	- DBus does the intercommunication 
- Databircks is experimentation data domain data. gb of data easy to proces
- prisma is the application data like data 
- Databtricks is gxp data and confidential data 
- we need an own certification we need the same that the data that is handling 
- observability, provenance, -> cloud watch is happening it. recording everything
- Different fomr the data that we store in progress use by the use cases
- have langfuse. 
- We can overload our endpoints so we useing ai manager to have global locks in redis
- Authorization to the data, entra id. 
- Toxilogival report. they will coreview. the structure for the process. 
- we don't share it speculatively. Can we access the 
- Documentation generation is fundamentally - one is the loop. 
- differnet data sources and ways to connect to them
- high level lofic 
- stream data to the frontend, how do you scale up 
- the user are not technologist - one of these requriement won't be 
- resulted in a one of the custom 
- pydantic ai  sophisticated ai 
- researcher 
	- ai research - not software engineers - job is to figure out how to shoehorn the use cases
	- drug researcher 
	- sometimes they ay it's not good enough
	- exampple ai workflow run for an hour colleect the data 
		- requirements was that it must ask clarificaiton questions. when the use says yes, then we do a planning phase. finished it's send back to the user. it needs to be editable. then we need to back to the clarification stage. 
		- how do you do this? Shouldn't need to stop afte 1 motnh to 6 month. 
	- how is the quality of the content measured? 
		- blood sweat and ters. the opengdss team. They're happy state 
		- they know the answer 
		- they don't  understand the shape of the answer
		- need to understand the agent tree to see where it made wrong 
		- it's trial and error. Everything we recorded and done 6 month you can extract it analytically. Are you sure you will do statistic of 50 users a day. Maybe not. 
		- AI research team it's literally their job. Data Science are responsible for the prompt engineering. 
		- The data science does it since they understand the subject matter experts. statistical analysis. large scale 
		- They need to deploy it 
	- care team need to take care of the team
	- another team for the data engineering team. 
	- how many teams are involved  - AI org 1000 people
	- Lancgchain not used langgraph i think 



# Follow up Planning 
- Technical landscape,SOP 
- Use case and architecture

- **Consistency and Quality Control**: SOPs ensure tasks are performed uniformly across the organization, reducing variability and maintaining product or service quality.
- **Efficiency and Time Saving**: With clear instructions, employees can execute tasks faster and with fewer errors, boosting productivity.
- **Training and Onboarding**: SOPs serve as effective training tools for new employees, helping them learn procedures without constant supervision.
- **Compliance and Safety**: SOPs help organizations meet industry regulations and safety standards, reducing legal risks and [improving workplace safety](https://www.hseblog.com/improve-workplace-safety/).
- **Accountability and Responsibility**: SOPs define who is responsible for each task, making it easier to track performance and manage accountability.
- **Business Continuity**: If key personnel are absent, others can rely on SOPs to ensure the work continues without interruption.
- **Improved Communication**: SOPs eliminate ambiguity by documenting exactly how tasks should be done, reducing misunderstandings between teams.


--- 


Agent orchestration 
agente memory 
agents artifactory 
agent patterns 
ai assistant 
agent integrations 
models 

# Enterprise agentic ai landscape 
datas indexing & retrievel 
data org
data storage 
obser 
deplyoment devops 
data governance 

Some are engineering activities and some are data science acitvities and fall on the data care team 

AWS is collaborating with the Innovation Hub 

## Scope of the agents 
Retrofit one of the solution which would include the data science part 
One is completely new 


## SOP 

Custom programming - 
