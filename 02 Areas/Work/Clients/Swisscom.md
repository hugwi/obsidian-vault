
19 july 

Anonymize client but give background

Able to aggregate data that was in silos. Discoverability. 

18 july

![[Pasted image 20230718091243.png]]

**Thursday 13 July**

Secured finance
Pradeep sabbatical end of July
A lot of material need to condense but big opportunity
Pick the individual topic, present some parts and ask to them? 
Klarna we had packages - 
FRP scanner - rule engine. Rule engine. Globally available in the 

What do they expect? 
-  
I've been trying to get insights from experts. Netlight have done or are doing quite a few. Offered lessons learned based on their various and experience in implementing data management solutions.    


1. Short Intro to Netlight
1. Short intro to your entire service portfolio (focus on Cloud transformation and Metadata Management)
2. Netlight's expertise and experience (#-customers, size-of-customers, which regions/industries, etc.) in metadata management (and using this centralized metadata for data catalog & data compliance usecases)
3. (Meta-)Data Management: 
	1. What are the targeted usecases and benefits with your customers? 
	2. Which solutions are popular with your customers?

	                                               i.     Vendor solutions such as Atlan, Collibra, Alation, Acryl Data.io, Data.World, etc.? 
	
	                                             ii.     Open-source solutions such as DataHubProject.io, Open-Metadata.org? 
	
	3. What would Netlight's' recommendation for Swisscom be, when it comes to vendor solution vs open-source? What are the pros & cons of each approach?
	4. What are Netlight's experiences w.r.to Atlan, Collibra, DataHubProject.io & Open-Metadata.org - Swisscom's frontrunning solution options?
	5. What should Swisscom consider when making the (meta-) data management solution decision?
	6. What are your recommendations for going live with the (meta-) data management solution? How to scope a first MVP? Usecases? Technology platforms? Concepts such as (data mesh) domains, ownership, etc.? 
	7. Any special considerations Swisscom should keep in mind?  

3. General interest from Swisscom: 

1. How big are the metadata management teams in your customers' companies? 

5. Q&A session

      I'd propose a 2-hour session given the heavy agenda. 

      What do you think? Would Netlight be willing and ready to make such a presentation for Swisscom?

**Last session**

Choose calibra first - had a bit more maturity to do POC. There where some gaps. 
Kafka is super important and they have nothingo

data marketplace 
compliance side - a few months ago they defined data steward and costodian. all metadata we need to do compliance.  

We need activate data management system
Need to act on it in real time. 

In what way do they need to act on it in real time? 
How is the marketplace intend to work? 

Managing data mgigration felix

Our own kafka clusters feeding into hdfs, some data is feeding into terradata. 

spark job will be the new peipline
redshift and athena and dashboard on quicksight. 

20% is on premise 

We need lineage and data catalogin in two different system

A lot of data is becoming real time. Most real time data is used for operation. 
We sell movile devices on credit and ew need to know if this person would pay. 
Current rating is in real time. 

3nf data warehouse. 150 system that is corretly 
You can map up that these systems as a starting point for the DW. 

What we want to do. Datahub architecture principal, everything goes to a central kafka datahub and then you use it in dw.

Public cloud we take anything in kafka and then replicate it to the cloud.

B2B, B2C, 
Terradata on 

Isolated catalog so they're duplicating
Two catalog - one for lake and one DW. 
People are not able to find the data and it's not enough metadata. 
They don't search they talk to their customers. 

Want to have all data and where the data is coming from. 

Crawler for all the technology and not maintain it. 
Breaks a pipeline, I didnt' know how they track it. 

did quick POC with datahub. On paper it looks good. Supports kafka and S3, HDFS, airflow. 

Impact analysis is available in datahub. 

Senior management - Long term what will happen. It's open source and.
700 customerso

Model the data within datahub. 

andreas: Confined to the analytics. Modeling it, 
Data steward is not analysts.  

A user can make a comment on a tables. 
I see the datasets but I don't see if there are some outstanding task for data assets that I'm working on.

Compliance: My dataset should have a confidentiality rating. 4 is business critical by the data custodian. Data steward need to change if this exist or not. You must do it else. 

