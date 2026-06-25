---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---

![[Pasted image 20251125181050.png]]

![[Pasted image 20251125181118.png]]
## To Consider
- Rollout Salesforce quickly and get business value is a great idea
	 - We've not talked about it much, but I think that's a great idea because, you know, with all these things, you don't want to go live necessarily the big bang and have like everybody using it and then going, oh, I don't like this and I don't like that. Obviously we want to use advisors during the course of designing all of this, but actually if, if we want to implement things quickly and get something rolled out and then, and then test and learn from it and then bit like we're doing in workflow and if that's one of the powerful things we can do with Salesforce because it's so configurable, then then, then that's a great idea. And it gets, and it gets business value much quicker as well. And the advisors will feel bought in because they'll feel they've been part of.
	-  Get this off the ground with Carolina that can explain their value. Create a reference group. Could start with salary exchange. They should be an active participant. 
- Karolina has a lot of different requirements for redesigning it **isn't mentioned in the requirements document**.  The advisor absolutely needs to love it. It's a big opportunity. **No one is gonna use it if the prospect is bad**. 



## Opportunities
-  Big cross sell opprtunity between wealth management and L&P 
	- And then there's obviously cross sell between, between PNC and Wealth management and LNP as well. The big one is between pnc, LNP because PNC is, is the sort of the fledgling business, whereas LNP is the, is the big business. So LNP is something like 90% of 80 to 90% of Maxim's commission. But all of every single LNP client is a potential PNC client. Right. So that's the big cross sell opportunity. And then within wealth management there's obviously cross sell into the private banking side of things, particularly between small businesses or the leadership of the big companies and within the PNC customers as well. So that's the kind of the whole cross sell upsell kind of dream that we want to do. So right now the kind of customers are not seen as a customer across all three business units. 
 - 



