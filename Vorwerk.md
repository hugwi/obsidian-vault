---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---
# Vorwkerk Data quality problems

https://vorwerktmde.slack.com/archives/CMS3SKE83/p1718100026670339

Identifying the ground truth of our customer base is difficult.
Expectations have been that CAR should have all dcids we can find in subscription table or in membership table.

 ---
 
 Relevant Tables: 
 **demo_data_products. bronze_connected_devices.connected_devices_v0**
 ---
 
Go live in September
PII handling can be pushed after September 
We need to match and merge in September. 
Spain and France identity matching

---

Want to start to collect behavioural data. 

Governance: 
How do we start

Databricks: 
Can we deploy infrastructure as code? 
Peter 

Point of contact of customer CRM 
offering digital platform for recipes 
subscription based model

Different data platforms. How do we define that? 
Have looked into prop CDP solution but doesn't fullfill 
build golden records
campaign automation code and segmentation 
leading system for marketing automation 
stream silos
cross selling, upselling, peronsalization

product lines - sales organisation, cookie dooo, netflix for films but recipes. 
aws services where  data team already is working 
problem there is that it's hard to assign roles. 
Abstraction layer: data science,  
evaluate demrio, snowflake, databricks compare to custom build.
databricks covers more use cases. 
pricing point it looks promising additional features. 
sql server data warehouse. 
databricks we already built pipelines 
how to make data teams work with the same language and context. 
Also for another potential teams. 
another project to build 360 degree view. 
digital warehouse was sharing from digital io 
we can't see what is shared to technology.  
Data licence model is not bill 

document metadata in a dictionary.
1 digital team 
1 subsidiary 
1 innovation team
1 data warehouse towards BI 
data people in the organisation sales
Trying to build this golden records for the 
1 recommender system
graph database for knowledge structure 
Person to have databricks knowledge, decision making and target architecture with databricks. How to build the golden record, combining records. 
Fallback plan interrrim solution merge by emails. 

off the shelf cdp too complex or don't have enough "features"
IOT data and not online prescence 
Platform data has a master view of all their customers that they can feed into 
feed into their marketing system
This platform would be the master ystem for the complete view
partly doing this since they already have use cases in databricks. Don't know if they're contractor or staff. 
The need for quite advance skills for databricks. 
Want to give other parts of information access to the 
they can't use the existent databricks "instance"
Usable that others then data engineers, set up segmentation rules for automation. 

2 weeks to migrate to snowflake 
1 month to setup gcp
What would consumption cost?  
need to figure out the non function requirement 

one prem data warehouse migrate to cloud


Deadline: fully automated CDP tool. March 2025

From us: 
Availability, 


**Questions:** 
- Long term vs short term? Do you already have the data sources? 
- What's current setup and why use databricks? 
- What comparison have you done already? 
- What use cases? Do you have any primary use cases? 
- Cost? 
- Urgency? 

Jag tror det är viktigt att vara konkret och visa att vi vill hjälpa dem att få saker gjorda samtidigt som vi är måna om att hjälpa dem fatta rätt val eftersom det verkar vara lite kort om tid.

Det är också lätt för dem att luta sig in i Databricks som jag förstår det men där tänker jag att vi ändå kan ha en holistisk vy när det gäller arkitektur och teknikval så att vi hjälper dem designa något som är modulärt, med tydliga gränssnitt mellan olika förmågor så att ett framtida byte av lagring eller tex integrationstjänst inte kräver att man skriver om allt.

Min bild är att det första de vill ha hjälp med är leverantörsvalet eftersom de har en tajt dialog med databricks

Det är viktigt att förstå CDP-domänen till en lagom nivå och även deras bild och förväntningar när det kommer till batch/realtid

Annars bra att fortsatt trycka på vår leveransmodell så att det inte blir några tveksamheter kring vår förmåga att leverera trots att det råkar vara någon annan än konsulten han träffade i första mötet som sen sitter i projektet.
###   CDP information

