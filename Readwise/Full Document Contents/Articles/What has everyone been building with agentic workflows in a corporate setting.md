# What has everyone been building with agentic workflows in a corporate setting?

![rw-book-cover](self)

## Metadata
- Author: [[QwopTillYouDrop]]
- Full Title: What has everyone been building with agentic workflows in a corporate setting?
- Category: #articles
- Summary: Many companies use agentic workflows mainly for automation tasks like code reviews, testing, and monitoring rather than having agents write all the code. Parallel agents can help break down tasks but still need human checks because AI often makes small mistakes. Overall, agents assist developers but do not replace them in creating production-quality software.
- URL: https://www.reddit.com/r/ExperiencedDevs/comments/1r1chos/what_has_everyone_been_building_with_agentic/

## Full Document
**[r/ExperiencedDevs](https://www.reddit.com/r/ExperiencedDevs/)**

### [QwopTillYouDrop](https://www.reddit.com/user/QwopTillYouDrop/)

 (2026-02-10 20:40:24)

I keep seeing content on Twitter/X and other social media platforms about building out agentic workflows. So much is on either using agents in development or building out massive, orchestrated agents working in parallel.

However it’s gotten to the point where it seems like everything is focused on building and configuring agents rather than what the agents are building.

Has anyone seen any notable projects or high quality work produced by agents? I don’t understand the benefit of having multiple agents working in parallel. Does throwing more agents at a problem produce higher quality work? Do people really need multiple agents routinely producing code? Are there applications where it makes sense for agents to be constantly writing code?

Much of the time, I see people getting help from agents (or really any LLM chatbot) with exceptions or maybe helping find potential issues during code reviews. What am I missing here?

#### [Superb\_Peanut9597](https://www.reddit.com/user/Superb_Peanut9597/)

 (2026-02-10 20:42:23)

Most corporate "agentic workflows" I've seen are just glorified chatbots with extra steps - the real wins come from targeted automation like automated code reviews or incident response, not some elaborate multi-agent orchestra that takes longer to debug than the original problem.

##### [raynorelyp](https://www.reddit.com/user/raynorelyp/)

 (2026-02-10 20:57:30)

That’s what I don’t get. We already have tools that can deterministic review our code (cyclomatic complexity, code coverage, linters, security static analysis) and the amount of effort to train an ai on the context is way more than the effort of reviewing. 

And I’ve never seen a serious company willing to let an ai handle an incident without supervision and human approvals anyways. Heck, that would violate the law in a lot of industries if you did.

###### [TastyToad](https://www.reddit.com/user/TastyToad/)

 (2026-02-10 22:22:05)

For transparency, I'm co-developing LLM based internal code review tooling.

> 
> We already have tools that can deterministic review our code (cyclomatic complexity, code coverage, linters, security static analysis)
> 
> 
> 

That's why we specifically tune our solution to work a level above. Point out bad practices not covered by conventional tooling, spot API and runtime compatibility issues, etc. The jury is still out but the results we've seen so far seem promising. Arguably, it's possible that all these problems could theoretically be found by a right combination of static analysis with a right set of configurations applied. Nobody has time for that, so we provide language and stack agnostic statistical safety net that you can add in a matter of minutes and get the benefits immediately.

Side note. Teams I've been working with for the past 10+ years all went heavy on on deterministic tools. I myself have been advocating using them for almost 20 years. While valuable, they aren't enough IMO, and tend to introduce too much noise / require too much tweaking with teams that don't make silly mistakes on a regular basis.

> 
> the amount of effort to train an ai on the context is way more than the effort of reviewing
> 
> 
> 

We don't train anything. We take existing models from top vendors, add context and internal knowledge via prompting and tools. At current token prices we pay ~$1 per review and user gets first round of (decent) feedback in minutes instead of waiting hours/days for another human to have a look.

> 
> And I’ve never seen a serious company willing to let an ai handle an incident without supervision and human approvals anyways
> 
> 
> 

100% agreed on this. AI can be useful in speeding up diagnosis but the responsibility is always on a human.

###### [kaibee](https://www.reddit.com/user/kaibee/)

 (2026-02-11 03:24:59)

> 
> Arguably, it's possible that all these problems could theoretically be found by a right combination of static analysis with a right set of configurations applied. Nobody has time for that
> 
> 
> 

Make the LLM do it.

###### [onemanforeachvill](https://www.reddit.com/user/onemanforeachvill/)

 (2026-02-11 08:20:33)

Yes. This is much better if you have a deterministic tool and can get the llm to do the configuration. Then you have deterministic output and can also easily tweak it.

###### [raynorelyp](https://www.reddit.com/user/raynorelyp/)

 (2026-02-11 00:38:07)

You’re splitting hairs on the word train. I don’t mean train as in the llm sense. I mean train as in providing the context it needs.

###### [originalchronoguy](https://www.reddit.com/user/originalchronoguy/)

 (2026-02-10 21:28:32)

UI isn't deterministic. A user logging into a web app clicks on different things in different order; redrawing data based on their interaction.  

The new tools like MCP and Playwright will simulate those different edge cases on what the code you or a LLM generated. And you can instruct it. Tell it to test the search flow with XYZ filters. And if it get a specific response, walk through the data flow of how data propagates. In the past, all of that was done through assume assertions in unit test cases or scripts like Selenium.

Now, I can say "my user clicked on the right hand toggle, the API is returning 5 jobs but the filter is not showing the ship data in column 3 of my table after I toggled the recent orders by 3 days" which is completely random and a MCP will replicate those clicks and observer everything and tell you, "the method XYZ on line 44 of controller/dataParser.json is retrieving a malform empty array when it should be a JSON. I will simulate the payload and show you with right payoload, your 3rd column will render correctly"

You can't always assert specific test cases in the wild. That is why many unit test fails.

###### [onemanforeachvill](https://www.reddit.com/user/onemanforeachvill/)

 (2026-02-11 08:22:56)

It's deterministic. What you are describing is just depending on initial conditions. If your application is very sensitive to those then it's chaotic.

##### [shiny0metal0ass](https://www.reddit.com/user/shiny0metal0ass/)

 (2026-02-10 22:09:37)

Well *some* of them are non-deterministic cicd pipelines..

###### [Visionexe](https://www.reddit.com/user/Visionexe/)

 (2026-02-11 20:44:12)

It's called DevOdds

##### [horserino](https://www.reddit.com/user/horserino/)

 (2026-02-11 05:50:25)

Using Claude Code is an "agentic workflow" and it is miles ahead of a "glorified chatbot with extra steps".

The main reason is simple, an "agentic" tool like Claude Code can run other tools and act on their output. That way you close a feedback loop over a chat based model and allow it to validate its output autonomously against a compiler, a test suite, a linter, etc.

Such a loop elevates the usefulness and quality of its output, essentially for free.

And given that this works well for coding, people are in a rush to apply the same principle elsewhere.

##### [micseydel](https://www.reddit.com/user/micseydel/)

 (2026-02-10 20:56:12)

> 
> the real wins come from targeted automation like automated code reviews or incident response
> 
> 
> 

Is this an evidence-based claim? If so I'd love to know more. I ask because devs' intuition isn't a reliable measure:

> 
> developers expected AI to speed them up by 24%, and even after experiencing the slowdown, they still believed AI had sped them up by 20%.
> 
> 
> 

Per <https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/> via <https://www.reddit.com/r/ExperiencedDevs/comments/1lwk503/>

Here are some pull requests that I'd love to see counter examples for:

* <https://github.com/dotnet/runtime/pull/115762>
	+ "@copilot fix the build error on apple platforms" (because it submitted broken code)
* <https://github.com/dotnet/runtime/pull/115743>
	+ "Please fix the style issues causing build failures, and move the new test into an existing test file." (because it couldn't just fix the build failures)
* <https://github.com/dotnet/runtime/pull/115733>
	+ "@copilot This seems like it's fixing the symptom rather than the underlying issue? What causes us to get into this situation in the first place, where we end up with an invalid index into the backtracking stack?"
* <https://github.com/dotnet/runtime/pull/115732>
	+ "Special casing NOT= like this seems like the wrong answer, especially since `1 NOT= 2` already worked."

Best I can tell, chatbot technology and automation do not mix. But I'd love to change my mind, while being mindful of cognitive biases: <https://www.youtube.com/watch?v=vKA4w2O61Xo>

###### [horserino](https://www.reddit.com/user/horserino/)

 (2026-02-11 12:48:44)

I dunno about automated incident response, I'm pretty skeptical about that one (other than some kind of agentic automated rollback mechanism or something, but we don't really need LLMs to leverage that).

In the code review world, I found code rabbit to be pretty promising (used a 2 week free trial) since it doesn't rely solely on the model's internal knowledge, and instead seems to trigger additional tooling to get more context for the review. Tried it on a personal project and on a big PR got something like 60%-70% signal to noise ratio on its comments and suggestions. Not much worse than static/deterministic tooling I've used (like Sonar and friends).

Not fully convinced but way better than just telling your average model to "review" your diff, and in theory it runs static tools and filters out the noise. I'm not fully advocating for this specific tool but I think this direction is definitely promising, since in my experience static tooling can be really hit and miss when it goes beyond compilers and tests

###### [micseydel](https://www.reddit.com/user/micseydel/)

 (2026-02-11 15:55:07)

> 
> Tried it on a personal project and on a big PR got something like 60%-70% signal to noise ratio on its comments and suggestions. **Not much worse** than static/deterministic tooling I've used (like Sonar and friends).
> 
> 
> 

This to me is damning - for how expensive LLMs are, they should be **much better**.

> 
> I think this direction is definitely promising, since in my experience static tooling can be really **hit and miss**
> 
> 
> 

LLMs are hit or miss, and aren't made of code that can be easily updated when bugs are found. I'm open to the idea that they're useful anyway, but I think it's a matter of running experiment and gathering data to figure out if they're worth it - do you disagree?

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-10 20:57:30)

