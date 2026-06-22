# So I stumbled across this prompt hack a couple weeks back and honestly? I wish I could unlearn it.

![rw-book-cover](https://readwise-assets.s3.amazonaws.com/static/images/article0.00998d930354.png)

## Metadata
- Author: [[cleancodecrew]]
- Full Title: So I stumbled across this prompt hack a couple weeks back and honestly? I wish I could unlearn it.
- Category: #articles
- Summary: A prompt hack where Claude AI reviews its own code harshly helps find many bugs and edge cases. Users find it effective but sometimes tiring due to many issues being raised. Using official plugins and multiple review agents improves code quality and learning.
- URL: https://www.reddit.com/r/ClaudeAI/comments/1q5a90l/so_i_stumbled_across_this_prompt_hack_a_couple/

## Full Document
**[r/ClaudeAI](https://www.reddit.com/r/ClaudeAI/)**

### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 05:40:06)

After Claude finishes coding a feature, run this:

```
Do a git diff and pretend you're a senior dev doing a code review and you HATE this implementation. What would you criticize? What edge cases am I missing?
```

here's the thing: it works *too well*.

Since I started using it, I've realized that basically every first pass from Claude (even Opus) ships with problems I would've been embarrassed to merge. We're talking missed edge cases, subtle bugs, the works.

Yeah, the prompt is adversarial by design. Run it 10 times and it'll keep inventing issues. But I've been coding long enough to filter signal from noise, and there's a *lot* of signal. Usually two passes catches the real stuff, as long as you push back on over-engineered "fixes."

The frustrating part? I used to trust my local code reviews with confidence. Sometimes, I'd try both claude-cli and cursor and I'd still find more issues with claude cli, but not so much from opus 4.5(when used in cusor)

I've settled at a point where I do a few local reviews ( 2-5). Finally I can't merge without doing a Deep Code Review of various aspects ( business logic walkthrough, security, regression & hallucination) in Github itself and finally implementing the fixes in CLI and reviewing one more time.

Anyway, no grand takeaway here. Just try it yourself if you want your vibe coding bubble popped. Claude is genuinely impressive, but the gap between "looks right" and "actually right" is bigger than I expected.

Update:

Thanks everyone for the discussion! Here are the key resources mentioned to automate this "adversarial code review" workflows

* **Claude Code Skills : /** [Turingmind Claude Code Reviewer Skill](https://github.com/turingmindai/turingmind-code-review) (Deep Reviews of uncommitted local changes via `/turingmind-code-review`). (Runs 6 specialized agents in parallel)
* **Local Git Review:**[Agent-3-7/agent37-skills-collection](https://github.com/Agent-3-7/agent37-skills-collection)(Reviews uncommitted local changes via `/local-review`).
* **Prompt Cookbooks:**[Claude Code Cookbook](https://github.com/wasabeef/claude-code-cookbook) and [Agent Debater](https://github.com/beyond-logic-labs/bl-agent-debater).
* **Methodology:**[BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD/tree/main/src%2Fmodules%2Fbmm%2Fworkflows%2F4-implementation%2Fcode-review)(Git diffs vs. Story specs) and Steve Yegge’s article on [The Rule of Five](https://steve-yegge.medium.com/six-new-tips-for-better-coding-with-agents-d4e9c86e42a9).
* **Official Plugin:** `/code-review:code-review` .

#### [ClaudeAI-mod-bot](https://www.reddit.com/user/ClaudeAI-mod-bot/)

 (2026-01-06 09:12:47)

**TL;DR generated automatically after 100 comments.**

**The consensus is a resounding "yes."** Y'all agree that OP's adversarial review prompt is brutally effective and exposes that Claude's first-pass code is often full of bugs and missed edge cases. It's a necessary evil.

The top comment is clutch and offers a more structured solution:
\* **Use Anthropic's official `/code-review` plugin.** It runs 5 specialized agents in parallel to review pull requests.
\* The same user created and shared a **custom plugin to run a similar multi-agent review on local `git diff`s**, which many in the thread are now using.

Other key takeaways from the thread:
\* This is a known strategy, sometimes called the "Rule of Five." The sweet spot is **2-3 review passes** before the suggestions become overly pedantic ("what if the user enters a negative number during a solar eclipse?").
\* Many of you use similar adversarial personas, like asking Claude to review the code as if it were **Linus Torvalds** or a salty principal engineer. The key is forcing it to be critical.
\* **PSA: This workflow is a massive token-eater.** You'll almost certainly need the Max plan to do this regularly.
\* While some question if this is faster than just coding it yourself, most feel it's worth it for catching subtle bugs and learning from the AI's critiques. It's less about speed and more about robustness.

##### 

#### [enthusiast\_bob](https://www.reddit.com/user/enthusiast_bob/)

 (2026-01-06 06:01:38)

Try the "/code-review:code-review (plugin:code-review@claude-plugins-official)" plugin from anthropic. It's brilliant because it runs 5 agents in parallel to do a code review and then runs haiku agents to rate it and only flags the issues that are scored 80 or above.

The one caveat is, it only does that on PRs. I just asked claude to look at that plugin and create a local version that does the same thing on git diff "/local-review" and it works beautifully. One shot a review and move on with your life.

Edit: Since many of you are asking for this, I published the command as a plugin on GitHub (<https://github.com/Agent-3-7/agent37-skills-collection>). For now it's part of our hosted AI skills collection at <https://agent37.com> but will move it out to it's own thing if needed.

```
/plugin marketplace add Agent-3-7/agent37-skills-collection
/plugin install local-review@agent37-skills
-- Restart CC
/local-review:local-review

```

##### [soopypoopy132](https://www.reddit.com/user/soopypoopy132/)

 (2026-01-06 08:39:29)

would this not take a crazy amount of tokens?

###### [enthusiast\_bob](https://www.reddit.com/user/enthusiast_bob/)

 (2026-01-06 08:43:00)

Yeah it takes a crazy amount of tokens. Don't use this if you're not on the Max plan.

###### [AdCommon2138](https://www.reddit.com/user/AdCommon2138/)

 (2026-01-06 16:27:43)

Thanks seems absolutely crucial to use if I forget to burn pro capacity somehow (vacations or something)

###### [mistermax76](https://www.reddit.com/user/mistermax76/)

 (2026-01-06 21:30:33)

WAIT.... man, is it like, all the AI is about getting the credits off the player? And is the veracity of the model in no way tied to that? WOWSER

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-01-06 13:41:31)

[removed]

###### [chiviet234](https://www.reddit.com/user/chiviet234/)

 (2026-01-06 14:09:22)

Your 20 dollar of credits go bye bye

##### [creegs](https://www.reddit.com/user/creegs/)

 (2026-01-06 13:13:56)

You can also do `/code-review:code-review on uncommitted changes` and it works fine. Agree that’s it’s a great implementation though!

###### [tobek](https://www.reddit.com/user/tobek/)

 (2026-01-12 22:58:53)

If you do this, the plugin is set up such that of the 5 review agents, one agent reviews git history and one agent reviews the previous PR. This might be overkill for what you want - the skill above avoids this and just spins up agents to review current changes.

###### [creegs](https://www.reddit.com/user/creegs/)

 (2026-01-13 01:24:14)

From what I’ve seen, it reviews past PRs which has been really useful at times, but yeah, if you’re not using a PR based workflow, it’s not helpful!

##### [Sidion](https://www.reddit.com/user/Sidion/)

 (2026-01-06 06:21:07)

Wow didnt know about this. Will definitely be trying

##### [Visionioso](https://www.reddit.com/user/Visionioso/)

 (2026-01-06 07:00:44)

I had just reinvented the wheel it seems lol

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:08:25)

Why so? are you building something similar?

##### [Mpjhorner](https://www.reddit.com/user/Mpjhorner/)

 (2026-01-06 07:46:32)

Can you make GitHub CI do this?

###### [enthusiast\_bob](https://www.reddit.com/user/enthusiast_bob/)

 (2026-01-06 08:33:52)

Well the anthropics plugin does use github pr ci I think to publish comments on the CR directly.

##### [9fxd](https://www.reddit.com/user/9fxd/)

 (2026-01-06 07:48:56)

TIL :o

##### [Ulysse31Ofp](https://www.reddit.com/user/Ulysse31Ofp/)

 (2026-01-06 16:40:09)

Nice, thank you, have been using it. However, while doing local review in plan mode claude edited a file (a fix that i approved) while remaining in plan mode, i believe this to be unexpected, letting you know

```
● Done. The IDOR vulnerability is fixed at services.py:337-341.
```

```
The authorization now:
```

```
2. Denies access if user's organisation doesn't match bilan's organisation
```

```
> how did you make an edit in plan mode ?
```

```
● You're right to question that. Plan mode was still active from the code review skill, which shouldn't have allowed edits. The edit went through anyway - likely a timing issue where the restriction appeared in the response after the edit was already processed.
```

```
The fix is applied correctly, but I should have asked you to exit plan mode first or waited for it to end. My apologies for the inconsistency.
```

##### [Shumuu](https://www.reddit.com/user/Shumuu/)

 (2026-01-06 07:17:21)

Could you share it?

#### [suprachromat](https://www.reddit.com/user/suprachromat/)

 (2026-01-06 05:58:08)

I've done this too and it works well, the only tiresome thing is that it keeps finding edge cases and issues one might never even thought of, so at a certain point, when reading the latest critiques, it becomes "well you're right but can we move on with this thing already, I'm tired of waiting for you to fix all the edge cases, adding defensive logic, etc."

I find the first couple of passes or so catch the biggest problems and then after that it's "good enough, ship it" - but I'm not doing this for work, only hobbyist stuff, so the bar for "it works well enough" is much, much lower

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 06:09:04)

Yeah exactly, there's diminishing returns after pass 2-3. The first round catches the "oh shit that would've broken in prod" stuff, then it starts inventing hypotheticals like "what if the user passes a negative number while the database is mid-transaction during a solar eclipse." 

At some point you have to tell it to stop or you'll never ship anything. For hobby stuff that bar makes total sense. 

For work I've started asking it to *run as multiple reviews till It bubbles up all the* the issues by severity then I let AI triage them before fixing anything. My solution, Let AI helps me decide what's worth addressing now vs. what's hallucination due to missed context - you'd be surprised to see how many of these are false positives.

###### [dopp3lganger](https://www.reddit.com/user/dopp3lganger/)

 (2026-01-06 12:04:47)

> 
> "what if the user passes a negative number while the database is mid-transaction during a solar eclipse."
> 
> 
> 

aaaand there goes my coffee 🤣

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 12:21:04)

lol finally someone reddit

###### [FjorgVanDerPlorg](https://www.reddit.com/user/FjorgVanDerPlorg/)

 (2026-01-06 13:11:46)

Love the sass from that prompt as well:

```
Lines 45-46
mongo_client = None
db = None
Why? discord.py supports bot.db as an attribute
This is 2026, not 2015

```

#### [No\_Programmer2705](https://www.reddit.com/user/No_Programmer2705/)

 (2026-01-06 08:35:04)

This is a repo I came across, it has a very interesting role/debate structure. 

<https://github.com/wasabeef/claude-code-cookbook>

I also found sometimes that different Agents are also interesting for review, they tackle it on different point of views, for that reason, I also started some experimentation with multi-agent Codex vs Claude. Which works with subscription all in your machine, here is the repo, in experimental version:

<https://github.com/beyond-logic-labs/bl-agent-debater> 

where codex and claude speak through files to review or plan over an issue.

The claude cookbook above is much better and richer but does not support multi agent debate roles

##### [flurdy](https://www.reddit.com/user/flurdy/)

 (2026-01-07 10:26:11)

Nice, I will take a look at that Detaber! I use Claude in VS Code for most of the work, but then I frequently do a code review versus the jira ticket with the new Codex plugin in VS Code to keep it honest. And my current client has enabled Amazon Q and github copilot code reviews in the github PRs. Which I tell Claude to read and address. So totally multi-agent overkill.

#### [Particular\_Guitar386](https://www.reddit.com/user/Particular_Guitar386/)

 (2026-01-06 09:26:02)

Rhetorical questions? Y'all need to use them less.

##### [Amasov](https://www.reddit.com/user/Amasov/)

 (2026-01-06 14:17:00)

You know what? Have an upvote.

##### [Humprdink](https://www.reddit.com/user/Humprdink/)

 (2026-01-07 00:47:14)

It's not a simple rhetorical question. It's a profound emotion invocation.

#### [IJustTellTheTruthBro](https://www.reddit.com/user/IJustTellTheTruthBro/)

 (2026-01-06 06:32:43)

Your prompts don’t work well enough for me to not recognize this post was written with AI assistance

##### [maxstronge](https://www.reddit.com/user/maxstronge/)

 (2026-01-06 07:02:02)

Quite honestly I'm about 102% sure I've seen this exact post before down to the 'I wish I could unlearn' part. 

Does seem like a good idea though tbf.

###### [bibboo](https://www.reddit.com/user/bibboo/)

 (2026-01-06 12:57:20)

Hahahah, might that be my [post](https://www.reddit.com/r/ClaudeAI/comments/1ptcbm3/code_quality_of_claude_a_sad_realization/) perhaps? I'm not complaining though, I couldn't remember from where I initially got the prompt.

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:12:29)

tbh, once you run the review it doesn't feel like a good idea, the upper limit here is your capability to review the reviews.

##### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-01-06 06:43:23)

[deleted]

###### [KnifeFed](https://www.reddit.com/user/KnifeFed/)

 (2026-01-06 12:42:16)

What brain are you using?

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 12:45:51)

one that responds to sarcasm with humor no one gets.

#### [kaihanga](https://www.reddit.com/user/kaihanga/)

 (2026-01-06 08:37:42)

This is an excellent practice that I’ve also found valuable and “codified” by the rule-of-fives principle as coined by Jeffrey Emanuel. More info’s available in a Yegge blog post at <https://steve-yegge.medium.com/six-new-tips-for-better-coding-with-agents-d4e9c86e42a9> at “5. The Rule of Five: When in doubt, have the agent review its own work 5 times.”

It’s not so much about the prompt structure as much as it’s rereviewing the work. I’ve found somewhere in the neighborhood of 3 to 4 reviews to be the sweet spot when effectiveness gives way to triviality.

##### [BlueVajra](https://www.reddit.com/user/BlueVajra/)

 (2026-01-08 05:25:13)

The interesting thing in that article is how it is being reviewed. He recommended a narrow to broad approach (or inverse) One of which was, do we really need this?

#### [Narrow-Belt-5030](https://www.reddit.com/user/Narrow-Belt-5030/)

 (2026-01-06 05:44:53)

Might be useful to include the actual prompt? ;-)

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 05:46:11)

Just fixed, lol!

#### [n\_lens](https://www.reddit.com/user/n_lens/)

 (2026-01-06 06:19:09)

At this point it might just be quicker to write code yourself.

##### [jngldrm](https://www.reddit.com/user/jngldrm/)

 (2026-01-06 07:37:44)

If you know how to code...

##### [sismograph](https://www.reddit.com/user/sismograph/)

 (2026-01-06 07:20:55)

What I was thinking, this prompt takes about the same time that it would take yourself to criticially read your own code and see what needs to change. 

If people never learn to critique their own code and hand everything to AI we are never going to have a new generation of sr engineers. 

(Yes I know how gatekeepy that sounds)

###### [Glad-Champion5767](https://www.reddit.com/user/Glad-Champion5767/)

 (2026-01-06 10:15:19)

Surely people will read the review that it spits out. And over time they learn from it, just like you would without an AI assistant? Its more than just critically reading your own code though. Its about edge cases, missing stuff. This is where these review tools shine, because they might find the gaps. That has nothing do with how good or bad the code you wrote is, it has something to do with the code that you did NOT write.

###### [kilopeter](https://www.reddit.com/user/kilopeter/)

 (2026-01-06 11:45:57)

My subjective, incomplete, vibes-based opinions incoming:

> 
> Surely people will read the review that it spits out. And over time they learn from it, just like you would without an AI assistant?
> 
> 
> 

This is a fantastic way to learn, but takes time. Most vibe coders will chase their deadlines and/or the dopamine and move on without reading a single line of code as soon as the thing passes tests, or just works in their moment of testing.

> 
> It's more than just critically reading your own code though. Its about edge cases, missing stuff. This is where these review tools shine, because they might find the gaps. That has nothing do with how good or bad the code you wrote is, it has something to do with the code that you did NOT write.
> 
> 
> 

All of the above is entirely within the scope of code review, and is exactly the type of critical thinking that humans don't exercise when they delegate it to AI.

###### [Glad-Champion5767](https://www.reddit.com/user/Glad-Champion5767/)

 (2026-01-06 12:00:32)

I understand you wrote "My subjective, incomplete, vibes-based opinions incoming:" - But hopefully no junior or seniors developers are vibe coding at work, so im not sure how much that relates to the point i was making. 

"All of the above is entirely within the scope of code review, and is exactly the type of critical thinking that humans don't exercise when they delegate it to AI."

Yes, but the person i replied to wrote "this prompt takes about the same time that it would take yourself to criticially read your own code and see what needs to change" - So while what you are saying in generally is true, for this part its not. It takes longer for us to sit and go through these scenarios than it takes a LLM, because it can search its memory and reason faster than we can. If the opposite were true, then we would not be using Opus or any other models for that sake.

I get your comment, but i think its misplaced as a reply to my comment.

###### [JoeKneeMarf](https://www.reddit.com/user/JoeKneeMarf/)

 (2026-01-06 09:33:35)

No I feel you. Junior dev here. I feel like my
programming skills are atrophying because of the increased time pressure and demand to use these tools. I’m not sure I’ll ever get to be as good as an engineer as I was hoping to be. 
I am becoming more critical and aware, but I used to spend more time thinking about writing code than reading code.

##### [vendeep](https://www.reddit.com/user/vendeep/)

 (2026-01-06 14:47:15)

how much have you used claude code? 

i disagree with your statement.

#### [witmann\_pl](https://www.reddit.com/user/witmann_pl/)

 (2026-01-06 07:16:32)

I've been using the BMAD Method on my project and its code-review slash command is pretty powerful too - it checks the git diff against the story specs, assigns high/medium/low severity flags to issues and generally works well (however it works better if executed using a different LLM than the one used to write the code). Here's the source code for inspiration <https://github.com/bmad-code-org/BMAD-METHOD/tree/main/src%2Fmodules%2Fbmm%2Fworkflows%2F4-implementation%2Fcode-review>

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:36:19)

That's a good collection of prompts. I see you have code-rabit config in there as well? have you compared the two approaches

###### [witmann\_pl](https://www.reddit.com/user/witmann_pl/)

 (2026-01-06 07:39:25)

I haven't used CodeRabbit. I imagine the BMAD Method creator (or some other contributor) added support for it.

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:42:34)

I like the details of the prompt, but does the agent ever ignore some of these. Too many instructions to follow type of thing?

###### [witmann\_pl](https://www.reddit.com/user/witmann_pl/)

 (2026-01-06 09:13:22)

The review quality depends on the model used. Claude often approves changes that gpt Codex rejects. Codex is more picky (sometimes too picky, but I prefer this way than ignoring bigger issues).

##### [NO\_Method5573](https://www.reddit.com/user/NO_Method5573/)

 (2026-01-06 13:30:12)

Smartest thing I've heard

#### [Practical-Customer16](https://www.reddit.com/user/Practical-Customer16/)

 (2026-01-06 06:29:24)

I always run into issues with Claude as I have a big project that I do and I have like 100 iterations since 2 weeks to fix issues and inconsistencies. There are a lot I am asking but sometimes I feel that whatever I tell there is also always something broken here or there. I am not a programmer but I try to have a proper artitechtiture. 

What I have been run continuous issue is that we may have different menus and I have the same thing to be run in both menus for a reason, instead of Claude just call the main function and have one source of truth, Claude replicates the same code one more time so if we do any adjustment later in one place the other place left off with inconsistencies.

Please share if there is lesson learned from your side as it is very tiring for me but will try to find my way. I don’t use anything other than Claude for simplicity.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:06:44)

the duplication problem you're describing is really common, oftentimes Claude defaults to copying code instead of calling shared functions, and it gets worse as the project grows because it loses track of what already exists.

Few things that helped me 

1. before asking for new features, tell it to search the codebase for existing functionality that can be reused without changes. Something like "before implementing, check if we already have a function that does X"
2. when you catch duplication, ask it to "find all places where this logic is duplicated and consolidate to a single source of truth"

###### [Calamero](https://www.reddit.com/user/Calamero/)

 (2026-01-06 08:28:08)

The latter is dangerous. I’d take it slower there and have it explain why it thinks there are duplicate logic and how it would change the architecture to prevent it, and make sure unit and e2e test cover the refactor sufficiently and make sure I understand the proposed implementation plan before executing.

###### [Practical-Customer16](https://www.reddit.com/user/Practical-Customer16/)

 (2026-01-06 08:48:53)

There are also something called fallback, so if Claude for any reason didn’t find the info or there is an error it falls back to some default values. Looks like Claude wants to get the job done and tick the box rather than doing the right thing, is this fallback heavily used in programming?

###### [Calamero](https://www.reddit.com/user/Calamero/)

 (2026-01-06 12:32:28)

It is a common pattern but depends a lot on the context if it makes sense. Suppose you want to defect user language, and when that fails you fall back to the os language and when that fails you fall back to English as default - that usually makes sense.

But when your db connection silently falls back to localhost… the fallback is a dangerous hack.

##### [Calamero](https://www.reddit.com/user/Calamero/)

 (2026-01-06 08:25:03)

Probably your architecture is difficult to reason about, could be the structure, could be more simple things like naming convention of variables and functions. Having bad naming can really confuse the ai just like it confused humans.

#### [Fine-State5990](https://www.reddit.com/user/Fine-State5990/)

 (2026-01-06 08:24:48)

so toxic can be useful?

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 08:33:55)

agents have learnt from the toxicity on the internet, so it might be trick worth trying for a good reason?

#### [Ellsass](https://www.reddit.com/user/Ellsass/)

 (2026-01-06 08:32:33)

I’ve done something similar when asking it to review a code base. “This code was written by a team of senior devs who all want to become principal engineers. You are a principal engineer who is mentoring them. Point out areas where they can improve.”

#### [No\_Cockroach\_7783](https://www.reddit.com/user/No_Cockroach_7783/)

 (2026-01-06 09:16:48)

Been running a similar workflow for months. What's interesting is that the adversarial prompt finds different classes of bugs than the "friendly" review. Friendly mode catches logic errors and obvious edge cases. Adversarial mode catches architectural issues - tight coupling you didn't notice, missing abstractions, error paths that go nowhere.

The real insight though: after using this for a while, I've started writing prompts differently up front. I explicitly ask for error handling patterns I know Claude tends to skip - network timeouts, null checks, concurrent access. The adversarial review still catches stuff, but the first pass is cleaner.

Curious if others have found their prompt style evolving in response to what reviews consistently catch?

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 09:37:07)

What all kinds of issues do you prefer to find in each PR? Architectural issues make sense for sure, but for me the biggest is regression. 

Curious, what other patterns does Claude tend to skip?

#### [cleverusernametry](https://www.reddit.com/user/cleverusernametry/)

 (2026-01-06 09:24:13)

Huh I swear I saw the same post a week ago?

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 09:30:17)

but an entirely new prompting strategy

#### [Pangomaniac](https://www.reddit.com/user/Pangomaniac/)

 (2026-01-06 14:51:03)

I simply ask the IDE to roast the code. The results are nice.

#### [Fuzzy\_Pop9319](https://www.reddit.com/user/Fuzzy_Pop9319/)

 (2026-01-06 16:18:34)

I am a senior dev and here is one for that

LLM-GENERATED CODE AUDIT: Review this C# file for typical mistakes and anti-patterns made by language models (LLMs) such as ChatGPT, Copilot, Gemini, etc.

LLM-SPECIFIC ISSUES TO CHECK:

• Duplicate code: repeated methods, classes, or property definitions

• Incomplete implementation: empty methods, TODOs left, partial stubs

• Unused variables, parameters, or fields

• Wrong or missing async/await usage

• Incorrect DI patterns: services injected but not used, or not injected but used

• Navigation property issues: missing .Include() on EF queries for navigation props

• Exception swallowing: catch blocks with no handling, or only logging

• Missing or broken null checks (especially after casting or service lookups)

• Blind catch-all: catch (Exception) without justification

• Redundant/redundant usings, excessive using directives

• Unintentional synchronous I/O or blocking in async methods

• Potential resource leaks (e.g., missing using/Dispose for streams, contexts)

• Service lifetime mismatch: long-lived services holding short-lived dependencies

• Poor naming: generic or placeholder names (e.g., 'myService', 'var1'), uninformative summaries

• Overly broad access: public fields/methods that should be private or internal

• Inconsistent error or return patterns: sometimes returns null, sometimes throws

If no issues: {"fileName": "[name]", "llmIssues": [], "summary": "No typical LLM issues detected"}

#### [SkullRunner](https://www.reddit.com/user/SkullRunner/)

 (2026-01-11 00:52:48)

Why not simply prompt better in the first place and include standards for your project so it’s doing this upfront not burning tokens doing after the fact.

#### [Coded\_Kaa](https://www.reddit.com/user/Coded_Kaa/)

 (2026-01-06 05:46:54)

Will probably create a slash command for this

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 05:48:29)

You'll need to switch to the Max plan

###### [Coded\_Kaa](https://www.reddit.com/user/Coded_Kaa/)

 (2026-01-06 06:44:28)

What?! Before I can create a slash command?

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 06:48:31)

i meant, the reviews can be super expensive in terms of tokens, and so are the fixes, which further need to be reviewed.

###### [Coded\_Kaa](https://www.reddit.com/user/Coded_Kaa/)

 (2026-01-06 06:48:55)

Oh ok, makes sense

###### [crystalpeaks25](https://www.reddit.com/user/crystalpeaks25/)

 (2026-01-06 07:22:20)

you can just wrap your prompt as is in a slahscommand its not gonna be expensive token wise.

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:28:25)

but here's my contention with cli powered reviews. They often don't maintain any sort of full code call Graph or local RAG. How effective do you think these cli tools are at understanding the full repo. More importantly - what are the reasoning effort levels / guarantees?

###### [crystalpeaks25](https://www.reddit.com/user/crystalpeaks25/)

 (2026-01-06 07:53:37)

thats where tools come in, RAG or GraphRAG is overkill, all you need is LSP, ripgrep, ast-grep and access to other terminal tools. you conflate Memory in the form of RAG and GraphRAG as a prerequisite to understanding.

alot of folks here are using claude code to build and maintain and refactor large codebases in vanilla, meaning no GraphRAG and RAG. And this was the main thesis behind Claude Code, when everyone was implementing RAG and Graphrag in their coding agents somehow Claude Code came out on top.

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 08:00:47)

nice looks like claude LSP is off by default and is enabled via an environment variable ENABLE\_LSP\_TOOL=1 . btw, LSP support lets Claude *query* the call relationships it needs (via “find references” and similar), but it does not constantly maintain or stream a full, global call graph into every code‑review prompt. Seems like it may not find everything needed where I would Ideally like to stuff call graph or summary if possible.

###### [crystalpeaks25](https://www.reddit.com/user/crystalpeaks25/)

 (2026-01-06 08:13:55)

sure but normally a coding agent will use the tool x amount of times to achieve its goal. like sometimes i see an agent trying to open a file thats too big so it gets an error then it starts reading the file in batches

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 08:23:46)

I like the file reader example, but I'm not sure the code retrieval part is explicit at each step.

#### [memetican](https://www.reddit.com/user/memetican/)

 (2026-01-06 05:58:23)

Similar experience with SDD. I'm building a DB+MCP-based spec-driven dev setup and it works incredibly well- but because I'm forcing it to describe it's thinking and processes I keep catching little oversights, assumptions, the occasional hallucination...

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 06:16:54)

the spec-driven approach is interesting because it forces the reasoning into the open where you can actually catch it. With pure vibe coding the assumptions are buried in the implementation — you don't see them until something breaks.

Curious about your DB+MCP setup. Are you storing the specs alongside the code or using the graph to track how requirements flow through to implementation? I've been messing with call graph stuff and wondering if there's a way to flag when Claude's implementation drifts from what the spec actually said.

###### [memetican](https://www.reddit.com/user/memetican/)

 (2026-01-06 09:45:54)

I've centralized it so that I can manage multiple projects in one place, with all the artifacts as easily-edited documents. The MCP does the translation, and knows the basic DB structure of the documents, how to add a Bug, retrieve a Feature. The basic shift for me so far is that I deliver almost nothing in the prompt, instead I point Claude at the feature doc I want to implement, and most communication between Claude and I are through those document artifacts. 

Somewhat game changing because I can always review, adjust, resubmit, change the model, use it to churn out docs with a different agent. Working well, we'll see where it goes.

I started this project because my markdown-based SDD setups were getting too difficult to navigate, and too closed off for the team. But also as an experiment- I'm building an MCP for project management, and the first project I'm managing is itself. So all work is cyclical and every feature I add is immediately available to help build the next feature. Fun.

##### [Original\_Finding2212](https://www.reddit.com/user/Original_Finding2212/)

 (2026-01-06 06:23:04)

Have you tried Kiro by Amazon? 
Their SDD is superb

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 06:31:07)

this seems interesting

#### [crystalpeaks25](https://www.reddit.com/user/crystalpeaks25/)

 (2026-01-06 06:32:34)

this is why i have a grumpy-gopher slashcommand

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:00:19)

What does the command trigger?

###### [crystalpeaks25](https://www.reddit.com/user/crystalpeaks25/)

 (2026-01-06 07:18:32)

jsut telling claude that our colleague "Greg" has submitted a PR. and a bit of backstory on what greg has done in the past for flavor. But mostly just a specific workflow for technical analysis of the change/PR.

essernitalyl you can just wrap your whole prompt abov ein a slash command so you can just run it anytime in a repeatable manner

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:33:44)

but how effective can that possibly be. I have realized asking it to critique, or to find issues, sarcastic opens a can of worms/bugs you are not ready to fix

###### [Historical-Lie9697](https://www.reddit.com/user/Historical-Lie9697/)

 (2026-01-06 07:49:16)

Just tell them Grok wrote the code. Claude hates Grok and will pick the code apart.

#### [naxmax2019](https://www.reddit.com/user/naxmax2019/)

 (2026-01-06 07:06:12)

As mentioned, code-review is great. 

What I've done is added a skill to do code reviews as part of commits. There are several guardrails but code review is one important part. 

Here is the full repo.. [www.github.com/alinaqi/claude-bootstrap](http://www.github.com/alinaqi/claude-bootstrap) 

just install it and use it with /initialize-project 

It may not fit with your stack but it works super well for me.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:35:54)

looks very cool, I'm impressed

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 07:31:43)

This seems super interesting and exhaustive, what are you doing for context selection? or does everything get included automatically as context?

###### [naxmax2019](https://www.reddit.com/user/naxmax2019/)

 (2026-01-06 07:49:43)

It's tricky and I don't have a solution. However, for me what works is that I focus on narrow todos and those basically enforce or help with context. i also have

- [current-state.md](http://current-state.md) - what im working on rn, next steps, blockers

- [decisions.md](http://decisions.md) - architectural choices so i dont re-explain why we picked X over Y

- [code-landmarks.md](http://code-landmarks.md) - important file locations for quick reference

i update [current-state.md](http://current-state.md) pretty frequently. i think hygine is super important. this is very powerful but needs proper hygine.

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 08:04:42)

Is there a way these can be automatically generated using AI for the most part + HITL approval? maybe look at agent chat history in claude etc or summarize the entire repo and generate these?

#### [srryshaktimaan](https://www.reddit.com/user/srryshaktimaan/)

 (2026-01-06 08:14:54)

Apparently there's a bug in cursor that introduces errors (reversing fixes, indentation etc) on restoring a previous checkpoint. I tried a few reviewers such as code rabbit and greptile but I felt like turingmind came out at the top in terms of detecting the non obvious stuff. Don't get me wrong, You don't get all the linter stuff but it seemed to allow multiple focused review types, which are very effective in my opinion.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 08:26:11)

what was it that you were not able to do in your cli?

###### [srryshaktimaan](https://www.reddit.com/user/srryshaktimaan/)

 (2026-01-06 08:43:24)

Frankly, I felt lazy typing all the prompts every time and still wanted to make sure my code was robust, so instead of running local reviews ( i'm not that consistent) I installed a github based pr reviewer which helps guarantees a level of quality every single time

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 09:32:36)

what reviewer did you use? frankly my concern is the local cli does not guarantee full context without explicit context management controls.

###### [srryshaktimaan](https://www.reddit.com/user/srryshaktimaan/)

 (2026-01-06 09:42:00)

I tried coderabbit free and [turingmind.ai](http://turingmind.ai) for a month before settling with the latter. I'd recommend turingmind if you want high level stuff as its not as nit picky as coderabbit, but coderabbit provides auto fixes in github itself, which I don't prefer. I'd rather dump the review in my claude or cursor and let it triage the response from turingmind and most of the times they were pretty on spot.

#### [naxmax2019](https://www.reddit.com/user/naxmax2019/)

 (2026-01-06 08:19:09)

Yup I’m experimenting with summarization etc. I tried creating graph knowledge base but it didn’t work well .. will post updates :)

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 08:32:05)

what graph database would you recommend for something like this? anything that serves both graph + rag use cases and is fast?

###### [srryshaktimaan](https://www.reddit.com/user/srryshaktimaan/)

 (2026-01-06 08:46:21)

frankly neo4j is too slow here

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 08:56:44)

i agree, but the only other options are in memory based graph + vector.

#### [Brilliant\_Call\_421](https://www.reddit.com/user/Brilliant_Call_421/)

 (2026-01-06 08:28:44)

I can attest this is absolutely the way to catch issues!

#### [tarkinlarson](https://www.reddit.com/user/tarkinlarson/)

 (2026-01-06 08:31:34)

Why other rub a code review or qa agent over it and while you're at it and agent that follows the asvs / owasp

#### [nimag42](https://www.reddit.com/user/nimag42/)

 (2026-01-06 08:57:51)

I usually tell it to review like it were Linus Torvalds, works well

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 09:07:54)

coding agents run on low effort fast sprints of reasoning, code review agents work at the other end of the spectrum. It may not be necessary to supply the full context, but one may not want to take chances with one's code reviews.

#### [DrAz57](https://www.reddit.com/user/DrAz57/)

 (2026-01-06 09:11:44)

great !

#### [freshWaterplant](https://www.reddit.com/user/freshWaterplant/)

 (2026-01-06 09:34:22)

Then use another prompt.

I use `rate and critique the output, Do a QA.`

I need a certain about of perfection without going crazy about it. This helps me. I also give it feedback when it goes to far that it commits to memory. 

Doing a QA with every revision speeds up the QA process at the end

##### [freshWaterplant](https://www.reddit.com/user/freshWaterplant/)

 (2026-01-06 09:35:58)

I also have an adveserial project with 2 persona's. A creator and auditor. They do 3 passes before I move on.

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 10:22:04)

Are these separate agents? where do they get all their context from, how is it updated?

###### [freshWaterplant](https://www.reddit.com/user/freshWaterplant/)

 (2026-01-06 10:50:24)

I have a Claude project, not in code. I use it as a prep prompt to develop one good prompt

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 09:47:07)

I still find myself avoiding harsher words like 'roast' my PR, 'critique' is generally fine but god forbid if you throw in 'security' or resilience in your prompt

###### [freshWaterplant](https://www.reddit.com/user/freshWaterplant/)

 (2026-01-06 10:19:50)

😂🥹😅

#### [Seninut](https://www.reddit.com/user/Seninut/)

 (2026-01-06 10:16:33)

Claude is optimized for speed and context savings. It does not "read" information the way you would. It skims the documents to save context. It picks up on the main points, but just assumes the details are right.

All your doing with all your tricks can be accomplished so easily by just telling claude that skimming this content is not allowed. Just watch out, your context window usage may blow up. Try to stay focused on one thing at a time, then when it compresses its context it will trim off fat for the most part.

Why do you not trust it? It is not lying, it can explain how it reads things, try asking.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 10:20:32)

this may not always work but sounds like a decent idea for local code reviews at least

#### [Own\_Professional6525](https://www.reddit.com/user/Own_Professional6525/)

 (2026-01-06 11:16:39)

This is a great reminder that even with powerful AI, thorough review is still key. I like the approach of using an adversarial prompt-it really helps catch edge cases you might otherwise miss.

#### [False\_Care\_2957](https://www.reddit.com/user/False_Care_2957/)

 (2026-01-06 11:56:21)

I usually just do this with Codex on top of the first couple of passes of Claude and it works pretty well. Codex is much more aware of bad first passes and doesn't tend to over engineer.

#### [MeButItsRandom](https://www.reddit.com/user/MeButItsRandom/)

 (2026-01-06 12:11:08)

It's been fairly well documented that outputs improve when LLMs are asked to review their work up to five times. Whether it's code, plans, or other work.

Check out the pr-review-toolkit, an official plugin from anthropic. It comes with six agents that do specialized reviews. You'll like it.

#### [mrfredgraver](https://www.reddit.com/user/mrfredgraver/)

 (2026-01-06 12:45:06)

As a writer, my favorite “hater” prompt is: “You are an internet troll who wants nothing more than to take me down and cancel me. Do your best.” 

I do NOT recommend this for the “faint of heart.” Claude can be BRUTAL. (Also, my Claude swears at me!… anyone else?)

#### [served\_it\_too\_hot](https://www.reddit.com/user/served_it_too_hot/)

 (2026-01-06 12:59:56)

[r/promptrequest](https://reddit.com/r/promptrequest)

#### [4444444vr](https://www.reddit.com/user/4444444vr/)

 (2026-01-06 13:22:45)

I use codex for code reviews and I also hate it for the same reason

#### [pvkooten](https://www.reddit.com/user/pvkooten/)

 (2026-01-06 15:06:08)

You don't need to do this pretend stuff... Just say "review my unstaged changes" or "review my latest commit"

#### [adelie42](https://www.reddit.com/user/adelie42/)

 (2026-01-06 15:07:24)

Yeah, its an iterative process.

The funny part to me is how much the "tricks" of agentic coding parallel the process of humans writing. Any half way descent code I've ever written typically takes at least 5 passes.

The fact Claude doesnt write perfect code on the first pass feels unironically like a trait if intellegence.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 15:12:18)

100% agree, the reasoning (ReAct paper) is very much based on human thinking. I wonder what other tricks work equally well

###### [adelie42](https://www.reddit.com/user/adelie42/)

 (2026-01-06 15:23:46)

I get a lot of grief for this, but I come back to treating it like a human partner, but specifically help it like you would help a human. DOCUMENT EVERYTHING relevant from features and architecture to high level goals and plans. Frame uncertainty in ideas with uncertainty, and ask more questions in the spirit of collaboration than simply telling it what to do.

Getting it to do something is easy. Getting people to do things is easy. Having a meeting of the minds where working together results in the vision in your head resulting in working code that does what you want is where the work is. And honestly, I find that challenging enough just doing that with myself. With all those considerations and when proper planning and collaboration are in place, Claude is a fantastic partner.

But it isn't a mind reading genie spinning magic. It's intelligent, perfectly imperfect intelligence. And at very least thinking that way has been pragmatic.

#### [HibiscusSabdariffa33](https://www.reddit.com/user/HibiscusSabdariffa33/)

 (2026-01-06 15:30:42)

You use Claude on GitHub? How? I’m switching to Claude Pro from GPT on the 21st.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 16:16:41)

You can if its hosted on a server. Some people in the comments found turingmind AI helpful, not sure if it supports running claude Agents, but it may be worth checking out.

#### [JsonPun](https://www.reddit.com/user/JsonPun/)

 (2026-01-06 15:33:02)

just use code rabbit to review your code much more effective in my option, since you don’t want the one writing the code also reviewing it

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-06 16:00:53)

yeah I prefer using a different model for review than the one I used to code.

#### [bostondave](https://www.reddit.com/user/bostondave/)

 (2026-01-06 16:09:52)

Thank you, great idea - trying this today! 

If I could post an image to represent this prompt, it would be the Comic Book Guy from The Simpsons. 

Every time I think of "Senior Dev," it brings me back to my early career, when they were all the comic book guy from The Simpsons.

#### [oh\_jaimito](https://www.reddit.com/user/oh_jaimito/)

 (2026-01-06 16:14:29)

RemindMe! tonight at 8:00 p.m..

##### [RemindMeBot](https://www.reddit.com/user/RemindMeBot/)

 (2026-01-06 16:15:09)

I will be messaging you in 16 hours on [**2026-01-07 08:00:00 UTC**](http://www.wolframalpha.com/input/?i=2026-01-07%2008:00:00%20UTC%20To%20Local%20Time) to remind you of [**this link**](https://www.reddit.com/r/ClaudeAI/comments/1q5a90l/so_i_stumbled_across_this_prompt_hack_a_couple/ny11ms0/?context=3)

[**CLICK THIS LINK**](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5Bhttps%3A%2F%2Fwww.reddit.com%2Fr%2FClaudeAI%2Fcomments%2F1q5a90l%2Fso_i_stumbled_across_this_prompt_hack_a_couple%2Fny11ms0%2F%5D%0A%0ARemindMe%21%202026-01-07%2008%3A00%3A00%20UTC) to send a PM to also be reminded and to reduce spam.

Parent commenter can  [delete this message to hide from others.](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Delete%20Comment&message=Delete%21%201q5a90l)

---

| [Info](https://www.reddit.com/r/RemindMeBot/comments/e1bko7/remindmebot_info_v21/) | [Custom](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=Reminder&message=%5BLink%20or%20message%20inside%20square%20brackets%5D%0A%0ARemindMe%21%20Time%20period%20here) | [Your Reminders](https://www.reddit.com/message/compose/?to=RemindMeBot&subject=List%20Of%20Reminders&message=MyReminders%21) | [Feedback](https://www.reddit.com/message/compose/?to=Watchful1&subject=RemindMeBot%20Feedback) |
| --- | --- | --- | --- |

#### [mihajlo\_null](https://www.reddit.com/user/mihajlo_null/)

 (2026-01-06 19:46:16)

I used claude to create a skill called "code-quality skill" and it describes a lot of stuff, SOLID, no fake tests, etc and it always catches issues with architecture, code duplication and so on, I guess similar results to yours.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 01:20:07)

care to share it with others?

###### [mihajlo\_null](https://www.reddit.com/user/mihajlo_null/)

 (2026-01-07 11:00:41)

[here you go](https://github.com/nostixx/claude-code-skills/tree/main)

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 20:10:43)

This is great, you’ve bundled together code review standards, debugging methodology, architectural philosophy, library/tooling opinions. One thing I noticed is hard-coding library choices can be fragile, eg - recommending lodash in 2026 is debatable - its prone to prototype pollution bugs

###### [mihajlo\_null](https://www.reddit.com/user/mihajlo_null/)

 (2026-01-07 20:47:20)

Thanks! True, I didn't spend too much time on it, feel free to open pull requests.

#### [Rhinoseri0us](https://www.reddit.com/user/Rhinoseri0us/)

 (2026-01-06 21:03:18)

Isn’t this a repost 🤔

#### [hellno-o](https://www.reddit.com/user/hellno-o/)

 (2026-01-06 21:14:00)

the session that wrote the code is the worst one to review those changes.

It's carrying all the context that led to those decisions - which means it has the same blind spots. A fresh session with just the diff and no prior context catches different things.

my workflow now:

1. build feature in one claude code session
2. Start new session in same worktree, check the diff
3. review using subagents similar to what you describe
4. different session (or first one if I'm in a rush) for the fix

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 01:21:31)

This is an excellent point

#### [Terrible\_Wave4239](https://www.reddit.com/user/Terrible_Wave4239/)

 (2026-01-06 21:14:14)

Love it. I now have these two prompts (in succession) in Keyboard Maestro:

ccbrutal: 

Do a git diff a nd pretend you're a senior dev doing a code review and you HATE this implementation. What would you criticize? What edge cases am I missing?

ccbrut2:

(1) Please summarise the learnings from this that can be generalised, then find the best place to store them in CLAUDE.m d or related CLAUDE\_[x].md files.

(2) Please generate a detailed implementation plan as a markdown file.

[Had to put a space in the CLAUDE dot md mention]

I don't just apply them to the most recent work, but am going through various sections of my project one by one, and applying the learnings to my CLAUDE md files (which are now refactored for different areas of concern.

#### [emptyharddrive](https://www.reddit.com/user/emptyharddrive/)

 (2026-01-06 22:06:32)

Well thank you for sharing this. This is a GREAT way to catch problems.

It seems so convinced that it did a great job, then I tell it to be an a\*\*hole boss and "rip it apart" and it finds all the bugs, almost as though it was too polite to do so before.... "You're absolutely right!"................ 

Great stuff, this is now a /command in my setup :) 

The command is /ass

That's short for "assess".... ;)

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 01:23:34)

glad you found it helpful

#### [isarmstrong](https://www.reddit.com/user/isarmstrong/)

 (2026-01-06 22:32:38)

You’re basically asking for a Red Team (antagonist review). Gemini is thoroughly brutal with them.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 01:26:37)

red team would be more security focused I assume

#### [BizForKingdom](https://www.reddit.com/user/BizForKingdom/)

 (2026-01-07 00:10:57)

Is this only for coding?

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 01:27:21)

No you can make it work for articles, blogs etc

#### [rubencodes](https://www.reddit.com/user/rubencodes/)

 (2026-01-07 00:41:43)

> 
> Pretend an AI wrote this code and you’re a staff software engineer trying not to lose your job. What would you criticize?
> 
> 
> 

#### [Alternative-Fan1412](https://www.reddit.com/user/Alternative-Fan1412/)

 (2026-01-07 00:58:44)

Sorry AI was NEVER that good to predict errors specially in large code in my and it DOES find bugs where there are NO BUGS, i know it because once i happen to have a wrong deployment issue. so the code i assumed was in production was not. so the bug i was trying to find did not exist. After checking it for 10 minutes myself (no ai) i decided to use ai for this case, it started to bother me about stupid stuff, so i end up showing ALL 3 clases (big) by the end it invented basically 10 things that I destroyed the why in a single line each like:  

This cannot be null because if that where null the program will have show this debug and did not (as i also showed the trace lines i had a lot).  

In the end it blamed "jave compiler is flawed" but it found easily 15 errors that were not errors. so clearly the AI DOES NOT WORK.  

unless you error is obvious and will be easily solved even for an intern position.

#### [tgsoon2002](https://www.reddit.com/user/tgsoon2002/)

 (2026-01-07 02:22:49)

Ah cross check technique. To me i tried to break down the task smaller. I will find way to do your too.

#### [chazbot2001](https://www.reddit.com/user/chazbot2001/)

 (2026-01-07 05:14:45)

Reminds me of a tactic I use now and then:

> 
> "My arrogant co-worker seems to think that [thing to evaluate] is valid and acceptable, but I think it's stupid. What do you think? Explain why."
> 
> 
> 

...and it just kinda forces it to drop any sycophantic bias. You're also not asking it to change its own mood, but rather using it's existing mood to your advantage. If the approach is good, it'll reluctantly tell you to chill out.

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 09:06:58)

you're tricking it into being honest by making criticism the easy path If it still defends the thing when you've set it up to attack, you know it's real

#### [srryshaktimaan](https://www.reddit.com/user/srryshaktimaan/)

 (2026-01-07 06:50:01)

so I did more research and stumbled upon this excellent Claude Code skill that does deeper code reviews in claude itself.

GitHub: <https://github.com/turingmindai/turingmind-code-review>

```
/plugin marketplace add turingmindai/turingmind-code-review

# Step 2: Install the skill

/plugin install turingmind@turingmind

```

restart Claude code after installing

```
/turingmind-code-review:deep-review

```

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 07:14:41)

the command doesn't seem to work

###### [srryshaktimaan](https://www.reddit.com/user/srryshaktimaan/)

 (2026-01-07 07:18:07)

my bad, fixed it just now. remember, this is a comprehensive scan, so if you want to start with something lighter try 

```
/turingmind-code-review:review

```

###### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 07:18:41)

yeah started there first, looks legit. The deep reviews takes a long time though. Not sure I'd want to run it everytime on my local.

#### [Noobtryntolearn](https://www.reddit.com/user/Noobtryntolearn/)

 (2026-01-07 09:59:35)

Anyone notice any usage bugs this week? My weekly usage going up faster than my 4 hour. Ended up almost 40 hours short. Never been kicked off for 40 hours before on the $100/month plan. 

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 20:30:57)

sometimes it consumes tokens really fast. Could just be your code's complexity or the version of claude may have changed

#### [IntroductionBig8044](https://www.reddit.com/user/IntroductionBig8044/)

 (2026-01-07 21:02:56)

Is this massively different than using BMAD?

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-07 21:13:08)

BMAD seems to cover a lot of areas, this one relies purely on the personality prompt of the agent.

#### [onetimeiateaburrito](https://www.reddit.com/user/onetimeiateaburrito/)

 (2026-01-08 02:47:00)

Do you need to use GitHub for this? I'm just using Claude to code a personal project, have no background or education in CS, and know nothing about code (syntax, normal practices etc) so I'm not planning on releasing or trying to sell. But I would like to use something like this to try and clean things up after I add a feature that breaks everything and I forget what the feature was while I'm fixing everything that was broken

##### [cleancodecrew](https://www.reddit.com/user/cleancodecrew/)

 (2026-01-08 04:43:32)

These are claude skills you can run locally

#### [HibiscusSabdariffa33](https://www.reddit.com/user/HibiscusSabdariffa33/)

 (2026-01-08 15:25:24)

I used this with GitHub copilot and it’s been helping me start to fix what’s been missing in my repos. And it’s been helping me turn my custom GPTs to the start of software! THANKS!

#### [gitGudBud416](https://www.reddit.com/user/gitGudBud416/)

 (2026-01-07 02:50:23)

Just gargling that ai dick
