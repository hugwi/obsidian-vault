---
categories:
  - "[[Resources]]"
domain: engineering
title: "Scrapling: The Web Scraper That Repairs Itself"
source: "https://www.youtube.com/watch?v=q-uj7wk0LRI"
author: "Better Stack"
published: 2026-06-03
created: 2026-06-05
description: "In this video, I test Scrapling, the adaptive Python web scraping framework\"
tags:
  - to-process
  - agent-tools
---

This is Scrapling, a Python scraper that tries to fix the worst part of web scraping. The scraper works today, then breaks the second the site changes. One renamed class, one moved div, one bot check, and now your data pipeline is dead. Scrapling's whole claim is that your scraper can adapt instead of falling apart. It has over 53,000 stars on GitHub. It supports adaptive parsing, stealth fetching, and bigger crawler workflows. I'm going to test the one question that actually matters. Can it 

survive a website change without rewriting selectors? Well, we're about to find out. So, what is Scrapling? Scrapling is an adaptive all-in-one Python web scraping framework. You get a self-healing parser, stealth fetchers, browser-based fetching when JavaScript is needed, and a spider framework for bigger crawls. One install, one API. That means fewer broken scrapers and more usable data that we get back. Now, let's see the 

part that actually matters. If you enjoy coding tools that speed up your workflow, be sure to subscribe. We have videos coming out all the time. Now, here I have a basic setup, right? I've already installed Scrapling, so we'll keep this part fast. One import and one call is all we need to get the page. Up top here, I made some HTML that changes. One is like a generic starting site, then I kept the same thing, but I switched the CSS selectors. Let's say I want the product name and price. Now, 

normally, I might grab them with CSS selectors, right? So, page CSS, I drop in my selector, auto save true. I can do that, and it's going to work, and we're going to get a dictionary of data back to us. Looks normal, two selectors, a dictionary, I move on. That's it. But, at the same time, that's actually the problem, because a normal scraper works great until that page changes. Now, what happens if the site randomly changes overnight? They redesign it, they do something to prevent this. So, product 

title becomes item heading or product price becomes pricing value. It's got the same data on the page, but the entire DOM changes. The old selectors should be dead, and this is where most scrapers are just going to break. But now, we can turn on adaptive mode. One change, auto save equals true becomes adaptive equals true. So, now I can still put product title with adaptive set to true. Same data, I 

didn't change the selectors. It's different page structure without the selector rewrite. That's the main idea here. Now, when you scrape an element with auto save true, Scrappling records clues about it. So, it's going to record things like the tag, attributes, parents and children, any neighboring text, probably the DOM position, and the structural shape. So, when a class name changes, Scrappling has more clues left. It doesn't need the entire site to stay the same. It only needs enough structural signal to recognize the element again. And that's the part that 

matters, because real scraper failures are almost never a total redesign. It's a renamed class, a new wrapper, a shifted layout, one tiny thing. That's exactly what adaptive matching is built for. Scrappling has three big pieces that actually matter. The first is adaptive parser, what you just saw. Then there's multiple fetcher, one workflow, right tool for the job. The fetcher goes for plain HTTP, fast for simple web pages. Stealthy fetcher can bypass antibots when needed. Dynamic fetcher is 

real browser for JS heavy sites. One API, swap the fetcher, keep the code. The spider framework is when quick scripts turn into a real crawler. Async crawling, pause and resume, proxy rotations, streaming, and all those mixed sessions. The stuff you usually add on later, it's already there. Scrappling isn't just another parser. It replaces the scraping stack. Requests, beautiful soup, playwright, retry logic, proxy helpers, spider code with one 

workflow. Scrappling is not saying beautiful soup is useless and it's not saying playwright or Scrapy is dead. Beautiful soup plus requests is still great for simple pages. It's easy, it's readable, and everyone understands it. But it does not give you any type of stealth. It does not give you adaptive selectors, and it does not render JavaScript. And for larger parsing jobs, it can become the actual bottleneck. Now, Scrapy is powerful. If you are 

