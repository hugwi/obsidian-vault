# To people who are *good* at reviewing code (or claim...

![rw-book-cover](https://pbs.twimg.com/profile_images/1863998001380831232/2Pcl6VAu.jpg)

## Metadata
- Author: [[Łukasz | Wookash Podcast]]
- Full Title: To people who are *good* at reviewing code (or claim...
- Category: #tweets
- Summary: The author wonders how people can review large code changes without knowing the codebase well. They prefer using metrics and AI to assess code quality instead of reading all the code themselves. Humans should focus on managing code rather than reviewing every detail.
- URL: https://x.com/unclebobmartin/status/2044114698451476492/?rw_tt_thread=True

## Full Document
To people who are *good* at reviewing code (or claim to be hehe) - how is that possible?

To what extend you can properly review the code with low familiarity with the codebase?

Eg. New project, you jump in, Claude Code PR - 500 lines changed - review now

What's the strategy? 

---

I'm weirded out by people acting it's a strange ask - isn't this what's happening in companies right now? 

---

I don’t review code written by agents. I measure things like test coverage, dependency structure, cyclomatic complexity, module sizes, mutation testing, etc. 

Much can be inferred about the quality of the code from those metrics. The code itself I leave to the AI. 

Humans are slow at code. To get productivity we humans need to disengage from code and manage from a higher level.
