## 1️⃣ Quick recap of the three methods (grounded in current practice)

### CRISP (and cousins like CRISPE / CRISPE)

Modern CRISP-style frameworks break a prompt into explicit fields such as **Context, Role, Instruction, Specification/Steps, Preferences/Parameters** so the model has a structured brief instead of a single vague sentence.

**Best mental model:** “Use CRISP when I need a *high-quality, repeatable template* for a task.”

### Chain of Thought (CoT)

Chain-of-thought prompting tells the model to **lay out intermediate reasoning steps** before giving an answer (“think step by step”). Research shows this improves performance on multi-step math, logic, and symbolic reasoning tasks.

**Best mental model:** “Use CoT when I need the model to *reason through* a problem, not just answer directly.”

### RGCC (Role + Goal + Context + Constraints)

Many recent guides describe effective prompts as **role + goal + context + constraints (+ output format)** : you define who the model is, what outcome you want, what background it should use, and what rules it must obey.

**Best mental model:** “Use RGCC when I need *tight control, guardrails, and predictable behavior* .”

Below, for each domain:

- **CRISP** → templated work products / docs / structured outputs
- **CoT** → analysis, root-cause, planning, tradeoffs
- **RGCC** → assistants, copilots, or automations that must stay within rules

### 2️⃣ Backoffice (HR, Finance, Accounting, IT)

#### ✅ CRISP use cases

1. **HR policy summarization:** Generate a 1-page, role-specific summary of a long HR policy using Context (policy text), Role (HR communications lead), Instructions (summarize for managers), Steps (outline → bullets → FAQs), Preferences (plain-language, Flesch target).
2. **Job description drafting:** Turn competency models and role profiles into consistent job descriptions with defined sections (mission, responsibilities, KSAs, clearance, location).
3. **Invoice exception handling email:** Produce standard, polite explanations for invoice rejections, given an exception reason and vendor details.
4. **IT change advisory briefs:** Convert raw technical change tickets into executive-ready CAB summaries with impact, risk, and rollback steps.
5. **Quarterly financial narrative:** Turn trial balance exports + variance notes into a narrative FP&amp;A commentary by cost center.

#### 🧠 CoT use cases

1. **Payroll discrepancy investigation:** Walk step-by-step through payroll inputs to explain why a specific paycheck amount differs from the prior period.
2. **Headcount &amp; budget planning:** Reason through scenarios (e.g., hiring freeze vs. backfill only) and lay out pros/cons and financial impacts step-by-step.
3. **IT incident root cause:** Take logs, user reports, and timestamps and reason through likely root cause chain and what additional data is needed.
4. **Spend optimization:** Analyze vendor list + spend categories and reason through a prioritized “consolidate vs renegotiate vs keep” plan.
5. **Control-gap analysis:** Given internal control requirements and current processes, reason through where gaps exist and how they could be closed.

#### 🎯 RGCC use cases

1. **HR assistant bot:** Role (HR generalist), Goal (answer policy FAQs), Context (current handbook snippets), Constraints (no legal advice; always cite policy section; escalate edge cases).
2. **Finance coding helper:** Role (AP clerk), Goal (suggest GL codes), Context (chart of accounts + past coded invoices), Constraints (never post, only recommend; always include confidence and rationale).
3. **IT ticket triage agent:** Role (service desk L1), Goal (route tickets to correct queue), Context (service catalog), Constraints (no config changes; default to “general support” if unclear).
4. **Onboarding checklist generator:** Role (HR operations), Goal (produce task checklists for new hires by role/location), Constraints (only use items approved in SOP library).
5. **Access-request validator:** Role (IT compliance), Goal (flag potentially excessive access requests), Constraints (never auto-deny; only produce a risk summary and required approvers).

### 3️⃣ Government Contracting (GovCon)

#### ✅ CRISP use cases

