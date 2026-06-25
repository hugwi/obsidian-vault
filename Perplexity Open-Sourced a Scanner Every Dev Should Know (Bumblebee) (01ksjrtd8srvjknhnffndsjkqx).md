---
categories:
  - "[[Resources]]"
domain: engineering
title: "Perplexity Open-Sourced a Scanner Every Dev Should Know (Bumblebee)"
source: "https://www.youtube.com/watch?v=L6iAw5yitfc"
author: "Better Stack"
published: 2026-05-26
created: 2026-05-26
description: "In this video, I take a hands-on look at Bumblebee, Perplexity’s new open-source\"
tags:
  - to-process
  - dev-tools
---

You know what's annoying about supply chain attacks? By the time everyone is panicking, the question is not is production safe, it's did anyone install this thing locally? This is Bumblebee. It's a new open source tool from Perplexity that scans your dev machine for packages, extensions, and MCP configs without running your package managers or executing project code. So, instead of looking around manually, you get a local inventory in seconds. I'm going to run it live, then we'll talk about where it actually works and where 

it doesn't. Now, the old model was simple. Scan the repo, scan the container, scan production. But, that's not how many of us work anymore. Today, one laptop can have package managers, browser extensions, editor extensions, AI coding tools, local agents, all of this living together. That is a lot of trust packed into one machine. Perplexity built Bumblebee internally for this exact reason, then open sourced it just a few 

days back. Bumblebee is a read-only single binary scanner that inventories packages, editor extensions, browser extensions, and AI tool configs from local metadata. No MPM LS, no pip show, no running random project code, just metadata. Let's try running it. If you enjoy coding tools that speed up your workflow, be sure to subscribe. We have videos coming out all the time. All right, first up to the plate, we got to install this thing with go install from GitHub. That gives us a single go 

binary. No daemon, no service. Now, let's run the self-test. All I got to do for this is run Bumblebee self-test, and hopefully we get back self-test okay. Good. The scanner can detect its known fixture data correctly. That's what this test did. Now, let's run a baseline scan. All we're going to do is do Bumblebee scan profile. We're going to say baseline, and we're going to drop in our NDJSON file. This is the scan we'd 

use for regular developable endpoint inventory. It checks common global and user level package roots, editor extensions, browser extensions, and supported MCP configs. Now, let's look at the output. I'm going to run head here and this is the big thing Bumblebee is doing now. Each line is a structured record we get back. So, you get the ecosystem package name, version, source file, confidence level, the metadata, and you get where Bumblebee found it. 

So, now instead of us asking, do I maybe have this installed somewhere on the system, we can actually now see it right here. And because this is read-only metadata parsing, Bumblebee is not calling NPM. It's not importing any Python packages and it's not building your Go project. All it's doing is it's just reading files and it's why this is useful during an incident. If you have Go installed, this is the point where I'd maybe pause the video, maybe try it on your own machine. It's super easy to spin up. Okay, cool. But, why is this 

not just another security scanner? Cuz we already have these. Now, at first glance, you might think a few things. It's another SCA tool, but that's actually not what this is. SCA tools are mostly about your application dependencies. SBOM tools are about what you shipped. EDR is about what you executed. Bumblebee is about the local developer state. So, imagine a compromised package advisory drops. You need to know which laptops might be 

exposed. The obvious move is to ask everyone to run package manager commands, but that's exactly the wrong thing here. If we're looking for something malicious, you don't want your command to accidentally execute the malicious behavior. So, Bumblebee is straightforward. Read metadata, emit inventory, match known exposures, and then get out. It's done. It has three scan profiles. First is the baseline. This is your lightweight recurring scan. It looks at global packages, user level 

tool chains, extensions, and MCP configs. Basically, what normally exists on this developer machine, that's the question that it's giving us back, it's answering. Then it goes to the project. This is for known workspace directories like code, source, or work. Use this when you care about lock files across actual dev folders. And then we can even get it to go deeper. This is the incident response mode. You point it at explicit roots, even something broad like home. Usually with an exposure 

