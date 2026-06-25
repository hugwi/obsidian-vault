---
categories:
  - "[[Resources]]"
domain: engineering
title: "Is There A Right Way To Write User Stories"
source: "https://scrumdistrict.com/is-there-a-right-way-to-write-user-stories/"
author: "Scrum Master"
published: 2021-04-27
created: 2025-12-16
description: "A user story must always reflect a business need, they are structured as"
tags:
  - to-process
  - startup-business
---

A user story must always reflect a business need, they are structured as system behavior functional descriptions. Of course, some user stories will generate adjacent tasks that are more technical oriented, that aim attention on non-functional system support. We won’t be focusing on the non-functional description here, but if you are new to this, it’s important to know that they exist.


**User stories should clearly state from the title what has to be achieved**. T**he description has to contain all the necessary information and the acceptance criteria should not be missing. In addition, it’s essential for a user story to be created to fit in only one sprint.**


A poor written user story can affect the way that functionality is understood and developed. You might end up having lots of missing parts or getting something different of what you’ve imagined the result will be. Pay attention to anything that might create confusion and try to simplify the content.


## Write great user stories following the INVEST criteria


The reason why many follow the INVEST criteria is that it allows you to create stories that can be delivered in only one sprint.


**Independent** – User stories should not depend on one another. They should allow developers to implement them in any sequence and, making changes to one of the stories must not affect others.


**N****egotiable** – The development team decides **how** they will implement the story. The Product Owner should be open to suggestions coming from the team.


**Valuable** – User stories deliver value to the business and end-users.


**Estimable** – It’s easy to estimate how much time the development of a User story will take.


**S****mall** – It should be small enough to go through the entire cycle (designing, coding, testing) during one sprint.


**Testable** – Have clear acceptance criteria to check if the team has implemented the feature as the PO envisions.


## How to format your user story


**Use the Vertical Slicing technique.** Imagine you have a cake with multiple layers of frosting. You can slice the cake vertically and you’ll get a bit from each layer in one slice, or slice it horizontally and you’ll have a big slice but only one layer of frosting.


Now let’s think a bit about what functionality can consist of. The Development Team implements the User Interface. They will create and configure the Database Interface, Security layers, there will maybe be some API calls needed, and the list can continue.


Using the **Vertical Slicing** technique, you will think of the user story from a business perspective. That is, the Development Team will implement a small section of the User Interface, Database Interface, Security, and API calls, that is just enough for the required piece of functionality to work.


On the other hand, the **Horizontal Slicing** technique approaches the requirement from a technical point of view. Meaning that, the Development Team will first create and configure the Database Interface, then they will take care of the API calls, Security and at the end, they will implement the User Interface.


The difference between these two techniques is that with **Vertical Slicing**, you can ship early working functionality. While with the **Horizontal Slicing** technique, you’ll have to wait for each layer to be finalized before delivering the feature.


A good user story structure contains the following details:


#### 1. Summary/Title


As a [user] I want [some feature] so that [some reason]


**As a [user]** – This should not be something generic as any [user]. Be as specific as you can and make sure it’s very clear to you, who you are addressing. It can be someone inside your company who will use it or someone external, as a customer. Add the exact role of that person who will benefit from the feature.


 **I want [some feature]** – Think about the intention of the user working with that feature. Want does he want to achieve? Instead of writing “I want to manage my bank account”, you can say something like, “I want to transfer money from account X to account Y”.


Also, it’s very important to have one intention per user story. If the intention sounds something like “I want to transfer money from account X to account Y and see the transaction details in a report”, you should split it into two separate stories.


**So That [some reason] –** What is the value this story will bring to the end-user? “I want to transfer money from account X to account Y so that I can save money into my Savings account”. Each story has to have a reason why you want to implement it for. And everyone must understand the value that it will bring. If there is no value, then you probably should not spend your time on it.


#### 2. Description


**This section should describe the flow that users will go through when using the feature.** It should not contain any UI or UX details. These details will be described separately in tools like [Zeplin](https://zeplin.io/). Remember that in scrum we don’t want to create exhaustive documentation, our focus is on communication.


By reading this description, the Development Team should understand how will this feature end up being used. Don’t leave important information aside. Just make sure that you don’t create stories that no one will want to read because they are too long. Also, don’t write any implementation details, the “how” is the Development Team’s job to figure out.


#### 3. Acceptance Criteria


**These are the conditions that a software product must meet to be validated by the end-user, or another system**. It’s a guideline for the team to understand when the functionality is complete and does what’s expected.


You’ll find scenario-oriented (Given/When/Then) rule-oriented (checklist) and many other custom formats of Acceptance Criteria. I personally used to write AC based on the rule-oriented type, it was just easier for my scenarios but each one works best with different stories.


**Scenario-oriented example:** 


As an online backing account user, I want to reset my password, so that I can log in to my account if I forget it


**Scenario**: Forgot password


**Given**: The user goes to the login page


**When**: The user clicks the Forgot Password button


**And**: Enters the email address associated with his bank account to receive the reset link


**Then**: The system sends the reset link to the entered email address


**Rule-oriented example:**


As an online backing account user, I want to reset my password, so that I can log in to my account if I forget it


* A blue Reset Button appears below the User/Password input fields
* When clicked, an email field appears and the Send button is active
* The system send the reset link to that email


No matter you are creating functional or non-functional stories, make sure that you hand over an accurate information to the Development Team. It’s not unusual to ask the team help you with some of the stories. This could be a good exercise for them. And also will make them feel more involved by being part in the process.


I hope this information will be helpful in the following user stories that you’ll create. If you have any other tips and you want to share them, please leave a comment a below.