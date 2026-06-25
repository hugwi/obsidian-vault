---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, ai-agents]
tags:
  - efficiency
  - tools
source: readwise
created: 2026-06-23
rating: 
action: 
theme: workflow-phases-gates
subtheme:
  - harness-loops
  - plan-phase
---

# I built a coding agent that gets 87% on benchmarks with a 4B parameter model, here's how

![rw-book-cover](https://preview.redd.it/ibtta0vvcu1h1.png?width=140&amp;height=78&amp;auto=webp&amp;s=30cecc42a1c810ff5e569a8fa1c8a608d9caca3d)

## Metadata
- Author: [[Glittering_Focus1538]]
- Full Title: I built a coding agent that gets 87% on benchmarks with a 4B parameter model, here's how
- Category: #articles
- Summary: A developer built SmallCode, a coding agent that scores 87% on benchmarks using a 4 billion parameter model by combining multiple tools into one and instantly checking code for errors. This approach helps small models work reliably by breaking tasks into simpler steps and escalating hard problems to bigger models if needed. SmallCode runs locally with OpenAI-compatible endpoints but lacks some advanced features like multi-session support.
- URL: https://www.reddit.com/r/LocalLLaMA/comments/1tgecrq/i_built_a_coding_agent_that_gets_87_on_benchmarks/?share_id=LJGkLuHLExZdTxg2MDriA&utm_content=2&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1

## Full Document
**[r/LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/)**

### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 06:38:11)

![](https://i.redd.it/ibtta0vvcu1h1.png)

I was frustrated that every coding agent (OpenCode, Cursor, Claude Code) assumes you're running GPT-5.4 or Claude Opus. If you try them with a local model like Gemma or Qwen they fall apart. I find that often tool calls fail, context overflows, multi-step tasks collapse.

So I built SmallCode. It's designed from the ground up for small local models.

**The result:** 87/100 benchmark tasks pass with a Gemma 4 model that only activates 4B parameters per token. OpenCode scores ~75% with 14B models. The harness does the heavy lifting, not the model size.

**How it works (the tricks that make small models reliable):**

* **Compound tools:** Instead of making the model chain 4 tool calls (find file → read file → edit file → verify), SmallCode gives it one tool that does all 4. Small models lose coherence after 3+ sequential calls. This cuts failures in half.
* **Improvement loop:** Every time the model writes code, SmallCode instantly compiles/lints it. If it fails, it feeds the errors back automatically. The model doesn't need to be smart enough to get it right first try — it just needs to fix errors when shown them.
* **Decompose on failure:** If the model fails the same thing twice, SmallCode stops retrying and instead breaks the problem into smaller pieces. "Fix this 200-line file" becomes "fix line 45 only."
* **Escalation:** If even decompose fails and you have a Claude/OpenAI key configured, it auto-escalates to the bigger model for just that one task. You stay local 95% of the time, cloud 5%.
* **Token budgeting:** Small models have 32k-256k context. SmallCode never dumps a whole file in. It summarizes, truncates, and manages every token so the model never sees "..." truncation in the middle of important code.
* **Code graph:** Instead of grep-searching your codebase, SmallCode indexes your code into a symbol graph (functions, classes, who-calls-what). When you ask "how does auth work," it walks the graph and returns just the relevant connected code — not 15 random file snippets.

**What it looks like:**

Full-screen terminal UI (like OpenCode/vim), scrollable chat, command palette with `/`, plugin system, persistent memory across sessions.

**What it doesn't do:**

* No LSP integration (yet)
* No multi-session (yet)
* No desktop app
* Doesn't compete with Claude Code for frontier model users

**Install:**

```
npm install -g smallcode
cd your-project
smallcode

```

Point it at LM Studio, Ollama, or any OpenAI-compatible endpoint.

MIT licensed, everything's on GitHub: <https://github.com/Doorman11991/smallcode>

Happy to answer questions about the architecture or benchmark methodology.

#### [WithoutReason1729](https://www.reddit.com/user/WithoutReason1729/)

 (2026-05-18 12:30:15)

Your post is getting popular and we just featured it on our Discord! [Come check it out!](https://discord.gg/PgFhZ8cnWW)

You've also been given a special flair for your contribution. We appreciate your post!

*I am a bot and this action was performed automatically.*

#### [Orolol](https://www.reddit.com/user/Orolol/)

 (2026-05-18 08:29:21)

> 
> OpenCode scores ~75% with 14B models. 
> 
> 
> 

Which Model ? Which Benchmark ? 

If you want to be taken seriously,you have to be precise enough so people are able to reproduce your results.

##### [Rustybot](https://www.reddit.com/user/Rustybot/)

 (2026-05-18 14:06:08)

TrustMeBro-2.1-hard

##### [sillib](https://www.reddit.com/user/sillib/)

 (2026-05-18 20:04:35)

That’s the real question that needs to be answered, what fucking benchmark test was used 

###### 

##### 

#### [rinaldo23](https://www.reddit.com/user/rinaldo23/)

 (2026-05-18 06:51:07)

Interesting. I think there is a trend towards using smaller, more focused models for specific tasks. Extraordinary claims require extraordinary evidence though.

##### [JollyJoker3](https://www.reddit.com/user/JollyJoker3/)

 (2026-05-18 09:58:40)

Pricing will make smaller models good eventually. This project does stuff I've been meaning to try myself so I'll have to give it a look.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 06:57:06)

Feel free to try it out with gemma 4 e4b, you'll be amazed how well it codes.

###### [1\_4\_1\_5\_9\_2\_6\_5](https://www.reddit.com/user/1_4_1_5_9_2_6_5/)

 (2026-05-18 08:20:50)

I'm going to try this out. I've been building something very similar, which works well for the same reasons, so I fully believe you're onto something here.

###### [someonesmall](https://www.reddit.com/user/someonesmall/)

 (2026-05-18 10:30:48)

Did you also test with Qwen?

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 10:33:42)

Yes qwen runs smoothly. Try it out. should work with any model made after qwen 2.5 14b

###### 

###### [ismail\_the\_whale](https://www.reddit.com/user/ismail_the_whale/)

 (2026-05-18 12:46:52)

> 
> gemma 4 e4b
> 
> 
> 

waht. extremely intrigued

###### [geek\_404](https://www.reddit.com/user/geek_404/)

 (2026-05-18 14:51:46)

Does it work with all languages or is it better with specific ones? I have been toying with the idea of doing a fine tune of a model to make it an expert in rust programming. I hadn’t thought about making the harness better. Kudos and look forward to trying it out.

###### 

###### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-05-18 07:32:03)

[deleted]

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 07:33:53)

No worries, you aren't the first to accidentally make that mistake today lol.

###### 

##### [hishazelglance](https://www.reddit.com/user/hishazelglance/)

 (2026-05-18 19:01:14)

There are, Nvidia has a great paper about Small Language Models (SLMs) and their use cases: <https://research.nvidia.com/labs/lpr/slm-agents/>

##### 

#### [AppealSame4367](https://www.reddit.com/user/AppealSame4367/)

 (2026-05-18 08:01:54)

How would you compare yourself to [pi.dev](http://pi.dev) or little-coder (based on [pi.dev](http://pi.dev), good swe bench 2 scores)?

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 08:04:48)

It's simple honestly, we have different goals.  

Pi/Little-Coder is a minimal harness. 4 tools (read, write, edit, bash), tiny system prompt, and it relies on the model being smart enough to figure things out. Their SWE-bench scores come from running frontier models (Claude, GPT-5) through a lightweight wrapper. The harness gets out of the way and lets the model do the heavy lifting.

SmallCode is the opposite bet, the harness does the heavy lifting so the model doesn't have to be smart. Compound tools, improvement loops, auto-validation, decompose-on-failure, token budgeting. We get 87% on our stress test with a 4B-active model. Pi would get maybe 40-50% with that same model because it doesn't compensate for the model's limitations.

###### [AppealSame4367](https://www.reddit.com/user/AppealSame4367/)

 (2026-05-18 08:41:38)

Your assessment of little-coder seems wrong to me. The swe bench benchmarks I referred to were made with Qwen3.6 27B and 35B and little-coder is an extension to pi that \_adds\_ a lot of rules and tools.

But I get your point: You try to encase a 4B in a way that it can't go wrong when editing and still produce very usable results. I will definitely try it, cause I have low vram anyway and rely on a lot of new optimizations in ik\_llama to run 35B at around 10tps output in little-coder.

