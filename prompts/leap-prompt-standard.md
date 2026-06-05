# LEAP Prompt — Standard Implementation Prompt

Generate the LEAP Prompt using the current LEAP framework.

The LEAP Recon pass must already be complete, and the user must have approved the required decisions or accepted safe defaults.

A LEAP Prompt is a bounded coding-agent handoff contract. It must not ask the agent to infer product behavior, silently resolve source conflicts, improvise architecture, or guess the execution profile.

Codex Plan Mode is a user-controlled Codex UI setting. It is separate from LEAP Execution Mode, which is an instruction inside the prompt.

Every Codex-targeted LEAP Prompt must make the required Codex Plan Mode setting obvious before the user submits the prompt.

## Prompt family taxonomy

LEAP Prompt is the broad category of Codex-ready or agent-ready instruction artifacts generated from Charter, Recon, user intent, or approved implementation scope.

| Prompt Type | Purpose | Use LHS? |
| --- | --- | --- |
| [Charter Prompt](leap-charter-standard.md) | Establish or reconcile direction, docs, roadmap, baseline | Sometimes |
| [Recon Prompt](leap-recon-standard.md) | Investigate focused risk, repo reality, or implementation uncertainty | Usually no |
| [Standard Implementation Prompt](leap-prompt-standard.md) | Small or medium implementation change | Sometimes no |
| [Fix Prompt](leap-prompt-standard.md) | Specific bug or remediation | Usually no |
| [Refactor Prompt](leap-prompt-standard.md) | Larger structural change | Often yes |
| [Governance Prompt](leap-governance-pass-standard.md) | Repo/process/source-of-truth cleanup | Sometimes |
| [Validation Prompt](leap-prompt-standard.md) | Verify tests/docs/acceptance and summarize handoff | Usually no |
| [LHS Prompt](../docs/leap.md) | Staged implementation sequence | Yes |

The generated prompt must state its prompt type:

```text
Standard LEAP Prompt
LHS Prompt
Fix Prompt
Refactor Prompt
Validation Prompt
Other clearly named prompt type
```

Use an LHS Prompt only when implementation gravity warrants staged execution.

LHS decision gate:

```text
Use LHS when two or more are true:
- The task touches more than 3 files.
- The task affects more than one system area.
- The task has dependency order.
- The task needs tests and docs.
- The task should be committed in phases.
- The task has meaningful rollback risk.
- The task changes architecture, data contracts, or user workflows.
- The task is part of a named layer.
- The task may generate follow-up work.
- The task needs explicit acceptance criteria.

Do not use LHS when:
- The work is pure analysis.
- The work is early brainstorming.
- The work is a one-file edit.
- The work is a small copy/doc fix.
- The work is a quick bug fix with obvious scope.
- The work would add ceremony without reducing risk.
```

## Materiality Gate

Before generating a LEAP Prompt, confirm that Recon applied Materiality Gate to open questions and assumptions.

Materiality Gate means:

```text
- Ask only unresolved questions whose answers would materially change architecture, scope, risk, source-of-truth hierarchy, validation, acceptance criteria, compatibility, or implementation path.
- Inspect discoverable repo/docs/contracts/tooling evidence before asking the user.
- Convert non-material unknowns into stated assumptions.
- Proceed on safe assumptions when not blocked.
```

Do not generate an implementation prompt if unresolved material questions remain. Non-material unknowns may be included as assumptions in the prompt.

## Required preflight

Confirm before writing the prompt:

```text
- LEAP Charter complete or not applicable
- Prompt type selected
- LHS decision gate completed
- Materiality Gate applied to open questions and assumptions
- Ideation Loop complete or residual material questions resolved
- Source-of-truth manifest complete
- Recon approved
- Repo reality checked when repo access exists
- Branch/worktree/PR drift reviewed
- Scope and non-goals defined
- Files/areas to inspect defined
- Files/areas not to touch defined
- Acceptance criteria defined
- Verification path defined
- Stop conditions defined
- Destructive-change permission stated
- Agent / Tool selected or recommended
- Codex Plan Mode selected or recommended for Codex-targeted prompts
- Execution Mode selected or recommended
- Model selected or recommended
- Reasoning level selected or recommended
```

