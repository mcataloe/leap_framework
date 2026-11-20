# LEAP Prompt Request Template

Use this template after LEAP Recon is complete and material questions have been resolved or accepted as explicit defaults.

Do not use it for vague ideas, unreconciled source truth, unclear Initiative ownership, or unresolved material Skill-selection questions.

```text
Generate the LEAP Prompt for <Initiative / Delivery Unit / Build Unit / Task>
using the current LEAP Framework.

Use the approved Recon findings and these decisions/defaults:
- <decision/default 1>
- <decision/default 2>

Traceability:
- Work item: <link to issue, ticket, or planning doc>
- Scope boundary:
- Initiative / Delivery Unit / Build Unit, when the project uses them:
- Cross-repository or cross-Domain dependencies, when material:

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
- Clarification mode: Materiality-Gated / No Gate
- Source-of-truth manifest complete:
- Repo reality checked:
- Branch / worktree / PR drift reviewed:
- Capability / Skill Review completed or not applicable:
- Human approvals granted:
- Agent / tool, model, reasoning level, and execution mode selected or recommended:

Source-of-truth instructions:
Use these sources:
- <canonical / active paths>

Do not use these sources:
- <Draft / stale / archived / superseded paths>

Use these Skill / capability sources separately, if any:
- <Skill source + loading method>

Agent execution configuration:
- Prompt Type: Standard LEAP Prompt / LHS Prompt / Fix Prompt / Refactor Prompt / Governance Prompt / Cleanup Prompt / Validation Prompt / other clear type
- LHS Decision: Use LHS / Do not use LHS
- Agent / Tool: Chat / repository-connected chat / Codex / Claude Code / Cursor / Work / other
- Model: exact model or approved default
- Reasoning Level: Low / Medium / High / Extended
- Execution Mode: implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only
- Scope Scale: small task / Build Unit / Delivery Unit / Initiative / multi-repository Initiative / repo-wide maintenance
- Repository or repositories:
- Branch / Worktree:
- Permissions:
- Validation:
- Verification State at Handoff: expected state from leap-validation-standard.md
- Skill Sources / Loading Method: named source + native / repo-local / prompt-embedded / none
- Commit Guidance:

Optional routing fields (omit when not needed):
- Codex Plan Mode: On / Off / User decision required
- Required Capability Class: E0 / E1 / E2 / E3 / E4 or combination
- Required Capabilities:
- Required Confidence / Validation:
- Preferred Surface:
- Escalation Surface:

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
- Confirm work item, scope boundary, and Build Unit or bounded task.
- Confirm repo reality, branch drift, scope, non-goals, validation, stop conditions, and execution profile.
- Confirm whether implementation gravity warrants LHS.
- For required Skills, confirm source, loading method, permission fit, and verification. A Skill must not widen Build Unit scope or Prompt authority.
- Derive required validation before choosing the execution surface. Cost optimization must not weaken the Definition of Done.
- Distinguish implementation from execution verification.
- Apply the Materiality Gate. No Gate never converts STOP into proceed and never bypasses hard blockers or required approval.

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

Keep the section numbers. Section 2 and the optional routing fields in section 3 are tool-specific; omit them when not needed. Section 16 returns the handoff report from [LEAP Validation](../prompts/leap-validation-standard.md#required-output). Omit sections with nothing material. Do not pad with N/A.

## Capability / Skill Composition format

```text
| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
|---|---|---|---|---|---|---|
```

The Build Unit remains the delivery boundary. Prompt constraints and permissions remain authoritative. See [LEAP Skills](../docs/leap-skills.md#prompt-composition).

## Execution roles, when relevant

Only for multi-agent work, a required independent review, or a cross-session continuation: name the coordinator, implementor write boundaries, reviewer, and human approver in section 3, and use the context packet and handoff from [Agent Execution Roles and Handoffs](../docs/agent-execution-roles.md). Omit for single-agent work. Roles grant no authority beyond this Prompt, and an independent review that cannot be performed stays outstanding.

## Strategic and delivery rules

For traceability, use the [project documentation model](../docs/project-documentation-model.md) when the project already uses it; otherwise link the external work item.

## Legacy Layer compatibility

Classify any legacy Layer with the [migration guide](../docs/maintainer/project-documentation-migration.md) before acting. Do not globally replace `Layer`.

## Required stop conditions

Use the stop conditions in [section 13 of the Prompt standard](../prompts/leap-prompt-standard.md#13-stop-conditions).

Use LHS only when staged execution materially reduces risk. Stage format: [LEAP LHS](../docs/leap-lhs.md).
