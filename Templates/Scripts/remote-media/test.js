// Harness: emulates enough of Obsidian's DOM helpers + Dataview's dv.view()
// to exercise Templates/Scripts/remote-media/view.js the way Dataview does.
const fs = require("fs");
const SRC = fs.readFileSync(require("path").join(__dirname, "view.js"), "utf8");

let networkRequests = [];
let rootEl = null;

function makeEl(tag) {
    const el = {
        tag,
        style: {},
        children: [],
        text: undefined,
        _listeners: {},
        get src() { return this._src; },
        set src(v) { this._src = v; networkRequests.push(`${tag}:${v}`); },
        createDiv(...a) { return this._add("div", ...a); },
        createEl(t, opts) { return this._add(t, opts); },
        _add(t, opts) {
            const c = makeEl(t);
            if (opts && opts.text) c.text = opts.text;
            if (opts && opts.href) c.href = opts.href;
            this.children.push(c);
            return c;
        },
        empty() { this.children = []; },
        remove() {
            for (const parent of walk(rootEl)) {
                const at = parent.children.indexOf(this);
                if (at >= 0) parent.children.splice(at, 1);
            }
        },
        addEventListener(ev, fn) { this._listeners[ev] = fn; },
        load() { this.loaded = true; },
        play() { this.played = true; return Promise.resolve(); },
    };
    return el;
}

function walk(el, out = []) {
    out.push(el);
    el.children.forEach((c) => walk(c, out));
    return out;
}
const find = (root, tag) => walk(root).filter((e) => e.tag === tag);

// Emulate the two engines Obsidian actually runs on:
//   desktop (Electron/Chromium) -> canPlayType("application/vnd.apple.mpegurl") === ""
//   iOS (WKWebView)             -> "maybe" or "probably"
function setEngine(hlsSupport) {
    global.document = {
        createElement: () => ({ canPlayType: () => hlsSupport }),
    };
}
setEngine("");

function run(page) {
    networkRequests = [];
    const container = makeEl("div");
    rootEl = container;
    const dv = { current: () => page, container };
    new Function("dv", "input", SRC)(dv, undefined);
    return { container, all: walk(container) };
}

let failures = 0;
function check(name, cond, detail = "") {
    if (cond) console.log(`  PASS  ${name}`);
    else { console.log(`  FAIL  ${name} ${detail}`); failures++; }
}

// ---------------------------------------------------------------- case 1
console.log("\n[1] Happy path: direct MP4 in media_url");
{
    const { container } = run({
        title: "Remote video test",
        source_url: "https://example.com/page",
        thumbnail_url: "https://cdn.example.com/poster.jpg",
        media_url: "https://cdn.example.com/video.mp4",
    });
    const btn = find(container, "button")[0];
    check("thumbnail rendered", find(container, "img").length === 1);
    check("Load video button present", btn && btn.text === "Load video");
    check("no <video> before click", find(container, "video").length === 0);
    check(
        "MP4 NOT requested before click",
        !networkRequests.some((r) => r.includes(".mp4")),
        JSON.stringify(networkRequests)
    );
    check("poster WAS requested (cheap)", networkRequests.some((r) => r.includes("poster.jpg")));

    btn._listeners.click();
    const vid = find(container, "video")[0];
    check("video created after click", !!vid);
    check("video src is the remote MP4", vid && vid._src === "https://cdn.example.com/video.mp4");
    check("preload=none", vid && vid.preload === "none");
    check("controls on", vid && vid.controls === true);
    check("poster set on player", vid && vid.poster === "https://cdn.example.com/poster.jpg");
    check("load() called", vid && vid.loaded === true);
    check("thumbnail replaced (img gone)", find(container, "img").length === 0);
}

// ---------------------------------------------------------------- case 2
console.log("\n[2] Fallback: no media at all (no video, no image)");
{
    const { container } = run({
        title: "Fallback test",
        source_url: "https://dribbble.com/shots/popular",
        thumbnail_url: "",
        media_url_secure: "", media_url: "", media_url_twitter: "",
        media_url_schema: "", media_url_source: "", media_url_video: "",
    });
    const p = find(container, "p")[0];
    const a = find(container, "a")[0];
    check("message shown", p && p.text === "No direct video URL was exposed by this page.");
    check("source link shown", a && a.text === "Open the original source");
    check("link points at source_url", a && a.href === "https://dribbble.com/shots/popular");
    check("link opens in new tab safely", a && a.target === "_blank" && a.rel === "noopener noreferrer");
    check("no button, no video", find(container, "button").length === 0 && find(container, "video").length === 0);
    check("no broken empty <img>", find(container, "img").length === 0);
}

