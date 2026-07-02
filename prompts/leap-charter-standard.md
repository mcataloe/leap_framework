# LEAP Charter - Standard Operational Prompt

Run LEAP Charter using the current LEAP Framework.

LEAP Charter is the project-alignment front door. It establishes or reconciles Mission, project direction, Strategic Outcomes, Initiative identity, Roadmap posture, Domains, Architecture direction, source truth, documentation, and implementation readiness before focused Recon or implementation Prompt generation.

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the Layered House Standard Prompt format for staged implementation. It is not a mandatory lifecycle stage and it does not define the project's strategic documentation hierarchy.

Not every task starts at Charter. Focused Recon may proceed when Baseline Freshness Check finds the existing baseline fresh enough.

## Canonical project-documentation model

Use this preferred traceability hierarchy:

```text
Mission / Project Charter
        ↓
Strategic Outcome
        ↓
Initiative
        ↓
Delivery Unit
        ↓
Build Unit
```

Treat these as supporting views:

```text
Roadmap      = timing, priority, dependencies, milestones, release targets, status, parallelism
Domain Map   = persistent business, responsibility, ownership, or technical boundaries
Architecture = structural technical organization
```

Roadmap does not permanently own Initiative identity. Initiatives and Domains have a many-to-many relationship. Delivery Unit is conditionally collapsible for small work. Build Unit is not required to be independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and historical compatibility references.

## Required behavior

You must:

1. preserve the user's original wording
2. classify the request as Greenfield or Brownfield Mode
3. use the Ideation Loop to clarify vague intent
4. apply Materiality Gate before asking questions
5. inspect discoverable evidence before asking
6. separate Known, Assumed, Unknown, Contested, Needs Decision, and Deprecated items
7. identify Mission, target users, problem, current workflow, success event, MVP or current scope, non-goals, risks, and constraints when relevant
8. identify or reconcile Strategic Outcomes
9. identify or reconcile Initiative boundaries before detailed Build Unit planning
10. treat Roadmap as a scheduling and dependency view
11. identify persistent Domains separately from temporary Initiatives
12. identify Architecture direction separately from strategic hierarchy
13. identify Delivery Units when meaningful release, enablement, adoption, demonstration, or cross-repository boundaries exist
14. avoid forcing Delivery Units or separate files for trivial work
15. pressure-test whether custom implementation is needed
16. use readiness gates C0-C5
17. block implementation planning when hard blockers remain
18. classify legacy Layer docs semantically before renaming or moving them
19. identify downstream Recon, Prompt, or LHS recommendations
20. end with a gate decision

## Materiality Gate

Classify missing context as:

```text
Material - changes direction, readiness, source truth, scope, risk,
Architecture, implementation path, validation, acceptance criteria,
or compatibility.

Non-material - changes naming, wording, formatting, ordering, tone,
or minor preference.

Discoverable - should be inspected from repo, docs, contracts, or tooling.

Safe assumption - can be reasonably stated without changing the decision.
```

Question sequence:

```text
1. Inspect discoverable sources.
2. Convert non-material unknowns into stated assumptions.
3. Proceed on safe assumptions.
4. Ask only unresolved material questions.
5. Ask the smallest useful set, preferably no more than three at a time.
```

Hard blockers override Materiality Gate.

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
6. classify each legacy Layer as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or Needs Reconciliation
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

Do not globally replace `Layer`.

Preserve:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified Architecture Layers
- compatibility and historical references

Use `docs/maintainer/project-documentation-migration.md` when available.

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

## Materiality Check format

```text
### Material Unknowns
Questions or missing facts that would change direction, readiness,
source-truth hierarchy, scope, risk, Architecture, implementation path,
validation, acceptance criteria, or compatibility.

### Assumptions Proceeding Under
Reasonable assumptions used so Charter can continue.

### Deferred Non-Material Details
Naming, wording, formatting, or preference details that do not block the gate.

### Question Decision
Proceed with assumptions / inspect sources first / ask targeted questions.
```

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
