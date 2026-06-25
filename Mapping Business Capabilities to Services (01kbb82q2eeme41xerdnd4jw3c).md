---
categories:
  - "[[Resources]]"
domain: engineering
title: "Mapping Business Capabilities to Services"
source: "https://alok-mishra.com/2021/07/15/mapping-business-capabilities-to-services/"
author: "alokmishra"
published: 2021-07-14
created: 2025-11-30
description: "One of the key questions around API strategy we get asked is how do we map"
tags:
  - to-process
  - software-architecture
---

3 Votes


One of the key questions around API strategy we get asked is *how do we map business capabilities to services*. An approach is to use domain driven design and build domain services, in this post we will look at what this looks like


**Capabilities**


Businesses domains offer capabilities. Given domains are classified into core, supporting or generic it helps to think of the domain services as core, supporting or generic


[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-11.07.52-am-1.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-11.07.52-am-1.png)Business Domains an example
[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.15.32-am.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.15.32-am.png)Source: <https://github.com/ddd-crew/ddd-starter-modelling-process>
Domain capabilities expressed as software features can then be written down as *desired capability in domain service*


[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-11.07.57-am-1.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-11.07.57-am-1.png)Business Capabilities in Domains
For example, the following ask comes from our customer domain where customer management, case management, document management happen in the context of a customer


[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-8.53.09-am.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-8.53.09-am.png)A sample of desired capability in a domain service software
And to realise this we need a domain service, lets call this Customer API. It is interesting to note here how that the language of ***we need an API strategy*** translates to ***we need a set of domain services*** 


[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.25.39-am.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.25.39-am.png)Domain Service to implement the capability
**Applying domain driven design**


It helps at this point to recognise that a domain service can be described using domain driven design (DDD) as an Open Host Service (OHS) with perhaps a Published Language (OHS+PL) and relies on Domain Aggregates (Customer Contact, Customer Case etc) which emerge from bounded contexts (Customer Contact Management, Case Management etc)


Applying this to other concepts we can see how context mapping and event-storming notation fit here


[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.28.24-am.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.28.24-am.png)Bounded Contexts, Aggregates, Commands, Queries and Events
The bounded contexts that form the business context boundaries within a domain contain the language to define the model (aggregate). The model is expressed in our software (domain service) allowing mutation (state changes) via commands, query and publishing business events when there is a state change (domain aggregate events)


**Putting it all together into a domain service**


So what is a domain service? It is a namespace with a specific context under which business context services are provided. For example, in a customer domain service all the operations provided by the domain service are in the context of a customer


So putting all these concepts together we get a domain service with a base uri (top-level context root) and services under that context. Note that I am not implying the contextual services are deployed together, they just belong to a common namespace


[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.36.50-am.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.36.50-am.png)
**Ownership and Communication: Team Topology** 


Given our software architecture will follow the organisation of the teams (Conway’s law) it is also key to organising them along the bounded contexts. An example is provided below and shows how capability is shared across teams in a domain


[![](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.40.10-am.png)](https://alok-mishra.com/wp-content/uploads/2021/07/screen-shot-2021-07-15-at-9.40.10-am.png)Contextual Software Teams
**Summary**


Mapping business capabilities to domain services requires enumerating the capabilities, identifying what will be expressed in software and then applying domain driven design to work out the business contexts, aggregates and services


This process also neatly aligns to an API strategy – the process where where we analyse current state, build a future state (using the techniques above) and plan a roadmap. More on API strategy and also API Market Place in future posts