# Web Clipper Templates (with AI summary)

Templates for the **Obsidian Web Clipper** browser extension. The `*-summary.json` ones
clip the full content and put an AI **TL;DR + Key points** on top; `inspiration-media.json`
is a no-AI visual clipper.

## Files

| Template | Triggers on | Saves to |
|---|---|---|
| `inspiration-media.json` | 21st.dev, dribbble.com, pinterest.com, pin.it, `schema:@VideoObject` | `Clippings` |
| `youtube-summary.json` | youtube.com/watch, youtu.be | `Clippings` |
| `medium-summary.json` | medium.com (+ subdomains) | `Inbox/Articles` |
| `article-summary.json` | any page with `schema:@Article` / `@NewsArticle` | `Inbox/Articles` |
| `reddit-summary.json` | reddit.com/r/ | `Inbox/Articles` |
| `x-summary.json` | x.com, twitter.com | `Inbox/Articles` |

> **Template order matters.** `inspiration-media.json` also triggers on
> `schema:@VideoObject`, which YouTube pages carry too. Keep `youtube-summary.json`
> **above** it in the extension's template list so YouTube still gets the transcript
> template — Web Clipper uses the first template whose trigger matches.

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
  The note is named `Title (VIDEO_ID)` and carries `type: video`, matching what
  `Templates/Scripts/youtube-archive/youtube_archive.py` writes — run that script with
  `--force` on the same URL to download the video and replace the clip with a full
  archive note (timestamped transcript, chapters, local player). See [[YouTube Archive]].
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
| `thumbnail_url` | `og:image` |

The note body calls the Dataview renderer:

```dataviewjs
await dv.view("Templates/Scripts/remote-video");
```

which shows the thumbnail plus a **Load video** button, and only attaches the remote
source once you press it. When no direct video URL was found it falls back to the
thumbnail plus an *Open the original source* link, so the clip stays useful either way.

**Requires DataviewJS.** Settings → Dataview → *Enable JavaScript Queries*. This vault
ships it pre-enabled via `.obsidian/plugins/dataview/data.json`.

Every clip starts with the tags `inspiration`, `web-design`, `ui`, `ux`; add finer ones
(`animation`, `navigation`, `mobile`, `landing-page`, `typography`, `dashboard`,
`interaction-design`) by hand. Browse the library at [[Inspiration]] / `Inspiration.base`.

### Known limitation

Pinterest and Dribbble often expose no stable direct MP4 — they use signed/expiring CDN
links, blob URLs, HLS playlists, JS-generated sources or embed players. A captured URL
may also work today and expire later. That is expected: the clip still keeps the title,
thumbnail, platform, source URL, tags and your notes. Automatic video downloading is
deliberately **not** part of this workflow.
