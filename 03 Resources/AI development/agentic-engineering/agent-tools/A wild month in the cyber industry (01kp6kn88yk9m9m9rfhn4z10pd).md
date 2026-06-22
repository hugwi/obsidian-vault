---
title: "A wild month in the cyber industry"
source: "https://jasperinsweden.substack.com/p/a-wild-month-in-the-cyber-industry?r=73dg7u&utm_campaign=post&utm_medium=web&triedRedirect=true"
author: "Hard Tech Era"
published: 2026-04-12
created: 2026-04-14
description: "On accountability, supply chains, and why the lawsuits matter more than the"
tags:
  - to-process
  - agent-tools
---

### On accountability, supply chains, and why the lawsuits matter more than the breaches


For those of you who haven’t been deep in the cybersecurity feeds this week, things are basically melting down and I am not even really talking about Mythos yet. There were so many major supply chain attacks with blast radiuses that are genuinely hard to get your head around, most of them carried out by state actors, and the carnage has been pretty wild to watch play out in real time. The kind of week where every message in your Slack starts with “Do we have a handle on x .. and has everyone seen y” and the answer is always yes but also somehow no because there’s always more.


If that wasn’t already a lot, Anthropic then announced Mythos, and without being too dramatic about it, what they’re describing is basically a race against time. They have built a model that can find and exploit software vulnerabilities at a level that surpasses all but the most skilled humans, it has already found a whole lot of zero-days including things that survived decades of human review and millions of automated tests, and they are not releasing it publicly because they are genuinely worried about what happens when something with similar capabilities gets into the wrong hands. Which it will, eventually, because the reality that some of the more skeptical researchers are pointing out is that a lot of what Mythos can do may already be possible with smaller cheaper models that anyone can download right now. So the twelve supply chain meltdowns we watched this week might actually feel like child’s play once that capability proliferates beyond the handful of actors currently committed to deploying it responsibly. Predictions range from “manageable” to “prepare for something much worse” and honestly both feel plausible depending on which thread you’re reading.


Cue the lawsuits.


Mercor and Delve are both being litigated in civil court right now and I have mixed feelings about the Delve situation specifically, mostly because while they almost certainly knew they were offering shoddy audits the more interesting moral dimension is that their product was specifically designed to appeal to well-intentioned startups who genuinely didn’t know what good compliance looked like and couldn’t afford to find out the proper way, which means a lot of founders who were actually trying to do the right thing are now sitting on security attestations that may be entirely worthless. The liability still lands on the startups. That’s correct legally. But it’s worth holding both things at once, which is that there are plenty of startups that without question did everything right and still used Delve because Delve presented itself as the thing you were supposed to use and still by all accounts were as compliant than if they had used whatever compliance automation platform. Rant over on that one.


The Mercor story is the more important one and the one I think people will be citing for a long time. Mercor is the AI data training startup that was valued at ten billion dollars six months ago after raising a three hundred and fifty million dollar Series C, working with OpenAI, Anthropic, and Meta on some of the most sensitive intellectual property in the AI industry, which is to say the custom datasets and processes these labs use to train their models. On March 27th, attackers used stolen developer credentials to publish two malicious versions of the LiteLLM package to PyPI, which is the Python package repository that essentially the entire AI development ecosystem uses. The tainted packages were available for roughly forty minutes before being identified and removed. In those forty minutes the payload harvested environment variables, API keys, SSH keys, cloud credentials across AWS, Google Cloud and Azure, Kubernetes configurations, CI/CD secrets, and database credentials, exfiltrating everything to an attacker-controlled server. Mercor was one of thousands of companies affected. The breach exposed approximately four terabytes of data including candidate profiles, personally identifiable information, employer data, source code, and API keys belonging to some of the most valuable AI operations in the world. Five class action lawsuits landed in federal courts in California and Texas within a single week. Some in the industry described the data that was supposedly sold on the dark web as amounting to a national security event, and looking at what was in there it is not hard to see why.


The mechanism here is what matters. The attack didn’t come through Mercor’s front door. It came through a dependency they trusted, a package with forty thousand weekly downloads that had been sitting in their stack doing its job right up until the moment it didn’t. And the blast radius wasn’t contained to one company, it was the entire web of organisations that touched the same dependency, which in the case of LiteLLM means essentially anyone building seriously in the AI space. Meta paused its contracts with Mercor. OpenAI confirmed it was investigating its exposure. The company was reportedly on track for over a billion dollars in annualised revenue before this. That is not a regulatory consequence. That is the market asserting consequences directly.


