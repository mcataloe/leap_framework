# LEAP Discovery and Pressure Test

Use Discovery to **understand and define** a domain or problem before deciding whether or how to build. Use Pressure Test to **challenge a candidate hypothesis or design**. Both reuse the existing Charter Ideation Loop and Materiality Gate; neither is another mandatory lifecycle phase.

## Invocation

- "Run LEAP Discovery on our integration model."
- "Help me explore who owns application findings in this project."
- "LEAP Pressure Test: would canonical vulnerability IDs lose vendor semantics?"

## LEAP Discovery (non-mutating by default)

1. Preserve the user's initial words and project scope. Inspect already accessible domain and repository evidence without guessing.
2. Explore the actors, goals, domain language, boundaries, entity relationships, workflows, exceptional cases, user experience and possible solution space.
3. Separate Known / Assumed / Unknown / Contested / Needs Decision. Ask short, cohesive rounds of useful domain questions. The questions may broaden understanding rather than unblock coding; do not force an artificial minimum number of rounds.
4. Apply the Materiality Gate to decisions that affect safety, scope and the next action. Avoid polishing questions that have no effect.
5. End when the user has enough domain definition to choose a next step or when additional questions stop changing the brief.
6. Deliver a concise Domain / Concept Brief: original intent; problem; actors; terminology; entities and relationships; workflows and exceptions; options; non-goals; constraints; known/assumed/unknown; candidate success event; recommended route.

Do not automatically create a repository file, Charter, Recon, architecture, or Prompt. Discovery can end with "no build justified".

## LEAP Pressure Test (non-mutating by default)

1. State the specific hypothesis/proposal and baseline assumptions.
2. Examine benefits, weak points, edge cases, competing alternatives, reversibility, cost and operational implications.
3. Define the strongest falsifier and what new evidence would change the conclusion.
4. When project implementation evidence is required, route to focused Recon instead of asserting speculation as repo fact.
5. Return a disposition: proceed, revise, investigate with Recon, defer, or reject, with relevant assumptions and confidence.

Pressure Test can occur inside Discovery or Charter without changing the workflow name or requiring another approval cycle.

See [Semantic Workflow Routing](../semantic-routing.md), [Charter](../leap-charter.md), and [Materiality Gate](../materiality-gate.md).
