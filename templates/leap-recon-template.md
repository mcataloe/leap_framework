# LEAP Recon Request Template

Use this template to request a LEAP Recon pass after LEAP Charter is complete, not needed, or an existing project already has sufficient source-of-truth documentation.

Recon investigates a focused area, gap, risk, feature, dependency, contract, or architectural question.

```text
Run LEAP Recon using the current LEAP framework.

LEAP Charter / project baseline status:
- LEAP Charter complete? yes/no/not applicable because source truth is already sufficient
- Charter mode used: Greenfield / Brownfield / unknown / not applicable
- Gate decision from Charter:
- Ideation Loop status: complete / still unclear / not applicable
- Human approvals already granted:
- Known open questions:

Source-of-truth manifest:
- Manifest path or pasted manifest:
- Charter output path:
- Product strategy / project charter path:
- MVP or scope boundary path:
- Pressure-test summary path:
- Implementation strategy path:
- Layer map path:
- Prompt backlog path:
- Execution log path:
- Cross-layer impact map path:
- Dependency register path, if any:
- Brownfield document inventory path:
- Gap register path:
- Migration map path:
- Stale / archived / do-not-use docs:
- AGENTS.md path:
- AGENTS.md Agent Pack status: current / outdated / outdated with local changes / pinned / unversioned LEAP-style / non-LEAP / missing / forked-custom / malformed / unknown

Solution/system overview:
- Solution name:
- Solution type:
- High-level goal:
- Current state:
- Known constraints:

Target area:
- <Focused area, gap, risk, feature, architectural question, layer number + layer name, or bounded task name>

Repo / branch context:
- Repository:
- Base branch:
- Target branch/worktree, if known:
- Open PRs or active branches to inspect, if known:
- Areas likely affected:
- Areas not to touch:
- Dependency or contract sources to inspect, if known:
- Current work operations or provider APIs involved, if known:

Buildout settings:
- Buildout mode: Rapid POC / Standard / Production-safe / Refactor
- LEAP process tier: Standard / Thinking Extended / Pro Standard / Pro Extended / you recommend
- Agent / Tool: Codex / Claude Code / Cursor / other / you recommend
- Model: <exact model name or you recommend>
- Reasoning level: Low / Medium / High / Extended / you recommend
- Execution mode: recon-only / plan-first / implement-directly / implement-with-brief-plan / you recommend
- Production compatibility required: yes/no/unknown
- Destructive changes allowed: yes/no/you recommend
- One Build Unit per commit: yes/no
- Source-of-truth updates required: yes/no/you recommend
- Execution log / drift ledger update required: yes/no/you recommend
- Cross-layer impact map update required: yes/no/you recommend

Required gate:
- Verify whether the LEAP Charter baseline and source-of-truth manifest are sufficient.
- Confirm whether more Ideation Loop questions are needed before planning implementation.
- Treat Brownfield Charter outputs as valid source-truth inputs when present.
- Classify docs as Canonical, Supporting, Current but poorly organized, Partially useful, Stale, Conflicting, Duplicate, Completed implementation plan, Misleading, Archived, or Unknown.
- Treat archived docs as historical unless a canonical doc explicitly references them.
- Inspect repo reality before implementation planning when repo access exists.
- Search for already-existing functionality before recommending new work.
- Detect `leap.dependencies.yaml` or an equivalent dependency register when present.
- If no dependency register exists, scan for dependency candidates and clearly label generated entries as candidates.
- Inspect declared dependency contract links such as OpenAPI, AsyncAPI, protobuf, GraphQL, provider repo URLs, docs URLs, package references, and artifacts when accessible.
- For OpenAPI contracts, compare provider contract evidence against consumer expectations such as accepted versions, last verified version, baseline hash, compatibility policy, and declared operations used.
- Separate dependency and contract findings into current-work impact, general system impact, and unknown / needs verification.
- Include dependency name, type, contract source, expected and observed versions when known, operation/schema when known, severity, confidence, evidence, and recommended next action for every dependency-contract finding.
- Keep provider repo and external contract access optional, read-only by default, permission-aware, and evidence-cited.
- Keep notification automation out of scope unless I explicitly approve it; report manual follow-up recommendations only.
- Check AGENTS.md Agent Pack metadata, managed/project/local markers, and manifest status when AGENTS.md exists or adoption is in scope.
- Recommend an explicit Agent Execution Configuration before LEAP Prompt generation.
- Recommend LHS only when implementation gravity warrants staged execution.
- Keep Recon investigative and non-mutating unless I explicitly authorize changes.
- If docs and repo reality conflict, report the conflict before generating a coding-agent prompt.
- If branch/worktree/PR drift affects ownership or merge order, require resolution before prompt generation.
- If agent/tool, model, or reasoning level is missing, recommend safe defaults based on scope, ambiguity, and implementation risk.

Return only the LEAP Recon output first. Do not generate the LEAP Prompt yet.
At the end, ask any material clarification questions that should be answered before generating the LEAP Prompt.
Then remind me that I can say: "Generate the LEAP Prompt."
```

## Expected Recon sections

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

## Dependency & Contract Recon subsection, when relevant

```text
### Dependency & Contract Recon

- Dependency register found: yes/no/equivalent convention/unknown
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

## Recommended Agent Execution Configuration section

```text
## 21. Recommended Agent Execution Configuration

| Field | Recommendation | Rationale |
|---|---|---|
| Agent / Tool | <Codex / Claude Code / Cursor / other> | <why> |
| Model | <exact model name or project default> | <why> |
| Reasoning Level | <low / medium / high / extended> | <why> |
| Execution Mode | <plan-first / implement-directly / implement-with-brief-plan> | <why> |
| Scope Scale | <small task / Build Unit / sublayer / entire layer / repo-wide maintenance> | <why> |
| Validation | <tests/lint/typecheck/build/manual checks> | <why> |
```

## Recon confidence guidance

Use confidence as a heuristic, not as a blocker override:

```text
New product / baseline: 90-95%
Whole layer: 80-90%
Sublayer: 75-85%
Single Build Unit / LEAP LHS: 60-75%, default around 67%
Tiny local fix: 50-60%, if no shared contracts are touched
```

Hard blockers override confidence impressions.

## LHS note

Recon usually should not use LHS. Recon may recommend an LHS prompt, but should not default to LHS and should not mutate runtime code or broad repo structure unless explicitly authorized.
