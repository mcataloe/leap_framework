# LEAP Recon Lite Request

Use this when you need a focused LEAP Recon pass, but the full Recon request template is heavier than the question.

For broader, higher-risk, dependency-heavy, or brownfield reconciliation work, use the full [`LEAP Recon Request Template`](leap-recon-template.md).

```text
Run LEAP Recon using the current LEAP framework.

Target area:
- <feature, risk, layer, dependency, contract, architecture question, or repo concern>

Current baseline:
- Charter complete? yes/no/not needed/unknown
- Source-truth docs:
- Repo:
- Branch:
- Known stale or archived docs:
- Known constraints:

What I need from Recon:
- <what decision or clarity is needed?>

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
- Findings
- Material unknowns
- Assumptions
- Recommended next step
- Whether a LEAP Prompt is ready
```
