---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, software-engineering]
tags:
  - patterns
  - testing
source: readwise
created: 2026-06-23
rating: 
action: 
theme: quality-gates
subtheme:
  - automated-tests
---

# emilybache/Theatrical-Players-Refactoring-Kata: Example from first chapter of 'Refactoring' by Martin Fowler, with tests and translations

![rw-book-cover](https://opengraph.githubassets.com/3a77506b46c72ac6ad1fbebfd0dc749f666bf17ca2a5d1f8193e79d9cdb89370/emilybache/Theatrical-Players-Refactoring-Kata)

## Metadata
- Author: [[https://github.com/emilybache/]]
- Full Title: emilybache/Theatrical-Players-Refactoring-Kata: Example from first chapter of 'Refactoring' by Martin Fowler, with tests and translations
- Category: #articles
- Summary: This GitHub repo offers a coding exercise from Martin Fowler's book "Refactoring" with tests in multiple languages. It helps you practice changing code, like adding HTML output and new play types. The author added tests using Approval testing to support safe refactoring.
- URL: https://github.com/emilybache/Theatrical-Players-Refactoring-Kata

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/emilybache/Theatrical-Players-Refactoring-Kata?resume=1) 

#### Create list

### emilybache/Theatrical-Players-Refactoring-Kata

main

tT

Go to file

Code

Open more actions menu

*Support this and all my katas via [Patreon](https://www.patreon.com/EmilyBache)*

### Theatrical Players Refactoring Kata

The first chapter of ['Refactoring' by Martin Fowler, 2nd Edition](https://www.thoughtworks.com/books/refactoring2) contains a worked example of this exercise, in javascript. That chapter is available to download for free. This repo contains the starting point for this exercise in several languages, with tests, so you can try it out for yourself.

I made a video ["Refactoring with Martin Fowler | Theatrical Players Code Kata"](https://youtu.be/TjIrKEaOiVw) that explains a little bit about the exercise and why you should give it a try.

#### What you need to change

Refactoring is usually driven by a need to make changes. In the book, Fowler adds code to print the statement as HTML in addition to the existing plain text version. He also mentions that the theatrical players want to add new kinds of plays to their repertoire, for example history and pastoral.

#### Automated tests

In his book Fowler mentions that the first step in refactoring is always the same - to ensure you have a solid set of tests for that section of code. However, Fowler did not include the test code for this example in his book. I have used an [Approval testing](https://medium.com/97-things/approval-testing-33946cde4aa8) approach and added some tests. I find Approval testing to be a powerful technique for rapidly getting existing code under test and to support refactoring. You should review these tests and make sure you understand what they cover and what kinds of refactoring mistakes they would expect to find.

#### Acknowledgements

Thankyou to Martin Fowler for kindly giving permission to use his code.
