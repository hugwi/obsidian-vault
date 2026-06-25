---
categories:
  - "[[Clippings]]"
domain: [software-engineering]
tags:
  - architecture
  - patterns
source: readwise
created: 2026-06-23
rating: 
action: 
---

# Pattern: Saga

![rw-book-cover](http://microservices.io/i/data/saga.jpg)

## Metadata
- Author: [[microservices.io]]
- Full Title: Pattern: Saga
- Category: #articles
- Summary: Sagas are a way to manage transactions that span multiple microservices, allowing for data consistency without using distributed transactions. They can be coordinated through choreography, where services communicate via events, or orchestration, where a central orchestrator directs the process. While sagas help maintain order and consistency, they add complexity and require careful design of compensating transactions.
- URL: https://microservices.io/patterns/data/saga.html

## Full Document
#### Context

You have applied the [Database per Service](https://microservices.io/patterns/data/database-per-service.html) pattern. Each service has its own database. Some business transactions, however, span multiple service so you need a mechanism to implement transactions that span services. For example, let’s imagine that you are building an e-commerce store where customers have a credit limit. The application must ensure that a new order will not exceed the customer’s credit limit. Since Orders and Customers are in different databases owned by different services the application cannot simply use a local ACID transaction.

#### Problem

How to implement transactions that span services?

#### Forces

* 2PC is not an option

#### Solution

Implement each business transaction that spans multiple services is a saga. A saga is a sequence of local transactions. Each local transaction updates the database and publishes a message or event to trigger the next local transaction in the saga. If a local transaction fails because it violates a business rule then the saga executes a series of compensating transactions that undo the changes that were made by the preceding local transactions.

![](https://chrisrichardson.net/i/sagas/From_2PC_To_Saga.png)There are two ways of coordination sagas:
* Choreography - each local transaction publishes domain events that trigger local transactions in other services
* Orchestration - an orchestrator (object) tells the participants what local transactions to execute

#### Example: Choreography-based saga

![](https://chrisrichardson.net/i/sagas/Create_Order_Saga.png)An e-commerce application that uses this approach would create an order using a choreography-based saga that consists of the following steps:
1. The `Order Service` receives the `POST /orders` request and creates an `Order` in a `PENDING` state
2. It then emits an `Order Created` event
3. The `Customer Service`’s event handler attempts to reserve credit
4. It then emits an event indicating the outcome
5. The `OrderService`’s event handler either approves or rejects the `Order`

#### Example: Orchestration-based saga

![](https://chrisrichardson.net/i/sagas/Create_Order_Saga_Orchestration.png)An e-commerce application that uses this approach would create an order using an orchestration-based saga that consists of the following steps:
1. The `Order Service` receives the `POST /orders` request and creates the `Create Order` saga orchestrator
2. The saga orchestrator creates an `Order` in the `PENDING` state
3. It then sends a `Reserve Credit` command to the `Customer Service`
4. The `Customer Service` attempts to reserve credit
5. It then sends back a reply message indicating the outcome
6. The saga orchestrator either approves or rejects the `Order`

#### Resulting context

This pattern has the following benefits:

* It enables an application to maintain data consistency across multiple services without using distributed transactions

This solution has the following drawbacks:

* The programming model is more complex. For example, a developer must design compensating transactions that explicitly undo changes made earlier in a saga.

There are also the following issues to address:

* In order to be reliable, a service must atomically update its database *and* publish a message/event. It cannot use the traditional mechanism of a distributed transaction that spans the database and the message broker. Instead, it must use one of the patterns listed below.
* A client that initiates the saga, which an asynchronous flow, using a synchronous request (e.g. HTTP `POST /orders`) needs to be able to determine its outcome. There are several options, each with different trade-offs:

	+ The service sends back a response once the saga completes, e.g. once it receives an `OrderApproved` or `OrderRejected` event.
	+ The service sends back a response (e.g. containing the `orderID`) after initiating the saga and the client periodically polls (e.g. `GET /orders/{orderID}`) to determine the outcome
	+ The service sends back a response (e.g. containing the `orderID`) after initiating the saga, and then sends an event (e.g. websocket, web hook, etc) to the client once the saga completes.

* The [Database per Service pattern](https://microservices.io/patterns/data/database-per-service.html) creates the need for this pattern
* The following patterns are ways to *atomically* update state *and* publish messages/events:
* A choreography-based saga can publish events using [Aggregates](https://microservices.io/patterns/data/aggregate.html) and [Domain Events](https://microservices.io/patterns/data/domain-event.html)

#### Learn more

* My book [Microservices patterns](https://microservices.io/book) describes this pattern in a lot more detail. The book’s [example application](https://github.com/microservice-patterns/ftgo-application) implements orchestration-based sagas using the [Eventuate Tram Sagas framework](https://github.com/eventuate-tram/eventuate-tram-sagas)
* My [presentations](https://microservices.io/presentations) on sagas and asynchronous microservices.

#### Example code

The following examples implement the customers and orders example in different ways:

  
#### Context

You have applied either the [Client-side Service Discovery pattern](https://microservices.io/patterns/client-side-discovery.html) or the [Server-side Service Discovery pattern](https://microservices.io/patterns/server-side-discovery.html). Service instances must be registered with the [service registry](https://microservices.io/patterns/service-registry.html) on startup so that they can be discovered and unregistered on shutdown.

#### Problem

How are service instances registered with and unregistered from the service registry?

#### Forces

* Service instances must be registered with the service registry on startup and unregistered on shutdown
* Service instances that crash must be unregistered from the service registry
* Service instances that are running but incapable of handling requests must be unregistered from the service registry

#### Solution

A 3rd party registrar is responsible for registering and unregistering a service instance with the service registry. When the service instance starts up, the registrar registers the service instance with the service registry. When the service instance shuts downs, the registrar unregisters the service instance from the service registry.

#### Examples

Examples of the 3rd Party Registration pattern include:

* [Netflix Prana](https://github.com/Netflix/Prana) - a “side car” application that runs along side a non-JVM application and registers the application with Eureka.
* [AWS Autoscaling Groups](http://aws.amazon.com/autoscaling/) automatically (un)registers EC2 instances with Elastic Load Balancer
* [Joyent’s Container buddy](https://github.com/joyent/containerbuddy) runs in a Docker container as the parent process for the service and registers it with the registry
* [Registrator](https://github.com/gliderlabs/registrator) - registers and unregisters Docker containers with various service registries
* Clustering frameworks such as [Kubernetes](https://github.com/GoogleCloudPlatform/kubernetes/blob/master/docs/services.md) and [Marathon](https://mesosphere.github.io/marathon/docs/service-discovery-load-balancing.html) (un)register service instances with the built-in/implicit registry

#### Resulting context

The benefits of the 3rd Party Registration pattern include:

* The service code is less complex than when using the [Self Registration pattern](https://microservices.io/patterns/self-registration.html) since its not responsible for registering itself
* The registrar can perform health checks on a service instance and register/unregister the instance based the health check

There are also some drawbacks:

* The 3rd party registrar might only have superficial knowledge of the state of the service instance, e.g. RUNNING or NOT RUNNING and so might not know whether it can handle requests. However, as mentioned above some registrars such as Netflix Prana perform a health check in order to determine the availability of the service instance.
* Unless the registrar is part of the infrastructure it’s another component that must be installed, configured and maintained. Also, since it’s a critical system component it needs to be highly available.

* [Service Registry](https://microservices.io/patterns/service-registry.html)
* [Self Registration](https://microservices.io/patterns/self-registration.html) is an alternative solution
