# Hacker News

![rw-book-cover](https://news.ycombinator.com/favicon.ico)

## Metadata
- Author: [[GodelNumbering]]
- Full Title: Hacker News
- Category: #articles
- Summary: Dirac uses smart code editing techniques like hash-anchored edits and AST to improve efficiency. Developers discuss how AST can help with easier code review and better context understanding. They also compare tools and methods for handling large codebases and improving AI-assisted coding.
- URL: https://news.ycombinator.com/item?id=47921034

## Full Document
### [GodelNumbering](https://news.ycombinator.com/user?id=GodelNumbering)

 (2026-04-27 13:03:01)

 Interesting things Dirac does:1. Uses an optimized version of Hash-Anchored edits for file editing (<https://dirac.run/posts/hash-anchors-myers-diff-single-token>)2. Utilizes language's AST to decide what to fetch into context, entirely avoids large code file reads3. Batches all operations. Does large number of reads/edits simultaneously (you can see a video demo for deepseek-v4-flash here [https://www.reddit.com/r/LocalLLaMA/comments/1suhdki/tested\_...](https://www.reddit.com/r/LocalLLaMA/comments/1suhdki/tested_deepseek_v4_flash_with_some_large_code/))4. Allows the model to execute code to analyze things on the fly, so the model can simply write bash/python/perl script to accomplish things where appropriate5. A lot of context curation and opportunistic context updates, i.e. put into context anything that you are certain model would ask next
 

#### [deskamess](https://news.ycombinator.com/user?id=deskamess)

 (2026-04-27 13:20:06)

 I always wondered why AST's were not more of a part in both editing and scoping of changes/parsing code. I thought I read an article where they said 'grep' was just as effective. It kinda made sense for the case they were talking about.
 

##### [miki123211](https://news.ycombinator.com/user?id=miki123211)

 (2026-04-27 21:53:35)

 I think we should use ASTS more, not for performance, but for easier code review.Changes that are primarily code refactorings, like breaking up a large module into a bunch of smaller ones, or renaming a commonly-used class, are extremely tedious to review, both in LLM generated diffs and human-written PRs. You still have to do it; LLMs have a habit of mangling comments when moving code across files, while for a human, an unassuming "rename FooAPIClient to LegacyFooAPIClient" PR is the best place to leave a backdoor when taking over a developer's account. Nevertheless, many developers just LGTM changes like this because of the tedium involved in reviewing them.If one could express such changes as a simple AST-wrangling script in a domain-specific language, which would then be executed in a trusted environment after being reviewed, that would decrease the review burden considerably.I believe that with agentic development, the most important constraint we have is human time. Making the LLM better and faster won't help us much if the human still needs to spend a majority of their time reading code. We should do what we can to give us less code to read, without losing confidence in the changes that the LLM makes.
 

##### [GodelNumbering](https://news.ycombinator.com/user?id=GodelNumbering)

 (2026-04-27 13:27:45)

 Grep is effective for the most part, except for situations like when you have huge codebases and the thing you're looking for is used in too many places both as symbol and non-symbol.Another annoying thing about plain grep is, LLMs often end up pulling in bundled packages when using grep where 1 line is large enough to ruin the context window
 

###### [embedding-shape](https://news.ycombinator.com/user?id=embedding-shape)

 (2026-04-27 13:39:46)

 > Grep is effective for the most partIt's very effective in well-written and well-designed code bases where concepts tend to be relatively well formed to not be named the same as everything else, so grepping for symbols give you good search results.Projects where the god-object or core concepts are generic names like "Tree", "Node" or other things that are used everywhere, tends to be short of impossible to search with grep and friends.
 

##### [lukeundtrug](https://news.ycombinator.com/user?id=lukeundtrug)

 (2026-04-27 19:43:15)

 Happened to have written both a tool and a blog post about the topic. It’s more about the different technical approaches you have in solving the problem but it might still interest you :)[https://www.context-master.dev/blog/deterministic-semantic-c...](https://www.context-master.dev/blog/deterministic-semantic-code-graphs)Let me know, what you think
 

###### [vintagedave](https://news.ycombinator.com/user?id=vintagedave)

 (2026-04-28 07:19:25)

 This is interesting - I have been working on the same thing, building contextual data, LSP-style.I saw the tools page where if I understand right, `get-symbol-context` is actually the main useful tool for what you provide? The others seem more metadata it's easy to get already (?) but that tool provides the extra info.I had been working on exposing mine as more high-level, ie multiple APIs to query different kinds of metadata about symbols, types, etc. But I am still not sure of the best approach, where my thinking was about not overloading the AI with too many different tools. They accumulate quickly.
 

#### [messh](https://news.ycombinator.com/user?id=messh)

 (2026-04-27 15:47:11)

 Anchor based editing requires injecting new anchors to the context, and dirac does so via a diff. So how is this more efficient (token-wise) than search and replace?? Even at a single token per hash. Also, code is read more than written so these just add up. I experimented once with stable anchors, albeit longer than a single token, and found it a downgrade.My conclusion is that the efficiency dirac sees comes mainly from showing file skeleton by default
 

##### [hedgehog](https://news.ycombinator.com/user?id=hedgehog)

 (2026-04-27 18:06:52)

 I'm not sure one way or another but I've been using a related tool called Tilth by another poster here. It doesn't do anchor-based editing, but it does do syntax-aware search and will e.g. report the line range for function definitions, provide file outlines with line numbers on a file name match, etc.<https://github.com/jahala/tilth>

###### [alexp90r](https://news.ycombinator.com/user?id=alexp90r)

 (2026-04-28 13:00:05)

 This seems really good...going to test it :)
 

###### [messh](https://news.ycombinator.com/user?id=messh)

 (2026-04-27 19:07:29)

 ohh this is really nice :) testing it
 

##### [gchamonlive](https://news.ycombinator.com/user?id=gchamonlive)

 (2026-04-27 19:24:17)

 > My conclusion is that the efficiency dirac sees comes mainly from showing file skeleton by defaulthow hard do you think it would be to bring this optimization to oh-my-pi and opencode? I am testing dirac and it's very cool but the tooling isn't there yet comparing to oh-my-pi in terms of UX.
 

###### [GodelNumbering](https://news.ycombinator.com/user?id=GodelNumbering)

 (2026-04-27 23:17:54)

 Would love some more feedback on this. Where do you think are major gaps?
 

#### [jbellis](https://news.ycombinator.com/user?id=jbellis)

 (2026-04-27 15:42:37)

 > Batches all operations. Does large number of reads/edits simultaneously...I wasn't sure what this meant, so I looked at the source. It seems to be referring to tool APIs being designed around taking multiple targets as a list parameter, instead of hoping the model makes appropriately parallel tool calls. (This matches my experience btw, models are reluctant to make a large number of parallel calls simultaneously, and this seems more pronounced with weaker models.)
 

##### [verdverm](https://news.ycombinator.com/user?id=verdverm)

 (2026-04-27 15:47:50)

 I think Anthropic may have mentioned this first, this pattern is also something my custom agent's tools are designed around, pretty sure I picked it up from them.
 

 There are more comments to this post:
 

* <https://news.ycombinator.com/item?id=47929109>
* <https://news.ycombinator.com/item?id=47922525>
* <https://news.ycombinator.com/item?id=47922805>
* <https://news.ycombinator.com/item?id=47923451>
* <https://news.ycombinator.com/item?id=47930206>
* <https://news.ycombinator.com/item?id=47922529>
* <https://news.ycombinator.com/item?id=47924578>
* <https://news.ycombinator.com/item?id=47921358>
