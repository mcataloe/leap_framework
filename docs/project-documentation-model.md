<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-reference
  authority: canonical
  applies_to: downstream-leap-projects
END_LEAP_DOC_METADATA
-->

# LEAP Project Documentation Model

## Purpose

This document defines the canonical project-specific documentation hierarchy used by LEAP.

LEAP must support solutions where several major bodies of work advance in parallel. It must also keep strategy, scheduling, persistent domains, architecture, release boundaries, and implementation boundaries distinct.

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

The hierarchy describes traceability. It does not require one Markdown file for every level and it does not imply that every relationship in a real system is a strict tree.

## Core principle

```text
Mission defines why.
Strategic Outcomes define the change sought.
Initiatives coordinate the work.
Delivery Units define releasable or adoptable increments.
Build Units define bounded implementation.
Roadmaps schedule.
Domains organize responsibility.
Architecture organizes technical structure.
```

## 1. Mission / Project Charter

The Mission or project-specific Project Charter defines:

- why the solution exists
- who it serves
- what problem it addresses
- governing intent and decision principles
- product boundaries and explicit non-goals
- what an initial or current version should prove

A project-specific Project Charter is an artifact that LEAP Charter may create or reconcile. It is not the same thing as the LEAP Charter process.

## 2. Strategic Outcome

A Strategic Outcome is a measurable or observable condition that advances the Mission.

A Strategic Outcome should identify:

- the desired change
- the beneficiary
- the success signal
- the evidence or measurement used to judge progress
- relevant constraints
- a time horizon when useful

Example:

```text
Ordinary nonprofit eligibility checks can be completed without manual
operator intervention while preserving auditable evidence.
```

Strategic Outcomes may live in the Project Charter, product strategy, or a separate strategic-outcome registry. Larger projects should use stable identifiers when several Initiatives advance the same outcome.

## 3. Initiative

An Initiative is a temporary, outcome-oriented body of coordinated work that advances one or more Strategic Outcomes.

An Initiative:

- may run in parallel with other Initiatives
- may span several Domains
- may span repositories or teams
- may contain one or more Delivery Units
- has explicit success criteria and non-goals
- identifies dependencies, risks, and human checkpoints
- ends when completed, abandoned, merged, or superseded

An Initiative is not a permanent Domain and is not owned by one Roadmap placement. It may exist before scheduling, while paused, or after removal from an active Roadmap.

### Minimum Initiative metadata

```text
Initiative ID:
Title:
Status:
Strategic Outcomes advanced:
Purpose:
Success criteria:
Non-goals:
Affected Domains:
Affected repositories:
Dependencies:
Risks:
Delivery Units:
Roadmap placement:
Human owner / approver:
Last reconciled:
```

Recommended Initiative statuses include:

- Proposed
- Approved
- Scheduled
- Active
- Paused
- Completed
- Abandoned
- Superseded

## 4. Delivery Unit

A Delivery Unit is a coherent functional increment that can be released, deployed, enabled, adopted operationally, or demonstrated as an end-to-end capability.

A Delivery Unit may contain one or more Build Units.

Use a Delivery Unit when:

- an Initiative contains several Build Units
- work has several meaningful release increments
- work spans repositories or teams
- a deployable, adoptable, or demonstrable capability boundary exists
- acceptance requires an end-to-end capability rather than one implementation commit

The Delivery Unit level is conditionally collapsible. A small Initiative may go directly to one Build Unit when that Build Unit delivers the full Initiative outcome and a separate Delivery Unit would add ceremony without reducing risk.

### Minimum Delivery Unit metadata

```text
Delivery Unit ID:
Initiative:
Outcome delivered:
Release / enablement / adoption boundary:
Scope:
Non-goals:
Affected Domains:
Affected Architecture Areas:
Build Units:
Dependencies:
Acceptance criteria:
Validation:
Rollback or disablement posture:
Status:
```

## 5. Build Unit

A Build Unit is a bounded implementation responsibility that can be implemented, tested, reviewed, and usually committed independently.

A Build Unit:

- must trace to an Initiative
- must trace to a Delivery Unit when the Delivery Unit level is used
- states scope and exclusions
- states dependencies and sequencing constraints
- states validation and evidence requirements
- states stop conditions
- should be small enough to avoid unapproved product or architecture decisions
- is not required to be independently deployable
- is not required to provide independently usable end-user value

### Minimum Build Unit metadata

```text
Build Unit ID:
Initiative:
Delivery Unit, if used:
Objective:
Scope:
Out of scope:
Affected Domains:
Affected Architecture Areas:
Dependencies:
Files / areas to inspect:
Files / areas not to touch:
Acceptance criteria:
Validation:
Stop conditions:
Commit guidance:
Status:
```

A Build Unit is too large when the implementation agent must modify unrelated capabilities, make unapproved architecture decisions, touch shared contracts without ownership clarity, or compress durable design into an improvised implementation.

## 6. Roadmap

A Roadmap is a planning projection over Initiatives and Delivery Units. It shows:

- priority
- timing
- sequence
- parallel work
- milestones
- dependencies
- capacity assumptions
- release targets
- status

A Roadmap does not permanently own Initiative identity. An Initiative may appear on zero or more Roadmap views over time.

Example:

```text
                    Q1          Q2          Q3
Verification       INIT-01 ──────────
Developer Platform       INIT-02 ─────────────
Operations          INIT-03 ─────
Public Experience               INIT-04 ───────
```

A Roadmap may group work visually by Domain, team, value stream, quarter, release, or another useful view, but the view does not redefine what an Initiative is.

## 7. Domain

A Domain is a persistent business, responsibility, ownership, or technical boundary.

Examples:

