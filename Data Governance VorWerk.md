---
categories:
  - "[[Resources]]"
domain: compliance
created: 2026-06-23
---

# Thougts 
+ **What conscious decision do we need to make with guardrails to prevent data from being ungovern?** **Could we outline some risks?** 
- What additional metadata do we need? Do we set restriction on descriptions to columns and tables? 
- Should data products be defined in a central repository outside Databricks? 
- There are some part of Data governance that needs to be implemented in order to provide data governance. That usually ties into he central Data governance topics?   
- Federated data access
	- Data access 
	- Data discovery
	 - Data roles: Owners,  Custodian, business owners 
- Data privacy 
- For data governance you need a collaboration hub where you can collaborate together: 
	- Comment on dataset 
	- Request access 
	- Isights in data quality
	- Even insights in data projects
- Is it easier to start with a platform that easily set up new initiatives. 
---
Yevgen thoughts 

Create a governance framework that outlines the structure, roles, and responsibilities

Policies and standards - to develop data policies and standards that define how data should be collected, stored, processed, and shared.

Other teams working in a self-served manner?

Governance Model (Federated approach?)

Data Lifecycle management

Roles and responsibilities

Measurement of the impact of the data

Define Data Stewardship: Data Quality, Compliance?

Secondary: 
- SLA: Each team need to address this. Might not be first priority. 

# Future use cases 


Upselling and Cross selling


 It’s also easier to do Data Governance at early stage. You can start thinking about different processes/data access patterns to make sure reliability and security. It does require some extra work but it is a lot easier than retrofit governance framework to big/clunky existing processes.
### Step 1. Identify the problem(s) to solve

First and foremost, take the time to clearly define what problem(s) you're seeking to solve that may be addressed by data governance practices. For example:

<mark style="background: #FFB86CA6;">**What are Vorwerk biggest problem?** </mark>

**- Data privacy compliance.**
**- Centralized data access management.?**
- <label class="ob-comment" title="" style=""> Data discovery and data literacy provisions <input type="checkbox"> <span style="">  Can we enhance discovery from the beginning. What make catalog better discoverable? Tags and Glossary? Does this need to be synchronised across organizations though? </span></label>.
- <label class="ob-comment" title="" style=""> Collaborative analytics <input type="checkbox"> <span style=""> Yes, but question is when this should be done. For instance creating automatic workspaces, catalogs etc </span></label> or building new <label class="ob-comment" title="" style=""> data products <input type="checkbox"> <span style=""> We probably need to define what a data product is </span></label>. 
- Create a centralized repository of all standardized business terms.


### Step 2. Set clear goals

This means we're targeting two goals: 1) assign **data ownership** and 2) build **data quality test coverage** for all assets. As a result, we expect to see a decrease in time spent resolving broken data pipelines.

# Data access

- Can we request data access within the data catalog.  

Can't request for data access in unity catalog, need to build own portal for that.
https://www.youtube.com/watch?v=EfOfUc0RiJE
![[Pasted image 20231219104626.png]]

# Food for thought

https://www.ibm.com/blog/a-step-by-step-guide-to-setting-up-a-data-governance-program/
Data governance is a crucial aspect of managing an organization’s data assets. The primary goal of any data governance program is to deliver against prioritized business objectives and unlock the value of your data across your organization.

Realize that a data governance program cannot exist on its own – it must solve business problems and deliver outcomes. Start by identifying business objectives, desired outcomes, key stakeholders, and the data needed to deliver these objectives. Technology and data architecture play a crucial role in enabling data governance and achieving these objectives.

![[Pasted image 20231214150922.png]]

- **_People_** refers to the organizational structure, roles, and responsibilities of those involved in data governance, including those who own, collect, store, manage, and use data.
- **_Policies_** provide the guidelines for using, protecting, and managing data, ensuring consistency and compliance.
- **_Process_** refers to the procedures for communication, collaboration and managing data, including data collection, storage, protection, and usage.
- **_Technology_** refers to the tools and systems used to support data governance, such as data management platforms and security solutions.

![[Pasted image 20231214151212.png]]

#### **Step 2: Secure executive support and essential stakeholders**

The following is an example of typical stakeholder levels that may participate in a data governance program:
![[Pasted image 20231214152017.png]]

#### **Step 3: Assess, build & refine your data governance program**
![[Pasted image 20231214152050.png]]

The structure of data governance can vary depending on the organization. In a large enterprise, data governance may have a dedicated team overseeing it (as in the table above), while in a small business, data governance may be part of existing roles and responsibilities

![[Pasted image 20231214152127.png]]

![[Pasted image 20231214152239.png]]

### The primary objectives of data governance are to:

1. Improve the agility of data-driven business decisions
2. Seamlessly share knowledge across the organization
3. Eliminate uncertainty and instill trust in data
4. Drive value through collaboration in current workflows
**5. Make security and privacy compliance effortless**

To understand these data governance objectives, we first must acknowledge the role data governance plays in an organization’s overarching data management strategy.

### Using data governance to enable painless security and compliance

The stakes associated with protecting high-value data have never been higher. [IBM’s Cost of a Data Breach Report 2021](https://www.ibm.com/security/data-breach) found that the average cost of a security breach has grown to $4.24 million, the highest amount in the 17-year history of this report.

## Mapping data governance objectives to business objectives

The key to successful data governance is to make sure your governance objectives are closely aligned with business objectives. [McKinsey notes](https://www.mckinsey.com/business-functions/mckinsey-digital/our-insights/designing-data-governance-that-delivers-value), “The problem is that most governance programs today are ineffective. The issue frequently starts at the top, with a C-suite that doesn’t recognize the value-creation potential in data governance.”

How can you create a transformational data governance program rather than one strictly managed by IT, resulting in a set of distant policies that are loosely followed and even resented?

https://www.youtube.com/watch?v=e7uVURCDfLk
![[Pasted image 20231214152707.png]]

![[Pasted image 20231214155411.png]]

![[Pasted image 20231214155623.png]]

https://www.youtube.com/watch?v=0xDXm7EcXVU
![[Pasted image 20231215105415.png]]
![[Pasted image 20231215105516.png]]

![[Pasted image 20231215105924.png]]

![[Pasted image 20231215110628.png]]
![[Pasted image 20231215112152.png]]

![[Pasted image 20231215112332.png]]

#### Data quality Databricks 
https://www.databricks.com/discover/pages/data-quality-management
##### Summary – When to Use Constraints, Expectations, Quarantining or Violation Flagging
![[Pasted image 20240111100706.png]]

# Potential topics
- Data retention? 
- Data roles? 
	- Data stewards 
	 - Data liaisons
	