Those github links are wildly outdated. The current tooling is leaps and bounds better.

Even content from November 2025 would be outdated to analyze current agentic flow.

###### [micseydel](https://www.reddit.com/user/micseydel/)

 (2026-02-10 20:59:18)

Like I said - counter examples are welcome! (Specifically, I'd love to see links to PRs on non-AI FOSS projects like dotnot, Firefox, Blender, etc.)

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-10 21:07:11)

I'm not really here to win an argument. This is a part of a lot of our jobs now at work. Can I show you my company's repository? No.

Will I go digging around the internet to find unicorn FOSS projects which cleanly demonstrate cutting edge agentic dev flows for you? Also no.

I'm just letting you know that if you are making your decision based on info from May 2025 then you are doing yourself a huge disservice.

###### [micseydel](https://www.reddit.com/user/micseydel/)

 (2026-02-10 21:15:23)

I'm asking why you believe what I quoted is true, not trying to "win." No one is asking you to dig, I just made clear what could in principle change my mind.

I'm curious: what if anything would change your mind? Is it possible the quote of your comment is untrue? How could we find out?

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-10 21:22:05)

You would need to change my boss's mind to change mine. What I'm telling you is that I'm required to use these tools. Their output, three months ago, was not sufficient for production work. Their output today is good enough that my boss would rather use it than me. The incidence of bugs remains low enough for his tolerance.

