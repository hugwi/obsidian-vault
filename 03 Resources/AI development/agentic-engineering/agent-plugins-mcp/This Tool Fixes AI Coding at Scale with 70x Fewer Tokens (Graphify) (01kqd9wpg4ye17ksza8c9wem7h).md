---
title: "This Tool Fixes AI Coding at Scale with 70x Fewer Tokens (Graphify)"
source: "https://www.youtube.com/watch?v=WNru_PFycT8"
author: "Better Stack"
published: 2026-04-29
created: 2026-04-29
description: "If you’re using AI coding tools like Claude Code or Cursor on anything bigger\"
tags:
  - to-process
  - agent-plugins-mcp
---

This might be one of the most insane ways to bring your code base to life. If you're using Claude code or cursor on a real project, you'd think the hard part is writing code. Well, it's not. The hard part is just understanding your own repo. You ask one question and your AI is burning through your tokens just to figure out what's going on. It's slow, it's expensive, and half the time still wrong. What if instead of sending your whole project every time, you gave the AI a map of it? That's exactly what Graphy does. And it can cut token usage 

by over 70%. Let me show you how all this works. Right now, your AI sees your project like this, just a pile of files. There's no real connections, there's no structure, there's no memory. So, every time you ask a question, it has to relearn everything from scratch. That's why answers feel close, but not quite right. And yeah, this is exactly what Carpathy pointed out when the raw folder 

problem. Graphy showed up right after that. It's more of a memory layer. If you enjoy coding tools and tips like this, be sure to subscribe. We have videos coming out all the time. All right, now let me show you. I've got a small repo here, code, docs, and diagram. Now, normally I'd have to explain all this to AI every time. Instead, I run one command, Graphy, right here. Give it a second. Now, look at this. After Claude executes Graphy, this isn't just files anymore, it's an 

actual graph. Everything is connected. I can click and dissect actually what's going on and what is linked together to just here within the HTML file that it generated. Then, instead of asking AI to read everything again, I can now ask it, "What connects off to the API layer?" And now it answers using relationships, using the MD file that it generated with this call. It's not guesses, it's relationships. And here's the part that surprised me. Before this, around 14,000 

tokens, okay, however many were used. After this, after it executes the first time, we drop that down to maybe a couple hundred. Same question, completely different cost. All because of this generated map. So, what is this actually doing? Graphy is basically like Google Maps for your code base. Instead of raw text, you get nodes and connections. Under it all, it uses tree-sitters to understand the structure, then an LLM to extract the 

meaning. Then, it can group everything into clusters and it's not just code. It reads PDFs, diagrams, even audio and video. All locally, nothing leaves the machine. What you get from this is simple. We get a visual graph, a written report, and a knowledge base we can actually explore. This visual graph is huge for a lot of us as we can see how things connect. Now, here's where this changes how AI coding usually works. Most tools use rag, which basically 

means find similar chunks of text. Well, Graphy doesn't do that. It builds real relationships. This function calls that one. This module depends on that. This idea came from this document. And it even tells you how confident it is. So, instead of this looks related, we get something like this is actually connected in an actual visual representation of what is connected. And the biggest difference here, it remembers too since it generated us that MD file, it can look back on. We're not 

starting from zero every time. It updates only what's changed, so your AI finally has context that sticks. All right, now I actually thought all this was pretty sweet. But what are the good and the bad things here? And now, first up to the plate, the efficiency compounds. Every question gets cheaper, and because it connects code, docs, diagrams, you start finding relationships you didn't even know existed. That's huge for onboarding for these messy projects that we get dumped into. That's great. Now, the drawbacks 

to all this are this. The first run can be slow and cost tokens, especially with a lot of documents. After that, it's cached, but yeah, that first hit is real. It's also early, so long-term support is still unknown. And small thing, when you install this, it's Graphy with two Ys, not one. So, check your spelling on that. The relationships aren't always perfect, but it labels them clearly, extracted, inferred, and biguous, so you know what you can actually trust. And if your repo is 

