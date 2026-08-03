#!/usr/bin/env python3
"""Sync saved Reddit posts into the vault as Clippings notes.

Reads your Reddit saved listing over the OAuth API, fetches each post's full
comment tree, and writes one markdown note per post into Clippings/ using the
vault's frontmatter conventions. Already-synced posts are skipped, so the
script is safe to run on a schedule.

Standard library only — no pip install needed.

    ./sync.py                      # sync new saved posts
    ./sync.py --dry-run            # show what would be written, write nothing
    ./sync.py --limit 20           # only the 20 most recently saved
    ./sync.py --update             # also rewrite notes that already exist
    ./sync.py --get-refresh-token  # one-time helper for 2FA accounts

Credentials come from .env next to this file (see .env.example); real
environment variables win over .env.
"""

from __future__ import annotations

import argparse
import base64
import csv
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
VAULT_DIR = SCRIPT_DIR.parent
CLIPPINGS_DIR = VAULT_DIR / "Clippings"

OAUTH_BASE = "https://oauth.reddit.com"
WWW_BASE = "https://www.reddit.com"
USER_AGENT = "obsidian-vault-reddit-sync/1.0"

# Reddit allows 100 requests/minute for OAuth clients. Stay well under it: a
# scheduled job has no deadline, and a 429 costs more than the wait does.
MIN_REQUEST_INTERVAL = 1.0

# Unauthenticated requests to www.reddit.com are rate limited far more
# aggressively than OAuth ones, so --from-export backs right off.
ANON_REQUEST_INTERVAL = 3.0

MAX_RETRIES = 5

# Filenames are the note title in this vault, so keep them readable. Reddit
# titles run to 300 characters; anything past this gets truncated and the full
# text is preserved in a `title:` property instead.
MAX_FILENAME_LEN = 100


def log(msg: str) -> None:
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {msg}", flush=True)


def die(msg: str) -> None:
    print(f"error: {msg}", file=sys.stderr)
    raise SystemExit(1)


# --------------------------------------------------------------------------
# config
# --------------------------------------------------------------------------


def load_config() -> dict[str, str]:
    """Merge .env next to this script with the real environment."""
    cfg: dict[str, str] = {}
    env_file = SCRIPT_DIR / ".env"
    if env_file.exists():
        for raw in env_file.read_text(encoding="utf-8").splitlines():
            line = raw.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            value = value.strip()
            if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
                value = value[1:-1]
            cfg[key.strip()] = value
    for key in (
        "REDDIT_CLIENT_ID",
        "REDDIT_CLIENT_SECRET",
        "REDDIT_USERNAME",
        "REDDIT_PASSWORD",
        "REDDIT_REFRESH_TOKEN",
    ):
        if os.environ.get(key):
            cfg[key] = os.environ[key]
    return cfg


# --------------------------------------------------------------------------
# http
# --------------------------------------------------------------------------


