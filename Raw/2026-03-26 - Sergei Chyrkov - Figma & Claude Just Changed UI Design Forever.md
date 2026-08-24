---
title: "Figma & Claude Just Changed UI Design Forever"
source: "youtube"
url: "https://www.youtube.com/watch?v=Xcgr-7LpzDM"
author: "Sergei Chyrkov"
published: "2026-03-26"
created: "2026-08-24"
duration: "0:17:43"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "local-llm"
  - "mcp"
  - "skills"
  - "video-gen"
  - "web-design"
summary: "Figma just changed the game again. You can now 
generate full UI designs directly inside your canvas using AI. You 
can use your actual design systems to generate layouts that already match your product."
---

# Figma & Claude Just Changed UI Design Forever

![Figma & Claude Just Changed UI Design Forever](https://www.youtube.com/embed/Xcgr-7LpzDM)

## Description

Figma just released a massive update: you can now generate UI directly inside your canvas using AI agent (Claude, Cursor) — and the craziest part is that it can use your own design system. This means no more generic AI layouts.

⚙️ How to set up Claude Code and Figma MCP: https://youtu.be/FqQMIQRcdj8
👉 Figma skills: https://www.figma.com/community/skills
👉 Design tokens file (full version): https://chyrkov.lemonsqueezy.com/checkout/buy/1dbeefbe-6925-4a43-a7e5-18d2d3affc57 (Use FANS10 for 10% off)
💌 Need help or want to learn more? Sign up for a mentor session: https://sergeichyrkov.com/learn

You can generate real product UI that already matches your components, styles, and workflow.
In this video, you’ll learn how to set up and use this new feature step by step using Figma, Claude Code, and the terminal.

We’ll cover:
- What the new Figma AI Canvas update is
- How to connect it with Claude Code
- How to generate UI inside Figma using prompts
- How to make the AI follow your design system
- Real workflow examples you can start using today
- How to turn your designs into code
If you're a UI/UX designer, product designer, or frontend developer, this feature can seriously speed up your workflow.

______________________________
Check out my links ⬇️
▸ My website — https://sergeichyrkov.com
▸ My studio — https://chyrkov.studio
▸ My curated resources library — https://designsweets.co
▸ Twitter — https://twitter.com/sergeichyrkov
▸ Instagram — https://instagram.com/chyrkov
▸ Behance — https://www.behance.net/chyrkov
▸ Linkedin — https://linkedin.com/in/sergeichyrkov
______________________________
Useful stuff:
👉 Build websites in minutes with Framer — https://framer.link/chyrkov
👉 Record your screen like a Pro — https://screenstudio.lemonsqueezy.com?aff=GO290
👉 Best music for your videos (get 30 days for free) — https://www.epidemicsound.com/referral/am81qn
______________________________
📝 Chapters:
0:00 — introduction
0:37 — how to create a design system library 
3:02 — how to launch Claude Code for you project
5:19 — connect design system with Claude project
8:25 — how to generate design using design system
9:18 — results 
11:26 — how to add Figma skills to Claude Code
14:10 — generate code from Figma design
15:30 — results
______________________________
😍 Monetarily Supporting The Channel:
If you like what I do and wish to support the channel monetarily, you can donate me with some coffee here: https://www.buymeacoffee.com/sergeichyrkov
This is appreciated and helps the channel, but please don't feel that it is necessary to enjoy my content.
______________________________
📃 Disclaimer:
Some of the links in my video descriptions are affiliate links, which means at no extra cost to you, I will make a small commission if you click them and make a qualifying purchase.

______________________________
#figma #ai #claude #vibecoding

## Transcript

Figma just changed the game again. You can now 
generate full UI designs directly inside your canvas using AI. But here's the crazy part. You 
can use your actual design systems to generate layouts that already match your product. No 
more random AI designs. No more redesigning everything from scratch. In this video, I will 
show you how this works using Figma Claude and your terminal step by step. Let's get into it. 
Hi, my name is Sergei. Welcome to my channel. Here I talk about Figma framework AI vibe coding. 
So be sure to subscribe if you want to learn more about it and like the video if you like it. So 
before we start generating our designs using AI, we need to have a design system that we'll be 
using. And if you don't have your own design system, you can grab one from community or create 
one yourself. Uh actually I'll be using a simple design system library by Figma. uh you can get 
it from the community as well. So you just go to community tab and then you go to uh this filters 
design resources you click UI kits and here you can choose a simple design system you click on it 
and open it in your uh Figma file. So basically you will duplicate it to your drafts but here's 
a trick you need to move this file from drafts to a project folder. I already done that. Uh and 
then what I need to do I need to go to assets in my file and then I need to click on this book icon 
which is called libraries and here we can see that uh in this window I see manage libraries 
screen and I need to publish it. So I press publish and this file will be published 
as a library. So it will be available uh for other um projects. This is like the first 
step that we've done. The next step will be is to create a new file. So let's press create and then 
we press new design file. And now we need to link our published library to this to this uh file. And 
actually it is in the drafts and it doesn't really matter where it is. So you only need to have your 
library in the projects folder. And here I go to assets and again I click on this library icon or 
I can click here browse team libraries. And when I click on it here I can choose the library that I 
want to use. So I'll click see more and I'll need to find the library that I have published. So 
this one is right here the simple design system library. So I click add to file. So it's added 
you see and I have it over here on the left. So now I can close this. Uh, and now if I want 
to create something here, I just go to assets. I click here and I can choose some of the things 
from the library. So I can basically drag and drop any assets that I want. And now let's go to cloud 
code and set it up and try to generate something. First of all, we need to create a folder for 
our project and it should be empty. So you don't need anything here. Uh but the only thing 
is that what you need you need to connect it to cloth. So basically you can't launch cloud just 
your desktop. Well you can but it's it's not a good thing. Uh you need to have a folder where all 
your files will be um will be set up and will be collected. Uh so and generate it of course if you 
generate some code from your designs. So I have my folder ready Figma cloud test and now I need to 
open it in terminal. So I just click right click and open it in terminal. So here's my ter terminal 
and here what I want to do I want to just write claude and basically I'm launching claude inside 
of my folder. Press enter and we need to wait a few seconds and here it is. We can see that Claude 
is launched. We can see that it's launched in my folder. So now I need to check that I have my 
Figma plug-in ready. So what I want to do, I want to press um the slash and then I'll write plugins. 
And now I will just click plugins and then I will search for installed. And here you can see that I 
have my plugins Figma remote MCP installed. It's local. So I can see some other some other uh 
plugins that I have installed um in my in my cloud and then I press enter on Figma remote MCP 
and I can see that it is ready. We have 16 tools inside and I have authorized it and to my account 
in Figma account. So it is connected. If you want to learn more about how to set up uh cloud code, 
how to connect it, how to connect it to Figma MCP, be sure to check out other video on my channel. 
The link will be somewhere on top and in description below. All right. So Figma MCP is set 
up. So we're cool with that. Now I press escape and I just go to my sort of like prompt window and 
now what I want to do I want to connect it to my um to my library right so I want to find it so 
basically that's why we need this folder so the folder project uh will be associated with uh this 
design system so now I go back to design system and I need to click share and copy link to it. 
And now I go back to cloud code and I just paste this link here and I want to write a prompt use 
this or just analyze this design system system file for future for future um work and press 
enter. Now it will do some thinking and one more important thing is that in order to have this 
clothe code running you need to have a paid plan uh of code here I need to press enter. Yes. 
Yes. So I agree with everything. Uh we see some errors but it's okay. Just go back to this design 
system. Uh let me just uh show you some of the things that we have everything in components. And 
this is super important that everything is in the components. So we have for example cards, buttons, 
everything is a component. And of course we have variables. This is super important as well to 
have design tokens inside of your library. And that all of your elements inside of your Figma 
design layouts, they should be um created using variables. So this is crucial. So as you can 
see, all the buttons are using variables here. So now let's go back to um code and and here you 
can see that I had some errors but uh here we can see that it loaded the skill figma use this is 
super important this one of the this is one of the updates the recent updates and here it says that 
excellent let me get the design tokens variables to inspect the key foundation pages so this is 
this is working correctly um don't worry about the errors sometimes Sometimes I get them because 
um for example some weird naming is used in the layers or it's not that important right now. 
Here you can see that it analyzes the text styles and component inventory and again it it is using 
Figma remote MCP again and here is the summary. So uh it organized everything in layers. So we have 
foundation with typography, color effects, icons, composition guide, component pages. So everything 
is set up. So yeah, it finished. So it read and understood the structure of the design system 
and now it understands and knows everything about all the elements that are inside of the 
design system. By the way, if you want to learn more about vibe coding, Figma, Framer, be sure 
to check out the link in description below to my courses and my newsletter. All right. So, what 
we want to do next, we want to generate something, right? We want to generate some UI element. So, we 
go to our untitled file. We have our design system connected to this is super important. And now we 
need to click here share and we need to copy link to this file. Now, we go back to clo code and we 
use a command. We use command to generate stuff. So we use slash and then we just find Figma. We 
use generate design. So I will just use a tab to save this command and I will use this command to 
generate design and uh write create login screen or using our design system here or yeah so I just 
pasted the link to uh the file and now I press enter and let's wait for magic to happen. Right. 
Claude code finished the job and as you can see our login screen is ready just from one prompt and 
here is the summary what it did actually it used some input fields some buttons and it created the 
layout in this desktop version right but let's see the most interesting thing about this um design 
because before we didn't have that before it just generated some designs uh and uh the elements that 
we used there that were generated basically from scratch. But here's the the most important thing 
about the list update. Let's check out the screen and let's click on some of the fields here. And 
as you can see, they're in the components and basically they're instances of the components. 
And if we right click on them, for example, on the button, I will click go to main component. 
And look what is happening. I'm going back to my design system file and to the button here. So this 
is super cool that it actually used the files the elements from the design system to build this UI 
element. And this is super cool. This is the power that basically from your design system now you can 
build interfaces without actually pushing pixels with the detailed explanation of what you need 
to have on in the interface and it will generate uh the interface for you using your design 
system. This is super cool. And if we since we're using design system you see I'm using this 
uh it uses the black button. Uh let's change it to for example green. And now I will publish this 
library. I'll publish it for for example something changed, right? Uh and we needed to change the 
color of the button. And now the library will be published. And now I go back to my file that 
was generated by Claude. I go to libraries and here I have an update. Pull the update. And now 
I have the green button here. Magic. Some extra things that you might be interested in is that 
you can actually add some special skills to your Claude Code. And these special skills are actually 
recommended by Figma. So if you go to your browser and if you go to figma.com community skills uh you 
will find uh here some Figma skills for AI agents and some of them are made by Figma which are 
already saved in your plug-in but some of them are like an extra skills made by other um community 
members. For example, this one apply design system and actually it connects existing design systems 
to publish design system components. So basically this is what we're doing but this commands will 
have more power and then just the basics that are already exist in the Figma plug-in. So if you 
go to this to the skill actually I recommend you going skills folder uh and uh this I guess Chris 
made this skills and there are three of them apply design system audit design system and fixed design 
system findings. So basically this is the skills that will help you work with your existing design 
system and you need to install these to Claude Code. How to do that? That's actually really easy. 
You just go to code here and you need to copy the link to this repository on the GitHub and then you 
need to go to your terminal just paste the link here and tell cloud to install skills and you 
need to wait a few minutes. There will be some questions about what I need to install exactly. 
You just say yes and it will in it will install all the kills inside of the cloud that is on your 
computer. So basically yeah here it asks should I look at the this repository. You say proceed yes 
and stuff like that. So and now you go back and um uh the these are the same from the same 
developer and there are other ones right here for example like sync Figma tokens. Basically 
what it does it syncs tokens from your from in the code and Figma variables. This is also a very 
important skill that and very important thing that you should do if you have uh your design system 
and code and you need to sync it with your Figma design system file. And same thing here you can 
just copy this command or right here you can copy the link to this skill and again you just go to 
your terminal and install it. So basically what it does it it reads the repo and it will install 
all the skills inside of your code. Now since we have this design already set up right in in Figma 
uh let's try to bring it to code right. So what we need to do we need to select the frame or we need 
to uh click right click on it and right click and here we need to find something like copy link to 
selection or basically you can just use comment l uh and then you go back to again terminal with 
your project the clone running in your folder and you just paste this link and tell them to 
basically uh develop it and you need to explain what kind of technology or what kind of tech you 
want to use. So basically, so create HTML CSS file from this design and press enter. And now it 
will launch the skills that are used to actually develop it. And now I want to use yes and don't 
ask again because basically similar questions concerning this particular project. Uh so I just 
want to allow claw to use it. And let's wait a few minutes. And yeah, that's it. It's ready. So 
I press yes. I want to save it. And when I go back to my folder, I have this file already here. And 
what I want to do now, I just want to launch it in my browser. Well, actually, it's not finished 
yet. So, let's wait just a few minutes. Oh, a few seconds. Yep, now it's finished. So, it created a 
login HTML and login CSS where all the styles are. And now I want to launch it in my browser. So, 
I just double click on it. And here it is. So, it already did it. So, it's in code. So, as you 
can see, it didn't use the green button. I'm not sure why. Probably because uh the main component 
had the black one and also it added the icon here that was inside of the design. I checked my 
terminal and I found out why it didn't use the green color of the button. And actually it 
told me that there was a mistake and there was an issue that in the design uh there was a green 
color that we used in the button. But it was wrong because in the Figma variables and design tokens 
inside of our design system it is stated and that the default brand color is black instead of 
green. So that's why it changed it from green to black to make it default as it is in the design 
system. So basically it thought that that was a mistake because it wasn't changed uh in the design 
tokens. So this is super cool and smart. But the cool thing is that it has all the styles all the 
variants of the components are used. You can see that we have hovers. So everything is cool here. 
I can even enter something and when I press uh of course sign in doesn't work but still looks pretty 
good. And let's check out the CSS file. I'll open it with my text mate. And as you can see, we have 
all our tokens in the CSS. They're used here uh from the design system, which is super cool. And 
let's just open the login just to check how the code looks. Yeah, here it is. Um, yep. So, it's 
pretty simple, but everything is here. Thank you so much for watching this video. I hope now you 
understand how you can use Claude Code to generate UIs using your design system and not some generic 
stuff. And be sure to subscribe to my channel if you haven't already and like the video if you like 
it. And I'll see you in the next one. Bye-bye.