// ---------------------------------------------------------------- case 3
console.log("\n[3] Priority order + de-duplication");
{
    const { container } = run({
        source_url: "https://example.com/page",
        media_url_secure: "https://cdn.example.com/secure.mp4",
        media_url: "https://cdn.example.com/plain.mp4",
        media_url_schema: "https://cdn.example.com/secure.mp4",
    });
    find(container, "button")[0]._listeners.click();
    check(
        "media_url_secure wins over media_url",
        find(container, "video")[0]._src === "https://cdn.example.com/secure.mp4"
    );
}

// ---------------------------------------------------------------- case 4
console.log("\n[4] source_url is itself a direct media file");
{
    for (const ext of ["mp4", "webm", "mov", "m4v"]) {
        const { container } = run({ source_url: `https://example.com/clip.${ext}` });
        const btn = find(container, "button")[0];
        check(`.${ext} accepted as playable`, !!btn);
    }
    const { container } = run({ source_url: "https://example.com/clip.mp4?sig=abc&x=1" });
    check("signed/query-string MP4 accepted", !!find(container, "button")[0]);
    const html = run({ source_url: "https://example.com/page.html" });
    check("plain HTML page NOT treated as video", find(html.container, "button").length === 0);
}

// ---------------------------------------------------------------- case 5
console.log("\n[5] Missing / malformed metadata does not throw");
{
    const cases = {
        "completely empty frontmatter": {},
        "all nulls": { source_url: null, media_url: null, thumbnail_url: null, title: null },
        "array-valued props (multitext)": { media_url: ["", "https://e.com/a.mp4"], thumbnail_url: [] },
        "nested arrays": { media_url: [["https://e.com/n.mp4"]] },
        "whitespace-only values": { media_url: "   ", source_url: "  " },
        "non-string title": { title: 12345, media_url: "https://e.com/a.mp4" },
        "malformed source_url": { source_url: "not a url at all" },
        "no thumbnail but has video": { media_url: "https://e.com/a.mp4" },
    };
    for (const [name, page] of Object.entries(cases)) {
        try { run(page); check(name, true); }
        catch (e) { check(name, false, `threw: ${e.message}`); }
    }

    // spot-check two of the trickier ones behave correctly, not just "not throw"
    const arr = run({ media_url: ["", "https://e.com/a.mp4"] });
    find(arr.container, "button")[0]._listeners.click();
    check("array prop -> first non-empty used", find(arr.container, "video")[0]._src === "https://e.com/a.mp4");

    const ws = run({ media_url: "   ", source_url: "  " });
    check("whitespace-only -> fallback path", find(ws.container, "p")[0].text.startsWith("No direct video"));

    const noThumb = run({ media_url: "https://e.com/a.mp4" });
    check("no thumbnail -> button is static, still works", find(noThumb.container, "button")[0].style.position === "static");
}

