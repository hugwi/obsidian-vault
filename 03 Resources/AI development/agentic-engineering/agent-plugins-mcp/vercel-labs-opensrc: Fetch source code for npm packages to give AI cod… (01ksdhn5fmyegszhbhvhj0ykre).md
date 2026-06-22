---
title: "vercel-labs/opensrc: Fetch source code for npm packages to give AI coding"
source: "https://github.com/vercel-labs/opensrc"
author: "github.com/vercel-labs"
published: 
created: 2026-05-24
description: "Fetch source code for npm packages to give AI coding agents deeper context"
tags:
  - to-process
  - agent-plugins-mcp
---

[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/vercel-labs/opensrc?resume=1) 


## Create list


# vercel-labs/opensrc


main


tT


Go to file


Code


Open more actions menu


# opensrc


Give coding agents access to any package's source code.


## Quick Start



```
npm install -g opensrc
# Search a package's source
rg "parse" $(opensrc path zod)

# Read a specific file
cat $(opensrc path zod)/src/types.ts

# Works with any registry
find $(opensrc path pypi:requests) -name "*.py"
```

`opensrc path` fetches on first use, then returns the cached path instantly. See the [CLI readme](https://github.com/vercel-labs/opensrc/blob/main/packages/opensrc/README.md) for full usage.


## Packages




| Package | Description |
| --- | --- |
| [`opensrc`](https://github.com/vercel-labs/opensrc/blob/main/packages/opensrc) | CLI — fetch and cache source code from npm, PyPI, crates.io, and GitHub |
| [`@opensrc/docs`](https://github.com/vercel-labs/opensrc/blob/main/apps/docs) | Documentation site |


## Development


This is a [Turborepo](https://turbo.build) monorepo using [pnpm](https://pnpm.io) workspaces.



```
pnpm install
turbo build
turbo dev
```

### CLI (Rust)



```
cargo build --manifest-path packages/opensrc/cli/Cargo.toml
cargo test --manifest-path packages/opensrc/cli/Cargo.toml
cargo fmt --manifest-path packages/opensrc/cli/Cargo.toml
cargo clippy --manifest-path packages/opensrc/cli/Cargo.toml -- -D warnings
```

### Docs (Next.js)



```
cd apps/docs
pnpm dev
```

## License


Apache-2.0