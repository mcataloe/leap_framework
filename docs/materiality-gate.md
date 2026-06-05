<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: supporting-framework-rule-reference
  authority: supporting
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Materiality Gate

Materiality Gate is the LEAP clarification discipline for deciding when to ask the user a question, when to inspect available sources first, and when to proceed with a stated assumption.

Materiality Gate is not a lifecycle phase. It is LEAP's question filter.

It refines LEAP's confidence and readiness behavior. It does not weaken source-of-truth, readiness-gate, hard-blocker, destructive-change, or sensitive-area rules.

## Core rule

LEAP agents must avoid unnecessary clarification loops.

Before asking a clarifying question, determine whether the answer would materially change the output.

A question is material only when the answer would change one or more of the following:

- architecture or repository structure
- implementation strategy
- scope or acceptance criteria
- risk assessment
- source-of-truth hierarchy
- compatibility or dependency behavior
- validation strategy
- user-facing recommendation
- irreversible or hard-to-reverse changes

If the missing information would only affect naming, wording, formatting, ordering, tone, minor preference, or polish, do not ask. Make a reasonable assumption, state it clearly, and proceed.

Plain-English rule:

- If the answer changes the work, ask.
- If the answer is discoverable, inspect first.
- If the answer only changes polish, assume and proceed.
- If the missing answer affects safety, source truth, destructive change, privacy, money, identity, legal exposure, or user trust, stop and ask.

If the question is really which LEAP workflow to use, start with the [workflow chooser](user/which-leap-workflow.md).

## Relationship to confidence

LEAP should still aim for high confidence before final recommendations, but confidence thresholds must not be used to justify avoidable questioning.

Use this rule:

```text
If confidence is below target because of non-material unknowns, proceed with assumptions.
If confidence is below target because of material unknowns, ask the smallest useful set of clarifying questions needed to unblock the work.
```

When questions are necessary, ask no more than three targeted questions at a time unless the user explicitly requests a more exhaustive discovery process.

## Required classification

Before asking the user, classify missing context as:

```text
Material - answer would change the work, risk, or decision.
Non-material - answer would only refine style, naming, wording, formatting, or polish.
Discoverable - answer should be inspected from repo/docs/contracts/tooling before asking.
Safe assumption - answer can be reasonably assumed and stated without changing the decision.
```

Question order:

```text
1. Inspect discoverable sources first.
2. Convert non-material unknowns into stated assumptions.
3. Proceed on safe assumptions when not blocked.
4. Ask only unresolved material questions.
```

## Materiality Check output

Recon, Charter, or Prompt-generation outputs may include a Materiality Check when clarification decisions affect the next gate.

Suggested section:

```text
## Materiality Check

### Material Unknowns
Questions or missing facts that would change architecture, scope, risk, acceptance criteria, source-of-truth hierarchy, validation strategy, or implementation path.

### Assumptions Proceeding Under
Reasonable assumptions being used so work can continue without unnecessary blocking.

### Deferred Non-Material Details
Items that may improve polish, naming, formatting, or preference alignment but do not block the current recommendation.

### Question Decision
State whether LEAP should:
- proceed with assumptions
- inspect repo/docs first
- ask targeted clarifying questions
```

## Examples

### Non-material unknown

If the user asks for Recon on dependency tracking, do not block on file naming or table formatting.

Acceptable assumption:

```text
Assumption: use a human-readable Markdown dependency register for the first version unless the repo already contains a machine-readable convention. This can later evolve into YAML or JSON if automation requires it.
```

### Material unknown

This question is material:

```text
Should dependency tracking be advisory only, or should breaking contract drift block implementation?
```

It changes CI behavior, risk posture, and developer workflow.

### Discoverable unknown

Do not ask whether the repo has a dependency manifest when repo access exists. Inspect the repository first for dependency, contract, package, integration, or documentation evidence.

## Interaction with hard blockers

Materiality Gate does not override hard blockers.

If a missing answer affects money, identity, privacy, data durability, legal exposure, user trust, destructive change permission, source-of-truth conflict, repo reality, or unapproved architecture, stop and ask or require human approval according to the relevant LEAP rule.
