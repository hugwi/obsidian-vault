---
title: "Relationships Between Bounded Contexts in DDD"
source: "https://medium.com/@iamprovidence/relationships-between-bounded-contexts-in-ddd-ce5cfe3aaa04"
author: "iamprovidence"
published: 2025-10-27
created: 2025-11-30
description: "In Domain-Driven Design, defining Bounded Contexts is only half the story."
tags:
  - to-process
  - software-architecture
---

![]()
In Domain-Driven Design, defining *Bounded Contexts* is only half the story. Real-world systems rarely exist in isolation. Contexts *depend on, communicate with, and influence* one another. Understanding these relationships is what turns a collection of models into a coherent architecture.


In this article, we’ll explore how Bounded Contexts interact, what kinds of relationships can form between them, and how all those patterns fit into the bigger picture.


Are you ready? Let’s begin.


## Big Ball Of Mud


You’ve probably heard of this pattern — or more accurately, this *anti-pattern*. It’s a perfect example of how *not*to design your system 😅.


![]()
There are no clear responsibilities, no clear boundaries, and everything is coupled together.


Working in such a system is complex; this is a pure nightmare 🫣. So, how exactly does DDD help us there?


## Context Map


Everything starts with a Context Map. It illustrates how different Bounded Contexts relate and interact within a larger system.


![]()
It is recommended that dependencies between contexts should be pointed out in the form of an *acyclic graph* or a *tree,* but not be circular.


Let’s see what relationship between contexts can exist:


## Separate Ways


The simplest communication possible is when you don’t have it 😅.


![]()
Each contexts operate on its own. Each builds its separate model. The team does not interact, nor do they disturb each other.


## Mutually Dependent


Often, teams work closely together and collaborate daily; changes are coordinated continuously.


![]()
In this case, we have two common patterns:


### — Shared Kenel (SK)


Two contexts can share a small subset of the code, model, data structures, and database schema that are maintained collaboratively.


