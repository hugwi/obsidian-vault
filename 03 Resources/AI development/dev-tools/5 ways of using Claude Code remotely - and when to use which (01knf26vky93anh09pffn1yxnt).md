---
title: "5 ways of using Claude Code remotely - and when to use which"
source: "https://www.youtube.com/watch?v=eLaf8rCSwIM"
author: "Academind"
published: 2026-03-31
created: 2026-04-05
description: "Claude Code offers multiple ways of using it remotely ... remote control,"
tags:
  - to-process
  - dev-tools
---

When working with Claude Code, there
are at least four official ways of using it remotely without you
sitting on your machine. And there is a fifth secret way which I'll also show you. Now, the four official ways that
are supported is by using the Claude Code cloud,
by using a feature called remote control,
by using a feature called dispatch, and by using a feature called 

channels. And the question obviously
is why do we have all these different approaches
and why do we need them and which approach?
And that's exactly what I'll show you, cloud. Now,
this is maybe the one that's easiest to understand even without this video. The idea is that you don't use Claude Code
on your machine, but instead, guess what? In the cloud,
on servers owned and managed by Anthropic. So you send a 

task to the cloud,
which you can do from the Claude Code CLI, but also from their web interface or their mobile app,
and this task then gets executed in the cloud on those
servers. For that to work,
you need to have your code on a GitHub repository, and you need to connect
that to your Claude Code account,
your Anthropic account. Give them access to it, of course, so
that this code can be downloaded onto the server where the task
is being executed, and there 

are various limitations here, of course. One limitation, obviously, is
that anything that is on your system, any global skills, any CLI tools you may rely on in your
application or in your build scripts or workflows, all that
is not available there on those cloud servers
because it isn't your machine. The advantage, of course, is
that you can truly execute tasks there without your
machine 

even being turned on because, well,
it's not happening on your machine. So
if you wanna run some task overnight or if you wanna run multiple tasks in parallel but can't
or don't want to use your machine for that, if you're traveling
or if you have an unstable internet connection or anything like that,
using the cloud may be an interesting alternative to using
Cloud Code on your machine. By the way,
if you wanna learn more about Cloud Code, 

I'm showing you here
and you wanna dive a bit deeper the most out of Cloud Code,
I do have a complete Cloud Code course which may be interesting to you. And right now,
we still have our spring sale going on the Academy Pro annual membership for a
much lower price than you normally would get it, 169 instead of 249,
and this membership gives you access to all the courses we have,
as long as you have an active membership, including the Cloud Code course
and any future courses we may release, 

in addition to the extensive course
catalog we already have. Links below this video. Now, all remaining approaches here, on the other hand,
are about executing Cloud Code on your machine,
not on Anthropic's server. So the cloud solution really
is kind of a special solution, also be used in conjunction to those other
approaches because, of course, nobody's stopping you from executing some
tasks in the cloud whilst also working on other
features in the same 

project on your machine.
You just have to merge the different changes thereafter.
So let's start with remote control then. Remote control is mostly about continuing some task or some work
that you maybe started on your system, still on your machine whilst you
are leaving your machine. So let's say you're going for lunch
or you have to go to a meeting, but your computer, your,
your Mac, your PC stays 

turned on and you want to continue working
on a task Now, obviously,
Cloud Code will continue you're leaving the machine,
as long as your machine doesn't go to But once it's done, it won't continue. Now, with remote control,
you can make it continue and you can also start a new task,
but your machine needs to be turned on. And not just that, instead,
you need to start Cloud Code,
the CLI in a special mode, in the 

remote control mode, or in an interactive session,
you need to turn on remote control mode by using the respective slash command. Once the remote control mode is turned on,
you can connect your mobile phone with the Cloud mobile
app, you need that,
to your machine by scanning a QR code, for example,
which you can have Cloud Code show you. And then once that connection
is established, you can use a chat session.
You can send messages to Cloud Code in 

your mobile app,
but those chat messages are then not sent to the cloud or somewhere else,
but instead to your connected machine through remote control.
So remote control can be very useful, but it has a couple of potential
disadvantages. The two most important ones,
in my opinion, being to keep your machine turned on, and
if it goes to sleep, you lose the connection,
so you must ensure it doesn't. And you must start your Cloud Code session
in 

that remote control mode.
If you forget this, there is no way for you to send messages to it.
So you must set it up first and then you can use
itThat is where Dispatch comes into play.
With Dispatch, you still need to ensure that your machine doesn't go to
sleep, though it gets a bit easier as you'll see,
but you don't need to start Claude Code in any special remote control
mode first in 

