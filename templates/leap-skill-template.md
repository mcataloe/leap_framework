# LEAP Skill Definition Template

Use this template to define a reusable LEAP Skill when specialized procedure will be reused across Build Units, repositories, or agent sessions.

Do not create a Skill for a one-off instruction that is clearer inside the governing Build Unit or Prompt.

```markdown
---
name: <stable-skill-name>
purpose: <one-sentence capability>
status: draft / active / deprecated
portability: portable / harness-specific
---

# <Skill Name>

## Purpose

<What specialized capability this Skill provides.>

## Use When

- <positive trigger>
- <positive trigger>

## Do Not Use When

- <simpler approach is better>
- <outside intended scope>

## Inputs

- <required context / artifact / parameter>

## Outputs

- <artifact / finding / code change / evidence>

## Preconditions

- <state that must already be true>

## Scope Boundary

### In scope

- <allowed responsibility>

### Out of scope

- <responsibility the Skill must not absorb>

## Tool Requirements

- <tool or none>

## Permission Ceiling

<Maximum authority this Skill can exercise. The governing Prompt may narrow it further.>

## Always

- <invariant>

## Ask First

- <human-owned decision>

## Never

- <hard prohibition>

## Procedure

1. <step>
2. <step>
3. <step>

## Verification

- <evidence required before success may be claimed>

## Progressive Disclosure / References

Load only when relevant:

- `<reference path>` — <when to load>

## Portability Notes

- Native agent implementation, if any:
- Repo-local fallback:
- Prompt-embedded fallback, if needed:
```

## LEAP composition rule

When a LEAP Prompt uses this Skill, record:

```text
| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
```

The Build Unit remains the delivery boundary. The Skill remains a reusable capability. The Skill must not silently widen scope or authority.
