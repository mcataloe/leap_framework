<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-reference
  authority: canonical
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# LEAP Execution Routing

LEAP routes work by required capability and confidence, then optimizes among adequate execution surfaces for total delivery cost.

The canonical rule is:

> Route work to the least-cost available execution surface capable of satisfying the work unit's required confidence and validation criteria, escalating capabilities only when necessary.

Provider-specific products, quotas, subscriptions, and credit systems are runtime configuration, not framework architecture.

## 1. Why execution routing exists

Reasoning difficulty, execution capability, environment access, and marginal cost are separate concerns.

A difficult Architecture decision may require high reasoning but no runtime-capable agent. A simple migration may require little reasoning but still require a shell, database, or deployment environment before it can be verified.

LEAP therefore does not map "hard problem" directly to "more expensive execution surface."

Instead:

```text
Required confidence
  -> validation requirements
    -> required capabilities
      -> eligible execution surfaces
        -> lowest expected total cost among eligible surfaces
```

Total cost may include constrained credits, compute or license cost, human time, handoff overhead, expected retries, and failure risk.

Cost optimization never lowers the Definition of Done.

## 2. Execution Environment Profile

During project onboarding, record the available execution surfaces and their relevant characteristics.

The profile may be lightweight and may live in Project Instructions, repository guidance, a project setup document, or equivalent source truth.

Recommended fields:

| Field | Meaning |
|---|---|
| Surface | Product, tool, agent, or environment |
| Capabilities | Repository mutation, shell/runtime, browser/UI, external-app access, deployment, etc. |
| Context reach | What project/repository/environment state the surface can actually inspect |
| Relative marginal cost | Free/included, constrained credits, metered, human-intensive, or other local classification |
| Usage constraints | Quotas, concurrency, time limits, plan limits, or organizational policy |
| Permission ceiling | Maximum authority available on that surface |
| Preferred use | Work types where the surface is normally economical |
| Escalation trigger | Capability or confidence requirement that should move work elsewhere |

The profile is configuration. It may change without changing LEAP doctrine.

## 3. Capability classes

LEAP may describe execution needs using the following classes.

| Class | Name | Typical capability |
|---|---|---|
| E0 | Reasoning | Analysis, Recon, Architecture, decomposition, research, specifications |
| E1 | Remote Mutation | Bounded repository/document/config mutation without proving runtime behavior |
| E2 | Execution Environment | Shell/runtime, build, lint, test, migration, dependency resolution, iterative repair |
| E3 | Agentic Environment | Browser, desktop, SaaS, or multi-application interaction |
| E4 | Human Gate | Human authority, judgment, credential use, destructive approval, or irreversible decisions |

These are capability classes, not intelligence rankings.

Recording a capability class is optional. Record it only when work crosses surfaces or the routing choice is not obvious.

A work unit may use more than one class across its lifecycle. Prefer the lowest adequate class for each coherent tranche of work rather than bouncing between surfaces after every file.

## 4. Build Unit and Delivery Unit routing metadata

When execution routing is materially relevant, a Build Unit or Delivery Unit may record:

```text
Required capabilities:
Required confidence:
Required validation:
Preferred execution surface:
Escalation surface:
Human gate, if any:
Verification state:
```

Do not require this metadata for trivial work where the routing choice is obvious and low-risk.

Execution routing does not add a new planning level. Build Units still define bounded delivery responsibility.

## 5. Implementation state versus verification state

LEAP distinguishes implementation from execution-grounded verification.

Recommended state language:

- **Implemented — execution unverified**: the intended artifacts were changed, but required runtime/build/integration checks have not been executed.
- **Execution verified**: the required execution-grounded checks were run successfully in an adequate environment.
- **Partially verified**: some required checks passed, while named checks remain unavailable, blocked, or pending.
- **Failed**: a required check ran and failed, or validation found an unexplained out-of-scope change or hard-stop violation.

[LEAP Validation](../prompts/leap-validation-standard.md) is the standard for reporting these states at handoff.

Never report "complete" when the Definition of Done requires checks that were not executed.

Static review, reasoning, or repository inspection may support confidence, but they do not substitute for an explicitly required runtime check.

## 6. Routing policy

For each coherent work tranche:

1. identify the required outcome and confidence
2. identify the validation needed to claim completion
3. derive required capabilities from that validation
4. eliminate surfaces that cannot provide those capabilities or permissions
5. choose the lowest expected total-cost eligible surface
6. complete as much coherent work as practical before crossing surfaces
7. escalate when a capability, confidence, or authority requirement cannot be satisfied
8. record checks not run and the resulting verification state

