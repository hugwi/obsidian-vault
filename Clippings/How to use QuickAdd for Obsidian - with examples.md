---
categories:
  - "[[Clippings]]"
title: "How to use QuickAdd for Obsidian - with examples"
source: "https://www.youtube.com/watch?v=gYK3VDQsZJo"
author:
  - "[[youtube.com]]"
published: 2021-07-24
created: 2026-06-25
rating: 
action: 
description: "Hey! I've made this neat little Obsidian plugin that I'm excited to share with you.QuickAdd: https://github.com/chhoumann/quickaddQuickAdd Q&A: https://bager..."
tags:
  - "clippings"
---
![](https://www.youtube.com/watch?v=gYK3VDQsZJo)

Hey! I've made this neat little Obsidian plugin that I'm excited to share with you.QuickAdd: https://github.com/chhoumann/quickaddQuickAdd Q&A: https://bager...

## Transcript

### Intro

**0:00** · hello my name is christian i've made a little plugin for obsidian called quick add and i'm very excited to show that to you today so what is quick add actually well it's a plugin for quickly creating and adding notes to your bolts this can be entirely known in new notes or something that you want to take a note of into an existing note

**0:21** · and it has a lot of ways to do that and that's what i'm here to show you today so why should you even use quick add well it can help you augment your workflows both your simple and advanced workflows but let's take a simple workflow as an example here you want to add something to your daily note but you're in the middle of writing something else and you don't want to interrupt your flow by going into your daily note and back

**0:45** · you can use quick add to add it to the daily note without ever leaving your note or moving your cursor i'll be showing you how in this video so let's just get started the first thing i'll show you is how you can actually install quick add so the first thing you're going to want to do is go into your settings then you will want to disable save mode and then you will want to click on browse open this model right here and enter in

### Installation

**1:11** · quick add and then you can click on the plugin click on install and you can enable it from here and you'll find that it is enabled here i have already installed a few other plugins and made a few files this is just so we can get through this a bit faster and you don't have to watch me type everything in so what we're going to be doing is we're going to be starting and creating a little setup i'm

**1:36** · going to show you things by analogy i'm going to show you some examples i'm going to explain how things work along the way so the first thing we're going to want to do here is you'll see we have this daily notes folder i've created this daily note template that we're going to be using so maybe we want to capture something

### Capture to daily note

**1:56** · and we want to capture something after this line that's where we're going to want to write if we did something that day maybe we bought some groceries we did some tasks and maybe we had some guests over something like that we want to note it down so we can go back to it in the future as relatively standard journal keeping or diary keeping i suppose you could say

**2:18** · so this what you're seeing right here is actually some format syntax i'll explain how that works a bit later but for now it's going to be seeing this template right here so i'm going to be copying this line because i'm not sure that i will be able to remember it later and let's just go in here into the settings and go into the quick add settings down here

**2:42** · so what we're dealing with is a capture and this capture is a capture to daily note i'm going to add this choice and we are going to click on the settings you will see there's a few buttons here there's first the add command which will add an obsidian command so we can do that and if i go into the command palette i can a quick add and it will show right here and i can activate the capture i will not be doing that right

**3:16** · now i will just want to go into the settings but there's also a delete and a move around there's not really much to move it between right now so that doesn't make sense to do so let's just go into the settings what you're seeing here is the settings for the capture i was asked how you can actually rename these choices and just click on the name that's maybe not as clear as it could be you can click on the name and you can rename it into something else maybe you want an emoji and let's just

### Renaming choices

**3:47** · pick sansa here and do that that was the windows emoji you get that up by clicking windows and dot at least on my computer i'm not sure how it works for mac or maybe linux but i'm sure you can figure something out so let's say we have this nice little capture to daily note and we're going to want to capture to a note the first thing it asks us to do is well which file do you want to capture two

### Capture Choice settings

**4:14** · and in our case we want to capture as you saw earlier to this folder we want to capture to some daily note but we want a node to have the name that is corresponding to the day it represents so in that case we're going to be writing daily underscore notes i think it was and then the slash this represents the folder then after that we're going to be writing these two brackets and then a date and then maybe a

**4:47** · colon and then we are going to be writing i believe it was dd slash mm slash and yy to represent date and you will see that this date actually appears here the 24th of the seventh month in a year and then year 21 that's the date and i'm recording this and it will change according to whichever moment you're writing something so if you actually write hh for hours and then

**5:20** · mm for minutes then you will see that i'm recording this very late in the evening and you can also write s for seconds which will update as you enter and of course when you activate the capture this will be frozen it will be the actual time that you activate the capture so let's just keep it like this for now and this is a fine daily notes format

**5:50** · and we write dot md after because that is the file name it is a markdown file after all and we're going to be creating the file if it doesn't already exist because if you're trying to capture to a file that doesn't exist well that doesn't really make any sense so we're going to be creating the file that doesn't exist and we're going to be creating it with template i showed you a bit earlier clicking here it will actually show you which templates i have in my templates folder click here and

**6:20** · select the template and it actually detects my template based on my settings for templater and the core templates plugin so if you inside of templater set that your folder is in this folder the templates are in this folder then it will actually look in that folder and prompt you to select from that one and the very same same thing counts for the chord templates plugin which i'm not sure i have enabled but it works just just as well so we're

**6:47** · going to go back into quick add here and you will see that we can also format what we enter as a task this is the very basic markdown task formatting also right to the bottom of the file we will not be doing that we will be inserting after which i'll show you how that works in a moment you also append a link this will append a link on your current cursor location which means in the file you're in currently linking to the file that

**7:14** · you're capturing too maybe you're capturing to some file and you want to record that you captured something to that file this will insert that link and what we are here after is the insert after this will insert the capture after the specified line and this accepts format syntax and this is what i showed you a bit earlier this right here that's format syntax

**7:39** · i'll show you all of the commands and where to find the reference for them a bit later in the video so we're just going to be entering here and this was why i copied the line before see right here this is the line that we're going to be inserting after and this will just enter it after the

**7:57** · line so if we select the setting here into that end of section then it would detect what will i personally believe it marks the section which is either another header or already three dashes this one right here which seems to be a marked down line splats or page break or i'm not

**8:22** · really sure what to call it but these three dashes you can also create the line if it isn't found you could do that at the top of the file or the bottom of the file we will not be doing that because i'm pretty sure this file exists because we created it in the template this line does exist i

**8:38** · also personally don't use these in my daily journals but you could do that if you want that's really up to you it's just really the order that it'll appear in when you enter things now right here you'll see that there's the capture format and we will be using this one because i enjoy having these in a

**8:57** · line or bullet point format i'm going to be writing a bullet point and i also like to record at the time of day that i recorded this so we're going to be writing very much the same that i showed you a bit earlier we will have the hours and the minutes

**9:14** · you will see just the same it will be appearing down here and we can write actually something called value this value right here it will ask you to enter something you could also just select some text and it will send that to that value so

**9:33** · if you have something selected it will take that and put it where the value is right here but this is generally what it will look like this tries to preview what you've entered in the format syntax here just the same as here and just the same as up here so let's try to see this in action i will just go out of the settings again close this down and i will make sure that this folder is expanded so when we click on the command palette

**10:01** · into quick ads right here and then capture to the daily note it will ask me well what do you want to write and i'll just say that i am recording because that's what i'm doing and you will see that right here it actually created the file and it entered this is the specific time that i am recording and you can do this for anywhere in any file you also create the file this concept kind of transfers so you got the general notion of what a

### Template Choices - create new note

**10:32** · capture can do and the very next thing i want to show you is how templates work you can see this template choices selected here and we will be creating something with this template right here it's a very simple template i just wanted to keep it simple for now but this template right here it will actually just write this and

**10:54** · then i will also show you that it works with the templater plugin syntax and that is the plugin you're seeing right here this is templater it works with everything that has to do with that so you can just write the template syntax freely and it will still work so you can go into settings here going back into the click out settings and we will create create note

**11:18** · and you just you can write whatever you want this is maybe semantically not very meaningful but create note is fine for now we'll be creating this choice and we'll go into the settings here template path we will just be selecting the one that i showed you before you can also format this file name

**11:38** · you can decide however you want to format it i will not choose to do it this time because i want to show you what happens if you don't click there you can also actually create it in a folder you can choose that well i want to actually select which folder it is out of all my folders when i'm creating the file you could also say instead well i want to either create it in the root or maybe i want to create it in the maybe daily notes folder and then it will ask

**12:07** · you which one of these you want to place it in if you only say it's in the root file the folder here you can also have another folder it doesn't really matter if there's only one here it will not ask you it will just put it in that folder we will not be using this it'll just

**12:23** · create it in the root and you could also append the link to the create a file in the current file we will not be doing that it doesn't really matter you could do that it will append a link to the new file you also increment the file name you may know this from your own file system if you create a file and it'll just name it untitled as per default at least in windows i'm not really sure for other operating systems it will create the file called untitled and you create one more file it will actually call it untitled one and that's the same

**12:55** · thing here it will just create it and call it untitled one two three four five um depending on which file name you give it this is really to prevent duplicates and so on you can also choose to open the file we will be doing that and you can open it in a new tab we will not be doing that you can choose if the tabs you have currently open should be split vertically or horizontally again that's really up to you but you can do it just as a quick note i actually after uh opening this template

**13:29** · just realized that this is uh here that had it before it's the wrong syntax it is actually tv.file a title i did not use template as much as i used to so i kind of forgot the syntax um but what you're going to want to do is you want to run quick add and create

**13:48** · a node we'll be calling it new file just for fun and then click enter you'll see that there's a template and it is the new file so you can see that this actually evaluated to what it's supposed to so that's really how that works i'm going to show you the multi-choice next that is really just a folder and maybe it's a bad name

### Multi choices

**14:12** · maybe it's not i'm not really sure it's multi-choice and it is a multi-choice because you can have multiple choices within that choice um so that's really all there is so let's just create one of those and call it let's say just a folder and maybe pick a

**14:29** · folder emoji for it and then add the choice we'll be dragging that to the top i know that this can be a bit finicky to get the choices within in here you can see that it's jumping around a bit that's because it's actually a very small margin to get it in there i will have to fix that at some point i have not done so yet it hasn't really been a priority because it does work and you can see that if i go back run quick add and i click on

**14:57** · folder it'll just show me the folder contents go back i can go in again i can click the capture and right test and you'll see that it still works just fine when i open the daily note and this is actually another thing that i forgot to mention when i was creating the capture you can go down here you can write backslides and and it will create a new line so instead of this occurring you will see that you can run it again

### Capture choice linebreaks

**15:24** · and if i test again it will create the new line and it works like you would probably expect it to and just the same you can go back in here instead if you don't want to write the backslash n which can be kind of confusing you just write enter and you can see that this works just the same go in here and again test again and it works just the same okay and the last type of

### Macros - capture new note from template to Kanban Board

**15:51** · choice i want to show you is the macro choice this one is going to be a bit more exciting and maybe a bit more advanced so i will try to explain how it works the best i can a macro choice represents some macro so we will just write maybe

**16:08** · add to kanban because that is what we are going to be doing and add the camera board what we're going to be doing like so adding it up here minimizing the folder and we will go into manage macros because we're going to be creating a macro and the very first macro i want to create here is add to kanban or it does not have to be

**16:32** · named the same as the macro choice but i like to do that because i can easily find it again then but you can decide on your own that's really up to you so we're going to be adding this macro here we can run this on the plug-in load that's really cool if you want to run something every time the plugin loads which in most cases is just every time that the every time that obsidian is started so you can just

**17:00** · do that or you can just go into this configure right here you will see that there's a lot of options and maybe too many maybe too little that is in the eyes of db holder so what we're going to be doing is we're going to be creating a template choice and this

**17:19** · is actually a nested choice or you also call it an anonymous choice because it is not going to appear out here and you cannot interact with it out here it is just something specific to this one macro and as you will see here when we are back in here we will have this template choice so

**17:40** · we will want to so let me just explain what we're going to be doing we're going to be adding something to this canon board we're going to be able to select which one of these four lanes we're going to be adding something to so let me show you how we can do that but first something about the kanban plugin and how it works so if you open this kanban plugin

**18:04** · board as markdown you will see that it actually just is a markdown heading level two with the lane here so and this is the same for everything else every other lane that you have so if we open this as the board again this is lanes you saw it in the markdown it's just a heading level too that's very important to take note of but let's just move in here into the after camera board so the first

**18:33** · thing we're going to be want doing is we're going to want to have this here i'm not going to say what the board is just yet you'll find out in just two seconds so add to oh actually it's create new item that's the first thing

**18:50** · we will be creating this as a cabin template and let's just say we don't want to clog up any uh folders files and so on so we will just be naming it updates this is a very normal way to do it as an id just dbmm yy um maybe

**19:11** · something else that's completely up to you and then yeah one out here and then let's just say uh value title like so and click that this is what is called a variable this variable right here will actually ask you to enter a title and this will be saved for the next choice that is in the macro

**19:39** · sequence i'll explain that in a moment just be aware of it for now we will not be creating anything in the folder that doesn't really matter for now you should do that if you're maybe doing that i prefer to do that it's choice so you can also paint the link no we will not be doing that we will not be doing this nor will we be actually yeah just let's just open it for fun we will do it as a split and we'll be copying this right here

### How macros work

**20:05** · we will be going back and i like to add a delay it doesn't really matter uh honestly it really doesn't matter but you can do it um just before i move on and create the capture let's just explain these this one here a student command this adds an upgrading command it's every single command that you have in your command palette you can run that so maybe you want to save the current file add it and that that's what it says save the current file through the obsidian command and that's really all there is to it you can delete that and the next thing here

**20:37** · editor commands this will copy whatever you have selected this will cut paste uh just the same deselect the line in the editor this will select the active line so that means the entire line and this will select the link on the active line it will go for the first link it will ignore all other links just to be aware of that we will not be doing that so we also have user scripts i will show you how those work a bit later that's a bit more advanced and maybe requires some skills and javascript or at least

**21:06** · someone to tell you what to do and that will be me today you can also add a choice if you want something like maybe this as the macro this would be very recursive and very annoying so don't do that that that would uh just maybe crash your obsidian or at least freeze it so don't don't do that you can add another choice uh create the note or maybe something else but we will not be doing that either we will be creating a capture this capture will add item to

**21:38** · board like so and we will actually just be selecting the kanban board and you could also make this use format syntax i don't think you're going to be renaming your common board that much if you do you're gonna have to change this but if you don't well then you just keep it as is and we will not be creating the file that does exist because we know that it does exist we'll we will be creating the thing as a

**22:06** · task i will show you what it ends up looking like in the end and we will not be writing to the bottom of the file we will not be appending a link we will be inserting after let me show you something a bit magical here so if we we actually write two hashtags or pound symbols and then right value and then a colon we if you remember from before there were four lanes and then they were all something very boring that is lane one plane two

**22:37** · and lane three and lane four so we just go back and actually delete the spacing here because that is um not necessary we will be well you could add to the section it doesn't matter you could do it this would add to the bottom of the lane beneath all other cards um you could yeah let's actually do that

**23:02** · create the line is not found no we know that the line is actually found so we will not be doing that so capture format now this is going to be and this is also why i copied the uh the format a bit earlier you'll see that we're just going to be once to when we just want to enter it here you can see that this represents the exact same name as before and we put some brackets

**23:26** · outside of it this is actually the name and the link to the um the file we create in this choice right here so let's actually go ahead and try this out so the way we're going to be doing that and something else that you maybe have seen here is that

**23:46** · when we're doing the capturing we actually selected a value title again but doesn't that ask me twice but no it actually doesn't it doesn't ask you twice because values persist through every single item in the sequence so every time you assign something to a variable it can be reused and another very important point is that it can also be reused in the scripts that you can add and you can also set values from your scripts this is an

**24:17** · important important point we'll get back to that a bit later it's just for now let's just try to add something to the comment board before we can do that we will click here configure we only have one macro right now so we're just gonna going to be selecting that going back here and we will be running click add and add common board as you can see it asked me for a title and well we're going to be entering a title before i'm going to be doing that i just want to make sure one thing so just hold on so you can see

**24:48** · right here i made this little template this looks very familiar to something we've seen before and if i actually did remember correctly i should not have written title it should have been this value right here so we're going to go back in here in here oh no right there but in here and here and instead of title it will be item name and the very same thing we will do in here under

**25:19** · here and that will make it a bit more consistent so let's just go back out and we will go back and maybe you can see what this will be in the moment when i add it here item name well let's say a verifying plant and the price well i don't really know let's say it's an expensive plant 50

**25:41** · something currency link i don't have a link right now uh let's just write a test uh this is oh i don't have a category for planes uh entertainment maybe some people but let's just select other and we will be creating it somewhere in some lane uh which lane should i choose maybe lane

**26:02** · two is fine just as a quick note i actually realized that i forgot to put spacing right here so that's just a little blender in my part just write the spacing between to actually make it match the line that you wrote in your kanban but besides that i will be deleting this file again that i mistakenly made go back here you can see that i also make mistakes uh so let's just run the quick add add to board as you can see we write an item name client and well it's an expensive plant

**26:33** · so 50 and again no link test again and while this is i don't really know what this is let's just say something else and then lane one then it appears here in the kanban board we can see we have it open here and this could be a plant tracker wishlist something i'm not sure this is just a very basic way to add something to a board you could also just use a capture

### Simple capture to Kanban Board

**27:00** · you could just select that you want to capture a simple line with no markdown this is because of the semi-advanced feature in the kanban board which allows you to inquiry for gamble front matter that's why what we've been doing here name price link and type and you will see that this is in the front matter for this file so when i uh enter preview it would actually not show anything right here so this is a relatively

**27:31** · maybe semi-advanced way to add something to a camera board a lot simpler way to do it is just to add to board make a capture and then just say go here we will just select the board and play task and nothing else really

**27:53** · besides say adding it to lane two and then sure and then here do we need to do that no we actually do not need to do anything here we could do it we could not do it that doesn't really matter we add it click add and add to board right test it will add it to the lane two and that's how that works so that's

### Advanced features

**28:17** · three pretty simple examples maybe this last one is a bit less simple but that's three examples of how you can use quick add to add something to your vault i will show you how to install user scripts next we will be looking at the satelizer that eleanor uses

**28:33** · um from what i can hear quite frequently and i will be showing you the quick add api and i'll be showing you inline js and how to use the api with that so let's just move to that okay so how do you actually install a user script into your quick ad so this is just going

### Installing user scripts - installation of Zettelizer script

**28:52** · to be something you're finding maybe on the quick ad repository on this repository i actually do have a lot of examples like i said a bit earlier we will be taking a look at look at the satelizer so let's open that and this shows the

**29:09** · video you can get the js file user script here that's what we're actually looking for and let's go in here this is a javascript file so there's a way there's actually a few ways to install the script one way is just click on raw and then copy everything in here right click copy

**29:31** · open a notepad document and just paste it like so let me zoom out here and i will go to my vault in the save as you will see that my bolt i have it actually open right here this is my demo vault

**29:55** · and let's just go into the scripts because that is where i want to place it it's very important that you save as type and you select all files and you can write something maybe even set a lighter i wrote that wrong it's yeah that's fine set and then save this is now a javascript

**30:12** · document and we close notepad we're done with that and you will see that it actually appeared in here in the scripts folder so what quick add does is it registers every single file with the js extension so if you're going to manage macros click on just add macro

**30:34** · configure that add your script and satelizer so the satelizer here will run as soon as we add activated which is done through a macro choice \[Music\] we will spell the name correctly this time add it here drag it to the top and we can run the

**30:56** · satellizer something very important to note about the satellizer and maybe i should just show you how you can change that let me open it with uh yeah notepad again you can see that i made this for eleanor so it's actually very specific to

### Customizing and using the Zettelizer script

**31:16** · the setup in her vault so right here you will see that this is a folder that you may not have so what you'll want to do is just write whichever folder you're going to want to save to i want to save to settle

**31:33** · and i don't have that folder i'll make it in just a moment so and again this is very specific to her workflow so it i will show you what it does in a moment i'll create a test file and show you how it actually works let's create the settle folder create a new file and this is a research

**31:54** · paper or something and then maybe some notes i'm not really sure how those would be structured this is the right test and then we have a heading three which the script looks for on this line you can see right here if the heading is totally free then we will do something and there's a location id so let's just say page 34 we will we do not care about that but we do want to add a new uh file in the saddle folder

**32:21** · and we will be calling this something maybe just a this is a heading and we can copy this line and paste it a few times and maybe three two one because i'm not very

**32:39** · creative right now so just if you run the satelizer on this right here and let's just forward uh the sake of having something at least different doing this we can run the satelizer run the satelizer and run the satelizer

**32:57** · and you will actually see something i forgot that just what i said you should do before you can just go ahead and click and click on settilizer select an actual macro for the macro choice otherwise it will not work i have been considering moving this a little bit so it's actually managed in the managed macros instead of um

**33:19** · through this kind of proxy here um that's a bit technical maybe for later but that is just how that works so let's just click add set laser you will see it made three files right here based on the names and it only registers

**33:35** · what's after the location and it just adds a link to the heading so if we open file gun and which file was it actually can't remember recent paper that's right and one two three you'll see that it actually uh turns i think it translucent i'm not really sure what the word is actually but this is what it does this is the satelizer in a nutshell uh there are variations of the scripts i

**34:04** · have made one for myself and other people have also made one uh you can really just pick and choose on the discord i sometimes share other people sometimes share how they use it and then you can see that some people create whole new files where you just copy all the content here into a new file just like i personally do so that's something you

**34:26** · to be you should be aware of that this is not the only fertilizer but there it's just the one way to do it but this actually keeps your your original file kind of clean because it doesn't remove anything it just adds links with the heading name still so you can link to it and it will just show what's actually under heading here okay and and this at this point we're actually at where i want to show you the quick add api this is some more advanced features

**34:58** · so i don't expect everyone to be able to follow and that's fine but if you want to follow along maybe some javascript knowledge would be a prerequisite i will try to explain as best as i can how to use it but it is something that is a bit more advanced so um we will take that as we get to it before

### Format Syntax

**35:18** · that i actually promised a bit earlier that i will show you how to find the format syntax reference it is right here you can see that you can use format syntax and a link to it here this is all the formats and text there is um there's explanations next to them so i will not be explaining them um you can just uh look at it right here

**35:41** · so the quick add api it's right here this is the quick add api this is also the page where i will be adding additional features too as they come out you will see that there are a few functions just very basic utilities and maybe

### QuickAdd API

**36:02** · features that allow you to interact with quick add and some of the things that i've made for quick add so the first thing is an input prompt which opens the prompt that you saw a bit earlier just no prompt that's just asking your yes no it's the very same one that actually appears when you maybe want to delete something and likewise we also have the suggester you saw that when we were adding a board card to a lane in a kanban board

**36:32** · and there's a example here that you can actually write it in this syntax and that is if you're not familiar with javascript this is just a map function on this parameter here then we also have a checkbox box prompt i have that shown in an example in here

**36:54** · and you will see it in the fetch task from to do it todoist and maybe it'll come in the video here but it will be appearing at some point during this video you'll see how that works the other thing here is the execute choice and we can actually execute any choice with a given name and you can pass variables to it so if you have a template choice and you want to spawn a template if let's just maybe say these value

**37:26** · names you can write these values or variable names and it will be filled into that choice and likewise all of these functions are actually async so just await them there's also the utility module this will allow you to interact with your clipboard which is what it does currently i will probably be adding some features to interact with some kind of date

**37:55** · and file system actually probably the obsidian file manager or something like that i'm not sure yet because it's actually already available something you will notice is that if you go in and check out what the parameters

**38:15** · send to you when you open the quick api and this is something that i may not have documented as well actually i did under macros if i remember correctly and down here somewhere i think here

**38:31** · somewhere here yeah here it is a when you make a macro like this you will be given access to these things a reference to the app the quick add api and variables and that's really all there is to it you also get access to the utility module but that's in the quick add api so when you actually have these for rams here you can see that i do some destructuring and um maybe just

**39:01** · drag out the input prompt here and then use it a bit later so that's what's happening there you can find the references here i expect that if you know what you're doing you probably don't need me to tell you what you're going to be doing with this so that's why i'm being a bit brief and maybe a bit cryptic but you can also actually do something that is i will show you in this template right here you can do something called inline js which is going to be spawned

### Inline JavaScript

**39:28** · when you write six back text you write this space quick add and let's just for fun write something to the console with console.log we'll be writing hello world because that is a very standard example and i will open the console there's a lot of things here so i'll just close that close this and when i execute oh that's the switcher

**39:56** · execute quick add open the folder and create a note and then give it a name it will actually just expand everything in that template boom and then you will see that it will execute this hello world and if we go back again to the templated demo you will see that if we console dot log this i have passed the quick add

**40:21** · api and the other references that you were given means we can actually console.log or this dot click add api and we can see what's inside the quick add api so let's just try doing that and click add and then folder and create the note and let's just write text one here and as you can see hello world logged and we have the this um

**40:51** · log and then we have the quick quick add api uh log here as well so that's how that works you can execute whatever javascript it is async by default so you can write async js in there if you want there's not really much more to it actually if you know javascript you can actually include whatever what you write in here will actually be written so if you return some string for example you can say

**41:25** · this was let's just do markdown this was my script and then you again make a new note like so and then you write test two you can see that this executes and it writes this was my script so you can write something dynamically and i use this to actually grab books from read-wise and put in all of my notes you can find that example right here and

**41:56** · then you can see that this will expand in the template here it runs the macro and read buys and then insta-fetch stupid book this is just a macro not inline api it didn't really matter it runs the macro goes into the revise i use this concept of name namespacing where you can access if you have a macro here this is a simple script instead of doing module.exports you can export an object and in this object you can

**42:28** · choose to export multiple functions or values it doesn't really matter so i could actually just say that i want to export maybe some value this is going to be 100 and i can go ahead and select that value and it will just write 100 so that's something you could do you do use that for api keys something else you could do is you could also import i'm going in notepad i didn't really think i was going to be doing that today you could import um some module

### Exporting multiple functions and variables from a module

### Importing modules

### Outro

**43:01** · uh this is just this is to be actually import module from and then you can write something which is going to be the path to the module like so so you can also do that you can use it down here so maybe module but do something something something

**43:23** · okay so that's that's how that works there's a lot of things you can do with um scripts you can ask me if there's something you want to do and you maybe don't know how to do it feel free to ask me but this is really this is a probably quick ad and nutshell probably took like 30 minutes so maybe there's a lot if there's something anything i did not cover in this video i will be writing about it so if there's some question that you feel that you asked me but it didn't cover i i will i'm already aware of those

**43:51** · questions i have written about them and if i miss your question please do just ask me in the comments i will respond to you and i will try to do my very best to give you a satisfactory answer i hope you enjoyed this very small demo of quick add i will gladly show how i use quick add in my own vault i have a lot of quick add templates and use cases but very many of those are

**44:20** · similar to the ones i showed in this video so i really hope you enjoy and i really hope you could get some inspiration inspiration out of this video thank you very much for watching i hope you have a great day