![]()
It is usually small and includes [marker interfaces](https://medium.com/@iamprovidence/the-actual-reason-behind-interfaces-9c5aac26eb54#f95f), value objects, or even domain events, as long as they are truly shared concepts.



```
interface IEntity { }  
  
readonly struct Money : IEquatable<Money>  
{  
    public required decimal Amount { get; init; }  
    public required string Currency { get; init; }  
}
```

It should follow the ubiquitous language, and changes require coordination between all teams. Do not try to put everything there. You sacrifice the independence that Bounded Contexts are meant to ensure — so use this pattern only when absolutely necessary.


### — Partnership


There could be no shared code.


However, teams still need to coordinate with each other, establish a planning process, etc.


![]()
It’s effective when teams genuinely need to move in sync, but it can quickly turn into a bottleneck that hinders independent progress.


## Upstream / Downstream


More than often, actions in one context will influence another.


![]()
In that case, the asymmetric relationship is referred to as upstream/downstream.


Let’s see what patterns we have here:


### — Published Language (PL)


Similarly to ubiquitous language, which applies and defines terminology *within* *a single* bounded context, a published language serves as the contract *between multiple* bounded contexts.


![]()
The upstream publishes an agreed, stable format for consumers. It could be an event (`CustomerChanged`) shared via message bus, [JWT](https://medium.com/@iamprovidence/jwt-authentication-12409520bc28) validation schema, or a standardized API response for retrieving product details.


However, it’s not tied to a specific technology (REST, message bus, etc.). It just ensures all parties understand the same meaning.


### — Open / Host Service (OHS)


The upstream provides a *well-defined interface* that other contexts can use to integrate with it.


![]()
It could be a RESTful [API](https://medium.com/@iamprovidence/services-communication-http-long-polling-server-sent-events-websocket-graphql-soap-grpc-b2e9b331fa54#f12f), [RPC endpoint](https://medium.com/@iamprovidence/services-communication-http-long-polling-server-sent-events-websocket-graphql-soap-grpc-b2e9b331fa54#d8d0), message queue, or any contract.


All the downstream context has to adapt to it.


### — Conformist (CF)


The Conformist pattern occurs when a downstream context uses upstream’s API as-is.


![]()
This may look like the simplest option; however, it can introduce unnecessary tight coupling, and your downstream model may become cluttered with concepts that don’t truly belong.


### — Anti-Corruption Layer (ACL)


Sometimes, one context evolves faster than another. As a result, it turns into legacy systems that suffer from quality issues.


Not to adhere the obsolete APIs, you can introduce an intermediate component — Anti-Corruption Layer — through which communication is performed.


![]()
An Anti-Corruption Layer acts as a translator between two bounded contexts or external systems, allowing your domain model to remain pure and consistent, even when interacting with legacy models. Plus, when the upstream API evolves, you only need to adjust the translation layer.



```
// Upstream model (from external service)  
public class ShipmentDto  
{  
    public string package_id { get; set; }  
    public int delivered_at { get; set; }  
    public string status { get; set; }  
}  
  
// Downstream model  
public class ShipmentDto  
{  
    public string ShipmentId { get; }  
    public DateTimeOffset DeliveryDate { get; }  
    public ShipmentStatus Status { get; }  
  
    public ShipmentDto(Legacy.ShipmentDto shipmentDto)  
    {  
        ShipmentId = shipmentDto.package_id;  
        DeliveryDate = DateTimeOffset.FromUnixTimeSeconds(shipmentDto.delivered_at);  
        Status = Enum.Parse<ShipmentStatus>(shipmentDto.status);  
    }  
}
```

This is basically the adapter pattern on a larger scale.


### — Customer / Supplier (CUS / SUP)


Even in upstream/downstream relationship team can work together.


![]()
The downstream context can influence the upstream team’s roadmap and ask for a specific API to implement.


This results in a collaborative but controlled relationship, where the upstream retains authority while still accommodating downstream needs.


## Spotting Conflicts Early


A context map provides a clear overview of how bounded contexts interact, helping teams spot hidden friction points early.


* **example 1:**


A and B provide OHS functionality for each other.


Circular dependencies between bounded contexts are usually a red flag.


![]()
Consider:  

 — merging contexts together  

— introducing a shared kernel between contexts  

 — split the shared functionality into a separate bounded context that will provide OHS for A and B  

 — define the API which context A request from the B, and apply [dependency inversion](https://medium.com/@iamprovidence/from-3-layered-to-ddd-architecture-in-one-step-f3de204bec2e) to change the dependency flow


* **example 2:**


Let's say you have three bounded contexts (A, B, and C):  

 — A provides Open Host Service  

 — A is also a supplier for the customer context B  

 — C uses A’s API as a conformist


This results in indirect dependencies; B can affect C’s integration through A.


![]()
Instead of C *conforming* directly to A, introduce an *anti-corruption layer*. This reduces tight coupling.


* **example 3:**


Below you have 4 contexts — A, B, C, and D:  

 — A and B are mutually dependent with a shared kernel  

 — A provides published language for C that uses it as a conformist  

 — B also provides published language for D that uses it as a conformist


Due to the Shared Kernel, there is a risk of a lot of model propagations and a very tight coupling between all 4 bounded contexts.


![]()
There are multiple solutions to this problem:  

 — try to refactor and remove the shared kernel between A and B if possible  

 — avoid published language  

— consider using anti-corruption layers for C and D


## Summary


In Domain-Driven Design, understanding how Bounded Contexts interact is as important as defining them individually.


A Context Map provides a high-level view of these relationships, helping teams reason about dependencies and integration.


The different patterns illustrate how bounded contexts interact, guiding teams in managing communication and collaboration effectively.


![]()
Let me know in the comment section, have you discovered something new💬 Clap if so 👋 Support me with a coffee using a link below☕ And follow to receive more ✅