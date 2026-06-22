# Claude Saves Tokens, Forgets Everything

![rw-book-cover](https://golev.com/og/claude-saves-tokens-forgets-everything.png)

## Metadata
- Author: [[Alexander Golev]]
- Full Title: Claude Saves Tokens, Forgets Everything
- Category: #articles
- Summary: Claude’s automatic context compaction summarizes earlier conversation parts to extend chat length but often causes it to forget important instructions. Users report that after compaction, Claude frequently ignores critical project rules and skills, making long sessions unreliable. To work well, users must manually manage context and save key information outside the conversation.
- URL: https://golev.com/post/claude-saves-tokens-forgets-everything/

## Full Document
![Ice sculpture of Einstein's E=mc² equation melting on deep blue background](https://golev.com/_astro/claude-context-compaction.DmZDptuS_2fb0p4.webp)Ice sculpture of Einstein's E=mc² equation melting on deep blue background
* 
* 
* 

I’ve been using Claude professionally for over a year now, mostly for long conversations on complex projects. The kind of work where you spend thirty turns teaching the model your preferences, establishing working patterns, building up a shared understanding of what you’re trying to accomplish.

For most of that year, these conversations had a way of ending just when they were getting useful. You’d be deep into a session, Claude finally understanding exactly what you needed, and then the message of doom would appear. “Claude hit the maximum length for this conversation.” Everything you’d built together, gone. Start fresh. Explain it all again.

Then in November 2025, Anthropic shipped a “fix.” (Claude Code had it from its February launch.) Instead of the wall, somewhere around the ninety-minute mark a progress bar appears. “Compacting our conversation so we can keep chatting. This takes about 1-2 minutes.”

When it finishes, you can keep chatting. Claude just can’t remember what you were chatting about. The coding conventions we established, the specific phrasing I asked it to avoid, all summarised into oblivion.

The [marketing was optimistic](https://www.anthropic.com/news/claude-opus-4-5): “For Claude app users, long conversations no longer hit a wall—Claude automatically summarizes earlier context as needed, so you can keep the chat going.”

What they didn’t mention is what happens to the context that gets summarised away.

#### What Compaction Actually Does

The mechanics are straightforward. Claude’s context window is [200,000 tokens on paid plans, with 500,000 tokens on some Enterprise models](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work). In the Claude app, automatic context management summarises earlier messages when a conversation approaches that limit. In SDK compaction, Claude generates a summary wrapped in `<summary></summary>` tags and replaces the message history with that summary.

Your chat history is preserved for scrollback, and Anthropic says Claude can still reference it after summarisation. But the working context that shapes the next response? That’s been compressed into whatever the context management process decided was worth keeping.

According to [Anthropic’s API documentation](https://platform.claude.com/docs/en/build-with-claude/context-editing), SDK compaction is a client-side alternative to server-side context management. In the Claude app, [automatic context management](https://support.claude.com/en/articles/11647753-how-do-usage-and-length-limits-work) requires code execution enabled in settings, and longer conversations consume more of your usage limit.

The problem isn’t that summarisation happens. The problem is what gets summarised away.

#### Documented Amnesia

I could describe my own frustrations, but anecdote isn’t evidence. So let’s look at what’s actually documented.

On GitHub, the bug reports tell a consistent story. [Issue #9796](https://github.com/anthropics/claude-code/issues/9796) from October 2025 describes a user whose project instructions were followed perfectly before compaction and violated 100% of the time after:

“After context compaction occurs during long conversations, the assistant completely forgets all instructions from .claude/project-context.md. This causes critical project rules to be violated: Uses TodoWrite when project requires Beads. Apologizes when project explicitly forbids apologies. Forgets to activate venv when project requires it. Ignores other critical workflow instructions.”

The user is explicit about the failure rate: “The assistant follows these rules perfectly before compaction, then violates them 100% of the time after compaction.”

[Issue #13919](https://github.com/anthropics/claude-code/issues/13919) from December 2025 documents the same pattern with Claude’s Skills feature:

“After auto-compaction occurs, Claude completely loses awareness of Claude Skills that were actively being used. Specifically: Claude forgets which skills were being used during the session. Claude forgets the procedures/methodologies from those skills. Claude does NOT proactively re-read the skill files after compaction. Claude repeats errors that the skills were specifically designed to prevent. Even explicit instructions in ~/.claude/CLAUDE.md telling Claude to reload skills after compaction are ignored.”

The issue cross-references five related bug reports, including #1534 on memory loss after auto-compact, which was closed but apparently never fixed.

[Issue #10960](https://github.com/anthropics/claude-code/issues/10960) documents Claude forgetting which repository it was working in:

“Claude is loosing [sic] context that we changed to new repo and u forget that after compaction and again start and commit same mistake again and again…”

The user’s frustration is palpable: Claude loses “the current directoy [sic], the command use, change of directory etc” and then starts guessing, mostly wrongly, ruining work already done.

These failures aren’t edge cases. The bug reports include reproduction steps and consistent failure patterns.

#### So, Someone Built a Whole CLI

The [DoltHub engineering blog](https://www.dolthub.com/blog/2025-06-30-claude-code-gotchas/) published a frank assessment in June 2025:

“For larger tasks, Claude will often hit the limit of what it can hold in context. At this point, it performs a context compaction that takes a couple minutes. After it is done, it prints out what the new context is which is a cool summary of what you’ve done in the session up to that point. The summary is cool but Claude Code is definitely dumber after the compaction. It doesn’t know what files it was looking at and needs to re-read them. It will make mistakes you specifically corrected again earlier in the session.”

“Definitely dumber after the compaction” is a fairly damning verdict.

Developer Du’An Lightfoot [described his workflow](https://www.duanlightfoot.com/posts/what-to-do-when-claude-code-starts-compacting/) in September 2025:

“Have you ever been deep into a vibe coding session and Claude Code starts compacting? There are few things in life that can kill the vibes like this. You and Claude were tag teaming building an amazing new app feature when suddenly, Claude can’t remember what you discussed five minutes ago. Do you push through? Try to salvage the session? Nope! Here’s what I do: /quit. Then immediately after enter claude again to begin a fresh new session with the right context.”

His solution to compaction is to abandon the conversation entirely.

Another developer [built an entire CLI toolkit](https://medium.com/@jason_81067/how-i-solved-claude-codes-context-loss-problem-with-a-cli-toolkit-cc4bcde9c9d4) specifically to work around the problem:

“If you’ve used Claude or any AI-assisted coding environment, you’ve probably hit the wall where your assistant just forgets everything mid-session. It’s not your imagination — context compaction is a real limitation, and it gets worse the longer your coding sessions get.”

The common thread in all of these accounts is that experienced users treat compaction as a failure mode to avoid rather than a feature to rely on.

#### What Anthropic Says

Anthropic’s official messaging emphasises the benefit. From the [Opus 4.5 announcement](https://www.anthropic.com/news/claude-opus-4-5):

“For Claude app users, long conversations no longer hit a wall—Claude automatically summarizes earlier context as needed, so you can keep the chat going.”

And:

“With effort control, context compaction, and advanced tool use, Claude Opus 4.5 runs longer, does more, and requires less intervention.”

The only caveat in Anthropic’s support documentation is about limits, not fidelity: “Rare edge cases (such as very large first messages) may still encounter context limits.”

Rare edge cases. That’s the characterisation of a problem that multiple GitHub issues describe as 100% reproducible.

One [user guide author](https://limitededitionjonathan.substack.com/p/ultimate-guide-fixing-claude-hit-a94) put it more bluntly:

“This isn’t magic. There are tradeoffs. You lose granularity. Every time Claude compacts, information gets compressed. Not just any information - often the precise technical details that matter most. The more compaction cycles you go through, the vaguer everything becomes.”

And:

“It’s automatic, not optimal. The automatic compaction triggers around 95% capacity (or 25% remaining context). Claude decides what to keep and what to summarize. It does a decent job, but it might not preserve what you would have preserved.”

#### The Architectural Problem

The fundamental issue is that compaction is a lossy summarisation process that has to make decisions about what matters. And the algorithm appears to privilege recency over importance.

Instructions you established early in a conversation get summarised away first. Corrections you made mid-conversation disappear. Working patterns that took multiple exchanges to refine vanish into a single sentence like “user prefers certain coding conventions.”

Claude Code users have a partial escape valve. The `/compact` command accepts preservation instructions. You can type `/compact preserve the coding patterns we established` or `/compact only keep the names of the websites we reviewed` and give the summarisation process some guidance.

Users of claude.ai get no such control. When compaction triggers, you’re at the mercy of whatever the algorithm decides is worth keeping.

There’s also no concept of protected context. System prompts persist because they’re architecturally separate from the conversation. But user-established patterns, preferences, and instructions? Those live in the conversation history and get compressed like everything else.

The [Claude Code system prompts repository](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/system-prompts/agent-prompt-conversation-summarization.md) on GitHub documents the summarisation prompt used for compaction. It’s about 1,200 tokens of instructions telling Claude how to create detailed conversation summaries. But detailed doesn’t mean complete. The prompt still requires Claude to decide what matters enough to preserve.

#### It Gets Worse with Opus

There’s an additional wrinkle for users of Anthropic’s then-flagship model. Opus 4.5 uses “extended thinking,” which generates `<thinking>` blocks in responses. [GitHub issue #12311](https://github.com/anthropics/claude-code/issues/12311), now closed, reported that these thinking blocks could break compaction entirely:

“The Opus 4.5 model uses ‘extended thinking’ which generates <thinking> blocks in responses. When Claude Code attempts to compact/summarize the conversation: It modifies or reorganizes messages containing thinking blocks. The API rejects this because thinking blocks ‘cannot be modified’ and ‘must remain as they were in the original response.’ Both streaming and non-streaming fallback fail with the same error. The compaction never succeeds, making the session unrecoverable.”

The reported workaround was to switch to Sonnet, which didn’t use extended thinking. So if you were paying for the most expensive model and doing extended work, you could end up with worse context management than cheaper alternatives.

#### Compaction vs Memory

It’s worth distinguishing compaction from Claude’s memory feature, because they solve different problems and their names cause confusion.

Compaction operates within a single conversation. When you approach the token limit, earlier exchanges get summarised. The compression is immediate and lossy.

Memory operates across conversations. It synthesises insights from your chat history, [updates every 24 hours](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context), and provides context for new conversations. Each Project has its own separate memory space.

The gap between these two systems is precisely where the problem lives. Memory handles cross-session continuity. Compaction handles within-session token management. But there’s no mechanism for preserving within-session learnings that were established through extended collaboration.

If you spend thirty turns teaching Claude your preferences and then compaction triggers, those preferences get summarised into something generic. Memory won’t capture the specifics because memory synthesises every 24 hours and focuses on persistent user context, not session-specific refinements that emerged from collaborative work.

The architecture has a blind spot. Context that’s too ephemeral for memory but too important to lose in summarisation has nowhere to live.

#### How People Actually Cope

The workarounds people have developed are revealing. They treat compaction as an adversary to be managed rather than a feature to be used.

Claude Code users have learned to run manual `/compact` at logical breakpoints rather than waiting for auto-compact to trigger mid-task. The [Steve Kinney course on Claude Code](https://stevekinney.com/courses/ai-development/claude-code-compaction) recommends doing this when you finish a task, before unrelated work piles up in the same chat. They store critical context in CLAUDE.md files that get reloaded each session, rather than relying on conversation history. And when compaction quality degrades anyway, many simply quit and restart with fresh context, as Du’An Lightfoot described.

Web users of claude.ai have fewer options but similar instincts. Projects let you store critical instructions that persist separately from conversation history. Some users checkpoint manually at roughly 70% capacity, asking Claude to summarise key decisions and copying the summary somewhere external before the automatic compaction triggers. Others front-load critical instructions at the start of every prompt and reiterate them every few messages. Keeping substantive work in Artifacts rather than the conversation itself helps too, since Artifact content survives compaction better than conversational context.

My own workaround for long research sessions is prompting Claude to maintain a running log of progress within the conversation itself. The instruction “Maintain a log, otherwise after every compacting you start from scratch. Update the log after every action, do not batch actions.” forces Claude to create recoverable state. When compaction breaks the flow, I tell it to check its own log and resume. Not external checkpointing, but teaching the model to checkpoint itself.

The common theme is that experienced users don’t trust compaction to preserve what matters. They’ve developed external systems to work around its limitations.

#### Was The Trade-Off Worth It?

Anthropic solved a real problem. Before compaction, hitting the context limit meant your conversation was over. You’d see “Claude hit the maximum length for this conversation” and have to start fresh. Compaction lets conversations continue indefinitely.

But the solution created a different problem. Instead of a hard stop that forces you to checkpoint manually, you get a soft degradation that erases your working context invisibly. The conversation continues, but Claude becomes “definitely dumber.”

The question Anthropic hasn’t publicly addressed is whether that trade-off is actually better for users.

A hard limit is annoying, but it’s honest. You know exactly when you’ve hit it, and you can prepare accordingly with strategic checkpointing or breaking work into separate conversations. The discipline is forced but the outcomes are predictable.

Automatic compaction is convenient, but it’s deceptive. Your conversation continues smoothly while Claude silently forgets the context that made it useful. You don’t realise the problem until Claude starts violating instructions it followed perfectly an hour ago.

For casual use, compaction is probably fine. Quick questions and throwaway conversations where the summarisation loss doesn’t matter because there’s nothing important to lose.

For serious work, compaction may actually be worse than the hard limit it replaced. The users doing extended collaborative sessions, building up shared understanding over time, establishing working patterns through iteration, those are precisely the users most harmed by lossy summarisation. And they’re the users most likely to be caught off guard because the conversation appears to continue normally.

#### Both Labs Hit the Same Wall

It’s worth noting that Anthropic isn’t alone in struggling with this problem. OpenAI announced that [GPT-5.1-Codex-Max](https://openai.com/index/gpt-5-1-codex-max/) is “the first model natively trained to operate across multiple context windows through a process called compaction.”

The language is almost identical to Anthropic’s. “Compaction enables GPT‑5.1-Codex-Max to complete tasks that would have previously failed due to context-window limits.”

Both companies are tackling the same architectural challenge. Context windows are finite, but user expectations are not. Something has to give, and that something is apparently the fidelity of earlier context.

Whether OpenAI’s approach handles the instruction-preservation problem better than Anthropic’s is an open question. The fact that both major AI labs are shipping similar solutions suggests the problem is genuinely hard, not that either has solved it well.

#### What Would Actually Help

The feature requests in the GitHub issues point toward potential solutions.

Protected context that survives compaction. Allow users to mark certain content, like project instructions or established preferences, as non-summarisable. Treat it like system prompt context that persists regardless of conversation length.

Post-compaction instruction reload. After compaction completes, automatically re-read instruction files like CLAUDE.md and project-context.md. One bug report notes that “Even explicit instructions in ~/.claude/CLAUDE.md telling Claude to reload skills after compaction are ignored.” The workaround shouldn’t require Claude to follow instructions that it’s demonstrably failing to follow.

User-guided compaction in claude.ai. Give web users the same `/compact` command with preservation instructions that Claude Code users have. Let people control what gets prioritised in the summarisation.

Compaction quality metrics. Surface information about what was preserved and what was lost, so users can make informed decisions about whether to continue or restart.

Opt-out for power users. [GitHub issue #6689](https://github.com/anthropics/claude-code/issues/6689) requests a `--no-auto-compact` flag for users who prefer to manage context manually. The issue remains open. “I’m quite certain that 80% of users, and definitely 100% of power users already manage their own context via saving and restoring plans from files…”

None of these solutions are technically exotic. They’re product decisions about how to balance convenience for casual users against control for serious ones.

#### Where This Leaves Us

If you’re doing extended work with Claude, you need to manage your own context. Use Projects for persistent instructions, CLAUDE.md files for project-specific context, or prompt Claude to maintain recovery logs within the conversation itself. Checkpoint manually before you hit the compaction threshold, whether that’s external documentation or internal state that Claude can reference when things break.

The workarounds exist because compaction isn’t reliable for preserving what matters. Treat it as a safety net for when you forget to checkpoint, not as a feature you can depend on.

If you’re building systems on Claude’s API, consider whether you actually want automatic compaction enabled. The [SDK documentation](https://platform.claude.com/docs/en/build-with-claude/context-editing) lets you configure thresholds, use cheaper models for summarisation, or disable the feature entirely. For applications where instruction fidelity matters more than conversation length, manual context management may be the better choice.

And if you’re investigating older Opus 4.5 sessions specifically, be aware that extended thinking was reported to break compaction entirely. The workaround in that report was to switch to Sonnet when approaching context limits, which rather defeated the purpose of paying for the flagship model.

For now, the honest answer is to trust compaction about as much as you’d trust a colleague who takes great meeting notes but loses them at random intervals. Useful to have around, but not something to build critical workflows on without backup systems in place.
