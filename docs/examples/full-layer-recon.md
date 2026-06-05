# Example: Full-Layer Recon

This example shows how LEAP handles a larger layer where repo reality, source truth, dependencies, and Build Unit sequencing matter.

---

## Scenario

A project has an existing product strategy and partial implementation. The next target is a full artifact lifecycle layer:

```text
Layer 6 — Artifact Lifecycle Completion
```

The layer includes artifact generation, versioning, review state, submitted-state workflow, archive/reactivate behavior, and traceability back to opportunities or source records.

This is too large for a Quick LEAP Brief.

---

## Recon request summary

```text
Run LEAP Recon for Layer 6 — Artifact Lifecycle Completion.

Project baseline:
- Existing product strategy exists.
- Source-of-truth manifest exists or must be created/updated.
- Repo has partial artifact behavior already implemented.

Target:
- Determine what already exists.
- Identify stale docs or roadmap claims.
- Split Layer 6 into Build Units.
- Recommend execution configuration for each Build Unit or the whole layer.
- Identify stop conditions and human checkpoints.
```

---

## What Recon should inspect

```text
- source-of-truth manifest
- current strategic plan
- layer plan for artifact lifecycle
- existing artifact models/entities
- artifact routes/API surfaces
- generated artifact storage behavior
- resume/cover-letter artifact UI
- versioning/review/submitted-state behavior
- tests and fixtures
- existing branches or PRs touching artifacts
- execution logs and drift ledgers
```

---

## Example Build Unit inventory

```text
Layer 6A — Artifact Model Reconciliation
- Reconcile existing artifact entities, statuses, ownership, and source relationships.
- Stop if schema changes are needed but destructive changes are not authorized.

Layer 6B — Artifact Generation Traceability
- Ensure generated artifacts connect to source material, search track, opportunity, and evaluation context.
- Stop if source material model is unclear.

Layer 6C — Versioning, Review, and Submitted-State Workflow
- Add or stabilize draft/reviewed/submitted/archive state transitions.
- Stop if state machine ownership is unclear.

Layer 6D — Artifact Retrieval and UX Stabilization
- Make artifact retrieval and display predictable in the UI.
- Stop if the current navigation model conflicts with the proposed workflow.

Layer 6E — Tests, Docs, and Execution Log
- Add/update tests and source-of-truth docs after repo reality changes.
```

---

## Example Recon gate decision

```text
Gate Decision: Generate LEAP Prompt after human answers the listed questions.

Required human decisions:
- Are destructive schema changes allowed in the current branch?
- Should submitted artifacts be immutable or editable with version history?
- Should artifact status transitions be enforced by backend, frontend, or both?
- Should each Build Unit be committed separately?

Recommended Agent Execution Configuration:
- Agent / Tool: Codex or project-approved coding agent
- Codex Plan Mode: On for whole-layer planning, Off for approved Build Unit prompts
- Model: project-approved reasoning-capable implementation model
- Reasoning Level: Extended for whole layer, High for individual Build Units
- Execution Mode: plan-first for whole layer, repo-preflight-then-implement for Build Units
- Scope Scale: entire layer or Build Unit
- Validation: backend tests, frontend tests, lint/typecheck/build, manual artifact workflow checks
- Commit Guidance: one Build Unit per commit where feasible
```

---

## Why this needs full Recon

This target touches:

```text
- data model
- workflow state
- UI behavior
- generated artifacts
- source traceability
- tests
- documentation
- future application workflow assumptions
```

A coding agent should not infer those decisions during implementation.

Recon turns the layer into bounded Build Units before any agent handoff.
