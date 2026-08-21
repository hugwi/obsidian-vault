---
categories:
  - "[[Clippings]]"
domain: [software-engineering]
tags:
  - architecture
  - ddd
source: readwise
created: 2026-06-23
rating: 
action: 
---

# Transforming Legacy with Domain-Driven Design, II: Strategy

![rw-book-cover](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-i243d6k.jpeg)

## Metadata
- Author: [[Anton Musatov]]
- Full Title: Transforming Legacy with Domain-Driven Design, II: Strategy
- Category: #articles
- Summary: Domain-Driven Design (DDD) is a collection of principles that helps create clear and maintainable software architectures in complex domains. It emphasizes building a domain model with input from experts, using a consistent language, and isolating different domain components to reduce complexity. The methodology also suggests dividing large domains into smaller, manageable parts called bounded contexts for better organization and understanding.
- URL: https://hackernoon.com/transforming-legacy-with-domain-driven-design-ii-strategy

## Full Document
#### Too Long; Didn't Read

Domain-Driven Design is not a specific software architecture or a strict set of rules but rather a collection of principles and ideas that help build a clear, scalable, and maintainable architecture in complex domains.

![](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-i243d6k.jpeg?w=1200&q=75&auto=format)featured image - Transforming Legacy with Domain-Driven Design, II: Strategy
1x

Read by **Dr. One** 

Listen to this story

