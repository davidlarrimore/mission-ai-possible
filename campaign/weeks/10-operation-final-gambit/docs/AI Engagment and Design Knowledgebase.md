**Whitepaper: Identifying Good AI Solutions With Customers**

**A practical problem-to-solution playbook for AI, GenAI, and LLM implementations**

**Executive summary**

Teams get better outcomes when they **start with the customer’s problem and constraints** , then select an AI pattern that matches: *retrieval vs generation* , *assist vs automate* , *structured vs unstructured data* , and *risk/oversight needs* . This whitepaper provides a repeatable customer engagement approach, a catalog of common AI solution patterns, and a **problem→solution matching guide** you can use in discovery workshops and solution design.

This playbook is anchored in:

- Human-centered design lifecycle practices (ISO 9241-210).
- NIST AI Risk Management Framework and GenAI Profile (risk/context, stakeholder impacts, and iterative measurement/management).
- Google PAIR’s People + AI Guidebook (identify user needs, define success, set expectations, and design feedback/control).
- CRISP-DM (business understanding → data understanding → modeling → evaluation → deployment).

**1) How to work with customers to identify good AI solutions**

**Step 1 — Frame the problem, not the tool**

Run a 60–90 minute discovery session focused on:

- **Who** is struggling (persona/role), **where** in the workflow, and **why** it hurts (time, errors, delays, rework).
- The “definition of done”: what outcome looks like in plain language.
- “What happens if we’re wrong?” (risk, rights/safety impact, reputational harm).

NIST’s AI RMF emphasizes mapping context, intended use, stakeholders, and impacts—and explicitly encourages considering non-AI options when they are more trustworthy for the situation.

**Deliverable:** a one-page problem statement with success metrics + constraints.

**Step 2 — Define success metrics customers actually care about**

Use a “before/after” approach:

- **Efficiency:** minutes saved per case, reduced handle time, reduced back-and-forth
- **Quality:** fewer errors, higher first-contact resolution, better compliance adherence
- **Experience:** higher CSAT, fewer escalations, reduced abandonment
- **Risk/Trust:** fewer policy violations, fewer unsafe outputs, better auditability

PAIR recommends translating user needs into measurable success criteria and designing for user trust through clear expectations and feedback/control loops.

**Deliverable:** 3–5 primary KPIs + guardrail metrics (e.g., “unsafe output rate”).

**Step 3 — Decide if AI is appropriate (fast triage)**

Ask four practical questions:

1. **Is the task repetitive or variable?**
2. **Is the input mostly structured (tables/fields) or unstructured (text/docs/calls)?**
3. **Do we need authoritative truth from customer content?**
4. **Does the system need to take actions, or only recommend/summarize?**

This lines up with the “business understanding first” discipline used in CRISP-DM, where the business goal and constraints come before modeling.

**Deliverable:** a short “AI fit” decision and a shortlist of solution patterns.

**Step 4 — Pick the simplest viable pattern, then mature**

Adopt a sequencing mindset:

- Start with **assistive** patterns (humans validate)
- Add **grounding** (RAG/search) before expanding scope
- Add **tools/actions** only when safety + audit are ready

NIST AI RMF + the GenAI Profile reinforce an iterative approach: govern/map/measure/manage and tailor controls to the system’s context and risk.

**2) Common AI solution patterns to consider**

Below are the “usual suspects”—the patterns customers most often end up with.

**A) Search and retrieval patterns (best when “find the right thing” is the problem)**

- **Semantic search / vector search** : retrieves similar items using embeddings and nearest-neighbor similarity—often the fastest win for knowledge discovery.
- **RAG (Retrieval-Augmented Generation)** : combines retrieval with generation to produce grounded answers; originally formalized as combining parametric models with non-parametric retrieval memory.
- **Knowledge graph + RAG (GraphRAG-style)** : when relationships matter (entities, provenance, linked policy sections), graphs can improve coherence and reduce “isolated chunk” retrieval.

**B) Conversational patterns**

