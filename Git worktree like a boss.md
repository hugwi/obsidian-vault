---
categories:
  - "[[Resources]]"
domain: engineering
title: "Git worktree like a boss"
source: "https://dev.to/metal3d/git-worktree-like-a-boss-2j1b"
author:
  - "[[dev.to]]"
published: 2026-03-18
created: 2026-06-08
description: "If there’s one Git tool that few people know about, it’s “worktree.” Once you’ve mastered this tool,... Tagged with git, devops, development."
tags:
  - "to-process"
  - dev-tools
---
If there’s one Git tool that few people know about, it’s “worktree.” Once you’ve mastered this tool, you’ll find it incredibly hard to do without it. But you have to use it the right way. Here’s a method I’ve been using for a very long time

## TL;DR

In an empty directory:

```
# 1. Clone the repo into a hidden .bare folder
git clone --bare git@github.com:user/repo.git .bare

# 2. Tell the root folder where the Git history is hidden
echo "gitdir: ./.bare" > .git

# 3. Fix the fetch configuration to see all remote branches
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

# 4. Create your first worktree (the main branch)
git worktree add main
git worktree add <name of the branch>

# Each folder correspond to a branch, everything is centralized
# Read the doc... or follow the article
```

> I provide you a script you can put in your `PATH` to ease the process. Take a look at the end of the article.

## First of all, what is a “worktree”?

In the fast-paced world of software development, **context switching** is often an unavoidable reality. You’ve likely been there: you’re deep into a complex feature branch when a critical production bug suddenly demands your immediate attention.

Or, sometimes, you have to manage 2 branches at the same time because you are preparing a big migration, refactoring or something complex that will be merged. So you need direct to several "working trees".

Traditionally, developers have relied on git stash to clear their workspace or simply cloned the entire repository into a separate folder. However, these methods can be clunky, error-prone, or heavy on disk space. This is where Git Worktree comes in.

Introduced in version 2.5, git worktree allows you to have **multiple working directories attached to a single repository**. Instead of having just one "checked out" branch at a time, you can have several branches checked out simultaneously in different folders. All these folders share the same underlying.git history, meaning you don't need to re-download data or deal with multiple independent clones.

You will understand why it's so powerful as soon as you will follow my method 😄

## The bad way

I often see articles that explains you can do a worktree using `"../name-of-worktree"`. That works and I can understand why it's the "common way to do". The developper has already cloned the repository and it does this to quickly have a second workspace for a branch.

But... it's not what I advice.

## How to do better

What I do for a long time now is to use a "bare" clone. This will not clone the repository but an history of the répository. So, after the below command, you are not ready to work. Let's take an example with my project:

```
mkdir -p ~/Projects/Katenary
cd ~/Projects/Katenary
git clone --bare git@repo.katenary.io:Katenary/katenary.git .bare
```

In the `.bare` directory, you'll see something like:

```
.bare
├── config
├── description
├── HEAD
├── hooks
├── info
├── objects
├── packed-refs
└── refs
```

When you use the Bare Clone method, you want your root project folder to stay clean. The goal is to have a hidden administrative folder and then your various worktrees (branches) as sibling folders.

Here is the "magic trick" to make the root folder behave like a Git repository without actually cluttering it:

```
echo "gitdir: ./.bare" > .git
```

By default, if you are inside your project folder but outside a worktree, Git won't know where the history is. By adding this one-line.git file, you are telling your terminal: "Treat this entire directory as part of the Git project located in./bare."

This allows you to run git worktree commands from the root of your project instead of having to cd into the.bare folder every time. It’s the glue that holds the "Pro" structure together.

> And now, ladies and gentlemen!

```
# I will explain this line in a few moments
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

# let's start to work on different branches
git worktree add main
git worktree add feature/better-depends-on
```

This makes:

```
.
├── feature
│   └── better-depends-on
└── main
```

I now see 2 folders, `main` and `better-dependencies`. Each directory contains the content of the desired branch. I can work in both of them, push, pull, and so on.

## The "Blind Clone" Trap: Why Your Fetch is Empty

If you've followed the steps so far, you might run into a confusing situation. You try to add a worktree **for an existing remote branch**, but Git instead creates a new, empty branch starting from main.

Look at your terminal. If git fetch only shows this:

```
git fetch
* branch            HEAD       -> FETCH_HEAD
```

> You are officially "Blind."

**Your local repository knows the code exists, but it has no idea that other branches exist on the server**.

When you use git clone --bare, Git assumes you want a backup or a server-side mirror, not a workspace for active development. To save resources, it doesn't set up "Remote Tracking." It only fetches the default branch (main or master).

**The Fix: Mapping the Remote**  
To turn your bare repository into a fully-aware development hub, you need to tell Git: "I want to see everything that happens on the origin server."

Run this command:

```
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"
```

Now, run git fetch --all again. You should see a list of all your teammates' branches appearing in your terminal.

## Wait... it's only like having cloned twice, right?

At first glance, you might think: "Why go through all this trouble? If I need to work on two branches at once, I’ll just clone the repo into two different folders and be done with it."

Technically, you could. But comparing a Git Worktree setup to multiple clones is like comparing a synchronized multi-room audio system to buying two separate stereos and trying to press "Play" at the exact same millisecond.

Here is why the "Multiple Clones" method is actually a trap:

### 1\. The Storage Tax

