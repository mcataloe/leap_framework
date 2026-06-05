# LEAP Framework

**LEAP - Layered Execution & Alignment Protocol** is a software delivery framework for turning rough intent into pressure-tested direction, source-grounded plans, and safe, bounded, implementation-ready AI coding-agent handoffs.

The active repository presents the current canonical LEAP framework document and current operational prompts without versioned filenames. Older version detail is intentionally kept out of active docs unless it applies to the current framework; use Git history, release notes, and release tags for older context.

LEAP AGENTS.md templates are distributed from the dedicated [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) repository. The Agent Pack owns the Codex/AGENTS.md execution adapter so downstream projects can pin stable agent instructions independently from LEAP Framework methodology updates.

## Basic Setup

1. Add LEAP to ChatGPT Project Instructions using [LEAP Project Setup](docs/user/LEAP_PROJECT_SETUP.md#step-1-add-leap-to-chatgpt-project-instructions).
2. Add the Agent Pack `AGENTS.md` template from the [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) to your project root.
3. Run the Agent Pack population prompt in Codex.
4. Ask ChatGPT:

```text
Run LEAP Recon on {{what you want to build or understand}}.
```

## Start Here

- New to LEAP: read [Start Here: LEAP in Plain English](docs/00_start_here.md).
- Choosing a workflow: use [Which LEAP Workflow Should I Use?](docs/user/which-leap-workflow.md).
- Deciding whether LEAP is too much: read [When Not to Use LEAP](docs/user/when-not-to-use-leap.md).
- Small agent-executed task: use the [Quick LEAP Brief](docs/user/quick-leap-brief.md).
- Setting up LEAP in a ChatGPT/Codex project: follow [LEAP Project Setup](docs/user/leap_project_setup.md).
- Looking for the docs map: use [LEAP Documentation Map](docs/README.md).

## Canonical References

- [LEAP Framework](docs/leap.md) - canonical current framework document
- [LEAP Charter](docs/leap-charter.md) - Charter modes and brownfield documentation reconciliation
- [Materiality Gate](docs/materiality-gate.md) - question, assumption, and inspect-first discipline
- [Dependency & Contract Recon](docs/dependency-contract-recon.md) - dependency register and contract-drift Recon guidance
- [Glossary](docs/glossary.md) - canonical terminology reference
- [Prompt Library](prompts/README.md) - operational prompt routing

## Prompt and Template Entry Points

- [LEAP Charter template](templates/leap-charter-template.md) - start a new product, major direction, or brownfield reconciliation
- [LEAP Recon Lite template](templates/leap-recon-lite-template.md) - request a short focused Recon
- [LEAP Recon template](templates/leap-recon-template.md) - request a fuller focused Recon
- [LEAP Prompt template](templates/leap-prompt-template.md) - generate implementation-ready instructions
- [Operational prompts](prompts/README.md) - reusable prompt standards for recurring LEAP work

Compatibility stubs remain at `templates/leap-phase-0-template.md` and `prompts/leap-phase-0-standard.md` for older links. Prefer Charter files for active work.

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
  materiality-gate.md
  dependency-contract-recon.md
  glossary.md
  user/
    leap_project_setup.md
    leap-for-humans.md
    quick-leap-brief.md
    when-not-to-use-leap.md
    which-leap-workflow.md
  reference/
  maintainer/
examples/
schemas/
templates/
prompts/
```

## Maintainer Notes

- Keep active framework docs on canonical current paths.
- Keep operational prompts as flattened files under `prompts/`.
- Keep release notes focused on current and unreleased changes.
- Use Git history, release notes, and release tags for older version context.
- Use the separate [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) repository for distributable AGENTS.md templates, manifests, install docs, and upgrade guidance.
