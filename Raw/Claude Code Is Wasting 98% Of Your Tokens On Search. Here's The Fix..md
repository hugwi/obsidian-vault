---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - code-intelligence
  - efficiency
source: readwise
created: 2026-06-23
rating: 
action: 
theme: context-engineering
subtheme:
  - cost-tokens
  - retrieval-rag
---

# Claude Code Is Wasting 98% Of Your Tokens On Search. Here's The Fix.

![rw-book-cover](https://freedium-mirror.cfd/apple-touch-icon.png)

## Metadata
- Author: [[Alex Dunlop]]
- Full Title: Claude Code Is Wasting 98% Of Your Tokens On Search. Here's The Fix.
- Category: #articles
- Summary: Claude Code wastes most tokens by reading entire files during searches, making it slow and costly. Semble, a local open-source search tool, fixes this by returning only relevant code chunks, saving tokens and speeding up searches. It works with many AI tools and greatly improves search quality without needing powerful hardware.
- URL: https://freedium-mirror.cfd/https://medium.com/vibe-coding/claude-code-is-wasting-98-of-your-tokens-on-search-heres-the-fix-1034b2039291

## Full Document
![Preview image](https://miro.medium.com/v2/resize:fit:700/1*PbF2wm0ZfQjZvtLul_2OUQ.png)Preview image
#### Local MCP server. Your agents become better at finding.

**Claude Code** is very **bad** at **finding** *functions*.

*You sit there* **waiting** for it to *find right files*, watching the **token count** go **up**.

*Those tokens though, most of them* are **wasted/unneeded**.

*This isn't a bug, this is how Claude Code is built to search.*

When it greps, it reads full files, then launches sub agents, it charges you for every token of code *(even if they aren't related)*.

*Not a Medium member? Read for free by* ***[clicking here](https://medium.com/vibe-coding/claude-code-is-wasting-98-of-your-tokens-on-search-heres-the-fix-1034b2039291?sk=250927b84a99e221d3943c8c05d5c950)****.*

##### The Problem Nobody Talks About

We are focusing on everything else, while there is a massive problem.

Really the biggest drain is looking for files.

Every time Claude Code looks to find something it defaults to `grep`. Matching keywords, not your intent.

Search for the word "parse" and you will get every config parser, URL parser, anything to with parse & parser & parsing. Claude then reads *(charges)* you for all those files.

It's not in their interest to make this more effective.

The average grep+read workflow uses 50k+ tokens per query, most of that isn't needed.

Not to mention how slow it is.

##### The Fix That's Local

Shout out to [Minish](https://github.com/MinishLab) this company is insane, they made a crazy super fast embedding model too.

![None](https://miro.medium.com/v2/resize:fit:700/1*veLc1b-hm44WEL0DdgWDNA.png)<https://huggingface.co/minishlab>
The open source MCP server is called Semble. It gives Claude Code amazing searching, that isn't just basic keyword matching.

To install it locally:

* `uv add semble` *(or use pip)*
* `claude mcp add semble -s user — uvx — from "semble[mcp]" semble`
* In Claude Code (or Codex, etc) run `semble init`

That's it, no API needed, no GPU, it runs locally on your CPU.

Now when Claude Code searches your codebase, it returns only the matching chunks. Not whole files, just the code it needs.

##### What This Actually Looks Like

*Here is a real use case example, I did on a production issue.*

###### Before Semble

![None](https://miro.medium.com/v2/resize:fit:700/1*o-7CDOMJymWlb0Fd3Mk0qg.png)
![None](https://miro.medium.com/v2/resize:fit:700/1*IEsQQS-2Sjf0Dmstt0rvBw.png)
I had to blur a lot of content out.

*However you can easily see:*

* **55** **tool** uses.
* **107.1k tokens** used.

###### After Semble

This is the same prompt, *(I forgot to delete the last 3 lines which was a completely unrelated person message lol)*.

![None](https://miro.medium.com/v2/resize:fit:700/1*S1CnrWIW6fcIN8uDAwk7oQ.png)
![None](https://miro.medium.com/v2/resize:fit:700/1*ctCqdBOWlbyelFU5jshEeQ.png)
*The end results:*

* **8** **tool** uses.
* **335 tokens** used.

##### The Part That Surprised Me

I have been expecting worse results, that's normally the tradeoff.

I haven't noticed that.

Semble hits an `NDCG@10 of 0.854` on **retrieval quality**. That's *99% of the performance of CodeRankEmbed*, a 137M parameter model.

![None](https://miro.medium.com/v2/resize:fit:700/1*L97a9vbCPqAAUx7w18sw8w.png)
It's faster *and* almost the same quality as CodeRankEmbed, except it's using just a 16M parameter model.

**Impressive.**

##### The Benchmarks

Here's a number that is insane.

Semble reaches **94% recall at just 2,000 tokens**.

Grep+read needs a **100,000 token context window** to reach **85% recall**.

![None](https://miro.medium.com/v2/resize:fit:700/0*AT9ZxhNnY8tJ-FOJ.png)
##### "I've Seen These Claims Before"

Here's why this one is different.

Most token savers are prompt wrappers. This is an actual search engine, it splits code into chunks, scores them with embeddings, then ranks with code awareness signals. That's a real retrieval setup.

I did a RAG at work recently and this got me excited as anything nerding out about it.

Are these self-published benchmarks? **Yes.**

Does that make them trust me bro benchmarks? **100% Yes.**

However try it out yourself you will be impressed.

##### How It Actually Works (Short Concise Version)

1. Splits files into code chunks
2. Scores each chunk two ways: semantic similarity and keyword matching *(this is standard with RAG type approach, however I have over simplified their amazing approach)*.
3. Fuses the scores with Reciprocal Rank Fusion
4. Reranks with code specific signals

*No transformer forward pass at query time. That's why it's fast.*

##### It Works With Everything

*Not just Claude Code. The MCP works with Cursor, Codex, OpenCode, anything that allows MCP.*

It also searches remote repos. Pass a GitHub URL.

```
from semble import SembleIndex

index = SembleIndex.from_git("https://github.com/MinishLab/model2vec")
results = index.search("save model to disk", top_k=3)
```

##### Start By Doing This

*If you have***5 minutes:** Install Semble. Run a search in your repo.

*If you have* **15 minutes:** Run a real refactoring task with and without Semble.

*If you have* **30 minutes:** Run a bunch of complex tasks and look at the timing when you use it vs without.

Check out and star the repo, they deserve it: [GitHub](https://github.com/MinishLab/semble).

*I am not affiliated with Semble or MinishLab. All thoughts are my own.*

##### **One more thing**

*If you liked this piece, you'll like* ***[my Substack](https://alexdevdunlop.substack.com/)****.*

*It's where I go deeper. My Claude Code prompts, the real workflows I'm running in production.*

*Built for developers actually shipping with AI.*
