---
categories:
  - "[[Resources]]"
domain: engineering
title: "How are push notifications created and handled in PWAs?"
source: "https://www.reddit.com/r/PWA/comments/1jmluey/how_are_push_notifications_created_and_handled_in/?share_id=G7L27QHDOr8WQvN6-_bF6&utm_content=2&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1"
author: "whitesydney2005"
published: 2025-03-29
created: 2026-04-03
description: "When you ask the browser for a push notification subscription, they provide"
tags:
  - to-process
  - design-automation
---

**[r/PWA](https://www.reddit.com/r/PWA/)**


# [whitesydney2005](https://www.reddit.com/user/whitesydney2005/)



 (2025-03-29 13:04:53)


I need to make a decision about whether to develop my news app in ReactNative or as PWA.


One feature that is very important to me is Push Notification as it is a news app and it should be very reliable especially in the case of breaking news etc. 


Some questions,


1. How is it done? Do I have to use a third-party solution or it is available natively?
2. Does it cost to send out push notification? We are a news app with thousands of users so the volume will be quite large.
3. Are PWA notifications different in look and behavior when compared to RN or native built apps?


I would be very grateful if you folks could please help me with these questions.





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-03-29 13:12:16)


[removed]





### [whitesydney2005](https://www.reddit.com/user/whitesydney2005/)



 (2025-03-29 13:22:55)


Thank you, very helpful.


Some follow-up questions,


1. Seems messy. Is there a way or service that unifies the sending process?
2. I would think in my case it would 2-3 notification per day.
3. My question wasn't clear. I meant is a difference in the way they looks when compared to native apps. Will the end-user see a difference?





#### [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-03-29 13:36:58)


[removed]





##### [whitesydney2005](https://www.reddit.com/user/whitesydney2005/)



 (2025-03-29 13:40:35)


Thank you once again.


Question #2, I meant 2-3 notifications per user. And we have around 2500+ singups in the database.


Regarding #1, is this all done manually?





###### [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-03-29 17:10:01)


[removed]





###### [whitesydney2005](https://www.reddit.com/user/whitesydney2005/)



 (2025-03-31 15:25:55)



> 
> I can send you our process how its done, but monday at best.
> 
> 
> 


Could you please DM? It would be of great help to me.


Thank you again!





#### [Rican7](https://www.reddit.com/user/Rican7/)



 (2025-03-29 16:05:36)


When you ask the browser for a push notification subscription, they provide you an endpoint URL and some details that you'll use to send the push notification from your backend. So you store those in your backend and then use them in a standard fashion to send the notification, so the different endpoints actually don't really matter. They're opaque.





#### [Ecstatic\_Builder8325](https://www.reddit.com/user/Ecstatic_Builder8325/)



 (2025-08-04 14:00:57)


There's a service called OneSignal. You can use that to unify the sending process. :D





## [Connexense](https://www.reddit.com/user/Connexense/)



 (2025-03-29 17:14:31)


Push notifications in a website or pwa rely on the browser being able to run a service worker in the background even while the browser (or pwa) is closed. The problem currently is that this is unreliable. Browsers close down that background service after some period of time (it differs in different browsers) such that notifications are not received until the site/pwa is opened again. PWAs installed by Chrome perform best in this respect. If it is important that your newsy notifications are received in timely fashion, native apps would serve you better because their push notification capabilities are much more reliable.





### [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-03-29 18:23:37)


This is absolutely NOT true. The process that takes care of receiving push notifications is a daemon on the OS level that activates the service worker when needed. It doesn’t matter if a PWA hasn’t been running for a period of time, the push notifications will still be delivered.





#### [Traditional-Night-25](https://www.reddit.com/user/Traditional-Night-25/)



 (2025-03-30 04:11:56)


True that. I recently setup pwa notifications on my iOS device, and no matter what if i opened that pwa or not , i always receive the notifications.





##### [nefynhop](https://www.reddit.com/user/nefynhop/)



 (2025-06-06 16:45:43)


Are the push notifications via email or text? Or do PWA’s now allow banner, sounds, and badge notifications?





###### [Traditional-Night-25](https://www.reddit.com/user/Traditional-Night-25/)



 (2025-06-06 16:49:31)


I only did mobile push notifications... for android it is instantaneous and for ios it gave some trouble for me... anways.. i got an internship and left behind this pwa





###### [karb10](https://www.reddit.com/user/karb10/)



 (2025-10-29 18:56:52)


