<!--
LEAP_FRAMEWORK_REPO_AGENTS:
  purpose: repo-specific guidance for maintaining the LEAP Framework repository
  source_repo: https://github.com/mcataloe/leap_framework
  agent_pack_repo: https://github.com/mcataloe/leap_agent_pack
  distributable_template: false
END_LEAP_FRAMEWORK_REPO_AGENTS
-->

# LEAP Framework Repo AGENTS.md

This repository-root `AGENTS.md` is repo-specific guidance for maintaining the LEAP Framework repository. It is not a distributable Agent Pack template.

Canonical distributable AGENTS.md templates live in:

```text
https://github.com/mcataloe/leap_agent_pack
```

This file has two managed sections:

1. **Locked Global Section** — reusable LEAP operating behavior.
2. **Editable Repository Section** — guidance specific to this repository.

---

<!-- LEAP_MANAGED_SECTION_BEGIN -->
<!-- LEAP_MASTER_GLOBAL_SECTION_START: DO NOT EDIT DURING REPO POPULATION -->

# Locked Global Section - LEAP Operating Template

## Purpose

Use LEAP as the default operating model for software engineering tasks unless the user, repository, or task-specific prompt says otherwise.

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP Charter establishes or reconciles project direction, source-of-truth docs, roadmap, and implementation posture.

LEAP Recon investigates a focused area, gap, risk, feature, or architectural question.

LEAP Prompt produces Codex-ready instructions for analysis, documentation, implementation, or remediation.

LEAP LHS is a structured LEAP Prompt format for layered implementation work using the House Standard. It is not a mandatory lifecycle stage.

LEAP Prompt is the instruction artifact family. It includes Charter, Recon, standard implementation, fix, refactor, governance, validation, and LHS prompts. Use LEAP LHS only when staged implementation is warranted by implementation gravity.

Validation/Handoff is the required completion step where Codex verifies changes, checks docs/tests, summarizes work, and recommends follow-up prompts.

## Instruction Priority

When working in a repository, follow instructions in this order:

1. System/developer/tool instructions.
2. Explicit user instructions for the current task.
3. The editable repository section below and closer scoped agent instruction files.
4. This locked global section.
5. Existing source code, tests, documentation, and conventions.

If instructions conflict, follow the more specific and more recent instruction unless it would create security, data-loss, or integrity risk.

## Documentation Starting Point

When present, start with `docs/00_start_here.md`.

Treat canonical docs as source of truth. Treat archived docs as historical unless a current canonical document explicitly references them.

During Charter work, prefer LEAP Charter outputs when reconciling project direction. Create LEAP Recon or LEAP Prompt recommendations instead of making risky implementation changes during Charter work.

Use LEAP Recon outputs for focused investigation findings. Use LEAP LHS only when the task needs staged implementation, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination. Do not treat LHS as a mandatory stage after every LEAP Prompt.

## Default Work Pattern

For non-trivial implementation tasks:

1. Understand the task.
2. Perform repository reconnaissance before editing.
3. Locate relevant canonical docs, code, tests, and existing patterns.
4. Make a concise implementation plan.
5. Implement the smallest coherent change.
6. Add or update relevant tests.
7. Run practical validation checks.
8. Complete Validation/Handoff with changes, validation, risks, and follow-ups.

Do not treat the task as greenfield unless the repository clearly lacks an existing implementation path.

## LEAP Command Shortcuts

When the user asks to run LEAP Charter, use `/prompts/leap-charter-standard.md` from the LEAP framework repository.

When the user asks to run LEAP Recon, use `/prompts/leap-recon-standard.md` from the LEAP framework repository.

Default Recon behavior:

1. Use the editable repository section first.
2. Inspect the current repository state.
3. Use source-of-truth documents identified by this file.
4. Treat Brownfield Charter outputs as source-truth inputs when present.
5. Return Recon only.
6. Do not implement code changes.
7. Do not generate the final LEAP implementation prompt unless the user asks after Recon.

