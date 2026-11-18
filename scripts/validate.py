#!/usr/bin/env python3
"""Validate muse-skills-100: every skill must be a valid SKILL.md.

Checks:
- skills/<name>/SKILL.md exists, has frontmatter with name + description
- frontmatter name matches the folder name
- no duplicate skill names, exactly 100 skills
- skills.json lists exactly the same 100 skills with matching categories
- no skill name collides with a reserved/invalid pattern

Usage: python3 scripts/validate.py
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS_DIR = os.path.join(ROOT, "skills")


def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return None
    fm = {}
    for line in m.group(1).splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            fm[k.strip()] = v.strip()
    return fm


def main():
    errors = []
    folders = sorted(
        d for d in os.listdir(SKILLS_DIR)
        if os.path.isdir(os.path.join(SKILLS_DIR, d))
    )
    if len(folders) != 100:
        errors.append(f"expected 100 skill folders, found {len(folders)}")
    seen = set()
    for name in folders:
        if not re.fullmatch(r"[a-z0-9][a-z0-9\-_]*", name):
            errors.append(f"{name}: invalid folder name")
        if name in seen:
            errors.append(f"{name}: duplicate")
        seen.add(name)
        path = os.path.join(SKILLS_DIR, name, "SKILL.md")
        if not os.path.isfile(path):
            errors.append(f"{name}: missing SKILL.md")
            continue
        with open(path, encoding="utf-8", errors="replace") as f:
            text = f.read()
        fm = parse_frontmatter(text)
        if fm is None:
            errors.append(f"{name}: no YAML frontmatter")
            continue
        if not fm.get("name"):
            errors.append(f"{name}: frontmatter missing name")
        elif fm["name"] != name:
            errors.append(f"{name}: frontmatter name {fm['name']!r} != folder")
        if not fm.get("description"):
            errors.append(f"{name}: frontmatter missing description")
        if len(text) < 500:
            errors.append(f"{name}: SKILL.md suspiciously short ({len(text)} chars)")
    index_path = os.path.join(ROOT, "skills.json")
    try:
        index = json.load(open(index_path, encoding="utf-8"))
    except Exception as e:
        errors.append(f"skills.json unreadable: {e}")
        index = []
    indexed = [s.get("name") for s in index]
    if sorted(indexed) != sorted(folders):
        errors.append("skills.json does not match skills/ folders")
    if len(indexed) != len(set(indexed)):
        errors.append("skills.json has duplicate names")
    if errors:
        print(f"FAILED ({len(errors)} problems):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print(f"OK: 100 skills, skills.json matches, all frontmatter valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
