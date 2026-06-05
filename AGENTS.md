<!--
LEAP_FRAMEWORK_REPO_AGENTS:
  purpose: repo-specific guidance for maintaining the LEAP Framework repository
  source_repo: https://github.com/mjcataldi/leap_framework
  agent_pack_repo: https://github.com/mcataloe/leap_agent_pack
  distributable_template: false
END_LEAP_FRAMEWORK_REPO_AGENTS
-->

# LEAP Framework Repo AGENTS.md

This repository-root `AGENTS.md` is repo-specific guidance for maintaining the LEAP Framework repository. It is not a distributable Agent Pack template.

Canonical distributable AGENTS.md templates live in the dedicated LEAP Agent Pack repository:

```text
https://github.com/mcataloe/leap_agent_pack
```

This file has two main managed sections:

1. **Locked Global Section** - reusable LEAP operating behavior copied from the global AGENTS.md template.
2. **Editable Repository Section** - project-specific AGENTS.md content populated from this repository.

When this file is used in the LEAP Framework repository, the code assistant should treat the locked global section as shared LEAP behavior and the editable repository section as the repository-level maintenance guidance.

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

Project name:

`LEAP Framework`

Project summary:

LEAP - Layered Execution & Alignment Protocol - is a documentation-first software delivery framework for turning rough intent into pressure-tested direction, source-grounded plans, and safe, bounded, implementation-ready AI coding-agent handoffs.

Application type and maturity:

- Type: Markdown framework, prompt library, examples, and framework governance docs.
- Runtime application: None discovered.
- Current repository model: Canonical current docs and flattened current prompt files; older version detail should stay out of active docs unless it applies to the current framework. Use Git history, release notes, and release tags for older context.
- Current active branch at last repo guidance update: `main`; verify with `git status --short --branch` before work.

Primary users and use cases:

- Humans adopting LEAP for AI-assisted software delivery.
- Coding agents that need source-truth discipline, Recon before implementation, bounded prompts, and Validation/Handoff.
- Repo owners adding LEAP AGENTS guidance to local or project repositories.
- Framework maintainers updating Charter, Recon, Prompt, LHS, governance, glossary, and examples.

## Documentation Starting Point

Start with `docs/00_start_here.md` when present.

LEAP Prompt is the instruction artifact family. Use LEAP Recon outputs for focused investigation findings. Use LEAP LHS only when the task needs staged implementation, commit boundaries, tests, docs, compatibility checks, rollback awareness, or multi-area coordination. Do not treat LHS as a mandatory stage after every LEAP Prompt.

Primary product/architecture docs:

- `README.md` - project overview, lifecycle summary, quick-start entry points, and canonical-current repository model.
- `docs/00_start_here.md` - plain-English front door and recommended starting point.
- `docs/leap.md` - canonical framework document and relationship model.
- `docs/leap-charter.md` - canonical Charter, Greenfield/Brownfield, and documentation reconciliation guidance.
- `docs/glossary.md` - terminology source for lifecycle, prompt taxonomy, source truth, and risk terms.
- `prompts/README.md` - prompt library routing and prompt-family guidance.
- `docs/README.md` - documentation domain map and source-of-truth routing.
- `https://github.com/mcataloe/leap_agent_pack` - Agent Pack templates, manifests, install docs, and upgrade guidance.

Canonical docs:

- `docs/leap.md` - Canonical current framework document.
- `docs/leap-charter.md` - Canonical Charter reference.
- `docs/glossary.md` - Canonical terminology reference.
- `prompts/leap-charter-standard.md` - Canonical operational Charter prompt.
- `prompts/leap-recon-standard.md` - Canonical operational Recon prompt.
- `prompts/leap-prompt-standard.md` - Canonical operational Prompt-generation standard.
- `prompts/leap-governance-pass-standard.md` - Canonical governance-pass standard.
- `templates/leap-charter-template.md`, `templates/leap-recon-template.md`, and `templates/leap-prompt-template.md` - current user-facing request templates.

