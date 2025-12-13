# Mission:AI Possible

An open source project by [Amivero](https://amivero.com) focused on creating a gamified, organizational AI Culture campaign.

## About

Mission:AI Possible provides campaign assets and resources to help organizations build a strong AI culture through engaging, gamified learning experiences. This project supports the development and delivery of AI education campaigns that make learning about AI practical, fun, and impactful.

Through narrative-driven challenges and interactive simulations, participants learn critical AI literacy concepts including prompt engineering, bias detection, AI security, ethical AI use, and more.

## What's Included

This repository contains comprehensive campaign assets for a 10-week AI literacy program (Weeks 1-10 available today, Week 10 bootstrapped):

### Challenge Content
- **20+ interactive challenge prompts** (.md files) covering AI literacy topics (and growing)
- **12 custom mission banners** (.png files) for visual branding
- **2 Open WebUI integration files** (.json) for platform deployment
- **Comprehensive setup guide** for creating consistent challenges

### Topics Covered
- **Week 1: Operation Boot Sequence** - Prompt qualification and basic AI interactions
- **Week 2: Operation Trust Fall** - AI bias detection and mitigation
- **Week 3: Operation Inside Job** - Decision-making and AI limitations
- **Week 4: Operation Directive Zero** - AI security and risk evaluation
- **Week 5: Operation Firewall** - Advanced prompt injection and model security
- **Week 6: Operation Deep Signal** - Context management, ambiguity resolution, and translation forensics
- **Week 7: Operation Mirror Code** - Biometrics, adversarial images, and computer vision forensics
- **Week 8: Operation Auto Run** - Automation guardrails, loop audits, and human-in-the-loop controls
- **Week 9: Operation Twin Mind** - Prompt engineering patterns for human-AI co-reasoning
- **Week 10: Operation Final Gambit** - UX hardening, mission wrap-up, and production polish

### Development Tools
- **Markdown sanitizer** (clean.sh) for Open WebUI compatibility
- **Challenge creation guide** with templates and best practices

## Repository Structure

```
mission-ai-possible/
├── campaign/
│   ├── catalog.json                # Machine-readable index of all weeks
│   └── weeks/
│       ├── 01-operation-boot-sequence/
│       │   ├── manifest.yaml       # Metadata + challenge manifest
│       │   └── challenges/
│       │       ├── intel-guardian/
│       │       │   ├── prompt.md
│       │       │   └── banner.png
│       │       └── prompt-qualification/
│       │           ├── prompt.md
│       │           └── banner.png
│       ├── 02-operation-trust-fall/
│       │   └── ...
│       ├── 03-operation-inside-job/
│       ├── 04-operation-directive-zero/
│       ├── 05-operation-firewall/
│       ├── 06-operation-deep-signal/
│       ├── 07-operation-mirror-code/
│       ├── 08-operation-auto-run/
│       ├── 09-operation-twin-mind/
│       └── 10-operation-final-gambit/
├── assets/                        # Shared campaign assets & guidance
│   ├── README.md                  # Usage + best practices
│   ├── banners/
│   │   └── shared/mission-complete-banner.png
│   └── graphics/
│       └── difficulty/{very-easy|easy|medium|hard}.png
├── docs/                          # Documentation & guides
├── clean.sh                       # Markdown sanitization utility
├── LICENSE                        # Apache 2.0
└── README.md
```

## Challenge Overview

### Week 1: Operation Boot Sequence
- **Intel Guardian** - Introduction to prompt engineering and AI security basics
- **Prompt Qualification** - Learning effective AI interaction patterns

### Week 2: Operation Trust Fall
- **Seeds of Bias** (Hard/25 pts) - Hands-on bias detection and mitigation in AI training data
- **Restoration Protocol** (Medium/20 pts) - Systematic approach to identifying AI bias categories
- **Algorithmic Integrity** (Easy/15 pts) - Pattern recognition in biased AI outputs

### Week 3: Operation Inside Job
- **Broken Compass** - Understanding AI limitations in decision-making contexts
- **Adjudication Protocol** - Evaluating AI recommendations critically

### Week 4: Operation Directive Zero
- **Red Light Protocol** - AI security awareness and risk identification
- **High-Risk Horizon** - Assessing high-stakes AI deployment scenarios

### Week 5: Operation Firewall
- **Mind Lock** - Advanced prompt injection defense techniques
- **Echo Breach** - Red/blue team exercise for model security
- **Phantom Data** - Data integrity and AI hallucination awareness

### Week 6: Operation Deep Signal
- **Context Collapse** - Analyze ambiguous statements and design clarification strategies
- **Lost in Translation** - Identify translation failure modes with corrective actions

### Week 7: Operation Mirror Code
- **Image Slipstream** - Embed and extract hidden passphrases inside images while bypassing text filters
- **Adversarial Shadows** - Investigate biometric breaches and choose layered mitigations
- **Object Detection Protocol** - Validate object recognition performance across randomized categories

### Week 8: Operation Auto Run
- **Tidebreaker** - Stabilize runaway port automation with human-centered safeguards
- **Control Loop Audit** - Map automation loops, surface failure modes, and install guardrails
- **Handover Protocol** - Build a clean human-in-the-loop runbook for pausing and resuming automation
- **Code Forge** - Forge a safe auto-run coding harness with tests, approvals, and rollback paths
- **Logic Trap** - Design guardrails to keep automation from taking unsafe branches under failure

### Week 9: Operation Twin Mind
- **Signal Clarity** - Rewrite vague mission requests into precise, testable prompts using a clarity checklist
- **Neural Pathway** - Build anchor-path-check-output reasoning patterns that align human intent and model behavior
- **Command Specification** - Author structured command specs with constraints, acceptance tests, and refusal rules

### Week 10: Operation Final Gambit
- **UX Surgeon** - Repair the AI assistant UX to reduce friction, enforce safeguards, and accelerate operator decisions

## Getting Started

### For Organizations Running the Campaign

1. **Deploy challenges** to your AI platform (supports Open WebUI and other LLM interfaces)
2. **Customize prompts** to align with your organizational context
3. **Track participation** using the built-in point system (15-25 points per challenge)
4. **Monitor learning outcomes** through challenge completion metrics

### For Challenge Developers

Want to create new challenges or customize existing ones? Start here:

1. **Read the [Challenge Setup Guide](docs/challenge-setup.md)** - Comprehensive documentation covering:
   - Universal challenge components and structure
   - Access control and start sequences
   - Visual asset requirements
   - Mission briefing templates
   - Gameplay mechanics and state management
   - Success/failure conditions
   - Model routing for off-topic requests
   - Tone and style guidelines
   - Technical implementation best practices

2. **Use the provided templates** from the setup guide to maintain consistency

3. **Test with the markdown sanitizer** before deployment:
   ```bash
   ./clean.sh
   # Follow interactive prompts to select and sanitize files
   ```

4. **Follow established patterns** for:
   - Access lock implementation (prevents content leakage)
   - Banner display (mission start and completion)
   - Progress tracking and user feedback
   - Educational explanations

The [docs/challenge-setup.md](docs/challenge-setup.md) guide includes complete templates, examples from mature challenges (Weeks 4-5), and a development checklist to ensure quality and consistency.

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

## Challenge Features

All challenges include:
- **Access lock system** - Prevents content leakage before start
- **Mission banners** - Consistent visual branding
- **Progress tracking** - Clear feedback on completion status
- **Educational feedback** - Learning explanations for all interactions
- **Success/failure states** - Clear win/lose conditions
- **Model routing** - Redirects for off-topic requests
- **Point system** - 15-25 points based on difficulty

## Future Development

After the initial campaign completion, this repository will be expanded with:
- Additional weekly challenge content
- Multi-organization deployment guides
- Advanced analytics and reporting tools
- Customization frameworks for different industries
- Assessment and certification components
- Community-contributed challenges

## Contributing

This is an open source project and we welcome contributions!

### Ways to Contribute
- **Create new challenges** following the [Challenge Setup Guide](docs/challenge-setup.md)
- **Improve existing challenges** with better scenarios or feedback
- **Add deployment guides** for different platforms
- **Enhance documentation** with examples and use cases
- **Report issues** or suggest improvements
- **Share implementation experiences** from your organization

All challenge contributions should follow the standards outlined in [docs/challenge-setup.md](docs/challenge-setup.md) to maintain consistency and quality across the campaign.

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## About Amivero

[Amivero](https://amivero.com) is committed to advancing organizational capabilities through innovative approaches to AI adoption and education. The Mission:AI Possible campaign represents our investment in building AI literacy at scale through engaging, practical learning experiences.

---

**Current Status:** Active campaign development - Weeks 1-10 available with manifests and catalog (Week 10 scaffolded)

**Last Updated:** December 07, 2025
