<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-framework-reference
  authority: canonical
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# LEAP Framework

This file represents the current canonical LEAP framework document. Older version detail should stay out of active docs unless it applies to the current framework; use Git history, release notes, and release tags for older context.

## Framework name

**LEAP - Layered Execution & Alignment Protocol**

LEAP is a software delivery framework for turning rough software intent into pressure-tested direction, source-grounded plans, and safe, bounded, implementation-ready AI coding-agent handoffs.

The current LEAP lifecycle is:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

Lifecycle terms:

- **LEAP Charter:** Establishes or reconciles the project direction, source-of-truth documents, roadmap, baseline assumptions, and implementation posture.
- **LEAP Recon:** Investigates a focused area, gap, risk, feature, dependency, contract, or architectural question.
- **LEAP Prompt:** Produces Codex-ready instructions for analysis, documentation, implementation, or remediation.
- **Implementation:** The execution of the approved LEAP Prompt by Codex or another coding agent.
- **Validation/Handoff:** The required completion step where Codex verifies changes, checks docs/tests, summarizes work, and recommends follow-up prompts.

LEAP LHS is not a mandatory lifecycle stage. It is a structured LEAP Prompt format for layered implementation work using the House Standard. Use it when work is layered, staged, or large enough to require House Standard-style execution. Not every LEAP Prompt is an LHS prompt.

---

## AGENTS.md and Agent Pack governance

LEAP AGENTS.md templates are distributed from the dedicated **LEAP Agent Pack** repository:

```text
https://github.com/mjcataldi/leap_agent_pack
```

The Agent Pack gives downstream repositories stable template IDs, hidden metadata, managed sections, and manifests that can be inspected during LEAP Recon.

Agent Pack governance rules:

- Keep distributable AGENTS.md templates in `leap_agent_pack`, not in the framework repository.
- Treat repository-root `AGENTS.md` files as installed downstream copies or repo-specific guidance, not canonical distributable templates.
- Use the Agent Pack manifests as the current Agent Pack source of truth.
- Use `leap-agent-pack-vX.Y.Z` tags for Agent Pack releases.
- Use notify/manual-merge updates only; never overwrite project or local sections automatically.
- Treat AGENTS.md version detection as LEAP Recon work.

AGENTS.md setup is LEAP adoption setup, not a new lifecycle phase. Do not reintroduce Phase 0 for AGENTS installation; use LEAP Charter for project direction and source-truth reconciliation.

---

## Relationship model

```text
LEAP Framework
  |-- LEAP Charter
  |   |-- Greenfield Mode
  |   `-- Brownfield Mode
  |
  |-- LEAP Recon
  |   |-- Investigation / discovery / pressure testing
  |   `-- Dependency & Contract Recon
  |
  |-- LEAP Prompt
  |   |-- Charter Prompt
  |   |-- Recon Prompt
  |   |-- Standard Implementation Prompt
  |   |-- Fix Prompt
  |   |-- Refactor Prompt
  |   |-- Governance Prompt
  |   |-- Validation Prompt
  |   `-- LHS Prompt
  |
  `-- Validation / Handoff
```

## Prompt family and LHS usage

LEAP Prompt is the broad category of Codex-ready or agent-ready instruction artifacts generated from Charter, Recon, user intent, or approved implementation scope.

LEAP LHS is the **Layered House Standard** prompt format used for staged implementation work. It is part of the LEAP Prompt family, not a separate lifecycle phase.

| Prompt Type | Purpose | Use LHS? |
| --- | --- | --- |
| [Charter Prompt](../prompts/leap-charter-standard.md) | Establish or reconcile direction, docs, roadmap, baseline | Sometimes |
| [Recon Prompt](../prompts/leap-recon-standard.md) | Investigate focused risk, repo reality, or implementation uncertainty | Usually no |
| [Standard Implementation Prompt](../prompts/leap-prompt-standard.md) | Small or medium implementation change | Sometimes no |
| [Fix Prompt](../prompts/leap-prompt-standard.md) | Specific bug or remediation | Usually no |
| [Refactor Prompt](../prompts/leap-prompt-standard.md) | Larger structural change | Often yes |
| [Governance Prompt](../prompts/leap-governance-pass-standard.md) | Repo/process/source-of-truth cleanup | Sometimes |
| [Validation Prompt](../prompts/leap-prompt-standard.md) | Verify tests/docs/acceptance and summarize handoff | Usually no |
| [LHS Prompt](leap.md) | Staged implementation sequence | Yes |

