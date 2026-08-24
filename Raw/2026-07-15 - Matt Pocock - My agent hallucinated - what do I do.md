---
title: "My agent hallucinated - what do I do?"
source: youtube
url: https://www.youtube.com/watch?v=H-JHumbpORI
author: "Matt Pocock"
published: 2026-07-15
created: 2026-08-24
duration: "0:01:32"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# My agent hallucinated - what do I do?

![My agent hallucinated - what do I do?](https://www.youtube.com/embed/H-JHumbpORI)

## Description

Learn how to identify and fix LLM hallucinations in your code. Discover the difference between factuality and faithfulness hallucinations, and master techniques to keep your AI agents reliable and accurate.

https://www.aicodingdictionary.com/?term=attention-degradation

Keep up to date with my skills here:

https://aihero.dev/s/cUQ4x1

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://aihero.dev/s/WiIvRE

## Transcript

hallucinations. They're going to happen. They're probably inherent to LLMs. So, how do you avoid them and how do you diagnose? Well, let's say you have some kind of coding hallucination and what you first need to say is was the information available to the LLM in its context window. People think that LLMs are kind of like databases where they store information and retrieve, but that's absolutely not right. It's more like they have a fuzzy JPEG of the entirety of human knowledge. And so, they know the basic shapes of things, but they can't really tell you specifics. And so, you have to basically say was the information in context? If it's not, then it's a factuality hallucination. A factuality hallucination is when it's attempting to read something that you haven't passed it and it just fails. It cannot recall things. You should never trust an unsourced LLM. So, the fix there is obvious. You just load the information into context. However, even if you pass the agent the right context, it's not always going to work. And so, you will get a faithfulness hallucination where it's not been faithful to the information that you provided. Now, this can sometimes happen because of attention degradation where the context window grows longer and longer and the attention relationships get strained between all the elements. So, the way to get the agent out of that is to reduce the number of tokens in its context window. So, you reduce the number of attention relationships and it can focus better. When you're deep in the context window and there's lots of attention degradation, I call that the dumb zone. So, the cure for faithfulness is to somehow get out of the dumb zone. That might be clearing the context, that might be running compact, that might be handing off to a separate session. Hallucinations are here to stay and so, you need to know how to deal with them.
