---
title: "How I Vibe Code Technical Videos With Claude Code and Remotion"
source: "https://www.youtube.com/watch?v=z7Bkf3Vc63U&t=37s"
author: "John Hartquist"
published: 2025-12-05
created: 2026-04-04
description: "In this video, I show how I create and edit videos with natural language"
tags:
  - to-process
  - agent-configuration
---

In this video, I'm going to show you how I create and edit videos with natural language using Claude Code and Remotion. If you've ever tried creating videos, even simple ones, you know [music] the pain. Scrubbing through timeline footage, slicing out the awkward pauses, gathering all the assets, sequencing them in the right place, [music] exporting. It's tedious, timeconuming, and it breaks your flow. [music] As a software engineer, I use Cloud Code every day to help me understand code bases, [music] track down bugs, and vibe code. I mean, architect new features. I 

also use it to automate workflows and quickly [music] spin up prototypes. It can be a very powerful tool. Recently, I've been experimenting with Remotion, which is a React library for rendering videos programmatically frame [music] by frame. Here's the thing. Cloud Code is really good at writing React code. React is one of the most popular web frameworks today and Claude excels at creating visuals with it. When you combine Cloud Code with Remotion, you can automate the tedious parts of video editing in a similar way to how it's used for general programming. I'm mainly 

interested in creating technical videos, tutorials, demos, that sort of thing. With Remotion, you get all the benefits of the web ecosystem. Code snippets with syntax highlighting, diagrams, smooth animations, anything you can build with React. With Cloud Code, you also get the full power of MCP servers. I can tell Claude to use the Playwright MCP to open a browser, navigate [music] to a documentation page, and take a screenshot. Then that goes straight into my video. With the replicate MCP, I can 

use a library of models to generate audio, images, B-roll footage, or even talking head videos using tools such as Nano Banana, VO3, 11 Labs, etc. All without leaving the command line. [music] And because it's all code- based, I can create reusable templates and tweak them just by telling Claude what I want. [music] Everything is stored in Git, and I can continue using the tools that I already love. I've put together a Claude and Remotion starter template that you can use to make your own videos. The link is in the 

description. After downloading the code from GitHub and installing the dependencies, we can run Cloud straight away. Run the dev server in the background. This pulls up the Remotion Studio where you can preview while editing the video. [music] There's a few examples included for reference. So, we can see this one has a title segment and then a content segment. And then there's also some pre-built components with some previews. For 

example, title slide with a fade in [music] content slide. Let's add a title slide that says how to explain things to programmers. Let's create a new step component. On each step, we'll have the text in the top left say step one [music] and then some supporting text. We'll have three steps. Step one, add some diagrams. Step two, show some code. [music] Step three, 

sprinkle in some AI. [music] For step one, let's add a fancy mermaid diagram. [music] For step two, let's add a code snippet from this repository and have it animate over time. [music] 

For step three, let's generate a video. Generate a 6second clip of the most advanced AI imaginable. For this step, Claude is going to use our generate video command, which calls the replicate API, and we'll generate a video using VO3.1 fast by default. [music] We can look in our assets folder here. Once the video is ready, it'll show up and we can preview it. 

[music] Okay, let's preview that video. Cool. And [snorts] back to our composition. It looks a little small. Let's make the video a little bit bigger. [music] 

Let's add one more slide to the end that just says, "Thanks for watching. >> [music] >> Let's update the font to be monospace and update the color scheme to be groove box. Make sure the text is centered on the first title slide. Maybe make the font slightly smaller. Let's generate a better background 

image. It should still follow the groove box color scheme and look technical but clean and modern and use it for the background for all of the slides. Again, Claude is using the replicate API to generate images using the new Nano Banana Pro and it'll place them images in the assets folder that we can preview over here. [music] Let's actually darken the background 

image. It's a little too bright for my taste. Now, let's create a voice over for the video. First, let's come up with a draft script. Each slide should say step one, [music] then the text, like add some diagrams, and then make some kind of comment relative to the slide. Let's try to make it a little funnier. [music] That looks great. Now let's generate the voice over using 11 Labs. 

