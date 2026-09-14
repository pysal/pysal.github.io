#!/usr/bin/env python3
"""
generate_news.py — create News page entries for new PySAL package releases.

For each federated package, fetches the latest GitHub release and, if it is
not already represented in content/news/ (matched by release URL, not by
filename), writes a new Hugo content file with the front matter used
throughout content/news/*.md:

    ---
    title: <pkg> <version>
    date: <release date, YYYY-MM-DD>
    description: <pkg> <version> released.
    type: news
    month: "MM.DD"
    year: "YYYY"
    link: "<github release url>"
    ---

Intended to run on a schedule via GitHub Actions, with the resulting new
files (if any) opened as a pull request rather than committed directly, so a
maintainer can enrich the auto-generated one-line description before it goes
live.

Stdlib only (matches the sibling ecosystem_releases.py report script).
Auth: set GH_TOKEN or GITHUB_TOKEN to raise the GitHub API rate limit.

Usage:
    python scripts/generate_news.py [--content-dir content/news] [--org pysal]
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import sys
import urllib.error
import urllib.request

ORG = "pysal"

# Packages bundled by the pysal meta-package, plus the meta-package itself.
PACKAGES = [
    "pysal",
    "libpysal",
    "access",
    "esda",
    "giddy",
    "inequality",
    "pointpats",
    "segregation",
    "spaghetti",
    "mgwr",
    "momepy",
    "spglm",
    "spint",
    "spml",
    "spreg",
    "tobler",
    "mapclassify",
    "splot",
    "spopt",
    "gwlearn",
]

UA = "pysal-news-generator (+https://github.com/pysal/pysal.github.io)"
TIMEOUT = 30

_token_rejected = False


# --------------------------------------------------------------------------- http


def _get_json(url: str, token: str | None = None, _auth: bool = True):
    global _token_rejected
    headers = {"User-Agent": UA, "Accept": "application/vnd.github+json"}
    use_auth = _auth and token and not _token_rejected and "api.github.com" in url
    if use_auth:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=TIMEOUT) as resp:
            return json.load(resp)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return None
        if e.code in (401, 403) and use_auth:
            _token_rejected = True
            print(
                "  ! GitHub token rejected — falling back to unauthenticated (60 req/hr)",
                file=sys.stderr,
            )
            return _get_json(url, token, _auth=False)
        print(f"  ! {url} -> HTTP {e.code}", file=sys.stderr)
        return None
    except (urllib.error.URLError, TimeoutError, json.JSONDecodeError) as e:
        print(f"  ! {url} -> {e}", file=sys.stderr)
        return None


# ------------------------------------------------------------------------- helpers


def _parse_dt(s: str | None):
    if not s:
        return None
    try:
        return dt.datetime.fromisoformat(s.replace("Z", "+00:00"))
    except ValueError:
        return None


def _norm(v: str) -> str:
    return v.lstrip("vV").strip()


def gh_latest_release(pkg: str, token: str | None):
    d = _get_json(f"https://api.github.com/repos/{ORG}/{pkg}/releases/latest", token)
    if isinstance(d, dict) and "tag_name" in d:
        return {
            "tag": d["tag_name"],
            "date": _parse_dt(d.get("published_at")),
            "url": d.get("html_url", ""),
        }
    return None


def existing_links(content_dir: str) -> set[str]:
    """Every 'link:' value already present in content/news/*.md front matter."""
    links = set()
    if not os.path.isdir(content_dir):
        return links
    for name in os.listdir(content_dir):
        if not name.endswith(".md"):
            continue
        path = os.path.join(content_dir, name)
        try:
            with open(path, encoding="utf-8") as fh:
                text = fh.read()
        except OSError:
            continue
        m = re.search(r'^link:\s*"?(.+?)"?\s*$', text, re.MULTILINE)
        if m:
            links.add(m.group(1).strip().rstrip("/"))
    return links


def slugify_filename(pkg: str, version: str) -> str:
    safe_version = re.sub(r"[^A-Za-z0-9.\-]", "-", version)
    return f"{pkg}_{safe_version}.md"


def render_entry(pkg: str, version: str, date: dt.datetime, url: str) -> str:
    return (
        "---\n"
        f"title: {pkg} {version}\n"
        f"date: {date:%Y-%m-%d}\n"
        f"description: {pkg} {version} released.\n"
        "type: news\n"
        f'month: "{date:%m.%d}"\n'
        f'year: "{date:%Y}"\n'
        f'link: "{url}"\n'
        "---\n"
    )


# ---------------------------------------------------------------------------- main


def main(argv=None):
    global ORG
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument("--content-dir", default="content/news", help="Hugo news content dir")
    ap.add_argument("--org", default="pysal", help="GitHub org (default: pysal)")
    args = ap.parse_args(argv)
    ORG = args.org

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        print(
            "note: no GH_TOKEN/GITHUB_TOKEN set — GitHub API is limited to 60 req/hr",
            file=sys.stderr,
        )

    known = existing_links(args.content_dir)
    os.makedirs(args.content_dir, exist_ok=True)

    created = []
    for pkg in PACKAGES:
        print(f"- {pkg}", file=sys.stderr)
        release = gh_latest_release(pkg, token)
        if not release or not release["url"] or not release["date"]:
            continue
        if release["url"].rstrip("/") in known:
            continue

        version = _norm(release["tag"])
        filename = slugify_filename(pkg, version)
        path = os.path.join(args.content_dir, filename)
        if os.path.exists(path):
            # Filename collision without a matching link (e.g. re-tagged
            # release) — don't clobber a hand-edited file.
            print(f"  ! {path} already exists, skipping", file=sys.stderr)
            continue

        with open(path, "w", encoding="utf-8") as fh:
            fh.write(render_entry(pkg, version, release["date"], release["url"]))
        created.append(path)
        print(f"  + {path}", file=sys.stderr)

    if created:
        print(f"created {len(created)} new news entr{'y' if len(created) == 1 else 'ies'}")
    else:
        print("no new releases found")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
