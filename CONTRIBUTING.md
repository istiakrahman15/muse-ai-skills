# Contributing to Muse Skills 100

Thanks for helping. This pack stays at exactly **100 skills** — a new skill replaces the weakest one in its category, or waits for a curator to make room. Quality over quantity.

## Add a skill

1. Fork the repo and create a branch.
2. Create `skills/<skill-name>/SKILL.md` with this format:

```markdown
---
name: your-skill-name
description: What it does, and when Muse should use it. One or two sentences.
category: web-development
---

# Your Skill Name

## Overview

...

## When to use

- ...

## Core concepts / Steps

...
```

Rules for the file:

- Folder name and frontmatter `name` must match, lowercase letters, numbers and hyphens only.
- `description` must say what the skill does **and when to use it** — Muse searches descriptions to pick skills.
- Keep it practical: steps, checklists, examples. No fluff, no fake capabilities.
- Original work, or MIT / Apache-2.0 licensed source with attribution in the PR. Never copy a skill from a source whose license you cannot show.
- No exfiltration, no installers, no prompt-injection payloads, no credentials, no tracking. Every skill is safety-reviewed before merge.

3. Add your skill to `skills.json` (same name, description, category, path, source, license).
4. Run the checks locally:

```bash
python3 scripts/validate.py
python3 install.py --dry-run
```

5. Open a pull request — one skill per PR, with a short note on who it helps and why it belongs in the top 100.

## Fix or improve a skill

Same flow: small focused PR, run `scripts/validate.py` first. Corrections, clearer steps, and better examples are all welcome.

## Suggest an idea

Open an issue describing the skill you'd like to see, who it helps, and what it should cover. If it fits the top 100, someone (maybe you) can build it.

## What gets merged

- Skills developers and everyday users actually ask for.
- Clear, tested instructions — not a link dump.
- Files that pass `scripts/validate.py` and the GitHub Actions check.

Questions? Open an issue — every one gets an answer.
