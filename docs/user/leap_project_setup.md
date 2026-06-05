<!--
LEAP_DOC_METADATA:
  audience: user
  doc_type: adoption-guide
  authority: supporting-adoption-guidance
  applies_to: downstream-projects
END_LEAP_DOC_METADATA
-->

# LEAP Project Setup

LEAP helps ChatGPT and Codex understand your project before they suggest or make changes.

Follow these four steps.

## Step 1: Add LEAP to ChatGPT Project Instructions

Open your ChatGPT Project. Go to the Project Instructions area.

Paste this:

```text
This project uses the LEAP Framework.

When I invoke LEAP commands such as Run LEAP Charter, Run LEAP Recon, Generate LEAP Prompt, Run LEAP Prompt, Generate LEAP LHS, Run LEAP LHS, Run LEAP Governance, Run LEAP Validation, or Run LEAP Handoff, use LEAP Framework behavior instead of responding generically.

Use the current LEAP Framework documentation as the governing framework source when repo access is available. Use this project's source-of-truth files, repository evidence, and current conversation context when available. If local project instructions conflict with the current LEAP Framework docs, flag the conflict instead of silently choosing one.

Treat LEAP as:

LEAP Charter -> LEAP Recon -> LEAP Prompt -> Implementation -> Validation/Handoff

Preserve my wording unless I ask for rewriting. Use the required LEAP headings for the workflow being invoked. Inspect project files, source-of-truth docs, repo reality, branch/worktree/PR drift, existing functionality, and dependency or contract evidence when available and relevant.

Do not claim repo inspection happened unless it actually happened.

Do not generate implementation prompts prematurely. LEAP Prompt and LEAP LHS require sufficient source truth, repo reality, scope, non-goals, validation, stop conditions, and agent execution configuration.

If context is missing, apply Materiality Gate: inspect discoverable sources first, ask only questions that would materially change the work, proceed on stated assumptions for non-material unknowns, and stop for source-truth, destructive-change, privacy, security, money, identity, legal, user-trust, or unapproved architecture risks.

Always end LEAP outputs with a clear gate decision or recommended next step.
```

| Command                | Expected LEAP behavior                                                                                                                                |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------- |
| `Run LEAP Charter`     | Establish or reconcile project direction, source truth, roadmap, baseline assumptions, and implementation posture.                                    |
| `Run LEAP Recon`       | Investigate a focused feature, risk, layer, dependency, contract, repo area, or architecture question before implementation planning.                 |
| `Generate LEAP Prompt` | Create an agent-ready prompt only after source truth, repo reality, scope, validation, stop conditions, and execution configuration are clear enough. |
| `Run LEAP Prompt`      | Execute or apply an already-approved LEAP Prompt according to its scope, constraints, and stop conditions.                                            |
| `Generate LEAP LHS`    | Create a staged Layered House Standard prompt only when implementation gravity warrants staged execution.                                             |
| `Run LEAP LHS`         | Execute or apply an approved LHS prompt according to its Build Unit sequence, validation, and stop conditions.                                        |
| `Run LEAP Governance`  | Reconcile framework, repo, docs, prompt-library, source-of-truth, terminology, or adoption drift.                                                     |
| `Run LEAP Validation`  | Verify completed work against scope, tests/checks, docs, acceptance criteria, and stop conditions.                                                    |
| `Run LEAP Handoff`     | Summarize completed work, unresolved risks, validation status, deviations, and recommended follow-up.                                                 |

## Step 2: Add AGENTS.md to Your GitHub Project Root

Copy the LEAP repo-level AGENTS.md file into the root of your GitHub project.

Use the repo-level template from the LEAP Agent Pack:

<https://github.com/mcataloe/leap_agent_pack/blob/main/repo/AGENTS.md>

Your project should look something like this:

```text
my-project/
AGENTS.md
README.md
src/
package.json
```

The AGENTS.md file teaches Codex how to work inside this specific repo.

## Step 3: Run the AGENTS.md Population Prompt in Codex

Open your project in Codex.

Then copy and paste the population prompt from here:

<https://github.com/mcataloe/leap_agent_pack/blob/main/repo/AGENTS_Population_Prompt.md>

Codex should inspect your repo and fill in AGENTS.md using real project evidence.

Codex should not guess.

If something is unknown, Codex should mark it as TBD.

When a LEAP Prompt includes a "User Action Before Codex Submission" section, set Codex Plan Mode to the requested On, Off, or User decision required value before submitting the prompt. Codex Plan Mode is a user-controlled Codex setting, separate from the LEAP Execution Mode written inside the prompt.

## Step 4: Run LEAP Recon

Now go back to ChatGPT and say:

> Run LEAP Recon on {{feature, change, risk, or project area}}.

Examples:

> Run LEAP Recon on adding password reset.

> Run LEAP Recon on adding user profile settings.

> Run LEAP Recon on adding Stripe billing.

> Run LEAP Recon on replacing the current login flow with Okta.

> Run LEAP Recon on whether the API contract matches the frontend.

> Run LEAP Recon on cleaning up stale documentation.

LEAP Recon should return:

- What the feature, change, risk, or project area is trying to do.
- What project files or docs matter.
- What is already clear.
- What is unclear or risky.
- What questions need answers before building.
- What the recommended next step is.

For tiny, obvious tasks, you may not need Recon or full LEAP. Use a normal prompt when the change is small and easy to verify. Use a [Quick LEAP Brief](quick-leap-brief.md) when the work is still small but an AI coding agent needs guardrails. See [When Not to Use LEAP](when-not-to-use-leap.md) for the full rule of thumb.

## Simple Version

If you only remember one thing, remember this:

Use the Recommended Full Project Instructions in Step 1 when you want full LEAP command coverage.

1. Add LEAP to ChatGPT Project Instructions.
2. Put AGENTS.md in your GitHub project root.
3. Run the population prompt in Codex.
4. Ask ChatGPT:

> Run LEAP Recon on {{what you want to build or understand}}.
