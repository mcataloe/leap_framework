<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: documentation-map
  authority: canonical-docs-map
  applies_to: leap-framework-repo
END_LEAP_DOC_METADATA
-->

# LEAP Documentation Map

New to LEAP? Read [`00_start_here.md`](00_start_here.md) first.

## Load tiers

| Tier | Load when | Documents |
|---|---|---|
| 0 | Always (via `AGENTS.md`) | [`leap-core.md`](leap-core.md) |
| 1 | Most non-trivial tasks | [`user/quick-leap-brief.md`](user/quick-leap-brief.md), [`../templates/leap-recon-lite-template.md`](../templates/leap-recon-lite-template.md), [`../prompts/leap-validation-standard.md`](../prompts/leap-validation-standard.md), [`../templates/leap-pull-request-template.md`](../templates/leap-pull-request-template.md) |
| 2 | When the work calls for it | Everything below |

## Canonical references

| Document | Purpose |
|---|---|
| [`leap-core.md`](leap-core.md) | The always-loaded rule set (under 650 words) |
| [`leap.md`](leap.md) | Framework reference: lifecycle, source truth, risk, Prompt behavior |
| [`leap-charter.md`](leap-charter.md) | Greenfield and Brownfield Charter |
| [`leap-lhs.md`](leap-lhs.md) | LHS stage format for staged implementation |
| [`semantic-routing.md`](semantic-routing.md) | `LEAP help`, command catalog, and choosing the workflow |
| [`execution-routing.md`](execution-routing.md) | Choosing the tool or surface; verification states; per-tool profiles |
| [`agent-execution-roles.md`](agent-execution-roles.md) | Optional architect, implementor, reviewer, and human-approver roles; context packets and handoffs |
| [`team-delivery-estimation.md`](team-delivery-estimation.md) | Advisory effort and delivery estimates; the work tracker stays the source of record |
| [`project-documentation-model.md`](project-documentation-model.md) | Optional planning model (Mission to Build Unit; Roadmap, Domain, Architecture) |
| [`leap-skills.md`](leap-skills.md) | Reusable execution capabilities and the Skill Contract |
| [`glossary.md`](glossary.md) | Terminology |
| [`materiality-gate.md`](materiality-gate.md) | Ask, assume, or stop; No Gate |
| [`dependency-contract-recon.md`](dependency-contract-recon.md) | Dependency and contract Recon |
| [`repository-cleanup.md`](repository-cleanup.md) | Governed artifact decommissioning |
| [`risk-taxonomy.md`](risk-taxonomy.md) | Risk categories and destructive-change controls |

Operational Prompts are indexed in [`../prompts/README.md`](../prompts/README.md).

## User guides

| Document | Purpose |
|---|---|
| [`user/leap_project_setup.md`](user/leap_project_setup.md) | Project and Agent Pack setup |
| [`user/which-leap-workflow.md`](user/which-leap-workflow.md) | Workflow chooser |
| [`user/quick-leap-brief.md`](user/quick-leap-brief.md) | Small bounded handoff |
| [`user/leap-discovery.md`](user/leap-discovery.md) | Discovery and Pressure Test |

## Maintainer references

| Document | Purpose |
|---|---|
| [`maintainer/framework-doc-governance.md`](maintainer/framework-doc-governance.md) | Framework documentation governance |
| [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md) | Classifying and migrating legacy `Layer` docs |
| [`maintainer/release-history.md`](maintainer/release-history.md) | Release-notes policy |

Examples in [`examples/`](examples/) and [`../examples/`](../examples/) are illustrative, not source truth.

## Agent reading rules

- Load only what the current workflow needs. LEAP Core is already loaded.
- Treat canonical references as doctrine, user guides as adoption guidance, maintainer docs as framework-repository guidance, and examples as illustrative.
- Distributable `AGENTS.md` templates live in the [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack).
