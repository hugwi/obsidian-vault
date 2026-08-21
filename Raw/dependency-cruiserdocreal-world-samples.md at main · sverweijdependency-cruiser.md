---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering]
tags:
  - human-factors
source: readwise
created: 2026-06-23
rating: 
action: 
theme: comprehension-maintainability
subtheme:
  - code-navigation
---

# dependency-cruiser/doc/real-world-samples.md at main · sverweij/dependency-cruiser

![rw-book-cover](https://repository-images.githubusercontent.com/74299372/239ed080-370b-11ea-8fe7-140cf7b90a33)

## Metadata
- Author: [[https://github.com/sverweij/]]
- Full Title: dependency-cruiser/doc/real-world-samples.md at main · sverweij/dependency-cruiser
- Category: #articles
- Summary: Dependency Cruiser analyzes and visualizes dependencies in real-world projects like React, Yarn, and TypeScript without extra build steps. It supports various languages including JavaScript, TypeScript, and CoffeeScript, helping find issues like circular dependencies. Users can generate detailed, high-level, or folder-level graphs to understand and manage complex codebases efficiently.
- URL: https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples.md

## Full Document
[Open in github.dev](https://github.dev/) [Open in a new github.dev tab](https://github.dev/) [Open in codespace](https://github.com/codespaces/new/sverweij/dependency-cruiser/tree/main?resume=1) 

More file actions

More file actions

Top

### Real world projects. Dependency cruised.

#### Some popular projects on npm

##### Commander

[tj/commander.js](https://github.com/tj/commander.js) - For command line parsing - and cooking command line interfaces.

[![commander](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/commander.svg)](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/commander.svg)
##### Chalk

[chalk/chalk](https://github.com/chalk/chalk) - For colouring strings in the terminal. A typical *Sorhus style* micro module that uses other micro modules to accomplish its goals.

[![chalk](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/chalk.png)](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/chalk.png)
##### Yarn 2 ('berry')

[yarnpkg/berry](https://github.com/yarnpkg/berry) - package manager.

When your app becomes big, dependency graphs on module level will become impractical. Dependency-cruiser can consolidate modules (+ their dependencies) and colour them. Consolidation works out of the box for many repositories, but can be [configured](https://github.com/sverweij/dependency-cruiser/blob/main/doc/options-reference.md#summarising-collapsepattern-dot-and-archi-reporters) to your [own liking](https://github.com/sverweij/dependency-cruiser/blob/main/doc/options-reference.md#reporteroptions).

Here's the resulting get high level dependency graph for berry:

[![berry](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/berry-high-level-dependencies.svg)](https://sverweij.github.io/dependency-cruiser/assets/berry-high-level-dependencies.html)
 howto To get the above graph we used [berry-dependency-cruiser-config.js](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/berry-dependency-cruiser-config.js). To generate it yourself do this in the root of the berry repo:

 * `yarn` (with yarn v2 :-))
* `yarn add -D dependency-cruiser`
* `rm -f berry-dependency-cruiser-config.js`
* `wget https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/doc/real-world-samples/berry-dependency-cruiser-config.js`
* add these two lines to the `scripts` section of the package.json (so don't use the globally installed depcruise or even the locally installed one - yarn's pnp resolution won't work otherwise:) 
```
"dc": "depcruise --version && depcruise --config berry-dependency-cruiser-config.js --output-type err packages",
"depcruise:archi": "depcruise --version && depcruise --config berry-dependency-cruiser-config.js --output-type archi packages | dot -T svg | tee berry-high-level-dependencies.svg | depcruise-wrap-stream-in-html > berry-high-level-dependencies.html",

```
* run `yarn depcruise:archi`

 
##### react

[facebook/react](https://github.com/facebook/react) - "a JavaScript library for building user interfaces".

Also high level:

[![react](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/react-high-level-dependencies.svg)](https://sverweij.github.io/dependency-cruiser/assets/react-high-level-dependencies.html)
 howto To get the above graph we used [react-dependency-cruiser-config.js](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/react-dependency-cruiser-config.js). To generate it yourself do this in the root of the react repo:

 * prepare

 
```
git clone git@github.com:facebook/react.git
cd react
yarn
yarn add -D -W dependency-cruiser
rm -f react-dependency-cruiser-config.js
wget https://raw.githubusercontent.com/sverweij/dependency-cruiser/main/doc/real-world-samples/react-dependency-cruiser-config.js
```
 * Add these run-scripts to the package.json:

 
```
  "dc": "depcruise --version && depcruise --ignore-known --config react-dependency-cruiser-config.js -T err packages/*/{*.js,src}",
  "depcruise:baseline": "depcruise --version && depcruise-baseline packages/*/{*.js,src} --config react-dependency-cruiser-config.js",
  "depcruise:archi": "depcruise --ignore-known --config react-dependency-cruiser-config.js -T archi packages/*/{*.js,src} | dot -T svg | tee react-high-level-dependencies.svg | depcruise-wrap-stream-in-html > react-high-level-dependencies.html

```
* `yarn depcruise:baseline`
* `yarn depcruise:archi`

 
##### Safe-regex

[substack/safe-regex](https://github.com/substack/safe-regex) - for sanity checking regular expressions against exponential time errors. For everyone who enables users to input regular expressions in.

[![safe-regex](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/safe-regex.png)](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/safe-regex.png)
##### Resolve

[substack/node-resolve](https://github.com/substack/node-resolve) - resolves (node) module names to files on disk.

[![resolve](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/resolve.png)](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/resolve.png)
##### Yargs

[yargs/yargs](https://github.com/yargs/yargs) - Another library to parse command line options/ cook command line interfaces.

[![yargs](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/yargs.png)](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/yargs.png)
#### TypeScript

It is possible to use dependency-cruiser to infer dependencies of typescript projects.

We got the picture of tslint by running this in its source folder:

```
dependency-cruise -T dot -x node_modules -v -- src/index.ts  | dot -T png > tslint-without-node_modules.png
```

(Yep, that's all - no separate transpilation steps necessary ...)

##### tslint

[palantir/tslint](https://github.com/palantir/tslint) - linter for typescript.

The orange lines are warnings for circular dependencies, which occur around two of tslint's 'barrel' `index.ts` modules:

[![tslint](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/tslint-without-node_modules.png)](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/tslint-without-node_modules.png)
#### CoffeeScript

In the same vein dependency-cruiser directly supports CoffeeScript.

In the `src` folder of the CoffeeScript repo run this:

```
depcruise -x node_modules -T dot . | dot -T png > coffee-script-coffee-without-node_modules.png
```

##### CoffeeScript

[jashkenas/coffeescript](https://github.com/jashkenas/coffeescript) - the CoffeeScript transpiler:

[![coffee-script](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/coffee-script-coffee-without-node_modules.png)](https://github.com/sverweij/dependency-cruiser/blob/main/doc/real-world-samples/coffee-script-coffee-without-node_modules.png)
(You see one module flagged as *unresolvable* - this is the parser code that the CoffeeScript build script generates jison into the folder with transpiled JavaScript.)

#### My own projects

##### dependency cruiser

Dependency cruiser used on itself, focusing on internal dependencies only, on three levels of abstraction - high level, folder and modules. A small [custom theme](https://github.com/sverweij/dependency-cruiser/blob/main/doc/options-reference.md#theme-dot-ddot-and-archi-reporters) in its [configuration](https://github.com/sverweij/dependency-cruiser/blob/main/.dependency-cruiser.json#L243) colours the various main parts (extract, validate, report) and the dependencies to them. Click for slightly more interactive versions.

###### high level overview ('archi')

[![dependency cruiser's dependency graph aggregated to its main parts](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/dependency-cruiser-archi-graph.svg)](https://sverweij.github.io/dependency-cruiser/dependency-cruiser-archi-graph.html)
 howto To generate this yourself do this in the root of the dependency-cruiser repo:

 
```
node ./bin/dependency-cruise.mjs bin src --config --output-type archi | \
  # format the output with dot. For this specific graph top-down (TD)
  # orientation works best
  dot -T svg -Grankdir=TD | \
  # save the svg
  tee doc/real-world-samples/dependency-cruiser-archi-graph.svg | \
  # process the svg into an interactive html graph
  node bin/wrap-stream-in-html.mjs > docs/dependency-cruiser-archi-graph.html

```
 
>  the only repository in the world you can't use the commands `depcruise`, `depcruise-fmt` or `depcruise-wrap-stream-in-html` is dependency-cruiser's own - instead we run the JavaScript files from `bin` directly. If you adapt the script for your own use replace `node ./bin/dependency-cruise.mjs` with `depcruise`, `node ./bin/wrap-stream-in-html.mjs` with `depcruise-wrap-stream-in-html`.
> 
>  

 
###### folder level overview ('ddot')

[![dependency cruiser's dependency graph aggregated to folders](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/dependency-cruiser-dir-graph.svg)](https://sverweij.github.io/dependency-cruiser/dependency-cruiser-dir-graph.html)
 howto To generate this yourself do this in the root of the dependency-cruiser repo:

 
```
node ./bin/dependency-cruise.js bin src --config --output-type ddot | \
  # format the output with dot. For this specific graph top-down (TD)
  # orientation works best
  dot -T svg -Grankdir=TD | \
  # save the svg
  tee doc/real-world-samples/dependency-cruiser-dir-graph.svg | \
  # process the svg into an interactive html graph
  node bin/wrap-stream-in-html.js > docs/dependency-cruiser-dir-graph.html

```
 
>  the only repository in the world you can't use the commands `depcruise`, `depcruise-fmt` or `depcruise-wrap-stream-in-html` is dependency-cruiser's own - instead we run the JavaScript files from `bin` directly. If you adapt the script for your own use replace `node ./bin/dependency-cruise.js` with `depcruise`, `node ./bin/wrap-stream-in-html.js` with `depcruise-wrap-stream-in-html`.
> 
>  

 
###### detailed overview ('dot')

[![dependency cruiser's dependency graph](https://github.com/sverweij/dependency-cruiser/raw/main/doc/real-world-samples/dependency-cruiser-without-node_modules.svg)](https://sverweij.github.io/dependency-cruiser/dependency-cruiser-dependency-graph.html)
 how to To generate this yourself do this in the root of the dependency-cruiser repo:

 
```
# The --prefix will make sure that any links in the report open in vscode
# You can alternatively configure this in your .dependency-cruiser.js
node ./bin/dependency-cruise.js bin src --prefix vscode://file/$(pwd)/ --config --output-type dot | \
  # format the output with dot
  dot -T svg |\
  # process the svg into an interactive html graph
  node ./bin/wrap-stream-in-html.js |\
  # The browser command opens the graph-in-html just produced in your
  # default browser
  browser

```
 
>  the only repository in the world you can't use the commands `depcruise`, `depcruise-fmt` or `depcruise-wrap-stream-in-html` is dependency-cruiser's own. Instead we run the JavaScript files from `bin` directly. Alternatively, in the dependency-cruiser repo you can run a script from package.json to get this result as well: `depcruise:graph:view` - which also opens the graph. If you adapt the script for your own use replace `node ./bin/dependency-cruise.js` with `depcruise`, `node ./bin/wrap-stream-in-html.js` with `depcruise-wrap-stream-in-html`.
> 
>  

 
##### state machine cat

[sverweij/state-machine-cat](https://github.com/sverweij/state-machine-cat) - an interpreter for writing nice state diagrams. Click for a slightly more interactive version. As you can see this graph does not group modules from same folders into clusters. Instead it uses only colors for 'grouping' and notes the folder name in the nodes. It's what the ['flat'](https://github.com/sverweij/dependency-cruiser/blob/main/doc/cli.md#flat-fdot) graph reporter does for you. See the *how to* foldout below to see how to reproduce it.

(For this too: click for a slightly more interactive version)

[![state-machine-cat without external dependencies](https://camo.githubusercontent.com/4bd50ca861d1d48e184c4d56438a1ff07b2e25687c6207d9803352a29105c97a/68747470733a2f2f73746174652d6d616368696e652d6361742e6a732e6f72672f646570656e64656e63792d637275697365722d67726170682d666c61742d646f742e737667)](https://state-machine-cat.js.org/dependency-cruiser-graph-flat-dot.html)
 how to 
```
git clone git@github.com:sverweij/state-machine-cat.git
cd state-machine-cat
npm install
npx depcruise src bin/smcat --progress \
    --config config/dependency-cruiser-graph.js \
    --output-type flat \
  | dot -Tsvg \
  | tee docs/dependency-cruiser-graph-flat-dot.svg \
  | npx depcruise-wrap-stream-in-html \
  > docs/dependency-cruiser-graph-flat-dot.html
```
 
##### mscgen.js

[mscgenjs/mscgenjs-core](https://github.com/mscgenjs/mscgenjs-core) - an interpreter library for turning text (in MscGen or two other DSLs) into sequence charts. Click for a slightly more interactive version.

[![mscgen.js](https://camo.githubusercontent.com/64c540b224bd74c93a0a429d99eeab7b84d262406486082e14c3b7457958aff6/68747470733a2f2f6d736367656e6a732e6769746875622e696f2f6d736367656e6a732d636f72652f646570656e64656e637967726170682e737667)](https://mscgenjs.github.io/mscgenjs-core/dependencygraph.html)
