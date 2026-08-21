# Web Clipper Templates (with AI summary)

Templates for the **Obsidian Web Clipper** browser extension. The `*-summary.json` ones
clip the full content and put an AI **TL;DR + Key points** on top; `inspiration-media.json`
is a no-AI visual clipper.

## Files

| Template | Triggers on | Saves to |
|---|---|---|
| `inspiration-media.json` | 21st.dev, dribbble.com, pinterest.com, pin.it, `schema:@VideoObject` | `Clippings` |
| `youtube-summary.json` | youtube.com/watch, youtu.be | `Inbox/Videos` |
| `medium-summary.json` | medium.com (+ subdomains) | `Inbox/Articles` |
| `article-summary.json` | any page with `schema:@Article` / `@NewsArticle` | `Inbox/Articles` |
| `reddit-summary.json` | reddit.com/r/ | `Inbox/Articles` |
| `x-summary.json` | x.com, twitter.com | `Inbox/Articles` |

### Template order in the extension

Web Clipper uses the **first** template whose trigger matches, in list order, and it does
not prefer a URL trigger over a schema one. No two templates here share a URL trigger, but
two schema triggers overlap, so order them most-specific → most-generic:

| # | Template | Why here |
|---|---|---|
| 1 | `youtube-summary.json` | YouTube pages also carry `schema:@VideoObject`, which #2 triggers on |
| 2 | `inspiration-media.json` | design sites also carry `schema:@Article` sometimes, which #6 triggers on |
| 3 | `medium-summary.json` | URL-specific, no overlap |
| 4 | `reddit-summary.json` | URL-specific, no overlap |
| 5 | `x-summary.json` | URL-specific, no overlap |
| 6 | `article-summary.json` | generic `schema:@Article` / `@NewsArticle` catch-all — must be last |

None of the pre-existing templates trigger on 21st.dev, Dribbble or Pinterest, so
`inspiration-media.json` is the only one that claims those sites.

### No community template covers these sites

