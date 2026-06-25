---
categories:
  - "[[Resources]]"
domain: engineering
title: "Building AI governance while building AI"
source: "https://governance.aicareer.pro/blog/building-ai-governance-while-building-ai"
author: "James Kavanagh"
published: 2026-04-02
created: 2026-04-18
description: "Real AI governance needs both practitioner capability and organisational"
tags:
  - to-process
  - agent-tools
---

Real AI governance needs both practitioner capability and organisational capacity, built together through messy practice. Stop waiting. Start building, start learning, and design your governance to evolve alongside the systems it is meant to govern.


![](https://lwfiles.mycourse.app/67fdc90af2a148ec2d172552-public/b6648d18c0d2c86458b6f391f02bbfd1.jpg) Governance Leadership 
### In 1932, there was an iconic photo taken of eleven ironworkers eating lunch on a bare steel beam eight hundred and fifty feet above Manhattan. No harnesses, no nets, no guardrails. Just men, steel, and air..


People look at that photograph now and see recklessness. But I think that misreads the history. Those men weren't ignoring safety. Safety, as we understand it today, didn't even exist. And it hadn't been invented, because it just couldn't be invented in the abstract. It had to be built alongside the thing it was protecting, by the people who were building.


Nobody sat in an office in 1925 and wrote a comprehensive safety framework for skyscraper construction. They didn't pretend they knew enough to write Skyscraper Safety Act. The knowledge simply didn't exist to write one. You could not know what would kill a man at eight hundred feet until men were working at eight hundred feet. The wind loads, the fatigue patterns, the way wet steel behaved underfoot, the hour of the afternoon when concentration failed, the foreman's judgment about when to pull a crew off the beam in advance of coming weather. None of that could be modelled in advance. It emerged through the work itself.


If you read my articles regularly, you probably know I look for safety lessons from disaster. I'm forever curious about the worst can teach us. And though the somewhat absurd cover of TIME magazine this year portraying the CEOs of AI companies as modern-day pioneers at height fell flat, I still see a lesson in this picture that's worth exploring.


You see in New York, safety practices grew with the skyline. Every floor taught something. Rivet gangs developed hand signals and staging practices that kept them alive. Foremen learned which conditions to refuse. Engineers learned to over-build where they couldn't yet calculate. They didn't know enough about steel under intense load, wind shear and earthquake effects. Jim Rasenberger's High Steel (1) tells this history in full: the Brooklyn Bridge, the Quebec Bridge, the Empire State Building, the World Trade Center. What comes through is that the craft and its dangers were never separate stories. They were the same story, written one building at a time.


The formal codes came later. Occupational health and safety in the form of OSHA in the US didn't exist until 1970. But the absence of formal regulation did not mean the absence of governance. It meant that governance was local, practical, and evolving. It lived in the practices that kept people alive, and it improved every time something went wrong and someone paid attention to why.


This is the history that matters for anyone building AI governance today. Not because the analogy is perfect, but because it dismantles the most common excuse for inaction: we don't know enough yet to govern properly. The ironworkers did not know enough either. They built anyway, and they built safety into the work as they learned what safety required. The two things grew together. They had to. There just wasn't any other way.


Let me be clear about what I'm saying with this analogy. I'll never argue that we should build AI recklessly and wait for the accidents to teach us the rules. The construction industry paid for its lessons in lives. We do not need to repeat that mistake and we should not want to. My point is different, and more pragmatic: we don't yet know what the right governance structures, policies, and controls look like. Nobody does. We can't wait until we have perfect answers before we start governing, because those answers won't arrive in a meeting room or a nicely structured Act or Standard. The EU AI Act will not define the real practices for how to build and govern safe, secure AI. Nor will some tool or technology, nor will a top-tier consulting firm, no matter how much you pay them


They will emerge from the practice of governing real systems, with real consequences, while the technology is being built. And the alternative isn't careful preparation. The alternative is doing nothing while the building goes up without you. Or worse, pretending you already have the answers. If we act as though we know what perfect AI governance looks like before we have built and governed real systems, we don't get safety. We get theatre. Elaborate frameworks that look rigorous on paper and govern nothing in practice. That is not a neutral outcome. It is actively harmful, because it creates the illusion of oversight where none exists, and it gives organisations permission to stop thinking.


In my last article, I argued that the biggest risk in AI governance is waiting too long to begin. That the chasm between talking about governance and actually doing it is widening. And that organisations need to stop treating governance as a project to be scoped and start building it as a permanent organisational capability.


So suppose you're an organisation using or building AI and you’ve taken that on board. You’ve decided to start actively governing. You have enough of a mandate to begin building something real. Now what?


The truth is that much of the guidance out there describes what governance should look like when it’s finished. That’s like describing a house to someone who needs to learn carpentry. What I think practitioners need is the sequence of construction and an understanding of the craft. What to build first, how to make it functional, and critically, how to design governance that learns and improves rather than calcifying into another layer of bureaucracy.


### Start with what you can see


You can't govern what you can't see. This is obvious, but it’s also a reason many organisations stall before they start. They interpret “you need an AI inventory” as “you need a comprehensive, validated, categorised register of every AI system in the organisation before you can do anything else.” So they ask, what should the register look like, what fields, what process for intake, which external consultant can come in and design that for us, what tool should we buy for the inventory? That’s the perfection trap again, and it will keep you stuck for months.


In my opinion, here’s what you actually need to start: a rough map of what AI exists in your organisation and where the most consequential decisions are being made. Talk to your business leads, your product managers, your data science teams. Ask three questions. What AI systems do you have in production or near production? What’s the most consequential thing each of them does? What worries you about them?


You'll get an incomplete picture. That’s fine. Put it in a spreadsheet. Don’t agonise over taxonomy or classification schemes. You’re mapping the territory, not surveying it to centimetre accuracy. I’ve written a detailed guide on building your AI system inventory (2, 3), but the first version doesn’t need to be detailed. It needs to exist.


What this rough inventory gives you is the ability to make a judgment call: of everything we’ve got, which systems could cause the most harm if they went wrong? Harm to customers, to vulnerable people, to the business, to your regulatory standing. Those are your starting points. You don’t need to govern everything at once. You just need to start governing the things that matter most, first, and expand from there.


Your inventory is a living document. It will grow and mature as your governance matures. Every time you discover a new AI system you didn’t know about (and you will, frequently), that’s your governance working. The inventory isn’t just a register. It’s a mechanism for maintaining visibility into a landscape that’s constantly changing.


### Build capacity, not bureaucracy


AI governance capacity has two components that are often confused. The organisation provides capacity: mandate, resources, structures, authority. Practitioners provide capability: the skills, the tools knowledge, the judgment to do the actual work of governance. You need both, and they reinforce each other in important ways.


An organisation can have all the capacity in the world. Executive sponsorship, a governance committee, budget, reporting lines. But if the people doing the work can’t actually assess AI risks, evaluate model behaviour, engage engineers in meaningful technical conversations, or design effective controls, you get governance theatre. The structures look impressive. The outcomes are hollow.


The reverse is equally true. I’ve seen brilliant practitioners with deep expertise in AI safety and governance achieve precisely nothing because the organisation gave them no authority, no budget, and no seat at the table where decisions are actually made. They produce excellent analysis that nobody reads and thoughtful recommendations that nobody follows. Honestly, they just burn out and leave if the situation doesn't change.


So you need both. Here’s what I think that looks like in practice.


Start with a small core. You don't need a dedicated AI governance team of five people to begin. You need one or two people with the right combination of skills: enough technical literacy to understand AI systems, enough risk thinking to assess what could go wrong, and enough organisational credibility to be taken seriously by both engineers and executives. In smaller organisations, this might be one person wearing multiple hats. That’s fine. The first AI governance lead at most companies I’ve worked with started as a single person with a mandate and a spreadsheet.


You build a network, not a silo. I don't believe governance can function effectively in a fast moving situation like AI, if it sits outside development and reviews things after the fact. That model is too slow, too adversarial, and too disconnected from the reality of how AI systems are actually built. You need people across the organisation, in engineering, legal, product, risk, and compliance, who understand their governance responsibilities and contribute to the work. This is a distributed capability, not a centralised department. The small core team orchestrates. The network does much of the work embedded in their own functions.


Then be thoughtful about tools, but don’t let tool selection become another reason to delay. Tools are enablers, not solutions. They help you automate the routine parts of governance, track what needs tracking, and generate the evidence that your governance is functioning. There are good open-source options and good commercial platforms. But the single biggest mistake I see organisations make with governance tooling is buying a platform before they understand their governance needs (and you can't understand them until you start doing the work). You end up configuring a tool to match a process you haven’t designed yet, and then blaming the tool when governance doesn’t work. Understand what you’re trying to do first. Select tools to support it. Not the other way around.


Capability builds through practice, not study. People learn to do governance by doing governance. Formal training and certifications have their place, and I’d always encourage practitioners to build their knowledge base. But the real learning happens when you assess your first AI system, run your first risk triage, navigate your first difficult conversation with an engineering team about a model that isn’t ready for production. Start the work. The capability develops as you go.


### Create mechanisms to make your policies real


Policies describe intent, they're necessary communication. Mechanisms produce outcomes. If you want governance that actually works, you build mechanisms.


I’ve written about this at length (4) reflecting Jeff Bezos’s observation that good intentions never work, you need good mechanisms to make anything happen. A mechanism is a closed-loop system. It senses something. It triggers a decision. The decision leads to an action. The action produces an outcome. And the outcome feeds back into the system so it can learn and adjust. That feedback loop is not a phase that comes later. It is not something you add once the mechanism is “mature.” It is part of the mechanism from the moment you design it. This is the single most important idea in adaptive governance: you build the mechanism and its feedback loop as one thing.


I teach all about this in our courses on our practitioner track (course 3 is all about mechanism design). So let me borrow a few examples from that course to make this concrete. Here's four governance mechanisms that every organisation governing AI needs in some form.


#### Risk triage


A process triggered by specific events: a new AI system is proposed, a model is retrained on new data, a data source changes, a performance threshold is breached, a new regulation takes effect. Each trigger initiates a structured assessment. How consequential is this system? What could go wrong? What controls exist? What’s missing? The output is a risk classification and a set of required actions proportionate to the risk level.


The feedback loop is all about what gets tracked and what gets triaged, what risk levels are assigned, how long triage takes, and what actions result. If you’re triaging fifty systems and none are assessed as high risk, something is wrong with your assessment criteria. If triage is taking three weeks and blocking deployments, your process is too heavy. If you’re finding systems in production that never went through triage, your triggers aren’t catching everything. Each of these signals tells you something about your mechanism and points to how it needs to adapt.


#### Escalation pathways


Defined routes for specific signals to reach people with authority to act. Bias detected in a production model: who is told, within what timeframe, and what are they authorised to do? A pattern of customer complaints about an AI-powered service: where does that signal go, and what happens when it arrives? A regulatory inquiry about a specific AI system: who owns the response?


This sounds basic, but most organisations cannot answer these questions clearly. They have general incident management processes that weren’t designed for AI-specific issues. When something goes wrong, people improvise. Sometimes the improvisation works. Often it doesn’t, and critical time is lost while people figure out who should be in the room.


The feedback loop: track what gets escalated, how quickly it’s resolved, and what changes as a result. An escalation pathway that catches issues but never leads to systemic changes is just firefighting. You want to see patterns in your escalation data that feed back into better controls, better design, better risk triage upstream.


#### Review processes


Structured reviews of AI systems that examine behaviour and outcomes, not just documentation completeness. This is where governance theatre can be the most visible and most corrosive. A review that asks “is the model card filled in?” is checking paperwork. A review that asks “what happened when we tested this model on edge cases, and how did it perform across different demographic groups, and what do the monitoring data from the last quarter tell us about drift?” is actually governing.


The feedback loop: are reviews finding issues? Are those issues being resolved before they reach production? Are the same types of issues recurring, suggesting a systemic problem in development practices? If your reviews never find anything wrong, that’s not a sign of excellence. It’s a sign your reviews aren’t looking hard enough.


#### Incident response


A process for when things go wrong with an AI system in production. Not just containment and remediation, but a structured approach to understanding what happened, why existing controls didn’t prevent it, and what needs to change to prevent recurrence. This is where governance learns its most painful and most valuable lessons.


The feedback loop: every incident should produce changes. Not just to the specific system that failed, but to the governance mechanisms that should have caught the problem earlier. If an AI system causes harm and your post-incident review concludes that all processes were followed correctly, you have a process problem, not a success story. Something in your governance design needs to change.


Notice the pattern across all four mechanisms. Each one senses something, triggers action, produces outcomes, and feeds back. None of them are “build it and forget it” systems. None of them are designed as elegant processes or workflows at the outset. Every one is measured, and they use those measurements to learn. And that learning is what makes governance adaptive rather than static. You don’t create perfection and then monitor it. You create something functional and then improve it continuously based on what it tells you about itself.


### Culture makes or breaks governance


You can design perfect mechanisms and they will still fail if people don’t trust them. I’ve written a full article on why AI governance has a culture problem, and I won’t repeat it all here (5). But the short version matters for anyone building governance in practice.


If engineers see governance as a gate that slows them down, they will route around it. They’ll find ways to deploy without triggering the review process. They’ll fill in documentation with the minimum required to pass the checklist. They’ll treat governance as something to be endured rather than something that helps them build better systems. And honestly, if your governance is just a gate that slows things down without adding value, they’re not wrong to resent it. If you've designed your governance around compliance processes in the EU AI Act, don't be surprised when your engineers don't return your calls.


If risk managers don’t understand the technology, they’ll produce risk assessments that miss the actual dangers and flag imaginary ones. Engineers will lose respect for the process, and rightly so. If people don’t feel safe reporting problems, your feedback loops go silent. The mechanism might exist on paper, but no signal flows through it.


And contrary to management consulting firms, you don’t build culture with a culture program. You build it through how you do everything else. When you involve users and engineers in designing governance mechanisms, that’s culture building. They feel ownership. The mechanisms are better because they reflect operational reality. When someone flags a concern and you act on it, visibly and promptly, that’s culture building. It signals that the feedback loop is real, that speaking up matters. When leadership talks about governance as a strategic capability rather than a compliance cost, that’s culture building too. It gives people permission to invest their best thinking in governance rather than treating it as overhead.


The aviation industry learned this lesson the hard way after Tenerife. After the worst aviation disaster in history and 583 people lost their lives (5), they didn’t just add more rules. They built a culture where pilots could report mistakes without fear, where crews were trained to speak up regardless of seniority, where learning from normal operations became as important as investigating accidents. AI governance needs the same kind of cultural foundation. Without it, even well-designed mechanisms will underperform.


### Governance that evolves


Here is the final and perhaps most important point. Your governance system is itself a system operating in a complex, changing environment. Regulations change. Your AI portfolio changes. New technology capabilities emerge. The risk landscape shifts. Public expectations evolve. What worked six months ago might not work today. This isn’t a failure of your governance. It’s the nature of governing complex adaptive systems.


So you've got to design for evolution from the beginning. Build in explicit triggers for reassessment: a significant new regulation, a major incident (yours or someone else’s), a fundamental change in your AI portfolio such as a move into agentic AI systems, or performance data from your own mechanisms showing something isn’t working. Don’t wait for annual reviews. If a trigger fires, respond.


Make governance retrospectives a habit, not a reaction to failure. Periodically ask: what did our governance mechanisms catch this quarter? What did they miss? Where did we struggle? What surprised us? These questions generate the intelligence that feeds adaptation. Without them, governance ossifies. It becomes the static, stale set of policies and procedures that I’ve been arguing against throughout these two articles.


If you can accept, genuinely, that your governance will never be “done.”, that your plan will never be perfect, then you can make real progress. The organisations that govern AI well will not be the ones who achieved some final state of governance perfection. There's no governance nirvana. There are just organisations who have built systems that keep learning, keep adapting, and keep on functioning effectively as everything around them changes. That’s what adaptive governance means in practice.


### So start building


Let me bring this back to where we started.


AI Governance is not a six-month implementation project. You do not need a consulting engagement to write a plan and a gap analysis. You do not need a comprehensive AI inventory, a perfect risk framework, a fully staffed governance team, or regulatory certainty on standards. You do not need to procure tools. You do not need a legal brief. You do not need a board submission and approval.


You need the decision to start. The honesty to start imperfectly, and the commitment to keep learning.


Get visibility into what AI you have. Identify what matters most. Put a very small, capable team around it. Build your first mechanisms with their feedback loops built in from day one. Pay attention to culture. And design the whole thing to evolve.


You will get things wrong. Your first risk assessment process will be clunky. Your first review will take too long and miss important things. Your inventory will have gaps. That’s not failure. That’s the starting point from which your governance learns and improves.


The organisations that will govern AI well in the years ahead are not the ones with the most comprehensive documentation, the most prestigious consulting partners, or the most elaborate committee structures. They’re the ones that started, built real mechanisms, paid attention to what those mechanisms told them, and kept adapting.


Stop deliberating. Start building. You'll be glad you did.


***The biggest risk in AI governance isn’t getting it wrong. It’s waiting too long to get it started.***