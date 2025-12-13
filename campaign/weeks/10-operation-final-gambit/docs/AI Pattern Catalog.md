**Pattern Catalog (start simple → mature)**

Each pattern includes: **Definition** , **Start here** , **Example** , **Mature to next** .

**1) Deterministic Automation (Scripting / RPA)**

**Definition:** Automate repeatable steps using scripts or “bots” that mimic user actions across systems (keystrokes, clicks, form entry). Gartner defines RPA as a productivity tool where scripts (“bots”) execute transaction steps in a process.

**Start here when**

- The task is stable, rules-based, and you can specify steps clearly.
- Inputs/outputs are structured (forms, fields, known screens).

**Example**

- “Every morning, download a report, rename it, upload to SharePoint, email a distribution list.”

**Mature to next**

- If variability appears (emails, PDFs, free text), add **IDP** (Pattern 2) or **LLM exception handling** (Pattern 8/9), while keeping the deterministic core.

**2) Intelligent Document Processing (IDP)**

**Definition:** Automates data capture from documents (PDFs, scans, email attachments) using OCR + NLP/ML, extracting fields and routing into downstream workflows. AWS describes IDP as automating manual data entry from paper/document images into digital processes.

**Start here when**

- The “work” is actually document intake: classify, extract fields, validate, route.
- The organization currently uses manual data entry or basic OCR.

**Example**

- “Extract invoice number, vendor, amount, and due date from emailed PDFs; push to ERP; flag low-confidence fields for review.”

**Mature to next**

- Add an LLM for: summarizing long documents, generating “missing info” requests, or explaining extraction results—while preserving HITL on low-confidence fields.

**3) Semantic Search / Vector Search**

**Definition:** Represent text as embeddings and retrieve similar items using nearest-neighbor similarity (“vector search”). OpenSearch describes vector search as similarity/nearest-neighbor search for items most similar to an input; Elastic documents semantic search over vector embeddings using kNN.

**Start here when**

- Users mostly need: “Find the right policy/article/ticket/case like this.”
- You don’t need the system to *write* answers—just *find* them.

**Example**

- “Show me the most relevant SOP sections for ‘emergency procurement justification’.”

**Mature to next**

- Add **Search UX improvements** (filters, facets, snippet highlighting), then consider **RAG** only if users truly need synthesized answers.

**4) Search-First Assistant (Retrieve + Cite, Minimal Generation)**

**Definition:** A UI that retrieves the best sources and presents them (snippets, citations), optionally with a short extractive summary. This stays closer to “search” than “chat.”

**Start here when**

- Accuracy matters and users prefer to read sources.
- You want low hallucination risk.

**Example**

- “Top 5 relevant HR policies + 3-line summary + direct links + ‘ask a human’ button.”

**Mature to next**

- Add light generation: “Draft answer *based only on these sources* ” with citations (Pattern 5).

**5) Naive RAG Q&amp;A (Retrieval-Augmented Generation)**

**Definition:** Combine retrieval from a document index with an LLM that generates an answer grounded in retrieved passages. Microsoft calls RAG an industry-standard approach for using proprietary data the model doesn’t know.

(Foundational research: RAG combines parametric memory (model) with non-parametric memory (retrieved passages).  )

**Start here when**

- Users ask questions and want a direct answer **based on internal content** .
- You can constrain content sources (approved corpus).

**Minimum viable build**

- Ingest docs → chunk → embed → vector index → retrieve top-k → prompt LLM with retrieved text → answer + citations.

**Example**

- “Answer questions about procurement policy using only the acquisition manual and recent memos.”

**Mature to next**

- If you see poor answers, don’t jump to “bigger models”—move to **Advanced RAG** (Pattern 6): better chunking, query rewriting, reranking, evaluation harness.

**6) Advanced RAG (Production RAG)**

**Definition:** A more realistic RAG pipeline with structured **ingestion** , **inference** , and **evaluation** stages; Microsoft explicitly distinguishes naive vs advanced RAG and emphasizes a rigorous design/evaluation approach.

**Start here when**

- Naive RAG fails due to: irrelevant retrieval, missing context, conflicting docs, long docs, or noisy content.

**Common “maturity upgrades”**

- **Chunking strategy** tuned to doc types (policies vs FAQs vs tickets)
- **Hybrid retrieval** (keyword + vector)
- **Reranking** retrieved passages
- **Query rewriting / decomposition**
- **Response post-processing** (citations, refusal when evidence is weak)
- **Evaluation harness** (test sets, regression tracking)

**Example**

