<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-charter-reference
  authority: canonical
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# LEAP Charter

LEAP Charter is the official project-alignment front door for LEAP. It replaces the active use of the older "Phase 0" label.

Definition:

```text
The initial solution-alignment process used to establish or reconcile a project before implementation begins or continues.
```

LEAP Charter establishes or reconciles the project direction, source-of-truth documents, roadmap, baseline assumptions, and implementation posture before deeper Recon or implementation prompt generation.

## Lifecycle

The current LEAP lifecycle is:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Lifecycle terms:

- **LEAP Charter:** Establishes or reconciles the project direction, source-of-truth docs, roadmap, and implementation posture.
- **LEAP Recon:** Investigates a focused area, gap, risk, feature, dependency, contract, or architectural question.
- **LEAP Prompt:** Produces Codex-ready instructions for analysis, documentation, implementation, or remediation.
- **Implementation:** The execution of the approved LEAP Prompt by Codex or another coding agent.
- **Validation/Handoff:** The required completion step where Codex verifies changes, checks docs/tests, summarizes work, and recommends follow-up prompts.

LEAP LHS is not a mandatory lifecycle stage. It is a structured LEAP Prompt format for layered implementation work using the House Standard. Use LEAP LHS when work is layered, staged, or large enough to require House Standard-style execution. Not every LEAP Prompt is an LHS prompt.

Charter does not use LHS by default. Charter may recommend a follow-up LHS prompt, and it may itself use LHS only when Charter has moved from discovery into staged repo-changing documentation work.

Not every task starts at Charter. Charter establishes or reconciles the baseline when that baseline is unclear; focused Recon may proceed without a new Charter when its Baseline Freshness Check finds the existing source truth fresh enough.

## Charter Modes

### LEAP Charter - Greenfield Mode

Used for brand-new projects, early-stage ideas, or solutions that do not yet have a stable repo, roadmap, architecture, or documentation structure.

Greenfield Mode should create enough structure to start safely and intentionally. It should not overbuild. Greenfield Charter should usually avoid LHS when it is doing early product shaping, naming, ideation, MVP definition, or strategic discovery.

It should help create or organize:

- Product mission.
- Target users.
- MVP boundary.
- Strategic goals.
- Initial architecture direction.
- Initial data model assumptions.
- Initial roadmap.
- Initial layer plan.
- Initial prompt backlog.
- AGENTS.md guidance if applicable.
- First recommended LEAP Recon or prompt sequence. Recommend LHS only when staged repo/docs foundation work is actually needed.

### LEAP Charter - Brownfield Mode

Used for existing or mid-buildout projects where LEAP needs to inspect the repo, reconcile documentation, identify gaps, establish source-of-truth docs, and prepare future LEAP Recon, LEAP Prompt, or LHS work.

Brownfield Mode should:

1. Identify existing documents.
2. Classify which documents are canonical, supporting, stale, conflicting, duplicate, or archived.
3. Familiarize itself with the current solution.
4. Compare docs against the actual repository/codebase where applicable.
5. Identify gaps between strategy, docs, roadmap, architecture, and implementation.
6. Fix documentation and planning gaps when safe.
7. Create or update supplemental Markdown docs.
8. Produce a gap register.
9. Produce a migration map for legacy documentation.
10. Prepare future LEAP Recon, LEAP Prompt, and LEAP LHS work.

Brownfield Mode may update documentation, organization, naming, and planning artifacts directly. It should generally avoid runtime implementation changes unless explicitly requested. Code, schema, API, UI, auth, workflow, or infrastructure changes should normally be captured as follow-up LEAP Prompts or LHS prompts.

Brownfield Charter should usually begin as a non-mutating discovery/reconciliation pass. It may use LHS after the plan is clear when it needs to reorganize documentation, absorb legacy docs into canonical docs, archive stale docs, create a migration map, update AGENTS templates, update prompt backlogs, or validate links and source-of-truth references.

## Documentation Reconciliation Policy

Brownfield Charter follows this principle:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

LEAP Charter should not simply rename legacy docs or delete old docs. It should reconcile them.

Preferred brownfield approach:

1. Create or confirm the canonical documentation structure.
2. Absorb useful current content into canonical docs.
3. Preserve original legacy docs in an archive folder.
4. Add clear archive/deprecation headers where appropriate.
5. Create a migration map showing old doc -> new canonical location -> status.
6. Update README, docs entry points, and AGENTS.md so humans and LLMs know where to begin.

## Legacy Document Classification

| Classification | Meaning | Recommended Action |
| --- | --- | --- |
| Canonical | Current source of truth | Keep or move into canonical docs structure |
| Supporting | Useful secondary detail | Keep near relevant canonical docs or reference from them |
| Current but poorly organized | Useful but structurally messy | Absorb into canonical docs, archive original |
| Partially useful | Mix of current and stale information | Extract useful content, archive original |
| Stale | No longer reflects current direction | Archive with deprecation note |
| Conflicting | Contradicts current strategy, code, or roadmap | Record conflict, resolve in canonical docs, archive original |
| Duplicate | Repeats content covered elsewhere | Consolidate, archive duplicate |
| Completed implementation plan | Old TODO or phase plan already implemented | Archive or convert remaining items to backlog |
| Misleading | Likely to confuse future work | Archive with explicit warning header |

