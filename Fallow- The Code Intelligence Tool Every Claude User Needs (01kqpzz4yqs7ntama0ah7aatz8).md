---
categories:
  - "[[Resources]]"
domain: engineering
title: "Fallow: The Code Intelligence Tool Every Claude User Needs"
source: "https://m.youtube.com/watch?v=-lCfwIoDXq8&time_continue=22&source_ve_path=NzY3NTg&embeds_referring_euri=https%3A%2F%2Fwww.google.com%2F&embeds_referring_origin=https%3A%2F%2Fwww.google.com"
author: "Better Stack"
published: 2026-05-01
created: 2026-05-03
description: "AI coding agents are great at shipping features fast, but they also ship"
tags:
  - to-process
  - agent-plugins-mcp
---

This is Follow, a code-based intelligence tool for TypeScript and JavaScript that analyzes your entire code base for dead code, duplication, unnecessary complexity, and much more, meaning there's no need to use a combination of nip, JSCPD, and ESLint just to stop your agents from shipping bad code. It's built in Rust and supports over 90 plugins, meaning it will work out of the box with most frameworks and popular packages. But, the fact that it only supports JavaScript and TypeScript make it less appealing for AI-assisted coders. Hit subscribe, and let's find out. 

So, here is a project that I'm working on that adds a cinematic film look to videos and images. It's mostly been built with Claude Code, so it will have some level of AI slot. There's also a PR here for a new feature in that project, which I'll talk about later, as long as GitHub doesn't make it disappear by accident. So, to get started, I'm going to run Follow with the summary flag using bun x, which means I don't have to install it. And this gives a snapshot of my project showing the dead code summary, duplication, and a complexity 

health summary. And if we check the Git status, it adds a new .follow directory that contains the cache, so that means subsequent runs of this command will be faster and contains snapshot and any plugin information. Now, you may have noticed it here that the health is 41 above the threshold. Now, what does that mean? Well, the Follow health score is calculated by working out the cyclomatic complexity and the cognitive complexity. And it uses some formulas to calculate the complexity density, and down here, all this is used to figure out the 

maintainability index, which is the score that we see over here. So, based on this score, it's detected that 41 of my files need to be refactored. From here, we can run any of these commands to get a more detailed report about a specific area. So, if I wanted to focus on health, we could run this command, and after a while, it lists all the files that have different health issues. Note, if you want to know what CRAP stands for, this is an abbreviation for change risk antipatterns, which you can learn all about in the documentation. But, this level of detail is very easy for an agent to follow and know what to 

fix. In fact, the duplication is a lot easier to follow since it gives the exact file and the specific line numbers. So, we'll stick with that for now. And if we wanted to, we could add a Follow configuration file to give Follow information about certain patterns or dependencies you want to ignore, as well as setting some custom duplication settings, health setting, and adding boundaries, which is a very cool way of declaring which directories can import from which other ones. But, all of this is too complex for my needs, so for now, we'll stick with the defaults. Now, from here, we could run the Follow fix command, or we could add the dry run 

flag to see exactly what it's going to do, which is try to address all the fixable issue types. And you can see here that it's going to remove a bunch of exports. But, I actually don't trust Follow to run an automatic fix because it doesn't have much context of my code, what each function does, and how everything works together. So, instead of using the fix flag, I'm going to hook Follow up to my agents, which you can do using the MCP server, or by using the VS Code plugin, which I guess will work with Cursor. But, I'm going to keep things simple and just install the Follow skill, which contains some guardrails, some agent rules, and some 

common pitfalls. So, with the skill installed, I'm going to run Claude Code, and I'm going to give it a prompt of study this project to understand how the code works. Then, run Follow to deal with the duplicated code, making sure removing it doesn't break core functionality. And when you're done, put the changes in a feature branch and run tests to make sure the app works as expected. So, we can see here, it loads the Follow skill, then it runs the Follow dups command, and it gets the format to export JSON, which is a machine-friendly format. And after about 

