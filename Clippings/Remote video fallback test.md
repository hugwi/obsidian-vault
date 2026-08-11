---
type: inspiration
title: Remote video fallback test
categories:
  - "[[Clippings]]"
domain: design
source_url: https://dribbble.com/shots/popular
platform: dribbble.com
thumbnail_url: https://cdn.dribbble.com/assets/dribbble-ball-icon-4e54c54abecf8efe027abe6f8bc7794553b8abef3bdb49cf22984ecc3ed2ba00.svg
media_url_secure: 
media_url: 
media_url_twitter: 
media_url_schema: 
media_url_source: 
media_url_video: 
saved_at: 2026-08-02
created: 2026-08-02
source: web-clipper
rating: 
action: review
tags:
  - inspiration
  - web-design
  - ui
  - ux
---

# Remote video fallback test

```dataviewjs
await dv.view("Templates/Scripts/remote-video");
```

[Open original source](https://dribbble.com/shots/popular)

## Notes

- Fallback path: every `media_url*` property is present but empty, so the renderer shows the
  thumbnail, the message *"No direct video URL was exposed by this page."* and an
  **Open the original source** link. Nothing breaks.

## Why I saved this

- Verifies that a clip stays useful when the platform exposes no playable MP4 — the common
  case on Pinterest and Dribbble.
