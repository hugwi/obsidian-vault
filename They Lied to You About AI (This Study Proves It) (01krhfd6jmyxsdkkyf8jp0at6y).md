---
categories:
  - "[[Resources]]"
domain: engineering
title: "They Lied to You About AI (This Study Proves It)"
source: "https://www.youtube.com/watch?v=AIYQp1n51ZI"
author: "Caleb Ulku"
published: 2026-03-17
created: 2026-05-13
description: "👉 Join me on the 21st for a FREE Live Class to learn how AI can do SEO work:"
tags:
  - to-process
  - llm-foundations
---

A father and son just mathematically proved that an AI agent will never do what Silicon Valley is promising. Not probably won't. Not might have limitations. They've mathematically proved they use computational complex theory that's been settled since the 1960s. And this isn't coming from some AI doomer clickbait journalist. This is coming from Vishel Sika, former CEO of Infosys, board member at Oracle and BMW. He's a Stanford PhD who literally studied under John McCarthy. He's the 

guy who coined the term artificial intelligence. He and his son just published a paper that no one in AI marketing departments wants you to read, especially right now as we enter the era of Magnus and Open Claw, the agents that can use your browser and click buttons for you. It looks like AGI has arrived, but Sika says we're actually just watching the ceiling get higher, not disappear. Their argument is simple. LLMs can only perform a certain number of computations per response. That 

number is fixed. And if a task requires more computation than that ceiling allows, the model will either fail or hallucinate. And this isn't a maybe. It's baked into the math. But if the math is so broken, then why are the big players still promising the world? I'll tell you the devious reason why at the end of this video, but first, I want to look at the ceiling that they discovered. Now when you send a prompt to chat GPT or cloud or Grock or any of the current frontier models, the model 

will do a fixed amount of work to generate each word as an output. This happens through the self attention mechanism. This is of course very simplified. But think of it like this. Every word in your prompt needs to look at every other word to understand the context. So if you have a thousand words, it's a million comparisons. A thousand a thousand. But there's no let me think about this harder. There's no give me more time on this one. Every token gets the same budget. A simple hello gets the same number of operations as a complex physics problem. That's the 

ceiling. It's not about better hardware. It's about the architecture of how the systems actually work. The paper and I have it here on screen if you want to read it. It uses traveling salesman problem as an example. To visit 20 cities and figure out the shortest possible route between those cities, you need to check over two quintilion combinations. An LLM physically cannot do that math in one shot. So, what does it do? It guesses. It pattern matches. It gives you something that looks 

plausible and it's not a bug. That's the architecture. But how would you actually handle tasks that require that level of computation? Next, I'll show you why even verifying the answers is just as impossible for these models. The authors of this paper make a distinction. Doing a task versus verifying it. Now, you'd think that the model could at least check if the answer is right, even if it can't handle the computational complexity to calculate it. But no, verification often requires just as much 

work as solving the problem up front. Every AI demo you've ever seen, it was running tasks designed to stay under the necessary complexity ceiling. They work because they're designed to work. Meanwhile, the real world tasks that your business actually needs are going to blow right past that ceiling. And this is where Sika's background becomes a factor. This isn't an outsers's perspective. Remember, he studied under John McCarthy, the man who literally coined the term artificial intelligence. He's bridging the gap between the 

foundational laws of the 1960s and the chaotic world of AI in 2026. He isn't saying these tools are useless. Far from it. He's just saying they're being marketed as reasoning engines when the math proves they're actually pattern mirrors. They reference the time hierarchy theorem. Again, I don't mean to throw so many fancy words, but this basically says that some problems require a minimum number of steps. You just can't shortcut them. And the argument that the paper makes, if a task needs more steps than the model can 

perform, it will unavoidably hallucinate. Unavoidably. And this is why hallucination isn't a training issue. Yes, more recent models have gotten better at it, but for certain problems, hallucination is the only possible output. But wait, you might be thinking, what about the new agentic era? Tools like Manis or OpenClaw. They don't just give one answer. They run thousands of loops, browsing the web and thinking through step by step. The tech community is calling this chain of thought or agentic workflows. And the 

idea is that if a model has a ceiling, just spread the problem across more steps. Give it more room to work. But Sika's paper argues this as a trap. And here's why. If you have a fixed amount of thinking power per word, giving the AI more steps is like giving a writer more sheets of paper. Each individual sheet is still the same size. You haven't made the writer smarter. You've just given them more room to ramble off topic. That's why you'll see an agent book a flight perfectly, but then get stuck in a bizarre infinite loop trying 

to change a seat assignment. The math, specifically again that time hierarchy theorem, says that for complex problems, errors eventually compound. The model goes off track at step five, and because it can't mathematically verify its own logic, the whole chain eventually falls apart. In the Agentic era, hallucination isn't a training bug. It's a cumulative mathematical certainty. Then of course you might be arguing, well they can just use a tool, give it a calculator. After all, we wouldn't expect a human to be 

