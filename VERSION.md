# LEAP Version

LEAP releases are Git tags. [CHANGELOG.md](CHANGELOG.md) records current and unreleased changes; use Git history and tags for older detail. Active files do not use versioned filenames.

## Framework release provenance (checked 2026-11-19)

Earlier docs recorded baseline `0.1.9` with tag `leap-v0.1.9`. No such tag exists in either repository, so do not describe `0.1.9` as a published release.

The verified published GitHub prereleases are `v0.1.10-alpha` and `v.0.1.11-alpha` (both 2026-05-29), in https://github.com/mcataloe/leap_framework. No stable release tag exists. Everything since then is unreleased; choosing the next release identity is a maintainer decision.

```text
Previously documented baseline: 0.1.9 (no matching tag)
Latest verified published prerelease: v.0.1.11-alpha
Current branch: unreleased changes
Next release version/tag: not established
```

Unreleased additions are listed in [CHANGELOG.md](CHANGELOG.md). The documentation map is [docs/README.md](docs/README.md).

## Current Agent Pack

```text
Version: 0.2.0-candidate.2 (unreleased; no tag)
Repository: https://github.com/mcataloe/leap_agent_pack
Manifest: manifests/latest.json
Update policy: manual review
```

Agent Pack templates embed [LEAP Core](docs/leap-core.md) verbatim. Version identity for templates belongs in Agent Pack metadata and its manifest, not in framework filenames. Tag the Agent Pack only after `scripts/check_pack.py --framework` passes.
