# LEAP Prompt Library

Operational standards for running LEAP workflows. The compact request templates live in [`../templates/`](../templates/). Commands, aliases, and choosing a workflow are covered in [semantic routing](../docs/semantic-routing.md) and the [workflow chooser](../docs/user/which-leap-workflow.md).

Every Prompt inherits [LEAP Core](../docs/leap-core.md): inspect first, order of truth, scope, hard stops, and honest verification. Prompts do not restate it.

## Prompt family

| Prompt type | Use when | Standard | Template |
|---|---|---|---|
| Charter | Direction, source truth, or documentation structure needs to be established or reconciled | [leap-charter-standard.md](leap-charter-standard.md) | [Charter](../templates/leap-charter-template.md) |
| Recon | A focused target needs evidence, risk, dependency, and readiness analysis | [leap-recon-standard.md](leap-recon-standard.md) | [Recon](../templates/leap-recon-template.md), [Recon Lite](../templates/leap-recon-lite-template.md) |
| Standard Implementation, Fix, Refactor | Bounded work is ready for agent instructions | [leap-prompt-standard.md](leap-prompt-standard.md) | [Prompt](../templates/leap-prompt-template.md) |
| LHS | Several Build Units with dependency order, checkpoints, or rollback risk | [leap-prompt-standard.md](leap-prompt-standard.md) + [LHS stage format](../docs/leap-lhs.md) | [Prompt](../templates/leap-prompt-template.md) |
| Governance | Source-truth, process, or documentation drift needs reconciliation | [leap-governance-pass-standard.md](leap-governance-pass-standard.md) | |
| Cleanup | Obsolete artifacts need a dependency-aware decommission proposal | [leap-cleanup-standard.md](leap-cleanup-standard.md) | [Cleanup](../templates/leap-cleanup-template.md) |
| Validation | Finished work needs a scope check, verification state, and handoff | [leap-validation-standard.md](leap-validation-standard.md) | [Pull request](../templates/leap-pull-request-template.md) |

For low-gravity work, use a [Quick LEAP Brief](../docs/user/quick-leap-brief.md) instead of a full Prompt.

## Notes

- Traceability: link the work item. Use the [project documentation model](../docs/project-documentation-model.md) only when the project already uses it.
- Skills: Recon may run a Capability / Skill Review once Build Unit boundaries are clear. Prompts that use Skills name the source, loading method, permission fit, and verification. A Skill never widens Prompt scope. See [LEAP Skills](../docs/leap-skills.md) and the [Skill template](../templates/leap-skill-template.md).
- Cleanup runs are discovery-only until the exact decommission set is approved. Approved work runs as a Refactor Prompt.
- Legacy `Layer` docs are classified before migration: [Project Documentation Migration](../docs/maintainer/project-documentation-migration.md).
