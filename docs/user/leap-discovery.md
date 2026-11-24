# LEAP Discovery and Pressure Test

Use Discovery to **understand and define** a domain or problem before deciding whether or how to build. Use Pressure Test to **challenge a candidate hypothesis or design**. Both reuse the existing Charter Ideation Loop and Materiality Gate; neither is another mandatory lifecycle phase.

## Invocation

- "Run LEAP Discovery on our integration model."
- "Help me explore who owns application findings in this project."
- "LEAP Pressure Test: would canonical vulnerability IDs lose vendor semantics?"

## LEAP Discovery (non-mutating by default)

1. Preserve the user's initial words and project scope. Inspect already accessible domain and repository evidence without guessing.
2. Explore the actors, goals, domain language, boundaries, entity relationships, workflows, exceptional cases, user experience and possible solution space.
3. Separate Known / Assumed / Unknown / Contested / Needs Decision. Ask short, cohesive rounds of useful domain questions, formatted as in [Presenting choices](#presenting-choices). The questions may broaden understanding rather than unblock coding; do not force an artificial minimum number of rounds.
4. Apply the [Materiality Gate](../materiality-gate.md) to every question before asking it: inspect approved sources, classify, then ask, assume and disclose, or stop, and re-evaluate after each answer. Ask only questions whose answers could change scope, risk, the recommendation or the next action; do not ask polishing questions. No Gate never overrides a stop.
5. Run the [pre-return QA pass](#pre-return-qa-pass) on every question round and on the final brief before returning it.
6. End when the user has enough domain definition to choose a next step or when additional questions stop changing the brief.
7. Deliver a concise Domain / Concept Brief: original intent; problem; actors; terminology; entities and relationships; workflows and exceptions; options; non-goals; constraints; known/assumed/unknown; candidate success event; recommended route.

Do not automatically create a repository file, Charter, Recon, architecture, or Prompt. Discovery can end with "no build justified".

### Presenting choices

When a Discovery question offers choices, let the user weigh the options before seeing the agent's view, so the recommendation informs the decision without anchoring it.

- Number each question. Under it, list lettered options. Word them neutrally and at comparable depth, and give each its own basis. Put no recommendation markers, "preferred" labels, or attribution of who proposed an option inside the list. A combined or staged path is its own lettered option.
- Directly after that question's options, add one `Recommended:` line naming a lettered option, with its rationale and the consideration most likely to reverse it. Stay within that question's domain: compare only its own options, and do not anticipate other questions. When the evidence supports no option, write `Recommended: none` and say what would settle it.
- Never place a recommendation before or among the options.

Layout, where the output renders Markdown:

- Put the question in bold. Indent each option as a list item that starts with its bold letter, and leave a blank line between options.
- After the last option, put the recommendation in a quote block, in italics with a bold label: one paragraph for `Recommended:` and one for `Would reverse it:`.
- Separate questions with a horizontal rule.

Where Markdown does not render, keep the same order: indented lettered options, then the `Recommended:` and `Would reverse it:` lines.

```markdown
**1. Where should session state live?**

  - **a.** In-process memory, because it is fastest and needs no new infrastructure.

  - **b.** A managed cache, because it survives restarts and scales across instances.

  - **c.** A database table, because it reuses existing storage and backups.

  - **d.** Start with the database table, then move to a managed cache if latency targets are missed.

> _**Recommended: d.** It needs no new infrastructure now and leaves a staged path if load grows._
>
> _**Would reverse it:** a latency target the database cannot meet at launch._

---

**2. Who owns session expiry rules?**

  - **a.** ...
```

### Pre-return QA pass

Before returning a question round or the final brief, check it against this list and fix anything that fails. If a check cannot be completed, say so in the output instead of implying it passed.

1. **Evidence:** every claim about current state cites its source or is marked assumed or unknown. Nothing claims a source was read that was not.
2. **Materiality:** each question passed the Materiality Gate. Discoverable items were inspected rather than asked, consequential assumptions are disclosed, and hard stops are stated.
3. **Choices:** options and recommendations follow [Presenting choices](#presenting-choices).
4. **Separation:** Known, Assumed, Unknown, Contested and Needs Decision stay distinct.
5. **Boundaries:** nothing was changed, and no approval, owner, date or decision was invented.
6. **Brief (final round only):** each element in step 7 is present or omitted because it does not apply.

This self-check does not replace an independent review where one is required; see [Agent execution roles](../agent-execution-roles.md).

## LEAP Pressure Test (non-mutating by default)

1. State the specific hypothesis/proposal and baseline assumptions.
2. Examine benefits, weak points, edge cases, competing alternatives, reversibility, cost and operational implications.
3. Define the strongest falsifier and what new evidence would change the conclusion.
4. When project implementation evidence is required, route to focused Recon instead of asserting speculation as repo fact.
5. Return a disposition: proceed, revise, investigate with Recon, defer, or reject, with relevant assumptions and confidence.

Pressure Test can occur inside Discovery or Charter without changing the workflow name or requiring another approval cycle.

See [Semantic Workflow Routing](../semantic-routing.md), [Charter](../leap-charter.md), and [Materiality Gate](../materiality-gate.md).
