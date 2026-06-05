# LEAP Glossary

## LEAP

**Layered Execution & Alignment Protocol**.

A software delivery framework for turning rough software intent into pressure-tested direction, sequenced plans, governed implementation prompts, and maintainable application documentation.

## Lifecycle

The current LEAP lifecycle is:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

## LEAP Charter

The initial solution-alignment process used to establish or reconcile a project before implementation begins or continues.

LEAP Charter establishes or reconciles the project direction, source-of-truth documents, roadmap, baseline assumptions, and implementation posture before deeper Recon or implementation prompt generation.

LEAP Charter replaces the active use of the older "Phase 0" label. Compatibility stubs may still mention the older term, but active framework docs should use Charter terminology.

## LEAP Charter - Greenfield Mode

Used for brand-new projects, early-stage ideas, or solutions that do not yet have a stable repo, roadmap, architecture, or documentation structure.

Greenfield Mode should help create or organize product mission, target users, MVP boundary, strategic goals, architecture direction, data model assumptions, roadmap, layer plan, prompt backlog, AGENTS.md guidance when applicable, and the first recommended LEAP Recon or prompt sequence. It should recommend LHS only when staged repo/docs foundation work is actually needed.

Also called Greenfield Charter.

## LEAP Charter - Brownfield Mode

Used for existing or mid-buildout projects where LEAP needs to inspect the repo, reconcile documentation, identify gaps, establish source-of-truth docs, and prepare future LEAP Recon, LEAP Prompt, or LHS work.

Brownfield Mode may update documentation, organization, naming, and planning artifacts directly. Runtime implementation changes should normally become follow-up LEAP Prompts or LEAP LHS prompts unless explicitly requested.

Also called Brownfield Charter.

## Documentation Reconciliation Policy

The Brownfield Charter policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

This means useful current content is absorbed into canonical docs, legacy originals are archived, archive/deprecation headers are added where appropriate, and a migration map preserves traceability.

## Legacy Document Classification

| Classification | Meaning | Recommended Action |
| --- | --- | --- |
| Canonical | Current source of truth | Keep or move into canonical docs structure |
| Supporting | Useful secondary detail | Keep near relevant canonical docs or reference from them |
| Current but poorly organized | Useful but structurally messy | Absorb into canonical docs, archive original |
| Partially useful | Mix of current and stale information | Extract useful content, archive original |
| Stale | No longer reflects current direction | Archive with deprecation note |
| Conflicting | Contradicts current strategy, code, or roadmap | Record conflict, resolve in canonical docs, archive original |
| Duplicate | Repeats content covered elsewhere | Consolidate, archive duplicate |
| Completed implementation plan | Old TODO or phase plan already implemented | Archive or convert remaining items to backlog |
| Misleading | Likely to confuse future work | Archive with explicit warning header |

## LEAP Recon

The analysis, source-of-truth reconciliation, repo reality reconciliation, pressure-test, Build Unit generation/refinement, sequencing, cross-layer impact review, stale-assumption scan, execution-configuration recommendation, and clarification stage.

LEAP Recon investigates a focused area, gap, risk, feature, dependency, contract, or architectural question.

## LEAP Dependency & Contract Recon

A subprocess inside LEAP Recon that checks whether the current repo declares or appears to depend on external APIs, services, provider repositories, packages, artifacts, or shared contracts.

It looks for `leap.dependencies.yaml` or an equivalent dependency register, follows declared contract links such as OpenAPI, AsyncAPI, protobuf, GraphQL, provider repo URLs, documentation URLs, packages, and artifacts when accessible, and reports whether provider evidence may affect current work or general system functionality.

Dependency & Contract Recon is read-only by default for provider sources and must report incomplete evidence instead of guessing.

## Dependency Register

A machine-readable repo-level file, recommended as `leap.dependencies.yaml`, that records consumer-owned dependency metadata for LEAP Recon.

It may include dependency name, type, direction, role, provider metadata, contract source, accepted versions, last verified version, baseline hash, compatibility policy, usage evidence, operations used, Recon confidence, and manual notification policy.

If no register exists, LEAP Recon may recommend one and provide candidate entries, but generated entries are not confirmed facts until ratified.

## Dependency Contract Finding

A LEAP Recon finding that compares provider contract evidence against consumer expectations.

