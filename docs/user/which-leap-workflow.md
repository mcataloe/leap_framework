<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: supporting-adoption-guidance
  authority: supporting
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Which LEAP Workflow Should I Use?

Use the lightest LEAP workflow that controls the actual risk.

Full LEAP is useful when direction, source truth, repo reality, or implementation risk needs discipline. Small, clear work can use a Quick LEAP Brief.

## Quick chooser

| If this is true | Start with |
| --- | --- |
| The task is small, source truth is clear, and the repo impact is localized. | [Quick LEAP Brief](quick-leap-brief.md) |
| The project direction is unclear, or docs are stale or conflicting. | LEAP Charter |
| A focused feature, risk, layer, dependency, contract, or architecture question needs investigation. | LEAP Recon |
| The work is bounded and the agent needs implementation-ready instructions. | LEAP Prompt |
| The work is staged, layered, multi-area, or needs explicit sequencing. | LEAP LHS |

Materiality Gate is not a phase. It is LEAP's question filter: inspect discoverable sources first, ask only when the answer changes the work, proceed on safe assumptions for polish-only unknowns, and stop for safety, source-truth, destructive-change, privacy, money, identity, legal exposure, or user-trust risks.

## Scenarios

### I have a new app idea.

Use LEAP Charter.

Use it when the user, problem, workflow, MVP, non-goals, risks, source truth, or roadmap are not settled.

Why: Charter turns early intent into a project baseline before any agent starts planning implementation.

Starter phrasing:

```text
Run LEAP Charter for this new app idea. Help clarify the user, problem, MVP, non-goals, risks, source-truth docs, and recommended next LEAP Recon or LEAP Prompt.
```

### My repo has old docs and I do not know what is current.

Use Brownfield LEAP Charter.

Use it when current docs, stale docs, archived docs, repo reality, and source truth need reconciliation.

Why: Brownfield Charter canonicalizes current docs forward, archives stale docs backward, and prevents old plans from competing with current source truth.

Starter phrasing:

```text
Run Brownfield LEAP Charter for this existing repo. Inspect current docs and repo reality, classify docs by lifecycle status, identify source truth, and recommend the next Recon or Prompt sequence.
```

### The project direction is clear, but I need to investigate authentication.

Use LEAP Recon.

Use it when the baseline is good enough, but one focused feature, risk, dependency, contract, layer, or architecture question needs investigation.

Why: Recon checks source truth and repo reality before turning uncertainty into implementation scope.

Starter phrasing:

```text
Run LEAP Recon on authentication. Inspect source-truth docs, repo reality, existing auth behavior, contracts, tests, risks, material unknowns, and whether a LEAP Prompt is ready.
```

For a shorter starter format, use the [LEAP Recon Lite template](../../templates/leap-recon-lite-template.md).

### I know the exact bounded implementation task.

Use LEAP Prompt.

Use it when scope, source truth, repo reality, constraints, non-goals, validation, stop conditions, and execution profile are clear enough for a coding agent.

Why: LEAP Prompt converts a bounded task into agent-ready instructions.

Starter phrasing:

```text
Generate a LEAP Prompt for this bounded task. Include objective, source-truth instructions, scope, non-goals, constraints, implementation sequence, verification, stop conditions, branch/worktree guidance, and completion report format.
```

### This is just a small doc or UI fix.

Use Quick LEAP Brief.

Use it when the change is small, localized, low-risk, and easy to verify.

Why: Quick LEAP Brief keeps the important guardrails without making the process heavier than the work.

Starter phrasing:

```text
Use a Quick LEAP Brief for this small task. Keep scope localized, state source truth, list files to inspect and not touch, define verification, and stop if the work expands beyond the brief.
```

### This work touches several areas and needs staged commits.

Use LEAP LHS.

Use it when implementation gravity is high: multi-area changes, dependency order, tests and docs, phased commits, rollback risk, architecture/data/workflow changes, or explicit acceptance criteria.

Why: LHS is a structured LEAP Prompt format for staged implementation. It is not a mandatory lifecycle stage.

Starter phrasing:

```text
Generate a LEAP LHS prompt for this staged implementation. Break the work into Build Units, define sequence, tests, docs, compatibility checks, rollback concerns, stop conditions, and Validation/Handoff expectations.
```