building serious crawling infrastructure, Scrapy still deserves some respect. But Scrapy often means settings, pipelines, middleware, extensions, and a lot more setup. Playwright and Selenium are great when you need a real browser. Sometimes the page just needs JavaScript. There's no way around that. But browsers are heavy. They are slower than raw HTTP, and they use more memory. And again, they still don't fix the issue of broken selectors. They run the page. They don't understand what your scraper meant to extract. So 

with Scrappling, you can use fast fetching when you can, stealth when you need it, use browser rendering when the page requires it, and use adaptive parsing so one small front-end change doesn't blow everything up. Now, all this doesn't mean Scrappling doesn't have issues, right? If you're dealing with data DOM level protection, advanced fingerprinting, or aggressive rate limits, you may still need good proxies. So, Scrappling can help, but it doesn't make you invisible. Dynamic fetching can also mean extra browser setup. That's just the tradeoff when JavaScript 

rendering is involved. Here's some food for thought for all of this. Scrappling is worth trying if you do real scraping work, especially if you're building data pipelines, you have rag jobs, AI agents, or anything that needs to keep running after the target site changes. The strongest reason to use it is not that it makes scraping possible. We already have tools that can actually do that, right? The strongest reason is that it reduces maintenance. Now, I'd probably just skip it if you have a really tiny 

script, right? Requests and Beautiful Soup are going to do the trick, right? If you enjoy coding tools like this, be sure to subscribe to the Better Stack channel. We'll see you in another video. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 This is Scrapling, a Python scraper that
 </span>
 <span data-rw-start="3.08" data-rw-transcript-version="2">
 tries to fix the worst part of web
 </span>
 <span data-rw-start="5.16" data-rw-transcript-version="2">
 scraping. The scraper works today, then
 </span>
 <span data-rw-start="7.44" data-rw-transcript-version="2">
 breaks the second the site changes. One
 </span>
 <span data-rw-start="9.88" data-rw-transcript-version="2">
 renamed class, one moved div, one bot
 </span>
 <span data-rw-start="13.04" data-rw-transcript-version="2">
 check, and now your data pipeline is
 </span>
 <span data-rw-start="15.24" data-rw-transcript-version="2">
 dead. Scrapling's whole claim is that
 </span>
 <span data-rw-start="17.4" data-rw-transcript-version="2">
 your scraper can adapt instead of
 </span>
 <span data-rw-start="19.4" data-rw-transcript-version="2">
 falling apart. It has over 53,000 stars
 </span>
 <span data-rw-start="22.24" data-rw-transcript-version="2">
 on GitHub.
 </span>
</p>
<p>
 <span data-rw-start="24.88" data-rw-transcript-version="2">
 It supports adaptive parsing,
 </span>
 <span data-rw-start="27.04" data-rw-transcript-version="2">
 stealth fetching, and bigger crawler
 </span>
 <span data-rw-start="29.04" data-rw-transcript-version="2">
 workflows. I'm going to test the one
 </span>
 <span data-rw-start="31.12" data-rw-transcript-version="2">
 question that actually matters. Can it
 </span>
 <span data-rw-start="32.759" data-rw-transcript-version="2">
 survive a website change without
 </span>
 <span data-rw-start="34.8" data-rw-transcript-version="2">
 rewriting selectors? Well, we're about
 </span>
 <span data-rw-start="40.56" data-rw-transcript-version="2">
 to find out.
 </span>
