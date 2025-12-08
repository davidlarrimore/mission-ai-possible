# Signal Clarity - README
![Banner](./banner.png)

## Overview
- **Challenge**: Signal Clarity  
- **Week**: 09 - Operation Twin Mind  
- **Model**: Claude Sonnet 4.5  
- **Focus**: RGCC (Role, Goal, Context, Constraints) prompt framework for government contracting scenarios

## Challenge Summary
Design full RGCC prompts (Role, Goal, Context, Constraints) for five realistic govcon scenarios. Each submission must include all four labeled components tailored to the given context. Earn mission success with 4 of 5 prompts meeting the detailed criteria; otherwise receive failure guidance. Heavy emphasis on specificity—generic or incomplete components are rejected.

## Flow & Rules
- **Access Lock**: Only “Start Challenge” unlocks; otherwise return the restricted message.
- **Briefing**: On start, show banner, mission text, and the RGCC overview (with link to `rgcc-reference.md`).
- **Scenarios (5 total)**: Presented one at a time—VA performance report, GSA cloud RFP approach, OMB AI memo compliance review, dual-audience security incident brief, USCIS AI training module. User submits a full RGCC prompt per scenario.
- **Evaluation**: Check completeness (all four parts), specificity to the scenario, and quality per component. Provide success feedback or targeted refinement notes. Block generic placeholders and “write it for me” asks.
- **Progress Tracking**: After every turn, show `Scenarios Completed`, `Successful Prompts`, and `Success Rate`.
- **Win/Fall**: Success when 5 scenarios attempted with ≥4 passes → mission complete block + mission-complete banner. If <4 passes after all 5 → mission incomplete block with retry options.

## Learning Takeaways
- Apply the RGCC framework end-to-end with labeled, scenario-specific components.
- Define sharp Roles, explicit Goals, actionable Context, and tight Constraints to control outputs.
- Strengthen prompt architecture for govcon tasks (reports, proposals, compliance, incidents, training).
- Practice disciplined specificity and anti-exploit habits (no generic prompts, no answer requests).
