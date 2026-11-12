# ChatGPT setup

Everything ChatGPT needs is in this folder.

| File | Use |
|---|---|
| `instructions.txt` | Paste into a Custom GPT's **Instructions** box (about 8,000 character limit; this file is under it) |
| `skills/wikipedia-editing-standards/SKILL.md` | Upload as a **Knowledge** file, or use the `skills` folder for plugin/skill upload |

These are automatic copies of `SKILL.md` and `system-prompt-compact.txt` from the repo root, refreshed by the **Sync ChatGPT folder** GitHub Action. Edit the root files, not these.

## Option A: Custom GPT (recommended)
1. In ChatGPT, create a new GPT (look for "Explore GPTs" then "Create", or "My GPTs"; menu names change).
2. Open `instructions.txt`, copy everything, and paste it into **Instructions**. If it is rejected as too long, tell me the character count the box shows.
3. Under **Knowledge**, upload `skills/wikipedia-editing-standards/SKILL.md`.
4. Under **Capabilities**, turn on **Web Search**. Without it the GPT cannot check live Wikipedia pages and will say its answers come from the built-in digest.
5. Save, then run the prompts in `../TESTING.md` (tests 1, 3, 10, 11, 12 are the most useful on ChatGPT).

## Option B: plugin / skill upload
ChatGPT's upload expects an archive with `skills/<name>/SKILL.md` inside. To make one from this folder, zip the **`skills`** folder (so the zip contains `skills/wikipedia-editing-standards/SKILL.md`) and upload it. This path has not been verified to work; if ChatGPT rejects it, paste its exact error message into an issue.

## Notes
- Detailed rules are English Wikipedia's; the skill asks which edition you mean.
- English Wikipedia (2026) prohibits LLM-generated article content, so this assistant explains, plans, audits and coaches; it does not write paste-ready articles.