</p>
<p>
 <span data-rw-start="40.56" data-rw-transcript-version="2">
 So, what is Scrapling? Scrapling is an
 </span>
 <span data-rw-start="42.84" data-rw-transcript-version="2">
 adaptive all-in-one Python web scraping
 </span>
 <span data-rw-start="45.56" data-rw-transcript-version="2">
 framework. You get a self-healing
 </span>
 <span data-rw-start="47.68" data-rw-transcript-version="2">
 parser, stealth fetchers, browser-based
 </span>
 <span data-rw-start="50.2" data-rw-transcript-version="2">
 fetching when JavaScript is needed, and
 </span>
 <span data-rw-start="52.12" data-rw-transcript-version="2">
 a spider framework for bigger crawls.
 </span>
 <span data-rw-start="54.48" data-rw-transcript-version="2">
 One install, one API. That means fewer
 </span>
 <span data-rw-start="57.52" data-rw-transcript-version="2">
 broken scrapers and more usable data
 </span>
 <span data-rw-start="59.56" data-rw-transcript-version="2">
 that we get back. Now, let's see the
 </span>
 <span data-rw-start="61.6" data-rw-transcript-version="2">
 Part that actually matters. If you enjoy
 </span>
 <span data-rw-start="63.76" data-rw-transcript-version="2">
 coding tools that speed up your
 </span>
 <span data-rw-start="64.96" data-rw-transcript-version="2">
 workflow, be sure to subscribe. We have
 </span>
 <span data-rw-start="66.88" data-rw-transcript-version="2">
 videos coming out all the time. Now,
 </span>
 <span data-rw-start="69.12" data-rw-transcript-version="2">
 here I have a basic setup, right? I've
 </span>
 <span data-rw-start="71.36" data-rw-transcript-version="2">
 already installed Scrapling, so we'll
 </span>
 <span data-rw-start="73.4" data-rw-transcript-version="2">
 keep this part fast. One import and one
 </span>
 <span data-rw-start="76.2" data-rw-transcript-version="2">
 call is all we need to get the page. Up
 </span>
 <span data-rw-start="78.84" data-rw-transcript-version="2">
 top here, I made some HTML that changes.
 </span>
</p>
<p>
 <span data-rw-start="81.76" data-rw-transcript-version="2">
 One is like a generic starting site,
 </span>
 <span data-rw-start="83.56" data-rw-transcript-version="2">
 then I kept the same thing, but I
 </span>
 <span data-rw-start="85.32" data-rw-transcript-version="2">
 switched the CSS selectors. Let's say I
 </span>
 <span data-rw-start="88.52" data-rw-transcript-version="2">
 want the product name and price. Now,
 </span>
 <span data-rw-start="91.04" data-rw-transcript-version="2">
 normally, I might grab them with CSS
 </span>
 <span data-rw-start="93.68" data-rw-transcript-version="2">
 selectors, right? So, page CSS, I drop
 </span>
 <span data-rw-start="96.72" data-rw-transcript-version="2">
 in my selector, auto save true. I can do
 </span>
 <span data-rw-start="99.32" data-rw-transcript-version="2">
 that, and it's going to work, and we're
 </span>
 <span data-rw-start="100.56" data-rw-transcript-version="2">
 going to get a dictionary of data back
 </span>
 <span data-rw-start="102.6" data-rw-transcript-version="2">
 to us. Looks normal, two selectors, a
 </span>
 <span data-rw-start="105.4" data-rw-transcript-version="2">
 dictionary, I move on. That's it. But,
 </span>
 <span data-rw-start="107.88" data-rw-transcript-version="2">
 at the same time, that's actually the
 </span>
 <span data-rw-start="109.56" data-rw-transcript-version="2">
 problem, because a normal scraper works
 </span>
 <span data-rw-start="112.08" data-rw-transcript-version="2">
 great until that page changes. Now, what
 </span>
 <span data-rw-start="115.04" data-rw-transcript-version="2">
 happens if the site randomly changes
 </span>
 <span data-rw-start="117.04" data-rw-transcript-version="2">
 overnight? They redesign it, they do
 </span>
 <span data-rw-start="118.72" data-rw-transcript-version="2">
 Something to prevent this. So, product
 </span>
 <span data-rw-start="121.12" data-rw-transcript-version="2">
 title becomes item heading
 </span>
 <span data-rw-start="123.6" data-rw-transcript-version="2">
 or product price becomes pricing value.
 </span>
