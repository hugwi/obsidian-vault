---
categories:
  - "[[Projects]]"
project: "[[Datahub]]"
created: 2026-06-23
---



Metadata test
https://datahubproject.io/docs/tests/metadata-tests/

### Automated Data Governance Monitoring


#datahub-cost
Cost for datahub is 1000 euro per cluster


Prevent Data Lake from becoming a Data swamp

Fair data
- Findable 
- Accessible
- Interoperableflood the data lake with unidentifiable mirrored data
- Reusable
https://www.go-fair.org/fair-principles/

https://www.dataversity.net/the-dangers-of-a-data-swamp-and-how-to-avoid-them/

- The data lake lacks proper protocols and guidelines for organizing and filtering data. This can lead to a build-up of old and irrelevant data.

**Keep it relevant:** Don’t hoard data if it isn’t relevant. Kept data should have clear purpose

**Establish necessities and goals:**  Establish clear intent on what kind of data you want to collect and the goals achieved with it.


**4. Document your data lineage and implement good governance processes**

Once people start using data in your data lake, they might clean it or integrate it with other data sets. Quite often it turns out that someone else has implemented a project that will have already cleansed the data that you are interested in. But if you only know about the raw data in your data lake, and not how others are using it, you are likely to redo work that has already been done. Avoid this problem by documenting data lineage thoroughly and implementing solid governance processes that illuminate the actions people took to ingest and transform data as it enters and moves through your data lake.

---
https://www.informationweek.com/big-data/four-basic-steps-to-prevent-your-data-lake-from-becoming-a-swamp
There are many other considerations that go into constructing a properly operationalized and governed data lake that aren’t covered here. However, these points provide a start if you want to have a data lake that works and provides value for your organization -- vs. a data lake that becomes a swamp.

---

https://medium.com/@ranjayd/navigating-the-murky-waters-of-data-swamps-identification-and-remediation-strategies-d016617c4fac

## Evolution of Data Swamps

**Inadequate Data Governance**: Many organizations underestimate the importance of data governance or fail to implement a comprehensive governance framework. As a result, there are no consistent policies, standards, or procedures in place to ensure data quality, security, and compliance. This lack of governance contributes to the deterioration of data lakes into data swamps.

**Insufficient Metadata Management**: In the absence of proper metadata management, data assets become poorly documented or lack adequate contextual information. This makes it difficult for users to understand the available data, locate relevant datasets, and effectively use them for analysis.

**Limited Resources and Expertise**: Organizations may lack the necessary resources or expertise to manage their growing data volumes effectively. This can result in insufficient data cataloging, data quality management, and data lifecycle management, all of which contribute to the development of a data swamp.

--- 

## Identifying a Data Swamp

There are several telltale signs that an organization may be dealing with a data swamp:

## Identifying a Data Swamp
1. **Slow Data Retrieval:** If data access and retrieval have become increasingly slow, it may indicate that the data lake has turned into a swamp.
2. **Lack of Metadata:** Poorly documented or missing metadata makes it challenging to understand and utilize the available data.
3. **Higher Volumes, Low usage:** When the overall data usage s low compared to collection. This may also be due to the lacking data lifecycle management

## Taking Corrective Action
**Adopt Data Lifecycle Management:** Implementing a data lifecycle management strategy helps to maintain data quality and relevance by identifying and eliminating outdated or unnecessary data.

---

For us two of the main issues was slow data retrieval and no clear data ownership and high volumes and low usage. 

---

https://www.linkedin.com/feed/update/urn:li:activity:7088929770696019968?updateEntityUrn=urn%3Ali%3Afs_feedUpdate%3A%28V2%2Curn%3Ali%3Aactivity%3A7088929770696019968%29

My advice is to think deeply about what guardrails and guidelines make sense at the current stage of your business, how you might enforce such guardrails through code, and how the guardrails scale as the business needs more or less governance over time.

---

Collect the more relvant data?


**Understanding the most important issues that you can solve for data workers**

---

**Question**: Do the ref clients we presented have a reference data model that would be a master on how different domains will be mapped
**Answer**:
Yes, at my client and the client I was before that they used a central repository where domains were mapped. At my last client when a new project gets created information such as domain and owner for that project needs to be added . The datasets in the project  simply inherits the tags/labels. 


---

**Question**: What were they able to do? -> Mirela’s ambition is that they can build a “business glossary” as part of the MDM
**Answer**: At my client we're currently defining and adding Business objects and Business KPIs to Datahub's business glossary as a part of MDM.  More info to how to do this in Datahub can be found here https://datahubproject.io/docs/glossary/business-glossary/.   

---

 **Question**: What tool has access to data sources? 
**Answer**: We only have one service account that has permission to read all tables to the project. You only need read permission since you only need to read the metadata. Our client is also going to need permission to alter data access to all the tables. 

 **Question**: Who has access to Data sources.  
**Answer**: Everyone will have access to all tables and metadata defined in catalog. Data owners and possibly data stewards will have permission to alter metadata in the catalog. 

**Question**:  When should a steward be involved and how many of them? 
**Answer**: At my client a data steward serves as a supporting function to the data owners and ensures maintenance of metadata. How many data stewards are needed depends on the scale and scope of data governance initiative. In some organisation the Data owner and steward might even be the same person.   


**Question**: Deletion of metadata? 
**Answer**: Datahub's ingestion is stateful which means that they can compare the state from the previous run and the current run to see which data has been deleted.  https://datahubproject.io/docs/metadata-ingestion/docs/dev_guides/stateful/

![[Pasted image 20230724210219.png]]

**Question**: 
How was feedback used from consumers to further improve the platform?
**Answer**: 
We have started to have UAT for additional features to understand what needs to be improved for that particular feature. It's also wise to have dedicated channel to understand what problems users are facing.  

---

**Question**: How to avoid data swamp?
**Answer**:

Since this depend on the organisation I'd say that these points are at least some of the key questions to ask to avoid the data swamp (or remedy the already existing symptoms) at least?   

**Understand the organisation data issues** 
Understand the biggest data issues the organisation currently is facing. Slow data retrieval, Poorly documented or missing metadata and data usage being low might need all be symptoms of a data swamp, but might need different solutions.  Understanding the biggest data issues an organisation if facing, guides where emphasis should be put, as well as which guardrails and guidelines you should have. 

**Guardrails and guidelines**
What guardrails and guidelines make sense at the current stage of your business. What guardrails can you enforce through code? 

**Interviews and Surveys**
One thing we did in our organisation to understand the issue data workers have was to have surveys and interviews with them.


**Requirement: Data consumer**
- Adding to Data Consumers: everyone should be able to consume also end-users --> features and also performance should be enhanced for the end-user
**- Not sure what this is referring to??**

---

**Data roles**

https://blog.satoricyber.com/the-datamasters-data-owners-vs-data-stewards-vs-data-custodians/
https://www.experian.co.uk/blogs/latest-thinking/data-quality/what-data-governance-roles-do-you-need-to-make-your-data-quality-initiative-a-success/