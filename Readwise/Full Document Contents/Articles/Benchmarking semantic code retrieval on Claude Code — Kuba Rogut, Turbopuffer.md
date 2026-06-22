# Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer

![rw-book-cover](https://i.ytimg.com/vi/zKk7sDMGDEQ/sddefault.jpg?v=6a1fdb23)

## Metadata
- Author: [[AI Engineer]]
- Full Title: Benchmarking semantic code retrieval on Claude Code — Kuba Rogut, Turbopuffer
- Category: #articles
- Summary: Cloud code mostly uses simple keyword search rather than semantic code search because it works faster and simpler. However, semantic search can improve code retrieval by understanding meaning, which helps find related files better and reduces wasted file reads. Tests show semantic search boosts precision and user satisfaction, especially when code has good comments or documentation.
- URL: https://www.youtube.com/watch?v=zKk7sDMGDEQ

## Full Document
[music]>> Hi everyone. Welcome to benchmarking semantic search or semantic code retrieval on cloud code.My name is Kuba. I'm here from Turbo Puffer.For those unfamiliar with Turbo Puffer, we are a serverless full text and vector search database built from first principles on top of object storage.We serve some of the fastest growing AI companies in the world, and if you'd like to know more about the talk or any questions about Turbo Puffer or anything, just feel free to find me afterwards.So, let's get started.

So, for those of you who are unaware, cloud code by default, or I mean, yeah, doesn't, doesn't use semantic code search.There's actually a tweet from Boris. Those unfamiliar with Boris, he's actually like the founding father of cloud code.And he talks about how cloud, the early versions of cloud code did actually use semantic search with aLocal vector DB, but they just kind offound agentic search, which is actuallyyou know, grepping through your filesystem, kind of worked better and youknow, seems to work simpler for, forcloud code.

However,one of Turbo Puffer's customers actuallyfun fact, one of our very first customersis Cursor.They do use semantic code search andindex code bases into Turbo Puffer, andyou may think, like, this seems like a lotof work, and it kind of is, but thereason they do this is because they seereal performance gains because of this.

They have this amazing blog post abouttheir semantic search. They also haveone about indexing code bases, which Ihighly recommend as well.But you can see, on the right, the kind ofperformance gains they see with theircomposer model, which is like a 24% increase inrelative improvement in answer accuracy,and I think it's like 12.5% or13% across all models and, you know, Ithis benchmark came up before composertwo, but you can probably imaginethere's some sort of similar performancegains with that new model as well.

And in the bottom right, you can see thisis from the same blog post. They talkabout how in they perform an online ABtest, where they found that addingsemantic, either allowing or disallowingsemantic code search, led to a like a 2.6%increase in code retention in large codebases, and then a 2.2% decrease indissatisfied user requests. And you mayalso think, like, these numbers seem kindof small. Like, what, 2.6%, 2.2%?Well, keep in mind that, you know, out of100 queries, not all queries will everreally need semantic search or like,benefit from it. So, these, they evenstate in the blog post thatthese numbers look small because notevery, you know, you can imagine a verysimple tool call or very simple querywould not really use semantic search.

So,what we think about here at Turbo Pufferand why we kind of really think vectorsearch and why Cursor probably sees thislike real performance gain is, we thinkabout how embeddings are cache compute,and you can also, you know, what is, whatdo you mean cache compute? This soundslike a bunch of baloney you're throwingat me.

You know, if we were like walk throughlike a cloud code trace and like aCursor type trace of kind of the samething, you can imagine that on the leftside this kind of like a, you know,grepping through the file system or whatthey call agentic search. How it justhas like grep through, this is forfinding metadata, filtering, andunderstanding it in your code base.

That's essentially grep through, readthe files, grep through more if itdoesn't find the right things, and again,this is repeated on every session acrossyou know, every agent.

Running in for the same code base, sothat even if you're asking the samequestion or trying to do the same thingmultiple times, you always have to dothis compute again, and you can see likeI mean, in this case, 6,000 tokens isn't alot in one time, but across everysession and every agent, this reallystarts to add up. And if we, you know, onthe right of this is more of a like, likeCursor style or cursor level trace, whereyou have this upfront cost, where youhave to chunk, embed, and index the codebase. But then, you would essentiallyhave this cache of the semantic meaning,so that when an agent wants tounderstand, you know, where or how doesmetadata filtering work,it can simply query, you know, how ismetadata filtered and get the chunks it needs,and kind of the understanding it needs,a lot faster, andwith token savings. And again,this isn't a lot of savings in one time, but we, you know, we'reNot really running one agent anymore.

Like, I'm running like three at one time.So,there's definitely some long-termsavings.So,what we did is, we built a simple CLItool for cloud code. We call it TurboGrep.It's essentially, you can imagine, it'sjust a simple way ofusing a tree splitter library toessentially parse through your codebase,chunk it, embed it using the Voyage codemodel, and then upload it to TurboPuffer.This is just a simplefile system walk through. There is anopen source library for the V1 version,and then soon the V2 version will beopen sourced.Here's a little video of an example, atool call trace for a cloud code whereyou'll see.

It will call the T Puffer tool. Now,it's called T Puffer search password reset token generator.This is in the Django repo.This is one of the repos I was testing it on,and you can see that it gets the contents and then is able tokind of give the full explanation to the user.Andyou know, it's very easy to say like, oh,this works better, but the important thing is obviously benchmarking it.

Let'ssee for real how much betterit works. Cursor has their owninternalcontext bench, and there's this paperthis public paper called context bench,where essentially the benchmark is notreally testing whether or not the codingagent solved or didn't solve a problem.

It tests when it, in the process ofsolving the problem, did it find certainfiles? Did it find certain lines, and itfind certain symbols? Because they, youknow, they kind of have this, this thesis.

That, like,it's also important how youget there, not justthe end goal. The process reallymatters for understanding ifagents are actually looking for the rightfiles. So, essentially, it's a humanlabeled dataset, in order tocomplete this task, the agent shouldhave looked at this file, these fewlines, and these few symbols toactually complete the task well.

And I tested with three conditions.Essentially, raw cloud code out of thebox.Then I tested it with cloud code with amax of 50 line reads at a time, and thenthe same thing with a windowed reads,with the T Puffer search tool. You mayask me, like, why this like 50 line readthing?It's because it became reallynoisy really fast if it just readslong files. It's really hard tounderstand.

And get a difference because it all—ifit just reads a whole like a thousandline file, it doesn't really make a lotof difference in the numbers.So we'll start with the first result ofit. This is precision. Precision isessentially thethe measure of how many files did itread in its total process? How manyof them were actually golden files? Soif there was, if cloud read 10 filesand eight of them were needed, it hits80% precision. You can see the baselineit hit like 65% precision, 33% on lineprecision and 43% on symbol, and it kindof goes up as we add windowed grep andthen windowed grep plus semantic search.Got it to like 87% file precision, forexample.And this is also due to the fact, likecloud code, by default, like it's a reallyexploratory. It loves to read as much asit can, and like try to read everythingfor example, and it kind of shows up inthe 65% precision.

And you know,it's hard to like translate thesenumbers, but a more like English or likehuman version of it is that you know,cloud code one in every three file readsis actually just a completely wastedfile.

And with windowed grep, it was one infive reads was an irrelevant file,and then with semantic search, there’s onlyone in eight files was a, you know, quoteunquote, wasted or irrelevant file,and it kind of like scales up as you kind ofadd these tools.

And you know, obviously, this, this isalready, like, pretty good.Then we have recall. Recall isessentially how many of the needed filesdid it find? So, for example, if therewas 10 files in the task that it shouldhave found, if cloud found five of them,five files in its total trajectory,and only three of them were actually thesegolden files, it would hit 30% recall.By default again,Cloud code actually does win the filerecall, and again, part of this isbecause it just loves to explore everysingle file it can.

Then we have line recall, where it dropsa lot more.This is kind of because it loved to read a lot of files,but also read, to really read, a lot offiles that didn't have a lot ofgolden context lines.

So, you can kind of see that even though it did explore alot, it also kind of explored the wrongthings a lot.And then, with grep and grepplus semantic, or windowed grep, andwindowed grep plus semantic search, kindof have the same recall.

You can kind of see on the right, like, kind of the whathappened with the behavior between thesethree conditions.

And you may be thinking, like, well, youknow, semantic search didn't really likeadd improvements here. Like, what, whatwent wrong? Like, actually, somedecreases. And we can like dig in alittle further into the recall numbers.

For certain tasks. This is across 50tasks by default, but if we break itdown into where semantic search won, you know, quote unquote, won, and where justlike windowed grep won, we see somestark differences between, like, certaintasks performed a lot better withsemantic searchallowed,and then certain tasks performed a lotbetter with no semantic search.

This kind of proves,you know, certain tasks requiredifferent types of tools. For example,when semantic search won, it was reallygood at finding a lot of behavioradjacent files that didn't have the samekind of keywords. For example, it waslike, I think, one example off the top of myhead was we were trying to, like, it was amulti, like, first handle lots ofdifferent ORMs that have to, like, handleacrossdifferent libraries and it didn't, bydefault, the keyword search didn't, byDefault, find all of them, but behaviorssemantic search was able to kind of likeunderstand these are all related files.

And then grep won when it was reallygood at just the task was a lot of itlike tracing through imports and if itlike was able to find the keywords inlike the first or second tool call, itwas able to like just keyword searchthrough that and find the relevantfiles. So again, it's like two differenttypes of how to find files, but theykind of lead to like really differentresults.So, in summary, what does this mean?Well, we saw semantic searchdid boost precision quite a bitand we kind of understand, like, grepand semantic search kind of finddifferent code in different ways.And an interesting thing to note as wellwas,these numbers weren't as great asCursor's because part of, like, part ofClaude code is it'sBuilt for just grepping. Like that'swhat Anthropic kind of focuseson. Like it's not built to understand, like, when to callsemantic search or how to call it. Uh, wekind of like add it as an extra tool, and

it's like, "Hey, like, here's this cooltool. You probably should use itsometimes." But it's very hard for it tohave a true understanding of when to useit, why to use it, uh, versus, like, forexample, Cursor's composer. Theyunderstand this is a built-in tool thatum,it knows when and how to use it, andthat's why they saw that it’s like 23 and a halfpercent, uh, performance gain. Uh,so, like, in summary,uh, you know, we think long-term winnerswere, like, kind of provide theselightweight tools to find the rightcontext in various different ways. Ithink it's something important to thinkabout. Uh, you can't just like grepthrough everything, unfortunately, in aFile system. Uh, we think there's a lotof different ways to access lots ofdifferent types of information. Uh, andthe people that provide these, like, easytools to provide to shrink down thesebillion context windows into the rightmillion, uh, will win in the long term.

Um, that's the general talk. Thank you.

If you have any questions, feel free tocome up.>> [applause]>> I have my own idea of what semanticsearch is, but could you define what youwhat's your definition is of semanticsearch?>> Sure. Uh, so this was just, uh, just doingvector search. It was just performingvector search using embedding, it usingVoyage's code model and then justembedding the, the, the query, umquery sentences orquery tokens and just sending them backto Turbo puffer. Yeah.Uh, sorry, theuh, embedding model, uh, Voyage code three.

Okay. And which vector DB? Turbo puffer.Yeah.>> Sorry. Uh no worries. Yeah, yeah. Yeah,for those who are unfamiliarwith Turbo puffer, we are the vector database that powers companieslike Cursor, Anthropic, Notion. So whenyou use something like Cursor, uh, youhave by proxy used Turbo puffer. Um, soyou may know us just not by name, Iguess.

I was just going to ask,you may not have a benchmark for this,but how does it performon code?Oh, that's tough. I mean,it's hard to say.>> Better, or is semantic better if thecode's like a mess and you need to goand sort it out? Uh,so I think it works best when there's alot of comments on the code, uh, becauseit kind of finds that semantic meaning.

>> Like the documentation is kind ofinline. Yeah, if it's like inline.

Documentation, that was like a big um boost. I believe one of the repos Iremember like looking through somedirectories and like asking Claude belike, "Why did it perform so well here versus not?" And it was one of its kindof explains me likeum when I was looking through as well,like those with like really goodcomments, for example, just likecomments above the function, it's ableto like really understand a lot more becauseyou kind of give this context to themodel and the embedding model. So thenit can like actually search better. Umbecause that's part of it. Like thethe embedding, it and is not the hardpart. It's like figuring out whatmeaning really is of that chunk.

Yeah.Yeah, you may have mentionedsome of it now, but of course, semanticsearch is just similarity search. So ifyour query doesn't really match theThen, you get some kind of innatedistance. Do you do any kind ofpreprocessing onwhat your target data before youlike, do you do a parent-child where theparent isquery-ish, and the child is the real code?

>> In this case, it was just simple, justjust the code. Yeah, just the raw codejust as a thing, butI can't speak for how these morecomplicated and sophisticated customersuse this, but I can imagine it'sdefinitely something of providing notjust code-level meaning, butyou know, as you said, at least aparent-child relationship of likeauthentication flow. Like that could bea good query to do a similarity searchagainst, but the code itself is morelike raw. Yeah.Yeah. Like Cursor has their ownembedding model, which I think kind ofhelps with this of like how do youTranslate code into more of like a humanlevel query. And I mean they're kind ofbeen experts on that. I can't speak forhow they do it, but I just know they dodo it.

I think they actually do what you saidlike they create fake comments on top ofof your code and then embed the codewith the comments. Yeah. Sothat's how they can have like their highrecall when theySo they add, they kind of injectcomments. Yes.Yeah, it's something that I thinkdefinitely could work. Yeah.In the back? Yeah.I was going to ask, like, how do you seeuh, I guess, the vector database kind ofworking with the partners,and howlike, when do youcode, like,long-term or need to reduce the size?

I mean, I think it depends. Likeobviously, the easiest wayLike, people love grepping because it'szero cost. Like, if you're able to likedownload everything to your local filesystem and just like grep through it,like, yeah, that works. Um, I think vectorDBs are built for actually likemultiplayer, and like this, like, supermaybe in a sense, like, hard to understandor, uh, complicated relationships betweenlots of data. For example, like aknowledge base, like a Notion, like youcan imagine, kind of hard to like reallygrep through that really easily on yourlocal machine. Like, it's in a sense, bestto like have that vectorize, uh, for theagents. Um,And even, stuff like, we have customersdoing stuff like with multimodal data.

You can't really grep through a videofile. You can't grep through an audiofile. You can't grep through an imagefile. Like, maybe you can glob on the file name,um, but like, get a trueunderstanding of, kind of, multimodal dataas well, is that something that we find aA lot of customers are doing.

Um, so it just kind of depends on theworkload andum, I, I, yeah, if you, if you're hittinglike, at some sort of even like miniaturescale, like a vector DB, kinda likehelps offload a lot of this workinto, you know, cache, computer cache,this semantic meaning.

Any other questions?Okay. Thank you all.>> [applause]