If your repository is 500MB, two clones take up 1GB. With Worktrees, you have one.git folder (the "source of truth"). Each additional worktree only adds the weight of the actual text files you are editing. Your disk will thank you.

### 2\. The "Single Source of Truth" Problem

**This is the real game-changer**. In a multi-clone setup:

- If you git fetch in Clone A, Clone B knows nothing about it.
- If you create a local branch in Clone A, you have to push it to the server (or a local remote) just to see it in Clone B.

With Worktrees, **they all share the same internal database**. If you fetch in your main worktree, the new branches are instantly available in your feature-xyz worktree. It’s one brain, many bodies.

### 3\. Hooks and Configs

Ever spent 20 minutes setting up a specific Git hook or a local config, only to realize you have to do it all over again because you're in a different clone?

Since Worktrees share the same.git directory, **your hooks, aliases, and local configurations are universal** across all your working folders.

### 4\. The "Safety Valve"

Git is smart: it won't let you check out the same branch in two different worktrees at the same time. This prevents you from accidentally overwriting your own work or creating massive HEAD conflicts—a protection you don't have if you're just using multiple clones.

> In short: Multiple clones are isolated silos. Worktrees are a unified workspace.

## The "pro" setup

```
# 1. Clone the repo into a hidden .bare folder
git clone --bare git@github.com:user/repo.git .bare

# 2. Tell the root folder where the Git history is hidden
echo "gitdir: ./.bare" > .git

# 3. Fix the fetch configuration to see all remote branches
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

# 4. Create your first worktree (the main branch)
git worktree add main
```

And now, a if you're in the "main" folder, an urgent hotfix must be done.

```
# inside the "main" directory
git worktree add ../hotfix
cd ../hotfix
```

This create a branch **and** the folder where you can work without having to stop working on "main" branch.

To be explicit:

```
git worktree add <where to create the tree> [-b name of the branch to create] [branch name reference]
```

For example, I need to create "feature/fix-db" from "feature/improve-db". I'm in the root workspace:

```
git worktree add improve-db -b feeature/fix-db feature/improve-db
```

The directory is created, I can now go to "`./improve-db` " and do my job.

Of course, you can use subdirectories (place all features in a `features` directory) and git worktree create them by default if you use slashes in your branchnames. I mean that `git worktree add features/A` creates `features/A` directory. And the branch is named this way, and ready to be pushed.

## Some traps

Removing a worktree with "rm -rf" doesn't really remove the worktree (no panic, it doesn't remove remote branches). Then if you want to get it back, you will think that "git worktree add" one more time will respawn the directory. But, an error will appear saying that the worktree already exists.

Is this is the case, you can do:

```
git worktree list
```

You will see "prunable" worktrees. You can then prune them:

```
git worktree prune
```

Then, you can use the `add` subcommand.

You can protect worktrees to not being pruned with the "lock" subcommand, and of course "unlock" it at any time.

## Conclusion: Give it a Week

I’ll be honest: if you’ve been using git stash and multiple clones for years, the Git Worktree workflow might feel like "over-engineering" a problem you don't think you have. It’s hard to see the immediate value when you're used to the friction of traditional context switching.

> But here is my challenge to you: Try it for a week.

Force yourself to use a Bare Clone setup on your next big project. The moment you realize you can run a heavy test suite in one folder while simultaneously hotfixing a bug in another—without ever losing your place or your "flow"—it will click.

You’ll stop thinking about "switching branches" and start thinking about "parallel workspaces." Your terminal will be cleaner, your disk space will be optimized, and your brain will thank you for not having to remember what you stashed three hours ago.

**Once you go Worktree, you rarely go back.**

## A simple script

I placed this in my `~/.local/bin` folder named `wtree` (don't forget to `chmod +x wtree`):

```bash
#!/bin/bash

# Usage: wtree <git url> (in an empty directory)

REPO_URL=$1
SCRIPT_NAME=$(basename "$0")

if [ -z "$REPO_URL" ]; then
    echo "❌ Error: Missing repository URL."
    echo "Usage: $0 <repo-url>"
    exit 1
fi

# 1. Check if the current directory is empty
# We allow the script itself to be present
FILES_IN_DIR=$(ls -A | grep -v "$SCRIPT_NAME")

if [ ! -z "$FILES_IN_DIR" ]; then
    echo "❌ Error: Current directory is not empty!"
    echo "To keep your worktree setup clean, please run this in a fresh folder."
    exit 1
fi

echo "🚀 Initializing Pro Git Worktree setup..."

# 2. Clone as bare into a hidden directory
git clone --bare "$REPO_URL" .bare

# 3. Link the root to the bare repository
echo "gitdir: ./.bare" > .git

# 4. Enable remote tracking (The "Remote Awareness" fix)
# This ensures 'git fetch' sees all branches from the server
git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

# 5. Fetch everything
git fetch --all

echo "✅ Setup complete!"
echo "Next step: git worktree add main"
```

DEV Community

[![Google AI Education track image](https://media2.dev.to/dynamic/image/width=775%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fu09y9fffqrb2one15j3g.png)](https://dev.to/deved/build-apps-with-google-ai-studio?bb=238781)

## Build Apps with Google AI Studio 🧱

This track will guide you through Google AI Studio's new "Build apps with Gemini" feature, where you can turn a simple text prompt into a fully functional, deployed web application in minutes.