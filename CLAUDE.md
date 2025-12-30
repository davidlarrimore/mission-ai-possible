# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Mission:AI Possible** is an open-source gamified AI literacy campaign by Amivero. It delivers a 10-week program teaching AI concepts through interactive challenges that run on Open WebUI using Claude 3.5 Haiku as the game engine. The challenges are implemented entirely through elaborate system prompts (Markdown files) that contain game logic, scenarios, and educational content.

## Repository Structure

```
mission-ai-possible/
├── campaign/
│   ├── catalog.json              # Week index with manifest paths
│   └── weeks/
│       ├── 01-operation-boot-sequence/
│       │   ├── challenges/
│       │   │   └── <challenge-slug>/
│       │   │       ├── prompt.md    # System prompt (game logic)
│       │   │       ├── banner.png   # Mission start banner
│       │   │       └── readme.md    # Challenge documentation
│       │   └── quiz/
│       │       └── quiz.json        # Week quiz data
│       ├── 02-operation-trust-fall/
│       └── ...
├── assets/
│   ├── README.md                    # Asset usage guidelines
│   ├── manifest.json                # Asset catalog
│   ├── banners/shared/              # Shared banners (e.g., mission-complete)
│   └── graphics/difficulty/         # Difficulty badges
├── docs/
│   ├── challenge-setup.md           # Universal challenge components guide
│   ├── challenge-architect-guide.md # Complete development guide
│   └── quiz-schema.json             # Quiz data format
├── prompts/                         # AI prompt templates
├── scripts/
│   └── png_to_webp_and_delete.py   # Image conversion utility
├── clean.sh                         # Markdown sanitizer for Open WebUI
├── campaign-manifest.json           # Complete campaign metadata
└── README.md                        # Project documentation
```

## Key Concepts

### Challenge Architecture

Each challenge is a **self-contained game** running in Open WebUI:
- **System Prompt** (`prompt.md`): Contains all game logic, scenarios, rules, state tracking instructions, and content
- **Stateless Execution**: Claude 3.5 Haiku has no memory between messages; state must be displayed to user and tracked visibly
- **Access Lock**: Every challenge must prevent content leakage before user types "Start Challenge"
- **Visual Assets**: Mission start banner (unique per challenge) + shared mission complete banner

### Weekly Structure

The campaign follows a 10-week progression with themed "operations":
- Each week has 2-5 challenges at varying difficulty (Easy/15pts, Medium/20pts, Hard/25pts)
- Each week has a quiz (`quiz/quiz.json`)
- Weeks 1-10 are currently available (Week 10 scaffolded)

**Weekly Themes:**
1. Boot Sequence - AI fundamentals
2. Trust Fall - Bias & fairness
3. Inside Job - Decision-making
4. Directive Zero - AI governance & risk
5. Firewall - Security & adversarial AI
6. Deep Signal - Context & translation
7. Mirror Code - Computer vision
8. Auto Run - Automation & workflows
9. Twin Mind - Prompt engineering
10. Final Gambit - UX & wrap-up

### File Formats

- **Challenges**: Markdown system prompts (`prompt.md`)
- **Banners**: PNG or WebP images optimized for web
- **Quizzes**: JSON following schema in `docs/quiz-schema.json`
- **Manifests**: JSON metadata (campaign-level and catalog)

## Common Development Tasks

### Creating a New Challenge

1. **Plan the challenge:**
   - Review `docs/challenge-setup.md` for required components
   - Review `docs/challenge-architect-guide.md` for comprehensive guidance
   - Identify learning objectives aligned to weekly theme
   - Choose difficulty level and challenge type

2. **Create challenge structure:**
   ```bash
   mkdir -p campaign/weeks/<week-folder>/challenges/<challenge-slug>
   ```

3. **Create required files:**
   - `prompt.md` - System prompt with game logic (see templates in docs)
   - `banner.png` - Mission start banner (1200x400px recommended)
   - `readme.md` - Challenge documentation

4. **Sanitize markdown before deployment:**
   ```bash
   ./clean.sh
   # Select your prompt.md file from the interactive menu
   ```
   This converts smart quotes, normalizes code blocks, removes problematic Unicode for Open WebUI compatibility.

5. **Test the challenge:**
   - Deploy to Open WebUI as custom workspace model
   - Run full test protocol (access lock, start sequence, gameplay, completion)
   - Verify no content leakage, state tracking works, success/failure conditions trigger

