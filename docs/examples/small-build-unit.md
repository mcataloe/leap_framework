# Example: Small Build Unit

This example shows how LEAP can stay lightweight for a small implementation task.

---

## Scenario

A product has an existing settings page. The user wants all dismissible notifications to use the same close behavior and visual pattern.

This is small enough for a Quick LEAP Brief if the existing notification component is clear and no shared state/API changes are needed.

---

## Quick LEAP Brief

```text
# Quick LEAP Brief — Normalize dismissible notifications

## 1. Goal
- Ensure all notification summaries on the settings page can be dismissed using the existing notification close pattern.

## 2. Current State
- Settings page already renders several notification/summary blocks.
- Existing toast notifications already support dismissal.
- Source truth: current implementation on target branch and existing notification/toast components.

## 3. Scope
In scope:
- Inspect existing notification/toast patterns.
- Reuse existing dismissible notification behavior where possible.
- Apply consistent dismiss behavior to settings-page validation/summary notifications.
- Add or update tests if notification behavior already has test coverage.

Out of scope:
- Do not redesign the full settings page.
- Do not introduce a new notification system.
- Do not change backend validation behavior.
- Do not change API contracts.

Files/areas to inspect:
- settings page component
- existing toast/notification component
- related tests

Files/areas not to touch:
- authentication/session code
- API routes
- database schema/migrations
- unrelated app navigation

## 4. Constraints
- Follow existing UI and accessibility patterns.
- Do not introduce new dependencies.
- Preserve existing notification copy unless a small wording correction is required.

## 5. Verification
Run/check:
- relevant component tests
- lint/typecheck if available
- manual check that each notification can be dismissed and does not reappear unexpectedly in the same view state

Done means:
- Settings-page summary notifications use a consistent dismiss behavior.
- Existing toast behavior still works.
- No unrelated settings behavior changes.

## 6. Stop Conditions
Stop and ask if:
- there is no reusable notification pattern
- notification state is controlled by shared global app state not covered by this brief
- dismissal requires backend persistence or schema changes
- tests reveal unrelated failures

## 7. Agent Execution Configuration
- Agent / Tool: project-approved coding agent
- Codex Plan Mode: Off, if using Codex
- Model: project-approved implementation model
- Reasoning Level: Medium
- Execution Mode: implement-directly
- Scope Scale: small task
- Repository: <repo>
- Branch / Worktree: <target branch>
- Permissions: settings-page notification UI only
- Validation: relevant tests + lint/typecheck if available
- Commit Guidance: one commit, message: `Settings — Normalize dismissible notifications`
```

---

## Why this is small enough

This task has:

```text
- clear target behavior
- obvious source truth
- limited files
- no schema/API/auth changes
- no product-strategy ambiguity
- reusable existing pattern
```

If any of those stop being true, escalate to Recon.
