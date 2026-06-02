<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: supporting-reference
  authority: supporting
  applies_to: leap-recon
END_LEAP_DOC_METADATA
-->

# LEAP Dependency & Contract Recon

LEAP Dependency & Contract Recon is a focused subprocess inside LEAP Recon. It helps a repo identify declared dependencies, inspect available contract evidence, and report whether provider drift may affect the current work or the wider system.

It is intentionally lightweight. LEAP may coordinate dependency awareness, but it does not own external repositories, mutate provider code, create tickets, block releases, or send notifications by default.

## When to run it

Run this subprocess during LEAP Recon when:

- the target work may touch APIs, SDKs, generated clients, events, queues, databases, infrastructure services, auth providers, payment providers, or package artifacts
- the repo declares dependencies in `leap.dependencies.yaml` or an equivalent project convention
- dependency evidence appears in config, code, tests, mocks, package manifests, IaC, CI/CD, docs, or generated contract files
- the user asks whether an external provider contract changed or may break current work

## Dependency Register

Recommended register path:

```text
leap.dependencies.yaml
```

If a repo already has an equivalent machine-readable dependency convention, use that convention instead of creating a duplicate. Recon may recommend mapping that existing file into LEAP terms.

The register should be treated as consumer-owned metadata. Provider repositories and external contract sources are optional, read-only by default, permission-aware, and contract-focused.

Minimal fields:

```yaml
repo: payments-api

dependencies:
  - name: customer-api
    type: internal-rest-api
    direction: outbound
    role: consumer

    provider:
      team: customer-platform
      repo_url: https://github.com/company/customer-api
      repo_access: optional-read-only

    contract:
      type: openapi
      name: Customer API
      source: https://docs.company.com/customer-api/openapi.yaml
      accepted_versions: "1.x"
      last_verified_version: "1.8.2"
      last_verified_contract_hash: "optional-sha256-or-other-fingerprint"
      compatibility_policy: semver
      breaking_change_policy: notify-consumers

    usage:
      environments:
        - dev
        - test
        - prod
      code_paths:
        - src/clients/customerClient.ts
      config_keys:
        - CUSTOMER_API_BASE_URL
      operations_used:
        - GET /customers/{customerId}
        - POST /customers/search

    recon:
      confidence: high
      evidence:
        - config/application.yml contains CUSTOMER_API_BASE_URL
        - src/clients/customerClient.ts uses CustomerApiClient
        - dependency register declares OpenAPI contract source

    notification_policy:
      notify_on:
        - major-version
        - breaking-change
        - deprecation
      channels:
        - manual
```

See [`../examples/leap.dependencies.yaml`](../examples/leap.dependencies.yaml) and [`../schemas/leap.dependencies.schema.json`](../schemas/leap.dependencies.schema.json) for a starter example and permissive JSON Schema.

## Candidate Detection

If no dependency register exists, Recon must not fail. It should report that the register is missing, scan for dependency candidates, and recommend creating `leap.dependencies.yaml`.

Candidate signals include:

- `.env`, `.env.example`, `application.yml`, `application.properties`, `appsettings.json`, and other config files
- Docker Compose, Helm values, Kubernetes manifests, Terraform, CloudFormation, CDK, and Pulumi
- GitHub Actions, GitLab CI, Azure Pipelines, Jenkinsfile, and other CI/CD files
- package manifests, generated API clients, OpenAPI, AsyncAPI, protobuf, and GraphQL files
- integration tests, mocks, WireMock, Pact files, README files, architecture docs, ADRs, and runbooks

Dependency types should include at least:

```text
internal REST API
external REST API
GraphQL API
gRPC service
event topic
queue
event bus
database
cache
object storage
identity provider
secret manager
payment provider
email provider
SMS provider
analytics provider
observability provider
feature flag provider
package/library
container image
infrastructure/platform dependency
```

Generated entries are candidates, not confirmed facts, until a human or repo owner ratifies them.

## Contract Inspection

For each declared dependency, Recon should inspect available metadata:

- dependency name and type
- provider repo URL and access posture, if declared
- contract type and source, if declared
- expected version, accepted version range, last verified version, baseline hash, or compatibility policy
- local usage evidence, including code paths, config keys, generated clients, and operations used

