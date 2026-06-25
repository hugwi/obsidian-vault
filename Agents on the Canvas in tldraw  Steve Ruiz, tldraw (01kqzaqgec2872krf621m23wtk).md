---
categories:
  - "[[Resources]]"
domain: engineering
title: "Agents on the Canvas in tldraw — Steve Ruiz, tldraw"
source: "https://www.youtube.com/watch?v=sPUjIBH5Cwg"
author: "AI Engineer"
published: 2026-05-01
created: 2026-05-06
description: "At tldraw, we''ve been bringing agents to our infinite canvas. In December"
tags:
  - to-process
  - agent-tools
---

Hello. Hey, I'm going to I'm going to kick off. Uh Sorry, we're starting a little bit late here. I am Steve Ruiz from Teal Draw. Does anyone know Teal Draw? Yes. Hey, all right, fans fans in 

the room. Uh if you don't know Teal Draw, Teal Draw is kind of kind of a couple of things. Teal Draw is a online whiteboard. You can go to it. It's free. It's really nice. Um I'm going to be using it for my slides. Uh Teal Draw is also a startup. We're based here in London. And Teal Draw is also an SDK, something that you can use to build other products. So, if you've used uh Replit's new um uh agent canvas, then that's built with 

our canvas. If you've used uh um Luma AI's new canvas, that's built with our canvas. If you've used Stitches' new canvas, that's not built with our canvas. But, if you go into this like kind of uh um annotate mode, this actually is our canvas. So, we're we're in there somewhere. It's a Angular app, you know. Uh So, anyway, um Teal Draw is again company makes a whiteboard makes whiteboard SDK. 

Part of the idea with the SDK is that you can build cool things with uh with the SDK, which means it's part of my job to build cool things with the SDK to prove it. Um and a lot of those things recently have have involved AI, right? Hackable canvas runtime built with React. In fact, the canvas is also just React components. So, component component component. Um which means you can do some pretty cool stuff. Uh first one uh I'm going to be at the 

mercy of the demo gods here in the the internet and and and other things. So, uh bear with me here. Um does anyone remember this app Make Real? Maybe maybe this tweet uh about Make Real. Did anyone Did anyone remember seeing this tweet back in 2023 when the vision models came out? All right, cool. Uh this was one of the first projects to kind of like break containment uh in um in AI. Don't We're going to go to my phone. [ \_\_ ] this. Um 

which which may may itself be a disaster. Uh So, the the basic idea with Make Real was that you could um use a canvas, draw this and send that to a a model and and have it make it into a working prototype, which sounds very very quaint in 2026. But, in 2023, it was all the rage because there was no lovable, there was no kind of vibe coding hadn't been termed or coined as a as a term. Uh and so, this was one of the first projects where non-technical people could make technical stuff without having to 

code or to look at code. And so again, we are at the mercy of the the uh several [ \_\_ ] various internet uh internet gods. So, so we'll see. I'm going to I'm going to let this cook for a minute. Um but at the risk of leaking my API keys, I will try and switch to a faster model. Oh, no, it's it's coming. All right. Maybe I just gave it something hard to uh hard to work on. We'll see. Hang on a second. 

Basic idea, something like that. Uh yeah, there there There's my API keys. I always got to rotate them every time I uh do this demo. Sadly. Uh we'll see how much how much gets spent before I get done with the talk. Um but it is a very simple problem. It's just like go go make this interactive. This is uh this is not what I asked for, but we'll see. All right, good job. Cool. And this is a this is a working working thing, which is great. It's like a real little bit of HTML. 

But, you could also annotate on top of it. And you could say like, "Hey, uh actually, make this green." And why don't we use these colors? I'm going to make this red and uh and and black. Um Use these colors. Right? And so, you're kind of constructing a prompt here, even the prompt that includes the old uh website. And uh there's not many apps that have actually like kind of use this Only only now, 

only like the the Google Stitch that I mentioned before, uh this idea of Well, uh it didn't do anything that I asked it for. Terrible demo. We're going to we're going to move on. Things have changed in the last couple of years. Anyway, uh there was another one in Teal Draw computer, which I'm actually not going to go into, but this was uh a couple of like chains of prompts. But, eventually we we were like, "Hey, AI on the canvas actually might be pretty cool. Maybe we should um have the AI kind of work as a collaborator, like work with 

you on the canvas." So, the first one of those was pretty pretty straightforward idea where you could say like, you know, draw a cat. You could do anything. You could say um draw me a diagram, you know, finish my slides, complete this graph that I'm working on, things like that. Uh and unlike maybe image models uh like diffusion models and things like that, it's not building an image. It is using text structured outputs to to make the same things that I could make, 

right? So, I have I have tools. I have like circles and shapes and like this. Uh and it's funny to see how these things have changed over Oh, it's sad. Uh but uh the uh you know, the fun of of this is as a way of exploring the model and and what the model knows and how it can comport all that stuff. Uh make the cat blow out the candle. Um It's pretty cool. 

You could also do something like uh draw a mouse. So, multiple um multiple prompts at the same time on different parts. And so, even though I didn't tell it what a candle was, and I certainly like the application doesn't know what a candle is, uh and I'm not even sure that cats can like blow. But, it's correctly interpreted that and kind of incorporated into the into the design. So, uh with incredible detail as well. Still sad. Uh so, the um 

this was really fun because this is like solving a lot of problems that might not be obvious. Like like vision models, when it comes to to structured data, um number one, there's much less vision training data than there is for text. Uh number two, a lot of that training data like conflicts in ways that text does not and other other types of things don't. So, for example, the the Y axis on a on a Cartesian graph, as you go up, that number goes up, right? So, 0 1 2 3 4 5. Uh on the web, 

the Y axis goes up in this direction, right? The top left corner is zero, your top left corner here, but as you go down, the Y goes up. There's left, right, like there's your left, there's stage left, there's all sorts of uh uh things that that conflict within language uh and within images. So, um training the model to kind of behave predictably and and produce things like this is uh was really Well, I used training uh prompt engineering the model 

to to do it was was really tricky. But, this was fun um but we felt like it it didn't go really far enough because it was just one shotting, right? We wanted to do an agent. So, this is what Cursor looked like back in uh in 2025 or something like that when I did this. Um draw a diagram uh of the life cycle of a butterfly. So, this put it into a kind of like 

agentic loop, like you might have seen seen elsewhere. Um but I'm sure you you interact with dozens of times a day by by now for this crowd. Um where you have it produce an output and then review the output and kind of iterate until it thinks it's done. Um And we really tried to adhere to the conventions at the time of um you know, coding agents that were where these agents um this agent loop was seen most most often. Where yeah, there's kind of like a lot of sub features like rejection, you know, seeing it's thinking, seeing 

seeing how it works. Um Great. And now we have the uh the butterfly life cycle on the canvas. Pretty cool. However, this was still not really enough because as as cool as this was, it still felt like I don't know. It felt like I was handing my keyboard to some some other AI rather than someone collaborating with me. Um although this model has been used really well in uh a lot of design apps that use Teal Draw, uh things like Lovelace or 

Magic Path, um and in in education, especially where you have this kind of tutor of like, "Help me with my homework and help me fill out my um you know, uh Oh gosh, let's see if I can do this on the fly. Steve Ruiz uh class, you know, age, whatever. Um and you can kind of ask it to like uh complete my D&D character 

sheet. All right. And it'll it'll kind of pick up what you're doing and fill out forms and do it do do fun stuff like this. Maybe I'll come back to that as it as it kind of chugs along. The what I really wanted is like to bring the the agent out of the sidebar and into the the canvas itself. Um Oh, I'm a fighter. Nice. Nice. All right, I'll take that. Uh and so, we did. And we did it with fairies, which maybe maybe you saw, maybe not. Um 

these are like little little guys on the on the canvas. You can kind of throw them around. Uh they don't like to be held for very long. They'll start freaking out. Uh yeah, okay. So, uh and uh but you can do the same thing like, you know, draw a a draw cat or something like that. Now, putting the agents on the canvas have a whole bunch of interesting things. You can see the state of the agent, right? These are multiple agents that I'm kind of running in in coding terms, these would be multiple terminal windows or something like that. 

Or this would be in composer composer. But you can kind of see what they're doing in a way that uh uh hang on. I'm zoomed way out. I did all the sprites myself. Um and you know, not only can you kind of see it's thinking, but you can see its action. You can see where it where in the project it's sort of like acting relative to the other um other agents. So, and you know, these other agents can can see each other what they're doing. So, if I ask this one to draw um a hat on 

the cat, uh and I draw this one uh draw the cat's neck. It looks like we missed the we missed the neck. Uh they'll they'll they'll get to work, right? And they're they're able to kind of work with each other's stuff at the same time. Um but we could also ask them to work together. So, if I grab all three of these uh these fairies fairies, Helen, and Joan, um draw some more 

animals. Uh one of them will be elected leader. So, this one is is the leader. And it's going to go scout kind of what's going on on the canvas, and then it's going to create a to-do list, and it's going to delegate that to-do list to the other agents, right? Um this is all like we we were doing this in like December October of last year. Uh and we're figuring this stuff out at the same time that a lot of people were figuring out agent orchestration. This idea of like, okay, how do we give them 

shared state? How do we uh you know, have a leader follower? Like, how do we manage the fact that these things are essentially blind while they're working? And prevent them from kind of overlapping uh in terms of like what they're doing. And so, you can kind of see the the the leader here isn't doing any of the work. Uh but it is going to kind of like observe Oh, no, that's that's the leader. That's the leader. Um it's observing. Uh uh and and judging and and establishing whether this is like done or not and and 

