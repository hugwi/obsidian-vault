
# TODO 
- [x] Check networking SQL Server ✅ 2023-11-30
- [x] Check networking for Delta sharing ✅ 2023-11-30
- [x] Secret management ✅ 2023-11-30
- Data security and encyption
-  Data Governance

# Onsdag 
- Compile security best practices 
- Read about how tokenization can be done
- [x] Read up on networking for on prem ✅ 2023-11-30
# Torsdag  
- [ ] Write down question for privacy
# Fredag
- [ ] See how a role for reading CDC can be setup.
- [ ] Setup multi cloud features
	
---


# Data privacy


- Setup a meeting with Valentina regarding data privacy. 
- How can pseudonymization be executed when ingesting data? 
- Read up about how tokenization would be done in real time. 

# Data ingestion

## Multi cloud 
- Add security features for multi cloud.
- Setup ingestion between cloud and check how it works

## SQL Server 

### Need to know about data: 
- Ingestion frequency 
- Volume
- Velocity
- Do all tables need to be ingested? 

### Which ingestion pattern?
- Does CDC makes more sense even if the data are ingested in batches? 
- Is it fine to have data model in a 3NF format? Most likely it is.

### How is networking done
Ask Peitro how this is done and if there's already a process for connecting to the database from an external service.

---

Hey Yevgen! 
How was the weekend? 

From what we discussed last Friday here are some suggestions for what we could look deeper into this week. 

`Data privacy`
- Setup a meeting with Valentina regarding data privacy. 
- Look into how pseudonymization can be executed when ingesting data? 

`Data ingestion`

SQL Server
- Networking - Setup a meeting with Petro to see how on prem is setup and if there is any process for connecting to the database from an external service. 
- Data sources information - It would also be useful to learn more about the data sources which we want to integrate to Azure. For example:
	- How many tables and which tables should be ingested? 
	- Ingestion frequency
	- Volume 
	- Velocity - How much new data is arriving every day/week/month.

Databricks AWS
- Provide a document for security best practices and security requirements when ingesting data via databricks delta sharing.
- Setup ingestion between cloud and check how it works.




