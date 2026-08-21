# Web Clipper Templates (with AI summary)

Templates for the **Obsidian Web Clipper** browser extension. The `*-summary.json` ones
clip the full content and put an AI **TL;DR + Key points** on top; `inspiration-media.json`
is a no-AI visual clipper.

## Files

| Template | Triggers on | Saves to |
|---|---|---|
| `inspiration-media.json` | 21st.dev, dribbble.com, pinterest.* (+ subdomains), pin.it | `Raw` |
| `youtube-summary.json` | youtube.com/watch, youtu.be | `Raw` |
| `medium-summary.json` | medium.com (+ subdomains) | `Raw` |
| `article-summary.json` | any page with `schema:@Article` / `@NewsArticle` | `Raw` |
| `reddit-summary.json` | reddit.com/r/ | `Raw` |
| `x-summary.json` | x.com, twitter.com | `Raw` |

All six save to `Raw/` and write the same triage frontmatter, so a clip is usable
from `Raw.base` the moment it lands: `categories: "[[Raw]]"` (the folder alone
means nothing in this vault — the property is what files it), `created`, `domain`,
`project`, `read: false`, `rating`, `action: review`. The five `*-summary.json` ones used
to save to `Inbox/Articles` / `Inbox/Videos` — folders that no longer exist — and set
`title`/`status: unread` instead, which left them invisible to every view.

### Template order in the extension

Web Clipper uses the **first** template whose trigger matches, in list order, and it does
not prefer a URL trigger over a schema one. So put URL-triggered templates above
schema-triggered ones, and keep the generic catch-all last:

| # | Template | Why here |
|---|---|---|
| 1–5 | `inspiration-media`, `youtube-summary`, `medium-summary`, `reddit-summary`, `x-summary` | all URL-triggered, mutually exclusive — order among them does not matter |
| 6 | `article-summary.json` | generic `schema:@Article` / `@NewsArticle` catch-all — **must be last**, or it claims design pages that happen to publish Article metadata |

`inspiration-media.json` is deliberately **URL-triggered only**. It briefly also triggered
on `schema:@VideoObject`, which the original brief asked for, but that matches any page
embedding video metadata — news sites, blogs, product pages, docs — so it fired almost
everywhere instead of on design sites. If you want it on a site with no trigger, pick
**Inspiration - Media** from the clipper's template dropdown, or add a trigger (see
*Adding another site*).

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
  other. Import at most one.

Their `CONTRIBUTING.md` also suggests pairing templates with a plugin that **downloads
images into the vault**. That is the opposite of what this workflow wants — remote URLs
only — so do not adopt that pattern here.

### Templater does not interfere

`Raw/` has a Templater folder template (`Templates/Raw Template.md`) and
`trigger_on_file_creation` is on, which looks like it would overwrite every clip. It does
not. Templater's creation handler measures the body length after the frontmatter and only
applies a folder template when that is **zero**; a file that arrives with a body instead
gets scanned for `<% %>` commands and is otherwise left alone. Every template here writes
a body (heading, summary blocks or `dataviewjs`, source link, notes sections), and none of
those bodies contain Templater syntax. The 378 Readwise notes already in `Raw/`
confirm the same behaviour in practice — none of them carry the folder template's markers.
This matters more now that all six templates land in `Raw/`, not just the visual one.

The one way to break this is to empty `noteContentFormat`. Keep a body in it.

> **Which browser you clip with does not affect playback.** The renderer runs inside
> Obsidian, not in your browser, so a clip made in Firefox behaves exactly like one made
> in Chrome. The Firefox and Chromium builds of the extension are the same extension, and
> `inspiration-media.json` uses no Interpreter/AI variables, so nothing here depends on
> browser-specific features.

## One-time setup

1. Install **Obsidian Web Clipper** (Chrome/Firefox/Safari extension).
2. Extension → **Settings → General** → set **Vault** to `obsidian-vault`.
3. **Settings → Interpreter** → enable it and add a model/API key
   (OpenAI, Anthropic, Ollama, etc.). **The AI summary only works with the
   Interpreter enabled** — without it the `TL;DR`/`Key points` blocks stay empty.
4. **Settings → Templates → Import** → import each `*.json` in this folder.