order to use it. For Dispatch,
you need the Claude desktop app,
though you need to download and once you did that,
you also need to go through a one-time setup process to enable Dispatch. In that Claude desktop app,
you can also turn on a setting that prevents your machine from
going to sleep whilst the app is up and running, though, so
that eliminates this my machine went to sleep and now my session broke or
was canceled 

problem. Now, with Dispatch then set up,
you can use the Claude mobile app again, and there,
the Dispatch feature to send messages to And the big difference now is
that you don't need to start a Claude Code session through the CLI first
or anything like that. Instead,
you just need to have the desktop app up and that is it. Now,
you can send messages to Claude on your machine, and it goes ahead
and executes them. 

Now, what's important here, though,
is that Dispatch was originally a feature released for Claude
Cowork, which is their more general AI assistant,
not specifically focused on coding, and therefore,
at least right now when I'm recording this, your Dispatch messages are not connected to a specific project,
which, on the other hand, with Remote Control
was the case since you deliberately interactive session. With Dispatch,
you're just sending a message to 

Claude on your machine,
and it needs to figure out what to do with that message.
That message could be totally unrelated to if you want to invoke Claude Code to do
some work in one of your projects, well, then,
you will need to tell it in that Dispatch message where to find
that project,
give it some hints regarding the folder to So, that can be a bit inconvenient here,
but it is doable, of course, and then you can start
or continue sessions 

from anywhere through the mobile app with
that Dispatch feature. And then last, but not least,
we have Channels, and you would kind of see Channels as maybe the connection of Remote Control and Dispatch,
and also, Channels is essentially Anthropic's way of trying to merge Claude Code or their Claude offering
in 

general into an OpenClaw alternative, kind of. Many features OpenClaw has
are missing, but Channels is, in the end, a-
a way for you to connect any kind of messaging channel
to Claude Code. And by default,
Anthropic gives you an official Telegram channel connector you can set up, which makes it quite easy
and straightforward to use Telegram to communicate with your 

Claude Code session. You still need to go through a one-time setup process
and enable Channels,
and you also need to start a Claude session with the channel you wanna use
enabled, so you need to do that just as you had to do
it with Remote Control. But once you did that, you can use
that channel to send messages to Claude Code. So,
you're then no longer limited to just the mobile app. Instead,
you can use your channel, and of course, 

could start a Claude session
that you keep on running forever, essentially, with that channel connected,
and therefore, you can keep on pushing messages to Claude
Code there and work on a broad variety of tasks. And of course,
you could also start Claude Code not connected to
one specific project, but in general on your machine with Channels
enabled, and then kind of use it as an OpenClaw alternative by
asking it to do all kinds of things on your machine.
You could also do that with 

Remote Control, and with Dispatch,
as mentioned, it's the default, simply allows you to use any communication
channel of your choice. And of course, therefore,
on the other hand, and with the setup process you have to go
through with Remote Control, then you can just keep on using that,
and you don't need Channels It's also noting that this Channel's feature right
now when I'm recording this is in research preview, and therefore,
both the setup process and 

the- the feature set may, of course,
change over time. I also mentioned a- a fifth, uh,
secret way of remotely talking to Claude Code,
and this is actually simply a way that you could use with any
tool you have installed on your machine, not just with Claude Code. If you're running Claude Code on a machine
which you could access via SSH, so which is exposed to a network or the internet, then, of course,
you can 

connect to that machine via SSH.
And for example, you could have a VPS up and running,
which you maybe use for development work instead of your Mac or your PC, and
when that is exposed to a network, to, uh,
to the internet, uh, preferably, of course, secured with,
for example, a VPN solution like Tailscale, then you can connect to it via SSH.
And you cannot just do that from your Mac,
which doesn't really give you a huge 

You still have to be you on your machine
for that, but you could also use an app like Terminus on your mobile phone,
make sure that this is connected to this machine through a key
pair preferably, and then, of course, you can start a session there
and simply invoke any command on that machine because it's just
a SSH session, and that, of course, therefore,
includes Claude Code, and you can then start sessions from there. Now,
it's worth noting that depending on your operating system
and so on, when you close that app, the 

SSH session gets, uh, terminated,
and therefore, the Claude Code session, uh, will stop
But still, it is a way of quickly invoking certain
one-off tasks, and of course, you can use a solution like Tmux to kind of
decouple your connected session from the session on the machine
and keep those sessions going.
That is all something you could also look And that's, therefore, how you can use
and control Claude Code remotely on your machine or a 