## Recommended Documentation Structure

This structure is a recommended LEAP-friendly pattern, not a mandatory structure for every project. LEAP should adapt to repo size, maturity, and existing conventions.

```text
docs/
  00_start_here.md

  01_leap_charter/
    00_leap_charter.md
    01_solution_baseline.md
    02_document_inventory.md
    03_gap_register.md
    04_reconciliation_notes.md

  02_product/
    00_product_strategy.md
    01_user_model.md
    02_mvp_scope.md
    03_roadmap.md

  03_architecture/
    00_architecture_overview.md
    01_system_context.md
    02_data_model.md
    03_api_surface.md
    04_integration_strategy.md
    05_security_and_governance.md

  04_layers/
    00_layer_map.md
    layer_01_core_platform.md
    layer_02_intake_and_parsing.md
    layer_03_core_entities.md
    layer_04_application_workflow.md

  05_decisions/
    0001-doc-structure.md
    0002-architecture-direction.md

  06_prompts/
    00_prompt_backlog.md
    01_lhs_sequence.md

  99_archive/
    README.md
    YYYY-MM-DD-leap-charter-reconciliation/
      legacy-docs-here.md
```

## Doc Metadata Convention

Important docs should include a small status header.

Canonical doc example:

```markdown
# Product Strategy

Status: Canonical
Last reconciled: YYYY-MM-DD
LEAP mode: Brownfield Charter
Source of truth: Yes

Purpose:
This document defines the current product strategy, target users, MVP boundary, and roadmap priorities.
```

Archived doc example:

```markdown
# Legacy Roadmap

Status: Archived / Superseded
Archived during: LEAP Charter - Brownfield Mode
Do not use as source of truth.

Replacement:
- ../02_product/03_roadmap.md
```

## Archive README

`docs/99_archive/README.md` should explain that archived docs are historical only.

Recommended language:

```markdown
# Documentation Archive

This folder contains superseded, historical, duplicate, or pre-reconciliation documentation.

These documents are preserved for traceability but are not source-of-truth materials. Use the canonical docs under `/docs` unless a current canonical document explicitly references an archived file.
```

## Migration Map

Brownfield Mode should produce a migration map.

| Legacy Doc | New Canonical Destination | Status | Notes |
| --- | --- | --- | --- |
| `old-roadmap.md` | `docs/02_product/03_roadmap.md` | Absorbed | Current roadmap items moved forward |
| `architecture-notes.md` | `docs/03_architecture/00_architecture_overview.md` | Partially absorbed | Stale deployment assumptions excluded |
| `layer-plan-v1.md` | `docs/04_layers/00_layer_map.md` | Superseded | Replaced by current layer map |
| `brainstorming.md` | `docs/99_archive/...` | Archived only | Historical ideation only |

## LLM-Friendly Documentation

LEAP documentation should help both humans and LLMs by:

- Using stable numbered filenames for high-priority docs.
- Creating a `00_start_here.md` entry point.
- Clearly labeling canonical vs archived docs.
- Keeping source-of-truth docs near the top of the docs tree.
- Avoiding duplicate competing roadmap files.
- Using explicit `Status` and `Purpose` sections.
- Creating gap registers and prompt backlogs.
- Keeping archived docs available but clearly non-authoritative.
- Updating AGENTS.md to point Codex and other coding assistants to canonical docs first.

## AGENTS.md and Prompt Backlogs

When LEAP Charter updates project documentation, it should also update the project guidance that coding agents use.

Coding-agent guidance should say:

1. Start with `docs/00_start_here.md` when present.
2. Treat canonical docs as source of truth.
3. Treat archived docs as historical unless explicitly referenced by a current canonical document.
4. Prefer LEAP Charter outputs when reconciling project direction.
5. Create LEAP Recon or LEAP Prompt recommendations instead of making risky implementation changes during Charter work.

Brownfield Charter should also create or update a prompt backlog that captures unresolved implementation, documentation, architecture, roadmap, and reconciliation work. Runtime implementation changes found during Charter should normally become follow-up LEAP Prompts or LEAP LHS prompts, not ad hoc code edits.

## Optional Baseline Register

Repository AGENTS.md should include a small LEAP Baseline State table for future Recon preflight checks. This table is a signal, not a hard gate, and should not become a running status log.

For larger or drift-prone projects, Brownfield Charter, LEAP Governance, or an explicitly authorized baseline/setup scan may create a machine-readable `leap.baseline.yaml` file. It is optional and should be created only when project complexity or source-truth drift risk justifies machine-readable tracking.

Recommended creation triggers include:

- multiple canonical docs exist
- stale/archive/conflict risk exists
- repo has layer plans, roadmap docs, ADRs, prompt backlogs, or gap registers
- multiple agents or humans may work in the repo
- project has recurring Recon, Prompt, or LHS work
- AGENTS.md would become too noisy
- Brownfield Charter produced a migration map or gap register
- dependency or contract tracking is present

When `leap.baseline.yaml` exists, treat it as the canonical machine-readable baseline record and keep AGENTS.md as a short pointer/summary. A normal LEAP Recon freshness check may recommend `leap.baseline.yaml`, but must not silently create it. For tiny projects, keep baseline state in AGENTS.md only.
