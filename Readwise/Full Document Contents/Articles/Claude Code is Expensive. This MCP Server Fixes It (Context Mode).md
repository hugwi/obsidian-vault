# Claude Code is Expensive. This MCP Server Fixes It (Context Mode)

![rw-book-cover](https://i.ytimg.com/vi/QUHrntlfPo4/sddefault.jpg)

## Metadata
- Author: [[Better Stack]]
- Full Title: Claude Code is Expensive. This MCP Server Fixes It (Context Mode)
- Category: #articles
- Summary: Claude code uses a lot of context space, making it expensive and causing the AI to forget important information. Context mode saves space by indexing data in a local database, reducing token use by up to 99%. This helps keep longer sessions, saves money, and lets Claude work smarter on big projects.
- URL: https://www.youtube.com/watch?v=QUHrntlfPo4

## Full Document
If you've been coding in Claude code,you've probably experienced context load. The problem is that every MCP toolcall in Claude code is ridiculouslyexpensive because every one of thesecalls dumps its full output directlyinto the model's 200k context window.And the more tools you have under thetool belt, the faster your contextdepletes. Under certain scenarios,you're looking at 30 minutes of activeagent use before your context compacts.

And that's when the AI starts forgettingfiles, tasks, and crucial decisions. Notto mention you're spending a lot ofmoney on those tokens. But, there is anMCP server out there that solves thiscrucial issue. It's called context mode.

In today's video, we'll take a look atwhat context mode does, how it works,and try it out for ourselves with alittle demo. It's going to be a lot offun, so let's dive into it.

To understand why this happens, let'slook at the math. A single PlaywrightSnapshot of a web page is about 56kilobytes. Reading 20 GitHub issues is59 kilobytes. If we do these operationsin the planning phase multiple times ina session, you've probably eaten 70% ofyour window before the agent has evenwritten a single line of code. Contextmode acts as a virtualization layer.

Instead of the AI talking directly toyour OS, it talks to a sandbox. Andinstead of dumping massive outputs,context mode indexes them in a localSQLite database using FTS5, akafull-text search. And the result ispretty significant. For example, that56k Playwright snapshot is reduced to299 bytes, a 99% reduction. Or forexample, this analytics CSV is cruncheddown to 222 bytes, which is a near 100%reduction. But, saving tokens is justone part of the fix. The real utilityhere is the session continuity. We'veall seen how the agents compact historyand suddenly you lose track of the codeit has written 10 minutes earlier, butContext mode uses hooks to monitor everyfile edit, get operation, and sub agenttask. When your conversation compacts,context mode builds a priority tieredsnapshot, usually under 2 kilobytes, andinjects it back in. It's essentially asave checkpoint for your coding session.

So, you could hypothetically extend yoursession time from 30 minutes toapproximately 3 hours. It also tracksdecisions and errors. For example, ifthe AI tried a fix that failed 20minutes ago, it won't repeat thatmistake even after the context resets.

And installing it is verystraightforward. If you're on ClaudeCode, first add the context modemarketplace by running this followingcommand,and then run the plugin install command.

And once you're done, you're good to go.Once you've installed it, it handles theMCP server, the hooks, and the routinginstructions automatically. If you're onGemini CLI or VS Code Copilot, you canRun npm install context mode and add theconfig to your settings. Now, let's seecontext mode in action. I have thissimple Python command here that willcreate a dummy access log file thatcontains a list of a bunch of dummy APIrequests and their status codes, andevery hundredth line is a 500 error log.

Now, we can fire up Claude and ask,"Hey, use context mode to indexaccess.log.I want to find all the 500 errorpatterns and summarize the IP addressesassociated with them." And in thebackground, context mode chunks the5,000 lines of the access.log file intoits own SQLite FTS5 database. And Claudeonly receives confirmation that the fileis indexed, not the raw 5,000 lines ofthe file. And now Claude canintelligently search the index databaseto query the contents instead of parsingthe whole file. And here we can see thefindings returned by Claude, but moreimportantly, let's look at the cost.

Savings. We can do this by runningcontext mode column CTS stats, and wecan check out how much data is saved bycontext mode in this current session.And you can see the results right here.Instead of dumping the entire 20kilobytes into the conversation, contextmode kept about 5 kilobytes of that rawdata in the sandbox. And this result ispretty impressive for a small file. Itspared about 1,200 tokens from enteringthe context window. So, overall, we geta nice 25% reduction running this littletest. That may not sound like much, butkeep in mind that in a standard Claudesession, the data would just sit thereforever getting resent with every singlemessage that you send. And by keeping itin the sandbox, we've already started toextend the life of the session. And thisdemo file is pretty small, but if youdeal with larger files, the savings herecould be massive. If you're running amassive repo research project or

analyzing production-scale logs, that1,200 token saving can easily turn into100,000 tokens. But the goal here isn'tjust about saving money on API costs,though that is a nice bonus. It's alsoabout maintaining the intelligence ofthe model. When you clear the noise outof the context window, you're leavingmore room for actual reasoning. You'regiving Claude the space it needs to be abetter engineer. So, if you're buildingcomplex projects with AI agents, givethis tool a shot and see how much longeryou can extend the sessions before theagent starts compacting and forgettingthings. And if you enjoyed thistechnical breakdown, please let me knowby smashing that like button underneaththe video. And also, don't forget tosubscribe to our channel. This has beenAndres from Better Stack, and I will seeyou in the next videos.

>> [music][music]
