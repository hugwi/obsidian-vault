# Context Is the New Code — Patrick Debois, Tessl

![rw-book-cover](https://i.ytimg.com/vi/bSG9wUYaHWU/sddefault.jpg?v=69f71351)

## Metadata
- Author: [[AI Engineer]]
- Full Title: Context Is the New Code — Patrick Debois, Tessl
- Category: #articles
- Summary: Context is becoming as important as code in software development. Instead of just writing code, developers create, test, and share context like reusable skills and prompts. This new approach helps improve AI agents and workflows through collaboration and continuous feedback.
- URL: https://www.youtube.com/watch?v=bSG9wUYaHWU&list=WL&index=1&t=243s

## Full Document
[music]>> There's a few people who want tostart earlier.I know I'm going to take the opportunityto officially open the kind of thearchitect track. There's no track host,so I do it myself. So, thank you forcoming here. I hope you already had likea good conference. UmIt's amazing that like so many peopleshowed up. Um, maybe before I start, umwho's used any AI coding agent in thisroom? Raise your hand.

Like, lower it. Who hasn't? Raise yourhand.Okay, my kind of people. Perfect. Allright.

Um,Okay. Context is a new code.Or, the context development life cycle. Um, Ifeel honored to be here. Every time Itry to do a different talk at the AIengineering.So, this is a little bit of, um,thinking ahead. It's anUnpolished thought. It's not likeeverything's there, but is thereanything there in AI anyway? ButSo,let's start.

I assumeyou all are now vibe coding withprompts. I barely touch anymore kind ofthe code. I just tell the AI to dosomething different.

So, I would say likecontext is the new code because it'sbeing generated.A little bit more advanced maybe isI see myself having a tendency is I hadlarge pieces of code that I was usingmaybe some helpers and some otherpieces.And I just turned them into a skill.We had that in our product. Itwas an onboarding from, you know, AIagents. UmPeople have Python, Node.js, all thevarious things. Then they have differenttools for packaging andIt is impossible to actually code that.

Like, it will require a lot of coding.But if I just say a skill says,please first figure out what theirpackage manager is, then figure out whattheir ecosystem is, and then do thesesteps together with the user.You know, it's solved a lot moreproblems that we could ever code.So, that is another piece that I would saycode is also transforming back intocontext as a skill as well, as aworkflow that's reusable.

And leave that with you.I like to think in parallels.In 2009, I don't know if there are anyDevOps people in the room. It was kindof me saying like what if ops lookedmore like dev? And then we got like,hey, collaboration, kind of ourdeployment, all that stuff. So, kind of,you know, last year I started thinking,what if contextis the code?How do we deal with this in a moreConsistent way? And it's basically saying if we have asoftware development life cycle,how does a context development lifecycle look like? Because we're basicallyshifting somewhere else. It's context,it's not code. How does it look like?

I came up with this, you know, of coursean infinity loop with some DevOpsbackground. But the whole idea is thatwe generate a lot of context.Then hopefully we test the context. Wedistribute context maybe to somecolleagues, to some other parts of theorganization. We observe whether itworks, and if it doesn't work or works,we call, like, you know, adapt andregenerate the context, and then go fromthere. So, that's kind of theloop of the talk that I'll be going forwith some examples.So, step by step going through.Generate. It's probably the one thatyou're all most familiar with.

Because you're all prompting.You're like the human context creation typing things, right? I was actuallyamazed that I just asked, tell me whenmy talk is at AI engineer, that it wouldfetch the website and it would just say,here's your talk. Like blew my mind. Buthey, I I said like the context that I'vegiven it, I'm Patrick, all that stuff,right? So, very simple context. It'swhat you do probably a lot in yoursetup.

If you get a little bit more advanced,you say that prompting is tedious. Iwant to have reusable prompts. So, youknow, depending on the flavor of yourcoding agents, they call itinstructions.Luckily, there's a little bit of astandardization now happening where it'slike an agent.md and some pieces likethat. Boo Claude for still calling itClaude.md, but anyway, you get thepicture. There's like reusable prompts,reusable pieces of context that we'reDoing.

We can also bring other context in.If we have documentation of librariesthat we use day to day,we want to pull that in because the LLMsmight not have the latest documentation.And so it's hallucinating. Is it versiontwo, version three? We don't know. So,we give it a context and say, pleasedownload the documentation. Hopefullythen the agent will be optimized. And then they willdo a better job at generating the codefor that version of the library.

Another piece of getting better contextand creating context from libraries.And of course, it wouldn't be completeif we saypull context from wherever. MCGet it from your GitLab, GitHub, kind ofSlack.All context we're pulling in, we'recreating. Even a ticket is creatingcontext because we're pulling that inwhile we go there.And then maybe the new kid on the block.

Is, okay, what if westart like writing our prompts asspecification? Spec-driven developmentwhich then gets broken down by the agentinto a planning mode, into step-by-stepkind of prompts that it then kind ofruns through. So, a lot of creationhappening in that field.You know, simple. This is probably whatyou're closest to.

Butwhen you're typing all that context andcreating all that context,you change two lines in your Claude.md.Do you know the impact?Is it like YOLO? Looks good to me. Let'sdo it. You have to think about how do wetest things?It's not just about we have a piece ofcode and we have a piece of context now.We need to write tests to see what isthe impact.New coding agent? We don'tknow where the lines still work.Now, it's not new in the world of AIengineering, but it's not that common yet.

In the world of coding with AI that youstart writing evals for which are testsfor your kind of code context.Uh, a little bit hard to read, but youknow, if you think in parallels,we have different levels of testing incode, and the simple one could belinting. Your IDE has the swigglylines like, hey, this is not, like, youknowthere's someincorrect syntax or you could do betterlike that.

Here's an example of a validation of askill where we say, well, you need tohave the description. It can only be solong. So, it's validating according tothe spec of the format of the context inthis case.Simple analogy, simple linter that youcan run.And then you can do other things likeand, and I haven't found maybe the goodcoding equivalent, but think of this asa Grammarly.

Right? So, if you write contextum,can the agent understandwhat you're writing? If you write twowords, it's not verbose enough for it toactually understand the context. So,what you can do is you can say, ask, islike, okay, you know, given thiscontext, what do you think about? Do youunderstand this? And then you can getfeedback, like,oh, it's not explicitly enough written,or it's not complete. Like, you'remissing pieces. So, that's kind of fromtools as well. So, whenever you'rewriting now your context, you get aGrammarly saying, hey,do this. That's why I like to voicecode. For some reason, I'm way moreelaborate with voice coding than typing. I'ma bad typer, two fingers,still after so many years. But when Italk, I feel like, you know, I see thesentences come on the screen, but ithelps to get good context there.

All right, another kind of test.So, imagine you put in your Claude.md or agent.md, I should say. Now,every API point must use the prefixawesome.Right? You have some convention in yourcompany. Right? Which is great.So, your prompter will be then, add me anew endpoint to save a user.And you expect actually your codingagent to just say the code that's beinggenerated has kind of {slash} awesome{slash} user.That's great.But the way we can test this is byasking thenan LLMthe code that was generateddoes it actually start with {slash}awesome? Now, you can do that withregex, I know. This is just for examplepurposes, but you can ask it to kind ofjudge your code based on your criteriaand whether it did the right thing.Right? So, imagine you would ask theSame question without your contextabove.

No LLM is ever going to prefix your URLwith awesome. So, that's kind of whereyour content or your company specific,your team specific things come in, andthat's why you still write those teststo see if this still works. Now, maybeGemini kind of reacts differently thanCopilot or something, and in yourcompany, you need to make it more, youknow, switchable of context. With this,you run the tests, and you can actuallytell.That's the difference.And then you can make like whole suites,and I would compare that almost to unittests. I have a bunch of these tests,and they tell me whether that'sactually, you know, good code, the codeis following the rules, and everything'sfine. In this case, it's even kind ofinfrastructure as code. It doesn't needto be code only. It could be variousthings. Could be config files as well.

And I just have it’s hard to read, but a bunch of kind of criteria that I justrun every time to do that.But,if you want to test,you know, whether an endpoint has{slash} awesome{slash} user,there's a real test that we want to run,which isI want to test the endpoint. I justdon't want only to check the code. Iwant to have it running. So, when yougive the judge a tool, and the judgebecomes an agent, and it can do thingsin a sandbox and execute stuff.

It can actually do the do the curl. So,you can bindLLM as a judge with kind of sometooling, and then you can have multitudeof tests actually, you know, in thiscase,it kind of ends up being an end-to-endtest, right? Because it's not justlooking at the file, it's actuallyRunning the piece with everything thatit’s supposed to do.

And then I can do this like, given acertain commit in my repo,I want to run this scenario,given this piece of context,did it make a difference? Yes or no?So, you’re kind of like building this upwhile you’re committing context alsowithin your repo.

And because we now have tests, and itgives us feedback whether it’s working,yes or no, or what it’s missing,we can optimize context.

So, that’s kind of the, you know,you can put that in acode action or something that says,"Okay, fix this context. Improve thiscontext."With all the feedback the LLMhas given usto improve that.

So, you know, again, codingimprovements, but we start thinkingmore in testing that piece as well.

Can we run this in a CI/CD systembecausethat's perfect, right? That's where werun all our tests and our testsuites and do that.Now, there's a little bit of a weirdthing.If you run evals,you run it once, you run it anothertime, it might not give the same result.Remember, undeterministic things.

So,you cannotsay, "Well, run it once, and then if itpasses or not." You're going to be infor a treat because it's like, "Ah, Ican't debug that." So,think about this like you run it fivetimes,and out of five, how many times does itsucceed?And, you know, maybein several cases it hits 100% all thetime, which is great.But, in others not. And depending on howYou change your context,it will influence which test actuallywork or not.

I find it personally helpful to thinkabout this as error budgets.I give a set of tests an error budgetthat I really care about, so it isonly allowed like, you know,to fail minimally, and other pieces areokay. So, that's how you have to thinkabout testing context. You cannot dolike exact testing all the time. It's adifferent way that this works.

All right. So,generate. Hopefully, you understand whatthe testing could do for you.And distribute.Maybe that's also something you alreadydid.If you maybe have checked context intoyour repo, right? Which is great, youknow, all of a sudden it becomesavailable, your colleague checks it out.Uh, zero friction, I can push, I canshare.

But,we have another mechanism for doingthings. Think of this like. Imagine youhave a reusable contextthat you want to reuse across multipleprojects, across multiple teams. We hadthe concept of a library.So, what if we packagekind of pieces of context, and then weare able to install pieces of contextthat we need for this project.Guidelines, front end. It doesn't matterfor that. And then if we take it that upa notch, how to discover what packagesexists?That's a registry.Right?Now,in that way, it's no surprise thatyou'll see things like skills and kindof the Tesla registry in themarketplace,where you can find a multitude ofskills. Now, the reality is99.9.

And I mean that in a very sincere way,the skills is crap.But, it's good to learn from others tosee what they're doing.But, hardly of them, if you run kind ofany set of evals on there, is actuallyup to a quality standard.Now,that will likely improve. But, there'salso a tendency thata lot of the skills and pieces,people actually want to put that intheir own registry.

So,I'll come to that later again. But,so you start seeing the gist, a skillnot only contains context, it cancontain scripts, it can containdocuments, contain bunch of things. So,is this kind of the package format?

Probably, you know, pluginscould now also contain MCP, but you seethere's like a standard coming in.Skills all of a sudden, when that cameout, all the coding agents said, "We'reSupporting this asalmost like a package format for peopleto distribute their context on.

And then, when I have one piece ofcontext,I have dependencies. And I’m sorry, butalso with context, we’re going to havedependency hell.Right? I’m, I’m, I’m going to downloadthis for front end, and maybe it’sconflicting what is in the React contextpackage. And so, you start having todeal with that as well. So, you startseeing also, uh, packages that’s, uh, mirroryour library versions, your code versions, and kind ofpull that in as well.

And of course, when we have packages andpeople are publishing things inregistry, we need security.Right? Open claw. Thank you for that.Like, everybody all of a sudden becameaware that we need more securethings because we are able to run thingson our laptop that are not, and coming.

From strangers, right? So,Snyk has a way of scanning context,right? It's doing some credentialhandling. It's uh exposing somethird-party pieces. So, you start seeingthe scanners on the context as well.

And then when you think about security,who actually built the skill? How was itbuilt? With what model was this built?So, all kind of capturing what welearned in maybe with packaging, likethe SBOM, is kind of the AI SBOM, likethe packaged of context that we'reputting in.

So, you've seenstill on the path, right? You generate,evaluate, distribute.Let's move into observe.

When youare making libraries of skills andcontext for others,and I don't mean copy and paste thisover Slack or something.But, when you actually want to maintainthis as something somebody else can use,Similar to a library,um, when they start using that, how doyou get feedback whether that stillworks?

Now, a great place to get feedback isactually by looking at the agent logs.So,imagine developer onecoding on the project, and the agent isnot doing what they want.They could put this into their context,which is great, right? Okay, let, let medo the TDD almost like, you know, I hita problem. It's not TDD, but you get mygist.Um,orwhat if we, at a team or an organizationscale, would look at the logs every timean agent said, "We're missing thispiece."And we surface that and say,"If everybody's missing this piece, weshould create context for this."And then we distribute the context toEverybody, and all of a sudden, theimpact of improvement is for everybody.

Luckily, like the agent and D, there'snow our standards becoming for logs. So,we can read from logs, and that's partof our feedback channel to see if theagent is actually using or missing someof the context.

Any feedback you get on a PR that's notcomplete, that's feedback on yourcontext becausethat PR was created with certain piecesof context. If you say this is notcorrect, you can kind of keep arguing onthe PR, or you can just say, "Let'simprove the context."So, the nextiteration actuallyimproves, uh, and you don't hit that sameproblem again.

What aboutrunning code in production that wasgenerated from context?And that's not correct becauseyes, we do our PR reviews and we saythumbs up, thumbs down, and we give theFeedback, but the actual feedback isalso in production when it's running.

So, this is a tool that actuallyinstruments your code,pushes it out, it's almost like awrapper, it pushes it out to production.When it fails, it says, "These pieces ofcode were changed and were failing.Hey, in this case, input, output,it did something wrong.

Can we create a test case for this? So,the next time we don't hit this again inproduction?"Feedback loop.

Now, these are all kind of prettytrivial, like missing pieces of contextor improvements.But, if you run agents and theequivalent of scanning, maybe, you know,in the CICD,you need to make sure when it's runningin production,it is not doing strange things. So, weneed kind of a way of looking at that.

I've been toying myself with uhyou know, sandboxing agents, and it is avery resourcefulat finding things.I like, okay, you know, run this thing,try to figure out like anything usefulto get break out of the system.And okay, it uses my environmentvariables. Okay, stupid. Let's let meremove the secret. Let me look at yourmemory files. So, you have to reallymake sure that like whatever it'sdoing, you can have a way of tracingthis as well.And uh, I apologize again for kind of theslide, butthe gist iswe can have a sandbox where the agentruns inside.But, your code agent by default withoutany restrictions loads your agent.md,you load your skill.md.Like, nothing is blocking that.So, if you download this,immediately, it's loaded.

So, you can't filter that withsandboxes. You need to have another way.I call that a context filter. Think ofthis as a web application firewall thatjust filters out any patterns or promptinjections or stuff that is coming indirectly in that piece.And if you take that, there's a lot oftalk here as well on harnessengineering. Harness engineering itselfalso has this kind of fullobservability, looking at logs, lookingat traces, looking at feedback.So, it's kind of, you know, useful fortraining pieces, but as much useful forrunning your own pieces well.Those were the pieces for me today.I would sayfor a lot of people, there's like createcontext,test context. Think of this as yourlibrary authoring tool loop.

And then when you push this into theenterprise, there's an organizationalloop. Hey, I made a library, somebodyElse is using it. I'm looking atwhatever that's useful, whether that'sstill working, whether that's stillworking for all the other pieces. So,that's kind of likethe kind ofimprovement almost like sonar CICD modelfor context. And thenyou're currently probably doing a lot atthe individual solo model, you'reimproving, you're honing, crafting yourown kind of markdown. What if you startdoing this more with your team? Makethat a reflex. If it's missing, add somecontext. What if you put that out to ateam of teams and you start having aflywheel, you know, if you fix it here,the other team can reuse it and, andthat's kind of like,you know, scaling things out into theorganization as well.

And so, there's a lot of talk about LLMsand coding agents, and I all love them,but the way that I see it is they'rejust the engine.

If you give the engine the wrong fuel,which is context,they're not going to perform. So, andyou can't do anything on the LLMs, atleast not me, right? I'm just using thecoding agent, I'm using whatever theygive me, but I can optimize my contextuh,and that's, I think, the message,uh, doingthis more in an engineered way than justcopying and pasting things and hoping forthe best in there.

If you like this talk, connect onLinkedIn for the slides. Uh,give me some feedback, good and bad.If you want to try Tessel, where weimplement some of the pieces of this, uh,have a go.

And if you're also interested in anotherconference, I know, you can never haveenough conferences, uh, visit, uh, AIDevCon, which I curate the content for,uh, here in London, first and second ofJune.

And that's it. I can maybe take a fewQuestions.

>> [Applause]>> Any questions?Sure.So, I was wondering if you have any thoughts about, like, more exotic forms ofcontext, like I don't know, thetraditional ones. So, for example, oneof the things I'm working on isan automated system for, uh, scoping outarchitectural problems and like tryingto create hard definitions for them sothat you can feed that to the agent and,you know, create actualobjectives, uh, tests.

Cool. Yeah.Microphones.Um, and one of the things I’ve beentesting out is, like,the ability to create consistency as aform of context or as a form of evaluation.So, um, given this rough, like, very loosedefinition of what the plan is, if youtry that agentsystem, turn that into a really crispDefinition, and you just have that donein parallel, how often do you get thesame crisp definition? And if they'reall over the place, then the originaldefinition was so poor, you need to likego back to base principles or to anarchitect. But, if they're all the same,then it's probably a pretty gooddefinition and you can carry on with thedownstream process. So, I think it'slike besides just code and typicalevals, um any other sources of contextfor generating context that you think isuseful?

UmI don't have maybe a a specific answerto your like exotic case, but uhI would say that maybe the piece thatpeople are underestimating is that onceyou know, you thought you were goingto save time by writing actually yourcontext uh instead of all your code,but if you take this rigorously, you'regoing to spend time on writing the rightevals. Right. And that's kind of like,You know, a lot of work to kind ofbecause now you don't only have oneprompt that you're trying to get right.

It's like all the prompts of the evalsand that, like, if people do almost like alike the more advanced people, theyalmost have their own process, and theythey build their own process on top oflike for building the right evals onyour business case as well. So,yeah.

Good question. Thank you. Any otherquestions?If not, I'll be around. Um,say hi. I'll also be at theTessel booth. So, thank you very much,and I'm going to make space for the nextspeaker. Thank you.

>> [music]
