---
categories:
  - "[[Resources]]"
domain: engineering
title: "What’s Your Current / Best AI Voice Agents Stack?"
source: "https://www.reddit.com/r/AI_Agents/comments/1lo8bf0/whats_your_current_best_ai_voice_agents_stack/?share_id=zatHDhvLsl4P0YLgq_L3i&utm_content=2&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1"
author: "Extension_Platypus15"
published: 2025-06-30
created: 2026-04-04
description: "My restaurant table reservation bot keeps telling people we're \"fully booked"
tags:
  - to-process
  - agent-tools
---

**[r/AI\_Agents](https://www.reddit.com/r/AI_Agents/)**


# [Extension\_Platypus15](https://www.reddit.com/user/Extension_Platypus15/)



 (2025-06-30 14:01:53)


Been building voice agents for a few weeks now. Started with a restaurant bot, thinking of expanding to hotels and real estate (majorly front desk)


Currently using Vapi but it hallucinates so much for some reason (exact problems down below)


**Quick questions:**


* What stack are you using?
* Rough monthly costs?
* Different tools for different industries or one-size-fits-all?


My restaurant table reservation bot keeps telling people we're "fully booked" when we're not and when people order takeaway — it keeps repeating the menu every time user asks for options. Happy to attach prompt if helpful.


Any "wish I knew earlier" tips appreciated 🙏





## [Asleep-Fault-5582](https://www.reddit.com/user/Asleep-Fault-5582/)



 (2025-08-23 22:43:08)


Vapi and Retell is good for building agents. If you prefer more flexibility, build your orchestration over open source frameworks like livekit or pipecact. For end to end testing and observability, use Cekura





### [butterchicken\_27](https://www.reddit.com/user/butterchicken_27/)



 (2025-11-21 12:34:00)


I’ve tried LiveKit, Vapi, Retell, and other agent builders platforms, and they all work until you put them in the real world.I've tried them at airports, background music, people talking nearby… they get triggered nonstop.


Agora Conversational AI Engine has been the only one that doesn't crap out when it's in the real world tbh. The VAD / voice lock stuff actually filters out the random noise, so the bot only reacts when it’s supposed to. The flow feels way smoother than anything else I’ve tested. Even in beta it’s been the best QoE by far. And somehow cheaper lol..





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-07-03 11:56:45)


[removed]





### [IndependentCollar838](https://www.reddit.com/user/IndependentCollar838/)



 (2025-09-16 05:04:46)


Hey thanks a lot for sharing this, would you be opposed to letting me pick your brain a bit on this?





## [Middle-Study-9491](https://www.reddit.com/user/Middle-Study-9491/)



 (2025-07-14 09:52:20)


