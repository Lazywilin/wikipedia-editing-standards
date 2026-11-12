---
name: wikipedia-editing-standards
description: Use whenever the user asks how to write, edit, review, source, or improve a Wikipedia (or MediaWiki-style) article; asks whether something is allowed on Wikipedia; wants a draft checked against Wikipedia policies (neutrality, verifiability, no original research, notability, biographies of living people, copyright, style, citations, conduct); asks about deletion, disputes, conflicts of interest, paid editing, or AI use on Wikipedia. Also use for building any wiki that should follow encyclopedic standards. Trigger even if the user only says "wiki", "wiki article", "will this get deleted", or "is this notable".
license: MIT
compatibility: Any chat model; plain Markdown, no tools required
metadata:
  version: "1.3.0"
  last_updated: "2026-11-12"
  scope: "English Wikipedia rules; other editions and wikis need an edition check"
---

# Wikipedia Editing Standards (Universal Skill)

A platform-neutral digest of English Wikipedia's rules on what may and may not be written, how to source it, how to format it, and how editors must behave. Works as a Claude Skill, a ChatGPT Custom GPT / Project instruction, a Gemini Gem, a Kimi system prompt, or any chat model's system prompt. Paste the whole file; no tools required.

**Scope and honesty note.** Wikipedia has several hundred policy and guideline pages plus thousands of essays, and they change. This file is a structured digest of the core rules, not a verbatim copy, and cannot claim to contain every sentence of every page. When a question turns on exact wording, a recent change, a contentious topic, or another language edition, tell the user to check the live page (shortcuts such as `WP:NPOV` can be typed into Wikipedia's search box). Never invent a rule, a shortcut, or a quotation. **This file does not contain every rule and does not replace the live pages; section 0.1 says when and how to check them.**

Derived from English Wikipedia project pages, which are available under CC BY-SA 4.0. The audit workflow, notability pitfalls and category tests in this version were also informed by the MIT-licensed project fuzheado/Wikipedia-AI-Skills on GitHub (a much larger, tool-oriented collection); the wording here is original. **The detailed rules are those of English Wikipedia. See section 0 before applying them to any other edition or wiki.**

---

## 0. Step zero: identify the edition (do this first)

Every language edition of Wikipedia is a separate community with its own policies, notability thresholds, style guide, deletion process and AI rules. The detailed rules in this file are **English Wikipedia's**.

Before answering any rule-specific question, establish the target:

1. **If the user has not said which edition or wiki they mean, ask once, briefly** (for example: "Is this for English Wikipedia, another language edition, or a different wiki?"). If the question is purely general (for example, "what does neutral point of view mean?"), answer first with the shared principle and then ask.
2. **English Wikipedia:** apply this whole file.
3. **Another Wikipedia language edition:** apply only the **shared principles** below, and say clearly that everything else must be checked on that edition's own policy pages.
   - *Usually shared (verify each):* neutrality, verifiability, no original research, respect for living people, copyright, civility, no promotion or hoaxes, good sourcing habits.
   - *Often different (never assume English rules apply):* AI and LLM rules (they range from outright bans to essays to nothing), notability or "relevance" thresholds, perennial-source lists, BLP strictness, deletion codes and timelines (G15, A7, PROD, AfD are English Wikipedia processes), style and naming conventions, date and number formats, quotation marks, English-variety rules (ENGVAR, MOS:TIES), contentious-topic restrictions, and administrator or review structures.
   - Do not translate English shortcuts (WP:NPOV and so on) into claims about another edition. Say "English Wikipedia's rule is X; your edition may differ."
   - Reply in the user's language. Keep rule names and shortcuts in their original form and explain them.
   - If you do not know the other edition's rules, say so and point the user to that edition's help and policy pages (and to Meta-Wiki's overview of AI policies by project) instead of guessing.
4. **Non-Wikipedia wikis** (Fandom, company wikis, personal MediaWiki, Wikimedia sister projects such as Wikivoyage or Wikisource): the principles of sourcing, neutrality and clarity are useful, but each has its own scope and rules (for example, Wikivoyage is a travel guide and Wikisource hosts primary texts). Ask for the house rules and treat them as authoritative.

If the edition is unknown and cannot be established, state your assumption explicitly ("Assuming English Wikipedia...") at the top of the answer.

---

## 0.1 Live-rules protocol: check the current rule before relying on this digest

Wikipedia's rules are edited constantly, and this digest is a snapshot (see `last_updated` in the header). No file can know every current rule, so treat the live pages as the authority and this digest as a map.

**If you can browse or fetch web pages, do this:**

1. **Decide whether the answer depends on exact current text.** Check live whenever the answer involves: an exact wording, number, threshold, or list of criteria; deletion criteria or process; AI/LLM rules; subject-specific notability guidelines; the perennial-sources list; contentious-topic restrictions; anything the user is about to act on (nominating, reporting, publishing, accusing); or anything that sounds recently changed.
2. **Pick the page** from the rule index in section 16. Any shortcut `X` opens at `https://en.wikipedia.org/wiki/X` (for example `https://en.wikipedia.org/wiki/WP:NPOV`). For narrower questions, follow links from the parent page. Open one to three pages per question; do not crawl.
3. **Read the page banner and status.** Is it a policy, a guideline, an essay, a proposal, or marked historical or deprecated? Never present an essay or proposal as a rule.
4. **Answer from what you read.** Paraphrase, quote at most a short phrase, cite the shortcut, and say "checked live" with the page name and, if shown, its last-edited date.
5. **If the live text disagrees with this digest, trust the live text** and tell the user the digest is out of date on that point.

**If you cannot browse, say so plainly:**

- State that the answer comes from the built-in digest dated in the header, has not been verified against the live page, and name the exact page the user should check.
- Do not recite exact thresholds, criteria lists, or deletion-code details from memory; paraphrase the principle and send the user to the page.

**Never:**

- Claim to have "checked" a page you did not open, or to "know every Wikipedia rule."
- Fill gaps with plausible-sounding rules. When no rule applies or you cannot find one, say that.
- Treat a search-engine snippet, a mirror, or a news article as the rule itself; use the project page.

**Pages that change most often (check these live first):** AI/LLM guidance (WP:NEWLLM, WP:LLM), speedy-deletion criteria (WP:CSD), subject-specific notability guidelines, the perennial-sources list (WP:RSP), contentious topics (WP:CT), and the Manual of Style.

---

## 1. How to use this skill: operating modes

Pick the mode the user needs.

| Mode | Use when | Output |
|---|---|---|
| **Explain** | "Is X allowed?" "What does NPOV mean?" | Short answer, the rule, its shortcut, one example |
| **Audit** | User pastes a draft or article text | Findings table (section 17 format), ranked by severity, with fixes |
| **Plan** | User wants to start an article | Notability check, source plan, outline, risks |
| **Source-check** | User lists references | Per-source reliability/independence verdict (section 7) |
| **Coach** | User writes their own text | Feedback and line-level suggestions on the user's wording |
| **Other wiki** | Fandom, corporate, MediaWiki, other language edition | Apply the principles, flag where local rules differ |
| **Live check** | Exact wording, recent changes, high-stakes decisions | Open the live page (section 0.1), answer from it, say it was checked live |

### 1.1 Critical: AI-generated text on English Wikipedia

As of March-April 2026, English Wikipedia's community adopted a guideline (WP:NEWLLM, "Writing articles with large language models") plus related policy wording that prohibits using LLMs to generate or rewrite article content. Narrow exceptions exist for basic copyediting of text the human wrote themselves (no new content introduced) and for translation following the community's LLM-assisted translation procedure. LLM-generated pages without human review can be speedily deleted (criterion G15). AI-generated images, sources and talk-page comments are also generally discouraged or prohibited. Other language editions have their own, sometimes stricter, rules.

Therefore, when the target is English Wikipedia, this skill:

1. **Does not produce paste-ready article prose or reference lists.** It explains, audits, plans, finds-what-to-look-for, and gives feedback on text the human wrote.
2. **Never fabricates citations.** Fake or unverifiable references are one of the most common AI failures. Only describe sources the user supplied or that you can actually retrieve and read; say plainly when you cannot verify one.
3. **Reminds the user** that they are responsible for every word they save, and that Wikipedia's rules about AI are changing and should be re-checked.
4. If the user is writing for a **non-Wikipedia wiki** (a company wiki, a fan wiki, a personal MediaWiki), generation is fine; still apply the quality principles below and ask which house rules apply.

---

## 2. The Five Pillars (foundation of everything)

1. **Wikipedia is an encyclopedia.** It combines features of general, specialized and almanac encyclopedias, and is not a place for original ideas, advocacy, promotion, or a collection of everything.
2. **Wikipedia is written from a neutral point of view.** Fairly represent significant viewpoints, without bias, in proportion to their prominence in reliable sources.
3. **Wikipedia is free content anyone can use, edit and distribute.** Do not copy non-free material. Contributions are licensed CC BY-SA 4.0 (and GFDL).
4. **Editors should treat each other with respect and civility.** Assume good faith, even in disagreement.
5. **Wikipedia has no firm rules.** Rules are approximations of principles; use judgment, and the spirit of a rule beats the letter. This is "Ignore all rules" (WP:IAR) and it is not permission to override the core content policies casually.

---

## 3. The three core content policies

They work together and should be read together. A neutral article must also be verifiable and free of original research.

### 3.1 Verifiability (WP:V): "verifiability, not truth"

- Content must be backed by a **published reliable source** that readers can check. Being true is not enough for inclusion.
- **Burden of evidence (WP:BURDEN):** whoever adds or restores material must supply the source. Unsourced material may be removed; a good-faith removal should not be restored without a source.
- Everything **challenged or likely to be challenged** needs an inline citation. Direct quotations, statistics, contentious claims, and claims about living people always do.
- Sources need not be online, free, or English, but should be accessible in principle. Cite the original-language source if it is the best one; quote or translate carefully.
- **Self-published sources** are generally unacceptable, with narrow exceptions (WP:ABOUTSELF): material by the subject about themselves is usable if it is not unduly self-serving, makes no claims about third parties, is not about events outside the subject's direct knowledge, is not doubtful in authenticity, and does not make up the main basis of the article.
- **Wikipedia and its mirrors are not reliable sources** (WP:CIRCULAR). Do not cite other Wikipedia articles.
- Verifiability is a **minimum** requirement, not a guarantee of inclusion.

### 3.2 No original research (WP:NOR)

Not allowed: unpublished facts, theories, arguments, ideas, analysis, or synthesis.

- **Synthesis (WP:SYNTH):** do not combine source A and source B to reach a conclusion that neither source states.
- **Primary sources** (documents, records, court filings, raw data, original studies, interviews, the subject's own statements) may be used carefully for straightforward, descriptive facts that any educated reader can verify. Do not interpret, evaluate, or analyze them yourself; do not use them to establish notability.
- Prefer **secondary sources** (which analyze or interpret primary ones) for claims, evaluations, and context. Tertiary sources (encyclopedias, textbooks) are fine for overviews.
- **Routine calculations** and obvious translations are not OR. Original images are allowed if they do not illustrate original ideas; original *images* depicting unpublished ideas are not.
- Your own knowledge, observations, experience, interviews you conducted, or "common sense" are not sources.
- Paraphrase faithfully. Do not distort what a source says; do not cherry-pick.

### 3.3 Neutral point of view (WP:NPOV)

Represent **fairly, proportionately, and without editorial bias** all significant views published in reliable sources.

Principles:
1. **Avoid stating opinions as facts.** Attribute opinions in the text ("According to X, ...") instead of speaking in Wikipedia's voice (WP:WIKIVOICE).
2. **Do state facts as facts.** Do not use "some say", "critics claim" for matters that are uncontested or well established. Avoid false balance between a mainstream view and a fringe one.
3. **Avoid stating seriously contested assertions as facts.** Use in-text attribution.
4. **Avoid stating facts as opinions.** Do not hedge well-documented facts.
5. **Prefer nonjudgmental language.** Describe disputes; do not engage in them. No editorial stance, no praise or condemnation.
6. **Due weight (WP:DUE / WP:UNDUE):** space and prominence should be proportional to how prominent each view is in the body of reliable sources, not equal time for everything. Do not give fringe theories parity with mainstream scholarship (WP:FRINGE, WP:PSCI for science).
7. **Balance and aspects (WP:BALASP):** do not let one aspect or one kind of detail dominate. Be wary of "criticism" and "controversy" sections that become a dumping ground (consider integrating the material instead).
8. **Biased sources are allowed** when properly attributed and weighed; biased *editors* are the problem, not biased sources per se (WP:BIASED).
9. **Avoid loaded or contentious labels** (WP:LABEL) such as "terrorist", "cult", "racist", "extremist", "pseudoscience" unless widely and consistently used by reliable sources; even then consider attribution.
10. **Neutral does not mean empty.** Cover disagreements; do not delete a viewpoint because you dislike it.
11. **Writing for the enemy** is encouraged: present opposing views in terms their best proponents would accept as accurate.
12. **Recentism (WP:RECENTISM):** do not overweight recent events at the expense of long-term perspective.
13. **Article and section titles, image selection, and wording choices** can all introduce bias.
14. **Neutrality is non-negotiable** and cannot be overridden by editor consensus. If it conflicts with a local preference, neutrality wins.

---

## 4. Biographies of living persons (WP:BLP): strictest rules

Applies to **all** content about living (or recently deceased, roughly within six months to two years, as judged by the context) people, including talk pages, user pages, and mentions in other articles.

- **Remove immediately**, without waiting for discussion, any contentious material about a living person that is unsourced or poorly sourced. The three-revert rule does not apply to such removals (WP:3RRBLP).
- Be **conservative**: do no harm. Err toward removal when in doubt.
- Use high-quality **reliable secondary sources**. Do not use tabloids, self-published blogs, or social media as the basis for contentious claims.
- **Privacy (WP:BLPPRIVACY):** do not publish non-public personal data (home addresses, phone numbers, unpublished birth dates, private relationships) unless widely published by reliable sources and relevant. Respect "outing" rules.
- **Crime (WP:BLPCRIME):** for people not convicted, be extremely cautious; presume innocence; in many cases omit allegations unless widely reported and relevant. Be careful with arrests, accusations, and "alleged" language.
- **Low-profile individuals (WP:NPF)** and **people notable for only one event (WP:BLP1E)** deserve extra protection; many should not have standalone articles.
- **Categories and descriptors** (religion, sexual orientation, ethnicity, health conditions, criminality) require self-identification **and** relevance to the subject's notability for living persons (WP:BLPCAT).
- **Name changes and gender identity:** follow MOS:GENDERID: use a person's latest self-identification for name and pronouns, including in past contexts, in general.
- **Subjects** may contact the project; never pressure or threaten them. Never include material derived from hacked or stolen sources without careful consideration of reliable-source reporting.
- **Edit-warring** over BLP content can lead to quick administrative sanctions.
- **Photographs** of living people must be properly licensed; do not use non-free images where a free one could reasonably be created.
- **Special case: contentious topics (WP:CT)** impose extra restrictions on certain areas (for example, specific political, nationalist, and biographical areas). Some require extended-confirmed status to edit (WP:ECR) or enforce 1RR. Check the page's notices before editing.

---

## 5. Copyright, plagiarism, and licensing

- **Do not copy** text, images, or media from non-free sources. Even with a citation, copying is a violation (WP:COPYVIO).
- **Close paraphrasing (WP:CLOP)** is also a problem: changing a few words or following the same structure and phrasing is not enough. Put ideas in genuinely new words.
- **Direct quotes** must be short, attributed, in quotation marks, and used sparingly (WP:QUOTE, WP:NFCCP for non-free text). Quote only when the exact wording matters; do not quote what you can summarize.
- **Public domain material** may be used if truly in the public domain, with attribution as appropriate (check the country-specific rules; "free on the internet" does not mean free to reuse).
- **Compatible licenses:** content must be compatible with CC BY-SA 4.0. Reuse of Wikipedia text from another Wikipedia article requires attribution in the edit summary (WP:CWW); translations need attribution to the source article.
- **Plagiarism** is unacceptable even for public-domain text if not attributed; use in-text attribution and citation.
- **Images (WP:IUP):** prefer freely licensed or public-domain images, ideally uploaded to Wikimedia Commons. **Non-free content (WP:NFCC)** is allowed only if all ten criteria are met, in short: (1) no free equivalent exists or could reasonably be created; (2) it respects the owner's commercial opportunities; (3) minimal use, both in number of items and in extent (for example, low resolution and short excerpts); (4) previously published outside Wikipedia; (5) meets general content standards; (6) meets any media-specific policy; (7) used in at least one article; (8) contextual significance, meaning it significantly increases readers' understanding and its omission would be detrimental; (9) appears only in the article namespace (not user pages, drafts or templates); and (10) has a proper description page with source, copyright tag, and a specific rationale for each use. Decorative use never qualifies.
- **AI-generated images** are subject to Wikipedia's image use policy and generally should not be used to depict real people or events as if factual.
- **Never** assume a creator's permission, an email, or a "free to share" claim is sufficient; use the Wikimedia permission process (VRT) where needed.

---

## 6. Notability (WP:N): does the topic deserve its own article?

A topic is generally presumed notable if it has received **significant coverage in reliable sources that are independent of the subject** (the General Notability Guideline, WP:GNG).

- **Significant:** more than a passing mention or trivial listing; the source addresses the topic directly in detail.
- **Reliable:** editorial oversight and a reputation for accuracy (section 7).
- **Independent:** not the subject itself, its publisher, its employer, a press release, a sponsored article, or content derived from them.
- **Sources** (plural): multiple sources are generally expected. One source is rarely enough.
- **Secondary:** coverage should include secondary analysis, not just primary documentation.
- Notability is about the **existence** of suitable sources, not the number currently in the article; but if you cannot name any, the article will probably be deleted.
- **Subject-specific notability guidelines (SNGs)** adapt the standard for particular areas (people: WP:BIO; organizations and companies: WP:NCORP; creative works, films, books, music: WP:NBOOK, WP:NFILM, WP:NMUSIC; academics: WP:NPROF; sports: WP:NSPORT; geographic features, events, web content, and more). Passing an SNG or the GNG is typically needed; for companies and organizations the bar is higher and requires in-depth independent coverage (WP:CORPDEPTH, WP:ORGCRIT), and promotional coverage does not count.
- **Inherited notability** does not exist: being related to, employed by, or working with a notable person or organization is not enough (WP:NOTINHERITED).
- **Not enough:** popularity, number of social-media followers, awards of minor or non-notable groups, existence, search-engine hits, or "importance" in the author's opinion.
- **Events (WP:NEVENT, WP:NOTNEWS):** need lasting, in-depth, diverse coverage, not a brief burst of news (WP:SUSTAINED, WP:LASTING).
- **Notability is not a content limit** (WP:NNC): the rules about what to include in an article are separate (WP:DUE).
- Alternatives when a topic is not notable: **merge** into a broader article, **redirect**, mention inside another article (WP:NOPAGE), or draft more sources first. Use **Articles for Creation (WP:AFC)** if you are new, have a conflict of interest, or are unsure.

### 6.1 How to assess notability (work in this order)

1. **Pin down the subject and its type** (person, company, event, creative work, place...). Different types have different guidelines.
2. **List the candidate sources and test each** for: significant coverage, reliability, independence, and being secondary. Name the strongest three.
3. **Collapse duplicates before counting.** Wire-service copy, rewrites by the same author, and stories derived from one press release count as one source, or zero if they are only a press release.
4. **If the general guideline is met, notability is presumed.** If not, check the matching subject-specific guideline, then check exclusions that can still defeat a presumption (WP:NOT, WP:BLP1E, WP:NOTNEWS, the stricter organization tests).
5. **Give a verdict:** likely notable, borderline, or unlikely, with the best sources named and the gaps stated. If borderline, say what kind of coverage would change the answer, and suggest drafting, Articles for Creation, or merging into a broader article.

### 6.2 Source-counting traps

- **Churnalism:** many outlets, one press release. Counts as one source at most.
- **Routine coverage:** announcements, product launches, funding rounds, scheduled events, routine results. Expected events do not show significance.
- **Databases and profiles** (IMDb, Discogs, MusicBrainz, WorldCat, LinkedIn, Crunchbase, directories): they show existence, not attention from independent sources.
- **Primary documents** (filings, annual reports, CVs, court records, company websites): useful to verify plain facts, but they do not establish notability.
- **Interviews:** the subject's own words are not independent. Independent analysis around the interview may be.
- **Counting articles or search hits:** quality beats quantity; ten in-depth independent features outweigh a hundred rewrites (WP:GOOGLEHITS).
- **Local-only coverage** for a topic that claims wider significance; **passing mentions** in books or articles about something else.

### 6.3 Weak versus strong arguments (useful when helping with deletion discussions)

Weak: "related to someone notable" (WP:NOTINHERITED); "famous" or "important"; "other similar articles exist" (WP:OTHERSTUFFEXISTS); "has an IMDb or LinkedIn page"; "lots of search hits"; "popular online"; "well written"; "I like it"; "it has an article in another language edition"; "sources exist" without naming any (see WP:NEXIST); and, for deletion, "poorly written" (a fixable problem, not a notability one). See WP:ATA for the community's list of arguments to avoid.

Strong: name specific independent, reliable sources with significant coverage; show a specific criterion of the relevant subject-specific guideline; or show concretely why the available sources fail independence or significance.

Also remember: notability is about the subject, not the article's quality (WP:CONTN); it is not temporary once established (WP:NTEMP); and it rests on sources that exist, not only those already cited (WP:NEXIST).

### 6.4 Do not recite subject-specific criteria from memory

The subject-specific guidelines (sports, music, academics, geography, numbers and others) are revised often, and popular summaries get details wrong. For example, sports notability was substantially tightened in 2022 so that merely having played or competed no longer settles it on its own (as I understand it; check WP:NSPORT). When a verdict depends on a specific criterion, paraphrase the principle, say which guideline applies, and tell the user to read its current text.

---

## 7. Reliable sources (WP:RS) and how to judge them

**Reliable** sources have editorial oversight, fact-checking, a reputation for accuracy, and (usually) a published correction policy. **Context matters** (WP:CONTEXTMATTERS): a source can be reliable for one claim and weak for another.

**Generally best:**
- Peer-reviewed journals and academic books from reputable university presses or established publishers.
- Reputable mainstream news outlets for news (reporting, not opinion).
- Specialist reference works, textbooks, and high-quality tertiary sources.
- For **medicine (WP:MEDRS):** systematic reviews, meta-analyses, major medical society guidelines, textbooks from academic publishers. Avoid single studies, press releases, primary studies for biomedical claims, and news reports on medical findings.
- For **history, science, and other specialty areas:** the highest-quality scholarship; beware of outdated sources.

**Use with caution or attribution:**
- Opinion pieces, editorials, columns (usable for attributed opinion, not facts; WP:RSOPINION).
- News published in the immediate aftermath of an event (WP:RSBREAKING); headlines are not reliable (WP:HEADLINES).
- Partisan or advocacy sources; state media of authoritarian regimes (for the state's own claims, attribute).
- Press releases and company self-descriptions (primary and non-independent).
- Sources that run sponsored content or "advertorials".

**Generally unreliable:**
- Self-published content: personal blogs, forums, social media posts, most wikis (including Wikipedia), "user-generated" content such as IMDb user content and Genius, content farms, and press-release aggregators.
- Sources with a poor reputation for fact-checking (check the Perennial Sources list, WP:RSP, which summarizes community consensus on frequently discussed sources and is updated over time).
- **AI chatbot output** (WP:RSPLLM): not a reliable source, and LLM-suggested citations may be wrong or fabricated. Always open and read the source yourself.
- Anything you cannot verify exists.

**Source evaluation checklist:** Who published it? Who wrote it? Is it independent of the subject? Is it primary, secondary, or tertiary? Is there editorial oversight? Does it say what you claim it says? Is it up to date? Does it have a conflict of interest or a sponsorship? Is it widely cited by other reliable sources?

---

## 8. What Wikipedia is NOT (WP:NOT)

Wikipedia is **not**:

- **A dictionary, thesaurus, or usage guide** (WP:NOTDICT): articles are about topics, not words.
- **A newspaper (WP:NOTNEWS):** not a place for breaking-news reports, routine coverage, celebrity gossip, or every news event.
- **A soapbox, battleground, or advocacy platform (WP:SOAP):** no propaganda, recruiting, campaigning, or personal essays.
- **An advertising or promotional medium (WP:PROMO):** no marketing language, product placement, resumes, spam, or press-release-style writing. Even factually accurate content can be promotional.
- **A crystal ball (WP:CRYSTAL):** no speculation about future events unless notable and already documented by reliable sources; do not predict.
- **An indiscriminate collection of information (WP:NOTINDISCRIMINATE):** not a mere list of facts, lyrics, quotes, statistics, or trivia; plot summaries should be concise and not the sole content (WP:NOTPLOT).
- **A directory (WP:NOTDIRECTORY):** not a phone book, a catalog, a price list (WP:NOTCATALOG), a travel guide (WP:NOTGUIDE), or a listing of every location, event, or person.
- **A how-to manual, textbook, or instruction guide (WP:NOTHOWTO):** describe, do not instruct.
- **A social network, a webhost, or a personal website** (WP:NOTWEBHOST, WP:NOTSOCIAL): user pages cannot be used as blogs or for unrelated content.
- **A memorial (WP:NOTMEMORIAL), a genealogical or family-history repository, or a place for personal tributes.**
- **A scandal sheet (WP:NOTSCANDAL):** coverage of controversies must remain proportionate and neutral.
- **A democracy or bureaucracy (WP:NOTDEMOCRACY, WP:NOTBUREAUCRACY):** consensus is built on arguments grounded in policy, not on votes alone.
- **Censored (WP:NOTCENSORED):** content is not removed because it is offensive to some, provided it meets the policies; this does not permit gratuitous shock content.
- **A publisher of original thought, research, or analysis** (see WP:NOR).

---

## 9. Article structure, titles, and the Manual of Style (MOS)

### 9.1 Titles (WP:AT)
- Use the **common name** in reliable sources (WP:COMMONNAME), balanced against **recognizability, naturalness, precision, concision, and consistency** (WP:CRITERIA).
- Sentence case; no unnecessary qualifiers, no articles ("a/the") at the start, no all-caps unless standard; singular nouns unless usual plural; no abbreviations unless the acronym is the common name.
- Disambiguate only when needed, using parenthetical qualifiers (WP:NCDAB).
- Neutral titles, no editorial or loaded wording.

### 9.2 Lead section (MOS:LEAD)
- A concise **summary of the article** that stands alone, usually 1 to 4 paragraphs, in proportion to article length.
- First sentence defines the topic, its type or category, and its significance; bold the title (and common alternative names) the first time, unless it is a descriptive title.
- Summarize the **body**, not new content; claims in the lead should also appear and be sourced in the body (citations in the lead are optional if cited in the body but required for contentious claims and quotations).
- No excessive detail, no teaser style, no "this article is about".

### 9.3 Layout (MOS:LAYOUT)
Typical order: lead, body sections, **See also**, **Notes**, **References**, **Further reading**, **External links**; navigation templates and categories at the end. Use hatnotes for disambiguation (WP:HATNOTE). Infoboxes summarize key facts, appear at the top, and must be consistent with the article text (WP:INFOBOX).

### 9.4 Headings (MOS:HEAD)
Sentence case; unique; no links in headings, no starting with "the"; avoid single-subsection splits; avoid repeating the title; keep them neutral; descriptive but concise.

### 9.5 Tone and wording (MOS:TONE, MOS:WTW)
- Formal, dispassionate, encyclopedic. No second person ("you"), no first-person singular ("I"), no rhetorical questions, no exclamations, no emotive language, no slang or contractions in general text (except in quotations).
- **Words to watch (MOS:WTW):** *peacock terms* (legendary, world-class, iconic, visionary), *weasel words* ("some say", "it is believed", "many people think"), *editorializing* ("notably", "interestingly", "it should be noted"), *doubt-casting verbs* ("claimed", "admitted", "revealed", "confessed", "denied" where "said" or "stated" works), *expressions of doubt*, and *unsupported attributions* ("critics argue" without naming any).
- **Time-relative language (MOS:RELTIME):** avoid "currently", "recently", "now", "this year"; use dates or "as of" with a specific date for facts that change (WP:ASOF).
- **Avoid words like "many", "few", "majority"** without numbers or sources when precision is possible.
- **Avoid jargon**; explain technical terms or link to them (WP:TECHNICAL: write for a general audience).
- **Prefer plain, direct language; avoid indefinite filler.**
- Avoid mirror or repetitive phrasing and over-long sentences.

### 9.6 Dates, numbers, units, and punctuation
- **Dates (MOS:DATE):** use a consistent format within an article, either "5 March 2024" or "March 5, 2024", depending on national ties; no ordinals ("5th") or "of"; spell out months in prose; avoid ambiguous numeric formats; use full years, no apostrophe abbreviations.
- **Numbers (MOS:NUM):** spell out zero to nine, use digits for 10 and above, with exceptions for measurements, percentages, and comparisons; non-breaking spaces between number and unit; use commas for thousands in numbers of 5 digits or more (4-digit numbers optional but consistent); decimals with a point.
- **Units (MOS:UNITS):** SI units are primary in most scientific contexts; provide conversions where needed (US topics: US customary first, and vice versa; UK topics: mixed per convention).
- **Quotation marks and punctuation (MOS:PUNCT, MOS:QUOTE):** use straight quotation marks consistently; **logical quotation**: punctuation goes inside quotation marks only if it belongs to the quoted material. Block-quote long quotations (generally four or more lines) without quotation marks. Do not alter quotations except for minor, flagged fixes.
- **Dashes (MOS:DASH):** hyphens for compounds, en dashes for ranges and relationships, em dashes sparingly and unspaced.
- **Capitalization (MOS:CAPS):** minimal; capitalize only proper names and what reliable sources consistently capitalize; do not capitalize for emphasis.
- **Italics (MOS:ITALIC):** for titles of major works, foreign words not in common English use, scientific names, and emphasis only rarely; do not use bold for emphasis outside specific cases (the lead's title, defined terms).
- **Abbreviations and acronyms (MOS:ABBR):** spell out at first use, with the abbreviation in parentheses.
- **English variety (MOS:ENGVAR, MOS:TIES):** follow one variety consistently, using the variety that has strong national ties to the topic (for example, British English for UK topics), or the variety of the first major contributor if no ties exist; do not change varieties without consensus.
- **Gender-neutral language and inclusive wording (MOS:GENDER, MOS:GENDERID):** use the pronouns and names a person uses; use gender-neutral language where precision is not needed.
- **Biographies (MOS:BIO):** full name in the first sentence, dates of birth and death, nationality, occupation; avoid unnecessary personal details; use surname afterward (not first names or titles).

### 9.7 Links (WP:LINK, WP:OVERLINK)
- Link to relevant articles at first meaningful mention; do not overlink common terms, or link the same term repeatedly, or make "sea of blue" clusters (WP:SEAOFBLUE).
- **No Easter eggs (WP:EGG):** link text should reveal where the link leads.
- External links belong in the "External links" section, not the body, and must meet WP:EL (no spam, no commercial links, no content that breaches copyright).
- Avoid redlinks to non-notable topics; check for existing articles and redirects first.

### 9.8 Lists, tables, images, captions, accessibility
- **Lists (MOS:LISTS):** use prose for narrative content; use lists for list-like content only; keep list items parallel and consistently punctuated.
- **Tables (WP:TABLES, MOS:TABLES):** for tabular data; sortable only when useful; include captions and scopes for accessibility; avoid color as the only distinguishing feature.
- **Images (MOS:IMAGES):** relevant, properly licensed, with captions (MOS:CAPTION) that are concise, informative, and not complete sentences unless they are; alt text for accessibility (MOS:ALT); avoid sandwiching text between images; do not stack images; no decorative images; respect right-to-left or left-to-right conventions.
- **Accessibility (MOS:ACCESS):** do not rely on color alone; use proper heading levels; provide alt text; avoid tiny text; use proper list markup; mind screen-reader behavior.

### 9.9 Categories, redirects, disambiguation
- **Categories (WP:CAT):** apply three tests to every category before adding it.
  1. **Verifiable (WP:CATV):** the article itself must show, with sourcing, why it belongs.
  2. **Neutral (WP:CATPOV):** categories carry no annotations or citations, so they must be uncontroversial. Contested labels (for example "criminals" for someone not convicted, or subjective ones like "controversial") belong in a referenced list article, not a category.
  3. **Defining (WP:CATDEF):** reliable sources commonly and consistently use the characteristic to describe the topic (nationality, occupation, genre, location), as opposed to trivial ones (WP:TRIVIALCAT).
  Also: use the most specific category available instead of its parents; keep the number reasonable (avoid category clutter); do not create categories that are subjective, arbitrary, or overly narrow (overcategorization); topic categories are singular and set categories plural; BLP category restrictions apply (WP:BLPCAT).
- **Redirects (WP:REDIRECT):** use for alternative names and plausible search terms; avoid redirects that are confusing, promotional, or cross-namespace without need.
- **Disambiguation (WP:DAB):** for terms with several possible topics; keep entries short with one link each; use hatnotes for two-topic cases.

### 9.10 Splitting, merging, and size
- Consider splitting (WP:SPLIT) when readable prose is very long (guideline: over roughly 8,000 words warrants consideration; over 15,000 words strongly suggests it) and merging (WP:MERGE) when small, overlapping, or non-notable topics fit better within another article.

---

## 10. Citing sources (WP:CITE, WP:REF)

- **Cite inline**, with a footnote after the claim it supports (after punctuation, with no space before the reference marker). Cite each paragraph's key claims; do not rely on a single reference at the end for all content if claims differ.
- **Required:** direct quotes, contentious statements, statistics, and BLP material. **Do not over-cite (WP:OVERCITE)** trivial facts with many redundant references.
- **Reference format:** be consistent. Include author, title, publisher/work, date, URL (if any), access-date for web sources, page numbers for books (WP:PAGENUMBERS), and DOI/ISBN where applicable. Use the existing citation style when editing an established article (WP:CITEVAR) and do not change it without consensus.
- **Archived links (WP:LINKROT):** archive web citations when possible so verification survives dead links; do not delete a dead link just because it is dead.
- **Do not cite** Wikipedia, a mirror, or social media for contentious claims; do not use "citation needed" as a license to leave claims unverified.
- **Reuse a reference** by name rather than duplicating it. Use the `{{cite web}}`, `{{cite news}}`, `{{cite book}}`, and `{{cite journal}}` templates or equivalents, as the article does.
- **Bare URLs** are discouraged; always give a descriptive citation.
- **Quotes in citations** can be added with a quote parameter for context when helpful.
- **Never cite a source you have not read**, and never attribute a claim to a source that does not state it (WP:SOURCETEXT, the "source-text integrity" principle).
- **Foreign-language sources** are fine; give the original title and, where helpful, a translation, and use `language=` parameters.
- **Paywalled** sources are acceptable (WP:PAYWALL); mark them and, if useful, quote a brief supporting passage.

- **Check which sentences a reference really supports.** A single footnote at the end of a paragraph does not automatically support every sentence before it; flag "citation dumping" (one reference covering many distinct claims).
- **Reuse a named reference instead of duplicating it**, and use meaningful names (not purely numeric).
- **Do not remove existing archive links** when editing a citation; add archives rather than replace them.
- **Use the right field for the right thing:** author or `last`/`first` for people, `work` or `website` for the publication, `publisher` for the company behind it, `journal` for journals.
- **Flag gaps honestly** with `{{citation needed}}`, `{{clarify}}` or `{{when}}` rather than quietly leaving unsupported text or inventing a source.
- **Never guess a URL** or fill in a DOI, ISBN, page number, date, or quotation you have not seen.

---

## 11. Editing policy and good practice (WP:EDIT, WP:PRESERVE)

- **Be bold (WP:BOLD)** but careful: improve articles directly; if reverted, discuss rather than repeat (**BRD cycle: Bold, Revert, Discuss**).
- **Preserve (WP:PRESERVE):** fix rather than delete where verifiable content can be improved; but remove unverifiable, unsourced contentious, or promotional text.
- **Use clear edit summaries (WP:ES)** for every edit that is not trivial; mark minor edits only when truly minor (typos, formatting), never for content changes or reverts.
- **Use the sandbox, draft space, or AfC** for new or large works. Do not publish unfinished text to mainspace if it would violate policy.
- **Do not leave articles worse than you found them:** fix as you go; do not introduce unsourced content, broken markup, or promotional language.
- **Check recent changes and talk pages** for consensus before contentious edits.
- **Do not edit articles about yourself, your employer, your clients, your family, or your organization** when you have a conflict of interest, except for uncontroversial fixes (typos, vandalism, obviously incorrect facts) on talk pages or via edit requests (WP:COI, WP:COIREQ).
- **Paid editing (WP:PAID):** you must disclose your employer, client, and affiliation (Wikimedia Terms of Use, on your user page, talk pages, and edit summaries as needed). Paid editors should not edit directly where they have a COI; they should propose edits on the talk page or use AfC.
- **Ownership (WP:OWN):** no one owns an article; do not treat pages as personal property.
- **Do not game the system (WP:GAME)**, make point-y edits (WP:POINT), sock-puppet (WP:SOCK), or use multiple accounts deceptively.
- **Do not canvass (WP:CANVASS):** do not recruit like-minded editors to tilt a discussion; notices must be neutral, limited, and open.
- **Edit warring (WP:EW):** repeatedly overriding another editor's changes is prohibited, even if you are right. **Three-revert rule (WP:3RR):** do not make more than three reverts on a single page within 24 hours (exceptions: obvious vandalism, BLP violations, copyright violations, banned users); edit-warring can occur with fewer reverts.
- **Vandalism (WP:VAND):** deliberate attempts to degrade the encyclopedia. Revert, warn, and report as appropriate; do not confuse a good-faith mistake with vandalism (assume good faith).
- **Bots and automated tools (WP:BOT, WP:MEATBOT):** high-speed or semi-automated editing needs approval; each edit remains the editor's responsibility.

---

## 12. Consensus, discussion, and dispute resolution

- **Consensus (WP:CONSENSUS)** is decided by the quality of arguments grounded in policy, not by headcount or voting; it can change.
- **Talk pages (WP:TPG):** discuss content, not contributors; stay on topic; start new topics at the bottom; sign with four tildes (`~~~~`); indent replies with colons; do not edit or delete others' comments except for narrow exceptions (retract your own words with strikethrough instead of deleting them, and mark finished threads with templates such as {{done}} or {{resolved}}); do not use talk pages as forums (WP:NOTFORUM) for general discussion of the subject. Discuss article content on the article's talk page, not on a user's talk page; use user talk pages for personal messages.
- **Civility (WP:CIV), no personal attacks (WP:NPA), assume good faith (WP:AGF), do not bite newcomers (WP:BITE).**
- **Harassment (WP:HARASS):** no stalking, hounding, outing (WP:OUTING), threats, or repeated unwelcome contact; **no legal threats (WP:NLT)**: threats of legal action are incompatible with editing and typically result in blocks until withdrawn.
- **Escalation path:** discuss on the article talk page, then seek input from relevant WikiProjects or noticeboards (neutral notice), use a **third opinion (WP:3O)**, **Requests for Comment (WP:RFC)**, then formal **dispute resolution (WP:DR)**, and finally administrators and arbitration for conduct matters.
- **Noticeboards:** Reliable Sources (RSN), Neutral Point of View (NPOVN), BLP (BLPN), Conflict of Interest (COIN), Original Research (NORN), Fringe Theories (FTN), Administrators (ANI/AN), and others.
- **Blocking and sanctions** are preventive, not punitive; policy violations can lead to warnings, topic bans, blocks, or bans.
- **Usernames (WP:USERNAME):** no promotional or organizational names (shared accounts are not allowed), no offensive or misleading names, no impersonation.

---

## 13. Deletion, drafts, and quality control

- **Speedy deletion (WP:CSD)** is only for narrow, clear-cut cases. Common criteria: G1 (patent nonsense), G2 (test pages), G3 (vandalism and hoaxes), G4 (recreation of a page deleted by discussion), G5 (creation by banned or blocked users), G7 (author request), G10 (attack pages), G11 (unambiguous advertising or promotion), G12 (unambiguous copyright infringement), G13 (abandoned drafts after 6 months), G14 (unnecessary disambiguation page), **G15 (LLM-generated pages without human review)**. Article-specific criteria include A1 (no context), A2 (foreign-language duplicate), A3 (no content), A7 (no credible indication of importance or significance for people, animals, organizations, web content, events), A9 (unremarkable musical recording by a non-notable artist), A10 (recently created duplicate), and A11 (obviously invented). Check the live CSD page; criteria are revised.
- **Proposed deletion (WP:PROD):** for uncontroversial deletions; removal of the tag by anyone contests it; waiting period (typically 7 days). **BLP PROD (WP:BLPPROD)** for unsourced biographies of living people.
- **Articles for Deletion (WP:AFD):** discussion (typically 7 days) assessed on policy-based arguments; "keep" requires showing that suitable sources exist (WP:BEFORE: nominators must first search for sources).
- **Draftification (WP:DRAFTIFY)** moves a not-ready article to draft space; **Articles for Creation (WP:AFC)** is the review route for new users, COI editors, and unsure cases.
- **Cleanup tags** (for example NPOV, unreferenced, COI, notability) should be used with a clear explanation on the talk page, not as drive-by tags.
- **Hoaxes (WP:HOAX)** are among the most serious problems: fabricated or fake-sourced content leads to deletion and sanctions.

---

## 14. Wikimedia-wide values and legal (brief)

- **Terms of Use** (Wikimedia Foundation) govern paid editing disclosure, licensing, and prohibited conduct.
- **Universal Code of Conduct** applies across Wikimedia projects (respect, no harassment, no abuse of power).
- **Privacy:** do not share non-public personal information about other editors (outing) or about living people beyond what is permitted.
- **Legal:** copyright (DMCA and equivalents) is handled by the Foundation; do not post content that violates law (defamation, privacy).
- **Child safety, threats of violence, and self-harm threats** are reported to the Foundation's emergency channels, not discussed on-wiki.

---

## 15. Wikitext quick reference (for authoring non-AI-written human drafts and non-Wikipedia wikis)

```
== Heading ==            === Subheading ===
'''bold'''   ''italic''   [[Article title|display text]]   [https://example.org label]
* bullet     # numbered   : indent (talk pages)
<ref name="a">{{cite web |url= |title= |publisher= |date= |access-date=}}</ref>   <ref name="a" />
{{reflist}}   [[Category:Name]]   #REDIRECT [[Target]]
{{Infobox ...}}   {{main|Article}}   {{see also|Article}}   {{citation needed|date=November 2026}}
~~~~  (signature, talk pages only)
```

---

## 16. Rule index: where to check live rules

Any shortcut `X` below opens at `https://en.wikipedia.org/wiki/X`. This is a starter map of the main pages, not the complete list. The complete, authoritative list is `WP:LPG` (List of policies and guidelines), and the repository's `rules-index.md` and `tools/check_updates.py` track revisions.

**Foundations:** `WP:5P` (Five Pillars), `WP:POLICY` and `WP:LPG` (what policies, guidelines and essays are; the full list), `WP:IAR`

**Content policies:** `WP:NPOV`, `WP:V`, `WP:NOR` (with `WP:SYNTH`, `WP:PRIMARY`), `WP:BLP`, `WP:NOT`, `WP:COPYRIGHT`, `WP:COPYVIO`, `WP:NFCC`, `WP:IUP`, `WP:AT`

**Sourcing and notability:** `WP:RS`, `WP:RSP` (perennial sources), `WP:MEDRS`, `WP:SPS`, `WP:CIRCULAR`, `WP:N` (with `WP:GNG`), `WP:BIO`, `WP:NCORP`, `WP:NSPORT`, `WP:NMUSIC`, `WP:NPROF`, `WP:NFILM`, `WP:NBOOK`, `WP:GEOLAND`, `WP:FRINGE`

**Style and structure:** `WP:MOS`, `MOS:LEAD`, `WP:LAYOUT`, `WP:CITE`, `WP:CITEVAR`, `WP:LINKROT`, `WP:EL`, `WP:CAT`, `WP:DAB`, `WP:REDIRECT`, `WP:INFOBOX`, `WP:SIZE`, `WP:MERGE`, `WP:SPLIT`, `MOS:ENGVAR`

**AI and automation:** `WP:NEWLLM`, `WP:LLM`, `WP:BOTPOL`

**Conduct and disputes:** `WP:CIVIL`, `WP:NPA`, `WP:AGF`, `WP:BITE`, `WP:HARASS`, `WP:OUTING`, `WP:NLT`, `WP:EW`, `WP:3RR`, `WP:OWN`, `WP:CANVASS`, `WP:SOCK`, `WP:COI`, `WP:PAID`, `WP:USERNAME`, `WP:DISRUPT`, `WP:NOTHERE`, `WP:CON` (consensus), `WP:DR`, `WP:RFC`, `WP:3O`, `WP:TPG`, `WP:CT` (contentious topics), `WP:ECR`, `WP:BLOCK`, `WP:BAN`, `WP:PROTECT`, `WP:VAND`

**Deletion and drafts:** `WP:DEL`, `WP:CSD`, `WP:PROD`, `WP:BLPPROD`, `WP:AFD`, `WP:ATD`, `WP:BEFORE`, `WP:DRAFTIFY`, `WP:AFC`

**Beyond English Wikipedia:** Wikimedia Terms of Use (foundation.wikimedia.org), Universal Code of Conduct (meta.wikimedia.org), and Meta-Wiki's "Artificial intelligence/Policies by project" for other editions. Each language edition has its own rules (see section 0).

If a shortcut does not open, search Wikipedia for the topic; shortcuts can be renamed or retargeted. Do not invent a shortcut.

---

## 17. Audit procedure and output format

An audit **reads and reports; it does not edit.** If the user then wants to act on it, they make the edits themselves (in their own words), ideally in a fresh pass after reviewing the report.

### 17.1 Step zero: is this a biography of a living person?

If yes, do the **BLP spotlight** before anything else. If you find a serious violation, report it first and say the rest of the audit is secondary.

| Check | What to look for | Action |
|---|---|---|
| Contentious claims | Allegations, legal disputes, negative personal details | Needs multiple high-quality independent sources; flag single-source claims |
| Private information | Home address, phone, email, non-public birth date, family details not in the public record | Remove (WP:BLPPRIVACY) |
| Legal or political framing | Sanctions, bans, security designations, criminal accusations | Attribute to a named source; avoid stating them in Wikipedia's voice |
| Editorial nicknames and superlatives | "Chip queen", "pioneer", "trailblazer" | Attribute to whoever coined it, or drop |
| Harm | Could this fact cause real-world harm and is it non-essential? | Consider omitting (WP:BLP, WP:BLPPRIVACY) |

### 17.2 Then work in this order

1. **Notability and scope** (section 6): significant, independent, reliable coverage? Standalone article warranted?
2. **Sourcing:** every challenged or likely-to-be-challenged claim cited? Sources reliable, independent, verifiable? Any citation dumping, bare URLs, dead links, self-published or primary-only sourcing?
3. **Claim-by-claim check** (see 17.3), for claims whose sources the user has given you or you can actually read.
4. **Original research and synthesis.**
5. **Neutrality and weight:** loaded or promotional wording, undue weight, false balance, missing significant views. Scan for peacock terms, weasel words, speculation ("it is likely that", "may have been"), and essay-style conclusions ("a testament to", "speaks to his").
6. **Copyright:** verbatim or closely paraphrased passages; image licensing.
7. **Structure and style:** lead summarizes the body; sections fit the article type (for a living person, do not demand "Later life" or "Legacy" sections); infobox consistent with the text and only filled with sourced fields; short description uses correct demonyms (for example "Chinese businesswoman", not "China businesswoman"); categories pass the three tests; open maintenance tags noted.
8. **Conduct and process flags:** conflict of interest, paid editing, AI-generated content, canvassing, edit-war risk.

### 17.3 Claim-by-claim verdicts

Use exactly one verdict per claim:

- **confirmed:** a reliable source you have read supports it, and the wording is neutral.
- **contradicted:** a reliable source says otherwise. Name the source and the passage in your own words, and say what the source supports instead.
- **npov_or:** the underlying fact may be fine, but the framing is editorial, speculative, or the editor's own interpretation. Suggest a plain factual restatement.
- **unverifiable:** no source found, or the cited source cannot be accessed. Suggest a citation-needed flag or removal.
- **mixed:** the sentence combines parts with different verdicts; split them.

**Never mark anything "confirmed" unless you have actually read the source text.** If you could not read it, the verdict is "unverifiable (not checked)", and you say so.

### 17.4 Report format

| # | Location | Rule (shortcut) | Problem | Priority | Suggested fix (for the human to apply in their own words) |
|---|---|---|---|---|---|

**Priority:** *P0* = factual error, BLP problem, copyright problem, serious NPOV or promotion, likely deletion. *P1* = structure, missing sourced content, weak sourcing, would be tagged or reverted. *P2* = style and formatting.

End with: overall verdict (ready / needs work / likely to be deleted), the top three actions, and everything you could not verify.

If the user wants a machine-readable version, offer a list of tasks in this shape (one object per issue, ordered by priority and dependency):

```json
{"id": "t1", "priority": "P0", "type": "contradicted|npov_or|unverifiable|structure|style|bio_privacy",
 "location": "Early life, sentence 2", "rule": "WP:V", "problem": "...", "suggestion": "...", "depends_on": []}
```

---

## 18. Pre-submission checklist (give to the user)

- [ ] I can name at least 3 independent, reliable, significant secondary sources.
- [ ] Every claim that could be challenged is cited, and I read each source.
- [ ] Nothing is copied or closely paraphrased; quotes are short, marked, and attributed.
- [ ] Wording is neutral; opinions are attributed; weight matches the sources.
- [ ] Any living person mentioned is covered with extra caution (BLP).
- [ ] No promotional language; no puffery; no "currently/recently".
- [ ] The lead summarizes the body; headings are in sentence case; categories are defining.
- [ ] I have disclosed any conflict of interest or payment.
- [ ] I wrote the text myself (English Wikipedia currently prohibits LLM-generated content).
- [ ] I have written a clear edit summary and checked the live policy pages.

---

## 19. Behavior rules for the assistant

1. **Never say or imply that you know every Wikipedia rule or that this file is complete.** Say it is a digest, and check live pages (section 0.1) when it matters.
2. **Establish the target edition or wiki first (section 0).** Never present English Wikipedia's rules as universal.
3. Be accurate before being comprehensive: if unsure, say so and point to the live page. Do not recite subject-specific notability criteria or numeric thresholds from memory (section 6.4).
4. Cite rule shortcuts (for example `WP:SYNTH`) so the user can verify.
5. Distinguish **policy** (broadly accepted, normally followed), **guideline** (best practice, exceptions allowed), and **essay** (opinion, no binding force); do not present essays as rules.
6. Do not give legal advice on defamation or copyright; recommend professional counsel or the Foundation's legal contacts for serious issues.
7. Never help evade rules: no sockpuppetry, undisclosed paid editing, canvassing, hiding COI, laundering AI text, or faking sources.
8. Never write promotional or reputation-management copy intended for Wikipedia mainspace.
9. Keep tone encouraging toward newcomers (WP:BITE) while being honest about problems.
10. Keep this skill's own limits in view: it is a digest as of late 2026 and Wikipedia's rules evolve.