4 minutes, Claude has finished fixing three files instead of all the files Follow suggested, mainly because the others are test files, which are sometimes supposed to have duplicated code. I also asked it to create a PR, and if we have a look at it, it's added 54 lines of code and removed 43. But, this is because I've asked it to add a Follow configuration file, which is about 20 lines, to ignore all test files in future reports. And of course, we could continue going down this line using Claude Code or any other agent to fix complexity issues or any dead code. 

But, Follow can also review PRs. So, if we take a look at this PR I showed you earlier, running the Follow audit command will check any issues on this branch versus main, so that we can only fix specific issues. And if we wanted to base it off a different branch, we could just use the base flag. But, if we also didn't want to prompt Claude over and over again each time to use Follow, we could run the setup hooks command, which will generate some Claude Code hooks for Follow. Follow can also run as a GitHub action with PR annotations. It supports workspaces. It can export health badges 

and supports baselines, meaning the current issues can be fixed over time, and the CI only picks up new issues, which is great for fixing a big project with lots of issues. It basically has a lot of features, but all of them are pretty much static code analysis, which means it doesn't actually execute your functions. If you wanted to something that did that, then Follow supports something called runtime intelligence to tell you what functions are being triggered when your app in production encounters real traffic. It does this by using V8 runtime coverage and merges the 

results to an existing health report through a sidecar that can run locally or can be deployed anywhere you want. But, this of course is a paid feature, which kind of makes sense. Overall, Follow is a great tool that I'm going to be using a lot more of, even though I think it has a lot of features, and it only supports the JavaScript tech stack. Although other languages do have their own tools, I'm not sure it combines everything together as well as Follow does, and I think its creator, Bart, has done a good job of creating this tool, which actually uses Olexy for parsing, 

semantic analysis, and module resolution before the graph-based analysis begins. So, basically, it's never going to leave JavaScript, and I'm sure this makes Evan You very happy, not the JavaScript bit, but the Olexy bit, since it's a tool that he's funding with Void Zero. Speaking of Evan You, if you want to hear us grill him about Void Zero, the plus if React server components was a good idea, and everything in between, then check out this video, which is an hour-long podcast, and I think it's one of my favorite assets that we've done. 

<p>
 <span data-rw-start="0" data-rw-transcript-version="2">
 This is Fallow, a code-based
 </span>
 <span data-rw-start="1.72" data-rw-transcript-version="2">
 intelligence tool for TypeScript and
 </span>
 <span data-rw-start="3.56" data-rw-transcript-version="2">
 JavaScript that analyzes your entire
 </span>
 <span data-rw-start="5.6" data-rw-transcript-version="2">
 code base for dead code, duplication,
 </span>
 <span data-rw-start="8.08" data-rw-transcript-version="2">
 unnecessary complexity, and much more,
 </span>
 <span data-rw-start="10.44" data-rw-transcript-version="2">
 meaning there's no need to use a
 </span>
 <span data-rw-start="11.84" data-rw-transcript-version="2">
 combination of npm, JSCPD, and ESLint
 </span>
 <span data-rw-start="15" data-rw-transcript-version="2">
 just to stop your agents from shipping
 </span>
 <span data-rw-start="16.64" data-rw-transcript-version="2">
 bad code. It's built in Rust and
 </span>
 <span data-rw-start="18.72" data-rw-transcript-version="2">
 supports over 90 plugins, meaning it
 </span>
 <span data-rw-start="20.6" data-rw-transcript-version="2">
 will work out of the box with most
 </span>
 <span data-rw-start="22.32" data-rw-transcript-version="2">
 frameworks and popular packages. But,
 </span>
 <span data-rw-start="23.92" data-rw-transcript-version="2">
 the fact that it only supports
 </span>
 <span data-rw-start="25.2" data-rw-transcript-version="2">
 JavaScript and TypeScript makes it less
 </span>
 <span data-rw-start="27.36" data-rw-transcript-version="2">
 appealing for AI-assisted coders. Hit
 </span>
 <span data-rw-start="29.56" data-rw-transcript-version="2">
 subscribe, and let's find out.
 </span>
