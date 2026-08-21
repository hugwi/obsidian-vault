---
categories:
  - "[[Clippings]]"
domain: [software-engineering]
tags:
  - ddd
  - patterns
source: readwise
created: 2026-06-23
rating: 
action: 
---

# What is the difference between the Facade and Adapter Pattern?

![rw-book-cover](https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded)

## Metadata
- Author: [[Stack Overflow]]
- Full Title: What is the difference between the Facade and Adapter Pattern?
- Category: #articles
- Summary: A Facade gives a simpler, higher-level interface to a complex system. An Adapter makes one interface compatible with another so they can work together. Think: Facade = one remote button doing many tasks; Adapter = plug that lets old hardware connect to new ports.
- URL: https://stackoverflow.com/questions/2961307/what-is-the-difference-between-the-facade-and-adapter-pattern

## Full Document
The [Facade Pattern](http://en.wikipedia.org/wiki/Facade_pattern) wiki page has a brief note about this.

>  "An Adapter is used when the wrapper must respect a particular interface and must support a polymorphic behavior. On the other hand, a facade is used when one wants an easier or simpler interface to work with."
> 
>  

I heard an analogy that you should think of your universal remote control that you've set up to work with all your different stereo systems - you press "on" and it turns on your cable box, your receiver, and your TV. Maybe it's a really fancy home theater and it dims the lights and draws the shades too. That's a Facade - one button/function that takes care of a more complicated set of steps.

The Adapter pattern just links two incompatible interfaces.

**EDIT:** A quick analogy for the Adapter pattern (based on the comments) might be something like a DVI-to-VGA adapter. Modern video cards are often DVI, but you've got an old VGA monitor. With an adapter that plugs into your video card's expected DVI input, and has its own VGA input, you'll be able to get your old monitor working with your new video card.
