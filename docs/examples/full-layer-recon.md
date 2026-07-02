# Example: Full-Layer Recon Path — Legacy-Compatible Initiative Recon

This file keeps its historical public path for compatibility. The example now shows how LEAP classifies a legacy `Layer` as an Initiative with Delivery Units and Build Units.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level. Qualified Architecture Layers and LEAP LHS remain valid.

---

## Scenario

A project has an existing product strategy and partial implementation. Its old plan names the next target:

```text
Layer 6 — Artifact Lifecycle Completion
```

The target includes artifact generation, versioning, review state, submitted-state workflow, archive/reactivate behavior, retrieval UX, and traceability to source records.

Recon classifies this legacy Layer as:

```text
Initiative INIT-006 — Complete the Artifact Lifecycle
```

because it is temporary coordinated work advancing a defined outcome and containing several releasable increments.

### Strategic Outcome

```text
Users can create, review, submit, retrieve, and retain traceable artifacts
without losing source relationships or lifecycle history.
```

### Affected Domains

```text
Artifact Management
Opportunity / Source Records
Application Workflow
User Experience
Audit and Traceability
```

The Initiative crosses several persistent Domains. Those Domains are not temporary Roadmap lanes.

---

## Parallel Roadmap context

The Initiative may run alongside other work:

```text
                    Q1          Q2          Q3
Artifact Lifecycle  INIT-006 ─────────────
Search Platform          INIT-007 ─────────────
Operations          INIT-008 ─────
Public Experience               INIT-009 ───────
```

The Roadmap shows timing and parallelism. It does not permanently own the Initiative records.

---

## Recon request summary

```text
Run LEAP Recon for INIT-006 — Complete the Artifact Lifecycle.

Legacy source:
- Existing docs call this Layer 6 — Artifact Lifecycle Completion.
- Treat that name as a compatibility reference.
- Classify its actual planning boundary before implementation.

Project baseline:
- Existing product strategy and Strategic Outcomes exist.
- Source-of-truth manifest exists or must be reconciled.
- Repository contains partial artifact behavior.

Target:
- Determine what already exists.
- Identify stale docs or Roadmap claims.
- Confirm the Initiative boundary.
- Define releasable or adoptable Delivery Units.
- Split each Delivery Unit into bounded Build Units.
- Identify cross-Initiative and cross-Domain impacts.
- Recommend execution configuration and human checkpoints.
```

---

## What Recon should inspect

```text
- Mission / Project Charter
- Strategic Outcomes
- Initiative registry
- active Roadmap
- Domain map
- Architecture docs
- source-of-truth manifest
- legacy Layer 6 plan
- existing artifact models and entities
- routes and API surfaces
- generated artifact storage behavior
- artifact UI and navigation
- versioning, review, submitted, archive, and reactivate behavior
- tests and fixtures
- branches or PRs touching artifact work
- execution logs and drift ledgers
```

---

## Example Delivery Unit inventory

### DU-006-1 — Traceable Artifact Foundation

Outcome:

```text
Artifacts have stable ownership, lifecycle identity, source relationships,
and retrieval behavior.
```

Candidate Build Units:

```text
BU-006-1A — Artifact Model Reconciliation
- Reconcile artifact entities, statuses, ownership, and source relationships.
- Stop if destructive schema changes are required but not authorized.

BU-006-1B — Artifact Generation Traceability
- Connect generated artifacts to source material, opportunity, evaluation,
  and other approved context.
- Stop if source-record ownership is unclear.

BU-006-1C — Retrieval Contract Stabilization
- Make artifact retrieval predictable across API and application use.
- Stop if public contract changes require an unapproved compatibility break.
```

### DU-006-2 — Review and Submission Lifecycle

Outcome:

```text
Users can move artifacts through draft, review, submission, archive, and
reactivation states with durable history.
```

Candidate Build Units:

```text
BU-006-2A — Lifecycle State-Machine Reconciliation
- Define or stabilize allowed transitions and ownership.
- Stop if backend versus frontend enforcement is unresolved.

BU-006-2B — Review and Submitted-State Behavior
- Implement approved review and submitted-state rules.
- Stop if submitted-artifact mutability is undecided.

BU-006-2C — Archive and Reactivate Behavior
- Add or stabilize archive/reactivate behavior without losing history.
- Stop if retention or deletion policy is unclear.
```

### DU-006-3 — End-to-End Artifact Experience

Outcome:

```text
Users can complete the artifact lifecycle through a coherent interface
with tests, documentation, and operational evidence.
```

Candidate Build Units:

```text
BU-006-3A — Artifact UX Stabilization
- Align retrieval, lifecycle actions, navigation, and error states.
- Stop if the current navigation model conflicts with the approved workflow.

BU-006-3B — End-to-End Verification
- Add or update backend, frontend, and workflow tests.
- Validate traceability and lifecycle transitions.

BU-006-3C — Source-Truth and Handoff Updates
- Update Initiative, Delivery Unit, Build Unit, Roadmap, Domain,
  Architecture, and execution records as implementation changes reality.
```

Each Delivery Unit represents a meaningful functional increment. Individual Build Units are implementation boundaries and are not assumed to be independently deployable.

---

## Example Recon gate decision

```text
Gate Decision: Generate LEAP Prompt after required human decisions.

Required decisions:
- Are destructive schema changes allowed?
- Should submitted artifacts be immutable or editable through version history?
- Which layer of the implementation enforces state transitions?
- What is the release order for the three Delivery Units?
- Can Build Units be committed independently while Delivery Units release together?

Recommended Agent Execution Configuration:
- Agent / Tool: Codex or project-approved coding agent
- Codex Plan Mode: On for Initiative planning; Off for approved Build Units
- Model: project-approved reasoning-capable implementation model
- Reasoning Level: Extended for Initiative / High for Build Units
- Execution Mode: plan-first for the Initiative; repo-preflight-then-implement for Build Units
- Scope Scale: Initiative, Delivery Unit, or Build Unit as specified
- Validation: backend tests, frontend tests, lint/typecheck/build,
  manual lifecycle checks, and source-truth review
- Commit Guidance: one Build Unit per commit where practical
```

---

## Why full Recon is warranted

The Initiative touches:

```text
- data model
- workflow state
- API contracts
- user experience
- generated artifacts
- source traceability
- tests
- documentation
- several persistent Domains
- other active Initiatives and Roadmap assumptions
```

A coding agent should not infer those decisions during implementation.

Recon turns the legacy Layer into an explicit Initiative, Delivery Units, and bounded Build Units before handoff.
