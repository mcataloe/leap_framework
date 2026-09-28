<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: supporting-framework-rule-reference
  authority: supporting
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Materiality Gate

Materiality Gate is LEAP's shared clarification discipline for deciding whether missing context should be inspected, asked about, assumed, or treated as a stop condition.

Materiality Gate is not a lifecycle phase. It is a framework-level execution primitive used by Charter, Recon, Prompt generation, implementation handoff, governance, destructive-change work, and other materially consequential LEAP workflows.

It refines LEAP's confidence and readiness behavior. It does not weaken source-of-truth, readiness-gate, hard-blocker, destructive-change, authorization, or sensitive-area rules.

## Core invariant

LEAP agents must avoid both confident guessing and unnecessary clarification loops.

Before asking a question, determine whether different plausible answers would materially change the work.

A question is material only when the answer could change one or more of the following:

- architecture or repository structure
- implementation strategy
- scope or acceptance criteria
- risk assessment
- source-of-truth hierarchy
- compatibility or dependency behavior
- validation strategy
- user-facing recommendation or gate decision
- irreversible or hard-to-reverse changes
- authorization or ownership boundaries

If the missing information would only affect naming, wording, formatting, ordering, tone, minor preference, or polish, do not ask. Make a reasonable assumption when needed and proceed.

Plain-English rule:

- If the answer changes the work, classify it as material.
- If the answer is discoverable, inspect first.
- If the answer only changes polish, assume or defer and proceed.
- If the missing answer creates a hard blocker, stop.
- Ask only when an unresolved material question is the safe route for the current clarification mode.

The expected result of Materiality Gate is often zero questions.

## Decision model

Use this flow for materially consequential LEAP work:

```text
INSPECT
  ↓
CLASSIFY
  ↓
ASK / ASSUME / STOP
  ↓
RE-EVALUATE
```

### INSPECT

Inspect available authoritative evidence before asking the user, including repository state, canonical docs, contracts, schemas, tests, active decisions, branch or PR state, and approved tooling.

Do not ask the user for information that LEAP can directly verify from an approved source.

### CLASSIFY

Classify each unresolved item as one of:

```text
Material - plausible answers would materially change the work, risk, or decision.
Non-material - plausible answers would only refine style, naming, wording, formatting, ordering, or polish.
Discoverable - the answer should be inspected from available sources before asking.
Safe assumption - the answer can be reasonably assumed and disclosed without creating a hard blocker.
Hard blocker - proceeding would require unsafe guessing, missing authorization, or violation of a LEAP stop condition.
```

### ASK

Ask only unresolved material questions whose answers are needed for the next safe gate decision.

Batch tightly related questions. Ask no more than three targeted questions at a time unless the user explicitly requests exhaustive discovery.

There is no minimum question count.

### ASSUME

Use a stated assumption when the uncertainty is non-material or safely assumable for the current decision.

A material assumption must be surfaced when changing it later would meaningfully alter architecture, scope, source truth, validation, compatibility, risk, or implementation.

Minor assumptions do not need ceremony.

### STOP

Stop when proceeding would violate a hard blocker or require guessing about matters such as:

- destructive-change permission
- unsafe source-of-truth conflict
- authorization or ownership
- privacy or security boundaries
- money or financial impact
- identity or access control
- legal exposure
- data durability
- user trust
- unapproved Architecture or public-contract changes

STOP is distinct from ASK. A hard stop remains a hard stop even when the user requests fewer clarification questions.

### RE-EVALUATE

After receiving an answer or discovering new evidence, re-run Materiality Gate only for the uncertainty that remains or was newly exposed.

The loop is recursive but bounded:

- continue only while another unresolved material answer could change the next safe decision
- stop asking when remaining items are discoverable, non-material, or safe assumptions
- do not continue discovery merely because more detail could be obtained
- do not impose an arbitrary one-round limit
- do not invent a minimum number of questions

## Clarification modes