### Implementation Gravity

Implementation Gravity is the amount of coordination, risk, dependency ordering, testing, documentation, and rollback concern attached to a task. Higher implementation gravity increases the likelihood that the task should use LHS.

Use LHS when two or more of these are true:

```text
- The task touches more than 3 files.
- The task affects more than one system area.
- The task has dependency order.
- The task needs tests and docs.
- The task should be committed in phases.
- The task has meaningful rollback risk.
- The task changes architecture, data contracts, or user workflows.
- The task is part of a named layer.
- The task may generate follow-up work.
- The task needs explicit acceptance criteria.
```

Do not use LHS when:

```text
- The work is pure analysis.
- The work is early brainstorming.
- The work is a one-file edit.
- The work is a small copy/doc fix.
- The work is a quick bug fix with obvious scope.
- The work would add ceremony without reducing risk.
```

Charter does not use LHS by default. Greenfield Charter should usually avoid LHS during early product shaping, naming, ideation, MVP definition, or strategic discovery. Greenfield Charter may use LHS when it is creating a staged repo/docs foundation. Brownfield Charter should usually begin as a non-mutating discovery/reconciliation pass; it may use or generate LHS only after the plan is clear and the work needs staged documentation changes, archive moves, migration maps, AGENTS updates, prompt backlog updates, or link/source-truth validation.

Recon usually should not use LHS. Recon should normally answer what is true, what is broken, what the risks are, and what should happen next. Recon may recommend LHS prompts, but should not mutate runtime code or broad repo structure unless explicitly authorized.

---

## 1. Core hard rules

```text
No clarity, no build.
No source-of-truth baseline, no Recon.
No repo-reality inspection, no implementation prompt for existing repos.
No MVP or scope boundary, no layer plan.
No concrete non-goals, no coding-agent prompt.
No stop conditions, no agent handoff.
No explicit execution profile, no agent-ready handoff.
No parallel-agent ownership map, no parallel-agent launch.
Repo reality outranks planning language unless a human explicitly decides otherwise.
Generated docs are Draft until marked Active or Canonical.
Archived docs are historical unless a current canonical document explicitly references them.
Use the lightest LEAP mode that controls the actual risk.
Use the lightest agent reasoning level that controls the implementation risk.
Ask until the idea becomes buildable, then stop asking and build only the bounded task.
```

LEAP may help clarify vague ideas. LEAP may not convert vague ideas or stale documentation directly into implementation plans, layer plans, or coding-agent prompts.

A coding agent must receive a bounded task packet, not a broad wish.

---

## 2. What LEAP is for

Use LEAP when:

```text
- the idea is vague
- the repo already has code
- docs may be stale
- docs conflict with repo reality
- old roadmaps or implementation plans may compete with current docs
- the task spans multiple files
- data models, APIs, auth, billing, AI behavior, privacy, security, or user trust are involved
- multiple people or agents may touch the same system
- the agent must know when to stop instead of guessing
```

Do not use full LEAP when:

```text
- the task is tiny
- the scope is obvious
- one file is affected
- no shared contract changes
- no strategic ambiguity
- no sensitive data, auth, billing, migration, AI behavior, or architecture risk
```

Use Small Project Mode or a Quick LEAP Brief for low-risk work.

---

## 3. Ideation Loop

Humans often begin with an intuitive picture of the solution. That picture may feel complete, but the gaps are often filled by assumptions, optimism, preference, frustration, or urgency rather than mechanisms.

LEAP treats ideation as a clarification loop:

```text
Intent -> Questions -> Evidence labels -> Assumption ledger -> Pressure test -> Revised intent -> Gate decision
```

The loop continues while hard blockers remain.

Question-loop rule:

```text
Ask the fewest questions needed to make the next safe gate decision.
If the next gate decision is still unsafe, ask another small question round.
Do not ask a giant question dump when a focused round will clarify the next blocker.
Do not proceed to implementation planning while hard blockers remain.
```

