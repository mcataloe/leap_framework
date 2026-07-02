# LEAP Framework

**LEAP - Layered Execution & Alignment Protocol** is a software delivery framework for turning rough intent into pressure-tested direction, source-grounded plans, and safe, bounded, implementation-ready coding-agent handoffs.

The active repository presents current canonical framework documentation and operational prompts without versioned filenames. Use Git history, release notes, and release tags for older context.

LEAP `AGENTS.md` templates are distributed from the dedicated [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) repository.

## Basic Setup

1. Add LEAP to ChatGPT Project Instructions using [LEAP Project Setup](docs/user/leap_project_setup.md#recommended-full-project-instructions).
2. Add the Agent Pack repo-level `AGENTS.md` template to the project root.
3. Run the Agent Pack repo population prompt in the coding agent.

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is the Layered House Standard Prompt format for staged implementation. It is not a mandatory lifecycle stage.

## Project Documentation Model

The preferred traceability hierarchy is:

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

Roadmaps schedule and prioritize work. Domains describe persistent responsibility boundaries. Architecture describes technical structure.

Several Initiatives may run in parallel. A Roadmap does not permanently own Initiative identity. Delivery Units may be collapsed for small work, and Build Units are not necessarily independently deployable.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level. The LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references remain valid.

See:

- [Project Documentation Model](docs/project-documentation-model.md)
- [Legacy Project Documentation Migration](docs/maintainer/project-documentation-migration.md)

## Start Here

- New to LEAP: [Start Here: LEAP in Plain English](docs/00_start_here.md)
- Choosing a workflow: [Which LEAP Workflow Should I Use?](docs/user/which-leap-workflow.md)
- Deciding whether LEAP is too much: [When Not to Use LEAP](docs/user/when-not-to-use-leap.md)
- Small agent-executed task: [Quick LEAP Brief](docs/user/quick-leap-brief.md)
- Setting up LEAP: [LEAP Project Setup](docs/user/leap_project_setup.md)
- Documentation map: [LEAP Documentation Map](docs/README.md)

## Canonical References

- [LEAP Framework](docs/leap.md)
- [LEAP Charter](docs/leap-charter.md)
- [Project Documentation Model](docs/project-documentation-model.md)
- [Glossary](docs/glossary.md)
- [Materiality Gate](docs/materiality-gate.md)
- [Dependency & Contract Recon](docs/dependency-contract-recon.md)
- [Prompt Library](prompts/README.md)
- [Legacy Project Documentation Migration](docs/maintainer/project-documentation-migration.md)
- Optional baseline metadata: [example](examples/leap.baseline.yaml) and [schema](schemas/leap.baseline.schema.json)

## Prompt and Template Entry Points

- [LEAP Charter template](templates/leap-charter-template.md)
- [LEAP Recon Lite template](templates/leap-recon-lite-template.md)
- [LEAP Recon template](templates/leap-recon-template.md)
- [LEAP Prompt template](templates/leap-prompt-template.md)
- [Operational prompts](prompts/README.md)

Compatibility stubs remain at `templates/leap-phase-0-template.md` and `prompts/leap-phase-0-standard.md`. Prefer Charter files for active work.

## Repository Structure

```text
README.md
CHANGELOG.md
CONTRIBUTING.md
VERSION.md
AGENTS.md
docs/
  00_start_here.md
  README.md
  leap.md
  leap-charter.md
  project-documentation-model.md
  materiality-gate.md
  dependency-contract-recon.md
  glossary.md
  user/
  reference/
  maintainer/
  examples/
examples/
schemas/
templates/
prompts/
```

## Maintainer Notes

- Keep active framework docs on canonical current paths.
- Keep operational prompts as flattened files under `prompts/`.
- Preserve public paths unless migration is explicitly approved.
- Keep release notes focused on current and unreleased changes.
- Use Git history, release notes, and tags for older context.
- Use the separate Agent Pack repository for distributable `AGENTS.md` templates, manifests, install docs, and upgrade guidance.