1. **RFP decomposition:** Turn an RFP section into structured fields (requirements, evaluation factors, constraints, deliverables, compliance needs).
2. **Proposal section drafting:** Generate full proposal sections from outlines (technical approach, management plan, staffing, past performance) using consistent headings.
3. **Compliance matrix generation:** Extract requirement IDs and map them to TOC sections and artifacts.
4. **Win theme development:** From a capture strategy, generate 3–5 sharp win themes with proof points and discriminators.
5. **Color team summary decks:** Summarize red/pink/etc team findings into slide-ready bullets by volume/section.

#### 🧠 CoT use cases

1. **Bid/no-bid reasoning:** Evaluate opportunity fit with weighted criteria (customer fit, Pwin, teaming, margin, capacity) and show the reasoning chain.
2. **Price-to-win analysis (high level):** Reason through how technical solution tradeoffs (staffing levels, tools, SLAs) impact likely competitive price bands.
3. **Risk register development:** Think through likely risks across technical, schedule, staffing, and compliance dimensions and link them to mitigations.
4. **Teaming strategy:** Analyze gaps vs. evaluation criteria and reason through which types of partners best close each gap.
5. **Proposal debrief analysis:** Given debrief notes, reason step-by-step about root causes of strengths/weaknesses and improvement actions.

#### 🎯 RGCC use cases

1. **Proposal drafting copilot:** Role (federal proposal writer), Goal (draft compliant text for assigned sections), Context (RFP, solution concept, boilerplate), Constraints (no new commitments; no made-up past performance).
2. **Requirements traceability assistant:** Role (requirements engineer), Goal (maintain RTM), Constraints (only map existing requirements; flag ambiguity instead of guessing).
3. **Contract mod impact analyzer:** Role (contracts analyst), Goal (summarize impact of proposed mod on scope, funding, and schedule), Constraints (no legal advice; highlight areas for CO review).
4. **Task-order triage bot:** Role (BD pipeline coordinator), Goal (summarize new TO notices), Constraints (no probability estimates; just classification, deadlines, and quick summary).
5. **Boilerplate compliance checker:** Role (QA reviewer), Goal (check sections against required boilerplate language), Constraints (only flag deltas, don’t auto-correct).

### 4️⃣ Law Enforcement (supportive, policy-bound uses)

#### ✅ CRISP use cases

1. **Incident report drafting:** Convert structured fields (time, location, parties, narrative notes) into a first-draft report with required headings.
2. **Case summary preparation:** Turn multi-incident notes into a concise case synopsis for supervisors or prosecutors.
3. **Interview question sets:** Generate tailored question lists based on offense type and case context (e.g., burglary vs. cybercrime).
4. **Training scenario creation:** Build realistic but anonymized training scenarios from patterns in historical cases.
5. **Policy explainer memos:** Summarize use-of-force or evidence-handling policies for line officers.

#### 🧠 CoT use cases

1. **Timeline reconstruction:** Given multiple incident reports and timestamps, reason through a unified, ordered sequence of events.
2. **Consistency checking:** Compare multiple witness statements and reason through where accounts align vs. conflict.
3. **Resource allocation reasoning:** Evaluate patrol or investigative resource allocation options and their trade-offs.
4. **Case linking hypotheses:** Suggest non-sensitive hypothesis chains for how similar MO or locations might indicate related incidents (leaving final judgement to investigators).
5. **Policy application reasoning:** Walk step-by-step through how a specific policy would apply to a described scenario.

#### 🎯 RGCC use cases

1. **Case file summarization assistant:** Role (case support analyst), Goal (summarize existing case files), Constraints (no predictive accusations; no identity guesses; only restate present data).
2. **Report quality checker:** Role (editor), Goal (check structure and clarity of incident reports), Constraints (no facts added; only style/structure suggestions).
3. **Evidence log validator:** Role (chain-of-custody checker), Goal (highlight missing handoffs or signatures), Constraints (no inference about what “must have happened”).
4. **Policy Q&amp;A bot:** Role (policy reference assistant), Goal (answer “what does policy X say about Y?”), Constraints (quote policy; no operational advice beyond text).
5. **Training content generator:** Role (academy instructor), Goal (generate quizzes and scenario prompts), Constraints (anonymized, no real case details).

### 5️⃣ Identity Fraud Detection