Every finding should include dependency name, dependency type, contract source when available, expected version or accepted version range when declared, observed provider version when available, relevant operation or schema when known, finding, impact category, severity, confidence, evidence, and recommended next action.

## Current-Work Impact

A dependency or contract finding that appears relevant to the feature, bug fix, refactor, or implementation currently being requested.

Examples include a changed endpoint used by the current work, a removed response field the current work depends on, a required provider version outside the accepted range, or a changed operation declared as used by the current repo.

## General System Impact

A dependency or contract finding that may affect the repo or portfolio but is not directly tied to the current implementation request.

Examples include provider major-version drift, deprecated operations with unclear local usage, contract changes without declared code paths, or changes to endpoints outside the current work.

## Unknown / Needs Verification

A dependency or contract finding category used when LEAP cannot access enough evidence.

Examples include inaccessible contract URLs, inaccessible provider repos, missing expected version metadata, missing baseline contracts, or local usage that cannot be tied to provider operations.

## LEAP Prompt

The broad category of Codex-ready or agent-ready instruction artifacts generated from Charter, Recon, user intent, or approved implementation scope.

LEAP Prompt produces Codex-ready instructions for analysis, documentation, implementation, or remediation.

A LEAP Prompt must be a bounded task packet with objective, scope, constraints, verification, stop conditions, and explicit Agent Execution Configuration.

LEAP Prompt types include Charter Prompt, Recon Prompt, Standard Implementation Prompt, Fix Prompt, Refactor Prompt, Governance Prompt, Validation Prompt, and LHS Prompt.

## Implementation

The execution of the approved LEAP Prompt by Codex or another coding agent.

Implementation should stay within scope, follow repo patterns, preserve non-goals, and stop when stop conditions are met.

## Validation/Handoff

The required completion step where Codex verifies changes, checks docs/tests, summarizes work, and recommends follow-up prompts.

Validation/Handoff should report files changed, tests/checks run, tests/checks not run, docs updated or needing update, deviations, risks, and follow-up LEAP Recon, LEAP Prompt, or LEAP LHS recommendations.

## LEAP LHS

The Layered House Standard prompt format used for staged implementation work.

Use LEAP LHS when work is layered, staged, or large enough to require House Standard-style execution. Not every LEAP Prompt is an LHS prompt, and LEAP LHS is not a mandatory lifecycle stage.

## LEAP Agent Pack

The versioned release unit for distributable LEAP AGENTS.md templates.

The Agent Pack lives in `https://github.com/mjcataldi/leap_agent_pack`. It includes template metadata, managed section conventions, update policy, and manifests. It lets downstream projects detect stale LEAP guidance without overwriting project-specific instructions.

## Agent Pack Manifest

The JSON source of truth for an Agent Pack release.

The manifest records the Agent Pack version, release tag, source repo, upstream repo, template list, template paths, checksums, update policy, and migration notes.

## AGENTS.md Managed Section

The LEAP-owned portion of an AGENTS.md file.

Managed sections may be updated only after user approval. Project sections should be preserved by default, and local override sections should never be overwritten by LEAP updates.

## AGENTS.md Update Status

The status assigned by LEAP Recon when comparing a downstream AGENTS.md file to the selected Agent Pack manifest.

Supported statuses include Current, Outdated, Outdated with local changes, Pinned, Unversioned LEAP-style file, Non-LEAP AGENTS.md, Missing AGENTS.md, Forked/custom source, and Unknown or malformed metadata.

## Prompt Family

The set of LEAP Prompt types used for different kinds of agent-ready work.

Prompt family members include:

- Charter Prompt
- Recon Prompt
- Standard Implementation Prompt
- Fix Prompt
- Refactor Prompt
- Governance Prompt
- Validation Prompt
- LHS Prompt

## Implementation Gravity

The amount of coordination, risk, dependency ordering, testing, documentation, and rollback concern attached to a task. Higher implementation gravity increases the likelihood that the task should use LHS.

## Solution

The system, product, platform, internal tool, data system, AI application, or infrastructure initiative being built.

## Ideation Loop

The repeated LEAP clarification cycle that turns vague human intent into buildable mechanisms.

```text
Intent -> Questions -> Evidence labels -> Assumption ledger -> Pressure test -> Revised intent -> Gate decision
```

The Ideation Loop continues while hard blockers remain.

## Question-Loop Rule

The rule that LEAP should ask the fewest questions needed to make the next safe gate decision.

