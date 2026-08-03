# Handoff — Reddit saved posts → vault sync

**Branch:** `claude/reddit-articles-vault-sync-7l4hny` · **Commit:** see `git log` · **Date:** 2026-08-03
**Status:** code complete and tested; **the import has not been run yet**

---

## The ask

Pull all saved Reddit posts into the vault, and make it run recurrently.

## What was decided

| Question | Choice |
|---|---|
| How to reach Reddit | OAuth API, "script" app (works unattended) |
| Fallback added later | `--from-export` — no app, no credentials, no 1000-cap |
| Where the schedule runs | Locally, launchd/cron |
| Note contents | Post **plus the full comment tree** |

## What is done

`reddit/` — zero-dependency Python 3.9+, stdlib only:

| File | Purpose |
|---|---|
| `sync.py` | The sync tool (~700 lines) |
| `.env.example` | Credential template; real `.env` is gitignored |
| `run.sh` | Scheduled-run wrapper — logging + rotation at 2000 lines |
| `com.obsidian.reddit-sync.plist` | launchd job, daily 07:30 |
| `README.md` | Setup, scheduling, flags, limits |
| `tests/` | 123 assertions, `./tests/run.sh`, no network needed |

Behaviour: authenticates (password grant, or refresh-token grant if 2FA), pages
the saved listing filtered to link posts, fetches each post's comments and
expands collapsed `more` branches, renders a note into `Clippings/`. Throttled
to ~60 req/min with retry/backoff on 429 and 5xx. Dedupes on the `reddit_id`
frontmatter property, so reruns only fetch new saves.

Note shape follows `CLAUDE.md`: `categories: "[[Clippings]]"`, blank `rating:`
and `action:` so imports surface as untriaged in `Clippings.base`, plus
`platform: reddit`, `subreddit`, `score`, `reddit_id`. Body is the post text
(or outbound link) then comments, nested as blockquotes to 6 levels.

## Three ways to run it — two need no Reddit app

App creation now redirects to Reddit's Responsible Builder Policy, and Reddit
steers developers to **Devvit**, which builds apps that run *on* Reddit and
cannot issue script credentials. Assume API mode may simply be unavailable.

- **Feed mode** (`--from-feed`) — the private saved-posts RSS feed from
  <https://old.reddit.com/prefs/feeds/>. No app; the feed url carries its own
  token. Covers roughly the 100 most recent saves and **runs unattended**, so
  this is what the scheduled job uses.
- **Export mode** (`--from-export saved_posts.csv`) — no app, no credentials,
  complete history, no cap. Manual export, so not schedulable.
- **API mode** (default) — needs a script app. Kept because it is the fastest
  and has no ~100-item feed window, but it is now the least available.

**Recommended, no app at all:** one export-mode backfill for the full history,
then feed mode daily for new saves. The launchd plist passes `--from-feed`.

## What is NOT done — the one remaining step

**No saved posts have been imported.** The work was done in a cloud container
where Reddit is blocked by network policy (`CONNECT tunnel failed, 403` for
both `reddit.com` and `oauth.reddit.com`) and where the account credentials
are not available. The import must run wherever the vault lives:

```bash
cd /path/to/vault/reddit

# 1. full backfill — needs nothing but the data export
#    (request it at https://www.reddit.com/settings/data-request)
./sync.py --from-export ~/Downloads/export/saved_posts.csv --dry-run --limit 5
./sync.py --from-export ~/Downloads/export/saved_posts.csv

# 2. recurring — grab the saved RSS url from old.reddit.com/prefs/feeds/
cp .env.example .env && $EDITOR .env   # set REDDIT_SAVED_FEED
chmod 600 .env
./sync.py --from-feed
```

Export mode runs at 3s/post, so budget ~100 minutes per 2000 posts.

