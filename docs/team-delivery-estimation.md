<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-estimation-reference
  authority: canonical
  applies_to: downstream-leap-projects
END_LEAP_DOC_METADATA
-->

# Team & Delivery Capacity Estimation

LEAP provides an **advisory estimation method**, not a staffing, timekeeping, resource-allocation, or project-management system of record. Apply this method only when effort, capacity, or forecast assumptions are material to Charter, Recon, Prompt, or Roadmap decisions. Small projects can use a short estimate with disclosed assumptions; no new register, database, integration, or extra planning hierarchy is mandatory.

## Authority and discovery

At the start of a materially capacity-dependent decision, inspect approved project sources before asking questions:

| Information | Preferred authority | LEAP's permitted use |
|---|---|---|
| Work items, owners, actual assignments, status, accepted estimates and worklogs | Project-designated tracker (for example Jira), where configured | Read with permission; propose, never silently overwrite |
| Planned allocations, availability, leave and cross-Initiative commitments | Project-designated resource system or attested team lead | Read and cite; distinguish confirmed and provisional |
| Code changes, PRs, reviews, test results and merges | Source control and CI | Workflow and complexity evidence, **not recorded labor hours** |
| Role, capabilities, domain expertise and available reviewer capacity | Approved team source or explicit project-owner input | Bounded, purpose-specific planning context |
| Mission, scope, dependencies and acceptance criteria | Project Charter, Initiative / Build Unit and canonical solution documents | Define the work and non-goals |
| Estimation method and output contract | This LEAP Framework document | Advisory guidance, not a replacement ledger |

The project may choose a system other than Jira; do not hardcode a provider, field, API, connector or availability assumption. Do not create a competing LEAP-owned roster, allocation register or estimate store. A time-stamped, source-attributed *working snapshot* is acceptable for an estimate, but must be labeled non-authoritative, incomplete where appropriate, and refreshed after material change.

When the designated source is inaccessible, record **not verified / unavailable**, not **no assignments / no worklogs**. Ask the responsible person only if that missing fact changes the next safe decision. Otherwise generate a conditional scenario or effort-only recommendation.

## Team model

Keep humans and AI tools or agents in separate categories. For people or **role placeholders**, the minimum useful, permissioned context is:

- identity or placeholder, capability areas, and relevant responsibility;
- reported capacity and relevant period, with the unit and source;
- Initiative-level allocations when material, including other known commitments;
- confirmed versus provisional status; human decision-maker or reviewer when required.

A person may span Initiatives; the same hours cannot be counted twice. Availability is not equivalent to calendar hours; include known meetings, operations, leave, mentoring, review and other committed work when those materially affect throughput. When source information is incomplete, flag potential overcommitment rather than claiming confirmed available hours. Identify critical specialist and human-review bottlenecks before assuming more headcount shortens delivery.

AI tools and agents are *capabilities with supervision and validation overhead*, not independent FTEs. Note approved tool and task suitability where known, permission/quotas if material, and the human supervision, integration, security and review burden. Do not assume parallel agents multiply end-to-end throughput.

## Evidence and calibration

1. **Direct evidence:** reliable actual worklogs or recorded work sessions, known capacity, accepted scope, completed comparable work and outcomes. Assess worklog completeness, definition of "done", and tool/project comparability.
2. **Contextual evidence:** issue state histories, PR opened/reviewed/merged times, commits, files affected, test coverage, rework, review cycles, handoffs, scope changes and known tool usage. Use for elapsed flow, task matching and risk—not as a substitute for actual worked hours.
3. **Assumptions or scenarios:** role placeholders, unknown capacities, unmatched tasks, extrapolated task similarity, and speculative AI acceleration. Mark these explicitly and prevent them from being mistaken for measured baselines.

**Forbidden inference:** commit count, code volume, the interval between first/last commit, author/committer timestamps, or PR elapsed time **do not equal labor hours**. Squashes, rebases, bots, parallel work, idle gaps and offline research defeat this inference. Commit events can inform change-flow analysis; actual effort requires credible time evidence or is an uncertain estimate.

Use comparable historic work only after checking task category, research depth and ambiguity, Architecture impact, integration/dependencies, acceptance and security requirements, validation, team context and completion criteria. Retain sample count, recency, source, exclusions and material differences when calibration is claimed. Do not assert percentile ranges or quantitative confidence without a defensible sample and method.

