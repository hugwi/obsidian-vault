---
categories:
  - "[[Clippings]]"
created: 2026-06-23
rating: 
action: 
---
# I told Claude Code to build me an executive assistant. This is what my work as CTO looks like now

![rw-book-cover](https://pbs.twimg.com/profile_images/1724948866615676928/DlQ5J21H.jpg)

## Metadata
- Author: [[Obie Fernandez]]
- Full Title: I told Claude Code to build me an executive assistant. This is what my work as CTO looks like now
- Category: #tweets
- Summary: Obie Fernandez uses Claude Code as a personal AI assistant to manage his CTO tasks without extra effort. The system organizes meetings, action items, and team info through natural conversation and automates updates across tools like Slack and Calendar. This approach saves time, keeps full context, and helps him focus on work instead of managing knowledge.
- URL: https://x.com/obie/status/2013955736292704342/?rw_tt_thread=True

## Full Document
![I told Claude Code to build me an executive assistant. This is what my work as CTO looks like now](https://pbs.twimg.com/media/G_L_lIwWgAEe2QL.jpg)

*Managing 10 engineers, shipping code, and operating at the C-level simultaneously, with superhuman focus and power.* 

About three weeks ago I started as full-time CTO at ZAR (@zardotapp) . I opened a fresh directory and gave Claude Code a simple prompt:

Create me a markdown-based system where I can regularly run you, Claude Code, that lets me be the best world-class CTO possible. I'm planning to use you as my personal executive assistant and CTO expert. Document everything in a series of folders as you see fit. 

I didn't design a folder structure. I didn't create templates. I just asked Claude to figure it out. 

I'm here to tell you what living in the future looks like. 

### The results

I'm prepared for every single meeting. Every day. 

I always understand my priorities. At any moment I can get centered or figure out what to focus on next. 

When someone asks about a decision from last month, I have the full context. Not a vague memory. The actual alternatives we considered, why we chose what we did, and who was involved. 

I've had executive assistants in the past. Good ones, making six figures. Some of them were fucking awesome. (Hey Mare Contrare, miss you!!!) 

Claude is better. Than all of them. Put together. Sorry gals. 

This system gives me superhuman capabilities. I'm managing 10 engineers, shipping code myself, and operating as a C-level executive simultaneously. The system keeps track of everything, surfaces what I need when I need it, and handles execution (posting to Slack, updating calendars, tracking action items) without me having to context switch. 

I didn't want another tool to maintain. I wanted to just **talk** to an assistant and have it handle everything. No thinking about where files go. No remembering to update documents. Just natural conversation with an AI that knows my entire organization and acts on my behalf. 

#### How it actually works

I keep at least one Claude Code session open in this directory at all times. During the day, I'll fire up extra tabs with additional concurrent sessions as I have parallel workstreams, like preparing for multiple meetings, researching candidates, or writing blog posts. 

And I don't just type to it. If it's more than a sentence or two I try to remember to use Wispr Flow for voice input. I literally just stream of consciousness to Claude like it's my assistant. "Morning sync." "Prep for 1:1 with Daniel." "Post a summary of this PR to Slack." It feels like having Jarvis, except I'm still limited to a terminal window. 

Can't wait until I can just chat with it continuously throughout the day without the terminal constraint. That's obviously where this is going. 

Here's what a normal day looks like right now. 

I say "good morning" and Claude: 

* Reads my weekly focus
* Checks pending action items
* **Fetches my actual calendar for today** (via Rube/MCP integration)
* Tells me what needs attention

Takes 30 seconds. I know exactly what my day looks like. 

After any meeting: I just paste the transcript 

I use Gemini to transcribe meetings. After a call, I paste the transcript into Claude. That's it. (I'll have an automated solution for this within a day or two.) 

Claude automatically: 

* Creates meeting notes
* Extracts action items with owners
* Updates team roster with anything new learned about people
* Updates any other relevant context files

I don't tell it what to do. I don't think about where things go. **It just handles it.** 

"Prep for 1:1 with Daniel" 

Before a 1:1, I say "prep for 1:1 with [name]". Claude reads their history, reviews recent notes, checks pending action items, and suggests topics to cover. 

I walk into every 1:1 with full context. I'm pretty sure my team notices. 

"Post this update to Slack" 

I need to update the engineering channel about a significant PR or decision. I say "post this to #engineering on Slack" and give Claude the message. It posts it. Done. 

I've had it communicate with all my direct reports for me via Slack, asking them to setup recurring 1:1s with my meeting maker link. (They didn't realize it was an AI.) 

