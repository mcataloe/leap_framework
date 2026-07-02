# LEAP Glossary

## LEAP

**Layered Execution & Alignment Protocol**.

A software-delivery framework for turning rough software intent into pressure-tested direction, source-grounded plans, governed implementation prompts, and maintainable project documentation.

The word `Layered` in the framework name remains unchanged. Generic unqualified project-planning `Layer` is a separate legacy-compatible term defined below.

## Lifecycle

The current LEAP lifecycle is:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

## LEAP Charter

The project-alignment process used to establish or reconcile direction, source truth, documentation, roadmap posture, and implementation readiness before deeper Recon or implementation prompt generation.

LEAP Charter may produce or reconcile a project-specific Project Charter. The process and the project artifact are not the same thing.

## LEAP Charter - Greenfield Mode

Used for new projects, early ideas, or solutions without a stable repository, source-truth baseline, roadmap, architecture, or documentation model.

Greenfield Charter may establish or organize:

- product Mission
- target users and MVP boundary
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain map when useful
- Architecture direction
- Delivery Units when implementation planning warrants them
- prompt backlog
- source-of-truth posture
- first recommended LEAP Recon or Prompt sequence

Small projects may combine these concepts into one or a few documents.

## LEAP Charter - Brownfield Mode

Used for existing or mid-buildout projects where LEAP must inspect repo reality, reconcile documentation, identify gaps, establish source truth, and prepare future Recon, Prompt, or LHS work.

Brownfield Charter may update documentation, organization, naming, and planning artifacts directly. Runtime changes should normally become follow-up LEAP Prompts unless explicitly requested.

Brownfield Charter classifies legacy Layer documents semantically before renaming or moving them.

## Documentation Reconciliation Policy

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Useful current content is absorbed into canonical docs, legacy originals are preserved or archived appropriately, and a migration map retains traceability.

## Legacy Document Classification

| Classification | Meaning | Recommended action |
|---|---|---|
| Canonical | Current source of truth | Keep or move into the canonical structure |
| Supporting | Useful secondary detail | Keep near or link from canonical docs |
| Current but poorly organized | Useful but structurally messy | Absorb into canonical docs; preserve original until safe |
| Partially useful | Mix of current and stale information | Extract useful content; archive or deprecate original |
| Stale | No longer reflects current direction | Archive with a warning |
| Conflicting | Contradicts current strategy, code, or planning | Record conflict; resolve in canonical docs |
| Duplicate | Repeats truth owned elsewhere | Consolidate and archive duplicate |
| Completed implementation plan | Historical TODO or plan already implemented | Archive or convert remaining work to backlog |
| Misleading | Likely to confuse future work | Archive or mark explicitly |
| Archived | Historical only | Do not treat as active source truth |
| Unknown | Not yet classified | Inspect before relying on it |

## LEAP Recon

The investigative pass that reconciles source truth and repo reality, detects drift and collisions, pressure-tests boundaries, reviews dependencies and risks, refines Delivery Units and Build Units, recommends execution configuration, and ends with a gate decision.

Recon may target a Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, question, or legacy Layer.

Every Recon begins with a lightweight Baseline Freshness Check. A new Charter is not required when the existing baseline is fresh enough.

## Baseline Freshness Check

A lightweight Recon preflight that asks whether the repo and source-truth baseline are fresh enough for the focused investigation.

It may inspect:

- repository `AGENTS.md`
- LEAP Baseline State or `leap.baseline.yaml`
- Project Charter and Strategic Outcomes
- Initiative registry and Roadmap
- Delivery Unit and Build Unit plans
- Domain and Architecture docs
- API and data-contract docs
- archive guidance, gap registers, and migration maps
- relevant repo reality and branch drift

Outcomes are:

- Fresh enough
- Minor drift
- Material drift
- Unsafe source-truth conflict

Baseline Freshness Check is not a lifecycle phase or separate user command.

## LEAP Baseline State

A small `AGENTS.md` table or equivalent metadata that helps Recon judge apparent baseline freshness. It is a signal, not a hard gate or running project-status log.

If `leap.baseline.yaml` exists, it is the canonical machine-readable baseline record and `AGENTS.md` should contain only a summary or pointer.

## Baseline Register

An optional machine-readable repository file, recommended as `leap.baseline.yaml`, for baseline metadata produced by Brownfield Charter, LEAP Governance, or an explicitly authorized baseline scan.

Normal Recon may recommend it but must not silently create it.

## LEAP Dependency & Contract Recon

