# LEAP Code Assistant Recon-Only Request Template

Illustrative only. Use this template inside a code assistant that already has access to the target repository.

This template is for **Recon only**. It should inspect repo reality, identify source truth and risk, classify the planning boundary, refine Delivery Units and Build Units, and decide whether implementation is safe to plan.

It is not an implementation Prompt.

## When to use

Use when:

```text
- the code assistant can inspect the target repo
- the project baseline is reasonably established
- you have one focused Initiative, Delivery Unit, Build Unit, Domain,
  Architecture area, feature, risk, dependency, contract, or legacy Layer
- you want repo-aware analysis before implementation
- you do not want files modified yet
```

Do not use when:

```text
- the Mission, user, problem, MVP, Strategic Outcome, or non-goals are unclear
- Initiative ownership is materially unclear
- docs require broad Brownfield reconciliation first
- the assistant cannot inspect the repo
- you want implementation to begin immediately
```

Run Charter first when the baseline or project direction is unclear.

## Copy-ready Prompt

```text
Run LEAP Recon on this codebase.

Target:
<Strategic Outcome, Initiative, Delivery Unit, Build Unit, Domain,
Architecture area, feature, risk, dependency, contract, question,
or legacy Layer>

Traceability, when the project uses it (or link a Jira, Azure DevOps,
or GitHub work item):
- Initiative / Delivery Unit / Build Unit or bounded task:
- Affected Domains or Architecture areas:

You already have access to the target codebase.

Do not implement anything.
Do not modify files.
Do not generate the implementation Prompt yet.
Do not silently make product, Architecture, schema, auth, security,
privacy, billing, data, or AI-behavior decisions.

Inspect the repo and return a Recon report identifying:
- Baseline Freshness Check result
- source-of-truth docs and stale, archived, missing, or conflicting docs
- alignment with strategy, planning records, and Architecture, when present
- current repo reality
- existing functionality related to the target
- affected files, routes, models, schemas, components, services, tests,
  configs, dependencies, and contracts
- cross-Initiative, cross-Domain, and cross-repository impacts
- whether the target is Initiative-sized, Delivery-Unit-sized,
  Build-Unit-sized, Domain-oriented, Architecture-oriented, a Phase,
  or an ambiguous legacy Layer
- legacy Layer classification, when relevant
- recommended Delivery Units when a release, enablement, adoption,
  demonstration, or cross-repository boundary exists
- recommended bounded Build Units
- areas not to touch
- risks, sensitive areas, and destructive-change concerns
- stop conditions
- tests and checks likely required
- material questions before Prompt generation
- recommended Agent Execution Configuration

Do not globally replace Layer terminology.

If required sources or implementation evidence are unavailable, stop and report what is missing.

Return only the Recon report.
```

## Expected Recon output and gate decisions

Use the output format and gate decisions in the [Recon standard](../prompts/leap-recon-standard.md). Omit sections with nothing material. Do not pad with N/A.

## Agent Execution Configuration

| Field | Recommendation | Rationale |
|---|---|---|
| Agent / Tool | Codex / Cursor / Claude Code / other | Why |
| Model | Exact model or approved default | Why |
| Reasoning Level | Low / Medium / High / Extended | Why |
| Execution Mode | implement-directly / repo-preflight-then-implement / plan-first / recon-only / validation-only | Why |
| Repository | Repo or repositories | Why |
| Branch / Worktree | Target context | Why |
| Permissions | Allowed changes | Why |
| Validation | Tests and checks | Why |
| Commit Guidance | Commit posture | Why |

Tool-specific fields such as Codex Plan Mode and Scope Scale are optional — omit when not needed. See [current-provider profiles](../docs/execution-routing.md#8-current-provider-profiles).

## Stop conditions

Stop instead of guessing if:

- required files or source docs are missing
- docs conflict with repo reality
- archived docs are treated as current source truth
- ownership of the target is materially unclear
- existing implementation contradicts the target
- work violates non-goals
- unapproved product or Architecture decisions are required
- unapproved schema, migration, auth, permission, billing, privacy,
  security, data, or AI-behavior changes are required
- destructive changes appear necessary without authorization
- branch or worktree drift creates unclear ownership
- tests or validation are missing or unclear
- a legacy Layer cannot be classified safely

This template is intentionally lightweight. Escalate to Charter when direction, scope, risk, or source truth is unclear.
