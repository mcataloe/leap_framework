# LEAP Prompt — Standard Implementation Prompt

Generate the LEAP Prompt using the current LEAP Framework.

The LEAP Recon pass must already be complete, and material decisions must be approved or accepted as explicit defaults.

A LEAP Prompt is a bounded coding-agent handoff contract. It must not ask the agent to infer product behavior, silently resolve source conflicts, improvise Architecture, invent Strategic Outcomes, or guess Initiative ownership.

## Canonical traceability model

Use this preferred hierarchy:

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

Roadmap schedules and prioritizes. Domains organize persistent responsibility. Architecture organizes technical structure.

Delivery Unit may be collapsed for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred scope term. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

## Prompt family taxonomy

| Prompt Type | Purpose | LHS posture |
|---|---|---|
| Charter Prompt | Establish or reconcile direction and baseline | Sometimes |
| Recon Prompt | Investigate focused uncertainty and repo reality | Usually no |
| Standard Implementation Prompt | Bounded Build Unit or small Delivery Unit | Usually no |
| Fix Prompt | Specific bug or remediation | Usually no |
| Refactor Prompt | Structural change | Often yes |
| Governance Prompt | Source-truth, process, or documentation reconciliation | Sometimes |
| Cleanup Prompt | Artifact decommission review and approval gate | Usually no |
| Validation Prompt | Verify acceptance and handoff | Usually no |
| LHS Prompt | Staged multi-Build-Unit execution | Yes |

The generated Prompt must state its type.

## LHS decision gate

Use LHS when two or more are true:

- more than three files
- more than one system or documentation area
- dependency order
- tests and docs
- phased commits
- rollback or compatibility risk
- Architecture, data contracts, or workflows change
- a named Initiative or Delivery Unit contains several Build Units
- cross-repository coordination
- follow-up work is likely
- explicit acceptance criteria and integration checkpoints are needed

Do not use LHS when it adds ceremony without reducing risk.

LEAP LHS stages execution. It does not define the project's strategic documentation hierarchy.

## Materiality Gate

Before generating a Prompt, confirm Recon:

- asked only unresolved material questions
- inspected discoverable repo, docs, contracts, and tooling evidence
- converted non-material unknowns into assumptions
- resolved or accepted Architecture, scope, risk, source-truth, validation, acceptance, and compatibility decisions

Do not generate an implementation Prompt while unresolved material questions remain.

## Required preflight

Confirm:

```text
- Charter complete or not applicable
- Recon complete and approved
- Prompt type selected
- LHS decision completed
- Materiality Gate completed
- source-of-truth manifest complete
- Mission / Project Charter identified
- Strategic Outcome identified for strategically material work
- Initiative identified
- Delivery Unit identified or explicitly collapsed
- Build Unit or bounded task identified
- Roadmap placement recorded when relevant
- affected Domains identified
- affected Architecture areas identified
- repo reality checked
- branch / worktree / PR drift reviewed
- scope and non-goals defined
- files / areas to inspect and avoid defined
- acceptance criteria defined
- verification path defined
- stop conditions defined
- destructive-change permission stated
- agent / tool selected
- Codex Plan Mode selected when Codex-targeted
- execution mode selected
- model and reasoning level selected
```

If a material item is missing, stop. Non-material unknowns may be stated as assumptions.

## Codex Plan Mode and Execution Mode

| Execution Mode | Meaning | Codex Plan Mode |
|---|---|---|
| `implement-directly` | Make a tiny obvious change and report | Off |
| `repo-preflight-then-implement` | Verify repo reality and proceed when clear | Off |
| `plan-first` | Return a plan and wait for approval before editing | On |
| `recon-only` | Investigate and report only | User decision required |
| `validation-only` | Validate existing work | Off unless fixes may be requested |

Prefer `repo-preflight-then-implement` for bounded approved Build Units. Use `plan-first` for Architecture-sensitive, multi-system, destructive, security, privacy, data-model, contract, or repo-wide work.

## Required Prompt sections

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
## 11. Implementation Sequence
## 12. Verification
## 13. Stop Conditions
## 14. Branch / Worktree / Commit Instructions
## 15. Source-of-Truth Update Policy
## 16. Completion Report Format
```

## 1. Prompt Type and LHS Decision

```text
- Prompt type: Standard LEAP Prompt / LHS Prompt / Fix Prompt /
  Refactor Prompt / Governance Prompt / Cleanup Prompt /
  Validation Prompt / other clear type
- LHS decision: Use LHS / Do not use LHS
- Rationale:
```

## 2. User Action Before Agent Submission

For Codex-targeted Prompts:

```text
USER ACTION REQUIRED BEFORE SUBMITTING TO CODEX