The most ambitious lawsuit is the one that names defendants across the supply chain. The White and Beltran filing, Case 6:26-CV-00143-H in the Northern District of Texas, names Mercor, LiteLLM’s parent company Berrie AI, and Delve Technologies as co-defendants and frames the failure not as one company’s negligence but as a systemic failure of the trust infrastructure the AI industry depends on. That legal theory is going to get a lot sharper over time. But I’ll come back to that.


I want to talk about why the tools and more importantly the processes that exist right now were not built for this and why the way the industry has responded, which has been almost entirely focused on identity, is necessary but structurally insufficient.


At RSAC 2026 five major vendors shipped five different agent identity frameworks in the same week. CrowdStrike, Cisco, Palo Alto, Microsoft, Cato. The message was unified and clear, which is that the first step to securing AI agents is knowing who they are, and that is true, but within days two Fortune 50 incidents demonstrated exactly why identity alone fails. In both cases every identity check passed. The failures were about what the agents did, not who they were.


Identity tells you who is at the door. It doesn’t tell you what they’ll do once they’re inside and it absolutely doesn’t tell you whether the tool they just called was the legitimate version or a poisoned replica that has been sitting in a public registry for three weeks with hidden instructions embedded in the tool description that redirect agent behaviour in ways that look completely normal right up until they don’t.


I don’t want to under-emphasise identity because it is legitimately important and in order to solve the AI and agent security problem it will need to be solved, but my prediction is that identity and governance more broadly will commoditise. They are solved problems in the making, hard and expensive and genuinely important, but the kind of problems that large incumbents with existing distribution advantages will absorb into their platforms within the next eighteen to twenty-four months. Microsoft has Entra and Purview and Sentinel and Defender and they are already stitching them together. Palo Alto has Prisma AIRS 3.0 with an agentic registry and an MCP gateway. The internal governance layer is being built and it will be bundled and eventually it will be table stakes the way endpoint security is table stakes today.


What will not commoditise, what cannot be absorbed into any single vendor’s ecosystem because it requires visibility across all of them simultaneously, is cross-ecosystem forensics and AI supply chain accountability.


The reason this becomes so important comes down to something that is an inconvenient truth about how agents actually get deployed in practice today, which is that they are routinely over-permissioned and this is not laziness or negligence, it is a deliberate architectural choice because over-permissioning is what makes agents genuinely powerful. An agent contained within a single application is useful but the value proposition gets really interesting when agents are connected across tooling sets, when they can move between your CRM and your calendar and your code repository and your communication tools and your external APIs, reasoning across all of them and acting across all of them, and that is where you start to see the productivity gains that justify the investment. The problem is that in order to do this today you essentially have to grant the agent broad access upfront because you cannot always predict at deployment time which resources it will need to complete an open-ended reasoning task, so developers err on the side of more access rather than less, and you end up with agents that have write access to systems they only needed to read, and credentials that grant far more than the task requires, and nobody has a complete picture of what any given agent is actually permitted to do across the full stack it touches because that permission set is distributed across five different platforms each with their own access controls and none of them talking to each other.


This creates two compounding problems and the combination of them is what makes the current moment genuinely dangerous. The first is that over-permissioned agents massively expand the blast radius of any compromise, whether that compromise comes from a prompt injection, a poisoned tool description, a supply chain attack on a dependency, or just an agent reasoning its way to an action that nobody authorised but nobody explicitly prohibited either. The second is that when something does go wrong you cannot reconstruct what happened because the action chain crosses multiple platforms and each platform only has its own slice of the story and there is no single place where the full sequence from initial prompt to final action has ever been assembled. Accountability to put it blunt, is lacking. Mercor brought in a team of third-party forensic experts because this reconstruction was such a significant challenge. A human SOC analyst trying to understand what happened after an incident involving an agent that touched Salesforce and Slack and GitHub and three external APIs is not looking at a stack trace, they are trying to manually reconstruct a decision chain across six different audit logs in six different formats while the attacker is long gone and the litigation clock is already running.


