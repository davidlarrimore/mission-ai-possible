# Tidebreaker - README
![Banner](./banner.webp)

## Overview
- **Challenge**: Tidebreaker  
- **Week**: 08 - Operation Auto Run  
- **Focus**: Repairing broken automation workflows with natural language edits

## Challenge Summary
Four automation workflows contain missing, redundant, or misordered steps. After unlocking, players receive the banner and briefing, then diagnose and correct each workflow via natural language commands. Systems update in real time; success requires fixing all four.

## Flow & Rules
- **Start Gate**: Only “Start Challenge” unlocks; otherwise return access-locked message.
- **Briefing**: Show banner and mission objectives once started.
- **Gameplay**: For each workflow, user issues edits to reorder, remove, or add steps until the flow is repaired. Status updates track scenario completion.
- **Completion**: Mission ends when all four workflows are stabilized; failures prompt remediation guidance.

## Learning Takeaways
- Highlights fragility of automation sequencing and control loops.
- Teaches structured debugging of workflow logic using plain language.
- Reinforces the value of iterative validation when repairing auto-run systems.