---

## 4. Intake classifier

Every LEAP run starts by classifying the request.

| Request Type | Default LEAP Path | Escalate When |
| --- | --- | --- |
| Small task | [Quick LEAP Brief](user/quick-leap-brief.md) or Small Project Mode | Scope is unclear, shared contracts change, dependency contracts drift, tests are missing, or repo/docs conflict |
| New product idea | [LEAP Charter - Greenfield Mode](leap-charter.md) | User/problem/workflow/MVP/non-goals are vague |
| Major new feature | [LEAP Charter](leap-charter.md) -> [Recon](../templates/leap-recon-lite-template.md) | User-facing workflow, data model, AI behavior, auth, billing, or privacy changes |
| Existing repo layer | [LEAP Charter - Brownfield Mode](leap-charter.md) or [Recon](../templates/leap-recon-lite-template.md) | Stale docs, open PRs, branch drift, partial implementation, or unclear layer boundary |
| Strategic pivot | [Brownfield Charter](leap-charter.md) -> [Recon](../templates/leap-recon-lite-template.md) | User, MVP, architecture, monetization, risk, or layer sequence changes |
| Parallel-agent work | Ownership preflight -> per-agent [Recon](../templates/leap-recon-lite-template.md)/[Prompt](../templates/leap-prompt-template.md) | Shared files, schemas, APIs, generated types, migrations, auth, or state machines are involved |

Default rule:

```text
Ask the fewest questions needed to make the next safe gate decision.
```

---

## 5. Readiness gates

LEAP uses readiness gates for user-facing decisions.

| Gate | Meaning | Allowed Output |
| --- | --- | --- |
| C0: Blocked | Idea, docs, or task are too vague for safe progress | Discovery questions only |
| C1: Discovery Ready | Enough context exists to explore the problem | Charter discovery note |
| C2: Concept Ready | User, problem, and current workflow are understandable | Concept draft and assumption ledger |
| C3: Pressure-Test Ready | Concept is specific enough to challenge | Alternatives/no-build/MVP pressure test |
| C4: Planning Ready | MVP boundary, non-goals, risks, and source-truth direction are clear | Recon request, layer plan, or prompt backlog |
| C5: Coding-Prompt Ready | Source truth, repo reality, scope, tests, stop conditions, and execution profile are clear | Bounded coding-agent prompt |

Hard blocker rule:

```text
A high readiness impression does not override a hard blocker.
```

Hard blockers include missing target user, missing problem, missing current workflow, missing MVP boundary, missing concrete non-goals, unexamined sensitive-data risk, unresolved source-of-truth conflict, unknown repo reality for existing repos, unapproved architecture decision, missing tests/verification path, missing human approval, missing agent/tool, missing model, or missing reasoning level.

---

## 6. LEAP Charter

LEAP Charter is the initial solution-alignment process used to establish or reconcile a project before implementation begins or continues.

Full Charter guidance lives in [`docs/leap-charter.md`](leap-charter.md).

### Greenfield Mode

Greenfield Mode is used for brand-new projects, early-stage ideas, or solutions that do not yet have a stable repo, roadmap, architecture, or documentation structure.

It should help create or organize product mission, target users, MVP boundary, strategic goals, initial architecture direction, data model assumptions, roadmap, layer plan, prompt backlog, AGENTS.md guidance if applicable, and the first recommended Recon or prompt sequence. It should recommend LHS only when staged repo/docs foundation work is actually needed.

Greenfield Mode should not overbuild. It should create enough structure to start safely and intentionally.

### Brownfield Mode

Brownfield Mode is used for existing or mid-buildout projects where LEAP needs to inspect the repo, reconcile documentation, identify gaps, establish source-of-truth docs, and prepare future LEAP Recon, LEAP Prompt, or LHS work.

Brownfield Mode may update documentation, organization, naming, and planning artifacts directly. It should generally avoid runtime implementation changes unless explicitly requested.

Brownfield reconciliation policy:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Brownfield outputs should include document inventory, source-of-truth recommendation, gap register, migration map, reconciliation notes, prompt backlog recommendations, and next LEAP Recon/Prompt/LHS sequence. Brownfield Charter may use LHS only after the reconciliation plan is clear and the repo-changing documentation work needs staged execution.