## Stop Conditions

Stop and ask before destructive data changes, auth/security changes, public contract changes, new paid services, major dependencies, major architecture replacement, unclear business rules, treating archived docs as current source truth, or irreversible git operations.

<!-- LEAP_MASTER_GLOBAL_SECTION_END -->
<!-- LEAP_MANAGED_SECTION_END -->

---

<!-- LEAP_PROJECT_SECTION_BEGIN -->
<!-- LEAP_MASTER_REPO_SECTION_START: EDIT THIS SECTION ONLY DURING REPO POPULATION -->

# Editable Repository Section - LEAP Framework Repository

## Project Identity

Project name: `LEAP Framework`

LEAP is a Markdown framework, Prompt library, template set, example set, and governance model for documentation-first software delivery.

Primary users:

- humans adopting LEAP
- coding agents requiring source-truth discipline and bounded handoffs
- repository owners using LEAP guidance
- framework maintainers updating doctrine, prompts, templates, examples, and release notes

## Canonical lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the Layered House Standard Prompt format for staged implementation. It is not a lifecycle stage and it does not define the project's strategic documentation hierarchy.

## Canonical project-documentation model

Use:

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

Treat these as separate views:

```text
Roadmap      = timing, priority, milestones, dependencies, releases, status, parallelism
Domain Map   = persistent responsibility boundaries
Architecture = technical structure
```

Rules:

- several Initiatives may run in parallel
- Roadmap does not permanently own Initiative identity
- Initiatives and Domains are many-to-many
- Delivery Unit may collapse for small work
- Build Unit is not necessarily independently deployable
- generic project-planning `Layer` is legacy-compatible and deprecated
- preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references
- classify legacy Layer meaning before migration

Canonical references:

- `docs/project-documentation-model.md`
- `docs/maintainer/project-documentation-migration.md`

## Documentation starting point

Start with `docs/00_start_here.md`.

Primary canonical docs:

- `docs/leap.md`
- `docs/leap-charter.md`
- `docs/project-documentation-model.md`
- `docs/glossary.md`
- `prompts/leap-charter-standard.md`
- `prompts/leap-recon-standard.md`
- `prompts/leap-prompt-standard.md`
- `prompts/leap-governance-pass-standard.md`
- current request templates under `templates/`

Supporting maps and guidance:

- `README.md`
- `docs/README.md`
- `docs/materiality-gate.md`
- `docs/dependency-contract-recon.md`
- `docs/user/`
- `docs/maintainer/framework-doc-governance.md`
- `docs/maintainer/project-documentation-migration.md`
- `prompts/README.md`

Examples are illustrative, not canonical source truth.

Compatibility stubs remain at:

- `prompts/leap-phase-0-standard.md`
- `templates/leap-phase-0-template.md`

Do not prefer compatibility stubs for active work.

## Repository layout

- `README.md` — repository entry point
- `CHANGELOG.md` — current and unreleased changes
- `VERSION.md` — current baseline and release policy
- `docs/` — doctrine, user guidance, maintainer guidance, and examples
- `prompts/` — operational Prompt standards
- `templates/` — request templates
- `examples/` — example artifacts
- `schemas/` — permissive metadata schemas

No runtime application, database, infrastructure, package manager, or test framework is currently defined.

## Framework Recon rules

Recon for this repository should inspect:

- canonical doctrine and documentation maps
- Strategic Outcome, Initiative, Delivery Unit, Build Unit, Roadmap, Domain, Architecture, and Layer terminology
- Charter, Recon, Prompt, Governance, and LHS consistency
- templates and examples
- Agent Pack dependencies
- current release notes and baseline metadata
- branch and PR drift
- public paths and compatibility stubs

When generic `Layer` is found, classify it as:

- framework name
- LHS name
- qualified Architecture term
- Phase
- legacy compatibility reference
- intentional historical example
- unresolved generic planning term

