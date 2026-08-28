# LEAP Governance Pass — Standard Operational Prompt

Run a LEAP strategic reconciliation pass using the current LEAP Framework.

Use this when the repository, docs, branch state, implementation reality, public terminology, or Agent Pack guidance may have drifted.

This is a governance pass, not an implementation Prompt.

## Canonical project-documentation model

Governance should verify alignment with:

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

Roadmap schedules and prioritizes. Domains describe persistent responsibility boundaries. Architecture describes technical structure.

Generic project-planning `Layer` is legacy-compatible and deprecated as the preferred planning level. Preserve the LEAP name, Layered House Standard, LEAP LHS, qualified Architecture Layers, public paths, and compatibility references.

## Required behavior

You must:

1. identify the current LEAP version and governing docs
2. inspect README, changelog, glossary, canonical references, templates, prompts, examples, and Agent Pack guidance
3. verify Mission, Strategic Outcome, Initiative, Delivery Unit, Build Unit, Roadmap, Domain, and Architecture terminology
4. verify that Roadmap does not permanently own Initiative identity
5. verify that Initiatives and Domains are treated as many-to-many
6. verify that Delivery Unit may collapse for small work
7. verify that Build Unit is not defined as necessarily independently deployable
8. classify remaining generic Layer uses as framework name, LHS name, qualified Architecture term, Phase, legacy compatibility, intentional historical example, or unresolved planning term
9. check whether new canonical docs are discoverable
10. check whether templates and operational prompts agree with current framework rules
11. confirm LHS is a Prompt format for staged execution, not the strategic hierarchy or lifecycle phase
12. check Materiality Gate, source truth, repo reality, stop conditions, and execution configuration
13. check risk, destructive-change, sensitive-area, dependency-contract, and implementation-gravity guidance
14. check Agent Pack metadata, managed/project/local markers, manifests, and distributed terminology
15. check Baseline State and optional `leap.baseline.yaml` guidance
16. check whether stale or obsolete artifacts require a dedicated LEAP Cleanup pass
17. classify all drift found
18. recommend updates, but do not rewrite files unless explicitly asked

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
## 10. Agent Execution Configuration Review
## 11. Agent Pack / AGENTS.md Review
## 12. Baseline State Review
## 13. Drift Ledger Candidates
## 14. Recommended Updates
## 15. Human Decisions Required
## 16. Gate Decision / Next Step
```

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
