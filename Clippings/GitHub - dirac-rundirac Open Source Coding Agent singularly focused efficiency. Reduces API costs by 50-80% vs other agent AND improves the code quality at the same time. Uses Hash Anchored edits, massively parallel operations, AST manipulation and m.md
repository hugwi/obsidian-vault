---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, ai-agents]
tags:
  - code-quality
  - efficiency
  - tools
source: readwise
created: 2026-06-23
rating: 
action: 
theme: context-engineering
subtheme:
  - cost-tokens
  - compaction-caching
---

# GitHub - dirac-run/dirac: Open Source Coding Agent singularly focused efficiency. Reduces API costs by 50-80% vs other agent AND improves the code quality at the same time. Uses Hash Anchored edits, massively parallel operations, AST manipulation and many many other optimizations. https://dirac.run/ · GitHub

![rw-book-cover](https://repository-images.githubusercontent.com/1202290616/3387b54d-bb91-4e2a-a35b-b933836bafad)

## Metadata
- Author: [[https://github.com/dirac-run/]]
- Full Title: GitHub - dirac-run/dirac: Open Source Coding Agent singularly focused efficiency. Reduces API costs by 50-80% vs other agent AND improves the code quality at the same time. Uses Hash Anchored edits, massively parallel operations, AST manipulation and many many other optimizations. https://dirac.run/ · GitHub
- Category: #articles
- Summary: Dirac is an open-source AI coding agent that edits code precisely and efficiently, cutting API costs by 64.8%. It works with multiple files at once and understands code structure to make accurate changes. You can install it as a VS Code extension or use it from the command line to automate coding tasks.
- URL: https://github.com/dirac-run/dirac

## Full Document
### dirac-run/dirac

master

Go to file

Code

Open more actions menu

### Dirac - Accurate & Highly Token Efficient Open Source AI Agent

It is a well studied phenomenon that any given model's reasoning ability degrades with the context length. If we can keep context tightly curated, we improve both accuracy and cost while making larger changes tractable in a single task.

Dirac is an open-source coding agent built with this in mind. It reduces API costs by **64.8%** on average while producing better and faster work. Using hash-anchored parallel edits, AST manipulation, and a suite of advanced optimizations.

#### 📊 Evals

Dirac is benchmarked against other leading open-source agents on complex, real-world refactoring tasks. Dirac consistently achieves 100% accuracy at a fraction of the cost. These evals are run on public github repos and should be reproducible by anyone.

| Task (Repo) | Files\* | Cline | Kilo | Ohmypi | Opencode | Pimono | Roo | **Dirac** |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Task1 ([transformers](https://github.com/huggingface/transformers)) | 8 | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_DynamicCache) [$0.37] | 🔴 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_DynamicCache_FAILURE) [N/A] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_DynamicCache) [$0.24] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_DynamicCache) [$0.20] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_DynamicCache) [$0.34] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_DynamicCache) [$0.49] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_DynamicCache) [$0.13]** |
| Task2 ([vscode](https://github.com/microsoft/vscode)) | 21 | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_IOverlayWidget) [$0.67] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_IOverlayWidget) [$0.78] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_IOverlayWidget) [$0.63] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_IOverlayWidget) [$0.40] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_IOverlayWidget) [$0.48] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_IOverlayWidget) [$0.58] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_IOverlayWidget) [$0.23]** |
| Task3 ([vscode](https://github.com/microsoft/vscode)) | 12 | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_addLogging) [$0.42] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_addLogging) [$0.70] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_addLogging) [$0.64] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_addLogging) [$0.32] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_addLogging) [$0.25] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_addLogging) [$0.45] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_addLogging) [$0.16]** |
| Task4 ([django](https://github.com/django/django)) | 14 | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_datadict) [$0.36] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_datadict) [$0.42] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_datadict) [$0.32] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_datadict) [$0.24] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_datadict) [$0.24] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_datadict) [$0.17] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_datadict) [$0.08]** |
| Task5 ([vscode](https://github.com/microsoft/vscode)) | 3 | 🔴 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_extensionswb_service_FAILURE) [N/A] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_extensionswb_service) [$0.71] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_extensionswb_service) [$0.43] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_extensionswb_service) [$0.53] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_extensionswb_service) [$0.50] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_extensionswb_service) [$0.36] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_extensionswb_service) [$0.17]** |
| Task6 ([transformers](https://github.com/huggingface/transformers)) | 25 | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_latency) [$0.87] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_latency_WRONG) [$1.51] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_latency) [$0.94] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_latency) [$0.90] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_latency) [$0.52] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_latency) [$1.44] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_latency) [$0.34]** |
| Task7 ([vscode](https://github.com/microsoft/vscode)) | 13 | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_sendRequest_2missing) [$0.51] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_sendRequest) [$0.77] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_refactor_sendRequest) [$0.74] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_sendRequest) [$0.67] | 🟡 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_refactor_sendRequest) [$0.45] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_sendRequest) [$1.05] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_sendRequest) [$0.25]** |
| Task8 ([transformers](https://github.com/huggingface/transformers)) | 3 | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/cline/cline_refactor_stoppingcriteria) [$0.25] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/kilo/kilo_code_refactor_stoppingcriteria) [$0.19] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/ohmypi/ohmypi_code_refactor_stoppingcriteria) [$0.17] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/opencode/opencode_refactor_stoppingcriteria) [$0.26] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/pimono/pimono_code_refactor_stoppingcriteria) [$0.23] | 🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/roo/roo_code_refactor_stoppingcriteria) [$0.29] | **🟢 [(diff)](https://github.com/dirac-run/dirac/blob/master/evals/dirac/dirac_refactor_stoppingcriteria) [$0.12]** |
| **Total Correct** |  | 5/8 | 5/8 | 6/8 | 8/8 | 6/8 | 6/8 | **8/8** |
| **Avg Cost** |  | $0.49 | $0.73 | $0.51 | $0.44 | $0.38 | $0.60 | **$0.18** |

>  🟢 Success | 🟡 Incomplete | 🔴 Failure
> 
>  

>  **Cost Comparison**: Dirac is **64.8% cheaper** than the competition (a **2.8x** cost reduction).
> 
>  \* Expected number of files to be modified/created to complete the task.
> 
>  See [evals/README.md](https://github.com/dirac-run/dirac/blob/master/evals/README.md) for detailed task descriptions and methodology.
> 
>  

#### 🚀 Key Features

* **Hash-Anchored Edits**: Dirac uses stable line hashes to target edits with extreme precision, avoiding the "lost in translation" issues of traditional line-number based editing. [![Hash-Anchored Edits](https://camo.githubusercontent.com/7c2146782e5ad29e647e51a95f9290c4e5eba1214d0a736d571de7f55cf7a98b/68747470733a2f2f7777772e64697261632e72756e2f7374617469632f696d616765732f6d756c7469706c655f656469742e706e67)](https://camo.githubusercontent.com/7c2146782e5ad29e647e51a95f9290c4e5eba1214d0a736d571de7f55cf7a98b/68747470733a2f2f7777772e64697261632e72756e2f7374617469632f696d616765732f6d756c7469706c655f656469742e706e67)
* **AST-Native Precision**: Built-in understanding of language syntax (TypeScript, Python, C++, etc.) allows Dirac to perform structural manipulations like function extraction or class refactoring with 100% accuracy. [![AST-Native Precision](https://camo.githubusercontent.com/37d1ad7e29ec1d50a714d80c7d60cf27efbf61514c449b48a0e0948245792a92/68747470733a2f2f7777772e64697261632e72756e2f7374617469632f696d616765732f706172616c6c656c5f4153545f656469742e706e67)](https://camo.githubusercontent.com/37d1ad7e29ec1d50a714d80c7d60cf27efbf61514c449b48a0e0948245792a92/68747470733a2f2f7777772e64697261632e72756e2f7374617469632f696d616765732f706172616c6c656c5f4153545f656469742e706e67)
* **Multi-File Batching**: Dirac can process and edit multiple files in a single LLM roundtrip, significantly reducing latency and API costs. [![Multi-File Batching](https://camo.githubusercontent.com/17195a2ee334a899e41d17267152feae6df9bb8459a4fac440f063206c4e7ede/68747470733a2f2f7777772e64697261632e72756e2f7374617469632f696d616765732f6d756c74695f66756e6374696f6e5f726561642e706e67)](https://camo.githubusercontent.com/17195a2ee334a899e41d17267152feae6df9bb8459a4fac440f063206c4e7ede/68747470733a2f2f7777772e64697261632e72756e2f7374617469632f696d616765732f6d756c74695f66756e6374696f6e5f726561642e706e67)
* **High-Bandwidth Context**: Optimized context curation keeps the agent lean and fast, ensuring the LLM always has the most relevant information without wasting tokens.
* **Autonomous Tool Use**: Dirac can read/write files, execute terminal commands, use a headless browser, and more - all while keeping you in control with an approval-based workflow.

#### 📦 Installation

##### VS Code Extension

Install Dirac from the [VS Code Marketplace](https://marketplace.visualstudio.com/items?itemName=dirac-run.dirac).

##### CLI (Terminal)

Install the Dirac CLI on macOS or Linux using our official installation script:

```
curl -fsSL https://raw.githubusercontent.com/dirac-run/dirac/master/scripts/install.sh | bash
```

#### 🚀 CLI Quick Start

This is still being fixed. Meanwhile you can download the source and build manually.

```
git clone https://github.com/dirac-run/dirac.git
cd dirac
npm install
npm run cli:build
npm run cli:link
```

1. **Install**: 
```
curl -fsSL https://raw.githubusercontent.com/dirac-run/dirac/master/scripts/install.sh | bash
```
2. **Authenticate**: 
```
dirac auth
```
3. **Run your first task**: 
```
dirac "Analyze the architecture of this project"
```

##### Common Commands

* `dirac "prompt"`: Start an interactive task.
* `dirac -p "prompt"`: Run in **Plan Mode** to see the strategy before executing.
* `dirac -y "prompt"`: **Yolo Mode** (auto-approve all actions, great for simple fixes).
* `git diff | dirac "Review these changes"`: Pipe context directly into Dirac.
* `dirac history`: View and resume previous tasks.

#### 🛠️ Getting Started

1. Open the Dirac sidebar in VS Code.
2. Configure your preferred AI provider (Anthropic, OpenAI, OpenRouter, etc.).
3. Start a new task by describing what you want to build or fix.
4. Watch Dirac go!

#### 📄 License

Dirac is **open source** and licensed under the [Apache License 2.0](https://github.com/dirac-run/dirac/blob/master/LICENSE).

#### 🤝 Acknowledgments

Dirac is a fork of the excellent [Cline](https://github.com/cline/cline) project. We are grateful to the Cline team and contributors for their foundational work.

Built with ❤️ by [Max Trivedi](https://www.linkedin.com/in/max-trivedi-49993aab/) at [Dirac Delta Labs](https://dirac.run)
