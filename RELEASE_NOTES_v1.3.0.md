## What's new in v1.3.0

**Live-rules protocol (the main change)**
- New section 0.1: when the AI can browse, it opens the live Wikipedia page before answering anything that depends on exact wording, numbers, criteria, deletion rules, AI rules or a decision you will act on, then says "checked live"
- Live text beats the built-in digest; page status (policy, guideline, essay, proposal) is checked
- When it cannot browse, it says the answer is from the built-in digest and names the page to check
- It no longer claims to know every rule, and never claims to have opened a page it did not

**Rule index**
- Section 16 rewritten as a grouped index of the main policy and guideline shortcuts, with the URL pattern for any shortcut
- New `rules-index.md` listing about 80 core pages

**Change detection**
- `tools/check_updates.py` fetches the latest revision of each core page (and, with `--listing`, every page in the official list), compares with the last run, and writes a change report with diff links; optional plain-text snapshots
- Weekly GitHub Action runs the script, updates the index and opens an issue when pages changed
- The script detects changes; it does not rewrite the skill

**Other**
- Compact prompt updated (7,948 characters) with the live-check rule
- `TESTING.md` tests 10-12 added; README rewritten for the flat layout

## Notes
- The script and Action were tested only against simulated API responses, not the live Wikipedia API. Run the Action once manually and check the result.
- English Wikipedia (2026) prohibits LLM-generated article content. This skill explains, plans, audits and coaches; it does not write paste-ready articles and never invents citations.
- Digest of core rules, not every page. Not yet tested on every AI platform.

**Full Changelog**: https://github.com/Lazywilin/wikipedia-editing-standards/compare/v1.2.1...v1.3.0
