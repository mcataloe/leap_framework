# LEAP Validation — Standard Operational Prompt

Run LEAP Validation/Handoff on completed or partially completed work.

Validation/Handoff is the required completion step of the LEAP lifecycle. It proves what changed against what was allowed, records what was and was not checked, and states an honest verification state. It is the guardrail that catches scope creep and unverified "done" claims.

Variant of: [`leap-prompt-standard.md`](leap-prompt-standard.md) (Validation Prompt). Verification-state doctrine: [`../docs/execution-routing.md`](../docs/execution-routing.md#5-implementation-state-versus-verification-state).

## Command contract

```text
Run LEAP Validation on <branch, PR, commit range, or working tree>
against <governing Prompt, Quick Brief, issue, or stated scope>.
```

Inherit same-thread context. When no governing scope exists, reconstruct it from the request that produced the work and say so.

Default posture is `validation-only`: inspect and report. Do not fix findings unless the user asks. Re-running checks is allowed; editing source is not.

## Required checks

Perform each check against evidence, not memory of the implementation.

1. **Diff against scope.** List every changed path from the actual diff (for example `git diff --name-status <base>...HEAD` plus uncommitted changes). Classify each as *in scope*, *out of scope but justified*, or *out of scope — unexplained*. Any change to a "do not touch" path is a finding.
2. **Non-goal check.** For each stated non-goal, confirm the diff does not implement it.
3. **Acceptance check.** For each acceptance criterion, cite the evidence (test, output, file, or manual check) or mark it unmet.
4. **Checks run.** List each test, build, lint, or manual check with the command and a short result. Paste failing output, not a summary of it.
5. **Checks not run.** List each required check that was not run and why (unavailable surface, missing credentials, out of time, blocked).
6. **Stop conditions.** List any stop condition that fired during implementation and how it was resolved, or confirm none fired. Flag any stop condition that should have fired but did not.
7. **Hard-stop areas.** Confirm no unapproved dependency, migration, auth, security, data, destructive, or public-contract change is present in the diff.
8. **Docs and source truth.** Confirm required documentation updates were made, or list them as follow-up.

## Verification state

Report exactly one:

- **Execution verified** — every required execution-grounded check ran and passed.
- **Partially verified** — some required checks passed; named checks are unavailable, blocked, or pending.
- **Implemented — execution unverified** — artifacts changed but required runtime, build, or integration checks were not run.
- **Failed** — a required check ran and failed, or an unexplained out-of-scope change or hard-stop violation is present.

Never report "complete" when the Definition of Done requires checks that did not run. Static review supports confidence; it does not replace a required runtime check.

## Required output

Keep each section short. Write "None" rather than padding.

```markdown
# LEAP Validation — <work item>

## 1. Verification State
<one state from the list above, plus one sentence why>

## 2. Scope Check
| Path | Change | Classification | Note |
|---|---|---|---|

Non-goals respected: yes / no — <detail>

## 3. Acceptance
| Criterion | Evidence | Met? |
|---|---|---|

## 4. Checks Run
| Check | Command | Result |
|---|---|---|

## 5. Checks Not Run
| Check | Why | Risk |
|---|---|---|

## 6. Stop Conditions and Hard Stops
<fired / should have fired / none>

## 7. Follow-up
<docs still needed, unresolved findings, recommended next LEAP work>
```

## Decision

End with one of:

- `accept` — verification state is Execution verified and no findings remain
- `accept-with-follow-up` — acceptable to merge; named follow-ups are recorded
- `return-for-fix` — findings must be fixed before merge
- `escalate` — a human decision is required (hard stop, unexplained scope, or ownership question)

## Team use

Copy the Verification State, Scope Check, Checks Not Run, and Stop Conditions sections into the pull request description. The [LEAP pull request template](../templates/leap-pull-request-template.md) carries the same fields.