tiny, this is going to be somewhat of an overkill. So, is it worth it? I mean, yeah, if you're using AI on anything real, this is cool. It's I thought it was worth it. Because your biggest problem isn't running the code, it's actually understanding it across files, across time, across context. And that's exactly what this fixes. The token savings alone make it worth trying, but the bigger win is this. Your AI stops guessing and starts reasoning. If you're working solo, doing research, or have all these big systems, this is a serious 

upgrade. If you're just working on smaller scripts, this is probably just an overkill, so you don't really need to try it. But most have to try this, this is going to be an awesome tool. If you enjoy coding tools and tips to speed up your workflow, be sure to subscribe to the Better Stack channel. We'll see you in another video. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 This might be one of the most insane
 </span>
 <span data-rw-start="2.04" data-rw-transcript-version="2">
 ways to bring your code base to life. If
 </span>
 <span data-rw-start="4.56" data-rw-transcript-version="2">
 you're using Claude code or cursor on a
 </span>
 <span data-rw-start="6.56" data-rw-transcript-version="2">
 real project, you'd think the hard part
 </span>
 <span data-rw-start="8.64" data-rw-transcript-version="2">
 is writing code. Well, it's not. The
 </span>
 <span data-rw-start="11.24" data-rw-transcript-version="2">
 hard part is just understanding your own
 </span>
 <span data-rw-start="13.28" data-rw-transcript-version="2">
 repo. You ask one question, and your AI
 </span>
 <span data-rw-start="15.92" data-rw-transcript-version="2">
 is burning through your tokens just to
 </span>
 <span data-rw-start="17.56" data-rw-transcript-version="2">
 figure out what's going on. It's slow,
 </span>
 <span data-rw-start="19.56" data-rw-transcript-version="2">
 it's expensive, and half the time, still
 </span>
 <span data-rw-start="22.04" data-rw-transcript-version="2">
 wrong. What if instead of sending your
 </span>
 <span data-rw-start="23.92" data-rw-transcript-version="2">
 whole project every time, you gave the
 </span>
 <span data-rw-start="26.32" data-rw-transcript-version="2">
 AI a map of it? That's exactly what
 </span>
 <span data-rw-start="28.48" data-rw-transcript-version="2">
 Graphy does. And it can cut token usage
 </span>
 <span data-rw-start="31.12" data-rw-transcript-version="2">
 by over 70%. Let me show you how all
 </span>
 <span data-rw-start="33.92" data-rw-transcript-version="2">
 this works.
 </span>
</p>
<p>
 <span data-rw-start="39.84" data-rw-transcript-version="2">
 Right now, your AI sees your project
 </span>
 <span data-rw-start="41.88" data-rw-transcript-version="2">
 like this, just a pile of files. There's
 </span>
 <span data-rw-start="45.16" data-rw-transcript-version="2">
 no real connections, there's no
 </span>
 <span data-rw-start="46.72" data-rw-transcript-version="2">
 structure, there's no memory. So, every
 </span>
 <span data-rw-start="49.2" data-rw-transcript-version="2">
 time you ask a question, it has to
 </span>
 <span data-rw-start="51.36" data-rw-transcript-version="2">
 relearn everything from scratch. That's
 </span>
 <span data-rw-start="53.56" data-rw-transcript-version="2">
 why answers feel close, but not quite
 </span>
 <span data-rw-start="55.96" data-rw-transcript-version="2">
 right. And yeah, this is exactly what
 </span>
 <span data-rw-start="58.48" data-rw-transcript-version="2">
 Carpathy pointed out when the raw folder
 </span>
 <span data-rw-start="60.88" data-rw-transcript-version="2">
 Problem. Graphy showed up right after
 </span>
 <span data-rw-start="63.44" data-rw-transcript-version="2">
 that. It's more of a memory layer. If
 </span>
 <span data-rw-start="66.28" data-rw-transcript-version="2">
 you enjoy coding tools and tips like
 </span>
 <span data-rw-start="67.8" data-rw-transcript-version="2">
 this, be sure to subscribe. We have
 </span>
 <span data-rw-start="69.56" data-rw-transcript-version="2">
 videos coming out all the time. All
 </span>
 <span data-rw-start="71.72" data-rw-transcript-version="2">
 right now, let me show you. I've got a
 </span>
 <span data-rw-start="73.56" data-rw-transcript-version="2">
 small repo here, code, docs, and
 </span>
 <span data-rw-start="76.12" data-rw-transcript-version="2">
 diagram. Now, normally I'd have to
 </span>
 <span data-rw-start="78.24" data-rw-transcript-version="2">
 explain all this to AI every time.
 </span>
