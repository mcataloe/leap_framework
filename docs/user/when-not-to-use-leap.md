<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: supporting-adoption-guidance
  authority: supporting
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# When Not to Use LEAP

LEAP is a risk-control framework, not a ceremony requirement.

Use the lightest workflow that controls the actual risk. Do not use full LEAP just because AI is involved.

Engage LEAP when guessing would be more expensive than pausing. If the result is already obvious and easy to verify, use a normal prompt or a Quick LEAP Brief instead.

## Do Not Use Full LEAP For

- typos
- small copy edits
- one-file obvious fixes
- pure brainstorming
- pure writing polish
- small local UI tweaks
- obvious bugs with clear scope
- tasks where extra process would not reduce risk

## Use a Normal Prompt When

You already know exactly what needs to change, the change is small, and the result is easy to verify.

Examples:

- "Fix this typo."
- "Change this heading from X to Y."
- "Update this link."
- "Apply the same existing wording pattern here."

## Use a Quick LEAP Brief When

The task is still small, but an AI coding agent needs guardrails.

Examples:

- a small UI fix
- a localized backend change
- a narrow refactor
- a simple test addition
- a low-risk documentation update

Use the [Quick LEAP Brief](quick-leap-brief.md) when the work needs scope, source-truth, verification, and stop-condition guardrails without full Charter or Recon.

## Use LEAP Recon When

A focused feature, risk, dependency, contract, architecture question, or repo-reality question needs investigation before implementation.

Use [LEAP Recon Lite](../../templates/leap-recon-lite-template.md) when the Recon request is focused and the full Recon template is heavier than the question.

## Use LEAP Charter When

Project direction, source truth, documentation, roadmap, or baseline assumptions need to be established or reconciled.

Use [LEAP Charter](../leap-charter.md) when guessing would be more expensive than pausing.

## Use LEAP Prompt When

The implementation scope is bounded and the coding agent needs clear instructions, constraints, acceptance criteria, validation, and stop conditions.

Use the [LEAP Prompt template](../../templates/leap-prompt-template.md) after source truth, repo reality, and scope are clear enough for implementation.

## Use LEAP LHS When

The work is staged, layered, multi-area, or has enough implementation gravity to require sequencing.

Examples:

- multiple system areas
- dependency order
- phased commits
- rollback risk
- architecture changes
- data contract changes
- user workflow changes
- tests and docs required

LEAP LHS is a structured LEAP Prompt format. It is not a mandatory lifecycle stage.

## Core Rule

If LEAP reduces risk, use it.

If LEAP only adds ceremony, do not.

For side-by-side workflow selection, use [Which LEAP Workflow Should I Use?](which-leap-workflow.md). For small agent-executed work, use the [Quick LEAP Brief](quick-leap-brief.md).