able to calculate the traveling salesman problem by hand. But Sika acknowledges this as well. You can build components around LLMs to overcome the limits, of course. And then the LLM becomes an orchestrator. But notice what just happened. The LLM didn't solve the problem. It just handed it off to a classical algorithm that could. But the catch, the model still has to verify that that tool worked. And if verifying correctness requires more math than the model can do, again, the agent fails in unpredictable ways. Well, what about 

those massive context windows? Gemini 3 Pro can see a million tokens at once. Yes, that solves information access. It doesn't solve the computational steps per word. Having a bigger filing cabinet doesn't help if you don't have the brain power to process what's inside. So, what does this mean for you? Now, the paper, it's not saying that AI is useless. Indeed, it it definitely is not. I use these tools every day in my business. I'm sure most of the people watching this do as well. For the right applications, current AI, the current 

frontier models are exceptional. Writing drafts, summarizing, reformatting data, research, and comparison. These stay under that ceiling. The problem is the gap between reality and the pitch decks. AI agents will autonomously run your business is a lie. The math just doesn't support it. To see this in action, look at vending bench 2 from Anden Labs. This is the 2026 gold standard for testing AI agents at running a business. Models like Claude Opus 4.6 Gemini 3 Pro. They're given $500 in a year to run a 

simulated vending machine business. And on paper, the agents look like they're winning. The current leader, Claude Opus 4.6, netted $8,000 in profit. Here's that test, Vending Bench 2. Feel free to look it up yourself. And here are the current standings for Frontier Models. We can see Claude Opus 4.6 $8,000. Pretty good. But here's the actual ceiling. And in labs calculated a human baseline for this exact same simulation. Let me scroll down and show that to you. 

It's a long paper here. This isn't the best ever, $63,000 a year. This is a human baseline and it blows the AI models out of the water. The reason the AI models can't make $63,000 a year is because they lose coherence over a long time frame. Result, the frontier models, the best we can make now, aren't hitting even 15% of a human baseline. Over these runs, we've seen agents honestly give away their inventory for free due to 

social engineering or they've even tried to contact the FBI to report their own $2 bank fees as fraud. And this is the time hierarchy theorem in the wild. As the chain of tasks gets longer, the AI's ability to verify its own logic collapses. It doesn't matter how smart the model is. The math says that without a human to reset the error rate, the autonomous chain will eventually break. So here's what you actually do to stay on the winning side of this math. First, 

be specific about tasks. [music] Draft an email using my tone and cadence that works. automate this workflow is going to fail. Build in human verification. This is a structural requirement, not an option. And third, use AI for pattern recognition, not logic heavy math. But here is the real tip off. Why the singularity probably isn't as close as people keep saying? Because if the singularity were just months away, why are the smartest people in the room quitting? Look at the insiders. If open 

AI was about to hit AGI, why would senior engineers be leaving to start risky startups? If you knew the world was about to change forever, you wouldn't leave. You wouldn't leave Open AI if they're on the verge of AGI. You'd stay to be part of the release of a lifetime, to be part of the equity of of a lifetime, unless you saw the ceiling. Now, they know the next model will be better, but not qualitatively different. Just like chat GPT5, it was better than four, but not qualitatively different. 

They're starting companies that use AI as a tool, not companies that use AI as a god. The opportunity here is not chasing some imaginary AGI. The opportunity is an understanding exactly what AI can do for you right now. The ceiling is real, but there's a lot of room underneath 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 A father and son just mathematically
 </span>
 <span data-rw-start="2.08" data-rw-transcript-version="2">
 proved that an AI agent will never do
 </span>
 <span data-rw-start="4.16" data-rw-transcript-version="2">
 what Silicon Valley is promising. Not
 </span>
 <span data-rw-start="6.64" data-rw-transcript-version="2">
 probably won't. Not might have
 </span>
 <span data-rw-start="8.559" data-rw-transcript-version="2">
 limitations. They've mathematically
 </span>
 <span data-rw-start="10.4" data-rw-transcript-version="2">
 proved they use computational complex
 </span>
 <span data-rw-start="12.639" data-rw-transcript-version="2">
 theory that's been settled since the
 </span>
 <span data-rw-start="14.639" data-rw-transcript-version="2">
 1960s. And this isn't coming from some
 </span>
 <span data-rw-start="16.8" data-rw-transcript-version="2">
 AI doomer clickbait journalist. This is
 </span>
 <span data-rw-start="19.68" data-rw-transcript-version="2">
 coming from Vishel Sika, former CEO of
 </span>
 <span data-rw-start="22.4" data-rw-transcript-version="2">
 Infosys, board member at Oracle and BMW.
 </span>
