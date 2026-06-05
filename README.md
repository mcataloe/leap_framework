# LEAP Framework

**LEAP - Layered Execution & Alignment Protocol** is a software delivery framework for turning rough intent into pressure-tested direction, source-grounded plans, and safe, bounded, implementation-ready AI coding-agent handoffs.

LEAP started as a practical response to AI-assisted software delivery: coding agents can move quickly, but speed is only useful when the idea is clear, the source truth is current, the repo reality is understood, and the implementation task is bounded.

The active repository presents the current canonical LEAP framework document and current operational prompts without versioned filenames. Older version detail is intentionally kept out of active docs unless it applies to the current framework; use Git history, release notes, and release tags for older context.

LEAP AGENTS.md templates are distributed from the dedicated [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) repository. The Agent Pack owns the Codex/AGENTS.md execution adapter so downstream projects can pin stable agent instructions independently from LEAP Framework methodology updates.

## Basic Setup

1. Add LEAP to [ChatGPT Project Instructions](INSERT LINK HERE).
2. Put (AGENTS.md)[INSERT LINK HERE] in your GitHub project root.
3. Run the [population prompt](INSERT LINK HERE) in Codex.
4. Ask ChatGPT:

> Run LEAP Recon on {{what you want to build or understand}}.

## LEAP in 60 seconds

LEAP helps turn rough software intent into a safe coding-agent handoff.

It does this by helping you:

1. Clarify the project.
2. Inspect what is already true.
3. Separate facts from assumptions.
4. Bound the work.
5. Tell the agent what to do, what not to touch, and when to stop.
6. Validate the result.

Use the lightest LEAP workflow that controls the actual risk. Small, clear work does not need the full framework.

## Which LEAP workflow should I use?

| Use this                                            | When                                                                                                                                                  |
| --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| Normal prompt                                       | The task is tiny, obvious, and easy to verify.                                                                                                        |
| [Quick LEAP Brief](docs/user/quick-leap-brief.md)   | The task is small, source truth is clear, repo impact is localized, and one Build Unit or less is involved.                                           |
| [LEAP Charter](docs/leap-charter.md)                | Project direction is unclear, docs are stale or conflicting, a greenfield idea needs shaping, or a brownfield repo needs source-truth reconciliation. |
| [LEAP Recon](templates/leap-recon-lite-template.md) | The baseline is good enough, but a focused feature, risk, layer, dependency, contract, or architecture question needs investigation.                  |
| [LEAP Prompt](templates/leap-prompt-template.md)    | The work is bounded, repo reality is understood, source truth is clear, and the coding agent needs implementation-ready instructions.                 |
| [LEAP LHS](docs/leap.md)                            | Implementation gravity is high: staged, layered, multi-area work where tests, docs, rollback, sequence, or commit boundaries matter.                  |

For scenario examples and starter phrasing, see [`docs/user/which-leap-workflow.md`](docs/user/which-leap-workflow.md). For a shorter Recon request, use [`templates/leap-recon-lite-template.md`](templates/leap-recon-lite-template.md).

For tiny, obvious tasks where full LEAP would not reduce risk, see [`docs/user/when-not-to-use-leap.md`](docs/user/when-not-to-use-leap.md).

## Core idea

```text
People often begin with a feeling for what they want built.
LEAP turns that feeling into a testable delivery path.

LEAP Charter establishes or reconciles project direction, source-of-truth docs, roadmap, baseline assumptions, and implementation posture.
LEAP Recon investigates a focused area, gap, risk, feature, dependency, contract, or architectural question.
Materiality Gate is not a phase; it is LEAP's question filter for deciding whether missing context should trigger a question, source inspection, or a stated assumption.
LEAP Prompt produces Codex-ready instructions for analysis, documentation, implementation, or remediation.
Implementation executes the approved prompt in the repository.
Validation/Handoff verifies changes, checks docs/tests, summarizes work, and recommends follow-up prompts.
```

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Relationship model:

```text
LEAP Framework
  |-- LEAP Charter
  |   |-- Greenfield Mode
  |   `-- Brownfield Mode
  |-- LEAP Recon
  |   |-- Investigation / discovery / pressure testing
  |   `-- Dependency & Contract Recon
  |-- LEAP Prompt
  |   |-- Charter Prompt
  |   |-- Recon Prompt
  |   |-- Standard Implementation Prompt
  |   |-- Fix Prompt
  |   |-- Refactor Prompt
  |   |-- Governance Prompt
  |   |-- Validation Prompt
  |   `-- LHS Prompt
  |-- Operating disciplines
  |   `-- Materiality Gate
  `-- Validation / Handoff