So now we can preview those audio files in our assets folder. See what it sounds like. >> How to explain things to programmers. Spoiler, it's not with words. >> Okay. and [music] it's already added the audio to our slides. However, we need to update the durations and timings for 

everything to line up nicely. Run the /transcribe command on each clip to generate word level timestamps. Next, update the transition durations for each animation so that the different text fades in at the correct time. [music] This command uses the deepgram API to generate word level timestamps. 

[music] Then once you're done, you just click render. [music] And here's the final video in all its glory. >> How to explain things to programmers. Spoiler, it's not with words. Step one, add some diagrams. Programmers are visual creatures. We can't read documentation, but we'll stare at a flowchart for hours. Step two, show some code. Forget paragraphs. Just throw in a 

code snippet and watch their eyes light up like it's Christmas morning. Step three, sprinkle in some AI because nothing says I'm a serious professional like generating a video of a glowing robot brain. Thanks for watching. Now go explain something to a programmer. Good luck. >> So that's the workflow. I'm curious, what kind of videos would you make with something like this? If you'd like a deeper tutorial, let me know in the comments. [music] For me, this isn't about AI generated content. It's about 

removing friction so you can focus on what you actually want to say. 

<p>
 <span data-rw-start="0.719" data-rw-transcript-version="2">
 In this video, I'm going to show you how
 </span>
 <span data-rw-start="2.399" data-rw-transcript-version="2">
 I create and edit videos with natural
 </span>
 <span data-rw-start="4.4" data-rw-transcript-version="2">
 language using Claude Code and Remotion.
 </span>
 <span data-rw-start="7.44" data-rw-transcript-version="2">
 If you've ever tried creating videos,
 </span>
 <span data-rw-start="9.28" data-rw-transcript-version="2">
 even simple ones, you know [music] the
 </span>
 <span data-rw-start="10.8" data-rw-transcript-version="2">
 pain. Scrubbing through timeline
 </span>
 <span data-rw-start="12.559" data-rw-transcript-version="2">
 footage, slicing out the awkward pauses,
 </span>
 <span data-rw-start="14.88" data-rw-transcript-version="2">
 gathering all the assets, sequencing
 </span>
 <span data-rw-start="16.72" data-rw-transcript-version="2">
 them in the right place, [music]
 </span>
 <span data-rw-start="18.16" data-rw-transcript-version="2">
 exporting. It's tedious, time-consuming,
 </span>
 <span data-rw-start="20.8" data-rw-transcript-version="2">
 and it breaks your flow. [music]
 </span>
 <span data-rw-start="22.8" data-rw-transcript-version="2">
 As a software engineer, I use Cloud Code
 </span>
 <span data-rw-start="25.199" data-rw-transcript-version="2">
 every day to help me understand code
 </span>
 <span data-rw-start="27.039" data-rw-transcript-version="2">
 bases, [music] track down bugs, and vibe
 </span>
 <span data-rw-start="29.359" data-rw-transcript-version="2">
 code. I mean, architect new features. I
 </span>
 <span data-rw-start="32.16" data-rw-transcript-version="2">
 also use it to automate workflows and
 </span>
 <span data-rw-start="34" data-rw-transcript-version="2">
 quickly [music] spin up prototypes. It
 </span>
 <span data-rw-start="35.76" data-rw-transcript-version="2">
 can be a very powerful tool. Recently,
 </span>
 <span data-rw-start="38.399" data-rw-transcript-version="2">
 I've been experimenting with Remotion,
 </span>
 <span data-rw-start="40.399" data-rw-transcript-version="2">
 which is a React library for rendering
 </span>
 <span data-rw-start="42.32" data-rw-transcript-version="2">
 videos programmatically frame [music] by
 </span>
 <span data-rw-start="44.239" data-rw-transcript-version="2">
 frame. Here's the thing. Cloud Code is
 </span>
 <span data-rw-start="46.719" data-rw-transcript-version="2">
 really good at writing React code. React
 </span>
 <span data-rw-start="48.879" data-rw-transcript-version="2">
 is one of the most popular web
 </span>
 <span data-rw-start="50.239" data-rw-transcript-version="2">
 frameworks today, and Claude excels at.
 </span>