</p>
<p>
 <span data-rw-start="25.359" data-rw-transcript-version="2">
 He's a Stanford PhD who literally
 </span>
 <span data-rw-start="27.68" data-rw-transcript-version="2">
 studied under John McCarthy. He's the
 </span>
 <span data-rw-start="30.08" data-rw-transcript-version="2">
 guy who coined the term artificial
 </span>
 <span data-rw-start="32.239" data-rw-transcript-version="2">
 intelligence. He and his son just
 </span>
 <span data-rw-start="34.399" data-rw-transcript-version="2">
 published a paper that no one in AI
 </span>
 <span data-rw-start="36.64" data-rw-transcript-version="2">
 marketing departments wants you to read,
 </span>
 <span data-rw-start="38.719" data-rw-transcript-version="2">
 especially right now as we enter the era
 </span>
 <span data-rw-start="41.28" data-rw-transcript-version="2">
 of Magnus and Open Claw, the agents that
 </span>
 <span data-rw-start="44.16" data-rw-transcript-version="2">
 can use your browser and click buttons
 </span>
 <span data-rw-start="46.239" data-rw-transcript-version="2">
 for you. It looks like AGI has arrived,
 </span>
 <span data-rw-start="49.039" data-rw-transcript-version="2">
 but Sika says we're actually just
 </span>
 <span data-rw-start="51.039" data-rw-transcript-version="2">
 watching the ceiling get higher, not
 </span>
 <span data-rw-start="53.36" data-rw-transcript-version="2">
 disappear. Their argument is simple.
 </span>
</p>
<p>
 <span data-rw-start="55.92" data-rw-transcript-version="2">
 LLMs can only perform a certain number
 </span>
 <span data-rw-start="58.32" data-rw-transcript-version="2">
 Of computations per response. That
 </span>
 <span data-rw-start="60.96" data-rw-transcript-version="2">
 number is fixed. And if a task requires
 </span>
 <span data-rw-start="63.68" data-rw-transcript-version="2">
 more computation than that ceiling
 </span>
 <span data-rw-start="65.76" data-rw-transcript-version="2">
 allows, the model will either fail or
 </span>
 <span data-rw-start="68.799" data-rw-transcript-version="2">
 hallucinate. And this isn't a maybe.
 </span>
</p>
<p>
 <span data-rw-start="71.36" data-rw-transcript-version="2">
 It's baked into the math. But if the
 </span>
 <span data-rw-start="73.28" data-rw-transcript-version="2">
 math is so broken, then why are the big
 </span>
 <span data-rw-start="75.92" data-rw-transcript-version="2">
 players still promising the world? I'll
 </span>
 <span data-rw-start="78.64" data-rw-transcript-version="2">
 tell you the devious reason why at the
 </span>
 <span data-rw-start="80.72" data-rw-transcript-version="2">
 end of this video, but first, I want to
 </span>
 <span data-rw-start="82.479" data-rw-transcript-version="2">
 look at the ceiling that they
 </span>
 <span data-rw-start="84" data-rw-transcript-version="2">
 discovered. Now, when you send a prompt
 </span>
 <span data-rw-start="85.84" data-rw-transcript-version="2">
 to chat GPT or cloud or Grock or any of
 </span>
 <span data-rw-start="88.4" data-rw-transcript-version="2">
 the current frontier models, the model
 </span>
 <span data-rw-start="90.56" data-rw-transcript-version="2">
 will do a fixed amount of work to
 </span>
 <span data-rw-start="92.56" data-rw-transcript-version="2">
 generate each word as an output. This
 </span>
 <span data-rw-start="94.64" data-rw-transcript-version="2">
 happens through the self-attention
 </span>
 <span data-rw-start="96.479" data-rw-transcript-version="2">
 mechanism. This is, of course, very
 </span>
 <span data-rw-start="97.92" data-rw-transcript-version="2">
 simplified. But think of it like this.
 </span>
</p>
<p>
 <span data-rw-start="99.759" data-rw-transcript-version="2">
 Every word in your prompt needs to look
 </span>
 <span data-rw-start="102.079" data-rw-transcript-version="2">
 at every other word to understand the
 </span>
 <span data-rw-start="104.24" data-rw-transcript-version="2">
 context. So if you have a thousand
 </span>
 <span data-rw-start="106.159" data-rw-transcript-version="2">
 words, it's a million comparisons. A
 </span>
 <span data-rw-start="108.64" data-rw-transcript-version="2">
 thousand, a thousand. But there's no, let
 </span>
 <span data-rw-start="110.799" data-rw-transcript-version="2">
 me think about this harder. There's no
 </span>
 <span data-rw-start="112.64" data-rw-transcript-version="2">
 Give me more time on this one. Every
 </span>
 <span data-rw-start="114.399" data-rw-transcript-version="2">
 token gets the same budget. A simple
 </span>
 <span data-rw-start="117.28" data-rw-transcript-version="2">
 hello gets the same number of operations
 </span>
 <span data-rw-start="119.52" data-rw-transcript-version="2">
 as a complex physics problem. That's the
 </span>
 <span data-rw-start="122.159" data-rw-transcript-version="2">
 ceiling. It's not about better hardware.
 </span>
