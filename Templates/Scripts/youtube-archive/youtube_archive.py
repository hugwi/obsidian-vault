#!/usr/bin/env python3
"""Download YouTube videos into the vault and write a note with the transcript.

Runs on the machine that holds the vault (it needs yt-dlp + ffmpeg). Media lands in
`Attachments/Videos/` (git-ignored), the note lands in `Clippings/` with the vault's
frontmatter conventions: categories -> "[[Clippings]]", rating, action, ISO dates.

    ./youtube_archive.py https://www.youtube.com/watch?v=dQw4w9WgXcQ
    ./youtube_archive.py --cookies-from-browser chrome WL      # Watch Later
    ./youtube_archive.py --no-media LL                         # Liked, transcript only

See `YouTube Archive.md` in the vault root for the full workflow.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
from dataclasses import dataclass
from datetime import date
from pathlib import Path

# YouTube's own playlist aliases, usable as bare arguments.
PLAYLIST_ALIASES = {
    "WL": "https://www.youtube.com/playlist?list=WL",
    "LL": "https://www.youtube.com/playlist?list=LL",
}

MEDIA_SUBDIR = Path("Attachments") / "Videos"
NOTE_SUBDIR = Path("Clippings")

# Characters Obsidian cannot carry in a filename, plus the ones that break wikilinks.
UNSAFE_FILENAME = re.compile(r'[\\/:*?"<>|\[\]#^\x00-\x1f]')

SUBTITLE_EXTS = (".vtt",)

# A cue line is dropped once it has been emitted; a paragraph closes at either bound.
PARAGRAPH_SECONDS = 45
PARAGRAPH_CHARS = 550


# --------------------------------------------------------------------------- helpers


def die(message: str) -> "None":
    print(f"error: {message}", file=sys.stderr)
    raise SystemExit(1)


def safe_filename(value: str, limit: int = 80) -> str:
    cleaned = UNSAFE_FILENAME.sub("", value)
    cleaned = re.sub(r"\s+", " ", cleaned).strip(" .")

    if len(cleaned) > limit:
        cleaned = cleaned[:limit].rsplit(" ", 1)[0].strip()

    return cleaned or "Untitled"


def yaml_string(value: str) -> str:
    escaped = value.replace("\\", "\\\\").replace('"', '\\"')

    return f'"{escaped}"'


def format_duration(seconds: object) -> str:
    try:
        total = int(float(seconds))  # type: ignore[arg-type]
    except (TypeError, ValueError):
        return ""

    hours, rest = divmod(max(total, 0), 3600)
    minutes, secs = divmod(rest, 60)

    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"

    return f"{minutes}:{secs:02d}"


def format_timestamp(seconds: float) -> str:
    total = int(seconds)
    hours, rest = divmod(total, 3600)
    minutes, secs = divmod(rest, 60)

    if hours:
        return f"{hours}:{minutes:02d}:{secs:02d}"

    return f"{minutes:02d}:{secs:02d}"


def iso_date(value: object) -> str:
    """`20260214` (yt-dlp's upload_date) -> `2026-02-14`."""
    text = str(value or "")

    if re.fullmatch(r"\d{8}", text):
        return f"{text[:4]}-{text[4:6]}-{text[6:]}"

    return ""


def run(command: list[str], *, capture: bool = False) -> subprocess.CompletedProcess:
    return subprocess.run(
        command,
        check=True,
        text=True,
        stdout=subprocess.PIPE if capture else None,
    )


# ------------------------------------------------------------------------ vtt parsing

TIMESTAMP = re.compile(
    r"(?P<start>\d{1,2}:\d{2}:\d{2}[.,]\d{3})\s*-->\s*(?P<end>\d{1,2}:\d{2}:\d{2}[.,]\d{3})"
)

# Auto-captions carry per-word timing and colour spans; both are noise here.
INLINE_TAG = re.compile(r"<[^>]+>")


def parse_vtt_seconds(stamp: str) -> float:
    hours, minutes, seconds = stamp.replace(",", ".").split(":")

    return int(hours) * 3600 + int(minutes) * 60 + float(seconds)


@dataclass
class Cue:
    start: float
    lines: list[str]


def parse_vtt(text: str) -> list[Cue]:
    cues: list[Cue] = []
    current: Cue | None = None

    for raw in text.splitlines():
        line = raw.strip()
        match = TIMESTAMP.search(line)

        if match:
            # A bare number just before a timestamp is a cue identifier, not speech
            # (VTT converted from SRT keeps them), and it landed in the previous cue.
            if current and current.lines and current.lines[-1].isdigit():
                current.lines.pop()

            current = Cue(start=parse_vtt_seconds(match.group("start")), lines=[])
            cues.append(current)
            continue

        if current is None or not line:
            continue

        if line.startswith(("WEBVTT", "NOTE", "Kind:", "Language:", "STYLE")):
            continue

        cleaned = INLINE_TAG.sub("", line)
        cleaned = re.sub(r"\s+", " ", cleaned).strip()

        if cleaned:
            current.lines.append(cleaned)

    return [cue for cue in cues if cue.lines]


def dedupe_cues(cues: list[Cue]) -> list[tuple[float, str]]:
    """YouTube auto-captions scroll: each cue repeats the previous cue's last lines."""
    segments: list[tuple[float, str]] = []
    emitted: list[str] = []

    for cue in cues:
        fresh = [line for line in cue.lines if line not in emitted]

        if not fresh:
            continue

        segments.append((cue.start, " ".join(fresh)))
        emitted = cue.lines[-4:]

    return segments


def transcript_markdown(segments: list[tuple[float, str]], video_id: str) -> str:
    """Group segments into timestamped paragraphs, each linking back into the video."""
    paragraphs: list[str] = []
    start = 0.0
    buffer: list[str] = []

    def flush() -> None:
        if not buffer:
            return

        stamp = format_timestamp(start)
        link = f"https://youtu.be/{video_id}?t={int(start)}"
        paragraphs.append(f"**[{stamp}]({link})** {' '.join(buffer)}")

    for offset, text in segments:
        long_enough = offset - start >= PARAGRAPH_SECONDS
        wide_enough = sum(len(part) + 1 for part in buffer) >= PARAGRAPH_CHARS

        # Close the paragraph *before* taking the segment that overflows it, so each
        # paragraph's timestamp is the moment its own first words are spoken.
        if buffer and (long_enough or wide_enough):
            flush()
            buffer = []

        if not buffer:
            start = offset

        buffer.append(text)

    flush()

    return "\n\n".join(paragraphs)


# ------------------------------------------------------------------------- yt-dlp glue


def expand_targets(targets: list[str], extra: list[str]) -> list[str]:
    """Turn URLs / playlist aliases into a flat list of video ids."""
    ids: list[str] = []

    for target in targets:
        url = PLAYLIST_ALIASES.get(target.upper(), target)
        command = ["yt-dlp", "--flat-playlist", "--print", "%(id)s", *extra, url]

        try:
            result = run(command, capture=True)
        except subprocess.CalledProcessError:
            print(f"skipped (could not list): {target}", file=sys.stderr)
            continue

        for line in result.stdout.splitlines():
            candidate = line.strip()

            if candidate and candidate not in ids:
                ids.append(candidate)

    return ids


def download(video_id: str, workdir: Path, args: argparse.Namespace) -> dict:
    url = f"https://www.youtube.com/watch?v={video_id}"

    command = [
        "yt-dlp",
        "--no-warnings",
        "--write-info-json",
        "--write-subs",
        "--write-auto-subs",
        "--sub-langs",
        args.lang,
        "--sub-format",
        "vtt/best",
        "--convert-subs",
        "vtt",
        "--output",
        "%(id)s.%(ext)s",
        "--paths",
        str(workdir),
    ]

    if args.no_media:
        command.append("--skip-download")
    elif args.audio_only:
        command += ["--extract-audio", "--audio-format", "m4a"]
    else:
        command += [
            "--format",
            f"bv*[height<={args.max_height}]+ba/b[height<={args.max_height}]/b",
            "--merge-output-format",
            "mp4",
        ]

    command += yt_dlp_extra(args)
    command.append(url)

    run(command)

    info_path = workdir / f"{video_id}.info.json"

    if not info_path.exists():
        raise RuntimeError(f"yt-dlp produced no metadata for {video_id}")

    return json.loads(info_path.read_text(encoding="utf-8"))


def yt_dlp_extra(args: argparse.Namespace) -> list[str]:
    extra: list[str] = []

    if args.cookies_from_browser:
        extra += ["--cookies-from-browser", args.cookies_from_browser]

    if args.cookies:
        extra += ["--cookies", args.cookies]

    return extra


def pick_subtitle(workdir: Path, video_id: str, lang: str) -> tuple[Path | None, str]:
    """Prefer human captions over auto-generated ones, and the requested language."""
    candidates = [
        path
        for path in sorted(workdir.glob(f"{video_id}.*"))
        if path.suffix.lower() in SUBTITLE_EXTS
    ]

    if not candidates:
        return None, "none"

    preferred = lang.split(",")[0].strip().rstrip("*").rstrip(".") or "en"

    def score(path: Path) -> tuple[int, int]:
        # `<id>.<lang>.vtt`, where auto-captions use a language like `en-orig` / `a.en`.
        tag = path.name[len(video_id) + 1 : -len(path.suffix)]
        matches_lang = 0 if tag.startswith(preferred) else 1
        is_auto = 1 if ("orig" in tag or tag.startswith("a.")) else 0

        return (matches_lang, is_auto)

    best = sorted(candidates, key=score)[0]

    return best, "captions"


def transcribe_with_whisper(media: Path, model: str) -> tuple[str, str]:
    """Fallback for videos with captions disabled. Requires `whisper` on PATH."""
    if shutil.which("whisper") is None:
        print("  no captions and whisper is not installed - skipping transcript")

        return "", "none"

    with tempfile.TemporaryDirectory() as tmp:
        run(
            [
                "whisper",
                str(media),
                "--model",
                model,
                "--output_format",
                "vtt",
                "--output_dir",
                tmp,
            ]
        )

        produced = sorted(Path(tmp).glob("*.vtt"))

        if not produced:
            return "", "none"

        return produced[0].read_text(encoding="utf-8"), "whisper"


# ------------------------------------------------------------------------- note output


def chapters_markdown(info: dict, video_id: str) -> str:
    chapters = info.get("chapters") or []
    lines: list[str] = []

    for chapter in chapters:
        title = str(chapter.get("title") or "").strip()
        start = chapter.get("start_time")

        if not title or start is None:
            continue

        stamp = format_timestamp(float(start))
        lines.append(f"- [{stamp}](https://youtu.be/{video_id}?t={int(float(start))}) {title}")

    return "\n".join(lines)


def build_note(
    info: dict,
    *,
    media_link: str,
    transcript: str,
    transcript_source: str,
    today: str,
) -> str:
    video_id = str(info.get("id") or "")
    title = str(info.get("title") or video_id)
    channel = str(info.get("channel") or info.get("uploader") or "")
    url = str(info.get("webpage_url") or f"https://www.youtube.com/watch?v={video_id}")
    published = iso_date(info.get("upload_date"))
    duration = format_duration(info.get("duration"))
    thumbnail = str(info.get("thumbnail") or "")
    description = str(info.get("description") or "").strip()

    frontmatter = [
        "---",
        "type: video",
        "categories:",
        '  - "[[Clippings]]"',
        f"created: {today}",
        "source: youtube",
        "platform: youtube",
        f"channel: {yaml_string(channel)}" if channel else "channel:",
        f"url: {url}",
        f"video_id: {video_id}",
        f"published: {published}" if published else "published:",
        f"duration: {yaml_string(duration)}" if duration else "duration:",
        f"media: {yaml_string(media_link)}" if media_link else "media:",
        f"transcript_source: {transcript_source}",
        f"thumbnail_url: {thumbnail}" if thumbnail else "thumbnail_url:",
        "rating:",
        "action: review",
        "tags:",
        "  - youtube",
        "  - video",
        "---",
    ]

    meta_line = " · ".join(
        part
        for part in [
            f"**{channel}**" if channel else "",
            duration,
            published,
            f"[Watch on YouTube]({url})",
        ]
        if part
    )

    body = [f"# {title}", ""]

    if media_link:
        body += [f"![[{media_link}]]", ""]
    elif thumbnail:
        body += [f"![thumbnail]({thumbnail})", ""]

    body += [meta_line, "", "## Notes", "", "", ""]

    chapters = chapters_markdown(info, video_id)

    if chapters:
        body += ["## Chapters", "", chapters, ""]

    if description:
        body += ["## Description", "", description, ""]

    body += ["## Transcript", ""]

    if transcript:
        body += [transcript, ""]
    else:
        body += ["_No transcript available for this video._", ""]

    return "\n".join(frontmatter) + "\n\n" + "\n".join(body)


# -------------------------------------------------------------------------------- main


def process(video_id: str, args: argparse.Namespace, vault: Path) -> str:
    note_dir = vault / NOTE_SUBDIR
    media_dir = vault / MEDIA_SUBDIR

    existing = list(note_dir.glob(f"* ({video_id}).md"))

    if existing and not args.force:
        return f"exists, skipped: {existing[0].name}"

    with tempfile.TemporaryDirectory() as tmp:
        workdir = Path(tmp)
        info = download(video_id, workdir, args)

        title = str(info.get("title") or video_id)
        stem = f"{safe_filename(title)} ({video_id})"

        media_link = ""

        if not args.no_media:
            media_files = [
                path
                for path in sorted(workdir.glob(f"{video_id}.*"))
                if path.suffix.lower() in (".mp4", ".mkv", ".webm", ".m4a", ".mp3", ".opus")
            ]

            if media_files:
                media_dir.mkdir(parents=True, exist_ok=True)
                target = media_dir / f"{stem}{media_files[0].suffix}"

                # A re-run with a different format would otherwise orphan the old file.
                for stale_media in media_dir.glob(f"* ({video_id}).*"):
                    if stale_media != target:
                        stale_media.unlink()

                shutil.move(str(media_files[0]), target)
                media_link = str(MEDIA_SUBDIR / target.name)

        subtitle_path, transcript_source = pick_subtitle(workdir, video_id, args.lang)
        vtt_text = subtitle_path.read_text(encoding="utf-8") if subtitle_path else ""

        if not vtt_text and args.whisper and media_link:
            vtt_text, transcript_source = transcribe_with_whisper(
                media_dir / Path(media_link).name, args.whisper
            )

        transcript = ""

        if vtt_text:
            transcript = transcript_markdown(dedupe_cues(parse_vtt(vtt_text)), video_id)

        note = build_note(
            info,
            media_link=media_link,
            transcript=transcript,
            transcript_source=transcript_source if transcript else "none",
            today=date.today().isoformat(),
        )

    note_dir.mkdir(parents=True, exist_ok=True)

    for stale in existing:
        stale.unlink()

    note_path = note_dir / f"{stem}.md"
    note_path.write_text(note, encoding="utf-8")

    return f"wrote: {note_path.relative_to(vault)}"


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Archive YouTube videos + transcripts into the Obsidian vault.",
    )

    parser.add_argument(
        "targets",
        nargs="+",
        metavar="TARGET",
        help="video URLs, playlist URLs, or the aliases WL (Watch Later) / LL (Liked)",
    )
    parser.add_argument(
        "--vault",
        type=Path,
        default=Path(__file__).resolve().parents[2],
        help="vault root (defaults to the vault this script lives in)",
    )
    parser.add_argument(
        "--lang",
        default="en.*,en",
        help="subtitle languages passed to yt-dlp --sub-langs (default: en.*,en)",
    )
    parser.add_argument(
        "--max-height",
        type=int,
        default=1080,
        help="cap the video height (default: 1080)",
    )
    parser.add_argument(
        "--audio-only",
        action="store_true",
        help="keep only the audio track (m4a) instead of the video",
    )
    parser.add_argument(
        "--no-media",
        action="store_true",
        help="write the note and transcript without downloading any media",
    )
    parser.add_argument(
        "--whisper",
        nargs="?",
        const="base",
        metavar="MODEL",
        help="transcribe locally with whisper when the video has no captions",
    )
    parser.add_argument(
        "--cookies-from-browser",
        metavar="BROWSER",
        help="read cookies from a browser (chrome/firefox/safari/brave) - needed for WL/LL",
    )
    parser.add_argument("--cookies", metavar="FILE", help="cookies.txt file instead of a browser")
    parser.add_argument("--limit", type=int, help="process at most N videos")
    parser.add_argument("--force", action="store_true", help="re-download and overwrite notes")
    parser.add_argument("--dry-run", action="store_true", help="list what would be archived")

    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)

    if shutil.which("yt-dlp") is None:
        die("yt-dlp is not installed - `brew install yt-dlp ffmpeg` or `pipx install yt-dlp`")

    vault = args.vault.expanduser().resolve()

    if not vault.is_dir():
        die(f"vault not found: {vault}")

    if args.audio_only and args.no_media:
        die("--audio-only and --no-media are mutually exclusive")

    video_ids = expand_targets(args.targets, yt_dlp_extra(args))

    if args.limit:
        video_ids = video_ids[: args.limit]

    if not video_ids:
        die("nothing to archive")

    if args.dry_run:
        for video_id in video_ids:
            print(f"would archive https://www.youtube.com/watch?v={video_id}")

        return 0

    failures = 0

    for index, video_id in enumerate(video_ids, start=1):
        print(f"[{index}/{len(video_ids)}] {video_id}")

        try:
            print(f"  {process(video_id, args, vault)}")
        except (subprocess.CalledProcessError, RuntimeError, OSError) as error:
            failures += 1
            print(f"  failed: {error}", file=sys.stderr)

    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
