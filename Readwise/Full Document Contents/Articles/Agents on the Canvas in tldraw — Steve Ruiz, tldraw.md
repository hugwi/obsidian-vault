# Agents on the Canvas in tldraw — Steve Ruiz, tldraw

![rw-book-cover](https://i.ytimg.com/vi/sPUjIBH5Cwg/sddefault.jpg?v=69f46780)

## Metadata
- Author: [[AI Engineer]]
- Full Title: Agents on the Canvas in tldraw — Steve Ruiz, tldraw
- Category: #articles
- Summary: tldraw makes a whiteboard tool that lets AI agents work directly on the canvas. These agents can draw, edit, and collaborate with users in real time. This approach helps people create and interact with designs easily, even without coding skills.
- URL: https://www.youtube.com/watch?v=sPUjIBH5Cwg

## Full Document
Hello. Hey, I'm going to, I'm going tokick off.Uh,sorry, we're starting a little bit latehere.I am Steve Ruizfrom Teal Draw. Does anyone know TealDraw? Yes. Hey, all right, fans, fans inthe room. Uh, if you don't know TealDraw, Teal Draw is kind of, kind of, acouple of things.Teal Draw is aonline whiteboard. You can go to it.It's free. It's really nice.Um,I'm going to be using it for my slides.Uh, Teal Draw is also a startup. We'rebased here in London. And, Teal Draw isalso an SDK, something that you can useto build other products. So, if you'veused, uh, Replit's newum,uh, agent canvas, then that's built withour canvas. If you've used, uh,um,Luma AI's new canvas, that's built withour canvas.

If you've used Stitches' new canvas,that's not built with our canvas.But, if you go into this like kind of uhum annotate mode,this actually is our canvas. So, we'rewe're in there somewhere. It's an Angularapp, you know. UhSo, anyway, umTldraw is again a company that makes awhiteboard, makes whiteboard SDK.Part of the idea with the SDK is thatyou can build cool things with uh withthe SDK,which means it's part of my job to buildcool things with the SDK to prove it.Um, and a lot of those things recentlyhave involved AI, right? Hackablecanvas runtime,built with React. In fact, the canvas isalso just React components. So,component, component, component.Um, which means you can do some prettycool stuff.

Uh, first one, uh, I'm going to be at themercy of the demo gods here in the, theinternet and, and, and other things. So,uh, bear with me here.Um, does anyone remember this app MakeReal? Maybe, maybe this tweet, uh, aboutMake Real. Did anyone, did anyoneremember seeing this tweet back in 2023when the vision models came out? Allright, cool.

Uh, this was one of the first projects tokind of like break containment, uh, in, umin AI.

Don't, we're going to go to my phone.[ \_\_ ] this.Um,which, which may, may itself be adisaster. Uh,So, the basic idea with Make Realwas that you could, um,use a canvas, draw thisand send that to a, a model, and haveit make it into a working prototype,which sounds very, very quaint in 2026.

But, in 2023, it was all the ragebecause there was no lovable, there wasno kind of vibe coding hadn't beentermed or coined as a as a term. Uh andso, this was one of the first projectswhere non-technical people couldmake technical stuff without having tocode or to look at code.And so again, we are at the mercy of thethe uhseveral[ \_\_ ] various internet uhinternet gods. So, so we'll see. I'mgoing to I’m going to let this cook fora minute. Um but at the risk of leakingmy API keys, I will try and switch to afaster model. Oh, no, it’s coming.All right. Maybe I just gave itsomething hard to uh hard to work on.We’ll see. Hang on a second.Basic idea,something like that.Uh yeah, there there There’s my APIkeys. I always got to rotate them everytime I uh do this demo.

Sadly, we'll see how much gets spent before I get donewith the talk.Um, but it is a very simple problem. It'sjust like go, go make this interactive.This is, uh, this is not what I asked for,but we'll see.All right, good job. Cool. And this is athis is a working, working thing, whichis great. It's like a real little bit ofHTML.

But, you could also annotate on top ofit. And you could say like, "Hey, uh,actually, make this green."And why don't we use these colors?I'm going to make this red and, uh,and, and, black. Um,use these colors.Right? And so, you're kind ofconstructing a prompt here, even theprompt that includes the old, uh, website.And, uh,there's not many apps that have actuallylike, kind of, use this. Only, only now,only, like, the Google Stitch that IMentioned before, uh, this idea ofwell, uh, it didn't do anything that Iasked it for. Terrible demo. We're goingto move on. Things havechanged in the last couple of years.

Anyway,uh, there was another one in Teal Drawcomputer, which I’m actually not goingto go into, but this was, uh, a couple oflike chains of prompts.But, eventually, we, we were like, "Hey,AI on the canvas actually might bepretty cool. Maybe we should, um, have theAI kind ofwork as a collaborator, like work withyou on the canvas."So, the first one of those waspretty, pretty straightforward idea whereyou could say, like, you know, draw acat.

You could do anything. You could say, um,draw me a diagram, you know, finish myslides, complete this graph that I'mworking on, things like that. Uh, andUnlike maybe image models, uh, like diffusion models and things like that,it's not building an image. It isusing text-structured outputs to makethe same things that I could make,right? So, I have tools. I havelike circles and shapes and like this.

Uh, and it's funny to see how thesethings have changed over. Oh, it's sad.

Uh,but, uh, the, uh,you know, the fun of this is as a wayof exploring the model and what themodel knows and how it can comport allthat stuff. Uh, make the cat blow out thecandle.

Um,it's pretty cool.

You could also do something like, uh, drawa mouse. So, multiple, um, multipleprompts at the same time on differentparts. And so, even though I didn't tellit what a candle was, and I certainlylike, the application doesn't know what acandle is.

Uh, and I'm not even sure that cats canlike blow.But, it's correctly interpreted that and kindof incorporated into the into thedesign. So,Uh, with incredible detail as well.Still sad. Uh,so, the um,this was really fun because this is likesolving a lot of problems thatmight not be obvious. Like, like, visionmodels, when it comes to to structureddata, um,number one, there's much less visiontraining data than there is for text. Uh,number two, a lot of that training datalike conflicts in ways that text doesnot, and other other types of thingsdon't. So, for example, the the Y axison a on a Cartesian graph,as you go up, that number goes up,Right? The top left corner is zero, yourtop left corner here, but as you godown, the Y goes up.

There's left, right, like there's yourleft, there's stage left, there's allsorts of uh uh things that conflictwithin language uh and within images.So,um,training the model to kind of behavepredictably and produce things likethis is uh was really well. I usedtraining, uh, prompt engineering the modeltodo it was really tricky. But,this was fun, um, but we felt like it didn't go really far enough because itwas just one shotting, right?We wanted to do an agent. So, this iswhat Cursor looked like back in, uh,in 2025 or something like that when Idid this.Um, drew a diagram, uh, of the lifecycle of a butterfly.So, this put it into a kind of likeAgentic loop, like you might have seenseen elsewhere.

Um, but I'm sure you interact withdozens of times a day by now for thiscrowd. Um, where you have it produce anoutput and then review the output andkind of iterate until it thinks it'sdone.

Um, and we really tried to adhere to theconventions at the time of, um,you know, coding agents that were, wherethese agents, um, this agent loop was seenmost often.Where, yeah, there's kind of like a lotof subfeatures like rejection, youknow, seeing it's thinking, seeingseeing how it works. UmGreat. And now we have the, uh, thebutterfly life cycle on the canvas.

Pretty cool.However, this was still not reallyenough because, as, as cool as this was,it still felt likeI don't know. It felt like I was handingmy keyboard to some, some other AI, rather.

Than someone collaborating with me. UmAlthough this model has been used reallywell in uh a lot of design apps that useTeal Draw, uh things like Lovelace orMagic Path, umand in in education, especially whereyou have this kind of tutor of like,"Help me with my homework and help mefill out my um you know,uhOh gosh, let's see if I can do this onthe fly. Steve Ruizuhclass,you know, age, whatever.Um and you can kind of ask it to like uhcomplete my D&Dcharactersheet.All right. And it'll it’ll kind of pickup what you're doing and fill out formsand do it do do fun stuff like this.Maybe I'll come back to that as it as itkind of chugs along.The what I really wanted is like toBring theagent out of the sidebar and intothe canvas itself. Um, oh, I'm afighter.

Nice. Nice. All right, I'll take that.Uh, and so, we did. And we did it withfairies, which maybemaybe you saw, maybe not. Um,these are like little, little guys on thecanvas. You can kind of throwthem around.Uh, they don't like to be held for verylong. They'll start freaking out.Uh, yeah, okay. So, uh,and, uh, but you can do the same thinglike, you know, draw a draw cat orsomething like that. Now, putting theagents on the canvas have a whole bunchof interesting things. You can see thestate of the agent, right? These aremultiple agents that I'm kind of runningin, incoding terms, these would be multipleterminal windows or something like that.Or, this would be in composer, composer.

But you can kind of see what they'redoing in a way that uh uh hang on. I'mzoomed way out.I did all the sprites myself.Umand you know, not only can you kind ofsee it's thinking, but you can see itsaction. You can see where it is inthe project. It's sort of like actingrelative to the other um other agents.So,and you know, these other agents can cansee each other what they're doing. So,if I ask this one to draw um a hat onthe cat,uhand I draw this one uh draw the cat'sneck.It looks like we missed the, we missedthe neck.Uhthey'll get to work,right? And they're able to kindof work with each other's stuff at thesame time.

Um, but we could also ask them to worktogether. So, if I grab all three ofthese, uh, these fairies—fairies, Helen,and Joan—um,draw some moreanimals.Uh,one of them will be elected leader. So,this one is the leader. And it'sgoing to go scout kind of what's goingon on the canvas, and then it's going tocreate a to-do list, and it's going todelegate that to-do list to the otheragents, right?Um, this is all likewe, we were doing this in, like, DecemberOctober of last year. Uh, andwe're figuring this stuff out at thesame time that a lot of people werefiguring out agent orchestration. Thisidea of, like, okay, how do we give themshared state? How do we, uh, you know,have a leader-follower? Like, how do wemanage the fact that these things areessentially blind while they're working?

And prevent them from kind ofoverlapping, uh, in terms of like whatthey're doing.And so, you can kind of see the, the, theleader here isn't doing any of the work.Uh,but it is going to kind of like observe,Oh, no, that's, that's the leader. That'sthe leader. Um,it's observing.

Uh,uh,and judging, and establishingwhether this is like done or not, andwhether it's done correctly.Um,still not enough, right? Fairies arefun. If you want to play with this, bythe way, this is at fairies.tldraw.com.Um,in the same way that Make Real was areally good introduction toum,tojust AI at all, right? Draw something,Click a button. Um, fairies is a greatway to talk about like multiple agentskind of working together.

Uh,and they can do real work. Let me tryand grab alike this is a big description of likean ebook or something like that. And ifI summon my fairies,uh,uh, make this, make the, make, make thewireframesfor this app.Cool.And I'll, I'll just kind of let them get to work while we keep talking.Um,thestarted 10 minutes later. I'm going toI'm going to take another 5 minutesbefore I jump. Uh, the next step for thisone,is to kind of give more access to thecanvas to the agents.Um,and there's reallywe started to kind of run into thebarriers of safety. Like, what isactually safe toto do with our hackable thing for, forusers? Um, because we have a runtime API.

You can just code against it, right? AndAI is really good at coding. So, maybewe could do some sandboxed, you know,stuff. But no, because we need the DOM.

We need the kind of the browser as a wayto see what's going on. We need to beable to generate screenshots, all thisstuff.

Um, so, we decided to use our uh ourdesktop app instead. So, I over theholidays I threw together a uman app that does an electron wrapperthat wrapped tldraw.

Uh,and Iopened a port essentially. I said, youknow, okay, Claude, like make a littleHTTP server and and open a put up anendpoint. And anything that gets postedTo that endpoint,uh, treat it as JavaScript and run it.

Which is a terrible idea. Not a good. Like,don't, don't, don't do that on yourapp. However, for an offline desktopapp that is file-based, like what's theworst that could happen?You could hurt yourself, I guess, butyou're not going to hurt the rest of me.Uh, and look at them. Look at them going.

It's building my little ebook reader.It's fantastic. Thank you, fairies.Doing the. TheUh, so, so, what does that? What does thatgive us, though? UmI'm going to skip the demowhere, uh, as you can imagine, I couldsay, hey, visualize this code.Make a diagram. Cool. All right, I'mgoing to change the diagram. Updatethe code to match the diagram.Easy, right? You can have these kinds oflike, let's pull up the level ofAbstraction that we want.

Um, but the more surprising stuff wasactually where I was like,you know, okay, like check this out. Uh,I'm going to draw a little userinterface or whatever, right?And I want this to be, uh, leg length.And I want this to be a T-shirtcolor.Uh,and even though tldraw doesn’t reallyhave the ability to, we don’t have likeprimitives for on hover, on click. It’snot likeit’s not a fully thing.This thing can write code againstthe editor.So, like, uh, make it interactive.And we’ll see, we’ll see where itgets to.Um,so far,the results on this have been likereally, really cool in ways that aresuper strange and disturbing. Uh.

Because like asking likethe AIs are like, sure, let's do somescripts script injection, right? Like,that's the way that it documents itselfis, like, this is how you should dothis. Um,it has no qualms at all, by the way,changing stuff that's on your desktop onyour computer. If you've ever wanted tolike, for example,like, we, uh,one of our team, Max, was like, you know,what? I don't like podcasts in mySpotify. I want to get rid of podcastsin my Spotify app. Claude, can you justdo that? And it's like, sure. Let me gothrough the minified code of the bundleof the thing. Let me just rip and tear.

Uh,and it's happy to do it. It makes themhappy. Uh, they like it.Um, oh, what the [ \_\_ ] was that?Um,I don't even know what you did. You madean HTML. What theWhat? Like, it, it created a new HTMLsite on this?

And this is the pointer? It's not even aslider. No, I want to, I wanted in, inthe tldraw. All right. Yeah, we don't, welove it.It's blinking as well. I don't know ifyou caught that.Come on, do it. Yeah, there we go.Let's see if it can. Come on, let's go.

UmSo, yeah, like, there's really like, uhno limit to what, what, what it can dowith the desktop app, and it's happy todo it in a way that, umI can almost tell that it, it, it, uh, wouldlove to do this to websites. Like, itwould love, like, just. Let me just get myclaws in there.Um, all right, come on, come on.

Still not working. We're going to, we'regoing to,we're, we're going to go.Set up the interactivity. Come on. UhThis is going to be really fun. I think.

We're going to just release this. Uh, we'rethe, I mean, it is released, butthe, the notion that you can takelike I love local-first apps. I lovefile-over-app. I love. There are all theseideas that up to now have kind of beencuriosities anduhalmost like,Hang on.

Oh, come on.Oh, that's such a, such a disappointment.We're going to have to catch me later.I'll make it work. Uh,but now, actually, the, like, the idea of alocal file-based thing that is ableto expose itself to, to, um,to, to, Claude and agents like locally inorder to, to, essentially script inject,kind of, motivates a lot of that, thatstuff, which previously was idealisticinto, like, well, that's the only waythat you could do this.

If you really want to maximize theagency in order to maximize what it cando,and take the risk, uh, and take on thatrisk,then you, you kind of just need to handthat to the user and say, good luck.Um, I think OpenAI does this prettywell. But, like, these are sharptools.Have fun, you know? Anyway,uh, that is my agents on the canvas talk.Uh,work continues. If you want to play withthe fairies, I highly recommend it becauseit's super fun, and you will find thingsthat surprise you,that have surprised me.Uh,they have IRC as well. Let me see. Yeah,anyway.Uh,and if you want to follow along withtldraw,we are on Twitter X at tldraw, and thenI'm at Steve Ruiz okay. I post a lotabout this stuff. So,uh thank you for coming.

Cheers.
