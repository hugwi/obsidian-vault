---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

https://victoria.dev/blog/do-i-raise-or-return-errors-in-python/

While it’s more idiomatic to `raise` errors in Python, there may be occasions where you find `return` to be more applicable.

For example, if your Python code is interacting with other components that do not handle exception classes, you may want to return a message instead. Here’s an example using a `try` … `except` statement:

![[Pasted image 20230530131511.png]]

https://lukeplant.me.uk/blog/posts/raising-exceptions-or-returning-error-objects-in-python/