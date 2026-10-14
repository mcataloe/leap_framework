#!/usr/bin/env python3
"""Dependency-free static LEAP router and Skill contract checks.

Usage:
    python tests/validate_semantic_router.py
    python tests/validate_semantic_router.py --agent-pack ../leap_agent_pack

This checks fixture integrity, metadata and local documentation, not native
automatic Skill invocation or semantic routing accuracy.
"""
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = {
    "help", "discovery", "pressure-test", "charter", "recon", "recon-lite",
    "prompt-generate", "prompt-execute", "lhs-generate", "lhs-execute",
    "governance", "cleanup", "validation", "handoff", "ordinary", "stop",
}
REQUIRED_FIELDS = {
    "id", "input", "expected_route", "mode", "mutation_policy",
    "disallowed_actions", "rationale",
}


def skill_metadata(file: Path) -> dict[str, str]:
    text = file.read_text(encoding="utf-8")
    assert text.startswith("---\n"), f"Skill missing YAML frontmatter: {file}"
    parts = text.split("---\n", 2)
    assert len(parts) == 3, f"Skill frontmatter is not closed: {file}"
    meta = {}
    for line in parts[1].splitlines():
        if not line.strip() or line.strip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        assert sep and key.strip() not in meta, f"Invalid or duplicate metadata: {line}"
        meta[key.strip()] = value.strip().strip('"').strip("'")
    assert re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", meta.get("name", "")), file
    assert 20 <= len(meta.get("description", "")) <= 1024, file
    return meta


def validate():
    cases = json.loads((ROOT / "tests/semantic-routing-cases.json").read_text(encoding="utf-8"))["cases"]
    assert len(cases) >= 30, "Need at least 30 evaluation cases"
    ids = [x["id"] for x in cases]
    assert len(set(ids)) == len(ids), "Duplicate case id"
    assert all(REQUIRED_FIELDS <= set(x) for x in cases)
    assert all(x["input"] and x["rationale"] and x["disallowed_actions"] for x in cases)
    assert REQUIRED <= {x["expected_route"] for x in cases}, "Insufficient route coverage"
    assert len([x for x in cases if x["mode"] == "semantic"]) >= 12
    assert len([x for x in cases if x["mode"] == "safety"]) >= 4
    assert all(x["mutation_policy"] != "unrestricted" for x in cases)
    assert not (ROOT / "SKILLS.md").exists(), "Root SKILLS.md must not be required"

    skill = ROOT / "skills/leap/SKILL.md"
    assert skill_metadata(skill)["name"] == "leap"
    router = (ROOT / "docs/semantic-routing.md").read_text(encoding="utf-8")
    for term in (
        "LEAP help", "LEAP Discovery", "LEAP Pressure Test", "Run LEAP Recon",
        "Generate LEAP Prompt", "Run LEAP Cleanup", "Run LEAP Validation",
        "Run LEAP Handoff", "Materiality Gate"
    ):
        assert term in router, f"Missing router catalog entry: {term}"
    assert (ROOT / "docs/user/leap-discovery.md").is_file()
    assert "No Gate never" in router, "Missing No Gate STOP guard"

    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-pack", type=Path, default=None)
    opts = parser.parse_args()
    if opts.agent_pack is not None:
        pack = opts.agent_pack.resolve()
        starter = pack / "templates/skills/project-skill-starter/SKILL.md"
        assert skill_metadata(starter)["name"] == "project-skill-starter"
        assert (pack / "docs/skills-installation.md").exists()
        for path in (
            "manifests/latest.json", "manifests/template-inventory.json",
            "manifests/compatibility.json",
        ):
            assert json.loads((pack / path).read_text(encoding="utf-8"))
        for path in (
            "templates/separated/global/AGENTS.md",
            "templates/separated/repo/AGENTS.md",
            "templates/combined/AGENTS.md",
        ):
            text = (pack / path).read_text(encoding="utf-8")
            assert "LEAP help" in text, f"Missing bootstrap help: {path}"
        for path in (
            "templates/separated/global/AGENTS.md",
            "templates/combined/AGENTS.md",
        ):
            text = (pack / path).read_text(encoding="utf-8")
            assert "Run LEAP Cleanup" in text, f"Missing cleanup command: {path}"
            assert text.count("LEAP_MANAGED_SECTION_BEGIN") <= 1
        print("Agent Pack static contract: PASS")
    print(f"Framework static contract: PASS ({len(cases)} evaluation specifications)")
    print("Native Codex/Claude automatic invocation: NOT TESTED by this script")


if __name__ == "__main__":
    validate()