</p>
<p>
 <span data-rw-start="34.36" data-rw-transcript-version="2">
 So, here is a project that I'm working
 </span>
 <span data-rw-start="36.08" data-rw-transcript-version="2">
 on that adds a cinematic film look to
 </span>
 <span data-rw-start="38.36" data-rw-transcript-version="2">
 videos and images. It's mostly been
 </span>
 <span data-rw-start="40.48" data-rw-transcript-version="2">
 built with Claude Code, so it will have
 </span>
 <span data-rw-start="42.64" data-rw-transcript-version="2">
 some level of AI support. There's also a PR
 </span>
 <span data-rw-start="44.92" data-rw-transcript-version="2">
 here for a new feature in that project,
 </span>
 <span data-rw-start="47" data-rw-transcript-version="2">
 which I'll talk about later, as long as
 </span>
 <span data-rw-start="49.08" data-rw-transcript-version="2">
 GitHub doesn't make it disappear by
 </span>
 <span data-rw-start="50.68" data-rw-transcript-version="2">
 accident. So, to get started, I'm going
 </span>
 <span data-rw-start="52.36" data-rw-transcript-version="2">
 To run Follow with the summary flag
 </span>
 <span data-rw-start="54.28" data-rw-transcript-version="2">
 using bun x, which means I don't have to
 </span>
 <span data-rw-start="56.2" data-rw-transcript-version="2">
 install it. And this gives a snapshot of
 </span>
 <span data-rw-start="58.28" data-rw-transcript-version="2">
 my project, showing the dead code
 </span>
 <span data-rw-start="59.8" data-rw-transcript-version="2">
 summary, duplication, and a complexity
 </span>
 <span data-rw-start="61.88" data-rw-transcript-version="2">
 health summary. And if we check the Git
 </span>
 <span data-rw-start="63.16" data-rw-transcript-version="2">
 status, it adds a new .follow directory
 </span>
 <span data-rw-start="66.04" data-rw-transcript-version="2">
 that contains the cache, so that means
 </span>
 <span data-rw-start="67.6" data-rw-transcript-version="2">
 subsequent runs of this command will be
 </span>
 <span data-rw-start="69.4" data-rw-transcript-version="2">
 faster and contain snapshot and any
 </span>
 <span data-rw-start="71.6" data-rw-transcript-version="2">
 plugin information. Now, you may have
 </span>
 <span data-rw-start="73.04" data-rw-transcript-version="2">
 noticed it here that the health is 41
 </span>
 <span data-rw-start="75.48" data-rw-transcript-version="2">
 above the threshold. Now, what does that
 </span>
 <span data-rw-start="77.64" data-rw-transcript-version="2">
 mean? Well, the Follow health score is
 </span>
 <span data-rw-start="79.16" data-rw-transcript-version="2">
 calculated by working out the cyclomatic
 </span>
 <span data-rw-start="81.68" data-rw-transcript-version="2">
 complexity and the cognitive complexity.
 </span>
</p>
<p>
 <span data-rw-start="84.56" data-rw-transcript-version="2">
 It uses some formulas to calculate
 </span>
 <span data-rw-start="86.32" data-rw-transcript-version="2">
 the complexity density, and down here,
 </span>
 <span data-rw-start="88.48" data-rw-transcript-version="2">
 all this is used to figure out the
 </span>
 <span data-rw-start="90.28" data-rw-transcript-version="2">
 maintainability index, which is the
 </span>
 <span data-rw-start="92.12" data-rw-transcript-version="2">
 score that we see over here. So, based
 </span>
 <span data-rw-start="93.92" data-rw-transcript-version="2">
 on this score, it's detected that 41 of
 </span>
 <span data-rw-start="96.88" data-rw-transcript-version="2">
 my files need to be refactored. From
 </span>
 <span data-rw-start="99.12" data-rw-transcript-version="2">
 here, we can run any of these commands
 </span>
 <span data-rw-start="100.68" data-rw-transcript-version="2">
 to get a more detailed report about a
 </span>
 <span data-rw-start="102.48" data-rw-transcript-version="2">
 Specific area. So, if I wanted to focus
 </span>
 <span data-rw-start="104.32" data-rw-transcript-version="2">
 on health, we could run this command,
 </span>
 <span data-rw-start="106.04" data-rw-transcript-version="2">
 and after a while, it lists all the
 </span>
 <span data-rw-start="107.56" data-rw-transcript-version="2">
 files that have different health issues.
 </span>
