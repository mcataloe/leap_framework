# LEAP Version

LEAP release versions should be managed by Git tags. Keep active release notes focused on current/unreleased changes and the current baseline; use Git history and release tags for older version detail.

LEAP AGENTS.md templates are released from the separate LEAP Agent Pack repository because downstream repositories copy and customize those files.

Current framework baseline:

```text
Version: 0.1.9
Release tag: leap-v0.1.9
Status: current baseline; current branch changes remain unreleased
```

Unreleased framework additions:

```text
- Dependency & Contract Recon subprocess inside LEAP Recon
- Dependency register guidance for leap.dependencies.yaml
- Starter dependency register example and permissive JSON Schema
```

Current Agent Pack:

```text
Version: 0.1.0
Release tag: leap-agent-pack-v0.1.0
Repository: https://github.com/mjcataldi/leap_agent_pack
Manifest: manifests/latest.json
Update policy: notify
```

The first Agent Pack release tag should be created in the Agent Pack repository after its manifest and template metadata are committed.

Canonical framework document:

```text
docs/leap.md
```

Canonical Charter reference:

```text
docs/leap-charter.md
```

Supporting Dependency & Contract Recon reference:

```text
docs/dependency-contract-recon.md
examples/leap.dependencies.yaml
schemas/leap.dependencies.schema.json
```

Release context is preserved through:

```text
CHANGELOG.md
Git tags, when present
Git commit history
```

Active framework and prompt files should not use versioned filenames.

Agent Pack template files live in `https://github.com/mjcataldi/leap_agent_pack`. Version identity lives in the Agent Pack metadata block and manifests, not in LEAP Framework filenames.
