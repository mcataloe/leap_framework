# LEAP Prompt Request Template

Use this template after LEAP Recon has been completed and the user has answered questions or approved safe defaults.

Do not use this template for vague app ideas or unreconciled brownfield docs. New projects must pass LEAP Charter and Recon before LEAP Prompt generation unless the baseline is explicitly not applicable.

```text
Generate the LEAP Prompt for <Target Layer or Task> using the current LEAP framework.

Use the LEAP Recon findings above.
Use my answers/defaults below:
- <answer/default 1>
- <answer/default 2>

Preflight status:
- LEAP Charter complete or not applicable:
- Prompt type selected:
- LHS decision gate completed:
- Ideation Loop complete or remaining questions resolved:
- Source-of-truth manifest complete:
- Recon approved:
- Repo reality checked:
- Branch/worktree/PR drift reviewed:
- Human approvals granted:
- Agent/tool selected or recommended:
- Codex Plan Mode selected or recommended for Codex-targeted prompts:
- Model selected or recommended:
- Reasoning level selected or recommended:
- Execution mode selected or recommended:

Source-of-truth instructions:
Use these sources:
- <canonical / active source paths>

Do not use these sources:
- <draft / stale / archived / superseded source paths>

Archived docs are historical unless a canonical document explicitly references them.

Agent execution configuration:
- Prompt Type: Standard LEAP Prompt / LHS Prompt / Fix Prompt / Refactor Prompt / Validation Prompt / other clearly named type
- LHS Decision: Use LHS / Do not use LHS
- Agent / Tool: <Codex / Claude Code / Cursor / other>
- Codex Plan Mode: <On / Off / User decision required>
- Model: <exact model name or recommended default>
- Reasoning Level: <low / medium / high / extended>
- Execution Mode: <implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only>
- Scope Scale: <small task / Build Unit / sublayer / entire layer / repo-wide maintenance>
- Repository:
- Branch / Worktree:
- Permissions:
- Validation:
- Commit Guidance:

Implementation target:
- Objective:
- User-visible outcome:
- Definition of done:
- In scope:
- Out of scope:
- Non-goals:
- Files/areas to inspect:
- Files/areas not to touch:
- Destructive changes allowed: yes/no/allowed only in specified areas
- Rollback/data preservation requirements:

Required gate:
- Confirm LEAP Charter / source-of-truth review is complete.
- Confirm repo reality has been checked when repo access exists.
- Confirm scope, non-goals, verification, stop conditions, and execution profile are defined.
- Confirm whether implementation gravity warrants LHS.
- Confirm the final prompt includes an explicit agent/tool, Codex Plan Mode when Codex-targeted, model, reasoning level, and LEAP Execution Mode.
- If baseline direction, MVP boundary, source truth, Recon approval, implementation scope, verification plan, stop conditions, agent/tool, model, or reasoning level are missing, stop and explain what must be completed first.

Create the final implementation prompt as a canvas/textdoc artifact if supported by the working environment.
Do not include extra analysis inside the prompt unless it is operationally necessary for the coding agent.
```

## Expected LEAP Prompt sections

```text
# <Solution Name> — LEAP Prompt — <Target Layer or Task>

## 1. Prompt Type and LHS Decision
## 2. User Action Before Codex Submission
## 3. Agent Execution Configuration
## 4. Objective
## 5. Current Repo Reality
## 6. Source-of-Truth Instructions
## 7. Materiality / Assumption Handling
## 8. Scope
## 9. Constraints
## 10. Implementation Sequence
## 11. Verification
## 12. Stop Conditions
## 13. Branch / Worktree / Commit Instructions
## 14. Source-of-Truth Update Policy
## 15. Completion Report Format
```

## Required Agent Execution Configuration

Every Codex-targeted LEAP Prompt must include this section near the top:

```text
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
```

Codex must follow the Execution Mode above.

Do not reinterpret this LEAP Prompt as a request to create a second implementation plan unless the execution mode is `plan-first` or a stop condition is triggered.

For `repo-preflight-then-implement`, perform a brief repo-local preflight. If referenced files exist, repo reality matches the prompt, and no stop condition is triggered, proceed directly with implementation.

If the agent/tool, model, or reasoning level is unknown, recommend one explicitly instead of leaving the field blank.

Codex Plan Mode is a user-controlled Codex UI setting. LEAP Execution Mode is an instruction inside the prompt. Use Codex Plan Mode Off for `implement-directly` and `repo-preflight-then-implement`, Codex Plan Mode On for `plan-first`, and `User decision required` when the user's desired approval gate is the deciding factor. The deprecated `implement-with-brief-plan` wording should be replaced with `repo-preflight-then-implement`.

Use LHS only when the work needs staged implementation, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination.

## Required stop conditions

Every LEAP Prompt should instruct the coding agent to stop and report instead of guessing when:

- required files or source documents are missing
- docs conflict with repo reality
- existing implementation contradicts the prompt
- implementation would violate explicit non-goals
- scope requires architecture not approved
- task requires touching forbidden files
- implementation requires a new dependency, migration, auth/permission change, billing change, AI behavior change, or sensitive-data handling not approved
- destructive changes are required but not explicitly authorized
- branch/worktree/PR drift creates unclear ownership
- required tests or verification paths are unavailable or unclear
- acceptance criteria are impossible as written
- requested agent/tool is unavailable and no approved fallback is provided
- requested model is unavailable and no approved fallback is provided
- requested reasoning level is unavailable and no approved fallback is provided
- archived docs appear to be treated as current source truth