Until that stops being true, I have to use the tool. You are asking me how I could be convinced a hammer cannot install nails. It can now, and so it does.

###### [micseydel](https://www.reddit.com/user/micseydel/)

 (2026-02-10 21:32:37)

> 
> You would need to change my boss's mind to change mine
> 
> 
> 

Thanks for clarifying.

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-10 21:45:39)

Okay

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 00:13:46)

[removed]

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-11 11:36:00)

My evidence is their real world usage at most software companies now.

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 11:49:28)

[removed]

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-11 14:15:00)

While they are losing money, the tools have real, measurable impacts and companies including mine have found that to be strongly positive.

OpenAI can lose money all day. My employer is gaining money by using their tools.

Until that changes, I have to use them.

###### [micseydel](https://www.reddit.com/user/micseydel/)

 (2026-02-11 15:57:56)

> 
> the tools have real, measurable impacts and companies including mine
> 
> 
> 

You should write an engineering blog post, or a research paper.

###### 

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 00:13:06)

[removed]

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-11 11:36:33)

That's okay, while you are in disbelief the world will continue to use the tools.

See you in a year!

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 11:50:16)

[removed]

###### [p1-o2](https://www.reddit.com/user/p1-o2/)

 (2026-02-11 14:14:14)

In my architecture at work they are massive multipliers. Maybe it isn't a good fit for your codebase.

##### [originalchronoguy](https://www.reddit.com/user/originalchronoguy/)

 (2026-02-10 21:23:02)

> 
> the real wins come from targeted automation like automated code reviews or incident response
> 
> 
> 

That is what multi-agent workflow is.  

People typically only use one agent at a time -- the coding agent.

The tertiary agents are doing things like running MCP servers to QA, debug. Another agent to check compliance against your coding standard to halt the primary agent.  

The others to scalfold Grafana/Prometheus health checks, and so on and so on.  

To pull Jira tickets. Automate the pen test and security scan when branch is merged.

As I wrote in my reply. It is very similar to developing CiCD tooling. But doing things that can't be done before like running a headless browser to test your UI against a backend with clicks and toggles that previously required Selenium hard coded scripting. That automation is completely hands free based on what UI elements you just committed to git.

###### [sneakysocks544](https://www.reddit.com/user/sneakysocks544/)

 (2026-02-10 22:30:51)

This just sounds like CI/CD with a lot of extra steps and $$$ spent on LLM calls. 

###### [originalchronoguy](https://www.reddit.com/user/originalchronoguy/)

 (2026-02-10 23:29:08)

Its not though. All of our devs use new M-series macbooks. It is just a git pull docker image to run a local LLM like ollama with qwen3. No outside LLM call $$$. All localized.

##### [mmcnl](https://www.reddit.com/user/mmcnl/)

 (2026-02-11 10:25:51)

What have you seen working well with regards to incident response?

##### [agazizov](https://www.reddit.com/user/agazizov/)

 (2026-02-18 23:12:03)

one area where agents actually deliver is e2e testing. the task is deterministic - click button, observe result, compare against expected. theres actual ground truth so the agent doesnt hallucinate uselessly.

been doing this at work, inspired partly by what agenti qa ppl were experimenting with. you write a test plan in plain english, agent executes it, takes sceenshots for evidence 

not code gen, not multi-agent orchestra. just agent as a human tester substitute. thats the loop that actually closes.

#### [bland3rs](https://www.reddit.com/user/bland3rs/)

 (2026-02-10 20:57:25)

Because AI is new (and scary), people are pushed to be performative and post every little thought or experiment to look like they are “on top of things.”

* Executives will try to sell that they are forward looking with LinkedIn ramblings.
* Engineers will try to look smart and show “cutting edge” demos.

Everyone is holding onto their seats scared of the future (a reasonable position) and it manifests as all these “look, I live and breathe AI” posts. This means that most of the content about AIs is largely driven by fear and not utility.

But onto your questions:

The only time I’ve seen parallel agents really useful is to make some greenfield project/component where you’re focused on something that works and not exactly if it works well.

A serious project could be multiple prototypes where you are weighing different approaches and you need working demos initially. Or it could be something dumb like “make me a GUI to generate SQL queries” where it’s a throwaway but still useful tool.

When correctness comes into play, you have to intervene or check more often and a bunch of parallel agents will be writing far more code than you can check.

You CAN still use them though — because waiting on an agent to do stuff is idle time so sometimes you want to have it do a bunch of things at once and then you come back from a break to review.

##### [Fidodo](https://www.reddit.com/user/Fidodo/)

 (2026-02-11 01:52:58)

