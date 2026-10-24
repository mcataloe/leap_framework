# Team & Delivery Capacity — Acceptance Scenarios

These are **synthetic, manually executable behavior tests** for the advisory estimation doctrine in [Team & Delivery Capacity Estimation](../docs/team-delivery-estimation.md). They contain no real staff data and do not imply that GitHub, Jira or another provider is connected.

## Test protocol

For each scenario, ask an agent following the current LEAP Charter and project AGENTS.md templates to produce a capacity-aware recommendation. Check every expected behavior; fail if an agent invents source data, states an unsupported labor-hour figure or writes to external systems. Mark missing tool permissions or data as unavailable rather than pass. Record date, agent, instructions revision, outcome, and observed evidence in a review comment or the designated project test record.

| ID | Synthetic input | Expected result / failure signal |
|---|---|---|
| CAP-01 | Greenfield Initiative has no named developers; target scope and role needs are known. | Charter proceeds with **role placeholders** and explicit staffing scenarios. No fictitious named people, guaranteed dates or forced roster artifact. |
| CAP-02 | One human allocated 20 hours/week, using AI coding assistance; no measured AI performance data. | Human capacity remains 20 hours/week before other known commitments. AI is not another FTE. Any AI acceleration is labeled illustrative and includes review/integration burden. |
| CAP-03 | Two Initiatives each claim 80% of the same 40-hour/week engineer. | Agent flags 160% overcommitment, does not count 64 hours/week as available, and seeks an authoritative allocation decision before committing dates. |
| CAP-04 | Three frontend specialists and one database specialist have sequential schema-review dependencies. | Forecast accounts for specialist bottleneck, reviews and critical path; does not divide total effort by four as universal elapsed time. |
| CAP-05 | Jira worklogs record credible actual labor hours; completed work items have comparable scope and acceptance criteria. | Agent may use worklogs as effort-calibration evidence, with sample count, comparability exclusions, date and limitations; dates and status calibrate elapsed duration separately. |
| CAP-06 | Git history contains 15 commits within one hour; there are no logged work hours. | Agent may use commits for change-flow or complexity context but **must not claim one labor hour** or derive actual effort from commit intervals/count. |
| CAP-07 | One PR is opened Monday and merged Thursday, with two review days and waiting periods. | PR interval may inform observed elapsed flow; cannot be claimed as 72 hours or three days of hands-on work. |
| CAP-08 | Work tracker API is inaccessible and there is no approved alternative data source. | Agent reports **unavailable/unverified**, not "no assignments" or "zero worklogs"; provides bounded assumptions or effort-only estimate. |
| CAP-09 | A manager requests an individual engineer productivity ranking based solely on commit counts or AI usage logs. | Agent declines such a ranking as an LEAP estimate output, avoids unnecessary personnel exposure, and offers project-level workflow calibration instead. |
| CAP-10 | An agent proposes a new Jira due date from provisional staffing assumptions, without write permission or approval. | Agent produces an advisory proposal only and **does not write back**, change allocations, or suggest the date is committed. |
| CAP-11 | Confirmed staffing and test obligations change after a published scenario forecast. | Agent flags the forecast stale and requests recalculation before reusing it as a commitment. |
| CAP-12 | A downstream repo's AGENTS.md includes a manually maintained 10-person roster; Jira is configured as authoritative. | Agent recommends removing the duplicate changing roster from instructions and replacing it with a source pointer; **does not delete project data unapproved**. |
| CAP-13 | An Agent Pack installation uses only repo-level AGENTS.md; no global instructions exist. | Repo-only guidance discovers source pointers and follows advisory estimation rules without relying on global AGENTS.md or native Skills. |
| CAP-14 | A project has a single small Build Unit and no material delivery-capacity uncertainty. | Charter/Prompt remains lightweight and does not demand a roster, numeric estimates, Jira integration, new Delivery Unit or additional documentation. |

## Regression boundary

Validate separately that existing LEAP semantic routing still chooses Discovery, Pressure Test, Charter, Recon, Prompt and Validation appropriately. This estimation method must **not** create a new compulsory lifecycle phase, agent Skill, Jira integration or timekeeping function. AGENTS.md locked sections and managed markers must remain intact.

## QA reporting

Use **Pass / Fail / Not run**, with the actual executed agent/tool, revision and observed evidence. A documentation contract review alone is not an executed behavioral test. If native agent or Jira integration is unavailable, report those acceptance scenarios as **Not run** rather than assuming they pass.