whether it's done correctly. Um Still not enough. Right? Fairies are fun. If you want to play with this, by the way, this is at fairies.tldraw.com. Um in the same way that Make Real was a really good introduction to um to just AI at all, right? Draw something, click a button. Um fairies is a great way to talk about like multiple agents kind of working together. 

Uh and they can do real work. Let me try and grab a like this is a big description of like an ebook or something like that. And if I summon my fairies, uh uh make this make the make make the wireframes for this app. Cool. And I'll I'll just kind of let them let them get to work while we keep talking. Um the started 10 minutes later. I'm going to I'm going to take another 5 minutes 

before I jump. Uh the next step for this one is to to kind of give more access to the canvas to the agents. Um and there's really we started to kind of run into the barriers of of safety. Like, what is actually safe to to do with our hackable thing for for users? Um because we have a runtime API. You can just code against it, right? And AI is really good at coding. So, maybe we could do some sandboxed, you know, 

stuff. But no, because we need the DOM. We need the kind of the browser as a way to see what's going on. We need to be able to generate screenshots, all this stuff. Um so, we decided to use our uh our desktop app instead. So, I over the holidays I threw together a um an app that does an electron wrapper that wrapped tldraw. Uh and I opened a port essentially. I said, you know, okay, Claude, like make a little HTTP server and and open a put up an endpoint. And anything that gets posted 

to that endpoint, uh treat it as JavaScript and run it. Which is a terrible idea. Not a good Like, don't don't don't do that on on your app. However, for an an offline desktop app that is file-based, like what's the worst that could happen? You could hurt yourself, I guess, but you're not going to hurt the rest of me. Uh and look at them look at them going. It's building my little ebook reader. It's fantastic. Thank you, fairies. Doing the the 

Uh so so, what does that What does that give us though? Um I'm going to I'm going to skip the demo where uh as you can imagine, I could I could say, hey, visualize this code. Make a diagram. Cool. All right, I'm going to change the the diagram. Update the code to match the diagram. Easy, right? You can have these kind of like, let's pull up the the level of abstraction that we want. Um but the the more surprising stuff was actually where I was like, you know, okay, like check this out. Uh I'm going to draw a little user interface or whatever, right? 

And I want this to be uh leg length. And I want this to be a t-shirt color. Uh and even though tldraw doesn't really have the ability to we don't have like primitives for on hover, on click. It's not like it's not a fully thing. This thing can write code against the editor. So, like uh make it interactive. And and we'll see we'll see where it 

gets to. Um so far, the results on this have been like really really cool in ways that are super strange and disturbing. Uh because like asking like the AIs are like, sure, let's do some scripts script injection, right? Like, that's the way that it documents itself is like, this is how you you should do this. Um it has no qualms at all, by the way, changing stuff that's on your desktop on your computer. If you've ever wanted to like, for example, 

like we uh one of our team, Max, was like, you know what? I don't like podcasts in my Spotify. I want to get rid of podcasts in my Spotify app. Claude, can you just do that? And it's like, sure. Let me go through the minified code of the bundle of the thing. Let me just rip and tear. Uh and it's happy to do it. It makes them happy. Uh they like it. Um oh, what the [ \_\_ ] was that? Um I don't even know what you did. You made a an HTML What the 

What? Like, it it created a new HTML site on this? And this is the pointer? It's not even a slider. No, I I want to I wanted in in the tldraw. All right. Yeah, we don't we we love it. It's blinking as well. I don't know if you caught that. Come on, do it. Yeah, there we go. Let's see if it can Come on, let's go. Um So, yeah, like there's really like uh 

no limit to what what what it can do with the desktop app, and it's happy to do it in a way that um I can almost tell that it it it uh would love to do this to websites. Like, it would love like just Let me just get my get my claws in there. Um all right, come on, come on. Still not working. We're going to we're going to we're we're going to we're going to go. Set up the interactivity. Come on. Um this is going to be really fun. I think we're going to just release this. Uh we're the um I mean, the it is released, but 

the uh the notion that you can take like I love local-first apps. I love file-over-app. I love There's all these ideas that up to now have kind of been curiosities and uh almost like Hang on. Oh, come on. Oh, that's such a such a disappointment. We're going to have to catch me later. I'll make it work. Uh but now actually the like the idea of a 

local file-based thing that is is able to expose itself to to um to to Claude and agents like locally in order to to essentially script inject kind of motivates a lot of that that stuff which previously was idealistic into like, well, that's the only way that you could do this. If you really want to maximize the agency in order to maximize what it can do and take the risk uh and take on that risk, then you you kind of just need to hand that to the user and say, good luck. Um I think open Claude does this pretty well. But like, this these are sharp 

tools. Have fun, you know? Anyway, uh that is my agents on the canvas talk. Uh work continues. If you want to play with the fairies, I highly recommend it cuz it's super fun, and you will find things that surprise you that have surprised me. Uh they have IRC as well. Let me see. Yeah, anyway. Uh and if you want to follow along with tldraw, we are on Twitter X at tldraw, and then 

I'm at Steve Ruiz okay. I post a lot about this stuff. So, uh thank you for coming. Cheers. 

<p>
 <span data-rw-start="14.68" data-rw-transcript-version="2">
 Hello. Hey, I'm going to, I'm going to
 </span>
 <span data-rw-start="16.8" data-rw-transcript-version="2">
 kick off.
 </span>
 <span data-rw-start="17.88" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="18.88" data-rw-transcript-version="2">
 sorry, we're starting a little bit late
 </span>
 <span data-rw-start="20.12" data-rw-transcript-version="2">
 here.
 </span>
 <span data-rw-start="22.32" data-rw-transcript-version="2">
 I am Steve Ruiz
 </span>
 <span data-rw-start="25.4" data-rw-transcript-version="2">
 from Teal Draw. Does anyone know Teal
 </span>
 <span data-rw-start="27.2" data-rw-transcript-version="2">
 Draw? Yes. Hey, all right, fans, fans in
 </span>
 <span data-rw-start="30.08" data-rw-transcript-version="2">
 the room. Uh, if you don't know Teal
 </span>
 <span data-rw-start="31.4" data-rw-transcript-version="2">
 Draw, Teal Draw is kind of, kind of, a
 </span>
 <span data-rw-start="32.92" data-rw-transcript-version="2">
 couple of things.
 </span>
 <span data-rw-start="34.68" data-rw-transcript-version="2">
 Teal Draw is a
 </span>
 <span data-rw-start="36.68" data-rw-transcript-version="2">
 online whiteboard. You can go to it.
 </span>
 <span data-rw-start="38.2" data-rw-transcript-version="2">
 It's free. It's really nice.
 </span>
 <span data-rw-start="39.8" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="41.64" data-rw-transcript-version="2">
 I'm going to be using it for my slides.
 </span>
 <span data-rw-start="43.92" data-rw-transcript-version="2">
 Uh, Teal Draw is also a startup. We're
 </span>
 <span data-rw-start="45.32" data-rw-transcript-version="2">
 based here in London. And, Teal Draw is
 </span>
 <span data-rw-start="48" data-rw-transcript-version="2">
 also an SDK, something that you can use
 </span>
 <span data-rw-start="50.96" data-rw-transcript-version="2">
 to build other products. So, if you've
 </span>
 <span data-rw-start="53.52" data-rw-transcript-version="2">
 used, uh, Replit's new
 </span>
 <span data-rw-start="55.92" data-rw-transcript-version="2">
 um,
 </span>
 <span data-rw-start="57.68" data-rw-transcript-version="2">
 uh, agent canvas, then that's built with
 </span>
 <span data-rw-start="60.32" data-rw-transcript-version="2">
 our canvas. If you've used, uh,
 </span>
 <span data-rw-start="62.72" data-rw-transcript-version="2">
 um,
 </span>
 <span data-rw-start="64.04" data-rw-transcript-version="2">
 Luma AI's new canvas, that's built with
 </span>
 <span data-rw-start="66.64" data-rw-transcript-version="2">
 our canvas.
 </span>
</p>
<p>
 <span data-rw-start="67.76" data-rw-transcript-version="2">
 If you've used Stitches' new canvas,
 </span>
 <span data-rw-start="69.68" data-rw-transcript-version="2">
 that's not built with our canvas.
 </span>
 <span data-rw-start="72.32" data-rw-transcript-version="2">
 But, if you go into this like kind of uh
 </span>
 <span data-rw-start="75.48" data-rw-transcript-version="2">
 um annotate mode,
 </span>
 <span data-rw-start="78.96" data-rw-transcript-version="2">
 this actually is our canvas. So, we're
 </span>
 <span data-rw-start="81.52" data-rw-transcript-version="2">
 we're in there somewhere. It's an Angular
 </span>
 <span data-rw-start="83.72" data-rw-transcript-version="2">
 app, you know. Uh
 </span>
 <span data-rw-start="85.6" data-rw-transcript-version="2">
 So, anyway, um
 </span>
 <span data-rw-start="87.12" data-rw-transcript-version="2">
 Tldraw is again a company that makes a
 </span>
 <span data-rw-start="89.68" data-rw-transcript-version="2">
 whiteboard, makes whiteboard SDK.
 </span>
 <span data-rw-start="92" data-rw-transcript-version="2">
 Part of the idea with the SDK is that
 </span>
 <span data-rw-start="93.48" data-rw-transcript-version="2">
 you can build cool things with uh with
 </span>
 <span data-rw-start="95.16" data-rw-transcript-version="2">
 the SDK,
 </span>
 <span data-rw-start="96.44" data-rw-transcript-version="2">
 which means it's part of my job to build
 </span>
 <span data-rw-start="97.96" data-rw-transcript-version="2">
 cool things with the SDK to prove it.
 </span>
 <span data-rw-start="101.24" data-rw-transcript-version="2">
 Um, and a lot of those things recently
 </span>
 <span data-rw-start="102.96" data-rw-transcript-version="2">
 have involved AI, right? Hackable
 </span>
 <span data-rw-start="107" data-rw-transcript-version="2">
 canvas runtime,
 </span>
 <span data-rw-start="108.92" data-rw-transcript-version="2">
 built with React. In fact, the canvas is
 </span>
 <span data-rw-start="111.12" data-rw-transcript-version="2">
 also just React components. So,
 </span>
 <span data-rw-start="113.04" data-rw-transcript-version="2">
 component, component, component.
 </span>
 <span data-rw-start="114.8" data-rw-transcript-version="2">
 Um, which means you can do some pretty
 </span>
 <span data-rw-start="116.16" data-rw-transcript-version="2">
 cool stuff.
 </span>
