const page = dv.current();

const VIDEO_EXT = /\.(mp4|webm|mov|m4v)(?:$|[?#])/i;
const IMAGE_EXT = /\.(png|jpe?g|gif|webp|avif|svg)(?:$|[?#])/i;
// Adaptive-streaming manifests. Chromium — and so Obsidian — cannot play these
// without a JS player, so a <video> pointed at one just fails silently.
const STREAM_EXT = /\.(m3u8|mpd)(?:$|[?#])/i;

function valuesOf(value) {
    if (value === null || value === undefined) {
        return [];
    }

    if (Array.isArray(value)) {
        return value.flatMap(valuesOf);
    }

    return [String(value).trim()].filter(Boolean);
}

function isRemoteUrl(value) {
    try {
        const url = new URL(value);

        // blob: and data: are page-local and meaningless once the tab is gone.
        return url.protocol === "http:" || url.protocol === "https:";
    } catch {
        return false;
    }
}

// A property may hold a bare URL, several URLs because the clipper matched a
// comma-separated selector list, or a srcset. Split on whitespace/commas and keep
// the pieces that are real remote URLs — descriptors like "1600w" fall away.
function urlsOf(...properties) {
    const found = [];

    for (const property of properties) {
        for (const raw of valuesOf(property)) {
            for (const piece of raw.split(/[\s,]+/)) {
                const candidate = piece.trim();

                if (candidate && isRemoteUrl(candidate)) {
                    found.push(candidate);
                }
            }
        }
    }

    return [...new Set(found)];
}

// srcset is "url 320w, url 640w" (or "url 1x, url 2x"). Return the URLs biggest
// first, so a note shows the highest resolution the page offered.
function srcsetUrlsOf(property) {
    const entries = [];

    for (const raw of valuesOf(property)) {
        for (const entry of raw.split(",")) {
            const [url, descriptor] = entry.trim().split(/\s+/);

            if (url && isRemoteUrl(url)) {
                entries.push({ url, weight: parseFloat(descriptor) || 0 });
            }
        }
    }

    entries.sort((a, b) => b.weight - a.weight);

    return [...new Set(entries.map((entry) => entry.url))];
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

// Video properties are video-specific, so anything in them counts — plenty of CDNs
// serve MP4 from an extensionless path. Only reject values that are plainly an
// image, which happens when a page puts a still in og:video.
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

const mediaUrl = videoCandidates.find(
    (candidate) => !extensionLooksLike(STREAM_EXT, candidate)
);

// Captured, but not playable here. Worth saying so rather than showing a dead player.
const streamUrl = videoCandidates.find((candidate) =>
    extensionLooksLike(STREAM_EXT, candidate)
);

// Biggest srcset entry first, then the container's own src, then the social-card
// image, then anything an image-shaped URL that turned up in a video property.
const imageCandidates = [
    ...srcsetUrlsOf(page.media_url_srcset),
    ...urlsOf(page.media_url_image, page.thumbnail_url, page.media_url_image_meta),
    ...declaredVideoUrls.filter((candidate) => extensionLooksLike(IMAGE_EXT, candidate)),
];

const posterUrl =
    imageCandidates.find((candidate) => extensionLooksLike(IMAGE_EXT, candidate)) ??
    imageCandidates[0] ??
    "";

const altText = page.title ? String(page.title) : "Preview";

const root = dv.container.createDiv();

root.style.width = "100%";
root.style.maxWidth = "960px";

function createNote(parent, text) {
    const note = parent.createEl("p", { text });

    note.style.fontSize = "0.85em";
    note.style.color = "var(--text-muted)";
    note.style.margin = "8px 0 0";

    return note;
}

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
        text: streamUrl
            ? "This page only exposed an adaptive video stream, which Obsidian cannot play."
            : "No direct video URL was exposed by this page.",
    });

    addSourceLink(fallback);

    return;
}

// ------------------------------------------------------------- still image
// No playable video, but we do have an image — the normal Dribbble / Pinterest
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

    if (streamUrl) {
        createNote(
            root,
            "This post has video, but only as an adaptive stream Obsidian cannot play — " +
                "showing the still. Open the source to watch it."
        );
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

    // A signed CDN link can expire long after the clip was saved. Say so instead
    // of leaving a black rectangle.
    video.addEventListener("error", () => {
        preview.empty();

        if (posterUrl) {
            const still = preview.createEl("img");

            still.src = posterUrl;
            still.alt = altText;
            still.style.width = "100%";
            still.style.maxHeight = "70vh";
            still.style.objectFit = "contain";
        }

        const failure = root.createDiv();

        createNote(
            failure,
            "The saved video URL did not load — it has probably expired."
        );

        addSourceLink(failure);
    });

    // Attach the remote media only after the user presses the button.
    video.src = mediaUrl;
    video.load();

    video.play().catch(() => {
        // Autoplay may be blocked.
        // The user can still use the video controls.
    });
});
