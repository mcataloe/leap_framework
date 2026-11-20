# LEAP Charter - Standard Operational Prompt

Run LEAP Charter using the current LEAP Framework.

LEAP Charter is the project-alignment front door. It establishes or reconciles Mission, project direction, Strategic Outcomes, Initiative identity, Roadmap posture, Domains, Architecture direction, source truth, documentation, and implementation readiness before focused Recon or implementation Prompt generation.

Charter is the first stage of the [LEAP lifecycle](../docs/leap.md). LEAP LHS is a Prompt format for staged implementation, not a lifecycle stage; see [LEAP LHS](../docs/leap-lhs.md).

Not every task starts at Charter. Focused Recon may proceed when Baseline Freshness Check finds the existing baseline fresh enough.

## Canonical project-documentation model

Charter establishes or reconciles the records in the [project documentation model](../docs/project-documentation-model.md) when the project uses them, or links an external work tracker instead.

## Required behavior

When a user explicitly asks for LEAP Discovery or conceptual Pressure Test without a full Charter, follow [Discovery and Pressure Test](../docs/user/leap-discovery.md) and [Semantic Workflow Routing](../docs/semantic-routing.md). Neither implies Charter artifact creation or authorization to mutate repository files.

You must:

1. preserve the user's original wording
2. classify the request as Greenfield or Brownfield Mode
3. use the Ideation Loop to clarify vague intent
4. apply Materiality Gate before asking questions, including any explicit `No Gate` modifier
5. inspect discoverable evidence before asking
6. separate Known, Assumed, Unknown, Contested, Needs Decision, and Deprecated items
7. identify Mission, target users, problem, current workflow, success event, MVP or current scope, non-goals, risks, and constraints when relevant
8. identify or reconcile Strategic Outcomes
9. identify or reconcile Initiative boundaries before detailed Build Unit planning
10. keep Roadmap, Domains, and Architecture as separate views from the planning hierarchy
11. identify Delivery Units only when meaningful release, enablement, adoption, demonstration, or cross-repository boundaries exist; do not force them or separate files for trivial work
12. pressure-test whether custom implementation is needed
13. block implementation planning when hard blockers remain
14. classify legacy Layer docs semantically before renaming or moving them
15. identify downstream Recon, Prompt, or LHS recommendations
16. end with a gate decision from the list below

## Materiality Gate

Apply the [Materiality Gate](../docs/materiality-gate.md):

```text
INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE
```

Default **Materiality-Gated** behavior:

```text
Hard blocker -> STOP
Discoverable -> INSPECT, then re-evaluate
Non-material -> ASSUME or DEFER
Material safely assumable and not requiring a decision now -> ASSUME + DISCLOSE
Material answer required for the next safe decision -> ASK
```

Explicit **No Gate**: ASK becomes ASSUME + DISCLOSE when safe. STOP remains STOP. No Gate does not bypass readiness requirements, source-truth integrity, authorization, destructive-change safeguards, sensitive-area checkpoints, security/privacy requirements, public-contract approval, or required human approval.

Re-evaluate only remaining or newly exposed uncertainty. Ask the smallest useful batch, preferably no more than three questions at a time unless exhaustive discovery is explicitly requested. There is no minimum question count.

## Greenfield Mode

Use for new projects, early ideas, or solutions without a stable repository, Roadmap, Architecture, or documentation baseline.

Greenfield Mode should help create or organize:

- Mission / Project Charter
- target users
- MVP boundary
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain map when useful
- Architecture direction
- initial data-model assumptions
- Delivery Units when implementation planning warrants them
- prompt backlog
- `AGENTS.md` guidance when applicable
- first recommended Recon or Prompt sequence

Do not overbuild documentation. Small projects may combine several concepts in one or a few files.

Do not generate detailed Build Units while Initiative boundaries, intended outcomes, or release boundaries remain unclear.

## Brownfield Mode

Use for existing or mid-buildout projects where LEAP must inspect repo reality, reconcile documentation, identify gaps, establish source truth, and prepare future work.

