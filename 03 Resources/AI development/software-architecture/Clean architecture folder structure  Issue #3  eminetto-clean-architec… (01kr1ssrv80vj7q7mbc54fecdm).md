---
title: "Clean architecture folder structure · Issue #3 · eminetto/clean-architecture-go-v2"
source: "https://github.com/eminetto/clean-architecture-go-v2/issues/3"
author: "github.com/eminetto"
published: 2023-05-26
created: 2026-05-07
description: "(Note: Newbie to Go here, so maybe all I''m saying does not apply (OO-mindset,"
tags:
  - to-process
  - software-architecture
---

This repository was archived by the owner on May 26, 2023. It is now read-only.


This repository was archived by the owner on May 26, 2023. It is now read-only.


# Clean architecture folder structure #3


Copy link


Copy link


Open


Open


[Clean architecture folder structure](https://github.com/eminetto/clean-architecture-go-v2/issues/3/#top)#3


Copy link


[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=80)](https://github.com/aschrijver)
## Description


[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=48)](https://github.com/aschrijver)
[aschrijver](https://github.com/aschrijver)


opened [on Aug 17, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issue-680180916) · edited by [aschrijver](https://github.com/aschrijver)


Edits


Issue body actions


(Note: Newbie to Go here, so maybe all I'm saying does not apply (OO-mindset, etcetera))


Hi [@eminetto](https://github.com/eminetto)


I was reading your [Clean Architecture, 2 years later](https://eltonminetto.net/en/post/2020-07-06-clean-architecture-2years-later/) with interest and it struck me that I would create a different folder structure. I'd like your opinion on that.


In a hexagonal architecture - and also when you move to microservices - each (sub)domain would be entirely self-contained. You have `Book` core domain and `User` generic domain. In a production app these could grow quite large in feature set they support and there might be potentially many other (sub)domains, like e.g. `Billing`, `Shipping`, `Reviews`, `Authors`, etc.


Your clean architecture has one hexagon with all domains in the center (in `domain/entity`), and some mixing of concerns that I'd plance in different layers (repository impls like `repository_inmem.go` are part of 'infrastructure' layer).


What I was looking at in a Typescript project (with DDD and Command/Query segregation i.e. CQRS) was something like:



```
/core
  └-- /user (generic domain)
         ├-- /domain (inner layer)
         |      ├ user.go (aggregate root)
         |      ├ user_profile.go (entity)
         |      ├ email.go (value object)
         |      ├ password.go (value object)
         |      └ repository.go (repository interface)
         |      ├-- /event
         |      |      ├ user_created.go
         |      |      └ user_verified.go
         |      └-- /error
         |              ├ user_exists.go
         |              └ password_invalid.go
         ├-- /application
         |      ├-- /usecase
         |      |      ├-- /register_new_user
         |      |      |      ├ register_user.go (command)
         |      |      |      ├ register_user_test.go (BDD feature test)
         |      |      |      └ register_user_saga.go (saga)
         |      |      └-- /verify_user_email
         |      |              └ verify_user.go (command)
         |      └ user_service.go
         └-- /infrastructure
                 ├-- /storage
                 |      ├ repository_inmem.go
                 |      └ repository_mysql.go
                 └-- /api
                         └ users.go
/modules
  ├-- /book (core domain)
  |      └    ... same story here ...
  └-- /reviews (sub domain)
          └    ... and here ...

```

Of course I left lotsa stuff out, and probably Go has some root folder [conventions](https://github.com/golang-standards/project-layout). But the idea holds.


## Activity


[![cjslep](https://avatars.githubusercontent.com/u/2395575?u=5f8643d72c1e624e5c206350c3dd9f8ae8ae93c3&v=4&size=80)](https://github.com/cjslep)
### cjslep commented on Aug 26, 2020


[![@cjslep](https://avatars.githubusercontent.com/u/2395575?u=5f8643d72c1e624e5c206350c3dd9f8ae8ae93c3&v=4&size=48)](https://github.com/cjslep)
[cjslep](https://github.com/cjslep)


[on Aug 26, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-681101239)


More actions


That layout *might* be possible in go. Cyclical dependencies are not allowed, which is why golang usually has all data types in the same package so that they can reference each other (data-as-data) or hides them entirely away as interfaces so that none reference each other (data-as-functions). Spreading types out between `core/user/domain` and `modules/book/domain` and `modules/reviews/domain` means they cannot concretely refer to each other (one-way is allowed), without creeping in some interface definitions. That to me is a smell: it goes down a frustrating path of mixed data-as-data or data-as-functions.


A lot of folder layouts inspired from the Uncle Bob or Martin Fowler line of thought were primarily motivated due to the way Object Oriented inheritance works in other languages. A golang-specific consideration is that each folder has a different [import declaration](https://golang.org/ref/spec#Import_declarations) based on the path:



```
import "example.com/core/user/domain" // This is imported as "domain"

var foo domain.User
```

Which means if you have multiple with the same import alias, you'll probably a convention to alias them all:



```
import (
  "example.com/core/user/domain" // "domain"
  "example.com/core/book/domain" // Uh oh, would also be aliased to "domain"
)
import (
  user "example.com/core/user/domain"
  book "example.com/core/book/domain"
)

var foo user.User
var bar book.Book
```

Separations of concerns in Go is slightly different. You can completely separate your data from behaviors using a pattern like:



```
package domain // example.com/modules/user/domain

type Behaviors interface {
  DoFoo()
}

type Statuser interface {
  SetStatus(string)
}

type State interface {
  RequestStatuser() (Statuser, error)
}

func doBusinessLogic(b Behaviors, s State) error {
  u, err := s.RequestStatuser() // not shown: do something with err
  u.SetStatus("hello")
  b.DoFoo()
  // etc.
}
```

Repeat the above for `modules/book/domain` package, another package, etc. This buys immense isolation. However, this is also typically overkill for small programs, requires strict discipline of outlining the problem, and costs a lot of boilerplate.


It is a pattern that essentially treats external data and external behaviors as, simply, a group of functions. So, elsewhere one could implement the `Statuser`, for example, onto a `User` type and `MicroServiceStatusUpdateClient` type, which means this particular isolated logic no longer cares if calling `SetStatus` on a `Statuser` is actually sending data to a `User` data type or winds up calling out to a microservice.


Finally, I do want to note that the clean architecture example has examples where it is problematic, in my opinion. A minor nit is that it uses, in my & the go linter's opinion, problematic visibility features of go. It has exported functions that return unexported types (in `domain/entity/book`): `func NewMySQLRepository(db *sql.DB) *mySQLRepo`. This minor nit actually buries the more pressing matter: for example, another use case eliminates this minor concern but from an architectural point of view is still problematic (in `domain/entity/user`): `func NewMySQLRepository(db *sql.DB) *MySQLRepo`.


In its current state the rest of the code is free to use the `*user.MySQLRepo` concrete type instead of the `user.Manager` interface type, so why have the latter at all? The point of Golang is to have the consumer define the interface, so for example the `domain/usecase` can define a `Manager` interface needed by its logic. So where would that new `ManagerImpl` glue of `*user.MySQLRepo` and `*book.mySQLRepo` be defined? Presumably, the `main.go` program would be responsible mapping any concrete types needed into the business interface logic.


And at this point, it is pretty much classic dependency injection.


👍React with 👍3fmetaphcode, ayunaoss and tareksalem❤️React with ❤️5aschrijver, runabol, julioc98, pwaterz and neko2h


[![eminetto](https://avatars.githubusercontent.com/u/197939?u=9a8120a39f6976a1becc20a49bb6932f147f1643&v=4&size=80)](https://github.com/eminetto)
### eminetto commented on Aug 26, 2020


[![@eminetto](https://avatars.githubusercontent.com/u/197939?u=9a8120a39f6976a1becc20a49bb6932f147f1643&v=4&size=48)](https://github.com/eminetto)
[eminetto](https://github.com/eminetto)


[on Aug 26, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-681112788)


Owner


More actions


[@aschrijver](https://github.com/aschrijver) sorry for the late reply.  

 I agree with the points in the [@cjslep](https://github.com/cjslep)'s text.  

 By the way, thanks [@cjslep](https://github.com/cjslep)! I will fix the problems you pointed.


[![aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=80)](https://github.com/aschrijver)
### aschrijver commented on Aug 27, 2020


[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=48)](https://github.com/aschrijver)
[aschrijver](https://github.com/aschrijver)


[on Aug 27, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-681612145) · edited by [aschrijver](https://github.com/aschrijver)


Edits


Author


More actions


Thank your for the great response, [@cjslep](https://github.com/cjslep) !



>  [@cjslep](https://github.com/cjslep) wrote: Spreading types out between `core/user/domain` and `modules/book/domain` and `modules/reviews/domain` means they cannot concretely refer to each other (one-way is allowed), without creeping in some interface definitions. That to me is a smell: it goes down a frustrating path of mixed data-as-data or data-as-functions.
> 
>  


I have to read more in-depth of how these data-as-data or data-as-functions principles work, so consider this is from my OOP perspective once again. And also DDD, which I am no expert of either, but which might indicate that the above is actually no bad thing at all.


Each (sub)domain defines its own Bounded Context that is internally consistent and in which the domain entities are named after the Ubiquitous Language that applies exclusively within the bounded context. If 2 bounded contexts have a `User` entity, then these can be completely different concepts that may or may not have a mapping between them. So direct references / invocations across bounded contexts need to be avoided, or at least the mapping should be taken care of.


The following image from Martin Fowler's [bounded contexts](https://www.martinfowler.com/bliki/BoundedContext.html) demonstrates this:


[![Bounded contexts](https://camo.githubusercontent.com/547fa4bf7de160cfe5884dbd3c6cd881c420acfa8c9ad44bd03890ed8aa65ec0/68747470733a2f2f6d617274696e666f776c65722e636f6d2f626c696b692f696d616765732f626f756e646564436f6e746578742f736b657463682e706e67)](https://camo.githubusercontent.com/547fa4bf7de160cfe5884dbd3c6cd881c420acfa8c9ad44bd03890ed8aa65ec0/68747470733a2f2f6d617274696e666f776c65722e636f6d2f626c696b692f696d616765732f626f756e646564436f6e746578742f736b657463682e706e67)
I intend to use `Events` to decouple bounded context, though I may not go with full Event Sourcing (where Aggregate Roots are hydrated with a stream of historic events from the db).


In this case, just as an example, a `sessionId` from the Rest API could be the `reviewerId` in a `CreateReview` command sent to the Review subdomain, that triggers a `ReviewCreated` event which is intercepted by the Books core domain where it is mapped to a `readerId` before entering the bounded context.



>  [@cjslep](https://github.com/cjslep) wrote: However, this is also typically overkill for small programs, requires strict discipline of outlining the problem, and costs a lot of boilerplate.
> 
>  


I agree. In my case the project should start as a modest MVP that should be able to evolve over time in size and complexity without the codebase becoming convoluted and needing significant restructuring / refactoring.


Regarding the boilerplate: This is something that OOP people are used to and it can be helpful in application design, though the anti-pattern here is adding too many layers of abstraction. But even in the Golang situation the boilerplate is not all that bad, I think.


The domain design namely, once it is implemented in code, will not change that much over time. It sits conveniently in the center of your hexagonal architecture in the Domain layer, while features are added in the Application layer (and maybe Infrastructure layer depending on architecture choices) by adding a set of `Command`, `Event` and `Query` definitions, and one or more BDD tests for the feature.


This follows a bit boring, but very straightforward process and the feature ends up in its own folder to be directly navigated to. No need to search the code.



>  [@cjslep](https://github.com/cjslep) wrote: It is a pattern that essentially treats external data and external behaviors as, simply, a group of functions. [...] And at this point, it is pretty much classic dependency injection.
> 
>  


Yes, this feels very familiar to me coming from an OOP standpoint as applying interface-based programming and proper inversion of control.


PS. I saw this great, great video about testdriving a full OAuth2 implementation in Golang using DDD, which I highly recommend watching: [OAuth2 Event Modeling in Go, Part 1](https://www.youtube.com/watch?v=32lvL_Un8ko)


👍React with 👍1royling


[![](https://avatars.githubusercontent.com/u/5111931?s=64&v=4)aschrijver](https://github.com/aschrijver)
mentioned this [on Aug 27, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#event-1046414396)


* [Plans for the project inklabs/goauth2#3](https://github.com/inklabs/goauth2/issues/3)


[![](https://avatars.githubusercontent.com/u/5111931?s=64&v=4)aschrijver](https://github.com/aschrijver)
mentioned this [on Oct 1, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#event-1050780253)


* [feat: improvements in structures #4](https://github.com/eminetto/clean-architecture-go-v2/pull/4)


[![aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=80)](https://github.com/aschrijver)
### aschrijver commented on Oct 1, 2020


[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=48)](https://github.com/aschrijver)
[aschrijver](https://github.com/aschrijver)


[on Oct 1, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-701945201)


Author


More actions


(See also comments on new structure by [@eminetto](https://github.com/eminetto) in [#4](https://github.com/eminetto/clean-architecture-go-v2/pull/4))


[@cjslep](https://github.com/cjslep) given my reaction above, highlighting the strict separation between bounded contexts, I think there is no manifestation of a code smell: between boundaries interface-based programming is used. *Full isolation* is a requirement.  

 Within a (sub)domain / bounded context this is not required and you can use both data-as-data and data-as-functions in a folder structure that is best suited for Go.


In [#4 (comment)](https://github.com/eminetto/clean-architecture-go-v2/pull/4#issuecomment-701908180) I also mentioned the 'inversion of control' that goes like `infrastructure ➜ application ➜ domain` (i.e. domain has no dependencies on outer layers, etc.)


Yes, I realize this leads to some amount of boilerplate and a degree of discipline that must be followed. I guess in Go the overall philosophy is to avoid this as much as possible, but the extent to which this is playing a role is already less than what one would have in an OOP-based system of similar complexity.


Then the import issue remains. Let's reconsider your code snippet (I pluralized the domain names):



```
import (
  users "example.com/core/users/domain"
  books "example.com/modules/books/domain"
)

var foo users.User
var bar books.Book
var baz books.Review
```

First of all the observation that this code would not exist in any `domain` layer: they are separated.


Secondly this code will probably also not exist in `application` layer if a CQRS design is followed. There might be an `authorize_user` command in Users domain and a `review_book` command in Books domain. Let's assume that the Books domain has the domain-specific language "A user reviews a book". Then this `user` is an entity in the Books domain and is a different one than the `user` in the Users domain.


There might be a mapper function to go from Users `user` to Books `user`, but this is not needed if passing properties to `review_book` command constructor (e.g. `user.id`, `user.name`) and there is a 1-to-1 match.


Commands are further decoupled by the events or errors that are triggered by their execution. Successful execution of `authorize_user` fires a `UserAuthorized(user)` event. This may trigger a saga (compare: workflow process) that will invoke the `review_book` command, or this occurs in `api` code in the infrastructure layer.


But I digress. In the few places where separate domains are referenced, you must apply appropriate aliases. Also there are still some other import issues..


review\_book.go



```
import (
  "example.com/core/cqrs"
  "example.com/modules/books/domain"
  events "example.com/modules/books/domain/events"
  errors "example.com/modules/books/domain/errors"
)

var foo Reviewer // this is probably what a Books domain would use instead of 'User'
var bar Book
var barrepo Books // this would be the repository interface, and DI would ensure it references proper impl (e.g. MySQL)
var baz events.BookReviewed
var bazerr errors.BookReviewTooShort
```

But I argue these are not so bad.


Another thing I want to address: Go programmers seem to value using (file) naming conventions as short as possible, and have the namespace (folder structure) bring clarity on their intent. E.g. in [#4](https://github.com/eminetto/clean-architecture-go-v2/pull/4) there are a bunch of `service.go` files. This is not done in OOP designs, and I wonder how it would look like in my IDE if I have multiple of these open. Can I still easily tell them apart.


In OOP, but maybe also in my Go project - with a bit of extra discipline - I would add more meaning to the name and use `book_service.go`, `user_service.go`, etc.


Does that make sense, or should I get rid of this OOP habit as a Go programmer?


[![aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=80)](https://github.com/aschrijver)
### aschrijver commented on Oct 6, 2020


[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=48)](https://github.com/aschrijver)
[aschrijver](https://github.com/aschrijver)


[on Oct 6, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-704047974) · edited by [aschrijver](https://github.com/aschrijver)


Edits


Author


More actions


[@cjslep](https://github.com/cjslep) would you be interested in having another *go* at feedback to the additional information here and in [#4](https://github.com/eminetto/clean-architecture-go-v2/pull/4) ?


Also interesting in light of [Event Sourcing in the ActivityPub Server](https://socialhub.activitypub.rocks/t/event-sourcing-the-activitypub-server/972).


[![cjslep](https://avatars.githubusercontent.com/u/2395575?u=5f8643d72c1e624e5c206350c3dd9f8ae8ae93c3&v=4&size=80)](https://github.com/cjslep)
### cjslep commented on Oct 16, 2020


[![@cjslep](https://avatars.githubusercontent.com/u/2395575?u=5f8643d72c1e624e5c206350c3dd9f8ae8ae93c3&v=4&size=48)](https://github.com/cjslep)
[cjslep](https://github.com/cjslep)


[on Oct 16, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-710570571) · edited by [cjslep](https://github.com/cjslep)


Edits


More actions


Sorry that I've been busy. I see that [#4](https://github.com/eminetto/clean-architecture-go-v2/pull/4) has been merged. I also see I've needed to catch up here. :) I'll try to consolidate everything into this post...


**On OOP, and thinking about data in Go**


Let me first start off with saying that Go does not have traditional OOP. No abstract / base classes. There is only "composition" (struct embedding) and "duck typing": if it *behaves* like a duck (`Quack()`) then it is a `Duck`. Like any other language, managing the value types (like AutoValues in Java or dictionaries in Python, etc) for each domain can be tricky. However, with "duck typing" you can separate the *value implementations* from *the information they bring into the domain*.


Using your example:



```
import (
  users "example.com/core/users/domain"
  books "example.com/modules/books/domain"
)

var foo users.User
var bar books.Book
var baz books.Review
```

Let us assume in `"example.com/core/users/domain"` there is this definition:



```
// in the user domain
type User struct {
  id int64
  name string
  email string
  // etc.
}
```

And in `"example.com/modules/books/domain"` for a BookReview, its own user is needed:



```
// in the book domain
type User struct {
  name string
  currentMoodEmoji []byte // I don't know, something not in the other User
}
```

This necessarily requires boilerplate to do the conversion. However, if the above instead were:



```
// in the user domain
type User interface {
  ID() int64
  Name() string
  Email() string
  // etc.
}
// in the book domain
type User interface {
  Name() string // Must match the signature of the other "Name" method
  CurrentMoodEmoji() []byte
}
```

then



```
// all at infrastructure layer

type LivestreamMoodManager struct { /* ... */ }
func (LivestreamMoodManager) CurrentMoodEmoji() []byte { /* ... */ }

type DatabaseUser struct {
  *MoodManager // Struct embedding, composition
   /* etc... */
}
func (DatabaseUser) ID() int64 { /* ... */ }
func (DatabaseUser) Name() string { /* ... */ }
func (DatabaseUser) Email() string { /* ... */ }

// The above implements both User domain requirements at compilation time
var _ users.User = &DatabaseUser{}
var _ books.User = &DatabaseUser{}
```

This isn't a typical design choice, but it works. I want to be clear that it is somewhat deceptive: it's easy to think these domain interfaces are independently defined and de-coupled, but the fact that the overlapping concepts *just so happen* to coincidentally collide method signatures really mean that yes, the code is technically isolated, but the mental concepts may not be. The truth is that both the book-User's concept of `Name` is shared with the user-User's concept of `Name`, despite being expressed in an isolated manner in different domains. If that is indeed desirable, it will result in some tedium of writing accessor methods, which is not idiomatic in the wider golang community. It's not a problem to break out of idioms, just wanted to make you aware.


**On how the above affects the domain/app/infra**


I'm not sure how you're thinking of the split between Domain, App, and Infra. Using the above, the following is how I could see it playing out in terms of go dependencies:


* `domains` depends on nothing ("not even each other" is possible)
* `infrastructure` depends on `domain`
* `application` depends on `domain`
* your `main` dependency-injects `infrastructure` into `application`


Which is a diamond-dependency setup.


So a sample domain:



```
// in the book domain
type User interface {
  Name() string // Must match the signature of the other "Name" method
  CurrentMoodEmoji() []byte
}
```

and the impl infra from above:



```
// all at infrastructure layer

type LivestreamMoodManager struct { /* ... */ }
func (LivestreamMoodManager) CurrentMoodEmoji() []byte { /* ... */ }

type DatabaseUser struct {
  *MoodManager // Struct embedding, composition
   /* etc... */
}
func (DatabaseUser) ID() int64 { /* ... */ }
func (DatabaseUser) Name() string { /* ... */ }
func (DatabaseUser) Email() string { /* ... */ }

// The above implements both User domain requirements at compilation time
var _ users.User = &DatabaseUser{}
var _ books.User = &DatabaseUser{}
```

then your app logic is:



```
// application layer, books == book domain
func DoBusinessLogic(u books.User) error {
  // do fun stuff, only knowing about domain(s)
}
```

And `main` would set it up so that:



```
package main

func main() {
  err := DoBusinessLogic(&infra.DatabaseUser{})
}
```

...and at this point I'm pretty sure something like this is far from the goal of eminetto's repository here. :) From the PR comments it seems like the objective is to balance simplicity and the pursuit of ideological purity. I have no judgement one way or the other.


EDIT: Reviewing the above more, I wouldn't recommend embedding struct literals as I have. Too tightly couples the infra types. Massive headache & inflexibility. The way around this would be to have yet more interfaces at the infra level that encapsulate what other infra pieces need to bring to fill in the gaps... and now we're talking galaxy-brain levels of using interfaces. Embedding anonymous interfaces in structs is not for the faint of heart and is problematic in its own right due to the fact that when composing, method signatures are *strictly* **not** allowed to overlap.


**On file/folder naming**


File names are a matter of personal preference. :) I don't have much more to say on that (excepting the special suffixes like `_test.go` that have special meaning).


This is probably redundant of me to bring up, but want to mention for completeness: Since folder naming dictates the package name (except for `main`), Go tends to favor succinctness in type names. Instead of having:



```
package services

type UsersService struct { /* ... */ }
```

where people using it would type the redundant `services.UsersService`, it's more readable to just name the struct `services.Users`.


...but when you invert that name, then filenames can indeed seem a little weird. In the case of the lots of `service.go` files in this repot, it seems to be because there's a lot of `Service` types, because the package is the descriptive usecase name. So it is `books.Service` in `books/service.go`, `users.Service` in `users/service.go`, etc. But the filename could be anything.


[![aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=80)](https://github.com/aschrijver)
### aschrijver commented on Oct 17, 2020


[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=48)](https://github.com/aschrijver)
[aschrijver](https://github.com/aschrijver)


[on Oct 17, 2020](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-710767361)


Author


More actions


Yet again I want to say I greatly appreciate your elaborate response, [@cjslep](https://github.com/cjslep) Thank you!


(I hope I don't bore both of you with my responses coming from an OOP mindset. For me the exercise is very valuable, and in OOP world DDD architectures are more commonplace. With renewed interest in these architecture designs I hope you find it equally interesting to see how things fit in Golang world.)



>  [@cjslep](https://github.com/cjslep) **wrote**: ...and at this point I'm pretty sure something like this is far from the goal of eminetto's repository here. :) From the PR comments it seems like the objective is to balance simplicity and the pursuit of ideological purity.
> 
>  


Yes, it is far from [@eminetto](https://github.com/eminetto) goal. But it is not about ideological purity either. It is about dealing early with complexity that you know will become an issue later on. Though clean architecture gives some benefits to small-scale project, it really starts to shine for projects that you know upfront will be complex both in terms of the domains it supports, as well in the amount of code that's needed to implement them.


My use case is a Fediverse platform where less-technical developers + users develop 'service modules' (plugins) that add support for arbitrary custom vocabularies + logic (domains). The deeper they can integrate with what's already out there, without causing problems, the better.



>  I want to be clear that it is somewhat deceptive: it's easy to think these domain interfaces are independently defined and de-coupled, but the fact that the overlapping concepts just so happen to coincidentally collide method signatures really mean that yes, the code is technically isolated, but the mental concepts may not be.
> 
>  


If I read this correctly, then conceptually the domains are not decoupled. There are implicit dependencies based on the method signatures that need to match. In that case explicit mappings (yes, boilerplate) seem preferable.


Another observation is that the implementation of `ID`, `Name` and `Email` is in infra layer with this. In DDD terms these properties are often Value Objects (and they may have some shared functionality, such as `validate()`). The ID would e.g. be an `EntityID` and you might have an `EmailAddress` value object. These are trivial cases, but e.g. a `Password` value object could implement the password strength policy of the company, and a `PostalAddress` value object the domain rule "Only allow *valid* addresses in the US and Canada", where the value object gets an address validation service injected in the application layer (e.g. in a `ValidateBuyer` command that is part of a `PurchaseProduct` saga).


The app logic would fetch and hydrate domain entities (going from the aggregate roots), then invoke domain logic on them which yield results and/or trigger events.


The infra logic, e.g. the API, would take data from external sources and (in a POST request) pass it on to the correct app logic (a Command in CQRS architecture) or retrieves data (in a GET request) from the app logic (invoking a Query in CQRS terms).


The `infrastructure` does not necessarily depend on `domain` (in a strict inversion of control set up it does not). It does not need to know that a User is a User. Just that it received a data object that must be passed to `ValidateUser` command.


### Layered architecture


It is interesting to look at the OAuth2 project of [@pdt256](https://github.com/pdt256) I referenced earlier. All the code for the domain lives in the same folder here, and the naming indicates what's in each file (commands, events, etc.). If this were a multi-domain project some more folder structure would be needed (e.g. these files in subfolder `oauth2`).


But I think there's another issue, in that there's no strict layering being implemented. Take e.g. [resource\_owner.go](https://github.com/inklabs/goauth2/blob/master/resource_owner.go), an aggregate root. This file contains both infrastructure code and command logic.


* If the project would switch to a different database than RangeDB, then all domain classes would need to change: The business domain changes based on an implementation choice.
* If the project would add a feature (Command) that is not domain-related, then the domain classes would need to change: The business domain changes based on application or UI logic.


(Note that in this case the choices are valid ones, because with the current implementation the OAuth2 impl is near complete)



>  But the filename could be anything.
> 
>  


Agreed. As long as filename + folder structure clearly convey what can code be found inside the file. I think I will need to experiment here a bit. A bit more discipline / boilerplate may be in order here, if that leads to things becoming less error-prone when less technical devs building extensions on the platform.


[![aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=80)](https://github.com/aschrijver)
### aschrijver commented on Jan 22, 2021


[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?v=4&size=48)](https://github.com/aschrijver)
[aschrijver](https://github.com/aschrijver)


[on Jan 22, 2021](https://github.com/eminetto/clean-architecture-go-v2/issues/3#issuecomment-765131352)


Author


More actions


Hi [@eminetto](https://github.com/eminetto) .. a FYI: I found this project and the related articles to be an invaluable resource to understand many of the concepts I want to implement: <https://github.com/ThreeDotsLabs/wild-workouts-go-ddd-example>


👍React with 👍3eminetto, fmetaphcode and jeijei4


[Sign up for free](https://github.com/signup?return_to=https://github.com/eminetto/clean-architecture-go-v2/issues/3) **to join this conversation on GitHub.** Already have an account? [Sign in to comment](https://github.com/login?return_to=https://github.com/eminetto/clean-architecture-go-v2/issues/3)


## Metadata


## Metadata


### Assignees


No one assigned


### Labels


No labels


No labels


### Projects


No projects


### Milestone


No milestone


### Relationships


None yet


### Development


No branches or pull requests


### Participants


[![@eminetto](https://avatars.githubusercontent.com/u/197939?s=64&u=9a8120a39f6976a1becc20a49bb6932f147f1643&v=4)](https://github.com/eminetto)
[![@cjslep](https://avatars.githubusercontent.com/u/2395575?s=64&u=5f8643d72c1e624e5c206350c3dd9f8ae8ae93c3&v=4)](https://github.com/cjslep)
[![@aschrijver](https://avatars.githubusercontent.com/u/5111931?s=64&v=4)](https://github.com/aschrijver)
## Issue actions