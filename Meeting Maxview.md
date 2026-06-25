---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---

- PML was used for everything 
	- Records for 
		- clients
		- customers 
		- arrends 
		- documentation
- Business is not using it. 1500 employees that are administrator and advisors. 
- 1:1 migration they wanted to do. 
- Isolated the database for PML. Maxview only speaks with a PML facade. 
+ Broken down into domains 
	- Customer information in one place
	- Client information in one place 
	- Policy infromatino place
+ Store procedure in PML that has business logic. Store procedure populated other database. More dependency before. 
+ Insurance is how you're insured and the information like fullmakt. Everything that happens after an advisory meeting. Sign a new insurance. 
+ Policy domain. What's a companies or client policy. You have contract with the customer and insurance companies. Premiums calculation tool, total premium service. Gather data OCG, tjänstegrupper. CEO 40% pension ordinary workers have 30%. 
+ Status for a customer should be manual
+ **Anton, Maria, Andreas for lifecycle management**
+ **Access management - we should reinvent the access model. Have it like the banks have -> Rather have an audit trail.** 
+ Sick salary was modeled on the individual
+ You will have an employment history.
+ The salary is flat and was not connected to the relation. 
+ Policy doesn't move a lot. 
+ **Problem with the old data although it has been remodeled**
+ Private customer at L&P
	+ Can sell private insurances, move into a new insurance. We look after your pension. Pay 3k we can have a meeting with you. 
+ Administrator get a task and it should remove the insruances and stop the employment. 
- Booked meeting is not connected to outlook 
- Popluated through faktainsamling
- We add it to the customer domain rather than going to PML. 
- Insclear and Heartbeat can replace some thigns but no all. Heartbeat is driven by a third party and only need to invoice and sign new insurances. 
- Sync between multiple systems