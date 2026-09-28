# LEAP Cleanup Request

Run LEAP Cleanup using the current LEAP Framework.

## Target

- Repository:
- Branch / worktree, if material:
- Scope: repository-wide / bounded paths or artifacts

## Cleanup intent

- Problem to solve:
- Known canonical source truth:
- Known stale, duplicate, conflicting, misleading, or superseded artifacts:
- Known consumers or dependencies:
- Public paths, retention rules, or compatibility obligations:

## Cleanup mode

Select one when known. Otherwise, let the Cleanup pass recommend it.

- `archive-only`
- `controlled-migration`
- `destructive-cutover`

## Authorization

```text
Discovery only. Do not modify, move, archive, or delete files.
```

Inventory and classify candidates, inspect authority and dependencies, identify canonical replacements, and return the exact proposed decommission set for approval.
