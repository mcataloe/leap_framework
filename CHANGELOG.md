# Changelog

Current and unreleased LEAP Framework changes are recorded here. Use Git history, release notes, and tags for older detail.

## Unreleased - LEAP Core reconciliation with execution roles, delegation, and estimation

The execution role, delegation, and estimation work merged to `main` through `f61cf30` (2026-11-10, #20–#26) is reconciled with LEAP Core below: it keeps its content and is adapted to LEAP Core's load tiers and define-once rule.

### Added

- `docs/agent-execution-roles.md`: optional architect, implementor, reviewer, and human-approver responsibilities, context packet, and minimum durable handoff. Expected scenarios in `tests/execution-role-cases.json` (all `not_tested`), evaluation guide `tests/EXECUTION_ROLE_EVALUATION.md`, and static validator `tests/validate_execution_roles.py` (run in CI).
- `docs/native-agent-delegation.md`: optional native multi-agent delegation policy, linked from `docs/execution-routing.md` section 11.
- `docs/team-delivery-estimation.md`: advisory effort and delivery estimates with the work tracker as source of record, plus synthetic cases in `tests/team-delivery-estimation-cases.md`. Load tier 2, with one pointer in the Charter doc.
- "Native Codex / Claude routing acceptance (outstanding)" section in `docs/semantic-routing.md`.

### Changed

- `VERSION.md` and `docs/maintainer/release-history.md` no longer claim a `0.1.9` release: tag `leap-v0.1.9` does not exist. The verified published prereleases are `v0.1.10-alpha` and `v.0.1.11-alpha`.
- `tests/check_framework.py` runs on Python 3.9.
- LEAP Core restores three rules from the previous global `AGENTS.md`: stop before changing (not only breaking) public contracts, APIs, schemas, or paths; stop before acting on an unclear business rule that would change the result; add or update tests for changed behavior and extend the existing implementation instead of treating the task as greenfield.
- `tests/validate_semantic_router.py --agent-pack` always requires `manifests/latest.json` and validates `template-inventory.json` and `compatibility.json` when the pack ships them.

### Condensed

- Estimation paragraphs repeated across the Charter standard and template, the Prompt standard, `docs/project-documentation-model.md`, and `docs/execution-routing.md` are removed. `docs/team-delivery-estimation.md` keeps the full doctrine; it is reached from LEAP Core's load tiers, `docs/leap-charter.md`, and a one-line trigger in the Prompt standard's preflight.
- The fill-in execution role block in the Prompt template is replaced by one paragraph pointing to `docs/agent-execution-roles.md`.
- Routing pointers in entry-point docs and the Phase 0 wording are rewritten in LEAP Core's style.

### Pending

- The LEAP Agent Pack (https://github.com/mcataloe/leap_agent_pack) does not yet embed the current LEAP Core. Until it does, the non-blocking CI step `check_framework.py --agent-pack` reports the global and combined templates as out of sync, and `AGENTS.md` and `VERSION.md` refer to Agent Pack `0.2.0-candidate.2`, which that change will publish.

## Unreleased - LEAP Core and ceremony reduction

Goal: keep developers and teams on track with sufficient guardrails and without ceremony. Most guardrail value comes from a short always-loaded rule set plus enforced checks, not from long output formats.

### Added

- `docs/leap-core.md`: the always-loaded rule set (under 650 words). It covers inspect first, the Materiality Gate with No Gate, order of truth, the lightest-workflow ladder with command routing, scope, hard stops with approvers, the four verification states, and handoff. Agent Pack templates embed it verbatim.
- `prompts/leap-validation-standard.md`: a Validation/Handoff standard with a diff-against-scope check, non-goal and acceptance checks, checks run and not run, stop conditions, one verification state, and a decision. It backs the existing `Run LEAP Validation` command.
- `docs/leap-lhs.md`: a one-page LHS stage format (goal, Build Units, paths, dependencies, checkpoint, commit, rollback point).
- `templates/leap-pull-request-template.md` (also installed as this repository's `.github/pull_request_template.md`): a team-facing PR template for scope, verification state, checks not run, and stop conditions.
- `Failed` verification state in `docs/execution-routing.md`.
- `tests/check_framework.py` and a CI workflow: links, anchors, LEAP Core budget and sync with `AGENTS.md` and the Agent Pack, and a define-once guard for the planning hierarchy block.

### Changed

- The planning hierarchy (Mission to Build Unit; Roadmap, Domain, Architecture) is optional. Prompts and briefs link the team's work item and use the full model only when the project already does. The hierarchy is defined in `docs/project-documentation-model.md`; other files link to it instead of restating it.
- Repeated lifecycle, hierarchy, and `Layer` deprecation boilerplate is replaced with links across docs, Prompts, and templates.
- Tool-specific Prompt fields (Codex Plan Mode, User Action Before Agent Submission, E0–E4 capability classes) are optional.
- Long Recon and Charter outputs omit empty sections instead of padding them. Low-value Recon sections are folded into findings and risks, and Recon has an explicit depth limit ("stop when the next safe decision is clear").
- Readiness levels C0–C5 removed; workflows use their own decision lists.
- `README.md`, `docs/00_start_here.md`, `docs/README.md`, `prompts/README.md`, `VERSION.md`, the Quick LEAP Brief, the workflow chooser, and project setup are rewritten around load tiers and the lightest workflow.
- `AGENTS.md` uses LEAP Core in its managed section and the unified `LEAP_MANAGED_SECTION_*` / `LEAP_PROJECT_SECTION_*` markers.
- Corrected stale references claiming the Phase 0 compatibility stubs still exist.
- Reconciled draft PR #19 (semantic routing, Discovery, Pressure Test, native `leap` Skill) and dropped its one-time QA handoff record.

### Removed

- `docs/user/leap-for-humans.md` and `docs/reference/README.md` (merged into `docs/00_start_here.md` and `docs/README.md`).
- `docs/user/when-not-to-use-leap.md` (merged into `docs/user/which-leap-workflow.md`).
- `docs/agent-profiles.md` (merged into `docs/execution-routing.md#8-current-provider-profiles`).
- `docs/maintainer/semantic-routing-qa-handoff.md` (from draft PR #19).

## Unreleased - Materiality Gate and Charter QA corrections

### Added (semantic routing, proposed)

- Added optional semantic workflow routing, help, Discovery and Pressure Test contracts; canonical LEAP SKILL.md and native metadata alignment.
- Added reproducible routing evaluation specifications and a dependency-free static contract validator.


### Fixed

- Clarified independent, composable materiality, discoverability, assumability, and blocker classifications, including the STOP-before-INSPECT routing precedence.
- Added the missing STOP decision and hard-blocker disclosure fields to Charter Materiality Check output.
- Corrected the No Gate copy-ready Charter request so safely assumable material unknowns do not trigger unnecessary questions, while unsafe assumptions and hard blockers cannot bypass checkpoints.
- Corrected duplicate workflow numbering in the Charter request template without changing lifecycle stages or existing paths.

## Unreleased - Capability- and cost-aware execution routing

### Added

- Added `docs/execution-routing.md` as canonical execution-surface routing doctrine.
- Added the Execution Environment Profile for onboarding-time capability, context, cost, quota, permission, and escalation configuration.
- Added E0-E4 capability classes for Reasoning, Remote Mutation, Execution Environment, Agentic Environment, and Human Gate.
- Added explicit verification states: `Implemented — execution unverified`, `Partially verified`, and `Execution verified`.

### Changed

- Required agent/tool selection to follow required confidence, validation, capability, and permission analysis rather than precede it.
- Established least-cost eligible execution surface selection while prohibiting cost optimization from weakening Definition of Done.
- Updated Recon, Prompt generation, templates, onboarding, governance, glossary, and repository guidance to support surface escalation and bounded handoffs.
- Kept provider-specific product names, credits, quotas, subscriptions, and pricing as environment configuration instead of framework architecture.

## Unreleased - Repository Cleanup workflow

### Added

- Added `Run LEAP Cleanup` as a specialized Governance workflow for repository artifact decommissioning.
- Added the cleanup contract, operational Prompt, compact request template, cleanup modes, decommission-set schema, approval gate, and effective-status rules.

### Changed

- Routed approved cleanup execution through LEAP Refactor Prompt and existing Validation/Handoff behavior instead of adding a lifecycle phase.
- Required authority, dependency, consumer, public-path, and canonical-replacement evidence before decommissioning.
- Defined cleanup modes as `archive-only`, `controlled-migration`, and `destructive-cutover`, separate from Agent Execution Mode.
- Established Git history as the default archive for destructive cutovers and required structural, semantic, and behavioral validation where relevant.

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
- Formalized the shared `INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE` decision model.
- Added explicit `Materiality-Gated` and `No Gate` clarification modes.
- Defined `No Gate` as `ASK -> ASSUME + DISCLOSE` only when safe; hard blockers remain `STOP`.
- Made clarification recursive but bounded, with zero questions as a valid and common outcome and no arbitrary minimum question count.
- Aligned Charter, Recon, Prompt generation, request templates, workflow guidance, glossary, and ChatGPT Project setup instructions with the shared behavior.

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
