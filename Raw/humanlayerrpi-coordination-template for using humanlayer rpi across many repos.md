---
categories:
  - "[[Raw]]"
title: "humanlayer/rpi-coordination-template: for using humanlayer rpi across many repos"
source: "https://github.com/humanlayer/rpi-coordination-template"
author:
published:
created: 2026-09-01
description: "for using humanlayer rpi across many repos . Contribute to humanlayer/rpi-coordination-template development by creating an account on GitHub."
tags:
  - "raw"
---
## coordination repo

⚠️

NOTE - if you are using humanlayer and have found your way to this repo, it is very possible that the [Workspaces feature](https://docs.humanlayer.com/guide/workspaces) obviates the need for a standalone repo, or at least the claude config and additionalRepos part of it. You may still want this setup for shared AGENTS.md, skills, etc.

### Setup

1. create a new repo from this template
2. Clone this repo as a sibling to all your other repos:

```markdown
~/src
  - repo1
  - repo2
  - rpi-coordination
```

3. edit.claude/settings.json to list out all repos you want to work on
```prolog
{
  "permissions": {
    "additionalDirectories": [
      "../repo1",
      "../repo2"
      ]
  }
}
```
4. edit CLAUDE.md to add list of repos and brief descriptions

replace this placeholder text in the markdown file:

```gradle
This is a coordination repo for multiple repositories. The repos you have access to are:

- ../repo1 - [DESCRIPTION]
- ../repo2 - [DESCRIPTION]
```

### Instructions

Run all your sessions from here