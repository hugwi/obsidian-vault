**Related:** [[Ingestion tools]] · [[Azure data factory]] · [[change data capture]] · [[_MOC/MOC-Engineering|Engineering MOC]]

BE AWARE THAT YOU NEED TO HAVE ADMINISTATOR ACCESS
# Snapshot

### Pros
- Simple to ingest
### Cons
- Wasteful (since it pulling in data that has already been processed) 
- Expensive
- Higher load on system 
- Data latency 
- Only get the latest data, if more need to be computed that needs to be accounted for
- If there are more changes during the interval frequency it will get lost (only get the last change) 


# Incremental load from watermark

### Pros
- Less load than snapshot
### Cons
- Same as full ingestion although the load is less
- More complicated than snapshot
	- Need to manually define the watermark
- Don’t handle hard deletes well - Deleted data doesn't show up as it no longer exists at the source

# CDC

Change Data Capture is **a software process that identifies and tracks changes to data in a database**. CDC provides real-time or near-real-time movement of data by moving and processing data continuously as new database events occur.

### Pros 
- It enables faster and more accurate decisions based on the most current data; for example, by feeding database transactions to streaming analytics applications.
- It minimizes disruptions to production workloads.
- It reduces the cost of transferring data over the wide area network (WAN) by sending only incremental changes.
- Can detect Deletes in source database
- More effiecient than other database replication methods since only data changes after the previous replication are synced.  

### Cons
- Might need to maintain infrastructure
- No control on how the events look like
- Small latency with CDC from the time a database update occurs until when the CDC event is published into the event stream
- Schema evolution might not be possible.  

Unsure?
+ Cost?
- Recovery from failure? Loss of data? 


## Challenges
https://medium-parser.vercel.app/?url=https://medium.com/@venkatkarthick15/change-data-capture-cdc-3a076c9bdaa3

In the CDC mechanisms of row versioning and update timestamps, the history of changes to a record is not automatically recorded in the main data table. Instead, these methods typically only reflect the most recent version of the record, whether by incrementing a version number or updating a timestamp to mark the time of the latest change.

If tracking the history of changes is a requirement, additional measures must be taken. Here are some common strategies to record the history:

1. **Audit Trail:** Implement an audit trail that logs changes to records, including what was changed, when it was changed, and possibly who made the change. This can be done through database triggers or application logic that writes to a separate audit log or history table.
2. **Historical Table:** Create a separate historical table that stores previous versions of records. Whenever a record is updated, the previous version can be copied to the historical table before the main table is updated. This historical table can include additional information such as timestamps to show when each version was active.


##### CDC with CDF  (Databricks)
https://freedium.cfd/https://medium.com/@venkatkarthick15/simplify-cdc-with-delta-lakes-change-data-feed-cdf-2ddfdedacf05

---
## CDC with outbox pattern

### Domain events vs Change events

Before we go deeper, it is essential to make a distinction about the types of events we are worried about regarding Event Sourcing as well as Change Data Capture:

- Domain name events– A specific event, part of your organization domain, that is created by your application. These events are normally represented in the past tense, such as Orders Placed, or Items Shipped. These occasions are the main concern for Event Sourcing
- Change events– Events that are produced from a database transaction log showing what state transition has actually taken place. These events are a problem for Change Data Capture.

Domain events and transform events are not related unless a change event occurs to include a domain name event, which is a facility for the Outbox Pattern to be introduced later in the write-up.

If you are working with critical data that need to consistent and need to accurate to catch all requests, then its good to use **Outbox pattern**. If in your case, the database update and sending of the message should be atomic in order to make sure **data consistency** than its good to use outbox pattern.

The Outbox is also meant to be abstracted from the application as it’s only an ephemeral store of outgoing event data, and not meant to be read or queried. In fact, the domain events residing in the Outbox may be deleted immediately after insertion!

![[Pasted image 20231123095542.png]]

## The downsides of the Outbox Pattern
https://www.squer.io/blog/stop-overusing-the-outbox-pattern

