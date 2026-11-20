# LEAP Framework

LEAP — **Layered Execution & Alignment Protocol** — is a documentation-first software-delivery framework for turning rough intent into pressure-tested direction, source-grounded plans, and safe, bounded coding-agent handoffs.

The current lifecycle is:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the **Layered House Standard** Prompt format for staged implementation. It is part of the LEAP Prompt family, not a mandatory lifecycle stage.

LEAP Skills are reusable execution capabilities that may be selected and composed inside that lifecycle. They are not a new lifecycle phase or a replacement for Build Units. Canonical Skill guidance lives in [`leap-skills.md`](leap-skills.md).

## Semantic workflow entry points

[LEAP Semantic Workflow Routing](semantic-routing.md) defines explicit command aliases, LEAP help, and safe natural-language selection. It is separate from capability- and cost-aware execution routing. [Discovery and Pressure Test](user/leap-discovery.md) are optional pre-planning or investigative entry points and do not change the lifecycle or authorization model.

## 1. Framework principles

LEAP applies these operating rules:

```text
No source truth, no Recon.
No repo reality, no implementation plan.
No bounded scope, no coding task.
No stop conditions, no safe handoff.
No validation, no completion.
```

LEAP should:

- preserve the user's original intent
- distinguish evidence from assumptions
- ask only material questions
- inspect discoverable sources before asking
- reconcile docs with repo reality
- define strategic and implementation boundaries before coding
- keep agent execution configuration explicit
- route work to the least-cost available execution surface capable of satisfying required confidence and validation
- keep provider pricing, quotas, credits, and product names in environment configuration rather than framework doctrine
- distinguish implementation from execution-grounded verification
- compose reusable Skills only when they materially improve execution
- keep Skill capability separate from execution authority and Build Unit scope
- preserve compatibility unless change is approved
- stop when an agent would otherwise need to guess

## 2. Lifecycle

### LEAP Charter

LEAP Charter establishes or reconciles:

- project Mission and direction
- Project Charter or equivalent strategy
- target users and MVP or current scope boundary
- Strategic Outcomes
- Initiative registry
- Roadmap posture
- Domain and Architecture documentation when useful
- source-of-truth structure
- documentation lifecycle
- prompt backlog and implementation posture

Charter has Greenfield and Brownfield modes.

### LEAP Recon

Recon investigates a focused Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, question, or legacy Layer.

Recon performs:

- Baseline Freshness Check
- source-of-truth manifest review
- repo-reality reconciliation
- branch / worktree / PR drift review
- stale-assumption and collision scans
- cross-Initiative and cross-Domain impact review
- planning-boundary review
- Delivery Unit and Build Unit refinement
- Capability / Skill Review when reusable specialized procedure may materially help
- dependency and destructive-change review
- risk and Architecture right-sizing review
- execution-configuration and execution-routing recommendation
- gate decision

### LEAP Prompt

A LEAP Prompt is a bounded agent-ready contract containing:

- objective and traceability
- current repo reality
- source-of-truth instructions
- scope, non-goals, and forbidden areas
- constraints and compatibility posture
- Capability / Skill composition when used
- implementation sequence
- verification
- stop conditions
- branch and commit guidance
- source-of-truth update policy
- completion report format
- explicit Agent Execution Configuration

### Implementation

The approved Prompt is executed on the least-cost available surface that can satisfy its capability, confidence, validation, and permission requirements. Complete the largest coherent tranche practical before crossing surfaces. When a surface cannot run required checks, report **Implemented — execution unverified** and hand bounded validation to an adequate surface. Required Skills are loaded from their named source; they cannot widen Prompt permissions.

Canonical execution-routing doctrine: [LEAP Execution Routing](execution-routing.md).

### Validation/Handoff

