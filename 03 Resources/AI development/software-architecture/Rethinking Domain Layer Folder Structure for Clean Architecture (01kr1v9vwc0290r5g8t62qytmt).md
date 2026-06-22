---
title: "Rethinking Domain Layer Folder Structure for Clean Architecture"
source: "https://www.linkedin.com/posts/milan-jovanovic_the-domain-layer-folder-structure-should-activity-7410220758771167232-l14B?utm_source=share&utm_medium=member_android&rcm=ACoAACDYSKgBNrQFbnZBbm-5p711lB6NBjpcBXA"
author: "Milan Jovanović"
published: 
created: 2026-05-07
description: "The Domain layer folder structure should express intent."
tags:
  - to-process
  - software-architecture
---

  Sign up for the .NET Weekly with 75K+ other engineers, and get a free Clean Architecture
  template: https://lnkd.in/edzd2tK5 | 40 comments on LinkedIn'
---

[Milan Jovanović](https://rs.linkedin.com/in/milan-jovanovic?trk=public_post_feed-actor-name)  


The Domain layer folder structure should express intent.


I didn't understand this until a few years ago.


The Domain sits at the core of Clean Architecture.


It's where you define your entities and the most important business logic.


So, I want to share a situation I ran into recently.


I was looking at a project I built many years ago.


The folder structure in the Domain layer bothered me.


I was focusing on technical concerns instead of features.


The symptoms of this are folders with names like:


- Entities  

- Enumerations  

- Exceptions  

- Repositories  

- ValueObjects


I'm sure you've done (or seen) this at some point.


What's the problem with grouping by type?


This folder structure doesn't tell you anything about the Domain.


It also has low cohesion. The types inside a folder aren't related.


So what did I do?


I reorganized the folders so that related concepts are in the same folder.


The benefits of this approach are:


- Improved cohesion  

- High coupling within one folder  

- Low coupling between unrelated folders


When you apply this on an application level, you end up with Vertical Slice Architecture.


Here's why this is so valuable: [https://lnkd.in/dPq9u8S4](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2FdPq9u8S4&urlhash=gZzG&trk=public_post-text)


What do you think about this approach?


---  

Sign up for the .NET Weekly with 75K+ other engineers, and get a free Clean Architecture template: [https://lnkd.in/edzd2tK5](https://www.linkedin.com/redir/redirect?url=https%3A%2F%2Flnkd%2Ein%2Fedzd2tK5&urlhash=VV6g&trk=public_post-text)


* ![text](https://media.licdn.com/dms/image/v2/D4D22AQFlRQj7SGf8bw/feedshare-shrink_800/B4DZtZkX0bKAAg-/0/1766734268001?e=2147483647&v=beta&t=UcFQZWFwCUFV0sQTWpHHdmMISEiYAu_-LKvaKSdgrAM)