For OpenAPI contracts, Recon should inspect provider contract metadata and structure when accessible. It should compare provider evidence against consumer expectations and declared `operations_used` when available.

Potentially breaking OpenAPI changes include:

- removed endpoint
- changed HTTP method
- removed request parameter
- new required request parameter
- new required request body field
- removed response field
- changed response field type
- changed enum values
- changed authentication scheme
- changed required authorization scope
- changed status code behavior
- deprecated operation used by the consumer
- removed or changed schema referenced by an operation
- contract major version outside the consumer's accepted version range

Classify comparison results as:

- Confirmed breaking change
- Potential breaking change
- Non-breaking additive change
- Unknown / insufficient evidence

If no baseline contract, previous version, hash, accepted version range, or operations-used list exists, report the limitation instead of pretending to know impact.

## Impact Categories

### Current-work impact

Use this category when a finding appears relevant to the feature, bug fix, refactor, or implementation currently being requested.

Examples:

- the desired implementation calls an endpoint that changed
- the desired implementation depends on a response field that was removed or changed
- the desired implementation requires a provider version outside the accepted range
- the dependency register says the current repo uses an operation that changed

### General system impact

Use this category when a finding may affect the repo or portfolio but is not directly tied to the current implementation request.

Examples:

- another endpoint changed that this repo may use
- a provider major version changed
- a deprecated operation exists but current usage is unclear
- a contract source changed but no local usage path is declared

### Unknown / needs verification

Use this category when LEAP cannot access enough evidence.

Examples:

- contract URL unavailable
- provider repo inaccessible
- dependency file missing expected version metadata
- local usage cannot be tied to provider operations
- contract source exists but no baseline or previous version is available

## Evidence and Confidence

Every finding must include:

- dependency name
- dependency type
- contract source, if available
- expected version or accepted version range, if declared
- observed provider version, if available
- relevant operation or schema, if known
- finding
- impact category
- severity
- confidence
- evidence
- recommended next action

Confidence levels:

| Confidence | Use when |
| --- | --- |
| High | Multiple direct signals agree, such as dependency register, OpenAPI diff, and local usage evidence. |
| Medium | Evidence is credible but incomplete, such as a contract change without full operation-level usage mapping. |
| Low | Evidence is weak or stale, such as old docs or package references without code/config usage. |
| Unknown | LEAP cannot verify enough evidence to make a claim. |

## Output Format

Add a `Dependency & Contract Recon` subsection inside the Recon `Dependency and Destructive-Change Review` section when dependencies or contract risks are relevant.

```markdown
# Dependency & Contract Recon

## Summary

- Dependencies declared: 4
- Contract sources accessible: 3
- Contract sources inaccessible: 1
- High-confidence breaking risks: 1
- Potential breaking risks: 2
- Current-work impacts: 1
- General system impacts: 2

## Current-work impact

| Dependency | Contract | Finding | Severity | Confidence | Evidence |
|---|---|---|---|---|---|
| customer-api | OpenAPI v2.0.0 | `GET /customers/{id}` response removed `riskProfile`, used by current work | High | High | dependency register + OpenAPI diff + code usage |

## General system impact

| Dependency | Contract | Finding | Severity | Confidence | Evidence |
|---|---|---|---|---|---|
| ledger-api | OpenAPI v3.1.0 | `POST /ledger/entries` now requires `sourceSystem`; repo usage unknown | Medium | Medium | OpenAPI diff only |

## Needs verification

| Dependency | Issue | Reason |
|---|---|---|
| fraud-api | Contract source inaccessible | Provider repo requires access or contract URL is unavailable |
```

## Notification Boundary

Notification behavior is metadata and manual recommendation only in this version.

Out of scope by default:

- Slack, Teams, or email notifications
- Jira, ServiceNow, or ticket creation
- release blocking
- runtime telemetry ingestion
- automatic provider repo pull requests
- automatic consumer repo mutation
- full service catalog functionality

Future notification hooks may use `notification_policy`, but LEAP Recon should only report findings and recommend manual follow-up unless the repository already has an approved automation mechanism and the user explicitly scopes it.