catalog and a duration limit. So your normal workflow might be Bumblebee scan profile baseline, okay. When something bad happens, you switch to a deeper scan. Bumblebee scan profile, you can go deeper with this command right here. That's really the process for all this. Baseline when things are calm, deep scan when there's smoke. And the coverage is what makes this really interesting. Bumblebee can look across NPM, PNPM, Yarn, Bun, Go modules, you name it. Plus 

it can look at supported MCP JSON configs. That one is a major feature, cuz nowadays MCP configs are becoming the new ENV files. We have them all over our system. Bumblebee also outputs NDJSON. Now, some people are going to hate that, but another way to look at it is it means you can pipe it into JQ, ship it to a file, collect it through MDM, ingest it into an SCIM, or hand it to another agentic workflow. It's just trying to be boring, scriptable 

infrastructure. And for this kind of problem, boring is probably best anyways. Now, it's fast. It's really fast. It's a single go binary with zero non-standard library dependencies. That is a very dev friendly starting point. That means it's safe by design. The read-only approach is not a small detail. During a supply chain incident, just run the package manager and see what happens. Uh that's not always the best plan. If the package you're looking at has malicious lifestyle scripts or weird 

plug-in behavior, you don't want your scanner to be the thing that accidentally triggers it. Now, this also fills a real gap. Most teams have some visibility into CI, some visibility into container production, and some endpoint visibility. But, the dev machine can get messy. It has half-finished projects. It has old clones, global package test virtual environments, AI tooling, all the stuff that never shows up in your clean official inventory. Bumblebee gives you a practical way to see that 

local state. And then finally, the AI config coverage is right on time. Local agents, MPC servers, and tool calling workflows are moving fast. But, keep this in mind now, too, while you're going to use Bumblebee. This is brand new. Like, I'm talking super, super new as it just dropped. So, expect changes. It is focused on macOS and Linux right now. The exposure catalog flow is nice, but it also means Bumblebee gets much more useful when you have good advisory data. And it is not EDR, right? It 

answers a narrower question. What packages, extensions, and dev tool configs are present on this machine? And do any match something that we already know is bad? That's the point. This is not replacing your security staff. It is filling the part your security staff probably doesn't see clearly. So, should you actually use Bumblebee? My answer is yes, especially your day-to-day work touches NPM, Go, VS Code, Cursor, Claude, servers, that kind of stuff. Run 

a baseline scan once a week, right? It's one single command. Bumblebee scan your profile, and it's going to do what I showed you here. Now, you have a snapshot of what's on your machine. Dump the NDJSON central, then when an incident hits, you can search across everything instead of asking everyone in Slack, "Hey, does anyone have this?" Bumblebee tells you what dev machines currently exposed through local package metadata, extension manifests, and supported AI tool configs. That is extremely useful 

in the first hour when anything goes wrong because nobody wants to debate. They want to know who is exposed, where is it, and how fast prove it. And for that, Bumblebee is pretty compelling. It's a pretty strong open-source tool that we just got. If you enjoy coding tools and tips like this, be sure to subscribe to the Better Stack channel. We'll see you in another video. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 You know what's annoying about supply
 </span>
 <span data-rw-start="1.76" data-rw-transcript-version="2">
 chain attacks? By the time everyone is
 </span>
 <span data-rw-start="3.6" data-rw-transcript-version="2">
 panicking, the question is not, "Is
 </span>
 <span data-rw-start="5.48" data-rw-transcript-version="2">
 production safe?" It's, "Did anyone install
 </span>
 <span data-rw-start="7.92" data-rw-transcript-version="2">
 this thing locally?" This is Bumblebee.
 </span>
 <span data-rw-start="11.16" data-rw-transcript-version="2">
 It's a new open-source tool from
 </span>
 <span data-rw-start="12.92" data-rw-transcript-version="2">
 Perplexity that scans your dev machine
 </span>
 <span data-rw-start="15.32" data-rw-transcript-version="2">
 for packages, extensions, and MCP
 </span>
 <span data-rw-start="18" data-rw-transcript-version="2">
 configs without running your package
 </span>
 <span data-rw-start="19.76" data-rw-transcript-version="2">
 managers or executing project code.
 </span>
 <span data-rw-start="22.56" data-rw-transcript-version="2">
 So, instead of looking around manually, you
 </span>
 <span data-rw-start="24.36" data-rw-transcript-version="2">
 get a local inventory in seconds. I'm
 </span>
 <span data-rw-start="26.92" data-rw-transcript-version="2">
 going to run it live, then we'll talk
 </span>
 <span data-rw-start="28.6" data-rw-transcript-version="2">
 about where it actually works and where
 </span>
 <span data-rw-start="30.36" data-rw-transcript-version="2">
 it doesn't.
 </span>