#### CDP on databricks 
https://www.databricks.com/blog/building-complete-and-composable-cdp-lakehouse
[databricks, snowplow, hightouch](https://www.databricks.com/wp-content/uploads/2022/06/db-240-blog-img-1.png)
(hightouch and snowlpow)[https://snowplow.io/blog/behavioral-data-with-reverse-etl/] 
Reverse ETL solutions like [Hightouch](https://hightouch.io/), alongside tools like Snowplow to capture and manage your behavioral data, are growing in prominence as a way to close the loop on the data lifecycle and help you get more from your data asset. To learn more about how Reverse ETL and Snowplow can work together, check out the next post in our series: Why Your Data Warehouse Should Be your CDP (Customer Data Platform).

###   [Reverse ETL 101](https://hightouch.com/blog/announcing-streaming-reverse-etl)

Reverse ETL syncs data from your company’s data warehouse to downstream tools like CRMs and marketing platforms. Today’s leading Reverse ETL solutions share several fundamental characteristics:

- **Deliver new data, updates, and deletions.** When underlying data in the warehouse is added, changed, or removed, Reverse ETL passes these changes to downstream tools. This delivery can take a few different forms. New data can be added in each tool as new rows or entries, but Reverse ETL also supports use cases where you’d update, resync, or remove existing records.
    
- **Declarative.** Declarative means you specify what data in your warehouse you’d like to sync and how you want it to appear in your downstream tool–the Reverse ETL platform does the rest. You shouldn’t need to think about the underlying API calls.
    
- **Abstract integration complexity.** Reverse ETL removes all the effort it would take for data teams to build and maintain custom data pipelines to third-party tools. At Hightouch, we’ve built an extensive [integration catalog](https://hightouch.com/integrations) of 200+ data sources and destinations. We constantly maintain APIs and endpoints for each of these integrations.
    
- **Only sync changed data.** To operate efficiently (for speed and cost), Reverse ETL must figure out what changed in the warehouse and sync only the new information to downstream tools. Figuring out what’s new is called [change data capture](https://hightouch.com/docs/getting-started/concepts#change-data-capture) (CDC). Without CDC, Reverse ETL would have to sync entire tables every time, which is not only slow but also cost and scale-prohibitive.


[streaming reverse etl](https://hightouch.com/blog/announcing-streaming-reverse-etl)



Databricks for a data platform 
He wanted to include data governance

Raising with precuement to get me onboarded

Reach out to Yevgen, do you have time this week to have a short kickoff. 
Dive deeper into his planning. 

Need approval  for CDP



### Assignment 

### Exploration and evaluation of technical solution based on Databricks
Need to specify what the technical solution is? Is this the evaluation if Databricks should be used at all? 

### Architectural support for data platform and technical enablement 

### Definition of data ingestion patterns
Suppose this have to do with the ingestion from aws to azue that we need to do and architecture to ingest them

For ingestion one can use: 
- Data factory 
- Fivetran 
- Airbyte

---
VPN is needed to move data between aws and azure.
https://community.databricks.com/t5/data-engineering/connect-databricks-hosted-on-azure-with-rds-on-aws/td-p/8995

AWS PrivateLink and VPN tunnels both provide secure connectivity between a customer's network and an AWS VPC (Virtual Private Cloud)

However, there can be some advantages of using PrivateLink over VPN tunnels

  
**Performance:** As PrivateLink does not require data to traverse the public internet (traffic never leaves the AWS network), it can provide faster and more consistent performance compared to VPN tunnels.

**Simplified setup:** Setting up a VPN connection can be complex, requiring the configuration of multiple components such as tunnels, gateways, and route tables. PrivateLink, on the other hand, provides a simpler setup as it only requires the creation of an interface endpoint in the VPC and an endpoint service in the customer's network.

**Cost-effective:** PrivateLink pricing is based on the number of requests made to the endpoint service, whereas VPN tunnels are charged based on data transferred o

---
###  Advisory on data governance principles and best practices
Might not be a focus point but something that we're aware of from the beginning? 

#email
[yevgen.tarasov@vorwerk.ch](mailto:yevgen.tarasov@vorwerk.ch)

Hey Yevgen,

I was stoked to hear that you've chosen to proceed with us for the upcoming 30 days!  Should we setup a meeting this week already to kick things off and discuss what we should focus on? 

Let me know when you're available, and we'll set up a time for our meeting. 

All the best, 

Hugo Bohlin Willfors



Start purchase order need to be signed for me still.   

It's more evaluating since it's greenfield 
Wanted to stop using CDP since it's not really CDP. 
Customer master record, golden record. 

How do we build a golden record. 

direct sales 360 
Marketing campaign - marces 
Need to find golden records to enable upselling and cross selling. 
How do we enable this?  
Other company areas also want to use the data platform. 
The problem: 
- Give possibilies and now we need some extra development. 
- New devops team 


Setting up another databricks for 360, checking egress cost 
Another databricks
usage box and cookidoo

Question from Yevgen: 
- How do we ingest the data? 
- How do we want to transform data? 
- How do we manage workspaces? 
- How do setup an account? Can we use terraform? 
- Tagging data dependent on tags? 


Have decided on Databricks 
High prio use case DS 360
Come up with rule? How do we integrate data catalog? 
We like to grow different use cases? Should we use portfolio management? 
If I build a data platform it's not duplicated?
Understanding what initiatives we have.  
Legally compliant? 
Should we have evaluation with DPO management?
	Expectation on how to implement that? Governance? I don't want gartner/deloitte governance. 
Formulate data strategy with blueprint -  having data initiative.  
100% sure data we should continue with Databricks. 
Doesn't make sense to start productionalise.  
Snowflake - higher abstraction but more vendor locking. 

emarsys
	
Technical govenrnace might have high impact. 
Clear structure, cost structure, responsibility, PII data

Talking to Matthias, what is the valid setup. What works and what doesn't work?  The focus should be the usability so we don't limit ourself. What is a good way to proceed. 

cookidoo - netflix for recipes. 

Ask me where my expertise lies and what I can help out. 
emarsys can only be integrated to gcp? 





## Building CDP 

- Who'll be using the data? 
- What additional processes are needed? 


## Building Data Governance Framework

NEED TO BE A BOTTOM UP AND TOP DOWN 

### Data access 
- Democratize data by allowing distributed data access.
### Data catalog
- data discoverability
- data ownership
### Data Quality
- Quality Metrics  
#### Data contracts
#### Data monitoring and alerting  
- Availability of data at the right SLAs  
- Health  
- Anomaly detection  

### Data security 
- PII Data Management  
- Data Access Controls (RBAC)  
GDPR
## Building Data platform on Databricks

- How do we onboard new teams into the data platform? 
- How do we seperate workspaces?  
Do we have any external dependencies? 

Risk: 
- What if we don't get buy in? 

![[Pasted image 20231116114840.png]]

# Questions
- Does it make sense to build the mesh for the product and onboard one core team that would use the data? That will help us see if the setup make sense? How much time do we have for the CDP?
- What risks do we have for each initiative? 
- Do we need buy in from someone to move to the new data platform? 
- Would other team need to migrate to the new platform? 


--- 
### Meeting 13 November 

We need to have a platform. It's not aa question mark? 
Opting in for databricks, central data platform? 
How to run this use case? 
First we can have a concept? How do we create a workspace? 
Notify in unity catalog? 
First case would be golden records? 

A lot of data initiatives? It doesn't make sense to migrate everything? 
if you develop a new thing they use the new data platform? 
We accept the risk of not having all of the data? 
Data stored on prem and aws? 
We need a better technology so enable access. 
Organisation wasn't ready to consume it? Management level also accepted. Got integrateed to the strategy. 
DSPro the commition level. Calculate upselling. 
How do we enable
There is no question about priority. The full system, consent, CDP, data layer.  
We saw a need for a proper data platform. Also aligned with the data platform. We use momentum to use. 
Already other use cases as a whole. They'll bring their own data source. Might be benificial

Matthias did the same for a big company where they did governance for CDP. 
Next week we get decision. 

Yevgen is not an architect
Have no databricks architecture. I know high level, but it's 
I'd like to achieve this business goal. I need to make sure that we 

I can have conflicting thoughts. Balance from different stakeholders. 

I don't want the focus out. Certain decision that prevents you to scale in the future. It should be scalable.  

1.  CDP for emasy
2. Technology that we can connect to all other components. 
3. 

Let's focus on one use case
Ask questions about what we need? 
Matthias to get some guidance. We want to establish these golden records.   

--- 
### Outcome 13 November 

Aligned that it make most sense to focus on a specific use case first - the CDP - and then add infrastructure and governance. We should have that in mind however when building the new data product. 

---
### Data ingestion
Aws databricks - IoT data is that usage box? Cookidoo is recipes?  
on prem - transactions  
emarsys - clicks from buyers on their website? interaction with emails? Purchases? Opt in and out? 

**What to consider for a Data ingestion service?** 
- Performance 
- Vendor lock in 
- Sources (how many do we need)
- Infrastructure setup
- Security 
- CDC or copy? 
- Integrates well with Databricks ecosystem 

#### Azure Data factory  
- Integrates well with Databricks (support delta tables)
- Can enable cdc

#### Airbyte
Fivetran, Stitch, Meltano and Airbyte.  
Airbute:
- big amount of integrations
-  fork a connector and develop it ourselves in case needed. 
- Also I've written a very basic connector myself in that assignment
-  Programmtic configuration via Octavia
	
**Cons**
- Maintain infrastructure (kubernetes)
- We could (at the time) not configure our workloads as code, i.e. as `yml`  or similar, but we needed to configure them in the UI manually
- It was slower than we expected, and we did not see a reduction in runtime for our Data Integration workloads (we used AWS DMS / Glue before)
- Mainly because of how beta the product was back then, and how we had issues integrating into our infrastructure and no information for such custom setups. Secondly same for what [@Johan Blad](https://netlight.slack.com/team/U01CX2VA3U7) mentioned about runtime.


#### event driven architecture
[Outbox pattern][https://medium.com/engineering-varo/event-driven-architecture-and-the-outbox-pattern-569e6fba7216] 

---

access controls
#### Consent mangement
"Consent management is a huge topic. How does consent flow between the different systems?" //Zeiss  
https://cdp.com/articles/consent-management-customer-data-platform-cdp/
Profile consent opt out?

Creating a [unified customer profile](https://cdp.com/articles/data-privacy-governance-best-practices/) across channels and platforms makes it easier to comply with data requests and preferences. The unified customer profile includes all consent and privacy requirements across applications and regions.

Because consent can vary across regions, platforms and experiences, it’s important to unify customer profiles across all channels and experiences. By unifying the customer profile, you can apply the right restrictions at the right time without slowing down campaigns.

---


---

#### Data activation
 Is it strong enough without considering cross selling and upselling? Are we sending golden records or are there other transformations that need to be done before?  
What kind of cross selling and upselling are we doing? For their products? 
Reverse etl to emarsys

Why these use case? Is it enough data? 


Consent management - shouldn't be apart of it. 
Afraid of having to compoments. 
Next step after management buy in. 
Food for thought - Across all the SAS 
Usagebox - pipeline that tracks on what your doing on thermomix. Looks like a log. 
Tracking - Aggregation of logs. Anonymized is handle the linkage is broken. 

3 differnet consent - marketing, personalization, device (gather device) 

Recipes - json data graph 

do spotify wrapped but for in cookidoo


ERP orders were done, adress name, stored in DWH 
CRM 
We need to think about customer ID
How to stitch users together. 
What would be the identifier that can be used serial number. 
Serial number fallback for stitching together.

Potential identifiers 
- Email
- serial number

Come up with business rules. When do you rely on them. 
Tracking - 
Using snowplow 
Using tag manager and upload it and offload data to your lake with snowplow.
Granular tracking data not only on aggregated low. 


Output is the golden records. 
We need that data to stictch 
Test interface to other systems. 
If it send a request, what is the latency. 
Emarsys will query the data. What is the window for the response time. 

Esimate egress cost?
How do we send the data to Emarsys. 
Databricks should give the final word of the cost. 
Restriction on cost? 
We want to identify.  
Scope out cost.

Sending data to emarsys? 
Scope out PII for now. 
Have different access requirement.


Batch vs real time? 

What's the downside of having consent management in emarsys? What happen if they're withdraw consent? Do we need to break the link of PII data in databricks as well?  

#### Data strategy
https://about.gitlab.com/handbook/business-technology/data-team/


### Golden records
[Splink: a software package for probabilistic record linkage and deduplication at scale][https://www.youtube.com/watch?v=msz3T741KQI]
Might be used to customer stitching 


[identity-and-access-management-in-multi-cloud-environments][https://medium.com/cloud-native-daily/identity-and-access-management-in-multi-cloud-environments-e2f8a4b82490]


### Sharing between clouds
[[Delta sharing]]
### Ingest data from on prem operational

https://www.tinybird.co/blog-posts/event-driven-architecture-best-practices-for-databases-and-files

Change Data Capture is an attractive strategy if you can’t or don’t want to update your existing API code. The team that owns the database will typically own CDC implementations, and there are free, open-source frameworks like Debezium that make it relatively simple to get up and running.


#lakehouse-architecture
![[Pasted image 20231121133613.png]]




Tekniska stödet för governance. 
CDP är ett första use case för data platform. 
Designar att varje grupp av förmågar så att man kan extenda. 
Ska cdp vara noden för anonymiserar? 
Del av designen? 
Var med i master data management? Inte trivialt? Manuell mappning? 
Vilken system är master data management? 
Om det ska ut i system som bara är konsumenter? 
Hur identifierar man användare? epost är bra till en början, men med en användare menar vi inte. Hur definierar man en användare? 
Man kan poca olika delar? 
1 vecka på high level design? 
Resultatet kommer inte vara ett implementerat system men en design. 
kanske ändå behövs en vecka för att sammanställa något. Behövs 



Databricks approve as a Data Layer
Couldn't provide cost estimation
Databricks need to do cost estimation. 
Since we aren't pressured to get the interim figures. 


#emarsys
Emarsys tracking data need to be fetch via API 
Customer data can be found in a mysql dataabase 
I sent a campaign how was the response. 


Primary use case to emarsys 
then for data scientist and engineer


Outsourcing the work for the integration 

Main benefit would be 

Usagebox from one databricks from aws to azure. What are the supporting structure? 
Golden records? 
How do we setup in databricks in general. 
Workspaces? 
How can we utilize the feature for the data lineage? 
What work with unity catalog? 
What is the proposal to structure 360? 
Can we structure workspaces? 


Snowplow - user trigger events (1st party)


YEVGEN STRESSED
Privacy can get

**Ingestion** 
What's the easiest setup.  
Data engineering tasks
DBT is one options. What has to be done to set it up. 

## Masking azure

https://learn.microsoft.com/en-us/azure/data-factory/solution-template-pii-detection-and-masking


### Data factory transformation 
[data factory etl](https://learn.microsoft.com/en-us/azure/data-factory/connector-sql-server?tabs=data-factory#native-change-data-capture)

## Native change data capture

Azure Data Factory can support native change data capture capabilities for SQL Server, Azure SQL DB and Azure SQL MI. The changed data including row insert, update and deletion in SQL stores can be automatically detected and extracted by ADF mapping dataflow. With the no code experience in mapping dataflow, users can easily achieve data replication scenario from SQL stores by appending a database as destination store. What is more, users can also compose any data transform logic in between to achieve incremental ETL scenario from SQL stores.

Copy data
https://learn.microsoft.com/en-us/azure/data-factory/connector-sql-server?tabs=data-factory

# Questions?



## TODO

- [x] Did they use multi cloud features? Feasible in general. Cost? Matthias - it's hard to find people to work with it ✅ 2023-11-16
- [x] Read up on tokenization ✅ 2023-11-16
- [x] Check how data is deleted for multi cloud ✅ 2023-11-16
- [x] Add data anonymization ✅ 2023-11-16
- [ ] Are the any data quality measures that are important?
- [ ] What kind of risks do we see?


