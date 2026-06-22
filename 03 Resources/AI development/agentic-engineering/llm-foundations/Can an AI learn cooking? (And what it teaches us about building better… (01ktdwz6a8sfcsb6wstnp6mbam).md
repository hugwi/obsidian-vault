---
title: "Can an AI learn cooking? (And what it teaches us about building better agents)"
source: "https://www.reddit.com/r/HowToAIAgent/comments/1tx2oqv/can_an_ai_learn_cooking_and_what_it_teaches_us/?share_id=tp5uZ0xeGLxLk2EVeHlZ1&utm_content=1&utm_medium=android_app&utm_name=androidcss&utm_source=share&utm_term=1"
author: "Harshil-Jani"
published: 2026-06-04
created: 2026-06-06
description: "Curious what this sub thinks: If you were building a domain-specific agent,"
tags:
  - to-process
  - llm-foundations
---

**[r/HowToAIAgent](https://www.reddit.com/r/HowToAIAgent/)**


# [Harshil-Jani](https://www.reddit.com/user/Harshil-Jani/)



 (2026-06-04 22:28:25)

![](https://i.redd.it/02kp5qb0gb5h1.png)

I just came across a paper where researchers trained what they claim is the largest multilingual food model yet:


• 4.1M recipes  

• 7 languages  

• 1,790 ingredients  

• 300-dimensional embeddings


And the entire thing is roughly 2 MB.


Paper: <https://arxiv.org/abs/2605.22391>


What caught my attention wasn't the food angle.


It's that while the rest of the industry is racing to build agents with larger context windows, bigger vector databases, and more retrieval layers, these researchers took a different approach.


Instead of giving the model access to millions of recipes at runtime, they compressed the relationships between ingredients into a tiny representation.


They ended up with a model that can reason about ingredient similarity, substitutions, cuisine relationships, and culinary structure without carrying around 4 million recipes.


A lot of today's agent architectures look like:



```
User Query → 
Retrieve More Documents → 
Add More Context → 
Ask LLM Again

```

When an agent struggles, our first instinct is usually to give it more context. But what if the better question is: "Can we represent the domain better?"


Maybe the future isn't agents with 10 million token context windows. Maybe it's agents that operate on compact, learned representations of their world and retrieve only when necessary.


Not saying this food model directly solves that problem. But I love papers like this because they challenge the default assumption that bigger context automatically means better intelligence.


Curious what this sub thinks: If you were building a domain-specific agent, would you rather give it access to 4 million raw records or a compact world model that already understands the relationships between them?





## [AutoModerator](https://www.reddit.com/user/AutoModerator/)



 (2026-06-04 22:28:26)


Welcome to [r/HowToAIAgent](https://reddit.com/r/HowToAIAgent)!


Please make sure your post includes:
- Clear context
- What you're trying to achieve
- Any relevant links or screenshots


Feel free to join our X community:
<https://x.com/i/communities/1874065221989404893>


*I am a bot, and this action was performed automatically. Please [contact the moderators of this subreddit](https://reddit.com/message/compose/?to=/r/HowToAIAgent) if you have any questions or concerns.*





## [MrBajt](https://www.reddit.com/user/MrBajt/)



 (2026-06-05 18:17:28)


watching LLM users recreate ML research backwards is one of my favorite sources of entertainment 





### [highso](https://www.reddit.com/user/highso/)



 (2026-06-05 22:59:33)


True, but the LLM user doesn't else have the insight under the hood





## [dat\_oldie\_you\_like](https://www.reddit.com/user/dat_oldie_you_like/)



 (2026-06-05 05:47:50)


This is cool asf 





## [emsiem22](https://www.reddit.com/user/emsiem22/)



 (2026-06-05 16:47:59)


<https://huggingface.co/Kaikaku/epicure-core>