does ios chrome and safari push notification need any payment?





###### [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-10-30 11:43:55)


No, push notifications are always free on any platform.





###### [karb10](https://www.reddit.com/user/karb10/)



 (2025-10-30 14:54:56)


Can iOS Safari receive WebPush + VAPID notifications without using APNs?


We implemented WebPush (v1.0.12 NuGet package) with VAPID, and it works fine on Android and Windows browsers, but not on iOS Safari. If APNs is required, are there any free alternatives for sending push notifications to iOS browsers (without using APNs or a paid service)?





###### [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-10-30 16:11:59)


Yes, I'm not familiar with APNs and I just use VAPID to send the notifications (<https://github.com/web-push-libs/web-push>)


I have a demo here that works on iOS: <https://whatpwacando.today/notifications>





### [Connexense](https://www.reddit.com/user/Connexense/)



 (2025-04-01 01:04:37)


As I said: it differs in different browsers. To get the facts about how deliverable push notifications really are, the most thorough approach would be to try all OS's/devices and all browsers, with and without installing the PWA, and send notifications to them while their respective windows are closed. Unfortunately, you'll get conflicting and frequently incomplete or incorrect information here.





#### [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-04-01 10:31:41)


I did test all this and with all due respect, you are the one providing incorrect information in your previous post.





##### [Connexense](https://www.reddit.com/user/Connexense/)



 (2025-04-06 17:10:00)


Here's an example of what I mean: installed Edge on my Android, then installed my pwa and subscribed for notifications. Permission dialog appeared, and I enabled notifications. Tested twice by sending notifs from my desktop browser, both successfully sent but not received. Although the endpoint was properly established (checked on my server, it's an fcm endpoint, not windows) I still had to go into phone settings to enable notifications for the PWA. Sent another notif from my desktop browser, received this time. The badge appears on the Edge icon, not the pwa icon. Tapping the Edge icon with the badge just opens the Edge browser, not at my url as intended. Pull down from top to get the notification there, click that and the pwa opens and behaves exactly as programmed.


None of this mess occurs when the pwa is installed on Android using Chrome - it just works! This is why I said that Chrome works best and that native app notifications are much more reliable.





###### [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-04-06 18:23:48)


Thanks for the clarification. Yes I agree that a PWA installed through Chrome works much better but you claim that push notifications are no longer displayed after a while. This is something I never experienced before.





###### [Connexense](https://www.reddit.com/user/Connexense/)



 (2025-04-06 19:18:53)


Oh, that would be in Edge too, although I haven't tested that issue for a long time. I remember reading somewhere that browsers shut down the service worker after "some time" and was able to confirm that in my pwas. It certainly was the case in Chrome too 3 -4 years ago - perhaps the daemon you spoke of which starts the service worker when needed is a new gizmo that I'm not aware of? Agreed, Chrome on Android now seems to do better now. I'm testing it now - will not send a notification to it nor open the browser or the pwa until tomorrow ...


