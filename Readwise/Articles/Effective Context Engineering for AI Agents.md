# Effective Context Engineering for AI Agents

![rw-book-cover](https://cdn.sanity.io/images/4zrzovbb/website/ea2bf01aa874d7ab776453e97dfeed5d2bf5a116-2400x1260.png)

## Metadata
- Author: [[anthropic.com]]
- Full Title: Effective Context Engineering for AI Agents
- Category: #articles
- Summary: Context engineering is about choosing the smallest, most relevant set of information to feed an LLM so it stays focused and effective. For long tasks, agents use techniques like compaction, structured notes, and sub-agents to avoid context overload. Treating context as a scarce resource is key to building reliable, autonomous AI agents.
- URL: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

## Full Document
[[Full Document Contents/Articles/Effective Context Engineering for AI Agents.md|See full document content →]]

## Highlights
- he broader question of “what configuration of context is most likely to generate our model’s desired behavior?" ([View Highlight](https://read.readwise.io/read/01kr7134xaa8dqh4w3papxb06n))
- **Context** refers to the set of tokens included when sampling from a large-language model (LLM). ([View Highlight](https://read.readwise.io/read/01kr712y0tbvjhmnnpsy4pccrv))
- **Context engineering** refers to the set of strategies for curating and maintaining the optimal set of tokens (information) during LLM inference, including all the other information that may land there outside of the prompts. ([View Highlight](https://read.readwise.io/read/01kr713se3q2h5rm70gg9s5sgm))
- agents that operate over multiple turns of ([View Highlight](https://read.readwise.io/read/01kr7151a54zpd2qx3hferz708))
- strategies for managing the entire context state (system instructions, tools, [Model Context Protocol](https://modelcontextprotocol.io/docs/getting-started/intro) (MCP), external data, message history, etc). ([View Highlight](https://read.readwise.io/read/01kr715e880qshhba34sdzzpnb))
- curating what will go into the limited context window ([View Highlight](https://read.readwise.io/read/01kr71602zyrk3zy63drrd7p0r))
- lose focus or experience confusion at a certain point ([View Highlight](https://read.readwise.io/read/01kr7169ejzase5xwfhdzyetsx))
- concept of [context rot](https://research.trychroma.com/context-rot): ([View Highlight](https://read.readwise.io/read/01kr716gme1w5jq7k7wrcgck6s))
- Context, therefore, must be treated as a finite resource with diminishing marginal returns. ([View Highlight](https://read.readwise.io/read/01kr717074yfntbmgz1xt81b69))
- which enables every token to [attend to every other token](https://huggingface.co/blog/Esmail-AGumaan/attention-is-all-you-need) ([View Highlight](https://read.readwise.io/read/01kr717ssb39qyawenq2nmaqf7))
- n² pairwise relationships for n tokens. ([View Highlight](https://read.readwise.io/read/01kr717gff75gxkyxzxxbkar4e))