</p>
<p>
 <span data-rw-start="109.72" data-rw-transcript-version="2">
 Note, if you want to know what CRAP
 </span>
 <span data-rw-start="111.28" data-rw-transcript-version="2">
 stands for, this is an abbreviation for
 </span>
 <span data-rw-start="113.52" data-rw-transcript-version="2">
 change risk antipatterns, which you can
 </span>
 <span data-rw-start="115.6" data-rw-transcript-version="2">
 learn all about in the documentation.
 </span>
 <span data-rw-start="117.2" data-rw-transcript-version="2">
 But, this level of detail is very easy
 </span>
 <span data-rw-start="118.68" data-rw-transcript-version="2">
 for an agent to follow and know what to
 </span>
 <span data-rw-start="120.08" data-rw-transcript-version="2">
 fix. In fact, the duplication is a lot
 </span>
 <span data-rw-start="122.28" data-rw-transcript-version="2">
 easier to follow since it gives the
 </span>
 <span data-rw-start="123.92" data-rw-transcript-version="2">
 exact file and the specific line
 </span>
 <span data-rw-start="125.88" data-rw-transcript-version="2">
 numbers. So, we'll stick with that for
 </span>
 <span data-rw-start="127.2" data-rw-transcript-version="2">
 now. And if we wanted to, we could add a
 </span>
 <span data-rw-start="129" data-rw-transcript-version="2">
 Follow configuration file to give Follow
 </span>
 <span data-rw-start="131.16" data-rw-transcript-version="2">
 information about certain patterns or
 </span>
 <span data-rw-start="132.72" data-rw-transcript-version="2">
 dependencies you want to ignore, as well
 </span>
 <span data-rw-start="134.68" data-rw-transcript-version="2">
 as setting some custom duplication
 </span>
 <span data-rw-start="135.96" data-rw-transcript-version="2">
 settings, health setting, and adding
 </span>
 <span data-rw-start="138.16" data-rw-transcript-version="2">
 boundaries, which is a very cool way of
 </span>
 <span data-rw-start="140.24" data-rw-transcript-version="2">
 declaring which directories can import
 </span>
 <span data-rw-start="142.4" data-rw-transcript-version="2">
 from which other ones. But, all of this
 </span>
</p>
<p>
 <span data-rw-start="144.28" data-rw-transcript-version="2">
 is too complex for my needs, so for now,
 </span>
 <span data-rw-start="145.92" data-rw-transcript-version="2">
 we'll stick with the defaults. Now, from
 </span>
 <span data-rw-start="147.28" data-rw-transcript-version="2">
 Here, we could run the Follow fix
 </span>
 <span data-rw-start="148.76" data-rw-transcript-version="2">
 command, or we could add the dry run
 </span>
 <span data-rw-start="150.68" data-rw-transcript-version="2">
 flag to see exactly what it's going to
 </span>
 <span data-rw-start="152.36" data-rw-transcript-version="2">
 do, which is try to address all the
 </span>
 <span data-rw-start="154.28" data-rw-transcript-version="2">
 fixable issue types. And you can see
 </span>
 <span data-rw-start="156" data-rw-transcript-version="2">
 here that it's going to remove a bunch
 </span>
 <span data-rw-start="157.6" data-rw-transcript-version="2">
 of exports. But, I actually don't trust
 </span>
 <span data-rw-start="159.48" data-rw-transcript-version="2">
 Follow to run an automatic fix because
 </span>
 <span data-rw-start="161.52" data-rw-transcript-version="2">
 it doesn't have much context of my code,
 </span>
 <span data-rw-start="163.48" data-rw-transcript-version="2">
 what each function does, and how
 </span>
 <span data-rw-start="165.04" data-rw-transcript-version="2">
 everything works together. So, instead
 </span>
 <span data-rw-start="166.72" data-rw-transcript-version="2">
 of using the fix flag, I'm going to hook
 </span>
 <span data-rw-start="168.64" data-rw-transcript-version="2">
 Follow up to my agents, which you can do
 </span>
 <span data-rw-start="170.56" data-rw-transcript-version="2">
 using the MCP server, or by using the VS
 </span>
 <span data-rw-start="173.24" data-rw-transcript-version="2">
 Code plugin, which I guess will work
 </span>