</p>
<p>
 <span data-rw-start="117.76" data-rw-transcript-version="2">
 Uh, first one, uh, I'm going to be at the
 </span>
 <span data-rw-start="118.92" data-rw-transcript-version="2">
 mercy of the demo gods here in the, the
 </span>
 <span data-rw-start="120.6" data-rw-transcript-version="2">
 internet and, and, and other things. So,
 </span>
 <span data-rw-start="122.36" data-rw-transcript-version="2">
 uh, bear with me here.
 </span>
 <span data-rw-start="124.72" data-rw-transcript-version="2">
 Um, does anyone remember this app Make
 </span>
 <span data-rw-start="128.64" data-rw-transcript-version="2">
 Real? Maybe, maybe this tweet, uh, about
 </span>
 <span data-rw-start="131.92" data-rw-transcript-version="2">
 Make Real. Did anyone, did anyone
 </span>
 <span data-rw-start="133.08" data-rw-transcript-version="2">
 remember seeing this tweet back in 2023
 </span>
 <span data-rw-start="135.24" data-rw-transcript-version="2">
 when the vision models came out? All
 </span>
 <span data-rw-start="136.4" data-rw-transcript-version="2">
 right, cool.
 </span>
</p>
<p>
 <span data-rw-start="137.48" data-rw-transcript-version="2">
 Uh, this was one of the first projects to
 </span>
 <span data-rw-start="138.96" data-rw-transcript-version="2">
 kind of like break containment, uh, in, um
 </span>
 <span data-rw-start="142.96" data-rw-transcript-version="2">
 in AI.
 </span>
</p>
<p>
 <span data-rw-start="145.6" data-rw-transcript-version="2">
 Don't, we're going to go to my phone.
 </span>
 <span data-rw-start="147.56" data-rw-transcript-version="2">
 [ \_\_ ] this.
 </span>
 <span data-rw-start="150" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="151.16" data-rw-transcript-version="2">
 which, which may, may itself be a
 </span>
 <span data-rw-start="152.64" data-rw-transcript-version="2">
 disaster. Uh,
 </span>
 <span data-rw-start="154.88" data-rw-transcript-version="2">
 So, the basic idea with Make Real
 </span>
 <span data-rw-start="157" data-rw-transcript-version="2">
 was that you could, um,
 </span>
 <span data-rw-start="158.92" data-rw-transcript-version="2">
 use a canvas, draw this
 </span>
 <span data-rw-start="160.68" data-rw-transcript-version="2">
 and send that to a, a model, and have
 </span>
 <span data-rw-start="162.56" data-rw-transcript-version="2">
 it make it into a working prototype,
 </span>
 <span data-rw-start="164.32" data-rw-transcript-version="2">
 which sounds very, very quaint in 2026.
 </span>
</p>
<p>
 <span data-rw-start="167.16" data-rw-transcript-version="2">
 But, in 2023, it was all the rage
 </span>
 <span data-rw-start="169.04" data-rw-transcript-version="2">
 because there was no lovable, there was
 </span>
 <span data-rw-start="170.84" data-rw-transcript-version="2">
 no kind of vibe coding hadn't been
 </span>
 <span data-rw-start="172.32" data-rw-transcript-version="2">
 termed or coined as a as a term. Uh and
 </span>
 <span data-rw-start="175.52" data-rw-transcript-version="2">
 so, this was one of the first projects
 </span>
 <span data-rw-start="177.32" data-rw-transcript-version="2">
 where non-technical people could
 </span>
 <span data-rw-start="179.72" data-rw-transcript-version="2">
 make technical stuff without having to
 </span>
 <span data-rw-start="182.28" data-rw-transcript-version="2">
 code or to look at code.
 </span>
 <span data-rw-start="184.72" data-rw-transcript-version="2">
 And so again, we are at the mercy of the
 </span>
 <span data-rw-start="186.4" data-rw-transcript-version="2">
 the uh
 </span>
 <span data-rw-start="188.2" data-rw-transcript-version="2">
 several
 </span>
 <span data-rw-start="189.48" data-rw-transcript-version="2">
 [ \_\_ ] various internet uh
 </span>
 <span data-rw-start="192.72" data-rw-transcript-version="2">
 internet gods. So, so we'll see. I'm
 </span>
 <span data-rw-start="194.16" data-rw-transcript-version="2">
 going to I’m going to let this cook for
 </span>
 <span data-rw-start="195.2" data-rw-transcript-version="2">
 a minute. Um but at the risk of leaking
 </span>
 <span data-rw-start="198.32" data-rw-transcript-version="2">
 my API keys, I will try and switch to a
 </span>
 <span data-rw-start="200.84" data-rw-transcript-version="2">
 faster model. Oh, no, it’s coming.
 </span>
 <span data-rw-start="202.92" data-rw-transcript-version="2">
 All right. Maybe I just gave it
 </span>
 <span data-rw-start="204.48" data-rw-transcript-version="2">
 something hard to uh hard to work on.
 </span>
 <span data-rw-start="207.16" data-rw-transcript-version="2">
 We’ll see. Hang on a second.
 </span>
 <span data-rw-start="210.56" data-rw-transcript-version="2">
 Basic idea,
 </span>
 <span data-rw-start="212.28" data-rw-transcript-version="2">
 something like that.
 </span>
 <span data-rw-start="214.04" data-rw-transcript-version="2">
 Uh yeah, there there There’s my API
 </span>
 <span data-rw-start="216.8" data-rw-transcript-version="2">
 keys. I always got to rotate them every
 </span>
 <span data-rw-start="218.12" data-rw-transcript-version="2">
 time I uh do this demo.
 </span>
</p>
<p>
 <span data-rw-start="220.4" data-rw-transcript-version="2">
 Sadly, we'll see how much gets spent before I get done
 </span>
 <span data-rw-start="223.48" data-rw-transcript-version="2">
 with the talk.
 </span>
 <span data-rw-start="225.16" data-rw-transcript-version="2">
 Um, but it is a very simple problem. It's
 </span>
 <span data-rw-start="228.64" data-rw-transcript-version="2">
 just like go, go make this interactive.
 </span>
 <span data-rw-start="230.8" data-rw-transcript-version="2">
 This is, uh, this is not what I asked for,
 </span>
 <span data-rw-start="232.92" data-rw-transcript-version="2">
 but we'll see.
 </span>
 <span data-rw-start="234.16" data-rw-transcript-version="2">
 All right, good job. Cool. And this is a
 </span>
 <span data-rw-start="236.04" data-rw-transcript-version="2">
 this is a working, working thing, which
 </span>
 <span data-rw-start="237.88" data-rw-transcript-version="2">
 is great. It's like a real little bit of
 </span>
 <span data-rw-start="239.6" data-rw-transcript-version="2">
 HTML.
 </span>
</p>
<p>
 <span data-rw-start="240.88" data-rw-transcript-version="2">
 But, you could also annotate on top of
 </span>
 <span data-rw-start="242.28" data-rw-transcript-version="2">
 it. And you could say like, "Hey, uh,
 </span>
 <span data-rw-start="244.48" data-rw-transcript-version="2">
 actually, make this green."
 </span>
 <span data-rw-start="247.52" data-rw-transcript-version="2">
 And why don't we use these colors?
 </span>
 <span data-rw-start="250.52" data-rw-transcript-version="2">
 I'm going to make this red and, uh,
 </span>
 <span data-rw-start="254.36" data-rw-transcript-version="2">
 and, and, black. Um,
 </span>
 <span data-rw-start="256.959" data-rw-transcript-version="2">
 use these colors.
 </span>
 <span data-rw-start="258.6" data-rw-transcript-version="2">
 Right? And so, you're kind of
 </span>
 <span data-rw-start="259.6" data-rw-transcript-version="2">
 constructing a prompt here, even the
 </span>
 <span data-rw-start="261.359" data-rw-transcript-version="2">
 prompt that includes the old, uh, website.
 </span>
 <span data-rw-start="265.36" data-rw-transcript-version="2">
 And, uh,
 </span>
 <span data-rw-start="267.56" data-rw-transcript-version="2">
 there's not many apps that have actually
 </span>
 <span data-rw-start="268.96" data-rw-transcript-version="2">
 like, kind of, use this. Only, only now,
 </span>
 <span data-rw-start="270.72" data-rw-transcript-version="2">
 only, like, the Google Stitch that I
 </span>
 <span data-rw-start="272.04" data-rw-transcript-version="2">
 Mentioned before, uh, this idea of
 </span>
 <span data-rw-start="274.32" data-rw-transcript-version="2">
 well, uh, it didn't do anything that I
 </span>
 <span data-rw-start="276.6" data-rw-transcript-version="2">
 asked it for. Terrible demo. We're going
 </span>
 <span data-rw-start="277.96" data-rw-transcript-version="2">
 to move on. Things have
 </span>
 <span data-rw-start="279.92" data-rw-transcript-version="2">
 changed in the last couple of years.
 </span>
