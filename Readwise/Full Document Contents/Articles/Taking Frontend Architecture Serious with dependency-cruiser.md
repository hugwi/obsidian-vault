# Taking Frontend Architecture Serious with dependency-cruiser

![rw-book-cover](https://xebia.com/media/2025/04/marc-olivier-jodoin-HIiNFXcbtQ-unsplash-scaled-1024x682.jpg)

## Metadata
- Author: [[Xebia]]
- Full Title: Taking Frontend Architecture Serious with dependency-cruiser
- Category: #articles
- Summary: Dependency-cruiser helps enforce and visualize frontend architecture by controlling imports and detecting unused or misplaced code. It improves code quality by ensuring proper module organization and preventing architectural drift. Using it alongside tools like eslint enhances development and keeps the codebase clean and maintainable.
- URL: https://xebia.com/blog/taking-frontend-architecture-serious-with-dependency-cruiser/

## Full Document
![Ruben Oostinga](https://kcdn.xebia.com/cdn-cgi/image/scq=50,format=auto,quality=75,onerror=redirect,width=3840/https://xebia.com/media/2025/03/avatar_user_317_1697205066-96x96-1.jpg)Ruben Oostinga

![](https://kcdn.xebia.com/cdn-cgi/image/scq=50,format=auto,quality=75,onerror=redirect,width=3840/https://xebia.com/media/2025/04/marc-olivier-jodoin-HIiNFXcbtQ-unsplash-scaled.jpg)
With [dependency-cruiser](https://github.com/sverweij/dependency-cruiser), you can enforce which imports are allowed. This enables you to create an architecture fitness function that ensures your code continues to adhere to the initial design. You can also visualize your dependencies to gain a clearer understanding of your code's actual structure, allowing you to compare it with your mental model and make improvements where necessary.

An application architecture design defines a folder structure and specifies which files can import from other files. On the backend, you have design patterns like layered architecture, hexagonal (or ports and adapters) architecture. On the frontend, there's the classical Model-View-Controller architecture. Modern component-based frameworks also offer their own approaches like having page, feature, or technical folders. Often there is also a shared or common folder.

Applying any architecture pattern or folder structure has an impact on how code should be imported by the rest of the codebase. Verifying the correctness of imports manually can be challenging and is often overlooked during code reviews. An automated check can benefit not only the current team but also future developers. Even when you design the [application architecture](https://xebia.com/articles/application-architectures-that-enable-your-agile-organization/) and implement the code, it's easy to unintentionally deviate from your own guidelines. One auto-import from an editor can compromise your design. Collaborating with others amplifies this challenge.

#### Keep Page-Specific Folders Isolated

You don't want modules from one page-specific folder importing modules from another page-specific folder. If there's a cross-page dependency, it likely means that some modules are actually shared modules placed in a page-specific folder by accident. The solution is to move the module to a shared or common folder.

In our codebase, we faced this issue because we built one page and later constructed a similar page, realizing we could reuse some components. We forgot to move the components to the shared folder, and this oversight wasn't caught during code review. With dependency-cruiser, the issue was easily discovered and will be avoided in the future. See [Isolating peer folders from each other](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-tutorial.md#isolating-peer-folders-from-each-other)

#### Finding Orphaned Code

If unused code is not removed as soon as it's no longer needed, detecting it later can be difficult. Especially for components that are imported by unit tests or Storybook stories, they may seem to be in use but are not actually included anywhere in the real application.

Dependency-cruiser can identify whether code is used by actual production code or not. Of course, exceptions can be made for configuration files that aren't supposed to be part of the application in the first place.

We found an unused component, complete with tests and Storybook stories. By removing it, we no longer need to maintain the code, and it eliminates confusion about why the code was there in the first place.

See [Is a module actually used?](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-tutorial.md#is-a-module-actually-used)

#### Shared Code

It's helpful to distinguish code that is genuinely shared between different parts from code that could be shared but isn't currently. Often, the way code is written makes assumptions about its usage.

By counting how many files depend on a module, you can determine whether a module should be considered shared. You can use this information to enforce that shared modules are placed in a `common/` or `shared/` folder. Conversely, you can ensure that all code in the shared folders is actually shared. When you remove an import to a shared module, you'll receive an error, allowing you to move the module to a page-specific folder.

Here, we also found code that could be, or had been, shared but, in reality, was specific to a single page. So, we moved this code from the shared folder to the page folder. This shift made the page code more cohesive and decreased its coupling to the shared code—both important architectural qualities.

See [Is a utility module shared?](https://github.com/sverweij/dependency-cruiser/blob/main/doc/rules-tutorial.md#is-a-utility-module-shared)

#### Visualization

Dependency-cruiser has [advanced visualization capabilities](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples.md) built-in.

When you visualize the dependencies between different folders, you can see:

* Dependencies that shouldn’t be there
* Whether a dependency is a dynamic import (for lazy loading) or not
* Circular dependencies
* Which folders have shared code
* If 3rd party code is kept separate or spread everywhere

This is also handy as documentation so everyone has the same understanding.

For the best visualization, you need to tweak the [configuration](https://github.com/sverweij/dependency-cruiser/blob/main/doc/options-reference.md#reporteroptions) to get the right amount of detail.

In the [visualization](https://xebia.com/articles/accelerate-your-transformation-with-visualization/) below, we want to show that pages don’t depend on other pages but only on the shared and service layers. The service layer itself doesn’t rely on any view-specific folders. What isn’t shown, but is enforced by dependency-cruiser, is that the services folder doesn’t have any React-specific dependencies.

![Real World React codebase visualized with dependency-cruiser](https://xebia.com/media/2025/02/architecture.png)Real World React codebase visualized with dependency-cruiser
#### Comparison to eslint-plugin-imports

When comparing dependency-cruiser to eslint-plugin-import, a noticeable overlap between the two becomes evident. Both tools can identify circular dependencies, impose limits on certain imports, and assist in keeping test code separate from production code. However, dependency-cruiser offers additional features. It can identify orphaned files even if they are imported by tests. It facilitates the separation of sibling folders to maintain organized code. Additionally, dependency-cruiser displays the usage frequency of a component, enabling teams to discern shared parts of the codebase.

A distinct advantage of eslint is its superior editor integration. Unlike dependency-cruiser, eslint displays red lines beneath invalid imports, providing immediate feedback. If in-editor feedback is valuable, eslint, with its rule `no-restricted-imports`, serves well in ensuring proper encapsulation of third parties. While dependency-cruiser can perform similarly, it usually provides feedback after a failed CI build, whereas eslint aids developers instantly.

The visualization provided by dependency-cruiser is undeniably a unique feature absent in a typical linter.

I advise utilizing a combination of both tools to attain a developer experience that aligns with your team’s needs.

#### Real World Experience

Our nearly three-month experience with dependency-cruiser was overwhelmingly positive. Upon activating the rules, we uncovered numerous incorrect imports and misplaced files, even in our high-quality, relatively new React codebase. These revelations prompted enhancements in architectural qualities like separation of concerns, encapsulation, and modularity. The fixes primarily involved relocating files and shifting code between modules. Not enforcing all rules from the outset allowed for incremental improvements, especially beneficial for larger codebases.

Once we began enforcing the rules, dependency errors were scarce, thanks to our consistent code structure and established patterns. Encountered errors were accurate, with straightforward solutions, reinforcing that our design remains intact, averting the risk of incremental degradation, or, more starkly, death by a thousand cuts.

The visualization is invaluable, reflecting current realities over idealized mental models. It aids in onboarding new members and, more importantly, allows existing team members to discover architectural improvements.

#### Conclusion

Vigilance in software architecture is crucial throughout the development cycle to counter incremental degradation; this is applicable to both frontend and backend codebases. Dependency-cruiser simplifies the design review process and ensures design enforcement during development.

Unfortunately, the production codebase where I applied dependency-cruiser is not public. However, I did conduct some experiments during a Xebia Innovation Day. [That code](https://github.com/0xR/fitness-functions-experiments) can be found on GitHub.

![Secure by Default, Slow by Surprise. What AWS Forgot to Mention About RDS IAM...](https://kcdn.xebia.com/cdn-cgi/image/scq=50,format=auto,quality=75,onerror=redirect,width=640/https://xebia.com/media/2026/04/banner-1.jpg)[Secure by Default, Slow by Surprise. What AWS Forgot to Mention About RDS IAM...](https://xebia.com/blog/rds-iam-auth-aurora-serverless-latency/)
![Growing by Saying Yes](https://kcdn.xebia.com/cdn-cgi/image/scq=50,format=auto,quality=75,onerror=redirect,width=640/https://xebia.com/media/2026/02/Hero-image_Victor-de-Baare.jpg)[Growing by Saying Yes](https://xebia.com/blog/growing-by-saying-yes/)
![GitHub Copilot – Coding Agent Examples Walkthrough](https://kcdn.xebia.com/cdn-cgi/image/scq=50,format=auto,quality=75,onerror=redirect,width=640/https://xebia.com/media/2026/02/Blog_GitHub-Copilot-_Hero_Desktop_1440459_L3_L4-scaled.jpg)[GitHub Copilot &#8211; Coding Agent Examples Walkthrough](https://xebia.com/blog/github-copilot-coding-agent-examples-walkthrough/)
