# LEAP Governance Pass — Standard Operational Prompt

Run a LEAP strategic reconciliation pass using the current LEAP framework.

Use this prompt when the repo, docs, branch state, implementation reality, and public framework language may have drifted.

This is a governance pass. It is not an implementation prompt.

## Required behavior

You must:

1. identify the current LEAP version and governing docs
2. inspect README, changelog, glossary, templates, and prompt library docs
3. identify stale terminology, especially outdated framework expansion or tool-specific language where tool-agnostic language is intended
4. check whether new docs are discoverable from the README
5. check whether templates and operational prompts are aligned with current framework rules
6. check whether LEAP Prompt taxonomy is aligned and LHS is treated as a prompt format, not a lifecycle phase
7. check whether the Ideation Loop and question-loop rules are represented consistently
8. check whether source-of-truth, repo reality, stop conditions, and execution profile requirements are preserved
9. check whether risk taxonomy, destructive-change, sensitive-area, and implementation-gravity guidance are present where needed
10. check whether AGENTS.md templates have Agent Pack metadata, managed/project/local markers, and manifest alignment
11. check whether AGENTS.md Baseline State and optional `leap.baseline.yaml` guidance are present, accurate, and not treated as mandatory
12. classify any drift found
13. recommend document updates, but do not rewrite files unless explicitly asked

LEAP Governance may update the AGENTS.md Baseline State table or create/update optional `leap.baseline.yaml` when the pass explicitly performs or confirms a full reconciliation, governance pass, or intentional baseline update. Do not treat `leap.baseline.yaml` as mandatory for every project.

## Drift categories

Use these categories:

```text
Strategy drift — framework direction or audience changed
Documentation drift — docs disagree with each other
Implementation drift — code or prompt artifacts do not match methodology
Branch drift — active branches or PRs conflict
Prompt drift — prompts assume stale files, old decisions, missing agent/tool, missing model, or missing reasoning level
Terminology drift — old terms remain after framework language changed
Adoption drift — public onboarding docs do not match current framework behavior
Agent Pack drift — AGENTS.md template metadata, managed sections, manifest, tags, or update guidance disagree
```

## Required output

```text
# LEAP Governance — Strategic Reconciliation Pass

## 1. Current Version and Governing Sources
## 2. Documentation Discovery Review
## 3. Terminology Alignment Review
## 4. Ideation Loop / Question-Loop Review
## 5. Source-of-Truth and Repo-Reality Review
## 6. Template and Operational Prompt Review
## 7. Prompt Taxonomy / LHS Placement Review
## 8. Risk / Sensitive Area / Destructive-Change Review
## 9. Agent Execution Configuration Review
## 10. Agent Pack / AGENTS.md Versioning Review
## 11. Baseline State Review
## 12. Drift Ledger Candidates
## 13. Recommended Updates
## 14. Human Decisions Required
## 15. Gate Decision / Next Step
```

## Gate decisions

Use one of these decisions:

```text
No Action Needed
Update Docs
Update Templates
Update Prompt Library
Reconcile Terminology
Needs Human Decision
Run Full Framework Recon
```
