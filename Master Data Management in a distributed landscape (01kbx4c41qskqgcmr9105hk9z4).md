---
categories:
  - "[[Resources]]"
domain: engineering
title: "Master Data Management in a distributed landscape"
source: "https://medium.com/@winfried.etzel/master-data-management-in-a-distributed-landscape-4ff10b7118eb"
author: "Winfried Adalbert Etzel"
published: 2024-06-18
created: 2025-12-07
description: "Prior to the rise of Data Mesh, as a conceptual shift in how we think data"
tags:
  - to-process
  - data-engineering
---

Prior to the rise of Data Mesh, as a conceptual shift in how we think data for scale in organizations, large-scale software projects like Master Data Management (MDM) dominate the “tech-heavy”, and certainly investment-heavy aspect of the filed of Data Management. However, despite significant investments and technical advancements, these efforts of unifying Master Data often fail to provide tangible value to end-users.


![](https://miro.medium.com/v2/resize:fit:1000/1*NNhbijZcNXYaGwr8BZ4atQ.png)
These aspects prove to be some of the most debated in a Data Mesh approach, since they are build a round a centralized management and a unified view. In general, all of the more traditional Data Management practices — Data Quality, Master Data Management, and Data Security — remain more than crucial, yet there’s historically been a lack of groundbreaking innovation on these core areas. Now, Data Mesh gives us some incentive to rethink our approach.


## Data Mesh and Knowledge Graphs: Evolutionary Steps Forward


As Mozhgan Tavakolifard puts it when we talked for MetaDAMA “2#10 — Knowledge Graph enabled Data Mesh”:



> “If we think of Data Mesh as an evolution of data lakes, knowledge graphs are an evolution of Master Data Management.”
> 
> 


Her statement highlights the natural progression from traditional methods to more advanced, interconnected systems. The shift towards knowledge graphs represents a significant leap, addressing many of the inherent issues in current MDM practices.


The episode was published January 2023, and the development since has been large on Knowledge Graphs, while we have also seen the rise of Vector Databases. Lets have a look at both as possible ways of solving the existing challenges with MDM.


# Challenges with Existing MDM Approaches


I do not intent to provide a conclusive list, but rather a set of points that stand out as challenges with existing approaches.


* **Investment-Heavy Solutions:** Current solutions often require substantial financial and resource investments, focusing on technology as the primary solution to MDM challenges.
* **Complexity and Implementation Time:** These solutions are typically complex and have long implementation phases, delaying any tangible value for end-users.
* **Downstream Quality Issues:** Problems with master data quality are frequently deferred downstream, exacerbating inefficiencies.
* **Canonical Modeling Complexity:** The canonical approach to data modeling adds layers of complexity, making systems harder to manage.
* **Siloed MDM Solutions:** MDM is often not integrated (though maybe intented) across operational and analytical data, focusing either on push or pull methods rather than a cohesive strategy.
* **Application-Centric Approaches:** These approaches hinder the development of fully integrated MDM solutions.
* **The “Golden Record” Myth:** Pursuing a “golden record” or single source of truth is both time-consuming and costly, often without delivering the expected value.


# My Key Learnings and a New Path Forward


Before we dive into Knowledge Graphs vs. Vector databases, there are many other aspects that contribute to a new path foward in MDM. Again, not an exhaustive list but rather some of my key learnings:


* **Technology as a Visualization Tool:** A technical solution alone cannot resolve MDM challenges. Instead, it should be used to visualize and manage the complexity of different perspectives within an organization.
* **Embracing Diverse Perspectives:** Different domains have unique “perspectives on the truth.” These perspectives should be acknowledged and embraced as parts of a larger whole, rather than forced into a homogenized view.
* **Vital Role of Master Data IDs:** Master data IDs are crucial for globally identifying master data and understanding its various perspectives.
* **Local vs. Global Definitions:** Global definitions should be an aggregate of local rules. Local domains should define their data autonomously and escalate issues only when conflicts arise.
* **Empowered Data Ownership:** True data ownership comes with the power to define data at the domain level. This requires granting autonomy to individual domains to manage their data effectively.


# Semantic Linking


To link the different perspectives on the truth is essential to gain an holistic oversight, minimize ambiguity and connect fractured data sources. This emphasizes the need for ontologies and semantic framework and structure.


## **Semantic Linking Through Vector Databases?**


Vector Databases build on similarities between data by capturing semantic relationships between entities through embeddings and representing them as point in a multi-dimensional space. The obvious advantage of Vector Databases lies in the capability to scale for large volumes.


Yet, similarities even with very nuanced representations are not equal to a deep understanding of relationships between entities and their context. Vector Databases seam generally less focused on understanding complex relationships between entities, which can lead to false connection, or incomplete representation of the different domain perspectives.


## **Semantic Linking Through Knowledge Graphs?**


Knowledge graphs based on Graph Databases can facilitate this by linking data in meaningful ways, capturing dependencies and relationships in a natural representation.


The strengths is in the representation of interconnected entities in a way that ensures better control, really focusing on the connection and hierarchies that can represent a unified view of Master Data, connecting the different perspectives of the truth.


The downside of Knowledge graphs lie in the complexity and work-intensive maintenance and complexity that requries expert knowledge and timely optimization.


# Conclusion


Data Mesh represents a paradigm shift in Data Management, including the way we think MDM. By focusing on semantic linking, embracing diverse perspectives, empower data owners, and rethinking technological solutions organizations can create more integrated and effective MDM solutions. Therefore a new approach should not only addresses the complexities of current systems, but also empowers domains with the autonomy to manage their data, ultimately leading to better Data Management practises and more tangiable and valuable outcomes for end-users.