VPS. And as mentioned,
if you wanna learn more, that offer I mentioned before 

<p>
 <span data-rw-start="0.3" data-rw-transcript-version="2">
 When working with Claude Code, there are at least four official
 </span>
 <span data-rw-start="4.2" data-rw-transcript-version="2">
 ways of using it remotely without you sitting
 </span>
 <span data-rw-start="8.34" data-rw-transcript-version="2">
 on your machine. And there is a fifth
 </span>
 <span data-rw-start="12.58" data-rw-transcript-version="2">
 secret way which I'll also show you.
 </span>
 <span data-rw-start="15.44" data-rw-transcript-version="2">
 Now, the four official ways that are supported are by
 </span>
 <span data-rw-start="19.26" data-rw-transcript-version="2">
 using the Claude Code cloud, by using a feature
 </span>
 <span data-rw-start="23.3" data-rw-transcript-version="2">
 called remote control, by using a feature called
 </span>
 <span data-rw-start="26.92" data-rw-transcript-version="2">
 dispatch, and by using a feature called
 </span>
 <span data-rw-start="30.4" data-rw-transcript-version="2">
 channels. The question, obviously, is why do we have all
 </span>
 <span data-rw-start="34.24" data-rw-transcript-version="2">
 these different approaches, and why do we need them? Which approach?
 </span>
</p>
<p>
 <span data-rw-start="41.96" data-rw-transcript-version="2">
 And that's exactly what I'll show you: cloud. Now,
 </span>
 <span data-rw-start="45.64" data-rw-transcript-version="2">
 this is maybe the one that's easiest to
 </span>
 <span data-rw-start="48.48" data-rw-transcript-version="2">
 understand even without this video.
 </span>
 <span data-rw-start="52.58" data-rw-transcript-version="2">
 The idea is that you don't use Claude Code
 </span>
 <span data-rw-start="56.58" data-rw-transcript-version="2">
 on your machine, but instead, guess what? In the cloud,
 </span>
 <span data-rw-start="60.32" data-rw-transcript-version="2">
 on servers owned and
 </span>
 <span data-rw-start="64.46" data-rw-transcript-version="2">
 managed by Anthropic. So, you send a
 </span>
 <span data-rw-start="67.84" data-rw-transcript-version="2">
 task to the cloud, which you can do from the Claude Code
 </span>
 <span data-rw-start="71.82" data-rw-transcript-version="2">
 CLI, but also from their web
 </span>
 <span data-rw-start="75.18" data-rw-transcript-version="2">
 interface or their mobile app, and this task
 </span>
 <span data-rw-start="88.86" data-rw-transcript-version="2">
 then gets executed in the cloud on those servers.
 </span>
</p>
<p>
 <span data-rw-start="78.9" data-rw-transcript-version="2">
 For that to work, you need to have your code on a GitHub
 </span>
 <span data-rw-start="82.76" data-rw-transcript-version="2">
 repository, and you need to connect
 </span>
 <span data-rw-start="84.98" data-rw-transcript-version="2">
 that to your
 </span>
 <span data-rw-start="88.86" data-rw-transcript-version="2">
 Claude Code account, your Anthropic account.
 </span>
</p>
<p>
 <span data-rw-start="92.6" data-rw-transcript-version="2">
 Are various limitations here, of course.
 </span>
 <span data-rw-start="95.66" data-rw-transcript-version="2">
 One limitation, obviously, is that anything that is on
 </span>
 <span data-rw-start="99.64" data-rw-transcript-version="2">
 your system, any global skills, any
 </span>
 <span data-rw-start="103.18" data-rw-transcript-version="2">
 CLI tools you may rely on in your application or in your
 </span>
 <span data-rw-start="107.08" data-rw-transcript-version="2">
 build scripts or workflows, all that is not
 </span>
 <span data-rw-start="110.74" data-rw-transcript-version="2">
 available there on those cloud servers because it isn’t your
 </span>
 <span data-rw-start="114.68" data-rw-transcript-version="2">
 machine. The advantage, of course, is that you can
 </span>
 <span data-rw-start="118" data-rw-transcript-version="2">
 truly execute tasks there without your machine
 </span>
 <span data-rw-start="122.12" data-rw-transcript-version="2">
 even being turned on because, well, it’s not
 </span>
 <span data-rw-start="126.08" data-rw-transcript-version="2">
 happening on your machine. So if you want to run some task
 </span>
 <span data-rw-start="129.74" data-rw-transcript-version="2">
 overnight or if you want to run multiple
 </span>
 <span data-rw-start="133.6" data-rw-transcript-version="2">
 tasks in parallel but can’t or don’t want to use your
 </span>
 <span data-rw-start="137.46" data-rw-transcript-version="2">
 machine for that, if you’re traveling or if you have an unstable
 </span>
 <span data-rw-start="141.28" data-rw-transcript-version="2">
 internet connection or anything like that, using the cloud may
 </span>
 <span data-rw-start="145.26" data-rw-transcript-version="2">
 be an interesting alternative to using Cloud Code on your machine.
 </span>
