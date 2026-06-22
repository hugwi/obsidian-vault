# Should we use custom exceptions in Python?

![rw-book-cover](https://miro.medium.com/v2/resize:fit:1200/0*iGAIZoa0bfZDff_z)

## Metadata
- Author: [[Marcin Kozak]]
- Full Title: Should we use custom exceptions in Python?
- Category: #articles
- Summary: Python has many built-in exceptions, but custom exceptions can make errors clearer and more related to your project. Custom exceptions are easy to create and can improve code readability and user understanding. While not always necessary, using custom exceptions thoughtfully can benefit your projects.
- URL: https://towardsdatascience.com/should-we-use-custom-exceptions-in-python-b4b4bca474ac

## Full Document
#### Python has so many built-in exceptions that we rarely need to create and use custom ones. Or do we?

![](https://miro.medium.com/v2/resize:fit:840/0*iGAIZoa0bfZDff_z)Custom exceptions: Own your own error. Photo by [Brett Jordan](https://unsplash.com/@brett_jordan?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com?utm_source=medium&utm_medium=referral)
Should we use custom exceptions or built-in ones? That’s a very good question, actually. Some say,

> Avoid custom exceptions at all costs. There are so many built-in exceptions that you seldom need a custom one, if ever.
> 
> 

Others say,

> Use custom exceptions in your projects. Leave built-in exceptions to typical situations in which they are raised, and raise custom ones to inform what went wrong in relation to the application, not the code itself.
> 
> 

Deitel and Deitel (2019) claim that one should use built-in exceptions. Kapil (2019) recommends using custom exceptions when one creates an interface or a library, as this helps diagnose problems that have occurred in the code. So does Bader (2017), explaining that custom exceptions help users when the code follows the [*it’s easier to ask for forgiveness than permission* coding strategy](https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/).

If you feel torn by this very situation, or if you’re simply interested in custom exceptions, this article is for you. We will discuss whether or not we should use custom exceptions in our projects, instead of using built-in exceptions whenever we can (so, basically, always). Before we continue, notice that this is not a choice between right and wrong. Rather, we will look for the golden rule, one which will help us find the right balance.

### **Defining a custom exception**

First, let’s see how to define a custom exception in Python. This is a simple task, as the only thing you need to do is to create a class that inherits from the built-in `Exception` class:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/eb8ce174eeb734d7e10dead4ece16060) 

I will show below that you can do more; but the truth is, most of the times I use just an empty class (actually, it’s not empty, as it inherits from `Exception`), as that’s all I need. Often, I add a descriptive docstring:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/6a704c4de63f070d1834aee7bc23e59e) 

As you can see, you do not need to use the `pass` statement if you add a docstring. You can also replace the `pass` statement with the ellipsis (`…`). The three versions work the same way. Choose whichever works better in a given situation, or whichever you prefer.

*Note how important naming is*. `PredictionError` seems to be quite a general custom exception to be used when something goes wrong during calculating predictions. Depending on your needs, you can create much more specific exceptions, but never forget to use informative names. A general rule in Python is to use short but informative names. Ironically, custom exceptions constitute an exception, as they often have long names. This is because most people — including myself — like to use self-standing exception names, and I think you should follow this rule too. Consider these pairs of informative and vague exception names:

* `NegativeValueToBeSquaredError` versus `SquaredError`
* `IncorrectUserNameError` versus `InputError`
* `OverloadedTruckError` and `NoLoadOnTruckError` versus `LoadError`

The names to the left are more specific and informative than those to the right. On the other hand, you could consider the right-hand-side exceptions as general errors from which those to the left can inherit; for instance:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/691529338182fccf0500ac914fe44efc) 

This is called *exception hierarchy*. Built-in errors also have their hierarchy. Exception hierarchy can serve an important purpose: When you create such a hierarchy, the user does not have to know all the specific exceptions (Lutz 2013). Instead, it’s enough to know, and catch, the general exception (in our example, it’s `LoadError`); it will make it possible to catch all exceptions that inherit from it (`OverloadTruckError` and `NoLoadOnTruckError`). Bader (2017) reinforces this recommendation, but warns not to make such a hierarchy too complicated.

