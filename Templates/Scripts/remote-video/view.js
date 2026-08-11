const page = dv.current();

function valuesOf(value) {
    if (value === null || value === undefined) {
        return [];
    }

    if (Array.isArray(value)) {
        return value.flatMap(valuesOf);
    }

    return [String(value).trim()].filter(Boolean);
}

function isDirectVideoUrl(value) {
    try {
        const url = new URL(value);

        return /\.(mp4|webm|mov|m4v)(?:$|[?#])/i.test(
            url.pathname + url.search
        );
    } catch {
        return false;
    }
}

const sourceUrl = valuesOf(page.source_url)[0] ?? "";

const candidates = [
    ...valuesOf(page.media_url_secure),
    ...valuesOf(page.media_url),
    ...valuesOf(page.media_url_twitter),
    ...valuesOf(page.media_url_schema),
    ...valuesOf(page.media_url_source),
    ...valuesOf(page.media_url_video),
];

if (isDirectVideoUrl(sourceUrl)) {
    candidates.push(sourceUrl);
}

const mediaUrl = [...new Set(candidates)].find(Boolean);
const posterUrl = valuesOf(page.thumbnail_url)[0] ?? "";

const root = dv.container.createDiv();

root.style.width = "100%";
root.style.maxWidth = "960px";

if (!mediaUrl) {
    const fallback = root.createDiv();

    fallback.createEl("p", {
        text: "No direct video URL was exposed by this page.",
    });

    if (posterUrl) {
        const image = fallback.createEl("img");

        image.src = posterUrl;
        image.alt = page.title
            ? String(page.title)
            : "Preview";

        image.loading = "lazy";
        image.style.width = "100%";
        image.style.borderRadius = "12px";
    }

    if (sourceUrl) {
        const link = fallback.createEl("a", {
            text: "Open the original source",
            href: sourceUrl,
        });

        link.target = "_blank";
        link.rel = "noopener noreferrer";
    }

    return;
}

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
    poster.alt = page.title
        ? String(page.title)
        : "Video preview";

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
