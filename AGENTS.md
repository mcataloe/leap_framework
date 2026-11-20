<!--
LEAP_FRAMEWORK_REPO_AGENTS:
  purpose: repo-specific guidance for maintaining the LEAP Framework repository
  source_repo: https://github.com/mcataloe/leap_framework
  agent_pack_repo: https://github.com/mcataloe/leap_agent_pack
  agent_pack_template: combined 0.2.0-candidate.2
  distributable_template: false
END_LEAP_FRAMEWORK_REPO_AGENTS
-->

# LEAP Framework Repo AGENTS.md

Guidance for maintaining the LEAP Framework repository. This file is not a distributable template; those live in the [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack). The managed section is the current [LEAP Core](docs/leap-core.md), synced from the Agent Pack combined template.

<!-- LEAP_MANAGED_SECTION_BEGIN -->

# LEAP Core

Canonical source: https://github.com/mcataloe/leap_framework/blob/main/docs/leap-core.md

## Purpose

LEAP keeps agent-assisted work grounded in repository evidence, bounded in scope, and honest about verification. Use the lightest workflow that controls the risk. For small, clear work, zero questions and zero ceremony are normal.

## Instruction priority

1. System, developer, and tool instructions.
2. Explicit user instructions for the current task.
3. Repository and closer-scoped `AGENTS.md` files.
4. This LEAP Core.
5. Existing code, tests, docs, and conventions.

When instructions conflict, prefer the more specific, current, and safer one.

## Inspect first; ask only what matters

- Inspect discoverable evidence (code, tests, docs, history) before asking.
- For each open question: answer it from evidence, proceed on a stated safe assumption, ask, or stop.
- Ask only when the answer would change the work. Batch questions. Zero questions is normal.
- `No Gate` means proceed on disclosed safe assumptions. It never overrides a hard stop.
- Stop investigating when the next safe decision is clear.

## Order of truth

Current code, tests, schemas, and migrations outrank docs. Canonical docs outrank drafts. Archived or superseded docs and old plans are history, not current truth. Call out conflicts; do not silently pick one.

## Pick the lightest workflow

| Situation | Use |
|---|---|
| Tiny, obvious change | Do it; report what changed and what was checked |
| Small, clear task | Quick LEAP Brief: goal, scope, non-goals, checks |
| Repo reality, risk, or design is unclear | `Run LEAP Recon` (Recon Lite when narrow) |
| Exploring a domain or challenging an idea | `Run LEAP Discovery` / `Run LEAP Pressure Test` |
| Direction, source truth, or doc structure is unclear | `Run LEAP Charter` |
| Bounded instructions for an agent | `Generate LEAP Prompt` (LHS only when staging reduces risk) |
| Obsolete or competing artifacts | `Run LEAP Cleanup`: discovery only until the exact set is approved |
| Documentation or adoption drift | `Run LEAP Governance` |
| Finished or handed-off work | `Run LEAP Validation` |

`LEAP help` lists commands: https://github.com/mcataloe/leap_framework/blob/main/docs/semantic-routing.md. Explicit commands win over inferred intent. Exploring, Recon, Charter, Discovery, and generating a Prompt never authorize changes.

## Scope

- Stay inside the stated scope. Respect non-goals and do-not-touch paths.
- Reuse existing patterns. No unrelated cleanup.
- Do not invent product rules or decisions. Mark unknowns `TBD` with the exact question for the owner.
- Never weaken or delete tests to make them pass.
- Link the governing ticket, issue, or plan when one exists. Use the full LEAP planning model (Strategic Outcome, Initiative, Delivery Unit, Build Unit) only when the project already uses it.

## Hard stops

Stop and ask before:

- destructive or irreversible data changes, including edits to applied migrations
- auth, permission, security, privacy, billing, or identity changes
- breaking public contracts, APIs, schemas, or paths
- new dependencies, paid services, or major Architecture replacement
- treating archived docs as current truth
- irreversible Git operations or discarding work you do not own
- any repository-specific stop condition