This is my experience too. I've never used parallel agents on a single codebase. The idea terrifies me because a single agent can produce slop faster than I can keep up with cleaning, parallel agents would just explode the amount of trash that needs to be fixed.

I do use parallel agents for doing totally different kinds of tasks though. While having an agent write up prototype code I'll use another agent to help me iterate on a spec and another agent to help me learn through research. I could also have multiple agents writing multiple isolated prototypes too as you point out. But I've yet to accept a single bit of AI output for anything for production without cleaning it up manually because they make so many tiny mistakes everywhere. The only exception would be highly normalized tasks like writing tests.

##### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 22:04:30)

Yup this perfectly explains my workflow. I run multiple agents in YOLO mode for POCs, discoveries, and quick demos for stakeholders. For actual development in the production codebase, I use a single agent and review each generated piece of code.

#### [PartBanyanTree](https://www.reddit.com/user/PartBanyanTree/)

 (2026-02-10 21:01:33)

I've been toying the last few weeks with github copilot and spinning up multiple prs to do parallel or semi-unrelated tasks.

it's a good fit because some things need multiple iterations and I don't need to spin up local environments and I can forget about them for hours or days and check in, make comments and/or merge. but can also dip into the PR at any time by checking out locally, hand tweaking. really good for dev cleanup and small refactors, or for laying out the tracks ahead.. set me up a new page for this new spike and some preliminary work, knowing I'll need that in another day. or just odd-ball unrelated side missions I wouldn't get to otherwise

it's a bad flow because the workflows always need permission to run so it's not as automated as I'd like. lots of new cognitive load keeping these multiple unrelated PRs moving forward. like not sure if it's amazing productivity gainz or just busywork that would be simpler if I just did one thing after another in sequence with focus

ultimately I'm just keeping an open mind and I'm suspecting I'll develop better intuition about when to spin up PRs when not to. I need to try some dedicated cursor time, or play with local work trees in parallel,a bit more for comparison 

#### [gfivksiausuwjtjtnv](https://www.reddit.com/user/gfivksiausuwjtjtnv/)

 (2026-02-10 20:48:51)

I’m a bit edgy so… Sometimes I run two Claude instances… *at the same time*

#### [zzzderp](https://www.reddit.com/user/zzzderp/)

 (2026-02-10 21:38:54)

Recently saw a blog from Stripe and a tweet from an eng at Ramp mentioning that background agents are a large chunk of their PRs merged.

Unfortunately it’s very hard to tell if these are just vanity metrics or if they are meaningfully contributing to what they’re building.

##### [micseydel](https://www.reddit.com/user/micseydel/)

 (2026-02-10 22:20:28)

> 
> it’s very hard to tell if these are just vanity metrics
> 
> 
> 

I'm of the opinion that if this was really happening, it would be visible in FOSS.

I'm inclined to believe that these tools aren't *actually* worth it (or many FOSS projects would happily and publicly adopt them), instead it's perverse incentives at workplaces where people feel pressured to align rather than speak honestly about what they've seen. (I know there's a study on this I've been meaning to go find.)

##### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 03:10:20)

[deleted]

###### [zzzderp](https://www.reddit.com/user/zzzderp/)

 (2026-02-11 17:04:07)

Interesting - how is the improvement in velocity being quantified?

#### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-10 21:12:41)

[deleted]

##### [Visionexe](https://www.reddit.com/user/Visionexe/)

 (2026-02-11 20:50:54)

> 
> This is not something I can disclose the details on
> 
> 
> 

Seems to be the trend with these claims. 

##### [JohnAMcdonald](https://www.reddit.com/user/JohnAMcdonald/)

 (2026-02-13 05:48:15)

Yes, I feel part of the reason why a lot of people seem to insist agents are so effective but don’t talk much about the work they’re doing is that a lot of it is this… “modernization”

#### [effectivescarequotes](https://www.reddit.com/user/effectivescarequotes/)

 (2026-02-11 00:47:50)

I've sat through a few meetings where someone proudly builds an API from scratch with unit tests. It's essentially the same comically simple API everytime. Basically little more than the sample code written for an O'Reily book.

I get that it's just for a demo, but I also haven't heard of anyone building anything worthwhile in my office. There's a big push to "find ways to improve our productivity with AI." I'm trying to be a good sport about it, but the tools just suck. 

#### [ReachingForVega](https://www.reddit.com/user/ReachingForVega/)

 (2026-02-10 21:37:26)

So we've got a low risk one. We have an agent that gets fed the details of an Incident ticket, the agent gets asked to pull number of users out of it then asked again how urgent the incident is and then lastly for the name of the system from a list of our systems.

We then use those outputs to determine if the priority of the ticket is correct and nudge it up or down.

It does drop a recommendation but it's not good enough to fully action. 

It has a decent accuracy on the mid items being incorrectly rated. We keep it away from P1 and P2. Otherwise it's the first touch. 

I have another really good one but it's proprietary and would reveal me to anyone from my work. Does about 50 queries to fill out a document. 

##### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-10 21:55:57)

[removed]

###### [ReachingForVega](https://www.reddit.com/user/ReachingForVega/)

 (2026-02-10 23:38:25)

How do you mean? The incident system cannot do it itself so unsure how you think so.

We've found people are really bad at correctly filling out certain fields. The benefit is our incident handlers don't incorrectly action the wrong items at the wrong time and shows the correct values for reporting. 

