# Semantic Router LHS — QA and Cross-Repository Handoff

Date: 2026-10-14
Status: **Static contract checks passed; native automatic invocation unverified.**
Branches: feature/leap-semantic-router-20261014 in both repositories.
Merge posture: **Review required; do not merge until native acceptance is exercised or the reviewer explicitly accepts this limitation.**

## Implementation summary

- BU-01: Canonical workflow-selection contract, LEAP help, optional Discovery and Pressure Test, concise domain brief, and portable LEAP Skill navigator.
- BU-02: Optional project-scope Skill installation guide, optional project-specific Skill template and population prompt, global/repo/combined AGENTS.md routing, manifest and upgrade instructions in Agent Pack.
- BU-03: 46 expected-routing specifications, Python standard-library static validator, backward-compatibility and no-mutation safeguards.

## Measured checks

The repository-connected readbacks from the feature branches confirmed:

1. Framework: 13 targeted static assertions passed (46 unique cases, all 16 required route outcomes, >=12 semantic cases, >=4 safety cases, valid name/description Skill metadata, source contract, unchanged lifecycle, corrected setup paths and linked documentation).
2. Agent Pack: 12 targeted static assertions passed (three bootstrap modes contain LEAP help; Cleanup is in global/combined command tables; template section markers preserved; manifests and starter paths resolve; optional install and no-overwrite guidance exist; release state remains unreleased).
3. Framework semantic-routing and Discovery markdown: seven unique local reference targets fetched successfully through GitHub.
4. Agent Pack Skill installation guide: two relative reference targets fetched successfully.
5. GitHub compare to main: Framework feature branch ahead with 0 behind; Agent Pack feature branch ahead with 0 behind at QA time.
6. Two repositories' relevant paths checked directly; the previously corrected setup links still target templates/separated/repo.

These are **static checks only**; expected route labels are test specifications, not observed classifier outcomes.

## Native behavior status

| Environment | Native Skill loading | Automatic selection accuracy | Explicit commands |
|---|---|---|---|
| Codex | NOT TESTED | NOT MEASURED | NOT TESTED live |
| Claude Code | NOT TESTED | NOT MEASURED | NOT TESTED live |

Neither native command was available in this execution environment. The target >=90% correct semantic selection, 100% explicit-command selection and zero authorization failures remain **unverified acceptance targets**, not passing results. The Python checkout validator has been committed but was not executed on a local checkout; the connected-repository static checks above are the measured evidence.

## Reproduce locally after checking out both feature branches

1. In the Framework checkout, run:

   ~~~bash
   python tests/validate_semantic_router.py --agent-pack ../leap_agent_pack
   ~~~

2. Read [Agent Pack installation instructions](https://github.com/mcataloe/leap_agent_pack/blob/feature/leap-semantic-router-20261014/docs/skills-installation.md) and install Framework skills/leap/SKILL.md into the Codex and/or Claude project location. If testing against feature branches before merge, install from the same feature-branch checkout, not the current main branch.
3. Start a **new** native assistant session within the project. Confirm the Skill is listed and can be invoked directly.
4. Run the 46 cases in tests/semantic-routing-cases.json with the user input in the actual assistant. Record: selected route, Skill load evidence, allowed/disallowed mutation, and whether the agent stopped correctly. Run with project permissions that prevent destructive effects and prefer a disposable test repository.
5. Record per-case Codex results independently of Claude Code results. Explicit routes must reach 100%; semantic routes target >=90%; unauthorized mutation count must remain zero.
6. Include at least LEAP help, Discovery-vs-Recon, Generate-vs-Run Prompt, Cleanup discovery-only, a tiny ordinary task and No Gate hard STOP in each smoke test.
7. If routing misfires, first refine native Skill description and bootstrap negative triggers; do not build a custom service without a separate LEAP decision.

## Adoption and rollback

Adoption sequence: merge Framework PR first; then Agent Pack PR after cross-repo link and compatibility review; downstream users manually reconcile their customized AGENTS.md and optionally copy the standard Skill to .agents/skills or .claude/skills. No separate SKILLS.md is required.

Rollback: remove the optional installed Skill files or restore the previously pinned installed copies. Existing explicit LEAP commands in AGENTS.md continue to work. Keep project-specific modifications; never overwrite them during upgrade.

## Remaining risks

- Implicit selection is model-dependent; false positives/negatives remain until measured in native sessions.
- The Skill references canonical Framework main URLs that become active after merging the Framework change. Before merge use branch-scoped sources.
- Upgrades must respect separate Framework/Agent Pack versioning and local edits.
- New package/code is documentation and tests only; no application runtime or CI was deployed.

**Gate:** Draft PR review ready; native invocation acceptance still outstanding.
