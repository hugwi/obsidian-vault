---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - skills
source: readwise
created: 2026-06-23
rating: 
action: 
theme: human-ux-frontend
subtheme:
  - design-systems-ui
  - ide-chat-ux
---

# Introducing /visual-plan - rich plans for Claude Code + Codex

![rw-book-cover](https://i.ytimg.com/vi/NE0aBuQF0HA/sddefault.jpg)

## Metadata
- Author: [[Steve (Builder.io)]]
- Full Title: Introducing /visual-plan - rich plans for Claude Code + Codex
- Category: #articles
- Document Tags: [[add]] 
- Summary: Steve created a tool called visual plan that makes coding plans easy to understand with interactive visuals and diagrams. It helps catch mistakes early and improves teamwork by sharing clear, visual plans and recaps. The tool is open source, customizable, and works with GitHub to show visual summaries on pull requests.
- URL: https://m.youtube.com/watch?v=NE0aBuQF0HA&pp=ugUEEgJlbg%3D%3D#

## Full Document
Plan mode in Claude code is incredible,but I always find my eyes glazing overthis huge markdown essay in my terminal.And I've realized after I implementthings that I totally miss someimportant small details that were notclear to me at first because it was justtoo much stuff to read, honestly. I'vebeen experimenting with this new skill Imade called visual plan. It's somewhatinspired by that post about how HTML isbetter than markdown, but HTML can beslow and verbose to write, it doesn'tlook good checked into a repo, and Ifound I can make much better visual

plans with reusable components. So, Imade a skill called visual plan. Itgenerates plans as MDX with super visualcomponents, diagrams, API specs that areinteractive, schema design changes,annotated code, and even pan andzoomable wireframes. Every UI lets youlook at a wireframe first, comment onit, iterate, answer open questionsvisually and interactively, and then haveThe agent work. I found this to be amuch more intuitive interface for me toreason about what the agent's doing.

It's really made me feel like humans andengineering is kind of entering this newabstraction phase where we reason aboutthings at the plan level. As long as theplan's what we want, agents are gettingmore and more reliable executing onthat. Almost to the degree to which wetrust the C compiler to compile toassembly reliably. As long as the planis good, and we make the plan clear,consumable, like easy to understand,easy for people to reason about, share,comment, etc., more and more we cantrust the agents to implement it asexpected. I also made a skill for thereverse of this. I call it visual recap.

What it can do is after the agent works,give you a recap of everything it did.

The same idea. Wireframes, interactiveAPI specs and diffs, schemas, annotatedcode, etc. So, now when you're reviewingwhat the agent has done for you, orLooking at like a pull request forsomebody else's code, rather thanlooking at a small summary, or a supergranular line-by-line mess, you can seea visual recap. Interactive, easy,intuitive. You can even share these withothers to comment, and then pass thecomments and feedback to the agent toimprove. This has let me catch stuff waysooner.

So, before the agent doessomething I didn't realize, becausemaybe the text sounded fine, but thewireframe makes me realize, "Oh, wait.No, that's not what I had in mind." Orin just a more clear and visual way, Isee what types of APIs I want to create.And I’d like them shaped differently.I'm able to catch stuff earlier as wellas afterwards in recaps of my work orsomeone else's work. I can match yourthings that maybe aren't as obvious inthe code, just looking at like React andTailwind code, are actually what Iwanted or expected before it goes out toGoing, "Oh, wait a second. This is notwhat I had in mind. That's not what Ithought I told the agent. That's notwhat I thought I saw in the code." AndI'll be honest, it's tedious tohand-test every single thing every time.

Having a snapshot at a glance that'sclear, and I can interactively drillinto, to me has been a game-changercompared to just static markdown. Andall of this stuff is customizable. Youcan add your own components, customizethe components. It's MDX. It's a betterformat for checking in. It can do waymore cool things, and there'sconsistency, too. It's not just randomHTML every time. This move to MDX fromHTML from previously markdown, I thinkis the full circle that at least Ineeded. I'd much rather see MDX rawfiles in code versus HTML. And there'sso much more you can do with reusablecomponents than generating honestly kindof HTML slop every time, different everytime. It also means when you changeAgents or models, you get consistency aswell. I open-sourced all of this. Theskills, the application that generatesMDX that you can fork and customize with

your own components. You can check itout over on GitHub, install and try itout with the CLI I made, and I'd love toknow your feedback. Not just on do youlike the plans or the recaps or is ithandy, including the fact that you caninstall a GitHub action with the CLI,but also does this new idea of like howwe reason as engineers make sense. Ireally believe that the plan level isreally the real reasoning level thatwe're going to be thinking in, talkingin, and working in. And I want to makeit clear and beautiful and a goodexperience. So, as we trust agents moreto implement correctly and other agentscheck the work against the plan, againstthe implementation spec, we can workfaster, we can get our minds out of thedetails. Like how people don't look atassembly much anymore. They would reason.

At the level of C and that opened up allnew potential and abstractions and theability to move fast relative to before,but safely. And I think this opens upnew ways of collaborating. You can sharethe same thing with your productmanagers, designers, et cetera, makingit so you reason about it similar toyou. At least the areas that care aboutlike the design or the wireframe and thePM about the behavior. And one morething I think is cool is there's also aGitHub action I made that can run thisautomatically on every pull request andshow you a snapshot of a visual planright there in the comments every time.

You can click in and interact with tomake it easier more consumable to reviewpull requests. So again, it's not just achoice between a short description and along granular line by line, but actuallysee visuals, diagrams, interactive APIspecs, more consumable code and evenannotated code. Anyway, it's all freeand open source you can find on myGitHub. Let me know what you think.
