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

Use the lightest LEAP workflow that controls the actual risk. If the work is tiny, obvious, and easy to verify, use a normal prompt. If the work is small but still needs coding-agent guardrails, start with a [Quick LEAP Brief](user/quick-leap-brief.md).

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

## How to choose a workflow

Start with the lightest workflow that controls the actual risk:

- Use the [workflow chooser](user/which-leap-workflow.md) for side-by-side routing between normal prompts, Quick Brief, Charter, Recon, Prompt, and LHS.
- Use [When Not to Use LEAP](user/when-not-to-use-leap.md) when you suspect full LEAP is heavier than the task.
- Use the [Quick LEAP Brief](user/quick-leap-brief.md) for the smallest useful coding-agent handoff.
- Use the [canonical framework reference](leap.md) when you need formal lifecycle and doctrine.

## The LEAP lifecycle

```text
LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff
```

LEAP Prompt is the family of agent-ready instruction artifacts. LEAP LHS is one format inside that family, used only when staged implementation is worth the structure.

Materiality Gate is not a phase. It is LEAP's question filter: ask only when the missing answer changes the work, inspect discoverable sources first, assume and proceed for polish-only unknowns, and stop for safety, source-truth, destructive-change, privacy, money, identity, legal exposure, or user-trust risks. See [Materiality Gate](materiality-gate.md) for the full rule.

## Why LEAP exists

People often start with a picture in their head of what a solution should be.

That picture can feel complete, but the missing pieces are often connected by emotion, urgency, assumptions, or taste rather than logic and mechanisms.

An existing repo can add a second problem: old docs, partial plans, duplicate roadmaps, and stale assumptions can compete with the current implementation.

A coding agent cannot safely build from that.

LEAP helps expose the gaps before major implementation begins.

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
https://github.com/mcataloe/leap_agent_pack
```

Use [LEAP Project Setup](user/leap_project_setup.md) for the adoption path across ChatGPT Project Instructions, repository-level `AGENTS.md`, Codex population, and the first LEAP Recon.

## The LEAP rule of thumb

```text
Ask until the idea becomes buildable.
Then stop asking and build only the bounded task.
```

LEAP should reduce chaos, not create ceremony. If the framework is slower than the low-risk work itself, use a lighter mode.
