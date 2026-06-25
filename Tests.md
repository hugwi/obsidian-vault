---
categories:
  - "[[Resources]]"
domain: engineering
created: 2026-06-23
---
https://medium.com/@stefanovskyi/unit-test-naming-conventions-dd9208eadbea

https://osherove.com/blog/2005/4/3/naming-standards-for-unit-tests.html

 **[UnitOfWork_StateUnderTest_ExpectedBehavior]**

https://enterprisecraftsmanship.com/posts/structural-inspection/
Overall, try to constantly ask yourself a question: **does this test verify some business requirement?** If the answer is no, remove it. The most valuable tests are always the tests that have at least some connection to the business requirements your code base is ought to address. Not surprisingly, such tests also fall into the formal definition I brought in the beginning of this article: they are likely to give a protection against regression errors and they are unlikely to turn red without a good reason.

This is an important point, so let me re-iterate on it. The way your domain objects communicate with each other is an implementation detail whereas the way your application collaborates with other applications is part of its public API. The latter is the contract, the post-conditions your system must guarantee to fulfill. And it’s your responsibility to make sure they are held. [1](https://enterprisecraftsmanship.com/posts/pragmatic-integration-testing/)

## Mocks vs stubs/spies from the value proposition point of view

Now I’d like to expand on the remark that while collaboration verification is perfectly reasonable to ensure integrity with external systems, you don’t necessarily have to use mocks for that. But before that, let me give you a refresher on the differences between mocks, stubs, and spies.

A mock is a test double which allows you to verify that some method was invoked during the test. It also lets you make sure this method is called using some particular parameters. A stub, on the other hand, is a test double that just returns some canned answer when you ask it. A spy is a test double that allows you to record calls to some methods and examine them later on manually (although, some authors also use the term "stub" for this kind of activity).

The term "mock" is also used to denote an instrument, a special tool that enables you to create test doubles:

```csharp
var mock = new Mock<IEmailGateway>();
```

Mock as a test double does not equate to Mock as a tool. You can use a mock-the-tool to introduce either a mock-the-test-double or a stub. Here’s an example:

```csharp
[Fact]
public void Test_with_a_mock()
{
    var mock = new Mock<IEmailGateway>();
    var sut = new Controller();
 
    sut.GreetUsers(mock.Object);
 
    mock.Verify(x => x.SendGreetingsEmail("user@email.com"));
}
 
[Fact]
public void Test_with_a_stub()
{
    var stub = new Mock<IDatabase>();
    stub.Setup(x => x.GetNumberOfUsers()).Returns(10);
    var sut = new Controller();
 
    Report report = sut.CreateReport(stub.Object);
 
    Assert.Equal(report.NumberOfUsers, 10);
}
```

The first test creates a mock-the-tool and uses it to make sure the SUT invoked the correct method on the `IEmailGateway` interface. The second test also creates a mock-the-tool but instead of checking what members of it were invoked, it uses the tool to set up a canned answer for the `GetNumberOfUsers` method.

This is essentially what differs a mock from a stub: mocks are used for verifying side effects whereas stubs - for providing the SUT with test data. Another way of thinking about these differences is using the terminology from the [CQS principle](https://en.wikipedia.org/wiki/Command–query_separation): mocks are for commands; stubs are for queries.

https://enterprisecraftsmanship.com/posts/pragmatic-integration-testing/

Notes: 
Still having problem u derstanding what a spy is?? 



Overall, the use of unit tests with mocks has the worst value proposition because of the bad signal/noise ratio. They do help catch regressions but they do that at the expense of producing lots of false positives. It defeats the whole purpose of unit testing: having a solid test suite which you can trust and rely upon.

The use of mocks is just a sign of a problem, of course, not the problem itself. However, it’s a very strong sign as it almost always signalizes an issue with your approach to unit testing. If you use mocks, you most likely couple your unit tests to the SUT’s implementation details.

https://enterprisecraftsmanship.com/posts/styles-of-unit-testing/


## Side effect vs return value
#mock
#test
https://pytest-with-eric.com/pytest-advanced/pytest-mock-multiple-return-values/

## Setup and teardown 

Good article about setup and tear down with pytest
https://medium.com/@ramanish1992/pytest-setup-tear-down-configuration-c8197558a8e2