Need to try to convince her colibra in datahub. Would like to do something within the next month. 
Lauer we can organize a meeting with them together. 
ur
More focus on why datahub is better than Colibra. We can help out the requirement.

Let's have a sync between us or Nic, if we want to convince Laur. Do we have someone working on colibra. We have done both. 
*If we have a knowledge article comparing the different solutions.* 

Define data products and contracts. 

8 Petabyte 

Use kafka since it's reliable even moving 500 gb of data

Kafka and Hadoop but want tot phase it out and use S3 and spark

**Meeting with Laur**
Did RFP, propsal to Collibra. Architect and Pradeep. Purchased the biggest in the market and they realised that they have 2nd generation data catalog. Had problem with Kafka (and s3). Laur was a bit chocked that it's a new player in the game. 
She said that we need to have some comparison to evaluate what's the best open source data catalog.  Atlan are quite good according to Pradeep.
Few stakeholder found additional data catalogs 

What should a data steward do and data custodian. We need to have some workshop to implement one of this use cases with Datahub (next week?) Requirement is increasing. Next meeting we want tho show that it's also best use case for compliance related topics.  

Not focused enough that I'm opening the door to open source but Laur thinks it's good idea  
6 weeks for the vision. Need to align with compliance.  

Pradeep is extensible that you can do anything with it but how you extend it is hard. No versioning who edits what. We need processes to make sure no one screws up workflow. 
Spring boot up is up to us for versioning all the code but therere are quite a few gaps to fill. We can habe every feature withh Collibra but we always need a customisation. 
The biggest whole is kafka support. On premise hdfs clsuter. We'll always go through kafka and then replicate through cloud
NEED s3 and kafka in lineage. Investigating with Collibra. 
Attribute level lineage. Need to upload files into file in the lineage extractor which costs 50k. You need to have a lot of customisation that you maintain. 
Concepts of owners need to be also customized. 

Need to add a component to detect changes.  
Collibra comes from the old world and they're trying to transform. 
Easier to have policies.  

Compare datahub, openmetadata, amundsen
acryl datahub and offer the managed version of datahub. 
Atlan seem to move very fast. LLM to generate descriptions. 
Did the comparison just prove datahub is better. 

We have 5 people in the team. It makes sense for us to do it. Amundsen is the best rated one. It would make sure to have implementation. 

Have some problem with budget. We have money 
Few people with backend engineer. Need somebody with backend skills. I could hire an external when it gets released. Laur want for implementation not investigating. We should take help for someone that has done it before. 

We don't have a good slicing of data products. Either you slice it too much and too little. 

If we have lineage and usage statistics. 
This is the process for deploying a data product and giving responsability to data owners and steward.  

Data governance don't like when people get to much columns. It's hard to get a good balance.  
Wants to see how people is implementing Data mesh. 

How is data produced today? 
It depends. Data is in all the transactional system. Some teams goes to source system. If it exists they don't need access to it directly. The data teams are the central teams source the data from trans systems and integrate to terradata and trying to move to the cloud. Move from terradata to a cloud native data warehouse. 
bootstrap the whole process, expose it as a data product. b2b and b2c customers. The central team is only responsible to aggregate data.

kristoffer; Each value stram has data compeetence, dont' allow people to connect to a database straight away. Before it would be have breaking changes.   

It was an audit and counted 3000 systems. 1000 systems but too many FTEs

We need principles. but only we think is needed. 
We need guiding principles. Assume that Collibra has this but probably don't have it.  

There are enough customers with Collibra but we're afraid that they're  

Principle: All data should be shared using one API. 
Want to build it into the cloud. Zurich region don't have all the services we need. 
We're not able to stop people going striaght to source system.  

We want to build a data mesh and metadata would be a key component.  

Would Laur be interested in meeting. 
Here calendar is super busy so might be hard to get a slot of here to show here our first hand reality. 
Go on a sabbatical end of July. 

She would raise questions about why it's not working for us when it's working for 700 other customers. Need to share the limitations of .
It would help with people that have worked with both side. 
.
It would help with people that have worked with both side. 
Data owners and custodian and the team that's joining the 

