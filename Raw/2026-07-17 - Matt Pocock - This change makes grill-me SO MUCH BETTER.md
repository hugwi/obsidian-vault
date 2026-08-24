---
title: "This change makes /grill-me SO MUCH BETTER"
source: "youtube"
url: "https://www.youtube.com/watch?v=tLyfDIt9wHg"
author: "Matt Pocock"
published: "2026-07-17"
created: "2026-08-24"
duration: "0:02:05"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "context-engineering"
  - "skills"
summary: "Yeah, I'm pretty sure that in the next version of my skills, uh Grill Me is going to change significantly and it's going to grill or instead of grilling one question at a time, it's going to grill in batches. Grill Me had this really weird failure mode where when you got to the end of a grilling session, it would basically just ask you a bunch of questions in a row that were all yeses. Yes, I agree with your recommendation."
---

# This change makes /grill-me SO MUCH BETTER

![This change makes /grill-me SO MUCH BETTER](https://www.youtube.com/embed/tLyfDIt9wHg)

## Description

Exploring /grill-me new batch-based question system. Learn how Matt is improving the skill by asking questions in rounds instead of one-by-one, reducing wait times and context switching while handling question dependencies.

Keep up to date with my skills here:

https://aihero.dev/s/Pt7OWW

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://aihero.dev/s/zXq81f

## Transcript

Yeah, I'm pretty sure that in the next version of my skills, uh Grill Me is going to change significantly and it's going to grill or instead of grilling one question at a time, it's going to grill in batches. Grill Me had this really weird failure mode where when you got to the end of a grilling session, it would basically just ask you a bunch of questions in a row that were all yeses. Yes, I agree with your recommendation. Agree, agree, agree. And that's just so wasteful in terms of time because you have to wait, send a model provider request up, wait for it to come back, and then only then can you ask the question. This is especially stupid for me because I use dictation all the time and so I can just dictate out a bunch of answers to loads of questions if I see them on screen. And so loads of people were modifying Grill Me just to say, "Okay, ask me all the questions at once instead of one by one to get around this." But if you ask them all at once, then you have an issue which is that questions have dependencies between them. The answer of one question might depend on the answer of another. And one by one gets around that by just asking them in sequence and you just have a discussion. And so I've managed to find a perfect middle ground here where it asks you rounds of questions. So this is Q1 in the first round, Q2 in the first round, Q3 in the first round, Q4 in the first round. And then I can just reply to all of those questions and then round two takes the answers that I've given in the previous round and then asks the next follow-up. This is about as concurrent as I can get it, I think. So Q4 in round two, Q5, Q6 all in round two. Yeah, all of those three in there. Now this does mean when you answer a grilling session, you're going to have to do a little bit more reading just to understand each question in turn, but it is faster and it means that you actually have less context switching if you're doing multiple of these in parallel. So I think in the next version of my skills, I'm going to be changing Grill Me to do this instead of the previous round because it seems to solve a big issue with Grill Me and make the whole thing faster. If you don't like this, of course, then you can just modify your global claw.md or modify the skill itself to use the old version. But, I've been trying this all week, and I really, really like it. So, why not give it to you?