---

## 7. Documentation reconciliation

LEAP Charter should not simply rename legacy docs or delete old docs. It should reconcile them.

Preferred brownfield approach:

1. Create or confirm the canonical documentation structure.
2. Absorb useful current content into canonical docs.
3. Preserve original legacy docs in an archive folder.
4. Add clear archive/deprecation headers where appropriate.
5. Create a migration map showing old doc -> new canonical location -> status.
6. Update README, docs entry points, and AGENTS.md so humans and LLMs know where to begin.

Legacy document classifications:

| Classification | Meaning | Recommended Action |
| --- | --- | --- |
| Canonical | Current source of truth | Keep or move into canonical docs structure |
| Supporting | Useful secondary detail | Keep near relevant canonical docs or reference from them |
| Current but poorly organized | Useful but structurally messy | Absorb into canonical docs, archive original |
| Partially useful | Mix of current and stale information | Extract useful content, archive original |
| Stale | No longer reflects current direction | Archive with deprecation note |
| Conflicting | Contradicts current strategy, code, or roadmap | Record conflict, resolve in canonical docs, archive original |
| Duplicate | Repeats content covered elsewhere | Consolidate, archive duplicate |
| Completed implementation plan | Old TODO or phase plan already implemented | Archive or convert remaining items to backlog |
| Misleading | Likely to confuse future work | Archive with explicit warning header |

---

## 8. Source-of-truth protocol

No Recon, layer plan, or coding prompt may proceed without an active source-of-truth baseline or an explicitly scoped minimum viable source-truth list.

Minimum viable source truth:

```text
1. Strategic plan, Charter output, or equivalent baseline strategy
2. Source-of-truth manifest or explicit source list
3. Current layer/task description
4. Repo reality summary when repo exists
5. Explicit stale/archive/do-not-use docs list
6. LEAP framework version being used
```

For a small solo project, this can be compressed into one doc. For AI-heavy teams, separate the documents.

### Source-of-truth hierarchy

When sources conflict, use this hierarchy unless a human explicitly decides otherwise:

```text
1. Running implementation / repo reality
2. Current target branch diff
3. Merged code on base branch
4. Database schema and migrations
5. Tests and fixtures
6. Canonical docs
7. Active ADRs / decision records
8. Current layer plan
9. Recent PR descriptions and execution logs
10. Old plans / archived docs
```

Old plans are not source truth unless explicitly reactivated.

---

## 9. Recommended project docs

Important docs should include a small status header with `Status`, `Last reconciled`, `LEAP mode`, `Source of truth`, and `Purpose`.

Recommended docs structure:

```text
docs/
  00_start_here.md
  01_leap_charter/
  02_product/
  03_architecture/
  04_layers/
  05_decisions/
  06_prompts/
  99_archive/
```

This is a recommended structure, not a mandatory structure for every project. LEAP should adapt to repo size, maturity, and existing conventions.

`docs/99_archive/README.md` should explain that archived docs are historical only and are not source-of-truth materials.

---

## 10. No-build protocol

Every new product idea and material feature should pass a no-build review before layer planning.

Required questions:

```text
What happens if we do nothing?
What manual workflow solves 80% of this?
What spreadsheet, checklist, template, or lightweight doc solves 80%?
What existing product solves 80%?
What integration, script, no-code automation, or service solves 80%?
What behavior/process change solves 80%?
Why is custom software still justified?
Why is AI specifically justified, if AI is proposed?
What would make this not worth building?
```

LEAP must not treat "the user wants an app" as evidence that an app should be built.

---

## 11. Build Unit sizing rule

A Build Unit is too large when it requires the agent to modify multiple unrelated capabilities, make unapproved architecture decisions, touch shared contracts without ownership clarity, or compress durable design into "good enough for now" implementation.

Split a layer before that happens.

Red flags:

```text
- one prompt touches schema, API, UI, auth, tests, docs, and workflow state
- the agent has to decide product behavior
- implementation sequence has more than 5-7 meaningful steps
- test plan becomes vague
- non-goals start sounding like "try not to"
```

---

## 12. Dependency and contract recon

