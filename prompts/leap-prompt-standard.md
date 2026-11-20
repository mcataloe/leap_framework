# LEAP Prompt — Standard Implementation Prompt

Generate the LEAP Prompt using the current LEAP Framework.

The LEAP Recon pass must already be complete, and material decisions must be approved or accepted as explicit defaults.

A LEAP Prompt is a bounded coding-agent handoff contract. It must not ask the agent to infer product behavior, silently resolve source conflicts, improvise Architecture, invent Strategic Outcomes, guess Initiative ownership, or assume a required Skill exists without identifying its source.

## Canonical traceability model

For traceability, use the [project documentation model](../docs/project-documentation-model.md) when the project already uses it; otherwise link the external work item. Skills are reusable execution capabilities, not planning levels; see [LEAP Skills](../docs/leap-skills.md).

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
| Validation Prompt | Verify acceptance and handoff; use [`leap-validation-standard.md`](leap-validation-standard.md) | Usually no |
| LHS Prompt | Staged multi-Build-Unit execution | Yes |

The generated Prompt must state its type. LHS Prompts use the stage format in [LEAP LHS](../docs/leap-lhs.md).

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

Do not use LHS when it adds ceremony without reducing risk. LHS stages execution; it does not define the planning hierarchy.

## Materiality Gate

Confirm Recon applied the [Materiality Gate](../docs/materiality-gate.md) (`INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE`):

- inspected discoverable evidence before asking
- asked only unresolved material questions needed for the next safe decision (default **Materiality-Gated** mode)
- under explicit **No Gate**, turned only safe ASK outcomes into disclosed assumptions; STOP remains STOP
- surfaced materially consequential assumptions
- preserved hard blockers, authorization, destructive-change safeguards, sensitive-area checkpoints, and required human approvals
- completed Capability / Skill Review or found it unnecessary

Prompt generation may proceed with a materially consequential assumption only when it is safely assumable, explicitly disclosed, and does not violate a hard blocker or approval requirement.

## Required preflight

Confirm:

```text
- Charter complete or not applicable
- Recon complete and approved
- Prompt type selected
- LHS decision completed
- Materiality Gate completed
- source-of-truth manifest complete
- work item and scope boundary identified
- Initiative / Delivery Unit / Build Unit identified, when the project uses them
- repo reality checked
- branch / worktree / PR drift reviewed
- Capability / Skill Review completed or not applicable
- required Skill sources and loading methods identified, when used
- Skill tool requirements fit the Prompt permission ceiling
- scope and non-goals defined
- files / areas to inspect and avoid defined
- acceptance criteria defined
- required validation defined
- verification path defined, including Skill-specific verification when material
- expected verification state at handoff defined
- stop conditions defined
- destructive-change permission stated
- agent / tool, model, reasoning level, and execution mode selected
- optional, when the tool or project uses them: Codex Plan Mode,
  capability class, and preferred / escalation execution surfaces
```

If a missing item maps to a hard blocker, stop. In Materiality-Gated mode, ask unresolved material questions before Prompt generation. In No Gate mode, only safely assumable material unknowns may become explicit disclosed assumptions; STOP conditions still block generation.

## Codex Plan Mode and Execution Mode

| Execution Mode | Meaning | Codex Plan Mode (optional) |
|---|---|---|
| `implement-directly` | Make a tiny obvious change and report | Off |
| `repo-preflight-then-implement` | Verify repo reality and proceed when clear | Off |
| `plan-first` | Return a plan and wait for approval before editing | On |
| `recon-only` | Investigate and report only | User decision required |
| `validation-only` | Validate existing work | Off unless fixes may be requested |

The Codex Plan Mode column is optional; use it only for Codex-targeted Prompts.

Prefer `repo-preflight-then-implement` for bounded approved Build Units when the selected surface has the needed repository and validation capabilities. Use `plan-first` for Architecture-sensitive, multi-system, destructive, security, privacy, data-model, contract, or repo-wide work.