If any item is missing, stop and explain what must happen first. If the missing item is non-material, state the assumption and proceed only when doing so does not change the gate decision or implementation path.

## Codex Plan Mode and LEAP Execution Mode

Use these execution mode terms going forward:

| Execution Mode | Meaning | Codex Plan Mode |
| --- | --- | --- |
| `implement-directly` | Make the change directly and summarize afterward. | Off |
| `repo-preflight-then-implement` | Verify repo reality and stop conditions, then implement if clear. | Off |
| `plan-first` | Produce a plan and wait for user approval before editing. | On |
| `recon-only` | Investigate and report only; do not edit. | User decision required |
| `validation-only` | Validate existing work and report findings. | Off unless changes are requested |

Prefer `repo-preflight-then-implement` for bounded LEAP Prompts where the prompt already contains the implementation contract. The phrase `implement-with-brief-plan` is deprecated because it can be confused with Codex Plan Mode.

Use Codex Plan Mode Off when the task is bounded, source truth is clear enough, risk is low or localized, stop conditions are enough to control risk, and another planning step would not materially reduce risk. Recommended execution mode: `repo-preflight-then-implement`.

Use Codex Plan Mode On when the user should approve the implementation plan before files are edited, including architecture changes, auth/session/permission changes, billing/payment logic, privacy/security-sensitive behavior, destructive migrations, data model changes, cross-system changes, multi-area refactors, unclear source truth, branch/PR drift risk, rollback risk, or changes affecting money, identity, legal exposure, user trust, or data durability. Recommended execution mode: `plan-first`.

Use Codex Plan Mode `User decision required` when either approval posture could be reasonable, such as recon-only work, validation-only work where fixes may or may not be requested, ambiguous medium-risk documentation or refactor work, or work where the user wants an approval gate even though LEAP does not strictly require it.

Codex must follow the Execution Mode below.

Do not reinterpret this LEAP Prompt as a request to create a second implementation plan unless the execution mode is `plan-first` or a stop condition is triggered.

For `repo-preflight-then-implement`, perform a brief repo-local preflight. If referenced files exist, repo reality matches the prompt, and no stop condition is triggered, proceed directly with implementation.

## Required prompt sections