#### ✅ CRISP use cases

1. **Fraud typology catalog:** Turn SME notes into structured descriptions of fraud types (e.g., account takeover, synthetic ID, mule accounts) with indicators and controls.
2. **Alert explainer templates:** Generate standardized internal “why this was flagged” explanations for analysts using known features.
3. **Customer-facing letters:** Draft clear explanations for customers whose applications are under review due to fraud checks (neutral, non-accusatory).
4. **Fraud playbook documentation:** Turn scattered notes into process documents for different alert queues.
5. **KPI dashboard narratives:** Convert raw metrics (alert volumes, false positives, time-to-close) into an executive narrative.

#### 🧠 CoT use cases

1. **Alert prioritization reasoning:** Given features (velocity, geography, device fingerprints), reason step-by-step which alerts should be prioritized and why.
2. **False-positive root cause analysis:** Analyze sets of resolved false positives and reason through which rules or thresholds may be miscalibrated.
3. **Scenario stress testing:** Think through how a new fraud pattern could exploit existing rules and where detection might fail (for internal red-team use).
4. **Case complexity assessment:** Reason through factors that make a case “simple vs complex” for staffing and SLA planning.
5. **Policy tradeoff analysis:** Analyze tradeoffs between stricter controls and customer friction.

#### 🎯 RGCC use cases

1. **Analyst triage copilot:** Role (fraud analyst assistant), Goal (summarize alerts and suggest next checks), Constraints (never auto-decline; never label someone “fraudster”; always defer final decision to analyst).
2. **KYC documentation checker:** Role (operations QA), Goal (check if required docs are present/legible), Constraints (no approval; only flag missing/incomplete items).
3. **Fraud-rule documentation generator:** Role (BA), Goal (generate natural-language descriptions of rules from configuration tables), Constraints (no new rules invented).
4. **Regulatory response helper:** Role (compliance writer), Goal (draft responses to regulator RFIs about fraud controls), Constraints (only use provided facts).
5. **Investigation checklist builder:** Role (playbook assistant), Goal (produce checklists for each fraud typology), Constraints (aligned to existing policy, no novel investigative techniques).

### 6️⃣ Customer Support

#### ✅ CRISP use cases

1. **Macro/template creation:** Generate tiered response templates (L1, L2, escalation) for common issues with required disclaimers and links.
2. **Knowledge-base articles:** Turn engineer notes into customer-facing KB docs with intro, steps, FAQs, and known issues.
3. **Post-contact summaries:** Convert chat transcripts into CRM-ready summaries and disposition codes.
4. **Proactive outreach scripts:** Draft outbound messages for known incidents (e.g., partial outage notifications).
5. **CSAT follow-up templates:** Create personalized follow-up messages based on survey feedback.

#### 🧠 CoT use cases

1. **Troubleshooting trees:** Reason step-by-step through possible causes of an issue and propose a decision tree for agents.
2. **Root cause pattern analysis:** Analyze categories of tickets and reason how product issues or UX problems are driving volume.
3. **Policy edge case reasoning:** Walk through a tricky scenario (refunds, exceptions) and reason how policy might apply with pros/cons.
4. **Capacity planning:** Reason about expected ticket volumes based on events (releases, campaigns) and staffing needed.
5. **Deflection opportunity analysis:** Analyze which ticket types are best suited for automation vs human handling and why.

#### 🎯 RGCC use cases

1. **Support chatbot:** Role (L1 support agent), Goal (resolve basic issues), Context (KB + policies), Constraints (no refunds beyond allowed; escalate abusive content; avoid personal data transformations beyond policy).
2. **Quality review assistant:** Role (QA coach), Goal (score agent interactions), Constraints (use provided rubric; no ranking of individuals by name outside rubric).
3. **SLAs watchdog:** Role (operations monitor), Goal (flag tickets breaching SLAs), Constraints (no auto-closing; alerts only).
4. **Multi-channel unifier:** Role (support analyst), Goal (merge email/chat/phone logs into a unified customer issue summary), Constraints (read-only; no ticket state changes).
5. **Response generator with redlines:** Role (agent copilot), Goal (draft replies), Constraints (always mark as “draft”; require agent confirmation).

