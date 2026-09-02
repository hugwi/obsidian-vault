---
title: "Spec-driven development is not one thing. There are three levels."
source: "x"
url: "https://x.com/simas_ch/status/2093232215966503399"
author: "Simon Martinelli"
published: "Fri Aug 28 07:00:25 +0000 2026"
created: "2026-08-28"
categories:
  - "[[Raw]]"
action: "review"
read: "false"
rating: ""
tags:
  - "clip/x"
  - "spec-driven-development"
  - "ai-unified-process"
  - "requirements-engineering"
  - "software-architecture"
  - "brownfield-systems"
summary: "Spec-driven development is not one thing. There are three levels."
theme:
  - "comprehension-maintainability"
  - "workflow-phases-gates"
  - "productivity-measurement"
subtheme:
  - "spec-first"
  - "spec-anchored"
  - "spec-as-source"
domain: "agentic-engineering"
---

# Spec-driven development is not one thing. There are three levels.

> Saved from X on 2026-08-28. Author: Simon Martinelli.

Spec-driven development is not one thing. There are three levels.

Birgitta Böckeler from Thoughtworks describes them in her article:

Spec-first: write a spec, generate the code, throw the spec away.
Spec-anchored: the spec stays in the repository and evolves with the code.
Spec-as-source: humans only edit the spec, the code is regenerated.

Where are the tools?

Kiro and spec-kit are spec-first.
BMad is spec-first with good planning documents on top.
OpenSpec is spec-anchored, with delta specs that merge into the main specs.

And the AI Unified Process? Also spec-anchored.

Requirements, use case specifications, and the entity model live next to the code for the whole life of the system. Tests are linked to use cases with @UseCase. Change the spec first, then the agent changes the code.

I rarely type code myself anymore. So is this level 3? No, and on purpose. The code is not regenerated, the agent evolves it. That is the only way brownfield works. Nobody regenerates a 15-year-old ERP from a spec.

You get most of the productivity of level 3 without depending on a non-deterministic compiler. And you keep a team that understands its own system.

Full article: https://t.co/W8y1zxThXt

#SpecDrivenDevelopment #AIUnifiedProcess #RequirementsEngineering #SoftwareArchitecture
