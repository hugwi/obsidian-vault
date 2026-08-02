const page = dv.current();

const VIDEO_EXT = /\.(mp4|webm|mov|m4v)(?:$|[?#])/i;
const IMAGE_EXT = /\.(png|jpe?g|gif|webp|avif|svg)(?:$|[?#])/i;

function valuesOf(value) {
    if (value === null || value === undefined) {
        return [];
    }

    if (Array.isArray(value)) {
        return value.flatMap(valuesOf);
    }

    return [String(value).trim()].filter(Boolean);
}

// A property may hold a bare URL, several URLs from a comma-separated selector,
// or a srcset ("url 1x, url 2x"). Split on whitespace/commas and keep the pieces
// that actually parse as http(s) URLs — descriptors like "1600w" fall away.
function urlsOf(...properties) {
    const found = [];

    for (const property of properties) {
        for (const raw of valuesOf(property)) {
            for (const piece of raw.split(/[\s,]+/)) {
                const candidate = piece.trim();

                if (!candidate) {
                    continue;
                }

                try {
                    const url = new URL(candidate);

                    if (url.protocol === "http:" || url.protocol === "https:") {
                        found.push(candidate);
                    }
                } catch {
                    // Not a URL — skip it.
                }
            }
        }
    }

    return [...new Set(found)];
}

function extensionLooksLike(pattern, value) {
    try {
        const url = new URL(value);

        return pattern.test(url.pathname + url.search);
    } catch {
        return false;
    }
}

const sourceUrl = valuesOf(page.source_url)[0] ?? "";

// Video properties are video-specific, so anything in them counts — streaming
// endpoints often have no file extension at all. Only reject values that are
// plainly an image, which happens when a page puts a still in og:video.
const declaredVideoUrls = urlsOf(
    page.media_url_secure,
    page.media_url,
    page.media_url_twitter,
    page.media_url_schema,
    page.media_url_source,
    page.media_url_video
);

const videoCandidates = declaredVideoUrls.filter(
    (candidate) => !extensionLooksLike(IMAGE_EXT, candidate)
);

if (extensionLooksLike(VIDEO_EXT, sourceUrl)) {
    videoCandidates.push(sourceUrl);
}

// media_url_image is scraped from the page's media container and is usually the
// full-size still; thumbnail_url (og:image) is the fallback. A still that the page
// wrongly published in og:video is rejected above — reuse it here rather than
// losing it, so the note still shows something.
const imageCandidates = [
    ...urlsOf(page.media_url_image, page.thumbnail_url),
    ...declaredVideoUrls.filter((candidate) => extensionLooksLike(IMAGE_EXT, candidate)),
];

if (extensionLooksLike(IMAGE_EXT, sourceUrl)) {
    imageCandidates.push(sourceUrl);
}

const mediaUrl = videoCandidates.find(Boolean);

const posterUrl =
    imageCandidates.find((candidate) => extensionLooksLike(IMAGE_EXT, candidate)) ??
    imageCandidates[0] ??
    "";

const altText = page.title ? String(page.title) : "Preview";

const root = dv.container.createDiv();

root.style.width = "100%";
root.style.maxWidth = "960px";

function addSourceLink(parent, text = "Open the original source") {
    if (!sourceUrl) {
        return;
    }

    const link = parent.createEl("a", {
        text,
        href: sourceUrl,
    });

    link.target = "_blank";
    link.rel = "noopener noreferrer";

    return link;
}

// ---------------------------------------------------------------- no media
if (!mediaUrl && !posterUrl) {
    const fallback = root.createDiv();

    fallback.createEl("p", {
        text: "No direct video URL was exposed by this page.",
    });

    addSourceLink(fallback);

    return;
}

// ------------------------------------------------------------- still image
// No video, but we do have an image — this is the normal Dribbble / Pinterest
// case. Show the still full width instead of reporting a missing video.
if (!mediaUrl) {
    const figure = root.createDiv();

    figure.style.overflow = "hidden";
    figure.style.borderRadius = "12px";
    figure.style.background = "var(--background-secondary)";

    const image = figure.createEl("img");

    image.src = posterUrl;
    image.alt = altText;
    image.loading = "lazy";
    image.style.width = "100%";
    image.style.maxHeight = "80vh";
    image.style.objectFit = "contain";
    image.style.display = "block";

    if (sourceUrl) {
        image.style.cursor = "pointer";
        image.addEventListener("click", () => window.open(sourceUrl, "_blank"));
    }

    const caption = root.createDiv();

    caption.style.marginTop = "8px";
    caption.style.fontSize = "0.85em";
    caption.style.color = "var(--text-muted)";

    addSourceLink(caption);

    return;
}

// ------------------------------------------------------------------- video
const preview = root.createDiv();

preview.style.position = "relative";
preview.style.minHeight = "240px";
preview.style.display = "grid";
preview.style.placeItems = "center";
preview.style.overflow = "hidden";
preview.style.borderRadius = "12px";
preview.style.background = "var(--background-secondary)";

if (posterUrl) {
    const poster = preview.createEl("img");

    poster.src = posterUrl;
    poster.alt = altText;
    poster.loading = "lazy";
    poster.style.width = "100%";
    poster.style.maxHeight = "70vh";
    poster.style.objectFit = "contain";
}

const loadButton = preview.createEl("button", {
    text: "Load video",
});

loadButton.type = "button";
loadButton.style.position = posterUrl
    ? "absolute"
    : "static";

loadButton.style.inset = posterUrl
    ? "auto auto 24px 24px"
    : "";

loadButton.style.padding = "10px 16px";
loadButton.style.cursor = "pointer";

loadButton.addEventListener("click", () => {
    preview.empty();

    const video = preview.createEl("video");

    video.controls = true;
    video.preload = "none";
    video.playsInline = true;
    video.style.width = "100%";
    video.style.maxHeight = "75vh";
    video.style.background = "black";

    if (posterUrl) {
        video.poster = posterUrl;
    }

    // Attach the remote media only after the user presses the button.
    video.src = mediaUrl;
    video.load();

    video.play().catch(() => {
        // Autoplay may be blocked.
        // The user can still use the video controls.
    });
});
