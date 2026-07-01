<!--
LEAP_DOC_METADATA:
  audience: maintainer, agent
  doc_type: migration-guidance
  authority: supporting
  applies_to: leap-framework-and-downstream-projects
END_LEAP_DOC_METADATA
-->

# Project Documentation Migration Guidance

## Purpose

This guide explains how to reconcile legacy LEAP project documents that use generic numbered `Layer` terminology.

The preferred current model is defined in [`../project-documentation-model.md`](../project-documentation-model.md):

```text
Mission / Project Charter
        ↓
Strategic Outcome
        ↓
Initiative
        ↓
Delivery Unit
        ↓
Build Unit
```

Roadmaps schedule work. Domains organize persistent responsibility. Architecture organizes technical structure.

Migration is semantic reconciliation, not a global rename.

## Migration policy

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Classify meaning before renaming.
Never let stale docs compete with current source truth.
```

## Legacy Layer classification

| Legacy Layer actually represents | Preferred classification |
|---|---|
| Outcome-oriented coordinated effort | Initiative |
| End-to-end releasable or adoptable capability | Delivery Unit |
| Bounded implementation responsibility | Build Unit |
| Persistent business or responsibility boundary | Domain |
| Technical structural tier | Architecture Layer |
| Required chronological stage | Phase |
| Mixed or unclear collection | Needs reconciliation |

## Classification questions

For each legacy Layer, ask:

1. What outcome does this work advance?
2. Does it end when a strategic objective is achieved?
3. Does it represent a persistent responsibility boundary?
4. Can it be released, enabled, adopted, or demonstrated independently?
5. Is it primarily a bounded implementation packet?
6. Is its ordering truly required, or does numbering only reflect an old plan?
7. Does it describe a technical tier rather than strategic work?
8. Does it combine several of these meanings?

## Migration decisions

### Migrate to Initiative when

- the document coordinates multiple capabilities or Build Units
- it advances one or more Strategic Outcomes
- it has success criteria and non-goals
- it may run in parallel with other work
- it ends when the intended outcome is completed, abandoned, or superseded

### Migrate to Delivery Unit when

- the document defines an end-to-end releasable or adoptable increment
- several Build Units are required to complete it
- acceptance is based on functional readiness rather than one implementation commit

### Migrate to Build Unit when

- the scope is bounded enough to implement, test, review, and usually commit independently
- it does not require the implementation agent to invent product or architecture decisions
- it has explicit validation and stop conditions

### Migrate to Domain when

- the concept persists across roadmap cycles
- it represents business responsibility, ownership, or a stable technical area
- several Initiatives may touch it over time

### Keep as Architecture Layer when

- the term describes a qualified technical tier such as Presentation Layer or Persistence Layer
- the meaning is structural rather than strategic or temporal

### Migrate to Phase when

- completion order is genuinely chronological and later work cannot safely begin first
- the phase is a temporary stage, not a persistent capability or Domain

### Mark Needs Reconciliation when

- the document combines strategy, releases, architecture, and implementation tasks
- its numbering implies sequence that current reality no longer follows
- ownership or source truth is unclear
- the document conflicts with repo reality

## Brownfield migration procedure

1. Inventory all active Layer documents and references.
2. Classify each document using the table above.
3. Compare its claims with repo reality, current Roadmaps, architecture docs, tests, and active decisions.
4. Identify the canonical destination for each type of truth.
5. Create or update Strategic Outcomes, Initiative records, Delivery Units, Build Units, Domain docs, or Architecture docs as needed.
6. Preserve IDs, old names, and links in a migration map.
7. Update active prompts and source-of-truth manifests.
8. Keep legacy files in place when renaming would break public paths or active references.
9. Add a compatibility or deprecation note where helpful.
10. Archive only after replacement source truth exists and links are validated.

## Migration map example

| Legacy path | Legacy meaning | New canonical owner | Path action | Status |
|---|---|---|---|---|
| `docs/04_layers/layer-2-intake.md` | Outcome-oriented coordinated work | `INIT-002 Intake Automation` | Keep path; add compatibility header and canonical link | Migrated |
| `docs/04_layers/layer-2a-parser.md` | Bounded implementation | `BU-002A Parser Stabilization` | Keep or move only with approved link plan | Planned |
| `docs/04_layers/layer-0-foundation.md` | Mixed product baseline and setup phase | Project Charter plus Phase record | Reconcile before rename | Needs reconciliation |

## Compatibility rules

Do not change these uses merely because they contain `Layer`:

- Layered Execution & Alignment Protocol
- Layered House Standard
- LEAP LHS
- qualified Architecture Layers
- historical release notes
- compatibility explanations

Do not force downstream migration when the existing Layer model is clear, stable, and creates no material risk.

Recommend migration when ambiguity creates:

- sequencing risk
- ownership confusion
- Domain confusion
- architecture confusion
- source-of-truth conflict
- implementation-scope ambiguity
- parallel-agent collision risk

## Public paths

Do not rename public paths solely to match new terminology.

Preferred first-pass behavior:

- retain the path
- update the title and semantic classification when safe
- add a canonical-reference notice
- update inbound links only when necessary
- defer physical moves to an explicitly approved documentation migration

## Source-of-truth handling

A legacy Layer document remains source truth until one of these occurs:

- a human ratifies a replacement canonical document
- Brownfield Charter records the migration
- repo reality proves the document stale or conflicting
- the document is explicitly archived or deprecated

Generated replacement documents are Draft until ratified.

## Small-project rule

Do not require a small project to split one clear document into several files.

A single document may contain:

- Mission or Project Charter
- Strategic Outcome
- one Initiative
- a collapsed Delivery Unit
- one Build Unit

The migration succeeds when meaning and traceability are clear, not when folder depth increases.

## Validation checklist

- [ ] Every legacy Layer use has been classified.
- [ ] Framework-name and LHS uses were preserved.
- [ ] Qualified Architecture Layers were preserved.
- [ ] Roadmap timing was not confused with Initiative identity.
- [ ] Domains were kept persistent and separate from temporary Initiatives.
- [ ] Delivery Units represent releasable or adoptable increments.
- [ ] Build Units remain bounded implementation responsibilities.
- [ ] Existing public paths were preserved or have an approved migration plan.
- [ ] Canonical ownership is unambiguous.
- [ ] Links were validated.
- [ ] Archive actions occurred only after replacement source truth existed.