</p>
<p>
 <span data-rw-start="282.12" data-rw-transcript-version="2">
 Anyway,
 </span>
 <span data-rw-start="283.52" data-rw-transcript-version="2">
 uh, there was another one in Teal Draw
 </span>
 <span data-rw-start="284.84" data-rw-transcript-version="2">
 computer, which I’m actually not going
 </span>
 <span data-rw-start="286.12" data-rw-transcript-version="2">
 to go into, but this was, uh, a couple of
 </span>
 <span data-rw-start="288.52" data-rw-transcript-version="2">
 like chains of prompts.
 </span>
 <span data-rw-start="290.6" data-rw-transcript-version="2">
 But, eventually, we, we were like, "Hey,
 </span>
 <span data-rw-start="292.6" data-rw-transcript-version="2">
 AI on the canvas actually might be
 </span>
 <span data-rw-start="293.8" data-rw-transcript-version="2">
 pretty cool. Maybe we should, um, have the
 </span>
 <span data-rw-start="297.16" data-rw-transcript-version="2">
 AI kind of
 </span>
 <span data-rw-start="298.4" data-rw-transcript-version="2">
 work as a collaborator, like work with
 </span>
 <span data-rw-start="300.16" data-rw-transcript-version="2">
 you on the canvas."
 </span>
 <span data-rw-start="301.52" data-rw-transcript-version="2">
 So, the first one of those was
 </span>
 <span data-rw-start="304.88" data-rw-transcript-version="2">
 pretty, pretty straightforward idea where
 </span>
 <span data-rw-start="307.08" data-rw-transcript-version="2">
 you could say, like, you know, draw a
 </span>
 <span data-rw-start="308.44" data-rw-transcript-version="2">
 cat.
 </span>
</p>
<p>
 <span data-rw-start="310.16" data-rw-transcript-version="2">
 You could do anything. You could say, um,
 </span>
 <span data-rw-start="313.56" data-rw-transcript-version="2">
 draw me a diagram, you know, finish my
 </span>
 <span data-rw-start="315.36" data-rw-transcript-version="2">
 slides, complete this graph that I'm
 </span>
 <span data-rw-start="316.76" data-rw-transcript-version="2">
 working on, things like that. Uh, and
 </span>
 <span data-rw-start="318.88" data-rw-transcript-version="2">
 Unlike maybe image models, uh, like diffusion models and things like that,
 </span>
 <span data-rw-start="321.24" data-rw-transcript-version="2">
 it's not building an image. It is
 </span>
 <span data-rw-start="322.8" data-rw-transcript-version="2">
 using text-structured outputs to make
 </span>
 <span data-rw-start="326.24" data-rw-transcript-version="2">
 the same things that I could make,
 </span>
 <span data-rw-start="329.76" data-rw-transcript-version="2">
 right? So, I have tools. I have
 </span>
 <span data-rw-start="331.04" data-rw-transcript-version="2">
 like circles and shapes and like this.
 </span>
</p>
<p>
 <span data-rw-start="334.72" data-rw-transcript-version="2">
 Uh, and it's funny to see how these
 </span>
 <span data-rw-start="337.16" data-rw-transcript-version="2">
 things have changed over. Oh, it's sad.
 </span>
</p>
<p>
 <span data-rw-start="344.84" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="345.88" data-rw-transcript-version="2">
 but, uh, the, uh,
 </span>
 <span data-rw-start="348.04" data-rw-transcript-version="2">
 you know, the fun of this is as a way
 </span>
 <span data-rw-start="350.8" data-rw-transcript-version="2">
 of exploring the model and what the
 </span>
 <span data-rw-start="352.4" data-rw-transcript-version="2">
 model knows and how it can comport all
 </span>
 <span data-rw-start="354.08" data-rw-transcript-version="2">
 that stuff. Uh, make the cat blow out the
 </span>
 <span data-rw-start="357.08" data-rw-transcript-version="2">
 candle.
 </span>
</p>
<p>
 <span data-rw-start="358.36" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="359.48" data-rw-transcript-version="2">
 it's pretty cool.
 </span>
</p>
<p>
 <span data-rw-start="361.16" data-rw-transcript-version="2">
 You could also do something like, uh, draw
 </span>
 <span data-rw-start="362.72" data-rw-transcript-version="2">
 a mouse. So, multiple, um, multiple
 </span>
 <span data-rw-start="364.88" data-rw-transcript-version="2">
 prompts at the same time on different
 </span>
 <span data-rw-start="366.16" data-rw-transcript-version="2">
 parts. And so, even though I didn't tell
 </span>
 <span data-rw-start="367.76" data-rw-transcript-version="2">
 it what a candle was, and I certainly
 </span>
 <span data-rw-start="369.72" data-rw-transcript-version="2">
 like, the application doesn't know what a
 </span>
 <span data-rw-start="371.08" data-rw-transcript-version="2">
 candle is.
 </span>
</p>
<p>
 <span data-rw-start="372.56" data-rw-transcript-version="2">
 Uh, and I'm not even sure that cats can
 </span>
 <span data-rw-start="376.04" data-rw-transcript-version="2">
 like blow.
 </span>
 <span data-rw-start="377.36" data-rw-transcript-version="2">
 But, it's correctly interpreted that and kind
 </span>
 <span data-rw-start="378.84" data-rw-transcript-version="2">
 of incorporated into the into the
 </span>
 <span data-rw-start="381.84" data-rw-transcript-version="2">
 design. So,
 </span>
 <span data-rw-start="383.2" data-rw-transcript-version="2">
 Uh, with incredible detail as well.
 </span>
 <span data-rw-start="388.12" data-rw-transcript-version="2">
 Still sad. Uh,
 </span>
 <span data-rw-start="389.52" data-rw-transcript-version="2">
 so, the um,
 </span>
 <span data-rw-start="391.04" data-rw-transcript-version="2">
 this was really fun because this is like
 </span>
 <span data-rw-start="393.04" data-rw-transcript-version="2">
 solving a lot of problems that
 </span>
 <span data-rw-start="396" data-rw-transcript-version="2">
 might not be obvious. Like, like, vision
 </span>
 <span data-rw-start="397.52" data-rw-transcript-version="2">
 models, when it comes to to structured
 </span>
 <span data-rw-start="399.6" data-rw-transcript-version="2">
 data, um,
 </span>
 <span data-rw-start="401.88" data-rw-transcript-version="2">
 number one, there's much less vision
 </span>
 <span data-rw-start="403.84" data-rw-transcript-version="2">
 training data than there is for text. Uh,
 </span>
 <span data-rw-start="406.04" data-rw-transcript-version="2">
 number two, a lot of that training data
 </span>
 <span data-rw-start="407.56" data-rw-transcript-version="2">
 like conflicts in ways that text does
 </span>
 <span data-rw-start="409.6" data-rw-transcript-version="2">
 not, and other other types of things
 </span>
 <span data-rw-start="411.4" data-rw-transcript-version="2">
 don't. So, for example, the the Y axis
 </span>
 <span data-rw-start="413.76" data-rw-transcript-version="2">
 on a on a Cartesian graph,
 </span>
 <span data-rw-start="415.8" data-rw-transcript-version="2">
 as you go up, that number goes up,
 </span>
 <span data-rw-start="424.28" data-rw-transcript-version="2">
 Right? The top left corner is zero, your
 </span>
 <span data-rw-start="426.44" data-rw-transcript-version="2">
 top left corner here, but as you go
 </span>
 <span data-rw-start="428.24" data-rw-transcript-version="2">
 down, the Y goes up.
 </span>
</p>
<p>
 <span data-rw-start="430.76" data-rw-transcript-version="2">
 There's left, right, like there's your
 </span>
 <span data-rw-start="433.2" data-rw-transcript-version="2">
 left, there's stage left, there's all
 </span>
 <span data-rw-start="435.76" data-rw-transcript-version="2">
 sorts of uh uh things that conflict
 </span>
 <span data-rw-start="438.8" data-rw-transcript-version="2">
 within language uh and within images.
 </span>
 <span data-rw-start="440.96" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="441.84" data-rw-transcript-version="2">
 um,
 </span>
 <span data-rw-start="443.88" data-rw-transcript-version="2">
 training the model to kind of behave
 </span>
 <span data-rw-start="445.8" data-rw-transcript-version="2">
 predictably and produce things like
 </span>
 <span data-rw-start="447.48" data-rw-transcript-version="2">
 this is uh was really well. I used
 </span>
 <span data-rw-start="449.76" data-rw-transcript-version="2">
 training, uh, prompt engineering the model
 </span>
 <span data-rw-start="451.92" data-rw-transcript-version="2">
 to
 </span>
 <span data-rw-start="453.2" data-rw-transcript-version="2">
 do it was really tricky. But,
 </span>
 <span data-rw-start="454.84" data-rw-transcript-version="2">
 this was fun, um, but we felt like it didn't go really far enough because it
 </span>
 <span data-rw-start="458.72" data-rw-transcript-version="2">
 was just one shotting, right?
 </span>
 <span data-rw-start="460.68" data-rw-transcript-version="2">
 We wanted to do an agent. So, this is
 </span>
 <span data-rw-start="462.12" data-rw-transcript-version="2">
 what Cursor looked like back in, uh,
 </span>
 <span data-rw-start="464.72" data-rw-transcript-version="2">
 in 2025 or something like that when I
 </span>
 <span data-rw-start="466.32" data-rw-transcript-version="2">
 did this.
 </span>
 <span data-rw-start="467.36" data-rw-transcript-version="2">
 Um, drew a diagram, uh, of the life
 </span>
 <span data-rw-start="473.36" data-rw-transcript-version="2">
 cycle of a butterfly.
 </span>
 <span data-rw-start="479.2" data-rw-transcript-version="2">
 So, this put it into a kind of like
 </span>
 <span data-rw-start="480.6" data-rw-transcript-version="2">
 Agentic loop, like you might have seen
 </span>
 <span data-rw-start="482.12" data-rw-transcript-version="2">
 seen elsewhere.
 </span>
