# LEAP Glossary

One short definition per term. Follow the link for the full rules.

## LEAP

**Layered Execution & Alignment Protocol**. A documentation-first framework for turning rough software intent into source-grounded plans and bounded agent handoffs. The word `Layered` in the name is unrelated to the legacy planning term [Layer](#layer).

## LEAP Core

The always-loaded LEAP rule set, kept under 650 words. Everything else loads on demand. See [LEAP Core](leap-core.md).

## Lifecycle

`LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff`. See [LEAP Framework](leap.md).

## LEAP Charter

The process that establishes or reconciles project direction, source truth, documentation, and Roadmap posture. It may produce a [Project Charter](#project-charter); the process and the artifact are different things. See [LEAP Charter](leap-charter.md).

## LEAP Charter - Greenfield Mode

Charter for new projects or unstable baselines. It creates only enough structure to proceed safely.

## LEAP Charter - Brownfield Mode

Charter for existing projects. It inspects repo reality, reconciles docs, and classifies legacy Layer docs before moving them. Runtime changes normally become follow-up Prompts.

## Documentation Reconciliation Policy

`Canonicalize forward. Archive backward. Preserve traceability. Never let stale docs compete with source-of-truth docs.`

## Legacy Document Classification

Canonical, Supporting, Current but poorly organized, Partially useful, Stale, Conflicting, Duplicate, Completed implementation plan, Misleading, Archived, or Unknown. See the [classification table](leap-charter.md#legacy-document-classification).

## LEAP Cleanup

A Governance workflow that inventories obsolete artifacts and proposes an exact decommission set. `Run LEAP Cleanup` is discovery-only until that set is approved. See [LEAP Repository Cleanup](repository-cleanup.md).

## Cleanup Mode

The retention posture for a cleanup candidate: `archive-only`, `controlled-migration`, or `destructive-cutover`. It is separate from Agent Execution Mode.

## Decommission Set

The exact, reviewable list of artifacts proposed for retention, migration, archival, or deletion, with evidence and approval status. Classification alone does not authorize removal.

## Effective Decommissioning

The state where absence evidence shows the retired artifact no longer has active authority, and replacement evidence shows the canonical replacement works for its consumers.

## LEAP Recon

The focused investigation that reconciles source truth with repo reality, reviews boundaries, dependencies, and risks, and ends with a [Gate Decision](#gate-decision). See [Recon standard](../prompts/leap-recon-standard.md).

## Baseline Freshness Check

A lightweight Recon preflight that rates the baseline as Fresh enough, Minor drift, Material drift, or Unsafe source-truth conflict.

## LEAP Baseline State

A small `AGENTS.md` table or equivalent metadata that signals baseline freshness. If `leap.baseline.yaml` exists, it is canonical.

## Baseline Register

An optional `leap.baseline.yaml` file for baseline metadata. Recon may recommend it but must not silently create it.

## LEAP Dependency & Contract Recon

A Recon subprocess that checks external APIs, packages, events, and shared contracts. Provider inspection is read-only by default. See [Dependency & Contract Recon](dependency-contract-recon.md).

## Dependency Register

A consumer-owned file, recommended as `leap.dependencies.yaml`, that records dependency and contract metadata.

## Dependency Contract Finding

A Recon finding comparing provider evidence with consumer expectations, with severity, confidence, evidence, and next action.

## Current-Work Impact

A dependency finding relevant to the current request.

## General System Impact

A dependency finding that may affect the broader system but not the current request.

## Unknown / Needs Verification

The dependency finding category used when evidence is insufficient.

## LEAP Prompt

A bounded, agent-ready instruction contract: objective, scope, constraints, verification, stop conditions, and Agent Execution Configuration. See [Prompt standard](../prompts/leap-prompt-standard.md).

## Prompt Family

The LEAP Prompt types: Charter, Recon, Standard Implementation, Fix, Refactor, Governance, Cleanup, Validation, and LHS.

## LEAP LHS

The **Layered House Standard** Prompt format for staged implementation. It is optional, not a lifecycle stage. See [LEAP LHS](leap-lhs.md).

## Implementation Gravity

The coordination, risk, ordering, testing, and rollback concern attached to a task. Higher gravity makes LHS more appropriate.

## LEAP Skill

A reusable execution capability that defines **how** a class of work is done. It is not a planning level or lifecycle phase. See [LEAP Skills](leap-skills.md).

## LEAP Skill Contract

The portable contract for a Skill: triggers, inputs, outputs, scope boundary, tools, permission ceiling, procedure, and verification. Skill capability does not grant authority.

## Capability / Skill Review

The Recon step that decides whether ordinary reasoning is enough or a Skill materially helps, and names its source, loading method, and verification.

## Progressive Disclosure

Keep a Skill's core small and load deep references only when needed.

## Implementation

Execution of an approved LEAP Prompt by a coding agent or other eligible surface, within scope and stop conditions.

## Validation/Handoff

The required completion step: verify changes, report checks run and not run, state the verification state, and name follow-up work. See [LEAP Validation](../prompts/leap-validation-standard.md).

## LEAP Agent Pack

The separately versioned release unit for distributable LEAP `AGENTS.md` templates, at `https://github.com/mcataloe/leap_agent_pack`.

## Agent Pack Manifest

The JSON source of truth for an Agent Pack release: version, template paths, checksums, update policy, and migration notes.

## AGENTS.md Managed Section

The LEAP-owned part of an `AGENTS.md` file. Project and local sections must be preserved.

## AGENTS.md Update Status

Recon's comparison of a downstream `AGENTS.md` with the Agent Pack manifest, such as Current, Outdated, Pinned, Non-LEAP, or Missing.

## Solution

The system, product, service, tool, or initiative being built or maintained.

## LEAP Semantic Routing

Selects the LEAP workflow from an explicit command or natural-language intent. It is separate from execution-surface routing. See [Semantic Workflow Routing](semantic-routing.md).

## LEAP Discovery

Optional domain or problem exploration that yields a Domain/Concept Brief. See [Discovery and Pressure Test](user/leap-discovery.md).

## LEAP Pressure Test

Optional challenge of a hypothesis or design through alternatives, falsifiers, and evidence.

## Ideation Loop

The clarification cycle: `Intent -> Questions -> Evidence labels -> Assumption ledger -> Pressure test -> Revised intent -> Gate decision`.

## Materiality Gate

The shared rule `INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE` for handling missing context. See [Materiality Gate](materiality-gate.md).

## No Gate

An explicit modifier that turns safe ASK outcomes into ASSUME + DISCLOSE. It never turns STOP into PROCEED.

## Question-Loop Rule

Ask only unresolved material questions, a few at a time, and re-evaluate after each answer. There is no minimum question count.

## Evidence Label

Known, Assumed, Unknown, Contested, Needs Decision, or Deprecated. A polished assumption is still an assumption.

## Gate Decision

The explicit next step at the end of Charter or Recon, such as Proceed to Recon, Generate LEAP Prompt, Needs Human Decision, Reconcile Docs First, Resolve Branch Drift First, or Do Not Build Yet.

## No-Build Gate

Blocks implementation planning until strategy, scope boundary, intended outcome, source list, open questions, and human approval exist for strategically material work.

## Approval Gate

The human checkpoint that approves direction, scope, non-goals, and risks before implementation planning.

## Human Checkpoint

A point where LEAP stops for human approval instead of guessing.

## Sensitive Area

Anything that can affect money, identity, privacy, data durability, legal exposure, or user trust. Stop and ask.

## Documentation Baseline

The current documentation scaffold and source-truth entry point for a LEAP-managed repository.

## Project Charter

The project-specific strategy artifact: what the product is, who it serves, its boundaries, and what the current version should prove.

## MVP Boundary

The smallest useful version of the product: primary user, workflow, success signal, must-haves, and non-goals.

## Mission

Why the solution exists. See the [project documentation model](project-documentation-model.md) for this and the following planning terms.

## Strategic Outcome

A measurable or observable change that advances the Mission.

## Initiative

A temporary, outcome-oriented body of coordinated work. Initiatives may run in parallel.

## Initiative Registry

The canonical list of Initiatives. It owns Initiative identity; a Roadmap only references them.

## Roadmap

A planning view of timing, priority, dependencies, milestones, and status.

## Domain

A persistent responsibility boundary. Initiatives and Domains are many-to-many.

## Domain Map

The source describing Domains, their ownership, contracts, and data responsibility.

## Architecture

The technical structure showing where implementation lives. Qualified terms such as Persistence Layer remain valid.

## Delivery Unit

A releasable or demonstrable functional increment containing one or more Build Units. It may be collapsed for small work.

## Build Unit

A bounded implementation responsibility that can be implemented, tested, and reviewed on its own. It need not be independently deployable.

## Layer

Generic unqualified project-planning `Layer` is legacy-compatible and deprecated. Classify its meaning before migrating; see [project-documentation migration](maintainer/project-documentation-migration.md).

## Phase

A genuinely chronological stage where later work depends on an earlier one.

## Source-of-Truth Manifest

The list of canonical, active, stale, and archived docs, plus repo reality and known conflicts. The minimum viable source list is in [LEAP Framework](leap.md#7-source-of-truth-protocol).

## Source-of-Truth Status

The classification of a planning document. No two canonical docs should own the same truth.

## Source-of-Truth Document

A project-specific canonical or active document that governs strategy, planning, Architecture, decisions, or implementation status.

## Repo Reality Reconciliation

Comparing source-truth claims with the actual repository. Repo reality guides planning; the doc conflict is reported.

## Branch / Worktree Drift Review

Checking whether branches, worktrees, or pull requests create conflicts or merge-order risk.

## Stale Assumption Scan

Finding stale docs, unverified assumptions, and facts that must be revalidated.

## Strategic Plan Reconciliation

Checking that the Project Charter, Strategic Outcomes, Initiatives, Roadmap, and implementation still agree.

## Cross-Initiative / Cross-Domain Impact Scan

Checking whether target work affects other Initiatives, Domains, shared contracts, or repositories. Legacy projects may call it Cross-Layer Impact Scan.

## Planning Boundary Review

Deciding whether the target is Initiative-, Delivery-Unit-, or Build-Unit-sized, Domain- or Architecture-oriented, a Phase, or an ambiguous legacy Layer.

## Agent Execution Configuration

The handoff block in an agent-ready Prompt: agent or tool, model, reasoning level, execution mode, repository, branch, permissions, validation, expected verification state, and commit guidance. Tool-specific and routing fields are optional. Fields are defined in the [Prompt standard](../prompts/leap-prompt-standard.md#3-agent-execution-configuration); routing in [LEAP Framework](leap.md#13-agent-execution-configuration-and-routing).

## Execution Environment Profile

Project-local configuration describing available execution surfaces, their capabilities, costs, and limits. See [LEAP Execution Routing](execution-routing.md).

## Execution Surface

A product, tool, agent, or environment through which LEAP work is done or verified.

## Capability Class

An optional classification of environment authority: E0 Reasoning, E1 Remote Mutation, E2 Execution Environment, E3 Agentic Environment, E4 Human Gate.

## Verification State

**Execution verified**, **Partially verified**, **Implemented — execution unverified**, or **Failed**. Implementation and verification are separate claims. See [verification states](execution-routing.md#5-implementation-state-versus-verification-state).

## Failed

The verification state when a required check ran and failed, or validation found an unexplained out-of-scope change or hard-stop violation. Do not report the work as complete.

## Execution Mode

How the agent proceeds: `implement-directly`, `repo-preflight-then-implement`, `plan-first`, `recon-only`, or `validation-only`.

## Stop Condition

A rule telling the agent to stop and report instead of guessing.

## Source-of-Truth Update Policy

The Prompt section that says which planning and state docs must be updated after implementation changes reality.

## Prompt Drift

When a Prompt assumes stale files, branch state, decisions, scope, or source truth.

## Risk Taxonomy

A lightweight risk classification that sets clarification, approval, and verification depth. Unacknowledged risk blocks work. See [LEAP Risk Taxonomy](risk-taxonomy.md).

## Destructive Change

Anything that can break, delete, or rewrite existing state in a way that is not trivially reversible. Not allowed unless explicitly authorized.

## Agent Failure Mode

A predictable agent failure, such as following stale docs, inventing behavior, broadening scope, or weakening tests.

## Quick LEAP Brief

The smallest LEAP Prompt format for bounded, low-risk work: goal, scope, non-goals, and checks.