</p>
<p>
 <span data-rw-start="124.24" data-rw-transcript-version="2">
 It's about the architecture of how the
 </span>
 <span data-rw-start="126.32" data-rw-transcript-version="2">
 systems actually work. The paper and I
 </span>
 <span data-rw-start="128.56" data-rw-transcript-version="2">
 have it here on screen if you want to
 </span>
 <span data-rw-start="130.64" data-rw-transcript-version="2">
 read it. It uses traveling salesman
 </span>
 <span data-rw-start="132.8" data-rw-transcript-version="2">
 problem as an example. To visit 20
 </span>
 <span data-rw-start="135.36" data-rw-transcript-version="2">
 cities and figure out the shortest
 </span>
 <span data-rw-start="137.2" data-rw-transcript-version="2">
 possible route between those cities, you
 </span>
 <span data-rw-start="139.12" data-rw-transcript-version="2">
 need to check over two quintillion
 </span>
 <span data-rw-start="140.879" data-rw-transcript-version="2">
 combinations. An LLM physically cannot
 </span>
 <span data-rw-start="143.84" data-rw-transcript-version="2">
 do that math in one shot. So, what does
 </span>
 <span data-rw-start="146.8" data-rw-transcript-version="2">
 it do? It guesses. It pattern matches.
 </span>
</p>
<p>
 <span data-rw-start="149.92" data-rw-transcript-version="2">
 It gives you something that looks
 </span>
 <span data-rw-start="151.52" data-rw-transcript-version="2">
 plausible and it's not a bug. That's the
 </span>
 <span data-rw-start="153.84" data-rw-transcript-version="2">
 architecture. But how would you actually
 </span>
 <span data-rw-start="155.76" data-rw-transcript-version="2">
 handle tasks that require that level of
 </span>
 <span data-rw-start="158.319" data-rw-transcript-version="2">
 computation? Next, I'll show you why
 </span>
 <span data-rw-start="160.319" data-rw-transcript-version="2">
 even verifying the answers is just as
 </span>
 <span data-rw-start="163.28" data-rw-transcript-version="2">
 impossible for these models. The authors
 </span>
 <span data-rw-start="165.44" data-rw-transcript-version="2">
 of this paper make a distinction. Doing
 </span>
 <span data-rw-start="168" data-rw-transcript-version="2">
 a task versus verifying it. Now, you'd
 </span>
 <span data-rw-start="170.879" data-rw-transcript-version="2">
 Think that the model could at least
 </span>
 <span data-rw-start="172.4" data-rw-transcript-version="2">
 check if the answer is right, even if it
 </span>
 <span data-rw-start="174.56" data-rw-transcript-version="2">
 can't handle the computational
 </span>
 <span data-rw-start="176" data-rw-transcript-version="2">
 complexity to calculate it. But no,
 </span>
 <span data-rw-start="178.08" data-rw-transcript-version="2">
 verification often requires just as much
 </span>
 <span data-rw-start="180.64" data-rw-transcript-version="2">
 work as solving the problem up front.
 </span>
</p>
<p>
 <span data-rw-start="182.959" data-rw-transcript-version="2">
 Every AI demo you've ever seen, it was
 </span>
 <span data-rw-start="185.76" data-rw-transcript-version="2">
 running tasks designed to stay under the
 </span>
 <span data-rw-start="188.08" data-rw-transcript-version="2">
 necessary complexity ceiling. They work
 </span>
 <span data-rw-start="190.4" data-rw-transcript-version="2">
 because they're designed to work.
 </span>
</p>
<p>
 <span data-rw-start="192.319" data-rw-transcript-version="2">
 Meanwhile, the real world tasks that
 </span>
 <span data-rw-start="194.64" data-rw-transcript-version="2">
 your business actually needs are going
 </span>
 <span data-rw-start="196.8" data-rw-transcript-version="2">
 to blow right past that ceiling. And
 </span>
 <span data-rw-start="199.04" data-rw-transcript-version="2">
 this is where Sika's background becomes
 </span>
 <span data-rw-start="201.04" data-rw-transcript-version="2">
 a factor. This isn't an outsider's
 </span>
 <span data-rw-start="203.36" data-rw-transcript-version="2">
 perspective. Remember, he studied under
 </span>
 <span data-rw-start="205.28" data-rw-transcript-version="2">
 John McCarthy, the man who literally
 </span>
 <span data-rw-start="207.28" data-rw-transcript-version="2">
 coined the term artificial intelligence.
 </span>
 <span data-rw-start="209.44" data-rw-transcript-version="2">
 He's bridging the gap between the
 </span>
 <span data-rw-start="211.12" data-rw-transcript-version="2">
 foundational laws of the 1960s and the
 </span>
 <span data-rw-start="214.08" data-rw-transcript-version="2">
 chaotic world of AI in 2026. He isn't
 </span>
 <span data-rw-start="217.68" data-rw-transcript-version="2">
 saying these tools are useless. Far from
 </span>
 <span data-rw-start="219.599" data-rw-transcript-version="2">
 it. He's just saying they're being
 </span>
 <span data-rw-start="221.36" data-rw-transcript-version="2">
 marketed as reasoning engines when the
 </span>
 <span data-rw-start="223.84" data-rw-transcript-version="2">
 math proves they're actually pattern
 </span>
 <span data-rw-start="225.76" data-rw-transcript-version="2">
 Mirrors. They reference the time hierarchy theorem. Again, I don't mean
 </span>
 <span data-rw-start="227.68" data-rw-transcript-version="2">
 to throw so many fancy words, but this
 </span>
