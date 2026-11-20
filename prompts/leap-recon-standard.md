# LEAP Recon - Standard Operational Prompt

Run LEAP Recon using the current LEAP Framework.

Recon investigates a focused Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain, Architecture area, feature, dependency, contract, risk, question, or legacy Layer. It is the source-truth, repo-reality, drift, dependency, risk, planning-boundary, capability-selection, and implementation-safety pass before Prompt generation.

Recon is normally investigative and non-mutating unless explicitly authorized.

LEAP Charter is not required before every Recon; see the [LEAP lifecycle](../docs/leap.md). Every Recon begins with a lightweight Baseline Freshness Check.

## Canonical project-documentation model

For traceability, use the [project documentation model](../docs/project-documentation-model.md) when the project already uses it; otherwise link the external work item. Skills are reusable execution capabilities, not planning levels; see [LEAP Skills](../docs/leap-skills.md).

## Investigation depth

Stop investigating when the next safe decision is clear. Inspect only what can change the gate decision, scope, risk, or Prompt content.

## Required behavior

You must:

1. perform Baseline Freshness Check
2. apply Materiality Gate before asking questions, including any explicit `No Gate` modifier, and carry residual Ideation Loop questions into it
3. require or construct a source-of-truth manifest; treat Brownfield Charter outputs as valid inputs
4. classify docs and legacy planning artifacts
5. inspect repo reality before implementation planning; treat it as operational truth when docs conflict unless a human decides otherwise
6. inspect branch, worktree, and PR drift when available
7. search for already-existing functionality
8. detect stale assumptions, docs, Prompts, Roadmap claims, and legacy Layer claims
9. inspect `AGENTS.md` and baseline metadata when present
10. run Dependency & Contract Recon when relevant
11. identify cross-Initiative, cross-Domain, cross-repository, contract, release, and merge-order impacts
12. evaluate risk and destructive-change implications
13. perform Planning Boundary Review before generating Build Units
14. refine Delivery Units only when meaningful release, enablement, adoption, demonstration, or cross-repository boundaries exist; generate Build Units only after Initiative and Delivery Unit boundaries are clear enough
15. perform Capability / Skill Review after Build Unit boundaries are clear enough; prefer ordinary reasoning when no explicit Skill materially improves execution
16. identify human checkpoints
17. distinguish LEAP process tier from Agent Execution Configuration
18. derive required validation, capabilities, and permissions before recommending an agent/tool; recommend the least-cost eligible surface, plus an escalation surface when needed
19. state the expected verification state at each material handoff
20. recommend Agent Execution Configuration, Skill loading posture, and commit posture when Prompt generation is allowed
21. recommend LHS only when implementation gravity warrants it
22. end with a gate decision

## Brownfield Charter inputs

When present, use Charter outputs as inputs: document inventory, canonical / supporting / do-not-use lists, planning records (Strategic Outcomes, Initiative registry, Roadmap, Domain map, Architecture, Delivery and Build Unit plans), adopted Skill sources, gap register, reconciliation notes, migration map, prompt backlog, and recommended next LEAP sequence.

If source truth remains unsafe, use `Reconcile Docs First` or `Continue LEAP Charter`.

## Baseline Freshness Check

Routing note: see [Semantic Workflow Routing](../docs/semantic-routing.md). Prefer conceptual Pressure Test when no repository evidence is needed, but keep Recon evidence-first when a proposal depends on actual code, branch or source truth. Discovery is not a mandatory prerequisite.

Answer:

```text
Is the repo/source-truth baseline fresh enough for this Recon?
```

Inspect, when available:

1. repository `AGENTS.md`
2. LEAP Baseline State or `leap.baseline.yaml`
3. source-truth entry point
4. planning records the project uses (Project Charter, Strategic Outcomes, Initiative registry, Roadmap, Domain and Architecture docs, Delivery and Build Unit plans)
5. APIs, schemas, decisions, dependencies, and contracts relevant to the target
6. archive and stale-doc guidance, gap register, migration map, and prompt backlog
7. relevant repo reality, doc-code conflicts, broken references, and stale planning claims

Use one outcome:

```text
Fresh enough
Minor drift
Material drift
Unsafe source-truth conflict
```

Normal Recon may recommend baseline metadata but must not silently create it.

## Source-of-Truth Manifest Check

```text
# Source-of-Truth Manifest Check

- Project:
- Date:
- Target branch / base branch:
- Work item: <link to issue, ticket, or planning doc>
- Initiative / Delivery Unit / Build Unit, when the project uses them:
- Planning records used, with paths:
- Canonical Architecture docs:
- Active decisions / ADRs:
- Dependency register path:
- Reusable Skill / capability sources, if any:
- Baseline record, inventory, gap register, migration map, when present:
- Legacy Layer docs requiring classification:
- Stale / archived / do-not-use docs:
- AGENTS.md path and Agent Pack status:
- Open branches / PRs affecting the work:
- Repo reality summary:
- Known doc-code conflicts:
- Human owner / approver:
- Last reviewed:
```

Skill definitions are capability instruction sources, not automatically project source truth outside the capability contract they explicitly own.

## Materiality Gate

Apply the [Materiality Gate](../docs/materiality-gate.md):

```text
INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE
```