</p>
<p>
 <span data-rw-start="149.24" data-rw-transcript-version="2">
 By the way, if you want to learn more about Cloud Code,
 </span>
 <span data-rw-start="153.16" data-rw-transcript-version="2">
 I’m showing you here and you want to dive a bit deeper
 </span>
 <span data-rw-start="156.98" data-rw-transcript-version="2">
 the most out of Cloud Code, I do have a complete Cloud Code
 </span>
 <span data-rw-start="160.86" data-rw-transcript-version="2">
 course which may be interesting to you.
 </span>
</p>
<p>
 <span data-rw-start="162.68" data-rw-transcript-version="2">
 And right now, we still have our spring sale going on
 </span>
 <span data-rw-start="166.66" data-rw-transcript-version="2">
 the Academy Pro annual membership for a much lower price than
 </span>
 <span data-rw-start="170.56" data-rw-transcript-version="2">
 you normally would get it, 169 instead of 249, and this membership gives you access
 </span>
 <span data-rw-start="172.48" data-rw-transcript-version="2">
 to all the courses we have, as long as you have an active membership,
 </span>
 <span data-rw-start="176.4" data-rw-transcript-version="2">
 including the Cloud Code course and any future courses we may release.
 </span>
</p>
<p>
 <span data-rw-start="183.98" data-rw-transcript-version="2">
 In addition to the extensive course catalog we already have,
 </span>
 <span data-rw-start="187.38" data-rw-transcript-version="2">
 links below this video. Now, all remaining
 </span>
 <span data-rw-start="190.8" data-rw-transcript-version="2">
 approaches here, on the other hand,
 </span>
 <span data-rw-start="194.58" data-rw-transcript-version="2">
 are about executing
 </span>
 <span data-rw-start="198.44" data-rw-transcript-version="2">
 Cloud Code on your machine, not on Anthropic's server.
 </span>
 <span data-rw-start="202.32" data-rw-transcript-version="2">
 So, the cloud solution really is kind of a special solution,
 </span>
 <span data-rw-start="205.86" data-rw-transcript-version="2">
 also to be used in conjunction with those other approaches because, of course,
 </span>
 <span data-rw-start="209.82" data-rw-transcript-version="2">
 nobody's stopping you from executing some tasks in
 </span>
 <span data-rw-start="213.44" data-rw-transcript-version="2">
 the cloud whilst also working on other features in the same
 </span>
 <span data-rw-start="217.26" data-rw-transcript-version="2">
 project on your machine. You just have to merge the different
 </span>
 <span data-rw-start="221.18" data-rw-transcript-version="2">
 changes thereafter. So, let's start with remote control then.
 </span>
</p>
<p>
 <span data-rw-start="224.24" data-rw-transcript-version="2">
 Remote control is mostly about
 </span>
 <span data-rw-start="228.22" data-rw-transcript-version="2">
 continuing some task or some work that you maybe started
 </span>
 <span data-rw-start="230.1" data-rw-transcript-version="2">
 on your system,
 </span>
 <span data-rw-start="233.9" data-rw-transcript-version="2">
 still on your machine whilst you are leaving your machine.
 </span>
 <span data-rw-start="237.56" data-rw-transcript-version="2">
 So, let's say you're going for lunch or you have to go to a
 </span>
 <span data-rw-start="241.52" data-rw-transcript-version="2">
 meeting, but your computer, your, your Mac, your PC stays
 </span>
 <span data-rw-start="245.34" data-rw-transcript-version="2">
 turned on and you want to continue working on a
 </span>
 <span data-rw-start="249.2" data-rw-transcript-version="2">
 task. Now, obviously, Cloud Code will continue
 </span>
 <span data-rw-start="253.17" data-rw-transcript-version="2">
 you're leaving the machine, as long as your machine doesn't go to
 </span>
 <span data-rw-start="255.2" data-rw-transcript-version="2">
 sleep or shut down. But once it's done, it won't continue.
 </span>
