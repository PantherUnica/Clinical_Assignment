# Production, Monitoring & Continuous Improvement Plan — Veterinary Clinical Intelligence Platform

**Document status:** Draft v1.0 · Operational
**Date:** 2026-09-30
**Owner:** Product Operations + SRE/DevOps + AI Operations + Clinical Governance
**Source of truth:** [`VALIDATION_AND_BASELINE.md`](./VALIDATION_AND_BASELINE.md) §12. **Companions:** [`AI_ML_VALIDATION_SPEC.md`](./AI_ML_VALIDATION_SPEC.md) (§7 gates, §8 monitoring), [`SECURITY_SAFETY_SPEC.md`](./SECURITY_SAFETY_SPEC.md) (§5 incidents), [`TESTING_QA_STRATEGY.md`](./TESTING_QA_STRATEGY.md), [`BACKLOG_EXECUTION_PLAN.md`](./BACKLOG_EXECUTION_PLAN.md).

**What this document answers:** *how does the platform go from validated software into controlled production, and how is it operated, monitored, maintained, and safely evolved?* It does **not** redesign the product or repeat prior docs — it defines production operations, monitoring, incidents, releases, AI/knowledge updates, feedback, governance, and improvement. Undecided items are `TBD`; no policy is invented. Labels: **CONFIRMED / PROPOSED / TBD / FUTURE**.

**Operating principle carried into production:** the same baseline rules hold live — verify before generate, fail closed, no dose without species, human review before any record, full audit. Production monitoring exists to *prove these keep holding* and to catch it fast when they don't.

---

## 1 · Production Lifecycle (end-to-end, with responsibilities)

`Production Readiness → Release → Deployment → Monitoring → Incident Detection → Investigation → Resolution → Re-validation → Release`

| Stage | What happens | Lead | Supporting |
|---|---|---|---|
| **Production Readiness** | all gates green (QA §14, Security §9, AI/ML §7); sign-offs recorded | Product | Safety, Security, Clinical, Eng |
| **Release** | approve a specific **versioned bundle** (software + models + prompts + indexes + pharmacology + ontology + safety rules + SOAP templates) | Product + Eng | AI/ML, Security |
| **Deployment** | roll out (staged/canary `PROPOSED`); smoke verification | DEVOPS | Eng |
| **Monitoring** | technical + AI/ML + clinical monitoring live (§2) | SRE + AI Ops | Clinical |
| **Incident Detection** | alerts/feedback surface a problem | whoever detects → on-call | all |
| **Investigation** | reconstruct via audit; classify severity | Eng/AI Ops + Clinical (if clinical) | Security |
| **Resolution** | fix / contain / **rollback** to last known-good bundle | Eng + DEVOPS | AI/ML |
| **Re-validation** | re-run affected evals/safety/clinical gate before the fix ships | AI/ML + QA + Clinical | — |
| **Release (again)** | approved fix re-enters the release step | Product | — |

**Bundle rule (CONFIRMED):** because an answer depends on software *and* models *and* prompts *and* indexes *and* pharmacology *and* ontology *and* safety rules together, releases and rollbacks operate on the **whole versioned bundle**, not one part in isolation.

---

## 2 · Monitoring (three distinct layers)

Monitoring is split so the right team owns the right signal. PHI never appears in metrics (Security C7).

### 2.1 Technical monitoring (SRE/DevOps)
| Signal | Watch for | Alert on |
|---|---|---|
| System health / availability | service up/down | below availability target (`TBD`) |
| Latency | p50/p95/p99 per endpoint | above NFR-001 target (`TBD`) |
| Error rates | 4xx/5xx by service | spike vs baseline |
| API performance | throughput, saturation, rate-limit hits | degradation |
| Infrastructure | compute/memory/storage/queues | resource pressure |