class Reddit:
    """Thin OAuth client: token handling, rate limiting, retries."""

    def __init__(self, cfg: dict[str, str], verbose: bool = False):
        self.client_id = cfg.get("REDDIT_CLIENT_ID", "")
        self.client_secret = cfg.get("REDDIT_CLIENT_SECRET", "")
        self.username = cfg.get("REDDIT_USERNAME", "")
        self.password = cfg.get("REDDIT_PASSWORD", "")
        self.refresh_token = cfg.get("REDDIT_REFRESH_TOKEN", "")
        self.verbose = verbose

        if not self.client_id or not self.client_secret:
            die("REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET are required (see .env.example)")
        if not self.refresh_token and not (self.username and self.password):
            die(
                "set either REDDIT_REFRESH_TOKEN, or REDDIT_USERNAME + REDDIT_PASSWORD "
                "(see .env.example)"
            )

        self._token = ""
        self._token_expires_at = 0.0
        self._last_request = 0.0
        self.base = OAUTH_BASE
        self.min_interval = MIN_REQUEST_INTERVAL
        self.user_agent = f"{USER_AGENT} by u/{self.username or 'unknown'}"

    # -- auth ------------------------------------------------------------

    def _basic_auth(self) -> str:
        raw = f"{self.client_id}:{self.client_secret}".encode()
        return "Basic " + base64.b64encode(raw).decode()

    def _fetch_token(self) -> None:
        if self.refresh_token:
            payload = {"grant_type": "refresh_token", "refresh_token": self.refresh_token}
        else:
            payload = {
                "grant_type": "password",
                "username": self.username,
                "password": self.password,
            }
        data = urllib.parse.urlencode(payload).encode()
        req = urllib.request.Request(
            f"{WWW_BASE}/api/v1/access_token",
            data=data,
            headers={"Authorization": self._basic_auth(), "User-Agent": self.user_agent},
        )
        try:
            with urllib.request.urlopen(req, timeout=30) as resp:
                body = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            detail = exc.read().decode("utf-8", "replace")[:300]
            if exc.code == 401:
                die(
                    "reddit rejected the credentials (401). Check client id/secret, and "
                    "that the app at reddit.com/prefs/apps is of type 'script'.\n"
                    f"  reddit said: {detail}"
                )
            die(f"token request failed ({exc.code}): {detail}")
        except urllib.error.URLError as exc:
            die(f"could not reach reddit: {exc.reason}")

        if "access_token" not in body:
            hint = ""
            if body.get("error") == "invalid_grant":
                hint = (
                    "\n  invalid_grant usually means a wrong password, or 2FA is enabled on "
                    "the account.\n  For 2FA, run: ./sync.py --get-refresh-token"
                )
            die(f"no access_token in reddit's response: {body}{hint}")

        self._token = body["access_token"]
        self._token_expires_at = time.time() + float(body.get("expires_in", 3600)) - 120
        if self.verbose:
            log("obtained access token")

    def _ensure_token(self) -> None:
        if not self._token or time.time() >= self._token_expires_at:
            self._fetch_token()

    # -- requests --------------------------------------------------------

    def _throttle(self) -> None:
        delta = time.time() - self._last_request
        if delta < self.min_interval:
            time.sleep(self.min_interval - delta)
        self._last_request = time.time()

    def _prepare_path(self, path: str) -> str:
        """Hook for subclasses that address endpoints differently."""
        return path

    def _headers(self) -> dict:
        return {"Authorization": f"Bearer {self._token}", "User-Agent": self.user_agent}

    def request(self, path: str, params: dict | None = None, post_data: dict | None = None):
        """Call a Reddit endpoint and return parsed JSON."""
        self._ensure_token()
        url = f"{self.base}{self._prepare_path(path)}"
        if params:
            url += "?" + urllib.parse.urlencode(params)

        for attempt in range(MAX_RETRIES):
            self._throttle()
            body = urllib.parse.urlencode(post_data).encode() if post_data else None
            req = urllib.request.Request(url, data=body, headers=self._headers())
            try:
                with urllib.request.urlopen(req, timeout=60) as resp:
                    remaining = resp.headers.get("X-Ratelimit-Remaining")
                    reset = resp.headers.get("X-Ratelimit-Reset")
                    if remaining is not None and reset is not None:
                        try:
                            if float(remaining) < 5:
                                wait = float(reset) + 1
                                log(f"rate limit nearly spent, sleeping {wait:.0f}s")
                                time.sleep(wait)
                        except ValueError:
                            pass
                    return json.loads(resp.read().decode("utf-8"))
            except urllib.error.HTTPError as exc:
                if exc.code == 401 and attempt == 0:
                    # Token went stale mid-run; get a fresh one and retry once.
                    self._token = ""
                    self._ensure_token()
                    continue
                if exc.code in (429, 500, 502, 503, 504):
                    wait = 2 ** (attempt + 1)
                    log(f"http {exc.code} on {path}, retrying in {wait}s")
                    time.sleep(wait)
                    continue
                detail = exc.read().decode("utf-8", "replace")[:200]
                raise RuntimeError(f"http {exc.code} on {path}: {detail}") from exc
            except (urllib.error.URLError, TimeoutError) as exc:
                wait = 2 ** (attempt + 1)
                log(f"network error on {path} ({exc}), retrying in {wait}s")
                time.sleep(wait)

        raise RuntimeError(f"giving up on {path} after {MAX_RETRIES} attempts")

    # -- endpoints -------------------------------------------------------

    def whoami(self) -> str:
        return self.request("/api/v1/me").get("name", "")

    def saved_posts(self, limit: int | None = None):
        """Yield saved link posts, newest save first.

        Reddit's listing API exposes only about the most recent 1000 saved
        items; anything older is not reachable this way. Saved *comments* are
        excluded by type=links.
        """
        after = None
        seen = 0
        while True:
            params = {"limit": 100, "type": "links", "raw_json": 1}
            if after:
                params["after"] = after
            data = self.request(f"/user/{self.username}/saved", params).get("data", {})
            children = data.get("children", [])
            if not children:
                return
            for child in children:
                if child.get("kind") != "t3":
                    continue
                yield child["data"]
                seen += 1
                if limit and seen >= limit:
                    return
            after = data.get("after")
            if not after:
                return

    def comments(self, post_id: str, max_more: int) -> list[dict]:
        """Fetch a post's comments, expanding collapsed 'more' nodes."""
        return self.thread(post_id, max_more)[1]

    def thread(self, post_id: str, max_more: int) -> tuple[dict | None, list[dict]]:
        """Fetch a post and its comments in one request.

        Returns (post, comments). The post is None only if Reddit returned a
        thread with no post in it — deleted, or an id that does not exist.
        """
        listing = self.request(
            f"/comments/{post_id}",
            {"limit": 500, "depth": 100, "sort": "top", "raw_json": 1},
        )
        post = None
        try:
            post = listing[0]["data"]["children"][0]["data"]
        except (IndexError, KeyError, TypeError):
            pass

        flat: dict[str, dict] = {}
        pending: list[dict] = []
        for part in listing[1:]:
            _walk_listing(part, flat, pending)

        link_fullname = f"t3_{post_id}"
        requests_used = 0
        while pending and requests_used < max_more:
            more = pending.pop(0)
            children = more.get("children") or []
            if not children:
                # "continue this thread" — the subtree hangs off a parent
                # comment rather than being addressable by child ids.
                parent = more.get("parent_id", "")
                if not parent.startswith("t1_"):
                    continue
                requests_used += 1
                try:
                    sub = self.request(
                        f"/comments/{post_id}/_/{parent[3:]}",
                        {"limit": 500, "depth": 100, "sort": "top", "raw_json": 1},
                    )
                except RuntimeError as exc:
                    log(f"  could not expand thread {parent}: {exc}")
                    continue
                for part in sub[1:]:
                    _walk_listing(part, flat, pending)
                continue

            for batch_start in range(0, len(children), 100):
                if requests_used >= max_more:
                    break
                batch = children[batch_start : batch_start + 100]
                requests_used += 1
                try:
                    resp = self.request(
                        "/api/morechildren",
                        post_data={
                            "api_type": "json",
                            "link_id": link_fullname,
                            "children": ",".join(batch),
                            "sort": "top",
                            "limit_children": "false",
                            "raw_json": "1",
                        },
                    )
                except RuntimeError as exc:
                    log(f"  could not expand {len(batch)} comments: {exc}")
                    continue
                for thing in resp.get("json", {}).get("data", {}).get("things", []):
                    _collect_thing(thing, flat, pending)

        if pending:
            log(f"  note: {len(pending)} collapsed branch(es) left unexpanded (--max-more)")
        return post, list(flat.values())


