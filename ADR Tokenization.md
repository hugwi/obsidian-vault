---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
https://icepanel.medium.com/architecture-decision-records-adrs-5c66888d8723
![[Pasted image 20240122101146.png]]

# Assumptions
# Context
In order to stay GDPR compliant Vorwerk need to pseudanonymize data. For the chosen technique of tokenize data, a decision needs to be taken about the technical implemntation. 

# Status 
**Draft**

# Requirements

## Scalability

### Data volume
- What is the number of records it needs to support?
### Latency
- How fast does the implementation needs to be? 

## Accessibility
How should it be consumed? Should it be exposed as a Rest API or like a table? 

If we expose it as a table in Databricks it might be enough from the start to grant it to users without the data taxonomy. If we need more granular access pattern, can we create them afterwards? Or do we need to create types? 

## Types of data 
- What kind of data should it support? Strucutred? Unstructured? 

## Decision

```markdown
We will transition to a microservices architecture to modularize the application and enable independent development and deployment of services.
```
## Consequences:

```markdown
- **Pros:** Improved scalability, easier maintenance, independent deployments.
- **Cons:** Increased network communication overhead, potential challenges in data consistency.
```


## Considered Options

1. Create a table in Databricks which can be joined to in order to retrieve the token data. 
2. Create a token service in order to make it faster. Can this be done later? 
3. Expose a Rest API to retrieve token. Then database can easily be changed. How is this retrieved though? https://freedium.cfd/https://medium.com/@think-data/be-cautious-of-batch-api-calls-in-pyspark-6e30295b8118 

```markdown
1. Stick with the monolithic architecture and improve modularization.
2. Adopt a serverless architecture for specific functionalities.
```

## Pros and Cons of Alternatives:

```markdown
- Alternative 1: Pros - Familiarity, simpler deployment. Cons - Limited scalability.
- Alternative 2: Pros - Reduced operational overhead. Cons - Cold start latency, vendor lock-in.
```


# Implementation
```markdown
**Example**
1. Define service boundaries.
2. Implement API gateways for communication.
3. Establish monitoring and logging for microservices.
```

## Database

Should it use something like a Databricks lookup table or 

## Option 1 - Databricks table. 

**Pros:** 
- Easy to setup. 
- Work natively in Databrics

**Cons:**
- Might be harder to scale
- Might be hard to make it easy for end users? How do we make it easy to anonymize/deanonymize? 

## References:

--- 
## Technical implementation 

### Read 
- Read data and decrypt selected rows. 



Write data. Encrypt data depending on schema. 



--- 
### Comparing solution between Implementation with join or cache
https://stackoverflow.com/questions/57241455/batch-processing-job-spark-with-lookup-table-thats-too-big-to-fit-into-memory

You have a few of options for dealing with this requirement:

**1- Use RDD or Dataset joins**

You can load both of your HBase tables as Spark RDD or Datasets and then do a `join` on your lookup key. Spark will split both RDD into partitions and shuffle content around so that rows with the same keys end up on the same executors. By managing the number of number of partitions within spark you should be able to join 2 tables on any arbitrary sizes.

**2- Broadcast a resolver instance**

Instead of broadcasting a map, you can broadcast a resolver instance that does a HBase lookup and temporary LRU cache. Each executor will get a copy of this instance and can manage its own cache and you can invoke them within for `foreachPartition()` code.

Beware, the resolver instance needs to implement Serializable so you will have to declare the cache, HBase connections and HBase Configuration properties as **transient** to be initialized on each executor.

I run such a setup in Scala on one of the projects I maintain: it works and can be more efficient than the straight Spark join if you know your access patterns and manage you cache efficiently


# Questions
- How many users do you have? 10 million customers. 4 million + paying customer. How many are active? Follow up on active users?  1 million are on trial. Paying customers. They have consent during trial period. You have sub for free. 
- What are the use cases? Which kind of data is needed? One workspace that deals with golden recrods. Only authorized users. How do we seperate the spaces. Potentially we don't have to tokenize the data. 
- Will any data need to be retrieved by for example a Rest API? 
- Partial deletes? 
 - Are we fine with easier access pattern in the beginning? 
 
	- When deleting a user we still need to keep the token mapping so we don't create any new token. Or maybe that will never be a problem? If it has be forgotten we will never anonymize it again and just need to return the token when doing a lookup.  
- If someone ask to be forgotten, can we get new information about that person or will that be treated as a completely new user? 
- How will data be inserted? Can there be multiple rows related to a user? 


Sree is starting next week? 
Scale data lake. Spin up the virtual machines. 
Provisioning of accounts. Spin up databricks and services for synapse. We need synapse for serverless which can mimic sql database. Create interface to emarsys. Just like sql database from mysql. 
Cognizant is consulting company. 
They made an offer. 
Don't know how to enable external with the access. 

Derek - responsible for applications, sales and marketing. Main point of contact for Yevgen. Was previous solution architect. 