Dependency & Contract Recon is a subprocess inside LEAP Recon. It checks whether the current repo declares or appears to depend on external APIs, services, provider repositories, packages, artifacts, or shared contracts, then reports whether available provider evidence may affect the current work or the broader system.

Recon should first look for a repo-level dependency register such as `leap.dependencies.yaml` or an equivalent existing convention. If none exists, Recon should report that limitation, scan for dependency candidates from config, source clients, generated contracts, package manifests, IaC, CI/CD, tests, mocks, and docs, and recommend a starter register with candidate entries clearly labeled as unconfirmed.

When contract links are declared, Recon should inspect them when accessible. Contract sources may include OpenAPI, AsyncAPI, protobuf, GraphQL schemas, provider repo URLs, documentation URLs, packages, and artifacts. Provider repo access is optional, read-only by default, permission-aware, and evidence-cited.

For OpenAPI contracts, Recon should compare provider contract metadata and structure against consumer expectations such as accepted version ranges, last verified versions, baseline hashes, compatibility policies, and declared operations used. Findings should be classified as current-work impact, general system impact, or unknown / needs verification, and each finding must include severity, confidence, evidence, and a recommended next action.

Notification automation, release blocking, ticket creation, runtime telemetry ingestion, provider repo mutation, consumer repo mutation, and full service catalog behavior are out of scope unless explicitly approved. Notification policy is metadata and manual follow-up guidance by default.

Supporting reference: [`dependency-contract-recon.md`](dependency-contract-recon.md).

## 13. Agent execution profile

LEAP is tool-agnostic. Codex is one possible implementation agent, not the framework boundary.

An agent execution profile should include:

```text
Agent / Tool:
Codex Plan Mode, for Codex-targeted prompts:
Model:
Reasoning level:
Execution Mode:
Context size:
Repo browsing ability:
Shell access:
Autonomous edit behavior:
Preferred handoff style:
Known strengths:
Known failure modes:
Required stop conditions:
Validation commands:
Commit behavior:
```

Codex Plan Mode is a user-controlled Codex UI setting. LEAP Execution Mode is the instruction inside the prompt. Codex-targeted prompts should tell the user whether Codex Plan Mode should be On, Off, or User decision required before submission.

Different agents need different constraints. Weak repo awareness requires stronger file lists and inspect-first steps. Strong autonomous editing requires tighter non-goals and forbidden-file lists.

---

## 14. Risk taxonomy

LEAP risk categories:

| Risk Area | Example | Control |
| --- | --- | --- |
| Product risk | Building the wrong workflow | [Charter](leap-charter.md) / no-build review |
| Source-truth risk | Agent follows stale docs | [Charter](leap-charter.md) reconciliation + manifest + doc lifecycle |
| Architecture risk | Feature forced into bad structure | [Recon](../templates/leap-recon-lite-template.md) + architecture right-sizing |
| Dependency contract risk | Provider contract drift breaks consumer expectations | [Dependency & Contract Recon](dependency-contract-recon.md) + evidence-based follow-up |
| Data risk | Destructive migration or data loss | Human approval + rollback plan |
| Security risk | Auth/session/permission changes | Mandatory checkpoint |
| Privacy risk | Sensitive user data exposed | Sensitive-area approval |
| AI behavior risk | Fabricated claims or unsafe automation | AI behavior constraints |
| UX risk | Flow becomes confusing or inaccessible | Acceptance criteria + manual checks |
| Collaboration risk | Agents touch same files/contracts | Ownership map + merge order |

Sensitive-area rule:

```text
If the change can affect money, identity, privacy, data durability, legal exposure, or user trust, stop and ask.
```

---

## 15. Destructive-change protocol

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

Default public rule:

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

## 16. Agent failure modes

LEAP should guard against:

```text
- hallucinating files, APIs, or business rules
- obeying stale docs over current code
- treating archived docs as current source truth
- broad refactors disguised as cleanup
- silent schema or contract changes
- adding dependencies without approval
- passing tests by weakening them
- overfitting to prompt wording instead of repo reality
- completing the task while violating non-goals
- making product decisions inside implementation
```

---

## 17. Operational outputs

### LEAP Charter output