class AnonReddit(Reddit):
    """Unauthenticated client for Reddit's public JSON endpoints.

    Used by --from-export. Reading a data-export CSV needs no Reddit app and
    no credentials at all, and it is not subject to the ~1000-item cap on the
    saved listing. The tradeoff is a much stricter rate limit, so it crawls.
    """

    def __init__(self, verbose: bool = False, interval: float = ANON_REQUEST_INTERVAL):
        self.verbose = verbose
        self.username = ""
        self.base = WWW_BASE
        self.min_interval = interval
        self._token = ""
        self._token_expires_at = float("inf")
        self._last_request = 0.0
        self.user_agent = f"{USER_AGENT} (export backfill)"

    def _ensure_token(self) -> None:
        """No auth to obtain — these endpoints are public."""

    def _headers(self) -> dict:
        return {"User-Agent": self.user_agent}

    def _prepare_path(self, path: str) -> str:
        # www.reddit.com serves JSON only when the path asks for it.
        if path.startswith("/comments/") and not path.endswith(".json"):
            return path + ".json"
        return path


def _walk_listing(node, flat: dict[str, dict], pending: list[dict]) -> None:
    """Flatten a nested comment Listing into flat{id: comment} + more nodes."""
    if not isinstance(node, dict):
        return
    if node.get("kind") == "Listing":
        for child in node.get("data", {}).get("children", []):
            _collect_thing(child, flat, pending)


