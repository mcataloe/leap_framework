# LEAP Recon - Standard Operational Prompt

Run LEAP Recon using the current LEAP Framework.

Recon investigates a focused Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, question, or legacy Layer. It is the source-truth, repo-reality, drift, dependency, risk, planning-boundary, capability-selection, and implementation-safety pass before Prompt generation.

Recon is normally investigative and non-mutating unless explicitly authorized.

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP Charter is not required before every Recon. Every Recon begins with a lightweight Baseline Freshness Check.

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

Treat Roadmap, Domain Map, and Architecture as separate supporting views.

- Roadmap schedules and prioritizes Initiatives and Delivery Units.
- Domain Map describes persistent responsibility boundaries.
- Architecture describes technical structure.
- Delivery Unit may be collapsed for small work.
- Build Unit is not necessarily independently deployable.
- LEAP Skill is an orthogonal reusable execution-capability primitive, not a planning level.
- Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level.

Canonical Skill guidance: `docs/leap-skills.md`.

## Required behavior

You must:

1. perform Baseline Freshness Check
2. identify residual Ideation Loop questions
3. apply Materiality Gate before asking questions
4. require or construct a source-of-truth manifest
5. treat Brownfield Charter outputs as valid inputs
6. classify docs and legacy planning artifacts
7. inspect repo reality before implementation planning
8. treat repo reality as operational truth when docs conflict unless a human decides otherwise
9. inspect branch, worktree, and PR drift when available
10. search for already-existing functionality
11. detect stale assumptions, stale docs, stale Prompts, stale Roadmap claims, and stale legacy Layer claims
12. inspect `AGENTS.md` and baseline metadata when present
13. run Dependency & Contract Recon when relevant
14. identify cross-Initiative and cross-Domain impacts
15. identify cross-repository, contract, release, and merge-order impacts
16. evaluate risk and destructive-change implications
17. perform Planning Boundary Review before generating Build Units
18. determine whether the target is Initiative-sized, Delivery-Unit-sized, Build-Unit-sized, Domain-oriented, Architecture-oriented, a Phase, or an ambiguous legacy Layer
19. refine Delivery Units when meaningful release, enablement, adoption, demonstration, or cross-repository boundaries exist
20. generate or refine Build Units only after Initiative and Delivery Unit boundaries are clear enough
21. perform Capability / Skill Review after Build Unit boundaries are clear enough
22. prefer ordinary agent reasoning and repository guidance when no explicit Skill materially improves execution
23. for each selected Skill, identify its source, loading method, required or optional status, tool and permission fit, and Skill-specific verification
24. keep Skill capability separate from Build Unit scope and execution authority
25. identify human checkpoints
26. distinguish LEAP process tier from Agent Execution Configuration
27. recommend agent/tool, Codex Plan Mode, model, reasoning, execution mode, validation, Skill loading posture when used, and commit posture when Prompt generation is allowed
28. recommend LHS only when implementation gravity warrants it
29. end with a gate decision

## Brownfield Charter inputs

Use these when present:

```text
- document inventory
- canonical and supporting docs lists
- stale / archived / do-not-use list
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain map
- Architecture docs
- Delivery and Build Unit plans
- reusable Skill / capability sources already adopted by the project
- gap register
- reconciliation notes
- migration map
- prompt backlog
- recommended next LEAP sequence
```

If source truth remains unsafe, use `Reconcile Docs First` or `Continue LEAP Charter`.

## Baseline Freshness Check

Answer:

```text
Is the repo/source-truth baseline fresh enough for this Recon?
```

Inspect, when available:

1. repository `AGENTS.md`
2. LEAP Baseline State or `leap.baseline.yaml`
3. source-truth entry point
4. Project Charter and Strategic Outcomes
5. Initiative registry and Roadmap
6. Domain and Architecture docs
7. Delivery Unit and Build Unit plans
8. APIs, schemas, decisions, dependencies, and contracts relevant to the target
9. archive and stale-doc guidance
10. gap register, migration map, and prompt backlog
11. relevant repo reality
12. doc-code conflicts and broken references
13. evidence of stale planning claims

Use one outcome:

```text
Fresh enough
Minor drift
Material drift
Unsafe source-truth conflict
```

Normal Recon may recommend baseline metadata but must not silently create it.

