"""Offline test: mock Reddit payloads through the real rendering + write path."""
import importlib.util, json, sys, tempfile, types
from pathlib import Path

SYNC_PATH = str(Path(__file__).resolve().parent.parent / "sync.py")
spec = importlib.util.spec_from_file_location("sync", SYNC_PATH)
sync = importlib.util.module_from_spec(spec)
spec.loader.exec_module(sync)

fails = []
def check(name, cond, extra=""):
    print(("  ok   " if cond else "  FAIL ") + name + (f"  {extra}" if extra and not cond else ""))
    if not cond:
        fails.append(name)

print("\n== sanitize_filename ==")
check("strips slashes", "/" not in sync.sanitize_filename('a/b:c*d?"e<f>g|h'))
check("no illegal chars", not set('\\/:*?"<>|#^[]') & set(sync.sanitize_filename('a/b:c*d?"e<f>g|h#^[x]')))
long = "word " * 60
check("truncates to <=100", len(sync.sanitize_filename(long)) <= 100, len(sync.sanitize_filename(long)))
check("keeps most of title when no late space", len(sync.sanitize_filename("x"*300)) == 100)
check("non-empty fallback", sync.sanitize_filename("///") == "reddit-post", repr(sync.sanitize_filename("///")))
check("no leading dot", not sync.sanitize_filename("...hidden").startswith("."))
check("unicode kept", sync.sanitize_filename("Åland — naïve") == "Åland — naïve", sync.sanitize_filename("Åland — naïve"))
check("no trailing space/dot", sync.sanitize_filename("trailing . ") == "trailing")

print("\n== yaml_str ==")
check("escapes quotes", sync.yaml_str('say "hi"') == '"say \\"hi\\""', sync.yaml_str('say "hi"'))
check("escapes backslash", sync.yaml_str('a\\b') == '"a\\\\b"', sync.yaml_str('a\\b'))
check("flattens newlines", "\n" not in sync.yaml_str("a\nb"))
check("handles None", sync.yaml_str(None) == '""')

print("\n== utc_date ==")
check("epoch -> date", sync.utc_date(1752451200) == "2025-07-14", sync.utc_date(1752451200))
check("bad input -> empty", sync.utc_date(None) == "")

print("\n== comment tree ==")
comments = [
    {"id": "c1", "parent_id": "t3_abc123", "author": "alice", "score": 50, "created_utc": 1752451200, "body": "Top comment.\n\nSecond para."},
    {"id": "c2", "parent_id": "t1_c1", "author": "bob", "score": 20, "created_utc": 1752451300, "body": "Reply to alice."},
    {"id": "c3", "parent_id": "t1_c2", "author": "carol", "score": 5, "created_utc": 1752451400, "body": "Nested deeper."},
    {"id": "c4", "parent_id": "t3_abc123", "author": "dave", "score": 99, "created_utc": 1752451500, "body": "Higher scored root."},
    {"id": "c5", "parent_id": "t1_missing", "author": "eve", "score": 1, "created_utc": 1752451600, "body": "Orphan whose parent was never fetched."},
    {"id": "c6", "parent_id": "t3_abc123", "author": None, "score": None, "created_utc": None, "body": ""},
]
tree = sync.render_comment_tree(comments)
print("\n".join("    | " + l for l in tree.splitlines()[:22]))
check("all 6 comments rendered", all(a in tree for a in ["alice","bob","carol","dave","eve"]) and "[deleted]" in tree)
check("higher score root first", tree.index("dave") < tree.index("alice"))
check("depth 1 quoted", "> **u/bob**" in tree)
check("depth 2 quoted twice", "> > **u/carol**" in tree)
check("orphan promoted to root", "\n**u/eve**" in tree or tree.startswith("**u/eve**"))
check("missing body -> removed marker", "_[removed]_" in tree)
check("no comments -> placeholder", "_No comments._" in sync.render_comment_tree([]))

print("\n== deep nesting cap ==")
deep = [{"id": f"d{i}", "parent_id": "t3_x" if i == 0 else f"t1_d{i-1}", "author": f"u{i}", "score": 1, "created_utc": 1752451200, "body": f"level {i}"} for i in range(10)]
dt = sync.render_comment_tree(deep)
import re as _re
maxdepth = max((len(_re.findall(r">", m.group(0))) for m in _re.finditer(r"^(?:> )+", dt, _re.M)), default=0)
check("caps at 6 levels", maxdepth == 6, f"maxdepth={maxdepth}")
check("deepest still present", "level 9" in dt)