Archived, stale, superseded, or do-not-use docs:

- Release notes policy: `CHANGELOG.md` and `docs/maintainer/release-history.md` should stay focused on current/unreleased changes, the current baseline, and release-notes policy. Do not retain older version-by-version detail in active docs unless the user explicitly asks for it.
- Compatibility stubs: `prompts/leap-phase-0-standard.md` and `templates/leap-phase-0-template.md`. Keep links valid, but prefer Charter files for active work.
- Archive folder: None discovered at population time. If future docs are archived, use the LEAP Charter archive guidance before treating them as current.
- Confirmed active stale/conflicting docs: None discovered during this population pass. Re-check with targeted `rg` searches before taxonomy or source-truth work.

Treat canonical docs as source of truth. Treat archived docs as historical unless a current canonical document explicitly references them.

## Repository Layout

- `README.md` - repository front door and quick-start routing.
- `CHANGELOG.md` - current unreleased changes plus current baseline notes.
- `VERSION.md` - canonical current-file and release notes policy.
- `CONTRIBUTING.md` - lightweight contribution guidance.
- `docs/` - framework docs, adoption docs, glossary, risk guidance, and examples.
- `prompts/` - copy-ready operational LEAP prompts.
- `templates/` - compact framework request templates.
- `examples/` - assistant prompt examples.
- Frontend path: Not applicable; no frontend application discovered.
- Backend/API path: Not applicable; no backend service discovered.
- Tests path: TBD - Project owner: should this repo add markdown/link validation tests or keep manual validation only?
- Scripts path: TBD - Project owner: should this repo include validation scripts for Markdown links and terminology checks?
- Infrastructure path: Not applicable; no infrastructure-as-code or deployment config discovered.

## Technology Stack

- Framework content: Markdown.
- Version control: Git.
- Frontend: Not applicable.
- Backend/API: Not applicable.
- Database/storage/queue/cache: None discovered.
- External services: None required by repository evidence.
- Infrastructure/deployment: None discovered.
- Package manager: None discovered.
- Test framework: None discovered.
- Runtime versions: None discovered.

Use the existing stack unless the user explicitly requests evaluation or migration.

## Infrastructure and External Dependencies

- Database: None discovered.
- Storage: None discovered.
- Queue/cache: None discovered.
- External services: None discovered.
- Deployment target: TBD - Project owner: is this repository published only through GitHub, or is there a docs site/release process to document?
- CI/CD: TBD - no `.github/`, workflow, or build configuration discovered.

## Setup Commands

```bash
# No install command discovered.
```

```bash
# No local dev server command discovered.
```

```bash
# No database setup or migration command discovered.
```

Do not invent setup commands. If a future package, docs site, or validation tool is added, update this section from repository evidence.

## Development Commands

```bash
# No development server or watch command discovered.
```

For documentation-only edits, use normal editor/Git workflows plus the validation searches below.

## Validation Commands

```bash
# Format command: TBD - no formatter config discovered.
```

```bash
# Lint command: TBD - no markdown lint config discovered.
```

```bash
# Typecheck command: Not applicable unless tooling is added.
```

```bash
# Test command: TBD - no test framework discovered.
```

```bash
# Build command: TBD - no docs build config discovered.
```

Practical manual validation for framework/documentation changes:

```bash
rg -n "LEAP LHS|LHS|Layered House Standard|LEAP Prompt|LEAP Charter|LEAP Recon|Review|Validation|Handoff|Phase 0" .
```

```bash
rg -n "\]\(([^)#]+\.md)(#[^)]+)?\)" README.md docs prompts templates examples CHANGELOG.md VERSION.md CONTRIBUTING.md
```

## LEAP Charter Rules

Use LEAP Charter when project direction, roadmap, source-truth status, documentation structure, implementation posture, or brownfield reconciliation is unclear.

Brownfield Charter policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

During Charter work:

- Identify canonical, supporting, stale, conflicting, duplicate, and archived docs.
- Compare docs against repo reality when applicable.
- Produce or update a gap register and prompt backlog.
- Preserve legacy docs in an archive when superseded.
- Avoid runtime implementation changes unless explicitly requested.
- Capture risky code, schema, API, UI, auth, workflow, or infrastructure work as follow-up LEAP Recon, LEAP Prompt, or LEAP LHS recommendations.
- For this repo, Charter work is normally documentation/framework reconciliation, prompt-standard reconciliation, AGENTS-template reconciliation, and link/source-truth validation.
- Do not move, archive, or rename docs during AGENTS population unless explicitly requested.
- Do not treat the compatibility Phase 0 stubs as active front doors; prefer LEAP Charter files.

Greenfield Charter expectations for this repo:

- Use only when creating a new LEAP-managed example, template family, or documentation foundation.
- Keep early product/framework shaping lightweight unless staged repo/docs foundation work is clearly needed.

Brownfield Charter expectations for this repo:

- Start as discovery and reconciliation.
- Verify current canonical docs, prompt standards, templates, and AGENTS templates before editing.
- Do not preserve older `Phase 0` release-note detail in active docs by default. Use Git history and release tags for older release context unless the user explicitly asks for a historical reconstruction.
- Use LHS only after the documentation reorganization or taxonomy plan is clear and staged execution reduces risk.

## LEAP Recon Rules

Use LEAP Recon for focused investigation before implementation or broad doc changes.

Recon for this repo should usually inspect:

- `README.md`
- `docs/00_start_here.md`
- `docs/leap.md`
- `docs/leap-charter.md`
- `docs/glossary.md`
- `prompts/README.md`
- relevant files in `prompts/` and `templates/`
- `CHANGELOG.md`, `VERSION.md`, and `docs/maintainer/release-history.md` when current release policy or baseline terminology is involved

Recon is normally investigative and non-mutating unless the user explicitly authorizes edits. It may recommend Standard LEAP Prompts or LHS prompts when staged documentation changes are warranted.

## LEAP Prompt / Implementation Handoff Rules

LEAP Prompt is the instruction artifact family for this repo. Generated prompts should state the prompt type, such as Standard LEAP Prompt, LHS Prompt, Fix Prompt, Refactor Prompt, Governance Prompt, Validation Prompt, or another clear type.

Implementation in this repo normally means Markdown, prompt, example, or AGENTS-template edits. Do not make runtime application changes because no runtime application is present.

Use LEAP LHS only when implementation gravity warrants staged execution, such as coordinated changes across framework docs, prompt standards, templates, AGENTS templates, changelog, and link validation. Do not treat LHS as a mandatory stage after every LEAP Prompt.

Complete Validation/Handoff after implementation by summarizing files changed, checks run or not run, docs touched, source-truth risks, and recommended follow-up Charter, Recon, Prompt, or LHS work.

## Project Source of Truth

Use this order of truth:

1. Explicit user instruction for the current task.
2. System/developer/tool instructions and the locked global section of this `AGENTS.md`.
3. The editable repo section of this `AGENTS.md` and any closer-scoped agent instruction files.
4. Current repo reality: files present, Git status, branch state, and current diffs.
5. `docs/00_start_here.md`.
6. `README.md`, `docs/leap.md`, `docs/leap-charter.md`, and `docs/glossary.md`.
7. `prompts/README.md` and current files under `prompts/`.
8. Current files under `templates/`.
9. `CONTRIBUTING.md` and `VERSION.md`.
10. `CHANGELOG.md` and `docs/maintainer/release-history.md` for current release notes and release policy only.
11. Archived, stale, or compatibility docs only when explicitly referenced by canonical docs.
12. Reasonable inference from nearby patterns, clearly labeled as inference.

If these conflict, call out the conflict and prefer the more specific, more recent, and safer source.

## Architecture Rules

Follow the project's existing architecture. Prefer incremental extension over replacement. Avoid broad rewrites unless the user requested a refactor.