</p>
<p>
 <span data-rw-start="126.16" data-rw-transcript-version="2">
 It's got the same data on the page, but
 </span>
 <span data-rw-start="128.2" data-rw-transcript-version="2">
 the entire DOM changes. The old
 </span>
 <span data-rw-start="130.759" data-rw-transcript-version="2">
 selectors should be dead, and this is
 </span>
 <span data-rw-start="132.56" data-rw-transcript-version="2">
 where most scrapers are just going to
 </span>
 <span data-rw-start="134.08" data-rw-transcript-version="2">
 break. But now, we can turn on adaptive
 </span>
 <span data-rw-start="137.24" data-rw-transcript-version="2">
 mode. One change, auto-save equals true
 </span>
 <span data-rw-start="140.4" data-rw-transcript-version="2">
 becomes adaptive equals true. So, now I
 </span>
 <span data-rw-start="144.52" data-rw-transcript-version="2">
 can still put product title with
 </span>
 <span data-rw-start="146.72" data-rw-transcript-version="2">
 adaptive set to true. Same data, I
 </span>
 <span data-rw-start="150.16" data-rw-transcript-version="2">
 didn't change the selectors. It's
 </span>
 <span data-rw-start="152.16" data-rw-transcript-version="2">
 different page structure without the
 </span>
 <span data-rw-start="154.28" data-rw-transcript-version="2">
 selector rewrite. That's the main idea
 </span>
 <span data-rw-start="156.959" data-rw-transcript-version="2">
 here. Now, when you scrape an element
 </span>
 <span data-rw-start="158.84" data-rw-transcript-version="2">
 with auto save true, Scrappling records
 </span>
 <span data-rw-start="161.08" data-rw-transcript-version="2">
 clues about it. So, it's going to record
 </span>
 <span data-rw-start="162.76" data-rw-transcript-version="2">
 things like the tag, attributes, parents
 </span>
 <span data-rw-start="164.88" data-rw-transcript-version="2">
 and children, any neighboring text,
 </span>
 <span data-rw-start="167.04" data-rw-transcript-version="2">
 probably the DOM position, and the
 </span>
 <span data-rw-start="168.8" data-rw-transcript-version="2">
 structural shape. So, when a class name
 </span>
 <span data-rw-start="171.12" data-rw-transcript-version="2">
 changes, Scrappling has more clues left.
 </span>
</p>
<p>
 <span data-rw-start="173.88" data-rw-transcript-version="2">
 It doesn't need the entire site to stay
 </span>
 <span data-rw-start="175.8" data-rw-transcript-version="2">
 the same. It only needs enough
 </span>
 <span data-rw-start="177.6" data-rw-transcript-version="2">
 Structural signal to recognize the
 </span>
 <span data-rw-start="179.56" data-rw-transcript-version="2">
 element again. And that's the part that
 </span>
 <span data-rw-start="181.48" data-rw-transcript-version="2">
 matters, because real scraper failures
 </span>
 <span data-rw-start="183.48" data-rw-transcript-version="2">
 are almost never a total redesign. It's
 </span>
 <span data-rw-start="185.959" data-rw-transcript-version="2">
 a renamed class, a new wrapper, a
 </span>
 <span data-rw-start="187.84" data-rw-transcript-version="2">
 shifted layout, one tiny thing. That's
 </span>
 <span data-rw-start="190.28" data-rw-transcript-version="2">
 exactly what adaptive matching is built
 </span>
 <span data-rw-start="192.6" data-rw-transcript-version="2">
 for. Scrapping has three big pieces
 </span>
 <span data-rw-start="195.04" data-rw-transcript-version="2">
 that actually matter. The first is
 </span>
 <span data-rw-start="196.519" data-rw-transcript-version="2">
 adaptive parser, what you just saw. Then
 </span>
 <span data-rw-start="198.92" data-rw-transcript-version="2">
 there's multiple fetcher, one workflow,
 </span>
 <span data-rw-start="201.4" data-rw-transcript-version="2">
 right tool for the job. The fetcher goes
 </span>
 <span data-rw-start="203.959" data-rw-transcript-version="2">
 for plain HTTP, fast for simple web
 </span>
 <span data-rw-start="207" data-rw-transcript-version="2">
 pages. Stealthy fetcher can bypass
 </span>
 <span data-rw-start="209.72" data-rw-transcript-version="2">
 antibots when needed. Dynamic fetcher is
 </span>
 <span data-rw-start="212.12" data-rw-transcript-version="2">
 real browser for JS-heavy sites. One
 </span>
 <span data-rw-start="214.68" data-rw-transcript-version="2">
 API, swap the fetcher, keep the code.
 </span>