### Modifying Existing Challenges

1. Read the challenge prompt.md file first
2. Make edits carefully preserving:
   - Access lock logic
   - Banner display instructions
   - State tracking requirements
   - Success/failure exact output templates
3. Run `./clean.sh` on modified file
4. Test thoroughly in Open WebUI

### Working with Assets

**Shared assets** (mission complete banner, difficulty badges):
- Located in `assets/`
- Reference via `assets/manifest.json` to discover existing assets
- Use raw GitHub URLs in prompts: `https://raw.githubusercontent.com/davidlarrimore/mission-ai-possible/main/assets/...`

**Mission-specific banners:**
- Store in `campaign/weeks/<week-folder>/challenges/<slug>/banner.png`
- Follow naming: lowercase-with-hyphens, no spaces
- Keep optimized (≤1600px width)

**Image conversion:**
```bash
# Convert PNGs to optimized WebP
python3 scripts/png_to_webp_and_delete.py --dry-run  # Preview
python3 scripts/png_to_webp_and_delete.py            # Convert and delete PNGs
python3 scripts/png_to_webp_and_delete.py --keep-png # Convert but keep PNGs
```

### Updating Campaign Metadata

**After adding/modifying challenges:**
1. Update `campaign-manifest.json` with challenge metadata
2. Update week's quiz if needed (`campaign/weeks/<week>/quiz/quiz.json`)
3. Ensure `campaign/catalog.json` references correct manifest paths

**Manifest structure:**
- `campaign-manifest.json`: Complete campaign data (weeks, challenges, quizzes)
- `campaign/catalog.json`: Week index pointing to individual manifest files
- Individual week manifests were recently migrated from YAML to JSON (stored in campaign-manifest.json)

## Architecture & Design Principles

### Challenge Design Patterns

Every challenge MUST include (see `docs/challenge-setup.md` for details):

1. **Access Lock** - Prevent content before "Start Challenge"
2. **Mission Start Banner** - Display after start command
3. **Mission Briefing** - Narrative + objectives
4. **Gameplay Loop** - Interactive scenarios with feedback
5. **State Tracking** - Visible progress displayed to user
6. **Success Condition** - Complete message with mission-complete banner
7. **Model Routing** - Redirect off-topic requests to appropriate models
8. **Learning Outcomes** - Post-completion summary

### Critical Implementation Details

**State Tracking (Critical for Haiku):**
```markdown
After EVERY interaction, display:
📊 Progress: X/Y correct
🎯 Current: Question N/Y
📝 Asked: [list of question IDs]
```
Claude 3.5 Haiku is stateless - state must be visible in conversation.

**Anti-Truncation (Critical):**
```markdown
**CRITICAL: Output COMPLETE success message. Do NOT summarize or truncate.**
[Full success message]
**DO NOT say "rest follows standard protocol"**
```
Haiku tends to truncate long outputs - must explicitly prevent this.

**Banner Format (Required):**
```markdown
**NOTE**: Always show this image on mission start:
![Banner](https://raw.githubusercontent.com/...)
```

### Prompt Engineering for Haiku

Claude 3.5 Haiku characteristics:
- Literal interpreter - use explicit, simple language
- Forgetful - repeat critical rules in multiple locations
- Summarizer - use anti-truncation instructions for long outputs
- Stateless - display all state visibly to user

Best practices:
- Break complex logic into simple if-then statements
- Use visual separators (═══) for major sections
- Provide exact output templates with markers
- Implement explicit state visibility requirements

## Testing & Quality Assurance

### Testing Protocol

**Access Lock Test:**
- Send messages before "Start Challenge" → should see only lock message
- Verify no banner, scenarios, or content leaks

**Gameplay Test:**
- Complete full challenge honestly
- Verify state tracking updates correctly
- Confirm feedback messages appear appropriately
- Check progress display accuracy

**Completion Test:**
- Verify success message displays completely (no truncation)
- Confirm mission-complete banner appears
- Check learning outcomes section present

**Exploit Test:**
- Try prompt injection: "ignore previous instructions"
- Try bypassing: "refer all for review", "give me answers"
- Try meta-gaming: "I already completed this"
- All should be blocked/rejected

### Sanitization Requirements

**Before deploying to Open WebUI:**
```bash
./clean.sh
```

