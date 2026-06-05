# LEAP Prompt Library

This directory contains reusable operational prompts for running LEAP workflows.

The `templates/` directory contains compact request templates. The `prompts/` directory contains fuller copy-ready operational prompts for recurring work.

## Current lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is not a mandatory lifecycle stage. It is a structured LEAP Prompt format for layered implementation work using the House Standard.

## LEAP Prompt family

LEAP Prompt is the broad category of Codex-ready or agent-ready instruction artifacts generated from Charter, Recon, user intent, or approved implementation scope.

| Prompt Type | Purpose | Use LHS? |
| --- | --- | --- |
| [Charter Prompt](leap-charter-standard.md) | Establish or reconcile direction, docs, roadmap, baseline | Sometimes |
| [Recon Prompt](leap-recon-standard.md) | Investigate focused risk, repo reality, or implementation uncertainty | Usually no |
| [Standard Implementation Prompt](leap-prompt-standard.md) | Small or medium implementation change | Sometimes no |
| [Fix Prompt](leap-prompt-standard.md) | Specific bug or remediation | Usually no |
| [Refactor Prompt](leap-prompt-standard.md) | Larger structural change | Often yes |
| [Governance Prompt](leap-governance-pass-standard.md) | Repo/process/source-of-truth cleanup | Sometimes |
| [Validation Prompt](leap-prompt-standard.md) | Verify tests/docs/acceptance and summarize handoff | Usually no |
| [LHS Prompt](../docs/leap.md) | Staged implementation sequence | Yes |

Use Quick LEAP Brief or a standard implementation prompt for low-gravity work. Use LHS when implementation gravity is high enough to need staged execution, commit boundaries, tests and docs, multi-area coordination, compatibility checks, rollback awareness, or explicit acceptance criteria.

Materiality Gate is the question, assumption, and inspect-first discipline used by Charter, Recon, and Prompt generation. Use it before asking clarifying questions: inspect discoverable sources first, proceed on stated assumptions for non-material unknowns, and ask only unresolved material questions. Supporting guidance lives in [`../docs/materiality-gate.md`](../docs/materiality-gate.md).

Dependency & Contract Recon is a subprocess inside LEAP Recon, not a separate lifecycle phase. Use it when the repo declares or appears to depend on provider APIs, external services, packages, artifacts, shared contracts, or cross-repo contract sources. Supporting guidance lives in [`../docs/dependency-contract-recon.md`](../docs/dependency-contract-recon.md).

## Prompt categories

```text
prompts/
  README.md
  leap-charter-standard.md
  leap-recon-standard.md
  leap-prompt-standard.md
  leap-governance-pass-standard.md
```

Compatibility stubs remain at `prompts/leap-phase-0-standard.md` for older links.

## Current public workflow

Use the current top-level templates:

```text
templates/leap-charter-template.md
templates/leap-recon-template.md
templates/leap-prompt-template.md
```

Use the current adoption docs first when onboarding new users:

```text
docs/00_start_here.md
docs/leap-charter.md
docs/materiality-gate.md
docs/user/leap-for-humans.md
docs/user/quick-leap-brief.md
docs/agent-profiles.md
docs/risk-taxonomy.md
```

## Categories

### Charter prompts

Use LEAP Charter prompts before Recon when project direction, target user, current workflow, MVP boundary, risks, non-goals, no-build alternatives, documentation structure, source-of-truth baseline, or brownfield reconciliation is unclear.

Greenfield Charter establishes enough structure to start safely.

Brownfield Charter reconciles existing docs and planning artifacts:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Charter applies Materiality Gate before asking discovery questions. It should inspect discoverable repo/docs evidence first, convert non-material unknowns into assumptions, and ask only unresolved material questions needed for the next gate decision.

### Recon prompts

Use Recon prompts before implementation. They investigate a focused area, gap, risk, feature, dependency, contract, or architectural question. They inspect source-of-truth manifests, document lifecycle status, repository reality, branch/worktree/PR drift, strategic-plan alignment, stale assumptions, existing functionality, dependency registers and contract sources when relevant, cross-layer impact, material unknowns, risk, destructive-change implications, and recommended agent execution configuration before creating implementation prompts.

### Implementation prompts

Use implementation prompts after Recon is complete and the Build Unit sequence has been approved or defaults have been accepted. These prompts are intended for Codex-style or another coding agent.

An implementation prompt is not agent-ready unless it includes an explicit agent/tool, Codex Plan Mode for Codex-targeted prompts, model, reasoning level, execution mode, Materiality / Assumption Handling section, validation plan, and stop conditions.

Codex Plan Mode is a user-controlled Codex UI setting. LEAP Execution Mode is the instruction inside the prompt. Use `repo-preflight-then-implement` for bounded prompts where Codex should verify repo reality and stop conditions, then proceed directly if clear.

Implementation prompts must not ask the coding agent to resolve material product, architecture, source-truth, risk, validation, or acceptance-criteria questions during implementation. New material uncertainty should become a stop condition.

### LEAP LHS prompts

LEAP LHS is a structured LEAP Prompt format for layered implementation work using the House Standard. Use it when work is layered, staged, or large enough to require House Standard-style execution. Not every LEAP Prompt is an LHS prompt.

Do not use LHS for pure analysis, early brainstorming, one-file edits, small copy/doc fixes, quick bugs with obvious scope, or work where ceremony would not reduce risk.

### Governance prompts

Use governance prompts outside normal layer implementation when the repo needs reconciliation, roadmap correction, branch/worktree drift review, cross-layer impact review, stale-plan cleanup, stale-prompt cleanup, source-of-truth ownership cleanup, or agent/model/reasoning guidance cleanup.

## Current prompt files

The active prompt library uses canonical root-level files under `prompts/`.

Current files:

```text
prompts/leap-charter-standard.md
prompts/leap-recon-standard.md
prompts/leap-prompt-standard.md
prompts/leap-governance-pass-standard.md
```

Operational prompt files represent the current canonical LEAP workflow. Historical prompt versions are preserved through Git tags and Git history.

## LEAP process tier guidance

Use the smallest LEAP process tier that controls the risk:

```text
Standard - small, clear, low-risk tasks
Thinking Extended - Charter discovery, MVP/non-goal work, moderate Recon, bounded prompt drafting
Pro Standard - existing repos, partial implementation, multiple docs, cross-layer review, significant refactor planning
Pro Extended - strategic pivots, stale docs, brownfield reconciliation, branch drift, parallel agents, privacy/security-sensitive workflows, high-risk AI behavior
```

## Agent reasoning-level guidance

Use the smallest agent reasoning level that controls the implementation risk:

```text
Low - tiny localized edits, typo fixes, obvious one-file changes
Medium - small bounded implementation, clear UI fixes, simple tests, isolated refactors
High - Build Units, sublayers, multi-file features, state workflows, cross-component UX, meaningful test updates
Extended - full-layer implementation, architecture-sensitive work, repo-wide refactors, parallel-agent sequencing, stale-doc reconciliation, destructive schema/data-model changes, sensitive AI behavior
```

LEAP process tier and agent reasoning level are related, but they are not the same thing. LEAP process tier controls how much framework analysis happens before prompt generation. Agent reasoning level controls how the implementation agent should be run after the prompt is generated.

## Public rule

```text
Ask only material questions.
Inspect discoverable sources first.
Proceed on stated assumptions for non-material unknowns.
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```

Use the current templates when you need readiness gates, source-of-truth manifests, doc lifecycle status, drift ledgers, branch/worktree/PR review, strict coding-agent stop conditions, and explicit agent/model/reasoning execution settings.