</p>
<p>
 <span data-rw-start="483.36" data-rw-transcript-version="2">
 Um, but I'm sure you interact with
 </span>
 <span data-rw-start="485.96" data-rw-transcript-version="2">
 dozens of times a day by now for this
 </span>
 <span data-rw-start="488" data-rw-transcript-version="2">
 crowd. Um, where you have it produce an
 </span>
 <span data-rw-start="490.84" data-rw-transcript-version="2">
 output and then review the output and
 </span>
 <span data-rw-start="493.6" data-rw-transcript-version="2">
 kind of iterate until it thinks it's
 </span>
 <span data-rw-start="495.04" data-rw-transcript-version="2">
 done.
 </span>
</p>
<p>
 <span data-rw-start="495.96" data-rw-transcript-version="2">
 Um, and we really tried to adhere to the
 </span>
 <span data-rw-start="498.16" data-rw-transcript-version="2">
 conventions at the time of, um,
 </span>
 <span data-rw-start="500.88" data-rw-transcript-version="2">
 you know, coding agents that were, where
 </span>
 <span data-rw-start="502.64" data-rw-transcript-version="2">
 these agents, um, this agent loop was seen
 </span>
 <span data-rw-start="504.8" data-rw-transcript-version="2">
 most often.
 </span>
 <span data-rw-start="506.56" data-rw-transcript-version="2">
 Where, yeah, there's kind of like a lot
 </span>
 <span data-rw-start="507.96" data-rw-transcript-version="2">
 of subfeatures like rejection, you
 </span>
 <span data-rw-start="509.96" data-rw-transcript-version="2">
 know, seeing it's thinking, seeing
 </span>
 <span data-rw-start="511.6" data-rw-transcript-version="2">
 seeing how it works. Um
 </span>
 <span data-rw-start="514" data-rw-transcript-version="2">
 Great. And now we have the, uh, the
 </span>
 <span data-rw-start="517.2" data-rw-transcript-version="2">
 butterfly life cycle on the canvas.
 </span>
</p>
<p>
 <span data-rw-start="520" data-rw-transcript-version="2">
 Pretty cool.
 </span>
 <span data-rw-start="521.68" data-rw-transcript-version="2">
 However, this was still not really
 </span>
 <span data-rw-start="524.159" data-rw-transcript-version="2">
 enough because, as, as cool as this was,
 </span>
 <span data-rw-start="526.04" data-rw-transcript-version="2">
 it still felt like
 </span>
 <span data-rw-start="527.88" data-rw-transcript-version="2">
 I don't know. It felt like I was handing
 </span>
 <span data-rw-start="529.12" data-rw-transcript-version="2">
 my keyboard to some, some other AI, rather.
 </span>
</p>
<p>
 <span data-rw-start="531.72" data-rw-transcript-version="2">
 Than someone collaborating with me. Um
 </span>
 <span data-rw-start="534.6" data-rw-transcript-version="2">
 Although this model has been used really
 </span>
 <span data-rw-start="536.16" data-rw-transcript-version="2">
 well in uh a lot of design apps that use
 </span>
 <span data-rw-start="538.8" data-rw-transcript-version="2">
 Teal Draw, uh things like Lovelace or
 </span>
 <span data-rw-start="541" data-rw-transcript-version="2">
 Magic Path, um
 </span>
 <span data-rw-start="543.32" data-rw-transcript-version="2">
 and in in education, especially where
 </span>
 <span data-rw-start="545.56" data-rw-transcript-version="2">
 you have this kind of tutor of like,
 </span>
 <span data-rw-start="546.76" data-rw-transcript-version="2">
 "Help me with my homework and help me
 </span>
 <span data-rw-start="548.68" data-rw-transcript-version="2">
 fill out my um you know,
 </span>
 <span data-rw-start="551.2" data-rw-transcript-version="2">
 uh
 </span>
 <span data-rw-start="552.2" data-rw-transcript-version="2">
 Oh gosh, let's see if I can do this on
 </span>
 <span data-rw-start="554.16" data-rw-transcript-version="2">
 the fly. Steve Ruiz
 </span>
 <span data-rw-start="556.56" data-rw-transcript-version="2">
 uh
 </span>
 <span data-rw-start="557.6" data-rw-transcript-version="2">
 class,
 </span>
 <span data-rw-start="559.08" data-rw-transcript-version="2">
 you know, age, whatever.
 </span>
 <span data-rw-start="561.68" data-rw-transcript-version="2">
 Um and you can kind of ask it to like uh
 </span>
 <span data-rw-start="567.16" data-rw-transcript-version="2">
 complete my D&amp;D
 </span>
 <span data-rw-start="569.76" data-rw-transcript-version="2">
 character
 </span>
 <span data-rw-start="571.2" data-rw-transcript-version="2">
 sheet.
 </span>
 <span data-rw-start="572.48" data-rw-transcript-version="2">
 All right. And it'll it’ll kind of pick
 </span>
 <span data-rw-start="574.12" data-rw-transcript-version="2">
 up what you're doing and fill out forms
 </span>
 <span data-rw-start="575.68" data-rw-transcript-version="2">
 and do it do do fun stuff like this.
 </span>
 <span data-rw-start="578.2" data-rw-transcript-version="2">
 Maybe I'll come back to that as it as it
 </span>
 <span data-rw-start="579.72" data-rw-transcript-version="2">
 kind of chugs along.
 </span>
 <span data-rw-start="581.36" data-rw-transcript-version="2">
 The what I really wanted is like to
 </span>
 <span data-rw-start="583.2" data-rw-transcript-version="2">
 Bring the
 </span>
 <span data-rw-start="584.44" data-rw-transcript-version="2">
 agent out of the sidebar and into
 </span>
 <span data-rw-start="586.12" data-rw-transcript-version="2">
 the canvas itself. Um, oh, I'm a
 </span>
 <span data-rw-start="588.76" data-rw-transcript-version="2">
 fighter.
 </span>
</p>
<p>
 <span data-rw-start="591.24" data-rw-transcript-version="2">
 Nice. Nice. All right, I'll take that.
 </span>
 <span data-rw-start="594.48" data-rw-transcript-version="2">
 Uh, and so, we did. And we did it with
 </span>
 <span data-rw-start="597" data-rw-transcript-version="2">
 fairies, which maybe
 </span>
 <span data-rw-start="599.8" data-rw-transcript-version="2">
 maybe you saw, maybe not. Um,
 </span>
 <span data-rw-start="602.44" data-rw-transcript-version="2">
 these are like little, little guys on the
 </span>
 <span data-rw-start="604.12" data-rw-transcript-version="2">
 canvas. You can kind of throw
 </span>
 <span data-rw-start="605.4" data-rw-transcript-version="2">
 them around.
 </span>
 <span data-rw-start="606.76" data-rw-transcript-version="2">
 Uh, they don't like to be held for very
 </span>
 <span data-rw-start="608.6" data-rw-transcript-version="2">
 long. They'll start freaking out.
 </span>
 <span data-rw-start="610.72" data-rw-transcript-version="2">
 Uh, yeah, okay. So, uh,
 </span>
 <span data-rw-start="613.8" data-rw-transcript-version="2">
 and, uh, but you can do the same thing
 </span>
 <span data-rw-start="615.4" data-rw-transcript-version="2">
 like, you know, draw a draw cat or
 </span>
 <span data-rw-start="617.4" data-rw-transcript-version="2">
 something like that. Now, putting the
 </span>
 <span data-rw-start="618.88" data-rw-transcript-version="2">
 agents on the canvas have a whole bunch
 </span>
 <span data-rw-start="620.36" data-rw-transcript-version="2">
 of interesting things. You can see the
 </span>
 <span data-rw-start="622.44" data-rw-transcript-version="2">
 state of the agent, right? These are
 </span>
 <span data-rw-start="624.24" data-rw-transcript-version="2">
 multiple agents that I'm kind of running
 </span>
 <span data-rw-start="626.12" data-rw-transcript-version="2">
 in, in
 </span>
 <span data-rw-start="627.52" data-rw-transcript-version="2">
 coding terms, these would be multiple
 </span>
 <span data-rw-start="628.72" data-rw-transcript-version="2">
 terminal windows or something like that.
 </span>
 <span data-rw-start="630.08" data-rw-transcript-version="2">
 Or, this would be in composer, composer.
 </span>
