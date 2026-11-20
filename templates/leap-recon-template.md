# LEAP Recon Request Template

Use this template after Charter is complete, not needed, or the project already has sufficient source truth.

Recon investigates a Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, question, or legacy Layer. The governing behavior is the [LEAP Recon standard](../prompts/leap-recon-standard.md).

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

Traceability:
- Work item: <link to issue, ticket, or planning doc>
- Initiative / Delivery Unit / Build Unit, when the project uses them:
- Strategic Outcome, Roadmap placement, Domains, Architecture areas, when material:

Source-of-truth manifest:
- Manifest path or pasted manifest:
- LEAP Baseline State source: AGENTS.md / leap.baseline.yaml / other / none
- Planning records used, with paths:
- MVP or scope boundary path:
- Active decisions / ADRs:
- Dependency register path:
- Reusable Skill / capability sources, if any:
- Baseline record, inventory, gap register, migration map, when present:
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
- Clarification mode: Materiality-Gated / No Gate
- Buildout mode: Rapid POC / Standard / Production-safe / Refactor
- LEAP process tier: Standard / Thinking Extended / Pro Standard / Pro Extended / recommend
- Agent / Tool: Chat / repository-connected chat / Codex / Claude Code / Cursor / Work / other / recommend
- Model:
- Reasoning level: Low / Medium / High / Extended / recommend
- Execution mode: implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only / recommend
- Skill loading posture: native / repo-local / prompt-embedded / none / recommend
- Production compatibility required: yes / no / unknown
- Destructive changes allowed: yes / no / recommend
- One Build Unit per commit: yes / no / recommend
- Source-of-truth or execution log updates required: yes / no / recommend
- Optional, omit when not needed: Codex Plan Mode, Execution Environment Profile, relative cost constraints

Required behavior:
- Follow the LEAP Recon standard.
- Perform Baseline Freshness Check. Continue when fresh enough; disclose minor drift; recommend Charter / Governance or limited scope for material drift; stop for unsafe source-truth conflict. Do not silently create leap.baseline.yaml.
- Apply the Materiality Gate. Inspect discoverable evidence before asking. No Gate never converts STOP into proceed. Ask no more than three targeted questions at a time.
- Inspect repo reality, existing functionality, branch / worktree / PR drift, and cross-Initiative, cross-Domain, and cross-repository impacts.
- Run Dependency & Contract Recon when relevant.
- Perform Planning Boundary Review before generating Build Units, then Capability / Skill Review. Skills must not widen Build Unit scope or Prompt authority.
- Classify legacy Layer meaning before migration.
- Derive required validation and permissions before recommending an Agent / Tool and execution surface; state the expected verification state at handoff.
- Recommend LHS only when implementation gravity warrants staged execution.
- Stop investigating when the next safe decision is clear.
- Keep Recon non-mutating unless explicitly authorized.

Return Recon only. Do not generate the implementation Prompt yet unless I explicitly request it after the gate decision.
```

## Expected Recon sections

```text
# LEAP Recon - <Target>

## 1. Source-of-Truth Manifest Check
## 2. Baseline Freshness Check
## 3. LEAP Charter / Baseline Gate Check
## 4. Materiality Check
## 5. Repo Reality Reconciliation
## 6. Branch / Worktree / PR Drift Review
## 7. Documentation Lifecycle Review
## 8. Strategic Plan Reconciliation
## 9. Existing Functionality Collision Check
## 10. Stale Assumption Scan
## 11. Cross-Initiative / Cross-Domain Impact Scan
## 12. Planning Boundary Review
## 13. Legacy Layer Classification, when relevant
## 14. Generated / Refined Delivery Unit Inventory, when relevant
## 15. Generated / Refined Build Unit Inventory
### Capability / Skill Composition, when relevant
## 16. Recommended Build Sequence
## 17. Dependency and Destructive-Change Review
### Dependency & Contract Recon, when relevant
## 18. Risk Taxonomy Review
## 19. Architecture Right-Sizing Review
## 20. Human Checkpoints Required
## 21. Execution Routing Review
## 22. Recommended Agent Execution Configuration
## 23. Clarification Questions Before Prompt Generation
## 24. Gate Decision / Next Step
```

Omit sections with nothing material. Do not pad with N/A. Keep the remaining section numbers unchanged.

Folded content:

- Section 4 includes residual Ideation Loop questions.
- Section 12 opens with how the target maps to LEAP.
- Section 16 includes expected execution log or drift ledger updates.
- Section 18 includes the coding-agent risk forecast.

## Capability / Skill Composition format

```text
| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
|---|---|---|---|---|---|---|
```

## Materiality Check format

```text
### Clarification Mode
Materiality-Gated / No Gate

### Material Unknowns
### Assumptions Proceeding Under
### Deferred Non-Material Details
### Stop Conditions / Hard Blockers
### Question Decision
Proceed with assumptions / inspect sources first / ask targeted questions / stop
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

Use the fields in [Prompt standard section 3](../prompts/leap-prompt-standard.md#3-agent-execution-configuration) with a Rationale column. Codex Plan Mode and the capability-class and surface routing fields are optional; omit them when not needed.

## LHS note

Recon may recommend LHS but should not default to it. LHS stages implementation; see [LEAP LHS](../docs/leap-lhs.md).
