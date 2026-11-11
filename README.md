# Wikipedia Editing Standards

A platform-neutral AI skill that digests Wikipedia's rules on what may be written and how: neutrality, verifiability, no original research, notability, biographies of living people, copyright, reliable sources, style, citations, conduct, deletion, and how to audit a draft.

- Detailed rules are those of **English Wikipedia**. The skill first asks which edition or wiki you mean and, for other editions, applies only shared principles and tells you what to verify locally.
- English Wikipedia (2026) prohibits LLM-generated article content. This skill **explains, plans, audits and coaches human editors**; it does not write paste-ready articles and never invents citations.
- It is a digest of the core rules, not a copy of every page. Rules change, so check the live policy pages.

## Which file do I use?

| Platform | What to use | How |
|---|---|---|
| **Claude** (skills) | `skills/wikipedia-editing-standards/` | Zip the `wikipedia-editing-standards` folder (zip must contain `wikipedia-editing-standards/SKILL.md`) and upload it in Claude's skill settings. Or paste the full prompt into a Project's instructions. |
| **Claude Code, OpenCode, Pi and similar agents** | `.claude/skills/wikipedia-editing-standards/` | Copy the `.claude` folder into your project. |
| **ChatGPT** (plugin/skill upload) | `skills/` folder | Zip so the archive contains `skills/wikipedia-editing-standards/SKILL.md`, then upload. |
| **ChatGPT** (Custom GPT) | `universal/system-prompt-compact.txt` + `SKILL.md` | Paste the compact file into Instructions (about 8,000 character limit) and upload `SKILL.md` as a Knowledge file. |
| **Gemini** (Gem) | `universal/system-prompt-full.md` | Paste into the Gem's instructions. If rejected as too long, use the compact file. |
| **Kimi, DeepSeek, Mistral, Perplexity, others** | `universal/system-prompt-full.md` | Paste as the system prompt or custom instructions; use the compact file if there is a length limit. |
| **Any API or local model** | `universal/system-prompt-full.md` | Send as the `system` message. |
| **No custom instructions available** | `universal/system-prompt-compact.txt` | Paste at the start of a chat, then ask your question. |

Menu names change between apps; look for "custom instructions", "system prompt", "Gem", "GPT instructions" or "skills". The copies under `skills/` and `.claude/skills/` are identical; keep them in sync when editing.

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
