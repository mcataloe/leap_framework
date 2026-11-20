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

See [`VERSION.md`](../../VERSION.md) for the verified tags and published prereleases. The previously documented `leap-v0.1.9` tag does not exist, so do not advertise `0.1.9` as a release. Current changes are unreleased; the next release identity is a maintainer decision.

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
