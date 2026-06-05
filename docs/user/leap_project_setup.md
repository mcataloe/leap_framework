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

> This project uses the LEAP Framework.
>
> When I say “Run LEAP Recon on {{feature, change, risk, or project area}},” inspect the project context and help me understand the feature, risks, missing information, source-of-truth files, likely implementation areas, and recommended next step.
>
> Use LEAP Recon for analysis and pressure testing.
>
> Use LEAP Prompt when I need an implementation-ready prompt for Codex.
>
> Use LEAP Charter when the project needs deeper setup, source-of-truth cleanup, or direction setting.
>
> Do not guess. Use project files and repository evidence as the source of truth. If something is unknown, mark it as TBD.

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

1. Add LEAP to ChatGPT Project Instructions.
2. Put AGENTS.md in your GitHub project root.
3. Run the population prompt in Codex.
4. Ask ChatGPT:

> Run LEAP Recon on {{what you want to build or understand}}.