This is why we've build this flow to connect, pass the data and have the ai respond and the flow takes the outputs and updates the ticket. 

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 07:45:22)

[removed]

###### [ReachingForVega](https://www.reddit.com/user/ReachingForVega/)

 (2026-02-11 09:06:59)

What are you even talking about. Tell me you've not seen helpdesk work without telling me.

The "production line" are humans. 

These tickets are written by humans. Humans suck at correctly filling out forms. They learn to game the fields to get their incidents prioritised. Instead of the wasteful process of having people triage the tickets, the AI Agent does a first pass to get the low hanging fruit and it costs bugger all to run, definitely less than 1/10 of a human.

We don't spam our incident system from the applications we run, we have proper monitoring for that.

FYI current org staff size 15k and prior org was 35k. 

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-11 17:07:36)

[removed]

###### [ReachingForVega](https://www.reddit.com/user/ReachingForVega/)

 (2026-02-11 21:17:13)

Ok champ. 

#### [Fidodo](https://www.reddit.com/user/Fidodo/)

 (2026-02-11 01:42:40)

I'm building a really complicated low level infrastructure project. I've utilized AI heavily for research and drafting specs and prototyping. I'm done with the prototyping phase and I'm productionizing the code.

It has so many small sloppy mistakes and duplicated code and inefficient structures. I know that I didn't do enough review during the prototyping process because I was doing rapid prototyping, but still, by the time I gave it enough specific instructions to write the code to my standards it would have been faster to write it myself.

I still find it faster to correct its mistakes than to write everything from scratch, especially in the early phases where the spec is still getting solidified. I find a good workflow to be getting code 70% there with an LLM, then cleaning up the rest manually.

But for the people claiming that they don't write any code manually anymore? I am HIGHLY suspicious about their general competency and work quality. Nobody I know that I respect uses AI output as is. They all closely review it all and rewrite a lot of it.

Are there people that use LLMs to write higher quality code than they could write themselves? Absolutely. But it's not because because they got LLMs to write higher quality code than we can, it's that they couldn't write high quality code in the first place.

##### [Hot-Swan-2362](https://www.reddit.com/user/Hot-Swan-2362/)

 (2026-02-20 04:32:47)

have u tried claude opus/ sonnet?

#### [detroitsongbird](https://www.reddit.com/user/detroitsongbird/)

 (2026-02-11 10:47:28)

I’m working on code bases that have been around a while. Along with adding new features I’m slowly modernizing them. For example, they didn’t originally generate swagger docs. Now they do. But, the quality isn’t great. 

One task that I used sub agents for was cleaning up the docs for controllers. Specifically HTTP return codes. Not all APIs can refund all possible return codes. So, I used claude code. First some back and forth building a plan. The I had it change one controller. Part of the plan listed all controller that needed fixing. The plan was in a Markdown file. 

The real productivity gain was the next part. 

I told Claude code to read the plan and to use a subagent for each controller in the plan. Each sub agent should only fix one controller. 

This worked great.

#### [Adept\_Carpet](https://www.reddit.com/user/Adept_Carpet/)

 (2026-02-10 21:17:00)

> 
>  Does throwing more agents at a problem produce higher quality work?
> 
> 
> 

I've certainly seen numbers saying it does. Anthropic in particular has published compelling pieces both as blog posts and academic papers on this issue.

It seems that giving the agents different roles helps them break down the problem and stay focused.

In practice, I haven't gotten it working beyond the smallest scale. I've gotten agents to do compelling prototypes and small modifications to the prototypes, but even that has required some human intervention and it hasn't ever been "sit back and watch your agents do their thing" ever.

##### [anotherleftistbot](https://www.reddit.com/user/anotherleftistbot/)

 (2026-02-10 23:59:32)

I don't think of it as roles, I think about it as responsibilities. We use agents to manage context window, not necessarily to play house.

We use skills as composable context.

#### [bushidocodes](https://www.reddit.com/user/bushidocodes/)

 (2026-02-14 12:50:13)

It’s useful to think of subagents and agent swarms in terms of context management. Each agent has a set context window sized in tokens and if the usage % gets high, the effective intelligence drops and then compaction occurs (lossy summarization of context window). The idea of subagents is that you can break up the problem you’re working in either by chunking or by specialization (as MCPs, skills, etc. also consume tokens) and then you have an overarching orchestration agent to manage the lifecycle of subagents.

I think it’s helpful to think of agentic development pipelines as analogous to DevOps but now applied to software creation itself. Most of Ops is now focused on iterative development of multi stage pipelines (including tool calls). Now we have agentic pipelines targeting development tasks. Most of the critiques I hear about developers not wanting to give up hands on keys development remind me of the “cattle not pets” debate and how that played out for IT systems administrators earlier in my career.

I use these techniques for modernization projects on core IRS tax processing systems, mostly COBOL to Java at the moment. A very large portion of my time is spend on internal evangelism and education.

#### [anotherleftistbot](https://www.reddit.com/user/anotherleftistbot/)

 (2026-02-10 23:58:20)

I'm responsible for agentic development at a mid-sized corporation and it has been a game changer. We have may millions of lines of code in our codebase and are between $100M and $1B ARR. Our customers are often technical. 

Still lots of growing pains and we're constantly evolving as the landscape changes. 

