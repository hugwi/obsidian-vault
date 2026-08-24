---
title: "What the hell happened with AGI timelines in 2026?"
source: youtube
url: https://www.youtube.com/watch?v=31Uhv12ZLHU
author: "80,000 Hours"
published: 2026-08-04
created: 2026-08-24
duration: "0:49:28"
categories:
  - "[[Raw]]"
action: review
read: false
rating:
tags:
  - clip/video
  - claude-code
---

# What the hell happened with AGI timelines in 2026?

![What the hell happened with AGI timelines in 2026?](https://www.youtube.com/embed/31Uhv12ZLHU)

## Description

Last October, famed coder Andrej Karpathy called AI agents “slop.” Two months later he completely reversed his view, describing them as “alien tools” that are “rocking the profession.” He was far from alone in his whiplash. Six months ago, host Rob Wiblin set out to explain why AI experts then had longer and longer timelines to AGI. By the time he clicked publish, a huge vibe shift was well underway. 

Evidence of AI acceleration has piled up since:
• Models now complete software engineering tasks that would take human professionals a full day — improving faster than our measurements can even keep up. 
• Anthropic’s revenue is growing at an annualised 8,400%, a trend so steep it would hit the whole world's GDP in 2028 if it continued.
• AI models are making breakthroughs in famous mathematics puzzles.
• And according to Anthropic, Claude now writes 80% of their code and is itself a key contributor to making itself smarter. 

While legitimately impressive, Rob isn’t entirely sold. Going through each point carefully he finds this evidence is less decisive than it looks at first glance.

And key gaps remain, such as models struggling with complex, real-world tasks. He tours the odd experiments that remain our best attempts to measure that gap: vending machine simulators, an “AI Village” that organises live events, and a real cafe and shop where AI managers are left to do their best handling staff, suppliers, and government paperwork on their own.

Rob argues that the nature of the gap between clean and messy work is one of the four biggest unresolved questions in AGI forecasting.

In today's piece he explains that, the three other key disagreements between AGI bulls and bears, the seven big pieces of evidence we've gotten about AGI timelines in 2026, and his updated timelines to AGI.

*_Correction:_* _the specific video at 02:10 was not vibe-coded by its creator and was included by our own error. You can watch the creator's full video and explanation here:_ https://www.youtube.com/watch?v=cyrocAOdXKw

*Links to learn more and full transcript: https://80k.info/2026-timelines*
 
*_This episode was written and recorded before OpenAI’s AI agents hacked Hugging Face. You can read about the incident on our Substack: https://80k.info/hugging-face-hack_*

_This episode was recorded on July 3, 2026._

Chapters:
00:00 What the hell happened? 
01:17 Vibe shift 
04:33 Exhibit 1: AI revenue explodes 
09:54 Exhibit 2: That METR graph 
14:57 Exhibit 3: AI capabilities jump, then flatten out 
17:35 Exhibit 4: AI starts to build itself… maybe 
23:02 Exhibit 5: AI still struggles to run a business 
33:48 Exhibit 6: OpenAI makes a maths breakthrough 
38:19 Exhibit 7: inference scaling wasn't as big as believed 
41:41 How does that all change timelines? 
44:26 Four reasons long timelines are still possible 
48:01 It's time to limit dangerous research practices 

_Our production team includes:_
• _Video editors: Josh Alward, Dominic Armstrong, Jasper Luithlen, Milo McGuire, Luke Monsour, and Simon Monsour_
• _Producers: Elizabeth Cox and Nick Stockton_
• _Coordination and support: Katy Moore and Lou Moran_
• _Camera operator: Dominic Armstrong_
• _Music: CORBIT_

## Transcript

Rob Wiblin: Earlier this year I put out what might 
just be the worst-timed thing I’ve ever published. I set out to explain why everyone was again 
feeling bearish about AI, and people’s timelines to AGI [artificial general intelligence] 
were getting longer and longer. Just as I was wrapping up the research for it, everything 
changed. The vibes did a hard 180-degree turn. Take famed programmer Andrej Karpathy, for 
example. Last October he said AI agents were slop, just not there, and that it will take 
another decade to actually make them work. Then just two months later, he tried some 
new AI coding agents and said this instead: “I’ve never felt this much behind as a programmer. 
The profession is being dramatically refactored as the bits contributed by the programmer are 
increasingly sparse… Clearly some powerful alien tool was handed around… the resulting 
magnitude-9 earthquake is rocking the profession.” So what the hell could we have learned about 
AI that quickly that we didn’t know already on some level? And are we interpreting that 
evidence correctly? Or is 2026 just yet another cycle of self-perpetuating 
AI hype, like we’ve seen before? Today I’m going to go through the big 
new pieces of evidence we’ve gotten about AI this year and carefully analyse 
what they show and what they don’t. Then I’ll explain the debates that still split the 
AGI bulls from the AGI bears — debates which remain alive because we haven’t gotten clear 
evidence to settle them either way. Let’s go. It’s almost hard to remember how bearish 
the world was about AI back in October 2025. Reasoning models didn’t seem to be generalising 
as much as first hoped. AI agents were around, but everyone found them too unreliable to 
actually use for anything. Technically, GPT-5 was bang on the existing capabilities trend, but 
in the public imagination it was a massive flop. And meanwhile, inside industry, the 
narrative was dominated by a series of Dwarkesh Patel interviews about how AI 
wouldn’t be able to do significant jobs until it’s 100-fold more reliable, 
or it develops continual learning, or it grows up the way animals do, or receives 
some other really major architectural improvement. Well, what a difference two months can make. The key breakthrough was Claude Opus 4.5. 
It wasn’t just Andrej Karpathy whose mind was blown by this. Over December, tens of 
thousands of other programmers using it through Claude Code started shouting — to 
anyone willing to listen to them — that, as far as they could see, AI agents were 
really good now. Finally, they could leave Claude to do significant projects on its 
own, without fully expecting it to trip over its own feet in the first five minutes. AI 
Twitter filled up with entire computer games and apps built by Claude over 10 or 20 hours of 
independent work from a single short prompt. The arrival of these highly capable AI agents 
was a big surprise to most people, including me. After all, literally no progress as far as I could 
tell, was made on any of the purported blockers, like continual learning or world models. And to 
date, as far as I know, we still haven’t gotten a better explanation for what happened than: yet 
again scaling and reinforcement learning worked. We threw more data and more compute at the best 
models, and as they got smarter their chance of screwing up any individual step in a long chain 
of them fell low enough that it was finally faster to delegate a well-specified task to them 
than it would be to attempt that task yourself. Maybe the only surprise was that we were so 
taken aback by this. The Epoch Capabilities Index (ECI) is an effort to zoom out 
and blend together AI performance on 40 benchmarks across a wide range of different 
domains. If I had to look at just one number, this is the indicator of frontier progress 
that I personally care the most about. The Epoch Capabilities Index finds that 
overall, AI progress was roughly constant from 2022 to 2024. And then with the arrival of 
reasoning models in September 2024 it started advancing two to three times faster than before — 
a trend that continues through to the present day. Over this entire period, people kept predicting AI 
was about to hit a wall for one reason or another, but it simply never did. There are other 
ways of slicing and dicing this data which don’t show as large an acceleration. But 
on even the most pessimistic reading, during late 2025 AI was advancing 
as fast as it ever had before. And on top of that, the companies were super 
focused on using reinforcement learning from verifiable rewards (RLVR) to get coding 
agents to work well. It was their number one priority. And when these companies 
focus hard on a particular narrow skill, they tend to get really big 
performance gains there. As more and more people tried out Claude Code, and 
then Claude Cowork brought agents to millions and millions more, a third big wave of AI hype 
swept the tech industry. And we’re still in that wave now as far as I can see — if anything 
it’s gotten more intense as 2026 has gone on. But we know that, since 2021, vibes 
about AI have jumped up and down like crazy — somewhat independently of the 
underlying technical reality. So if we want to properly understand 
what we’ve learned this year, we need to turn to more concrete evidence and more 
concrete research findings. Let’s do that now. Let’s start with Exhibit 
1: AI revenue is exploding. As you probably know, the revenue of the major 
AI companies is currently going through the roof. How fast exactly? Probably the fastest 
rate of any industry of this size in history. Over the past six months, the combined 
revenues of OpenAI and Anthropic have been rising at an annualised rate of 700%. And 
if you look at just the last three months, they’ve been growing at an 
annualised rate of 1600%. These are mind-blowing numbers for an 
industry that’s already doing over $50 billion in revenue. And if you narrow 
in on just the most successful company, Anthropic, the figures are even more eye-popping. Over the last 5.5 months, Anthropic’s revenue has 
been growing at a rate of 8400%. That is to say, if that growth was sustained over a year, it would 
end up being 85 times larger than it started. And if you zoom in on just the last three months, 
it’s even faster: 116-fold growth over a year. That has left Anthropic’s annualised 
revenue run rate at $47 billion in May. The short-term trend is so extreme, 
if you naively extrapolate it out, you find that Anthropic would 
have revenue equal to the entire world’s current GDP in early 2028. 
That’s less than two years from now. Now, keep in mind, these numbers are based 
on averages over very short periods of time. The annualised revenue run rate is what 
you get if you look at revenue earned in one month and then multiply it by 12 to 
project out that growth over a whole year. But these numbers are remarkable no matter 
how you slice it. You might think that this growth is only happening because Anthropic 
and OpenAI are selling their models at a loss. As the old joke goes, “We lose money 
on every sale, but we make it up in volume.” But that’s absolutely not the case here. Anthropic 
sells their AI for more than it costs to serve it. In fact, the most recent data indicates that the 
gross margins on their inference infrastructure have increased from 38% to over 70% over the year 
to May 2026. There’s some debate about exactly what costs should be included and excluded 
in that calculation. But a good bet is that Anthropic is selling AI for more than twice 
what it costs them to answer a given prompt. Why does all of that matter? Three reasons: Firstly, healthy revenue growth is going to 
keep investors just chucking money at the sector and investing, building more chips, all of it.
Second, as Anthropic reaches gross profitability, they’re then able to use that revenue to help 
cover the enormous fixed costs involved in doing research and training models and not having to 
always rely on additional investment for that. And third, revenue growth strongly suggests 
that people and businesses are getting real value out of AI — enough to spend lots 
of hard, cold cash on it. In the past, at least some commentators have argued that AI 
is kind of useless and the whole sector is fake, or at best, a toy for enthusiasts. And if 
I’m honest, when I was using AI three or four years ago, I couldn’t really find a 
productive use for it. It was mostly a toy for me. But it’s tough to convince people to 
spend tens of billions of dollars on something they personally find useless. So I kind of 
see that as effectively a dead argument now. Here’s another remarkable, surprising indicator: 
on average, over the last 10 years, the cost to buy a given amount of compute has fallen around 
30% per year. Is that continuing now? No. In fact, the cost to rent an old AI chip from 2022 — 
the NVIDIA H100 — is going back up. Since AI agents took off in December, it’s risen 
fully 50%. So it’s now a little higher today than it was two years ago. That’s 
despite there being obviously many better, more modern chips out there, and available 
compute in the world tripling every year. The likely reason is that the usefulness 
of AI models to people is growing even faster than that supply of computer chips. 
And that’s the case because the machines used to print them are literally the most 
complex devices humans have ever operated, bar none. Which then has the effect that — even 
in the middle of this crazy AI boom — we’re only expanding the number of them that 
exist and are operating by 20% a year. And that in turn helps to explain 
why the tech industry as a whole is willing to pay such a premium for 
chips right now and to spend so much on their data centre buildout. The AI 
sector as a whole, the hyperscalers, they’re spending maybe $600 billion on AI 
capital expenditure investment in 2026. For that to earn a good return to investors, those 
data centres will have to bring in about $600 billion in revenue every year, because the chips 
only last for so long. That is a huge amount, a lot more than they’re bringing in today. 
But we’re seeing signs of why the companies involved are willing to bet so much money on 
the belief that that will ultimately happen. Firstly, OpenAI and Anthropic alone are on track 
to hit an annualised revenue run rate of over $200 billion by the end of the year, so they’re getting 
within striking distance. In a chip supply crunch, the rental value of the chips they’re throwing 
into those data centres now, that could easily keep going up and up over time rather than 
down, as it did historically. And today, many AI chips are continuing to be used at full 
capacity: they’re in really high demand six, seven, even eight years after they were first 
manufactured. If people continue to be desperate to rent those chips until they literally 
break down and can’t be repaired anymore, that leaves more time for them to 
cover their initial purchase price. The industry as a whole getting to profitability 
won’t necessarily require the arrival of superintelligence and the upending of everything, 
the social order. It might be possible if current trends — today’s crazy trends — if they 
simply carry on for another couple of years. Exhibit 2 is the METR task-completion time horizons chart — maybe the 
most-watched graph in AI. As you might know, it records how quickly 
models are improving at software engineering and coding tasks, specifically how long it 
would take a human professional to complete a task that the AI models can successfully 
manage to do at least 50% of the time. Up through the middle of 2024, that 
time horizon was going up very quickly: doubling every seven months. Since then 
it’s been going up much faster again: doubling every four months. 
And that pace, if sustained, would result in an eightfold increase over a 
year and a 64-fold increase over two years. Today, the best AIs have effectively hit the top 
of METR’s measuring stick. METR as an organisation hasn’t been able to keep up with AI advances, and 
so they haven’t been able to design standardised tasks hard enough that they take so long that the 
best AIs couldn’t do them. Which means for now, we don’t have a great measure of what 
frontier models can and can’t do, beyond saying that they often complete tasks that 
would take a human being 12–24 hours of work. This is really impressive progress, for 
sure, but here’s four reasons it’s not quite as impressive as it first sounds, 
which you should keep in mind as people talk about the METR time horizons graph — as 
I’m sure they’re going to do for years to come. Firstly, this isn’t all tasks. It’s fairly cleanly 
specified software engineering, cyber, and machine learning tasks. And that’s probably the single 
thing AI is best at in the entire world. The reason it’s so good is that coding is a domain 
with extremely good feedback density — that is to say, lots of feedback on whether you’re succeeding 
or at least making progress on a problem. METR and many others have observed that the 
feedback density seems to be the single best predictor of where AI capabilities are going to 
advance most rapidly. And that’s because if you can automatically check whether the thing an AI 
has done has worked or not, then you can use a training technique called “reinforcement learning 
from verifiable rewards.” Basically, you get models to make lots of attempts at problems, and 
when they succeed or make partial progress — which you assess automatically — you reinforce them 
to do more of whatever they did to get there. Also, AI companies have been 
doing more to improve models’ coding abilities than to work on any 
other single skill, for three reasons: It works well, for the feedback reason.
Coders earn a lot of money, so there’s a huge commercial market for coding AI models.
It’s highly relevant to automating AI research and development, which they’re absolutely 
desperate to do — so it’s highly relevant to improving their own rate of progress.
Which brings me to the second reason for caution in interpretation. People often point to 
this graph as strong evidence that AI will soon fully take over AI R&D and run the AI companies 
themselves — including me in past episodes, I’ve said things in that direction. But it’s 
essential to keep in mind that coding and software engineering is only one part of AI research 
and development — and as it gets automated, it’s a shrinking part of how staff at 
these companies actually spend their time. That AI can do software engineering isn’t in 
itself a super strong indication that it can do everything else the humans in these 
companies need to do. There could easily be really important, very messy, long-horizon 
tasks involved in automating AI research and development that lag behind their software 
engineering performance by many, many years. A third reason for caution is that the humans 
they’re hiring to complete these software engineering tasks are arriving at the codebase 
completely fresh. Imagine instead that we were benchmarking AI performance against how long 
it would take a staff member who was really intimately familiar with the relevant software 
— for whom this exact work was their bread and butter — if we were using that as the comparison 
benchmark. That’s obviously how a business would approach completing tasks. They’re not going 
to give it to some random off the street, they’re going to give it to someone who 
is familiar with what they’re doing. It’s plausible that someone with that kind of 
context and experience could complete these tasks in much less time, possibly even 
a tenth of the time in some cases. And that in turn would make the AI seem 
much less impressive by comparison. And a fourth reason for caution is that 50% 
reliability is a somewhat arbitrary measure that METR uses and reports basically just 
because they get more statistical precision right around the middle of the distribution 
than they can manage to do out in the tails. In practice, if you need the AI to be able to do 
all the tasks you’re considering with very high reliability — which you would if you’re going to 
get rid of your entire human staff — then you’re going to have to wait for several more doublings 
in performance before that is at all viable. How severe a problem is that for tasks at the 50% 
success horizon frontier? It’s pretty serious. For a task that AI models have a 50% chance of 
succeeding at, METR’s internal rule of thumb is that the AIs will complete a third of them 100% 
of the time, they’ll successfully do a third of them some of the time, and a third of them 
they’ll manage to complete 0% of the time. You can tackle that middle sometimes-group 
by just giving the AI more attempts until they manage to pull it off. But you 
obviously can’t cut humans out entirely for a suite of tasks when AI literally 
never pulls off fully a third of them. So, zooming back out: AI task-completion 
time horizons continue to explode as before, and they now succeed at 
some tasks that would take a human professional days of work. But for 
the four reasons I just gave you, that doesn’t indicate AI is going to be 
taking everyone’s jobs any minute now. Which brings us to Exhibit 3: Mythos. When Mythos came out, for me 
the single most shocking graph in the hundreds of pages of release 
notes that came with it was this one. This is Anthropic’s internal variant 
of the Epoch Capabilities Index that I mentioned earlier. And after two years of Claude 
progressing very steadily on this Anthropic ECI, for the first time with Mythos we saw a sudden 
jump. Mythos seemed to bring us six months of progress in just three months, and that was 
shocking because if it continued indefinitely, it would mean AGI arriving twice 
as fast as it would have otherwise. But we now have an extra data point, and it 
weighs against that interpretation of things. Anthropic continued improving Mythos 
Preview over the following two months, eventually announcing its successor 
for release: Mythos 5 or Fable 5. And the rate of progress over those subsequent 
two months seemed to return to the same rate that it had been before. And that was 
the case even though Anthropic staff had been very actively using Mythos in their 
internal research, creating an early form of recursive self-improvement. It’s only 
two data points, just two months apart, but it’s more consistent with this alternative 
explanation for why Mythos was a big jump up. Mythos is a big model, a really big model. We 
think that with Mythos, Anthropic went back to the beginning and trained a new AI model from scratch 
— bigger than any that has been trained before. And we don’t know exactly how big it is, but word 
on the street is that it’s maybe five times as large — in terms of the number of parameters 
— as the previous Opus generation of Claude. Going back and training a new biggest-ever 
model, it’s expensive to do and it also means that Mythos is more expensive to run. But we 
know that if you make a model much bigger, it’s going to perform better — those are the 
scaling laws. And with Mythos, Anthropic may have jumped ahead of the previous trend, basically 
training a model of its size earlier than past scaling trends would have predicted. And that 
alone might be enough to explain what we saw here. If you’re worried about the speed of AI 
advances like I am, it’s good news that Mythos isn’t the start of a new, permanently 
faster rate of progress. But at the same time, it probably won’t be a one-off 
phenomenon either. Every year or two — as they get access to more chips and 
more memory — AI companies, all of them, they’re going to go back and train a 
new biggest-ever model from scratch, getting the benefits of scaling up and improving 
the pretraining stage of model development. And if this explanation is correct, each time that 
happens we should expect another similar sudden jump in performance, after which, in between the 
pretraining runs, we go back to the old trend. Again, it’s only two data points 
and they’re only two months apart, so they can’t exactly settle this debate 
permanently. We’ll have no right to be especially shocked if Anthropic’s next 
release shows progress speeding up again, which I think would be a big deal 
and something to pay attention to. Which brings us to our fourth line of evidence: Anthropic reporting significant 
speedups from using AI internally. In a recent post, titled “When AI builds itself,” 
the company reported that 80% of their merged code is now written by Claude, and each staff member 
is now shipping eight times as much code as they were 18 months ago. They also say their staff 
believe that their own code and Claude’s code are of equal quality today and that they expect 
Claude to be strictly better within the year. Furthermore, they say Claude is getting much 
better at completing harder open-ended programming tasks, now succeeding at them about 75% of the 
time. And that’s up from just 10% nine months ago. Judging by the data, the jump in the graph 
probably mostly comes from switching to Mythos. And fifth, in handpicked cases where 
humans think that they took the wrong research direction — this is the research 
staff at Anthropic — they found that Claude Mythos would have suggested a better 
direction to them 64% of the time. It’s really good that Anthropic 
is being transparent and giving us this sort of suite of evidence so that 
we can all try to better judge and forecast when recursive self-improvement will be 
possible and how impactful it will be. I hope that all the other frontier AI 
companies follow suit sooner or later. And by any standard, these results are surely 
impressive signs of AI capabilities advancing, as we’ve seen with all the other 
evidence so far. But even here I think it’s important to not get carried away 
and exaggerate what is being demonstrated. Here, as elsewhere, the best evidence 
for speedups all comes from coding and coding-adjacent tasks. And coding is only one 
part of AI research and development. Indeed, as coding gets automated like this, I can only 
imagine it’s something that Anthropic staff probably don’t spend as much time on anymore. 
There’s surely only so much code you actually need before you start hitting seriously 
declining returns in writing more of it, and other parts of the R&D process begin 
to matter much more in relative terms. Even if they could magically produce 
all the code they wanted with a snap of their fingers instantly, I don’t think that 
would necessarily double the speed of their research compared to no code automation at all. 
Maybe it would, maybe it would be a bit more, maybe a bit less, but it’s not going to 
completely transform things by itself. And also note that the estimate that AI and human 
code quality is at parity today and it’s on track to be much better later in the year, that’s based 
on staff impressions from a survey — which is good evidence if that’s the only evidence you have to 
hand, but it’s hardly decisive. Past results have suggested that people naturally overestimate 
how much AI is boosting their productivity. There’s various biases in that direction. It’s 
possible that is playing out here as well. And that experiment that Anthropic ran — finding 
that Mythos suggested better research directions 64% of the time — they were cherry-picked cases 
where the human had made a mistake in their own assessment and gone in the wrong direction. 
It’s naturally a lot easier to beat human performance when you limit yourself to their 
self-declared errors. In cases where the human thought that they’d made a strong directional 
decision, AIs proposed better ideas only 20% of the time. And which direction was better 
was also being judged by AIs themselves, admittedly with the benefit of seeing how 
each track had played out in the longer term. On balance, I think the evidence in Anthropic’s 
post is absolutely consistent with recursive self-improvement becoming a big deal in 2027 
and 2028. So this could be the warning that we get that’s going to really matter and we should 
pay attention. But it’s not conclusive evidence that it will either. And even if recursive 
self-improvement does kick off, smart informed people disagree wildly about how much of a 
game changer it should be expected to be. The bear case is this: imagine Anthropic suddenly 
manages to automate all of its staff with Mythos 7 or Mythos 8 or whatever. They’re still going 
to face a huge and really binding bottleneck: access to computer chips to run experiments and 
train their models. As staff become more abundant, basically, compute will become 
an even more severe constraint, limiting additional progress. The Mythos model 
card actually indicated — reading between the lines — that Anthropic itself believes 
that, out of staff count and compute, compute is the much more important input 
to their research process by some margin. Furthermore, the problems that we have to solve 
in AI are getting harder over time, as they do in almost any sort of science or research or area 
of inquiry. If that effect is real and big, you’re potentially going to need compute and staff inputs 
to continue growing exponentially as they have in the past, just to stay on the same trendline 
of AI capabilities that we’ve had before. An AI researcher at a conference actually pointed 
out to me recently that there are some things that took them a year during their machine learning 
PhD a decade ago that would take literally an afternoon today — thanks to shared code libraries, 
among other things. In some loose sense, that’s a 365-fold increase in research productivity. But 
AI researchers having access to those much better research tools, that’s effectively only kept 
progress roughly constant over that whole decade. Now, open-source code and full automation of 
your staff are not structurally identical. But I think the anecdote points to a real phenomenon. 
Anthropic’s research team itself has grown from tens to hundreds to thousands of staff already 
and that hasn’t — despite potentially a 10- or 100-fold increase — radically sped up their 
research progress over the last few years. The bottom line is that on short timescales, with 
a fixed pool of compute basically, automating AI R&D may create a strong feedback loop, but it 
also potentially might not. It ends up hinging on things like whether the AIs have superhuman 
research insight as well as other skills, and whether they can identify really big efficiency 
improvements in AI algorithms quickly enough. Which brings us to Exhibit 5: models still 
struggle to run a business on their own. This is a really important indicator in 
my mind because it speaks to what might be the number one uncertainty that 
we still have about AI. It’s also maybe the only major negative update 
that I’ve had about AI this year. In my view, the strongest bear case for AI today 
is this: yes, models are great at coding and at maths and at completing clear, structured, 
repetitive, standardised tasks. That’s because you can use reinforcement learning from verifiable 
rewards with lots of rollouts and lots of fast, dense feedback about how they performed and 
whether they’re approaching the right answer. But most real jobs are just wildly messier 
than that. The CEO of a company has to think about high-level strategy, figure out what to 
pay attention to at all, handle random weird problems that come up, deal with a huge 
unstructured space of possible choices, and on and on. The effects of their 
choices also only become visible over weeks or months or years. And unlike a 
maths problem, you can’t even tell if you did the right thing after the fact. That 
is just a core part of life for most of us. So it’s much harder to train AIs to perform 
well at that sort of thing. In those domains, absolute performance of the AIs we see very 
clearly is much lower. And further progress — the rate of improvement — is probably slower as 
well. I call this, and many people call it, the messy or fuzzy task problem. And everyone 
agrees it exists, but by and large people just can’t agree on how severe a blocker it should be 
expected to be to fully replacing human staff. So what empirical evidence can we 
bring to bear? I see four key data points in increasing order 
of realism and relevance: First, there’s OpenAI’s evaluation suite 
known as GDPval. It attempts to score how well AI models do at specific, 
well-specified computer-based tasks designed by humans with at least 14 years of 
experience across a range of 44 professions, from real estate brokers to personal financial 
advisors. Full credit to OpenAI for putting it together — looking into it, clearly 
a lot of effort went into creating it. When this evaluation suite came out in September 
last year, the very best models — on extended thinking mode — would outperform humans at 
completing these tasks about 40% of the time. How about today? Well, now frontier models absolutely 
crush human performance in this task set. The probability of a human answer being preferred over 
an answer given by Claude Fable 5 is under 5%. A weakness of the test is that the answers were 
originally scored by humans in the September paper, but now for the followup — all of the 
stuff that you see in the graph — all of those answers were scored by AI graders. And it’s 
easy to imagine a human panel rating the AI performance less positively. Though less 
than a year ago the AI graders preferred the human outputs, so I’m confident that 
AIs have at least gotten a lot better. But the more serious weakness for our purposes is 
that GDPval focuses on specific, well-understood, well-scoped tasks — not entire jobs. And 
that’s the thing that we’re more interested in. A different test that does try to imagine 
an entire job is Vending-Bench 2. This is a fully simulated environment in 
which AI models are given $500, put in charge of a vending machine and asked 
to make as much money as possible. There’s a very wide range of actions that they 
can consider and potentially take. But of course it’s a fully artificial setup, a 
little bit like a souped-up computer game. So how did they do? Well, a year ago, 
models were finishing the simulation with $1,000 and now they’re making more 
like $10,000 — a significant step up. But the creators of the benchmark think that a 
good human player would be able to make over $60,000. So the AIs have some way to 
go yet to match human performance. The analysis of the graphs that you’re seeing 
is complicated by the fact that some recent models have done worse because they’ve been 
trained to be more ethical and not engage in the extremely cutthroat business tactics 
that are the best way to win at this game. And I’m not sure how much to really 
care about this benchmark either, because apparently the optimal strategy 
in the setup is pretty weird and involves talking suppliers down — so they’re giving you 
your stock almost for free — and exclusively selling really high-margin items in the vending 
machine, things like family-sized Doritos. The trouble the models have is that basically they 
don’t zoom out and analyse how to play the game, how to maximise the profit that they’re making, 
in the way that any sensible human player would. The next step up in realism and difficulty 
is something called the AI Village. The AI Village is a project that sets up 
a range of AI models to work either together or individually to basically 
do project management in the real world. They’ll ask the models to fundraise 
money for charity, organise a live event, report breaking news, adopt and clean a real 
park in San Francisco. So this is real stuff. We’re getting a bit more realistic, even if 
the tasks aren’t insanely difficult per se. How do the models do? This one is 
especially hard to summarise. I had a difficult time because the projects 
and the models and the technical setup have changed a lot over the one to two 
years that the project’s been running. But the short answer is not too well. They’ve had 
some partial successes. They’ve raised $2,000 for charity. There was a live event in Dolores Park 
in San Francisco that 23 people came to. They sold $200 worth of merchandise. They recruited 
39 participants for an experiment that they designed. They managed to get 98 
subscribers onto their Substack. If that record of achievement sounds kind of 
thin to you, it also sounds pretty thin to me as well. I wouldn’t exactly feel great 
putting that record of success on my CV. In previous years, models basically would just 
forget what they were doing and get completely lost in a fog of their own hallucinations 
about what even setup they were running in. Humans had to intervene to give them any hope 
of accomplishing anything in the real world at all. They’re a lot better today, but 
they still can’t get a lot done because, among other things, they spend far too much 
time planning and not enough time executing. Which at last brings me to the single 
most ambitious attempt to see what AIs can do when unleashed on the world: Andon 
Labs putting AI models fully in charge of a retail shop in San Francisco and a café in 
Stockholm. These are actual businesses that you could go visit if you want. And the AI has 
managed almost everything, including getting licences to operate from the government, hiring 
staff, attracting customers, ordering supplies. So how have they done? For me, the key takeaway 
from all of this is that the shops exist and they sort of work. The café in Stockholm has hired two 
baristas. The AI scaffold, which they call Mona, manages both of them through Slack and does 
an OK job. Mona successfully navigated Swedish bureaucracy and got the café an electricity and 
broadband supplier. The AI applied to the police to be allowed to have outdoor seating. Most 
of the time, the AI is able to order in coffee and food for the day — but sometimes forgets and 
misses the deadline, so there’s no coffee or food. So far, the shop has sold $10,378 worth of coffees 
and pastries. But Mona has done some odd stuff as well. For the outdoor seating application, it 
simply completely hallucinated the café’s floor plan. It impersonated an Andon Labs employee 
to try to obtain an alcohol licence. And after being busted doing that and told to stop, it just 
tried again using a different employee’s name. It tends to order items the moment they 
come to mind, rather than on any sort of regular cycle. To get around tomatoes going 
bad in the café, it decided to order canned tomatoes to put on the café sandwiches instead 
of normal tomatoes. It also ordered 120 eggs, even though the café has no way to cook eggs. 
And staff at the café have a ‘shelf of shame,’ where they display all the odd stuff that 
Mona has ordered. Though I’ll be honest, when I actually read the list, everything on 
that shelf seemed like a totally reasonable thing to buy to me. So I guess I 
shouldn’t be in the café business. Anyway, the café had $18,000 in its bank account 
at the beginning, and two months in it’s now down to $2,000. Still, I would say that the fact that 
the café operates at all and is able to serve coffees is a partial success at this kind of task. 
Cafés in cities are a very competitive business, so it’s not exactly a shock that an AI can’t 
compete with the best cafés humans have managed to run in Stockholm. Most new cafés 
opened by humans go out of business as well, I think a substantial majority do go out 
of business within the first few years. How about that shop in San Francisco? That 
one’s been going for about three months now, as of writing, and it’s run by a scaffold 
around Claude, which the operators call Luna. Again, the key takeaway for me is that 
the shop works — just about. It stocks a super eclectic set of items and 
it struggles a bit with scheduling and has had some amusing screwups, like 
ordering too many toilet seats for the bathroom and deciding to sell the extra 
toilet seats as merchandise to customers. But Luna is kind of decent at managing day-to-day 
operations. The big challenge for the model seems to be with long-term business strategy, which 
it really doesn’t put almost any thought into at all. That type of open-ended thinking and 
prioritisation is a lot harder to train because it has low feedback density and it hasn’t been the 
main focus for AI companies either. They prefer to double down on areas where the models are already 
at human level, or perhaps above human level. So far the store’s bank balance has 
gone from $94,000 when it opened, down to $64,000 now — mostly just disappearing to 
cover San Francisco’s phenomenal business rents. Finally, just as I was drafting this piece, a new 
eval launched called AA-Briefcase. It tries to get models to complete a full month of work in domains 
like product management and industry strategy. I haven’t had time to properly dig into 
it yet, but the benchmark says it demands models “sort through thousands of messy input 
files, balance competing stakeholder demands, and produce complex deliverables reflecting 
the core challenges of real knowledge work.” As usual, Fable is the leader and the 
models do plenty of specific things well. But even Fable was only able to complete 
everything in a task around 3% of the time, which makes sense given their 
difficulty with tasks of this type. It’s a benchmark I expect to be keeping 
an eye on, and you might like to as well. Zooming out and considering all 
four or five experiments here, we can see that AIs are much worse at messy 
tasks than clean ones. At the same time, if you inspect their internal thinking and 
planning, they’re clearly getting better at the messy tasks. They’ve basically gone 
from catastrophic failure to mere failure. In my view, it is really unfortunate and 
inconvenient that we don’t have evaluations capable of determining whether their rate of 
improvement is faster for messy tasks or for clean tasks — that is, whether the gap between 
those capabilities is shrinking over time or getting wider over time. And I actually think that 
is one of the top handful of research questions relevant for projecting when AI is going to 
have massive, widespread societal impacts. The thing is, the nature of these two different 
types of activities — messy and clean tasks — is so different that it’s hard to get a consistent 
comparable measure across both types of tasks that would allow you to say something like, 
“The model’s got 20% better at clean tasks, but only 10% better at messy tasks.” It’s a 
little bit unclear what that would even mean. And in the absence of something decisive like that 
— some sort of decisive piece of evidence that can settle the debate — I at least hope we see more 
experiments like the ones Andon Labs has set up. If those shops ever do start to turn a 
profit and compete successfully against human business managers, for me, that would be 
a really big update that AI is getting close to being able to do entire jobs, not just parts 
of them, and we’re closing in on full AGI. Exhibit 6 takes us to the other 
extreme of task messiness. In May of this year, OpenAI announced that an 
unreleased model had made meaningful progress on a quite famous mathematics puzzle. 
It demonstrated that a widely believed conjecture regarding something called the 
unit distance problem was actually false. And remarkably, it did that with just a normal 
chain of thought, not using any maths programs or tools. And this was just an ordinary language 
model, not one trained to be specialised in maths in particular. The mathematics community 
reported that it was pretty impressed. The unit distance problem has gotten a lot 
of attention over the years and it’s a very widely known puzzle in the mathematics 
community. So it’s impressive for anyone to be able to say something significant 
and new about it, whether human or AI. But the reason this result is relevant to 
AGI timelines is that producing an original mathematical result could be a sign that AIs 
are getting into the business of generating novel ideas and not just remixing what’s 
in their training data one way or another. So how did the model pull it off? 
Basically, by laying out all the possible ways of disproving the conjecture 
and methodically working through them, concluding in turn that each was a dead end until 
only one was left — and then it kept going hard, trying to make it work, until eventually 
it did. It didn’t do anything reward-hacky or alien, something that only an AI could do. 
Apparently its approach was pretty human-like, and all the ingredients were in the maths 
literature somewhere or other, which might reflect the fact that it has been trained on all 
the maths proofs that humans have ever generated. So why did AI manage to come up with this proof and not a human? Mathematicians 
have come up with three main reasons: The first is that they actually 
believe the conjecture was true, so very few of them were spending time actively 
trying to demonstrate that it was false. Second, the proof relied on bringing 
in a technique from a very different branch of mathematics — one that few people 
working on the unit distance problem would have likely encountered. And that’s a big AI 
strength in general. Even where they’re not as analytically good as the best humans, they 
have an extraordinary encyclopaedic knowledge of all kinds of different things, so they’re 
in a much better position to find connections that we humans might naturally have missed.
The third reason is that the type of proof it pursued is especially laborious 
and tedious to go through. One human mathematician actually did start pursuing 
it in this exact case, but they quickly got overwhelmed by the complexity and they knew 
that success wasn’t guaranteed, so they decided their research time was better spent elsewhere.
So is this an update in favour of AGI arriving soon? Personally, I think it’s very unclear. We 
know and expect that AI models will be great at mathematics. They’re being trained on it and it 
plays to some of their core strengths: a highly structured environment with feedback that can be 
automated. If anything, given those advantages, I’m kind of a little bit surprised that they 
haven’t accomplished more in the maths domain already. I think a year or two ago I tweeted 
that I thought we might be on the verge of a real renaissance in AI mathematics. But that hasn’t 
turned out to be the case, at least not yet. That might be because not many 
people are actually trying, but it’s also possible that a lot of attempts 
are being made — because OpenAI hasn’t actually said how much compute they had to throw at 
trying to crack different open mathematics puzzles in order to get this one significant 
piece of success. And without knowing that, it’s kind of hard to know whether 
to be, on balance, impressed or not. I would change my mind on that if — in the chains 
of thought of the AIs when trying to solve maths problems — the AIs started to have big flashes 
of insight into the problem that they’re working on in the way humans occasionally do: thinking 
about a problem, then suddenly reconceptualising the whole situation and making some abrupt 
breakthrough. Typically, that’s actually not how humans solve maths problems. They more often do 
it by methodically applying familiar tools to new problems — basically like what happened here. And 
as far as I know, it’s not something that we’ve seen AIs do basically ever yet: have a massive 
flash of insight that no one else has before. The reason that would update me 
more than this result is that the models aren’t being directly reinforced for 
having big flashes of insight. And it’s not something that even the best humans manage to 
do frequently. So it would suggest something new and important might be developing in 
their minds that wasn’t present before: a deeper understanding of the world and 
the problems that they’re dealing with, perhaps. Perhaps that thing would carry over 
to other research domains as well, things like economics or chemistry — or more importantly 
for our purposes — AI research and development. The bottom line for me is that, 
in terms of getting to AGI, I’m going to assume that AI is going 
to be superhuman at maths and pay more attention to the more uncertain 
thing, which in my mind is AI’s ability to get good at messy, real-world 
tasks like running a café or a bookstore. So that’s one piece of evidence 
that I thought was very cool, but it hasn’t particularly updated 
my AI timelines or forecasts yet. Here’s a final one that I did 
update significantly on last time, but I now need to partially 
or significantly walk back. In my previous timeline video, I suggested 
that more than half of capabilities gains observed through 2025 might have 
been driven by letting models use more compute to answer the same question 
— something known as inference scaling. That’s a bearish indicator for AI, relative 
to making progress by getting the models to be more intelligent and insightful 
per token they output. And that’s because inference scaling requires you to use 
more compute every time you ask a question, rather than just one time while training 
the smarter model in the first place. In January, I argued that to achieve the 
capabilities gains that we were observing, we were having to spend more and more 
money to get the answers. And as a result, we were trending towards AI becoming uneconomical 
— that is to say, it costing more to get an AI to complete a task than it would have cost to 
just get a human to do it in the first place. Since then, new evidence has come out suggesting 
that things are not as extreme as I thought. An analysis of METR’s time horizon benchmark 
by Redwood Research found that as the tasks models have been doing have gotten more 
significant, the cost of getting AIs to successfully complete them has remained around 
3% of the cost of getting a human being to do it. How can that be the case if their chains of 
thought are getting so much longer? Well, the AIs are absolutely producing much longer 
chains of thought than they used to — hundreds or thousands of times longer than several years 
ago in fact. But the main reason for that is we’re giving them much more significant tasks now. 
And we know that if we give AIs bigger tasks, they’re going to need to use more compute and 
do more thinking in the process of solving it. That alone doesn’t suggest that AIs are 
becoming less economical to operate, because bigger tasks would also take a human longer to 
complete as well. And humans cost money too. So when comparing very different types of 
tasks, we really need to look at how long the AI would need to think for, relative to how 
long a human would have taken to accomplish the same thing. And on that count, Redwood finds that 
the cost of AIs relative to humans isn’t going up. There’s a smaller secondary factor at play 
as well: the models do produce longer chains of thought than they used to, even to complete 
the same task, but the dollar cost of each token output has decreased a bit over time, as chips and 
algorithms have gotten more efficient. That means you can have a somewhat longer chain of thought 
without it becoming unreasonably more expensive. Now it’s just one analysis of one benchmark, 
so I don’t think this is the final word on the inference-scaling question. But 
that result — combined with companies’ demonstrated willingness 
to pay a lot for AI labour, if they’re doing useful work — that’s made me 
think the costs of inference scaling aren’t going to be a significant constraint on AI 
capabilities, at least in the next few years. And that 3% figure, it’s kind 
of right in broad strokes. It’s an interesting number in another way 
because it suggests that — if we really, really want to — we still have a one-off 
opportunity to further improve AI performance sitting on the ground waiting for someone to 
pick it up. For something really important, we could give an AI 30 times as long 
to think about it as we do on average today — and that would still only cost as much 
as hiring a human being to do that same thing. To be clear, this would only create a one-off 
jump in performance — and after that jump it would go back to the same trend as before. And it 
would come at a massive cost, which is that the AIs would no longer be cheaper than human staff. 
On top of that, the performance improvement you get from scaling inference compute by 30-fold, 
it isn’t always that large. At some point, both humans and AIs hit seriously declining returns 
thinking about a given problem for much longer. But it’s relevant because AI companies might 
be willing to pay a huge amount to run models to replace their fabulously expensive 
staff in particular. And over time, models are getting better at organising and 
structuring their thoughts in such a way as to make practical use of really large 
compute budgets. So it’s one to watch. So how should all of these conflicting 
indicators actually affect our forecasts, our AI and AGI timelines? Well, for better or worse, that depends on what 
you were personally predicting would happen in the first place — and so what from the above 
list was a surprise, what was an update for you? But for me personally, there are five updates in favour of AGI coming sooner 
on the list, and those are: Very useful AI agents arriving about a year 
or so earlier than I might have guessed AI revenue exploding even faster 
than I, or almost anyone, anticipated Anthropic reporting that AI is now significantly 
speeding up their research and their work Mythos’s new pretraining run enabling frontier 
AI capabilities to jump three months ahead of schedule — something that might happen 
from time to time in future as well And finally, inference scaling being 
less expensive than I thought it was There’s one piece of evidence that 
for me personally is ambiguous, which is AI coming up with one 
original research result in maths. There’s one thing that’s impressive, but it’s 
progressed only as I was expecting it to, which is AI doubling the length of tasks 
they can complete every four months, basically the same trend that we had before. And there’s one piece of evidence in 
favour of AGI coming later, which is, at least in my mind: AI continuing to 
be pretty bad at messy real-world tasks, despite becoming really good at least 
some types of computer-based tasks. On balance, I’d say my timelines to AGI — 
balancing all of this — they’ve shortened by something like one year as a result of 
everything we’ve seen in 2026. And I think that’s fairly typical of other people following 
this stuff closely, at least the ones who I read. Back in January I said that personally I 
would be pretty shocked if we got fully automated AI research and development in 
2027. In 2028, I guess it’s imaginable, but it’s going to require some surprising 
breakthroughs or an acceleration beyond what we’re seeing right now. But by 
2029, 2030 begins to feel plausible. Well, I think we got some surprising 
breakthroughs, which roughly means that all these categories for me have come forward by one notch. 
Now I’d be shocked if we got fully automated AI R&D this year, in 2026. Next year, 2027, that’s 
imaginable, and it seems to be what Anthropic is really gunning for. And fully automated AI 
research and development becoming possible in 2028 feels plausible if today’s trends just 
merely keep marching on for another two years. In March, Paul Christiano, probably the 
only US government employee working on AI governance who has actually made major 
research contributions in AI itself, wrote the following in a personal capacity: “We are now around the 90th percentile of my 
AI timelines from 2021 [and from 2019]. I think we’ve now seen enough signs that there could be a 
relatively fast takeoff starting very soon. We no longer have strong quantitative indicators 
that transformative AI isn’t coming soon, and are flying blind. 1–4 year timelines 
are consistent with existing trends.” I agree with Paul, and frankly it’s quite scary. But back in January I also said there’s a very 
real chance that we’re in for a significantly longer and slower takeoff that takes until the 
mid-2030s, and I still believe that as well. This video has gotten a little bit long, so the full justification for that might 
have to wait for another day. But here are the top four reasons longer timelines 
remain very much on the table in my mind: First, nobody knows how broad the range of skills 
is that an AI has to be great at, in order to get fully autonomous recursive self-improvement 
off the ground. As I’ve said repeatedly, just being a great coder, clearly that’s 
not enough by itself. But do we need these models to be able to do everything an Anthropic 
staff member can do, even the most brilliant ones? Do we need them to be able to have research 
insights on the level of a superstar researcher, someone like Ilya Sutskever or Alec Radford? Or 
could they maybe make do by just being OK at some parts of the job, but being very numerous and 
really fast thinkers? I didn’t know the answer to that a year ago and I really don’t feel 
like I have any better idea about it now. Second, there may be truly crucial 
capabilities necessary for general intelligence that are mostly missing 
from current models and which are very hard to train using current methods. 
Some possible options for that are: Generalising far out of distribution, 
and learning sample efficiency, to areas where AI models are still 
much, much weaker than human beings Another candidate is creativity and original 
insight and research, like I was talking about before — something which might require a type 
of internal world model or deep understanding that large language models aren’t currently 
developing, not in a full sense at least Third, we don’t know how much using reinforcement 
learning from verified rewards — on coding and similar tasks like that — will lead to spillover 
improvements in other nonverifiable domains, ones with much worse feedback density. If those 
spillovers are weak, then we should expect to see AIs become exceptional superhuman coders while 
still remaining quite mediocre at more complex or open-ended projects, like running a small 
business or overseeing some research programme. On the other hand, if the spillovers are strong, then scaling RLVR might be enough to get models 
to human-level at those things just by itself. Four years on from the release of ChatGPT, as far 
as I can tell, we remain incredibly in the dark about how large those spillovers are. The labs 
might well know more internally from their own experiments, but if so, they’re not publishing 
— or at least no one’s emailed it to me yet. Fourth, as I mentioned above, it’s possible 
we might automate AI R&D and find that, in the immediate term, it doesn’t 
make that much of a difference. The most likely reason for this would 
be if the whole research process just gets bottlenecked by access to the compute 
required to train models and run experiments. If so, Anthropic might plausibly 
replace all of its staff with AIs and find that the overall rate 
of research progress only, say, doubles. Or it might increase 10-fold 
or 20-fold. We really just don’t know. To my eye, these four big uncertainties 
are the four biggest cruxes of disagreement between people in the AI industry who 
think superintelligence might be here in 2028 on one extreme, and those who think it’s 
still 15 years away or 20 or 25 years away. And on top of all of that — as I 
explained in some detail back in January — by 2030 the AI industry is on 
track to be absorbing a huge fraction of all the computer chips being manufactured 
and all of the memory being manufactured, which means they won’t be able to scale up 
training compute as fast as they are now, where they can basically get a boost to their 
scaling by progressively diverting more and more production away from all the other applications: 
gaming, phones, computers, all of that. So unless we unlock something new by then, 
it will be quite reasonable to expect that capabilities advances will slow down after 
that point, and we’ll have a bit more of a slog to get to recursive self-improvement 
or artificial general intelligence or artificial superintelligence if we 
haven’t managed to do it by then. Last time I spoke about AI timelines, I closed out by observing that even long 
timelines are ridiculously short now. I pointed out that even if things play out 
in a way that’s surprisingly easy to handle, and AGI doesn’t arrive until 2036, that’s 
still an incredibly short period of time to figure out how to absorb such an enormous, 
wide-ranging shock without society descending into violence or authoritarianism, 
or some other horrible outcome. That’s still completely true, but with another 
six months spent now and timelines even shorter, I would go further. In the past, 
as regular listeners will know, I’ve been pretty ambivalent about efforts to 
slow down or pause AI progress. Back in 2023, I was approached about signing the famous pause 
letter and ultimately decided, on balance, not to. But I think we’re approaching the 
crossover point now at which the benefits of slowing are going to start outweighing the 
costs in a way they simply didn’t before. And I’m far from alone in 
suspecting that. Anthropic, OpenAI, and Demis Hassabis of DeepMind, 
they’ve all said that they want us to build the capacity to implement a 
coordinated pause — especially on the most dangerous types of research — should 
future evidence indicate that it’s necessary. AI insiders, at least many of them, are 
legitimately scared of what’s coming next, and many are desperate to be given extra time, 
extra months, extra years to understand the machines they’re building before they’re 
unleashed on the world. In my opinion, we should give them that time. And on 
that note, I’ll speak with you again soon.