That is the gap that internal governance platforms cannot close regardless of how well-funded or well-designed they are, because the gap is not inside any single organisation’s perimeter, it is in the spaces between organisations, between tools, between the components of an AI supply chain that no single vendor controls and no single platform can see. The forensic layer that matters is the one that works across all of them simultaneously and produces an accountability record that is continuous rather than assembled retrospectively, and that is attributable at the level of granularity a court will eventually require.


The Mercor breach is not a conventional data breach story even though it looks like one from the outside. It is a preview of an entirely new category of incident, which is what happens when a compromised AI supply chain dependency takes down not one company but a category of companies that all trusted the same component, and where the evidence trail needed to understand what happened, attribute it, and assign liability crosses multiple organisational boundaries in ways that no single vendor’s governance tooling can reconstruct.


The traditional controls that were built for static software supply chains, signed code and scanned dependencies and trusted repositories, are structurally inadequate for AI supply chains because AI supply chains extend into runtime in ways that software supply chains never did. When your agent connects to an MCP server it is not importing a library that you can inspect at build time. It is importing instructions that will be interpreted by a language model at runtime, and those instructions can change, and the server can be poisoned, and the tool description can contain hidden directives that redirect the agent’s behaviour, and none of this will appear in any SBOM or identity log or governance dashboard that any of the platforms shipping at RSAC were talking about.


What is needed is a continuously maintained AI supply chain registry, not a snapshot, not a compliance artefact produced at the end of a build and filed in a digital drawer, but a living record of every AI component in the chain, agents and models and MCP servers and LLM providers and tool dependencies, continuously monitored, with the forensic depth to reconstruct what happened across organisational boundaries when something goes wrong.


Think about what it would mean to bring a contractor into your organisation without a contract, without defined scope, without any accountability framework for what they were permitted to do or not do, without any record of what they actually did while they were there. No onboarding. No defined responsibilities. No audit trail. Nobody would do this. The liability exposure alone would be disqualifying and every legal team, every halfway serious HR function would shut it down immediately. And yet this is exactly what is happening with AI agents today, at scale, across the enterprise, with broad permissions and no contracts and no continuous record of what they did or who sanctioned it.


The contractor analogy is not a metaphor. It is the actual structure of the problem. Agents are workers. They access systems, they make decisions, they take actions with real consequences, they touch data that has regulatory and contractual obligations attached to it. The accountability frameworks that govern human workers, the contracts, the defined scope, the audit trails, the liability assignment when something goes wrong, none of that infrastructure exists yet for agents and the industry has been moving fast enough that most organisations have not noticed the gap until something like Mercor makes it impossible to ignore.


Who is liable when something fails? Can you prove that you knew what was in your supply chain, that you were monitoring it continuously rather than auditing it periodically, and that when something deviated you had the forensic record to say exactly what happened? The organisations that can answer that question are in a fundamentally different legal position than those that cannot.


Regulation will not catch up. This is not a pessimistic take, it is just an accurate one based on the pace of change. Emerging frameworks like AIUC-1 are trying to address these problems and making a real effort to put strenuous tests on organisations by implementing quarterly adversarial testing requirements that are sharper than most frameworks. These are real forcing functions and I am not dismissing them. But the pace of AI capability development is faster than any regulatory body can track and the attack surface is expanding in ways that the frameworks being written today will not anticipate.


What will actually drive accountability is not a compliance checkbox. It is customers demanding proof and litigating when they don’t get it, and this ties directly to revenue. The forcing function that most people in this space are not talking about honestly enough is not regulation and it is not audits. I want to be careful here because I am not dismissing regulation, DORA is live enforcement and it is genuinely moving the needle in European financial services, the EU AI Act is real, and these are all meaningful forcing functions that I think about every day in the context of what I am building. But regulation alone has never been what actually changes enterprise behaviour at speed and if you are waiting for a compliance deadline to be the thing that forces your hand on AI supply chain accountability you are already behind the curve.


Look at Mercor.


Mercor was not taken down by a regulator. Five class action complaints in one week. The White and Beltran filing does not just name Mercor, it names LiteLLM and Delve across the supply chain and argues that the entire trust infrastructure failed. That is not a regulatory action. That is the market asserting consequences directly and the consequences are immediate, they are financial, they are reputational, and they land before any regulator has had time to open an investigation.