Compliance side
We should have a mapping form resourecs to dataset 
Implement data use cases to be enforce. 
Colleague from compliance side 

Weak with data steward. Nothing that says. For this that you're responbile. 
Every dataset is  
The role of data steward is to 
This is allowed to be moved to the cloud. Data steward. 

Look in the the network when it comes to a Data Mesh. 
You will check with Laur. I'll like to have 
When you get a go for Datahub POC. 


Question: 

What kind of compliance use cases do we have? 
compliance side - a few months ago they defined data steward and costodian. all metadata we need to do compliance.  
Compliance: My dataset should have a confidentiality rating. 4 is business critical by the data custodian. Data steward need to change if this exist or not. You must do it else. 


- [ ] Check how Datahub can react on for example missing description - How can you enforce certain aspects like documentation?


Comparison of datahub verses other properietary alternatives 
https://github.com/opendatadiscovery/awesome-data-catalogs


Kristoffer Adwent 

Tehh är 100 pers
Enklare att prata med folk, inte så användarvänlig.

User experience: 
+ Not that user fiendly
+ A lot of request and response flows and task list that doesn't feels smooth. 
+ A lot of the requests is funneled via a central team. 
+ The user experience has to be more straightforward and simple so that business users can easily interact with the Data Catalog

Cumbersome developer environment: 
@Kristoffer mentioned that they have a specialist who needs to iterate 100 time because the developer environment is so complicated and cumbersome. It's very flexible which makes is easy to get something wrong and that adding something becomes difficult.  

Tech lock in: 
Their also a bit locked into the tech they've chosen (which seems to be quite niche?).   Their worfklow designed is built into the their UI (interace?) where you define a workflow via a form and steps which then needs to be mapped by groovy code. Before you needed to do this in CLIPS and iteratively download and upload a zip file. o

Falling behind the market: 
- They were chosen since they were market leaders but has been following behind the market. There progress One example could be not having integrations to state of the art tools like dbt. 

Hard to discover the "entities" that you're looking for: 
As a customer if you for example search for the word "employee" looking for a dataset with employee data you get hundreds of results for columns with the field employee. 

Partnership:
They have strong partnership with companies like Snowflake and Tableau, but also for example AWS. This will probably given them an advantage in some of the integrations between this service but also leads to that they wouldn't prioritize features/services that aren't connected to these partnership.


De har starka partnerskap så de kommer ligga långt fram. Bryr sig inte lika mkt om de partnerskap. 

Workflow motor är lite låst i den tech de har valt. 

Workflow motor är lite låst i den tech de har valt. 
De har en worfklow designer inbyggd i gränssnittet, där man dels tar fram formulär och dels definierar de stegen. Man skriver groovy kod för att mappa ihop flödena. Tidigt var man tvungen att modellera i clips och ladda upp i en zip fil. Nu har man en komponent 

One reason for choosing Collibra was that it already have 700 companies and it's easier to find people with the same problems. 

Jag behöver det här och jag skickar en förfrågan till ett centralt team.
Mycket request och response flöden och. task list och inte alls tillräckligt smidig. 
Involvera business mera, en person som är inne en gång per månad måste vara enkel. 
Hur är användarupplevelsen undrar Kristoffers, från curator från consumer?
Collibra valde man för att de var marknadsledande och de kommer följa marknaden. Ingen integration med dbt. Ligger efter marknaden. 
Har haft referneskunder så Kristoffer har ändå ganska bra insikt. 
Det har varit långsamt i mål. Vi har pratat om ett år sen att få en dbt integration. 
Vi har möten med referenskunder samtidigt som de tittat på något enklara. 
Användarvänlighet och maintanability samt kostnad är hög. Workflow motor är lite låst i den tech de har valt. 
Om ett event sker ska det kickas igång en katalogisering. Eller att vi ska ge notifikationer på gammal metadata. 
De har en worfklow designer inbyggd i gränssnittet, där man dels tar fram formulär och dels definierar de stegen. Man skriver groovy kod för att mappa ihop flödena. Tidigt var man tvungen att modellera i clips och ladda upp i en zip fil. Nu har man en komponent 