</p>
<p>
 <span data-rw-start="52.16" data-rw-transcript-version="2">
 Creating visuals with it. When you
 </span>
 <span data-rw-start="54.079" data-rw-transcript-version="2">
 combine Cloud Code with Remotion, you
 </span>
 <span data-rw-start="56.239" data-rw-transcript-version="2">
 can automate the tedious parts of video
 </span>
 <span data-rw-start="58" data-rw-transcript-version="2">
 editing in a similar way to how it's
 </span>
 <span data-rw-start="59.76" data-rw-transcript-version="2">
 used for general programming. I'm mainly
 </span>
 <span data-rw-start="62.16" data-rw-transcript-version="2">
 interested in creating technical videos,
 </span>
 <span data-rw-start="64.32" data-rw-transcript-version="2">
 tutorials, demos, that sort of thing.
 </span>
 <span data-rw-start="66.88" data-rw-transcript-version="2">
 With Remotion, you get all the benefits
 </span>
 <span data-rw-start="68.56" data-rw-transcript-version="2">
 of the web ecosystem. Code snippets with
 </span>
 <span data-rw-start="71.04" data-rw-transcript-version="2">
 syntax highlighting, diagrams, smooth
 </span>
 <span data-rw-start="73.439" data-rw-transcript-version="2">
 animations, anything you can build with
 </span>
 <span data-rw-start="75.52" data-rw-transcript-version="2">
 React. With Cloud Code, you also get the
 </span>
 <span data-rw-start="78.4" data-rw-transcript-version="2">
 full power of MCP servers. I can tell
 </span>
 <span data-rw-start="81.04" data-rw-transcript-version="2">
 Claude to use the Playwright MCP to open
 </span>
 <span data-rw-start="83.439" data-rw-transcript-version="2">
 a browser, navigate [music] to a
 </span>
 <span data-rw-start="85.119" data-rw-transcript-version="2">
 documentation page, and take a
 </span>
 <span data-rw-start="86.88" data-rw-transcript-version="2">
 screenshot. Then that goes straight into
 </span>
 <span data-rw-start="88.64" data-rw-transcript-version="2">
 my video. With the replicate MCP, I can
 </span>
 <span data-rw-start="91.52" data-rw-transcript-version="2">
 use a library of models to generate
 </span>
 <span data-rw-start="93.2" data-rw-transcript-version="2">
 audio, images, B-roll footage, or even
 </span>
 <span data-rw-start="96.159" data-rw-transcript-version="2">
 talking head videos using tools such as
 </span>
 <span data-rw-start="98.24" data-rw-transcript-version="2">
 Nano Banana, VO3, 11 Labs, etc. All
 </span>
 <span data-rw-start="102.32" data-rw-transcript-version="2">
 without leaving the command line.
 </span>
 <span data-rw-start="104.146" data-rw-transcript-version="2">
 [music] And because it's all code-
 </span>
 <span data-rw-start="105.6" data-rw-transcript-version="2">
 based, I can create reusable templates.
 </span>
</p>
<p>
 <span data-rw-start="107.6" data-rw-transcript-version="2">
 and tweak them just by telling Claude
 </span>
 <span data-rw-start="109.36" data-rw-transcript-version="2">
 what I want. [music] Everything is
 </span>
 <span data-rw-start="110.799" data-rw-transcript-version="2">
 stored in Git, and I can continue using
 </span>
 <span data-rw-start="112.799" data-rw-transcript-version="2">
 the tools that I already love. I've put
 </span>
 <span data-rw-start="115.36" data-rw-transcript-version="2">
 together a Claude and Remotion starter
 </span>
 <span data-rw-start="117.36" data-rw-transcript-version="2">
 template that you can use to make your
 </span>
 <span data-rw-start="118.96" data-rw-transcript-version="2">
 own videos. The link is in the
 </span>
 <span data-rw-start="120.479" data-rw-transcript-version="2">
 description.
 </span>
 <span data-rw-start="122" data-rw-transcript-version="2">
 After downloading the code from GitHub
 </span>
 <span data-rw-start="123.92" data-rw-transcript-version="2">
 and installing the dependencies, we can
 </span>
 <span data-rw-start="126.32" data-rw-transcript-version="2">
 run Cloud straight away.
 </span>
