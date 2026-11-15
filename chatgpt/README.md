# ChatGPT setup

Everything ChatGPT needs is in this folder.

| File | Use |
|---|---|
| `instructions.txt` | Paste into a Custom GPT's **Instructions** box (about 8,000 character limit; this file is under it) |
| `knowledge.md` | Upload as a **Knowledge** file (the full skill, as plain text) |

These are automatic copies of `system-prompt-compact.txt` and `system-prompt-full.md` from the repo root, refreshed by the **Sync ChatGPT folder** GitHub Action. Edit the root files, not these.

## Custom GPT (recommended)
1. In ChatGPT, create a new GPT (look for "Explore GPTs" then "Create", or "My GPTs"; menu names change).
2. Open `instructions.txt`, copy everything, and paste it into **Instructions**. If it is rejected as too long, check the character count the box shows.
3. Under **Knowledge**, upload `knowledge.md`.
4. Under **Capabilities**, turn on **Web Search**. Without it the GPT cannot check live Wikipedia pages and will say its answers come from the built-in digest.
5. Save, then run the prompts in `../TESTING.md` (tests 1, 3, 10, 11, 12, 13 are the most useful on ChatGPT).

## ChatGPT plugin / skill upload (not verified)
ChatGPT's upload has been reported to expect `skills/<name>/SKILL.md` inside the archive. To try it, make a zip containing only `skills/wikipedia-editing-standards/SKILL.md` (copy the root `SKILL.md` into that path). Do not upload this whole repo: a skill must contain exactly one `SKILL.md`.

## Notes
- Detailed rules are English Wikipedia's; the skill asks which edition you mean.
- English Wikipedia's AI guideline (WP:NEWLLM) prohibits using LLMs to generate or rewrite article content, with narrow exceptions, so this assistant explains, plans, audits and coaches; it does not write or rewrite article text.
