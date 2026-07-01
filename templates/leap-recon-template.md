# LEAP Recon Request Template

Use this template after Charter is complete, not needed, or the project already has sufficient source truth.

Recon investigates a Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, question, or legacy Layer.

Every Recon begins with Baseline Freshness Check. Charter is not required before every Recon.

For smaller work, use [`LEAP Recon Lite`](leap-recon-lite-template.md).

```text
Run LEAP Recon using the current LEAP Framework.

Charter / baseline status:
- Charter complete? yes / no / not applicable because source truth is sufficient
- Charter mode: Greenfield / Brownfield / unknown / not applicable
- Charter gate decision:
- Ideation Loop status:
- Human approvals granted:
- Known open questions:

Strategic and planning context:
- Mission / Project Charter path:
- Strategic Outcomes path:
- Current Strategic Outcome:
- Initiative registry path:
- Current Initiative:
- Active Roadmap path:
- Roadmap placement, if any:
- Domain map path:
- Affected Domains:
- Canonical Architecture docs:
- Affected Architecture areas:
- Delivery Unit path / ID, if used:
- Build Unit / bounded task:
- Delivery Unit collapse rationale, if omitted:

Source-of-truth manifest:
- Manifest path or pasted manifest:
- LEAP Baseline State source: AGENTS.md / leap.baseline.yaml / other / none
- Baseline record path:
- MVP or scope boundary path:
- Active decisions / ADRs:
- Prompt backlog path:
- Execution log / drift ledger path:
- Cross-Initiative / Cross-Domain impact map path:
- Dependency register path:
- Brownfield document inventory path:
- Gap register path:
- Migration map path:
- Legacy Layer docs requiring classification:
- Stale / archived / do-not-use docs:
- AGENTS.md path and Agent Pack status:

Solution overview:
- Solution name:
- Solution type:
- High-level goal:
- Current state:
- Known constraints:

Target area:
- <Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain,
  Architecture area, feature, dependency, contract, risk, question,
  legacy Layer, or bounded task>

Repository / branch context:
- Repository or repositories:
- Base branch:
- Target branch / worktree:
- Open PRs or active branches:
- Areas likely affected:
- Areas not to touch:
- Dependency or contract sources:

Execution settings:
- Buildout mode: Rapid POC / Standard / Production-safe / Refactor
- LEAP process tier: Standard / Thinking Extended / Pro Standard / Pro Extended / recommend
- Agent / Tool: Codex / Claude Code / Cursor / other / recommend
- Codex Plan Mode: On / Off / User decision required / recommend
- Model:
- Reasoning level: Low / Medium / High / Extended / recommend
- Execution mode: implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only / recommend
- Production compatibility required: yes / no / unknown
- Destructive changes allowed: yes / no / recommend
- One Build Unit per commit: yes / no / recommend
- Source-of-truth updates required: yes / no / recommend
- Execution log / drift ledger update required: yes / no / recommend

Required behavior:
- Perform Baseline Freshness Check using AGENTS.md, baseline metadata,
  Project Charter, Strategic Outcomes, Initiative registry, Roadmap,
  Domains, Architecture, Delivery / Build plans, and relevant repo reality.
- Continue normally when fresh enough.
- Continue with disclosed limitations for minor drift.
- Recommend Charter / Governance, limited-scope Recon, or deferral for material drift.
- Stop for unsafe source-truth conflict.
- Do not silently create leap.baseline.yaml.
- Apply Materiality Gate before asking questions.
- Inspect discoverable evidence before asking.
- Treat Brownfield Charter outputs as source-truth inputs.
- Classify docs as Canonical, Supporting, Current but poorly organized,
  Partially useful, Stale, Conflicting, Duplicate, Completed plan,
  Misleading, Archived, or Unknown.
- Inspect repo reality and search for existing functionality.
- Inspect branch / worktree / PR drift.
- Run Dependency & Contract Recon when relevant.
- Check cross-Initiative, cross-Domain, cross-repository, contract,
  release-order, and Architecture impacts.
- Treat Roadmap as a scheduling and dependency view, not Initiative ownership.
- Treat Domains as persistent and many-to-many with Initiatives.
- Determine whether the target is Initiative-sized, Delivery-Unit-sized,
  Build-Unit-sized, Domain-oriented, Architecture-oriented, a Phase,
  or an ambiguous legacy Layer.
- Refine Delivery Units only when meaningful release, enablement, adoption,
  demonstration, or cross-repository boundaries exist.
- Allow Delivery Unit collapse for small work.
- Generate Build Units only after Initiative and Delivery boundaries are clear.
- Do not define Build Units as necessarily independently deployable.
- Classify legacy Layer meaning before migration.
- Preserve the LEAP name, Layered House Standard, LEAP LHS,
  qualified Architecture Layers, public paths, and compatibility references.
- Recommend explicit Agent Execution Configuration before Prompt generation.
- Recommend LHS only when implementation gravity warrants staged execution.
- Keep Recon non-mutating unless explicitly authorized.

Return Recon only. Do not generate the implementation Prompt yet unless I explicitly request it after the gate decision.
```

