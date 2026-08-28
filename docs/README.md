<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: documentation-map
  authority: canonical-docs-map
  applies_to: leap-framework-repo
END_LEAP_DOC_METADATA
-->

# LEAP Documentation Map

This folder contains LEAP Framework documentation for users, reference readers, maintainers, and agents.

## Documentation domains

| Domain | Audience | Authority | Start here |
|---|---|---|---|
| Root entry point | Users and agents | Entry point | [`00_start_here.md`](00_start_here.md) |
| User docs | Downstream adopters | Supporting guidance | [`user/leap-for-humans.md`](user/leap-for-humans.md) |
| Reference docs | Users, maintainers, agents | Canonical or supporting reference | [`reference/README.md`](reference/README.md) |
| Maintainer docs | Framework maintainers | Repository governance and migration guidance | [`maintainer/framework-doc-governance.md`](maintainer/framework-doc-governance.md) |
| Examples | Users and agents | Example-only | [`examples/`](examples/) |

## Canonical framework references

| Document | Purpose | Authority |
|---|---|---|
| [`leap.md`](leap.md) | Lifecycle, doctrine, source truth, risk, Prompt behavior, and Skill composition | Canonical |
| [`leap-charter.md`](leap-charter.md) | Greenfield and Brownfield Charter behavior | Canonical |
| [`project-documentation-model.md`](project-documentation-model.md) | Mission, Strategic Outcome, Initiative, Delivery Unit, Build Unit, Roadmap, Domain, and Architecture model | Canonical |
| [`leap-skills.md`](leap-skills.md) | Reusable execution capabilities, Skill Contract, selection, permissions, progressive disclosure, and verification | Canonical |
| [`glossary.md`](glossary.md) | Canonical terminology | Canonical |
| [`materiality-gate.md`](materiality-gate.md) | Question and assumption discipline | Supporting framework rule |
| [`dependency-contract-recon.md`](dependency-contract-recon.md) | Dependency and contract Recon behavior | Supporting Recon reference |

## Project documentation model

Preferred traceability:

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

LEAP Skills are orthogonal execution capabilities: Build Units define what bounded responsibility is delivered; Skills define reusable how. Do not insert Skills into the strategic hierarchy.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level. Use [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md) to classify legacy Layer documents before migration.

## Important user docs

| Document | Purpose |
|---|---|
| [`00_start_here.md`](00_start_here.md) | Plain-English entry point |
| [`user/leap_project_setup.md`](user/leap_project_setup.md) | Project and Agent Pack setup |
| [`user/which-leap-workflow.md`](user/which-leap-workflow.md) | Workflow routing |
| [`user/when-not-to-use-leap.md`](user/when-not-to-use-leap.md) | Lightweight alternatives |
| [`user/leap-for-humans.md`](user/leap-for-humans.md) | Human-oriented overview |
| [`user/quick-leap-brief.md`](user/quick-leap-brief.md) | Small bounded handoff |

## Maintainer references

| Document | Purpose |
|---|---|
| [`maintainer/framework-doc-governance.md`](maintainer/framework-doc-governance.md) | Framework documentation governance |
| [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md) | Legacy Layer semantic migration |
| [`maintainer/release-history.md`](maintainer/release-history.md) | Release-notes policy |

## Common starting points

- New to LEAP: [`00_start_here.md`](00_start_here.md)
- Project hierarchy: [`project-documentation-model.md`](project-documentation-model.md)
- Reusable execution capability: [`leap-skills.md`](leap-skills.md)
- Define a Skill: [`../templates/leap-skill-template.md`](../templates/leap-skill-template.md)
- Existing Layer-based project: [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md)
- Project setup: [`user/leap_project_setup.md`](user/leap_project_setup.md)
- Workflow choice: [`user/which-leap-workflow.md`](user/which-leap-workflow.md)
- Small task: [`user/quick-leap-brief.md`](user/quick-leap-brief.md)
- Short Recon request: [`../templates/leap-recon-lite-template.md`](../templates/leap-recon-lite-template.md)
- Full Recon request: [`../templates/leap-recon-template.md`](../templates/leap-recon-template.md)
- Optional baseline metadata: [`../examples/leap.baseline.yaml`](../examples/leap.baseline.yaml) and [`../schemas/leap.baseline.schema.json`](../schemas/leap.baseline.schema.json)

## Agent reading rules

- Start with [`00_start_here.md`](00_start_here.md).
- Use [`leap.md`](leap.md), [`leap-charter.md`](leap-charter.md), [`project-documentation-model.md`](project-documentation-model.md), [`leap-skills.md`](leap-skills.md), and [`glossary.md`](glossary.md) as canonical doctrine.
- Use [`leap-skills.md`](leap-skills.md) only when reusable execution capability is relevant; do not force Skill ceremony into tiny work.
- Use [`maintainer/project-documentation-migration.md`](maintainer/project-documentation-migration.md) only for legacy project-documentation reconciliation.
- Treat user docs as downstream adoption guidance.
- Treat maintainer docs as LEAP Framework repository guidance unless a downstream project explicitly adopts them.
- Treat examples as illustrative, not canonical source truth.
- Use the dedicated [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) for distributable `AGENTS.md` templates, install guidance, manifests, and upgrade guidance.
- Keep active docs focused on the current framework baseline. Use Git history and release tags for older detail.