</p>
<p>
 <span data-rw-start="80.92" data-rw-transcript-version="2">
 Instead, I run one command, Graphy,
 </span>
 <span data-rw-start="84.12" data-rw-transcript-version="2">
 right here. Give it a second. Now, look
 </span>
 <span data-rw-start="87.08" data-rw-transcript-version="2">
 at this. After Claude executes Graphy,
 </span>
 <span data-rw-start="89.36" data-rw-transcript-version="2">
 this isn't just files anymore, it's an
 </span>
 <span data-rw-start="91.68" data-rw-transcript-version="2">
 actual graph. Everything is connected. I
 </span>
 <span data-rw-start="94.88" data-rw-transcript-version="2">
 can click and dissect actually what's
 </span>
 <span data-rw-start="97.2" data-rw-transcript-version="2">
 going on and what is linked together to
 </span>
 <span data-rw-start="99.36" data-rw-transcript-version="2">
 just here within the HTML file that it
 </span>
 <span data-rw-start="101.92" data-rw-transcript-version="2">
 generated. Then, instead of asking AI to
 </span>
 <span data-rw-start="104.56" data-rw-transcript-version="2">
 read everything again, I can now ask it,
 </span>
 <span data-rw-start="107.68" data-rw-transcript-version="2">
 "What connects off to the API layer?"
 </span>
 <span data-rw-start="110.48" data-rw-transcript-version="2">
 And now it answers using relationships,
 </span>
 <span data-rw-start="112.8" data-rw-transcript-version="2">
 using the MD file that it generated with
 </span>
 <span data-rw-start="115.52" data-rw-transcript-version="2">
 this call. It's not guesses, it's
 </span>
 <span data-rw-start="117.68" data-rw-transcript-version="2">
 relationships. And here's the part that
 </span>
 <span data-rw-start="119.76" data-rw-transcript-version="2">
 surprised me. Before this, around 14,000
 </span>
 <span data-rw-start="122.24" data-rw-transcript-version="2">
 Tokens, okay, however many were used.
 </span>
</p>
<p>
 <span data-rw-start="124.8" data-rw-transcript-version="2">
 After this, after it executes the first
 </span>
 <span data-rw-start="126.84" data-rw-transcript-version="2">
 time, we drop that down to maybe a
 </span>
 <span data-rw-start="128.64" data-rw-transcript-version="2">
 couple hundred. Same question,
 </span>
 <span data-rw-start="130.64" data-rw-transcript-version="2">
 completely different cost. All because
 </span>
 <span data-rw-start="132.88" data-rw-transcript-version="2">
 of this generated map. So, what is this
 </span>
 <span data-rw-start="135.96" data-rw-transcript-version="2">
 actually doing? Graphy is basically like
 </span>
 <span data-rw-start="138.56" data-rw-transcript-version="2">
 Google Maps for your code base. Instead
 </span>
 <span data-rw-start="141.04" data-rw-transcript-version="2">
 of raw text, you get nodes and
 </span>
 <span data-rw-start="143.28" data-rw-transcript-version="2">
 connections. Under it all, it uses
 </span>
 <span data-rw-start="145.64" data-rw-transcript-version="2">
 tree-sitters to understand the
 </span>
 <span data-rw-start="147.32" data-rw-transcript-version="2">
 structure, then an LLM to extract the
 </span>
 <span data-rw-start="150.16" data-rw-transcript-version="2">
 meaning. Then, it can group everything
 </span>
 <span data-rw-start="152.4" data-rw-transcript-version="2">
 into clusters and it's not just code. It
 </span>
 <span data-rw-start="155.24" data-rw-transcript-version="2">
 reads PDFs, diagrams, even audio and
 </span>
 <span data-rw-start="158.08" data-rw-transcript-version="2">
 video. All locally, nothing leaves the
 </span>
 <span data-rw-start="160.76" data-rw-transcript-version="2">
 machine. What you get from this is
 </span>
 <span data-rw-start="162.88" data-rw-transcript-version="2">
 simple. We get a visual graph, a written
 </span>
 <span data-rw-start="165.88" data-rw-transcript-version="2">
 report, and a knowledge base we can
 </span>
 <span data-rw-start="168.12" data-rw-transcript-version="2">
 actually explore. This visual graph is
 </span>
 <span data-rw-start="170.52" data-rw-transcript-version="2">
 huge for a lot of us as we can see how
 </span>
 <span data-rw-start="172.92" data-rw-transcript-version="2">
 things connect. Now, here's where this
 </span>
 <span data-rw-start="175.28" data-rw-transcript-version="2">
 changes how AI coding usually works.
 </span>
