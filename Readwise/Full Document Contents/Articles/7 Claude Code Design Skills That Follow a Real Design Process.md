# 7 Claude Code Design Skills That Follow a Real Design Process

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*S9O3eN9BgqBVV8-uOUnvvA.png)

## Metadata
- Author: [[Julian Oczkowski]]
- Full Title: 7 Claude Code Design Skills That Follow a Real Design Process
- Category: #articles
- Summary: Julian Oczkowski shows that AI changes how design work happens by replacing the whole process, not just tools. He created seven Claude Code skills that follow a real design process from planning to review, making AI design reliable and structured. This approach helps designers use AI with clear steps, avoiding chaos and improving quality.
- URL: https://medium.com/@julian.oczkowski/7-claude-code-design-skills-that-follow-a-real-design-process-b871b8673d05

## Full Document
![]()
I have been designing for 29 years. I have worked as an individual contributor, a design manager, and a dev team lead across enterprise companies like Adobe, IBM, and Danone. I have seen tools come and go. Sketch replaced Photoshop. Figma replaced Sketch. Each time, the tooling changed but the process underneath stayed the same.

AI is different. AI is not just replacing the tool. It is replacing the process. And most people are skipping straight to the fun part, typing a prompt and watching code appear, without thinking about what comes before.

That is how you get faster chaos.

#### The problem with “prompt and pray”

Open Claude Code. Type “build me a dashboard.” Watch it generate something. It looks decent. Maybe even impressive.

But ask yourself: does it solve the right problem? Does it match the user’s mental model? Are the information architecture decisions intentional or random? Are the design tokens consistent or did the LLM just pick whatever looked good in the moment?

![]()
Most of the time, the answer is no. The output looks like software but does not feel like software. It is missing the invisible work that separates a prototype from a product.

That invisible work is the design process. Requirements gathering. Design briefs. Information architecture. Design tokens. Task decomposition. Review cycles. It is not glamorous. It is not the part people post on X. But it is the part that makes everything else work.

#### What I built: 7 Claude Code skills that follow a real design process

Instead of fighting this, I decided to encode the process into Claude Code itself. I built 7 custom skills that you can install and run in any project. They follow a professional design workflow from vague idea to working, accessible, reviewed frontend.

Here is the full flow.

![]()
#### 1. Grill Me

This is the most important skill and probably the shortest one in terms of code. The LLM becomes relentless. It stress-tests your requirements before a single line of code gets written.

You might spend 20 minutes answering questions. That is the point. If you cannot articulate what you are building and why, the LLM should not be building it for you. This skill uses decision trees to probe deeper based on your answers: what type of application, who are the users, what is the scale, what are the edge cases.

The output is a grill summary that captures everything you discussed. Think of it as the requirements handshake between you and the LLM.

![]()
Credit where it is due: the grill-me concept was inspired by Matt Pocock’s skills work at [github.com/mattpocock/skills](https://github.com/mattpocock/skills). I took the idea and adapted it for a designer’s workflow.

#### 2. Design Brief

Once the grill is done, the LLM generates a design brief. But it does not just summarise your answers. It looks through the actual codebase. It checks for existing components, design systems, patterns already in the repository.

Before creating the brief, it asks design-specific questions. Not just what the application needs to do, but how you want it to feel. Emotional tone. Visual inspiration. It might suggest references like Linear or the Google Admin Console based on your domain.

The result is a proper design brief document saved to your project.

![]()
#### 3. Information Architecture

The LLM goes through all the documentation generated so far and structures the information architecture. Pages, navigation patterns, content hierarchy. If the feature is complex, like a multi-page flow or a full navigation redesign, it will ask additional clarifying questions before committing.

![]()
#### 4. Design Tokens

If your project does not already have a design system with components in the repository, this skill generates a complete set of design tokens as CSS custom properties. Colours, typography, spacing, elevation, border radius. Everything saved to a theme file that the frontend skill will consume later.

If you already have a design system, this step gets skipped automatically. The brief skill detected it earlier.

![]()
#### 5. Brief to Tasks

This is where the design brief gets broken down into actionable tasks. The skill reads all the documentation, identifies dependencies between tasks, and creates a separate markdown file that tracks every task with its status.

Foundation tasks first, then core UI, then responsive and polish. Each task has a clear scope and the LLM knows what order to execute them in.

![]()
#### 6. Frontend Design

This is the build phase. The LLM uses the design brief, information architecture, design tokens, and task list to generate the actual frontend. Components, pages, layouts. Not random code. Intentional code that follows the decisions made in the previous five steps.

The output is a working application. In my demo, I started with nothing more than “I want an asset management application” and ended up with a complete IT asset management tool with a dashboard, asset tracking, categories, reports, filtering, sorting, empty states, edit dialogs, and proper navigation.

![]()
#### 7. Design Review

Once the frontend is generated, the design review skill analyses the output. You can either paste screenshots into Claude Code manually or, better yet, use a Playwright MCP server to automate the entire review.

With Playwright, Claude Code opens a headless browser, navigates through the application, takes screenshots of every page, and then runs the design review skill against those screenshots autonomously. No manual work.

The review catches things like sparse layouts, incorrect chart ordering, missing dark mode considerations, and accessibility gaps. It then proposes specific changes and can apply them directly.

![]()
#### The result

From a vague one-line prompt to a working application with:

* 91 Lighthouse performance score
* 100 Lighthouse accessibility score
* Proper information architecture
* Consistent design tokens
* Documented design brief and task tracking

Not because the LLM is magic. Because it followed a process.

![]()
#### Why this matters for designers right now

The old design process, or the pseudo-process that most teams actually followed, is gone. AI tools are getting better and faster every month. But speed without direction just means you waste time faster.

I have seen this from both sides. As an IC shipping work, and as a manager reviewing it. The people who will thrive with AI tools are the ones who bring process, judgment, and accountability. The tools handle execution. You handle the “what” and the “why.”

That is what these skills encode. Not shortcuts. A professional design process that happens to run inside a terminal.

#### Try it yourself

The skills are free and open source. Install them in any Claude Code project with a single command:

```
npx skills add julianoczkowski/designer-skills
```

GitHub repo: [github.com/julianoczkowski/designer-skills](https://github.com/julianoczkowski/designer-skills)

Some content could not be imported from the original document. [View content ↗](https://medium.com/@julian.oczkowski/7-claude-code-design-skills-that-follow-a-real-design-process-b871b8673d05) 

I walk through the entire process from start to finish in a video on my channel, AI For Work. If you want to see every step running live, including the Playwright MCP autonomous review, it is all there.

If you are a designer, whether you are just starting out or you have been doing this for decades, the shift is happening. The question is not whether AI will change your work. It is whether you will bring process to the chaos or just let the chaos run faster.

*Julian Oczkowski is a designer with 29 years of experience across enterprise companies, startups, and agencies. He runs the AI For Work YouTube channel, covering AI tool comparisons, workflow demos, and practical builds for designers and individual contributors.*

*YouTube:* [*youtube.com/@aiforwork\_app*](https://www.youtube.com/@aiforwork_app)