In [the previous article](https://hackernoon.com/preview/ewoGBcx2wigV0udb9f4S?ref=hackernoon.com), I discussed the main preconditions that led me to implementing Domain-Driven Design (DDD) in a large legacy project. To provide context for the information in the upcoming articles, I will briefly outline here the core concepts of this methodology, explain why they are used, and describe the problems they solve.

The term Domain-Driven Design (DDD) was first introduced by Eric Evans in his blue book, "Domain-Driven Design: Tackling Complexity in the Heart of Software", published in 2003. The approach and its ideas were supported by Martin Fowler, who wrote the foreword for Evans' book. Additionally, Martin Fowler's website features several articles on DDD. Although Eric Evans uses examples and code snippets in his book, he focuses more on theoretical justifications and discussions. Later, Vaughn Vernon's "Implementing Domain-Driven Design", published in 2013 with a foreword by Evans, also became popular.

![](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-g923do3.png?w=800&q=75&auto=format)
In my opinion, these two books are essential reads if you plan to implement DDD in your project. Despite containing valuable theoretical and practical information, you are likely to encounter challenges not fully covered in these books when implementing DDD in a specific project. This happened to me: after studying these books and numerous articles, I faced several situations during the implementation of DDD in our legacy project that I hadn't read about anywhere. That's why I decided to write a series of articles about my experience implementing this methodology in a large legacy project, sharing non-obvious challenges and solutions.

Domain-Driven Design is not a specific software architecture or a strict set of rules but rather a collection of principles and ideas that help build a clear, scalable, and maintainable architecture in complex domains. The key aspect here is complex domains. Automating business processes is a technically challenging task, especially with additional requirements like performance, scalability, or availability. However, very often, the domain itself turns out to be extremely complex. This can involve a set of rules and regulations created by analysts or business experts or complex real-world processes. In all cases, if the domain is highly complex, the developer cannot avoid this complexity because it is part of the system's fundamental requirements. However, with the right approaches, we can reduce the complexity of individual parts of the application, organize it in a way that reduces cognitive load for developers, and separate business logic complexity from technical aspects. This is where DDD helps: the methodology reduces the overall complexity of the application and helps organize and structure the code to make it easier to maintain and extend.

DDD offers both fundamental strategic ideas and tactical practices that allow you to achieve the overall strategic goals. Let's consider some strategic principles.

#### Building a Domain Model

In most cases, the domain that needs to be automated does not directly relate to computer technology, and the application's developers are not experts in that domain. Therefore, DDD suggests starting with creating a model of the domain. You need to work closely with domain experts to create a carefully selected and deliberately simplified knowledge set of the domain. You don't need to create the most realistic or detailed model, as delving into a complex domain can take too much time. You need to create a model sufficient for simulating the domain while reflecting the nuances of how it works.

At this stage, developers often lean towards data models or framework models, often starting with database tables. This is not the right approach. At this point, we need to understand how the domain works, how experts think about and discuss it, what terms they use, and how they visualize the domain's objects. Developers need to immerse themselves in the rules and invariants of the domain, abstracting from future methods of storing information and possible ways of implementing the model.

A metaphor for this principle could be a family tree. You may know individual people in your family tree, know what they do, what their names are, and where they live, but to understand family relationships more accurately, it is better to build a visual tree and explicitly denote the connections. Such a model will focus specifically on family connections and may not be as useful in other everyday matters, but it accurately reflects the relationships between people.

![](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-i733d7s.png?w=800&q=75&auto=format)
#### Ubiquitous Language

Another obstacle adding unnecessary complexity to a project can be the use of different terms and expressions by developers and domain experts. If this happens, developers must "translate" words from one language to another in each conversation with experts and during the implementation of new tasks. This slows down the process and can lead to inaccurate modeling of domain objects, as some information gets lost in translation. It's important to stay in close contact with the business and use consistent terms both in communication and the domain model. Don't forget about documentation and tests—they should also use a common language and terms.

This principle is quite obvious, as are the benefits of adhering to it. However, in practice, building a ubiquitous language may not happen quickly or easily. Some terms may not be fully defined at the business level, and sometimes the business simplifies terms when assigning tasks. Experts often use domain words so frequently that they don't realize their specificity. Using technical terms instead of domain terms may seem easier for developers at first, as it eliminates the need for additional communication with the business. This requires discipline and a shared understanding of the principle's importance across the team. Only through constant discussions will it be possible to truly build a shared language for communication.

![](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-h973d2f.png?w=800&q=75&auto=format)
#### Model-Driven Design

Once the analytical domain model is created, it can be translated into code and the application's architecture. The Model-Driven Design principle suggests building the architectural model as close as possible to the analytical one, minimizing the gap between them so that both models reflect the same goals and approaches. For long-term support projects, it's important not only to initially transfer the abstract model into code correctly but also to synchronize all future changes with both the analytical model and the application's architecture. In Model-Driven Design, development follows the model, guiding changes and ensuring that each new decision aligns with the logic and structure of the system laid out in the domain model. This also reduces overall system complexity, as there is no need for complicated conversions between the analytical model and the application model in the code.

A metaphor for this principle could be an architect's blueprint and the subsequently built building. The architect's project outlines the analytical model of the future building: how it should look, what elements it should contain, and why. The building should then be constructed as closely as possible to the original design. Any new changes to the project should be reflected in the real structure, and implementation constraints, in turn, should influence the architectural project.

![](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-2d63d9t.png?w=800&q=75&auto=format)
#### Domain Model Isolation

Software development involves many technically complex tasks and approaches. Even without business logic from a specific domain, we deal with highly abstract programming languages, various databases, complex data formats, and different frameworks. To separate this technical complexity from the domain complexity, DDD suggests isolating the domain layer from all other layers. This allows for more focused attention on each layer. Separate layers simplify maintenance and architecture formation, as each layer can use the most appropriate approaches. This also reduces cognitive load on developers, as encapsulated logic enables them to focus on one layer or their integration at any given time.

![](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-a583do8.png?w=408&q=75&auto=format)
#### Bounded Contexts

Another method of reducing the complexity of domain components is to divide a large domain into several parts, into subdomains or bounded contexts. The idea is that certain components and models may repeat in different contexts but may have different names, properties, and business logic in different subdomains. In some contexts, certain entities may only be available for reading. With such division, changes to the model in one context may not even lead to changes in other contexts. Depending on the business importance of the contexts, a specific hierarchy and interaction methods may also be established between them. All of this further structures the application's code and makes it easier to work with each component individually.

![](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-i293d13.png?w=800&q=75&auto=format)
These are the main strategic approaches used in the Domain-Driven Design methodology. These ideas lay the foundational principles for working with complex domains.

In [the next article](https://hackernoon.com/preview/GIXDHQTOJ0Lk9rW9wZDl?ref=hackernoon.com), I will discuss the tactical and more practical principles in more detail.