Classify each unresolved item by consequence, discoverability, safe assumability, and hard-blocker status. Default **Materiality-Gated** mode:

```text
Hard blocker -> STOP
Discoverable -> INSPECT, then re-evaluate
Non-material -> ASSUME or DEFER
Material safely assumable and not requiring a decision now -> ASSUME + DISCLOSE
Material answer required for the next safe decision -> ASK
```

Explicit **No Gate**: ASK becomes ASSUME + DISCLOSE when safe. STOP remains STOP. No Gate does not bypass source-truth integrity, authorization, destructive-change safeguards, sensitive-area checkpoints, security/privacy requirements, public-contract approval, or required human approval.

Re-evaluate only remaining or newly exposed uncertainty. There is no minimum question count; ask no more than three targeted questions at a time unless exhaustive discovery is explicitly requested.

Record the active clarification mode and materially consequential assumptions in the Recon output.

## Required repo-reality inspection

Inspect, when available:

- target and base branches
- worktrees and open PRs
- current implementation and tests
- routes, APIs, contracts, schemas, and migrations
- UI components and workflows
- auth/session/permission behavior
- package and dependency files
- IaC and CI/CD
- canonical docs and planning records
- work item, Initiative, Delivery Unit, and Build Unit status, when used
- execution logs and impact maps

## Legacy Layer classification

When a legacy Layer appears, classify it with the [migration guide](../docs/maintainer/project-documentation-migration.md). Do not globally replace `Layer`.

## Planning Boundary Review

Start by stating how the target maps to LEAP. Then determine whether the target is:

- one or more parallel Initiatives
- one Delivery Unit
- one Build Unit
- a persistent Domain concern
- an Architecture concern
- a chronological Phase
- an ambiguous legacy Layer

A Build Unit must be bounded enough to implement, test, review, and usually commit independently without inventing product or Architecture decisions. Skills are not planning boundaries.

## Capability / Skill Review

For each Build Unit, determine:

1. whether ordinary agent reasoning and repository guidance are sufficient
2. whether reusable specialized procedure materially reduces ambiguity, repetition, risk, or domain error
3. whether a matching Skill already exists
4. the Skill source and how the target agent will load it
5. whether the Skill is required or optional
6. whether its tool requirements fit the Prompt permission ceiling
7. what Skill-specific verification is required
8. whether a missing required Skill is material enough to block Prompt generation

Use this output shape when Skills are relevant:

```text
### Capability / Skill Composition

| Build Unit | Skill | Source | Loading method | Required? | Tools / permissions | Verification |
|---|---|---|---|---|---|---|
```

Do not select a Skill merely because one exists, and do not let a Skill widen Build Unit scope, permissions, or source-truth ownership. See [Recon capability review](../docs/leap-skills.md#recon-capability-review).

## Cross-Initiative / Cross-Domain Impact Scan

Inspect whether target work affects:

- other Initiatives
- shared Delivery Units
- persistent Domains
- shared data, workflows, APIs, events, schemas, or contracts
- Architecture areas
- other repositories
- release and merge order
- existing assumptions

Legacy projects may retain `Cross-Layer Impact` as a compatibility term while migration is pending.

## Dependency & Contract Recon

When relevant, follow [Dependency & Contract Recon](../docs/dependency-contract-recon.md):

1. detect `leap.dependencies.yaml` or equivalent
2. identify dependency candidates from code, config, contracts, IaC, tests, and docs
3. inspect declared contract sources when accessible
4. compare provider evidence with expected versions and consumer usage
5. flag confirmed breaking, potential breaking, additive, and insufficient-evidence cases
6. classify as Current-work impact, General system impact, or Unknown / needs verification
7. include severity, confidence, evidence, and next action
8. keep provider access read-only and permission-aware
9. keep notification automation and cross-repo mutation out of scope unless approved

## Risk review

Include:

```text
- Product risk: low / medium / high
- Source-truth risk: low / medium / high
- Architecture risk: low / medium / high
- Dependency contract risk: low / medium / high / not applicable
- Data/security/privacy risk: low / medium / high
- AI behavior risk: low / medium / high / not applicable
- Collaboration risk: low / medium / high
- Verification risk: low / medium / high
- Coding-agent risks: likely agent mistakes to guard against in the Prompt
```

Sensitive-area rule:

```text
If the change can affect money, identity, privacy, data durability,
legal exposure, or user trust, stop and ask.
```

## Recommended Agent Execution Configuration

When the gate is `Generate LEAP Prompt`, recommend the fields in [Prompt standard section 3](leap-prompt-standard.md#3-agent-execution-configuration), with a rationale for each. Codex Plan Mode and the capability-class and surface routing fields are optional; omit them when not needed.

## Gate decisions

Use one:

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

A missing Skill does not automatically block Prompt generation. Block only when the specialized capability is material to safe execution and there is no acceptable source or bounded fallback.

## Required output

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

## Baseline output format

```text
- Baseline status: Fresh enough / Minor drift / Material drift / Unsafe source-truth conflict
- Evidence checked:
  - ...
- Source-truth confidence: High / Medium / Low / Unknown
- Reconciliation needed before proceeding: No / Recommended / Required
- Notes:
  - ...
```

## Materiality output format

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

Do not generate the implementation Prompt unless explicitly requested and the gate decision allows it.