The job changes in ways that not everyone loves. The people who love it most are actually senior/lead/principles who are used to delegating. Juniors love it because they get shit done but we have to keep them from pushing swillin. Mid-level engineers who are very attached to every line of code they write are not having fun.

Some people have irrational opinions about what AI can and can't do but its getting harder for them as their peers surpass them in both quantity and quality of work. Its a business at the end of the day.

##### [QwopTillYouDrop](https://www.reddit.com/user/QwopTillYouDrop/)

 (2026-02-11 02:02:38)

Very interesting! How is quality and quantity measured? 

I keep seeing n times improvement or x% increase but rarely any explanations of how it’s calculated.

###### [anotherleftistbot](https://www.reddit.com/user/anotherleftistbot/)

 (2026-02-11 02:19:20)

It’s far from perfect but we look at a few signals.

we follow a Lean/Kanban style flow where stories and epics have been roughly the same size for several years. There are zero estimates, just small stories that take 1-2 days, and epics that complete in <2 weeks tip to tail.

When I compare throughput and cycle time for epics and stories that were estimated before adopting Agentic workflows, we see cycle time down and throughout of epics and stories up between 33-50% almost across the board.

AI analysis indicates similar complexity of stories that used to take longer. 

Teams eventually tend to start increasing story size because story and epic overhead has its own cost and it can be annoying to review so many PRs. So throughput tends to level out at some point and LoC is up a bit.

Our PMs and UX also convey the feeling that they are struggling to keep up with our most advanced teams, as they are completing work more quickly than the PM can define requirements. I’m working with them on efficiencies as well.

As for quality we measure incoming bug rate, automation test failures, and support calls. All of those are flat over the last 6 months of heavy agentic development. They tend to go up a bit for a month or two as teams figure out how to implement guardrails and then go down.

Our open bug count has gone down (from very low to almost zero) since we now have AI take the first pass at fixing a bug. We don’t usually accept the fix from the agent but we have sent some back to support saying the bug could not be reproduced and ended up with either better reproduction steps or support closing the defect. AI is ridiculously good at identifying the code that is causing the problem if the bug is well written.

So yeah, it’s been an awesome ride and has far surpassed expectations.

It isn’t sunshine and rainbows. We’ve had some good people attrit even though we don’t force anyone to use AI. We are all working in new ways and identifying new bottlenecks and working through problems, but overall we’re way ahead of most organizations our sizeZ

Compared to a year ago when I sounded the alarms about the opportunity that was passing us by, I feel way more confident in my abilities and our company’s ability to adapt. The rate of change in both the tech/tools and our organization is staggering. It’s unlike anything I’ve seen in almost 19 years in this industry and 17 years in engineering.

Lots of people in this sub have irrational opinions that they WANT to be true about AI but few of them have j vested enough in AI capability and skills to hold those opinions. Anti-AI is as much a cult as they accuse the Pro-AI of being.

###### [dats\_cool](https://www.reddit.com/user/dats_cool/)

 (2026-02-14 00:44:23)

Sounds cool. How has it changed demand for software developer talent? Meaning, when do you find it appropriate to hire new developers given these new workflows?

How has compensation changed for new hires? What about layoffs?

###### [anotherleftistbot](https://www.reddit.com/user/anotherleftistbot/)

 (2026-02-14 05:02:43)

No layoffs. We were gonna have flat headcount anyway. 

Comp is similar. Budget never enough to reward everyone we want to but they’ve always been that way. Most money goes to promotions.

We’re up 40% YoY for epic/story throughput. LoC is up too. Cycle time is down 25% but PRs take longer.

Bugs, customer bugs, and build success are all flat.

##### [Virtual\_Chain9547](https://www.reddit.com/user/Virtual_Chain9547/)

 (2026-03-02 03:01:18)

Do you find the quality of juniors to just be substantially higher these days cause I'm struggling with the idea that I should be utilizing agentic development that heavily? 

I'm a new grad and wondering if I'm just behind the ball of the majority of the pack of new devs and that's all this boils down to. Have spoken with seniors I know about their utilization of AI in workflows at the enterprise level and what not and they've suggested to really embrace it cause it's the future and I know they aren't just feeding me propaganda. There's no incentive for them to be lying based on the nature of our relationship so it seems to be the truth that there are really large gains to be had in some workflows.

As a new grad though I still feel like I'm learning new things all the time that trying to lean hard into AI feels like I'm going to be doing myself a disservice in the long run and is going to really hamper my ability and understanding at what's really going on. 

I imagine your first job is where you get that guidance from more senior developers and where you make big steps in improving your abilities, it just feels hard to emulate that large, enterprise level environment when working on personal projects.

But then I hear that juniors are expected to be using this stuff and I just feel like maybe I just haven't done enough self-teach on the side to feel comfortable enough using the tech and not feel like I'm automating things I don't fully understand under the hood. 

Is there a disconnect I'm missing in my understanding of the state of things and new grads may not understand the ins and outs of everything they are generating and that's just a side effect that is being accepted or is it just a matter of I need to continue grinding and learning things so that I can safely utilize the tech without sacrificing my knowledge of what's actually happening? 

###### [anotherleftistbot](https://www.reddit.com/user/anotherleftistbot/)

 (2026-03-02 04:15:50)

I honestly stopped hiring juniors. Fucked yup, I know. We just haven’t grown headcount in about 2 years.