## Source-of-Truth Manifest Check

```text
# Source-of-Truth Manifest Check

- Project:
- Date:
- Target branch:
- Base branch:
- Mission / Project Charter path:
- Strategic Outcomes path:
- Initiative registry path:
- Current Initiative:
- Active Roadmap path:
- Domain map path:
- Canonical Architecture docs:
- Current Delivery Unit, if used:
- Current Build Unit / bounded task:
- Active decisions / ADRs:
- Prompt backlog path:
- Execution log / drift ledger path:
- Cross-Initiative / Cross-Domain impact map path:
- Dependency register path:
- Reusable Skill / capability sources, if any:
- Baseline record path:
- Brownfield document inventory path:
- Gap register path:
- Migration map path:
- Legacy Layer docs requiring classification:
- Stale / archived / do-not-use docs:
- AGENTS.md path and Agent Pack status:
- Open branches / PRs affecting the work:
- Repo reality summary:
- Known doc-code conflicts:
- Human owner / approver:
- Last reviewed:
```

Skill definitions are capability instruction sources, not automatically project source truth outside the capability contract they explicitly own.

## Materiality Gate

Classify missing context as:

```text
Material - changes Architecture, scope, risk, source truth, validation,
acceptance criteria, compatibility, or implementation path.

Non-material - changes naming, wording, formatting, or preference.

Discoverable - should be inspected before asking.

Safe assumption - can be stated without changing the decision.
```

Inspect first. Ask only unresolved material questions.

## Required repo-reality inspection

Inspect, when available:

- target and base branches
- worktrees and open PRs
- current implementation and tests
- routes, APIs, contracts, schemas, and migrations
- UI components and workflows
- auth/session/permission behavior
- package and dependency files
- IaC and CI/CD
- canonical docs and planning records
- Initiative, Delivery Unit, and Build Unit status
- execution logs and impact maps

## Legacy Layer classification

Do not globally replace `Layer`.

When a legacy Layer appears, classify it as:

- Initiative
- Delivery Unit
- Build Unit
- Domain
- Architecture Layer
- Phase
- mixed or unclear collection

Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and historical references.

Use migration guidance when available.

## Planning Boundary Review

Determine whether the target is:

- one or more parallel Initiatives
- one Delivery Unit
- one Build Unit
- a persistent Domain concern
- an Architecture concern
- a chronological Phase
- an ambiguous legacy Layer

A Delivery Unit is warranted when several Build Units, several repositories, several release increments, or a meaningful deployable/adoptable boundary exists.

A Build Unit must be bounded enough to implement, test, review, and usually commit independently without inventing product or Architecture decisions.

A Skill is not another planning boundary. It is a reusable capability that may be composed only after the delivery boundary is clear enough.

## Capability / Skill Review

For each Build Unit, determine:

1. whether ordinary agent reasoning and repository guidance are sufficient
2. whether reusable specialized procedure materially reduces ambiguity, repetition, risk, or domain error
3. whether a matching Skill already exists
4. the Skill source and how the target agent will load it
5. whether the Skill is required or optional
6. whether its tool requirements fit the Prompt permission ceiling
7. what Skill-specific verification is required
8. whether a missing required Skill is material enough to block Prompt generation

Use this output shape when Skills are relevant:

```text
### Capability / Skill Composition

| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
|---|---|---|---|---|---|---|
```

Rules:

- do not create or select a Skill merely because one exists
- do not place Skills in the strategic traceability hierarchy
- do not let a Skill widen Build Unit scope, product behavior, Architecture, or source-truth ownership
- do not let Skill tool requirements widen Prompt permissions
- do not assume a harness-native Skill exists without a resolvable source
- use progressive disclosure; load only Skill references relevant to the current Build Unit
- a one-off instruction should stay in the Prompt when creating a reusable Skill would add more ceremony than value

## Cross-Initiative / Cross-Domain Impact Scan

Inspect whether target work affects:

- other Initiatives
- shared Delivery Units
- persistent Domains
- shared data, workflows, APIs, events, schemas, or contracts
- Architecture areas
- other repositories
- release and merge order
- existing assumptions

Legacy projects may retain `Cross-Layer Impact` as a compatibility term while migration is pending.

## Dependency & Contract Recon

When relevant:

1. detect `leap.dependencies.yaml` or equivalent
2. identify dependency candidates from code, config, contracts, IaC, tests, and docs
3. inspect declared contract sources when accessible
4. compare provider evidence with expected versions and consumer usage
5. flag confirmed breaking, potential breaking, additive, and insufficient-evidence cases
6. classify as Current-work impact, General system impact, or Unknown / needs verification
7. include severity, confidence, evidence, and next action
8. keep provider access read-only and permission-aware
9. keep notification automation and cross-repo mutation out of scope unless approved

## Risk review

Include:

```text
- Product risk: low / medium / high
- Source-truth risk: low / medium / high
- Architecture risk: low / medium / high
- Dependency contract risk: low / medium / high / not applicable
- Data/security/privacy risk: low / medium / high
- AI behavior risk: low / medium / high / not applicable
- Collaboration risk: low / medium / high
- Verification risk: low / medium / high
```

Sensitive-area rule:

```text
If the change can affect money, identity, privacy, data durability,
legal exposure, or user trust, stop and ask.
```

## Recommended Agent Execution Configuration

When the gate is `Generate LEAP Prompt`, include:

| Field | Recommendation | Rationale |
|---|---|---|
| Agent / Tool | Codex / Claude Code / Cursor / other | Why |
| Codex Plan Mode | On / Off / User decision required | Why |
| Model | Exact model or approved project default | Why |
| Reasoning Level | Low / Medium / High / Extended | Why |
| Execution Mode | implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only | Why |
| Scope Scale | small task / Build Unit / Delivery Unit / Initiative / multi-repo Initiative / repo-wide maintenance | Why |
| Repository | Repo or repositories | Why |
| Branch / Worktree | Target context | Why |
| Permissions | Allowed changes | Why |
| Skill Sources / Loading Method | Named source + native / repo-local / prompt-embedded / none | Why |
| Validation | Tests and checks | Why |
| Commit Guidance | Commit posture | Why |

## Gate decisions

Use one:

```text
Generate LEAP Prompt
Continue LEAP Charter
Pressure Test Further
Narrow Scope First
Needs Human Decision
Reconcile Docs First
Resolve Branch Drift First
Do Not Build Yet
```

A missing Skill does not automatically block Prompt generation. Block only when the specialized capability is material to safe execution and there is no acceptable source or bounded fallback.

## Required output

```text
# LEAP Recon - <Target>

## 1. Framework Interpretation
## 2. Source-of-Truth Manifest Check
## 3. Baseline Freshness Check
## 4. LEAP Charter / Baseline Gate Check
## 5. Ideation Loop Residual Questions
## 6. Materiality Check
## 7. Repo Reality Reconciliation
## 8. Branch / Worktree / PR Drift Review
## 9. Documentation Lifecycle Review
## 10. Strategic Plan Reconciliation
## 11. Existing Functionality Collision Check
## 12. Stale Assumption Scan
## 13. Cross-Initiative / Cross-Domain Impact Scan
## 14. Planning Boundary Review
## 15. Legacy Layer Classification, when relevant
## 16. Generated / Refined Delivery Unit Inventory, when relevant
## 17. Generated / Refined Build Unit Inventory
### Capability / Skill Composition, when relevant
## 18. Recommended Build Sequence
## 19. Dependency and Destructive-Change Review
### Dependency & Contract Recon, when relevant
## 20. Risk Taxonomy Review
## 21. Architecture Right-Sizing Review
## 22. Human Checkpoints Required
## 23. Execution Log / Drift Ledger Expectations
## 24. Coding-Agent Risk Forecast
## 25. Recommended Agent Execution Configuration
## 26. Clarification Questions Before Prompt Generation
## 27. Gate Decision / Next Step
```

## Baseline output format

```text
- Baseline status: Fresh enough / Minor drift / Material drift / Unsafe source-truth conflict
- Evidence checked:
  - ...
- Source-truth confidence: High / Medium / Low / Unknown
- Reconciliation needed before proceeding: No / Recommended / Required
- Notes:
  - ...
```

## Materiality output format

```text
### Material Unknowns
### Assumptions Proceeding Under
### Deferred Non-Material Details
### Question Decision
```

Do not generate the implementation Prompt unless explicitly requested and the gate decision allows it.