</p>
<p>
 <span data-rw-start="177.76" data-rw-transcript-version="2">
 Most tools use rag, which basically
 </span>
 <span data-rw-start="180.92" data-rw-transcript-version="2">
 means find similar chunks of text. Well,
 </span>
 <span data-rw-start="183.88" data-rw-transcript-version="2">
 Graphy doesn't do that. It builds real
 </span>
 <span data-rw-start="186.2" data-rw-transcript-version="2">
 relationships. This function calls that
 </span>
 <span data-rw-start="189.08" data-rw-transcript-version="2">
 one. This module depends on that. This
 </span>
 <span data-rw-start="191.96" data-rw-transcript-version="2">
 idea came from this document. And it
 </span>
 <span data-rw-start="194.2" data-rw-transcript-version="2">
 even tells you how confident it is. So,
 </span>
 <span data-rw-start="196.84" data-rw-transcript-version="2">
 instead of this looks related, we get
 </span>
 <span data-rw-start="199.4" data-rw-transcript-version="2">
 something like this is actually
 </span>
 <span data-rw-start="200.84" data-rw-transcript-version="2">
 connected in an actual visual
 </span>
 <span data-rw-start="202.52" data-rw-transcript-version="2">
 representation of what is connected. And
 </span>
 <span data-rw-start="205" data-rw-transcript-version="2">
 the biggest difference here, it
 </span>
 <span data-rw-start="206.32" data-rw-transcript-version="2">
 remembers too since it generated us that
 </span>
 <span data-rw-start="208.92" data-rw-transcript-version="2">
 MD file, it can look back on. We're not
 </span>
 <span data-rw-start="211.68" data-rw-transcript-version="2">
 starting from zero every time. It
 </span>
 <span data-rw-start="213.76" data-rw-transcript-version="2">
 updates only what's changed, so your AI
 </span>
 <span data-rw-start="216.36" data-rw-transcript-version="2">
 finally has context that sticks. All
 </span>
 <span data-rw-start="219" data-rw-transcript-version="2">
 right, now I actually thought all this
 </span>
 <span data-rw-start="220.68" data-rw-transcript-version="2">
 was pretty sweet. But what are the good
 </span>
 <span data-rw-start="222.84" data-rw-transcript-version="2">
 and the bad things here? And now, first
 </span>
 <span data-rw-start="224.88" data-rw-transcript-version="2">
 up to the plate, the efficiency
 </span>
