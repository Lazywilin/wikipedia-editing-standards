## What's new in v1.2.0

**Audit workflow**
- BLP check now comes first; serious violations are reported before anything else
- Claim-by-claim verdicts: confirmed, contradicted, npov_or, unverifiable, mixed
- Never marks a claim "confirmed" unless the source was actually read
- Prioritized findings (P0, P1, P2) and an optional machine-readable task list
- Structural checks: sections by article type, short-description demonyms, citation dumping, maintenance tags
- Audit is read-and-report only

**Notability**
- Step-by-step assessment procedure and verdict format
- Source-counting traps: churnalism, routine coverage, databases, primary documents, interviews, search hits
- Weak versus strong arguments for deletion discussions
- New rule: do not recite subject-specific criteria from memory; name the guideline and send the user to the live page

**Categories, citations, talk pages**
- Three category tests (verifiable, neutral, defining) plus overcategorization rules
- Citation hygiene: named-reference reuse, keep archive links, correct fields, honest gap flags
- Talk-page etiquette: strike instead of delete, closing templates, article vs user talk

**Packaging**
- Added `.claude/skills/` layout for Claude Code, OpenCode and Pi
- Frontmatter now includes license, compatibility and version metadata
- README credits and links the related project fuzheado/Wikipedia-AI-Skills
- Tests 7-9 added to `TESTING.md`

## Notes
- English Wikipedia (2026) prohibits LLM-generated article content. This skill explains, plans, audits and coaches; it does not write paste-ready articles and never invents citations.
- Digest of core rules, not every page. Check live policy pages for exact wording.
- Not yet tested on every platform; see `TESTING.md`.

**Full Changelog**: https://github.com/Lazywilin/wikipedia-editing-standards/compare/v1.1.0...v1.2.0
