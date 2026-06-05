# LEAP Recon - Standard Operational Prompt

Run LEAP Recon using the current LEAP framework.

Recon investigates a focused area, gap, risk, feature, dependency, contract, or architectural question. It is the source-of-truth, repo-reality, drift, dependency, risk, execution-configuration, and implementation-safety pass before prompt generation. It is not the coding-agent prompt.

Recon is normally investigative and non-mutating unless the user explicitly authorizes changes. Recon may recommend LHS prompts, but it should not default to LHS and should not mutate runtime code or broad repo structure unless explicitly authorized.

Current lifecycle:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

## Required behavior

You must:

1. verify LEAP Charter / baseline readiness before planning implementation
2. identify any residual Ideation Loop questions that must be answered first
3. apply Materiality Gate before asking clarifying questions
4. require or construct a source-of-truth manifest
5. treat Brownfield Charter outputs as valid source-truth inputs when present
6. classify docs as Canonical, Supporting, Current but poorly organized, Partially useful, Stale, Conflicting, Duplicate, Completed implementation plan, Misleading, Archived, or Unknown
7. inspect repo reality before implementation planning when repo access exists
8. treat repo reality as operational truth when docs conflict, unless a human decides otherwise
9. treat archived docs as historical unless a current canonical document explicitly references them
10. inspect branch, PR, and worktree drift when available
11. search for already-existing functionality before recommending new work
12. detect stale assumptions, stale docs, stale prompts, and stale layer claims
13. check AGENTS.md Agent Pack metadata, managed/project/local markers, and manifest status when AGENTS.md exists or adoption is in scope
14. run Dependency & Contract Recon when dependencies, contract sources, provider repos, APIs, SDKs, events, packages, or platform services are declared or detected
15. identify cross-layer impacts and downstream assumptions
16. evaluate risk, sensitive areas, and destructive-change implications
17. define or refine Build Units only after the above checks
18. identify human checkpoints
19. distinguish LEAP process tier from agent execution configuration
20. recommend the explicit agent/tool, model, reasoning level, execution mode, validation, and commit posture when prompt generation is allowed
21. recommend LHS only when implementation gravity warrants staged execution
22. end with a gate decision

## Brownfield Charter inputs

When present, use these Brownfield Charter outputs as source-truth inputs:

```text
- document inventory
- canonical docs list
- supporting docs list
- stale / archived / do-not-use docs list
- gap register
- reconciliation notes
- migration map
- prompt backlog
- recommended next LEAP Recon / LEAP Prompt / LEAP LHS sequence
```

If these are missing and source truth is unclear, use the gate decision `Reconcile Docs First` or `Continue LEAP Charter`.

## Required source-of-truth manifest check

```text
# Source-of-Truth Manifest Check

- Project:
- Date:
- Target branch:
- Base branch:
- Current area / layer / task:
- Charter output path:
- Canonical strategic docs:
- Canonical architecture docs:
- Active ADRs / decision records:
- Active layer plan:
- Prompt backlog path:
- Execution log path:
- Cross-layer impact map path:
- Dependency register path:
- Brownfield document inventory path:
- Gap register path:
- Migration map path:
- Stale / archived docs:
- Do-not-use docs:
- AGENTS.md path:
- AGENTS.md Agent Pack status:
- Open branches / PRs affecting this work:
- Repo reality summary:
- Known doc-code conflicts:
- Human owner / approver:
- Last reviewed:
```

## Materiality Gate

Apply Materiality Gate before asking the user clarifying questions.

Classify missing context as:

```text
Material - answer would change the work, risk, gate decision, source-of-truth hierarchy, architecture, implementation path, validation strategy, or acceptance criteria.
Non-material - answer would only refine naming, wording, formatting, ordering, tone, minor preference, or polish.
Discoverable - answer should be inspected from repo/docs/contracts/tooling before asking.
Safe assumption - answer can be reasonably assumed and stated without changing the decision.
```

Question decision sequence:

```text
1. Inspect discoverable sources before asking the user.
2. Convert non-material unknowns into stated assumptions.
3. Proceed on safe assumptions when not blocked.
4. Ask only unresolved material questions.
5. Ask the smallest useful set of questions, preferably no more than three at a time.
```

Material questions are appropriate when the answer would change architecture or repository structure, implementation strategy, scope or acceptance criteria, risk assessment, source-of-truth hierarchy, compatibility or dependency behavior, validation strategy, user-facing recommendation, or irreversible / hard-to-reverse changes.

Confidence thresholds are heuristics, not permission to ask unnecessary questions. If confidence is below target because of non-material unknowns, proceed with assumptions. If confidence is below target because of material unknowns, ask targeted questions.

## Required repo-reality inspection

Inspect, when available:

```text
- target branch and base branch
- open PRs and relevant branches
- recent commits
- routes and API surfaces
- database schema and migrations
- generated types and shared contracts
- dependency registers such as `leap.dependencies.yaml`
- declared contract sources such as OpenAPI, AsyncAPI, protobuf, GraphQL schemas, provider repo URLs, docs URLs, packages, and artifacts
- existing UI components, hooks, utilities, services, and text
- tests, fixtures, scripts, package/dependency files
- auth/session/permission logic
- docs/execution logs/cross-layer impact map
```

## Dependency & Contract Recon

When dependencies or contract risks are relevant, include a focused Dependency & Contract Recon subsection inside `## 16. Dependency and Destructive-Change Review`.

Required behavior:

