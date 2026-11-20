# Which LEAP Workflow Should I Use?

Use the lightest workflow that controls the actual risk. LEAP is risk control, not a ceremony requirement; a coding agent being involved is not by itself a reason to use it.

## Quick chooser

| Situation | Start with |
|---|---|
| Typo, copy edit, obvious one-file fix, pure brainstorming | A normal prompt. No LEAP. |
| Small, localized task an agent will run | [Quick LEAP Brief](quick-leap-brief.md) |
| Understand a domain, its actors, and workflows before choosing a solution | [LEAP Discovery](leap-discovery.md) |
| Challenge a proposed approach | [LEAP Pressure Test](leap-discovery.md#leap-pressure-test-non-mutating-by-default) |
| One focused question about repo reality, a risk, a dependency, or a design | [LEAP Recon Lite](../../templates/leap-recon-lite-template.md) |
| A larger target needs evidence, scope, and Build Units before implementation | [LEAP Recon](../../prompts/leap-recon-standard.md) |
| Direction, source truth, or documentation structure is unclear or conflicting | [LEAP Charter](../leap-charter.md) |
| Obsolete artifacts need an exact, dependency-aware decommission proposal | [LEAP Cleanup](../repository-cleanup.md) |
| Bounded, implementation-ready work for an agent | [LEAP Prompt](../../templates/leap-prompt-template.md) |
| Several Build Units with dependency order, phased commits, or rollback risk | [LEAP LHS](../leap-lhs.md) |
| Work is finished or being handed off | [LEAP Validation](../../prompts/leap-validation-standard.md) |

Say **LEAP help** for the command list. [Semantic routing](../semantic-routing.md) covers aliases and intent rules.

## Same-thread commands

```text
Run LEAP Recon on the feature above.
Run LEAP Charter on the project above.
Run LEAP Cleanup on the obsolete artifacts above.
Generate a LEAP Prompt from the approved Recon.
Turn the approved Build Units into an LHS Prompt.
Run LEAP Validation on the completed changes.
```

Add **No Gate** to any request to have LEAP proceed on disclosed safe assumptions instead of asking. It never overrides a hard stop. See [Materiality Gate](../materiality-gate.md).

## Notes per workflow

- **Charter:** use it when the mission, users, MVP, non-goals, source truth, or (for teams that use them) Strategic Outcomes, Initiatives, Roadmap, and Domains are unsettled. Brownfield Charter reconciles current, stale, and conflicting docs. It is not required before every Recon.
- **Recon:** use it when the baseline is good enough but one target needs evidence. It starts with a Baseline Freshness Check and stops investigating once the next safe decision is clear.
- **Cleanup:** an unqualified run is discovery-only. It returns an exact proposed decommission set and stops for approval.
- **LEAP Prompt:** use it when source truth, scope, constraints, validation, and stop conditions are clear. Traceability to a work item is enough unless the project uses the full [planning model](../project-documentation-model.md).
- **Quick Brief:** reduced traceability is fine when broader context does not change the work.
- **LHS:** stages execution. It does not define the project's strategic hierarchy.

## Final rule

```text
If guessing is more expensive than pausing, use LEAP.
If LEAP adds more ceremony than risk control, use a lighter workflow.
```