I'm excited about the latest advances in Ios and iPadIos - just don't want to spend a silly amount of money to buy a new one :(





###### [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-04-06 19:33:37)


Great, I will do some thorough testing as well to see what the current status is.





###### [Connexense](https://www.reddit.com/user/Connexense/)



 (2025-04-07 15:35:48)


So after 10 hours with Chrome and the pwa closed and phone sleeping, I sent a notification which was silently received and only seen and heard when I opened the pwa after unlocking the device.





###### [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-04-08 19:51:21)


Interesting. Thanks for reporting, I will test again as well.





## [dannymoerkerke](https://www.reddit.com/user/dannymoerkerke/)



 (2025-03-29 18:25:31)


In addition to earlier replies, on iOS the options for defining different actions (buttons) that can be shown in a notification are limited compared to Android.





## [[deleted]](https://www.reddit.com/user/[deleted]/)



 (2025-03-31 20:12:50)


I am working on the same, I tested to push a notification using js code while app is running successfully and I came to the following conclusion, you need to grant notification permission as a website using js since you are a website, but the most important is to grant it as an app, which I came to know that most probably you need to enable it manually,





## [Scarred-Tissues](https://www.reddit.com/user/Scarred-Tissues/)



 (2025-04-01 10:42:05)


Does anyone have an issue of impressions falling sharply over time with a PWA? This is even after receiving a 201 status from the push service.





### [nguha\_am](https://www.reddit.com/user/nguha_am/)



 (2025-04-01 12:05:44)


Couple of questions here:


1. What service are you using?
2. Was there an existing service worker file for your PWA before you tried integrating push notifications?


PWAs don't usually need a service worker. But sometimes, we see PWAs with a pre-existing service worker that conflicts with the integration code.


Essentially, what happens in that case is that your service stops collecting push subscribers even though everything seems fine on the surface.





#### [Scarred-Tissues](https://www.reddit.com/user/Scarred-Tissues/)



 (2025-04-01 13:01:11)


1.I'm using the web-push (npm) package which handles the calls to the browser push service. 


1. only the current service worker. We created the PWA with Push functionality from the outset.


The use is for e-commerce stores to send push notifications. Some stores have other service workers but it's generally not the case





##### [nguha\_am](https://www.reddit.com/user/nguha_am/)



 (2025-07-02 11:24:13)


Hmm... How many notifications do you send a user in a week on average? Sometimes, Firebase will throttle the delivery rates if you send too many notifications. Are you using subscriber segments for your notifications? Or is it all broadcast?





## [nguha\_am](https://www.reddit.com/user/nguha_am/)



 (2025-04-01 11:45:52)


You should check out PushEngage. They have a detailed guide on how to integrate PWA push notifications: <https://www.pushengage.com/pwa-push-notifications/>


Not just that, they have a full-fledged marketing layer on top. So, there's really no coding involved. You can send automated, personalized push notifications from a simple, easy to use dashboard.


The underlying technology is FCM (Google) and APNS (Apple). But PushEngage allows you to send notifications without having to worry about the technical details of integration. It's really just a simple copy and paste for PWAs.


Since you're running a news agency, a major feature you'd be interested in is their segmentation options. It allows you to send specific notifications to particular audience segments. For example, only people who have susbcribed for Tech News will get tech news updates. This helps you stay relevant and urgent.


You can also **automate the entire process** using your RSS feed. It's all a few clicks. They also have a list of campaign ideas by industry you can check out:


<https://www.pushengage.com/push-notification-examples/>





### [nefynhop](https://www.reddit.com/user/nefynhop/)



 (2025-06-07 16:44:20)


Do the notifications include banners, sounds, and badges?





#### [nguha\_am](https://www.reddit.com/user/nguha_am/)



 (2025-07-02 11:21:06)


Banners and badges, yes. Sounds, no. I'm not 100% sure of this, but I think you can only add custom alert sounds to mobile app push notifications. If you also have a mobile app, then yeah. You can do that too. :)





##### [nefynhop](https://www.reddit.com/user/nefynhop/)



 (2025-07-02 13:08:14)


Awesome. So how do you add that capability to the PWA?





###### [nguha\_am](https://www.reddit.com/user/nguha_am/)



 (2025-07-02 14:34:08)


Well, if you're using PushEngage, it's really easy. You get a full-fledged interface where adding large images, small images, CTA buttons, and multiple links is dead simple. If you're not using PushEngage, I highly recommend shifting to PushEngage. I think the support team helps you with free migrations as well.





## [ElectricalLong6657](https://www.reddit.com/user/ElectricalLong6657/)



 (2025-07-29 12:24:57)


LaraPush is a simple way to add push notifications to PWAs.





## [kevbrown044](https://www.reddit.com/user/kevbrown044/)



 (2025-08-28 06:46:22)


We have a clever work around for this that is used by our clients at FanCircles. 
We’re just about to launch as a separate service that will work by a simple API call to join a user and a further API to push a notification to both IOS and Android. 
You can check it out here <https://www.fancircles.com/mobile-push-notifications/>





## [Gravath](https://www.reddit.com/user/Gravath/)



 (2025-03-29 13:28:28)


Ignore me I was wrong.





### [eawardie](https://www.reddit.com/user/eawardie/)



 (2025-03-29 15:44:56)


This is incorrect. Safari handles push notifications fine.





#### [Gravath](https://www.reddit.com/user/Gravath/)



 (2025-03-29 16:32:56)


I retract my statement then





### [whitesydney2005](https://www.reddit.com/user/whitesydney2005/)



 (2025-03-29 14:37:05)


Why not?


I googled before answering and it seems there are ways to get it done.





### [Rican7](https://www.reddit.com/user/Rican7/)



 (2025-03-29 16:02:54)


Push Notifications have been available to iOS apps that are installed as PWAs (Added to Homescreen) since 16.4.