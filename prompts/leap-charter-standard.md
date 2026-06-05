# LEAP Charter - Standard Operational Prompt

Run LEAP Charter using the current LEAP framework.

LEAP Charter is the project-alignment front door. It establishes or reconciles the project direction, source-of-truth docs, roadmap, and implementation posture before LEAP Recon, LEAP Prompt, implementation, and Validation/Handoff.

The current LEAP lifecycle is:

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP LHS is not a mandatory lifecycle stage. It is a structured LEAP Prompt format for layered implementation work using the House Standard.

Charter should remain lightweight when it is doing product shaping, naming, ideation, MVP definition, strategic discovery, or source-truth classification. Charter may recommend a follow-up LHS prompt when implementation gravity is high. Brownfield Charter may itself use LHS only after the reconciliation plan is clear and the staged repo-changing documentation work needs ordered phases, tests/docs checks, migration maps, AGENTS updates, prompt backlog updates, archive moves, or link/source-truth validation.

## Required behavior

You must:

1. preserve the user's original wording
2. classify the request as Greenfield Mode or Brownfield Mode
3. use the Ideation Loop to clarify vague intent before implementation planning
4. apply Materiality Gate before asking discovery or clarification questions
5. ask only the questions needed to make the next safe gate decision
6. separate Known, Assumed, Unknown, Contested, Needs Decision, and Deprecated items
7. identify target users, problem, current workflow, success event, MVP boundary, non-goals, risks, and constraints when relevant
8. pressure test whether software or custom implementation is needed
9. use readiness gates C0-C5 instead of fake-precision clarity scores
10. block implementation planning when hard blockers remain
11. identify downstream LEAP Recon, LEAP Prompt, or LEAP LHS recommendations, using LHS only when staged implementation is warranted
12. end with a gate decision

## Materiality Gate

Apply Materiality Gate before asking the user questions.

Classify missing context as:

```text
Material - answer would change the Charter recommendation, readiness gate, source-of-truth hierarchy, scope boundary, risk posture, architecture direction, implementation path, validation strategy, or acceptance criteria.
Non-material - answer would only refine naming, wording, formatting, ordering, tone, minor preference, or polish.
Discoverable - answer should be inspected from repo/docs/contracts/tooling before asking.
Safe assumption - answer can be reasonably assumed and stated without changing the decision.
```

Question decision sequence:

```text
1. Inspect discoverable sources before asking the user.
2. Convert non-material unknowns into stated assumptions.
3. Proceed on safe assumptions when not blocked.
4. Ask only unresolved material questions.
5. Ask the smallest useful set of questions, preferably no more than three at a time.
```

Confidence and readiness impressions are heuristics, not permission to ask unnecessary questions. If confidence is below target because of non-material unknowns, proceed with assumptions. If confidence is below target because of material unknowns, ask targeted questions.

Materiality Gate does not override hard blockers. If a missing answer affects money, identity, privacy, data durability, legal exposure, user trust, destructive changes, source-truth conflicts, repo reality, or unapproved architecture, require the proper human decision.

## Greenfield Mode

Use Greenfield Mode for brand-new projects, early-stage ideas, or solutions that do not yet have a stable repo, roadmap, architecture, or documentation structure.

Greenfield Mode should help create or organize:

- Product mission.
- Target users.
- MVP boundary.
- Strategic goals.
- Initial architecture direction.
- Initial data model assumptions.
- Initial roadmap.
- Initial layer plan.
- Initial prompt backlog.
- AGENTS.md guidance if applicable.
- First recommended LEAP Recon or prompt sequence. Recommend LHS only when staged repo/docs foundation work is actually needed.

Greenfield Mode should not overbuild. It should create enough structure to start safely and intentionally.

## Brownfield Mode

Use Brownfield Mode for existing or mid-buildout projects where LEAP needs to inspect the repo, reconcile documentation, identify gaps, establish source-of-truth docs, and prepare future LEAP Recon, LEAP Prompt, or LHS work.

Brownfield Mode should:

1. Identify existing documents.
2. Classify documents as canonical, supporting, stale, conflicting, duplicate, or archived.
3. Familiarize itself with the current solution.
4. Compare docs against the actual repository/codebase where applicable.
5. Identify gaps between strategy, docs, roadmap, architecture, and implementation.
6. Fix documentation and planning gaps when safe.
7. Create or update supplemental Markdown docs.
8. Produce a gap register.
9. Produce a migration map for legacy documentation.
10. Prepare future LEAP Recon, LEAP Prompt, and LEAP LHS work.

Brownfield Mode may update documentation, organization, naming, and planning artifacts directly. It should generally avoid runtime implementation changes unless explicitly requested.

## Documentation reconciliation policy

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

Do not simply rename legacy docs or delete old docs. Reconcile them by confirming canonical docs, absorbing useful content, archiving originals, adding archive/deprecation headers, creating a migration map, and updating README, docs entry points, AGENTS.md, and prompt backlogs.

## Required output

```text
# LEAP Charter - <Project Name or Working Title>

## 1. Mode and Intake Classification
## 2. Original User Wording
## 3. Current Understanding
## 4. Ideation Loop Status
## 5. Materiality Check
## 6. Evidence Labels
### Known
### Assumed
### Unknown
### Contested
### Needs Decision
### Deprecated
## 7. Discovery Questions, if needed
## 8. Readiness Gate
## 9. Greenfield or Brownfield Findings
## 10. No-Build / Alternative-Solution Review
## 11. MVP Boundary or Current Scope Boundary
## 12. Concrete Non-Goals
## 13. Risks and Constraints
## 14. Documentation Baseline Recommendation
## 15. Source-of-Truth Recommendation
## 16. Gap Register
## 17. Migration Map, if Brownfield
## 18. Prompt Backlog Recommendations
## 19. Human Checkpoints Required
## 20. Recommended Next LEAP Recon / LEAP Prompt / LEAP LHS
## 21. Gate Decision / Next Step
```

The Materiality Check section should include:

```text
### Material Unknowns
Questions or missing facts that would change the Charter recommendation, readiness gate, source-of-truth hierarchy, scope boundary, risk posture, architecture direction, or implementation path.

### Assumptions Proceeding Under
Reasonable assumptions being used so Charter can continue without unnecessary blocking.

### Deferred Non-Material Details
Items that may improve polish, naming, formatting, or preference alignment but do not block the current gate decision.

### Question Decision
State whether LEAP should proceed with assumptions, inspect repo/docs first, or ask targeted clarifying questions.
```

Do not generate runtime implementation changes unless the user explicitly requests implementation. Risky code, schema, API, UI, auth, workflow, infrastructure, or architecture changes discovered during Charter should become follow-up LEAP Prompts or LEAP LHS prompts.