Do not perform a global replacement.

## Charter rules

Use Charter when direction, Strategic Outcomes, Initiative identity, Roadmap, Domains, Architecture, source truth, documentation structure, or implementation posture is unclear.

Brownfield policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Do not rename or archive public docs without an approved migration and link-validation plan.

## Prompt and implementation rules

Implementation in this repository normally means Markdown, Prompt, template, example, metadata, or repository-guidance changes.

Use LHS only when implementation gravity warrants staged work, such as coordinated updates across canonical docs, prompts, templates, examples, governance, release notes, and Agent Pack guidance.

Complete Validation/Handoff with:

- files changed
- checks run or unavailable
- semantic consistency review
- remaining Layer classifications
- public-path and compatibility status
- Agent Pack follow-up

## Source-of-truth order

1. Explicit current user instruction
2. System, developer, and tool instructions
3. Editable repository section and closer-scoped guidance
4. Current branch and repository reality
5. `docs/00_start_here.md`
6. Canonical doctrine docs
7. operational prompts
8. request templates
9. supporting user and maintainer docs
10. release metadata
11. archived and compatibility docs only when explicitly relevant
12. clearly labeled inference

## Public contracts

Treat these as public-facing contracts:

- documentation paths
- Prompt and template names
- headings and output shapes
- lifecycle terms
- project-documentation terminology
- `AGENTS.md` marker conventions
- compatibility stubs

Preserve backward compatibility or provide an approved migration plan.

## Documentation expectations

Keep these aligned when framework behavior changes:

- `README.md`
- `docs/00_start_here.md`
- `docs/README.md`
- `docs/leap.md`
- `docs/leap-charter.md`
- `docs/project-documentation-model.md`
- `docs/glossary.md`
- `docs/user/`
- `docs/maintainer/project-documentation-migration.md`
- `prompts/README.md`
- active operational prompts
- active request templates
- examples
- `CHANGELOG.md`
- `VERSION.md`
- Agent Pack repository when distributable guidance changes

## Validation

Practical manual validation:

```bash
rg -n "\bLayer\b|layer plan|Layer map|sublayer|entire layer|full-layer|cross-layer|current layer|active layer" .
```

```bash
rg -n "Strategic Outcome|Initiative|Delivery Unit|Build Unit|Roadmap|Domain|Architecture" README.md AGENTS.md docs prompts templates examples CHANGELOG.md VERSION.md
```

```bash
rg -n "\]\(([^)#]+\.md)(#[^)]+)?\)" README.md docs prompts templates examples CHANGELOG.md VERSION.md CONTRIBUTING.md
```

Do not add new validation tooling or dependencies without approval.

## Stop conditions

Stop if:

- active canonical docs materially conflict
- local or branch work creates unclear ownership
- a task requires editing the locked global section or marker boundaries
- a public path must be removed or renamed without approval
- a compatibility stub must be removed
- a new dependency, CI system, docs generator, or external service is required
- Agent Pack changes are needed but repository scope or versioning is unclear
- a generic Layer use cannot be classified safely
- validation cannot be performed

## Branch and commit conventions

- default branch is `main`; verify before work
- inspect branch and worktree state before edits
- preserve unowned work
- do not reset, discard, force push, or rewrite unrelated history
- use focused commits
- do not create a release tag unless explicitly requested

## Known follow-up area

When framework project-documentation terminology changes, inspect the separate Agent Pack repository for distributed guidance drift. Keep framework and Agent Pack commits separate.

## Completion requirements

A task is complete when requested behavior is implemented, canonical and supporting docs agree, public paths are preserved, validation is reported, and follow-up Agent Pack or downstream migration work is identified.

<!-- LEAP_MASTER_REPO_SECTION_END -->
<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->
<!--
Optional local team or developer-specific notes go here.
Keep durable project guidance in the editable repository section above.
-->
<!-- LEAP_LOCAL_OVERRIDES_END -->
