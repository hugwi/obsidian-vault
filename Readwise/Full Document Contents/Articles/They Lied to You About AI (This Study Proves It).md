# They Lied to You About AI (This Study Proves It)

![rw-book-cover](https://i.ytimg.com/vi/AIYQp1n51ZI/sddefault.jpg)

## Metadata
- Author: [[Caleb Ulku]]
- Full Title: They Lied to You About AI (This Study Proves It)
- Category: #articles
- Summary: A math proof shows AI can't fully do complex tasks because of fixed limits in how it processes information. Current AI tools are good for simple work but can't run businesses alone or solve big problems without human help. The hype about AI being super smart soon is wrong; real progress means knowing what AI can do now, not chasing impossible goals.
- URL: https://www.youtube.com/watch?v=AIYQp1n51ZI

## Full Document
A father and son just mathematicallyproved that an AI agent will never dowhat Silicon Valley is promising. Notprobably won't. Not might havelimitations. They've mathematicallyproved they use computational complextheory that's been settled since the1960s. And this isn't coming from someAI doomer clickbait journalist. This iscoming from Vishel Sika, former CEO ofInfosys, board member at Oracle and BMW.

He's a Stanford PhD who literallystudied under John McCarthy. He's theguy who coined the term artificialintelligence. He and his son justpublished a paper that no one in AImarketing departments wants you to read,especially right now as we enter the eraof Magnus and Open Claw, the agents thatcan use your browser and click buttonsfor you. It looks like AGI has arrived,but Sika says we're actually justwatching the ceiling get higher, notdisappear. Their argument is simple.

LLMs can only perform a certain numberOf computations per response. Thatnumber is fixed. And if a task requiresmore computation than that ceilingallows, the model will either fail orhallucinate. And this isn't a maybe.

It's baked into the math. But if themath is so broken, then why are the bigplayers still promising the world? I'lltell you the devious reason why at theend of this video, but first, I want tolook at the ceiling that theydiscovered. Now, when you send a promptto chat GPT or cloud or Grock or any ofthe current frontier models, the modelwill do a fixed amount of work togenerate each word as an output. Thishappens through the self-attentionmechanism. This is, of course, verysimplified. But think of it like this.

Every word in your prompt needs to lookat every other word to understand thecontext. So if you have a thousandwords, it's a million comparisons. Athousand, a thousand. But there's no, letme think about this harder. There's noGive me more time on this one. Everytoken gets the same budget. A simplehello gets the same number of operationsas a complex physics problem. That's theceiling. It's not about better hardware.

It's about the architecture of how thesystems actually work. The paper and Ihave it here on screen if you want toread it. It uses traveling salesmanproblem as an example. To visit 20cities and figure out the shortestpossible route between those cities, youneed to check over two quintillioncombinations. An LLM physically cannotdo that math in one shot. So, what doesit do? It guesses. It pattern matches.

It gives you something that looksplausible and it's not a bug. That's thearchitecture. But how would you actuallyhandle tasks that require that level ofcomputation? Next, I'll show you whyeven verifying the answers is just asimpossible for these models. The authorsof this paper make a distinction. Doinga task versus verifying it. Now, you'dThink that the model could at leastcheck if the answer is right, even if itcan't handle the computationalcomplexity to calculate it. But no,verification often requires just as muchwork as solving the problem up front.

Every AI demo you've ever seen, it wasrunning tasks designed to stay under thenecessary complexity ceiling. They workbecause they're designed to work.

Meanwhile, the real world tasks thatyour business actually needs are goingto blow right past that ceiling. Andthis is where Sika's background becomesa factor. This isn't an outsider'sperspective. Remember, he studied underJohn McCarthy, the man who literallycoined the term artificial intelligence.He's bridging the gap between thefoundational laws of the 1960s and thechaotic world of AI in 2026. He isn'tsaying these tools are useless. Far fromit. He's just saying they're beingmarketed as reasoning engines when themath proves they're actually patternMirrors. They reference the time hierarchy theorem. Again, I don't meanto throw so many fancy words, but this

basically says that some problemsrequire a minimum number of steps. Youjust can't shortcut them. And theargument that the paper makes, if a taskneeds more steps than the model canperform, it will unavoidablyhallucinate. Unavoidably. And this iswhy hallucination isn't a trainingissue. Yes, more recent models havegotten better at it, but for certainproblems, hallucination is the onlypossible output. But wait, you might bethinking, what about the new agenticera? Tools like Manis or OpenClaw. Theydon't just give one answer. They runthousands of loops, browsing the web and

thinking through step by step. The techcommunity is calling this chain ofthought or agentic workflows. And theidea is that if a model has a ceiling,just spread the problem across moresteps. Give it more room to work. ButSika's paper argues this as a trap. Andhere's why. If you have a fixed amountof thinking power per word, giving theAI more steps is like giving a writermore sheets of paper. Each individualsheet is still the same size. Youhaven't made the writer smarter. You'vejust given them more room to ramble offtopic. That's why you'll see an agentbook a flight perfectly, but then getstuck in a bizarre infinite loop trying

to change a seat assignment. The math,specifically again that time hierarchytheorem, says that for complex problems,errors eventually compound. The modelgoes off track at step five, and becauseit can't mathematically verify its ownlogic, the whole chain eventually fallsapart. In the Agentic era, hallucinationisn't a training bug. It's a cumulativemathematical certainty. Then of courseyou might be arguing, well they can justuse a tool, give it a calculator. Afterall, we wouldn't expect a human to beable to calculate the traveling salesmanproblem.

Problem by hand. But Sika acknowledgesthis as well. You can build componentsaround LLMs to overcome the limits, ofcourse. And then the LLM becomes anorchestrator. But notice what justhappened. The LLM didn't solve theproblem. It just handed it off to aclassical algorithm that could. But thecatch, the model still has to verifythat that tool worked. And if verifyingcorrectness requires more math than themodel can do, again, the agent fails inunpredictable ways. Well, what aboutthose massive context windows? Gemini 3Pro can see a million tokens at once.

Yes, that solves information access. Itdoesn't solve the computational stepsper word. Having a bigger filing cabinetdoesn't help if you don't have the brainpower to process what's inside. So, whatdoes this mean for you? Now, the paper,it's not saying that AI is useless.Indeed, it definitely is not. I usethese tools every day in my business.I'm sure most of the people watchingThis do as well. For the right applications, current AI, the currentfrontier models are exceptional. Writingdrafts, summarizing, reformatting data,research, and comparison. These stayunder that ceiling. The problem is thegap between reality and the pitch decks.

AI agents will autonomously run yourbusiness is a lie. The math just doesn'tsupport it. To see this in action, lookat vending bench 2 from Anden Labs. Thisis the 2026 gold standard for testing AIagents at running a business. Modelslike Claude Opus 4.6 Gemini 3 Pro.

They're given $500 in a year to run asimulated vending machine business. Andon paper, the agents look like they'rewinning. The current leader, Claude Opus4.6, netted $8,000 in profit. Here'sthat test, Vending Bench 2. Feel free tolook it up yourself. And here are thecurrent standings for Frontier Models.

We can see Claude Opus 4.6 $8,000.Pretty good. But here's the actualceiling. And in labs calculated a humanBaseline for this exact same simulation.

Let me scroll down and show that to you.It's a long paper here. This isn't thebest ever, $63,000 a year. This is ahuman baseline and it blows the AImodels out of the water. The reason theAI models can't make $63,000 a year isbecause they lose coherence over a longtime frame. As a result, the frontier models,the best we can make now, aren't hittingeven 15% of a human baseline. Over theseruns, we've seen agents honestly giveaway their inventory for free due tosocial engineering or they've even triedto contact the FBI to report their own$2 bank fees as fraud. And this is the

time hierarchy theorem in the wild. Asthe chain of tasks gets longer, the AI'sability to verify its own logiccollapses. It doesn't matter how smartthe model is. The math says that withouta human to reset the error rate, theautonomous chain will eventually break.So here's what you actually do to stayon the winning side of this math. First,Be specific about tasks. [music] Draftan email using my tone and cadence thatworks. Automate this workflow or it's goingto fail. Build in human verification.

This is a structural requirement, not anoption. And third, use AI for patternrecognition, not logic-heavy math. Buthere is the real tip-off. Why thesingularity probably isn't as close aspeople keep saying? Because if thesingularity were just months away, whyare the smartest people in the roomquitting? Look at the insiders. If openAI was about to hit AGI, why wouldsenior engineers be leaving to startrisky startups? If you knew the worldwas about to change forever, youwouldn't leave. You wouldn't leave OpenAI if they're on the verge of AGI. You'dstay to be part of the release of alifetime, to be part of the equity of alifetime, unless you saw the ceiling.Now, they know the next model will bebetter, but not qualitatively different.Just like ChatGPT-5, it was better thanFour, but not qualitatively different.

They're starting companies that use AIas a tool, not companies that use AI asa god. The opportunity here is notchasing some imaginary AGI. Theopportunity is an understanding exactlywhat AI can do for you right now. Theceiling is real, but there's a lot ofroom underneath.
