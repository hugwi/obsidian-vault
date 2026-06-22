---
title: "What is the difference between the Facade and Adapter Pattern?"
source: "https://stackoverflow.com/questions/2961307/what-is-the-difference-between-the-facade-and-adapter-pattern"
author: "Stack Overflow"
published: 2022-11-07
created: 2025-12-08
description: "I''ve been reading both definitions and they seem quite the same."
tags:
  - to-process
  - software-architecture
---

The [Facade Pattern](http://en.wikipedia.org/wiki/Facade_pattern) wiki page has a brief note about this.



>  "An Adapter is used when the wrapper must respect a particular interface and must support a polymorphic behavior. On the other hand, a facade is used when one wants an easier or simpler interface to work with."
> 
>  


I heard an analogy that you should think of your universal remote control that you've set up to work with all your different stereo systems - you press "on" and it turns on your cable box, your receiver, and your TV. Maybe it's a really fancy home theater and it dims the lights and draws the shades too. That's a Facade - one button/function that takes care of a more complicated set of steps.


The Adapter pattern just links two incompatible interfaces.


**EDIT:** A quick analogy for the Adapter pattern (based on the comments) might be something like a DVI-to-VGA adapter. Modern video cards are often DVI, but you've got an old VGA monitor. With an adapter that plugs into your video card's expected DVI input, and has its own VGA input, you'll be able to get your old monitor working with your new video card.