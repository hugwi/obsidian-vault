---
categories:
  - "[[Clippings]]"
domain: [data-engineering]
tags:
  - governance
source: readwise
created: 2026-06-23
rating: 
action: 
---

# My MDM Framework

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*nT8IZ51m4aRwwqaG4YZXEg.png)

## Metadata
- Author: [[Willem Koenders]]
- Full Title: My MDM Framework
- Category: #articles
- Summary: The author presents a practical Master Data Management (MDM) framework that brings together strategy, governance, people, processes, and technology. MDM ensures consistent, accurate master data to support business transactions and use cases like customer management. Implementing MDM requires clear roles, integration with business processes and programs, and measurable value indicators.
- URL: https://medium.com/@willemkoenders/my-mdm-framework-4d2233f7e3f

## Full Document
There are many great MDM frameworks already out there, and for sure my personal version will have “borrowed” from them. That said, none of the existing ones really worked for me in any sort of real-life assessment. I’d have to use 2 or 3 at the same time to ensure that all critical components were covered.

My MDM Framework isn’t terribly complicated, nor will it contain things you can’t find anywhere else, but I think it does a decent job of bringing together *all* the major components of a fit-for-purpose MDM solution.

![](https://miro.medium.com/v2/resize:fit:700/1*nT8IZ51m4aRwwqaG4YZXEg.png)My MDM Framework 
If you are evaluating your current master data management maturity, or if you are reviewing a proposed future state solution, you should be able to take this framework and go box by box, asking yourself, “Do we, or should we, have this in place?”

In the remainder of this article, we’ll unpack the components of the framework and review how it can be tactically applied.

### **MDM Definition**

Before we do so, let’s make sure we clarify what we are referring to with “MDM.” It stands for *Master Data Management* and [can be defined as](https://en.wikipedia.org/wiki/Master_data_management) “a technology-enabled discipline in which business and [information technology](https://en.wikipedia.org/wiki/Information_technology) work together to ensure the uniformity, accuracy, stewardship, semantic consistency and accountability of the enterprise’s official shared [master data](https://en.wikipedia.org/wiki/Master_data) assets.”

To understand master data, you should consider what the *transactions* are for a given organization. These could be financial transactions, but I would interpret it more widely to include any sort of recurrent steps that enable eventual customer transactions and engagement (perhaps we can refer to these as “business transactions”). For each transaction, some data is new and unique — it only exists in the context of that one, single transaction. If we are taking the example of a store selling shoes, for a given transaction, this could be the Transaction ID, the timestamp, or the monetary value of that specific transaction.

But some data is required to make these business transactions happen that exists across many (or an *n-*number of) transactions. In the same example, the transaction is for a customer and covers a pair of shoes. For this customer, we have data on her name, bank account, and Customer ID, and for the pair of shoes, we have data on the type of shoes, for example its Product ID and the SKU. When the same customer comes in a week later to buy another pair of shoes, the same name, Customer ID, and bank account can be connected to the new transaction.

Theoretically, you could manually assign a number the first time she walks in, and write down her name and other relevant information on a piece of paper. The second time she walks in, you’d have to remember that this is not her first visit, and you’d have to retrieve that piece of paper for the initially captured information and to add new details. Of course, once business scales and becomes more complex, this become untenable. This is where MDM comes in — it uses technology to manage the critical data that *provides context* for business transactions.

The most common categories of master data include:

* *Parties* — data about organizations and individuals, and the roles they play. The most common use case is the Customer MDM, where master data for customers is stored and managed. Party data is important for virtually any organization, whether non- or for-profit.
* *Products* — data about the products (and possibly services) that a company sells. Important for most sectors, but typically critical for organizations selling a large number of products across a large number of customers, such as retailers.
* *Vendors* —data identifying the firms that an organization is procuring products and services from.
* *Materials* — [descriptions of all materials](https://www.verdantis.com/solutions/) that an enterprise procures, produces, and keeps in stock, particularly important in the manufacturing sector.

Having covered this, let’s dive into the framework components.

### (Master) Data Strategy

![](https://miro.medium.com/v2/resize:fit:700/1*5BRp5B9ypiDtj3TJiNxqqQ.png)
Deliberately at the top of the framework is the *strategy*. Yes, you really need this. You don’t necessarily need to have a long, written statement, but you do need to have guidelines to inform how MDM can create value.

*Data Assets* and *Trusted Sources* are called out as components. If your organization’s Data Strategy specifically calls these out as foundational capabilities, [which is the case ever more frequently](https://medium.com/@koendit/whats-the-big-deal-about-data-products-26ac347b7d7a), then chances are that there is a role for MDM, as it is foundational to creating and governing many data assets of such a nature.

Similarly, it is a good idea to identify actual, tactical *use cases* that exist within your organization that would benefit from MDM. If you don’t do this, you’ll have a much tougher job explaining why MDM is important, and chances are your funding requests will be denied.

Related to this, *performance indicators* can be derived to evidence MDM-powered value creation. For example, if the marketing team has “sales campaigns” as a prioritized use case, and they use the MDM-powered customer data source as an input, metrics around the number of successful outgoing calls or e-mails, and following increased conversion rates, can be powerful to evidence true value creation.

### Governance

![](https://miro.medium.com/v2/resize:fit:700/1*a5W5tAA01V5SK6R0SW5sBQ.png)
The function of the *governance* layer is to translate the strategy and objectives into implemented practices — how are we going to implement MDM, who is going to be responsible, and how do we ensure that it actually happens?

[*Policies* and *Standards*](https://www.complianceforge.com/faq/word-crimes/policy-vs-standard-vs-control-vs-procedure) are the first component. They codify explicit expectations, for example that critical customer data must be managed in a Customer MDM. Policies are broader statements of intent, whereas standards are much more tactical rules that prescribe how these policies are to be implemented. Once these are in place, a *compliance* process can be instituted to monitor adherence, with *governance forums* as an instrument to highlight, prioritize, and remediate compliance gaps.

Most tangible are *Roles* and *Responsibilities*. What are the roles in the MDM process, what are the corresponding responsibilities, and who are assigned to these roles? As we will see shortly, MDM is comprised of a number of very distinct processes, which is why across the entire topic it is recommendable to have a set of *process maps*, that outline these processes and their interdependencies, and connect them to agreed roles and responsibilities (ideally in a [RACI-format](https://www.cio.com/article/287088/project-management-how-to-design-a-successful-raci-project-plan.html)).

For all of these governance components, you don’t necessarily need separate instantiations for MDM. The overall data policy should contain references or perhaps a chapter dedicated to MDM; you can use existing data governance forums to discuss MDM; and MDM-related roles and responsibilities can be included in a broader data management RACI matrix. In fact, this is recommended, because fit-for-purpose MDM actually invokes a lot of adjacent data governance capabilities such as metadata and data quality, which also exist outside the scope of MDM.

### People, Process, Technology

The People, Process, and Technology (“PPT”) layer is where all the actual work is being done.

![](https://miro.medium.com/v2/resize:fit:700/1*gO8S4lS7aZFXXhnVhaFQhw.png)
#### People

The people component concerns the actual individuals that are involved in the MDM processes. Key roles include *Data Owners*, *Data Stewards*, *Process Owners*, and *App/System Owners*. These or similar roles should be identified and described, in line with the roles and responsibilities from the Governance layer, and they should then be assigned to actual people. These people might be hired for and dedicated to the respective MDM-role, but more likely, they already have a “day job” with existing responsibilities.

Across and against these roles, required or desired *skills* and *experience* can be defined. *Training* materials and instruction manuals can be used to upskill people, and a specific *adoption program* can be considered to ensure that MDM-roles are and stay appropriately implemented, with room for questions and support.

#### Process

Under process, we see all the actual processes that together make up the MDM-process. To call out a few:

* [*Data Modeling*](https://www.techtarget.com/searchdatamanagement/definition/data-modeling#:~:text=Data%20modeling%20is%20the%20process,or%20reengineering%20a%20legacy%20application.) is used to capture the conceptual and logical model, which is critical to consistently manage whatever data and quality standards apply to the master data.
* [*Metadata Mgmt.*](https://atlan.com/master-data-management-vs-metadata-management/) is critical to ensure that the master data is appropriately governed, where metadata can capture definitions, quality standards, and ownership for the data elements that make up the master data.
* A [*Data Quality* process](https://www.intricity.com/learningcenter/data-governance/whats-the-difference-between-mdm-data-quality) measures the fitness-for-purpose of the master data, which is critical to ensure that all of its downstream consumers can indeed trust it.
* [*Data Capture and Integration*](https://mastechinfotrellis.com/blog/integrating-data-with-mdm) are about managing where master data is created and captured, and how these inputs are integrated into the overall MDM solution. This may include not just identification and ingestion of a selection of master data sources, but also capture points of new master data values, for example within a call center.
* [*Entity Resolution*](https://towardsdatascience.com/an-introduction-to-entity-resolution-needs-and-challenges-97fba052dde5) and [*Survivorship*](https://www.youtube.com/watch?v=O7dhh9yAzgE&ab_channel=SandipM) describe the process where several sources might have data on the same unique record, where [these records need to be matched](https://www.quantexa.com/entity-resolution/#chapter-1). Where values differ (for example, where primary phone numbers for a given person are different) rules are defined and executed to [choose the “surviving” value](https://mdmlist.com/2019/08/22/three-master-data-survivorship-approaches/).
* [*MDM Remediation*](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE/6d52de87aa0d4fb6a90924720a5b0549/c0ba1cdbff3f4a48b12857be3e1d1f1d.html?version=2020.002) has to do with fixing the data within the MDM system or process itself, for example by remediating spelling errors in names. [Enrichment](https://www.ibm.com/docs/en/imdm/11.5?topic=integration-mdm-driven-data-enrichment) most typically has to do with bringing in new data to complement existing data, providing for a fuller understanding.
* When data is remediated or enriched within the MDM system, this can then be used to update the sources as well (*Source Remediation*). For example, for a given customer, the MDM system received “Jon Jones”, “John J. Jones”, and “John Jones” from 3 different sources. When it is clarified that “John Jones” is the correct version, the 2 sources with the incorrect value can now be updated.
* Finally, and perhaps most importantly, there is [*Sharing and Consumption*](https://www.pacificdataintegrators.com/insights/mdm-consumption-utilization). There is no value creation if no-one actually uses the governed master data. MDM data can be made available directly to consuming parties. In one example, a marketing team was planning sales campaigns directly based on MDM data. But it can also be used more indirectly, where the mastered data is used to update other distribution points (e.g., a separate CRM) that already have existing consumers.

#### Technology

Under technology, indeed we capture all the related technologies and capabilities that are needed to support the mentioned roles in the described processes. An overall data or solution *architecture* is important to understand the solution design and integration, which should outline how *storage*, *interoperability*, and *security* are embedded. See [here](https://learn.microsoft.com/en-us/azure/architecture/reference-architectures/data/profisee-master-data-management-data-factory\) for a great example from Azure.

Especially useful capabilities are *workflows* and *audit trails*. In some cases where records are gathered and reconciled, it is clear what the right, accurate data is. But in some cases, sources might have conflicting information, and the existing survivorship rules don’t lead to a proposed surviving value with sufficient confidence. In that case, data stewards can be looped in to review and arbitrate through [workflows](https://www.ibm.com/support/pages/want-know-about-mdm-workflow-we-have-answers).

When data is updated, it is critical — definitely in the early stages of adoption, when trust in the solution still needs to be earned — that there is transparency. In our “Jon Jones” / “John J. Jones” / “John Jones” example, it should be automatically captured and logged what the change was and what triggered it. This is also important to be able to improve the process. Both automated business rules and human data stewards can make mistakes and benefit from clarified guidance.

*Infrastructure Management and System Operations & Maintenance* refer to all the critical services required to keep the solution up and running. This includes monitoring of all relevant system operations, for example related to storage capacity, runtimes, latency, and patch management. Where specific issues are detected or requests are received to upgrade the system, work orders can be prioritized and processed through *Change & Incident Management*.

### Implementation

![](https://miro.medium.com/v2/resize:fit:700/1*J92hvEXp2pIzkYYVMnIDNA.png)
Having defined all the components of Strategy, Governance, People, Process, and Technology, there is one thing left to do, which is to ensure that we are implementing them consistently. This is easily overlooked as business leaders may assume that “someone would take responsibility” given that “everything is in place.”

But implementation of MDM is hard and disruptive. As we defined upfront, master data by definition is used across business transactions. So if you are changing anything about this master data — the standards that guide what valid values are, the location where to pull it from, etc. — this will impact a lot of people across a lot of processes.

With that in mind, let’s review a couple of channels and lenses through which MDM can be implemented:

* *Domains*. Master data can usually be mapped pretty directly to data domains such as Customer, Product, Employees, Vendors, Legal, and Finance. In general, it is a best practice to have some level of [domain-driven data governance](https://towardsdatascience.com/effective-data-management-with-domain-driven-and-product-thinking-approach-fc4ace13bddd), which is to say that for a given domain an owner is assigned who has responsibilities in terms of ensuring data governance and quality, including defining so-called trusted sources or approved distribution points. Enabling these domains with MDM capabilities will be a very powerful, direct way of driving implementation across the enterprise.
* *Transformation Programs*. Implementing an MDM solution can be a transformation program by itself, but here I am more referring to all the other transformation initiatives in the enterprise. It is much easier to influence design at the drawing board than trying to get data flows changed after implementation. Ensuring that MDM guidelines and principles are considered during the architecture design phase of data transformations is a path of relatively low resistance yet enormous impact, because if consistently done, over time it will benefit the entire organization.
* *Business Processes.* Similar to domain-driven data governance, it is a best practice that business process owners have a role in data governance. They should have a responsibility to ensure that their business process abides by data policies and standards. If a business process is a producer or consumer of master data, that implies that MDM best practices and standards should be observed. For example, a Customer Onboarding process should feed updated data into a customer MDM solution, and an Outbound Customer Engagement process should consume the right contact details that are in sync with the customer master. Often, process owners are preoccupied with the business-side of their process, and bringing up data governance may trigger a reaction that it impedes their business and that they don’t have time for it. But if explained well, practically any process owner will go along as MDM is the single-biggest lever of guaranteeing data quality and consistency for the stakeholders of their process.
* *Remediation Programs*. Finally, MDM is often introduced because it is part of a solution to a set of issues. In one example, I worked with a leading insurance corporate group in Latin America. The enterprise had separate divisions dedicated to health and life insurance, retirement, car insurance, and various insurances for businesses. Each division managed its own customer data, even though people could be customers across several divisions. When customers called to update their contact information, it would be updated in one place, but not the others. Also, cross-selling was virtually impossible as there was no effective means of understanding the customer across the different product groups. As you can imagine, MDM was a very logical solution to help synchronizing and enhancing data across product divisions, and in this case, it became its own remediation program.

### Closing

I’m afraid… that’s it! For me, this framework of sorts has helped me understand specific organizational situations, as it enabled me to map issues and opportunities to specific framework components. Here, the logic flows both ways: if any one component of the framework is overlooked or insufficiently built out, your MDM solution will fail, but if each component is respected and given appropriate attention, success is inevitable.

*All expressed opinions are my own, and are not attributable to any organization that I may or may not be, or have been, affiliated with.*
