# Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next

![rw-book-cover](https://i.ytimg.com/vi/SlGRN8jh2RI/sddefault.jpg)

## Metadata
- Author: [[Sequoia Capital]]
- Full Title: Anthropic's Boris Cherny: Why Coding Is Solved, and What Comes Next
- Category: #articles
- Summary: Boris Cherny from Anthropic says coding is mostly solved because AI can now write most code automatically. Their tool, Claude code, helps everyone on the team code faster and better. In the future, AI will write all code, making software building easier and more common.
- URL: https://m.youtube.com/watch?v=SlGRN8jh2RI&pp=ugUEEgJlbg%3D%3D

## Full Document
Okay, I'm excited to introduce our nextspeaker. Show of hands, who here usesClaude code?Okay, show of hands, who here has Claudecode psychosis?Come on, guys, [clears throat] it's okay.It's okay. Um, my team lovinglysays I have Claude code psychosis, whichmay or may not be true.Um, we aredelighted to have Boris Cherny with ustoday. Uh, Boris is the creator, thefather of Claude code. Um, and in theprocess of doing that, he has just had afront-row seat to reinventing themodern way of software development.Um, and we're really grateful toyou, Boris, for taking the time to speakwith us today. We know that theentirety of software development kind ofrests on your shoulders. So, thank youfor taking the time out of your schedule to bewith us today. And interviewing Boris isLauren Reader from our team.Thank you.

>> [applause]>> Giving our chairs.

Um, you took my opening line,Asia. We asked who here uses Claudecode. There's a lot of hands. That'sawesome.Thank you for joining us, Boris. It'svery special to have you here. Um,as a roomful of builders, I think youare changing building entirely. And so,I'm very curious to explore how youthink about the future of software,coding, and what we should spend all ofour free time on. Um, but I'll give you ame a tiny bit more background on you sothat everyone has a little bit morecontext. So, beyond creating Claude

code, Boris is very much an engineer'sengineer. You were writing a lot of codethrough your whole career, writingtextbooks about code, includingprogramming in TypeScript. Um, and Ithink last time we chatted you hadn'twritten a single line of code in thelast year, or at least so far in 2026,which is quite the change. Um, there'sAlso, a little known thing back inmiddle school, I wrote a guide about uhwriting BASIC for TI-83 Pluscalculators.

And I, I just, I searched for it, it'sactually still on the internet. It'sextremely embarrassing, so please don'tsearch it. But it [laughter] exists. Wewill definitely be finding that. Um, so,we're going to do, I’m going to startwith a few questions here. Maybe we'llstart with a little bit of the historyof Claude code, how you started it, andthen we're going to have a lot ofaudience Q&A for this one. And so, startthinking about your questions in theback of your head, uh, and would love toturn it over to you all soon.

Yeah. Um, and also, real quick, so forpeople that use Claude code, do peopleuse the CLI mostly? Like, okay, majorityCLI?Okay. That's a lot. Majority desktop?

Okay. Majority VS code or JetBrains IDE?Okay. That's actually not a lot. Okay.

Other?I'm like iOS mostly these days. Yeah.>> [laughter]>> Okay. Cool.Um yeah, so I started Claude code kind of accidentally in a lot of ways.Um, I joined this team back in late 2024.It was a sort of this incubator within Anthropic called Anthropic Labs.And, uh, the team kind of served its purpose.

Um, we created Claude code, MCP, and the desktop app.It was a team that was just a few of us.So, very much like an innovation team.We built the thing that we wanted to build,we disbanded the team.

Uh, now the team's actually back together for round two.Mike Krieger, who's the, you know,like the chief product officer at Anthropic,and used to be one of the founders at Instagram,so he's leading that right now.

Um, so, the kind of the reason that I started to work on coding is we felt like there was this product.

Overhang. And I, I'm guessing people hereuse that word a lot. Uh, but wedefinitely use this word a lot in kindof within the lab.Uh, there's this idea that the model cando all the stuff that no product has yetcaptured. And in late 2024, when we werelooking at coding, the way that we didcoding, the state of the art at the timewas type ahead. It was you open your IDEand you press tab, and you can likecomplete like one line at a time. Andthat was the thing that Sonnet 3.5enabled for the first time. But thefeeling was, we could actually go a lotfurther than that. And the model wasalmost ready for the next big step. So,we don't have to do type ahead anymore,we can just have the agent write all ofthe code.

And so, I built it, and it just reallydidn't work for the first 6 months. Itwas like not very good. It was barelyusable. I wrote it from, I used it formaybe 10% of my code or something like that.

That. And even after we released Claudecode initially, it was not a hit.There's a lot of people that used it,but it did not have this exponentialgrowth that it has today.Um, that started with Opus 4 in May. AndI, I remember that very clearly. That'slike when the exponential growthstarted, and then it kind of inflectedwith every model release. Uh, like itstarted with Opus 4, then 4.5, then 4.6,now 4.7. It just kind of keepsinflecting.

But, essentially, we were trying to buildthis thing that was like pre-PMF, and weknew that it wouldn't have PMF for 6months because we were building for thenext model. And that was the idea, thepretty much the whole time.

And, you know, for Anthropic in general,we've always just been very focused.We've always cared about business andenterprise, and safety, and coding. That'sjust always been kind of the way that wewanted to build. And so, at some point,We kind of knew that we wanted to builda product. We didn't know exactly whatwe wanted. So, this kind of ended upbeing the product bet.

It's an incredible story, especiallythat it was an accident.Um,so, you've said on the record that youthink coding is solved. Uh, if this isone of the three best from Anthropic,can you tell us more about what you meanby that, and what might still not besolved, or what second-order problemsmight come? All right. I can ask anotherquestion for the room. Who writes 100%of their code by hand?Who writes 100% of their code using anagent like Claude code?Okay. Who's like somewhere in between?Okay. So, like 50% solved.>> [laughter]>> I mean, for me it's like, forme, it's 100%. Like the Claude codebase, um, you know, it leaked, soyou know, people know. Uh, it's pretty.

Simple. It's just like TypeScript andit's React. Like there's no big secret.There's nothing reallycomplicated. The reason we pickedTypeScript and React is it's very ondistribution for the model. So, when westarted, you know, building the codebase, the model was not as intelligentas it is today, so the language and theframework mattered a lot. Nowadays, youknow, it can write whatever, and it canpick up new languages, new frameworks ithasn't seen. But back then, you wantedto use something pretty on distribution.

Because of that, I think fairly early wegot to the point where the model justwrote 100% of the code. And for us, thishappened sometime in October, Novemberlast year.And so, for me today, you know, like themodel writes 100% of my code. I writesomewhere, you know, usually a few dozenPRs every day.Uh, there was a day last week I did like150 PRs in a day. That was like, that wasA record. I was just trying to kind ofpush to see how far I can get it.

Um, but yeah, it's like for me, for meit's just solved. Um, but this is not thecase everywhere. There are very bigcomplicated code bases. There's kind ofweird languages, the model's not good atyet. Um, and you know, as everyone hereknows, it's getting there. Usuallythe answer is just wait for the nextmodel.

Can you actually tell us about yourpersonal setup? You walked us through itthe other day. It is pretty wild.

Yeah. Um, so, I shared my personal setuplike six months ago or something on Twitter. And it it's funny, I actually, Ishared it, I didn't realize that it wouldbe surprising for anyone. That was justlike the way that I coded.

>> [laughter]>> And it's changed since then. It'schanged. Um, and so, now actually most ofmy work I do from my phone.

I don't know if like you guys won't beable to see this, but I have, um,so, I have like the Claude app, and ifyou open the Claude app,on the left-hand side, there's thislittle code tab,and I just have a bunch of sessionsgoing.Um,you probably can't see it.>> How many sessions?Uh, usually I have like maybe five to10 sessions. Uh, and then the sessionsusually have a bunch of agents, so Ithink, currently probably like a fewhundred agents going.Um, usually every night I have like a fewthousand that are doing kind of deeperwork. There are a few ways to manage it.One is that you ask Claude to use abunch of sub-agents to do work.Actually, the thing that I've beenfinding myself using more and more isthe loop. So, this is {slash} loop, andit's just like the coolest thing. It'sLike the simplest thing that works. Allit is, is you have Claude use cron toschedule a job for some point in thefuture, and it's a repeat job.

And it can run every, every minute, every5 minutes, every day, kind of howeveroften you want to schedule it.And at [snorts], this point, I have likedozens of loops that are running forstuff. So, I have one that's babysittingmy PRs, like fixing CI, auto-rebasing. Ihave another one that keeps CI healthy.

So, like if there's like a flaky test orwhatever, it'll go and fix it. Um,I have another one that grabs, uh,feedback from Twitter and kind ofclusters it for me every 30 minutes. So,I just have a bunch of these loopsrunning at any time. I sort of feel likeloops are the future at this point. Ifyou haven't experimented with it, highlyhighly recommend it. And we also justlaunched routines, which is the samething but kind of on the server. So,even if you close your laptop, it, itKeeps going.

So, that's your personal setup. Tell usabout what you think teams will looklike in the future. How do youextrapolate from all the work you'redoing to keep everyone on the teammoving forward, understanding thecontext, or do you think we need to letgo of a lot more to agents to make itwork?Um, I think so. I, you know, it's like it'sso hard to make predictions, but, umI'm here to make predictions, so I'lltry to make some.I feel like the way that things aregoing is generally there's going to be alot more generalists than there aretoday.Andtoday, when we talk about generalists, Ithink largely we're talking about peoplethat are still engineers. So, they'restill writing code, but maybe they'rekind of product engineers. So, maybewhen we say "generalist," it's like a youknow, they do iOS and web and server,for example. That's like a generalist inengineering.

But I think the thing that we're goingto start to see a lot more of isgeneralists that are cross-disciplinary.So, this is engineers that are reallygood at product engineering, but alsoreally great at design. Or really greatat product and data science andengineering.

UmI don't know. It's something thatwe're starting to see on our team. So,actually, like a lot of people on theClaude code teamare generalists across disciplines.Everyone on our team codes. So, like ourengineering manager, our productmanager, our designers, our datascientist, our finance guy, our userresearcher, every single person on ourteam writes code.

Everyone's just coding.And you know,I'm seeing some nods, but I bet alsoit's actually not that surprising topeople in this room because I bet you'reseeing the same things.Um [clears throat] I'll have one morefavorite question, then we'll open up tothe audience. So, we talked a bit aboutwhat's changing with coding. I’m curiousabout what you see changing in the worldof software or software products.Um,I think as we see AI making writing code10 or 100 times cheaper,what happens to the value of theproducts that are produced withsoftware? Do we have a SAS apocalypse onour hands? How do you think this playsout? And again, you're going to have tomake another prediction.The SAS apocalypse question is myfavorite question then.Um,I think there are two things that areGoing to happen, and I don't thinkeither of them is the thing that peoplehave been talking about.

I think one is, is anyone here anacquired listener? Like the acquiredpodcast?Yeah, it's like the best podcast.Uh, I actually, I got to do an unpluggedwith them the other week, and I just, Ifelt like I got to meet my heroes because they're just like the hosts are the best.

So, they have this idea of, uh, sevenpowers, and this is a, this is likeHamilton. He kind of wrote, he wrote abook about this, and this is kind of theseven modes in business. And I thinkwhat's going to happen is because of AI,some of these modes are going to getmore important, and some are going to getless important. And so, like, forexample, one that gets less important is,uh, switching costs because you can justuse the model and you can kind of port.

from one thing to a different thing.Another one that gets less important isprocess power,because for companies whose mode is likeworkflows and process and things likethis,Claude is getting really good atfiguring out process. And especiallywith 4.7, it can just hill climbanything. So, if you give it a targetand you tell it to iterate until it'sdone, it will just do it. I think thisis the first model like that.

So, I think these are going to get lessimportant, but I think the previousmodes actually still matter. So, this islike network effects, uh scaleeconomies, cornered resources, thingslike that. These are not really changingwith AI.

I think the second thing is, if you lookat the number of startups today or, like,maybe in the next, you know, the past 10years, I think the number of startups inthe next 10 years that are just going toLike disrupt everything is going toincrease like 10x.

Because right now you can be a tinystartup, you could build a thing that'sas valuable as a large company, and youcan actually compete head-to-head because the large company has to evolvetheir business process, they have toevolve the way they work, they have toretrain everyone to use technology,they're going to face a lot of internal resistance to that.

Butyou know, no one here has that problem.If you're starting fresh, then you cankind of build with AI natively from theground up.So, I don't know. I think it's thebest time to build. It's the best timeto be a startup. There's so muchdisruption coming.So, there is hope for us after all.

Thank you, Boris.Um, I would love to open up to audience questions if anyone has anything theyWould like to ask.

Dan?I, yeah, I'm curious.Um, you said that you built, uh6 months before there was product marketfit, but now given that the models aregood enough, how much do you attributethe success of Claude code to the modelversus like product decisions in thefield of product?Uh, I think it's probably a mix.Yeah, I think it's a mix. I think,if you asked me, maybe a year ago,the ratio was maybe something like50/50.Um, maybe I don't know. If you asked me sixmonths ago, the mix would be 50/50.> >> What about in two years?Oh, two years, I don't know, dude. We planin, like, we plan in one week out.>> Months. Sometime in the future.>> [Laughter]>> And, by the way, I think the reason itwas 50/50 is, umYou know, I I I like I I did YC back inthe day. I was like the first hire at aYC company, and like I did a bunch ofstartups.

And in startups, like the thing that theydrill into you and then especially in YCover and over is build something peoplelove.And so, it doesn't matter what theproduct is, it doesn't matter like themodel and all this stuff. You still inthe end have to build a thing thatpeople love. And I think that's thatwhy the product matters. We pay somuch attention to the little details sothat as you use it all day, it's areally great experience.I think as the model's gotten better,the harness kind of gets less important.And I think, like, I think that we'rethinking about right now is, like, how dowe evolve the harness? So, like, how dowe make loops more of a first-classthing? How do we make it easier to run alot of agents? Uh, you know, besides you.

Know, like sub agents is one idea.There's a bunch more stuff that we'recooking.But I think in a year, the model will bemuch better aligned. And so, all thesafety mechanisms that we have todayarounduh prompt injection and kind of staticverification of commands and uhpermission modes, human in the loop, allthis kind of stuff is just going to beless important cuz the model will justdo the right thing.Um, so, yeah, that's that prediction.

Thank you.You want to toss the box, Dan?>> [snorts]>> Great.

Um, to zoom out a little bit fromsoftware, I think Claude code did acultural change a few months ago whereit democratized like building software.You can see, uh, shop owners buildingtheir ownUm, software for themselves or even uhprogramming microcontrollers to controlthe light when someone opens the door.

Um, do you see in the future, um,building software becoming a skill likeuh, I know, uh, Microsoft Office?

Um, so, it's a thing that ev- everybody can do,not just people in the tech industry. Oh,my god, yes. Yes. Yes. I think it’sgoing to be even more than that. I thinkit's going to be—I don't know. It'sgoing to be a skill like yeah, like Iknow how to send a text message.

I, I, I think, um,you know, like I, I read a, my, my twogenres are essentially sci-fi and techhistory. This is what I read a lot of.

I, I think in tech history, there’s onething which I think to me is theclearest parallel for what’s happeningright now. And this is in the 1400s,the printing press in Europe.

And what happened was, before theprinting press, essentially 10% of theEuropean population was literate. TheyKnew how to read and write.

They were often employed by like kingsand lords that were not literate.And their job was to, you know, theirjob was to read and write, and thisis not something that everyone knew howto do.

>> [snorts]>> The printing press was invented, thenthere were two more presses, and in the50 years after the first printing press,there was more literature published inEurope than in the thousand yearsbefore.

And over the same period, the cost ofliterature, the cost of a book, went downlike a 100x. And then, you know, it tooka couple hundred years because, you know,learning to read and write is hard. Youneed education systems and governmentand everyone can't be working on farms,and so on. But over the next few hundredyears, literacy globally went up to like70%. And so, you know, now we can allread and write, and you don't need aDegree in reading and writing to knowhow to read and write. Although stillthere are professional writers and thatis a thing that you can do.

So, I think the thing that's about tohappen and it's going to be much fasterthan 50 years is software will be athing that is fully democratized, thatanyone can do.

And you know, there's a lot ofcorollaries to this. So, for example,let's say you're writing accountingsoftware.The best person to write accountingsoftware, I think maybe even today, isnot an engineer, it's a really goodaccountant because they know the domainreally well, and coding is the easy part.It's knowing the domain that's the hardpart. And I think this is justobviously the future.

So, uh, one of the things Greg said wasthat you guys are living in the future alittle bit because you get to have access tothe models and the agents. Claude code.

Was an internal tool before you releasedit. Um, is the gap between where you guysare in engineering and the rest of theworld, is that a month? Is it 3 months?Is it 6 months? And is that, is that gapgetting bigger or smaller over time?

Yeah, so, so internally, we use the samemodels everyone else does.Um, for us, the dogfooding is reallyreally important. So, we use the thingthat everyone else here does. Um, youknow, we use a little bit of Mythosto try it and then we use a lot of Opus4.7 to dogfood it and to write mostof our code.

Um, I think on the model side, thereisn't really a gap. Um, you know, it'slike, it's pretty much Mythos, and youknow, that will become some version ofsome descendant of that will becomeavailable at some point to everyone.

I think on the product side, there'sprobably a far larger gap. And that'sjust related to us changing all of ourprocesses. Like, if you talk to people atAnthropic, we use Claude for literallyeverything. And our Claudes are talkingall day, like, as I'm coding, as myClaudes are coding in a loop, they willcommunicate over Slack to talk to otherpeople's Claudes that are also runningin a loop to kind of figure outunknowns.

We have no more manually written codeanywhere at the company. All of the SQLis written by, uh, by models. Everythingis just built by the models. So, I, I, Ithink, actually, the place that we'reahead is not the technology, because the sametechnology available to us is availableto everyone here because, fundamentally,we are building a platform. And so, forus, it's really important thatdevelopers can use the same thing thatwe're using and that we, we dog foodeverything that we put out there.But, I think there's actually a farbigger weed in, kind of, theorganizational structure andorganizational process. And, this is aPlace where you know, hopefully we cantalk about it in places like this and uheveryone can kind of learn from it andand also evolve.

Yeah, and I think that's one of theadvantages startups have. It's so mucheasier to start there.Jared?Yeah, um, last time we talked, I think Ithink you'd mentioned we talked a littlebit about multi-agent, and it was very incode at the time, at a prior Sequoiaevent, and you mentioned that there weresome things going down the pipeline, andthings you're talking about, you're thinkingabout. Now, obviously, there's slashbatch, there's slash loop, there's subteams, there are teams. Can you speak some

to either the model level or theharness level, how you're injectingpriors in the harness level, and how theobjective function is changing at the modellevel to make this experiencearound delegating work, spinning upagents better? Because so much of the workis parallelizable. You can do so manythings so much faster, and I feel like Ihave to overlay my own intuition forwhen to parallelize things rather thanthe model kind of understanding that youcan spin up 10 sub-agents for something.

Yeah, I mean, on the product side, itreally just comes down to prompting.That's how it is. And so, youknow, we tweak prompts to kind ofhelp the model do stuff in parallelmore.

But also, honestly, as the model getsbetter, it just naturally does this. Andso, something like loop, I foundactually 4.7, it just starts doing. Uhwhich is really cool. It's like it doessomething like, uh, you know, I'll I'lltell it, "Go, uh,pull this data query." And it's like,"Hey, I noticed that the data ischanging over time. I'll start a loopand I'll give you a report every 30minutes." And I'm like, "Great. Can yousend it to me over Slack?"Uses the Slack MCP to do that. So, Ithink actually over time, it's not onusers to figure out how to hold thetools better. And if that's the case,it's actually a product design problem,and like I'm not doing a good job.

It's really on the model to do thisstuff better and on us, kind of promptingit so it naturally does this.

Um, so right now it seems like a lot ofus use, um, like Claude or Codex or theseuh tools in the cloud to do a lot of ourcomputing. But then, there are some veryvocal advocates of, uh, having your AI belocal. And I could imagine over time, asopen way models and other thingscatch up, that this could be more of apossibility for people to get reallyhigh-quality coding assistance. So, I'mcurious about your vision of, say, over the nextlikeyears or something like that. Do you seethe trajectory of everyone still reallyrelying on the cloud, centralizedcompute? Or, uh, is there a pivot to, oh, weAll just have our local agents that wecan rely on and they don't get throttledand other benefits?

Yeah, I think it, um,I don't know. There's maybe a few waysto answer that. I think maybe like kindof the most fundamental way toanswer that is it doesn't matter.

Cause, cause I think now we're getting to thepoint where the model is just able tofigure it out. So, I think like by acouple of years from now, the model is justgoing to be doing all the code. It'sgoing to be starting the agents. It'sgoing to be building the environments.

And so, like if it decides, like, actually,I'll use, like, local models to do this,then you know, that's what it'll do.These, I don't think these will bedecisions that we are making asengineers anymore.

We have time for a couple morequestions, so I can toss this out.Jamie,Nester. Thank you.

It feels like one of the great uh decisions with Claude Code was makinguse of the fact that a lot ofdevelopers' tools and workflows arelocal.But um that isn't necessarily always thecase for sort of general knowledge workwith, you know, cloud tools. I’m curioushow you're thinking about this withCo-work of how do you give Co-workenough access to the tools that we useto be powerful the same way that ClaudeCode is for developers?

Yeah, it's That’s a really greatquestion. Um I know I know when I was uhwhen I was at a big company, we tooklike 5 years moving all the environmentsto remote. It’s just like so much work,especially at a big scale.

Um but for knowledge work, largely, it’sthere already with like Salesforce andDocs and things like that.Um for us, it’s always just the simplestanswer. It’s just MCP.So, the same MCP connector that you haveIn Claude AI, you hook up like, youknow, Salesforce, you hook up GoogleDocs, Google Calendar. Uh, and thenCo-work can use that. Claude CLI can useit. Claude Code everywhere can use it.

And for the systems that don'thave MCPs, like, do you think that'swhere computer use is going to be a bigopportunity?

Yeah, I think computer use is kind of acatch-all. Um, so, I think currently, foras far as I know, I think Anthropic islike pretty far ahead on computers. Andso, like if you use it through Co-work,it's quite good. Um, so, it's able to usepretty much any piece of software thatyou have on your computer. It's veryslow, but it does it quite well now,especially with 4.7.Um, yeah, but I think, I think otherwise,like MCP is kind of the answer. It'sand you know, all this stuff justdoesn't matter that much. It could beMCPs, APIs, just some sort ofprogrammatic access because the modelDoesn't care. It's to mo- to the model,it's just tokens.

All right, we have time for one morequestion.Um, Ryan.Sean, do you want to toss the thank you?Um, you've kind of alluded to this, butif, like, sometime ago, you saw theprobabil- the product overhang, andthought to build a product that wouldthen become more interesting once modelsgot better.Could you just talk, even in vague terms,about the shape of a product you'd buildtoday that you think could become amuch more interesting as models getbetter in six months to a year?Yeah, Claude design, I think, is areally good example. It's, uh, it's prettygood today. It's going to get a lotbetter.Um, there's also a few things that we'recooking up for Claude Code, uh, that aregoing to land over the comingweeks. So, you'll see those.

Um, and then I think, uh, I think loop andbatch and things like this around likemassively parallelizing agents, that'sgoing to get better.

And computer use is another good one.

All right, Boris. Thank you so much forjoining us. I think we'll be here for alittle longer if anyone has questions.>> [applause]>> Thanks, guys.
