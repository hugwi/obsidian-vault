---
title: "Let Claude use your computer from the CLI"
source: "https://code.claude.com/docs/en/computer-use"
author: "Claude Code Docs"
published: 
created: 2026-04-02
description: "Enable computer use in the Claude Code CLI so Claude can open apps, click,"
tags:
  - to-process
  - dev-tools
---

Computer use is a research preview on macOS that requires a Pro or Max plan. It is not available on Team or Enterprise plans. It requires Claude Code v2.1.85 or later and an interactive session, so it is not available in non-interactive mode with the `-p` flag.


Computer use lets Claude open apps, control your screen, and work on your machine the way you would. From the CLI, Claude can compile a Swift app, launch it, click through every button, and screenshot the result, all in the same conversation where it wrote the code. This page covers how computer use works in the CLI. For the Desktop app, see [computer use in Desktop](https://code.claude.com/docs/en/desktop#let-claude-use-your-computer). Computer use handles tasks that require a GUI: anything you’d normally have to leave the terminal and do by hand.


* **Build and validate native apps**: ask Claude to build a macOS menu bar app. Claude writes the Swift, compiles it, launches it, and clicks through every control to verify it works before you ever open it.
* **End-to-end UI testing**: point Claude at a local Electron app and say “test the onboarding flow.” Claude opens the app, clicks through signup, and screenshots each step. No Playwright config, no test harness.
* **Debug visual and layout issues**: tell Claude “the modal is clipping on small windows.” Claude resizes the window, reproduces the bug, screenshots it, patches the CSS, and verifies the fix. Claude sees what you see.
* **Drive GUI-only tools**: interact with design tools, hardware control panels, the iOS Simulator, or proprietary apps that have no CLI or API.


 Claude has several ways to interact with an app or service. Computer use is the broadest and slowest, so Claude tries the most precise tool first:


* If you have an [MCP server](https://code.claude.com/docs/en/mcp) for the service, Claude uses that.
* If the task is a shell command, Claude uses Bash.
* If the task is browser work and you have [Claude in Chrome](https://code.claude.com/docs/en/chrome) set up, Claude uses that.
* If none of those apply, Claude uses computer use.


Screen control is reserved for things nothing else can reach: native apps, simulators, and tools without an API. Computer use is available as a built-in MCP server called `computer-use`. It’s off by default until you enable it.


The first time Claude tries to use your computer, you’ll see a prompt to grant two macOS permissions:


* **Accessibility**: lets Claude click, type, and scroll
* **Screen Recording**: lets Claude see what’s on your screen


The prompt includes links to open the relevant System Settings pane. Grant both, then select **Try again** in the prompt. macOS may require you to restart Claude Code after granting Screen Recording.


After setup, ask Claude to do something that needs the GUI: Enabling the `computer-use` server doesn’t grant Claude access to every app on your machine. The first time Claude needs a specific app in a session, a prompt appears in your terminal showing:


* Which apps Claude wants to control
* Any extra permissions requested, such as clipboard access
* How many other apps will be hidden while Claude works


Choose **Allow for this session** or **Deny**. Approvals last for the current session. You can approve multiple apps at once when Claude requests them together. Apps with broad reach show an extra warning in the prompt so you know what approving them grants: These apps aren’t blocked. The warning lets you decide whether the task warrants that level of access. Claude’s level of control also varies by app category: browsers and trading platforms are view-only, terminals and IDEs are click-only, and everything else gets full control. See [app permissions in Desktop](https://code.claude.com/docs/en/desktop#app-permissions) for the complete tier breakdown. Computer use holds a machine-wide lock while active. If another Claude Code session is already using your computer, new attempts fail with a message telling you which session holds the lock. Finish or exit that session first. When Claude starts controlling your screen, other visible apps are hidden so Claude interacts with only the approved apps. Your terminal window stays visible and is excluded from screenshots, so you can watch the session and Claude never sees its own output. When Claude finishes the turn, hidden apps are restored automatically. When Claude acquires the lock, a macOS notification appears: “Claude is using your computer · press Esc to stop.” Press `Esc` anywhere to abort the current action immediately, or press `Ctrl+C` in the terminal. Either way, Claude releases the lock, unhides your apps, and returns control to you. A second notification appears when Claude is done. The built-in guardrails reduce risk without requiring configuration:


* **Per-app approval**: Claude can only control apps you’ve approved in the current session.
* **Sentinel warnings**: apps that grant shell, filesystem, or system settings access are flagged before you approve.
* **Terminal excluded from screenshots**: Claude never sees your terminal window, so on-screen prompts in your session can’t feed back into the model.
* **Global escape**: the `Esc` key aborts computer use from anywhere, and the key press is consumed so prompt injection can’t use it to dismiss dialogs.
* **Lock file**: only one session can control your machine at a time.


 After making changes to a macOS or iOS app, have Claude compile and verify in one pass: Claude runs `xcodebuild`, launches the app, interacts with the UI, and reports what it finds. Claude resizes the window, captures the broken state, and reads the relevant stylesheets. Claude controls the simulator the same way you would with a mouse. The CLI and Desktop surfaces share the same computer use engine. A few Desktop-specific controls aren’t yet in the CLI:




| Feature | Desktop | CLI |
| --- | --- | --- |
| Enable | Toggle in **Settings > Desktop app > General** | Enable `computer-use` in `/mcp` |
| Denied apps list | Configurable in Settings | Not yet available |
| Auto-unhide toggle | Optional | Always on |
| Dispatch integration | Dispatch-spawned sessions can use computer use | Not applicable |


 Another Claude Code session holds the lock. Finish the task in that session or exit it. If the other session crashed, the lock is released automatically when Claude detects the process is no longer running. macOS sometimes requires a restart of the requesting process after you grant Screen Recording. Quit Claude Code completely and start a new session. If the prompt persists, open **System Settings > Privacy & Security > Screen Recording** and confirm your terminal app is listed and enabled. 


* You’re on macOS. Computer use is not available on Linux or Windows.
* You’re running Claude Code v2.1.85 or later. Run `claude --version` to check.
* You’re on a Pro or Max plan. Run `/status` to confirm your subscription.
* You’re authenticated through claude.ai. Computer use is not available with third-party providers like Amazon Bedrock, Google Cloud Vertex AI, or Microsoft Foundry. If you access Claude exclusively through a third-party provider, you need a separate claude.ai account to use this feature.
* You’re in an interactive session. Computer use is not available in non-interactive mode with the `-p` flag.