```text
# LEAP Charter - <Project>

## 1. Mode and Intake Classification
## 2. Original User Wording
## 3. Current Understanding
## 4. Ideation Loop Status
## 5. Evidence Labels
## 6. Discovery Questions, if needed
## 7. Readiness Gate
## 8. Greenfield or Brownfield Findings
## 9. No-Build / Alternative-Solution Review
## 10. MVP Boundary or Current Scope Boundary
## 11. Concrete Non-Goals
## 12. Risks and Constraints
## 13. Documentation Baseline Recommendation
## 14. Source-of-Truth Recommendation
## 15. Gap Register
## 16. Migration Map, if Brownfield
## 17. Prompt Backlog Recommendations
## 18. Human Checkpoints Required
## 19. Recommended Next LEAP Recon / LEAP Prompt / LEAP LHS
## 20. Gate Decision / Next Step
```

### Recon output

```text
# LEAP Recon - <Target Area, Layer, Feature, Dependency, Contract, Risk, or Question>

## 1. Framework Interpretation
## 2. Source-of-Truth Manifest Check
## 3. LEAP Charter / Baseline Gate Check
## 4. Ideation Loop Residual Questions
## 5. Repo Reality Reconciliation
## 6. Branch / Worktree / PR Drift Review
## 7. Documentation Lifecycle Review
## 8. Strategic Plan Reconciliation
## 9. Existing Functionality Collision Check
## 10. Stale Assumption Scan
## 11. Cross-Layer Impact Scan
## 12. Layer Boundary Review
## 13. Generated / Refined Build Unit Inventory
## 14. Recommended Build Sequence
## 15. Dependency and Destructive-Change Review
### Dependency & Contract Recon, when relevant
## 16. Risk Taxonomy Review
## 17. Architecture Right-Sizing Review
## 18. Human Checkpoints Required
## 19. Execution Log / Drift Ledger Expectations
## 20. Coding-Agent Risk Forecast
## 21. Recommended Agent Execution Configuration
## 22. Clarification Questions Before LEAP Prompt Generation
## 23. Gate Decision / Next Step
```

### Prompt output

```text
# <Solution> - LEAP Prompt - <Target Layer or Task>

## 1. Prompt Type and LHS Decision
## 2. User Action Before Codex Submission
## 3. Agent Execution Configuration
## 4. Objective
## 5. Current Repo Reality
## 6. Source-of-Truth Instructions
## 7. Materiality / Assumption Handling
## 8. Scope
## 9. Constraints
## 10. Implementation Sequence
## 11. Verification
## 12. Stop Conditions
## 13. Branch / Worktree / Commit Instructions
## 14. Source-of-Truth Update Policy
## 15. Completion Report Format
```

### Validation/Handoff output

```text
Summary of changes
Files changed
Tests/checks run
Tests/checks not run
Docs updated or needing update
Stop conditions encountered
Risks and follow-ups
Recommended next LEAP Recon / LEAP Prompt / LEAP LHS
```

---

## 18. Canonical current documentation

The active repository uses canonical current files instead of versioned active filenames.

```text
docs/leap.md
docs/leap-charter.md
prompts/leap-charter-standard.md
prompts/leap-recon-standard.md
prompts/leap-prompt-standard.md
prompts/leap-governance-pass-standard.md
```

Older version detail is preserved through Git history, release notes, and release tags when present. Active docs should stay focused on current source truth.

Compatibility stubs remain at:

```text
prompts/leap-phase-0-standard.md
templates/leap-phase-0-template.md
```

Current Agent Pack source:

```text
https://github.com/mjcataldi/leap_agent_pack
```

---

## 19. Repository maintenance rule

Active framework and prompt files should use canonical current paths:

- keep the current framework at `docs/leap.md`
- keep Charter guidance at `docs/leap-charter.md`
- keep current operational prompts under `prompts/`
- do not restore old versioned framework files unless there is a specific compatibility reason
- keep active release notes focused on current/unreleased changes and the current baseline
- use Git history and release tags for older version detail

The short rule:

```text
No clarity, no build.
No source truth, no Recon.
No repo reality, no implementation plan.
No stop conditions, no coding task.
No execution profile, no agent-ready prompt.
Ask until the idea becomes buildable, then stop asking and build only the bounded task.
```
