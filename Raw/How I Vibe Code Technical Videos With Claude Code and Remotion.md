---
categories:
  - "[[Clippings]]"
domain: [ai-agents]
tags:
  - media-gen
  - tools
source: readwise
created: 2026-06-23
rating: 
action: 
---

# How I Vibe Code Technical Videos With Claude Code and Remotion

![rw-book-cover](https://i.ytimg.com/vi/z7Bkf3Vc63U/sddefault.jpg)

## Metadata
- Author: [[John Hartquist]]
- Full Title: How I Vibe Code Technical Videos With Claude Code and Remotion
- Category: #articles
- Summary: John Hartquist shows how he makes and edits technical videos using Claude Code and Remotion. This method automates video tasks with code, making the process faster and easier. It helps focus on content, not tedious editing.
- URL: https://www.youtube.com/watch?v=z7Bkf3Vc63U&t=37s

## Full Document
In this video, I'm going to show you howI create and edit videos with naturallanguage using Claude Code and Remotion.If you've ever tried creating videos,even simple ones, you know [music] thepain. Scrubbing through timelinefootage, slicing out the awkward pauses,gathering all the assets, sequencingthem in the right place, [music]exporting. It's tedious, time-consuming,and it breaks your flow. [music]As a software engineer, I use Cloud Codeevery day to help me understand codebases, [music] track down bugs, and vibecode. I mean, architect new features. Ialso use it to automate workflows andquickly [music] spin up prototypes. Itcan be a very powerful tool. Recently,I've been experimenting with Remotion,which is a React library for renderingvideos programmatically frame [music] byframe. Here's the thing. Cloud Code isreally good at writing React code. Reactis one of the most popular webframeworks today, and Claude excels at.

Creating visuals with it. When youcombine Cloud Code with Remotion, youcan automate the tedious parts of videoediting in a similar way to how it'sused for general programming. I'm mainlyinterested in creating technical videos,tutorials, demos, that sort of thing.With Remotion, you get all the benefitsof the web ecosystem. Code snippets withsyntax highlighting, diagrams, smoothanimations, anything you can build withReact. With Cloud Code, you also get thefull power of MCP servers. I can tellClaude to use the Playwright MCP to opena browser, navigate [music] to adocumentation page, and take ascreenshot. Then that goes straight intomy video. With the replicate MCP, I canuse a library of models to generateaudio, images, B-roll footage, or eventalking head videos using tools such asNano Banana, VO3, 11 Labs, etc. Allwithout leaving the command line.[music] And because it's all code-based, I can create reusable templates.

and tweak them just by telling Claudewhat I want. [music] Everything isstored in Git, and I can continue usingthe tools that I already love. I've puttogether a Claude and Remotion startertemplate that you can use to make yourown videos. The link is in thedescription.After downloading the code from GitHuband installing the dependencies, we canrun Cloud straight away.

Run the dev server in the background.This pulls up the Remotion Studio whereyou can preview while editing the video.[music] There's a few examples includedfor reference. So, we can see this onehas a title segment and then a contentsegment.And then there's also some pre-builtcomponents with some previews. Forexample, a title slide with a fade-in[music] content slide. Let's add a titleslide that says how to explain things toprogrammers.Let's create a new step component. OnEach step, we'll have the text in thetop left say step one [music] and thensome supporting text. We'll have threesteps. Step one, add some diagrams. Steptwo, show some code. [music] Step three,sprinkle in some AI.

[music]For step one, let's add a fancy mermaiddiagram. [music]For step two, let's add a code snippetfrom this repository and have it animateover time.

[music]For step three, let's generate a video.

Generate a 6-second clip of the mostadvanced AI imaginable.For this step, Claude is going to useour generate video command, which callsthe replicate API, and we'll generate avideo using VO3.1 fast by default.[music] We can look in our assets folderhere. Once the video is ready, it'llshow up and we can preview it.[music]Okay, let's preview that video.

Cool.And [snorts] back to ourcomposition. It looks a little small.Let's make the video a little bit bigger.[music]Let's add one more slide to the end that just says, "Thanks for watching.">> [music]>> Let's update the font to be monospace and update the color scheme to be groove box.Make sure the text is centered on the first title slide.Maybe make the font slightly smaller.Let's generate a better background image. It should still follow the groove box color scheme and look technical but clean and modern, and use it for the background for all of the slides.Again, Claude is using the replicate API to generate images using the new Nano Banana Pro, and it'll place them in the assets folder that we can preview over here. [music]Let's actually darken the backgroundimage. It's a little too bright for mytaste.

Now, let's create a voice-over for thevideo. First, let's come up with a draftscript. Each slide should say step one,[music], then the text, like add somediagrams, and then make some kind ofcomment relative to the slide.Let's try to make it a little funnier.[music].That looks great. Now let's generate thevoice-over using 11 Labs.So now we can preview those audio filesin our assets folder.See what it sounds like.>> How to explain things to programmers.Spoiler, it's not with words.>> Okay, and [music], it's already added theaudio to our slides. However, we need toupdate the durations and timings foreverything to line up nicely. Run the/transcribe command on each clip togenerate word-level timestamps. Next,update the transition durations for eachAnimation so that the different textfades in at the correct time. [music]This command uses the Deepgram API togenerate word-level timestamps.

[music]Then, once you're done, you just clickrender.[music] And here's the final video inall its glory.

>> How to explain things to programmers.Spoiler, it's not with words. Step one,add some diagrams. Programmers arevisual creatures. We can't readdocumentation, but we'll stare at aflowchart for hours. Step two, show somecode. Forget paragraphs. Just throw in acode snippet and watch their eyes lightup like it's Christmas morning. Stepthree, sprinkle in some AI becausenothing says I'm a serious professionallike generating a video of a glowingrobot brain. Thanks for watching. Now goexplain something to a programmer. Goodluck.

>> So that's the workflow. I'm curious,What kind of videos would you make withsomething like this? If you'd like adeeper tutorial, let me know in thecomments.

[Music] For me, this isn'tabout AI-generated content. It's aboutremoving friction so you can focus onwhat you actually want to say.