Checked against [obsidian-community/web-clipper-templates](https://github.com/obsidian-community/web-clipper-templates)
(2026-08-02, repo still marked "under construction"). All 14 templates there are
URL-triggered at text/link sites — Apple Podcasts, GitHub (issues/releases/repo), Gmail,
Indeed, Medium, Reddit, Stackademic, The Hacker News and five YouTube variants. **Nothing
targets Dribbble, Pinterest, 21st.dev or Behance, and nothing scrapes `og:video` or a
media container.** So this template is not duplicating existing work.

Two things to watch if you ever import from that collection:

- `stackademic-bullet-summary-clipper.json` also triggers on the generic `schema:@Article`,
  so it belongs down at position 6 alongside `article-summary.json`.
- Its five YouTube templates all trigger on `youtube.com/watch` and would collide with each
  other and with our `schema:@VideoObject`. Import at most one, and keep it at position 1.

Their `CONTRIBUTING.md` also suggests pairing templates with a plugin that **downloads
images into the vault**. That is the opposite of what this workflow wants — remote URLs
only — so do not adopt that pattern here.

### Templater does not interfere

`Clippings/` has a Templater folder template (`Templates/Clipping Template.md`) and
`trigger_on_file_creation` is on, which looks like it would overwrite every clip. It does
not. Templater's creation handler measures the body length after the frontmatter and only
applies a folder template when that is **zero**; a file that arrives with a body instead
gets scanned for `<% %>` commands and is otherwise left alone. Clips from this template
always carry a body (heading, `dataviewjs` block, source link, notes sections), and that
body contains no Templater syntax. The 378 Readwise notes already in `Clippings/` confirm
the same behaviour in practice — none of them carry the folder template's markers.

The one way to break this is to empty `noteContentFormat`. Keep a body in it.

> **Which browser you clip with does not affect playback.** The renderer runs inside
> Obsidian, not in your browser, so a clip made in Firefox behaves exactly like one made
> in Chrome. The Firefox and Chromium builds of the extension are the same extension, and
> `inspiration-media.json` uses no Interpreter/AI variables, so nothing here depends on
> browser-specific features.

## One-time setup

1. Install **Obsidian Web Clipper** (Chrome/Firefox/Safari extension).
2. Extension → **Settings → General** → set **Vault** to `hugwi`.
3. **Settings → Interpreter** → enable it and add a model/API key
   (OpenAI, Anthropic, Ollama, etc.). **The AI summary only works with the
   Interpreter enabled** — without it the `TL;DR`/`Key points` blocks stay empty.
4. **Settings → Templates → Import** → import each `*.json` in this folder.

## How it works

- The `context` field is the *only* text the AI sees. Prompt variables
  `{{"...prompt..."|filters}}` run against that context.
- Summary is placed first in the note body; raw content follows below it.
- The filter chains (`strip_tags|strip_md|replace:...`) force clean ASCII
  plain-text and bullet lists so frontmatter/body stay tidy.
- Every `noteNameFormat` must use Web Clipper's `safe_name` filter for every
  title-derived component. This is required for Android sync: generated filenames
  must not contain `" * / : < > ? \\ |`, emoji, or unusual Unicode punctuation.
  Keep the original unsanitized title in the note body/properties, not the filename.
  If adding a template, use `safe_name` on each title/author/snippet component and
  keep the result reasonably short.

## Per-platform notes

- **YouTube**: open the **Transcript** panel on the video page *before* clipping —
  the transcript is scraped from the DOM (`#segments-container`). Summary context
  = description + transcript, so it still produces a summary if no transcript.
- **Reddit / X**: these are SPAs with changing CSS. Scroll to load the post/thread
  (and comments) before clipping. If selectors break after a site redesign, update
  the `selector:`/`selectorHtml:` paths via right-click → Inspect.
- **Article**: generic fallback using Obsidian's readability extraction
  (`{{content}}`). Use it (pick manually from the clipper dropdown) for any blog
  or news site without a dedicated template.

## Editing summary style

Change the prompt text inside `{{"..."}}` in `noteContentFormat` to adjust length
or focus (e.g. "5 bullet action items", "ELI5 paragraph"). Keep the trailing
`|...` filter chain — it does the cleanup.

## `inspiration-media.json` — design inspiration

Saves web-design inspiration to `Clippings/` as **metadata + remote URLs only**. No AI,
no Interpreter needed, and **no MP4 is ever written into the vault**.

It scrapes the page for a playable video in this order and stores whatever it finds:

| Property | Scraped from |
|---|---|
| `media_url_secure` | `og:video:secure_url` |
| `media_url` | `og:video` |
| `media_url_twitter` | `twitter:player:stream` |
| `media_url_schema` | Schema.org `VideoObject` → `contentUrl` |
| `media_url_source` | `<video><source src>` |
| `media_url_video` | `<video src>` |
| `media_url_image` | `src` of the page's media container (see selectors below) |
| `media_url_srcset` | `srcset` of the same container — the renderer picks the biggest entry |
| `media_url_image_meta` | `og:image:secure_url`, `twitter:image`, schema `ImageObject.contentUrl`, `<video poster>` |
| `thumbnail_url` | `og:image` |

Most Dribbble and Pinterest posts are **stills, not video**, so the clipper grabs the
image out of the media container rather than only hunting for an MP4.

The container selector is a list, ordered site-specific → generic, so it degrades to
something sensible on a site it has never seen:

```
[data-test-id="pin-closeup-image"] img,   ← Pinterest
[data-test-id="closeup-image"] img,
[data-test-id="pin-image"] img,
.shot-media-container img,                ← Dribbble
.media-shot img,
[data-testid="shot-media"] img,
figure img,                               ← generic semantic markup
main img
```

If every selector misses, `media_url_image_meta` and `thumbnail_url` still carry the
social-card image, which nearly every site publishes. For a site with no dedicated
trigger, pick **Inspiration - Media** manually from the clipper's template dropdown.

The note body calls the Dataview renderer:

```dataviewjs
await dv.view("Templates/Scripts/remote-video");
```

It picks one of three presentations:

| Page has | Note shows |
|---|---|
| a playable video (`.mp4`, `.webm`, `.mov`, `.m4v`, or an extensionless CDN path) | thumbnail + **Load video** button; the source is attached only on click |
| a still only | the image full width, click-through to the original |
| an HLS/DASH stream only | the still, plus a line saying Obsidian cannot play it |
| neither | *"No direct video URL was exposed by this page."* + source link |

Selection happens at render time, not clip time, so the note picks the best of whatever
was captured:

- A still is never handed to the `<video>` element, and an image-shaped URL found in a
  video property is reused as the image rather than discarded.
- `.m3u8` / `.mpd` manifests are only offered where the engine can actually play them.
  The renderer asks via `canPlayType` rather than assuming: desktop Obsidian is
  Electron/Chromium and has no native HLS, so you get the still plus an explanation;
  Obsidian on iOS runs in WKWebView and plays HLS fine, so there you get a player. A real
  MP4 always wins over a manifest on either.
- `blob:` and `data:` URLs are dropped. They are page-local and meaningless once the tab
  closes, which is what Pinterest's player often hands you.
- `srcset` is parsed and the **largest** entry wins, so pins saved from a grid still show
  full resolution rather than the 236px thumbnail.
- If the video fails to load when you press the button — a signed CDN link that has since
  expired — the note says so and falls back to the still plus the source link.

**Requires DataviewJS.** Settings → Dataview → *Enable JavaScript Queries*. This vault
ships it pre-enabled via `.obsidian/plugins/dataview/data.json`.

Every clip starts with the tags `inspiration`, `web-design`, `ui`, `ux`; add finer ones
(`animation`, `navigation`, `mobile`, `landing-page`, `typography`, `dashboard`,
`interaction-design`) by hand. Browse the library at [[Inspiration]] / `Inspiration.base`.

## Adding another site

The workflow is built in two layers, and most new sites need only the first.

**1. Capture** — `inspiration-media.json`

- Add a trigger. Prefer a regex so subdomains and country domains come along:
  `"/^https?:\\/\\/([a-z0-9-]+\\.)?example\\.com\\//"`.
- If the site's media does not sit in a `figure`, `article` or `main`, add its
  container selector to the **front** of the `media_url_image`, `media_url_srcset`,
  `media_url_video` and `media_url_source` lists. Right-click the image → Inspect.
- **Scope every video selector to the media container.** A bare `{{selector:video?src}}`
  matches the first `<video>` anywhere on the page, which on a Dribbble still-shot page is
  a clip from the "More by this designer" grid — the note then offers a Load video button
  for somebody else's shot. The video selectors deliberately stop at `figure video` and do
  not fall back to `article video` / `main video`, because a video that far out is almost
  always a recommendation rather than the thing you clipped. The image selectors do go that
  broad, since a stray `<img>` in `main` is usually the hero.
- Nothing else changes: the property schema, the note body and the renderer are shared.

Often you can skip even this. The generic selectors plus `media_url_image_meta`
(`og:image`, `twitter:image`, schema, `<video poster>`) already cover most sites — try
clipping one first and only add a selector if `media_url_image` comes back empty.

**2. Presentation** — `Templates/Scripts/remote-video/view.js`

Only needed when a site serves downscaled stills and a URL rewrite gets the full-size
one. Append an entry to the `SITES` table at the top of the file:

```js
{
    id: "example",
    match: /(^|\.)example\.com$/,   // tested against the MEDIA host, not the page
    upgrade: (url) => [url.replace("/thumb/", "/full/")],
},
```

`upgrade` returns URLs to try **before** the captured one. A wrong guess is free — the
renderer walks down the list on each load error and ends at the URL the clipper actually
saved. Nothing else in the file is site-aware.

**3. Check it** — `node Templates/Scripts/remote-video/test.js`

93 assertions covering both engines, all three built-in sites, and the malformed-metadata
cases. Add a case next to `[16] Site rules` for whatever you added.

### Sites handled today

| Site | Trigger | Rule |
|---|---|---|
| Dribbble | `dribbble.com` + subdomains | drop the `?resize=…` query for the unscaled original |
| Pinterest | `pinterest.*` + subdomains, `pin.it` | rewrite `/236x/` → `/originals/` |
| 21st.dev | `21st.dev` + subdomains | none needed; assets are served full size |
| anything else | manual pick, or `schema:@VideoObject` | generic selectors + meta/schema fallbacks |

### Known limitation

Pinterest and Dribbble often expose no stable direct MP4 — signed/expiring CDN links,
blob URLs, HLS playlists, JS-generated sources or embed players. The renderer detects and
explains each of those cases rather than failing silently, but it cannot play them: no
video downloading, and no bundled HLS player, are part of this workflow by design.

The clipper also only sees the DOM **as it stands when you click clip**. Media that loads
after a scroll or a click may not be in the page yet — so on Pinterest, open the pin's
closeup view first. Either way the clip keeps the title, image, platform, source URL,
tags and your notes, which is the point of saving it.