###### [rpkarma](https://www.reddit.com/user/rpkarma/)

 (2026-05-18 12:30:38)

Not seems. Is entirely wrong. 

###### [AppealSame4367](https://www.reddit.com/user/AppealSame4367/)

 (2026-05-18 12:32:53)

If you wanna speak in scientific terms, you cannot rush to conclusions. Also not if you wanna be diplomatic.

OP put in honest, serious work and tried to provide a benchmark. There might be doubts, but there is no reason to punch him in the face with an "all wrong!"

###### [SummarizedAnu](https://www.reddit.com/user/SummarizedAnu/)

 (2026-05-18 15:16:54)

I mean even if he used Ai to make it. As long as it works better than it's alternatives 
I would put all my chip on it.

###### [rpkarma](https://www.reddit.com/user/rpkarma/)

 (2026-05-18 21:17:20)

It’s objectively true: his assessment of what Little Coder is is entirely wrong; it’s literally backwards. 

I passed no judgment on the rest of his work. 

###### [rpkarma](https://www.reddit.com/user/rpkarma/)

 (2026-05-18 12:29:54)

That is not at all what Little Coder is. 

###### [mister2d](https://www.reddit.com/user/mister2d/)

 (2026-05-18 12:30:04)

Pi is small with intention. It's fully extensible so you could have applied your harness concepts easily to it.

###### [Pleasant-Shallot-707](https://www.reddit.com/user/Pleasant-Shallot-707/)

 (2026-05-18 11:40:55)

Pi’s philosophy isn’t that the harness is minimal and the llm does the hard work. It’s more nuanced. Yes, you can yolo like that in Pi, but the actual philosophy is that the harness is minimal and unopinionated and easily extended so the developer can craft a harness they want to use without burning a bunch of tokens on bloated system prompts.

###### [gh0stwriter1234](https://www.reddit.com/user/gh0stwriter1234/)

 (2026-05-18 16:26:19)

Yes building this kind of thing is exactly what [pi.dev](http://pi.dev) is supposed to be able to do.

###### [brakx](https://www.reddit.com/user/brakx/)

 (2026-05-18 12:31:04)

Can you explain using your own words?

#### [OsmanthusBloom](https://www.reddit.com/user/OsmanthusBloom/)

 (2026-05-18 07:09:03)

Interesting tricks. Though I wish these could be integrated with existing tools like Pi or OpenCode instead of creating Yet Another Coding Agent. See for example [little-coder](https://github.com/itayinbarr/little-coder) which is nowadays a set of Pi extensions.

A standard benchmark instead of "87% of my self selected tasks" would be more convincing.

The README in the GitHub repo looks heavily AI generated. All the "Supported Models" are basically obsolete. This makes me wonder if this is a serious project or just AI slop.

##### [faldore](https://www.reddit.com/user/faldore/)

 (2026-05-18 09:56:01)

OpenCode is really unfriendly towards community contributions. They put up enough friction that I would just fork it instead of contributing.

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 10:11:09)

the reason for the fork is honestly because I had to re-arrange the guts, not just put on a shinier coat of paint.

###### [gh0stwriter1234](https://www.reddit.com/user/gh0stwriter1234/)

 (2026-05-18 15:59:45)

Why not just make this as an extension for [Pi.dev](http://Pi.dev)

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 16:12:08)

The governor doesn't exist elsewhere. The Bayesian tool scoring, hard fail detection, automatic decompose -> escalate pipeline. that's what makes small models actually usable for agentic work. Pi doesn't have this because it doesn't need it (it targets models that don't fail as often). You can't "add" this as an extension without reimplementing the entire agent loop.

Compound tools and 2-stage routing. SmallCode halves context overhead by routing tools in two stages and offering compound operations (read\_and\_patch, find\_and\_read). This matters when your model has 32k-128k context. 

Pi can afford to dump all tool schemas because it assumes 128k+.

That being said, many others have already proved if you're already in Pi's ecosystem and using frontier models, SmallCode probably isn't for you. 

###### [gh0stwriter1234](https://www.reddit.com/user/gh0stwriter1234/)

 (2026-05-18 16:23:10)

The whole point of pi dev is you CAN easily implement a whole different agent loop... 

###### [capsid](https://www.reddit.com/user/capsid/)

 (2026-05-18 17:24:45)

Daily pi user. I love the idea of optimizing for small models. I'm also a believer in the stuff Mario Zechner said about extra features like LSPs and MCPs affecting context observability depending on how it's implemented. Does SmallCode have a minimalist mode in line with Pi's philosophy? Is extensibility/self-modification planned? Looking forward to trying it out. 

##### [LetsGoBrandon4256](https://www.reddit.com/user/LetsGoBrandon4256/)

 (2026-05-18 12:15:18)

> 
> All the "Supported Models" are basically obsolete.
> 
> 
> 

That's probably the biggest sign that the repo is AI slop. 

Edit: 

OP has updated that section of README.md but here's the "supported models" that was originally there. Damn I missed 2024.

* Devstral Small 14B
* Mistral-Nemo-12B
* Qwen2.5-Coder-14B
* CodeLlama-13B
* StarCoder2-15B
* Phi-3-Mini

###### [HFRleto](https://www.reddit.com/user/HFRleto/)

 (2026-05-18 14:54:10)

ahaha, this section is now removed

###### [LetsGoBrandon4256](https://www.reddit.com/user/LetsGoBrandon4256/)

 (2026-05-18 14:57:34)

Now OP just need to fix their prompt so they don't constantly switch between "we" and "I". 

I gave them the benefit of doubt that they are using "we" because they are a small team or something. Nope, just a random bloke with a six-day-old GitHub account.

###### [\_TheWolfOfWalmart\_](https://www.reddit.com/user/_TheWolfOfWalmart_/)

 (2026-05-18 19:44:48)

[r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) of all places doesn't like that someone used AI to code?

Huh?

###### [a\_beautiful\_rhind](https://www.reddit.com/user/a_beautiful_rhind/)

 (2026-05-18 19:58:52)

The real "huh" is how everyone got oneshotted by an obvious self promotion post and an hours old project.

###### [LetsGoBrandon4256](https://www.reddit.com/user/LetsGoBrandon4256/)

 (2026-05-18 20:01:34)

* Reddit algorithm doing its thing
* OP bought some updoots
* [r/LocalLLaMA](https://reddit.com/r/LocalLLaMA) bros collectively decide to turn our brains off for this slop.

Sometimes it just happens.

###### 

###### 

##### [IronColumn](https://www.reddit.com/user/IronColumn/)

 (2026-05-18 18:33:34)

> 
> All the "Supported Models" are basically obsolete. This makes me wonder if this is a serious project or just AI slop.
> 
> 
> 87/100 benchmark tasks pass with a Gemma 4 model that only activates 4B parameters per token.
> 
> 
> 

this is such a weird way to say it's a moe model while implying it's e4b

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 07:10:27)

I have a partial solution for you, <https://github.com/Doorman11991/opencode-bonescript-backend>  

gives LLM's the tools they need to use my TS/NodeJS backend compiler to make more complete and secure backend code all from one .bone file.

###### [yoomiii](https://www.reddit.com/user/yoomiii/)

 (2026-05-18 16:36:57)

![](https://preview.redd.it/7aa6m9tdbx1h1.png?width=1838&format=png&auto=webp&s=e9f5db9567f7c6827b3715356916323453267f38)

boy, what a busy little bee you are!

###### [a\_beautiful\_rhind](https://www.reddit.com/user/a_beautiful_rhind/)

 (2026-05-18 19:59:20)

Hey man, opus works fast.

##### [alphatrad](https://www.reddit.com/user/alphatrad/)

 (2026-05-18 17:59:16)

it's AI slop based on the use of Maxscript

##### [KontoOficjalneMR](https://www.reddit.com/user/KontoOficjalneMR/)

 (2026-05-19 04:55:09)

> 
> Though I wish these could be integrated with existing tools like Pi or OpenCode instead of creating Yet Another Coding Agent
> 
> 
> 

I mean all the improvements seem to come from improved tooling. But "the best way to improve LLM coding is to actually give them symbolic code and make them less english" s a tough sell

##### 

#### [zoomaaron](https://www.reddit.com/user/zoomaaron/)

 (2026-05-18 12:31:51)

I think the idea is very much oversold. 4B active parameters is not the same as 4B parameter model. That’s misleading. You also made your own benchmark without telling us where it is so we can verify your claim. If you are using bench/stress\_test in your repo, I’m afraid that’s making a completely wrong claim, because it didn’t even check for the success of any of the test. As long as it produced 20 characters of output it passes. What kind of benchmark is this?

Some of the ideas you introduced is neat in demo but unclear to me how well they work in real world. For example, different models have different abilities to compose multiple tool calls. I’ve tested this extensively with my own harness and got mixed results because some models are just not well trained to chain tool calls; it’s out of distribution for them and caused more round trips than before. There are also models like deepseek which is trained to launch large batch of tool calls at the same time, asking it to compose calls actually reduced its token efficiency by a factor of a few. 

The error decomposition is also unconvincing. The most challenging part is often to figure out which is the one line that needs to change. I don’t see how a harness alone can pin point that precisely on a generic problem beyond syntax error, without relying on a large model.

##### 

#### [nuclearbananana](https://www.reddit.com/user/nuclearbananana/)

 (2026-05-18 06:49:22)

Which benchmark btw?

Also I see "patch first editing" in the readme. Can you explain what that is and how it helps?

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 06:54:57)

it was a custom 100-task stress test that was across multiple different coding languages.

as for the patch first editing.  

When a small model needs to edit an existing file, there are two approaches:

Rewrite: model outputs the entire file with changes (what most agents do)

Patch: model specifies just the old text and new text to swap

Small models (4B-14B) are terrible at rewriting. They truncate files at 60-120 lines, hallucinate middle sections, change indentation randomly, or forget imports they didn't modify. A 200-line file comes back as 140 lines with subtle bugs.

Patch is safer because:

The model only needs to produce the changed lines, not reproduce 180 unchanged lines from memory. It's cheaper on tokens (10 lines of context vs 200 lines of full file) It's verifiable, if old\_str doesn't match exactly one location, the tool rejects it and asks the model to be more specific.

It can't accidentally delete code it didn't intend to touch.

The tradeoff is the model needs to get the old\_str exactly right (whitespace and all). That's why SmallCode also has read\_and\_patch: a new compound tool that reads the file AND patches it in one call, so the model sees the exact content right before editing. Eliminates the "remembered it wrong" failure mode.

###### [gffftgdft455](https://www.reddit.com/user/gffftgdft455/)

 (2026-05-18 07:22:30)

Custom benchmarks is like marking your own homework. Sure you could mark it with honesty, but not everyone will believe you.

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 07:34:21)

I agree, im working on adapting opencode bench to work with smallcode so I can give concrete results.

###### [nuclearbananana](https://www.reddit.com/user/nuclearbananana/)

 (2026-05-18 08:24:08)

Ah, that's a standard replace tool. Patch had me thinking it was a codex style patch, which is hard for non-gpt models. 

How does read\_and\_patch work? Like it takes until the next round for the model to get the benefit of the read, so how does it help the patch?

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 08:37:05)