</p>
<p>
 <span data-rw-start="258.959" data-rw-transcript-version="2">
 Now, with remote control, you can make it continue and you
 </span>
 <span data-rw-start="262.9" data-rw-transcript-version="2">
 can also start a new task, but your machine needs to
 </span>
 <span data-rw-start="266.56" data-rw-transcript-version="2">
 be turned on. And not just that, instead,
 </span>
 <span data-rw-start="270.54" data-rw-transcript-version="2">
 you need to start Cloud Code, the CLI in a special mode, in the
 </span>
 <span data-rw-start="273.88" data-rw-transcript-version="2">
 remote control mode, or in an interactive mode.
 </span>
</p>
<p>
 <span data-rw-start="274.34" data-rw-transcript-version="2">
 Session, you need to turn on remote control mode by
 </span>
 <span data-rw-start="278.16" data-rw-transcript-version="2">
 using the respective slash command.
 </span>
 <span data-rw-start="280.82" data-rw-transcript-version="2">
 Once the remote control mode is turned on, you can connect
 </span>
 <span data-rw-start="284.71" data-rw-transcript-version="2">
 your mobile phone with the Cloud mobile app, you
 </span>
 <span data-rw-start="288.66" data-rw-transcript-version="2">
 need that, to your machine by scanning a QR code,
 </span>
 <span data-rw-start="292.66" data-rw-transcript-version="2">
 for example, which you can have Cloud Code show you.
 </span>
 <span data-rw-start="295.65" data-rw-transcript-version="2">
 And then once that connection is established, you can
 </span>
 <span data-rw-start="299.66" data-rw-transcript-version="2">
 use a chat session. You can send messages to Cloud Code in
 </span>
 <span data-rw-start="303.54" data-rw-transcript-version="2">
 your mobile app, but those chat messages are then not sent
 </span>
 <span data-rw-start="307.51" data-rw-transcript-version="2">
 to the cloud or somewhere else, but instead to your connected machine
 </span>
 <span data-rw-start="311.1" data-rw-transcript-version="2">
 through remote control. So remote control can be very useful,
 </span>
 <span data-rw-start="315.02" data-rw-transcript-version="2">
 but it has a couple of potential disadvantages.
 </span>
</p>
<p>
 <span data-rw-start="318.98" data-rw-transcript-version="2">
 The two most important ones, in my opinion, being
 </span>
 <span data-rw-start="322.9" data-rw-transcript-version="2">
 to keep your machine turned on, and if it goes to sleep, you
 </span>
 <span data-rw-start="326.72" data-rw-transcript-version="2">
 lose the connection, so you must ensure it doesn't.
 </span>
 <span data-rw-start="329.7" data-rw-transcript-version="2">
 And you must start your Cloud Code session in
 </span>
 <span data-rw-start="333.58" data-rw-transcript-version="2">
 that remote control mode. If you forget this, there is no way
 </span>
 <span data-rw-start="337.54" data-rw-transcript-version="2">
 for you to send messages to it. So you must
 </span>
 <span data-rw-start="341.4" data-rw-transcript-version="2">
 set it up first and then you can use it. That is
 </span>
 <span data-rw-start="345.456" data-rw-transcript-version="2">
 where Dispatch comes into play. With Dispatch, you still need to
 </span>
 <span data-rw-start="349.476" data-rw-transcript-version="2">
 ensure that your machine doesn't go to sleep, though it gets a bit
 </span>
 <span data-rw-start="353.356" data-rw-transcript-version="2">
 easier, as you'll see, but you don't need to start
 </span>
 <span data-rw-start="357.316" data-rw-transcript-version="2">
 Claude Code in any special remote control mode first in
 </span>
 <span data-rw-start="361.216" data-rw-transcript-version="2">
 order to use it. For Dispatch, you need the
 </span>
 <span data-rw-start="365.196" data-rw-transcript-version="2">
 Claude desktop app, though you need to download.
 </span>
