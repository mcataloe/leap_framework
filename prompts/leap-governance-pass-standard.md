# LEAP Governance Pass — Standard Operational Prompt

Run a LEAP strategic reconciliation pass using the current LEAP Framework.

Use this when the repository, docs, branch state, implementation reality, public terminology, or Agent Pack guidance may have drifted.

This is a governance pass, not an implementation Prompt.

## Canonical project-documentation model

Governance verifies alignment with the [project documentation model](../docs/project-documentation-model.md) and the Layer rules in the [migration guide](../docs/maintainer/project-documentation-migration.md).

## Required behavior

You must:

1. identify the current LEAP version and governing docs
2. inspect README, changelog, glossary, canonical references, templates, prompts, examples, and Agent Pack guidance
3. verify that planning terminology and rules (Mission, Strategic Outcome, Initiative, Delivery Unit, Build Unit, Roadmap, Domain, Architecture) match the project documentation model
4. classify remaining generic Layer uses as framework name, LHS name, qualified Architecture term, Phase, legacy compatibility, intentional historical example, or unresolved planning term
5. check whether new canonical docs are discoverable
6. check whether templates and operational prompts agree with current framework rules
7. confirm LHS is a Prompt format for staged execution, not the strategic hierarchy or lifecycle phase
8. check Materiality Gate decision flow, Materiality-Gated / No Gate semantics, source truth, repo reality, stop conditions, and execution configuration
9. check execution-routing doctrine, onboarding Execution Environment Profile guidance, capability-before-tool selection, cost optimization boundaries, and implementation-versus-verification state
10. check risk, destructive-change, sensitive-area, dependency-contract, and implementation-gravity guidance
11. check Agent Pack metadata, managed/project/local markers, manifests, and distributed terminology
12. check Baseline State and optional `leap.baseline.yaml` guidance
13. check whether stale or obsolete artifacts require a dedicated LEAP Cleanup pass
14. classify all drift found
15. recommend updates, but do not rewrite files unless explicitly asked

Governance may update baseline metadata only when the pass explicitly performs or confirms a full reconciliation or intentional baseline update.

## Drift categories

```text
Strategy drift — framework direction, Mission, Outcomes, or audience changed
Documentation drift — canonical and supporting docs disagree
Planning-model drift — Initiative, Delivery Unit, Build Unit, Roadmap,
  Domain, Architecture, or legacy Layer meanings conflict
Implementation drift — code or Prompt artifacts do not match methodology
Branch drift — active branches, worktrees, or PRs conflict
Prompt drift — Prompts assume stale files, decisions, scope, or execution settings
Execution-routing drift — tool selection, capability requirements, validation, or provider-cost assumptions no longer match current environment
Terminology drift — deprecated or ambiguous terms remain
Adoption drift — onboarding docs do not match current behavior
Agent Pack drift — distributed AGENTS.md templates or manifests disagree
Compatibility drift — public paths or legacy references break without a plan
```

## Required output

```text
# LEAP Governance — Strategic Reconciliation Pass

## 1. Current Version and Governing Sources
## 2. Documentation Discovery Review
## 3. Project Documentation Model Review
## 4. Legacy Layer Classification Review
## 5. Materiality / Question Discipline Review
## 6. Source-of-Truth and Repo-Reality Review
## 7. Template and Operational Prompt Review
## 8. Prompt Taxonomy / LHS Placement Review
## 9. Risk / Dependency / Destructive-Change Review
## 10. Agent Execution Configuration and Routing Review
## 11. Agent Pack / AGENTS.md Review
## 12. Baseline State Review
## 13. Drift Ledger Candidates
## 14. Recommended Updates
## 15. Human Decisions Required
## 16. Gate Decision / Next Step
```

Omit sections with nothing material. Do not pad with N/A.

## Gate decisions

```text
No Action Needed
Update Docs
Update Templates
Update Prompt Library
Reconcile Project Documentation Model
Reconcile Legacy Layer Terminology
Update Agent Pack
Run LEAP Cleanup
Needs Human Decision
Run Full Framework Recon
```
