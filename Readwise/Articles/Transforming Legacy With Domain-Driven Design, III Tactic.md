# Transforming Legacy With Domain-Driven Design, III: Tactic

![rw-book-cover](https://hackernoon.imgix.net/images/3L1CP4liRQQ55QjQn3vJVyA00H52-8923de2.jpeg)

## Metadata
- Author: [[Anton Musatov]]
- Full Title: Transforming Legacy With Domain-Driven Design, III: Tactic
- Category: #articles
- Summary: This article explains practical, tactical patterns of Domain-Driven Design to modernize legacy systems. It outlines layered architecture (Client, Application, Domain, Infrastructure) and key patterns like Commands, Entities, Value Objects, Services, Specifications, Events, and Repositories. These techniques keep business logic isolated, explicit, and easier to change or integrate.
- URL: https://hackernoon.com/preview/GIXDHQTOJ0Lk9rW9wZDl?ref=hackernoon.com

## Full Document
[[Full Document Contents/Articles/Transforming Legacy With Domain-Driven Design, III Tactic.md|See full document content →]]

## Highlights
- The command pattern is a good fit for structuring an internal API to the domain. It is a behavioral design pattern that turns requests into distinct objects. These objects typically have a single `execute` method that triggers the action. Request parameters can be stored as fields in the command object through a constructor, thus formalizing the request parameters explicitly and encapsulating interactions with domain objects within the command objects. ([View Highlight](https://read.readwise.io/read/01kbbcmmyfxpncmjbysg054z6v))