```

### LEAP Charter

Use LEAP Charter when project direction, source truth, documentation structure, roadmap, implementation posture, or existing-project alignment needs to be established or reconciled.

Greenfield Mode is for brand-new projects, early-stage ideas, or solutions that do not yet have a stable repo, roadmap, architecture, or documentation structure.

Brownfield Mode is for existing or mid-buildout projects where LEAP needs to inspect the repo, reconcile documentation, identify gaps, establish source-of-truth docs, and prepare future LEAP Recon, LEAP Prompt, or LHS work.

Brownfield reconciliation follows this policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

### LEAP Recon

Recon investigates a focused area, gap, risk, feature, dependency, contract, or architectural question before implementation planning.

Recon must inspect source-of-truth manifests, documentation lifecycle status, stale assumptions, repo reality, branch/worktree/PR drift, existing functionality, declared or detected dependency contracts, cross-layer impacts, layer boundaries, human checkpoints, material unknowns, and the recommended agent execution configuration.

Dependency & Contract Recon is a subprocess inside Recon. It looks for `leap.dependencies.yaml` or an equivalent dependency register, follows declared contract links such as OpenAPI sources when accessible, compares provider evidence against consumer expectations, and separates findings into current-work impact, general system impact, and unknown / needs verification. See [`docs/dependency-contract-recon.md`](docs/dependency-contract-recon.md), [`examples/leap.dependencies.yaml`](examples/leap.dependencies.yaml), and [`schemas/leap.dependencies.schema.json`](schemas/leap.dependencies.schema.json).

### Materiality Gate

Materiality Gate is not a lifecycle phase. It is LEAP's clarification discipline and question filter. Before asking a question, LEAP determines whether the missing answer would materially change the output, implementation path, risk profile, source-of-truth hierarchy, validation strategy, acceptance criteria, or user-facing recommendation.

If the answer would materially change the work, LEAP asks the smallest useful set of targeted questions. If the information is discoverable from available sources, LEAP inspects those sources first. If the answer would only refine naming, wording, formatting, ordering, tone, minor preference, or polish, LEAP states a reasonable assumption and proceeds. See [`docs/materiality-gate.md`](docs/materiality-gate.md).

### LEAP Prompt

LEAP Prompt converts approved Charter and Recon findings into Codex-ready instructions for analysis, documentation, implementation, or remediation.

A valid LEAP Prompt includes objective, current repo reality, source-of-truth instructions, scope, non-goals, constraints, implementation sequence, verification, stop conditions, branch/worktree/commit instructions, source-of-truth update policy, completion report format, and a required Agent Execution Configuration block.

LEAP LHS is not a mandatory lifecycle stage. It is a structured LEAP Prompt format for layered implementation work using the House Standard. Use it when work is layered, staged, or large enough to require House Standard-style execution. Not every LEAP Prompt is an LHS prompt.

Use LHS when implementation gravity is high: staged changes, dependency order, multi-area work, tests plus docs, phased commits, architecture/data/workflow changes, rollback risk, named-layer work, follow-up work, or explicit acceptance criteria. Do not use LHS for pure analysis, early brainstorming, one-file edits, small copy/doc fixes, obvious quick bugs, or ceremony that does not reduce risk.

### Implementation

Implementation is the execution of the approved LEAP Prompt by Codex or another coding agent.

Implementation should stay within the approved scope, follow repo patterns, preserve non-goals, and stop when the prompt's stop conditions are met.

### Validation/Handoff

Validation/Handoff is the required completion step where Codex verifies changes, checks docs/tests, summarizes work, and recommends follow-up prompts.

## Agent execution configuration

Every agent-ready LEAP Prompt must explicitly state:

```text
- Agent / Tool
- Codex Plan Mode
- Model
- Reasoning Level
- Execution Mode
- Scope Scale
- Repository
- Branch / Worktree
- Permissions
- Validation
- Commit Guidance
```

A prompt is not ready for a coding agent unless it tells the user exactly which execution profile to use. For Codex-targeted prompts, it must also tell the user whether Codex Plan Mode should be On, Off, or User decision required before submission.

Codex Plan Mode is a user-controlled Codex UI setting. LEAP Execution Mode is the instruction inside the prompt. Use `repo-preflight-then-implement` for bounded work where Codex should check repo reality and stop conditions, then proceed directly if clear.

If the exact model, reasoning level, Codex Plan Mode, or execution mode is unknown, LEAP must recommend one instead of leaving the field blank.

## Current framework

Canonical framework document: [`docs/leap.md`](docs/leap.md).

Charter reference: [`docs/leap-charter.md`](docs/leap-charter.md).

Materiality Gate reference: [`docs/materiality-gate.md`](docs/materiality-gate.md).

Older version detail is preserved through Git history, [`CHANGELOG.md`](CHANGELOG.md), [`docs/maintainer/release-history.md`](docs/maintainer/release-history.md), and release tags when present. Active docs should stay focused on the current framework baseline.

## Quick start

### Start here

- [`docs/00_start_here.md`](docs/00_start_here.md) - the plain-English front door
- [`docs/README.md`](docs/README.md) - documentation map

### Use LEAP

- [`docs/user/LEAP_PROJECT_SETUP.md`](docs/user/LEAP_PROJECT_SETUP.md) - set up LEAP in a ChatGPT/Codex project
- [`docs/user/leap-for-humans.md`](docs/user/leap-for-humans.md) - the simple explanation of how LEAP thinks
- [`docs/user/which-leap-workflow.md`](docs/user/which-leap-workflow.md) - choose Quick Brief, Charter, Recon, Prompt, or LHS
- [`docs/user/when-not-to-use-leap.md`](docs/user/when-not-to-use-leap.md) - decide when a normal prompt or Quick Brief is enough
- [`docs/user/quick-leap-brief.md`](docs/user/quick-leap-brief.md) - the smallest useful LEAP workflow
- [`templates/leap-charter-template.md`](templates/leap-charter-template.md) - start a new product, major direction, or brownfield reconciliation

After Charter is approved, use [`templates/leap-recon-template.md`](templates/leap-recon-template.md) to request a Recon pass for the first focused area, target layer, feature, risk, dependency, contract, or architectural question. For a shorter starter version, use [`templates/leap-recon-lite-template.md`](templates/leap-recon-lite-template.md).

After Recon is approved, use [`templates/leap-prompt-template.md`](templates/leap-prompt-template.md) to generate the final implementation, documentation, analysis, or remediation prompt.

For repeatable workflows, use the operational prompt library under [`prompts/`](prompts/).

### Adopt AGENTS.md

Use [`docs/user/LEAP_PROJECT_SETUP.md`](docs/user/LEAP_PROJECT_SETUP.md) for the end-to-end adoption path across ChatGPT Project Instructions, repository-level `AGENTS.md`, Codex population, and first LEAP Recon.

Use the dedicated [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) repository for AGENTS.md templates, install guidance, versioning, compatibility manifests, and upgrade guidance.

### Framework reference

- [`docs/leap.md`](docs/leap.md) - canonical current framework document
- [`docs/leap-charter.md`](docs/leap-charter.md) - Charter modes and brownfield documentation reconciliation
- [`docs/materiality-gate.md`](docs/materiality-gate.md) - question, assumption, and inspect-first discipline
- [`docs/dependency-contract-recon.md`](docs/dependency-contract-recon.md) - dependency register and contract-drift Recon guidance
- [`docs/reference/README.md`](docs/reference/README.md) - current reference index

### Maintain LEAP Framework

- [`docs/maintainer/framework-doc-governance.md`](docs/maintainer/framework-doc-governance.md) - documentation domain governance

## Source-of-truth document model

Every serious LEAP-managed application should maintain a source-of-truth manifest. The manifest identifies canonical and active docs, draft/stale/archived/delete-candidate docs, source ownership, current branch, relevant PRs, repo reality, doc-code conflicts, and the human owner/approver.

Docs should be classified as:

```text
Canonical | Supporting | Current but poorly organized | Partially useful | Stale | Conflicting | Duplicate | Completed implementation plan | Misleading | Archived | Unknown
```

Generated docs are Draft until explicitly ratified. Archived docs are historical unless a current canonical document explicitly references them.

## Repository structure

```text
README.md
CHANGELOG.md
CONTRIBUTING.md
VERSION.md
docs/
  00_start_here.md
  README.md
  leap-charter.md
  dependency-contract-recon.md
  materiality-gate.md
  leap.md
  glossary.md
  agent-profiles.md
  risk-taxonomy.md
  user/
    LEAP_PROJECT_SETUP.md
    leap-for-humans.md
    when-not-to-use-leap.md
    quick-leap-brief.md
    which-leap-workflow.md
  reference/
    README.md
  maintainer/
    release-history.md
    framework-doc-governance.md
  examples/
    small-build-unit.md
    full-layer-recon.md
examples/
  leap.dependencies.yaml
  code-assistant-prompt-for-humans.md
schemas/
  leap.dependencies.schema.json
templates/
  leap-charter-template.md
  leap-recon-lite-template.md
  leap-recon-template.md
  leap-prompt-template.md
prompts/
  README.md
  leap-charter-standard.md
  leap-recon-standard.md
  leap-prompt-standard.md
  leap-governance-pass-standard.md
```

Compatibility stubs remain at `templates/leap-phase-0-template.md` and `prompts/leap-phase-0-standard.md` for older links.

## Short rule

```text
No clarity, no build.
No source truth, no Recon.
No repo reality, no prompt.
No non-goals, no agent handoff.
No stop conditions, no coding task.
No execution profile, no agent-ready prompt.
Canonical docs first.
Archived docs are historical.
Ask only material questions; inspect discoverable sources first; proceed on stated assumptions for non-material unknowns.
Ask until the idea becomes buildable, then stop asking and build only the bounded task.
```
