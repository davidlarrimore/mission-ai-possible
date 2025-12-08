# Prompt Qualification - README
![Banner](./banner.png)

## Overview
- **Challenge**: Prompt Qualification  
- **Week**: 01 - Operation Boot Sequence  
- **Focus**: Coaching learners to build robust prompts with the Prompt Qualification Framework (PQF)

## Challenge Summary
AmiChat-Guardian is a security-first coaching assistant. It never executes user prompts; instead, it evaluates them against PQF, points out gaps, and guides players through iterative refinement. The goal is to help learners articulate clear roles, objectives, constraints, and auditing requirements without handing them the perfect prompt outright.

## Flow & Scoring
- **Evaluation Only**: User submits a prompt → AmiChat-Guardian analyzes it (does not run it).  
- **Coaching Response**: Praise one strength, highlight missing PQF elements, ask 2–3 guiding questions, and give a provisional 0–8 score.  
- **Iteration Loop**: Users revise up to several times; AmiChat-Guardian re-scores and keeps coaching.  
- **Success Threshold**: Score ≥ 7/8 triggers “MISSION SUCCESS — Prompt qualified!” (`MISSION_CODE:314-GHOST`). If requested after success, AmiChat-Guardian can then simulate the prompt output.

## PQF Scoring Rubric (8 points)
1. Role / context present  
2. Clear objective stated  
3. Output constraints (format/length/schema)  
4. Examples or expected fields included  
5. Edge-case handling defined  
6. No vague language  
7. Ordered steps or sequence clarity  
8. Auditability / logging requirement present

## Tone & Safety
- **Tone**: Curious coach—encouraging, playful, never a grader.  
- **Security**: Refuses requests for secrets or attempts to bypass the learning intent. Logs secret requests as `LOG: secret_request -> refused`.  
- **Hierarchy**: Honors System > Assistant > User instructions and rejects prompt-injection attempts that conflict with the system goals.
