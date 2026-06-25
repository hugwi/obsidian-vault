---
categories:
  - "[[Resources]]"
domain: engineering
title: "What AI augmentation means for technical leaders – Birgitta Boeckeler"
source: "https://www.youtube.com/watch?v=qB7rsbDfmQg"
author: "Agile meets Architecture"
published: 2026-03-21
created: 2026-05-06
description: "AI assistance for software development teams continues to evolve at a fast\"
tags:
  - to-process
  - llm-foundations
---

Yeah. Hi everybody. Um, yeah. So, the reason that I talk about this a lot is that at the moment I have a full-time role at uh, ThoughtWorks, my employer, a consulting company, to just be like a kind of like an advocate for the topic of using AI on software delivery teams to deliver software. um it's it's about more than just using it for the coding but obviously the coding is the area where all of the um the energy is 

happening right now and I've done a lot of these like kind of stateof play of AI coding at conferences over the past two and a half years and usually when I hand in an abstract or talk to the conference committee and then when the conference actually happens a lot of stuff happens right so I had actually originally planned to talk about things like you know AI relevance for technical leaders like using AI for your own work. Using AI to improve and modernize the systems landscape. Uh help your teams amplify the good, not the bad 

and the ugly and make it as safe as possible to use AI. Um but what I'll actually focus on is really the context of coding in particular and like uh um yeah point out different aspects of how you can help make it more safe or help your teams do this. And what I'll actually do is just uh describe kind of on a high level 30,000 feet sometimes a little bit lower view of what happened over the last year or so in the AI coding space because I'm sure most 

people are pretty overwhelmed right even I am even though I do this uh full-time. So and one thing that really really evolved over the past year is the topic of context engineering. This is a term that uh first started going around maybe in June or so last year and it means different things for like when you're building agents um uh but also it means a specific things when you're using coding agents and at the time about a year ago or so when I was talking about this topic the simplest form of context 

engineering for a coding agent was these rules files. So context engineering the simplest definition of it is that you curate the information that the model sees so that you get better results better for your situation. And again the simplest form at the time were these rules files. So um it's either like agents.md or claw.md or these types of files in your workspace that uh you describe your coding conventions or certain things that you see the coding agent step into um again and again. Like 

here mine kept forgetting to activate the virtual environment in my Python project. So I put it into this file so that the agent would forget it less. But since then the space has kind of like exploded and there are more and more advanced ways of curating this information for your coding agent so that you have higher probability of getting the results that you want. So there's now skills and commands and MCP servers already were there a year ago of course but that has also evolved. There 

are sub agents specs plugins. So it's all a little bit overwhelming. Um it's kind of like a mandrang time like a storming time uh in in this space. Um and by the way doing all of these things is not a prerequisite for using a coding agent. Like I can see people who are now starting to use them kind of like freak out a bit and they don't even like want to use them until they have like a good rules file or something like that. you can just get started very plainly without any of this and I would even recommend doing that so that you 

experience it kind of in its in its raw firm for form first. Um so maybe to just go into a little bit more detail of one of these things that has been like a big topic recently which is skills to kind of give you an example of how uh the space has become more sophisticated what you can do with context engineering. So skills is a new uh concept that was introduced by anthropic as part of cloud code and was then almost immediately start like the other products started implementing that as well. So GitHub 

copilot has it, cursor has it like almost all the big coding assistants have it now and so what's different with these skills in comparison to the agents MD file or you know like a slash command like a reusable um prompt. So one thing is that this now allows you to better modularize your rules or the reusable prompts that you have. So I don't know if you can all see this here but I have an example here with multiple folders. Uh one is code review, one is get logs and one is react component. So those react components would maybe be your 

conventions about how to build a react component. Get logs would be one to like how do we get logs from our AWS uh test environment or something like that. So that's one thing you can modularize this more. And then the second thing is that this modularization also means that you can kind of progressively disclose this to the large language model. So the large language model gets this description here at the top. Uh in my example, it's get logs from our test environment for example for debugging incidents and the large language model 

initially only gets this description and it can decide itself when to load it. So everything you have in the skill is not put into the context window until either the human or the large language model decides that you want to pull it in. Um it can also include more files. So it's folders, right? So you can put in uh documentation there or you can put in scripts. Um like in this case I put could put in the script that calls the AWS CLI exactly in the way that we want 

to. Um so and again you it's not dumped into the context window from the beginning but it's loaded just in time ideally when the large language model makes the right decision. Um, yeah, and often these also refer to already installed CLIs or scripts like I just said, right? And so that's the reason why you might have heard that skills in some cases are replacing MCP servers because instead of having an MCP server run that can call your AWS API, you 

maybe just tell the agent in the skill that they should call the AWS CLI that's installed on your machine. So like CLIs are in a lot of places replacing uh MCP servers and context engineering in a nutshell just to like step back from it a little bit again is like uh a combination of on the one hand reusable instructions and conventions that you write down in natural language. it's often like uh lots of markdown files, right? Um in combination with this uh idea of context 

interfaces, right? So um that the the agent really just as gets descriptions of all the tools and MCP servers and skills that are available. Uh and that's also part of the context, right? And then the large language model can decide when to load or call those things, when to tell the agent to do that. And then ideally like I just said so it's like part of this context engineering is that you want to intelligently load these things just in time. And as a human then often our job is to manage and monitor the context 

size because even though technically the context windows have gotten a lot bigger um you you want to really like not have the window too full. So like a lot of people kind of like try to wrap up a coding session when the window is maybe 60% full and start a new one because it becomes like more erratic the results and it also becomes more expensive. So here's an example of uh on the left cloud code and on the right GitHub copilot they now provide a lot more 

transparency into what's in the context window. Right? So here on the left actually in cloud code um at this point in time my session I had actually just started it. I had maybe like done one back and forth and my context window was already 15% full. That's because you have the system prompt the agents MD you have maybe like the descriptions of all of your context interfaces. So you want to kind of like monitor this and see kind of like balance your setup of how much stuff you're putting into the um context window because when there's 

irrelevant stuff in there, it also can confuse the model, right? And then maybe as the last technique that has really uh unlocked a lot of stuff that I'll talk about in a little bit as well in context engineering is the idea of sub agents. So where you have like a main conversation and it spawns off little um sub aents that have their own context window. So a really good example of that that a lot of coding agents are doing now I don't know if you can read it in the back there's a screenshot here of cloud code and it 

says running to explore agents. So um in the beginning of a session when the agents uh kind of research what's in your codebase that often takes a lot of tokens because they have to read a lot of files and then when you spawn that off as a separate agent that just reports the results back to the main session then you can potentially like save a lot of tokens that you don't need in your uh main uh conversation. And yeah, so sub agents are also really important when you want to do like more longer running workflows that you don't 

just want to do in one big context window. So as technical leaders in the context engineering space, so ask yourself, you know, what coding conventions you want to amplify and maybe like put into skills that teams can use. Um what workflows can you build to for modernization initiative? So migration is actually a really really good use case for generative AI with the human in the loop, right? But it can like really help with this. I was recently uh uh talking to a colleague was working for a 

client where they had uh she said thousands of uh team city pipelines that they all wanted to migrate to GitHub uh actions and she was working on a workflow how generative AI can help them migrate and map all of those things. Um what tools should be available in your organization that agents can use? So are there maybe like custom CLIs for very common things that that that you would need or what MCP servers make sense and so on. Um what are practices you want to amplify? So in the past my favorite 

examples have always been like can you have a prompt that helps people write better architecture decision record or can you have a prompt that makes threat modeling less daunting and makes it easier to start with that. Those can also be skills that people can can use in their um coding agents. Um, this one is kind of like yellow because like versioning and distribution and stuff like that, there's still like a lot of um open questions about these things, right? And also, is it making things better or worse? So, it's kind of 

context engineering in scare quotes, right? Is this really engineering when we're not versioning it when we don't know if we're making it better or worse, right? There's like um evals coming out now in some places in this like skills registry, Tesla, they have evals now. Anthropic has also just released something to do eval so kind of like is it better or worse kind of testing for skills. So there's a lot still to do to mature this but uh even at this stage like you can take advantage of uh some of these things quite well already. 

So this more sophisticated context engineering in combination with models getting a lot better, right? Probably most of you have heard about um the jump that uh the models have done recently again at coding with the newest uh version of the Opus model and the newest version of the GPT codeex model. So those things in combination have now led to like a trend of people trying like more agent autonomy with less human 

supervision, right? And by supervision I mean like you know supervised I sit in front of it. I actually like intervene. I like steer. I uh maybe like keep saying yes you're allowed to execute this command. No you're not allowed to execute that command. Right. In comparison to unsupervised where this is like a screenshot from OpenAI uh codecs from their um cloud interface. So where you really like put a prompt in there and just send it off by itself for 20 

minutes or so. And these um kind of platforms have also started popping up a lot over the past year, right? So just recently, this is a um a screenshot from a platform called Warp uh Oz that was just recently released and all of the big coding uh agent products now actually also have a cloud version, right? So this is like cursor for example, this is cloud code. So for all of them you can now say not just do it like on your machine but say do this in 

this um cloud environment right and um this has also been uh pushed forward by one of the attributes of the CLIs that have really gotten traction over the past year as well uh starting with clawed code. Now all of the other uh coding agent products have started copying that as well. They also all have CLIs and one of the attributes of those is that they're headless, right? So you can run uh you can run them in headless 

mode. So it also makes it easier to start experimenting with integrating these into your pipelines if you want to. So it's like a more natural building block of what we're already used to. So here I was uh integrating clot code into a GitHub actions um pipeline. Maybe just a note about this like terminal user interface versus graphical user interface because I think there's a lot of talk about how cloud code is so uh um successful and people don't even open their IDEs anymore. I actually think that claude code in part is so 

successful because of how good it is under the hood and uh um so I know you probably can't read the details but so the bottom right is basically a screenshot of cursor right and I actually still prefer that graphical user interface and cursor is also quite good under the hood so I'm not like 100% convinced yet that it's all about that terminal user experience I just think like clot code is really cloud code is really good and there will still be a preference of people which kind of visual exper experience they um they prefer as long as what's happening 

inside of the agent is is good enough for what they want to do. So as part of this a familiar beast rears its head which is like kind of dev sandboxes right or all the challenges that we also have when we run things in a in a pipeline right so we have to have everything installed that the agent needs to uh to run things right so all the dev tools all the language compilers and so on we have to things about we will run into things like out of memory errors and stuff like that right we have 

to think about internet access in even more different ways than we have to with our you know pipelines before where internet access was mostly about installing things but now it's also about like do I want to allow the agent to do web research and potentially get prompt injected right so uh we have to think about like internet access yes or no when should it have internet access and and where too and this is also true of course for local sandboxes which I'll get to in a few minutes as well 

so a short intermetso for this uh autonomy hype. So the the hype duour so to say is um got like a lot of new starting attention let's say with this uh blog post by Steve Yagi welcome to Gas Town which maybe like lots of you have read. Yeah I see some hands. Yeah. So this is a um this is from that article where he's saying okay this is stages of deaf evolution like when you're at stage six you have three clot 

code instances open at the same time when you're at stage seven you have like 10 of them and stage eight is this like big thing that things like gas town are doing which um I usually call like agent swarms right so it's this idea of throwing as many agents as you can at the wall and seeing what sticks kind of like a brute force um uh uh approach. Um I kind of think of it as like with large language models, we threw all of this data at a model architecture and we had 

all of these emergent capabilities that even the makers didn't really expect and I think of agent swarms almost as like what if we throw lots of agents out there and they just all coordinate with each other and there dozens or hundreds of them. Um what will happen? Will we also get some emerging capabilities? There were these two experiments by cursor and anthropic recently that also got a lot of attention and made some people really nervous. So cursor had uh like lots of agents like that running for a week to build a browser and anthropic had lots of agents running for 

a while to build a C compiler. The interesting thing about these experiments is that both of these use cases browser and C compiler have very very good specification and in the case of the C compiler in particular very good test suites already out there on the internet. So specification is there and a really good safety net for the functionality. So at least cursor is also explicitly saying that's why they chose this use case. So I don't think that makes the experiments like useless or something but it's just like 

something to keep in mind, right? that it wasn't just magically just getting one prompt to build something and then it uh then it did it. But there's lots of specification out there already. Um setting up tools like Gas Town or this Cloudflow tool is sometimes like a little bit scary and it also like eats a lot of tokens of course. So if you just want to dip your toes in and not just go into this like futuristic swarm direction, but just try to run something with multiple agents, you can also try this new feature in cloud code called 

agent teams where you can see a little bit like of like some of the coordination that the agent is trying to do to kind of determine what do I run in parallel, what do I run sequentially. So if you just want to like experiment with that a little bit, then that's maybe a a safer and easier way than with these super big machines. [snorts] So I say back to the present now because I would say that these things are really like probably none of the organizations that you work for it makes 

sense to experiment with uh swarms um like that yet or ever. Let's see. [laughter] So for the less supervision, more autonomy part as technical leaders, I think maybe what you can ask yourself if you want to like uh uh start looking if this makes sense for organization for your organization is one maybe like where do you want to experiment with these cloud agents or with like um uh more autonomy less supervision. So and that will also make you reflect like how safe is actually the environment in our 

organization right like what is the safety net here for the agent? that you you know if you feel unsure about it, you can try it with smaller things like cleaning up feature toggles and stuff like that and just see uh um what happens. Uh it it's definitely become because of all of these platforms a lot um easier to try this uh to try this out. Um yeah, and how do you help your teams gauge the appropriate level of supervision for a particular task, right? When you don't want them to like maybe build full features in this 

autonomous mode, but like how do you gauge that in general? Um, so what I found myself doing a lot more on all kinds of micro and macro levels is like little risk assessments of when I use AI and also like how much review I apply to it. And a risk assessment is always in any situation a combination of three things of probability, impact and detectability, right? So I think about what is the probability that AI gets it wrong like does something that I don't 

want and that's usually uh uh reflecting on things like knowing my tool that I use like cloud code or cursor and also knowing the context like do I even give the agent a chance to do what I want like how uh uh how confident am I even in the level of requirements and how much context do I give it then the second one is like what's the impact if AI gets something wrong so that's obviously about the critical ality of the use case, right? Is this proof of concept or a spike or is this something 

that I I'm on call for at the weekend and it's in the critical path of uh our um our business processes, right? And then the third one, detectability that AI got something wrong. So, I have to know my feedback loops, right? Not only did it get something wrong, but also how quickly will I notice, right? Like will it be easy to test for me and see if it did what I wanted? And then um all of those things kind of like maybe determine which workflow I use, right? Do I just dump like a quick prompt in or 

do I put more effort into what I tell um the agent? How much review do I apply? Like again the case of a proof of uncritical proof of concept uh that I know uh um it's the type of thing that the agent is really good at. I might not look at a single line of code, but again if it's other stuff I apply at different levels of of review. And it also might determine how long I let it go without supervision. Like, do I actually sit in front of it and like look at every single response or not? Of course, I 

don't have this checklist on my desk and like really academically think about it every time, but I've just felt myself getting like um more intuitive at doing this assessment over time. Almost like a new skill uh to develop. And interestingly, I actually think that except for the one thing that I highlighted as yellow here, all of these things are actually things that are already skills that a good developer should have, right? Reflecting, being good at reflecting on the criticality of what we're doing, knowing our feedback 

loops, kind of uh reflecting on how much certainty and uncertainty we have. So the new thing that we need to develop is like knowing our AI tool and like kind of getting good at fe curating this context that I was talking about before and this is something that you cannot learn from a book right you actually have to do it for a while so especially as more experienced people even if you're skeptical of this right you have to use this so that you can help the people who are less experienced than you 

like understand where it's good where it's not good like what what new safety controls you need and so on. So yeah, it's kind of like almost this probability and detectability part is also uh reflection on you know like a you have to be this tall to reduce supervision in the agents right like what is your environment in your organization like how many feedback loops are there how automated are they um the probability that AI gets something wrong can also have to do with the quality of the existing code bases 

that are there right we already heard um I think Kevin was mentioning it as well like AI amplifies right AI I amplifies indiscriminately. So, um it kind of like amplifies the environment it's in. So, this um helps you also on an organizational level think about probability and detectability. But of course, with more autonomy, less supervision with this trend like uh there's like other beasts that rear their heads, right? So, beware of uh security and uh cost, right? So the 

stories about security problems are starting to become more frequent. Um one of the things is for example unwanted command execution right. So this is a combination of prompt injection and now sorry this kind of like line break. So bypassing allow lists, right? So um uh I told you before like some when you supervise you actually sometimes say yes you're allowed to execute this no you're not allowed to execute that and but you can set certain allow lists and sometimes there's weaknesses in these 

regular expressions or however they implemented that you can still um get around those um the mo freshest story that I've heard this was from yeah okay March 5th what do we have today March 10th yeah so this is from 5 days ago um this was about a GitHub issue where there was basically instructions in the GitHub issue on an open source project that led to like a whole chain of attack that actually extracted the secret that was needed to push that package to the 

npm registry and it was ultimately pushed to the registry with like a new post install um command. Um so this is like a great example of the lethal trifecta. Can I ask you has heard of the lethal trifecta before? uh should like this is like hopefully after this you all look this up and uh and internalize it like this is like a super super helpful model to think about the uh the safety of like agent agentic 

use cases right so Simon Willis wrote this up and he says that when you have an agent that has these three attributes or features the agent has uh exposure to untrusted content in this case that was a GitHub issue right it's untrusted content because anybody can create an a GitHub issue. Um the agent also has access to private data and the agent has the ability to externally communicate. Then you have a problem, right? Because then yeah, somebody can just inject untrusted instructions. The agent might 

get like something private and externally communicate it. And by the way, like when you think about a lot of the agentic use cases in the business world that we are being promised for the future, right? Many many many of those use cases have this conceptual problem. It's not a technical problem, right? It's a conceptual thing about a use case. So yeah, will be interesting how we can even get around that for some of those use cases. And then secondly, after security uh is 

cost, right? Uh obviously the the honeymoon is over, right? So here's a quote from a keynote I heard at Craftcon in 2024 where the speaker said, "Generating a 100 lines of code only costs about 12 cents. Compare that to a developer salary, right? Then fast forward to uh this is data from last summer. Uh it's some website where people post their token usage with I think at the time it was cloud code. And this particular person that I have the screenshot for here was on average uh using 380 burning $380 a day. That 

extrapolated to a salary is actually $91,200 which is a pretty good salary for a developer in Germany, right? So, um, yeah, it's it's not really, uh, like that anymore, right? So, we went from $20 flat rates or I think GitHub Copilot in the beginning was even $10 a month to more like around like the Claude Max subscription is $200 and it's not really a real flat rate anymore. So, 

you still get throttled and there's request limiting and probably even that is still subsidized by the companies. There was this blue sky thread recently where a journalist was asking people who have these flat rate subscriptions. There was like a way to determine what you're actually using in terms of tokens. And this person was on a $100 plan and was using $591 in that particular month. And I think even the $591 is probably still a subsidized perspective on what it costs. So it's 

kind of like yeah unclear where this is going. So, and why do 100 lines of code now cost more like 250 and not 12 cents? And I should mention, of course, like number of lines of code is not a measure that we should be looking at anyway, right? So, let's leave that aside for now. It's just like an example of like um uh the the the the cost explosion, right? Um because now we don't just like ask a chat to give us a 

few lines of code or like have autocomp completion but we research the existing code. We plan we review the plan. We start implementing making changes. Then the agent runs the tests, fixes the tests, checks lint errors, fixes those uh checks the browser maybe if it's a front-end feature. So they can now open the browser and kind of like check what's going on there. Uh you know there's more fixes. There's a code review step. uh summarization at the end. So it's all of these like loops that we built in and every single back 

