---
title: "You HAVE to know this TypeScript pattern"
source: youtube
url: https://www.youtube.com/watch?v=HDaPLwZWguo
author: "Matt Pocock"
published: 2025-06-13
created: 2026-08-24
duration: "0:01:45"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# You HAVE to know this TypeScript pattern

![You HAVE to know this TypeScript pattern](https://www.youtube.com/embed/HDaPLwZWguo)

## Description

Become a TypeScript Wizard with my TypeScript course:

https://www.totaltypescript.com

Follow Matt on Twitter

https://twitter.com/mattpocockuk

Join the Discord:

https://mattpocock.com/discord

## Transcript

is a TypeScript pattern you absolutely have to know about. Let's imagine we have an interface here called state where we have a status property, an error property, and a data property. We can use this setup to model several different states our application can be in. For instance, a status of loading or if I replace this a status with error, and we still have this error. We could potentially use this in a front-end application to model the state of a data fetch, for instance. However, I would consider this type to be incorrect to the point of being dangerous because it allows you to model states that should not exist. For instance, we can just remove this error here. And now our application will show as having errored, but we won't know why because we don't have the error on it. Or for instance, we might be in a loading state, but still showing the error that we had before. In other words, instead of three different states, there are actually a combinatorial explosion of a bunch of possible states here. So instead of this interface, I'm going to replace this with a special type here. This type is a union of three objects that all have the status property. loading doesn't have any extra properties. Status success has the data and status error has the error. This is what's called a discriminated union where this thing here, the status is the discriminant. In other words, it's the thing that tells us which branch of this union we're in. Now, instead of about a dozen possible states, we now only have three. We're getting an error here saying the error does not exist in type status loading. Let's remove that to fix the error. But if instead we're modeling the success case here, then it's now going to yell at us until we include the data which is currently missing. So discriminated unions are amazing for modeling data that can only be in one of a few possible shapes. And you'll know you'll need one if you notice that you have a state object with a bunch of optionals here. Thanks for joining along and I'll see you in the next
