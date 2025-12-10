# 🧾 CHEAT SHEET — CRISP vs. Chain of Thought vs. RGCC

## 1. CRISP Framework

**C**ontext • **R**ole • **I**nstructions • **S**teps • **P**references

**Purpose:** A complete prompt structure that gives models everything they need up front.

**Use when:**
- You want consistently high-quality outputs
- Tasks require multiple moving parts
- You want to embed tone, formatting, and workflow preferences

**Template:**
- Context: [Background the model needs]
- Role: [Who the model should act as]
- Instructions: [What you want produced]
- Steps: [How to approach it]
- Preferences: [Tone, format, limits, style]

**Strengths:**
- Reduces ambiguity
- Works for almost any task
- Ensures repeatability

## 2. Chain of Thought (CoT)

**Purpose:** A reasoning *mode*, not a format. It instructs the model to show intermediate steps.

**Use when:**
- Problem solving, logic, math
- Strategic planning
- Root cause analysis
- Multi-stage evaluations

**Template:**
- Think step-by-step. Show your reasoning before your final answer.

**Strengths:**
- Increases accuracy on complex tasks
- Encourages deliberate reasoning

## 3. RGCC — Role + Goal + Context + Constraints

**Purpose:** A streamlined operational framework that keeps AI tightly aligned with boundaries and outcomes.

**Use when:**
- You need high controllability
- You’re automating workflows
- You’re giving procedural guidance
- You need compliance guardrails

**Template:**
- Role: [Identity]
- Goal: [The desired outcome]
- Context: [Relevant background]
- Constraints: [Rules, limits, safeguards]

**Strengths:**
- Fantastic for enterprise, agents, and reproducible tasks
- Clear scope and boundaries
- Less verbose than CRISP

## Quick Comparison Table

| Framework        | Best For                      | Level of Structure   | Why Use It                           |
|------------------|-------------------------------|----------------------|--------------------------------------|
| CRISP            | General-purpose prompts       | High                 | Ensures clarity & consistency        |
| Chain of Thought | Complex reasoning             | Medium               | Boosts accuracy by forcing reasoning |
| RGCC             | Operational tasks, automation | Medium–High          | Tight control + explicit guardrails  |

## 🖼️ ONE-PAGE VISUAL — “The Prompt Engineering Trio”

You can paste this directly into a slide or document:

```
THE THREE ESSENTIAL PROMPT FRAMEWORKS

┌─────────────────────────────────────────────────────────────┐
│                           CRISP                             │
│─────────────────────────────────────────────────────────────│
│ C = Context        (What background is relevant?)           │
│ R = Role           (Who should the AI be?)                  │
│ I = Instructions   (What do you want?)                      │
│ S = Steps          (How should it work through the task?)   │
│ P = Preferences    (Tone, format, style, constraints)       │
│ Use for: Clear, stable, repeatable results                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                     CHAIN OF THOUGHT                        │
│─────────────────────────────────────────────────────────────│
│ A reasoning technique: “Think step-by-step.”                │
│ Enhances: Logic • planning • math • deep analysis           │
│ Use for: Complex reasoning or multi-step tasks              │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│                ROLE + GOAL + CONTEXT + CONSTRAINTS          │
│─────────────────────────────────────────────────────────────│
│ Role: Identity of the model                                 │
│ Goal: Clear desired outcome                                 │
│ Context: Background needed                                  │
│ Constraints: Rules & boundaries                             │
│ Use for: Operational tasks, agents, workflow automation     │
└─────────────────────────────────────────────────────────────┘

✔ CRISP = Most complete structure
✔ Chain of Thought = Deep reasoning mode
✔ RGCC = Tight control & guardrails
```
