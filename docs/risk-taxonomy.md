# LEAP Risk Taxonomy

LEAP uses risk categories to decide how much clarification, Recon, approval, and verification are needed before implementation.

The taxonomy should stay lightweight. Its job is to make risk visible, not to create bureaucracy.

Implementation Gravity is the amount of coordination, risk, dependency ordering, testing, documentation, and rollback concern attached to a task. Higher implementation gravity increases the chance that the implementation prompt should use LEAP LHS.

---

## Core risk categories

| Risk Area | Example | Required Control |
|---|---|---|
| Product risk | Building the wrong workflow | [LEAP Charter](leap-charter.md) / no-build review |
| Source-truth risk | Agent follows stale or archived docs | [Charter](leap-charter.md) reconciliation + manifest + doc lifecycle |
| Architecture risk | Feature forced into bad structure | [Recon](../templates/leap-recon-lite-template.md) + architecture right-sizing |
| Dependency contract risk | Provider contract drift breaks consumer expectations | [Dependency & Contract Recon](dependency-contract-recon.md) + evidence-based follow-up |
| Data risk | Destructive migration or data loss | Human approval + rollback plan |
| Security risk | Auth/session/permission changes | Mandatory checkpoint |
| Privacy risk | Sensitive user data exposed | Sensitive-area approval |
| AI behavior risk | Fabricated claims or unsafe automation | AI behavior constraints |
| UX risk | Flow becomes confusing or inaccessible | Acceptance criteria + manual checks |
| Collaboration risk | Agents touch same files/contracts | Ownership map + merge order |
| Verification risk | No reliable way to prove success | Define tests/checks before prompt generation |

---

## Sensitive-area rule

```text
If the change can affect money, identity, privacy, data durability, legal exposure, or user trust, stop and ask.
```

Sensitive areas include:

```text
- authentication
- sessions
- permissions
- user roles
- billing
- payments
- credits
- subscriptions
- private user data
- resumes, employment history, or compensation data
- personally identifiable information
- AI-generated user-facing claims
- external messaging or application submission
- production infrastructure
- secrets
- networking
- data deletion or migration
```

---

## Destructive-change protocol

A destructive change is anything that can break, delete, rewrite, or invalidate existing state in a way that is not trivially reversible.

Examples:

```text
- dropping database columns or tables
- replacing a data model
- deleting existing records
- changing IDs or ownership relationships
- rewriting migrations
- changing auth/session behavior
- changing infrastructure that affects availability
- removing user-visible workflows
```

Default rule:

```text
Destructive changes are not allowed unless explicitly authorized.
```

A LEAP Prompt should state:

```text
Destructive changes: allowed / not allowed / allowed only in these areas.
Rollback required: yes/no.
Data preservation required: yes/no.
Human approval required before migration: yes/no.
```

---

## Risk escalation rules

Escalate from Small Project Mode to Recon when:

```text
- source truth is unclear
- repo reality is unknown
- stale docs may affect the task
- multiple files or shared contracts are involved
- dependency contracts, provider APIs, or accepted versions may have drifted
- API/schema/auth/billing/AI behavior may change
- the work touches sensitive data
- validation is unclear
- a human decision is needed
```

Escalate from Recon to LEAP Charter when:

```text
- the target user is unclear
- the problem is unclear
- MVP boundary is missing
- non-goals are missing
- no-build alternatives have not been considered
- the feature changes product strategy
- the proposed work is a full product disguised as a feature
- docs need brownfield reconciliation before source truth is safe
```

---

## Risk decision output

A LEAP Recon or Prompt should summarize risk like this:

```text
## Risk Review

- Product risk: low / medium / high
- Source-truth risk: low / medium / high
- Architecture risk: low / medium / high
- Dependency contract risk: low / medium / high / not applicable
- Data/security/privacy risk: low / medium / high
- AI behavior risk: low / medium / high / not applicable
- Collaboration risk: low / medium / high
- Verification risk: low / medium / high

Required controls:
- <control 1>
- <control 2>

Human checkpoints:
- <checkpoint 1>
- <checkpoint 2>
```

---

## Practical rule

Risk does not automatically block work.

Unacknowledged risk blocks work.

LEAP can proceed when the risk is visible, accepted, bounded, and testable.