Sometimes, however, it’s enough to go for simplicity:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/64803fed33da3047a1f9d41fadba5060) 

If you think that `NoLoadOnTruckError` should not be an error because trucks do sometimes have empty rides, you’re right. Do remember, however, that exceptions do not have to mean errors; they mean… well, they mean exceptions. However, this is a Python rule to end an exception class’s name with “Error”, and all built-in exceptions are named like that (e.g., `ValueError` or `OSError`).

### **Raising a custom exception**

Custom exceptions are raised in the same way as built-in ones. It’s worth, however, to remember that we can do it in several ways.

#### **Check a condition, raise if it’s not met**

An exception is raised when a particular condition is not met. You can do this with or without a message:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/71699e37e9e3f5366bf20f3f43e77feb) 

#### Catch a built-in exception and raise a custom one

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/440cf9bdb1a4fdbb171015c59dbc1998) 

Here, instead of raising `ZeroDivisionError`, we raise custom `EmptyVariable Error`. On one hand, this approach can be more informative, as it says what the problem was. On the other hand, it does not tell the whole story; that is to say, raising `EmptyVariableError` alone does not inform the user that the variable was empty and for this reason the division by zero occurred when calculating the mean value using `get_mean()`. The developer’s needs to decide whether or not the user should know such detailed information; sometimes, there is no such need, but other time the more information the traceback conveys, the better.

We can convey this information via a message provided along with `EmptyVariableError`, but there is a better way of doing this — the one described below.

#### **Catch a built-in exception and raise a custom one from it**

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/119380d7ff82ee64580a13ebcbfb6cd4) 

Here, we include both `EmptyVariableError` and `ZeroDivisionError` in the traceback; the only thing we changed is adding `as e` in the 10th line of the previous snippet and `from e` in the 11th line.

This version is much more informative, as it says more details: that the variable was empty, there were no data, and `ZeroDivisionError` was raised due to this lack of data when the mean was cacluated using `get_mean()`. Does `ZeroDivisionError: division by zero` say this? Definitely not directly, but you need to carefully analyze the traceback to see that indirectly.

Hence raising a custom exception from a built-in exception helps you to convey much more detailed information about what has happened.

### **Enriching custom exceptions**

Till now, we have used only bare custom exceptions. Despite being simple, this approach is highly customizable, which is thanks to the ability to use any message when raising an exception. We can, however, create a message that is built into the exception class. Then, you do not have to provide a message when raising an exception. Look here:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/e1147083e694e9cd3794b1547c9fecbf) 

So, if you do not provide `truck_no`, no message will be used. When you do, `NoLoadOnTruckError` would be raised with message `"The truck 12333 is empty"`. This is a simple example; you can read more about this topic [here](https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca).

I use this approach in only one situation: when otherwise I would have to use the same long message in several places in code, where I raise this exception. Then, extending such an exception class with a built-in message makes sense, but I keep the class as simple as possible, trying not to complicate its code.

In other situations, however, more often than not I use just an empty class that inherits from the `Exception` base class: the simplest solution that offers what I need. Enriched exception classes can become complicated, despite not offering richer functionality. Besides, such a class cannot be customized further; you can only omit a message or use the one built into the class, but you cannot use a different one. Allowing for this would make the class even more complicated.

### **Example**

Now that we know how to define custom exceptions, let’s see them in action.

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/ab533cb9bc8b480c8aaee5f38b1dfa7f) 

First, note that I changed the way I present the code, with commands starting with `>>>`. This is how you format code and its output in the`[doctest](https://docs.python.org/3/library/doctest.html)`, a built-in module for documentation testing. Not only can you run the documents as `doctest` tests, in order to see if the code works fine, but also you can easily distinguish the code and its output.