</p>
<p>
 <span data-rw-start="36" data-rw-transcript-version="2">
 Now, the old model was simple. Scan the
 </span>
 <span data-rw-start="38.36" data-rw-transcript-version="2">
 repo, scan the container, scan
 </span>
 <span data-rw-start="40.6" data-rw-transcript-version="2">
 production. But, that's not how many of
 </span>
 <span data-rw-start="42.68" data-rw-transcript-version="2">
 us work anymore. Today, one laptop can
 </span>
 <span data-rw-start="45.6" data-rw-transcript-version="2">
 have package managers, browser
 </span>
 <span data-rw-start="47.48" data-rw-transcript-version="2">
 extensions, editor extensions, AI coding
 </span>
 <span data-rw-start="49.76" data-rw-transcript-version="2">
 tools, local agents, all of this living
 </span>
 <span data-rw-start="52.44" data-rw-transcript-version="2">
 together. That is a lot of trust packed
 </span>
 <span data-rw-start="54.76" data-rw-transcript-version="2">
 into one machine. Perplexity built
 </span>
 <span data-rw-start="57.12" data-rw-transcript-version="2">
 Bumblebee internally for this exact
 </span>
 <span data-rw-start="59.24" data-rw-transcript-version="2">
 Reason, then, open sourced it just a few
 </span>
 <span data-rw-start="61.48" data-rw-transcript-version="2">
 days back. Bumblebee is a read-only
 </span>
 <span data-rw-start="64" data-rw-transcript-version="2">
 single binary scanner that inventories
 </span>
 <span data-rw-start="66.16" data-rw-transcript-version="2">
 packages, editor extensions, browser
 </span>
 <span data-rw-start="68.36" data-rw-transcript-version="2">
 extensions, and AI tool configs from
 </span>
</p>
<p>
 <span data-rw-start="71" data-rw-transcript-version="2">
 local metadata. No MPM LS, no pip show,
 </span>
 <span data-rw-start="75.16" data-rw-transcript-version="2">
 no running random project code, just
 </span>
 <span data-rw-start="77.52" data-rw-transcript-version="2">
 metadata. Let's try running it. If you
 </span>
 <span data-rw-start="79.6" data-rw-transcript-version="2">
 enjoy coding tools that speed up your
 </span>
 <span data-rw-start="81" data-rw-transcript-version="2">
 workflow, be sure to subscribe. We have
 </span>
 <span data-rw-start="82.96" data-rw-transcript-version="2">
 videos coming out all the time. All
 </span>
 <span data-rw-start="84.96" data-rw-transcript-version="2">
 right, first up to the plate, we got to
 </span>
 <span data-rw-start="86.52" data-rw-transcript-version="2">
 install this thing with go install from
 </span>
 <span data-rw-start="88.96" data-rw-transcript-version="2">
 GitHub. That gives us a single go
 </span>
 <span data-rw-start="91.64" data-rw-transcript-version="2">
 binary. No daemon, no service. Now,
 </span>
 <span data-rw-start="94.8" data-rw-transcript-version="2">
 let's run the self-test. All I got to do
 </span>
 <span data-rw-start="97.64" data-rw-transcript-version="2">
 for this is run Bumblebee self-test, and
 </span>
 <span data-rw-start="101.12" data-rw-transcript-version="2">
 hopefully we get back self-test okay.
 </span>