</p>
<p>
 <span data-rw-start="229.68" data-rw-transcript-version="2">
 basically says that some problems
 </span>
 <span data-rw-start="231.76" data-rw-transcript-version="2">
 require a minimum number of steps. You
 </span>
 <span data-rw-start="233.36" data-rw-transcript-version="2">
 just can't shortcut them. And the
 </span>
 <span data-rw-start="235.84" data-rw-transcript-version="2">
 argument that the paper makes, if a task
 </span>
 <span data-rw-start="237.84" data-rw-transcript-version="2">
 needs more steps than the model can
 </span>
 <span data-rw-start="240" data-rw-transcript-version="2">
 perform, it will unavoidably
 </span>
 <span data-rw-start="242" data-rw-transcript-version="2">
 hallucinate. Unavoidably. And this is
 </span>
 <span data-rw-start="244.48" data-rw-transcript-version="2">
 why hallucination isn't a training
 </span>
 <span data-rw-start="246.56" data-rw-transcript-version="2">
 issue. Yes, more recent models have
 </span>
 <span data-rw-start="248.4" data-rw-transcript-version="2">
 gotten better at it, but for certain
 </span>
 <span data-rw-start="250.48" data-rw-transcript-version="2">
 problems, hallucination is the only
 </span>
 <span data-rw-start="252.159" data-rw-transcript-version="2">
 possible output. But wait, you might be
 </span>
 <span data-rw-start="256.239" data-rw-transcript-version="2">
 thinking, what about the new agentic
 </span>
 <span data-rw-start="258.16" data-rw-transcript-version="2">
 era? Tools like Manis or OpenClaw. They
 </span>
 <span data-rw-start="260.239" data-rw-transcript-version="2">
 don't just give one answer. They run
 </span>
 <span data-rw-start="262.32" data-rw-transcript-version="2">
 thousands of loops, browsing the web and
 </span>
</p>
<p>
 <span data-rw-start="264.4" data-rw-transcript-version="2">
 thinking through step by step. The tech
 </span>
 <span data-rw-start="266.72" data-rw-transcript-version="2">
 community is calling this chain of
 </span>
 <span data-rw-start="268.4" data-rw-transcript-version="2">
 thought or agentic workflows. And the
 </span>
 <span data-rw-start="270.72" data-rw-transcript-version="2">
 idea is that if a model has a ceiling,
 </span>
 <span data-rw-start="273.12" data-rw-transcript-version="2">
 just spread the problem across more
 </span>
 <span data-rw-start="274.8" data-rw-transcript-version="2">
 steps. Give it more room to work. But
 </span>
 <span data-rw-start="277.12" data-rw-transcript-version="2">
 Sika's paper argues this as a trap. And
 </span>
 <span data-rw-start="279.52" data-rw-transcript-version="2">
 here's why. If you have a fixed amount
 </span>
 <span data-rw-start="281.12" data-rw-transcript-version="2">
 of thinking power per word, giving the
 </span>
 <span data-rw-start="284.479" data-rw-transcript-version="2">
 AI more steps is like giving a writer
 </span>
 <span data-rw-start="287.28" data-rw-transcript-version="2">
 more sheets of paper. Each individual
 </span>
 <span data-rw-start="289.44" data-rw-transcript-version="2">
 sheet is still the same size. You
 </span>
 <span data-rw-start="291.199" data-rw-transcript-version="2">
 haven't made the writer smarter. You've
 </span>
 <span data-rw-start="293.28" data-rw-transcript-version="2">
 just given them more room to ramble off
 </span>
 <span data-rw-start="295.44" data-rw-transcript-version="2">
 topic. That's why you'll see an agent
 </span>
 <span data-rw-start="297.6" data-rw-transcript-version="2">
 book a flight perfectly, but then get
 </span>
 <span data-rw-start="299.919" data-rw-transcript-version="2">
 stuck in a bizarre infinite loop trying
 </span>
