---
categories:
  - "[[Projects]]"
project: "[[PII]]"
created: 2026-06-23
---

## Datahub x Membership team - 27 November 

They're rebuilding a lot of logic. Massive queries, a lot of business logic. Rate plan limits. 

Issue: 
- Only calculate on demand. 
- Only provide data for active customers. 
- Do need completeness of data 
- Miss out on subscription that changed recently 
- Dynamo db not prepared in paginated way. With lose data if try ot query in paginated way. 

Still make sense to own it. Improve queries on their own. 
Would be more expensive on the operational side.

can we push left and create datasets and reports instead of writing the logic in another source system

Have more reason to focus on this topic since we have prioritized use cases

### What data is needed? 

### Feedback
Could prepare more to give examples? 

### Next steps
- Might have different subscription model time. 

# Membership team provides with the data 


## Options of sourcing data

Fact event - We get the entire history every time
https://developer.confluent.io/courses/event-design/fact-vs-delta-events/

Pros:
- Makes it much easier to build history
- 
Cons: 
- Everytime a subscription updates they need to pull the entire history. 


Need a unified schema for subscriptions. Shouldn't need to care about implementation details.

ca 50K updaterateplan per day



This query fails on two days which must mean that there is more than 10M rows per day? 
```

SELECT UpdatedDate, COUNT(*) cnt FROM rateplancharge
WHERE Date(UpdatedDate) BETWEEN Date('2024-04-05') AND Date('2024-04-06')
GROUP BY UpdatedDate
ORDER BY UpdatedDate
```


raw_apple_subscription_events_log_v1
payload
struct<subscriptionName:string,subscriptionType:string,productId:string,appleMarket:string,originalTransactionId:string,applicationVersion:string,purchaseDateTime:string,expireDate:string,cancellationDateTime:string,cancellationReason:string>


membership_raw_events_log_v1
struct<subscriptionId:string,subscriptionStartDate:string,subscriptionCreateDate:string,cancelPolicy:string,subscriptionExpireDate:string,subscriptionEndDate:string,subscriptionName:string,subscriptionType:string,subscriptionStatus:string,subscriptionLevel:string,voucherId:string,campaign:string,voucherType:string,id:string,created:string,yearAndMonth:string,subscriptionExpiryDate:string,feedbackInteractionType:string,user:string,market:string,autoRenewalProduct:string,lowUsage:boolean,notForMe:boolean,notSatisfied:boolean,didNotUnderstand:boolean,technicalProblems:boolean,couldNotFindRecipes:boolean,usingAnotherPlatform:boolean,didNotKnowMembership:boolean,missingFunctionalities:boolean,didNotKnowTrialExpired:boolean,customReason:string,productId:string,appleMarket:string,originalTransactionId:string,applicationVersion:string,purchaseDateTime:string,expireDate:string,deviceId:string>

```
SELECT COUNT(*) FROM "prod_subscriptions"."subscriptions_zuora_history_v1" limit 10;
```
97,945,887 records in the entire history 
How is possible that there is such a big difference between this and rateplan/rateplancharges in Zuora? 


### Meeting 18 Sept
**Avoiding schema changes since it's messy to recreate the tables**


Autoreneweal the original transctionalId is the same as the initial buyers. 
Transaction id changes but original transaction id.

How do you defer the new subscription to the orginal. 

She handle a renewal as a new subscription. 


Cancellation

Refund - refund for a non auto renewal

Only 

Might not be able to give transaction id. The original buy 
Refund refer to the initial buy. 
subscription id is the original transaction id. 
Refund might even have a transaction id on its own. 

Might be able to get the full history to infer the "subscription id"

Refund is only important if we it change the expiration date? 