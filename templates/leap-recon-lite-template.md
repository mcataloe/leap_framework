# LEAP Recon Lite Request

Use this for a focused Recon when the full template would add unnecessary ceremony.

For broad, high-risk, dependency-heavy, multi-repository, or Brownfield reconciliation work, use the full [`LEAP Recon Request Template`](leap-recon-template.md).

LEAP Charter is not required before every Recon. Recon starts with Baseline Freshness Check. Stop investigating when the next safe decision is clear.

References: [project documentation model](../docs/project-documentation-model.md), [Materiality Gate](../docs/materiality-gate.md), [LEAP Recon standard](../prompts/leap-recon-standard.md).

```text
Run LEAP Recon using the current LEAP Framework.

Target area:
- <Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain,
  Architecture area, feature, risk, dependency, contract, legacy Layer,
  or repository concern>

Current baseline:
- Charter complete? yes / no / not needed / unknown
- Work item: <link to issue, ticket, or planning doc>
- Initiative / Delivery Unit / Build Unit, when the project uses them:
- Planning or Architecture docs, when relevant:
- Source-truth docs:
- LEAP Baseline State source: AGENTS.md / leap.baseline.yaml / other / none
- Repository and branch:
- Known stale, archived, or legacy Layer docs:
- Known constraints:

What I need from Recon:
- <decision, risk assessment, boundary review, or clarity needed>

Baseline Freshness Check:
- Inspect AGENTS.md, baseline metadata, source truth, and relevant repo reality.
- If fresh enough, continue.
- If minor drift exists, continue and disclose the limitation.
- If material drift exists, recommend Charter / Governance or continue only with explicit limits.
- If conflict makes Recon unsafe, stop and recommend reconciliation.
- Do not silently create leap.baseline.yaml.

Planning-boundary checks:
- Determine whether the target is Initiative-sized, Delivery-Unit-sized,
  Build-Unit-sized, Domain-oriented, Architecture-oriented, a Phase,
  or an ambiguous legacy Layer.
- Use the LEAP project documentation model when the project already uses it.
- Classify legacy Layer meaning before migration.

Risk areas:
- Source truth and repo reality
- Existing functionality
- Cross-Initiative / cross-Domain impact
- Dependencies and contracts
- Architecture and compatibility
- Tests and validation
- Human checkpoints

Materiality Gate:
- Clarification mode: Materiality-Gated / No Gate.
- Apply the Materiality Gate. Inspect discoverable sources first.
- Ask only material questions needed for the next safe decision. No Gate never converts STOP into proceed.
- Stop for destructive-change, privacy, security, money, identity, legal exposure,
  user-trust, unsafe source-truth, missing authorization, or unapproved Architecture risk.

Return:
- Baseline Freshness Check
- Findings
- Planning Boundary Review
- Cross-Initiative / Cross-Domain impacts
- Legacy Layer classification, if relevant
- Material unknowns and assumptions
- Recommended Delivery Units / Build Units, when relevant
- Recommended next step
- Whether a LEAP Prompt is ready
```