I decided to use type aliases in type hints. [In my opinion, such type hints are more readable than complex type hints added directly into the function’s signature](https://betterprogramming.pub/pythons-type-hinting-friend-foe-or-just-a-headache-73c7849039c7). Thus, we have the `TimeSeriesDates` and `TimeSeriesValues` types, both being lists, the former of `datetime.datetime.date` objects while the latter of floating-point numbers.

Then, I created `IncorrectTSDataError`, which is an exception to be used when the time-series data are incorrect. Note that we use the same exception class in three different situations in which data are incorrect. This is a simple solution that in this simple situation is sufficient. We could create an exception hierarchy, with three custom exceptions inheriting from `IncorrectTSDataError`. In your project, however, perhaps a more complex exception hierarchy will work better.

Then, the main model-building function, `build_model()`, is defined. It’s a simplified function, of course, and it does only two things:

* checks if the data are correct: `ts` is not missing, `y` is not missing, and `ts` and `y` have the same lengths; and
* builds the model (which is represented by the `run_model()` function).

We could move the checking code to a dedicated function (e.g., `check_data()`), and I would definitely do this if the code of `build_model()` gets much longer.

If one of the checks fails, the function will throw the `IncorrectTSDataError` exception, with the message depending on what went wrong. Otherwise, the function proceeds and calls the `run_model()` function. Of course, the data check is overly simplistic here, as it serves only the presentation purpose. We could check if the data are indeed a `datetime.datetime.date` list; we could check if the number of points is enough to build a forecasting model; and the like.

Now, look at how we’re running the `run_model()` function: We do so using a `try-except` block, in order to be able to catch any error thrown during this process. When we catch an error, we do not silence it but re-raise it, raising `PredictionError` from it: `raise PredictionError from e`. For simplicity, I did not include the message in the error. That way, the original error will be included in the traceback.

To run this and see how this works, we need the `run_model()` function. Let’s create its mock that will only raise an error (here, `ValueError`).

> [A *mock*](https://en.wikipedia.org/wiki/Mock_object) of an object is its artificial representation that mimics the behavior of the original object, in our case, the `run_model()` function. This means we do not need the whole object (function), just its mock that will do what we need to mimic. Here, it’s enough for it to raise `ValueError`.
> 
> 

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/90bbebab00876211ecfacc9901d3e78d) 

That way, whenever we run the function, it will raise `ValueError`:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/37c3d036c2bfade3438d7d768f16c2f8) 

This is our app in action. We will generate the values from a univariate distribution, so there will unlikely be a trend in the data.

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/3e6c7ea737287417f11a004d6cd770ff) 

The full traceback from lines 23–25 looks like this (with the ellipses used instead of paths, names etc.):

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/8d1cae21b39ebe14236a4ad5c90d3239) 

We should now look at what the traceback would look like with a built-in exception raised instead of `PredictionError`. We need to change the `build_model()` function first:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/dddb69bba7aa2b086a3651c43aeb5d26) 

This version of the `build_model()` function, actually, does not make much sense, because it simply calls `run_model()`. It could, however, do more; for example, it could check the data or conduct data preprocessing.

Let’s check out the traceback in the very same scenarios as above:

