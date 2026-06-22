# TODO

How does it integrate to Databricks? 
Mostly about operational systems.  
System can be managed to Piiano or by themself. We give you terraform. Postgres KMS. 
ORM specific integration. 
Use openapi. 
Use cloud function to get the data

Seggragated by collections 

Main system 

Cost? 
Scaling? 
Effort to implement? What do us as consumers need to do? 
Configure access controls - what if a user only should get access to part of the data 

Uniquness across 

## Tokens 

Serial id 
Tokenization works on multiple fields 
Can also use scope - Can work on multiple fields

Using hmap for hashing. Dedicated key. 

Self hosted is a bit more expensive 

# Pricing 
Thousands a month
Larger company want to have self hosted 

As for pricing, please provide the following information:

### Amount of stored records (number of users + number of objects and fields per user)
5 - 10 million users
Dields: 
- Email
- Dcid 
- SNR


### Requests per second (RPS) and usage pattern (e.g., consistent 5 RPS vs. a daily spike of 1 hour of 500 RPS)  

    
### SaaS vs. Self-hosted
We would like to get a pricing for both. 

### Do you need cross-region replication? We run on a single region in two availability zones by default. 
I assume that we don't need that, but do we want to get their perspective on why we might want to have it?    
	
- Any special additional requirements?

#  Multicloud
Deploy to one of them 
Many customer deploying into different regions


Share secrets cloud between the deployments of the vault. 


Think about long term



# Advantage on skyflow
Ability to host themself

# Architecture 
https://www.piiano.com/blog/piiano-vault-architecture