As shown above, this pattern works well and solves the initially described problem. Unfortunately, it comes with a significant downside. It turns the database into the system's bottleneck — something we wanted to avoid with EDAs in the first place. Combined with widespread use, this can become a significant problem for the resilience and elasticity of our overall system.
https://www.squer.io/blog/stop-overusing-the-outbox-pattern

Seems like outbox pattern is already done in CDC services.


---


# Event streaming/sourcing
Instead of having the database publish the events via CDC, the microservice would publish the events.
### Pros
- Can have different schema. Microservice can translate the event into a more readable business event.
- Easier schema evoluition
- No small latency with CDC from the time a database update occurs until when the CDC event is published into the event stream
- Good if you don't already have database setupK

### Cons 
- Not easy to change to for existing sources
- Can get out of sync to what is in the database? 


---
https://medium.com/capital-one-tech/the-journey-from-batch-to-real-time-with-change-data-capture-c598e56146be

# CDC VS Event sourcing 
I have found CDC is a better fit for existing applications, where transforming a monolith into microservices is either further down the road or the application is a custom off the shelf product that can’t be modified. It also enables a parallel adoption approach where consumers can migrate to the new pattern at their own pace. In these scenarios, there are several factors to consider to determine if CDC is a fit.

Another good article 
https://labs.ebury.rocks/2021/09/16/demystifying-event-sourcing-and-change-data-capture-i/
https://labs.ebury.rocks/2021/09/22/demystifying-event-sourcing-and-change-data-capture-ii/

## Do you need CDC 


- **Consumers desire incremental data updates**. If consumers only need current state and not the detailed updates, then CDC isn’t needed.
- **Consumers desire real-time data updates.** This one may be obvious, but if consumers only need the data once a day or less frequent, then CDC isn’t needed. It’s like paying for that monthly magazine subscription that you never read.
- **Data Producers can adapt to CDC.** If the source of your data is on a data producer that is out of your control, such as a 3rd party vendor, they have to be willing to adopt CDC. Streaming events from daily batch files will achieve data decomposability, however the events will be stale. The goal is to stream the events as soon as they occur to enable microservices to react to them in real-time.
- **Consumers are OK with replaying events to get the current state.** It’s very important that consumers understand that to get the current state they will have to replay events. If some consumers are OK with this and others are not, one approach is to have a separate service that generates and publishes the current state based off of the CDC events.

---

[1][https://quantumagile.fr/distributed-data-for-microservices-event-sourcing-vs-change-data-capture/] 
## Domain Events vs. Change Events 

Before we go deeper, it is essential to make a distinction about the types of events we are worried about regarding Event Sourcing as well as Change Data Capture:

- Domain name events– A specific event, part of your organization domain, that is created by your application. These events are normally represented in the past tense, such as Orders Placed, or Items Shipped. These occasions are the main concern for Event Sourcing
- Change events– Events that are produced from a database transaction log showing what state transition has actually taken place. These events are a problem for Change Data Capture.

Domain events and transform events are not related unless a change event occurs to include a domain name event, which is a facility for the Outbox Pattern to be introduced later in the write-up.

Since we have actually developed some commonality on Event Sourcing and Change Data Capture, we can go deeper.

**Event sourcing, CDC, CDC + Outbox**
![[Pasted image 20231122170449.png]]

---

### Comparing patterns 
https://towardsdatascience.com/all-data-integrations-should-use-change-data-capture-a1d207091773

![[Pasted image 20231127131836.png]]

![[Pasted image 20231127132231.png]]
---
https://towardsdatascience.com/all-data-integrations-should-use-change-data-capture-a1d207091773

https://quantumagile.fr/distributed-data-for-microservices-event-sourcing-vs-change-data-capture/

Intested article comparing event streaming event sourcing and cdc 
https://event-driven.io/en/event_streaming_is_not_event_sourcing/

https://stackoverflow.com/questions/72284628/comparing-cdc-vs-outbox-pattern-for-creating-event-streams