</p>
<p>
 <span data-rw-start="104.36" data-rw-transcript-version="2">
 Good. The scanner can detect its known
 </span>
 <span data-rw-start="107.08" data-rw-transcript-version="2">
 fixture data correctly. That's what this
 </span>
 <span data-rw-start="109.12" data-rw-transcript-version="2">
 test did. Now, let's run a baseline
 </span>
 <span data-rw-start="111.96" data-rw-transcript-version="2">
 scan. All we're going to do is do
 </span>
 <span data-rw-start="113.92" data-rw-transcript-version="2">
 Bumblebee scan profile. We're going to
 </span>
 <span data-rw-start="115.96" data-rw-transcript-version="2">
 say baseline, and we're going to drop in
 </span>
 <span data-rw-start="117.76" data-rw-transcript-version="2">
 our NDJSON file. This is the scan we'd
 </span>
 <span data-rw-start="120.96" data-rw-transcript-version="2">
 Use for regular developable endpoint
 </span>
 <span data-rw-start="122.96" data-rw-transcript-version="2">
 inventory. It checks common global and
 </span>
 <span data-rw-start="125.84" data-rw-transcript-version="2">
 user level package roots, editor
 </span>
 <span data-rw-start="127.56" data-rw-transcript-version="2">
 extensions, browser extensions, and
 </span>
 <span data-rw-start="129.44" data-rw-transcript-version="2">
 supported MCP configs. Now, let's look
 </span>
 <span data-rw-start="132.08" data-rw-transcript-version="2">
 at the output. I'm going to run head
 </span>
 <span data-rw-start="133.8" data-rw-transcript-version="2">
 here,
 </span>
 <span data-rw-start="134.84" data-rw-transcript-version="2">
 and this is the big thing Bumblebee is
 </span>
 <span data-rw-start="137.44" data-rw-transcript-version="2">
 doing now. Each line is a structured
 </span>
 <span data-rw-start="140.56" data-rw-transcript-version="2">
 record we get back. So, you get the
 </span>
 <span data-rw-start="143.4" data-rw-transcript-version="2">
 ecosystem package name, version, source
 </span>
 <span data-rw-start="146.28" data-rw-transcript-version="2">
 file, confidence level, the metadata,
 </span>
 <span data-rw-start="148.64" data-rw-transcript-version="2">
 and you get where Bumblebee found it.
 </span>
</p>
<p>
 <span data-rw-start="150.64" data-rw-transcript-version="2">
 So, now instead of us asking, do I maybe
 </span>
 <span data-rw-start="153.2" data-rw-transcript-version="2">
 have this installed somewhere on the
 </span>
 <span data-rw-start="154.72" data-rw-transcript-version="2">
 system, we can actually now see it right
 </span>
 <span data-rw-start="157.16" data-rw-transcript-version="2">
 here. And because this is read-only
 </span>
 <span data-rw-start="159.32" data-rw-transcript-version="2">
 metadata parsing, Bumblebee is not
 </span>
 <span data-rw-start="161.32" data-rw-transcript-version="2">
 calling NPM. It's not importing any
 </span>
 <span data-rw-start="164.6" data-rw-transcript-version="2">
 Python packages, and it's not building
 </span>
 <span data-rw-start="166.6" data-rw-transcript-version="2">
 your Go project. All it's doing is it's
 </span>
 <span data-rw-start="169.4" data-rw-transcript-version="2">
 just reading files, and this is why this is
 </span>
 <span data-rw-start="171.959" data-rw-transcript-version="2">
 useful during an incident. If you have
 </span>
 <span data-rw-start="174.04" data-rw-transcript-version="2">
 Go installed, this is the point where
 </span>
 <span data-rw-start="175.8" data-rw-transcript-version="2">
 I'd maybe pause the video, maybe try it.
 </span>
