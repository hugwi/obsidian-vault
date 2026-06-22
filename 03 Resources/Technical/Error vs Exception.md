https://www.educative.io/answers/what-is-the-difference-between-errors-and-exceptions-in-java

Errors and exceptions are subclasses of the Throwable Java class. The **Error class** represents critical conditions that can not be caught and handled by the code of the program. On the other hand, the **Exception class** represents concerning conditions raised by the application itself; these can be caught and handled within the code to ensure that ​the application continues to run smoothly.o

**Errors**

Errors are usually raised by the environment in which the application is running. For example, an error will occur due to a lack of system resources.

Exceptions are caused by the code of the application itself.

It is not possible to recover from an error.

The use of **try-catch** blocks can handle exceptions and recover the application from them.

Errors occur at run-time and are not known by the compiler; hence, they are classified as “unchecked.”

**Exceptions**
Exceptions can be “checked” or “unchecked,” meaning they may or may not be caught by the compiler.

“OutOfMemory” and “StackOverflow” are examples of errors.

“IndexOutOfBounds” is an example of an unchecked exception, while “ClassNotFound” is an example of a checked exception.


#### Python naming of exceptions
#error #exceptions #python
However, this is a Python rule to end an exception class’s name with “Error”, and all built-in exceptions are named like that (e.g., `ValueError` or `OSError`).