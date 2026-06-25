---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - code-quality
  - harness
source: readwise
created: 2026-06-23
rating: 
action: 
theme: quality-gates
subtheme:
  - code-review-gates
  - automated-tests
---

# ESLint as AI Guardrails: The Rules That Make AI Code Readable

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/1*O3ARLy1WIG_nj0XLdvTttw.png)

## Metadata
- Author: [[Alex Brohshtut]]
- Full Title: ESLint as AI Guardrails: The Rules That Make AI Code Readable
- Category: #articles
- Summary: AI-generated code often has more bugs and readability issues than human code. Using strict ESLint rules acts as guardrails that force AI to write clearer, maintainable code. These rules stop AI from bypassing limits and help create reliable, self-documenting programs.
- URL: https://medium.com/@albro/eslint-as-ai-guardrails-the-rules-that-make-ai-code-readable-8899c71d3446

## Full Document
![](https://miro.medium.com/v2/resize:fit:2000/1*O3ARLy1WIG_nj0XLdvTttw.png)
I’ve been running AI agents on my codebase for a long time now. Claude Code, specifically Opus 4.5, writing features end-to-end while I drink coffee. And I learned something the hard way: **the agent is great, but it’s not smart — not in the way we are.**

Here’s what I mean. I once asked the agent to implement a file download service. Without constraints, it produced a 180-line function with hardcoded timeouts (`10000`), magic retry counts (`3`), and helpful comments like "// download the file" above a line that downloads the file. It worked. But six months from now, nobody would understand what `10000` meant.

That’s when I realized: when we do linting for humans, we’re nudging them. Humans are smart — they don’t need someone digging into every decision. **Agents are different. They need guardrails. Hard constraints they cannot bypass.**

#### The Problem Is Real (And Measured)

This isn’t just my experience. [CodeRabbit’s 2024 report](https://www.coderabbit.ai/blog/state-of-ai-vs-human-code-generation-report) found that AI-generated code produces **1.7x more issues** and **1.4x more critical bugs** than human-written code. [Qodo’s State of AI Code Quality](https://www.qodo.ai/reports/state-of-ai-code-quality/) research reveals that structural tasks — such as refactoring — are where AI struggles most, often missing context and introducing inconsistencies.

With 85% of developers now regularly using AI coding tools, we can’t pretend this will fix itself. We need a different approach.

#### The Core Philosophy: Responsible AI Coding

This isn’t about rejecting AI assistance. It’s about **responsible AI coding** — getting readable, maintainable output from agents that would otherwise produce chaos.

My solution has two parts:

1. **Tests** — If you don’t have tests, you don’t know what broke
2. **Linting** — Not suggestions. Enforcement.

When you give an agent guardrails, it has no choice. It must obey. And that changes everything.

#### Why Linters (Not Just CLAUDE.md)

You can write the most detailed `CLAUDE.md` or `.cursorrules` file in the world. The agent might follow it. Or it might not. Documentation provides hints, but **linters provide rules**. The difference is critical: AI can choose to ignore documentation, but it cannot ignore linting errors in your CI (and dev!) pipeline.

More importantly: while we have many ways to guide AI — prompt engineering, spec files, few-shot examples — **only linters give you enforceable rules for every technology in your stack**. React components, NestJS services, Prisma schemas, Playwright tests — each has its own patterns, and I can enforce them all in one place.

#### The Five Rules That Changed Everything

I narrowed it down to five ESLint rules that do the heavy lifting. Even these basic rules alone achieve remarkable results. These aren’t suggestions — they’re the difference between readable code and spaghetti.

#### 1. No Comments (`no-comments/disallowComments`)

```
'no-comments/disallowComments': 'error'  

```

This sounds extreme. It is. And it works.

Here’s why: AI loves to write comments. Long, verbose, explaining-the-obvious comments. “This function logs in the user” above a function called `loginUser`.

But there’s a deeper reason. When you forbid comments, you force the agent to write self-documenting code. It has to pick better names, extract functions properly, make the code speak for itself.

As for explanations needed, they go to the docs, as they should.

**Real example from my codebase:**

```
export const validateContentLength = (  
  response: Response,  
  maxSizeBytes: number,  
): void => {  
  const contentLength = response.headers.get("content-length");  
  if (!contentLength) return  
  const sizeBytes = Number.parseInt(contentLength, 10);  
  if (sizeBytes > maxSizeBytes) {  
    throw new Error(  
      `File size ${sizeBytes} bytes exceeds maximum ${maxSizeBytes} bytes`,  
    );  
  }  
};  

```

Seven lines. No comments needed. The function name tells you exactly what it does.

#### 2. Maximum Two Parameters (`better-max-params`)

```
'better-max-params/better-max-params': [  
  'error',  
  {  
    constructor: 10,  // NestJS DI needs more  
    func: 2,  
  },  
]  

```

Two parameters max for functions. This forces the agent to use object parameters with destructuring:

```
export type FetchParameters = {  
  allowedDomains: readonly string[];  
  logger: Logger;  
  maxSizeBytes: number;  
  regulationId: string;  
  timeoutMs: number;  
  url: string;  
};  
  
export const fetchAttachment = async (  
  parameters: FetchParameters,  
): Promise<Response> => {  
  const { allowedDomains, logger, maxSizeBytes, regulationId, timeoutMs, url } =  
    parameters;  
  // ...  
};  

```

Without this rule, the agent will happily write `fetchAttachment(url, logger, maxSizeBytes, timeoutMs, allowedDomains, regulationId)`. Good luck remembering that order in six months.

#### 3. Maximum 50 Lines Per Function

```
'max-lines-per-function': ['error', { max: 50, skipBlankLines: true }]  

```

This is where the magic happens. The agent **does refactor while it runs**. It hits the 50-line limit, realizes it can’t fit everything, and starts extracting helpers.

From my actual codebase, here’s what the agent produced — small, focused functions:

```
export const validateAllowedUrl = (  
  url: string,  
  allowedDomains: readonly string[],  
): void => {  
  const parsedUrl = new URL(url);  
  const hostname = parsedUrl.hostname.toLowerCase();  
  const isAllowed = allowedDomains.some(  
    (domain) => hostname.endsWith(domain) || hostname === domain,  
  );  
  
 if (!isAllowed) {  
    throw new Error(  
      `URL must be from allowed domains (${allowedDomains.join(", ")}), got: ${hostname}`,  
    );  
  }  
};  
  
export const validateContentLength = (  
  response: Response,  
  maxSizeBytes: number,  
): void => {  
  const contentLength = response.headers.get("content-length");  
  if (contentLength) {  
    const sizeBytes = Number.parseInt(contentLength, 10);  
    if (sizeBytes > maxSizeBytes) {  
      throw new Error(  
        `File size ${sizeBytes} bytes exceeds maximum allowed ${maxSizeBytes} bytes`,  
      );  
    }  
  }  
};  

```

Each function does one thing. You can understand what’s happening at a glance.

#### 4. Maximum 250 Lines Per File

```
'max-lines': ['error', { max: 250, skipBlankLines: true }]  

```

Same principle, higher level. This prevents the agent from dumping everything into one god file. It forces proper module separation.

#### 5. No Magic Numbers

```
'no-magic-numbers': [  
  'error',  
  {  
    detectObjects: false,  
    enforceConst: true,  
    ignore: [0, 1, -1, 2],  
    ignoreArrayIndexes: true,  
  },  
]  

```

Without this rule, the agent will scatter random numbers across your codebase. What’s `10000`? A timeout? A retry interval? A lucky number?

#### Get Alex Brohshtut’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

Remember me for faster sign in

With this rule, the agent is forced to define named constants:

```
const VISIBILITY_TIMEOUT_MS = 10_000;  
const MAX_RETRY_ATTEMPTS = 5;  
const DEFAULT_PAGE_SIZE = 20;  

```

Now, when you see `VISIBILITY_TIMEOUT_MS` in the code, you know exactly what it means. And when you need to change it, there's one place to look.

#### The Escape Attempts (And How to Block Them)

Here’s the fun part. Different models try different escapes.

**Sonnet** tried to disable rules with inline comments:

```
// eslint-disable-next-line max-lines-per-function  

```

**Opus** was smarter. It tried to edit my ESLint config directly. “I’ll just increase the limit to 100 lines; that should be fine.”

No.

I block both approaches. First, I use `eslint-plugin-no-comments` which forbids all comments—including `eslint-disable` directives. The agent can't sneak past the rules with inline disables.

Second, I use Claude Code hooks that run before tool use. Here’s my `protect-eslint.sh`:

```
#!/bin/bash  
INPUT=$(cat)  
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')  
FILENAME=$(basename "$FILE_PATH")  
  
if [[ "$FILENAME" == "eslint.config.mjs" ]]; then  
  jq -n '{  
    decision: "block",  
    reason: "Modifying eslint.config.mjs is forbidden.   
  
    If you believe a rule makes your task impossible,   
    report this to the user and explain why."  
  }'  
  exit 0  
fi  
echo '{"decision": "approve"}'  

```

The agent physically cannot edit the ESLint config. But here’s the key: the message tells the agent it’s allowed to come back and explain why a rule is blocking it. Sometimes at the end of a run, the agent says “Listen, I really tried, but this rule makes what you asked for impossible — here’s why.” That’s fine. Then I decide if the rule needs changing, not the agent.

#### The Lint Feedback Loop

Another hook I run: after every file edit, lint runs automatically. If it fails, the agent gets the errors immediately and tries to fix them.

The key is tracking attempts **per file** — otherwise the agent could fail on file A, succeed on file B, and reset its counter:

```
if [ $LINT_EXIT_CODE -ne 0 ]; then  
  ATTEMPT=$((ATTEMPT + 1))  
if [ "$ATTEMPT" -ge 3 ]; then  
    # Stop trying, ask human for help  
    jq -n --arg out "$LINT_OUTPUT" '{  
      decision: "approve",  
      reason: "CRITICAL: File has failed linting 3 times. STOP. Report to user."  
    }'  
  else  
    jq -n --arg out "$LINT_OUTPUT" '{  
      decision: "approve",  
      reason: "Linting failed. Please fix these errors:\n\($out)"  
    }'  
  fi  
fi  

```

Three strikes per file, and it stops. This prevents infinite loops where the agent keeps “fixing” the same thing over and over, making it worse each time.

#### Beyond The Basics: Recommended Configs

The five core rules do the heavy lifting, but I don’t stop there. The ESLint ecosystem has excellent recommended configs for every technology I use:

```
import { configs as sonarjsConfigs } from "eslint-plugin-sonarjs";  
import unicorn from "eslint-plugin-unicorn";  
import security from "eslint-plugin-security";  
import eslintNestJs from "@darraghor/eslint-plugin-nestjs-typed";  
import react from "eslint-plugin-react";  
import tailwindcss from "eslint-plugin-tailwindcss";  
import playwright from "eslint-plugin-playwright";  
  
export default defineConfig([  
  sonarjsConfigs.recommended, // Code smells, cognitive complexity  
  unicorn.configs["recommended"], // Modern JS best practices  
  security.configs.recommended, // Security vulnerabilities  
  eslintNestJs.configs.flatRecommended, // NestJS patterns  
  react.configs.flat.recommended, // React rules  
  tailwindcss.configs["flat/recommended"], // Tailwind consistency  
  playwright.configs["flat/recommended"], // Test patterns  
  // ...  
]);  

```

Each plugin brings domain expertise. The security plugin flags potential vulnerabilities. The NestJS plugin enforces dependency injection patterns. I don’t have to think about all this — the rules do.

SonarJS deserves special mention. Its `cognitive-complexity` rule provides a similar experience to the five core rules—it forces the agent to break down complex logic into smaller, understandable pieces. When a function gets too hard to follow, the rule fails, and the agent refactors.

Then I add my custom rules on top:

```
'complexity': ['error', 10],           // No spaghetti logic  
'max-depth': ['error', 4],             // No pyramid of doom  
'max-statements': ['error', 20],       // Keep functions focused  
'max-classes-per-file': ['error', 1],  // One class, one file  
'no-console': 'error',                 // Use proper logging  
'id-length': ['error', { min: 2 }],    // No 'x' or 'a' variables  
'eqeqeq': ['error', 'always'],         // No == surprises  

```

And domain-specific constraints:

```
'no-restricted-syntax': [  
  'error',  
  {  
    selector: "MemberExpression[object.name='process'][property.name='env']",  
    message: 'Direct process.env access forbidden. Use DI to get configuration',  
  },  
]  

```

The agent can’t access `process.env` directly—it must use dependency injection. This keeps the configuration testable and explicit.

#### Results

The code that I receive is code I can genuinely live with. I can go to any file, see some layout or function, and understand what’s happening. The agent does refactoring as it develops — hit a limit, extract a function, keep going.

Tests cost nothing now. The agent writes them, they’re clean, I can understand them:

```
await expect(page.getByTestId("user-initials")).toBeVisible();  
await page.getByTestId("logout-button").click();  
await expect(page.getByTestId("login-form")).toBeVisible();  

```

No comments needed. The code says what it does.

#### The Paradigm Shift

The main message: **guardrails, not guidelines**.

> “Rather than relying on prompts or hoping the AI ‘does the right thing,’ we can build guardrails that make certain behaviors impossible.”
> 
> 

The paradigm isn’t using agents to generate code or help you write. You need to give them control — and the most important thing is to fence them in. Tests, linting, hooks.

Then you get the right thing. Because there isn’t someone going over every line of code anymore. That era is over.

#### Actionable Steps

1. **Start with these five rules** — no comments, max 2 params, 50 lines/function, 250 lines/file, no magic values. Even this alone will transform your AI output.
2. **Install the plugins:** `npm install -D eslint-plugin-no-comments eslint-plugin-better-max-params`
3. **Add recommended configs for your stack** — Don’t reinvent the wheel. Use `eslint-plugin-react`, `eslint-plugin-playwright`, whatever matches your tech.
4. **Protect your config** — If you’re using Claude Code, add a PreToolUse hook that blocks edits to `eslint.config.*` There are also hooks for other agentic tools.
5. **Add a lint feedback hook** — Run lint after every file edit, feed errors back to the agent
6. **Iterate** — Your config will evolve as you discover what works for your stack.

*This article is based on a talk I gave about AI-assisted development. ESLint guardrails are just one piece of the puzzle — I also covered agent orchestration with BMAD, TDD loops, context optimization, and more. Stay tuned for upcoming articles diving deeper into each topic.*