Same with Twitter. Same with calendar invites. Same with any other service I've connected via [Rube](https://rube.app/). 

The **Rube integration is absolutely essential**. It gives me full access to Calendar, Slack, Twitter, Linear, and everything else that contains organizational information. At any moment I can say "give me notes for the next meeting" and Claude just knows what to do. 

"Log decision about \_\_\_\_\_\_" 

When I make a decision, I say "log decision about X". Claude discusses context and options with me, creates a structured decision record, links to relevant context. 

Three months later when someone asks "why did we switch from X to Y?", I have the full rationale documented. Not just the decision, but the alternatives considered and why we rejected them. 

Looking at the above, I'm probably still underselling it. I can talk to this thing about my day, about decisions I need to make. I can ask it advice, and know that it's drawing upon the collected wisdom of humanity, but with access to all of my relevant context. This is not the same as popping into ChatGPT and asking it a question. 

#### The part I don't ever think about

Here's what's interesting: I have no idea how Claude organized the files. I mean, I *could* look. But I don't need to. That's the entire point. 

There are folders. There are markdown files. There's some structure Claude came up with. It works. I don't think about it.

![Image](https://pbs.twimg.com/media/G_MA1-pWsAADPkr.jpg) 

Compare that to Notion where you're constantly deciding "should this be a page or a database?" or "which workspace does this belong in?" or reorganizing things because the taxonomy you picked six months ago doesn't fit anymore. 

With this system, **the implementation is invisible**. I just talk to Claude and it handles everything. That's the entire value proposition. 

#### Real examples

**It's conversational.** I don't fill out forms. I don't update spreadsheets. I just talk like I'm talking to a human assistant. 

**It has full access to my work tools.** Calendar, Slack, Twitter, Linear. I can say "what's on my calendar tomorrow?" or "post this to Slack" and it just works. This is what the Rube/MCP integration provides and it's priceless. 

**It maintains context across sessions.** Everything is in markdown files under version control. Hooks handle keeping the contents of this folder in sync with its backing repo, which is just a personal repo on my Github account. Claude can reference decisions from weeks ago. Compare notes from multiple 1:1s. Surface patterns I wouldn't have noticed. 

**The system gets smarter over time.** Every conversation adds context. Every decision creates a reference point. Every team update builds a richer picture of who people are and what they care about. 

When I need to make a strategic decision, I can say "what similar decisions have we made?" and get actual relevant history, not a search results page of possibly-related documents. 

**It scales with parallel work.** Multiple Claude Code sessions mean I can prep for three different meetings simultaneously, each in its own tab with full context. 

#### Real Examples

**Hiring:** I paste a candidate's resume or LinkedIn. Claude updates its recruiting pipeline information, suggests questions based on gaps in our team, and preps me for the screening call by reading recent 1:1s to understand what the team actually needs. 

**Recruiting updates:** "Post an update about Stephen accepting our offer to [#leadership](https://x.com/search?q=%23leadership&src=hashtag_click) on Slack." Done. I don't context switch to Slack. I don't lose my train of thought. Claude handles it. 

**Performance issues:** Say an engineer isn't doing a great job. I say "walk me through the history with [Engineer Name]". Claude pulls up 1:1 notes, shows me the pattern of concerns, references the decision record about expectations not being met. When I eventually have to let them go, I'm not doing it based on vague feelings. I have documented evidence of repeated patterns. I tell Claude to post a report to a new thread on the the company's private HR slack channel to discuss offboarding. 

**Planning:** "What are the top three things blocking productivity right now?" Claude reads recent meeting notes, checks pending action items, status of projects and issues on Linear, and surfaces actual bottlenecks rather than what I *think* the bottlenecks might be based on hunches. 

#### Better than other systems

Most knowledge management systems fail because **maintaining them is a second job**. You have to remember to update things. You have to organize things. You have to think about the system instead of thinking about your actual work. 

This system works because **I never think about the system**. I think about my work, and the system captures it as a side effect of natural conversation. 

It's not a todo list I have to maintain. It's not a wiki I have to keep up to date. It's just Claude, always there, always listening, always organizing, always ready to surface exactly what I need. 

#### What this means for you, dear reader

If you're a CTO or technical manager operating across multiple roles, managing a team while shipping code, and expected to maintain perfect context across dozens of concurrent workstreams, this is table stakes. 

If you're any kind of knowledge worker, this is now table stakes. 

Not my exact system necessarily. Claude built what works for my brain and my role. It would build something different for you based on your needs. 

But you need **some** system that: 

* Captures context without requiring conscious effort
* Maintains institutional knowledge that compounds over time
* Gives you full access to your actual work tools
* Lets you work in natural language instead of forms and fields
* Scales with parallel workstreams

Here's what I'd suggest: 

**Just start.** Open Claude Code in a fresh directory. Tell it what you need. Let it figure out the structure. Use it for a week and see what happens. If you're an engineer put it in a private Git repo. Otherwise do it in a Google Drive, iCloud, or Dropbox folder so that it's automatically backed up. 

**Connect your tools.** Rube/MCP integration is essential. Calendar access alone is worth the setup. Being able to say "post to Slack" or "schedule a meeting" without context switching is game-changing. 

**Run multiple sessions.** One session is good. Three concurrent sessions for parallel work is when you feel the superpower. 

The actual Numbers (Three Weeks In)happens fast. By week three, you're operating at a level that wasn't possible before.a 

#### The actual numbers (three weeks in)

Let me show you what this looks like in practice. Here's the real data from my system: 

* **82 meeting notes** processed and filed
* **47 meetings** in January alone (2+ per day)
* **18 documented 1:1s** with full context and follow-up
* **35 action item tracking files** with owners and status
* **23 team members** everyone in the company, tracked with 264 lines of detailed context (background, strengths, career goals, recent conversations)
* **9 context documents** maintained (company strategy, architecture, tools, stakeholders)
* **11,579 total lines** of institutional knowledge captured

That's in three weeks. While also shipping code. While also operating at the C-level with the CEO and CPO. 

Will it scale? Yes, of course it will scale. If at some point it seems to be bogging down, I'll say something like "Hey you seem to be bogging down due to too much data, why don't you do something about it". 

Problem solved. 

And this is just version 1. Right now I'm constrained to a terminal window. But voice input via Wispr Flow already makes it feel like talking to Jarvis. The future is continuous conversation throughout the day. Not "using a tool." Just having an assistant who knows everything about your organization and can act on your behalf. 

Also the models are only going to get better. Imagine this with Opus 5 or 6. With better tools and integrations. In some sort of wearable? Wow. It's just a matter of time, probably later this year. 

And it's happening faster than most people realize. There are still people out there debating whether AI is useful or not. They're so fucked if they don't get with the program. 

**Everyone will have something like this eventually.** Either you figure it out now and get the compounding benefits, or you fall behind while your competition builds competitive advantages that actually persist and scale. Everyone at ZAR is being encouraged to adopt this kind of system, and I'm investing in consultants to hold their hand and get them past the initial learning curve of figuring out. All of my direct reports are *required* to adopt it, and since they're engineers they are expected to figure it out and make it their personal playground for experimenting with the latest cutting-edge techniques. 

### Give it a try yourself

Seriously, just open Claude Code in a brand new directory, and say "build a markdown-based operating system that makes me operate like a world-class ***\_***\_\_\_\_\_\_". Fill in the blank with your role. See what it comes up with. 

The future is here. It's just not evenly distributed yet. 

**About me:** I'm Obie Fernandez, CTO at ZAR. I've written multiple books including "The Rails Way" and "Patterns of Application Development Using AI." I've been building software for 30 years and I'm more excited about where we're going than I've ever been. 

**About ZAR:** We're building fintech infrastructure for emerging markets. Backed by a16z crypto, Dragonfly, the founders of Solana, and whole slew of other top-tier investors. If you're a senior Ruby on Rails product engineer who wants to work on hard problems with a team that's figured out how to fully automate its business using AI, we're hiring. You know how to reach me.
