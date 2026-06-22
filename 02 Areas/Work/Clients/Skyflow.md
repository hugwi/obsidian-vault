# Questions 

1. How would a hybrid setup look like
2. How would the solution fit into our current ecosystem (Databricks) and can be used by external consumers (Other services for example
3. How would the solution be maintained and operated?
4. Can we deploy in our own cloud?
	- Do we need to change consent? 
1. Time to implement
2. Cost
3. Service Agreement
4. Build vs buy
5. How does subject request work like RTBF and Data Portability?
6. Can we create a smaller "token space" to improve data storage and memory consumption?
7. Format preserving tokens (retain format and data type)

Solution depends
Who builts UDF? 
Can do conversion
How is groups synced? 

Throughput is the most important. Couple of ms won't matter. Pick two regions close 
German for gcp and aws frankfurt. 10 ms
Can set expiration.

Help with setting up sdk. Doing POC together like they did for snowflake. 
Open mutual slack channel. 

Row level security - They're adding it, but it's not there yet. 
Can filter it with a mask

# Anonymizer function

Built in and custom in javascript
Want to get the least amount of information 

Rotating encryption

- Creation of vault 
	- Add fields to vault
- Data access policies mapped to users? Synced with current IAM solutions
- Other anonymization techniques? 

- How does the UDF work? 
- How policies and IAM work? Can we sync entra id 
- Risk for building it ourself. 
- Isolate data: different use cases. For example finance.  


- Competitors privacera or PIIano


Not integrated IAM but you need to maintain mapping. 

### Authenticate to Datbricks
Service account with their access
account keys in the secret manager 
you allow them their secret 
jwot token authentication. 

# How do we anonymize the data
To anonymize data to batch the data. Locked down data that it lands in. You need to delete that for the data from skyflow and our dw. 
Introduce elt job before ingestion. 

# Third party 
Can integrate with third parties
![[Pasted image 20240614113614.png]]

Probably want to use the proxy
**Look through the user agreement. Don't allow you to hold health informatino**

Do they need the plain data? 


![[Pasted image 20240614112203.png]]

![[Pasted image 20240614112252.png]]
![[Pasted image 20240614112329.png]]

Leading US health 
migrated 700 million tokens -> took 15 days

## Owning the data 
Can deploy in our VPC. 
## SLA 
Include 99.9 SLA 
Premium support for additional 20%. Higher SLA 99.99. Can send the document.

## Timeframe 
Integrating api gateway and databricks. 
Build in sdk takes longer


## Build vs Buy
![[Pasted image 20240614113034.png]]
8 months to build
# Demo

## 

Table structure
can have multiple tables
can store binary files
Customisable schema

### Tokens 
Preserve formatting: We provide regex. 

Don't delete by tokens. 
For deletion we use unique ids. 

	# Polymorphic encryption 
	Makes more performant, normally encryption take
	age ranges, give me customers between ... Then we can do aggregation comparisons. 

Don't have not enough use cases for other methods. 

pgadmin

Snowflake has had breaches

How does it integrate to Databricks? 

golden layer - lock down table
push further to the left. Web or app frontend
Integrate via API gateway. 


Cost? 

Scaling? 

Effort to implement? What do us as consumers need to do? 


Match and merge linkability

![[Pasted image 20240507134742.png]]
Challenge of PII need to be used more often? 


![[Pasted image 20240507134834.png]]

Tokens - mathematical relationship. 

format preserving and/or consistent

Workspace 
encryption keys 
isolated vaults to specific regoin

shyflow id cardholder_name, email address ssn, state
not key, value store. We made it look like a database. It's different data stores. 

You can add your own id

api first company.
We have a query api. 
We don't encrypt the data. 


Serial number as another column. Have it in two different places. Same token. two different people. 
Talk to fenish developer. 
How hard it to find this person? 

split data in indexes. polymorph encryption 
homomorph encryption - encrypt data that allow you to perform analytics on it without encrypting it. Takes a lot of time! 

polymorph morhpism break down data and run indexes. 

## How to use? 
Using a UDF. Can run a demo!

## Pricing 
The number of vaults + number of records. 
25 000 dollar a year. 
per record 
The API calls? 
Discount based on active and inactive. 


## Latency  
Less that a 100 ms. 
500 tokenization a second. 
We have 4-500 000 a second.
50 million rows. Latency 
Batch operations. 25 records at a time. 

## Maturity 

- [Raises 30 million 2024](https://techcrunch.com/2024/03/28/skyflow-raises-30m-ai-spikes-privacy-business/?guccounter=1&guce_referrer=aHR0cHM6Ly93d3cuc2t5Zmxvdy5jb20v&guce_referrer_sig=AQAAACSChzFtr0N0Z3vkV-xPjGEuXJksYCmC8OCSDevVUd_wZH_9lsGucDMd_DouUW7MYTt29aShkguBOPmh7yjFhLnC4ImLFKa9ZS_TWyTHUdBe-pIuKKtbL-G223pGoCsntAO4aqqCf7daqtbULgr4QMsbv8dwln_A7y5PcQQkLVPM)
- [Support for LLM](https://venturebeat.com/ai/skyflow-launches-privacy-vault-for-building-llms/) 
- Skyflow reached 100 customers in 2023, Lenovo, IBM, and GoodRx
- Partners like Amazon Web Services and Visa

# UDF 
https://medium.com/snowflake/privacy-safe-analytics-with-snowflake-and-skyflow-7aa54d73c50f


![[Pasted image 20240614111716.png]]