</p>
<p>
 <span data-rw-start="175" data-rw-transcript-version="2">
 with Cursor. But, I'm going to keep
 </span>
 <span data-rw-start="176.36" data-rw-transcript-version="2">
 things simple and just install the
 </span>
 <span data-rw-start="177.88" data-rw-transcript-version="2">
 Follow skill, which contains some
 </span>
 <span data-rw-start="179.96" data-rw-transcript-version="2">
 guardrails, some agent rules, and some
 </span>
 <span data-rw-start="182.52" data-rw-transcript-version="2">
 common pitfalls. So, with the skill
 </span>
 <span data-rw-start="184.16" data-rw-transcript-version="2">
 installed, I'm going to run Claude Code,
 </span>
 <span data-rw-start="186" data-rw-transcript-version="2">
 and I'm going to give it a prompt of
 </span>
 <span data-rw-start="187.68" data-rw-transcript-version="2">
 study this project to understand how the
 </span>
 <span data-rw-start="189.56" data-rw-transcript-version="2">
 code works. Then, run Follow to deal
 </span>
 <span data-rw-start="192.36" data-rw-transcript-version="2">
 with the duplicated code, making sure
 </span>
 <span data-rw-start="194.28" data-rw-transcript-version="2">
 Removing it doesn't break core
 </span>
 <span data-rw-start="195.84" data-rw-transcript-version="2">
 functionality. And when you're done, put
 </span>
 <span data-rw-start="197.96" data-rw-transcript-version="2">
 the changes in a feature branch and run
 </span>
 <span data-rw-start="199.64" data-rw-transcript-version="2">
 tests to make sure the app works as
 </span>
 <span data-rw-start="201.56" data-rw-transcript-version="2">
 expected. So, we can see here, it loads
 </span>
 <span data-rw-start="203.32" data-rw-transcript-version="2">
 the Follow skill, then it runs the
 </span>
 <span data-rw-start="204.92" data-rw-transcript-version="2">
 Follow dups command, and it gets the
 </span>
 <span data-rw-start="206.52" data-rw-transcript-version="2">
 format to export JSON, which is a
 </span>
</p>
<p>
 <span data-rw-start="208.2" data-rw-transcript-version="2">
 machine-friendly format. And after about
 </span>
 <span data-rw-start="210.08" data-rw-transcript-version="2">
 4 minutes, Claude has finished fixing
 </span>
 <span data-rw-start="211.92" data-rw-transcript-version="2">
 three files instead of all the files
 </span>
 <span data-rw-start="213.64" data-rw-transcript-version="2">
 Follow suggested, mainly because the
 </span>
 <span data-rw-start="215.64" data-rw-transcript-version="2">
 others are test files, which are
 </span>
 <span data-rw-start="217.56" data-rw-transcript-version="2">
 sometimes supposed to have duplicated
 </span>
 <span data-rw-start="219.24" data-rw-transcript-version="2">
 code. I also asked it to create a PR,
 </span>
 <span data-rw-start="221.68" data-rw-transcript-version="2">
 and if we have a look at it, it's added
 </span>
 <span data-rw-start="223.4" data-rw-transcript-version="2">
 54 lines of code and removed 43. But,
 </span>
 <span data-rw-start="226.28" data-rw-transcript-version="2">
 this is because I've asked it to add a
 </span>
 <span data-rw-start="228.2" data-rw-transcript-version="2">
 Follow configuration file, which is
 </span>
 <span data-rw-start="230.32" data-rw-transcript-version="2">
 about 20 lines, to ignore all test files
 </span>
 <span data-rw-start="232.92" data-rw-transcript-version="2">
 in future reports. And of course, we
 </span>
 <span data-rw-start="234.6" data-rw-transcript-version="2">
 could continue going down this line
 </span>
 <span data-rw-start="236.08" data-rw-transcript-version="2">
 using Claude Code or any other agent to
 </span>
 <span data-rw-start="238.48" data-rw-transcript-version="2">
 fix complexity issues or any dead code.
 </span>