</p>
<p>
 <span data-rw-start="217.4" data-rw-transcript-version="2">
 The spider framework is when quick
 </span>
 <span data-rw-start="219.88" data-rw-transcript-version="2">
 scripts turn into a real crawler. Async
 </span>
 <span data-rw-start="222.8" data-rw-transcript-version="2">
 crawling, pause and resume, proxy
 </span>
 <span data-rw-start="224.68" data-rw-transcript-version="2">
 rotations, streaming, and all those
 </span>
 <span data-rw-start="226.92" data-rw-transcript-version="2">
 mixed sessions. The stuff you usually
 </span>
 <span data-rw-start="229.48" data-rw-transcript-version="2">
 add on later, it's already there.
 </span>
 <span data-rw-start="231.64" data-rw-transcript-version="2">
 Scrappling isn't just another parser. It
 </span>
 <span data-rw-start="234.08" data-rw-transcript-version="2">
 replaces the scraping stack. Requests,
 </span>
 <span data-rw-start="236.88" data-rw-transcript-version="2">
 Beautiful soup, playwright, retry logic,
 </span>
 <span data-rw-start="239.4" data-rw-transcript-version="2">
 proxy helpers, spider code with one
 </span>
 <span data-rw-start="242" data-rw-transcript-version="2">
 workflow. Scrappling is not saying
 </span>
 <span data-rw-start="243.96" data-rw-transcript-version="2">
 beautiful soup is useless and it's not
 </span>
 <span data-rw-start="245.96" data-rw-transcript-version="2">
 saying playwright or Scrapy is dead.
 </span>
</p>
<p>
 <span data-rw-start="248.64" data-rw-transcript-version="2">
 Beautiful soup plus requests is still
 </span>
 <span data-rw-start="250.959" data-rw-transcript-version="2">
 great for simple pages. It's easy, it's
 </span>
 <span data-rw-start="253.52" data-rw-transcript-version="2">
 readable, and everyone understands it.
 </span>
 <span data-rw-start="255.88" data-rw-transcript-version="2">
 But it does not give you any type of
 </span>
 <span data-rw-start="258.56" data-rw-transcript-version="2">
 stealth. It does not give you adaptive
 </span>
 <span data-rw-start="261.2" data-rw-transcript-version="2">
 selectors, and it does not render
 </span>
 <span data-rw-start="263.6" data-rw-transcript-version="2">
 JavaScript. And for larger parsing jobs,
 </span>
 <span data-rw-start="266.08" data-rw-transcript-version="2">
 it can become the actual bottleneck.
 </span>
</p>
<p>
 <span data-rw-start="268.04" data-rw-transcript-version="2">
 Now, Scrapy is powerful. If you are
 </span>
 <span data-rw-start="270.4" data-rw-transcript-version="2">
 building serious crawling
 </span>
 <span data-rw-start="271.36" data-rw-transcript-version="2">
 infrastructure, Scrapy still deserves
 </span>
 <span data-rw-start="273.12" data-rw-transcript-version="2">
 some respect. But Scrapy often means
 </span>
 <span data-rw-start="275.44" data-rw-transcript-version="2">
 settings, pipelines, middleware,
 </span>
 <span data-rw-start="276.84" data-rw-transcript-version="2">
 extensions, and a lot more setup.
 </span>
 <span data-rw-start="278.84" data-rw-transcript-version="2">
 Playwright and Selenium are great when
 </span>
 <span data-rw-start="281.16" data-rw-transcript-version="2">
 you need a real browser. Sometimes the
 </span>
 <span data-rw-start="283.64" data-rw-transcript-version="2">
 page just needs JavaScript. There's no
 </span>
 <span data-rw-start="285.76" data-rw-transcript-version="2">
 way around that. But browsers are heavy.
 </span>
 <span data-rw-start="288.16" data-rw-transcript-version="2">
 They are slower than raw HTTP, and they
 </span>
 <span data-rw-start="290.919" data-rw-transcript-version="2">
 use more memory. And again, they still
 </span>
 <span data-rw-start="293.4" data-rw-transcript-version="2">
 Don't fix the issue of broken selectors.
 </span>
