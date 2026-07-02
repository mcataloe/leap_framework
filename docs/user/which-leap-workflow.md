# Which LEAP Workflow Should I Use?

Use the lightest workflow that controls the actual risk.

## Quick chooser

| Situation | Start with |
|---|---|
| Tiny, obvious, easy-to-verify task | Normal prompt |
| Small localized coding-agent task | [Quick LEAP Brief](quick-leap-brief.md) |
| Mission, Strategic Outcomes, Initiative identity, Roadmap, or source truth is unclear | [LEAP Charter](../leap-charter.md) |
| A focused Initiative, Delivery Unit, Build Unit, Domain, Architecture area, dependency, contract, risk, or legacy Layer needs investigation | [LEAP Recon](../../templates/leap-recon-lite-template.md) |
| A bounded Build Unit or task is implementation-ready | [LEAP Prompt](../../templates/leap-prompt-template.md) |
| A named Initiative or Delivery Unit needs staged multi-Build-Unit execution | [LEAP LHS](../leap.md) |

## Project-documentation model

```text
Mission / Project Charter
  -> Strategic Outcome
    -> Initiative
      -> Delivery Unit
        -> Build Unit
```

Roadmap schedules and prioritizes. Domains describe persistent responsibility boundaries. Architecture describes technical structure.

Delivery Unit may be collapsed for small work. Build Unit is not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level. See [Project Documentation Model](../project-documentation-model.md) and [Project Documentation Migration](../maintainer/project-documentation-migration.md).

## Materiality Gate

Before asking questions:

- inspect discoverable evidence
- ask only when the answer changes direction, scope, Architecture, risk, source truth, validation, acceptance, or compatibility
- proceed on stated assumptions for non-material unknowns
- stop for safety, destructive changes, privacy, money, identity, legal exposure, user trust, or unsafe source truth

## Codex Plan Mode and LEAP Execution Mode

- Plan Mode Off: `implement-directly` or `repo-preflight-then-implement`
- Plan Mode On: `plan-first`
- User decision required: approval posture is the deciding factor

## Same-thread commands

```text
Run LEAP Charter on the project above.
Run LEAP Recon on the Initiative or feature above.
Generate a LEAP Prompt from the approved Recon.
Turn the Delivery Unit and Build Unit sequence into an LHS Prompt.
Run LEAP Validation/Handoff on the completed changes.
```

## When to use Charter

Use Charter when Mission, users, problem, workflow, MVP, Strategic Outcomes, Initiative identity, Roadmap, Domains, Architecture, non-goals, risks, or source truth are unsettled.

Use Brownfield Charter when current, stale, archived, duplicate, or conflicting docs need reconciliation.

Brownfield Charter classifies a legacy Layer as Initiative, Delivery Unit, Build Unit, Domain, Architecture Layer, Phase, or Needs Reconciliation before migration.

## When to use Recon

Use Recon when the baseline is good enough but one focused target needs source-truth, repo-reality, risk, dependency, planning-boundary, or implementation-safety analysis.

Recon begins with Baseline Freshness Check. Charter is not required before every Recon.

## When to use LEAP Prompt

Use Prompt when source truth, Initiative ownership, Delivery Unit or collapse rationale, Build Unit scope, constraints, validation, stop conditions, and execution profile are clear.

## When to use Quick LEAP Brief

Use Quick Brief for a small, localized, low-risk task. Reduced strategic traceability is acceptable when broader context is not material.

## When to use LHS

Use LHS for staged work with several Build Units, dependency order, tests and docs, phased commits, rollback or compatibility risk, cross-area changes, or cross-repository coordination.

LEAP LHS stages implementation. It does not define the project's strategic hierarchy.

## Final rule

```text
If guessing is more expensive than pausing, use LEAP.
If LEAP adds more ceremony than risk control, use a lighter workflow.
```
