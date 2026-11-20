<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: adoption-guide
  authority: supporting-adoption-guidance
  applies_to: downstream-projects
END_LEAP_DOC_METADATA
-->

# LEAP Project Setup

Four steps put LEAP in front of your chat assistant and coding agents.

## Step 1: Add LEAP to ChatGPT Project Instructions

Optional; skip it if you only use coding agents. Paste this into the Project Instructions area, followed by the text of [LEAP Core](../leap-core.md) (everything after the `LEAP_CORE_TEXT_BEGIN` marker):

```text
This project uses the LEAP Framework (https://github.com/mcataloe/leap_framework).
Repository to inspect: {{ REPOSITORY HANDLE OR URL }}

When I invoke a LEAP command (LEAP help, Discovery, Pressure Test, Charter,
Recon, Generate/Run Prompt, Generate/Run LHS, Governance, Cleanup,
Validation, Handoff), follow the current framework docs for that workflow.
Do not claim repository inspection happened unless it did.
Preserve my wording unless I ask for rewriting.
End LEAP outputs with a clear decision or recommended next step.

LEAP Core:
<paste docs/leap-core.md text here>
```

The command catalog lives in [semantic routing](../semantic-routing.md). If several assistants or agents are available, you can record an [Execution Environment Profile](../execution-routing.md#2-execution-environment-profile) so LEAP routes each task to the cheapest tool that can run its required checks.

## Step 2: Add AGENTS.md

Install the [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) templates. The pack README has the per-tool locations (Codex, Claude Code) and macOS, Linux, and Windows commands. The result is LEAP Core in every session plus a short project section at the repository root:

```text
my-project/
  AGENTS.md
  README.md
  src/
```

## Step 3: Populate the project section

Run the population prompt that sits next to the template (`AGENTS_Population_Prompt.md`). The agent fills the project section from repository evidence (commands, source-truth docs, project rules, stop conditions with approvers) and marks unknowns `TBD` instead of guessing.

Add the [LEAP pull request template](../../templates/leap-pull-request-template.md) as `.github/pull_request_template.md` so every PR reports scope, verification state, and checks not run.

## Step 4: Run the first LEAP workflow

Most work needs no ceremony: use a normal prompt or a [Quick LEAP Brief](quick-leap-brief.md). When something is unclear:

```text
Run LEAP Recon on <feature, risk, dependency, contract, or design question>.
Run LEAP Charter for this repo.          # only if direction or source truth is unclear
Run LEAP Cleanup on <stale docs or artifacts>.
Run LEAP Validation on <branch or PR>.
```

Add **No Gate** to a request to proceed on disclosed safe assumptions instead of questions. It never overrides a hard stop.

See the [workflow chooser](which-leap-workflow.md) for which to use.
