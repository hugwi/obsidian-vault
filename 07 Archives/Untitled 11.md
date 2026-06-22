activities or agreements. It was actually a nice analysis of these relationships, and their
experiments with the model had the quality of an academic research project. But it wasn't getting
us anywhere near an insurance application.
My first instinct was to start slashing, finding a small CORE DOMAIN to fall back on, then refactoring
that and reintroducing other complexities as we went. But the management was alarmed by this
attitude. The document was invested with great authority. Its production had involved experts
from across the industry, and in any event they had paid the consortium far more than they were
paying me, so they were unlikely to weigh my recommendations for radical change too heavily.
But I knew we had to get a shared picture of our CORE DOMAIN and get everyone's efforts focused
on that.
Instead of refactoring, I went through the document and, with the help of a business analyst who
knew a great deal about the insurance industry in general and the requirements of the application
we were to build in particular, I identified the handful of sections that presented the essential,
differentiating concepts we needed to work with. I provided a navigation of the model that clearly
showed the CORE and its relationship to supporting features.

Content

74.29%

(page 92)

In a software system for tracking accounts due, that modest "customer" object may have a more
colorful side. It accumulates status by prompt payment or is turned over to a bill-collection agency
for failure to pay. It may lead a double life in another system altogether when the sales force
extracts customer data into its contact management software. In any case, it is unceremoniously
squashed flat to be stored in a database table. When new business stops flowing from that source,
the customer object will be retired to an archive, a shadow of its former self.
Each of these forms of the customer is a different implementation based on a different
programming language and technology. But when a phone call comes in with an order, it is
important to know: Is this the customer who has the delinquent account? Is this the customer that
Jack (a particular sales representative) has been working with for weeks? Is this a completely new
customer?
A conceptual identity has to be matched between multiple implementations of the objects, its
stored forms, and real-world actors such as the phone caller. Attributes may not match. A sales
representative may have entered an address update into the contact software, which is just being
propagated to accounts due. Two customer contacts may have the same name. In distributed
software, multiple users could be entering data from different sources, causing update transactions
to propagate through the system to be reconciled in different databases asynchronously.
Object modeling tends to lead us to focus on the attributes of an object, but the fundamental
concept of an ENTITY is an abstract continuity threading through a life cycle and even passing
through multiple forms.
Some objects are not defined primarily by their attributes. They represent a thread of
identity that runs through time and often across distinct representations. Sometimes
such an object must be matched with another object even though attributes differ. An

Content

74.25%

(page 93)

Consider transactions in a banking application. Two deposits of the same amount to the same
account on the same day are still distinct transactions, so they have identity and are ENTITIES. On
the other hand, the amount attributes of those two transactions are probably instances of some
money object. These values have no identity, since there is no usefulness in distinguishing them.
In fact, two objects can have the same identity without having the same attributes or even,
necessarily, being of the same class. When the bank customer is reconciling the transactions of the
bank statement with the transactions of the check registry, the task is, specifically, to match
transactions that have the same identity, even though they were recorded by different people on
different dates (the bank clearing date being later than the date on the check). The purpose of the
check number is to serve as a unique identifier for this purpose, whether the problem is being
handled by a computer program or by hand. Deposits and cash withdrawals, which don't have an
identifying number, can be trickier, but the same principle applies: each transaction is an ENTITY,
which appears in at least two forms.
It is common for identity to be significant outside a particular software system, as is the case with
the banking transactions and the apartment tenants. But sometimes the identity is important only
in the context of the system, such as the identity of a computer process.
Therefore:
When an object is distinguished by its identity, rather than its attributes, make this
primary to its definition in the model. Keep the class definition simple and focused on
life cycle continuity and identity. Define a means of distinguishing each object
regardless of its form or history. Be alert to requirements that call for matching objects
by attributes. Define an operation that is guaranteed to produce a unique result for
each object, possibly by attaching a symbol that is guaranteed unique. This means of

Content

73.21%

(page 42)

Persistent use of the UBIQUITOUS LANGUAGE will force the model's weaknesses into the open. The
team will experiment and find alternatives to awkward terms or combinations. As gaps are found
in the language, new words will enter the discussion. These changes to the language will be
recognized as changes in the domain model and will lead the team to update class diagrams and
rename classes and methods in the code, or even change behavior, when the meaning of a term
changes.
Committed to using this language in the context of implementation, the developers will point out
imprecision or contradictions, engaging the domain experts in discovering workable alternatives.
Of course, domain experts will speak outside the scope of the UBIQUITOUS LANGUAGE, to explain and
give broader context. But within the scope the model addresses, they should use LANGUAGE and
raise concerns when they find it awkward or incomplete—or wrong. By using the model-based
language pervasively and not being satisfied until it flows, we approach a model that is complete
and comprehensible, made up of simple elements that combine to express complex ideas.
Therefore:
Use the model as the backbone of a language. Commit the team to exercising that
language relentlessly in all communication within the team and in the code. Use the
same language in diagrams, writing, and especially speech.
Iron out difficulties by experimenting with alternative expressions, which reflect
alternative models. Then refactor the code, renaming classes, methods, and modules to
conform to the new model. Resolve confusion over terms in conversation, in just the
way we come to agree on the meaning of ordinary words.
Recognize that a change in the UBIQUITOUS LANGUAGE is a change to the model.
Domain experts should object to terms or structures that are awkward or inadequate to