Do not escalate merely because implementation work exists. Repository mutation alone does not imply that a shell-capable agent is required.

Do not remain on a cheaper surface when required validation cannot be performed there.

## 7. Handoff between surfaces

A handoff should preserve enough context that the next surface can prove or repair the work without repeating unnecessary analysis.

Recommended handoff content:

```text
Objective:
Build Unit / Delivery Unit:
Changes already made:
Source truth:
Required capabilities:
Required validation:
Checks already completed:
Checks not yet run:
Known risks:
Stop conditions:
Expected completion evidence:
```

When moving from E0/E1 to E2, prefer a bounded validation-and-repair handoff over re-running the entire design process.

## 8. Current-provider profiles

Provider-specific guidance belongs in the Execution Environment Profile, not in this doctrine. One environment may treat conversational repository mutation as cheap and shell-capable agents as constrained; another may price both the same. Route differently without changing this document.

A profile describes what a tool can do. An **execution role** (architect, implementor, reviewer, human approver) describes who is responsible for planning, bounded implementation, independent review, and required approval; see [Agent Execution Roles and Handoffs](agent-execution-roles.md). Roles are optional assignments within the existing lifecycle, not new agent types or required sessions.

A per-tool profile is optional. Write one only when a team uses a tool often enough that its quirks change how Prompts should be written. Useful fields: strengths, known failure modes, required constraints, validation commands, and commit behavior.

Adjust handoffs to the tool's behavior:

| Agent behavior | LEAP adjustment |
|---|---|
| Weak repo awareness | Strong source list, file list, and inspect-first instructions |
| Strong autonomous editing | Tight non-goals and forbidden-file list |
| Shell access | Explicit validation commands and permission limits |
| Chat-only | Generate a plan or Prompt only |
| Fast but shallow | Smaller Build Units and explicit acceptance criteria |
| Strong refactoring tendency | Block broad cleanup unless scoped and testable |
| Weak test discipline | Require exact verification and evidence |
| Multi-repository access | Explicit ownership, contract, merge-order, and rollback boundaries |

Example profiles (optional — omit when not needed):

```text
Codex
- Plan Mode: a user-controlled setting. Off for implement-directly,
  repo-preflight-then-implement, and validation-only; On for plan-first;
  user decision for recon-only. LEAP Execution Mode is an instruction
  inside the Prompt; Plan Mode is a tool setting.
- Strengths: bounded multi-file Build Units when source truth is clear;
  test-driven edits when verification is explicit.
- Known failure modes: over-completing broad Prompts; touching adjacent
  files when boundaries are vague; treating missing decisions as
  implementation choices.
- Constraints: name files not to touch, validation commands, and stop
  conditions for conflicts, missing files, and unapproved Architecture changes.
- Commit behavior: one Build Unit or task per commit where feasible.

Claude Code
- Plan Mode: a user-controlled setting that plans before editing; use it
  for plan-first work.
- Repository guidance: reads AGENTS.md when the repository has no
  CLAUDE.md; otherwise add an @AGENTS.md import to CLAUDE.md. Use
  permission rules or PreToolUse hooks to enforce do-not-touch paths.
- Constraints and commit behavior: same as above; state permissions and
  validation commands explicitly.
```

## 9. Failure modes to avoid

LEAP should guard against:

- selecting an expensive agent merely because a task is complex
- selecting a cheap surface that cannot satisfy required validation
- treating repository mutation as equivalent to execution verification
- claiming tests passed when they were not run
- excessive surface switching that creates handoff overhead
- hard-coding current vendor pricing into framework doctrine
- using cost savings to justify weaker acceptance criteria
- ignoring human time and retry risk when calculating practical cost

## 10. Relationship to Agent Execution Configuration

Agent Execution Configuration remains the explicit handoff block in an agent-ready Prompt.

When routing is material, for example when work crosses surfaces, it may also capture these optional fields (omit when not needed):

```text
Required Capability Class:
Required Capabilities:
Required Confidence / Validation:
Preferred Surface:
Escalation Surface:
Verification State at Handoff:
```

The selected Agent / Tool is an execution decision derived from requirements, not an assumption made before requirements are known.

## 11. Optional native multi-agent delegation

For independently bounded work, see [Native Multi-Agent Delegation Policy](native-agent-delegation.md). It adds dependency, ownership, model and effort selection, and integration rules to surface routing; it does not change the lifecycle, permissions, or Definition of Done.
