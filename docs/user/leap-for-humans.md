# LEAP for Humans

LEAP helps people build software without letting confusion become code.

Coding agents can turn instructions into changes quickly. LEAP helps make sure those instructions are current, bounded, strategically aligned, and verifiable.

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Charter establishes or reconciles direction and source truth. Recon checks what is true. Prompt turns bounded work into instructions. Implementation changes the repository. Validation/Handoff proves what happened.

LEAP LHS is the Layered House Standard Prompt format for staged implementation. It is not a lifecycle phase and it does not define the project's strategic hierarchy.

## Project documentation in plain English

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

- **Mission / Project Charter:** why the solution exists, who it serves, boundaries, and non-goals.
- **Strategic Outcome:** the measurable or observable change being sought.
- **Initiative:** temporary coordinated work advancing one or more Strategic Outcomes.
- **Delivery Unit:** a releasable, deployable, enabled, adoptable, or demonstrable increment.
- **Build Unit:** bounded implementation that can be implemented, tested, reviewed, and usually committed independently.

Several Initiatives may run in parallel.

A small Initiative may collapse the Delivery Unit level when one Build Unit delivers the complete outcome.

A Build Unit is not required to be independently deployable or independently useful to an end user.

## Roadmap, Domain, and Architecture

These are separate views:

- **Roadmap:** timing, priority, milestones, dependencies, release targets, status, and parallel work.
- **Domain:** persistent business, responsibility, ownership, or technical boundary.
- **Architecture:** technical structure, components, data, contracts, deployment, and qualified technical Layers.

A Roadmap schedules Initiatives but does not permanently own them.

Initiatives and Domains have a many-to-many relationship.

## Legacy Layer terminology

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level because it was used for phases, capabilities, Domains, Architecture tiers, release increments, and implementation tasks at the same time.

LEAP still preserves:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified Architecture Layers
- existing legacy Layer docs until reconciled

Classify what a legacy Layer actually represents before renaming it:

- Initiative
- Delivery Unit
- Build Unit
- Domain
- Architecture Layer
- Phase
- mixed or unclear collection

See [Project Documentation Model](../project-documentation-model.md) and [Project Documentation Migration](../maintainer/project-documentation-migration.md).

## Questions LEAP asks

```text
Why does the solution exist?
What measurable change should happen?
Which Initiative owns the coordinated work?
Can several Initiatives run in parallel?
What belongs on the Roadmap now?
Which Domains and Architecture areas are affected?
What can be delivered end to end?
What Build Unit is small enough to verify?
What already exists?
Which docs are canonical, stale, or archived?
What should never happen?
How do we prove completion?
```

## Evidence and readiness

LEAP separates Known, Assumed, Unknown, Contested, Needs Decision, and Deprecated information.

Readiness gates:

```text
C0 Blocked
C1 Discovery Ready
C2 Concept Ready
C3 Pressure-Test Ready
C4 Planning Ready
C5 Coding-Prompt Ready
```

A confident feeling does not override a hard blocker.

## Brownfield documentation

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Existing Layer docs are semantically reconciled before renaming or moving them.

## Use the lightest workflow

- Tiny obvious change: normal prompt
- Small bounded coding task: Quick LEAP Brief
- New or unclear direction: Charter
- Focused uncertainty or repository question: Recon
- Obsolete artifacts competing with current truth: Cleanup
- Ready bounded implementation: LEAP Prompt
- Staged multi-Build-Unit work: LHS Prompt

Small projects do not need one file per concept. The model exists to clarify meaning and traceability, not to create documentation ceremony.

## Human-friendly summary

```text
Decide why the solution exists.
Define the change you want.
Organize coordinated work into Initiatives.
Use the Roadmap to schedule, not to define identity.
Keep Domains persistent and Architecture structural.
Define Delivery Units when release or adoption boundaries matter.
Make Build Units small enough to verify.
Check what is already true.
Tell the agent what not to touch and when to stop.
Then build only the bounded work.
```