</p>
<p>
 <span data-rw-start="302.479" data-rw-transcript-version="2">
 to change a seat assignment. The math,
 </span>
 <span data-rw-start="304.88" data-rw-transcript-version="2">
 specifically again that time hierarchy
 </span>
 <span data-rw-start="306.96" data-rw-transcript-version="2">
 theorem, says that for complex problems,
 </span>
 <span data-rw-start="309.6" data-rw-transcript-version="2">
 errors eventually compound. The model
 </span>
 <span data-rw-start="311.84" data-rw-transcript-version="2">
 goes off track at step five, and because
 </span>
 <span data-rw-start="314.24" data-rw-transcript-version="2">
 it can't mathematically verify its own
 </span>
 <span data-rw-start="316.4" data-rw-transcript-version="2">
 logic, the whole chain eventually falls
 </span>
 <span data-rw-start="318.16" data-rw-transcript-version="2">
 apart. In the Agentic era, hallucination
 </span>
 <span data-rw-start="320.56" data-rw-transcript-version="2">
 isn't a training bug. It's a cumulative
 </span>
 <span data-rw-start="323.039" data-rw-transcript-version="2">
 mathematical certainty. Then of course
 </span>
 <span data-rw-start="325.28" data-rw-transcript-version="2">
 you might be arguing, well they can just
 </span>
 <span data-rw-start="327.36" data-rw-transcript-version="2">
 use a tool, give it a calculator. After
 </span>
 <span data-rw-start="329.199" data-rw-transcript-version="2">
 all, we wouldn't expect a human to be
 </span>
 <span data-rw-start="330.96" data-rw-transcript-version="2">
 able to calculate the traveling salesman
 </span>
 <span data-rw-start="332.24" data-rw-transcript-version="2">
 problem.
 </span>
</p>
<p>
 <span data-rw-start="332.8" data-rw-transcript-version="2">
 Problem by hand. But Sika acknowledges
 </span>
 <span data-rw-start="334.56" data-rw-transcript-version="2">
 this as well. You can build components
 </span>
 <span data-rw-start="336.479" data-rw-transcript-version="2">
 around LLMs to overcome the limits, of
 </span>
 <span data-rw-start="338.8" data-rw-transcript-version="2">
 course. And then the LLM becomes an
 </span>
 <span data-rw-start="340.72" data-rw-transcript-version="2">
 orchestrator. But notice what just
 </span>
 <span data-rw-start="342.639" data-rw-transcript-version="2">
 happened. The LLM didn't solve the
 </span>
 <span data-rw-start="345.039" data-rw-transcript-version="2">
 problem. It just handed it off to a
 </span>
 <span data-rw-start="347.44" data-rw-transcript-version="2">
 classical algorithm that could. But the
 </span>
 <span data-rw-start="349.52" data-rw-transcript-version="2">
 catch, the model still has to verify
 </span>
 <span data-rw-start="351.84" data-rw-transcript-version="2">
 that that tool worked. And if verifying
 </span>
 <span data-rw-start="354.08" data-rw-transcript-version="2">
 correctness requires more math than the
 </span>
 <span data-rw-start="356" data-rw-transcript-version="2">
 model can do, again, the agent fails in
 </span>
 <span data-rw-start="358.4" data-rw-transcript-version="2">
 unpredictable ways. Well, what about
 </span>
 <span data-rw-start="360.639" data-rw-transcript-version="2">
 those massive context windows? Gemini 3
 </span>
 <span data-rw-start="363.039" data-rw-transcript-version="2">
 Pro can see a million tokens at once.
 </span>
</p>
<p>
 <span data-rw-start="365.28" data-rw-transcript-version="2">
 Yes, that solves information access. It
 </span>
 <span data-rw-start="367.84" data-rw-transcript-version="2">
 doesn't solve the computational steps
 </span>
 <span data-rw-start="369.84" data-rw-transcript-version="2">
 per word. Having a bigger filing cabinet
 </span>
 <span data-rw-start="372.72" data-rw-transcript-version="2">
 doesn't help if you don't have the brain
 </span>
 <span data-rw-start="374.72" data-rw-transcript-version="2">
 power to process what's inside. So, what
 </span>
 <span data-rw-start="376.88" data-rw-transcript-version="2">
 does this mean for you? Now, the paper,
 </span>
 <span data-rw-start="378.56" data-rw-transcript-version="2">
 it's not saying that AI is useless.
 </span>
 <span data-rw-start="380.4" data-rw-transcript-version="2">
 Indeed, it definitely is not. I use
 </span>
 <span data-rw-start="382.8" data-rw-transcript-version="2">
 these tools every day in my business.
 </span>
 <span data-rw-start="384.479" data-rw-transcript-version="2">
 I'm sure most of the people watching
 </span>
 <span data-rw-start="386.319" data-rw-transcript-version="2">
 This do as well. For the right applications, current AI, the current
 </span>
 <span data-rw-start="388" data-rw-transcript-version="2">
 frontier models are exceptional. Writing
 </span>
 <span data-rw-start="390.319" data-rw-transcript-version="2">
 drafts, summarizing, reformatting data,
 </span>
 <span data-rw-start="392.639" data-rw-transcript-version="2">
 research, and comparison. These stay
 </span>
 <span data-rw-start="394.72" data-rw-transcript-version="2">
 under that ceiling. The problem is the
 </span>
 <span data-rw-start="396.8" data-rw-transcript-version="2">
 gap between reality and the pitch decks.
 </span>
