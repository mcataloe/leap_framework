<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: supporting-adoption-guidance
  authority: supporting
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Which LEAP Workflow Should I Use?

Use the lightest LEAP workflow that controls the actual risk.

Full LEAP is useful when direction, source truth, repo reality, architecture, dependencies, implementation scope, or validation needs discipline. It is not meant to turn every tiny task into a planning exercise.

If the work is small, obvious, and easy to verify, a normal prompt may be enough. If the work is still small but an AI coding agent needs guardrails, use a Quick LEAP Brief.

Engage LEAP when guessing would be more expensive than pausing. If LEAP only adds ceremony, use a lighter workflow.

## Quick chooser

| If this is true | Start with |
| --- | --- |
| The task is tiny, obvious, and easy to verify. | Normal prompt |
| The task is small, source truth is clear, and the repo impact is localized. | [Quick LEAP Brief](quick-leap-brief.md) |
| The project direction is unclear, or docs are stale or conflicting. | [LEAP Charter](../leap-charter.md) |
| A focused feature, risk, layer, dependency, contract, or architecture question needs investigation. | [LEAP Recon](../../templates/leap-recon-lite-template.md) |
| The work is bounded and the agent needs implementation-ready instructions. | [LEAP Prompt](../../templates/leap-prompt-template.md) |
| The work is staged, layered, multi-area, or needs explicit sequencing. | [LEAP LHS](../leap.md) |

Materiality Gate is not a phase. It is LEAP's question filter: inspect discoverable sources first, ask only when the answer changes the work, proceed on safe assumptions for polish-only unknowns, and stop for safety, source-truth, destructive-change, privacy, money, identity, legal exposure, or user-trust risks.

## Codex Plan Mode vs. LEAP Execution Mode

Codex Plan Mode is a user-controlled Codex setting. LEAP Execution Mode is an instruction inside the prompt.

They are related, but not the same thing.

- Use Codex Plan Mode Off for `implement-directly` and `repo-preflight-then-implement`.
- Use Codex Plan Mode On for `plan-first`.
- Use `User decision required` when the user's desired approval gate is the deciding factor.

A LEAP Prompt should make the required Codex Plan Mode setting obvious before the user submits the prompt.

## When Not to Use Full LEAP

Do not use full LEAP just because AI is involved.

Use the lightest workflow that controls the actual risk. Full LEAP is helpful when direction, source truth, repo reality, architecture, dependencies, implementation scope, or validation needs discipline. It is not meant to turn every typo fix into a planning summit.

Do not use full LEAP for:

- typos
- small copy edits
- one-file obvious fixes
- pure brainstorming
- pure writing polish
- small local UI tweaks
- obvious bugs with clear scope
- tasks where extra process would not reduce risk

For small but agent-executed work, use a [Quick LEAP Brief](quick-leap-brief.md).

Use [LEAP Charter](../leap-charter.md), [LEAP Recon](../../templates/leap-recon-lite-template.md), [LEAP Prompt](../../templates/leap-prompt-template.md), or [LEAP LHS](../leap.md) only when the work has enough uncertainty, risk, or implementation gravity to justify the added structure.

For the longer version, see [When Not to Use LEAP](when-not-to-use-leap.md).

## Recommended Same-Thread Workflow

LEAP works best when ideation, clarification, Recon, and prompt generation stay in the same conversation whenever practical.

When the discussion happens in the same thread, you do not need to restate every detail. The prior conversation is part of the working context.

A normal workflow can be:

1. Discuss the feature, risk, bug, or project idea naturally.
2. Ask questions, compare options, and pressure test the idea.
3. When ready, use a short LEAP command.

Examples:

```text
Run LEAP Recon on what we just discussed.
```

```text
Run LEAP Recon on the password reset idea above.
```

```text
Run LEAP Charter on the app idea we just talked through.
```

```text
Generate a LEAP Prompt from the approved Recon above.
```

```text
Turn the Build Unit sequence above into a LEAP LHS prompt.
```

```text
Run LEAP Validation/Handoff on the completed changes above.
```

## When to Add More Detail

Use a longer prompt when:

- starting a new conversation
- the previous discussion is not visible
- you want LEAP to focus on a specific risk
- the repo, branch, file, dependency, or source-truth location needs to be named
- you need to set hard boundaries up front

In the same thread, prefer short commands. LEAP should inspect available context, classify the request, ask only material questions, and avoid making you repeat the framework checklist.

New-thread example:

```text
Run LEAP Recon on password reset for this repo.

Context:
- The app already has login and signup.
- We want users to reset forgotten passwords by email.
- We have not decided token expiration, rate limits, or email template behavior.
```

Optional steering can be short:

```text
Run LEAP Recon on the onboarding improvement idea above, focusing on source-truth gaps and UX risk.
```

## Scenarios

### I have a new app idea.

Use LEAP Charter.

Use it when the user, problem, workflow, MVP, non-goals, risks, source truth, or roadmap are not settled.

Why: Charter turns early intent into a project baseline before any agent starts planning implementation.

Starter phrasing:

```text
Run LEAP Charter on the app idea we just talked through.
```

### My repo has old docs and I do not know what is current.

Use Brownfield LEAP Charter.

Use it when current docs, stale docs, archived docs, repo reality, and source truth need reconciliation.

Why: Brownfield Charter canonicalizes current docs forward, archives stale docs backward, and prevents old plans from competing with current source truth.

Starter phrasing:

```text
Run Brownfield LEAP Charter for this repo.
```

### The project direction is clear, but I need to investigate authentication.

Use LEAP Recon.

Use it when the baseline is good enough, but one focused feature, risk, dependency, contract, layer, or architecture question needs investigation.

Why: Recon checks source truth and repo reality before turning uncertainty into implementation scope.

Starter phrasing:

```text
Run LEAP Recon on authentication.
```

For a shorter starter format, use the [LEAP Recon Lite template](../../templates/leap-recon-lite-template.md).

### I know the exact bounded implementation task.

Use LEAP Prompt.

Use it when scope, source truth, repo reality, constraints, non-goals, validation, stop conditions, and execution profile are clear enough for a coding agent.

Why: LEAP Prompt converts a bounded task into agent-ready instructions.

Starter phrasing:

```text
Generate a LEAP Prompt from the approved Recon above.
```

### This is just a small doc or UI fix.

Use Quick LEAP Brief.

Use it when the change is small, localized, low-risk, and easy to verify.

Why: Quick LEAP Brief keeps the important guardrails without making the process heavier than the work.

Starter phrasing:

```text
Use a Quick LEAP Brief for this small task.
```

If the change is tiny, obvious, and easy to verify, use a normal prompt instead. See [When Not to Use LEAP](when-not-to-use-leap.md).

### This work touches several areas and needs staged commits.

Use LEAP LHS.

Use it when implementation gravity is high: multi-area changes, dependency order, tests and docs, phased commits, rollback risk, architecture/data/workflow changes, or explicit acceptance criteria.

Why: LHS is a structured LEAP Prompt format for staged implementation. It is not a mandatory lifecycle stage.

Starter phrasing:

```text
Turn the Build Unit sequence above into a LEAP LHS prompt.
```
