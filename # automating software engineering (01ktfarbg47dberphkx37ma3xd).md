---
categories:
  - "[[Resources]]"
domain: engineering
title: "# automating software engineering"
source: "https://x.com/karpathy/status/1767598414945292695/?rw_tt_thread=True"
author: "Andrej Karpathy"
published: 2024-03-12
created: 2026-06-06
description: "# automating software engineering"
tags:
  - to-process
  - agent-tools
---

# automating software engineering

  
In my mind, automating software engineering will look similar to automating driving. E.g. in self-driving the progression of increasing autonomy and higher abstraction looks something like:

  
2. first the human performs all driving actions manually
  
4. then the AI helps keep the lane
  
6. then it slows for the car ahead
  
8. then it also does lane changes and takes forks
  
10. then it also stops at signs/lights and takes turns
  
12. eventually you take a feature complete solution and grind on the quality until you achieve full self-driving.
  

  
There is a progression of the AI doing more and the human doing less, but still providing oversight. In Software engineering, the progression is shaping up similar:

  
2. first the human writes the code manually
  
4. then GitHub Copilot autocompletes a few lines
  
6. then ChatGPT writes chunks of code
  
8. then you move to larger and larger code diffs (e.g. Cursor copilot++ style, nice demo here <https://t.co/u8ueY0mGxZ>)


5....

Devin is an impressive demo of what perhaps follows next: coordinating a number of tools that a developer needs to string together to write code: a Terminal, a Browser, a Code editor, etc., and human oversight that moves to increasingly higher level of abstraction.  
  
There is a lot of work not just on the AI part but also the UI/UX part. How does a human provide oversight? What are they looking at? How do they nudge the AI down a different path? How do they debug what went wrong? It is very likely that we will have to change up the code editor, substantially.

In any case, software engineering is on track to change substantially. And it will look a lot more like supervising the automation, while pitching in high-level commands, ideas or progression strategies, in English.

Good luck to the team!  






![](https://pbs.twimg.com/profile_images/1765909640364068865/MvH-m0gd.jpg)


[Cognition](https://twitter.com/cognition_labs)
[@cognition\_labs](https://twitter.com/cognition_labs)






Today we're excited to introduce **Devin, the first AI software engineer**.

Devin is the new state-of-the-art on the SWE-Bench coding benchmark, has successfully passed practical engineering interviews from leading AI companies, and has even completed real jobs on Upwork.

Devin is an autonomous agent that solves engineering tasks through the use of its own shell, code editor, and web browser.

When evaluated on the **SWE-Bench** benchmark, which asks an AI to resolve GitHub issues found in real-world open-source projects, Devin correctly resolves 13.86% of the issues unassisted, far exceeding the previous state-of-the-art model performance of 1.96% unassisted and 4.80% assisted.

Check out what Devin can do in the thread below.  


Your browser does not support the video tag.



[Posted Mar 12, 2024 at 1:50PM](https://twitter.com/cognition_labs/status/1767548763134964000)