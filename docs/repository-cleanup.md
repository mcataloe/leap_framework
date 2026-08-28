<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: governance-rule
  authority: supporting-framework-rule
  applies_to: downstream-projects
END_LEAP_DOC_METADATA
-->

# LEAP Repository Cleanup

LEAP Repository Cleanup is the governed workflow for identifying and decommissioning stale, duplicate, conflicting, misleading, superseded, or otherwise obsolete repository artifacts.

Invoke it with:

```text
Run LEAP Cleanup on <repository or bounded scope>.
```

Same-thread source truth and scope should be inherited. Add a scope or cleanup mode only when the existing context does not determine them.

## Place in the LEAP lifecycle

Repository Cleanup is a specialized Governance workflow, not a new lifecycle phase, Agent Execution Mode, authorization substitute, or general permission to delete files.

```text
Run LEAP Cleanup
        ↓
Inventory and proposed decommission set
        ↓
Human approval
        ↓
LEAP Refactor Prompt
        ↓
Implementation
        ↓
Validation/Handoff
```

An unqualified `Run LEAP Cleanup` command is discovery-only. It must not modify, move, archive, or delete files before the proposed decommission set is explicitly approved.

## Cleanup modes

Cleanup modes describe compatibility and retention posture. They are not lifecycle phases or Agent Execution Modes. `archive-only` is cleanup-specific; `controlled-migration` and `destructive-cutover` apply their corresponding compatibility and supersession postures to cleanup work.

| Mode | Use when | Required posture |
|---|---|---|
| `archive-only` | Retention, audit, public-path, or traceability needs require the original artifact to remain available | Remove the artifact from active source-truth routing; retain it only in an explicitly historical location or as an approved compatibility stub; do not delete it |
| `controlled-migration` | Live consumers, contracts, environments, or operational dependencies require temporary coexistence | Migrate consumers in a stated sequence, define a sunset condition, and keep old and new authority unambiguous during coexistence |
| `destructive-cutover` | The replacement should become the only supported current state and coexistence would create false authority or maintenance cost | Prove the replacement is effective, remove obsolete active-tree artifacts and references, use Git history as the archive by default, and require explicit approval before deletion |

When the mode is not supplied, the Cleanup pass recommends one but remains discovery-only. Confirmed coexistence requirements route to `controlled-migration`; unresolved material obligations block destructive cutover.

For `archive-only`, an in-tree archive is allowed only when an explicit retention or traceability need justifies it. It must be clearly labeled historical and excluded from current source-truth routing. When repository retention is unnecessary, Git history is preferred over a permanent archive directory.

## Required inventory and classification

A repository-wide run inventories documentation, plans, prompts, templates, manifests, compatibility files, and any code, configuration, test, or runtime artifact proposed for removal. A bounded run inventories the requested scope plus the references and consumers needed to judge it safely.

Each candidate must record:

- path or artifact identifier
- artifact type and current authority
- classification and evidence
- inbound references, imports, routing, and runtime consumers
- external or cross-repository consumers when discoverable
- canonical replacement and replacement evidence
- public-path or compatibility obligations
- proposed action and cleanup mode
- risk, unknowns, and required approval

Use the existing documentation classifications:

- Canonical
- Supporting
- Current but poorly organized
- Partially useful
- Stale
- Conflicting
- Duplicate
- Misleading
- Completed implementation plan
- Archived
- Unknown

Classification alone never authorizes removal.

## Replacement and dependency evidence

A candidate is ready for decommissioning only when the pass establishes both:

1. **Absence evidence** — the retired artifact will no longer be active, routed, referenced, imported, executed, or presented as current.
2. **Replacement evidence** — the canonical replacement exists, is discoverable, owns the required truth or behavior, and works for the relevant consumers.

For `archive-only`, absence means absence from active authority and routing, not filesystem absence.

Evidence should inspect, when relevant:

- source-of-truth manifests and documentation entry points
- Markdown links, paths, imports, exports, and package references
- configuration, CI/CD, infrastructure, scripts, tests, and generated artifacts
- runtime routes, APIs, schemas, data, integrations, and active environments
- other repositories and external consumers that can be verified
- retired names, terminology, identifiers, and compatibility surfaces

Text search is useful but cannot by itself prove effective decommissioning. Validation must be structural, semantic, and behavioral when those surfaces exist.

## Approval contract

Before any mutation, the Cleanup pass must present the exact proposed decommission set. Approval must cover the candidate paths, proposed actions, cleanup mode, replacement, reference repairs, public-contract handling, and validation plan.

Additional destructive-cutover requirements:

- no broad or unresolved deletion targets
- replacement authority established before purge
- zero-live-dependency review across discoverable internal and external surfaces
- explicit handling or handoff for consumers that cannot be modified in scope
- a human checkpoint immediately before destructive deletion
- no in-tree backup of the retired design unless separately required and approved

If new material dependencies or public contracts appear after approval, stop and return the affected candidates for a new decision.

## Refactor Prompt contract

After approval, generate a LEAP Refactor Prompt that includes:

- the approved decommission set and exact allowed mutations
- ordered canonicalization, migration, reference-repair, and removal steps
- explicit non-goals and forbidden areas
- source-of-truth manifest and entry-point updates
- compatibility and public-path handling
- forbidden-pattern checks for retired terminology and identifiers
- targeted validation followed by the practical full validation suite
- stop conditions and the destructive human checkpoint when required
- Validation/Handoff evidence requirements

The Refactor Prompt may use Delivery Units and Build Units when sequencing, consumer migration, or destructive risk warrants staged execution. Cleanup itself does not create a new planning hierarchy.

## Validation and effective status

Validation/Handoff must report:

- branch or revision validated
- artifacts moved, retained, rewritten, or deleted
- references and consumers checked
- source-of-truth and documentation-front-door updates
- structural, semantic, and behavioral checks run
- forbidden-pattern results
- exceptions, unavailable checks, and unresolved external surfaces
- public-path and compatibility status
- final status for each candidate

Valid final statuses are:

- `Effective` — both absence and replacement evidence pass
- `Partially effective` — approved work completed but a stated non-blocking exception remains
- `Blocked` — a material dependency, replacement gap, or approval requirement remains
- `Not decommissioned` — the candidate was retained or removed from the approved set

Moving a file, adding a warning, or passing a text search does not by itself justify `Effective`.

## Cleanup gate decisions

```text
No Action Needed
Needs Human Classification
Blocked - Replacement Missing
Blocked - Live Dependencies
Ready for Decommission Approval
Route to Controlled Migration
Generate LEAP Refactor Prompt
Run Full LEAP Recon
```