</p>
<p>
 <span data-rw-start="177.6" data-rw-transcript-version="2">
 On your own machine, it's super easy to
 </span>
 <span data-rw-start="179.36" data-rw-transcript-version="2">
 spin up. Okay, cool. But, why is this
 </span>
 <span data-rw-start="182.84" data-rw-transcript-version="2">
 not just another security scanner? Because
 </span>
 <span data-rw-start="185.28" data-rw-transcript-version="2">
 we already have these. Now, at first
 </span>
 <span data-rw-start="187.12" data-rw-transcript-version="2">
 glance, you might think a few things.
 </span>
 <span data-rw-start="189.04" data-rw-transcript-version="2">
 It's another SCA tool, but that's
 </span>
 <span data-rw-start="191.56" data-rw-transcript-version="2">
 actually not what this is. SCA tools are
 </span>
 <span data-rw-start="194.48" data-rw-transcript-version="2">
 mostly about your application
 </span>
 <span data-rw-start="196.04" data-rw-transcript-version="2">
 dependencies. SBOM tools are about what
 </span>
 <span data-rw-start="198.76" data-rw-transcript-version="2">
 you shipped. EDR is about what you
 </span>
 <span data-rw-start="200.92" data-rw-transcript-version="2">
 executed. Bumblebee is about the local
 </span>
 <span data-rw-start="203.64" data-rw-transcript-version="2">
 developer state. So, imagine a
 </span>
 <span data-rw-start="205.92" data-rw-transcript-version="2">
 compromised package advisory drops. You
 </span>
 <span data-rw-start="208.76" data-rw-transcript-version="2">
 need to know which laptops might be
 </span>
 <span data-rw-start="210.88" data-rw-transcript-version="2">
 exposed. The obvious move is to ask
 </span>
 <span data-rw-start="213.4" data-rw-transcript-version="2">
 everyone to run package manager
 </span>
 <span data-rw-start="215.28" data-rw-transcript-version="2">
 commands, but that's exactly the wrong
 </span>
 <span data-rw-start="217.12" data-rw-transcript-version="2">
 thing here. If we're looking for
 </span>
 <span data-rw-start="218.92" data-rw-transcript-version="2">
 something malicious, you don't want your
 </span>
 <span data-rw-start="220.519" data-rw-transcript-version="2">
 command to accidentally execute the
 </span>
 <span data-rw-start="222.48" data-rw-transcript-version="2">
 malicious behavior. So, Bumblebee is
 </span>
 <span data-rw-start="224.44" data-rw-transcript-version="2">
 straightforward. Read metadata, emit
 </span>
 <span data-rw-start="226.92" data-rw-transcript-version="2">
 inventory, match known exposures, and
 </span>
 <span data-rw-start="229.4" data-rw-transcript-version="2">
 then get out. It's done. It has three
 </span>
 <span data-rw-start="231.76" data-rw-transcript-version="2">
 scan profiles. First is the baseline.
 </span>
</p>
<p>
 <span data-rw-start="234.64" data-rw-transcript-version="2">
 This is your lightweight recurring scan.
 </span>
 <span data-rw-start="237.32" data-rw-transcript-version="2">
 It looks at global packages, user level tool chains, extensions, and MCP configs. Basically, what normally exists on this developer machine, that's the question that it's giving us back, it's answering.
 </span>
 <span data-rw-start="248.6" data-rw-transcript-version="2">
 Then it goes to the project.
 </span>
 <span data-rw-start="253.32" data-rw-transcript-version="2">
 This is for known workspace directories like code, source, or work. Use this when you care about lock files across actual dev folders.
 </span>
 <span data-rw-start="260.2" data-rw-transcript-version="2">
 And then we can even get it to go deeper.
 </span>
