<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-reference
  authority: canonical
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Agent Execution Roles and Handoffs

Status: optional execution contract; no new LEAP lifecycle stage or required runtime.

## Purpose and relationship to existing LEAP contracts

LEAP defines the approved **work** through Charter, Recon, and an agent-ready Prompt. [Execution routing](execution-routing.md) selects the eligible surface and required validation. [Agent profiles](agent-profiles.md) describe an agent/tool's capabilities and failure modes. This document defines **responsibilities and handoff evidence** when one or more agents execute that approved work.

The LEAP lifecycle, Materiality Gate, Build Unit boundaries, Definition of Done, permission hierarchy, and human approval requirements remain unchanged. A role is a responsibility, not a mandated agent process, model, Skill, new planning level, or persistent service.

Default to a single agent for straightforward work. Use separate roles/sessions only when independence, specialization, or concurrent execution provides a material benefit. A coordinator may fulfill multiple roles for low-risk work; never claim independent review when no independent review occurred.

## Responsibility contract

| Role | Accountable for | Must not |
|---|---|---|
| **Architect / coordinator** | Confirming current source truth, resolving material decisions with the user, identifying approved Build Units and dependencies, assembling bounded assignments, coordinating integration, accepting evidence and handoff | Silently change an approved Architecture decision; treat delegation as permission to mutate outside scope; approve on behalf of a required human |
| **Implementor** | Inspecting assigned repo reality, implementing only the authorized bounded task, recording changed files and commits, executing available required checks, identifying deviations and blockers | Broaden scope, change contracts or security posture without approval, invent evidence, or assume a stale plan remains valid |
| **Reviewer** | Independently assessing the approved scope versus diff and evidence, challenging correctness, checking residual risk, documenting a clear disposition and fix-up scope where needed | Rely exclusively on the implementor's narrative, silently lower acceptance criteria, claim checks were rerun if they were not |
| **Human approver** | Making decisions reserved by project policy or the governing Prompt, including irreversible, destructive, external, sensitive, or production actions | Be replaced by an AI role or inferred from a default configuration |

These responsibilities can be assigned to humans, native subagents, or separate agent sessions only when the available surface, data-handling rules, and authorization allow it. Agent count is not an indicator of quality.

## Assignment and bounded context packet

For a materially consequential delegated task, the coordinator assembles a minimal **context packet** from authoritative sources. A packet is a transport/handoff artifact, not a competing source of truth.

Include, when relevant:

1. **Identity and baseline:** task/Build Unit identifier, owner, repository, branch/worktree, inspected revision or contract version, and freshness trigger.
2. **Authority and intent:** approved Prompt, objective, acceptance criteria, applicable decisions and architectural invariants; explicit source-of-truth pointers.
3. **Boundaries:** inputs to inspect, files or resources the worker may modify, forbidden areas, dependencies and prerequisites, shared-resource ownership, permissions, and human approval gates.
4. **Execution:** output artifacts, required capabilities and Skills (with actual loading methods), validation commands or evidence requirements, reporting destination, and stop/escalation conditions.
5. **Uncertainty:** material assumptions, known limitations, unresolved decisions, and the condition under which the assignment becomes stale.

Prefer paths, excerpts, and versioned references to copying entire histories or duplicating repository policy. Do **not** exclude a relevant security, data, or compatibility invariant just to reduce context size. The receiver must inspect current source evidence before mutation; a packet cannot make stale information authoritative.

Workers may receive only task-relevant information, but the packet must be **sufficient**, not merely short. If it is missing a material prerequisite, stop and return a targeted question or blocker.

## Execution and review boundaries

