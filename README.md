# Wikipedia Editing Standards

A platform-neutral AI skill that digests English Wikipedia's rules: neutrality, verifiability, no original research, notability, biographies of living people, copyright, reliable sources, style, citations, editor conduct and deletion.

## Files
- `SKILL.md`: the full skill
- `COMPACT_INSTRUCTIONS.txt`: a short version for platforms with instruction length limits
- `LICENSE`: MIT

## How to use
- **Claude:** upload as a skill, or paste `SKILL.md` into a Project
- **ChatGPT:** paste `COMPACT_INSTRUCTIONS.txt` into a Custom GPT's instructions and upload `SKILL.md` as a knowledge file
- **Gemini:** paste `SKILL.md` into a Gem
- **Kimi and others:** paste `SKILL.md` as the system prompt, or the compact file if there is a length limit

## Language editions
The detailed rules are those of **English Wikipedia**. Other language editions have their own policies. The skill asks which edition you mean and, for other editions, applies only the shared principles and tells you what to check on that edition's policy pages.

## AI-generated content
English Wikipedia (as of 2026) prohibits LLM-generated article content. This skill is built for explaining, planning, auditing and coaching human editors, not for generating paste-ready articles. It never fabricates citations.

## Limitations
This is a digest of the core rules, not a copy of every Wikipedia page. Rules change, so check the live policy pages for exact wording.

## Source
Derived from English Wikipedia project pages (CC BY-SA 4.0).