A subprocess inside Recon that checks whether the current repository depends on external APIs, services, provider repositories, packages, artifacts, events, or shared contracts.

It looks for `leap.dependencies.yaml` or an equivalent dependency register, follows declared contract links when accessible, and reports whether provider evidence affects current work or the broader system.

Provider inspection is read-only by default. Insufficient evidence must be reported rather than guessed.

## Dependency Register

A machine-readable repository file, recommended as `leap.dependencies.yaml`, that records consumer-owned dependency metadata.

It may include dependency name, type, direction, provider metadata, contract source, accepted versions, last verified version, baseline hash, compatibility policy, operations used, evidence, confidence, and manual notification policy.

## Dependency Contract Finding

A Recon finding that compares provider evidence with consumer expectations.

Each finding should include:

- dependency name and type
- contract source
- expected and observed versions when known
- relevant operation or schema
- finding and impact category
- severity and confidence
- evidence
- recommended next action

## Current-Work Impact

A dependency or contract finding relevant to the currently requested work.

## General System Impact

A dependency or contract finding that may affect the repository or portfolio but is not directly tied to the current implementation request.

## Unknown / Needs Verification

A dependency or contract category used when accessible evidence is insufficient.

## LEAP Prompt

The broad family of agent-ready instruction artifacts generated from Charter, Recon, approved user intent, or approved implementation scope.

A LEAP Prompt is a bounded handoff contract with objective, traceability, scope, constraints, verification, stop conditions, source-truth instructions, and explicit Agent Execution Configuration.

Prompt types include Charter, Recon, Standard Implementation, Fix, Refactor, Governance, Validation, and LHS Prompts.

## Implementation

Execution of an approved LEAP Prompt by Codex or another coding agent.

Implementation must stay within scope, follow repository patterns, preserve non-goals, and stop when a stop condition is met.

## Validation/Handoff

The required completion step where the implementation agent verifies changes, checks docs and tests, summarizes work, records deviations, and recommends follow-up LEAP work.

## LEAP LHS

The **Layered House Standard** Prompt format used for staged implementation work.

LEAP LHS stages execution. It does not define the project's strategic documentation hierarchy.

Not every LEAP Prompt is an LHS Prompt, and LHS is not a mandatory lifecycle stage.

## LEAP Agent Pack

The separately versioned release unit for distributable LEAP `AGENTS.md` templates.

The Agent Pack lives in `https://github.com/mcataloe/leap_agent_pack`. It contains template metadata, managed-section conventions, update policy, manifests, install guidance, and migration notes.

## Agent Pack Manifest

The JSON source of truth for an Agent Pack release, including version, tag, source repository, template paths, checksums, update policy, and migration notes.

## AGENTS.md Managed Section

The LEAP-owned portion of an `AGENTS.md` file. Managed sections may be updated only under the applicable approval and compatibility rules. Project and local sections must be preserved.

## AGENTS.md Update Status

The status assigned by Recon when comparing a downstream `AGENTS.md` file with the selected Agent Pack manifest.

Statuses may include Current, Outdated, Outdated with local changes, Pinned, Unversioned LEAP-style, Non-LEAP, Missing, Forked/custom, and Unknown or malformed.

## Prompt Family

The set of LEAP Prompt types used for different kinds of agent-ready work.

## Implementation Gravity

The amount of coordination, risk, dependency ordering, testing, documentation, compatibility, and rollback concern attached to a task.

Higher implementation gravity increases the likelihood that LHS is appropriate.

## Solution

The system, product, platform, service, internal tool, data system, AI application, or infrastructure initiative being built or maintained.

## Ideation Loop

The repeated clarification cycle that turns vague intent into buildable mechanisms:

```text
Intent -> Questions -> Evidence labels -> Assumption ledger -> Pressure test -> Revised intent -> Gate decision
```

## Materiality Gate

The rule for deciding whether LEAP should ask a question, inspect discoverable evidence, proceed with a stated assumption, or stop.

Missing context is classified as:

- Material
- Non-material
- Discoverable
- Safe assumption

Ask only unresolved material questions needed for the next safe gate decision.

## Question-Loop Rule

Ask the fewest questions needed to reach the next safe gate decision.

```text
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```

## Evidence Label

A label separating implementation truth from uncertainty.

Supported labels:

- Known
- Assumed
- Unknown
- Contested
- Needs Decision
- Deprecated

A polished assumption is still an assumption.

## Readiness Gate

A user-facing operational gate:

- C0: Blocked
- C1: Discovery Ready
- C2: Concept Ready
- C3: Pressure-Test Ready
- C4: Planning Ready
- C5: Coding-Prompt Ready

C5 requires source truth, repo reality, scope, tests or validation, stop conditions, agent/tool, model, and reasoning level.

## Gate Decision

The explicit decision at the end of Charter or Recon.

Supported decisions include:

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

A rule that blocks implementation planning and agent-ready prompts until the minimum strategy, scope, source-truth, and approval requirements are met.

At minimum, strategically material work should not proceed without:

- Project Charter, Charter output, or equivalent strategy
- MVP or explicit scope boundary
- Strategic Outcome or intended outcome
- source-of-truth manifest or explicit source list
- open-questions list
- explicit human approval

## Approval Gate

The human checkpoint between product alignment and implementation planning.

The user approves direction, scope, non-goals, risks, assumptions, documentation posture, and permission to begin Initiative, Delivery Unit, or Build Unit planning.

## Human Checkpoint

A point where LEAP must stop for human approval rather than guess about product direction, source truth, Architecture, auth, permissions, sensitive data, monetization, destructive changes, external integrations, AI behavior, overlapping scopes, or execution configuration.

## Sensitive Area

A part of the system where mistakes can affect money, identity, privacy, data durability, legal exposure, or user trust.

```text
If the change can affect money, identity, privacy, data durability,
legal exposure, or user trust, stop and ask.
```

## Documentation Baseline

The current documentation scaffold and source-truth entry point for a LEAP-managed repository.

Recommended baselines may include a Project Charter, Strategic Outcomes, Initiative registry, Roadmap, Domain and Architecture docs, Delivery and Build Unit plans, decisions, prompts, gap registers, and a clearly labeled archive.

## Project Charter

A project-specific strategy artifact defining what the product is, who it serves, what problem it solves, its boundaries, and what the current version should prove.

It is not the same thing as the LEAP Charter process.

## MVP Boundary

The document or section defining the smallest useful version of the product, including primary user, workflow, success signal, must-haves, manual-for-now behavior, non-goals, later candidates, validation, and overbuild risks.

## Mission

The durable explanation of why the solution exists and the governing intent that Strategic Outcomes and Initiatives must advance.

## Strategic Outcome

A measurable or observable condition that advances the Mission.

It identifies the desired change, beneficiary, success signal, evidence or measurement, constraints, and optionally a time horizon.

## Initiative

A temporary, outcome-oriented body of coordinated work that advances one or more Strategic Outcomes.

An Initiative may run in parallel with others, span Domains and repositories, contain Delivery Units, and ends when completed, abandoned, merged, or superseded.

## Initiative Registry

The canonical list of current and proposed Initiatives, their identifiers, status, Strategic Outcomes, ownership, dependencies, and source documents.

It owns Initiative identity. A Roadmap references Initiatives but does not permanently own them.

## Roadmap

A planning projection over Initiatives and Delivery Units showing priority, timing, sequence, parallelism, milestones, dependencies, capacity assumptions, release targets, and status.

An Initiative may exist without current Roadmap placement and may appear on different Roadmap views over time.

## Domain

A persistent business, responsibility, ownership, or technical boundary.

Initiatives and Domains have a many-to-many relationship. A Domain is not a temporary Roadmap lane.

## Domain Map

The source describing persistent Domains, their purpose, ownership, contracts, dependencies, data responsibility, and active Initiatives touching them.

## Architecture

The technical structure showing where and how implementation resides, including components, services, contracts, data, deployment topology, and qualified technical Layers.

Architecture is not the default strategic planning hierarchy.

## Delivery Unit

A coherent functional increment that can be released, deployed, enabled, adopted operationally, or demonstrated end to end.

A Delivery Unit belongs to an Initiative and contains one or more Build Units.

The level may be collapsed for small work when one Build Unit directly delivers the entire Initiative outcome.

## Build Unit

A bounded implementation responsibility that can be implemented, tested, reviewed, and usually committed independently.

A Build Unit traces to an Initiative and, when used, a Delivery Unit. It states scope, exclusions, dependencies, validation, stop conditions, and affected Domains or Architecture areas.

A Build Unit is not required to be independently deployable or independently useful to an end user.

## Layer

Generic unqualified project-planning `Layer` is legacy-compatible and deprecated as the preferred LEAP planning level.

A legacy Layer must be classified by meaning before migration:

- Initiative
- Delivery Unit
- Build Unit
- Domain
- Architecture Layer
- Phase
- mixed or unclear collection

Preserve the LEAP name, Layered House Standard, qualified Architecture Layers, and compatibility references.

## Phase

A genuinely chronological stage where later work depends on completion of an earlier stage.

Do not use Phase merely because a capability was numbered in an old plan.

## Source-of-Truth Manifest

The active manifest identifying canonical and active docs, stale and archived docs, branch context, repo reality, known conflicts, owners, and relevant planning records.

Minimum viable source truth:

```text
1. Project Charter, Charter output, or equivalent strategy
2. Strategic Outcome and current Initiative or bounded task
3. Source-of-truth manifest or explicit source list
4. Current Delivery Unit / Build Unit when implementation is planned
5. Repo reality summary when a repository exists
6. Explicit stale / archive / do-not-use list
7. LEAP framework version
```

## Source-of-Truth Status

The classification for a planning document. No two canonical docs should own the same truth. Generated docs are Draft until ratified.

## Source-of-Truth Document

A project-specific canonical or active document governing strategy, Strategic Outcomes, Initiatives, Roadmap, Domains, Architecture, Delivery Units, Build Units, decisions, execution state, or implementation status.

## Repo Reality Reconciliation

A Recon section comparing source-truth claims with actual repository state. Repo reality guides implementation planning when docs conflict, while the documentation conflict is reported.

## Branch / Worktree Drift Review

A Recon section identifying whether branches, worktrees, pull requests, or recent changes create conflicts, ownership ambiguity, or merge-order risk.

## Stale Assumption Scan

A Recon section identifying stale docs, stale Roadmap claims, unverified assumptions, conflicts, and facts that must be revalidated.

## Strategic Plan Reconciliation

A Recon section checking whether the Project Charter, Strategic Outcomes, Initiative registry, Roadmap, Delivery plans, and implementation reality remain aligned.

## Cross-Initiative / Cross-Domain Impact Scan

A Recon section identifying whether target work affects other Initiatives, persistent Domains, shared contracts, data models, Architecture areas, repositories, or assumptions.

Legacy projects may still use the phrase Cross-Layer Impact Scan while migration is pending.

## Planning Boundary Review

A Recon section determining whether the target is Initiative-sized, Delivery-Unit-sized, Build-Unit-sized, Domain-oriented, Architecture-oriented, a Phase, or an ambiguous legacy Layer.

## Agent Execution Configuration

The explicit handoff block required in every agent-ready Prompt.

It includes:

- Agent / Tool
- Codex Plan Mode when Codex-targeted
- Model
- Reasoning Level
- Execution Mode
- Scope Scale
- Repository
- Branch / Worktree
- Permissions
- Validation
- Commit Guidance

## Execution Mode

The instruction describing how the implementation agent should proceed:

- `implement-directly`
- `repo-preflight-then-implement`
- `plan-first`
- `recon-only`
- `validation-only`

## Stop Condition

A rule telling the agent to stop and report instead of guessing.

## Source-of-Truth Update Policy

The Prompt section describing whether and when Initiative, Roadmap, Delivery Unit, Build Unit, Domain, Architecture, and execution-state documents must be updated after implementation changes reality.

## Prompt Drift

A drift type where a Prompt assumes stale files, branch state, decisions, scope, execution configuration, or source truth.

## Risk Taxonomy

A lightweight classification used to determine clarification, Recon, approval, and verification depth.

Core categories include Product, Source-truth, Architecture, Dependency contract, Data, Security, Privacy, AI behavior, UX, Collaboration, and Verification risk.

Risk does not automatically block work. Unacknowledged risk blocks work.

## Destructive Change

Anything that can break, delete, rewrite, or invalidate existing state in a way that is not trivially reversible.

```text
Destructive changes are not allowed unless explicitly authorized.
```

## Agent Failure Mode

A predictable way a coding agent may fail, such as following stale docs, inventing behavior, broadening scope, silently changing contracts, weakening tests, confusing Initiative and Domain, or treating a Build Unit as independently deployable without evidence.

## Quick LEAP Brief

The smallest useful public LEAP Prompt format for bounded, low-risk work.

Escalate to Charter or Recon when work involves strategy, source-truth reconciliation, parallel Initiatives, Architecture decisions, sensitive areas, destructive changes, or branch drift.

## Canonical project-documentation reference

See [`project-documentation-model.md`](project-documentation-model.md).

See [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md) for legacy Layer reconciliation.