</p>
<p>
 <span data-rw-start="129.599" data-rw-transcript-version="2">
 Run the dev server in the background.
 </span>
 <span data-rw-start="133.599" data-rw-transcript-version="2">
 This pulls up the Remotion Studio where
 </span>
 <span data-rw-start="135.76" data-rw-transcript-version="2">
 you can preview while editing the video.
 </span>
 <span data-rw-start="138.206" data-rw-transcript-version="2">
 [music] There's a few examples included
 </span>
 <span data-rw-start="139.84" data-rw-transcript-version="2">
 for reference. So, we can see this one
 </span>
 <span data-rw-start="142.72" data-rw-transcript-version="2">
 has a title segment and then a content
 </span>
 <span data-rw-start="145.12" data-rw-transcript-version="2">
 segment.
 </span>
 <span data-rw-start="147.599" data-rw-transcript-version="2">
 And then there's also some pre-built
 </span>
 <span data-rw-start="149.36" data-rw-transcript-version="2">
 components with some previews. For
 </span>
 <span data-rw-start="151.68" data-rw-transcript-version="2">
 example, a title slide with a fade-in
 </span>
 <span data-rw-start="154.581" data-rw-transcript-version="2">
 [music] content slide. Let's add a title
 </span>
 <span data-rw-start="157.92" data-rw-transcript-version="2">
 slide that says how to explain things to
 </span>
 <span data-rw-start="160.4" data-rw-transcript-version="2">
 programmers.
 </span>
 <span data-rw-start="164.08" data-rw-transcript-version="2">
 Let's create a new step component. On
 </span>
 <span data-rw-start="167.04" data-rw-transcript-version="2">
 Each step, we'll have the text in the
 </span>
 <span data-rw-start="168.959" data-rw-transcript-version="2">
 top left say step one [music] and then
 </span>
 <span data-rw-start="172.48" data-rw-transcript-version="2">
 some supporting text. We'll have three
 </span>
 <span data-rw-start="175.12" data-rw-transcript-version="2">
 steps. Step one, add some diagrams. Step
 </span>
 <span data-rw-start="178.8" data-rw-transcript-version="2">
 two, show some code. [music] Step three,
 </span>
 <span data-rw-start="182.56" data-rw-transcript-version="2">
 sprinkle in some AI.
 </span>
</p>
<p>
 <span data-rw-start="186.677" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="190" data-rw-transcript-version="2">
 For step one, let's add a fancy mermaid
 </span>
 <span data-rw-start="192.56" data-rw-transcript-version="2">
 diagram. [music]
 </span>
 <span data-rw-start="198.959" data-rw-transcript-version="2">
 For step two, let's add a code snippet
 </span>
 <span data-rw-start="201.12" data-rw-transcript-version="2">
 from this repository and have it animate
 </span>
 <span data-rw-start="203.519" data-rw-transcript-version="2">
 over time.
 </span>
</p>
<p>
 <span data-rw-start="205.672" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="210.799" data-rw-transcript-version="2">
 For step three, let's generate a video.
 </span>
</p>
<p>
 <span data-rw-start="213.44" data-rw-transcript-version="2">
 Generate a 6-second clip of the most
 </span>
 <span data-rw-start="215.599" data-rw-transcript-version="2">
 advanced AI imaginable.
 </span>
 <span data-rw-start="218.56" data-rw-transcript-version="2">
 For this step, Claude is going to use
 </span>
 <span data-rw-start="220.08" data-rw-transcript-version="2">
 our generate video command, which calls
 </span>
 <span data-rw-start="223.28" data-rw-transcript-version="2">
 the replicate API, and we'll generate a
 </span>
 <span data-rw-start="226.159" data-rw-transcript-version="2">
 video using VO3.1 fast by default.
 </span>
 <span data-rw-start="229.907" data-rw-transcript-version="2">
 [music] We can look in our assets folder
 </span>
 <span data-rw-start="233.04" data-rw-transcript-version="2">
 here. Once the video is ready, it'll
 </span>
 <span data-rw-start="235.519" data-rw-transcript-version="2">
 show up and we can preview it.
 </span>
 <span data-rw-start="241.042" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="247.2" data-rw-transcript-version="2">
 Okay, let's preview that video.
 </span>