and forth uh costs tokens, right? So for the less human supervision, we also now have to ask ourselves as technical leaders like how to sandbox the coding agents, right? So that's like not just in the cloud but also locally. So I uh a lot of developers now are starting to use dev containers more or there's some built-in sandbox modes in some of the coding agents that it's also easy to get around. But yeah, so there's like a lot of with security, you know, you have to think about the sandboxing and make it easy for people in your 

organization and making sure that everybody really understands this lethal trifecta when they um when they build agent use cases. And then finally like more autonomy, less supervision. What about maintainability? So um um I'm not going to talk here about like what the current state is of uh you know how how good the code is that comes out of the coding agents um directly. So like in in in terms of time but um 

obviously you know like uh there will always be a level of non-determinism. we can never be 100% sure that we get exactly what we want even though it has gotten a lot better, right? Um, and so what uh what are maybe new ideas to uh to tackle that just from a code quality uh standpoint? There was recently this really interesting article by a team at OpenAI um who uh started a new codebase from scratch five months ago and their goal was to not touch the code 

themselves at all. And instead over those five months, every time there was like a problem in the code, they they worked on this what they call like a harness. So kind of uh that that gives the agent feedback um and uh let's self-correct um as well. So in the article they're talking about context engineering that they've done. So kind of like all of these skills and agents MD things. They talk about setting architectural constraints with uh custom llinters and structural tests. And they 

also talk about garbage, what they call garbage collection. So they still saw with all of this that there was still a lot of drift and entropy the same way as when humans um maintain code. So they had like a bunch of agents run regularly on the codebase to again look for the structural issues and try to try to improve um over time. So I recently also did some like um experimentation with these architectural constraints in particular um structural tests as agent 

feedback. I mean this is something that we've had for quite a while right when you think about arcunit or maybe some of you know spring u modulith right so kind of like frameworks where you can define rules about how you want your codebase to be structured and then they can give you an indication when you violate those rules. And so I was just working on a codebase and then developed with AI kind of the layers that I wanted and then different rules like for example in the only the clients package was allowed to import 

external SDKs so that my domain wouldn't be dirtied by that. Right? So I just had a bunch of those rules and then I had them running in parallel to the agent and the agent could kind of like request you know how am I doing and it would give it these um uh yeah these messages and you can also then when you think of like custom llinters or these structural tests you can in the messages of the linting right you can prompt inject in a good way 

right so you can change the messages of lint uh errors to kind of tell the agent what it to do, right? So, for example, when it's a rule like each file should have maximum 500 lines of code to prevent that the agent starts just putting lots of statements in one one line, you can put into the error message that is a smell we should redesign, right? So, that's kind of like all part of this like evolving llinters and stuff like that for agent usage. And so for me like I've been playing 

around with this mental model. I would also be interested uh later maybe in the networking if you have any feedback for that if that resonates or if it's confusing. So um we have the uh coding agent and then what we're doing when we're doing this context engineering so writing down coding conventions, rules, examples, reference documentation, giving the agent access to all of that stuff. I think of that as like feed forward, right? So we're anticipating that the agent might need to know all these things or might do them wrong like not use the virtual environment. And so 

we're kind of like feed forward but it's a little bit like hope and pray that the agent will do this right and then what we also need and this is like uh this is only now what people start talking about more is kind of the feedback. So kind of like sensors that tell it about the runtime state of the application, the static analysis state. Um uh maybe mutation testing is a good feedback as well because it will tell the agent like how good the tests are that it wrote. And um so these different colors here 

are supposed to indicate that we can have a mix here of things that are large language model executed so GPU inference and things that are executed by the CPU right something like static code analysis is CPU right so it gives us a lot more trust in the outcomes and it's also cheaper and faster uh but we can still have I just called it agent as judge here so we can still have a code review agent running or some uh stuff like that and also take advantage of an LLM them to give us more review and also in the feed forward you can do that by 

the way. So some of that is already built into coding agents. But in feed forward you can also think about for example giving the agent access to uh refactoring functionality like there's a jet brains MCP server that gives the agent the ability to do the rename symbol function from uh from like a proper IDE right and with that again you increase like um the uh how good the outcome is and um kind of like prevent that it or you increase the probability 

that it does the right thing in the first place. So it's all about you know turning that lever of uh that dial of probability uh that you get a good outcome and then the human is kind of like in this steering situation right where you also can use an agent to continuously work on these guides and on these sensors and especially for the sensors because we have coding agents now we can actually build a lot more custom tooling here. It's a lot easier um than it used to be to build more advanced llinters. In the past, we never 

would have done that because it felt like a a waste of time, right? And then that whole thing is kind of that harness that uh was also being talked about in that in that article, right? Um yeah, so kind of like harness, right? So you have kind of like reins and you know restrict the movement of the system that you're regulating so to say, right? So all kind of like reminds us of cybernetics and stuff like that, right? 

So yeah, and you want to have like as many CPU executed sensors in particular as possible, right? And also you want them to be as left as possible, right? I see so many people write about how they have all of these things after they do the commit or on the pull request. And it's even built into some of the tools. There's a review uh skill and a security review skill in cloud code that you cannot just apply to your local changes. 

It expects a br to be on a branch on a git branch or it expects to be in a pull request which to me is like what I want to use this on my local changes. I want to do this before I create the commit. Right? So um I also see like first signs of people there was a an article from Stripe recently who wrote about like how they are doing this and they're also talking about doing things pre-commit. So there's like first signs of like this realization coming in but it's still because our industry is so like pull request by default uh um at this moment 

in time like a lot of this stuff happens too late I think. Yeah. Yeah. And again, this harness kind of again, like I said, changes the the probability that AI gets something wrong or right and is also a way for us to reflect on the detectability of some things, right? So the probability part is basically our trust in the agent and what are the things that we can do to move that trust level and it cannot just be by oh yeah the model magically got 

better, right? So we want to have some some other stuff around that as well. And by the way, I was mainly talking about internal code quality here, right? And things like maintainability. I can totally see how maybe an agent at some point is a lot better than us at modularizing a codebase, right? We have been so shitty at that historically, right? That's why we start creating a new microser all the time because we're so bad at modularizing internally. But there's still like lots of open questions for me about verifying 

functionality because there's this whole dilemma of we have to specify correctly and then how do you verify that and you can't just like at the moment most people just seem to trust the tests that are generated by the AI when they use agents at a at a high level which I think is just uh not enough right so I think of these harnesses almost like there's different ones right like I was just talking about some for maintainability maybe there's others that you know kind of try to uh kind of harness in the quality of the 

operability of a system. But then there's behavior as well, right? And for the behavior part, yeah, like I said, I still have lots of open questions, but I kind of like this uh uh thinking in harnesses because it helps us reflect on what is actually our safety net around an agent. And then in combination with models that got better, I think then we can make that risk assessment of like when do I trust it, when do I not trust it? And then finally I feel like maybe you know will we have some topologies in 

the future that are the new abstraction level where you can have a harness around it right so let's say there's like that structure was a typical layer structure that I was showing you before right like there was like routes coming in there was like a almost like a controller that loads data from some client APIs and that then has like a domain layer right that's super typical of what we do right and then let's say in combination with a text stack you have a bunch of guides and sensors that you can just instantiate whenever you want to do a project like this, right? 

And then maybe I at some point I don't even care if it's ReactJS or Vue.js or whatever because I don't even like yeah I don't have to deal with those details anymore. And maybe uh it will be a big question for us when we choose technologies like how harnessable are they because it will reduce the work that I have so much more. So in summary, context engineering uh has evolved a lot over the past year and it's this powerful lever for us as technical leaders to of amplification, 

right? Um and then secondly, there are very strong forces right now tempting humans out of the loop, right? Oh, the models are getting better. There's like everything's a lot easier to experiment with with these cloud agents and oh, you just have to have like a simple harness like that and then everything will be better, right? So it's like it is really like a strong pull right now and uh with together with the hype. So it's about like where can your organization give into that poll and where is it dangerous 

right like this reflection on probability uh impact and detectability. Yeah, that's all like I have. Um I regularly write on my colleague Martin Farer's um website and uh yeah, all of my other content is also on my personal website. And that's it. And I'm in time. [applause] 

>> One question. >> Perfect. And since you're you you haven't extended your time almost at all, let's do at least one question. Um, how can a technical leader coordinate over a team of human engineers that all use cloud code? >> Um, coordinate across the team. Yeah, I mean I don't know what the background of the question is but um so there's multiple like one coordination level is 

is what I was talking about to to help the team amplify the right things with like thinking about skills and tools that should be available to the agents right but I don't know if it's also related the question to um when you have a full team like going all in with this and creating a lot of throughput then as the leader of a team or the delivery manager or something like that you a lot of moving pieces on the table that you can't just revert like uh in inside of a coding session right so I don't know if the question is related to that but that's 

also like one of my big question marks what happens with like parallelization and this higher throughput that is happening in so many places I mean the managing that is just one of the many bottlenecks right I didn't even have time to go into all of that what happens to the pipelines what happens to the requirements coming in what happens to monitoring all of those new features if they actually create value and so so on and so on. So it's a big question. I am >> so basically it's a good question. We have to deal with it. >> It's a good question. [laughter] 

>> Okay. I mean, I tried this like three cloud code instances at the same time and I abandoned it again because it was too it was too much. And that's also like Kevlin talked a bit about it today as well like there are first reports of like burnout or being overwhelmed or like Steve himself says I can work like this two or three hours a day and then I'm tired and done. Right. So it's like not even on the team level just like you with like three, four, five cloud code instances is just Yeah. 

Okay. So, as usual, you all know the drill already. Um, you'll be around, you can be found, you can be ask questions, right? >> Yeah. >> Okay. So, for now, thank you very much. Yeah. >> Thank you. [applause] 

<p>
 <span data-rw-start="7.04" data-rw-transcript-version="2">
 Yeah. Hi everybody. Um, yeah. So, the
 </span>
 <span data-rw-start="9.44" data-rw-transcript-version="2">
 reason that I talk about this a lot is
 </span>
 <span data-rw-start="11.2" data-rw-transcript-version="2">
 that at the moment I have a full-time
 </span>
 <span data-rw-start="12.88" data-rw-transcript-version="2">
 role at uh, ThoughtWorks, my employer, a
 </span>
 <span data-rw-start="15.44" data-rw-transcript-version="2">
 consulting company, to just be like a
 </span>
 <span data-rw-start="18" data-rw-transcript-version="2">
 kind of like an advocate for the topic
 </span>
 <span data-rw-start="20.08" data-rw-transcript-version="2">
 of using AI on software delivery teams
 </span>
 <span data-rw-start="22.24" data-rw-transcript-version="2">
 to deliver software. Um, it's about
 </span>
 <span data-rw-start="25.519" data-rw-transcript-version="2">
 more than just using it for the coding,
 </span>
 <span data-rw-start="27.199" data-rw-transcript-version="2">
 but obviously, the coding is the area
 </span>
 <span data-rw-start="29.359" data-rw-transcript-version="2">
 where all of the energy is
 </span>
 <span data-rw-start="31.84" data-rw-transcript-version="2">
 happening right now. And I've done a lot
 </span>
 <span data-rw-start="33.68" data-rw-transcript-version="2">
 of these state-of-play of AI
 </span>
 <span data-rw-start="36.32" data-rw-transcript-version="2">
 coding at conferences over the past two
 </span>
 <span data-rw-start="38.32" data-rw-transcript-version="2">
 and a half years. Usually when I hand
 </span>
 <span data-rw-start="41.28" data-rw-transcript-version="2">
 in an abstract or talk to the conference
 </span>
 <span data-rw-start="43.36" data-rw-transcript-version="2">
 committee, and then when the conference
 </span>
 <span data-rw-start="44.96" data-rw-transcript-version="2">
 actually happens, a lot of stuff happens.
 </span>
 <span data-rw-start="47.039" data-rw-transcript-version="2">
 Right, so I had actually originally
 </span>
 <span data-rw-start="49.44" data-rw-transcript-version="2">
 planned to talk about
 </span>
 <span data-rw-start="51.84" data-rw-transcript-version="2">
 things like, you know, AI relevance for
 </span>
 <span data-rw-start="53.52" data-rw-transcript-version="2">
 technical leaders, like using AI for your
 </span>
 <span data-rw-start="55.52" data-rw-transcript-version="2">
 own work. Using AI to improve and
 </span>
 <span data-rw-start="57.36" data-rw-transcript-version="2">
 modernize the systems landscape. Uh, help
 </span>
 <span data-rw-start="59.84" data-rw-transcript-version="2">
 your teams amplify the good, not the bad.
 </span>
</p>
<p>
 <span data-rw-start="61.68" data-rw-transcript-version="2">
 And the ugly and make it as safe as
 </span>
 <span data-rw-start="63.199" data-rw-transcript-version="2">
 possible to use AI. Um, but what I'll
 </span>
 <span data-rw-start="66.479" data-rw-transcript-version="2">
 actually focus on is really the context
 </span>
 <span data-rw-start="69.6" data-rw-transcript-version="2">
 of coding in particular, and like uh, um,
 </span>
 <span data-rw-start="73.28" data-rw-transcript-version="2">
 yeah, point out different aspects of how
 </span>
 <span data-rw-start="75.2" data-rw-transcript-version="2">
 you can help make it more safe or help
 </span>
 <span data-rw-start="77.04" data-rw-transcript-version="2">
 your teams do this. And what I'll
 </span>
 <span data-rw-start="79.2" data-rw-transcript-version="2">
 actually do is just uh describe kind of
 </span>
 <span data-rw-start="81.759" data-rw-transcript-version="2">
 on a high level 30,000 feet, sometimes a
 </span>
 <span data-rw-start="84.56" data-rw-transcript-version="2">
 little bit lower view of what happened
 </span>
 <span data-rw-start="87.04" data-rw-transcript-version="2">
 over the last year or so in the AI
 </span>
 <span data-rw-start="89.2" data-rw-transcript-version="2">
 coding space, because I’m sure most
 </span>
 <span data-rw-start="91.2" data-rw-transcript-version="2">
 people are pretty overwhelmed right even
 </span>
 <span data-rw-start="93.6" data-rw-transcript-version="2">
 I am, even though I do this uh, full-time.
 </span>
</p>
<p>
 <span data-rw-start="97.2" data-rw-transcript-version="2">
 So, and one thing that really, really
 </span>
 <span data-rw-start="98.96" data-rw-transcript-version="2">
 evolved over the past year is the topic
 </span>
 <span data-rw-start="101.6" data-rw-transcript-version="2">
 of context engineering. This is a term
 </span>
 <span data-rw-start="103.92" data-rw-transcript-version="2">
 that uh, first started going around maybe
 </span>
 <span data-rw-start="106" data-rw-transcript-version="2">
 in June or so last year, and it means
 </span>
 <span data-rw-start="108.079" data-rw-transcript-version="2">
 different things for, like, when you’re
 </span>
 <span data-rw-start="109.28" data-rw-transcript-version="2">
 building agents. Um, uh, but also it means
 </span>
 <span data-rw-start="112.159" data-rw-transcript-version="2">
 specific things when you’re using
 </span>
 <span data-rw-start="114.56" data-rw-transcript-version="2">
 coding agents. And at the time, about a
 </span>
 <span data-rw-start="117.119" data-rw-transcript-version="2">
 year ago or so, when I was talking about
 </span>
 <span data-rw-start="118.64" data-rw-transcript-version="2">
 this topic, the simplest form of context.
 </span>
</p>
<p>
 <span data-rw-start="121.68" data-rw-transcript-version="2">
 Engineering for a coding agent was these
 </span>
 <span data-rw-start="124.24" data-rw-transcript-version="2">
 rules files. So, context engineering, the
 </span>
 <span data-rw-start="127.2" data-rw-transcript-version="2">
 simplest definition of it is that you
 </span>
 <span data-rw-start="129.44" data-rw-transcript-version="2">
 curate the information that the model
 </span>
 <span data-rw-start="131.44" data-rw-transcript-version="2">
 sees so that you get better results
 </span>
 <span data-rw-start="133.68" data-rw-transcript-version="2">
 better for your situation. And again, the
 </span>
 <span data-rw-start="136.239" data-rw-transcript-version="2">
 simplest form at the time were these
 </span>
 <span data-rw-start="137.52" data-rw-transcript-version="2">
 rules files. So, um, it's either like
 </span>
 <span data-rw-start="140.08" data-rw-transcript-version="2">
 agents.md or claw.md or these types of
 </span>
 <span data-rw-start="143.36" data-rw-transcript-version="2">
 files in your workspace that, uh, you
 </span>
 <span data-rw-start="146.16" data-rw-transcript-version="2">
 describe your coding conventions or
 </span>
 <span data-rw-start="147.84" data-rw-transcript-version="2">
 certain things that you see the coding
 </span>
 <span data-rw-start="149.599" data-rw-transcript-version="2">
 agent step into, uh, again and again. Like
 </span>
 <span data-rw-start="152.879" data-rw-transcript-version="2">
 here, mine kept forgetting to activate
 </span>
 <span data-rw-start="155.44" data-rw-transcript-version="2">
 the virtual environment in my Python
 </span>
 <span data-rw-start="157.2" data-rw-transcript-version="2">
 project. So, I put it into this file so
 </span>
 <span data-rw-start="159.599" data-rw-transcript-version="2">
 that the agent would forget it less.
 </span>
</p>
<p>
 <span data-rw-start="162.879" data-rw-transcript-version="2">
 But, since then, the space has kind of
 </span>
 <span data-rw-start="164.48" data-rw-transcript-version="2">
 like exploded, and there are more and
 </span>
 <span data-rw-start="165.92" data-rw-transcript-version="2">
 more advanced ways of curating this
 </span>
 <span data-rw-start="168.239" data-rw-transcript-version="2">
 information for your coding agent, so
 </span>
 <span data-rw-start="170" data-rw-transcript-version="2">
 that you have a higher probability of
 </span>
 <span data-rw-start="171.68" data-rw-transcript-version="2">
 getting the results that you want. So
 </span>
 <span data-rw-start="173.519" data-rw-transcript-version="2">
 there's now skills, commands, and MCP
 </span>
 <span data-rw-start="176.239" data-rw-transcript-version="2">
 servers already there, a year ago, of
 </span>
 <span data-rw-start="178.16" data-rw-transcript-version="2">
 Course, but that has also evolved. There
 </span>
