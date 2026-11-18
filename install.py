#!/usr/bin/env python3
"""Install muse-ai-skills into Muse as custom skills.

Usage (run from the cloned repo root):
    python3 install.py               # install all 100 skills
    python3 install.py --only nextjs-pro supabase-pro
    python3 install.py --list        # list the 100 skills, install nothing
    python3 install.py --dry-run     # show what would be installed
    python3 install.py --dest ~/workspace/custom-skills   # custom dest

How Muse uses it: paste this repo link into a chat with Muse and say
"install koro" / "install this". Muse clones the repo and runs this script.
No packages, no network, no code execution from skill files: it only copies
markdown files and writes a small skill.yaml per skill.

Install target is Muse's custom-skills directory
(~/workspace/custom-skills). Skills are installed with
include_in_prompt: false, so they do not flood every prompt; Muse finds
them with skill search when a task matches their description.
"""
import argparse
import os
import re
import shutil
import sys

REPO_ROOT = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(REPO_ROOT, "skills")
DEFAULT_DST = os.path.join(os.path.expanduser("~"), "workspace", "custom-skills")
SYSTEM_SKILLS = "/opt/muse/skills"


def parse_frontmatter(text):
    """Parse SKILL.md frontmatter without PyYAML (descriptions contain
    unquoted colons, so strict YAML parsing fails on many files)."""
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.DOTALL)
    if not m:
        return None, text
    fm = {}
    for line in m.group(1).splitlines():
        if ": " in line:
            k, v = line.split(": ", 1)
            fm[k.strip()] = v.strip()
        elif line.strip().endswith(":"):
            fm[line.strip()[:-1]] = ""
    return fm, m.group(2).lstrip("\n")


def yaml_quote(value):
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def install_one(src_dir, dest_root, dry_run=False):
    src_skill = os.path.join(src_dir, "SKILL.md")
    if not os.path.isfile(src_skill):
        return None, "no SKILL.md"
    with open(src_skill, encoding="utf-8", errors="replace") as f:
        text = f.read()
    fm, body = parse_frontmatter(text)
    if fm is None:
        return None, "no frontmatter"
    dirname = os.path.basename(src_dir)
    name = str(fm.get("name") or dirname).strip()
    desc = str(fm.get("description") or "").strip()
    category = str(fm.get("category") or "general").strip()
    if not re.fullmatch(r"[a-z0-9][a-z0-9\-_]*", name):
        return None, f"bad name {name!r}"
    title_m = re.search(r"^# (.+)$", body, re.MULTILINE)
    title = title_m.group(1).strip() if title_m else name.replace("-", " ").title()
    cat_title = category.replace("-", " ").title()
    dest_dir = os.path.join(dest_root, name)
    if dry_run:
        return name, None
    os.makedirs(dest_dir, exist_ok=True)
    for root, _dirs, files in os.walk(src_dir):
        rel = os.path.relpath(root, src_dir)
        for fn in files:
            if fn == "SKILL.md":
                continue
            s = os.path.join(root, fn)
            d = os.path.join(dest_dir, rel, fn) if rel != "." else os.path.join(dest_dir, fn)
            os.makedirs(os.path.dirname(d), exist_ok=True)
            shutil.copyfile(s, d)
    with open(os.path.join(dest_dir, "SKILL.md"), "w", encoding="utf-8") as f:
        f.write(body)
    yaml_text = (
        f"name: {yaml_quote(name)}\n"
        f"title: {yaml_quote(title)}\n"
        f"description: {yaml_quote(desc)}\n"
        f"category: {yaml_quote(cat_title)}\n"
        f"include_in_prompt: false\n"
    )
    with open(os.path.join(dest_dir, "skill.yaml"), "w", encoding="utf-8") as f:
        f.write(yaml_text)
    return name, None


def main():
    ap = argparse.ArgumentParser(description="Install muse-ai-skills into Muse.")
    ap.add_argument("--only", nargs="+", default=None, help="Install only these skills")
    ap.add_argument("--dest", default=DEFAULT_DST, help="Custom-skills directory")
    ap.add_argument("--list", action="store_true", help="List skills, install nothing")
    ap.add_argument("--dry-run", action="store_true", help="Show what would be installed")
    args = ap.parse_args()

    if not os.path.isdir(SRC):
        print(f"skills/ not found under {REPO_ROOT}. Run this from the repo root.")
        return 1
    names = sorted(os.listdir(SRC))
    if args.only:
        wanted = set(args.only)
        missing = sorted(wanted - set(names))
        if missing:
            print(f"not in this pack: {', '.join(missing)}")
            return 1
        names = [n for n in names if n in wanted]
    if args.list:
        for n in names:
            print(n)
        print(f"total: {len(names)} skills")
        return 0

    system_names = set(os.listdir(SYSTEM_SKILLS)) if os.path.isdir(SYSTEM_SKILLS) else set()
    installed, skipped_sys, failed = [], [], []
    for dirname in names:
        src_dir = os.path.join(SRC, dirname)
        if not os.path.isdir(src_dir):
            continue
        # Peek at the skill name to check system collision before installing.
        with open(os.path.join(src_dir, "SKILL.md"), encoding="utf-8", errors="replace") as f:
            fm, _ = parse_frontmatter(f.read())
        skill_name = str((fm or {}).get("name") or dirname).strip()
        if skill_name in system_names:
            skipped_sys.append(skill_name)
            continue
        name, err = install_one(src_dir, args.dest, dry_run=args.dry_run)
        if err:
            failed.append((dirname, err))
        elif name:
            installed.append(name)

    print(f"installed: {len(installed)}")
    if skipped_sys:
        print(f"skipped (built-in Muse skill already exists): {', '.join(skipped_sys)}")
    if failed:
        print(f"failed: {failed}")
    if args.dry_run:
        print("dry run only, nothing was written.")
    else:
        print(f"dest: {args.dest} ({len(os.listdir(args.dest))} skills total there now)")
        print("Done. Ask Muse about a topic and it will find the matching skill.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
