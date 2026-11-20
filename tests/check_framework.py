#!/usr/bin/env python3
"""Static checks for the LEAP Framework repository. Standard library only.

Usage:
    python3 tests/check_framework.py
    python3 tests/check_framework.py --agent-pack ../leap_agent_pack

Checks:
  - relative Markdown links and anchors resolve
  - docs/leap-core.md has the LEAP Core text markers and stays within budget
  - AGENTS.md managed section carries the current LEAP Core text
  - define-once guard: the multi-line planning hierarchy block appears only in
    the canonical files listed in HIERARCHY_ALLOWED
  - with --agent-pack: the pack's global and combined templates embed the same
    LEAP Core text
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CORE_MAX_WORDS = 650
HIERARCHY_ALLOWED = {
    "docs/project-documentation-model.md",
    "docs/maintainer/project-documentation-migration.md",
    "CHANGELOG.md",
}
HIERARCHY_BLOCK = re.compile(r"Strategic Outcome\s*\n\s*(?:↓|->)", re.M)
CORE_MARKERS = re.compile(r"<!-- LEAP_CORE_TEXT_BEGIN -->(.*?)<!-- LEAP_CORE_TEXT_END -->", re.S)
MANAGED = re.compile(r"<!-- LEAP_MANAGED_SECTION_BEGIN -->(.*?)<!-- LEAP_MANAGED_SECTION_END -->", re.S)

errors: list[str] = []


def fail(msg: str) -> None:
    errors.append(msg)


def words(text: str) -> int:
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.S)
    return len(re.findall(r"[A-Za-z0-9][\w'’.-]*", text))


def core_from_managed(text: str) -> str | None:
    m = MANAGED.search(text)
    if not m:
        return None
    body = m.group(1)
    idx = body.find("## Purpose")
    return body[idx:].strip() if idx >= 0 else None


def slug(heading: str) -> str:
    s = heading.strip().lower()
    s = re.sub(r"[^\w\- ]", "", s)
    return s.replace(" ", "-")


def anchors(path: Path) -> set[str]:
    found, seen, in_code = set(), {}, False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.lstrip().startswith(("```", "~~~")):
            in_code = not in_code
            continue
        m = None if in_code else re.match(r"#{1,6}\s+(.*)", line)
        if m:
            base = slug(m.group(1))
            n = seen.get(base, 0)
            seen[base] = n + 1
            found.add(base if n == 0 else f"{base}-{n}")
    return found


def markdown_files() -> list[Path]:
    return sorted(p for p in ROOT.rglob("*.md") if ".git" not in p.parts)


def check_links() -> None:
    for md in markdown_files():
        text = re.sub(r"(```|~~~).*?\1", "", md.read_text(encoding="utf-8"), flags=re.S)
        text = re.sub(r"`[^`\n]*`", "", text)
        for target in re.findall(r"\]\(<?([^)\s>]+)>?\)", text):
            if re.match(r"[a-z]+:", target):
                continue
            file_part, _, frag = target.partition("#")
            dest = (md.parent / file_part).resolve() if file_part else md
            rel = md.relative_to(ROOT).as_posix()
            if not dest.exists():
                fail(f"{rel}: broken link -> {target}")
            elif frag and dest.suffix == ".md" and frag not in anchors(dest):
                fail(f"{rel}: missing anchor -> {target}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--agent-pack", type=Path, help="path to a leap_agent_pack checkout")
    args = parser.parse_args()

    check_links()

    core_doc = (ROOT / "docs/leap-core.md").read_text(encoding="utf-8")
    m = CORE_MARKERS.search(core_doc)
    core = m.group(1).strip() if m else ""
    if not core:
        fail("docs/leap-core.md: LEAP_CORE_TEXT markers missing or empty")
    elif words(core) > CORE_MAX_WORDS:
        fail(f"docs/leap-core.md: LEAP Core is {words(core)} words (> {CORE_MAX_WORDS})")

    agents_core = core_from_managed((ROOT / "AGENTS.md").read_text(encoding="utf-8"))
    if agents_core != core:
        fail("AGENTS.md: managed section does not match docs/leap-core.md")

    for md in markdown_files():
        rel = md.relative_to(ROOT).as_posix()
        if rel not in HIERARCHY_ALLOWED and HIERARCHY_BLOCK.search(md.read_text(encoding="utf-8")):
            fail(f"{rel}: restates the planning hierarchy block; link to docs/project-documentation-model.md instead")

    if args.agent_pack:
        for tpl in ("templates/separated/global/AGENTS.md", "templates/combined/AGENTS.md"):
            path = args.agent_pack / tpl
            if not path.is_file():
                fail(f"agent pack: missing {tpl}")
            elif core_from_managed(path.read_text(encoding="utf-8")) != core:
                fail(f"agent pack: {tpl} LEAP Core differs from docs/leap-core.md")

    if errors:
        print("\n".join(f"FAIL {e}" for e in errors))
        print(f"\n{len(errors)} problem(s)")
        return 1
    print(f"LEAP Framework: PASS (LEAP Core {words(core)} words"
          + (", Agent Pack in sync" if args.agent_pack else "") + ")")
    return 0


if __name__ == "__main__":
    sys.exit(main())
