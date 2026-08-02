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

### Known limitation

Pinterest and Dribbble often expose no stable direct MP4 — signed/expiring CDN links,
blob URLs, HLS playlists, JS-generated sources or embed players. The renderer detects and
explains each of those cases rather than failing silently, but it cannot play them: no
video downloading, and no bundled HLS player, are part of this workflow by design.

The clipper also only sees the DOM **as it stands when you click clip**. Media that loads
after a scroll or a click may not be in the page yet — so on Pinterest, open the pin's
closeup view first. Either way the clip keeps the title, image, platform, source URL,
tags and your notes, which is the point of saving it.
