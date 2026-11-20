<!--
LEAP_DOC_METADATA:
  audience: user, maintainer, agent
  doc_type: canonical-charter-reference
  authority: canonical
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# LEAP Charter

LEAP Charter is the project-alignment front door for LEAP. It establishes or reconciles project direction, source truth, documentation, Roadmap posture, and implementation readiness before focused Recon or implementation Prompt generation.

Charter is the first step of the [LEAP lifecycle](leap.md#2-lifecycle). Not every task starts with Charter. A focused Recon may proceed when its Baseline Freshness Check finds the existing baseline fresh enough.

## Charter outcomes

Charter should establish or reconcile, at the level warranted by project size:

- Mission or project-specific Project Charter
- target users and MVP or current scope boundary
- Strategic Outcomes
- Initiative registry
- Roadmap
- Domain map when useful
- Architecture direction
- Delivery Units when implementation planning requires them
- source-of-truth manifest
- documentation baseline
- prompt backlog
- human checkpoints and next LEAP work

For traceability, use the [project documentation model](project-documentation-model.md) when the project already uses it.

## Materiality Gate

Charter uses the shared [Materiality Gate](materiality-gate.md): inspect what is discoverable, ask only unresolved material questions needed for the next safe Charter decision, and stop on hard blockers. The Materiality Check must record hard blockers explicitly rather than implying that a blocked Charter can proceed. **No Gate** never bypasses unsafe source truth, authorization, destructive-change safeguards, sensitive-area checkpoints, public-contract approval, or required human approval.

## Charter modes

### Greenfield Mode

Use for brand-new projects, early ideas, or solutions without a stable repository, source-truth baseline, Roadmap, Architecture, or documentation model.

Greenfield Charter should create only enough structure to proceed safely. It should not force one file per concept.

It may create or organize:

- Mission and Project Charter
- target users
- MVP boundary
- Strategic Outcomes
- Initiative registry
- initial Roadmap
- Domain map when useful
- initial Architecture direction
- initial data-model assumptions
- Delivery Units when implementation planning is ready
- prompt backlog
- `AGENTS.md` guidance when applicable
- first recommended Recon or Prompt sequence

Greenfield Charter should not generate Build Units before Initiative boundaries and intended outcomes are clear.

Small projects may combine these concepts into one or a few documents.

### Brownfield Mode

Use for existing or mid-buildout projects where LEAP must inspect repo reality, reconcile documentation, identify gaps, establish source truth, and prepare future Recon and Prompt work.

Brownfield Charter should:

1. identify existing documents and source-truth entry points
2. classify documents
3. inspect the current solution and relevant repo reality
4. compare strategy, Strategic Outcomes, Initiatives, Roadmap, Domains, Architecture, Delivery plans, and implementation
5. detect stale, conflicting, duplicate, and misleading material
6. reconcile legacy Layer documents semantically
7. fix safe documentation and planning gaps
8. create or update supplemental Markdown docs
9. produce a gap register
10. produce a migration map
11. prepare focused Recon and Prompt work

Brownfield Charter may update documentation and planning artifacts directly. Runtime changes should normally become follow-up LEAP Prompts unless explicitly requested.

## Documentation reconciliation policy

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Do not simply rename or delete legacy docs.

Preferred approach:

1. confirm canonical ownership
2. absorb useful current content
3. preserve original paths when compatibility requires them
4. add deprecation or compatibility headers when helpful
5. archive only after replacement source truth exists
6. create a migration map
7. update entry points, `AGENTS.md`, and prompt backlogs
8. validate links and source-truth references

Brownfield Charter reconciles documentation posture but does not by itself authorize deletion. Route exact decommission candidates to [LEAP Repository Cleanup](repository-cleanup.md) for dependency analysis, cleanup-mode selection, approval, and Refactor Prompt generation.

## Legacy document classification

| Classification | Meaning | Recommended action |
|---|---|---|
| Canonical | Current source of truth | Keep or move into canonical structure |
| Supporting | Useful secondary detail | Keep near or reference from canonical docs |
| Current but poorly organized | Useful but structurally messy | Absorb into canonical docs; preserve original until safe |
| Partially useful | Mix of current and stale information | Extract useful content; archive or deprecate original |
| Stale | No longer reflects current direction | Archive with warning |
| Conflicting | Contradicts current strategy or repo reality | Record and resolve in canonical docs |
| Duplicate | Repeats truth owned elsewhere | Consolidate and archive duplicate |
| Completed implementation plan | Historical plan already completed | Archive or convert remaining items to backlog |
| Misleading | Likely to confuse future work | Archive or mark explicitly |
| Archived | Historical only | Do not treat as source truth |
| Unknown | Not yet classified | Inspect before relying on it |

## Legacy Layer reconciliation

Brownfield Charter classifies each legacy generic `Layer` by meaning before migrating it, using the [project-documentation migration guide](maintainer/project-documentation-migration.md). Do not rename public paths solely for terminology consistency. Recommend migration when Layer ambiguity creates sequencing, ownership, Domain, Architecture, source-truth, or implementation-scope risk.

## Recommended documentation pattern

This is an example, not a mandatory structure:

```text
docs/
  00_start_here.md

  01_charter/
    00_project_charter.md
    01_source_of_truth.md
    02_document_inventory.md
    03_gap_register.md
    04_reconciliation_notes.md

  02_strategy/
    00_product_strategy.md
    01_strategic_outcomes.md
    02_initiative_registry.md
    03_roadmap.md

  03_domains/
    00_domain_map.md

  04_architecture/
    00_architecture_overview.md
    01_system_context.md
    02_data_model.md
    03_api_surface.md

  05_delivery/
    INIT-001/
      00_initiative.md
      DU-001.md

  06_build_units/
    INIT-001/
      BU-001.md

  07_decisions/
  08_prompts/
  99_archive/
```

Existing conventions may be retained. Semantic clarity matters more than folder conformity.

## Strategic Outcomes and Initiatives

Charter should keep Strategic Outcomes, Initiatives, Roadmap, Domains, Architecture, Delivery Units, and Build Units distinct, as defined in the [project documentation model](project-documentation-model.md). A Roadmap references Initiatives but does not own their identity.

## Initiative and Roadmap outputs

For larger projects, Charter should produce or recommend an Initiative registry containing:

```text
Initiative ID:
Title:
Status:
Strategic Outcomes advanced:
Purpose:
Success criteria:
Non-goals:
Affected Domains:
Affected repositories:
Dependencies:
Risks:
Delivery Units:
Roadmap placement:
Owner / approver:
Last reconciled:
```

The Roadmap should show current scheduling without becoming a competing source for Initiative identity.

When staffing or delivery timing changes the next safe planning decision, use [Team & Delivery Capacity Estimation](team-delivery-estimation.md). The project's work tracker (for example Jira) stays the source of record; Charter proposes estimates and does not keep its own roster or write estimates back without authorization.

## Delivery and Build planning

Charter may identify candidate Delivery Units but should normally leave detailed Build Unit generation to focused Recon.

Use a Delivery Unit only when it adds a meaningful release or coordination boundary.

## Doc metadata convention

Important docs should include concise metadata:

```markdown
Status: Canonical / Supporting / Draft / Archived
Last reconciled: YYYY-MM-DD
LEAP mode: Greenfield Charter / Brownfield Charter / Recon / Governance
Source of truth: Yes / No / Partial
Purpose: <one concise statement>
```

Generated docs are Draft until ratified.

## Archive README

`docs/99_archive/README.md` should state that archived documents are preserved for traceability but are not source truth unless a current canonical document explicitly references them.

## Migration map

Brownfield Charter should produce a migration map:

| Legacy document | Semantic classification | New canonical owner | Path action | Status | Notes |
|---|---|---|---|---|---|

Path action may be Keep, Update in place, Add compatibility header, Move with approved redirect plan, or Archive after replacement.

## LLM-friendly documentation

LEAP docs should:

- provide a clear `00_start_here.md`
- label canonical, supporting, Draft, and archived material
- use stable identifiers for Strategic Outcomes, Initiatives, Delivery Units, and Build Units when complexity warrants them
- avoid duplicate competing Roadmaps and Initiative registries
- separate persistent Domains from temporary Initiatives
- update agent guidance to point to canonical docs first
- preserve old paths when link compatibility matters

## AGENTS.md and prompt backlogs

When Charter changes the documentation baseline, update repository guidance so coding agents:

1. start with `docs/00_start_here.md`
2. use canonical docs first
3. inspect Strategic Outcomes, Initiative registry, Roadmap, Domains, Architecture, Delivery Units, and Build Units as relevant
4. treat archived docs as historical
5. classify legacy Layers before migration
6. create focused Recon or Prompt recommendations instead of making risky runtime changes during Charter

The prompt backlog should capture unresolved strategy, documentation, Architecture, reconciliation, Delivery, and implementation work.

## Optional baseline register

Repository `AGENTS.md` may contain a small LEAP Baseline State summary.

For larger or drift-prone projects, Brownfield Charter, Governance, or an explicitly authorized baseline scan may create `leap.baseline.yaml`.

Creation may be justified when:

- several canonical docs exist
- stale or conflicting docs create risk
- Initiative, Roadmap, Domain, Architecture, Delivery, or Build records are distributed
- several agents or humans work in the repository
- recurring Recon and Prompt work occurs
- a migration map, gap register, or dependency register exists

Normal Recon may recommend the file but must not silently create it.

## Charter output

Use the output format in the [Charter standard](../prompts/leap-charter-standard.md). Omit sections with nothing material. Do not pad with N/A.

## Gate behavior

Charter should end with a clear next step, such as:

- Continue Discovery
- Draft Concept Brief
- Pressure Test Further
- Needs Human Decision
- Reconcile Docs First
- Proceed to Recon
- Generate a documentation-focused LEAP Prompt
- Do Not Build Yet

Do not generate runtime implementation changes unless explicitly requested. Risky code, schema, API, UI, auth, workflow, infrastructure, or Architecture changes discovered during Charter should become follow-up LEAP work.
