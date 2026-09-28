<!--
LEAP_DOC_METADATA:
  audience: maintainer, agent
  doc_type: documentation-governance
  authority: supporting
  applies_to: leap-framework-repo
END_LEAP_DOC_METADATA
-->

# Framework Documentation Governance

This guide defines how LEAP Framework documentation should be organized.

## Domains

- `docs/user/` - how to adopt and use LEAP in downstream projects.
- `docs/reference/` - index for canonical framework references.
- `docs/maintainer/` - how to maintain, version, and release the LEAP Framework repository.
- `docs/examples/` - examples only.

## Audience Rules

- User docs should be safe for downstream project users.
- Reference docs define LEAP behavior and terminology.
- Maintainer docs apply to this LEAP Framework repository.
- Examples illustrate usage and should not override canonical docs.

## Authority Rules

- Canonical docs define current framework behavior.
- Supporting docs explain or apply canonical behavior.
- Runbooks describe repeatable maintenance procedures.
- Release notes should focus on current/unreleased changes and the current baseline.
- Older version detail should live in Git history and release tags instead of active docs.
- Example-only docs are not source truth.

## Maintenance Rules

- `docs/00_start_here.md` remains the public front door.
- `docs/leap.md` remains the canonical framework reference unless intentionally moved with a compatibility stub.
- Maintainer docs must not be used as downstream project instructions by default.
- Old paths should receive compatibility stubs when moved after public or agent-facing references exist.
- Docs moves require README and changelog updates.
- Do not restore older release-note detail or versioned historical docs unless there is a specific compatibility reason.
- Use [LEAP Repository Cleanup](../repository-cleanup.md) when obsolete framework artifacts need an exact decommission set rather than ordinary documentation reconciliation.
- For an approved destructive cutover, use Git history as the default archive and validate that retired material no longer competes with current framework truth.