### 2.2 AI/ML monitoring (AI Operations)
| Signal | Watch for | Alert on |
|---|---|---|
| Retrieval quality | online proxies (citation open/confirm), periodic offline re-eval | sustained decline |
| Knowledge freshness / drift | behaviour change after any corpus/index update | drift beyond expected |
| Model behaviour | output/refusal/uncertainty distributions | distribution shift |
| Citation failures | verification reject rate, verifier errors | spike |
| Hallucination signals | flagged unsupported-claim attempts | any increase |
| Pharmacology issues | `{no_data}` rates, dosing lookups | anomalies |
| Agent failures | child timeout/quorum, degraded runs | rising failure/partial rate |
| Model/token usage | per-query, per-model | cost/latency anomalies |

### 2.3 Clinical safety monitoring (Clinical Governance)
| Signal | Watch for | Alert on |
|---|---|---|
| Clinical safety events | reported unsafe dose / wrong species / unsupported claim shown | **any occurrence** |
| Fail-closed events | verifier/safety blocking generation | spike (component health) |
| Uncertainty behaviour | low-evidence/conflict flag rates | unexpected drop (over-confidence) |
| Faithfulness (live sample) | E-3 on sampled production answers | below gate |
| User-reported clinical issues | vet corrections/disputed citations | trend up |

---

## 3 · Incident Management (technical + clinical-safety)

**Severity (CONFIRMED, aligned with QA §12 / Security §5):**
- **SEV-1 / Critical:** clinical-safety incident (an AI response may have caused/contributed to a safety concern), data exposure, or full outage. → immediate escalation + consider rollback.
- **SEV-2 / Major:** degraded clinical quality, partial outage, security weakness.
- **SEV-3 / Minor:** limited impact, workaround exists.

**Process:** Detection → Triage/severity → Escalation → Investigation (reconstruct from audit: inputs, retrieval, verification outcomes, output, **bundle versions**) → Containment → **Rollback** (to last known-good bundle) → Resolution → Documentation → **Post-incident review (blameless)** with corrective actions and a new regression/eval/clinical case.

**Special handling — AI response linked to a clinical-safety concern (CONFIRMED):**
1. Treat as **SEV-1** until proven otherwise; notify Clinical Governance + Safety immediately.
2. Preserve the full audit trace of that query (do not delete/modify).
3. Assess patient impact with clinical input; determine if broader exposure exists (same pattern in other answers).
4. Contain: rollback or disable the affected path (fail closed) if risk is ongoing.
5. Root-cause across the whole bundle; add a clinical regression case that reproduces it.
6. **Re-validate** (safety suite + faithfulness + clinical review) before the fix returns to production.
7. Post-incident review includes Clinical Governance; record outcome and any disclosure obligations (regulatory scope `TBD`, D-10).

---

## 4 · Release & Change Management

Every change is classified; classification determines what validation is required **before** it reaches production. (Re-eval triggers from AI/ML §6.)

| Change type | Examples | Requires |
|---|---|---|
| **Software release** | app/API/service code | regression + integration + security review (if security-relevant) + release approval |
| **API change** | endpoint/contract | contract regression + client compatibility + approval |
| **Model change** | LLM / embedding / re-ranker / specialist | **full AI eval + safety suite + clinical re-validation** + regression + approval |
| **Prompt / config change** | prompts, thresholds, DAT config | AI eval (affected) + safety suite + **clinical review if answer-path** + regression |
| **DAT / agent change** | routing, add/modify agent | routing/orchestration tests (E-9) + pipeline eval + safety + approval |
| **Knowledge index update** | PMC re-index/re-embed | retrieval eval + faithfulness + drift check + regression |
| **Textbook / PMC source update** | new/updated corpus | ingestion validation + retrieval/faithfulness eval + versioning + clinical spot-check |
| **Ontology mapping change** | SNOMED/VeNom/LOINC | mapping accuracy + routing check + regression |
| **Pharmacology data update** | dosing/interactions | **pharmacology safety eval (E-7/S-2) + clinical review** + regression |
| **Safety rule change** | guardrails, fail-closed logic | safety suite (all) + security review + approval — **never relaxed without Clinical + Safety sign-off** |
| **SOAP template change** | note structure | SOAP eval (E-10) + review-before-save intact + regression |

