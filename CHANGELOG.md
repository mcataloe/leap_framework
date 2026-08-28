# Changelog

Current and unreleased LEAP Framework changes are recorded here. Use Git history, release notes, and tags for older detail.

## Unreleased - First-class LEAP Skills

### Added

- Added `docs/leap-skills.md` as the canonical reference for reusable execution capabilities.
- Added `templates/leap-skill-template.md` for portable Skill Contract definitions.
- Added Capability / Skill Review to Recon after Build Unit boundaries are clear enough.
- Added Skill source, loading method, permission fit, required/optional status, and Skill-specific verification to agent handoffs.

### Changed

- Defined the Build Unit / Skill boundary: Build Units define **what** bounded implementation responsibility is delivered; Skills define reusable **how** for specialized execution.
- Kept Skills outside the Mission / Strategic Outcome / Initiative / Delivery Unit / Build Unit hierarchy and outside the LEAP lifecycle phase model.
- Updated Recon and LEAP Prompt standards and request templates to select and compose Skills without assuming harness-native availability.
- Made Skill authority subordinate to the governing Prompt and repository policy.
- Added progressive disclosure guidance so deep Skill references load only when relevant.
- Updated canonical framework doctrine, glossary, navigation, entry points, and release metadata.

### Deferred

- Did not add a mandatory Skill registry, automatic Skill discovery service, self-modifying framework loop, or new persisted continuity store. These remain evidence-gated follow-up areas.

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