</p>
<p>
 <span data-rw-start="369.416" data-rw-transcript-version="2">
 And once you did that, you also need to go through a
 </span>
 <span data-rw-start="373.036" data-rw-transcript-version="2">
 one-time setup process to enable Dispatch.
 </span>
 <span data-rw-start="376.296" data-rw-transcript-version="2">
 In that Claude desktop app, you can also turn on a
 </span>
 <span data-rw-start="380.036" data-rw-transcript-version="2">
 setting that prevents your machine from going to sleep whilst the app is
 </span>
 <span data-rw-start="383.996" data-rw-transcript-version="2">
 up and running, though, so that eliminates this my machine went
 </span>
 <span data-rw-start="387.936" data-rw-transcript-version="2">
 to sleep and now my session broke or was canceled problem. Now, with Dispatch then set up, you
 </span>
 <span data-rw-start="391.656" data-rw-transcript-version="2">
 can use the Claude mobile app again, and
 </span>
 <span data-rw-start="395.736" data-rw-transcript-version="2">
 there, the Dispatch feature to send messages to
 </span>
 <span data-rw-start="399.476" data-rw-transcript-version="2">
 And the big difference now is that you don't need to start a Claude
 </span>
 <span data-rw-start="403.236" data-rw-transcript-version="2">
 Code session through the CLI first or anything like
 </span>
 <span data-rw-start="406.816" data-rw-transcript-version="2">
 that. Instead, you just need to have the desktop app up
 </span>
 <span data-rw-start="410.676" data-rw-transcript-version="2">
 and that is it. Now, you can send messages to Claude
 </span>
 <span data-rw-start="414.676" data-rw-transcript-version="2">
 on your machine, and it goes ahead and executes them.
 </span>
</p>
<p>
 <span data-rw-start="418.516" data-rw-transcript-version="2">
 Now, what's important here, though, is that Dispatch was
 </span>
 <span data-rw-start="421.436" data-rw-transcript-version="2">
 originally a feature released for Claude Cowork, which
 </span>
 <span data-rw-start="425.416" data-rw-transcript-version="2">
 is their more general AI assistant, not specifically
 </span>
 <span data-rw-start="429.336" data-rw-transcript-version="2">
 focused on coding, and therefore, at least right now when I'm
 </span>
 <span data-rw-start="433.256" data-rw-transcript-version="2">
 recording this, your Dispatch messages are
 </span>
 <span data-rw-start="436.756" data-rw-transcript-version="2">
 not connected to a specific project, which, on the other
 </span>
 <span data-rw-start="440.816" data-rw-transcript-version="2">
 hand, with Remote Control was the case since you deliberately
 </span>
 <span data-rw-start="444.616" data-rw-transcript-version="2">
 interactive session. With Dispatch, you're just sending a message to
 </span>
 <span data-rw-start="448.356" data-rw-transcript-version="2">
 Claude on your machine, and it needs to figure out what to
 </span>
 <span data-rw-start="452.156" data-rw-transcript-version="2">
 do with that message. That message could be totally unrelated to
 </span>
 <span data-rw-start="455.996" data-rw-transcript-version="2">
 if you want to invoke Claude Code to do some work in one
 </span>
 <span data-rw-start="464.016" data-rw-transcript-version="2">
 If you want to manage your projects, well, then, you will need to tell
 </span>
 <span data-rw-start="467.936" data-rw-transcript-version="2">
 it in that Dispatch message where to find that
 </span>
 <span data-rw-start="471.936" data-rw-transcript-version="2">
 project, give it some hints regarding the folder to
 </span>
 <span data-rw-start="475.275" data-rw-transcript-version="2">
 So, that can be a bit inconvenient here, but it is doable, of course,
 </span>
 <span data-rw-start="479.616" data-rw-transcript-version="2">
 and then you can start or continue sessions
 </span>
 <span data-rw-start="483.556" data-rw-transcript-version="2">
 from anywhere through the mobile app with that.
 </span>
</p>
<p>
 <span data-rw-start="487.196" data-rw-transcript-version="2">
 Dispatch feature.
 </span>