- **Customer-facing chatbot** (bounded scope): good for FAQs and low-risk guidance, with escalation.
- **Agent assist copilot** : supports human agents with suggested answers, summaries, and retrieval—often the safest first step.
- **Tool-using assistant** : can call APIs to look up status, create tickets, schedule appointments (requires strong controls).

**C) Document and content processing patterns**

- **Intelligent Document Processing (IDP)** : uses OCR + NLP/ML and increasingly LLMs to extract, classify, summarize, and route documents.
- **Structured extraction pipelines** : when you need reliable field capture into systems of record.

**D) Automation patterns**

- **RPA / scripting automation** : best for deterministic, repetitive UI or system tasks; Gartner defines RPA as scripts (“bots”) that automate keystrokes/actions across applications.
- **RPA + AI** : use AI for unstructured variability (emails, documents, free text), and RPA for deterministic steps.

**3) Problem → Solution matching guide**

Use this in customer workshops as a “menu with rules.”

**Problem types and best-fit solutions**

| **Customer problem signal**                              | **Best first solution**                              | **Mature to (when ready)**                      | **Why this fits**                                    |
|----------------------------------------------------------|------------------------------------------------------|-------------------------------------------------|------------------------------------------------------|
| “We can’t find the right policy/page quickly.”           | Semantic search (vector search)                      | RAG Q&A with citations                          | Retrieval is the core need; generation is optional   |
| “Agents repeat the same answers; wrap-up takes forever.” | Agent assist copilot (summaries + suggested replies) | Customer-facing bot with handoff                | Humans already present to validate early             |
| “Users ask policy questions; wrong answers are risky.”   | RAG with strict scope + citations                    | Human-in-the-loop escalation + decision support | Grounding + auditability matters                     |
| “We have piles of PDFs/forms/emails.”                    | IDP (classify/extract/route)                         | LLM-based summarization + exception handling    | Start with extraction; add GenAI where helpful       |
| “Process is repetitive across systems.”                  | RPA / scripts                                        | RPA + AI for exception handling                 | Deterministic automation is safer/cheaper            |
| “We must understand relationships and provenance.”       | Knowledge graph + retrieval                          | Graph-guided RAG                                | Graphs help link entities and reduce missing context |
| “We need consistent routing/triage.”                     | Classification model (traditional ML)                | LLM triage with guardrails                      | Structured outcomes often don’t need GenAI           |

**A quick “GenAI vs traditional ML” rule**

- If the output is **a label, score, forecast, or anomaly flag** → traditional ML is often the simplest path (and easier to validate).
- If the input/output is **language-heavy** (summaries, Q&amp;A, drafting, dialog) → GenAI/LLMs are often the right fit.
- If the answer must be **grounded in customer content** → RAG or search-first is usually required.

**4) A practical customer workshop format (repeatable)**

**90-minute “AI Fit &amp; Pattern Selection” agenda**

1. **Journey + pain points (20 min)** — where the work breaks (ISO HCD mindset).
2. **Success metrics (10 min)** — 3 KPIs + 2 guardrails (PAIR).
3. **Risk &amp; constraints (15 min)** — what’s unacceptable; who is impacted (NIST AI RMF Map).
4. **Pattern shortlist (25 min)** — pick 1 “start” pattern + 1 “mature-to” pattern
5. **Pilot plan (20 min)** — data sources, evaluation approach, rollout scope (CRISP-DM discipline).

**Outputs:** problem statement, KPI set, risk notes, recommended pattern, pilot backlog.

**5) Common anti-patterns (bad fits) to watch for**

- “We want a chatbot” with no defined user problem or success metric.
- High-stakes decisions without a human escalation path or audit plan (NIST risk posture).
- Expecting an LLM to be the “system of record” instead of grounding in authoritative sources (RAG exists largely because parametric-only models struggle with precise, updatable factual knowledge).
- Automating a broken process (fix the workflow first; then automate).

**6) Conclusion**

A good AI solution starts with a well-framed customer problem, measurable success, and a pattern that matches the true nature of the work (retrieval, generation, classification, extraction, automation). Teams that adopt a “start simple, prove value, then mature” approach—grounded in human-centered design and risk management practices—ship faster and earn trust more reliably.