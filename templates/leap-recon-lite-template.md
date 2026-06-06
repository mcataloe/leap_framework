# LEAP Recon Lite Request

Use this when you need a focused LEAP Recon pass, but the full Recon request template is heavier than the question.

For broader, higher-risk, dependency-heavy, or brownfield reconciliation work, use the full [`LEAP Recon Request Template`](leap-recon-template.md).

LEAP Charter is not required before every Recon. Recon starts with a lightweight Baseline Freshness Check; it is preflight behavior, not a lifecycle phase, Charter mode, or separate command.

```text
Run LEAP Recon using the current LEAP framework.

Target area:
- <feature, risk, layer, dependency, contract, architecture question, or repo concern>

Current baseline:
- Charter complete? yes/no/not needed/unknown
- Source-truth docs:
- LEAP Baseline State source: AGENTS.md / leap.baseline.yaml / other / unknown / none
- Repo:
- Branch:
- Known stale or archived docs:
- Known constraints:

What I need from Recon:
- <what decision or clarity is needed?>

Baseline Freshness Check:
- Use repository AGENTS.md, Baseline State metadata if present, optional `leap.baseline.yaml`, source-truth docs, and relevant repo reality.
- If fresh enough, continue normally.
- If minor drift exists, continue with the limitation disclosed.
- If material drift exists, ask whether to run Brownfield Charter or LEAP Governance, continue with limited scope, or defer reconciliation.
- If source-truth conflict would make Recon unsafe or misleading, stop and recommend reconciliation.
- Do not silently create `leap.baseline.yaml`; Recon may recommend it as follow-up.

Risk areas to check:
- Source truth
- Repo reality
- Existing functionality
- Dependencies/contracts
- Cross-layer impact
- Tests/validation
- Human checkpoints

Materiality Gate:
- Inspect discoverable sources first.
- Ask only unresolved material questions.
- Proceed on stated assumptions for non-material unknowns.
- Stop for safety, source-truth, destructive-change, privacy, money, identity, legal exposure, or user-trust risks.

Return:
- Baseline Freshness Check
- Findings
- Material unknowns
- Assumptions
- Recommended next step
- Whether a LEAP Prompt is ready
```
