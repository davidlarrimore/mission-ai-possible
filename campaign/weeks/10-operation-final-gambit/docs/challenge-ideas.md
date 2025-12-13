# Week 10: Operation Final Gambit - Challenge Ideas
## Human-Centered AI Design & UX/IX/CX Focus

Based on the Week 10 knowledge base materials, here are challenge concepts that teach practical HCD and UX/CX principles for AI systems.

---

## Challenge 1: **Pattern Matcher**
**Type:** Interactive Pattern Selection / Decision Tree  
**Difficulty:** Easy (15 points)  
**Duration:** 10-15 minutes

### Concept
Users are presented with 5 different customer problems and must select the appropriate AI pattern from the catalog. This teaches the "start simple → mature" philosophy and pattern-to-problem matching.

### Learning Objectives
- Recognize when different AI patterns are appropriate
- Understand the maturity progression (deterministic → IDP → semantic search → RAG → etc.)
- Practice "fit the tool to the problem" instead of "use the coolest tech"

### Gameplay
1. Present a customer problem scenario
2. User selects from 5 pattern options (with descriptions)
3. Immediate feedback on why their choice was good/suboptimal
4. 5 scenarios total covering different contexts

### Example Scenarios
- **Scenario 1:** "Every morning we download reports, rename them, and upload to SharePoint"
  - Correct: Deterministic Automation (RPA)
  - Common mistake: RAG (over-engineering)

