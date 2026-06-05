# LEAP for Humans

LEAP is for people who want to build software without letting confusion become code.

It is especially useful when AI coding agents are involved, because agents are very good at turning instructions into changes. They are not automatically good at knowing whether the instructions are complete, current, safe, or wise.

## The human problem LEAP solves

Humans often describe solutions from the outside:

```text
I want a dashboard.
I want an app that automates this.
I want AI to help users do that.
I want the platform to support this workflow.
```

Those statements may be directionally useful, but they are not yet implementation instructions.

The missing details matter:

```text
Who uses it?
What do they do today?
What is painful?
What is the smallest useful version?
What should stay manual for now?
What must never happen?
What data is sensitive?
What already exists in the codebase?
Which docs are canonical?
Which docs are stale or archived?
What does success look like?
```

LEAP helps uncover those missing details before implementation begins.

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Charter asks where the project is going. Recon checks what is true. Prompt turns the next bounded task into instructions. Implementation changes the repo. Validation/Handoff proves what happened and reports what remains.

LEAP LHS is one structured LEAP Prompt format for staged implementation. It is useful when the work has enough coordination, risk, or sequencing to justify it. For the formal lifecycle and LHS rules, use the [canonical framework reference](../leap.md).

## Questions are the source of answers

LEAP uses questions because good questions expose the difference between:

```text
what someone imagines
```

and

```text
what the system must actually do
```

A good LEAP question is not random. It should clarify the next blocker.

Examples:

```text
Who is the first user?
What do they do today without this feature?
What is the first moment where this becomes useful?
What should the system refuse to do?
What is manual for now?
What would make this not worth building?
What part of the repo already handles this?
What would break if this changed?
Which docs are source truth?
Which docs should be archived?
```

## The Ideation Loop

LEAP's ideation loop is:

```text
Intent -> Questions -> Evidence labels -> Assumptions -> Pressure test -> Revised intent -> Gate decision
```

This loop continues while the next step is unsafe.

The goal is not endless discussion. The goal is to reach the next safe gate.

## Evidence labels

LEAP separates what is known from what is guessed.

```text
Known: confirmed by the user, repo, tests, or current docs
Assumed: plausible but not confirmed
Unknown: missing
Contested: sources conflict
Needs Decision: a human must choose
Deprecated: used to be true, but no longer governs
```

This matters because a polished assumption is still an assumption.

## Readiness gates

LEAP uses gates instead of fake precision scores.

```text
C0 Blocked: only ask questions
C1 Discovery Ready: enough to explore
C2 Concept Ready: enough to draft the concept
C3 Pressure-Test Ready: enough to challenge the idea
C4 Planning Ready: enough to plan Recon, docs, or prompt backlog
C5 Coding-Prompt Ready: enough to hand off to a coding agent
```

The important rule:

```text
A high confidence feeling does not override a hard blocker.
```

## What counts as a hard blocker?

Implementation planning should stop when any of these are missing:

```text
- primary user
- concrete problem
- current workflow or workaround
- MVP or scope boundary
- concrete non-goals
- sensitive-data/risk profile when applicable
- source truth for existing projects
- repo reality for existing repos
- canonical-vs-archived doc status
- verification path
- human approval for risky decisions
- execution profile for the coding agent
```

## Brownfield docs

Existing projects often have useful but messy documentation. LEAP Charter - Brownfield Mode reconciles that documentation before implementation work depends on it.

The rule is:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

This means useful current content moves into canonical docs, old originals are preserved in an archive, and agents are told where to start.

For the full Brownfield Charter doctrine, use [LEAP Charter](../leap-charter.md).

## LEAP should feel practical

LEAP is not supposed to make small work heavy.

Use the smallest version of LEAP that controls the risk.

For a tiny fix, a short LEAP brief may be enough.

For project alignment or stale docs, use LEAP Charter.

For a major feature or focused repo question, use LEAP Recon.

For implementation, use LEAP Prompt. Use LEAP LHS only when the work is layered, staged, or large enough to benefit from House Standard-style execution.

If you are not sure where to start, use the [workflow chooser](which-leap-workflow.md).

## The human-friendly summary

```text
Decide what problem matters.
Check what is already true.
Separate facts from guesses.
Canonicalize current docs.
Archive stale docs.
Make the work small enough to verify.
Tell the agent what not to touch.
Tell the agent when to stop.
Then build only the bounded task.
```
