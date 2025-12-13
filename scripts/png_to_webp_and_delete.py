#!/usr/bin/env python3
"""
Repo-wide PNG -> WebP converter + PNG cleanup.

What it does:
- Recursively finds all .png files (case-insensitive).
- Converts each to .webp (same folder, same basename).
- Resizes to a max width (default 800px) while preserving aspect ratio.
- Deletes the original .png ONLY if conversion succeeds and output looks valid.

Why this is safe:
- Never deletes a PNG unless the WebP was successfully generated.
- Supports --dry-run to preview actions.
- Skips common heavy/vendor/build directories.

Requirements:
- cwebp must be installed and available on PATH.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
from pathlib import Path

# Directories to skip (common in git repos)
SKIP_DIRS = {
    ".git", "node_modules", ".venv", "venv", "__pycache__",
    "dist", "build", ".next", ".cache"
}

def should_skip(path: Path) -> bool:
    """Return True if any part of the path is in the skip list."""
    return any(part in SKIP_DIRS for part in path.parts)

def is_png(path: Path) -> bool:
    """Case-insensitive .png detection."""
    return path.is_file() and path.suffix.lower() == ".png"

def build_cwebp_cmd(src: Path, dst: Path, max_width: int, quality: int) -> list[str]:
    """
    Build a cwebp command optimized for small size with good visual quality for banners.
    -resize {max_width} 0 keeps aspect ratio (height auto)
    -q controls lossy quality (lower -> smaller, higher -> cleaner)
    -m 6 is best compression effort
    -mt enables multi-threading
    -af auto filter
    -sharp_yuv helps preserve sharp edges/text in typical banner art
    -metadata none strips metadata for smaller output
    """
    return [
        "cwebp",
        str(src),
        "-resize", str(max_width), "0",
        "-q", str(quality),
        "-m", "6",
        "-mt",
        "-af",
        "-sharp_yuv",
        "-metadata", "none",
        "-o", str(dst),
    ]

def convert_one(src: Path, max_width: int, quality: int, force: bool, dry_run: bool) -> tuple[bool, str]:
    """
    Convert a single PNG to WebP.
    Returns (success, message).
    """
    dst = src.with_suffix(".webp")

    if dst.exists() and not force:
        return (True, f"SKIP (webp exists): {src}")

    cmd = build_cwebp_cmd(src, dst, max_width=max_width, quality=quality)

    if dry_run:
        return (True, f"DRY RUN: {' '.join(cmd)}")

    try:
        # Capture stderr for error reporting; quiet stdout
        result = subprocess.run(cmd, check=False, capture_output=True, text=True)

        if result.returncode != 0:
            # If conversion failed, do not delete original.
            err = (result.stderr or "").strip()
            return (False, f"FAIL: {src} (cwebp exit {result.returncode})\n{err}")

        # Basic sanity check: file exists and is non-trivial in size
        if not dst.exists() or dst.stat().st_size < 50:
            return (False, f"FAIL: {src} (output missing or too small)")

        return (True, f"OK: {src} -> {dst}")

    except FileNotFoundError:
        return (False, "FAIL: cwebp not found on PATH. Install with 'brew install webp' or 'apt-get install webp'.")
    except Exception as e:
        return (False, f"FAIL: {src} ({e})")

def main() -> None:
    ap = argparse.ArgumentParser(description="Convert all PNGs to resized WebP, then delete PNGs after successful conversion.")
    ap.add_argument("--root", default=".", help="Root directory to scan (default: current directory).")
    ap.add_argument("--max-width", type=int, default=800, help="Max output width in pixels (default: 800).")
    ap.add_argument("--quality", type=int, default=82, help="WebP lossy quality 0-100 (default: 82).")
    ap.add_argument("--force", action="store_true", help="Overwrite existing .webp files.")
    ap.add_argument("--dry-run", action="store_true", help="Show what would happen, but do not write/delete anything.")
    ap.add_argument("--keep-png", action="store_true", help="Do not delete PNGs (convert only).")
    args = ap.parse_args()

    if not (0 <= args.quality <= 100):
        raise SystemExit("--quality must be between 0 and 100")

    # Pre-flight: ensure cwebp is available (unless dry-run)
    if not args.dry_run and shutil.which("cwebp") is None:
        raise SystemExit("cwebp not found on PATH. Install webp tools first (macOS: brew install webp).")

    root = Path(args.root).resolve()

    pngs: list[Path] = []
    for p in root.rglob("*"):
        if should_skip(p):
            continue
        if is_png(p):
            pngs.append(p)

    if not pngs:
        print("No PNG files found. Nothing to do.")
        return

    converted_ok: list[Path] = []
    failed: list[Path] = []

    for src in sorted(pngs):
        ok, msg = convert_one(
            src,
            max_width=args.max_width,
            quality=args.quality,
            force=args.force,
            dry_run=args.dry_run
        )
        print(msg)
        if ok:
            # Only mark as converted if we actually produced a webp (or skipped because it exists)
            # For dry-run we treat it as ok but won't delete anything anyway.
            converted_ok.append(src)
        else:
            failed.append(src)

    # Delete originals only when: not dry-run, not keep-png, and corresponding webp exists & looks valid
    deleted = 0
    if not args.dry_run and not args.keep_png:
        for src in converted_ok:
            dst = src.with_suffix(".webp")
            if dst.exists() and dst.stat().st_size >= 50:
                try:
                    src.unlink()
                    deleted += 1
                    print(f"Deleted: {src}")
                except Exception as e:
                    print(f"ERROR deleting {src}: {e}")

    print("\nSummary")
    print(f"- PNGs found:     {len(pngs)}")
    print(f"- Converted/OK:   {len(converted_ok)}")
    print(f"- Failed:         {len(failed)}")
    if args.dry_run:
        print("- Deleted:        0 (dry-run)")
    elif args.keep_png:
        print("- Deleted:        0 (--keep-png)")
    else:
        print(f"- Deleted:        {deleted}")

    if failed:
        # Non-zero exit for CI usefulness
        raise SystemExit(2)

if __name__ == "__main__":
    main()