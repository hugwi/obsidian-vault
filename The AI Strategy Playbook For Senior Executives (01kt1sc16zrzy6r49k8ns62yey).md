---
categories:
  - "[[Resources]]"
domain: engineering
title: "The AI Strategy Playbook For Senior Executives"
source: "https://getdx.com/uploads/ai-strategy-playbook.pdf"
author: "Unknown"
published: 2025-10-28
created: 2026-06-01
description: ""
tags:
  - to-process
  - agent-tools
---

![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/jJh8Li3f4Jz8Uxj0zO5LoefviAtdEE8dUxwJE7ft0gI-_pa_qyzhQEH.jpeg)




![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/EZ2j-6TJZ8QBmqVzdX3M-rS_i59LEudEO4G1k9kusLw-_pa_qQtaSUT.jpeg)



# 
 The AI strategy


# 
 playbook for senior executives



![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/qOHCReP0ZydzdhCVj4SwCsylQZHipbJWDaN3OZzxBZA-_pa_xf5vOem.jpeg)



# 
 Table of contents



[Executive Summary](#page-2-0) 
 iii
 


#### 
[Introduction: The uneven impact of GenAI on software development](#page-3-0) 
 4





* 1.1
 [Quantifiable impacts exist in speed and quality on average](#page-3-0) 
 4
* 1.2
 [The reality of GenAI shows variance and volatility](#page-4-0) 
 5
* 1.3
 [The imperatives for leaders who want to stay ahead of the curve](#page-5-0) 
 6


#### 
[Setting organizational context and ensuring trust](#page-6-0) 
 7




| 
 2.1
  | 
 Lessons from Google's Project Aristotle
  | 
 7
  |
| --- | --- | --- |
| 
 2.2
  | 
 Strategies for framing AI as a force multiplier
  | 
 7
  |
|  | 
 Building a strategic measurement framework
  | 
 8
  |
| 
 3.1
  | 
 Collect AI data using a mix of methods
  | 
 8
  |
| 
 3.2
  | 
 The DX AI Measurement Framework
  | 
 9
  |
|  | 
 Focus on security, risk reduction and trust from the beginning
  | 
 10
  |
| 
 4.1
  | 
 Human oversight, verification, and prompt optimization
  | 
 10
  |
| 
 4.2
  | 
 Managing and manipulating determinism
  | 
 10
  |
| 
 R
  | 
 oot your initiatives in employee success
  | 
 11
  |




| 
 5.2
  | 
 Establish prompt libraries and internal AI guilds
  | 
 11
  |
| --- | --- | --- |
| 
 U
  | 
 nblock usage to drive organization
 
 wide adoption
  | 
 12
  |
| 
 6.1
  | 
 Creatively overcome organizational constraints
  | 
 12
  |
| 
 6.2
  | 
 Clear the runways for adoption
  | 
 12
  |
|  | 
 Integration Across the S
 
 DLC
  | 
 13
  |
| 
 7.1
  | 
 Thinking beyond code generation
  | 
 13
  |
| 
 7.2
  | 
 Industry
 
 established use cases
  | 
 13
  |
| 
 7.3
  | 
 Morgan Stanley Legacy code refactoring
  | 
 13
  |
| 
 7.4
  | 
 Faire Automated code review
  | 
 13
  |
| 
 7.5
  | 
 Canva PRD generation
  | 
 14
  |



 7.6
 [Spotify Incident management](#page-13-0) 
 14
 



 7.7
 [Zapier Administrative Automation](#page-13-0) 
 14
 


#### 
[Start today: A timeline for AI implementation](#page-14-0) 
 15



 8.1
 [Leading the AI](#page-16-0) 
 native future 17
 


# 


 The AI strategy playbook for senior executives



 Justin Reock, Deputy CTO at DX
 



 GenAI represents the next inflection point in the SDLC, presenting a foundational shift in how we design, build, test, and maintain software. Yet, as with any transformational technology, its impact is uneven. Some organizations are realizing enormous gains in developer velocity, quality, and satisfaction; others are struggling to translate early excitement into measurable outcomes.
 



 For senior engineering leaders, this is an active imperative to lead, a strategic challenge to navigate, and a new opportunity to unlock higher levels of productivity, quality, and innovation within your organization.
 



 Success will not come from simply "turning on" AI tools. It demands intentional leadership. The winners are building cultures of enablement, data-driven measurement, and governed experimentation that treat AI as a force multiplier, not a threat.
 



 This guide distills research from DX, DORA, and top engineering organizations into a guidebook for long-term AI integration. It shows leaders how to:
 









* Build trust and reduce fear of AI adoption.
* Measure real impact across utilization, quality, and cost.
* Foster education, compliance, and continuous enablement.
* Integrate AI across the full SDLC, far beyond code generation.



 The companies that will dominate are not those that merely adopt AI, but those whose leaders thoughtfully and intentionally cultivate an environment where AI augments human capability, streamlines complex workflows, and becomes a force multiplier for individual and team performance. This is your blueprint to becoming one of those leaders.
 


# 


 1. Introduction: The uneven impact of GenAI on software development


### 
 Quantifiable impacts exist in speed and quality on average



 Data from
 [DORA's research into the impact of GenAI](https://dora.dev/research/ai/gen-ai-report/) 
 in software development provides evidence of its benefits when successfully adopted. An analysis shows that a 25% increase in AI adoption within an organization is directly associated with relatively modest but positive-leaning improvements in key engineering metrics.
 



 Specifically, this level of adoption correlates with a:
 


#### 
 7.5% increase in documentation quality





* 3.4% increase in code quality
* 3.1% increase in code review speed
* 1.3% increase in approval speed
* 1.8% decrease in code complexity



![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/MHe-plK2hYSwanhPRIbGMxTjmwomWAaVL2mNI-7WJr0-_pa_PqjG4tQ.jpeg)














[Further data from DX,](https://newsletter.getdx.com/p/ai-impact-on-quality-in-engineering?utm_source=aistrategyplaybook) 
 based on surveys of tens of thousands of developers, calculated with top box scoring on a Likert scale reinforces these positive albeit modest trends. When comparing AI users to non-AI users:
 





* Change confidence score: AI users score an average of 78.7, a 2.6-point gain over non-users at 76.1. This suggests developers using AI feel slightly more confident in the changes they are shipping.
* Code maintainability score: AI users score an average



![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/u_ra4xKm2KWqEUNu7fOC3UYsWu99SL7Eu9W0qWQQ9qo-_pa_c0UCGdl.jpeg)




 of 76.0, a 2.2-point gain over non-users at 73.8. This indicates that, on average, AI-assisted code is perceived as slightly easier to maintain.
 



 Change failure rate: AI users experience a slightly lower change failure rate of 3.93% compared to 4.04% for non-users, a reduction of 0.11%.
 


### 
 The reality of GenAI shows variance and volatility



 While the average gains are positive, they mask a much more dramatic and important reality: industry averages hide the big picture. When the data is broken down on a
 



 per-company basis, the variance in impact is enormous. For every company seeing a 20-point jump in change confidence with AI adoption, another is seeing a 20-point drop. For every organization reducing its change failure rate, another is seeing it skyrocket. We see similar patterns when we analyze other metrics such as code maintainability and change failure rate.
 















 This proves a critical point for leadership: GenAI ROI is not evenly distributed. While many organizations are seeing positive KPI impacts, others are struggling and even seeing negative outcomes.
 



 What does this mean for you? Strategy is everything. Simply providing access to an AI tool does not guarantee success. In fact, without the right guardrails, education, and implementation, it can make things worse. The organizations succeeding with AI are not just adopting technology; they are leading a comprehensive change management process.
 


### 


 The imperatives for leaders who want to stay ahead of the curve



 Data shows that unstructured rollouts lead to inconsistent outcomes. Organizations that simply "turn on" AI tools without strategy or enablement often see confusion, reticence, and degraded code quality.
 



 As leaders, it's imperative then to focus on a range of factors, which will, when taken together, greatly increase
 



 the chances of long-term success with AI. The remainder of this guide will provide a blueprint for these imperatives, ensuring that your organization will fall into a highperforming cohort, concentrating specifically on:
 


#### 
 Setting clear organizational context on AI usage



 Frame AI adoption as a force multiplier for performance which unlocks organizational capabilities. Leaders should remind engineers that these tools are meant to augment capabilities and transcend what was possible before, not replace jobs.
 


#### 
 Measuring impact and facilitating open metrics






#### 
 discussions



 Learn how to measure GenAI impact using tools such as
 [DX's GenAI impact reporting,](https://getdx.com/ai-impact-analysis/?utm_source=aistrategyplaybook) 
 and advertise and evangelize these metrics to teams. Showcase teams with particularly good adoption and velocity improvements to drive healthy competition.
 


#### 
 Ensuring compliance and trust



 Validate AI-generated code through human oversight and verification. Ensure proper testing gates exist to limit change failures. If your culture already embraces testdriven design, then continue that practice and continue to run your battery of linting and testing against output code.
 


#### 
 Integration across the SDLC



 The biggest payoffs are rewarded to companies that think beyond code generation, and integrate across multiple areas of the SDLC, including always-on code reviews, automated incident management, refactor, and documentation.
 


#### 
 Unblocking usage



 Make sure that there are as few impediments as possible to using code assistants for the use cases called out in this document. Proactively seek ways to limit barriers to adoption, including running models on-premise and training locally on code repositories.
 


#### 
 Employee education and success



 Developers who leverage AI will outperform those who resist adoption. Remind engineers that this is an opportunity to learn about techniques that are likely to benefit them for the remainder of their careers, and provide training and time to increase their skills and understanding.
 


## 


 2. Setting organizational context and ensuring trust



 One of the greatest barriers to successful AI adoption is not technical; it is human. Fear, uncertainty, and a lack of psychological safety can cripple even the most wellfunded AI initiative. Giving engineers the ability to speak up about concerns and questions, and make mistakes without being punished or humiliated is a huge leading indicator of success.
 



 Google's landmark study on team performance, Project Aristotle, demonstrated clearly that psychological safety is the strongest predictor of team success. This insight is even more critical in the era of AI.
 



 Engineers experimenting with generative tools must feel safe to utilize this technology without fear of displacement, share mistakes, and question AI-generated output. Without that safety, innovation stalls. So, treat psychological safety as a non-optional prerequisite for success.
 







 Engineers may worry about job displacement, resent being monitored, or distrust the quality of AI-generated code. As a leader, your primary role is to address these fears head-on and create an environment built on trust and empowerment.
 


### 
 Lessons from Google's Project Aristotle



 Google's landmark study on team performance, Project Aristotle, demonstrated clearly that psychological safety is the strongest predictor of team success. This insight is even more critical in the era of AI.
 


#### 
 Engineers experimenting with generative tools must feel



 safe to utilize this technology without fear of
 



 displacement, share mistakes, and question AI-generated
 



 output. Without that safety, innovation stalls.
 


### 
 Strategies for framing AI as a force multiplier



 Executives play a critical role in framing AI adoption as an accelerant for performance, not a threat to employment. Core messaging should include:
 





* Enthusiastic, grassroots adoption: When you mandate a tool that engineers fear could devalue their skills or replace them, you are directly eroding that safety. True adoption is not about usage metrics; it is about enthusiastic, voluntary integration into daily workflows. When engineers begin to learn that this can reduce toil and solve real problems, then better engagement and adoption follow.
* Augmentation over displacement: AI is an assistant, not a replacement, and current model benchmarks such as SWEBench substantiate this reality. Though AI can provide engineers with additional capabilities, the technology has been repeatedly proven incapable of





* fully replacing human engineers.
* Transparency in monitoring: AI usage metrics are for understanding utilization and impact, not surveillance. If you'll measure AI usage or impact, share exactly what's being tracked and why. Communicate what metrics are being looked at and how it benefits developer experience.



 Encourage conversations about AI openly, in all-hands meetings, retrospectives, and skip-level meetings. Normalize questions about bias, hallucination, and overreliance. Remind your teams that developers who effectively leverage AI will outperform those who resist,
 


#### 
 and that learning these skills is an opportunity that will



 benefit them for the remainder of their careers.
 


### 


 3. Building a strategic measurement framework



 To effectively lead an AI transformation, you must be able to measure its impact. Without data, you are flying blind, unable to justify investment, identify what's working, or correct course when needed. However, even before the emergence of mainstream GenAI, productivity measurement itself has been a challenge. Traditional productivity metrics are often insufficient, and
 



 organizations struggle to know what to track. A successful strategy requires a mixed-methods approach that balances quantitative system data with qualitative, human-centered feedback.
 



 Executives must balance speed and sustainability. Common AI metrics reflect both:
 





* Velocity metrics such as PR throughput, time saved per developer, and PR cycle time.
* Quality metrics like change failure rate, code maintainability, confidence in releases, and time spent on bugs.


### 
 3.1 Collect AI data using a mix of methods



 A comprehensive measurement plan should be built on three distinct but complementary types of data collection:
 



 Telemetry metrics: This is system data pulled directly from your development stack and AI tools. It can include metrics like AI tool usage (daily/weekly active users), code suggestion acceptance rates, and the percentage of committed code that was AI-generated.
 





* Good for: Measuring the impact on raw developer output and adoption rates.
* Challenges: This data provides a limited and possibly inaccurate insight. High acceptance rates, for example, don't tell you if the code was actually useful or if it had to be heavily refactored. Furthermore, useful suggestions may have been copied and pasted or even just used for guidance without a developer clicking "Accept" in the IDE. It tells part of the story, but never the whole story.



 Self-reported data: These are regular (e.g., quarterly) surveys that capture trends in the developer experience that system data cannot. They are essential for measuring developer satisfaction, perceived productivity, confidence in changes, and the maintainability of code.
 





* Good For: Measuring adoption, satisfaction, and perceived productivity gains.
* Challenges: Surveys can suffer from low participation rates and can only be run periodically, offering a snapshot in time rather than a continuous view.



 Experience sampling: This powerful technique involves
 



 gathering targeted, in-the-moment feedback by asking brief questions during key workflows. For example, after a developer merges a pull request, a bot could ask, "Did you use an AI assistant for this PR?" followed by, "On a scale of 1-5, how much time did it save you?"
 





* Good For: Quantifying ROI by collecting specific timesavings data and identifying the best use cases.
* Challenges: This method can be more complex to set up and must be run over a period of time to gather meaningful data.


### 


 3.2 The DX AI Measurement Framework



 By combining these methods, you can build a comprehensive view of AI impact. The DX AI Measurement Framework provides a useful model, validated against thousands of data points, and organizing metrics across three key dimensions: Utilization, Impact, and Cost. This framework is not just theoretical; it is actively being used by
 [leading tech](https://newsletter.getdx.com/p/how-18-companies-measure-ai-impact-in-engineering?utm_source=aistrategyplaybook) 



#### 
[companies to guide their AI strategies.](https://newsletter.getdx.com/p/how-18-companies-measure-ai-impact-in-engineering?utm_source=aistrategyplaybook)



 Leading engineering organizations are not just tracking speed; they are carefully balancing short-term speed gains with longer-term maintainability and quality. Openly discussing these metrics, advertising them to teams, and evangelizing the "why" behind them is crucial for building the trust needed for success.
 



 This framework also represents a maturity curve. While most organizations will start by measuring utilization, those metrics are mostly useful for correlating that utilization to existing, validated core productivity metrics.
 



![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/2hmoOiBVqGbsyLJyXMOz3GvKtvHVEICTJX_lewsf1E8-_pa_YpqNIvr.jpeg)




 On their own, utilization metrics do not provide enough context to fully understand the impact and ROI of AI investments. Amidst all the hype surrounding AI, it's easy to forget that the point of AI is still to improve developer productivity and experience, and so our foundational productivity metrics are still what are most important to measure.
 



![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/LBz-hZCqIQmAgPAC45f_qzPeLZfYDVblaUH4ICx5a8k-_pa_ePqNOGO.jpeg)



#### 
 For more information, refer to this
 [comprehensive white](https://getdx.com/research/measuring-ai-code-assistants-and-agents/?utm_source=aistrategyplaybook) 
[paper.](https://getdx.com/research/measuring-ai-code-assistants-and-agents/?utm_source=aistrategyplaybook)




| 
 Utilization
  | 
 Impact
  | 
 Cost
  |
| --- | --- | --- |
| 
 How much are developers adopting and utilizing AI tools?
  | 
 How is AI impacting engineering productivity?
  | 
 Is our AI spend and return on investment optimal?
  |
| 
 AI tool usage (DAUs/WAUs)
 
 Percentage of PRs that are AI
 
 assisted
 
 Percentage of co
 
 mmitted code that
 
 is AI-generated
 
 asks assigned to agents \*
 
 T
  | 
 AI-dri
 
 ven time savings (dev hours/
 
 week)
 
 De
 
 veloper satisfaction
 
 D
 
 X Core 4 metrics, including:
 
 PR throughput
 
 Perceived rate of delivery
 
 Developer Experience Index (DXI)
 
 Code maintainability
 
 Change confidence
  | 
 AI s
 
 pend (both total and per
 
 developer)
 
 et time gain per developer
 
 N
 
 (time savings AI spend)
 
 Agent hourl
 
 y rate (HEH / AI spend) \*
  |




| 
 Change fail percentage
  |  |
| --- | --- |
| 
 uman-equivalent hours (HEH) of
 
 H
 
 work completed by agents \*
  |  |



 \* Metrics for autonomous AI agents
 


## 


 4. Focus on security, risk reduction and trust from the beginning



 Security and legal concerns kill many AI initiatives before they start. Engineers want to move fast, and are often compelled by senior leadership to do so, but compliance teams slam the brakes and innovation stalls. Leading organizations will balance trust in the code with model tuning and optimization that ensures compliance with
 



 organizational standards.
 


### 
 4.1 Human oversight, verification, and prompt optimization



 Every AI-generated artifact must pass through clear validation gates:
 





* Code review remains mandatory for production paths. For critical changes, this should always include human oversight.
* Testing pipelines and linting must run unchanged or



 strengthened.
 



 Bias and security training should empower engineers to detect hallucinations or data leaks.
 



 AI amplifies both speed and risk. Effective leaders ensure the organization's testing culture scales alongside AI adoption.
 



 Most enterprise AI solutions allow updates to the system prompt, the underlying instruction that shapes team-wide interactions with bots. When recurring inaccuracies appear, refine the system prompt rather than retraining from scratch. This transforms prompt management into a
 


#### 
 continuous improvement process, akin to CI/CD for AI



 behavior.
 



 Establish feedback loops within the organization which can inform admins when models misbehave, so that admins can update system prompts accordingly. Create structured channels where engineers can surface AI failures without friction:
 





* Dedicated channels for flagging bugs and biases
* Regular office hours with AI enablement teams
* Retrospectives that explicitly capture AI learnings



 For a more distributed approach, consider managing system prompt configuration markdown through source control, allowing for easy contribution to the prompt by multiple members of the engineering team.
 






### 
 4.2 Managing and manipulating determinism



 System prompts are not the only lever for improving a model's domain-specific behavior. Understanding temperature settings enables predictable outputs. Temperature settings determine whether AI outputs are consistent or creative. Low temperature (≈0.1) produces deterministic, repeatable results, which can be essential for compliance documentation and production code. High temperature (≈0.9) generates creative variation, useful for brainstorming and exploration. Understanding when to use each mode separates sophisticated AI programs from chaotic ones.
 





* Low temperature (≈0.1) yields deterministic, repeatable results.
* High temperature (≈0.9) yields creative, varied responses.



 For production-grade workflows, like compliance
 



 documentation or code generation, favor determinism.
 



 For brainstorming or ideation, embrace non-determinism.
 





 Combining human oversight, well-tuned and continuously improved system prompts, and reasonable determinism settings can help models move from chaotic sources of friction to mechanisms that enforce domain-specific semantics and compliance. Over time, this will lead to better trust in AI outputs and higher quality code in general.
 


# 
 5. Root your initiatives in


## 
 employee success



 As a leader, you have an opportunity to help your employees build a new skillset that is highly likely to follow them for the rest of their career.
 


### 
 5.1 Provide access to both education and time to learn



 Remind engineers that this is an opportunity to learn about techniques that are likely to benefit them for the remainder of their careers.
 



 AI tools evolve rapidly. Expecting engineers to self-train during sprint cycles is unrealistic. Leaders must allocate dedicated learning time, such as half-day AI deep-dives each sprint or quarterly hack weeks focused on new workflows. It's important to embrace both experimentation and creative destruction.
 



 The results that organizations hope to achieve follow a clear learning curve. Do not be surprised if early adoption of AI in the organization leads to short-term productivity or quality loss. In fact, expect this. Understand that as engineers become more skilled in understanding best practices and recognize how LLMs behave, gains will
 



![](https://readwise-assets.s3.amazonaws.com/media/reader/parsed_document_assets/381538727/mVFqdNRmeJhGCyb5ZhXLfpvZJeac6UrvM1dwm1d2Oao-_pa_wvDXtjj.jpeg)




 Circulate guides such as
 [DX's Guide to AI Assisted](https://getdx.com/guide/ai-assisted-engineering/?utm_source=aistrategyplaybook) 
[Engineering,](https://getdx.com/guide/ai-assisted-engineering/?utm_source=aistrategyplaybook) 
 which includes numerous prompting techniques and best practices based on data collected from top-performing organizations that have successfully moved through AI rollouts.
 



 Invest in workshops, training courses, and other formats of material, to ensure that multiple learning styles have access to knowledge and techniques.
 



 Remember that AI-driven workflows invite trial and error. Frame pilots as "safe-to-fail" experiments rather than "failsafe" mandates. Encourage curiosity, reward exploration, and treat misfires as learning opportunities. Promote inclusive learning by encouraging leaders and employees to share their own AI missteps or discoveries publicly.
 


### 
 5.2 Establish prompt libraries and internal AI guilds



 Encourage employees to share their best prompts for different use cases, and store them in an accessible place, such as source control. Embrace the guild model by
 



 recognizing AI champions and encourage them to share knowledge through brown-bag sessions, hackathons, and other knowledge-transfer mechanisms. If possible, rotate AI champions between teams.
 






## 


 6. Unblock usage to drive organization-wide adoption



 A successful implementation strategy focuses on systematically removing barriers to adoption while simultaneously building guardrails that protect quality and ensure compliance.
 


### 
 6.1 Creatively overcome organizational constraints



 Security and legal concerns often slow AI adoption. However, compliance should enable innovation, not block it. Your first priority should be to remove as many impediments as possible that are preventing engineers from safely and effectively using AI assistants, whether legal, technical, or otherwise.
 



 Key leadership strategies:
 



 Partner early with compliance to co-design workflows that satisfy regulatory and privacy requirements.
 



 Adopt self-hosted or private models where sensitive IP
 



 or customer data are involved.
 





* Use anonymization and synthetic data to allow experimentation without exposing real data.
* Create sandboxes that provide teams safe, compliant environments where they can experiment with AIassisted processes without fear of breaking production or violating compliance.



 By framing compliance as a collaborative enabler, not a gatekeeper, engineering leaders can accelerate safe experimentation.
 


### 
 6.2 Clear the runways for adoption



 To proliferate AI successfully:
 





* Eliminate access barriers. Provide licenses, on-prem or private model options, and pre-approved workflows.
* Automate onboarding. Offer one-click setup for AI assistants within IDEs, CI/CD tools, and chat



 environments.
 



 Train models locally. Where possible, train models on your own repositories for contextually relevant suggestions.
 



 AI adoption, especially at later phases, often stalls not from resistance but from friction. Make adoption effortless.
 


### 


 7. Integration across the SDLC


### 
 7.1 Thinking beyond code generation



 The most common use case for GenAI is code generation. While valuable, the companies achieving the greatest returns are those that think beyond the editor and integrate AI across multiple, often more impactful, areas of the SDLC.
 



 As Eli Goldratt, author of The Goal, famously stated, "An hour saved on something that isn't the bottleneck is worthless." For most organizations, writing code was never the bottleneck. Before automating, identify where developer time or throughput is most constrained. Is it PR review latency? Incident triage? Documentation upkeep?
 



 Utilize tools such as the
 [DX Workflow](https://getdx.com/workflow-analysis/?utm_source=aistrategyplaybook) 
 view to identify true bottlenecks, and then where possible and reasonable, apply AI to alleviate the constraint.
 



 Some examples include:
 



 Always-on code review agents that continuously comment on pull requests.
 



 Each use case compounds organizational leverage when connected via shared context and data.
 


### 
 7.2 Industry-established use cases


### 
 Morgan Stanley - Legacy code refactoring





* T he bottleneck: Morgan Stanley manages a vast library of legacy code. Modernizing this code requires developers to spend enormous amounts of time reverse engineering old systems to create specifications for the new ones.
* The AI solution:
 [They built "DevGen.AI,"](https://www.wsj.com/articles/how-morgan-stanley-tackled-one-of-codings-toughest-problems-4f465959) 
 an internal





* T he bottleneck: As an engineering organization scales and PRs increase, especially with AI, code review can become a significant though necessary bottleneck.
* The AI solution: Faire developed an AI agent named Fairey that triggers automatically on every GitHub pull request. The agent pulls context from surrounding code and documentation to provide always on, instantaneous PR comments and suggestions.
* Incident-management bots that correlate logs and suggest remediation.
* Refactoring assistants that analyze legacy systems and draft developer specs.
* Documentation agents that keep READMEs, wikis, and architecture diagrams current.



 solution where AI agents read the legacy code, gather additional context, and automatically generate detailed developer specs.
 



 The impact: This automation saves the company over 280,000 developer hours annually by eliminating reverse engineering.
 


### 
 Faire - Automated code review



 The impact: Fairey completes roughly 3,000 code reviews per week, freeing up senior engineers from routine checks to focus on more complex architectural issues and mentoring.
 


### 


 Canva - PRD generation





* The bottleneck: The process of translating a product idea into a developer-friendly PRD can be slow and prone to miscommunication between product managers and engineers.
* The AI solution: Canva built an internal PRD generator that allows PMs to use prompts to develop epics, user stories, and even initial design mockups. The system connects to their internal documentation, Jira, and
* The AI solution: Zapier's AI Agents team built an internal automation ecosystem where employees design and deploy lightweight AI agents that handle day-to-day coordination and operational chores. Agents now run async stand-ups, summarize team updates, automate onboarding steps like email signature creation, and integrate seamlessly with Slack for approvals, notifications, and summaries.
* The impact: The initiative has led to fewer synchronous meetings, faster onboarding (new
* Figma via MCP to create developer-friendly specs.
* The impact: The tool significantly streamlines the PRD process, improving the speed and quality of communication between product and engineering.


### 
 Spotify - Incident management





* The bottleneck: When a production incident occurs, SREs often spend critical minutes and hours correlating alerts, digging through logs, and identifying the correct runbook steps.
* The AI solution: Spotify created an internal incident management agent platform that monitors logs and correlates alerts in real-time. When an incident is



 detected, the agent automatically suggests remediation steps from relevant runbooks directly into the SREs' communication channels.
 



 The impact: The platform is currently handling 90% of all incidents at Spotify, dramatically reducing mean time to resolution (MTTR) and freeing up SREs to focus on proactive reliability work.
 


### 
 Zapier - Administrative automation



 The bottleneck: Engineers and teams at Zapier were losing valuable focus time to repetitive administrative work such as daily stand-ups, onboarding tasks,
 







 internal reporting, and routine Slack
 



 communications, all contributing to meeting
 



 overload and fragmented collaboration.
 



 engineers become productive within ~2 weeks), and an automation-focused culture. Experimentation cycles take days, not weeks, and every employee is encouraged to "build the robot" when they repeat a task.
 



 Each of these companies recognized that AI value starts where engineers can apply it safely, in high-impact workflows that align with organizational bottlenecks.
 


### 


 8. Start today: A timeline for AI implementation



 Transforming your organization into an AI-assisted engineering powerhouse is a journey, not a destination, and a strategic action plan is essential. This playbook summarizes the key actions from this guide into a concrete set of steps you can take to lead this change effectively.
 


#### 
 Phase 1: Foundation and strategy (months 1-3)


#### 
 1. Educate yourself and your leadership team:





* Share this guide and the underlying presentation with your direct reports and peers.
* Establish a shared, data-driven understanding of AI's real-world benefits and challenges.



 2. Define and communicate your vision:
 



 Articulate the "why" for AI adoption. Frame it as a strategy to augment engineers, improve product
 





* quality, and accelerate innovation, not to cut costs or replace people.
* Begin openly addressing potential fears and concerns in all-hands meetings and team forums.


#### 
 3. Establish your measurement framework:





* Determine the core metrics you will use to track Utilization, Impact, and Cost, following the DX AI Measurement Framework.
* Set up the necessary infrastructure for data collection (surveys, telemetry, experience sampling).


#### 
 4. Develop clear AI policies:



 Partner with Security, Legal, and Compliance to create
 



 clear, simple guidelines for the acceptable use of AI
 



 tools, focusing on data privacy, IP protection, and quality assurance.
 





* Communicate these policies widely so every engineer
	+ knows the rules of engagement.


### 
 Phase 2: Enablement and experimentation (months 4-9)


#### 
 1. Unblock usage and provide tools:





* Roll out access to approved AI coding assistants and tools.
* Proactively remove barriers, whether they are procurement-related, technical, or educational.


#### 
 2. Invest in education and "time to learn":



 Launch formal training programs on prompt
 



 engineering and best practices for your chosen tools.
 



 Explicitly grant engineers "permission" and time in their schedules to learn and experiment.
 


#### 
 3. Launch data-driven tool evaluations:





* Identify teams to pilot AI agents for specific, highvalue use cases beyond simple code generation (e.g., automated code review, documentation generation, test case creation).
* Focus these pilots on solving real bottlenecks identified by the teams themselves.



 4. Showcase early wins and evangelize:
 





* 
* Measure the impact of your pilots using your established framework.
* Publicly celebrate successes and showcase teams with strong adoption and velocity improvements to drive healthy, positive competition and share best practices.


### 
 Phase 3: Scale and iterate (months 10+)


#### 
 1. Scale successful use cases:





* Based on pilot results, begin a broader rollout of the most impactful AI-driven workflows across the organization.
* Provide the necessary resources and support for wider adoption.


#### 
 2. Implement continuous feedback loops:





* Use your measurement framework to continuously track the impact of AI on your core engineering KPIs.
* Use feedback from surveys, experience sampling, and direct channels to iterate on your strategy, tools, and training.


#### 
 3. Distribute and maintain an AI guide:



 Formalize your organization's best practices, use cases, and policies into a living document or internal guide that serves as a reference for all engineers.
 


#### 
 4. Look to the future:



 Stay abreast of the rapidly evolving landscape of AI in
 



 engineering, particularly the rise of autonomous software engineering agents.
 



 Continuously challenge your teams to find new bottlenecks that can be solved with intelligent automation.
 


### 


 Leading the AI-native future



 AI-assisted engineering is not a silver bullet, but it is a pivotal opportunity. The organizations that thrive will be those that combine technological enablement with cultural readiness, transparent measurement, and strong leadership messaging.
 



 For senior engineering leaders, the mandate is clear:
 





* Educate and empower teams to use AI safely.
* Measure impact through mixed methods.
* Integrate AI deeply across the SDLC.
* Communicate openly to maintain trust.
* Iterate relentlessly as the technology evolves.



 The integration of artificial intelligence into software engineering is no longer a question of "if," but "how." As leaders, the responsibility falls to us to guide this transition in a way that is not only technologically successful but also human centric. The data and case studies are clear: success is not achieved through mandates or by simply providing a tool. It is achieved through a deliberate strategy of building psychological safety, fostering a culture of learning, measuring what matters, and thoughtfully integrating automation to solve the most pressing challenges in your development lifecycle.
 



 By framing AI as a collaborative partner rather than a disruptive threat, you can transform your engineering organization into a continuously learning, adaptive system, one where human creativity and machine intelligence co-evolve to deliver better software, faster, and with greater joy.
 


















### 
 Engineering intelligence



 Learn more at getdx.com Copyright © 2025