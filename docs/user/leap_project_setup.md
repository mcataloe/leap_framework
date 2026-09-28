<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: adoption-guide
  authority: supporting-adoption-guidance
  applies_to: downstream-projects
END_LEAP_DOC_METADATA
-->

# LEAP Project Setup

LEAP helps ChatGPT and coding agents understand your project before they suggest or make changes.

Follow these four steps.

## Step 1: Add LEAP to ChatGPT Project Instructions

Paste this into the Project Instructions area:

```text
This project uses the LEAP Framework.

Use the current LEAP Framework documentation at
https://github.com/mcataloe/leap_framework as the governing framework
source when repository access is available.

The project repository to inspect is:
{{ INSERT REPOSITORY HANDLE OR ACCESSIBLE URL HERE }}

When I invoke commands such as Run LEAP Charter, Run LEAP Recon,
Generate LEAP Prompt, Run LEAP Prompt, Generate LEAP LHS,
Run LEAP LHS, Run LEAP Governance, Run LEAP Cleanup, Run LEAP Validation, or
Run LEAP Handoff, use LEAP Framework behavior.

Treat the lifecycle as:
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff

Use this project-documentation hierarchy when strategically material:
Mission / Project Charter -> Strategic Outcome -> Initiative -> Delivery Unit -> Build Unit

Treat Roadmap as timing, priority, milestones, dependencies, release targets,
status, and parallelism. Do not treat Roadmap placement as permanent Initiative identity.

Treat Domains as persistent responsibility boundaries with a many-to-many
relationship to Initiatives. Treat Architecture as technical structure.

Allow Delivery Unit to collapse for small work. Do not define Build Units as
necessarily independently deployable.

Generic project-planning Layer is legacy-compatible and deprecated as the
preferred planning level. Preserve the LEAP name, Layered House Standard,
LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.
Classify legacy Layer meaning before migration.

Preserve my wording unless I ask for rewriting. Use the required LEAP headings.
Inspect source-truth docs, repo reality, branches, worktrees, pull requests,
existing functionality, dependencies, and contracts when available.

Do not claim repository inspection happened unless it actually happened.
Do not generate implementation Prompts prematurely.

Apply Materiality Gate: inspect discoverable sources first, ask only questions
that materially change the work, proceed on stated assumptions for non-material
unknowns, and stop for unsafe source truth, destructive changes, privacy,
security, money, identity, legal exposure, user trust, or unapproved Architecture.

Always end LEAP outputs with a clear gate decision or recommended next step.
```

## Command behavior

| Command | Expected behavior |
|---|---|
| `Run LEAP Charter` | Establish or reconcile Mission, Strategic Outcomes, Initiative identity, Roadmap, Domains, Architecture, source truth, and implementation posture. |
| `Run LEAP Recon` | Investigate a focused Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, risk, dependency, contract, or legacy Layer. |
| `Generate LEAP Prompt` | Create an agent-ready Prompt only after traceability, source truth, repo reality, scope, validation, stop conditions, and execution configuration are clear. |
| `Run LEAP Prompt` | Execute an approved Prompt according to its scope, constraints, validation, and stop conditions. |
| `Generate LEAP LHS` | Create a staged Layered House Standard Prompt when implementation gravity warrants several Build Units or integration checkpoints. |
| `Run LEAP LHS` | Execute an approved LHS Prompt according to its Delivery Unit and Build Unit sequence. |
| `Run LEAP Governance` | Reconcile framework, repository, docs, terminology, source truth, or adoption drift. |
| `Run LEAP Cleanup` | Inventory and classify obsolete artifacts, inspect references and replacements, and return an exact proposed decommission set for approval. |
| `Run LEAP Validation` | Verify completed work against scope, acceptance, tests, docs, and stop conditions. |
| `Run LEAP Handoff` | Summarize work, unresolved risks, validation, deviations, and follow-up. |

## Step 2: Add AGENTS.md to the project root

Use the repository-level template from the LEAP Agent Pack:

```text
https://github.com/mcataloe/leap_agent_pack/blob/main/repo/AGENTS.md
```

Example:

```text
my-project/
  AGENTS.md
  README.md
  src/
  package.json
```

`AGENTS.md` teaches the coding agent how to work in the specific repository.

It should include a small LEAP Baseline State summary. Larger or drift-prone projects may use optional `leap.baseline.yaml` metadata created through an authorized Charter, Governance, or baseline setup pass.

## Step 3: Run the AGENTS.md population Prompt

Use:

```text
https://github.com/mcataloe/leap_agent_pack/blob/main/repo/AGENTS_Population_Prompt.md
```

The agent should inspect real repository evidence and mark unknowns as `TBD` instead of guessing.

When a LEAP Prompt includes a User Action Before Codex Submission section, set Codex Plan Mode to the requested value before submission. Codex Plan Mode is separate from LEAP Execution Mode.

## Step 4: Run the first LEAP workflow

Use Charter when the project direction or documentation baseline is unclear:

```text
Run LEAP Charter for this repo.
```

Use Recon when the baseline is already sufficient:

```text
Run LEAP Recon on <Initiative, Delivery Unit, Build Unit, Domain,
Architecture area, feature, risk, dependency, contract, or legacy Layer>.
```

Examples:

```text
Run LEAP Recon on the password-reset Initiative.
Run LEAP Recon on the account-recovery Delivery Unit.
Run LEAP Recon on whether the API contract matches the frontend.
Run LEAP Recon on the legacy Layer 3 plan and classify what it represents.
Run LEAP Recon on cleaning up stale documentation.
Run LEAP Cleanup on the stale documentation identified above.
```

Recon should report:

- Baseline Freshness Check
- source truth and repo reality
- Strategic Outcome and Initiative alignment
- Roadmap, Domain, and Architecture impacts
- Planning Boundary Review
- Delivery Unit and Build Unit recommendations
- risks and material questions
- recommended next step

For tiny work, use a normal prompt or [Quick LEAP Brief](quick-leap-brief.md).

## Simple version

1. Add LEAP to Project Instructions.
2. Put Agent Pack `AGENTS.md` in the project root.
3. Run the population Prompt.
4. Run Charter or a focused Recon.
