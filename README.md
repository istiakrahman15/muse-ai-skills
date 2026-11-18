# Muse Skills 100

The 100 most useful Muse skills in one place — curated, tested, and installable in 30 seconds. No 2,000-skill maze, no dead skills, just the ones developers and everyday users actually ask for.

[![License: MIT](https://img.shields.io/github/license/istiakrahman15/muse-skills-100?style=flat-square&color=yellow)](LICENSE)
[![GitHub Stars](https://img.shields.io/github/stars/istiakrahman15/muse-skills-100?style=flat-square&logo=github)](https://github.com/istiakrahman15/muse-skills-100/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/istiakrahman15/muse-skills-100?style=flat-square&logo=github)](https://github.com/istiakrahman15/muse-skills-100/network/members)
[![Skills](https://img.shields.io/badge/Skills-100-blue?style=flat-square)](skills.json)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)](CONTRIBUTING.md)
[![Last Commit](https://img.shields.io/github/last-commit/istiakrahman15/muse-skills-100?style=flat-square)](https://github.com/istiakrahman15/muse-skills-100/commits/main)
[![Support Me](https://img.shields.io/badge/Support-Me-FF6B35?style=flat-square&logo=heart&logoColor=white)](https://www.supportkori.com/istiakrahman15)
[![Visitors](https://visitor-badge.laobi.icu/badge?page_id=istiakrahman15.muse-skills-100)](https://github.com/istiakrahman15/muse-skills-100)

A skill is a portable `SKILL.md` file that teaches Muse a reusable workflow: when to use it, what steps to follow, and what good output looks like. Install this pack once, and Muse finds the right skill whenever your task matches it.

> If this pack saved you even one hour, please consider supporting it. It is free for everyone, forever, and your support keeps it alive. See [Support this project](#support-this-project).

## Install in 30 seconds

Paste this link into a chat with Muse and say **install koro**:

```
https://github.com/istiakrahman15/muse-skills-100
```

Or copy-paste this exact message:

> Install the skills from https://github.com/istiakrahman15/muse-skills-100 — clone the repo and run install.py, then tell me how many skills were installed.

Muse clones the repo, runs `install.py`, and copies all 100 skills into its custom-skills folder. It will tell you the installed count when it is done. Nothing else to set up, no packages, no accounts.

Manual install, if you prefer:

```bash
git clone https://github.com/istiakrahman15/muse-skills-100.git
cd muse-skills-100
python3 install.py
```

Install only a few skills:

```bash
python3 install.py --only nextjs-pro supabase-pro tailwind-pro
python3 install.py --list        # see all 100 skill names
python3 install.py --dry-run     # preview without installing
```

### Install a single skill

Open `skills/<name>/SKILL.md` on GitHub, paste its content into a chat with Muse, and add: *"Please use this skill whenever I ask about \<topic\>. Remember it for our future conversations."*

## What's inside — 100 skills, 10 categories

| Category | Skills | Examples |
|---|---|---|
| Web Development | 10 | nextjs-pro, react-pro, tailwind-pro, typescript-pro, javascript-pro |
| Backend & APIs | 10 | nodejs-pro, express-pro, supabase-pro, auth-pro, graphql-pro |
| AI & Agents | 10 | ai-agents-pro, agents-pro, rag-pro, mcp-builder, langchain-pro |
| GitHub & DevOps | 10 | github-pro, github-actions-pro, git-pro, vercel-pro, docker-pro |
| Productivity | 10 | email-triage, calendar-pro, notion-pro, second-brain, task-manager |
| Everyday Assistant | 10 | daily-briefing, budget-checkin, meal-plan-generator, travel-day-planner |
| Business & Marketing | 10 | seo-specialist, content-strategist, copywriter, growth-hacker |
| Design & Creative | 10 | figma-expert, design-systems, ui-ux-designer, brand-identity |
| Data & Security | 10 | sql-pro, mongodb-pro, owasp-security, secrets-manager, devsecops-pro |
| Career & Learning | 10 | resume-writer, interview-coach, portfolio-builder, career-coach |

The full machine-readable list is [`skills.json`](skills.json). Every skill lives in `skills/<name>/SKILL.md` with `name` + `description` frontmatter, in the open Agent Skills format — so the same files work in any assistant that supports it.

Start with [`getting-started-with-muse-skills`](skills/getting-started-with-muse-skills/SKILL.md) if you are new to skills.

## Why 100, not 2,648?

Big catalogs list everything and help no one choose. This pack is a curated shortlist: the skills developers actually reach for — Next.js, React, Tailwind, Supabase, TypeScript, GitHub Actions, SEO, email triage, daily briefings — plus the everyday ones (budget, meals, travel, habits). Every entry was checked: it exists, its frontmatter is valid, and the installer was tested on all 100.

## Contributing

New skills and fixes are welcome. Please read [CONTRIBUTING.md](CONTRIBUTING.md) first — every submission must pass `scripts/validate.py`.

Ways to contribute:

- ✨ **Add a skill** — write an original `SKILL.md` following the format guide and open a PR.
- 🐛 **Fix or improve** an existing skill — corrections, clearer steps, better examples.
- 💡 **Suggest ideas** — open an issue describing a skill you'd like to see.
- ⭐ **Star the repo** — the simplest contribution of all; it helps others find the project.

## Support this project

Hi, I'm Istiak Rahman — a 19-year-old student from Bangladesh. I build all of this from my Android phone, late at night, because I don't have a PC. This pack is free for everyone, forever.

If it helped you, a small support means a lot — it goes directly into keeping these projects alive and building the next one:

[![Support Me](https://img.shields.io/badge/Support-Me-FF6B35?style=flat-square&logo=heart&logoColor=white)](https://www.supportkori.com/istiakrahman15)

**[Support on SupportKori →](https://www.supportkori.com/istiakrahman15)**

Starring the repo and sharing it with a developer friend also helps, and costs nothing.

## Our Sponsors

| Sponsor | |
|---|---|
| *No sponsors yet. Be the first one.* | [Become a sponsor](https://www.supportkori.com/istiakrahman15) |

To get listed here, support the project on [SupportKori](https://www.supportkori.com/istiakrahman15) or use the Sponsor button above, then open an issue or PR with your name and link.

## Credits & license

The 100 skills in this pack are curated from the open-source collection [aicodedecode/awesome-muse-skills](https://github.com/aicodedecode/awesome-muse-skills) (MIT license). The curation, installer, validation, and docs here are original work by Istiak Rahman. Each skill's source is linked in [`skills.json`](skills.json).

This repo is released under the [MIT License](LICENSE). This is an unofficial community project. It is not affiliated with, endorsed by, or sponsored by Meta. "Muse" is a trademark of Meta Platforms, Inc.