</p>
<p>
 <span data-rw-start="180.319" data-rw-transcript-version="2">
 are sub-agents, specs, plugins. So it's
 </span>
 <span data-rw-start="182.56" data-rw-transcript-version="2">
 all a little bit overwhelming. Um, it's
 </span>
 <span data-rw-start="184.959" data-rw-transcript-version="2">
 kind of like a mandarake time, like a
 </span>
 <span data-rw-start="187.519" data-rw-transcript-version="2">
 storming time, uh, in this space. Um,
 </span>
 <span data-rw-start="191.04" data-rw-transcript-version="2">
 and by the way, doing all of these things
 </span>
 <span data-rw-start="193.2" data-rw-transcript-version="2">
 is not a prerequisite for using a coding
 </span>
 <span data-rw-start="195.36" data-rw-transcript-version="2">
 agent. Like, I can see people who are now
 </span>
 <span data-rw-start="197.68" data-rw-transcript-version="2">
 starting to use them kind of like freak
 </span>
 <span data-rw-start="199.28" data-rw-transcript-version="2">
 out a bit, and they don't even like want
 </span>
 <span data-rw-start="201.36" data-rw-transcript-version="2">
 to use them until they have like a good
 </span>
 <span data-rw-start="204.08" data-rw-transcript-version="2">
 rules file or something like that. You
 </span>
 <span data-rw-start="205.84" data-rw-transcript-version="2">
 can just get started very plainly
 </span>
 <span data-rw-start="207.76" data-rw-transcript-version="2">
 without any of this, and I would even
 </span>
 <span data-rw-start="209.36" data-rw-transcript-version="2">
 recommend doing that so that you
 </span>
 <span data-rw-start="210.959" data-rw-transcript-version="2">
 experience it kind of in its, in its raw
 </span>
 <span data-rw-start="212.959" data-rw-transcript-version="2">
 form first. Um, so maybe to just
 </span>
 <span data-rw-start="217.12" data-rw-transcript-version="2">
 go into a little bit more detail of one
 </span>
 <span data-rw-start="218.799" data-rw-transcript-version="2">
 of these things that has been like a big
 </span>
 <span data-rw-start="220.239" data-rw-transcript-version="2">
 topic recently, which is skills, to kind
 </span>
 <span data-rw-start="222.72" data-rw-transcript-version="2">
 of give you an example of how, uh, the
 </span>
 <span data-rw-start="225.04" data-rw-transcript-version="2">
 space has become more sophisticated. What
 </span>
 <span data-rw-start="227.12" data-rw-transcript-version="2">
 you can do with, context engineering. So
 </span>
 <span data-rw-start="229.2" data-rw-transcript-version="2">
 skills is a new, uh, concept that was
 </span>
 <span data-rw-start="232" data-rw-transcript-version="2">
 introduced by Anthropic, as part of cloud.
 </span>
</p>
<p>
 <span data-rw-start="233.76" data-rw-transcript-version="2">
 Code and was then almost immediately
 </span>
 <span data-rw-start="236.4" data-rw-transcript-version="2">
 started, like the other products, started
 </span>
 <span data-rw-start="238.48" data-rw-transcript-version="2">
 implementing that as well. So, GitHub
 </span>
 <span data-rw-start="240.4" data-rw-transcript-version="2">
 Copilot has it, Cursor has it, like
 </span>
 <span data-rw-start="243.36" data-rw-transcript-version="2">
 almost all the big coding assistants
 </span>
 <span data-rw-start="245.36" data-rw-transcript-version="2">
 have it now, and so what's different with
 </span>
 <span data-rw-start="247.2" data-rw-transcript-version="2">
 these skills in comparison to the agents
 </span>
 <span data-rw-start="249.519" data-rw-transcript-version="2">
 MD file, or you know, like a slash command
 </span>
 <span data-rw-start="252.239" data-rw-transcript-version="2">
 like a reusable um prompt. So, one thing
 </span>
 <span data-rw-start="255.36" data-rw-transcript-version="2">
 is that this now allows you to better
 </span>
 <span data-rw-start="257.28" data-rw-transcript-version="2">
 modularize your rules, or the reusable
 </span>
 <span data-rw-start="259.919" data-rw-transcript-version="2">
 prompts that you have. So, I don't know
 </span>
 <span data-rw-start="261.199" data-rw-transcript-version="2">
 if you all can see this here, but I have
 </span>
 <span data-rw-start="263.04" data-rw-transcript-version="2">
 an example here with multiple folders.
 </span>
</p>
<p>
 <span data-rw-start="265.04" data-rw-transcript-version="2">
 Uh, one is code review, one is get logs,
 </span>
 <span data-rw-start="266.96" data-rw-transcript-version="2">
 and one is React component. So, those
 </span>
 <span data-rw-start="268.88" data-rw-transcript-version="2">
 React components would maybe be your
 </span>
 <span data-rw-start="270.96" data-rw-transcript-version="2">
 conventions about how to build a React
 </span>
 <span data-rw-start="272.639" data-rw-transcript-version="2">
 component. Get logs would be one, to, like
 </span>
 <span data-rw-start="275.199" data-rw-transcript-version="2">
 how do we get logs from our AWS, uh, test
 </span>
 <span data-rw-start="278.08" data-rw-transcript-version="2">
 environment, or something like that. So,
 </span>
 <span data-rw-start="279.919" data-rw-transcript-version="2">
 that's one thing you can modularize this
 </span>
 <span data-rw-start="281.84" data-rw-transcript-version="2">
 more. And then, the second thing is that
 </span>
 <span data-rw-start="285.199" data-rw-transcript-version="2">
 this modularization also means that you
 </span>
 <span data-rw-start="287.12" data-rw-transcript-version="2">
 can kind of progressively disclose this.
 </span>
</p>
<p>
 <span data-rw-start="289.28" data-rw-transcript-version="2">
 To the large language model, so the
 </span>
 <span data-rw-start="291.28" data-rw-transcript-version="2">
 large language model gets this
 </span>
 <span data-rw-start="292.479" data-rw-transcript-version="2">
 description here at the top. Uh, in my
 </span>
 <span data-rw-start="294.479" data-rw-transcript-version="2">
 example, it's get logs from our test
 </span>
 <span data-rw-start="296.56" data-rw-transcript-version="2">
 environment, for example, for debugging
 </span>
 <span data-rw-start="298.24" data-rw-transcript-version="2">
 incidents, and the large language model
 </span>
 <span data-rw-start="301.44" data-rw-transcript-version="2">
 initially only gets this description, and
 </span>
 <span data-rw-start="303.6" data-rw-transcript-version="2">
 it can decide itself when to load it. So
 </span>
 <span data-rw-start="306.32" data-rw-transcript-version="2">
 everything you have in the skill is not
 </span>
 <span data-rw-start="308.32" data-rw-transcript-version="2">
 put into the context window until either
 </span>
 <span data-rw-start="310.8" data-rw-transcript-version="2">
 the human or the large language model
 </span>
 <span data-rw-start="312.4" data-rw-transcript-version="2">
 decides that you want to pull it in. Um,
 </span>
 <span data-rw-start="316.08" data-rw-transcript-version="2">
 it can also include more files. So, it's
 </span>
 <span data-rw-start="318.24" data-rw-transcript-version="2">
 folders, right? So, you can put in, uh
 </span>
 <span data-rw-start="320.72" data-rw-transcript-version="2">
 documentation there, or you can put in
 </span>
</p>
<p>
 <span data-rw-start="322.639" data-rw-transcript-version="2">
 scripts. Uh, like in this case, I put
 </span>
 <span data-rw-start="325.68" data-rw-transcript-version="2">
 could put in the script that calls the
 </span>
 <span data-rw-start="327.68" data-rw-transcript-version="2">
 AWS CLI, exactly in the way that we want
 </span>
 <span data-rw-start="330.479" data-rw-transcript-version="2">
 to. Um, so, and again, it's not dumped
 </span>
 <span data-rw-start="333.759" data-rw-transcript-version="2">
 into the context window from the
 </span>
 <span data-rw-start="335.199" data-rw-transcript-version="2">
 beginning, but it's loaded just in time.
 </span>
 <span data-rw-start="338.24" data-rw-transcript-version="2">
 Ideally, when the large language model
 </span>
 <span data-rw-start="340.16" data-rw-transcript-version="2">
 makes the right decision. Um, yeah, and
 </span>
 <span data-rw-start="344" data-rw-transcript-version="2">
 often, these also refer to already
 </span>
 <span data-rw-start="346.72" data-rw-transcript-version="2">
 installed CLIs or scripts like I just
 </span>
 <span data-rw-start="348.72" data-rw-transcript-version="2">
 Said, right? And so that's the reason
 </span>
 <span data-rw-start="350.72" data-rw-transcript-version="2">
 why you might have heard that skills in
 </span>
 <span data-rw-start="352.72" data-rw-transcript-version="2">
 some cases are replacing MCP servers.
 </span>
</p>
<p>
 <span data-rw-start="355.36" data-rw-transcript-version="2">
 Because instead of having an MCP server
 </span>
 <span data-rw-start="357.52" data-rw-transcript-version="2">
 run that can call your AWS API, you
 </span>
 <span data-rw-start="360.479" data-rw-transcript-version="2">
 maybe just tell the agent in the skill
 </span>
 <span data-rw-start="363.44" data-rw-transcript-version="2">
 that they should call the AWS CLI that's
 </span>
 <span data-rw-start="365.68" data-rw-transcript-version="2">
 installed on your machine. So, like, CLIs
 </span>
 <span data-rw-start="368" data-rw-transcript-version="2">
 are in a lot of places replacing uh MCP
 </span>
 <span data-rw-start="371.36" data-rw-transcript-version="2">
 servers.
 </span>
</p>
<p>
 <span data-rw-start="372.88" data-rw-transcript-version="2">
 And context engineering, in a nutshell,
 </span>
 <span data-rw-start="374.639" data-rw-transcript-version="2">
 just to like, step back from it a little
 </span>
 <span data-rw-start="376.16" data-rw-transcript-version="2">
 bit again, is like uh a combination of on
 </span>
 <span data-rw-start="379.039" data-rw-transcript-version="2">
 the one hand, reusable instructions and
 </span>
 <span data-rw-start="381.6" data-rw-transcript-version="2">
 conventions that you write down in
 </span>
 <span data-rw-start="383.199" data-rw-transcript-version="2">
 natural language. It’s often like uh
 </span>
 <span data-rw-start="385.44" data-rw-transcript-version="2">
 lots of markdown files, right? Um, in
 </span>
 <span data-rw-start="388.24" data-rw-transcript-version="2">
 combination with this uh idea of context
 </span>
 <span data-rw-start="390.8" data-rw-transcript-version="2">
 interfaces, right? So, um, that the the
 </span>
 <span data-rw-start="394" data-rw-transcript-version="2">
 agent really just as gets descriptions
 </span>
 <span data-rw-start="396.24" data-rw-transcript-version="2">
 of all the tools and MCP servers and
 </span>
 <span data-rw-start="398.4" data-rw-transcript-version="2">
 skills that are available. Uh, and that's
 </span>
 <span data-rw-start="400.639" data-rw-transcript-version="2">
 also part of the context, right? And
 </span>
 <span data-rw-start="402.56" data-rw-transcript-version="2">
 then, the large language model can decide
 </span>
 <span data-rw-start="404.639" data-rw-transcript-version="2">
 when to load or call those things, when
 </span>
 <span data-rw-start="407.199" data-rw-transcript-version="2">
 To tell the agent to do that.
 </span>
</p>
<p>
 <span data-rw-start="410.319" data-rw-transcript-version="2">
 And then, ideally, like I just said, so
 </span>
 <span data-rw-start="412.56" data-rw-transcript-version="2">
 it’s like part of this context
 </span>
 <span data-rw-start="414.16" data-rw-transcript-version="2">
 engineering is that you want to
 </span>
 <span data-rw-start="415.199" data-rw-transcript-version="2">
 intelligently load these things just in
 </span>
 <span data-rw-start="417.44" data-rw-transcript-version="2">
 time. And as a human, then, often our job
 </span>
 <span data-rw-start="420" data-rw-transcript-version="2">
 is to manage and monitor the context
 </span>
 <span data-rw-start="422.24" data-rw-transcript-version="2">
 size because, even though technically, the
 </span>
 <span data-rw-start="424" data-rw-transcript-version="2">
 context windows have gotten a lot bigger,
 </span>
 <span data-rw-start="426.479" data-rw-transcript-version="2">
 um, you want to really like not have
 </span>
 <span data-rw-start="429.44" data-rw-transcript-version="2">
 the window too full. So, like, a lot of
 </span>
 <span data-rw-start="431.84" data-rw-transcript-version="2">
 people try to wrap up a
 </span>
 <span data-rw-start="433.68" data-rw-transcript-version="2">
 coding session when the window is maybe
 </span>
 <span data-rw-start="435.599" data-rw-transcript-version="2">
 60% full and start a new one because it
 </span>
 <span data-rw-start="438.479" data-rw-transcript-version="2">
 becomes more erratic, the results
 </span>
 <span data-rw-start="440.88" data-rw-transcript-version="2">
 and it also becomes more expensive.
 </span>
</p>
<p>
 <span data-rw-start="444" data-rw-transcript-version="2">
 So, here’s an example of, uh, on the left
 </span>
 <span data-rw-start="446.24" data-rw-transcript-version="2">
 cloud code and on the right, GitHub
 </span>
 <span data-rw-start="448.24" data-rw-transcript-version="2">
 Copilot. They now provide a lot more
 </span>
 <span data-rw-start="450.88" data-rw-transcript-version="2">
 transparency into what’s in the context
 </span>
 <span data-rw-start="453.36" data-rw-transcript-version="2">
 window. Right? So, here, on the left,
 </span>
 <span data-rw-start="455.28" data-rw-transcript-version="2">
 actually, in cloud code, at this point,
 </span>
 <span data-rw-start="457.919" data-rw-transcript-version="2">
 in time, my session, I had actually just
 </span>
 <span data-rw-start="459.68" data-rw-transcript-version="2">
 started it. I had maybe like done one
 </span>
 <span data-rw-start="462.08" data-rw-transcript-version="2">
 back and forth, and my context window was
 </span>
 <span data-rw-start="464.319" data-rw-transcript-version="2">
 Already 15% full. That's because you
 </span>
 <span data-rw-start="467.12" data-rw-transcript-version="2">
 have the system prompt the agents MD you
 </span>
 <span data-rw-start="469.28" data-rw-transcript-version="2">
 have maybe like the descriptions of all
 </span>
 <span data-rw-start="470.8" data-rw-transcript-version="2">
 of your context interfaces. So you want
 </span>
 <span data-rw-start="473.039" data-rw-transcript-version="2">
 to kind of like monitor this and see
 </span>
 <span data-rw-start="474.879" data-rw-transcript-version="2">
 kind of like balance your setup of how
 </span>
 <span data-rw-start="476.56" data-rw-transcript-version="2">
 much stuff you're putting into the um
 </span>
 <span data-rw-start="478.96" data-rw-transcript-version="2">
 context window because when there's
 </span>
 <span data-rw-start="480.72" data-rw-transcript-version="2">
 irrelevant stuff in there, it also can
 </span>
 <span data-rw-start="482.56" data-rw-transcript-version="2">
 confuse the model, right?
 </span>
</p>
<p>
 <span data-rw-start="485.759" data-rw-transcript-version="2">
 And then maybe as the last technique
 </span>
 <span data-rw-start="487.44" data-rw-transcript-version="2">
 that has really uh unlocked a lot of
 </span>
 <span data-rw-start="490.08" data-rw-transcript-version="2">
 stuff that I'll talk about in a little
 </span>
 <span data-rw-start="491.52" data-rw-transcript-version="2">
 bit as well in context engineering is
 </span>
 <span data-rw-start="493.919" data-rw-transcript-version="2">
 the idea of sub agents. So where you
 </span>
 <span data-rw-start="496" data-rw-transcript-version="2">
 have like a main conversation and it
 </span>
 <span data-rw-start="498.24" data-rw-transcript-version="2">
 spawns off little um sub agents that have
 </span>
 <span data-rw-start="501.759" data-rw-transcript-version="2">
 their own context window. So a really
 </span>
 <span data-rw-start="504" data-rw-transcript-version="2">
 good example of that, that a lot of
 </span>
 <span data-rw-start="505.84" data-rw-transcript-version="2">
 coding agents are doing now, I don’t know
 </span>
 <span data-rw-start="507.68" data-rw-transcript-version="2">
 if you can read it in the back, there’s a
 </span>
 <span data-rw-start="509.039" data-rw-transcript-version="2">
 screenshot here of cloud code, and it
 </span>
 <span data-rw-start="511.039" data-rw-transcript-version="2">
 says running to explore agents. So, um, in
 </span>
 <span data-rw-start="514.719" data-rw-transcript-version="2">
 the beginning of a session, when the
 </span>
 <span data-rw-start="516.32" data-rw-transcript-version="2">
 agents, uh, kind of research what's in
 </span>
</p>
<p>
 <span data-rw-start="518.24" data-rw-transcript-version="2">
 Your codebase, which often takes a lot of
 </span>
 <span data-rw-start="520.24" data-rw-transcript-version="2">
 tokens because they have to read a lot
 </span>
 <span data-rw-start="522" data-rw-transcript-version="2">
 of files, and then when you spawn that
 </span>
 <span data-rw-start="524.159" data-rw-transcript-version="2">
 off as a separate agent that just
 </span>
 <span data-rw-start="525.76" data-rw-transcript-version="2">
 reports the results back to the main
 </span>
 <span data-rw-start="527.76" data-rw-transcript-version="2">
 session, then you can potentially like
 </span>
 <span data-rw-start="530.399" data-rw-transcript-version="2">
 save a lot of tokens that you don't need
 </span>
 <span data-rw-start="532.08" data-rw-transcript-version="2">
 in your uh main uh conversation. And
 </span>
 <span data-rw-start="536.32" data-rw-transcript-version="2">
 yeah, so sub-agents are also really
 </span>
 <span data-rw-start="538.08" data-rw-transcript-version="2">
 important when you want to do more
 </span>
 <span data-rw-start="539.6" data-rw-transcript-version="2">
 longer-running workflows that you don't
 </span>
 <span data-rw-start="541.76" data-rw-transcript-version="2">
 just want to do in one big context
 </span>
 <span data-rw-start="543.36" data-rw-transcript-version="2">
 window.
 </span>
</p>
<p>
 <span data-rw-start="545.36" data-rw-transcript-version="2">
 So, as technical leaders in the context
 </span>
 <span data-rw-start="547.2" data-rw-transcript-version="2">
 of engineering space, ask yourself, you
 </span>
 <span data-rw-start="549.04" data-rw-transcript-version="2">
 know, what coding conventions you want
 </span>
 <span data-rw-start="550.959" data-rw-transcript-version="2">
 to amplify and maybe put into
 </span>
 <span data-rw-start="553.2" data-rw-transcript-version="2">
 skills that teams can use. Um, what
 </span>
 <span data-rw-start="556.16" data-rw-transcript-version="2">
 workflows can you build for
 </span>
 <span data-rw-start="558" data-rw-transcript-version="2">
 modernization initiatives? So, migration
 </span>
 <span data-rw-start="560" data-rw-transcript-version="2">
 is actually a really, really good use
 </span>
 <span data-rw-start="561.68" data-rw-transcript-version="2">
 case for generative AI with the human in
 </span>
 <span data-rw-start="564.48" data-rw-transcript-version="2">
 the loop, right? But it can like really
 </span>
 <span data-rw-start="566.399" data-rw-transcript-version="2">
 help with this. I was recently, uh, uh
 </span>
 <span data-rw-start="568.88" data-rw-transcript-version="2">
 talking to a colleague who was working for a.
 </span>
</p>
<p>
 <span data-rw-start="570.88" data-rw-transcript-version="2">
 Client, where they had, uh, she said,
 </span>
 <span data-rw-start="573.6" data-rw-transcript-version="2">
 thousands of, uh, team city pipelines that
 </span>
 <span data-rw-start="576.56" data-rw-transcript-version="2">
 they all wanted to migrate to GitHub, uh,
 </span>
 <span data-rw-start="578.64" data-rw-transcript-version="2">
 actions, and she was working on a
 </span>
 <span data-rw-start="580.399" data-rw-transcript-version="2">
 workflow how generative AI can help them
 </span>
 <span data-rw-start="582.56" data-rw-transcript-version="2">
 migrate and map all of those things. Um,
 </span>
 <span data-rw-start="585.44" data-rw-transcript-version="2">
 What tools should be available in your
 </span>
 <span data-rw-start="587.279" data-rw-transcript-version="2">
 organization that agents can use? So, are
 </span>
 <span data-rw-start="589.36" data-rw-transcript-version="2">
 there maybe, like, custom CLIs for very
 </span>
 <span data-rw-start="592.24" data-rw-transcript-version="2">
 common things that you would
 </span>
 <span data-rw-start="594.08" data-rw-transcript-version="2">
 need, or what MCP servers make sense, and
 </span>
 <span data-rw-start="596.64" data-rw-transcript-version="2">
 so on. Um, what are practices you want to
 </span>
 <span data-rw-start="599.6" data-rw-transcript-version="2">
 amplify? So, in the past, my favorite
 </span>
