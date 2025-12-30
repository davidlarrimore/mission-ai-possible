# Repository Guidelines

## Project Structure & Module Organization
- `campaign/` holds gameplay content by week: `weeks/<##-operation-name>/challenges/<slug>/` with `prompt.md`, `readme.md`, and `banner.(png|webp)` plus `quiz/quiz.json` for assessments. Keep slugs lowercase-with-hyphens.
- `campaign-manifest.json` contains full campaign metadata; `campaign/catalog.json` indexes week manifests.
- `assets/` stores shared banners and difficulty badges with `assets/manifest.json` as the catalog; prefer WebP when possible.
- `docs/` contains contributor guides and data schemas; `prompts/` has reusable AI prompt templates; `scripts/` hosts utilities; `clean.sh` sanitizes Markdown for Open WebUI.

## Build, Test, and Development Commands
- `./clean.sh` — interactive sanitizer for any `*.md`; run before committing prompts to normalize quotes and code fences.
- `python3 scripts/png_to_webp_and_delete.py --dry-run` then rerun without `--dry-run` — convert and resize PNG banners to WebP; add `--keep-png` if originals must remain.
- `python3 -m json.tool <path/to/file.json>` — quick validation/pretty-print for `campaign-manifest.json`, week quizzes, and catalogs.
- Manual gameplay check in Open WebUI (Claude 3.5 Haiku) for new or edited challenges to verify access lock, mission start banner, state tracking, and completion messaging.

## Coding Style & Naming Conventions
- Markdown: concise headings, bullet lists, and explicit instructions; avoid smart quotes and trailing spaces (use `clean.sh`).
- JSON: two-space indent, double quotes, stable ordering (weeks in chronological order, challenges grouped by week); keep keys consistent with existing manifests.
- Assets: name banners `banner.webp` when converted; keep width ≤1600px; store in the challenge folder or shared `assets/` paths referenced via raw GitHub URLs.

## Testing Guidelines
- Quizzes must match `docs/quiz-schema.json`; validate JSON shape with `python3 -m json.tool` and spot-check options/answers.
- For prompts, confirm the "Start Challenge" access lock remains, success/failure messaging is intact, and visible progress/state is updated every turn in Open WebUI.
- After edits, re-run `./clean.sh` on touched Markdown and ensure manifests still reference the correct slugs and assets.

## Commit & Pull Request Guidelines
- Commit messages: present-tense, imperative, under ~72 characters, and mention the week/challenge when relevant (e.g., "Refine Firewall/Mind Lock prompt copy").
- PRs should summarize scope, list touched weeks/challenges or assets, link related issues, note if assets were converted or sanitized, and include screenshots for new/updated banners when feasible.
- Keep changes focused; update manifests and catalogs alongside content edits so metadata stays in sync.

## Security & Content Handling
- Do not commit secrets, API keys, or participant data. Use placeholders for any sample credentials or URLs.
- Prefer lightweight, optimized assets; run the WebP converter before adding new banners.
- Preserve access-lock language to prevent premature content leakage, and avoid embedding proprietary data in prompts or quizzes.
