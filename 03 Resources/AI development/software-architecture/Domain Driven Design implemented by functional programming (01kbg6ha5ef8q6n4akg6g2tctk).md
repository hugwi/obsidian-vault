---
title: "Domain Driven Design implemented by functional programming"
source: "https://www.thoughtworks.com/en-us/insights/blog/microservices/ddd-implemented-fp"
author: "Yang Zhang"
published: 2022-08-19
created: 2025-12-02
description: "Usually, Object Oriented programming languages are the go-to choice to implement"
tags:
  - to-process
  - software-architecture
---

![](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/banner-image/insights/in_banner_blogs.jpg) 
DDD (Domain Driven Design) is a well-established approach to designing software that ensures that domain experts and developers work together effectively to create high-quality software.


This article introduces how to apply FP (Functional Programming) to implement DDD both elegantly and concisely.


In the C4 model, software architecture diagrams consist of four levels: “System Context”, “Container”, “Component” and “Code.”


“Component” is the basic unit of how a Container is made up, it is also the level described in this article.


#### Code organization structure


As applications grow in complexity, one way to manage that complexity is to break up the application according to its responsibilities or concerns. [Layered architecture](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice) is an approach that follows this principle and can help keep a growing codebase organized so that developers can easily find where a certain functionality is implemented.


In [Layered architecture](https://docs.microsoft.com/en-us/dotnet/architecture/microservices/microservice-ddd-cqrs-patterns/ddd-oriented-microservice), the code is split horizontally into different layers, with each layer encapsulated through OO (Object Oriented) design. The request is entered from the top, the code is executed from top to bottom, and the output comes from the top layer.


![Example of layered architecture](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/inline-image/insights/blog/microservices/blg_inline_ddd_implemented_fp_01.png)![Pause](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/pause-icon.svg)![Play](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/play-icon.svg)Example of layered architecture
One of the problems of this design is that multiple layers not only separate concerns but also separate the context of the same business function to different places, which means that when modifying the same business function, it may be necessary to modify multiple layers at the same time.


Another problem with this design is that the presentation and application layers are usually designed as [facade patterns](https://en.wikipedia.org/wiki/Facade_pattern), which can easily become [God objects](https://en.wikipedia.org/wiki/God_object), which is considered an [anti-pattern](https://www.yegor256.com/2016/02/03/design-patterns-and-anti-patterns.html).


The nature of FP is composition. FP is more geared towards organizing code vertically rather than splitting code horizontally. Several functions required for the one business function (typically an API) are vertically combined as a function pipeline through [Monad](https://en.wikipedia.org/wiki/Monad_(functional_programming)).


![Vertical code structure according to functional programming](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/inline-image/insights/blog/microservices/blg_inline_ddd_implemented_fp_02.png)![Pause](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/pause-icon.svg)![Play](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/play-icon.svg)Vertical code structure according to functional programming
In the real world, the boundaries between problem domains are blurred. Bounded context is the artificial projection of a real-world problem in a computer system.


The world outside the boundaries cannot be trusted, as it includes various inputs from the user. And the world inside the boundaries is a trusted, legitimate, shared domain model.


![Diagram of the domain model](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/inline-image/insights/blog/microservices/blg_inline_ddd_implemented_fp_03.png)![Pause](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/pause-icon.svg)![Play](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/play-icon.svg)Diagram of the domain model
This requires us to introduce validation and transformation at the boundary of the bounded context, thereby preventing external input and verifying the output to the outside.


Common validation and transformation such as:


* Transfer input data as domain model
* Verify the validity of the input data, e.g. ensuring the user name and email aren’t empty
* Output checker, to prevent sensitive information such as user passwords from being included in the output data


[Applicative](https://en.wikibooks.org/wiki/Haskell/Applicative_functors) is often used in FP to validate and transform input to the domain model. Once the input data breaks through the trust boundary, you don't have to worry about whether the user name is empty or the email format is correct. You should focus on [using ADTs for domain modeling](https://www.thoughtworks.com/insights/blog/microservices/domain-modeling-algebraic-data-types-pt1) and handle business rules through pure functions.


#### Modeling domain by state machine


Business models can be modeled as transitions between different states. You can always model your domain as a state machine by [union types (sum type)](https://en.wikipedia.org/wiki/Tagged_union). Another benefit is that in FP, [pattern matching](https://en.wikipedia.org/wiki/Pattern_matching) forces you to deal with each branch of the union types to avoid missing cases.


![Transition between states](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/inline-image/insights/blog/microservices/blg_inline_ddd_implemented_fp_04.png)![Pause](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/pause-icon.svg)![Play](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/play-icon.svg)Transition between states
Take user registration as an example: registration can be broken down into three steps:


* Input user name and password
* Verify email
* Pay membership fee


These three steps can be documented as three explicit states by union type. The behaviors like registration, adding email, verifying email, etc. can easily be designed as functions by pattern matching against this domain model.


Applications that follow the Dependency Inversion Principle tend to achieve [Onion Architecture](https://jeffreypalermo.com/blog/the-onion-architecture-part-1/) or Clean Architecture. The idea is to put the business logic and domain model at the center of the application, instead of having business logic depend on data access or other infrastructure concerns. This dependency is inverted: infrastructure and implementation details depend on the application core.


Similarly, in FP, we tend to combine functions as pipelines in each API request. As with Onion Architecture, we are going to put the side effects out to the domain as much as possible to keep the domain pure. The pure functions follow the persistent ignorance principle, they are focusing on implementing business rules.


![Onion Architecture](https://www.thoughtworks.com/content/dam/thoughtworks/images/photography/inline-image/insights/blog/microservices/blg_inline_ddd_implemented_fp_05.png)![Pause](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/pause-icon.svg)![Play](https://www.thoughtworks.com/etc.clientlibs/thoughtworks/clientlibs/clientlib-site/resources/images/play-icon.svg)Onion Architecture
Disclaimer: The statements and opinions expressed in this article are those of the author(s) and do not necessarily reflect the positions of Thoughtworks.