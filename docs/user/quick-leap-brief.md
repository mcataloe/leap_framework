# Quick LEAP Brief

Use this for one small task when Charter and Recon would be heavier than the work, but a coding agent still needs scope, checks, and stop conditions.

**Good fit:** small UI fixes, localized backend changes, simple tests, narrow refactors, documentation updates, low-risk behavior changes.

**Not a fit; escalate to [Recon](../../templates/leap-recon-lite-template.md) or [Charter](../leap-charter.md):** unclear direction or source truth, major data-model or Architecture changes, auth, billing, or sensitive-data changes, destructive migrations, or work spanning several branches, agents, or repositories.

## Copy-ready brief

Delete any line that does not apply.

```text
# Quick LEAP Brief - <Task Name>

## 1. Goal
- <What should change, and why>
- Work item: <ticket / issue link, if any>

## 2. Current State
- <What exists now>
- Source truth: <files and docs to trust>
- Do not use: <stale or archived docs, if any>

## 3. Scope
- In scope: <allowed changes>
- Non-goals: <what this must not do>
- Do not touch: <files, directories, components>

## 4. Constraints
- Follow existing patterns. No new dependencies without approval.
- Do not change API, schema, auth, billing, data, or AI behavior without approval.
- Preserve compatibility unless told otherwise. Archived docs are history, not current truth.

## 5. Verification
- Run: <tests, lint, typecheck, build, manual checks>
- Done means: <observable acceptance criteria>

## 6. Stop Conditions
Stop and report if required files are missing, existing code or docs
contradict this brief, a stale or archived doc is the only source for
required behavior, forbidden files must change, a hard stop is reached
(dependency, migration, auth, security, billing, sensitive data, public
contract), acceptance criteria are impossible, or verification cannot run.

## 7. Handoff
Return files changed, checks run with results, checks not run, the
verification state (Execution verified / Partially verified / Implemented —
execution unverified / Failed), and any follow-up.
```

Optional fields, when they help:

```text
Agent / tool / model:        <for example Codex, Claude Code; reasoning level>
Execution mode:              implement-directly / repo-preflight-then-implement
Planning traceability:       <Initiative / Delivery Unit / Build Unit, if the project uses them>
Branch / commit guidance:
```

## Escalation rule

If the brief starts needing product discovery, Architecture decisions, source-truth reconciliation, or more than one coherent change, stop and run Recon or Charter. If the work has several Build Units with dependency order or rollback risk, use [LHS](../leap-lhs.md).