Brownfield Mode should:

1. inventory existing docs and source-truth entry points
2. classify documents
3. inspect the current solution and relevant repo reality
4. compare Mission, Strategic Outcomes, Initiatives, Roadmap, Domains, Architecture, Delivery plans, and implementation
5. identify stale, conflicting, duplicate, misleading, and archived material
6. classify each legacy Layer (see Legacy Layer handling)
7. fix safe documentation and planning gaps
8. create or update supplemental Markdown docs
9. produce a gap register
10. produce a migration map
11. prepare focused Recon and Prompt work

Brownfield Mode may update docs and planning artifacts directly. Runtime changes should normally become follow-up Prompts unless explicitly requested.

## Documentation reconciliation policy

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Do not mechanically rename or delete legacy docs. Preserve public paths unless a separately approved migration says otherwise.

## Legacy Layer handling

Classify legacy Layer docs with the [migration guide](../docs/maintainer/project-documentation-migration.md) before renaming or moving them. Do not globally replace `Layer`.

## No-build review

For new or strategically material work, ask:

```text
What happens if we do nothing?
What manual workflow solves most of this?
What spreadsheet, checklist, template, or lightweight doc solves most?
What existing product solves most?
What integration, script, no-code automation, or service solves most?
What process or behavior change solves most?
Why is custom software justified?
Why is AI specifically justified, if proposed?
What would make this not worth building?
```

## Required output

```text
# LEAP Charter - <Project Name or Working Title>

## 1. Mode and Intake Classification
## 2. Original User Wording
## 3. Current Understanding
## 4. Ideation Loop Status
## 5. Materiality Check
## 6. Evidence Labels
### Known
### Assumed
### Unknown
### Contested
### Needs Decision
### Deprecated
## 7. Discovery Questions, if needed
## 8. Readiness Gate
## 9. Greenfield or Brownfield Findings
## 10. No-Build / Alternative-Solution Review
## 11. Mission / Project Charter Recommendation
## 12. MVP Boundary or Current Scope Boundary
## 13. Strategic Outcomes
## 14. Initiative Registry Recommendation
## 15. Roadmap Recommendation
## 16. Domain and Architecture Recommendations
## 17. Delivery Unit Recommendations, when warranted
## 18. Concrete Non-Goals
## 19. Risks and Constraints
## 20. Documentation Baseline Recommendation
## 21. Source-of-Truth Recommendation
## 22. Gap Register
## 23. Migration Map, if Brownfield
## 24. Legacy Layer Classification, if present
## 25. Baseline State Recommendation
## 26. Prompt Backlog Recommendations
## 27. Human Checkpoints Required
## 28. Recommended Next LEAP Recon / LEAP Prompt / LEAP LHS
## 29. Gate Decision / Next Step
```

Omit sections with nothing material. Do not pad with N/A. Keep the remaining section numbers unchanged.

Section 8 states whether direction is ready for Recon or Prompt generation and names any blockers. Section 29 records the final decision from the gate decision list.

## Materiality Check format

```text
### Clarification Mode
Materiality-Gated / No Gate

### Material Unknowns
### Assumptions Proceeding Under
### Deferred Non-Material Details
### Stop Conditions / Hard Blockers
State "None" when no hard blockers remain.
### Question Decision
Proceed with assumptions / inspect sources first / ask targeted questions / stop
```

See [Materiality Check output](../docs/materiality-gate.md#materiality-check-output) for field meanings.

## Gate decisions

Use an explicit next step, such as:

- Continue Discovery
- Draft Concept Brief
- Pressure Test Further
- Narrow MVP First
- Needs Human Decision
- Reconcile Docs First
- Proceed to Recon
- Generate LEAP Prompt
- Do Not Build Yet

Do not generate runtime implementation changes unless explicitly requested. Risky code, schema, API, UI, auth, workflow, infrastructure, data, or Architecture changes should become follow-up LEAP work.
