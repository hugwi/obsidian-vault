---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - code-quality
  - code-review
  - metrics
source: readwise
created: 2026-06-23
rating: 
action: 
theme: comprehension-maintainability
subtheme:
  - code-navigation
  - diff-review-undo
---

# Visualize TypeScript Dependencies of Changed Files in a Pull Request Using dependency-cruiser-report-action

![rw-book-cover](https://media2.dev.to/dynamic/image/width=1000,height=500,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fraliizi28lgrwxm4h2qd.png)

## Metadata
- Author: [[Hirotaka Miyagi]]
- Full Title: Visualize TypeScript Dependencies of Changed Files in a Pull Request Using dependency-cruiser-report-action
- Category: #articles
- Summary: The article introduces dependency-cruiser-report-action, a GitHub Action that visualizes TypeScript file dependencies changed in a Pull Request. It creates a Mermaid.js graph that helps teams understand complex module relationships during code reviews. This tool improves review clarity and supports safer, long-term project maintenance.
- URL: https://dev.to/mh4gf/visualize-typescript-dependencies-of-changed-files-in-a-pull-request-using-127j

## Full Document
This article introduces [dependency-cruiser-report-action](https://github.com/MH4GF/dependency-cruiser-report-action), a custom action for GitHub Actions created by the author.

In JavaScript / TypeScript programs, you can split modules by exporting them and then import (require) those modules. However, once a function or component is exported, it can be imported from anywhere in the project. If imports are increased without a clear structure and dependency relationships become complex, modules can become tightly coupled. This can create a vicious cycle: a single small change can lead to a large-scale failure, or the lead time for releasing changes grows longer.

To maintain a product safely over the long term, you must confront these “dependencies.” Approaches include using framework conventions, adopting design principles like SOLID, or implementing architectural patterns with a few well-defined layers. On a more practical level, some teams implement ESLint plugins in their CI to enforce constraints.

* <https://zenn.dev/uhyo/articles/eslint-plugin-import-access>
* <https://github.com/knowledge-work/eslint-plugin-strict-dependencies>

Among such tools is a CLI called dependency-cruiser, which analyzes and visualizes JavaScript / TypeScript project dependencies, creating a single image representation.

* <https://github.com/sverweij/dependency-cruiser>

If you could visualize the dependencies of PR changes when you want to deepen the discussion about these “dependencies” as a team, you might achieve a more holistic and meaningful review process. [dependency-cruiser-report-action](https://github.com/MH4GF/dependency-cruiser-report-action) can make that possible.

####  Demo

[dependency-cruiser-report-action](https://github.com/MH4GF/dependency-cruiser-report-action) runs as a GitHub Actions job. It generates a text output in Mermaid.js syntax for the graph of your dependencies, then posts it as a comment on the Pull Request.

Because dependency-cruiser-report-action itself is written in TypeScript, I actually use it in its own development. Here’s an example of what it can look like:

[![](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkgp2vpru7rwx1p65ph1s.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fkgp2vpru7rwx1p65ph1s.png)
Actual Pull Request: <https://github.com/MH4GF/dependency-cruiser-report-action/pull/80>

The file names highlighted in green indicate the files changed in the Pull Request. dependency-cruiser recursively enumerates any modules those files depend on, giving reviewers visibility not just into the changes themselves but also the surrounding dependencies.

Because the output is Mermaid.js syntax in plain text, you can also paste it into tools like Notion.

 Example of the output text   
 
```
flowchart LR

subgraph 0["src"]
1["ActionError.ts"]
2["main.ts"]
3["options.ts"]
subgraph 4["options"]
5["validateOptions.ts"]
9["validateOptions.test.ts"]
d["filterSupportedFiles.ts"]
e["formatFocusOption.ts"]
end
subgraph 6["report"]
subgraph 7["body"]
8["reportBody.ts"]
a["reportBody.test.ts"]
f["uniqueTag.ts"]
end
b["generateReport.ts"]
end
c["installDependencies.ts"]
g["runDepcruise.ts"]
end
2-->1
2-->c
2-->3
2-->b
2-->g
3-->d
3-->e
3-->5
5-->1
8-->f
9-->1
9-->5
a-->8
b-->8

style 1 fill:lime,color:black
style 2 fill:lime,color:black
style 3 fill:lime,color:black
style 5 fill:lime,color:black
style 8 fill:lime,color:black
style 9 fill:lime,color:black
style a fill:lime,color:black

```
 #####  Technical Aside

 As you may notice, dependency-cruiser replaces file paths with hexadecimal strings when outputting Mermaid.js text. There are two reasons for this:

 1. Even valid file paths can contain characters that Mermaid.js interprets as special characters, which often results in syntax errors (e.g., `foo/bar--baz.js` could cause syntax errors due to `/` and `--`).
2. Mermaid.js has a default text size (byte count) limit of 50,000 characters. If your text exceeds this limit, the syntax will no longer be parsed. You can configure that limit in [Mermaid.js settings](https://github.com/mermaid-js/mermaid/blob/c269dc822c528e1afbde34e18a1cad03d972d4fe/src/defaultConfig.js#L55), but it requires permission from service providers like GitHub, Notion, and others. Most of them are set to 50,000 characters.

 Using hexadecimal strings ensures the text is not interpreted as special characters, and helps reduce the byte size while keeping each node uniquely identifiable.

 By default, dependency-cruiser uses this setting. You can disable this by setting `minify: false` in your .dependency-cruiser.js config file to produce more human-readable output:

 * <https://github.com/sverweij/dependency-cruiser/blob/develop/doc/options-reference.md#mermaid>

 
Mermaid.js is a lightweight rendering tool that runs in the browser, and multiple services including GitHub have adopted it. In contrast to well-known rendering tools like GraphViz (which outputs SVG/PNG), Mermaid.js text can be placed directly in a comment. If you want to handle images as part of CI, you’d need to upload them to S3 or Google Cloud Storage, since GitHub’s API doesn’t allow attaching files directly to comments.[1](https://dev.to/mh4gf/visualize-typescript-dependencies-of-changed-files-in-a-pull-request-using-127j/#fn1)

With Mermaid.js being broadly adopted by GitHub and other services, this approach becomes feasible.

####  How to Use

Here’s how to introduce this setup into an actual project. The [README](https://github.com/MH4GF/dependency-cruiser-report-action#readme) also explains in detail, but below are some extra notes.

####  Install dependency-cruiser Locally in Your Project

Run the following command to install dependency-cruiser in your project:

```
npm install --save-dev dependency-cruiser

# or
yarn add --dev  dependency-cruiser

```

 Why not use npx? Although dependency-cruiser can be run with npx, it may fail to correctly detect dependencies. I recommend installing it locally. This is because dependency-cruiser doesn’t come bundled with transpilers for TypeScript / Vue / CoffeeScript / LiveScript, etc., and instead uses what’s available in the local environment.  
  
 ref: <https://github.com/sverweij/dependency-cruiser/blob/develop/doc/faq.md#q-typescript-coffeescript-livescript-or-vue-single-file-component-sfc-dependencies-dont-show-up-how-can-i-fix-that>

 
####  Create a Configuration File for dependency-cruiser Interactively

Run the following command to generate a configuration file in an interactive manner. If your project uses tsconfig.json or .babelrc, you can specify those files here:

```
npm run depcruise --init

```

For more information on the various options, check out the official documentation:

<https://github.com/sverweij/dependency-cruiser/blob/develop/doc/options-reference.md>

Below is an example configuration from the author’s Next.js project (for reference):

<https://github.com/MH4GF/mysite/blob/main/.dependency-cruiser.js>

####  Add a Workflow File Under .github/workflows

Add a workflow file like the one below:

```
name: 'depcruise'
on:
  pull_request:

jobs:
  report:
    permissions:
      pull-requests: write
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: MH4GF/dependency-cruiser-report-action@v2

```

That’s it! Once a new commit is added to a Pull Request, a comment with the diagram will be posted.

####  Conclusion

In this article, I introduced [dependency-cruiser-report-action](https://github.com/MH4GF/dependency-cruiser-report-action), which visualizes the dependencies of modified files per Pull Request and adds them as a comment.

Because it visualizes dependencies for the changed files only, it can be used on any JS/TS project, regardless of size. Of course, running dependency-cruiser locally to see the entire project’s dependencies is also worthwhile. Feel free to give it a try, and consider leaving a star on the repository if you find it helpful!

1. As an example, reg-suit or lighthouse-ci take that approach. You can also use GitHub Artifacts, but since they can’t be hosted for public access, you’d need to navigate to the Actions summary and download them. This can be somewhat inconvenient for continuously viewing images during development. [↩](https://dev.to/mh4gf/visualize-typescript-dependencies-of-changed-files-in-a-pull-request-using-127j/#fnref1)