When `read_and_patch` fails (old\_str not found), it returns the actual file content in the error so the model can correct itself in one retry. instead of needing a separate read\_file call first. Cuts 3 round trips to 2. Less turns = less coherence loss for small models.

###### [nuclearbananana](https://www.reddit.com/user/nuclearbananana/)

 (2026-05-18 08:44:13)

That's actually pretty smart. Do you give it the whole file or try to guess which part oldText was trying to point to

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 08:54:26)

First 50 lines. Small models can't process a full 200-line file in the error response without losing track of what they were trying to do. 50 lines is usually enough to see the actual content around where they thought their `old_str` was.

If the file is short (under 50 lines), it gets the whole thing. Could be smarter, Fuzz matching the failed `old_str` against the file to find the closest section. But honestly the simple approach works well enough. The model usually just got whitespace or a variable name slightly wrong, and seeing the real first 50 lines is enough to self-correct.

###### 

###### 

#### [Distinct\_Lion7157](https://www.reddit.com/user/Distinct_Lion7157/)

 (2026-05-18 07:33:10)

can you use several real benchmarks and not one you created please

#### [Future\_Manager3217](https://www.reddit.com/user/Future_Manager3217/)

 (2026-05-18 11:33:30)

The architecture choices make sense for small models: fewer sequential tool calls, immediate compile/lint feedback, patch-first edits, graph search.

The part I’d want before trusting the 87% is a reproducible harness: frozen repos, published task set, pass/fail criteria, raw transcripts, and the same tasks run through OpenCode/Pi with the same model. Otherwise it’s hard to separate a real harness win from a well-shaped private benchmark.

#### [almbfsek](https://www.reddit.com/user/almbfsek/)

 (2026-05-18 08:12:39)

it's great. a simple pet peeve I have with all new harnesses are why build a custom UI that will be subpar instead of making it ACP-first (<https://zed.dev/acp>)

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 11:28:13)

You can now just use the ACP adapter if you'd like. --acp

###### [almbfsek](https://www.reddit.com/user/almbfsek/)

 (2026-05-18 11:28:43)

nice

###### 

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 08:18:38)

Fair point. The terminal UI isn't the end goal. I'll be honest, it's just the fastest way to get the agent loop working and testable without depending on any specific editor.

Honestly ACP is interesting and we're watching it. The reason we didn't start there: SmallCode's target audience is people running local models on consumer hardware who probably aren't using or better yet have never heard of zed. The terminal works everywhere.

###### [almbfsek](https://www.reddit.com/user/almbfsek/)

 (2026-05-18 08:47:40)

fair enough. just to make it clear, it's originally developed by zed but there are mature plugins for jetbrains, vscode and many cli tools too.

##### 

#### [AbjectBug5885](https://www.reddit.com/user/AbjectBug5885/)

 (2026-05-18 09:29:21)

The 4B parameter claim is what caught my eye tbh. If you're actually hitting 87% on something like SWE-bench or HumanEval with that small of a model, that's genuinely impressive and worth writing up properly. But without knowing which benchmark or seeing the eval methodology, this just reads like another demo project that worked on cherry-picked examples.

##### [gh0stwriter1234](https://www.reddit.com/user/gh0stwriter1234/)

 (2026-05-18 16:27:58)

He's not ... its his own bench which he hasn't even released. 

#### [dyeusyt](https://www.reddit.com/user/dyeusyt/)

 (2026-05-18 09:26:43)

I recently finetuned a Qwen3-4B for Next.js & shadcn generation, and was prompting it using a Gemma4 e2b (like it understands user needs and drafts a blueprint of the page)

This problem of SLM-generated code having syntax issues is real. I'm wondering if I could delegate code gen to another model using your arch; if yes, then I could probably swap out LangGraph in my Electron app with it.

<https://github.com/iamDyeus/qwendean>

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 09:29:16)

Do whatever you want, it's open src and MIT. If you need my help let me know!

Here's some general instructions though.  

Run SmallCode as`smallcode --mcp` and call it from your Electron app over stdio. Your Gemma4 plans, sends prompts to SmallCode, SmallCode calls your finetuned Qwen3 for code gen, then auto-validates (lint/compile), retries on syntax errors, and returns clean output. Replaces LangGraph's tool chain with built-in validation. You can also hot-swap models mid-session with `/model`

#### [vitordeas](https://www.reddit.com/user/vitordeas/)

 (2026-05-18 11:18:14)

Very smart approach, it seems exactly what we need for local models, well done!

I really want to see the results on some comparable benchmarks

#### [South\_Hat6094](https://www.reddit.com/user/South_Hat6094/)

 (2026-05-18 12:08:45)

the tool call reliability is what kills small models in agent loops more than raw intelligence. breaking tasks into tighter steps instead of expecting multi-hop reasoning is the real fix.

#### [WebOsmotic\_official](https://www.reddit.com/user/WebOsmotic_official/)

 (2026-05-18 13:17:14)

this is the right direction imo. small models don’t need “better vibes,” they need fewer chances to wander off. compound tools + instant lint/compile feedback is basically putting guardrails where the model is weakest.

#### [Finorix079](https://www.reddit.com/user/Finorix079/)

 (2026-05-19 01:39:58)

The harness-over-model thesis is right, and the benchmark gap backs it up. Two things worth pushing on though.

Compound tools cut failures but they also cut your visibility when something breaks. If find\_read\_edit\_verify fails, you don't know which of the 4 steps regressed. Worth logging the sub-step that failed even if the model only sees the unified tool. You'll want it the first time someone reports "edits started failing on Tuesday."

The decompose-on-failure trigger is interesting. Two attempts feels low for a 4B model. Have you looked at whether the second attempt is materially different from the first, or is it the same failure mode? If it's the same failure, decompose makes sense. If it's drifting randomly, more retries with temperature variation might be cheaper than decomposing.