</p>
<p>
 <span data-rw-start="601.76" data-rw-transcript-version="2">
 examples have always been, like, can you
 </span>
 <span data-rw-start="603.68" data-rw-transcript-version="2">
 have a prompt that helps people write
 </span>
 <span data-rw-start="605.36" data-rw-transcript-version="2">
 better architecture decision records, or
 </span>
 <span data-rw-start="607.279" data-rw-transcript-version="2">
 can you have a prompt that makes threat
 </span>
 <span data-rw-start="609.44" data-rw-transcript-version="2">
 modeling less daunting and makes it
 </span>
 <span data-rw-start="610.88" data-rw-transcript-version="2">
 easier to start with. Those can
 </span>
 <span data-rw-start="612.48" data-rw-transcript-version="2">
 also be skills that people can, like, can use
 </span>
 <span data-rw-start="614.8" data-rw-transcript-version="2">
 in their, um, coding agents. Um, this one
 </span>
 <span data-rw-start="618.72" data-rw-transcript-version="2">
 is kind of like yellow because, like,
 </span>
 <span data-rw-start="620.64" data-rw-transcript-version="2">
 versioning and distribution and stuff,
 </span>
 <span data-rw-start="622.32" data-rw-transcript-version="2">
 like that, there's still, like, a lot of
 </span>
 <span data-rw-start="624.56" data-rw-transcript-version="2">
 open questions about these things.
 </span>
</p>
<p>
 <span data-rw-start="627.04" data-rw-transcript-version="2">
 Right? And also, is it making things
 </span>
 <span data-rw-start="628.56" data-rw-transcript-version="2">
 better or worse? So, it's kind of
 </span>
 <span data-rw-start="630.079" data-rw-transcript-version="2">
 context engineering in scare quotes.
 </span>
 <span data-rw-start="632.56" data-rw-transcript-version="2">
 Right? Is this really engineering when
 </span>
 <span data-rw-start="634.8" data-rw-transcript-version="2">
 we're not versioning it when we don't
 </span>
 <span data-rw-start="636.64" data-rw-transcript-version="2">
 know if we're making it better or worse.
 </span>
 <span data-rw-start="638.64" data-rw-transcript-version="2">
 Right? There are evals coming out
 </span>
 <span data-rw-start="641.6" data-rw-transcript-version="2">
 now in some places, like in this skills
 </span>
 <span data-rw-start="643.76" data-rw-transcript-version="2">
 registry. Tesla, they have evals now.
 </span>
 <span data-rw-start="646.24" data-rw-transcript-version="2">
 Anthropic has also just released
 </span>
 <span data-rw-start="647.839" data-rw-transcript-version="2">
 something to do with eval, so kind of like, is
 </span>
 <span data-rw-start="650.399" data-rw-transcript-version="2">
 it better or worse, kind of testing for
 </span>
 <span data-rw-start="652.16" data-rw-transcript-version="2">
 skills? So, there's a lot still to do to
 </span>
 <span data-rw-start="654.64" data-rw-transcript-version="2">
 mature this. But, uh, even at this stage,
 </span>
 <span data-rw-start="657.44" data-rw-transcript-version="2">
 you can take advantage of, uh, some
 </span>
 <span data-rw-start="659.36" data-rw-transcript-version="2">
 of these things quite well already.
 </span>
 <span data-rw-start="666.32" data-rw-transcript-version="2">
 So, this more sophisticated context
 </span>
 <span data-rw-start="668.32" data-rw-transcript-version="2">
 engineering, in combination with models,
 </span>
 <span data-rw-start="670.32" data-rw-transcript-version="2">
 getting a lot better, right? Probably
 </span>
 <span data-rw-start="672.16" data-rw-transcript-version="2">
 most of you have heard about, um, the jump
 </span>
 <span data-rw-start="675.04" data-rw-transcript-version="2">
 that, uh, the models have done recently,
 </span>
 <span data-rw-start="677.76" data-rw-transcript-version="2">
 again at coding, with the newest, uh,
 </span>
 <span data-rw-start="679.76" data-rw-transcript-version="2">
 version of the Opus model and the newest
 </span>
 <span data-rw-start="682.32" data-rw-transcript-version="2">
 version of the GPT Codex model. So,
 </span>
 <span data-rw-start="684.88" data-rw-transcript-version="2">
 those things, in combination, have now led.
 </span>
</p>
<p>
 <span data-rw-start="687.36" data-rw-transcript-version="2">
 To like a trend of people trying like
 </span>
 <span data-rw-start="690" data-rw-transcript-version="2">
 more agent autonomy with less human
 </span>
 <span data-rw-start="692.64" data-rw-transcript-version="2">
 supervision, right? And by supervision I
 </span>
 <span data-rw-start="695.36" data-rw-transcript-version="2">
 mean, like, supervised. I sit in
 </span>
 <span data-rw-start="697.279" data-rw-transcript-version="2">
 front of it. I actually like intervene,
 </span>
 <span data-rw-start="699.2" data-rw-transcript-version="2">
 I like to steer. I, uh, maybe like keep
 </span>
 <span data-rw-start="702.56" data-rw-transcript-version="2">
 saying, "Yes, you're allowed to execute
 </span>
 <span data-rw-start="704" data-rw-transcript-version="2">
 this command." "No, you're not allowed to
 </span>
 <span data-rw-start="705.68" data-rw-transcript-version="2">
 execute that command." Right? In
 </span>
 <span data-rw-start="707.68" data-rw-transcript-version="2">
 comparison to unsupervised, where this is
 </span>
 <span data-rw-start="710.24" data-rw-transcript-version="2">
 like a screenshot from OpenAI, uh, codecs
 </span>
 <span data-rw-start="713.76" data-rw-transcript-version="2">
 from their, uh, cloud interface. So, where
 </span>
 <span data-rw-start="716.24" data-rw-transcript-version="2">
 you really like put a prompt in there
 </span>
 <span data-rw-start="717.92" data-rw-transcript-version="2">
 and just send it off by itself for 20,
 </span>
 <span data-rw-start="721.279" data-rw-transcript-version="2">
 minutes or so. And these, um, kind of
 </span>
 <span data-rw-start="724.32" data-rw-transcript-version="2">
 platforms have also started popping up a
 </span>
 <span data-rw-start="727.279" data-rw-transcript-version="2">
 lot over the past year, right? So, just
 </span>
 <span data-rw-start="729.44" data-rw-transcript-version="2">
 recently, this is a, um, a screenshot from
 </span>
 <span data-rw-start="732.639" data-rw-transcript-version="2">
 a platform called Warp, uh, Oz, that was
 </span>
 <span data-rw-start="735.2" data-rw-transcript-version="2">
 just recently released. And all of the
 </span>
 <span data-rw-start="737.12" data-rw-transcript-version="2">
 big coding, uh, agent products now
 </span>
 <span data-rw-start="740.16" data-rw-transcript-version="2">
 actually also have a cloud version,
 </span>
 <span data-rw-start="741.6" data-rw-transcript-version="2">
 right? So, this is like cursor for
 </span>
 <span data-rw-start="744.24" data-rw-transcript-version="2">
 example, this is cloud code. So, for all
 </span>
 <span data-rw-start="747.04" data-rw-transcript-version="2">
 of them, you can now say, "Not just do it".
 </span>
</p>
<p>
 <span data-rw-start="748.88" data-rw-transcript-version="2">
 Like on your machine, but say do this in
 </span>
 <span data-rw-start="751.36" data-rw-transcript-version="2">
 this, um, cloud environment, right? And, um,
 </span>
 <span data-rw-start="756.72" data-rw-transcript-version="2">
 this has also been, uh, pushed forward by
 </span>
 <span data-rw-start="761.6" data-rw-transcript-version="2">
 one of the attributes of the CLIs that
 </span>
 <span data-rw-start="764.32" data-rw-transcript-version="2">
 have really gotten traction over the
 </span>
 <span data-rw-start="766.079" data-rw-transcript-version="2">
 past year as well, uh, starting with
 </span>
 <span data-rw-start="767.76" data-rw-transcript-version="2">
 clawed code. Now, all of the other, uh,
 </span>
 <span data-rw-start="771.36" data-rw-transcript-version="2">
 coding agent products have started
 </span>
 <span data-rw-start="773.12" data-rw-transcript-version="2">
 copying that as well. They also all have
 </span>
 <span data-rw-start="774.639" data-rw-transcript-version="2">
 CLIs, and one of the attributes of those
 </span>
 <span data-rw-start="776.88" data-rw-transcript-version="2">
 is that they're headless, right? So, you
 </span>
 <span data-rw-start="778.56" data-rw-transcript-version="2">
 can run, uh, you can run them in headless
 </span>
 <span data-rw-start="780.56" data-rw-transcript-version="2">
 mode. So, it also makes it easier to
 </span>
 <span data-rw-start="782.959" data-rw-transcript-version="2">
 start experimenting with integrating
 </span>
 <span data-rw-start="784.48" data-rw-transcript-version="2">
 these into your pipelines, if you want
 </span>
 <span data-rw-start="786.079" data-rw-transcript-version="2">
 to. So, it's like a more natural building
 </span>
 <span data-rw-start="788.079" data-rw-transcript-version="2">
 block of what we're already used to. So,
 </span>
 <span data-rw-start="789.76" data-rw-transcript-version="2">
 here, I was, uh, integrating clot code into
 </span>
 <span data-rw-start="792.24" data-rw-transcript-version="2">
 a GitHub actions, um, pipeline.
 </span>
</p>
<p>
 <span data-rw-start="795.839" data-rw-transcript-version="2">
 Maybe just a note about this, like,
 </span>
 <span data-rw-start="797.36" data-rw-transcript-version="2">
 terminal user interface versus graphical
 </span>
 <span data-rw-start="799.36" data-rw-transcript-version="2">
 user interface, because I think there's a
 </span>
 <span data-rw-start="800.959" data-rw-transcript-version="2">
 lot of talk about how cloud code is so
 </span>
 <span data-rw-start="803.68" data-rw-transcript-version="2">
 uh, um, successful, and people don't even
 </span>
 <span data-rw-start="806.639" data-rw-transcript-version="2">
 open their IDEs anymore.
 </span>
</p>
<p>
 <span data-rw-start="809.36" data-rw-transcript-version="2">
 I think that Claude code in part is so
 </span>
 <span data-rw-start="811.04" data-rw-transcript-version="2">
 successful because of how good it is
 </span>
 <span data-rw-start="812.639" data-rw-transcript-version="2">
 under the hood, and uh, um, so I know you
 </span>
 <span data-rw-start="816.72" data-rw-transcript-version="2">
 probably can't read the details, but so
 </span>
 <span data-rw-start="818.16" data-rw-transcript-version="2">
 the bottom right is basically a
 </span>
 <span data-rw-start="819.68" data-rw-transcript-version="2">
 screenshot of cursor, right, and I
 </span>
 <span data-rw-start="821.92" data-rw-transcript-version="2">
 actually still prefer that graphical
 </span>
 <span data-rw-start="823.92" data-rw-transcript-version="2">
 user interface, and cursor is also quite
 </span>
 <span data-rw-start="825.839" data-rw-transcript-version="2">
 good under the hood, so I’m not like 100%
 </span>
 <span data-rw-start="828.24" data-rw-transcript-version="2">
 convinced yet that it’s all about that
 </span>
 <span data-rw-start="829.76" data-rw-transcript-version="2">
 terminal user experience. I just think
 </span>
 <span data-rw-start="832.16" data-rw-transcript-version="2">
 like Claude code is really cloud code is
 </span>
 <span data-rw-start="834.48" data-rw-transcript-version="2">
 really good, and there will still be a
 </span>
 <span data-rw-start="836.16" data-rw-transcript-version="2">
 preference of people, which kind of
 </span>
 <span data-rw-start="837.6" data-rw-transcript-version="2">
 visual experience they, um, they
 </span>
 <span data-rw-start="839.76" data-rw-transcript-version="2">
 prefer, as long as what’s happening
 </span>
 <span data-rw-start="841.6" data-rw-transcript-version="2">
 inside of the agent is good enough
 </span>
 <span data-rw-start="843.6" data-rw-transcript-version="2">
 for what they want to do.
 </span>
</p>
<p>
 <span data-rw-start="845.839" data-rw-transcript-version="2">
 So, as part of this, a familiar beast
 </span>
 <span data-rw-start="848.32" data-rw-transcript-version="2">
 rears its head, which is like kind of dev
 </span>
 <span data-rw-start="850.399" data-rw-transcript-version="2">
 sandboxes, right, or all the challenges
 </span>
 <span data-rw-start="852.56" data-rw-transcript-version="2">
 that we also have when we run things in
 </span>
 <span data-rw-start="854.56" data-rw-transcript-version="2">
 a pipeline, right, so we have to have
 </span>
 <span data-rw-start="857.92" data-rw-transcript-version="2">
 everything installed that the agent
 </span>
 <span data-rw-start="859.76" data-rw-transcript-version="2">
 needs to, uh, to run things, right, so all
 </span>
 <span data-rw-start="861.92" data-rw-transcript-version="2">
 The dev tools, all the language compilers,
 </span>
 <span data-rw-start="864.32" data-rw-transcript-version="2">
 and so on, we have to think about things like out of memory,
 </span>
 <span data-rw-start="866.8" data-rw-transcript-version="2">
 errors and stuff like that, right? We have
 </span>
 <span data-rw-start="868.48" data-rw-transcript-version="2">
 to think about internet access in even
 </span>
 <span data-rw-start="870.399" data-rw-transcript-version="2">
 more different ways than we have to with
 </span>
 <span data-rw-start="872.88" data-rw-transcript-version="2">
 our, you know, pipelines before, where
 </span>
 <span data-rw-start="874.8" data-rw-transcript-version="2">
 internet access was mostly about
 </span>
 <span data-rw-start="877.279" data-rw-transcript-version="2">
 installing things. But now it's also
 </span>
 <span data-rw-start="878.639" data-rw-transcript-version="2">
 about like, do I want to allow the agent
 </span>
 <span data-rw-start="880.88" data-rw-transcript-version="2">
 to do web research and potentially get
 </span>
 <span data-rw-start="882.72" data-rw-transcript-version="2">
 prompt injected, right? So, uh, we have to
 </span>
 <span data-rw-start="887.279" data-rw-transcript-version="2">
 think about, like, internet access, yes or
 </span>
 <span data-rw-start="889.44" data-rw-transcript-version="2">
 no? When should it have internet access,
 </span>
 <span data-rw-start="891.68" data-rw-transcript-version="2">
 and, and where too? And this is also true
 </span>
 <span data-rw-start="895.36" data-rw-transcript-version="2">
 of course, for local sandboxes, which I'll
 </span>
 <span data-rw-start="897.839" data-rw-transcript-version="2">
 get to in a few minutes as well.
 </span>
</p>
<p>
 <span data-rw-start="901.04" data-rw-transcript-version="2">
 So, a short intermission for this, uh,
 </span>
 <span data-rw-start="903.68" data-rw-transcript-version="2">
 autonomy hype. So, the, the hype duo, so
 </span>
 <span data-rw-start="906.959" data-rw-transcript-version="2">
 to say is, um, got like a lot of new
 </span>
 <span data-rw-start="912.639" data-rw-transcript-version="2">
 starting attention, let’s say, with this
 </span>
 <span data-rw-start="914.399" data-rw-transcript-version="2">
 uh, blog post by Steve Yagi. Welcome to
 </span>
 <span data-rw-start="916.56" data-rw-transcript-version="2">
 Gas Town, which maybe, like, lots of you
 </span>
 <span data-rw-start="918.32" data-rw-transcript-version="2">
 have read. Yeah, I see some hands. Yeah.
 </span>
</p>
<p>
 <span data-rw-start="924" data-rw-transcript-version="2">
 Article where he's saying, okay, this is
 </span>
 <span data-rw-start="926.32" data-rw-transcript-version="2">
 stages of development, like when
 </span>
 <span data-rw-start="928.72" data-rw-transcript-version="2">
 you're at stage six, you have three cloned
 </span>
 <span data-rw-start="930.8" data-rw-transcript-version="2">
 code instances open at the same time.
 </span>
 <span data-rw-start="932.56" data-rw-transcript-version="2">
 When you're at stage seven, you have, like,
 </span>
 <span data-rw-start="934.16" data-rw-transcript-version="2">
 ten of them, and stage eight is this, like,
 </span>
 <span data-rw-start="936.639" data-rw-transcript-version="2">
 big thing that things like GPT are
 </span>
 <span data-rw-start="939.279" data-rw-transcript-version="2">
 doing, which, um, I usually call, like, agent
 </span>
 <span data-rw-start="942.079" data-rw-transcript-version="2">
 swarms, right? So, it's this idea of
 </span>
 <span data-rw-start="944.32" data-rw-transcript-version="2">
 throwing as many agents as you can at
 </span>
 <span data-rw-start="946.56" data-rw-transcript-version="2">
 the wall and seeing what sticks, kind of
 </span>
 <span data-rw-start="948.32" data-rw-transcript-version="2">
 like a brute-force, um, uh, approach. Um
 </span>
 <span data-rw-start="953.279" data-rw-transcript-version="2">
 I kind of think of it as, like, with large
 </span>
 <span data-rw-start="955.199" data-rw-transcript-version="2">
 language models, we threw all of this
 </span>
 <span data-rw-start="956.639" data-rw-transcript-version="2">
 data at a model architecture, and we had
 </span>
 <span data-rw-start="960.16" data-rw-transcript-version="2">
 all of these emergent capabilities that
 </span>
 <span data-rw-start="962.32" data-rw-transcript-version="2">
 even the makers didn't really expect. And
 </span>
 <span data-rw-start="964.399" data-rw-transcript-version="2">
 I think of agent swarms almost as, like,
 </span>
 <span data-rw-start="966.24" data-rw-transcript-version="2">
 what if we throw lots of agents out,
 </span>
 <span data-rw-start="968" data-rw-transcript-version="2">
 there, and they just all coordinate with
 </span>
 <span data-rw-start="969.519" data-rw-transcript-version="2">
 each other, and there are dozens or hundreds
 </span>
 <span data-rw-start="971.279" data-rw-transcript-version="2">
 of them. Um, what will happen? Will we
 </span>
 <span data-rw-start="973.6" data-rw-transcript-version="2">
 also get some emerging capabilities?
 </span>
