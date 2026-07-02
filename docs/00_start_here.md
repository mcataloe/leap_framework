<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: entrypoint
  authority: entry-point
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Start Here: LEAP in Plain English

**LEAP - Layered Execution & Alignment Protocol** helps you avoid asking a coding agent to build from confusion.

Coding agents can move quickly. That is useful only when the idea is clear, source documents are current, repository state is understood, strategic ownership is explicit, and the task is small enough to verify.

LEAP helps with the messy middle between:

```text
"I have an idea"
```

and:

```text
"Here is a bounded implementation task a coding agent can safely run."
```

## LEAP in 60 seconds

LEAP helps you:

1. Clarify the Mission and intended outcome.
2. Inspect what is already true.
3. Separate facts from assumptions.
4. Identify Strategic Outcomes and Initiatives.
5. Separate Roadmap timing from persistent Domains and Architecture.
6. Break Delivery Units into bounded Build Units.
7. Tell the agent what to do, what not to touch, and when to stop.
8. Validate the result.

Use the lightest LEAP workflow that controls the actual risk. Tiny, obvious work may use a normal prompt. Small bounded coding work may use a [Quick LEAP Brief](user/quick-leap-brief.md).

## The project-documentation model

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

Supporting views remain separate:

```text
Roadmap      = timing, priority, dependencies, milestones, status, parallelism
Domain Map   = persistent responsibility boundaries
Architecture = technical structure
```

This means:

- several Initiatives may run in parallel
- a Roadmap schedules Initiatives but does not permanently own them
- one Initiative may touch several Domains
- one Domain may support several Initiatives
- a Delivery Unit is a releasable, enabled, adoptable, or demonstrable increment
- a Build Unit is bounded implementation and is not necessarily independently deployable
- small work may collapse the Delivery Unit level

Read [Project Documentation Model](project-documentation-model.md) for the full doctrine.

## What happened to Layer?

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level because it was used for phases, capabilities, Domains, Architecture, and implementation scope at the same time.

LEAP still preserves:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified Architecture Layers
- historical and compatibility references
- existing downstream Layer docs until they are reconciled

See [Project Documentation Migration](maintainer/project-documentation-migration.md) for legacy Layer classification.

## The questions LEAP asks

```text
Why does this solution exist?
What measurable change are we trying to create?
Which Initiative owns the coordinated work?
Can several Initiatives run in parallel?
What belongs on the Roadmap now?
Which Domains and Architecture areas are affected?
What can be released, enabled, adopted, or demonstrated?
What Build Units can be implemented and verified safely?
What already exists?
Which docs are canonical, stale, or archived?
Which dependencies or contracts affect the work?
What should not be built?
What could go wrong?
When must the agent stop?
How do we prove completion?
```

If those answers are unclear, LEAP keeps asking only the material questions needed before implementation Prompt generation.

## How to choose a workflow

- Use the [workflow chooser](user/which-leap-workflow.md) to compare normal prompts, Quick Brief, Charter, Recon, Prompt, and LHS.
- Use [When Not to Use LEAP](user/when-not-to-use-leap.md) when full LEAP is heavier than the task.
- Use the [Quick LEAP Brief](user/quick-leap-brief.md) for the smallest useful coding-agent handoff.
- Use the [canonical framework reference](leap.md) for formal doctrine.

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Charter establishes or reconciles the baseline when Mission, source truth, Strategic Outcomes, Initiatives, Roadmap, Domains, Architecture, or documentation posture is unclear.

Recon begins with Baseline Freshness Check and investigates a focused Initiative, Delivery Unit, Build Unit, Domain, Architecture area, dependency, risk, question, or legacy Layer.

LEAP Prompt is the agent-ready instruction family.

LEAP LHS is one Prompt format for staged implementation. It is not a lifecycle phase and it does not define the strategic hierarchy.

## Materiality Gate

Materiality Gate filters questions:

- inspect discoverable sources first
- ask only when the answer changes direction, scope, Architecture, risk, source truth, validation, acceptance, or compatibility
- proceed on stated assumptions for non-material unknowns
- stop for safety, destructive changes, privacy, money, identity, legal exposure, user trust, or unsafe source truth

See [Materiality Gate](materiality-gate.md).

## Shortest useful checklist

Before handing work to a coding agent, answer:

```text
1. What Mission or outcome does this serve?
2. What Strategic Outcome and Initiative own it?
3. Is a Delivery Unit needed, or can it be collapsed?
4. What is the bounded Build Unit or task?
5. What is the current repository state?
6. Which docs are canonical?
7. Which docs are stale, archived, or do-not-use?
8. Which Domains and Architecture areas are affected?
9. What is in scope and out of scope?
10. What should the agent not touch?
11. What tests or checks prove success?
12. When should the agent stop?
13. What execution profile should be used?
```

If you cannot answer these, run Charter or Recon first.

## AGENTS.md adoption

LEAP `AGENTS.md` templates are distributed from:

```text
https://github.com/mcataloe/leap_agent_pack
```

Use [LEAP Project Setup](user/leap_project_setup.md) for ChatGPT Project Instructions, repository-level `AGENTS.md`, coding-agent population, and the first LEAP workflow.

## Rule of thumb

```text
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```

LEAP should reduce chaos, not create ceremony.
