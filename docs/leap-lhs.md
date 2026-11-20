# LEAP LHS — Layered House Standard

LEAP LHS is the LEAP Prompt format for staged implementation. It is a variant of the [LEAP Prompt](../prompts/leap-prompt-standard.md), not a lifecycle stage, and it does not define the project's strategic hierarchy.

## When to use it

Use LHS only when staging reduces real risk. Typical triggers, usually two or more together:

- several Build Units with a dependency order
- coordinated changes across code, tests, docs, and contracts
- compatibility, migration, or rollback risk
- work that should land as several reviewable commits
- a handoff between execution surfaces mid-way

Do not use LHS for a single coherent change. A standard LEAP Prompt or a [Quick LEAP Brief](user/quick-leap-brief.md) is enough.

## Format

An LHS Prompt is a standard LEAP Prompt whose **Implementation Sequence** is replaced by an ordered list of stages. Every other Prompt section still applies once, at the top. Do not repeat them per stage.

Each stage has exactly these fields:

```text
### Stage <n> — <name>

Goal:            one sentence: what is true after this stage
Build Units:     the bounded units delivered in this stage
Paths:           files or areas this stage may change
Depends on:      earlier stages, or "none"
Checkpoint:      checks that must pass before the next stage starts
Commit:          commit boundary and message intent
Rollback point:  how to revert this stage without undoing earlier ones
```

Rules:

- Stages run in order. A failed checkpoint stops the sequence; report it, don't push on.
- A stage may not widen the Prompt's scope, non-goals, or permissions.
- Prefer two to five stages. More usually means the work should be split into separate Prompts.
- Report a verification state per stage, then an overall state, using [LEAP Validation](../prompts/leap-validation-standard.md).

## Minimal example

```text
### Stage 1 — Add the new field behind a default
Goal:            API accepts and stores `priority`, defaulting to "normal"
Build Units:     BU-1 schema + model
Paths:           src/models/, migrations/ (new file only)
Depends on:      none
Checkpoint:      unit tests pass; migration applies and rolls back locally
Commit:          "Add priority field with default"
Rollback point:  revert commit; down-migration drops the column

### Stage 2 — Expose the field in the UI
Goal:            users can set priority on create and edit
Build Units:     BU-2 form + list badge
Paths:           src/ui/tasks/
Depends on:      Stage 1
Checkpoint:      component tests pass; manual create/edit check
Commit:          "Expose task priority in UI"
Rollback point:  revert commit; API remains backward compatible
```
