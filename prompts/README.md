# LEAP Prompt Library

This directory contains reusable operational prompts for running LEAP workflows.

The `templates/` directory contains compact request templates. The `prompts/` directory contains fuller copy-ready operational prompts for recurring work.

## Prompt Family Routing

LEAP Prompt is the broad category of Codex-ready or agent-ready instruction artifacts generated from Charter, Recon, user intent, or approved implementation scope.

Some prompt types have dedicated operational files. Others are prompt variants handled by the standard implementation prompt.

| Prompt Type | Use When | File / Source |
| --- | --- | --- |
| Charter Prompt | Project direction, source truth, roadmap, baseline, or brownfield docs need alignment. | [leap-charter-standard.md](leap-charter-standard.md) |
| Recon Prompt | A focused risk, feature, layer, dependency, contract, repo-reality, or architecture question needs investigation. | [leap-recon-standard.md](leap-recon-standard.md) |
| Standard Implementation Prompt | The task is bounded and ready for coding-agent instructions. | [leap-prompt-standard.md](leap-prompt-standard.md) |
| Fix Prompt | A specific bug or remediation needs bounded implementation guidance. | [leap-prompt-standard.md](leap-prompt-standard.md), as a Fix Prompt variant |
| Refactor Prompt | Structural change needs constraints, sequencing, verification, and stop conditions. | [leap-prompt-standard.md](leap-prompt-standard.md), as a Refactor Prompt variant |
| Governance Prompt | Repo/process/source-truth cleanup needs a focused governance pass. | [leap-governance-pass-standard.md](leap-governance-pass-standard.md) |
| Validation Prompt | Completed work needs verification and handoff. | [leap-prompt-standard.md](leap-prompt-standard.md), as a Validation Prompt variant |
| LHS Prompt | Staged implementation needs House Standard-style sequencing. | [../docs/leap.md](../docs/leap.md), as the Layered House Standard prompt format |

Use a [Quick LEAP Brief](../docs/user/quick-leap-brief.md) or a standard implementation prompt for low-gravity work.

Use LHS when implementation gravity is high enough to need staged execution, commit boundaries, tests and docs, multi-area coordination, compatibility checks, rollback awareness, or explicit acceptance criteria.

## Current Public Workflow

Use the current top-level templates:

```text
templates/leap-charter-template.md
templates/leap-recon-lite-template.md
templates/leap-recon-template.md
templates/leap-prompt-template.md
```

Use the current user and reference docs first when onboarding or choosing a workflow:

- [Start Here](../docs/00_start_here.md)
- [Which LEAP Workflow Should I Use?](../docs/user/which-leap-workflow.md)
- [When Not to Use LEAP](../docs/user/when-not-to-use-leap.md)
- [Quick LEAP Brief](../docs/user/quick-leap-brief.md)
- [LEAP Framework](../docs/leap.md)
- [LEAP Charter](../docs/leap-charter.md)
- [Materiality Gate](../docs/materiality-gate.md)
- [Dependency & Contract Recon](../docs/dependency-contract-recon.md)

## Operational Prompt Files

The active prompt library uses these canonical root-level files under `prompts/`:

```text
prompts/leap-charter-standard.md
prompts/leap-recon-standard.md
prompts/leap-prompt-standard.md
prompts/leap-governance-pass-standard.md
```

Prompt variants such as Fix Prompt, Refactor Prompt, and Validation Prompt are currently handled by `prompts/leap-prompt-standard.md`.

LHS Prompt is not a separate lifecycle phase or standalone prompt file. It is the Layered House Standard prompt format documented in `docs/leap.md`.

## Usage Notes

- Charter prompts establish or reconcile project direction and source truth before implementation depends on them.
- Recon prompts investigate focused uncertainty before generating implementation prompts.
- Implementation prompts must include scope, non-goals, constraints, validation, stop conditions, and explicit agent execution configuration.
- Fix prompts are bounded implementation prompts for known bugs or remediation work.
- Refactor prompts are bounded implementation prompts for structural changes where sequencing, verification, and rollback awareness matter.
- Governance prompts are for reconciliation, drift review, source-truth ownership cleanup, and prompt-standard cleanup outside normal implementation work.
- Validation prompts verify completed work, summarize evidence, and identify handoff or follow-up needs.
- LHS is a structured LEAP Prompt format, not a mandatory lifecycle phase.

Supporting doctrine lives in the canonical reference docs instead of this routing file:

- [LEAP lifecycle and LHS usage](../docs/leap.md)
- [Materiality Gate](../docs/materiality-gate.md)
- [Dependency & Contract Recon](../docs/dependency-contract-recon.md)
- [Agent profiles](../docs/agent-profiles.md)
- [Risk taxonomy](../docs/risk-taxonomy.md)

## Public Rule

```text
Ask only material questions.
Inspect discoverable sources first.
Proceed on stated assumptions for non-material unknowns.
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```