// ---------------------------------------------------------------- case 6
console.log("\n[6] Vault never receives the MP4");
{
    const { container } = run({
        thumbnail_url: "https://cdn.example.com/poster.jpg",
        media_url: "https://cdn.example.com/video.mp4",
    });
    find(container, "button")[0]._listeners.click();
    const vid = find(container, "video")[0];
    check("src is an absolute remote URL (streamed, not vault-relative)",
        /^https:\/\//.test(vid._src));
    check("no vault/attachment path anywhere",
        !vid._src.includes("Attachments") && !vid._src.startsWith("app://"));
}

// ---------------------------------------------------------------- case 7
console.log("\n[7] Still image (Dribbble shot with no video)");
{
    const png =
        "https://cdn.dribbble.com/userupload/15023900/file/original-ccf7358e67c02f6c2b8b2aae66554e49.png?resize=1600x1200&vertical=center";
    const { container } = run({
        title: "Landing Page for Yoga Platform",
        source_url: "https://dribbble.com/shots/24325045-Landing-Page-for-Yoga-Platform",
        thumbnail_url: png,
        media_url_image: png,
        media_url: "", media_url_secure: "", media_url_video: "",
    });
    const img = find(container, "img")[0];
    const p = find(container, "p");
    const a = find(container, "a")[0];
    check("image rendered, upgraded to the unresized original",
        !!img && img._src === png.split("?")[0]);
    img._listeners.error();
    check("falls back to the captured URL if the original is gone", img._src === png);
    check("PNG with ?resize query recognised as image", !!img);
    check("NO 'no direct video' message", p.length === 0, JSON.stringify(p.map((x) => x.text)));
    check("no Load video button", find(container, "button").length === 0);
    check("no <video>", find(container, "video").length === 0);
    check("source link still present", a && a.text === "Open the original source");
    check("image is clickable to source", img && img.style.cursor === "pointer");
    check("alt text uses title", img && img.alt === "Landing Page for Yoga Platform");
}

// ---------------------------------------------------------------- case 8
console.log("\n[8] Image vs video precedence");
{
    // A page with both: video must still win, image becomes the poster.
    const { container } = run({
        media_url: "https://cdn.example.com/clip.mp4",
        media_url_image: "https://cdn.example.com/still.png",
    });
    const btn = find(container, "button")[0];
    check("video wins when both exist", !!btn);
    check("image used as poster", find(container, "img")[0]._src === "https://cdn.example.com/still.png");
    btn._listeners.click();
    check("player gets the video, not the image",
        find(container, "video")[0]._src === "https://cdn.example.com/clip.mp4");

    // A still wrongly placed in og:video must not be handed to <video>.
    const wrong = run({ media_url: "https://cdn.example.com/still.png" });
    check("PNG in og:video rejected as video", find(wrong.container, "button").length === 0);
    check("...and rendered as an image instead", find(wrong.container, "img").length === 1);

    // media_url_image should outrank a small og:image thumbnail.
    const both = run({
        media_url_image: "https://cdn.example.com/full.png",
        thumbnail_url: "https://cdn.example.com/thumb.jpg",
    });
    check("media_url_image preferred over thumbnail_url",
        find(both.container, "img")[0]._src === "https://cdn.example.com/full.png");
}

// ---------------------------------------------------------------- case 9
console.log("\n[9] Messy selector output (comma lists / srcset)");
{
    const multi = run({
        media_url_image: "https://cdn.example.com/a.png, https://cdn.example.com/b.png",
    });
    check("comma-separated selector result -> first URL",
        find(multi.container, "img")[0]._src === "https://cdn.example.com/a.png");

    const srcset = run({
        media_url_image: "https://cdn.example.com/a.png 1x, https://cdn.example.com/b.png 2x",
    });
    check("srcset descriptors stripped",
        find(srcset.container, "img")[0]._src === "https://cdn.example.com/a.png");

    const junk = run({ media_url_image: "1600w  not-a-url  ", thumbnail_url: "" });
    check("pure junk -> falls through to no-media message",
        find(junk.container, "p")[0].text.startsWith("No direct video"));

    const rel = run({ media_url: "/relative/path.mp4", thumbnail_url: "" });
    check("relative path rejected (not http/https)",
        find(rel.container, "p").length === 1);
}

// --------------------------------------------------------------- case 10
console.log("\n[10] Still no media written to the vault, image path included");
{
    const { container } = run({
        media_url_image: "https://cdn.example.com/still.png",
        source_url: "https://dribbble.com/shots/1",
    });
    check("image src is remote absolute", /^https:\/\//.test(find(container, "img")[0]._src));
    check("no vault path", !find(container, "img")[0]._src.startsWith("app://"));
}

// --------------------------------------------------------------- case 11
console.log("\n[11] Pinterest: HLS stream instead of a real MP4");
{
    const png = "https://i.pinimg.com/originals/ab/cd/pin.jpg";
    const { container } = run({
        title: "Pin with video",
        source_url: "https://www.pinterest.com/pin/12345/",
        media_url: "https://v1.pinimg.com/videos/mc/hls/ab/cd/ef.m3u8",
        thumbnail_url: png,
    });
    check("no Load video button for .m3u8", find(container, "button").length === 0);
    check("shows the still instead", find(container, "img")[0]._src === png);
    const notes = find(container, "p").map((p) => p.text);
    check("explains why there is no player",
        notes.some((t) => t.includes("adaptive stream")), JSON.stringify(notes));
    check("source link present", find(container, "a")[0].text === "Open the original source");

    // HLS and no image at all -> dedicated message, not the generic one
    const bare = run({
        source_url: "https://www.pinterest.com/pin/1/",
        media_url: "https://v1.pinimg.com/videos/mc/hls/x.m3u8",
    });
    check("HLS + no image -> stream-specific message",
        find(bare.container, "p")[0].text.includes("adaptive video stream"));

    // A real MP4 alongside an HLS manifest must still win
    const both = run({
        media_url: "https://v1.pinimg.com/videos/x.m3u8",
        media_url_video: "https://v1.pinimg.com/videos/x.mp4",
    });
    const btn = find(both.container, "button")[0];
    check("MP4 preferred over HLS", !!btn);
    btn._listeners.click();
    check("player gets the MP4",
        find(both.container, "video")[0]._src === "https://v1.pinimg.com/videos/x.mp4");
}

// --------------------------------------------------------------- case 11b
console.log("\n[11b] Same clip on an engine that DOES support HLS (Obsidian iOS)");
{
    setEngine("maybe");
    const m3u8 = "https://v1.pinimg.com/videos/mc/hls/ab/cd/ef.m3u8";
    const { container } = run({
        title: "Pin with video",
        source_url: "https://www.pinterest.com/pin/12345/",
        media_url: m3u8,
        thumbnail_url: "https://i.pinimg.com/originals/ab/cd/pin.jpg",
    });
    const btn = find(container, "button")[0];
    check("HLS offered as playable where supported", !!btn);
    check("no 'cannot play' note on this engine",
        !find(container, "p").some((p) => p.text.includes("adaptive stream")));
    btn._listeners.click();
    check("player gets the manifest", find(container, "video")[0]._src === m3u8);

    // MP4 must still be preferred over the manifest even here.
    const both = run({
        media_url: m3u8,
        media_url_video: "https://v1.pinimg.com/videos/x.mp4",
    });
    find(both.container, "button")[0]._listeners.click();
    check("MP4 still preferred over HLS on iOS",
        find(both.container, "video")[0]._src === "https://v1.pinimg.com/videos/x.mp4");

    setEngine(""); // back to desktop for the remaining cases
}

// --------------------------------------------------------------- case 12
console.log("\n[12] blob: and data: URLs are not saveable");
{
    const { container } = run({
        media_url_video: "blob:https://www.pinterest.com/9f8e-7d6c",
        thumbnail_url: "https://i.pinimg.com/originals/a.jpg",
    });
    check("blob: rejected as video", find(container, "button").length === 0);
    check("falls back to the still", find(container, "img").length === 1);

    const dataUri = run({ media_url_image: "data:image/png;base64,iVBORw0KG" });
    check("data: URI rejected", find(dataUri.container, "img").length === 0);
}

// --------------------------------------------------------------- case 13
console.log("\n[13] srcset: pick the largest offered resolution");
{
    const { container } = run({
        media_url_srcset:
            "https://i.pinimg.com/236x/a.jpg 236w, https://i.pinimg.com/736x/a.jpg 736w, https://i.pinimg.com/originals/a.jpg 1200w",
        media_url_image: "https://i.pinimg.com/236x/a.jpg",
    });
    check("largest srcset entry wins over the small src",
        find(container, "img")[0]._src === "https://i.pinimg.com/originals/a.jpg");

    const dpr = run({
        media_url_srcset: "https://cdn.example.com/a.png 1x, https://cdn.example.com/b.png 2x",
    });
    check("density descriptors handled (2x wins)",
        find(dpr.container, "img")[0]._src === "https://cdn.example.com/b.png");

    const noDesc = run({ media_url_srcset: "https://cdn.example.com/only.png" });
    check("srcset with no descriptor still works",
        find(noDesc.container, "img")[0]._src === "https://cdn.example.com/only.png");
}

// --------------------------------------------------------------- case 14
console.log("\n[14] Expired video URL surfaces instead of a black box");
{
    const { container } = run({
        media_url: "https://cdn.example.com/expired.mp4",
        thumbnail_url: "https://cdn.example.com/poster.jpg",
        source_url: "https://dribbble.com/shots/1",
    });
    find(container, "button")[0]._listeners.click();
    const vid = find(container, "video")[0];
    check("error handler registered", typeof vid._listeners.error === "function");
    vid._listeners.error();
    const notes = find(container, "p").map((p) => p.text);
    check("expiry explained", notes.some((t) => t.includes("expired")), JSON.stringify(notes));
    check("still shown after failure", find(container, "img").length === 1);
    check("source link offered after failure",
        find(container, "a").some((a) => a.text === "Open the original source"));
}

// --------------------------------------------------------------- case 15
console.log("\n[15] Generic site with only og:image / twitter:image");
{
    const { container } = run({
        title: "Some other site",
        source_url: "https://example.com/work/thing",
        media_url_image: "",
        media_url_image_meta: "https://example.com/og.jpg https://example.com/twitter.jpg",
    });
    check("meta fallback used", find(container, "img")[0]._src === "https://example.com/og.jpg");
    check("no error message", find(container, "p").length === 0);
}

// --------------------------------------------------------------- case 16
console.log("\n[16] Site rules: the three must-have sites");
{
    // Pinterest: a grid thumbnail should be upgraded to /originals/
    const pin = run({
        source_url: "https://www.pinterest.com/pin/1/",
        media_url_image: "https://i.pinimg.com/236x/ab/cd/ef.jpg",
    });
    check("pinterest 236x -> originals",
        find(pin.container, "img")[0]._src === "https://i.pinimg.com/originals/ab/cd/ef.jpg");

    // ...and if /originals/ does not exist, fall back to what was captured
    const pinImg = find(pin.container, "img")[0];
    pinImg._listeners.error();
    check("falls back to the captured 236x on 404",
        pinImg._src === "https://i.pinimg.com/236x/ab/cd/ef.jpg");

    // Dribbble: drop the resize query to get the unscaled original
    const dribbble = run({
        source_url: "https://dribbble.com/shots/24325045-Landing-Page-for-Yoga-Platform",
        media_url_image:
            "https://cdn.dribbble.com/userupload/15023900/file/original-ccf7358e.png?resize=1600x1200&vertical=center",
    });
    check("dribbble resize query dropped",
        find(dribbble.container, "img")[0]._src ===
            "https://cdn.dribbble.com/userupload/15023900/file/original-ccf7358e.png");

    const dribbbleImg = find(dribbble.container, "img")[0];
    dribbbleImg._listeners.error();
    check("falls back to the resized URL if the original 404s",
        dribbbleImg._src.includes("resize=1600x1200"));

    // 21st.dev: video-first, no upgrade rule, must still work end to end
    const twentyFirst = run({
        source_url: "https://21st.dev/component/hero",
        media_url: "https://cdn.21st.dev/hero.mp4",
        media_url_image: "https://cdn.21st.dev/hero.png",
    });
    const btn = find(twentyFirst.container, "button")[0];
    check("21st.dev video plays", !!btn);
    check("21st.dev image used as poster",
        find(twentyFirst.container, "img")[0]._src === "https://cdn.21st.dev/hero.png");

    const twentyFirstStill = run({
        source_url: "https://21st.dev/component/card",
        media_url_image: "https://cdn.21st.dev/card.png",
    });
    check("21st.dev still renders as an image",
        find(twentyFirstStill.container, "img")[0]._src === "https://cdn.21st.dev/card.png");
}

// --------------------------------------------------------------- case 17
console.log("\n[17] Site rules stay contained");
{
    // An unknown host must be left exactly as captured.
    const other = run({ media_url_image: "https://cdn.example.com/236x/a.jpg" });
    check("unknown host is not rewritten",
        find(other.container, "img")[0]._src === "https://cdn.example.com/236x/a.jpg");

    // Rules match on the media host, not the page host.
    const mixed = run({
        source_url: "https://www.pinterest.com/pin/2/",
        media_url_image: "https://images.unsplash.com/photo-123?w=400",
    });
    check("page host does not trigger another site's rule",
        find(mixed.container, "img")[0]._src === "https://images.unsplash.com/photo-123?w=400");

    // Upgrades must never be applied to video URLs.
    const vid = run({ media_url: "https://cdn.dribbble.com/videos/x.mp4?token=abc" });
    find(vid.container, "button")[0]._listeners.click();
    check("video URL keeps its query string",
        find(vid.container, "video")[0]._src === "https://cdn.dribbble.com/videos/x.mp4?token=abc");

    // Exhausting every candidate removes the image rather than leaving it broken.
    const dead = run({ media_url_image: "https://i.pinimg.com/236x/a.jpg" });
    const deadImg = find(dead.container, "img")[0];
    deadImg._listeners.error();
    deadImg._listeners.error();
    check("image removed once all candidates fail", find(dead.container, "img").length === 0);
}

// --------------------------------------------------------------- case 18
console.log("\n[18] Related-shot grid must never outrank the page's own metadata");
{
    // Real case: clipped shot 27586011, but a generic selector matched shot 27611035
    // from the "more shots" grid further down the page.
    const mine = "https://cdn.dribbble.com/userupload/burger-island.png";
    const neighbour = "https://cdn.dribbble.com/userupload/health-analytics.png";

    const { container } = run({
        title: "Burger Island, burger delivery platform line art logo design",
        source_url: "https://dribbble.com/shots/27586011-Burger-Island",
        thumbnail_url: mine,                    // og:image — authoritative
        media_url_image: "",                    // tight selector missed
        media_url_image_generic: neighbour,     // matched the wrong shot
    });
    check("og:image beats a generic DOM match",
        find(container, "img")[0]._src === mine);

    // The generic match is still usable when nothing better exists.
    const onlyGeneric = run({
        source_url: "https://example.com/thing",
        media_url_image_generic: neighbour,
    });
    check("generic still used as a last resort",
        find(onlyGeneric.container, "img")[0]._src === neighbour);

    // A tight, site-specific match outranks og:image, since it is the real container.
    const tight = run({
        thumbnail_url: "https://cdn.dribbble.com/og-card.png",
        media_url_image: mine,
        media_url_image_generic: neighbour,
    });
    check("tight container selector still wins over og:image",
        find(tight.container, "img")[0]._src === mine);

    // Full precedence chain in one go.
    const all = run({
        media_url_srcset: "https://cdn.example.com/big.png 1200w",
        media_url_image: "https://cdn.example.com/container.png",
        thumbnail_url: "https://cdn.example.com/og.png",
        media_url_image_meta: "https://cdn.example.com/twitter.png",
        media_url_image_generic: "https://cdn.example.com/stray.png",
    });
    const img = find(all.container, "img")[0];
    const order = [];
    order.push(img._src);
    for (let i = 0; i < 4; i++) { img._listeners.error(); order.push(img._src); }
    check("precedence: srcset > container > og > meta > generic",
        JSON.stringify(order) === JSON.stringify([
            "https://cdn.example.com/big.png",
            "https://cdn.example.com/container.png",
            "https://cdn.example.com/og.png",
            "https://cdn.example.com/twitter.png",
            "https://cdn.example.com/stray.png",
        ]), JSON.stringify(order));
}

// --------------------------------------------------------------- case 19
console.log("\n[19] Multi-match selectors arrive as a JSON array string");
{
    // This is exactly what the clipper writes when a selector matches >1 element.
    const json = '["https://cdn.dribbble.com/a.png","https://cdn.dribbble.com/b.png"]';

    const { container } = run({ media_url_image: json });
    check("JSON array parsed, first image used",
        find(container, "img")[0]._src === "https://cdn.dribbble.com/a.png");

    // A single match is stored bare — must still work.
    const single = run({ media_url_image: "https://cdn.dribbble.com/only.png" });
    check("single match still handled",
        find(single.container, "img")[0]._src === "https://cdn.dribbble.com/only.png");

    // A bracketed string that is not JSON must not blow up.
    const notJson = run({ media_url_image: "[not json at all", thumbnail_url: "https://e.com/f.png" });
    check("malformed bracket text falls through safely",
        find(notJson.container, "img")[0]._src === "https://e.com/f.png");

    // Video properties get the same treatment.
    const vid = run({ media_url_video: '["https://cdn.example.com/a.mp4"]' });
    const btn = find(vid.container, "button")[0];
    check("JSON array in a video property parsed", !!btn);
    btn._listeners.click();
    check("player gets the parsed URL",
        find(vid.container, "video")[0]._src === "https://cdn.example.com/a.mp4");
}

// --------------------------------------------------------------- case 20
console.log("\n[20] A shot with several images renders all of them");
{
    const gallery = '["https://cdn.dribbble.com/one.png","https://cdn.dribbble.com/two.png","https://cdn.dribbble.com/three.png"]';

    const { container } = run({
        source_url: "https://dribbble.com/shots/27606181-Financial-Dashboard",
        media_url_gallery: gallery,
        thumbnail_url: "https://cdn.dribbble.com/one.png",
    });
    const imgs = find(container, "img");
    check("all three stills rendered", imgs.length === 3, `got ${imgs.length}`);
    check("in document order",
        imgs.map((i) => i._src.split("/").pop()).join(",") === "one.png,two.png,three.png",
        imgs.map((i) => i._src).join(" | "));
    check("each is clickable to the source", imgs.every((i) => i.style.cursor === "pointer"));

    // Each image keeps its own upgrade + fallback chain.
    const pins = run({
        media_url_gallery: '["https://i.pinimg.com/236x/a.jpg","https://i.pinimg.com/236x/b.jpg"]',
    });
    const pinImgs = find(pins.container, "img");
    check("every gallery image is upgraded",
        pinImgs.map((i) => i._src).join(",") ===
            "https://i.pinimg.com/originals/a.jpg,https://i.pinimg.com/originals/b.jpg");
    pinImgs[0]._listeners.error();
    check("one image failing does not affect the others",
        pinImgs[0]._src === "https://i.pinimg.com/236x/a.jpg" &&
        pinImgs[1]._src === "https://i.pinimg.com/originals/b.jpg");

    // media_url_image alone already carries every match, so it drives the gallery too.
    const fromImageProp = run({
        media_url_image: '["https://cdn.dribbble.com/x.png","https://cdn.dribbble.com/y.png"]',
    });
    check("media_url_image with several matches renders all",
        find(fromImageProp.container, "img").length === 2);

    // A single-image shot still renders exactly one.
    const one = run({ media_url_gallery: "https://cdn.dribbble.com/solo.png" });
    check("single-image gallery renders one", find(one.container, "img").length === 1);

    // No gallery captured -> unchanged single-hero behaviour.
    const noGallery = run({ thumbnail_url: "https://cdn.example.com/og.png" });
    check("falls back to the single hero image",
        find(noGallery.container, "img").length === 1 &&
        find(noGallery.container, "img")[0]._src === "https://cdn.example.com/og.png");

    // Video still wins over a gallery of stills.
    const withVideo = run({
        media_url: "https://cdn.example.com/clip.mp4",
        media_url_gallery: gallery,
    });
    check("video still takes precedence over a still gallery",
        find(withVideo.container, "button").length === 1);
}

// --------------------------------------------------------------- case 21
console.log("\n[21] Real Dribbble shot 27606181 (probed 2026-08-04)");
{
    // Verified in-page: the shot's images live in #ssr-app .block-media, while the
    // designer's services-by-user cards sit outside #ssr-app entirely. og:image is a
    // *different* upload id from the DOM image, so metadata alone cannot rebuild the set.
    const ogImage =
        "https://cdn.dribbble.com/userupload/48556246/file/08515bfa69a616df29fc490bfbc19bf1.png?crop=0x0-3200x2400&resize=1600x1200";
    const inPage = "https://cdn.dribbble.com/userupload/48556248/file/f2e88a1df2306dbe0534.png";
    const serviceCard = "https://cdn.dribbble.com/userupload/44513408/file/still-aa63a796441785.png";

    const { container } = run({
        title: "Financial Dashboard, B2B Sales Pipeline & Revenue Tracking",
        source_url: "https://dribbble.com/shots/27606181-Financial-Dashboard",
        media_url_gallery: JSON.stringify([ogImage, inPage]),
        thumbnail_url: ogImage,
    });
    const imgs = find(container, "img");
    check("both shot images rendered", imgs.length === 2, `got ${imgs.length}`);
    check("og:image crop/resize stripped to the original",
        imgs[0]._src ===
            "https://cdn.dribbble.com/userupload/48556246/file/08515bfa69a616df29fc490bfbc19bf1.png",
        imgs[0]._src);
    imgs[0]._listeners.error();
    check("falls back to the cropped og:image if the original 404s", imgs[0]._src === ogImage);
    check("second image independent", imgs[1]._src === inPage);

    // The services cards are outside #ssr-app, so they never reach the gallery — but
    // if one ever leaked in via the generic tier it must not displace the shot.
    const leaked = run({
        media_url_gallery: inPage,
        media_url_image_generic: serviceCard,
    });
    check("a service-card image cannot displace the shot",
        find(leaked.container, "img")[0]._src === inPage);
}

// ── Case 22: a lazy-loaded shot, where the src capture under-counts ──────────
// Dribbble renders images below the fold with a placeholder, so their `src` comes
// back empty and only the srcset (or data-src) carries the real URL.
{
    const first = "https://cdn.dribbble.com/userupload/1/one.png";
    const second = "https://cdn.dribbble.com/userupload/2/two.png";

    // The clipper stores one entry per matched element, empty for the placeholder.
    const viaSrcset = run({
        media_url_gallery: JSON.stringify([first, ""]),
        media_url_gallery_srcset: JSON.stringify([
            `${first}?resize=400x300 400w, ${first}?resize=800x600 800w`,
            `${second}?resize=400x300 400w, ${second}?resize=800x600 800w`,
        ]),
    });
    const srcsetImgs = find(viaSrcset.container, "img");
    check("srcset recovers the lazy image the src capture missed",
        srcsetImgs.length === 2, `got ${srcsetImgs.length}`);
    check("largest srcset entry per image, upgraded",
        srcsetImgs[0]._src === first, srcsetImgs[0]._src);
    check("no variant of image one leaks in as image two",
        srcsetImgs[1]._src === second, srcsetImgs[1]._src);

    const viaLazy = run({
        media_url_gallery: JSON.stringify([first, ""]),
        media_url_gallery_lazy: JSON.stringify(["", second]),
    });
    check("data-src recovers the lazy image",
        find(viaLazy.container, "img").length === 2);

    // Richest capture wins; a poorer one must not shrink the gallery.
    const mixed = run({
        media_url_gallery: JSON.stringify([first, second]),
        media_url_gallery_srcset: `${first} 800w`,
        media_url_gallery_lazy: "",
    });
    check("a one-image srcset cannot shrink a two-image src capture",
        find(mixed.container, "img").length === 2);

    // A genuine single-image shot keeps the full precedence chain, not the gallery
    // shortcut — otherwise a 404 could no longer fall back to og:image.
    const single = run({
        media_url_gallery: first,
        media_url_gallery_srcset: `${first}?resize=400x300 400w`,
        thumbnail_url: "https://cdn.dribbble.com/userupload/3/og.png",
    });
    const singleImgs = find(single.container, "img");
    check("single-image shot still renders one image", singleImgs.length === 1);
    singleImgs[0]._listeners.error();
    check("single-image shot keeps its fallback chain",
        singleImgs[0]._src !== first, singleImgs[0]._src);
}

// ── Case 23: the real clipped note, verbatim ────────────────────────────────
// Values copied from "Financial Dashboard - B2B Sales Pipeline & Revenue Tracking.md"
// as the clipper actually wrote them — except shotTwo, which is a stand-in: that clip
// never captured the second image, which is the bug this case pins down. The empty
// slot at index 1 is where it should have been.
{
    const shotOne =
        "https://cdn.dribbble.com/userupload/48556248/file/f2e88a1df2306dbe05345d34077eef9d.png?resize=752x&vertical=center";
    const shotTwo =
        "https://cdn.dribbble.com/userupload/48556249/file/a1b2c3d4e5f60718293a4b5c6d7e8f90.png?resize=752x&vertical=center";
    const serviceCards = [
        "https://cdn.dribbble.com/userupload/44513408/file/still-aa63a796441785157c67c8b39238af71.png?resize=400x300&vertical=center",
        "https://cdn.dribbble.com/userupload/46513805/file/still-f52ceef54e6e34456e6f2e3ce55d167a.png?resize=400x300&vertical=center",
    ];
    const ogImage =
        "https://cdn.dribbble.com/userupload/48556246/file/08515bfa69a616df29fc490bfbc19bf1.png?crop=0x0-3200x2400&resize=1600x1200";

    // What the old, over-narrow `.block-media` selector produced: nothing.
    const empty = run({
        media_url_gallery: "",
        media_url_image: "",
        thumbnail_url: ogImage,
        media_url_image_generic: JSON.stringify([shotOne, "", ...serviceCards]),
    });
    check("an empty gallery still renders something rather than failing",
        find(empty.container, "img").length === 1);

    // What `#ssr-app img` produces: two slots, the second one lazy.
    const fixed = run({
        media_url_gallery: JSON.stringify([shotOne, ""]),
        media_url_gallery_srcset: JSON.stringify(["", `${shotTwo} 752w`]),
        media_url_gallery_lazy: JSON.stringify(["", ""]),
        thumbnail_url: ogImage,
        media_url_image_generic: JSON.stringify([shotOne, "", ...serviceCards]),
    });
    const imgs = find(fixed.container, "img");
    check("both shot images render from the real clip", imgs.length === 2,
        `got ${imgs.length}`);
    check("the ?resize= variant is upgraded to the original",
        imgs[0]._src === shotOne.split("?")[0], imgs[0]._src);
    check("no service card reaches the gallery",
        !imgs.some((img) => /still-/.test(img._src)));
}

console.log(failures === 0 ? "\nALL CHECKS PASSED" : `\n${failures} CHECK(S) FAILED`);
process.exit(failures === 0 ? 0 : 1);