Your Vapi hallucination issue is not a Vapi issue but an LLM/Prompt issue. Your agent has clearly not been instructed well enough and thats why these issues are happening (I would be happy to take a quick look at what you've done so far and give you some help).


I run a YouTube channel ([Hugo Podw](https://www.youtube.com/@HugoPodw)) focused on Voice AI and founded Artilo AI - we're an AI development studio that creates bespoke voice AI solutions.


To answer your question:  

1. At Artilo AI our stack is currently Vapi with a custom LLM, this gives us full customisability of the LLM logic, handling context etc... whilst also allowing us to use the prebuilt platform  

2. This just depends on the client that we are building for, if we build a solution for a large company doing say 10,000 calls a month at an average 5min call time this would come out to roughly $6,000 (10,000 x 5 x $0.12). Usually we are looking at around $0.8 - $0.12 per min cost  

3. Yes different tools but not for different industries but more to do with different size of company. If we work with a large sized business we use different platforms like Livekit/Pipecat for full customisation and control whereas for medium to small sized business we will use Vapi + Custom LLM like I mentioned (we do also use this stack for large sized businesses too)


Dm me on Reddit or find me on Linkedin (don't want to self promo but I'm sure you can find me based on my channel) and I will do my best to help you out.





## [baghdadi1005](https://www.reddit.com/user/baghdadi1005/)



 (2025-06-30 14:41:13)


Its going to be a fun ride, Vapi is a great start, test for all the flows by manually calling your agent, setup proper tool calling and test each time (maybe use airtable or any other general CRM) you will definitely face issues with CRM and POS integration that restaurants use so stay aware of that (there is no direct solution but to partner with crm software to route to you too what they route to its POS). I advice to not go in hotel booking as youd most definitely wont cut it with competitors like sevenrooms unless you work with an real estate agent.





### [Swimming\_Heat7049](https://www.reddit.com/user/Swimming_Heat7049/)



 (2025-07-01 12:30:17)


manually calling each time?





#### [baghdadi1005](https://www.reddit.com/user/baghdadi1005/)



 (2025-07-01 12:35:23)


Yeah that works the best initially, you can try using testing automation tools like Hamming AI later on





## [burcapaul](https://www.reddit.com/user/burcapaul/)



 (2025-06-30 14:16:12)


Vapi’s hallucinations sound frustrating but not unheard of. I ended up mixing a few tools—use a solid NLU like Rasa or Dialogflow for intent handling, then an AI layer for chit-chat. 


For industries, one-size usually gets messy fast, especially with booking or menu details. Tailored prompts or logic per sector really help. 


If you want less tweak and more plug-n-play, Assista AI’s got a neat setup for multi-agent workflows that might save you some headache. Costs can vary a ton though depending on scale. 


Would love to see your prompt, btw. Sometimes the devil’s in those details.





## [iwanttopartynow](https://www.reddit.com/user/iwanttopartynow/)



 (2025-07-29 18:53:32)


didnt need a stack, i just bought a ready to go, plug and play voice AI. miss me with that shit fr im way too lazy to experiment with tech stacks





### [Proper\_Ad\_88](https://www.reddit.com/user/Proper_Ad_88/)



 (2025-10-18 12:09:40)


Which one?





## [AutoModerator](https://www.reddit.com/user/AutoModerator/)



 (2025-06-30 14:01:53)


Thank you for your submission, for any questions regarding AI, please check out our wiki at <https://www.reddit.com/r/ai_agents/wiki> (this is currently in test and we are actively adding to the wiki)


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](https://reddit.com/message/compose/?to=/r/AI_Agents) if you have any questions or concerns.*





## [Sajedaquraan1](https://www.reddit.com/user/Sajedaquraan1/)



 (2025-06-30 18:54:08)


Hey! I’ve been working on voice agents as well and totally relate to what you’re facing — especially the hallucination issues and repeated responses.


I switched to using VoiceHub, a no-code platform that’s been really solid for me. One of the things I like most is how it lets you visually build logic with something called Conversational Pathways. That helped me eliminate a lot of the confusion like false “fully booked” replies.


I also used webhooks in VoiceHub to connect real-time data (like live menu or availability), which fixed most of the issues I had with earlier tools.


It works well across industries — I’ve tested it for restaurants, service bookings, and even support flows. Plus, the pricing plans are clearly explained and flexible, so it’s easy to pick what fits your needs without any surprises.


And it doesn’t require complex setup or coding, which made it easy to iterate fast.


If you’re exploring other stacks, definitely worth a try. I can send you the documentation or answer any questions if you’re curious.





### [Whole\_Gur\_3426](https://www.reddit.com/user/Whole_Gur_3426/)



 (2025-07-01 04:56:01)


I'll appreciate a documentation.





### [etherrich](https://www.reddit.com/user/etherrich/)



 (2025-07-01 07:53:51)


do you gave a link to their page?





## [AdmiralUrbi](https://www.reddit.com/user/AdmiralUrbi/)



 (2025-07-01 02:47:03)


Vapi for basic infrastructure. I tried Bland but felt that Vapi had better documentation. I've also been following Vapi's progress on LinkedIn and they seem more driven to build a good platform.


ElevenLabs is my go-to for synthetic voice. I've used it extensively to automate inbound calls at an accounting firm. Even in Spanish, the voices sound good enough that most people either do not mind or cannot tell that they are talking to AI.


Praxos for memory. Depending on the complexity of the call you will need to add a memory module so that the agent does not hallucinate call information. Going through call transcripts and noticing that the AI starts making stuff up or gets hung up trying to recall facts is embarassing and has left a lasting bad impression in some of my clients. I've tried Praxos and Mem0 for memory, with Praxos having much better performance but being more limited since it's newer.





## [Omarashraf2823](https://www.reddit.com/user/Omarashraf2823/)



 (2025-07-01 12:18:20)


I’ve been building Arabic voice agents using VoiceHub, mostly for service businesses like logistics and appointment-based sectors. What helped us avoid hallucinations was keeping prompts short, and splitting logic across multiple smaller agents (VoiceHub’s builder makes this easy). For pricing, we optimized costs by switching between Meta and ElevenLabs based on latency per region. One tip: define fallback phrases and redirect edge cases early in the prompt, especially for repetitive flows like menus or availability.





### [Middle-Study-9491](https://www.reddit.com/user/Middle-Study-9491/)



 (2025-07-14 09:57:27)


How are Arabic voice agents going for you? Do you find the STT and TTS are good enough? i.e. Does it sound good/realistic





#### [Electrical-Cap7836](https://www.reddit.com/user/Electrical-Cap7836/)



 (2025-07-22 12:11:19)


I’ve been using DataQueue’s Voicehub, and it handles Arabic dialects pretty well. It supports Gulf, Levantine, and Egyptian dialects, and both the STT and TTS are quite solid sounding good and accurate in most cases.





## [Whole\_Gur\_3426](https://www.reddit.com/user/Whole_Gur_3426/)



 (2025-07-02 12:59:39)


Thank you,I really appreciate.





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-07-05 08:54:01)


[removed]





### [Big\_News\_3769](https://www.reddit.com/user/Big_News_3769/)



 (2025-07-11 22:52:14)


are you connecting elevenlabs to a n8n workflow that uses ai agent connected to openai model? is that what you mean or you just use the openai model in elevenlabs





## [IslamGamalig](https://www.reddit.com/user/IslamGamalig/)



 (2025-07-06 12:44:15)


Interesting thread! I’ve been testing out VoiceHub lately for some restaurant and booking flows too. Still tweaking prompts to cut down on repeat answers, but it’s promising so far. Curious to see what stacks others are running too.





## [Interesting\_Run\_5757](https://www.reddit.com/user/Interesting_Run_5757/)



 (2025-07-09 12:59:44)


Right now, I’m using calhippo AI voice agent, and it’s been working well for me. It takes care of inbound and outbound calls, responds naturally, and even qualifies leads or transfers calls when needed. I’ve paired it with hubspot for CRM and zapier for automations so everything syncs smoothly. It’s a solid setup if you’re looking to streamline voice communication without losing the human touch.





## [UpperYogurtcloset636](https://www.reddit.com/user/UpperYogurtcloset636/)



 (2025-07-28 14:36:12)


Been using CloudTalk lately, mostly for routing, bookings, and basic lead intake. It’s been reliable so far, and the setup didn’t take much time.


It runs around $0.25/min, which feels fair unless you’re doing crazy volume. 


I haven’t built anything for restaurants specifically, but maybe worth tweaking the prompt to clarify when it should respond with availability, or to add a condition like “only list the menu once unless the user asks for something specific.”





## [Funny\_Working\_7490](https://www.reddit.com/user/Funny_Working_7490/)



 (2025-08-23 09:50:07)


Has anyone hosted a livekit pipeline?





### [maltmaker](https://www.reddit.com/user/maltmaker/)



 (2025-10-06 01:43:24)


most of the resel[lers (vapi, bland etc.) use livekit under the hood, I'm looking at best reseller to use short term to validate market, then plan on either hiring out or building out the livekit setup. I've built a voice cloning convo app with livekit but haven't used SIP trunking and my day job takes up too much time. if you want to collab on a project i'd be interested if you've played around in livekit.





## [Jeff-in-Bournemouth](https://www.reddit.com/user/Jeff-in-Bournemouth/)



 (2025-08-29 08:37:47)


I was searching for an AI voice agent that captured 100% accurate details from website visitors, but couldn't find one.


So I built this open source website voice agent which uses a human in the loop details verification step to ensure 100% accuracy: <https://github.com/jeffo777/input-right>


There is a two minute demo video on the Github page which clearly shows how it works.


**Edit: NEW: Join the cloud platform waitlist (Free access for first beta testers):** [**https://inputright.com/**](https://inputright.com/)





## [ig\_hawkeye\_op](https://www.reddit.com/user/ig_hawkeye_op/)



 (2025-09-03 03:25:31)


Ran into the same thing with Vapi when I was testing a booking flow for a café bot it kept defaulting to “no availability” whenever it got confused. What helped was realizing that just tweaking prompts wasn’t enough. I started running automated test calls against the agent before pushing anything live, because manually calling it 20 times a day was driving me crazy.


For that I’ve been using Cekura. It basically simulates a bunch of different user personas (impatient caller, heavy accent, background noise, etc.) and flags when the bot goes off script or hallucinates. That’s how I caught the “fully booked” issue early. It’s not magic (still need to tighten prompts + API calls), but having those automated checks means I’m not relying on gut feel anymore.


So yeah, I’d say keep Vapi for routing/telephony if it’s working for you, but layer in some testing/monitoring so you know when it’s breaking before your customers do.





## [damaan2981](https://www.reddit.com/user/damaan2981/)



 (2025-09-18 15:28:26)


If you are a business with high call volume and looking for more complex but also reliable voice AI agent solutions, check out Leaping AI.





## [West-Championship853](https://www.reddit.com/user/West-Championship853/)



 (2025-09-19 13:19:02)


This is a great question, and it's a common challenge when building AI voice agents. The hallucination issue you're facing with Vapi is often related more to the underlying LLM and the prompt design rather than the platform itself.


The key to a good AI voice agent stack is often a combination of specialized tools for each part of the pipeline:


• **Speech-to-Text (STT)**: Tools like Deepgram or OpenAI's Whisper are top-notch for accurately transcribing speech.  

• **Large Language Model (LLM)**: This is where you'll do most of your prompt engineering to guide the conversation.  

• **Text-to-Speech (TTS)**: Platforms like ElevenLabs offer high-quality, natural-sounding voices.  

• **Orchestration and Logic**: This is where you connect everything. You might need to add layers for intent handling (e.g., Rasa, Dialogflow) and integrate with real-time data via webhooks to prevent the bot from fabricating information. For example, instead of the bot just "knowing" if a restaurant is booked, it should query a reservation system.


One solution that can help streamline this process is a platform that integrates these components seamlessly. You may want to [try VoiceSpin](https://www.voicespin.com/)' AI voice agent as a Vapi alternative.





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-09-25 18:12:38)


[removed]





### [Traditional\_Stay9874](https://www.reddit.com/user/Traditional_Stay9874/)



 (2025-09-25 20:48:07)


We trusted them because they are backed by google. [LINKEDIN POST LINK](https://www.linkedin.com/feed/update/urn:li:activity:7364015873415671809?commentUrn=urn%3Ali%3Acomment%3A%28activity%3A7364015873415671809%2C7364654949021933568%29&dashCommentUrn=urn%3Ali%3Afsd_comment%3A%287364654949021933568%2Curn%3Ali%3Aactivity%3A7364015873415671809%29)


![](https://preview.redd.it/0gfkztm0idrf1.png?width=702&format=png&auto=webp&s=c6dad968923a1a8b1d554d59f73c169575e81079)





## [washyerhands](https://www.reddit.com/user/washyerhands/)



 (2025-09-29 09:12:25)


"Ran into the same thing with Vapi when I was testing a booking flow for a café bot it kept defaulting to “no availability” whenever it got confused. What helped was realizing that just tweaking prompts wasn’t enough. I started running automated test calls against the agent before pushing anything live, because manually calling it 20 times a day was driving me crazy.


For that I’ve been using Cekura. It basically simulates a bunch of different user personas (impatient caller, heavy accent, background noise, etc.) and flags when the bot goes off script or hallucinates. That’s how I caught the “fully booked” issue early. It’s not magic (still need to tighten prompts + API calls), but having those automated checks means I’m not relying on gut feel anymore.


So yeah, I’d say keep Vapi for routing/telephony if it’s working for you, but layer in some testing/monitoring so you know when it’s breaking before your customers do."





## [fluentsai](https://www.reddit.com/user/fluentsai/)



 (2025-10-14 15:39:28)


For your stack questions - we've found that having multiple LLM/voice providers helps a ton with hallucination issues. We use a mix of OpenAI, ElevenLabs, and sometimes Deepgram depending on the use case. It varies based on call volume and client budget.


One big "wish I knew earlier" tip: create separate prompt blocks for different conversation paths. For your restaurant bot, have a dedicated reservation flow that checks availability directly from your system before responding (not letting the LLM guess). Same with takeaway - create a menu section that doesn't repeat unless explicitly asked.


For the different industries question - we started with one template but quickly realized each vertical needs tweaking. Restaurant bots need menu knowledge and reservation logic, hotel needs check-in/out flows, real estate needs property details structured differently. About 70% can be shared though.


Would love to see your prompt if you're willing to share! The hallucination issues might be fixable with some structural changes to how you're querying availability data.





## [IllustriousCard5627](https://www.reddit.com/user/IllustriousCard5627/)



 (2025-10-14 17:37:18)


Most of the time I see an agent "hallucinating", its because the API or integration its calling is failing or outputting data in a format that the agent isn't expecting. Are you using a custom function on Vapi? Plugging into some restaurant API like OpenTable? I'm guessing that would be the issue.


Before even building your agent, I'd focus on your API layer first and make sure that is rock solid. If there are errors, those should be handled gracefully or else you might see unexpected responses. If your set on building the API layer yourself, use AWS Lambda or something and have AI help you write something that wraps whatever your data source is. 


On cost, your cost is going to entirely depend a lot on volume. Most platforms charge per minute pricing.


Full disclosure, I'm the founder of a voice AI startup called Pod AI (callpod.ai). We see this kind of thing all the time. We try to be different by doing a lot of hand-holding with customers; most of the time we even help/advise them on how to build their API / data layer. Lmk if I can be more helpful.





## [Sandraen\_joyablev1](https://www.reddit.com/user/Sandraen_joyablev1/)



 (2025-10-26 17:32:12)


The hallucination issue is a prompting issue unfortunately and not a provider issue. This will not resolve unless you improve the prompt.


I currently run a white label voice agent solution and have over 50 agents in production right now. My recommendations for the stack is using voice.ai on the agent side. I've tried almost every other provider and find that either their latency or their cost is prohibitive. I think voice ai has the best latency and pricing by far. 


For context, my average cost per minute with them is $0.04 including LLM costs. We used to use 11 but found that their pricing was absurd and they didn't listen to any feedback. Further - their latency is horrible. I think we were averaging over 2s per turn which is ridiculous.





## [Danielle\_fetching](https://www.reddit.com/user/Danielle_fetching/)



 (2025-10-26 20:49:12)


"I have over 50 agents in production for companies ranging from small to very large enterprises. I have tried essentially every provider and my feedback is to avoid the wrapper companies. They cannot control the infrastructure, pricing, or controls because they don't own any piece of the stack. 


My recommendation on companies is to either use (idk if i can post links) when u write voice(dot)ai or 11. I prefer voice ai because their pricing is much more competitive, latency is better, and the voice cloning seems to be more accurate. For context, I had agents with 11 before and I measured over 2s of time between each turn which is attrocious. For voice ai, the time is in the ms not seconds..





## [Happy-Fruit-8628](https://www.reddit.com/user/Happy-Fruit-8628/)



 (2025-10-29 18:42:20)


We have been building similar bots recently and ran into the same looping and hallucination issues on Vapi, especially when handling dynamic data like availability or menus. Switched over to AgentVoice for production use since it lets you handle logic directly via Zapier or webhooks, and the response latency is noticeably lower.





## [Adventurous-Chip-754](https://www.reddit.com/user/Adventurous-Chip-754/)



 (2025-11-18 11:41:41)


In my opinion, readymade providers already bundle technical stack ASR, TTS, LLM, SIP and they are more reliable than building the stack on your own. One-size-fits-all providers include **MirrorFly, Apphitect, VoiceSpin** and **Retell**. So you don't want to go for different tools for different industries, these providers have **industry-specific templates**. 


You can just spend time designing your customer experience, no headache for fixing audio pipelines. For a voice agent, the pricing is usually based on per user per day, and most of them have custom pricing options which may not be available publicly. 





## [kcrconsultant97](https://www.reddit.com/user/kcrconsultant97/)



 (2025-12-05 12:41:53)


I’ve tested a few stacks over the last couple of months and what worked best for me are MirrorFly and Sendbird. I use a mix of stacks depending on the use case, LLM + STT or TTS, and a communication layer.  


For projects where I need stable calling infrastructure and low latency, I use providers like MirrorFly or Sendbird for the RTC layer. It gives more control over workflows and no hallucination issues I faced. 


Monthly costs depend on call minutes, and they differ for each voice agent provider. And lastly, in my opinion, one size fits all industries is a good option.