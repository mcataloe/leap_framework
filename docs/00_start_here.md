<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: entrypoint
  authority: entry-point
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Start Here: LEAP in Plain English

**LEAP (Layered Execution & Alignment Protocol)** keeps coding agents and teams on track: grounded in what is actually true, bounded in scope, and honest about what was verified. It aims for enough guardrails and no ceremony beyond that.

Coding agents move fast. That only helps when the task is clear, the docs they read are current, and someone can check the result.

## LEAP in 60 seconds

1. **Inspect before asking.** Look at the code, tests, and docs first. Ask only questions whose answer would change the work. Zero questions is normal.
2. **Trust code over docs, and current docs over old plans.** Call out conflicts.
3. **Bound the work.** State the scope, the non-goals, and what not to touch.
4. **Stop at hard stops.** Destructive data changes, auth or security, breaking contracts, new dependencies, and irreversible Git operations need a human.
5. **Be honest about verification.** Say which checks ran and which did not. "Implemented, not verified" is a valid answer; "done" without the checks is not.

These five ideas are [LEAP Core](leap-core.md), the short rule set that loads into every agent session. Everything below is optional depth.

## Use the lightest workflow that controls the risk

| Situation | Use |
|---|---|
| Tiny, obvious change | A normal prompt |
| Small, clear task | [Quick LEAP Brief](user/quick-leap-brief.md) |
| Exploring a domain or challenging an idea | [Discovery or Pressure Test](user/leap-discovery.md) |
| Repo reality, risk, or design is unclear | [Recon](../prompts/leap-recon-standard.md) (or [Recon Lite](../templates/leap-recon-lite-template.md)) |
| Direction, source truth, or doc structure is unclear | [Charter](leap-charter.md) |
| Bounded instructions for an agent | [LEAP Prompt](../prompts/leap-prompt-standard.md); [LHS](leap-lhs.md) only when staging reduces risk |
| Obsolete artifacts competing with current truth | [Cleanup](repository-cleanup.md) |
| Finished work | [Validation/Handoff](../prompts/leap-validation-standard.md) |

Say **LEAP help** to an agent for the command list, or see [semantic routing](semantic-routing.md). Not sure? Use the [workflow chooser](user/which-leap-workflow.md).

## Lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Most work enters partway through. A small task goes straight to a brief and then Validation. Charter and Recon run only when direction or repository reality is unclear. See the [framework reference](leap.md).

## Guardrails for teams

Written rules are requests to the agent; enforced checks are what actually hold. Pair LEAP with:

- the [LEAP pull request template](../templates/leap-pull-request-template.md): scope, non-goals, verification state, checks not run, stop conditions hit
- [Validation/Handoff](../prompts/leap-validation-standard.md) on every non-trivial change, including a check of the actual diff against the stated scope
- CODEOWNERS or branch protection on paths your stop conditions name
- CI checks and agent permission rules for anything that can be enforced mechanically

## Planning traceability (optional)

If your team already tracks work in Jira, Azure DevOps, or GitHub, link the work item and say what the change delivers. That is enough for most projects.

For teams that run portfolio planning, LEAP offers a [project documentation model](project-documentation-model.md) (Mission, Strategic Outcome, Initiative, Delivery Unit, Build Unit, with Roadmap, Domain, and Architecture as separate views). Small projects do not need one file per concept.

The older generic planning term `Layer` is deprecated; existing Layer docs are classified before migration. See [Project Documentation Migration](maintainer/project-documentation-migration.md).

## Going deeper

- [Materiality Gate](materiality-gate.md): how LEAP decides to ask, assume, or stop (including **No Gate**)
- [Execution routing](execution-routing.md): choosing the cheapest tool that can run the required checks, and the verification states
- [LEAP Skills](leap-skills.md): reusable procedures. A Skill never widens what the Prompt allows.
- [Dependency & Contract Recon](dependency-contract-recon.md), [Risk taxonomy](risk-taxonomy.md), [Glossary](glossary.md)
- [Documentation map](README.md)

## AGENTS.md adoption

The [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) distributes `AGENTS.md` templates containing LEAP Core plus a short project section. [LEAP Project Setup](user/leap_project_setup.md) walks through it.

## Rule of thumb

```text
Inspect what is discoverable.
Ask only what changes the next safe decision.
Assume or defer the rest.
Stop when a hard blocker applies.
Report what was verified, and what was not.
```
