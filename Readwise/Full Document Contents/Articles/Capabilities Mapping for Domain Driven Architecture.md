# Capabilities Mapping for Domain Driven Architecture

![rw-book-cover](https://freedium-mirror.cfd/apple-touch-icon.png)

## Metadata
- Author: [[freedium-mirror.cfd]]
- Full Title: Capabilities Mapping for Domain Driven Architecture
- Category: #articles
- Summary: Domain Driven Design helps map business capabilities to bounded contexts so systems can evolve from monoliths to cloud-native architectures. Start by modeling the business and organization, create a capabilities map, and use it to define isolated bounded contexts. Keep dependencies between contexts loose to avoid hard technical coupling that breaks services.
- URL: https://freedium-mirror.cfd/https://louwersj.medium.com/capabilities-mapping-for-domain-driven-architecture-a64eec2050a

## Full Document
#### Using Domain Driven Architecture as part of your Enterprise Architecture strategy is in general a good idea. Especially companies who…

Using Domain Driven Design as part of your Enterprise Architecture strategy is in general a good idea. Especially companies who transfer from a primarily monolith based landscape to a cloud native and hybrid cloud native based architecture can benefit from using a Domain Driven Design.

**Bounded Context** One of the prime "building blocks" of using a Domain Driven Design is ensuring you use the model of Bounded Context in the right way. You can use a bounded context to "isolate" a business functionality or business capability and ensure that everything within the bounded context can work in isolation and is not having a hard dependency on services within another Bounded Context.

**Define the Bounded Contexts** Business analysis, enterprise architects and all people involved in defining an Enterprise Architecture will at one point in time question if they have defined the bounded contexts in the correct way. The same applies for the question on how to get started with defining the bounded contexts in an enterprise.

One of the most effective ways is to start by understanding the business model, understanding then organisation structure that is mapped upon the business model and defining a enterprise wide capabilities map. Even though capabilities mapping is not originally born in the Enterprise Architecture world it is now fully accepted as a very useful way of defining the enterprise.

The below image shows a capabilities mapping with 4 levels of capabilities, the example shows the hierarchy drill-down into "logistics management" and downwards.

![None](https://miro.medium.com/v2/resize:fit:700/1*DKFMvVlwB8AUQMmMh9zkCA.png)
Taking first the approach of understanding the business model and understanding then organisation structure while defining business capabilities while doing this and not focussing on any technical implementation currently in place will provide the best starting point for defining the Bounded Contexts for your Enterprise Architecture.

When the enterprise has been mapped and visualized in capabilities hierarchy the exercise of consolidating duplicate capabilities found in the wider enterprise could be the first exercise in mapping capabilities to required systems and required subsystem.

Having a clear picture of all required capabilities and a clear view of duplicated capabilities will help you to build a mapping to required services and set the bounded contexts for those services. When setting the bounded context for a service one has to keep in mind the allowed and disallowed dependencies between the different services / bounded contexts as they will be explained on a high level in the following section of this post.

**Bounded Context Dependencies** Business services residing in different bounded contexts will have dependencies from an Enterprise Business point of view. The shipping department will have a dependency on the customer relationship management department to ensure the correct delivery address is provided when they will ship something to the customer. Those relations, soft dependencies, are fully acceptable and can cross the bounded context.

The not so perfectly acceptable dependencies between services in different bounded contexts are the type where the service will fail to work from a technical point of view when the service in another bounded context is experiencing an issue.

This means, loosely coupled dependencies between services in different bounded contexts are perfectly allowed from the transfer of data and events. However, one should be aware of and refrain from building hard technical dependencies. A hard technical dependency could be for example that the application used in shipping requires direct access to the database of the finance department to check if a shipping hold applies.

In case that the shipping application will fail from a technical point of view, "crash", you have violated the concept of bounded context soft dependencies and you have introduced a hard dependency.

**About the Author** [Johan Louwers](https://www.linkedin.com/in/johanlouwers/) currently has the role of Chief Enterprise Architect within [Oracle](http://www.oracle.com)¹ and has a long standing background as Chief Architect within one the leading global technology consultancy firms for a diverse number of industries and enterprises as well as governmental institutions. He combines his love for complex technology and business optimization by supporting clients around the globe with advise on technology, open-source, complex system development as well as on business optimization and C-level strategy advisory. Views are his own and not per definition those of his current employer.

¹ At the time of writing this article.