If hard blockers remain, LEAP should ask another small question round instead of generating implementation plans or coding-agent prompts.

```text
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```

## Evidence Label

A label that separates implementation truth from uncertainty.

Supported labels:

- Known
- Assumed
- Unknown
- Contested
- Needs Decision
- Deprecated

A polished assumption is still an assumption.

## Readiness Gate

A user-facing operational gate that replaced fake-precision clarity scoring.

Supported gates:

- C0: Blocked
- C1: Discovery Ready
- C2: Concept Ready
- C3: Pressure-Test Ready
- C4: Planning Ready
- C5: Coding-Prompt Ready

C5 requires source truth, repo reality, scope, tests, stop conditions, explicit agent/tool, explicit model, and explicit reasoning level.

## Gate Decision

The explicit decision at the end of Charter or Recon.

Supported gate decisions include:

- Continue Discovery
- Draft Concept Brief
- Proceed to Recon
- Pressure Test Further
- Narrow MVP First
- Needs Human Decision
- Reconcile Docs First
- Resolve Branch Drift First
- Generate LEAP Prompt
- Do Not Build Yet

## No-Build Gate

A LEAP rule that blocks implementation planning and coding-agent prompts until minimum clarity and documentation requirements are met.

At minimum, LEAP should not proceed to layer planning without:

- Charter output, project charter, or equivalent baseline strategy
- MVP boundary or explicit scope boundary
- pressure-test summary when the idea is new or strategically material
- source-of-truth manifest or explicit source-of-truth list
- open questions list
- explicit human approval

## Approval Gate

The explicit human checkpoint between Charter and layer planning.

The user must approve the baseline product direction, MVP boundary, non-goals, risks, assumptions, documentation scaffold, and permission to begin layer planning.

## Human Checkpoint

A point where LEAP must stop and ask for human approval before continuing.

Human approval is required when the agent would otherwise need to guess about product direction, MVP expansion, source-of-truth changes, architecture, auth, permissions, sensitive data, monetization, destructive migrations, external integrations, AI behavior, overlapping parallel-agent scopes, or execution configuration.

## Sensitive Area

A part of the system where mistakes can affect money, identity, privacy, data durability, legal exposure, or user trust.

Rule:

```text
If the change can affect money, identity, privacy, data durability, legal exposure, or user trust, stop and ask.
```

## Documentation Baseline

The current documentation scaffold and source-truth entry point for a LEAP-managed repository.

Recommended docs should include a `00_start_here.md` entry point, canonical product/architecture/layer/prompt docs, a gap register when needed, and a clearly labeled archive for historical docs.

## Project Charter

A project-specific strategy document that defines what the product is, who it serves, what problem it solves, and what the first version should prove.

Project Charter is an artifact a LEAP Charter may produce or reconcile. It is not the same thing as the LEAP Charter process.

## MVP Boundary

The document or section that defines the smallest useful version of the product.

It should include:

- first useful user outcome
- primary user
- primary workflow
- primary success signal
- must-have features
- manual-for-now workflows
- explicit non-goals
- later roadmap candidates
- validation criteria
- overbuild risks

## Source-of-Truth Manifest

The active manifest that identifies canonical and active docs, stale/archived/do-not-use docs, target branch, base branch, relevant PRs, repo reality, known conflicts, and human owner/approver.

Minimum viable source truth:

```text
1. Strategic plan, LEAP Charter output, project charter, or equivalent baseline strategy
2. Source-of-truth manifest or explicit source list
3. Current layer/task description
4. Repo reality summary when repo exists
5. Explicit stale/archive/do-not-use docs list
6. LEAP framework version being used
```

## Source-of-Truth Status

The classification for a planning document.

Recommended statuses include:

- Canonical
- Supporting
- Current but poorly organized
- Partially useful
- Stale
- Conflicting
- Duplicate
- Completed implementation plan
- Misleading
- Archived
- Unknown

No two canonical docs should own the same truth.

Generated docs are Draft until ratified.

## Layer

A major capability phase or architectural slice of the solution.

Examples:

- Layer 0 - Product foundation
- Layer 1 - Core platform
- Layer 2 - Intake & Parsing
- Layer 3 - Evaluation & Artifacts
- Layer 4 - Application Workflow

Project-specific layer names may vary.

## Build Unit

A scoped subsection of a layer that can be implemented, tested, and committed independently.