**Rule (CONFIRMED):** anything that touches the **answer path** (models, prompts, indexes, pharmacology, ontology, safety rules) requires the matching **AI evaluation + safety suite**, and if it can change clinical output, **clinical re-validation**, before release. Pure infra/UX changes need regression + relevant review only.

---

## 5 · Knowledge & AI Maintenance (by change class)

Distinct maintenance tracks — each validated differently, all versioned:

- **Knowledge updates (source content):** new textbook/PMC/pharmacology/ontology data → re-ingest → version → **retrieval + faithfulness eval + clinical spot-check** → release in a bundle.
- **Index updates (re-embed/re-index without new sources):** → retrieval eval + drift check → release.
- **Prompt/configuration changes:** → affected AI eval + safety suite + clinical review if answer-path → release.
- **Model changes:** → **full eval + safety + clinical re-validation** (highest scrutiny) → release.
- **Software releases:** → regression + relevant review → release.

**Freshness cadence (`PROPOSED — TBD`):** how often PMC/pharmacology/ontology are refreshed is a decision (relates D-11 licences/cadence); every refresh is a knowledge update above.

---

## 6 · Continuous Feedback Loop

`Veterinarian feedback → Issue/Insight → Investigation → Product/AI/Clinical change → Testing → Validation → Release → Monitoring` (then back to feedback).

- **Capture:** in-product feedback (usefulness, disputed citations, corrections) + support + monitoring signals.
- **Triage & prioritize:** by **safety first**, then clinical usefulness, then UX/perf. A safety signal jumps the queue.
- **Controlled change (CONFIRMED):** feedback never changes clinical behaviour directly. It becomes a classified change (§4), goes through the required validation, and only then ships. **No hotfix bypasses the safety suite / clinical gate for answer-path changes.**
- **Close the loop:** the vet-facing issue is tracked to a release and confirmed resolved in monitoring; a regression/clinical case is added so it can't silently return.

---

## 7 · Production Governance

- **Ownership:** each layer has a named owner — SRE/DevOps (technical), AI Operations (AI/ML), Clinical Governance (clinical safety), Security (privacy/security), Product (overall). Specific names `TBD`.
- **Approval responsibilities:** answer-path and safety-rule changes require **Clinical + Safety sign-off**; security-relevant changes require **Security sign-off**; all production releases require **Product approval**.
- **Operational reviews (`PROPOSED` cadence `TBD`):** regular ops review (technical health), AI/ML review (eval/drift), and **clinical safety review** (incidents, faithfulness, feedback).
- **Clinical oversight:** Clinical Governance owns the clinical-safety monitoring, incident special-handling (§3), and the clinical gate for changes.
- **Audit & documentation:** every query reconstructable; every release records its bundle versions and approvals; every incident has a documented review.
- **Major-change decision-making:** significant changes (new model, new specialist, integration, scope expansion) go through governance approval with the required validation evidence attached.

---

## 8 · Long-Term Improvement (safe evolution)

All improvements preserve backward compatibility, traceability, and clinical safety; each is a classified change (§4) with its validation.

| Improvement | Notes | Status |
|---|---|---|
| Performance optimization | latency/cost; must not weaken verification/safety | ongoing |
| Knowledge expansion | more textbooks/PMC/pharmacology; re-validate | ongoing |
| Additional species | expand species coverage; species-safety re-validation per species | FUTURE |
| Additional specialist avatars | Oncology/Dentistry/Anesthesia; each clinically validated | FUTURE (OQ-9) |
| PMS/EHR integration | export; needs security + regulatory clearance | FUTURE (D-10) |
| Image interpretation | vision; new eval + safety class | FUTURE (OQ-14) |
| AI model improvements | swap/upgrade models; full re-validation | ongoing (`TBD` models) |
| New clinical capabilities | new question types/features; full spec→validate path | FUTURE |