</p>
<p>
 <span data-rw-start="262.6" data-rw-transcript-version="2">
 This is the incident response mode. You point it at explicit roots, even something broad like home.
 </span>
 <span data-rw-start="269.32" data-rw-transcript-version="2">
 Usually with an exposure catalog and a duration limit.
 </span>
 <span data-rw-start="273.96" data-rw-transcript-version="2">
 So your normal workflow might be Bumblebee scan profile baseline, okay.
 </span>
 <span data-rw-start="278.64" data-rw-transcript-version="2">
 When something bad happens, you switch to a deeper scan.
 </span>
 <span data-rw-start="280.4" data-rw-transcript-version="2">
 Bumblebee scan profile, you can go deeper with this command right here.
 </span>
 <span data-rw-start="285.28" data-rw-transcript-version="2">
 That's really the process for all this.
 </span>
 <span data-rw-start="287.2" data-rw-transcript-version="2">
 Baseline when things are calm, deep scan when there's smoke.
 </span>
 <span data-rw-start="290" data-rw-transcript-version="2">
 And the coverage is what makes this really interesting.
 </span>
</p>
<p>
 <span data-rw-start="294.04" data-rw-transcript-version="2">
 Bumblebee can look across NPM, PNPM,
 </span>
 <span data-rw-start="297.4" data-rw-transcript-version="2">
 Yarn, Bun, Go modules, you name it. Plus
 </span>
 <span data-rw-start="300.72" data-rw-transcript-version="2">
 it can look at supported MCP JSON
 </span>
 <span data-rw-start="303.2" data-rw-transcript-version="2">
 configs. That one is a major feature,
 </span>
 <span data-rw-start="306" data-rw-transcript-version="2">
 because nowadays MCP configs are becoming
 </span>
 <span data-rw-start="308.84" data-rw-transcript-version="2">
 the new ENV files. We have them all over
 </span>
 <span data-rw-start="311.48" data-rw-transcript-version="2">
 our system. Bumblebee also outputs
 </span>
 <span data-rw-start="313.76" data-rw-transcript-version="2">
 NDJSON. Now, some people are going to
 </span>
 <span data-rw-start="316" data-rw-transcript-version="2">
 hate that, but another way to look at it
 </span>
 <span data-rw-start="317.919" data-rw-transcript-version="2">
 is it means you can pipe it into JQ,
 </span>
 <span data-rw-start="321.08" data-rw-transcript-version="2">
 ship it to a file, collect it through
 </span>
 <span data-rw-start="322.96" data-rw-transcript-version="2">
 MDM, ingest it into an SCIM, or hand it
 </span>
 <span data-rw-start="326.48" data-rw-transcript-version="2">
 to another agentic workflow. It's just
 </span>
 <span data-rw-start="329.08" data-rw-transcript-version="2">
 trying to be boring, scriptable
 </span>
 <span data-rw-start="331.24" data-rw-transcript-version="2">
 infrastructure. And for this kind of
 </span>
 <span data-rw-start="332.919" data-rw-transcript-version="2">
 problem, boring is probably best
 </span>
 <span data-rw-start="334.68" data-rw-transcript-version="2">
 anyways. Now, it's fast. It's really
 </span>
 <span data-rw-start="337.52" data-rw-transcript-version="2">
 fast. It's a single Go binary with zero
 </span>
 <span data-rw-start="339.8" data-rw-transcript-version="2">
 non-standard library dependencies. That
 </span>
 <span data-rw-start="342.04" data-rw-transcript-version="2">
 is a very dev-friendly starting point.
 </span>
</p>
<p>
 <span data-rw-start="344.64" data-rw-transcript-version="2">
 That means it's safe by design. The
 </span>
 <span data-rw-start="347.4" data-rw-transcript-version="2">
 read-only approach is not a small
 </span>
 <span data-rw-start="349.6" data-rw-transcript-version="2">
 detail. During a supply chain incident,
 </span>
 <span data-rw-start="351.92" data-rw-transcript-version="2">
 just run the package manager and see
 </span>
 <span data-rw-start="353.76" data-rw-transcript-version="2">
 what happens.
 </span>
