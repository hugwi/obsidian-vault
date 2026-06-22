
https://stackoverflow.com/questions/2588265/when-to-use-custom-exceptions-vs-existing-exceptions-vs-generic-exceptions

Don't try to repurpose exceptions that are specific to some other module. Use those exceptions that have a clear, generic purpose, and don't use them for business rules. For example, `InvalidOperationException` should indicate a bad operation w/ regards to your API, not a violation of a business rule.

For exceptions specific to your library, create a base exception class, `BadgeAuthException`, and always throw that. The specific scenarios should each get their own subclass (`BadgeDeactivatedException`, `NoPermissionsAtWorkstationException`, etc.)


https://towardsdatascience.com/should-we-use-custom-exceptions-in-python-b4b4bca474ac