- **Scenario 2:** "We need to extract vendor names and invoice amounts from 500 PDF invoices daily"
  - Correct: Intelligent Document Processing (IDP)
  - Common mistake: Semantic Search (doesn't extract fields)

- **Scenario 3:** "Help desk agents need to find the right KB article for complex questions"
  - Correct: Semantic Search / Vector Search
  - Common mistake: Naive RAG Q&A (users prefer reading sources)

- **Scenario 4:** "Users ask open-ended questions about internal policies and need answers"
  - Correct: Naive RAG Q&A
  - Common mistake: Search-First Assistant (doesn't synthesize)

- **Scenario 5:** "Customers need simple answers to common questions from our FAQ"
  - Correct: Search-First Assistant
  - Common mistake: Full RAG (over-engineering)

### Why This Works
- Teaches practical pattern recognition
- Reinforces "simplest viable pattern" philosophy
- Directly applicable to their work
- Quick wins build confidence

---

## Challenge 2: **Maturity Ladder**
**Type:** Simulation / Sequencing Exercise  
**Difficulty:** Medium (20 points)  
**Duration:** 15-20 minutes

### Concept
Users are a solution architect for a government agency. They must sequence AI implementation from Level 0 (Foundation) → Level 3 (Transactional) by making decisions at each maturity gate. Wrong sequencing causes "deployment failures."

### Learning Objectives
- Understand AI Implementation Maturity Model (AIMM)
- Recognize why foundation work matters
- Practice risk-based sequencing
- Learn graduation criteria for each level

### Gameplay Structure
Players start at **Level 0** and must make 3 decisions at each level to "graduate" to the next:

**Level 0 - Foundation:**
- Decision 1: "Which content sources should we prioritize?"
- Decision 2: "Who owns the content governance workflow?"
- Decision 3: "What risk categories apply to citizen-facing responses?"

**Level 1 - Assisted Work:**
- Decision 1: "Which internal use case should we start with?"
- Decision 2: "What monitoring metrics do we need?"
- Decision 3: "When can we graduate to customer-facing?"

**Level 2 - Guided Self-Service:**
- Decision 1: "How do we ensure safe escalation?"
- Decision 2: "What topics are 'bounded' enough?"
- Decision 3: "What quality thresholds matter?"

**Level 3 - Transactional:**
- Decision 1: "Which transactions can be fully automated?"
- Decision 2: "What guardrails prevent harm?"
- Decision 3: "How do we measure ongoing quality?"

### Failure Conditions
- Skip foundation work → "Customer-facing failure: hallucinated policy citation"
- Deploy Level 3 before monitoring → "Undetected quality drift causes incorrect benefits denial"
- Wrong escalation logic → "Citizens stuck in loops, CSAT plummets"

### Success Condition
Successfully graduate through all 4 levels with working monitoring, governance, and safe customer outcomes.

### Why This Works
- Teaches systematic thinking about AI deployment
- Reinforces risk management principles
- Shows consequences of skipping steps
- Aligns with NIST AI RMF approach

---

## Challenge 3: **UX Surgeon**
**Type:** Design Critique / Repair Exercise  
**Difficulty:** Medium (20 points)  
**Duration:** 15-20 minutes

### Concept
Users are shown 5 "broken" AI UX designs (mockups or descriptions) and must identify what's wrong and suggest fixes using HCD principles.

### Learning Objectives
- Apply UX/UI best practices for AI systems
- Recognize common UX antipatterns
- Practice clarity, control, and transparency principles
- Understand human-centered explainability

### Example Broken Designs

**Design 1: The Overconfident Chatbot**
- Problem: AI says "The answer is..." with 100% confidence, no citations
- Issues: No uncertainty communication, no source attribution, no human control
- Fix: Add confidence indicators, source citations, "verify with human" option

**Design 2: The Black Box Recommender**
- Problem: System says "We recommend denying this claim" with no explanation
- Issues: No explainability, high-stakes decision, no human override
- Fix: Show reasoning ("because X, Y, Z"), require human review, allow override

**Design 3: The Invisible AI**
- Problem: AI-generated content not distinguished from human-written content
- Issues: Transparency violation, user can't calibrate trust
- Fix: Clear labeling, AI badge/watermark, show generation date

**Design 4: The Expert-Only Interface**
- Problem: Complex AI controls with no onboarding or help
- Issues: Not inclusive, assumes expertise, no progressive disclosure
- Fix: Adaptive help, tooltips, "simple/advanced" modes, contextual examples

**Design 5: The Authority Bot**
- Problem: AI makes final decisions in high-stakes scenarios
- Issues: No human control, wrong automation level, rights-impacting
- Fix: Change to "recommend + require human approval" pattern

### Gameplay Mechanics
1. Show design (mockup or detailed description)
2. User identifies 3 problems from provided list
3. User selects appropriate fixes from options
4. Immediate feedback with HCD principle explanation

### Scoring
- Identify all 3 problems: +4 points each
- Select optimal fix: +4 points each
- Total: 20 points possible

### Why This Works
- Visual/concrete examples easier than abstract principles
- Directly applicable to design reviews
- Reinforces "people + AI" thinking
- Teaches through critique (powerful learning mode)

---

## Challenge 4: **Risk Router**
**Type:** Decision Tree / Responsible AI Framework  
**Difficulty:** Medium (20 points)  
**Duration:** 15-20 minutes

### Concept
Using the Responsible AI Integration Decision Tree, users must classify 8 different AI use cases and determine the appropriate level of human oversight.

### Learning Objectives
- Apply risk-based decision framework
- Recognize rights/safety impacting scenarios
- Understand automation vs augmentation appropriateness
- Practice responsible AI governance

### Decision Tree Logic
```
Is the AI outcome rights or safety impacting?
├─ YES → Is outcome verifiable against ground truth?
│         ├─ YES → Human-in-command (human makes final decision)
│         └─ NO → Do not automate (too risky)
│
└─ NO → Is task well-bounded and low-variability?
          ├─ YES → Can automate with monitoring
          └─ NO → Human-in-the-loop (AI suggests, human decides)
```

### Example Use Cases to Classify

1. **USCIS Benefits Adjudication**
   - Rights impacting? YES
   - Verifiable? Partially
   - Correct: Human-in-command (AI assists, officer decides)

2. **Email Routing to Departments**
   - Rights impacting? NO
   - Well-bounded? YES
   - Correct: Automate with monitoring

3. **Medical Diagnosis Recommendations**
   - Rights impacting? YES
   - Verifiable? NO (complex, multi-factorial)
   - Correct: Do not automate

4. **Travel Report Expense Extraction**
   - Rights impacting? NO
   - Well-bounded? YES
   - Correct: Automate with monitoring

5. **Security Clearance Recommendations**
   - Rights impacting? YES
   - Verifiable? Partially
   - Correct: Human-in-command

6. **Customer Support FAQ Answers**
   - Rights impacting? NO
   - Well-bounded? YES
   - Correct: Automate with monitoring

7. **Loan Application Approval**
   - Rights impacting? YES
   - Verifiable? Partially
   - Correct: Human-in-command

8. **Creative Content Generation for Marketing**
   - Rights impacting? NO
   - Well-bounded? NO (creative, variable)
   - Correct: Human-in-the-loop

### Gameplay Mechanics
1. Present use case with context
2. User answers decision tree questions
3. User selects oversight level
4. Feedback explains why that level is appropriate
5. 8 scenarios total

### Why This Works
- Teaches systematic risk assessment
- Reinforces NIST AI RMF principles
- Practical framework they can use immediately
- Covers diverse government/corporate scenarios

---

## Challenge 5: **Metrics That Matter**
**Type:** KPI Selection / Success Measurement  
**Difficulty:** Medium (20 points)  
**Duration:** 15-20 minutes

### Concept
Users are given 4 different AI implementation scenarios and must select the right success metrics (before/after approach) from the knowledge base framework.

### Learning Objectives
- Define customer-centered success metrics
- Distinguish efficiency, quality, experience, and trust metrics
- Avoid vanity metrics
- Apply before/after measurement approach

### Framework Categories
**Efficiency Metrics:**
- Minutes saved per case
- Reduced handle time
- Reduced back-and-forth

**Quality Metrics:**
- Fewer errors
- Higher first-contact resolution
- Better compliance adherence

**Experience Metrics:**
- Higher CSAT/NPS
- Fewer escalations
- Reduced abandonment

**Risk/Trust Metrics:**
- Fewer policy violations
- Fewer unsafe outputs
- Better auditability
- Lower hallucination rate

### Example Scenarios

**Scenario 1: Agent Assist Copilot for USCIS Call Center**
- User selects 3-5 KPIs
- Optimal choices:
  - Efficiency: Average handle time (AHT) reduction
  - Quality: First-contact resolution rate
  - Trust: Policy violation rate
- Poor choices:
  - "AI usage rate" (vanity metric)
  - "Number of suggestions generated" (activity, not outcome)

**Scenario 2: RAG-based Policy Q&A for Citizens**
- Optimal choices:
  - Quality: Answer accuracy rate
  - Experience: Abandonment rate, CSAT
  - Trust: Hallucination/incorrect citation rate
- Poor choices:
  - "Response speed" (table stakes, not differentiator)
  - "Documents in index" (input, not outcome)

**Scenario 3: IDP for Invoice Processing**
- Optimal choices:
  - Efficiency: Processing time per invoice
  - Quality: Extraction accuracy, field error rate
  - Risk: Low-confidence flag rate
- Poor choices:
  - "PDFs processed" (volume, not outcome)

**Scenario 4: Semantic Search for Internal Knowledge**
- Optimal choices:
  - Efficiency: Time to find relevant document
  - Quality: Relevance score, click-through rate
  - Experience: User satisfaction, search abandonment
- Poor choices:
  - "Search queries executed" (usage, not success)

### Gameplay Mechanics
1. Present scenario with context
2. User selects 3-5 KPIs from 12 options
3. System scores based on category balance and outcome focus
4. Feedback explains why selections are strong/weak
5. Bonus for identifying "guardrail metrics"

### Why This Works
- Teaches outcome-focused thinking
- Reinforces customer-centered measurement
- Prevents "AI for AI's sake"
- Directly applicable to project planning

---

## Challenge 6: **The Four Questions**
**Type:** Fast Triage / Pattern Qualification  
**Difficulty:** Easy (15 points)  
**Duration:** 10-15 minutes

### Concept
Users practice the "fast triage" method from the knowledge base by answering four key questions for different customer problems to determine AI appropriateness.

### The Four Questions
1. Is the task **repetitive** or **variable**?
2. Is the input mostly **structured** (tables/fields) or **unstructured** (text/docs/calls)?
3. Do we need **authoritative truth** from customer content?
4. Does the system need to **take actions** or only **recommend/summarize**?

### Learning Objectives
- Quickly assess AI fit
- Recognize structured vs unstructured data implications
- Understand action vs recommendation distinction
- Practice problem framing

### Example Problems

**Problem 1: "We get 200 support emails daily asking the same 10 questions"**
- Repetitive (same questions)
- Unstructured (email text)
- Authoritative truth needed (company policies)
- Recommend/summarize (provide answers)
- → AI is appropriate (Search-First Assistant or Naive RAG)

**Problem 2: "Every invoice needs approval from 3 managers"**
- Repetitive (same approval flow)
- Structured (approval forms, fields)
- No authoritative truth needed (routing logic)
- Take action (route to managers)
- → AI appropriate but simple automation better (RPA/workflow)

**Problem 3: "We need creative marketing copy for unique client pitches"**
- Variable (each pitch unique)
- Unstructured (text)
- No authoritative truth (creative content)
- Recommend (drafts for review)
- → AI appropriate (LLM drafting with human review)

**Problem 4: "Process complex multi-factor medical diagnoses"**
- Variable (each patient unique)
- Mixed (structured + unstructured)
- Authoritative truth critical (medical evidence)
- Take action → NO (too risky)
- → AI NOT appropriate for automation (maybe decision support only)

**Problem 5: "Extract dates, amounts, vendors from 1000 identical invoice formats"**
- Repetitive (same format)
- Structured (consistent fields)
- Authoritative truth (exact extraction)
- Take action (populate database)
- → AI appropriate (IDP) or template-based extraction

### Gameplay Mechanics
1. Present problem
2. User answers all 4 questions
3. User makes "AI appropriate?" decision
4. Feedback explains reasoning
5. 6 problems total

### Why This Works
- Simple, repeatable framework
- Fast decision-making skill
- Prevents analysis paralysis
- Filters bad AI projects early

---

## Challenge 7: **Graduation Gates** (Advanced)
**Type:** Maturity Assessment / Quality Review  
**Difficulty:** Hard (25 points)  
**Duration:** 20-25 minutes

### Concept
Users are a governance lead reviewing an AI system trying to "graduate" from Level 1 (Assisted) → Level 2 (Customer-facing). They must audit the system against graduation criteria and make a go/no-go decision.

### Learning Objectives
- Apply maturity graduation criteria
- Understand quality gates
- Practice governance reviews
- Recognize deployment readiness

### Graduation Criteria (Level 1 → Level 2)
User must verify:
1. **Quality Metrics:** Stable quality for top intents
2. **Monitoring:** "I don't know" detection, low confidence tracking
3. **Failure Handling:** Safe escalation paths exist
4. **Guardrails:** Unsafe output prevention
5. **Documentation:** Operating procedures, runbooks
6. **Human Oversight:** Clear HITL workflows for edge cases

### Gameplay Scenario
**Context:** USCIS is moving their Agent Assist RAG system (internal) to customer-facing self-service for common visa questions.

**Provided Evidence:**
- Last 30 days metrics dashboard
- Sample conversations (good and bad)
- Escalation procedures doc
- Monitoring alerts log

**User Tasks:**
1. Review evidence for each criterion
2. Identify what's missing or concerning
3. Make go/no-go decision
4. Justify decision with specific evidence

### Example Evidence Issues
- **Quality:** Accuracy is 87% (below 90% threshold)
- **Monitoring:** No "I don't know" detection in place
- **Failure:** Escalation path exists but not tested
- **Guardrails:** No toxic content filter
- **Documentation:** Runbook is outdated
- **Oversight:** HITL process unclear for policy updates

### Correct Decision
**NO-GO** with specific remediation items:
1. Improve accuracy to 90%+ before customer deployment
2. Implement "I don't know" detection
3. Test escalation path with real scenarios
4. Add content safety filters
5. Update documentation
6. Formalize HITL procedures

### Scoring
- Identify all 6 criterion gaps: 3 points each
- Correct go/no-go decision: 5 points
- Quality of justification: 2 points

### Why This Works
- Teaches governance thinking
- Reinforces quality-first mindset
- Practical review skills
- Prevents premature deployment

---

## Challenge 8: **Problem→Solution Workshop** (Advanced)
**Type:** Design Exercise / Customer Engagement Simulation  
**Difficulty:** Hard (25 points)  
**Duration:** 25-30 minutes

### Concept
Users facilitate a simulated customer discovery workshop using the Step 1-4 framework from the knowledge base. They must frame the problem, define metrics, assess AI fit, and recommend a pattern.

### Learning Objectives
- Conduct customer discovery
- Apply human-centered design lifecycle
- Frame problems before solutions
- Make pattern recommendations

### Gameplay Structure

**STEP 1: Frame the Problem**
Customer says: "We want to use AI to make our call center better."

User must ask the right questions:
- Who is struggling? (agents? supervisors? customers?)
- Where in the workflow? (routing? answering? follow-up?)
- Why does it hurt? (time? errors? escalations?)
- What is "done"? (what does success look like?)
- What if we're wrong? (what's the risk?)

**System provides answers based on user's questions.**

Example good questions:
- "What specific pain point causes the most delays?"
- "How many calls end in escalation due to agents lacking info?"
- "What happens if the AI gives a wrong answer?"

Example bad questions:
- "What AI tools do you want?" (solution-first)
- "How many calls do you get?" (not outcome-focused)

**STEP 2: Define Success Metrics**
User must select 3-5 KPIs from options:
- Efficiency: AHT, handle time, call volume
- Quality: FCR, accuracy, compliance
- Experience: CSAT, NPS, abandonment
- Trust: error rate, policy violations

**STEP 3: Fast Triage**
User answers the 4 questions about the specific problem identified

**STEP 4: Pattern Recommendation**
User selects appropriate pattern and justifies why

### Example Customer Problem (revealed through questioning)
**Context:** USCIS call center agents spend 8 minutes per call searching for policy information across 50+ documents.

**Ideal User Journey:**
1. Questions reveal: agents struggling, during call, wastes time searching
2. Success: reduce search time to <2 minutes, maintain accuracy
3. Risk: if wrong, agent gives incorrect info → compliance violation
4. Triage: repetitive, unstructured, need truth, recommend only
5. Pattern: Semantic Search or RAG with citation requirements

### Scoring Rubric
- Asked problem-framing questions (not solution questions): 5 pts
- Identified correct metrics: 5 pts
- Correct triage assessment: 5 pts
- Appropriate pattern selection: 5 pts
- Strong justification: 5 pts

### Why This Works
- Simulates real customer engagement
- Teaches consultative approach
- Reinforces entire framework
- Builds discovery skills

---

## Challenge 9: **Experience Audit**
**Type:** Heuristic Evaluation / UX Review  
**Difficulty:** Medium (20 points)  
**Duration:** 15-20 minutes

### Concept
Users conduct a UX audit of 3 AI systems using the PAIR principles (People + AI Guidebook): identify user needs, define success, set expectations, design feedback/control.

### Learning Objectives
- Apply PAIR framework
- Conduct heuristic evaluations
- Identify UX gaps
- Recommend improvements

### PAIR Principles to Audit
1. **User Needs:** Does system align with actual user goals?
2. **Success Definition:** Are success criteria clear and measurable?
3. **Expectations:** Does system communicate capabilities and limitations?
4. **Feedback/Control:** Can users provide input and override AI?

### Example System Reviews

**System 1: Benefits Eligibility Chatbot**
Presented with conversation transcript and user feedback

User audit checklist:
- ☐ Clear communication of what bot can/cannot do?
- ☐ User can ask clarifying questions?
- ☐ Bot admits uncertainty when appropriate?
- ☐ User can override or escalate easily?
- ☐ Feedback mechanism exists?

**System 2: Document Classification Tool**
Presented with UI mockup

User audit checklist:
- ☐ Confidence scores visible?
- ☐ User can correct misclassifications?
- ☐ Explanation of why doc was classified that way?
- ☐ Batch review for low-confidence items?

**System 3: Recommendation Engine**
Presented with output sample

User audit checklist:
- ☐ Reasoning transparent?
- ☐ User can see alternatives?
- ☐ User can reject recommendation?
- ☐ System learns from rejections?

### Gameplay Mechanics
1. Show system evidence (transcript/mockup/output)
2. User completes audit checklist
3. User identifies top 3 issues
4. User recommends fixes aligned to PAIR principles
5. 3 systems total

### Why This Works
- Practical evaluation skill
- Teaches PAIR framework
- Pattern recognition for good/bad UX
- Immediately applicable

---

## Challenge 10: **Transparency Toolkit**
**Type:** Explainability Design Exercise  
**Difficulty:** Medium (20 points)  
**Duration:** 15-20 minutes

### Concept
Users design transparency/explainability features for 4 different AI systems based on user expertise level and risk context.

### Learning Objectives
- Design appropriate explainability
- Tailor explanations to user expertise
- Balance transparency with usability
- Apply XAI principles

### Framework
Different users need different explanations:
- **Novice:** "What happened" in plain language
- **Intermediate:** "Why it happened" with key factors
- **Expert:** "How it works" with model details

Different risks need different transparency:
- **Low risk:** Brief explanation
- **Medium risk:** Detailed reasoning
- **High risk:** Full auditability trail

### Example Scenarios

**Scenario 1: Spam Filter (Low Risk, Mixed Expertise)**
Design explanation for email user (novice) vs IT admin (expert)

Novice option: "This email was marked as spam because it contains suspicious links and urgency language."
Expert option: "Spam score: 0.87 | Features: link_count=5, urgency_words=3, sender_reputation=-2 | Model: Random Forest v2.3"

**Scenario 2: Loan Recommendation (High Risk, Intermediate User)**
Design explanation for loan officer

Correct approach:
- Show key factors: income, credit score, debt ratio
- Highlight which factors weighted most heavily
- Provide "what-if" tool: change variables, see impact
- Show similar approved/denied cases
- Require officer to document final decision

**Scenario 3: Content Moderation (Medium Risk, Expert User)**
Design explanation for content moderator

Correct approach:
- Show specific policy violations detected
- Highlight exact text triggering flags
- Provide confidence score per violation
- Allow appeal with justification
- Track moderator agreement rate

**Scenario 4: Medical Decision Support (High Risk, Expert User)**
Design explanation for physician

Correct approach:
- Show evidence from medical literature (citations)
- Display differential diagnosis with probabilities
- Explain key symptoms driving assessment
- Link to similar cases
- Make clear it's support, not diagnosis
- Require physician sign-off

### Gameplay Mechanics
1. Present scenario with context
2. User selects appropriate transparency features from options
3. User rates explanation verbosity (low/medium/high)
4. System scores based on risk-expertise match
5. 4 scenarios total

### Why This Works
- Teaches context-appropriate explainability
- Reinforces human-centered XAI
- Prevents "one size fits all"
- Practical design skill

---

## Recommended Challenge Implementation Priority

### Phase 1: Foundation (Launch with these)
1. **Pattern Matcher** (Easy, 15pts) - Teaches core pattern catalog
2. **The Four Questions** (Easy, 15pts) - Teaches fast triage
3. **UX Surgeon** (Medium, 20pts) - Teaches HCD principles

### Phase 2: Application (Add second week)
4. **Maturity Ladder** (Medium, 20pts) - Teaches sequencing
5. **Risk Router** (Medium, 20pts) - Teaches responsible AI
6. **Metrics That Matter** (Medium, 20pts) - Teaches measurement

### Phase 3: Advanced (Add third week)
7. **Graduation Gates** (Hard, 25pts) - Teaches governance
8. **Problem→Solution Workshop** (Hard, 25pts) - Teaches discovery
9. **Experience Audit** (Medium, 20pts) - Teaches PAIR framework
10. **Transparency Toolkit** (Medium, 20pts) - Teaches explainability

---

## Cross-Cutting Themes for All Challenges

All challenges should reinforce:
1. **Human-Centered First:** People over technology
2. **Problem Before Solution:** Frame need before picking tools
3. **Simple → Mature:** Start basic, add complexity only when needed
4. **Risk-Based Decisions:** Higher stakes = more oversight
5. **Measurement Matters:** Define success metrics early
6. **Transparency Builds Trust:** Users need to understand AI behavior
7. **Feedback Loops:** Systems should learn and improve
8. **Responsible Deployment:** Governance is not optional

---

## Notes for Challenge Development

### Narrative Framing
Week 10 is the culmination - "Operation Final Gambit" suggests bringing it all together. Frame challenges as:
- "Final mission briefing before deployment"
- "Proving you can design responsibly"
- "Earning certification to lead AI initiatives"

### Spy-Thriller Integration
- Pattern Matcher: "Selecting the right tool for covert operations"
- Maturity Ladder: "Scaling deployment without detection"
- UX Surgeon: "Debugging compromised interfaces"
- Risk Router: "Classifying threat levels"
- Graduation Gates: "Final security clearance review"

### Connection to Previous Weeks
- Week 2 (Bias): Feeds into Risk Router's rights-impacting assessment
- Week 4 (Policy): Connects to Maturity Ladder's governance gates
- Week 5 (Security): Relates to Risk Router's safety evaluation
- Week 6-8 (Technical): Pattern Matcher covers NLP, CV, automation patterns
- Week 9 (Prompt Engineering): Experience Audit includes prompt quality

### Reusability for Training
These challenges work well for:
- Lunch-and-learn sessions
- Solution architect onboarding
- Customer workshop facilitation training
- UX/product manager education
- Executive awareness briefings (simplified versions)