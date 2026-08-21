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

# Exploring Self-Healing Playwright Automation with AI — Looking for Suggestions

![rw-book-cover](https://www.redditstatic.com/desktop2x/img/favicon/android-icon-192x192.png)

## Metadata
- Author: [[Flaky_Vegetable_1613]]
- Full Title: Exploring Self-Healing Playwright Automation with AI — Looking for Suggestions
- Category: #articles
- Summary: A tester asked about using AI for self-healing Playwright tests to reduce flaky failures and script rewrites. Many replied that AI often guesses wrong, making issues harder to fix, and suggested better selectors and rerun strategies instead. Some think AI can help only with classifying failures or summarizing reports, but not reliably fix tests.
- URL: https://www.reddit.com/r/QualityAssurance/comments/1o67zw9/exploring_selfhealing_playwright_automation_with/

## Full Document
**[r/QualityAssurance](https://www.reddit.com/r/QualityAssurance/)**

### [Flaky\_Vegetable\_1613](https://www.reddit.com/user/Flaky_Vegetable_1613/)

 (2025-10-14 06:24:36)

Hey everyone,

I’ve been using **Playwright integrated with the Pytest framework** for about a year now. While it’s a powerful combo for end-to-end testing, I often run into challenges with **flaky tests** and **frequent product revamps or UI updates**.

These constant changes mean we end up **rewriting large portions of our test scripts** over and over again just to keep things stable — which eats up a lot of time and slows down automation coverage.

With the growing number of **AI tools and frameworks** emerging lately, I’m exploring how to **implement self-healing test scripts** — something that can automatically adapt when an element locator changes or when the test fails due to a minor UI shift.

If anyone here has experimented with **Agentic**-AI-driven self-healing automation (especially with Playwright + Pytest), I’d love to hear:

* What tools, libraries, or workflows worked for you?
* Any open-source or paid solutions you recommend?
* Gotchas or lessons learned from your experience?

Appreciate any insights or suggestions!

#### [TomatilloIcy3206](https://www.reddit.com/user/TomatilloIcy3206/)

 (2025-10-14 06:26:43)

We spent months trying to make self healing work with playwright. The AI stuff sounds cool but when you actually implement it, it's like.. the test breaks, the AI tries to guess what changed, and half the time it guesses wrong. Then you're debugging why the AI picked the wrong element instead of just fixing the locator yourself. We tried a few tools - testim had some self healing features, also looked at functionize. Both were expensive and honestly didn't save us that much time.

What we do now is just write better selectors from the start. Like instead of relying on classes that change every sprint, we add data-testid attributes to everything. Yeah it means working with the frontend team but it's worth it. Also we run our test suite on every PR so we catch breaks immediately instead of finding out 3 days later when half the tests are broken. The self healing dream is nice but in practice we found it easier to just prevent the breaks in the first place.

The flaky test thing though.. that never goes away. We have this whole system where if a test fails we automatically rerun it 2 more times before marking it as failed. Not elegant but it works. Also we tag tests that are known to be flaky and run them separately so they don't block deploys. One thing that helped was adding explicit waits everywhere - like wait for this specific element to be visible, wait for this API call to complete, etc. Playwright's auto waiting is good but not perfect especially when you have complex loading states.

##### [OTee\_D](https://www.reddit.com/user/OTee_D/)

 (2025-10-14 07:22:12)

The fundamental logical problem with AI:

How OK am I with the AI fucking up?

1. \_"Totally fine, it doesn't matter if it generates some strange or wrong results."\_  Even unattended AI is possible, all good.
2. \_"That would not be optimal, we must be certain we don't get bad data or reputation damage, because our result look like made by a toddler."\_  You need a human support process or other additional verification steps. Doable and may still save grunt work but the benefit of AI minimizes.
3. *"That is not acceptable. We would face financial or legal repercussions as possible errors would corrupt the following business processes steps."* (like wrongful tests producing defect systems, wrongful decisions leading to liability)  You are toast, AI adds a layer of complexity on top the complexity of the actual business process so your risk increases and the depth on needed verification and thus "work" increases as well.

#### [ajmalhinas](https://www.reddit.com/user/ajmalhinas/)

 (2025-10-14 12:11:16)

There’s a fundamental flaw in the idea of using AI for testing. **Tests, by definition, must be deterministic**, but **AI is inherently not deterministic**. That’s not a flaw in AI but it is an inherent nature. I believe that, at some point, AI will learn **when to behave like AI** and **when to behave like traditional logic**.In testing, you can automate the **process around validation** but not the **truth of the validation itself**. So human review is a must to determine what exactly is needed.

#### [PalpitationCalm9303](https://www.reddit.com/user/PalpitationCalm9303/)

 (2025-10-14 07:24:18)

How does the self healing work? What if the AI fixes the test but it was actually a bug in the application?

##### [Wookovski](https://www.reddit.com/user/Wookovski/)

 (2025-10-14 08:03:19)

Yeah also "self healing" implies the test is broken, when usually it's because the application has changed

##### [probablyabot45](https://www.reddit.com/user/probablyabot45/)

 (2025-10-14 11:38:43)

It doesn't work. This is still a huge problem I've never heard an explanation for. All they really do is update locators and its not even great at that. 

#### [Hanzoku](https://www.reddit.com/user/Hanzoku/)

 (2025-10-14 16:45:44)

Oh yay, more AI written dross. Anyone else noticed how AI likes to bold key phrases unlike how any human writes? Big giveaway is random fresh account as well.

##### [peebeesweebees](https://www.reddit.com/user/peebeesweebees/)

 (2025-10-14 18:49:56)

Yup, they’re everywhere on this sub.

##### [Flaky\_Vegetable\_1613](https://www.reddit.com/user/Flaky_Vegetable_1613/)

 (2025-10-14 16:59:13)

Hi am ai 😂

#### [Hopeful\_Flamingo\_564](https://www.reddit.com/user/Hopeful_Flamingo_564/)

 (2025-10-14 07:18:41)

Playwright TS came up with auto healing tests by default , try it?

#### [Dangerous\_Fix\_751](https://www.reddit.com/user/Dangerous_Fix_751/)

 (2025-10-14 11:56:41)

hey - yes there are maybe one or two companies that offer agentic fallback (wrap a Playwright script in an agent - if the script fails, then error is handled gracefully as the agent takes over). Most cost effective and correct way to use agents in the current landscape imo

##### [Flaky\_Vegetable\_1613](https://www.reddit.com/user/Flaky_Vegetable_1613/)

 (2025-10-14 12:02:35)

Would like to here from you if you have explore any.

#### [Flaky\_Vegetable\_1613](https://www.reddit.com/user/Flaky_Vegetable_1613/)

 (2025-10-14 07:52:19)

After going though your valuable comments I think instead of using AI to actually fix the issues, we can rather use it as a reporting system which can classify the failure atleast to an extent. As AI models are good at classification.

And also by the term AI. I was referring to models and api services which can be incorporated into a workflow. A simple example we can consider for this is n8n workflow + (llma2 or gpt models). We can design a flow and use the failure logs to help us classify the issue.  

I believe this saves time.

##### [probablyabot45](https://www.reddit.com/user/probablyabot45/)

 (2025-10-14 11:40:38)

I wouldn't even do that. Playwright tells you why the tests fails. You don't need AI and it feels like you're just trying to find a reason to use AI and are forcing it. 

###### [Flaky\_Vegetable\_1613](https://www.reddit.com/user/Flaky_Vegetable_1613/)

 (2025-10-14 11:49:27)

Thanks for the clarification.

###### [Flaky\_Vegetable\_1613](https://www.reddit.com/user/Flaky_Vegetable_1613/)

 (2025-10-14 11:49:09)

No I am not forcing just wanted to know if it works. Just wanted opinion XD.

###### [ajmalhinas](https://www.reddit.com/user/ajmalhinas/)

 (2025-10-14 13:01:28)

But we can use AI to summarise the reports for management.

###### [probablyabot45](https://www.reddit.com/user/probablyabot45/)

 (2025-10-14 13:19:23)

What do you expect those reports to say? 

###### [ajmalhinas](https://www.reddit.com/user/ajmalhinas/)

 (2025-10-14 13:38:29)

It’s more like an overview or a statement for chat message; it’s not really a report per se.

###### [probablyabot45](https://www.reddit.com/user/probablyabot45/)

 (2025-10-14 13:42:58)

So what do you expect them to say that a normal pass fail report doesn't? 

###### [ajmalhinas](https://www.reddit.com/user/ajmalhinas/)

 (2025-10-14 14:27:47)

Here’s a small glimpse from a large raw report that contains thousands of test cases. I ran this report through AI.

### Key Failing Areas

Failures are concentrated in the following functional areas, often due to data verification mismatches:

* **Supplier Management**: 28 failures
* **Purchase Verification**: 26 failures

### Common Failure Patterns

* **Data Mismatches**: Text verification failures (e.g., "Expected text 'X' actual 'Y'") in search and display operations.

### Passing Areas

All core CRUD operations for items and basic customer creation pass.

###### [probablyabot45](https://www.reddit.com/user/probablyabot45/)

 (2025-10-14 15:10:03)

So it's a pass fail report. You don't need AI for that. That's over engineering. 

###### [ajmalhinas](https://www.reddit.com/user/ajmalhinas/)

 (2025-10-14 15:15:04)

Do you mean to say that we can just use some statistical analysis.I dont think traditional tools can identify what is CRUD or give overview of failure pattern in a generic form. Can you eleborate bit more?

###### [probablyabot45](https://www.reddit.com/user/probablyabot45/)

 (2025-10-14 15:27:20)

I mean you can just use the out of the box playwright reports and get the exact same info. All you've created is a simple pass fail report with a fuck ton more steps.

######
