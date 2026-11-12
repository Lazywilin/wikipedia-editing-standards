# Wikipedia Editing Standards

A platform-neutral AI skill that digests Wikipedia's rules on what may be written and how: neutrality, verifiability, no original research, notability, biographies of living people, copyright, reliable sources, style, citations, conduct, deletion, and how to audit a draft.

**Honest scope:** this is a digest of the core rules, not a copy of every Wikipedia page, and no file can stay current by itself. The skill is built to **check the live pages first** when it can browse, and to say so plainly when it can't.

- Detailed rules are those of **English Wikipedia**. The skill first asks which edition or wiki you mean and, for other editions, applies only shared principles and tells you what to verify locally.
- English Wikipedia (2026) prohibits LLM-generated article content. This skill **explains, plans, audits and coaches human editors**; it does not write paste-ready articles and never invents citations.

## Files
- `SKILL.md`: the full skill (Claude skill format)
- `system-prompt-full.md`: the same content as plain text, without the skill header
- `system-prompt-compact.txt`: short version (about 7,900 characters) for platforms with instruction length limits
- `chatgpt/`: everything for ChatGPT (instructions, knowledge file, setup steps); copies kept in sync automatically
- `rules-index.md`: index of the main policy and guideline pages (updated automatically once the Action runs)
- `tools/check_updates.py`: script that detects when Wikipedia's rule pages change
- `.github/workflows/check-wikipedia-rules.yml`: weekly GitHub Action that runs the script
- `.github/workflows/sync-chatgpt-folder.yml`: keeps `chatgpt/` identical to the root files
- `TESTING.md`: test prompts with expected behavior

## Which file do I use?

| Platform | What to use | How |
|---|---|---|
| **Claude** (skills) | `SKILL.md` | Put it in a folder named `wikipedia-editing-standards`, zip the folder, and upload it in Claude's skill settings. Or paste `system-prompt-full.md` into a Project's instructions. |
| **ChatGPT** | `chatgpt/` folder | Follow `chatgpt/README.md`: paste `instructions.txt` into a Custom GPT, upload `SKILL.md` as Knowledge, turn on Web Search so the live check works. |
| **Gemini** (Gem) | `system-prompt-full.md` | Paste into the Gem's instructions; use the compact file if it is too long. |
| **Kimi, DeepSeek, Mistral, Perplexity, others** | `system-prompt-full.md` | Paste as the system prompt or custom instructions; use the compact file if there is a length limit. |
| **Any API or local model** | `system-prompt-full.md` | Send as the `system` message. |
| **Claude Code, OpenCode, Pi** | `SKILL.md` | Place it at `.claude/skills/wikipedia-editing-standards/SKILL.md` in your project. |

Menu names change between apps; look for "custom instructions", "system prompt", "Gem", "GPT instructions" or "skills".

## Live rules: how it stays current
1. **At answer time.** If the AI can browse, it opens the live Wikipedia page before answering anything that depends on exact wording, numbers, criteria or a decision you will act on, and says "checked live". If it can't browse, it says the answer comes from the built-in digest and tells you which page to check.
2. **At maintenance time.** `tools/check_updates.py` asks the MediaWiki API for the latest revision of about 80 core rule pages (and, with `--listing`, every page in the official list). It compares them with the last run and writes a change report with diff links. The weekly GitHub Action runs it and opens an issue when something changed. You then re-read those pages and update the digest. **The script detects changes; it does not rewrite the skill for you.**

### Running the checker yourself
```
python tools/check_updates.py --listing --write          # baseline or update; writes rules/revisions.json and rules-index.md
python tools/check_updates.py --listing                  # compare only
python tools/check_updates.py --snapshot snapshots       # also save plain-text copies of the pages
python tools/check_updates.py --report report.md         # save the change report
```
Needs Python 3.8+ and internet access. Exit code 10 means changes were found.

### Turning on the weekly Action
Repository **Settings → Actions → General → Workflow permissions**: choose **Read and write permissions** (needed by both workflows). Then open the **Actions** tab and run **Check Wikipedia rules for changes** once manually to create the baseline.

## Limits
- Not every rule is in the digest, and Wikipedia changes constantly.
- The script has been tested only against simulated API responses, not against the live Wikipedia API. Run it once and check the output.
- Other language editions have their own rules.
- Not tested on every AI platform; see `TESTING.md`.

## Testing
See [TESTING.md](TESTING.md). Run at least two prompts on your platform before relying on it.

## Related projects
- [fuzheado/Wikipedia-AI-Skills](https://github.com/fuzheado/Wikipedia-AI-Skills): a much larger, MIT-licensed collection of skills for coding agents, focused on Wikimedia APIs, tooling and workflows. This project is the policy-and-rules counterpart and was informed by it.
- Meta-Wiki, "Artificial intelligence/Policies by project": community AI policies per Wikimedia project and language.

## License and source
MIT for this packaging. Derived from English Wikipedia project pages (CC BY-SA 4.0); see the attribution in `SKILL.md`.