</p>
<p>
 <span data-rw-start="226.6" data-rw-transcript-version="2">
 compounds. Every question gets cheaper,
 </span>
 <span data-rw-start="229.72" data-rw-transcript-version="2">
 and because it connects code, docs,
 </span>
 <span data-rw-start="231.96" data-rw-transcript-version="2">
 diagrams, you start finding
 </span>
 <span data-rw-start="233.84" data-rw-transcript-version="2">
 relationships you didn't even know
 </span>
 <span data-rw-start="235.28" data-rw-transcript-version="2">
 existed. That's huge for onboarding for
 </span>
 <span data-rw-start="238" data-rw-transcript-version="2">
 these messy projects that we get dumped
 </span>
 <span data-rw-start="239.92" data-rw-transcript-version="2">
 Into. That's great. Now, the drawbacks to all this are this. The first run can be slow and cost tokens, especially with
 </span>
 <span data-rw-start="242.08" data-rw-transcript-version="2">
 a lot of documents. After that, it's
 </span>
 <span data-rw-start="244.28" data-rw-transcript-version="2">
 cached, but yeah, that first hit is
 </span>
 <span data-rw-start="247.4" data-rw-transcript-version="2">
 real. It's also early, so long-term
 </span>
 <span data-rw-start="249.6" data-rw-transcript-version="2">
 support is still unknown. And a small
 </span>
 <span data-rw-start="256.6" data-rw-transcript-version="2">
 thing: when you install this, it's
 </span>
 <span data-rw-start="258.359" data-rw-transcript-version="2">
 Graphy with two Ys, not one. So, check
 </span>
 <span data-rw-start="261.04" data-rw-transcript-version="2">
 your spelling on that. The relationships
 </span>
 <span data-rw-start="262.8" data-rw-transcript-version="2">
 aren't always perfect, but it labels
 </span>
 <span data-rw-start="264.56" data-rw-transcript-version="2">
 them clearly, extracted, inferred, and
 </span>
 <span data-rw-start="267.36" data-rw-transcript-version="2">
 ambiguous, so you know what you can
 </span>
 <span data-rw-start="269.36" data-rw-transcript-version="2">
 actually trust. And if your repo is
 </span>
 <span data-rw-start="271.36" data-rw-transcript-version="2">
 tiny, this is going to be somewhat of an
 </span>
 <span data-rw-start="273.24" data-rw-transcript-version="2">
 overkill. So, is it worth it? I mean,
 </span>
 <span data-rw-start="275.8" data-rw-transcript-version="2">
 yeah, if you're using AI on anything
 </span>
</p>
<p>
 <span data-rw-start="277.56" data-rw-transcript-version="2">
 real, this is cool. It's I thought it
 </span>
 <span data-rw-start="279.36" data-rw-transcript-version="2">
 was worth it. Because your biggest
 </span>
 <span data-rw-start="281.12" data-rw-transcript-version="2">
 problem isn't running the code, it's
 </span>
 <span data-rw-start="283" data-rw-transcript-version="2">
 actually understanding it across files,
 </span>
 <span data-rw-start="284.92" data-rw-transcript-version="2">
 across time, across context. And that's
 </span>
 <span data-rw-start="287.32" data-rw-transcript-version="2">
 exactly what this fixes. The token
 </span>
 <span data-rw-start="289.6" data-rw-transcript-version="2">
 savings alone make it worth trying, but
 </span>
 <span data-rw-start="291.72" data-rw-transcript-version="2">
 the bigger win is this. Your AI stops
 </span>
 <span data-rw-start="294.36" data-rw-transcript-version="2">
 Guessing and starts reasoning. If you're
 </span>
 <span data-rw-start="296.48" data-rw-transcript-version="2">
 working solo, doing research, or have
 </span>
 <span data-rw-start="298.56" data-rw-transcript-version="2">
 all these big systems, this is a serious
 </span>
 <span data-rw-start="301.12" data-rw-transcript-version="2">
 upgrade. If you're just working on
 </span>
 <span data-rw-start="302.36" data-rw-transcript-version="2">
 smaller scripts, this is probably just
 </span>
 <span data-rw-start="303.76" data-rw-transcript-version="2">
 an overkill, so you don't really need to
 </span>
 <span data-rw-start="305.64" data-rw-transcript-version="2">
 try it. But most have to try this; this
 </span>
 <span data-rw-start="308.08" data-rw-transcript-version="2">
 is going to be an awesome tool. If you
 </span>
 <span data-rw-start="309.44" data-rw-transcript-version="2">
 enjoy coding tools and tips to speed up
 </span>
 <span data-rw-start="311.16" data-rw-transcript-version="2">
 your workflow, be sure to subscribe to
 </span>
 <span data-rw-start="313" data-rw-transcript-version="2">
 the Better Stack channel. We'll see you
 </span>
 <span data-rw-start="314.92" data-rw-transcript-version="2">
 in another video.
 </span>
</p>