Approval comes from the user or the owner the repository names.

## Honest verification

Run the most relevant checks the repository defines. Choose the cheapest tool or surface that can actually run them; never weaken the Definition of Done to save cost. Report exactly one state:

- **Execution verified**: every required check ran and passed.
- **Partially verified**: named required checks are still pending.
- **Implemented — execution unverified**: required checks did not run.
- **Failed**: a required check failed, or the diff exceeds scope or crosses a hard stop.

Never call work complete when required checks did not run.

## Handoff

Report files changed, scope deviations, checks run with results, checks not run and why, verification state, stop conditions hit, and follow-ups. `Run LEAP Validation` is the full standard.

<!-- LEAP_MANAGED_SECTION_END -->

<!-- LEAP_PROJECT_SECTION_BEGIN -->

# Project Guidance - LEAP Framework

## Project

- Name: LEAP Framework
- Summary: Markdown doctrine, operational Prompts, templates, and examples for keeping agent-assisted software delivery on track with guardrails and minimal ceremony.
- Start here: `docs/00_start_here.md`
- Work tracking: GitHub issues and PRs on `mcataloe/leap_framework`. Distributable `AGENTS.md` templates live in `mcataloe/leap_agent_pack`.

## Source truth

- Always-loaded rules: `docs/leap-core.md`. Change it here first, then propagate to the Agent Pack.
- Canonical doctrine: `docs/leap.md`, `docs/project-documentation-model.md`, `docs/execution-routing.md`, `docs/semantic-routing.md`, `docs/glossary.md`, and the standards in `prompts/`.
- Supporting: `docs/user/`, `docs/maintainer/`, `templates/`. Examples are illustrative, not source truth.
- Release state: `CHANGELOG.md` and `VERSION.md`.
- The former Phase 0 entry points were removed in favor of the Charter files. Do not recreate them.

## Layout

- `docs/`: doctrine, user and maintainer guidance, examples
- `prompts/`: operational Prompt standards
- `templates/`: request, Skill-definition, and pull request templates
- `skills/leap/`: the optional native LEAP navigator Skill
- `examples/`, `schemas/`: example artifacts and permissive metadata schemas
- `tests/`: dependency-free validation scripts and routing evaluation cases

## Commands

```bash
python3 tests/check_framework.py                       # links, anchors, LEAP Core budget
python3 tests/check_framework.py --agent-pack ../leap_agent_pack   # plus Core drift vs the pack
python3 tests/validate_semantic_router.py --agent-pack ../leap_agent_pack
```

Both scripts use only the Python standard library. CI runs them on every push and pull request.

## Project rules

- Keep each concept defined in one canonical place and link to it. Do not restate the planning hierarchy, lifecycle, or Layer guidance in other files.
- Keep `docs/leap-core.md` under 650 words. A new Core rule must name the real failure it prevents.
- `Layer`: classify each use as framework name, LHS name, qualified Architecture term, Phase, legacy reference, historical example, or unresolved planning term. Never globally replace it. Guidance: `docs/maintainer/project-documentation-migration.md`.
- Tool-specific detail (Codex, Claude Code, others) belongs in optional profiles, not in required Prompt fields.
- Record every behavior change in `CHANGELOG.md`.

## Project stop conditions

- Renaming or removing a public doc, Prompt, or template path: approver repository owner (mcataloe)
- Changing `AGENTS.md` marker names or the LEAP Core text: approver repository owner, with a matching Agent Pack change
- Adding a dependency, docs generator, or external service: approver repository owner

## Branches and commits

- Default branch is `main`. Use focused commits and one PR per repository.
- Keep framework and Agent Pack commits separate. When distributable guidance changes, open the matching Agent Pack PR and merge the framework first.
- Do not create release tags unless asked.

<!-- LEAP_PROJECT_SECTION_END -->

<!-- LEAP_LOCAL_OVERRIDES_BEGIN -->
<!-- Optional local team or developer notes. Keep durable project guidance in the project section. -->
<!-- LEAP_LOCAL_OVERRIDES_END -->
