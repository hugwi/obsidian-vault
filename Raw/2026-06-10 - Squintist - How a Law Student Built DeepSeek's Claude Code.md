---
title: "How a Law Student Built DeepSeek's Claude Code"
source: "youtube"
url: "https://www.youtube.com/watch?v=AsRSstoOL5U"
author: "Squintist"
published: "2026-06-10"
created: "2026-08-24"
duration: "0:11:37"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating:
tags:
  - "clip/video"
  - "claude-code"
  - "agents"
  - "anthropic"
  - "engineering"
  - "evaluation"
  - "harness-engineering"
  - "local-llm"
  - "microsoft"
  - "skills"
  - "video-gen"
summary: "May 2026, a university hall in Hangzhou, China. There's a stage, a banner that reads Whale Bros fan meet and greet, and a line of developers waiting to get a photo with the guest of honor, a 32-year-old American named Hunter Bown. Hunter is not a famous engineer."
---

# How a Law Student Built DeepSeek's Claude Code

![How a Law Student Built DeepSeek's Claude Code](https://www.youtube.com/embed/AsRSstoOL5U)

## Description

In May 2026, Chinese developers lined up for photos with Hunter Bown — a 32-year-old American with two music degrees, half a law degree, and no CS training. His spare-time project, CodeWhale (born "DeepSeek TUI"), is to DeepSeek what Claude Code is to Claude: a terminal coding agent. It hit #1 on GitHub trending and made him "Whale Brother" to the Chinese dev community.

This video is about the choices underneath — choices a trained programmer wouldn't make. A system prompt written as a literal constitution ("You shall not fabricate tool results"), affordable only because DeepSeek's cached input runs about a penny per million tokens. A model router that reads keywords in four languages. RLM, an MIT idea that fans giant documents out to sixteen cheap parallel readers. And the human arc: whale brothers, a fan tour that curdled, a dream job at an open-weight lab. If you'd watch a full RLM deep dive, say so in the comments — and subscribe for more under-the-hood breakdowns.


## Chapters
00:00 A fan meet-and-greet for a law student
00:45 The tool: from DeepSeek TUI to CodeWhale
01:13 Choices a programmer wouldn't make
01:49 Contradictory orders, and who outranks whom
02:49 A 10,000-token rulebook that's basically free
03:18 "You shall not fabricate"
03:54 The router that speaks four languages
04:48 Why it actually exploded: access
05:19 RLM — the MIT paper he just wired in
06:48 Honestly, is any one of these the reason?
07:19 Whale brothers
08:33 The tour curdles
09:03 The dream job at Arcee
09:48 The harness is the car, not the engine
10:25 Law-school brain, and traffic that runs both ways
11:06 One last thing: want the RLM deep dive?

## Sources & further reading
- CodeWhale on GitHub — https://github.com/Hmbown/CodeWhale
- The Constitution itself (the system prompt, Articles I–VII) — https://github.com/Hmbown/CodeWhale/blob/main/crates/tui/src/prompts/base.md
- CodeWhale site — http://www.deepseek-tui.com/
- Hunter's post on the Hangzhou meet-and-greet — https://x.com/goodhunt/status/2058952266963398701
- Pandaily on the star explosion — https://pandaily.com/deepseek-claude-code-clone-8700-stars
- Why Chinese developers can't just use the Western tools — https://x.com/VincentLogic/status/2063682825011048786
- Recursive Language Models (Zhang, Kraska, Khattab — MIT CSAIL) — https://arxiv.org/abs/2512.24601
- PandaYoo: "I'm an American guy, can someone help me get WeChat?" — https://pandayoo.com/post/im-an-american-guy-can-someone-help-me-get-wechat-en/
- huxiu on the China tour souring (Chinese) — https://www.huxiu.com/article/4861377.html
- Hunter announces he's joining Arcee AI — https://x.com/goodhunt/status/2059657721465409588
- VentureBeat on Arcee's open-weight models — https://venturebeat.com/ai/arcee-aims-to-reboot-u-s-open-source-ai-with-new-trinity-models-released

## Transcript

May 2026, a university hall in Hangzhou, China. There's a stage, a banner that reads Whale Bros fan meet and greet, and a line of developers waiting to get a photo with the guest of honor, a 32-year-old American named Hunter Bown. Here's the catch. Hunter is not a famous engineer. He has no computer science degree. Both his degrees are in music, and he's partway through law school. A year earlier, basically nobody in software knew his name. So, how does this guy end up with a fan meet and greet in a country he'd never set foot in? He wrote a coding tool in his spare time, and the Chinese developer community didn't just use it, they kind of fell for the guy who made it. The tool's called Code Whale, back then the very literal deep seek twee. Think Claude code, but open and built around deep seek. It lives in your terminal, reads your files, edits them, runs commands, handles get. Plenty of tools do that. Hunter wrote it in Rust, a serious systems language most beginners run screaming from, leaning on AI the whole way. And it worked. In a few weeks it blew past 35,000 stars and hit number one on GitHub's trending. So, why this one? The feature list is just the wrapper. It's the choices underneath that count, and they're choices a programmer wouldn't make. He was studying patent law while he built this, and it bleeds into the design everywhere. Start with a system prompt. That's the block of instructions a model reads before every single turn, the standing orders. Most people write theirs as a bulleted list of do's and don'ts. Hunter wrote his as a legal document. He calls it the constitution, and it's built to solve a specific annoying problem. A coding agent gets contradictory orders constantly. You tell it to edit a file, the project's own rules say don't touch that file. A tool result from three turns ago says the file already got changed. So, which order wins? A normal prompt just leaves the model to guess. The Constitution doesn't. It ranks every possible source of authority top to bottom. So, there's always an answer. There are nine ranks, but you don't need all nine. The shape is the point. Your live message outranks some stale rule written into the project last month. Actual evidence, what a command really printed, what's really in the file, outranks whatever the model thinks it remembers. "Evidence outranks narration." is how he puts it. And that's exactly how a courtroom works. Constitution beats statute beats regulation. Physical evidence beats testimony. That's the idea. A courtroom's pecking order dropped into a system prompt. Now, that thing is long. 10,000 tokens of rules the model rereads every turn. On something like Claude's Opus, you'd feel that. All that preamble on every call adds up fast. But this is where building for one specific model pays off. DeepSeek caches it. After the first turn, the whole rulebook is cached. And cached input on its cheap tier runs about a penny per million tokens. So, it's basically free to keep on. On a pricier model, nobody would write a constitution this big. It only makes sense here. And that rulebook has a specific job. DeepSeek's cheap tier is fast and loose. It makes things up more than the expensive models do. So, one article is aimed straight at that. Don't fake a tool result. Don't claim you verified something you didn't. Never declare success on faith. It's trying to patch a model's bad habit with a written rule instead of retraining the model. Does that hold up over a long session? Nobody really knows yet. But it's a sharp thing to try. Second move a normal engineer probably wouldn't make. Code Wheel picks which model to use for you fresh on every message. First it runs a quick keyword scan locally, no API call. If your message says debug or error or crash, it kicks the request up to the heavy reasoning model. If it's a search, it drops to the cheapest fastest tier. Everything in between gets the middle. And the keywords aren't just English. They're in four languages. Two kinds of Chinese plus Japanese. The router knows that tiaoshi means debug. So a developer in Shenzhen typing help me debug this in Chinese gets bumped up to the smart model automatically. Before this, every other terminal agent only watched for the English words. A Chinese developer asking for the hardest kind of help would silently get the dumbest setting. Nobody had bothered to check. And that point's why this thing actually exploded, which isn't really the router, it's access. If you're a developer in China, the big Western tools are a pain. Claude Code, Codex, you need a VPN and a foreign credit card just to log in. Cursor works, but it's expensive. Code Wheel? You install it, you pay deep sinking yuan, there's no wall to climb. For a huge number of developers, this was the first tool like it they could just use. That alone goes a long way toward explaining the stars. One more piece, and this one shows he's actually reading research, not just vibing. It's called RLM, recursive language models. It comes straight out of a paper from MIT published a few months back, and he just wired it into the agent. The idea is clean. When you work in a big code base, you don't paste the entire repo into the chat. You open files as you need them. The file system is your scratch space. You only ever look at the slice that matters. RLM does that same trick for any giant blob of text, a massive log, a research paper, a 60,000-word document. Codewhale spins up a little Python session in the background and drops the whole giant thing into a variable in there. The model never sees it. Instead, the model writes Python. Pick at this slice. Search for that pattern. Chop it into chunks. Then it fans the chunks out to a swarm of cheap helpercles, 16 at a time, each one chewing on a different piece and handing back a short answer. The model is just the foreman. It writes the code, collects the results, stitches them together. The enormous input never once enters its prompt. And because the helper model is so cheap, 16 of those calls in parallel cost less than a single call to the expensive one. You get a pile of parallel reading for almost nothing. Most agents just can't do this. Now, is any one of these the single reason to use it? Honestly, no. Plenty of tasks never touch batch document analysis. And some power users will tell you a rival agent edges it out on raw speed. The point isn't that Codewhale wins some benchmark. It's that every one of these choices is strange, specific, and built for this exact engine. But cheap access and clever engineering still don't get you a fan meet and greet. For that, look at how Hunter treated the people using it. A lot of Western tools quietly treat Chinese developers as an afterthought. Geo-blocked, building dollars, English only. Hunter went the other way, and not in a polished corporate way. He wrote full Chinese docs. He set up download mirrors so people inside China could actually install it. He started learning Chinese. He got on Twitter and more or less asked, "I'm an American guy. Can somebody help me get a WeChat account?" which is a real pain for a foreigner, because he wanted to be where these developers actually talked. One of China's big open-source communities, DataWhale, pulled him in. And since his tool was CodeWhale, the nickname wrote itself, Whale Brothers. So, he flew out to meet them, 7,000 miles, and that's the meet and greet from the top of the video. He wrote a genuinely moving post about the Hang Zhou stop, a room full of his users, a lot of them school teachers, hitting him with these incredibly detailed questions. He said he felt bad his schedule was too tight to sit with every single one and hear their story. A year earlier, he was an anonymous law student. Now, people were lining up to meet him because of something he made at home. But, it curdled a bit. What started as a grassroots community trip got inflated into a full commercial roadshow, a multi-city tour with corporate sponsors, partner universities, media partners, his name and DeepSeek plastered across all of it. And somewhere in there, he started to feel like the merchandise. He said it quietly in a Chinese group chat, "It feels like I'm being used." He cut the tour short and flew home. Chinese tech press framed it as the foreigner who came for the community and got a fast, hard lesson in how quickly enthusiasm turns into a business. No clear villain, more a coalition he never saw coming. Days after he gets home, he announces he's joining RCAI, and RC's the real deal, one of the more interesting AI labs in the US right now. They build open-weight models, the kind anyone can download and actually own, backed by Microsoft's and Samsung's venture arms, reportedly raising money at a billion-dollar valuation. His words on the job? A dream come true. And the fit is almost too perfect. He spent his nights building a harness for cheap open models. RC builds the open models. The hobby just became the job. Step back from Codewheel for a second. The harness matters as much as the model. The model's the engine, but the engine isn't the car. The rules, the routing, the feedback loops, the pecking order for whose instruction wins, that's the harness. And it's what turns a model that can talk about your code into one that actually finishes the job. And a harness built for one engine beats a generic one. People bolt Claude code onto Deep Seek through a proxy, and it works, but it's tuned for a different model's brain, so it leaves performance on the table. Codewheel goes the other way. It's shaped around this engine. The pricing, the sloppiness, the language its users actually speak. Take the Constitution. That one's pure law school brain. And it flips a story we keep telling about AI. The conversation always runs one way. AI's coming for lawyers. Engineers can do legal work now without the degree. This goes the other direction. Which rule wins when they conflict? What counts as evidence? Law has spent centuries formulating exactly that. And Hunter already had the whole framework in his head. So, he used it. We always talk about tech skills bleeding into every other field. The traffic runs both ways. One last thing. That RLM trick, recursive language models, I gave you the gist here, but it's a whole topic on its own. There's a paper behind it out of MIT, but the idea is big enough for its own video, a real deep dive. It would go deeper than this and lean more explainer than story. If you'd want that video, let me know.