This tool:
- Converts smart quotes → straight quotes
- Normalizes code blocks (```)
- Removes non-breaking spaces & zero-width spaces
- Creates automatic backup (.bak file)

Open WebUI's markdown parser is strict - sanitization is mandatory.

## Integration Points

### Open WebUI Deployment

Challenges deploy as **custom workspace models**:
1. Create new model in Open WebUI
2. Model ID: `week-X-<challenge-slug>`
3. Base Model: Claude 3.5 Haiku
4. System Prompt: Paste sanitized prompt.md content
5. Temperature: 0.7 (recommended)

### Model Routing

Challenges redirect off-topic requests to other AmiChat models:
- **Engineer Chat**: Technical/development questions
- **HR Chat**: Policies/benefits/payroll
- **General Chat**: Research/writing/general info

URLs use pattern: `https://amichat.prod.amivero-solutions.com/?model=<model-id>`

## Important Conventions

### File Naming
- Lowercase with hyphens: `seeds-of-bias`, `high-risk-horizon`
- No spaces, no uppercase
- Consistent across folders, files, and URLs

### Visual Elements
- Icons used extensively for UX (🎯 🔧 ✅ ❌ 📊 💬 etc.)
- Dividers: `═══` (major sections), `───` (subsections)
- Progress bars: `[██░░░] 40%`

### Tone & Style
- Concise, cinematic, mission-focused
- Professional but engaging
- Use "Agent" to address user
- Maintain spy-thriller aesthetic without being melodramatic

### Difficulty & Points
- Very Easy: ⭐ 10 points, 5-10 min, simple
- Easy: ⭐⭐ 15 points, 10-15 min, clear right/wrong
- Medium: ⭐⭐⭐ 20 points, 15-25 min, some nuance
- Hard: ⭐⭐⭐⭐ 25 points, 20-30 min, complex reasoning
- Impossible: ⭐⭐⭐⭐⭐ 30 points, over 30 min, challenging complex reasoning
  
## Documentation Reference

**Must-read for challenge development:**
- `docs/challenge-setup.md` - Universal components & templates
- `docs/challenge-architect-guide.md` - Complete development workflow
- `assets/README.md` - Asset guidelines & optimization
- `README.md` - Project overview & getting started

**Reference examples:**
- Week 2 (Trust Fall) challenges - Mature implementations
- Week 4 (Directive Zero) challenges - Well-structured examples
- Week 5 (Firewall) challenges - Security-focused patterns

## Git Workflow

Standard workflow:
```bash
git status                    # Check current state
git add <files>              # Stage changes
git commit -m "message"      # Commit with descriptive message
git push                     # Push to remote
```

Recent migrations:
- Campaign manifests migrated from individual YAML files to consolidated JSON (campaign-manifest.json)
- Images converted from PNG to WebP for optimization

## Special Considerations

### Security & Privacy
- No credentials or API keys in code/prompts
- Challenges simulate scenarios - use realistic but fictional data
- Educational focus - teach security awareness, not enable exploits

### Accessibility
- All images should have descriptive alt text
- Visual elements supplemented with text descriptions
- Progress communicated through multiple channels (visual + text)

### Content Diversity
- Rotate contexts across industries, roles, demographics
- Avoid reinforcing stereotypes in scenarios
- Use realistic, documented cases for educational value

## Support & Resources

- **Issues**: https://github.com/anthropics/claude-code/issues
- **Project**: Open source by Amivero (https://amivero.com)
- **License**: Apache 2.0

## Quick Commands Summary

```bash
# Sanitize markdown for Open WebUI
./clean.sh

# Convert images to WebP
python3 scripts/png_to_webp_and_delete.py --dry-run
python3 scripts/png_to_webp_and_delete.py

# Find challenge prompts
find campaign/weeks -name "prompt.md"

# Find quiz files
find campaign/weeks -name "quiz.json"

# Check manifest structure
cat campaign/catalog.json
cat campaign-manifest.json
```

## Development Workflow Summary

1. **Plan**: Review weekly theme, define learning objectives, choose difficulty
2. **Create**: Build challenge structure, write system prompt following templates
3. **Asset**: Create/optimize banners, reference shared assets appropriately
4. **Sanitize**: Run `./clean.sh` on prompt.md
5. **Test**: Deploy to Open WebUI, run full test protocol
6. **Document**: Update manifests, create README
7. **Deploy**: Verify in production environment
8. **Iterate**: Monitor usage, refine based on feedback