def _collect_thing(thing, flat: dict[str, dict], pending: list[dict]) -> None:
    if not isinstance(thing, dict):
        return
    kind = thing.get("kind")
    data = thing.get("data", {})
    if kind == "more":
        pending.append(data)
        return
    if kind != "t1":
        return
    cid = data.get("id")
    if not cid or cid in flat:
        return
    flat[cid] = data
    replies = data.get("replies")
    if isinstance(replies, dict):
        _walk_listing(replies, flat, pending)


# --------------------------------------------------------------------------
# note rendering
# --------------------------------------------------------------------------


def yaml_str(value) -> str:
    """Quote a scalar for YAML frontmatter."""
    text = "" if value is None else str(value)
    text = text.replace("\\", "\\\\").replace('"', '\\"')
    text = text.replace("\n", " ").replace("\r", " ")
    return f'"{text}"'


def sanitize_filename(title: str) -> str:
    """Turn a post title into a filename that is safe on macOS/Windows/Linux."""
    name = unicodedata.normalize("NFC", title)
    name = re.sub(r'[\\/:*?"<>|#^\[\]]', " ", name)
    name = "".join(ch for ch in name if ch.isprintable())
    name = re.sub(r"\s+", " ", name).strip()
    name = name.lstrip(".")
    if len(name) > MAX_FILENAME_LEN:
        cut = name[:MAX_FILENAME_LEN]
        # Prefer a word boundary, but not one that throws away half the title.
        if " " in cut[MAX_FILENAME_LEN // 2 :]:
            cut = cut.rsplit(" ", 1)[0]
        name = cut.rstrip(" .,;:-")
    name = name.rstrip(" .")
    return name or "reddit-post"


def utc_date(epoch) -> str:
    try:
        return datetime.fromtimestamp(float(epoch), tz=timezone.utc).strftime("%Y-%m-%d")
    except (TypeError, ValueError):
        return ""


def build_description(post: dict) -> str:
    text = (post.get("selftext") or "").strip()
    if not text:
        # Link posts carry no body; fall back to the destination domain.
        domain = post.get("domain") or ""
        return f"Link post to {domain}" if domain else ""
    text = re.sub(r"\s+", " ", text)
    if len(text) > 200:
        text = text[:200].rsplit(" ", 1)[0] + "…"
    return text


def render_comment_tree(comments: list[dict]) -> str:
    """Render comments as nested blockquotes, deepest replies indented."""
    if not comments:
        return "_No comments._\n"

    by_parent: dict[str, list[dict]] = {}
    for c in comments:
        by_parent.setdefault(c.get("parent_id", ""), []).append(c)
    for siblings in by_parent.values():
        siblings.sort(key=lambda c: (-(c.get("score") or 0), c.get("created_utc") or 0))

    known = {c["id"] for c in comments}
    # Top-level comments hang off the post; treat any comment whose parent we
    # never fetched as top-level too, so nothing silently disappears.
    roots = [c for c in comments if not (c.get("parent_id", "")[3:] in known)]
    roots.sort(key=lambda c: (-(c.get("score") or 0), c.get("created_utc") or 0))

    lines: list[str] = []

    def emit(comment: dict, depth: int) -> None:
        author = comment.get("author") or "[deleted]"
        score = comment.get("score")
        score_txt = f" · {score} points" if isinstance(score, int) else ""
        date = utc_date(comment.get("created_utc"))
        date_txt = f" · {date}" if date else ""
        body = (comment.get("body") or "").strip() or "_[removed]_"

        # Blockquote nesting past ~6 levels stops being readable; deeper
        # replies keep the same indent and rely on the header for context.
        prefix = "> " * min(depth, 6)
        lines.append(f"{prefix}**u/{author}**{score_txt}{date_txt}")
        lines.append(prefix.rstrip() if prefix else "")
        for line in body.splitlines():
            lines.append(f"{prefix}{line}".rstrip())
        lines.append(prefix.rstrip() if prefix else "")

        for child in by_parent.get(f"t1_{comment['id']}", []):
            emit(child, depth + 1)

    for root in roots:
        emit(root, 0)
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def render_note(post: dict, comments: list[dict], filename_stem: str) -> str:
    title = (post.get("title") or "").strip()
    permalink = post.get("permalink") or ""
    url = f"{WWW_BASE}{permalink}" if permalink else (post.get("url") or "")
    subreddit = post.get("subreddit_name_prefixed") or f"r/{post.get('subreddit', '')}"
    author = post.get("author") or "[deleted]"

    fm = [
        "---",
        "categories:",
        '  - "[[Clippings]]"',
    ]
    # The filename is the title in this vault, so `title:` is only worth
    # carrying when sanitizing or truncating lost part of the original.
    if filename_stem != title:
        fm.append(f"title: {yaml_str(title)}")
    fm += [
        f"source: {yaml_str(url)}",
        f"author: {yaml_str('u/' + author)}",
        f"published: {utc_date(post.get('created_utc'))}",
        f"created: {datetime.now().strftime('%Y-%m-%d')}",
        "rating: ",
        "action: ",
        f"description: {yaml_str(build_description(post))}",
        "type: discussion",
        "platform: reddit",
        f"subreddit: {yaml_str(subreddit)}",
        f"score: {post.get('score', 0)}",
        f"reddit_id: {yaml_str(post.get('name') or 't3_' + str(post.get('id')))}",
        "tags:",
        '  - "clippings"',
        '  - "reddit"',
        "---",
        "",
    ]

    body = [f"# {title}", ""]
    meta = f"> Posted in **{subreddit}** by *u/{author}*"
    if isinstance(post.get("score"), int):
        meta += f" · {post['score']} points"
    if isinstance(post.get("num_comments"), int):
        meta += f" · {post['num_comments']} comments"
    body += [meta, "", f"[View on Reddit]({url})", ""]

    selftext = (post.get("selftext") or "").strip()
    if selftext:
        body += ["## Post", "", selftext, ""]
    elif post.get("url") and not (post.get("url") or "").startswith(WWW_BASE):
        body += ["## Link", "", f"<{post['url']}>", ""]

    body += ["## Comments", "", render_comment_tree(comments)]

    return "\n".join(fm) + "\n".join(body).rstrip() + "\n"


# --------------------------------------------------------------------------
# vault side
# --------------------------------------------------------------------------


def existing_reddit_ids(clippings: Path) -> dict[str, Path]:
    """Map reddit_id -> note path for everything already synced."""
    found: dict[str, Path] = {}
    if not clippings.is_dir():
        return found
    pattern = re.compile(r'^reddit_id:\s*"?([\w:]+)"?\s*$')
    for path in clippings.glob("*.md"):
        try:
            with path.open("r", encoding="utf-8") as fh:
                if fh.readline().rstrip("\n") != "---":
                    continue
                for _ in range(40):
                    line = fh.readline()
                    if not line or line.rstrip("\n") == "---":
                        break
                    match = pattern.match(line.rstrip("\n"))
                    if match:
                        found[match.group(1)] = path
                        break
        except OSError:
            continue
    return found


POST_ID_RE = re.compile(r"/comments/([a-z0-9]+)", re.I)


def read_export(path: Path) -> list[str]:
    """Extract post ids from a Reddit data-export saved_posts.csv.

    The export ships `id,permalink`, but be liberal: accept any column that
    holds an id or a thread URL, with or without a header row, so a hand-made
    list of permalinks works too.
    """
    if not path.exists():
        die(f"export file not found: {path}")

    ids: list[str] = []
    seen: set[str] = set()

    def add(value: str, bare_ok: bool = False) -> None:
        """Record a post id from a cell.

        `bare_ok` is only set for a column the header actually calls "id".
        Without it a bare word is rejected: plenty of ordinary text is short
        and lowercase, and silently treating it as an id would send the
        crawler after posts that do not exist.
        """
        value = (value or "").strip().strip('"')
        if not value:
            return
        match = POST_ID_RE.search(value)
        if match:
            pid = match.group(1)
        elif value.startswith("t3_"):
            pid = value[3:]
        elif bare_ok:
            pid = value
        else:
            return
        # Reddit ids are short base36; anything else is a stray column.
        if not re.fullmatch(r"[a-z0-9]{4,10}", pid, re.I):
            return
        if pid not in seen:
            seen.add(pid)
            ids.append(pid)

    with path.open(newline="", encoding="utf-8-sig", errors="replace") as fh:
        rows = list(csv.reader(fh))

    if not rows:
        die(f"export file is empty: {path}")

    header = [c.strip().lower() for c in rows[0]]
    has_header = "id" in header or "permalink" in header
    if has_header:
        want = [(i, c) for i, c in enumerate(header) if c in ("id", "permalink", "url")]
        for row in rows[1:]:
            before = len(ids)
            for i, col in want:
                if i < len(row) and row[i].strip():
                    add(row[i], bare_ok=(col == "id"))
                    if len(ids) > before:
                        break
    else:
        # No header to trust, so only accept unambiguous thread references.
        for row in rows:
            for cell in row:
                add(cell)

    if not ids:
        die(
            f"no post ids found in {path}.\n"
            "  Expected Reddit's saved_posts.csv (columns: id, permalink), or a "
            "file of thread URLs."
        )
    return ids


def unique_path(clippings: Path, stem: str, post_id: str) -> Path:
    """Pick a free filename, disambiguating collisions with the post id."""
    candidate = clippings / f"{stem}.md"
    if not candidate.exists():
        return candidate
    return clippings / f"{stem} ({post_id}).md"


# --------------------------------------------------------------------------
# refresh-token helper
# --------------------------------------------------------------------------


def get_refresh_token(cfg: dict[str, str]) -> None:
    """Walk through the code flow once, for accounts with 2FA enabled."""
    client_id = cfg.get("REDDIT_CLIENT_ID", "")
    client_secret = cfg.get("REDDIT_CLIENT_SECRET", "")
    if not client_id or not client_secret:
        die("REDDIT_CLIENT_ID and REDDIT_CLIENT_SECRET must be set first")

    redirect = "http://localhost:8080"
    state = base64.urlsafe_b64encode(os.urandom(9)).decode()
    params = urllib.parse.urlencode(
        {
            "client_id": client_id,
            "response_type": "code",
            "state": state,
            "redirect_uri": redirect,
            "duration": "permanent",
            "scope": "identity history read",
        }
    )
    print("\n1. Make sure your app's redirect uri at reddit.com/prefs/apps is exactly:")
    print(f"     {redirect}")
    print("\n2. Open this URL in a browser and click Allow:\n")
    print(f"   {WWW_BASE}/api/v1/authorize?{params}\n")
    print("3. You land on a localhost page that fails to load — that is fine.")
    print("   Copy the `code=` value out of the address bar (drop any trailing #_).\n")
    code = input("Paste the code here: ").strip()
    if not code:
        die("no code entered")

    data = urllib.parse.urlencode(
        {"grant_type": "authorization_code", "code": code, "redirect_uri": redirect}
    ).encode()
    auth = base64.b64encode(f"{client_id}:{client_secret}".encode()).decode()
    req = urllib.request.Request(
        f"{WWW_BASE}/api/v1/access_token",
        data=data,
        headers={"Authorization": f"Basic {auth}", "User-Agent": USER_AGENT},
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as exc:
        die(f"token exchange failed ({exc.code}): {exc.read().decode('utf-8', 'replace')[:300]}")

    token = body.get("refresh_token")
    if not token:
        die(f"no refresh_token returned (codes expire fast — try again): {body}")
    print("\nSuccess. Add this line to .reddit-sync/.env:\n")
    print(f"REDDIT_REFRESH_TOKEN={token}\n")
    print("You can then remove REDDIT_PASSWORD from .env.")


# --------------------------------------------------------------------------
# main
# --------------------------------------------------------------------------


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--limit", type=int, help="only process the N most recently saved posts")
    parser.add_argument("--dry-run", action="store_true", help="report what would change, write nothing")
    parser.add_argument("--update", action="store_true", help="rewrite notes for posts already synced")
    parser.add_argument("--no-comments", action="store_true", help="skip comment fetching")
    parser.add_argument(
        "--max-more",
        type=int,
        default=20,
        help="max extra requests per post to expand collapsed comment branches (default 20)",
    )
    parser.add_argument(
        "--from-export",
        type=Path,
        metavar="CSV",
        help="backfill from a Reddit data-export saved_posts.csv — needs no app "
        "and no credentials, and is not subject to the ~1000-item API cap",
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=ANON_REQUEST_INTERVAL,
        help=f"seconds between requests in --from-export mode (default {ANON_REQUEST_INTERVAL})",
    )
    parser.add_argument("--out", type=Path, default=CLIPPINGS_DIR, help="output folder")
    parser.add_argument("--verbose", action="store_true")
    parser.add_argument(
        "--get-refresh-token",
        action="store_true",
        help="one-time helper to obtain a refresh token (needed if 2FA is on)",
    )
    args = parser.parse_args()

    cfg = load_config()
    if args.get_refresh_token:
        get_refresh_token(cfg)
        return 0

    work_ids: list[str] = []
    if args.from_export:
        # No app, no credentials, no 1000-item cap — just the export plus
        # Reddit's public JSON endpoints.
        client = AnonReddit(verbose=args.verbose, interval=args.interval)
        work_ids = read_export(args.from_export)
        if args.limit:
            work_ids = work_ids[: args.limit]
        eta = len(work_ids) * args.interval / 60
        log(f"{len(work_ids)} post(s) in export — unauthenticated mode, ~{eta:.0f} min at best")
    else:
        client = Reddit(cfg, verbose=args.verbose)
        if not client.username:
            client.username = client.whoami()
            if not client.username:
                die("could not determine the reddit username; set REDDIT_USERNAME in .env")
            log(f"authenticated as u/{client.username}")

    clippings = args.out
    if not args.dry_run:
        clippings.mkdir(parents=True, exist_ok=True)

    known = existing_reddit_ids(clippings)
    log(f"{len(known)} reddit post(s) already in {clippings.name}/")

    counts = {"written": 0, "skipped": 0, "failed": 0}

    def emit(post: dict, comments: list[dict]) -> None:
        fullname = post.get("name") or f"t3_{post.get('id')}"
        stem = sanitize_filename((post.get("title") or "").strip() or "(untitled)")
        target = known.get(fullname) or unique_path(clippings, stem, post.get("id", ""))
        note = render_note(post, comments, target.stem)
        if args.dry_run:
            log(f"would write {target.name} ({len(comments)} comments)")
        else:
            target.write_text(note, encoding="utf-8")
            log(f"wrote {target.name} ({len(comments)} comments)")
        counts["written"] += 1

    if args.from_export:
        for post_id in work_ids:
            fullname = f"t3_{post_id}"
            if fullname in known and not args.update:
                counts["skipped"] += 1
                if args.verbose:
                    log(f"skip (already synced): {post_id}")
                continue
            try:
                post, comments = client.thread(
                    post_id, max_more=0 if args.no_comments else args.max_more
                )
                if post is None:
                    counts["failed"] += 1
                    log(f"FAILED {post_id}: no post in thread (deleted or bad id)")
                    continue
                emit(post, [] if args.no_comments else comments)
            except (RuntimeError, OSError) as exc:
                counts["failed"] += 1
                log(f"FAILED {post_id}: {exc}")
    else:
        for post in client.saved_posts(limit=args.limit):
            fullname = post.get("name") or f"t3_{post.get('id')}"
            title = (post.get("title") or "").strip() or "(untitled)"

            if fullname in known and not args.update:
                counts["skipped"] += 1
                if args.verbose:
                    log(f"skip (already synced): {title[:70]}")
                continue

            try:
                comments: list[dict] = []
                if not args.no_comments:
                    comments = client.comments(post["id"], max_more=args.max_more)
                emit(post, comments)
            except (RuntimeError, OSError) as exc:
                counts["failed"] += 1
                log(f"FAILED {title[:60]}: {exc}")

    written, skipped, failed = counts["written"], counts["skipped"], counts["failed"]
    verb = "would write" if args.dry_run else "wrote"
    log(f"done — {verb} {written}, skipped {skipped}, failed {failed}")
    return 1 if failed else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        print("\ninterrupted", file=sys.stderr)
        raise SystemExit(130)