# Meetings
- [Requirements Gathering 18 November](obsidian://open?vault=hugwi&file=MaxM%2FMaxM%20Meeting%2017%20November\)



--- 

# Objectives

- Client relationship value across L&P, P&C, and Wealth Management
- Client, products, premiums, capital and commission insights
- Historical trends 
- Identify Cross and upsell opportunities
- View Customer Journey  
- Data activation - Email, SMS, in-platform messages
products held, premiums paid, and commissions generated
- Provide single operational data view of clients (including prospects) and customers
- View client relationship value across L&P, P&C, and Wealth Management, including products held, premiums paid, and commissions generated
- Identify which employees are customers and which are not, and measure penetration rates for products across the employee base
- Ability to track historical trends in client, product, premium, capital and commission data over time
- Identify potential cross-/upsell opportunities at both employee and company level.
- Identify a customer’s current stage in the customer journey
- Ability to see all Private Banking clients 
- Asess the total relationship value across WM and non-WM products, including premiums and commissions.
- Ability to see commission generated
-  Ability to see in Salesforce, per corporate client
- Deliver relevant communications via email, SMS, and in-platform messages on the homepage.


# Objectives summary
1. Establish unified client and prospect data views to enhance transparency and operational efficiency.
2. Track and analyze the full relationship value (products, premiums, commissions) across business lines and customer segments.
3. Monitor historical data and client journey stages to identify trends and opportunities.
4. Enable segmentation to measure product penetration, cross-/upsell potentials, and employee-customer relationships.
5. Integrate data and insights into platforms like Salesforce for actionable intelligence per client.
6. Deliver targeted communications through multiple channels (email, SMS, platform messaging) for better engagement.

# Dependencies

# System Integration
L&P and P&C Client Prospecting process
- System integration with swedish National Companies database to validate company. 
L&P cross/upsell potential
- Integration of WM platforms (e.g., MaxFonder, Alwy) with Salesforce and the Data Warehouse.
P&C 
- Integration of P&C platforms (e.g., Bonnaya replacement / Broker Platform) with Salesforce and the Data Warehouse. 

# Data Quality issues
L&P and P&C Client Prospecting process
- Data quality issues such as missing data and dependecy on rearchitecture mention on page 20. 

L&P cross/upsell potential
- RS Advisor system Unstructured data prevents measurement of cross/upsell, requiring a spreadsheet workaround
- Data quality uplift to ensure consistent client/product data across systems.

P&C 
- Data quality uplift to ensure consistency across CRM, DWH, and the Commission System.

All
- Data quality uplift through unique identifiers for clients and customers, deduplication, cleanup of outdated records, and standardisation across upstream systems (RS, PML, MaxView, Commission System, Bonnaya, MaxFonder, etc.).




# Cross section 2 and 4 
- **The MDM strategy** needs both to take in account as well as design the as is and to be data landscape.  This includes the refactoring and / or full re-architecting of PML, LINDA, DWH and other databases.  The implementation of this design is likely to be performed by the GCP Cloud Migration initiative
- DWH to the GCP Big Query and provide a basis for AI (note: this is not included within the VCP initiative)
- Improved data quality
- Integration of Swedish national companies datbase 
- 

- Ingest (if not already exist) and stitch data to create a customer 360 record. 
- Built facade and ingest data into SF 
- Build data model in SF
- Ingest data into Salesforce 
# Feedback

+ Commercials 
	+ Team setup 
	+ Team structure
	+ near shore vs long
	- Rates are we playing around we
	- Onboard people 
	- Length of activities 
- Implementation phase 
	- High level activities and people we need 
- 12-18 months 
- Key deliverables 

Not hold accountable for us. 
The other companies always looked towards two people when they get questinos 

Deadline at latest to Friday. 



![[Pasted image 20251029093740.png]]

Most important is to focus on the  
- key activities, the deliverables for each and one and
- how long time they take and
- how many people are needed from Netlight, MaxM, and sollers
##  Discovery - understanding of current state
- Current state 

##  Build data strategy and roadmap 
- Identify source of data and roll-out 
- Design MDM strategy 
- Design architecture

## Design Architecture


## Implementation 
- 


## Questions 
+ Can we make a strategy this early? Will we miss information?  


## Salesforce 
+ Att vi inte bygger för komplexa system. 
- Map use cases, high impact 
- How can we made informed decision. 
- How does we avoid making things with low impact for adhoc quesstions. 
- 

Produktägare är nya roller. 


+ Strategy   
	- Operational -> BQ 
	- DWH -> BQ
		- Data lineage - Vad flyttar vi först? Vilka tabeller?  
		+ Hur flyttar man? 
- Target architecture
+ Data governance - row level secruty. Data access. Personlig data. 
## breakout room 


- Affärsområden har inte en koppling  

Maxview, en rådgivare kan inte sa. Behörighetskrav.  

Maxview ger bra överblick. Merförsäljningsområden. 
Det fungerar men de kommer inte signalare 
merförsäljningskampanjer till individer. Kunderna bearbetas. GÖr en berbetning. Har den bearbetas. 
-> Innefektiv i säljprocesserna. Har den tagit till vara. 
Kan inte kommunicera till kunderna på vårt status 
Inte riktiade 
Kunderna tack nej.. 

- Affärsmöjligheterna 
- Säljkampanjer 

Utmaning
	-  Vad är en aktiv kund? 
	- Olika kundföretag kan ha vissa regelverk. Inte strukutrerat. Skriven policy. Lägga in i ett system. 

Kunden finns i alla värden. 
Flytta det rådgivarna ser till Salesforce från Maxview. 
10% nyförsäljning. 
Det är bara en extra syssla. 
Vissa jobbar bara med försäljning. De flesta har sina kunder. Rådgivning, men vill öka försäljning. 
Prospekt har inte någon 

Bonnaya står still utvecklingsmässigt. Mostvarande Maxview.
Svårt att se gränsen 

Komplex struktur kring premie mer komplex liv och pension Fastighetsäare och konsultbolag. Ska hanteras i ett extern system. 
Just nu bara excel ark. 
Svårt att få in i Bonnaya. inte så mycket data. Kommunikation . 
Mesta data går mellan är excel. 


Bonnaya är stand alone, men systemet inte stöder pdf och excel. Man kan ett arbetsätt som kan stöta det. Vad är den centrala datan.  Inte knappa in datan på vissa ställen. 

Rådgivningsstödet måste också vara kopplat. Dokumentera, ekonomisk situation. 

Feeda in via DWH. Integrations. Kund master. 


### Questions 
- Organisatoriska utmaningar. 


# North Star
+ 


+ Use case 
+ Commision 


# TODO 
- Add description of master data:  that it's a non transactional data
- Update with new master data. 

# Feedback
- Tydligare vad workshop är med WS 
- Gör texten större i MIRO. Fetmarkera Salesforce


https://profisee.com/master-data-management-what-why-how-who/
# Resources 

https://netlight.slack.com/archives/C09JDMK24TU/p1759773295538099

# Stream 2 

### Dream 
- Make sure to ask about priorities and this is normally how we would do. Do they see any low hanging fruits where they have all the data and just need to ingest it to SF? 
- Differentiate data insights from operational data 
- Add slides about domain driven design and moving responsability into domains. 
- Add slide on why we shouldn't have MDM doing everything. Show it growing and becoming an bottleneck as well of need to have SLAs, rather push ownership into domains. 
- Make sure to explain why it isn't enough to only have the DWH stitching data together to build the golden record. 
j
# Master data management Benedikt 
-  Do they need a golden record? 
- It is costly to implement. 
- Some of them had MDM solution in place, a lot of clients went away for that? 
- Not focus on MDM but the problems they want to address
- Organizational issue and technical 
- What should be in the CDP or Salesforce
- Understand commision shouldn't be in Salesforce
- Create a facade between salesforce and business model
- What competences do they need


# EQT 
- finns ej ett ref case 
- Ref case split to Monolith 
- UI för ett MDM, huge dependencies. Var inte mening att vara en stor databas som inte skalar. 
- Human in the loop. Du löser inte validering av punkter utan personer. 
	- Måste ha personer som äger vissa data punkter
	- Nån måste korrigera data inconsistencies
	- Andra system tar prevelance över andra
	- Validera ny matchning, marked for review
- Ville exposa golden records med för operationella datan
- Går att skapa golden recods för analys men ska inte gå två vägars. Inte operationell dependency. Stort arkitekturellt problem. 
- Rules: 
	- Systems prevelance 
	- Human in the loop

# Notes
- Ask questions again in the case study
- Should be a final pitch at the end of the day - it's more beneficial to pitch it at the end. 

# Learnings MDM
- Huge dependency on the MDM system 
- 


# Thoughts
- Seems like francis want to have salesforce as an operational systems where clients are onboarded.  
- They don't want to focus too much on GDPR, but also want us to make sure to incorporate it. 
- How do we neutralise that you need to subcontract. How is that a improvement? How do we work on the a single company. 

# Workshop setup

- What are risks that make Netlight not choose us. 
- Don't repeat requirements. 
- Risk with two different companies. 
- Share our ref cases. 
- Do we want tot do some kind of prioritization matrix. Are there low hanging fruits. 
- Goal is to have princiuples of MDM principles and not necessarily MDM strategy. 
- Do everyone need to be part of it. 
- How do we reuse sames tools and methodology or do we use different tools? 
- Is it more prioritized to to show how we work or the output? 

## TODO
- Add francis to attendees
- We want to understand the vision and goals. 

## Important things to consider
How do you get learning the code set, the existing systems are (seems to see how we solve the procecces? What is your methodology to approach the case studies existing application, data flows. How do you get up to speed in understanding that. What your method and approach. We want to be confident taht you know how to get your way around heartbeat. Assuming that you know about heartbeat, what's the solution to single person, do it in a workshop style, "how is it to work with you"? The analogy: If you're hiring them, you read cv, but employees do case studies and we watch how they code or solve architectural problems. 

 A lot of logic sitting in these procedures. Stick it in the application layers and not the database layer. If you've done a case study and we have seen it in sybase. People eyes would light up. Something close to sybase. Not only how to move to GCP but also refactoring legacy code and modernize the architecture, is API centric, do I use domain driven design. 

Advisors want all the data in maxview! Do you need to refactor it or can you decomission, we don't know the answer to that questions. 

It could be an opportunity for simplification! 

For the case study PML is mentioned. The focus on the workshop should be addressing.

- What have we done this before, what are you approach? 
- Migrating the legacy to bigquery. It is in two flavours, medallion architecture, easy to move. The old one doesn't follow any form of architecture and don't have knowledge on how it works. 
- For GCP is more about what you've done before. Don't get hung up on the lift and shift. Focus on the refactoring. 
- On the CRM data one, we got two sets of data. If possible it would be great to see how that would look in Salesforce. 
- Linked to GCP we linked some crappy stuff. It's in the CRM data but more about a migration questions than a MDM kind of thing. 
- Advantages of doing it serially is that we they can participate in all streams. j

# Salesforce stream
- Important with MDM strategy
- Would be great to see the Salesforce data. o


Övertid 
Thu 16 Oktober - 08:00 - 18:00
Wed 15 Oktober - 08:00 - 00:00
Tue 14 Oktober - 0800 - 00:00
Mon 13 Oktober - 08:00  - 22:30 
Sun 12 Oktober - 08:00 - 00:30
Fr 10 Oktober - 08:00 - 23:00
Th 09 Oktober - 09:00 - 20:00
Wed 08 Oktober - 09:00 - 22:00
