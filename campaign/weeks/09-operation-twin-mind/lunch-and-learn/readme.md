![Lunch and Learn Banner](https://raw.githubusercontent.com/davidlarrimore/mission-ai-possible/main/campaign/weeks/09-operation-twin-mind/lunch-and-learn/banner.png)

# Lunch & Learn Lab Guide: Prompt Engineering in AmiChat

This guide contains all of the hands-on activities for the Prompt Engineering Lunch & Learn. You’ll use [AmiChat](https://amichat.prod.amivero-solutions.com/) and the prompts/content below. Each exercise is self-contained.

## Table of contents

- [Exercise 1 – RGCC: Backoffice & Customer Support](#exercise-1)
- [Exercise 2 – CRISP: GovCon RFP & Compliance](#exercise-2)
- [Exercise 3 – Chain-of-Thought: Reasoning Through Work Problems](#exercise-3)
- [Exercise 4 – Capstone: Build Your Own Prompt](#exercise-4)

## How to use this guide

1. Open [AmiChat](https://amichat.prod.amivero-solutions.com/) in your browser.
2. For each exercise:
   - Copy the **Content to paste into AmiChat** section into the chat/input box.
   - Then copy the **Bad prompt** (or **Baseline prompt**) and run it once to see the difference.
   - Replace it with the **Improved prompt** and run again.
3. Tweak prompts and see how the model responds.

---

<p align="center">🎛️ 🎛️ 🎛️</p>
<a id="exercise-1"></a>

## Exercise 1 – RGCC: Backoffice & Customer Support

In these scenarios, you’ll practice **RGCC**:

- **R – Role**: Who should the model “be”?
- **G – Goal**: What outcome are you aiming for?
- **C – Context**: What information does it need?
- **C – Constraints**: What rules or formatting should it follow?

### Quick RGCC overview

```text
Role → Goal → Context → Constraints
(Who)   (What)   (Info)     (Rules & format)

You decide who the assistant is, what you want, what information it should use, and what boundaries or output shape it must follow.
```

For a one-page RGCC reference, see the Twin Mind docs: [(RGCC Reference)](https://github.com/davidlarrimore/mission-ai-possible/blob/main/campaign/weeks/09-operation-twin-mind/docs/rgcc-reference.md).

You’ll work through three scenarios:

1. IT Ticket Triage Agent (Backoffice RGCC)
2. HR Assistant Bot (Backoffice RGCC)
3. Customer Support Response Drafter (Customer Support RGCC)

For each scenario, you will:

- Copy the test data into AmiChat.
- Run a short **Bad Prompt** to see baseline results.
- Run the improved RGCC prompt for the same data.
- Compare how Role, Goal, Context, and Constraints change the output.

---

### 1.1 IT Ticket Triage Agent (Backoffice RGCC)

**Scenario:** You are building an assistant to help a Level 1 IT service desk triage tickets into the right queue.

#### Step 1 – Content to paste into AmiChat

```csv
ticket_id,subject,description
INC-10234,"Can't log into VPN","User reports: 'VPN keeps saying my credentials are invalid since password reset yesterday.'"
INC-10235,"New laptop request","Manager requesting a new laptop for a new hire starting next week in the DC office."
INC-10236,"Wi-Fi dropping","Several users on 3rd floor say Wi-Fi disconnects every 10-15 minutes, especially near conference rooms."
INC-10237,"Suspicious email","User forwarded an email that looks like a phishing attempt asking them to update payroll info via attached link."
INC-10238,"Software install","Request to install Adobe Creative Cloud for a marketing contractor on their existing laptop."
```

#### Step 2 – Bad prompt (run this once)

```text
Help me route IT tickets.
```

#### Step 3 – Improved RGCC prompt (run this next)

```markdown
You are a Level 1 IT service desk agent.

Your goal is to route incoming IT tickets to the correct queue.

Context:
- You can assign tickets to one of these queues:
  - "Account Access"
  - "Hardware"
  - "Networking"
  - "Security"
  - "General Support"
- Here are some recent tickets in CSV form:
~~~csv
ticket_id,subject,description
INC-10234,"Can't log into VPN","User reports: 'VPN keeps saying my credentials are invalid since password reset yesterday.'"
INC-10235,"New laptop request","Manager requesting a new laptop for a new hire starting next week in the DC office."
INC-10236,"Wi-Fi dropping","Several users on 3rd floor say Wi-Fi disconnects every 10-15 minutes, especially near conference rooms."
INC-10237,"Suspicious email","User forwarded an email that looks like a phishing attempt asking them to update payroll info via attached link."
INC-10238,"Software install","Request to install Adobe Creative Cloud for a marketing contractor on their existing laptop."
~~~

Constraints:
- Do not suggest or perform any technical fixes.
- For each ticket, only return:
  - ticket_id
  - assigned_queue
  - one-sentence rationale
- If the ticket mentions phishing, malware, suspicious email, or data breach, route to "Security".
- If the correct queue is unclear, route to "General Support" and say why it’s unclear.

Now, read the tickets and produce a markdown table with columns:
ticket_id | assigned_queue | rationale
```

#### Reflection

- How does the output change between the bad and improved prompts?
- What additional constraints would you add for your real IT environment?

---

### 1.2 HR Assistant Bot (Backoffice RGCC)

**Scenario:** You are building an HR assistant that answers employee questions strictly based on approved policy text.

#### Step 1 – Content to paste into AmiChat

```markdown
# Amivero PTO Policy (Excerpt)

- Full-time employees accrue 10 hours of Paid Time Off (PTO) per month during their first two years.
- After two years of continuous service, employees accrue 14 hours of PTO per month.
- PTO requests must be submitted at least 5 business days in advance for planned leave.
- PTO balances cannot go negative. Employees may not "borrow" future accruals.
- PTO does not carry over more than 40 hours into the next calendar year.

# Amivero Remote Work Policy (Excerpt)

- Employees may work remotely up to 3 days per week with manager approval.
- Fully remote arrangements require VP-level approval.
- Employees must be available during core hours (9am–3pm Eastern).
```

#### Step 2 – Bad prompt

```text
Answer HR questions for employees.
```

#### Step 3 – Improved RGCC prompt

```markdown
You are an HR generalist supporting employees.

Your goal is to answer HR policy questions clearly and consistently based only on the snippets I provide.

Context:
I will provide:
1) Excerpts of our HR handbook, and
2) One or more employee questions about those policies.

Here are the current handbook excerpts:
~~~markdown
# Amivero PTO Policy (Excerpt)

- Full-time employees accrue 10 hours of Paid Time Off (PTO) per month during their first two years.
- After two years of continuous service, employees accrue 14 hours of PTO per month.
- PTO requests must be submitted at least 5 business days in advance for planned leave.
- PTO balances cannot go negative. Employees may not "borrow" future accruals.
- PTO does not carry over more than 40 hours into the next calendar year.

# Amivero Remote Work Policy (Excerpt)

- Employees may work remotely up to 3 days per week with manager approval.
- Fully remote arrangements require VP-level approval.
- Employees must be available during core hours (9am–3pm Eastern).
~~~

Constraints:
- Answer ONLY using the policy excerpts above.
- Do NOT give legal advice or personal opinions.
- Always cite the relevant section heading in your answer (e.g., "PTO Policy (Excerpt)").
- If the policy text does not clearly answer the question, say:
  - what’s unclear, and
  - that the employee should contact HR directly.

Employee questions:
1. "I’ve been here 3 years. How many hours of PTO do I earn per month?"
2. "Can I take PTO next week if I submit the request two days before?"
3. "Can I work fully remote without VP approval if my manager is ok with it?"

Please answer each question in 2–3 sentences, numbered 1, 2, 3.
```

#### Reflection

- How did the output change between the bad and improved prompts?
- Did the model stay strictly within the provided policy excerpts?
- What additional constraints would you add for your real HR environment (e.g., escalation rules, disclaimers)?

---

### 1.3 Customer Support Response Drafter (Customer Support RGCC)

**Scenario:** You want the model to draft **DRAFT** replies to customer tickets that agents will review and edit before sending.

#### Step 1 – Content to paste into AmiChat

```markdown
## Ticket 48291
Channel: Email
Customer: Sarah Lopez
Issue: Double charge on last invoice
Customer message:
"I was charged twice for my April invoice. Please refund the duplicate charge as soon as possible."

Internal notes:
- Stripe logs show two identical charges within 2 minutes.
- Policy: Immediate refund allowed on confirmed duplicate charges.

## Ticket 48292
Channel: Chat
Customer: Federal Agency Helpdesk
Issue: Users cannot access reports after latest update
Customer message:
"After yesterday's update, our analysts can’t open the 'Monthly Compliance' report. They get a 500 error."

Internal notes:
- Incident #INC-2207 opened with engineering.
- Status page shows: "Degraded performance on Reporting service."
- Policy: Acknowledge outage, share status page link, no ETA promises.
```

#### Step 2 – Bad prompt

```text
Write replies to these tickets.
```

#### Step 3 – Improved RGCC prompt

```markdown
You are an L1 customer support agent copilot.

Your goal is to draft DRAFT replies to customers based on their ticket details and internal notes.

Context:
Below are two tickets with customer messages and internal notes.
~~~markdown
## Ticket 48291
Channel: Email
Customer: Sarah Lopez
Issue: Double charge on last invoice
Customer message:
"I was charged twice for my April invoice. Please refund the duplicate charge as soon as possible."

Internal notes:
- Stripe logs show two identical charges within 2 minutes.
- Policy: Immediate refund allowed on confirmed duplicate charges.

## Ticket 48292
Channel: Chat
Customer: Federal Agency Helpdesk
Issue: Users cannot access reports after latest update
Customer message:
"After yesterday's update, our analysts can’t open the 'Monthly Compliance' report. They get a 500 error."

Internal notes:
- Incident #INC-2207 opened with engineering.
- Status page shows: "Degraded performance on Reporting service."
- Policy: Acknowledge outage, share status page link, no ETA promises.
~~~

Constraints:
- Always mark each reply clearly as a DRAFT – agent review required at the top.
- Follow the policy hints in the internal notes.
- Be friendly, concise, and professional.
- Do NOT promise specific outcomes or dates beyond what’s in the notes.
- Do NOT issue refunds yourself; only talk about what "our team will do".

Instructions:
- For each ticket, produce:
  - A heading with the ticket number (e.g., "Ticket 48291")
  - A draft email/chat reply to the customer
  - Separate the two replies with a horizontal rule (---).

Now, draft the replies.
```

#### Reflection

- How did the improved RGCC prompt change the structure and tone of the replies?
- Did the model follow the internal notes and avoid over-promising?
- What additional constraints would you add for your real support environment (e.g., regulatory language, escalation paths)?

---

<p align="center">📐 📐 📐</p>
<a id="exercise-2"></a>

## Exercise 2 – CRISP: GovCon RFP & Compliance

In these scenarios, you’ll practice **CRISP**:

- **C – Context**: What’s going on? Who is involved?
- **R – Role**: What expert do you want the model to be?
- **I – Instructions**: Clear, step-by-step directions.
- **S – Specifics**: Format, style, length, structure.
- **P – Purpose**: Why you need this; how you’ll use it.

### Quick CRISP overview

```text
Context → Role → Instructions → Specifics → Purpose
(What's going on?) (Who am I?) (What to do?) (How to format?) (Why it matters?)

You give the model the situation, assign a role, walk it through the steps, lock in the format, and remind it how the result will be used.
```

For a visual CRISP reference, see the Twin Mind docs: [CRISPE Reference)](https://github.com/davidlarrimore/mission-ai-possible/blob/main/campaign/weeks/09-operation-twin-mind/docs/crispe-reference.md).

### Example outputs (optional – for comparison)

Use these examples if you’d like to see what a typical “bad” vs improved response looks like before or after you run your own prompts.

#### Exercise 1.1 – IT Ticket Triage

**Bad Prompt Output Example**

1. The VPN issue should go to IT support since it's about login credentials.
2. The laptop request is a hardware request for a new employee.
3. The Wi-Fi problem sounds like a networking issue affecting multiple users.
4. The suspicious email is definitely a security concern and should be investigated.
5. The software installation is a standard support request.

**Improved RGCC Prompt Output Example**

| ticket_id | assigned_queue | rationale |
|-----------|----------------|-----------|
| INC-10234 | Account Access | User's VPN credentials became invalid after password reset yesterday, indicating an authentication sync issue between AD and VPN system. |
| INC-10235 | Hardware | Manager requesting new laptop for incoming employee with specific timeline (next week) and location (DC office). |
| INC-10236 | Networking | Multiple users on same floor experiencing consistent Wi-Fi disconnections suggests access point or infrastructure issue requiring networking team diagnosis. |
| INC-10237 | Security | Email requesting payroll info update via attached link matches phishing attack pattern and must be reviewed by security team immediately. |
| INC-10238 | General Support | Software installation request for contractor requires verification of licensing and approval before routing to appropriate technical team. |

#### Exercise 1.2 – HR Assistant Bot

**Bad Prompt Output Example**

1. After 3 years, you'd be earning 14 hours of PTO per month since you're past the 2-year mark.
2. No, you need to submit PTO requests at least 5 business days in advance, so 2 days wouldn't be enough notice.
3. You can work remotely up to 3 days per week with manager approval, but going fully remote requires VP-level approval, so your manager's approval alone isn't sufficient.

**Improved RGCC Prompt Output Example**

1. According to the **PTO Policy (Excerpt)**, after two years of continuous service, employees accrue 14 hours of PTO per month. Since you've been here 3 years, you earn 14 hours per month.
2. According to the **PTO Policy (Excerpt)**, PTO requests must be submitted at least 5 business days in advance for planned leave. Two days before would not meet this requirement, so your request would likely not be approved under the standard policy. For urgent situations, please contact HR directly to discuss options.
3. According to the **Remote Work Policy (Excerpt)**, employees may work remotely up to 3 days per week with manager approval, but fully remote arrangements require VP-level approval. Your manager's approval alone would not be sufficient for a fully remote arrangement. You would need to escalate the request to the VP level.

#### Exercise 1.3 – Customer Support Response Drafter

**Bad Prompt Output Example**

**Ticket 48291**

Hi Sarah,

Thanks for reaching out about the duplicate charge. I can see this happened on your April invoice. We'll process a refund for you right away. You should see it back in your account within 5-7 business days.

Sorry for the inconvenience!

---

**Ticket 48292**

Hello,

We're aware of the issue with the Monthly Compliance report. Our engineering team is working on it. We'll update you as soon as it's fixed.

Thanks for your patience.

**Improved RGCC Prompt Output Example**

**Ticket 48291**

**DRAFT – agent review required**

Hi Sarah,

Thank you for contacting us about the duplicate charge on your April invoice. Our team has reviewed the transaction logs and confirmed that two identical charges were processed within 2 minutes of each other.

Our billing team will process a refund for the duplicate charge today. You should see the credit back to your original payment method within 5-7 business days.

We apologize for this error and any inconvenience it caused.

Best regards,  
[Your name]

---

**Ticket 48292**

**DRAFT – agent review required**

Hello,

Thank you for reporting the issue with the Monthly Compliance report. We're aware that users are receiving a 500 error when attempting to access this report following yesterday's update.

Our engineering team has opened incident #INC-2207 and is actively investigating the issue. You can monitor the status on our status page at [status page link]. Due to the complexity of the issue, we're unable to provide a specific resolution timeframe at this time.

We understand the importance of this report for your analysts and will keep you updated as we make progress. Please check the status page for real-time updates, or reply to this message if you need additional assistance.

Best regards,  
[Your name]

---

### 2.1 RFP Decomposition (GovCon CRISP)

**Scenario:** You’re analyzing an RFP excerpt and want to pull out requirements, evaluation factors, constraints, and deliverables.

#### Step 1 – Content to paste into AmiChat

```markdown
SECTION C – STATEMENT OF WORK (Excerpt)

The Contractor shall provide Operations and Maintenance (O&M) support for the Department’s Case Management System (CMS).

1. The Contractor shall provide Tier 2 and Tier 3 support services for approximately 3,000 users nationwide, 7 days per week, 6am–10pm Eastern Time.
2. The Contractor shall maintain system availability of 99.5% during core business hours (8am–6pm Eastern Time, Monday–Friday), excluding planned maintenance.
3. The Contractor shall comply with DHS 4300A Sensitive Systems Handbook and all applicable federal information security requirements.
4. The Contractor shall provide monthly performance reports including, at a minimum: ticket volumes, mean time to resolution, system availability, and summary of significant incidents.
5. The Contractor shall support one major and up to four minor releases per year, including regression testing and deployment support.

SECTION L – INSTRUCTIONS TO OFFERORS (Excerpt)

- Offerors shall describe their technical approach to meeting the requirements in Section C.
- Offerors shall provide a staffing plan including key personnel and labor categories.
- Page limit: 25 pages for the technical volume.
```

#### Step 2 – Bad prompt

```text
Help me with this RFP.
```

#### Step 3 – Improved CRISP prompt

```markdown
Context:
I am preparing a proposal response for a DHS Case Management System O&M contract.
Below is an excerpt from Sections C and L of the RFP.

~~~markdown
SECTION C – STATEMENT OF WORK (Excerpt)

The Contractor shall provide Operations and Maintenance (O&M) support for the Department’s Case Management System (CMS).

1. The Contractor shall provide Tier 2 and Tier 3 support services for approximately 3,000 users nationwide, 7 days per week, 6am–10pm Eastern Time.
2. The Contractor shall maintain system availability of 99.5% during core business hours (8am–6pm Eastern Time, Monday–Friday), excluding planned maintenance.
3. The Contractor shall comply with DHS 4300A Sensitive Systems Handbook and all applicable federal information security requirements.
4. The Contractor shall provide monthly performance reports including, at a minimum: ticket volumes, mean time to resolution, system availability, and summary of significant incidents.
5. The Contractor shall support one major and up to four minor releases per year, including regression testing and deployment support.

SECTION L – INSTRUCTIONS TO OFFERORS (Excerpt)

- Offerors shall describe their technical approach to meeting the requirements in Section C.
- Offerors shall provide a staffing plan including key personnel and labor categories.
- Page limit: 25 pages for the technical volume.
~~~

Role:
Act as a federal proposal analyst experienced in IT services RFPs.

Instructions:
1. Extract all explicit requirements as individual line items.
2. Identify any evaluation factors implied or stated in the text.
3. Identify any constraints (page limits, standards, required reports, hours of support).
4. Identify any deliverables (e.g., reports, releases, support).

Specifics:
- Output a markdown table with columns:
  - ID
  - Requirement / Factor / Constraint / Deliverable
  - Source Section (e.g., "C.1", "L.1")
  - Notes (e.g., related metrics, standards)
- Keep entries short and scannable.

Purpose:
I will use this table as the starting point for our compliance matrix and writing plan.

Now read the RFP excerpt and produce the table.
```

---

### 2.2 Compliance Matrix Generation (GovCon CRISP)

**Scenario:** You’re building a compliance matrix from the same RFP excerpt and need a structured table to assign writing responsibilities.

#### Step 1 – Content to reuse in AmiChat

Use the **same RFP excerpt** from Exercise 2.1.

#### Step 2 – Improved CRISP prompt

```text
Context:
We are building a compliance matrix for the DHS CMS O&M RFP.
Below is the same RFP excerpt (Sections C and L).

~~~markdown
[RFP excerpt from Exercise 2.1]
~~~

Role:
Act as a proposal manager creating a compliance matrix.

Instructions:
1. Identify each requirement that the proposal must address.
2. For each requirement, recommend:
   - A short "Requirement ID" label (e.g., "REQ-AVAIL-99.5").
   - The likely volume/section of the proposal where it should be addressed (e.g., "Tech Approach – O&M").
3. Note any required artifacts (e.g., staffing plan, reports).

Specifics:
- Output a markdown table with columns:
  - Requirement ID
  - Requirement Text
  - Recommended Proposal Section
  - Required Artifact (if any)
- Limit each cell to one brief sentence.

Purpose:
I will import this table into our compliance matrix and use it to assign writing owners.

Generate the table now.
```

---

<p align="center">🧠 🧠 🧠</p>
<a id="exercise-3"></a>

## Exercise 3 – Chain-of-Thought: Reasoning Through Work Problems

In these scenarios, you’ll practice **Chain-of-Thought (CoT)** prompting:

- Ask the model to **think step-by-step**.
- Have it show its **intermediate reasoning** before it gives a final answer.
- Compare a simple “direct” prompt vs. a structured CoT prompt.

### Quick CoT overview

```text
Problem → Break into steps → Reason step-by-step → Check the work → Final answer

You explicitly ask the model to show its thinking before giving the final result, so you can verify the logic and catch mistakes.
```

For more CoT diagrams and examples, see the Twin Mind docs: [Chain of Thought Reference)](https://github.com/davidlarrimore/mission-ai-possible/blob/main/campaign/weeks/09-operation-twin-mind/docs/chain-of-thought-reference.md).

---

### 3.1 Payroll Discrepancy Investigation (Backoffice CoT)

**Scenario:** You need to explain to an employee why their take-home pay changed between two pay periods, despite working overtime and receiving a bonus.

#### Step 1 – Content to paste into AmiChat

```markdown
Employee: Jordan Smith
Pay frequency: Bi-weekly

Previous paycheck (Pay Period: 2025-03-01 to 2025-03-14)
- Regular hours: 80 @ $40.00/hr
- Overtime hours: 0
- Bonus: $0
- Pre-tax deductions:
  - 401(k): 5% of gross pay
- Post-tax deductions:
  - Parking: $50
- Federal tax withheld: $620
- State tax withheld: $220
- Net pay: $2,710

Current paycheck (Pay Period: 2025-03-15 to 2025-03-28)
- Regular hours: 72 @ $40.00/hr
- Overtime hours: 8 @ $60.00/hr (time-and-a-half)
- Bonus: $250 spot bonus
- Pre-tax deductions:
  - 401(k): 5% of gross pay
- Post-tax deductions:
  - Parking: $50
  - One-time equipment charge: $150
- Federal tax withheld: $760
- State tax withheld: $260
- Net pay: $2,630

Employee question:
"My hours and pay look weird this period. Why is my take-home pay lower than last time if I worked overtime and got a bonus?"
```

#### Step 2 – Baseline (Direct prompt – run this once)

```text
Explain why this employee's take-home pay decreased despite overtime and a bonus.

[payroll data]
```

Reflection tip: As you run this, notice whether the model shows its work, how confident you feel in the answer, and how easy it is to verify the math.

#### Step 3 – Improved CoT prompt (run this next)

```markdown
You are a payroll analyst helping explain paycheck differences to employees.

Think through this step-by-step.

1. First, restate the key inputs for the previous paycheck and the current paycheck (hours, overtime, bonus, deductions, taxes).
2. Then, calculate and explain:
   - The gross pay for each period.
   - How pre-tax deductions and taxes changed between periods.
   - The impact of the one-time equipment charge.
3. Step-by-step, explain how these differences result in the current net pay being lower even with overtime and a bonus.
4. Finally, draft a short, plain-language explanation that could be sent to the employee (3–5 sentences).

Here is the data:

~~~markdown
[payroll data from above]
~~~

Show your reasoning for steps 1–3 before giving the final explanation.
```

#### Reflection

- How did the **Direct prompt** answer differ from the **CoT prompt** answer?
- Where did the CoT version make it easier to **check the calculations**?
- Which answer would you feel more confident sending to Jordan?

---

### 3.2 Bid / No-Bid Reasoning (GovCon CoT)

**Scenario:** You’re helping a capture team decide whether to bid on an opportunity.

#### Step 1 – Content to paste into AmiChat

```markdown
Opportunity: DOJ Cloud Migration and Managed Services

Customer: Department of Justice (DOJ)
NAICS: 541512
Scope (simplified):
- Migrate 15 legacy on-prem applications to a FedRAMP High cloud environment.
- Provide 24x7 operations and security monitoring.
- Support CI/CD pipelines for ongoing enhancements.

Contract Type: Hybrid FFP / T&M
Estimated Value: $75M total over 5 years
Set-Aside Status: Full & Open

Our company profile (for this exercise):
- Strong past performance with DHS and DOJ components on cloud and DevSecOps work.
- 3 active FedRAMP High-authorized environments managed today.
- Limited experience with 24x7 follow-the-sun operations (we mostly run 8x5).
- Current staffing is tight; would require hiring ~20 additional FTEs within 6 months.
- Existing strategic partner with a large Tier 1 integrator interested in teaming.
```

#### Step 2 – Baseline (Direct prompt – run this once)

```text
Should we bid on this opportunity?

[opportunity and company profile]
```

Reflection tip: After you run this, ask yourself whether the model actually shows how it reached the recommendation, or just gives a high-level answer.

#### Step 3 – Improved CoT prompt (run this next)

```markdown
You are a capture strategist helping with a bid/no-bid decision.

Think through this step-by-step.

1. Restate the opportunity in 2–3 sentences based on the description.
2. Rate our position on each of these criteria from 1–5, with 5 being strongest:
   - Customer fit
   - Technical fit
   - Past performance
   - Capacity to staff
   - Margin potential
3. For each rating, give 1–2 bullets explaining your reasoning based on the company profile.
4. Compute a simple "fit score" (for example, the average of all ratings) and explain what that number implies in plain language.
5. Finally, recommend "bid" or "no-bid" and explain why in 3–4 bullets, including any key conditions (e.g., must team with X, must negotiate Y).

Here is the opportunity and company profile:

~~~markdown
[opportunity and company profile from above]
~~~

Show your reasoning for steps 1–4 before giving the final recommendation.
```

#### Reflection

- How did the CoT prompt change the **structure** of the answer (ratings, fit score, bullets)?
- Which version would you feel comfortable taking into a **capture review** with leadership?
- What CoT steps would you tweak to better match your real bid/no-bid process?

---

<p align="center">🚀 🚀 🚀</p>
<a id="exercise-4"></a>

## Exercise 4 – Capstone: Build Your Own Prompt

In this final exercise, you’ll combine what you’ve learned about **RGCC**, **CRISP**, and **Chain-of-Thought**.

### Your task

1. Pick a real, recurring task from your own work (or choose one of the scenarios above).
2. Decide which structure fits best:
   - **RGCC** – if you are defining a reusable “assistant” with clear guardrails.
   - **CRISP** – if you want a structured, repeatable template for an artifact (matrix, summary, deck, etc.).
   - **CoT** – if the task involves multi-step reasoning or tradeoffs.
3. Draft a prompt that:
   - Clearly defines **Role, Goal, Context, Constraints** (RGCC) or
   - Uses **Context, Role, Instructions, Specifics, Purpose** (CRISP), and
   - Optionally includes at least one CoT instruction (e.g., “Think through this step-by-step…”).
4. Run it in [AmiChat](https://amichat.prod.amivero-solutions.com/) with some realistic content.
5. Make **one improvement**:
   - Add or tighten a constraint.
   - Clarify the role.
   - Change the output format (table vs bullets).
6. Save the final version somewhere you’ll reuse it (notes, bookmark, preset, etc.).

If you need a quick reminder of any framework while you work, you can glance back at the overviews above or open the Twin Mind reference docs: [Prompting Strategy References (RGCC, CRISP, CoT)](https://github.com/davidlarrimore/mission-ai-possible/tree/main/campaign/weeks/09-operation-twin-mind/docs).

### Optional sharing

- If you’re in a live session, share your favorite prompt with the group or drop it in chat.
- Look for:
  - Clear role definition.
  - Specific, concrete instructions.
  - Helpful constraints and output format.
  - Thoughtful reasoning steps where appropriate.

---

*End of Lab Guide*
