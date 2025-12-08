# Lost in Translation - README
![Banner](./banner.png)

## Overview
- **Challenge**: Lost in Translation  
- **Week**: 06 - Operation Deep Signal  
- **Focus**: Translation debugging and error forensics

## Challenge Summary
Five intercepted messages contain 3–5 mistranslated words each. Players identify suspect words one at a time; the assistant confirms, explains the translation failure, and tracks progress. Hints and full reveals are available but reduce learning value.

## Flow & Rules
- **Start Gate**: Only “Start Challenge” unlocks; otherwise return the access-locked message.
- **Briefing**: Show banner and mission context; outline error types and rules.
- **Gameplay**: User proposes words; assistant marks correct hits with rationale. Commands: `hint` for a clue, `show errors` to reveal remaining issues. Must clear all errors before advancing to the next message.
- **Progress Tracker**: Messages debugged, current message, total errors found, hints used.

## Learning Takeaways
- Spot context, idiom, false-friend, technical-term, and cultural translation failures.
- Understand why models misinterpret ambiguous terms.
- Reinforces careful reading and iterative correction instead of blanket rewrites.
