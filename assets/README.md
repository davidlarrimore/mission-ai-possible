# Shared Campaign Assets

This folder centralizes evergreen artwork that challenges can reuse without duplicating files. Follow these guidelines when referencing assets in prompts, docs, or integrations:

1. **Use canonical paths** – reference assets relative to the repo root (e.g., `assets/banners/shared/mission-complete-banner.png`). When embedding in Markdown for remote use, point to the raw GitHub URL `https://raw.githubusercontent.com/davidlarrimore/mission-ai-possible/main/<path>`.
2. **Avoid spaces and uppercase** – filenames are lowercase-with-hyphens to stay URL-friendly and consistent across platforms.
3. **Prefer shared banners** – only create mission-specific art inside `campaign/weeks/.../challenges/<slug>/banner.png`. Shared art (mission complete, difficulty badges, etc.) belongs here.
4. **Document new assets** – when adding files, update `assets/manifest.json` with a short description, tags, and intended usage so authors can discover them quickly.
5. **Keep files optimized** – export PNGs at web resolution (typically 1600px width or less) to prevent bloated prompts and Git history.

## Directory Overview

```
assets/
├── README.md
├── banners/
│   └── shared/
│       └── mission-complete-banner.webp
└── graphics/
    └── difficulty/
        ├── very-easy.webp
        ├── easy.webp
        ├── medium.webp
        └── hard.webp
```

- `banners/shared/mission-complete-banner.png` – universal success banner referenced by every challenge.
- `graphics/difficulty/*.png` – optional badges for docs or marketing collateral based on challenge difficulty.

When in doubt, keep assets DRY: if multiple challenges need the same graphic, keep it here rather than copying files into each week.
