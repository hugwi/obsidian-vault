---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---

## Create a python package
https://py-pkgs.org/03-how-to-package-a-python#

## Package Versioning

https://blog.inedo.com/python/best-practices-for-versioning-python-packages-in-the-enterprise/

### Best Practice: Approximate Semantic Versioning 

Python’s versioning specifications were designed to be flexible and support a wide range of different versioning schemes. However, we recommend following a three-part versioning scheme like [Semantic Versioning](https://semver.org/) (SemVer).

While Python doesn’t fully support SemVer, you can still create three-part versions in the same manner. Semantic Versioning works by structuring each version identifier into three parts, MAJOR, MINOR, and PATCH. Each of these parts is managed as a number and incremented according to the following rules: 

- **Major** releases (5.0.0) indicate changes that will be incompatible with previous versions. 
- **Minor** releases (5.1.0) add functionality while still being backward-compatible (in this example 5.1.0 would be compatible with 5.0.0). 
- **Patch** (often termed Micro in Python) releases are minor bug fixes or security patches that should always be backward compatible (5.1.4).


## What Can Go Wrong When Updating to Python’s Latest Bugfix Version?[](https://realpython.com/python-bugfix-version/#what-can-go-wrong-when-updating-to-pythons-latest-bugfix-version "Permanent link")

Python maintenance releases only introduce a few types of changes. The focus is on fixing bugs and security issues. There shouldn’t be any new features or changes in how existing functions behave.

Still, you should always run your tests after updating to a new Python version. If you don’t have a lot of tests in your hobby project, then at least run your code to confirm that nothing obvious has changed.

While the risk of running into issues is low, there are a few possible scenarios that you should be aware of.

Python is a complex piece of software, and there are times when fixing one bug introduces another. Some bugfix versions may contain unexpected **regressions**. For example, [Python 3.10.3](https://www.python.org/downloads/release/python-3103/) introduced a [bug](https://github.com/python/cpython/issues/91124) that made Python unusable on an older [Red Hat Enterprise Linux](https://www.redhat.com/en/technologies/linux-platforms/enterprise-linux) version.

Python’s core team handled the regression and released [Python 3.10.4](https://www.python.org/downloads/release/python-3104/) earlier than planned.

Sometimes, you may have unconsciously been relying on the behavior of a bug in Python. If that bug is fixed, then you’ll find that your code stops working. In this case, you need to update your code. It may be tempting to leave your code alone and stop updating Python instead. Doing so will work in the short term, but it isn’t a sustainable solution.

While rare, it sometimes happens that a **security fix affects your code**. For example, [Python 3.10.7](https://www.python.org/downloads/release/python-3107/) disallows conversion between string and integer types for very large integers. Python introduced [the fix](https://github.com/python/cpython/issues/95778) to prevent a certain kind of attack. However, this also meant that some code valid in earlier versions of Python [no longer worked](https://realpython.com/python-news-september-2022/#python-introduced-a-breaking-change-to-fix-a-vulnerability).

Making such significant changes in a bugfix version is [controversial](https://discuss.python.org/t/int-str-conversions-broken-in-latest-python-bugfix-releases/18889) and doesn’t happen often. It’s not fun if your project is affected by such a change. Still, your best option is to update your code to continue using the latest bugfix versions.


## [Version 


A version specifier consists of a series of version clauses, separated by commas. For example:

`~= 0.9, >= 1.0, != 1.3.4.*, < 2.0`

The comparison operator determines the kind of version clause:

- `\~=`: [Compatible release](https://peps.python.org/pep-0440/#compatible-release) clause
- `\==` - : [Version matching](https://peps.python.org/pep-0440/#version-matching) clause
- `!=`: [Version exclusion](https://peps.python.org/pep-0440/#version-exclusion) clause
- `<=`, `>=`: [Inclusive ordered comparison](https://peps.python.org/pep-0440/#inclusive-ordered-comparison) clause
- `<`, `>`: [Exclusive ordered comparison](https://peps.python.org/pep-0440/#exclusive-ordered-comparison) clause
- `\===`: [Arbitrary equality](https://peps.python.org/pep-0440/#arbitrary-equality) clause.


For example, the following groups of version clauses are equivalent:

```python
~= 2.2
>= 2.2, == 2.*

~= 1.4.5
>= 1.4.5, == 1.4.*
```


For example, the following groups of version clauses are equivalent:

```python
~= 2.2
>= 2.2, == 2.*

~= 1.4.5
>= 1.4.5, == 1.4.*
```


The use of `'=='` (without at least the wildcard suffix) when defining dependencies for published distributions is strongly discouraged as it greatly complicates the deployment of security fixes. The strict version comparison operator is intended primarily for use when defining dependencies for repeatable _deployments of applications_ while using a shared distribution index.