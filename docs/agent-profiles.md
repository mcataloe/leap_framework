# Agent Profiles

LEAP is tool-agnostic.

Codex is one possible implementation agent, but the framework should work with any AI coding agent or assisted-development environment that can receive a bounded handoff.

Different agents have different strengths, weaknesses, context limits, autonomy levels, and failure modes. LEAP captures those differences in an **Agent Execution Profile**.

---

## Why agent profiles matter

A good handoff depends on the agent.

Some agents are strong at repo navigation. Some are better at isolated edits. Some are fast but shallow. Some can run shell commands. Some can make broad autonomous changes. Some are chat-only and should only produce plans or prompts.

LEAP should not pretend every agent behaves the same way.

---

## Agent Execution Profile template

```text
# Agent Execution Profile — <Agent / Tool Name>

## 1. Basic Profile
- Agent / Tool:
- Model:
- Reasoning level:
- Context size:
- Repo browsing ability:
- Shell access:
- Autonomous edit behavior:
- Preferred handoff style:

## 2. Strengths
- <What this agent is good at>

## 3. Known Failure Modes
- <What this agent commonly gets wrong>

## 4. Required Constraints
- <Rules the handoff should always include for this agent>

## 5. Required Stop Conditions
- <When this agent should stop and ask>

## 6. Validation Commands
- <Tests/lint/typecheck/build/manual checks>

## 7. Commit Behavior
- <Should it commit? One Build Unit per commit? Message convention?>
```

---

## Common agent adjustment rules

| Agent Behavior | LEAP Adjustment |
|---|---|
| Weak repo awareness | Stronger source list, file list, and inspect-first instructions |
| Strong autonomous editing | Tighter non-goals and forbidden-file list |
| Long context | More source material allowed, but still require source hierarchy |
| Shell access | Explicit validation commands and permission limits |
| Chat-only | Generate plan/prompt only; do not assume implementation |
| Fast but shallow | Smaller Build Units and more explicit acceptance criteria |
| Strong refactoring tendency | Explicitly block broad cleanup unless scoped and testable |
| Weak test discipline | Require exact verification commands and expected evidence |

---

## Common failure modes to guard against

```text
- hallucinating files, APIs, or business rules
- obeying stale docs over current code
- broad refactors disguised as cleanup
- silent schema or contract changes
- adding dependencies without approval
- passing tests by weakening them
- overfitting to prompt wording instead of repo reality
- completing the task while violating non-goals
- making product decisions inside implementation
- changing auth, billing, privacy, AI behavior, or data contracts without approval
```

---

## Agent-ready handoff rule

A LEAP Prompt is not ready for an implementation agent unless it includes:

```text
- Agent / Tool
- Codex Plan Mode, for Codex-targeted prompts
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

Codex Plan Mode is a user-controlled Codex UI setting. LEAP Execution Mode is an instruction inside the prompt.

If a field is unknown, LEAP should recommend a safe default and label it as a recommendation rather than leaving the field blank.

Every generated implementation prompt should also state its prompt type:

```text
Standard LEAP Prompt / LHS Prompt / Fix Prompt / Refactor Prompt / Validation Prompt / other clearly named type
```

Use LEAP LHS only when implementation gravity warrants staged execution. LHS is a LEAP Prompt format, not a required lifecycle stage after every prompt.

---

## Codex profile example

```text
# Agent Execution Profile — Codex

## 1. Basic Profile
- Agent / Tool: Codex
- Codex Plan Mode: Off for bounded implementation prompts, On when the user should approve the plan before edits, User decision required when approval posture is the deciding factor
- Model: project-approved Codex model
- Reasoning level: medium / high / extended based on scope
- Repo browsing ability: available when connected to repo/worktree
- Shell access: depends on environment
- Autonomous edit behavior: can modify files when permitted
- Preferred handoff style: explicit task packet with scope, non-goals, stop conditions, validation, and commit instructions

## 2. Strengths
- Bounded implementation
- Test-driven edits when verification is explicit
- Multi-file Build Units when source truth is clear
- Following structured implementation sequences

## 3. Known Failure Modes
- Can over-complete broad prompts
- Can follow stale planning docs if source hierarchy is unclear
- Can touch adjacent files if boundaries are vague
- Can treat missing decisions as implementation choices

## 4. Required Constraints
- Include source-of-truth instructions
- Include files/areas not to touch
- Include explicit validation commands
- Include stop conditions for conflicts, missing files, and unapproved architecture changes

## 5. Commit Behavior
- Prefer one Build Unit per commit where feasible
- Commit message should include layer/sublayer/task prefix when project convention exists
```
