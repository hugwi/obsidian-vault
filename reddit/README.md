# Reddit saved posts → Clippings

Pulls your saved Reddit posts into `Clippings/` as one note per post, with the
full comment tree, using the vault's normal frontmatter conventions. Re-running
is cheap: posts already synced are skipped, so this is safe on a schedule.

Python 3.9+ standard library only — nothing to `pip install`.

Three ways to run it. **Two of them need no Reddit app at all** — which
matters, because app creation is now gated behind Reddit's
[Responsible Builder Policy](https://support.reddithelp.com/hc/en-us/articles/42728983564564-Responsible-Builder-Policy).

| | Feed (`--from-feed`) | Export (`--from-export`) | API (default) |
|---|---|---|---|
| Reddit app | **none** | **none** | required + policy review |
| Credentials | private feed url | **none** | id/secret/password |
| History reachable | ~100 most recent | **everything** | ~1000 most recent |
| Runs unattended | **yes** | no | yes |
| Speed | ~1 post/3sec | ~1 post/3sec | ~1 post/sec |

**Recommended setup, no app required:** export mode once to backfill your
whole history, then feed mode on a schedule to catch new saves.

## Feed mode — no app, and it can be scheduled

1. Open <https://old.reddit.com/prefs/feeds/> and copy the **RSS** link on the
   *saved* row. It contains a private token — treat it like a password.
2. Put it in `.env` as `REDDIT_SAVED_FEED=...` (gitignored).
3. Run:

```bash
./sync.py --from-feed --dry-run
./sync.py --from-feed
```

The feed carries roughly your 100 most recent saves, which is plenty for a
daily job. Pair it with one export-mode backfill for everything older.

## Export mode — no app, complete history

1. Request your data at <https://www.reddit.com/settings/data-request>
   (choose GDPR or CCPA; the archive arrives by email, usually within a day).
2. Unzip it and find `saved_posts.csv`.
3. Run:

```bash
./sync.py --from-export ~/Downloads/export/saved_posts.csv --dry-run --limit 5
./sync.py --from-export ~/Downloads/export/saved_posts.csv
```

This reads Reddit's public JSON endpoints, which need no authentication. It
is deliberately slow — unauthenticated requests are rate limited hard, so it
waits 3 seconds between posts (`--interval` to change, at your own risk).
2000 saved posts is about 100 minutes. Leave it running.

It also accepts a plain file of thread URLs, one per line, if you would
rather hand-pick.

## API mode setup — only if you can get an app

> Reddit now routes app creation through the **Responsible Builder Policy**,
> and steers developers toward **Devvit**, which builds apps that run *on*
> Reddit and cannot issue script credentials. If you land on the policy page
> and cannot get past it, use feed + export mode above — together they do
> everything API mode does, and they need no app.

**1. Create a Reddit app** at <https://www.reddit.com/prefs/apps> →
*create another app…* (or <https://old.reddit.com/prefs/apps/>)

- type: **script**
- redirect uri: `http://localhost:8080`

The client id is the string shown under the app name; the secret is labelled
*secret*.

**2. Fill in credentials**

```bash
cd /path/to/vault/reddit
cp .env.example .env
$EDITOR .env
chmod 600 .env
```

`.env` is gitignored — the vault auto-commits, so keep credentials only there.

**If 2FA is enabled** on your Reddit account, password login cannot work
unattended. Run `./sync.py --get-refresh-token` once, follow the prompts, put
the resulting `REDDIT_REFRESH_TOKEN` in `.env`, and remove `REDDIT_PASSWORD`.

**3. Try it**

```bash
./sync.py --dry-run --limit 5   # writes nothing, shows what it would do
./sync.py --limit 5             # write 5 notes for real
./sync.py                       # full sync
```

The first full run takes a while: each post costs at least one request for the
post plus one or more for comments, deliberately throttled to ~60 requests/min
to stay under Reddit's limit. A few hundred saved posts means roughly 10–30
minutes. Later runs only touch new saves.

## Scheduling

### launchd (macOS, recommended)

```bash
# edit the file first: replace both VAULT_PATH occurrences with your real path
cp com.obsidian.reddit-sync.plist ~/Library/LaunchAgents/
launchctl load ~/Library/LaunchAgents/com.obsidian.reddit-sync.plist
launchctl start com.obsidian.reddit-sync   # run once now to verify
```

Runs daily at 07:30. Output goes to `sync.log` in this folder.

To remove it:
`launchctl unload ~/Library/LaunchAgents/com.obsidian.reddit-sync.plist`

### cron (Linux, or if you prefer it)

```cron
30 7 * * * /bin/bash /path/to/vault/reddit/run.sh
```

`run.sh` handles the working directory, appends to `sync.log`, and trims that
log at 2000 lines. It passes its arguments straight through to `sync.py`, so
for a no-app scheduled sync use:

```cron
30 7 * * * /bin/bash /path/to/vault/reddit/run.sh --from-feed
```

The launchd plist does the same — see the `--from-feed` argument in it.

## What a note looks like

```yaml
---
categories:
  - "[[Clippings]]"
source: "https://www.reddit.com/r/ClaudeAI/comments/abc123/..."
author: "u/someone"
published: 2026-07-14
created: 2026-08-03
rating:
action:
description: "First ~200 characters of the post body…"
type: discussion
platform: reddit
subreddit: "r/ClaudeAI"
score: 412
reddit_id: "t3_abc123"
tags:
  - "clippings"
  - "reddit"
---
```

Then the post body (or the outbound link, for link posts) and the comment
tree, with replies nested as blockquotes up to 6 levels deep.

`rating:` and `action:` are left blank on purpose — they are your triage
fields, so `Clippings.base` surfaces new imports as untriaged.

Notes match the vault conventions in `CLAUDE.md`:

- `title:` is omitted when the filename already is the full title, and only
  written when the title had to be truncated (filenames cap at 100 characters)
  or contained characters illegal in a filename.
- `author:` is plain text `u/name`, not a `[[wikilink]]` — hundreds of
  redditors would otherwise become unresolved links, and they are not People
  notes in `References/`.

## Options

| Flag | Effect |
|---|---|
| `--dry-run` | Report what would change, write nothing |
| `--limit N` | Only the N most recently saved posts |
| `--update` | Rewrite notes for posts already synced (refreshes scores/comments) |
| `--no-comments` | Post body only, much faster |
| `--max-more N` | Cap extra requests per post for expanding collapsed comment branches (default 20) |
| `--from-export CSV` | Backfill from a data-export `saved_posts.csv` — no app or credentials needed |
| `--from-feed [URL]` | Sync from the private saved-posts RSS feed — no app, schedulable. Omit the url to use `REDDIT_SAVED_FEED` |
| `--interval S` | Seconds between requests in feed/export mode (default 3.0) |
| `--out DIR` | Write somewhere other than `Clippings/` |
| `--verbose` | Log skips and token activity |

## Tests

```bash
./tests/run.sh
```

123 assertions, no credentials or network required — `tests/test_http.py`
serves a fake Reddit on localhost and drives the real HTTP stack against it
(OAuth grants, headers, throttle, 429 backoff, mid-run token expiry,
pagination), and `test_export.py` does the same for the unauthenticated
export and feed paths. Takes about 30 seconds, most of it the deliberate throttle and
backoff waits. Worth running after any edit to `sync.py`.

## Known limits

- **~1000 saved items in API mode.** Reddit's listing API exposes only
  roughly your 1000 most recent saved items. Use `--from-export` for the rest;
  the data export has every permalink and export mode has no cap.
- **Saved comments are skipped.** The listing is filtered to link posts
  (`type=links`). Saved *comments* are not imported.
- **Very large threads.** `--max-more` caps how hard the script works to
  expand "load more comments" branches. When it runs out it says so in the log
  rather than silently dropping them; raise the cap for those posts.
- **Deleted/removed content** appears as `[deleted]` / `_[removed]_`, which is
  all the API returns.
- **The feed window is ~100 posts.** Fine for a daily job. If the machine is
  off for weeks and you save heavily, older items can fall out the back —
  re-run an export backfill occasionally as a safety net.
- Unsaving a post on Reddit does not delete the note here — imports are
  one-way by design.

## Notes for future edits

- **Credentials must never be committed.** The vault auto-commits ("vault
  backup" commits), so `.gitignore` covers `reddit/.env`, `reddit/*.log` and
  `reddit/__pycache__/`. The RSS feed url is a live credential too — anyone
  holding it can read your saved posts. Reset it at
  <https://old.reddit.com/prefs/feeds/> if it leaks.
- **This folder is hidden from Obsidian** by `"userIgnoreFilters": ["reddit/"]`
  in `.obsidian/app.json`. Without it, this README and any other `.md` here
  get indexed as vault notes and show up in `Vault.base` with no frontmatter.
  Obsidian rewrites `app.json` on some settings changes, so if these docs
  reappear as notes, that filter was dropped.
- **Don't move this into `Templates/Scripts/`.** That folder is for `dv.view()`
  JavaScript, which has to live in an *indexed* folder — the opposite
  requirement to this one.
- **`Templates/Web Clipper/reddit-summary.json` is unrelated** to this script
  and untouched by it. Worth knowing it is now inconsistent with `CLAUDE.md`:
  it still writes to `Inbox/Articles` with `title:`/`status:`/
  `tags: clip/discussion`, predating the flat property-driven restructure.
  Fixing it is a separate job.
- **Two deliberate deviations** from the other 443 clippings, both reversible
  in `render_note()`: `title:` is written only when the filename had to be
  truncated or sanitized (per `CLAUDE.md`'s "no redundant title"), and
  `author:` is plain `u/name` rather than a `[[wikilink]]`, to avoid hundreds
  of unresolved links for people who are not `References/` notes.
