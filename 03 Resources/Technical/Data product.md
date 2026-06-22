## Questions
Is there any benefit of grouping assets to a data product rather than giving access to for example on data product that is related to one asset 1:1 mapping?

## Data contract 

https://medium.com/@mikldd/activating-ownership-with-data-contracts-in-dbt-4f2de41c4657

## Data Classification 
https://www.datamesh-governance.com/policies/privacy/data-classification/data-classification.html
![[Pasted image 20240423172924.png]]
--- 
## Medium
The cost of creating a single data contract is non-trivial, and managing a large volume of contracts can quickly become challenging; you must ensure that you’re creating contracts on the most valuable data assets.

## **Start small**

Start with valuable, revenue-generating use cases. Introduce constraints gradually. Start with one or two meaningful and easy-to-debug constraints and introduce more nuanced use cases over time.

## **Leverage what you have**

Don’t look at data contracts as a net-new phenomenon. Maybe you’re already using dbt Tests or encoding quality checks within your Airflow DAGs — treat that as your starting point and build from there.

Whenever possible, **meet people where they are and introduce as little change to their existing workflows as possible.** The more deviation from their current workflow, the harder it will be to scale.


---

# Meeting 24 April

**Data tagging** 
Alienz 
A lot of PII data. Data catalog Informatica. Fill the data. 
Building ontologies. Domain independent objects. Got more granular dependent on the use case. Properties to generate masking policies. 
Templates for pipelines. 
Data steward - these properties are PII. 
Data steward 
Who's defining the tags for the down stream use cases?
Knowledge of PII data was divided by IT and Business. 

### Data products
**Wences**
unstructured data
Platform ingestion  HIPPA GDPR compliant 
Data contracts
Zeiss - 
Set of assets. Need to have master table. 
Don't have quality checks. 
Data product is multiple assets. 
Master table to share. 
Product needs to point to assets.
Automatic scanning. 
PII scanning 

---

**Mascha** 
Struggled with ownership and enforcement
Need buy in from top level. 
Motivates team to take care of data and a "dangling carrot"
Need centralized control.
Many times fall if you don't have buy in.
It's hard to establish governance. 
How much control from central governance team. 
Self service 
People that produces the data don't want to take ownership 

**Maturity**
Teams that create the products have knowledge. 

Starting with one domain and then the next 

Start with templating. 
Need to extend 
A lot of data experts. We can take that and offer that as a service for other teams.  
Ingestion as a service. 


**Wences**  

**Julius** 
Touchpoints data mesh 
Architecture pespective 
Planning a talk about Data mesh in organisational aspects

**Sven** 
Rebuilding data lake 
Thinking about modelling data in a better way 
Want to move away from centralisea way 

**Mascha** 
Led transition to data mesh 
Full data mesh - data within product teams
porduct teams with less knowlecge 
Need to use with proper governance 
Self service 
Monitor data quality 
proper data documentation 
Data contracts
Just having the definition adds a lot of value. One of the learning is that it needs to sit somewhere where it can be used. In the end it was the catalog. 
Best team is to look at the owners and the 

**Laurens** 
Problem with domain knowledge
Shifting self service project