</p>
<p>
 <span data-rw-start="253.36" data-rw-transcript-version="2">
 Cool.
 </span>
 <span data-rw-start="257.919" data-rw-transcript-version="2">
 And [snorts] back to our
 </span>
 <span data-rw-start="260.16" data-rw-transcript-version="2">
 composition. It looks a little small.
 </span>
 <span data-rw-start="262.079" data-rw-transcript-version="2">
 Let's make the video a little bit bigger.
 </span>
 <span data-rw-start="266.587" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="271.36" data-rw-transcript-version="2">
 Let's add one more slide to the end that just says, "Thanks for watching."
 </span>
 <span data-rw-start="280.343" data-rw-transcript-version="2">
 &gt;&gt; [music]
 </span>
 <span data-rw-start="280.639" data-rw-transcript-version="2">
 &gt;&gt; Let's update the font to be monospace and update the color scheme to be groove box.
 </span>
 <span data-rw-start="292" data-rw-transcript-version="2">
 Make sure the text is centered on the first title slide.
 </span>
 <span data-rw-start="294.32" data-rw-transcript-version="2">
 Maybe make the font slightly smaller.
 </span>
 <span data-rw-start="298.88" data-rw-transcript-version="2">
 Let's generate a better background image. It should still follow the groove box color scheme and look technical but clean and modern, and use it for the background for all of the slides.
 </span>
 <span data-rw-start="312.479" data-rw-transcript-version="2">
 Again, Claude is using the replicate API to generate images using the new Nano Banana Pro, and it'll place them in the assets folder that we can preview over here. [music]
 </span>
 <span data-rw-start="328.479" data-rw-transcript-version="2">
 Let's actually darken the background
 </span>
 <span data-rw-start="330.08" data-rw-transcript-version="2">
 image. It's a little too bright for my
 </span>
 <span data-rw-start="331.919" data-rw-transcript-version="2">
 taste.
 </span>
</p>
<p>
 <span data-rw-start="334.479" data-rw-transcript-version="2">
 Now, let's create a voice-over for the
 </span>
 <span data-rw-start="337.039" data-rw-transcript-version="2">
 video. First, let's come up with a draft
 </span>
 <span data-rw-start="340.32" data-rw-transcript-version="2">
 script. Each slide should say step one,
 </span>
 <span data-rw-start="345.188" data-rw-transcript-version="2">
 [music], then the text, like add some
 </span>
 <span data-rw-start="347.36" data-rw-transcript-version="2">
 diagrams, and then make some kind of
 </span>
 <span data-rw-start="349.759" data-rw-transcript-version="2">
 comment relative to the slide.
 </span>
 <span data-rw-start="353.36" data-rw-transcript-version="2">
 Let's try to make it a little funnier.
 </span>
 <span data-rw-start="355.014" data-rw-transcript-version="2">
 [music].
 </span>
 <span data-rw-start="357.199" data-rw-transcript-version="2">
 That looks great. Now let's generate the
 </span>
 <span data-rw-start="359.52" data-rw-transcript-version="2">
 voice-over using 11 Labs.
 </span>
 <span data-rw-start="369.68" data-rw-transcript-version="2">
 So now we can preview those audio files
 </span>
 <span data-rw-start="372.4" data-rw-transcript-version="2">
 in our assets folder.
 </span>
 <span data-rw-start="376.16" data-rw-transcript-version="2">
 See what it sounds like.
 </span>
 <span data-rw-start="377.44" data-rw-transcript-version="2">
 &gt;&gt; How to explain things to programmers.
 </span>
 <span data-rw-start="379.919" data-rw-transcript-version="2">
 Spoiler, it's not with words.
 </span>
 <span data-rw-start="383.759" data-rw-transcript-version="2">
 &gt;&gt; Okay, and [music], it's already added the
 </span>
 <span data-rw-start="386.8" data-rw-transcript-version="2">
 audio to our slides. However, we need to
 </span>
 <span data-rw-start="389.919" data-rw-transcript-version="2">
 update the durations and timings for
 </span>
 <span data-rw-start="393.039" data-rw-transcript-version="2">
 everything to line up nicely. Run the
 </span>
 <span data-rw-start="395.12" data-rw-transcript-version="2">
 /transcribe command on each clip to
 </span>
 <span data-rw-start="397.44" data-rw-transcript-version="2">
 generate word-level timestamps. Next,
 </span>
 <span data-rw-start="400.24" data-rw-transcript-version="2">
 update the transition durations for each
 </span>
 <span data-rw-start="403.6" data-rw-transcript-version="2">
 Animation so that the different text
 </span>
 <span data-rw-start="406.24" data-rw-transcript-version="2">
 fades in at the correct time. [music]
 </span>
 <span data-rw-start="411.12" data-rw-transcript-version="2">
 This command uses the Deepgram API to
 </span>
 <span data-rw-start="413.759" data-rw-transcript-version="2">
 generate word-level timestamps.
 </span>
