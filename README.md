# LEAP Framework

**LEAP (Layered Execution & Alignment Protocol)** keeps coding agents and teams on track: grounded in repository evidence, bounded in scope, and honest about what was verified. It aims for enough guardrails and no ceremony beyond that.

New to LEAP? Read [Start Here](docs/00_start_here.md).

## Basic setup

1. Install the [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) `AGENTS.md` templates. They put [LEAP Core](docs/leap-core.md) in every agent session, plus a short section for your project's own rules.
2. Run the Agent Pack population prompt in your coding agent to fill the project section from repository evidence.
3. Add the [LEAP pull request template](templates/leap-pull-request-template.md) to `.github/pull_request_template.md`.
4. Optional: add LEAP to ChatGPT Project Instructions using [LEAP Project Setup](docs/user/leap_project_setup.md#step-1-add-leap-to-chatgpt-project-instructions).

## How LEAP is organized

| Tier | Loaded | Contents |
|---|---|---|
| 0 | Always | [LEAP Core](docs/leap-core.md) and the repository's `AGENTS.md` project section |
| 1 | On demand | [Quick LEAP Brief](docs/user/quick-leap-brief.md), [Recon Lite](templates/leap-recon-lite-template.md), [Validation/Handoff](prompts/leap-validation-standard.md) |
| 2 | When the work needs it | [Charter](docs/leap-charter.md), [Recon](prompts/leap-recon-standard.md), [LEAP Prompt](prompts/leap-prompt-standard.md), [LHS](docs/leap-lhs.md), [Cleanup](docs/repository-cleanup.md), [Skills](docs/leap-skills.md), [Execution routing](docs/execution-routing.md), [Project documentation model](docs/project-documentation-model.md) |

Lifecycle, when the full path is warranted:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Most work enters partway through. Use the lightest workflow that controls the risk; see the [workflow chooser](docs/user/which-leap-workflow.md). Say **LEAP help** to an agent for the [command catalog](docs/semantic-routing.md).

## References

- [Framework reference](docs/leap.md) and [Glossary](docs/glossary.md)
- [Documentation map](docs/README.md) and [Prompt library](prompts/README.md)
- Templates: [Charter](templates/leap-charter-template.md), [Recon](templates/leap-recon-template.md), [Recon Lite](templates/leap-recon-lite-template.md), [Prompt](templates/leap-prompt-template.md), [Cleanup](templates/leap-cleanup-template.md), [Skill](templates/leap-skill-template.md), [Pull request](templates/leap-pull-request-template.md)
- Optional baseline metadata: [example](examples/leap.baseline.yaml) and [schema](schemas/leap.baseline.schema.json)

The former Phase 0 entry points (`prompts/leap-phase-0-standard.md`, `templates/leap-phase-0-template.md`) were removed; use the Charter files above.

## Repository structure

```text
AGENTS.md            maintainer guidance (LEAP Core + framework rules)
docs/                doctrine, user and maintainer guides, examples
prompts/             operational Prompt standards
templates/           request, Skill, and pull request templates
skills/leap/         optional native LEAP navigator Skill
examples/, schemas/  example artifacts and permissive metadata schemas
tests/               dependency-free checks and routing evaluation cases
```

## Maintainer notes

- Define each concept once and link to it. `docs/leap-core.md` stays under 650 words.
- Run `python3 tests/check_framework.py --agent-pack ../leap_agent_pack` before opening a PR; CI runs the same checks.
- Distributable `AGENTS.md` templates, install, and upgrade guidance live in the [Agent Pack](https://github.com/mcataloe/leap_agent_pack). Merge framework changes first.
- Use Git history, release notes, and tags for older context.
