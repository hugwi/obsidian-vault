Tokenization and encryption can be combined! 

## Next steps
- How is data retention respected? 
- How do we want to setup account deletion? 
- Is TLS enough for data in transit? 




# Thoughts 

If we collect data from legitimate interest, such as GA or subscription to provide user journeys. We need to make sure when **consent** is given they **can't be connected to tokenized behaviour**. 

The disclosure of additional data over the years (e.g. in a personal data breach) can make it possible to link previously anonymous data to identified individuals.

# Questions: 
- Will it be easier to get raw data or to do they do any cleaning?  
- What are the source systems and how are they ingested? They don't get email data from where? 
	- Do the PII from on prem has the same level of sensitivity?   
+ What PII data do we actually need? 
- Is it ok that data land unanonymized in a staging table that then gets removed? x
- If you don't have consent for more that legitimate interest can you still store the data anonymized? 


# 

# Data access 
#data-access
Hello,  




# Consent management

Two consent management systems. They will be 
synchronized. Can put a token vault. One is for cookiedoo 52 countries, need to serve the 
sales organization when they get in custom. CDC take care of their eshop, CRM. I give one consent when I buy the device. 
We want to unify the consent, but now it's managed as two entities.   

# GDPR 

## PII collection
One bucket for errors and device is one stream.
Personalization is another stream.
IP is collected from AWS but then 

# Data portability 
Data portability is done by a huge query for DCID and email. Hasn't been too many requests yet. 
It would be good in general to have the concepts of tagging and GDPR. Customer data, behavioural data.

**Verify the identify of the individual**
![[Pasted image 20240115143909.png]]

# Data tagging 

We don't have a global catalog. Metadata would be an important data. Materialize. Databricks unity catalog. Share catalog aligned. 

Usage data. id for recipes that is created by the customer. If you need that data.

Question: Should data be tagged on table level or column level? There might be for instance column level tags for PII data. 

Should policies/tags be soft or hard enforced? 


```
[ ... {   "name": "ssn",   "type": "STRING",   "mode": "REQUIRED",   "policyTags": {     "names": ["projects/project-id /locations/location /taxonomies/taxonomy-id /policyTags/policytag-id
"]   } }, ...  
]
```


https://medium.com/@andrewpweaver/identifying-and-tagging-pii-data-with-unity-catalog-870522f25730
https://github.com/andyweaves/databricks-notebooks/blob/main/notebooks/privacy/information_schema_pii_tags.sql

	
# Data access

https://docs.databricks.com/en/data-governance/unity-catalog/row-and-column-filters.html

Can we use something like this to filter out PII? 
![[Pasted image 20240116131718.png]]

# Data deletion of deactivated account

800 users a week want to have their account deleted 
On a monthly basis Service management provide consolidated list of ata that needs to be deleted. 

**Thoughts**
Should one keep the data for an extra time in case of something is wrong? For example the account? 


# Anonymization


# Pseudanonymization

## Tokenization

### Implementation 
#tokenization-implementation

