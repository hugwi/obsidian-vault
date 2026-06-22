# GitHub - keploy/keploy: Shadow Test generation for Developers. Generate tests and stubs for your application that actually work!

![rw-book-cover](https://repository-images.githubusercontent.com/449649393/3df356de-a8d9-43a5-925b-a75a795af9e3)

## Metadata
- Author: [[https://github.com/keploy/]]
- Full Title: GitHub - keploy/keploy: Shadow Test generation for Developers. Generate tests and stubs for your application that actually work!
- Category: #articles
- Summary: Keploy is an API testing tool that quickly generates tests and mocks from your application's API and database calls. It features a unit test generator that automates the creation of comprehensive tests to improve coverage and handle complex scenarios. Keploy is easy to install and integrates seamlessly with various testing libraries and CI/CD pipelines.
- URL: https://github.com/keploy/keploy

## Full Document
### keploy/keploy

[![keploy logo](https://camo.githubusercontent.com/74cbc79070c04e7077cfd86981c110678fe434e9269ea8f52eafb37b781cfb4a/68747470733a2f2f646f63732e6b65706c6f792e696f2f696d672f6b65706c6f792d6c6f676f2d6461726b2e7376673f733d32303026763d34)](https://camo.githubusercontent.com/74cbc79070c04e7077cfd86981c110678fe434e9269ea8f52eafb37b781cfb4a/68747470733a2f2f646f63732e6b65706c6f792e696f2f696d672f6b65706c6f792d6c6f676f2d6461726b2e7376673f733d32303026763d34)
#####   **⚡️ API tests faster than unit tests, from user traffic ⚡️**

🌟 The must-have tool for developers in the AI-Gen era 🌟

######   [Keploy Twitter](https://twitter.com/Keploy_io)   [Help us reach 4k stars!](https://github.com/Keploy/Keploy/issues)   [Keploy CNCF Landscape](https://landscape.cncf.io/?item=app-definition-and-development--continuous-integration-delivery--keploy)  [Slack](https://join.slack.com/t/keploy/shared_invite/zt-2dno1yetd-Ec3el~tTwHYIHgGI0jPe7A) [LinkedIn](https://www.linkedin.com/company/keploy/) [YouTube](https://www.youtube.com/channel/UC6OTg7F4o0WkmNtSoob34lg) [Twitter](https://twitter.com/Keployio)

[Keploy](https://keploy.io) is **developer-centric** API testing tool that creates **tests along with built-in-mocks**, faster than unit tests.

Keploy not only records API calls, but also records database calls and replays them during testing, making it **easy to use, powerful, and extensible**.

[![Convert API calls to test cases](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-tc.gif)](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-tc.gif)
  [![Convert API calls to test cases](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-tc.gif)](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-tc.gif)  

>  🐰 **Fun fact:** Keploy uses itself for testing! Check out our swanky coverage badge: [![Coverage Status](https://camo.githubusercontent.com/6a82bd4a7d1ee3b14a230e00f821a048859360f33a8c7159151713faae149149/68747470733a2f2f636f766572616c6c732e696f2f7265706f732f6769746875622f6b65706c6f792f6b65706c6f792f62616467652e7376673f6272616e63683d6d61696e266b696c6c5f63616368653d31)](https://coveralls.io/github/keploy/keploy?branch=main&kill_cache=1) 
> 
>  

#### 🚨 Here for [Unit Test Generator](https://github.com/keploy/keploy/blob/main/README-UnitGen.md) (ut-gen)?

Keploy's new launched world's first unit test generator(ut-gen) implementation of [Meta LLM research paper](https://arxiv.org/pdf/2402.09171), it understands code semantics and generates meaningful unit tests, aiming to:

* **Automate unit test generation (UTG)**: Quickly generate comprehensive unit tests and reduce the redundant manual effort.
* **Improve edge cases**: Extend and improve the scope of tests to cover more complex scenarios that are often missed manually.
* **Boost test coverage**: As codebase grows, ensuring exhaustive coverage should become feasible.

##### 📜 Follow [Unit Test Generator README](https://github.com/keploy/keploy/blob/main/README-UnitGen.md)! ✅

#### 📘 Documentation!

Become a Keploy pro with **[Keploy Documentation](https://keploy.io/docs/)**.

[![Record Replay Testing](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-replay.gif)](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-replay.gif)
  [![Record Replay Testing](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-replay.gif)](https://raw.githubusercontent.com/keploy/docs/main/static/gif/record-replay.gif)  

### 🚀 Quick Installation (API test generator)

Integrate Keploy by installing the agent locally. No code-changes required.

```
curl --silent -O -L https://keploy.io/install.sh && source install.sh
```

#### 🎬 Recording Testcases

Start your app wit Keploy to convert API calls as Tests and Mocks/Stubs.

```
keploy record -c "CMD_TO_RUN_APP" 
```

For example, if you're using a simple Python app the `CMD_TO_RUN_APP` would resemble to `python main.py`, for Golang `go run main.go`, for java `java -jar xyz.jar`, for node `npm start`..

```
keploy record -c "python main.py"
```

#### 🧪 Running Tests

Shut down the databases, redis, kafka or any other services your application uses. Keploy doesn't need those during test.

```
keploy test -c "CMD_TO_RUN_APP" --delay 10
```

#### ✅ Test Coverage Integration

To integrate with your unit-testing library and see combine test coverage, follow this [test-coverage guide](https://keploy.io/docs/server/sdk-installation/go/).

>  ###### **If You Had Fun:** Please leave a 🌟 star on this repo! It's free, and you'll bring a smile. 😄 👏
> 
>  

#### One-Click Setup 🚀

Setup and run keploy quickly without any installation on your local machine:

[![GitHub Codescape](https://camo.githubusercontent.com/8a3dab7131fbf8910f10dedaa3715bb633e74654365963fe19421d53dc8321eb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4748253230636f646573706163652d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d666666)](https://camo.githubusercontent.com/8a3dab7131fbf8910f10dedaa3715bb633e74654365963fe19421d53dc8321eb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4748253230636f646573706163652d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d676974687562266c6f676f436f6c6f723d666666)
#### 🤔 Questions?

Reach out to us. We're here to help!

[![Slack](https://camo.githubusercontent.com/d86a78c227aed2775574dc12b4c15620d7a92bdee289bf2ede968f37428a83f6/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f536c61636b2d3441313534423f7374796c653d666f722d7468652d6261646765266c6f676f3d736c61636b266c6f676f436f6c6f723d7768697465)](https://join.slack.com/t/keploy/shared_invite/zt-2dno1yetd-Ec3el~tTwHYIHgGI0jPe7A)
[![LinkedIn](https://camo.githubusercontent.com/0c59c81be6c6e981fbad69ea742692368b3fdc1018090a34cb7764dfea5a1a91/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6c696e6b6564696e2d2532333030373742352e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6c696e6b6564696e266c6f676f436f6c6f723d7768697465)](https://www.linkedin.com/company/keploy/)
[![YouTube](https://camo.githubusercontent.com/a67feba4f5643de3002051e6c0957687aa81bab72741956e80905f3589795ddb/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f596f75547562652d2532334646303030302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d596f7554756265266c6f676f436f6c6f723d7768697465)](https://www.youtube.com/channel/UC6OTg7F4o0WkmNtSoob34lg)
[![Twitter](https://camo.githubusercontent.com/368b10740f29d9d23f748b908dc48c3634a20309bd4b47699823bf4cd16e4781/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f547769747465722d2532333144413146322e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d54776974746572266c6f676f436f6c6f723d7768697465)](https://twitter.com/Keployio)
#### 🌐 Language Support

From Go's gopher 🐹 to Python's snake 🐍, we support:

[![Go](https://camo.githubusercontent.com/29f331ff0b9cd5621d1233c541c575511c7ebb7cd6c09cb18c175c8bc729d14b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f676f2d2532333030414444382e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d676f266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/29f331ff0b9cd5621d1233c541c575511c7ebb7cd6c09cb18c175c8bc729d14b/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f676f2d2532333030414444382e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d676f266c6f676f436f6c6f723d7768697465)
[![Java](https://camo.githubusercontent.com/6d9ad4becc2d73ac5cefacc1370a6c37458f272a553046ea5e2b8351ea185747/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a6176612d2532334544384230302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6a617661266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/6d9ad4becc2d73ac5cefacc1370a6c37458f272a553046ea5e2b8351ea185747/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6a6176612d2532334544384230302e7376673f7374796c653d666f722d7468652d6261646765266c6f676f3d6a617661266c6f676f436f6c6f723d7768697465)
[![NodeJS](https://camo.githubusercontent.com/8477a50d7210f0f3bf15fbe5b44809296b75f2101a2927818599d72c8ea72cef/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f64652e6a732d3644413535463f7374796c653d666f722d7468652d6261646765266c6f676f3d6e6f64652e6a73266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/8477a50d7210f0f3bf15fbe5b44809296b75f2101a2927818599d72c8ea72cef/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f64652e6a732d3644413535463f7374796c653d666f722d7468652d6261646765266c6f676f3d6e6f64652e6a73266c6f676f436f6c6f723d7768697465)
[![Rust](https://camo.githubusercontent.com/9781ee998334222675c31cdb8763bcc8d0fb875b1296222b071502c8b0a346af/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f527573742d6461726b7265643f7374796c653d666f722d7468652d6261646765266c6f676f3d72757374266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/9781ee998334222675c31cdb8763bcc8d0fb875b1296222b071502c8b0a346af/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f527573742d6461726b7265643f7374796c653d666f722d7468652d6261646765266c6f676f3d72757374266c6f676f436f6c6f723d7768697465)
[![C#](https://camo.githubusercontent.com/4ac6e871efa2edfcb7bbbe416f87ec2ba4773d1a225d17c40aafbf1428ce9b33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6373686172702d707572706c653f7374796c653d666f722d7468652d6261646765266c6f676f3d637368617270266c6f676f436f6c6f723d7768697465)](https://camo.githubusercontent.com/4ac6e871efa2edfcb7bbbe416f87ec2ba4773d1a225d17c40aafbf1428ce9b33/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6373686172702d707572706c653f7374796c653d666f722d7468652d6261646765266c6f676f3d637368617270266c6f676f436f6c6f723d7768697465)
[![Python](https://camo.githubusercontent.com/0d0779a129f1dcf6c31613b701fe0646fd4e4d2ed2a7cbd61b27fd5514baa938/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)](https://camo.githubusercontent.com/0d0779a129f1dcf6c31613b701fe0646fd4e4d2ed2a7cbd61b27fd5514baa938/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f707974686f6e2d3336373041303f7374796c653d666f722d7468652d6261646765266c6f676f3d707974686f6e266c6f676f436f6c6f723d666664643534)
#### 🫰 Keploy Adopters 🧡

So you and your organisation are using Keploy? That’s great. Please add yourselves to [**this list,**](https://github.com/orgs/keploy/discussions/1765) and we'll send you goodies! 💖

We are happy and proud to have you all as part of our community! 💖

#### 🎩 How's the Magic Happen?

Keploy proxy captures and replays **ALL** (CRUD operations, including non-idempotent APIs) of your app's network interactions.

Take a journey to **[How Keploy Works?](https://keploy.io/docs/keploy-explained/how-keploy-works/)** to discover the tricks behind the curtain!

Here are Keploy's core features: 🛠

* ♻️ **Combined Test Coverage:** Merge your Keploy Tests with your fave testing libraries(JUnit, go-test, py-test, jest) to see a combined test coverage.
* 🤖 **EBPF Instrumentation:** Keploy uses EBPF like a secret sauce to make integration code-less, language-agnostic, and oh-so-lightweight.
* 🌐 **CI/CD Integration:** Run tests with mocks anywhere you like—locally on the CLI, in your CI pipeline (Jenkins, Github Actions..) , or even across a Kubernetes cluster.
* 📽️ **Record-Replay Complex Flows:** Keploy can record and replay complex, distributed API flows as mocks and stubs. It's like having a time machine for your tests—saving you tons of time!
* 🎭 **Multi-Purpose Mocks:** You can also use keploy Mocks, as server Tests!

#### 👨🏻‍💻 Let's Build Together! 👩🏻‍💻

Whether you're a newbie coder or a wizard 🧙‍♀️, your perspective is golden. Take a peek at our:

📜 [Contribution Guidelines](https://github.com/keploy/keploy/blob/main/CONTRIBUTING.md)

❤️ [Code of Conduct](https://github.com/keploy/keploy/blob/main/CODE_OF_CONDUCT.md)

#### 🐲 Current Limitations!

* **Unit Testing:** While Keploy is designed to run alongside unit testing frameworks (Go test, JUnit..) and can add to the overall code coverage, it still generates integration tests.
* **Production Lands**: Keploy is currently focused on generating tests for developers. These tests can be captured from any environment, but we have not tested it on high volume production environments. This would need robust deduplication to avoid too many redundant tests being captured. We do have ideas on building a robust deduplication system [#27](https://github.com/keploy/keploy/issues/27)

#### ✨ Resources!

🤔 [FAQs](https://keploy.io/docs/keploy-explained/faq/)

🕵️‍️ [Why Keploy](https://keploy.io/docs/keploy-explained/why-keploy/)

⚙️ [Installation Guide](https://keploy.io/docs/application-development/)

📖 [Contribution Guide](https://keploy.io/docs/keploy-explained/contribution-guide/)