## Expected Recon sections

```text
# LEAP Recon - <Target>

## 1. Framework Interpretation
## 2. Source-of-Truth Manifest Check
## 3. Baseline Freshness Check
## 4. Charter / Baseline Gate Check
## 5. Ideation Loop Residual Questions
## 6. Materiality Check
## 7. Repo Reality Reconciliation
## 8. Branch / Worktree / PR Drift Review
## 9. Documentation Lifecycle Review
## 10. Strategic Plan Reconciliation
## 11. Existing Functionality Collision Check
## 12. Stale Assumption Scan
## 13. Cross-Initiative / Cross-Domain Impact Scan
## 14. Planning Boundary Review
## 15. Legacy Layer Classification, when relevant
## 16. Generated / Refined Delivery Unit Inventory, when relevant
## 17. Generated / Refined Build Unit Inventory
## 18. Recommended Build Sequence
## 19. Dependency and Destructive-Change Review
### Dependency & Contract Recon, when relevant
## 20. Risk Taxonomy Review
## 21. Architecture Right-Sizing Review
## 22. Human Checkpoints Required
## 23. Execution Log / Drift Ledger Expectations
## 24. Coding-Agent Risk Forecast
## 25. Recommended Agent Execution Configuration
## 26. Clarification Questions Before Prompt Generation
## 27. Gate Decision / Next Step
```

## Materiality Check format

```text
### Material Unknowns
### Assumptions Proceeding Under
### Deferred Non-Material Details
### Question Decision
```

## Dependency & Contract Recon format

```text
### Dependency & Contract Recon

- Dependency register found:
- Dependency register path:
- Dependencies declared:
- Contract sources accessible:
- Contract sources inaccessible:
- High-confidence breaking risks:
- Potential breaking risks:
- Current-work impacts:
- General system impacts:
- Needs verification:

Current-work impact:
| Dependency | Contract | Finding | Severity | Confidence | Evidence |
|---|---|---|---|---|---|

General system impact:
| Dependency | Contract | Finding | Severity | Confidence | Evidence |
|---|---|---|---|---|---|

Needs verification:
| Dependency | Issue | Reason | Recommended next action |
|---|---|---|---|
```

## Recommended Agent Execution Configuration format

```text
| Field | Recommendation | Rationale |
|---|---|---|
| Agent / Tool | Codex / Claude Code / Cursor / other | Why |
| Codex Plan Mode | On / Off / User decision required | Why |
| Model | Exact model or project default | Why |
| Reasoning Level | Low / Medium / High / Extended | Why |
| Execution Mode | implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only | Why |
| Scope Scale | small task / Build Unit / Delivery Unit / Initiative / multi-repo Initiative / repo-wide maintenance | Why |
| Repository | Repo or repositories | Why |
| Branch / Worktree | Target context | Why |
| Permissions | Allowed changes | Why |
| Validation | Tests and checks | Why |
| Commit Guidance | Commit posture | Why |
```

## LHS note

Recon may recommend LHS but should not default to it. LEAP LHS stages implementation; it does not define the strategic documentation hierarchy.
