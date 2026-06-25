---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

https://www.keboola.com/blog/data-ingestion-tools?
## Airbyte

Airbyte is an open-source data integration platform and ETL tool that also supports data ingestion processes. You can either self-provision its open-source version or pay for the Cloud-managed Airbyte service. 

### Pros: 

- **300+ no-code connectors:** Airbyte offers a wide range of pre-built no-code integrations to speed up your data ingestion initiatives.  
- **Connector Development Kit (CDK)**: Airbyte streamlines new connector development with their CDK, giving you the freedom to build the connector you want. 
- **Extensible (open-source):** As the entire platform is open-sourced, you can customize it to your own needs. 
- **Real-time data streaming:** Many of Airbyte’s connectors are designed for real-time data streaming.

### Cons: 

- **Maintenance**: Building your own integrations is great. Just make sure to reserve some time for maintenance, support, and debugging which comes alongside developing your own connectors. 
- **Integrations lack maturity**: Many Airbyte connectors are still in the alpha stage and aren’t production-ready. Expect to work alongside the Airbyte team to flag issues, resolve them (often yourself), and maintain the Airbyte codebase.
- **Complex deployment**: Airbyte is user-friendly when accessed from its UI, but configuring the platform and deploying it requires a lot of engineering work. 

### Pricing: 

There are two ways to estimate Airbyte’s costs: 

- The **open-source** platform is free (minus the servers and engineering hours). 
- The **cloud-managed** platform will cost you at least $2.5/credit. Airbyte uses credits as a single pricing model for the differently priced services: database replication is priced differently than API data ingestion. Check their [pricing calculator](https://cost.airbyte.com/) to get a better sense of Airbyte’s expected costs.


Johan Blad![:palm_tree:](https://a.slack-edge.com/production-standard-emoji-assets/14.0/apple-large/1f334.png) [Sep 21st, 2022 at 9:57 AM](https://netlight.slack.com/archives/C04G2CJP6/p1663747030711369?thread_ts=1663745439.243669)
I have worked with Airbyte in a POC for my last client, hosting it ourselves. We decided not to use it for 2 main reasons:  

- We could (at the time) not configure our workloads as code, i.e. as `yml`  or similar, but we needed to configure them in the UI manually
- It was slower than we expected, and we did not see a reduction in runtime for our Data Integration workloads (we used AWS DMS / Glue before)

Christoph Klingspor![:lufthansatechnikag:](https://slack-imgs.com/?c=1&o1=gu&url=https%3A%2F%2Femoji.slack-edge.com%2FT0252T2EC%2Flufthansatechnikag%2F8a6c502c6e5c3655.jpg) [Jun 22nd at 5:17 PM](https://netlight.slack.com/archives/C04G2CJP6/p1687447062859249?thread_ts=1687445979.820329)

In the assignment I've looked at Fivetran, Stitch, Meltano and Airbyte. We went with Airbyte because of the big amount of integrations, the fact that we could fork a connector and develop it ourselves in case needed. Also I've written a very basic connector myself in that assignment.However, Airbyte (at least 8 months ago) did not allow for programmatic configuration. If this is still the case and the requirement is a deal breaker for you you have to look elsewhere

# Fivetran

### Pros
- Fully managed 
- Industry leading
- Integrates well with databricks 
- Could work for new sources as well

### Cons
- Might be costly 
- Can't add additional connectors

### Pricing 

MAR is a changed record (deleted, updated, inserted)

Fivetran labels its Standard plan as the most popular option among its customers. Its features are identical to those of the Standard Select plan. However, it caps neither the user number nor usage. With this plan, you can expect to pay between $180 and $3570 per month.

With the Standard Plan, your Fivetran pricing estimate will be:

- $180/month for 200K MARs
- $413/month for 500K MARs
- $750/month for 1M MARs
- $1,190/month for 2M MARs
- $3,570/month for 10M MARs
- $6,942/month for 50M MARs

Syncs take up approximately 15 minutes.

### CDC use case 

Getting data out of Salesforce incrementally can be very complex due to its poor unique ID support. For many Salesforce objects like Contacts or CampaignMembers, there is no guaranteed unique field that can be used to identify new vs updated records. 

Without defined primary keys, you would have to build custom logic to match records between Salesforce and the destination, handle duplicates, and prevent data loss. This sync logic needs to closely mirror Salesforce's internal sharing and update behaviour. 

With Fivetran, all this complexity is handled for you. Fivetran employs advanced heuristics to match records between Salesforce and destination when unique IDs are unavailable. It ensures duplicates are handled properly and all record changes are accounted for. 

Instead of spending time on complex duplicate identification and record matching, Fivetran enables you to be productive on day one with your Salesforce data. It operationalizes the difficult aspects of synchronization, so you can rely on accurate data in your warehouse.


# Azure Data Factory

### Pros
- Integrate well with databricks and azure eco system
- Have integration for snapshot, incremental and CDC
- Support to do inline transformation
- Also have transformation capabilities with data flows
### Cons
- Limited connectors 
- Vendor lock in (Azure) 

Azure service 
Payed ingestion tool 
Open source or Proprietary 


- **Cost**: Proprietary tools like Fivetran can be expensive, while open-source tools like Airbyte are free to use. However, open-source tools may require more time and resources to set up and maintain.
    
- **Ease of use**: Proprietary tools are often designed to be user-friendly and require minimal technical expertise. Open-source tools may require more technical knowledge to set up and use.
    
- **Customization**: Proprietary tools may offer more customization options, while open-source tools may be more flexible and allow for more customization.
    
- **Features**: Proprietary tools may offer more features out of the box, while open-source tools may require more customization to achieve the same functionality.
    
- **Support**: Proprietary tools often come with dedicated support teams, while open-source tools may rely on community support.