</p>
<p>
 <span data-rw-start="976.24" data-rw-transcript-version="2">
 There were these two experiments by,
 </span>
 <span data-rw-start="977.68" data-rw-transcript-version="2">
 Cursor and Anthropic recently, that also
 </span>
 <span data-rw-start="979.92" data-rw-transcript-version="2">
 Got a lot of attention and made some
 </span>
 <span data-rw-start="981.92" data-rw-transcript-version="2">
 people really nervous. So Cursor had, uh
 </span>
 <span data-rw-start="985.279" data-rw-transcript-version="2">
 like, lots of agents like that running
 </span>
 <span data-rw-start="986.8" data-rw-transcript-version="2">
 for a week to build a browser, and
 </span>
 <span data-rw-start="989.12" data-rw-transcript-version="2">
 Anthropic had lots of agents running for
 </span>
 <span data-rw-start="991.04" data-rw-transcript-version="2">
 a while to build a C compiler. The
 </span>
 <span data-rw-start="993.44" data-rw-transcript-version="2">
 interesting thing about these
 </span>
 <span data-rw-start="994.399" data-rw-transcript-version="2">
 experiments is that both of these use
 </span>
 <span data-rw-start="996.8" data-rw-transcript-version="2">
 cases, browser and C compiler, have very
 </span>
 <span data-rw-start="999.36" data-rw-transcript-version="2">
 very good specifications, and in the case
 </span>
 <span data-rw-start="1002.079" data-rw-transcript-version="2">
 of the C compiler in particular, very
 </span>
 <span data-rw-start="1004.399" data-rw-transcript-version="2">
 good test suites already out there on
 </span>
 <span data-rw-start="1006" data-rw-transcript-version="2">
 the internet. So, the specification is there
 </span>
 <span data-rw-start="1008.56" data-rw-transcript-version="2">
 and a really good safety net for the
 </span>
 <span data-rw-start="1010.32" data-rw-transcript-version="2">
 functionality. So, at least Cursor is
 </span>
 <span data-rw-start="1013.04" data-rw-transcript-version="2">
 also explicitly saying that’s why they
 </span>
 <span data-rw-start="1014.56" data-rw-transcript-version="2">
 chose this use case. So I don’t think
 </span>
 <span data-rw-start="1016.399" data-rw-transcript-version="2">
 that makes the experiments like useless
 </span>
 <span data-rw-start="1018.8" data-rw-transcript-version="2">
 or something, but it’s just like
 </span>
 <span data-rw-start="1020.16" data-rw-transcript-version="2">
 something to keep in mind, right? That
 </span>
 <span data-rw-start="1021.759" data-rw-transcript-version="2">
 it wasn’t just magically getting
 </span>
 <span data-rw-start="1023.6" data-rw-transcript-version="2">
 one prompt to build something, and then
 </span>
 <span data-rw-start="1025.12" data-rw-transcript-version="2">
 it, uh, then it did it. But there’s lots
 </span>
 <span data-rw-start="1027.28" data-rw-transcript-version="2">
 of specifications out there already.
 </span>
</p>
<p>
 <span data-rw-start="1030.319" data-rw-transcript-version="2">
 Um, setting up tools like Gas Town or
 </span>
 <span data-rw-start="1032.64" data-rw-transcript-version="2">
 This Cloudflow tool is sometimes like a little bit scary, and it also sometimes eats a lot of tokens, of course. So, if you just want to dip your toes in and not just go
 </span>
 <span data-rw-start="1035.039" data-rw-transcript-version="2">
 into this like futuristic swarm
 </span>
 <span data-rw-start="1037.919" data-rw-transcript-version="2">
 direction, but just try to run something
 </span>
 <span data-rw-start="1039.439" data-rw-transcript-version="2">
 with multiple agents, you can also try
 </span>
 <span data-rw-start="1042.079" data-rw-transcript-version="2">
 this new feature in cloud code called
 </span>
 <span data-rw-start="1044.16" data-rw-transcript-version="2">
 agent teams, where you can see a little
 </span>
 <span data-rw-start="1046.079" data-rw-transcript-version="2">
 bit of, like, some of the
 </span>
 <span data-rw-start="1048.24" data-rw-transcript-version="2">
 coordination that the agent is trying to
 </span>
 <span data-rw-start="1050.16" data-rw-transcript-version="2">
 do to kind of determine what do I run in
 </span>
 <span data-rw-start="1052.16" data-rw-transcript-version="2">
 parallel, what do I run sequentially. So,
 </span>
 <span data-rw-start="1053.36" data-rw-transcript-version="2">
 if you just want to like experiment with
 </span>
 <span data-rw-start="1055.28" data-rw-transcript-version="2">
 that a little bit, then that’s maybe a safer and easier way than with these
 </span>
 <span data-rw-start="1057.52" data-rw-transcript-version="2">
 super big machines. [snorts]
 </span>
 <span data-rw-start="1070.64" data-rw-transcript-version="2">
 So, I say, back to the present now,
 </span>
 <span data-rw-start="1075.6" data-rw-transcript-version="2">
 because I would say that these things
 </span>
 <span data-rw-start="1076.88" data-rw-transcript-version="2">
 are really, like, probably none of the
 </span>
 <span data-rw-start="1078.72" data-rw-transcript-version="2">
 organizations that you work for, it makes
 </span>
 <span data-rw-start="1080.16" data-rw-transcript-version="2">
 sense to experiment with, uh, swarms, um,
 </span>
 <span data-rw-start="1083.36" data-rw-transcript-version="2">
 like that yet, or ever. Let's see.
 </span>
</p>
<p>
 <span data-rw-start="1087.312" data-rw-transcript-version="2">
 [laughter] So, for the less supervision,
 </span>
 <span data-rw-start="1089.44" data-rw-transcript-version="2">
 more autonomy part, as technical leaders,
 </span>
 <span data-rw-start="1091.52" data-rw-transcript-version="2">
 I think maybe what you can ask yourself
 </span>
 <span data-rw-start="1093.44" data-rw-transcript-version="2">
 if you want to like, uh, uh, start looking
 </span>
 <span data-rw-start="1095.919" data-rw-transcript-version="2">
 if this makes sense for organization, for
 </span>
 <span data-rw-start="1097.679" data-rw-transcript-version="2">
 your organization is one, maybe, like,
 </span>
 <span data-rw-start="1099.2" data-rw-transcript-version="2">
 where do you want to experiment with
 </span>
 <span data-rw-start="1100.559" data-rw-transcript-version="2">
 these cloud agents or with, like, um, uh,
 </span>
 <span data-rw-start="1104.559" data-rw-transcript-version="2">
 more autonomy, less supervision. So, and
 </span>
 <span data-rw-start="1106.96" data-rw-transcript-version="2">
 that will also make you reflect, like, how
 </span>
 <span data-rw-start="1110" data-rw-transcript-version="2">
 safe is actually the environment in our
 </span>
 <span data-rw-start="1111.919" data-rw-transcript-version="2">
 organization, right? Like, what is the
 </span>
 <span data-rw-start="1113.84" data-rw-transcript-version="2">
 safety net here for the agent? That you
 </span>
 <span data-rw-start="1115.76" data-rw-transcript-version="2">
 know, if you feel unsure about it,
 </span>
</p>
<p>
 <span data-rw-start="1117.44" data-rw-transcript-version="2">
 you can try it with smaller things like
 </span>
 <span data-rw-start="1118.88" data-rw-transcript-version="2">
 cleaning up feature toggles and stuff
 </span>
 <span data-rw-start="1120.32" data-rw-transcript-version="2">
 like that, and just see, uh, um, what
 </span>
 <span data-rw-start="1122.64" data-rw-transcript-version="2">
 happens. Uh, it's definitely become
 </span>
 <span data-rw-start="1125.2" data-rw-transcript-version="2">
 because of all of these platforms a lot
 </span>
 <span data-rw-start="1127.84" data-rw-transcript-version="2">
 easier to try this, uh, to try this
 </span>
 <span data-rw-start="1130.4" data-rw-transcript-version="2">
 out. Um, yeah, and how do you help your
 </span>
 <span data-rw-start="1133.28" data-rw-transcript-version="2">
 teams gauge the appropriate level of
 </span>
 <span data-rw-start="1135.36" data-rw-transcript-version="2">
 supervision for a particular task,
 </span>
 <span data-rw-start="1137.28" data-rw-transcript-version="2">
 right? When you don't want them to like,
 </span>
 <span data-rw-start="1139.28" data-rw-transcript-version="2">
 maybe build full features in this
 </span>
 <span data-rw-start="1141.6" data-rw-transcript-version="2">
 autonomous mode, but like, how do you
 </span>
 <span data-rw-start="1143.28" data-rw-transcript-version="2">
 gauge that in general?
 </span>
</p>
<p>
 <span data-rw-start="1147.039" data-rw-transcript-version="2">
 Found myself doing a lot more on all
 </span>
 <span data-rw-start="1150.16" data-rw-transcript-version="2">
 kinds of micro and macro levels is like
 </span>
 <span data-rw-start="1152" data-rw-transcript-version="2">
 little risk assessments of when I use AI
 </span>
 <span data-rw-start="1154.88" data-rw-transcript-version="2">
 and also like how much review I apply to
 </span>
 <span data-rw-start="1157.44" data-rw-transcript-version="2">
 it. And a risk assessment is always in
 </span>
 <span data-rw-start="1159.84" data-rw-transcript-version="2">
 any situation a combination of three
 </span>
 <span data-rw-start="1161.679" data-rw-transcript-version="2">
 things: probability, impact, and
 </span>
 <span data-rw-start="1164.24" data-rw-transcript-version="2">
 detectability, right? So I think about
 </span>
 <span data-rw-start="1167.039" data-rw-transcript-version="2">
 what is the probability that AI gets it
 </span>
 <span data-rw-start="1169.84" data-rw-transcript-version="2">
 wrong, like does something that I don't
 </span>
 <span data-rw-start="1171.44" data-rw-transcript-version="2">
 want, and that’s usually reflecting
 </span>
 <span data-rw-start="1174.24" data-rw-transcript-version="2">
 on things like knowing my tool that I
 </span>
 <span data-rw-start="1177.76" data-rw-transcript-version="2">
 use, like cloud code or cursor, and also
 </span>
 <span data-rw-start="1180" data-rw-transcript-version="2">
 knowing the context, like do I even give
 </span>
 <span data-rw-start="1182" data-rw-transcript-version="2">
 the agent a chance to do what I want,
 </span>
 <span data-rw-start="1184.16" data-rw-transcript-version="2">
 like how, uh, how confident am I even
 </span>
 <span data-rw-start="1187.12" data-rw-transcript-version="2">
 in the level of requirements, and how
 </span>
 <span data-rw-start="1188.559" data-rw-transcript-version="2">
 much context do I give it? Then the
 </span>
</p>
<p>
 <span data-rw-start="1190.88" data-rw-transcript-version="2">
 second one is, like, what's the impact if
 </span>
 <span data-rw-start="1192.48" data-rw-transcript-version="2">
 AI gets something wrong? So that's
 </span>
 <span data-rw-start="1194.32" data-rw-transcript-version="2">
 obviously about the criticality of
 </span>
 <span data-rw-start="1196" data-rw-transcript-version="2">
 the use case, right? Is this proof of
 </span>
 <span data-rw-start="1198.48" data-rw-transcript-version="2">
 concept, or a spike, or is this something
 </span>
 <span data-rw-start="1200.32" data-rw-transcript-version="2">
 that I’m on call for at the weekend,
 </span>
 <span data-rw-start="1202.4" data-rw-transcript-version="2">
 and it's in the critical path of our
 </span>
 <span data-rw-start="1205.2" data-rw-transcript-version="2">
 Um, our business processes, right? And
 </span>
 <span data-rw-start="1207.52" data-rw-transcript-version="2">
 then the third one, detectability that
 </span>
 <span data-rw-start="1209.679" data-rw-transcript-version="2">
 AI got something wrong. So, I have to
 </span>
 <span data-rw-start="1211.44" data-rw-transcript-version="2">
 know my feedback loops, right? Not only
 </span>
 <span data-rw-start="1214.4" data-rw-transcript-version="2">
 did it get something wrong, but also how
 </span>
 <span data-rw-start="1216.24" data-rw-transcript-version="2">
 quickly will I notice, right? Like, will
 </span>
 <span data-rw-start="1218.559" data-rw-transcript-version="2">
 it be easy to test for me and see if it
 </span>
 <span data-rw-start="1221.12" data-rw-transcript-version="2">
 did what I wanted? And then, um, all of
 </span>
 <span data-rw-start="1224.799" data-rw-transcript-version="2">
 those things kind of like maybe
 </span>
 <span data-rw-start="1226.16" data-rw-transcript-version="2">
 determine which workflow I use, right?
 </span>
</p>
<p>
 <span data-rw-start="1228.24" data-rw-transcript-version="2">
 Do I just dump like a quick prompt in, or
 </span>
 <span data-rw-start="1230.24" data-rw-transcript-version="2">
 do I put more effort into what I tell, um,
 </span>
 <span data-rw-start="1232.799" data-rw-transcript-version="2">
 the agent? How much review do I apply?
 </span>
 <span data-rw-start="1235.679" data-rw-transcript-version="2">
 Like, again, the case of a proof of
 </span>
 <span data-rw-start="1237.679" data-rw-transcript-version="2">
 uncritical proof of concept, uh, that I
 </span>
 <span data-rw-start="1240.559" data-rw-transcript-version="2">
 know, uh, um, it's the type of thing that
 </span>
 <span data-rw-start="1243.76" data-rw-transcript-version="2">
 the agent is really good at. I might not
 </span>
 <span data-rw-start="1245.52" data-rw-transcript-version="2">
 look at a single line of code, but again,
 </span>
 <span data-rw-start="1247.52" data-rw-transcript-version="2">
 if it's other stuff, I apply at different
 </span>
 <span data-rw-start="1249.2" data-rw-transcript-version="2">
 levels of review. And it also might
 </span>
 <span data-rw-start="1252.4" data-rw-transcript-version="2">
 determine how long I let it go without
 </span>
 <span data-rw-start="1254.24" data-rw-transcript-version="2">
 supervision. Like, do I actually sit in
 </span>
 <span data-rw-start="1256.159" data-rw-transcript-version="2">
 front of it and look at every
 </span>
 <span data-rw-start="1257.6" data-rw-transcript-version="2">
 single response or not? Of course, I
 </span>
 <span data-rw-start="1260.32" data-rw-transcript-version="2">
 don't have this checklist on my desk.
 </span>
</p>
<p>
 <span data-rw-start="1262" data-rw-transcript-version="2">
 Like really academically think about it.
 </span>
 <span data-rw-start="1263.6" data-rw-transcript-version="2">
 Every time, but I've just felt myself
 </span>
 <span data-rw-start="1265.6" data-rw-transcript-version="2">
 getting more intuitive at doing
 </span>
 <span data-rw-start="1268.48" data-rw-transcript-version="2">
 this assessment over time, almost like a
 </span>
 <span data-rw-start="1270.799" data-rw-transcript-version="2">
 new skill to develop.
 </span>
</p>
<p>
 <span data-rw-start="1274.96" data-rw-transcript-version="2">
 And interestingly, I actually think that
 </span>
 <span data-rw-start="1276.96" data-rw-transcript-version="2">
 except for the one thing that I
 </span>
 <span data-rw-start="1279.52" data-rw-transcript-version="2">
 highlighted as yellow here, all of these
 </span>
 <span data-rw-start="1281.52" data-rw-transcript-version="2">
 things are actually things that are
 </span>
 <span data-rw-start="1283.039" data-rw-transcript-version="2">
 already skills that a good developer
 </span>
 <span data-rw-start="1284.559" data-rw-transcript-version="2">
 should have, right? Reflecting, being
 </span>
 <span data-rw-start="1286.559" data-rw-transcript-version="2">
 good at reflecting on the criticality of
 </span>
 <span data-rw-start="1288.48" data-rw-transcript-version="2">
 what we're doing, knowing our feedback
 </span>
 <span data-rw-start="1290.4" data-rw-transcript-version="2">
 loops, kind of reflecting on how much
 </span>
 <span data-rw-start="1293.6" data-rw-transcript-version="2">
 certainty and uncertainty we have.
 </span>
</p>
<p>
 <span data-rw-start="1295.919" data-rw-transcript-version="2">
 So the new thing that we need to develop is
 </span>
 <span data-rw-start="1298.159" data-rw-transcript-version="2">
 like knowing our AI tool and like kind
 </span>
 <span data-rw-start="1301.039" data-rw-transcript-version="2">
 of getting good at fe curating this
 </span>
 <span data-rw-start="1304.08" data-rw-transcript-version="2">
 context that I was talking about before,
 </span>
 <span data-rw-start="1306.159" data-rw-transcript-version="2">
 and this is something that you cannot
 </span>
 <span data-rw-start="1307.44" data-rw-transcript-version="2">
 learn from a book, right? You actually
 </span>
 <span data-rw-start="1308.88" data-rw-transcript-version="2">
 have to do it for a while. So especially
 </span>
 <span data-rw-start="1310.799" data-rw-transcript-version="2">
 as more experienced people, even if
 </span>
 <span data-rw-start="1313.12" data-rw-transcript-version="2">
 you're skeptical of this, right? You have
 </span>
 <span data-rw-start="1316.159" data-rw-transcript-version="2">
 to use this so that you can help the
 </span>
 <span data-rw-start="1317.76" data-rw-transcript-version="2">
 People who are less experienced than you
 </span>
 <span data-rw-start="1320.159" data-rw-transcript-version="2">
 like understand where it's good, where
 </span>
 <span data-rw-start="1322.159" data-rw-transcript-version="2">
 it's not good, like what new safety
 </span>
 <span data-rw-start="1324.32" data-rw-transcript-version="2">
 controls you need, and so on.
 </span>
</p>
<p>
 <span data-rw-start="1327.919" data-rw-transcript-version="2">
 So yeah, it's kind of like almost this
 </span>
 <span data-rw-start="1329.6" data-rw-transcript-version="2">
 probability and detectability part is
 </span>
 <span data-rw-start="1331.44" data-rw-transcript-version="2">
 also, uh, reflection on, you know, like a
 </span>
 <span data-rw-start="1334" data-rw-transcript-version="2">
 you have to be this tall to reduce
 </span>
 <span data-rw-start="1336.24" data-rw-transcript-version="2">
 supervision in the agents, right? Like
 </span>
 <span data-rw-start="1338.159" data-rw-transcript-version="2">
 what is your environment in your
 </span>
 <span data-rw-start="1339.679" data-rw-transcript-version="2">
 organization, like? How many feedback
 </span>
 <span data-rw-start="1341.36" data-rw-transcript-version="2">
 loops are there? How automated are they?
 </span>
 <span data-rw-start="1344" data-rw-transcript-version="2">
 Um, the probability that AI gets
 </span>
 <span data-rw-start="1346.24" data-rw-transcript-version="2">
 something wrong can also have to do with
 </span>
 <span data-rw-start="1347.919" data-rw-transcript-version="2">
 the quality of the existing code bases,
 </span>
 <span data-rw-start="1350.24" data-rw-transcript-version="2">
 that are there, right? We already heard, um,
 </span>
 <span data-rw-start="1352.64" data-rw-transcript-version="2">
 I think Kevin was mentioning it as well,
 </span>
 <span data-rw-start="1354.32" data-rw-transcript-version="2">
 like, AI amplifies, right? AI amplifies
 </span>
 <span data-rw-start="1357.2" data-rw-transcript-version="2">
 indiscriminately. So, um, it kind of like
 </span>
 <span data-rw-start="1360.24" data-rw-transcript-version="2">
 amplifies the environment it's in. So,
 </span>
 <span data-rw-start="1362.4" data-rw-transcript-version="2">
 this, um, helps you also on an
 </span>
 <span data-rw-start="1364.08" data-rw-transcript-version="2">
 organizational level, think about
 </span>
 <span data-rw-start="1365.52" data-rw-transcript-version="2">
 probability and detectability.
 </span>
 <span data-rw-start="1369.84" data-rw-transcript-version="2">
 But of course, with more autonomy, less
 </span>
 <span data-rw-start="1371.52" data-rw-transcript-version="2">
 supervision with this trend, like, uh.
 </span>