### 7️⃣ Employee Background Adjudication

#### ✅ CRISP use cases

1. **Case file condensation:** Summarize large background investigation files into 1–2 page briefs with structured sections (employment, education, references, concerns).
2. **Follow-up question drafting:** Generate tailored follow-up questions for investigators based on identified gaps or inconsistencies.
3. **Issue code mapping:** Map narrative issues into standardized issue codes for tracking.
4. **Adjudication memo templates:** Draft memos with defined headings (summary, issues, mitigating factors, recommendation) from structured notes.
5. **Applicant communication drafts:** Create clear, neutral notification letters requesting additional information.

#### 🧠 CoT use cases

1. **Timeline reconstruction:** Reason through employment and residence histories and highlight gaps.
2. **Discrepancy analysis:** Step-by-step comparison of forms, references, and checks to identify and categorize inconsistencies.
3. **Mitigation reasoning outline:** For a flagged issue, outline possible mitigating and aggravating factors (for adjudicator review).
4. **Case complexity scoring:** Reason through factors that increase complexity (foreign travel, multiple jurisdictions) for prioritization.
5. **Policy-application reasoning:** Walk through how adjudicative guidelines might apply to a hypothetical case (supporting training, not final decisions).

#### 🎯 RGCC use cases

1. **Adjudicator assistant:** Role (case support analyst), Goal (organize and summarize case info), Constraints (no automated “eligible/ineligible” decisions; only structure info for human review).
2. **Policy Q&amp;A assistant:** Role (policy explainer), Goal (answer “what do the guidelines say about X?”), Constraints (cite policy text; no specific case advice).
3. **Redaction helper:** Role (privacy assistant), Goal (suggest content for redaction before sharing case files), Constraints (follow configured redaction rules only).
4. **Checklist verifier:** Role (QC checker), Goal (check if all required checks are documented), Constraints (no inference of results, just presence/absence).
5. **Training case builder:** Role (training designer), Goal (generate synthetic practice cases), Constraints (no real names or identifiable details).

### 8️⃣ Immigration Adjudication (e.g., USCIS RIVER-related work)

#### ✅ CRISP use cases

1. **Case summary sheets:** Generate digestible case overviews from application forms, supporting documents, and prior decisions.
2. **RFE draft letters:** Produce structured RFE templates given missing or unclear evidence patterns.
3. **Country-conditions briefs:** Summarize open-source country conditions into adjudicator-ready briefs with sources.
4. **Form-to-criteria mapping:** Turn statutory/regulatory eligibility criteria into checklists tied to form questions.
5. **Policy update digests:** Summarize new policy updates and map them to affected case types.

#### 🧠 CoT use cases

1. **Eligibility reasoning walkthrough:** Step through criteria for a hypothetical case and outline what evidence would support or undermine each element (for training use).
2. **Impact assessment of rule changes:** Reason about how a regulatory change could affect volumes, processing time, or evidence requirements.
3. **Caseload prioritization reasoning:** Analyze case attributes and reason through which cases should be prioritized under policy.
4. **Template improvement reasoning:** Evaluate current RFE or decision templates and reason how they could be clearer and more consistent.
5. **Quality review analysis:** Examine sample decisions and reason about common clarity or consistency issues.

#### 🎯 RGCC use cases

1. **Case file organization assistant:** Role (case organizer), Goal (reorganize and label evidence sections), Constraints (no decision recommendations; no risk scoring).
2. **Evidence checklist assistant:** Role (workflow helper), Goal (check which standard pieces of evidence are present/missing for a case type), Constraints (no inference from partial evidence).
3. **Policy-lookup bot:** Role (policy librarian), Goal (find relevant sections of policy manual/regulation), Constraints (quote references; no case-specific conclusions).
4. **Template-filler assistant:** Role (document drafter), Goal (pre-fill standard sections of notices from structured data), Constraints (leaving determination fields blank for humans).
5. **Translation &amp; summarization helper:** Role (linguistic assistant), Goal (summarize foreign-language docs), Constraints (mark as unofficial; require interpreter review).