</p>
<p>
 <span data-rw-start="632.36" data-rw-transcript-version="2">
 But you can kind of see what they're
 </span>
 <span data-rw-start="633.56" data-rw-transcript-version="2">
 doing in a way that uh uh hang on. I'm
 </span>
 <span data-rw-start="636.4" data-rw-transcript-version="2">
 zoomed way out.
 </span>
 <span data-rw-start="638.84" data-rw-transcript-version="2">
 I did all the sprites myself.
 </span>
 <span data-rw-start="643.08" data-rw-transcript-version="2">
 Um
 </span>
 <span data-rw-start="644.24" data-rw-transcript-version="2">
 and you know, not only can you kind of
 </span>
 <span data-rw-start="645.6" data-rw-transcript-version="2">
 see it's thinking, but you can see its
 </span>
 <span data-rw-start="647.08" data-rw-transcript-version="2">
 action. You can see where it is in
 </span>
 <span data-rw-start="648.84" data-rw-transcript-version="2">
 the project. It's sort of like acting
 </span>
 <span data-rw-start="651.44" data-rw-transcript-version="2">
 relative to the other um other agents.
 </span>
 <span data-rw-start="654.6" data-rw-transcript-version="2">
 So,
 </span>
 <span data-rw-start="655.68" data-rw-transcript-version="2">
 and you know, these other agents can can
 </span>
 <span data-rw-start="657.8" data-rw-transcript-version="2">
 see each other what they're doing. So,
 </span>
 <span data-rw-start="659.76" data-rw-transcript-version="2">
 if I ask this one to draw um a hat on
 </span>
 <span data-rw-start="662.28" data-rw-transcript-version="2">
 the cat,
 </span>
 <span data-rw-start="663.44" data-rw-transcript-version="2">
 uh
 </span>
 <span data-rw-start="664.2" data-rw-transcript-version="2">
 and I draw this one uh draw the cat's
 </span>
 <span data-rw-start="668.12" data-rw-transcript-version="2">
 neck.
 </span>
 <span data-rw-start="670.32" data-rw-transcript-version="2">
 It looks like we missed the, we missed
 </span>
 <span data-rw-start="671.839" data-rw-transcript-version="2">
 the neck.
 </span>
 <span data-rw-start="674.68" data-rw-transcript-version="2">
 Uh
 </span>
 <span data-rw-start="675.56" data-rw-transcript-version="2">
 they'll get to work,
 </span>
 <span data-rw-start="676.8" data-rw-transcript-version="2">
 right? And they're able to kind
 </span>
 <span data-rw-start="677.839" data-rw-transcript-version="2">
 of work with each other's stuff at the
 </span>
 <span data-rw-start="679.08" data-rw-transcript-version="2">
 same time.
 </span>
</p>
<p>
 <span data-rw-start="680.2" data-rw-transcript-version="2">
 Um, but we could also ask them to work
 </span>
 <span data-rw-start="682.28" data-rw-transcript-version="2">
 together. So, if I grab all three of
 </span>
 <span data-rw-start="684.2" data-rw-transcript-version="2">
 these, uh, these fairies—fairies, Helen,
 </span>
 <span data-rw-start="686.839" data-rw-transcript-version="2">
 and Joan—um,
 </span>
 <span data-rw-start="689.08" data-rw-transcript-version="2">
 draw some more
 </span>
 <span data-rw-start="690.64" data-rw-transcript-version="2">
 animals.
 </span>
 <span data-rw-start="692.28" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="693.72" data-rw-transcript-version="2">
 one of them will be elected leader. So,
 </span>
 <span data-rw-start="695.56" data-rw-transcript-version="2">
 this one is the leader. And it's
 </span>
 <span data-rw-start="697.44" data-rw-transcript-version="2">
 going to go scout kind of what's going
 </span>
 <span data-rw-start="699.36" data-rw-transcript-version="2">
 on on the canvas, and then it's going to
 </span>
 <span data-rw-start="700.64" data-rw-transcript-version="2">
 create a to-do list, and it's going to
 </span>
 <span data-rw-start="701.96" data-rw-transcript-version="2">
 delegate that to-do list to the other
 </span>
 <span data-rw-start="703.56" data-rw-transcript-version="2">
 agents, right?
 </span>
 <span data-rw-start="705.4" data-rw-transcript-version="2">
 Um, this is all like
 </span>
 <span data-rw-start="708.24" data-rw-transcript-version="2">
 we, we were doing this in, like, December
 </span>
 <span data-rw-start="710" data-rw-transcript-version="2">
 October of last year. Uh, and
 </span>
 <span data-rw-start="714.16" data-rw-transcript-version="2">
 we're figuring this stuff out at the
 </span>
 <span data-rw-start="715.28" data-rw-transcript-version="2">
 same time that a lot of people were
 </span>
 <span data-rw-start="716.839" data-rw-transcript-version="2">
 figuring out agent orchestration. This
 </span>
 <span data-rw-start="718.68" data-rw-transcript-version="2">
 idea of, like, okay, how do we give them
 </span>
 <span data-rw-start="720.04" data-rw-transcript-version="2">
 shared state? How do we, uh, you know,
 </span>
 <span data-rw-start="722.6" data-rw-transcript-version="2">
 have a leader-follower? Like, how do we
 </span>
 <span data-rw-start="724.12" data-rw-transcript-version="2">
 manage the fact that these things are
 </span>
 <span data-rw-start="725.36" data-rw-transcript-version="2">
 essentially blind while they're working?
 </span>
</p>
<p>
 <span data-rw-start="727.6" data-rw-transcript-version="2">
 And prevent them from kind of
 </span>
 <span data-rw-start="728.6" data-rw-transcript-version="2">
 overlapping, uh, in terms of like what
 </span>
 <span data-rw-start="730.68" data-rw-transcript-version="2">
 they're doing.
 </span>
 <span data-rw-start="731.72" data-rw-transcript-version="2">
 And so, you can kind of see the, the, the
 </span>
 <span data-rw-start="733.52" data-rw-transcript-version="2">
 leader here isn't doing any of the work.
 </span>
 <span data-rw-start="735.92" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="736.76" data-rw-transcript-version="2">
 but it is going to kind of like observe,
 </span>
 <span data-rw-start="738.76" data-rw-transcript-version="2">
 Oh, no, that's, that's the leader. That's
 </span>
 <span data-rw-start="740.36" data-rw-transcript-version="2">
 the leader. Um,
 </span>
 <span data-rw-start="742.16" data-rw-transcript-version="2">
 it's observing.
 </span>
</p>
<p>
 <span data-rw-start="744.24" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="746.44" data-rw-transcript-version="2">
 uh,
 </span>
 <span data-rw-start="747.72" data-rw-transcript-version="2">
 and judging, and establishing
 </span>
 <span data-rw-start="749.36" data-rw-transcript-version="2">
 whether this is like done or not, and
 </span>
 <span data-rw-start="751.2" data-rw-transcript-version="2">
 whether it's done correctly.
 </span>
 <span data-rw-start="753.52" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="757.64" data-rw-transcript-version="2">
 still not enough, right? Fairies are
 </span>
 <span data-rw-start="760.12" data-rw-transcript-version="2">
 fun. If you want to play with this, by
 </span>
 <span data-rw-start="761.2" data-rw-transcript-version="2">
 the way, this is at fairies.tldraw.com.
 </span>
 <span data-rw-start="764.08" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="764.88" data-rw-transcript-version="2">
 in the same way that Make Real was a
 </span>
 <span data-rw-start="766" data-rw-transcript-version="2">
 really good introduction to
 </span>
 <span data-rw-start="768.44" data-rw-transcript-version="2">
 um,
 </span>
 <span data-rw-start="770.08" data-rw-transcript-version="2">
 to
 </span>
 <span data-rw-start="771.52" data-rw-transcript-version="2">
 just AI at all, right? Draw something,
 </span>
 <span data-rw-start="774.36" data-rw-transcript-version="2">
 Click a button. Um, fairies is a great
 </span>
 <span data-rw-start="777.04" data-rw-transcript-version="2">
 way to talk about like multiple agents
 </span>
 <span data-rw-start="778.839" data-rw-transcript-version="2">
 kind of working together.
 </span>
</p>
<p>
 <span data-rw-start="780.52" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="781.56" data-rw-transcript-version="2">
 and they can do real work. Let me try
 </span>
 <span data-rw-start="783.48" data-rw-transcript-version="2">
 and grab a
 </span>
 <span data-rw-start="785.2" data-rw-transcript-version="2">
 like this is a big description of like
 </span>
 <span data-rw-start="786.76" data-rw-transcript-version="2">
 an ebook or something like that. And if
 </span>
 <span data-rw-start="789.12" data-rw-transcript-version="2">
 I summon my fairies,
 </span>
 <span data-rw-start="791.24" data-rw-transcript-version="2">
 uh,
 </span>
 <span data-rw-start="793.28" data-rw-transcript-version="2">
 uh, make this, make the, make, make the
 </span>
 <span data-rw-start="796.64" data-rw-transcript-version="2">
 wireframes
 </span>
 <span data-rw-start="798.32" data-rw-transcript-version="2">
 for this app.
 </span>
 <span data-rw-start="799.839" data-rw-transcript-version="2">
 Cool.
 </span>
 <span data-rw-start="800.64" data-rw-transcript-version="2">
 And I'll, I'll just kind of let them get to work while we keep talking.
 </span>
 <span data-rw-start="804.2" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="806.44" data-rw-transcript-version="2">
 the
 </span>
 <span data-rw-start="808.2" data-rw-transcript-version="2">
 started 10 minutes later. I'm going to
 </span>
 <span data-rw-start="809.8" data-rw-transcript-version="2">
 I'm going to take another 5 minutes
 </span>
 <span data-rw-start="811.16" data-rw-transcript-version="2">
 before I jump. Uh, the next step for this
 </span>
 <span data-rw-start="814.36" data-rw-transcript-version="2">
 one,
 </span>
 <span data-rw-start="815.839" data-rw-transcript-version="2">
 is to kind of give more access to the
 </span>
 <span data-rw-start="818.839" data-rw-transcript-version="2">
 canvas to the agents.
 </span>
 <span data-rw-start="821.24" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="823.32" data-rw-transcript-version="2">
 and there's really
 </span>
 <span data-rw-start="825.16" data-rw-transcript-version="2">
 we started to kind of run into the
 </span>
 <span data-rw-start="826.36" data-rw-transcript-version="2">
 barriers of safety. Like, what is
 </span>
 <span data-rw-start="828.6" data-rw-transcript-version="2">
 actually safe to
 </span>
 <span data-rw-start="830.16" data-rw-transcript-version="2">
 to do with our hackable thing for, for
 </span>
 <span data-rw-start="833.4" data-rw-transcript-version="2">
 users? Um, because we have a runtime API.
 </span>
