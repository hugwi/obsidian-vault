---
title: "The First Real LLM Breakthrough Is Here...  SubQ (1000x Less Compute)"
source: "youtube"
url: "https://www.youtube.com/watch?v=uzkTAT81FxA"
author: "TheAIGRID"
published: "2026-06-18"
created: "2026-08-24"
duration: "0:10:41"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "anthropic"
  - "context-engineering"
  - "evaluation"
  - "video-gen"
  - "youtube-strategy"
summary: ">> Today, we're announcing a major architectural breakthrough. The world's first fully sub-quadratic LLM. SubQ has a 12 million token context window and frontier-level intelligence."
---

# The First Real LLM Breakthrough Is Here...  SubQ (1000x Less Compute)

![The First Real LLM Breakthrough Is Here...  SubQ (1000x Less Compute)](https://www.youtube.com/embed/uzkTAT81FxA)

## Description

🎓 Learn AI With Me For Free - https://www.skool.com/the-aigrid-community-1726
🌐Subscribe To My Newsletter - https://aigrid.beehiiv.com/subscribe
Get your Free AGI Preparedness Guide - https://theaigrid.kit.com/agi

🐤 Follow Me on Twitter https://twitter.com/TheAiGrid

00:00 What is SubQ and why is everyone talking about it?
00:38 What did SubQ announce about 12 million token context?
02:00 What is SubQ 1.1 Small?
02:20 Why does normal transformer attention scale quadratically?
03:03 Why do long-context AI models need a new architecture?
03:52 How does sub-quadratic sparse attention work?
04:28 How is SubQ different from Longformer, BigBird, and Mamba?
05:04 How much compute does SubQ save versus dense attention?
05:51 Can SubQ actually retrieve information from long context?
06:47 How does SubQ compare to GPT, Claude, and smaller models?
07:53 Did SubQ train its model from scratch?
08:20 What are the real-world use cases for 12 million token AI context?
09:11 Are SubQ’s benchmark claims independently verified?
10:05 What are the main limitations of sparse attention?
10:21 When will SubQ be available and what happens next?

Links From Todays Video:
https://subq.ai/subq-1-1-small-technical-report

Welcome to TheAIGRID — the place to learn AI for free. I create simple, practical videos that help beginners, creators, entrepreneurs, and business owners understand artificial intelligence, AI tools, automation, AI agents, robotics, ChatGPT, Claude, Gemini, and the future of technology. Whether you want AI tutorials, tool breakdowns, beginner guides, or explanations of the latest breakthroughs, this channel gives you the knowledge you need to stay ahead. Subscribe to start learning AI for free and keep up with the fast-moving world of artificial intelligence.

Was there anything i missed?

(For Sponsorship Enquiries)  aigrid@faiz.mov
(Contact Me Direclty - contact@thaigrid.com

Music Used

LEMMiNO - Cipher
https://www.youtube.com/watch?v=b0q5PR1xpA0
CC BY-SA 4.0
LEMMiNO - Encounters
https://www.youtube.com/watch?v=xdwWCl_5x2s


#ArtificialIntelligence

## Transcript

So, there's a new breakthrough called SubQ, and apparently it's the first model built on a fully sub-quadratic sparse attention architecture and the first model with a 12 million token context window, which is apparently 52 times faster than flash attention and less than 5% the cost of Opus. So, apparently transformer-based LLMs waste compute by processing every possible relationship between words, and only a fraction of those words matter. So, apparently this company has managed to do it, and it's nearly 1,000 times less compute and a new way for LLMs to scale. So, take a look at this, then we're going to dive into today's announcement. >> Today, we're announcing a major architectural breakthrough. The world's first fully sub-quadratic LLM. SubQ has a 12 million token context window and frontier-level intelligence. It outperforms Opus 4.7 on long context at less than 5% of the cost. At 1 million tokens, SubQ processes tokens 52 times faster than flash attention and dramatically changes the cost of training and inference, enabling us to scale context windows to 12 million tokens and beyond, pushing the boundaries of intelligence. This means your agents can now complete weeks of work at a time without degrading, reasoning across entire code bases, merging hundreds of PRs at once, and finding patterns in tens of thousands of documents. All in one shot without losing accuracy, speed, or context. SubQ is not just another model. It represents a major algorithmic breakthrough. It is the first model built on a fully sub-quadratic sparse attention architecture. LLMs today waste compute by processing every possible relationship between words, but only a small fraction of these matter. SubQ finds and focuses only on those relationships, meaning compute is used where it matters most. At 12 million tokens, this reduces compute almost 1,000 times, changing the way the LLM scale. Today, SubQ is available for early access along with SubQ code, a coding agent built on the next generation of AI technology. This marks a new era for builders, an era powered by sub-quadratic intelligence. Visit subq.ai to get early access. >> So, the new release that has happened today is the second iteration of the same idea, and this is the smaller size. So, the company says that it's already rolling out to a first group of design partners with a bigger lineup of models ranging from 2 million to 12 million tokens planned for later this year. So, the story is not just like some brand new company appearing out of nowhere. This is the follow-up that puts harder numbers on the table, and it says that the early claims are holding up. So, to understand why this matters, you need to understand the one problem that has limited every large language model since the original Transformers paper in 2017. Normal models use something called a dense attention, and that basically means that when the model reads your text, every single word looks at every other word to decide what's important. If you double the length of that text, you don't double the work, you roughly quadruple it, and that's called quadratic scaling, and that's the reason that long documents get so expensive and slow. Now, companies have built years building workarounds for this, like chunking documents into pieces, using retrieval systems to pull out only the relevant bits, and stacking agents on top of each other. But, the introduction of Sub Q's own report makes the point that all of those tools are really just patches for the underlying limit, attention that scales quadratically with length. So, this is the opening of the research page, and it basically sets the whole tone for what follows. The page is titled introducing Sub Q 1.1 small, and it says that this is of course designed for enterprises because these are the problems that they face. Now, of course, consumers could eventually use this, but all problems, you know, share a common shape. They require reasoning over complete artifacts like entire code bases, document collections, contracts, and financial filings. And that single sentence is the entire reason this company exists. They're not trying to win at the short chatbot era. They are betting that the most valuable AI work involves holding something huge in front of an AI model, and it can essentially read it all at once. And the current way that we do that is basically too expensive to be practical. Now, the trick behind all of this entire magic is what they call sub-quadratic sparse attention or SSA. And the idea is that in a trained model, almost all of those word-to-word relationships are basically empty. Each word really only cares about a handful of others. So, instead of paying to compute all of them, SSA [music] learns to pick for each word a small group of other words that actually matter. Then it does the full attention math on that small group. And this is different from all the shortcuts methods like Longformer and Big Bird also skipped the relationships, but they did it based on position, like only looking at nearby words. [music] SSA does it based on content, which means a word can pull a relevant detail from millions of tokens away if the meanings line up. And unlike systems like Mamba that compress everything into a fixed memory, SSA still computes real exact attention on the word it selects. So, the company says there's no quality loss from approximation. Now, now this chart is the clearest picture of what SSA is supposed to buy you. And it is the heart of the announcement. It compares dense attention the normal way against SSA as the amount of text grows. The black line is dense attention and it curves upward steeply because the cost rises faster and faster as the context gets longer. By the time you reach 1 million tokens, dense attention needs about 252 PFLOPS per attention layer. And the orange line is the SSA and it stays almost flat along [music] the bottom, sitting at just under 4 PFLOPS at that same 1 million token mark. The gap widens as the text get longer, going from eight times less at 128k to 31 times less at 512k to 64 and a half times less at 1 million tokens. The line at the bottom of the chart sums it up. SubQ uses 64.5 times less compute than dense attention and is 56 times faster than Flash Attention 2 at a 1 million token context. And so, a huge context window is effectively useless if the model cannot find and use what's inside of it. So, this chart tackles the most important question directly. It shows two retrieval sets. On the left is ruler, and which the sub quadratic calls a capability test because its 13 tasks go beyond finding one fact. And instead of requiring tracing variables, counting how often things appear, and combining information across the whole document, sub 1.1 small scores 99.12% on ruler at 128k, which is kind of multi-step reasoning that the real world actually needs. And on the right is the needle in the haystack text, which is hiding a single fact in a giant deep block of text, and ask the model to pull it out exactly. Sub Q scores 100% at 1 million and 2 million tokens, and 98% at both 6 million and 12 million tokens. The reason that that is striking is that the model was mostly trained at 1 million tokens, yet it still finds the needle reliably at 12 times that length, while only looking at about 0.13 of all possible relationships. Of course, long context retrieval does not mean much if the model is dumb at everything else. So, they put it side by side with the major frontier models, and this table is where the honest trade-offs show up. On graduate-level science, the GPQA diamond test sub 1.1 small scores 85.4. That sits below GPT-4.5 at 93.2 and Opus 4.8 at 92, but comfortably above the other smaller models like Haiku 4.5 at 67.2. On competitive programming, the live code bench, sub Q hits 89.7, which is genuinely close to the top where GPT-4.5 is at 92 and Opus 4.8 is at 92.2. On agentic finance called the automation bench, sub Q scores 13%, which is ahead of Sonnet at 8% on the mini and nano models, but the report is up front that every model scores low here. The point of this table is not that sub Q wins at everything, it's that a small model built mainly for long context still holds its own on a and coding instead of falling apart. One detail that the report changes how you should read all of this is that Sub Quadratic did not train this model from scratch. They started with an existing open weight frontier model ripped out of its dense attention and replaced it with SSA. They then stretched the context ability in stages going from 262K, then 512K, then 1 million, and 2 million followed by roughly 1 trillion tokens of extra training >> [music] >> on naturally long material like books, full documents, and entire code repositories. The company says the biggest lever for getting good at long context retrieval was simply training on long data, which only became affordable because SSA made those million token experiments cheap enough to run over 100 times. So, part of the story here is not just a clever architecture, it is that the architecture that made the researchers start fast enough to actually find a good recipe. The reason that this is getting so much attention is that the use cases behind it is that if you can hold an entire code base, a full set of financial filings, or a giant stack of contracts in front of a model all at once, you no longer need to retrieve fragile, you know, pipelines that grab pieces and hope nothing important got left out. Sub Quadratic points to three obvious areas: financial analysis and due diligence, legal contract work where a term defined on a page or two might get changed on page 12, and carved out on page 46, and software engineering where an entire repository fits into one window. On top of all of that, the cost claims are dramatic. Outside reports describe a long context evaluation that reportedly cost about $8 on Sub Q versus roughly $2,600 on Claude Opus at the same length. And if that holds up, it makes that work that's currently too expensive for everyone to do suddenly normal. Now, of course, some people are wondering is this true? Is this verified? The launch got some loud reactions. Some people are, you know, of course, saying that this is incredible, one of the biggest breakthroughs since Transformer paper, but plenty of researchers are holding back. The main concerns are pretty simple. Most of these eye-catching numbers come from the company's own testing, and while a third party called Appen verified the benchmarks in the latest report. The broader efficiency claims have not been widely reproduced by independent labs. The model weights are not public, so outsiders can't really, you know, poke at it. And And there is actually a known weak spot with sparse attention. It tends to help out on very long inputs, while short everyday prompts, the kind that most chat and agent use actually involves, are not really covered in the published [music] benchmarks. So, some analysts flagged the gap between the lab retrieval scores and the deployed ones in certain multi-fact tests. None of this means the claims are false. It just means that the proof isn't finished yet. And so, Subquadratic says it's kicking off with its first cohort of design partners in the next few weeks, with a broader rollout throughout the quarter, and the general releases by the end of the year. And they've also even signaled bigger targets down the line, with some reports pointing to a 50-million token context window goal later in 2026. So, the real test is coming over the next few months. Independent users and labs will get their hands on it, run their own evaluations, and then we'll figure out whether the efficiency and accuracy of the numbers survive contact with the real world. And if they do, this is genuinely a new way for models to scale. If they shrink under pressure, it just joins a long list of approaches that didn't, unfortunately, work.
