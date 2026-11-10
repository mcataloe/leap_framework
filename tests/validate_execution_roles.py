#!/usr/bin/env python3
"""Static LEAP execution-role contract checks.

Usage:
    python tests/validate_execution_roles.py
    python tests/validate_execution_roles.py --agent-pack ../leap_agent_pack

This validates documentation and expected-case integrity, NOT native assistant
behavior, real review independence, live permission boundaries or handoffs.
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_MODES = {"single", "coordination", "review", "handoff", "safety", "evidence", "learning"}
REQUIRED_CASE_FIELDS = {
    "id", "mode", "setup", "action", "expected", "disallowed",
    "evidence_to_record", "observed_status",
}


def read(path: Path) -> str:
    assert path.is_file(), f"Missing required file: {path}"
    return path.read_text(encoding="utf-8")


def validate_framework() -> int:
    doc = read(ROOT / "docs/agent-execution-roles.md")
    for marker in (
        "LEAP_DOC_METADATA:", "Default to a single agent",
        "Architect / coordinator", "Implementor", "Reviewer", "Human approver",
        "Materiality Gate", "source-of-truth", "Execution verified",
        "human approval", "independent review",
    ):
        assert marker.lower() in doc.lower(), f"Missing role contract marker: {marker}"

    linked = {
        ROOT / "docs/agent-profiles.md": "agent-execution-roles.md",
        ROOT / "docs/README.md": "agent-execution-roles.md",
        ROOT / "templates/leap-prompt-template.md": "../docs/agent-execution-roles.md",
    }
    for path, target in linked.items():
        assert target in read(path), f"Missing optional role reference: {path}"

    payload = json.loads(read(ROOT / "tests/execution-role-cases.json"))
    assert payload["version"] == 1
    assert payload["source_contract"] == "docs/agent-execution-roles.md"
    cases = payload["cases"]
    assert len(cases) >= 12, "Insufficient behavioral scenario coverage"
    ids = [case["id"] for case in cases]
    assert len(ids) == len(set(ids)), "Duplicate behavioral case id"
    assert REQUIRED_MODES <= {case["mode"] for case in cases}, "Missing role scenario category"
    for case in cases:
        assert REQUIRED_CASE_FIELDS <= set(case), f"Malformed scenario: {case.get('id')}"
        assert all(isinstance(case[k], str) and case[k].strip()
                   for k in ("id", "mode", "setup", "action", "expected"))
        assert isinstance(case["disallowed"], list) and case["disallowed"]
        assert isinstance(case["evidence_to_record"], list) and case["evidence_to_record"]
        assert case["observed_status"] == "not_tested", (
            "Evaluation specifications must not claim observed runtime passes"
        )
    return len(cases)


def validate_agent_pack(root: Path) -> None:
    paths = (
        "templates/execution/architect.md",
        "templates/execution/implementor.md",
        "templates/execution/reviewer.md",
        "templates/execution/context-manifest.example.yaml",
        "templates/execution/active-handoff.md",
        "templates/execution/implementation-report.md",
        "templates/execution/independent-review.md",
        "templates/execution/lesson-candidate.md",
        "docs/optional-execution-roles.md",
        "docs/execution-continuity.md",
    )
    for name in paths:
        read(root / name)
    manifest = read(root / "templates/execution/context-manifest.example.yaml")
    assert "enabled: false" in manifest, "Example context manifest must remain opt-in"
    for role in ("architect", "implementor", "reviewer"):
        assert f"{role}: \"templates/execution/{role}.md\"" in manifest, (
            f"Missing manifest role reference: {role}"
        )
    assert "do not" in read(root / "docs/execution-continuity.md").lower(), (
        "Continuity guide must preserve restrictions"
    )


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-pack", type=Path, default=None)
    args = parser.parse_args()
    case_count = validate_framework()
    print(f"Framework role contract static checks: PASS ({case_count} expected cases)")
    if args.agent_pack:
        validate_agent_pack(args.agent_pack.resolve())
        print("Agent Pack optional template static checks: PASS")
    print("Native agent behavioral acceptance: NOT TESTED by this script")


if __name__ == "__main__":
    main()
