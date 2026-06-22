# Exhaustiveness Checking with Mypy

![rw-book-cover](https://hakibenita.com/images/01-python-mypy-exhaustive-checking.png)

## Metadata
- Author: [[Haki Benita]]
- Full Title: Exhaustiveness Checking with Mypy
- Category: #articles
- Summary: Mypy can check if you handle all possible cases in your code using a function called assert_never. This helps catch missing cases in enums or union types before running the program. It works by narrowing types and showing errors when some cases are not handled.
- URL: https://hakibenita.com/python-mypy-exhaustive-checking

## Full Document
[Mypy](https://mypy-lang.org/) is an optional static type checker for Python. It's been around since 2012 and is gaining traction even since. One of the main benefits of using a type checker is getting errors at "compile time" rather than at run time.

Exhaustiveness checking is a common feature of type checkers, and a very useful one! In this article I'm going to show you **how you can get mypy to perform exhaustiveness checking!**

![Playing cards are also useful for explaining enumeration types...<br><small>Photo by <a href="https://unsplash.com/photos/G6wlppP4EN8">Daniel Rykhev</a></small>](https://hakibenita.com/images/01-python-mypy-exhaustive-checking.png)Playing cards are also useful for explaining enumeration types...
Say you have a system to manage orders. To represent the status of an order, you have the following enum:

```
import enum

class OrderStatus(enum.Enum):
    Ready = 'ready'
    Shipped = 'shipped'

```

You also have the following code to process an `Order`:

```
def handle_order(status: OrderStatus) -> None:
    if status is OrderStatus.Ready:
        print('ship order')

    elif status is OrderStatus.Shipped:
        print('charge order')

```

When the order is ready, you ship it; and when it's shipped, you charge it.

A few months go by and your system becomes big. So big in fact, that you can no longer ship orders immediately, and you add a new status:

```
import enum

class OrderStatus(enum.Enum):
    Ready = 'ready'
    Scheduled = 'scheduled'
    Shipped = 'shipped'

```

Before you push this change to production, you run a quick check with mypy to make sure everything is OK:

```
$ mypy main.py
Success: no issues found in 1 source file

```

Mypy does not see anything wrong in this code, Do you? The problem is that **you forgot to handle the new status in your function**.

One way to make sure you always handle all possible order statuses is to add an assert, or throw an exception:

```
def handle_order(status: OrderStatus) -> None:
    if status is OrderStatus.Ready:
        print('ship order')

    elif status is OrderStatus.Shipped:
        print('charge order')

    assert False, f'Unhandled status "{status}"'

```

Now, when you execute the function with the new status `OrderStatus.Scheduled`, you will get a runtime error:

```
>>> handle_order(OrderStatus.Scheduled)
AssertionError: Unhandled status "OrderStatus.Scheduled"

```

Another way to with deal with cases like this is to go over your test suite and add scenarios in all the places that use order status. But... if you forgot to change the function when you added the status, what are the chances you'll remember to update the tests? That's not a good solution...

**Exhaustiveness Checking in Mypy**

What if mypy could warn you at "compile time" about such cases? Well... it can, using this little magic function:

```
from typing import NoReturn
import enum

def assert_never(value: NoReturn) -> NoReturn:
    assert False, f'Unhandled value: {value} ({type(value).__name__})'

```

Before you dig into the implementation, try to use it to see how it works. In the function above, place `assert_never` after you handled all the possible order statuses, where you previously used `assert` or raises an exception:

```
def handle_order(status: OrderStatus) -> None:
    if status is OrderStatus.Ready:
        print('ship order')

    elif status is OrderStatus.Shipped:
        print('charge order')

    else:
        assert_never(status)

```

Now, check the code with Mypy:

```
$ mypy main.py
error: Argument 1 to "assert_never" has incompatible type "Literal[OrderStatus.Scheduled]";
expected "NoReturn"
Found 1 error in 1 file (checked 1 source file)

```

Amazing! **Mypy warns you about a status you forgot to handle!** The message also includes the value, `OrderStatus.Scheduled`. If you use a modern editor such as VSCode you can get these warnings immediately as you type:

![mypy Error in VSCode](https://hakibenita.com/images/00-python-mypy-exhaustive-checking.png)mypy Error in VSCode
You can now go ahead and fix your function to handle the missing status:

```
def handle_order(status: OrderStatus) -> None:
    if status is OrderStatus.Pending:
        print('schedule order')

    elif status is OrderStatus.Scheduled:
        print('ship order')

    elif status is OrderStatus.Shipped:
        print('charge order')

    else:
        assert_never(status)

```

Check with mypy again:

```
$ mypy main.py
Success: no issues found in 1 source file

```

Great! You can now rest assure you handled all order statuses. The best part is that you did that with **no unit tests**, and there were **no runtime errors**. If you include mypy in your CI, the **bad code will never make it into production**.

In the previous section you used mypy to perform exhaustiveness check on an `Enum`. You can use mypy, and `assert_never` to perform exhaustiveness check on other enumeration types as well.

**Exhaustiveness Checking of a Union**

A `Union` type represents several possible types. For example, a function that casts an argument to `float` can look like this:

```
from typing import Union

def get_float(num: Union[str, float]) -> float:
    if isinstance(num, str):
        return float(num)

    else:
        assert_never(num)

```

Check the function with mypy:

```
$ mypy main.py
error: Argument 1 to "assert_never" has incompatible type "float"; expected "NoReturn"

```

Whoops... you forgot to handle the `float` type in the code:

```
from typing import Union

def get_float(num: Union[str, float]) -> float:
    if isinstance(num, str):
        return float(num)

    elif isinstance(num, float):
        return num

    else:
        assert_never(num)

```

Check again:

```
$ mypy main.py
Success: no issues found in 1 source file

```

Great! mypy is happy...

**Exhaustiveness Checking of a Literal**

Another useful type is `Literal`. It is included in the built-in `typing` module since Python3.8, and prior to that it is part of the complementary [`typing_extensions` package](https://pypi.org/project/typing-extensions/).

A `Literal` is used to type primitive values such as strings and numbers. `Literal` is also an enumeration type, so you can use exhaustiveness checking on it as well:

```
from typing_extensions import Literal

Color = Literal['R', 'G', 'B']

def get_color_name(color: Color) -> str:
    if color == 'R':
        return 'Red'
    elif color == 'G':
        return 'Green'
    # elif color == 'B':
    #     return 'Blue'
    else:
        assert_never(color)

```

Checking the code without the commented part will produce the following error:

```
$ mypy main.py
error: Argument 1 to "assert_never" has incompatible type "Literal['B']"; expected "NoReturn"

```

Very handy indeed!

Now that you've seen what `assert_never` can do, you can try and understand how it works. `assert_never` works alongside **"type narrowing"**, which is a mypy feature where the type of a variable is narrowed based on the control flow of the program. In other words, mypy is gradually eliminating possible types for a variable.

First, it's important to understand how various things translate to a `Union` type in mypy:

```
Optional[int]
# Equivalent to Union[int, None]

Literal['string', 42, True]
# Equivalent to Union[Literal['string'], Literal[42], Literal[True]]

class Suit(Enum):
    Clubs = "♣"
    Diamonds = "♦"
    Hearts = "♥"
    Spades = "♠"

Suit
# ~Equivalent to Union[
#   Literal[Suit.Clubs],
#   Literal[Suit.Diamonds],
#   Literal[Suit.Hearts],
#   Literal[Suit.Spades]
# ]

```

To display the type of an expression, mypy provides a useful utility called [`reveal_type`](https://mypy.readthedocs.io/en/stable/common_issues.html#reveal-type). Using `reveal_type` you can ask mypy to show you the inferred type for a variable at the point it's called:

```
def describe_suit(suit: Optional[Suit]) -> str:
    # Revealed type is Union[Suit, None]
    reveal_type(suit)

```

In the function above, the reveled type of `suit` is `Union[Suit, None]`, which is the type of the argument `suit`.

At this point you haven't done anything in the function, so mypy is unable to narrow down the type. Next, add some logic and see how mypy narrows down the type of the variable `suit`:

```
def describe_suit(suit: Optional[Suit]) -> str:
    assert suit is not None
    # Revealed type is Suit
    reveal_type(suit)

```

After eliminating the option of suit being `None`, the revealed type is `Suit`. Mypy used your program's logic to narrow the type of the variable.

Keep in mind, the type `Suit` is equivalent to the type `Union[Literal[Suit.Clubs], Literal[Suit.Diamonds], Literal[Suit.Hearts], Literal[Suit.Spades]]`, so next, try to narrow down the type even more:

```
def describe_suit(suit: Optional[Suit]) -> str:
    assert suit is not None

    if suit is Suit.Clubs:
        # Revealed type is Literal[Suit.Clubs]
        reveal_type(suit)
        return "Clubs"

    # Revealed type is Literal[Suit.Diamonds, Suit.Hearts, Suit.Spades]
    reveal_type(suit)

```

After checking if `suit` is `Suit.Clubs`, mypy is able to narrow down the type to `Suit.Clubs`. Mypy is also smart enough to understand that if the condition does not hold, the variable *is definitely not* `Clubs`, and narrows down the type to `Diamonds`, `Hearts` or `Spades`.

Mypy can also use other conditional statements to further narrow the type, for example:

```
def describe_suit(suit: Optional[Suit]) -> str:
    assert suit is not None

    if suit is Suit.Clubs:
        # Revealed type is Literal[Suit.Clubs]
        reveal_type(suit)
        return "Clubs"

    # Revealed type is Literal[Suit.Diamonds, Suit.Hearts, Suit.Spades]
    reveal_type(suit)

    # `and`, `or` and `not` also work.
    if suit is Suit.Diamonds or suit is Suit.Spades:
        # Revealed type is Literal[Suit.Diamonds, Suit.Spades]
        reveal_type(suit)
        return "Diamonds or Spades"

    # Revealed type is Literal[Suit.Hearts]
    reveal_type(suit)

```

By the end of the function, mypy narrowed down the type of `suit` to `Suit.Hearts`. If, for example, you add a condition that imply a different type for `suit`, mypy will issue an error:

```
def describe_suit(suit: Optional[Suit]) -> str:
    assert suit is not None

    if suit is Suit.Clubs:
        # Revealed type is Literal[Suit.Clubs]
        reveal_type(suit)
        return "Clubs"

    # Revealed type is Literal[Suit.Diamonds, Suit.Hearts, Suit.Spades]
    reveal_type(suit)

    # `and`, `or` and `not` also work.
    if suit is Suit.Diamonds or suit is Suit.Spades:
        # Revealed type is Literal[Suit.Diamonds, Suit.Spades]
        reveal_type(suit)
        return "Diamonds or Spades"

    # Revealed type is Literal[Suit.Hearts]
    reveal_type(suit)

    # mypy error [comparison-overlap]: Non-overlapping identity check
    # left operand type: "Literal[Suit.Hearts]"
    # right operand type: "Literal[Suit.Diamonds]"
    if suit is Suit.Diamonds:
        # mypy error [unreachable]: Statement is unreachable
        return "Diamonds"

```

After mypy narrowed down the type of `suit` to `Literal[Suit.Hearts]`, it knows the next condition `suit is Suit.Diamonds` will always evaluate to False, and issues an error.

Once all the possibilities have been narrowed-out, the rest of the function becomes unreachable:

```
def describe_suit(suit: Optional[Suit]) -> str:
    assert suit is not None

    if suit is Suit.Clubs:
        return "Clubs"

    if suit is Suit.Diamonds or suit is Suit.Spades:
        return "Diamonds or Spades"

    if suit == Suit.Hearts:
        return 'Hearts'

    # This is currently unreachable
    assert_never(suit)

```

`assert_never` works by taking an argument of type `NoReturn`, which is only possible when the argument type is "empty". That is, when all possibilities have been narrowed-out and the statement is unreachable. If the statement does become reachable, then the `NoReturn` is not allowed and mypy issues an error. To illustrate, remove the last condition and check the code with mypy:

```
def describe_suit(suit: Optional[Suit]) -> str:
    assert suit is not None

    if suit is Suit.Clubs:
        return "Clubs"

    if suit is Suit.Diamonds or suit is Suit.Spades:
        return "Diamonds or Spades"

    # if suit == Suit.Hearts:
    #     return 'Hearts'

    # mypy error: Argument 1 to "assert_never" has
    # incompatible type "Literal[Suit.Hearts]"; expected "NoReturn"
    assert_never(suit)

```

Mypy narrowed down the type of `suit` to `Suit.Hearts`, but `assert_never` expects `NoReturn`. This mismatch triggers the error, which **effectively performs exhaustiveness checking** for `suit`.

In 2018 [Guido though `assert_never` is a pretty clever trick](https://github.com/python/mypy/issues/5818#issuecomment-431863917), but it never made it into mypy. Instead, exhaustiveness checking will become officially available as part of mypy if/when [PEP 622 - Structural Pattern Matching](https://www.python.org/dev/peps/pep-0622/) is implemented. Until then, you can use `assert_never` instead.

Django provides a very useful attribute to most model field types called [`choices`](https://docs.djangoproject.com/en/3.1/ref/models/fields/#choices):

```
from django.db import models
from django.utils.translation import gettext_lazy as _

class Order(models.Model):

    status: str = models.CharField(
        max_length = 20,
        choices = (
            ('ready', _('Ready')),
            ('scheduled', _('Scheduled')),
            ('shipped', _('Shipped')),
        ),
    )

```

When you provide choices to a field, Django adds all sorts of nice things to it:

* Add a validation check to `ModelForm` (which are used by Django admin, among others)
* Render the field as a `<select>` html element in forms
* Add a `get_{field}_display_name` method to get the description

However, mypy can't know that a Django field with choices has a limited set of values, so it cannot perform exhaustiveness checking on it. To adapt our example from before:

```
# Will not perform exhaustiveness checking!
def handle_order(order: Order) -> None:
    if order.status == 'ready':
        print('ship order')

    elif order.status == 'shipped':
        print('charge order')

    else:
        assert_never(status)

```

The function is not handling the status "scheduled", but mypy can't know that.

One way to overcome this is to use an enum to generate the choices:

```
import enum
from django.db import models

class OrderStatus(enum.Enum):
    Ready = 'ready'
    Scheduled = 'scheduled'
    Shipped = 'shipped'

class Order(models.Model):
    status: str = models.CharField(
        max_length = 20,
        choices = ((e.value, e.name) for e in OrderStatus),
    )

```

Now, you can achieve exhaustiveness checking with a slight change to the code:

```
def handle_order(order: Order) -> None:
    status = OrderStatus(order.status)

    if status is OrderStatus.Pending:
        print('ship order')

    elif status is OrderStatus.Shipped:
        print('charge order')

    else:
        assert_never(status)

```

The tricky part here is that the model field `status` is actually a string, so to achieve exhaustiveness checking you have to turn the value into an instance of the `OrderStatus` enum. There are two downsides to this approach:

1. **You have to cast the value every time**: This is not very convenient. This can possibly be solved by implementing a custom "Enum field" in Django.
2. **The status descriptions are not translated**: Previously you used gettext (`_`) to translate the enum values, but now you just used the description of the enum.

While the first is still a pain, the second issue was addressed in Django 3.1 with the addition of [Django enumeration types](https://docs.djangoproject.com/en/3.1/ref/models/fields/#enumeration-types):

```
from django.db import models

class OrderStatus(models.TextChoices):
    Ready = 'ready', _('Ready')
    Scheduled = 'scheduled', _('Scheduled')
    Shipped = 'shipped', _('Shipped')

class Order(models.Model):
    status: str = models.CharField(
        max_length = 20,
        choices = OrderStatus.choices,
    )

```

Notice how you replaced the enum with a `TextChoices`. The new enumeration type looks a lot like an Enum (it actually extends Enum under the hood), but it let's you provide a tuple with a value and a description instead of just the value.

After publishing this article a few readers suggested ways to improve the implementation, so I made the following edits:

1. **2020-12-09**: The initial version of the article had `assert_never` take a value of type `NoReturn`. [A commenter on Lobsters](https://lobste.rs/s/1un01t/exhaustiveness_checking_with_mypy#c_ws1qku) made an excellent suggestion to use the more intuitive `Union[()]` type instead. This also results in a better error message.
2. **2020-12-09**: The initial version of the article used `assert False, ...` in `assert_never` instead of `raise AssertionError(...)`. [A commenter on Lobsters](https://lobste.rs/s/1un01t/exhaustiveness_checking_with_mypy#c_l3obsb) mentioned that `assert` statements are removed when python is run with the `-O` flag. Since the `assert` in `assert_never` should not be removed, I changed it to `raise AssertionError` instead.
3. **2020-12-10**: After looking some more, [tmcb found](https://lobste.rs/s/1un01t/exhaustiveness_checking_with_mypy#c_oeezlr) that `Union[()]` is not currently accepted by Python *at runtime*, so I reverted the argument to `NoReturn` again.
