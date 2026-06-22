---
title: "Understanding Epics, Features, And User Stories"
source: "https://scrumdistrict.com/understanding-epics-features-and-user-stories/"
author: "Scrum Master"
published: 2021-05-26
created: 2025-12-16
description: "To avoid constraining teams, the Scrum Guide is not clear about each of these"
tags:
  - to-process
  - startup-business
---

To avoid constraining teams, the Scrum Guide is not clear about each of these terms’ purposes. So there is a lot of confusion on how to capture requirements for a product or application. Different companies and individuals have different interpretations, so we should not force a hierarchy in a context where it doesn’t fit. In this post, you’ll find out what is the difference between epics, features and user stories.


**Requirements have certain characteristics, such as size, the moment they emerge, or the level of detail. Epics, Features, and User Stories all have their role in different phases of the project life cycle. I will explain the difference between them and how I apply them in which phase of the project.** 


![Increment VS Release](https://scrumdistrict.com/wp-content/uploads/2021/05/Features-3.png)Increment VS Release
But before, I should clarify one aspect about increments and releases, some terms that I will use later on.


At the end of each sprint, we create a potentially shippable product increment. A release is a piece of working software that is made available to users in a production environment. It’s not required for every product increment to be released at the end of the sprint we produced it in.


## What are Epics


An Epic is a large body of work that spans across releases. They are high-level bullet points of functionality, usually having a business case that supports them. We create Epics early in the project life cycle and the Scrum Team will break them down into smaller pieces of work, called User Stories.


Epics can also span across several teams. If there are multiple sizeable areas that it has to cover, Scrum Teams can split these areas among them. Or, in some companies, different Scrum Teams manage certain components that are present in the requirement. Here, they cover that part of the functionality that is under their responsibility.


Well-written Epics provide a good understanding and help avoid misunderstandings during development. We can define them in the same way as the User Stories: As a < type of user> I want <goal>, so that <reason>. And, they are placeholders for a required feature that describes the final output of users’ needs.


![](https://scrumdistrict.com/wp-content/uploads/2021/05/EPIC-VS-FEATURE-VS-EPIC-1.png)
## **The basic structure of an Epic includes:**


**Introduction**


The Epic introduction should contain the “what” and “why”. What feature are you going to build and why are you building it?


**Product requirement**


Here you provide the details for the entire development team to understand what they are going to build. It should list the functionality that is desired.


**Technical and design requirements**


In this phase, involve the UX designer and the developers and collaborate with them as much as you can. Their inputs in the early stage are so valuable to build the functionality correctly.


## **Applying the Epic structure**


**Summary** 


As a customer, I want to have a shopping cart so that I can buy products online


**Introduction** 


More and more customers prefer to order products online. This functionality will allow customers to place orders faster. It will bring new customers that prefer online orders over placing orders by phone.


**Product requirement**


Users can add products to the shopping cart


Users can select the quantity for each product


Users can remove products from the shopping cart


Users can pay by Credit Card


Users can get a refund if they return the product to the same CC they paid with


**Design and technical requirements**


The shopping cart should have pagination when the list exceeds 10 unique items


An indicator that shows the shopping cart is loading will be displayed to the user


Create an auto-delete system to remove items that have been in the shopping cart for over 24 hours


## What is a Feature


Defining Features is a common practice in the Scaled Agile Framework, where they should fit in a Program. But does this mean we cannot use Features in Scrum? Not at all. We use them to manage big product functionalities, that will deliver significant benefits when released to users.


Features group together User Stories. You can think about them as a collection of related User Stories or simple tags. Features provide business value and are sizable. Therefore, they must have enough details for the Scrum team to size it.


Features span across sprints but they should fit in a single release. It means that we should finish a feature in a maximum of 2-3 months. They should be small enough to fit in a couple of sprints, and in case they are not, the Scrum Team should split them down further.


In order to be acceptable to the client, a feature must pass a set of tests, therefore, it has to be testable.


![](https://scrumdistrict.com/wp-content/uploads/2021/05/EPIC-VS-FEATURE-VS-EPIC-2.png)
## Elements that help us define a Feature


**Business hypothesis** 


It represents the “why” behind the reason this feature is needed, and what benefits this functionality will bring to its users.


**Business value**


To evaluate the business value, consider the number of users that will use the functionality, how much will they use it, the urgency of releasing the feature, the ROI, the development effort, and the competition.


**Description**


The description focuses on “what” will be implemented and the problem that this feature is going to solve. So it should describe the context in which users will make use of the functionality.


**Acceptance criteria**


Not knowing the conditions in which a feature can be marked as done is a problem because you cannot measure the progress. They are the same as the acceptance criteria for User Stories, and we should write them exactly the same.


## Now, let’s write a Feature


**Business hypothesis** 


The Product Manager noticed that the business can grow if online payments are available. The reasoning behind this is that customers prefer having more control during their purchase journey. For two weeks, the operators asked the customers they were in contact with if they would order more often if they had access to an online shopping cart.


**Business value**


At this moment, customers are placing orders by phone. The number of operators that are processing these calls is limited. Therefore, they are not answering 40% of these calls. 20% of the customers that don’t get an answer never try to make an order again. This feature will increase our sales by 45%. We’ll gain 20% from the missed orders, and having this additional feature will bring us 25% more new customers.


**Description**


Shopping cart – These include all the functionality necessary to implement the shopping cart, such as adding and removing products from the shopping cart


Payment options – These include all the functionality necessary to implement the shopping cart, such as


**Acceptance criteria**


Given I am a customer looking to buy a product,


When I want to place an order,


Then I have the option to add products to the shopping cart.


Given I am a customer adding products to the shopping cart,


When I want to place the order,


Then I have the option to pay by credit card.


## One more step, create the User Story


User Stories reflect the business needs. They clearly state what should the developers implement and have enough details for them to be well understood. They are smaller chunks of work that should fit one sprint. The developers should make sure that every User Story they include in the Sprint Backlog has the right size so they can deliver a potentially shippable increment at the end. If it’s not small enough, the developers should split it further until it has a proper size.


We can write a User Story following the INVEST criteria, which is great because it allows you to create small and complete enough pieces of work, to deliver them in one sprint.


They have a relevant title/summary, an appropriate description of what we should implement, and acceptance criteria which are mandatory for a good User Story.


We split them from Epics but can also be standalone stories that are not generated by the need for a large piece of work. In relationship with Features, we group the related User Stories under the same Feature. If you are interested in more details about how to structure user stories, you can find more information **[here](https://scrumdistrict.com/is-there-a-right-way-to-write-user-stories/)**.


![difference between epics and user stories](https://scrumdistrict.com/wp-content/uploads/2021/05/EPIC-VS-FEATURE-VS-EPIC-3.png)difference between epics and user stories
## Defining the User Story


**Summary**


As a customer, I want to add multiple products to the shopping cart, so that I can buy them all at once – we will group this story under the Shopping cart Feature described previously.


**Description**


The customers will have the possibility to check out the products available on our website and add each one of them to the shopping cart


As soon as they click “Add” they can see the product in the Shopping cart


**Acceptance criteria**


Given I am a customer trying to purchase products from the website,


When I add a product to the shopping cart,


Then I can immediately check the shopping cart and see the product.


**Other User Stories that may result** 


As a customer, I want to remove products one by one from the shopping cart so that I don’t start adding the products all over again when I change my mind


As a customer, I want to get a refund on my credit card, so that I can track the transaction


As a customer, I want to pay with Visa so that I can use my existing credit card


You may see others placing the Features before Epics, or using Themes to include Epics and completely remove Features. That’s not wrong, it’s just another approach.


Do you have questions about how to define requirements following this structure? Do you have any best practices that you’d like to share? Leave a comment below.