Then schedule it: edit both `VAULT_PATH` placeholders in the plist, copy to
`~/Library/LaunchAgents/`, `launchctl load`, and `launchctl start` once to
confirm. The plist already passes `--from-feed`. Cron alternative is in
`README.md`.

## Verification

123 assertions across four suites in `tests/`, all passing. No credentials or
network needed — run them with:

```bash
./tests/run.sh
```

- `test_render.py` — filename sanitization (illegal characters, truncation,
  unicode, collisions), YAML escaping round-tripped through a real parser,
  comment-tree nesting and score ordering, orphaned comments, the 6-level
  nesting cap, dedupe scanning, and an end-to-end run against a mocked client
  covering fresh sync, rerun-skips-existing, `--update`, and `--dry-run`.
- `test_api.py` — listing flattening, `more` expansion including "continue
  this thread", 100-item batching, `max_more` capping, saved-listing
  pagination and the `t1` filter.
- `test_export.py` — feed mode (Atom parsing, dedupe, `limit=100`, non-Reddit
  url rejected, empty feed and stale-token 403 exits, end-to-end run from
  `.env` and from an explicit url), plus CSV parsing (official export,
  permalink-only,
  headerless URL lists, BOM, duplicates, `t3_` prefixes, and three
  malformed-input exits), plus an end-to-end `--from-export` run against a
  fake `www.reddit.com` with **no credentials configured at all**, including a
  deleted post that must not abort the run.
- `test_http.py` — stands up a **fake Reddit on localhost** and drives
  `sync.py`'s real HTTP stack against it: OAuth password and refresh-token
  grants, Authorization/User-Agent headers, the request throttle, a served 429
  with backoff, mid-run token expiry and re-auth, pagination over the wire,
  and both credential-failure error messages.

**What remains unverified is Reddit itself** — its real payload shapes and
whether the account's saved listing behaves as documented. Everything on this
side of the socket is covered. If the first real run breaks, the likeliest
cause is auth, and `sync.py` prints a specific message for 401 and
`invalid_grant`.

## Open items

1. **The ~1000 cap applies to API mode only.** If the import count comes in
   below expectation, backfill with `--from-export` against
   `saved_posts.csv` from <https://www.reddit.com/settings/data-request>.
   Built and tested.
2. **Saved comments are skipped** — the listing is filtered to link posts.
3. **Two deliberate deviations** from the existing 443 clippings, either of
   which can be reverted in `render_note()`:
   - `title:` is written only when the filename had to be truncated (100 char
     cap) or sanitized, per `CLAUDE.md`'s "no redundant title" rule. Existing
     clippings all carry `title:`.
   - `author:` is plain text `u/name`, not a `[[wikilink]]` — hundreds of
     redditors would otherwise become unresolved links, and they are not
     People notes in `References/`.
4. **Unsaving on Reddit does not remove the note.** Import is one-way.

## Notes for whoever picks this up

- Credentials must never be committed. The vault auto-commits ("vault backup"
  commits), so `.gitignore` covers `reddit/.env`, `*.log`, and
  `__pycache__/`. Verified with `git check-ignore`.
- `reddit/` is a plain visible folder at the vault root, so Obsidian would
  normally index `README.md` and `HANDOFF.md` as notes and show them in
  `Vault.base` without frontmatter. `"userIgnoreFilters": ["reddit/"]` in
  `.obsidian/app.json` keeps it out of search, graph and the file explorer.
  If those docs ever reappear as notes, that setting was reset — Obsidian
  rewrites `app.json` on some settings changes.
- Do not move this into `Templates/Scripts/` — that folder is for `dv.view()`
  JavaScript, which must live in an *indexed* folder for the opposite reason.
- The pre-existing `Templates/Web Clipper/reddit-summary.json` clipper is
  unrelated and untouched, but note it still writes to `Inbox/Articles` with
  `title:`/`status:`/`tags: clip/discussion` — it predates the flat
  property-driven restructure and is now inconsistent with `CLAUDE.md`.
  Worth fixing separately.
