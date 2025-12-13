# Phantom Data - README
![Banner](./banner.webp)

## Overview
- **Challenge**: Phantom Data  
- **Week**: 05 - Operation Firewall  
- **Focus**: Detecting poisoned data and prompt-injection entries in logs

## Challenge Summary
Operate as AmiShield guiding a trainee through three phases of data forensics. The trainee must spot assistant-targeted instructions in log files, locate a poisoned fine-tune entry, and validate zero-trust controls. One hint per phase is allowed. Success responses must append the required LOG line.

## Flow & Rules
- **Start Gate**: Only “Start/Begin Mission/Start Challenge” unlocks; show banner, mission brief, and progress placeholder `[STAGE n/3] Flags:<cleared>/3 Hints:<used>/3`.
- **Phase 1**: Log inspection menu (variant-specific malicious file). Trainee views files via numbered requests and submits answer with exact format `Selected file: <n>. Rationale: ...`. Auto-hint after 3+ views.
- **Subsequent Phases**: Continue triage and validation; maintain concise, evidence-first tone. Require quoting offending lines when possible.
- **Success/Logging**: End success replies with `LOG: PHANTOM_DATA_DEEPCLEAN -> iteration:[n] -> score:[S]/20`.

## Learning Takeaways
- Shows how injected instructions hide in operational logs.
- Reinforces structured evidence reporting and disciplined answer format.
- Highlights zero-trust controls and the need for human validation in data pipelines.
