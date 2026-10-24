# LEAP Release Notes Policy

This file records the active release-notes policy for the LEAP Framework repository.

## Current Policy

Keep active release notes focused on the current framework baseline and unreleased changes.

Do not keep older version-by-version detail in active documentation when that detail is not applicable to the current framework version. It adds noise, increases the chance that coding agents use older information unintentionally, and competes with canonical current docs.

Older release detail should be recovered from:

```text
Git history
Release tags
Published release notes, when present
```

## Current release provenance

Read [`VERSION.md`](../../VERSION.md) for verified Git tags, published prereleases, and the unresolved `0.1.9` baseline claim. The previously documented `leap-v0.1.9` tag was not found in the inspected refs as of 2026-10-24; do not advertise that claim as a confirmed release. Current `main` has unreleased changes, and the next release identity is a maintainer decision.

```text
Canonical framework document: docs/leap.md
Canonical Charter reference: docs/leap-charter.md
Current operational prompts: prompts/
```

## Maintainer Rules

- Keep current source-truth paths in active docs.
- Avoid restoring old versioned framework docs or nested prompt directories unless there is a specific compatibility reason.
- Keep `CHANGELOG.md` focused on current/unreleased changes and the current baseline.
- Use release tags and Git history for older details.
- When an old path is needed for compatibility, prefer a small compatibility stub over restoring full stale content.
