# LEAP Semantic Workflow Routing

Status: Canonical workflow-selection contract (proposed for release)
Source: LEAP Framework. Distribution: LEAP Agent Pack.

## Purpose and boundary

Semantic routing chooses WHICH LEAP workflow applies to a user request. Existing LEAP Execution Routing separately chooses WHERE and HOW approved work runs. Neither grants permission to mutate a repository.

The lifecycle remains: LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff. Discovery and Pressure Test are optional entry points, not lifecycle phases.

## Priority and behavior

1. Explicit user-selected LEAP commands take precedence over inferred intent, except where higher-priority instructions, safety, source truth, permissions, or mandatory approval prevent execution.
2. Resolve references such as "this", "that design", and "continue" from the current thread. Preserve the latest approved scope and existing gate state.
3. Select the smallest useful workflow, rather than running LEAP for every ordinary task.
4. Never interpret exploration, investigation, or a request to generate a prompt as permission to implement. Charter, Discovery, Pressure Test and Recon are normally non-mutating unless a separately explicit, authorized instruction provides bounded exceptions.
5. If the necessary baseline is missing, route from Recon toward Charter. If implementation readiness is missing, route from Prompt or Execution back to Recon or a bounded decision.
6. Apply the Materiality Gate: INSPECT -> CLASSIFY -> ASK / ASSUME / STOP -> RE-EVALUATE. No Gate never overrides STOP.
7. Report the selected route briefly when material to user expectations; do not add a status badge to every simple answer.

## Canonical command and help catalog

A user may type "LEAP help", "what can LEAP do?", or "which LEAP command?" to see the following compact menu. The first column is the stable explicit invocation; an agent may also recognize comparable natural language. Help does not modify files.

| Explicit invocation | Use when | Example intent |
|---|---|---|
| LEAP help | Discover commands and examples | "What LEAP workflows are available?" |
| Run LEAP Discovery | Explore a domain, problem, actors, relationships, workflows or possibilities | "Help me understand how incident ownership works" |
| Run LEAP Pressure Test | Challenge a proposal/hypothesis and compare alternatives | "Would this data model lose vendor-specific meaning?" |
| Run LEAP Charter | Establish or reconcile mission, scope, strategy, or source truth | "Set up this new product" |
| Run LEAP Recon | Inspect repo reality, dependencies, drift and delivery readiness | "Investigate our existing ingestion architecture" |
| Run LEAP Recon Lite | A narrowly scoped, lower-gravity Recon | "Focused review of this design change" |
| Generate LEAP Prompt | Create a bounded implementation contract after readiness | "Write the agent implementation instructions" |
| Run LEAP Prompt | Execute an approved bounded implementation prompt | "Implement the approved Build Unit" |
| Generate LEAP LHS | Plan staged multi-Build-Unit execution | "Create staged instructions across services" |
| Run LEAP LHS | Execute an approved staged prompt | "Run the approved staged plan" |
| Run LEAP Governance | Reconcile documentation, framework or adoption drift | "Find conflicting source-of-truth docs" |
| Run LEAP Cleanup | Inventory obsolete artifacts and propose a decommission set; require approval before mutation | "Remove obsolete Lambda references" |
| Run LEAP Validation | Verify against acceptance criteria, tests and docs | "Check the result against the brief" |
| Run LEAP Handoff | Summarize changes, evidence, risks and next steps | "Provide implementation handoff" |

Also supported: Quick LEAP Brief for a small coding-agent task; Fix, Refactor, Validation and LHS Prompt variants; Brownfield Charter; and the "No Gate" modifier (safe assumptions only). These are not separate required lifecycle phases. If a task is trivial, answer or fix it normally.

**Aliases:** "LEAP Recon Lite", "Generate LEAP Prompt", "LEAP help", "LEAP Discovery", and "LEAP Pressure Test" can be used without the "Run" prefix. Keep earlier explicit command forms valid.

## Discovery, Pressure Test and Recon are different

| Intent | Primary question | Expected output | Default route |
|---|---|---|---|
| Discovery | What is this domain/task, and what possibilities and constraints exist? | Domain / Concept Brief, open decisions | Continue Discovery, Pressure Test or Charter |
| Pressure Test | Does this proposed approach survive challenges? | Assumptions, counterexamples, tradeoffs, falsifiers, recommendation | Revise proposal, Recon or stop |
| Recon | What is true in the actual solution and is it implementation-ready? | Evidence-based findings, dependencies, scope, Build Units, gate | LEAP Prompt when ready |

Discovery may ask iterative domain questions that are not immediate implementation blockers. It should avoid unnecessary batches, use existing evidence, preserve the user's language, and distinguish known, assumed, contested and unknown information. It is valid to finish Discovery with no proposed build. End with a concise Domain/Concept Brief: goal, actors, terminology, workflows, entities and relationships, constraints, options, unknowns, and next recommended step. Do not force architecture or file creation.

Pressure Test starts with a candidate hypothesis/decision and examines what would make it fail or reverse: evidence, risks, assumptions, alternatives, operational costs and reversibility. For conceptual questions use the Charter Ideation Loop; for challenges that require repository evidence use Recon. It can be invoked explicitly or within ongoing Discovery. Return conclusion and the strongest consideration that would reverse it.

Recon remains source-grounded with Baseline Freshness Check, current repository and branch reality, cross-Domain implications, and Materiality Gate. A proposed architecture backed by a repository generally routes to Recon, even if phrased as "would this work?"

## Routing edge cases

- "Tell me about [domain]" without LEAP context -> ordinary explanation; don't force LEAP.
- "Let's discover [domain] for this project" -> Discovery.
- "Should we migrate this deployed EKS solution?" -> Recon if inspecting the project is material; Pressure Test for a theoretical comparison.
- "Implement what we discussed" with no approved bounded prompt -> check readiness, do not infer authorization for unrelated decisions.
- "Can we safely delete old artifacts?" -> Cleanup discovery first.
- "No Gate; delete production data" -> STOP on destructive authorization; no bypass.
- Ambiguous choice with meaningful safety/scope difference -> inspect available evidence, then ask one targeted question; otherwise take a disclosed safe route.
- Existing explicit Charter, Recon, Prompt, LHS, Governance, Cleanup, Validation/Handoff invocations remain fully valid.

## Skill integration

Native Skills are optional entry points. A canonical ready-to-use LEAP routing Skill is stored at ../skills/leap/SKILL.md and distributed, without rewriting its core, by Agent Pack instructions. Its description is a useful signal, not a guarantee that the native agent will invoke it. The project AGENTS.md remains responsible for local source truth, permissions and validation.

Do not duplicate the entire methodology into Skills or introduce a mandatory registry/service. LEAP help must also work if no native Skill was installed and the AGENTS.md bootstrap was loaded.

## Related sources

- [LEAP Framework](leap.md)
- [LEAP Skills](leap-skills.md)
- [LEAP Charter](leap-charter.md)
- [Materiality Gate](materiality-gate.md)
- [Execution routing](execution-routing.md)
- [Workflow chooser](user/which-leap-workflow.md)