Content

73.17%

(page 404)

Figure 16.17. The proposed model, now underconstrained
Figure 16.18. Employees can be associated with the wrong plan.
This model allows each employee to be associated with either kind of retirement plan, so each
office administrator can be switched. This model is rejected by management because it does not
reflect company policy. Some administrators could be switched and others not. Or the janitor could
be switched. Management wants a model that enforces the policy:
Office administrators are hourly employees with defined-benefit retirement plans.
This policy suggests that the "job title" field now represents an important domain concept.
Developers could refactor to make that concept explicit as an "Employee Type."
Figure 16.19. The Type object allows requirements to be met.

Content

72.98%

(page 340)

precise and tailored to their needs. Changing them (for example, by imposing a standardized,
enterprise-wide terminology) requires extensive training and analysis to resolve the differences.
Even then, the new terminology may not serve as well as the finely tuned version they already
had.
You may decide to cater to these special needs in separate BOUNDED CONTEXTS, allowing the
models to go SEPARATE WAYS, except for CONTINUOUS INTEGRATION of translation layers. Different
dialects of the UBIQUITOUS LANGUAGE will evolve around these models and the specialized jargon
they are based on. If the two dialects have a lot of overlap, a SHARED KERNEL may provide the
needed specialization while minimizing the translation cost.
Where integration is not needed, or is relatively limited, this allows continued use of customary
terminology and avoids corruption of the models. It also has its costs and risks.
The loss of shared language will reduce communication.
There is extra overhead in integration.
There will be some duplication of effort, as different models of the same business activities
and entities evolve.
But perhaps the biggest risk is that it can become an argument against change and a justification
for any quirky, parochial model. How much do you need to tailor this individual part of the system
to meet specialized needs? Most important, how valuable is the particular jargon of this user
group? You have to weigh the value of more in-dependent action of teams against the risks of
translation, keeping an eye out for rationalizing terminology variations that have no value.
Sometimes a deep model emerges that can unify these distinct languages and satisfy both groups.
The catch is that deep models emerge later in the life cycle, after a lot of development and
knowledge crunching, if at all. You can't plan on a deep model; you just have to accept the
opportunity when it arises, change your strategy, and refactor.
Keep in mind that, where integration requirements are extensive, the cost of translation goes way

Content

72.85%

(page 115)

The most effective tool for holding the parts together is a robust UBIQUITOUS LANGUAGE that
underlies the whole heterogeneous model. Consistently applying names in the two environments
and exercising those names in the UBIQUITOUS LANGUAGE can help bridge the gap.
This is a topic that deserves a book of its own. The goal of this section is merely to show that it
isn't necessary to give up MODEL-DRIVEN DESIGN, and that it is worth the effort to keep it.
Although a MODEL-DRIVEN DESIGN does not have to be object oriented, it does depend on having an
expressive implementation of the model constructs, be they objects, rules, or workflows. If the
available tool does not facilitate that expressiveness, reconsider the choice of tools. An
unexpressive implementation negates the advantage of the extra paradigm.
Here are four rules of thumb for mixing nonobject elements into a predominantly object-oriented
system:
Don't fight the implementation paradigm. There's always another way to think about a
domain. Find model concepts that fit the paradigm.
Lean on the ubiquitous language. Even when there is no rigorous connection between tools,
very consistent use of language can keep parts of the design from diverging.
Don't get hung up on UML. Sometimes the fixation on a tool, such as UML diagramming,
leads people to distort the model to make it fit what can easily be drawn. For example, UML
does have some features for representing constraints, but they are not always sufficient.
Some other style of drawing (perhaps conventional for the other paradigm), or simple English
descriptions, are better than tortuous adaptation of a drawing style intended for a certain
view of objects.
Be skeptical. Is the tool really pulling its weight? Just because you have some rules, that
doesn't necessarily mean you need the overhead of a rules engine. Rules can be expressed
as objects, perhaps a little less neatly; multiple paradigms complicate matters enormously.