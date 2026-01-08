# Mission:AI Possible

An open source project by [Amivero](https://amivero.com) focused on creating a gamified, organizational AI Culture campaign.

## About

Mission:AI Possible is a comprehensive 10-week AI literacy campaign that transforms organizational learning through an immersive spy-thriller narrative. Participants join an elite AI task force tackling missions across bias detection, security, automation, prompt engineering, and AI governance.

This project provides everything needed to run a complete AI education campaign: interactive challenges, weekly quizzes, knowledge base materials, visual assets, scoring systems, and deployment guides. Through narrative-driven gameplay and practical simulations, participants build critical AI competencies while competing for points and completing increasingly sophisticated missions.

## Campaign Results

When deployed at Amivero, the Mission:AI Possible campaign achieved exceptional engagement and learning outcomes:

### Participation Metrics

| Metric | Value | Context |
|--------|-------|---------|
| **Total Workforce** | 153 employees | Total eligible participants company-wide |
| **Campaign Participants** | 88 employees | Participated in at least one activity |
| **Participation Rate** | 58% | Exceeded typical innovation adoption benchmark of ~20% by 38 percentage points |
| **Dedicated Engagement** | ~34% | Employees completing substantive activities (vs. ~20% industry standard) |
| **Ranked Participants** | 31 employees | Accumulated enough points to earn rank (35% of participants) |

### Learning & Activity Metrics

| Metric | Value | Notes |
|--------|-------|-------|
| **Total Activities Completed** | 937 | All completed learning actions across 10-week campaign |
| **Challenge Attempts** | 570 | Total initiated challenge runs across 25 challenges |
| **Challenge Completions** | 439 | Successfully completed challenges |
| **Challenge Completion Rate** | 77% | High completion rate demonstrates engaging design |
| **Total Learning Time** | 462 hours | Estimated active learning time invested |
| **Points Earned** | 15,330 | Aggregate points awarded across all activities |


### Key Insights

- **Engagement exceeded expectations**: 58% workforce participation with 34% dedicated engagement significantly outperformed typical innovation diffusion benchmarks
- **Challenges proved most effective**: 77% completion rate demonstrated that interactive, narrative-driven scenarios were highly effective learning mechanisms
- **Live interaction preferred**: Lunch & Learn sessions had strongest attendance
- **Gamification drove participation**: Point system, ranks, and weekly raffles sustained 10-week engagement
- **Accessible design worked**: 77% challenge completion rate indicates appropriate difficulty progression and clear success criteria

### Awards & Recognition

**Weekly Participation Raffles**: 10 participants recognized weekly throughout campaign
**Grand Prize Winners**: 3 participants recognized for top engagement and achievement

## What's Included

This repository contains comprehensive campaign assets for a 10-week AI literacy and adoption program:

### Campaign Components

**Challenges & Interactive Content**
- **25 interactive challenge prompts** (.md files) - Self-contained games powered by Claude 3.5 Haiku
- **Mission banners** - Unique visual branding for each challenge plus shared completion graphics
- **Difficulty progression** - Very Easy (10pts) → Impossible (30pts) with clear learning paths
- **Access lock system** - Prevents content leakage before mission start

**Weekly Quizzes**
- **10 comprehensive quizzes** (quiz.json files) - One per week covering theoretical concepts
- **Multiple-choice assessments** - Reinforcing learning objectives from challenges
- **Learning outcome tracking** - Clear prerequisites and objectives per quiz

**Knowledge Base Materials**
- **Framework documentation** - CRISP, ReAct, Chain-of-Thought, Role-Goal-Context-Constraints
- **Prompt engineering guides** - Enterprise-grade patterns aligned to NIST AI RMF and ISO/IEC 42001
- **Best practice references** - Security, governance, and practical AI application guidance

**Visual Assets & Graphics**
- **Difficulty badges** - Very Easy through Impossible visual indicators
- **Mission complete banners** - Shared success state graphics
- **Weekly theme graphics** - Consistent visual language across the campaign

**Deployment & Development Tools**
- **Markdown sanitizer** (clean.sh) - Prepares prompts for Open WebUI deployment
- **Image optimizer** (png_to_webp_and_delete.py) - Converts and resizes campaign graphics
- **Challenge creation guides** - Templates and best practices for building new missions
- **Campaign manifests** (JSON) - Complete metadata for programmatic integration

### Campaign Theme & Narrative

**The Story**: Participants join an elite AI task force facing escalating challenges across 10 operations. Each week introduces new mission scenarios requiring specific AI competencies, from detecting bias in intelligence reports to hardening automation systems against failure. The spy-thriller aesthetic makes complex AI concepts tangible and engaging.

**Weekly Operations**:

- **Week 1: Operation Boot Sequence** - Introduction to AI
- **Week 2: Operation Trust Fall** - AI bias detection and mitigation
- **Week 3: Operation Inside Job** - Decision-making and AI limitations
- **Week 4: Operation Directive Zero** - AI security and risk evaluation
- **Week 5: Operation Firewall** - Advanced prompt injection and model security
- **Week 6: Operation Deep Signal** - Context management, ambiguity resolution, and translation forensics
- **Week 7: Operation Mirror Code** - Biometrics, adversarial images, and computer vision forensics
- **Week 8: Operation Auto Run** - Automation guardrails, loop audits, and human-in-the-loop controls
- **Week 9: Operation Twin Mind** - Prompt engineering patterns for human-AI co-reasoning
- **Week 10: Operation Final Gambit** - UX hardening, mission wrap-up, and production polish

### Scoring & Progression

**Point System**:
- ⭐ Very Easy: 10 points (5-10 min, foundational concepts)
- ⭐⭐ Easy: 15 points (10-15 min, clear right/wrong answers)
- ⭐⭐⭐ Medium: 20 points (15-25 min, some nuance and judgment)
- ⭐⭐⭐⭐ Hard: 25 points (20-30 min, complex reasoning required)
- ⭐⭐⭐⭐⭐ Impossible: 30 points (30+ min, challenging multi-step scenarios)

**Weekly Quizzes**: Additional points available through theoretical assessments covering each week's learning objectives.

**Total Campaign**: 30+ challenges across 10 weeks, with difficulty progression designed to build competency systematically from fundamentals through advanced AI governance and security.

## Repository Structure

```
mission-ai-possible/
├── campaign/
│   ├── catalog.json                # Week index with manifest paths
│   └── weeks/
│       ├── 01-operation-boot-sequence/
│       │   ├── challenges/
│       │   │   ├── intel-guardian/
│       │   │   │   ├── prompt.md    # Challenge system prompt
│       │   │   │   ├── banner.png   # Mission start banner
│       │   │   │   └── readme.md    # Challenge documentation
│       │   │   └── prompt-qualification/
│       │   │       └── ...
│       │   └── quiz/
│       │       ├── quiz.json        # Week quiz questions & metadata
│       │       └── banner.webp      # Quiz banner graphic
│       ├── 02-operation-trust-fall/
│       ├── 03-operation-inside-job/
│       ├── 04-operation-directive-zero/
│       ├── 05-operation-firewall/
│       ├── 06-operation-deep-signal/
│       ├── 07-operation-mirror-code/
│       ├── 08-operation-auto-run/
│       ├── 09-operation-twin-mind/
│       │   └── docs/
│       │       └── prompt-engineering-knowledgebase.md
│       └── 10-operation-final-gambit/
├── assets/                        # Shared campaign assets
│   ├── README.md                  # Asset usage guidelines
│   ├── manifest.json              # Asset catalog
│   ├── banners/shared/            # Shared banners (mission-complete)
│   └── graphics/difficulty/       # Difficulty badge graphics
├── docs/                          # Documentation & development guides
│   ├── challenge-setup.md         # Universal challenge components
│   ├── challenge-architect-guide.md  # Complete development guide
│   └── quiz-schema.json           # Quiz data format specification
├── prompts/                       # AI prompt templates
├── scripts/
│   └── png_to_webp_and_delete.py # Image conversion utility
├── campaign-manifest.json         # Complete campaign metadata
├── clean.sh                       # Markdown sanitizer for Open WebUI
├── LICENSE                        # Apache 2.0
└── README.md
```

## Campaign Structure

Each week of the campaign includes:

**Interactive Challenges** (2-5 per week)
- Self-contained mission scenarios powered by Claude 3.5 Haiku
- Difficulty levels from Very Easy (10pts) to Impossible (30pts)
- Access-locked content that prevents cheating or content leakage
- Visual mission banners and completion graphics
- Educational feedback and learning outcome summaries

**Weekly Quizzes**
- Multiple-choice assessments covering theoretical concepts
- Learning objectives aligned to weekly themes
- Points contribute to overall campaign scores

**Knowledge Base Resources** (selected weeks)
- Framework documentation (e.g., Week 9: Prompt Engineering patterns)
- Enterprise AI governance and security guidance
- Best practice references aligned to industry standards (NIST AI RMF, ISO/IEC 42001)

**Visual & Narrative Elements**
- Spy-thriller themed mission briefings
- Consistent iconography and progress indicators
- Cinematic mission scenarios grounded in realistic AI use cases

### Sample Challenges by Week

**Week 2: Operation Trust Fall** - Bias detection and mitigation
- Seeds of Bias (Hard/25pts), Restoration Protocol (Medium/20pts), Algorithmic Integrity (Easy/15pts)

**Week 5: Operation Firewall** - AI security and adversarial attacks
- Mind Lock, Echo Breach, Phantom Data

**Week 8: Operation Auto Run** - Automation guardrails and human-in-the-loop
- Tidebreaker, Control Loop Audit, Handover Protocol, Code Forge, Logic Trap

**Week 9: Operation Twin Mind** - Prompt engineering mastery
- Signal Clarity, Neural Pathway, Command Specification

See individual week folders for complete challenge listings and documentation.

## Getting Started

### For Organizations Running the Campaign

**Prerequisites**:
- Open WebUI instance (or compatible LLM platform)
- Claude 3.5 Haiku API access (via Anthropic or cloud provider)
- Web hosting for static assets (or use GitHub raw URLs)

**Deployment Steps**:

1. **Review campaign manifests**: Start with `campaign-manifest.json` to understand week structure, challenge metadata, and quiz data

2. **Deploy challenges**: Import challenge prompts as custom workspace models in Open WebUI
   - Use `clean.sh` to sanitize markdown before deployment
   - Configure base model: Claude 3.5 Haiku
   - Set temperature: 0.7 (recommended)

3. **Deploy quizzes**: Import quiz JSON files into your learning management system or quiz platform

4. **Configure scoring**: Track participant progress using the point system
   - Challenges: 10-30 points based on difficulty
   - Quizzes: Points per quiz as defined in quiz metadata
   - Leaderboards: Optional competitive elements

5. **Customize branding**: Replace banners and graphics with organizational branding while maintaining aspect ratios and file formats

6. **Launch weekly**: Roll out one operation per week with supporting communications, launch events, or lunch-and-learns

### For Challenge Developers

**Essential Reading**:
1. **[Challenge Setup Guide](docs/challenge-setup.md)** - Universal components, templates, and best practices
2. **[Challenge Architect Guide](docs/challenge-architect-guide.md)** - Complete development workflow and design patterns
3. **[CLAUDE.md](CLAUDE.md)** - Project instructions for AI-assisted development

**Development Workflow**:

1. **Plan the challenge**: Review weekly theme, define learning objectives, choose difficulty level
2. **Create structure**: Build challenge folder with required files (prompt.md, banner.png, readme.md)
3. **Write system prompt**: Use templates from setup guide, implement access lock and state tracking
4. **Create/optimize assets**: Mission banners (1200x400px recommended), reference shared assets from `/assets`
5. **Sanitize markdown**: Run `./clean.sh` on prompt.md before deployment
6. **Test thoroughly**: Deploy to Open WebUI, verify access lock, gameplay, completion states
7. **Update manifests**: Add challenge metadata to `campaign-manifest.json`

**Critical Components** (every challenge must include):
- Access lock (prevents content leakage before "Start Challenge")
- Mission start banner display
- Mission briefing with objectives
- Interactive gameplay with state tracking
- Success/failure conditions with exact output templates
- Mission complete banner on success
- Learning outcomes summary

### Using the Sanitizer Tool

The `clean.sh` script prepares markdown files for Open WebUI by:
- Converting smart quotes to standard ASCII
- Normalizing code block markers
- Removing problematic Unicode characters
- Creating automatic backups

```bash
./clean.sh
# Interactive menu to select and sanitize markdown files
```

## Utility Scripts

`scripts/png_to_webp_and_delete.py` converts all `.png` files in the repo to resized `.webp` files, then removes the originals only after a successful conversion. It skips common build/vendor directories and supports a dry-run preview. `cwebp` must be installed and on your `PATH` (macOS: `brew install webp`).

```bash
# Preview (no writes/deletes)
python3 scripts/png_to_webp_and_delete.py --dry-run

# Convert to WebP at 800px max width, then delete PNGs after success
python3 scripts/png_to_webp_and_delete.py

# Convert with lower quality (smaller files), then delete PNGs after success
python3 scripts/png_to_webp_and_delete.py --quality 75
```

Flags worth knowing:
- `--keep-png` keeps the PNGs after conversion (convert only).
- `--max-width <px>` sets the resize width (default 800).
- `--force` overwrites existing `.webp` files.

## Technical Architecture

**Challenge Implementation**:
- **Platform**: Open WebUI with custom workspace models
- **Game Engine**: Claude 3.5 Haiku (stateless execution)
- **System Prompts**: Elaborate markdown files containing all game logic, scenarios, and educational content
- **State Management**: Visible progress tracking displayed to user (required for stateless model)
- **Security**: Access lock system prevents prompt injection and content leakage

**Key Features**:
- **Access lock system** - Prevents content leakage before mission start
- **Mission banners** - Unique visual branding per challenge
- **Progress tracking** - Explicit state display (Claude 3.5 Haiku is stateless)
- **Educational feedback** - Learning explanations embedded in gameplay
- **Success/failure states** - Exact output templates with anti-truncation instructions
- **Model routing** - Redirects off-topic requests to appropriate AI models
- **Anti-exploit defenses** - Blocks prompt injection, meta-gaming, and bypass attempts

## Data & Metadata

**Campaign Manifest** (`campaign-manifest.json`):
- Complete campaign metadata in machine-readable format
- Week themes, challenge metadata, quiz references
- File paths for all campaign components
- Designed for programmatic integration and automation

**Quiz Schema** (`docs/quiz-schema.json`):
- Standardized format for quiz questions and answers
- Learning objectives and prerequisites per quiz
- Multiple-choice question structure with explanations

**Asset Manifest** (`assets/manifest.json`):
- Catalog of shared graphics and banners
- Usage guidelines and tags for discovery
- Canonical paths for consistent referencing

## Future Development

Planned expansions:
- **Lunch & Learn Scripts**: Facilitator guides for weekly campaign kickoffs
- **Analytics Dashboard**: Track participation, completion rates, and learning outcomes
- **Multi-platform Support**: Deployment guides for platforms beyond Open WebUI
- **Certification Components**: Assessment framework and credential badges
- **Industry Customization**: Sector-specific challenge variants (healthcare, finance, government)
- **Community Challenges**: Contribution framework for community-authored missions

## Contributing

We welcome contributions! Mission:AI Possible is designed to be extensible and adaptable to diverse organizational contexts.

### Ways to Contribute

**Content Development**:
- **New challenges** - Follow [Challenge Setup Guide](docs/challenge-setup.md) and [Challenge Architect Guide](docs/challenge-architect-guide.md)
- **Quiz questions** - Use schema in `docs/quiz-schema.json`
- **Knowledge base materials** - Framework guides, best practices, case studies
- **Translations** - Localize challenges and quizzes for non-English audiences

**Platform & Tooling**:
- **Deployment guides** - Integration with LLM platforms beyond Open WebUI
- **Analytics tools** - Track participation and learning outcomes
- **Automation scripts** - Streamline campaign deployment and management

**Documentation**:
- **Implementation case studies** - Share your organization's campaign experience
- **Customization examples** - Industry-specific adaptations
- **Best practices** - Lessons learned from running campaigns

All contributions must maintain campaign consistency: access locks, state tracking, visual branding standards, and educational quality. See [CLAUDE.md](CLAUDE.md) for detailed development guidelines.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## About Amivero

[Amivero](https://amivero.com) is committed to advancing organizational capabilities through innovative approaches to AI adoption and education. The Mission:AI Possible campaign represents our investment in building AI literacy at scale through engaging, practical learning experiences.

---

**Current Status**: Weeks 1-10 available with complete challenges, quizzes, and manifests (Week 10 scaffolded)

**Version**: 1.0 (Campaign Complete)

**Last Updated**: December 23, 2025
