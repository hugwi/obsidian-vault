---
categories:
  - "[[Areas]]"
domain: clients
created: 2026-06-23
---

1. **How would a hybrid setup look like**
- 
2. How would the solution fit into our current ecosystem (Databricks) and can be used by external consumers (Other services for example
3. How would the solution be maintained and operated?
4. Can we deploy in our own cloud?
	- Do we need to change consent? 
1. **Time to implement**
2. Cost
3. Service Agreement
4. Build vs buy
5. How does subject request work like RTBF and Data Portability?
6. Can we create a smaller "token space" to improve data storage and memory consumption?
7. Format preserving tokens (retain format and data type)

Asking: 
- Which BI tools -> Mainly Clicksense, notebooks 

We want to fuel marketing tools.  

# Immuta works

We do things compare vs encryption vs tokenization
Integrate with Azure AD to provision job tiltle, department, training courses etc

Take tags in databricks and bring them across Immuta and will have understanding of your data. 
Classifiers and push to Immuta to tag the data. Discovered by Immuta or classified by Immuta. 

Mask is built in immuta, but it will create the code that databricks need. Create udf and masking policies. 

Three things to 
1. Binary for tokenizaiton
### Tokenization
All of nothing?
### Masking
Mask the entire credential   
2. Need to get the original value
Was tokenized 

3. Performance
Find the key, 

## RTBF 
- Mark the data as RTBF
- Delete the data 

**How will it affect aggregates?** 
Need to deal with it yourself

**Don't handle PII data for other system**

How many users? 
- 100 mix of scientist, analytics

Christian - Focus on databricks 
Florian - Commercial IT since february. Based in Cologne
Marius - 

Pricing - Per user not data. 

https://www.immuta.com/product/secure/
![[Pasted image 20240626180706.png]]