</p>
<p>
 <span data-rw-start="489.396" data-rw-transcript-version="2">
 And then last, but not least, we have Channels, and you would
 </span>
 <span data-rw-start="493.436" data-rw-transcript-version="2">
 kind of see Channels as maybe the
 </span>
 <span data-rw-start="497.156" data-rw-transcript-version="2">
 connection of Remote Control and Dispatch, and also,
 </span>
 <span data-rw-start="500.996" data-rw-transcript-version="2">
 Channels is essentially Anthropic's way of
 </span>
 <span data-rw-start="504.796" data-rw-transcript-version="2">
 trying to
 </span>
 <span data-rw-start="506.396" data-rw-transcript-version="2">
 merge Claude Code or their Claude offering
 </span>
 <span data-rw-start="510.136" data-rw-transcript-version="2">
 in general into an OpenClaw alternative.
 </span>
 <span data-rw-start="514.236" data-rw-transcript-version="2">
 Many features OpenClaw has are missing,
 </span>
 <span data-rw-start="518.216" data-rw-transcript-version="2">
 but Channels is, in the end, a way for you
 </span>
 <span data-rw-start="522.166" data-rw-transcript-version="2">
 to connect any kind of messaging channel to Claude
 </span>
 <span data-rw-start="526.216" data-rw-transcript-version="2">
 Code. And by default, Anthropic gives you an official
 </span>
 <span data-rw-start="529.736" data-rw-transcript-version="2">
 Telegram channel connector you can set
 </span>
 <span data-rw-start="533.216" data-rw-transcript-version="2">
 up, which makes it quite easy and straightforward
 </span>
 <span data-rw-start="536.856" data-rw-transcript-version="2">
 to use Telegram to communicate with your
 </span>
 <span data-rw-start="540.776" data-rw-transcript-version="2">
 Claude Code session. You still need to go
 </span>
 <span data-rw-start="544.536" data-rw-transcript-version="2">
 through a one-time setup process and enable
 </span>
 <span data-rw-start="548.456" data-rw-transcript-version="2">
 Channels,
 </span>
 <span data-rw-start="552.376" data-rw-transcript-version="2">
 and you also need to start a Claude
 </span>
 <span data-rw-start="556.216" data-rw-transcript-version="2">
 session with the channel you wanna use enabled, so.
 </span>
</p>
<p>
 <span data-rw-start="556.356" data-rw-transcript-version="2">
 You need to do that just as you had to do it with Remote Control.
 </span>
 <span data-rw-start="560.456" data-rw-transcript-version="2">
 But once you did that, you can use that channel to send
 </span>
 <span data-rw-start="564.316" data-rw-transcript-version="2">
 messages to Claude Code. So, you're then no longer limited to just
 </span>
 <span data-rw-start="568.276" data-rw-transcript-version="2">
 the mobile app. Instead, you can use your channel, and of course,
 </span>
 <span data-rw-start="572.216" data-rw-transcript-version="2">
 you could start a Claude session that you keep on running forever,
 </span>
 <span data-rw-start="575.816" data-rw-transcript-version="2">
 essentially, with that channel connected, and therefore, you
 </span>
 <span data-rw-start="579.836" data-rw-transcript-version="2">
 can keep on pushing messages to Claude Code there and work on
 </span>
 <span data-rw-start="583.736" data-rw-transcript-version="2">
 a broad variety of tasks. And of course, you could
 </span>
 <span data-rw-start="587.776" data-rw-transcript-version="2">
 also start Claude Code not connected to one specific project, but
 </span>
 <span data-rw-start="591.716" data-rw-transcript-version="2">
 in general on your machine with Channels enabled, and then kind
 </span>
 <span data-rw-start="595.596" data-rw-transcript-version="2">
 of use it as an OpenClaw alternative by asking it to do all
 </span>
 <span data-rw-start="599.546" data-rw-transcript-version="2">
 kinds of things on your machine. You could also do that with
 </span>
 <span data-rw-start="603.436" data-rw-transcript-version="2">
 Remote Control, and with Dispatch, as mentioned, it's the default,
 </span>
 <span data-rw-start="607.236" data-rw-transcript-version="2">
 simply allows you to use any communication channel of your
 </span>
 <span data-rw-start="610.776" data-rw-transcript-version="2">
 choice.
 </span>
</p>
<p>
 <span data-rw-start="612.076" data-rw-transcript-version="2">
 And of course, therefore, on the other hand,
 </span>
 <span data-rw-start="615.976" data-rw-transcript-version="2">
 and with the setup process you have to go through with Remote Control,
 </span>
 <span data-rw-start="620.136" data-rw-transcript-version="2">
 then you can just keep on using that, and you don't need Channels. It's also
 </span>
 <span data-rw-start="623.976" data-rw-transcript-version="2">
 noting that this Channel's feature right now when I'm recording this is in
 </span>
 <span data-rw-start="627.816" data-rw-transcript-version="2">
 research preview, and therefore, both the setup process and
 </span>
 <span data-rw-start="631.696" data-rw-transcript-version="2">
 the feature set may, of course, change over time.
 </span>
