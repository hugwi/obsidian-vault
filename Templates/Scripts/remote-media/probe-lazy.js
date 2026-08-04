// Paste into the browser console on a shot/pin page, then read the JSON it returns.
// Answers one question: does the page hold every image at clip time, and in which
// attribute? The clipper only ever sees the DOM as it stands when you press clip, so
// an image the page has not materialised yet cannot be captured by any selector.
//
// Wrapped in an IIFE and logged explicitly because Firefox displays an async IIFE as
// a pending Promise without necessarily printing its eventual return value.
(async () => {
    const SELECTOR = [
        "#ssr-app img",
        '[data-test-id="pin-closeup-image"] img',
        '[data-test-id="closeup-image"] img',
    ].join(", ");

    const count = () => document.querySelectorAll(SELECTOR).length;

    const before = count();

    // Walk to the bottom the way a reader would, giving lazy loaders time to fire.
    for (let y = 0; y < document.body.scrollHeight; y += window.innerHeight) {
        window.scrollTo(0, y);
        await new Promise((resolve) => setTimeout(resolve, 600));
    }

    window.scrollTo(0, document.body.scrollHeight);
    await new Promise((resolve) => setTimeout(resolve, 1500));

    const matched = [...document.querySelectorAll(SELECTOR)];

    const report = {
        url: location.href,
        matchedBeforeScroll: before,
        matchedAfterScroll: matched.length,
        ssrAppImgTotal: document.querySelectorAll("#ssr-app img").length,
        ssrAppExists: Boolean(document.querySelector("#ssr-app")),
        // Per matched element: which attribute actually holds a usable URL. A row
        // where all three are empty is an image the page never materialised.
        images: matched.map((img) => ({
            src: (img.getAttribute("src") || "").slice(0, 100),
            dataSrc: (img.getAttribute("data-src") || "").slice(0, 100),
            srcset: (img.getAttribute("srcset") || "").slice(0, 120),
            natural: `${img.naturalWidth}x${img.naturalHeight}`,
        })),
        // Any shot image the selector is missing entirely — if this is non-empty the
        // container selector needs widening, not the attribute list.
        missedBySelector: [...document.querySelectorAll("img")]
            .filter(
                (img) =>
                    /userupload/.test(img.src) &&
                    !matched.includes(img) &&
                    img.naturalWidth > 500
            )
            .map((img) => ({
                src: img.src.slice(0, 100),
                natural: `${img.naturalWidth}x${img.naturalHeight}`,
                alt: img.alt,
                parents: (() => {
                    const chain = [];
                    let el = img.parentElement;

                    for (let n = 0; n < 5 && el; n += 1) {
                        chain.push(
                            el.tagName.toLowerCase() +
                                (el.id ? "#" + el.id : "") +
                                (typeof el.className === "string" && el.className
                                    ? "." +
                                      el.className.trim().split(/\s+/).slice(0, 2).join(".")
                                    : "")
                        );
                        el = el.parentElement;
                    }

                    return chain;
                })(),
            })),
    };

    const output = JSON.stringify(report, null, 2);

    console.log(output);
    return output;
})();