</p>
<p>
 <span data-rw-start="1374" data-rw-transcript-version="2">
 There's like other beasts that rear
 </span>
 <span data-rw-start="1376.559" data-rw-transcript-version="2">
 their heads, right? So, beware of uh
 </span>
 <span data-rw-start="1378.799" data-rw-transcript-version="2">
 security and uh cost, right? So the
 </span>
 <span data-rw-start="1381.679" data-rw-transcript-version="2">
 stories about security problems are
 </span>
 <span data-rw-start="1384.48" data-rw-transcript-version="2">
 starting to become more frequent. Um, one
 </span>
 <span data-rw-start="1387.44" data-rw-transcript-version="2">
 of the things is, for example, unwanted
 </span>
 <span data-rw-start="1389.28" data-rw-transcript-version="2">
 command execution, right? So, this is a
 </span>
 <span data-rw-start="1391.36" data-rw-transcript-version="2">
 combination of prompt injection and
 </span>
 <span data-rw-start="1395.039" data-rw-transcript-version="2">
 now, sorry, this kind of like line break.
 </span>
</p>
<p>
 <span data-rw-start="1396.64" data-rw-transcript-version="2">
 So, bypassing allow lists, right? So, um,
 </span>
 <span data-rw-start="1400.24" data-rw-transcript-version="2">
 I told you before, like, some, when you
 </span>
 <span data-rw-start="1402" data-rw-transcript-version="2">
 supervise, you actually sometimes say yes,
 </span>
 <span data-rw-start="1403.6" data-rw-transcript-version="2">
 you're allowed to execute this. No, you're
 </span>
 <span data-rw-start="1405.2" data-rw-transcript-version="2">
 not allowed to execute that. And, but you
 </span>
 <span data-rw-start="1407.28" data-rw-transcript-version="2">
 can set certain allow lists, and
 </span>
 <span data-rw-start="1408.88" data-rw-transcript-version="2">
 sometimes, there are weaknesses in these
 </span>
 <span data-rw-start="1410.559" data-rw-transcript-version="2">
 regular expressions or however they
 </span>
 <span data-rw-start="1412.32" data-rw-transcript-version="2">
 are implemented, that you can still, um, get
 </span>
 <span data-rw-start="1414.4" data-rw-transcript-version="2">
 around those. Um, the most recent story
 </span>
 <span data-rw-start="1418.08" data-rw-transcript-version="2">
 that I've heard, this was from—yeah, okay,
 </span>
 <span data-rw-start="1420.48" data-rw-transcript-version="2">
 March 5th. What do we have today? March
 </span>
 <span data-rw-start="1422.96" data-rw-transcript-version="2">
 10th. Yeah, so this is from five days ago. Um,
 </span>
 <span data-rw-start="1426.64" data-rw-transcript-version="2">
 this was about a GitHub issue, where
 </span>
 <span data-rw-start="1428.32" data-rw-transcript-version="2">
 there were basically instructions in the
 </span>
 <span data-rw-start="1430.799" data-rw-transcript-version="2">
 GitHub issue on an open-source project.
 </span>
</p>
<p>
 <span data-rw-start="1433.44" data-rw-transcript-version="2">
 That led to like a whole chain of attack
 </span>
 <span data-rw-start="1435.919" data-rw-transcript-version="2">
 that actually extracted the secret that
 </span>
 <span data-rw-start="1438.559" data-rw-transcript-version="2">
 was needed to push that package to the
 </span>
 <span data-rw-start="1440.88" data-rw-transcript-version="2">
 npm registry, and it was ultimately
 </span>
 <span data-rw-start="1443.2" data-rw-transcript-version="2">
 pushed to the registry with like a new
 </span>
 <span data-rw-start="1445.12" data-rw-transcript-version="2">
 post-install um command. Um,
 </span>
 <span data-rw-start="1449.12" data-rw-transcript-version="2">
 So, this is like a great example of the
 </span>
 <span data-rw-start="1452.24" data-rw-transcript-version="2">
 lethal trifecta. Can I ask you, has anyone heard
 </span>
 <span data-rw-start="1454.159" data-rw-transcript-version="2">
 of the lethal trifecta before?
 </span>
</p>
<p>
 <span data-rw-start="1456.88" data-rw-transcript-version="2">
 Uh, this is like, hopefully,
 </span>
 <span data-rw-start="1459.6" data-rw-transcript-version="2">
 after this, you all look this up and, uh,
 </span>
 <span data-rw-start="1462.32" data-rw-transcript-version="2">
 and internalize it. This is like a
 </span>
 <span data-rw-start="1464.48" data-rw-transcript-version="2">
 super, super helpful model to think about
 </span>
 <span data-rw-start="1466.88" data-rw-transcript-version="2">
 the, uh, the safety of agent, agentic
 </span>
 <span data-rw-start="1471.039" data-rw-transcript-version="2">
 use cases, right? So, Simon Willis wrote
 </span>
 <span data-rw-start="1473.36" data-rw-transcript-version="2">
 this up, and he says that when you have
 </span>
 <span data-rw-start="1474.799" data-rw-transcript-version="2">
 an agent that has these three attributes,
 </span>
 <span data-rw-start="1477.039" data-rw-transcript-version="2">
 or features, the agent has, uh, exposure to
 </span>
 <span data-rw-start="1480.08" data-rw-transcript-version="2">
 untrusted content. In this case, that was
 </span>
 <span data-rw-start="1482.96" data-rw-transcript-version="2">
 a GitHub issue, right? It’s untrusted
 </span>
 <span data-rw-start="1485.6" data-rw-transcript-version="2">
 content because anybody can create a
 </span>
 <span data-rw-start="1487.44" data-rw-transcript-version="2">
 GitHub issue. Um, the agent also has
 </span>
 <span data-rw-start="1490.4" data-rw-transcript-version="2">
 access to private data, and the agent has
 </span>
 <span data-rw-start="1492.799" data-rw-transcript-version="2">
 the ability to externally communicate.
 </span>
 <span data-rw-start="1494.88" data-rw-transcript-version="2">
 Then you have a problem, right? Because
 </span>
 <span data-rw-start="1496.96" data-rw-transcript-version="2">
 Then, yeah, somebody can just inject
 </span>
 <span data-rw-start="1499.76" data-rw-transcript-version="2">
 untrusted instructions. The agent might
 </span>
 <span data-rw-start="1502.559" data-rw-transcript-version="2">
 get, like, something private and
 </span>
 <span data-rw-start="1504.159" data-rw-transcript-version="2">
 externally communicate it. And by the
 </span>
 <span data-rw-start="1506.72" data-rw-transcript-version="2">
 way, like, when you think about a lot of
 </span>
 <span data-rw-start="1508.159" data-rw-transcript-version="2">
 the agentic use cases in the business
 </span>
 <span data-rw-start="1510" data-rw-transcript-version="2">
 world that we are being promised for the
 </span>
 <span data-rw-start="1512.159" data-rw-transcript-version="2">
 future, right? Many, many, many of those
 </span>
 <span data-rw-start="1514.559" data-rw-transcript-version="2">
 use cases have this conceptual problem.
 </span>
</p>
<p>
 <span data-rw-start="1516.96" data-rw-transcript-version="2">
 It's not a technical problem, right?
 </span>
 <span data-rw-start="1518.4" data-rw-transcript-version="2">
 It's a conceptual thing about a use
 </span>
 <span data-rw-start="1520.72" data-rw-transcript-version="2">
 case. So, yeah, will be interesting how
 </span>
 <span data-rw-start="1523.52" data-rw-transcript-version="2">
 we can even get around that for some of
 </span>
 <span data-rw-start="1525.12" data-rw-transcript-version="2">
 those use cases.
 </span>
</p>
<p>
 <span data-rw-start="1527.6" data-rw-transcript-version="2">
 And then, secondly, after security, uh, is
 </span>
 <span data-rw-start="1530.24" data-rw-transcript-version="2">
 cost, right? Uh, obviously, the the
 </span>
 <span data-rw-start="1532.159" data-rw-transcript-version="2">
 honeymoon is over, right? So, here's a
 </span>
 <span data-rw-start="1534.24" data-rw-transcript-version="2">
 quote from a keynote I heard at Craftcon
 </span>
 <span data-rw-start="1536.32" data-rw-transcript-version="2">
 in 2024, where the speaker said,
 </span>
 <span data-rw-start="1538.4" data-rw-transcript-version="2">
 "Generating 100 lines of code only
 </span>
 <span data-rw-start="1540.559" data-rw-transcript-version="2">
 costs about 12 cents. Compare that to a
 </span>
 <span data-rw-start="1543.52" data-rw-transcript-version="2">
 developer's salary, right? Then, fast
 </span>
 <span data-rw-start="1545.919" data-rw-transcript-version="2">
 forward to—uh, this is data from last
 </span>
 <span data-rw-start="1548.159" data-rw-transcript-version="2">
 summer. Uh, it's some website where
 </span>
 <span data-rw-start="1550.64" data-rw-transcript-version="2">
 people post their token usage with.
 </span>
</p>
<p>
 <span data-rw-start="1553.36" data-rw-transcript-version="2">
 Think, at the time it was cloud code. And
 </span>
 <span data-rw-start="1555.52" data-rw-transcript-version="2">
 this particular person that I have the
 </span>
 <span data-rw-start="1557.2" data-rw-transcript-version="2">
 screenshot for here was on average, uh,
 </span>
 <span data-rw-start="1559.76" data-rw-transcript-version="2">
 using $380 a day. That
 </span>
 <span data-rw-start="1564.4" data-rw-transcript-version="2">
 extrapolated to a salary is actually
 </span>
 <span data-rw-start="1566.64" data-rw-transcript-version="2">
 $91,200,
 </span>
 <span data-rw-start="1568.48" data-rw-transcript-version="2">
 which is a pretty good salary for a
 </span>
 <span data-rw-start="1570" data-rw-transcript-version="2">
 developer in Germany, right?
 </span>
 <span data-rw-start="1572.24" data-rw-transcript-version="2">
 So, um, yeah, it's, it's not really, uh,
 </span>
 <span data-rw-start="1576.08" data-rw-transcript-version="2">
 like that anymore, right?
 </span>
 <span data-rw-start="1577.84" data-rw-transcript-version="2">
 So, we went
 </span>
 <span data-rw-start="1580.559" data-rw-transcript-version="2">
 from $20 flat rates, or I think GitHub
 </span>
 <span data-rw-start="1582.72" data-rw-transcript-version="2">
 Copilot in the beginning was even $10 a
 </span>
 <span data-rw-start="1585.36" data-rw-transcript-version="2">
 month, to more like around, like the
 </span>
 <span data-rw-start="1588.72" data-rw-transcript-version="2">
 Claude Max subscription, which is $200,
 </span>
 <span data-rw-start="1590.72" data-rw-transcript-version="2">
 and it’s not really a flat rate anymore.
 </span>
</p>
<p>
 <span data-rw-start="1592.48" data-rw-transcript-version="2">
 So, you still get throttled, and there’s
 </span>
 <span data-rw-start="1595.279" data-rw-transcript-version="2">
 request limiting, and probably even that
 </span>
 <span data-rw-start="1598.08" data-rw-transcript-version="2">
 is still subsidized by the companies.
 </span>
</p>
<p>
 <span data-rw-start="1599.84" data-rw-transcript-version="2">
 There was this blue sky thread recently,
 </span>
 <span data-rw-start="1602" data-rw-transcript-version="2">
 where a journalist was asking people who
 </span>
 <span data-rw-start="1604.08" data-rw-transcript-version="2">
 have these flat rate subscriptions.
 </span>
 <span data-rw-start="1605.679" data-rw-transcript-version="2">
 There was like a way to determine what
 </span>
 <span data-rw-start="1607.039" data-rw-transcript-version="2">
 you're actually using in terms of
 </span>
 <span data-rw-start="1609.36" data-rw-transcript-version="2">
 tokens. And this person was on a $100
 </span>
 <span data-rw-start="1611.36" data-rw-transcript-version="2">
 plan and was using $591 in that
 </span>
 <span data-rw-start="1612.799" data-rw-transcript-version="2">
 Particular month. And I think even the
 </span>
 <span data-rw-start="1614.799" data-rw-transcript-version="2">
 $591 is probably still a subsidized
 </span>
 <span data-rw-start="1618.32" data-rw-transcript-version="2">
 perspective on what it costs. So it's
 </span>
 <span data-rw-start="1620.24" data-rw-transcript-version="2">
 kind of like yeah unclear where this is
 </span>
 <span data-rw-start="1623.279" data-rw-transcript-version="2">
 going. So, and why do 100 lines of code
 </span>
 <span data-rw-start="1626.96" data-rw-transcript-version="2">
 now cost more like 250 and not 12 cents?
 </span>
</p>
<p>
 <span data-rw-start="1629.919" data-rw-transcript-version="2">
 And I should mention, of course,
 </span>
 <span data-rw-start="1633.039" data-rw-transcript-version="2">
 like number of lines of code is not a
 </span>
 <span data-rw-start="1635.2" data-rw-transcript-version="2">
 measure that we should be looking at
 </span>
 <span data-rw-start="1637.12" data-rw-transcript-version="2">
 anyway, right? So, let's leave that
 </span>
 <span data-rw-start="1639.2" data-rw-transcript-version="2">
 aside for now. It's just like an example
 </span>
 <span data-rw-start="1640.96" data-rw-transcript-version="2">
 of like um uh the the the the cost
 </span>
 <span data-rw-start="1645.039" data-rw-transcript-version="2">
 explosion, right? Um because now we
 </span>
 <span data-rw-start="1648.48" data-rw-transcript-version="2">
 don't just like ask a chat to give us a
 </span>
 <span data-rw-start="1650.559" data-rw-transcript-version="2">
 few lines of code or like have autocomp
 </span>
 <span data-rw-start="1653.039" data-rw-transcript-version="2">
 letion but we research the existing
 </span>
 <span data-rw-start="1655.44" data-rw-transcript-version="2">
 code. We plan, we review the plan. We
 </span>
 <span data-rw-start="1658.32" data-rw-transcript-version="2">
 start implementing, making changes. Then
 </span>
 <span data-rw-start="1660.799" data-rw-transcript-version="2">
 the agent runs the tests, fixes the
 </span>
 <span data-rw-start="1662.72" data-rw-transcript-version="2">
 tests, checks lint errors, fixes those,
 </span>
 <span data-rw-start="1666.32" data-rw-transcript-version="2">
 uh, checks the browser, maybe if it's a
 </span>
 <span data-rw-start="1668.24" data-rw-transcript-version="2">
 front-end feature. So they can now open
 </span>
 <span data-rw-start="1669.76" data-rw-transcript-version="2">
 the browser and kind of like check
 </span>
 <span data-rw-start="1671.2" data-rw-transcript-version="2">
 what's going on there. Uh, you know,
 </span>
 <span data-rw-start="1673.12" data-rw-transcript-version="2">
 there's more fixes. There's a code
 </span>
 <span data-rw-start="1674.559" data-rw-transcript-version="2">
 Review step, summarization at the
 </span>
 <span data-rw-start="1677.279" data-rw-transcript-version="2">
 end. So it's all of these like loops
 </span>
 <span data-rw-start="1679.36" data-rw-transcript-version="2">
 that we built in, and every single back
 </span>
 <span data-rw-start="1681.52" data-rw-transcript-version="2">
 and forth, uh, costs tokens, right?
 </span>
</p>
<p>
 <span data-rw-start="1685.52" data-rw-transcript-version="2">
 So, for the less human supervision, we
 </span>
 <span data-rw-start="1687.6" data-rw-transcript-version="2">
 also now have to ask ourselves as
 </span>
 <span data-rw-start="1688.96" data-rw-transcript-version="2">
 technical leaders, like, how to sandbox
 </span>
 <span data-rw-start="1691.039" data-rw-transcript-version="2">
 the coding agents, right? So that's like
 </span>
 <span data-rw-start="1693.36" data-rw-transcript-version="2">
 not just in the cloud but also locally.
 </span>
 <span data-rw-start="1695.279" data-rw-transcript-version="2">
 So, I, uh, a lot of developers now are
 </span>
 <span data-rw-start="1697.76" data-rw-transcript-version="2">
 starting to use dev containers more, or
 </span>
 <span data-rw-start="1699.84" data-rw-transcript-version="2">
 there's some built-in sandbox modes in
 </span>
 <span data-rw-start="1702" data-rw-transcript-version="2">
 some of the coding agents that it's also
 </span>
 <span data-rw-start="1704.32" data-rw-transcript-version="2">
 easy to get around. But yeah, so there's
 </span>
 <span data-rw-start="1706.399" data-rw-transcript-version="2">
 like a lot of with security, you know,
 </span>
 <span data-rw-start="1708" data-rw-transcript-version="2">
 you have to think about the sandboxing,
 </span>
 <span data-rw-start="1710" data-rw-transcript-version="2">
 and make it easy for people in your
 </span>
 <span data-rw-start="1711.679" data-rw-transcript-version="2">
 organization, and making sure that
 </span>
 <span data-rw-start="1713.84" data-rw-transcript-version="2">
 everybody really understands this lethal
 </span>
 <span data-rw-start="1716.24" data-rw-transcript-version="2">
 trifecta when they, um, when they build
 </span>
 <span data-rw-start="1718.48" data-rw-transcript-version="2">
 agent use cases.
 </span>
</p>
<p>
 <span data-rw-start="1722.159" data-rw-transcript-version="2">
 And then, finally, like, more autonomy,
 </span>
 <span data-rw-start="1723.76" data-rw-transcript-version="2">
 less supervision. What about
 </span>
 <span data-rw-start="1725.52" data-rw-transcript-version="2">
 maintainability? So, um,
 </span>
 <span data-rw-start="1729.44" data-rw-transcript-version="2">
 I'm not going to talk here about, like,
 </span>
 <span data-rw-start="1730.88" data-rw-transcript-version="2">
 What the current state is of, uh, you know,
 </span>
 <span data-rw-start="1733.679" data-rw-transcript-version="2">
 how how good the code is that comes out
 </span>
 <span data-rw-start="1735.919" data-rw-transcript-version="2">
 of the coding agents, um, directly. So
 </span>
 <span data-rw-start="1739.76" data-rw-transcript-version="2">
 like in, in, in terms of time, but, um,
 </span>
 <span data-rw-start="1743.279" data-rw-transcript-version="2">
 obviously, you know, like, uh, there will
 </span>
 <span data-rw-start="1745.44" data-rw-transcript-version="2">
 always be a level of non-determinism. We
 </span>
 <span data-rw-start="1747.36" data-rw-transcript-version="2">
 can never be 100% sure that we get
 </span>
 <span data-rw-start="1749.279" data-rw-transcript-version="2">
 exactly what we want, even though it has
 </span>
 <span data-rw-start="1750.799" data-rw-transcript-version="2">
 gotten a lot better, right? Um, and so
 </span>
 <span data-rw-start="1753.279" data-rw-transcript-version="2">
 what, uh, what are maybe new ideas to, uh,
 </span>
 <span data-rw-start="1756.559" data-rw-transcript-version="2">
 to tackle that, just from a code quality
 </span>
