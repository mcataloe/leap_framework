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

## Documentation Domains

User docs explain how to adopt and use LEAP.

Reference docs define what LEAP is.

Maintainer docs explain how to maintain, version, and release the LEAP Framework itself.

Examples illustrate usage but are not canonical source truth.

| Domain           | Audience                   | Authority                         | Start Here                                                                         |
| ---------------- | -------------------------- | --------------------------------- | ---------------------------------------------------------------------------------- |
| Root entry point | Users and agents           | Entry point                       | [`00_start_here.md`](00_start_here.md)                                             |
| User docs        | Downstream LEAP adopters   | Supporting adoption guidance      | [`user/leap-for-humans.md`](user/leap-for-humans.md)                               |
| Reference docs   | Users, maintainers, agents | Canonical or supporting reference | [`reference/README.md`](reference/README.md)                                       |
| Maintainer docs  | LEAP Framework maintainers | Repo governance and runbooks      | [`maintainer/framework-doc-governance.md`](maintainer/framework-doc-governance.md) |
| Examples         | Users and agents           | Example-only                      | [`examples/`](examples/)                                                           |

## Important Docs

| Document                                                         | Audience                   | Authority                           |
| ---------------------------------------------------------------- | -------------------------- | ----------------------------------- |
| [`00_start_here.md`](00_start_here.md)                           | Users                      | Entry point                         |
| [`user/leap_project_setup.md`](user/leap_project_setup.md)       | Users                      | Supporting adoption guidance        |
| [`user/which-leap-workflow.md`](user/which-leap-workflow.md)     | Users                      | Supporting adoption guidance        |
| [`user/when-not-to-use-leap.md`](user/when-not-to-use-leap.md)   | Users                      | Supporting adoption guidance        |
| [`user/leap-for-humans.md`](user/leap-for-humans.md)             | Users                      | Supporting adoption guidance        |
| [`user/quick-leap-brief.md`](user/quick-leap-brief.md)           | Users                      | Supporting adoption guidance        |
| [`leap.md`](leap.md)                                             | Users, maintainers, agents | Canonical framework reference       |
| [`leap-charter.md`](leap-charter.md)                             | Users, maintainers, agents | Canonical Charter reference         |
| [`materiality-gate.md`](materiality-gate.md)                     | Users, maintainers, agents | Supporting framework rule reference |
| [`dependency-contract-recon.md`](dependency-contract-recon.md)   | Users, maintainers, agents | Supporting Recon reference          |
| [`glossary.md`](glossary.md)                                     | Users, maintainers, agents | Canonical terminology reference     |
| [`risk-taxonomy.md`](risk-taxonomy.md)                           | Users, agents              | Supporting reference                |
| [`agent-profiles.md`](agent-profiles.md)                         | Users, agents              | Supporting reference                |
| [`maintainer/release-history.md`](maintainer/release-history.md) | Maintainers                | Release-notes policy                |

## Common Starting Points

- If you are new to LEAP, read [`00_start_here.md`](00_start_here.md).
- If you want to add LEAP to an existing ChatGPT/Codex project, use [`user/leap_project_setup.md`](user/leap_project_setup.md).
- If you need to choose between Quick Brief, Charter, Recon, Prompt, or LHS, use [`user/which-leap-workflow.md`](user/which-leap-workflow.md).
- If you need to decide whether full LEAP is too much for a tiny task, use [`user/when-not-to-use-leap.md`](user/when-not-to-use-leap.md).
- If the task is small and low-risk, use [`user/quick-leap-brief.md`](user/quick-leap-brief.md).
- If you need a short Recon request, use [`../templates/leap-recon-lite-template.md`](../templates/leap-recon-lite-template.md).
- If the Recon scope is broad or high-risk, use [`../templates/leap-recon-template.md`](../templates/leap-recon-template.md).
- Optional baseline metadata examples live at [`../examples/leap.baseline.yaml`](../examples/leap.baseline.yaml) and [`../schemas/leap.baseline.schema.json`](../schemas/leap.baseline.schema.json).

## Agent Reading Rules

- Start with [`00_start_here.md`](00_start_here.md) for public LEAP usage.
- Use [`leap.md`](leap.md) as the canonical current framework reference.
- Use [`leap-charter.md`](leap-charter.md) as the canonical Charter reference.
- Use [`materiality-gate.md`](materiality-gate.md) when deciding whether to ask a clarifying question, inspect sources first, or proceed with a stated assumption.
- Use [`dependency-contract-recon.md`](dependency-contract-recon.md) when Recon involves dependency registers, contract sources, provider API drift, or cross-repo contract evidence.
- Treat user docs as downstream adoption guidance.
- Treat maintainer docs as LEAP Framework repository guidance only.
- Do not treat maintainer docs as downstream project instructions unless the current repository is the LEAP Framework repository.
- Treat examples as illustrative, not source-of-truth doctrine.
- Use the dedicated [LEAP Agent Pack](https://github.com/mcataloe/leap_agent_pack) repository for AGENTS.md templates, install guidance, versioning, compatibility manifests, and upgrade guidance.
- Keep active docs focused on the current framework baseline. Use Git history and release tags for older version detail.
