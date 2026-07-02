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

Use the lightest workflow that controls the actual risk. Do not use full LEAP merely because a coding agent is involved.

## Do not use full LEAP for

- typos
- small copy edits
- one-file obvious fixes
- pure brainstorming
- pure writing polish
- small local UI tweaks
- obvious bugs with clear scope
- work where extra process would not reduce risk

## Use a normal prompt when

You know exactly what needs to change, the change is small, and the result is easy to verify.

## Use a Quick LEAP Brief when

The task is still small but an agent needs scope, source-truth, validation, and stop-condition guardrails.

Examples:

- small UI fix
- localized backend change
- narrow refactor
- simple test addition
- low-risk documentation update

A small Brief may use reduced strategic traceability when Mission, Strategic Outcome, Initiative, Domain, and Architecture context are not material.

## Use Recon when

A focused Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, risk, dependency, contract, legacy Layer, or repository-reality question needs investigation.

Use [LEAP Recon Lite](../../templates/leap-recon-lite-template.md) when the full Recon template is heavier than the question.

## Use Charter when

Mission, Strategic Outcomes, Initiative identity, Roadmap, Domains, Architecture, source truth, documentation, or baseline assumptions need to be established or reconciled.

Use [LEAP Charter](../leap-charter.md) when guessing would be more expensive than pausing.

## Use LEAP Prompt when

The implementation scope is bounded and the agent needs clear traceability, instructions, constraints, acceptance criteria, validation, and stop conditions.

Use the [LEAP Prompt template](../../templates/leap-prompt-template.md) after source truth, repo reality, and scope are clear enough.

## Use LHS when

A named Initiative or Delivery Unit needs staged multi-Build-Unit execution.

Examples:

- several system or documentation areas
- dependency order
- phased commits
- rollback or compatibility risk
- Architecture or data-contract changes
- cross-repository coordination
- tests and docs required

LEAP LHS is a structured Prompt format. It is not a lifecycle stage and it does not define the strategic hierarchy.

## Documentation-model rule

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Roadmap schedules. Domains organize persistent responsibility. Architecture organizes technical structure.

Delivery Unit may collapse for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level.

## Core rule

```text
If LEAP reduces risk, use it.
If LEAP only adds ceremony, do not.
```

For side-by-side selection, use [Which LEAP Workflow Should I Use?](which-leap-workflow.md).