</p>
<p>
 <span data-rw-start="355.12" data-rw-transcript-version="2">
 Uh, that's not always the best plan. If
 </span>
 <span data-rw-start="357.4" data-rw-transcript-version="2">
 the package you're looking at has
 </span>
 <span data-rw-start="359.24" data-rw-transcript-version="2">
 malicious lifestyle scripts or weird
 </span>
 <span data-rw-start="361.08" data-rw-transcript-version="2">
 plugin behavior, you don't want your
 </span>
 <span data-rw-start="363.2" data-rw-transcript-version="2">
 scanner to be the thing that
 </span>
 <span data-rw-start="364.44" data-rw-transcript-version="2">
 accidentally triggers it. Now, this also
 </span>
 <span data-rw-start="366.84" data-rw-transcript-version="2">
 fills a real gap. Most teams have some
 </span>
 <span data-rw-start="369.72" data-rw-transcript-version="2">
 visibility into CI, some visibility into
 </span>
 <span data-rw-start="372.56" data-rw-transcript-version="2">
 container production, and some endpoint
 </span>
 <span data-rw-start="375" data-rw-transcript-version="2">
 visibility. But, the dev machine can get
 </span>
 <span data-rw-start="377.28" data-rw-transcript-version="2">
 messy. It has half-finished projects. It
 </span>
 <span data-rw-start="379.919" data-rw-transcript-version="2">
 has old clones, global package test
 </span>
 <span data-rw-start="382.6" data-rw-transcript-version="2">
 virtual environments, AI tooling, all
 </span>
 <span data-rw-start="385.28" data-rw-transcript-version="2">
 the stuff that never shows up in your
 </span>
 <span data-rw-start="387.16" data-rw-transcript-version="2">
 clean official inventory. Bumblebee
 </span>
 <span data-rw-start="389.56" data-rw-transcript-version="2">
 gives you a practical way to see that
 </span>
 <span data-rw-start="391.44" data-rw-transcript-version="2">
 local state. And then finally, the AI
 </span>
 <span data-rw-start="393.68" data-rw-transcript-version="2">
 config coverage is right on time. Local
 </span>
 <span data-rw-start="396.72" data-rw-transcript-version="2">
 agents, MPC servers, and tool calling
 </span>
 <span data-rw-start="399.64" data-rw-transcript-version="2">
 workflows are moving fast. But, keep
 </span>
 <span data-rw-start="401.64" data-rw-transcript-version="2">
 this in mind now, too, while you're
 </span>
 <span data-rw-start="403.2" data-rw-transcript-version="2">
 going to use Bumblebee. This is brand
 </span>
 <span data-rw-start="405.4" data-rw-transcript-version="2">
 new. Like, I'm talking super, super new
 </span>
 <span data-rw-start="407.76" data-rw-transcript-version="2">
 as it just dropped. So, expect changes.
 </span>
 <span data-rw-start="410.48" data-rw-transcript-version="2">
 It is focused on macOS and Linux right.
 </span>
