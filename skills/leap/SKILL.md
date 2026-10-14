---
name: leap
description: Route explicit LEAP commands and help requests; in a LEAP-adopted project, select Discovery, Pressure Test, Recon or other LEAP workflow when the user wants that methodology. Do not trigger for generic programming questions or ordinary tiny edits.
---

# LEAP workflow navigator

Use this Skill as a small entry point, not a replacement for the LEAP Framework. A native Skill is optional: existing explicit LEAP commands and project AGENTS.md continue to work without it.

## When to use

- The user says LEAP help, names a LEAP workflow, or asks which LEAP procedure suits a project decision.
- The user asks for domain discovery, a proposal pressure test, or project reconnaissance in an adopted LEAP project.
- The user requests a nontrivial engineering workflow where choosing the right LEAP stage materially reduces risk.

Do not use for trivial routine edits, generic explanations, unrelated chat, or tasks clearly governed by another methodology.

## Router

1. Honor the explicit user workflow first, subject to permissions and hard blockers.
2. If the user asks for LEAP help, show the supported menu: Discovery, Pressure Test, Charter, Recon/Lite, Generate/Run Prompt, Generate/Run LHS, Governance, Cleanup, Validation and Handoff. Explain Quick Brief and No Gate as optional variant/modifier.
3. Without explicit command, classify by intent:
   - Understand domain, actors and relationships -> Discovery.
   - Test a candidate idea, risks and alternatives -> Pressure Test.
   - Establish or reconcile project strategy and sources -> Charter.
   - Inspect actual repo state and design feasibility -> Recon, Lite when narrow.
   - Produce agent-ready instructions -> Generate Prompt, LHS when multi-stage.
   - Execute approved instructions -> Run Prompt/LHS, respecting actual approval and bounds.
   - Reconcile docs -> Governance; obsolete artifact candidates -> Cleanup.
   - Verify work -> Validation; report completion -> Handoff.
   - Tiny obvious task -> ordinary response without formal LEAP ceremony.
4. Follow the canonical source at https://github.com/mcataloe/leap_framework/blob/main/docs/semantic-routing.md and the corresponding current Framework operational prompt when accessible. If not accessible, disclose the limitation and proceed only within the known, safe boundary.
5. Consult project AGENTS.md, source truth, existing branch/worktree, and current approved scope before recommending implementation. Never invent external tool permissions.

## Hard boundaries

- Discovery, Pressure Test, Charter and Recon are normally non-mutating. Separate authorization is required for any modifications.
- Generate Prompt is not Run Prompt.
- Cleanup inventories and proposes decommission; no deletion without exact human approval.
- No Gate does not bypass hard STOP, destructive, contract, security or data-ownership checkpoints.
- Skills never expand Build Unit scope or LEAP Prompt permissions.
- LEAP semantic routing selects the workflow; execution routing separately selects the tools/environment.
- If the Skill source cannot be loaded, do not claim it was loaded or completed.

## Verification and output

State the selected workflow when that choice materially affects behavior. Return its required deliverable and gate/next step. For native-skill invocation, distinguish confirmed load from assumed availability; for mutations, use repository tests and explicit Validation/Handoff evidence.
