---
type: inspiration
title: Remote video fallback test
categories:
  - "[[Clippings]]"
domain: design
source_url: https://dribbble.com/shots/popular
platform: dribbble.com
thumbnail_url: 
media_url_image: 
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
await dv.view("Templates/Scripts/remote-media");
```

[Open original source](https://dribbble.com/shots/popular)

## Notes

- Nothing-at-all path: every media property is present but empty, so the renderer shows the
  message *"No direct video URL was exposed by this page."* and an **Open the original
  source** link. Nothing breaks.
- When a still *is* available the renderer shows it instead of this message — see
  [[Landing Page for Yoga Platform]].

## Why I saved this

- Verifies the note stays useful when a page exposes neither a playable video nor an image.