</p>
<p>
 <span data-rw-start="836.16" data-rw-transcript-version="2">
 You can just code against it, right? And
 </span>
 <span data-rw-start="838.04" data-rw-transcript-version="2">
 AI is really good at coding. So, maybe
 </span>
 <span data-rw-start="839.6" data-rw-transcript-version="2">
 we could do some sandboxed, you know,
 </span>
 <span data-rw-start="841.16" data-rw-transcript-version="2">
 stuff. But no, because we need the DOM.
 </span>
</p>
<p>
 <span data-rw-start="843.36" data-rw-transcript-version="2">
 We need the kind of the browser as a way
 </span>
 <span data-rw-start="844.6" data-rw-transcript-version="2">
 to see what's going on. We need to be
 </span>
 <span data-rw-start="845.96" data-rw-transcript-version="2">
 able to generate screenshots, all this
 </span>
 <span data-rw-start="847.36" data-rw-transcript-version="2">
 stuff.
 </span>
</p>
<p>
 <span data-rw-start="848.36" data-rw-transcript-version="2">
 Um, so, we decided to use our uh our
 </span>
 <span data-rw-start="851.28" data-rw-transcript-version="2">
 desktop app instead. So, I over the
 </span>
 <span data-rw-start="854.64" data-rw-transcript-version="2">
 holidays I threw together a um
 </span>
 <span data-rw-start="857.28" data-rw-transcript-version="2">
 an app that does an electron wrapper
 </span>
 <span data-rw-start="858.6" data-rw-transcript-version="2">
 that wrapped tldraw.
 </span>
</p>
<p>
 <span data-rw-start="860.2" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="860.88" data-rw-transcript-version="2">
 and I
 </span>
 <span data-rw-start="862.12" data-rw-transcript-version="2">
 opened a port essentially. I said, you
 </span>
 <span data-rw-start="863.92" data-rw-transcript-version="2">
 know, okay, Claude, like make a little
 </span>
 <span data-rw-start="865.8" data-rw-transcript-version="2">
 HTTP server and and open a put up an
 </span>
 <span data-rw-start="868.8" data-rw-transcript-version="2">
 endpoint. And anything that gets posted
 </span>
 <span data-rw-start="871.48" data-rw-transcript-version="2">
 To that endpoint,
 </span>
 <span data-rw-start="873.04" data-rw-transcript-version="2">
 uh, treat it as JavaScript and run it.
 </span>
</p>
<p>
 <span data-rw-start="877.2" data-rw-transcript-version="2">
 Which is a terrible idea. Not a good. Like,
 </span>
 <span data-rw-start="879.24" data-rw-transcript-version="2">
 don't, don't, don't do that on your
 </span>
 <span data-rw-start="883.88" data-rw-transcript-version="2">
 app. However, for an offline desktop
 </span>
 <span data-rw-start="886.56" data-rw-transcript-version="2">
 app that is file-based, like what's the
 </span>
 <span data-rw-start="888.6" data-rw-transcript-version="2">
 worst that could happen?
 </span>
 <span data-rw-start="890.16" data-rw-transcript-version="2">
 You could hurt yourself, I guess, but
 </span>
 <span data-rw-start="891.4" data-rw-transcript-version="2">
 you're not going to hurt the rest of me.
 </span>
 <span data-rw-start="893.56" data-rw-transcript-version="2">
 Uh, and look at them. Look at them going.
 </span>
</p>
<p>
 <span data-rw-start="895.28" data-rw-transcript-version="2">
 It's building my little ebook reader.
 </span>
 <span data-rw-start="896.64" data-rw-transcript-version="2">
 It's fantastic. Thank you, fairies.
 </span>
 <span data-rw-start="899.28" data-rw-transcript-version="2">
 Doing the. The
 </span>
 <span data-rw-start="901.88" data-rw-transcript-version="2">
 Uh, so, so, what does that? What does that
 </span>
 <span data-rw-start="903.48" data-rw-transcript-version="2">
 give us, though? Um
 </span>
 <span data-rw-start="905.079" data-rw-transcript-version="2">
 I'm going to skip the demo
 </span>
 <span data-rw-start="906.28" data-rw-transcript-version="2">
 where, uh, as you can imagine, I could
 </span>
 <span data-rw-start="909.48" data-rw-transcript-version="2">
 say, hey, visualize this code.
 </span>
 <span data-rw-start="911.68" data-rw-transcript-version="2">
 Make a diagram. Cool. All right, I'm
 </span>
 <span data-rw-start="912.88" data-rw-transcript-version="2">
 going to change the diagram. Update
 </span>
 <span data-rw-start="915.04" data-rw-transcript-version="2">
 the code to match the diagram.
 </span>
 <span data-rw-start="917.48" data-rw-transcript-version="2">
 Easy, right? You can have these kinds of
 </span>
 <span data-rw-start="918.959" data-rw-transcript-version="2">
 like, let's pull up the level of
 </span>
 <span data-rw-start="920.6" data-rw-transcript-version="2">
 Abstraction that we want.
 </span>
</p>
<p>
 <span data-rw-start="922.24" data-rw-transcript-version="2">
 Um, but the more surprising stuff was
 </span>
 <span data-rw-start="924.32" data-rw-transcript-version="2">
 actually where I was like,
 </span>
 <span data-rw-start="925.92" data-rw-transcript-version="2">
 you know, okay, like check this out. Uh,
 </span>
 <span data-rw-start="927.839" data-rw-transcript-version="2">
 I'm going to draw a little user
 </span>
 <span data-rw-start="929.2" data-rw-transcript-version="2">
 interface or whatever, right?
 </span>
 <span data-rw-start="931.68" data-rw-transcript-version="2">
 And I want this to be, uh, leg length.
 </span>
 <span data-rw-start="935.16" data-rw-transcript-version="2">
 And I want this to be a T-shirt
 </span>
 <span data-rw-start="937.52" data-rw-transcript-version="2">
 color.
 </span>
 <span data-rw-start="938.92" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="940.959" data-rw-transcript-version="2">
 and even though tldraw doesn’t really
 </span>
 <span data-rw-start="942.4" data-rw-transcript-version="2">
 have the ability to, we don’t have like
 </span>
 <span data-rw-start="945.64" data-rw-transcript-version="2">
 primitives for on hover, on click. It’s
 </span>
 <span data-rw-start="947.959" data-rw-transcript-version="2">
 not like
 </span>
 <span data-rw-start="949.079" data-rw-transcript-version="2">
 it’s not a fully thing.
 </span>
 <span data-rw-start="950.4" data-rw-transcript-version="2">
 This thing can write code against
 </span>
 <span data-rw-start="952.4" data-rw-transcript-version="2">
 the editor.
 </span>
 <span data-rw-start="953.48" data-rw-transcript-version="2">
 So, like, uh, make it interactive.
 </span>
 <span data-rw-start="958.8" data-rw-transcript-version="2">
 And we’ll see, we’ll see where it
 </span>
 <span data-rw-start="960.2" data-rw-transcript-version="2">
 gets to.
 </span>
 <span data-rw-start="961.32" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="962.28" data-rw-transcript-version="2">
 so far,
 </span>
 <span data-rw-start="963.48" data-rw-transcript-version="2">
 the results on this have been like
 </span>
 <span data-rw-start="965.48" data-rw-transcript-version="2">
 really, really cool in ways that are
 </span>
 <span data-rw-start="968" data-rw-transcript-version="2">
 super strange and disturbing. Uh.
 </span>
</p>
<p>
 <span data-rw-start="971.6" data-rw-transcript-version="2">
 Because like asking like
 </span>
 <span data-rw-start="973.88" data-rw-transcript-version="2">
 the AIs are like, sure, let's do some
 </span>
 <span data-rw-start="975.32" data-rw-transcript-version="2">
 scripts script injection, right? Like,
 </span>
 <span data-rw-start="976.88" data-rw-transcript-version="2">
 that's the way that it documents itself
 </span>
 <span data-rw-start="978.6" data-rw-transcript-version="2">
 is, like, this is how you should do
 </span>
 <span data-rw-start="981" data-rw-transcript-version="2">
 this. Um,
 </span>
 <span data-rw-start="982.76" data-rw-transcript-version="2">
 it has no qualms at all, by the way,
 </span>
 <span data-rw-start="984.8" data-rw-transcript-version="2">
 changing stuff that's on your desktop on
 </span>
 <span data-rw-start="987.04" data-rw-transcript-version="2">
 your computer. If you've ever wanted to
 </span>
 <span data-rw-start="988.28" data-rw-transcript-version="2">
 like, for example,
 </span>
 <span data-rw-start="990.32" data-rw-transcript-version="2">
 like, we, uh,
 </span>
 <span data-rw-start="992" data-rw-transcript-version="2">
 one of our team, Max, was like, you know,
 </span>
 <span data-rw-start="993.52" data-rw-transcript-version="2">
 what? I don't like podcasts in my
 </span>
 <span data-rw-start="994.959" data-rw-transcript-version="2">
 Spotify. I want to get rid of podcasts
 </span>
 <span data-rw-start="996.68" data-rw-transcript-version="2">
 in my Spotify app. Claude, can you just
 </span>
 <span data-rw-start="998.44" data-rw-transcript-version="2">
 do that? And it's like, sure. Let me go
 </span>
 <span data-rw-start="1000.28" data-rw-transcript-version="2">
 through the minified code of the bundle
 </span>
 <span data-rw-start="1002.16" data-rw-transcript-version="2">
 of the thing. Let me just rip and tear.
 </span>