> **Editing a template here does nothing until you re-import it.** The extension keeps
> its own copy; these files are the source, not the live config.

## The `project` field

Every template carries an empty `project` property. The extension shows properties as
editable fields in the clip preview, so if you already know the clip belongs to a
project, type `[[Ethira]]` there before saving and it lands on that project's desk
straight away. Leave it empty and nothing happens — an empty value is ignored by the
desk and by every `.base` view. You can always attach it later with the **Attach note
to project** command (Cmd/Ctrl+P → "project"). See [[Project workflow]].

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

Saves web-design inspiration to `Raw/` as **metadata + remote URLs only**. No AI,
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
| `media_url_21st_video` | 21st.dev component iframe bundle rewritten to its paired immutable MP4 |
| `media_url_21st_preview` | current component's direct `cdn.21st.dev/.../preview.*` poster |
| `live_preview_url` | sandboxed 21st.dev component bundle, linked but never embedded |
| `demo_code_url` | public 21st.dev `code.demo.*.tsx` source URL |
| `media_url_image` | `src` of the page's media container (tight selectors, below) |
| `media_url_srcset` | `srcset` of the same container — the renderer picks the biggest entry |
| `media_url_image_meta` | `og:image:secure_url`, `twitter:image`, schema `ImageObject.contentUrl`, container `<video poster>` |
| `thumbnail_url` | `og:image` |
| `media_url_image_generic` | `figure img`, `article img`, `main img` — last resort only |

Most Dribbble and Pinterest posts are **stills, not video**, so the clipper grabs the
image out of the media container rather than only hunting for an MP4.

Images are captured at three confidence levels, and the renderer prefers them in this
order:

```
1. tight — the media container itself
   [data-test-id="pin-closeup-image"] img    ← Pinterest
   [data-test-id="closeup-image"] img
   [data-test-id="pin-image"] img
   .shot-media-container img                 ← Dribbble
   .media-shot img
   [data-testid="shot-media"] img
   [class*="shot-media"] img
   img[src^="https://cdn.21st.dev/"][src*="/preview."][alt="Default preview"]
                                                ← 21st.dev current component only

2. metadata — what the page says it is
   og:image · og:image:secure_url · twitter:image · schema ImageObject

3. generic — any image in figure / article / main
```

**Level 2 outranks level 3 deliberately.** A broad `article img` matches whatever comes
first in the DOM, which on a Dribbble shot page is often a shot from the related-shots
grid — a different designer's work. `og:image` always describes the page you clipped, so
it wins. The generic level exists only so an unknown site still yields something.

Every **video** selector is container-scoped for the same reason, and stops at
`figure video` rather than falling through to `article`/`main`: a video that far from the
container is almost always a recommendation.

21st.dev component pages are a separate shape: the visual runs inside a sandboxed
`bundle.*.html` iframe, while the page stores a paired immutable `video.*.mp4`,
`preview.*`, and `code.demo.*.tsx` under the same CDN path. The clipper derives those
URLs from the hydrated iframe. The renderer shows the preview first, attaches the MP4
only after **Load video**, and links the live bundle and demo source rather than executing
community code inside the note. Broad `[class*="component"]` selectors are intentionally
not used because they capture the related-components grid.

The 21st.dev homepage is different again: its main motion is a native
`/landing/codex-floral-sm.mp4` with a poster, alongside CSS/SVG animation that has no
standalone media URL. The template captures the video/poster and leaves CSS/SVG motion
as source-only context.

If every selector misses, `media_url_image_meta` and `thumbnail_url` still carry the
social-card image, which nearly every site publishes. For a site with no dedicated
trigger, pick **Inspiration - Media** manually from the clipper's template dropdown.

The note body calls the Dataview renderer:

```dataviewjs
await dv.view("Templates/Scripts/remote-media");
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

**2. Presentation** — `Templates/Scripts/remote-media/view.js`

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

**3. Check it** — `node Templates/Scripts/remote-media/test.js`

93 assertions covering both engines, all three built-in sites, and the malformed-metadata
cases. Add a case next to `[16] Site rules` for whatever you added.

### Sites handled today

| Site | Trigger | Rule |
|---|---|---|
| Dribbble | `dribbble.com` + subdomains | drop the `?resize=…` query for the unscaled original |
| Pinterest | `pinterest.*` + subdomains, `pin.it` | rewrite `/236x/` → `/originals/` |
| 21st.dev | `21st.dev` + subdomains | component poster + derived MP4/live bundle/demo source; homepage native video/poster |
| anything else | pick manually from the dropdown, or add a trigger | generic selectors + meta/schema fallbacks |

### Dribbble container, verified 2026-08-04

Probed on `dribbble.com/shots/27606181` from the browser console, because guessing here
had already produced two wrong-image bugs:

| Question | Answer |
|---|---|
| Does `#ssr-app` exist? | yes |
| Is it the whole app root? | **no** — no `nav`, no `header`, no `footer` inside it |
| Images inside it | 2 — the shot's own |
| Where the shot's images sit | directly under `#ssr-app` — both of them, and nothing else |
| The designer's "services" cards | `services-by-user__service-card`, **outside** `#ssr-app` |
| Actual shot uploads | `48556248` and lazy-loaded `48556247` |
| `og:image` | separate social-card upload `48556246`; not a shot gallery image |

The gallery cannot be reconstructed from page metadata: `og:image` is a separate social
card. `media_url_gallery` therefore captures only direct full-width content blocks under
`#ssr-app`; related shots are outside that container.

CDP identifies shot images as `img[data-test="v-img"]` and their stable links as
`a[data-photoswipe-image]`. Do not prefix these with `#ssr-app`: the hydrated browser DOM
has that wrapper, but Web Clipper's extraction snapshot does not. Description blocks use
`.formatted-text.content-block`.

#### Lazy-loaded images

A shot image below the fold is rendered with a placeholder, so `getAttribute("src")`
returns `""` for it while the real URL sits in `srcset` or `data-srcset`. The clipper stores
one entry per matched element (`shared.ts` → `extractContentBySelector`), so that empty
string still occupies its slot in the array — which is what makes the fix possible.

Three captures therefore read the same element set:

| Property | Attribute |
|---|---|
| `media_url_gallery` | `src` |
| `media_url_gallery_srcset` | `srcset` |
| `media_url_gallery_lazy` | `data-srcset` |
| `media_url_gallery_href` | `href` of Dribbble's `a[data-photoswipe-image]` |

The renderer resolves **each image from its own slot index**, taking the first capture
that has a URL there. It deliberately does not pick "whichever capture matched the most
images": on a lazy-loaded page the `src` and `data-srcset` captures can hold different
*half* of the set, so choosing one discards the other half. Nor does it concatenate them,
which would render one image's variants as separate pictures.

Some long Dribbble shots never materialise several `<img>` attributes even after a full
scroll. Their enclosing PhotoSwipe anchors still expose stable `href` values, so
`media_url_gallery_href` is the final positional fallback for those slots.

If images are still missing, run `Templates/Scripts/remote-media/probe-lazy.js` in the
browser console on the page. `missedBySelector` non-empty means the container selector
needs widening; a row in `images` with all three attributes empty means the page had not
materialised that image at all, and no selector can capture it — scroll the page first.

The note body captures the shot's text with

```
{{selectorHtml:#ssr-app|remove_html:("img,picture,source,video,svg,button,noscript,form")|markdown|trim}}
```

Images are stripped from that markdown deliberately — the renderer already shows them, and
embedding them twice would double every remote request.

**Scroll through the shot before clipping.** Dribbble lazy-loads images below the fold, and
the clipper only sees the DOM as it stands when you press clip. An image that has not
loaded yet has no usable `src` to capture.

### Known limitation

Pinterest and Dribbble often expose no stable direct MP4 — signed/expiring CDN links,
blob URLs, HLS playlists, JS-generated sources or embed players. The renderer detects and
explains each of those cases rather than failing silently, but it cannot play them: no
video downloading, and no bundled HLS player, are part of this workflow by design.

The clipper also only sees the DOM **as it stands when you click clip**. Media that loads
after a scroll or a click may not be in the page yet — so on Pinterest, open the pin's
closeup view first. Either way the clip keeps the title, image, platform, source URL,
tags and your notes, which is the point of saving it.
