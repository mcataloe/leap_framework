<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-reference
  authority: canonical
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Native Multi-Agent Delegation Policy

Status: optional execution capability; no change to the canonical LEAP lifecycle.

This policy extends [execution routing](execution-routing.md). LEAP controls **scope, dependencies, approval, and acceptance**; a supported execution runtime controls **agent spawning, messaging, scheduling, and tool invocation**. A vendor's native agent feature is not a new LEAP lifecycle stage or a substitute for governance.

## Decision gate

Default to one agent. Delegate only when an independent bounded task has a clear outcome and source-truth context, the host actually exposes subagent tools, permissions and data policies allow delegation, and expected benefit exceeds coordination cost. Independent read-only Recon investigations and separate test reviews are good candidates. Short tasks, tightly coupled sequential modifications, ambiguous ownership, and overlapping file writes generally are not.

Before delegation:
1. Identify governing Initiative / Delivery Unit / Build Unit (when material), scope, approved Prompt, source-truth documents, acceptance criteria, and stop conditions.
2. Build a dependency and shared-resource map. Parallel work must not bypass prerequisites; assign disjoint write ownership or use separate isolated worktrees with explicit integration ownership.
3. Verify actual runtime support, allowed models and reasoning settings, budget, credentials, provider/data restrictions, and permission ceiling. Documentation or instructions alone cannot enable runtime features.
4. Assign a role and *capability requirement* to each task. Select model and reasoning effort from the currently available runtime catalog. Do not hard-code product versions or assume a requested effort is supported.
5. Give each worker a bounded task contract: inputs, outputs, permitted files/tools, no-touch paths, required verification, escalation conditions, and reporting format.
6. Integrate in dependency order, run relevant checks, and record validation/handoff. Parent review is required; worker self-reported success is not verification.

## Suggested role / effort policy

| Work | Reasoning starting point | Delegation posture |
|---|---|---|
| Architecture Recon, design tradeoffs, security review | High when available | Independent read-only review is useful |
| Dependency analysis and Build Unit planning | High when material | Usually coordinator-owned; use independent review |
| Bounded code implementation and tests | Medium | Parallel only with separated ownership |
| Mechanical documentation or formatting | Low | Delegate only if coordination overhead is justified |
| Final integration, permissions, acceptance | Based on risk; often high | Coordinator retains responsibility |

These are *hints*, not mandatory model assignments. Increase effort when ambiguity, failure, novelty, or security risk warrants it. A more expensive model is not automatically the best execution surface. Measure cost per **accepted, validated outcome**, including parent work, workers, retries, review, and human effort.

## Non-negotiable boundaries

- Subagents inherit no new authority. Follow the same user approvals, security rules, privacy/data-handling constraints, tool limits, and LEAP stop conditions as the parent.
- A Markdown instruction is not a hard security or approval boundary. Enforce consequential gates through tool permissions, external checks, and human review where available.
- No unattended production changes, deployment, merging, permission expansion, procurement, or destructive operations without independent authorization.
- Never claim parallelism, tests, model selection, isolation, or cost savings occurred unless observed.
- If the runtime lacks agents or supported overrides, execute sequentially with the same Definition of Done; report any loss of capability. Do not emulate subagents using unapproved external services.
- Use an explicit integration owner; workers must disclose changed files, tests run, failures, uncertainty, conflicts, and unresolved dependencies.

## Agent-ready execution handoff addition

When parallel execution is material, append this *optional* block to the existing Agent Execution Configuration:

```text
Delegation Mode: sequential | native-subagents-if-eligible | prohibited
Work Unit / Approved Scope:
Independent Tasks and Dependency Edges:
Worker Roles and Ownership / No-Touch Paths:
Available Runtime / Models / Effort Levels: verified | unknown
Reasoning Policy: low / medium / high guidance; runtime mapping
Concurrency / Budget Ceiling:
Permissions / Data Handling / Stop Conditions:
Integration Owner and Merge Order:
Worker Evidence / Validation Required:
Fallback: sequential; no weaker Definition of Done
```

Do not add this block to trivial prompts. It does not change Charter, Recon, Prompt, Implementation, or Validation/Handoff. Agent Pack runtime-specific examples belong in [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack); provider-specific knobs are examples, not framework doctrine.

## Pressure-test cases

1. Independent read-only Recon of frontend and backend: eligible if both have access and independent scopes.
2. Two workers changing the same contract file: **not** parallel without isolation/serialization and integration owner.
3. Worker discovers a missing auth decision: **stop and escalate**, not infer authority.
4. Runtime lacks native agents or model override: **sequential fallback**.
5. Worker reports passing tests without execution evidence: mark **execution unverified** until checked.
6. Higher-reasoning worker costs more but reduces retries: compare validated end-to-end outcomes, not token price alone.
