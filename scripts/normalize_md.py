#!/usr/bin/env python3
"""normalize_md.py — invisible-character & line-ending hygiene for Markdown.

Modern, idempotent replacement for the old interactive ``clean.sh``. It fixes
the things that genuinely break Open WebUI rendering or confuse the model when
a prompt is pasted in from Word, Google Docs, or another AI tool — and it
deliberately LEAVES PUNCTUATION ALONE (smart quotes and em-dashes are part of
the intentional Mission:AI Possible typography).

What it normalizes
------------------
- BOM (U+FEFF) stripped
- Junk zero-width characters removed: U+200B ZWSP, U+2060 word-joiner,
  U+FEFF (also as mid-file ZWNBSP)
- Non-breaking space (U+00A0) and narrow NBSP (U+202F) -> regular space
- CRLF / lone CR -> LF
- Ensures the file ends with exactly one trailing newline

What it does NOT touch (on purpose)
-----------------------------------
- Smart quotes, em/en dashes, bullets — preserved
- Trailing whitespace — preserved (markdown hard-breaks use it)
- Code fences and the ⟦MISSION_CODE: GHOST-314⟧ reserved strings — untouched
- ZWJ (U+200D) / ZWNJ (U+200C) — preserved: they are meaningful inside
  emoji sequences (e.g. 👩‍🏫) and scripts like Persian/Indic

Usage
-----
  normalize_md.py PATH [PATH ...]   normalize the given files in place
  normalize_md.py --all             normalize all repo Markdown (campaign/, docs/, root)
  normalize_md.py --staged          normalize git-staged Markdown (used by pre-commit)
  normalize_md.py --check [...]      report problems and exit 1 if any (CI); no writes

--check composes with --all / --staged / explicit paths.
"""
from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

# Junk zero-width characters removed outright. NOTE: ZWJ (U+200D) and ZWNJ
# (U+200C) are intentionally NOT here — they are meaningful inside emoji
# sequences (e.g. 👩‍🏫) and in scripts like Persian/Indic.
ZERO_WIDTH = {
    "﻿",  # U+FEFF BOM / zero-width no-break space
    "​",  # U+200B zero-width space
    "⁠",  # U+2060 word joiner
}
# Characters mapped to a regular space.
SPACE_LIKE = {
    " ",  # non-breaking space
    " ",  # narrow no-break space
}


def normalize_text(text: str) -> str:
    """Return the cleaned form of *text*. Pure function, idempotent."""
    # Line endings first.
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    for ch in ZERO_WIDTH:
        text = text.replace(ch, "")
    for ch in SPACE_LIKE:
        text = text.replace(ch, " ")
    # Exactly one trailing newline (only if file is non-empty).
    if text and not text.endswith("\n"):
        text += "\n"
    text = text.rstrip("\n") + "\n" if text.strip() else text
    return text


def describe_problems(text: str) -> list[str]:
    """Human-readable list of issues found in *text* (for --check)."""
    problems: list[str] = []
    lines = text.split("\n")
    if "\r" in text:
        problems.append("contains CR / CRLF line endings")
    for lineno, line in enumerate(lines, start=1):
        for ch in ZERO_WIDTH:
            if ch in line:
                problems.append(f"line {lineno}: zero-width char U+{ord(ch):04X}")
        for ch in SPACE_LIKE:
            if ch in line:
                problems.append(f"line {lineno}: non-breaking space U+{ord(ch):04X}")
    return problems


def iter_repo_markdown() -> list[Path]:
    """All Markdown under campaign/, docs/, and the repo root."""
    found: list[Path] = []
    found.extend(sorted((REPO_ROOT / "campaign").rglob("*.md")))
    found.extend(sorted((REPO_ROOT / "docs").glob("*.md")))
    found.extend(sorted(REPO_ROOT.glob("*.md")))
    # De-dupe while preserving order.
    seen: set[Path] = set()
    unique: list[Path] = []
    for p in found:
        if p not in seen:
            seen.add(p)
            unique.append(p)
    return unique


def iter_staged_markdown() -> list[Path]:
    out = subprocess.run(
        ["git", "diff", "--cached", "--name-only", "--diff-filter=ACM"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
        check=True,
    ).stdout
    return [REPO_ROOT / line for line in out.splitlines() if line.endswith(".md")]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", type=Path, help="Markdown files to process")
    parser.add_argument("--all", action="store_true", help="process all repo Markdown")
    parser.add_argument("--staged", action="store_true", help="process git-staged Markdown")
    parser.add_argument("--check", action="store_true", help="report only; exit 1 if any issues (no writes)")
    args = parser.parse_args(argv)

    if args.all:
        targets = iter_repo_markdown()
    elif args.staged:
        targets = iter_staged_markdown()
    else:
        targets = [p if p.is_absolute() else (Path.cwd() / p) for p in args.paths]

    if not targets:
        if args.staged:
            return 0  # nothing staged; not an error
        parser.error("no files given (pass paths, --all, or --staged)")

    changed: list[Path] = []
    flagged: list[tuple[Path, list[str]]] = []

    for path in targets:
        if not path.is_file():
            print(f"skip (not a file): {path}", file=sys.stderr)
            continue
        original = path.read_text(encoding="utf-8")
        cleaned = normalize_text(original)
        if args.check:
            problems = describe_problems(original)
            if problems or original != cleaned:
                flagged.append((path, problems or ["needs normalization (line endings / trailing newline)"]))
            continue
        if cleaned != original:
            path.write_text(cleaned, encoding="utf-8")
            changed.append(path)

    rel = lambda p: p.relative_to(REPO_ROOT) if p.is_relative_to(REPO_ROOT) else p

    if args.check:
        if flagged:
            print("❌ Markdown hygiene issues found:\n")
            for path, problems in flagged:
                print(f"  {rel(path)}")
                for problem in problems[:10]:
                    print(f"      - {problem}")
                if len(problems) > 10:
                    print(f"      - ... and {len(problems) - 10} more")
            print("\nRun: python3 scripts/normalize_md.py --all")
            return 1
        print(f"✅ Markdown hygiene clean ({len(targets)} files checked).")
        return 0

    if changed:
        print(f"🧼 Normalized {len(changed)} file(s):")
        for path in changed:
            print(f"  {rel(path)}")
    else:
        print(f"✅ Nothing to change ({len(targets)} files already clean).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