</p>
<p>
 <span data-rw-start="240.8" data-rw-transcript-version="2">
 But, Follow can also review PRs. So, if
 </span>
 <span data-rw-start="243" data-rw-transcript-version="2">
 We take a look at this PR I showed you
 </span>
 <span data-rw-start="244.72" data-rw-transcript-version="2">
 earlier, running the Follow audit
 </span>
 <span data-rw-start="246.28" data-rw-transcript-version="2">
 command will check any issues on this
 </span>
 <span data-rw-start="248.36" data-rw-transcript-version="2">
 branch versus main, so that we can only
 </span>
 <span data-rw-start="250.6" data-rw-transcript-version="2">
 fix specific issues. And if we wanted to
 </span>
 <span data-rw-start="252.92" data-rw-transcript-version="2">
 base it off a different branch, we could
 </span>
 <span data-rw-start="254.84" data-rw-transcript-version="2">
 just use the base flag. But, if we also
 </span>
 <span data-rw-start="257.079" data-rw-transcript-version="2">
 didn't want to prompt Claude over and
 </span>
 <span data-rw-start="258.76" data-rw-transcript-version="2">
 over again each time to use Follow, we
 </span>
 <span data-rw-start="260.68" data-rw-transcript-version="2">
 could run the setup hooks command, which
 </span>
 <span data-rw-start="262.6" data-rw-transcript-version="2">
 will generate some Claude Code hooks for
 </span>
 <span data-rw-start="264.28" data-rw-transcript-version="2">
 Follow. Follow can also run as a GitHub
 </span>
 <span data-rw-start="266.48" data-rw-transcript-version="2">
 action with PR annotations. It supports
 </span>
 <span data-rw-start="269.24" data-rw-transcript-version="2">
 workspaces. It can export health badges
 </span>
 <span data-rw-start="271.52" data-rw-transcript-version="2">
 and supports baselines, meaning the
 </span>
 <span data-rw-start="273.4" data-rw-transcript-version="2">
 current issues can be fixed over time,
 </span>
</p>
<p>
 <span data-rw-start="275.72" data-rw-transcript-version="2">
 and the CI only picks up new issues,
 </span>
 <span data-rw-start="278.24" data-rw-transcript-version="2">
 which is great for fixing a big project
 </span>
 <span data-rw-start="280.12" data-rw-transcript-version="2">
 with lots of issues. It basically has a
 </span>
 <span data-rw-start="282.08" data-rw-transcript-version="2">
 lot of features, but all of them are
 </span>
 <span data-rw-start="284.52" data-rw-transcript-version="2">
 pretty much static code analysis, which
 </span>
 <span data-rw-start="286.68" data-rw-transcript-version="2">
 means it doesn’t actually execute your
 </span>
 <span data-rw-start="288.4" data-rw-transcript-version="2">
 functions. If you wanted to something
 </span>
 <span data-rw-start="290.08" data-rw-transcript-version="2">
 that did that, then Follow supports
 </span>
 <span data-rw-start="292.24" data-rw-transcript-version="2">
 something called runtime intelligence to
 </span>
 <span data-rw-start="294.48" data-rw-transcript-version="2">
 Tell you what functions are being
 </span>
 <span data-rw-start="295.84" data-rw-transcript-version="2">
 triggered when your app in production
 </span>
 <span data-rw-start="297.64" data-rw-transcript-version="2">
 encounters real traffic. It does this by
 </span>
 <span data-rw-start="299.88" data-rw-transcript-version="2">
 using V8 runtime coverage and merges the
 </span>
 <span data-rw-start="302.2" data-rw-transcript-version="2">
 results to an existing health report
 </span>
 <span data-rw-start="304.12" data-rw-transcript-version="2">
 through a sidecar that can run locally
 </span>
 <span data-rw-start="306.2" data-rw-transcript-version="2">
 or can be deployed anywhere you want.
 </span>