Ultimately what I’m looking for is high agency engineers who can jump in and make decisions right away and move fast.

I was one and it helped me be promoted to senior in 3 years. I’ve had other juniors jump in and be able to make a splash because they have the right mindset to deeply understand things, not get blocked, and rather than accept mediocrity from themselves or their teammates they make things better whether someone asked them to or not.

###### [Virtual\_Chain9547](https://www.reddit.com/user/Virtual_Chain9547/)

 (2026-03-02 05:44:22)

Appreciate the input, I don't think it's fucked up, gotta do what you gotta do.

#### [ivancea](https://www.reddit.com/user/ivancea/)

 (2026-02-10 20:56:37)

> 
> Has anyone seen any notable projects or high quality work produced by agents?
> 
> 
> 

I mean, using agents doesn't mean not reviweing. Most companies using agents will just use them for the work they always do.

> 
> I don’t understand the benefit of having multiple agents working in parallel
> 
> 
> 

You have 5 bugs to triage and reproduce, or 5 unrelated tasks, or whatever, then you just spawn an agent for each one. It's not easy, it requires adapting your development workflow, but it can be done.

Think about it as a way to reduce "idle time" to a minimum. If 1 agent can take on a task in 20 minutes, 10 agents can solve 10 tasks in 20 minutes too. But, wait! Because <you> have to 1) prompt and take care of them, and 2) review the results. So now it's not about "spawning infinite agents", but about reducing the times *you* are idle. So you spawn them in a way that gives you time to review and re-prompt. Well, worst case, they wait for your input, so you still work at your own pace. Btw, I'm not parallelizing agents, I'm not at that point yet. But it's clear to me that it's theoretically positive, as long as you manage yourself correctly. Not easy. It's like using Vim for the first time: you have a learning curve, and you won't be fast.

If you want a real example, I'm pretty new to using agents. I started last year, and used them from time to time, when they weren't as good as they're now. This week, I found an issue in my company, hard to reproduce becuase the error gave not enough information. It would require some time to investigate in depth, so, as I had some meetings, I just gave the error to the agent. 10 minutes later, it found the issue. I asked for a reproduction test, and it did, flawlessly, at the first try. After that, I asked for a fix, and it also got it. No time lost, an issue found, and everybody's happy!

Edit: as some final words: start workign with them. Slowly. Use them for some task, challenge it to do this or that. Eventually you'll see whee it's good or bad, and how to use them for your best benefit

#### [BusEquivalent9605](https://www.reddit.com/user/BusEquivalent9605/)

 (2026-02-10 21:16:13)

internal document search

#### [originalchronoguy](https://www.reddit.com/user/originalchronoguy/)

 (2026-02-10 21:18:49)

This is no different than building a CI/CD pipeline.

Agentic, running multiple agents for coding, load testing, QA, and hall monitoring checking each other is pretty much similar to DevOps app lifecycle development.

Eventually, it has to be built if the org wants to be proficient and ensure some normalcy of guard rails.

#### [F1B3R0PT1C](https://www.reddit.com/user/F1B3R0PT1C/)

 (2026-02-10 22:34:52)

Internal tools and low-risk projects. I still believe it’s better off as a helper inside the programming IDE rather than as a driver in the vibe-code IDE.

#### [behusbwj](https://www.reddit.com/user/behusbwj/)

 (2026-02-11 02:33:40)

The simple implementations have been the most useful for me. Answering repetitive questions, generating repetitive code, generally automating repetitive tasks that require unstructured input from a human

#### [MeButItsRandom](https://www.reddit.com/user/MeButItsRandom/)

 (2026-02-11 02:43:13)

We are starting to do agentic intakes that spin up a demo using client preferences. And loads of CRM related stuff to help us be more responsive.

We really like BAML and temporal.

#### [ryan\_the\_dev](https://www.reddit.com/user/ryan_the_dev/)

 (2026-02-11 13:03:58)

We have gone wild. We just launched an internal skill marketplace as well. 

We have it everywhere. From our own PR review to incident response.

#### [dmikalova-mwp](https://www.reddit.com/user/dmikalova-mwp/)

 (2026-02-11 16:24:47)

We have a huuuuuge migration project from cloudformation to pulumi that we've set up a workflow for, and it's turned a tooon of toil into just a lot of toil.

#### [latchkeylessons](https://www.reddit.com/user/latchkeylessons/)

 (2026-02-11 21:41:51)

A couple chatbots.

Another that was supposed to do "automatic" inventory routing based on defined inputs and ML-derived feedback mechanisms for inputs that were guided. Then they laid off the people doing regression training on inputs and... inventory went everywhere and the business eventually failed. There's going to be a lot more of that in the near future.

Chatbots are fine I guess, sometimes. Have yet to see anything successful in the data management world though.

#### [insanetheta](https://www.reddit.com/user/insanetheta/)

 (2026-02-12 17:29:29)

A simple agent chatbot that can form sql queries on a few common user log tables has been a huge time saver for product and customer service where I work. It’s cut out the data analysts from needing to keep building specialized charts for non technical folks

#### [narcisd](https://www.reddit.com/user/narcisd/)

 (2026-02-12 21:56:25)

Yaml.. I don’t write it anynore, tell Ai to do the changes.. no more white space issues

#### [Left-Block7970](https://www.reddit.com/user/Left-Block7970/)

 (2026-02-13 05:39:28)