Do not use individual output/activity metrics as a productivity ranking, employee appraisal or surveillance proxy. Prefer team/workflow-level calibration. Person-linked historical analysis requires approved purpose, access, applicable privacy and employment policy, and data minimization; refuse or omit it when authorization is missing. Respect worklogs and repository access boundaries across organizations and contractors.

## Estimation workflow

1. **Bound the work.** Use a clear outcome, acceptance criteria, research/discovery work, complexity, dependencies, testing, integration, review and release obligations. Record unknowns that affect the estimate.
2. **Inspect authorized evidence.** Locate the configured source of record and available comparable completed work. Identify evidence gaps rather than fabricating availability, time or an individual's capability.
3. **Estimate implementation effort.** Produce a person-effort range (or explicitly qualitative uncertainty if numeric evidence is too weak); separate research, design, build, verification, review and rework where useful. Calibrate against reliable measured effort only when comparable.
4. **Estimate calendar delivery separately.** Condition the timeline on stated Initiative allocations, availability periods, specialist bottlenecks, parallelizability, dependencies, review queues, waiting time and critical path. Never use \`effort / total headcount\` as a universal schedule calculation.
5. **Handle AI assistance explicitly.** Credit measurable reductions only from comparable evidence that includes prompt/agent setup, human oversight, integration, failures and validation. Where evidence is absent, show an *illustrative AI-assisted scenario*, not an evidence-backed forecast or guaranteed multiplier.
6. **Review and propose.** Present assumptions, cited evidence and source timestamps, comparability, exclusions, effort and duration ranges, uncertainty, confidence rationale, risks, required human approvals and re-estimation triggers. A project lead accepts/rejects the proposal in the external authoritative workflow; no silent write-back.
7. **Calibrate after delivery.** Compare forecast effort with credible recorded effort when available, and forecast elapsed time with actual workflow dates separately. Record causes of deviation in the designated project system. Avoid persisting a shadow team ledger in LEAP.

### Required recommendation shape (when estimation is material)

\`\`\`text
Work item / scope:
Authoritative tracker and evidence timestamp:
Human / role capability and allocation assumptions:
AI assistance (observed / modeled / unavailable):
Comparable historical samples and exclusions:
Proposed effort (range, person-hours; or reason no numeric estimate is defensible):
Conditional delivery duration (range / calendar scenario; or not currently estimable):
Research / build / review / verification and integration assumptions:
Dependencies and review bottlenecks:
Evidence strength, uncertainty and confidence rationale:
What would change the estimate / refresh triggers:
Approver and next action in the external system:
\`\`\`

The recommendation is not the external system's accepted estimate. Do not manufacture timestamps, hours, precise probabilities, comparative performance scores or completion dates. Scope, staffing, availability, task ownership, Architecture, dependencies, or validation changes can invalidate the scenario; flag affected forecasts for reassessment rather than quietly repeating them.

## Charter and Roadmap interaction

At Charter, identify the **owner of operational truth** and whether the staffing/capacity picture is known, provisional, or unavailable. Ask a material question only when an answer is necessary for the next safe planning decision. A greenfield Charter may use role placeholders and conditional staffing scenarios; missing named staff does **not** itself block Charter or effort-only estimates. Do not imply that a conditional timeline is a committed date.

A Roadmap may *reference* the proposed estimate and assumption set, but staffing allocations, accepted estimates and work status stay authoritative in the designated external system. Do not establish a second scheduling authority. An estimate is not a new Initiative, Delivery Unit, Build Unit or permanent LEAP artifact.

In AGENTS.md, store concise guidance/pointers to the configured work and capacity systems **if known**; never copy frequently changing assignments, allocations or individual performance histories into agent instructions. If no source is configured, use a clearly unconfigured pointer and conditional planning.

## Boundaries and checkpoints

- Read-only authorized evidence gathering is the default. Write-back, changing committed dates or changing tracked estimates require explicit, separate authorization and field mapping.
- Do not infer missing individual productivity data or use unaudited AI tools with sensitive personnel information.
- Stop for missing authorization, unsafe privacy exposure, material conflicting source truth, or externally consequential changes without approval.
- Do not add an obligatory Jira connector, staffing database, persistent snapshot, ML model, time-tracking application or numeric productivity multiplier for this method.
- Execution **surface routing** (tool cost/capabilities, see [Execution Routing](execution-routing.md)) is distinct from project delivery **capacity estimation**; reuse available capability evidence without treating them as the same decision.
