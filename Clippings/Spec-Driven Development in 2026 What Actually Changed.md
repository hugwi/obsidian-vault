---
title: "Spec-Driven Development in 2026: What Actually Changed"
source: https://www.youtube.com/watch?v=b6cbxSaa4U4
author:
  - "[[@peterjordanson4201]]"
published: 2026-04-22
created: 2026-06-30
description: One spec-driven framework grew 863% in six months. Another in the same category grew 18%. This is the honest six-month update on OpenSpec, BMAD, Spec Kit, Ag...
tags:
  - clippings
  - agentic-engineering
  - spec-driven-development
---
![](https://www.youtube.com/watch?v=b6cbxSaa4U4)

## Transcript

### Hook — +863% vs +18

**0:00** · One framework grew 863% over the last six months.

**0:05** · Another one in the same category grew 18.

**0:08** · Last October I made a video comparing three spec-driven development frameworks — BMAD, Spec Kit, and OpenSpec.

**0:16** · Later I covered Taskmaster and Agent OS in separate videos.

**0:20** · Eighty-six thousand of you watched the first one.

**0:23** · The combined GitHub stars of those five jumped from around eighty-seven thousand to two hundred and two thousand.

**0:30** · Plus one hundred and thirty-one percent in six months.

**0:34** · That part isn't the interesting number.

**0:36** · The interesting number is the spread.

**0:38** · Inside that same average, one framework ran away with it while another stalled.

**0:43** · One rewrote itself from scratch, and one quietly shrunk its own scope.

**0:48** · Spec-driven development gained momentum over the last six months — partly because the tools got better, partly because of marketing.

**0:56** · This video is the six-month update: What changed, who won, who stalled, and what the rest of the community has been saying.

**1:03** · No hands-on retest this time — that's a separate one, coming later.

### OpenSpec — the rocket

**1:13** · OpenSpec grew from four thousand one hundred stars in October to thirty-nine thousand five hundred now.

**1:20** · Plus eight hundred and sixty-three percent in six months.

**1:23** · The runaway story of the last half year.

**1:26** · Honestly, back when I first compared the three frameworks, I recommended Spec Kit.

**1:31** · What actually changed my mind wasn't the v1 release — it was what happened after I published the video.

**1:37** · I kept using both OpenSpec and Spec Kit on real work, and over a few weeks it became obvious OpenSpec was producing the same quality, just much faster.

**1:47** · Spec Kit was simply too slow to plan.

**1:49** · So I dropped Spec Kit and stuck with OpenSpec.

**1:51** · Then — and this is where it gets interesting — I eventually dropped even OpenSpec.

**1:56** · Claude Code's built-in plan mode started covering most of what I needed for day-to-day work, and Superpowers handled the bigger features.

**2:04** · OpenSpec didn't do anything wrong.

**2:06** · The native tooling just caught up.

**2:08** · The growth numbers suggest a lot of other people went through some version of that same funnel — which is part of why OpenSpec, the lightest-weight framework in the set, came out on top.

**2:19** · A lot changed on their side.

**2:20** · The v-one release is a significant rewrite — smaller output, clearer structure, less markdown sprawl.

**2:27** · The team also joined Y Combinator's Winter 26 batch and expanded tool compatibility to more than 25 agents and IDEs.

**2:36** · The community coverage matches the numbers.

**2:38** · Augment Code's ranking has it at number four out of six, but Augment Code's own product is ranked number one in the same list, so I wouldn't weight that placement too heavily.

**2:49** · Rick Hightower's piece consistently calls out OpenSpec as the lightest-ceremony option of the four he compared.

**2:56** · My own take: lightweight beats heavy when the frontier model is already doing most of the implementation work.

**3:03** · A small disclosure.

**3:04** · A lot of people at Toggl — where I work — use OpenSpec as their framework of choice.

**3:10** · A couple of enthusiasts even built an internal UI wrapper around it, essentially a Kanban-style board for OpenSpec workflows.

**3:18** · So factor that in.

**3:19** · I have a biased sample of one engineering organization.

**3:23** · Stars aren't a perfect metric either — YC cohorts and Hacker News spikes can juice them.

**3:29** · But plus eight hundred sixty-three percent is a lot, and that one's public, not mine to manipulate.

**3:35** · My honest take.

**3:36** · If you're coming to spec-driven development for the first time, OpenSpec is where I'd start.

**3:41** · It's fast.

**3:42** · It won't bury you in markdown before you write any code, and the community around it is growing faster than any of the original five I'm covering today.

**3:51** · That doesn't mean it's the right fit for every team.

**3:54** · BMAD's fans will tell you otherwise, and they have a point too.

**3:58** · But as a default starting position for a new team exploring the space — OpenSpec is the one I'd hand somebody first.

### BMAD — the heavy-agent rewrite

**4:04** · BMAD went from nineteen thousand one hundred stars to forty-four thousand four hundred.

**4:10** · Plus one hundred and thirty-three percent, which tracks with the rest of the market growth but doesn't lead it.

**4:16** · The interesting thing here isn't the raw number — it's what they shipped along the way.

**4:21** · Version six shipped back in February.

**4:24** · v6.0.0 came out on February 17th, and they've been pushing point releases ever since — v6.3 is from early April.

**4:34** · The stable six release was essentially a ground-up rewrite.

**4:38** · They consolidated several older agents into a single persona called Amelia, introduced what they call a Skills Architecture, and shipped a Cross-Platform Agent Team that works across more than twenty agent runtimes.

**4:53** · Twelve-plus specialized agent personas are available.

**4:56** · On top of that, the team spun out BMad Builder as its own project for building custom agents and workflows.

**5:03** · It's at v1.4 already.

**5:06** · Dev Loop Automation is another piece of the ecosystem.

**5:10** · There's also a small marketplace of community-contributed skills.

**5:13** · That's a lot of surface area.

**5:15** · Community reception is mostly positive on the technical side.

**5:19** · On the critical side, the most common complaint is the ceremony itself: the number of markdown files per spec, the full PM-to-developer handoff rituals, and a PRD phase that asks you to define business success metrics for a weekend project.

**5:34** · That's the tradeoff BMAD has always made.

**5:37** · And by the way — no wonder so many BMAD fans showed up in the comments of my last video to defend it.

**5:43** · The community around this one runs hot.

**5:45** · BMAD has one of the most active communities on this leaderboard; their Discord usually has close to two thousand people online at any given time, which is genuinely a lot for a framework this specialized.

**5:58** · I'm not going to claim it's literally the biggest without doing a head-count across every project, but it's among the most active, easily.

**6:05** · Quick disclosure on my own side.

**6:07** · I did re-test BMAD v6 fairly recently — the full four-phase flow, which is the actual ceremony: Planning, Solutioning, Implementation, all of it.

**6:16** · The results weren't great.

**6:18** · Seven hours to build a cat game I could build in ten minutes with plan mode.

**6:22** · I have a separate video on that whole experience, linked below.

**6:26** · A fair number of viewers in the comments made a point worth repeating: BMAD is designed for bigger project scopes, and a small test project doesn't let it show what it can actually do.

**6:36** · That's a legitimate critique.

**6:38** · I'm not going to rerun the full four-phase ceremony on a bigger project though — that would cost me another eight to twenty hours, and I'd rather keep my weekends.

**6:47** · What I do want to retest is Party Mode and Quick Flow, on a larger scope, and see whether the lighter-touch modes hold up better than the heavy one did.

**6:56** · That'll be its own video — hit subscribe if you don't want to miss it.

**7:00** · My honest take.

**7:01** · BMAD isn't really a team tool — I don't think "for teams" is even the right framing.

**7:06** · What kind of team is this, where each member orchestrates their own nested squad of virtual PM, architect, and developer agents?

**7:14** · BMAD is for individual builders who genuinely want the full agile ritual layered on top of their AI coding setup.

**7:21** · Solo devs, serious vibe coders, agent orchestrators — whatever we're calling them this month.

**7:27** · If you like structured multi-agent workflows and don't mind reading spec documents, this is the one.

**7:32** · Spec Kit grew from thirty-nine thousand three hundred stars to eighty-seven thousand five hundred.

### Spec Kit — the GitHub-backed one

**7:42** · Plus one hundred and twenty-three percent.

**7:45** · That's a huge raw number — almost fifty thousand new stars — and it puts Spec Kit at the top of the leaderboard in absolute stars by a comfortable margin.

**7:54** · What GitHub shipped.

**7:55** · One hundred and thirty-six releases since October.

**7:58** · Support for more than fourteen AI agent platforms — Claude Code, Cursor, Windsurf, Copilot, and a long tail of smaller agents.

**8:06** · Microsoft also published an official Spec Kit training module on Microsoft Learn.

**8:11** · Other SDD frameworks have courses on platforms like Udemy, sure, but the Microsoft Learn module signals something different in an enterprise context.

**8:20** · The creator, Den Delimarsky, also left Microsoft, where he built Spec Kit as a GitHub project — for Anthropic, along the way.

**8:28** · Could be read as a founder leaving the project; could be read as a vote of confidence in where AI-assisted development is going more broadly.

**8:36** · Probably a bit of both.

**8:38** · Community reception is mixed.

**8:40** · Martin Fowler's analysis of Spec Kit was the sharpest critique in the space.

**8:44** · His observation: Spec Kit generates eight-plus markdown files per spec, and in his words, those files were "repetitive, verbose and tedious to review."

**8:53** · His closer — and this is verbatim — was "I'd rather review code than all these markdown files."

**8:59** · He also noted that agents frequently ignored the instructions in those specs.

**9:04** · Augment Code's ranking puts Spec Kit at number three out of six.

**9:08** · Rick Hightower's comparison describes it as middle-ground execution — it executes through the connected AI, but it doesn't manage parallelism the way frameworks like GSD do.

**9:18** · My honest take.

**9:19** · Spec Kit is faster than BMAD.

**9:21** · It's also noticeably slower than OpenSpec.

**9:24** · The difference isn't really about structure.

**9:27** · When I ran Spec Kit back in October, the output quality felt about the same as OpenSpec's, just arriving inside a much larger pile of markdown.

**9:36** · And that plan phase — I remember it took around five minutes just to complete planning, which felt incredibly slow compared to OpenSpec finishing the same step in a fraction of the time.

**9:46** · My instinct — and I'll be upfront this is instinct, not a proven claim — is that a meaningful chunk of Spec Kit's growth comes from GitHub's brand and Microsoft's Learn module, not from the product being the best on merit.

**9:58** · I'd love to see some real-world comparisons that confirm or deny that.

**10:02** · Remember the thesis from the hook: momentum from actual tools.

**10:06** · Momentum from marketing.

**10:08** · Spec Kit is probably where the marketing side of that shows up most clearly.

**10:12** · If you're considering Spec Kit, test it yourself against OpenSpec on a real task before committing a team to it.

**10:19** · Go in with eyes open about what you're buying.

### Agent OS — the skeptic's pick

**10:22** · Agent OS went from roughly 2500 stars to 4300, about plus 72%, which sounds healthy in isolation, but in a market that more than doubled.

**10:34** · It's the slowest growth story on the leaderboard.

**10:37** · And the repository activity tells you why.

**10:40** · The last release — version three — shipped on January 20th, which was three months ago, and there's been nothing since.

**10:47** · For comparison, Spec Kit has shipped around 40 releases in the same three months.

**10:52** · BMAD ships weekly to biweekly.

**10:54** · OpenSpec ships weekly, and even Taskmaster manages a release every few weeks.

**10:59** · Agent OS has gone completely quiet.

**11:02** · In practical terms, the project looks abandoned.

**11:05** · What did ship was version three, and this is the interesting part.

**11:09** · V3 was an explicit, public downsizing of the framework.

**11:13** · The creator, Brian Casel, was direct about the reason in his changelog — frontier models, which is the industry's term for the large models like Claude and GPT that sit at the top of the capability curve, now handle a lot of what earlier Agent OS versions were built to handle — spec writing, task breakdown, implementation orchestration, all of it.

**11:35** · So V3 intentionally retired those phases and refocused the framework on what Casel calls its core strength: establishing and injecting standards.

**11:44** · The V3 commands reflect that — /discover-standards, /inject-standards, /index-standards, /shape-spec, and /plan-product.

**11:52** · Five commands, narrow scope, clear purpose.

**11:55** · Community coverage is thin.

**11:57** · If you go looking for Agent OS in the comparison pieces — Rick Hightower, Augment Code, Vishal Mysore's map of thirty-plus frameworks — it mostly gets a brief mention.

**12:07** · It's no longer one of the frameworks people are actively comparing.

**12:11** · Now, my honest take, and this is where I want to be careful.

**12:14** · The headline question I had going in was: what does Agent OS actually give me in twenty twenty-six that CLAUDE.md files and Claude Code's built-in skills and plan mode don't already provide?

**12:26** · Standards enforcement used to be something you needed a dedicated framework for.

**12:31** · Now the coding tool itself handles a lot of it.

**12:34** · But reading Casel's V3 rationale, the steel-man is actually reasonable — Agent OS isn't trying to replace plan mode, it's trying to layer on top of it by making standards discovery and injection more automatic.

**12:47** · /inject-standards can bake your rules into Claude Skills, subagents, or any prompt, which is genuinely more sophisticated than pasting them into a CLAUDE.md file by hand.

**12:57** · So there's a real value proposition if standards automation is specifically what you need.

**13:02** · Whether that's worth adopting a whole framework for, given that the project hasn't pushed a release in three months — that's the question I'd weigh carefully.

**13:11** · If you're using V3 and it's working for you, drop a comment.

**13:14** · I'd genuinely like to hear from people it's clicking for.

**13:18** · And one thing I'll say for Casel: shipping a smaller V3, instead of pretending the tool still does what it used to do, is respectable.

**13:26** · Not every maintainer would make that call.

### Taskmaster — the stall

**13:29** · Taskmaster went from 22,500 stars to 26,500.

**13:35** · Plus 18%.

**13:36** · In a market where the average framework grew more than 100%, plus 18 is effectively going backwards.

**13:43** · And this is the one that surprised me most on the leaderboard, because six months ago, Taskmaster was arguably the most convenient framework of the set.

**13:52** · What happened.

**13:53** · A few things, in combination.

**13:55** · The project moved from the original repository into a dedicated one.

**13:59** · The team launched a commercial layer called Hamster over at tryhamster.com — a paid offering built around the same task-decomposition engine.

**14:08** · The license on the open-source side is MIT plus a Commons Clause rider, which restricts commercial resale.

**14:15** · That has actually been the case for a while — Taskmaster wasn't pure MIT to begin with — but it's worth noting that among all the frameworks on this leaderboard, Taskmaster is the only one that isn't pure MIT.

**14:27** · Around this same period, the community also raised concerns about Sentry telemetry calls getting shipped on by default with an opt-out rather than opt-in.

**14:36** · Release cadence also slowed — Taskmaster ships roughly every few weeks.

**14:41** · Now, closer to monthly than weekly.

**14:43** · Community coverage is still positive on the technical side.

**14:46** · Rick Hightower's comparison explicitly says Taskmaster "shines at the decomposition layer" — turning product requirements documents into dependency-aware task graphs.

**14:57** · That part of the tool really does work well.

**14:59** · The results Taskmaster produces are, in my experience back when I tested it, genuinely good.

**15:05** · The engine is solid.

**15:07** · My honest take.

**15:08** · When I used Taskmaster six months ago, I thought it was the most convenient of the frameworks I tried.

**15:13** · And the code it produced was actually good — I want to be fair to the tool, because the output was not the problem.

**15:20** · The developer experience was fine overall, honestly.

**15:23** · But over time I noticed two specific things I wish worked better.

**15:27** · First, the way Taskmaster scopes tasks — it uses tags, where you have separate buckets like a master tag and whatever custom ones you create on top.

**15:36** · Switching between them never felt natural to me.

**15:39** · It could be smoother.

**15:40** · Second, the tasks themselves are stored in JSON files.

**15:43** · You can absolutely read them in the terminal when you run the CLI commands — that part is fine.

**15:49** · But opening the raw JSON in an editor and trying to skim through it is not a pleasant experience.

**15:54** · Both of those are fixable, and neither is a dealbreaker.

**15:58** · The engine is solid.

**15:59** · So the core tool still works.

**16:01** · But you combine the commercial pivot, the license situation, the telemetry concern, and the slower release cadence — and you can see why the star growth stalled.

**16:11** · It's an interesting case study in monetization timing.

**16:14** · Taskmaster was growing well when the commercial pivot happened.

**16:17** · Twelve months from now there'll probably be a blog post from somebody — a proper teardown — arguing either that the pivot saved the project or that it stalled it.

**16:27** · Right now, based on the numbers, the stall side of that argument is winning.

### New players and native features

**16:32** · While the original five were busy rewriting themselves or going commercial, the space around them kept expanding.

**16:39** · A couple of new projects have grown large enough that you can't really talk about spec-driven development in 2026 without mentioning them.

**16:47** · Superpowers, by Jesse Vincent.

**16:49** · One hundred and fifty-six thousand stars — more than any single one of the five I just covered.

**16:55** · Superpowers isn't strictly a spec-driven framework.

**16:58** · It's an agentic skills system for Claude Code that enforces test-driven development and a structured brainstorm-plan-execute workflow.

**17:06** · It's adjacent to SDD rather than squarely inside it.

**17:10** · But it's the largest structured-AI-coding project on GitHub right now, and I use it personally, daily, alongside plan mode.

**17:18** · When I have a big feature to plan, Superpowers asks many more questions than plan mode does.

**17:23** · I already have a full video on Superpowers — link in the description if you want the deeper walk-through.

**17:29** · GSD — Get Shit Done, by TACHES.

**17:31** · Fifty-one thousand six hundred stars.

**17:34** · This one is execution-first.

**17:36** · Wave-based parallel orchestration, fresh context windows for researchers and planners and executors, all coordinated by a top-level runtime.

**17:45** · Forty-seven releases since December.

**17:47** · A different model from most of the leaderboard — GSD is more about running specs than writing them, with parallel agent contexts doing the actual work.

**17:56** · Beads, by Steve Yegge.

**17:58** · Twenty thousand eight hundred stars and the maintainer is still pushing commits — last push was a couple of days ago.

**18:04** · Beads is a distributed graph issue tracker for AI agents, backed by Dolt, which is a version-controlled SQL database.

**18:12** · Their pitch is literally "replaces messy markdown plans with a dependency-aware graph."

**18:17** · It sits in Taskmaster's category — task tracking and agent memory — but without the Commons Clause license and with a sharper thesis.

**18:25** · A few of you have asked me to look at Beads.

**18:28** · This is my brief flag: interesting, I want to try it properly, it'll be its own video.

**18:33** · And then there's the native-features side of this story, which is the thing that changed most quietly.

**18:38** · Claude Code itself now ships with skills, plan mode, ultra plan mode — that last one is a newer addition — and CLAUDE.md files for project-level standards.

**18:47** · A lot of what the smaller spec-driven frameworks were built to provide — planning structure, standards enforcement, multi-agent coordination — has been absorbed into the coding tool you're already running.

**18:59** · That's part of why some of these frameworks are growing slower than you'd expect.

**19:03** · The competition isn't other frameworks anymore.

**19:06** · It's the tools they sit on top of.

**19:08** · Vishal Mysore mapped more than thirty agentic coding frameworks in a March Medium piece.

**19:14** · The space is crowded.

**19:15** · A lot of these projects won't make it through another six months.

**19:19** · The ones that do will be the ones with strong communities or a clear reason to exist alongside the native features.

### Community sentiment

**19:26** · Spec-driven development now has a Wikipedia page.

**19:29** · It has four papers on arXiv — that's the open-access preprint server academics use to publish research before formal peer review.

**19:38** · Four of them in the first quarter of this year alone.

**19:41** · Thoughtworks put SDD on their Technology Radar in the "Assess" category.

**19:45** · Six months ago, the idea was still something you argued about on X.

**19:50** · Today it's a topic for conference keynotes and enterprise rollouts.

**19:54** · Martin Fowler wrote a long, cautiously skeptical analysis — he uses a German word for "making things worse through attempted improvement," which I'm not going to try to pronounce on camera.

**20:06** · His bigger worry is that SDD reminds him of model-driven development.

**20:11** · Quick context: model-driven development was a nineties movement where you'd draw diagrams and generate code from them, and it mostly didn't work out.

**20:19** · His concern is that SDD makes the same promise — write the spec, generate the code — and might hit the same walls.

**20:26** · His piece is the most coherent skeptical case I've read on SDD so far.

**20:31** · On the critical side, François Zaninotto from Marmelab wrote a piece back in November called "Spec-Driven Development: The Waterfall Strikes Back" — arguing SDD brings waterfall-era problems back in markdown form.

**20:43** · It hit Hacker News the same week.

**20:45** · Marc Brooker from AWS wrote a direct rebuttal arguing that SDD gets you designing earlier and more iteratively, rather than locking you into a big upfront design phase the way old-school waterfall did.

**20:58** · The debate has shifted from "is SDD a good idea" to "how do you do SDD well."

**21:04** · On the enthusiast side, Prezi Engineering ran four teams through SDD workflows.

**21:09** · One engineer migrated an application to Material UI in two minutes, which they contrasted with another company where seven frontend teams took twelve months to do a similar migration the old way.

**21:21** · Those are two different apps and two different scopes, so the numbers don't translate directly — but the Prezi team treated it as proof SDD actually works at scale.

**21:31** · That's the kind of anecdote that gets people to give SDD a try.

### The takeaway

**21:35** · Six months of spec-driven development, compressed.

**21:38** · OpenSpec ran away with it — plus eight hundred and sixty-three percent.

**21:42** · The fastest workflow of the five, and the one I personally kept using the longest.

**21:47** · Spec Kit grew on GitHub's brand as much as on its own merits.

**21:52** · BMAD rewrote itself and kept its loyal community.

**21:55** · Taskmaster stalled right as it tried to go commercial.

**21:58** · Agent OS went quiet and narrowed its scope to the one job it still does well.

**22:03** · Around the edges, Superpowers, GSD, and Beads showed up.

**22:07** · And Claude Code itself quietly absorbed a bunch of what these frameworks used to do.

**22:12** · The headline: spec-driven development is real now, it's not all winning, and some of it is being replaced by features shipping inside the tools you already use.

**22:21** · New players keep appearing.

**22:23** · This video is going to age badly — which is, honestly, the point of making it at all.

**22:29** · A hands-on retest of the original five is on the list for a future video.

**22:33** · If that's something you want, let me know in the comments.

**22:36** · And one last thing.

**22:38** · Every framework in this video is pitched as "the right way" to plan software with AI.

**22:43** · My cat never writes a spec.

**22:45** · She walks up at five in the morning, sings a song, and food appears.

**22:49** · Fastest feedback loop I have ever seen.