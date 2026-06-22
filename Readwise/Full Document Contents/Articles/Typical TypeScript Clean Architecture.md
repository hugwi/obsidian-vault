# Typical TypeScript Clean Architecture

![rw-book-cover](https://cdn.blog.zacfukuda.com/2025/5/typical-typescript-clean-architecture-thumb.webp)

## Metadata
- Author: [[https://www.facebook.com/zac.fukuda]]
- Full Title: Typical TypeScript Clean Architecture
- Category: #articles
- Summary: Clean Architecture organizes software into layers, keeping business rules at the center and external systems at the edges. This approach helps separate concerns and makes the system easier to maintain and understand. The article explains how to apply Clean Architecture principles using TypeScript for clearer and more practical design.
- URL: https://www.zacfukuda.com/blog/typical-typescript-clean-architecture

## Full Document
Model View Controller pattern or any web framework does a job. Very, very quick. Very Scalable? I don't think so.

Since I became a programmer, or web designer formerly, my projects have been small. Ten-page website was average. My clients were usually small business owners. They didn't have much budget for the website. The primary reason why they wanted to have websites is not to boost their revenue. They wanted a bare minimum of trust from their customers. I am not a corporate type. I don't fit working in a big company. Even in a team. It has been very pleasurable working with customers very closely. I could hear what they wanted directly and exactly. No messaging intermediary involved. Also, they were very independent. No one blamed their environment, more precisely their superiors and coworkers. They were the superiors.

Despite these satisfaction with customers, I started to feel my ability is over spec for their small websites since a few years ago. I want to build something more sophisticated. So I got a part time engineering job through the agent. The job is to build an internal corporate system from scratch. We use Laravel and React.js as a main framework and library. Another developer was also hired at the same time. We worked hand in hand. Four or five other engineers joined. Only two of them stuck. I was taking a chief engineer position. I really enjoyed it…for one year.

After one year, I started to feel again that my ability was over spec for the project. I practiced React.js very much. I saw a lot of margin perfecting my React.js skill. The team also saw the similar view. They wanted to scale more of a single paged application. But the backend and infrastructure tech? They were quite oblivious to what's going on out there. The server was monolith. No sign of adopting ECS. No desire to modernize the infrastructure. “I think we should use the container for production environment,” I said. “I haven't heard anyway using Docker for production.” said the other engineer.

Several months passed. I quit the job, in search of a bigger project. I landed on a consumer-business relation web application. The application draws over a million page views per month. It brought up ten-times monthly revenue than the websites I used to build. Maybe ten-times is a selfish estimation. It brought up a hundred times revenue than the website I built.

My new client had been developing a monolith application, just like the one I worked on. The app is built with Laravel, just like the one I worked on. Before my joining, they were modernizing infrastructure. They began to use CloudFront, ALB, Lambda, CodePipeline, ECS, Terraform, GitHub actions and so on. As a part of modernization they just started to replacing a consumer part of application with Next.js. That was what I was signed up for.

The Next.js project was led by a three-year experienced web engineer, who shall be anonymously called Honda. He had a lack of experience but lot of enthusiasm. The purpose of replacement was to develop a consumer application free from administrative dashboard pages, at scale. The project had been going on for a year and three months when I joined. By then, the application was already a mess, at least in my point of view, but not in the Honda's, who was, organizationally speaking, my new boss. (I didn't see him as a boss, not because he was friendly but because he looked so junior to me. And he was.)

I'd done performance test using Playwright and artillery, then written unit tests with Jest as much as possible on the code the project lead had written.

It was time for me to develop an application. “We should design an architecture.” said Honda. “Huh.” I replied.

I had heard “architecture.” But I had never done an architecture. The frameworks enable you to build applications unconcerned about architecture. I mean, that is what the “frame” is all about.

The project lead and I did pair-programming. I programmed, he oversaw. We did so day after day for a week. He made me programmed. When something didn't look right, he pointed out. I fixed. Sometimes I counter argued. Nevertheless, his gigantic enthusiasm left me little space for him to listen. The fact was that we—actually I, who was bringing the next release—were running out of time to the deadline. It would oppress me more and more if we argued longer and longer. Plus, I saw the project lead would not stick to this project for long time future. His enthusiasm was telling me he would leave this job when he got everything he wanted from this project. What he wanted was a impressive resume. (It turned out I was right on this.) It is a waste of time discussing with someone temporally. Hence I compromised.

Eventually, we got a software architecture shown in the figure 1.

![Impersonating architecture](https://cdn.blog.zacfukuda.com/2025/5/impersonating-architecture@2x.webp)Figure 1. Impersonating Architecture
I found this architecture ambiguous and impractical. Honda found it the state of the art. I personally call this *Impersonating Architecture*.

The confusion rooted, I believed, in that he was mixing up the Clean Architecture, Layered Architecture, and Domain Driven Design without the much of deliberation. The jargons bespoke. The architecture impersonates.

Since the birth of Impersonating Architecture, I embarked on TypeScript Clean Architecture idea. I read *Clean Architecture* by Robert C. Martin, *Object Oriented Software Design* by Ivar Jacobson, *Structure and Interpretation of Computer Programs* by Harold Abelson and Gerald Jay Sussman, *Domain Drive Design(DDD)* by Martin Fowler. I also bought a Japanese magazine, topic of which is how to integrate DDD with Clean Architecture. This magazine provided me the source code that I wanted more than theory and knowledge. I even read *Good Code, Bad Code* by Tom Long, though which has nothing to with software architecture. I just needed a bit of break.

It is not yet perfect. But I think now I reached to a [typical TypeScript Clean Architecture version 1.0.0](https://github.com/zacfukuda/typescript-clean-architecture). I'd like to emphasize that it is a “typical” TypeScript Clean Architecture. That said, it is not practical in that:

(1) It does not follow functional programming paradigm.

TypeScript and JavaScript by nature are object oriented programming languages. But we many TS/JS engineers decided to use them in functional way. We define bunch of I/O functions, chain them up together one after another until we get what we want. That is how modern TypeScript applications are made. Lots of Promise, Promise, Promise. Your library might have a class. But your core application might not have any class. You only have objects and functions.

(2) You don't need view models anymore. Maybe presenter as well.

Most of web applications are now REST APIs. The output of REST API is a JSON, which is just a text that represents a data structure. It is a job of the REST API client to implement presenters and view models. Your frontend and backend application as a whole look like a Clean Architecture. But as an individual application it lacks complete architecture. Lacking Architecture?. You might wonder. But isn't it exactly the point why we wanted to separate frontend application from backend.

Anyway, I wanted to be able to build a typical TypeScript Clean Architecture before I would be able to build a practical one. I believe it would give me an edge to understand the fundamental basics of Clean Architecture. To skip this process will cause a future disaster…like Impersonating Architecture.

#### Clean Architecture

In this article I want to introduce you to my process of implementing Clean Architecture. Before do that, let's recap what Clean Architecture is.

Clean Architecture is proposed by Robert C. Martin. The heart of Clean Architecture lays enterprise business rules. The term "rule" could be translated into "layer." All business related programs shall belong to this rule. These programs are called *Entities*. It could be a state object like Product or could be an actor object like Consumer. Consumer buys Product. So far, so good.

Outside of enterprise business rules are application business rules. These rules are more software related. Entities must be, ideally speaking, a mirror of business. (You might call these mirrors Model but let's just skip this topic.) Applications business rules are, on the other hand, medium to work on your *Entities*. This is where your *Entities* are given life, where software becomes the software. These Moses like programs, which give light to people of Israel, are *Use cases*.

Outside of Applications business rules are interface adapters. Adapters are agents. Moses is shy. He needs Aron. He needs a translator. He needs a representative. This is a kind of relation between Use cases and Adapters. Controllers, presenters, and gateways are examples of adapters in software and computer.

Then we have frameworks and devices at the most outer part. These are not your software. Some other folks build it. You don't care who they are or what they are, at least technically speaking. You would care very much if they brings you cash. There is nothing you can do about these things. It is outside of your control; it is outside of your software. Your software ends at interface adapters. Let the world speak to your software through interface adapters.

Thus we have relations of frameworks and devices-interface adapters-application business rules-enterprise business rules. That is Clean Architecture.

Clean Architecture would be illustrated as circular rings. It looks like onion rings. I could embed the image from Clean Architecture book or Martin's website. But something stopped me. I wanted it to be more like layers. So the figure 2 is a flatten version of Clean Architecture depicted.

![Flatten version of clean architecture](https://cdn.blog.zacfukuda.com/2025/5/clean-architecture-flatten@2x.webp)Figure 2. Clean Architecture Flatten
The objective of Clean Architecture, or any other architecture, is to establish dependency rules. We slice one software into layers, let each of which has a distinct role and purpose. One layer can dependent on the same layer or one layer below/inward. One layer should not know anything about the above/outward layer.

Beside famous Clean Architecture illustration is a diagram on the flow of control in the architecture. The figure 3 is a copy of original.

![Clean Architecture - the flow of control](https://cdn.blog.zacfukuda.com/2025/5/clean-architecture-flow-of-control@2x.webp)Figure 3. Flow of control
To this point, Clean Architecture is just a theory. It gives you an idea but it does not tell you how to make it at all. The chapter 22 of *Clean Architecture* book provides the UML of typical web-based Java system design. The UML is the closest thing we can ever get from the book about how to implement Clean Architecture. The figure 4 shows the design. I added bit of modifications so that the concept and terms are concordant with the circles.

![Typical Clean Architecture system design](https://cdn.blog.zacfukuda.com/2025/5/typical-typescript-clean-architecture@2x.webp)Figure 4. Typical web system in Clean Architecture
It is pretty much like the figure 2 shows, except the inside the application logic rules, the use cases. The use cases are best described not by Martin, but by Ivar Jacobson, the author of *Object Oriented Software Design*. The subtile of the book reads “A Use Case Driven Approach.” Lots must be going on in the use case.

The reason why people love Clean Architecture is that it puts database or something external outside of your application. In the traditional Layered Architecture, the database comes at very bottom, under the application layer, under the business layer, under the persistence layer. The very, very bottom. If the database changes, in theory, whole your application needs to change as well. It's like your database provider owns your application as if your bank owns your company. It's not a healthy relationship. The database provider can hedge their risk. In a meantime you would take greater risks. Your database provider might bankrupt. They would introduce you to the newer and better version of product line, at higher price. You might want to switch to the other vendor but the cost of doing so outweighs the benefit. So you'd stick to the current vendor in sorrow. Heck.

So the question is “how do we put our vendors having nothing to do with our core business?” Answer: **Dependency Inversion**. The implementation of Clean Architecture is all about it.

#### Implementation

I introduce you to the process of developing a web-based simple auto teller machine(ATM). The ATM has three features:

1. Balance teller
2. Deposit
3. Withdrawal

I wish I could go through every features. But that would be very long and tiresome. So I show you only the case of balance teller. Also I only show you the process. For the source code please refer to my [GitHub repository](https://github.com/zacfukuda/typescript-clean-architecture). The source code includes both CLI and Web application.

Entities will never change unless your business changes. Let me say that again. Entities “will” never change unless your business changes. It's not that entities “should” never change unless your business changes. It's not an opinion. It's a fact. You've got to be more of a business man than a programmer to design and implement entities.

So what kind of entity do we need to make our balance telling work. Obviously, Balance.

```
export class Balance {
  constructor(
    public readonly accountNumber: string,
    public readonly balance: number
  ) {}
}
```

This was my first attempt. I designed the database accordingly, which basically has only numeral information.

After I finished making balance telling, I started to implement the deposit feature. In that process I made Transaction entity. Then it struck me. The information about your balance is right there. Your current balance is written in your latest transaction. This is how you tell the balance. So I deprecated my Balance entity and eventually got a Transaction entity that I can use for all of balance telling, deposit, and withdrawal.

```
export class Transaction {
  constructor(
    public readonly date: Date,
    public readonly debit: number | null,
    public readonly credit: number | null,
    public readonly balance: number
  ) {}
}

```

After all, we used to know our current balance by checking the last transaction recorded in our bank note. And this Transaction entity is the best model of our real, physical world. And this Transaction entity is not going to change for long time.

You might ask at this point “why don't you create a BankNote entity that hold the collection of Transaction?” I could. But I think it is too much for the demo.

#### Use case

The figure 4 shows you what lays under the use case. Namely, Input Data, Input Boundary, Output Data, Output Boundary, Data Access, and Interactor. The heart of use case is an interactor.

“You should call an interactor an use case.” Martin shares his story about Clean Architecture at [one of tech conferences](https://www.youtube.com/watch?v=2dKZ-dWaCiU&pp=ygUSY2xlYW4gYXJjaGl0ZWN0dXJl). Anyway he decided to call it an interactor.

I agree with him on this. In object oriented programming there are basically two types of objects: state object and control object. A state object is a mere record of something. It does not have a spirit. It can't do anything on his own. A control object mutates and interacts with state objects. It is a agent. It produces behaviors by itself. These control objects are named something actor in the practice of OOP. If you call an interactor a use case, the name would give you an impression that that object does nothing on its own. Non actor object shall not have a verb property, i.e. a method.

What Clan Architecture distinguishes from the other architecture are interfaces defined in the use case. They are Input Boundary, Output Boundary, and Data Access. By providing the interfaces to the outside of application, your application becomes independent of third parties or UI. Rather, they depend on your application.

##### Data Access

![Data Access design](https://cdn.blog.zacfukuda.com/2025/5/data-access@2x.webp)Data Access design
The Data Access is an interface how database client are plugged in to your application. Although your application will have much of control over how to retrieve data or how it should be mutated, still your application needs database, and the application will highly depend on it. There is no question about it. Data Access is sometimes called Repository, interchangeably. I am not sure the implementation of Data Access is the Repository, or a Repository is also an interface and implementation of Repository is call something Repository like MySQL Repository.

As mentioned above, you would know your balance of your bank account by checking the last transaction information. So in the case of balance telling, the Data Access have an interface like this:

```
import { Transaction } from "./entities";

export interface BalanceTellerDataAccess {
  readLastTransaction(accountNumber: string): Promise<Transaction>;
}

```

You might thinks it is a bad idea to simply pass a string to the Data Access. Instead it would be better to have an entity like Account or AccountNumber, and pass that entity to the Data Access. You are absolutely right. You should. But I just decided to use primitives. This article is about architecture. Not about implementation detail. Primitives make things more understandable.

Junior programmers don't start writing code by interfaces. They jump on implementations. I was one of them. I wanted to write the code that does the job right away and move on. Or getting paid. Let's just slow down a little bit.

You don't care how the data are retrieved at this point in the use case. That is the whole point of Clean Architecture. The implementation does not matter. The Data Access says “we are just going to provide you the interface. Do whatever you want with it.”

No implementation detail makes programmers anxious. Well…get over it.

##### Input Data

The Input Data is a struct data that will eventually passed to the Input Boundary as an argument. In many real cases, this Input Data will be something similar to the arguments of Data Access's methods. In order to get the balance of one bank account, we need an account number of the person.

```
export class BalanceTellerInputData {
  constructor(public readonly accountNumber: string) {};
}

```

##### Input Boundary

![Input Boundary design](https://cdn.blog.zacfukuda.com/2025/5/input-boundary@2x.webp)Input Boundary design
The Input Boundary is an interface that will eventually be implemented by an interactor. You already have an argument of Input Boundary's method an Input Data. So, the only thing left to complete the interface is what you should return. I will give you an answer. Nothing. Just void.

```
import { BalanceTellerInputData } from "./BalanceTellerInputData";

export interface BalanceTellerInputBoundary {
  handle(balanceTellerInputData: BalanceTellerInputData): Promise<void>;
}

```

How is that possible?

The use case delegates this matter to the Output Data and Output Boundary.

##### Output Data

In a traditional sense, an Output Data is what you want to return with a method from the use case to the interface adapter. What do you want to return with balance teller's method? Balance.

```
export class BalanceTellerOutputData {
  constructor(
    public readonly accountNumber: string,
    public readonly balance: number
  ) {}
}

```

We might not need to return accountNumber because that comes from the client and the client already have it. Anyway, I decided to add accountNumber to make the use case be more applicable for general purposes.

##### Output Boundary

![Output Boundary design](https://cdn.blog.zacfukuda.com/2025/5/output-boundary@2x.webp)Output Boundary design
The Output Boundary is an interface that would be eventually implemented by the Presenter. You already have an argument of Output Boundary's method Output Data. So, the only thing left to complete the interface is what you should return. I will give you an answer. Nothing. Just void.

```
import { BalanceTellerOutputData } from "./BalanceTellerOutputData";

export interface BalanceTellerOutputBoundary {
  handle(balanceTellerOutputData: BalanceTellerOutputData): void;
}

```

How is that possible? Presenter has the answer. We'll come back shortly for that.

##### Interactor

![Interactor design](https://cdn.blog.zacfukuda.com/2025/5/interactor@2x.webp)Interactor design
An Interactor implements the Input Boundary. This is where all use cases data structs and interfaces be orchestrated.

```
import type { BalanceTellerInputBoundary } from "./BalanceTellerInputBoundary";
import type { BalanceTellerOutputBoundary } from "./BalanceTellerOutputBoundary";
import type { BalanceTellerDataAccess } from "./BalanceTellerDataAccess";
import { BalanceTellerInputData } from "./BalanceTellerInputData";
import { BalanceTellerOutputData } from "./BalanceTellerOutputData";

export class BalanceTellerInteractor implements BalanceTellerInputBoundary {  
  constructor(
    private readonly balanceTellerDataAccess: BalanceTellerDataAccess,
    private readonly balanceTellerOutputBoundary: BalanceTellerOutputBoundary
  ) {}

  async handle(balanceTellerInputData: BalanceTellerInputData): Promise<void> {
    const { accountNumber } = balanceTellerInputData;
    const transaction = await this.balanceTellerDataAccess.readLastTransaction(accountNumber);
    const balanceTellerOutputData = new BalanceTellerOutputData(accountNumber, transaction.balance);

    this.balanceTellerOutputBoundary.handle(balanceTellerOutputData);
  }
}

```

The notable thing about the interactor is that it has BalanceTellerDataAccess and BalanceTellerOutputBoundary injected. It declares what it wants, but does not interfere on how the things are achieved. Two dependencies are injected in runtime, not compile time. Both Data Access and Output Boundary are subjects of use case, same as interactor. The interactor should not know about outside of its layer. No outside dependency.

#### Gateway

Gateway is, in this article, an implementation of Data Access interface. The term gateway might not be preferable in many projects. We have internet gateways, api gateways, and so on. Lots of gateways in infrastructure. It would could be confusing if there is a gateway in the application. People love to call it Repository. But I stick to Gateway to be concordant with the famous hour-circle illustration of Clean Architecture.

In this article and the sample source code, I use file system as our database. Setting up the SQL server is cumbersome. The file of transactions, the database, is a CSV file. The CSV file formats date, debit(deposit), credit(withdrawal), and balance comma-separated.

The implementation of Data Access, Gateway, has to do two things.

1. It must read the last transaction of a specific account from the database, from a file in our situation.
2. It must translate the retrieved data into Transaction entity, then return it.

```
import { readFile } from "node:fs/promises";
import path from "node:path";
import { cwd } from "node:process";
import { Transaction } from "use-cases/deposit/entities/Transaction";
import type { BalanceTellerDataAccess } from "use-cases/balance-teller/BalanceTellerDataAccess";

export class BalanceTellerFileSystemGateway implements BalanceTellerDataAccess {
  async readLastTransaction(accountNumber: string): Promise<Transaction> {
      const fileName = 'transactions.csv';
      const filePath = path.resolve(cwd(), 'database', 'accounts', accountNumber, fileName);
      const content = await readFile(filePath, 'utf8');
      const lines = content.trim().split('\n');
      const lastLine = lines[lines.length - 1];
      const fields = lastLine.split(',');
  
      const date = new Date(fields[0]);
      const debit = fields[1] ? Number(fields[1]) : null;
      const credit = fields[2] ? Number(fields[2]) : null;
      const balance = Number(fields[3]);
  
      return new Transaction(date, debit, credit, balance);
    }
}

```

From the stand point of the use case, the implementation BalanceTellerFileSystemGateway does not matter. The only thing that matters is that it satisfies BalanceTellerDataAccess. The use case relies on BalanceTellerDataAccess, which is a part of the use case, not on BalanceTellerFileSystemGateway. The use case doesn't care if you use the file system or MySQL. It doesn't care if you would switch your database from file system to MySQL to DynamoDB. The database changes; the interface never changes; your use case never changes. And God would see it is good.

The input signal to your application comes through a Controller. I mean through, not from. In a web application all signals come from HTTP network. But in a desktop application the signals come from controllers like keyboards and mouse.

A Controller uses the two things provided by the use case: the Input Data and Input Boundary. You know in your brain the equation Input Boundary = Interactor. But a controller doesn't. An interactor is behind the scene. The responsibility of controller is to translate user's input into an Input Data and call the Input Boundary method. The controller wouldn't know how it is handled. It is very confidential. The controller even wouldn't get a returning data. The Input Boundary says “we've got this handled.” If a controller is a decent citizen of one nation, he/she would see an use case a tyranny. Yes, it is. We want our use cases to be tyrannies, and entities to be gods.

```
import { BalanceTellerInputData } from "use-cases/balance-teller/BalanceTellerInputData"
import type { BalanceTellerInputBoundary } from "use-cases/balance-teller/BalanceTellerInputBoundary";

export class BalanceTellerWebController {
  constructor (
    private readonly balanceTellerInputBoundary: BalanceTellerInputBoundary
  ) {}

  async get(accountNumber: string): Promise<void> {
    const balanceTellerInputData = new BalanceTellerInputData(accountNumber);
    
    await this.balanceTellerInputBoundary.handle(balanceTellerInputData);
  }
}

```

The Presenter is an implementation of Output Boundary, which will be injected into an Interactor instance. Beside the Presenter is a View Model. Which put a Presenter in an awkward position. It is sandwiched by a Use Case and View. It must slave to both of those. Presenter is where most of changes happen. When a use case changes, the Presenter must change. When View(UI) changes, the Presenter must change. The Presenter can never have a good night sleep.

Honestly, I was not sure about the best, at least good, way to implement Presenter-View Model-View. I struggled. I search “clean architecture” on GitHub. I found hundreds of sample projects, only a few were good sample, but none of them follows Martin's original Clean Architecture UML design like the figure 4. They were happy to blend their flavor and practice. So I imitated [the source code of a sample Clean Architecture Java project](https://github.com/nrslib/gihyo_software_design_clean_architecture_sample) that I found in a piece of Japanese tech magazine.

```
export class BalanceTellerWebViewModel {
  constructor(public readonly balance: number) {}
}

```

```
import type { BalanceTellerOutputData } from "use-cases/balance-teller/BalanceTellerOutputData";
import type { BalanceTellerOutputBoundary } from "use-cases/balance-teller/BalanceTellerOutputBoundary";
import { BalanceTellerWebViewModel } from "./BalanceTellerWebViewModel";

export class BalanceTellerWebPresenter implements BalanceTellerOutputBoundary {
  private viewModel: BalanceTellerWebViewModel;

  handle(balanceTellerOutputData: BalanceTellerOutputData) {
    const { balance } = balanceTellerOutputData;
    this.viewModel = new BalanceTellerWebViewModel(balance);    
  }

  result(): BalanceTellerWebViewModel {
    return this.viewModel;
  }
}

```

The Presenter sets its view model as it is given the Output Data in the method. The result() returns that View Model which eventually passed to the View.

Our BalanceTellerOutputData has a accountNumber property as well. But I decided not to use it in our View Model. This is to indicate that you don't always have to pass everything you get in the Output Boundary to View Model.

If you don't like the method name result(), you can change the name of private property for View Model to #viewModel, which is a native JavaScript syntax, and name the method viewModel().

```
export class BalanceTellerWebPresenter implements BalanceTellerOutputBoundary {
  #viewModel: BalanceTellerWebViewModel;

  handle(balanceTellerOutputData: BalanceTellerOutputData) {
    const { balance } = balanceTellerOutputData;
    this.#viewModel = new BalanceTellerWebViewModel(balance);    
  }

  viewModel(): BalanceTellerWebViewModel {
    return this.#viewModel;
  }
}

```

#### View

View is only aware of View Model. No more, no less. It is very common for modern web applications that Response body is formatted as a JSON string. Let our View have a method that returns JSON string from the View Model.

```
import { BalanceTellerWebViewModel } from "./BalanceTellerWebViewModel";

export class BalanceTellerWebView {
  render(balanceTellerWebViewModel: BalanceTellerWebViewModel): string {
    const { balance } = balanceTellerWebViewModel;

    return JSON.stringify({ balance });
  }
}

```

A typical TypeScript or JavaScript application doesn't have main.ts. Neither main(). Here, the main means a program responsible for receiving the HTTP request and sending the HTTP response. In [Express](https://expressjs.com/) the main is a callback function you pass to Router's method.

This article has nothing to do with Express but Clean Architecture. As a disciple of Martin or Clean Architecture, you are incline not to depend on third party vendors, who eventually mess with us sooner or later.

```
import { BalanceTellerFileSystemGateway } from 'gateways/balance-teller-file-system-gateways';
import { BalanceTellerInteractor } from 'use-cases/balance-teller/BalanceTellerInteractor';
import { BalanceTellerWebPresenter, BalanceTellerWebController, BalanceTellerWebView } from './balance-teller-web-interface-adapters';

async function callback(request: Request, response: Response) {
  // URL/body parsing, etc…
  
  const balanceTellerDataAccess = new BalanceTellerFileSystemGateway();
  const balanceTellerOutputBoundary = new BalanceTellerWebPresenter();
  const balanceTellerInputBoundary = new BalanceTellerInteractor(balanceTellerDataAccess, balanceTellerOutputBoundary);
  const balanceTellerWebController = new BalanceTellerWebController(balanceTellerInputBoundary);
  const balanceTellerWebView = new BalanceTellerWebView();

  await balanceTellerWebController.get(accountNumber);
  response.writeHead(200, { 'Content-Type': 'application/json' });
  response.end(balanceTellerWebView.render(balanceTellerOutputBoundary.result()));

  return;
}

```

You would think that the instantiation of all classes is cluttered. Some frameworks have a Dependency Injection(DI) container to make this procedure simple. DI container is out of scope of this article. In fact, I don't have much knowledge about. I shall read [*Dependency Injection Principles, Practices, and Patterns*](https://mng.bz/BYNl).

Congratulation. We got ourselves a Clean Architecture.

#### To Be Practical

I'd like to point out, as I mentioned earlier, that the design and implementation shown above are typical TypeScript Clean Architecture that strictly follows the UML design Martin provides us. The design, in my opinion, is nothing practical. To make our TypeScript Clean Architecture more practical, I believe we can do two things.

1. Remove OOP
2. Remove View Model

I shall deal these matters in the following article.
