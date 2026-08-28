<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-reference
  authority: canonical
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# LEAP Skills

LEAP Skills are reusable execution capabilities that a LEAP workflow may select and compose when specialized procedure materially improves quality, safety, consistency, or efficiency.

A Skill answers:

```text
How should an agent competently perform this kind of work?
```

A Build Unit answers:

```text
What bounded implementation responsibility must be delivered and verified?
```

These are different dimensions. Skills do not replace Build Units, Delivery Units, Initiatives, Recon, or LEAP Prompt generation.

## Core boundary

```text
Objective
   ↓
LEAP Recon
   ↓
Workflow / Plan
   ↓
Build Units               WHAT gets delivered
   ↓
Skills                    HOW specialized work is performed
   ↓
Tools / MCP / Shell       WHAT performs actions
   ↓
Verification / Evidence
```

The controlling invariant is:

> A Build Unit defines an independently bounded and verifiable delivery responsibility. A Skill defines reusable capability used to achieve that responsibility. A Skill may shape local execution procedure but may not silently expand scope, authority, product behavior, Architecture, or source-of-truth ownership.

## Skills are not a new lifecycle phase

Do not add a mandatory Skills phase to the LEAP lifecycle.

The lifecycle remains:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Skills are latent capabilities selected only when useful. A tiny obvious task may use no explicit Skill. A complex migration may compose several.

## Portable Skill model

A LEAP Skill is a semantic contract, not a Claude-specific or Codex-specific runtime feature.

A Skill may be supplied as:

- a native agent-skill package such as a `SKILL.md` bundle
- repository-local instructions
- a LEAP-maintained capability document
- a prompt fragment with explicit boundaries
- a script plus a thin instruction contract
- another harness-specific capability that satisfies the same LEAP Skill Contract

A LEAP Prompt must never assume a named Skill exists merely because the agent platform supports skills. When a Skill is required, identify the source and loading method.

## LEAP Skill Contract

A reusable Skill should define at least:

| Field | Requirement |
|---|---|
| Name | Stable, descriptive capability name |
| Purpose | What specialized outcome or procedure the Skill provides |
| Use when | Positive trigger conditions |
| Do not use when | Cases where ordinary reasoning or a simpler procedure is better |
| Inputs | Context, artifacts, repo state, or parameters required |
| Outputs | Artifacts, findings, changes, or evidence produced |
| Preconditions | State that must already be true |
| Scope boundary | What the Skill may and may not change |
| Tool requirements | Tools the procedure may need |
| Permissions | Maximum authority allowed while using the Skill |
| Always | Invariants that must hold |
| Ask first | Decisions that require human approval |
| Never | Hard prohibitions |
| Procedure | Smallest reusable execution flow |
| Verification | Evidence required to claim the Skill succeeded |
| References | Optional detail loaded only when needed |
| Portability notes | Runtime-specific adaptation, if any |

Use [`../templates/leap-skill-template.md`](../templates/leap-skill-template.md) when defining a reusable Skill.

## Authority rule

Capability and authority are separate.

A Skill may request tools, but the governing LEAP Prompt and repository policy decide whether those tools and actions are permitted.

Use the narrower authority when Skill and Prompt differ.

Examples:

- a security-review Skill may inspect deployment configuration without gaining permission to deploy
- a migration Skill may recommend destructive cleanup without gaining permission to delete data
- a code-review Skill may identify a public-contract problem without gaining permission to change the contract

A Skill must not weaken LEAP stop conditions, repository instructions, user approvals, or system/tool policy.

## Progressive disclosure

Keep the Skill core small enough to select and reason about cheaply.

The core should contain:

- triggers
- boundaries
- required decisions
- procedure
- verification

Move deep platform guidance, long examples, scripts, variant-specific rules, and reference tables into linked supporting files. Load only the references needed for the current Build Unit.

Do not load an entire skill library into every Prompt.

## Recon capability review

Recon should perform a Capability / Skill Review after Build Unit boundaries are clear enough.

For each Build Unit, determine:

1. whether ordinary agent reasoning and repository guidance are sufficient
2. whether a reusable Skill materially reduces ambiguity, repetition, risk, or specialized-domain error
3. whether a matching Skill already exists
4. where the Skill comes from and how the agent will load it
5. whether its tool requirements fit the Prompt permissions
6. what Skill-specific verification is required
7. whether a missing Skill is material enough to block Prompt generation

A Skill should not be introduced merely because one exists.

## Prompt composition

When Skills are used, the generated LEAP Prompt should identify them explicitly without duplicating the full Skill body.

Recommended composition table:

```text
| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
|---|---|---|---|---|---|---|
```

Rules:

- Build Unit scope remains authoritative
- Prompt constraints remain authoritative
- Skill authority cannot exceed Prompt authority
- required Skill sources must be resolvable before execution
- optional Skills may be omitted when ordinary execution remains safe
- do not inline large Skill references unless the target agent cannot load them otherwise
- do not let a Skill reorder unrelated Build Units or invent new delivery scope

## Skill verification

A Skill is not successful merely because its procedure ran.

Verification should be capability-specific and evidence-bearing, for example:

- dependency tracing identifies all required call sites and reports unresolved uncertainty
- destructive cutover proves both target-state presence and legacy-state absence
- security review records checks performed and unresolved findings
- code review reports findings against the governing Build Unit and acceptance criteria
- migration validates resulting state and required rollback posture

Verification evidence belongs in Validation/Handoff when the Skill affects completion confidence.

## Skill selection failure modes

LEAP should guard against:

- treating Skills as another mandatory ceremony
- using a Skill because it exists rather than because it helps
- allowing a Skill to broaden a Build Unit
- assuming a harness has a Skill without identifying its source
- letting Skill tool requirements silently widen permissions
- loading large reference bundles unnecessarily
- duplicating the same procedure in many generated Prompts instead of reusing a stable contract
- treating a runtime-specific skill format as the LEAP abstraction itself

## Initial scope

The first-class Skill abstraction establishes:

- the Skill / Build Unit boundary
- a portable Skill Contract
- Recon capability selection
- Prompt composition
- progressive disclosure
- tool and authority boundaries
- Skill-specific verification

The following are deliberately deferred until enough real Skill usage exists to justify them:

- a mandatory global Skill registry
- automated Skill discovery infrastructure
- autonomous framework self-modification
- automatic promotion of repeated corrections into framework rules
- a new persisted continuity store solely for Skills

Add these only when evidence shows they materially improve LEAP rather than add process weight.
