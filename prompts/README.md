# LEAP Prompt Library

This directory contains reusable operational Prompts for running LEAP workflows.

The `templates/` directory contains compact request templates. The `prompts/` directory contains fuller operational standards.

## Project-documentation model

LEAP Prompts use this preferred traceability hierarchy:

```text
Mission / Project Charter
        ↓
Strategic Outcome
        ↓
Initiative
        ↓
Delivery Unit
        ↓
Build Unit
```

Roadmaps schedule and prioritize. Domains describe persistent responsibility boundaries. Architecture describes technical structure.

Delivery Unit may be collapsed for small work. Build Unit is not necessarily independently deployable.

LEAP Skills are reusable execution capabilities composed against Build Units. Skills are not planning levels and do not grant authority beyond the governing Prompt.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

Canonical references:

- [`../docs/project-documentation-model.md`](../docs/project-documentation-model.md)
- [`../docs/leap-skills.md`](../docs/leap-skills.md)

## Prompt family routing

| Prompt Type | Use when | File / source |
|---|---|---|
| Charter Prompt | Mission, Strategic Outcomes, Initiative identity, Roadmap, source truth, or Brownfield docs need alignment | [leap-charter-standard.md](leap-charter-standard.md) |
| Recon Prompt | A focused Initiative, Delivery Unit, Build Unit, Domain, Architecture, dependency, contract, risk, or legacy Layer needs investigation | [leap-recon-standard.md](leap-recon-standard.md) |
| Standard Implementation Prompt | A bounded Build Unit or small Delivery Unit is ready for agent instructions | [leap-prompt-standard.md](leap-prompt-standard.md) |
| Fix Prompt | A specific bug or remediation needs bounded implementation guidance | [leap-prompt-standard.md](leap-prompt-standard.md) |
| Refactor Prompt | Structural change needs sequencing, compatibility, verification, and stop conditions | [leap-prompt-standard.md](leap-prompt-standard.md) |
| Governance Prompt | Source-truth, process, or documentation cleanup needs a focused pass | [leap-governance-pass-standard.md](leap-governance-pass-standard.md) |
| Validation Prompt | Completed work needs verification and handoff | [leap-prompt-standard.md](leap-prompt-standard.md) |
| LHS Prompt | A named Initiative or Delivery Unit needs staged multi-Build-Unit execution | [../docs/leap.md](../docs/leap.md) |

Use a [Quick LEAP Brief](../docs/user/quick-leap-brief.md) or Standard Implementation Prompt for low-gravity work.

Use LHS when staged execution, commit boundaries, tests and docs, multi-area coordination, compatibility checks, rollback awareness, or explicit integration checkpoints materially reduce risk.

LEAP LHS stages implementation. It does not define the project's strategic hierarchy.

## Skill composition

Recon performs Capability / Skill Review only after Build Unit boundaries are clear enough.

When Skills are selected, implementation Prompts identify:

```text
| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
```

Use ordinary reasoning and repository guidance when an explicit Skill adds no material value. Use progressive disclosure instead of loading entire skill libraries into every Prompt.

Define reusable Skill contracts with [`../templates/leap-skill-template.md`](../templates/leap-skill-template.md).

## Current public workflow

Current request templates:

```text
templates/leap-charter-template.md
templates/leap-recon-lite-template.md
templates/leap-recon-template.md
templates/leap-prompt-template.md
templates/leap-skill-template.md
```

Start with:

- [Start Here](../docs/00_start_here.md)
- [Project Documentation Model](../docs/project-documentation-model.md)
- [LEAP Skills](../docs/leap-skills.md)
- [Which LEAP Workflow Should I Use?](../docs/user/which-leap-workflow.md)
- [When Not to Use LEAP](../docs/user/when-not-to-use-leap.md)
- [Quick LEAP Brief](../docs/user/quick-leap-brief.md)
- [LEAP Framework](../docs/leap.md)
- [LEAP Charter](../docs/leap-charter.md)
- [Materiality Gate](../docs/materiality-gate.md)
- [Dependency & Contract Recon](../docs/dependency-contract-recon.md)
- [Legacy Project Documentation Migration](../docs/maintainer/project-documentation-migration.md)

## Operational Prompt files

```text
prompts/leap-charter-standard.md
prompts/leap-recon-standard.md
prompts/leap-prompt-standard.md
prompts/leap-governance-pass-standard.md
```

Fix, Refactor, and Validation Prompts are variants of `leap-prompt-standard.md`.

LHS is a Prompt format documented in `docs/leap.md`, not a separate lifecycle phase.

## Usage notes

- Charter establishes or reconciles Mission, Strategic Outcomes, Initiatives, Roadmap, Domains, Architecture, and source truth.
- Recon begins with Baseline Freshness Check and investigates focused uncertainty.
- Recon performs Planning Boundary Review before Delivery Unit or Build Unit generation.
- Recon performs Capability / Skill Review after Build Unit boundaries are clear enough and only when useful.
- Implementation Prompts include strategic and delivery traceability when material.
- Implementation Prompts identify selected Skill sources, loading methods, permission fit, and verification without letting Skills widen scope.
- Roadmap placement must not be treated as permanent Initiative identity.
- Domains and Initiatives are many-to-many.
- Build Units are bounded implementation responsibilities and are not necessarily independently deployable.
- Skills are reusable execution capabilities and are not planning levels.
- Legacy Layer docs must be classified before migration.
- Governance Prompts handle source-truth ownership and documentation drift.
- Validation Prompts verify completed work and record handoff evidence.

## Public rule

```text
Inspect discoverable sources first.
Ask only material questions.
Proceed on stated assumptions for non-material unknowns.
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```
