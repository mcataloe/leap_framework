# LEAP Charter Request Template

Use this template when starting a solution or reconciling an existing project before focused Recon or implementation Prompt generation.

LEAP Charter is scan-first and question-second. After LEAP `AGENTS.md` files are initialized, the preferred invocation remains:

```text
Run LEAP Charter.
```

or:

```text
Run LEAP Charter for this repo.
```

The user should not have to complete a large intake form before the agent inspects available evidence.

## Canonical project-documentation model

Charter establishes or reconciles the records in the [project documentation model](../docs/project-documentation-model.md) when the project uses them, or links an external work tracker instead. The governing behavior is the [LEAP Charter standard](../prompts/leap-charter-standard.md).

## Scan-first operating model

When repository or project files are available, inspect before asking:

- global and repository `AGENTS.md`
- `docs/00_start_here.md`
- Project Charter, product strategy, and planning records the project uses (Strategic Outcomes, Initiatives, Roadmap, Domain and Architecture docs, Delivery and Build Unit plans)
- existing legacy Layer docs
- source code, config, schemas, tests, and scripts
- package, build, and CI/CD files
- decisions, prompts, validation, and handoff records
- gap registers, migration maps, archives, and baseline metadata

Do not treat missing user-supplied context as a blocker until discoverable evidence has been inspected.

## Materiality Gate

Apply the [Materiality Gate](../docs/materiality-gate.md) (`INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE`). Check hard blockers first and inspect discoverable evidence before asking. Default mode is **Materiality-Gated**: ask only for answers the next safe decision needs. Under explicit **No Gate**, ASK becomes ASSUME + DISCLOSE when safe; STOP remains STOP, and No Gate never bypasses source-truth integrity, authorization, destructive-change safeguards, sensitive-area checkpoints, public-contract approval, or required human approval. Ask the smallest useful set, preferably no more than three questions at a time.

## Charter discovery flow

### 1. Determine Charter mode

Infer:

- Greenfield
- Brownfield
- documentation reconciliation
- source-truth reset
- implementation ahead of planning
- agent should recommend

### 2. Infer the starting signal

Examples:

- new solution needing baseline docs
- existing repo needing LEAP alignment
- stale, missing, duplicate, or conflicting docs
- parallel work not represented in the Roadmap
- existing implementation ahead of Initiative or Delivery planning
- legacy Layer material needing semantic reconciliation

### 3. Populate known context from evidence

Infer when possible:

- solution name and Mission
- target users and current workflow
- MVP or current scope boundary
- Strategic Outcomes
- current and proposed Initiatives
- active Roadmap placement and parallel work
- persistent Domains
- Architecture direction
- Delivery Units and Build Units already present
- legacy Layer semantics
- implementation posture
- canonical, stale, duplicate, and conflicting docs
- existing and open decisions
- technical constraints
- timeline and urgency
- sensitive areas and compliance
- readiness for Recon or Prompt generation

Do not leave discoverable facts as blank intake fields.

### 4. Ask only material Discovery Questions

Questions should only cover facts that change:

- Mission or direction
- Strategic Outcomes
- Initiative identity or boundary
- Roadmap posture
- Domain or Architecture ownership
- MVP or scope boundary
- source-truth decisions
- risk posture
- readiness gate
- recommended next LEAP work

If no blockers remain, state:

```text
No blocking Charter questions remain based on the current repository and documentation scan.
```

## Copy-ready Charter request