Materiality Gate supports two clarification modes.

### Materiality-Gated

This is the default.

```text
Discoverable -> INSPECT
Non-material -> ASSUME or DEFER
Safe assumption -> ASSUME + DISCLOSE when consequential
Material unresolved -> ASK
Hard blocker -> STOP
```

### No Gate

`No Gate` is an explicit per-operation modifier for users who want LEAP to avoid ordinary clarification interruptions and proceed with the strongest reasonable assumptions.

Example:

```text
Run LEAP Recon on this design — No Gate.
```

No Gate changes only the normal ASK path:

```text
Discoverable -> INSPECT
Non-material -> ASSUME or DEFER
Safe assumption -> ASSUME + DISCLOSE when consequential
Material unresolved that is safely assumable -> ASSUME + DISCLOSE
Hard blocker -> STOP
```

In shorthand:

```text
No Gate: ASK -> ASSUME + DISCLOSE, when safe.
No Gate never changes STOP -> PROCEED.
```

No Gate does not bypass:

- hard blockers
- authorization boundaries
- source-of-truth integrity requirements
- destructive-change safeguards
- sensitive-area checkpoints
- security or privacy requirements
- public-contract approval requirements
- required human approval

When No Gate is active, consequential assumptions must be visible in the output so later work can distinguish accepted defaults from verified facts.

No Gate is not a separate LEAP workflow or lifecycle phase.

## Relationship to confidence

LEAP should aim for high confidence before final recommendations, but confidence thresholds must not drive clarification behavior.

Use consequence first:

```text
1. Material consequence
2. Evidence availability
3. Safe assumption
4. Confidence
```

A low-confidence non-material detail should not create a clarification loop. A high-confidence guess about a material architectural fork may still require ASK or STOP.

## Materiality Check output

Charter, Recon, Prompt-generation, or other materially consequential LEAP outputs may include:

```text
## Materiality Check

### Clarification Mode
Materiality-Gated / No Gate

### Material Unknowns
Unresolved facts whose plausible answers could change architecture, scope, risk,
acceptance criteria, source truth, validation, compatibility, recommendation,
or the next gate decision.

### Assumptions Proceeding Under
Reasonable assumptions being used so work can continue.
Mark materially consequential assumptions explicitly.

### Deferred Non-Material Details
Items that may improve polish, naming, formatting, ordering, or preference
alignment but do not change the current decision.

### Stop Conditions / Hard Blockers
Items that require human approval, reconciliation, or another mandatory
checkpoint before proceeding.

### Question Decision
Proceed with assumptions / inspect sources first / ask targeted questions / stop.
```

## Examples

### Non-material unknown

If the user asks for Recon on dependency tracking, do not block on file naming or table formatting.

Acceptable assumption:

```text
Assumption: use a human-readable Markdown dependency register for the first version
unless the repo already contains a machine-readable convention.
```

### Material unknown in default mode

This question is material:

```text
Should dependency tracking be advisory only, or should breaking contract drift block implementation?
```

It changes CI behavior, risk posture, and developer workflow, so the default mode asks.

### Material unknown in No Gate mode

If the same question is safely assumable for a documentation-only proposal, No Gate may proceed with a visible default:

```text
Assumption: dependency tracking remains advisory for this change.
No enforcement or CI blocking is introduced without separate approval.
```

If implementation would actually introduce or remove release blocking, the authorization or public-contract impact may instead require STOP.

### Discoverable unknown

Do not ask whether the repo has a dependency manifest when repo access exists. Inspect the repository first.

## Interaction with hard blockers

Materiality Gate filters clarification. Hard blockers govern whether work is authorized or sufficiently grounded to proceed.

That distinction is intentional:

```text
Materiality Gate: "Do I need information from the user before I can make the next safe decision?"
Hard blocker:     "Am I allowed and grounded enough to perform this action at all?"
```

No Gate can reduce clarification friction. It cannot authorize unsafe or unapproved work.
