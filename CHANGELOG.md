# Changelog

All notable current changes to the LEAP Framework will be documented here.

Historical details that are not applicable to the current framework version should not remain in active docs. Use Git history, release notes, and release tags for older version detail.

## Unreleased - Materiality Gate

### Added

- Added `docs/materiality-gate.md` as supporting guidance for deciding when LEAP agents should ask a clarifying question, inspect available sources first, or proceed with a stated assumption.
- Added Materiality Gate references to the README, docs map, and reference index.

### Changed

- Refined LEAP clarification behavior so confidence thresholds do not create avoidable question loops.
- Clarified that non-material unknowns should become stated assumptions, discoverable unknowns should be inspected from available sources, and unresolved material unknowns should trigger the smallest useful set of targeted questions.

## Unreleased - Dependency & Contract Recon

### Added

- Added Dependency & Contract Recon as a subprocess inside LEAP Recon for dependency registers, provider contract links, and contract-drift findings.
- Added `docs/dependency-contract-recon.md` as supporting guidance for dependency register detection, candidate dependency scanning, OpenAPI contract comparison, impact classification, evidence, confidence, and notification boundaries.
- Added `examples/leap.dependencies.yaml` as a starter dependency register.
- Added `schemas/leap.dependencies.schema.json` as a permissive starter schema for `leap.dependencies.yaml`.

### Changed

- Updated Recon prompts and templates to check dependency registers, inspect declared contract sources when accessible, compare provider evidence against consumer expectations, and classify findings as current-work impact, general system impact, or unknown / needs verification.
- Added dependency contract risk to the risk taxonomy and Recon risk review.
- Updated framework routing docs, glossary, README, and docs maps to reference Dependency & Contract Recon.
- Clarified that notification automation, release blocking, ticket creation, runtime telemetry ingestion, and automatic cross-repo mutation remain out of scope by default.

## Unreleased - Dedicated LEAP Agent Pack repository

### Added

- Added references to the dedicated LEAP Agent Pack repository for AGENTS.md templates, manifests, install docs, and upgrade guidance.

### Changed

- Moved distributable AGENTS.md template ownership out of the LEAP Framework repo and into the LEAP Agent Pack repository.
- Clarified that AGENTS.md updates are notify/manual-merge only and must not overwrite downstream project or local sections automatically.
- Clarified that Agent Pack release tags use `leap-agent-pack-vX.Y.Z` separately from framework tags.
- Reorganized LEAP documentation into clearer user, reference, maintainer, and example domains.
- Added `docs/README.md` as the documentation source-of-truth map.
- Added maintainer documentation governance guidance.
- Removed unreleased moved-path stubs for AGENTS.md documentation and repointed active references to the live docs.
- Normalized framework release labels to pre-1.0 `v0.1.x` versioning.
- Clarified the current framework baseline and pre-1.0 framework tag shape.

### Removed

- Removed framework-local distributable AGENTS.md templates, Agent Pack manifests, and Agent Pack-specific install/versioning docs now owned by the dedicated Agent Pack repo.

## Unreleased - LEAP Prompt taxonomy and LHS clarification

### Changed

- Clarified that LEAP LHS is a structured implementation-prompt format within the LEAP Prompt family, not a mandatory lifecycle phase.
- Updated lifecycle language to use `LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff`.
- Added guidance for when Charter, Recon, and implementation prompts should or should not use LHS.
- Added LHS decision rules based on implementation gravity, staged execution, tests, docs, compatibility risk, and commit boundaries.

## Unreleased - LEAP Charter and brownfield reconciliation

### Added

- Added `docs/leap-charter.md` as the canonical LEAP Charter reference.
- Added `prompts/leap-charter-standard.md` and `templates/leap-charter-template.md`.
- Added Greenfield and Brownfield Charter modes.
- Added the Brownfield documentation reconciliation policy:
  - Canonicalize forward.
  - Archive backward.
  - Preserve traceability.
  - Never let stale docs compete with source-of-truth docs.
- Added legacy document classification rules, migration map guidance, archive README guidance, status-header metadata convention, and LLM-friendly documentation guidance.

### Changed

- Updated the active lifecycle to:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

- Replaced active "Phase 0" terminology with LEAP Charter terminology.
- Clarified that LEAP LHS is a structured LEAP Prompt format for layered House Standard-style implementation work, not a mandatory lifecycle stage.
- Updated Recon and Prompt standards to treat Brownfield Charter outputs as source-truth inputs.
- Updated AGENTS templates to start with `docs/00_start_here.md` when present, prefer canonical docs, treat archived docs as historical, and recommend Recon/Prompt follow-ups instead of risky implementation changes during Charter work.

### Compatibility

- Kept `prompts/leap-phase-0-standard.md` and `templates/leap-phase-0-template.md` as compatibility stubs for older links.

## LEAP v0.1.9 - Repository canonicalization and prompt flattening

### Added

- Added canonical current framework document path: `docs/leap.md`.
- Added current version marker in `VERSION.md`.
- Added flattened current operational prompt files:
  - `prompts/leap-phase-0-standard.md`
  - `prompts/leap-recon-standard.md`
  - `prompts/leap-prompt-standard.md`
  - `prompts/leap-governance-pass-standard.md`

### Changed

- Updated README and prompt-library documentation to describe the canonical-current repository model.
- Replaced the active versioned framework-doc model with a canonical current framework document.
- Replaced nested current prompt paths with root-level prompt files under `prompts/`.
- Updated templates and current prompt files to use version-neutral current-framework wording.

### Removed

- Removed old versioned framework docs from the active repository.
- Removed nested historical prompt directories from the active repository.
- Removed the old v0.1.3 prompt-library document from the active repository.

### Notes

LEAP v0.1.9 is the current framework baseline. Older version details are intentionally omitted from active docs; use Git history and release tags for older release context.