### 9️⃣ Open Source Intelligence (OSINT) Analysis

#### ✅ CRISP use cases

1. **OSINT situation reports (SITREPs):** Turn multi-source feeds into structured period reports (summary, assessed trends, notable events, source list).
2. **Source catalogs:** Generate profiles of sources (feeds/sites/accounts) with reliability, coverage, and access notes.
3. **Thematic briefs:** Create briefs on topics (e.g., migration trends, cyber threats) from open-source articles.
4. **Event timelines:** Turn timestamped items into a visualizable timeline description.
5. **Analytic product templates:** Standardize report structures for recurring deliverables.

#### 🧠 CoT use cases

1. **Narrative analysis:** Reason step-by-step about how different actors’ narratives on a topic converge/diverge.
2. **Claim plausibility assessment:** Walk through evidence for and against a specific open-source claim.
3. **Hypothesis generation:** Develop competing hypotheses about what might explain observed open-source indicators.
4. **Bias &amp; gap analysis:** Reason through where collection or sources might be biased or incomplete.
5. **Scenario analysis:** Outline potential future scenarios and reasoning chains leading to each.

#### 🎯 RGCC use cases

1. **OSINT research assistant:** Role (open-source analyst), Goal (collect and summarize info on topics), Constraints (no targeted harassment or doxxing; only use open sources; no predictions about individuals).
2. **Source vetting assistant:** Role (source reviewer), Goal (classify new sources by topic, language, and basic reliability indicators), Constraints (no sensitive attribution; use standard scales only).
3. **Alert triage assistant:** Role (monitor), Goal (surface items relevant to defined watch-terms), Constraints (no auto-escalation; analysts decide).
4. **Sanitization helper:** Role (redaction assistant), Goal (help remove non-essential personal identifiers from OSINT excerpts in reports).
5. **Template enforcer:** Role (editor), Goal (enforce consistent structure/citations across analytic products), Constraints (no content changes beyond formatting).

### 🔟 Software Development / Engineering

#### ✅ CRISP use cases

1. **Requirements-to-user-stories:** Turn requirement docs into user stories with acceptance criteria and edge cases.
2. **Architecture documentation:** Generate architecture overviews (context diagrams, component descriptions) from design notes.
3. **API documentation:** Turn code comments and examples into developer portal-ready docs.
4. **Release notes:** Convert merged PR descriptions into release notes grouped by feature/bug/security.
5. **Design decision records (ADRs):** Turn meeting notes into standardized ADRs (context, decision, alternatives, consequences).

#### 🧠 CoT use cases

1. **Bug diagnosis reasoning:** Reason step-by-step through logs and error messages to propose likely causes and next investigative steps.
2. **Refactor planning:** Reason about trade-offs between different refactor approaches (big-bang vs incremental).
3. **Performance analysis:** Walk through potential sources of latency and order them by likely impact.
4. **Threat modeling brainstorm:** Reason through attack surfaces and possible mitigations for a given component.
5. **Migration planning:** Step-by-step plan for migrating from legacy stack to new stack, highlighting risks.

#### 🎯 RGCC use cases

1. **Code review copilot:** Role (reviewer), Goal (spot potential issues), Constraints (no auto-approval; no style wars; prioritize correctness/security).
2. **Test generator:** Role (QA engineer), Goal (propose test cases from requirements), Constraints (no editing production code).
3. **DevOps change-plan assistant:** Role (release engineer), Goal (generate change plans and rollback steps), Constraints (no direct system access).
4. **Technical-debt tracker:** Role (arch review assistant), Goal (summarize and classify tech debt items from backlogs), Constraints (no prioritization beyond given rules).
5. **Coding tutor:** Role (mentor), Goal (explain code and concepts), Constraints (no unsafe code; follow secure coding guidelines).

## A. DHS Immigration &amp; Security Operations (USCIS vetting, ICE threat monitoring)

#### CRISP

