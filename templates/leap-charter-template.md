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

LEAP Charter should use this preferred traceability hierarchy:

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

Treat these as separate supporting views:

```text
Roadmap      = timing, priority, milestones, dependencies, release targets, status, parallelism
Domain Map   = persistent responsibility boundaries
Architecture = technical structure
```

Roadmap does not permanently own Initiative identity. Initiatives may run in parallel and may span Domains or repositories. Delivery Unit is conditionally collapsible. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning term. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

## Scan-first operating model

When repository or project files are available, inspect before asking:

- global and repository `AGENTS.md`
- `docs/00_start_here.md`
- Project Charter and product strategy
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain and Architecture docs
- Delivery Unit and Build Unit plans
- existing legacy Layer docs
- source code, config, schemas, tests, and scripts
- package, build, and CI/CD files
- decisions, prompts, validation, and handoff records
- gap registers, migration maps, archives, and baseline metadata

Do not treat missing user-supplied context as a blocker until discoverable evidence has been inspected.

## Materiality Gate

Classify missing context as:

```text
Material - changes direction, readiness, source truth, scope, risk,
Architecture, implementation path, validation, acceptance criteria,
or compatibility.

Non-material - changes naming, wording, formatting, ordering, tone,
or minor preference.

Discoverable - should be inspected before asking.

Safe assumption - can be stated without changing the gate decision.
```

Use this sequence:

```text
1. Inspect discoverable sources.
2. Convert non-material unknowns into stated assumptions.
3. Proceed on safe assumptions.
4. Ask only unresolved material questions.
5. Ask the smallest useful set, preferably no more than three.
```

Hard blockers still require a human decision.

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
- Use readiness gates C0-C5.
- Pressure-test whether custom software is needed where relevant.
- Establish or reconcile Mission / Project Charter and MVP or current scope boundary.
- Establish or reconcile Strategic Outcomes.
- Establish or reconcile an Initiative registry before detailed Build Unit planning.
- Treat Roadmap as a scheduling, priority, dependency, milestone, release, status, and parallelism view.
- Treat Domains as persistent responsibility boundaries with a many-to-many relationship to Initiatives.
- Treat Architecture as technical structure, not the strategic hierarchy.
- Identify Delivery Units only when meaningful release, enablement, adoption, demonstration, or cross-repository boundaries exist.
- Allow the Delivery Unit level to collapse for small work.
- Do not define Build Units as necessarily independently deployable.
- If Brownfield, inventory and classify existing docs before relying on them.
- If legacy Layer docs exist, classify each as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or Needs Reconciliation.
- Do not globally replace Layer or rename public paths solely for terminology consistency.
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
7. Ask only unresolved material questions.
8. Run no-build review where relevant.
9. Define Mission, scope boundary, and non-goals.
10. Define or reconcile Strategic Outcomes.
11. Define or reconcile Initiative identity and Roadmap posture.
12. Identify Domain, Architecture, and Delivery planning needs.
13. Recommend documentation baseline and source-truth ownership.
14. Create gap register and Brownfield migration map when needed.
15. Recommend next Recon, Prompt, LHS, Validation, or Handoff work.
16. Make a readiness-gate decision.

Return the LEAP Charter output only.
If more information is needed, ask the next small material question round instead of producing implementation plans.
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

Apply Materiality Gate before asking follow-up questions. Ask only for missing answers that materially change the gate decision or recommended next LEAP step.
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

## LHS note

LEAP LHS stages implementation work. It does not define the project's strategic hierarchy. Greenfield Charter should usually avoid LHS during early shaping. Brownfield Charter may recommend or use LHS only after the reconciliation plan is clear and repository-changing documentation work needs staged execution.
