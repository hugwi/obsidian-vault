---
categories:
  - "[[Projects]]"
project: "[[Datahub]]"
created: 2026-06-23
---

The MediaMarktSaturn Retail Group is a German holding company with approximately 65.000 employees and the leading consumer electronics retailer in Europe in terms of revenue, sales area and headcount with headquarters in Ingolstadt, Germany. The Group operates more than 1000 stores and offers online shopping in 15 countries in Europe. MediaMarktSaturn runs a relatively new technology division in Munich with focus to improve existing and building new digital products.

Problem: 
Mediamarkt  Google Cloud data lake has +5PB data & over 100k data objects built over ~5 years. The tremendous volume and variety of data across the enterprise made it increasingly hard to find, understand and trust the data. 
To break data silos facilitating data sharing and enable data workers to consume governed, trustworthy data Mediamarkt accomplish this through data governance integrated with a data catalog.  

The Data Catalog was built use an open source product Datahub. Hugo was responsible for deploying the open source project to a Kubernetes cluster in and maintain it. He was also responsible for the integration between the Data Lake in Bigquery to ingest the metadata into the catalog.  


it difficult to understand the data’s origin, format, lineage, and how it is organized, classified, and connected.  
 - Increased visibility on key datasets that exist in the data lake
- Avoid double purchases of similar datasets by different teams
•Data Ownership often not clear
•Proper Governance impossible to establish
- Data silos
- Difficulty finding and accessing data

Miss insights in what datasets was used and valuable
•No entry point for finding, understanding and getting access to data in BQ

One of the most common challenges organizations face, though, with their data lakes is the inability to find, understand, and trust the data they need for business value or to gain a competitive edge. That’s because the data might be gibberish (in its native format)—or even conflicting
they need to add context to their data by implementing policy-driven processes that classify and identify what information is in the lake, and why it’s in there, what it means, who owns it, and who is using it.
Especially if that data is hidden in the data lake with no governance in place. A data lake without data governance will ultimately end up being a collection of disconnected data pools or information silos—just all in one place.

Solution:
This can best be accomplished through data governance integrated with a data catalog.
- Break data silos, enable data sharing across the organisation and expose duplication of existing datasets
- To understand upstream and downstream dependencies - lineage
Govern data by classifying data, understand usage and context as well as quality of the data
- Classify data
- understand usage and context 
- quality

The tremendous volume and variety of big data across an enterprise makes it difficult to understand the data’s origin, format, lineage, and how it is organized, classified, and connected. Because data is dynamic, understanding all of its features is essential to its quality, usage, and context. Data governance provides systematic structure and management to data residing in the data lake, making it more accessible and meaningful.
A data catalog’s tagging system methodically unites all the data through the creation and implementation of a common language, which includes data and data sets, glossaries, definitions, reports, metrics, dashboards, algorithms, and models. This unifying language allows users to understand the data in business terms, while also establishing relationships and associations between data sets.


This effort results in breaking down organizational silos of data, it often clarifies differences in similar data domains and often exposes duplication of data across the company.


Why data catalog? 
- Wasted time and effort on finding and accessing data
- Data lakes turning into data swamps
- No common business vocabulary
- Improved productivity and reduced time spent by teams searching for relevant information or data
- Increased visibility on key datasets that exist in the data lake
- Avoid double purchases of similar datasets by different teams

https://www.infoworld.com/article/3290433/data-lakes-just-a-swamp-without-data-governance-and-catalog.html


One of the most common challenges organizations face, though, with their data lakes is the inability to find, understand, and trust the data they need for business value or to gain a competitive edge. That’s because the data might be gibberish (in its native format)—or even conflicting
When the data scientist wants to access enterprise data for modeling or to deliver insights for analytics teams, this person is forced to dive into the depths of the data lake, and wade through the murkiness of undefined data sets from multiple sources. As data becomes an increasingly more important tool for businesses, this scenario is clearly not sustainable in the long run.
To be clear, for businesses to effectively and efficiently maximize data stored in data lakes, they need to add context to their data by implementing policy-driven processes that classify and identify what information is in the lake, and why it’s in there, what it means, who owns it, and who is using it.
This can best be accomplished through data governance integrated with a data catalog.

Especially if that data is hidden in the data lake with no governance in place. A data lake without data governance will ultimately end up being a collection of disconnected data pools or information silos—just all in one place.

Ungoverned, noncataloged data leaves businesses vulnerable. Users won’t know where the data comes from, where it’s been, with whom they can share it, or if it’s certified. Regulatory and privacy compliance risks are magnified, and data definitions can change without any user’s knowledge. The data could be impossible to analyze or be used inappropriately because there are inaccuracies and/or the data is missing context.

The impact: stakeholders won’t trust results gathered from the data. A lack of data governance transforms a data lake from a business asset to a murky business liability.

The tremendous volume and variety of big data across an enterprise makes it difficult to understand the data’s origin, format, lineage, and how it is organized, classified, and connected. Because data is dynamic, understanding all of its features is essential to its quality, usage, and context. Data governance provides systematic structure and management to data residing in the data lake, making it more accessible and meaningful.

A data catalog’s tagging system methodically unites all the data through the creation and implementation of a common language, which includes data and data sets, glossaries, definitions, reports, metrics, dashboards, algorithms, and models. This unifying language allows users to understand the data in business terms, while also establishing relationships and associations between data sets.