# Agent Profiles

LEAP is tool-agnostic.

Different coding agents have different strengths, context limits, autonomy, repository access, and failure modes. LEAP captures those differences in an **Agent Execution Profile**.

## Why profiles matter

A good handoff depends on the agent.

Some agents navigate repositories well. Some are better at isolated edits. Some can run shell commands. Some should only produce plans or Prompts. LEAP should not assume they behave the same way.

## Agent Execution Profile template

```text
# Agent Execution Profile — <Agent / Tool>

## 1. Basic Profile
- Agent / Tool:
- Model:
- Reasoning level:
- Context size:
- Repository browsing ability:
- Shell access:
- Autonomous edit behavior:
- Preferred handoff style:

## 2. Strengths
- <What this agent is good at>

## 3. Known Failure Modes
- <What this agent commonly gets wrong>

## 4. Required Constraints
- <Rules every handoff should include>

## 5. Required Stop Conditions
- <When this agent must stop>

## 6. Validation Commands
- <Tests, lint, typecheck, build, manual checks>

## 7. Commit Behavior
- <Should it commit? One Build Unit per commit? Message convention?>
```

## Strategic and delivery traceability

For strategically material work, the handoff should identify:

```text
Mission / Project Charter
Strategic Outcome
Initiative
Delivery Unit, if used
Build Unit / bounded task
Roadmap placement, if relevant
Affected Domains
Affected Architecture Areas
```

Roadmap schedules and prioritizes. Domains are persistent responsibility boundaries. Architecture is technical structure.

Delivery Unit may be collapsed for small work. Build Unit is not necessarily independently deployable.

## Common adjustment rules

| Agent behavior | LEAP adjustment |
|---|---|
| Weak repo awareness | Strong source list, file list, and inspect-first instructions |
| Strong autonomous editing | Tight non-goals and forbidden-file list |
| Long context | More source material allowed, but preserve source hierarchy |
| Shell access | Explicit validation commands and permission limits |
| Chat-only | Generate plan or Prompt only |
| Fast but shallow | Smaller Build Units and explicit acceptance criteria |
| Strong refactoring tendency | Block broad cleanup unless scoped and testable |
| Weak test discipline | Require exact verification and evidence |
| Multi-repository access | Explicit ownership, contract, merge-order, and rollback boundaries |

## Failure modes to guard against

```text
- hallucinating files, APIs, or business rules
- obeying stale docs over repo reality
- broad refactors disguised as cleanup
- silent schema or contract changes
- adding dependencies without approval
- weakening tests
- overfitting to Prompt wording instead of repo reality
- violating non-goals
- making product or Architecture decisions during implementation
- confusing Initiative with Domain
- treating Roadmap placement as permanent Initiative identity
- treating Build Units as independently deployable without evidence
- globally replacing legacy Layer terminology
```

## Agent-ready handoff rule

An implementation Prompt is not ready unless it includes:

```text
- Agent / Tool
- Codex Plan Mode, when Codex-targeted
- Model
- Reasoning Level
- Execution Mode
- Scope Scale
- Repository
- Branch / Worktree
- Permissions
- Validation
- Commit Guidance
```

Scope Scale values may include:

```text
small task
Build Unit
Delivery Unit
Initiative
multi-repository Initiative
repo-wide maintenance
```

Codex Plan Mode is a user-controlled setting. LEAP Execution Mode is an instruction inside the Prompt.

Every Prompt must also state its Prompt type.

Use LHS only when implementation gravity warrants staged execution. LEAP LHS stages implementation; it does not define the strategic hierarchy.

## Codex profile example

```text
# Agent Execution Profile — Codex

## 1. Basic Profile
- Agent / Tool: Codex
- Codex Plan Mode: Off for bounded Build Units; On when plan approval is required
- Model: project-approved current Codex model
- Reasoning level: Medium / High / Extended based on scope
- Repository browsing ability: available when connected
- Shell access: environment-dependent
- Autonomous edit behavior: can modify permitted files
- Preferred handoff style: explicit task packet with traceability,
  scope, non-goals, stop conditions, validation, and commit guidance

## 2. Strengths
- bounded implementation
- test-driven edits when verification is explicit
- multi-file Build Units when source truth is clear
- staged Delivery Unit and Initiative execution

## 3. Known Failure Modes
- over-completing broad Prompts
- following stale plans when source hierarchy is unclear
- touching adjacent files when boundaries are vague
- treating missing decisions as implementation choices

## 4. Required Constraints
- include source-of-truth instructions
- include Strategic Outcome and Initiative when material
- include files and areas not to touch
- include validation commands
- include stop conditions for conflicts, missing files, and unapproved Architecture changes

## 5. Commit Behavior
- prefer one Build Unit per commit where feasible
- use Initiative / Delivery Unit / Build Unit or task identifiers when the project has them
```