</p>
<p>
 <span data-rw-start="1758.799" data-rw-transcript-version="2">
 uh, standpoint? There was recently this
 </span>
 <span data-rw-start="1761.039" data-rw-transcript-version="2">
 really interesting article by a team at
 </span>
 <span data-rw-start="1763.12" data-rw-transcript-version="2">
 OpenAI, um, who, uh, started a new codebase
 </span>
 <span data-rw-start="1766.88" data-rw-transcript-version="2">
 from scratch five months ago, and their
 </span>
 <span data-rw-start="1769.2" data-rw-transcript-version="2">
 goal was to not touch the code
 </span>
 <span data-rw-start="1770.96" data-rw-transcript-version="2">
 themselves at all. And instead, over
 </span>
 <span data-rw-start="1773.44" data-rw-transcript-version="2">
 those five months, every time there was
 </span>
 <span data-rw-start="1775.12" data-rw-transcript-version="2">
 like a problem in the code, they, they
 </span>
 <span data-rw-start="1777.2" data-rw-transcript-version="2">
 worked on this, what they call, like a
 </span>
 <span data-rw-start="1778.559" data-rw-transcript-version="2">
 harness. So, kind of, uh, that gives
 </span>
 <span data-rw-start="1781.36" data-rw-transcript-version="2">
 the agent feedback, um, and, uh, let's
 </span>
 <span data-rw-start="1786.159" data-rw-transcript-version="2">
 self-correct, um, as well. So, in the
 </span>
 <span data-rw-start="1788.48" data-rw-transcript-version="2">
 article, they're talking about context
 </span>
</p>
<p>
 <span data-rw-start="1790.48" data-rw-transcript-version="2">
 engineering that they've done. So, kind
 </span>
 <span data-rw-start="1791.76" data-rw-transcript-version="2">
 Of like all of these skills and agents
 </span>
 <span data-rw-start="1793.76" data-rw-transcript-version="2">
 MD things. They talk about setting
 </span>
 <span data-rw-start="1795.76" data-rw-transcript-version="2">
 architectural constraints with uh custom
 </span>
 <span data-rw-start="1798.08" data-rw-transcript-version="2">
 linters and structural tests. And they
 </span>
 <span data-rw-start="1800.799" data-rw-transcript-version="2">
 also talk about garbage, what they call
 </span>
 <span data-rw-start="1802.24" data-rw-transcript-version="2">
 garbage collection. So they still saw
 </span>
 <span data-rw-start="1804.799" data-rw-transcript-version="2">
 with all of this that there was still a
 </span>
 <span data-rw-start="1806.64" data-rw-transcript-version="2">
 lot of drift and entropy the same way as
 </span>
 <span data-rw-start="1808.72" data-rw-transcript-version="2">
 when humans um maintain code. So they
 </span>
 <span data-rw-start="1812.24" data-rw-transcript-version="2">
 had like a bunch of agents run regularly
 </span>
 <span data-rw-start="1814.64" data-rw-transcript-version="2">
 on the codebase to again look for the
 </span>
 <span data-rw-start="1817.76" data-rw-transcript-version="2">
 structural issues and try to try to
 </span>
 <span data-rw-start="1819.84" data-rw-transcript-version="2">
 improve um over time. So I recently also
 </span>
 <span data-rw-start="1823.12" data-rw-transcript-version="2">
 did some like um experimentation with
 </span>
 <span data-rw-start="1825.919" data-rw-transcript-version="2">
 these architectural constraints in
 </span>
 <span data-rw-start="1827.52" data-rw-transcript-version="2">
 particular um structural tests as agent
 </span>
 <span data-rw-start="1830.24" data-rw-transcript-version="2">
 feedback. I mean this is something that
 </span>
 <span data-rw-start="1832" data-rw-transcript-version="2">
 we've had for quite a while, right? When
 </span>
 <span data-rw-start="1833.6" data-rw-transcript-version="2">
 you think about ArcUnit or maybe some of
 </span>
 <span data-rw-start="1835.84" data-rw-transcript-version="2">
 you know, Spring U Modulith, right? So kind
 </span>
 <span data-rw-start="1838.96" data-rw-transcript-version="2">
 of like frameworks where you can define
 </span>
 <span data-rw-start="1840.72" data-rw-transcript-version="2">
 rules about how you want your codebase
 </span>
 <span data-rw-start="1842.72" data-rw-transcript-version="2">
 to be structured and then they can give
 </span>
 <span data-rw-start="1844.72" data-rw-transcript-version="2">
 you an indication when you violate those
 </span>
 <span data-rw-start="1847.279" data-rw-transcript-version="2">
 rules.
 </span>
</p>
<p>
 <span data-rw-start="1849.76" data-rw-transcript-version="2">
 And so I was just working on a codebase
 </span>
 <span data-rw-start="1851.44" data-rw-transcript-version="2">
 and then developed with AI kind of the
 </span>
 <span data-rw-start="1854.399" data-rw-transcript-version="2">
 layers that I wanted and then different
 </span>
 <span data-rw-start="1856.24" data-rw-transcript-version="2">
 rules, like, for example, in the only the
 </span>
 <span data-rw-start="1859.679" data-rw-transcript-version="2">
 clients package, was allowed to import
 </span>
 <span data-rw-start="1862" data-rw-transcript-version="2">
 external SDKs, so that my domain wouldn’t
 </span>
 <span data-rw-start="1865.039" data-rw-transcript-version="2">
 be dirtied by that. Right? So I just had
 </span>
 <span data-rw-start="1868.159" data-rw-transcript-version="2">
 a bunch of those rules, and then I had
 </span>
 <span data-rw-start="1870.08" data-rw-transcript-version="2">
 them running in parallel to the agent,
 </span>
 <span data-rw-start="1872.159" data-rw-transcript-version="2">
 and the agent could kind of like request
 </span>
 <span data-rw-start="1874.48" data-rw-transcript-version="2">
 you know, how am I doing, and it would
 </span>
 <span data-rw-start="1876.64" data-rw-transcript-version="2">
 give it these, um,
 </span>
 <span data-rw-start="1879.36" data-rw-transcript-version="2">
 uh, yeah, these messages, and you can also
 </span>
 <span data-rw-start="1882.24" data-rw-transcript-version="2">
 then, when you think of, like, custom
 </span>
 <span data-rw-start="1883.76" data-rw-transcript-version="2">
 linter or these structural tests, you
 </span>
</p>
<p>
 <span data-rw-start="1885.84" data-rw-transcript-version="2">
 can, in the messages of the linting, right,
 </span>
 <span data-rw-start="1889.12" data-rw-transcript-version="2">
 you can prompt inject in a good way,
 </span>
 <span data-rw-start="1891.76" data-rw-transcript-version="2">
 right? So, you can change the messages of
 </span>
 <span data-rw-start="1893.679" data-rw-transcript-version="2">
 lint, uh, errors to kind of tell the agent
 </span>
 <span data-rw-start="1896.559" data-rw-transcript-version="2">
 what it to do, right? So, for example,
 </span>
 <span data-rw-start="1898.72" data-rw-transcript-version="2">
 when it's a rule like each file should
 </span>
 <span data-rw-start="1901.2" data-rw-transcript-version="2">
 have a maximum of 500 lines of code to
 </span>
 <span data-rw-start="1903.6" data-rw-transcript-version="2">
 prevent that the agent starts just
 </span>
 <span data-rw-start="1905.039" data-rw-transcript-version="2">
 putting lots of statements in one, one
 </span>
 <span data-rw-start="1906.72" data-rw-transcript-version="2">
 line, you can put into the error message
 </span>
 <span data-rw-start="1909.12" data-rw-transcript-version="2">
 That is a smell we should redesign,
 </span>
 <span data-rw-start="1911.12" data-rw-transcript-version="2">
 right? So, that's kind of like all part
 </span>
 <span data-rw-start="1913.44" data-rw-transcript-version="2">
 of this evolving linter and stuff
 </span>
 <span data-rw-start="1916.159" data-rw-transcript-version="2">
 like that for agent usage.
 </span>
</p>
<p>
 <span data-rw-start="1919.519" data-rw-transcript-version="2">
 And so, for me, I've been playing
 </span>
 <span data-rw-start="1921.039" data-rw-transcript-version="2">
 around with this mental model. I would
 </span>
 <span data-rw-start="1922.96" data-rw-transcript-version="2">
 also be interested, uh, later maybe, in the
 </span>
 <span data-rw-start="1925.039" data-rw-transcript-version="2">
 networking if you have any feedback for
 </span>
 <span data-rw-start="1926.399" data-rw-transcript-version="2">
 that, if that resonates or if it's
 </span>
 <span data-rw-start="1927.84" data-rw-transcript-version="2">
 confusing. So, um, we have the, uh, coding
 </span>
 <span data-rw-start="1931.519" data-rw-transcript-version="2">
 agent, and then what we're doing when
 </span>
 <span data-rw-start="1933.919" data-rw-transcript-version="2">
 we're doing this context engineering, so
 </span>
 <span data-rw-start="1935.679" data-rw-transcript-version="2">
 writing down coding conventions, rules,
 </span>
 <span data-rw-start="1938.24" data-rw-transcript-version="2">
 examples, reference documentation,
 </span>
 <span data-rw-start="1939.919" data-rw-transcript-version="2">
 giving the agent access to all of that
 </span>
 <span data-rw-start="1941.6" data-rw-transcript-version="2">
 stuff. I think of that as like feed
 </span>
 <span data-rw-start="1943.679" data-rw-transcript-version="2">
 forward, right? So, we're anticipating
 </span>
 <span data-rw-start="1945.6" data-rw-transcript-version="2">
 that the agent might need to know all
 </span>
 <span data-rw-start="1947.6" data-rw-transcript-version="2">
 these things or might do them wrong, like
 </span>
 <span data-rw-start="1949.44" data-rw-transcript-version="2">
 not use the virtual environment. And so,
 </span>
 <span data-rw-start="1951.519" data-rw-transcript-version="2">
 we're kind of like feed-forward, but it's
 </span>
 <span data-rw-start="1953.44" data-rw-transcript-version="2">
 a little bit like hope and pray that the
 </span>
 <span data-rw-start="1955.519" data-rw-transcript-version="2">
 agent will do this right. And then what
 </span>
 <span data-rw-start="1958.32" data-rw-transcript-version="2">
 we also need, and this is like, uh, this is
 </span>
 <span data-rw-start="1962.559" data-rw-transcript-version="2">
 only now, what people start talking about.
 </span>
</p>
<p>
 <span data-rw-start="1964.159" data-rw-transcript-version="2">
 More is kind of the feedback. So kind of
 </span>
 <span data-rw-start="1966.48" data-rw-transcript-version="2">
 like sensors that tell it about the
 </span>
 <span data-rw-start="1968.48" data-rw-transcript-version="2">
 runtime state of the application, the
 </span>
 <span data-rw-start="1970.08" data-rw-transcript-version="2">
 static analysis state. Um, uh, maybe
 </span>
 <span data-rw-start="1973.039" data-rw-transcript-version="2">
 mutation testing is a good feedback as
 </span>
 <span data-rw-start="1974.96" data-rw-transcript-version="2">
 well because it will tell the agent how
 </span>
 <span data-rw-start="1976.48" data-rw-transcript-version="2">
 good the tests are that it wrote.
 </span>
 <span data-rw-start="1978.559" data-rw-transcript-version="2">
 And, um, so these different colors here
 </span>
 <span data-rw-start="1982" data-rw-transcript-version="2">
 are supposed to indicate that we can
 </span>
 <span data-rw-start="1983.6" data-rw-transcript-version="2">
 have a mix here of things that are large
 </span>
 <span data-rw-start="1985.84" data-rw-transcript-version="2">
 language model executed, so GPU inference
 </span>
 <span data-rw-start="1988.399" data-rw-transcript-version="2">
 and things that are executed by the CPU.
 </span>
</p>
<p>
 <span data-rw-start="1990.799" data-rw-transcript-version="2">
 Right, something like static code
 </span>
 <span data-rw-start="1992.399" data-rw-transcript-version="2">
 analysis is CPU, right? So, it gives us a
 </span>
 <span data-rw-start="1995.12" data-rw-transcript-version="2">
 lot more trust in the outcomes, and it's
 </span>
 <span data-rw-start="1996.799" data-rw-transcript-version="2">
 also cheaper and faster, uh, but we can
 </span>
 <span data-rw-start="1999.279" data-rw-transcript-version="2">
 still have, I just called it, agent as
 </span>
 <span data-rw-start="2000.88" data-rw-transcript-version="2">
 judge here, so we can still have a code
 </span>
 <span data-rw-start="2002.64" data-rw-transcript-version="2">
 review agent running or some uh stuff
 </span>
 <span data-rw-start="2005.039" data-rw-transcript-version="2">
 like that, and also take advantage of an
 </span>
 <span data-rw-start="2007.519" data-rw-transcript-version="2">
 LLM, then to give us more review and also
 </span>
 <span data-rw-start="2009.919" data-rw-transcript-version="2">
 in the feed forward, you can do that by
 </span>
 <span data-rw-start="2011.679" data-rw-transcript-version="2">
 the way. So, some of that is already
 </span>
 <span data-rw-start="2013.2" data-rw-transcript-version="2">
 built into coding agents. But in feed
 </span>
 <span data-rw-start="2015.6" data-rw-transcript-version="2">
 forward, you can also think about for
 </span>
 <span data-rw-start="2017.679" data-rw-transcript-version="2">
 Example giving the agent access to uh
 </span>
 <span data-rw-start="2020.88" data-rw-transcript-version="2">
 refactoring functionality, like there's a
 </span>
</p>
<p>
 <span data-rw-start="2022.799" data-rw-transcript-version="2">
 JetBrains MCP server that gives the
 </span>
 <span data-rw-start="2025.44" data-rw-transcript-version="2">
 agent the ability to do the rename
 </span>
 <span data-rw-start="2027.279" data-rw-transcript-version="2">
 symbol function from uh from like a
 </span>
 <span data-rw-start="2030.399" data-rw-transcript-version="2">
 proper IDE, right? And with that, again, you
 </span>
 <span data-rw-start="2032.96" data-rw-transcript-version="2">
 increase, like, um, the uh how good the
 </span>
 <span data-rw-start="2036.48" data-rw-transcript-version="2">
 outcome is, and um, kind of like prevent
 </span>
 <span data-rw-start="2039.519" data-rw-transcript-version="2">
 that it—or you increase the probability
 </span>
 <span data-rw-start="2042.08" data-rw-transcript-version="2">
 that it does the right thing in the
 </span>
 <span data-rw-start="2043.519" data-rw-transcript-version="2">
 first place. So, it's all about, you know,
 </span>
 <span data-rw-start="2045.919" data-rw-transcript-version="2">
 turning that lever of uh that dial of
 </span>
 <span data-rw-start="2048.399" data-rw-transcript-version="2">
 probability, uh, that you get a good
 </span>
 <span data-rw-start="2050.48" data-rw-transcript-version="2">
 outcome, and then the human is kind of
 </span>
 <span data-rw-start="2053.28" data-rw-transcript-version="2">
 like in this steering situation, right?
 </span>
</p>
<p>
 <span data-rw-start="2055.599" data-rw-transcript-version="2">
 Where you also can use an agent to
 </span>
 <span data-rw-start="2057.52" data-rw-transcript-version="2">
 continuously work on these guides and on
 </span>
 <span data-rw-start="2059.44" data-rw-transcript-version="2">
 these sensors, and especially for the
 </span>
 <span data-rw-start="2061.76" data-rw-transcript-version="2">
 sensors, because we have coding agents,
 </span>
 <span data-rw-start="2063.679" data-rw-transcript-version="2">
 now we can actually build a lot more
 </span>
 <span data-rw-start="2065.44" data-rw-transcript-version="2">
 custom tooling here. It's a lot easier
 </span>
 <span data-rw-start="2067.919" data-rw-transcript-version="2">
 uh than it used to be to build more
 </span>
 <span data-rw-start="2069.679" data-rw-transcript-version="2">
 advanced linters. In the past, we never
 </span>
 <span data-rw-start="2071.76" data-rw-transcript-version="2">
 would have done that because it felt
 </span>
 <span data-rw-start="2072.96" data-rw-transcript-version="2">
 like a waste of time, right?
 </span>
</p>
<p>
 <span data-rw-start="2076.56" data-rw-transcript-version="2">
 And then that whole thing is kind of
 </span>
 <span data-rw-start="2078.72" data-rw-transcript-version="2">
 that harness that uh was also being
 </span>
 <span data-rw-start="2081.52" data-rw-transcript-version="2">
 talked about in that in that article,
 </span>
 <span data-rw-start="2083.679" data-rw-transcript-version="2">
 right? Um yeah, so kind of like harness,
 </span>
 <span data-rw-start="2087.04" data-rw-transcript-version="2">
 right? So you have kind of like reins
 </span>
 <span data-rw-start="2088.639" data-rw-transcript-version="2">
 and you know restrict the movement of
 </span>
 <span data-rw-start="2091.28" data-rw-transcript-version="2">
 the system that you're regulating, so to
 </span>
 <span data-rw-start="2094.159" data-rw-transcript-version="2">
 say, right? So all kind of like reminds
 </span>
 <span data-rw-start="2097.119" data-rw-transcript-version="2">
 us of cybernetics and stuff like that.
 </span>
</p>
<p>
 <span data-rw-start="2099.68" data-rw-transcript-version="2">
 Right?
 </span>
 <span data-rw-start="2102.079" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="2103.76" data-rw-transcript-version="2">
 yeah, and you want to have like as many
 </span>
 <span data-rw-start="2106" data-rw-transcript-version="2">
 CPU executed sensors in particular as
 </span>
 <span data-rw-start="2108.72" data-rw-transcript-version="2">
 possible, right? And also you want them
 </span>
 <span data-rw-start="2111.52" data-rw-transcript-version="2">
 to be as left as possible, right? I see
 </span>
 <span data-rw-start="2114.48" data-rw-transcript-version="2">
 so many people write about how they have
 </span>
 <span data-rw-start="2116.48" data-rw-transcript-version="2">
 all of these things after they do the
 </span>
 <span data-rw-start="2118.24" data-rw-transcript-version="2">
 commit or on the pull request. And it's
 </span>
 <span data-rw-start="2120.64" data-rw-transcript-version="2">
 even built into some of the tools.
 </span>
</p>
<p>
 <span data-rw-start="2122.079" data-rw-transcript-version="2">
 There's a review uh skill and a security
 </span>
 <span data-rw-start="2125.44" data-rw-transcript-version="2">
 review skill in cloud code that you
 </span>
 <span data-rw-start="2128" data-rw-transcript-version="2">
 cannot just apply to your local changes.
 </span>
 <span data-rw-start="2130.32" data-rw-transcript-version="2">
 It expects a br to be on a branch on a
 </span>
 <span data-rw-start="2132.48" data-rw-transcript-version="2">
 git branch or it expects to be in a pull
 </span>
 <span data-rw-start="2134.48" data-rw-transcript-version="2">
 request, which to me is like what I want.
 </span>
</p>
<p>
 <span data-rw-start="2137.359" data-rw-transcript-version="2">
 To use this on my local changes, I want
 </span>
 <span data-rw-start="2139.119" data-rw-transcript-version="2">
 to do this before I create the commit.
 </span>
 <span data-rw-start="2141.44" data-rw-transcript-version="2">
 Right? So, um, I also see like first signs
 </span>
 <span data-rw-start="2144.56" data-rw-transcript-version="2">
 of people. There was a, an article from
 </span>
 <span data-rw-start="2146.8" data-rw-transcript-version="2">
 Stripe recently, who wrote about how
 </span>
 <span data-rw-start="2148.88" data-rw-transcript-version="2">
 they are doing this, and they're also
 </span>
 <span data-rw-start="2150.24" data-rw-transcript-version="2">
 talking about doing things pre-commit.
 </span>
 <span data-rw-start="2152.64" data-rw-transcript-version="2">
 So, there are like first signs of this
 </span>
 <span data-rw-start="2154.64" data-rw-transcript-version="2">
 realization coming in, but it's still
 </span>
 <span data-rw-start="2157.68" data-rw-transcript-version="2">
 because our industry is so, like, pull
 </span>
 <span data-rw-start="2159.68" data-rw-transcript-version="2">
 request by default, uh, um, at this moment,
 </span>
 <span data-rw-start="2163.28" data-rw-transcript-version="2">
 in time, like, a lot of this stuff happens
 </span>
 <span data-rw-start="2165.599" data-rw-transcript-version="2">
 too late, I think.
 </span>
