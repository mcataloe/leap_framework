<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: entrypoint
  authority: entry-point
  applies_to: leap-framework
END_LEAP_DOC_METADATA
-->

# Start Here: LEAP in Plain English

**LEAP - Layered Execution & Alignment Protocol** helps you avoid asking an AI coding agent to build from confusion.

AI coding agents can move quickly. That is useful only when the idea is clear, source documents are current, repo state is understood, and the task is small enough to verify.

LEAP helps with the messy middle between:

```text
"I have an idea"
```

and:

```text
"Here is a bounded implementation task an AI coding agent can safely run."
```

## LEAP in 60 seconds

LEAP helps turn rough software intent into a safe coding-agent handoff.

It does this by helping you:

1. Clarify the project.
2. Inspect what is already true.
3. Separate facts from assumptions.
4. Bound the work.
5. Tell the agent what to do, what not to touch, and when to stop.
6. Validate the result.

Use the lightest LEAP workflow that controls the actual risk. If the work is small, clear, and easy to verify, start with a [Quick LEAP Brief](user/quick-leap-brief.md).

## The simple version

LEAP asks:

```text
What are we trying to build?
Who is it for?
What problem does it solve?
What already exists?
What do the current docs say?
Which docs are canonical?
Which docs are stale or archived?
Which dependencies or external contracts may affect this work?
What should not be built?
What could go wrong?
What should the agent stop and ask about?
How do we prove the work is done?
```

If those answers are unclear, LEAP keeps asking focused questions before creating an implementation prompt.

Questions are not a delay. Questions are how LEAP turns a vague idea or messy repo into a buildable system.

## Why LEAP exists

People often start with a picture in their head of what a solution should be.

That picture can feel complete, but the missing pieces are often connected by emotion, urgency, assumptions, or taste rather than logic and mechanisms.

An existing repo can add a second problem: old docs, partial plans, duplicate roadmaps, and stale assumptions can compete with the current implementation.

A coding agent cannot safely build from that.

LEAP helps expose the gaps before major implementation begins.

## The LEAP lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP Prompt is the family of agent-ready instruction artifacts. LEAP LHS is one format inside that family, used only when staged implementation is worth the structure.

Materiality Gate is not a phase. It is LEAP's question filter: ask only when the missing answer changes the work, inspect discoverable sources first, assume and proceed for polish-only unknowns, and stop for safety, source-truth, destructive-change, privacy, money, identity, legal exposure, or user-trust risks.

## Which LEAP workflow should I use?

| Use this | When |
| --- | --- |
| [Quick LEAP Brief](user/quick-leap-brief.md) | The task is small, source truth is clear, repo impact is localized, and one Build Unit or less is involved. |
| [LEAP Charter](leap-charter.md) | Project direction is unclear, docs are stale or conflicting, a greenfield idea needs shaping, or a brownfield repo needs source-truth reconciliation. |
| [LEAP Recon](../templates/leap-recon-lite-template.md) | The baseline is good enough, but a focused feature, risk, layer, dependency, contract, or architecture question needs investigation. |
| [LEAP Prompt](../templates/leap-prompt-template.md) | The work is bounded, repo reality is understood, source truth is clear, and the coding agent needs implementation-ready instructions. |
| [LEAP LHS](leap.md) | Implementation gravity is high: staged, layered, multi-area work where tests, docs, rollback, sequence, or commit boundaries matter. |

For scenario examples and copy-ready starter phrasing, see [Which LEAP workflow should I use?](user/which-leap-workflow.md). For a short Recon request, use [LEAP Recon Lite](../templates/leap-recon-lite-template.md).

### 1. LEAP Charter

Use LEAP Charter when the project direction or source truth needs to be established or reconciled.

LEAP Charter establishes or reconciles:

```text
- project direction
- source-of-truth docs
- roadmap
- baseline assumptions
- documentation structure
- implementation posture
- prompt backlog
- AGENTS.md guidance when applicable
```

Greenfield Mode is for brand-new projects and early-stage ideas.

Brownfield Mode is for existing or mid-buildout projects. It inspects docs and repo reality, identifies gaps, canonicalizes current docs, archives stale docs, and prepares future LEAP Recon, LEAP Prompt, or LEAP LHS work.

Brownfield Charter follows this rule:

```text
Canonicalize forward.
Archive backward.
Preserve traceability.
Never let stale docs compete with source-of-truth docs.
```

### 2. LEAP Recon

Use Recon when there is a focused area, gap, risk, feature, architectural question, repo, layer, or plan to investigate.