Project-specific architecture constraints:

- Keep active framework docs on canonical current paths instead of reintroducing nested versioned active files.
- Keep current operational prompts as flattened files under `prompts/`.
- Preserve compatibility stubs for old Phase 0 paths unless the user explicitly requests removal and a migration plan.
- Keep examples and templates aligned with canonical lifecycle language.
- Keep release notes streamlined; remove older version-by-version detail from active docs unless it is explicitly needed for compatibility or current decision-making.

## Data and Migration Rules

Preserve existing data unless destructive changes are explicitly allowed. Inspect existing models and migrations before changing schemas, migrations, seed data, or persistence behavior.

Project-specific data rules:

- Not applicable to runtime data; no database, migrations, queues, cache, or storage layer discovered.
- Treat docs, templates, prompts, and examples as framework artifacts that need traceability.
- Do not delete, rename, or archive docs without explicit scope and link validation.

## API and Contract Rules

Preserve backward compatibility unless explicitly told otherwise. Update shared types, validation, tests, and docs together when contracts change.

Project-specific contract rules:

- Public-facing contracts are documentation paths, prompt names, template names, headings, lifecycle terms, and AGENTS marker conventions.
- Preserve existing Markdown links or provide compatibility stubs when paths are renamed.
- Do not modify AGENTS boundary markers unless explicitly requested.

## UI/UX Rules

Follow existing component and styling patterns. Preserve user-entered data. Make loading, success, error, and empty states explicit.

Project-specific UX rules:

- Not applicable to a runtime UI; this repo has no frontend application.
- For docs, keep language concise, practical, and navigable.
- Prefer stable filenames and clear headings that work for both humans and LLMs.

## AI / Automation Rules

Keep AI outputs reviewable by the user. Preserve traceability to source material where applicable. Do not fabricate facts or automate irreversible user-facing actions without review.

Project-specific AI rules:

- Separate verified repo evidence from inference.
- Mark unknown commands, tooling, architecture, or workflow as `TBD` instead of inventing them.
- During Charter work, recommend Recon or Prompt follow-ups instead of risky implementation changes.
- When editing prompts or templates, keep agent stop conditions and source-truth hierarchy explicit.

## Security and Privacy Rules

Never commit secrets, weaken authentication, bypass validation, expose sensitive data, add third-party services without approval, or change security-sensitive behavior without calling it out.

Project-specific security/privacy rules:

- No secrets or credentials are required for normal repository work.
- Do not add API keys, tokens, private paths, personal data, or environment-specific secrets to docs, prompts, templates, or examples.
- Do not introduce external services, paid services, telemetry, or automation dependencies without explicit approval.

## Documentation Expectations

Update docs when changes affect product behavior, user workflows, API contracts, data models, setup, commands, environment variables, architecture, layer status, or roadmap assumptions.

Project-specific docs to keep aligned:

- `README.md`
- `docs/00_start_here.md`
- `docs/leap.md`
- `docs/leap-charter.md`
- `docs/glossary.md`
- `prompts/README.md`
- `prompts/leap-charter-standard.md`
- `prompts/leap-recon-standard.md`
- `prompts/leap-prompt-standard.md`
- `prompts/leap-governance-pass-standard.md`
- `templates/leap-charter-template.md`
- `templates/leap-recon-template.md`
- `templates/leap-prompt-template.md`
- Agent Pack repository at `https://github.com/mcataloe/leap_agent_pack` when AGENTS.md templates, manifests, install docs, or upgrade guidance are involved.

Doc classification at population time:

| Path | Status | Notes |
| --- | --- | --- |
| `docs/leap.md` | Canonical | Current framework document. |
| `docs/leap-charter.md` | Canonical | Charter and brownfield reconciliation doctrine. |
| `docs/glossary.md` | Canonical | Term definitions. |
| `README.md` | Canonical entry point | Repository overview and routing. |
| `docs/00_start_here.md` | Canonical entry point | Plain-English first read. |
| `docs/README.md` | Canonical docs map | Documentation domains and authority routing. |
| `docs/reference/README.md` | Supporting | Current root-level reference docs map. |
| `prompts/README.md` | Canonical supporting | Prompt-family routing. |
| `docs/maintainer/framework-doc-governance.md` | Supporting | Documentation domain and move governance. |
| Current `prompts/leap-*-standard.md` files except Phase 0 stub | Canonical operational prompts | Active prompt standards. |
| Current `templates/leap-*-template.md` files except Phase 0 stub | Canonical templates | Active user request templates. |
| `CONTRIBUTING.md` | Supporting | Contribution behavior. |
| `VERSION.md` | Supporting | Canonical file and release-history notes. |
| `docs/agent-profiles.md`, `docs/risk-taxonomy.md`, `docs/user/leap-for-humans.md`, `docs/user/quick-leap-brief.md` | Supporting | Adoption and risk guidance. |
| `CHANGELOG.md`, `docs/maintainer/release-history.md` | Current release notes and release policy | Older version detail belongs in Git history and release tags unless explicitly needed. |
| `prompts/leap-phase-0-standard.md`, `templates/leap-phase-0-template.md` | Compatibility stubs | Keep for old links; do not prefer for active work. |

## Stop Conditions

Stop and ask before:

- Destructive schema or data changes unless the project explicitly allows them.
- Changing auth/session/ownership rules.
- Changing public API contracts in a breaking way.
- Adding paid services or external integrations.
- Introducing new production dependencies.
- Removing major existing functionality.
- Replacing established architecture.
- Implementing unclear business rules with material product impact.
- Treating archived docs as current source truth.
- Weakening privacy, traceability, auditability, or security controls.

Project-specific stop conditions:

- Any task requires editing the locked global section of root `AGENTS.md` or changing section boundary markers.
- A task would modify files outside the explicitly approved scope.
- A task requires runtime code, tests, product docs, or configuration changes during AGENTS population.
- Active docs conflict on the current lifecycle, prompt taxonomy, Charter/Brownfield policy, or LHS placement.
- A proposed change would remove compatibility stubs without an approved migration plan.
- A proposed change would invent setup, test, build, deployment, service, or credential assumptions not supported by repo evidence.
- A proposed change would add dependencies, generated navigation, CI, docs-build tooling, or external services without explicit approval.
- A task requires deleting, moving, or archiving docs without a Brownfield reconciliation plan.

## Branch, Worktree, PR, and Commit Conventions

- Default branch context at last guidance update: `main`; verify before work.
- Run `git status --short --branch` before edits and before final handoff.
- Preserve user changes. Do not reset, checkout, or discard unowned work.
- Do not commit unless the user explicitly asks for a commit.
- If the user supplies a commit message, use it exactly.
- Keep documentation changes focused and avoid broad rewrites unless the task is explicitly a reconciliation pass.

## Known Unknowns

- TBD - Project owner: should this repo add a formal Markdown lint command?
- TBD - Project owner: should this repo add a Markdown link-check command or script?
- TBD - Project owner: should this repo have CI for terminology drift and link validation?
- Resolved: root `AGENTS.md` remains committed as LEAP Framework repo-specific guidance. Distributable AGENTS templates live in `https://github.com/mcataloe/leap_agent_pack`.
- TBD - Project owner: should `docs/99_archive/` be created now or only when real framework docs are archived?

## Completion Requirements

A task is complete when the requested behavior is implemented, relevant checks were run or explained, docs were updated if needed, risks and follow-ups are called out, and Validation/Handoff includes follow-up LEAP Recon, LEAP Prompt, or LEAP LHS recommendations when needed.

<!-- LEAP_MASTER_REPO_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->

<!--
Optional local team or developer-specific notes go here.
Keep durable project guidance in the editable repository section above.
-->

<!-- LEAP_LOCAL_OVERRIDES_END -->