A Build Unit should be specific enough for implementation, large enough to represent a coherent domain capability, small enough to be one commit in most cases, sequenced against earlier Build Units, explicit about exclusions and boundaries, aligned to source-of-truth documents, and checked against repo reality when repo access is available.

## Quick LEAP Brief

The smallest useful public LEAP Prompt format.

Use it for small, bounded work where full LEAP Charter and Recon would be heavier than the task.

Escalate from Quick LEAP Brief to Charter or Recon when product discovery, architecture decisions, source-truth reconciliation, brownfield documentation reconciliation, sensitive data, or branch drift are involved.

## Source-of-Truth Document

An application-specific roadmap, layer status, domain model, architecture, project-charter, MVP-boundary, execution-state, or implementation-status document that governs repo-specific planning.

LEAP uses source-of-truth documents to avoid relying on stale chat history and to prevent rebuilding capabilities that already exist.

## Repo Reality Reconciliation

A LEAP Recon section that compares source-of-truth claims against the actual repository state when repo access is available.

If repo reality conflicts with source-of-truth documents, repo reality should guide implementation planning, and the documentation conflict should be reported.

## Branch / Worktree Drift Review

A LEAP Recon section that identifies whether the base branch, target branch, active branches, worktrees, or recent changes may conflict with the planned implementation.

## Stale Assumption Scan

A LEAP Recon section that identifies old docs, stale roadmap claims, unverified assumptions, conflicting claims, and assumptions that must be revalidated before implementation.

## Strategic Plan Reconciliation

A LEAP Recon section that checks whether strategic or layer-planning documents remain aligned with current implementation reality.

## Cross-Layer Impact Scan

A LEAP Recon section that identifies whether work in the target layer affects shared entities, workflows, APIs, data models, architecture, future layers, or previous assumptions.

## Agent Execution Configuration

The explicit runtime handoff block required in every agent-ready LEAP Prompt.

It must include:

- Agent / Tool
- Codex Plan Mode, for Codex-targeted prompts
- Model
- Reasoning Level
- Execution Mode
- Scope Scale
- Repository
- Branch / Worktree
- Permissions
- Validation
- Commit Guidance

A prompt is not agent-ready unless it tells the user exactly which execution profile to use.

Codex Plan Mode is the user-controlled Codex UI setting that determines whether Codex should stop for plan approval before editing. LEAP Execution Mode is the prompt instruction that tells the agent how to proceed.

Current LEAP Execution Mode values are:

- `implement-directly`
- `repo-preflight-then-implement`
- `plan-first`
- `recon-only`
- `validation-only`

## Stop Condition

A rule inside a LEAP Prompt that tells the coding agent to stop and report instead of guessing.

Stop conditions are required when docs conflict with code, architecture is unclear, sensitive data handling is unclear, implementation requires unapproved dependencies/migrations/auth/billing/AI behavior changes, model or reasoning level is unavailable without an approved fallback, destructive changes are not authorized, or the task would violate non-goals.

## Source-of-Truth Update Policy

A LEAP Prompt section that tells the coding agent whether and when to update application-specific roadmap/status documents after implementation changes reality.

Generic LEAP methodology should not be updated from an application implementation prompt unless the prompt explicitly targets the LEAP repository.

## Prompt Drift

A LEAP drift type where a prompt assumes stale files, stale branch state, old decisions, missing agent/tool, missing model, or missing reasoning level.

Prompt drift requires a prompt freshness check and regenerated handoff.

## Risk Taxonomy

A lightweight classification of risks that determines how much clarification, Recon, approval, and verification are needed.

Core risk categories:

- Product risk
- Source-truth risk
- Architecture risk
- Data risk
- Security risk
- Privacy risk
- AI behavior risk
- UX risk
- Collaboration risk
- Verification risk

Risk does not automatically block work. Unacknowledged risk blocks work.

## Destructive Change

Anything that can break, delete, rewrite, or invalidate existing state in a way that is not trivially reversible.

Default rule:

```text
Destructive changes are not allowed unless explicitly authorized.
```

## Agent Failure Mode

A predictable way a coding agent may fail.

Common examples:

- hallucinating files, APIs, or business rules
- obeying stale docs over current code
- treating archived docs as current source truth
- broad refactors disguised as cleanup
- silent schema or contract changes
- adding dependencies without approval
- passing tests by weakening them
- overfitting to prompt wording instead of repo reality
- completing the task while violating non-goals
- making product decisions inside implementation
