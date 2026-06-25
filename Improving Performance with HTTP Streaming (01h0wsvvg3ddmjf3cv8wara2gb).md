---
categories:
  - "[[Resources]]"
domain: engineering
title: "Improving Performance with HTTP Streaming"
source: "https://medium.com/airbnb-engineering/improving-performance-with-http-streaming-ba9e72c66408"
author: "Victor"
published: 2023-05-17
created: 2023-05-20
description: "How HTTP Streaming can improve page performance and how Airbnb enabled it"
tags:
  - to-process
  - dev-tools
---

How HTTP Streaming can improve page performance and how Airbnb enabled it on an existing codebase


**By:** [Victor Lin](https://www.linkedin.com/in/victorhlin/)


![](https://miro.medium.com/v2/resize:fit:700/1*q2A2ZjnULygCKIWuiSBKXg.jpeg)
# Introduction


You may have heard a joke that the [Internet is a series of tubes](https://en.wikipedia.org/wiki/Series_of_tubes). In this blog post, we’re going to talk about how we get a cool, refreshing stream of Airbnb.com bytes into your browser as quickly as possible using HTTP Streaming.


Let’s first understand what streaming means. Imagine we had a spigot and two options:


* Fill a big cup, and then pour it all down the tube (the “buffered” strategy)
* Connect the spigot directly to the tube (the “streaming” strategy)


In the buffered strategy, everything happens sequentially — our servers first generate the entire response into a buffer (filling the cup), and then more time is spent sending it over the network (pouring it down). The streaming strategy happens in parallel. We break the response into chunks, which are sent as soon as they are ready. The server can start working on the next chunk while previous chunks are still being sent, and the client (e.g, a browser) can begin handling the response before it has been fully received.


# Implementing Streaming at Airbnb


Streaming has clear advantages, but most websites today still rely on a buffered approach to generate responses. One reason for this is the additional engineering effort required to break the page into independent chunks. This just isn’t feasible sometimes. For example, if all of the content on the page relies on a slow backend query, then we won’t be able to send anything until that query finishes.


However, there’s one use case that’s universally applicable. We can use streaming to reduce **network waterfalls**. This term refers to when one network request triggers another, resulting in a cascading series of sequential requests. This is easily visualized in a tool like Chrome’s [Waterfall](https://developer.chrome.com/docs/devtools/network/reference/#waterfall):


![](https://miro.medium.com/v2/resize:fit:700/1*qhOyK4HxTnhImOTPhSA4DQ.png)Chrome Network Waterfall illustrating a cascade of sequential requests 
Most web pages rely on external JavaScript and CSS files linked within the HTML, resulting in a network waterfall — downloading the HTML triggers JavaScript and CSS downloads. As a result, it’s a best practice to place all CSS and JavaScript tags near the beginning of the HTML in the `<head>` tag. This ensures that the browser sees them earlier. With streaming, we can reduce this delay further, by sending that portion of the `<head>` tag first.


# Early Flush


The most straightforward way to send an early `<head>` tag is by breaking a standard response into two parts. This technique is called **Early Flush**, as one part is sent (“flushed”) before the other.


The first part contains things that are fast to compute and can be sent quickly. At Airbnb, we include tags for fonts, CSS, and JavaScript, so that we get the browser benefits mentioned above. The second part contains the rest of the page, including content that relies on API or database queries to compute. The end result looks like this:


Early chunk:



```
<html>  
  <head>  
    <script src=… defer />  
    <link rel=”stylesheet” href=… />  
    <!--lots of other <meta> and other tags… ->
```

Late chunk:



```
<!-- <head> tags that depend on data go here ->  
  </head>  
  <body>  
    <! — Body content here →  
  </body>  
</html>
```

We had to restructure our app to make this possible. For context, Airbnb uses an Express-based NodeJS server to render web pages using React. We previously had a single React component in charge of rendering the complete HTML document. However, this presented two problems:


* Producing incremental chunks of content means we need to work with partial/unclosed HTML tags. For example, the examples you saw above are invalid HTML. The `<html>` and `<head>` tags are opened in the Early chunk, but closed in the Late chunk. There’s no way to generate this sort of output using the standard React rendering functions.
* We can’t render this component until we have all of the data for it.


We solved these problems by breaking our monolithic component into three:


* an “Early <head>” component
* a “Late <head>” component, for <head> tags that depend on data
* a “<body>” component


Each component renders the *contents* of the head or body tag. Then we stitch them together by writing open/close tags directly to the HTTP response stream. Overall, the process looks like this:


1. Write `<html><head>`
2. Render and write the Early <head> to the response
3. Wait for data
4. Render and write the Late <head> to the response
5. Write `</head><body>`
6. Render and write the <body> to the response
7. Finish up by writing `</body></html>`


# Data Streaming


Early Flush optimizes CSS and JavaScript network waterfalls. However, users will still be staring at a blank page until the `<body>` tag arrives. We’d like to improve this by rendering a loading state when there’s no data, which gets replaced once the data arrives. Conveniently, we already have loading states in this situation for client side routing, so we could accomplish this by just rendering the app without waiting for data!


Unfortunately, this causes another network waterfall. Browsers have to receive the SSR (Server-Side Render), and then JavaScript triggers another network request to fetch the actual data:


![](https://miro.medium.com/v2/resize:fit:700/1*6kTkLA-UnBm5UGayU0WAcw.png)Graph showing a network waterfall where SSR and client-side data fetch happen sequentially 
In our testing, this resulted in a slower *total* loading time.


What if we could include this data in the HTML? This would allow our server-side rendering and data fetching to happen in parallel:


![](https://miro.medium.com/v2/resize:fit:700/1*AKzOqc2Nd6BcrV-1LZbfxA.png)Graph showing SSR and client-side data fetch happening in parallel 
Given that we had already broken the page into two chunks with Early Flush, it’s relatively straightforward to introduce a third chunk for what we call **Deferred Data**. This chunk goes after all of the visible content and does not block rendering. We execute the network requests on the server and stream the responses into the Deferred Data chunk. In the end, our three chunks look like this:


Early chunk



```
<html>  
  <head>  
    <link rel=”preload” as=”script” href=… />  
    <link rel=”stylesheet” href=… />  
    <! — lots of other <meta> and other tags… →
```

Body chunk



```
    <! — <head> tags that depend on data go here →  
  </head>  
  <body>  
     <! — Body content here →  
     <script src=… />
```

Deferred Data chunk



```
    <script type=”application/json” >  
      <!-- data -->  
    </script>   
  </body>  
</html>
```

With this implemented on the server, the only remaining task is to write some JavaScript to detect when our Deferred Data chunk arrives. We did this with a [MutationObserver](https://developer.mozilla.org/en-US/docs/Web/API/MutationObserver), which is an efficient way to observe DOM changes. Once the Deferred Data JSON element is detected, we parse the result and inject it into our application’s network data store. From the application’s perspective, it’s as though a normal network request has been completed.


**Watch out for `defer`**


You may notice that some tags are re-ordered from the Early Flush example. The script tags moved from the Early chunk to the Body chunk and no longer have the [defer attribute](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script#attributes). This attribute avoids render-blocking script execution by deferring scripts until after the HTML has been downloaded and parsed. This is suboptimal when using Deferred Data, as all of the visible content has already been received by the end of the Body chunk, and we no longer worry about render-blocking at that point. We can fix this by moving the script tags to the end of the Body chunk, and removing the defer attribute. Moving the tags later in the document does introduce a network waterfall, which we solved by adding [preload](https://developer.mozilla.org/en-US/docs/Web/HTML/Attributes/rel/preload) tags into the Early chunk.


# Implementation Challenges


# Status codes and headers


Early Flush prevents subsequent changes to the headers (e.g to redirect or change the status code). In the React + NodeJS world, it’s common to delegate redirects and error throwing to a React app rendered after the data has been fetched. This won’t work if you’ve already sent an early `<head>` tag and a 200 OK status.


We solved this problem by moving error and redirect logic out of our React app. That logic is now performed in [Express server middleware](https://expressjs.com/en/guide/using-middleware.html) before we attempt to Early Flush.


# Buffering


We found that [nginx](https://www.nginx.com/resources/wiki/start/topics/examples/x-accel/#x-accel-buffering) buffer responses by default. This has resource utilization benefits but is counterproductive when the goal is sending incremental responses. We had to configure these services to disable buffering. We expected a potential increase in resource usage with this change but found the impact to be negligible.


# Response delays


We noticed that our Early Flush responses had an unexpected delay of around 200ms, which disappeared when we disabled gzip compression. This turned out to be an interaction between [Nagle’s algorithm](https://en.wikipedia.org/wiki/Nagle%27s_algorithm) and [Delayed ACK](https://en.wikipedia.org/wiki/TCP_delayed_acknowledgment). These optimizations attempt to maximize data sent per packet, introducing latency when sending small amounts of data. It’s especially easy to run into this issue with [jumbo frames](https://en.wikipedia.org/wiki/Jumbo_frame), which increases maximum packet sizes. It turns out that gzip reduced the size of our writes to the point where they couldn’t fill a packet, and the solution was to disable Nagle’s algorithm in our [haproxy](https://www.haproxy.com/documentation/hapee/latest/onepage/#4.2-option%20http-no-delay) load balancer.


# Conclusion


HTTP Streaming has been a very successful strategy for improving web performance at Airbnb. Our experiments showed that Early Flush produced a flat reduction in [First Contentful Paint](https://web.dev/fcp/) (FCP) of around 100ms on every page tested, including the Airbnb homepage. Data streaming further eliminated the FCP costs of slow backend queries. While there were challenges along the way, we found that adapting our existing React application to support streaming was very feasible and robust, despite not being designed for it originally. We’re also excited to see the broader frontend ecosystem trend in the direction of prioritizing streaming, from [@defer and @stream in GraphQL](https://graphql.org/blog/2020-12-08-improving-latency-with-defer-and-stream-directives/) to [streaming SSR in Next.js](https://nextjs.org/docs/advanced-features/react-18/streaming). Whether you’re using these new technologies, or extending an existing codebase, we hope you’ll explore streaming to build a faster frontend for all!


If this type of work interests you, check out some of our related positions [here](https://careers.airbnb.com/).


# Acknowledgments


Elliott Sprehn, Aditya Punjani, Jason Jian, Changgeng Li, Siyuan Zhou, Bruce Paul, Max Sadrieh, and everyone else who helped design and implement streaming at Airbnb!


# \*\*\*\*\*\*\*\*\*\*\*\*\*\*\*\*


*All product names, logos, and brands are property of their respective owners. All company, product and service names used in this website are for identification purposes only. Use of these names, logos, and brands does not imply endorsement.*