**Guardrail:** no evolution ships that lowers a safety control without explicit Clinical + Safety governance approval and re-validation.

---

## 9 · Deliverable Artifacts

### 9.1 Production Readiness Checklist
- [ ] All release gates green (QA §14, Security §9, AI/ML §7); sign-offs recorded.
- [ ] Three monitoring layers live with alerts (§2).
- [ ] Incident process + on-call + escalation operational (§3).
- [ ] Rollback to last known-good **bundle** drilled and proven.
- [ ] Change-management classification in force (§4).
- [ ] Audit reconstructs any query; bundle versions recorded per release.
- [ ] Feedback capture + triage operational (§6).
- [ ] Governance owners + approval paths named (§7).
- [ ] Open decisions (§9.8) resolved or accepted with owner.

### 9.2 Monitoring Matrix
| Layer | Owner | Key signals | Alert trigger |
|---|---|---|---|
| Technical | SRE/DevOps | availability, latency, errors, infra | thresholds `TBD` |
| AI/ML | AI Operations | retrieval, drift, model behaviour, citation/hallucination, agents | drift/spike |
| Clinical safety | Clinical Governance | safety events, fail-closed, faithfulness (live), uncertainty rates | **any safety event** |

### 9.3 Incident Response Matrix
| Severity | Example | Response | Rollback? | Review |
|---|---|---|---|---|
| SEV-1 | AI response → possible clinical harm; data exposure; outage | immediate escalation; contain | **yes if ongoing risk** | mandatory (+ Clinical) |
| SEV-2 | degraded clinical quality; partial outage; security weakness | prioritized fix | if needed | yes |
| SEV-3 | minor, workaround exists | scheduled fix | no | logged |

### 9.4 Change Management Matrix
See §4 (change type → required validation). Answer-path change ⇒ AI eval + safety suite (+ clinical re-validation).

### 9.5 AI / Knowledge Update Process
Classify (knowledge / index / prompt-config / model / software) → validate per class (§5) → version the bundle → approve → release → monitor for drift → feed back.

### 9.6 Governance Model
Named owners per layer; Clinical + Safety sign-off for answer-path/safety changes; Security sign-off for security changes; Product approval for releases; regular technical/AI/clinical reviews; documented audit + approvals. (§7)

### 9.7 Continuous Improvement Loop
Feedback → Issue → Investigation → Classified change → Testing → Validation → Release → Monitoring → Feedback. Safety-first prioritization; no direct changes to clinical behaviour.

### 9.8 Open Decisions (`TBD` / DECISION REQUIRED)
- **PD-1** Deployment strategy (canary/blue-green `PROPOSED`) and rollout controls.
- **PD-2** Monitoring thresholds/alert levels (tie NFR-001/002, faithfulness gate).
- **PD-3** On-call model, incident SLAs, escalation owners (also SD-10).
- **PD-4** Operational/clinical review cadence.
- **PD-5** Knowledge-refresh cadence per source (also D-11).
- **PD-6** Regulatory obligations for incident disclosure/record-keeping (also D-10).
- **PD-7** Named governance owners across all layers.
- (Plus inherited D-/VD-/SD- decisions that gate the components being operated.)

---

*This plan defines how the platform is released, operated, monitored, maintained, improved, and safely evolved in production, without redesigning the product or repeating prior specs. Releases and rollbacks operate on the whole versioned bundle; answer-path changes always re-run AI evaluation, the safety suite, and (where clinical output can change) clinical re-validation; feedback never alters clinical behaviour without controlled validation. Undecided operational and regulatory items are marked `TBD`; nothing is invented.*