Revenue, choice, and customer churn are what will actually drive change and Mercor is the clearest example yet of how that mechanism works. The moment the breach became public, Meta paused its contracts. OpenAI confirmed it was investigating. Other model labs began quietly reviewing their relationships. The company was reportedly on track for over a billion dollars in annualised revenue before this. The commercial consequence of a trust infrastructure failure at this scale is not a fine paid to a regulator on a two year timeline, it is customers reassessing whether the accountability evidence they need actually exists and making procurement decisions accordingly, right now, this week, while the litigation is still being filed.


The White and Beltran filing, the most ambitious of the five cases, frames the failure as a systemic failure of trust infrastructure across a supply chain, names defendants at multiple points in that chain, and argues that each of them had an obligation to the people whose data ultimately ended up in a dark web auction. That legal theory is going to get sharper and broader as more incidents follow the same pattern. The question will not just be whether you had a security programme. It will be whether you had continuous accountability for the AI components in your supply chain, whether your contracts were demonstrably operationalised, what agents were permitted to do and under what conditions, and whether you have the forensic record to prove it.


Enterprise procurement has already started moving. Security questionnaires that used to ask whether you had a policy are now asking whether you can demonstrate continuous monitoring. Compliance certifications that used to satisfy procurement teams are getting scrutinised in ways they never were before, partly because of exactly what happened with Delve and partly because the people signing these contracts have started to understand that a document describing what good looks like is not the same thing as evidence that you are actually doing it. The buyers who are most sophisticated about this, which tends to mean the most regulated and the most valuable as customers, are beginning to treat the inability to produce continuous accountability evidence as a commercial disqualifier rather than just a risk flag. That is a revenue conversation, not a compliance conversation, and it is happening right now in procurement cycles across financial services and healthcare and any other sector where the regulatory environment has started to bite.


Customer churn is the sharper edge. Once you have a customer in a regulated environment who has built procurement criteria around continuous accountability evidence, losing that capability or failing to maintain it becomes a reason to leave that has nothing to do with product features. The customers who matter most are going to start treating continuous AI supply chain accountability the same way they treat data residency today, which is as a non-negotiable baseline rather than a differentiating feature, and the companies that figure this out early do not just reduce their liability exposure, they shorten their sales cycles, reduce the friction in renewals, and build a category of customer relationship that is structurally harder to disrupt.


Where I think this goes longer term is that the compliance artefact model dies entirely. Not gradually, not through regulatory mandate, but because the market makes it obsolete. The idea that you produce a document once a year that describes the state of your security posture at a point in time and that document is treated as meaningful evidence of anything is already starting to look absurd to the more sophisticated buyers and within a few years it will look absurd to everyone. What replaces it is a continuous data stream. Your accountability record is not something you produce before an audit, it is something that exists and updates in real time and the audit is just a query against it. A customer does not ask you to fill out a security questionnaire, they request a time-stamped export from your accountability record for the period they care about. A regulator does not ask you to demonstrate continuous monitoring, they pull the log. A court does not ask whether you had a programme, they ask for the forensic record of what the programme actually captured and when.


This is already how the most mature parts of financial services think about transaction records and it is the direction that AI governance is heading whether the incumbents building compliance automation platforms are ready for it or not. Periodic audits do not go away entirely but they become what they probably should always have been, which is a structured review of a data stream that already exists rather than a scramble to assemble evidence that the data stream was never capturing in the first place.


The practical implication is that trust between enterprises and their AI supply chains & agent actions will increasingly be mediated not by certifications or questionnaires but by live data access, where a customer can request a read against your accountability record for a defined time window and the record either supports the claim you are making or it does not, with no room for interpretation and no lag between what happened and what can be verified.


The companies that relied on Delve certifications thought they had proof. They had a document that described what proof would look like if it existed. The legal system is now in the process of deciding whether that distinction matters and based on the White and Beltran theory the answer is going to be yes, it matters enormously, and the gap between a compliance snapshot and a continuous accountability record is going to be one of the most consequential distinctions in enterprise AI over the next few years. Not because regulators required it. Because customers demanded it and courts enforced it.


My thesis has always been that contracts will be king and that they will be used and audited against. I saw the early beginnings of this when I was working in regulated industries and as the dysfuncion debate of how to regulate or oversee AI became more obvious, it was also becoming more obvious that real time data and operationalized contracts would become central. I expected it to take longer. April 2026 moved faster than I thought it would.


### Ready for more?


Subscribe