```text
# <Solution Name> — LEAP Prompt — <Target Layer or Task>

## 1. Prompt Type and LHS Decision
- Prompt type: <Standard LEAP Prompt / LHS Prompt / Fix Prompt / Refactor Prompt / Validation Prompt / other clearly named type>
- LHS decision: <Use LHS / Do not use LHS>
- Rationale:

## 2. User Action Before Codex Submission

USER ACTION REQUIRED BEFORE SUBMITTING TO CODEX

| Field | Required Setting |
|---|---|
| Codex Plan Mode | <On / Off / User decision required> |
| Reason | <why this setting is recommended> |

Important: Set Codex Plan Mode before submitting this prompt.

Codex Plan Mode is a user-controlled Codex UI setting. It is separate from LEAP Execution Mode.

## 3. Agent Execution Configuration

| Field | Value |
|---|---|
| Agent / Tool | <Codex / Claude Code / Cursor / other> |
| Codex Plan Mode | <On / Off / User decision required> |
| Model | <exact model name or approved project default> |
| Reasoning Level | <low / medium / high / extended / project-approved enum> |
| Execution Mode | <implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only> |
| Scope Scale | <small task / Build Unit / sublayer / entire layer / repo-wide maintenance> |
| Repository | <owner/repo or local repo name> |
| Branch / Worktree | <target branch/worktree> |
| Permissions | <allowed modifications> |
| Validation | <tests/lint/typecheck/build/manual checks> |
| Commit Guidance | <commit message convention or none> |

Codex must follow the Execution Mode above.

Do not reinterpret this LEAP Prompt as a request to create a second implementation plan unless the execution mode is `plan-first` or a stop condition is triggered.

For `repo-preflight-then-implement`, perform a brief repo-local preflight. If referenced files exist, repo reality matches the prompt, and no stop condition is triggered, proceed directly with implementation.

## 4. Objective
- Objective:
- User-visible outcome:
- Definition of done:

## 5. Current Repo Reality
- Target branch:
- Base branch:
- Existing implementation summary:
- Known doc-code conflicts:
- Existing functionality to reuse:

## 6. Source-of-Truth Instructions
Use these sources:
- <canonical / active sources>

Do not use these sources:
- <draft / stale / archived / superseded sources>

Archived docs are historical unless a canonical document explicitly references them.

If any source conflict appears, stop and report.

## 7. Materiality / Assumption Handling
- Material questions resolved:
- Assumptions accepted:
- Non-material unknowns deferred:
- Discoverable sources already inspected:

Do not ask the coding agent to resolve material product, architecture, source-truth, risk, validation, or acceptance-criteria questions during implementation. Stop and report if new material uncertainty appears.

## 8. Scope
- In scope:
- Out of scope:
- Non-goals:
- Files/areas to inspect:
- Files/areas not to touch:

## 9. Constraints
- Existing patterns to follow:
- Dependencies allowed/disallowed:
- Architecture constraints:
- Data/privacy/security constraints:
- API/schema/state constraints:
- AI behavior constraints, if relevant:
- UX/accessibility constraints, if relevant:
- Destructive changes: allowed / not allowed / allowed only in these areas:
- Rollback/data preservation requirements:

## 10. Implementation Sequence
- Suggested sequence:
- Build Unit order:
- One Build Unit per commit where feasible:
- Edge cases:
- Error handling:
- Backward compatibility:

## 11. Verification
- Tests to run:
- Manual checks:
- Expected result:
- Verification evidence to report:

## 12. Stop Conditions
Stop and report instead of guessing if:
- required files or sources are missing
- docs conflict with repo reality
- existing implementation contradicts this prompt
- unresolved material questions appear during implementation
- implementation would require deciding architecture, product behavior, source-truth hierarchy, risk posture, validation strategy, or acceptance criteria
- implementation would violate non-goals
- task requires architecture not approved
- task requires touching forbidden files
- task requires new dependency, migration, auth/permission change, billing change, AI behavior change, or sensitive-data handling not approved
- destructive changes are required but not explicitly authorized
- branch/worktree drift creates unclear ownership
- verification cannot be performed or is undefined
- acceptance criteria are impossible as written
- requested agent/tool is unavailable and no approved fallback is provided
- requested model is unavailable and no approved fallback is provided
- requested reasoning level is unavailable and no approved fallback is provided
- archived docs appear to be treated as current source truth

## 13. Branch / Worktree / Commit Instructions
- Branch/worktree:
- Commit guidance:
- One Build Unit per commit:
- Merge/order notes:

## 14. Source-of-Truth Update Policy
- Docs to update:
- Execution log / drift ledger update required:
- Cross-layer impact map update required:

## 15. Completion Report Format
Return:
- Summary of changes
- Files changed
- Tests/checks run
- Deviations from prompt
- Assumptions made
- Stop conditions encountered
- Docs updated or needing update
- Follow-up required
- Recommended next LEAP Recon / LEAP Prompt / LEAP LHS, if needed
```

## Reasoning-level selection guidance

Use the smallest reasoning level that controls the implementation risk:

```text
Low — tiny localized edits, typo fixes, obvious one-file changes
Medium — small bounded implementation, clear UI fixes, simple tests, isolated refactors
High — Build Units, sublayers, multi-file features, state workflows, cross-component UX, meaningful test updates
Extended — full-layer implementation, architecture-sensitive work, repo-wide refactors, parallel-agent sequencing, stale-doc reconciliation, destructive schema/data-model changes, sensitive AI behavior
```

Do not include broad cleanup instructions unless cleanup is explicitly scoped and testable.