</p>
<p>
 <span data-rw-start="412.68" data-rw-transcript-version="2">
 Now, the exposure catalog flow is nice,
 </span>
 <span data-rw-start="414.76" data-rw-transcript-version="2">
 but it also means Bumblebee gets much
 </span>
 <span data-rw-start="416.84" data-rw-transcript-version="2">
 more useful when you have good advisory
 </span>
 <span data-rw-start="419.28" data-rw-transcript-version="2">
 data. And it is not EDR, right? It
 </span>
 <span data-rw-start="422.52" data-rw-transcript-version="2">
 answers a narrower question. What
 </span>
 <span data-rw-start="424.96" data-rw-transcript-version="2">
 packages, extensions, and dev tool
 </span>
 <span data-rw-start="427.36" data-rw-transcript-version="2">
 configs are present on this machine? And
 </span>
 <span data-rw-start="430.04" data-rw-transcript-version="2">
 do any match something that we already
 </span>
 <span data-rw-start="432" data-rw-transcript-version="2">
 know is bad? That's the point. This is
 </span>
 <span data-rw-start="434.12" data-rw-transcript-version="2">
 not replacing your security staff. It is
 </span>
 <span data-rw-start="436.64" data-rw-transcript-version="2">
 filling the part your security staff
 </span>
 <span data-rw-start="438" data-rw-transcript-version="2">
 probably doesn't see clearly. So, should
 </span>
 <span data-rw-start="439.96" data-rw-transcript-version="2">
 you actually use Bumblebee? My answer is
 </span>
 <span data-rw-start="441.88" data-rw-transcript-version="2">
 yes, especially your day-to-day work
 </span>
 <span data-rw-start="444.32" data-rw-transcript-version="2">
 touches NPM, Go, VS Code, Cursor,
 </span>
 <span data-rw-start="447.04" data-rw-transcript-version="2">
 Claude, servers, that kind of stuff. Run
 </span>
 <span data-rw-start="450.16" data-rw-transcript-version="2">
 a baseline scan once a week, right? It's
 </span>
</p>
<p>
 <span data-rw-start="452.8" data-rw-transcript-version="2">
 one single command. Bumblebee scans your
 </span>
 <span data-rw-start="455.04" data-rw-transcript-version="2">
 profile, and it's going to do what I
 </span>
 <span data-rw-start="457" data-rw-transcript-version="2">
 showed you here. Now, you have a
 </span>
 <span data-rw-start="458.48" data-rw-transcript-version="2">
 snapshot of what's on your machine. Dump
 </span>
 <span data-rw-start="461.28" data-rw-transcript-version="2">
 the NDJSON
 </span>
 <span data-rw-start="463.04" data-rw-transcript-version="2">
 central, then when an incident hits, you
 </span>
 <span data-rw-start="465.48" data-rw-transcript-version="2">
 can search across everything instead of
 </span>
 <span data-rw-start="467.52" data-rw-transcript-version="2">
 asking everyone in Slack, "Hey, does
 </span>
 <span data-rw-start="470.2" data-rw-transcript-version="2">
 Anyone have this? "Bumblebee tells you
 </span>
 <span data-rw-start="472.36" data-rw-transcript-version="2">
 what dev machines are currently exposed
 </span>
 <span data-rw-start="474.56" data-rw-transcript-version="2">
 through local package metadata,
 </span>
 <span data-rw-start="476.6" data-rw-transcript-version="2">
 extension manifests, and supported AI
 </span>
 <span data-rw-start="479.08" data-rw-transcript-version="2">
 tool configs. That is extremely useful
 </span>
 <span data-rw-start="481.84" data-rw-transcript-version="2">
 in the first hour when anything goes
 </span>
 <span data-rw-start="483.8" data-rw-transcript-version="2">
 wrong because nobody wants to debate.
 </span>
</p>
<p>
 <span data-rw-start="486.2" data-rw-transcript-version="2">
 They want to know who is exposed, where
 </span>
 <span data-rw-start="488.52" data-rw-transcript-version="2">
 it is, and how fast to prove it. And for
 </span>
 <span data-rw-start="490.96" data-rw-transcript-version="2">
 that, Bumblebee is pretty compelling.
 </span>
 <span data-rw-start="493.2" data-rw-transcript-version="2">
 It's a pretty strong open-source tool
 </span>
 <span data-rw-start="495.12" data-rw-transcript-version="2">
 that we just got. If you enjoy coding
 </span>
 <span data-rw-start="496.96" data-rw-transcript-version="2">
 tools and tips like this, be sure to
 </span>
 <span data-rw-start="498.44" data-rw-transcript-version="2">
 subscribe to the Better Stack channel.
 </span>
 <span data-rw-start="499.919" data-rw-transcript-version="2">
 We'll see you in another video.
 </span>
</p>