| Field | Required Setting |
|---|---|
| Codex Plan Mode | On / Off / User decision required |
| Reason | Why |
```

## 3. Agent Execution Configuration

| Field | Value |
|---|---|
| Agent / Tool | Codex / Claude Code / Cursor / other |
| Codex Plan Mode | On / Off / User decision required |
| Model | Exact model or approved project default |
| Reasoning Level | Low / Medium / High / Extended |
| Execution Mode | implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only |
| Scope Scale | small task / Build Unit / Delivery Unit / Initiative / multi-repository Initiative / repo-wide maintenance |
| Repository | Repository or repositories |
| Branch / Worktree | Target context |
| Permissions | Allowed modifications |
| Validation | Tests and checks |
| Commit Guidance | Commit posture |

## 4. Strategic and Delivery Traceability

```text
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
```

Do not require full hierarchy for a tiny task when it would add no clarity. Strategic materiality determines the minimum traceability required.

## 5. Objective

```text
- Objective:
- User-visible or operational outcome:
- Definition of done:
```

## 6. Current Repo Reality

```text
- Target branch:
- Base branch:
- Existing implementation summary:
- Existing functionality to reuse:
- Known doc-code conflicts:
- Active branches / worktrees / PRs:
```

## 7. Source-of-Truth Instructions

List canonical and active sources.

List Draft, stale, archived, superseded, and do-not-use sources separately.

Archived docs are historical unless a current canonical source explicitly references them.

Stop if source conflict appears.

## 8. Materiality / Assumption Handling

```text
- Material questions resolved:
- Assumptions accepted:
- Non-material unknowns deferred:
- Discoverable sources inspected:
```

Do not ask the implementation agent to resolve material product, Architecture, source-truth, risk, validation, acceptance, Strategic Outcome, or Initiative ownership questions.

## 9. Scope

```text
- In scope:
- Out of scope:
- Non-goals:
- Files / areas to inspect:
- Files / areas not to touch:
```

## 10. Constraints

```text
- Existing patterns to follow:
- Dependencies allowed / disallowed:
- Architecture constraints:
- Domain ownership constraints:
- Data / privacy / security constraints:
- API / schema / state constraints:
- AI behavior constraints, if relevant:
- UX / accessibility constraints, if relevant:
- Compatibility constraints:
- Destructive changes: allowed / not allowed / limited:
- Rollback and data-preservation requirements:
```

## 11. Implementation Sequence

```text
- Suggested sequence:
- Delivery Unit order, when relevant:
- Build Unit order:
- One Build Unit per commit where feasible:
- Cross-repository merge / release order:
- Edge cases:
- Error handling:
- Backward compatibility:
```

A Build Unit should be implementable, testable, reviewable, and usually committable independently. It is not required to be independently deployable.

## 12. Verification

```text
- Tests to run:
- Manual checks:
- Expected result:
- Verification evidence to report:
- Cross-Initiative or cross-Domain regression checks:
```

## 13. Stop Conditions

Stop and report instead of guessing if:

- required sources are missing
- docs conflict with repo reality
- Initiative, Delivery Unit, Build Unit, Domain, or Architecture ownership is materially unclear
- an unresolved product or Architecture decision appears
- implementation violates non-goals
- forbidden files are required
- a new dependency, migration, auth, billing, AI behavior, or sensitive-data change is needed without approval
- destructive changes are required without authorization
- public contracts or paths must break without approval
- branch or worktree drift creates ownership ambiguity
- verification is unavailable or undefined
- acceptance criteria are impossible
- agent, model, or reasoning level is unavailable without an approved fallback
- archived docs are being treated as source truth
- a legacy Layer cannot be classified safely

## 14. Branch / Worktree / Commit Instructions

```text
- Branch / worktree:
- Commit guidance:
- One Build Unit per commit:
- Merge and release order:
- Parallel-agent ownership:
```

## 15. Source-of-Truth Update Policy

State whether implementation must update:

- Initiative registry
- Roadmap
- Delivery Unit status
- Build Unit status
- Domain docs
- Architecture docs
- decisions / ADRs
- execution log or drift ledger
- cross-Initiative / cross-Domain impact map
- dependency register

Do not update generic LEAP methodology unless the Prompt targets the LEAP Framework repository.

## 16. Completion Report Format

Return:

- Summary of changes
- Strategic and delivery traceability confirmed
- Files changed
- Tests and checks run
- Checks not run and why
- Deviations
- Assumptions
- Stop conditions
- Docs updated or still needed
- Initiative, Delivery Unit, and Build Unit status impact
- Follow-up LEAP work

## Legacy Layer compatibility

When a legacy Layer is referenced, classify it as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or mixed / unclear.

Do not globally replace `Layer` and do not rename public paths solely for terminology consistency.

## Reasoning-level guidance

```text
Low      - tiny localized copy or obvious one-file change
Medium   - small bounded implementation with clear tests
High     - Build Units, Delivery Units, multi-file workflows, meaningful tests
Extended - Initiative-scale work, Architecture-sensitive changes,
           repo-wide refactors, parallel-agent sequencing, stale-doc
           reconciliation, destructive changes, or sensitive AI behavior
```

Do not include broad cleanup instructions unless cleanup is explicitly scoped and testable.

When a Refactor Prompt decommissions obsolete artifacts, use an approved decommission set and the validation contract in [`../docs/repository-cleanup.md`](../docs/repository-cleanup.md).
