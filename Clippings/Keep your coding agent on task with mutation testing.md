---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - code-quality
  - testing
source: readwise
created: 2026-06-23
rating: 
action: 
theme: quality-gates
subtheme:
  - automated-tests
  - verification-loops
---

# Keep your coding agent on task with mutation testing

![rw-book-cover](https://cdn.prod.website-files.com/6647a84a9616b0776fb903e9/68f78ee70e60685b848a4d4d_help-your-coding-agent-stay-on-task-with-mutation-testing.jpg)

## Metadata
- Author: [[testdouble.com]]
- Full Title: Keep your coding agent on task with mutation testing
- Category: #articles
- Summary: AI coding agents often generate extra or untested code, so you should make them run linters, typechecks, and tests after each change. Use mutation testing (e.g., Stryker) to break code and find weak tests that let bugs survive. Run mutations only on changed files and use coverage to limit tests so runs stay fast.
- URL: https://testdouble.com/insights/keep-your-coding-agent-on-task-with-mutation-testing

## Full Document
![](https://cdn.prod.website-files.com/6647a84a9616b0776fb903e9/68f78ee70e60685b848a4d4d_help-your-coding-agent-stay-on-task-with-mutation-testing.jpg)
AI coding agents are great at generating code. In fact, they'll happily generate too much code. Working effectively with them means getting good at asking for what you want up front, but also getting good at paring down their output.

The more of that pruning process you can foist back onto the computer, the tighter your iteration loop will be.

For instance, I've always gotten value out of code linters and formatters, but LLMs benefit from them so much more. I can't tell you how often Claude has created unused variables that my linter flags before I even open the file.

Tell your coding agent to run formatting, linting, typechecking (if available), and your unit tests after every change. It makes a huge difference in the quality of the code produced.

#### My tests have to be *good*?

Yes, this presumes you have unit tests and that they are effective. You can (and should) have the agent write tests, but ensuring they are effective is trickier. There is no full substitute to reading and understanding the code, but we want the computer to solve as many of our problems as possible.

To that end I have had a lot of success lately using mutation testing.

#### What is mutation testing?

A mutation testing tool intentionally breaks your code and then runs your tests. If your tests pass when your code is broken, they probably need improvement.

I first encountered this concept with [Heckle](https://ruby.sadi.st/Heckle.html), a gem designed to break your Ruby code. (I just now realized that gem is old enough to vote.) I knew I wanted something like that for TypeScript and found [Stryker Mutator](https://stryker-mutator.io).

Stryker is a well-maintained collection of tools with a long history. In addition to JavaScript/TypeScript there are versions available for C# and Scala. The JavaScript version has explicit support for most popular test runners like Jest and Vitest, but it will happily run whatever your `npm test` script is if you're using something obscure like [teenytest](https://github.com/testdouble/teenytest).

#### How to use Stryker

To install it run: `npm install --save-dev @stryker-mutator/core` and `npx stryker init`, which helps you create a config file.

The `stryker run` command will try to mutate all of your non-test code. If you're concentrating on a particular file though you can tell Stryker that with `-m filename` on the command-line. The output looks something like this:

```
% npx stryker run -m lib/clean_cache.js
16:06:53 (96157) INFO ProjectReader Found 1 of 21 file(s) to be mutated.
16:06:53 (96157) INFO Instrumenter Instrumented 1 source file(s) with 19 mutant(s)
16:06:53 (96157) INFO ConcurrencyTokenProvider Creating 9 test runner process(es).
16:06:53 (96157) INFO DryRunExecutor Starting initial test run (command test runner with "off" coverage analysis). This may take a while.
16:06:54 (96157) INFO DryRunExecutor Initial test run succeeded. Ran 1 tests in 0 seconds (net 847 ms, overhead 0 ms).
Mutation testing  [==================================================] 100% (elapsed: <1m, remaining: n/a) 19/19 Mutants tested (1 survived, 0 timed out)
All tests
  ✓ All tests (killed 18)
[Survived] ConditionalExpression
lib/clean_cache.js:4:7
-     if (sizeMax === Infinity) return
+     if (false) return
Ran 1.00 tests per mutant on average.
----------------|------------------|----------|-----------|------------|----------|----------|
                | % Mutation score |          |           |            |          |          |
File            |  total | covered | # killed | # timeout | # survived | # no cov | # errors |
----------------|--------|---------|----------|-----------|------------|----------|----------|
All files       |  94.74 |   94.74 |       18 |         0 |          1 |        0 |        0 |
 clean_cache.js |  94.74 |   94.74 |       18 |         0 |          1 |        0 |        0 |
----------------|--------|---------|----------|-----------|------------|----------|----------|
16:06:59 (96157) INFO MutationTestExecutor Done in 5 seconds.

```

In this example, Stryker found a condition that it hard-coded to `false` without breaking any tests. Here it is again by itself:

This is an example of the limits of mutation testing. This line is an optimization in my caching library to bail out early if the programmer hasn't set a maximum size for the cache. The code *works* without this optimization, so it is very hard to test around it. I can either abandon the optimization, complicate my code to make the optimization testable, or live with a less-than-100% score. Stryker does not have any facility for "magic comments" to disable checks the way linters do. Fortunately in my testing both Claude and Codex "figured out" that mutations like this are not a problem and didn't insist on getting to 100%.

> The scare quotes around the phrase "figured out" are because I don't really know why these agents do what they do. The thing that happens is that the agents sometimes give up before reaching 100%. Sometimes they have reasonable-sounding explanations why giving up was the right thing to do. I am guessing that the agent has a limit on how long it will bang around on a puzzle. If we ask them to solve the halting problem, maybe they would "recognize" it as unsolvable. Maybe they would hit some internal limit and justify giving up by saying the problem is unsolvable. It's interesting to think about, but a little outside the scope of this post. Anyhow, having the agent give up can be good, but I'll mention it again when I talk about the limitations of mutation testing.

Running mutations in your terminal is a great way to check if the coding agent did its homework, but having the agent itself run mutations lets it observe the output directly and run multiple passes. It can take some coaxing, but when it complies it can increase the quality of the tests it writes dramatically, requiring your attention less often.

#### Asking the robot to run the mutation tool

I have a `"mutate"` script set up in my `package.json` that will run mutation only against changed files in the `src/` directory.

```
sh
{ git diff --name-only -z HEAD -- src/ ; git ls-files --others --exclude-standard -z -- src/ ; } | xargs -0 printf '%s,' | xargs stryker run -m
```

(It's a little wordy in order to get both tracked and untracked files, and to join file names together with commas as the -`m` option expects.)

Most of the time when I ask Claude or Codex for a new feature it will look something like this:

> Implement feature 3 from TODO.md. Make sure you write tests and see them fail before you implement the feature. Once you've written the implementation, check to make sure your tests are good by running `npm run mutate`.

I generally put instructions about things like this in `CLAUDE.md` or `AGENTS.md`, but sometimes I have to be explicit in my prompt.

When you think the tests around a particular file could be better you can ask the agent for specifically that:

> This is a ten-minute screen recording condensed into about half a minute of looping GIF. I included it as an illustration, but I am worried people will try to actually read it. Please spare yourself the headache and trust my summary below.

![](https://cdn.prod.website-files.com/6647a84a9616b0776fb903e9/68f7920de91e95ef3dabb5bd_mutation-example.gif)
This is a very sped-up recording of me asking Claude:

> Please run `npx stryker run -m src/store/serial.ts` and use that information to test serial.ts more thorougyly.

After my prompt Claude does indeed run the Stryker command I gave it and writes some tests. In the middle somewhere it has to compact the context. After writing tests it ran the Stryker command again. At the end it summarizes its changes and reports that it increased the final score to 96.30%. Hilariously, when I double-checked in a different terminal the final score was 94.44%—still a good number, but also a reminder to not take these tools at their word.

#### Doesn't code coverage give us this?

Code coverage tools will give you some of the value you get from mutation testing, but not all. For instance, the line that Stryker flagged in my first example would not have been flagged by a code coverage tool.

I think of mutation testing as a more strict version of code coverage. And when you're trying to wrangle the profuse code generation an LLM gives you into code that actually does what you want, strictness is gold.

That doesn't mean you should ignore code coverage. If you have it configured with a test runner that Stryker has explicit support for, Stryker is smart enough to leverage it to decide what tests to run. If it sees that `src/a.ts` is only covered by `test/a.test.ts`, it can run just that test file when it mutates `src/a.ts`. This will make a huge difference to mutation testing run times as your test suite grows. Furthermore, if you have coverage minimums you can enforce those before running mutation the first time, giving your coding agent faster feedback. All this makes code coverage even more useful if you're using Stryker.

#### Limitations of mutation testing with coding agents

We've already talked about mutation testing complaining about difficult-to-test things like my early return optimization. There are a few other things that might cause you problems.

I mentioned LLMs giving up before reaching 100% as a good thing, but there's no guarantee they won't give up too early. Unlike your test suite or your linter which can give clear pass/fail results, Stryker can only point you to code that *might* be a problem. So when the machine says "I got it to 80% and that's pretty good." you might have to apply a critical eye and ask it to revisit a line that really looks testable.

However, the main problem most people will run into is unit test suite duration. If the run time of your tests caused you problems before, imagine running them for every possible mutation. It can get out of hand quickly. As your codebase grows, you're going to have to tell your LLM to only run mutations against the files that have changed. And as your test suite grows, Stryker's use of code coverage to run a subset of tests will be important as well.

#### The future

In this coding-agent-ified world, stocks are way up on code quality tools. Mutation testing was always too far down the list for me to reach for in the past, but I am now excited by the value I'm getting out of it. I expect that these tools will eventually start to change to make themselves even more useful to coding agents, and I wonder what new tools will emerge to help us keep them on task.

‍*Neal Lindsay is a Senior Software Consultant at Test Double, and has experience in JavaScript, Ruby, Rails, and sudden changes in how software development gets done.*

[![](https://cdn.prod.website-files.com/6647a84a9616b0776fb903e9/68e7b1bde382527aafd637b8_ai-in-the-workforce.jpg)](https://testdouble.com/insights/ai-in-the-workforce-a-shifting-talent-equation)

[![](https://cdn.prod.website-files.com/6647a84a9616b0776fb903e9/68e41f0d5d546c4744f7e612_anvil-of-alignment.jpg)](https://testdouble.com/insights/the-anvil-of-alignment-the-value-of-monoliths-over-microservices)

 [![Letter art spelling out NEAT](https://cdn.prod.website-files.com/6647a84a9616b0776fb9040e/6668d4f56e646b8e97927eef_asset-image-neat-logo.jpg)[Letter art spelling out NEAT](https://testdouble.com/neat)](https://testdouble.com/neat) 

 [![Test Double Executive Leadership Team](https://cdn.prod.website-files.com/6647a84a9616b0776fb9040e/6668d4f570d5444938620c9b_asset-image-team-smiling.jpg)[Test Double Executive Leadership Team](https://testdouble.com/about)](https://testdouble.com/about)
