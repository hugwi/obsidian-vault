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

# Understanding clean architectures

![rw-book-cover](https://media2.dev.to/dynamic/image/width=1000,height=500,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fl213tst98m36yfg4wmri.png)

## Metadata
- Author: [[Carlos Gándara]]
- Full Title: Understanding clean architectures
- Category: #articles
- Summary: Clean architecture divides an application into layers, each with its own clear responsibility. It keeps the core domain model separate from technical details to reduce accidental complexity. This approach works best for complex problems where isolating the domain helps maintain and evolve the software.
- URL: https://dev.to/xoubaman/understanding-clean-architectures-33j0

## Full Document
The *clean architecture* concept was introduced by Robert C. Martin [back in 2012](https://blog.cleancoder.com/uncle-bob/2012/08/13/the-clean-architecture.html). He later published a well known book about it with the slightly lazy but straightforward title [Clean Architecture](https://www.goodreads.com/book/show/18043011-clean-architecture).

In this post we will cover the foundations behind this architectural pattern.

It is worth mentioning that I have not read the book. Therefore, the following content is not based directly on it but in its underlying concepts.

####  TL:DR;

In a clean architecture the application is divided into layers, assigning concrete responsibilities to each of them.

Those layers wrap each other and communicate only inwards: an outer layer can use stuff from inner layers, but not the other way around. This is known as Dependency Rule.

The more outward a layer is, the lower-level its responsibilities are. The innermost layer takes care only of the higher level details: the domain model.

That's basically it when it comes to how this architectural pattern structures things. The *how.*

It is only by knowing the *why* behind it that we will understand what we get in return and when it is worth to use it.

####  Software purpose

We create software to solve problems. We should at least. If it's not the case, please spend a bit of reflection on what we want this world to be and what are we doing to achieve it. Anyway. Solve problems.

To solve a real world problem with software, we create a model that represents part of the real world that helps us to tackle its complexity.

Software does not only have to deal with just the problems it solves, though. It runs in computers, it's written in a language, uses networks, servers, protocols...

If we mix together all these technicalities with the problem model, we are putting a spoke in our wheels by making the model and the technical part more complex than they actually are. Which is something we usually want to avoid. Clean architectures help keep separated the stuff that do not belong together.

Before moving forward with the clean architecture itself, we will take an interlude to talk about complexity and cognitive load, concepts tightly related to the goals of clean architectures.

####  Complexity is all over the place

Complexity is, oversimplifying, how hard it is to grasp how all the moving parts of a system work together.

More *complexity* means more effort is required to understand, maintain, and extend a software system. This effort is known as cognitive load.

Therefore, keeping cognitive load low by removing complexity is a good thing to do. Easier said than done, because complexity cannot be removed in its entirety.

There are two types of complexity: essential and accidental.

The *essential complexity* is intrinsic to the problem we want to solve, and it's there no matter what. It cannot be eliminated. Not even reduced.

For instance, in an e-commerce we cannot realistically say "no, rejected payments are not a thing for us". Certainly life would be easier without them, but the reality is payments are sometimes rejected. This complexity is essential to the problem our application solves.

The *accidental complexity* is what we humans, in all our messiness, add to things, consciously or not, making things harder than they essentially are. We cannot escape it, it's part of the human nature. We can, though, stay vigilant and mitigate it as much as we reasonably can (or want).

A blatant example of accidental complexity would be adding load balancing and database sharding to an application intended to manage a small dental clinic. The application does not need that, and it makes harder to understand it.

A more subtle example would be, in our previous e-commerce application, to mix up technical details like HTTP requests and the database table relations needed to fetch data, with the domain logic needed to manage something already complex enough like payments. By not keeping those different concerns separated, we are making both parts harder to understand.

####  What for

Now that we have agreed on some definitions, we can state the purpose of a clean architecture:

>  To keep our model of the real world separated from technical details, so we avoid introducing accidental complexity in both sides.
> 
>  

In other words, to reduce accidental complexity by keeping the essential complexity of running software separated from the essential complexity of the problem solved by the software.

Clean architectures structure applications in a way that helps us to keep the accidental complexity (a part of it at least) under control.

####  The layers

Layers are groupings of responsibilities. There can be any number of them at code level but attending to its purpose they boil down to three.

>  👉 Indeed, the original post where the pattern was presented includes four layers. Which to my understanding is an implementation-level decision rather than a purpose-level grouping. Like with everything else, I'm just a guy with an opinion on the internet. Read, ponder, and build you own understanding without blindly follow anything.
> 
>  

[![A diagram showing three concentric layers: infrastructure is the outermost, application is the one in the middle and domain the one in the center](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv5holc0wihogfmm7z493.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv5holc0wihogfmm7z493.png)
In a clean architecture, we visualize layers as concentric circles (or half a circle to optimize space, he). The more we move inside, the higher level of detail the layer takes care of.

The outermost layer is the **Infrastructure Layer**, connecting the different technologies the application interacts with in the way the inner layers require. This is the lower level of detail our application has to deal with, technology specific stuff like HTTP headers, the format of request payloads, databases, etc.

Next is the **Application Layer** (also known as *Service Layer*), holding a representation of the use cases the application exposes and taking care of orchestrating the execution of the right logic for the use case requested. It manages a higher level of detail by knowing the logic a use case needs, without any technical details involved.

>  👉 The Application Layer does not need to always orchestrate Domain Layer logic, although it may seem so from the usual diagrams used to represent a clean architecture. For instance, use cases for plain read operations may not require any business logic.
> 
>  

The innermost one is the **Domain Layer**, where our model of the problem to solve lives. This is the highest level of detail. By keeping our domain model isolated from the concerns of the Infrastructure and Application layers, we can approach its complexity without distractions, making it easier to evolve and change.

>  👉 The framework we use to run our application is an infrastructural concern as well. We can think of it as if Application and Domain code is "portable" and should require no change if we switch to another framework.
> 
>  

####  The Dependency Rule

The Dependency Rule defines the visibility between layers. It states that a layer can only depend on inner layers, never in outer layers. In other words, a layer cannot have code references to anything that is declared in an outer layer.

[![Diagram showcasing how it is allowed to import code from inner layers, but it is forbidden to import code from outer layers](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4o8ykogsr8gy0vszzb0x.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4o8ykogsr8gy0vszzb0x.png)
What we achieve with the Dependency Rule is that no details of a layer leak into the others. By applying inversion of dependencies (the "I" in SOLID), inner layers define abstractions that outer layers implement. The abstraction is defined by the inner layer, and therefore sticks to its level of abstraction, and it's not polluted by lower level details.

The classic example are Domain repositories. At Domain level we define an interface which is implemented in the Infrastructure layer. But this interface sets a contract expressed in Domain language, with no technicalities involved. In the Infrastructure layer, the implementation will take care of mapping the data to the right tables, which are lower level details that should not concern the Domain.

####  Anatomy of a clean architecture

It's about time we come with somewhat practical examples after all this theory.

In the Domain Layer we have our domain model, an abstraction of the real world problem. The design may not be the best, but it's good enough to illustrate how the thing works:

```
interface PaymentRepository {
    fn findById(PaymentId id): Payment
}

class Payment {
    private Status status;
    private RejectionDate rejectedOn;

    fn reject(Date when) {
        status = Status.rejected();
        rejectedOn = RejectionDate.fromDate(when);
    }
}

```

Our domain model is written in pure domain language. There are no references to databases, HTTP requests, message queues or any other technology. Neither there are references the framework.

When we go to the code to see what rejecting a payment means, the code tells us directly, and we do not need extra cognitive load to separate the business logic from other unrelated details. Analogously, the `PaymentRepository` is a contract the Domain defines in its own terms. The implementations will live in the Infrastructure, dealing with the technical details of the technologies used.

At the Application Layer we have the use case that represents a payment must be rejected:

```
class RejectPaymentUseCase {
    fn RejectPaymenUseCase (
        private PaymentRepository repository,
        private Clock clock
    );

    fn execute(RejectPayment request) {
        payment = repository.findById(PaymentId.fromValue(request.paymentId));
        payment.reject(Clock.now());
    }
}

```

The Application Layer just orchestrates the logic needed to fulfill the "reject payment" use case. It does not know what it means at business level, only what must be executed to do it. Analogously to the Domain Layer, there is no interference from technical details.

It is in the Infrastructure Layer where we find technical references:

```
class RejectPaymentHttpController {
    fn RejectPaymentHttpController (
        private RejectPaymentUseCase useCase
    );

    fn execute(HttpRequest request): void {
        payload = JsonHelper.deserialize(request.payload);
        useCase.execute(
            new RejectPayment(payload.paymentId);
        );
    }
}

class SqlPaymentRepository < PaymentRepository {
    fn findById(PaymentId $id): Payment {
        //details of database tables, prepared statements and other DB stuff
    }
}

```

The entry points to the application are the ones that handle the low level details of the underlying technology. In this case the HTTP controller knows about HTTP requests, deserializing JSON payloads, etc. Same for the repository implementation: at Application Layer level, the use case knows nothing about the persistence details of a Payment, it just knows the contract the Domain Layer defines.

>  👉 Contracts can be defined by Application Layer as well, it's not an exclusive treatment for the Domain.
> 
>  

While adhering to the contracts specified by inner layers, they prevent this complexity to leak into layers with different purposes.

In this sneak peek into what a clean architecture looks like we have deliberately used a quite simple example. There is way much more to it. The purpose of this example is to just show how the layers are taking care of their own concerns, liberating other layers of extraneous details.

Real life™️ will require a much more complex implementation because there are many more things to model and take into consideration: message buses, event driven design, the outbox pattern, CQRS, configurations and environments... the list is huge. Some stuff is optional, some other contextual. But rest assured there is more and the above is not a blueprint to start with.

####  Humans after all

As with every pattern, it is up to us to be consistent with it. In case of clean architecture there is no standard implementation (unless you take the one from Robert C. Martin as such... just be aware there are other valid options).

The most common pitfall when going clean is to make the Application Layer too smart, leaking Domain logic in our use cases instead of just using the right parts of the domain model. And that's something the architecture cannot prevent.

It would be also tempting to make the Infrastructure Layer to run some domain logic to get a persisted entity into a certain state.

Or to introduce technical details into the domain model because it seems convenient.

While I would discourage to do any of this, it might make sense under certain circumstances. It is our decision to contravene the architecture foundations at a given moment.

At this point we should already have the understanding of what we are giving in exchange. And that probably the transgressions should not stay there for long.

####  When and when not

There is a trade-off. There always is.

As we have seen, there is a level of essential complexity in a clean architecture itself. Not only knowing about the layers, their responsibilities, and the Dependency Rule. There is also all the extra salt we can or must add for the architecture to actually do the work.

Turns out in our attempt to reduce complexity we are adding more complexity. What a world!

So when does it make sense to use clean architectures? The math is simple: when the problem we are solving is complex enough on its own that the additional complexity introduced by clean architecture is outweighed by what we gain in return.

Clean architectures will work best when we are dealing with the core domain of our business. This is usually complex enough to compensate the effort of having such an architecture. We want our core to be easy to iterate, and clean architectures are good at that by keeping the domain model isolated. Not so critical parts of the system may not be worth the effort. When the problem is not complex enough a more dirty approach can suffice for the same effectiveness with a lower effort.

In our e-commerce example we have seen payments are complex and a clean architecture pays back. But something accessory like the comments of products might be simple enough so that a hardcore-framework MVC approach will provide the same result in less time with no perceptible penalties.

Architectures are chosen to support our needs. If the needs change, maybe an architectural change is required as well. If our comments subsystem becomes a differential part of the business and grows in functionalities and complexity, our good old MVC system could become overwhelmed, and we will need to transition to a different architecture to support it. Maybe a clean one. Embrace the change!

>  👉 It could make sense that within the same application we may go clean for part of it and use another architecture for the less complex use cases. Symmetry has its advantages: if everything works the same way, it's easier to understand. But is it worth all the indirection for the most basic use cases? Well... it depends.
> 
>  

####  What is not

Clean architecture is not a synonym of Ports and Adapters (aka Hexagonal Architecture). Neither it is a synonym or a requirement for CQRS, Event Sourcing, Event Driven Architectures, or Domain Driven Design.

It is possible to go with any of those without a clean architecture. Although clean architectures are great friends of those other patterns.

####  Concluding

We should have now a clear understanding of the principles behind clean architectures (or, at least, my version of them).

We didn't dig much into implementation details, though. There is a lot to say about it. Reading about the message bus and the command + command handler patterns is a good follow-up to take the most out of a clean architecture, along with approaches that focus on domain modeling, like Domain Driven Design.

That's all. Feedback is always welcome so drop a comment if you want.

Be kind. And as happy as possible.

*The cover picture is the science library of Upper Lusatia in Görlitz, Germany. The photo was taken by Ralf Roletschek ([Roletschek.at](https://Roletschek.at)), who holds the copyright, and it's available at [Wiki Commons](https://commons.wikimedia.org/wiki/File:13-11-02-olb-by-RalfR-03.jpg)*