</p>
<p>
 <span data-rw-start="399.44" data-rw-transcript-version="2">
 AI agents will autonomously run your
 </span>
 <span data-rw-start="404" data-rw-transcript-version="2">
 business is a lie. The math just doesn't
 </span>
 <span data-rw-start="406.88" data-rw-transcript-version="2">
 support it. To see this in action, look
 </span>
 <span data-rw-start="408.8" data-rw-transcript-version="2">
 at vending bench 2 from Anden Labs. This
 </span>
 <span data-rw-start="411.52" data-rw-transcript-version="2">
 is the 2026 gold standard for testing AI
 </span>
 <span data-rw-start="414.96" data-rw-transcript-version="2">
 agents at running a business. Models
 </span>
 <span data-rw-start="417.12" data-rw-transcript-version="2">
 like Claude Opus 4.6 Gemini 3 Pro.
 </span>
</p>
<p>
 <span data-rw-start="420" data-rw-transcript-version="2">
 They're given $500 in a year to run a
 </span>
 <span data-rw-start="422.88" data-rw-transcript-version="2">
 simulated vending machine business. And
 </span>
 <span data-rw-start="424.96" data-rw-transcript-version="2">
 on paper, the agents look like they're
 </span>
 <span data-rw-start="426.72" data-rw-transcript-version="2">
 winning. The current leader, Claude Opus
 </span>
 <span data-rw-start="428.88" data-rw-transcript-version="2">
 4.6, netted $8,000 in profit. Here's
 </span>
 <span data-rw-start="431.759" data-rw-transcript-version="2">
 that test, Vending Bench 2. Feel free to
 </span>
 <span data-rw-start="433.599" data-rw-transcript-version="2">
 look it up yourself. And here are the
 </span>
 <span data-rw-start="435.44" data-rw-transcript-version="2">
 current standings for Frontier Models.
 </span>
</p>
<p>
 <span data-rw-start="437.199" data-rw-transcript-version="2">
 We can see Claude Opus 4.6 $8,000.
 </span>
 <span data-rw-start="441.599" data-rw-transcript-version="2">
 Pretty good. But here's the actual
 </span>
 <span data-rw-start="443.44" data-rw-transcript-version="2">
 ceiling. And in labs calculated a human
 </span>
 <span data-rw-start="446.479" data-rw-transcript-version="2">
 Baseline for this exact same simulation.
 </span>
</p>
<p>
 <span data-rw-start="448.88" data-rw-transcript-version="2">
 Let me scroll down and show that to you.
 </span>
 <span data-rw-start="450.479" data-rw-transcript-version="2">
 It's a long paper here. This isn't the
 </span>
 <span data-rw-start="452.96" data-rw-transcript-version="2">
 best ever, $63,000 a year. This is a
 </span>
 <span data-rw-start="456.639" data-rw-transcript-version="2">
 human baseline and it blows the AI
 </span>
 <span data-rw-start="459.28" data-rw-transcript-version="2">
 models out of the water. The reason the
 </span>
 <span data-rw-start="461.44" data-rw-transcript-version="2">
 AI models can't make $63,000 a year is
 </span>
 <span data-rw-start="465.12" data-rw-transcript-version="2">
 because they lose coherence over a long
 </span>
 <span data-rw-start="468" data-rw-transcript-version="2">
 time frame. As a result, the frontier models,
 </span>
 <span data-rw-start="470.639" data-rw-transcript-version="2">
 the best we can make now, aren't hitting
 </span>
 <span data-rw-start="472.88" data-rw-transcript-version="2">
 even 15% of a human baseline. Over these
 </span>
 <span data-rw-start="476.639" data-rw-transcript-version="2">
 runs, we've seen agents honestly give
 </span>
 <span data-rw-start="478.72" data-rw-transcript-version="2">
 away their inventory for free due to
 </span>
 <span data-rw-start="480.72" data-rw-transcript-version="2">
 social engineering or they've even tried
 </span>
 <span data-rw-start="482.879" data-rw-transcript-version="2">
 to contact the FBI to report their own
 </span>
 <span data-rw-start="485.52" data-rw-transcript-version="2">
 $2 bank fees as fraud. And this is the
 </span>