Code graph approach beats grep, agreed. Curious how you handle stale graphs during active editing. Rebuild on every save or lazy invalidate?

Escalation policy is the part I'd think hardest about. "Failed twice locally" is one signal, but the more useful one is "this kind of task has a 40% local success rate historically, just escalate immediately." Otherwise you burn tokens and wall clock on tasks the small model was never going to land.

Will try it on a Qwen 2.5 Coder 7B setup this week.

##### 

#### [trajo123](https://www.reddit.com/user/trajo123/)

 (2026-05-18 07:28:11)

Ah, the good old "trust me bro" benchmark! I know it's exciting to jump into building an idea that you had, but investing some time into more standard benchmarks will pay off either by making you realize that the problem is harder than you initially thought or properly quantifying the improvement your solution provides, giving much more credibility/popularity to your project.

#### [professormunchies](https://www.reddit.com/user/professormunchies/)

 (2026-05-18 12:52:30)

These models have likely been bench Maxxed for swebench. A better dataset now is rebench v2 by nebius. I was finding for gemma4-31 just because it has a 100% patch rate doesn’t mean it was 100% pass rate, it was usually in the 70-80s for swebench and <10 for rebench.

#### [CircularSeasoning](https://www.reddit.com/user/CircularSeasoning/)

 (2026-05-18 13:24:47)

It feels like OP has been watching how I work with my models over my shoulder. This is how I harness my models manually to do great things they initially didn't seem capable of doing.

Whether you use this harness or not, pay attention to the techniques listed in bullet points here. They seem simple and even almost old/unoriginal as the ideas have been around already, but they are very powerful.

Not sure I would be comfortable doing all this with such a small model and a large codebase, but if it's all you got, it all helps. It's just as effective on bigger models.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 13:36:31)

Thank you?

###### [CircularSeasoning](https://www.reddit.com/user/CircularSeasoning/)

 (2026-05-18 13:49:23)

You're... welcome? 

Wait. Let's start again. You say "Thanks." and I say, "You're welcome."

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 13:52:22)

qwelcome

###### [CircularSeasoning](https://www.reddit.com/user/CircularSeasoning/)

 (2026-05-18 13:54:33)

This one's gonna need a bigger harness. Or a smaller one. I'm not sure.

###### [an0maly33](https://www.reddit.com/user/an0maly33/)

 (2026-05-18 14:27:41)

\*The user is saying the harness needs to be bigger.\*

\*Wait. They also said it might need to be smaller.\*

\*Wait. The user is not sure if the harness needs to be bigger or smaller. I should acknowledge this and wait for user input.\*

You were right to call him out. He should have had a differently-sized harness from the start.

##### 

#### [Economy-Register97](https://www.reddit.com/user/Economy-Register97/)

 (2026-05-19 01:03:14)

This is what I've been doing with the exception of this:
"Compound tools: Instead of making the model chain 4 tool calls (find file → read file → edit file → verify), SmallCode gives it one tool that does all 4. Small models lose coherence after 3+ sequential calls. This cuts failures in half."

How was this done? Did you just have it combine the process in a single script? I've seen failures on my side due to too many tool calls. Just like memes, I'm stealing this 😂

As far as the continuous learning, I've included Obsidian and some scripts to provide counts, analysis, thresholds, and promotion criteria. It's been working really well.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-19 01:09:14)

We use a db based memory layer that's searched the same way we'd search a codebase, so you get efficient memory recall across sessions.

But honestly, there's no magic orchestration framework, each compound tool is a single function definition that internally runs the steps sequentially in plain JS. The model makes one tool call, and the handler does the multi-step work server-side.

Here are the 5 compound tools:

| Compound Tool | Replaces |
| --- | --- |
| `read_and_patch` | read\_file → patch |
| `create_and_run` | write\_file → bash |
| `find_and_read` | find\_files → read\_file |
| `search_and_read` | search → read\_file |
| `run` | simplified bash |

The key design choices:

1. Each handler is ~15-25 lines of synchronous JS,  reads the file, does the operation, returns a combined result. For example `read_and_patch` reads the file, validates the old\_str exists exactly once, replaces it, writes it back, and returns the line number where the edit happened. If `old_str` isn't found, it returns the file content so the model can see what's actually there and self-correct — no second call needed.
2. Error feedback is baked in**.** When `read_and_patch` fails, it shows the file contents in the error response. When `create_and_run` has a command failure, it still reports the file was created plus the error output. The model gets everything it needs to course-correct in one round trip.
3. The system prompt tells the model to prefer these. The tools are merged into the tool list alongside the atomic ones, and the prompt explicitly steers toward compound usage.
4. There's also 2-stage tool routing for really small context models. a category selector narrows the tool set before the model picks a specific tool. This reduces confusion from seeing 20+ tool definitions at once.

Steal away. It's the simplest possible approach: just bundle the steps in a single handler function. The insight isn't architectural, it's that small models fundamentally can't maintain intent across 3-4 sequential decisions, so you move the sequencing out of the model's responsibility and into deterministic code.

Your Obsidian-based learning loop sounds solid. SmallCode does something similar with `tool_scores.json` tracking success/failure rates per tool to adjust which tools get offered.

###### [Economy-Register97](https://www.reddit.com/user/Economy-Register97/)

 (2026-05-19 01:17:35)

Kudos and appreciate the sharing of info. Very cool and I'm jealous of how well it's working for you at 4B! That's very impressive. I chose obsidian and smart connections to monitor and document my entire pipeline. Mostly out of ease and simplicity for a single user. Seems to do ok although I probably should address house keeping efforts on the data 😅. Appreciate you taking the time to reply.

###### 

#### [dinerburgeryum](https://www.reddit.com/user/dinerburgeryum/)

 (2026-05-18 12:55:55)

“4B (active) parameter model.” Not even saying the claims are untrue, but the title leaves out some pretty important detail. 

##### 

#### [minus\_28\_and\_falling](https://www.reddit.com/user/minus_28_and_falling/)

 (2026-05-18 09:44:28)

What benchmarks?

#### [overand](https://www.reddit.com/user/overand/)

 (2026-05-18 13:44:43)

I was going to suggest "You might not want to use the face of YouTube star 'Markiplier' as your profile photo on GitHub if you want to be taken seriously," but in further consideration, I think maybe it's a good thing.

##### 

#### [OsmanthusBloom](https://www.reddit.com/user/OsmanthusBloom/)

 (2026-05-18 14:31:25)

How does this compare to [Dirac](https://dirac.run/)? It seems that you have similar ideas e.g. about precise file edits and keeping contexts short to better support small/local models.

#### [nickl](https://www.reddit.com/user/nickl/)

 (2026-05-18 15:06:22)

This is interesting. I've been working on a custom agent for small models too, and I've been tempted to go down the "many tool" route. One problem I've found is that including the instructions bloats the context more than these small models can deal with easily. 

Progressive disclosure ala skills helps, but it remains a problem. 

How are you handling this?

##### 

#### [fittyscan](https://www.reddit.com/user/fittyscan/)

 (2026-05-18 21:10:31)

Have you tried <https://github.com/swival/swival> ?

#### [DiscipleofDeceit666](https://www.reddit.com/user/DiscipleofDeceit666/)

 (2026-05-19 00:33:59)

I tried doing something similar lol. I tried building my own harness to try to manage context bc that’s local ai biggest enemy. I learned that by harnesses are just fancy text formatters. How do you format the chatter, inconsistent spacing, and just random “if you need anything else, let me know” statements in the output.

Props to you for not only building that, but handling it in a way that even truly regarded models can use.

I wanted to use my GPU for coding development too, but the limited context was hard to work with directly so I built a loop that sends tasks written down in a toml file to an AI harness (like yours) and then runs unit tests after each task is done. Feeds failures back into the LLM for a fix.

If I could use tiny models instead of the qwen3.6 35B, I could probably run multiple agents in parallel each reaching 100 tok/s nearly tripling my current output. I might give this a go.

Do you support the -p syntax other CLI tools use? Where you send it a prompt to send it off?

##### 

#### [\_mayuk](https://www.reddit.com/user/_mayuk/)

 (2026-05-18 07:16:38)

Look quite cool c:

#### [LegacyRemaster](https://www.reddit.com/user/LegacyRemaster/)

 (2026-05-18 07:29:07)

I'll try it with Qwen3 8b

##### [overand](https://www.reddit.com/user/overand/)

 (2026-05-18 14:00:33)

Why not push for Qwen3.5-9b?

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 07:31:55)