- Draft **vetting workflow guides** translating complex screening logic into stepwise SOPs.
- Produce **analyst shift handover summaries** from daily case notes and alert queues.
- Generate **data quality issue catalogs** from profiling results (e.g., missing fields, inconsistent IDs).

#### CoT

- Reason through **alert prioritization logic** for mixed immigration/security signals, outlining trade-offs between sensitivity and workload.
- Analyze multi-step **information flows** between systems (e.g., portal → vetting → case management) to identify bottlenecks.
- Step-by-step **impact analysis** of new data sources or rule changes on vetting workloads.

#### RGCC

- Build an **analyst copilot** : Role (screening analyst assistant), Goal (organize data and highlight anomalies), Constraints (no automatic derogatory labels; no final determinations; only summarize and compare).
- Set up a **policy-bound Q&amp;A assistant** for vetting guidelines, constrained to quote vetted policy text only.
- Use a **data catalog assistant** : Role (data steward), Goal (document datasets and fields used in vetting), Constraints (no speculation about hidden fields or external data).

### B. CBP Trade &amp; Workforce Planning (PWSS IDIQ, workforce planning task)

#### CRISP

- Turn **workforce survey results** into summarized findings and recommendations by office/role.
- Generate **role competency profiles** for trade analysts, auditors, and planners.
- Create **scenario narrative briefs** for workforce planning options (e.g., regional staffing shifts).

#### CoT

- Reason through **future workload scenarios** (trade volume shifts, new mandates) and staffing implications.
- Analyze **skill gaps** vs. future mission needs, step-by-step.
- Evaluate **organizational design options** (centralized vs. regionalized functions) with pros/cons.

#### RGCC

- Build a **workforce planning assistant** : Role (HR planner), Goal (summarize workforce data and scenario outputs), Constraints (no individual-level recommendations; aggregate only).
- Use an **initiative tracker assistant** : Role (PMO analyst), Goal (summarize status of workforce-related projects), Constraints (no altering status; only report).
- Create a **training recommendation helper** : Role (L&amp;D planner), Goal (suggest training themes), Constraints (no individual targeting, only by role/grade).

### C. Federal Acquisition &amp; eProcurement (e.g., VA eCMS support)

#### CRISP

- Turn **acquisition plan inputs** into structured plans with sections for requirements, market research, evaluation, and risk.
- Generate **performance work statement (PWS)** drafts from requirements notes.
- Create **source selection briefing decks** from evaluation records.

#### CoT

- Reason through **contracting strategy** options (IDIQ vs BPA vs single-award) and trade-offs.
- Analyze **evaluation score patterns** to identify where criteria might be unclear or mis-weighted.
- Reason step-by-step about **schedule risks** in procurement milestones.

#### RGCC

- Build an **acquisition assistant** : Role (1102 support), Goal (suggest clause packages and templates), Constraints (use only approved clause libraries; no legal advice).
- Set up a **documentation completeness checker** for acquisition packages with constraints to flag missing docs only.
- Use a **market research summarizer** that only aggregates open-source/vendor responses without recommending specific vendors.

### D. AI Data Modernization for DHS (ICE AI data modernization task)

#### CRISP

- Document **current-state data flows** and target-state architectures from SME interviews.
- Generate **data dictionary drafts** from schema definitions.
- Draft **AI use case one-pagers** for candidate analytics projects (problem, users, data, outcomes, risks).

#### CoT

- Reason through **data pipeline migration paths** (lift-and-shift vs re-platforming) with pros/cons.
- Evaluate **which datasets** provide the most value for early AI use cases.
- Analyze **risk and governance implications** of proposed AI integrations step-by-step.

#### RGCC

- Create a **data-governance assistant** : Role (data steward coach), Goal (map data uses to policies), Constraints (no approval of use; only policy mapping).
- Build an **AI use case intake assistant** : Role (portfolio triage), Goal (classify and summarize proposed AI use cases), Constraints (no go/no-go decisions).
- Set up a **metadata documentation helper** : Role (data catalog editor), Goal (draft dataset descriptions), Constraints (no guessing about unseen fields).