# The Future of MCP — David Soria Parra, Anthropic

![rw-book-cover](https://i.ytimg.com/vi/v3Fr2JR47KA/sddefault.jpg?v=69e40e55)

## Metadata
- Author: [[AI Engineer]]
- Full Title: The Future of MCP — David Soria Parra, Anthropic
- Category: #articles
- Summary: MCP is a powerful protocol that helps agents connect and work with different tools and interfaces smoothly. In 2026, agents will use MCP along with other methods to handle complex tasks for knowledge workers. The community is open and growing, aiming to improve MCP for better connectivity and smarter agents.
- URL: https://m.youtube.com/watch?v=v3Fr2JR47KA&t=467s

## Full Document
[music]>> Well,welcome.Let's get started.This is an MCP application.That's an agent shipping its owninterface not through like a plugin, notthrough an SDK,not rendered on the fly by the model onthe client side, or hardcoded into theproduct. That is something that isserved over an MCP server, and you cantake the server, put it into the cloud, youcan put it into ChatGPT, you can put itinto VS Code Cursor, and it will justwork.

And that, I think, is kind of cool because fordoing that, you need something that alot of things that we're want in theecosystem do not offer. You needsemantics, you need to have both sides,client and the server, to understandwhat each side is talking about, to understand.

How you render this, understand thatthere's a UI coming.And for that, you need a protocol.And the best part about this,an MCP server doesn't just ship an app,or can ship an app, it can also shiptools with it, and so you can interactwith it with the application as a human,and you can have the model interact withit through tools, which is I think avery unique thing that I think we havenot explored much.Just yet.

Okay.But, let's quickly rewind a little bitfrom this, what I think is a really coolglimpse into the future of MCP into overa year ago, 18 months, an eternity in AIlife cycle, uh, all of this did notexist. There was just a little specdocument, a few SDKs, uh, mostly writtenby Claude, local-only with little morethan just tools. And in that last 18 or12 months, you guys have been absolutelycrazy building stuff.

Servers, building an crazy ecosystemaround this, and we on our side havebeen busy, busy taking this local onlything, added remote capabilities, addedcentralized authorization, added newprimitives like elicitation and tasks,and last but not least, added newexperimental features to the protocollike the MCP applications that you'vejust seen.

And in the meantime,we have reached, I think, a really coolmilestone because, again, all of youhave been absolutely crazy building,building, and building. Of course,luckily with the help of a bunch ofagents. Um,We're now like at 110 millionmonthly downloads. And that's just, ofcourse, not us using it in our clientsand servers. That's like OpenAI's agentSDK, that's Google's SDK, that'sLangChain, thousands of frameworks andtools that you might have never everheard of, pulling it as aAs a dependency, which means there's onecommon standard that all of us have atour disposal to speak to each other. Um,just a bit for context, uh, React, one ofthe most successful, um,open source projects, probably of thelast decades, took roughly double theamount of time to reach that downloadvolume.

And in the meantime, of course, you allhave been building really, really coolservers from, like, little toy projects ofWhatsApp servers and Blender servers, uh,to building SaaS integrations likeLinear, Slack, and Notion that arereally powering what everyone does everyday when they use MCPs. But mostimportantly, the vast majority of MCPserver, most of all of us have built, arebehind closed doors, uh, connectingcompany systems to agents, uh, and AIapplications.

But I still think this is just theabsolute beginning of where we are.

Because I think 2025 was all aboutExploring, and 2026 is all about puttingthese agents into production. Because ifyou really think about it, in my mind,2024, we just built a bunch of likedemos and showed some cool stuff topeople, and there was a little bit of abuzz there. 2025 was really all aboutcoding agents. But coding agent, if youreally think about it, are the mostideal scenario for an agent. It's local,it's verifiable, you can call acompiler, like you have a developer whocan fix if it goes wrong in frontof the computer, uh, andyou can display a UI interface, and theuser's quite happy.

But I think now, with the capabilities ofthe model increasing, we're going into anew era, which I think this year will bewe will see the start, where we're notjust doing coding agents, we're going tohave general agents that will do realknowledge worker stuff, like things afinancial analysis analyst wants to do,uh, a marketing person wants to do.

They need one thing in particular. Theydon't need a local agent that calls acompiler. What they need is somethingthat could connect to like five SASapplications and a shared drive,because the most important part for themfor an agent is connectivity.And in my mind, connectivity is not onething. If one if someone tells youthere's one solution to all yourconnectivity problem, be it computeruse, be it CLIs, be it MCP,they are probably pretty wrong becausethe right because the right thing, ofcourse, is that it always means itdepends, and there's a real a bigconnectivity stack, and there's a righttool for the right job. And in my mind,there are three major things that youwant to consider building an agent in2026. It's skills, MCP, and of course,like CLI or computer use depending onyour use case. And they have three verydistinct things that they can do inthree different things you want toConsider when you build your agent.

Number one, skills, of course, is justlike domain knowledge, it's just likecapture-specific capabilities put into avery simple file, and it's mostlyreusable. There are some minordifferences between the differentplatform.Of course, CLI is very popular when localcoding agents. It's an amazing tool toget started, to have somethingthat you can pose in a bash, that youthat automatically discovers where themodel can automatically discover whatthe CLI is capable of. And mostimportantly, if you have things that arelike CLIs, like GitHub, Git, and otherthings that are in pre-training, CLI isan amazing solution for yourconnectivity part, and they'reparticularly good when you have a localagent where you can assume a sandbox,where you can assume a code executionenvironment.

But if you don't have this, if you needRich semantics, when you need a UI thatcan display long-running tasks, when youcan have, when you need things likeresources, when you need to buildsomething that is fully decoupled andneeds platform independence, or youdon't have a sandbox, when you needthings like authorization, governance,policies, or, short to say, boring but important enterprise stuff,or if you want to have experiments likeMCP applications or what comes soon,skills over MCP, then I think MCP isjust like additional connective tissuethat is just yet another tool in thetoolbox for you to build an amazingagent.

And so, this is all to say that I thinkin 2026, we're going to start buildingagents that use all of it. They don'tuse one thing, they use all of it, andthey use them quite seamlessly together.But I don't think we're quite there justyet.Because we need to build a lot of stuff.

Partially, um, becauseour agents kind of still suck.Um, and partially because I think we justhaven't talked enough about, like, some ofthe techniques you can douh, to really put this connective tissuetogether.The number one thing that we need to goand start building is on the clientside, on the agent harness side,on the things that power the connectiveparts, that be it a cloud code, uh, be ita pie, be it whatever application you'regoing to build.And the number one thing we're going todo there, and what we all have to do,and something I want to really getacross today, is that we need to go andstart building something calledprogressive discovery.

Most people when they think about, like,"Oh,I MCP," they can't think about, like,context load. But if you really considerwhat a protocol does, the protocol justputs information across the wire, butthe client is responsible for dealingwith that information. And whateverybody so far has done because we'rein this very early experimentationphase, is to simply put all the toolsinto the context window, and then bequite surprised that maybe the contextwindow gets large. Umbut what you can do instead, and whatyou should do instead, you should startusing this progressive discoverypattern,which is to say, use something like toolsearch to defer the loading of thetools, and start loading the tools whenthe model needs it. And we have this inthe Anthropic API, and people can usethis uh on on competitors' APIs as well.

But also, you can just build this inyourself where you just download thetool directly, and the moment you givethe model a tool loadingtool, basically, and the model goeslike, "Ah, maybe I need a tool now. LetLet's look up what tools I need.

And then you load them on demand.And here, in this example, what you'reseeing is on the left side is uh ClaudeCode before we added this to ClaudeCode, and then after it, uhto Claude Code. So you see a massivereductionin tooluh use, uh tool context usage.

The second part of that is is somethingcalled programmatic tool calling, orwhat other people usually refer to, umto code mode.Um, this is the idea that one thing thatyou really want to do is you want tocompose things together. You don't wantthe model to go call a tool, take theresult, then go and talk, call anothertool,take the result, call another tool.

Because what you're effectively doing isyou're letting the model orchestratethings together, and in thatorchestration, you're using inference.

You're; it's; latency sensitive, andall of it stuff could be done way moreeffective if you would instead writea script.Um,and in fact, that's actually what youconstantly do, and what you constantlysee, things like hard code do, when itwrites the bash command. But you can, ofcourse, do this with everything, and youcan do this with MCP, and you should dothis with MCP. So, what does this mean?

So, what you want, instead of having onetool at another, is to give themodel a reusable tool, provide, like, aexecution environment, like a V8isolate, or a Monty, or something likethat, or a Lua interpreter, and justhave the model write the code for you,and the model just executes that code,and then composes them together. Andthere's a neat little feature in MCPcalled structured output that tells youwhat the return value of the output willbe, and the model can use this.

Information to figure out typeinformation, which then means it canreally nicely compose these thingstogether. And in this example here,instead of doing two different calls,you do one call, and you can filter thatthe model will automaticallyremove things from a JSON and justcontinue.Of course, if you don't have uhstructured output, you can always justask the model to give you structuredoutputumuh, by just extracting it and saying,"Hey, call us cheap model and say, 'Iwant this expected type, give it back tome.'And bam, you have a type, themodel can compose things together, and Ithink this is something we're just notdoing enough yet, and this is I thinksomething where we can improve our agentharnesses.And then last but not least, of course,you can just compile and compose theseThings together with executables, likewith CLIs, with other components, withAPIs as well.

Um, next, what we need to do besides theclient work, which is progressivediscovery andum, programmatic tool calling, we need togo and start building properly foragents. And that means we all need tostop taking REST APIs and put themone-to-oneintouh, an MCP server. Every time I seesomeone building another REST to MCPserver, a conversion tool, I think it'sa bitcringe because I think it's just, it justresults in horrible things.

Um, and what you should do instead, youshould design for an agent. Orbasically, you can start designing foryou as a human, how you would want tointeract with this, because that'sactually a very, very good start for anagent.

Together, you should reach, of course,for programmatic tool calling, and youcan do this on the client side, as Isaid before, but you can also do this onthe server side. The CloudflareMCP server and others like that aregreat examples of how you can have, insteadof providing tools, provide an executionenvironment to the model and then justhave them orchestrate things together,which again cuts on token usages,cuts on latency, and is way morepowerful in its composition. And thenlast but not least, you should start andwe should start as server authors to usethis rich semantics that MCP offers over

alternatives. This means shipping MCPapplications, it means shippingskills over MCP, it meansum, using things like task and otheraspects that the protocol offers thatwe're currently slightly underused, orthings like elicitations.Things that only MCP can do for you.And of course,That's all the work you all need to do,and maybe some of our product peopleneed to do. We also need to do a lot ofwork on MCP itself. And there are a fewthings down the line that we're going togo and have to go and solve.

The number one thing is we need toimprove the core. There are a few thingsthat, as we have developed the protocolover the last year, are just not ina good shape. Number one is that thecurrent streamable HTTP is very hard toscale if you're a large hyperscaler.

>> [snorts]>> And so, we have a proposal from ourfriends at Google,who are working on something called astateless transport protocol, which makesit significantly easier to just treatMCP servers likeyou know, another stateless, uh, restserver or something like that, and we areused to know how to deploy to like cloudruns or Kubernetes and so on. So, that'scoming down in June and hopefully lining.

In the SDKs very soon.In addition, we need to improve ourasynchronous task primitive, whichbasically is a very fancy way to say wejust want to have agent-to-agentcommunication. We have a veryexperimental version of the protocolthat very few clients support, so we'regoing to start building more clients outlike that, and most importantly, we areimproving some of the little semanticsthat we need to do. We're going to shipa TypeScript version SDK version two andPython SDK version two based on a lot ofthe lessons learned over the last year.

There's a there’s aSDK called fast MCP.Who's using fast MCP? Yeah. It's justway better than Python SDK thatwe're shipping, right? And that's on mebecause I wrote the Python SDK.

Um, and so, I have a bunch of peoplewho are way better Python developersthan me helping me write it better. Um, thesecond part is we need to startIntegrating everywhere. We're going toship, particularly for enterprises,something called cross-app access. It'sa new thing that we're working closelytogether with identity providers, whichjust allows you. It's a very fancy way tosay,once you log in once with your localcompany identity provider, be it aGoogle, or be it an Okta, you will be ableto just use MCP servers without havingto re-login. So, it's a bit moresmooth. In addition, we're goingto add something called a serverdiscovery, byspecifying how you can discoverservers on well-known URLs,automatically. So, crawlers, browsers,um,agents can just go to a website and say,"Oh, I'm instead of just parsing thewebsite, is there also an MCP server Ican use?" And we will be able toautomatically discover this.

This is a really cool thing that willCome down also in June when we launchthe next specificationand will be supported there.

And then last but not least, we'restarting to use our extension mechanismsin MCP, which means that some clientswill support this, like for example, MCPapplications will only be supported byweb-based interfaces, because if you'rea CLI, you just have a hard timerendering HTML, right? Um, and we will domore of these extensions. One of themost exciting extensions that I think isis cool, we're just going to ship skillsover MCP, because it's very obvious thatif you have a large MCP server with tonsand tons of tools, you just want to shipthe main knowledge with it and say, "Oh,this is how you're supposed to use this.

This is how you're supposed to usethis." And it allows you as a serverauthor to continuously ship updatedskills without having to rely on pluginmechanisms on registries and otherstuff.

So, that's coming down.Um, there's a lot of experimentationfrom people already in that space. Youcan already do some of that today if youjust give the model a load skills tool.Like, there you can, you can buildprimitives or versions of this todaywithout having to rely on the semantics,but, of course, we're going to define thesemantics.

Okay. So, that's for me a long-windedway to think, to say that I think MCP isactually in a really good shape, and Ithink in this year, we're going to pushuh,agents to full connectivity.Um, MCP will continue to play a major,major, major role. And we want, ofcourse, your feedback. We are very opencommunity. We just have created afoundation. We're mostly running as anopen-source community with a Discord,with issues. Um, just come to us and tellus where we are wrong, what areWe’re getting right,uh, so that we canimprove this on a continuous basis.

So, 2026, I think is all aboutconnectivity, and the best agents useevery available method. Like they willuse computer use, they will use CLIs,they will use MCPs, and they will usewill use skills.

Because they want to have a wide varietyof things they can do, and then they canship cool stuff like this,uh,which isuh,one of the product features we shippedrecently.Uh, under the hood, it's nothing but anMCP applicationuh, that renders stuff, right?

Cool.So, we can now look at,uh, the modelwriting graphs.Anyway,thank you.

>> [music]