Validation/Handoff confirms what changed, what was checked, and the honest verification state. It reports checks not run and why, deviations, assumptions, and follow-up work. Use the [LEAP Validation standard](../prompts/leap-validation-standard.md) for the checks and output; verification states are defined in [LEAP Execution Routing](execution-routing.md#5-implementation-state-versus-verification-state).

## 3. Canonical project-documentation model

When a project wants traceability, LEAP uses one optional hierarchy: Mission / Project Charter, Strategic Outcome, Initiative, Delivery Unit, and Build Unit. Roadmap, Domain Map, and Architecture are separate supporting views. Small projects may collapse levels, and a link to an external work item (Jira, Azure DevOps, GitHub issue) is an acceptable substitute.

The full definitions, collapse rules, and generic `Layer` compatibility rules live in the [project documentation model](project-documentation-model.md). Migration guidance lives in [project-documentation migration](maintainer/project-documentation-migration.md).

A LEAP Skill is orthogonal to this hierarchy. A Build Unit defines **what** bounded responsibility is delivered; a Skill defines reusable **how**. See [LEAP Skills](leap-skills.md).

## 4. Greenfield and Brownfield Charter

### Greenfield Charter

Use for new projects or unstable baselines.

Greenfield Charter should establish only enough structure to proceed safely. It may combine several concepts in one document for a small project.

Recommended outputs:

- Project Charter
- MVP or current scope boundary
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain map when useful
- Architecture direction
- first Delivery Units when implementation planning warrants them
- source-of-truth manifest
- prompt backlog

Do not generate Build Units before Initiative boundaries and intended outcomes are clear.

### Brownfield Charter

Use for existing repositories, incomplete implementations, stale documentation, or unclear source truth.

Brownfield Charter should:

1. inventory docs and repo reality
2. classify documents
3. identify canonical ownership
4. compare strategy and implementation
5. reconcile legacy Layer docs semantically
6. create a gap register and migration map
7. update source-truth entry points
8. preserve public paths unless a separate migration is approved
9. prepare focused Recon and Prompt work

Policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

### Repository Cleanup governance workflow

Use [LEAP Repository Cleanup](repository-cleanup.md) when obsolete artifacts must be inventoried, classified, and decommissioned rather than merely reconciled conceptually.

Repository Cleanup is a specialized Governance workflow, not a lifecycle phase. An unqualified `Run LEAP Cleanup` command is discovery-only: it produces an exact proposed decommission set and stops for approval. Approved cleanup is executed through a LEAP Refactor Prompt and completed through Validation/Handoff.

Cleanup modes (`archive-only`, `controlled-migration`, `destructive-cutover`) describe retention and compatibility posture; they do not replace Agent Execution Mode. Details are in [LEAP Repository Cleanup](repository-cleanup.md).

## 5. Materiality Gate

Materiality Gate is a shared LEAP execution primitive, not a lifecycle phase:

```text
INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE
```

Inspect discoverable facts first, assume and disclose safe non-material ones, ask only about unresolved material uncertainty, and stop on hard blockers. An explicit **No Gate** modifier turns safe ASK outcomes into ASSUME + DISCLOSE; it never turns STOP into PROCEED.

Canonical details: [Materiality Gate](materiality-gate.md).

## 6. Readiness gates

Each workflow ends with its own gate decision, such as `Proceed to Recon`, `Generate LEAP Prompt`, `Needs Human Decision`, `Reconcile Docs First`, or `Do Not Build Yet`. The decision lists live in the [Charter](../prompts/leap-charter-standard.md) and [Recon](../prompts/leap-recon-standard.md) standards.

Work is ready for an agent-ready Prompt when it has source truth, repo reality, bounded scope, accepted assumptions, a validation path, stop conditions, and resolvable Skill sources when Skills are used.

## 7. Source-of-truth protocol

No Recon or agent-ready implementation Prompt may proceed without an active source-truth baseline or an explicitly scoped minimum source list.

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

Skill definitions are execution instruction sources, not automatically project source truth. Treat a Skill as authoritative only for the capability contract it explicitly owns.

### Conflict hierarchy

Unless a human decides otherwise:

```text
1. Running implementation / repo reality
2. Current target-branch diff
3. Merged code on base branch
4. Database schema and migrations
5. Tests and fixtures
6. Canonical docs
7. Active ADRs and decision records
8. Current Initiative / Delivery Unit / Build Unit plans
9. Recent PR descriptions and execution logs
10. Old plans and archived docs
```

Old plans are not source truth unless explicitly reactivated.

### Baseline Freshness Check

Recon checks whether the baseline is fresh enough by inspecting, when available:

- repository `AGENTS.md`
- `leap.baseline.yaml`
- Project Charter and Strategic Outcomes
- Initiative registry and Roadmap
- Domain and Architecture docs
- Delivery Unit and Build Unit records
- decisions, contracts, gap registers, and migration maps
- relevant repo reality

Outcomes:

- Fresh enough
- Minor drift
- Material drift
- Unsafe source-truth conflict

## 8. Recommended project docs

Important docs should include concise metadata such as Status, Last reconciled, LEAP mode, Source of truth, and Purpose.

Example structure:

```text
docs/
  00_start_here.md
  01_charter/
  02_strategy/
  03_domains/
  04_architecture/
  05_delivery/
  06_build_units/
  07_decisions/
  08_prompts/
  99_archive/
```

This is an example, not a requirement. Small projects may combine concepts, and Brownfield projects may retain existing conventions.

Reusable Skills may live elsewhere according to the target harness or repository. Do not force Skills into the project-documentation hierarchy or create a Skill registry merely because Skills are supported.

## 9. No-build protocol

Every new product idea and materially new capability should pass a no-build review before implementation planning:

```text
What happens if we do nothing?
What manual workflow solves most of this?
What spreadsheet, checklist, template, or lightweight doc solves most of this?
What existing product solves most of this?
What integration, script, no-code automation, or service solves most of this?
What process or behavior change solves most of this?
Why is custom software justified?
Why is AI specifically justified, if proposed?
What would make this not worth building?
```

LEAP must not treat a request for software as proof that software should be built.

## 10. Planning-boundary and Build Unit rules

Recon should classify the target as one or more of:

- Initiative-sized
- Delivery-Unit-sized
- Build-Unit-sized
- Domain-oriented
- Architecture-oriented
- chronological Phase
- ambiguous legacy Layer

A Build Unit is too large when it requires an agent to:

- modify unrelated capabilities
- decide product behavior
- invent Architecture
- touch shared contracts without ownership clarity
- perform vague multi-system validation
- compress more than roughly five to seven meaningful implementation steps without clear sub-boundaries

Split work before this happens.

### Capability / Skill composition

After Build Unit boundaries are clear enough, Recon may identify reusable Skills that materially reduce ambiguity, repetition, risk, or specialized-domain error.

Skills do not become a planning level, do not own Build Unit identity, and may not expand scope or widen Prompt permissions. Required Skills must name a resolvable source and loading method. Do not create a Skill when a one-off instruction is clearer.

Canonical reference: [`leap-skills.md`](leap-skills.md).

## 11. Cross-Initiative and cross-Domain impact

Recon should identify whether target work affects:

- other Initiatives
- shared Delivery Units
- persistent Domains
- shared entities or workflows
- APIs, events, schemas, or data models
- Architecture areas
- other repositories
- release or merge order
- previous assumptions

Legacy projects may continue using `Cross-Layer Impact` as a compatibility term until reconciled.

## 12. Dependency & Contract Recon

Dependency & Contract Recon is a subprocess inside Recon.

It should:

1. detect `leap.dependencies.yaml` or an equivalent register
2. identify dependency candidates from code, config, contracts, tests, IaC, and docs
3. inspect declared OpenAPI, AsyncAPI, protobuf, GraphQL, package, artifact, provider-repo, or documentation sources when accessible
4. compare provider evidence with accepted versions and consumer usage
5. classify findings as Current-work impact, General system impact, or Unknown / needs verification
6. include severity, confidence, evidence, and recommended action
7. remain read-only by default for provider sources

Notification automation, release blocking, ticket creation, and cross-repo mutation are out of scope unless explicitly approved.

## 13. Agent Execution Configuration and Routing

Agent / Tool selection should be derived from required capabilities and validation, not assumed before the work unit is understood.

Every agent-ready Prompt states its Agent Execution Configuration. The required and optional fields are defined once in the [Prompt standard, section 3](../prompts/leap-prompt-standard.md#3-agent-execution-configuration) and carried by the [Prompt template](../templates/leap-prompt-template.md).

Use [LEAP Execution Routing](execution-routing.md) to select the least-cost eligible surface. Cost optimization may influence surface choice but may not lower acceptance criteria or the Definition of Done.

Execution modes:

| Mode | Meaning |
|---|---|
| `implement-directly` | Make a tiny obvious change |
| `repo-preflight-then-implement` | Verify repo reality and proceed when clear |
| `plan-first` | Return a plan for approval before editing |
| `recon-only` | Investigate and report |
| `validation-only` | Validate existing work |

Tool-specific mappings, such as Codex Plan Mode, are in [current-provider profiles](execution-routing.md#8-current-provider-profiles).

## 14. LHS decision

Use LHS when implementation gravity warrants staged execution, such as when several of these are true:

- more than three files
- several system or documentation areas
- dependency order
- tests and docs
- phased commits
- rollback or compatibility risk
- Architecture, contracts, or workflows change
- a named Initiative or Delivery Unit contains several Build Units
- follow-up work is likely

LEAP LHS stages execution. It does not define the project's strategic hierarchy. The stage format is in [LEAP LHS](leap-lhs.md).

## 15. Risk taxonomy

| Risk | Example control |
|---|---|
| Product | Charter and no-build review |
| Source truth | Baseline Freshness Check and reconciliation |
| Architecture | Recon and right-sizing |
| Dependency contract | Dependency & Contract Recon |
| Data | Human approval and rollback plan |
| Security / Privacy | Mandatory checkpoint |
| AI behavior | Explicit behavior constraints and evaluation |
| UX | Acceptance criteria and manual checks |
| Collaboration | ownership map, branch review, merge order |
| Verification | concrete tests and evidence |

Details: [LEAP Risk Taxonomy](risk-taxonomy.md).

Sensitive-area rule:

```text
If the change can affect money, identity, privacy, data durability,
legal exposure, or user trust, stop and ask.
```

## 16. Destructive-change protocol

Destructive changes include dropping or rewriting data, changing IDs or ownership, rewriting migrations, changing auth/session behavior, removing workflows, or changing infrastructure in a hard-to-reverse way.

Default:

```text
Destructive changes are not allowed unless explicitly authorized.
```

Every relevant Prompt should state:

```text
Destructive changes: allowed / not allowed / limited
Rollback required: yes / no
Data preservation required: yes / no
Human approval required before migration: yes / no
```

When destructive change removes obsolete repository artifacts, use the approval, dependency, replacement-evidence, and validation contract in [LEAP Repository Cleanup](repository-cleanup.md). Destructive cleanup must not retain an unapproved in-tree backup of the retired design.

## 17. Agent failure modes

LEAP should guard against:

- hallucinating files, APIs, or business rules
- following stale docs over repo reality
- treating archived docs as active
- broad refactors disguised as cleanup
- silent schema or contract changes
- adding dependencies without approval
- weakening tests to make them pass
- confusing Initiative with Domain
- treating Roadmap placement as Initiative identity
- treating Build Units as independently deployable without evidence
- letting a Skill broaden Build Unit scope or execution authority
- assuming a required Skill exists without identifying its source and loading method
- forcing every project to create every documentation level
- globally replacing legacy Layer terminology
- completing the task while violating non-goals

## 18. Operational outputs

Omit sections with nothing material. Do not pad with N/A.

### Charter output

A Charter output should include:

- mode and intake classification
- original wording and current understanding
- Ideation Loop and Materiality status
- evidence labels
- Greenfield or Brownfield findings
- no-build review
- MVP or current scope boundary
- Strategic Outcomes and Initiative recommendations
- Roadmap, Domain, Architecture, and documentation-baseline recommendations
- gap register and migration map when needed
- prompt backlog
- human checkpoints
- gate decision

### Recon output

A Recon output should include:

- source-of-truth and baseline checks
- Charter gate check
- Materiality check
- repo reality and branch drift
- documentation lifecycle and strategic reconciliation
- existing-functionality collision and stale assumptions
- cross-Initiative / cross-Domain impacts
- planning-boundary review
- Delivery Unit and Build Unit inventory
- Capability / Skill Review when applicable
- recommended sequence
- dependency, destructive-change, and risk review, including coding-agent risks
- Architecture right-sizing
- human checkpoints
- Agent Execution Configuration
- clarification questions, if material
- gate decision

### Cleanup output

A Cleanup output should include:

- scope, governing sources, and repository reality
- cleanup-mode assessment
- artifact inventory and classification
- authority and canonical-replacement evidence
- inbound references, dependencies, and consumers
- public-path, retention, and compatibility obligations
- exact proposed decommission set
- blocked, unknown, and human-decision candidates
- reference and source-of-truth repair plan
- structural, semantic, and behavioral validation plan
- forbidden-pattern checks
- explicit approval requirement and gate decision

### Prompt output

A generated Prompt should include:

- Prompt type and LHS decision
- user action before submission (optional)
- Agent Execution Configuration
- objective and traceability
- current repo reality
- source-of-truth instructions
- assumptions
- scope and constraints
- Capability / Skill composition when used
- implementation sequence
- verification
- stop conditions
- branch and commit instructions
- source-of-truth update policy
- completion report

## 19. Compatibility and migration

Existing downstream Layer docs remain valid source inputs until reconciled. Classify each generic `Layer` before migrating it, using the [project-documentation migration guide](maintainer/project-documentation-migration.md). Do not globally replace `Layer`, and do not rename public paths merely for terminology consistency.
