# LEAP Version

LEAP release versions are managed by Git tags. Active release notes should stay focused on current and unreleased changes; use Git history and release tags for older detail.

LEAP `AGENTS.md` templates are released separately from the LEAP Agent Pack repository because downstream repositories copy and customize those files.

## Current framework baseline

```text
Version: 0.1.9
Release tag: leap-v0.1.9
Status: current released baseline; current branch changes remain unreleased
```

## Unreleased framework additions

```text
- Parallel-capable project documentation model
- Mission / Project Charter -> Strategic Outcome -> Initiative -> Delivery Unit -> Build Unit traceability
- Roadmap as scheduling, priority, dependency, milestone, release, status, and parallelism view
- Domains as persistent responsibility boundaries with many-to-many Initiative relationships
- Architecture separated from the strategic hierarchy
- Delivery Unit collapse rule for small work
- Build Unit clarified as bounded implementation, not necessarily independently deployable
- Legacy-compatible generic Layer deprecation and semantic migration guidance
- Planning Boundary Review and cross-Initiative / cross-Domain impact review
- Materiality Gate for clarifying-question discipline
- Dependency & Contract Recon subprocess
- Baseline Freshness Check preflight
- Optional baseline and dependency register guidance
- Repository Cleanup Governance workflow and `Run LEAP Cleanup` command
- `archive-only`, `controlled-migration`, and `destructive-cutover` cleanup modes
- Dependency-aware decommission sets, approval gates, and effective-status validation
```

## Canonical framework documents

```text
docs/leap.md
docs/leap-charter.md
docs/project-documentation-model.md
docs/glossary.md
docs/repository-cleanup.md
```

## Supporting references

```text
docs/materiality-gate.md
docs/dependency-contract-recon.md
prompts/leap-cleanup-standard.md
templates/leap-cleanup-template.md
docs/maintainer/project-documentation-migration.md
examples/leap.baseline.yaml
schemas/leap.baseline.schema.json
examples/leap.dependencies.yaml
schemas/leap.dependencies.schema.json
```

## Current Agent Pack

```text
Version: 0.2.0 candidate
Release tag: none verified
Repository: https://github.com/mcataloe/leap_agent_pack
Manifest: manifests/latest.json
Update policy: notify
```

The first Agent Pack release tag should be created only after its manifest and template metadata are committed and validated.

Release context is preserved through:

```text
CHANGELOG.md
Git tags
Git commit history
```

Active framework and Prompt files should not use versioned filenames.

Agent Pack template files live in the Agent Pack repository. Version identity belongs in Agent Pack metadata and manifests, not LEAP Framework filenames.