Recon checks:

```text
- what the canonical docs say
- what the repo actually does
- what is stale or archived
- what already exists
- what branches or PRs may conflict
- what shared contracts may be affected
- what declared or detected dependency contracts may have drifted
- what Build Units should be sequenced
```

Dependency & Contract Recon is part of LEAP Recon when dependencies, provider APIs, services, packages, or shared contracts are relevant. It looks for a dependency register such as `leap.dependencies.yaml`, follows declared contract links such as OpenAPI sources when accessible, and reports current-work impact, general system impact, or unknowns needing verification.

### 3. LEAP Prompt

Use LEAP Prompt only after Charter and/or Recon are clear enough.

A LEAP Prompt produces Codex-ready instructions for analysis, documentation, implementation, or remediation.

It tells the coding agent:

```text
- the objective
- what is in scope
- what is not in scope
- what files to inspect
- what files not to touch
- what constraints apply
- what tests/checks to run
- when to stop instead of guessing
- what execution profile to use
```

LEAP LHS is a structured LEAP Prompt format for layered implementation work using the House Standard. It is not a mandatory lifecycle stage, and not every LEAP Prompt is an LHS prompt.

LEAP Prompt is a family of prompt types:

```text
- Charter Prompt
- Recon Prompt
- Standard Implementation Prompt
- Fix Prompt
- Refactor Prompt
- Governance Prompt
- Validation Prompt
- LHS Prompt
```

Use LHS only when implementation gravity is high enough to justify staged execution: multi-file or multi-area work, dependency order, tests and docs, phased commits, rollback risk, architecture/data/workflow changes, named-layer work, follow-up work, or explicit acceptance criteria.

### 4. Implementation

Implementation is the execution of the approved LEAP Prompt by Codex or another coding agent.

The agent should build only the bounded task, follow the repo's patterns, and stop if the prompt's stop conditions are met.

### 5. Validation/Handoff

Validation/Handoff is the required completion step.

The agent should:

```text
- verify changes
- run or explain tests/checks
- check whether docs need updates
- summarize work completed
- report deviations or stop conditions
- recommend follow-up LEAP Recon, LEAP Prompt, or LEAP LHS work
```

## The Ideation Loop

LEAP does not assume the first version of an idea is ready to build.

It loops:

```text
Idea -> Questions -> Assumptions -> Pressure test -> Better idea -> Gate decision
```

The loop continues until the next safe step is clear.

Use the loop when:

```text
- the problem is vague
- the user is unclear
- the workflow is not known
- the MVP is too broad
- non-goals are missing
- risks are hand-waved
- source truth is missing
- docs conflict with repo reality
- archived docs might be mistaken for current docs
- the agent would need to guess
```

## The shortest useful LEAP checklist

Before giving work to an AI coding agent, answer:

```text
1. What is the goal?
2. What is the current state?
3. What is in scope?
4. What is out of scope?
5. What files/docs are source truth?
6. What docs are stale, archived, or do-not-use?
7. What should the agent not touch?
8. What tests/checks prove success?
9. When should the agent stop and ask?
10. What model/reasoning/execution profile should be used?
```

If you cannot answer these, run LEAP Charter or Recon first.

## AGENTS.md adoption

LEAP AGENTS.md templates are distributed from the dedicated LEAP Agent Pack repository:

```text
https://github.com/mjcataldi/leap_agent_pack
```

Use that repository for AGENTS.md templates, install guidance, versioning, compatibility manifests, and upgrade guidance.

Recon may check whether an installed downstream `AGENTS.md` file is current, outdated, pinned, forked, unversioned, malformed, missing, or non-LEAP. AGENTS updates are notify/manual-merge only; LEAP should not overwrite project-specific or local override sections automatically.

## When to use full LEAP

Use full LEAP for:

```text
- new products
- major features
- AI-heavy workflows
- multi-file changes
- existing repos with stale docs
- documentation reconciliation
- data model changes
- API changes
- dependency contract drift
- auth/session/permission changes
- billing or credit logic
- privacy/security-sensitive features
- multiple people or agents working in parallel
```

Use Small Project Mode for:

```text
- tiny fixes
- obvious one-file changes
- text edits
- low-risk UI cleanup
- tasks with clear acceptance criteria
```

For most first-time lightweight work, use the [Quick LEAP Brief](user/quick-leap-brief.md) instead of full Charter and Recon.

## The LEAP rule of thumb

```text
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```

LEAP should reduce chaos, not create ceremony.

If the framework is slower than the low-risk work itself, use a lighter mode.
