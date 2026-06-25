---
categories:
  - "[[Resources]]"
domain: engineering
title: "Adapter and Facade Patterns"
source: "https://medium.com/@BobGuBobGu/adapter-and-facade-patterns-8b05e00a29a3"
author: "Robert Gu"
published: 2016-04-15
created: 2025-12-08
description: "I have a friend(I know yes I have at least one friend, crazy huh?) that works"
tags:
  - to-process
  - software-architecture
---

I have a friend(I know yes I have at least one friend, crazy huh?) that works at a digital marketing agency, she works longs hours, does a lot with social media content and the other day had to count the amount of hashtags for a certain keyword by hand!


The snarky, nerdy, programming voice in my head said “mehhh why hasn’t someone built something that can use the Instagram API to count the hash tags for her”.


Building applications that rely on external third party APIs is something that almost every developer has to deal with. Incredibly powerful companies are built on the backs of these social media giant’s APIs.


The adapter pattern is commonly used when we want to make sure that our application can use these third party APIs correctly. More simply put Adapter pattern is used when we have two classes that need to talk to each other but currently have no way of doing so. The adapter will convert the interface of the API into an interface that our application can use.


## Get Robert Gu’s stories in your inbox


Join Medium for free to get updates from this writer.


Lets take a simple example. I want to build an application that retrieves the number of posts from Instagram, and tweets from twitter based off of a certain hashtag. I’ve adopted this code below that is a part of this application.


Some content could not be imported from the original document. [View content ↗](https://medium.com/@BobGuBobGu/adapter-and-facade-patterns-8b05e00a29a3) 


Our application is trying to make use of these interfaces to get posts and tweets from Instagram and Twitter. These could be libraries we need to use such as a JAR file.


Some content could not be imported from the original document. [View content ↗](https://medium.com/@BobGuBobGu/adapter-and-facade-patterns-8b05e00a29a3) 


To create an adapter we are going to wrap these interfaces, with our Social Media Content interface. That way our application can now use the social media interface to make use of the Instagram and Twitter APIs. Here is an adapter for Instagram.


Some content could not be imported from the original document. [View content ↗](https://medium.com/@BobGuBobGu/adapter-and-facade-patterns-8b05e00a29a3) 


Sweet now our application can talk to these external APIs, two things we are missing are classes that implement the InstagramAPI interface, and the social media content interface, once we have those, we are all wired up.


Some content could not be imported from the original document. [View content ↗](https://medium.com/@BobGuBobGu/adapter-and-facade-patterns-8b05e00a29a3) 


Some content could not be imported from the original document. [View content ↗](https://medium.com/@BobGuBobGu/adapter-and-facade-patterns-8b05e00a29a3) 


Wow this is a lot of code, lets do a quick step by step again.


1. We have a client interface(social media content), we use this to wrap the interface we want to use(twitter, Instagram), this is known as the **adapter**.
2. The **adaptee** is the thing getting adapted which is the Instagram and twitter interface.
3. The **client** is the class interacting with the social media content interface, which we are specifying which social media network we want to find content by a specific hashtag.


### Facade Pattern


Great now we have this tool to get posts from certain social media sites by a hashtag. As a marketer in charge of a social media campaign, they probably would also want the number of media content by a certain keyword across all social networks. They could individually find the amount of media content and add them up by hand, or we could use the facade patten to do that for them.


Facade pattern will allow users of our application to call methods that have more overarching and general functionality to them. Methods on this facade might include, finding the actual posts by keyword, finding other related keywords, number of likes related to a keyword. All these methods would be across all social media networks.


Also the good thing about facade is the user does not have to go through it to retrieve data, it has the option of using it, hence the name facade or false front. This allows users to still get data relevant to specific social networks.


Some content could not be imported from the original document. [View content ↗](https://medium.com/@BobGuBobGu/adapter-and-facade-patterns-8b05e00a29a3) 


Sweet this number of content method will now retrieve all the content across the sites we our tracking. Facade uses an interface to talk to a group of interfaces, and leverages their functionality to create more general overarching functionality.


Both adapter and facade patterns provide us with a lot of modularity and allows are application to be more isolated from any changes third party APIs may make. When you think “isolating yourself from changes to APIs” the adapter pattern might come in handy.