# Wikipedia Editing Standards

A platform-neutral AI skill that digests Wikipedia's rules on what may be written and how: neutrality, verifiability, no original research, notability, biographies of living people, copyright, reliable sources, style, citations, conduct and deletion.

- Detailed rules are those of **English Wikipedia**. The skill first asks which edition or wiki you mean and, for other editions, applies only shared principles and tells you what to verify locally.
- English Wikipedia (2026) prohibits LLM-generated article content. This skill **explains, plans, audits and coaches human editors**; it does not write paste-ready articles and never invents citations.
- It is a digest of the core rules, not a copy of every page. Rules change, so check live policy pages.

## Which file do I use?

| Platform | What to use | How |
|---|---|---|
| **Claude** (skills) | `skills/wikipedia-editing-standards/` | Zip the `wikipedia-editing-standards` folder (so the zip contains `wikipedia-editing-standards/SKILL.md`) and upload it in Claude's skill settings. Or paste the full prompt into a Project's instructions. |
| **ChatGPT** (plugin/skill upload) | `skills/` folder | Zip so the archive contains `skills/wikipedia-editing-standards/SKILL.md`, then upload. |
| **ChatGPT** (Custom GPT) | `universal/system-prompt-compact.txt` + `skills/.../SKILL.md` | Paste the compact file into Instructions (about 8,000 character limit) and upload `SKILL.md` as a Knowledge file. |
| **Gemini** (Gem) | `universal/system-prompt-full.md` | Paste into the Gem's instructions. If rejected as too long, use the compact file. |
| **Kimi, DeepSeek, Mistral, Perplexity, others** | `universal/system-prompt-full.md` | Paste as the system prompt or custom instructions. If rejected as too long, use the compact file. |
| **Any API or local model** | `universal/system-prompt-full.md` | Send as the `system` message. |
| **No custom instructions available** | `universal/system-prompt-compact.txt` | Paste at the start of a chat, then ask your question. |

Menu names change between apps; look for "custom instructions", "system prompt", "Gem", "GPT instructions" or "skills".

## Rule of thumb
- Fits and the platform supports files/skills: use the full version.
- Length error: use the compact version.
- Compact version is a summary, so it follows edge cases less precisely.

## Testing
See [TESTING.md](TESTING.md). Run at least two prompts on your platform before relying on it.

## License and source
MIT for this packaging. Derived from English Wikipedia project pages (CC BY-SA 4.0); see the attribution in `SKILL.md`.
