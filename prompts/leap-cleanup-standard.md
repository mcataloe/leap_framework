# LEAP Cleanup — Standard Operational Prompt

Run a LEAP Repository Cleanup pass using the current LEAP Framework.

Use this when stale, duplicate, conflicting, misleading, superseded, archived, or otherwise obsolete artifacts may compete with current source truth or remain wired into the repository.

Governing behavior: [`../docs/repository-cleanup.md`](../docs/repository-cleanup.md).

This is a specialized Governance workflow. It is not a lifecycle phase, Agent Execution Mode, authorization substitute, or implementation Prompt.

## Command contract

```text
Run LEAP Cleanup on <repository or bounded scope>.
```

Inherit same-thread context. Ask only for missing information that materially changes scope, authority, compatibility, risk, or approval.

Unless the user has already approved an exact decommission set, this pass is discovery-only. Do not modify, move, archive, or delete files.

## Cleanup modes

Use or recommend exactly one mode for each candidate. `archive-only` is cleanup-specific; `controlled-migration` and `destructive-cutover` apply their corresponding compatibility and supersession postures to cleanup work:

- `archive-only`
- `controlled-migration`
- `destructive-cutover`

Confirmed coexistence requirements route to `controlled-migration`. Unresolved material obligations block `destructive-cutover`.

Git history is the default archive for destructive cutovers. Do not retain an in-tree backup of the retired design unless a separate retention requirement is explicitly approved.

## Required behavior

You must:

1. identify the repository, branch, worktree, pull-request, and governing source-truth context
2. inventory the requested scope and the references and consumers needed to judge it
3. classify each candidate as Canonical, Supporting, Current but poorly organized, Partially useful, Stale, Conflicting, Duplicate, Completed implementation plan, Misleading, Archived, or Unknown
4. determine current authority and whether the artifact still owns truth or behavior
5. inspect inbound references, imports, routing, configuration, tests, runtime dependencies, active environments, and discoverable external consumers when relevant
6. identify the canonical replacement and collect replacement evidence
7. identify public paths, contracts, retention rules, and compatibility obligations
8. recommend an action and cleanup mode for each candidate
9. separate safe candidates from blocked, unknown, or human-decision candidates
10. produce an exact proposed decommission set
11. define reference repairs, source-of-truth updates, forbidden-pattern checks, and validation
12. stop for approval before any mutation

Do not treat text search, a warning label, a file move, or a classification by itself as proof that decommissioning is effective.

## Proposed decommission-set fields

For each candidate report:

```text
Artifact:
Type:
Classification:
Current authority:
Evidence:
Inbound references and consumers:
External or cross-repository surfaces:
Canonical replacement:
Replacement evidence:
Public-path / compatibility obligations:
Proposed action:
Cleanup mode:
Risk and unknowns:
Approval required:
Validation:
```

## Required output

```text
# LEAP Cleanup — Decommission Review

## 1. Scope and Governing Sources
## 2. Repository and Branch Reality
## 3. Cleanup Mode Assessment
## 4. Artifact Inventory and Classification
## 5. Authority and Canonical Replacement Review
## 6. Reference, Dependency, and Consumer Review
## 7. Public-Path, Retention, and Compatibility Review
## 8. Proposed Decommission Set
## 9. Blocked, Unknown, and Human-Decision Candidates
## 10. Reference and Source-of-Truth Repair Plan
## 11. Validation and Forbidden-Pattern Plan
## 12. Human Approval Required
## 13. Gate Decision / Next Step
```

## Gate decisions

```text
No Action Needed
Needs Human Classification
Blocked - Replacement Missing
Blocked - Live Dependencies
Ready for Decommission Approval
Route to Controlled Migration
Generate LEAP Refactor Prompt
Run Full LEAP Recon
```

After the exact decommission set is approved, generate a LEAP Refactor Prompt for execution. Do not silently convert the Cleanup pass into implementation.