Streaming [#pseudonymization](https://www.linkedin.com/feed/hashtag/?keywords=pseudonymization&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A6910601404818620416) with a central token store requires efficient caching. At Mathem we use Caffeine to cache tokens in the [#dataflow](https://www.linkedin.com/feed/hashtag/?keywords=dataflow&highlightedUpdateUrns=urn%3Ali%3Aactivity%3A6910601404818620416) workers and use Firestore as a central token store. We also use the same caching technique to cache the schemas (contracts) we use to serialize data. The difference is that tokens expire on read while schemas refresh on write. The reason is that tokens are immutable and we want to cache tokens that are frequently used while schemas evolve and we refresh them with a configurable interval. In the attached screenshot you see an example from our test environment with custom metrics counting the number of schema and token cache calls and the number of misses and that caching significantly reduces the load on the data catalog and Firestore APIs (cache miss rate: 0.0006% and 0.02%).  

**Tokenization with encryption**
![[Pasted image 20231205154732.png]]
  


 https://freedium.cfd/https://ketansoni.medium.com/data-tokenization-9c5aa213cd71

### Vault Based
#### Concern
- Performance: Look up can become expensive if the list of mapped values grows over a period of time. More the number of mapping, the slower the lookup is.
- If the vault key is compromised, all the actual values are exposed.
- <mark style="background: #FF5582A6;">if the vault based tokenization server is hosted in various regions then it requires an expensive synchronization capability in order to keep it out of the loop of collision.</mark>  #tokenization-concern

### Vault less


### **Points to consider while choosing the tokenization provider**


### Token Generation capabilities

- Should support bulk token generation for data bundled in CSV or batch so that round trip time between calling service and tokenization server can be reduced.
- Should support token generation for JSON based requests.
<mark style="background: #FF5582A6;">- It should be able to generate tokens for the different data types for e.g. alphanumeric, numeric, Date and boolean.</mark>
- <mark style="background: #FF5582A6;">It should be able to generate tokens for multibyte characters with accented characters (for e.g. [umlaut](http://www.disknet.com/indiana_biolab/ger004.htm) characters) by <mark style="background: #FF5582A6;">preserving</mark> appearance, length and delimiter.</mark>
- <mark style="background: #FF5582A6;">Some PII fields like surname can be two or three letters (for e.g. Yu or Lee), it should be able to generate tokens for those by either padding or some other mechanism. Reason being de-tokenization of two characters can be hacked.</mark>
-<mark style="background: #FF5582A6;"> Should support the prefix or suffix for an application to identify the multi region tokenized data so that it can be routed to the appropriate region for de-tokenization.</mark>
-<mark style="background: #FF5582A6;"> Should be able to perform partial tokenization for e.g. for a given 16 digit credit card number just tokenize first 12 numbers and keep the last 4 digits real.</mark>
-<mark style="background: #D2B3FFA6;"> Should be able to provide VaultLess tokenization service.</mark>
### Performance:

- Should be able to generate thousands of tokens fast and secured else this could become the biggest bottleneck.
- Should be able to handle the request coming in MBs and should provide the response faster.

###  Scalability:

- Should be scalable if the number of connections that performs tokenizations and not just by throwing a hardware to existing tokenization server farm.

### PCI and CCPA/GDPR compliant:

- Ensure provider understand PCI and GDPR compliance, security, and the risk.

### Sensitive data

SNR - was bought by this person that's why it's sensitive.

---

### Deleting DCID
#right-to-be-forgotten
#dcid
#deletion

According to Benedikt the reason why they need to delete dcid is described in [SIM-15780] Deletion of customer data incomplete when customer requests account deletion ticket. Document can be found [here](https://vorwerkholding.sharepoint.com/:w:/r/teams/DatabricksEval/_layouts/15/Doc.aspx?sourcedoc=%7BAA76D4C0-85A9-42AA-9814-6C2E951896B0%7D&file=SIM-15780.doc&action=default&mobileredirect=true).

However I still can't figure out how this has anything to do with the DCID?


# Meeting 1 December

Valentina - In the same team as Yevgen, working Business, PM for datahub, collect data in cookiedoo
Benedikt - Anonymization, cozy 

We don't need PII data like email, last name. We try to reduce the data. 

**Usage box** 
Created mapping table between digital id and usageboxid

Cookie doo
Digital ID. Is used across cookie doo.
Remove mapping between userdeviceid usageboxid  
Terrabytes of data. 
Subscription data. 
**Assumed that dcid is already the token? When dcid and email adress is this kept if they delete their account. In bulk deletes every dcid that needs to be deleted and runs through all the** Created own user id and mapping.  
<mark style="background: #FF5582A6;">Only users box uses the actual mapping. </mark>

We does the informatica 
Saves Usagebox id 
We need to share the the mapping. 

 Since we need to connnect sales data and cookiedoo. We need to have the email. 

At the moment information factory doesn't get the data from datahub. Get's the data from adobe campaign. This is we need the email. They're getting the email from the address and the dcid. Combined view is already connected. email adress from sales and from cookiedoo dcid and the email. 

List that someone distribute. Christofs teams. 

Cookiedoo they have not an atuomated process for right to be forgotten but get s done manually.  
We have a table for  

DPO anita in BI. We just designed that. Wasn't much input on the decision. 
Agreed with DPO that if there isn't a link it's good enough to encrypt. 

Requirement is high level of right to be forgotten.

Right to be forgotten: We need 3-4 months tecnically. 

Thoughts: 
Benedikt 
- Nobody will touch
cozy - 
I'll keep the simple. Tokenizatoin usagebox is simple. 
Start with a nifty, simple process. Validity times. 
Legal topic is causing frustration and complexity. 

Valentina
Tokenization in usage box works.  
We thought dcid was enough for it to be anonymized. **Useful to deal with the GDPR. Governance tagging PII data. In datasets and column. And give access to the data.** 
Request to have access. If we can tokenize everything all people can have access to everything and people give permission to the vault if they need anonymized data. 

Data privacy meeting: 

1. Start showing what you already now? Give background to our project? 
- What was the reason choosing vault tokenization over vault less tokenization with encryption keys? 
3.  Deep dive into the tokenizatin process? Any more in depth documentation? 
- Can we reuse the logic for tokenization? 
- How fast do data need to be forgotten? 30 days?
4. Sync between clouds? 
- How can tokenization be done in multi cloud? 
- Follow vs leaders? 

Next steps: 
- How do we synchronize 
- We provide the data anonymized dcid. 
- Question for Pietro: Possible to join with email and rebuild a customer. 
- Complexity to maintain and keep use the tokenization of the other data.  
- Discuss how they thought their current system. 

---
## Meeting 19/20 December

Why have the token instead of not having it at all?

How do we collect history of a customer behaviour. 

Mapping is removed which makes us loose the data. 
Collect data for consumers that don't have consent. 

Have session with DPO if we can collect dcid. 

How often customer change consent status?
usagebox id is renewed everytime they use new consent

dcid when customer create the account
	
mapping usageboxid and dcid is done with a microservice
How to retain information about anonymized users. 

How to deal with token vault, when we have dcid

---

All data points can be collected since it's covered by legitimat4 einterest
Got a list with all data points need to be anonymized. Device id and user id needs to be anonymized. 
If we have consent we can use the dcid, but if we don't have consent we can't use it. 
Will also have data where we don't have a cookiedoo 

We could go live in the beginning with data with consent. 

Recipe optimization and product improvement. Need identifier for user. 
serial number and dcid makes a session unique.

not possible - but with a lot of effort. 

Can continue with priority 1 but not 2.
Linkability - 

DS360 - Doesn't change much. Will receive all the data if there is in consent. Since we're collecting serial number and you'll have the serial number in the sales data. Probably we don't want ingest serial number from sales data. 

Landing zone has retention period of 1 week or x days of receiving it. It's not persisted. 
Needs to be anonymized if we store it without consent. DCID and SNR. 

Personalization in customer 360 relates to customer consent. 
Consider what other PII we have. 
A list what's requirered in the platform. We should think which data is needed for customer 360. 
Do we need to consider marketing consent. If we use emarsys we don't need to enforce marketing consent. 
Only personalization consent is relevant not marketing. 

Problem with consent change is historical data. A little bit more problem with historical data. Is usagebox the only historical data. 
If it's a fact table you can use it or not use it. You delete the history or you keep storing the. 
See if we have other with history, then we need to set it up as different users depnding on consent. 

Discuss the scope and what data 

---

## Meeting notes 12 Jan

 Device would call for the consent decision. 
 We didn't separate the data. The streams are separated. 

One bucket for errors and device is one stream.
Personalization is another stream.

Do we need to store personal information since we don't have use cases? Ip address, serial number, we can collect but should we? The IP will only be used to derive geo location. Hashed serial number. All the ids. 
Resolution? Not precis location, No postal code. Region.
Types of recipes are cooked where. Send invites cooking classes.   
IP address is better since it's not enough to know where it was bought. 
TM6 and Cosy is location.
Yevgen: Location should be enough
DS360: We need to remove if it's 

Use the tokenization for serial number, introduce to Benedikt. Usagebox data and, connected devices and utensiles. 
Mechanism for removing PII data. We never store email. 

Cannot incorporate Hugo in DS360. 

It doesn't need to be implementing now. We don't have the complexity for the team if I can support the technical team. 

### Data portability 
Huge query for DCID and email. Not many requests. 
It would be good in general to have the concepts of tagging and GDPR. Customer data, behavioural data.

### Data tagging 

We don't have a global catalog. Metadata would be an important data. Materialize. Databricks unity catalog. Share catalog aligned. 

Usage data. id for recipes that is created by the customer. If you need that data.

### Data vault 
Databricks concept for data vault

---
## Meeting Gustav Osswald 
- Workshop? 
- Vad förväntas platformen användas till? 
+ Soft or hard enforcement? 
Bygg en hard enforcement. För viktigare topics som tex data owner. 
Bygg en minimalistisk i början

Mentimeter - Var hittar vi data information? 