</p>
<p>
 <span data-rw-start="1004.6" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="1005.32" data-rw-transcript-version="2">
 and it's happy to do it. It makes them
 </span>
 <span data-rw-start="1007" data-rw-transcript-version="2">
 happy. Uh, they like it.
 </span>
 <span data-rw-start="1009.72" data-rw-transcript-version="2">
 Um, oh, what the [ \_\_ ] was that?
 </span>
 <span data-rw-start="1015.56" data-rw-transcript-version="2">
 Um,
 </span>
 <span data-rw-start="1017.44" data-rw-transcript-version="2">
 I don't even know what you did. You made
 </span>
 <span data-rw-start="1018.56" data-rw-transcript-version="2">
 an HTML. What the
 </span>
 <span data-rw-start="1021.76" data-rw-transcript-version="2">
 What? Like, it, it created a new HTML
 </span>
 <span data-rw-start="1024.28" data-rw-transcript-version="2">
 site on this?
 </span>
</p>
<p>
 <span data-rw-start="1026.16" data-rw-transcript-version="2">
 And this is the pointer? It's not even a
 </span>
 <span data-rw-start="1028" data-rw-transcript-version="2">
 slider. No, I want to, I wanted in, in
 </span>
 <span data-rw-start="1029.92" data-rw-transcript-version="2">
 the tldraw. All right. Yeah, we don't, we
 </span>
 <span data-rw-start="1033.199" data-rw-transcript-version="2">
 love it.
 </span>
 <span data-rw-start="1034.56" data-rw-transcript-version="2">
 It's blinking as well. I don't know if
 </span>
 <span data-rw-start="1035.72" data-rw-transcript-version="2">
 you caught that.
 </span>
 <span data-rw-start="1038.4" data-rw-transcript-version="2">
 Come on, do it. Yeah, there we go.
 </span>
 <span data-rw-start="1042.72" data-rw-transcript-version="2">
 Let's see if it can. Come on, let's go.
 </span>
</p>
<p>
 <span data-rw-start="1045.64" data-rw-transcript-version="2">
 Um
 </span>
 <span data-rw-start="1047.8" data-rw-transcript-version="2">
 So, yeah, like, there's really like, uh
 </span>
 <span data-rw-start="1050.4" data-rw-transcript-version="2">
 no limit to what, what, what it can do
 </span>
 <span data-rw-start="1051.92" data-rw-transcript-version="2">
 with the desktop app, and it's happy to
 </span>
 <span data-rw-start="1053.16" data-rw-transcript-version="2">
 do it in a way that, um
 </span>
 <span data-rw-start="1055.64" data-rw-transcript-version="2">
 I can almost tell that it, it, it, uh, would
 </span>
 <span data-rw-start="1057.84" data-rw-transcript-version="2">
 love to do this to websites. Like, it
 </span>
 <span data-rw-start="1059.84" data-rw-transcript-version="2">
 would love, like, just. Let me just get my
 </span>
 <span data-rw-start="1061.56" data-rw-transcript-version="2">
 claws in there.
 </span>
 <span data-rw-start="1062.96" data-rw-transcript-version="2">
 Um, all right, come on, come on.
 </span>
</p>
<p>
 <span data-rw-start="1066.72" data-rw-transcript-version="2">
 Still not working. We're going to, we're
 </span>
 <span data-rw-start="1068.16" data-rw-transcript-version="2">
 going to,
 </span>
 <span data-rw-start="1069.4" data-rw-transcript-version="2">
 we're, we're going to go.
 </span>
 <span data-rw-start="1071.52" data-rw-transcript-version="2">
 Set up the interactivity. Come on. Uh
 </span>
 <span data-rw-start="1074.32" data-rw-transcript-version="2">
 This is going to be really fun. I think.
 </span>
</p>
<p>
 <span data-rw-start="1075.24" data-rw-transcript-version="2">
 We're going to just release this. Uh, we're
 </span>
 <span data-rw-start="1076.679" data-rw-transcript-version="2">
 the, I mean, it is released, but
 </span>
 <span data-rw-start="1077.8" data-rw-transcript-version="2">
 the, the notion that you can take
 </span>
 <span data-rw-start="1080.24" data-rw-transcript-version="2">
 like I love local-first apps. I love
 </span>
 <span data-rw-start="1086.6" data-rw-transcript-version="2">
 file-over-app. I love. There are all these
 </span>
 <span data-rw-start="1088.56" data-rw-transcript-version="2">
 ideas that up to now have kind of been
 </span>
 <span data-rw-start="1090.08" data-rw-transcript-version="2">
 curiosities and
 </span>
 <span data-rw-start="1092.44" data-rw-transcript-version="2">
 uh
 </span>
 <span data-rw-start="1093.08" data-rw-transcript-version="2">
 almost like,
 </span>
 <span data-rw-start="1095.84" data-rw-transcript-version="2">
 Hang on.
 </span>
</p>
<p>
 <span data-rw-start="1097.56" data-rw-transcript-version="2">
 Oh, come on.
 </span>
 <span data-rw-start="1099.52" data-rw-transcript-version="2">
 Oh, that's such a, such a disappointment.
 </span>
 <span data-rw-start="1105" data-rw-transcript-version="2">
 We're going to have to catch me later.
 </span>
 <span data-rw-start="1107.28" data-rw-transcript-version="2">
 I'll make it work. Uh,
 </span>
 <span data-rw-start="1109.36" data-rw-transcript-version="2">
 but now, actually, the, like, the idea of a
 </span>
 <span data-rw-start="1110.8" data-rw-transcript-version="2">
 local file-based thing that is able
 </span>
 <span data-rw-start="1113.12" data-rw-transcript-version="2">
 to expose itself to, to, um,
 </span>
 <span data-rw-start="1116.32" data-rw-transcript-version="2">
 to, to, Claude and agents like locally in
 </span>
 <span data-rw-start="1118.12" data-rw-transcript-version="2">
 order to, to, essentially script inject,
 </span>
 <span data-rw-start="1120.52" data-rw-transcript-version="2">
 kind of, motivates a lot of that, that
 </span>
 <span data-rw-start="1122.44" data-rw-transcript-version="2">
 stuff, which previously was idealistic
 </span>
 <span data-rw-start="1124.24" data-rw-transcript-version="2">
 into, like, well, that's the only way
 </span>
 <span data-rw-start="1125.44" data-rw-transcript-version="2">
 that you could do this.
 </span>
</p>
<p>
 <span data-rw-start="1126.8" data-rw-transcript-version="2">
 If you really want to maximize the
 </span>
 <span data-rw-start="1128.2" data-rw-transcript-version="2">
 agency in order to maximize what it can
 </span>
 <span data-rw-start="1129.84" data-rw-transcript-version="2">
 do,
 </span>
 <span data-rw-start="1130.919" data-rw-transcript-version="2">
 and take the risk, uh, and take on that
 </span>
 <span data-rw-start="1133.4" data-rw-transcript-version="2">
 risk,
 </span>
 <span data-rw-start="1134.44" data-rw-transcript-version="2">
 then you, you kind of just need to hand
 </span>
 <span data-rw-start="1136.12" data-rw-transcript-version="2">
 that to the user and say, good luck.
 </span>
 <span data-rw-start="1138.159" data-rw-transcript-version="2">
 Um, I think OpenAI does this pretty
 </span>
 <span data-rw-start="1139.84" data-rw-transcript-version="2">
 well. But, like, these are sharp
 </span>
 <span data-rw-start="1141.8" data-rw-transcript-version="2">
 tools.
 </span>
 <span data-rw-start="1143.96" data-rw-transcript-version="2">
 Have fun, you know? Anyway,
 </span>
 <span data-rw-start="1146.44" data-rw-transcript-version="2">
 uh, that is my agents on the canvas talk.
 </span>
 <span data-rw-start="1149.88" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="1150.44" data-rw-transcript-version="2">
 work continues. If you want to play with
 </span>
 <span data-rw-start="1151.88" data-rw-transcript-version="2">
 the fairies, I highly recommend it because
 </span>
 <span data-rw-start="1153.4" data-rw-transcript-version="2">
 it's super fun, and you will find things
 </span>
 <span data-rw-start="1155.56" data-rw-transcript-version="2">
 that surprise you,
 </span>
 <span data-rw-start="1157.64" data-rw-transcript-version="2">
 that have surprised me.
 </span>
 <span data-rw-start="1159.24" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="1159.96" data-rw-transcript-version="2">
 they have IRC as well. Let me see. Yeah,
 </span>
 <span data-rw-start="1162.24" data-rw-transcript-version="2">
 anyway.
 </span>
 <span data-rw-start="1163.28" data-rw-transcript-version="2">
 Uh,
 </span>
 <span data-rw-start="1164.52" data-rw-transcript-version="2">
 and if you want to follow along with
 </span>
 <span data-rw-start="1166.32" data-rw-transcript-version="2">
 tldraw,
 </span>
 <span data-rw-start="1168.64" data-rw-transcript-version="2">
 we are on Twitter X at tldraw, and then
 </span>
 <span data-rw-start="1171.48" data-rw-transcript-version="2">
 I'm at Steve Ruiz okay. I post a lot
 </span>
 <span data-rw-start="1173.88" data-rw-transcript-version="2">
 about this stuff. So,
 </span>
 <span data-rw-start="1175.44" data-rw-transcript-version="2">
 uh thank you for coming.
 </span>
</p>
<p>
 <span data-rw-start="1177.159" data-rw-transcript-version="2">
 Cheers.
 </span>
</p>