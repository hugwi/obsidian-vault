---
categories:
  - "[[Resources]]"
domain: engineering
title: "GitHub - gitpod-io/gitpod: The developer platform for on-demand cloud development"
source: "https://github.com/gitpod-io/gitpod"
author: "github.com/gitpod-io"
published: 
created: 2026-05-07
description: "The developer platform for on-demand cloud development environments to create"
tags:
  - to-process
  - dev-tools
---

# gitpod-io/gitpod


[![Gitpod banner image](https://private-user-images.githubusercontent.com/55068936/325208697-ff393a65-a4f3-4997-a066-10337562cc34.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjUyNzk5OTAsIm5iZiI6MTcyNTI3OTY5MCwicGF0aCI6Ii81NTA2ODkzNi8zMjUyMDg2OTctZmYzOTNhNjUtYTRmMy00OTk3LWEwNjYtMTAzMzc1NjJjYzM0LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTAyVDEyMjEzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWMxODdiZjJiNjUyYWVlNTJkYTAyYjllNDU3N2MxMDM3ZTdkY2ZjZDc2MWMyYzllMzE0ZGRhOGFmNmYwMzQwYzEmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.wEXBmM0dp7cx4q-GMBNo6x6Me_bnZBbtlznTX8junpc)](https://www.gitpod.io)
[![](https://private-user-images.githubusercontent.com/55068936/325218727-01a00b23-e1f5-4650-a629-89db8e300708.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjUyNzk5OTAsIm5iZiI6MTcyNTI3OTY5MCwicGF0aCI6Ii81NTA2ODkzNi8zMjUyMTg3MjctMDFhMDBiMjMtZTFmNS00NjUwLWE2MjktODlkYjhlMzAwNzA4LnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTAyVDEyMjEzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTliNjJmNDdhNDI3NDcxNzU0MzM0MTNlNWI5NmFkZjk5OGUxOTE4MTkzZTZlYTg2YzczZDc2ZDAyMjkzY2I0MmYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.YAVhB2PQiNJL6FLFCV25pBz94RHif2R4p7H6s4EzWwc)](https://www.gitpod.io#gh-light-mode-only)
[![](https://private-user-images.githubusercontent.com/55068936/325218906-ff437ec6-adda-4814-9e92-fff44cfd00ad.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjUyNzk5OTAsIm5iZiI6MTcyNTI3OTY5MCwicGF0aCI6Ii81NTA2ODkzNi8zMjUyMTg5MDYtZmY0MzdlYzYtYWRkYS00ODE0LTllOTItZmZmNDRjZmQwMGFkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTAyVDEyMjEzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM3Njc0NTdiZDk1NjViZmFhOGMzYTY4YTZiMWJhNTUyNjMzNTZhYjVmMTBkODYyMDU0YzVhM2FlZWIzY2I3NzkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.5d7y3G9-B2kJGTVetZhyYfkcB5Glb_icCoCa8LpBPV4)](https://www.gitpod.io#gh-dark-mode-only)
[Gitpod](https://www.gitpod.io)’s developer platform provides on-demand, pre-configured environments that automatically integrate into any tool, library, or dependency required for creating software. Gitpod workspaces are the fastest and most secure way to ship software and are as easy as adding a .gitpod.yml file to the root of any repository.


📄 [Read Cloud Development Environment white paper](https://www.gitpod.io/whitepaper/cde)


[![](https://private-user-images.githubusercontent.com/55068936/325210491-84beb5da-fa5b-4966-a454-8f5b2607a8ed.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjUyNzk5OTAsIm5iZiI6MTcyNTI3OTY5MCwicGF0aCI6Ii81NTA2ODkzNi8zMjUyMTA0OTEtODRiZWI1ZGEtZmE1Yi00OTY2LWE0NTQtOGY1YjI2MDdhOGVkLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTAyVDEyMjEzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWI1YzU0NjlkMjVmODM5Yzc4NGNjMDk3YmZiNzliZTYxN2YzMzI4NTA1YmViMTk2Yjk2MWQ1NjNkZTg3NmNmN2EmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.RrNKnQt-R7lWrvtxgx8txJrNzqENK651YhNxsi6N_r8)](https://www.gitpod.io#gh-light-mode-only)
[![](https://private-user-images.githubusercontent.com/55068936/325218179-3912a60a-65a9-45f2-b151-93621ac8bf53.jpg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjUyNzk5OTAsIm5iZiI6MTcyNTI3OTY5MCwicGF0aCI6Ii81NTA2ODkzNi8zMjUyMTgxNzktMzkxMmE2MGEtNjVhOS00NWYyLWIxNTEtOTM2MjFhYzhiZjUzLmpwZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA5MDIlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwOTAyVDEyMjEzMFomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTkwYTI1MTgzYzYzNzMwNmI2OGRiMzYzMGU4YTEzOGJhN2I4NTQ1ZjY2Yjg0MTI3ZWZmMmYyYjk5OWM1ZmRmNDgmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.bemppIgEH80yh0mmKMisNoyOXX2TmarAV7bAFscvmFk)](https://www.gitpod.io#gh-dark-mode-only)
## Features


* **Dev environments as code** - Gitpod is like infrastructure-as-code, but for your development environment. Gitpod defines your editor extensions and requires dependencies in a declarative [`.gitpod.yml` configuration](https://www.gitpod.io/docs/introduction/gitpod-tutorial/2-configure-your-gitpod-yml). Spinning up dev environments is easily repeatable and reproducible empowering you to automate, version-control, and share dev environments across your team.
* [**Prebuilt dev environments**](https://www.gitpod.io/docs/configure/projects/prebuilds) - Gitpod continuously prebuilds all your git branches similar to a CI server. Control how Gitpod pre-configures and initializes environments before you even start a workspace through tasks commands in your .gitpod.yml. No more watching apt-get or npm install again.
* [**Secure**](https://www.gitpod.io/security) - Each Gitpod workspace or prebuild runs on a secured single-use container providing fast startup times without compromising on security. Gitpod generates SLSA level 1 compliant provenance. Gitpod is also GDPR and SOC2 compliant. And, of course, Gitpod is open-source and available for review by everyone.
* **Workspaces based on Docker** - Gitpod instantly starts a container in the cloud based on an (optional) [Docker image](https://www.gitpod.io/docs/config-docker/). If you’re already using Docker, you can easily re-use your Docker file.
* **GitLab, GitHub, and Bitbucket integration** - Gitpod seamlessly [integrates](https://www.gitpod.io/docs/configure/authentication) into your workflow and works with all major Git hosting platforms including GitHub, GitLab, and Bitbucket.
* **Integrated code reviews** - with Gitpod you can do native code reviews on any PR/MR. No need to switch contexts anymore and clutter your local machine with your colleagues' PR/MR.
* **Collaboration** - invite team members to your dev environment or snapshot of any state of your dev environment to share it with your team asynchronously. **Professional & customizable developer experience** - a Gitpod workspace gives you the same capabilities as your Linux machine - pre-configured and optimized for your development workflow. Install any [VS Code extension](https://www.gitpod.io/docs/references/ides-and-editors/vscode-extensions) with one click on a user and/or team level. You can also bring your [dotfiles](https://www.gitpod.io/docs/configure/user-settings/dotfiles#dotfiles) and customize your dev environment as you like.


## Getting Started


* **Browser**:
	+ Using Gitpod dashboard [gitpod.io/new](https://gitpod.io/new).
	+ Add `gitpod.io/#` as a prefix to any of your GitHub/ GitLab/ Bitbucket repository, like [this](https://gitpod.io/#https://github.com/gitpod-io/template-typescript-react)
* **CLI**: You can also [install Gitpod CLI](https://www.gitpod.io/docs/references/gitpod-cli#installation) and create your first workspace directly from your terminal :)


## Documentation


All documentation can be found on [www.gitpod.io/docs](https://www.gitpod.io/docs). For example, see [Gitpod tutorial](https://www.gitpod.io/docs/introduction/gitpod-tutorial) and check the following helpful resources:


* [Workspace Lifecycle](https://www.gitpod.io/docs/configure/workspaces/workspace-lifecycle)
* [Configure repositories](https://www.gitpod.io/docs/configure/repositories)
* [Organizations](https://www.gitpod.io/docs/configure/orgs)
* [IDE & Editors support](https://www.gitpod.io/docs/references/ides-and-editors)
* [Video screencasts](https://www.gitpod.io/screencasts)
* [Gitpod samples](https://github.com/gitpod-samples)


## Questions


For questions and support please use [Gitpod community Discord](https://www.gitpod.io/chat). Join the conversation, and connect with other community members. 💬 You can also follow [@gitpod](https://twitter.com/gitpod) for announcements and updates from our team.


For enterprise deployment and customized solutions, please explore our [**Enterprise offerings**](https://www.gitpod.io/contact/enterprise-self-serve) to get started with a setup that meets your organization's needs.


## Issues


The issue tracker is used for tracking bug reports and feature requests for the Gitpod open source project as well as planning current and future development efforts. 🗺️


You can upvote popular feature requests or create a new one.


## Related Projects


During the development of Gitpod, we also developed some of our infrastructure toolings to make development easier and more efficient. To this end, we've developed many open-source projects including:


* [Workspace images](https://github.com/gitpod-io/workspace-images): Ready to use docker images for Gitpod workspaces
* [OpenVSCode Server](https://github.com/gitpod-io/openvscode-server): Run the latest VS Code on a remote machine accessed through a browser
* [Gitpod browser extension](https://github.com/gitpod-io/browser-extension): It adds a Gitpod button to the configured GitLab, GitHub and Bitbucket installations
* [Leeway](https://github.com/gitpod-io/leeway) - A heavily caching build system
* [Dazzle](https://github.com/gitpod-io/dazzle) - An experimental Docker image builder
* [Werft](https://github.com/csweichel/werft) - A Kubernetes native CI system


## Code of Conduct


We want to create a welcoming environment for everyone interested in contributing to Gitpod or participating in discussions with the Gitpod community. This project has adopted the [Contributor Covenant Code of Conduct](https://github.com/gitpod-io/.github/blob/main/CODE_OF_CONDUCT.md), [version 2.0](https://www.contributor-covenant.org/version/2/0/code_of_conduct/).