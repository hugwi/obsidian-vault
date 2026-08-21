---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - evals
  - skills
source: readwise
created: 2026-06-23
rating: 
action: 
theme: quality-gates
subtheme:
  - evals
---

# GitHub - hamelsmu/evals-skills: Skills for AI Evals to compliment the course: AI Evals For Engineers & PMs · GitHub

![rw-book-cover](https://opengraph.githubassets.com/c0b90134f1e718007438508ced814369522cfcad8462813aebc4d064266d1d70/hamelsmu/evals-skills)

## Metadata
- Author: [[https://github.com/hamelsmu/]]
- Full Title: GitHub - hamelsmu/evals-skills: Skills for AI Evals to compliment the course: AI Evals For Engineers & PMs · GitHub
- Category: #articles
- Summary: This GitHub repo offers skills to help AI coding agents build and improve LLM evaluations. It includes tools like eval-audit to find common problems and recommends fixes. Users can install the plugin, use available skills, and create custom ones tailored to their projects.
- URL: https://github.com/hamelsmu/evals-skills

## Full Document
### hamelsmu/evals-skills

main

Go to file

Code

Open more actions menu

### Eval Skills for AI Coding Agents

Skills that guide AI coding agents to help you build LLM evaluations.

These skills guard against common mistakes I've seen helping 50+ companies and teaching students in our [AI Evals course](https://maven.com/parlance-labs/evals?promoCode=evals-info-url). If you're new to evals, see [questions.md](https://github.com/hamelsmu/evals-skills/blob/main/questions.md) for free resources on the fundamentals.

#### New to Evals? Start Here

If you are new to evals or aren't a student in our course, start with the `eval-audit` skill. Give your coding agent these instructions:

>  Install the eval skills plugin from <https://github.com/hamelsmu/evals-skills>, then run /evals-skills:eval-audit on my eval pipeline. Investigate each diagnostic area using a separate subagent in parallel, then synthesize the findings into a single report. Use other skills in the plugin as recommended by the audit.
> 
>  

The audit isn't a complete solution, but it will catch common problems we've seen in evals. It will also recommend other skills to use to fix the problems.

#### Installation

In Claude Code, run these two commands:

```
# Step 1: Register the plugin repository
/plugin marketplace add hamelsmu/evals-skills

# Step 2: Install the plugin
/plugin install evals-skills@hamelsmu-evals-skills
```

To upgrade:

```
/plugin update evals-skills@hamelsmu-evals-skills
```

After installation, restart Claude Code. The skills will appear as `/evals-skills:<skill-name>`.

#### Available Skills

| Skill | What it does |
| --- | --- |
| eval-audit | Audit an eval pipeline and surface problems with prioritized severity |
| error-analysis | Guide the user through reading traces and categorizing failures |
| generate-synthetic-data | Create diverse synthetic test inputs using dimension-based tuple generation |
| write-judge-prompt | Design LLM-as-Judge evaluators for subjective quality criteria |
| validate-evaluator | Calibrate LLM judges against human labels using data splits, TPR/TNR, and bias correction |
| evaluate-rag | Evaluate retrieval and generation quality in RAG pipelines |
| build-review-interface | Build custom annotation interfaces for human trace review |

Invoke a skill with `/evals-skills:skill-name`, e.g., `/evals-skills:error-analysis`.

#### Write Your Own Skills

These skills are a starting point and only encode common mistakes that generalize across projects. Skills grounded in your stack, your domain, and your data will outperform them. Start here, then write your own.

The [meta-skill](https://github.com/hamelsmu/evals-skills/blob/main/meta-skill.md) can help you ground custom skills. It works best alongside the context provided in the course.

#### Beyond These Skills

These skills handle the parts of eval work that generalize across projects. Much of the process doesn't: production monitoring, CI/CD integration, data analysis, and much more. The [course](https://maven.com/parlance-labs/evals?promoCode=evals-info-url) covers all of it.
