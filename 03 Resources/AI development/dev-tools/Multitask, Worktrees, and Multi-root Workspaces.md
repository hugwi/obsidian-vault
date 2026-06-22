---
title: "Multitask, Worktrees, and Multi-root Workspaces"
source: "https://cursor.com/changelog/04-24-26"
author:
  - "[[cursor.com]]"
published: 2026-04-24
created: 2026-06-07
description:
tags:
  - "to-process"
  - dev-tools
---
3.2 

This release introduces a new way to multitask with async subagents, an improved worktrees experience, and multi-root workspaces for making cross-repo changes.

## Multitask in Agents Window

With `/multitask`, Cursor will run async subagents to parallelize your requests instead of adding them to the queue. It will also break down larger tasks into smaller chunks for a fleet of async subagents to tackle simultaneously.

If you already have messages in the queue, you can ask Cursor to multitask on them instead of waiting for the current run to finish.

 <video src="blob:https://cursor.com/ca3c41f0-b3c7-4e0b-8374-6d1b7e8c507c" controls=""><track kind="metadata" label="cuepoints"> <track kind="chapters" label="chapters" src=""></video>

## Worktrees in Agents Window

We've added new and improved [worktrees](https://cursor.com/docs/configuration/worktrees) in the [Agents Window](https://cursor.com/docs/agent/agents-window).

Run isolated tasks in the background across different branches. When you're ready to test changes, move any branch into your local foreground with one click.

 <video src="blob:https://cursor.com/8a2445ec-f0d9-44e5-9953-5de542acc9f0" controls=""><track kind="metadata" label="cuepoints"> <track kind="chapters" label="chapters" src=""></video>

## Multi-root workspaces in Agents Window

A single agent session can now target a reusable workspace made of multiple folders.

This allows Cursor to make cross-repo changes spanning frontend, backend, and shared libraries, without retargeting the agent every time it moves between repos.

 <video src="blob:https://cursor.com/63a2a885-8c6f-4ad9-8f4c-dc389b5570d8" controls=""><track kind="metadata" label="cuepoints"> <track kind="chapters" label="chapters" src=""></video>