please do!

##### 

#### [bronekkk](https://www.reddit.com/user/bronekkk/)

 (2026-05-18 07:51:32)

I am very interested in an alternative to Augment which I could point to locally hosted LLM. Although you do not mention vscode integration that's not the most important point about Augment, it's a secondary thing. Indexing is important and you seem to have done it. Thank you and I am definitely going to follow this project! 

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 07:55:43)

I could technically get that working, give me a day or two to make a viable plugin.

###### 

#### [dark-light92](https://www.reddit.com/user/dark-light92/)

 (2026-05-18 08:06:14)

Where did you find Qwen 3.6 9b to benchmark?

##### 

#### [Sad\_Initiative133](https://www.reddit.com/user/Sad_Initiative133/)

 (2026-05-18 09:10:29)

!Remindme in 3days

##### 

#### [Desther](https://www.reddit.com/user/Desther/)

 (2026-05-18 11:17:18)

Where do I set the ip for lm studio? Im getting "Cannot reach LM Studio at <http://10.0.0.20:1234/v1>"

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 11:23:39)

you need to edit these files.

Create a `.env` file in your project directory:

```
SMALLCODE_BASE_URL=http://localhost:1234/v1
SMALLCODE_MODEL=your-model-name

```

Or `smallcode.toml`:

```
[model]
provider = "openai"
name = "your-model-name"
baseUrl = "http://localhost:1234/v1"

```

If you're running LM Studio on a different machine (like `10.0.0.20`), change the IP accordingly:

```
SMALLCODE_BASE_URL=http://10.0.0.20:1234/v1

```

Make sure you're on `smallcode@0.2.7` or later (`npm install -g smallcode@latest`).  

 Earlier versions had a hardcoded IP that's since been removed.

###### 

#### [celsowm](https://www.reddit.com/user/celsowm/)

 (2026-05-18 11:28:46)

Amazing job! Congrats!
How does it deals with context window? 

##### 

#### [Substantial-Cicada-4](https://www.reddit.com/user/Substantial-Cicada-4/)

 (2026-05-18 12:24:55)

Good idea, but not going to install an npm based anything from reddit with "too good to be true" signals left and right. I don't want to be on the hews.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 12:26:07)

then compile it from source, its right there.

###### [Substantial-Cicada-4](https://www.reddit.com/user/Substantial-Cicada-4/)

 (2026-05-18 13:25:07)

Let ne rephrase. At this point I have severe allergies towards dependencies and trust issues with anything in the chain being compromised. Don't get me wrong, what you did looks good. "It's not you, it's me".

##### 

#### [LittleCelebration412](https://www.reddit.com/user/LittleCelebration412/)

 (2026-05-18 12:26:16)

What benchmarks did you run? 

#### [migsperez](https://www.reddit.com/user/migsperez/)

 (2026-05-18 12:27:40)

I tried. It didn't work well for me at all. I used gemma4:e4b via ollama. The responses weren't related to the prompt. I couldn't paste into the prompt area. I couldn't write me the one line, shift return didn't work it just sends the message. Lots of issues.

I wanted it to do well. Let me know when the next version is out.

##### 

#### [ehiz88](https://www.reddit.com/user/ehiz88/)

 (2026-05-18 12:36:28)

if my opencode works well with small models through llama cpp server why should i use this instead?

##### 

#### [cj886](https://www.reddit.com/user/cj886/)

 (2026-05-18 13:01:24)

