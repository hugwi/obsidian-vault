What personal data should be in scope. 
+ sso_id
+ cookie_id
- subscription data
- tracking data
 Which systems/data producers that handle personal data should be in scope?
Upstream/downstream dependencies. 
- Who is producing/owning the data 
- Who consumes the data and get affected by data? How are they affected if personal data is removed?  


**Legal Basis and Purpose**
- What consent mechanisms are in place for using personal data, especially for analytics?
- What happens if someone withdraws their consent?

**Data Subject Rights**
- What data subject rights processes do you have in place today?
- How is the right to be forgotten handled?

# Vad händer 1 september. 

workshop 1-2 dagar. 
kick off 
buy or no buy.


4 brands work independently 
12 months ago reorganized got the same organization 
Victor has helped to some part of it. Trying to plan our new roadmap while keeping everything alive. 
GDPR compliance. 
# JP / Politikens Hus

Förståelsen för scopet för data platformen

Claus - Data platform lead 
# Data privacy


# Head of data and AI
legacy data 

EFP - big storage. Other parts
We can't do a gap analysis on something we don't know about. 
What technical solution do you have? 
- Storage, ice berg 

First scope 
How big is the DFP
The number is really big
We need more certainity so we know what we're going through


Scanning for existing personal data? 
Label Personal data? 

Data strategy for Vorwerk
Very slow right for gotten request 
Handling consent 

What is personal data? Doing risk assessment? 
Secure personal data? 
Pseudanonymizaiton 


# Mariah - Change Management 
Sattelite teams 
data platform team
Anna Netlight

Should start with the data platform
Made in 2018

Skills to look at it. What is the GAPS? Best practices is for security.
Don't want something to take answer,  we want upskilling.
Knowledge transfer is there. 
Knowledge sharing. 
How open is the data team. They know what we need to do. o

Cost, team, estimation of GAP analysis. 
Realisticall 
Next steps: 
- Reach out 
- Prepare 
 


# Möte 
Mariah känner inte oss och därför viktigt att vi vill 
+ vill vara i teamen 
+ knowledge sharing 
+ GDPR råd
Viktigt att förklara skillnad mellan fas 1 och fas 2. 


---


Hi Claus,

We're really looking forward to the upcoming meeting with you this Friday. To make the most of our time together, we've put together a few questions in advance around the current data architecture and how personal data is used today in that system. 

We might not have time to go through everything and you might not have the answers to all questions, but hopefully this gives a good starting point for the discussion.

Good idea what data is personal data. Knows what the data are, but not headache how you go from pseudo and anonymization. 

**Data Architecture and Flow**
- Do you have any architectural diagrams you could share?
- How does data flow through your systems?
- Is the data processed in batch, streaming, or both?

![[Pasted image 20250627101214.png]]
Parquest files in s3
Write python code
Ingest snowflake 

Other teams upload to s3 copy. 
Snowflake vendor zuroa -> subscription. 
BI team is in love with snowflake. 
Open table format data lakehouse. 
Small programs to find the parquest files and remove and save it again. 
Snowflake is a possability as an engine. We have it under evalution. 
redshift 80% of the workload. 
And Athena. 
Powerbi report server. 

2-3 events per minute (not really streaming)
new platform Kafka stream to exchange data between system.  

100 000 million events tracking per day snowplow. 

Aprroximately 20 data sources. 
Commercial (advertising), subscription related and behviour, editorial content

Compliant for tracking? 

**Use of Personal Data**
- What personal data is collected, and in what volume?
- How does personal data move between systems? Who produces and consumes it?
- How much of the analytical insights/use cases rely on personal data?

- When login you get an id sso_id, linked to users email. 
- anonymized cookie ids
- IP address -> Are not used

- Subscription data have a lot of personal data remove when it's not necessarya
	- Accounting get affecting. It doesn't matter but if the sum is not day.  
	- Retention rules

Analytical data would be reduced if you remove that data. 

The possabilities of keeping data. Easy to understand conceptually tokenizaiton and remove it. 

It's difficult to get an answer related to this questions? GDPR and security function. Employed to 
**STUCK AT TAKING DECISION ON HOW TO EXECUTE**
The people in the analytical space say they can't proceed. 
**The number of users is forgotten is small**
Only allowed to keep behaviour data. Retention small. 
10 request per month. 
Workflow - Mara sends a document with person who should be forgotten. Few jupyter notebook. 

Need to track all the users that is consuming. 

They're not allowed to get copies. 
**Consumer only need the identifier**

### Data producing team 
not theirself 
1500 tables. We make the seggragation. 
 


**Legal Basis and Purpose**
- What consent mechanisms are in place for using personal data, especially for analytics?
- What happens if someone withdraws their consent?

**Data Subject Rights**
- What data subject rights processes do you have in place today?
- How is the right to be forgotten handled?
- How do deletion requests affect your reporting or metrics?

**Data Governance**
- Do you have an overview or inventory of personal data? Is it tagged and owned by specific roles?
- Who controls access to personal data, and are access controls in place?
- Do you log access to personal data? How is that monitored?
- How is personal data accessed, and by whom?

- Here are personal data. 
- Access control is coarse. If you work for politiken brand you can get access to politiken. 
- We don't have seperation behaviour  
- Only discussed on how separate it. 

Very nice if we can have it review to new snowplow. 

Really missing  

Business catalog - signy. What is PII. Help with documentation. 

4 people. But this are is super important and it will be prioritized. 

Claus builder by heart. Buy could be a good solution. A bit against. Hard to choose vendor.  

**Data Security**
- How is personal data secured? Is it encrypted?


# Help on Apache Iceberg 
How to setup? 
Victor is assigned to build enterprise architecture. Somewhere between his system. 

In the next 3 month roadmap. Gap analysis
Iceberg it worked and it was challenging. 
After the summer. Hands full right now, but maybe after the summer. 