Vi har en specialist, så vi måste iterera 100 gånger, besvärlig utvecklignsmiljö. Väldigt flexiblet så det är lätt att något blir för svårt. Allting kan modellera som en asset och sen skapar man relationer. I och med att det är så flexibelt så är det lätt att lägga till saker.
I grunden är allt assets, attribut och relationer. Det är svårt att lyfta fram vad som är viktigt och 
Vi skulle vilja dölja kolumner och och dataset. Vi vill 
När man söknar på employee får man 100 tals kolumner med fältet employee. Svårt att styra vad som ploppar upp. 
3 lager: känna till att det finns, dokumentera, kurerat. 
De har starka partnerskap så de kommer ligga långt fram. Bryr sig inte lika mkt om de partnerskap. 
TODO: Kolla partnerskap. 

#### Hugo
Background in applied physcis and electrical engineering 
Building data products for analysis and reporting  

Current client we're implementing a data catalog datahub and building a custom scanner for PII data. 

Joining an existing team mainting data pipelines and integrating new data source to building data platforms from scratch


# Pradeep R. Fernando

### Swisscom - Biggest telecom company in Switzerland

90 000 empoloyees
IT is larger than 1000 people

Hard time convincing employees implementing for datahub
What would help him: 
- Connect Swisscom with other companies

Long term vision for bringing the company to Data mesh
We need to work on making things more tangible. 

Swisscom hired top talents but they didn't manage to keep them.

Nicolas ambition: 
- Winning Swisscom is big.  
- He would like to have someone to have done it before. Making it transparent how we keep the experience to other projects and bring in the knowledge and it stays there. 

If we can initative a wrap up. Making an "offer". We noticed this and that.  15 minutes. Where are we and what do we know.  

Why datahub? Did you do an evaluation? The decision is a more concrete and urgent topic that we need to act on. 

He also used to work as a consultant so we could describe how we work on. 

Find which stage they're at in their data journey. 

## Overview
-   Meeting with [Pradeep](https://www.linkedin.com/in/pradeepfernando), VP PM, Data & AI within Data Services
-   **Techstack**: Transition to AWS ongoing (20% still on-prem/hybrid cloud setup), KAFKA, S3, Spark/Hadoop, Kubernetes, Tableau, Cassandra, Sagemaker, etc.)
-   DWH + big Datalake in place (for the Datalake the apparently have a good data catalogue in place)
-   Meta-Data-Mgmt ongoing topic (PoCs with Collibra vs. OpenSource, eg. DataHub)
-   DWH Transformation + Dashboard (ca. 3k) migration is the big (long-term) project - no lift+shift, focus is on transformation.
-   General goal/objectives for the organisation:

-   Upskill/ get the teams ready for the migration
-   Data Literacy -> increase adoption/enablement of eg. Shop Agents
-   mid/longterm strategy: Data Mesh --> Enterprise Data Strategy:
-   Data Product -> access via data catalog
-   Data Asset

Product Manager with 10+ years experience in product & project management. Passionate about hypothesis-based, and metrics-driven lean product development. Currently working on launching a data marketplace and self-service data & analytics strategy for Swisscom.  
  
A sample of my products: Data Marketplace, Big Data Platforms (Kafka, Hadoop, Kubernetes), Data Warehouse (TeraData, MS-SQL), BI tools (Tableau, SAS, Microstrategy), Anti-Phishing Threat Intelligence, Enterprise Mobility Management, Enterprise Device-as-a-Service  
  
Passionate about innovative, futuristic technologies: AI, robotics, artificial evolution, smart data and analytics, etc. My current interests lie in using digital technologies to drive enterprise success (from business model innovation to user experience and process automation).  

