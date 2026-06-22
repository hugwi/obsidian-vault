https://www.dataversity.net/data-governance-vs-master-data-management/

Master data is a type of data that describes subjects related to the **‘who,’ ‘what,’ and ‘where’** in business transactions communications, and events. The ‘who’ could be a customer or an employee; the ‘what’ could be a product or service, and the ‘where’ could be a store, office, or a virtual location.

---
https://www.datamation.com/big-data/data-governance-vs-data-management/

## **What Is Master Data Management (MDM)?**

[Master data management (MDM)](https://www.datamation.com/big-data/master-data-management-implementation-styles/) is the overlap of technology and business operations to enforce the policies of data governance, ensuring the uniformity, accuracy, and accessibility of the enterprise’s data. By consolidating the data, MDM ensures it’s consistently synchronized across the various systems, bridging data islands to create a seamless flow of up-to-date data and information.

MDM combines software and other tools, processes, and the mechanisms outlined by an organization’s data governance policies to ensure that master data is governed and coordinated across the enterprise with high accuracy and integrity.

### **Components of MDM**

MDM isn’t a single entity, but a combination of multiple technical and operational components. Each of the following plays a role in the [data management process](https://www.datamation.com/big-data/data-management-trends/):

- **Data Integration**—Integrates incoming data from legacy systems, CRMs, ERPs, and external data feeds into a central repository to offer a comprehensive view.
- **Data Quality**—Ensures that the consolidated data maintains its quality by removing duplicates, rectifying errors, and filling in gaps to ensure a complete set.
- **Data Governance**—Controls who can access the data, how it’s categorized, and how often it gets updated.
- **Business Process Management**— Updates data seamlessly as processes change (for example, during a product launch or merger).

---

https://towardsdatascience.com/why-data-governance-matters-master-data-management-mdm-5d9af0f64573

# What is Master Data?

Let’s start with understanding **master data**. It is, after all, what we are aiming to manage.

A definition on [Wikipedia](https://en.wikipedia.org/wiki/Master_data): _Master Data represents the business objects that contain the most valuable, agreed upon information shared across an organization._ [1]

Another one: _Data about the business entities that provide context for business transactions._ [1]

A bit vague right? It’s a tricky term to define. Below are a few examples of data considered “master”:

- Customers
- Products
- Services
- Vendors

In my own words, I would describe MDM as "trying to make sure master data is distinct and has minimal quality issues"

Wikipedia: _Master data management (MDM) is a technology-enabled discipline in which business and information technology work together to ensure the uniformity, accuracy, stewardship, semantic consistency and accountability of the enterprise's official shared master data assets. [2]_

### What problem does MDM solve?

MDM aims to resolve **duplicate master data.**

The main idea here is there are duplicate records of master data across the enterprise. Examples include:

- Multiple instances of the same customer with different addresses and phone numbers, etc.
- Multiple versions of products sold with the same name but different attributes. Or worse, multiple products with slightly different-worded names with the same attributes
- Multiple Vendors with the same name but different attributes

Let's look at duplicate customer examples at a fictional Auto Repair shop, "Car Repair ABC".

- Ben has an existing account with Car Repair ABC, but he opens up another membership with a different email accidentally. This leads to two instances of Ben in their system. _This is an example of duplicate records being created due to an internal control limitation._
- The advertising department of Company ABC has its own database which contains both current customers and prospective customers. This database does not have a 1:1 match with the customer records of sales, accounting, etc. _This is an example of duplicate records existing due to siloed / segmented source system processes within an enterprise._
- Merger and acquisition: Car Repair ABC purchases a smaller auto shop. If Sally has accounts at both stores pre merger, there will likely be multiple instances of Sally post merger. _This is an example of M&A-related duplicates._

These are a few basic examples of duplicate data. It's important to remember this issue isn't solely for customer data. The same principles can apply to the products, services, employees, or any other [master data](https://en.wikipedia.org/wiki/Master_data).

---
https://atlan.com/databricks-master-data-management/#what-is-master-data-managementk

## What is master data management?

[Master data management](https://atlan.com/master-data-management-vs-metadata-management/#what-is-master-data-management) is a process that involves creating a single, authoritative master record for each key entity in a business, such as people, places, or things, by aggregating, de-duplicating, reconciling, and enriching data from various internal and external sources and applications.

This master data becomes a reliable and consistent source that is managed and shared across the organization. The purpose of master data management is to:

- Provide a trusted view of critical business data
- Enhance accuracy in reporting
- Reduce errors and redundancies in data
- Support better-informed business decisions

---

https://cloud.google.com/blog/products/data-analytics/how-tamr-delivers-master-data-management-at-scale-with-bigquery
![[Pasted image 20240130172950.png]]

---

Master data
![[Pasted image 20240130174616.png]]
https://www.youtube.com/watch?v=SkZCQ6KZfi0
![[Pasted image 20240130174358.png]]

https://winpure.com/blog/guide-to-master-data-management-mdm/
![[Pasted image 20240131105121.png]]


https://www.linkedin.com/advice/3/what-main-challenges-benefits-implementing-1c?lipi=urn%3Ali%3Apage%3Ad_flagship3_search_srp_all%3Bw6OQffJDQl%2BLeoGuESL8Ow%3D%3D

For those starting their MDM journey, establishing a rigorous data quality program, for the source systems that will feed into your MDM solution, should precede the implementation of your MDM solution. MDM solutions assume that incoming data is complete and accurate. In order for MDM to combine multiple instances of the same party record (coming from numerous source systems) into a golden record, it is important to ensure the data fed into MDM is of the highest quality. Ensuring high data quality standards are in place prior to implementing your MDM will significantly improve the chances of success of your MDM implementation.

One of the main benefits of MDM is increasing the value and usability of your data. By having a **single source of truth** for your master data, you can **eliminate data silos**, reduce **data redundancy**, and improve **data consistency** and **reliability**. This can help you optimize your business processes, workflows, and systems, and increase your operational efficiency and agility. You can also leverage your master data for better analytics, reporting, and insights, and enhance your business intelligence and performance.


https://www.linkedin.com/pulse/why-master-data-management-matters-ganesh-gajre-pma6f/
Master Data Management is a methodology that involves creating a single, consistent view of critical data entities within an organization.

The Master Data Management market is witnessing significant growth, driven by the increasing importance of data quality and governance

**Master Data Management Tools**

Implementing a successful MDM strategy requires the right tools. Here's where [master data management](https://quadrant-solutions.com/download-form/market-research/market-share-master-data-management-2022-2027-worldwide-2810) tools come in. These software solutions automate various MDM tasks, including:

**Data cleansing and standardization**: MDM tools identify and remove inconsistencies in your data, ensuring all formats and definitions are aligned.

**Data matching and consolidation**: These tools help you identify duplicate records and create a single, unified master record for each entity.

**Data enrichment**: MDM solutions can enrich your master data with additional information from external sources, providing a more comprehensive view of your data.

https://www.linkedin.com/pulse/unlocking-data-potential-mastering-business-insights-suryawanshi-rbnmf/

The proliferation of advanced analytics platforms coupled with the expansion of the market has exacerbated the issue, resulting in disparate data silos, outdated information, and inconsistencies across systems. These data integrity issues have severe repercussions, impacting crucial business functions such as Customer Relationship Management (CRM), Enterprise Resource Planning (ERP), and Supply Chain Management (SCM), ultimately compromising the accuracy of analytics.

One of MDM's key features is its support for data governance, empowering users to define data definitions, standardization protocols, access rights, and quality rules. This governance framework, augmented by metadata management capabilities, captures intricate business entity relationships and hierarchies, ensuring consistency across data migration processes.

[# Actionable Data behind Digital Transformation: A Discussion on MDM and CDP.](https://www.youtube.com/watch?v=POYFgbN5ir8)

![[Pasted image 20240325183722.png]]


https://www.tamr.com/blog/what-is-customer-master-data-management
#### **What are common data sources for Customer Master Data?**

While the list of internal and external customer data sources is long and varied at the enterprise level, common key sources of customer data are:

1. ERPs e.g. SAP, Oracle
2. CRMs e.g. Salesforce, Microsoft Dynamics
3. Marketing automation tools e.g. Adobe Experience Cloud, Eloqua

#### **Components of Customer Mastering**

**Persistent IDs**: Creating a unique ID that connects customer records within and across systems and enables a golden record view of customers, grouping the underlying records to ensure accurate, consistent information feeds a holistic customer view.

**Deduplication**: Identifying where there are erroneous or necessary duplicate customer records to ensure that the same underlying customer is treated as one

**Data aggregation**: Joining customer information across disparate systems and business units to provide a truly holistic view of interactions. Customer data can be continuously integrated with operational and analytical systems so changes in customer information and behavior is seamlessly flowed through the enterprise to reflect in business reporting and actions.

An ultimate Customer Master Data set should be a high-priority goal for the organization hoping to best leverage their digital assets in line with [key DataOps principles](https://www.tamr.com/blog/key-principles-of-a-dataops-ecosystem/).


https://www.getcensus.com/blog/what-is-master-data-management-master

### Definition and Importance of MDM

Master Data Management can be defined as the process of creating, managing, and distributing master data across an organization to ensure data consistency, accuracy, and integrity. The goal of MDM is to provide a unified and accurate view of master data, eliminating data silos and inconsistencies that may arise from disparate systems and applications.

The importance of MDM in today's data-driven world cannot be overstated. Organizations generate vast amounts of data each day, and it is crucial to have a solid foundation of accurate and consistent master data. MDM enables businesses to make informed decisions, improve operational efficiency, enhance customer experiences, and comply with regulatory requirements.

### Key Components of MDM

Master Data Management comprises several key components that work together to ensure the success of MDM initiatives. These components include:

1. **Data Governance:** Data governance establishes policies, procedures, and responsibilities for managing and maintaining master data. It ensures that data is accurate, consistent, and compliant with regulations.
2. **Data Quality Management:** [Data quality](https://www.getcensus.com/blog/understanding-the-significance-of-data-quality) management focuses on assessing, improving, and maintaining the quality of master data. It involves activities such as data profiling, cleansing, and standardization.
3. **Data Integration and Consolidation:** Data integration and consolidation involve bringing together master data from various sources and systems into a centralized repository. This process eliminates data redundancies and inconsistencies.
4. **Data Security and Privacy:** Data security and privacy are crucial aspects of MDM. It involves implementing measures to protect master data from unauthorized access, ensuring compliance with data protection regulations.
5. **Continuous Monitoring and Maintenance:** MDM is an ongoing process that requires continuous monitoring and maintenance to ensure data accuracy and integrity. Regular audits, data cleansing, and updates are essential to keep the master data up-to-date.

### Benefits of Implementing MDM

Implementing Master Data Management offers a wide range of benefits for organizations. Some of the key benefits include:

- **Improved Data Quality:** MDM ensures that master data is accurate, consistent, and reliable. This improves the quality of data used for decision-making and operational processes.
- **Enhanced Operational Efficiency:** By centralizing and standardizing master data, MDM eliminates data redundancies and inconsistencies, leading to improved operational efficiency and streamlined business processes.
- **Better Business Insights:** MDM provides a single, unified view of master data, enabling organizations to gain valuable insights into customers, products, and other key entities. This, in turn, supports data-driven decision-making.
- **Compliance with Regulations:** MDM helps organizations comply with data protection and privacy regulations by establishing data governance policies and implementing security measures to protect master data.
- **Improved Customer Experience:** With accurate and consistent customer data, organizations can provide personalized experiences, targeted marketing campaigns, and better customer service.
- **Increased ROI:** Implementing MDM can result in a positive return on investment, as it improves data quality, operational efficiency, and business insights.

#### Red Wing Shoes: Consolidating Data for Operational Efficiency
Prior to implementing MDM, Red Wing Shoes faced challenges in maintaining consistent customer information across their retail stores, e-commerce platform, and customer service centers. With MDM, they were able to create a single, unified view of customer data, enabling them to provide personalized experiences, targeted marketing campaigns, and improved customer service.


#### IBM: Unifying Customer Data for Personalization

IBM, a global technology company, implemented MDM to unify their customer data and enable personalized experiences for their clients. With a vast customer base and a wide range of products and services, IBM faced challenges in identifying and understanding their customers' needs and preferences.

By implementing MDM, IBM was able to consolidate customer data from various sources, including CRM systems, sales databases, and marketing platforms. This allowed them to create a comprehensive [Customer 360](https://) view, which provided a holistic understanding of each customer's interactions, preferences, and history with the company.

With the Customer 360 view, IBM was able to deliver personalized experiences, targeted marketing campaigns, and tailored product recommendations to their clients. This helped them build stronger customer relationships, enhance customer loyalty, and drive business growth.

### Establishing a Data Governance Framework

Data governance is a critical component of MDM and provides the foundation for successful MDM implementation. It involves establishing policies, procedures, and responsibilities for managing and maintaining master data. A robust data governance framework ensures that data is accurate, consistent, and compliant with regulations.

Key elements of a data governance framework include:

- **Data Governance Council:** Establishing a cross-functional council responsible for setting data governance policies, resolving conflicts, and making strategic decisions related to master data.
- **Data Stewardship:** Assigning data stewards who are responsible for data quality, data integrity, and ensuring compliance with data governance policies.
- **Data Standards and Policies:** Defining data standards, data definitions, and data quality requirements to ensure consistency and accuracy of master data.
- **Data Governance Processes:** Implementing processes for data profiling, data cleansing, data integration, and data lifecycle management.

By establishing a robust data governance framework, organizations can effectively manage and maintain master data, ensuring its accuracy, consistency, and integrity.

---

27 Mars 

 Varför? 
 Varför behöver vi enhetliga begrepp?  
 Hur definierar vi ett användare? 
 operationell för analytiska? 

9-13 nästa tisdag. Enbart placeholder.  

Customer stitching? 
System för att definiera data entities?  
Dokumentera hur vi definierar olika "master data" till exempel vad är en användare. 
Usually have a customer interface. 
Ownership for data definitions. Mathias client, manually update stitching that didn't work. Will we have similar problems.  
Risk where data sources isn't consistent. 
MDM systems becomes hub where CRM, ERPS can get master data. 
Governance is also a bigger part of it. How owns the data sources and definitions? 
Could have different systems that owns certain columns of the customer data.  

How does organization support that? One responsible person? Analytics manager take part of that? Is there one person that is 100% responsible. 

---

Meeting 31 Jan - Gustav Kullberg, Dennis Rosell

Man skapar samma data i olika system och de är olika 
E är inte golden standard. Man behövde en applikation där man behövde ett data projekt. 
Finns för mycket features. 
Investors matchar ihop de till olika records. Governance på kolumn nivå. Ni har 50 olika "kategorier"
Data governance i källsystemen, harmoniserar. Erik Dahlberg E 
MDM verktyg kan godkänna begrepp och verktyg. Lätt att de får för stort scope. 
Allt är så generellt att när vi behöver MDM verktyget är så generellt att det inte fungerar. 

Bygger på att man inte kan kontrollera data. 
Ingesta datan och validera den och se att den går bra. Ha transparency. 
Mappning måste bli rätt som jag inte skickar ett mail till rätt. 
Master data är det viktigaste i informationen. 
3rd part system. EBX. Stichningen är jord för hand i javascript. 
Reglerna. 
Framförallt dimensionsdata. 
Skapa foregin key master. Minimala i MDM. 
Manuellt göra mappningar eller automatiskt. 
Hur får man det automatiska och det manuella att lira tillsammans. 
Vi har en excel fil det finns inga regler bakom den. 
Beror vi på vilka datakällor vi drar in. 
Vad är det för problem man ser och inte använda ett MDM verktyg om det inte behöv . 
Dashboard över icke validerade punkter. 