</p>
<p>
 <span data-rw-start="635.796" data-rw-transcript-version="2">
 I also mentioned a, a fifth, uh, secret way of
 </span>
 <span data-rw-start="639.936" data-rw-transcript-version="2">
 remotely talking to Claude Code, and this is actually
 </span>
 <span data-rw-start="643.896" data-rw-transcript-version="2">
 simply a way that you could use with any tool you have installed on your
 </span>
 <span data-rw-start="647.576" data-rw-transcript-version="2">
 machine, not just with Claude Code.
 </span>
</p>
<p>
 <span data-rw-start="650.536" data-rw-transcript-version="2">
 If you're running Claude Code on a machine which you could access
 </span>
 <span data-rw-start="654.556" data-rw-transcript-version="2">
 via SSH, so which is exposed to a
 </span>
 <span data-rw-start="658.396" data-rw-transcript-version="2">
 network or the internet, then, of course, you can
 </span>
 <span data-rw-start="662.276" data-rw-transcript-version="2">
 connect to that machine via SSH. And for example, you could have a
 </span>
 <span data-rw-start="666.076" data-rw-transcript-version="2">
 VPS up and running, which you maybe use for development work
 </span>
 <span data-rw-start="670.016" data-rw-transcript-version="2">
 instead of your Mac or your PC, and when that is
 </span>
 <span data-rw-start="673.896" data-rw-transcript-version="2">
 exposed to a network, to, uh, to the internet, uh,
 </span>
 <span data-rw-start="677.396" data-rw-transcript-version="2">
 preferably, of course, secured with, for example, a VPN
 </span>
 <span data-rw-start="680.996" data-rw-transcript-version="2">
 solution like Tailscale, then you can
 </span>
 <span data-rw-start="684.676" data-rw-transcript-version="2">
 connect to it via SSH. And you cannot just do that from your
 </span>
 <span data-rw-start="688.676" data-rw-transcript-version="2">
 Mac, which doesn't really give you a huge
 </span>
 <span data-rw-start="691.916" data-rw-transcript-version="2">
 You still have to be you on your machine for that, but you could also use an
 </span>
 <span data-rw-start="695.796" data-rw-transcript-version="2">
 app like Terminus on your mobile phone, make sure that this is
 </span>
 <span data-rw-start="699.636" data-rw-transcript-version="2">
 connected to this machine through a key pair, preferably, and then, of course,
 </span>
 <span data-rw-start="703.656" data-rw-transcript-version="2">
 you can start a session there and simply invoke any
 </span>
</p>
<p>
 <span data-rw-start="707.676" data-rw-transcript-version="2">
 command on that machine because it's just a SSH session, and
 </span>
 <span data-rw-start="711.596" data-rw-transcript-version="2">
 that, of course, therefore, includes Claude Code, and you can then
 </span>
 <span data-rw-start="715.516" data-rw-transcript-version="2">
 start sessions from there. Now, it's worth noting that
 </span>
 <span data-rw-start="719.336" data-rw-transcript-version="2">
 depending on your operating system and so on, when you close that app, the
 </span>
 <span data-rw-start="722.876" data-rw-transcript-version="2">
 SSH session gets, uh, terminated, and therefore, the
 </span>
 <span data-rw-start="726.616" data-rw-transcript-version="2">
 Claude Code session, uh, will stop. But still,
 </span>
 <span data-rw-start="730.536" data-rw-transcript-version="2">
 it is a way of quickly invoking certain one-off tasks, and of course, you
 </span>
 <span data-rw-start="734.496" data-rw-transcript-version="2">
 can use a solution like Tmux to kind of decouple your connected
 </span>
 <span data-rw-start="738.416" data-rw-transcript-version="2">
 session from the session on the machine and keep those sessions
 </span>
 <span data-rw-start="742.016" data-rw-transcript-version="2">
 going. That is all something you could also look
 </span>
 <span data-rw-start="745.726" data-rw-transcript-version="2">
 And that's, therefore, how you can use and control
 </span>
 <span data-rw-start="749.436" data-rw-transcript-version="2">
 Claude Code remotely on your machine or a
 </span>
 <span data-rw-start="753.076" data-rw-transcript-version="2">
 VPS. And as mentioned, if you wanna learn more,
 </span>
 <span data-rw-start="756.936" data-rw-transcript-version="2">
 that offer I mentioned before.
 </span>
</p>