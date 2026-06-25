---
categories:
  - "[[Resources]]"
domain: engineering
title: "How we use Claude Agents to automate test coverage"
source: "https://dev.to/melnikkk/how-we-use-claude-agents-to-automate-test-coverage-3bfa"
author: "dev.to"
published: 2025-10-11
created: 2026-04-10
description: "Facing the lack of test coverage, we used Claude Agents to automate writing"
tags:
  - to-process
  - agent-configuration
---

*Facing the lack of test coverage, we used Claude Agents to automate writing and reviewing tests. As a result, we are up almost 20% of test coverage in a few days. Here is how.*


[![Robotic hands](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv144bhfiyv5p43g2uctf.jpg)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fv144bhfiyv5p43g2uctf.jpg)
Our team faced a challenge: our service had around 30% test coverage despite being our largest service that we owned. We leveraged spare capacity to tackle test coverage. Writing tests manually would take weeks.


##  Plans


We recognised that the first step was creating a comprehensive roadmap to document our investigation and track progress.


We decided to use Claude Code’s plan mode (`Shift + Tab` *for mode switching*) managed by the Opus model. Opus is strong at understanding architectural relationships, identifying dependencies, and, as we checked in, creating comprehensive testing strategies.


The prompt required providing the comprehensive roadmap for improving common test coverage of the repo. The output result should be split by criticality — critical, medium, and minor. Here is the template:



```
# Test Coverage Roadmap for [PROJECT_NAME]

## Executive Summary

**Current Coverage:** ~[X]%
**Target Coverage:** [TARGET]%
**Priority:** Critical business logic first, UI components last

The [PROJECT_NAME] repository currently has [low/medium/high] test coverage. This roadmap provides a systematic approach to achieve [TARGET]% test coverage by prioritizing high-risk business logic that directly impacts revenue, data integrity, and user experience.

## Current State Analysis

### Package Breakdown

| Package       | Source Files | Test Files | Coverage Priority |
|---------------| ------------ | ---------- | ----------------- |
| `[package-1]` | ~[X]         | [Y]        | 🔴 CRITICAL       |
| `[package-2]` | ~[X]         | [Y]        | 🟡 MEDIUM         |
| `[package-3]` | ~[X]         | [Y]        | 🟢 MINOR          |

### Testing Framework

- **Framework:** [Jest/Vitest/Mocha/etc.]
- **React Testing:** [React Testing Library/Enzyme/etc.]
- **Coverage Tool:** [Istanbul/nyc/c8/etc.]
- **Commands:** `[test command]` for development, `[ci test command]` for CI/CD

---

## 🔴 CRITICAL Priority (~[X] days)

_Focus: High-risk business logic affecting revenue and data integrity_

---

## 🟡 MEDIUM Priority

_Focus: Important features that need coverage but are more stable_

---

## 🟢 MINOR Priority

_Focus: UI components and less critical features_

---

## Implementation Guidelines

### Code Coverage Targets

| Priority | Target Coverage | Focus Areas                       |
| -------- | --------------- | --------------------------------- |
| Critical | [X]%            | Domain models, business logic     |
| Medium   | [Y]%            | Services, repositories, use cases |
| Minor    | [Z]%            | UI components, utilities          |

### Quality Gates

#### Critical Checkpoint

- ✅ Domain models: [X]%+ coverage
- ✅ View models: [X]%+ coverage
- ✅ Core business logic: [X]%+ coverage

#### Medium Checkpoint

- ✅ Repository layer: [X]%+ coverage
- ✅ Use cases: [X]%+ coverage
- ✅ Overall coverage: [Y]%+

#### Minor Checkpoint

- ✅ Overall coverage: [Z]%+
- ✅ All critical paths tested
- ✅ Performance benchmarks established

### Tools & Setup

#### Required Dependencies

json
{
  "devDependencies": {
    "[testing-library-package]": "^[version]",
    "[testing-framework]": "^[version]",
    "[user-event-library]": "^[version]",
    "[test-environment]": "^[version]",
    "[mocking-library]": "^[version]"
  }
}


#### Test Configuration Updates

javascript
// [config-file] additions
{
  "coverageThreshold": {
    "global": {
      "branches": [X],
      "functions": [X],
      "lines": [X],
      "statements": [X]
    },
    "[critical-path-pattern]": {
      "branches": [X],
      "functions": [X],
      "lines": [X],
      "statements": [X]
    }
  },
  "collectCoverageFrom": [
    "[source-pattern]",
    "![exclusion-pattern]",
    "![type-definitions]"
  ]
}


---

## Success Criteria

### Quantitative Goals

- ✅ [X]% overall test coverage
- ✅ [Y]% coverage for critical business logic
- ✅ <[Z]% flaky test rate
- ✅ Test execution time <[N] minutes

### Qualitative Goals

- ✅ All critical user flows covered by tests
- ✅ Edge cases and error scenarios tested
- ✅ Performance benchmarks established
- ✅ Documentation for testing patterns available

---

## Timeline & Milestones

| Phase    | Duration | Deliverables                                      |
| -------- | -------- | ------------------------------------------------- |
| Critical | [X] days | [Critical priority items completed]               |
| Medium   | [Y] days | [Medium priority items completed]                 |
| Minor    | [Z] days | [Minor priority items + overall coverage reached] |

---

## Notes for Implementation

1. **Start with Critical Priority**: Focus on business logic that affects revenue and data integrity
2. **Test-Driven Development**: Consider writing tests before implementing new features
3. **Continuous Integration**: Ensure tests run in CI/CD pipeline with coverage enforcement
4. **Regular Reviews**: Review coverage reports weekly to track progress
5. **Documentation**: Document complex test scenarios and testing patterns
6. **Maintenance**: Regularly update and refactor tests as code evolves

```