```text
Identity
Eligibility Verification
Organization Records
Developer Platform
Billing
Reporting
```

Initiatives and Domains have a many-to-many relationship:

- one Initiative may touch several Domains
- one Domain may support several Initiatives

A Domain is not a temporary Roadmap lane and should not be renamed whenever strategic priorities change.

### Domain map expectations

A Domain map may identify:

- Domain purpose
- ownership
- key entities and workflows
- public contracts
- dependencies
- data responsibility
- active Initiatives touching the Domain

## 8. Architecture

Architecture documentation describes where and how implementation resides.

It may include:

- system context
- services and components
- data models
- contracts and events
- deployment topology
- security boundaries
- qualified technical Layers

Qualified terminology such as Presentation Layer, Application Layer, Domain Layer, Persistence Layer, and Infrastructure Layer remains valid.

Architecture is not the default strategic planning hierarchy.

## 9. Layer compatibility rule

Generic unqualified project-planning `Layer` is legacy-compatible and deprecated as the preferred LEAP planning level.

Do not globally replace every use of `Layer`.

Preserve:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified architectural Layers
- historical or compatibility references
- existing downstream Layer documents until they are reconciled

When a legacy Layer document is encountered, determine whether it actually represents an Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or mixed collection before changing terminology.

See [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md) for migration guidance.

## 10. Required traceability relationships

```text
Mission / Project Charter
  owns or governs:
    Strategic Outcomes

Strategic Outcome
  advanced by:
    one or more Initiatives

Initiative
  advances:
    one or more Strategic Outcomes
  touches:
    one or more Domains
  appears on:
    zero or more Roadmap views over time
  contains:
    one or more Delivery Units, unless collapsed

Delivery Unit
  belongs to:
    one Initiative
  delivers:
    a releasable, deployable, enabled, adoptable, or demonstrable increment
  contains:
    one or more Build Units

Build Unit
  belongs to:
    one Initiative
  belongs to:
    one Delivery Unit when Delivery Units are used
  affects:
    one or more Domains or Architecture areas
  defines:
    scope, exclusions, dependencies, validation, and stop conditions
```

References across Initiatives are allowed for shared dependencies, shared contracts, and coordinated release work. LEAP should not force a strict tree when real relationships are many-to-many.

## 11. Source-of-truth ownership

No two canonical documents should own the same truth.

A practical ownership model is:

| Truth | Preferred owner |
|---|---|
| Mission, boundaries, decision principles | Project Charter |
| Desired measurable changes | Strategic Outcomes |
| Outcome-oriented coordinated work | Initiative registry or Initiative docs |
| Timing, priority, milestones, parallelism | Roadmap |
| Persistent responsibility boundaries | Domain map and Domain docs |
| Technical structure | Architecture docs and ADRs |
| Releasable or adoptable increments | Delivery Unit docs |
| Bounded implementation work | Build Unit docs or approved LEAP Prompts |
| Actual implementation state | Repo reality, tests, schemas, and merged code |

Generated planning documents are Draft until ratified.

## 12. Small-project collapse rules

Small projects may combine the hierarchy into one or a few documents.

Acceptable examples:

```text
Project Charter containing Strategic Outcomes and one Initiative
Initiative document containing one collapsed Delivery Unit and Build Unit
One approved LEAP Prompt containing Initiative and Build Unit traceability
```

Do not create separate files merely to satisfy the hierarchy when they would not improve clarity, traceability, ownership, or implementation safety.

## 13. Scaled documentation example

The following is an example, not a mandatory structure:

```text
docs/
  00_start_here.md

  01_charter/
    00_project_charter.md
    01_source_of_truth.md

  02_strategy/
    00_product_strategy.md
    01_strategic_outcomes.md
    02_initiative_registry.md
    03_roadmap.md

  03_domains/
    00_domain_map.md
    identity.md
    verification.md
    developer_platform.md

  04_architecture/
    00_architecture_overview.md
    01_system_context.md
    02_data_model.md
    03_api_surface.md

  05_delivery/
    INIT-001/
      00_initiative.md
      DU-001.md
      DU-002.md

  06_build_units/
    INIT-001/
      BU-001.md
      BU-002.md

  07_decisions/
  08_prompts/
  99_archive/
```

Existing project conventions may be retained. Semantic clarity matters more than folder conformity.

## 14. Cross-repository Initiatives

An Initiative may span repositories when the outcome requires coordinated changes across services, applications, contracts, infrastructure, or documentation.

A cross-repository Initiative should identify:

- participating repositories
- ownership per repository
- shared contracts
- merge or release order
- compatibility posture
- independent rollback boundaries
- repository-specific Delivery Units and Build Units

Do not give one agent unbounded write access across repositories without explicit ownership, scope, validation, and commit guidance.

## 15. Status and lifecycle expectations

Project planning status must not compete with repo reality.

Recommended rules:

- Initiative status reflects coordinated strategic work.
- Delivery Unit status reflects release or adoption readiness.
- Build Unit status reflects implementation progress.
- Roadmap status reflects current planning placement.
- Domain and Architecture docs are persistent and updated as system reality changes.
- Completed plans are historical unless remaining work is explicitly reactivated.

## 16. Anti-patterns

Avoid:

- treating a Roadmap as the permanent owner of Initiatives
- using Domain and Initiative as synonyms
- making every Build Unit independently deployable
- making Delivery Units mandatory for trivial work
- numbering capabilities in a way that falsely implies strict sequence
- using one generic Layer term for phase, capability, Domain, architecture, and implementation scope
- creating one file for every concept regardless of project size
- defining Initiative status in several competing canonical documents
- asking an implementation agent to infer Strategic Outcomes or Initiative ownership
- migrating legacy Layer documents through blind filename or text replacement