so how do you get it to work? ive set the env file, and even updated the toml file as per your instructions, all i get is this "" ✓ ✗ Failed to parse URL from undefined/v1/chat/completions"""

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 13:05:18)

UHHHH... do an npm -g install again, sorry.

###### [cj886](https://www.reddit.com/user/cj886/)

 (2026-05-18 13:14:22)

thanks! look forward to seeing what it can do :)

#### [sillib](https://www.reddit.com/user/sillib/)

 (2026-05-18 13:20:37)

What benchmarking did you use? Mbpp?

#### [R\_Duncan](https://www.reddit.com/user/R_Duncan/)

 (2026-05-18 13:34:05)

I was just noticing last opencode version has toolcalling issues even with Qwen3.6-35B-A3B (issues that weren't there a month ago)

##### 

#### [Infamous\_Jaguar\_2151](https://www.reddit.com/user/Infamous_Jaguar_2151/)

 (2026-05-18 14:32:39)

This is awesome, will it also work well with models 27b+ sized? How would it compare to open code for those larger local models?

##### 

#### [Hot-Employ-3399](https://www.reddit.com/user/Hot-Employ-3399/)

 (2026-05-18 14:42:16)

First impressions weren't good. It didn't work well with qwen3.6-27B (task was to make custom "autotype" in bevy so holding Ctrl-Z triggered undo N times per second; other agents complete from ~30 minutes(pi) to ~12 hours(hermes))

> 
> ✗ bash ✗ Exit code 100│ ✓ bash $ cd /workspace && cargo check 2>&1 2610ms  
> 
>  ✗ bash ✗ Exit code 100│ ✓ read\_file ✓ 0ms  
> 
>  ✗ bash ✗ Exit code 100│ ✓ read\_file ✓ 0ms  
> 
> ✓ ◇ DECOMPOSE: Command keeps failing. Changing approach.  
> 
> AI: The output is truncated. Let me run with a specific filter to see all results: 
> 
> 
> 

And stopped talking with llm (total time: ~30 minutes).

Also it didn't print much info, at least by default. (Like what is it thinking, or what bash is doing, or what file is being read)

Also it ignored config at .config/smallcode/config.toml which I saw in [source](https://github.com/Doorman11991/smallcode/blob/e754f9799ba0ff9e44db572943889f7613498a3f/src/core/config.ms#L83) code, and ignored env variables (I've used /endpoint to setup model; didn't test .env file)

Also created too much extra dirs into project dir ( `.smallcode/ .code-graph/ .memory/ ` )

##### 

#### [DigThatData](https://www.reddit.com/user/DigThatData/)

 (2026-05-18 14:59:21)

Some clever work from a few years ago demonstrated a competitive solution w/o involving agentic components at all: <https://github.com/OpenAutoCoder/Agentless>

#### [cafedude](https://www.reddit.com/user/cafedude/)

 (2026-05-18 15:00:01)

claude code seems to have recently added an /advisor option. It allows you to designate an advisor model that is consulted if the model you're using gets stuck. It would be interesting to have something like that where you designate a frontier model that would be consulted when needed. That would help reduce token usage of the frontier model.

#### [HiddenMushroom11](https://www.reddit.com/user/HiddenMushroom11/)

 (2026-05-18 15:14:50)

Anyway to use a global config file instead of having to setup smallcode every time in my projects? Something like ~/.config/smallcode.conf

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 15:17:12)

Already supported since 0.4.5. Put your `.env` at any of these paths:

```
~/.config/smallcode/.env       (recommended)
~/.smallcode/.env              (alternative)

```

SmallCode checks in this order, first found wins:

1. `<project>/.env` (project-level override)
2. `<project>/.smallcode/.env`
3. `~/.config/smallcode/.env` (global)
4. `~/.smallcode/.env` (global alt)

So set up your model endpoint once in `~/.config/smallcode/.env` and it works everywhere without per-project config:

```
mkdir -p ~/.config/smallcode
cat > ~/.config/smallcode/.env << 'EOF'
SMALLCODE_MODEL=your-model-name
SMALLCODE_BASE_URL=http://localhost:1234/v1
SMALLCODE_CONTEXT_WINDOW=131072
EOF

```

Then just `cd any-project && smallcode,` no setup needed.

###### 

#### [MerePotato](https://www.reddit.com/user/MerePotato/)

 (2026-05-18 15:54:48)

This kind of elegant simplicity is missing from so many projects in this space, props to you

#### [Specialist\_Major\_976](https://www.reddit.com/user/Specialist_Major_976/)

 (2026-05-18 16:04:17)

The compound-tools bit is the interesting part to me. Small models aren't really failing at coding first, they're failing at staying coordinated across tool hops, so moving the boring orchestration into the harness makes sense.

#### [\_underlines\_](https://www.reddit.com/user/_underlines_/)

 (2026-05-18 17:05:53)

did you look into [little-coder](https://github.com/itayinbarr/little-coder) and how it differs? maybe even combine forces, if goals align well enough between these two projects?

and a relevant add on that might interest you: [semble](https://github.com/MinishLab/semble) for faster, less token heavy and more accurate code search, compared to glob and grep

#### [JustFinishedBSG](https://www.reddit.com/user/JustFinishedBSG/)

 (2026-05-18 17:26:33)

Great post but I find it amusing that two of the steps to « how to have great results with a 4B model » are :

* actually, don’t use a 4B model, use an 8B-A4 MOE
* delegate to a giant model when things are hard

##### 

#### [itsyourboiAxl](https://www.reddit.com/user/itsyourboiAxl/)

 (2026-05-18 20:53:08)

I want to try local but i wonder how precise you must be? Claude code is good at understanding, like i can explain a feature like i am 5 and he will do it right on first try. Do local models also perform this good or do you need more careful prompting and planning? Maybe its a bit naive but i’ve never tried local ai for serious dev. I will give your agent a try

#### [dtdisapointingresult](https://www.reddit.com/user/dtdisapointingresult/)

 (2026-05-18 21:53:41)

I can't install this.

'npx smallcode' gives:

```
const { MemoryStore: McpMemoryStore } = require('budget-aware-mcp/dist/memory/store.js');
Error [ERR_REQUIRE_ESM]: require() of ES Module /home/user/.npm/_npx/2a34a6c93b3d02a2/node_modules/budget-aware-mcp/dist/memory/store.js from /home/user/.npm/_npx/2a34a6c93b3d02a2/node_modules/smallcode/bin/smallcode.js not supported. Instead change the require of store.js in /home/user/.npm/_npx/2a34a6c93b3d02a2/node_modules/smallcode/bin/smallcode.js to a dynamic import() which is available in all CommonJS modules. at Object.<anonymous> (/home/user/.npm/_npx/2a34a6c93b3d02a2/node_modules/smallcode/bin/smallcode.js:48:41) { code: 'ERR_REQUIRE_ESM' }
Node.js v18.20.4

```

EDIT: fixed after I installed a newer node.js.

##### 

#### [MetricZero](https://www.reddit.com/user/MetricZero/)

 (2026-05-18 23:34:02)

Bro, you cooked. This is great for mid-tier models too.

#### [jonas-reddit](https://www.reddit.com/user/jonas-reddit/)

 (2026-05-19 17:11:13)

Benchmaxxed or outright cheating. 

If it sounds like too good to be true, and out of the blue, it usually is.

<https://debugml.github.io/cheating-agents/>

#### [dtdisapointingresult](https://www.reddit.com/user/dtdisapointingresult/)

 (2026-05-19 19:39:36)

Doesn't work with Qwen 3.5.

```
You: What is 2+2?
│ ✓ ✗ API error 400: {"error":{"message":"System message must be at the beginning.",

```

I recommend adding a TRADITIONAL\_OPENAI\_MODE=true/false setting. When enabled, you must do this:

1. System prompt goes at the beginning, followed by User and Assistant turns
2. Do not use the Developer role added later by OpenAI, only System/User/Assistant (many models don't support it, most importantly Qwen)
3. Never send Assistant as the last message, some backends/models don't support this. If you need to give hidden additional guidelines, those are User messages. Don't try to be cute or special.

Every single model and backend supports this classic setup. In fact I recommend this should be your default behavior, it will work universally.

#### [Snoo-81733](https://www.reddit.com/user/Snoo-81733/)

 (2026-05-20 08:57:02)

The topic you're tackling is really cool, I like it a lot.

If I may, I’ve been thinking about the same problem space recently, and I’d like to share a few ideas that have been floating around in my head.

The patch.ms tool

Asking the LLM to reconstruct the exact `oldStr` feels too expensive and fragile to me.

I mean, requiring the model to rebuild, and therefore emit, the exact old code strings to replace is an extremely difficult task. I was thinking about implementing an `Edit` tool (the name used by other agent to refer your `patch.ms`) where, instead of passing the `oldStr`, you provide a checksum identifier for the lines of code that should be replaced.

I haven’t fully explored the idea yet, but I was considering taking inspiration from a well-known algorithm called the Fenwick Tree, which efficiently computes prefix sums between nodes (line of rows in our case). Maybe it could be adapted to accumulate identifying checksums incrementally, ensuring that only explicitly marked lines are replaced.

The plan.ms tool

In my opinion, the interface could be simpler. Maybe something based on a stack-oriented task planner.

Initially, you can insert an array of tasks. From that point onward, no more than one task can be added at a time.

I was thinking about something along these lines:

```
Use the plan tool to track mini tasks.

For an empty plan, split the main task into small concrete steps and add
them together. Each task has:

- title: short concrete step
- detail: optional implementation guidance

The plan is a stack: item 1 is current. Future items are context only.
Execute only item 1, then mark it done.

If a plan already exists, add at most one new task at a time. Do not add
duplicates.

Initial plan:

<tool_call>
{"name":"plan","arguments":{"tasks":[{"title":"<step>","detail":"<optional
guidance>"},{"title":"<next step>","detail":"<optional guidance>"}]}}
</tool_call>

Mark current task done:

<tool_call>
{"name":"plan","arguments":{"done":true}}
</tool_call>

If done and plan is empty, you may add multiple replacement tasks:

<tool_call>
{"name":"plan","arguments":{"done":true,"tasks":
[{"title":"<step>","detail":"<optional guidance>"},{"title":"<next
step>","detail":"<optional guidance>"}]}}
</tool_call>

If done but plan still has items, add at most one priority task:

<tool_call>
{"name":"plan","arguments":{"done":true,"tasks":[{"title":"<single
priority step>","detail":"<optional guidance>"}]}}
</tool_call>

Divide et impera: plan small, execute item 1 only, mark done, continue.

```

The bash.ms tool

For `bash.ms`, there’s a much broader discussion to be had.

Personally, I implemented fairly complex policies based on command parsing and positional string analysis to determine whether a command is suspicious or not, including re-read and approval policies.

I also added a layer based on restricted shell usage through:

```
bash -r

```

(the restricted bash mode)

Along with instructions like these:

```
Use bash for filesystem inspection, searching, editing files, and running programs.
Work in the current working directory unless explicitly told otherwise.
Use relative paths when practical.

- Prefer combining related operations in one command using && and |.
- Prefer multi-pattern search with grep -E "a|b|c".
- Prefer awk instead of sed for portable cross-platform file edits.
- After each command, include a status message inside the shell command:
  && echo "DONE: description" || echo "ERROR: description"

```

#### [AspadaXL](https://www.reddit.com/user/AspadaXL/)

 (2026-05-23 07:21:01)

WARNING: This tool will leave huge folders in your working repo. Use it at your discretion!

The big folders are .code-graph / .memory / .smallcode

I just tried this one on my open source project and it left these huge folders without any notice. I then accidentally committed them to my repo. It was a mess! 

##### 

#### [BC\_MARO](https://www.reddit.com/user/BC_MARO/)

 (2026-05-23 16:25:16)

If you want people to trust the 87%, ship a reproducible eval (tasks + config + logs) and run it on SWE-bench Lite or rebench. Compound tools are the right idea; fewer tool hops is the whole game for small models.

#### [JimmyBenHsu](https://www.reddit.com/user/JimmyBenHsu/)

 (2026-05-24 12:37:12)

The compound tools idea is genuinely interesting — I've hit this exact wall where local models fall apart after the third sequential tool call. 

Wrapping multiple operations into one call is a smart engineering decision for small models. The decompose-on-failure pattern with optional escalation is pragmatic too. 

The benchmark number needs more scrutiny, but these patterns solve problems I've actually run into building side projects with local models.

#### [Celestialien](https://www.reddit.com/user/Celestialien/)

 (2026-05-25 10:47:03)

The decompose-on-failure idea is neat. Once it breaks "fix this 200-line file" into single-piece fixes like "fix line 45 only," how do the pieces get stitched back together, and is there a final whole-file compile/lint pass after the decomposed steps land? Wondering if local fixes can ever end up conflicting with each other before the model sees the file as a whole again.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-25 11:19:46)

it basically breaks it into smaller errors, keeps track of where those errors were and lets the ai work through them in a min-todo list style.

###### 

#### [Spectrum1523](https://www.reddit.com/user/Spectrum1523/)

 (2026-05-18 12:35:25)

I am so tired of cliche LLM reddit posts.

> 
> Here Is a Problem: there isn't enough slop online.
> 
> 
> So I Built vibeslop, the sloppiest vibe project of all time
> 
> 
> 

#### [NandaVegg](https://www.reddit.com/user/NandaVegg/)

 (2026-05-18 09:14:31)

Very interesting work. Though the repo looks fairly vibecoded at a glance, explanations made by the OP and intention for each feature (with nice fallbacks) makes very much sense.

Smaller models are typically post-trained much more with synthetic data from larger models than direct RL optimization (it's generally harder to make a 4B-sized model converge on diverse tasks that way), but those synthetic data generation pipeline tends to result in a single or two-turn instruction rather than a long multi-turn actions. So I can see how "tool call packing" helps.

Even in general chatbot-type use, copy pasting the list of current variables in every user instruction (and subsequently removing it from past instruction) helps a lot. It's like always assuming the model only has attention span of 2-3 turns, and was the case for most models before agentic RL (forcing CoT aka reasoning extends that a bit).

#### [xeeff](https://www.reddit.com/user/xeeff/)

 (2026-05-18 09:37:17)

dishonest advertising/comparison.

> 
> us = TODO-file planning, others = single-shot planning
> 
> 
> 

just no

#### [\_mayuk](https://www.reddit.com/user/_mayuk/)

 (2026-05-18 07:18:06)

How is the work flow to per example if I have a small repo … how I would initialize the graph db of it ? 

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 07:20:45)

It's automatic, you don't need to do anything.

```
cd my-project
smallcode

```

When SmallCode boots, it:

1. Starts the code graph MCP server in the background
2. Detects sub-projects (looks for `package.json`, `Cargo.toml`, `go.mod`, `src/` dirs)
3. Indexes each one with tree-sitter (extracts functions, classes, imports, call edges)
4. Stores the graph in graph.db (SQLite, stays local)

Takes around 100ms for a small repo, a few seconds for larger ones. After that, when you ask "how does auth work?" it searches the symbol graph instead of grep-reading every file. If you want to re-index (say you pulled new code), just restart SmallCode or use `graph_search,`it checks staleness automatically. The graph DB stays in your project folder (gitignored by default). Nothing leaves your machine.

###### [\_mayuk](https://www.reddit.com/user/_mayuk/)

 (2026-05-18 07:23:09)

🥹 beautiful … i was so annoyed with megamem … even using Gemini api it felt so annoying …to set up …this can be huge !!! 

Great work c:

###### [\_mayuk](https://www.reddit.com/user/_mayuk/)

 (2026-05-18 07:24:58)

Another maybe dumb questions … I guess small code handles the updates of the graph.db after any major changes right ? C: 

###### 

#### [No\_Field3913](https://www.reddit.com/user/No_Field3913/)

 (2026-05-18 08:02:06)

Im doing something related but havnt touched the tool side yet, first getting my flow working work OC as harness then bench various custom stuff :)

Will try this one out :) too 

##### 

#### [Kodrackyas](https://www.reddit.com/user/Kodrackyas/)

 (2026-05-18 08:08:16)

This is definitelly a trend, nice to see, also i agree on letting the ai test and proceed so you can measure errors with executing code, but you cant measure quality on the finished builded code, do you have any process for that?

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 08:15:23)

I'm glad you asked, we actually track that with several metrics.

1. Structural checks, the verifier catches placeholders (// TODO, // ...), truncated output, unbalanced braces, and incomplete implementations before delivering code. If the model wrote a lazy skeleton, it gets rejected and re-prompted.
2. Governor scoring, every tool call is tracked with Bayesian confidence. If the model consistently produces bad patches or writes code that fails validation, it learns to avoid those patterns for that task type. Over time it routes toward approaches that produce working code.
3. BoneScript for backends, instead of letting the model freestyle Express routes (which leads to inconsistent quality), it writes a declarative spec and the compiler generates the implementation deterministically. The quality is guaranteed by the compiler, not the model.
4. Memory, conventions and decisions persist across sessions. Once you tell it "always use error boundaries" or "follow this naming pattern", it loads those as efficient context on every future task.

What we don't have yet: automated style/complexity scoring (cyclomatic complexity, duplication detection) or human-eval-style "does this actually solve the problem correctly" verification beyond compile+run. That's on the roadmap, likely as a plugin that runs static analysis post-generation.

Honest take: for a 4B model, "it compiles, runs, and passes basic tests" is already a high bar. Quality beyond that (clean architecture, proper error handling, idiomatic patterns) is where escalation to a stronger model helps. The local model handles the 80-90% of straightforward tasks, and Claude/GPT handles the 10-20% that need more sophistication.

###### [BillDStrong](https://www.reddit.com/user/BillDStrong/)

 (2026-05-18 08:35:43)

Does this work better using something like Qwen3.6-35B-A3B or Qwen3.6-27B?

I would think the same tools would make working with the larger models more efficient as well, reducing complexity they can use elsewhere.

Guess I need to try it.

###### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 08:38:56)

The better the model, the better it will run. It should be excellent for Qwen3.6 a3b. 

#### [ganonfirehouse420](https://www.reddit.com/user/ganonfirehouse420/)

 (2026-05-18 08:55:51)

I wonder wonder if it good enough for coding in python and go. 

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 08:57:33)

Go has mixed results for gemma 4 e4b, but pythron results were almost perfect. Give it a shot and let me know how it goes!

#### [ConfusedLisitsa](https://www.reddit.com/user/ConfusedLisitsa/)

 (2026-05-18 09:48:58)

If the idea is combining many tools into just one I understand you will end up with a very large numbers of final tools 

The model itself has then to choose the correct one between all of the available ones

So I wonder how does this not actually make the model fail at just choosing the correct tool to call

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 09:54:01)

I actually found the solution to that here: <https://github.com/atripati/ark>  

The model never sees all tools at once, 2-stage routing shows categories first 5 choices, then only the tools in that category. Compound tools replace sequences, they don't add to the count. Total stays around 15 which small models handle fine.

#### [ziphnor](https://www.reddit.com/user/ziphnor/)

 (2026-05-18 10:10:01)

Sounds a bit like <https://itayinbarr.substack.com/p/honey-i-shrunk-the-coding-agent?triedRedirect=true> ?

This new trend is super exciting for local llms.

#### [solarmass](https://www.reddit.com/user/solarmass/)

 (2026-05-18 10:39:23)

Github reports that you built this using 53% MAXScript. I am curious of that choice.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 10:44:42)

GitHub is misidentifying the `.ms` files, they're not 3ds Max MAXScript. It's a typed module format for internal declarations. The actual runtime is plain JavaScript. GitHub just doesn't recognize the extension and picks the closest match.

those infinity stones are mine sir, no looksies

###### 

#### [JsThiago5](https://www.reddit.com/user/JsThiago5/)

 (2026-05-18 10:51:14)

How **Decompose on failure** work**?** Do you call the model to decompose the problem into TODOs?

##### 

#### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-05-18 11:24:23)

[deleted]

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 11:25:12)

no it wasn't, that wouldn't be fair lol.

#### [Pleasant-Shallot-707](https://www.reddit.com/user/Pleasant-Shallot-707/)

 (2026-05-18 11:29:16)

This is pretty cool. I like how you can augment with cloud AI automatically when the model determines its in over its head. That’s a great way to sip expensive tokens to ensure you’re still being productive. I also like the idea of compound tools. 

##### 

#### [jfowers\_amd](https://www.reddit.com/user/jfowers_amd/)

 (2026-05-18 12:14:53)

So you’re saying it could run on AMD NPU, interesting!

##### 

#### [shuwatto](https://www.reddit.com/user/shuwatto/)

 (2026-05-18 12:27:47)

Is it the only way to setup a local llama.cpp server to put `.env` in each projects?

##### 

#### [geekynerd44](https://www.reddit.com/user/geekynerd44/)

 (2026-05-18 12:27:59)

Will definitely take a look, most of my local model for coding experiment success has come from using Aider, but that is not agentic, every agentic tool felt too heavy (16k system prompt to start with) and small models struggled with those.

Are you planning to add web search? Being able research latest documentation makes a huge difference.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 12:33:27)

bookmarking this, can definitely get that working.

###### 

#### [nostriluu](https://www.reddit.com/user/nostriluu/)

 (2026-05-18 12:57:05)

I would like to integrated a coding agent into an existing Typescript framework. I would ideally pass it a prompt, context, and test condition(s), and let it do its thing. Would smallcode be a good choice for this? Thanks!

##### 

#### [overand](https://www.reddit.com/user/overand/)

 (2026-05-18 13:41:00)

What are these `.ms` files? (GitHub unhelpfully thinks they're "MAXScript" files, but I'm pretty sure this isn't a framework for 3D Studio MAX!)

They look like JS to me, but that's not how they're named - and this is the first time I've seen that extension used. Granted I'm not a JS developer, but this smells odd to me.

##### 

#### [ThiccStorms](https://www.reddit.com/user/ThiccStorms/)

 (2026-05-18 14:19:43)

oh wow, i really like the symbol graph thing, is it commonly used elsewhere? i wanna read more about it, and i've recently been trying the small gemma models with opencode and gave up because my passive cooling mac just struggles sometimes, ill try this out.

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 14:22:27)

the idea is loosely used in other projects, I based my custom memory/codebase <https://github.com/Doorman11991/budget-aware-mcp>  

off of <https://github.com/CodeGraphContext/CodeGraphContext>  

just repiped in some improvements and added memory support, changed the db it uses yada yada yada

###### [ThiccStorms](https://www.reddit.com/user/ThiccStorms/)

 (2026-05-18 14:36:04)

oh great! hard to explain but i've never ever used MCP servers and stuff. (i still use LLMs the old way, browser copy and paste, for reasons i cannot explain) so yeah i will explore more about MCP servers, and yeah also about the linting part, is it also an MCP thing? 

#### [Imaginary\_String\_954](https://www.reddit.com/user/Imaginary_String_954/)

 (2026-05-18 14:39:05)

How can this be explained to a newbie? If this isn't an LLM, how do I make the best use of it

##### 

#### [[deleted]](https://www.reddit.com/user/[deleted]/)

 (2026-05-18 15:22:42)

[removed]

##### 

#### [Hezy](https://www.reddit.com/user/Hezy/)

 (2026-05-18 15:24:47)

It sounds like this could be useful with non local models as well. Any reason not to try it?

##### 

#### [Ashraf\_mahdy](https://www.reddit.com/user/Ashraf_mahdy/)

 (2026-05-18 15:34:50)

Sent you a Message! Check your DMs

#### [Konamicoder](https://www.reddit.com/user/Konamicoder/)

 (2026-05-18 16:04:29)

Hey there, I am trying to install smallcode on my Linux Mint rig. My models are being served up by oMLX running on an M1 Max Mac on my Tailscale network. So per your instructions on github, i pointed smallcode to my project folder and created a .env file to tell smallcode the model name and base url where it should connect to find my models. smallcode gave me this error message:

" Cannot reach LM Studio at <https://MY-OPENAI-ENDPOINT-TAILNET-URL/v1> 

Make sure LM Studio server is running."

The TailNet URL is verified correct and working because it's what I am using to drive nanocoder and pi on the same rig. So i know the issue is not an incorrect URL. My suspicion is that my omlx server requires an API key. So I tried to add a SMALLCODE\_API\_KEY line in the .env file, but the error message persists. Thoughts on how I can get smallcode to connect to my model backend over the TailScale network? I would really like to try it out. Also your github states to "See `.env.example` for all options. " but I can't seem to find that example file?

Help!

##### 

#### [Arrowstar](https://www.reddit.com/user/Arrowstar/)

 (2026-05-18 16:12:03)

How can I get this pointing at a llama-server instance I have running on another machine?

##### [Glittering\_Focus1538](https://www.reddit.com/user/Glittering_Focus1538/)

 (2026-05-18 16:13:14)

Create a .env file in your project directory:

SMALLCODE\_MODEL=your-model-name

SMALLCODE\_BASE\_URL=http://OTHER\_MACHINE\_IP:8080/v1

That's it. llama-server exposes an OpenAI-compatible endpoint at /v1 by default. SmallCode talks to anything that speaks that protocol.

If you started llama-server with --api-key, also add:

OPENAI\_API\_KEY=your-key

#### [aegismuzuz](https://www.reddit.com/user/aegismuzuz/)

 (2026-05-18 16:32:26)

I love these posts. First, we loudly claim an 87% benchmark score, and then in the comments, we quietly mention it’s a custom stress test where the model just has to spit out 20 characters of code. The architecture itself - compound tools and compiler validation - is legit, but trying to sell it with cooked metrics is a total shot in the foot. Run it through a proper SWE-bench, take your honest 30-40% for a 4B model and be proud of it, because for that size, it would already be a massive breakthrough

#### [elijahebanks](https://www.reddit.com/user/elijahebanks/)

 (2026-05-18 16:56:47)

Good work! I'm working on an engine specifically for the raspberry Pi! 

#### [Warsel77](https://www.reddit.com/user/Warsel77/)

 (2026-05-18 17:20:49)

Does it get "87% on benchmarks with a 4B parameter model" with Opus in the loop or without?

#### [alphatrad](https://www.reddit.com/user/alphatrad/)

 (2026-05-18 17:56:20)

You could just use Pi which works great with local models. I also don't see mentioned here or in your repo WHAT benchmark you claim this scores so high in.

#### [wow-a-shooting-star](https://www.reddit.com/user/wow-a-shooting-star/)

 (2026-05-18 18:03:56)

This is what I’m looking for. I’m limited with devices, raspberry pi 5 8gb and my iPhone 17 pro as a host for the llm. Currently have it linked with Hermes agent on my pi. 

#### [LippyBumblebutt](https://www.reddit.com/user/LippyBumblebutt/)

 (2026-05-18 18:36:40)

I gave this a quick look. I first tried on CPU with E4B and it timed out all the time. Partially because of llama.cpp, but even with --timeout 99999 it failed in smallcode.

Running on GPU, I let it code a 2048 game in html/js. After it worked ok, I asked for animations. Then [this](https://privatebin.net/?0d80c6e47b029cc2#6gc1zFV6ZofqBeV1uxs5vXyKX9pWTbsr52J1mkQPSd8a) happened.

It repeated all it's answers twice all the time. Didn't read the file a couple of times and then crashed.

I asked for no external dependencies. Maybe that's why it created a single 13kb file with embedded js/css. Might have been part of the problem?

Also "Created index.html (104 lines) 2ms" wow, you can write a file in 2ms! Amazing. That's not how long it took though...

#### [josuf107](https://www.reddit.com/user/josuf107/)

 (2026-05-18 19:06:49)

In <https://github.com/Doorman11991/smallcode/blob/ec6df2dc205f25c48b8799ab54c118a7a213bf35/src/plugins/skills.js#L79> there's a parsing bug in that inline comments in the frontmatter are parsed as values. E. g. `keywords: manual # manual is best` will set `keywords` to `manual # manual is best` since the value regex is `(.+)$`. Probably should use a library for parsing YAML, but if you are wanting to roll your own that's one thing that doesn't currently work correctly.

#### [Prize\_Negotiation66](https://www.reddit.com/user/Prize_Negotiation66/)

 (2026-05-18 19:14:32)

qwen code works good even with 27b model

#### [takuarc](https://www.reddit.com/user/takuarc/)

 (2026-05-18 19:39:11)

I love Gemma, it’s pretty powerful as it is. I wanted to do something similar but even more focused. Will definitely check out your repo.

#### [FancyNet9095](https://www.reddit.com/user/FancyNet9095/)

 (2026-05-18 19:59:39)

I understand the "how", but why?

#### [eightshone](https://www.reddit.com/user/eightshone/)

 (2026-05-18 19:59:47)

Interesting project. I’m working on a small tool that cleans up uncommitted files in my local branches by composing grouped commits in one command using 3b model (qwen 2.5 coder). What I learned was that with small models we have to be clever how to make the prompts and how pass context, while with frontier models you can just throw everything at it and they’ll work as expected.
I think building agents that are focused on small models is a great way to come up with cleaver tricks that overcome challenging situations.

#### [yoomiii](https://www.reddit.com/user/yoomiii/)

 (2026-05-18 20:17:36)

> 
> For Node.js/TypeScript backends, SmallCode uses BoneScript — write ONE `.bone` file and compile it to a complete project (routes, auth, DB, events, migrations, SDK, admin panel, Docker, CI). Reduces 8-15 tool calls to 1-2, dramatically improving reliability with small models.
> 
> 
> 

Why force this upon users of your harness? Why can't tool calls be reduced without "BS"? Pun intended

##### 

#### [Imjustmisunderstood](https://www.reddit.com/user/Imjustmisunderstood/)

 (2026-05-18 20:23:01)

Wow I tried it and I’m pleasantly surprised. Please keep building this up, apply the same philosophy to MCPs, and you will have a more accessible, cheaper claudecode! Good job!

####