</p>
<p>
 <span data-rw-start="421.824" data-rw-transcript-version="2">
 [music]
 </span>
 <span data-rw-start="423.52" data-rw-transcript-version="2">
 Then, once you're done, you just click
 </span>
 <span data-rw-start="425.52" data-rw-transcript-version="2">
 render.
 </span>
 <span data-rw-start="427.719" data-rw-transcript-version="2">
 [music] And here's the final video in
 </span>
 <span data-rw-start="429.52" data-rw-transcript-version="2">
 all its glory.
 </span>
</p>
<p>
 <span data-rw-start="431.84" data-rw-transcript-version="2">
 &gt;&gt; How to explain things to programmers.
 </span>
 <span data-rw-start="434.319" data-rw-transcript-version="2">
 Spoiler, it's not with words. Step one,
 </span>
 <span data-rw-start="438.319" data-rw-transcript-version="2">
 add some diagrams. Programmers are
 </span>
 <span data-rw-start="440.88" data-rw-transcript-version="2">
 visual creatures. We can't read
 </span>
 <span data-rw-start="443.28" data-rw-transcript-version="2">
 documentation, but we'll stare at a
 </span>
 <span data-rw-start="445.12" data-rw-transcript-version="2">
 flowchart for hours. Step two, show some
 </span>
 <span data-rw-start="448.56" data-rw-transcript-version="2">
 code. Forget paragraphs. Just throw in a
 </span>
 <span data-rw-start="451.28" data-rw-transcript-version="2">
 code snippet and watch their eyes light
 </span>
 <span data-rw-start="452.88" data-rw-transcript-version="2">
 up like it's Christmas morning. Step
 </span>
 <span data-rw-start="455.28" data-rw-transcript-version="2">
 three, sprinkle in some AI because
 </span>
 <span data-rw-start="458.24" data-rw-transcript-version="2">
 nothing says I'm a serious professional
 </span>
 <span data-rw-start="460.479" data-rw-transcript-version="2">
 like generating a video of a glowing
 </span>
 <span data-rw-start="462.4" data-rw-transcript-version="2">
 robot brain. Thanks for watching. Now go
 </span>
 <span data-rw-start="465.36" data-rw-transcript-version="2">
 explain something to a programmer. Good
 </span>
 <span data-rw-start="467.199" data-rw-transcript-version="2">
 luck.
 </span>
</p>
<p>
 <span data-rw-start="468.479" data-rw-transcript-version="2">
 &gt;&gt; So that's the workflow. I'm curious,
 </span>
 <span data-rw-start="470.639" data-rw-transcript-version="2">
 What kind of videos would you make with
 </span>
 <span data-rw-start="472.16" data-rw-transcript-version="2">
 something like this? If you'd like a
 </span>
 <span data-rw-start="474" data-rw-transcript-version="2">
 deeper tutorial, let me know in the
 </span>
 <span data-rw-start="475.759" data-rw-transcript-version="2">
 comments.
 </span>
</p>
<p>
 <span data-rw-start="477.599" data-rw-transcript-version="2">
 [Music] For me, this isn't
 </span>
 <span data-rw-start="480.08" data-rw-transcript-version="2">
 about AI-generated content. It's about
 </span>
 <span data-rw-start="482" data-rw-transcript-version="2">
 removing friction so you can focus on
 </span>
 <span data-rw-start="484.24" data-rw-transcript-version="2">
 what you actually want to say.
 </span>
</p>