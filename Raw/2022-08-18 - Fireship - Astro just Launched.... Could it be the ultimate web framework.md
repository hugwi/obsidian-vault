---
title: "Astro just Launched.... Could it be the ultimate web framework?"
source: "youtube"
url: "https://www.youtube.com/watch?v=gxBkghlglTg"
author: "Fireship"
published: "2022-08-18"
created: "2026-08-24"
duration: "0:03:17"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "video-gen"
  - "web-design"
summary: "it is august 18 2022 and you're watching the code report one of the most difficult decisions of a front-end developer's life is choosing between front-end ui frameworks because once you get jumped into a gang it's really hard to get out but what if there is a way you could be a part of multiple gangs at one time without causing a bunch of complex drama well that's just one of the amazing things that astro does which is a tool for building multi-page applications that just hit version 1.0 a few days ago i made 100 second video about it a while ago but it has some really interesting new features and deserves a second look at a very high level it's kind of like a static site generator that allows you to write content and markdown using the file system for routing then renders it all as a static multi-page application for templating it has its own language called astro components which feel very nice and familiar to the modern front end developer what's really interesting though is that you can bring in your favorite front-end framework like react spelt vue and so on and it will render the ui on the server while shipping zero javascript to the browser javascript is the main bottleneck for performance which means with astro you get really fast page loads while using your favorite javascript framework or multiple frameworks at the same time but you might be wondering how does a component work if it doesn't have its javascript with it the answer is it doesn't it's just static html by default however if you do need interactivity and state you can opt into javascript as needed to add islands of interactivity to your website from a developer's perspective astro provides a variety of directives that determine when to hydrate or load the javascript for a component if you want to load it right away like normal use client load but if you don't need the component to be interactive right away you can also use idle to wait until the browser is just chilling or visible to wait until the component comes into the viewport under the hood astro is using a technique called partial or selective hydration to render components in place as opposed to taking over the entire dom that's a huge deal when it comes to performance less javascript to run means faster page loads and better time to interactive scores that's awesome but astro can do many things beyond the typical static site generator like next.js it can statically generate dynamic routes by allowing you to define a git static paths function however if you don't want to pre-render all your pages it can also handle full server-side rendering that means your pages will be generated at request time and it's also possible to have dedicated api routes but with full ssr it needs to be deployed to a server and can run on node.js or the edge using platforms like cloudflare netlife or cell and so on now as much as i love astro if you watch my recent video the one limitation i ran into is that it's not possible out of the box to do client-side routing it's different from something like nexjs that does full hydration where the client-side router takes over after the initial page load with astro you get an entirely new page for each navigation that could be an issue if you plan on sharing data or state between route changes however i discovered there is a project called astro spa that addresses this exact issue although it's not yet a stable part of the framework i also made a meme framework to help with this and shout out to everybody who's contributed to make that library better if astro does get the ability to work like a single page application at some point it would really become the ultimate framework because it would cover every single use case on this flowchart and not only that but you could use any ui framework you want at that point it could put an end to the great javascript framework wars and we could go back to building apps and peace and harmony when these rich companies wage javascript framework war it's us poor developers who die this has been the code report thanks for watching and i will see you in the next one"
---

# Astro just Launched.... Could it be the ultimate web framework?

![Astro just Launched.... Could it be the ultimate web framework?](https://www.youtube.com/embed/gxBkghlglTg)

## Description

Astro version 1.0 just launched giving developers a way to build server-rendered websites with any JavaScript framework. It uses the islands architecture and partial hydration to deliver fast apps with frameworks like React, Vue, Svelte, and more. 

#programming #javascript #TheCodeReport

🔗 Resources

- Astro Launch Blog https://astro.build/blog/astro-1/
- Astro on GitHub https://github.com/withastro/astro
- I built a JS framework https://youtu.be/SJeBRW1QQMA
- Astro in 100 Seconds https://youtu.be/dsTXcSeAZq8

🔥 Get More Content - Upgrade to PRO

Upgrade to Fireship PRO at https://fireship.io/pro
Use code lORhwXd2 for 25% off your first payment. 

🎨 My Editor Settings

- Atom One Dark 
- vscode-icons
- Fira Code Font

🔖 Topics Covered

- What is Astro.js?
- Is Astro a good framework?
- Pros and cons of using Astro
- How build a fast website
- Top web development frameworks
- Best JS frameworks in 2022
- JS framework drama

## Transcript

it is august 18 2022 and you're watching the code report one of the most difficult decisions of a front-end developer's life is choosing between front-end ui frameworks because once you get jumped into a gang it's really hard to get out but what if there is a way you could be a part of multiple gangs at one time without causing a bunch of complex drama well that's just one of the amazing things that astro does which is a tool for building multi-page applications that just hit version 1.0 a few days ago i made 100 second video about it a while ago but it has some really interesting new features and deserves a second look at a very high level it's kind of like a static site generator that allows you to write content and markdown using the file system for routing then renders it all as a static multi-page application for templating it has its own language called astro components which feel very nice and familiar to the modern front end developer what's really interesting though is that you can bring in your favorite front-end framework like react spelt vue and so on and it will render the ui on the server while shipping zero javascript to the browser javascript is the main bottleneck for performance which means with astro you get really fast page loads while using your favorite javascript framework or multiple frameworks at the same time but you might be wondering how does a component work if it doesn't have its javascript with it the answer is it doesn't it's just static html by default however if you do need interactivity and state you can opt into javascript as needed to add islands of interactivity to your website from a developer's perspective astro provides a variety of directives that determine when to hydrate or load the javascript for a component if you want to load it right away like normal use client load but if you don't need the component to be interactive right away you can also use idle to wait until the browser is just chilling or visible to wait until the component comes into the viewport under the hood astro is using a technique called partial or selective hydration to render components in place as opposed to taking over the entire dom that's a huge deal when it comes to performance less javascript to run means faster page loads and better time to interactive scores that's awesome but astro can do many things beyond the typical static site generator like next.js it can statically generate dynamic routes by allowing you to define a git static paths function however if you don't want to pre-render all your pages it can also handle full server-side rendering that means your pages will be generated at request time and it's also possible to have dedicated api routes but with full ssr it needs to be deployed to a server and can run on node.js or the edge using platforms like cloudflare netlife or cell and so on now as much as i love astro if you watch my recent video the one limitation i ran into is that it's not possible out of the box to do client-side routing it's different from something like nexjs that does full hydration where the client-side router takes over after the initial page load with astro you get an entirely new page for each navigation that could be an issue if you plan on sharing data or state between route changes however i discovered there is a project called astro spa that addresses this exact issue although it's not yet a stable part of the framework i also made a meme framework to help with this and shout out to everybody who's contributed to make that library better if astro does get the ability to work like a single page application at some point it would really become the ultimate framework because it would cover every single use case on this flowchart and not only that but you could use any ui framework you want at that point it could put an end to the great javascript framework wars and we could go back to building apps and peace and harmony when these rich companies wage javascript framework war it's us poor developers who die this has been the code report thanks for watching and i will see you in the next one