Choose the execution surface from required validation, not from whether code changes. See [execution routing](../docs/execution-routing.md#6-routing-policy).

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

Keep the section numbers. Omit sections and optional fields with nothing material. Do not pad with N/A.

## 1. Prompt Type and LHS Decision

```text
- Prompt type: Standard LEAP Prompt / LHS Prompt / Fix Prompt /
  Refactor Prompt / Governance Prompt / Cleanup Prompt /
  Validation Prompt / other clear type
- LHS decision: Use LHS / Do not use LHS
- Rationale:
```

## 2. User Action Before Agent Submission

Optional — omit when not needed. Use it only when the user must change a tool setting before submitting, such as Codex Plan Mode:

```text
USER ACTION REQUIRED BEFORE SUBMITTING TO CODEX

| Field | Required Setting |
|---|---|
| Codex Plan Mode | On / Off / User decision required |
| Reason | Why |
```

## 3. Agent Execution Configuration

Select Agent / Tool only after required validation and permissions are known. Use the least-cost eligible surface; never weaken the Definition of Done to save cost.

| Field | Value |
|---|---|
| Agent / Tool | Chat / repository-connected chat / Codex / Claude Code / Cursor / Work / other |
| Model | Exact model or approved project default |
| Reasoning Level | Low / Medium / High / Extended |
| Execution Mode | implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only |
| Scope Scale | small task / Build Unit / Delivery Unit / Initiative / multi-repository Initiative / repo-wide maintenance |
| Repository | Repository or repositories |
| Branch / Worktree | Target context |
| Permissions | Allowed modifications |
| Validation | Tests and checks |
| Verification State at Handoff | Expected state from [LEAP Validation](leap-validation-standard.md#verification-state) |
| Skill Sources / Loading Method | Named source + native / repo-local / prompt-embedded / none |
| Commit Guidance | Commit posture |

Optional routing fields — omit when not needed. Add them when the project uses an [Execution Environment Profile](../docs/execution-routing.md) or the surface choice is not obvious:

| Field | Value |
|---|---|
| Codex Plan Mode | On / Off / User decision required |
| Required Capability Class | E0 / E1 / E2 / E3 / E4 or combination |
| Required Capabilities | Concrete environment capabilities needed |
| Required Confidence / Validation | Evidence required to claim completion |
| Preferred Surface | Lowest-cost eligible surface |
| Escalation Surface | Surface used when the preferred surface cannot satisfy capability or validation requirements |

## 4. Strategic and Delivery Traceability

```text
- Work item: <link to issue, ticket, or planning doc>
- Scope boundary:
- Initiative / Delivery Unit / Build Unit, when the project uses them:
- Cross-repository or cross-Domain dependencies, when material:
```

Add Strategic Outcome, Roadmap, Domain, or Architecture fields only when they change the work.

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

List Skill sources separately as execution capability sources. Do not imply that a Skill definition owns unrelated project source truth.

Archived docs are historical unless a current canonical source explicitly references them.

Stop if source conflict appears.

## 8. Materiality / Assumption Handling

```text
- Clarification mode: Materiality-Gated / No Gate
- Material questions resolved:
- Material assumptions accepted under No Gate, if any:
- Assumptions accepted:
- Non-material unknowns deferred:
- Discoverable sources inspected:
- Hard blockers cleared:
```

Do not ask the implementation agent to resolve material product, Architecture, source-truth, risk, validation, acceptance, Strategic Outcome, Initiative ownership, material Skill-selection, authorization, or destructive-change questions. A No Gate assumption must be explicit and must not bypass a stop condition.

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

### Capability / Skill Composition

Include this subsection when one or more Skills are selected:

```text
| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
|---|---|---|---|---|---|---|
```

Build Unit scope and the Prompt permission ceiling stay authoritative. Required Skill sources must be resolvable before execution; if the harness cannot load one, give the smallest safe prompt-embedded fallback or stop. Follow the composition rules in [LEAP Skills](../docs/leap-skills.md#prompt-composition).

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

## 12. Verification

```text
- Tests to run:
- Manual checks:
- Skill-specific verification, when used:
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
- a required Skill source is unavailable without a bounded safe fallback, or a Skill needs tools, permissions, or scope beyond the Prompt
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

State which project records implementation must update, when the project keeps them: Roadmap; Initiative, Delivery Unit, or Build Unit status; Domain or Architecture docs; decisions / ADRs; execution log or drift ledger; impact map; dependency register.

Do not create a project Skill registry merely because Skills were used. Add or modify durable Skill definitions only when the Prompt explicitly scopes that work.

Do not update generic LEAP methodology unless the Prompt targets the LEAP Framework repository.

## 16. Completion Report Format

Return the handoff report defined in [LEAP Validation](leap-validation-standard.md#required-output), including its verification state and scope check. Also include:

- summary of changes
- work item and Build Unit traceability, when used
- Skills used and their sources, when material
- deviations and assumptions
- docs updated or still needed
- Initiative, Delivery Unit, and Build Unit status impact, when used

## Legacy Layer compatibility

When a legacy Layer is referenced, classify it with the [migration guide](../docs/maintainer/project-documentation-migration.md) before acting. Do not globally replace `Layer` or rename public paths.

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