By switching back to Sonnet, we created the roadmap completion checklist for better team collaboration and results tracking. Here is the template:



```
# Test Coverage Implementation Checklist

**Target Coverage:** [TARGET]% | **Current Coverage:** ~[CURRENT]%

---

## 🔴 CRITICAL Priority | 🟡 MEDIUM Priority | 🟢 MINOR Priority

### [Category X - e.g., Core Domain Models & Business Logic]

Task: [TICKET-NUMBER]([project-tracker-url])

- [ ] Test [TEST-DESCRIPTION]

  - File: `[path/to/file.ts]`
  - Test [feature 1], [feature 2], [feature 3], [edge cases]
  - **Tests implemented**: `[path/to/test.spec.ts]` ([X] test cases)
  - **Coverage**: [X]% - [Description of what's covered]

## Notes

- [✓] Completed items are marked with [x]
- [ ] Pending items are marked with [ ]
- ** Double asterisks indicate items not yet started
- Items without ** have been started or completed
- Update coverage percentages after each test implementation
- Link test files to source files for easy navigation
- Track test case counts for comprehensive documentation

```

##  Claude init


Before writing tests, we needed Claude to understand our project’s specific requirements without repeating context in every prompt.


The `/init` command creates a CLAUDE.md file - persistent memory that Claude loads into context. This file helps provide base info to Claude without additional requests in the prompt. The CLAUDE.md file shapes Claude before any interaction begins, and then it is automatically included in every interaction.


There are no rules as Cursor has, so we’ve included some specific repo rules and test coverage thresholds right in this file. CLAUDE.md can be initiated in any directory of the project, so it could potentially solve the lack of rules and support concrete specific code requirements on different levels instead of handling single large CLAUDE.md file. Looks like a good solution for repos with different independent packages inside.


##  Agents


With completed roadmap, we needed further process optimisations. The solution was to use Claude Agents.


Agents are the simple Markdown files stored in *.claude/agents*. Claude can automatically select appropriate agents based on task context and agent description. Claude uses the agent description field as a semantic trigger to determine which agent best matches the request. This means that the agent description should focus on the real agent capabilities.


We initiated a small agent system consisting of 2 agents. Use the `/agents` command with the selected `Create new agent` option.


The first agent is typescript-test-specialist. Here it is:



```
---
name: typescript-test-specialist
description: Expert TypeScript test implementation specialist. Use for writing comprehensive unit and integration tests with proper TypeScript typing and TDD principles.
tools: Read, Write, Edit, Bash, Grep, mcp__**ide**__getDiagnostics
model: sonnet
color: green
---

You are an expert TypeScript test implementation specialist with deep expertise in modern testing frameworks, test-driven development, and TypeScript's advanced type system. You excel at creating comprehensive, maintainable test suites that provide confidence in code quality and facilitate safe refactoring.

Your core responsibilities:

- Write thorough unit and integration tests using popular frameworks
- Implement proper TypeScript typing in tests, including generic constraints and utility types
- Apply TDD principles: Red-Green-Refactor cycle with meaningful test names
- Design test cases that cover happy paths, edge cases, error conditions, and boundary values
- Create effective test doubles (mocks, stubs, spies) with proper typing
- Structure tests for readability using AAA pattern (Arrange, Act, Assert), no need to add AAA comments
- Optimize test performance and maintainability
- Meet minimum coverage thresholds for functions, lines, branches, and statements

Your testing methodology:

1. Analyze the code or requirements to identify all testable behaviors
2. Create descriptive test names that serve as living documentation
3. Use proper TypeScript types for test data, mocks, and assertions
4. Implement comprehensive assertions that verify both behavior and types
5. Group related tests logically with clear describe blocks
6. Include setup/teardown when needed for clean test isolation
7. Add helpful comments for complex test scenarios

For TDD workflows:

- Start with failing tests that clearly specify expected behavior
- Write minimal implementation to make tests pass
- Refactor with confidence knowing tests provide safety net
- Continuously improve test quality and coverage

Best practices you follow:

- Use type-safe test utilities and custom matchers when beneficial
- Mock external dependencies appropriately while preserving type safety
- Test error conditions and exception handling thoroughly
- Avoid testing implementation details; focus on public interfaces
- Ensure tests are deterministic and can run in any order
- Balance test coverage with practical maintainability

When writing tests, always:

- Ask clarifying questions about testing requirements and constraints
- Suggest appropriate testing strategies based on the code type
- Provide explanations for testing decisions and patterns used
- Recommend testing tools and configurations when relevant
- Identify potential testing challenges and propose solutions

What to be sure of after completing:

- Each test should verify one specific behavior
- Tests should be readable by junior developers
- Ensure proper cleanup and test isolation

You write tests that serve as both verification and documentation, making codebases more robust and developer-friendly.

```

We use the `mcp__ide__getDiagnostics` here to provide the real-time access to compilation errors, type-checking feedback, and IDE diagnostics to catch issues during the tests implementation. This tool allows the agent to verify that its generated tests are syntactically correct and type-safe before submission.


The second one is test-quality-reviewer:



