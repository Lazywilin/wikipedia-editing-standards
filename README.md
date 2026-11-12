# Wikipedia Editing Standards

A platform-neutral AI skill that digests Wikipedia's rules on what may be written and how: neutrality, verifiability, no original research, notability, biographies of living people, copyright, reliable sources, style, citations, conduct, deletion, and how to audit a draft.

- Detailed rules are those of **English Wikipedia**. The skill first asks which edition or wiki you mean and, for other editions, applies only shared principles and tells you what to verify locally.
- English Wikipedia (2026) prohibits LLM-generated article content. This skill **explains, plans, audits and coaches human editors**; it does not write paste-ready articles and never invents citations.
- It is a digest of the core rules, not a copy of every page. Rules change, so check the live policy pages.

## Files
- `SKILL.md`: the full skill (Claude skill format)
- `system-prompt-full.md`: the same content as plain text, without the skill header
- `system-prompt-compact.txt`: short version (about 7,700 characters) for platforms with instruction length limits
- `TESTING.md`: test prompts with expected behavior

## Which file do I use?

| Platform | What to use | How |
|---|---|---|
| **Claude** (skills) | `SKILL.md` | Put it in a folder named `wikipedia-editing-standards`, zip the folder, and upload it in Claude's skill settings. Or paste `system-prompt-full.md` into a Project's instructions. |
| **ChatGPT** (Custom GPT) | `system-prompt-compact.txt` + `SKILL.md` | Paste the compact file into Instructions (about 8,000 character limit) and upload `SKILL.md` as a Knowledge file. |
| **ChatGPT** (plugin/skill upload) | zip from the Releases page | Use the attached plugin zip, which has the `skills/wikipedia-editing-standards/SKILL.md` layout. |
| **Gemini** (Gem) | `system-prompt-full.md` | Paste into the Gem's instructions; use the compact file if it is too long. |
| **Kimi, DeepSeek, Mistral, Perplexity, others** | `system-prompt-full.md` | Paste as the system prompt or custom instructions; use the compact file if there is a length limit. |
| **Any API or local model** | `system-prompt-full.md` | Send as the `system` message. |
| **Claude Code, OpenCode, Pi** | `SKILL.md` | Place it at `.claude/skills/wikipedia-editing-standards/SKILL.md` in your project. |

Menu names change between apps; look for "custom instructions", "system prompt", "Gem", "GPT instructions" or "skills".

## What it can do
- Explain a rule and cite its shortcut (for example `WP:NPOV`)
- Assess notability and judge sources (independence, significance, churnalism and other traps)
- Audit a draft: BLP check first, claim-by-claim verdicts, prioritized findings
- Check categories, citations, style, conflicts of interest and deletion risk
- Handle other language editions honestly by flagging what differs

## Testing
See [TESTING.md](TESTING.md). Run at least two prompts on your platform before relying on it.

## Related projects
- [fuzheado/Wikipedia-AI-Skills](https://github.com/fuzheado/Wikipedia-AI-Skills): a much larger, MIT-licensed collection of skills for coding agents, focused on Wikimedia APIs, tooling and workflows. This project is the policy-and-rules counterpart and was informed by it.
- Meta-Wiki, "Artificial intelligence/Policies by project": community AI policies per Wikimedia project and language.

## License and source
MIT for this packaging. Derived from English Wikipedia project pages (CC BY-SA 4.0); see the attribution in `SKILL.md`.