Some content could not be imported from the original document. [View content ↗](https://towardsdatascience.com/media/2ed063561fe1c01b7ffa2c2c9d56aec0) 

Look at the graph below to compare the two tracebacks:

![Two tracebacks, divided by a vertical grey line.](https://miro.medium.com/v2/resize:fit:840/1*cJip7VEskq0n2tZQBulNCg.png)To the left, the traceback when a custom exception was used. To the right, built-in ValueError was used. Source: Author. 
Pay attention to the following:

* The traceback using the custom exception provided the original error (`ValueError`), but explained it using the custom `PredictionError` exception with a customized message.
* At the same time, the part with original `ValueError` was concise and much easier to read than the corresponding traceback when the built-in exception class used.

Do you agree with me that the traceback with the custom exception is clearer?

The `raise MyException from AnotherExcepion` syntax is extremely powerful, as it enables you to show both the root exception’s traceback, and the custom exception’s traceback. That way, the traceback can be far more informative in terms of the problem that led to the error than the traceback obtained when using a built-in exception only.

### **Conclusion**

Custom exceptions are easy to create, especially when you do not go into all the fuss of adding the `.__init__()` and `.__str__()` methods. This is one of these rather rare situations in which less code means more functionality. More often than not, an empty class inheriting from the `Exception` class is the way to go.

But also with an empty class, you need to make a decision: whether or not to write a docstring. (The decision as to whether to choose the `pass` statement or the ellipsis does not matter at all, so we can ignore it.) And the answer is, it depends. It depends on what you expect from your class. If it’s to be a general class that will serve different exceptions, then you may need a docstring that will say this. If you choose this option, however, you need to consider whether several more precise exception classes would do the job better. I am not saying they will, because often you will not want to use 50 custom exceptions; unlike with $100 bills in your wallet, sometimes five is better than 50.

One more thing makes a difference: a good, informative name. If you use a good name, your exception class may be self-standing even without a docstring and a message. Even if you do need a docstring and a message, your exception still needs a good name. One good thing is that exception classes can have longer names than a typical Python object. So, `IncorrectAlphaValueError` and `MissingAlphaValueError` do not even seem to be long.

What is really great is `raise from`, which enables us to raise our custom exception from the exception that was raised inside the code. This functionality lets us include two parts in the traceback: one that is related to the exception raised originally (it does not have to be built-in, though), which shows what happened and where it happened; we can call it the basic source of the error. A second part is related to our custom exception, which in fact *explains* to the user what really happened, using the words related to the project. Combining these two parts makes the traceback powerful.

It makes a difference, however, whether you work on a package you want to offer to others, a business project, or anything else (e.g., a notebook presenting a report with some analyses). To explain in further detail:

1. *A package to be used by others*. Such packages often will benefit from custom exceptions. They need to be well-designed and wisely used, so that they can accurately show what has gone wrong and where.
2. *A business project*. Custom exceptions are usually a good choice. Built-in exceptions offer information about Python-related problems, and custom exceptions will add information about project-related problems. That way, you can design your code (and traceback, if an exception is raised) in a way that combines Python code with the language of the project.
3. *Lightweight code*, like in a notebook. Similarly, this can be code of a script, or even a snippet, to be used once or twice. More often than not, custom exceptions would be an overkill, unnecessarily complicating the code. Notebooks usually do not need such far-going exception handling; so, in such situations, you will seldom need to create custom exceptions.

Of course, there will always be exceptions to these rules, so choose the best approach in a particular situation based on your experience and the details of your project. But ***do not be afraid of using custom exceptions***, as they can greatly benefit your projects.

I hope you have enjoyed this article. Somehow, many books silently omit this topic, not even mentioning custom exceptions. There are counter-examples, of course, like the books I referred to in the text. I feel, however, that most authors do not consider custom exceptions a topic interesting and/or important enough to discuss. My opinion is opposite, for the simple reason that I’ve found custom exceptions valuable in quite a few projects. If one has not ever tried to use custom exceptions, maybe it’s time to do it and check oneself how they work.

In my eyes, custom exceptions offer a fantastic tool for diagnosing problems. Python is known for its readability and user-friendliness; using custom exceptions can help us improve this even more, especially when we are designing our package. If you decide to avoid, at all costs, custom exceptions by using only built-in ones, you risk decreasing Python’s readability.

Thus, I hope that from now on, you will not be afraid to create your own exception classes. When you work on an interface or a package, do not be afraid to create a nested hierarchy of exception classes. Sometimes, however, you will not need custom exceptions. The point is that it’s always good to consider whether or not your Python project would benefit from custom exceptions. If you do decide to use them, remember to not overdo complexity, and never forget [the Zen of Python](https://peps.python.org/pep-0020/): “Simple is better than complex,” and “Flat is better than nested.”

### Resources

* Bader D. (2017). *Python Tricks: A Buffet of Awesome Python Features*. BookBaby.
* Deitel P., Deitel H. (2019). *Python for Programmers: with Big Data and Artificial Intelligence Case Studies*. Pearson Education.
* Kapil S. (2019). *Clean Python: Elegant Coding in Python*. APress Media.
* Lutz M. (2013). *Learning Python*. 5nd edition. O’Reilly Media.
* <https://towardsdatascience.com/how-to-define-custom-exception-classes-in-python-bfa346629bca>
* <https://devblogs.microsoft.com/python/idiomatic-python-eafp-versus-lbyl/>
* <https://betterprogramming.pub/pythons-type-hinting-friend-foe-or-just-a-headache-73c7849039c7>
* <https://docs.python.org/3/library/doctest.html>
* <https://peps.python.org/pep-0020/>
* <https://en.wikipedia.org/wiki/Mock_object>
