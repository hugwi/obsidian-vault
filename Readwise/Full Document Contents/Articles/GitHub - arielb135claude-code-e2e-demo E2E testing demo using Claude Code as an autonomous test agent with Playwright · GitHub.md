# GitHub - arielb135/claude-code-e2e-demo: E2E testing demo using Claude Code as an autonomous test agent with Playwright · GitHub

![rw-book-cover](https://opengraph.githubassets.com/b1ba119185dec89593d7edf311fa1602145da5f78e4740a0a4c6d252a2d00f07/arielb135/claude-code-e2e-demo)

## Metadata
- Author: [[https://github.com/arielb135/]]
- Full Title: GitHub - arielb135/claude-code-e2e-demo: E2E testing demo using Claude Code as an autonomous test agent with Playwright · GitHub
- Category: #articles
- Summary: This project demonstrates automated end-to-end testing of a shopping cart app using Claude Code and Playwright. Tests are written in plain English and run securely with optimized API usage and parallel execution. It handles login safely and supports various shopping cart scenarios like adding items and completing checkout.
- URL: https://github.com/arielb135/claude-code-e2e-demo

## Full Document
### arielb135/claude-code-e2e-demo

main

Go to file

Code

Open more actions menu

### Shopping Cart E2E Testing with Claude Code

Automated E2E testing framework for a shopping cart web app using Claude Code and Playwright.

#### What This Does

* Runs a simple Node.js shopping cart app (the "Soup Shop")
* Uses Claude Code as an autonomous test agent to interact with the app via Playwright
* Tests login, adding items to cart, checkout flows, and error handling

#### How It Works

Write tests in **plain English** - describe what you want to test and how to validate it:

```
{
  "name": "checkout-success",
  "prompt": "add Clam Chowder to cart, go to checkout, fill name 'John Doe' and address '123 Main St'",
  "validation": "Verify the success page shows 'Order Confirmed' with an order ID"
}
```

The framework uses natural language for both the test action (`prompt`) and the pass/fail criteria (`validation`). No page objects, selectors, or test code required.

#### Cost Optimization

All commands and agents use **Claude Haiku** to minimize API costs while maintaining reliable test execution. Haiku is well-suited for structured automation tasks like form filling, button clicking, and page verification.

#### Prerequisites

* [Claude Code](https://claude.ai/code) installed (`npm install -g @anthropic-ai/claude-code`)

#### Quick Start

```
# Clone and enter the repo,
# Run the setup command in Claude Code
claude
/init-cart
```

The `/init-cart` command will:

1. Check and install all other prerequisites (Node.js, npm, Python)
2. Set up environment files
3. Start the shopping cart app
4. Optionally run a test

#### Running Tests

**Single test via Claude command:**

```
/cart-test add Mulligatawny Soup to cart

```

**All tests via Python (parallel):**

```
python3 run_tests.py --parallel 3 --verbose
```

**Run specific tests:**

```
python3 run_tests.py --filter checkout-success
python3 run_tests.py --filter "add-item-to-cart,checkout-success"
```

##### Test Output

With `--verbose`, you can inspect detailed output in the `results/` directory:

* `{test-name}.log` - Full execution log for each test
* `{test-name}-mcp.json` - Per-session MCP config (browser profile isolation)
* `summary.json` - Aggregated results with pass/fail counts and durations

#### Parallel Testing

Playwright MCP doesn't support parallel testing by default ([issue #893](https://github.com/microsoft/playwright-mcp/issues/893)).

We work around this by creating a separate browser session per test worker:

* Each parallel worker gets a unique `--user-data-dir` (`/tmp/playwright-e2e-worker-{N}`)
* A per-test MCP config is generated in `results/{test-name}-mcp.json`

This allows running multiple tests concurrently without session conflicts.

#### Secure Credential Handling

Login is handled by a dedicated **login subagent** (`.claude/agents/login.md`) with two key security properties:

1. **Context isolation** - The login subagent runs with no context from the parent request. This reduces token usage and prevents credential leakage into the main conversation.
2. **Secret injection via Playwright MCP** - Credentials never appear in the LLM context. The `--secrets` flag in `.mcp.json` points to `.env.e2e-secrets`:

 
```
"--secrets", ".env.e2e-secrets"
```
 The agent uses placeholder values (`SHOP_USERNAME`, `SHOP_PASSWORD`) in `browser_type` calls, and Playwright MCP substitutes them with actual values from the secrets file at execution time.

This architecture ensures credentials are handled securely without being exposed to any LLM context.

#### Test Cases

| Test | Description |
| --- | --- |
| view-cart | Verify cart page loads with soups |
| add-item-to-cart | Add soup and verify it's in cart |
| checkout-success | Complete checkout flow |
| checkout-no-soup-for-you | Test the "No soup for you!" Easter egg |
| remove-item-from-cart | Add then remove item |
| multiple-items-checkout | Checkout with multiple items |