</p>
<p>
 <span data-rw-start="295.96" data-rw-transcript-version="2">
 They run the page. They don't understand
 </span>
 <span data-rw-start="298.12" data-rw-transcript-version="2">
 what your scraper meant to extract.
 </span>
 <span data-rw-start="300.2" data-rw-transcript-version="2">
 So, with Scrappling, you can use fast
 </span>
 <span data-rw-start="302.2" data-rw-transcript-version="2">
 fetching when you can, stealth when you
 </span>
 <span data-rw-start="304.2" data-rw-transcript-version="2">
 need it, use browser rendering when the
 </span>
 <span data-rw-start="306.12" data-rw-transcript-version="2">
 page requires it, and use adaptive
 </span>
 <span data-rw-start="308.48" data-rw-transcript-version="2">
 parsing so one small front-end change
 </span>
 <span data-rw-start="310.6" data-rw-transcript-version="2">
 doesn't blow everything up. Now, all
 </span>
 <span data-rw-start="312.76" data-rw-transcript-version="2">
 this doesn't mean Scrappling doesn't
 </span>
 <span data-rw-start="314.2" data-rw-transcript-version="2">
 have issues, right? If you're dealing
 </span>
 <span data-rw-start="315.88" data-rw-transcript-version="2">
 with data DOM level protection, advanced
 </span>
 <span data-rw-start="318.04" data-rw-transcript-version="2">
 fingerprinting, or aggressive rate
 </span>
 <span data-rw-start="319.84" data-rw-transcript-version="2">
 limits, you may still need good proxies.
 </span>
</p>
<p>
 <span data-rw-start="322.56" data-rw-transcript-version="2">
 So, Scrappling can help, but it doesn't
 </span>
 <span data-rw-start="324.919" data-rw-transcript-version="2">
 make you invisible. Dynamic fetching can
 </span>
 <span data-rw-start="327.2" data-rw-transcript-version="2">
 also mean extra browser setup. That's
 </span>
 <span data-rw-start="329.72" data-rw-transcript-version="2">
 just the tradeoff when JavaScript
 </span>
 <span data-rw-start="331.36" data-rw-transcript-version="2">
 rendering is involved. Here's some food
 </span>
 <span data-rw-start="333.68" data-rw-transcript-version="2">
 for thought for all of this. Scrappling
 </span>
 <span data-rw-start="335.36" data-rw-transcript-version="2">
 is worth trying if you do real scraping
 </span>
 <span data-rw-start="337.88" data-rw-transcript-version="2">
 work, especially if you're building data
 </span>
 <span data-rw-start="340.56" data-rw-transcript-version="2">
 pipelines, you have rag jobs, AI agents,
 </span>
 <span data-rw-start="343.4" data-rw-transcript-version="2">
 or anything that needs to keep running
 </span>
 <span data-rw-start="345.64" data-rw-transcript-version="2">
 after the target site changes. The
 </span>
 <span data-rw-start="347.68" data-rw-transcript-version="2">
 The strongest reason to use it is not that
 </span>
 <span data-rw-start="349.68" data-rw-transcript-version="2">
 it makes scraping possible. We already
 </span>
 <span data-rw-start="351.8" data-rw-transcript-version="2">
 have tools that can actually do that,
 </span>
 <span data-rw-start="354.32" data-rw-transcript-version="2">
 right? The strongest reason is that it
 </span>
 <span data-rw-start="356.08" data-rw-transcript-version="2">
 reduces maintenance. Now, I'd probably
 </span>
 <span data-rw-start="358.92" data-rw-transcript-version="2">
 just skip it if you have a really tiny
 </span>
 <span data-rw-start="360.72" data-rw-transcript-version="2">
 script, right? Requests and Beautiful
 </span>
 <span data-rw-start="362.48" data-rw-transcript-version="2">
 Soup are going to do the trick, right?
 </span>
</p>
<p>
 <span data-rw-start="365.08" data-rw-transcript-version="2">
 If you enjoy coding tools like this, be
 </span>
 <span data-rw-start="366.88" data-rw-transcript-version="2">
 sure to subscribe to the Better Stack
 </span>
 <span data-rw-start="368.24" data-rw-transcript-version="2">
 channel. We'll see you in another video.
 </span>
</p>