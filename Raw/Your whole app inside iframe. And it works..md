---
categories:
  - "[[Clippings]]"
domain: [agentic-engineering, software-engineering]
tags:
  - security
  - spec-driven
source: readwise
created: 2026-06-23
rating: 
action: 
theme: work-breakdown-specs
subtheme:
  - architecture-design
  - spec-driven
---

# Your whole app inside iframe. And it works.

![rw-book-cover](https://media2.dev.to/dynamic/image/width=1000,height=500,fit=cover,gravity=auto,format=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F1mmco9p24dlnsup01egh.png)

## Metadata
- Author: [[DEV Community]]
- Full Title: Your whole app inside iframe. And it works.
- Category: #articles
- Summary: Embedding your app as an iframe widget lets others easily add it to their websites using simple HTML and JavaScript. The widget communicates with the host page to resize and handle navigation smoothly, even across different browsers. For security and usability, you control embedding permissions and handle special cases like Safari’s cookie restrictions.
- URL: https://dev.to/javar/wrap-them-all-odo

## Full Document
Imagine a big web-service with hundreds of thousands users, complex interfaces and navigation, authorization, and payment integrated. Imagine one day your PO comes to you and asks to make not one part of it, but everything, and embeddable. Is it even possible and how much will it cost?

####  Why?

Yeah, that question comes to your mind first. Why does someone want to do things like this? The answer is simple - this is the cheapest possible way of integration. If you want as much people as possible to use your widget on their web-pages, you have to embed. In this case the consumer only needs to insert some html tags, or call some javascript - and thats's it, job's done. No development needed.

It starts making even more sense when your business is connected with sales on the web. If you want to sell airplane tickets or hotel bookings, you have to be on the travel-bloggers web pages. If you want to sell tools for web-advertising, you need to be on the sites like Tilda and Shopify, where people manage their business. And the easiest way to get there is through a embeddable widget.

Big guys have a [separate](https://medium.com/r/?url=https%3A%2F%2Fb2b.anywayanyday.com%2Fen%2Fb2b%2Fweb%2F) [applications](https://medium.com/r/?url=https%3A%2F%2Fwww.booking.com%2Faffiliate-program%2Fv2%2Fselfmanaged.en-gb.html) to work inside a widgets, but what if your business is not that big and you don't have a team of developers to implement every feature twice, for the main service and for the embedded one. In that case this crazy idea comes to your mind. Why do not just embed everything?

####  How?

First, you need to build a proof-of-concept application. For that, let's first create a service, that will act like external consumer of your widget, I'll call it Dummy. You will use it for development, testing, and experimenting. Here are the requirements:

1. Dummy-service and widget **must** use different origins. The port address is also a part of the origin, so for the local development you may just run your widget and dummy service on the different ports.
2. It should be easy to switch the address of your widget-application via the dummy-service interface.
3. Dummy-service must be mobile-friendly, especially if your widgets are.
4. It will be helpful if dummy-service will mimic to the real-world services that you want to use your widgets on.

I consider Dummy to look like this:

[![Separate service for developing and testing embed widget](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feaz5z797w2ryo4xo1yda.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Feaz5z797w2ryo4xo1yda.png)
From now on, we can start experimenting. Let's create `iframe`, set its `src` to our application url, reset some styles and insert it to our Dummy.

```

<iframe
    title="My application widget"
    src="https://my-application.com"
    style="width:100%; border:none; min-height:300px;"
>
</iframe>

```

The first thing you’ll notice — frame filled all available width, but has a hight of only `300px` and a vertical scroll bar. Our host application, Dummy in this case, knows nothing about your frame content and can not resize itself to frame’s height.

The only way for Dummy to respect widget’s application height is through frame communication, and the only way to organize cross-origin frame communication is through [window.postMessage](https://developer.mozilla.org/en-US/docs/Web/API/Window/postMessage) API.

From here it becomes clear, that we need some javascript on the page of Dummy service to listen to all this messages and resize the frame. So, our application will be distributed not just by inserting an `<iframe>` tag, but with `<script>` tag and initialization call.

[![Initialization section subheader](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fllen8lamnww0aadkfymc.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fllen8lamnww0aadkfymc.png)
####  Initialization

The main goal of this script is to provide a javascript API for our consumers to embed our widget. Let’s imagine how may look a call to this API in browser.

```

<script async src="https://some-cdn-server.net/widget/v1/script.js"></script>
<script>
   window.framedWidgetCallback = () => {
      const widget = new window.FramedWidget({
         container: document.querySelector('#container'),
         consumerId: 'dummy'
      });
   }
</script>

```

Here are the important things:

1. Use versioning for initialization script: `/widget/v1/script.js`. In the future we may want to break the backward compatibility to be able to change our widget in any possible way.
2. My advice is **not to cache** this script for a long time, especially on the early stages of development. You may want to provide a new functionality with the same script file. Or, the worst scenario, you may find a bug inside this code and you'll want all of you consumers to get it fixed. So don't set [`max-age`](https://medium.com/r/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FCache-Control%23cache_directives) to more than couple of hours and just use [`ETag`](https://medium.com/r/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FHTTP%2FHeaders%2FETag) for cache invalidation.
3. Use `async` attribute with your script tag, or be ready, that the consumer will set it. To be sure that your script is loaded when you call an initialization function, use the callback as shown in the code above, or fire some custom event.
4. Provide every consumer with unique id, it will be used for security, metrics tracking, and problems investigations.

The script itself may be written in OOP style, I prefer using typescript when possible, but you may choose anything that works for you:

```

interface Window {
    FramedWidget: typeof FramedWidget;
    framedWidgetCallback: () => void;
}

interface InitParams {
    container: HTMLElement;
    consumerId: string;
}

interface Message {
    type: 'height-changed';
    value: number;
}

class FramedWidget {
    constructor(params: InitParams) {
        this.init(params);
    }

    private frameOrigin = 'https://my-application.com';

    private frame: HTMLIFrameElement | undefined;

    private parseMessage(message: string) {
        let result: Message | undefined;

        try {
            result = JSON.parse(message);
        } catch (e) {}

        return result;
    }

    private postMessageHandler = (event: MessageEvent<string>) => {
        if (event.origin !== this.frameOrigin) {
            return;
        }

        const message = this.parseMessage(event.data);

        if (message?.type === 'height-changed') {
            this.frame!.style.height = `${message.value}px`;
        }
    };

    private init(params: InitParams) {
        this.frame = document.createElement('iframe');
        this.frame.src = `${this.frameOrigin}?consumerId=${params.consumerId}`;
        this.frame.setAttribute('style', 'width:100%; border:none; min-height:300px;');

        params.container.appendChild(this.frame);

        window.addEventListener('message', this.postMessageHandler);
    }

    destroy = () => {
        window.removeEventListener('message', this.postMessageHandler);
    };
}

if (typeof window !== 'undefined') {
    window.FramedWidget = FramedWidget;
    window.framedWidgetCallback?.();
}

```

The things to notice are:

1. Provide your consumers with `destroy` method out of the box, they should be able to use your code inside single-page applications.
2. When parsing messages inside `postMessageHandler` always check the `event.origin` and wrap your `JSON.parse` code inside `try ... catch` blocks.
3. Set `min-height` style attribute to the frame to some meaningful value. It will help on initial rendering and in case if something goes not as planned.
4. Build this code to be used in as many browsers as possible. The fallback with message for older browser must be a part of your widget code, not a part of this script. My advice is to set `"target": "es6"` in your `tsconfig.json` or something like `> 0.2%, not dead` in .browserslistrc.
5. You may also want to use `debounce` when changing the frame hight to provide better performance.

I should also mention that there are some libraries to resize frames to fit their contained content, the most popular is [iframe-resizer](https://medium.com/r/?url=https%3A%2F%2Fgithub.com%2Fdavidjbradshaw%2Fiframe-resizer%2Fblob%2Fmaster%2Fsrc%2FiframeResizer.js), but maybe you don't need all of it's complexity.

So far so good. Now we can initialize our widget through script and it will be resized horizontally and vertically. Everything seems to work fine, until we click our first external link, for example, to social media. Yep, the Facebook will be opened inside the frame. Navigation inside the frame might be a really tricky, but now we have all the tools to make it work right.

[![Navigation section subheader](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F180nwk3ywtsk1pb6azhe.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F180nwk3ywtsk1pb6azhe.png)
####  Navigation

There are only four types of navigation cases you may want to differ inside your widget:

1. Real links that should be opened *inside the frame*. This is a simple case, just use `target="self"` and everything will be fine.
2. Real links that should be opened in the *host window*. Also easy to solve, `target="top"` will do the trick.
3. Transitions made through javascript, `window.location.href` or `history.pushState`, that you want to do *inside the frame* - just leave them as they are, they are supposed to work fine.
4. Transitions made through javascript, that you want to do in the *host window*. The only way to do it is through the `window.parent.postMessage` calls.

For everything here to work properly on every page of your application you need to know either it is running inside the frame or standalone. The way of receiving this information in browser is [quite simple](https://medium.com/r/?url=https%3A%2F%2Fdeveloper.mozilla.org%2Fen-US%2Fdocs%2FWeb%2FAPI%2FWindow%2Fparent):

```

const isInFrame = window !== window.parent;

```

So, if your application runs only in browser, that is actually all you need.

But the server-side logic is much trickier. There is no way to figure out where the application is running by looking at the HTTP-request, no special headers, nothing more. So, you need to use custom urls when your application runs inside the frame. Here are the possibilities:

1. Use query param, like `?inFrame=1` and append it to all the links of your application.
2. Use custom subdomain for framed application, like `framed.my-application.com`. This is a ‘cleaner’ way, because your links and application logic might not change that much. The caveat here is that if you want your authorization and other cookie-based logic to work on this subdomain pages, you need to always [specify domain](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cookies#define_where_cookies_are_sent) when setting your cookies.  
 Another important restriction here is that data stored in **local/session storage won’t be available on subdomains**, so bear this in mind and choose wisely.

When this is achieved, you may customize some of your application behavior, when it runs inside the frame. For example, you may want to hide your header or footer, change some contact information for your support to know that they are dealing with widget users, and so on.

So, application works fine inside and outside the frame, it resizes properly, you may follow any link. Even authorization works just as expected, server receives cookies from your embedded widget, the job’s seams to be done. Until you open your widget with Safari browser.

[![Authorization section header](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4kyw7s3lfvjsqnshbptt.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2F4kyw7s3lfvjsqnshbptt.png)
####  Authorization

The reason authorization won’t work in Safari is the [Full Third-Party Cookie Blocking](https://webkit.org/blog/10218/full-third-party-cookie-blocking-and-more/) policy. Safari won’t send any cookies for cross-site resources, that means that your widget just won’t get any cookies in the Safari. And not just in the Safari, but in all of the [WebKit-based](https://en.wikipedia.org/wiki/WebKit) browsers.

And trust me here, I tried a lot of very different approaches, the only way to do it right is by using [Storage Access API](https://webkit.org/blog/8124/introducing-storage-access-api/) introduced by the WebKit developers. What you need here is to *ask* users for the access to the data, stored in their browsers. The restriction is that you can do it only after user interaction, like click event.

I consider doing it this way:

1. When application is loaded and the user is not authorized, firstly check the `document.hasStorageAccess()`.
2. If this resolves as `false`, you should show the user a page with an explanation of what is the storage access and why you ask for it, and of course the button to grant it.
3. After the storage access is granted, you may proceed to the authorization.
4. The access to storage will be granted for the origin and `document.hasStorageAccess()` will resolve to true afterwards. The duration of this access vary from browser to browser and may be changed because all the Storage Access API is still a [draft](https://privacycg.github.io/storage-access/).

The code for this flow may look like this.

```

const checkStorageAccess = async (): Promise<boolean> => {
    if (document.hasStorageAccess) {
        return document.hasStorageAccess();
    }

    return true;
}

const requestStorageAccess = async () => {
    const hasStorageAccess = await checkStorageAccess();

    if (hasStorageAccess) {
        proceedToAuthorization();
        return;
    }

    return document.requestStorageAccess()
        .then(() => {
            proceedToAuthorization();
        })
        .catch(() => {
            proceedToErrorPage()
        })
}

document
    .querySelector('.grant-access-button')
    .addEventListener('click', requestStorageAccess);

```

You may now use authorization in your widget. The only important thing left is security.

[![Security section header](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcwqgpzuiogem4ycwfxyj.png)](https://media2.dev.to/dynamic/image/width=800%2Cheight=%2Cfit=scale-down%2Cgravity=auto%2Cformat=auto/https%3A%2F%2Fdev-to-uploads.s3.amazonaws.com%2Fuploads%2Farticles%2Fcwqgpzuiogem4ycwfxyj.png)
####  Security

From the security perspective, you want to control the pages that embed your widget. This is achievable with [`frame-ancestors`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors) directive inside your `Content-Security-Policy` HTTP-header. Here is my advice:

1. Use some sort of identifier for your consumer, like `consumerId` mentioned above, and set the `frame-ancestors` to only specify domains used by this consumer.
2. Use `https://` for all the domains listed in `frame-ancestors` directive.
3. Check the `event.origin` when listening to the `message` event.
4. Use only `Secure` and `HttpOnly` cookies to store authorization data.
5. I would not recommend to set `sandbox` attribute to your iframe with any value.

And that’s it. With all these preparations, you can build a truly responsible, secure and feature-full widget made on top of your base application, without the need to rewrite all of it and to maintain a separate versions of it.

Just make the testing of a widget a part of your e2e-pipeline and remember to check it when developing new features.

If you have any further questions or want to discuss the topic — please contact me here.
