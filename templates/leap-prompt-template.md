# LEAP Prompt Request Template

Use this template after LEAP Recon is complete and material questions have been resolved or accepted as explicit defaults.

Do not use it for vague ideas, unreconciled source truth, unclear Initiative ownership, or unresolved material Skill-selection questions.

```text
Generate the LEAP Prompt for <Initiative / Delivery Unit / Build Unit / Task>
using the current LEAP Framework.

Use the approved Recon findings and these decisions/defaults:
- <decision/default 1>
- <decision/default 2>

Strategic and delivery traceability:
- Mission / Project Charter:
- Strategic Outcome:
- Initiative:
- Delivery Unit, if used:
- Delivery Unit collapse rationale, if omitted:
- Build Unit / bounded task:
- Roadmap placement, if relevant:
- Affected Domains:
- Affected Architecture Areas:
- Cross-Initiative dependencies:
- Cross-repository dependencies:

Capability / Skill composition, if used:
- Selected Skills:
- Skill sources:
- Loading methods: native / repo-local / prompt-embedded / other
- Required vs optional:
- Tool / permission requirements:
- Skill-specific verification:

Preflight status:
- Charter complete or not applicable:
- Recon approved:
- Prompt type selected:
- LHS decision completed:
- Materiality Gate completed:
- Source-of-truth manifest complete:
- Repo reality checked:
- Branch / worktree / PR drift reviewed:
- Capability / Skill Review completed or not applicable:
- Human approvals granted:
- Agent / tool selected or recommended:
- Codex Plan Mode selected or recommended:
- Model selected or recommended:
- Reasoning level selected or recommended:
- Execution mode selected or recommended:

Source-of-truth instructions:
Use these sources:
- <canonical / active paths>

Do not use these sources:
- <Draft / stale / archived / superseded paths>

Use these Skill / capability sources separately, if any:
- <Skill source + loading method>

Agent execution configuration:
- Prompt Type: Standard LEAP Prompt / LHS Prompt / Fix Prompt / Refactor Prompt / Validation Prompt / other clear type
- LHS Decision: Use LHS / Do not use LHS
- Agent / Tool: Codex / Claude Code / Cursor / other
- Codex Plan Mode: On / Off / User decision required
- Model: exact model or approved default
- Reasoning Level: Low / Medium / High / Extended
- Execution Mode: implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only
- Scope Scale: small task / Build Unit / Delivery Unit / Initiative / multi-repository Initiative / repo-wide maintenance
- Repository or repositories:
- Branch / Worktree:
- Permissions:
- Skill Sources / Loading Method: named source + native / repo-local / prompt-embedded / none
- Validation:
- Commit Guidance:

Implementation target:
- Objective:
- User-visible or operational outcome:
- Definition of done:
- In scope:
- Out of scope:
- Non-goals:
- Files / areas to inspect:
- Files / areas not to touch:
- Destructive changes allowed: yes / no / limited
- Rollback / data-preservation requirements:
- Compatibility requirements:

Required gate:
- Confirm Mission / Project Charter traceability when strategically material.
- Confirm Strategic Outcome and Initiative ownership.
- Confirm Delivery Unit or explicit collapse rationale.
- Confirm Build Unit or bounded task.
- Treat Roadmap as scheduling and dependency view, not Initiative identity.
- Treat Domains as persistent responsibility boundaries.
- Treat Architecture as technical structure.
- Do not define Build Units as necessarily independently deployable.
- Treat Skills as reusable execution capabilities, not planning levels.
- Prefer ordinary reasoning when an explicit Skill adds no material value.
- For required Skills, confirm source, loading method, permission fit, and verification.
- Do not let a Skill widen Build Unit scope or Prompt authority.
- Confirm repo reality, branch drift, scope, non-goals, validation, stop conditions, and execution profile.
- Confirm whether implementation gravity warrants LHS.
- Stop when a material item is missing.

Create only the final agent-ready Prompt.
```

## Expected Prompt sections

```text
# <Solution> — LEAP Prompt — <Initiative / Delivery Unit / Build Unit / Task>

## 1. Prompt Type and LHS Decision
## 2. User Action Before Agent Submission
## 3. Agent Execution Configuration
## 4. Strategic and Delivery Traceability
## 5. Objective
## 6. Current Repo Reality
## 7. Source-of-Truth Instructions
## 8. Materiality / Assumption Handling
## 9. Scope
## 10. Constraints
### Capability / Skill Composition, when relevant
## 11. Implementation Sequence
## 12. Verification
## 13. Stop Conditions
## 14. Branch / Worktree / Commit Instructions
## 15. Source-of-Truth Update Policy
## 16. Completion Report Format
```

## Capability / Skill Composition format

```text
| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
|---|---|---|---|---|---|---|
```

The Build Unit remains the delivery boundary. A Skill supplies reusable capability. Prompt constraints and permissions remain authoritative.

## Strategic and delivery rules

Use the preferred hierarchy:

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Roadmap schedules. Domains organize persistent responsibility. Architecture organizes technical structure.

Delivery Unit may be collapsed for small work. Build Unit is not necessarily independently deployable.

Skills are orthogonal to this hierarchy and must not be inserted into it.

## Legacy Layer compatibility

If a legacy Layer is referenced, classify it as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or mixed / unclear.

Do not globally replace `Layer`. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

## Required stop conditions

Stop and report if:

- required files or sources are missing
- docs conflict with repo reality
- Initiative, Delivery Unit, Build Unit, Domain, or Architecture ownership is materially unclear
- implementation violates non-goals
- unapproved Architecture is required
- forbidden files must be touched
- a new dependency, migration, auth, billing, AI behavior, or sensitive-data change is needed without approval
- destructive changes are required without authorization
- branch or worktree drift creates unclear ownership
- a required Skill source/loading method is unavailable without a bounded safe fallback
- a Skill requires tools or permissions not granted by the Prompt
- a Skill attempts to widen Build Unit scope or source-truth ownership
- verification is unavailable or undefined
- acceptance criteria are impossible
- archived docs are being treated as source truth
- a legacy Layer cannot be classified safely

Use LHS only when staged execution, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination materially reduce risk.
