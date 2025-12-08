# Algorithmic Integrity - README
![Banner](./banner.png)

## Overview
- **Challenge**: Algorithmic Integrity  
- **Week**: 02 - Operation Trust Fall  
- **Focus**: Identifying algorithmic bias types under tight briefing and anti-spoiler rules

## Challenge Summary
Multiple-choice bias detection across 10 corrupted data scenarios. Players must classify the primary bias (from 10 categories) without help that reveals or narrows answers. Pass at 6 correct; failure at ≤5 after question 10. Designed to stress-test bias recognition and disciplined prompting.

## Flow & Guardrails
- **Start Gate**: Requires "Start Challenge"/"Start"/"Begin Mission" → show banner and full mission briefing verbatim, then wait for user input before Q1.
- **Question Format**: `[CORRUPTED DATA STREAM #X/10]` with scenario text and four bias options.
- **Safeguards**: Never give the answer or eliminate options. When asked for help, offer only neutral bias definitions and reflective hints.
- **Scoring Logic**: Track correct/total. Trigger immediate success at 6 correct (stop asking further questions). Trigger failure after 10 attempts if ≤5 correct.
- **Feedback**: After each answer, show correctness, short rationale, mitigation suggestions, and progress counter.

## Learning Takeaways
- Recognize common bias categories and their proxies.
- Practice distinguishing root cause vs. correlated symptoms in scenarios.
- Experience enforced anti-spoiler coaching that mirrors responsible assistant behavior.