```text
Run LEAP Charter using the current LEAP Framework.

Charter settings:
- Scan first and ask questions second.
- Apply Materiality Gate before asking discovery questions.
- Infer Charter mode, starting signal, and known context from repo/docs evidence.
- Preserve the raw invocation or starting signal.
- Separate Known, Assumed, Unknown, Contested, Needs Decision, and Deprecated items.
- Pressure-test whether custom software is needed where relevant.
- Establish or reconcile Mission / Project Charter and MVP or current scope boundary.
- Establish or reconcile Strategic Outcomes and Initiatives before detailed Build Unit planning, when the project uses them.
- Keep Roadmap, Domains, and Architecture as separate views; identify Delivery Units only when a meaningful boundary exists.
- If Brownfield, inventory and classify existing docs before relying on them.
- If legacy Layer docs exist, classify each with the migration guide before renaming or moving it. Do not globally replace Layer.
- Apply this Brownfield policy:
  Canonicalize forward. Archive backward. Preserve traceability. Never let stale docs compete with source-of-truth docs.
- Update AGENTS.md Baseline State only when this Charter performs an authorized full reconciliation or baseline update.
- Treat leap.baseline.yaml as canonical machine-readable baseline metadata when it exists.
- Do not generate runtime implementation changes unless explicitly requested.
- Capture runtime work as follow-up Recon, Prompt, or LHS recommendations.
- Use LHS only when staged repository or documentation implementation is warranted.

Required workflow:
1. Scan repository, docs, and AGENTS guidance.
2. Determine Charter mode and starting signal.
3. Infer known context.
4. Apply Materiality Gate.
5. Label evidence and assumptions.
6. Identify documentation and repo-reality drift.
7. Route unresolved context through ASK / ASSUME / STOP according to the active clarification mode.
8. Re-evaluate only remaining or newly exposed material uncertainty.
9. Run no-build review where relevant.
10. Define Mission, scope boundary, and non-goals.
11. Define or reconcile Strategic Outcomes.
12. Define or reconcile Initiative identity and Roadmap posture.
13. Identify Domain, Architecture, and Delivery planning needs.
14. Recommend documentation baseline and source-truth ownership.
15. Create gap register and Brownfield migration map when needed.
16. Recommend next Recon, Prompt, LHS, Validation, or Handoff work.
17. Make a gate decision.

Return the LEAP Charter output only. Include Clarification Mode, Stop Conditions / Hard Blockers, and a Question Decision supporting "stop" in the Materiality Check.
If the next safe gate decision requires a material answer that cannot safely be assumed, ask the next small material question round (including under No Gate when an assumption would be unsafe). Under No Gate, continue with explicit disclosed assumptions when safe instead of asking. If a hard blocker exists, stop and report the checkpoint needed; never generate implementation plans past STOP.
```

## Fallback when no repo or files are available

```text
Run LEAP Charter using the current LEAP Framework.

No repository or project files are available to scan.

Minimal starting context:
- Solution or working title:
- Greenfield / Brownfield / you recommend:
- Brief project description or Mission:
- Known target users and current workflow:
- Known Strategic Outcomes or desired changes:
- Known Initiatives, Roadmap notes, or parallel work:
- Known Domains or Architecture constraints:
- Known source-truth concerns, risks, or sensitive areas:

Apply Materiality Gate before follow-up questions. In Materiality-Gated mode, ask only for missing answers that materially change the next safe gate decision. In No Gate mode, use explicit disclosed assumptions when safe. Hard blockers still stop.
```

## Expected Charter sections

```text
# LEAP Charter - <Project Name or Working Title>

## 1. Mode and Starting Signal
## 2. Repository and Documentation Scan Summary
## 3. Current Understanding
## 4. Materiality Check
## 5. Evidence Labels
### Known
### Assumed
### Unknown
### Contested
### Needs Decision
### Deprecated
## 6. Discovery Questions, if needed
## 7. Readiness Gate
## 8. Mission / Project Charter Recommendation
## 9. MVP or Current Scope Boundary
## 10. Strategic Outcomes
## 11. Initiative Registry Recommendation
## 12. Roadmap Recommendation
## 13. Domain and Architecture Recommendations
## 14. Delivery Unit Recommendations, when warranted
## 15. Source-of-Truth Inventory and Recommendation
## 16. Gap and Drift Register
## 17. Legacy Layer Classification, if present
## 18. Migration Map, if Brownfield
## 19. Baseline State Recommendation
## 20. Concrete Non-Goals
## 21. Risks and Constraints
## 22. No-Build / Alternative-Solution Review, if relevant
## 23. Prompt Backlog Recommendations
## 24. Recommended Next LEAP Recon / LEAP Prompt / LEAP LHS / Validation / Handoff
## 25. Gate Decision / Next Step
```

Omit sections with nothing material. Do not pad with N/A. Keep the remaining section numbers unchanged. Section 7 states whether direction is ready for Recon or Prompt generation and names any blockers; section 25 records the final gate decision.

## LHS note

LEAP LHS stages implementation work; see [LEAP LHS](../docs/leap-lhs.md). Greenfield Charter should usually avoid LHS during early shaping. Brownfield Charter may recommend or use LHS only after the reconciliation plan is clear and repository-changing documentation work needs staged execution.