</p>
<p>
 <span data-rw-start="489.039" data-rw-transcript-version="2">
 time hierarchy theorem in the wild. As
 </span>
 <span data-rw-start="491.199" data-rw-transcript-version="2">
 the chain of tasks gets longer, the AI's
 </span>
 <span data-rw-start="493.84" data-rw-transcript-version="2">
 ability to verify its own logic
 </span>
 <span data-rw-start="496.319" data-rw-transcript-version="2">
 collapses. It doesn't matter how smart
 </span>
 <span data-rw-start="498.4" data-rw-transcript-version="2">
 the model is. The math says that without
 </span>
 <span data-rw-start="500.479" data-rw-transcript-version="2">
 a human to reset the error rate, the
 </span>
 <span data-rw-start="502.72" data-rw-transcript-version="2">
 autonomous chain will eventually break.
 </span>
 <span data-rw-start="505.68" data-rw-transcript-version="2">
 So here's what you actually do to stay
 </span>
 <span data-rw-start="508" data-rw-transcript-version="2">
 on the winning side of this math. First,
 </span>
 <span data-rw-start="510.8" data-rw-transcript-version="2">
 Be specific about tasks. [music] Draft
 </span>
 <span data-rw-start="513.68" data-rw-transcript-version="2">
 an email using my tone and cadence that
 </span>
 <span data-rw-start="516.959" data-rw-transcript-version="2">
 works. Automate this workflow or it's going
 </span>
 <span data-rw-start="519.279" data-rw-transcript-version="2">
 to fail. Build in human verification.
 </span>
</p>
<p>
 <span data-rw-start="521.839" data-rw-transcript-version="2">
 This is a structural requirement, not an
 </span>
 <span data-rw-start="523.76" data-rw-transcript-version="2">
 option. And third, use AI for pattern
 </span>
 <span data-rw-start="526.48" data-rw-transcript-version="2">
 recognition, not logic-heavy math. But
 </span>
 <span data-rw-start="529.2" data-rw-transcript-version="2">
 here is the real tip-off. Why the
 </span>
 <span data-rw-start="531.76" data-rw-transcript-version="2">
 singularity probably isn't as close as
 </span>
 <span data-rw-start="534.16" data-rw-transcript-version="2">
 people keep saying? Because if the
 </span>
 <span data-rw-start="535.92" data-rw-transcript-version="2">
 singularity were just months away, why
 </span>
 <span data-rw-start="538.24" data-rw-transcript-version="2">
 are the smartest people in the room
 </span>
 <span data-rw-start="539.92" data-rw-transcript-version="2">
 quitting? Look at the insiders. If open
 </span>
 <span data-rw-start="541.76" data-rw-transcript-version="2">
 AI was about to hit AGI, why would
 </span>
 <span data-rw-start="544.959" data-rw-transcript-version="2">
 senior engineers be leaving to start
 </span>
 <span data-rw-start="547.519" data-rw-transcript-version="2">
 risky startups? If you knew the world
 </span>
 <span data-rw-start="549.68" data-rw-transcript-version="2">
 was about to change forever, you
 </span>
 <span data-rw-start="551.68" data-rw-transcript-version="2">
 wouldn't leave. You wouldn't leave Open
 </span>
 <span data-rw-start="553.76" data-rw-transcript-version="2">
 AI if they're on the verge of AGI. You'd
 </span>
 <span data-rw-start="555.92" data-rw-transcript-version="2">
 stay to be part of the release of a
 </span>
 <span data-rw-start="558" data-rw-transcript-version="2">
 lifetime, to be part of the equity of a
 </span>
 <span data-rw-start="559.92" data-rw-transcript-version="2">
 lifetime, unless you saw the ceiling.
 </span>
 <span data-rw-start="562.24" data-rw-transcript-version="2">
 Now, they know the next model will be
 </span>
 <span data-rw-start="563.68" data-rw-transcript-version="2">
 better, but not qualitatively different.
 </span>
 <span data-rw-start="565.68" data-rw-transcript-version="2">
 Just like ChatGPT-5, it was better than
 </span>
 <span data-rw-start="568.16" data-rw-transcript-version="2">
 Four, but not qualitatively different.
 </span>
</p>
<p>
 <span data-rw-start="570.32" data-rw-transcript-version="2">
 They're starting companies that use AI
 </span>
 <span data-rw-start="572.16" data-rw-transcript-version="2">
 as a tool, not companies that use AI as
 </span>
 <span data-rw-start="575.279" data-rw-transcript-version="2">
 a god. The opportunity here is not
 </span>
 <span data-rw-start="577.44" data-rw-transcript-version="2">
 chasing some imaginary AGI. The
 </span>
 <span data-rw-start="580.32" data-rw-transcript-version="2">
 opportunity is an understanding exactly
 </span>
 <span data-rw-start="582.959" data-rw-transcript-version="2">
 what AI can do for you right now. The
 </span>
 <span data-rw-start="585.68" data-rw-transcript-version="2">
 ceiling is real, but there's a lot of
 </span>
 <span data-rw-start="588" data-rw-transcript-version="2">
 room underneath.
 </span>
</p>