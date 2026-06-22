# Legit-Control/monorepo: A Git based Version control system for AI agents to make them safe, reliable collaborators.

![rw-book-cover](https://opengraph.githubassets.com/06fae8594fa0de9d73d9c9a2f15c5efb681ae5e79c72941e68819213a02a9a9d/Legit-Control/monorepo)

## Metadata
- Author: [[https://github.com/Legit-Control/]]
- Full Title: Legit-Control/monorepo: A Git based Version control system for AI agents to make them safe, reliable collaborators.
- Category: #articles
- Summary: Legit SDK is a Git-based version control system that makes apps fail-safe and easy to use. It lets users track changes, branch safely, and roll back to previous states through a familiar file system API. The SDK works everywhere, including browsers and servers, and supports many programming environments.
- URL: https://github.com/Legit-Control/monorepo/tree/main

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/Legit-Control/monorepo/tree/main?resume=1) 

#### Create list

### Legit-Control/monorepo

main

tT

Go to file

Code

Open more actions menu

### Legit Monorepo

##### Meet Legit SDK — fail-safe apps made simple.

Legit SDK is built around **two core ideas**: fail-safe by design, and effortlessly simple to use.

Fail-safe means giving your users the same superpowers you know from Git:

* Roll back to any previous state
* Branch off to run experiments safely
* Accept changes when you’re happy with the result

And it’s easy because you interact through the **file system API** (Legit FS) — the same one you learned in your first semesters of computer science.

**Runs everywhere.** Use Legit SDK as an API in the browser, or mount it as a folder on your machine. That means instant compatibility with the stack of your choice: Node.js, Python, Java… you name it.

##### Quick Links

* [Documentation](https://legitcontrol.com/docs): Full guide and API reference
* [Getting Started](https://legitcontrol.com/docs/quickstart): Minimal example to get your first LegitFS repo up
* [Example Starter](https://legitcontrol.com/docs/examples): See a working editor demo with history tracking
* [Contributing](https://github.com/Legit-Control/monorepo/blob/main/CONTRIBUTING.md): How to contribute, including the Contributor License Agreement

##### Installation

```
npm install @legit-sdk/core
```

##### Minimal example

```
import { fs } from 'memfs';
import { initLegitFs } from '@legit-sdk/core';

async function main() {
  const legitFs = await initLegitFs(fs, '/');

  await legitFs.promises.writeFile(
    '/.legit/branches/main/hello.txt',
    'Hello world'
  );

  const history = await legitFs.promises.readFile(
    '/.legit/branches/main/.legit/history',
    'utf8'
  );
  console.log(content);
}
main();
```

##### Features

* **Versioned filesystem** – Every write is tracked in .legit
* **Branching and history** – Access past states, branch safely, merge confidently
* **Interoperable** – Works with Node.js, browsers, Docker, serverless, and more
* **Extensible API** – Compatible with custom storage backends

##### Project Structure

* `packages/sdk/` – Source code of the SDK
* `packages/sdk/dist/` – Bundled outputs for Node.js, browser, and TypeScript
* `packages/sdk/src/compositeFs/` – Core filesystem abstraction
* `packages/sdk/src/compositeFs/subsystems/` – Ephemeral, hidden, pass-through, and Git-backed file systems

##### Contributing

Please review the [CLA](https://github.com/Legit-Control/monorepo/blob/main/cla/CLA.md) before submitting contributions.

We welcome PRs, issues, and suggestions to make Legit SDK better for everyone.