1. **Preflight:** reconcile current code, branch/PR state, scope, dependencies, approval, and required verification before work. Use the [Materiality Gate](materiality-gate.md) for consequential uncertainty.
2. **Isolation:** assign disjoint mutable ownership or separate worktrees with an explicit integration owner. Do not run conflicting writes concurrently. The runtime's actual isolation must be verified, not assumed from instructions.
3. **Implementation:** perform the approved task and preserve a record of observed actions. Record checks with exact command, environment or surface, outcome, and relevant log reference; state checks not run and why.
4. **Review:** give the reviewer the approved requirements, relevant decisions, source revision, diff/commits, and evidence. Independent review requires independent examination of the artifact. A separate session or agent is desirable for consequential work, but a different model is not required.
5. **Verification:** the reviewer selectively reruns checks when evidence is missing, stale, questionable, changed, or when risk/policy demands independent execution. Repeating every test is not automatically required. Evidence quality, not number of agents or duplicated test runs, determines confidence.
6. **Disposition:** report accepted, fix-up required, or blocked with specific findings and supporting evidence. Approval to merge, deploy, or perform another protected action remains separate from a reviewer disposition.
7. **Integration/handoff:** the coordinator reconciles dependencies and changed baselines, performs required integrated validation, and reports LEAP's actual verification state: Implemented — execution unverified, Partially verified, or Execution verified.

A mandatory independent review that cannot be performed remains **outstanding**; do not silently substitute a self-check or claim completion.

## Minimum durable handoff

An active handoff must enable a fresh authorized agent to determine:

```text
Objective / Build Unit:
Current owner and stage (project-defined; not a LEAP lifecycle replacement):
Approved scope and source-of-truth references:
Repository / branch / worktree / inspected revision:
Applicable decisions, assumptions, and dependency versions:
Changes / commits / artifact paths:
Checks run (command, result, environment, evidence):
Checks not run (reason and impact):
Review disposition and outstanding fix-ups:
Blockers and human approvals still required:
Next safe action and responsible role:
```

Use an existing issue, PR, work tracker, or repository handoff convention when one is authoritative. Keep completion history and reusable lessons separate from live state. Do not create duplicate registries, new status schemas, or automatic wake-up infrastructure solely to satisfy this contract.

## Changes, failures, and stale handoffs

- A changed source revision, API contract, Architecture decision, authorization boundary, or Build Unit scope may invalidate a handoff. Compare the changed evidence to the packet's assumptions before continuation; replan only the affected work.
- When validation fails, return a bounded fix-up with observed failure, expected behavior, suspected scope, exact verification, and ownership. Do not pass a generic "try again" between agents.
- When an implementor is blocked, preserve the work and report the blocker; do not auto-dispatch another agent to bypass approval.
- If a required execution surface, independent reviewer, or tool is unavailable, use an authorized fallback with unchanged acceptance criteria or report the outstanding work. Never claim unavailable capabilities were exercised.
- Agent-generated instructions are not a security boundary. Enforce protected actions with available tool permissions, independent checks, and human authorization.

## Portable acceptance scenarios

An adopter can exercise these scenarios with a real agent surface or a controlled simulation:

| Scenario | Required observation |
|---|---|
| Small localized fix | Single-agent workflow remains allowed, without compulsory role ceremony |
| Material auth or contract decision | Worker stops rather than selecting an unapproved architecture |
| Disjoint parallel Build Units | Assignments have distinct ownership and integration sequencing |
| Conflicting same-file writes | Coordinator serializes or isolates the work; no silent collision |
| Independent reviewer | Reviewer examines diff and evidence and can issue a bounded fix-up |
| Missing test results | Completion is not reported as Execution verified |
| Interrupted session or changed baseline | A fresh agent identifies the next action and detects material staleness |
| Protected mutation | Human approval and execution-surface permissions remain authoritative |

Record what was actually tested. Static document checks cannot establish native delegation, model selection, session isolation, review independence, or stop-gate behavior.

## Ownership and future implementation

The **Framework** owns this portable role and handoff contract. The separately versioned **LEAP Agent Pack** may provide optional role templates, context manifests, and runtime-specific adapters. Existing `AGENTS.md`, the Prompt, and project source-truth hierarchy remain authoritative for permissions and factual decisions. Persistent inboxes, status validators, session hooks, and dashboards are optional operational implementations justified by observed coordination failures, not LEAP prerequisites.
