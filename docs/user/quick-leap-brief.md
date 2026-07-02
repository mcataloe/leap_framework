# Quick LEAP Brief

Use this when full Charter and Recon would be heavier than the task, but a coding agent still needs bounded scope, validation, and stop conditions.

Quick LEAP Brief is for one small task or Build Unit. If the brief begins requiring product discovery, Strategic Outcome or Initiative decisions, Architecture changes, dependency review, branch-drift review, or source-truth reconciliation, escalate to Charter or Recon.

## Project-documentation posture

A small task does not need the full documentation hierarchy when broader context is not material.

When useful, include:

```text
Mission / Project Charter:
Strategic Outcome:
Initiative:
Delivery Unit: collapsed / not applicable / <ID>
Build Unit / task:
Affected Domains:
Affected Architecture Areas:
```

Delivery Unit may be collapsed when one Build Unit directly delivers the complete outcome.

A Build Unit is not necessarily independently deployable.

## When to use it

```text
- small UI fixes
- localized backend changes
- one Build Unit
- simple tests
- narrow refactors
- documentation updates
- low-risk behavior changes
```

Do not use it for:

```text
- unclear Mission, Strategic Outcome, or Initiative ownership
- major data-model or Architecture changes
- auth, session, permission, billing, or sensitive-data changes
- destructive migrations
- several branches, agents, or repositories
- stale docs or unclear source truth
- Brownfield documentation reconciliation
- ambiguous legacy Layer plans
```

## Copy-ready brief

```text
# Quick LEAP Brief - <Task Name>

## 1. Goal
- <What should change?>

## 2. Current State
- <What exists now?>
- <What files and docs are source truth?>
- <What docs are stale, archived, or do-not-use?>

## 3. Optional Traceability
- Mission / Project Charter:
- Strategic Outcome:
- Initiative:
- Delivery Unit: collapsed / not applicable / <ID>
- Build Unit / task:
- Affected Domains:
- Affected Architecture Areas:

## 4. Scope
In scope:
- <Allowed changes>

Out of scope:
- <Disallowed changes>

Files / areas to inspect:
- <Files, directories, components>

Files / areas not to touch:
- <Forbidden files, directories, components>

## 5. Constraints
- Follow existing patterns.
- Do not introduce dependencies without approval.
- Do not change API, schema, auth, billing, data, or AI behavior without approval.
- Preserve compatibility unless explicitly told otherwise.
- Treat archived docs as historical unless a current canonical doc references them.
- Do not expand the task into a new Initiative, Delivery Unit, Domain, or Architecture refactor.

## 6. Verification
Run or check:
- <tests, lint, typecheck, build, manual checks>

Done means:
- <observable acceptance criteria>

## 7. Stop Conditions
Stop and report if:
- required files are missing
- existing code contradicts the brief
- docs conflict with repo reality
- a stale or archived doc is the only source for required behavior
- Initiative, Domain, or Architecture ownership becomes materially unclear
- forbidden files must be touched
- new dependencies, migrations, auth, billing, or sensitive-data handling are required
- verification cannot be run or is unclear
- acceptance criteria are impossible
- a legacy Layer must be interpreted without enough evidence

## 8. Agent Execution Configuration
- Agent / Tool: <Codex / Claude Code / Cursor / other>
- Codex Plan Mode: <usually Off>
- Model: <exact model or recommendation>
- Reasoning Level: <Low / Medium / High / Extended>
- Execution Mode: <implement-directly / repo-preflight-then-implement>
- Scope Scale: <small task / Build Unit>
- Repository:
- Branch / Worktree:
- Permissions:
- Validation:
- Commit Guidance:

## 9. Validation/Handoff
Return:
- Summary of changes
- Files changed
- Tests and checks run
- Checks not run
- Docs updated or needing update
- Follow-up Charter / Recon / Prompt / LHS recommendations
```

## Default settings

Tiny low-risk work:

```text
Codex Plan Mode: Off
Reasoning Level: Medium
Execution Mode: implement-directly
Scope Scale: small task
```

Coherent Build Unit:

```text
Codex Plan Mode: Off
Reasoning Level: High
Execution Mode: repo-preflight-then-implement
Scope Scale: Build Unit
```

Use LHS instead when two or more are true:

- more than three files
- several system or documentation areas
- dependency order
- tests and docs
- phased commits
- rollback or compatibility risk
- Architecture, data-contract, or workflow changes
- a named Initiative or Delivery Unit contains several Build Units
- cross-repository coordination
- explicit integration checkpoints are needed

LEAP LHS stages implementation. It does not define the project's strategic hierarchy.

## Escalation rule

```text
If the brief starts needing product discovery, Strategic Outcome or
Initiative decisions, Architecture decisions, source-truth reconciliation,
Brownfield documentation reconciliation, or branch-drift review, stop and
run Charter or Recon.
```