```text
1. Detect whether the repo has `leap.dependencies.yaml` or an equivalent dependency register.
2. Read declared dependencies from that register when present.
3. Identify contract and dependency links, including OpenAPI, AsyncAPI, protobuf, GraphQL, provider repo URLs, docs URLs, packages, and artifacts.
4. For OpenAPI contracts, inspect provider contract metadata and structure when accessible.
5. Compare available provider evidence against expected versions, accepted ranges, baseline hashes, last verified versions, compatibility policy, and declared operations used.
6. Flag confirmed breaking changes, potential breaking changes, non-breaking additive changes, and unknown or insufficient-evidence cases.
7. Separate findings into Current-work impact, General system impact, and Unknown / needs verification.
8. Include evidence, confidence, severity, and recommended next action for every finding.
9. If no dependency register exists, report that limitation, scan for dependency candidates, and recommend a starter `leap.dependencies.yaml`.
10. Keep provider repo and external contract access optional, read-only by default, permission-aware, and evidence-cited.
11. Keep notification automation out of scope; represent notification behavior only as metadata or manual follow-up unless explicitly approved.
```

Candidate evidence should include config files, source clients, IaC, CI/CD, package manifests, generated clients, OpenAPI/AsyncAPI/protobuf/GraphQL files, integration tests, mocks, Pact/WireMock files, README files, architecture docs, ADRs, and runbooks.

For OpenAPI, look for likely breaking changes such as removed endpoints, changed methods, removed or newly required parameters, newly required request body fields, removed response fields, response type changes, enum changes, auth or authorization-scope changes, status-code behavior changes, deprecated operations used by the consumer, changed referenced schemas, or provider major versions outside the consumer's accepted range.

Every finding must include:

```text
- Dependency name
- Dependency type
- Contract source, if available
- Expected version or accepted version range, if declared
- Observed provider version, if available
- Relevant operation/schema, if known
- Finding
- Impact category
- Severity
- Confidence
- Evidence
- Recommended next action
```

Use [`docs/dependency-contract-recon.md`](../docs/dependency-contract-recon.md) as supporting reference when available.

## Risk review

Include a risk review:

```text
- Product risk: low / medium / high
- Source-truth risk: low / medium / high
- Architecture risk: low / medium / high
- Dependency contract risk: low / medium / high / not applicable
- Data/security/privacy risk: low / medium / high
- AI behavior risk: low / medium / high / not applicable
- Collaboration risk: low / medium / high
- Verification risk: low / medium / high
```

Sensitive-area rule:

```text
If the change can affect money, identity, privacy, data durability, legal exposure, or user trust, stop and ask.
```

## Required Agent Execution recommendation

If the gate decision is `Generate LEAP Prompt`, include:

```text
## Recommended Agent Execution Configuration

| Field | Recommendation | Rationale |
|---|---|---|
| Agent / Tool | <Codex / Claude Code / Cursor / other> | <why> |
| Model | <exact model name or project default> | <why> |
| Reasoning Level | <low / medium / high / extended> | <why> |
| Execution Mode | <plan-first / implement-directly / implement-with-brief-plan> | <why> |
| Scope Scale | <small task / Build Unit / sublayer / entire layer / repo-wide maintenance> | <why> |
| Repository | <repo> | <why> |
| Branch / Worktree | <branch/worktree> | <why> |
| Permissions | <allowed changes> | <why> |
| Validation | <tests/lint/typecheck/build/manual checks> | <why> |
| Commit Guidance | <commit convention> | <why> |
```

Do not leave agent/tool, model, or reasoning level blank. If unknown, recommend a safe default and label it as a recommendation.

## Gate decisions

Use one of these decisions:

```text
Generate LEAP Prompt
Continue LEAP Charter
Pressure Test Further
Narrow Scope First
Needs Human Decision
Reconcile Docs First
Resolve Branch Drift First
Do Not Build Yet
```

## Required output

```text
# LEAP Recon - <Target Area, Layer, Feature, Dependency, Contract, Risk, or Question>

## 1. Framework Interpretation
## 2. Source-of-Truth Manifest Check
## 3. LEAP Charter / Baseline Gate Check
## 4. Ideation Loop Residual Questions
## 5. Materiality Check
## 6. Repo Reality Reconciliation
## 7. Branch / Worktree / PR Drift Review
## 8. Documentation Lifecycle Review
## 9. Strategic Plan Reconciliation
## 10. Existing Functionality Collision Check
## 11. Stale Assumption Scan
## 12. Cross-Layer Impact Scan
## 13. Layer Boundary Review
## 14. Generated / Refined Build Unit Inventory
## 15. Recommended Build Sequence
## 16. Dependency and Destructive-Change Review
### Dependency & Contract Recon, when relevant
## 17. Risk Taxonomy Review
## 18. Architecture Right-Sizing Review
## 19. Human Checkpoints Required
## 20. Execution Log / Drift Ledger Expectations
## 21. Coding-Agent Risk Forecast
## 22. Recommended Agent Execution Configuration
## 23. Clarification Questions Before LEAP Prompt Generation
## 24. Gate Decision / Next Step
```

The Materiality Check section should include:

```text
### Material Unknowns
Questions or missing facts that would change architecture, scope, risk, acceptance criteria, source-of-truth hierarchy, validation strategy, or implementation path.

### Assumptions Proceeding Under
Reasonable assumptions being used so work can continue without unnecessary blocking.

### Deferred Non-Material Details
Items that may improve polish, naming, formatting, or preference alignment but do not block the current recommendation.

### Question Decision
State whether LEAP should proceed with assumptions, inspect repo/docs first, or ask targeted clarifying questions.
```

Do not generate the implementation prompt unless explicitly requested and the gate decision allows it.