They actually helped me debug why my acceptance tests weren’t working

#### [JohnAMcdonald](https://www.reddit.com/user/JohnAMcdonald/)

 (2026-02-13 05:50:24)

I think people are sleeping on how useful it is to be able to trigger an agent from your phone the moment you have an idea.

Pull reviews are the highest reward use case for agents I’ve seen so far. They are useful more often than not.

Agents are also good at iterating through and analyzing large amounts of data that people would never think to analyze. The contents of a Linux servers filesystem, an entire multi-repo code repository, an entire internal wiki, whatever.

As for working in parallel, people do it for the same reason poker players do it. There’s a long wait between interactions. If the tools operated instantly, people would focus on one thing at a time.

> 
> Has anyone seen any notable projects or high quality work produced by agents
> 
> 
> 

Dogfooding like openclaw aside, no. High quality work? Absolutely, these agents have all the time in the world to audit the codebase over and over looking for every fuck-up people have ever made. They’re better at bringing up the floor of work than raising the ceiling though.

#### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-02-13 10:44:33)

we use coding agents internally but more as a way to parallelise and get claude code / cursor to build multiple features while waiting on it to complete. or alternatively to break a bigger feature into multiple smaller tasks and assign them to individual agents to reduce task complexity for each individual agent and hence reduce the chance of hallucination / bad code

i don't think there is value in an always on agent for coding. it does make sense for specific cases like let's say a code review agent which checks on every push to git

#### [PeachScary413](https://www.reddit.com/user/PeachScary413/)

 (2026-02-13 10:58:09)

The benefit is that Anthropic can sell more tokens faster 👌

#### [Candid-Profession720](https://www.reddit.com/user/Candid-Profession720/)

 (2026-02-13 17:32:03)

Automated code review, automated pull request approvals, automated error understanding (having an LLM assist in evaluating an error returned by automation) entirely tasks around text processing or looking things up tbh

#### [3ABO3](https://www.reddit.com/user/3ABO3/)

 (2026-02-14 23:32:35)

Claude code made my k8s work more tolerable. I can just ask it "why did pod xyz roll" and it runs all the kubectl commands I don't want to remember, then summarizes it's findings

#### [brightcarvings](https://www.reddit.com/user/brightcarvings/)

 (2026-02-15 06:09:45)

I have had excellent success using LLMs to help add OpenTelemetry tracing into various parts of our codebase that was previously uninstrumented. Also for adding telemetry into our internal tooling, pipelines and testing that would never have been prioritised to be instrumented in the first place.

Helps that I'm an Engineering Manager so I can invest my limited available development time into things that are more "exploratory" and off the critical path, but these have definitely been some high value use-cases that I wouldn't never have been able to achieve without LLMs doing so much of the heavy implementation and debugging involved.

#### [paveltashev](https://www.reddit.com/user/paveltashev/)

 (2026-02-15 09:38:31)

Fascinating discussion on enterprise agentic workflows. I'm curious about the integration challenges.

For those implementing multi-agent systems: How do you manage:
1. Consistent context preservation across agents
2. Error handling and recovery mechanisms  

3. Performance monitoring and optimization

Would love to hear real-world implementation insights.

#### [Beginning\_Debt\_4584](https://www.reddit.com/user/Beginning_Debt_4584/)

 (2026-02-15 15:55:31)

I have seem agentic automate parts of customer support at my company. Mostly in areas that are low-risk

#### [KGoovaer](https://www.reddit.com/user/KGoovaer/)

 (2026-03-09 13:06:53)

Take a look here: <https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/>

I've been using it to automatically update documentation for now, but starting to experiment with migrating COBOL to Java in the next few weeks.

#### [EllaHall\_](https://www.reddit.com/user/EllaHall_/)

 (2026-03-10 05:05:27)

In most companies, agentic workflows aren’t about many agents writing code they’re used for automation like support triage, research assistants, or internal copilots using tools like LangGraph or CrewAI.

#### [theywantnone](https://www.reddit.com/user/theywantnone/)

 (2026-03-12 10:10:04)

I think a lot of the replies here are basically right that the useful stuff is narrower than the hype. Most teams do not need five agents arguing with each other to write production code, they need one system that can handle a repeatable workflow without creating more review debt than it saves. That is why MindStudio feels more practical to me in this space since it makes more sense for packaging a real agent workflow than chasing the whole parallel agents everywhere vision.

#### [Nik\_AIMT](https://www.reddit.com/user/Nik_AIMT/)

 (2026-03-17 12:30:42)

Most of the multi-agent stuff i see does feels like over-engineered theater. throwing more agents at a problem usually just results in more hallucinated code that someone eventually has to peer-review. it’s a massive distraction from actually shipping.

at the company where i work, they’ve basically stopped trying to make agents "the developers." instead, they use them for the invisible technical heavy lifting that everyone hates doing. 

for example, instead of writing new features, they have agents running gtm health checks and data sanity checks in the background. the agents just sit there and monitor tags or validate analytics in real-time. if something stops firing or the data looks weird, it gets caught before a human even opens a dashboard.

it's not flashy, but it's the only way they've found to actually regain any mental space. the machines handle the millisecond-level audits, and the people stay in charge as the architects. solving the "logistical grind" is way more useful than trying to get an llm to build a whole app from scratch.