print("\n== render_note ==")
post = {
    "id": "abc123", "name": "t3_abc123",
    "title": 'How I use Claude Code: "tips" & tricks/hacks',
    "permalink": "/r/ClaudeAI/comments/abc123/how_i_use/",
    "subreddit": "ClaudeAI", "subreddit_name_prefixed": "r/ClaudeAI",
    "author": "someone", "created_utc": 1752451200, "score": 412, "num_comments": 88,
    "selftext": "Here is the body of the post.\n\nWith **markdown** and a list:\n- one\n- two",
    "url": "https://www.reddit.com/r/ClaudeAI/comments/abc123/how_i_use/",
    "domain": "self.ClaudeAI",
}
stem = sync.sanitize_filename(post["title"])
note = sync.render_note(post, comments, stem)
print("\n".join("    | " + l for l in note.splitlines()[:20]))
check("frontmatter opens", note.startswith("---\ncategories:\n  - \"[[Clippings]]\"\n"))
check("title present (filename was sanitized)", "title:" in note.split("---")[1])
check("reddit_id present", 'reddit_id: "t3_abc123"' in note)
check("rating/action blank", "\nrating: \naction: \n" in note)
check("score numeric", "\nscore: 412\n" in note)
check("subreddit quoted", 'subreddit: "r/ClaudeAI"' in note)
check("author plain not wikilink", 'author: "u/someone"' in note and "[[u/someone" not in note)
check("published from post", "published: 2025-07-14" in note)
check("body has post section", "## Post" in note and "## Comments" in note)
check("ends with newline", note.endswith("\n"))

# title omitted when filename == title
plain = dict(post, title="A clean title")
n2 = sync.render_note(plain, [], "A clean title")
check("title omitted when redundant", "\ntitle:" not in n2)

# link post
linkpost = dict(post, selftext="", url="https://example.com/article", domain="example.com")
n3 = sync.render_note(linkpost, [], "x")
check("link post shows Link section", "## Link" in n3 and "<https://example.com/article>" in n3)
check("link post description falls back to domain", 'description: "Link post to example.com"' in n3)

print("\n== frontmatter YAML parses ==")
try:
    import yaml
    fm = yaml.safe_load(note.split("---\n")[1])
    check("valid YAML", isinstance(fm, dict), str(fm)[:200])
    check("categories is list", isinstance(fm.get("categories"), list) and fm["categories"] == ["[[Clippings]]"])
    check("title round-trips exactly", fm.get("title") == post["title"], repr(fm.get("title")))
    check("score is int", isinstance(fm.get("score"), int))
    check("published is date", str(fm.get("published")) == "2025-07-14")
    check("rating is None", fm.get("rating") is None and fm.get("action") is None)
except ImportError:
    print("  skip  pyyaml not installed")

print("\n== existing_reddit_ids + unique_path ==")
with tempfile.TemporaryDirectory() as td:
    d = Path(td)
    (d / "Existing.md").write_text(note, encoding="utf-8")
    (d / "NotReddit.md").write_text("---\ncategories:\n  - \"[[Clippings]]\"\n---\nbody\n", encoding="utf-8")
    (d / "NoFrontmatter.md").write_text("just text\n", encoding="utf-8")
    ids = sync.existing_reddit_ids(d)
    check("finds reddit_id", ids.get("t3_abc123") == d / "Existing.md", str(ids))
    check("ignores non-reddit notes", len(ids) == 1, str(ids))
    check("unique_path free name", sync.unique_path(d, "Brand New", "zzz").name == "Brand New.md")
    (d / "Taken.md").write_text("x", encoding="utf-8")
    check("unique_path collision", sync.unique_path(d, "Taken", "zzz").name == "Taken (zzz).md")

print("\n== end-to-end with mocked API ==")
with tempfile.TemporaryDirectory() as td:
    out = Path(td)
    calls = {"comments": 0}

    class FakeReddit:
        username = "tester"
        def saved_posts(self, limit=None):
            posts = [post, dict(post, id="def456", name="t3_def456", title="Second saved post")]
            return posts[:limit] if limit else posts
        def comments(self, pid, max_more):
            calls["comments"] += 1
            return comments

    sync.Reddit = lambda cfg, verbose=False: FakeReddit()
    sync.load_config = lambda: {"REDDIT_CLIENT_ID": "x", "REDDIT_CLIENT_SECRET": "y", "REDDIT_USERNAME": "tester", "REDDIT_PASSWORD": "z"}
    sys.argv = ["sync.py", "--out", str(out)]
    rc = sync.main()
    check("exit 0", rc == 0)
    files = sorted(p.name for p in out.glob("*.md"))
    print("    files:", files)
    check("2 notes written", len(files) == 2, str(files))
    check("comments fetched twice", calls["comments"] == 2)

    # second run must skip both
    calls["comments"] = 0
    rc = sync.main()
    check("rerun skips all", calls["comments"] == 0 and len(list(out.glob("*.md"))) == 2)

    # --update rewrites in place, no duplicate files
    sys.argv = ["sync.py", "--out", str(out), "--update"]
    rc = sync.main()
    check("--update reuses same files", len(list(out.glob("*.md"))) == 2 and calls["comments"] == 2)

    # dry-run writes nothing new
    with tempfile.TemporaryDirectory() as td2:
        sys.argv = ["sync.py", "--out", str(td2), "--dry-run"]
        sync.main()
        check("dry-run writes nothing", len(list(Path(td2).glob("*.md"))) == 0)

print("\n" + ("ALL PASS" if not fails else f"{len(fails)} FAILURES: {fails}"))
sys.exit(1 if fails else 0)