</p>
<p>
 <span data-rw-start="2168.96" data-rw-transcript-version="2">
 Yeah, yeah. And again, this harness kind
 </span>
 <span data-rw-start="2170.32" data-rw-transcript-version="2">
 of, again, like I said, changes the
 </span>
 <span data-rw-start="2172.96" data-rw-transcript-version="2">
 probability that AI gets something wrong
 </span>
 <span data-rw-start="2174.72" data-rw-transcript-version="2">
 or right, and is also a way for us to
 </span>
 <span data-rw-start="2177.359" data-rw-transcript-version="2">
 reflect on the detectability of some
 </span>
 <span data-rw-start="2179.599" data-rw-transcript-version="2">
 things, right? So, the probability part
 </span>
 <span data-rw-start="2181.359" data-rw-transcript-version="2">
 is basically our trust in the agent, and
 </span>
 <span data-rw-start="2183.92" data-rw-transcript-version="2">
 what are the things that we can do to
 </span>
 <span data-rw-start="2185.92" data-rw-transcript-version="2">
 move that trust level? And it cannot just
 </span>
 <span data-rw-start="2188.079" data-rw-transcript-version="2">
 be, oh yeah, the model magically got
 </span>
 <span data-rw-start="2190.48" data-rw-transcript-version="2">
 better, right? So, we want to have some
 </span>
 <span data-rw-start="2192.48" data-rw-transcript-version="2">
 other stuff around that as well.
 </span>
</p>
<p>
 <span data-rw-start="2195.44" data-rw-transcript-version="2">
 And by the way, I was mainly talking
 </span>
 <span data-rw-start="2197.599" data-rw-transcript-version="2">
 about internal code quality here, right?
 </span>
 <span data-rw-start="2199.76" data-rw-transcript-version="2">
 And things like maintainability. I can
 </span>
 <span data-rw-start="2201.76" data-rw-transcript-version="2">
 totally see how maybe an agent at some
 </span>
 <span data-rw-start="2204.079" data-rw-transcript-version="2">
 point is a lot better than us at
 </span>
 <span data-rw-start="2206.48" data-rw-transcript-version="2">
 modularizing a codebase, right? We have
 </span>
 <span data-rw-start="2209.04" data-rw-transcript-version="2">
 been so shitty at that historically,
 </span>
 <span data-rw-start="2210.72" data-rw-transcript-version="2">
 right? That’s why we start creating a
 </span>
 <span data-rw-start="2212.56" data-rw-transcript-version="2">
 new microser all the time because we’re
 </span>
 <span data-rw-start="2214.24" data-rw-transcript-version="2">
 so bad at modularizing internally. But
 </span>
 <span data-rw-start="2217.359" data-rw-transcript-version="2">
 there’s still like lots of open
 </span>
 <span data-rw-start="2218.88" data-rw-transcript-version="2">
 questions for me about verifying
 </span>
 <span data-rw-start="2220.48" data-rw-transcript-version="2">
 functionality because there’s this whole
 </span>
 <span data-rw-start="2222" data-rw-transcript-version="2">
 dilemma of we have to specify correctly
 </span>
 <span data-rw-start="2224.64" data-rw-transcript-version="2">
 and then how do you verify that? And you
 </span>
 <span data-rw-start="2226.8" data-rw-transcript-version="2">
 can’t just, like, at the moment most
 </span>
 <span data-rw-start="2229.76" data-rw-transcript-version="2">
 people just seem to trust the tests that
 </span>
 <span data-rw-start="2231.92" data-rw-transcript-version="2">
 are generated by the AI when they use
 </span>
 <span data-rw-start="2234.16" data-rw-transcript-version="2">
 agents at a high level, which I
 </span>
 <span data-rw-start="2236.64" data-rw-transcript-version="2">
 think is just, uh, not enough, right? So I
 </span>
 <span data-rw-start="2239.04" data-rw-transcript-version="2">
 think of these harnesses almost like
 </span>
 <span data-rw-start="2240.4" data-rw-transcript-version="2">
 there’s different ones, right? Like I was
 </span>
 <span data-rw-start="2242.4" data-rw-transcript-version="2">
 just talking about some for
 </span>
 <span data-rw-start="2243.44" data-rw-transcript-version="2">
 maintainability. Maybe there’s others
 </span>
 <span data-rw-start="2245.599" data-rw-transcript-version="2">
 that you know, kind of try to, uh, kind of
 </span>
 <span data-rw-start="2248.4" data-rw-transcript-version="2">
 Harness in the quality of the
 </span>
</p>
<p>
 <span data-rw-start="2250.16" data-rw-transcript-version="2">
 operability of a system. But then
 </span>
 <span data-rw-start="2252.24" data-rw-transcript-version="2">
 there's behavior as well, right? And for
 </span>
 <span data-rw-start="2254.56" data-rw-transcript-version="2">
 the behavior part, yeah, like I said, I
 </span>
 <span data-rw-start="2256.48" data-rw-transcript-version="2">
 still have lots of open questions, but I
 </span>
 <span data-rw-start="2258.64" data-rw-transcript-version="2">
 kind of like this, uh, uh, thinking in
 </span>
 <span data-rw-start="2261.2" data-rw-transcript-version="2">
 harnesses because it helps us reflect on
 </span>
 <span data-rw-start="2263.599" data-rw-transcript-version="2">
 what is actually our safety net around
 </span>
 <span data-rw-start="2266.88" data-rw-transcript-version="2">
 an agent. And then, in combination with
 </span>
 <span data-rw-start="2269.04" data-rw-transcript-version="2">
 models that got better, I think then we
 </span>
 <span data-rw-start="2271.28" data-rw-transcript-version="2">
 can make that risk assessment of, like,
 </span>
 <span data-rw-start="2272.8" data-rw-transcript-version="2">
 when do I trust it, when do I not trust
 </span>
 <span data-rw-start="2274.56" data-rw-transcript-version="2">
 it? And then finally, I feel like maybe
 </span>
 <span data-rw-start="2278.64" data-rw-transcript-version="2">
 you know, will we have some topologies in
 </span>
 <span data-rw-start="2281.599" data-rw-transcript-version="2">
 the future that are the new abstraction
 </span>
 <span data-rw-start="2283.2" data-rw-transcript-version="2">
 level where you can have a harness
 </span>
 <span data-rw-start="2285.44" data-rw-transcript-version="2">
 around it, right? So, let’s say there’s
 </span>
 <span data-rw-start="2287.599" data-rw-transcript-version="2">
 like that structure was a typical layer
 </span>
 <span data-rw-start="2290.079" data-rw-transcript-version="2">
 structure that I was showing you before,
 </span>
 <span data-rw-start="2291.52" data-rw-transcript-version="2">
 right? Like, there was like routes coming
 </span>
 <span data-rw-start="2293.28" data-rw-transcript-version="2">
 in, there was like a, almost like a
 </span>
 <span data-rw-start="2294.88" data-rw-transcript-version="2">
 controller that loads data from some
 </span>
 <span data-rw-start="2296.96" data-rw-transcript-version="2">
 client APIs, and that then has like a
 </span>
 <span data-rw-start="2299.52" data-rw-transcript-version="2">
 domain layer, right? That’s super typical
 </span>
 <span data-rw-start="2301.44" data-rw-transcript-version="2">
 of what we do, right? And then, let’s say.
 </span>
</p>
<p>
 <span data-rw-start="2303.359" data-rw-transcript-version="2">
 In combination with a text stack, you
 </span>
 <span data-rw-start="2304.88" data-rw-transcript-version="2">
 have a bunch of guides and sensors that
 </span>
 <span data-rw-start="2306.96" data-rw-transcript-version="2">
 you can just instantiate whenever you
 </span>
 <span data-rw-start="2308.8" data-rw-transcript-version="2">
 want to do a project like this, right?
 </span>
 <span data-rw-start="2311.2" data-rw-transcript-version="2">
 And then maybe at some point, I don’t
 </span>
 <span data-rw-start="2313.119" data-rw-transcript-version="2">
 even care if it’s ReactJS or Vue.js or
 </span>
 <span data-rw-start="2315.2" data-rw-transcript-version="2">
 whatever, because I don’t even like, yeah,
 </span>
 <span data-rw-start="2317.68" data-rw-transcript-version="2">
 I don’t have to deal with those details
 </span>
 <span data-rw-start="2319.52" data-rw-transcript-version="2">
 anymore. And maybe, uh, it will be a big
 </span>
 <span data-rw-start="2322.72" data-rw-transcript-version="2">
 question for us when we choose
 </span>
 <span data-rw-start="2324.079" data-rw-transcript-version="2">
 technologies, like how harnessable are
 </span>
 <span data-rw-start="2326.72" data-rw-transcript-version="2">
 they, because it will reduce the work
 </span>
 <span data-rw-start="2328.72" data-rw-transcript-version="2">
 that I have so much more.
 </span>
</p>
<p>
 <span data-rw-start="2332.16" data-rw-transcript-version="2">
 So, in summary, context engineering, uh,
 </span>
 <span data-rw-start="2334.48" data-rw-transcript-version="2">
 has evolved a lot over the past year, and
 </span>
 <span data-rw-start="2336.48" data-rw-transcript-version="2">
 it's this powerful lever for us as
 </span>
 <span data-rw-start="2338.48" data-rw-transcript-version="2">
 technical leaders to, of amplification,
 </span>
 <span data-rw-start="2341.28" data-rw-transcript-version="2">
 right? Um, and then secondly, there are
 </span>
 <span data-rw-start="2344.32" data-rw-transcript-version="2">
 very strong forces right now tempting
 </span>
 <span data-rw-start="2346.48" data-rw-transcript-version="2">
 humans out of the loop, right? Oh, the
 </span>
 <span data-rw-start="2348.88" data-rw-transcript-version="2">
 models are getting better. There’s like
 </span>
 <span data-rw-start="2350.8" data-rw-transcript-version="2">
 everything’s a lot easier to experiment
 </span>
 <span data-rw-start="2352.56" data-rw-transcript-version="2">
 with, with these cloud agents, and oh, you
 </span>
 <span data-rw-start="2355.359" data-rw-transcript-version="2">
 just have to have like a simple harness,
 </span>
 <span data-rw-start="2357.04" data-rw-transcript-version="2">
 like that, and then everything will be.
 </span>
</p>
<p>
 <span data-rw-start="2358.56" data-rw-transcript-version="2">
 Better, right? So it's like it is really
 </span>
 <span data-rw-start="2361.92" data-rw-transcript-version="2">
 like a strong pull right now, and uh, with
 </span>
 <span data-rw-start="2364.8" data-rw-transcript-version="2">
 together with the hype. So it's about
 </span>
 <span data-rw-start="2367.2" data-rw-transcript-version="2">
 where can your organization give
 </span>
 <span data-rw-start="2368.72" data-rw-transcript-version="2">
 into that pull, and where is it dangerous?
 </span>
 <span data-rw-start="2370.64" data-rw-transcript-version="2">
 Right, like this reflection on
 </span>
 <span data-rw-start="2372.64" data-rw-transcript-version="2">
 probability, uh, impact, and detectability.
 </span>
 <span data-rw-start="2377.44" data-rw-transcript-version="2">
 Yeah, that's all I have. Um, I
 </span>
 <span data-rw-start="2379.68" data-rw-transcript-version="2">
 regularly write on my colleague Martin
 </span>
 <span data-rw-start="2381.52" data-rw-transcript-version="2">
 Farer's website, and uh, yeah, all of
 </span>
 <span data-rw-start="2385.04" data-rw-transcript-version="2">
 my other content is also on my personal
 </span>
 <span data-rw-start="2386.72" data-rw-transcript-version="2">
 website. And that's it. And I'm in time.
 </span>
 <span data-rw-start="2392.742" data-rw-transcript-version="2">
 [applause]
 </span>
 <span data-rw-start="2401.04" data-rw-transcript-version="2">
 »&gt; One question.
 </span>
</p>
<p>
 <span data-rw-start="2401.599" data-rw-transcript-version="2">
 »&gt; Perfect. And since you're, you, you
 </span>
 <span data-rw-start="2404.64" data-rw-transcript-version="2">
 haven't extended your time almost at
 </span>
 <span data-rw-start="2407.68" data-rw-transcript-version="2">
 all, let's do at least one question. Um,
 </span>
 <span data-rw-start="2412.24" data-rw-transcript-version="2">
 how can a technical leader coordinate
 </span>
 <span data-rw-start="2414" data-rw-transcript-version="2">
 over a team of human engineers that all
 </span>
 <span data-rw-start="2416" data-rw-transcript-version="2">
 use cloud code?
 </span>
</p>
<p>
 <span data-rw-start="2420.079" data-rw-transcript-version="2">
 »&gt; Um, coordinate across the team. Yeah, I
 </span>
 <span data-rw-start="2423.119" data-rw-transcript-version="2">
 mean, I don't know what the background of
 </span>
 <span data-rw-start="2425.2" data-rw-transcript-version="2">
 the question is, but, um, so there's
 </span>
 <span data-rw-start="2427.839" data-rw-transcript-version="2">
 multiple, like, one coordination level is
 </span>
 <span data-rw-start="2430.16" data-rw-transcript-version="2">
 what I was talking about to help.
 </span>
</p>
<p>
 <span data-rw-start="2432.24" data-rw-transcript-version="2">
 The team amplify the right things with
 </span>
 <span data-rw-start="2434.4" data-rw-transcript-version="2">
 like thinking about skills and tools
 </span>
 <span data-rw-start="2436.079" data-rw-transcript-version="2">
 that should be available to the agents.
 </span>
 <span data-rw-start="2437.52" data-rw-transcript-version="2">
 Right, but I don't know if it's also
 </span>
 <span data-rw-start="2439.2" data-rw-transcript-version="2">
 related, the question to, um, when you have
 </span>
 <span data-rw-start="2442.4" data-rw-transcript-version="2">
 a full team, like
 </span>
 <span data-rw-start="2445.2" data-rw-transcript-version="2">
 going all in with this and creating a
 </span>
 <span data-rw-start="2447.2" data-rw-transcript-version="2">
 lot of throughput, then as the leader of
 </span>
 <span data-rw-start="2450.079" data-rw-transcript-version="2">
 a team or the delivery manager, or
 </span>
 <span data-rw-start="2451.68" data-rw-transcript-version="2">
 something like that, you have a lot of moving
 </span>
 <span data-rw-start="2453.28" data-rw-transcript-version="2">
 pieces on the table that you can't just
 </span>
 <span data-rw-start="2455.28" data-rw-transcript-version="2">
 revert, like uh, inside of a coding
 </span>
 <span data-rw-start="2458.079" data-rw-transcript-version="2">
 session, right? So, I don't know if the
 </span>
 <span data-rw-start="2459.76" data-rw-transcript-version="2">
 question is related to that, but that's
 </span>
 <span data-rw-start="2461.839" data-rw-transcript-version="2">
 also, one of my big question marks.
 </span>
 <span data-rw-start="2463.92" data-rw-transcript-version="2">
 What happens with, like, parallelization?
 </span>
 <span data-rw-start="2465.76" data-rw-transcript-version="2">
 And this higher throughput that is
 </span>
 <span data-rw-start="2467.68" data-rw-transcript-version="2">
 happening in so many places. I mean, the
 </span>
 <span data-rw-start="2470.319" data-rw-transcript-version="2">
 managing that is just one of the many
 </span>
 <span data-rw-start="2471.839" data-rw-transcript-version="2">
 bottlenecks, right? I didn't even have
 </span>
 <span data-rw-start="2473.92" data-rw-transcript-version="2">
 time to go into all of that. What happens
 </span>
 <span data-rw-start="2475.359" data-rw-transcript-version="2">
 to the pipelines? What happens to the
 </span>
 <span data-rw-start="2477.2" data-rw-transcript-version="2">
 requirements coming in? What happens to
 </span>
 <span data-rw-start="2478.8" data-rw-transcript-version="2">
 monitoring all of those new features, if
 </span>
 <span data-rw-start="2480.64" data-rw-transcript-version="2">
 they actually create value, and so on.
 </span>
</p>
<p>
 <span data-rw-start="2482.16" data-rw-transcript-version="2">
 And so on. So it's a big question. I am
 </span>
 <span data-rw-start="2486.72" data-rw-transcript-version="2">
 &gt;&gt; So, basically, it's a good question. We
 </span>
 <span data-rw-start="2488.8" data-rw-transcript-version="2">
 have to deal with it.
 </span>
 <span data-rw-start="2489.28" data-rw-transcript-version="2">
 &gt;&gt; It's a good question. [laughter]
 </span>
 <span data-rw-start="2490.72" data-rw-transcript-version="2">
 &gt;&gt; Okay. I mean, I tried this like three
 </span>
 <span data-rw-start="2492.8" data-rw-transcript-version="2">
 cloud code instances at the same time
 </span>
 <span data-rw-start="2495.44" data-rw-transcript-version="2">
 and I abandoned it again because it was
 </span>
 <span data-rw-start="2497.28" data-rw-transcript-version="2">
 too much. And that's also
 </span>
 <span data-rw-start="2499.52" data-rw-transcript-version="2">
 like Kevlin talked a bit about it today
 </span>
 <span data-rw-start="2501.599" data-rw-transcript-version="2">
 as well. Like, there are first reports of
 </span>
 <span data-rw-start="2503.76" data-rw-transcript-version="2">
 burnout or being overwhelmed or
 </span>
 <span data-rw-start="2506.8" data-rw-transcript-version="2">
 like Steve himself says, I can work like
 </span>
 <span data-rw-start="2508.96" data-rw-transcript-version="2">
 this two or three hours a day, and then
 </span>
 <span data-rw-start="2511.04" data-rw-transcript-version="2">
 I'm tired and done. Right. So it's like
 </span>
 <span data-rw-start="2513.76" data-rw-transcript-version="2">
 not even on the team level, just like you
 </span>
 <span data-rw-start="2515.839" data-rw-transcript-version="2">
 with like three, four, five cloud code
 </span>
 <span data-rw-start="2517.68" data-rw-transcript-version="2">
 instances is just Yeah.
 </span>
</p>
<p>
 <span data-rw-start="2521.2" data-rw-transcript-version="2">
 Okay. So, as usual, you all know the
 </span>
 <span data-rw-start="2524.48" data-rw-transcript-version="2">
 drill already. Um, you'll be around, you
 </span>
 <span data-rw-start="2527.52" data-rw-transcript-version="2">
 can be found, you can ask questions,
 </span>
 <span data-rw-start="2529.68" data-rw-transcript-version="2">
 right?
 </span>
 <span data-rw-start="2530.16" data-rw-transcript-version="2">
 &gt;&gt; Yeah.
 </span>
 <span data-rw-start="2530.96" data-rw-transcript-version="2">
 &gt;&gt; Okay. So, for now, thank you very much.
 </span>
 <span data-rw-start="2533.359" data-rw-transcript-version="2">
 Yeah.
 </span>
 <span data-rw-start="2533.76" data-rw-transcript-version="2">
 &gt;&gt; Thank you. [applause]
 </span>
</p>