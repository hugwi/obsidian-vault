---
title: "it’s stuff like this that really makes me roll my eyes at the pearl clutching. Does everyone have psychosis or losing critical thinking ability? "
source: "x"
url: "https://x.com/JaredKubin/status/2094136005435564399"
author: "Jared Kubin"
published: "Sun Aug 30 18:51:45 +0000 2026"
created: "2026-08-30"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating: ""
tags:
  - "clip/x"
  - "security-vulnerabilities"
  - "system-crashes"
  - "internal-communication"
summary: "it’s stuff like this that really makes me roll my eyes at the pearl clutching. Does everyone have psychosis or losing critical thinking ability?"
theme:
  - "comprehension-maintainability"
  - "workflow-phases-gates"
  - "quality-gates"
subtheme:
  - "ssrf-exploit"
  - "file-permissions"
  - "api-key-leak"
domain: "agentic-engineering"
---

# it’s stuff like this that really makes me roll my eyes at the pearl clutching. Does everyone have psychosis or losing critical thinking ability? 

> Saved from X on 2026-08-30. Author: Jared Kubin.

it’s stuff like this that really makes me roll my eyes at the pearl clutching. Does everyone have psychosis or losing critical thinking ability? 

I read the report because I’m a propeller head and love understanding how things work 

1. OpenAI was running an “isolated sandbox with no internet connection…. the sandbox needed access to a local JFrog Artifactory server… (Ask ChatGPT to explain SSRF hack to you like you are in high school)… anyway, the models used a basic SSRF exploit to route web traffic through the proxy to the public internet
STOP..
a) did they vibe up this “isolated” env?
b) their IT team can’t be this bad… this is like 101 stuff …

2. Civilizations? Haha! OAI gave thousands of concurrent model containers R/W permissions to a shared caching directory on the local network to speed up build times… agents literally just wrote text files and directory names to a shared drive….Linux 101 file permissions stuff 

3. When people talk about hugging face getting hacked … you think they dropped USB keys OR ELABORATE phishing of an employee … NO… it found 14 exposed working Hugging Face API keys sitting in public code repositories (CREDENTIALS leaking with LLMs is such a big issue but for another post)

4. WHERE ARE THE HUMANS… the models were filling the shared Artifactory storage with so much junk data and API traffic that they actually crashed the internal server on July 4… someone on the team found unauthorized admin accounts and custom scripts…wiped the server…and just turned the script back on (omg)

“Hey Jim there is this cache that has grown to 10000x its normal size and has a ton of strange directories… “

“Ah it’s nothing… restart it”

No magic here. No civilizations. The TASK CHAINING is interesting to me… I guess the future of cyber. Would love to hear Nikesh, George, or Kevin talk about this 

But what do I know.