</p>
<p>
 <span data-rw-start="308.08" data-rw-transcript-version="2">
 But, this of course is a paid feature,
 </span>
 <span data-rw-start="309.84" data-rw-transcript-version="2">
 which kind of makes sense. Overall,
 </span>
 <span data-rw-start="311.6" data-rw-transcript-version="2">
 Follow is a great tool that I'm going to
 </span>
 <span data-rw-start="313.48" data-rw-transcript-version="2">
 be using a lot more of, even though I
 </span>
 <span data-rw-start="315.44" data-rw-transcript-version="2">
 think it has a lot of features, and it
 </span>
 <span data-rw-start="317.44" data-rw-transcript-version="2">
 only supports the JavaScript tech stack.
 </span>
 <span data-rw-start="319.56" data-rw-transcript-version="2">
 Although other languages do have their
 </span>
 <span data-rw-start="321.4" data-rw-transcript-version="2">
 own tools, I'm not sure it combines
 </span>
 <span data-rw-start="323.24" data-rw-transcript-version="2">
 everything together as well as Follow
 </span>
 <span data-rw-start="324.92" data-rw-transcript-version="2">
 does, and I think its creator, Bart, has
 </span>
 <span data-rw-start="327.2" data-rw-transcript-version="2">
 done a good job of creating this tool,
 </span>
 <span data-rw-start="329.12" data-rw-transcript-version="2">
 which actually uses Olexy for parsing,
 </span>
 <span data-rw-start="331.52" data-rw-transcript-version="2">
 semantic analysis, and module resolution
 </span>
 <span data-rw-start="333.92" data-rw-transcript-version="2">
 before the graph-based analysis begins.
 </span>
 <span data-rw-start="336.16" data-rw-transcript-version="2">
 So, basically, it's never going to leave
 </span>
 <span data-rw-start="338.04" data-rw-transcript-version="2">
 JavaScript, and I'm sure this makes Evan
 </span>
 <span data-rw-start="340.16" data-rw-transcript-version="2">
 very happy, not the JavaScript bit,
 </span>
 <span data-rw-start="342.36" data-rw-transcript-version="2">
 but the Olexy bit, since it's a tool
 </span>
 <span data-rw-start="344.84" data-rw-transcript-version="2">
 That he's funding with Void Zero.
 </span>
</p>
<p>
 <span data-rw-start="346.92" data-rw-transcript-version="2">
 Speaking of Evan You, if you want to
 </span>
 <span data-rw-start="348.64" data-rw-transcript-version="2">
 hear us grill him about Void Zero, the
 </span>
 <span data-rw-start="351.12" data-rw-transcript-version="2">
 plus if React server components was a
 </span>
 <span data-rw-start="353.32" data-rw-transcript-version="2">
 good idea, and everything in between,
 </span>
 <span data-rw-start="355.52" data-rw-transcript-version="2">
 then check out this video, which is an
 </span>
 <span data-rw-start="357.56" data-rw-transcript-version="2">
 hour-long podcast, and I think it's one
 </span>
 <span data-rw-start="359.84" data-rw-transcript-version="2">
 of my favorite assets that we've done.
 </span>
</p>