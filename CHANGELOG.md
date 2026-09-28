# Changelog

Current and unreleased LEAP Framework changes are recorded here. Use Git history, release notes, and tags for older detail.

## Unreleased - Repository Cleanup workflow

### Added

- Added `Run LEAP Cleanup` as a specialized Governance workflow for repository artifact decommissioning.
- Added the cleanup contract, operational Prompt, compact request template, cleanup modes, decommission-set schema, approval gate, and effective-status rules.

### Changed

- Routed approved cleanup execution through LEAP Refactor Prompt and existing Validation/Handoff behavior instead of adding a lifecycle phase.
- Required authority, dependency, consumer, public-path, and canonical-replacement evidence before decommissioning.
- Defined cleanup modes as `archive-only`, `controlled-migration`, and `destructive-cutover`, separate from Agent Execution Mode.
- Established Git history as the default archive for destructive cutovers and required structural, semantic, and behavioral validation where relevant.

## Unreleased - Parallel-capable project documentation

### Added

- Added `docs/project-documentation-model.md` as the canonical project documentation hierarchy.
- Added `docs/maintainer/project-documentation-migration.md` for semantic reconciliation of legacy Layer documents.
- Added Strategic Outcome, Initiative, Delivery Unit, Roadmap, Domain, Architecture, Planning Boundary Review, and cross-Initiative / cross-Domain concepts.
- Added examples for parallel Initiatives and collapsed Delivery Units.

### Changed

- Established the preferred traceability model:

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

- Defined Roadmap as a scheduling, priority, dependency, milestone, release, status, and parallelism view rather than permanent Initiative ownership.
- Defined Domains as persistent responsibility boundaries with a many-to-many relationship to Initiatives.
- Defined Architecture as technical structure rather than a strategic planning level.
- Clarified that Delivery Units may collapse for small work and Build Units are not necessarily independently deployable.
- Marked generic project-planning `Layer` as legacy-compatible and deprecated as the preferred planning level.
- Updated canonical docs, Charter, Recon, Prompt, Governance, templates, examples, navigation, user guidance, and repository `AGENTS.md`.

### Compatibility

- Preserved the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public documentation paths, Phase 0 compatibility stubs, and existing downstream Layer documents pending reconciliation.
- Agent Pack alignment is versioned separately in the Agent Pack repository.

## Unreleased - Baseline Freshness Check

- Added Baseline Freshness Check as Recon preflight behavior.
- Added optional `leap.baseline.yaml` example and schema.
- Clarified that Charter is not required before every Recon.

## Unreleased - Project setup instructions

- Added full ChatGPT Project Instructions and LEAP command coverage to project setup guidance.

## Unreleased - Materiality Gate

- Added Materiality Gate guidance for inspect-first, question, and assumption discipline.

## Unreleased - Dependency & Contract Recon

- Added Dependency & Contract Recon, dependency-register guidance, example, schema, risk classification, and read-only provider evidence rules.

## Unreleased - Dedicated LEAP Agent Pack repository

- Moved distributable `AGENTS.md` template ownership to the separate Agent Pack repository.
- Added docs-domain routing and Agent Pack update guidance.

## Unreleased - LEAP Prompt taxonomy and LHS clarification

- Clarified that LHS is a structured LEAP Prompt format rather than a lifecycle phase.
- Standardized the lifecycle as `LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff`.

## Unreleased - LEAP Charter and Brownfield reconciliation

- Added canonical Charter doctrine, Greenfield and Brownfield modes, migration maps, archive guidance, and compatibility stubs for older Phase 0 paths.

## LEAP v0.1.9 - Repository canonicalization and Prompt flattening

- Established canonical current framework files and flattened operational Prompts.
- Older version detail remains in Git history, release notes, and tags.