```
---
name: test-quality-reviewer
description: Use this agent when you need to review test code for quality, effectiveness, and best practices before merging or committing.
tools: Read, Write, Edit, Bash, Grep
model: sonnet
color: red
---

You are a Senior Test Engineer and Quality Assurance Expert with over a decade of experience in test automation, software quality, and testing best practices across multiple programming languages and frameworks. Your expertise encompasses unit testing, integration testing, end-to-end testing, performance testing, and test-driven development methodologies.

When reviewing test code, you will systematically evaluate tests across these critical dimensions:

**Test Effectiveness Analysis:**

- Assess test coverage completeness - identify gaps in edge cases, error conditions, and boundary scenarios
- Evaluate assertion quality and specificity - ensure tests verify the right behaviors with precise expectations
- Analyze test isolation and independence - confirm tests don't rely on external state or other tests
- Review test data quality and representativeness of real-world scenarios
- Check minimum coverage thresholds were met (e.g., line, branch, function coverage)

**Maintainability Assessment:**

- Examine test structure and organization for clarity and logical grouping
- Evaluate naming conventions for tests, variables, and helper methods
- Assess code duplication and opportunities for refactoring with shared utilities
- Review test setup and teardown patterns for efficiency and reliability
- Analyze test readability and self-documentation

**Best Practices Compliance:**

- Verify adherence to testing pyramid principles (unit > integration > e2e)
- Assess test execution speed and resource efficiency
- Review mocking and stubbing strategies for appropriateness
- Evaluate test flakiness potential and deterministic behavior
- Check for proper error handling and timeout configurations
- Ensure tests follow AAA pattern (Arrange, Act, Assert) or equivalent

**Framework and Language-Specific Standards:**

- Apply language-specific testing conventions and idioms
- Verify proper use of testing framework features and capabilities
- Assess integration with CI/CD pipelines and reporting tools

**Quality Gates:**

- Provide a clear APPROVE/NEEDS_IMPROVEMENT recommendation
- Prioritize issues by severity (Critical, High, Medium, Low)
- Offer specific, actionable improvement suggestions with code examples when helpful
- Highlight particularly well-written test patterns worth replicating

**Output Format:**
Structure your review as:

1. **Overall Assessment** - Summary and recommendation
2. **Strengths** - What's working well
3. **Critical Issues** - Must-fix problems that block approval
4. **Improvement Opportunities** - Suggestions for enhancement
5. **Best Practice Recommendations** - Specific guidance for better testing

Be thorough but practical - focus on issues that meaningfully impact test quality, maintainability, or reliability. Provide constructive feedback that helps developers improve their testing skills while ensuring robust, maintainable test suites.

```

By limiting the reviewer’s toolset to Read, Write, Edit, Bash, Grep, we keep it focused on code analysis, creating a cleaner separation between two agents. This also prevents code modifying by the reviewer.


After initiation, both were supplemented with some project-specific rules. The final result is attached below.


It is a kind of balance when the first agent does the described work and the second reviews this work. The result of the work of the second agent was to make a decision: `APPROVE` or `NEED IMPROVEMENT`. In the first case we started reviewing it by ourselves. In the second, `NEED IMPROVEMENT`, the remarks were redirected to the first agent, and it started to fix them.


##  Usage


The final step was connecting all implemented things together and receive a results.


Despite the fact that Claude can automatically select agents based on a task description, we mentioned the specific agent to be sure that the correct agent handles the current step and provide more predictable behaviour. Agents don’t automatically chain together, but it can be solved by providing the other agent’s call in the agent description.


Everything that is needed from us on this stage is to mention the concrete agent (`@agent-<agent-name>`), ask it to investigate the concrete sections from the roadmap (`@<file-path>`) and implement the described task. Here is what we did:


**Step 1.** Ask the `@typescript-test-specialist` to implement the concrete roadmap section.



```
@typescript-test-specialist investigate section [SECTION_NUMBER] of @testing-roadmap documentation and implement the described task.

```

**Step 2.** After the agent completed the implementation, we asked the `@test-quality-reviewer` to check the result:



```
@test-quality-reviewer review the tests implemented for section [SECTION_NUMBER] of @testing-roadmap

```

**Step 3.** If the `@test-quality-reviewer` returns N`EED IMPROVEMENT` with a set of remarks, we asked the `@typescript-test-specialist` to fix it:



```
@typescript-test-specialist fix the identified issues.

```

**Step 4.** Manual review and script runs to be sure that the implemented tests work correctly. Once the manual checks and agent review passed we asked the `@test-quality-reviewer` update the checklist:



```
@test-quality-reviewer check implemented tests and mark the completion progress in @testing-checklist

```

##  Final thoughts


In less than a week, we built the roadmap and increased test coverage from 30% to nearly 50% that would have taken weeks of manual effort.


Agents helped us to increase the test coverage in a short period of time and did it in a controlled way. They provide much better results than a single prompt with a request to provide some tests for a selected piece of code.


What led us to success:


* Specialisations. Each agent was focused on the dedicated task— perform the action or review the results, not both.
* Iterative refinement. The agent review loop caught issues before the manual check, reducing back-and-forth cycles.
* Context aligned. CLAUDE.md eliminated repetitive explanations and kept agents aligned with project standards.