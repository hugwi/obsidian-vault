---
title: "Angular v16 is here!"
source: "https://blog.angular.io/angular-v16-is-here-4d7a28ec680d"
author: "Minko Gechev"
published: 2023-05-14
created: 2025-11-22
description: "Six months ago, we reached a significant milestone in Angular’s simplicity"
tags:
  - to-process
  - design-automation
---

Six months ago, we reached a significant milestone in Angular’s simplicity and developer experience by [graduating the standalone APIs](https://blog.angular.io/angular-v15-is-now-available-df7be7f2f4c8) from developer preview. Today, we’re thrilled to share that **we’re continuing the Angular Momentum with the biggest release since the initial rollout of Angular**; making large leaps in reactivity, server-side rendering, and tooling. All this comes with [dozens](https://github.com/angular/angular/releases) of quality-of-life improvements across feature requests, with over 2,500 combined thumbs up on GitHub!


![Visual of for the Angular v16 release showing the text “v16” on a laptop with the Angular logo on the right of the image.](https://miro.medium.com/v2/resize:fit:700/1*CNy2EclZxC1hmi_govb_7w.png)Angular v16 release
This post includes lots of content, capturing most of the improvements we made over the past six months. If you want a quick overview watch the video below:


# Rethinking Reactivity


As part of the v16 release we’re excited to share a developer preview of a brand new reactivity model for Angular which brings significant improvements to performance and developer experience.


It’s **entirely backward compatible and interoperable with the current system, and enables**:


* Better run time performance by reducing the number of computations during change detection. Once Angular Signals rollout completely, we’re expecting significant improvements of the [INP](https://web.dev/inp) Core Web Vital metric for apps built with signals
* Brings a simpler mental model for reactivity, making it clear what are the dependencies of the view and what’s the flow of data through the app
* [Enables fine-grained reactivity](https://github.com/angular/angular/discussions/49684), which in future releases will allow us to check for changes only in affected components
* Makes [Zone.js](http://zone.js) optional in future releases by using signals to notify the framework when the model has changed
* Delivers [computed properties](https://github.com/angular/angular/discussions/49683#:~:text=against%20this%20goal.-,Computed%20signals,-Computed%20signals%20create) without the penalty of recomputation in each change detection cycle
* Enables better [interoperability with RxJS](https://github.com/angular/angular/discussions/49681) by outlining a [plan to introduce reactive inputs](https://github.com/angular/angular/discussions/49682#:~:text=request%20for%20Angular.-,Signal%2Dbased%20inputs,-In%20signal%2Dbased)


The initial [GitHub discussion](https://github.com/angular/angular/discussions/49090) hit 682 comments and since then we shared [a series of RFCs](https://github.com/angular/angular/discussions/49685) which received over 1,000 more!


In v16 you can find a new signals library that’s part of `@angular/core` and an RxJS interop package — `@angular/core/rxjs-interop`, the full signal integration in the framework is coming later this year.


## Angular Signals


The Angular signals library allows you to define reactive values and express dependencies between them. You can learn more about the properties of the library in the [corresponding RFC](https://github.com/angular/angular/discussions/49683). Here’s a simple example how to use it with Angular:



```
@Component({  
  selector: 'my-app',  
  standalone: true,  
  template: `  
    {{ fullName() }} <button (click)="setName('John')">Click</button>  
  `,  
})  
export class App {  
  firstName = signal('Jane');  
  lastName = signal('Doe');  
  fullName = computed(() => `${this.firstName()} ${this.lastName()}`);  
  
  constructor() {  
    effect(() => console.log('Name changed:', this.fullName()));  
  }  
  
  setName(newName: string) {  
    this.firstName.set(newName);  
  }  
}
```

The snippet above creates a computed value `fullName`, which depends on the signals `firstName` and `lastName`. We also declare an effect, which callback will execute every time we change the value of any of the signals it reads — in this case `fullName`, which means it transitively also depends on `firstName` and `lastName`.


When we set the value of `firstName` to ”John”, the browser will log into the console:



```
"Name changed: John Doe"
```

## RxJS interoperability


You’ll be able to easily “lift” signals to observables via functions from `@angular/core/rxjs-interop` which is in developer preview as part of the v16 release!


Here’s how you can convert a signal to observable:



```
import { toObservable } from '@angular/core/rxjs-interop';  
  
@Component({...})  
export class App {  
  count = signal(0);  
  count$ = toObservable(this.count);  
  
  ngOnInit() {  
    this.count$.subscribe(() => ...);  
  }  
}
```

…and here’s an example how you can convert an observable to signal to avoid using the async pipe:



```
import {toSignal} from '@angular/core/rxjs-interop';  
  
@Component({  
  template: `  
    <li *ngFor="let row of data()"> {{ row }} </li>  
  `  
})  
export class App {  
  dataService = inject(DataService);  
  data = toSignal(this.dataService.data$, []);  
}
```

Angular users often want to complete a stream when a related subject completes. The following illustrative pattern is quite common:



```
destroyed$ = new ReplaySubject<void>(1);  
  
data$ = http.get('...').pipe(takeUntil(this.destroyed$));  
  
ngOnDestroy() {  
  this.destroyed$.next();  
}
```

We are introducing a new RxJS operator called `takeUntilDestroyed`, which simplifies this example into the following:



```
data$ = http.get('…').pipe(takeUntilDestroyed());
```

By default, this operator will inject the current cleanup context. For example, used in a component, it will use the component’s lifetime.


`takeUntilDestroyed` is especially useful when you want to tie the lifecycle of an Observable to a particular component’s lifecycle.


## Next steps for signals


Next we’ll be working on [signal-based components](https://github.com/angular/angular/discussions/49682) which have a simplified set of lifecycle hooks, and an alternative, more simple way of declaring inputs and outputs. We will also work on a more complete set of examples and documentation.


One of the most popular issues in the Angular repository is “[Proposal: Input as Observable](https://github.com/angular/angular/issues/5689).” A couple of months ago we [responded](https://github.com/angular/angular/issues/5689#issuecomment-879474919) that we want to support this use case as part of a larger effort in the framework. We’re happy to share that later this year we’ll land a feature that will enable signal-based inputs — you’ll be able to transform the inputs to observables via the interop package!


# Server-side rendering and hydration


Based on our annual developer survey, server-side rendering is the number one opportunity for improvement for Angular. For the past couple of months we partnered with the [Chrome Aurora team](https://web.dev/aurora) on improving the performance and DX of the hydration and server-side rendering. Today we are happy to share the developer preview of full app non-destructive hydration!


![A banner for Angular hydration with the hydration text in blue water pattern over the Angular logo](https://miro.medium.com/v2/resize:fit:700/1*9aS-J745p45bqdzASTH3sw.png)A banner for Angular hydration with the hydration text in blue water pattern over the Angular logo
In the new full app non-destructive hydration, Angular no longer re-renders the application from scratch. Instead, the framework looks up existing DOM nodes while building internal data structures and attaches event listeners to those nodes.


The benefits are:


* No content flickering on a page for end users
* Better [Web Core Vitals](http://web.dev/vitals) in certain scenarios
* Future-proof architecture that enables fine-grained code loading with primitives we’ll ship later this year. Currently this surfaces in progressive lazy route hydration
* Easy integration with existing apps, in just a few lines of code (see code snippet below)
* Incremental adoption of hydration with the `ngSkipHydration` attribute in templates for components performing manual DOM manipulation


**In early tests we saw up to 45% improvement of** [**Largest Contentful Paint**](http://web.dev/lcp) **with full app hydration!**


Some applications already enabled hydration in production and reported CWV improvements:


To get started it is as easy as adding a few lines to your `main.ts`:



```
import {  
  bootstrapApplication,  
  provideClientHydration,  
} from '@angular/platform-browser';  
  
...  
  
bootstrapApplication(RootCmp, {  
  providers: [provideClientHydration()]  
});
```

You can find more details on how it works in the [documentation](https://angular.io/guide/hydration).


## New server-side rendering features


As part of the v16 release we also [updated the ng add schematics](https://github.com/angular/universal/commit/3af1451abac574f5e57c5f8b45192532bec2b23a) for Angular Universal which enables you to add server-side rendering to projects using standalone APIs. We also [introduced support for stricter Content Security Policy](https://github.com/angular/universal/commit/9fbdb23c528baffa4cb1cda737382b4cab590269) for inline styles.


## Next steps of hydration and server-side rendering


There is more we plan to do here and the work in v16 is just a stepping stone. In certain cases there are opportunities to delay loading JavaScript that is not essential for the page and hydrate the associated components later. This technique is known as partial hydration and we will explore it next.


Since Qwik popularized the idea of resumability from Google’s closed-source framework Wiz, we’ve received many requests for this feature in Angular. Resumability is definitely on our radar, and we’re working closely with the Wiz team to explore the space. We’re cautious about the constraints on developer experience it comes with, evaluating the different trade-offs and will keep you posted as we make progress.


You can read more about our future plans in “[What’s next for server-side rendering in Angular](https://blog.angular.io/whats-next-for-server-side-rendering-in-angular-2a6f27662b67)”.


# Improved tooling for standalone components, directives, and pipes


Angular is a framework used by millions of developers for a lot of mission critical apps and we take major changes seriously. We started exploring standalone APIs [years ago](https://github.com/angular/angular/pull/27481), in 2022 we released them under developer preview. Now after more than a year of collecting feedback and iterating on the APIs we’d like to encourage an even wider adoption!


To support developers transitioning their apps to standalone APIs, we developed migration schematics and a [standalone migration guide](https://angular.io/guide/standalone-migration). Once you’re in your project directory run:



```
ng generate @angular/core:standalone
```

The schematics will convert your code, remove unnecessary `NgModules` classes, and finally change the bootstrap of the project to use standalone APIs.


## Standalone ng new collection


As part of Angular v16 you can create new projects as standalone from the start! To try the developer preview of the standalone schematics make sure you’re on Angular CLI v16 and run:



```
ng new --standalone
```

You’ll get a simpler project output without any `NgModules`. Additionally, all the generators in the project will produce standalone directives, components, and pipes!


## Configure Zone.js


After the initial release of the standalone APIs we heard from developers that you’d like to be able to configure Zone.js with the new `bootstrapApplication` API.


We added an option for this via `provideZoneChangeDetection`:



```
bootstrapApplication(App, {  
  providers: [provideZoneChangeDetection({ eventCoalescing: true })]  
});
```

# Advancing developer tooling


Now, let us share a few feature highlights from the Angular CLI and language service.


## Developer preview of the esbuild-based build system


Over a year ago we announced that we’re working on experimental support for esbuild in the Angular CLI to make your builds faster. Today we’re excited to share that in v16 our esbuild-based build system enters developer preview! **Early tests showed over 72% improvement in cold production builds.**


![An image showing the logos of Vite and esbuild](https://miro.medium.com/v2/resize:fit:700/1*upgm3yDMVz8pd2jae7S71g.png)An image showing the logos of Vite and esbuild
In `ng serve` we’re now using Vite for the development server, and esbuild powers both your development and production builds!


We want to emphasize that Angular CLI relies on Vite exclusively as a development server. To support selector matching, the Angular compiler needs to maintain a dependency graph between your components which requires a different compilation model than Vite.


You can give Vite + esbuild a try by updating your `angular.json`:



```
...  
"architect": {  
  "build": {                     /* Add the esbuild suffix  */  
    "builder": "@angular-devkit/build-angular:browser-esbuild",  
...
```

Next we’ll be tackling support for i18n before we graduate this project out of developer preview.


## Better unit testing with Jest and Web Test Runner


Based on developer surveys in the Angular and the broader JavaScript community, [Jest](https://jestjs.io/) is one of the most loved testing frameworks and test runners. We’ve received numerous requests to support Jest which comes with reduced complexity since no real browsers are required.


Today, we’re happy to announce that we’re introducing experimental Jest support. In a future release we will also move existing [Karma](https://karma-runner.github.io/) projects to [Web Test Runner](https://modern-web.dev/docs/test-runner/overview/) to continue supporting browser-based unit testing. This will be a no-op for the majority of developers.


You can experiment with Jest in new projects by installing Jest with `npm install jest --save-dev` and updating your `angular.json` file:



```
{  
  "projects": {  
    "my-app": {  
      "architect": {  
        "test": {  
          "builder": "@angular-devkit/build-angular:jest",  
          "options": {  
            "tsConfig": "tsconfig.spec.json",  
            "polyfills": ["zone.js", "zone.js/testing"]  
          }  
        }  
      }  
    }  
  }  
}
```

You can learn more about our future unit testing strategy in our [recent blog post](https://blog.angular.io/moving-angular-cli-to-jest-and-web-test-runner-ef85ef69ceca).


## Autocomplete imports in templates


How many times do you use a component or a pipe in a template to get an error from the CLI or the language service that you’ve actually not imported the corresponding implementation? I bet a ton of times!


The language service now allows auto-import components and pipes.


![Gif showing the automatic import functionality of the Angular language service.](https://miro.medium.com/v2/resize:fit:700/1*exv7w0_OpfVu4v7wfnIupQ.gif)Gif showing the automatic import functionality of the Angular language service.
Gif showing the auto-import functionality of the Angular language service in VSCode


## And there’s more!


In v16 we’re also enabling support for TypeScript 5.0, with [support](https://github.com/angular/angular/pull/49492) for [ECMAScript decorators](https://github.com/tc39/proposal-decorators), removing the overhead of ngcc, adding support for [service workers](https://github.com/angular/angular-cli/commit/c2d2da41b15143e11f597192eef755c5e3fb4c5d) and [app shell](https://github.com/angular/angular-cli/commit/50b9e59a50b737e34ee12ee48ab83d17c2b8744a) in standalone apps, expanding [CSP support in the CLI](https://github.com/angular/angular-cli/commit/ff5ebf9b1244c5a01961cd3dba6bb345392aa57c), and [more](https://github.com/angular/angular-cli/releases)!


# Improving Developer Experience


Together with the large initiatives we’re focused on, we are also working towards bringing highly requested features.


## Required inputs


Since we introduced Angular in 2016 it has not been possible to get a compile-time error if you don’t specify a value for a specific input. The change adds zero overhead at runtime since the Angular compiler performs the check at build time. Developers [kept](https://github.com/angular/angular/issues/37706) [asking](https://github.com/angular/angular/issues/11904) [for](https://github.com/angular/angular/issues/18156) [this](https://github.com/angular/angular/issues/24879) [feature](https://github.com/angular/angular/issues/28403) [over](https://github.com/angular/angular/issues/30974) the years and we got a strong indication that this will be very handy!


In v16 now you can mark an input as required:



```
@Component(...)  
export class App {  
  @Input({ required: true }) title: string = '';  
}
```

## Passing router data as component inputs


The router’s developer experience has been moving forward quickly. A [popular feature request](https://github.com/angular/angular/issues/18967) on GitHub is asking for the ability to bind route parameters to the corresponding component’s inputs. We’re happy to share that this feature is now available as part of the v16 release!


Now you can pass the following data to a routing component’s inputs:


* Route data — resolvers and data properties
* Path parameters
* Query parameters


Here’s an example of how you can access the data from a route resolver:



```
const routes = [  
  {  
    path: 'about',  
    loadComponent: import('./about'),  
    resolve: { contact: () => getContact() }  
  }  
];  
  
@Component(...)  
export class About {  
  // The value of "contact" is passed to the contact input  
  @Input() contact?: string;  
}
```

You can enable this feature by using `withComponentInputBinding` as part of the `provideRouter`.


## CSP support for inline-styles


Inline style elements that Angular includes in the DOM for component styles violate the default `style-src` [Content Security Policy (CSP)](https://angular.io/guide/security#content-security-policy). To fix this, they should either contain a `nonce` attribute or the server should include a hash of the style’s content in the CSP header. Even though at Google we did not find a meaningful attack vector to this vulnerability, many companies enforce strict CSP, leading to the popularity of a [feature request](https://github.com/angular/angular/issues/6361) on the Angular repository.


In Angular v16, we’ve implemented a new feature spanning the framework, Universal, CDK, Material, and the CLI which allows you to specify a `nonce` attribute for the styles of the components that Angular inlines. There are two ways to specify the nonce: using the `ngCspNonce` attribute or through the `CSP_NONCE` injection token.


The `ngCspNonce` attribute is useful if you have access to server-side templating that can add the `nonce` both to the header and the `index.html` when constructing the response.



```
<html>  
<body>  
  <app ngCspNonce="{% nonce %}"></app>    
</body>  
</html>
```

The other way of specifying the nonce is through the `CSP_NONCE` injection token. Use this approach if you have access to the `nonce` at runtime and you want to be able to cache the `index.html`:



```
import {bootstrapApplication, CSP_NONCE} from '@angular/core';  
import {AppComponent} from './app/app.component';  
  
bootstrapApplication(AppComponent, {  
  providers: [{  
    provide: CSP_NONCE,  
    useValue: globalThis.myRandomNonceValue  
  }]  
});
```

## Flexible ngOnDestroy


Angular’s lifecycle hooks provide a lot of power to plug into different moments of the execution of your app. An opportunity over the years has been to enable higher flexibility, for example, provide access to [OnDestroy as an observable](https://github.com/angular/angular/issues/10185).


In v16 we made OnDestroy injectable which enables the flexibility developers have been asking for. This new feature allows you to inject `DestroyRef` corresponding to a component, directive, service or a pipe — and register the `onDestroy` lifecycle hook. The `DestroyRef` can be injected anywhere within an injection context, including outside of your component — in such case the `onDestroy` hook is executed when a corresponding injector is destroyed.:



```
import { Injectable, DestroyRef } from '@angular/core';  
  
@Injectable(...)  
export class AppService {  
  destroyRef = inject(DestroyRef);  
  
  destroy() {  
    this.destroyRef.onDestroy(() => /* cleanup */ );  
  }  
}
```

## Self-closing tags


A [highly requested feature](https://github.com/angular/angular/issues/39525) we recently implemented allows you to use self-closing tags for components in Angular templates. It’s a small developer experience improvement that could save you some typing!


Now you can replace:



```
<super-duper-long-component-name [prop]="someVar"></super-duper-long-component-name>
```

with this:



```
<super-duper-long-component-name [prop]="someVar"/>
```

# Better and more flexible components


Over the past couple of quarters we worked closely with the Material Design team at Google to provide the reference Material 3 implementation for the Web with Angular Material. The MDC Web-based components we [shipped](https://angular.io/guide/roadmap#enhanced-angular-material-components-by-integrating-mdc-web) in 2022 set the foundation for this effort.


As the next step, we’re working towards launching later this year an expressive token-based theming API that enables higher customization of the Angular material components.


**A reminder that we’ll be removing the legacy, non-MDC based components in v17. Make sure you follow our** [**migration guide**](https://github.com/angular/components/blob/main/guides/v15-mdc-migration.md) **to move to the latest.**


## Continuing our accessibility initiative


Following Google’s mission, Angular lets you build web apps for everyone! That’s why we’re continuously investing in [better accessibility](https://github.com/angular/components/issues?q=is%3Aissue+label%3Aa11y+is%3Aclosed) for the Angular CDK and Material components.


# Community contribution highlights


Two of the features introduced by the community we want to highlight are:


* The [extended diagnostics](https://github.com/angular/angular/pull/49512) for proper use of ngSkipHydration by [Matthieu Riegler](https://github.com/JeanMeche)
* The [introduction](https://github.com/angular/angular/pull/48247) of `provideServiceWorker` to enable usage of the Angular service worker without `NgModules` by [Julien Saguet](https://github.com/jsaguet)


Over 175 people contributed to v16 on GitHub and thousands of others contributed via blog posts, talks, podcasts, videos, comments on the reactivity RFCs, etc.


**We want to say a big thank you to everyone who helped us make this release special.**


# Let’s keep the momentum going together!


Version 16 is the stepping stone for the future improvements coming to Angular’s reactivity and server-side rendering over the next year. We’ll be moving the Web forward by innovating in developer experience, performance, while enabling you to build for everyone!


You can be part of the Angular Momentum and help us shape the future of the framework by sharing your thoughts in the upcoming RFCs, surveys, or social media.


![](https://miro.medium.com/v2/da:true/resize:fit:0/5c50caa54067fd622d2f0fac18392213bf92f6e2fae89b691e62bceb40885e74)