- “Citizen services Q&amp;A: query gets rewritten, retrieves across multiple policy libraries, reranks, returns cited answer + ‘what I used’ list.”

**Mature to next**

- If users ask multi-part questions requiring multiple lookups, consider **agentic retrieval** (Pattern 7). Microsoft describes “agentic retrieval” as breaking complex queries into subqueries executed in parallel.

**7) Agentic Retrieval (Multi-step Retrieval, Still “Read-Only”)**

**Definition:** The LLM plans multiple retrieval steps (subqueries), gathers evidence, then synthesizes. This adds “planning” but can still be kept read-only.

**Start here when**

- Questions are complex: “Compare, reconcile, or explain across multiple sources.”
- You need better coverage than single-shot retrieval.

**Example**

- “What changed between Policy A (2023) and Policy A (2025) and what does it mean for small businesses?”

**Mature to next**

- If the user wants the system to *do things* (create cases, update status), move to tool-using assistants (Pattern 9).

**8) Agent Assist (Copilot for employees)**

**Definition:** An assistant embedded in an employee workflow (contact center, ITSM, casework) that provides recommendations, summaries, and knowledge suggestions in real time. Microsoft’s “Smart assist” is explicitly described as giving real-time recommendations like knowledge articles, similar cases, and next-best steps.

**Start here when**

- Mistakes are costly and you want a human quality gate.
- You need rapid iteration with lower external risk.

**Example**

- “During a support chat, suggest the best KB article + a draft reply; after the call, generate case summary.”

**Mature to next**

- Promote the best-performing intents into **customer self-service** with safe escalation (Pattern 10). Handoff patterns with conversation context/history are documented in Microsoft guidance.

**9) Tool-Using Assistant (Function/Tool Calling)**

**Definition:** The model calls external functions/APIs to fetch data or take actions. OpenAI describes function (tool) calling as letting models interface with external systems and data outside training.

OpenAI’s agent framing: an agent is an LLM equipped with **instructions, tools, and handoffs** .

**Start here when**

- The problem isn’t just answering—it’s completing tasks (status checks, ticket creation, scheduling, form submission).

**Example**

- “Look up benefits application status → explain next steps → offer to schedule an appointment → create a case if needed.”

**Mature to next**

- Add: approvals for sensitive actions, audit logs, rollback paths, and session memory for reliable handoffs. (OpenAI provides patterns for session memory and handoff resilience.)

**10) Customer/Citizen-Facing Assistant with Escalation (Hybrid Self-Service)**

**Definition:** A user-facing chatbot (often RAG-backed) that resolves low-risk requests and escalates to humans with full context. Microsoft Copilot Studio and Azure Bot Service guidance describe handing off to a live agent with context/transcript/history.

**Start here when**

- You can strictly bound scope and provide a reliable “escape hatch.”
- You’ve validated content quality internally (Patterns 5–8).

**Example**

- “Taxpayer Q&amp;A bot answers ‘where do I file X?’; escalates when user asks eligibility determination; passes transcript + summary to agent.”

**Mature to next**

- Promote stable flows into transactional automation (Pattern 9 + workflows), but only for low/medium risk actions first.

**11) Knowledge Graph + Retrieval (Relationship-Heavy Domains)**

**Definition:** Represent facts as graphs of subject–predicate–object triples (RDF). W3C defines RDF graphs as sets of subject–predicate–object triples used to describe resources.

**Start here when**

- Relationship reasoning matters: provenance, “who is connected to what,” multi-entity traceability.

**Example**

- “Show all vendors connected to a contract vehicle, their past performance, and related compliance findings; use RAG to explain the result.”

**Mature to next**

- Combine with semantic retrieval (graph for relationships + vectors for meaning) and apply in targeted domains rather than everywhere.

**Concrete “mature when…” signals (so teams don’t over-engineer)**

Use these as decision triggers:

- **Move from Semantic Search → RAG** when users consistently ask for “the answer,” not “the document,” and you can ground in authoritative sources.
- **Move from Naive RAG → Advanced RAG** when retrieval misses key passages, or answers vary wildly due to chunking/noise; Microsoft highlights advanced RAG design/evaluation phases for real-world use.
- **Move from Internal Copilot → External Bot** only when escalation/handoff is reliable and you can pass context/transcript cleanly.
- **Move from “Answering” → “Doing” (tool use)** only when you can bound permissions and audit actions; function/tool calling is explicitly for interfacing with external systems.
- **Move to agentic retrieval / multi-step plans** when single-shot retrieval can’t cover multi-part questions; Microsoft describes agentic retrieval as decomposing complex queries into focused subqueries.