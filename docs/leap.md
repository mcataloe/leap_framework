# LEAP Framework

LEAP — **Layered Execution & Alignment Protocol** — is a documentation-first software-delivery framework for turning rough intent into pressure-tested direction, source-grounded plans, and safe, bounded coding-agent handoffs.

The current lifecycle is:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the **Layered House Standard** Prompt format for staged implementation. It is part of the LEAP Prompt family, not a mandatory lifecycle stage.

LEAP Skills are reusable execution capabilities that may be selected and composed inside that lifecycle. They are not a new lifecycle phase or a replacement for Build Units. Canonical Skill guidance lives in [`leap-skills.md`](leap-skills.md).

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
- execution-configuration recommendation
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

The approved Prompt is executed by Codex or another coding agent. Implementation must remain within scope, preserve non-goals, follow repository conventions, and stop when a stop condition is met.

When a Prompt requires a Skill, implementation must use the named source and loading method rather than assuming the harness already has that Skill. Skill tool requirements cannot widen Prompt permissions.

### Validation/Handoff

Validation/Handoff reports:

- changes made
- files changed
- tests and checks run
- checks not run and why
- deviations
- assumptions
- Skills used, when material to completion confidence
- stop conditions
- documentation updates
- risks and follow-up LEAP work

## 3. Canonical project-documentation model

The preferred traceability hierarchy is:

```text
Mission / Project Charter
        ↓
Strategic Outcome
        ↓
Initiative
        ↓
Delivery Unit
        ↓
Build Unit
```

Supporting views are separate:

```text
Roadmap      = timing, priority, dependencies, milestones, status, and parallelism
Domain Map   = persistent business, responsibility, ownership, or technical boundaries
Architecture = structural implementation boundaries and technical organization
```

Canonical reference: [`project-documentation-model.md`](project-documentation-model.md).

Migration guidance: [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md).

### Mission / Project Charter

Defines why the solution exists, who it serves, boundaries, non-goals, governing intent, and what the current version should prove.

### Strategic Outcome

Defines a measurable or observable change that advances the Mission.

### Initiative

A temporary, outcome-oriented body of coordinated work. Initiatives may run in parallel, span Domains and repositories, and contain one or more Delivery Units.

### Delivery Unit

A releasable, deployable, enabled, adoptable, or demonstrable functional increment. It may contain several Build Units.

The level is optional when one small Build Unit directly delivers the full Initiative outcome.

### Build Unit

A bounded implementation responsibility that can be implemented, tested, reviewed, and usually committed independently.

A Build Unit is not required to be independently deployable or independently useful to an end user.

A LEAP Skill is orthogonal to this hierarchy. A Build Unit defines **what** bounded responsibility is delivered; a Skill defines reusable **how** for specialized execution. Skills must not be inserted into the Mission-to-Build-Unit traceability chain.

### Roadmap

A planning projection over Initiatives and Delivery Units. It does not permanently own Initiative identity.

### Domain

A persistent responsibility boundary. Initiatives and Domains have a many-to-many relationship.

### Architecture

The technical structure showing where implementation resides. Qualified terms such as Presentation Layer and Persistence Layer remain valid.

### Layer compatibility

Generic unqualified project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level.

Preserve:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified Architecture Layers
- historical and compatibility references
- existing downstream Layer docs until reconciled

Do not globally replace `Layer`. Classify its meaning before migration.

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

## 5. Materiality Gate

Before asking a question, classify missing context as:

- **Material** — changes architecture, scope, risk, source-truth hierarchy, validation, acceptance criteria, compatibility, or implementation path
- **Non-material** — changes naming, wording, formatting, or minor preference
- **Discoverable** — should be inspected from repo, docs, contracts, or tooling
- **Safe assumption** — can be stated without changing the decision

Question sequence:

```text
1. Inspect discoverable evidence.
2. Convert non-material unknowns into stated assumptions.
3. Proceed on safe assumptions.
4. Ask only unresolved material questions.
5. Ask the smallest useful set.
```

Hard blockers override this rule.

## 6. Readiness gates

- C0: Blocked
- C1: Discovery Ready
- C2: Concept Ready
- C3: Pressure-Test Ready
- C4: Planning Ready
- C5: Coding-Prompt Ready

C5 requires:

- source truth
- repo reality
- bounded scope
- accepted assumptions
- validation path
- stop conditions
- agent/tool
- model
- reasoning level
- execution mode
- resolvable required Skill sources and loading methods, when Skills are used

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

Rules:

- ordinary agent reasoning and repository guidance remain valid when no explicit Skill is needed
- Skills do not become a planning level
- Skills do not own Initiative, Delivery Unit, or Build Unit identity
- Skills may shape local execution procedure but may not expand Build Unit scope
- required Skills must identify a resolvable source and loading method
- Skill tool requirements may not widen Prompt permissions
- Skill-specific verification should be carried into the Prompt and Validation/Handoff
- do not create a new Skill when a one-off instruction is clearer and cheaper

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

## 13. Agent Execution Configuration

Every agent-ready Prompt should state:

```text
Agent / Tool:
Codex Plan Mode, when Codex-targeted:
Model:
Reasoning Level:
Execution Mode:
Scope Scale:
Repository:
Branch / Worktree:
Permissions:
Skill Sources / Loading Method, when used:
Validation:
Commit Guidance:
```

Execution modes:

| Mode | Meaning | Typical Codex Plan Mode |
|---|---|---|
| `implement-directly` | Make a tiny obvious change | Off |
| `repo-preflight-then-implement` | Verify repo reality and proceed when clear | Off |
| `plan-first` | Return a plan for approval before editing | On |
| `recon-only` | Investigate and report | User decision required |
| `validation-only` | Validate existing work | Off unless fixes are requested |

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

LEAP LHS stages execution. It does not define the project's strategic hierarchy.

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

### Charter output

A Charter output should include:

- mode and intake classification
- original wording and current understanding
- Ideation Loop and Materiality status
- evidence labels
- readiness gate
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

- Framework interpretation
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
- dependency, destructive-change, and risk review
- Architecture right-sizing
- human checkpoints
- execution-log expectations
- coding-agent risk forecast
- Agent Execution Configuration
- clarification questions, if material
- gate decision

### Prompt output

A generated Prompt should include:

- Prompt type and LHS decision
- user action before submission
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

Existing downstream Layer docs remain valid source inputs until reconciled.

When encountered, classify whether the Layer represents:

- Initiative
- Delivery Unit
- Build Unit
- Domain
- Architecture Layer
- Phase
- mixed or unclear collection

Do not rename public paths merely for terminology consistency. Preserve compatibility and migrate only when semantic clarity, source-truth safety, or implementation coordination materially improves.