## Responsibility
   -   Leading company-wide initiatives: data marketplace, data management, public cloud move, and **self-service data** & analytics to **enable quick and reliable company-wide business value creation** from data in a **secure and compliant manner**. Addressing the problems of "Consumer" (#augmentedconsumer), "Engineer", and "Analyst" user personas. Working on building empowered and aligned product teams that provably create value for our users and the company through our data platform and data products. Product Lead for the 10 data lake agile product teams. Transformation lead for the self-service, enablers, and analytical tools streams.Leading company-wide initiatives: data marketplace, data management, public cloud move, and self-service data & analytics to enable quick and reliable company-wide business value creation from data in a secure and compliant manner. Addressing the problems of "Consumer" (#augmentedconsumer), "Engineer", and "Analyst" user personas. Working on building empowered and aligned product teams that provably create value for our users and the company through our data platform and data products. Product Lead for the 10 data lake agile product teams. Transformation lead for the self-service, enablers, and analytical tools streams.




## MMS 
- Business object lifecycle with prevent wild west to create more mature object that fits with the good data architecture
- Access and finding data
- People are sharing data marts and then it’s easier to create data without risk of duplication
![[Pasted image 20230606091234.png]]

![[Pasted image 20230606091308.png]]

![[Pasted image 20230606091336.png]]

![[Pasted image 20230606091405.png]]

### Datahub

#### Roadmap

Tag and Term propagation 

Tag vs Term? 

**DataHub Tags are informal, loosely controlled labels while Terms are part of a controlled vocabulary, with optional hierarchy**. Tags have no element of formal, central management. Usage and applications: An asset may have multiple tags.

Tag 
-   Tagging a dataset with a phrase that a co-worker can use to quickly query the same dataset
-   Mapping assets to a category or group of your choice
-   Any other Tags that will assist you or your teammates in more efficiently querying data in the future

Term 
-   Labeling datasets with concepts that are relevant to the business/industry
-   Labeling a data asset with sensitivity information (PII, Highly sensitive etc.)
-   Applying Gold/Silver/Bronze data-tier labels based on centrally defined standards


![[Pasted image 20230606091614.png]]


#### Problems

Scaling to 40k dataset, a bit slow on search right now.
Kafka events became a bottleneck queued up 

**A MCE is a "proposal" for a set of metadata changes, as opposed to MAE, which is conveying a committed change**
MCE is a proposal you send everytime you interact with the API 


**Authentication** is the process of verifying the identity of a user or service. There are two places where Authentication occurs inside DataHub:

1.  DataHub frontend service when a user attempts to log in to the DataHub application.
2.  DataHub backend service when making API requests to DataHub.

We use single sign on (custom by Mediamarkt)

**Authorization** specifies _what_ accesses an _authenticated_ user has within a system. This section is all about how DataHub authorizes a given user/service that wants to interact with the system.

#### Questions

##### How would you implement datahub? 

What are the underlying issues we like to solve with a data catalog? 


Debrief
If we could write a blog about this on medium. 
Bring this up during

![[Screenshot 2023-02-01 at 14.20.13.png]]

![[Pasted image 20230719142352.png]]


### Follow up 

Need more of the 
- Workshop 
- Use case


Using this centralized metadata for data catalog & data compliance usecases

- Common pitfalls
- How to start your governance journey

Data governance: 
- Organizational structure
- Privacy and compliance
- Data discovery and access
- (Data quality)


- Comparing data catalog alternatives 

What are the targeted usecases and benefits with your customers? 
How to scope a first MVP? Usecases? Technology platforms? Concepts such as (data mesh) domains, ownership, etc.? 


During the meeting, we discussed the goal of Data Governance, where to start and how to build an efficient Data Governance. We also explored the role of Data Catalogs within the framework of Data Governance.

1. **Data Governance**: A deeper dive into various aspects of data governance, such as organizational structure, privacy, compliance, data discovery & access, as well as data quality management.

2. **Starting Your Governance Journey**: There was a discussion on how to initiate and navigate the governance journey effectively, including considerations for organizational readiness and initial steps.

4. **Common Pitfalls**: We discussed potential challenges or mistakes that organizations might encounter when implementing centralized metadata solutions for data catalog and compliance purposes.
    
4. **Comparing Data Catalog Alternatives**: We explored different options available for data cataloging and compared their features, strengths, and weaknesses as well of which roles it plays for Data Governance.
    

Regarding the targeted use cases and benefits for customers, we delved into understanding the specific needs and objectives of customers in utilizing centralized metadata for data catalog and compliance. We also discussed strategies for scoping a minimum viable product (MVP), including identifying use cases, selecting appropriate technology platforms, and considering concepts such as data mesh, domains, ownership, etc.